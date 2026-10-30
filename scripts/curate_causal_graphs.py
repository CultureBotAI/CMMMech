#!/usr/bin/env python3
"""Curate causal_graphs and mechanism protein_examples on CMMMech records with atomic history minting.

Addresses infrastructure task cmmmech-infra-0004:
- Enforces canonical top-level key ordering on CriticalMineralRecord mappings so
  `causal_graphs` is always serialized immediately after `mechanisms` and before
  `curation_history` and `history_refs`.
- Enforces canonical key ordering on Mechanism mappings so `protein_examples` is
  serialized immediately after `organisms` and before `evidence` and `observations`.
- Applies structured YAML/JSON patch payloads for `causal_graphs`,
  `mechanism_protein_examples`, and optional supporting `sources`.
- Validates the updated record via `cmmmech.validation.validate_record` prior to
  minting history or mutating the record file on disk.
- Atomically mints a canonical `HistoryRecord` sidecar via `cmmmech.history.cmd_new`
  and appends the matching `curation_history` event and `history_refs` reference.
"""

from __future__ import annotations

import argparse
import contextlib
import copy
import io
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from cmmmech.history import cmd_new as history_cmd_new  # noqa: E402
from cmmmech.history import validate_references  # noqa: E402
from cmmmech.validation import read_record, validate_record  # noqa: E402

CANONICAL_RECORD_KEYS: tuple[str, ...] = (
    "id",
    "name",
    "material_kind",
    "ima_symbol",
    "polymorph_or_grade",
    "description",
    "identifiers",
    "sources",
    "criticality",
    "mechanisms",
    "causal_graphs",
    "curation_history",
    "history_refs",
)

CANONICAL_MECHANISM_KEYS: tuple[str, ...] = (
    "id",
    "name",
    "process",
    "description",
    "context",
    "microbial",
    "organisms",
    "protein_examples",
    "evidence",
    "observations",
)


def order_mapping_keys(mapping: dict[str, Any], canonical_keys: tuple[str, ...]) -> dict[str, Any]:
    """Return a new dict with keys ordered according to canonical_keys, preserving extras at end."""
    ordered: dict[str, Any] = {}
    for key in canonical_keys:
        if key in mapping:
            ordered[key] = mapping[key]
    for key, value in mapping.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def order_record_keys(record: dict[str, Any]) -> dict[str, Any]:
    """Order top-level CriticalMineralRecord keys and nested Mechanism keys canonically."""
    copied = copy.deepcopy(record)
    if isinstance(copied.get("mechanisms"), list):
        copied["mechanisms"] = [
            order_mapping_keys(m, CANONICAL_MECHANISM_KEYS) if isinstance(m, dict) else m
            for m in copied["mechanisms"]
        ]
    return order_mapping_keys(copied, CANONICAL_RECORD_KEYS)


