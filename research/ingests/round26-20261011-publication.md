# Round26 reviewed secondary-resource additions

Worktree: `/private/tmp/CMMMech-expansion-round26-20261011`. Branch: `curate/cmm-expansion-round26-20261011`.
Trusted base: `d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`. Acceptance: [issue 93](https://github.com/CultureBotAI/CMMMech/issues/93).

Four new records bring the corpus to **169 records**. They describe process-defined secondary resources with source-qualified laboratory evidence. No feed inherits elemental criticality. Dissolution, stage-specific solution depletion, resin elution and precipitation remain distinct from verified isolated-product recovery. No schema, validator, skill, governed artifact or previously committed scientific file was changed.

## Independent scientific reviews

| Record | Final exact-state review |
|---|---|
| [Electric-arc-furnace dust](../../data/records/electric-arc-furnace-dust.yaml) | [YAML](../../reviews/structured/20261011T154251Z-electric-arc-furnace-dust-round26-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T154251Z-electric-arc-furnace-dust-round26-independent/review.md) |
| [Basic-oxygen-furnace steel slag](../../data/records/basic-oxygen-furnace-steel-slag.yaml) | [YAML](../../reviews/structured/20261011T154039Z-basic-oxygen-furnace-steel-slag-round26-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T154039Z-basic-oxygen-furnace-steel-slag-round26-independent/review.md) |
| [Pharmaceutical blister packaging waste](../../data/records/pharmaceutical-blister-packaging-waste.yaml) | [YAML](../../reviews/structured/20261011T154432Z-pharmaceutical-blister-packaging-waste-round26-independent-resolution/review.yaml) · [Markdown](../../reviews/structured/20261011T154432Z-pharmaceutical-blister-packaging-waste-round26-independent-resolution/review.md) |
| [Beverage-carton hydropulping reject](../../data/records/beverage-carton-hydropulping-reject.yaml) | [YAML](../../reviews/structured/20261011T154436Z-beverage-carton-hydropulping-reject-round26-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T154436Z-beverage-carton-hydropulping-reject-round26-independent/review.md) |

Each record has an actual CREATE sidecar, a distinct inline event and an independent scientific review matching its final hash. The [manifest](round26-frontier-20261011.json) lists exact record, history and review paths. All four final verdicts are qualified passes; source limitations remain visible.

Independent review identified [issue 94](https://github.com/CultureBotAI/CMMMech/issues/94): the blister mechanism summary reversed the acid-comparison direction. The corrected record describes a conditional biogenic-acid advantage at 22 degrees C that is absent at 50 degrees C. The initial needs-curation observation remains immutable; an EDIT history and completed scientific successor explicitly resolve its finding. [Issue 95](https://github.com/CultureBotAI/CMMMech/issues/95) corrects a source-report inventory description from steel-slag draft to EAF-dust draft. The 166-entry raw snapshot confirms EAF dust as its sole addition beyond the trusted base. Both report copies retain matching prose and location-specific links; final packaging reviews capture corrected source context. A fresh independent release reviewer identified [issue 96](https://github.com/CultureBotAI/CMMMech/issues/96): the frontier's blanket completeness wording overstated the blister equation-layout inspection. Its corrected synopsis expressly retains documented primary-evidence access limits; no scientific record changed for that correction.

## Evidence boundaries and priorities

EAF dust retains the Fe-precipitation abstract/result discrepancy, Dust 1 table/graph mismatch and unresolved linkage between the best leachate and diluted electrolysis feed. Catholyte depletion and selected-metal electrode composition do not constitute overall dust-to-product yield. The unresolved mixed anode culture is not assigned invented taxon identifiers.

BOF slag retains preliminary community profiling, acid-unmatched controls, unestablished column replication and disagreement between feed inventories, concentrations and source extraction percentages. Source-reported Al above 100% is not normalized away. Poor resin elution is kept separate from aqueous removal; fitted kinetics and modeled speciation do not prove enzyme pathways or measured oxidation states.

Blister waste retains poor silver-fraction release, the high-temperature comparison null and lower 1 L results. The author-accessible equation rendition, composition discrepancy and lack of a complete balance prevent verified yield reconstruction. Proposed biosurfactant activity and blister-specific recovered-product purity remain unestablished.

Carton hydropulping reject separates enzyme pretreatment, culture-derived acid, less effective direct culture and chemical hydroxide precipitation. Comparable chemical-acid performance, DSM 583 naming conflict, non-detection without a stated limit and uncharacterized precipitate purity remain explicit.

The [prioritized frontier](round26-frontier-20261011.md) leads with superalloy residue powders, beverage cans, EAF slag, brake-pad residues and pickling sludge. Source dossiers distinguish full inspection from inaccessible figures, previews and metadata-only responses. Existing-resource extensions are listed separately. New identities and source families remain; exhaustion is not established.

## Validation and preservation

Baseline `just check`: **308 passed, 3 skipped in 145.58 seconds**, with 165 records and 186 histories. The first batch passed **308 tests, 3 skipped in 145.97 seconds**, with 169 records and 190 histories. After the review correction and added EDIT session, final `just check` passed **308 tests, 3 skipped in 126.15 seconds**. Separate nonempty record and trusted-base history checks passed with zero failures. The final corpus has **169 records, 191 histories and 195 structured review bundles**. The canonical structured-review gate and independent exact-hash coverage check passed: all 169 current records have completed positive scientific reviews. The original needs-curation observation remains as resolved history; it does not replace final coverage.

All **1124 prior scientific files** under data/history/reviews/research are unchanged from the trusted base. README membership is 169 unique record rows. Original ignored/untracked and unrelated dirty-skill work are preserved separately; the publication closeout rechecks them before and after advancing original main.

All new review bases are already-merged `d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`. There are **27 distinct available review bases**. Existing annotated tag `review-base/cmm-source-survey-20261009` retains commit `c0adc2c0763e1515ed07dc712b024974d98fb342`, tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`; no new otherwise-lost topic base is required.

The live merge queue remains active, SQUASH/ALLGREEN, with required `validate-strict` from App 15368 and no bypass actors. All 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Admission, shared history and governance are installed. The PR shepherd remains manual/comment-only and was not invoked. Future integration must use CLAW's supported admission and synchronization process; no governance side effect is part of this curation.

Independent publication audit, exact-tree squash-shaped preflight, queue merge, branch deletion and fresh remote-main validation are the remaining publication steps at report preparation. Their terminal evidence is recorded on the PR; these steps are not claimed complete in this precommit report.
