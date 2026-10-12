# Round 55 scientific review and publication report

Add two distinct mixed primary-resource owners: tetrahedrite concentrate and enargite-pyrite concentrate. The corpus grows from 259 to 261 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round55-20261012`; branch: `curate/cmm-expansion-round55-20261012`; trusted base: `19d0972767b266f86a256a3f36f0f7177ab4cf25`. Generated at 2026-10-12T11:24:05.880857+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [tetrahedrite-concentrate](../../data/records/tetrahedrite-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T112153Z-tetrahedrite-concentrate-round55-science/review.md) / [YAML](../../reviews/structured/20261012T112153Z-tetrahedrite-concentrate-round55-science/review.yaml) |
| [enargite-pyrite-concentrate](../../data/records/enargite-pyrite-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T112042Z-enargite-pyrite-concentrate-round55-independent/review.md) / [YAML](../../reviews/structured/20261012T112042Z-enargite-pyrite-concentrate-round55-independent/review.yaml) |

All 2 independent final scientific reviews match the current record bytes. The [manifest](round55-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Tetrahedrite concentrate separates two acidophile culture assays and abiotic controls while retaining inconsistent source units, feed composition and pretreatment limitations. Enargite-pyrite concentrate preserves three feed arms, variable carbon effects, nonsterile no-added-inoculum controls and conflicts in arsenic values and phase assignments. Neither record presents dissolved metal as an isolated product or laboratory assays as industrial deployment.

## Findings and corrections

Independent scientific reviews of both final record states found no corrective record defect. Both retain source inconsistencies and explicit control, identity and recovery limits. Source-acquisition issue #169 remains open.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Complete official supplements were acquired for Han2026 and Zhao2025, but their main methods and graphics remain unavailable through bounded legitimate routes. The paired clay-recovery dossier supports a source-only deferral, with no artificial record/history event. Issue #169 tracks Han2026 evidence acquisition; no existing source-acquisition issue is closed by this batch. Acquisition issues remain open; see the [frontier](round55-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round54-postmerge-20261012-published-terminal.json`, SHA-256 `8cafacdda0298bdd18138952313b62f0ea1366e8261a4cca69946c867343e6c9`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `368378eebc1e33c512b77ad50f461150276ae68c35cadd33086bb5a1002bb85c`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `07ecaf0aaf13688ac91b566cb887c9df5a85979d24fbddaffe83d88993bbd4ea`.
- `uv run --locked cmmmech validate-history --base 19d0972767b266f86a256a3f36f0f7177ab4cf25`: exit 0; log SHA-256 `c1801812798f7ab93a42704bf8ace6b2575514ffa80d5cb52c52945780c9ff22`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 19d0972767b266f86a256a3f36f0f7177ab4cf25 --require-reviews`: exit 0; log SHA-256 `609696f144095e2ed38214eb0fd3cc16f61bbf80b7c499eff5470f873829e900`.

Final `just check`: 317 passed, 3 skipped in 129.24 seconds. The gates accept 261 records, 309 histories and 319 review bundles. Exact-hash coverage verifies 261/261 current scientific reviews and 56 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round55/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round55/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
