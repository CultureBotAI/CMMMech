# Cycle 13 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `13`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Frozen Predecessor Commit (`source_revision`)**: `eda4d51de595671d30cf55438a0724bb087c923b`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml` (`sha256: 297254433f266a44507f83c259b937a8105d8923675bffee143d6044311c898e`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261110T165200Z-cycle13-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | Stage 4 Issue Key | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `GRP-C13S5-001` | `cmmmech-cycle13-stage4-finding-0001` | `cmmmech.levar2017-akaganeite.abbreviated-graph-nodes-edges-and-redox-complementation-qualifications` | [#991](https://github.com/CultureBotAI/CMMMech/issues/991) (and [#995](https://github.com/CultureBotAI/CMMMech/issues/995)) | `cmmmech:akaganeite` | `resolved` |
| `GRP-C13S5-002` | `cmmmech-cycle13-stage4-finding-0002` | `cmmmech.zorzetto2023-hydroxylapatite.abbreviated-graph-nodes-edges-and-fixed-biofilm-control-qualifications` | [#992](https://github.com/CultureBotAI/CMMMech/issues/992) (and [#995](https://github.com/CultureBotAI/CMMMech/issues/995)) | `cmmmech:hydroxylapatite` | `resolved` |
| `GRP-C13S5-003` | `cmmmech-cycle13-stage4-finding-0003` | `cmmmech.schmitz-marecos-gluconobacter-graphs.template-pqqc-gdh-nodes-edges-and-relative-denominator-qualifications` | [#993](https://github.com/CultureBotAI/CMMMech/issues/993) (and [#995](https://github.com/CultureBotAI/CMMMech/issues/995)) | `cmmmech:allanite-concentrate`, `cmmmech:fluorescent-lamp-phosphor`, `cmmmech:neodymium` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C13S5-001` (`cmmmech-cycle13-stage4-finding-0001` -> Issue [#991](https://github.com/CultureBotAI/CMMMech/issues/991))
- **Root Cause**: In `data/records/akaganeite.yaml` (`levar_2017`, Levar et al. 2017 *ISME Journal* 11:741–752), `mechanisms[0].protein_examples[0..1]` (`UniProtKB:Q747K6` ImcH, `UniProtKB:Q74GH2` CbcL), `causal_graphs[0].nodes[0..4].description`, and `causal_graphs[0].edges[0..3]` used abbreviated one-sentence descriptions and `supports: support` polarity that omitted pH 6.8 vs 6.3 and 121 °C autoclaving phenotypes, inferred mineral redox potential vs Figure 1 soluble Fe(III)-citrate, cited-only complementation, unquantified initial akaganeite Fe loading, and 0.5 N HCl ferrozine extraction scope.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0..1]`, `causal_graphs[0].nodes[0..1].protein_examples[0]`, `causal_graphs[0].nodes[0..4].description`, and `causal_graphs[0].edges[0..3]` (with `supports: partial` on all 4 edges and both protein examples) in `data/records/akaganeite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/akaganeite/2026-11-10T174328Z-marcin-386d0d.yaml`

### 2. `GRP-C13S5-002` (`cmmmech-cycle13-stage4-finding-0002` -> Issue [#992](https://github.com/CultureBotAI/CMMMech/issues/992))
- **Root Cause**: In `data/records/hydroxylapatite.yaml` (`zorzetto_2023` / `zorzetto_2023_si`, Zorzetto et al. 2023 *Chemistry of Materials* 35:2762–2772), `causal_graphs[0]` (`w3110_phoa_biofilm_hydroxyapatite_graph`) used abbreviated 88–108 char node/edge descriptions and `supports: support` on `edges[1]`, omitting P-Ca 10:10 and 10:1 salt-free LB agar conditions, 4% PFA/PBS-fixed biofilm mineralization (Figure S9, Table S10), 20 mM L-glutathione (Figure 4A, Figure S7) and pH 10.4 purified-ALP (Figure 4B) control limits, and WAXS OH/F/Cl occupancy and yield caveats.
- **Remediation**:
  - Updated `causal_graphs[0].description`, `causal_graphs[0].nodes[0..2].description`, and `causal_graphs[0].edges[0..1]` (with `supports: partial` on both edges) in `data/records/hydroxylapatite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/hydroxylapatite/2026-11-10T174328Z-marcin-38f616.yaml`

### 3. `GRP-C13S5-003` (`cmmmech-cycle13-stage4-finding-0003` -> Issue [#993](https://github.com/CultureBotAI/CMMMech/issues/993))
- **Root Cause**: In `data/records/allanite-concentrate.yaml` (`schmitz2025`, Schmitz et al. 2025 *Communications Biology* 8:815), `data/records/fluorescent-lamp-phosphor.yaml` (`schmitz2021`, Schmitz et al. 2021 *Nature Communications* 12:6693), and `data/records/neodymium.yaml` (`marecos2025` / `marecos2025_data4`, Marecos et al. 2025 *Communications Biology* 8:682), *Gluconobacter oxydans* B58 `protein_examples` and `causal_graphs[0]` edges retained generic template descriptions and `supports: support` polarity that omitted: (1) proxy grounding of B58 loci (`mgdh`, `pqqC`, `pstC`, `pstS`, `GO_1598`, `GO_1096`) to the *G. oxydans* 621H reference proteome (`UP000006375`, `NCBITaxon:290633`); (2) residual REE leaching by `mgdh` and `pqqC` disruption mutants in Schmitz et al. (2021) Fig. 4D and hypothesized `pstC`/`pstS` pho-regulon regulation; (3) the 9 of 12 selected B58 disruption strains in Marecos et al. (2025) that altered Mon2 Nd extraction without significant pH shifts and unresolved concentration vs composition in Schmitz et al. (2025) Discussion; and (4) relative-over-wild-type (`53.1%`/`73.1%` in `schmitz2025`, `18%` / literature denominator in `schmitz2021`, `56–111%` in `marecos2025`) versus absolute-recovery denominators and study-specific timing/control caveats.
- **Remediation**:
  - Updated `protein_examples` and `causal_graphs[0]` nodes/edges to `supports: partial` with study-specific prose across `data/records/allanite-concentrate.yaml`, `data/records/fluorescent-lamp-phosphor.yaml`, and `data/records/neodymium.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/allanite-concentrate/2026-11-10T174328Z-marcin-a6b0be.yaml`
    - `history/records/fluorescent-lamp-phosphor/2026-11-10T165144Z-marcin-daa0d7.yaml`
    - `history/records/neodymium/2026-11-10T165144Z-marcin-3d1c04.yaml`
