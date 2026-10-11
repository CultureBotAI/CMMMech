# Round27 reviewed resource additions and BOF-slag extension

Worktree: `/private/tmp/CMMMech-expansion-round27-20261011`. Branch: `curate/cmm-expansion-round27-20261011`.
Trusted base: `3f1350b24b4f6248ed2e17caade936c15af9be93`.

Two new records bring the corpus to **171 records**: [BOF steelmaking dust](../../data/records/basic-oxygen-furnace-steelmaking-dust.yaml) and [electroformed copper-silver manufacturing scrap](../../data/records/electroformed-copper-silver-manufacturing-scrap.yaml). The Austrian 2022 study extends [BOF steel slag](../../data/records/basic-oxygen-furnace-steel-slag.yaml), preserving its earlier UK evidence. These are distinct process-defined secondary resources. No inherited criticality, universal microbial enhancement, industrial deployment or whole-feed product yield is asserted. No schema, validator, test, skill or governed artifact changes were needed.

## Evidence and independent review

BOF dust retains early culture enhancement followed by abiotic convergence, unlike hybrid pretreatment and direct-leaching conditions, lack of matched ferric and column controls, Table 1/Table 3 inventory differences, and column-clogging failure. Dissolved or source-calculated fractions do not establish isolated products.

BOF slag retains separate UK and Austrian feeds, the DSM 583 naming conflict, unmatched acid inputs, source figure/prose differences and cumulative retained reactor inventory. Downstream NaOH precipitation used synthetic solutions; it does not establish separation from actual bioleachate. The prior 2018 mechanism blocks remain unchanged.

Cu/Ag manufacturing scrap retains current versus historical CF3 naming, different flask/reactor operating conditions, limited biological replication, source endpoint and stirring-speed conflicts, Cu losses during iron removal, and local rather than bulk EDS composition. Its chemical electrowinning stage remains nonmicrobial and separate from culture-associated dissolution.

The initial independent Cu/Ag review identified a minor Figure 5 interpretation error. The curator removed the incorrect assertion that the graph corroborates the Results value 50.0%, retaining the source conflict with abstract 59% and avoiding an invented exact graph value. The initial observation and CREATE sidecar remain immutable; an actual EDIT sidecar records the correction. A separate publication audit corrected two frontier wording issues: attribution of that record error, and the limited scope of the goethite supplement inspection.

All three final independent scientific reviews are completed qualified passes matching the final record hashes. The corrected Cu/Ag successor explicitly resolves the exact initial F1 occurrence.

| Record | Final exact-state review |
|---|---|
| [Basic oxygen furnace steelmaking dust](../../data/records/basic-oxygen-furnace-steelmaking-dust.yaml) | [YAML](../../reviews/structured/20261011T162622Z-basic-oxygen-furnace-steelmaking-dust-round27-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T162622Z-basic-oxygen-furnace-steelmaking-dust-round27-independent/review.md) |
| [Basic-oxygen-furnace steel slag](../../data/records/basic-oxygen-furnace-steel-slag.yaml) | [YAML](../../reviews/structured/20261011T162604Z-basic-oxygen-furnace-steel-slag-round27-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T162604Z-basic-oxygen-furnace-steel-slag-round27-independent/review.md) |
| [Electroformed copper-silver manufacturing scrap](../../data/records/electroformed-copper-silver-manufacturing-scrap.yaml) | [YAML](../../reviews/structured/20261011T162619Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-resolution/review.yaml) · [Markdown](../../reviews/structured/20261011T162619Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-resolution/review.md) |

The [initial Cu/Ag finding](../../reviews/structured/20261011T161956Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-initial/review.md) and [publication wording audit](../../reviews/publication/20261011-round27/20261011T162349Z-readiness-audit.md) retain findings and dispositions. The [manifest](round27-frontier-20261011.json) records exact record/history/review paths and hashes. Research reports and raw-artifact manifests distinguish inspected evidence from inaccessible primary content. The [frontier](round27-frontier-20261011.md) prioritizes industrial goethite byproduct, EAF slag, furnace dust/anodizing sludge, superalloy residues and beverage cans. No exhaustion claim is made.

## Validation, provenance and publication boundary

Baseline `just check` passed **308 tests, 3 skipped in 165.15 seconds**, validating 169 records and 191 histories. A first dependency-setup attempt failed under sandbox DNS restrictions; the network-enabled retry passed. The final batch has 195 canonical histories, including separate CREATE and correction events for Cu/Ag scrap. Final corrected `just check` passed **308 tests, 3 skipped in 140.18 seconds**; separate `validate --require-records` and `validate-history --base 3f1350b24b4f6248ed2e17caade936c15af9be93` both passed with zero errors. All three changed record hashes remained unchanged through these checks. The separate trusted-base `just review-check --require-reviews` gate passed for all 199 bundles. The full exact-hash coverage audit also passed for all 171 current records; its receipt and command-log checksums are retained in the manifest.

Original main and unrelated work were preserved at session start: all 7,187 ignored/untracked entries matched the initial inventory, and the separate dirty skill worktree retained its five-file/Git-state baseline and bounded eight-path snapshot. Publication closeout will recheck before and after advancing original main. Hidden and ignored files were included in preservation and bounded deduplication searches.

All **171/171** current records have completed positive scientific reviews matching their exact hashes; there are **199 structured review bundles** and **28 distinct available review bases**. Of 1,159 previously tracked scientific/research files, only the intended BOF-slag record changed; the other **1,158** are byte-identical. README contains 171 distinct valid record rows.

All new review bases are the already-merged trusted base above; 27 of the 28 total bases are main ancestors. Existing annotated provenance tag `review-base/cmm-source-survey-20261009` retains commit `c0adc2c0763e1515ed07dc712b024974d98fb342`, tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`; no new topic-only review base is intended.

Live checks confirmed the active SQUASH/ALLGREEN merge queue, required `validate-strict` from App 15368 and no bypass actors. All **22** governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Admission, shared curation history and governance are installed. PR shepherd automation remains manual/comment-only and was not invoked. Future admission or synchronization must use CLAW's supported process.

This precommit report does not claim PR creation, CI success, queue merge or branch deletion. Publication receipts on the PR will record actual outcomes, isolated squash-shaped verification, and fresh main-only validation after deleting the topic branch. The earlier external issue attempt was rejected by automatic approval review over exact-content authorization; no issue is claimed from that attempt.
