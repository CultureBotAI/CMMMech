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
import hashlib
import json
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode, urlsplit

import yaml
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "cmmmech" / "templates"
RECORDS_DIR = REPO_ROOT / "data" / "records"
PAGES_DIR = REPO_ROOT / "pages"
SCHEMA_PATH = REPO_ROOT / "src" / "cmmmech" / "schema" / "cmmmech.yaml"
REVIEWS_DIR = REPO_ROOT / "reviews" / "structured"
HISTORY_DIR = REPO_ROOT / "history" / "records"

GITHUB_REPO = "https://github.com/CultureBotAI/CMMMech"
SITE_URL = "https://culturebotai.github.io/CMMMech/"
# GitHub Pages answers a missing address at any depth with the artifact root's
# 404.html, so that page's links are site-root-absolute, never relative.
SITE_ROOT = "/CMMMech/"
TAXONMECH_RECORD = "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:"
TAXONMECH_SEARCH = "https://culturebotai.github.io/TaxonMech/pages/browse.html?q="

# libyaml when PyYAML has it: the same documents as SafeLoader, about ten times
# faster on the 844 review bundles. The rendered bytes do not depend on which.
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

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
    "NCBIfam": "https://www.ebi.ac.uk/interpro/entry/ncbifam/",
    "ComplexPortal": "https://www.ebi.ac.uk/complexportal/complex/",
    # IntEnz answers 404 for every EC number and at its root (2026-10-25);
    # ExPASy ENZYME resolves full and partial (1.1.1.-) numbers alike.
    "EC": "https://enzyme.expasy.org/EC/",
}

# This repository's own namespace. No registry resolves it: a cmmmech: CURIE is
# linkable only through the record page it names.
LOCAL_PREFIX = "cmmmech"
# Prefixes a registry fallback would turn into a dead link. bioregistry.io has
# no IMA prefix (HTTP 404, 2026-10-25) and the IMA list has no page per
# approval number, so an IMA number stays labelled text.
UNRESOLVED_PREFIXES = frozenset({"IMA"})
CURIE_SHAPE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'\\]+")
PROTEOME_ID = re.compile(r"UP[0-9]{9}")


def curie_url(curie: str) -> str | None:
    """Resolve a displayed CURIE to an external page.

    Known prefixes use PREFIX_URL; any other well-formed CURIE falls back to
    bioregistry.io, which resolves or explains every registered prefix, so a
    displayed identifier is never a dead end. This repository's own records
    and the unregistered prefixes above resolve to nothing here.
    """
    if not isinstance(curie, str) or ":" not in curie:
        return None
    value = curie.strip()
    if not CURIE_SHAPE.fullmatch(value):
        return None
    prefix, local = value.split(":", 1)
    base = PREFIX_URL.get(prefix)
    if base:
        return f"{base}{local}"
    if prefix == LOCAL_PREFIX or prefix in UNRESOLVED_PREFIXES:
        return None
    return "https://bioregistry.io/" + quote(value, safe=":/")


def proteome_url(proteome_id: object) -> str | None:
    """UniProt reference proteomes are bare UP accessions, not CURIEs."""
    if isinstance(proteome_id, str) and PROTEOME_ID.fullmatch(proteome_id):
        return f"https://www.uniprot.org/proteomes/{proteome_id}"
    return None


def taxonmech_url(organism: dict[str, Any]) -> str:
    """TaxonMech's record for an NCBITaxon id; its label search otherwise."""
    oid = str(organism.get("id") or "")
    prefix, _, local = oid.partition(":")
    if prefix == "NCBITaxon" and local.isdigit():
        return TAXONMECH_RECORD + local
    return TAXONMECH_SEARCH + quote(str(organism.get("label") or oid), safe="")


def reference_url(reference: object) -> str | None:
    """Resolve a citation token without turning arbitrary text into a link."""
    if not isinstance(reference, str):
        return None
    if any(ord(char) < 32 or ord(char) == 127 for char in reference):
        return None
    value = reference.strip()
    if re.fullmatch(r"DOI:10\.[0-9]{4,9}/\S+", value, re.IGNORECASE):
        return "https://doi.org/" + quote(value[4:], safe="/():;")
    if any(char.isspace() or char in '\\<>"' for char in value):
        return None
    try:
        parsed = urlsplit(value)
        if (parsed.scheme.lower() in {"http", "https"} and parsed.hostname
                and parsed.username is None and parsed.password is None):
            _ = parsed.port  # rejects a malformed or non-numeric port
            return value
    except ValueError:
        pass
    return None


