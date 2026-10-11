# Fourth expansion: scientific acceptance and publication preparation

Trusted base: `c081a749cd63feafcc25414f5ad006d1f78f1e36`.
Worktree: `/private/tmp/CMMMech-expansion-round4-20261011`.
Branch: `curate/cmm-expansion-round4-20261011`.

## Accepted scope

The add-record workflow followed the round3 frontier: accessible feed-specific
evidence for two mineral hosts and a production sludge, an antimony source
decision, and a bounded search for phosphorus/individual-REE evidence. Six
new roots retain the distinction between elements, minerals and resources.

| Record | Dossier | Scientific boundary |
|---|---|---|
| [Antimony](../../data/records/antimony.yaml) | [Johnson2021 and BES decision](round4-antimony-20261011.md) | Sediment-community transformation; strong abiotic sorption, indirect sulfide route, lactate recipe conflict and nonunique product assignments |
| [Phosphorus](../../data/records/phosphorus.yaml) | [Kang2022](round4-phosphorus-cerium-20261011.md) | Fungal mobilization from mixed struvite/dittmarite; background phosphate and unspecified Pi assay prevent a mineral-specific yield |
| [Cerium](../../data/records/cerium.yaml) | [Same Kang study, separate stage](round4-phosphorus-cerium-20261011.md) | Pretreated cell-free fungal filtrate; resin/pH processing and synthetic Ce solution; removal is not pure-metal recovery |
| [Chalcopyrite](../../data/records/chalcopyrite.yaml) | [Mineral-host dossier](round4-mineral-hosts-20261011.md) | IMA identity separate from impure Aitik concentrate; released-Cu assay and differing endpoints constrain comparison |
| [Sphalerite](../../data/records/sphalerite.yaml) | [Mineral-host dossier](round4-mineral-hosts-20261011.md) | IMA identity separate from iron-bearing concentrate; matched-chemistry null results and source tension remain explicit |
| [GaAs-production hydroxide sludge](../../data/records/gaas-production-hydroxide-sludge.yaml) | [Fritze2026](round4-gaas-sludge-20261011.md) | Characterized secondary resource; acid-dominated leaching and higher-load arsenic counterevidence; no inherited criticality |

Antimony and cerium cite the final US 2025 list; phosphorus cites Canada's
10 June 2024 update. Each includes jurisdiction, issuing authority, edition
and commodity-to-element scope. Mineral/resource roots inherit no constituent
criticality. No record asserts industrial deployment. Studies reused across
element, mineral and resource roots are identified as shared evidence, not
independent replications.

Six actual CREATE sidecars and separate inline events were attached before
review. Existing 21 records and all committed histories/reviews remain unchanged.
No schema, validator, test behavior, dependency or governed file changed;
the existing contract supports these bounded claims. Measurements outside the
exact mg/kg source-cell contract remain qualified prose.

## Review and acceptance

[Issue 27](https://github.com/CultureBotAI/CMMMech/issues/27) tracks concrete
scientific and publication acceptance. It does not falsely allege that acknowledged
source limitations are missing from the records. Each record is reviewed by a
different agent from its curator: the mineral curator reviews antimony, the
antimony curator reviews both minerals, the sludge curator reviews P/Ce, and
the root reviews sludge. The shared inspect/save workflow captures final record
hashes, working-tree provenance and this trusted main base.

All six independent observations returned `pass_with_limitations`, with zero
actionable findings. Each final history-attached record hash matches its review.
No corrective record edits or successor dispositions were needed. Source gaps
remain explicit limitations, without a claim that new experiments were performed.

| Record | Immutable scientific review pair |
|---|---|
| Antimony | [YAML](../../reviews/structured/20261011T050326Z-antimony-round4-science/review.yaml), [Markdown](../../reviews/structured/20261011T050326Z-antimony-round4-science/review.md) |
| Phosphorus | [YAML](../../reviews/structured/20261011T050034Z-phosphorus-round4-independent/review.yaml), [Markdown](../../reviews/structured/20261011T050034Z-phosphorus-round4-independent/review.md) |
| Cerium | [YAML](../../reviews/structured/20261011T050034Z-cerium-round4-independent/review.yaml), [Markdown](../../reviews/structured/20261011T050034Z-cerium-round4-independent/review.md) |
| Chalcopyrite | [YAML](../../reviews/structured/20261011T050418Z-chalcopyrite-round4-independent/review.yaml), [Markdown](../../reviews/structured/20261011T050418Z-chalcopyrite-round4-independent/review.md) |
| Sphalerite | [YAML](../../reviews/structured/20261011T050418Z-sphalerite-round4-independent/review.yaml), [Markdown](../../reviews/structured/20261011T050418Z-sphalerite-round4-independent/review.md) |
| GaAs-production sludge | [YAML](../../reviews/structured/20261011T050103Z-gaas-sludge-round4-independent/review.yaml), [Markdown](../../reviews/structured/20261011T050103Z-gaas-sludge-round4-independent/review.md) |

## Completed local checks

- Baseline `just check`:307 passed, 3 skipped in 62.61s;21 records / 30 histories valid.
- Final scientific batch `just check`:307 passed, 3 skipped in 47.17s;
  27 records / 36 histories valid, exit 0.
- `cmmmech validate --require-records`:27 checked, 0 failed.
- `cmmmech validate-history --base c081a749cd63feafcc25414f5ad006d1f78f1e36`:
  36 checked, 0 errors.
- `bash scripts/check_vendored_sync.sh`: 22 governed artifacts match
  `a5d562962c75a2ad9efd8160b548df5944315422`.
- Each new record passed named-file validation. `just review-check --base
  c081a749cd63feafcc25414f5ad006d1f78f1e36 --require-reviews` passed:
  31 valid review bundles. Manual exact-hash coverage passed for all six new
  records. Squash and post-deletion checks remain publication gates recorded
  in the final PR receipt rather than preclaimed here.

Raw articles, figures and supplements remain outside Git. Dossier receipts
preserve actual attempts, dates, hashes, rechecks and source-specific terms.
The newly recovered sludge supplement adds explicit counterevidence; it does
not rewrite earlier Ga/As reviews' access history. A curator access failure
and a later reviewer's successful independent acquisition are separate facts.

## Integration and durable review provenance

Live checks on 2026-10-11 confirm CLAW admission PR #581 merged at
`849f336e025510316a5f235eb0af8547b8bd50cc`, 22 governed artifacts installed,
and active main ruleset 24692449 with SQUASH/ALLGREEN native queue and required
`validate-strict`. The PR shepherd is active as a manual, comment-only workflow;
the workflow-runs API returned zero runs. No model run or general autonomous
fleet capability is claimed. This batch changes no integration configuration.
Future integration must use CLAW's supported admission/synchronization process.

All six new review bases are the trusted main revision above. The previously
published annotated tag `review-base/cmm-source-survey-20261009` remains intact:
tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Every distinct review base must be
available through main ancestry or a retained exact tag before queue admission.
The final receipt records the isolated squash-shaped check, actual queue/merge
CI, branch deletion and fresh remote-main validation with explicit tag fetch.

## Remaining work

The [frontier snapshot](round4-frontier-20261011.md) records 27 roots and 73
unrepresented historical proposals: 43 elements and 30 overlapping commodity
proposals. This is not 73 automatic imports. Next priorities are iron,
germanium and individual-REE evidence; Suyamud 2020 phosphorus/magnesium
follow-up; commodity/resource concept decisions; and element-specific BES
antimony provenance gaps. This batch advances coverage without claiming
that no additional CMMs or mechanisms can be found.
