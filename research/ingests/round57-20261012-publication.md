# Round 57 scientific review and publication report

Add three material owners: electroplating sludge, copper autoclave slime and coffinite. The corpus grows from 264 to 267 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round57-20261012`; branch: `curate/cmm-expansion-round57-20261012`; trusted base: `76509ff65c70edb5f212b6b4217febe5493bb0f3`. Generated at 2026-10-12T12:50:04.475439+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [electroplating-sludge](../../data/records/electroplating-sludge.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T124301Z-electroplating-sludge-round57-independent/review.md) / [YAML](../../reviews/structured/20261012T124301Z-electroplating-sludge-round57-independent/review.yaml) |
| [copper-autoclave-slime](../../data/records/copper-autoclave-slime.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T124735Z-copper-autoclave-slime-round57-science/review.md) / [YAML](../../reviews/structured/20261012T124735Z-copper-autoclave-slime-round57-science/review.yaml) |
| [coffinite](../../data/records/coffinite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T124723Z-coffinite-round57-science/review.md) / [YAML](../../reviews/structured/20261012T124723Z-coffinite-round57-science/review.yaml) |

All 3 independent final scientific reviews match the current record bytes. The [manifest](round57-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Electroplating sludge separates a living sulfur-culture assay from leaching with centrifuged biogenic ferric acidic liquor; mismatched controls and source calculation, model and toxicity conflicts remain explicit. Copper autoclave slime is a processed refinery residue, distinct from raw anode slime; Raman and headspace evidence support laboratory EPR3-associated transformation, while sterile dissolution is not reported as biological yield. Coffinite separates dated mineral identity and natural occurrence from abiotic formation on a prepared UO2 pellet; added dissolved uranium, missing parallel controls and source inconsistencies limit the proposed pathway.

## Findings and corrections

Independent scientific reviews of the three final record states found no corrective record defect. The qualified records retain scientific source limitations; unresolved acquisition and source-reconciliation work is tracked separately.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. The complete Hu2026 enargite study was assessed and deferred because feed ownership, durations, dose/figure values and the proposed two-stage assay remain unresolved; issue #175 tracks reconciliation without creating a record or artificial history. Issue #176 tracks acquisition of the complete Yang2021 microbial uranium-mineral study; the separate abiotic coffinite record does not resolve it. No existing source issue is closed by this batch. Acquisition issues remain open; see the [frontier](round57-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round56-postmerge-20261012-published-terminal.json`, SHA-256 `591b8fb6af309cf7b06de6e88f9f66bc875f3f38033476abb50c39167dbb06e0`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `c834f7cf79d44ea33b137dc964f0ba2bf097be9da9012707e6700f27955890f3`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `a2c77b50859d82147390c1a4e162a9806cf956719c56572f0a8ed5deed0da631`.
- `uv run --locked cmmmech validate-history --base 76509ff65c70edb5f212b6b4217febe5493bb0f3`: exit 0; log SHA-256 `83779df572a6de796147bf4f4188908481faa73b4865621d3461eb0c11e374e0`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 76509ff65c70edb5f212b6b4217febe5493bb0f3 --require-reviews`: exit 0; log SHA-256 `ee73a29807630b061a647b21543fc57b2263eb72750303ede5958e8317d33a71`.

Final `just check`: 317 passed, 3 skipped in 148.81 seconds. The gates accept 267 records, 315 histories and 325 review bundles. Exact-hash coverage verifies 267/267 current scientific reviews and 58 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round57/preservation-prepublication.json) verifies 6,416 hidden/ignored nontracked source-clone entries plus Git state. The Documents checkout and its linked unrelated worktree were inaccessible (EPERM) during this batch and were not modified by this batch; no current hash-preservation claim is made for those unavailable paths. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round57/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
