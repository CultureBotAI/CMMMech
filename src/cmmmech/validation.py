"""Offline closed-schema and record-local integrity validation."""

import json
import math
import re
from collections import Counter
from decimal import Decimal, DecimalException
from functools import lru_cache
from importlib.resources import as_file, files
from pathlib import Path

import yaml
from jsonschema import FormatChecker
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator

BIOLOGICAL_NODE_TYPES = {
    "GENE_OR_PROTEIN",
    "BIOLOGICAL_PROCESS",
    "CELLULAR_STRUCTURE",
    "PHENOTYPE_OR_TRAIT",
}

MAX_SOURCE_TITLE_LENGTH = 1000
SOURCE_TITLE_ASSAY_PATTERN = re.compile(
    r"\b(?:wt\.?\s*%|apfu|wR2\s*=|GOF\s*=)\b",
    re.IGNORECASE,
)


def _section_order_errors(record: dict) -> list[str]:
    """Enforce top-level YAML section ordering invariants across evidence, mechanisms, and history."""
    keys = list(record.keys())
    if keys == sorted(keys):
        # Allow synthetic test fixtures dumped with PyYAML default sort_keys=True.
        return []
    pos = {key: idx for idx, key in enumerate(keys)}
    errors: list[str] = []
    if "criticality" in pos and "sources" in pos and pos["criticality"] < pos["sources"]:
        errors.append("$: criticality must appear after sources")
    if "mechanisms" in pos:
        for earlier in ("sources", "criticality"):
            if earlier in pos and pos["mechanisms"] < pos[earlier]:
                errors.append(f"$: mechanisms must appear after {earlier}")
    if "causal_graphs" in pos and "mechanisms" in pos and pos["causal_graphs"] < pos["mechanisms"]:
        errors.append("$: causal_graphs must appear after mechanisms")
    if "history_refs" in pos and "curation_history" in pos and pos["history_refs"] < pos["curation_history"]:
        errors.append("$: history_refs must appear after curation_history")
    for history_key in ("curation_history", "history_refs"):
        if history_key in pos:
            for content_key in ("sources", "criticality", "mechanisms", "causal_graphs"):
                if content_key in pos and pos[history_key] < pos[content_key]:
                    errors.append(f"$: {history_key} must appear after {content_key}")
    return errors


def _source_title_errors(sources_list: list[dict]) -> list[str]:
    """Flag over-long or assay-prose-stuffed Source.title entries (cmmmech-infra-0010)."""
    errors: list[str] = []
    for index, source in enumerate(sources_list):
        title = str(source.get("title", ""))
        if len(title) > MAX_SOURCE_TITLE_LENGTH:
            errors.append(
                f"sources/{index}/title: exceeds maximum bibliographic length ({MAX_SOURCE_TITLE_LENGTH} chars); "
                "move detailed assay prose to description or mechanisms"
            )
        if SOURCE_TITLE_ASSAY_PATTERN.search(title):
            errors.append(
                f"sources/{index}/title: contains embedded empirical assay/refinement metrics "
                "(wt.%, apfu, wR2, or GOF); keep Source.title concise and place analytical metrics "
                "in description or mechanisms with table provenance"
            )
    return errors



class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, "duplicate or non-string mapping key", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


@lru_cache(maxsize=2)
def schema_validator(filename: str, top_class: str):
    resource = files("cmmmech").joinpath(f"schema/{filename}")
    with as_file(resource) as path:
        schema = json.loads(JsonSchemaGenerator(
            str(path), top_class=top_class, not_closed=False, include_null=False
        ).serialize())
    validator = validator_for(schema)
    validator.check_schema(schema)
    return validator(schema, format_checker=FormatChecker())


def record_validator():
    return schema_validator("cmmmech.yaml", "CriticalMineralRecord")


def _observation_errors(observation, path: str) -> list[str]:
    """Validate a source cell without treating a censoring boundary as a measurement."""
    errors = []
    below_detection = observation["result_status"] == "below_detection"
    required = "detection_limit" if below_detection else "value"
    forbidden = "value" if below_detection else "detection_limit"
    if required not in observation:
        errors.append(f"{path}: {observation['result_status']} requires {required}")
    if forbidden in observation:
        errors.append(f"{path}: {observation['result_status']} forbids {forbidden}")

    try:
        raw = Decimal(observation["raw_value"])
    except DecimalException:
        errors.append(f"{path}/raw_value: cannot represent numeric source value")
        return errors
    if below_detection and raw >= 0:
        errors.append(f"{path}/raw_value: below_detection requires negative limit encoding")
    elif not below_detection and raw < 0:
        errors.append(f"{path}/raw_value: measured concentration cannot use negative encoding")

    for field in ("value", "detection_limit"):
        if field not in observation:
            continue
        value = observation[field]
        if isinstance(value, float) and not math.isfinite(value):
            errors.append(f"{path}/{field}: must be finite")
        elif field == "detection_limit" and value <= 0:
            errors.append(f"{path}/{field}: must be positive")
        elif field == required and Decimal(str(value)) != (
            raw.copy_abs() if below_detection else raw
        ):
            errors.append(f"{path}/{field}: does not match raw_value and result_status")

    has_sample_date = "sampled_on" in observation
    if has_sample_date != ("sampling_source_locator" in observation):
        errors.append(f"{path}: sampled_on and sampling_source_locator must be supplied together")
    if has_sample_date and observation["sampled_on"] > observation["analyzed_on"]:
        errors.append(f"{path}/sampled_on: cannot be after analyzed_on")
    return errors