# Reference tokens inside record prose. URLs match first, so a DOI or PMCID
# inside a URL stays part of that URL. Matching runs on the raw string and each
# piece is escaped on the way out, so record text can never become markup. A
# token ends at "]" as well as at whitespace, quotes and angle brackets: in
# Markdown link syntax "[10.1038/x](https://doi.org/10.1038/x)" a DOI must not
# swallow "](https://..." into its href (TraitMech #2022).
AUTOLINK_TOKEN = re.compile(
    r"(?P<url>\b(?i:https?)://[^\s<>\"\\\]]+)"
    r"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{4,9}/[^\s<>\"\\\]]+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
    r"|(?P<own>\b" + LOCAL_PREFIX + r":[a-z][a-z0-9-]*)"
)
CLOSING = {")": "(", "]": "[", "}": "{"}
# Sentence punctuation, plus the Markdown emphasis and code marks that close a
# token written as **10.x/y** or `10.x/y`.
TRAILING = ".,;:!?'\"*`"


def _trim_token(token: str) -> str:
    """Drop punctuation, Markdown marks and unbalanced closers that end a token."""
    while token:
        last = token[-1]
        if last in TRAILING or (last in CLOSING and token.count(last) > token.count(CLOSING[last])):
            token = token[:-1]
            continue
        break
    return token


