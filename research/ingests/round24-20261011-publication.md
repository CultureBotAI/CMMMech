# Round24 reviewed secondary-resource additions

Worktree: `/private/tmp/CMMMech-expansion-round24-20261011`.
Branch: `curate/cmm-expansion-round24-20261011`.
Trusted base: `d7183efeb2e528d6d88f0b69da41323642b8fa85`.
Acceptance: [issue 86](https://github.com/CultureBotAI/CMMMech/issues/86).

Four new records bring the corpus to **160 records**: spent sulfuric-acid-production catalyst, copper-smelter slag, coal-mine-drainage treatment solids and spent nickel-metal-hydride batteries. These are distinct secondary resources with source-scoped laboratory evidence. None inherits constituent criticality, and filtered-liquid mobilization is not described as an isolated product or industrial extraction process.

## Independent scientific reviews

| Change | Record | Kind | Final exact-state review |
|---|---|---|---|
| New | [Coal-mine-drainage treatment solids](../../data/records/coal-mine-drainage-treatment-solids.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T142727Z-coal-mine-drainage-treatment-solids-round24-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T142727Z-coal-mine-drainage-treatment-solids-round24-independent/review.md) |
| New | [Copper smelter slag](../../data/records/copper-smelter-slag.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T142755Z-copper-smelter-slag-round24-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T142755Z-copper-smelter-slag-round24-independent/review.md) |
| New | [Spent nickel-metal-hydride batteries](../../data/records/spent-nickel-metal-hydride-batteries.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T142958Z-spent-nickel-metal-hydride-batteries-round24-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T142958Z-spent-nickel-metal-hydride-batteries-round24-independent/review.md) |
| New | [Spent sulfuric-acid-production catalyst](../../data/records/spent-sulfuric-acid-production-catalyst.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T142924Z-spent-sulfuric-acid-production-catalyst-round24-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T142924Z-spent-sulfuric-acid-production-catalyst-round24-independent/review.md) |

All four records have actual CREATE sidecars, distinct inline events and independent scientific reviews matching final hashes. The [manifest](round24-frontier-20261011.json) lists both review formats and exact record/history paths. No actionable defect in the four frozen scientific records was identified; source limitations remain explicit and are not erased by passing validation.

[Issue 87](https://github.com/CultureBotAI/CMMMech/issues/87) tracks a verified citation defect in the prior discovery handoff. The round23 frontier gave the intended 2019 copper-slag paper the wrong DOI, `10.3390/min9110542`. The verified DOI is **10.3390/min9090542**. The new record and dossier use the correct citation, and the [successor frontier](round24-frontier-20261011.md) explicitly corrects the historical handoff without rewriting it.

A further minor publication finding, [issue 88](https://github.com/CultureBotAI/CMMMech/issues/88), concerned spacing in two sulfuric-catalyst source reports. The correction changes only whitespace; record/history bytes remain unchanged. The original scientific review is preserved. A [YAML successor](../../reviews/structured/20261011T143215Z-spent-sulfuric-acid-production-catalyst-round24-context-readability/review.yaml) and [generated Markdown](../../reviews/structured/20261011T143215Z-spent-sulfuric-acid-production-catalyst-round24-context-readability/review.md) attest the corrected context with `scientific_review: false`, explicitly without a fresh literature assessment.

## Evidence limits and next work

Sulfuric-acid catalyst evidence retains inconsistent pulp-loading and sieve labels, declining liquid V after its peak, high-loading controls that can outperform cultures, and residual vanadium and aluminium leachability. The companion residue study is not independent replication or a complete vanadium recovery balance.

Copper-slag evidence retains divergent source endpoints and highest-loading labels, unlike pH trajectories, undefined temperature/working volume and an inconsistent fold-change claim. Chemical-acid comparisons under different conditions do not establish universal microbial superiority.

Drainage treatment solids retain substantial site-specific sterile release and a below-control JR07 outcome, missing isolate/feed rows, unclear REE replication and analytical fraction, and an unresolved percentage-versus-inventory conflict. Lactate, biofilm and gene associations do not prove causal pathways.

NiMH evidence distinguishes Gluconobacter delayed/spent-medium successes from null one-step and Streptomyces treatments. Different media and culture histories limit causal comparison. Abstract/main yield and growth-timing inconsistencies remain explicit. Main figures/tables and supplementary native chart data were inspected; original Word rendering was unavailable and is not claimed.

The [prioritized next ingests](round24-frontier-20261011.md) include accessible cast-house dust evidence, heavy-fuel-oil ash, EAF steel slag and existing-record extensions. New resource leads remain: this batch is concrete progress, not literature or identity exhaustion. No schema, validator, skill or governed-artifact change was needed.

## Checks, governance and preservation

Baseline: 308 tests passed, 3 skipped in 121.35 seconds; 156 records and 177 histories. Final `just check`: **308 passed, 3 skipped in 89.10s (0:01:29)**. Separate `validate --require-records`, trusted-base history and structured-review checks passed: **160 records, 181 history sessions and 183 review pairs**. All 160 current records have independent scientific coverage matching current hashes.

All **1050 prior scientific files** under data/history/reviews/research are byte-identical. All 25 saved review bases resolve. New reviews use the merged trusted base; the annotated source-survey provenance tag remains unchanged.

The 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Live ruleset 24692449 is active with SQUASH/ALLGREEN, required validate-strict from App 15368 and no bypass actors. Fleet admission, shared history and governed artifacts are installed; the PR shepherd remains documented as manual/comment-only. This batch does not reconfigure fleet capabilities. Any future integration must use CLAW's supported admission and synchronization process.

At preparation of this report, independent publication audit, exact-tree squash-shaped verification, queue merge, branch cleanup and fresh remote-main validation are pending. Their terminal receipts belong on the PR. Original-main advancement requires clean-state, path/symlink collision and ignored/untracked preservation checks; unrelated worktrees remain intact.
