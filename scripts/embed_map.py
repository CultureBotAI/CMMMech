#!/usr/bin/env python3
"""Project data/embeddings/vectors.npy to 2D with PaCMAP and write a compact JSON bundle for pages/map.html.

Run inside the embeddings env after scripts/embed_records.py:
    python3 scripts/embed_map.py

Writes:
    data/embeddings/corpus_map.json
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pacmap
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = ROOT / "data" / "records"
EMB_DIR = ROOT / "data" / "embeddings"


def main() -> None:
    vecs = np.load(EMB_DIR / "vectors.npy")
    ids: list[str] = json.loads((EMB_DIR / "ids.json").read_text(encoding="utf-8"))
    meta: dict = json.loads((EMB_DIR / "meta.json").read_text(encoding="utf-8"))
    assert vecs.shape[0] == len(ids), "vectors.npy and ids.json row count mismatch"

    by_id: dict[str, tuple[str, str, list[str]]] = {}
    for path in sorted(RECORDS_DIR.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or not doc.get("name"):
            continue
        rec_id = doc.get("id") or f"cmmmech:{path.stem}"
        kind = doc.get("material_kind") or "other"
        procs = sorted({
            m.get("process")
            for m in (doc.get("mechanisms") or [])
            if isinstance(m, dict) and m.get("process")
        })
        by_id[rec_id] = (doc.get("name", path.stem), kind, procs)

    classes = sorted({by_id[i][1] for i in ids})
    class_to_idx = {c: idx for idx, c in enumerate(classes)}

    n_neighbors = min(10, max(2, len(ids) - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=42,
    )
    xy = reducer.fit_transform(vecs)

    mins = xy.min(axis=0)
    span = np.where((xy.max(axis=0) - mins) == 0, 1.0, xy.max(axis=0) - mins)
    xy = (xy - mins) / span

    points = []
    for (x, y), rec_id in zip(xy, ids, strict=True):
        name, cls, procs = by_id[rec_id]
        points.append([
            round(float(x), 4),
            round(float(y), 4),
            class_to_idx[cls],
            rec_id,
            name,
            procs,
        ])

    bundle = {
        "model": meta["model"],
        "method": "pacmap",
        "n": len(points),
        "corpus_fingerprint": meta["corpus_fingerprint"],
        "classes": classes,
        "points": points,
    }
    out = EMB_DIR / "corpus_map.json"
    out.write_text(json.dumps(bundle, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(points)} points)")


if __name__ == "__main__":
    main()
