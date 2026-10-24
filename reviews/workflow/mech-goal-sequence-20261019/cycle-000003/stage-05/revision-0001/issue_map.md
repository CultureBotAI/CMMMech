# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 3, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `3d36a06c76337922d651bdacbffbe05368e28abc`
- **Scope Frozen At**: `2026-10-24T03:38:00Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml` (`0f2abb0b16f292df06e8e4388f14528c328feb975ce8b5240855f8c092bd0a60`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261024T034200Z-cycle3-stage5-remediation-verification/review.yaml` (`sha256: 844baae17cc770de5632f1d22375cf707794ca6ae2884a7e54fcbdbd68cd77eb`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state all --limit 100`. Only 2 open backlog issues existed (`#106`, `#115`), neither covering the 3 Cycle 3 Stage 4 review findings (`cmmmech-cycle3-stage4-finding-0001`, `cmmmech-cycle3-stage4-finding-0002`, `cmmmech-cycle3-stage4-finding-0003`). Three new tracked GitHub issues (`#830`, `#831`, `#832`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (3 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C3S5-001` | `cmmmech-cycle3-stage4-finding-0001` | `cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol` | [`#830`](https://github.com/CultureBotAI/CMMMech/issues/830) | `resolved` | 1 mineral record (`bixbyite-mn`) | Added `gene_symbol: Mesau_02205` to `mechanisms[0].protein_examples[0]` and `causal_graphs[0].nodes[0].protein_examples[0]` for `UniProtKB:A0A0K2YWP2` (`A0A0K2YWP2_9HYPH`) in `data/records/bixbyite-mn.yaml` with 1 append-only `EDIT` history sidecar (`history/records/bixbyite-mn/2026-10-24T034011Z-claude-8983ab.yaml`). |
| `GRP-C3S5-002` | `cmmmech-cycle3-stage4-finding-0002` | `cmmmech.mineral_group.noncanonical-ima-compendium-source-id` | [`#831`](https://github.com/CultureBotAI/CMMMech/issues/831) | `resolved` | 1 mineral_group record (`olivine-group`) | Normalized `sources[0].id` from `ima_compendium` to canonical `ima_compendium_2019` for the 2019 IMA-CNMNC Nomenclature Compendium in `data/records/olivine-group.yaml` with 1 append-only `EDIT` history sidecar (`history/records/olivine-group/2026-10-24T034011Z-claude-4d2bc8.yaml`). |
| `GRP-C3S5-003` | `cmmmech-cycle3-stage4-finding-0003` | `cmmmech.mineral.noncanonical-ch407-its-source-id` | [`#832`](https://github.com/CultureBotAI/CMMMech/issues/832) | `resolved` | 1 mineral record (`humboldtine`) | Normalized `sources[4].id` and `mechanisms[0].evidence[3].source_ref` from `genbank_niger` to canonical `genbank_ch407` for GenBank ITS accession `KF768341.1` (*Aspergillus niger* strain Ch 4/07) in `data/records/humboldtine.yaml` with 1 append-only `EDIT` history sidecar (`history/records/humboldtine/2026-10-24T034011Z-claude-148f6e.yaml`). |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all fixes are record-level YAML and history sidecar updates; no Cycle 3 Stage 4 findings required infrastructure changes).
