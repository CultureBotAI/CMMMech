# Independent review: integrated native and canonical history

## Identity, timestamp and reviewed working changes

- UTC snapshot: 2026-10-08T02:32:00Z.
- Reviewer: independent `queue_admission_audit` agent.
- Published CMMMech main: `842edc17fc603831c6ab56fd0ef1d813416d3ea5` (PR #9).
- Local base: `c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1`.
  Independently verified both have tree
  `f1031f7f18d5da43681d6f1ac2791f7c3a3bfe9b`; their tracked contents are identical.
- Governed pin: `849f336e025510316a5f235eb0af8547b8bd50cc`.
- SHA-256 of the reviewed tracked `git diff --binary HEAD`:
  `14627961c4c51c49ff2d39760c11a598d927046a238eec764bf4523f3ade7004`.
- Native untracked adapter SHA-256:
  `1d20985f4e3b068acb9842ceeb743c32acd297ff7f019e23a1122064a98882b8`.
- Untracked `tests/test_history.py` SHA-256:
  `ea9b3a4d6aae327b52b3ae2ff3757369aaf3e87e2ef9e6fb44d1e154141c8825`.
- Untracked `history/README.md` SHA-256:
  `0ea2166f9db96cb8d4d0875c4d1af860184f394cd8e3589308f2cbdd2fef31f6`.

## Scope and evidence checked

Read the current working guide, record guide, combined schema, CLI/validator,
native history adapter, recipes, check command, CI workflow and regression tests.
This review supersedes the earlier prototype's field design: **published inline
`curation_history: CurationEvent[]` remains intact; canonical sidecar paths use
the separate optional `history_refs` list**. Existing inline timestamp and shape
rules are preserved, and the new coexistence regression exercises both fields.

The adapter differs from the independently accepted symlink repair only in
renaming its attachment field and corresponding diagnostics to `history_refs`.
The #7 target-existence distinction and #8 ancestor-symlink/no-clobber/append-only
guards remain intact. No canonical payload or pin has been edited.

CI now passes its trusted pull-request base SHA, merge-group base SHA, or push
`before` SHA to `CMMMECH_HISTORY_BASE`, and checkout uses `fetch-depth: 0` so the
comparison revision is available. The combined event commit remains the checkout
target; the required job remains unconditional. The existing governed-sync step
still follows the offline gate and is not removed or weakened.

The new end-to-end regression first commits a valid session, then commits a
rewrite and verifies a clean working tree. Running the actual `scripts/check.py`
with the original base fails at append-only validation after lint, a nested smoke
suite and record validation pass. Holding the entire candidate constant but
setting the baseline to `HEAD` passes, demonstrating why the event-specific base
is necessary instead of merely asserting a command string.

## Independent verification

- Five focused actual-repository tests passed in **36.80s**: inline/sidecar
  coexistence, the committed directory-alias bypass, new-target existence,
  retention after historical-target removal, and the end-to-end committed-rewrite
  CI-base regression.
- Ran the supported standalone governed checker against the actual worktree:
  **18 governed artifacts match the pinned CLAW revision**. This is a real
  published-authority comparison, unlike the prior external-fixture tests.
- The implementer additionally reported the actual complete `just check` passed:
  **214 tests passed, 3 skipped**, lint passed, three records validated and the
  currently empty sidecar corpus validated. These full-suite results are
  implementer evidence, distinguished from the independent checks above.
- The inspected `history/` tree contains only its README; hidden/ignored-inclusive
  path inventory was used. No new scientific record bytes or real migration events
  are accepted by this code review because that next step has not happened yet.

## Findings by severity

- Critical: none.
- Major: none unresolved. #7 and #8 repairs remain effective after adaptation.
- Minor: none newly confirmed.

## Corrections, limits and verdict

The necessary integration correction—preserving incoming inline events while
using `history_refs` for canonical sidecars—is present and regression-tested.
The committed-rewrite gate now receives the correct CI comparison base, and the
governed byte identity check passes at the published pin.

**Accept the combined code and CI changes at the reviewed bytes.** Proceed with
real current-time migration events and record attachments, then independently
review each metadata-only record diff and its exact hash. Those events must state
the present migration, actual actor/model and earlier-review links without
reconstructing historical authorship or implying fresh scientific verification.
Final PR/merge-group CI and operational queue evidence remain required before
claiming completed deployment.
