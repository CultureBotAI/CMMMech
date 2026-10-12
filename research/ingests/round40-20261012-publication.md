# Round 40 scientific review and publication report

This batch adds birnessite and extends manganese ore with a separate primary fungal experiment. The corpus grows from 210 to 211 records. Birnessite represents the synthetic sodium-form feed in Wei2012, whose product arm is already represented by lindbergite; the new material view does not create an independent replication. The manganese-ore extension covers Ferrier2022's natural mixed Nkamouna laterite. No constituent criticality, isolated-metal yield or industrial deployment is inferred.

Worktree: `/private/tmp/CMMMech-expansion-round40-20261012`; branch: `curate/cmm-expansion-round40-20261012`; trusted base: `215cb3f4f9940b3785cf8ca20ecb28d2acc89950`.

## Scientific review

| Record | Action | Verdict | Review artifacts |
|---|---|---|---|
| [birnessite](../../data/records/birnessite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T005518Z-birnessite-round40-independent/review.md) / [YAML](../../reviews/structured/20261012T005518Z-birnessite-round40-independent/review.yaml) |
| [manganese-ore](../../data/records/manganese-ore.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T005436Z-manganese-ore-round40-independent/review.md) / [YAML](../../reviews/structured/20261012T005436Z-manganese-ore-round40-independent/review.yaml) |

Both final independent scientific observations match the record bytes. The [manifest](round40-frontier-20261012.json) pins records, histories, reviews, source dossiers and gate receipts. Neither review found a corrective record defect. The manganese-ore reviewer freshly assessed Ferrier2022; older Borkar2026 fields remain exactly unchanged and linked to their earlier independent resolution review. That preservation check is not presented as fresh review of older science.

Birnessite retains uncertain batch composition/polytype, separate organism arms, 23/25-day sampling differences, recovered oxalate assignments and hot-water/drying limits. The ore extension retains incomplete transformation, fragment aluminium/magnesium figure-versus-prose conflict, synthetic-versus-natural arm distinctions, qualitative elemental associations and missing causal/mass-balance controls. All accepted observations are laboratory results. One CREATE history and one EDIT history were appended. No schema, validator, test, skill or governed file changed.

## Evidence issues and corrections

[Issue #133](https://github.com/CultureBotAI/CMMMech/issues/133) tracks original samarium biomineralization graphics, protocol discrepancies and source-era strain naming. [Issue #134](https://github.com/CultureBotAI/CMMMech/issues/134) tracks original manganese-ore oxalate main graphics, phase/time/control checks and manuscript-versus-CIF discrepancies. Full text and official crystallographic supplements were recovered where available; these advances do not resolve the outstanding acceptance requirements. Both studies remain source-only deferrals with no speculative record or history. Earlier source issues #103, #104, #120, #129 and #130 also remain open.

An unsaved review draft failed UTC-format and maintained-target metadata validation; those metadata were corrected and canonical inspection repeated before the review was saved. No scientific record bytes changed for that correction. Independent publication review identified missing README inventory coverage and a displaced historical review link. [Issue #135](https://github.com/CultureBotAI/CMMMech/issues/135) tracks the correction: birnessite and the new ore arm are represented, the round39 report link is retained, and the latest frontier remains round40. Initial and resolving observations are retained. Final publication review supplies the findings and dispositions in [the publication audit directory](../../reviews/publication/20261012-round40).

## Validation and preservation

The baseline reuses the preceding fresh remote-main full gate at the exact unmodified base/tree, receipt `/private/tmp/cmm-round39-postmerge-20261012-published-terminal.json`, SHA-256 `88efeb16b8484a1ae9572305867b7c993c06f2851da12e77c8a933ab3c2f80a2`; no new baseline execution is claimed. The completed cohort then passed:

- `just check`: exit 0; log SHA-256 `0665c580872720049264794b273d7ea6e4ee7e888a0a06951c26f725ba6b48db`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `8a10f1c1959e9e938e137e67cf47d6b48b4dfd325ea5732a7df10607c6cf4558`.
- `uv run --locked cmmmech validate-history --base 215cb3f4f9940b3785cf8ca20ecb28d2acc89950`: exit 0; log SHA-256 `e478038f34a36fe0187e8927493285080a190fff085e60de5c93d35d18255d30`.
- `just review-check --base 215cb3f4f9940b3785cf8ca20ecb28d2acc89950 --require-reviews`: exit 0; log SHA-256 `d4dad13bda11729d12614af5ce9a0f90a2d4d4605cca455bc7fab21803a1f4e4`.

`just check` passed 308 tests with 3 skipped in 149.21 seconds, validating 211 records and 244 histories. The separate structured-review check and exact-hash audit establish 248 valid bundles, 41 available review bases and current scientific review coverage for all 211 records. Structural validity does not itself prove scientific truth.

The [prepublication preservation receipt](../../reviews/publication/20261012-round40/preservation-prepublication.json) compares 7,187 hidden/ignored original-main entries and eight bounded unrelated skill-worktree entries, including symlinks and Git state, against the untouched initial snapshot. All project commands used the isolated worktree; standalone source tools ran outside checkouts.

## Publication and remaining work

The [live status snapshot](../../reviews/publication/20261012-round40/current-status.json) confirms merged CLAW admission, four active workflows and effective native SQUASH/ALLGREEN queue rules, required `validate-strict`, and no bypass actors. Canonical history and pinned governance are installed. Workflow presence does not verify PR-shepherd credentials or fleet-wide convergence. Future governance changes use CLAW's supported admission and synchronization process.

All new reviews use the trusted main base. The existing `review-base/cmm-source-survey-20261009` tag retains the earlier otherwise-lost base. Exact-tree isolated squash-shaped validation is required before queue admission; actual hosted PR/merge-group checks, branch deletion, fresh-main validation and guarded main synchronization are future execution steps at this report's timestamp. Completed runtime evidence belongs in the PR closeout.

[The frontier](round40-frontier-20261012.md) retains concrete source priorities. Curation has advanced; source exhaustion is not claimed.
