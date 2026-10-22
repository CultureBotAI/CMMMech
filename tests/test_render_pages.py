"""Tests for CMMMech static site generation."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("render_pages", ROOT / "scripts/render_pages.py")
render_pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render_pages)

PAGES_DIR = render_pages.PAGES_DIR
RECORDS_DIR = render_pages.RECORDS_DIR
REPO_ROOT = render_pages.REPO_ROOT
render_main = render_pages.main


def test_site_pages_exist_and_match_corpus():
    assert PAGES_DIR.exists(), "pages/ directory does not exist; run `just render`"
    assert (PAGES_DIR / ".nojekyll").exists()
    assert (PAGES_DIR / "style.css").exists()
    assert (PAGES_DIR / "theme-toggle.js").exists()
    assert (PAGES_DIR / "record-browser.js").exists()
    assert (PAGES_DIR / "index.html").exists()
    assert (PAGES_DIR / "browse.html").exists()
    assert (PAGES_DIR / "index.json").exists()

    root_index = REPO_ROOT / "index.html"
    assert root_index.exists(), "root redirect index.html does not exist"
    assert 'url=pages/index.html' in root_index.read_text(encoding="utf-8")


def test_render_check_succeeds_without_drift():
    exit_code = render_main(["--check"])
    assert exit_code == 0, "pages/ is out of sync with data/records/; run `just render`"


def test_index_json_covers_all_records():
    index_path = PAGES_DIR / "index.json"
    data = json.loads(index_path.read_text(encoding="utf-8"))
    record_files = list(RECORDS_DIR.glob("*.yaml"))
    assert len(data) == len(record_files)

    slugs = {entry["slug"] for entry in data}
    for rf in record_files:
        assert rf.stem in slugs, f"Missing {rf.stem} in index.json"


@pytest.mark.parametrize("slug", ["cobalt", "neodymium", "lithium", "aluminium", "copper"])
def test_sample_material_pages_content(slug):
    page_path = PAGES_DIR / "materials" / f"{slug}.html"
    assert page_path.exists(), f"Missing detail page for {slug}"
    content = page_path.read_text(encoding="utf-8")

    yaml_path = RECORDS_DIR / f"{slug}.yaml"
    doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

    # Name and kind must be present
    assert doc["name"] in content
    assert doc["material_kind"].replace("_", " ") in content

    # All identifiers must be present
    for id_entry in doc.get("identifiers") or []:
        assert id_entry["id"] in content

    # All mechanisms must be present
    for m in doc.get("mechanisms") or []:
        assert m["name"] in content
        for org in m.get("organisms") or []:
            assert org["label"] in content


def test_kind_and_process_pages_generated():
    kinds_dir = PAGES_DIR / "kinds"
    assert (kinds_dir / "element.html").exists()
    assert (kinds_dir / "mineral.html").exists()
    assert (kinds_dir / "secondary_resource.html").exists()

    proc_dir = PAGES_DIR / "processes"
    assert (proc_dir / "bioleaching.html").exists()
    assert (proc_dir / "biomineralization.html").exists()


def test_protein_examples_and_causal_graphs_rendered():
    assert (
        render_pages.curie_url("NCBIfam:TIGR01234")
        == "https://www.ebi.ac.uk/interpro/entry/ncbifam/TIGR01234"
    )
    assert (
        render_pages.curie_url("UniProtKB:Q747K6")
        == "https://www.uniprot.org/uniprotkb/Q747K6"
    )

    akaganeite_html = (PAGES_DIR / "materials" / "akaganeite.html").read_text(encoding="utf-8")
    assert "UniProtKB:Q747K6" in akaganeite_html
    assert "https://www.uniprot.org/uniprotkb/Q747K6" in akaganeite_html
    assert "SWISS_PROT" in akaganeite_html
    assert "Causal Graphs &amp; Molecular Pathways" in akaganeite_html
    assert "causal-node-pca_imch_cbcl_akaganeite_pathway-imch_cytochrome" in akaganeite_html

    manganese_html = (PAGES_DIR / "materials" / "manganese.html").read_text(encoding="utf-8")
    assert "UNGROUNDED" in manganese_html
    assert "UPI000164C1D1" in manganese_html
    assert "UniProtKB:B0KQT1" in manganese_html
    assert "UniProtKB:B0KSN7" in manganese_html

    browse_html = (PAGES_DIR / "browse.html").read_text(encoding="utf-8")
    assert "uniprotkb:q747k6" in browse_html
    assert "imch_geosl" in browse_html


def test_unified_facets_search_and_map():
    index_html = (PAGES_DIR / "index.html").read_text(encoding="utf-8")
    assert 'class="hero-search"' in index_html
    assert 'href="map.html"' in index_html

    browse_html = (PAGES_DIR / "browse.html").read_text(encoding="utf-8")
    assert 'class="browse-layout"' in browse_html
    assert '<aside class="facet-sidebar"' in browse_html

    map_html = (PAGES_DIR / "map.html").read_text(encoding="utf-8")
    assert 'class="browse-layout"' in map_html
    assert '<aside class="facet-sidebar"' in map_html
    assert 'id="corpus-map"' in map_html
    assert "BAAI/bge-large-en-v1.5" in map_html

    cobalt_html = (PAGES_DIR / "materials" / "cobalt.html").read_text(encoding="utf-8")
    assert 'class="page-search"' in cobalt_html


def test_ima_symbol_and_polymorph_or_grade_rendered(tmp_path):
    doc = {
        "id": "cmmmech:silicon-carbide",
        "name": "Silicon carbide",
        "material_kind": "commodity",
        "ima_symbol": "Moi",
        "polymorph_or_grade": "3C-SiC",
        "description": "Cubic beta-silicon carbide polytype.",
        "sources": [
            {
                "id": "src_test",
                "title": "Test source",
                "url": "https://example.org/sic",
                "accessed_on": "2026-10-21",
            }
        ],
    }
    rec_path = tmp_path / "silicon-carbide.yaml"
    rec_path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    prepared = render_pages.prepare_record_data(rec_path, doc)
    assert prepared["ima_symbol"] == "Moi"
    assert prepared["polymorph_or_grade"] == "3C-SiC"
    assert "moi" in prepared["search_text"]
    assert "3c-sic" in prepared["search_text"]

    env = render_pages.Environment(
        loader=render_pages.FileSystemLoader(str(render_pages.TEMPLATES_DIR)),
        autoescape=render_pages.select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = render_pages.curie_url
    env.globals["build_provenance"] = {
        "total_materials": 1,
        "total_mechanisms": 0,
        "latest_curation": "2026-10-21",
        "corpus_digest": "000000000000",
    }
    html = env.get_template("material.html").render(
        root="../",
        r=prepared,
        source_path="data/records/silicon-carbide.yaml",
    )
    assert "IMA: Moi" in html
    assert "Grade / Polymorph: 3C-SiC" in html


