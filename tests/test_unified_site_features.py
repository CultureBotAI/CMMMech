"""X-Mech unified website features on the CMMMech site (wave 1, 2026-10-25).

Covers what the 2026-10-25 review left partial or missing: references in record
prose are followable and record ids cited in it open their record (evidence),
EC numbers, proteomes and organisms resolve (term_links), a record's own id is
shown and searchable (search), saved structured reviews are shown with what they
do and do not establish (review_status, curation_notice), map clicks open the
right record and the map says which records it omits (text_map), a table
alternative for each canvas (visual_alternative), detail tables that scroll in
their own region (responsive), verified sibling routes (cross_mech_links),
readable schema documentation (schema_docs), the deploy-time complete export
(downloads), the licence footer, a skip link, a not-found page and a per-record
feedback route. Each test is driven by an input on which the old rendering and
the new one differ.
"""

from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import re
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
TEMPLATES = ROOT / "src" / "cmmmech" / "templates"
GH = "https://github.com/CultureBotAI/CMMMech/blob/main"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


render_pages = _load("render_pages")
export_records = _load("export_records")


class Page(HTMLParser):
    """Anchors with their text, footer links and text, ids, and text outside anchors."""

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.anchors: list[tuple[dict, str]] = []
        self.footer_links: list[str] = []
        self.footer_text: list[str] = []
        self.text: list[str] = []
        self.outside_anchor_text: list[str] = []
        self.ids: set[str] = set()
        self.tags: list[str] = []
        self._open: list[tuple[dict, list[str]]] = []
        self._footer = 0
        self._skip = 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "footer":
            self._footer += 1
        if tag == "a":
            self._open.append((attrs, []))
            if self._footer:
                self.footer_links.append(attrs.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "a" and self._open:
            attrs, text = self._open.pop()
            self.anchors.append((attrs, " ".join("".join(text).split())))
        if tag == "footer":
            self._footer -= 1
        if tag in ("script", "style"):
            self._skip -= 1

    def handle_data(self, data):
        if self._skip:
            return
        self.text.append(data)
        for _, text in self._open:
            text.append(data)
        if not self._open:
            self.outside_anchor_text.append(data)
        if self._footer:
            self.footer_text.append(data)

    def hrefs(self) -> list[str]:
        return [attrs.get("href", "") for attrs, _ in self.anchors]

    def anchor(self, href: str) -> tuple[dict, str]:
        matches = [(attrs, text) for attrs, text in self.anchors if attrs.get("href") == href]
        assert matches, f"no anchor to {href}"
        return matches[0]

    def plain_text(self) -> str:
        return " ".join("".join(self.text).split())

    def unlinked_text(self) -> str:
        return " ".join("".join(self.outside_anchor_text).split())

    def footer(self) -> str:
        return " ".join("".join(self.footer_text).split())


def section(html: str, pattern: str) -> str:
    match = re.search(pattern, html, re.S)
    assert match, f"section {pattern!r} not found"
    return match.group(0)


def record(**fields) -> dict:
    """A synthetic record in prepare_record_data's shape; not scientific content."""
    base = {"id": "cmmmech:synthetic-material", "slug": "synthetic-material",
            "name": "Synthetic material", "material_kind": "commodity",
            "description": "Synthetic fixture.", "identifiers": [], "sources": [],
            "mechanisms": [], "causal_graphs": [], "criticality": [], "curation_history": []}
    return {**base, **fields}


def render_material(r: dict, *, slugs=("synthetic-material", "other-material"), **context) -> str:
    env = render_pages.template_environment(frozenset(slugs))
    values = {"root": "../", "source_path": f"data/records/{r['slug']}.yaml", **context}
    return env.get_template("material.html").render(r=r, **values)


def autolink(text: str, *, slugs=("synthetic-material", "other-material"), own="synthetic-material",
             root="../") -> str:
    env = render_pages.template_environment(frozenset(slugs))
    template = env.from_string("{{ value | autolink }}")
    return template.render(value=text, root=root, r={"slug": own})


# ---------------------------------------------------------------- evidence --

LINKED_TOKENS = [
    ("Canadian Mineralogist 38:1457-1466, DOI 10.2113/gscanmin.38.6.1457. Complete",
     "https://doi.org/10.2113/gscanmin.38.6.1457", "DOI 10.2113/gscanmin.38.6.1457"),
    ("(PMID:26236307; DOI:10.3389/fmicb.2015.00734; strain T-1)",
     "https://pubmed.ncbi.nlm.nih.gov/26236307/", "PMID:26236307"),
    ("(PMID:26236307; DOI:10.3389/fmicb.2015.00734; strain T-1)",
     "https://doi.org/10.3389/fmicb.2015.00734", "DOI:10.3389/fmicb.2015.00734"),
    ("e06275; PMID 33681496; PMC7930292.", "https://pubmed.ncbi.nlm.nih.gov/33681496/",
     "PMID 33681496"),
    ("e06275; PMID 33681496; PMC7930292.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7930292/",
     "PMC7930292"),
    ("PMCID PMC13185686.1. Complete", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13185686/",
     "PMC13185686"),
    ("Huang et al. (2024), DOI 10.1016/j.jenvman.2023.119868, whose",
     "https://doi.org/10.1016/j.jenvman.2023.119868", "DOI 10.1016/j.jenvman.2023.119868"),
    ("bare 10.1371/journal.pbio.3002726.s002) here",
     "https://doi.org/10.1371/journal.pbio.3002726.s002", "10.1371/journal.pbio.3002726.s002"),
    ("pdf at https://example.org/a/b.pdf.", "https://example.org/a/b.pdf",
     "https://example.org/a/b.pdf"),
    ("(https://en.wikipedia.org/wiki/Foo_(bar))", "https://en.wikipedia.org/wiki/Foo_(bar)",
     "https://en.wikipedia.org/wiki/Foo_(bar)"),
    ("cross-represented in cmmmech:other-material; not", "../materials/other-material.html",
     "cmmmech:other-material"),
    ("elemental iron (cmmmech:other-material), a", "../materials/other-material.html",
     "cmmmech:other-material"),
]


@pytest.mark.parametrize("text,href,label", LINKED_TOKENS)
def test_autolink_links_reference_tokens_and_keeps_surrounding_text(text, href, label):
    page = Page(autolink(text))
    _, anchor_text = page.anchor(href)
    assert anchor_text == label
    # The text a reader sees is unchanged: only the token became an anchor.
    assert page.plain_text() == " ".join(text.split())


UNLINKED_TEXT = [
    "Natural falcondoite fibers",                      # "doi" inside a word
    "the 2022 DOI/USGS Final List of Critical Minerals",  # Department of the Interior
    "javascript:alert(1)", "https://user:pw@evil.example/", "https://",
    "PMID:not-a-number", "PMC12 is too short", "source key pmc11811698",
    "version v10.1234/abc", "cmmmech:no-such-record here",
    "this record, cmmmech:synthetic-material, itself",  # the page's own record
    "ISBN 978-84-7993-915-1.",
]


@pytest.mark.parametrize("text", UNLINKED_TEXT)
def test_autolink_leaves_unsafe_or_non_reference_text_unlinked(text):
    page = Page(autolink(text))
    assert page.anchors == []
    assert page.plain_text() == " ".join(text.split())


def test_autolink_escapes_markup_and_cannot_break_out_of_the_attribute():
    page = Page(autolink('<script>alert(1)</script> https://example.org/x" onclick="alert(2) &'))
    assert "script" not in page.tags
    assert page.hrefs() == ["https://example.org/x"]
    assert not any(key.startswith("on") for attrs, _ in page.anchors for key in attrs)
    assert "<script>alert(1)</script>" in page.plain_text()
    assert autolink(None) == ""


MARKDOWN_TOKENS = [
    ("[10.1038/nrmicro2166](https://doi.org/10.1038/nrmicro2166)",
     ["https://doi.org/10.1038/nrmicro2166", "https://doi.org/10.1038/nrmicro2166"]),
    ("[https://example.org/x](https://example.org/x)", ["https://example.org/x", "https://example.org/x"]),
    ("**10.1099/ijs.0.003251-0**", ["https://doi.org/10.1099/ijs.0.003251-0"]),
    ("`10.1146/annurev-cellbio-101011-155745`",
     ["https://doi.org/10.1146/annurev-cellbio-101011-155745"]),
    ("see **https://example.org/y**, and `https://example.org/z`.",
     ["https://example.org/y", "https://example.org/z"]),
]


@pytest.mark.parametrize("text,hrefs", MARKDOWN_TOKENS)
def test_autolink_stops_at_markdown_syntax(text, hrefs):
    """Markdown marks are not part of a DOI or URL (TraitMech #2022)."""
    page = Page(autolink(text))
    assert page.hrefs() == hrefs
    assert page.plain_text() == text


PARENTHESIZED_TOKENS = [
    # Two parenthesized URLs with nothing but "-" between them are two links,
    # not one href running from the first to the second (TraitMech #2033).
    ("(https://a.example/x)-(https://b.example/y)", ["https://a.example/x", "https://b.example/y"]),
    # What the cut leaves behind is scanned again for the next reference.
    ("(https://a.example/x)-(PMID:12)", ["https://a.example/x", "https://pubmed.ncbi.nlm.nih.gov/12/"]),
    ("(10.1000/a)-(10.2000/b)", ["https://doi.org/10.1000/a", "https://doi.org/10.2000/b"]),
    # Parentheses opened inside the token stay in it.
    ("(https://en.wikipedia.org/wiki/Foo_(bar))", ["https://en.wikipedia.org/wiki/Foo_(bar)"]),
    ("(see 10.1016/0005-2744(70)90044-4)", ["https://doi.org/10.1016/0005-2744(70)90044-4"]),
]


@pytest.mark.parametrize("text,hrefs", PARENTHESIZED_TOKENS)
def test_autolink_ends_a_token_at_a_parenthesis_it_never_opened(text, hrefs):
    page = Page(autolink(text))
    assert page.hrefs() == hrefs
    assert page.plain_text() == text


def test_record_page_links_references_in_every_prose_field():
    """Each surface the review found carrying plain identifiers, plus the other prose fields."""
    protein = {"uniprot_accession": "UniProtKB:Q747K6", "protein_name": "Synthetic protein",
               "entry_status": "SWISS_PROT", "functional_role": "Role, see PMID:5.",
               "target_organism": {"id": "NCBITaxon:35554", "label": "Geobacter sulfurreducens"},
               "annotation_note": "Linked by PMID:6."}
    r = record(
        description="Same study as cmmmech:other-material (DOI 10.1000/desc).",
        criticality=[{"jurisdiction": "X", "list_name": "L", "edition": "PMID 1 edition",
                      "classification": "critical", "source_ref": "s"}],
        mechanisms=[{"id": "m", "name": "Mechanism", "process": "other", "microbial": True,
                     "description": "See PMID:2.", "context": "Methods in PMC1234567.",
                     "organisms": [], "protein_examples": [protein],
                     "evidence": [{"source_ref": "s", "supports": "support",
                                   "explanation": "Table 2 of DOI:10.1000/expl."}]}],
        causal_graphs=[{"id": "g", "name": "Graph", "scope": "BROAD_MECHANISM",
                        "description": "After https://example.org/graph",
                        "nodes": [{"id": "n", "label": "Node", "node_type": "GENE_OR_PROTEIN",
                                   "protein_grounding_status": "GROUNDED",
                                   "description": "Node PMID:3.",
                                   "protein_examples": [{**protein, "functional_role": "Node role, PMID:8.",
                                                         "annotation_note": "Node PMID:7."}]}],
                        "edges": [{"source": "n", "target": "n", "predicate": "binds",
                                   "description": "Edge PMID:4."}]}],
        sources=[{"id": "s", "title": "Journal 1:2-3, DOI 10.1000/title. Complete PDF.",
                  "url": "https://example.org/pdf", "accessed_on": "2026-10-25"}],
        curation_history=[{"timestamp": "2026-10-25T00:00:00Z", "curator": "codex",
                           "action": "EDIT", "summary": "Added PMC7654321 tables."}],
    )
    hrefs = set(Page(render_material(r)).hrefs())
    for expected in [
        "../materials/other-material.html",              # description: cited record
        "https://doi.org/10.1000/desc",                   # description
        "https://pubmed.ncbi.nlm.nih.gov/1/",             # criticality edition
        "https://pubmed.ncbi.nlm.nih.gov/2/",             # mechanism description
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/",  # mechanism context
        "https://doi.org/10.1000/expl",                   # evidence explanation
        "https://pubmed.ncbi.nlm.nih.gov/5/",             # protein functional role
        "https://pubmed.ncbi.nlm.nih.gov/6/",             # protein annotation note
        "https://example.org/graph",                      # causal graph description
        "https://pubmed.ncbi.nlm.nih.gov/3/",             # causal node description
        "https://pubmed.ncbi.nlm.nih.gov/7/",             # causal node protein note
        "https://pubmed.ncbi.nlm.nih.gov/8/",             # causal node protein role
        "https://pubmed.ncbi.nlm.nih.gov/4/",             # causal edge description
        "https://doi.org/10.1000/title",                  # source title
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7654321/",  # curation summary
    ]:
        assert expected in hrefs, expected


# PMCIDs are upper case; a lower-case "pmc11811698" is a record-local source key.
REFERENCE_TOKEN = re.compile(r"(?<![\w./])10\.[0-9]{4,9}/\S+|\b(?i:pmid)(?::\s?|\s)[0-9]+|\bPMC[0-9]{4,9}\b")


def test_committed_record_pages_link_every_cited_reference_and_record():
    """The review's acceptance check: no DOI, PMID or PMCID left as text on any record page."""
    pages = sorted((PAGES / "materials").glob("*.html"))
    assert len(pages) == len(list((ROOT / "data" / "records").glob("*.yaml")))
    unlinked: dict[str, list[str]] = {}
    linked = 0
    for path in pages:
        page = Page(path.read_text(encoding="utf-8"))
        text = page.unlinked_text()
        found = REFERENCE_TOKEN.findall(text)
        found += [t for t in re.findall(r"\bcmmmech:[a-z][a-z0-9-]*", text) if t != f"cmmmech:{path.stem}"]
        if found:
            unlinked[path.stem] = found
        linked += sum(href.startswith(("https://doi.org/", "https://pubmed.ncbi.nlm.nih.gov/",
                                       "https://pmc.ncbi.nlm.nih.gov/")) for href in page.hrefs())
    assert unlinked == {}
    assert linked > 600  # not vacuous: the corpus cites hundreds in prose


# -------------------------------------------------------------- term_links --

@pytest.mark.parametrize("curie,expected", [
    ("EC:1.8.5.4", "https://enzyme.expasy.org/EC/1.8.5.4"),
    ("EC:3.12.1.-", "https://enzyme.expasy.org/EC/3.12.1.-"),
    ("CHEBI:27638", "https://www.ebi.ac.uk/chebi/CHEBI:27638"),
    ("NCBIfam:TIGR01234", "https://www.ebi.ac.uk/interpro/entry/ncbifam/TIGR01234"),
    ("NCIT:C12345", "https://bioregistry.io/NCIT:C12345"),
    ("IMA:1962-004", None),            # bioregistry.io has no IMA prefix
    ("cmmmech:cobalt", None),          # own records resolve to their pages, not a registry
    ("not a curie", None),
    ("X:<y>", None),
    ("", None),
])
def test_curie_resolver_map_with_registry_fallback(curie, expected):
    assert render_pages.curie_url(curie) == expected


def test_proteome_ids_resolve_to_uniprot_proteomes():
    assert render_pages.proteome_url("UP000000531") == "https://www.uniprot.org/proteomes/UP000000531"
    assert render_pages.proteome_url("UP0000005") is None
    assert render_pages.proteome_url(None) is None


def test_protein_example_organisms_and_proteomes_are_linked_in_both_tables():
    protein = {"uniprot_accession": "UniProtKB:Q747K6", "protein_name": "Synthetic protein",
               "entry_status": "SWISS_PROT", "functional_role": "Role.",
               "target_organism": {"id": "NCBITaxon:35554", "label": "Geobacter sulfurreducens"},
               "reference_proteome_id": "UP000000577", "ec_numbers": ["EC:1.8.5.4"]}
    r = record(
        mechanisms=[{"id": "m", "name": "Mechanism", "process": "other", "microbial": True,
                     "description": "d", "context": "c", "organisms": [],
                     "protein_examples": [protein], "evidence": []}],
        causal_graphs=[{"id": "g", "name": "Graph", "scope": "BROAD_MECHANISM", "description": "d",
                        "nodes": [{"id": "n", "label": "Node", "node_type": "GENE_OR_PROTEIN",
                                   "protein_grounding_status": "GROUNDED",
                                   "protein_examples": [protein]}],
                        "edges": [{"source": "n", "target": "n", "predicate": "binds"}]}],
    )
    html = render_material(r)
    taxon = render_pages.curie_url("NCBITaxon:35554")
    table = Page(section(html, r'<th scope="col">UniProtKB</th>.*?</table>'))
    assert "NCBITaxon:35554" in [text for attrs, text in table.anchors if attrs["href"] == taxon]
    assert table.anchor("https://www.uniprot.org/proteomes/UP000000577")[1] == "UP000000577"
    assert table.anchor("https://enzyme.expasy.org/EC/1.8.5.4")[1] == "EC:1.8.5.4"
    nodes = Page(section(html, r'<th scope="col">Node</th>.*?</table>'))
    assert nodes.anchor(taxon)[1] == "Geobacter sulfurreducens (NCBITaxon:35554)"
    assert nodes.anchor("https://www.uniprot.org/proteomes/UP000000577")[1] == "UP000000577"


def test_no_committed_page_links_the_retired_intenz_service():
    pages = sorted(PAGES.rglob("*.html"))
    assert [p.name for p in pages if "ebi.ac.uk/intenz" in p.read_text(encoding="utf-8")] == []
    ec_links = sum(p.read_text(encoding="utf-8").count('href="https://enzyme.expasy.org/EC/')
                   for p in pages)
    assert ec_links > 100


# ------------------------------------------------------------------ search --

def test_own_identifier_is_searchable_and_shown():
    path = ROOT / "data" / "records" / "cobalt.yaml"
    prepared = render_pages.prepare_record_data(path, yaml.safe_load(path.read_text(encoding="utf-8")))
    assert prepared["id"] == "cmmmech:cobalt"
    assert "cmmmech:cobalt" in prepared["search_text"]
    browse = (PAGES / "browse.html").read_text(encoding="utf-8")
    row = section(browse, r'<tr data-name="cobalt".*?</tr>')
    assert 'cmmmech:cobalt' in re.search(r'data-search="([^"]*)"', row).group(1)
    assert "<code>cmmmech:cobalt</code>" in section(row, r"<td>\s*<div><code>cmmmech:.*?</td>")
    cobalt = (PAGES / "materials" / "cobalt.html").read_text(encoding="utf-8")
    header = Page(section(cobalt, r'<p class="record-id">.*?</p>'))
    assert header.anchor(f"{GH}/data/records/cobalt.yaml")[1] == "cmmmech:cobalt"


def test_an_exact_own_id_query_selects_that_record_alone():
    """cmmmech:cobalt begins cmmmech:cobaltite, so a substring match answered it with three rows.

    The listing filter is client-side; the browser pass exercises it. This pins
    the data it reads and the rule it applies.
    """
    browse = (PAGES / "browse.html").read_text(encoding="utf-8")
    ids = re.findall(r'<tr data-name="[^"]*"\s+data-id="([^"]+)"', browse)
    assert sorted(ids) == sorted(f"cmmmech:{p.stem}" for p in (ROOT / "data" / "records").glob("*.yaml"))
    assert [i for i in ids if i != "cmmmech:cobalt" and i.startswith("cmmmech:cobalt")]
    js = (TEMPLATES / "record-browser.js").read_text(encoding="utf-8")
    assert "id: (row.dataset.id || '').toLowerCase()," in js
    assert "var exactId = term && rows.some(function (r) { return r.id === term; }) ? term : '';" in js
    assert "var matchText = exactId ? r.id === exactId : (!term || r.text.indexOf(term) !== -1);" in js


# ---------------------------------------------- review_status, curation_notice --

def review(review_id, finished_at, kind="record", verdict="pass_with_limitations", **extra):
    return {"review_id": review_id, "kind": kind, "title": f"Review {review_id}",
            "finished_at": finished_at, "verdict": verdict, "completion": "completed",
            "scientific_review": True, "reviewer_kind": "agent", "reviewer_model": "GPT-6",
            "markdown": f"reviews/structured/{review_id}/review.md", **extra}


def test_structured_reviews_index_every_record_newest_first(tmp_path):
    saved = tmp_path / "structured"
    # Same finish time for a record and a category review, named so that id order
    # alone would put the category review first.
    for review_id, finished, kind, paths in [
        ("a-old", "2026-10-01T00:00:00Z", "record", ["data/records/x.yaml"]),
        ("c-category", "2026-10-02T00:00:00Z", "category", ["data/records/x.yaml", "data/records/y.yaml"]),
        ("b-record", "2026-10-02T00:00:00Z", "record", ["data/records/x.yaml", "data/records/x.yaml"]),
    ]:
        (saved / review_id).mkdir(parents=True)
        (saved / review_id / "review.yaml").write_text(yaml.safe_dump({
            "review_id": review_id, "kind": kind, "title": review_id, "finished_at": finished,
            "verdict": "pass", "completion": "completed", "scientific_review": True,
            "reviewer": {"kind": "agent", "model": "m"},
            "targets": [{"path": path} for path in paths]}), encoding="utf-8")
    index, everything = render_pages.load_structured_reviews(saved)
    # The same finish time: a record review outranks a category review, and a
    # review naming the same file twice is listed once.
    assert [r["review_id"] for r in index["data/records/x.yaml"]] == ["b-record", "c-category", "a-old"]
    assert [r["review_id"] for r in index["data/records/y.yaml"]] == ["c-category"]
    assert len(everything) == 3


def test_every_record_has_its_saved_reviews_on_its_page():
    index, _ = render_pages.load_structured_reviews()
    records = sorted((ROOT / "data" / "records").glob("*.yaml"))
    for path in records[::40]:
        rel = path.relative_to(ROOT).as_posix()
        reviews = index.get(rel, [])
        html = (PAGES / "materials" / f"{path.stem}.html").read_text(encoding="utf-8")
        if not reviews:
            assert "none is saved for this record" in html
            continue
        table = Page(section(html, r'<div class="detail-section" id="structured-reviews">.*?</table>'))
        assert [href for href in table.hrefs()] == [f"{GH}/{r['markdown']}" for r in reviews]
        status = Page(section(html, r'<div class="review-status">.*?</p>'))
        assert reviews[0]["finished_at"][:10] in status.plain_text()
        assert reviews[0]["verdict"].replace("_", " ") in status.plain_text()


def test_record_page_shows_the_latest_review_and_lists_all_of_them():
    reviews = [review("new", "2026-10-24T02:45:00Z", kind="category", verdict="needs_curation",
                      completion="partial", scientific_review=False, reviewer_model="claude"),
               review("old", "2026-10-10T01:18:41Z")]
    html = render_material(record(), reviews=reviews)
    status = Page(section(html, r'<div class="review-status">.*?</p>')).plain_text()
    assert status == ("Latest structured review: needs curation (partial), 2026-10-24, category review "
                      "by an agent reviewer (claude); not a scientific review · all 2 saved reviews")
    rows = Page(section(html, r'id="structured-reviews">.*?</table>'))
    assert rows.hrefs() == [f"{GH}/reviews/structured/new/review.md", f"{GH}/reviews/structured/old/review.md"]
    assert "pass with limitations" in rows.plain_text()


def test_record_page_without_a_saved_review_says_so():
    html = render_material(record(), reviews=[])
    assert "Structured review: none is saved for this record." in Page(
        section(html, r'<div class="review-status">.*?</p>')).plain_text()
    assert 'id="structured-reviews"' not in html


def normalized(path: str) -> str:
    return " ".join((ROOT / path).read_text(encoding="utf-8").split())


@pytest.mark.parametrize("key", sorted(render_pages.CURATION_QUOTES))
def test_curation_quotes_are_verbatim_in_their_sources(key):
    source, quote = render_pages.CURATION_QUOTES[key]
    assert quote in normalized(source)


def test_record_page_explains_the_status_in_the_repositorys_words():
    html = render_material(record(), reviews=[review("r", "2026-10-24T00:00:00Z")])
    disclosure = Page(section(html, r'<details class="status-meaning">.*?</details>'))
    text = disclosure.plain_text()
    assert text.startswith("What this review status means")
    for key in ("observation", "report", "passing", "qualified", "newer"):
        assert render_pages.CURATION_QUOTES[key][1].replace("`", "") in text
    assert f"{GH}/docs/record-reviews.md" in disclosure.hrefs()


def landing(curation: dict) -> str:
    env = render_pages.template_environment()
    return env.get_template("index.html").render(
        root="", total_materials=2, total_mechanisms=0, materials_with_mechs=0,
        critical_materials_count=0, kinds=[], processes=[], featured=[], curation=curation)


def test_landing_counts_history_actor_types_and_reviewer_kinds_from_the_data():
    schema = render_pages.schema_reference()
    sessions = [{"actors": [{"type": "ai_agent"}]}, {"actors": [{"type": "ai_agent"}]},
                {"actors": [{"type": "human"}, {"type": "ai_agent"}]}]
    curation = {"actors": render_pages.actor_types(schema, sessions),
                "reviewers": render_pages.reviewer_kinds([review("a", "t"), review("b", "t")]),
                "human": 1}
    notice = Page(section(landing(curation), r'<section id="curation".*?</section>'))
    text = notice.plain_text()
    assert "History sessions (3)" in text
    assert "ai_agent: 3 sessions An LLM-driven agent, whether human-supervised or autonomous." in text
    assert "human: 1 session A person working directly." in text
    assert "human 0, agent 2, deterministic 0" in text
    # Only said when the data says it.
    assert "No saved history session has a human actor" not in text
    curation["human"] = 0
    assert "No saved history session has a human actor" in Page(
        section(landing(curation), r'<section id="curation".*?</section>')).plain_text()


def test_committed_landing_states_the_corpus_actor_types():
    actors = render_pages.actor_types(render_pages.schema_reference(), render_pages.history_sessions())
    agent = next(t for t in actors["types"] if t["type"] == "ai_agent")
    notice = Page(section((PAGES / "index.html").read_text(encoding="utf-8"),
                          r'<section id="curation".*?</section>')).plain_text()
    assert f"History sessions ({actors['total']:,})" in notice
    assert f"ai_agent: {agent['sessions']:,} sessions" in notice
    assert actors["total"] > 1000


# ---------------------------------------------------------------- text_map --

def test_map_clicks_are_keyed_by_record_id_and_points_without_a_record_are_dropped():
    records = [{"id": "cmmmech:a", "page": "materials/a.html", "name": "A"},
               {"id": "cmmmech:b", "page": "materials/b.html", "name": "B"}]
    data = {"corpus_fingerprint": "f", "points": [[0, 0, 0, "cmmmech:a", "A", []],
                                                  [1, 1, 0, "cmmmech:gone", "Gone", []]]}
    coverage = render_pages.plot_coverage(data, records)
    assert data["hrefs"] == {"cmmmech:a": "materials/a.html"}
    assert [p[3] for p in data["points"]] == ["cmmmech:a"]
    assert (coverage["plotted"], coverage["total"], coverage["dropped"]) == (1, 2, 1)
    assert [r["id"] for r in coverage["missing"]] == ["cmmmech:b"]


def committed_map() -> tuple[str, dict]:
    html = (PAGES / "map.html").read_text(encoding="utf-8")
    data = json.loads(section(html, r'(?<=<script id="corpus-map-data" type="application/json">).*?(?=</script>)'))
    return html, data


def test_every_committed_map_point_opens_its_own_record_page():
    _, data = committed_map()
    assert len(data["points"]) > 500
    for point in data["points"]:
        href = data["hrefs"][point[3]]
        assert href == f"materials/{point[3].split(':', 1)[1]}.html"
        assert (PAGES / href).is_file()


def test_map_says_how_many_records_it_plots_and_lists_the_rest():
    html, data = committed_map()
    slugs = {path.stem for path in (ROOT / "data" / "records").glob("*.yaml")}
    plotted = {point[3].split(":", 1)[1] for point in data["points"]}
    coverage = Page(section(html, r'<p class="map-coverage".*?</p>')).plain_text()
    assert f"The map plots {len(plotted)} of the {len(slugs)} records." in coverage
    listed = Page(section(html, r'<section class="detail-section" id="map-missing".*?</section>'))
    assert sorted(href for href in listed.hrefs()) == sorted(f"materials/{s}.html" for s in slugs - plotted)
    assert slugs - plotted, "every record is plotted; this test no longer exercises the list"


# ------------------------------------------------------- visual_alternative --

@pytest.mark.parametrize("page,table,builder", [
    ("map.html", "map-table", "D.points"), ("graph.html", "graph-table", "= activeSet();"),
])
def test_each_canvas_has_a_keyboard_reachable_table_built_from_its_own_data(page, table, builder):
    html = (PAGES / page).read_text(encoding="utf-8")
    details = section(html, rf'<details class="visual-table" id="{table}-details">.*?</details>')
    assert re.search(r"<summary>View the .+? as a table</summary>", details)
    assert f'<table id="{table}">' in details and "<thead>" in details
    region = re.search(r'<div class="record-table-scroll"([^>]*)>', details).group(1)
    assert 'role="region"' in region and 'tabindex="0"' in region and "aria-label=" in region
    assert "<noscript>" in details
    script = section(html, r"function renderTable\(\) \{.*?\n  \}")
    assert "tableDetails.open" in script and builder in script and "textContent" in script
    assert "innerHTML" not in script
    assert "tableDetails.addEventListener('toggle', renderTable)" in html
    assert re.search(r'<canvas id="[^"]+"[^>]* role="img" aria-label="[^"]+"', html)


# -------------------------------------------------------------- responsive --

def test_every_record_page_table_scrolls_in_a_named_region():
    region = re.compile(r'<div class="record-table-scroll[^"]*" role="region" aria-label="[^"]+" tabindex="0">\s*<table')
    for path in sorted((PAGES / "materials").glob("*.html")):
        html = path.read_text(encoding="utf-8")
        assert html.count("<table") == len(region.findall(html)), path.name


def test_header_nav_wraps_whole_words():
    css = (TEMPLATES / "style.css").read_text(encoding="utf-8")
    nav = section(css, r"\nheader nav \{.*?\}")
    link = section(css, r"\nheader nav a \{.*?\}")
    assert "flex-wrap: wrap" in nav
    assert "white-space: nowrap" in link


def test_narrow_layout_column_cannot_outgrow_the_viewport():
    """A bare 1fr track grows to its widest item's min-content; minmax(0, 1fr) cannot.

    Measured at 320 and 390 px with the map and graph tables open, the page did
    not widen before this rule either (.browse-main has min-width: 0); this
    keeps the single-column layout safe for any item, not just that one.
    """
    css = (TEMPLATES / "style.css").read_text(encoding="utf-8")
    narrow = section(css, r"@media \(max-width: 860px\) \{.*?\n\}")
    assert re.search(r"\.browse-layout \{\s*grid-template-columns: minmax\(0, 1fr\);", narrow)


def test_detail_table_cells_keep_whole_words():
    """body's overflow-wrap:anywhere let a scrolled table crush a column and split its words."""
    css = (TEMPLATES / "style.css").read_text(encoding="utf-8")
    assert "overflow-wrap: anywhere;" in section(css, r"\nbody \{.*?\}")
    assert ".detail-table-scroll th, .detail-table-scroll td { overflow-wrap: break-word; }" in css


@pytest.mark.parametrize("template", ["map.html", "graph.html"])
def test_canvas_takes_the_wrapper_width_without_a_floor(template):
    source = (TEMPLATES / template).read_text(encoding="utf-8")
    resize = section(source, r"function resize\(\) \{.*?\n  \}")
    assert "Math.max(360" not in resize
    assert "canvas.parentElement.clientWidth" in resize


# -------------------------------------------------------- cross_mech_links --

# The fleet's verified sibling routes (X-Mech unified standard, each loaded live
# with HTTP 200 and its query applied on 2026-10-25). A link elsewhere on a
# sibling site is a guess nothing here can check.
VERIFIED_SIBLING_ROUTES = (
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/PathwayMech/pages/records/",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
)
# The footer's sibling-site links carry no query: each must be exactly a site
# root (every one answered HTTP 200 on 2026-10-25), as must the suite directory.
SIBLING_SITE_ROOTS = {f"https://culturebotai.github.io/{name}/" for name in (
    "CultureMech", "MediaIngredientMech", "CommunityMech", "TraitMech", "proteintraitsmech",
    "AntibioticMech", "CellStructureMech", "NaturalProductMech", "DUFMech", "PathwayMech",
    "TaxonMech", "HabitatMech", "AIMech", "mechs")}
FLEET_URL = re.compile(r"https?://culturebotai\.github\.io/[^\s\"'<>)]*")


def unverified_sibling_urls(text: str) -> set[str]:
    return {url for url in FLEET_URL.findall(text)
            if not url.startswith("https://culturebotai.github.io/CMMMech/")
            and url not in SIBLING_SITE_ROOTS and not url.startswith(VERIFIED_SIBLING_ROUTES)}


def test_sibling_links_in_renderer_sources_use_verified_routes():
    sources = [*sorted(TEMPLATES.glob("*.html")), *sorted(TEMPLATES.glob("*.js")),
               ROOT / "scripts" / "render_pages.py"]
    found = {path.name: unverified_sibling_urls(path.read_text(encoding="utf-8")) for path in sources}
    assert {name: urls for name, urls in found.items() if urls} == {}


def test_every_sibling_link_in_the_built_site_uses_a_verified_route():
    built = sorted(PAGES.rglob("*.html"))
    assert len(built) > 650
    emitted: set[str] = set()
    bad: dict[str, set[str]] = {}
    for path in built:
        text = path.read_text(encoding="utf-8")
        emitted |= set(FLEET_URL.findall(text))
        if urls := unverified_sibling_urls(text):
            bad[path.relative_to(PAGES).as_posix()] = urls
    assert bad == {}
    # Not vacuous: organisms open their TaxonMech records.
    assert sum(url.startswith("https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:")
               for url in emitted) > 100


def test_organisms_open_their_taxonmech_record_and_others_search_it():
    assert (render_pages.taxonmech_url({"id": "NCBITaxon:35554", "label": "Geobacter"})
            == "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:35554")
    assert (render_pages.taxonmech_url({"id": "TEST:organism", "label": "Test organism"})
            == "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=Test%20organism")


# ------------------------------------------------------------- schema_docs --

def test_schema_reference_documents_every_class_slot_and_enum():
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(ROOT / "src/cmmmech/schema/cmmmech.yaml"))
    reference = render_pages.schema_reference()
    assert reference["classes"][0]["name"] == "CriticalMineralRecord"
    assert {c["name"] for c in reference["classes"]} == set(view.all_classes())
    assert {e["name"] for e in reference["enums"]} == set(view.all_enums())
    root = reference["classes"][0]
    assert [s["name"] for s in root["slots"]] == [s.name for s in view.class_induced_slots(root["name"])]
    slots = {s["name"]: s for s in root["slots"]}
    assert slots["id"]["identifier"] and slots["id"]["required"]
    assert slots["id"]["pattern"] == "^cmmmech:[a-z][a-z0-9-]*$"
    assert slots["mechanisms"]["multivalued"]
    assert slots["mechanisms"]["ranges"] == [{"name": "Mechanism", "kind": "class"}]
    assert slots["name"]["ranges"] == [{"name": "NonEmptyText", "kind": "type"}]
    process = next(e for e in reference["enums"] if e["name"] == "ProcessType")
    assert "recycling" in {v["text"] for v in process["permissible"]}


