# Homepage mechanism labels: initial independent finding

UTC: 2026-10-15T18:50:56.573446Z. Reviewer: codex `/root/round100_pentagonite` (GPT-6). Base: `b6831c1da19b475ea048baea4ba5c10b96d678af`.

Scope: preparatory presentation/provenance audit. The final publication package is not frozen; this is not independent scientific acceptance of the reviewer-authored pentagonite owner.

## Finding

**Revise — one minor finding: `CMMMech:round100:homepage-mechanism-labels`.** `scripts/render_pages.py:214–215` counts every mechanism and every material with one. The maintained homepage labels these totals “Biological Mechanisms” and “Materials with Bio-Mechanisms”, then labels the full process list “Microbial Transformation Processes” and says every mechanism has microbial agents.

The generated totals rise 490 → 496 mechanisms and 401 → 405 mechanism-bearing materials. Of the six added mechanisms, goldmanite has two abiotic syntheses, haradaite one abiotic synthesis, pentagonite two abiotic thermal/pressure processes, and seawater one biological mechanism. Calling all six biological overstates the curated evidence. This inherited template defect is directly demonstrated by the new batch.

## Exact reviewed inputs

- `src/cmmmech/templates/index.html` — SHA256 `fe4ebe26311dbcb6cb45775e07da7b90f46188d0bc1317c0ee50553355d6a2fb`
- `scripts/render_pages.py` — SHA256 `f1aaa6c382b057a4e4f2702a24e2bebb974403703e4e3b055fffdda024797357`
- `pages/index.html` — SHA256 `0d13f75ec8ab6582544e27900757b2419caea197c85f99be2571f472adca5a90`
- `data/records/goldmanite.yaml` — SHA256 `02ed7a5f86826088ea63dda56b5d401532164a211ddbf932d0135b414751d59f`
- `data/records/haradaite.yaml` — SHA256 `3254359adeb4d0e78c35d8afdb83819e54507341369451e71ee93df2108f0c06`
- `data/records/pentagonite.yaml` — SHA256 `b9df9885b6850d0e03cf5d30220e806e060b618fe07166804574a375598235ed`
- `data/records/seawater.yaml` — SHA256 `3eca7555a6f0a9f377001f5968a9924b73d014179255a4c1d4a6bcf412850ec5`

## Correction and acceptance

Use neutral mechanism/material/process labels and prose in `src/cmmmech/templates/index.html`; keep counting logic and all scientific owners unchanged. Regenerate pages, verify labels/counts and frozen owner hashes, run affected renderer checks and appropriate existing tests, then save a linked successor.

## Search coverage and limitations

253 all-state issues searched for exact biological labels and related page/count phrases; only unrelated closed stevensite locator #263 matched incidentally. Hidden/ignored/followed bounded template/docs/review/report searches included source files.

- Final package/report review is pending.
- No scientific owner or existing scientific review is changed or invalidated by this presentation finding.
- No preflight, merge or remote-main verification is claimed.