def _protein_example_errors(
    examples: list[dict],
    path: str,
    references: list[tuple[str, str]],
    allowed_organisms: set[str] | None = None,
) -> list[str]:
    errors = []
    counts = Counter(item["uniprot_accession"] for item in examples)
    errors.extend(
        f"{path}: duplicate uniprot_accession {acc}"
        for acc, count in counts.items()
        if count > 1
    )
    for p_idx, pe in enumerate(examples):
        pe_path = f"{path}/{p_idx}"
        org_id = pe["target_organism"]["id"]
        if not re.fullmatch(r"NCBITaxon:[0-9]+", org_id):
            errors.append(f"{pe_path}/target_organism/id: must be an NCBITaxon CURIE")
        if (
            allowed_organisms is not None
            and org_id not in allowed_organisms
            and not pe.get("annotation_note")
        ):
            errors.append(
                f"{pe_path}: target_organism {org_id} not in mechanism organisms requires annotation_note"
            )
        for field in ("ec_numbers", "interpro_ids", "pfam_ids", "ncbifam_ids"):
            values = pe.get(field, [])
            if len(set(values)) != len(values):
                errors.append(f"{pe_path}/{field}: duplicate value")
        go_terms = pe.get("go_terms", [])
        go_ids = [g["id"] for g in go_terms]
        if len(set(go_ids)) != len(go_ids):
            errors.append(f"{pe_path}/go_terms: duplicate GO term id")
        for g_idx, go_term in enumerate(go_terms):
            if not re.fullmatch(r"GO:[0-9]{7}", go_term["id"]):
                errors.append(f"{pe_path}/go_terms/{g_idx}/id: must be a 7-digit GO CURIE")
        references.extend(
            (f"{pe_path}/evidence/{e_idx}", ev["source_ref"])
            for e_idx, ev in enumerate(pe.get("evidence", []))
        )
    return errors