def test_an_identifier_slot_is_documented_as_required_even_when_not_declared(tmp_path):
    """LinkML identifiers are required. This corpus's only identifier also declares it, so the
    rule is pinned on another schema: the page relies on SchemaView's induced slots for it."""
    schema = tmp_path / "synthetic.yaml"
    schema.write_text(yaml.safe_dump({
        "id": "https://example.org/synthetic", "name": "synthetic",
        "prefixes": {"linkml": "https://w3id.org/linkml/"}, "imports": ["linkml:types"],
        "default_range": "string",
        "classes": {"Thing": {"attributes": {"key": {"identifier": True},
                                             "label": {"required": True}, "note": {}}}},
    }), encoding="utf-8")
    reference = render_pages.schema_reference(schema)
    assert reference["source"] == "synthetic.yaml"
    slots = {s["name"]: s for s in reference["classes"][0]["slots"]}
    assert (slots["key"]["required"], slots["label"]["required"], slots["note"]["required"]) == (True, True, False)


def test_committed_schema_page_is_current_and_its_anchors_resolve():
    env = render_pages.template_environment()
    html = env.get_template("schema.html").render(root="", schema=render_pages.schema_reference())
    committed = (PAGES / "schema.html").read_text(encoding="utf-8")
    assert html.split("<footer")[0] == committed.split("<footer")[0]
    page = Page(committed)
    assert {"class-CriticalMineralRecord", "enum-ProcessType", "type-NonEmptyText"} <= page.ids
    internal = [href[1:] for href in page.hrefs() if href.startswith("#")]
    assert internal and set(internal) <= page.ids


