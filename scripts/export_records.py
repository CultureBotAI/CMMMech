#!/usr/bin/env python3
"""Write every CMMMech record, complete, as one deterministic JSON Lines export.

Usage:
    python scripts/export_records.py --out DIR [--commit SHA]

Each data/records/*.yaml file becomes one JSON object per line, exactly as the
YAML states it, sorted by id and gzip-compressed with a zero timestamp, so the
same records always produce the same bytes. manifest.json beside it gives the
record count and the SHA-256 of the compressed and the uncompressed bytes.

The Pages workflow runs this at deploy time into the uploaded artifact
(.github/workflows/pages.yaml), so the export always matches the deployed
commit's records. Its output is never committed; pages/index.html links it.
"""

from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import io
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = "data/records"
RECORDS_FILE = "cmmmech-records.jsonl.gz"
MANIFEST_FILE = "manifest.json"
# What LICENSE says, and no more.
LICENCES = {
    "data": "CC-BY-4.0 (LICENSE-DATA); third-party material retains its own terms (LICENSE)",
    "code": "BSD-3-Clause (LICENSE-CODE)",
}


def _json_value(value: Any) -> str:
    """An unquoted YAML date or timestamp, written as the ISO text it was."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    raise TypeError(f"{type(value).__name__} is not JSON serializable")


def load_records(root: Path = REPO_ROOT) -> list[dict[str, Any]]:
    """Every record file, in id order; a file that is not a record with an id is an error."""
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    records = []
    for path in sorted((root / RECORDS_DIR).glob("*.yaml")):
        with path.open(encoding="utf-8") as handle:
            doc = yaml.load(handle, Loader=loader)
        if not isinstance(doc, dict) or not doc.get("id"):
            raise ValueError(f"{path.relative_to(root)}: not a record with an id")
        records.append(doc)
    ids = [doc["id"] for doc in records]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate record ids")
    return sorted(records, key=lambda doc: doc["id"])


def export(out_dir: Path, *, commit: str | None = None, root: Path = REPO_ROOT) -> dict[str, Any]:
    """Write the gzip-compressed JSON Lines file and its manifest; return the manifest."""
    records = load_records(root)
    lines = "".join(
        json.dumps(doc, ensure_ascii=False, separators=(",", ":"), default=_json_value) + "\n"
        for doc in records
    ).encode("utf-8")
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, compresslevel=9, mtime=0) as gz:
        gz.write(lines)
    compressed = buffer.getvalue()
    manifest = {
        "file": RECORDS_FILE,
        "format": "JSON Lines, gzip-compressed: one complete record per line, sorted by id",
        "records": len(records),
        "bytes": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_bytes": len(lines),
        "uncompressed_sha256": hashlib.sha256(lines).hexdigest(),
        "source": f"{RECORDS_DIR}/*.yaml",
        "schema": "src/cmmmech/schema/cmmmech.yaml",
        "licences": LICENCES,
        "commit": commit,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / RECORDS_FILE).write_bytes(compressed)
    (out_dir / MANIFEST_FILE).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, required=True, help="directory to write into")
    parser.add_argument("--commit", help="the commit the export was built from")
    args = parser.parse_args(argv)
    try:
        manifest = export(args.out, commit=args.commit)
    except (OSError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {manifest['records']} records to {args.out / RECORDS_FILE} "
          f"(sha256 {manifest['sha256']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
