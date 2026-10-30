# Stage 5 Grouped Remediation Issue Map (`mech-goal-sequence-20261019`, Cycle 4, Stage 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Source Revision**: `cfbf9053da1f950d6c2f6c7bac55f8bb38a5116f`
- **Scope Frozen At**: `2026-10-30T10:35:00Z`
- **Previous Stage Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml` (`757e91d63f85ce1e0a97b5f05f7150273dff631c57ea0a65d4fa9333afbc48ee`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261030T104000Z-cycle4-stage5-remediation-verification/review.yaml` (`sha256: 67a469cfc85ba0cf2f041f8c19573269bbc395f02a08218e19ae141f3de72521`)

## 1. Deduplication Against Open & Closed GitHub Issues

Before creating issues, the open and closed GitHub issue queues in `CultureBotAI/CMMMech` were searched via `gh issue list --repo CultureBotAI/CMMMech --state all --limit 100`. Open issues (`#106`, `#115`, `#805`, `#822`, `#839`, `#840`) were inspected and none covered the 3 Cycle 4 Stage 4 review findings (`cmmmech-cycle4-stage4-finding-0001`, `cmmmech-cycle4-stage4-finding-0002`, `cmmmech-cycle4-stage4-finding-0003`). Three new tracked GitHub issues (`#862`, `#863`, `#864`) were created, one per root-cause and repair-ownership group.

## 2. Root-Cause Groups, Issue Mapping, and Finding Dispositions

| Group ID | Finding IDs | Issue Key | GitHub Issue | Status | Target Records (25 total) | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `GRP-C4S5-001` | `cmmmech-cycle4-stage4-finding-0001` | `cmmmech.traction-battery-hydrometallurgical-residue.causal-node-spurious-br-sample-codes-and-consortium-label` | [`#862`](https://github.com/CultureBotAI/CMMMech/issues/862) | `resolved` | 1 secondary_resource record (`traction-battery-hydrometallurgical-residue`) | Updated `causal_graphs[0]` (`ferrooxidans_battery_residue_bioleaching_graph`) in `data/records/traction-battery-hydrometallurgical-residue.yaml` so `nodes[3].label` (`solid_feed_substrate`) reads `Industrial traction-battery hydrometallurgical residues (nickel-line and cobalt-line residues)`, `nodes[0].label` reads `Sqr / Sqor sulfide-quinone reductase (consortium sqr / sqor)`, `nodes[1].label` reads `Tth / TetH tetrathionate hydrolase (consortium tth)`, and `edges[0].evidence[0].explanation` reads `Reduced sulfur oxidation in the five-member acidophile consortium couples Sqr/Sqor and tetrathionate hydrolysis to sulfuric acid proton generation.` with 1 append-only `EDIT` history sidecar (`history/records/traction-battery-hydrometallurgical-residue/2026-10-30T103604Z-claude-33e08d.yaml`). |
| `GRP-C4S5-002` | `cmmmech-cycle4-stage4-finding-0002` | `cmmmech.records.mechanisms-before-sources-key-order` | [`#863`](https://github.com/CultureBotAI/CMMMech/issues/863) | `resolved` | 8 records (`cadmium-telluride-photovoltaic-module-scrap`, `cathode-ray-tube-glass`, `churchite-y`, `end-of-life-cigs-photovoltaic-modules`, `end-of-life-crystalline-silicon-photovoltaic-modules`, `iron-ore-tailings`, `polymetallic-nodules`, `waste-printed-circuit-boards`) | Normalized top-level YAML key order to `CANONICAL_RECORD_KEYS` so `sources` and `criticality` precede `mechanisms` and `causal_graphs` across all 8 records with 8 append-only `EDIT` history sidecars. |
| `GRP-C4S5-003` | `cmmmech-cycle4-stage4-finding-0003` | `cmmmech.records.history-refs-before-curation-history-key-order` | [`#864`](https://github.com/CultureBotAI/CMMMech/issues/864) | `resolved` | 16 records (`aluminium-salt-slag`, `beryllium`, `beverage-carton-hydropulping-reject`, `biogas-desulfurization-sulfur-residue`, `cesium`, `electroformed-copper-silver-manufacturing-scrap`, `ground-waste-tire-rubber`, `ion-adsorption-rare-earth-clay`, `pharmaceutical-blister-packaging-waste`, `rhenium`, `rubidium`, `spent-lead-acid-battery-electrolyte`, `spent-vanadium-flow-battery-electrolyte`, `strontium`, `zinc-leach-residue`, `zinc-purification-hot-filter-cake`) | Normalized top-level YAML key order to `CANONICAL_RECORD_KEYS` so `curation_history` precedes `history_refs` across all 16 records with 16 append-only `EDIT` history sidecars. |

## 3. Carry-Forward Blockers & Infrastructure Tasks

- **Carry-Forward Findings (`carry_forward_ids`)**: `[]` (0 open/deferred findings remain).
- **Infrastructure Tasks (`infra_tasks`)**: `[]` (all 3 Cycle 4 Stage 4 findings were resolved directly in record YAML and history sidecars; the pre-existing `cmmmech-infra-0012` note in `INFRA_TASKS.md` regarding Seatbelt `NamedTemporaryFile` fallback in `src/cmmmech/history.py` and `scripts/curate_causal_graphs.py` was updated with a Stage 5 confirmation reference to `#862`, `#863`, and `#864`).