PAGE_TYPES = [("index.html", ""), ("browse.html", ""), ("kinds/element.html", "../"),
              ("processes/bioleaching.html", "../"), ("materials/cobalt.html", "../"),
              ("map.html", ""), ("graph.html", ""), ("schema.html", ""),
              ("404.html", "/CMMMech/pages/")]


@pytest.mark.parametrize("page,root", PAGE_TYPES)
def test_schema_link_is_visible_from_every_page_type(page, root):
    html = (PAGES / page).read_text(encoding="utf-8")
    nav = Page(section(html, r'<nav aria-label="Site">.*?</nav>'))
    assert nav.anchor(f"{root}schema.html")[1] == "Schema"
    assert f"{root}schema.html" in Page(html).footer_links


# ----------------------------------------------------------------- license --

LICENSE_LINKS = {f"{GH}/LICENSE-DATA", f"{GH}/LICENSE-CODE", f"{GH}/LICENSE"}


def licence_terms() -> dict[str, str]:
    """The data and code licences as LICENSE names them, in the form the footer prints."""
    scope = " ".join((ROOT / "LICENSE").read_text(encoding="utf-8").split())
    data = re.search(r"Project-authored data,.*? are licensed under .*?\((CC-BY-(\d+\.\d+))\)\. "
                     r"See LICENSE-DATA", scope)
    code = re.search(r"Project-authored code,.*? is licensed under (\S+)\. See LICENSE-CODE", scope)
    assert data and code and "retain their own licenses" in scope
    # The scope file and the legal texts it points to must name the same licences.
    assert (ROOT / "LICENSE-DATA").read_text(encoding="utf-8").startswith(
        f"Attribution {data.group(2)} International")
    assert (ROOT / "LICENSE-CODE").read_text(encoding="utf-8").startswith(
        code.group(1).replace("-", " ", 1) + " License")
    return {"data": data.group(1).replace("-", " "), "code": code.group(1)}


