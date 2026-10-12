# Round 46 scientific review and publication report

Add alburnite, zincobriartite, roquesite, laforêtite and cassiterite as distinct mineral owners. The corpus grows from 224 to 229 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round46-20261012`; branch: `curate/cmm-expansion-round46-20261012`; trusted base: `94d743a1b8bb3fe595f96e88f4cdb54a4ee72375`. Generated at 2026-10-12T04:57:03.838177+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [alburnite](../../data/records/alburnite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T045348Z-alburnite-round46-final-context/review.md) / [YAML](../../reviews/structured/20261012T045348Z-alburnite-round46-final-context/review.yaml) |
| [zincobriartite](../../data/records/zincobriartite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T045359Z-zincobriartite-round46-final-context/review.md) / [YAML](../../reviews/structured/20261012T045359Z-zincobriartite-round46-final-context/review.yaml) |
| [roquesite](../../data/records/roquesite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T044806Z-roquesite-round46-independent/review.md) / [YAML](../../reviews/structured/20261012T044806Z-roquesite-round46-independent/review.yaml) |
| [laforetite](../../data/records/laforetite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T044924Z-laforetite-round46-independent/review.md) / [YAML](../../reviews/structured/20261012T044924Z-laforetite-round46-independent/review.yaml) |
| [cassiterite](../../data/records/cassiterite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T044820Z-cassiterite-round46-independent/review.md) / [YAML](../../reviews/structured/20261012T044820Z-cassiterite-round46-independent/review.yaml) |

All 5 independent final scientific reviews match the current record bytes. The [manifest](round46-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Alburnite and zincobriartite have narrow identity support from original IMA announcements and dated current authority. The inaccessible 2014 alburnite description, disputed 2016 occurrence and April 2026 notice that zincobriartite lacks a full published description remain explicit. Roquesite and laforêtite are grounded in original natural-specimen characterization, with synthetic comparators, analytical limits and page-range conflicts kept separate. Cassiterite adds laboratory separation using cultivated, subsequently sterilized Rhodococcus opacus biomass. The approximately 64.5% source endpoint describes mineral flotation, not isolated tin recovery; contradictory pH, conditioning times and cell-count equivalents, unequal assay fractions and missing zero-biomass flotation/gangue-selectivity results remain qualified. No constituent-derived criticality or industrial deployment is inferred.

## Findings and corrections

Five independent final scientific reviews cover the current records. Issue #149 tracks six trailing dossier spaces and incomplete context capture in the first attempted successors. Both were corrected: the final Ge scientific reviews explicitly capture eight target/context inputs each. The initial finding, intermediate observations and exact predecessor links remain preserved; the independent disposition confirms resolution. Review issues: [#149](https://github.com/CultureBotAI/CMMMech/issues/149).

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Existing acquisition issues remain open; see the [frontier](round46-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round45-postmerge-20261012-published-terminal.json`, SHA-256 `c16f7eda1e58dcec125bb51e74ada103f2a1afb40a46901dd693b41212c05723`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `8caead3980a6da1e7b4d54ea4895572c931741b48ccd353e542e8edf2b876b53`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `ff7ed8bc3fc67548605ba5d958c3f8057489701d8221b508c7670b58955b7dba`.
- `uv run --locked cmmmech validate-history --base 94d743a1b8bb3fe595f96e88f4cdb54a4ee72375`: exit 0; log SHA-256 `17691e066e03358c6eabe98608db086af9b35dcc46fde40810e46ead5f061163`.
- `just review-check --base 94d743a1b8bb3fe595f96e88f4cdb54a4ee72375 --require-reviews`: exit 0; log SHA-256 `0727adec4a796db0e64bd29f4d7bd066e0c78eba3e5ee44dc2e6bf04b01584f1`.

Final `just check`: 308 passed, 3 skipped in 236.91 seconds. The gates accept 229 records, 272 histories and 281 review bundles. Exact-hash coverage verifies 229/229 current scientific reviews and 47 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round46/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round46/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
