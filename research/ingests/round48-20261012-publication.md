# Round 48 scientific review and publication report

Add zircon, rutile, stannite, kësterite and tennantite-(In) as distinct mineral owners with source-qualified evidence. The corpus grows from 231 to 236 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round48-20261012`; branch: `curate/cmm-expansion-round48-20261012`; trusted base: `9b397b1f215381208c3381b175b3da8b6fe31399`. Generated at 2026-10-12T06:12:25.671148+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [zircon](../../data/records/zircon.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T060755Z-zircon-round48-independent/review.md) / [YAML](../../reviews/structured/20261012T060755Z-zircon-round48-independent/review.yaml) |
| [rutile](../../data/records/rutile.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T060755Z-rutile-round48-independent/review.md) / [YAML](../../reviews/structured/20261012T060755Z-rutile-round48-independent/review.yaml) |
| [stannite](../../data/records/stannite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T060910Z-stannite-round48-independent/review.md) / [YAML](../../reviews/structured/20261012T060910Z-stannite-round48-independent/review.yaml) |
| [kesterite](../../data/records/kesterite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T060910Z-kesterite-round48-independent/review.md) / [YAML](../../reviews/structured/20261012T060910Z-kesterite-round48-independent/review.yaml) |
| [tennantite-in](../../data/records/tennantite-in.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T060620Z-tennantite-in-round48-independent/review.md) / [YAML](../../reviews/structured/20261012T060620Z-tennantite-in-round48-independent/review.yaml) |

All 5 independent final scientific reviews match the current record bytes. The [manifest](round48-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Zircon and tennantite-(In) receive identity and natural-specimen context without microbial or inherited criticality claims. Rutile supports a narrowly scoped mineral-assisted microbial iron-cycling assay, not titanium recovery. Stannite and kësterite retain natural/synthetic phase boundaries, historical assay inconsistencies and control limits. Relative composition, solution release and inferred mineral formation are not converted into recovered-product yields or industrial deployment.

## Findings and corrections

Five independent final scientific reviews cover the exact current record bytes. No unresolved corrective finding remains in their assessed scope.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. The bounded acquisition objective in #151 is addressed by complete alternative originals and reviewed stannite/kësterite curation. Other acquisition issues remain open; see the [frontier](round48-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round47-postmerge-20261012-published-terminal.json`, SHA-256 `f9e7eddeb201e51f1d4b75e21a37818425ba09bb29af28397bd3fab1e18a4250`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `41150421ddd753d0cecf6d7a22bebd5a34d52f11b309beb820523a57d1624039`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `ed2bc5cf4c32744127edd92734e33277402fc4a6990da56ff6c309c0c4e7673e`.
- `uv run --locked cmmmech validate-history --base 9b397b1f215381208c3381b175b3da8b6fe31399`: exit 0; log SHA-256 `885e537286de29f10eb43fd520a420768782950c80808f190df3c2dd01832122`.
- `just review-check --base 9b397b1f215381208c3381b175b3da8b6fe31399 --require-reviews`: exit 0; log SHA-256 `ab0492bf5fa395185f6e08e2e84a3e30bd3cc69e3e5f5647a2e2815e389d65d3`.

Final `just check`: 308 passed, 3 skipped in 175.55 seconds. The gates accept 236 records, 279 histories and 288 review bundles. Exact-hash coverage verifies 236/236 current scientific reviews and 49 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round48/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round48/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