@pytest.mark.parametrize("page,root", PAGE_TYPES)
def test_every_page_type_footer_states_the_repository_licences(page, root):
    terms = licence_terms()
    footer = Page((PAGES / page).read_text(encoding="utf-8"))
    assert LICENSE_LINKS <= set(footer.footer_links)
    assert footer.anchor(f"{GH}/LICENSE-DATA")[1] == terms["data"]
    assert footer.anchor(f"{GH}/LICENSE-CODE")[1] == terms["code"]
    text = footer.footer()
    assert f"Project data: {terms['data']}. Code: {terms['code']}." in text
    assert "Third-party source material keeps its own terms (licence scope)." in text


# ----------------------------------------------- skip link and not-found page --

class FirstTabStop(HTMLParser):
    """The first keyboard-focusable element in <body>, and every <main>."""

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.first: tuple[str, dict] | None = None
        self.mains: list[dict] = []
        self._body = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._body = self._body or tag == "body"
        if tag == "main":
            self.mains.append(attrs)
        focusable = ((tag == "a" and "href" in attrs)
                     or tag in {"button", "input", "select", "textarea", "summary"}
                     or attrs.get("tabindex") not in (None, "-1"))
        if self._body and self.first is None and focusable:
            self.first = (tag, attrs)


@pytest.mark.parametrize("page,root", PAGE_TYPES)
def test_first_tab_stop_skips_to_main(page, root):
    stops = FirstTabStop((PAGES / page).read_text(encoding="utf-8"))
    tag, attrs = stops.first
    assert (tag, attrs.get("href"), attrs.get("class")) == ("a", "#main-content", "skip-link")
    assert [main.get("id") for main in stops.mains] == ["main-content"]


