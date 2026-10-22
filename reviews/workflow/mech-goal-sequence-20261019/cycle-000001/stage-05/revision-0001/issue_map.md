# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 1, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `5a9c27bb6e6313e050b02a595240b2048e13cfdf`
- **Scope Frozen At**: `2026-10-22T04:50:43Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`41b6901ec49ce42f9bd600393e6b2e933c530a17692dbb5b8f8353cc454892f7`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261022T050900Z-stage5-remediation-verification/review.yaml` (`sha256: 57b3fcc44286d5f46a0584c8a21381095a3eee98ccc1037920920bd98fbe3826`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state all --limit 50`. Only 2 open backlog issues existed (`#106`, `#115`), neither covering the 3 Stage 4 review findings (`cmmmech-stage4-finding-0001`, `cmmmech-stage4-finding-0002`, `cmmmech-stage4-finding-0003`). Three new tracked GitHub issues (`#801`, `#802`, `#803`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (20 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C1S5-001` | `cmmmech-stage4-finding-0001` | `cmmmech.mineral.missing-ima-identifiers-on-cited-species` | [`#801`](https://github.com/CultureBotAI/CMMMech/issues/801) | `resolved` | 17 mineral records (`alburnite`, `briartite`, `cavansite`, `compreignacite`, `falottaite`, `greigite`, `katsarosite`, `lindbergite`, `metavivianite`, `moolooite`, `pentagonite`, `pertlikite`, `regerite`, `schwertmannite`, `struvite-k`, `wheatleyite`, `zincobriartite`) | Added structured `IMA:YYYY-NNN` identifier entries matching `ima_2026_09` and each record's `description`, plus 17 append-only `EDIT` history sidecars. |
| `GRP-C1S5-002` | `cmmmech-stage4-finding-0002` | `cmmmech.wulfenite.missing-ima-master-list-source` | [`#802`](https://github.com/CultureBotAI/CMMMech/issues/802) | `resolved` | 1 mineral record (`wulfenite`) | Added `ima_2026_09` (`The New IMA List of Minerals, September 2026`) to `data/records/wulfenite.yaml` `sources`, plus 1 append-only `EDIT` history sidecar. |
| `GRP-C1S5-003` | `cmmmech-stage4-finding-0003` | `cmmmech.records.trailing-mechanisms-after-history` | [`#803`](https://github.com/CultureBotAI/CMMMech/issues/803) | `resolved` | 2 `primary_resource` records (`cobalt-rich-ferromanganese-crusts`, `rare-earth-rich-deep-sea-mud`) | Reordered top-level keys so `mechanisms` precedes `curation_history` and `history_refs`, plus 2 append-only `EDIT` history sidecars. |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all fixes are record-level YAML and history sidecar updates).
