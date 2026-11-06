# Cycle 10 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `10`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Frozen Predecessor Commit (`source_revision`)**: `9e14224d8bee0865a43f15eda28c0d01351c3c47`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/evidence.yaml` (`sha256: 32b1c7236e2946c878d23d7a7823ebd4e34985dd0d636e7b9629e9a55da7716f`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261106T145500Z-cycle10-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GRP-C10S5-001` | `cmmmech-cycle10-stage4-finding-0001` | [#950](https://github.com/CultureBotAI/CMMMech/issues/950) | `cmmmech:calcite`, `cmmmech:vaterite`, `cmmmech:lithium-bearing-geothermal-brine` | `resolved` |
| `GRP-C10S5-002` | `cmmmech-cycle10-stage4-finding-0002` | [#951](https://github.com/CultureBotAI/CMMMech/issues/951) | `cmmmech:brushite` | `resolved` |
| `GRP-C10S5-003` | `cmmmech-cycle10-stage4-finding-0003` | [#952](https://github.com/CultureBotAI/CMMMech/issues/952) | `cmmmech:strontianite`, `cmmmech:smithsonite` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C10S5-001` (`cmmmech-cycle10-stage4-finding-0001` -> Issue [#950](https://github.com/CultureBotAI/CMMMech/issues/950))
- **Root Cause**: Across the three *Sporosarcina pasteurii* DSM 33 Cornish geothermal-brine MICP pretreatment records from Rehmanji et al. (2025, `rehmanji2025` / `rehmanji2025_si`) — `data/records/calcite.yaml`, `data/records/vaterite.yaml`, and `data/records/lithium-bearing-geothermal-brine.yaml` — `causal_graphs[0].nodes[2..3].description` retained generic template descriptions repeating their capitalized node labels in parentheses and included inapplicable `/phosphate` wording (also on `edges[2].relationship`), `edges[0].evidence[0].explanation` used a generic 70-character string, and `edges[1..2]` interpolated capitalized node labels mid-sentence with singular verb `precipitates` and `supports: support` without noting ex situ mixed-phase XRD and control/aliquot caveats.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[2..3].description`, `causal_graphs[0].edges[0].evidence[0].explanation`, `causal_graphs[0].edges[1..2].description`, `causal_graphs[0].edges[1..2].evidence[0].{supports,explanation}`, and `causal_graphs[0].edges[2].relationship` (`cation precipitation with carbonate`) across all three records via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/calcite/2026-11-06T145838Z-marcin-f0ecb2.yaml`
    - `history/records/vaterite/2026-11-06T145838Z-marcin-7a48a7.yaml`
    - `history/records/lithium-bearing-geothermal-brine/2026-11-06T145838Z-marcin-23f180.yaml`

### 2. `GRP-C10S5-002` (`cmmmech-cycle10-stage4-finding-0002` -> Issue [#951](https://github.com/CultureBotAI/CMMMech/issues/951))
- **Root Cause**: In `data/records/brushite.yaml` (`heveran2019`), `causal_graphs[0].nodes[2..3].description` and `causal_graphs[0].edges[0..2]` retained generic template descriptions, depicted brushite as formed via ureolytic alkalinization (`supports: support`) rather than precipitating initially (including in cell-free and nonureolytic *E. coli* HB101 controls, Figure 2D-E) and being replaced in bulk XRD by calcite as pH rises and dissolved phosphorus returns to solution (`supports: partial`), interpolated capitalized node labels mid-sentence with singular verb `precipitates`, and cited `XRD/SEM-EDS` instead of XRD, SEM, Raman, and WDS.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[2..3].description` and `causal_graphs[0].edges[0..2]` in `data/records/brushite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`), setting `edges[1..2].evidence[0].supports: partial` and citing XRD, SEM, Raman, and WDS.
  - Minted append-only `EDIT` history sidecar:
    - `history/records/brushite/2026-11-06T145838Z-marcin-6aaf13.yaml`

### 3. `GRP-C10S5-003` (`cmmmech-cycle10-stage4-finding-0003` -> Issue [#952](https://github.com/CultureBotAI/CMMMech/issues/952))
- **Root Cause**: In `data/records/strontianite.yaml` (`natalio2024`) and `data/records/smithsonite.yaml` (`huang2025`), `causal_graphs[0].nodes[2..3].description` and `causal_graphs[0].edges[0..2]` retained generic template descriptions repeating their capitalized labels in parentheses, stated `cation precipitation with carbonate/phosphate` on chloride-urea (`SrCl2`, `ZnCl2`) systems, interpolated capitalized node labels mid-sentence with `supports: support` on `edges[1]` despite absent matched-pH or urease-inhibition controls (`supports: partial`), and `smithsonite.yaml` `edges[2].evidence[0].explanation` cited `FTIR, SEM-EDS` not present in `huang2025`.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[2..3].description`, `causal_graphs[0].edges[0..2]`, and `causal_graphs[0].edges[2].relationship` (`cation precipitation with carbonate`) in `strontianite.yaml` and `smithsonite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`), setting `edges[1].evidence[0].supports: partial` and citing powder XRD (PDF 08-0449), AAS solution Zn removal, and Nessler/pH assays in `smithsonite.yaml`.
  - Minted append-only `EDIT` history sidecars:
    - `history/records/strontianite/2026-11-06T145838Z-marcin-434527.yaml`
    - `history/records/smithsonite/2026-11-06T145838Z-marcin-350cd9.yaml`
