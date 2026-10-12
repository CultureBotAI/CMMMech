# Round 54 scientific review and publication report

Add three distinct material owners: a mixed tennantite concentrate, catapleiite mineral identity, and laboratory-prepared rare-earth clay leach residue. The corpus grows from 256 to 259 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round54-20261012`; branch: `curate/cmm-expansion-round54-20261012`; trusted base: `5c83f27fa4d916a8432894e07031c2b5c7451a09`. Generated at 2026-10-12T10:52:08.747454+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [tennantite-concentrate](../../data/records/tennantite-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T104846Z-tennantite-concentrate-round54-science/review.md) / [YAML](../../reviews/structured/20261012T104846Z-tennantite-concentrate-round54-science/review.yaml) |
| [catapleiite](../../data/records/catapleiite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T104910Z-catapleiite-round54-science/review.md) / [YAML](../../reviews/structured/20261012T104910Z-catapleiite-round54-science/review.yaml) |
| [ion-adsorption-rare-earth-leach-residue](../../data/records/ion-adsorption-rare-earth-leach-residue.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T104845Z-ion-adsorption-rare-earth-leach-residue-round54-science/review.md) / [YAML](../../reviews/structured/20261012T104845Z-ion-adsorption-rare-earth-leach-residue-round54-science/review.yaml) |

All 3 independent final scientific reviews match the current record bytes. The [manifest](round54-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Tennantite concentrate records linked acidophile flask/reactor assays, with nonmonotonic carbon effects, evolving cultures, missing abiotic controls and no isolated product yield. Catapleiite retains its natural mineral identity; silver exchange in a heat-transformed derivative is not attributed to unheated mineral. The rare-earth residue is chemically prepared from natural clay before fungal/metabolite assays; source percentage, control and phase-assignment limits remain explicit.

## Findings and corrections

Independent review identified an unsupported tennantite redox-source discrepancy (issue #167). The assertion was removed with an EDIT and explicit source correction while preserving the original investigation and initial review. The final independent successor resolves that exact finding; all three final scientific reviews match the accepted record bytes. Review issues: [#167](https://github.com/CultureBotAI/CMMMech/issues/167).

- `CMMMech.tennantite-concentrate.early-redox-source-fidelity`: resolved in the final review, retaining [the preceding observation](../../reviews/structured/20261012T104025Z-tennantite-concentrate-round54-initial/review.md) and exact predecessor `F1`.

Scientific source limitations remain documented. The Gluconobacter genome-scale screen is already represented in the unchanged neodymium record. Fresh source reassessment and matching prior scientific review support a no-change disposition, with no duplicate record or artificial history event. No existing source-acquisition issue is closed by this batch. Acquisition issues remain open; see the [frontier](round54-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round53-postmerge-20261012-published-terminal.json`, SHA-256 `b0517a4886bd92d448224d63e0085ee73b54603268a57e28fb929b6cbb9fa208`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `7df7af409fc0dcbe038e79ee6eb827d01eac21459322f279c36bcebbbf242b32`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `d6352ce5892e0da95df27d121ac84e0c387cc23d5583acbeafce8944f357bb6c`.
- `uv run --locked cmmmech validate-history --base 5c83f27fa4d916a8432894e07031c2b5c7451a09`: exit 0; log SHA-256 `b3a780aa618d78baed0dce1308db129dd8cfc00e4f9fabbcc2081e9d44ebdc32`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 5c83f27fa4d916a8432894e07031c2b5c7451a09 --require-reviews`: exit 0; log SHA-256 `2458229dc3f9783d0b97446d44cedfc31a957e6cd9888bd885b52a565e80b1fa`.

Final `just check`: 317 passed, 3 skipped in 167.50 seconds. The gates accept 259 records, 307 histories and 317 review bundles. Exact-hash coverage verifies 259/259 current scientific reviews and 55 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round54/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round54/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