def workflow() -> dict:
    return yaml.safe_load((ROOT / ".github" / "workflows" / "pages.yaml").read_text(encoding="utf-8"))


def deploy_steps() -> list[dict]:
    return workflow()["jobs"]["deploy"]["steps"]


def test_not_found_page_is_copied_to_the_artifact_root_and_every_site_link_is_root_absolute():
    """GitHub Pages serves the artifact root's 404.html for a missing URL at any depth."""
    stage = next(step for step in deploy_steps() if step.get("name") == "Stage site")["run"]
    assert 'cp pages/404.html "$RUNNER_TEMP/site/404.html"' in stage
    html = (PAGES / "404.html").read_text(encoding="utf-8")
    targets = re.findall(r'(?:href|src|action)="([^"]+)"', html)
    site = [t for t in targets if not t.startswith(("https://", "#"))]
    assert len(site) >= 10
    for target in site:
        # A relative link would resolve against whatever missing path was asked for.
        assert target.startswith("/CMMMech/pages/"), target
        assert (PAGES / target[len("/CMMMech/pages/"):].split("#")[0]).is_file(), target
    page = Page(html)
    assert {"/CMMMech/pages/index.html", "/CMMMech/pages/browse.html"} <= set(page.hrefs())
    assert 'action="/CMMMech/pages/browse.html"' in html
    assert "Page not found" in page.plain_text()


