# Round 51 scientific review and publication report

Add elpidite mineral identity and two distinct primary resources: ion-adsorption rare-earth clay and mixed monazite ore. The corpus grows from 246 to 249 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round51-20261012`; branch: `curate/cmm-expansion-round51-20261012`; trusted base: `466cb14cbc271ba73ba05e89ed188cfd113d06ea`. Generated at 2026-10-12T08:49:30.578668+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [elpidite](../../data/records/elpidite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T084041Z-elpidite-round51-science/review.md) / [YAML](../../reviews/structured/20261012T084041Z-elpidite-round51-science/review.yaml) |
| [ion-adsorption-rare-earth-clay](../../data/records/ion-adsorption-rare-earth-clay.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T083950Z-ion-adsorption-rare-earth-clay-round51-resolution/review.md) / [YAML](../../reviews/structured/20261012T083950Z-ion-adsorption-rare-earth-clay-round51-resolution/review.yaml) |
| [monazite-ore](../../data/records/monazite-ore.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T084632Z-monazite-ore-round51-resolution/review.md) / [YAML](../../reviews/structured/20261012T084632Z-monazite-ore-round51-resolution/review.yaml) |

All 3 independent final scientific reviews match the current record bytes. The [manifest](round51-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

The clay record preserves nonsterile controls, genus-only assignments and chemical salt comparators that generally outperform microbial treatments. The monazite-ore record supports biofilm colonization and qualitative surface alteration without importing prior-study dissolution yields. Elpidite is a source-qualified natural occurrence, with unavailable supplementary evidence and source inconsistencies explicit. No record inherits constituent criticality or asserts industrial deployment.

## Findings and corrections

Three independent final scientific reviews cover the exact record bytes. Review issues #160 and #161 correct a clay-dossier Table4 inspection error and a monazite-ore figure locator, preserving initial observations and exact successor lineage. The clay record/history remain unchanged; the monazite correction has an actual EDIT history. No unresolved corrective finding remains in their assessed scope. Review issues: [#160](https://github.com/CultureBotAI/CMMMech/issues/160), [#161](https://github.com/CultureBotAI/CMMMech/issues/161).

- `CMMMech.ion-adsorption-rare-earth-clay.dossier-table4-eh`: resolved in the final review, retaining [the preceding observation](../../reviews/structured/20261012T083701Z-ion-adsorption-rare-earth-clay-round51-initial/review.md) and exact predecessor `F1`.
- `CMMMech.monazite-ore.s12-evidence-locator`: resolved in the final review, retaining [the preceding observation](../../reviews/structured/20261012T084101Z-monazite-ore-round51-initial/review.md) and exact predecessor `F1`.

Scientific source limitations remain documented. For issue #153, the corrected public Bansal2007 author-PDF route exposes complete text, but original Figures1/4 still lack inspectable pixels and Hedrich2023 remains incomplete. The issue stays open. Acquisition issues remain open; see the [frontier](round51-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round50-postmerge-20261012-published-terminal.json`, SHA-256 `7bdde370bba43d304d38dc6818b7f03fd357e93e3afa93335905f49eb99519fa`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `c0cbef14272165bf6ffb5adc08754dd2d1aa0015bffbec643877011f82c1985f`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `06b051452e7949992afa10ca6afb43fcde683c0e3fcbd9ec1827b3fc360a702b`.
- `uv run --locked cmmmech validate-history --base 466cb14cbc271ba73ba05e89ed188cfd113d06ea`: exit 0; log SHA-256 `df80503fb8ec25b085cb361d093a451884dbfcffc44e709429ab4ad637720717`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 466cb14cbc271ba73ba05e89ed188cfd113d06ea --require-reviews`: exit 0; log SHA-256 `652073a437d8e21a75badd8c07255199d6d9f864da5c399e5ba1627e70317a24`.

Final `just check`: 317 passed, 3 skipped in 148.96 seconds. The gates accept 249 records, 295 histories and 305 review bundles. Exact-hash coverage verifies 249/249 current scientific reviews and 52 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round51/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round51/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
