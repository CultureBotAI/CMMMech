# Round28 reviewed resource additions

Worktree: `/private/tmp/CMMMech-expansion-round28-20261011`. Branch: `curate/cmm-expansion-round28-20261011`.
Trusted base: `9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3`.

The cohort adds three records, bringing the corpus to **174**: [metal grinding sludge](../../data/records/metal-grinding-sludge.yaml), [metalliferous black shale](../../data/records/metalliferous-black-shale.yaml) and [ground waste tire rubber](../../data/records/ground-waste-tire-rubber.yaml). The geological black shale is a primary resource; the manufactured residues are secondary resources. None receives inherited criticality, a mineral-species identifier for a mixed feed, or an industrial-deployment claim. No schema, validator, tests, skills or governed artifacts needed modification.

## Scientific limits and review

The sludge record retains culture-associated changes at laboratory scale, a source-defined historical organism name with verified species mapping, missing matched abiotic controls, and unreconciled published recovery calculations. The black-shale record keeps three separate feeds and experiments: Bacillus-associated leaching after earlier acid treatment; the Heap1 culture comparison with copper nulls and a below-control manganese condition; and a mixed-community additive comparison with no abiotic arm. It preserves source figure/prose conflicts, ambiguous ferrous dosing, and residue-based extraction estimates with incomplete mass accounting.

The tire record accepts partial rubber transformation by the source's Rhodococcus culture. Chemical DES pretreatment stays separate. Gross mass loss and subtraction from the untreated abiotic control differ, and no matched DES-pretreated abiotic arm is shown. Relative zinc composition does not establish microbial zinc extraction or an absolute zinc mass balance. All accepted mechanisms remain laboratory evidence.

The independent reviewers found no corrective scientific defect in the frozen record bytes. A pre-freeze tire research handoff had mistakenly alleged a supplementary taxon spelling conflict; original-table inspection showed *rhodochrous*, and the curator corrected the handoff before the record/research dossier was frozen. The final dossier explicitly records this correction. Unsupported measurements and unresolved evidence remain scoped limitations.

All three final independent scientific reviews are completed qualified passes, matching the frozen record hashes.

| Record | Final exact-state review |
|---|---|
| [Metal grinding sludge](../../data/records/metal-grinding-sludge.yaml) | [YAML](../../reviews/structured/20261011T171324Z-metal-grinding-sludge-round28-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T171324Z-metal-grinding-sludge-round28-independent/review.md) |
| [Metalliferous black shale](../../data/records/metalliferous-black-shale.yaml) | [YAML](../../reviews/structured/20261011T171321Z-metalliferous-black-shale-round28-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T171321Z-metalliferous-black-shale-round28-independent/review.md) |
| [Ground waste tire rubber](../../data/records/ground-waste-tire-rubber.yaml) | [YAML](../../reviews/structured/20261011T171324Z-ground-waste-tire-rubber-round28-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T171324Z-ground-waste-tire-rubber-round28-independent/review.md) |

See the [ingest manifest](round28-frontier-20261011.json) for exact hashes/history references and [remaining priorities](round28-frontier-20261011.md) for source acquisition work. Full texts and images remain outside Git; tracked dossiers record evidence, access limits and raw-file provenance.

## Validation and preservation

Baseline `just check` passed 308 tests with 3 skipped, 171 records and 195 histories. The continuation worktree initially used the prior topic tip; before curation it was reanchored, with zero child commits and no file changes, to the durable merged base above. Both revisions have tree `54f58c3e5058f0d24282661d8645eb4748176c93`. All 7,208 ignored/untracked worktree entries were preserved. Independently completed fresh-main gates also passed on that exact tree. No duplicate baseline run is claimed.

Final `just check` passed **308 tests, 3 skipped in 159.30 seconds**. Separate `validate --require-records` and `validate-history --base 9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3` passed with zero errors: **174 records and 198 canonical histories**. All three frozen record hashes remained unchanged. The separate trusted-base `just review-check --require-reviews` gate passed for all **202 bundles**.

Preservation checks include hidden and ignored files. Original main's 7,187-entry ignored/untracked baseline and the unrelated dirty skill worktree's five-file/Git-state baseline and bounded eight-path snapshot are retained for closeout checks. Existing records, histories and reviews are immutable in this cohort; only new records and their new history/review artifacts are intended.

The exact-hash coverage audit passed for **174/174 records**, with **202 structured review bundles** and **29 distinct available bases**. All **1,194** prior scientific/research files are byte-identical to the trusted base. All **22** governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`.

New scientific reviews use the durable merged-main base above. All prior bases remain retained by main history or annotated provenance tag `review-base/cmm-source-survey-20261009`, whose remotely verified object is `fc4040c3abcd28f0a9cc52467e308100144ad1fd` and peeled commit is `c0adc2c0763e1515ed07dc712b024974d98fb342`. The native checker and isolated squash-shaped checkout verification are required before queue admission; no topic-only base is introduced.

The [initial publication audit](../../reviews/publication/20261011-round28/20261011T171354Z-readiness-initial.md) retains the resolved pre-freeze tire documentation finding, reviewer independence limits and the in-progress audit boundaries. Publication follow-up assessments are retained in the [same audit directory](../../reviews/publication/20261011-round28/).

Live ruleset inspection confirmed the active SQUASH/ALLGREEN queue, required `validate-strict` from App15368 and no bypass actors. Installed fleet admission, history and governance use the immutable CLAW pin; future integration must use CLAW's supported admission/synchronization process. PR shepherd remains manual/comment-only and was not invoked. This precommit report does not claim PR creation, remote CI success, merge or branch deletion; publication receipts will record those actual outcomes and fresh-main validation after deletion.