# ---------------------------------------------------------- feedback_route --

def test_every_record_page_links_a_prefilled_issue_and_its_yaml_edit_view():
    for path in sorted((PAGES / "materials").glob("*.html")):
        slug = path.stem
        line = Page(section(path.read_text(encoding="utf-8"), r'<p class="history".*?</p>'))
        issues = [h for h in line.hrefs() if h.startswith("https://github.com/CultureBotAI/CMMMech/issues/new?")]
        assert len(issues) == 1, slug
        query = parse_qs(urlsplit(issues[0]).query)
        assert query == {"title": [f"Problem with cmmmech:{slug}"],
                         "body": [f"https://culturebotai.github.io/CMMMech/pages/materials/{slug}.html"]}
        assert line.anchor(f"https://github.com/CultureBotAI/CMMMech/edit/main/data/records/{slug}.yaml")
        assert (ROOT / "data" / "records" / f"{slug}.yaml").is_file()


def test_feedback_query_is_url_encoded():
    routes = render_pages.feedback_routes({"id": "cmmmech:a-b", "page": "materials/a-b.html"},
                                          "data/records/a-b.yaml")
    assert routes["issue"] == ("https://github.com/CultureBotAI/CMMMech/issues/new?title=Problem%20with"
                               "%20cmmmech%3Aa-b&body=https%3A%2F%2Fculturebotai.github.io%2FCMMMech"
                               "%2Fpages%2Fmaterials%2Fa-b.html")
    assert unquote(routes["issue"]).endswith("pages/materials/a-b.html")


