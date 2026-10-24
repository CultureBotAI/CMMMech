# Cycle 3 Stage 6 Infrastructure Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Cycle / Stage**: `3` / `6` (`infrastructure`)

## 1. Validation Commands & Outcomes

| Validation Gate | Command | Result |
| :--- | :--- | :--- |
| LinkML / Closed-Schema Record Validation | `.venv/bin/python -m cmmmech.cli validate --require-records` | `0` errors across all `646` records in `data/records/` |
| Append-Only History Sidecar Validation | `.venv/bin/python -m cmmmech.cli validate-history --base main` | `0` errors across all `966` history sidecars in `history/` |
| Structured Record Review Contract | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` errors across all `788` review bundles |
| Static Site Drift & Sandboxed Render Check | `.venv/bin/python scripts/render_pages.py` and `.venv/bin/python scripts/render_pages.py --check` | `Wrote .../pages` (`646` materials, `422` mechanisms) and `pages/ is current` (`0` diffs) inside the Seatbelt sandbox |
| Vendored Artifact Governance Check | `.venv/bin/python scripts/check_vendored_sync.py` | `OK: 22 governed artifacts match the pinned claw revision` |
| Unit Test Suite | `.venv/bin/python -m pytest -q` | `377 passed, 3 skipped` (`373 passed, 3 skipped` in sandbox + `4 passed` in `tests/test_record_review_contract.py`; includes `test_remove_tree_falls_back_when_shutil_rmtree_blocked` & `test_sync_rendered_tree_updates_in_place_when_remove_tree_blocked` in `tests/test_render_pages.py` and `test_apply_curation_patch_supports_mechanism_field_patches` & `test_apply_curation_patch_syncs_node_and_mechanism_protein_examples_parity` in `tests/test_curate_causal_graphs.py`) |
| Linter Check | `.venv/bin/python -m ruff check --no-cache src/ scripts/curate_causal_graphs.py scripts/render_pages.py tests/` | `All checks passed!` |
| Workflow Profile & INFRA_TASKS Ledger Validation | `PYTHONPATH=.../culturebotai-claw/src .venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --repository-key cmmmech` | `Workflow profile valid` (`INFRA_TASKS.md` inventory valid with real GitHub issue URLs) |

## 2. Issue-Linked Task Dispositions

- **`cmmmech-infra-0007`** ([#834](https://github.com/CultureBotAI/CMMMech/issues/834)) — **`resolved`**:
  Added `_remove_tree()` (catching `PermissionError` from `shutil.rmtree` and falling back to bottom-up `Path.unlink()` / `Path.rmdir()`) and `_sync_rendered_tree()` (rendering into a `TemporaryDirectory` in `/tmp` and updating only changed files in `args.out` when Seatbelt blocks unlinking provenance-tagged workspace files) in `scripts/render_pages.py`. Verified by `test_remove_tree_falls_back_when_shutil_rmtree_blocked` and `test_sync_rendered_tree_updates_in_place_when_remove_tree_blocked` in `tests/test_render_pages.py` and sandboxed execution of `scripts/render_pages.py`.
- **`cmmmech-infra-0008` & `cmmmech-infra-0009`** ([#835](https://github.com/CultureBotAI/CMMMech/issues/835)) — **`resolved`**:
  Extended `apply_curation_patch()` in `scripts/curate_causal_graphs.py` to support mechanism-ID-keyed `mechanism_organisms`, `mechanism_evidence`, `mechanism_observations`, and composite `mechanism_patches` (in both upsert and `replace_*` modes), plus `node_protein_examples` upsert support with automatic bidirectional `mechanisms[].protein_examples` ↔ `causal_graphs[].nodes[].protein_examples` parity synchronization via `graph.mechanism_ref`. Verified by `test_apply_curation_patch_supports_mechanism_field_patches` and `test_apply_curation_patch_syncs_node_and_mechanism_protein_examples_parity` in `tests/test_curate_causal_graphs.py`.
- **`cmmmech-infra-0002`** ([#806](https://github.com/CultureBotAI/CMMMech/issues/806)), **`cmmmech-infra-0003`** ([#807](https://github.com/CultureBotAI/CMMMech/issues/807)), **`cmmmech-infra-0004`** ([#808](https://github.com/CultureBotAI/CMMMech/issues/808)), & **`cmmmech-infra-0006`** ([#822](https://github.com/CultureBotAI/CMMMech/issues/822)) — **`resolved`** (retained from Cycle 1 and Cycle 2 Stage 6):
  Verified regression-free across all `646` records, `966` history sidecars, and `377` unit tests.
- **`cmmmech-infra-0001` & `cmmmech-infra-0005`** ([#805](https://github.com/CultureBotAI/CMMMech/issues/805)) — **`deferred`**:
  Explicitly deferred and carried forward under open issue `#805` because `scripts/record_review.py` and `tests/test_record_review_contract.py` are vendored artifacts governed by `CultureBotAI/culturebotai-claw` and checked by `scripts/check_vendored_sync.py`.
