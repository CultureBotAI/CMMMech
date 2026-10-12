# Round 44 scientific review and publication report

Add tungsten-nickel-iron alloy scrap; extend coal-beneficiation-waste and lithium-mica-ore with complete primary studies. The corpus grows from 220 to 221 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round44-20261012`; branch: `curate/cmm-expansion-round44-20261012`; trusted base: `3fc8b873487ed2c1c253ecf131d99e09b8b8d452`. Generated at 2026-10-12T03:30:23.750373+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [coal-beneficiation-waste](../../data/records/coal-beneficiation-waste.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T032709Z-coal-beneficiation-waste-round44-independent/review.md) / [YAML](../../reviews/structured/20261012T032709Z-coal-beneficiation-waste-round44-independent/review.yaml) |
| [lithium-mica-ore](../../data/records/lithium-mica-ore.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T032611Z-lithium-mica-ore-round44-independent/review.md) / [YAML](../../reviews/structured/20261012T032611Z-lithium-mica-ore-round44-independent/review.yaml) |
| [tungsten-nickel-iron-alloy-scrap](../../data/records/tungsten-nickel-iron-alloy-scrap.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T032729Z-tungsten-nickel-iron-alloy-scrap-round44-independent/review.md) / [YAML](../../reviews/structured/20261012T032729Z-tungsten-nickel-iron-alloy-scrap-round44-independent/review.yaml) |

All three independent final scientific reviews match the current record bytes. The [manifest](round44-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

The tungsten source separates W-Ni-Fe scrap from VK8 carbide and describes chemical/mechanical powder separation. It does not isolate a microbial contribution. Its unverified purity assertion and preparation-dependent pressed-surface size distributions are qualified rather than converted into a recovery yield.

The coal2017 source reports a medium experiment on the same feed family and cites earlier work. It is not treated as independent replication. Conflicting optimum recipes and outcomes, source units and absent matched sterile comparisons remain explicit.

The lithium2025 study is newly accessible in full, including original figures and supplement. Its mixed mica-bearing feed remains a resource, and distinct analytical fractions and culture experiments retain their source-specific scope. The earlier 2020 evidence remains separate.

## Findings and corrections

Three independent scientific reviews found no corrective defects; source limitations remain explicit.

No unresolved corrective finding remains in the three final scientific reviews.

Scientific source limitations remain documented. Existing acquisition issues remain open; see the [frontier](round44-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round43-postmerge-20261012-published-terminal.json`, SHA-256 `e8c2431292134376a236be913fcaaca4b367d3c7081bd4a7bab4872b37ab0e0d`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `5f59ca3fdfeeaf69482b376be1ca76969d6ca9c590f2ffa6dc64413352d66f1e`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `f6534d690f943b3b0f1b5f133045ff0dae9f1200c399c6268ea9a337dec8ad7e`.
- `uv run --locked cmmmech validate-history --base 3fc8b873487ed2c1c253ecf131d99e09b8b8d452`: exit 0; log SHA-256 `8082c1c88ab5757f95d231f20c299d9f4e92312cccd4c71e5ba5ca72aaae63fd`.
- `just review-check --base 3fc8b873487ed2c1c253ecf131d99e09b8b8d452 --require-reviews`: exit 0; log SHA-256 `da84d4db12e68330bfd7cbe2057fcc9026638108e206bbde33730be1af70990c`.

Final `just check`: 308 passed, 3 skipped in 158.12 seconds. The gates accept 221 records, 262 histories and 266 review bundles. Exact-hash coverage verifies 221/221 current scientific reviews and 45 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round44/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round44/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
