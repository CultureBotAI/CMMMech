# Round 53 scientific review and publication report

Add three distinct material owners—chemically prepared allanite-derived leachate, beneficiated eudialyte concentrate and hafnon mineral identity—and extend the existing ion-adsorption rare-earth clay record with a separate primary study. The corpus grows from 253 to 256 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round53-20261012`; branch: `curate/cmm-expansion-round53-20261012`; trusted base: `b85c2c2c753fe83a2fc21f073ee1e49675ae647e`. Generated at 2026-10-12T10:10:33.536599+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [allanite-leachate](../../data/records/allanite-leachate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T100758Z-allanite-leachate-round53-independent/review.md) / [YAML](../../reviews/structured/20261012T100758Z-allanite-leachate-round53-independent/review.yaml) |
| [eudialyte-concentrate](../../data/records/eudialyte-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T100755Z-eudialyte-concentrate-round53-science/review.md) / [YAML](../../reviews/structured/20261012T100755Z-eudialyte-concentrate-round53-science/review.yaml) |
| [hafnon](../../data/records/hafnon.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T100714Z-hafnon-round53-science/review.md) / [YAML](../../reviews/structured/20261012T100714Z-hafnon-round53-science/review.yaml) |
| [ion-adsorption-rare-earth-clay](../../data/records/ion-adsorption-rare-earth-clay.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T100738Z-ion-adsorption-rare-earth-clay-round53-science/review.md) / [YAML](../../reviews/structured/20261012T100738Z-ion-adsorption-rare-earth-clay-round53-science/review.yaml) |

All 4 independent final scientific reviews match the current record bytes. The [manifest](round53-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Allanite-derived liquor receives centrifuged engineered-yeast supernatant after chemical preparation; solution depletion, impurity co-removal and source dose inconsistencies stay explicit. Eudialyte concentrate has documented beneficiation and chemical laboratory/pilot processing, without inferred microbial or industrial deployment. Hafnon is a dated mineral identity with a qualified source-reported natural occurrence and explicit reuse of older inaccessible microanalysis. The added clay study retains mismatched controls, stronger salt comparators and invalid printed extraction arithmetic.

## Findings and corrections

Four independent scientific reviews assess final record bytes; source discrepancies and experimental limitations remain explicit.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Issue #163 is addressed by the complete relevant primary/supplementary assessment and a reviewed processing-liquor record. Its closure denotes completed curation, not resolution of the source experimental limitations. The separate zircon source gap #153 remains open. New source follow-up #165 records Li2025 sequencing and extraction-calculation gaps without blocking the qualified qualitative extension. Acquisition issues remain open; see the [frontier](round53-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round52-postmerge-20261012-published-terminal.json`, SHA-256 `d918156b18fd4a3f90bd0a5441c76e6a343f304027e65e12a59ae2325d85d326`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `5dccf1da78b9111e8714e725ea5b540e319448ec511b2cd3cd161ed16ab3d5a5`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `f102e7162eedb9bf7d45e2a2fa9b011e7a3bf83fb2c341e1424889b9dd856f34`.
- `uv run --locked cmmmech validate-history --base b85c2c2c753fe83a2fc21f073ee1e49675ae647e`: exit 0; log SHA-256 `60b1330e0225bff7414e09d933725aee3784ed120b5151b881814e9a98ae731c`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base b85c2c2c753fe83a2fc21f073ee1e49675ae647e --require-reviews`: exit 0; log SHA-256 `0f668468e4b8a1a167cc995ad56f14960a3ed59fe1e48f93b3af376902233832`.

Final `just check`: 317 passed, 3 skipped in 137.72 seconds. The gates accept 256 records, 303 histories and 313 review bundles. Exact-hash coverage verifies 256/256 current scientific reviews and 54 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round53/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round53/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
