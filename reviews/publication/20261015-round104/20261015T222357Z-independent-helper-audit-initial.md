# Independent publication-helper audit: initial findings

Recorded UTC: 2026-10-15T22:23:57.509533+00:00. Initial inspection receipt UTC: 2026-10-15T22:22:19.118023+00:00.
Reviewer: codex (GPT-6), `/root/round104_ree`, separate from helper author `/root`.
Worktree: `/private/tmp/CMMMech-expansion-round104-20261015`. Trusted base: `6b6ccf160a457ceb5ebc265b55bbc5d515964707`.
Branch: `curate/cmm-expansion-round104-20261015`.

## Scope and actual actions

Static inspection of temporary commit, push/PR, isolated verification/coverage, review-base retention, queue, cleanup and archive helpers. No mutation helper was executed by this reviewer. Initial config still marked measured counts provisional; queue, cleanup, archive and later-stage helpers contained explicit `ROUND104_` placeholders. This observation is not execution approval or a claim that publication occurred. Final concrete topic/tree/PR/merge and receipt bindings require a successor audit.

Initial inspected file hashes:

| Helper | SHA256 |
| --- | --- |
| `cmm-round104-commit.py` | `f6a08889b89ce6af9cc98c74ac9cd3c367a7a982581ff9afccf92466dab47e1f` |
| `cmm-round104-push-pr.py` | `d4032e1aee905aae8ded65e2be1dfa12f88f8c5981dff9740abe3a4b39bce0f0` |
| `cmm-round104-isolated-verification.py` | `721deebbb17ad936d8297a01d9971b188f0f3c7c0e34102484308446386316d6` |
| `cmm-round104-isolated-coverage.py` | `f8f2f0bdb493b244af5655994ec479e9396fde4e90e8e45cc0470a826ac2a563` |
| `cmm-round104-queue.py` | `90d3eb88c1f2f01f6cdd710c728f495f487909662061c06f0354fe06dec52519` |
| `cmm-round104-cleanup.py` | `2dfdf533e559a5d845b1ff54c966053bcfea6b0350fe7d6395a3678cb3dc4dd7` |
| `cmm-round104-archive.py` | `d20c712e950b71caaccbcc0e019e97a4b0159c86d8e09702bd0b5e9151e98317` |
| `cmm-round104-review-bases.py` | `4c25d8855950c9834b51ea13b477a1ae168e7ed913b21382348dd1d1685b7468` |
| `cmm-round104-review-check-final.py` | `d0efcc8b86cb4fb49a71f6c9fa7ad37b093696902c54749d2c573bece1604ebf` |

The initial audit receipt is `/private/tmp/cmm-round104-helper-audit/independent-precommit-review.json`, SHA256 `3a0b1750fb16fa76f51a782ad0d486db160603500ef12389f8234c085ba5cfce`. It preserves the exact earlier inspected versions even though the coordinator began corrections while this artifact was being saved.

## Findings by severity

### Minor — gate-receipt-binding

Owner: `/private/tmp/cmm-round104-commit.py`, successful receipt loop before `git add`.

The inspected version accepted exit-0 `final-gates` and `review-check-final` receipts with matching log hashes without requiring their trusted base, the final-gates completed state, expected command set, or current record-input hashes. A stale or unrelated successful receipt could therefore pass this portion of the precommit gate.

Correction: require finalized configuration status; expected base and exact terminal commands; all zero exits; unchanged-input assertion; agreement between gate inputs and current measured coverage; rehash each record before staging. Acceptance: stale base, incomplete/failed receipts, altered commands, provisional counts or changed record bytes fail before mutation.

### Minor — push-config-binding

Owner: `/private/tmp/cmm-round104-push-pr.py`, configuration and commit-receipt loading before push.

The inspected version reloaded mutable configuration without comparing its digest to the successful commit receipt and did not reassert the topic's one-parent trusted-base relationship or intended origin URL. A changed config could be consumed by publication without retaining the exact reviewed configuration binding.

Correction: match config and publication-guard digests to the successful commit receipt, require its base/branch/head/tree and exact topic parent relationship, and require the canonical `https://github.com/CultureBotAI/CMMMech.git` origin before push. Acceptance: stale digest, mismatched parent/base, wrong branch/head/tree or remote fail before mutation.

## Positive checks and preserved boundaries

The isolated verifier uses a fresh main-only clone, fetches tags, checks the topic commit is absent, creates or observes the exact reviewed tree, validates records/history/reviews and requires all reviewed bases to be available. The retained annotated review-base tag preserves the non-ancestral historical source review. Exclusive receipt creation protects occupied paths; in-progress receipts lack a successful terminal exit and fail downstream checks. Cleanup uses expected-head remote lease and local compare-and-delete, preserves a detached worktree and checks the evidence tag.

The coordinator additionally requested inspection of the hosted-assessment gate. The version observed after these initial findings already calls `check_hosted_assessment`, requiring `passed is True`, exact topic/tree/merge and success of all five latest hosted attempts. No new unresolved finding is asserted against that already-hardened version; successor verification must check its concrete bindings and negative fixtures.

## Corrections, unresolved questions and verdict

The coordinator has begun correcting both findings with pure shared guards. Their final bytes and tests were not yet verified at the time of this initial observation. Required successor work: inspect corrected helpers and meaningful negative receipts, reconcile measured counts/config, bind real head/tree/PR/preflight/merge values, inspect final hosted evidence, and preserve source-review bases after branch deletion.

Verdict: **needs correction and successor verification** for the initially inspected helpers. No blocker/major finding or scientific-record defect was found. This audit makes no publication, merge, cleanup or approval claim.
