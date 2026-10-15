# Publication helper audit

- UTC timestamp: 2026-10-15T20:31:20.521929+00:00
- Reviewed base: `1c2a3bb043c4bd267a3d911d0e77b029c742689e`; working helpers, not committed artifacts.
- Reviewer: codex /root/round100_pentagonite (GPT-6).

## Scope

Read-only seven-helper/config audit and bounded comparison with round101; no helper execution except isolated receipt-pattern reproduction. Source snapshots and diffs retained outside checkout.

## Evidence checked

- `/private/tmp/cmm-round102-helper-config.json` — SHA256 `ef961e5d6476cf0e9d317dfde9331f5362e5e6a331fefc1566b45eaa19669717`.
- `/private/tmp/cmm-round102-final-gates.py` — SHA256 `5814f4dd5ec9002847e8f01e0aa759992cc88004dd795ceacfcf18999bbbb238`.
- `/private/tmp/cmm-round102-review-check-final.py` — SHA256 `4fab8f5bd2df77c5cf09e5b9cb5157d798e4327ca9b776e3ad77333c578bc56d`.
- `/private/tmp/cmm-round102-review-bases.py` — SHA256 `a3675560fea6b75f942f35d0276f0cd2df1b04d5cf092704c9652c9b19cb65f5`.
- `/private/tmp/cmm-round102-isolated-coverage.py` — SHA256 `eadfdb3a154e892d147a05618fcbc0b7a51922eb1f8d6f590817fc8ae4ca9e8c`.
- `/private/tmp/cmm-round102-isolated-verification.py` — SHA256 `94f1fc379602c715e53acc9d9df1e27525540e12e887719a6a3b2da8393994a2`.
- `/private/tmp/cmm-round102-preservation-before-commit-check.py` — SHA256 `f723e545ffdd0ec62668ea3d404c7b6a1651201bacd9681f52d03adca3a450a6`.

- All six Python sources parse successfully. Config specifies current base, dedicated branch, seven assigned slugs and explicitly provisional501/572/589/103/501 counts.
- Round101 comparisons change only round/path/base bindings and expected record count; coverage exclusive creation retains the prior issue367 fix.
- Coverage requires exact current owner ID/path/hash, completed positive scientific review and available commit bases; it supplements rather than replaces canonical review validation.
- Isolated verification requires main-only clone, explicit tag fetch, topic absence, exact squash parent/tree, strict record/history/native-review commands, coverage and clean clone; postmerge requires local/remote topic deletion.
- Review-check-final and review-bases use exclusive output creation. Preservation checks main HEAD/status and baseline nontracked bytes/modes/symlink identity.

## Findings by severity

- Minor, open: `CMMMech:publication:round102-gate-receipt-exclusivity`. Existence assertion followed by write_text does not reserve the receipt. A dangling symlink passes exists() and write_text creates its target; a creator between check/write is overwritten. Exact pathlib sequence independently reproduced in isolated temporary paths. Reproduction: `/private/tmp/cmm-round102-helper-audit/receipt-reproduction.json`.

## Corrections

Preserve original helpers; replace final receipt publication with exclusive open(x), explicitly refuse symlinks, and test normal creation, existing regular file, existing and dangling symlinks, and racing creator. Do not silently change the active gate process; retain which helper generated its receipt. No helper was edited by the reviewer.

## Unresolved questions and limitations

- Expected counts and exact coverage await all seven scientific bundles and canonical validation.
- No committed topic head, PR, queue guard or preflight is assessed by this audit.
- Live final-gate result is not yet terminal. No finding asserts that an actual receipt was overwritten.
- Current retained-tag remote result and all review-base ancestry require final run reconciliation; source-level review is not remote verification.
- This is not a fresh scientific review or acceptance of reviewer-authored borate owners.

## Verdict

Needs curation of two temporary receipt writers. Other reviewed guard behavior matches the intended previous-round implementation within this bounded scope.