def _upsert_by_key(existing: list[dict[str, Any]], incoming: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    result = [copy.deepcopy(item) for item in existing]
    index_by_id = {item[key]: idx for idx, item in enumerate(result) if isinstance(item, dict) and key in item}
    for item in incoming:
        item_copy = copy.deepcopy(item)
        item_id = item_copy.get(key)
        if item_id in index_by_id:
            result[index_by_id[item_id]] = item_copy
        else:
            if item_id is not None:
                index_by_id[item_id] = len(result)
            result.append(item_copy)
    return result


def _upsert_organisms(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Upsert OrganismRef entries matching by id/ncbi_taxon_id first and falling back to label."""
    result = [copy.deepcopy(item) for item in existing]
    for item in incoming:
        item_copy = copy.deepcopy(item)
        matched_idx: int | None = None
        for key in ("id", "ncbi_taxon_id", "label"):
            val = item_copy.get(key)
            if val is not None:
                for idx, cur in enumerate(result):
                    if isinstance(cur, dict) and cur.get(key) == val:
                        matched_idx = idx
                        break
            if matched_idx is not None:
                break
        if matched_idx is not None:
            result[matched_idx] = item_copy
        else:
            result.append(item_copy)
    return result


def _normalize_mech_field_map(raw: Any, value_key: str) -> dict[str, list[dict[str, Any]]]:
    if isinstance(raw, dict):
        return {str(k): list(v or []) for k, v in raw.items()}
    if isinstance(raw, list):
        out: dict[str, list[dict[str, Any]]] = {}
        for entry in raw:
            if not isinstance(entry, dict) or "mechanism_id" not in entry or value_key not in entry:
                raise ValueError(f"Expected mapping with 'mechanism_id' and {value_key!r}, got {entry!r}")
            out[str(entry["mechanism_id"])] = list(entry[value_key] or [])
        return out
    return {}


def _normalize_node_pe_updates(raw: Any) -> list[tuple[str, str, list[dict[str, Any]]]]:
    updates: list[tuple[str, str, list[dict[str, Any]]]] = []
    if isinstance(raw, dict):
        for key, value in raw.items():
            if isinstance(key, tuple) and len(key) == 2:
                updates.append((str(key[0]), str(key[1]), list(value or [])))
            elif isinstance(value, dict):
                for node_id, pe_list in value.items():
                    updates.append((str(key), str(node_id), list(pe_list or [])))
            elif isinstance(key, str) and ("/" in key or ":" in key):
                sep = "/" if "/" in key else ":"
                graph_id, node_id = key.split(sep, 1)
                updates.append((graph_id, node_id, list(value or [])))
            else:
                raise ValueError(
                    f"Unsupported node_protein_examples key {key!r}; use '<graph_id>/<node_id>', "
                    "nested {graph_id: {node_id: [...]}}, or list of {'graph_id', 'node_id', 'protein_examples'}."
                )
    elif isinstance(raw, list):
        for entry in raw:
            if not isinstance(entry, dict) or "graph_id" not in entry or "node_id" not in entry:
                raise ValueError(
                    f"Expected mapping with 'graph_id', 'node_id', and 'protein_examples', got {entry!r}"
                )
            updates.append(
                (str(entry["graph_id"]), str(entry["node_id"]), list(entry.get("protein_examples") or []))
            )
    return updates


def apply_curation_patch(record: dict[str, Any], patch: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Apply a structured causal_graphs / protein_examples / mechanism patch and return (updated_record, sections)."""
    updated = copy.deepcopy(record)
    touched_sections: list[str] = []

    def _mark_section(section: str) -> None:
        if section not in touched_sections:
            touched_sections.append(section)

    if "ima_symbol" in patch:
        if patch["ima_symbol"] is None:
            updated.pop("ima_symbol", None)
        else:
            updated["ima_symbol"] = patch["ima_symbol"]
        _mark_section("ima_symbol")

    if "polymorph_or_grade" in patch:
        if patch["polymorph_or_grade"] is None:
            updated.pop("polymorph_or_grade", None)
        else:
            updated["polymorph_or_grade"] = patch["polymorph_or_grade"]
        _mark_section("polymorph_or_grade")

    if patch.get("sources"):
        updated["sources"] = _upsert_by_key(updated.get("sources", []), patch["sources"], "id")
        _mark_section("sources")

    mechanisms = updated.get("mechanisms", [])
    mech_by_id = {m["id"]: m for m in mechanisms if isinstance(m, dict) and "id" in m}

    mech_org_map = _normalize_mech_field_map(patch.get("mechanism_organisms"), "organisms")
    mech_ev_map = _normalize_mech_field_map(patch.get("mechanism_evidence"), "evidence")
    mech_obs_map = _normalize_mech_field_map(patch.get("mechanism_observations"), "observations")
    mech_pe_map = _normalize_mech_field_map(patch.get("mechanism_protein_examples"), "protein_examples")

    raw_mech_patches = patch.get("mechanism_patches")
    mech_subpatches: dict[str, dict[str, Any]] = {}
    if isinstance(raw_mech_patches, dict):
        for mech_id, subpatch in raw_mech_patches.items():
            if not isinstance(subpatch, dict):
                continue
            mech_key = str(mech_id)
            mech_subpatches[mech_key] = subpatch
            if "organisms" in subpatch:
                mech_org_map[mech_key] = list(subpatch["organisms"] or [])
            if "evidence" in subpatch:
                mech_ev_map[mech_key] = list(subpatch["evidence"] or [])
            if "observations" in subpatch:
                mech_obs_map[mech_key] = list(subpatch["observations"] or [])
            if "protein_examples" in subpatch:
                mech_pe_map[mech_key] = list(subpatch["protein_examples"] or [])

    if mech_org_map:
        for mech_id, org_list in mech_org_map.items():
            if mech_id not in mech_by_id:
                raise ValueError(f"Unknown mechanism_id in patch: {mech_id!r}")
            target_mech = mech_by_id[mech_id]
            sub = mech_subpatches.get(mech_id, {})
            if patch.get("replace_organisms", False) or sub.get("replace_organisms", False):
                target_mech["organisms"] = copy.deepcopy(org_list)
            else:
                target_mech["organisms"] = _upsert_organisms(target_mech.get("organisms", []), org_list)
        _mark_section("mechanisms")

    if mech_ev_map:
        for mech_id, ev_list in mech_ev_map.items():
            if mech_id not in mech_by_id:
                raise ValueError(f"Unknown mechanism_id in patch: {mech_id!r}")
            target_mech = mech_by_id[mech_id]
            sub = mech_subpatches.get(mech_id, {})
            if patch.get("replace_evidence", False) or sub.get("replace_evidence", False):
                target_mech["evidence"] = copy.deepcopy(ev_list)
            else:
                target_mech["evidence"] = _upsert_by_key(target_mech.get("evidence", []), ev_list, "source_ref")
        _mark_section("mechanisms")

    if mech_obs_map:
        for mech_id, obs_list in mech_obs_map.items():
            if mech_id not in mech_by_id:
                raise ValueError(f"Unknown mechanism_id in patch: {mech_id!r}")
            target_mech = mech_by_id[mech_id]
            sub = mech_subpatches.get(mech_id, {})
            if patch.get("replace_observations", False) or sub.get("replace_observations", False):
                target_mech["observations"] = copy.deepcopy(obs_list)
            else:
                target_mech["observations"] = _upsert_by_key(
                    target_mech.get("observations", []),
                    obs_list,
                    "parameter",
                )
        _mark_section("mechanisms")

    if mech_pe_map:
        for mech_id, pe_list in mech_pe_map.items():
            if mech_id not in mech_by_id:
                raise ValueError(f"Unknown mechanism_id in patch: {mech_id!r}")
            target_mech = mech_by_id[mech_id]
            sub = mech_subpatches.get(mech_id, {})
            if patch.get("replace_protein_examples", False) or sub.get("replace_protein_examples", False):
                target_mech["protein_examples"] = copy.deepcopy(pe_list)
            else:
                target_mech["protein_examples"] = _upsert_by_key(
                    target_mech.get("protein_examples", []),
                    pe_list,
                    "uniprot_accession",
                )
        _mark_section("mechanisms")

    if "causal_graphs" in patch:
        incoming_graphs = patch["causal_graphs"] or []
        if patch.get("replace_causal_graphs", False):
            if incoming_graphs:
                updated["causal_graphs"] = copy.deepcopy(incoming_graphs)
            else:
                updated.pop("causal_graphs", None)
        else:
            updated["causal_graphs"] = _upsert_by_key(
                updated.get("causal_graphs", []),
                incoming_graphs,
                "id",
            )
        _mark_section("causal_graphs")

    node_pe_updates = _normalize_node_pe_updates(patch.get("node_protein_examples"))
    if node_pe_updates:
        graphs = updated.get("causal_graphs", [])
        graph_by_id = {g["id"]: g for g in graphs if isinstance(g, dict) and "id" in g}
        for graph_id, node_id, pe_list in node_pe_updates:
            if graph_id not in graph_by_id:
                raise ValueError(f"Unknown causal_graph id in node_protein_examples: {graph_id!r}")
            graph = graph_by_id[graph_id]
            node_by_id = {n["id"]: n for n in graph.get("nodes", []) if isinstance(n, dict) and "id" in n}
            if node_id not in node_by_id:
                raise ValueError(f"Unknown node_id {node_id!r} in causal_graph {graph_id!r}")
            target_node = node_by_id[node_id]
            if patch.get("replace_node_protein_examples", False) or patch.get("replace_protein_examples", False):
                target_node["protein_examples"] = copy.deepcopy(pe_list)
            else:
                target_node["protein_examples"] = _upsert_by_key(
                    target_node.get("protein_examples", []),
                    pe_list,
                    "uniprot_accession",
                )
            if target_node.get("node_type") == "GENE_OR_PROTEIN" and target_node.get("protein_examples"):
                target_node["protein_grounding_status"] = "GROUNDED"
            mech_ref = graph.get("mechanism_ref")
            if mech_ref and mech_ref in mech_by_id and patch.get("sync_protein_examples_parity", True):
                target_mech = mech_by_id[mech_ref]
                target_mech["protein_examples"] = _upsert_by_key(
                    target_mech.get("protein_examples", []),
                    pe_list,
                    "uniprot_accession",
                )
                _mark_section("mechanisms")
        _mark_section("causal_graphs")

    if patch.get("sync_protein_examples_parity", False) or (
        mech_pe_map and patch.get("sync_protein_examples_parity", True)
    ):
        graphs = updated.get("causal_graphs", [])
        for graph in graphs:
            if not isinstance(graph, dict):
                continue
            mech_ref = graph.get("mechanism_ref")
            if not mech_ref or mech_ref not in mech_by_id:
                continue
            target_mech = mech_by_id[mech_ref]
            mech_pe_by_acc = {
                pe["uniprot_accession"]: pe
                for pe in target_mech.get("protein_examples", [])
                if isinstance(pe, dict) and "uniprot_accession" in pe
            }
            gene_or_protein_nodes = [
                n for n in graph.get("nodes", [])
                if isinstance(n, dict) and n.get("node_type") == "GENE_OR_PROTEIN"
            ]
            node_accs: set[str] = set()
            for node in graph.get("nodes", []):
                if not isinstance(node, dict) or not node.get("protein_examples"):
                    continue
                node_pes = node["protein_examples"]
                changed_node = False
                for idx, node_pe in enumerate(node_pes):
                    acc = node_pe.get("uniprot_accession") if isinstance(node_pe, dict) else None
                    if acc:
                        node_accs.add(acc)
                    if acc and acc in mech_pe_by_acc and node_pe != mech_pe_by_acc[acc]:
                        node_pes[idx] = copy.deepcopy(mech_pe_by_acc[acc])
                        changed_node = True
                    elif acc and acc not in mech_pe_by_acc:
                        target_mech["protein_examples"] = _upsert_by_key(
                            target_mech.get("protein_examples", []),
                            [node_pe],
                            "uniprot_accession",
                        )
                        mech_pe_by_acc[acc] = copy.deepcopy(node_pe)
                        _mark_section("mechanisms")
                if changed_node:
                    _mark_section("causal_graphs")

            for acc, mech_pe in mech_pe_by_acc.items():
                if acc in node_accs:
                    continue
                target_node: dict[str, Any] | None = None
                gene_sym = mech_pe.get("gene_symbol")
                if gene_sym:
                    for cand in gene_or_protein_nodes:
                        if cand.get("gene_symbol") == gene_sym:
                            target_node = cand
                            break
                if target_node is None and len(gene_or_protein_nodes) == 1:
                    target_node = gene_or_protein_nodes[0]
                if target_node is not None:
                    target_node["protein_examples"] = _upsert_by_key(
                        target_node.get("protein_examples", []),
                        [mech_pe],
                        "uniprot_accession",
                    )
                    if target_node.get("protein_examples"):
                        target_node["protein_grounding_status"] = "GROUNDED"
                    node_accs.add(acc)
                    _mark_section("causal_graphs")

    return order_record_keys(updated), touched_sections


def write_record_atomic(record: dict[str, Any], path: Path) -> None:
    """Serialize record YAML with canonical key order and replace target file atomically."""
    ordered = order_record_keys(record)
    serialized = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True, width=1000)
    tmp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.stem}-",
            suffix=".tmp",
            delete=False,
        ) as stream:
            tmp_name = stream.name
            stream.write(serialized)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_name, path)
    except PermissionError:
        if tmp_name is not None:
            try:
                Path(tmp_name).unlink(missing_ok=True)
            except OSError:
                pass
        path.write_text(serialized, encoding="utf-8")


