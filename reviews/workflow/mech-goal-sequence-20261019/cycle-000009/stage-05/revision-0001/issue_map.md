# Cycle 9 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `9`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Remediated Commit (`source_revision`)**: `7f671e363396cc864fc13d5461717c56d16b4aee`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml`
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261105T234500Z-cycle9-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GRP-C9S5-001` | `cmmmech-cycle9-stage4-finding-0001` | [#940](https://github.com/CultureBotAI/CMMMech/issues/940) | `cmmmech:uranium`, `cmmmech:vanadium` | `resolved` |
| `GRP-C9S5-002` | `cmmmech-cycle9-stage4-finding-0002` | [#941](https://github.com/CultureBotAI/CMMMech/issues/941) | `cmmmech:rhodochrosite`, `cmmmech:chlorite` | `resolved` |
| `GRP-C9S5-003` | `cmmmech-cycle9-stage4-finding-0003` | [#942](https://github.com/CultureBotAI/CMMMech/issues/942) | `cmmmech:asbolane`, `cmmmech:feitknechtite`, `cmmmech:pyrochroite` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C9S5-001` (`cmmmech-cycle9-stage4-finding-0001` -> Issue [#940](https://github.com/CultureBotAI/CMMMech/issues/940))
- **Root Cause**: `data/records/uranium.yaml` (`mr1_bes_uranium_reduction_graph`) and `data/records/vanadium.yaml` (`mr1_bes_vanadium_reduction_graph`) retained generic template descriptions on `oxidized_metal_substrate` and `reduced_metal_product` and capitalized mid-sentence node labels with generic one-line explanations on `edges[1..3]`; in addition, `uranium.yaml` labeled `reduced_metal_product` `'Cell-associated reduced U(IV) precipitate'` with `supports: support` on `edges[3]` despite unverified solid valence/phase and abiotic U removal in `kane_2026_bes`.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[3..4]` and `causal_graphs[0].edges[1..3]` in `data/records/uranium.yaml` and `data/records/vanadium.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`), qualifying `reduced_metal_product` in `uranium.yaml` as `'Depleted aqueous U and carbon-felt electrode-associated uranium deposits (unverified solid valence and phase)'` and `edges[3].evidence[0].supports: partial`.
  - Minted append-only `EDIT` history sidecars:
    - `history/records/uranium/2026-11-05T234652Z-marcin-a1c586.yaml`
    - `history/records/uranium/2026-11-06T003438Z-marcin-a0558b.yaml`
    - `history/records/vanadium/2026-11-05T234652Z-marcin-a29b5f.yaml`
    - `history/records/vanadium/2026-11-06T003438Z-marcin-12e729.yaml`

### 2. `GRP-C9S5-002` (`cmmmech-cycle9-stage4-finding-0002` -> Issue [#941](https://github.com/CultureBotAI/CMMMech/issues/941))
- **Root Cause**: `data/records/rhodochrosite.yaml` (`mr1_mn_oxide_rhodochrosite_graph`) retained generic template wrappers on `nodes[3..4]`, stated `'in Ca-free artificial freshwater medium'` instead of the 1 L modified M1 medium (`~6.3 mM` colloidal MnO2, `20 mM` lactate, no added phosphate, pH 8 under N2) from Johnson et al. (2016) Methods pp. C-D, and interpolated capitalized node labels mid-sentence on `edges[1..3]`; `data/records/chlorite.yaml` (`mr1_chlorite_fe_reduction_graph`) similarly interpolated capitalized `'Chlorite-associated Fe(III) (ferroan clinochlore)'` mid-sentence with generic one-line explanations on `edges[1..2]`.
- **Remediation**:
  - Updated `causal_graphs[0].nodes[3..4]` and `causal_graphs[0].edges[1..3]` in `data/records/rhodochrosite.yaml` and `causal_graphs[0].edges[1..2]` in `data/records/chlorite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/rhodochrosite/2026-11-05T234652Z-marcin-d651e4.yaml`
    - `history/records/chlorite/2026-11-05T234653Z-marcin-12e7f2.yaml`
    - `history/records/chlorite/2026-11-06T003438Z-marcin-5a1086.yaml`

### 3. `GRP-C9S5-003` (`cmmmech-cycle9-stage4-finding-0003` -> Issue [#942](https://github.com/CultureBotAI/CMMMech/issues/942))
- **Root Cause**: Across `data/records/asbolane.yaml`, `data/records/feitknechtite.yaml`, and `data/records/pyrochroite.yaml` (Buchanan 2021/2022 Chapter 4), `causal_graphs[0].nodes[2..3]` repeated their capitalized node labels in parenthetical template descriptions and `causal_graphs[0].description` and `causal_graphs[0].edges[0].description` interpolated those capitalized node labels mid-sentence.
- **Remediation**:
  - Updated `causal_graphs[0].description`, `causal_graphs[0].nodes[2..3].description`, and `causal_graphs[0].edges[0].description` across `asbolane.yaml`, `feitknechtite.yaml`, and `pyrochroite.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/asbolane/2026-11-05T234941Z-marcin-37607c.yaml`
    - `history/records/feitknechtite/2026-11-05T234942Z-marcin-11de3e.yaml`
    - `history/records/pyrochroite/2026-11-05T234942Z-marcin-a5f660.yaml`
