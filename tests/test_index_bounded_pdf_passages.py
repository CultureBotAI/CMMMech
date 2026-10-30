"""Unit tests for scripts/index_bounded_pdf_passages.py (cmmmech-infra-0011 / issue #840)."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "index_bounded_pdf_passages", ROOT / "scripts" / "index_bounded_pdf_passages.py"
)
indexer_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(indexer_mod)


def test_chunk_text_by_utf8_bytes_enforces_byte_bound():
    long_lines = [f"Line {idx:03d}: " + ("mineral-assay-column " * 4) for idx in range(40)]
    text = "\n".join(long_lines)
    chunks = indexer_mod.chunk_text_by_utf8_bytes(text, max_bytes=512)
    assert len(chunks) >= 5
    for chunk in chunks:
        assert len(chunk.encode("utf-8")) <= 512

    # Single over-long line is also split cleanly <= max_bytes
    single_line = "X" * 1500
    line_chunks = indexer_mod.chunk_text_by_utf8_bytes(single_line, max_bytes=400)
    assert len(line_chunks) >= 4
    for chunk in line_chunks:
        assert len(chunk.encode("utf-8")) <= 400

    with pytest.raises(ValueError, match="max_bytes must be between"):
        indexer_mod.chunk_text_by_utf8_bytes("test", max_bytes=9000)


def test_index_pdf_passages_writes_bounded_passages_and_manifests(tmp_path):
    pdf_a = tmp_path / "CM20_231.pdf"
    pdf_b = tmp_path / "AM72_1230.pdf"
    pdf_a.write_bytes(b"%PDF-1.4 synthetic fixture A\n")
    pdf_b.write_bytes(b"%PDF-1.4 synthetic fixture B\n")

    pages_by_name = {
        "CM20_231.pdf": [
            "Page 1 introduction\nAnother line on page 1\n",
            "Page 2 Table 1 Chemical composition of Gjerdingenite-(Fe) and Johnsenite-(Ce)\n"
            + "\n".join(f"Row {i}: Nb2O5 {40 + i}.12 wt.% measured by WDS" for i in range(50)),
        ],
        "AM72_1230.pdf": [
            "Page 1 Howardevansite crystal structure refinement\nSpace group P-1\n",
        ],
    }

    def fake_extractor(path: Path) -> list[str]:
        return pages_by_name[path.name]

    out_dir = tmp_path / "bounded-out"
    summary = indexer_mod.index_pdf_passages(
        [pdf_a, pdf_b],
        out_dir,
        candidates=[
            indexer_mod.parse_candidate_spec("Gjerdingenite-(Fe)=Gjerdingenite"),
            indexer_mod.parse_candidate_spec("Howardevansite"),
            indexer_mod.parse_candidate_spec("UnmentionedMineral"),
        ],
        max_passage_bytes=512,
        context_lines=30,
        page_extractor=fake_extractor,
    )

    assert summary["max_passage_bytes"] == 512
    assert summary["total_selected_files"] >= 3
    assert summary["max_selected_file_bytes"] <= 512

    # Check source SHA-256 provenance
    sources_by_id = {s["source_id"]: s for s in summary["sources"]}
    assert sources_by_id["cm20-231"]["pdf_sha256"] == hashlib.sha256(pdf_a.read_bytes()).hexdigest()
    assert sources_by_id["am72-1230"]["pdf_sha256"] == hashlib.sha256(pdf_b.read_bytes()).hexdigest()

    # Check hits and misses
    assert summary["candidates"]["Gjerdingenite-(Fe)"]["hits"]
    assert summary["candidates"]["Gjerdingenite-(Fe)"]["absent_in_sources"] == ["am72-1230"]
    assert summary["candidates"]["Howardevansite"]["hits"]
    assert summary["candidates"]["Howardevansite"]["absent_in_sources"] == ["cm20-231"]
    assert summary["candidates"]["UnmentionedMineral"]["hits"] == []
    assert summary["candidates"]["UnmentionedMineral"]["absent_in_sources"] == [
        "cm20-231",
        "am72-1230",
    ]

    # Verify summary.json and passage-map.tsv on disk
    summary_disk = json.loads((out_dir / "summary.json").read_text(encoding="utf-8"))
    assert summary_disk["total_selected_files"] == summary["total_selected_files"]

    tsv_lines = (out_dir / "passage-map.tsv").read_text(encoding="utf-8").splitlines()
    assert tsv_lines[0] == "source_id\tcandidate\tpage\tbytes\tlines\tfile\tfirst_line"
    assert len(tsv_lines) == 1 + summary["total_selected_files"]

    for hit in (
        summary["candidates"]["Gjerdingenite-(Fe)"]["hits"]
        + summary["candidates"]["Howardevansite"]["hits"]
    ):
        passage_file = out_dir / hit["file"]
        assert passage_file.is_file()
        assert passage_file.stat().st_size == hit["bytes"]
        assert hit["bytes"] <= 512
