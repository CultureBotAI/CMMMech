# Round30 main-sync finding and code resolution

- UTC: 2026-10-11T18:41:58.545121+00:00
- Reviewer: Codex `/root/round27_packaging`; helper authored and corrected by the root coordinator.
- Issue: [#108](https://github.com/CultureBotAI/CMMMech/issues/108), stable key `cmmmech-round30-sync-skill-branch-postcondition`, finding F1 (minor).
- Revision: `930ce995269f0ded5df009eb5916162971eb1f58` on `curate/cmm-expansion-round30-20261011`, working-tree state. No publication commit is implied.
- Scope: read-only inspection of the one-line synchronization-helper correction. No helper or Git/GitHub mutation was executed. Reviewer authored basalt; this artifact does not review that record's science.

## Evidence and initial finding

The original helper checked the unrelated skill worktree's HEAD, branch and status before main synchronization. Afterward it checked HEAD and status, then reported the complete Git state unchanged. Different branches can share a commit and working-tree status, so that last claim lacked a branch postcondition.

The original audit remains immutable at `/private/tmp/cmm-round30-sync-main-audit.md`, SHA-256 `c4456365909819a15d595f089ff7af3fa39b07beec3fb3e6a4ba30a6b0b613bf`. Its reviewed helper SHA-256 was `8eeda71f5208782f5a39571cc16ab6e828f91eb077947968872312db87fba867`. The issue body retained at `/private/tmp/cmm-round30-sync-review-issue.md` has SHA-256 `1c9cfd34ea772a5df3321c7b9c452406fc3cffef96c50cb1b84fea4e0bd1363c`.

## Correction and acceptance checks

The corrected `/private/tmp/cmm-round30-sync-main.py` has SHA-256 `d028675b640050cb9927dcd6f93798268c90c1d954c87f9c32e11c2ea6e4c301`. It now checks the same branch identity after the fast-forward, beside the final HEAD/status checks and before emitting success:

```python
assert git(skill,'branch','--show-current')==initial['repositories']['skill']['branch']
```

Python AST parsing passed without executing the helper. Removing only that final added assertion reconstructs the exact original reviewed SHA-256. This proves the reviewed correction is one added postcondition; all prior safeguards remain unchanged. The final code checks skill HEAD, branch, status and the bounded preserved-file identities before reporting unchanged Git state.

## Disposition and unresolved operational work

**F1 is resolved in code.** Actual queue merge, fresh postmerge verification and guarded main synchronization remain pending. The eventual preservation receipt is still required for operational completion; no execution, preserved-runtime-state or remote-issue-closure claim is made here. The temporary helper is outside Git and identified by its exact hash.
