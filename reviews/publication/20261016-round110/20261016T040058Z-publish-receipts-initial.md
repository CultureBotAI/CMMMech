# Initial commit/push helper review

UTC: 2026-10-16T04:00:58.874816Z. Reviewer: codex /root/round104_ree (GPT-6). Base `0482e7b0af9b18685dabe310dbe86487b6ac4226`.

Reviewed helper `/private/tmp/cmm-round110-publish.py`, SHA256 `4ceb6536df584031e3509b3de5811b32372ebc0d2b8cce1b5810c34e31ab4498`; exact bytes preserved at `/private/tmp/cmm-round110-publish-initial-reviewed.py`. Predecessor isolated-helper/report audit `reviews/publication/20261016-round110/20261016T035955Z-isolated-helpers-report-audit.json` remains unchanged. This addendum covers the newly supplied publication helper.

## Major finding

Stable key: `round110-publish-required-receipts`. Before staging/commit, final-batch consumption does not require the exact worktree and successful four-command sequence. Canonical-review consumption requires only exit/base/log hash, without completion/worktree/required command checks. A valid log hash does not prove those omitted bindings. A same-base receipt from another checkout or one with omitted/replaced required checks can pass these conditions.

Current actual final-batch evidence is correct; the defect concerns fail-closed admission. Require terminal completion, exact worktree/base, successful unique required command rows and coverage root/counts. Exercise negative fixtures before mutation, preserve this initial artifact and save an independent successor.

No Git/GitHub mutation or clone was run. Current report hashes after the parent’s reported spacing-only changes are retained in the paired JSON; scientific/dossier bytes are unchanged.

Verdict: **needs_curation** for publication receipt guards.