@pass_context
def autolink(context, value: object) -> Markup:
    """Escape record prose and link the references and record ids it cites.

    PMID, PMCID, DOI and http(s) URL tokens link to PubMed, PMC, doi.org and
    the URL itself. A cmmmech: id naming another record links to that record's
    page; one naming the page's own record, or no record at all, stays text.
    Surrounding text is kept verbatim, so text without a reference renders
    exactly as plain escaping would.
    """
    if value is None:
        return Markup("")
    if isinstance(value, Markup):
        return value
    text = str(value)
    slugs = context.get("record_slugs") or ()
    record = context.get("r")
    own_slug = record.get("slug") if isinstance(record, dict) else None
    out: list[str] = []
    position = 0
    for match in AUTOLINK_TOKEN.finditer(text):
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind == "own":
            token = token.rstrip("-")
            slug = token.split(":", 1)[1]
            url = (f"{context.get('root') or ''}materials/{slug}.html"
                   if slug in slugs and slug != own_slug else None)
        elif kind in {"url", "doi"}:
            token = _trim_token(token)
            if kind == "url":
                url = reference_url(token)
            else:
                url = reference_url("DOI:" + token[token.index("10."):]) if token else None
        elif kind == "pmid":
            url = f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
        else:
            url = f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"
        if not url:
            continue
        out.append(escape(text[position:match.start()]))
        out.append(Markup('<a href="{}">{}</a>').format(url, token))
        position = match.start() + len(token)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def template_environment(record_slugs: frozenset[str] = frozenset()) -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = curie_url
    env.filters["proteome_url"] = proteome_url
    env.filters["taxonmech_url"] = taxonmech_url
    env.filters["autolink"] = autolink
    env.filters["inline_code"] = inline_code
    env.globals["record_slugs"] = record_slugs
    env.globals["quotes"] = CURATION_QUOTES
    return env


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    records = []
    for path in sorted(RECORDS_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("name"):
            records.append((path, doc))
    return records


# How records are curated and reviewed, in the repository's own words. Pages
# quote these rather than paraphrase them, so no page claims more about a review
# (who made it, and what it establishes) than the repository does. Each is
# checked verbatim against its source file by tests/test_unified_site_features.py.
CURATION_QUOTES = {
    "reviewed_corpus": ("README.md", "Each record has a timestamped scientific review; "
                        "synthetic test fixtures remain separate."),
    "validation": ("README.md", "Validation is not scientific verification."),
    "sources": ("docs/records.md", "Sources establish provenance; they do not imply that an "
                "agent has verified the publication or that every claim in it is correct."),
    "report": ("docs/record-reviews.md", "A valid report does not certify scientific truth or "
               "authorize curation, Git publication, paid research, or status promotion."),
    "observation": ("schema/record_review.yaml", "An immutable, scoped review observation, not "
                    "permission to curate or proof of scientific truth."),
    "passing": ("docs/record-reviews.md", "Passing verdicts cannot conceal unresolved "
                "major/blocker findings or failed required checks."),
    "qualified": ("docs/record-reviews.md", "An unknown or concerning assessment precludes plain "
                  "`pass`; a qualified pass must state its limitations and still positively "
                  "assess each actually reviewed target."),
    "newer": ("docs/record-reviews.md", "A newer clean review does not close an older issue."),
}


def inline_code(text: object) -> Markup:
    """Escape a quotation and set its `backticked` spans as code, as its Markdown source does."""
    parts = str(text or "").split("`")
    return Markup("").join(
        Markup("<code>{}</code>").format(part) if index % 2 else escape(part)
        for index, part in enumerate(parts)
    )


def load_structured_reviews(reviews_dir: Path = REVIEWS_DIR) -> tuple[dict[str, list[dict]], list[dict]]:
    """Saved structured reviews, by the repository path of each file they target.

    reviews/structured/<id>/review.yaml is authoritative and review.md beside it
    is its rendering (docs/record-reviews.md). Every saved review of a record is
    kept, newest first: a newer clean review does not close an older finding,
    so a page lists them all rather than choosing one. Returns the index and
    every review, for corpus-wide counts.
    """
    by_path: dict[str, dict[str, dict]] = defaultdict(dict)
    reviews: list[dict] = []
    for path in sorted(reviews_dir.glob("*/review.yaml")):
        doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
        reviewer = doc.get("reviewer") or {}
        summary = {
            "review_id": doc["review_id"],
            "kind": doc["kind"],
            "title": doc["title"],
            "finished_at": doc["finished_at"],
            "verdict": doc["verdict"],
            "completion": doc["completion"],
            "scientific_review": bool(doc["scientific_review"]),
            "reviewer_kind": reviewer.get("kind", ""),
            "reviewer_model": reviewer.get("model", ""),
            # Where the bundle is published: reviews/structured/<id>/review.md.
            "markdown": f"{REVIEWS_DIR.relative_to(REPO_ROOT).as_posix()}/{path.parent.name}/review.md",
        }
        reviews.append(summary)
        for target in doc.get("targets") or []:
            by_path[target["path"]][summary["review_id"]] = summary
    index = {
        target: sorted(found.values(), reverse=True, key=lambda review: (
            review["finished_at"], review["kind"] == "record", review["review_id"]))
        for target, found in by_path.items()
    }
    return index, reviews


def history_sessions(history_dir: Path = HISTORY_DIR) -> list[dict]:
    """Every saved HistoryRecord session, for the actor-type counts the landing page states."""
    sessions = []
    for path in sorted(history_dir.glob("*/*.yaml")):
        doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
        sessions.append((doc or {}).get("session") or {})
    return sessions


def schema_reference(schema_path: Path = SCHEMA_PATH) -> dict[str, Any]:
    """Readable documentation of the record schema, read from the schema itself.

    The site linked only the raw YAML. This documents what LinkML resolves
    instead: every class with its induced slots (imports and slot_usage
    applied), the schema's own types, and every enum with its permissible
    values. Declaration order and no clock, so an unchanged schema renders
    byte-identically under the pages/ staleness gate.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    def repo_path(path: Path) -> str:
        return path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else path.name

    view = SchemaView(str(schema_path))
    view.imports_closure()
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.exists():
            module_file[schema.id] = repo_path(source)
    classes = view.all_classes()
    enums = view.all_enums()
    types = view.all_types(imports=False)
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]
    local_enums = list(view.all_enums(imports=False))
    ordered_enums = local_enums + [name for name in enums if name not in local_enums]

    def range_kind(name: str | None) -> str:
        if name in classes:
            return "class"
        if name in enums:
            return "enum"
        if name in types:
            return "type"
        return "builtin"

    def slot_row(slot) -> dict[str, Any]:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        ranges = names or [slot.range or view.schema.default_range or "string"]
        return {
            "name": slot.name,
            "ranges": [{"name": name, "kind": range_kind(name)} for name in ranges],
            # SchemaView's induced slots already mark an identifier required.
            "required": bool(slot.required),
            "multivalued": bool(slot.multivalued),
            "identifier": bool(slot.identifier),
            "pattern": slot.pattern or "",
            "description": " ".join((slot.description or "").split()),
        }

    def source_of(element) -> str:
        return module_file.get(element.from_schema, "")

    return {
        "title": view.schema.title or view.schema.name,
        "description": view.schema.description or "",
        "license": view.schema.license or "",
        "source": repo_path(schema_path),
        "modules": sorted(set(module_file.values())),
        "classes": [{
            "name": name,
            "description": " ".join((classes[name].description or "").split()),
            "is_a": classes[name].is_a or "",
            "tree_root": bool(classes[name].tree_root),
            "source": source_of(classes[name]),
            "slots": [slot_row(slot) for slot in view.class_induced_slots(name)],
        } for name in ordered],
        "types": [{
            "name": name,
            "typeof": types[name].typeof or "",
            "pattern": types[name].pattern or "",
            "description": " ".join((types[name].description or "").split()),
        } for name in types],
        "enums": [{
            "name": name,
            "description": " ".join((enums[name].description or "").split()),
            "source": source_of(enums[name]),
            "permissible": [{"text": text, "description": " ".join((value.description or "").split()),
                             "meaning": value.meaning or ""}
                            for text, value in (enums[name].permissible_values or {}).items()],
        } for name in ordered_enums],
    }


def first_sentence(text: str) -> str:
    """A definition's first sentence; ai_agent's second is an instruction to authors."""
    head, separator, _ = text.partition(". ")
    return head + "." if separator else text


def actor_types(schema: dict[str, Any], sessions: list[dict]) -> dict[str, Any]:
    """Saved history sessions by actor type, beside the history schema's own definitions."""
    enum = next(e for e in schema["enums"] if e["name"] == "HistoryActorTypeEnum")
    counts = Counter(
        actor_type
        for session in sessions
        for actor_type in {actor.get("type") for actor in session.get("actors") or []}
    )
    return {
        "description": enum["description"],
        "total": len(sessions),
        "types": [{"type": value["text"], "description": first_sentence(value["description"]),
                   "sessions": counts.get(value["text"], 0)} for value in enum["permissible"]],
    }


def reviewer_kinds(reviews: list[dict]) -> dict[str, Any]:
    """Saved structured reviews by reviewer kind, in the review schema's order."""
    from linkml_runtime.utils.schemaview import SchemaView

    enum = SchemaView(str(REPO_ROOT / "schema" / "record_review.yaml")).get_enum("ReviewerKind")
    counts = Counter(review["reviewer_kind"] for review in reviews)
    return {
        "total": len(reviews),
        "kinds": [{"kind": kind, "reviews": counts.get(kind, 0)} for kind in enum.permissible_values],
    }


def _collect_protein_example_tokens(pe: dict[str, Any], out: list[str]) -> None:
    out.extend(
        filter(
            None,
            [
                pe.get("uniprot_accession"),
                pe.get("entry_name"),
                pe.get("protein_name"),
                pe.get("gene_symbol"),
                pe.get("complex_portal_id"),
            ],
        )
    )
    for field in ("ec_numbers", "interpro_ids", "pfam_ids", "ncbifam_ids"):
        out.extend(pe.get(field) or [])
    for go in pe.get("go_terms") or []:
        out.extend(filter(None, [go.get("id"), go.get("label")]))


def prepare_record_data(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    slug = path.stem
    record_id = doc.get("id") or f"{LOCAL_PREFIX}:{slug}"
    name = doc.get("name", slug)
    material_kind = doc.get("material_kind", "other")
    ima_symbol = (doc.get("ima_symbol") or "").strip()
    polymorph_or_grade = (doc.get("polymorph_or_grade") or "").strip()
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
    protein_tokens: list[str] = []
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
            _collect_protein_example_tokens(pe, protein_tokens)

    causal_graphs = doc.get("causal_graphs") or []
    for cg in causal_graphs:
        for node in cg.get("nodes") or []:
            protein_tokens.extend(filter(None, [node.get("label"), node.get("gene_symbol")]))
            for pe in node.get("protein_examples") or []:
                _collect_protein_example_tokens(pe, protein_tokens)

    # Search text for client-side filter
    search_parts = [
        name,
        record_id,
        slug,
        material_kind,
        ima_symbol,
        polymorph_or_grade,
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
        "id": record_id,
        "name": name,
        "material_kind": material_kind,
        "ima_symbol": ima_symbol,
        "polymorph_or_grade": polymorph_or_grade,
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


def plot_coverage(map_data: dict[str, Any], records_data: list[dict[str, Any]]) -> dict[str, Any]:
    """Restrict the map to records that exist, key its clicks by record id, and say what it omits.

    Point ids are record ids (cmmmech:<slug>), so the click lookup is keyed by
    them; it was keyed by slug and no click opened anything. The map plots the
    records its embedding was computed from: a point whose record is gone is
    dropped, and every record it lacks is returned for the page to list.
    """
    by_id = {r["id"]: r for r in records_data}
    points = map_data.get("points") or []
    plotted = [p for p in points if p[3] in by_id]
    plotted_ids = {p[3] for p in plotted}
    map_data["points"] = plotted
    map_data["hrefs"] = {p[3]: by_id[p[3]]["page"] for p in plotted}
    return {
        "plotted": len(plotted),
        "total": len(records_data),
        "dropped": len(points) - len(plotted),
        "missing": [r for r in records_data if r["id"] not in plotted_ids],
        "fingerprint": map_data.get("corpus_fingerprint", ""),
    }


def feedback_routes(record: dict[str, Any], source_path: str) -> dict[str, str]:
    """A prefilled GitHub issue naming the record and its page, and the edit view of its YAML."""
    page = f"{SITE_URL}pages/{record['page']}"
    query = urlencode({"title": f"Problem with {record['id']}", "body": page}, quote_via=quote)
    return {
        "issue": f"{GITHUB_REPO}/issues/new?{query}",
        "edit": f"{GITHUB_REPO}/edit/main/{source_path}",
    }


def render(out_dir: Path) -> None:
    raw_records = load_records()
    records_data = [prepare_record_data(p, d) for p, d in raw_records]
    env = template_environment(frozenset(r["slug"] for r in records_data))

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

    latest_curation = max(
        (
            str(ch.get("timestamp", ""))[:10]
            for r in records_data
            for ch in (r.get("curation_history") or [])
            if ch.get("timestamp")
        ),
        default="",
    )
    digest_payload = json.dumps(
        [
            (
                r["slug"],
                r["name"],
                r["material_kind"],
                len(r["mechanisms"]),
                len(r.get("curation_history") or []),
            )
            for r in records_data
        ],
        separators=(",", ":"),
    ).encode("utf-8")
    build_provenance = {
        "total_materials": total_materials,
        "total_mechanisms": total_mechanisms,
        "latest_curation": latest_curation,
        "corpus_digest": hashlib.sha256(digest_payload).hexdigest()[:12],
    }
    env.globals["build_provenance"] = build_provenance

    schema = schema_reference()
    reviews_by_path, all_reviews = load_structured_reviews()
    curation = {
        "actors": actor_types(schema, history_sessions()),
        "reviewers": reviewer_kinds(all_reviews),
    }
    curation["human"] = (
        sum(t["sessions"] for t in curation["actors"]["types"] if t["type"] == "human")
        + sum(k["reviews"] for k in curation["reviewers"]["kinds"] if k["kind"] == "human")
    )

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
        curation=curation,
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Readable schema documentation, generated from the LinkML schema.
    schema_html = env.get_template("schema.html").render(root="", schema=schema)
    (out_dir / "schema.html").write_text(schema_html, encoding="utf-8")

    # The not-found page. The Pages workflow copies it to the artifact root,
    # where GitHub serves it for a missing address at any depth.
    not_found_html = env.get_template("404.html").render(root=SITE_ROOT + "pages/")
    (out_dir / "404.html").write_text(not_found_html, encoding="utf-8")

    # Render browse.html
    browse_html = env.get_template("browse.html").render(
        root="",
        records=records_data,
        kinds_counts=kinds_counts,
        process_counts=process_counts,
    )
    (out_dir / "browse.html").write_text(browse_html, encoding="utf-8")

    # Render map.html
    corpus_map_path = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"
    if corpus_map_path.exists():
        map_data = json.loads(corpus_map_path.read_text(encoding="utf-8"))
        shutil.copy(corpus_map_path, out_dir / "corpus_map.json")
    else:
        map_data = {"model": "", "method": "PaCMAP", "n": 0, "classes": [], "points": []}
    coverage = plot_coverage(map_data, records_data)
    map_html = env.get_template("map.html").render(
        root="",
        map_data=map_data,
        map_coverage=coverage,
        map_data_json=json.dumps(map_data, separators=(",", ":")).replace("</", "<\\/"),
        kinds_counts=kinds_counts,
        process_counts=process_counts,
    )
    (out_dir / "map.html").write_text(map_html, encoding="utf-8")

    # Build and render graph.html (material -> process -> organism mechanism network)
    graph_nodes: list[dict[str, Any]] = []
    graph_edges: list[dict[str, Any]] = []
    seen_nodes: set[str] = set()
    for p_id, p_cnt in process_counts:
        nid = f"proc:{p_id}"
        seen_nodes.add(nid)
        graph_nodes.append({
            "id": nid,
            "label": PROCESS_LABELS.get(p_id, p_id.replace("_", " ").title()),
            "type": "process",
            "kind": p_id,
            "href": f"processes/{p_id}.html",
            "count": p_cnt,
        })
    for r in records_data:
        if not r["mechanisms"]:
            continue
        mat_id = f"mat:{r['slug']}"
        if mat_id not in seen_nodes:
            seen_nodes.add(mat_id)
            graph_nodes.append({
                "id": mat_id,
                "label": r["name"],
                "type": "material",
                "kind": r["material_kind"],
                "critical": r["is_critical"],
                "href": r["page"],
                "count": len(r["mechanisms"]),
            })
        for m in r["mechanisms"]:
            proc = m.get("process") or "other"
            proc_nid = f"proc:{proc}"
            graph_edges.append({
                "source": mat_id,
                "target": proc_nid,
                "process": proc,
                "label": m.get("name", proc),
            })
            for org in (m.get("organisms") or [])[:4]:
                oid = org.get("id") or org.get("label") or ""
                if not oid:
                    continue
                org_nid = f"org:{oid}"
                if org_nid not in seen_nodes:
                    seen_nodes.add(org_nid)
                    graph_nodes.append({
                        "id": org_nid,
                        "label": org.get("label", oid),
                        "type": "organism",
                        "kind": "organism",
                        "href": curie_url(oid) or f"browse.html?q={quote(str(org.get('label', oid)))}",
                        "count": 1,
                    })
                graph_edges.append({
                    "source": proc_nid,
                    "target": org_nid,
                    "process": proc,
                    "label": m.get("name", proc),
                })
    graph_data = {"nodes": graph_nodes, "edges": graph_edges}
    graph_html = env.get_template("graph.html").render(
        root="",
        graph_data=graph_data,
        graph_data_json=json.dumps(graph_data, separators=(",", ":")).replace("</", "<\\/"),
        kinds_counts=kinds_counts,
        process_counts=process_counts,
    )
    (out_dir / "graph.html").write_text(graph_html, encoding="utf-8")

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
        rendered_r["ima_symbol"] = r["ima_symbol"]
        rendered_r["polymorph_or_grade"] = r["polymorph_or_grade"]
        rendered_r["identifiers"] = r["identifiers"]
        rendered_r["slug"] = r["slug"]
        rendered_r["id"] = r["id"]
        source_path = p.relative_to(REPO_ROOT).as_posix()

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
            reviews=reviews_by_path.get(source_path, []),
            feedback=feedback_routes(r, source_path),
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
        root_index_path = REPO_ROOT / "index.html"
        if not root_index_path.exists() or root_index_path.read_text(encoding="utf-8") != root_index:
            root_index_path.write_text(root_index, encoding="utf-8")


def _remove_tree(path: Path) -> bool:
    """Remove a directory tree, falling back to path-based unlinking when dir_fd unlinkat is blocked."""
    try:
        shutil.rmtree(path)
        return True
    except PermissionError:
        removed_all = True
        for child in sorted(path.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            try:
                if child.is_file() or child.is_symlink():
                    child.unlink()
                elif child.is_dir():
                    child.rmdir()
            except PermissionError:
                removed_all = False
        if removed_all:
            try:
                path.rmdir()
                return True
            except PermissionError:
                return False
        return False


def _sync_rendered_tree(src: Path, dst: Path) -> None:
    """Synchronize rendered files from src into dst, updating only changed files and pruning stale paths."""
    if dst.exists() and _remove_tree(dst):
        shutil.copytree(src, dst)
        return

    dst.mkdir(parents=True, exist_ok=True)
    src_rel_files: set[Path] = set()
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            src_rel_files.add(rel)
            data = item.read_bytes()
            if not target.exists() or target.read_bytes() != data:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)

    for existing in sorted(dst.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        rel = existing.relative_to(dst)
        if existing.is_file() or existing.is_symlink():
            if rel not in src_rel_files:
                existing.unlink()
        elif existing.is_dir() and not (src / rel).exists():
            existing.rmdir()


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

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        render(tmp_path)
        _sync_rendered_tree(tmp_path, args.out)
    if args.out.resolve() == PAGES_DIR.resolve():
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
        root_index_path = REPO_ROOT / "index.html"
        if not root_index_path.exists() or root_index_path.read_text(encoding="utf-8") != root_index:
            root_index_path.write_text(root_index, encoding="utf-8")
    print(f"Rendered CMMMech site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
