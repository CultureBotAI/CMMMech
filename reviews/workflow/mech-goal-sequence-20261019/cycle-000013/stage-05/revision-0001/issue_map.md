# Cycle 13 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `13`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Frozen Predecessor Commit (`source_revision`)**: `eda4d51de595671d30cf55438a0724bb087c923b`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml` (`sha256: 297254433f266a44507f83c259b937a8105d8923675bffee143d6044311c898e`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261110T165200Z-cycle13-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GRP-C13S5-001` | `cmmmech-cycle13-stage4-finding-0001` | [#991](https://github.com/CultureBotAI/CMMMech/issues/991) | `cmmmech:akaganeite` | `resolved` |
| `GRP-C13S5-002` | `cmmmech-cycle13-stage4-finding-0002` | [#992](https://github.com/CultureBotAI/CMMMech/issues/992) | `cmmmech:hydroxylapatite` | `resolved` |
| `GRP-C13S5-003` | `cmmmech-cycle13-stage4-finding-0003` | [#993](https://github.com/CultureBotAI/CMMMech/issues/993) | `cmmmech:allanite-concentrate`, `cmmmech:fluorescent-lamp-phosphor`, `cmmmech:neodymium` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C13S5-001` (`cmmmech-cycle13-stage4-finding-0001` -> Issue [#991](https://github.com/CultureBotAI/CMMMech/issues/991))
- **Root Cause**: In `data/records/akaganeite.yaml` (`cutting_2009`), `mechanisms[0].protein_examples[0..1]` (`UniProtKB:Q747K6` ImcH, `UniProtKB:Q74GH2` CbcL), `causal_graphs[0].nodes[0..1]`, and `causal_graphs[0].edges[0..3]` asserted `supports: support` with generic inner-membrane cytochrome prose, omitting that Cutting et al. (2009) used wild-type *Geobacter sulfurreducens* PCA with exogenously added `10 microM` AQDS without genetic, proteomic, or transcriptomic assays of ImcH or CbcL, and omitting the secondary goethite (~14%) alongside magnetite (~86%) and dissolution-reprecipitation caveats already documented in `mechanisms[0].evidence[1]`.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0..1]`, `causal_graphs[0].nodes[0..1].protein_examples[0]`, `causal_graphs[0].nodes[0..4].description`, and `causal_graphs[0].edges[0..3]` (with `supports: partial` on all 4 edges and both protein examples) in `data/records/akaganeite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/akaganeite/2026-11-10T165144Z-marcin-7c5a6c.yaml`

### 2. `GRP-C13S5-002` (`cmmmech-cycle13-stage4-finding-0002` -> Issue [#992](https://github.com/CultureBotAI/CMMMech/issues/992))
- **Root Cause**: In `data/records/hydroxylapatite.yaml` (`antonijevic2023`), `causal_graphs[0]` described the substrate and edges as `supports: support` dissolution of `'Finely ground (<37 um) hydroxylapatite mineral feed'`, whereas `mechanisms[0].evidence[1]` (`supports: partial`) notes that Antonijevic et al. (2023) leached natural Tunisian Gafsa sedimentary phosphorite ore (~27.7 wt% P2O5, dominated by carbonate-fluorapatite/francolite with carbonate and quartz gangue) rather than phase-pure hydroxylapatite.
- **Remediation**:
  - Updated `causal_graphs[0].description`, `causal_graphs[0].nodes[0..2].description`, and `causal_graphs[0].edges[0..1]` (with `supports: partial` on both edges) in `data/records/hydroxylapatite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/hydroxylapatite/2026-11-10T165144Z-marcin-7f0203.yaml`

### 3. `GRP-C13S5-003` (`cmmmech-cycle13-stage4-finding-0003` -> Issue [#993](https://github.com/CultureBotAI/CMMMech/issues/993))
- **Root Cause**: In `data/records/allanite-concentrate.yaml` (`schmitz2021`), `data/records/fluorescent-lamp-phosphor.yaml` (`schmitz2021`), and `data/records/neodymium.yaml` (`marecos2025`, `marecos2025_data4`), *Gluconobacter oxydans* B58 `protein_examples` and `causal_graphs[0]` edges used `supports: support` with generic explanations that omitted: (1) proxy grounding of B58 loci (`mgdh`, `pqqC`, `pstC`, `GO_1598`, `GO_1096`) to the *G. oxydans* 621H reference proteome (`UP000006375`, `NCBITaxon:290633`); (2) residual REE leaching by `mgdh` and `pqqC` disruption mutants in Schmitz et al. (2021) Fig. 4D and the hypothesized status of `pstC` phosphate-sensing derepression; (3) the 9 of 12 selected B58 disruption strains in Marecos et al. (2025) that altered Mon2 Nd extraction without significant pH shifts; and (4) relative-over-wild-type (`11%`, `18%`, `56-111%`) versus absolute-recovery denominators and study-specific timing/control caveats.
- **Remediation**:
  - Updated `protein_examples` and `causal_graphs[0]` nodes/edges to `supports: partial` with study-specific prose across `data/records/allanite-concentrate.yaml`, `data/records/fluorescent-lamp-phosphor.yaml`, and `data/records/neodymium.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/allanite-concentrate/2026-11-10T165144Z-marcin-b31f32.yaml`
    - `history/records/fluorescent-lamp-phosphor/2026-11-10T165144Z-marcin-daa0d7.yaml`
    - `history/records/neodymium/2026-11-10T165144Z-marcin-3d1c04.yaml`
