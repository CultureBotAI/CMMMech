# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 5, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `35a238bcbe1239d32e401f11976481f3e3cb1f5f`
- **Scope Frozen At**: `2026-10-30T22:15:00Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml` (`d77d6b46b063baee49ecc557266e16a8f3b08fbaa55c8ad43543c42df65c57dc`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261030T222000Z-cycle5-stage5-remediation-verification/review.yaml` (`sha256: 9eb6918607c53f92c7ea3a884a5473c82537278324dd08df2a078ce43c71e72e`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state all --limit 50`. Open issues (`#106`, `#115`, `#805`) and recently closed issues were inspected and none covered the 3 Cycle 5 Stage 4 review findings (`cmmmech-cycle5-stage4-finding-0001`, `cmmmech-cycle5-stage4-finding-0002`, `cmmmech-cycle5-stage4-finding-0003`). Three new tracked GitHub issues (`#877`, `#878`, `#879`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (15 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C5S5-001` | `cmmmech-cycle5-stage4-finding-0001` | `cmmmech.records.criticality-before-sources-key-order` | [`#877`](https://github.com/CultureBotAI/CMMMech/issues/877) | `resolved` | 13 records (`chromium`, `electrical-steel`, `hafnium`, `manganese`, `praseodymium`, `rare-earth-element-commodities`, `scandium`, `selenium`, `silicon-carbide`, `silicon`, `synthetic-graphite`, `uranium`, `vanadium`) | Normalized top-level YAML key order to `CANONICAL_RECORD_KEYS` so `sources` precedes `criticality` across all 13 records with 13 append-only `EDIT` history sidecars. |
| `GRP-C5S5-002` | `cmmmech-cycle5-stage4-finding-0002` | `cmmmech.tetrahedrite-concentrate.causal-node-tth-hydrolase-species-label-scope` | [`#878`](https://github.com/CultureBotAI/CMMMech/issues/878) | `resolved` | 1 primary_resource record (`tetrahedrite-concentrate`) | Updated `causal_graphs[0]` (`ferrooxidans_tetrahedrite_bioleaching_graph`) in `data/records/tetrahedrite-concentrate.yaml` so `nodes[1].label` (`tth_hydrolase`) reads `Tth / TetH tetrathionate hydrolase (tth / AFE_0029 / tetH)`, `nodes[1].description` names both `A. ferrooxidans` (`tth` / `AFE_0029`) and `A. ferrivorans` CF27 (`tetH` `UniProtKB:A0A060URH6`), and `edges[0].evidence[0].explanation` covers both culture arms per Kupka et al. (2025) with 1 append-only `EDIT` history sidecar (`history/records/tetrahedrite-concentrate/2026-10-30T222651Z-claude-b6026b.yaml`). |
| `GRP-C5S5-003` | `cmmmech-cycle5-stage4-finding-0003` | `cmmmech.waste-liquid-crystal-display-panels.causal-node-tth-hydrolase-paralog-label-scope` | [`#879`](https://github.com/CultureBotAI/CMMMech/issues/879) | `resolved` | 1 secondary_resource record (`waste-liquid-crystal-display-panels`) | Updated `causal_graphs[0]` (`ferrooxidans_lcd_indium_bioleaching_graph`) in `data/records/waste-liquid-crystal-display-panels.yaml` so `nodes[1].label` (`tth_hydrolase`) reads `Tth tetrathionate hydrolase (tth AFE_0029 / tth GCD22_14205 / tth GCD22_02315)` and `nodes[1].description` names both `Acidithiobacillus thiooxidans` ATCC 19377 `tth` paralogs (`GCD22_14205` and `GCD22_02315`) alongside `A. ferrooxidans` `tth` (`AFE_0029`) per Pourhossein & Mousavi (2023) with 1 append-only `EDIT` history sidecar (`history/records/waste-liquid-crystal-display-panels/2026-10-30T222652Z-claude-9536c6.yaml`). |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all 3 Cycle 5 Stage 4 findings were resolved directly in record YAML and history sidecars; an advisory follow-up note `cmmmech-infra-0013` was recorded in `INFRA_TASKS.md` linked to validator-hygiene issue `#839` and `#877` so Cycle 5 Stage 6 can extend `_section_order_errors()` in `src/cmmmech/validation.py` to enforce `sources` before `criticality`).
