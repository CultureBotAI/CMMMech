# Independent release-helper integration review

UTC timestamp: 2026-10-16T00:57:00.301473+00:00. Reviewed revision: `27d842b3e6239bf60565f93c958d3f2cad395037` with current round107 working changes.

Reviewer: codex /root/round104_borates, GPT-6. Independent of the coordinator-authored posting and collector scripts. I authored the queue adapter; its independent acceptance is supplied by the separate REE-agent successor, not claimed here.

## Scope and evidence checked

The complete posting script, collector and final queue interface were read; exact snapshots are retained under `/private/tmp/cmm-round107-borates-research/release-helper-audit`.

- `/private/tmp/cmm-round107-post-review.py` — SHA256 `9195a664015abd99759b8acbb00dd7acf343e73deed405b28505937689c79aad`.
- `/private/tmp/cmm-round107-release-acquire.py` — SHA256 `30a0316b78ab23d707751805a13e6109b10e323520f60f9eab111a7b7ca09f64`.
- `/private/tmp/cmm-round107-queue.py` — SHA256 `f505913f2e09aa4a20e10fc4c8b202bf3e24434bf526ca6e4bb018bac826d4f7`.

The strict mock suite passed **20 cases** (18 posting, 2 collector). Receipt `/private/tmp/cmm-round107-borates-research/release-helper-tests.json`, SHA256 `a9734ce0a406f12a38cfe55d5182d05a8daab9c77e027cfcf749e7729fbd3882`. No Git, GitHub or network command was executed by these fixtures.

## Findings by severity

No supported critical, major or minor corrective finding.

## Integration and pagination assessment

- Posting requires completed/passed positive release assessment bound to repository, actual receipt-derived PR, head, tree and base; checks local origin/head/tree/clean state and fresh PR content before posting.
- Posting paginates prior reviews, issue comments and inline comments, refusing new discussion. It snapshots assessment and review-body bytes and rechecks them immediately before POST.
- The POST payload names the exact reviewed commit and COMMENT event. Raw GitHub response is saved separately; the local envelope preserves all server fields and adds independent_review_sha256. A fresh GET verifies the resulting comment.
- The queue requires that same envelope digest equal the current completed positive assessment digest, exact head/tree/base/PR/repository, and rechecks captured files before admission.
- Collector resolves PR/head from current round107 receipts; the GraphQL417 template is replaced with the actual PR number. REST files/commits/reviews/comments/events/check-runs/workflow runs/issues-comments/annotations/jobs all use explicit pagination.
- GraphQL review threads paginate with endCursor; nested comments exceeding100 trigger a failed acquisition rather than a false completeness receipt.
- Mock collection used PR987 and a synthetic head, two check-run pages and two workflow-run pages; both annotations were fetched, latest run202 and attempt3 jobs selected. No old417 query remained.

## Corrections

None required in this reviewed scope; no target script was edited.

## Unresolved questions and limitations

- Real commit/PR/preflight/independent release assessment receipts are still future artifacts at this precommit audit; no live success is inferred.
- The collector captures the aggregate combined-status response as a single snapshot; its statuses array is not an exhaustive paginated legacy-status history. Exact release assessment must use the required-check and workflow/check-run evidence and disclose this boundary.
- Collector acquisition is read-only evidence gathering, not approval: the later reviewer must validate raw/final PR identity and run conclusions. Successful HTTP acquisition alone does not establish passing CI.
- Posting/queue discussion and base observations have a non-atomic remote race; subsequent exact queue/live gates and squash verification remain necessary.
- No live GitHub mutation executed; all posting calls in tests were fixtures. No original-main project/environment command ran.
- The independent scope covers coordinator-authored posting/collector scripts; queue authorship is explicitly disclosed.

## Verdict

Pass with limitations for the inspected helper integration and mock cases. Actual release identity, hosted CI and publication results remain pending.
