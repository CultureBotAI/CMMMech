# Cycle 11 Stage 4 Record & Cohort Review Report (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `11`
- **Stage**: `4` (`record_review`)
- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Frozen Inventory Revision**: `794684703f77385b6e9bca32167f6c8d1e5e29bf` (`main`)
- **Scope Frozen At**: `2026-11-09T04:15:09Z`
- **Previous Stage 4/5 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-05/revision-0001/evidence.yaml` (`sha256: cd657ac93cf80c4fca8689814ba69985bdd7affe69ee6cc138a2f00907ef0c1b`)
- **Skills Applied**:
  - `.claude/skills/review-yaml-category/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/cmmmech-evolve-workflow/SKILL.md`

## 1. Frozen Inventory Coverage Summary

All **698 / 698 eligible records** in `data/records/*.yaml` at frozen commit `794684703f77385b6e9bca32167f6c8d1e5e29bf` were reviewed across **6 disjoint `material_kind` cohort reviews**, **1 cross-cohort `causal_graphs` & `protein_examples` review (`182` records)**, and **3 single-record deep-dive reviews** (`cmmmech:enstatite`, `cmmmech:metacinnabar`, `cmmmech:scandium`):

| Cohort (`material_kind`) | Population | Reviewed | With Criticality | With Mechanisms (Microbial / Abiotic-only; Total Mechs) | With `causal_graphs` (Graphs / Nodes / Edges) | `GENE_OR_PROTEIN` Nodes (`GROUNDED` / `UNGROUNDED`) | With `protein_examples` (Unique UniProtKB Accessions) | Open Findings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `element` | 66 | 66 (100%) | 64 | 63 (63 / 0; 66 mechs) | 30 (31 / 145 / 114) | 60 (57 / 3) | 29 (54) | 1 (`finding-0003`: `scandium`) |
| `mineral` | 447 | 447 (100%) | 0 | 285 (158 / 127; 343 mechs) | 78 (82 / 361 / 279) | 140 (137 / 3) | 76 (84) | 2 (`finding-0001`: `enstatite`; `finding-0002`: `metacinnabar`) |
| `mineral_group` | 7 | 7 (100%) | 0 | 7 (7 / 0; 7 mechs) | 3 (3 / 15 / 12) | 9 (9 / 0) | 3 (10) | 1 (`finding-0001`: `olivine-group`) |
| `commodity` | 36 | 36 (100%) | 26 | 6 (6 / 0; 6 mechs) | 4 (4 / 16 / 12) | 6 (6 / 0) | 4 (6) | 0 |
| `primary_resource` | 31 | 31 (100%) | 0 | 31 (29 / 2; 42 mechs) | 16 (17 / 80 / 63) | 34 (34 / 0) | 16 (46) | 1 (`finding-0001`: `dunite`) |
| `secondary_resource` | 111 | 111 (100%) | 0 | 108 (85 / 23; 145 mechs) | 51 (54 / 256 / 202) | 102 (102 / 0) | 51 (43) | 0 |
| **Total (Disjoint Corpus)** | **698** | **698 (100%)** | **90** | **500 (348 / 152; 609 mechs)** | **182 (191 / 873 / 682)** | **351 (345 / 6)** | **179 (139 unique across corpus)** | **3 unique findings across 5 records** |

### Cycle 11 Stage 1–3 Additions & Cycle 10 Stage 5 Remediations Verified

1. **Cycle 10 Stage 5 Remediations (`PR #953`, commit `09e04a33`, Issues `#950..#952`)**:
   - Verified complete resolution of `cmmmech-cycle10-stage4-finding-0001` (`calcite`, `vaterite`, `lithium-bearing-geothermal-brine`), `cmmmech-cycle10-stage4-finding-0002` (`brushite`), and `cmmmech-cycle10-stage4-finding-0003` (`strontianite`, `smithsonite`).
2. **Cycle 11 Stage 1 Additions (`PR #955`, commit `8287b17e`)**:
   - Verified all 5 new Round 129 IMA mineral species records (`belmonteite` `Bmt` `IMA:2024-039`, `dacostaite` `Dco` `IMA:2024-015`, `fluormacraeite` `Fmcr` `IMA:2024-054`, `macraeite` `Mcr` `IMA:2023-065`, `zhiqinite` `Zqn` `IMA:2024-037`).
3. **Cycle 11 Stage 2 & Stage 3 Causal-Graph & UniProtKB Grounding Expansions (`PR #960`, commit `df061de7`; `PR #963`, commit `79468470`)**:
   - Verified all 10 newly expanded records (`chukanovite`, `feroxyhyte`, `illite`, `lepidocrocite`, `manganite`, `palygorskite`, `plumbojarosite`, `silica-sand`, `thallium`, `titanium`), confirming 100% synchronization between `mechanisms[i].protein_examples` and `causal_graphs[j].nodes[k].protein_examples` (29 groundings per layer, 58 total across 15 unique UniProtKB accessions, including 7 newly introduced accessions `P94127`, `Q9Z4S6`, `Q934L0`, `B6YQ47`, `A4Y2B9`, `A4Y626`, `A4Y627`).

## 2. Native Structured Review Bundles Persisted

| Review ID | Scope | Targets | `review.yaml` SHA-256 | `review.md` SHA-256 |
| --- | --- | ---: | --- | --- |
| `20261109T041500Z-cycle11-stage4-element-cohort-review` | `element` | 66 | `ccdb372567d450adbe43f1b72e5cc03e1059fd8e0dea999943aa1b68686366a0` | `ce0255a434f9a603d2c2a537d4ec712b83a8130e5ae9b4337f0c7ef5ca692caa` |
| `20261109T041501Z-cycle11-stage4-mineral-cohort-review` | `mineral` | 447 | `5c5304870d843ec513230a0e29a41132bf07a4fdcf32319b6f5f61e5921e4e73` | `7cc8e20761e64f0171a35be48e372b20adc1598b47195d41ea8efce925f71e5c` |
| `20261109T041502Z-cycle11-stage4-mineral-group-cohort-review` | `mineral_group` | 7 | `e3142c2402af132d8e6a1ecf0bcdf4981321c03a2a491726dc4e6450bf36e5e2` | `8e640603ba9f5a666076a63c3dc10b5cb04020261bcee3d7ca2720965f28fc0f` |
| `20261109T041503Z-cycle11-stage4-commodity-cohort-review` | `commodity` | 36 | `4bce9cc76ddcd14e08428c207679ed893721b5b31932749931bb7cab7c71b127` | `12cf2aa52907971e47086c40cc1e31a51914eabd1e10fae795acd7a9e6ab4cc6` |
| `20261109T041504Z-cycle11-stage4-primary-resource-cohort-review` | `primary_resource` | 31 | `f799faaef2bf90c70023f89f4f4dafe93e126d742517a5f96553f512440c0239` | `83e23acc7115aecd3f03f94a5db8ace72dbd89caea8bd7d5805ffd26556c7f48` |
| `20261109T041505Z-cycle11-stage4-secondary-resource-cohort-review` | `secondary_resource` | 111 | `bb5d3813e4ef00066043ececaadbc47825025e6032ad65efa3f81c302739ee0f` | `6bfaaf508e12177c99a37cdfb8d176d10f8f2ccc6b853a2a681354b2911eec31` |
| `20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review` | `causal_graphs (cross-cohort)` | 182 | `a72e550ccd3d7dafe78d0106e5e10bdbd581a3a916905a41a3b522f305ac96fd` | `037e8a5675ae63b0759a16cb643af7f177bcea74c0fe3b10b211f89169354a42` |
| `20261109T041507Z-enstatite-cycle11-stage4-record-review` | `record: cmmmech:enstatite` | 1 | `6edb5cc897246a4a124559c0eed2e82f8d5124fcf3330fa4c2abe7a03d581750` | `f813204ce07d3be3965964091fbaac710c14146eba7ac423034f9d69c27305c4` |
| `20261109T041508Z-metacinnabar-cycle11-stage4-record-review` | `record: cmmmech:metacinnabar` | 1 | `9241d77a6fc376e06b1f7539c2961fecd99aacd0e347e5ec67f68659df743117` | `f6e221de5cf72ee64dbeffd4179a5e3071a5059ef70037e087f7d3b8468c7361` |
| `20261109T041509Z-scandium-cycle11-stage4-record-review` | `record: cmmmech:scandium` | 1 | `c94d76d5b065b1965ccb77980ee7e9d714059a5a13d4a44ab28131119cf3a808` | `09118a0240ce17fe45d4014fe337ef899288b0a47a0e8a4a2bf0ea6a658ab6a2` |

## 3. Open Findings Preserved for Stage 5 Grouped Remediation (`carry_forward_ids`)

1. **`cmmmech-cycle11-stage4-finding-0001`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support`
   - **Target Records (3)**: `cmmmech:enstatite` (`data/records/enstatite.yaml`), `cmmmech:olivine-group` (`data/records/olivine-group.yaml`), `cmmmech:dunite` (`data/records/dunite.yaml`)
   - **Summary**: Across the three *Gluconobacter oxydans* whole-culture biolixiviant silicate bioleaching records (`klug_2026` in `enstatite.yaml` and `olivine-group.yaml`; `lee2025` in `dunite.yaml`), `enstatite.yaml` `causal_graphs[0].nodes[4].description` (`enstatite_mixed_feed`, line 269) retains the generic parenthetical template string repeating the capitalized node label (`'Starting solid substrate (Enstatite-bearing mixed silicate feed) exposed to the acidic biolixiviant.'`), `edges[1..2].evidence[0].explanation` across all three records and `edges[0].evidence[0].explanation` in `enstatite.yaml` and `olivine-group.yaml` retain generic one-line template explanations, and `dunite.yaml` asserts `supports: support` with generic template explanations on `mechanisms[0].protein_examples[2..3]` (`UniProtKB:Q9L3B2` `pqqC` and `UniProtKB:P27175` `gdh`), `causal_graphs[0].nodes[1..2].protein_examples[0]`, and `causal_graphs[0].edges[1..2]` despite Lee et al. (2025) comparing whole-culture biolixiviants without single-gene knockouts or purified-enzyme assays isolating `pqqC` or `mgdh` (`supports: partial`, matching `enstatite.yaml` and `olivine-group.yaml`).
2. **`cmmmech-cycle11-stage4-finding-0002`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support`
   - **Target Records (1)**: `cmmmech:metacinnabar` (`data/records/metacinnabar.yaml`)
   - **Summary**: In `data/records/metacinnabar.yaml` (Vazquez-Rodriguez et al. 2015, *Frontiers in Microbiology* 6:596, `vazquez_rodriguez2015`), `mechanisms[0].protein_examples[0].evidence[0].explanation` (lines 118-120) and `causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation` (lines 192-194) for `UniProtKB:U5TVQ7` (`soxB`) state that Vazquez-Rodriguez et al. (2015) studied pure-culture dissolution of `"synthetic metacinnabar (beta-HgS)"`, whereas the primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural museum metacinnabar (`<250 um`, with pyritic inclusions, autoclaved under N2) and tested commercial synthetic black HgS only in the separate daily-thiosulfate-spike comparison (Figures 6-7); additionally, `causal_graphs[0].nodes[1].description` omits the natural vs synthetic feed distinction, `edges[1]` (`metacinnabar_substrate -> dissolved_hg2_species`) asserts `supports: support` for soluble Hg(II) accumulation even though viable *T. thioparus* incubations kept aqueous Hg low via reduction to volatile Hg(0) while killed-cell and thiosulfate controls showed substantial chemical Hg release and inoculum elemental-sulfur carryover (`supports: partial`), and `edges[0..3]` retain generic one-line explanations.
3. **`cmmmech-cycle11-stage4-finding-0003`** (`severity: minor`, `category: graph`, `status: open`):
   - **Issue Key**: `cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording`
   - **Target Records (1)**: `cmmmech:scandium` (`data/records/scandium.yaml`)
   - **Summary**: In `data/records/scandium.yaml` (Dong et al. 2024, *Separation and Purification Technology* 333:125919, `dong2024`), `mechanisms[0].protein_examples[0].evidence[0]` (lines 64-66) and `causal_graphs[0].nodes[0].protein_examples[0].evidence[0]` (lines 109-111) for `UniProtKB:C5B164` (`lanM` / Mex-LanM) assert `supports: support` with `explanation: 'Immobilized Mex-LanM selectively binds Sc(III) over competing transition/base metals and elutes high-purity scandium upon mild acid stripping.'`, whereas Dong et al. (2024) Section 3.4 and Figures 3C and 5E-F loaded a synthetic pH 3.0 16-REE chloride-salt mixture (nominal `0.4 mM` total REE in Figure 5; `0.2430 mM` sum with `23.8 +/- 1.1 uM` Sc in Table S9/S10) and eluted Sc(III) at 95.4% purity using stepwise 30 mM and 50 mM malonate at pH 5.0 without a matched Sc-only resin-without-LanM control (`supports: partial`); furthermore, `causal_graphs[0].description`, `nodes[1..2]`, and `edges[1]` describe the synthetic 16-REE chloride feed as a `"mixed leachate feed"` / `"multi-metal leachate"`, and `edges[0]` uses a generic 78-character explanation with `supports: support`.
