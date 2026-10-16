# Round112 hosted observer: initial independent finding

UTC: 2026-10-16T05:26:09.980372+00:00

Reviewed helper: `/private/tmp/cmm-round112-observe-hosted-final.py`; SHA256 `07fa00ebf2bd5819a760663fb664df59074868ac924dca51e1859dd643331720`. Exact pre-fix bytes are retained at `/private/tmp/cmm-round112-observe-hosted-final-before-fix.py`. Worktree base: `e3a638e04d9e64cbda7c26d277bdf4f5e7d1e3ae`.

## Scope and evidence

Read-only static/AST inspection of the prepared observer and adjacent final collector/job-log acquisition helpers. No helper was executed and no GitHub state was changed.

## Finding by severity

**Minor — `round112-hosted-observer-stale-identity`**: the observer hardcodes the preceding topic `5fd9beb…`, tree `7b8cc879…`, PR 467 and merge/queue `e3a638e…` (the current round's base). These values form its workflow queries and output identity, so prior successful workflows could be mislabeled as round112 readiness. This confirms the coordinator's reported defect.

The separate final collector already reads current commit/push receipts and explicit merge/queue SHAs. Job-log acquisition reads that exact collection's run/job/attempt bindings. Neither contains the same stale topic/tree literals. Existing eight-helper static acceptance is unaffected.

## Corrections and unresolved questions

Pending: bind successful current commit/push receipts and the actual merged PR/queue observation; reject missing, inconsistent or unmerged identities before observing workflow success. Preserve this initial evidence and test the corrected guard without live mutation. Actual round112 head, PR, merge and hosted outcomes remain future evidence.

## Verdict

**Needs curation** for the prepared observer. No invalid actual acceptance or publication mutation has occurred.
