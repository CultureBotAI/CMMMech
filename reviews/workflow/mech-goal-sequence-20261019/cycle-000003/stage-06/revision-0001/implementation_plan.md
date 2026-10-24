# Cycle 3 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `3` / `6` (`infrastructure`)
- **Frozen `INFRA_TASKS.md` Cutoff Timestamp**: `2026-10-24T04:20:20Z`
- **Frozen `INFRA_TASKS.md` SHA-256**: `d3bbc5b0b6083110107f7e1a6b632cc92d32c84997e0ee03c84108ed5485e0a1`
- **Frozen Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`

## 1. Frozen Task Intake & Dependency-Aware Issue Grouping

The supervisor-frozen `INFRA_TASKS.md` snapshot (`d3bbc5b0b6083110107f7e1a6b632cc92d32c84997e0ee03c84108ed5485e0a1`, 9 total tasks: `cmmmech-infra-0001` through `cmmmech-infra-0009`, including 5 non-resolved tasks `cmmmech-infra-0001`, `cmmmech-infra-0005`, `cmmmech-infra-0007`, `cmmmech-infra-0008`, `cmmmech-infra-0009`) was partitioned by repair ownership and dependency structure into GitHub issues in `CultureBotAI/CMMMech`:

| Group ID | Task IDs | Category | Target | GitHub Issue | Planned Disposition | Dependencies |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `IGRP-C1S6-001` | `cmmmech-infra-0001`, `cmmmech-infra-0005` | `workflow` | `scripts/record_review.py`, `tests/test_record_review_contract.py` | [#805](https://github.com/CultureBotAI/CMMMech/issues/805) | `deferred` | Upstream `CultureBotAI/culturebotai-claw` vendored sync (`scripts/check_vendored_sync.py`) |
| `IGRP-C1S6-002` | `cmmmech-infra-0002` | `schema` | `src/cmmmech/schema/cmmmech.yaml`, `scripts/render_pages.py`, `src/cmmmech/templates/material.html` | [#806](https://github.com/CultureBotAI/CMMMech/issues/806) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-003` | `cmmmech-infra-0003` | `schema` | `src/cmmmech/schema/cmmmech.yaml` | [#807](https://github.com/CultureBotAI/CMMMech/issues/807) | `resolved` (Cycle 1 Stage 6) | None |
| `IGRP-C1S6-004` | `cmmmech-infra-0004` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#808](https://github.com/CultureBotAI/CMMMech/issues/808) | `resolved` (Cycle 1 Stage 6) | `cmmmech-infra-0002`, `cmmmech-infra-0003` |
| `IGRP-C2S6-001` | `cmmmech-infra-0006` | `script` | `src/cmmmech/history.py`, `tests/test_history.py` | [#822](https://github.com/CultureBotAI/CMMMech/issues/822) | `resolved` (Cycle 2 Stage 6) | `cmmmech-infra-0004` |
| `IGRP-C3S6-001` | `cmmmech-infra-0007` | `script` | `scripts/render_pages.py`, `tests/test_render_pages.py` | [#834](https://github.com/CultureBotAI/CMMMech/issues/834) | `resolved` (Cycle 3 Stage 6) | None |
| `IGRP-C3S6-002` | `cmmmech-infra-0008`, `cmmmech-infra-0009` | `script` | `scripts/curate_causal_graphs.py`, `tests/test_curate_causal_graphs.py` | [#835](https://github.com/CultureBotAI/CMMMech/issues/835) | `resolved` (Cycle 3 Stage 6) | `cmmmech-infra-0004` |

## 2. Dependency Order & Execution Plan

1. **Step 1 — Preserve Cycle 1 & Cycle 2 Stage 6 Resolved Infrastructure (`cmmmech-infra-0002`, `cmmmech-infra-0003`, `cmmmech-infra-0004`, `cmmmech-infra-0006`)**:
   - Retain all schema, history sidecar, and CLI writer enhancements delivered in Cycle 1 and Cycle 2 Stage 6 (`#806`, `#807`, `#808`, `#822`) and verify regression-free operation across the 646-record corpus and 966 history sidecars.
2. **Step 2 — Implement Sandboxed Static Page Rendering Fallback (`cmmmech-infra-0007`, `#834`)**:
   - In `scripts/render_pages.py`, add `_remove_tree(path: Path) -> bool` (wrapping `shutil.rmtree(path)` and falling back to bottom-up `Path.unlink()` / `Path.rmdir()` when Python 3.13's `dir_fd` `unlinkat()` raises `PermissionError`, returning `False` if the sandbox disallows deleting existing provenance-tagged workspace files) and `_sync_rendered_tree(src: Path, dst: Path)` (rendering into a `TemporaryDirectory` in `/tmp` and updating only changed files in `args.out` when `_remove_tree` returns `False`).
   - Add unit tests `test_remove_tree_falls_back_when_shutil_rmtree_blocked` and `test_sync_rendered_tree_updates_in_place_when_remove_tree_blocked` in `tests/test_render_pages.py`, and verify `.venv/bin/python scripts/render_pages.py` succeeds inside the Seatbelt sandbox.
3. **Step 3 — Implement Mechanism-Level Field Patches and Node-Level `protein_examples` Parity Upsert (`cmmmech-infra-0008`, `cmmmech-infra-0009`, `#835`)**:
   - In `scripts/curate_causal_graphs.py` `apply_curation_patch()`, add support for mechanism-ID-keyed `mechanism_organisms`, `mechanism_evidence`, `mechanism_observations`, and composite `mechanism_patches` (supporting both upsert and `replace_*` modes, raising `ValueError` on unknown `mechanism_id`, and marking `mechanisms` in `touched_sections`).
   - Add `node_protein_examples` upsert support (`{"<graph_id>/<node_id>": [...]}`, `{graph_id: {node_id: [...]}}`, or list of `{"graph_id", "node_id", "protein_examples"}` entries) with automatic bidirectional `mechanisms[].protein_examples` ↔ `causal_graphs[].nodes[].protein_examples` parity synchronization via `graph.mechanism_ref`.
   - Add unit tests `test_apply_curation_patch_supports_mechanism_field_patches` and `test_apply_curation_patch_syncs_node_and_mechanism_protein_examples_parity` in `tests/test_curate_causal_graphs.py`.
4. **Step 4 — Explicit Deferral of Upstream-Governed `scripts/record_review.py` Tasks (`cmmmech-infra-0001`, `cmmmech-infra-0005`)**:
   - Because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` and enforced by `scripts/check_vendored_sync.py`, retain both tasks in open issue [#805](https://github.com/CultureBotAI/CMMMech/issues/805) (`status: deferred`) and carry them forward explicitly.
