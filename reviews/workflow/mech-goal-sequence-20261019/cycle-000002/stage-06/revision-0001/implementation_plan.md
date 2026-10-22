# Cycle 2 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `2` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff Timestamp**: `2026-10-22T14:41:19Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `b1c109d7c403e03e7bef7a0008a771577f7fb403a72757ec45e49f59ee3f15cd`
- **Frozen Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`

## 1. Frozen Task Intake & Dependency-Aware Issue Grouping

The supervisor-frozen `INFRA_TASKS.md` snapshot (`b1c109d7c403e03e7bef7a0008a771577f7fb403a72757ec45e49f59ee3f15cd`, 6 tasks: `cmmmech-infra-0001` through `cmmmech-infra-0006`) was partitioned by repair ownership and dependency structure into 5 GitHub issues in `CultureBotAI/CMMMech`:

| Group ID | Task IDs | Category | Target | GitHub Issue | Planned Disposition | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `IGRP-C1S6-001` | `cmmmech-infra-0001`, `cmmmech-infra-0005` | `workflow` | `scripts/record_review.py`, `tests/test_record_review_contract.py` | [#805](https://github.com/CultureBotAI/CMMMech/issues/805) | `deferred` | Upstream `CultureBotAI/culturebotai-claw` vendored sync (`scripts/check_vendored_sync.py`) |
| `IGRP-C1S6-002` | `cmmmech-infra-0002` | `schema` | `src/cmmmech/schema/cmmmech.yaml`, `scripts/render_pages.py`, `src/cmmmech/templates/material.html` | [#806](https://github.com/CultureBotAI/CMMMech/issues/806) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-003` | `cmmmech-infra-0003` | `schema` | `src/cmmmech/schema/cmmmech.yaml` | [#807](https://github.com/CultureBotAI/CMMMech/issues/807) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-004` | `cmmmech-infra-0004` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#808](https://github.com/CultureBotAI/CMMMech/issues/808) | `resolved` (Cycle 1 Stage 6) | `cmmmech-infra-0002`, `cmmmech-infra-0003` |
| `IGRP-C2S6-001` | `cmmmech-infra-0006` | `script` | `src/cmmmech/history.py`, `tests/test_history.py` | [#822](https://github.com/CultureBotAI/CMMMech/issues/822) | `resolved` (Cycle 2 Stage 6) | `cmmmech-infra-0004` |

## 2. Dependency Order & Execution Plan

1. **Step 1 — Preserve Cycle 1 Stage 6 Resolved Infrastructure (`cmmmech-infra-0002`, `cmmmech-infra-0003`, `cmmmech-infra-0004`)**:
   - Retain all schema and CLI writer enhancements delivered in Cycle 1 Stage 6 (`#806`, `#807`, `#808`) and verify regression-free operation across the expanded 631-record corpus and 924 history sidecars.
2. **Step 2 — Implement Sandboxed History Sidecar Creation Fallback (`cmmmech-infra-0006`, `#822`)**:
   - In `src/cmmmech/history.py` `cmd_new()`, keep `os.link(stream.name, path)` as the primary atomic hardlink path when permitted by the operating system, and catch `PermissionError` (raised inside macOS Seatbelt sandboxes that disallow `os.link`) to fall back to exclusive file creation via `os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o644)` with `fsync`.
   - Ensure that if the exclusive-create write fails mid-stream, any partial target is unlinked before re-raising, and that an existing target file raises `FileExistsError` without ever truncating or overwriting an existing history session.
   - Add unit test `test_scaffolder_falls_back_to_exclusive_create_when_hardlink_blocked` in `tests/test_history.py` verifying both successful fallback creation and collision refusal when `os.link` raises `PermissionError`, and verify that `tests/test_curate_causal_graphs.py` executes cleanly inside the Seatbelt sandbox.
3. **Step 3 — Explicit Deferral of Upstream-Governed `scripts/record_review.py` Tasks (`cmmmech-infra-0001`, `cmmmech-infra-0005`)**:
   - Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` and enforced by `scripts/check_vendored_sync.py`, retain both tasks in open issue [#805](https://github.com/CultureBotAI/CMMMech/issues/805) (`status: deferred`) and carry them forward explicitly.
