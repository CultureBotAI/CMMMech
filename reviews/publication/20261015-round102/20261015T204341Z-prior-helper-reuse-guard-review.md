# Prior-helper reuse guard review

UTC: 2026-10-15T20:43:41.388191+00:00. Reviewer: Codex (GPT-6), `/root/round100_vanadium`.

Trusted base: `1c2a3bb043c4bd267a3d911d0e77b029c742689e`. Worktree: `/private/tmp/CMMMech-expansion-round102-20261015`.

**Verdict: guard corrections required before round102 reuse.** These are complete snapshots of four round101 reuse candidates, not helpers executed for round102. No helper was executed and no source helper, real Git ref or GitHub state was changed.

## Reviewed inputs

| Prior helper | SHA-256 | Snapshot |
|---|---|---|
| `cmm-round101-queue.py` | `842416bd34c260e387889d687b74b9cbda0ee945a889e77fba9a02a080c383c3` | [cmm-round101-queue.py](20261015T204341Z-prior-helper-reuse-guard-review-sources/cmm-round101-queue.py) |
| `cmm-round101-cleanup.py` | `1651060e62c1496e1852832ee8e92b6c04d8d8e5f915cbebda5f51002c3c0211` | [cmm-round101-cleanup.py](20261015T204341Z-prior-helper-reuse-guard-review-sources/cmm-round101-cleanup.py) |
| `cmm-round101-finalize.py` | `a42d092d2153cc4a8ada703fa7c3fe89f3ae54641da8f0b73143e6c49833f936` | [cmm-round101-finalize.py](20261015T204341Z-prior-helper-reuse-guard-review-sources/cmm-round101-finalize.py) |
| `cmm-round101-hosted-final-collector.py` | `67b0e1618aa792ca9173669dd2bec6bd37d4e7516c17faed5c0b5418e2939116` | [cmm-round101-hosted-final-collector.py](20261015T204341Z-prior-helper-reuse-guard-review-sources/cmm-round101-hosted-final-collector.py) |

## Findings by severity

### R102-OPS-001 — major: Fast-forward may overwrite ignored original-main work before preservation assertion

Input: `cmm-round101-finalize.py`, lines 20, 23. Status: open.

baseline_unchanged verifies stored nontracked bytes before and after git merge --ff-only, but the merge command lacks --no-overwrite-ignore. Git documents ignored-file overwriting as the default. An ignored file at a path introduced by the target tree can be destroyed before the after-check reports failure.

**Correction:** Use --no-overwrite-ignore and retain before/after preservation checks. Prefer a target-tree collision check as additional evidence.

**Acceptance:** In a disposable repository, a pre-existing ignored file colliding with a newly tracked target path must cause refusal with HEAD, file bytes and mode unchanged. A non-colliding fast-forward must succeed while preserving ignored content.

[Official Git documentation](https://git-scm.com/docs/git-merge).

### R102-OPS-002 — major: Local branch deletion lacks an atomic expected-old-OID guard

Input: `cmm-round101-cleanup.py`, lines 21, 23. Status: open.

After detach the helper reads refs/heads/BRANCH and then invokes git branch -D. A concurrent ref advance between these separate operations can be force-deleted. Remote deletion already has an explicit expected-SHA force-with-lease.

**Correction:** After detaching and verifying no worktree owns the branch, use atomic compare-and-delete with expected HEAD. Retain harmless branch configuration rather than risk deleting concurrently changed configuration.

**Acceptance:** In a disposable repository, advancing the branch after the expected SHA is captured must make deletion fail and preserve the advanced ref. With the exact expected SHA and no worktree owner, deletion must succeed while detached HEAD remains unchanged.

[Official Git documentation](https://git-scm.com/docs/git-update-ref.html).

### R102-OPS-003 — minor: Admission checks base SHA but not the intended branch ref

Input: `cmm-round101-queue.py`, lines 21, 30. Status: open.

The PR check requires base.sha == BASE, but does not assert base.ref == main. Another target branch at the same SHA is not excluded by this predicate; checking main branch rules and the live main SHA does not itself bind the PR base ref.

**Correction:** Bind the PR base ref to main and explicitly bind expected head ref and repository identity before admission.

**Acceptance:** Static inspection of the rebound helper must show these explicit bindings, and fixture predicates must reject a PR with the right SHA but the wrong base/head ref or repository.

### R102-OPS-004 — minor: Selected-run attempt recheck does not detect a newly created workflow run

Input: `cmm-round101-hosted-final-collector.py`, lines 39, 64, 82. Status: open.

The collector lists matching workflow runs once, selects the latest created run and later checks that selected run ID for an unchanged run_attempt. A newer matching run appearing after the original list can be omitted while all_five_latest_attempts_successful remains true.

**Correction:** Before final receipt, re-list each workflow/event/SHA and require the selected latest run ID and run_attempt to remain the inspected values; fail closed if they changed.

**Acceptance:** Fixture with a newer matching run after initial selection must fail freshness assessment; unchanged latest run and attempt must pass. Keep final observation times explicit.

## Existing guards checked

- Queue pins exact local head/tree/branch and clean tracked/untracked status; checks preflight/config/helper/log/coverage hashes and required command results; binds posted review to the exact head and rejects new discussion.
- Queue reads live main immediately before admission and uses --match-head-commit. This is an observation, not an atomic base lock.
- Cleanup verifies the merged PR, merge parent BASE, expected tree and live-main commit before remote cleanup. Remote deletion uses an explicit expected-SHA force-with-lease.
- Hosted collector requests exact workflow/event/SHA, current run_attempt and paginated jobs, check annotations, reviews, comments, threads and issue surfaces; it rejects truncated thread-comment pagination.
- Finalizer pins its preservation manifest hash, base/head/tree and exact merge parent, and checks pre-existing nontracked file bytes/modes and symlink targets before/after. It does not run project environment commands in original main.

## Limits and unresolved questions

- The finalizer loads and hashes hosted assessment but the coordinator must semantically verify PASS before invocation. This stated manual boundary is not classified as a defect.
- Collector queue-tree equality alone is not proof of queue ancestry or connection to this PR. Concrete round102 evidence assessment must verify queue event/ancestry linkage.
- Even final re-listing and live-main checks are non-atomic observations. Later remote changes are possible; each receipt must retain observation times and no permanent freshness guarantee should be claimed.
- No prior-round execution failure or data loss is asserted. Findings concern supported code paths when relevant collisions or concurrent changes occur.
- Concrete round102 PR/base/head/tree, branch/repository, issue IDs, receipt paths, preservation-manifest hash and historical tag bindings have not yet been reviewed here.
- Corrected round102 helper source and concrete bindings remain pending.
- Isolated toy Git regression is planned only after corrected code is ready; no test result is claimed in this initial audit.

## Corrections and successor review

No corrections were made in this review. The coordinator will author corrected round102 helpers. Their concrete bindings, behavioral regressions and final source hashes require a separate successor assessment. No initial finding is closed by this document.
