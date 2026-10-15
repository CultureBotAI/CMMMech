# Independent publication helper audit

UTC: 2026-10-15T18:41:11.960970Z. Reviewer: codex `/root/round100_pentagonite` (GPT-6), independent of the helper author.

Reviewed base: `b6831c1da19b475ea048baea4ba5c10b96d678af`. Temporary helper bytes are uncommitted external inputs. This is a supplementary code audit, not an executed preflight.

## Exact inputs

- `/private/tmp/cmm-round100-isolated-verification.py` — SHA256 `055854012976be4a7144676d30ad72748858bbe710a7d112d76af6b4b18b331d`
- `/private/tmp/cmm-round100-isolated-coverage.py` — SHA256 `a7233d12b1f245d4c073933da755765d63d02dcdb15359797557fa6c4f9506ca`
- `/private/tmp/cmm-round100-helper-config.json` — SHA256 `959395a35d7c3c858abab45d09bb3e16f2d495ba11cdd6c4067657d4d81d9f2c`

## Finding and verdict

**Revise — one minor finding, `CMMMech:round100:coverage-receipt-exclusivity`.** The coverage helper checks `exists()` then uses `write_text()`. A dangling output symlink passes that check and is followed; the write is not exclusive. The wrapper already rejects pre-existing symlinks, so ordinary wrapper use is mitigated. The child helper should reserve its own receipt exclusively.

Bounded reproduction: `/private/tmp/cmm-round100-helper-audit-1wd7gzvk/reproduction.json` (SHA256 `18c720dea55c7e50878186d8a396cdd3e5e78b31c4385d75383afa253d302a05`). Only a unique empty fixture under `/private/tmp/cmm-round100-helper-audit-1wd7gzvk` was used. The helper exited 1 for expected zero-record count failure but created the symlink target, proving the output-path defect. No repository, helper or Git state was mutated.

Acceptance: reject occupied regular files and dangling/occupied symlinks without changing bytes; allow normal exclusive creation. Preserve the original helper and save a linked successor assessment.

## Supported checks

- Syntax parsed for both helpers without executing publication workflow.
- Mechanical diff of coverage helper versus round99 changed only the configured JSON path.
- Verifier pins configured base/branch, supplied topic tree, clean topic HEAD before preflight and single-parent exact base after merge.
- Fresh main-only clone uses --single-branch --branch main --no-tags then explicit tag fetch; fetch refspec and absent topic commit are checked before and after extraction/checks.
- Archive extraction uses a bounded fresh clone and data filter; tracked removed paths are removed only there; synthetic parent and exact resulting tree are asserted.
- Offline schema/history/structured-review commands require exit zero. Coverage additionally matches current record ID, target path, scope and exact SHA256 to completed positive scientific reviews, and checks every retained review base as a commit.
- Verifier receipts/log are created with exclusive mode and retain command outcomes, hashes, counts and unchanged config; child coverage output exclusivity is the one finding.
- Postmerge mode verifies local and remote topic-branch absence and exact merged parent/tree.

## Unresolved work and limitations

- No clone/preflight/merge command was run by this reviewer.
- Counts in current helper config remain explicitly provisional until six scientific record reviews are saved and reconciled.
- Remote review-base tags and their peeled commits are a separate coordinator verification; availability alone does not prove remote retention.
- Current audit covers recorded helper bytes. Revisions require a successor audit; no previous report is overwritten.

No owner correction is requested. Scientific owner bytes remain frozen. The coordinator owns remediation and the review issue.
