# Independent adversarial recheck: native history repairs

## Identity and reviewed state

- UTC timestamp: 2026-10-08T02:20:40Z.
- Reviewer: independent `queue_admission_audit` agent.
- CMMMech base: `c32d78e26a15bb67a737700668badaed7da10597`, with uncommitted native
  history changes.
- Scope: the nine native files recorded in the
  [prior review](20261008T021706Z-history-adversarial.md), including the repair
  for [#8](https://github.com/CultureBotAI/CMMMech/issues/8) and the target
  distinction tracked in [#7](https://github.com/CultureBotAI/CMMMech/issues/7).

Relative to the prior reviewed snapshot, six file hashes are unchanged. Changed
reviewed bytes are:

| Path | SHA-256 |
|---|---|
| `src/cmmmech/history.py` | `0271f2ff4712702d0d85fb96b687b26b5ec350602790cd0b4c918e880799afa7` |
| `tests/test_history.py` | `a70af6c49a56e38627db5d34833c9895efdf9fe102eff7db5eb9023423315733` |
| `docs/records.md` | `e9befd31a07b8f6408133a0d42328a0f772437e6997f05c54a525c5b410d1acb` |

The independent snapshot was captured at 02:19:53Z; these three hashes were
rechecked against the native worktree at this report's timestamp.

## Evidence checked

Re-read the repair and regression tests against the previously reviewed canonical
history schema. `check_history_path` now walks every lexical component beneath
the resolved repository root and refuses any sidecar symlink before opening a
record or creating a session. Direct structural validation also checks this
boundary. This keeps sidecars physically within the Git-audited `history/` tree.

Discovery now walks without following links and explicitly rejects root,
intermediate, file and dangling symlinks rather than silently skipping nested
aliases. Ordinary target-file semantics are separate. The append-only comparison
continues to reject edits and deletion of published sidecar bytes against the
chosen reviewed Git base.

Independent full native suite: **97 passed in 32.90s**, including the actual
committed `history -> archive` bypass reproduction, pre-read reference rejection,
scaffolder ancestor rejection, nested/dangling discovery, no-clobber creation,
timestamps and actor fields, reference identity, duplicate sessions, closed
schema and new-target/retained-history distinction. Native lint and
`git diff --check` also passed.

The tests ran in a separate external fixture at
`/private/tmp/cmmmech-history-independent-review-fixed-20261008`, containing a
snapshot of the native implementation and canonical schema bytes. The reviewer
did not overwrite the implementer's fixture or alter native implementation.
This is independent native-code validation, not a claim of deployed governed
artifacts, successful synchronization, or final repository CI.

## Findings by severity

- Critical: none.
- Major: prior #8 finding is **resolved in the reviewed bytes**.
- Minor: none newly confirmed.

## Corrections and remaining integration work

- #8's directory-alias bypass now fails validation, and creation through the
  same alias is refused; regression tests exercise the concrete previous failure.
- #7 remains correct: new sidecars with a reviewed base require a current file;
  existing unchanged sessions can remain after their historical target is removed.
  Presence and attachment stay advisory as specified by the canonical contract.
- No initial migration sidecars were part of this reviewed implementation
  snapshot. Their real actor/model, timestamps, target links and claimed work must
  be checked when generated; the guides correctly prohibit invented backdating
  or reconstructed authorship.
- The parent task still owns supported governed synchronization, event-specific
  CI comparison-base wiring, the final combined gate, initial provenance and
  scientific-record reference additions, remote CI and queue-execution proof.

## Verdict

**Accept the repaired native history implementation.** No open blocking finding
remains within this review's implementation scope. Preserve the prior report as
the evidence for the fixed defect; final integrated deployment needs its own
checks and review of any subsequent substantive edits.
