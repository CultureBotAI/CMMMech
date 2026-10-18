#!/usr/bin/env python3
"""Render the browsable GitHub Pages site under pages/ from data/records/.

Usage:
    python scripts/render_pages.py
    python scripts/render_pages.py --check
    python scripts/render_pages.py --out /tmp/site
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "cmmmech" / "templates"
RECORDS_DIR = REPO_ROOT / "data" / "records"
PAGES_DIR = REPO_ROOT / "pages"

KIND_LABELS = {
    "element": "Elements",
    "mineral": "Minerals",
    "secondary_resource": "Secondary Resources",
    "commodity": "Commodities",
    "primary_resource": "Primary Resources",
    "mineral_group": "Mineral Groups",
}

KIND_BLURBS = {
    "element": "Chemical elements distinct from ores, alloys, and waste streams.",
    "mineral": "Naturally occurring crystalline inorganic substances with defined IMA mineral status.",
    "secondary_resource": "Post-consumer and industrial byproducts including spent batteries, slags, red mud, and scrap.",
    "commodity": "Aggregated commercial products, traded raw materials, and manufactured chemical compounds.",
    "primary_resource": "Raw unrefined geological deposits, mined ores, and run-of-mine materials.",
    "mineral_group": "Mineral supergroups and solid-solution series sharing related crystal structures.",
}

PROCESS_LABELS = {
    "bioleaching": "Bioleaching",
    "biomineralization": "Biomineralization",
    "redox_transformation": "Redox Transformation",
    "biosorption": "Biosorption",
    "separation": "Separation",
    "recovery": "Recovery",
    "other": "Other Transformations",
}

PROCESS_BLURBS = {
    "bioleaching": "Microbial solubilization and mobilization of target metals from ores, concentrates, and wastes.",
    "biomineralization": "Biological precipitation, crystallization, and synthesis of mineral phases or nanoparticles.",
    "redox_transformation": "Oxidation-reduction reactions that alter metal valence states; microbial involvement is specified in each record.",
    "biosorption": "Passive binding and retention of metal ions by microbial cell walls and biomass.",
    "separation": "Selective partitioning by biological or abiotic processes. See each record for microbial involvement, experimental conditions and recovery limits.",
    "recovery": "Integrated microbial processing schemes yielding concentrated or isolated materials.",
    "other": "Complex community transformations, multi-stage processes, or unclassified interactions.",
}

PREFIX_URL = {
    "CHEBI": "https://www.ebi.ac.uk/chebi/CHEBI:",
    "NCBITaxon": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=",
    "DOI": "https://doi.org/",
    "PMID": "https://pubmed.ncbi.nlm.nih.gov/",
    "GO": "http://purl.obolibrary.org/obo/GO_",
    "UniProtKB": "https://www.uniprot.org/uniprotkb/",
    "InterPro": "https://www.ebi.ac.uk/interpro/entry/InterPro/",
    "Pfam": "https://www.ebi.ac.uk/interpro/entry/pfam/",
    "NCBIfam": "https://www.ncbi.nlm.nih.gov/genome/annotation_prok/evidence/",
    "ComplexPortal": "https://www.ebi.ac.uk/complexportal/complex/",
    "EC": "https://www.ebi.ac.uk/intenz/query?cmd=SearchEC&ec=",
}


def curie_url(curie: str) -> str | None:
    if not isinstance(curie, str) or ":" not in curie:
        return None
    prefix, local = curie.split(":", 1)
    base = PREFIX_URL.get(prefix)
    return f"{base}{local}" if base else None


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    records = []
    for path in sorted(RECORDS_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("name"):
            records.append((path, doc))
    return records


def prepare_record_data(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    slug = path.stem
    name = doc.get("name", slug)
    material_kind = doc.get("material_kind", "other")
    description = doc.get("description", "").strip()

    # Identifiers with URLs
    identifiers = []
    for item in doc.get("identifiers") or []:
        cid = item.get("id", "")
        identifiers.append({
            "id": cid,
            "label": item.get("label", ""),
            "url": curie_url(cid),
        })

    # Criticality
    criticality = doc.get("criticality") or []
    is_critical = any(
        str(c.get("classification", "")).lower() in {"critical", "strategic", "high"}
        for c in criticality
    )
    criticality_summary = "; ".join(
        f"{c.get('jurisdiction', '')} {c.get('list_name', '')} ({c.get('classification', '')})"
        for c in criticality
    )

    # Mechanisms
    mechanisms = doc.get("mechanisms") or []
    mechanism_processes = sorted(list({m.get("process") for m in mechanisms if m.get("process")}))

    organisms = []
    seen_orgs = set()
    protein_tokens = []
    for m in mechanisms:
        for org in m.get("organisms") or []:
            oid = org.get("id", "")
            if oid not in seen_orgs:
                seen_orgs.add(oid)
                organisms.append({
                    "id": oid,
                    "label": org.get("label", oid),
                    "url": curie_url(oid),
                })
        for pe in m.get("protein_examples") or []:
            protein_tokens.extend(
                filter(
                    None,
                    [
                        pe.get("uniprot_accession"),
                        pe.get("entry_name"),
                        pe.get("protein_name"),
                        pe.get("gene_symbol"),
                    ],
                )
            )

    causal_graphs = doc.get("causal_graphs") or []
    for cg in causal_graphs:
        for node in cg.get("nodes") or []:
            protein_tokens.extend(filter(None, [node.get("label"), node.get("gene_symbol")]))
            for pe in node.get("protein_examples") or []:
                protein_tokens.extend(
                    filter(
                        None,
                        [
                            pe.get("uniprot_accession"),
                            pe.get("entry_name"),
                            pe.get("protein_name"),
                            pe.get("gene_symbol"),
                        ],
                    )
                )

    # Search text for client-side filter
    search_parts = [
        name,
        slug,
        material_kind,
        description,
        " ".join(i["id"] for i in identifiers),
        " ".join(i["label"] for i in identifiers),
        " ".join(mechanism_processes),
        " ".join(o["label"] for o in organisms),
        " ".join(o["id"] for o in organisms),
        " ".join(protein_tokens),
        criticality_summary,
    ]
    search_text = " ".join(filter(None, search_parts)).lower()

    # Evidence boundary summary
    evidence_boundary = ""
    for m in mechanisms:
        ctx = m.get("context", "")
        if ctx:
            evidence_boundary = ctx[:120] + ("…" if len(ctx) > 120 else "")
            break

    return {
        "slug": slug,
        "name": name,
        "material_kind": material_kind,
        "description": description,
        "identifiers": identifiers,
        "criticality": criticality,
        "is_critical": is_critical,
        "criticality_summary": criticality_summary,
        "mechanisms": mechanisms,
        "causal_graphs": causal_graphs,
        "mechanism_processes": mechanism_processes,
        "organisms": organisms,
        "sources": doc.get("sources") or [],
        "curation_history": doc.get("curation_history") or [],
        "page": f"materials/{slug}.html",
        "search_text": search_text,
        "evidence_boundary": evidence_boundary,
        "raw_doc": doc,
    }


def render(out_dir: Path) -> None:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = curie_url

    raw_records = load_records()
    records_data = [prepare_record_data(p, d) for p, d in raw_records]

    # Group by kind and process
    by_kind = defaultdict(list)
    by_process = defaultdict(list)
    for r in records_data:
        by_kind[r["material_kind"]].append(r)
        for proc in r["mechanism_processes"]:
            by_process[proc].append(r)

    kinds_counts = [
        (k, len(by_kind[k]))
        for k in ["element", "mineral", "secondary_resource", "commodity", "primary_resource", "mineral_group"]
        if k in by_kind
    ]
    process_counts = [
        (p, len(by_process[p]))
        for p in ["bioleaching", "biomineralization", "redox_transformation", "biosorption", "separation", "recovery", "other"]
        if p in by_process
    ]

    total_materials = len(records_data)
    total_mechanisms = sum(len(r["mechanisms"]) for r in records_data)
    materials_with_mechs = sum(1 for r in records_data if r["mechanisms"])
    critical_materials_count = sum(1 for r in records_data if r["is_critical"])

    # Featured materials
    featured_slugs = [
        "cobalt", "neodymium", "lithium", "copper", "nickel", "palladium",
        "tellurium", "gallium", "germanium", "fluorescent-lamp-phosphor",
        "gaas-production-hydroxide-sludge", "chalcopyrite",
    ]
    by_slug = {r["slug"]: r for r in records_data}
    featured = [by_slug[s] for s in featured_slugs if s in by_slug]

    kinds_meta = [
        {
            "id": k,
            "label": KIND_LABELS.get(k, k.replace("_", " ").title()),
            "count": len(by_kind[k]),
            "blurb": KIND_BLURBS.get(k, ""),
            "page": f"kinds/{k}.html",
        }
        for k, _ in kinds_counts
    ]

    processes_meta = [
        {
            "id": p,
            "label": PROCESS_LABELS.get(p, p.replace("_", " ").title()),
            "count": sum(sum(1 for m in r["mechanisms"] if m.get("process") == p) for r in by_process[p]),
            "blurb": PROCESS_BLURBS.get(p, ""),
            "page": f"processes/{p}.html",
        }
        for p, _ in process_counts
    ]

    # Create directories
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "materials").mkdir(parents=True, exist_ok=True)
    (out_dir / "kinds").mkdir(parents=True, exist_ok=True)
    (out_dir / "processes").mkdir(parents=True, exist_ok=True)

    # Assets
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    shutil.copy(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")
    shutil.copy(TEMPLATES_DIR / "record-browser.js", out_dir / "record-browser.js")

    # Render index.html
    index_html = env.get_template("index.html").render(
        root="",
        total_materials=total_materials,
        total_mechanisms=total_mechanisms,
        materials_with_mechs=materials_with_mechs,
        critical_materials_count=critical_materials_count,
        kinds=kinds_meta,
        processes=processes_meta,
        featured=featured,
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Render browse.html
    browse_html = env.get_template("browse.html").render(
        root="",
        records=records_data,
        kinds_counts=kinds_counts,
        process_counts=process_counts,
    )
    (out_dir / "browse.html").write_text(browse_html, encoding="utf-8")

    # Write index.json
    index_json_data = [
        {
            "slug": r["slug"],
            "name": r["name"],
            "material_kind": r["material_kind"],
            "is_critical": r["is_critical"],
            "criticality": [c.get("list_name") for c in r["criticality"]],
            "mechanisms_count": len(r["mechanisms"]),
            "processes": r["mechanism_processes"],
            "organisms": [o["label"] for o in r["organisms"]],
            "page": r["page"],
        }
        for r in records_data
    ]
    (out_dir / "index.json").write_text(
        json.dumps(index_json_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Render kinds/*.html
    for k_meta in kinds_meta:
        k = k_meta["id"]
        k_records = by_kind[k]
        k_html = env.get_template("kind.html").render(
            root="../",
            kind=k_meta,
            records=k_records,
            kinds_counts=kinds_counts,
            process_counts=process_counts,
        )
        (out_dir / "kinds" / f"{k}.html").write_text(k_html, encoding="utf-8")

    # Render processes/*.html
    for p_meta in processes_meta:
        p = p_meta["id"]
        p_records = by_process[p]
        p_html = env.get_template("process.html").render(
            root="../",
            process=p_meta,
            records=p_records,
            kinds_counts=kinds_counts,
            process_counts=process_counts,
        )
        (out_dir / "processes" / f"{p}.html").write_text(p_html, encoding="utf-8")

    # Render materials/*.html
    for p, doc in raw_records:
        r = prepare_record_data(p, doc)
        # Add organism URLs into raw doc mechanisms for rendering
        rendered_r = dict(doc)
        rendered_r["name"] = r["name"]
        rendered_r["material_kind"] = r["material_kind"]
        rendered_r["identifiers"] = r["identifiers"]
        source_path = str(p.relative_to(REPO_ROOT))

        # Enrich mechanisms with urls
        enriched_mechs = []
        for m in r["mechanisms"]:
            m_copy = dict(m)
            enriched_orgs = []
            for org in m.get("organisms") or []:
                oid = org.get("id", "")
                enriched_orgs.append({
                    "id": oid,
                    "label": org.get("label", oid),
                    "url": curie_url(oid),
                })
            m_copy["organisms"] = enriched_orgs
            enriched_mechs.append(m_copy)
        rendered_r["mechanisms"] = enriched_mechs

        mat_html = env.get_template("material.html").render(
            root="../",
            r=rendered_r,
            source_path=source_path,
        )
        (out_dir / "materials" / f"{r['slug']}.html").write_text(mat_html, encoding="utf-8")

    # Root redirect index.html
    if out_dir.resolve() == PAGES_DIR.resolve():
        root_index = (
            '<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '<meta charset="utf-8">\n'
            '<meta http-equiv="refresh" content="0; url=pages/index.html">\n'
            '<link rel="canonical" href="pages/index.html">\n'
            '<title>Redirecting to CMMMech...</title>\n'
            '</head>\n'
            '<body>\n'
            '<p>Redirecting to <a href="pages/index.html">CMMMech</a>...</p>\n'
            '</body>\n'
            '</html>\n'
        )
        (REPO_ROOT / "index.html").write_text(root_index, encoding="utf-8")


def _tree_differs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        diffs.extend(f"{prefix}{n}" for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(a, b), "")
    return diffs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to a temp dir and diff against --out.",
    )
    args = parser.parse_args(argv)

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render(Path(tmp))
            if not args.out.exists():
                print(f"{args.out} does not exist; run `just render`", file=sys.stderr)
                return 1
            diffs = _tree_differs(Path(tmp), args.out)
        if diffs:
            print(
                f"pages/ is stale ({len(diffs)} file(s) differ), e.g. {diffs[:5]}; run `just render`",
                file=sys.stderr,
            )
            return 1
        print("pages/ is current")
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    render(args.out)
    print(f"Rendered CMMMech site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
