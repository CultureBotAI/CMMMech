# Cycle 13 Stage 4 Record & Cohort Review Report (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `13`
- **Stage**: `4` (`record_review`)
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Frozen Inventory Revision**: `01de2d17fc49adec7f67da17266cbc82713d0df1` (`main`)
- **Scope Frozen At**: `2026-11-10T08:50:09Z`
- **Previous Stage 4/5 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-05/revision-0001/evidence.yaml` (`sha256: 2914481bc70e6120582b09b1393ba3d6ae195428120e1220ffde55a4ecfd0c70`)
- **Skills Applied**:
  - `.claude/skills/review-yaml-category/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/cmmmech-evolve-workflow/SKILL.md`

## 1. Frozen Inventory Coverage Summary

All **708 / 708 eligible records** in `data/records/*.yaml` at frozen commit `01de2d17fc49adec7f67da17266cbc82713d0df1` were reviewed across **6 disjoint `material_kind` cohort reviews**, **1 cross-cohort `causal_graphs` & `protein_examples` review (`201` records)**, and **3 single-record deep-dive reviews** (`cmmmech:akaganeite`, `cmmmech:hydroxylapatite`, `cmmmech:neodymium`):

| Cohort (`material_kind`) | Population | Reviewed | With Criticality | With Mechanisms (Microbial / Abiotic-only; Total Mechs) | With `causal_graphs` (Graphs / Nodes / Edges) | `GENE_OR_PROTEIN` Nodes (`GROUNDED` / `UNGROUNDED`) | With `protein_examples` (Unique UniProtKB Accessions) | Open Findings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `element` | 66 | 66 (100%) | 64 | 63 (63 / 0; 66 mechs) | 33 (34 / 151 / 117) | 65 (62 / 3) | 32 (66) | 1 (`finding-0003`: `neodymium`) |
| `mineral` | 457 | 457 (100%) | 0 | 285 (158 / 127; 343 mechs) | 91 (97 / 421 / 324) | 159 (154 / 5) | 89 (132) | 2 (`finding-0001`: `akaganeite`; `finding-0002`: `hydroxylapatite`) |
| `mineral_group` | 7 | 7 (100%) | 0 | 7 (7 / 0; 7 mechs) | 5 (5 / 24 / 19) | 11 (11 / 0) | 5 (22) | 0 |
| `commodity` | 36 | 36 (100%) | 26 | 6 (6 / 0; 6 mechs) | 4 (4 / 18 / 14) | 6 (6 / 0) | 4 (6) | 0 |
| `primary_resource` | 31 | 31 (100%) | 0 | 31 (29 / 2; 42 mechs) | 16 (17 / 82 / 65) | 34 (34 / 0) | 16 (46) | 1 (`finding-0003`: `allanite-concentrate`) |
| `secondary_resource` | 111 | 111 (100%) | 0 | 108 (85 / 23; 145 mechs) | 52 (55 / 263 / 208) | 104 (104 / 0) | 52 (47) | 1 (`finding-0003`: `fluorescent-lamp-phosphor`) |
| **Total (Disjoint Corpus)** | **708** | **708 (100%)** | **90** | **500 (348 / 152; 609 mechs)** | **201 (212 / 959 / 747)** | **379 (371 / 8)** | **198 (203 unique across corpus)** | **3 unique findings across 5 records** |

### Cycle 13 Stage 1–3 Additions & Cycle 12 Stage 5 Remediations Verified

1. **Cycle 12 Stage 5 Remediations (`PR #983`, commit `c18dd8dd6`)**:
   - Verified complete resolution of `cmmmech-cycle12-stage4-finding-0001` (`anatase`), `cmmmech-cycle12-stage4-finding-0002` (`selenium`), and `cmmmech-cycle12-stage4-finding-0003` (`praseodymium`, `rare-earth-element-commodities`).
2. **Cycle 13 Stage 1 Additions (`PR #985`, commit `3bc89f7ae`)**:
   - Verified all 5 new Round 131 EJM critical-element mineral species records (`delchiaroite` `IMA:2025-076`, `heimaeyite` `IMA:2023-127a`, `jonlarsenite` `IMA:2024-078a`, `marioantofilliite` `IMA:2025-012`, `nannoniite` `IMA:2024-010`).
3. **Cycle 13 Stage 2 & Stage 3 Causal-Graph & UniProtKB Grounding Expansions (`PR #988`, commit `4bdd13ae9`; `PR #989`, commit `01de2d17f`)**:
   - Verified all 10 newly expanded records (`bismuth`, `chromium-tanned-leather-shavings`, `greenockite`, `hawleyite`, `cadmium`, `monohydrocalcite`, `cuprite`, `atacamite`, `brochantite`, `kaolinite`), confirming 100% synchronization between `mechanisms[i].protein_examples` and `causal_graphs[j].nodes[k].protein_examples` (`18` `GENE_OR_PROTEIN` nodes: `16` `GROUNDED` and `2` `UNGROUNDED` across `11` `causal_graphs` and `44` `protein_examples` spanning `28` unique verified UniProtKB accessions).

## 2. Native Structured Review Bundles Persisted

| Review ID | Scope | Targets | `review.yaml` SHA-256 | `review.md` SHA-256 |
| --- | --- | ---: | --- | --- |
| `20261110T085000Z-cycle13-stage4-element-cohort-review` | `element` | 66 | `00fcb14136cd76aed527916af32049f6620097601b71d7dba9cbc4cbed04abaf` | `084d2591e269e757686c670caafa91cd3e64c310ceb2dddd0527df7a73cd9b6b` |
| `20261110T085001Z-cycle13-stage4-mineral-cohort-review` | `mineral` | 457 | `78162a59fa0d80d94323b11e996fb248ab287d97c543cb2eda19d82ac2e827f1` | `5034c042fa8770cf9559197e2c10197b63458d48fe573c0f082107d4e512e1e7` |
| `20261110T085002Z-cycle13-stage4-mineral-group-cohort-review` | `mineral_group` | 7 | `1d2171cbdfbbcec2ba355676dd92e475a679b15133a2ac702f6bf067d44ee7de` | `790185e240c0324eb803eda2c92174c340d36f0c4162aa6366ca884e5308837d` |
| `20261110T085003Z-cycle13-stage4-commodity-cohort-review` | `commodity` | 36 | `ff50c8c687c41953fcf60dec166ac29461cc391554f06bedd66bc6e284a917e0` | `cdcdb445ca478461938dfc7c8370340c43af22edca5979609d402e4d8a530414` |
| `20261110T085004Z-cycle13-stage4-primary-resource-cohort-review` | `primary_resource` | 31 | `eccff1c0a51778360e4fe0482553b372afb42d9fde3b15e853262d7f19ec4b65` | `29f88583942edefa797712b319d16c5676ec0f4023366cb24229b5483ce9d919` |
| `20261110T085005Z-cycle13-stage4-secondary-resource-cohort-review` | `secondary_resource` | 111 | `657972b8bb37adb5ef0cf044d31ef54e9dda81fd02dfeaf2978e25443d95ec37` | `3038f2163412d8e87e9360e58c2b2458beab2c53bbf8c845784d62f0d8bb59f3` |
| `20261110T085006Z-cycle13-stage4-causal-graphs-cohort-review` | `causal_graphs (cross-cohort)` | 201 | `6f428ba2765ebdb1c1b7b1be64366fad7b7fbbe549daa72cec2801cc8330fdf3` | `34303307120c75d21da5696134282012bbf3b20cb6d3fbc536ee4f05622febad` |
| `20261110T085007Z-akaganeite-cycle13-stage4-record-review` | `record: cmmmech:akaganeite` | 1 | `53d59d55baa33198e44e0dec50929dfd685b51123cff4df616aa7178ce394041` | `7490ce47bb3d6014b515042094d22778dd53e7b8487683fa43f70bf3f9a30869` |
| `20261110T085008Z-hydroxylapatite-cycle13-stage4-record-review` | `record: cmmmech:hydroxylapatite` | 1 | `780b16b03b0d7a7fd91dd6786c601aaa2c1d1eba64157d6baeb56a730e7e6aff` | `9ce9664d5c961d2388056e3580387d3084af65b1f29fa829b8e3037f66c62625` |
| `20261110T085009Z-neodymium-cycle13-stage4-record-review` | `record: cmmmech:neodymium` | 1 | `b412316d99d8a85c47813f342c41a7c88e3ea74d1386f5d78c95b2a927b0f4fc` | `cd3f5a683428f9c78764c8fc7d7afee6e722ade520d11dacf4820016093d62d7` |

## 3. Open Findings Preserved for Stage 5 Grouped Remediation (`carry_forward_ids`)

1. **`cmmmech-cycle13-stage4-finding-0001`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.levar2017-akaganeite.abbreviated-graph-nodes-edges-and-redox-complementation-qualifications`
   - **Target Records (1)**: `cmmmech:akaganeite` (`data/records/akaganeite.yaml`)
   - **Summary**: In `data/records/akaganeite.yaml` (Levar et al. 2017, *ISME Journal* 11:741-752, `levar_2017`), `mechanisms[0].protein_examples[0..1]` (`UniProtKB:Q747K6` ImcH, `UniProtKB:Q74GH2` CbcL), `causal_graphs[0].nodes[0..1].protein_examples[0]`, `causal_graphs[0].nodes[3..4].description`, and `causal_graphs[0].edges[0..3]` use abbreviated 51–103 char descriptions/explanations and `supports: support` polarity that omit unmeasured akaganeite redox potential (Figure 1 soluble Fe(III)-citrate potentials vs akaganeite), cited-only complementation and absence of purified-protein assays, unquantified initial akaganeite Fe loading, and 0.5 N HCl extraction (`>=24 h` at 23–25 C before ferrozine) scope.
2. **`cmmmech-cycle13-stage4-finding-0002`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.zorzetto2023-hydroxylapatite.abbreviated-graph-nodes-edges-and-fixed-biofilm-control-qualifications`
   - **Target Records (1)**: `cmmmech:hydroxylapatite` (`data/records/hydroxylapatite.yaml`)
   - **Summary**: In `data/records/hydroxylapatite.yaml` (Zorzetto et al. 2023, *Chemistry of Materials* 35:2762-2772, `zorzetto_2023` / `zorzetto_2023_si`), `causal_graphs[0]` (`w3110_phoa_biofilm_hydroxyapatite_graph`) `nodes[0..2].description` and `edges[0..1]` use abbreviated 88–108 char strings and `supports: support` on `edges[1]`, omitting `P-Ca 10:10` and `10:1` salt-free LB agar conditions, 4% PFA/PBS-fixed biofilm mineralization (Figure S9, Table S10), 20 mM L-glutathione (Figure 4A, Figure S7) and pH 10.4 purified-ALP (Figure 4B) control limits, and WAXS phase-occupancy/yield caveats.
3. **`cmmmech-cycle13-stage4-finding-0003`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.schmitz-marecos-gluconobacter-graphs.template-pqqc-gdh-nodes-edges-and-relative-denominator-qualifications`
   - **Target Records (3)**: `cmmmech:allanite-concentrate` (`data/records/allanite-concentrate.yaml`), `cmmmech:fluorescent-lamp-phosphor` (`data/records/fluorescent-lamp-phosphor.yaml`), `cmmmech:neodymium` (`data/records/neodymium.yaml`)
   - **Summary**: Across `allanite-concentrate.yaml` (`schmitz2025`), `fluorescent-lamp-phosphor.yaml` (`schmitz2021`), and `neodymium.yaml` (`marecos2025`), *Gluconobacter oxydans* B58 `protein_examples` (`UniProtKB:Q9L3B2` PqqC, `UniProtKB:P27175` Gdh, `UniProtKB:Q5FT13` PstC, `UniProtKB:Q5FQK7` GOX1598) and `causal_graphs[0]` nodes/edges retain generic 72–130 char template descriptions and `supports: support` polarity omitting 621H reference-proteome (`UP000006375`) proxy grounding for strain B58, residual `mgdh`/`pqqC` mutant leaching (Figure 4D in `schmitz2021`) and non-pH mutant effects (`9 of 12` mutants in `marecos2025`; unresolved concentration vs composition in `schmitz2025`), relative-over-wild-type vs absolute-recovery denominators (`53.1%`/`73.1%` in `schmitz2025`; `~111%` in `marecos2025`; literature-based `4.7%`/`5.5%` phosphor denominator in `schmitz2021`), and study-specific timing/control caveats.
