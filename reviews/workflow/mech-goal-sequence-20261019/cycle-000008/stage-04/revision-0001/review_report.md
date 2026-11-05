# CMMMech Cycle 8 Stage 4 Full-Corpus Record Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech`
- **Cycle**: `8`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Inventory Commit**: `573410374de4d10b2595b6bf75a1f2138ea33ed7`
- **Scope Frozen At**: `2026-11-05T00:35:00Z`
- **Timestamp**: `2026-11-05T00:55:09Z`
- **Coverage**: `683 / 683` eligible records (`100.0%`, `0` skipped, `0` failed)

## 1. Frozen Inventory & Cohort Breakdown

At commit `573410374de4d10b2595b6bf75a1f2138ea33ed7`, the `data/records/*.yaml` corpus contains `683` maintained `MaterialRecord` files across 6 disjoint `material_kind` cohorts plus 1 cross-cohort `causal_graphs` & `protein_examples` slice:

| Cohort / Slice | Eligible Records | Reviewed Records | Coverage Ratio | Records with `mechanisms` (Total `mechanisms`) | Records with `causal_graphs` (Total `causal_graphs`) | Records with `protein_examples` (Unique UniProtKB Accessions) | Structured Review Bundle (`reviews/structured/<id>/`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `element` | `66` | `66` | `1.000` | `63` (`63` microbial, `0` abiotic-only; `66` microbial mechanisms, `0` abiotic) | `26` (`27`) | `25` (`40`) | `20261105T005500Z-cycle8-stage4-element-cohort-review` |
| `mineral` | `432` | `432` | `1.000` | `285` (`158` microbial, `127` abiotic-only; `343` total: `179` microbial, `164` abiotic) | `62` (`66`) | `60` (`43`) | `20261105T005501Z-cycle8-stage4-mineral-cohort-review` |
| `mineral_group` | `7` | `7` | `1.000` | `7` (`7` microbial, `0` abiotic-only; `7` microbial mechanisms, `0` abiotic) | `2` (`2`) | `2` (`7`) | `20261105T005502Z-cycle8-stage4-mineral-group-cohort-review` |
| `commodity` | `36` | `36` | `1.000` | `6` (`6` microbial, `0` abiotic-only; `6` microbial mechanisms, `0` abiotic) | `4` (`4`) | `4` (`6`) | `20261105T005503Z-cycle8-stage4-commodity-cohort-review` |
| `primary_resource` | `31` | `31` | `1.000` | `31` (`29` microbial, `2` abiotic-only; `42` total: `40` microbial, `2` abiotic) | `13` (`14`) | `13` (`35`) | `20261105T005504Z-cycle8-stage4-primary-resource-cohort-review` |
| `secondary_resource` | `111` | `111` | `1.000` | `108` (`85` microbial, `23` abiotic-only; `145` total: `104` microbial, `41` abiotic) | `45` (`48`) | `45` (`34`) | `20261105T005505Z-cycle8-stage4-secondary-resource-cohort-review` |
| **Total Disjoint Corpus** | **`683`** | **`683`** | **`1.000`** | **`500` (`348` microbial, `152` abiotic-only; `609` total: `402` microbial, `207` abiotic)** | **`152` (`161`)** | **`149` (`81` unique: `23` `SWISS_PROT`, `58` `TREMBL`)** | — |
| Cross-Cohort `causal_graphs` & `protein_examples` | `152` | `152` | `1.000` | `152` | `152` (`161` graphs, `742` nodes, `581` edges, `283` `GENE_OR_PROTEIN`: `277` `GROUNDED`, `6` `UNGROUNDED`) | `149` (`491` `protein_examples` per layer, `982` total) | `20261105T005506Z-cycle8-stage4-causal-graphs-cohort-review` |

### Single-Record Deep-Dive Reviews (`kind: record`)

1. **`20261105T005507Z-schwertmannite-cycle8-stage4-record-review`**:
   - Target: `cmmmech:schwertmannite` (`data/records/schwertmannite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle8-stage4-finding-0001`, `cmmmech-cycle8-stage4-finding-0002`)
2. **`20261105T005508Z-eudialyte-ore-cycle8-stage4-record-review`**:
   - Target: `cmmmech:eudialyte-ore` (`data/records/eudialyte-ore.yaml`, `primary_resource`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle8-stage4-finding-0002`)
3. **`20261105T005509Z-uraninite-cycle8-stage4-record-review`**:
   - Target: `cmmmech:uraninite` (`data/records/uraninite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle8-stage4-finding-0003`)

## 2. Verification of Prior Cycle 7 Stage 4 Findings & Cycle 8 Stage 1–3 Additions

- **Cycle 7 Stage 4 Findings (`cmmmech-cycle7-stage4-finding-0001` through `0003`)**:
  - `cmmmech-cycle7-stage4-finding-0001` (top-level `ima_symbol` slots `Fru`, `Ig`, `Lzc`, `Pgtb` on `cmmmech:fengruiite`, `cmmmech:igelstromite`, `cmmmech:lazerckerite`, `cmmmech:plumbogottlobite`): **Confirmed resolved** (`PR #921`, commit `be23f1ee`).
  - `cmmmech-cycle7-stage4-finding-0002` (edge-description verb number agreement across 9 sulfur-oxidizing records and complete Sqr/TetH/Tth locus lists in `edges[0].evidence[0].explanation` across 7 records): **Confirmed resolved** (`PR #921`, commit `be23f1ee`).
  - `cmmmech-cycle7-stage4-finding-0003` (`cexa_citrate_exporter.description` naming both `UniProtKB:G3Y4N5` and `UniProtKB:A0A254TZW7` across `cmmmech:birnessite`, `cmmmech:lindbergite`, `cmmmech:manganese-ore`): **Confirmed resolved** (`PR #921`, commit `be23f1ee`).
- **Cycle 8 Stage 1–3 Additions**:
  - **Stage 1 (`PR #923`, commit `863f5b2c`)**: Added 5 IMA-CNMNC Round 126 critical-element mineral species records (`cmmmech:niasite`, `cmmmech:manganoschafarzikite`, `cmmmech:erzwiesite`, `cmmmech:kenoargentotetrahedrite-zn`, `cmmmech:lopatkaite`). Formulae, IMA approval numbers, type localities, crystal structures, and top-level `ima_symbol` slots (`Msfz`, `Erw`, `Kattr-Zn`, `Lpk` on the 4 species with approved symbols; `niasite` IMA 2019-105 has no symbol in Kampf et al. `2020`, *Eur. J. Mineral.* `32:373-385` or the September 2026 IMA Master List) pass with `0` open findings.
  - **Stage 2 (`PR #924`, commit `d69682fb`) & Stage 3 (`PR #926`, commit `57341037`)**: Stage 2 added `causal_graphs` (11 graphs) and `protein_examples` to 10 records (`argentojarosite`, `basic-oxygen-furnace-steelmaking-dust`, `cemented-tungsten-carbide-scrap`, `enargite-pyrite-concentrate`, `eudialyte-ore`, `nickel-smelter-slag`, `rutile`, `schwertmannite`, `spent-steel-pickling-liquors`, `tennantite-concentrate`), and Stage 3 added multi-strain/paralog UniProtKB entries (`UniProtKB:A0A2W1KH68` `DN052_11975` on the 8 *Acidithiobacillus ferrooxidans* records and `UniProtKB:A0A060A5X1`, `A0A059ZWQ2`, `A0A060A0U3`, `Q8RR59`, `A0A521C1T0`, `A0A063XP03`, `A0A063XM75`, `A0A063XP52` on `enargite-pyrite-concentrate` and `tennantite-concentrate`). While `enargite-pyrite-concentrate` and `tennantite-concentrate` pass with `0` open findings, `schwertmannite` retains inverted pre-remediation node IDs in `causal_graphs[1]` (`cmmmech-cycle8-stage4-finding-0001`), and the 8 *A. ferrooxidans* records retain a mid-sentence capitalized target node label in `edges[0].description` (`cmmmech-cycle8-stage4-finding-0002`).

## 3. Open Findings Preserved for Cycle 8 Stage 5 (`resolve_review_findings`)

In accordance with the Stage 4 read-only record boundary (`data/records/*.yaml` unmodified during Stage 4), all 3 confirmed minor findings across `10` distinct records are preserved with `status: "open"` and listed in `carry_forward_ids` for grouped remediation in Stage 5:

| Finding ID | Issue Key | Severity | Category | Affected Records (`count`) | Summary & Stage 5 Remediation |
| --- | --- | --- | --- | --- | --- |
| `cmmmech-cycle8-stage4-finding-0001` | `cmmmech.schwertmannite.lx5-eps-removal-perturbation-graph-inverted-node-ids` | `minor` | `graph` | `1` (`cmmmech:schwertmannite`) | In `data/records/schwertmannite.yaml` (`causal_graphs[1]`, `lx5_eps_removal_perturbation_graph`, lines 537–583), after Cycle 8 Stage 2 (`PR #924`, Issue `#925`) corrected `nodes[2]` and `nodes[3]` labels and descriptions to match Song et al. (`2018`, *Materials* `11(9):1739`, Section 3.4, Table 1, Figures 5–7) — where 20,000 g EPS removal leaves 72 h Fe(II) oxidation unimpaired and increases 72 h dry schwertmannite mass from `0.89 g` / `0.96 g` to `1.29 g` — `nodes[2].id` (`attenuated_12_to_40h_ferrous_oxidation_flux`) and `nodes[3].id` (`reduced_12_to_40h_schwertmannite_precipitate_yield`) and their references in `edges[2].target`, `edges[3].source`, and `edges[3].target` still retain the inverted pre-remediation IDs. Rename both node IDs and their edge references in Stage 5. |
| `cmmmech-cycle8-stage4-finding-0002` | `cmmmech.ferrooxidans-cyc2-causal-graphs.mid-sentence-capitalized-periplasmic-target-label-in-edge-description` | `minor` | `graph` | `8` (`3` `mineral`: `cmmmech:argentojarosite`, `cmmmech:rutile`, `cmmmech:schwertmannite`; `1` `primary_resource`: `cmmmech:eudialyte-ore`; `4` `secondary_resource`: `cmmmech:basic-oxygen-furnace-steelmaking-dust`, `cmmmech:cemented-tungsten-carbide-scrap`, `cmmmech:nickel-smelter-slag`, `cmmmech:spent-steel-pickling-liquors`) | Across all 8 *Acidithiobacillus ferrooxidans* records (`9` causal graphs) updated in Cycle 8 Stage 2 (`PR #924`) and Stage 3 (`PR #926`), `edges[0].description` (`cyc2_outer_membrane_cytochrome -> rus_cyc1_periplasmic_electron_transfer`) interpolates the capitalized target node label `"Periplasmic rusticyanin and diheme cytochrome c4 Cyc1 (rus AFE_3146; cyc1 AFE_3152)"` verbatim mid-sentence (`"... to Periplasmic rusticyanin ..."`). Replace `"to Periplasmic "` with `"to periplasmic "` across all 9 causal graphs in Stage 5. |
| `cmmmech-cycle8-stage4-finding-0003` | `cmmmech.shewanella-mr1-chromium-uraninite.unqualified-template-node-descriptions-and-capitalized-interpolations` | `minor` | `graph` | `2` (`1` `element`: `cmmmech:chromium`; `1` `mineral`: `cmmmech:uraninite`) | In `data/records/chromium.yaml` (Belchik et al. `2011`, *Appl. Environ. Microbiol.* `77(12):4035-4041`) and `data/records/uraninite.yaml` (Marshall et al. `2006`, *PLOS Biology* `4(8):e268`), `oxidized_metal_substrate` and `reduced_metal_product` in `causal_graphs[0]` retain generic template placeholder descriptions (`"Oxidized metal species or mineral substrate (<Label>) accepting extracellular electrons."` and `"Reduced metal species or mineral phase (<Label>) formed by extracellular electron transfer."`), `protein_examples` and `edges` interpolate capitalized node labels mid-sentence, and `chromium.yaml` labels `reduced_metal_product` as `"Reduced Cr(III) precipitate/complexes"` without qualifying that Cr(III) valence in Belchik et al. (`2011`) was inferred from prior studies rather than established by oxidation-state spectroscopy. Remediate both records in Stage 5. |