def validate_record(record) -> list[str]:
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in record_validator().iter_errors(record)
    ]
    if errors:
        return sorted(errors)

    errors.extend(_section_order_errors(record))
    errors.extend(_source_title_errors(record.get("sources", [])))

    for section in ("sources", "mechanisms", "causal_graphs"):
        counts = Counter(item["id"] for item in record.get(section, []))
        errors.extend(f"{section}: duplicate id {key}" for key, count in counts.items() if count > 1)
    history = record.get("history_refs", [])
    if len(set(history)) != len(history):
        errors.append("history_refs: duplicate history reference")
    sources = {source["id"] for source in record["sources"]}
    references = [(f"criticality/{index}", item["source_ref"])
                  for index, item in enumerate(record.get("criticality", []))]
    observation_ids = set()
    source_cells = set()
    for index, mechanism in enumerate(record.get("mechanisms", [])):
        if mechanism.get("organisms") and not mechanism["microbial"]:
            errors.append(f"mechanisms/{index}: organisms require microbial: true")
        if mechanism.get("protein_examples") and not mechanism["microbial"]:
            errors.append(f"mechanisms/{index}: protein_examples require microbial: true")
        mech_org_ids = {org["id"] for org in mechanism.get("organisms", [])}
        errors.extend(
            _protein_example_errors(
                mechanism.get("protein_examples", []),
                f"mechanisms/{index}/protein_examples",
                references,
                allowed_organisms=mech_org_ids,
            )
        )
        references.extend((f"mechanisms/{index}/evidence/{i}", item["source_ref"])
                          for i, item in enumerate(mechanism["evidence"]))
        evidence_sources = {item["source_ref"] for item in mechanism["evidence"]}
        for number, observation in enumerate(mechanism.get("observations", [])):
            path = f"mechanisms/{index}/observations/{number}"
            references.append((path, observation["source_ref"]))
            if observation["source_ref"] not in evidence_sources:
                errors.append(f"{path}: source_ref must occur in this mechanism's evidence")
            if observation["id"] in observation_ids:
                errors.append(f"{path}: duplicate observation id {observation['id']}")
            observation_ids.add(observation["id"])
            cell = tuple(observation[field] for field in (
                "source_ref", "source_table", "source_sample_id", "source_column", "analyzed_on"
            ))
            if cell in source_cells:
                errors.append(f"{path}: duplicate source concentration cell")
            source_cells.add(cell)
            errors.extend(_observation_errors(observation, path))
    mechanisms_by_id = {m["id"]: m for m in record.get("mechanisms", [])}
    for g_idx, graph in enumerate(record.get("causal_graphs", [])):
        g_path = f"causal_graphs/{g_idx}"
        mech_ref = graph.get("mechanism_ref")
        if mech_ref:
            if mech_ref not in mechanisms_by_id:
                errors.append(f"{g_path}: unknown mechanism_ref {mech_ref}")
            elif not mechanisms_by_id[mech_ref]["microbial"] and any(
                n["node_type"] in BIOLOGICAL_NODE_TYPES for n in graph.get("nodes", [])
            ):
                errors.append(
                    f"{g_path}: biological or GENE_OR_PROTEIN nodes require microbial mechanism_ref"
                )
        graph_allowed_organisms = (
            {org["id"] for org in mechanisms_by_id[mech_ref].get("organisms", [])}
            if mech_ref and mech_ref in mechanisms_by_id
            else None
        )
        node_counts = Counter(node["id"] for node in graph.get("nodes", []))
        errors.extend(
            f"{g_path}/nodes: duplicate id {key}"
            for key, count in node_counts.items()
            if count > 1
        )
        node_ids = {node["id"] for node in graph.get("nodes", [])}
        for n_idx, node in enumerate(graph.get("nodes", [])):
            n_path = f"{g_path}/nodes/{n_idx}"
            p_examples = node.get("protein_examples", [])
            status = node.get("protein_grounding_status")
            if node["node_type"] == "GENE_OR_PROTEIN":
                if status not in {"GROUNDED", "UNGROUNDED"}:
                    errors.append(
                        f"{n_path}: GENE_OR_PROTEIN node requires GROUNDED or UNGROUNDED protein_grounding_status"
                    )
                if status == "GROUNDED" and not p_examples:
                    errors.append(f"{n_path}: GROUNDED node requires protein_examples")
                if status == "UNGROUNDED":
                    if p_examples:
                        errors.append(f"{n_path}: UNGROUNDED node cannot have protein_examples")
                    if not node.get("description"):
                        errors.append(
                            f"{n_path}: UNGROUNDED node requires description explaining ungrounded status"
                        )
            else:
                if status != "NOT_APPLICABLE":
                    errors.append(
                        f"{n_path}: non-GENE_OR_PROTEIN node requires NOT_APPLICABLE protein_grounding_status"
                    )
                if p_examples:
                    errors.append(
                        f"{n_path}: protein_examples are only permitted on GENE_OR_PROTEIN nodes"
                    )
                if node.get("gene_symbol"):
                    errors.append(
                        f"{n_path}: gene_symbol is only permitted on GENE_OR_PROTEIN nodes"
                    )
            errors.extend(
                _protein_example_errors(
                    p_examples,
                    f"{n_path}/protein_examples",
                    references,
                    allowed_organisms=graph_allowed_organisms,
                )
            )
        seen_edges = set()
        connected_nodes = set()
        for e_idx, edge in enumerate(graph.get("edges", [])):
            e_path = f"{g_path}/edges/{e_idx}"
            src, tgt, pred = edge["source"], edge["target"], edge["predicate"]
            connected_nodes.add(src)
            connected_nodes.add(tgt)
            if src not in node_ids:
                errors.append(f"{e_path}: unknown source node {src}")
            if tgt not in node_ids:
                errors.append(f"{e_path}: unknown target node {tgt}")
            if src == tgt:
                errors.append(f"{e_path}: self-loop edge on node {src}")
            edge_key = (src, tgt, pred)
            if edge_key in seen_edges:
                errors.append(f"{e_path}: duplicate edge {src} -> {tgt} ({pred})")
            seen_edges.add(edge_key)
            references.extend(
                (f"{e_path}/evidence/{ev_idx}", ev["source_ref"])
                for ev_idx, ev in enumerate(edge.get("evidence", []))
            )
        for n_idx, node in enumerate(graph.get("nodes", [])):
            if node["id"] not in connected_nodes:
                errors.append(
                    f"{g_path}/nodes/{n_idx}: disconnected node {node['id']} has no incident edges"
                )
    errors.extend(f"{path}: unknown source_ref {key}" for path, key in references if key not in sources)
    return sorted(errors)


def read_record(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)

