# Round30 main synchronization helper audit

UTC: 2026-10-11T18:38:47.524601+00:00

Reviewer: Codex `/root/round27_packaging`. Read-only code inspection and AST parse; no helper, synchronization, Git mutation or remote action executed. This is a publication-safety audit and does not independently certify the reviewer's own basalt record.

Target: `/private/tmp/cmm-round30-sync-main.py`, SHA-256 `8eeda71f5208782f5a39571cc16ab6e828f91eb077947968872312db87fba867`.

Baseline receipt: `/private/tmp/cmm-round30-preservation-before.json`, SHA-256 `63c41e5c0c3b7f6307099fbe83b0ddbf9612905cf65eff22ac9ae458d6986576`; main inventory7187 entries, unrelated skill inventory8 explicitly bounded entries. The baseline names the original CMMMech main checkout and `/private/tmp/CMMMech-add-record-skill-20261010`, not the round30 worktree as the synchronization target.

## Findings by severity

### F1 — minor: final skill-branch postcondition is omitted

Before the main fast-forward, the helper checks unrelated skill HEAD, current branch and status. Afterward it checks HEAD and status but omits branch, then emits `unrelated_skill_git_state_unchanged: true`.

A branch name is not determined by HEAD and status: another branch can point at the same commit with identical working changes. Thus the receipt's full Git-state claim is slightly stronger than its final checks. This is an assurance gap, not evidence that the helper switches the unrelated checkout.

Correction: repeat `assert git(skill,'branch','--show-current') == initial['repositories']['skill']['branch']` alongside the final HEAD/status assertions. Acceptance: inspect the amended helper and confirm all three final state checks precede receipt emission. No mutation or test execution is needed to verify this small guard addition.

## Supported safeguards

- Requires a successful fresh postmerge terminal receipt whose merge commit matches cleanup and whose expected tree matches the committed tree.
- Requires original checkout branch `main`, exact reviewed base via the commit receipt, and a clean tracked/unignored worktree before synchronization.
- Uses `git ls-files --others -z` without exclusion options, so the main preservation inventory includes hidden and ignored nontracked files. Hashes compare file bytes; symlinks compare link targets rather than following them. Exact name-to-identity mapping is compared before and after, detecting additions/removals and changed entries within this declared scope.
- Skill file checks are accurately bounded to the eight baseline entries; this is not a claim that every file in that worktree was inventoried.
- Requires the shared `origin/main` ref to equal the verified actual merge and invokes only `git merge --ff-only <merge>` on main. It has no reset, stash, clean, remote push, branch deletion, or skill-checkout mutation.
- Afterward requires main HEAD and tree to match the actual merge/committed tree, a clean tracked/unignored main worktree, unchanged preservation mappings/counts, and unchanged skill HEAD/status. The missing final skill branch check is F1 above.
- Fresh postmerge verification and the actual synchronization receipt remain pending. Interrupted operations require state inspection; this one-time helper refuses an existing final receipt.

Verdict: one minor postcondition correction requested before execution; no other actionable finding identified. Prior helper audit remains unchanged.
