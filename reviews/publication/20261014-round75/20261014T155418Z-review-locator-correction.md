# Round75 review receipt-locator correction

UTC: 2026-10-14T15:54:18.265013+00:00. Author: Codex GPT-6, /root/round68_phosphates. This is an operational metadata addendum to two immutable scientific reviews, not another scientific review or curation event.

Both original `evidence[evidence_id=batch].locator` fields say **“all three command exits”**. The correct wording is **“all four command exits”**. Every actual command is already correctly enumerated and marked passed in each original `checks` list. The original YAML and generated Markdown remain unchanged.

- `20261014T155141Z-vermiculite-round75-independent`: [original YAML](../../structured/20261014T155141Z-vermiculite-round75-independent/review.yaml), SHA256 `b939eef289ef0a3a939ada649de817ab8249503abf73d3202193e6a83255ad82`; [original Markdown](../../structured/20261014T155141Z-vermiculite-round75-independent/review.md), SHA256 `ce7f6f34a8fcfdadbede52daa8b52fa903aa0dfbce5fd9381c3b752d9bd9370d`.
- `20261014T155141Z-montmorillonite-round75-independent`: [original YAML](../../structured/20261014T155141Z-montmorillonite-round75-independent/review.yaml), SHA256 `4ed2f7867b4cf8a5509be4934540c453412ff0db2b43d87b668251f0acee3634`; [original Markdown](../../structured/20261014T155141Z-montmorillonite-round75-independent/review.md), SHA256 `0fc9650d920df0c59f3c9f9556513f14a144d5c1b8bc743cc7e4f785e4044aed`.

The actual terminal receipt is `/private/tmp/cmm-round75-final-gates.json`, SHA256 `181ca72cfa526f2d6e43b7472b32024d250ce34583cadf1d400e2a2a1e394879`. Its log is `/private/tmp/cmm-round75-final-gates.log`, SHA256 `c6b5357c7bcc3003495533f942055076b5c6e8320007a4af9741592c69d98270`. The batch ran from 2026-10-14T15:46:37.831327+00:00 to 2026-10-14T15:50:14.550718+00:00; all four commands exited zero:

- `just check` — exit 0.
- `uv run --locked cmmmech validate --require-records` — exit 0.
- `uv run --locked cmmmech validate-history --base 4cb10d22d5542370cf5fac27288907ec0d42308c` — exit 0.
- `uv run --locked python scripts/render_pages.py --check` — exit 0.

No record, history, scientific assessment or scientific verdict changed. Both original reviews have `findings: []`; this addendum changes no prior canonical finding disposition. Exact original hashes, four listed checks, actual receipt/log hashes and unchanged owner hashes were checked before saving. The paired JSON retains each original and corrected locator verbatim plus command timestamps.