def curate_record_file(
    record_path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    patch: dict[str, Any] | None = None,
    summary: str = "",
    details: str = "",
    actor_name: str = "marcin",
    actor_type: str = "ai_agent",
    model: str = "claude-opus-4-6",
    agent_tool: str = "antigravity",
    agent_version: str = "",
    issues: list[str] | None = None,
    prs: list[str] | None = None,
    urls: list[str] | None = None,
    record_history: bool = True,
) -> tuple[dict[str, Any], str | None]:
    """Apply patch (or key-order normalization) to record_path, validate, and optionally mint history."""
    repo_root = repo_root.resolve()
    record_path = record_path if record_path.is_absolute() else (repo_root / record_path)
    record_path = record_path.resolve()

    original = read_record(record_path)
    if patch is not None:
        updated, touched_sections = apply_curation_patch(original, patch)
    else:
        updated = order_record_keys(original)
        touched_sections = []

    pre_errors = validate_record(updated)
    if pre_errors:
        raise ValueError(f"Record validation failed before write: {'; '.join(pre_errors)}")

    history_rel_path: str | None = None
    if record_history:
        if not summary.strip() or not details.strip():
            raise ValueError("--summary and --details are required when minting history")
        slug = updated["id"].split(":", 1)[1]
        rel_record_path = record_path.relative_to(repo_root).as_posix()
        sections_With_history = list(
            dict.fromkeys([*touched_sections, "curation_history", "history_refs"])
        )
        ns = argparse.Namespace(
            repo_root=repo_root,
            kind="record",
            slug=slug,
            path=rel_record_path,
            event="EDIT",
            outcome="changed",
            summary=summary.strip(),
            details=details.strip(),
            sections=",".join(sections_With_history),
            actor_name=actor_name,
            actor_type=actor_type,
            model=model,
            agent_tool=agent_tool,
            agent_version=agent_version,
            issue=issues or [],
            pr=prs or [],
            url=urls or [],
        )
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = history_cmd_new(ns)
        output = buf.getvalue().strip()
        if rc != 0 or not output.startswith("history/"):
            raise RuntimeError(f"Failed to mint history sidecar: {output}")
        history_rel_path = output.splitlines()[-1].strip()

        sidecar_doc = read_record(repo_root / history_rel_path)
        timestamp = sidecar_doc["session"]["timestamp"]
        if not isinstance(updated.get("curation_history"), list):
            updated["curation_history"] = []
        updated["curation_history"].append(
            {
                "timestamp": timestamp,
                "curator": actor_name,
                "action": "edit",
                "summary": summary.strip(),
            }
        )
        if not isinstance(updated.get("history_refs"), list):
            updated["history_refs"] = []
        updated["history_refs"].append(history_rel_path)
        updated = order_record_keys(updated)

        post_errors = validate_record(updated) + validate_references(updated, record_path, repo_root)
        if post_errors:
            # Clean up the newly minted sidecar if post-validation fails
            (repo_root / history_rel_path).unlink(missing_ok=True)
            raise ValueError(f"Post-history validation failed: {'; '.join(post_errors)}")

    write_record_atomic(updated, record_path)
    return updated, history_rel_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Apply causal_graphs and protein_examples updates with canonical key ordering and history minting."
    )
    parser.add_argument("record", type=Path, help="Path to target data/records/<slug>.yaml")
    parser.add_argument(
        "--patch",
        type=Path,
        default=None,
        help="YAML or JSON file containing causal_graphs / mechanism_protein_examples / sources updates",
    )
    parser.add_argument(
        "--normalize-only",
        action="store_true",
        help="Normalize canonical key order without applying a patch",
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--no-history", action="store_true", help="Skip history sidecar creation")
    parser.add_argument("--summary", default="", help="Curation summary (required unless --no-history)")
    parser.add_argument("--details", default="", help="Detailed curation rationale (required unless --no-history)")
    parser.add_argument("--actor-name", default="marcin")
    parser.add_argument(
        "--actor-type",
        choices=("human", "ai_agent", "automation", "other"),
        default="ai_agent",
    )
    parser.add_argument("--model", default="claude-opus-4-6")
    parser.add_argument("--agent-tool", default="antigravity")
    parser.add_argument("--agent-version", default="")
    parser.add_argument("--issue", action="append", default=[])
    parser.add_argument("--pr", action="append", default=[])
    parser.add_argument("--url", action="append", default=[])
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.patch is None and not args.normalize_only:
        parser.error("Provide --patch <path> or --normalize-only")
    patch_data: dict[str, Any] | None = None
    if args.patch is not None:
        patch_data = read_record(args.patch)
        if not isinstance(patch_data, dict):
            print("ERROR --patch file must contain a top-level mapping", file=sys.stderr)
            return 1
    try:
        _, history_rel = curate_record_file(
            args.record,
            repo_root=args.repo_root,
            patch=patch_data,
            summary=args.summary,
            details=args.details,
            actor_name=args.actor_name,
            actor_type=args.actor_type,
            model=args.model,
            agent_tool=args.agent_tool,
            agent_version=args.agent_version,
            issues=args.issue,
            prs=args.pr,
            urls=args.url,
            record_history=not args.no_history,
        )
    except (OSError, ValueError, RuntimeError, yaml.YAMLError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    if history_rel:
        print(history_rel)
    return 0


if __name__ == "__main__":
    sys.exit(main())
