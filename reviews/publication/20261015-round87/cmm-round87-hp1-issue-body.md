The independently reviewed round87 hosted package selector and manifest builder used `dismissed` as a terminal native finding status. The current review contract uses `rejected`. A valid rejected finding would therefore fail these publication selectors, although the current cohort has not demonstrated a hosted runtime failure and no record science is implicated.

Preserved finding: `HP1`, stable key `round87-hosted-native-finding-status`.

- Initial observation: `reviews/publication/20261015-round87/cmm-round87-hosted-static-initial-20261015T034920Z.json`, with immutable module snapshot SHA256 `2b604b672732057f211aa8cf183785532838578c4964f11b1c4bf4388a624867`.
- Expanded observation: `reviews/publication/20261015-round87/cmm-round87-hosted-static-expanded-20261015T035023Z.json`, which captures both exact occurrences and corrects the initial line-number transcription without overwriting it. Module expression is line50; builder expression is line25.
- Original builder snapshot SHA256 `b2564ee3e322b0f92e0331594e24a615e240202df01f0a23b30fadcd7b794251`.

Acceptance criteria:

1. Use `resolved` and `rejected` in both selectors while retaining exact predecessor occurrence, target, stable-key and hash checks.
2. Keep `open`, `deferred`, schema-invalid `dismissed` and unassessed `accepted_risk` outside positive publication acceptance.
3. Exercise the actual parsed helper predicates/functions with meaningful positive rejected/resolved cases and negative invalid/unresolved cases; retain original and corrected receipts.
4. Save an independent successor that explicitly binds both original observations, both corrected helper hashes and the focused fixture results. Do not rewrite immutable scientific reviews or imply that static checks establish actual PR/CI success.

Both corrections are already prepared after the independent initial captures; the issue records the review defect and its evidence-backed resolution through the authorized PR.

The initial observations, exact source snapshots, correction receipts, focused fixture sources/results and independent successor will be included under `reviews/publication/20261015-round87/` in the resolving PR. Local acquisition paths remain only as provenance inside those artifacts.
