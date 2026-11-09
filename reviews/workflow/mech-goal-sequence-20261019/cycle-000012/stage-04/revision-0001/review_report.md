# Cycle 12 Stage 4 Record & Cohort Review Report (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `12`
- **Stage**: `4` (`record_review`)
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Frozen Inventory Revision**: `f145e25990270f79cb760bb68e900595df4d308c` (`main`)
- **Scope Frozen At**: `2026-11-09T20:30:09Z`
- **Previous Stage 4/5 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-05/revision-0001/evidence.yaml` (`sha256: 5b577d2c72d575efb32c022ae3bbda5835b1db7e0e66061d62b4647b41e05618`)
- **Skills Applied**:
  - `.claude/skills/review-yaml-category/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/cmmmech-evolve-workflow/SKILL.md`

## 1. Frozen Inventory Coverage Summary

All **703 / 703 eligible records** in `data/records/*.yaml` at frozen commit `f145e25990270f79cb760bb68e900595df4d308c` were reviewed across **6 disjoint `material_kind` cohort reviews**, **1 cross-cohort `causal_graphs` & `protein_examples` review (`191` records)**, and **3 single-record deep-dive reviews** (`cmmmech:anatase`, `cmmmech:selenium`, `cmmmech:praseodymium`):

| Cohort (`material_kind`) | Population | Reviewed | With Criticality | With Mechanisms (Microbial / Abiotic-only; Total Mechs) | With `causal_graphs` (Graphs / Nodes / Edges) | `GENE_OR_PROTEIN` Nodes (`GROUNDED` / `UNGROUNDED`) | With `protein_examples` (Unique UniProtKB Accessions) | Open Findings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `element` | 66 | 66 (100%) | 64 | 63 (63 / 0; 66 mechs) | 31 (32 / 141 / 109) | 61 (58 / 3) | 30 (58) | 2 (`finding-0002`: `selenium`; `finding-0003`: `praseodymium`) |
| `mineral` | 452 | 452 (100%) | 0 | 285 (158 / 127; 343 mechs) | 84 (89 / 390 / 301) | 147 (144 / 3) | 82 (116) | 1 (`finding-0001`: `anatase`) |
| `mineral_group` | 7 | 7 (100%) | 0 | 7 (7 / 0; 7 mechs) | 5 (5 / 24 / 19) | 11 (11 / 0) | 5 (22) | 0 |
| `commodity` | 36 | 36 (100%) | 26 | 6 (6 / 0; 6 mechs) | 4 (4 / 18 / 14) | 6 (6 / 0) | 4 (6) | 1 (`finding-0003`: `rare-earth-element-commodities`) |
| `primary_resource` | 31 | 31 (100%) | 0 | 31 (29 / 2; 42 mechs) | 16 (17 / 82 / 65) | 34 (34 / 0) | 16 (46) | 0 |
| `secondary_resource` | 111 | 111 (100%) | 0 | 108 (85 / 23; 145 mechs) | 51 (54 / 258 / 204) | 102 (102 / 0) | 51 (43) | 0 |
| **Total (Disjoint Corpus)** | **703** | **703 (100%)** | **90** | **500 (348 / 152; 609 mechs)** | **191 (201 / 913 / 712)** | **361 (355 / 6)** | **188 (175 unique across corpus)** | **3 unique findings across 4 records** |

### Cycle 12 Stage 1–3 Additions & Cycle 11 Stage 5 Remediations Verified

1. **Cycle 11 Stage 5 Remediations (`PR #970`, commit `fa873bb0`)**:
   - Verified complete resolution of `cmmmech-cycle11-stage4-finding-0001` (`enstatite`, `olivine-group`, `dunite`), `cmmmech-cycle11-stage4-finding-0002` (`metacinnabar`), and `cmmmech-cycle11-stage4-finding-0003` (`scandium`).
2. **Cycle 12 Stage 1 Additions (`PR #972`, commit `7449fa912`)**:
   - Verified all 5 new Round 130 EJM critical-element mineral species records (`heimite` `IMA:2022-019`, `keutschite` `IMA:2014-038`, `spaltiite` `IMA:2014-012`, `tianhuixinite` `IMA:2022-081`, `zhenruite` `IMA:2022-050`).
3. **Cycle 12 Stage 2 & Stage 3 Causal-Graph & UniProtKB Grounding Expansions (`PR #974`, commit `122cb72c6`; `PR #976`, commit `f145e2599`)**:
   - Verified all 10 newly expanded records (`azurite`, `biotite`, `calcite`, `chernikovite`, `hematite`, `lizardite`, `meta-ankoleite`, `otavite`, `potassium-feldspar`, `strontium`), confirming 100% synchronization between `mechanisms[i].protein_examples` and `causal_graphs[j].nodes[k].protein_examples` (`11` grounded `GENE_OR_PROTEIN` nodes across `11` `causal_graphs` and `52` `protein_examples` spanning `39` unique verified UniProtKB accessions, including Stage 3 remediation of Issue `#977`).

## 2. Native Structured Review Bundles Persisted

| Review ID | Scope | Targets | `review.yaml` SHA-256 | `review.md` SHA-256 |
| --- | --- | ---: | --- | --- |
| `20261109T203000Z-cycle12-stage4-element-cohort-review` | `element` | 66 | `8ca225f2e9ea68552ccdf225e6fda79186d082929b0d8ef1c360f5507648a96a` | `50dcd3de8e88bab7506bf5458826d901f6a1b147ee9e0b7788d6588fb2f28629` |
| `20261109T203001Z-cycle12-stage4-mineral-cohort-review` | `mineral` | 452 | `d5adc1a3595573c5d7719856c647c1a428647705dc3e5ce65e13b5bb8d5b966d` | `104ec9859f55cdc16657af58e471116a1c407e373c7f23480f9bac1dac0e8b56` |
| `20261109T203002Z-cycle12-stage4-mineral-group-cohort-review` | `mineral_group` | 7 | `5ab5b2ba61fc9980cc77a5af854699cac01377b1c7e6cab2c5eaa294a1d85c0b` | `dbdfa0d87ab71fcc4273415436065b633afb99f6ecd2d51f50d5763c25906fa7` |
| `20261109T203003Z-cycle12-stage4-commodity-cohort-review` | `commodity` | 36 | `dd3847d45a2c6e88ac96c80e95078d3922e0a1dc1f060756fc2c3b2cf2b562f3` | `e51def639a4ebfa140a0cb99f32bf24e2d82c32552519799436c5910c3119c7e` |
| `20261109T203004Z-cycle12-stage4-primary-resource-cohort-review` | `primary_resource` | 31 | `8ee63aa5c37474fd8b5d1644858c9812e941cd0b32b0089bb2f1f15661907833` | `2caf8fd0c2037b6ea3070f592e517a2daa81fd6bb01124ee715aef06c3c6c77d` |
| `20261109T203005Z-cycle12-stage4-secondary-resource-cohort-review` | `secondary_resource` | 111 | `d003aab49afaf12455bddba04cc70b54feb4a61a935d04b399e6cce833c8444a` | `d0f86c662da0a26a232e2574281b4d9d6f900549131855a3c4de88f5555fffaf` |
| `20261109T203006Z-cycle12-stage4-causal-graphs-cohort-review` | `causal_graphs (cross-cohort)` | 191 | `7630520d8859ff7b51c0dd74eadbd874d1ba51a0b4469c10d815610c4f849432` | `0d0aa8bff3b9eca5f8e4020262aafdf21a386c27e03f9394bca86b5b8e6a64a1` |
| `20261109T203007Z-anatase-cycle12-stage4-record-review` | `record: cmmmech:anatase` | 1 | `36597335dd39329052e0ce5c3b34829f870fe4ea1954476d32444c66ce47175a` | `1b6432e21c5c5da266af61621cb770260b3775f45df7cbb33d8ae6b2797a4fac` |
| `20261109T203008Z-selenium-cycle12-stage4-record-review` | `record: cmmmech:selenium` | 1 | `0a071de4420cd38820062b9dc6936574ad5cc40f20e18ad7258da2e54ecee4e2` | `b505e20ef4836d3113c96115ffa7eb018d444f99a93222f7945963b760e9cead` |
| `20261109T203009Z-praseodymium-cycle12-stage4-record-review` | `record: cmmmech:praseodymium` | 1 | `0ff64c228cd91b054e97d9cf1408013dcdea12f897a388f6e63980d4fcbcec70` | `a3130559b4224381b95b3e4c33aaf16f6bfa8658d645c44e35d5415c2891b4c8` |

## 3. Open Findings Preserved for Stage 5 Grouped Remediation (`carry_forward_ids`)

1. **`cmmmech-cycle12-stage4-finding-0001`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.ping2016-anatase.construct-control-discrepancy-and-abbreviated-graph-evidence`
   - **Target Records (1)**: `cmmmech:anatase` (`data/records/anatase.yaml`)
   - **Summary**: In `data/records/anatase.yaml` (Ping et al. 2016, *Chemical Science* 7:6330-6336, `ping2016`), `mechanisms[0].protein_examples[0..1]`, `causal_graphs[0].nodes[0..1].protein_examples[0]`, and `causal_graphs[0].edges[0..1]` name `'pET28a-INP-silaffin'` and state that `'non-engineered E. coli controls were not included'`, contradicting `mechanisms[0].context` (`pET(INP-nR5)` with `n = 1, 3, 5` R5 repeats in *E. coli* BL21(DE3)) and `mechanisms[0].evidence[2]` (which documents that INP-only comparator cells were tested in Figures S2 and S4b, while matched cell-free precursor controls and live-vs-killed comparisons were omitted); additionally, `nodes[1].description`, `nodes[3].description`, and `edges[0,2]` omit the proposed-mechanism caveat (Figures 1d, 3d, 5), the 37 C / 80 C / 600 C (air vs argon anatase-carbon composite) stages, the PDF `21-1271` vs `21-1272` reference-card discrepancy, and `supports: partial` polarity.
2. **`cmmmech-cycle12-stage4-finding-0002`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.li2014-selenium-mr1.abbreviated-graph-evidence-and-localization-catalysis-qualifications`
   - **Target Records (1)**: `cmmmech:selenium` (`data/records/selenium.yaml`)
   - **Summary**: In `data/records/selenium.yaml` (Li et al. 2014, *Scientific Reports* 4:3735, `li_2014` / `li_2014_supplement`; Klonowska et al. 2005, `klonowska_2005`), `causal_graphs[0]` (`mr1_fcca_cyma_selenite_reduction_graph`) and `protein_examples[0..1]` (`UniProtKB:P83223` FccA, `UniProtKB:Q8E8S0` CymA) use abbreviated 75–90 char descriptions/explanations and `supports: support` polarity stating direct periplasmic FccA catalysis and periplasmic/cell-envelope Se(0) accumulation, omitting the conditional deletion kinetics (`0.54 +/- 0.13` vs `1.35 +/- 0.05` umol/h in Figure 2), absence of complementation or purified-FccA assays, substantial residual reduction in `delta-cymA` (Figure 4; `klonowska_2005`), and predominantly intracellular plus smaller surface particle distribution (Figure 5 TEM/EDX and 48 h Se 3d XPS; Table 1 ICP-AES balance).
3. **`cmmmech-cycle12-stage4-finding-0003`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.diep2026-mattocks2023-lanmodulin-graphs.abbreviated-edge-evidence-and-batch-dimer-qualifications`
   - **Target Records (2)**: `cmmmech:praseodymium` (`data/records/praseodymium.yaml`), `cmmmech:rare-earth-element-commodities` (`data/records/rare-earth-element-commodities.yaml`)
   - **Summary**: In `data/records/praseodymium.yaml` (`diep2026`, `melba_mex_lanm_pr_la_separation_graph`), `nodes[2..3]` and `edges[0..2]` carry 77–87 char strings and `supports: support` on `edges[0,2]` omitting the 0.8 mL column / 0.4 mM Pr + 0.4 mM La feed / pH 2.4 -> 1.5 single-run Figure 6d result (`99.97 mol%` Pr purity, `83.16%` summed-eluate recovery across bed volumes 48–80) versus the triplicate 0.4 mL repeat columns at pH 2.5 -> 1.5 (`96.5 +/- 0.2 mol%` purity, `72.0 +/- 5.8%` yield across fractions 53–93 in Extended Data Figure 8d) and Mex-LanM co-elution; in `data/records/rare-earth-element-commodities.yaml` (`mattocks_2023`, `hans_lanm_r100k_nd_dy_separation_graph`), `protein_examples[0]` and `edges[0..2]` omit the Page 92 / Extended Data Figure 6 immobilized-dimer minority and bare-agarose control caveats (`supports: partial`), the Extended Data Figure 6 wild-type Hans-LanM comparison (`83.6%` Dy purity / `98.1%` yield; `99.8%` Nd purity / `98.5%` yield), and the `mattocks_2023_fig4_data` summed-eluate yield denominator and Table S16 vs workbook Nd SD discrepancy (`4.4` vs `~15.1942`).
