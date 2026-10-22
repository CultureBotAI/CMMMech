# Cycle 1 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `1` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff Timestamp**: `2026-10-22T05:48:39Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `ca26f50eb674fb9abbcc0cabfc1f27ec9da44d5259cb1af8196db23b6c94e341`
- **Frozen Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`

## 1. Frozen Task Intake & Dependency-Aware Issue Grouping

The supervisor-frozen `INFRA_TASKS.md` snapshot (`ca26f50eb674fb9abbcc0cabfc1f27ec9da44d5259cb1af8196db23b6c94e341`, 5 tasks: `cmmmech-infra-0001` through `cmmmech-infra-0005`) was partitioned by repair ownership and dependency structure into 4 GitHub issues in `CultureBotAI/CMMMech`:

| Group ID | Task IDs | Category | Target | GitHub Issue | Planned Disposition | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `IGRP-C1S6-001` | `cmmmech-infra-0001`, `cmmmech-infra-0005` | `workflow` | `scripts/record_review.py`, `tests/test_record_review_contract.py` | [#805](https://github.com/CultureBotAI/CMMMech/issues/805) | `deferred` | Upstream `CultureBotAI/culturebotai-claw` vendored sync (`scripts/check_vendored_sync.py`) |
| `IGRP-C1S6-002` | `cmmmech-infra-0002` | `schema` | `src/cmmmech/schema/cmmmech.yaml`, `scripts/render_pages.py`, `src/cmmmech/templates/material.html` | [#806](https://github.com/CultureBotAI/CMMMech/issues/806) | `resolved` | None |
| `IGRP-C1S6-003` | `cmmmech-infra-0003` | `schema` | `src/cmmmech/schema/cmmmech.yaml` | [#807](https://github.com/CultureBotAI/CMMMech/issues/807) | `resolved` | None |
| `IGRP-C1S6-004` | `cmmmech-infra-0004` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#808](https://github.com/CultureBotAI/CMMMech/issues/808) | `resolved` | `cmmmech-infra-0002`, `cmmmech-infra-0003` |

## 2. Dependency Order & Execution Plan

1. **Step 1 — Schema Enhancements (`cmmmech-infra-0002`, `cmmmech-infra-0003`)**:
   - In `src/cmmmech/schema/cmmmech.yaml`, add optional backward-compatible `ima_symbol` (`range: NonEmptyText`) and `polymorph_or_grade` (`range: NonEmptyText`) attributes to `CriticalMineralRecord` (`#806`).
   - In `src/cmmmech/schema/cmmmech.yaml`, expand `CausalPredicateEnum` with `degrades`, `dissolves`, `hydrolyzes`, and `solubilizes` in alphabetical order (`#807`).
   - Add unit tests in `tests/test_validation.py` verifying that `ima_symbol` and `polymorph_or_grade` accept valid non-empty strings and reject blank strings, and that all 4 new causal predicates validate cleanly on `CausalEdge` instances.
2. **Step 2 — Static Site Rendering Support (`cmmmech-infra-0002`)**:
   - Update `scripts/render_pages.py` (`prepare_record_data` and `render`) and `src/cmmmech/templates/material.html` so records with `ima_symbol` or `polymorph_or_grade` render header badges and index those tokens in client-side search while preserving zero diff on existing `pages/` output.
   - Add unit tests in `tests/test_render_pages.py`.
3. **Step 3 — First-Class Causal-Graph & Protein-Example Curation Writer (`cmmmech-infra-0004`)**:
   - Implement `scripts/curate_causal_graphs.py` (`#808`) depending on the updated `CriticalMineralRecord` schema slots (`ima_symbol`, `polymorph_or_grade`, `causal_graphs`) and `CausalPredicateEnum`.
   - Enforce canonical key ordering (`CANONICAL_RECORD_KEYS` and `CANONICAL_MECHANISM_KEYS`) so `causal_graphs` is always serialized immediately after `mechanisms` and before `curation_history` and `history_refs`.
   - Validate candidate updates via `cmmmech.validation.validate_record` prior to writing or minting history, and atomically mint `EDIT` `HistoryRecord` sidecars via `cmmmech.history.cmd_new`.
   - Add unit tests in `tests/test_curate_causal_graphs.py`.
4. **Step 4 — Explicit Deferral of Upstream-Governed `scripts/record_review.py` Tasks (`cmmmech-infra-0001`, `cmmmech-infra-0005`)**:
   - Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` and enforced by `scripts/check_vendored_sync.py`, track both tasks in open issue [#805](https://github.com/CultureBotAI/CMMMech/issues/805) (`status: deferred`) and carry them forward explicitly to Cycle 2.
