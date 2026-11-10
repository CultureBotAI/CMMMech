# Cycle 12 Stage 5 Issue Map & Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `12`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Frozen Predecessor Commit (`source_revision`)**: `7fcb2a9fde66904e6274a675769cdbfe608cfa33`
- **Predecessor Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/evidence.yaml` (`sha256: 980b60dfc4f33d1c1c2f8590cae92fecd954fe811cedeb3896b3d7eb5020e5eb`)
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261109T231500Z-cycle12-stage5-remediation-verification/review.yaml` (`verdict: pass`, `0` open findings)

## Grouped Remediation Summary

| Group ID | Finding ID | GitHub Issue | Target Records | Status |
| :--- | :--- | :--- | :--- | :--- |
| `GRP-C12S5-001` | `cmmmech-cycle12-stage4-finding-0001` | [#980](https://github.com/CultureBotAI/CMMMech/issues/980) | `cmmmech:anatase` | `resolved` |
| `GRP-C12S5-002` | `cmmmech-cycle12-stage4-finding-0002` | [#981](https://github.com/CultureBotAI/CMMMech/issues/981) | `cmmmech:selenium` | `resolved` |
| `GRP-C12S5-003` | `cmmmech-cycle12-stage4-finding-0003` | [#982](https://github.com/CultureBotAI/CMMMech/issues/982) | `cmmmech:praseodymium`, `cmmmech:rare-earth-element-commodities` | `resolved` |

## Detailed Finding Dispositions

### 1. `GRP-C12S5-001` (`cmmmech-cycle12-stage4-finding-0001` -> Issue [#980](https://github.com/CultureBotAI/CMMMech/issues/980))
- **Root Cause**: In `data/records/anatase.yaml` (`ping2016`), `mechanisms[0].protein_examples[0..1]` (`UniProtKB:P06620` InaZ and `UniProtKB:Q9SE35` Sil1), `causal_graphs[0].nodes[0..1].protein_examples[0]`, and `causal_graphs[0].edges[0..1]` named `'pET28a-INP-silaffin'` and stated that `'non-engineered E. coli controls were not included'`, contradicting `mechanisms[0].context` (`pET(INP-nR5)` with `n = 1, 3, or 5` R5 repeats in *E. coli* BL21(DE3)) and `mechanisms[0].evidence[2]` (INP-only comparator cells tested in Supporting Figures S2 and S4b, while matched cell-free precursor and live-vs-killed controls were omitted); additionally, `nodes[1,3]` and `edges[0,2]` omitted proposed-mechanism (Figures 1d, 3d, 5), 37 °C / 80 °C / 600 °C air-vs-argon, and PDF `21-1271` vs `21-1272` qualifications and asserted `supports: support` on `edges[0]` and `edges[2]`.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0..1]`, `causal_graphs[0].nodes[0..1].protein_examples[0]`, `causal_graphs[0].nodes[0,1,3].description`, and `causal_graphs[0].edges[0..2]` (with `supports: partial` on `edges[0..2]`) in `data/records/anatase.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/anatase/2026-11-09T231311Z-marcin-bf64d4.yaml`

### 2. `GRP-C12S5-002` (`cmmmech-cycle12-stage4-finding-0002` -> Issue [#981](https://github.com/CultureBotAI/CMMMech/issues/981))
- **Root Cause**: In `data/records/selenium.yaml` (`li_2014`, `li_2014_supplement`, `klonowska_2005`), `causal_graphs[0]` and `protein_examples[0..1]` (`UniProtKB:P83223` FccA, `UniProtKB:Q8E8S0` CymA) used abbreviated 75–90 char explanations and `supports: support` polarity stating direct periplasmic FccA catalysis and periplasmic/cell-envelope Se(0) accumulation, omitting conditional deletion kinetics (`0.54 +/- 0.13` vs `1.35 +/- 0.05` umol/h over 12 h in Figure 2, standard errors of triplicate cultures), 20 mM fumarate competition, absence of complementation or purified-FccA assays, substantial residual reduction in `delta-cymA` (Figure 4; `klonowska_2005`), and predominantly intracellular plus smaller surface particle localization (Figure 5 TEM/EDX and 48 h Se 3d XPS; Table 1 ICP-AES balance).
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0..2]`, `causal_graphs[0].nodes[0..2].protein_examples[0]`, `causal_graphs[0].nodes[0..4].description`, and `causal_graphs[0].edges[0..3]` (with `supports: partial` on `protein_examples[0..2]` and `edges[0..3]`) in `data/records/selenium.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecar:
    - `history/records/selenium/2026-11-09T231312Z-marcin-cdc7f2.yaml`

### 3. `GRP-C12S5-003` (`cmmmech-cycle12-stage4-finding-0003` -> Issue [#982](https://github.com/CultureBotAI/CMMMech/issues/982))
- **Root Cause**: In `data/records/praseodymium.yaml` (`diep2026`) and `data/records/rare-earth-element-commodities.yaml` (`mattocks_2023`, `mattocks_2023_si`, `mattocks_2023_fig4_data`), immobilized-lanmodulin column causal graphs retained abbreviated 71–119 char node/edge descriptions and `supports: support` explanations omitting 0.8 mL vs 0.4 mL repeat-column batch variance (Figure 6d `99.97 mol%` Pr purity / `83.16%` summed-eluate recovery across bed volumes 48–80 vs Extended Data Figure 8d `96.5 +/- 0.2 mol%` Pr purity / `72.0 +/- 5.8%` yield across fractions 53–93 in `diep2026`), Page 92 / Extended Data Figure 6 immobilized-dimer minority and wild-type Hans-LanM (`83.6%` Dy purity / `98.1%` yield; `99.8%` Nd purity / `98.5%` yield) and bare-agarose control caveats in `mattocks_2023`, and summed-eluate yield denominator / binary molar-share purity qualifications.
- **Remediation**:
  - Updated `mechanisms[0].protein_examples[0]`, `causal_graphs[0].nodes[1].protein_examples[0]`, `causal_graphs[0].nodes[2..3].description`, and `causal_graphs[0].edges[0..2]` (`supports: partial`) in `data/records/praseodymium.yaml` and `mechanisms[0].protein_examples[0..1]`, `causal_graphs[0].nodes[0..1].protein_examples[0]`, and `causal_graphs[0].edges[0..2]` (`supports: partial`) in `data/records/rare-earth-element-commodities.yaml` via `scripts/curate_causal_graphs.py` (`curate_record_file`).
  - Minted append-only `EDIT` history sidecars:
    - `history/records/praseodymium/2026-11-09T231312Z-marcin-a907c8.yaml`
    - `history/records/rare-earth-element-commodities/2026-11-09T231312Z-marcin-025f56.yaml`
