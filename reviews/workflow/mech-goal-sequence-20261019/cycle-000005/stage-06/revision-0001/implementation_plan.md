# Cycle 5 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `5` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff Timestamp**: `2026-10-31T00:16:21Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `db9e7a512b24c52f7ba8d1b47ff7019a32768c390f2c0d6e6cc10296f23870a0`
- **Frozen Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`

## 1. Frozen Task Intake & Dependency-Aware Issue Grouping

The supervisor-frozen `INFRA_TASKS.md` snapshot (`db9e7a512b24c52f7ba8d1b47ff7019a32768c390f2c0d6e6cc10296f23870a0`, 13 total tasks: `cmmmech-infra-0001` through `cmmmech-infra-0013`, including 3 non-resolved tasks `cmmmech-infra-0001` [`deferred`], `cmmmech-infra-0005` [`deferred`], and `cmmmech-infra-0013` [`note`]) was partitioned by repair ownership and dependency structure into GitHub issues in `CultureBotAI/CMMMech`:

| Group ID | Task IDs | Category | Target | GitHub Issue | Planned Disposition | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `IGRP-C1S6-001` | `cmmmech-infra-0001`, `cmmmech-infra-0005` | `workflow` | `scripts/record_review.py`, `tests/test_record_review_contract.py` | [#805](https://github.com/CultureBotAI/CMMMech/issues/805) | `deferred` | Upstream `CultureBotAI/culturebotai-claw` vendored sync (`scripts/check_vendored_sync.py`) |
| `IGRP-C1S6-002` | `cmmmech-infra-0002` | `schema` | `src/cmmmech/schema/cmmmech.yaml`, `scripts/render_pages.py`, `src/cmmmech/templates/material.html` | [#806](https://github.com/CultureBotAI/CMMMech/issues/806) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-003` | `cmmmech-infra-0003` | `schema` | `src/cmmmech/schema/cmmmech.yaml` | [#807](https://github.com/CultureBotAI/CMMMech/issues/807) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-004` | `cmmmech-infra-0004` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#808](https://github.com/CultureBotAI/CMMMech/issues/808) | `resolved` (Cycle 1 Stage 6) | `cmmmech-infra-0002`, `cmmmech-infra-0003` |
| `IGRP-C2S6-001` | `cmmmech-infra-0006` | `script` | `src/cmmmech/history.py`, `tests/test_history.py` | [#822](https://github.com/CultureBotAI/CMMMech/issues/822) | `resolved` (Cycle 2 Stage 6) | `cmmmech-infra-0004` |
| `IGRP-C3S6-001` | `cmmmech-infra-0007` | `script` | `scripts/render_pages.py`, `tests/test_render_pages.py` | [#834](https://github.com/CultureBotAI/CMMMech/issues/834) | `resolved` (Cycle 3 Stage 6) | None |
| `IGRP-C3S6-002` | `cmmmech-infra-0008`, `cmmmech-infra-0009` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#835](https://github.com/CultureBotAI/CMMMech/issues/835) | `resolved` (Cycle 3 Stage 6) | `cmmmech-infra-0004` |
| `IGRP-C4S6-001` | `cmmmech-infra-0010` | `validation` / `skill` | `src/cmmmech/validation.py`, `tests/test_validation.py`, `.claude/skills/*`, `docs/records.md` | [#839](https://github.com/CultureBotAI/CMMMech/issues/839) | `resolved` (Cycle 4 Stage 6) | [#838](https://github.com/CultureBotAI/CMMMech/issues/838), [#837](https://github.com/CultureBotAI/CMMMech/pull/837) |
| `IGRP-C4S6-002` | `cmmmech-infra-0011` | `script` / `skill` | `scripts/index_bounded_pdf_passages.py`, `tests/test_index_bounded_pdf_passages.py`, `.claude/skills/*`, `docs/records.md` | [#840](https://github.com/CultureBotAI/CMMMech/issues/840) | `resolved` (Cycle 4 Stage 6) | `cmmmech-infra-0010` ([#839](https://github.com/CultureBotAI/CMMMech/issues/839)) |
| `IGRP-C4S6-003` | `cmmmech-infra-0012` | `script` | `src/cmmmech/history.py`, `scripts/curate_causal_graphs.py`, `tests/test_history.py`, `tests/test_curate_causal_graphs.py` | [#822](https://github.com/CultureBotAI/CMMMech/issues/822) (companion [#866](https://github.com/CultureBotAI/CMMMech/issues/866)) | `resolved` (Cycle 4 Stage 6) | `cmmmech-infra-0004`, `cmmmech-infra-0006` ([#822](https://github.com/CultureBotAI/CMMMech/issues/822)) |
| `IGRP-C5S6-001` | `cmmmech-infra-0013` | `validation` | `src/cmmmech/validation.py`, `tests/test_validation.py` | [#839](https://github.com/CultureBotAI/CMMMech/issues/839) (companion [#882](https://github.com/CultureBotAI/CMMMech/issues/882), [#877](https://github.com/CultureBotAI/CMMMech/issues/877)) | `resolved` (Cycle 5 Stage 6) | `cmmmech-infra-0004`, `cmmmech-infra-0010` ([#839](https://github.com/CultureBotAI/CMMMech/issues/839)) |

## 2. Dependency Order & Execution Plan

1. **Step 1 — Preserve Cycles 1–4 Stage 6 Resolved Infrastructure (`cmmmech-infra-0002`–`0004`, `cmmmech-infra-0006`–`0012`)**:
   - Retain all schema, history sidecar, static page renderer, CLI writer, bounded PDF passage indexing, and validation enhancements delivered in Cycles 1–4 Stage 6 (`#806`, `#807`, `#808`, `#822`, `#834`, `#835`, `#839`, `#840`, `#866`) and verify regression-free operation across the 668-record corpus and 1,073 history sidecars.
2. **Step 2 — Enforce Canonical `sources`-before-`criticality` Top-Level Section Ordering (`cmmmech-infra-0013`, `#839` & companion `#882`, `IGRP-C5S6-001`)**:
   - In `src/cmmmech/validation.py`, extend `_section_order_errors(record: dict)` so that when both `sources` and `criticality` are present in `pos` (and the record is not an alphabetically sorted synthetic fixture dict where `keys == sorted(keys)`), `pos["criticality"] < pos["sources"]` appends `"$: criticality must appear after sources"`.
   - In `tests/test_validation.py`, extend `test_top_level_section_ordering_guardrail(record)` to verify that a record dictionary with `criticality` preceding `sources` fails `validate_record()` with `"$: criticality must appear after sources"`.
   - Verify that all `668` records in `data/records/*.yaml` (including the `13` legacy records normalized in Cycle 5 Stage 5 under `#877` / PR `#880`) pass `.venv/bin/python -m cmmmech.cli validate --require-records` with `0` errors.
3. **Step 3 — Explicit Deferral of Upstream-Governed `scripts/record_review.py` Tasks (`cmmmech-infra-0001`, `cmmmech-infra-0005`, `#805`, `IGRP-C1S6-001`)**:
   - Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` and enforced by `scripts/check_vendored_sync.py`, retain both tasks in open issue [#805](https://github.com/CultureBotAI/CMMMech/issues/805) (`status: deferred`) and carry them forward explicitly.
