#!/usr/bin/env python3
"""Serialize each CMMMech material record to structured text and embed with BAAI/bge-large-en-v1.5.

Run inside the GPU/MPS embeddings env:
    python3 scripts/embed_records.py

Writes:
    data/embeddings/vectors.npy   float32 array of shape (N, 1024), L2-normalized
    data/embeddings/ids.json      ordered list of record IDs matching row axis of vectors.npy
    data/embeddings/meta.json     model name, dim, count, corpus sha256 fingerprint
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = ROOT / "data" / "records"
OUT_DIR = ROOT / "data" / "embeddings"
DEFAULT_MODEL = "BAAI/bge-large-en-v1.5"


def record_to_text(doc: dict) -> str:
    """Flatten a CMMMech material record into a deterministic prose passage."""
    lines: list[str] = []
    name = doc.get("name", "")
    rec_id = doc.get("id", "")
    kind = (doc.get("material_kind") or "").replace("_", " ")
    lines.append(f"{name} ({rec_id}): {kind}.")

    if desc := (doc.get("description") or "").strip():
        lines.append(desc)

    if idents := doc.get("identifiers"):
        ident_strs = [
            f"{i.get('label', '')} ({i.get('id', '')})".strip()
            for i in idents
            if isinstance(i, dict)
        ]
        if ident_strs:
            lines.append("Identifiers: " + "; ".join(ident_strs) + ".")

    if crits := doc.get("criticality"):
        crit_strs = [
            f"{c.get('jurisdiction', '')} {c.get('list_name', '')} ({c.get('classification', '')})".strip()
            for c in crits
            if isinstance(c, dict)
        ]
        if crit_strs:
            lines.append("Criticality: " + "; ".join(crit_strs) + ".")

    for mech in doc.get("mechanisms") or []:
        if not isinstance(mech, dict):
            continue
        m_name = mech.get("name", "")
        m_proc = (mech.get("process") or "").replace("_", " ")
        m_desc = (mech.get("description") or "").strip()
        m_ctx = (mech.get("context") or "").strip()
        orgs = [
            o.get("label") or o.get("id", "")
            for o in (mech.get("organisms") or [])
            if isinstance(o, dict)
        ]
        org_str = f" Organisms: {', '.join(orgs)}." if orgs else ""
        lines.append(f"Mechanism ({m_proc}) — {m_name}: {m_desc} {m_ctx}{org_str}".strip())
        for ev in mech.get("evidence") or []:
            if isinstance(ev, dict) and (expl := (ev.get("explanation") or "").strip()):
                lines.append(f"Evidence ({ev.get('supports', '')}): {expl}")

    return "\n".join(lines)


def load_corpus() -> tuple[list[str], list[str], list[str], str]:
    ids: list[str] = []
    names: list[str] = []
    texts: list[str] = []
    h = hashlib.sha256()
    for path in sorted(RECORDS_DIR.glob("*.yaml")):
        raw = path.read_bytes()
        h.update(raw)
        doc = yaml.safe_load(raw)
        if not isinstance(doc, dict) or not doc.get("name"):
            continue
        rec_id = doc.get("id") or f"cmmmech:{path.stem}"
        ids.append(rec_id)
        names.append(doc.get("name", path.stem))
        texts.append(record_to_text(doc))
    return ids, names, texts, h.hexdigest()[:16]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--device", default=None, help="mps | cuda | cpu (auto if omitted)")
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Serialize only; print stats and sample passage without importing torch.",
    )
    args = ap.parse_args()

    ids, _names, texts, fingerprint = load_corpus()
    lengths = [len(t) for t in texts]
    print(
        f"{len(texts)} documents  chars: min={min(lengths)} "
        f"p50={sorted(lengths)[len(lengths) // 2]} "
        f"p95={sorted(lengths)[int(len(lengths) * 0.95)]} max={max(lengths)}"
    )

    if args.dry_run:
        print("\n--- sample document (index 0) ---")
        print(texts[0])
        return

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = args.device or (
        "mps"
        if torch.backends.mps.is_available()
        else "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )
    print(f"loading {args.model} on {device} ...")
    model = SentenceTransformer(args.model, device=device)

    Order = sorted(range(len(texts)), key=lambda i: len(texts[i]), reverse=True)
    sorted_texts = [texts[i] for i in Order]
    sorted_vecs = model.encode(
        sorted_texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    if device == "mps":
        torch.mps.empty_cache()

    vecs = np.empty_like(sorted_vecs, dtype=np.float32)
    for new_pos, orig_idx in enumerate(Order):
        vecs[orig_idx] = sorted_vecs[new_pos]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.save(OUT_DIR / "vectors.npy", vecs)
    (OUT_DIR / "ids.json").write_text(json.dumps(ids, indent=2) + "\n", encoding="utf-8")
    meta = {
        "model": args.model,
        "dim": int(vecs.shape[1]),
        "count": int(vecs.shape[0]),
        "normalized": True,
        "corpus_fingerprint": fingerprint,
    }
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT_DIR / 'vectors.npy'} {vecs.shape} and meta.json")


if __name__ == "__main__":
    main()
