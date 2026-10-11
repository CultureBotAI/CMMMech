# Round21 reviewed secondary and marine resources

Worktree: `/private/tmp/CMMMech-expansion-round21-20261011`.
Branch: `curate/cmm-expansion-round21-20261011`.
Trusted base: `55fd1947e80f67ec91dfe63e7bf15f72d822cefb`.
Acceptance: [issue 77](https://github.com/CultureBotAI/CMMMech/issues/77).

Three additions bring the corpus to **152 records**. Waste printed circuit boards are a secondary resource with two separately scoped laboratory bioleaching studies. Cobalt-rich ferromanganese crusts and rare-earth-rich deep-sea mud are natural primary resources with verified identity evidence and no accepted microbial mechanism. Neither feed inherits the criticality of its constituents. No industrial deployment or isolated-product recovery is inferred.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Cobalt-rich ferromanganese crusts](../../data/records/cobalt-rich-ferromanganese-crusts.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T124733Z-cobalt-rich-ferromanganese-crusts-round21-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T124733Z-cobalt-rich-ferromanganese-crusts-round21-independent/review.md) |
| [Rare-earth-rich deep-sea mud](../../data/records/rare-earth-rich-deep-sea-mud.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T124626Z-rare-earth-rich-deep-sea-mud-round21-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T124626Z-rare-earth-rich-deep-sea-mud-round21-independent/review.md) |
| [Waste printed circuit boards](../../data/records/waste-printed-circuit-boards.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction/review.yaml) · [Markdown](../../reviews/structured/20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction/review.md) |

Every final record has an actual CREATE sidecar, a distinct inline event and a completed independent scientific review matching its current bytes. The [manifest](round21-frontier-20261011.json) lists exact hashes, history and review paths. Review findings and explicit source limitations are retained in the linked observations; structural checks do not establish scientific truth.

The initial PCB review is preserved alongside a successor correcting an overstatement of which figures had been visually inspected at the first save. [Issue 78](https://github.com/CultureBotAI/CMMMech/issues/78) tracks this review-provenance correction; the later inspection does not retroactively change the original coverage. Both artifacts remain available. No scientific record or CREATE history changed for this correction.

The board evidence retains unequal controls, source figure/text discrepancies, dissolved-metal denominators and reagent additions. Community descriptions do not identify causal strains. Crust and mud identities remain distinct from nodules, host mineral grains, constituent elements and processed products. Mechanistic leads remain in research until complete assay review supports them.

## Evidence and remaining work

The [prioritized frontier](round21-frontier-20261011.md) links the paired source dossiers and a nodule-lead reassessment. A commercial manganese-oxide assay is not imported into the natural-nodule record. Raw primary articles and supplements remain outside Git. No schema, validator or skill change was necessary, and no source exhaustion is claimed.

## Validation and preservation

Baseline: 308 tests passed, 3 skipped in 101.41 seconds; 149 records and 166 histories.
Final `just check`: **308 passed, 3 skipped in 132.48s (0:02:12)**. All **152 records and 169 history sessions** validate. Separate nonempty-corpus and trusted-base history checks passed. Structured review validation passed for **169 pairs**. All 152 current records have independent scientific reviews matching their exact hashes.

All **958 prior tracked scientific files** under data, history, reviews and research remain unchanged. All **22 distinct review bases** resolve. The annotated source-survey provenance tag is preserved; all new reviews use the already merged trusted base. The 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`.

Live ruleset 24692449 remains active with SQUASH/ALLGREEN queue, required validate-strict from App 15368 and no bypass actors. Fleet admission and shared history are installed; PR shepherd remains manual/comment-only as documented. This batch changes no governance. Future fleet changes must use CLAW's supported admission and synchronization process.

An independent publication audit, exact-tree squash-shaped checkout and required PR checks precede native queue admission. Actual merge state and tree identity must be verified before deleting only the merged topic branch. Fresh remote-main checks then verify the complete corpus and durable review bases. Original main advances only after collision/symlink checks and matching ignored/untracked snapshots. These publication steps are pending at this report's preparation; their terminal evidence belongs on the PR.
