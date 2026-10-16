# Queue guard remediation verification

UTC timestamp: 2026-10-16T00:53:01.222390+00:00. Reviewed source base: `27d842b3e6239bf60565f93c958d3f2cad395037`.

Author: codex /root/round104_borates, GPT-6. This is author verification; the independent successor is being performed separately. The original [author audit](helper-lifecycle-review.md) and [independent finding observation](queue-cleanup-initial-review.md) remain unchanged.

## Findings and corrections

[Issue #425](https://github.com/CultureBotAI/CMMMech/issues/425) tracks two minor guard findings:

- `round107-queue-preflight-command-location`: require one successful matching row at the exact isolated-clone cwd for each mandatory command. Eight focused negative fixtures cover duplicate rows and wrong cwd for all four commands.
- `round107-queue-independent-release-verdict`: require completed/passed positive review for the exact repository, PR, base, head and tree. Snapshot and recheck its digest; the posted review receipt must name the identical `independent_review_sha256`. Missing, negative, wrong-identity, changed-byte and posted-digest fixtures now fail closed.

Cleanup also requires both corrective issues #424 and #425 closed after verified squash merge; source issues #418–#423 remain open. The check occurs before branch deletion. The existing remote force-with-lease and local expected-old-SHA deletion are retained.

## Evidence and exact bytes

- `/private/tmp/cmm-round107-queue.py`: initial `85b1a0cb9ad4b96fa5be5d743527621457fb33c80daa5de2e7f1ee2cad40936e`, final `f505913f2e09aa4a20e10fc4c8b202bf3e24434bf526ca6e4bb018bac826d4f7`. Exact snapshots/diffs retained under `/private/tmp/cmm-round107-borates-research/helper-lifecycle-audit`.
- `/private/tmp/cmm-round107-cleanup.py`: initial `f9d84a05c7a995e7fbf2a86d898c679fc9ad443dd0dd3b35414da3ab8f467684`, final `4598476ee178073ae56e9bdce9eca5cf66a3f0c6630f195b0eee7f0e559f3e30`. Exact snapshots/diffs retained under `/private/tmp/cmm-round107-borates-research/helper-lifecycle-audit`.

All **79 strict mock cases passed**; receipt `/private/tmp/cmm-round107-borates-research/helper-lifecycle-mock-tests-final.json`, SHA256 `a5feda35dc8e0b2060c615dafd8205190fa7632c20ec027b72a6d6f23b083ab9`. Every subprocess was replaced with a fixture. No Git or GitHub mutation executed. Initial58-case and intermediate75-case results are preserved separately.

## Unresolved questions and verdict

The author fixes are verified, pending the separate independent successor. Issue #425 is not claimed closed before merge. Real commit, PR, preflight, release-review and hosted outcomes remain pending; mock success is not publication success.
