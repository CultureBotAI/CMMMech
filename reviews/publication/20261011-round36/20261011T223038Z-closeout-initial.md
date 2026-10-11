# Round 36 closeout-helper initial finding

UTC: 2026-10-11T22:30:38.068045+00:00

Reviewer: Codex `/root/round27_eaf_slag` (GPT-6; codex). Trusted base `1ef6fdde620a4053fbfff99c51065082dce32d39`. I authored uramphite; root independently reviews its science. This is a separate operational-helper assessment.

Verdict: **needs curation** for this future closeout helper. No helper was executed and no false published comment or scientific-record defect is alleged.

## F1 — minor: final comment does not check all facts it prints

Stable key: `CMMMech.round36.closeout-receipt-binding`.

Reviewed `/private/tmp/cmm-round36-closeout.py`, SHA-256 `94bebb5f64937c6c3696f2cafa6124087c6c58129313853a684c75d21b9339f8`. An exact original snapshot is retained at `/private/tmp/cmm-round36-publication-audit/20261011T223038Z-closeout-initial.py`. The receipt assertions before `def run` check success, merge/tree and some deletion flags. The generated body then hard-codes “308 passed, 3 skipped” without reading the actual postmerge test log. It also asserts clean main/detached worktree and unchanged skill/inventory state without requiring all corresponding receipt flags or exact 7,187/8 preservation counts. Postmerge/hosted topic identity and hosted base are not explicitly matched to the commit receipt at this final-message boundary.

The underlying verification and sync helpers produce these facts; this finding concerns their incomplete verification immediately before an external POST. Bind every receipt to the exact reviewed head/tree/base/merge, verify the actual just-check command and its log section, and assert each printed cleanup/preservation flag and count before publishing. Preserve this initial observation; a corrected-helper assessment should resolve this exact issue key.

Acceptance: independent read-only inspection of the corrected helper, followed later by use of actual successful postmerge, cleanup, preservation and hosted receipts. This outside-Git wrapper correction does not alter records or require repetition of unchanged corpus tests.

Coordinator has been notified. Correction and issue linkage are pending. [Machine-readable finding](20261011T223038Z-closeout-initial.json).
