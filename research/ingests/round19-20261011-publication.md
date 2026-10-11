# Round19 reviewed resource records

Worktree: `/private/tmp/CMMMech-expansion-round19-20261011`.
Branch: `curate/cmm-expansion-round19-20261011`.
Trusted base: `c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a`.
Acceptance: [issue70](https://github.com/CultureBotAI/CMMMech/issues/70).
Scientific correction: [issue71](https://github.com/CultureBotAI/CMMMech/issues/71).
Publication formatting correction: [issue72](https://github.com/CultureBotAI/CMMMech/issues/72).

Seven additions bring the corpus to **145 records**: one natural manganese-ore primary resource and six processing-derived secondary resources. Six records carry scoped microbial evidence; the spent vegetable-oil catalyst establishes identity only because complete experimental evidence remains inaccessible. No inherited criticality, universal feed composition or industrial microbial deployment is asserted. Each addition has an actual CREATE sidecar and distinct inline event; manganese ore also has an EDIT correction session.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Automotive wastewater-treatment sludge](../../data/records/automotive-wastewater-treatment-sludge.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114655Z-automotive-wastewater-treatment-sludge-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114655Z-automotive-wastewater-treatment-sludge-round19-independent/review.md) |
| [Chrysotile asbestos tailings](../../data/records/chrysotile-asbestos-tailings.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114820Z-chrysotile-asbestos-tailings-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114820Z-chrysotile-asbestos-tailings-round19-independent/review.md) |
| [Copper flotation tailings](../../data/records/copper-flotation-tailings.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114827Z-copper-flotation-tailings-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114827Z-copper-flotation-tailings-round19-independent/review.md) |
| [Electrolytic manganese residue](../../data/records/electrolytic-manganese-residue.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114810Z-electrolytic-manganese-residue-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114810Z-electrolytic-manganese-residue-round19-independent/review.md) |
| [Iron-ore tailings](../../data/records/iron-ore-tailings.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114841Z-iron-ore-tailings-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114841Z-iron-ore-tailings-round19-independent/review.md) |
| [Manganese ore](../../data/records/manganese-ore.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T115158Z-manganese-ore-round19-resolution/review.yaml) · [Markdown](../../reviews/structured/20261011T115158Z-manganese-ore-round19-resolution/review.md) |
| [Spent vegetable-oil hydrogenation catalyst](../../data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T114655Z-spent-vegetable-oil-hydrogenation-catalyst-round19-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T114655Z-spent-vegetable-oil-hydrogenation-catalyst-round19-independent/review.md) |

Each reviewer is independent of the respective record's author. The [manifest](round19-frontier-20261011.json) records final hashes, history paths and reviews. Earlier observations remain immutable.

Adversarial review found that the manganese record repeated the primary paper's carbonate-absence prose without preserving conflicting rhodochrosite markers in Figure 11. Issue 71 tracks the correction. The initial needs_curation observation is retained, and the independent successor explicitly resolves that finding against the corrected final bytes. Neither confirmed carbonate detection nor confirmed absence is inferred from the conflicting source. Publication must wait for that successor and all affected checks.

The manganese and iron-tailings records describe linked stages of one study, not independent replications. Historical controls do not isolate a contemporaneous microbial effect. Roasted Mn3O4 oxide-equivalent analysis is not battery-grade MnO2 or directly measured daily product recovery. The residue record retains the J62/CJB1 accession conflict and unresolved mechanistic chemistry. Sludge experiments establish conditional solubilization, not isolated product. Copper-tailings treatment tests physical stabilization with active background controls. Asbestos-tailings evidence supports Mg leaching; modeled carbon benefits do not establish net sequestration or detoxification.

## Evidence and remaining work

- [Iron/manganese dossier](round19-iron-manganese-sources-20261011.md), [JSON](round19-iron-manganese-sources-20261011.json).
- [Residue dossier](round19-manganese-residue-sources-20261011.md), [JSON](round19-manganese-residue-sources-20261011.json).
- [Catalyst/sludge dossier](round19-hydrogenation-catalyst-sources-20261011.md), [JSON](round19-hydrogenation-catalyst-sources-20261011.json).
- [Tailings dossier](round19-tailings-sources-20261011.md), [JSON](round19-tailings-sources-20261011.json).
- [Prioritized next ingests and extensions](round19-frontier-20261011.md).

Timestamped source assessments preserve bounded hidden/ignored searches, actual acquisitions and access limits. Raw full texts remain outside Git. Mafic-tailings/nodule/mining-waste candidates, original comparator studies and missing full texts/supplements remain concrete follow-up work. This batch does not establish global source exhaustion.

## Validation and preservation

Baseline: 308 tests passed, 3 skipped in 97.97 seconds; 138 records and 154 histories.
Initial batch before carbonate correction:308 passed, 3 skipped in 122.38 seconds; 145 records and 161 histories.
Final corrected `just check`: **308 passed, 3 skipped in 109.70s (0:01:49)**.
All **145 records and 162 history sessions** validate. Separate nonempty corpus and trusted-base history validation passed. No schema or validator behavior changed.

Structured review validation passed for **161 pairs**. All 145 current records have independent scientific reviews matching their final bytes. All 879 prior tracked files under data, history, reviews and research remain unchanged. All 20 distinct review bases resolve; the annotated source-survey provenance tag remains unchanged. New reviews use the already merged trusted base.

All 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Live main ruleset 24692449 remains active SQUASH/ALLGREEN, requiring validate-strict from App 15368 with no bypass actors. Fleet admission and shared history are installed; PR shepherd remains manual/comment-only. Future integration must use CLAW's supported process. No governance or skill change belongs to this batch.

Independent publication audit, exact-tree squash verification and native queue checks precede merge. A fresh remote-main checkout after topic deletion must validate again. Original main advances only after collision/symlink checks and matching before/after ignored/untracked snapshots. Terminal evidence will be posted on the PR; unrelated worktrees and branches remain intact.
