# Round 60 scientific review and publication report

Add four distinct material owners: fluorite, spent lead-acid battery electrolyte, copper-smelter flue dust and traction-battery hydrometallurgical residue. The corpus grows from 274 to 278 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round60-20261012`; branch: `curate/cmm-expansion-round60-20261012`; trusted base: `3ac02ecf15ba53e28b15b2f4afcdcb083d0a226c`. Generated at 2026-10-12T15:05:31.073874+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [fluorite](../../data/records/fluorite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T145843Z-fluorite-round60-science/review.md) / [YAML](../../reviews/structured/20261012T145843Z-fluorite-round60-science/review.yaml) |
| [spent-lead-acid-battery-electrolyte](../../data/records/spent-lead-acid-battery-electrolyte.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T145900Z-spent-lead-acid-battery-electrolyte-round60-science/review.md) / [YAML](../../reviews/structured/20261012T145900Z-spent-lead-acid-battery-electrolyte-round60-science/review.yaml) |
| [copper-smelter-flue-dust](../../data/records/copper-smelter-flue-dust.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T145358Z-copper-smelter-flue-dust-round60-independent/review.md) / [YAML](../../reviews/structured/20261012T145358Z-copper-smelter-flue-dust-round60-independent/review.yaml) |
| [traction-battery-hydrometallurgical-residue](../../data/records/traction-battery-hydrometallurgical-residue.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T150313Z-traction-battery-hydrometallurgical-residue-round60-identity-resolution/review.md) / [YAML](../../reviews/structured/20261012T150313Z-traction-battery-hydrometallurgical-residue-round60-identity-resolution/review.yaml) |

All 4 independent final scientific reviews match the current record bytes. The [manifest](round60-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Fluorite evidence concerns washed-cell-associated settling, not dissolution or fluorspar commodity recovery. Electrolyte evidence separates culture-associated precipitation from chemical polishing and retains missing controls and contradictory discharge claims. Smelter dust evidence distinguishes acid pretreatment, controlled flask comparisons and an unreplicated continuous train with evaporation and operational interventions. Battery-process residue evidence preserves separate nickel/cobalt feeds, unmatched temperatures and inconsistent feed concentrations and reported cobalt yields.

## Findings and corrections

Four final independent scientific reviews assess the records. The exact-coverage gate caught a noncanonical target ID in the first traction-residue review, leaving 277/278 covered despite schema-valid bundles. Issue #188 records the defect. The original review is retained; a freshly inspected and reassessed scientific successor uses the canonical ID. Final coverage verifies the correction without scientific record edits; the publication audit must confirm the disposition before commit. Review issues: [#188](https://github.com/CultureBotAI/CMMMech/issues/188).

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Issue #186 tracks missing original zinc-leach-residue graphics, supplement and thesis evidence. Issue #187 tracks complete direct fluorite-dissolution evidence and unresolved source identity. Both remain open. No existing source issue is closed by this batch. Acquisition issues remain open; see the [frontier](round60-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round59-postmerge-20261012-published-terminal.json`, SHA-256 `37b177e9331824121bae3d36f73a5baabc2e2ac6f985d7f2c5cb79460443db3f`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `31ed61338a744c9b148197d23cbc4dc2f7a39c0a6649166252f9edbb587add2e`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `80ad3e411cdd26e65c9fb36e659f75a7debac59a6edcc248d71a591ccf93aebb`.
- `uv run --locked cmmmech validate-history --base 3ac02ecf15ba53e28b15b2f4afcdcb083d0a226c`: exit 0; log SHA-256 `c91dc67c9b7ba2c0016a2a94035439a26243aa498eab23730cd69df3e1a3ee3e`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 3ac02ecf15ba53e28b15b2f4afcdcb083d0a226c --require-reviews`: exit 0; log SHA-256 `13e07ea7c6f03bbd471cb38b7c77778ed3b991275d949252e7e35be409e34c06`.

Final `just check`: 317 passed, 3 skipped in 178.88 seconds. The gates accept 278 records, 326 histories and 337 review bundles. Exact-hash coverage verifies 278/278 current scientific reviews and 61 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round60/preservation-prepublication.json) verifies the original Documents checkout's 7,187 nontracked/ignored entries and the unrelated skill worktree's 7,389 tracked and nontracked/ignored entries, including file modes and symlink targets. Their Git states are unchanged from initialization. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round60/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
