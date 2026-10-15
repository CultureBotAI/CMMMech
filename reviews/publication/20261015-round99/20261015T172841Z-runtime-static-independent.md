# Independent round99 runtime helper review

Reviewed 2026-10-15T17:21:14.768760+00:00 to 2026-10-15T17:28:41.243358+00:00; reviewer `codex /root/round99_vanadium` (GPT-6). Base `beb757591995399e079d8892e8e27f8130f6bc5c`.

Verdict: **pass with limitations**. Thirteen active helper hashes and source lineage verified. One minor stale authorship literal was corrected; no unresolved findings.

- All thirteen source hashes match accepted round98 review bytes and all active scripts parse. Nine differ only by round/base. Four additionally change exact approved literals: final gate output and commit selectors, archival retention of both gate stages and original runner, accurate resource authorship.
- Corrected final-gates writer selects cmm-round99-final-gates-corrected.json and its matching log. Commit collector, log bindings and guard invocation consistently select that stage; all command/base/hash/unchanged-input/count requirements remain intact. The first gate receipt/log and original runner remain retained separately.
- Shared guards reject occupied files/directories/dangling links, reserve an exclusive descriptor before mutations, check inode identity and preserve explicit failure. Commit/publication handoff still binds current config/body/runtime helper bytes and prepared/committed files.
- Publish verifies branch/base/head/tree, clean checkout and live main before push; repeats exact handoff after push and passes verified PR body bytes through stdin. Enqueue reconciles preflight/commit/created receipts, current required checks, posted head-bound review, native queue rules and live main.
- Cleanup requires the actual squash tree, sole parent and exact topic head before leased deletion of the owned branch. Original-main fast-forward checks hidden/ignored collision paths, baseline file bytes/modes/links and retained tag/backup manifest. Isolated pre/post clones verify the exact tree/base and absence of the topic object.
- Hosted-five verifies all five workflow roles at exact commits and current attempts/jobs, complete pagination/blob identities, explicit issue states, posted review and closing identities. Its resource-authorship text now agrees with this cohort.
- Archive retains both initial/corrected gate receipts and logs, original runner, active helpers and guards plus selected pre/post/publication evidence. It is not a claim of complete primary-source or every API-response retention.
- Prior independent eight-test receipt/log/test bytes and all ten original tested helper hashes still match. Inspected tests cover occupied outputs, stale/missing bindings, bound stdin, after-push body changes, late collisions, explicit failures and receipt path replacement. No condition or behavior beyond exact stage-path selection changed, so this suite was not rerun.

Limitations

- This is static operational acceptance, not evidence that publication, native queue, branch cleanup or hosted workflows already succeeded. Fresh final gates, exact scientific coverage, immutable handoff, hosted peer, isolated preflight and postmerge verification remain required.
- Config counts and PR body are still provisional context; final measured counts and exact publication text require independent acceptance before binding. This artifact does not approve their current claimed final outcomes.
- No tests or mutating runtime helpers were run during this review. Prior regression is inherited only through verified source/diff/hash lineage; provider failures and live races are outside the fixture scope.
- Any later runtime helper byte change requires affected re-review. Final config/body changes require final metadata/handoff verification. Live main reads are observations, not atomic base locks; actual merge tree/parent remain required.
- The initial gate runner is a hash-proven retained prior version, not a fourteenth active helper. The report builder and separately reviewed readonly-hosted helper are outside this thirteen-helper acceptance.

Exact hashes, accepted diffs and preserved eight-test lineage: [20261015T172841Z-runtime-static-independent.json](20261015T172841Z-runtime-static-independent.json).
