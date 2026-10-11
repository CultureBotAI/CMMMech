# Round23 reviewed resource additions and marine evidence

Worktree: `/private/tmp/CMMMech-expansion-round23-20261011`.
Branch: `curate/cmm-expansion-round23-20261011`.
Trusted base: `80899a3d3ea5c0f7c5d54f1b3583e43768e92767`.
Acceptance: [issue 83](https://github.com/CultureBotAI/CMMMech/issues/83).

Two new secondary resources and two primary-resource updates bring the corpus to **156 records**. Waste LCD panels have evidence for laboratory indium/tin mobilization with explicit abiotic comparisons. Spent automotive three-way catalyst has evidence for aluminium-leaching pretreatment, without inferred isolated PGM recovery. Crusts gain a qualified community-associated metal-redistribution experiment; REY-rich mud gains explicitly inferred natural-diagenesis evidence. No resource inherits constituent criticality, and none establishes industrial microbial extraction.

## Independent scientific reviews

| Change | Record | Kind | Final exact-state review |
|---|---|---|---|
| New | [Spent automotive three-way catalyst](../../data/records/spent-automotive-three-way-catalyst.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T135351Z-spent-automotive-three-way-catalyst-round23-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T135351Z-spent-automotive-three-way-catalyst-round23-independent/review.md) |
| New | [Waste liquid-crystal display panels](../../data/records/waste-liquid-crystal-display-panels.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T135255Z-lcd-panels-round23-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T135255Z-lcd-panels-round23-independent/review.md) |
| Updated | [Cobalt-rich ferromanganese crusts](../../data/records/cobalt-rich-ferromanganese-crusts.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T135718Z-cobalt-rich-ferromanganese-crusts-round23-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T135718Z-cobalt-rich-ferromanganese-crusts-round23-independent/review.md) |
| Updated | [Rare-earth-rich deep-sea mud](../../data/records/rare-earth-rich-deep-sea-mud.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T135649Z-rare-earth-rich-deep-sea-mud-round23-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T135649Z-rare-earth-rich-deep-sea-mud-round23-independent/review.md) |

All four changed records have actual CREATE/EDIT sidecars, distinct inline events and independent scientific reviews matching final hashes. The [manifest](round23-frontier-20261011.json) lists both review formats, record/history paths and before/after hashes. Prior immutable source and review artifacts remain intact. No actionable scientific correction was identified in these four final reviews; scientific limitations remain explicit.

The publication auditor identified a minor readability defect in the new Ghiorse report and saved automotive review. [Issue 84](https://github.com/CultureBotAI/CMMMech/issues/84) tracks its correction. The source report's spacing was normalized without changing scientific values. The original automotive review pair remains immutable; a [corrected successor in YAML](../../reviews/structured/20261011T135759Z-spent-automotive-three-way-catalyst-round23-readability/review.yaml) and [generated Markdown](../../reviews/structured/20261011T135759Z-spent-automotive-three-way-catalyst-round23-readability/review.md) carries forward the same exact-target assessment with readable quantities. It explicitly uses `scientific_review: false` and does not claim a new literature assessment. Original scientific coverage remains authoritative; no record or history bytes changed.

## Evidence limits and remaining work

The LCD source has percentage/denominator and figure/table labeling discrepancies, unequal pH trajectories, unclear replication and tin maxima at different times. The automotive source has figure/prose and economic percentage conflicts, unlike initial media, missing supplements and no measured PGM product mass balance. Crust interpretation is limited by azide chemistry, solution-versus-solid partitioning, unavailable original figure pixels and distinct companion experiments. REY mud concerns inferred past diagenesis, model-dependent contribution and community associations; source units, table numbering and age inconsistencies remain explicit. No sequencing or mineral association alone proves a particular organism caused the observed material transformation.

The Ghiorse 1982 assessment separates natural-concretion inoculum origin from synthetic MnSO4 assays, and leaves quantitative B4 evidence for a later manganese-record assessment. See the [prioritized next ingests](round23-frontier-20261011.md). No schema, validator, skill or governed-artifact change was needed.

## Checks and preservation

Baseline: 308 tests passed, 3 skipped in 118.73 seconds; 154 records and 173 histories. Final `just check`: **308 passed, 3 skipped in 93.20s (0:01:33)**. All **156 records and 177 history sessions** validate. Separate `validate --require-records`, trusted-base history and structured-review checks passed; **178 review pairs** are valid. All 156 current records have independent scientific coverage matching current hashes.

Of 1016 prior scientific files under data/history/reviews/research, **1014 are byte-identical**; only the two explicitly named maintained records changed. All earlier sidecars, review bundles and source dossiers are preserved. All 24 review bases resolve; the annotated source-survey provenance tag is retained, and new reviews use the merged trusted base.

The 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Live ruleset 24692449 remains active with SQUASH/ALLGREEN queue, required validate-strict from App 15368 and no bypass actors. Admission and shared history are installed; the documented PR shepherd is manual/comment-only. This curation batch does not configure fleet capabilities. Future integration must use CLAW's supported admission and synchronization process.

Publication audit, exact-tree squash-shaped validation, native queue admission, actual merge verification, topic-branch deletion and fresh remote-main checks remain pending at preparation of this report. Terminal publication receipts belong on the PR. Original-main advancement requires clean-state, new-path/symlink collision and ignored/untracked preservation checks; unrelated worktrees remain intact.