# --------------------------------------------------------------- downloads --

def test_export_writes_every_record_completely_and_deterministically(tmp_path, monkeypatch):
    first = export_records.export(tmp_path / "a", commit="abc")
    # A later clock: gzip would stamp it into the header unless the export pins it.
    monkeypatch.setattr(time, "time", lambda: 2_000_000_000.0)
    second = export_records.export(tmp_path / "b", commit="abc")
    data = (tmp_path / "a" / export_records.RECORDS_FILE).read_bytes()
    assert data == (tmp_path / "b" / export_records.RECORDS_FILE).read_bytes()
    assert first == second
    lines = gzip.decompress(data).decode("utf-8").splitlines()
    paths = sorted((ROOT / "data" / "records").glob("*.yaml"))
    assert first["records"] == len(lines) == len(paths)
    assert first["sha256"] == hashlib.sha256(data).hexdigest()
    assert first["uncompressed_sha256"] == hashlib.sha256(gzip.decompress(data)).hexdigest()
    exported = [json.loads(line) for line in lines]
    assert [doc["id"] for doc in exported] == sorted(doc["id"] for doc in exported)
    # Complete: each line is its YAML file, field for field.
    by_id = {doc["id"]: doc for doc in exported}
    for path in paths[::25]:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert by_id[doc["id"]] == json.loads(json.dumps(doc, default=str))
    manifest = json.loads((tmp_path / "a" / export_records.MANIFEST_FILE).read_text(encoding="utf-8"))
    assert manifest == first and manifest["commit"] == "abc"


