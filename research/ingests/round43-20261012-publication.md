# Round 43 scientific review and publication report

Added germanite, renierite, lithium-mica ore and coal beneficiation waste; extended the existing titanium-metal record with a qualified culture-containing grinding study. The corpus grows from 216 to 220 records. The two germanium-bearing mineral species have identity and geological context only. Mixed feeds remain distinct from elements, mineral species and commodities; no criticality or industrial deployment is inferred from a constituent or laboratory result.

Worktree: `/private/tmp/CMMMech-expansion-round43-20261012`; branch: `curate/cmm-expansion-round43-20261012`; trusted base: `59e24ec38d9c7b377dcfeade1637b298aab9623e`. Generated at 2026-10-12T02:54:32.859182+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [coal-beneficiation-waste](../../data/records/coal-beneficiation-waste.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T025133Z-coal-beneficiation-waste-round43-resolution/review.md) / [YAML](../../reviews/structured/20261012T025133Z-coal-beneficiation-waste-round43-resolution/review.yaml) |
| [germanite](../../data/records/germanite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T025122Z-germanite-round43-independent/review.md) / [YAML](../../reviews/structured/20261012T025122Z-germanite-round43-independent/review.yaml) |
| [lithium-mica-ore](../../data/records/lithium-mica-ore.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T025143Z-lithium-mica-ore-round43-independent/review.md) / [YAML](../../reviews/structured/20261012T025143Z-lithium-mica-ore-round43-independent/review.yaml) |
| [renierite](../../data/records/renierite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T025128Z-renierite-round43-independent/review.md) / [YAML](../../reviews/structured/20261012T025128Z-renierite-round43-independent/review.yaml) |
| [titanium-metal](../../data/records/titanium-metal.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T025118Z-titanium-metal-round43-resolution/review.md) / [YAML](../../reviews/structured/20261012T025118Z-titanium-metal-round43-resolution/review.yaml) |

All five completed independent reviews match the final record bytes. The [manifest](round43-frontier-20261012.json) retains exact record, history, review and dossier hashes. Four CREATE and three EDIT sidecars were added: the titanium extension and two correction sessions. Initial reviews remain immutable.

Germanite retains the Handbook/primary space-group disagreement rather than choosing unsupported agreement. Renierite retains composition variation and distinguishes ideal formulae, new microprobe data and prior literature. Neither inherits a criticality designation or a microbial mechanism from germanium.

The lithium study's complete original and supplementary figures support separate acidophile, fungal and yeast observations on a mixed Beauvoir feed. Li versus Li2O denominators, timing and agitation conflicts remain explicit. The fraction of extracted lithium associated with biomass is not a fraction of the entire feed. Rich-medium bacterial null results remain represented.

Coal-waste leaching evidence retains unresolved community identity, absent matched sterile controls, ambiguous endpoints, sulfur-formula/Eh-label conflicts and unreconciled percentages. The 2019 electrochemical report remains context only. Titanium's relative four-element composition excludes oxygen/hydrogen and cannot establish metallic purity or extraction yield; mixed oxides/hydride, pooled feed outcomes and absent matched controls remain explicit.

## Adversarial findings and corrections

[Issue #142](https://github.com/CultureBotAI/CMMMech/issues/142) restores the source's average-grain-size qualifier in the titanium record. [Issue #143](https://github.com/CultureBotAI/CMMMech/issues/143) corrects the coal record's Figure 2 assay scope and Kamskaya author spelling. All three confirmed minor findings are locally resolved with appended history and independent successors. The issues are intended to close through the future PR.

- `CMMMech.coal-beneficiation-waste.figure-assay-scope`: resolved by the linked final review, retaining [the initial finding](../../reviews/structured/20261012T024442Z-coal-beneficiation-waste-round43-initial/review.md) and exact predecessor `F1`.
- `CMMMech.coal-beneficiation-waste.author-transliteration`: resolved by the linked final review, retaining [the initial finding](../../reviews/structured/20261012T024442Z-coal-beneficiation-waste-round43-initial/review.md) and exact predecessor `F2`.
- `CMMMech.titanium-metal.average-grain-size`: resolved by the linked final review, retaining [the initial finding](../../reviews/structured/20261012T023745Z-titanium-metal-round43-initial/review.md) and exact predecessor `F1`.

No unresolved corrective finding remains in the five final scientific reviews. Evidence limitations remain scientific limits, not silently closed acquisition issues. Existing source issues #103, #104, #120, #129, #130, #133, #134, #137 and #140 remain open. The [frontier](round43-frontier-20261012.md) gives concrete next work; no source exhaustion is claimed.

## Validation and preservation

Baseline evidence reuses the freshly validated published base/tree: `/private/tmp/cmm-round42-postmerge-20261012-published-terminal.json`, SHA-256 `dd80cddd7bbf18f1f96a1b0cb2a96b7cf39e0bfe2939e5f294a7c2a01f97a323`. It was not rerun before curation. The first batch check passed before coal corrections; final checks were repeated after correction:

- `just check`: exit 0; log SHA-256 `3b461ec716372779d864a3273f66a8f5e36a3275912d2edc011da55513defab4`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `5f5111acf2e1d4f13998e3baccfe8b9a433c95528bd47cfbc3572bbbef706f99`.
- `uv run --locked cmmmech validate-history --base 59e24ec38d9c7b377dcfeade1637b298aab9623e`: exit 0; log SHA-256 `a7e1e37a7ef921c16b129f63f7319e52d3effcf1660ec0e77c1d93369e0f3063`.
- `just review-check --base 59e24ec38d9c7b377dcfeade1637b298aab9623e --require-reviews`: exit 0; log SHA-256 `13e04b9c6c41298f12c91b9da36c1526c59356acf6b9df69ede85f66b7cd34ac`.

Final `just check`: 308 passed, 3 skipped in 214.77 seconds; 220 valid records and 259 valid histories. Native review validation accepts 263 bundles. Independent exact-hash coverage finds current completed positive scientific reviews for all 220 records and 44 available review bases. Validation is distinct from scientific verification.

The [preservation receipt](../../reviews/publication/20261012-round43/preservation-prepublication.json) verifies 7,187 hidden/ignored main-checkout entries and eight bounded unrelated skill-worktree entries, plus their Git states. This is prepublication evidence; preservation is checked again after merge. Raw copyrighted originals remain outside Git, referenced through provenance manifests. No schema, validator, test, skill or governed artifact changed in this batch.

## Integration and publication

The [live status summary](../../reviews/publication/20261012-round43/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Effective main rules use native SQUASH/ALLGREEN queue admission, required validate-strict and no bypass actors. Workflow presence does not verify shepherd credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

The package and operational helper ports require [independent publication review](../../reviews/publication/20261012-round43). Commit, isolated squash-shaped validation, hosted review/CI, queue merge, branch deletion and fresh-main validation are subsequent guarded steps; this report does not claim they have happened. Actual publication results belong in the PR closeout. Historical provenance tags remain retained, and all current review bases must remain available after topic deletion.
