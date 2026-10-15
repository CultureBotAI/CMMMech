# Round105 independent publication-helper audit

Recorded 2026-10-15T23:10:07.812812+00:00; reviewer `codex /root/round104_uranium` (GPT-6, Codex), independent of helper adapter `/root`. Reviewed revision `ee4ea8c2efa351a688946660c9ddc70560c3e86e` plus current temporary helpers and working changes. Exact file hashes and executable probe results are in the paired JSON.

**Verdict: changes requested.** Two minor defensive guard gaps are demonstrated; no external mutation was performed and no publication failure is alleged.

## Scope and evidence

Read the eight publication helpers, helper config and their retained adaptation diffs. All eight parse as Python. Inert AST execution tested exact finalization guard statements and cleanup control flow with mocked Git/API responses. Original main, refs and GitHub were not changed.

## Findings by severity

### Minor — PUB105-1: Finalization accepts incomplete postmerge validation evidence

The checked prefix would allow progression to main-preservation/fetch/fast-forward operations despite incomplete postmerge gate evidence. No external or repository mutation was executed.

Before any main fetch or fast-forward, require exact postmerge mode/base/topic/tree/merge binding, a complete required successful validation command set, successful coverage and measured counts, and current config/helper digests matching the commit receipt and postmerge receipt. Retain existing log and coverage digest verification.

Acceptance checks:

- A valid postmerge receipt is accepted.
- An empty command set and each missing required validation/coverage command are rejected.
- A nonzero required gate, failed coverage or changed counts is rejected.
- Changed current or receipt config/verification/coverage/guard digests are rejected.
- All evidence checks precede the first main mutation.

### Minor — PUB105-2: Cleanup deletion does not verify the Git remote repository

An otherwise matching branch SHA on a changed origin is deleted without verifying the repository URL. SHA lease protects branch content, not repository identity.

Require the expected CMMMech origin URL before any remote branch deletion, alongside the existing exact SHA lease and local compare-and-delete guards.

Acceptance checks:

- Expected origin with all existing PR/tree/SHA guards satisfied is accepted.
- A different origin is rejected before git push, checkout or update-ref.
- Moved remote or local refs remain rejected and the inspected worktree stays preserved.

## Supported protections

- Commit requires terminal complete batch checks, unchanged current record hashes, scientific coverage, explicit allowed paths, clean tracked changes, one-parent base and expected origin.
- Push binds config/guard digests, exact head/tree/branch/parent, origin, absent remote branch and live base before publication.
- Queue requires successful isolated preflight with required validations, coverage, current helper/config hashes, exact PR text/files/head/base, required hosted check, native squash queue rules, assessed discussion and immediate live-main comparison.
- Cleanup verifies actual merged PR, sole base parent and exact tree, retains the worktree, uses a remote SHA lease and local compare-and-delete, and preserves review provenance tags.
- Fresh verification constructs a squash-shaped tree or checks actual merge in a main-only clone with fetched tags and without topic commit availability; current scientific review coverage matches IDs, paths and hashes.
- Original-main finalization compares retained nontracked byte hashes, sizes, modes and symlink targets, rejects added-path collisions and uses --no-overwrite-ignore.

## Corrections

None applied by reviewer; initial audit remains immutable. Coordinator will address findings and request a successor review.

## Unresolved questions and limits

- Exact final topic/tree/PR/issue bindings and measured corpus counts remain pending.
- Native queue and final hosted/latest-attempt evidence must be assessed after those events occur.
- ROUND105 topic/tree/PR/preflight/issue placeholders and provisional counts intentionally await coordinator binding. This audit is not publication authorization or a claim that hosted checks passed.
- The probes demonstrate missing guard checks, not an observed wrong-repository deletion or incomplete real validation run.
- The retained original-main preservation inventory was inspected by structure and bound hash; this audit does not independently enumerate all current original-main content.
- Pure receipt checks are defense in depth under trusted local invocation; assertions are not hardened against an adversarial Python runtime.

## Review provenance

Reviewed helper copies and the nonmutating probe source are retained under `/private/tmp/cmm-round105-helper-audit/independent-initial-*` and `independent-probes.py`. The paired JSON embeds both probe outcomes and all nine inspected hashes. This is an immutable initial observation; future corrections require a separate successor artifact.
