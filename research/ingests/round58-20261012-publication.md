# Round 58 scientific review and publication report

Add three distinct material owners: smithsonite, mixed spent alkaline/zinc-carbon batteries and spent selective catalytic reduction catalysts. The corpus grows from 267 to 270 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round58-20261012`; branch: `curate/cmm-expansion-round58-20261012`; trusted base: `b6014c43b8174904e80f71df22be2251a802b418`. Generated at 2026-10-12T13:36:19.734893+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [smithsonite](../../data/records/smithsonite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T133315Z-smithsonite-round58-science/review.md) / [YAML](../../reviews/structured/20261012T133315Z-smithsonite-round58-science/review.yaml) |
| [spent-alkaline-zinc-carbon-batteries](../../data/records/spent-alkaline-zinc-carbon-batteries.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T133243Z-spent-alkaline-zinc-carbon-batteries-round58-science/review.md) / [YAML](../../reviews/structured/20261012T133243Z-spent-alkaline-zinc-carbon-batteries-round58-science/review.yaml) |
| [spent-selective-catalytic-reduction-catalyst](../../data/records/spent-selective-catalytic-reduction-catalyst.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T133310Z-spent-selective-catalytic-reduction-catalyst-round58-independent/review.md) / [YAML](../../reviews/structured/20261012T133310Z-spent-selective-catalytic-reduction-catalyst-round58-independent/review.yaml) |

All 3 independent final scientific reviews match the current record bytes. The [manifest](round58-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Smithsonite phase evidence is confined to the traditional zinc/urea specimen dried at105 degrees C; sequential-addition zinc depletion is a separate arm without its own phase confirmation. The battery record separates microbial acid/polythionate production, mixed-feed leaching and abiotic electrolysis, preserving manganese extraction and manganese-oxide purity conflicts. The SCR record separates centrifuged microbial bioacid arsenic removal and combined regeneration from an independent chemical V/W leaching study; alkaline-comparator tradeoffs, unclear composition units, missing controls and conflicting120/240-minute duration remain explicit.

## Findings and corrections

Three independent scientific reviews assess the final record states; documented source limitations are retained. Final reviewed hashes and any corrective dispositions are verified in the manifest.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. A complete Kordloo2024 pickling-liquor main was acquired and compared with the2026 study. Missing supplementary evidence and unresolved experiment provenance keep the existing electroplating record unchanged. Earlier SCR microbial studies remain acquisition priorities. No existing source issue is closed by this batch. New source issues #178 and #179 track these concrete acquisition/reconciliation tasks; no source-only deferral is reported resolved. Acquisition issues remain open; see the [frontier](round58-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round57-postmerge-20261012-published-terminal.json`, SHA-256 `0e6f6474decc09603e2a734639bb595e69cf68e284f35fd0402922b8b18c5e4a`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `a4e3583b24f1ab0adb2763d33493af2992247c3da208acfda6f278981d32ea80`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `6e12075def4466323f11ee9b4e4efcef34a00ce9249d1dfdc03bfc0f8071b1df`.
- `uv run --locked cmmmech validate-history --base b6014c43b8174904e80f71df22be2251a802b418`: exit 0; log SHA-256 `41419c5d1c6c1a4a9f9ac7075b9e4d58403affb54c2da5e4ef28f51e90646065`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base b6014c43b8174904e80f71df22be2251a802b418 --require-reviews`: exit 0; log SHA-256 `6db97877480465710f9c06306bba1d76becbe878f67e7261839b5e52c80ecf5f`.

Final `just check`: 317 passed, 3 skipped in 138.82 seconds. The gates accept 270 records, 318 histories and 328 review bundles. Exact-hash coverage verifies 270/270 current scientific reviews and 59 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round58/preservation-prepublication.json) verifies the original Documents checkout's 7,187 nontracked/ignored entries and the unrelated skill worktree's 7,389 tracked and nontracked/ignored entries, including file modes and symlink targets. Their Git states are unchanged from initialization. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round58/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
