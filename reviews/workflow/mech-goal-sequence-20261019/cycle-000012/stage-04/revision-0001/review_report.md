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
| `element` | 66 | 66 (100%) | 64 | 63 (63 / 0; 66 mechs) | 31 (32 / 149 / 117) | 61 (58 / 3) | 30 (58) | 2 (`finding-0002`: `selenium`; `finding-0003`: `praseodymium`) |
| `mineral` | 452 | 452 (100%) | 0 | 285 (158 / 127; 343 mechs) | 84 (89 / 393 / 304) | 147 (144 / 3) | 82 (116) | 1 (`finding-0001`: `anatase`) |
| `mineral_group` | 7 | 7 (100%) | 0 | 7 (7 / 0; 7 mechs) | 5 (5 / 23 / 18) | 11 (11 / 0) | 5 (22) | 0 |
| `commodity` | 36 | 36 (100%) | 26 | 6 (6 / 0; 6 mechs) | 4 (4 / 16 / 12) | 6 (6 / 0) | 4 (6) | 1 (`finding-0003`: `rare-earth-element-commodities`) |
| `primary_resource` | 31 | 31 (100%) | 0 | 31 (29 / 2; 42 mechs) | 16 (17 / 80 / 63) | 34 (34 / 0) | 16 (46) | 0 |
| `secondary_resource` | 111 | 111 (100%) | 0 | 108 (85 / 23; 145 mechs) | 51 (54 / 252 / 198) | 102 (102 / 0) | 51 (43) | 0 |
| **Total (Disjoint Corpus)** | **703** | **703 (100%)** | **90** | **500 (348 / 152; 609 mechs)** | **191 (201 / 913 / 712)** | **361 (355 / 6)** | **188 (175 unique across corpus)** | **3 unique findings across 4 records** |

### Cycle 12 Stage 1–3 Additions & Cycle 11 Stage 5 Remediations Verified

1. **Cycle 11 Stage 5 Remediations (`PR #970`, commit `fa873bb0`)**:
   - Verified complete resolution of `cmmmech-cycle11-stage4-finding-0001` (`enstatite`, `olivine-group`, `dunite`), `cmmmech-cycle11-stage4-finding-0002` (`metacinnabar`), and `cmmmech-cycle11-stage4-finding-0003` (`scandium`).
2. **Cycle 12 Stage 1 Additions (`PR #972`, commit `d3b14981`)**:
   - Verified all 5 new Round 130 IMA mineral species records (`berthierine` `IMA:1959 s.p.`, `chamosite` `IMA:1962 s.p.`, `cronstedtite` `IMA:1821`, `fayalite` `IMA:1840`, `greenalite` `IMA:1903`).
3. **Cycle 12 Stage 2 & Stage 3 Causal-Graph & UniProtKB Grounding Expansions (`PR #974`, commit `0b494e98`; `PR #976`, commit `f145e259`)**:
   - Verified all 10 newly expanded records (`berthierine`, `chamosite`, `biotite`, `lizardite`, `meta-ankoleite`, `azurite`, `calcite`, `otavite`, `strontium`, `vaterite`), confirming 100% synchronization between `mechanisms[i].protein_examples` and `causal_graphs[j].nodes[k].protein_examples` (40 `GENE_OR_PROTEIN` nodes grounded across 28 unique verified UniProtKB accessions, including Stage 3 remediation of Issue `#977`).

## 2. Native Structured Review Bundles Persisted

| Review ID | Scope | Targets | `review.yaml` SHA-256 | `review.md` SHA-256 |
| --- | --- | ---: | --- | --- |
| `20261109T203000Z-cycle12-stage4-element-cohort-review` | `element` | 66 | `1e1109f56e9554eed13370b7ec4b5d3f7d3a2df15130c285ed75fc0df9732c7c` | `f9916b0a644aec882e5441049fe2d39a1a2ddd6e6833c69e4a7a2dba1091bc03` |
| `20261109T203001Z-cycle12-stage4-mineral-cohort-review` | `mineral` | 452 | `5af4d888f7f9adde4585efe5842db1dfb7fa9c73bba31cc095ee54ccd00aaadc` | `b1526c5fb55b096428ad0e8832e7a62ec3a591832bc602817970adce1fbd21b5` |
| `20261109T203002Z-cycle12-stage4-mineral-group-cohort-review` | `mineral_group` | 7 | `81c015792d3cb60257beafcace538bade46c1485796b069a3fd9d0121c4c6fe5` | `2b99c89f2b2659b5ae02d72b45beb682394e7b00f5b598da97eb237fec491020` |
| `20261109T203003Z-cycle12-stage4-commodity-cohort-review` | `commodity` | 36 | `9627aa42a7e152caaaebab7b8b9a908b576c3d9425bd3b29912d723aa9a215be` | `303f8e17b73b7ec781391915d322615f0ebf7044c61c71ac52310f46ef3d8b5f` |
| `20261109T203004Z-cycle12-stage4-primary-resource-cohort-review` | `primary_resource` | 31 | `7d829dd643893c7c5d114501e882c2a5dfe32699c276524ef3160741000d6823` | `935170c334d64a9e451a4529b45f863299980b7a974f11556bcd191716c1d618` |
| `20261109T203005Z-cycle12-stage4-secondary-resource-cohort-review` | `secondary_resource` | 111 | `881a9e6a5d89871f70c06569d41bc7d75030e67b741c66cbaf1994b046034baa` | `97bb5d7533ebcb7226311f1b82ca450f9efe0fe5d8bf5609da2b977bd77739f7` |
| `20261109T203006Z-cycle12-stage4-causal-graphs-cohort-review` | `causal_graphs (cross-cohort)` | 191 | `bfbab13879eb6fef272c319302ebeca51f9a251eed6c36281102bee22d8f5c9a` | `7faf42670b0f598207938bb1d454bc7d65b3920b095ac954f9f93022c8d7b1b2` |
| `20261109T203007Z-anatase-cycle12-stage4-record-review` | `record: cmmmech:anatase` | 1 | `36597335dd39329052e0ce5c3b34829f870fe4ea1954476d32444c66ce47175a` | `1b6432e21c5c5da266af61621cb770260b3775f45df7cbb33d8ae6b2797a4fac` |
| `20261109T203008Z-selenium-cycle12-stage4-record-review` | `record: cmmmech:selenium` | 1 | `0a071de4420cd38820062b9dc6936574ad5cc40f20e18ad7258da2e54ecee4e2` | `b505e20ef4836d3113c96115ffa7eb018d444f99a93222f7945963b760e9cead` |
| `20261109T203009Z-praseodymium-cycle12-stage4-record-review` | `record: cmmmech:praseodymium` | 1 | `3bad94d1108498300d5a05e29dea6382fbf2198728d4e04aa3f9755d37292233` | `4716fce0dc85651a3233672f38833176d466b886a4bc8bd9c793798b6d333b7e` |

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
