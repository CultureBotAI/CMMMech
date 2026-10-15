# Round97 static runtime-helper review

- Reviewer: codex /root/round97_phosphates (GPT-6); independent of helper author.
- UTC: 2026-10-15T15:22:14Z to 2026-10-15T15:24:25.220775Z
- Reviewed revision: `9272005a590c9fa1e5fbb75b30f914ce38c3924a`; current external prepared helper bytes and working changes.
- Scope: twelve listed helpers and lineage; static reading, AST parsing and harmless receipt-path test only.
- Verdict: **Needs revision before runtime publication.** Two major and one minor findings; no remote mutation performed.

## Findings

### OP97-01 — minor: Hosted receipt repeats previous-cohort authorship and round label

The future round97 receipt says root authored bassanite and reviewed wood ash, which belong to the preceding cohort. Its Markdown heading remains Round96. A copied helper should not emit false authorship for the present six-record cohort.

Locations: `/private/tmp/cmm-round97-hosted-five.py:166`, `/private/tmp/cmm-round97-hosted-five.py:377`

Acceptance: Replace authorship with accurate round97 operational scope and fix the heading; retain actual role limits and hash the corrected helper.

### OP97-02 — major: Mutating helpers do not reject occupied dangling receipt paths before acting

These four helpers guard output only with not Path.exists(), then perform push/PR creation, queue admission, branch deletion or main fast-forward and write receipts with write_text. A dangling symlink is an occupied path for which exists() is false, so the promised early no-overwrite/refuse-existing-path behavior is bypassed; write_text follows it. A bounded synthetic test reproduced those Path semantics without running any helper or external mutation. Existing regular receipts are rejected; no exploit or actual corruption is claimed.

Locations: `/private/tmp/cmm-round97-publish.py:3,7-10`, `/private/tmp/cmm-round97-enqueue.py:4,25-27`, `/private/tmp/cmm-round97-cleanup.py:4,14-23`, `/private/tmp/cmm-round97-sync-main.py:4,26-28`

Acceptance: Before any mutation reject exists() OR is_symlink(); use exclusive receipt creation so a collision introduced later cannot overwrite a receipt. Apply consistently to maintained receipt writers and add a targeted harmless guard regression check.

### OP97-03 — major: Publish does not bind current external PR metadata to prepared/committed bytes

Commit records a helper-config hash in its bindings, but publish loads the current config title without comparing that hash and first reads PR body only after pushing. Its post-create comparison confirms agreement with the current body, not the prepared/reviewed body. Thus changing config title or body after preparation can publish changed metadata with an unchanged reviewed Git HEAD. This is a static stale-input gap, not a claim that the current draft metadata has changed.

Locations: `/private/tmp/cmm-round97-publish.py:3,7-10`, `/private/tmp/cmm-round97-commit.py:46-50,76`

Acceptance: Bind the reviewed body and config hashes in an immutable preparation/commit or dedicated publication handoff, validate those bindings and exact branch/base/head/tree before the first remote mutation, and use the bound bytes for creation. Recheck body/config bindings before queue admission.

## Positive checks

- All twelve files parse as Python. All ten lineage source and target hashes match, and the claimed lower-case round/base substitutions reproduce each target exactly. That verifies lineage, not semantic fitness of carried-forward prose.
- Commit checks actual record/history/review hashes, base/head, untracked-path allowlist, explicit staged paths and current main; no existing owner/history/review replacement is admitted.
- Enqueue requires preflight base/head/tree, mandatory successful commands, exact PR file set/current required check and an immediately preceding live-main observation. Native queue and postmerge checks remain necessary because this is not atomic locking.
- Cleanup verifies exact merged tree and sole parent, then removes only the owned remote ref using a lease and the owned local branch; retains a clean detached worktree.
- Main sync checks original hidden/ignored files, modes and symlinks, preserved review tag and durable backup, incoming/nontracked path conflicts, then uses ff-only without autostash.
- Fresh-clone pre/post verification rejects occupied paths including symlinks and checks retained tags, absent topic object, exact tree/parent, native record/history/review gates and coverage.
- Hosted audit uses GET operations and current attempt-specific job lists, checks all five roles, exact identities/blobs, closing observations and immutable hash checks.
- Configured null pending counts are a deliberate incomplete handoff; no runtime approval or successful execution is inferred.

## Corrections and unresolved work

No helper edits made by this reviewer. Owner corrections, targeted guard checks and a successor review remain required. Config counts and all live publication receipts are pending.

## Exact input hashes

| Helper | SHA256 |
| --- | --- |
| commit | `7180b1d8d90c1a196fe7294cd0d0a939cd2135b09330264be1fe3087d97382c3` |
| publish | `699e5f44c2e4620bbcc3ac027fe1adad826ac03fd634aaeaaa1273f4991bf4e4` |
| enqueue | `68ce274f0ce33cfbd2a2e640beefd8e73b212bc71610d4118068a89479fef939` |
| cleanup | `7f9a8a5e30e2c870ff3e4e1dfb1342f84b40dc90ebd60cbbbd2fd184a2642f4a` |
| sync-main | `9c0a520ddec77f79ba79861fc1be4a131f460216af466bf50e1cd8c729996ddb` |
| isolated-coverage | `2976fa37edb6f1fd50dd5aaf600133a07149388fe098fef68c03354b51afd844` |
| isolated-verification | `7957840d8bc2300b88e2aec2d9930c1625396f17ec3585f2df56d9c46c95274a` |
| hosted-five | `d014573c717a084d2be7fdd5b10cca9aa25193b2d538a12f28729f471e4dc723` |
| preservation-check | `5ba7e641845710767b9d35c9a4460ef2639fd42d24946c8d2befac9edc1b0038` |
| review-check-final | `f19787384f01c3c8b4dfe911584f04be12faa4321fc80a2eeac6eda1d5a6ca4a` |
| final-gates | `d1c4db7a2728a74d789445eecbfa7fcc765a9ff4686add9b124830d955503754` |
| archive | `6fc1d557f8a4674717592e673ef3552fc069c76ee36cc547724ef0c915cdf625` |
| helper-lineage.json | `da4d0b265053063562cfa9ad6754d154c9f2f1a2cca785390ed9ec721ef39362` |

## Limits

- No PR, merge, hosted run, issue state or runtime receipt was accepted by this static review. Fresh gate, preparation, peer, commit, preflight, queue and postmerge receipts remain mandatory.
- No full test suite rerun. A local synthetic receipt-path experiment tested only pathlib semantics; actual helpers were not imported or run.
- The helper-lineage document is an accurate snapshot of initial copied bytes; subsequent fixes require explicit new current-hash provenance rather than silently claiming substitution-only lineage.
- Archive is scope-limited to selected listed helpers; it does not currently copy final-gates, preservation-check, review-check-final or its own helper source. Their current hashes are recorded in this review.

Exact structured evidence and findings: [20261015T152425Z-runtime-static-initial.json](20261015T152425Z-runtime-static-initial.json).
