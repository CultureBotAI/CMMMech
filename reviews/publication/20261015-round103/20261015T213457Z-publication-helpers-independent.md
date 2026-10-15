# Independent round103 publication-helper audit

UTC: 2026-10-15T21:34:57.298719Z
Reviewer: codex /root/round100_sulfates (GPT-6).
Trusted base: `44d5b468519eb862b32ef54bf7c066bc0f79ba62`.

Verdict: helper templates pass with stated limits; concrete bindings and real lifecycle gates remain pending. No additional corrective defect was found.

Exact source snapshots and SHA256 values are in `20261015T213457Z-publication-helpers-independent.json` and `20261015T213457Z-publication-helpers-independent-sources/`.

## Prior receipt finding

For the push and archive portions of #391, the corrected helpers reserve their output before side effects. I independently reran all 16 isolated stub cases successfully, including occupied regular files, valid symlinks and dangling symlinks, fresh success and missing-config failure. Original versions reproduce effects before failure; corrected versions prevent them. No real Git/GitHub command ran. The issue-creator analog remains attributed to the separate preparation review.

## Guard assessment

- **Exact coverage and review bases:** Coverage enumerates hidden/ignored files and follows symlinks with cycle prevention. It requires record ID, maintained path, reviewed target scope and exact SHA256 to match completed positive scientific reviews, and verifies every referenced Git object is a commit. This supplements canonical review validation; it does not replace semantic triage or independently repeat historical science.
- **Squash-shaped verification:** Preflight constructs an exact-tree synthetic commit over trusted main in a fresh main-only/no-tags clone, then explicitly fetches tags. Postmerge requires the exact merge commit, single trusted-base parent and expected tree. Both reject availability of the topic commit, use offline dependencies, run strict records/history/native review checks and exact coverage, retain actual command/log hashes and require clean final state. Config stability is checked across the run.
- **Commit and PR creation:** Commit checks trusted base/branch, terminal local receipts and log hashes, current coverage record bytes, intended paths, staged whitespace, clean postcommit state and single parent. Push verifies committed head/tree, clean topic, unused remote branch, live main and exact returned PR metadata. The newly corrected PR receipt is exclusively reserved before any configuration read or Git/GitHub effect; failures are retained through that handle.
- **Queue admission:** Queue requires concrete preflight mode/base/head/tree, successful required command vectors and exact coverage/log/helper/config hashes, clean unchanged committed files, both repository and ref identities, exact PR title/body/files, successful required validate-strict, SQUASH/ALLGREEN rules, the exact COMMENTED review and absence of new unassessed discussion. Its final live-main read immediately precedes match-head queue admission. This is not an atomic base lock; native merge_group and actual merged-tree verification remain necessary.
- **Branch cleanup:** Cleanup requires the merged PR, actual merge single parent/tree, current remote main and clean expected topic. Remote deletion uses the expected topic OID as force-with-lease; local deletion uses update-ref with expected old OID after detach and worktree-owner inspection. It preserves branch configuration, detached worktree and evidence tag. These are conservative checks, not a global lock against every concurrent process.
- **Hosted acquisition:** Collector selects each expected workflow/event/head independently, fetches latest run_attempt metadata, all paginated attempt jobs and check annotations, then rechecks run_attempt and newest run. It requires topic/queue/merge identities and queue ancestry/tree agreement. PR comments, reviews, inline comments, events, review threads and selected issues are acquired; nested thread-comment truncation fails closed. Raw job steps and annotations are retained for semantic review. Successful job conclusions are not a claim that annotations are empty or all review findings are resolved.
- **Main preservation and manual hosted gate:** Finalizer checks exact postmerge and cleanup receipts, log/coverage hashes, current main/base, remote merge, expected parent/tree, collision with all prior nontracked entries, and --no-overwrite-ignore fast-forward. Before/after preservation covers bytes, sizes, modes and symlink targets. The pinned preservation digest was independently verified. The hosted assessment is only loaded/hashed by code; coordinator semantic assessment of actual final hosted results is intentionally a separate mandatory gate, not an automatic PASS assertion.
- **Archive:** Archive is additive into a new ignored directory with exclusive output receipt reserved before effects, no-overwrite file copies, source/destination hash checks, selected audit trees, a manifest and original-entry preservation checks. Its final validation/issue narrative is still a placeholder and must be written from actual evidence before execution. It does not include raw primary-source files, which remain at documented research paths.

## Pending execution checks

- Reconcile provisional helper-config totals from actual final native-review and coverage receipts.
- Bind all ROUND103_* sentinel values from actual committed head/tree/PR, exact preflight receipt and real issue dispositions; inspect the exact binding diff and frozen helper hashes before invocation.
- Run and verify actual committed-tree preflight, hosted strict/queue checks, merge identity, latest postmerge jobs/steps/annotations/discussion and isolated postmerge verification.
- Coordinator must semantically accept hosted assessment before finalizer; code does not automatically certify hosted PASS.
- Populate archive validation/issue narrative only from terminal evidence.

## Scope and limits

- All nine sources were statically inspected; only AST-relocated push/archive copies ran, with every subprocess mocked. No real remote or repository effect occurred.
- Current ROUND103_* placeholders and provisional totals intentionally prevent treating this template audit as final concrete binding approval.
- Batch gates/native review saves were still pending at audit time. No publication outcome is inferred from source code.
- Latest hosted snapshots and live-main reads are bounded observations; later reruns or concurrent changes require reassessment.

This audit assesses operational controls. It does not self-certify the Ce/La science I authored or substitute for independent native scientific reviews.
