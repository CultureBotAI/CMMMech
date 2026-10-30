#!/usr/bin/env python3
"""Index PDFs into bounded per-page text passages (<= 2-8 KB) for CMMMech curation and review.

Prevents context-window overflow from reading full multi-page PDFs or master-list catalogues
directly into chat context (cmmmech-infra-0011 / issue #840).

Produces in --out-dir:
  - summary.json: per-source SHA-256 provenance, page counts, candidate hits/misses, and byte totals
  - passage-map.tsv: tab-separated manifest of bounded passage files
  - passages/<source_id>.p<page>.<candidate>.w<window>.part<n>.txt: UTF-8 excerpt files <= max_bytes
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Callable

DEFAULT_MAX_PASSAGE_BYTES = 2048
HARD_MAX_PASSAGE_BYTES = 8192

PageExtractor = Callable[[Path], list[str]]


def sha256_file(path: Path) -> str:
    """Return hex SHA-256 digest of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify_token(value: str) -> str:
    """Normalize a source or candidate label into a filename-safe slug."""
    token = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return token or "item"


def extract_pdf_pages_mutool(pdf_path: Path) -> list[str]:
    """Extract per-page UTF-8 text from a PDF using mutool or pdftotext."""
    mutool = shutil.which("mutool")
    if mutool:
        info = subprocess.run(
            [mutool, "info", "-M", str(pdf_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        match = re.search(r"^Pages:\s*(\d+)", info.stdout, flags=re.MULTILINE)
        if match:
            page_count = int(match.group(1))
            pages: list[str] = []
            for page_num in range(1, page_count + 1):
                proc = subprocess.run(
                    [mutool, "draw", "-q", "-F", "txt", str(pdf_path), str(page_num)],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                pages.append(proc.stdout)
            return pages
        proc = subprocess.run(
            [mutool, "draw", "-q", "-F", "txt", str(pdf_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        return [page for page in proc.stdout.split("\f") if page.strip()]

    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        proc = subprocess.run(
            [pdftotext, str(pdf_path), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
        raw_pages = proc.stdout.split("\f")
        if raw_pages and not raw_pages[-1].strip():
            raw_pages.pop()
        return raw_pages

    raise RuntimeError(
        f"Neither 'mutool' nor 'pdftotext' is available on PATH to extract pages from {pdf_path}"
    )


def chunk_text_by_utf8_bytes(text: str, max_bytes: int = DEFAULT_MAX_PASSAGE_BYTES) -> list[str]:
    """Split text into non-empty chunks each <= max_bytes in UTF-8 encoding."""
    if max_bytes <= 0 or max_bytes > HARD_MAX_PASSAGE_BYTES:
        raise ValueError(
            f"max_bytes must be between 1 and {HARD_MAX_PASSAGE_BYTES} (got {max_bytes})"
        )
    cleaned = text.strip()
    if not cleaned:
        return []
    if len(cleaned.encode("utf-8")) <= max_bytes:
        return [cleaned + "\n" if len((cleaned + "\n").encode("utf-8")) <= max_bytes else cleaned]

    chunks: list[str] = []
    current_lines: list[str] = []
    current_bytes = 0

    def _flush() -> None:
        nonlocal current_lines, current_bytes
        if current_lines:
            chunk = "\n".join(current_lines).strip()
            if chunk:
                with_nl = chunk + "\n"
                chunks.append(
                    with_nl if len(with_nl.encode("utf-8")) <= max_bytes else chunk
                )
            current_lines = []
            current_bytes = 0

    for line in cleaned.splitlines():
        line_bytes = len((line + "\n").encode("utf-8"))
        if line_bytes > max_bytes:
            _flush()
            buf = ""
            for ch in line:
                candidate = buf + ch
                if len(candidate.encode("utf-8")) > max_bytes - 1:
                    if buf.strip():
                        chunks.append(buf.strip() + "\n")
                    buf = ch
                else:
                    buf = candidate
            if buf.strip():
                with_nl = buf.strip() + "\n"
                chunks.append(
                    with_nl if len(with_nl.encode("utf-8")) <= max_bytes else buf.strip()
                )
            continue

        if current_bytes + line_bytes > max_bytes and current_lines:
            _flush()
        current_lines.append(line)
        current_bytes += line_bytes

    _flush()
    return chunks


def parse_candidate_spec(spec: str) -> tuple[str, list[str]]:
    """Parse '<candidate_name>[=<term1>,<term2>,...]' into (candidate_name, search_terms)."""
    if "=" in spec:
        name, raw_terms = spec.split("=", 1)
        name = name.strip()
        terms = [t.strip() for t in raw_terms.split(",") if t.strip()]
    else:
        name = spec.strip()
        terms = [name] if name else []
    if not name or not terms:
        raise ValueError(f"Invalid candidate specification: {spec!r}")
    return name, terms


def index_pdf_passages(
    pdf_paths: list[Path],
    out_dir: Path,
    *,
    candidates: list[tuple[str, list[str]]] | None = None,
    max_passage_bytes: int = DEFAULT_MAX_PASSAGE_BYTES,
    context_lines: int = 8,
    page_extractor: PageExtractor | None = None,
) -> dict:
    """Index PDFs into bounded per-page passage files and write summary.json + passage-map.tsv."""
    if max_passage_bytes <= 0 or max_passage_bytes > HARD_MAX_PASSAGE_BYTES:
        raise ValueError(
            f"max_passage_bytes must be in 1..{HARD_MAX_PASSAGE_BYTES} (got {max_passage_bytes})"
        )
    extractor = page_extractor or extract_pdf_pages_mutool
    out_dir = out_dir.resolve()
    passages_dir = out_dir / "passages"
    passages_dir.mkdir(parents=True, exist_ok=True)

    candidate_specs = candidates or [("all-pages", [])]
    sources_meta: list[dict] = []
    candidate_hits: dict[str, list[dict]] = {name: [] for name, _ in candidate_specs}
    candidate_misses: dict[str, list[str]] = {name: [] for name, _ in candidate_specs}
    tsv_rows: list[dict] = []

    total_files = 0
    total_bytes = 0
    max_file_bytes = 0

    for pdf_path in pdf_paths:
        pdf_path = pdf_path.resolve()
        source_id = slugify_token(pdf_path.stem)
        pages = extractor(pdf_path)
        sources_meta.append(
            {
                "source_id": source_id,
                "source_pdf": str(pdf_path),
                "pdf_bytes": pdf_path.stat().st_size,
                "pdf_sha256": sha256_file(pdf_path),
                "pages": len(pages),
                "raw_text_bytes": sum(len(p.encode("utf-8")) for p in pages),
            }
        )

        for cand_name, terms in candidate_specs:
            cand_slug = slugify_token(cand_name)
            matched_In_source = False
            compiled_terms = [re.compile(re.escape(term), re.IGNORECASE) for term in terms]

            for page_idx, page_text in enumerate(pages, start=1):
                lines = page_text.splitlines()
                if not lines:
                    continue

                if not compiled_terms:
                    windows = [(0, len(lines))]
                else:
                    hit_indices = [
                        idx
                        for idx, line in enumerate(lines)
                        if any(pattern.search(line) for pattern in compiled_terms)
                    ]
                    if not hit_indices:
                        continue
                    windows = []
                    for hit_idx in hit_indices:
                        start = max(0, hit_idx - context_lines)
                        end = min(len(lines), hit_idx + context_lines + 1)
                        if windows and start <= windows[-1][1]:
                            windows[-1] = (windows[-1][0], max(windows[-1][1], end))
                        else:
                            windows.append((start, end))

                matched_In_source = True
                for win_idx, (w_start, w_end) in enumerate(windows, start=1):
                    window_text = "\n".join(lines[w_start:w_end])
                    chunks = chunk_text_by_utf8_bytes(window_text, max_bytes=max_passage_bytes)
                    for part_idx, chunk in enumerate(chunks, start=1):
                        fname = (
                            f"{source_id}.p{page_idx}.{cand_slug}.w{win_idx}.part{part_idx}.txt"
                        )
                        rel_file = f"passages/{fname}"
                        file_path = out_dir / rel_file
                        encoded = chunk.encode("utf-8")
                        byte_len = len(encoded)
                        file_path.write_bytes(encoded)

                        chunk_lines = chunk.splitlines()
                        first_line = chunk_lines[0].strip() if chunk_lines else ""
                        hit_entry = {
                            "source_id": source_id,
                            "page": page_idx,
                            "window": win_idx,
                            "part": part_idx,
                            "file": rel_file,
                            "bytes": byte_len,
                            "lines": len(chunk_lines),
                            "first_line": first_line[:160],
                        }
                        candidate_hits[cand_name].append(hit_entry)
                        tsv_rows.append(
                            {
                                "source_id": source_id,
                                "candidate": cand_name,
                                "page": page_idx,
                                "bytes": byte_len,
                                "lines": len(chunk_lines),
                                "file": rel_file,
                                "first_line": first_line[:160],
                            }
                        )
                        total_files += 1
                        total_bytes += byte_len
                        if byte_len > max_file_bytes:
                            max_file_bytes = byte_len

            if not matched_In_source:
                candidate_misses[cand_name].append(source_id)

    summary = {
        "created_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "purpose": (
            "Bounded source-text handoff for CMMMech discovery, curation, and scientific review; "
            "prevents context-window overflow from reading full PDFs or master catalogues directly."
        ),
        "max_passage_bytes": max_passage_bytes,
        "total_selected_files": total_files,
        "total_selected_bytes": total_bytes,
        "max_selected_file_bytes": max_file_bytes,
        "sources": sources_meta,
        "candidates": {
            cand_name: {
                "hits": candidate_hits[cand_name],
                "absent_in_sources": candidate_misses[cand_name],
            }
            for cand_name, _ in candidate_specs
        },
    }

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    tsv_path = out_dir / "passage-map.tsv"
    fieldnames = ["source_id", "candidate", "page", "bytes", "lines", "file", "first_line"]
    with tsv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in tsv_rows:
            writer.writerow(row)

    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdfs",
        nargs="+",
        type=Path,
        help="Input PDF file(s) to index into bounded per-page passages.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="Output directory for summary.json, passage-map.tsv, and passages/*.txt.",
    )
    parser.add_argument(
        "--candidate",
        action="append",
        default=[],
        help=(
            "Candidate query specification '<name>[=<term1>,<term2>,...]'. "
            "May be passed multiple times; if omitted, indexes all pages."
        ),
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_PASSAGE_BYTES,
        help=f"Maximum UTF-8 bytes per passage file (default: {DEFAULT_MAX_PASSAGE_BYTES}, max: {HARD_MAX_PASSAGE_BYTES}).",
    )
    parser.add_argument(
        "--context-lines",
        type=int,
        default=8,
        help="Lines of surrounding page context to include around each matched line (default: 8).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    candidates = [parse_candidate_spec(item) for item in args.candidate] if args.candidate else None
    summary = index_pdf_passages(
        args.pdfs,
        args.out_dir,
        candidates=candidates,
        max_passage_bytes=args.max_bytes,
        context_lines=args.context_lines,
    )
    print(
        f"Indexed {len(summary['sources'])} PDF(s) into {summary['total_selected_files']} bounded passage(s) "
        f"({summary['total_selected_bytes']} bytes total, max {summary['max_selected_file_bytes']} bytes/file) "
        f"at {args.out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