def test_export_refuses_a_file_that_is_not_a_record(tmp_path):
    (tmp_path / "data" / "records").mkdir(parents=True)
    (tmp_path / "data" / "records" / "x.yaml").write_text("name: no id\n", encoding="utf-8")
    with pytest.raises(ValueError, match="not a record with an id"):
        export_records.export(tmp_path / "out", root=tmp_path)
    assert not (tmp_path / "out").exists()


def test_landing_links_the_deploy_time_export_that_the_workflow_builds():
    """pages/ links two files the Pages workflow writes into the artifact at deploy time."""
    downloads = Page(section((PAGES / "index.html").read_text(encoding="utf-8"),
                             r'<section id="downloads".*?</section>'))
    linked = {href for href in downloads.hrefs() if href.startswith("downloads/")}
    assert linked == {f"downloads/{export_records.RECORDS_FILE}", f"downloads/{export_records.MANIFEST_FILE}"}
    assert "generated from this site's commit each time the site is deployed" in downloads.plain_text()
    steps = deploy_steps()
    names = [step.get("name") for step in steps]
    export = steps[names.index("Export complete records")]["run"]
    assert 'scripts/export_records.py --out "$RUNNER_TEMP/site/pages/downloads"' in export
    # Built into the uploaded artifact, before the upload.
    assert names.index("Stage site") < names.index("Export complete records") < names.index("Upload Pages artifact")
    assert workflow()["permissions"] == {"contents": "read", "pages": "write", "id-token": "write"}
    # Never committed, so nothing stale can be published from the tree.
    assert not (PAGES / "downloads").exists()
