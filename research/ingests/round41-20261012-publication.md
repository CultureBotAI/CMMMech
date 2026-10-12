# Round 41 scientific review and publication report

This batch adds todorokite and kutnohorite as mineral identity records and extends birnessite and nickel laterite ore with separately scoped primary experiments. The corpus grows from 211 to 213 records. The new mineral owners have no microbial mechanism: incomplete manganese-ore oxalate graphics remain a source gap. Birnessite retains its earlier Wei2012 arm and adds the distinct Ferrier2022 synthetic cobalt-bearing feed and Sasaki2008 prepared fungal-composite sorption assays. Newsome2020 extends the laterite owner with ore-specific cobalt mobilization evidence. No constituent criticality, isolated-metal recovery yield or industrial deployment is inferred.

Worktree: `/private/tmp/CMMMech-expansion-round41-20261012`; branch: `curate/cmm-expansion-round41-20261012`; trusted base: `762508748eaa4f857179fa6f3450765bc62ebd6a`. Report generated at 2026-10-12T01:33:06.509507+00:00.

## Scientific review

| Record | Action | Verdict | Review artifacts |
|---|---|---|---|
| [todorokite](../../data/records/todorokite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T012804Z-todorokite-round41-independent/review.md) / [YAML](../../reviews/structured/20261012T012804Z-todorokite-round41-independent/review.yaml) |
| [kutnohorite](../../data/records/kutnohorite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T012813Z-kutnohorite-round41-independent/review.md) / [YAML](../../reviews/structured/20261012T012813Z-kutnohorite-round41-independent/review.yaml) |
| [birnessite](../../data/records/birnessite.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T012836Z-birnessite-round41-independent/review.md) / [YAML](../../reviews/structured/20261012T012836Z-birnessite-round41-independent/review.yaml) |
| [nickel-laterite-ore](../../data/records/nickel-laterite-ore.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T012911Z-nickel-laterite-ore-round41-independent/review.md) / [YAML](../../reviews/structured/20261012T012911Z-nickel-laterite-ore-round41-independent/review.yaml) |

All four completed independent scientific observations match the current record bytes. The [manifest](round41-frontier-20261012.json) pins each record, complete history chain, review, source dossier and completed gate receipt. No corrective scientific finding was identified. Prior record science is retained, and the reviews disclose their precise fresh-assessment and preservation scope.

The birnessite extension distinguishes live fungal transformation from later sorption by a freeze-dried biogenic composite. Weak phase assignments, an unlike chemical-oxide comparator, source-normalization inconsistencies, ex situ XPS and opposed oxidant preferences remain explicit. The laterite extension separates natural ore origins, donor amendments, augmentation and repeat experiments; it retains a factor-of-ten nickel reporting conflict, source-specific sampling and controls, qualitative speciation and operational extraction denominators. A sum of aqueous and acid-extractable cobalt is not isolated product recovery. Two CREATE and two EDIT histories were appended. No schema, validator, test, skill or governed file changed.

## Evidence gaps and process corrections

[Issue #137](https://github.com/CultureBotAI/CMMMech/issues/137) records the remaining Yu2012 full-primary gap. The complete accepted Sasaki2008 study, an author-summary figure and thesis-summary pages do not substitute for the 2012 methods and complete original graphics. [Issue #134](https://github.com/CultureBotAI/CMMMech/issues/134) receives a progress update for newly recovered SEM reproductions; it remains open because original phase/control figures and discrepancies remain unresolved. Earlier source issues #103, #104, #120, #129, #130 and #133 remain open. These are unfinished research tasks, not corrected accepted-record defects.

Before publication, an author-handoff oxidant/electron-donor wording error was corrected before record integration. Unsaved review metadata with invalid dimension labels or YAML aliases was corrected before immutable reviews were saved. Four trailing spaces in the new mineral dossier were removed before final artifact hashing. None of these changes altered scientific record bytes after their final frozen state. The [independent helper audit](../../reviews/publication/20261012-round41/20261012T012548Z-independent-helper-audit.md) verified all 13 ported helpers and passed 1 positive plus 33 adverse pure-guard tests using explicitly earlier-round completed fixtures. Those tests are not round41 runtime publication evidence. Final document readiness is independently assessed in [the publication audit directory](../../reviews/publication/20261012-round41).

## Validation and preservation

The baseline reuses the preceding fresh remote-main full gate at this exact unmodified base/tree: `/private/tmp/cmm-round40-postmerge-20261012-published-terminal.json`, SHA-256 `27c53b7b0608f920f5c7742b6c1285419c188b2419ef906a09db0bf15ed4a59c`. No new baseline execution is claimed. The final cohort passed:

- `just check`: exit 0; log SHA-256 `408f773b76559736d91562a26d537e9143f241393e84d65e6379cbba8db6397b`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `7c214b2dfc443a636336b4bee5fb9b872bf92f9b0c8782a3fbefdbcbaddb32d7`.
- `uv run --locked cmmmech validate-history --base 762508748eaa4f857179fa6f3450765bc62ebd6a`: exit 0; log SHA-256 `992bba227a677a063bbb8584ffef1b45db04a156f0c7d396bba097852b6f479f`.
- `just review-check --base 762508748eaa4f857179fa6f3450765bc62ebd6a --require-reviews`: exit 0; log SHA-256 `590d8b81335cac7567181b043c0c8946f1d823c11590ee34c9ef0b45af5b15a0`.

`just check` passed 308 tests with 3 skipped in 164.97 seconds and validated 213 records and 248 histories. The separate native review check validates 252 bundles; exact-hash coverage identifies current completed positive scientific reviews for all 213 records and 42 available review bases. Structural validity does not itself prove scientific truth.

The [prepublication preservation receipt](../../reviews/publication/20261012-round41/preservation-prepublication.json) compares 7,187 hidden/ignored original-main entries and eight bounded unrelated skill-worktree entries, including symlinks and Git state, against the original snapshot. This is the actual prepublication check; final postmerge preservation remains a separate required step. Source originals stay outside Git, with provenance and SHA-256 manifests in the dossiers.

## Integration and publication status

The [live status summary](../../reviews/publication/20261012-round41/current-status.json) records merged CLAW admission, four active workflows and effective native SQUASH/ALLGREEN queue rules with required `validate-strict` and no bypass actors. Native canonical history and pinned governance are installed. Workflow presence does not verify PR-shepherd credentials or fleet-wide convergence. Future changes use CLAW's supported admission and synchronization process.

All four new reviews use the trusted base; the existing `review-base/cmm-source-survey-20261009` tag retains the earlier otherwise-lost provenance base. At this report's timestamp, commit, exact-tree isolated squash-shaped preflight, hosted PR and native queue checks, branch deletion, fresh-main validation and guarded main synchronization are still future execution steps. Their actual completion belongs in the PR closeout. [The frontier](round41-frontier-20261012.md) retains concrete next work; source exhaustion is not claimed.
