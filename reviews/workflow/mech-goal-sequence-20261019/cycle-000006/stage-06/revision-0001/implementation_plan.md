# Cycle 6 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `6` / `6` (`infrastructure`)
- **Source Revision (`main`)**: `4962511c71617d418789940aad343cd17aac06d0`
- **Frozen `INFRA_TASKS.md` Cutoff Timestamp**: `2026-11-03T07:37:21Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `82196195615969b34da614062fa323c56b827d8a07a52c66ab910498cba301a9`
- **Frozen Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`

## 1. Frozen Task Intake & Dependency-Aware Issue Grouping

The supervisor-frozen `INFRA_TASKS.md` snapshot (`82196195615969b34da614062fa323c56b827d8a07a52c66ab910498cba301a9`, `13` total tasks: `cmmmech-infra-0001` through `cmmmech-infra-0013`, including `2` non-resolved tasks `cmmmech-infra-0001` [`deferred`] and `cmmmech-infra-0005` [`deferred`] and `11` previously resolved tasks `cmmmech-infra-0002`–`0004` and `cmmmech-infra-0006`–`0013`; `0` new `note` or `open` tasks arrived during Cycle 6 Stages 1–5) was partitioned by repair ownership and dependency structure into GitHub issues in `CultureBotAI/CMMMech`:

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

1. **Step 1 — Preserve Cycles 1–5 Stage 6 Resolved Infrastructure (`cmmmech-infra-0002`–`0004`, `cmmmech-infra-0006`–`0013`)**:
   - Retain all schema, history sidecar, static page renderer, CLI writer (`scripts/curate_causal_graphs.py`), bounded PDF passage indexing (`scripts/index_bounded_pdf_passages.py`), and validation (`Source.title` and top-level section ordering) enhancements delivered in Cycles 1–5 Stage 6 (`#806`, `#807`, `#808`, `#822`, `#834`, `#835`, `#839`, `#840`, `#866`, `#882`, `#877`) and verify regression-free operation across all `673` records in `data/records/*.yaml`, `1,245` history sidecars in `history/`, `981` review bundles in `reviews/structured/`, and the full unit test suite.
2. **Step 2 — Explicit Deferral and Carry-Forward of Upstream-Governed `scripts/record_review.py` Tasks (`cmmmech-infra-0001`, `cmmmech-infra-0005`, `#805`, `IGRP-C1S6-001`)**:
   - Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` (pinned revision `a1c9db3260fc253de16cabfaef5cf6c2fc3fbdd7`) and enforced by `scripts/check_vendored_sync.py` (`AGENTS.md`: *"Fleet admission and governed artifacts are installed. Use CLAW's supported synchronizer and the immutable pin; never hand-edit governed copies."*), retain both non-resolved tasks in open issue [#805](https://github.com/CultureBotAI/CMMMech/issues/805) (`status: deferred`), update their dispositions in `INFRA_TASKS.md` and `evidence.yaml` to record Cycle 6 Stage 6 evaluation, and carry them forward explicitly.
3. **Step 3 — Synchronize `reviews/workflow/latest.yaml` and Validate Workflow & Corpus Contracts**:
   - Append the verified Cycle 6 Stage 5 entry (`PR #904`, `merge_commit_sha: 4962511c71617d418789940aad343cd17aac06d0`) from `verified-evidence-index.json` to `reviews/workflow/latest.yaml`.
   - Validate all repository offline checks, vendored artifact synchronization, and Stage 6 workflow evidence (`kg_microbe_workflows validate-evidence`).
