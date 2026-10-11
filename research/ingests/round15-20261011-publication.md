# Round 15 reviewed minerals and geothermal-brine resource

Worktree: `/private/tmp/CMMMech-expansion-round15-20261011`.
Branch: `curate/cmm-expansion-round15-20261011`.
Trusted base: `a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0`.
Acceptance: [issue #59](https://github.com/CultureBotAI/CMMMech/issues/59).
Contract review finding: [issue #60](https://github.com/CultureBotAI/CMMMech/issues/60).
Review-provenance correction: [issue #61](https://github.com/CultureBotAI/CMMMech/issues/61).

Three additions bring the corpus to 122 records. Dittmarite and glushinskite
capture separate substrate/product identities in the same Suyamud2020 fungal
experiment already represented under magnesium. Lithium-bearing geothermal
brine adds a natural-resource identity with a qualified ureolytic pretreatment
result. Impurity removal with lithium retained in solution does not establish
isolated lithium recovery. No new criticality or industrial deployment is asserted.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Dittmarite](../../data/records/dittmarite.yaml) | mineral | [YAML](../../reviews/structured/20261011T100535Z-dittmarite-round15-successor/review.yaml) · [Markdown](../../reviews/structured/20261011T100535Z-dittmarite-round15-successor/review.md) |
| [Glushinskite](../../data/records/glushinskite.yaml) | mineral | [YAML](../../reviews/structured/20261011T100535Z-glushinskite-round15-successor/review.yaml) · [Markdown](../../reviews/structured/20261011T100535Z-glushinskite-round15-successor/review.md) |
| [Lithium-bearing geothermal brine](../../data/records/lithium-bearing-geothermal-brine.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T100226Z-lithium-bearing-geothermal-brine-round15-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T100226Z-lithium-bearing-geothermal-brine-round15-independent/review.md) |

Each record has an actual CREATE sidecar and separate inline event. The independent
reviewers did not author their review targets. Source controls, phase assignments,
analytical fractions, timing/percentage discrepancies and deployment limits remain
explicit; source limitations are not invented actionable defects. Review hashes
refer to the final record bytes, including history links. See the
[record/hash/history manifest](round15-frontier-20261011.json).

## Corrected review provenance

The independent publication audit found a minor error in the two initial mineral
reviews: they grouped the existing struvite record with magnesium as reusing
Suyamud2020. Magnesium cites Suyamud2020; struvite instead cites Kang2022
(DOI10.1007/s00253-021-11721-0). The new mineral records themselves were correct.
Issue #61 is addressed by two fresh successor observations that explicitly link
and correct the initial reviews. Both original immutable pairs remain present.
No record bytes or history events were changed for this review-context correction.
The three final reviews above are drawn from five new review pairs in total.

## Narrow schema correction

The independent contract audit found that naturally sourced geothermal brine
could not truthfully be assigned any existing resource kind. Issue #60 is addressed
by adding `primary_resource` to the native LinkML enum, defining its boundary in
the schema and record guide, and updating the add-record skill. No existing
record is reclassified. The offline validator already derives the closed schema;
no validator implementation or governed CLAW copy needed alteration.

The new regression checks a primary resource with microbial separation evidence,
then identity-only optionality, and rejects an adjacent unsupported spelling.
Focused validation tests passed 40/40; lint and skill structural validation passed.
The broader batch check results below include that regression.

## Sources and next work

- [Mineral dossier](round15-mineral-sources-20261011.md) and [JSON](round15-mineral-sources-20261011.json).
- [Brine dossier](round15-brine-sources-20261011.md) and [JSON](round15-brine-sources-20261011.json).
- [Prioritized remaining ingests](round15-frontier-20261011.md).

The dossiers distinguish newly acquired primary text/supplements, authority
identifier checks, retained local artifacts and bounded searches. PDFs remain
outside Git. Hidden/ignored files were included within the documented local
search boundaries. Further catalyst, rare-earth-feed, ash, produced-water and
product-grade leads remain; this is not global source exhaustion.

## Validation and preservation

Baseline: 307 tests passed, three skipped; 119 records and 135 histories valid.
Final native batch: 308 tests passed, three skipped; 122 records and 138 histories
valid. Separate required-record and trusted-base history gates also passed.
The current record hashes are retained with the actual command receipts; offline
validation does not establish scientific truth.

All 747 earlier tracked files under `data`, `history`, `reviews` and `research`
remain byte-identical to the trusted base. New reviews use that already merged
base. The annotated `review-base/cmm-source-survey-20261009` provenance tag is
retained; all sixteen distinct review bases must remain available after squash.
Required structured-review checks and final independent publication audit follow
this package assembly, before publication. Their actual results and the later
queue/merge/fresh-checkout receipts are recorded on the PR.

Canonical synchronization passed: all 22 governed artifacts match CLAW pin
`a5d562962c75a2ad9efd8160b548df5944315422`. The live native queue remains active
SQUASH/ALLGREEN with `validate-strict` from App15368 and no bypass actors.
Fleet admission and shared history are installed; PR shepherd remains manual
and comment-only. Future governance changes use CLAW's supported process.

An isolated squash-shaped checkout is validated before queue admission and a
fresh remote-main clone after merge/branch deletion. The original checkout is
advanced only after collision checks covering ignored/untracked paths and
matching before/after preservation snapshots. The installed add-record skill is
synchronized only after verifying its original bytes and the merged canonical
version; unrelated local metadata is preserved.
