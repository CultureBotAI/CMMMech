# CMMMech Cycle 9 Stage 4 Full-Corpus Record Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech`
- **Cycle**: `9`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Inventory Commit**: `f8f0d8e724bcc013b5e9d98e3d12d5c7557587af`
- **Scope Frozen At**: `2026-11-05T20:06:00Z`
- **Timestamp**: `2026-11-05T20:20:09Z`
- **Coverage**: `688 / 688` eligible records (`100.0%`, `0` skipped, `0` failed)

## 1. Frozen Inventory & Cohort Breakdown

At commit `f8f0d8e724bcc013b5e9d98e3d12d5c7557587af`, the `data/records/*.yaml` corpus contains `688` maintained `MaterialRecord` files across 6 disjoint `material_kind` cohorts plus 1 cross-cohort `causal_graphs` & `protein_examples` slice:

| Cohort / Slice | Eligible Records | Reviewed Records | Coverage Ratio | Records with `mechanisms` (Total `mechanisms`) | Records with `causal_graphs` (Total `causal_graphs`) | Records with `protein_examples` (Unique UniProtKB Accessions) | Structured Review Bundle (`reviews/structured/<id>/`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `element` | `66` | `66` | `1.000` | `63` (`63` microbial, `0` abiotic-only; `66` microbial mechanisms, `0` abiotic) | `26` (`27`) | `25` (`40`) | `20261105T202000Z-cycle9-stage4-element-cohort-review` |
| `mineral` | `437` | `437` | `1.000` | `285` (`158` microbial, `127` abiotic-only; `343` total: `179` microbial, `164` abiotic) | `69` (`73`) | `67` (`70`) | `20261105T202001Z-cycle9-stage4-mineral-cohort-review` |
| `mineral_group` | `7` | `7` | `1.000` | `7` (`7` microbial, `0` abiotic-only; `7` microbial mechanisms, `0` abiotic) | `2` (`2`) | `2` (`7`) | `20261105T202002Z-cycle9-stage4-mineral-group-cohort-review` |
| `commodity` | `36` | `36` | `1.000` | `6` (`6` microbial, `0` abiotic-only; `6` microbial mechanisms, `0` abiotic) | `4` (`4`) | `4` (`6`) | `20261105T202003Z-cycle9-stage4-commodity-cohort-review` |
| `primary_resource` | `31` | `31` | `1.000` | `31` (`29` microbial, `2` abiotic-only; `42` total: `40` microbial, `2` abiotic) | `13` (`14`) | `13` (`35`) | `20261105T202004Z-cycle9-stage4-primary-resource-cohort-review` |
| `secondary_resource` | `111` | `111` | `1.000` | `108` (`85` microbial, `23` abiotic-only; `145` total: `104` microbial, `41` abiotic) | `48` (`51`) | `48` (`39`) | `20261105T202005Z-cycle9-stage4-secondary-resource-cohort-review` |
| **Total Disjoint Corpus** | **`688`** | **`688`** | **`1.000`** | **`500` (`348` microbial, `152` abiotic-only; `609` total: `402` microbial, `207` abiotic)** | **`162` (`171`)** | **`159` (`112` unique: `26` `SWISS_PROT`, `86` `TREMBL`)** | — |
| Cross-Cohort `causal_graphs` & `protein_examples` | `162` | `162` | `1.000` | `162` | `162` (`171` graphs, `782` nodes, `611` edges, `303` `GENE_OR_PROTEIN`: `297` `GROUNDED`, `6` `UNGROUNDED`) | `159` (`548` `protein_examples` per layer, `1096` total) | `20261105T202006Z-cycle9-stage4-causal-graphs-cohort-review` |

### Single-Record Deep-Dive Reviews (`kind: record`)

1. **`20261105T202007Z-uranium-cycle9-stage4-record-review`**:
   - Target: `cmmmech:uranium` (`data/records/uranium.yaml`, `element`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle9-stage4-finding-0001`)
2. **`20261105T202008Z-rhodochrosite-cycle9-stage4-record-review`**:
   - Target: `cmmmech:rhodochrosite` (`data/records/rhodochrosite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle9-stage4-finding-0002`)
3. **`20261105T202009Z-asbolane-cycle9-stage4-record-review`**:
   - Target: `cmmmech:asbolane` (`data/records/asbolane.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle9-stage4-finding-0003`)

## 2. Verification of Prior Cycle 8 Stage 4 Findings & Cycle 9 Stage 1–3 Additions

- **Cycle 8 Stage 4 Findings (`cmmmech-cycle8-stage4-finding-0001` through `0003`)**:
  - `cmmmech-cycle8-stage4-finding-0001` (node IDs `unimpaired_72h_ferrous_oxidation_trajectory` and `enhanced_72h_schwertmannite_precipitate_yield` in `causal_graphs[1]` of `cmmmech:schwertmannite`): **Confirmed resolved** (`PR #932`, commit `9b3188dc`).
  - `cmmmech-cycle8-stage4-finding-0002` (lowercase mid-sentence `to periplasmic rusticyanin` in `edges[0].description` across 8 *Acidithiobacillus ferrooxidans* records / 9 causal graphs): **Confirmed resolved** (`PR #932`, commit `9b3188dc`).
  - `cmmmech-cycle8-stage4-finding-0003` (study-specific `oxidized_metal_substrate` and `reduced_metal_product` descriptions, TEM-EDX elemental Cr qualification, and lowercase mid-sentence node labels in `cmmmech:chromium` and `cmmmech:uraninite`): **Confirmed resolved** (`PR #932`, commit `9b3188dc`).
- **Cycle 9 Stage 1–3 Additions**:
  - **Stage 1 (`PR #935`, commit `503b381e`)**: Added 5 IMA-CNMNC Round 127 critical-element mineral species records (`cmmmech:ginelfite`, `cmmmech:graulichite-la`, `cmmmech:karlseifertite`, `cmmmech:skogbyite`, `cmmmech:tetrahedrite-cd`). Formulae, IMA approval numbers, type localities, crystal structures, and top-level `ima_symbol` slots (`Glf`, `Karl`, `Skb`, `Ttr-Cd` on the 4 species with approved symbols; `graulichite-la` IMA 2020-093 has no symbol in Biagioni et al. `2022`, *Eur. J. Mineral.* `34:365-374` or the September 2026 IMA Master List) pass with `0` open findings.
  - **Stage 2 (`PR #936`, commit `2215c814`) & Stage 3 (`PR #938`, commit `f8f0d8e7`)**: Stage 2 added `causal_graphs` (10 graphs) and initial `protein_examples` (51 entries per layer) across 10 microbial records (`ammoniojarosite`, `baricite`, `electroformed-copper-silver-manufacturing-scrap`, `mackinawite`, `metal-grinding-sludge`, `millerite`, `polydymite`, `scorodite`, `spent-nickel-cadmium-batteries`, `vaesite`), and Stage 3 added 10 companion subunit/paralog/strain `ProteinExample` entries (`UniProtKB:P45573` `dsvC DVU_2776` on `millerite`, `polydymite`, `vaesite`; `UniProtKB:Q314T3` `Dde_0762` on `baricite`; `UniProtKB:L0RB25` `dsvC DESAM_21662` on `mackinawite`; `UniProtKB:A0ACD5IN56` `HF292_015290` on `electroformed-copper-silver-manufacturing-scrap`; `UniProtKB:A0A2U9IB88` `DFR85_00235` on `scorodite`; and `UniProtKB:A0A2W1KP86` `DN052_11940` on `ammoniojarosite`, `metal-grinding-sludge`, `spent-nickel-cadmium-batteries`). All 10 records updated in Cycle 9 Stages 2 and 3 pass with `0` open findings.

## 3. Open Findings Preserved for Cycle 9 Stage 5 (`resolve_review_findings`)

In accordance with the Stage 4 read-only record boundary (`data/records/*.yaml` unmodified during Stage 4), all 3 confirmed minor findings across `7` distinct records are preserved with `status: "open"` and listed in `carry_forward_ids` for grouped remediation in Stage 5:

| Finding ID | Issue Key | Severity | Category | Affected Records (`count`) | Summary & Stage 5 Remediation |
| --- | --- | --- | --- | --- | --- |
| `cmmmech-cycle9-stage4-finding-0001` | `cmmmech.shewanella-mr1-bes-uranium-vanadium.template-node-descriptions-and-unqualified-uranium-product-label` | `minor` | `graph` | `2` (`2` `element`: `cmmmech:uranium`, `cmmmech:vanadium`) | In `data/records/uranium.yaml` and `data/records/vanadium.yaml` (`kane_2026_bes`, DOI `10.5066/P9ERLSM6`), `oxidized_metal_substrate` and `reduced_metal_product` in `causal_graphs[0]` retain generic template descriptions (`"Terminal electron acceptor substrate (<Label>) in kane_2026_bes."` and `"Resulting reduced product state (<Label>) in kane_2026_bes."`), `edges[1..3]` interpolate capitalized node labels mid-sentence with generic one-line explanations, and `uranium.yaml` labels `reduced_metal_product` `"Cell-associated reduced U(IV) precipitate"` with `supports: support` on `edges[3]` despite `mechanisms[0]` stating that `kane_2026_bes` does not establish a crystalline phase or `U(IV)` oxidation state and abiotic controls also removed U (`supports: partial`). Remediate both records in Stage 5. |
| `cmmmech-cycle9-stage4-finding-0002` | `cmmmech.shewanella-mr1-rhodochrosite-chlorite.medium-mismatch-template-descriptions-and-capitalized-edge-labels` | `minor` | `graph` | `2` (`1` `mineral`: `cmmmech:rhodochrosite`; `1` `mineral_group`: `cmmmech:chlorite`) | In `data/records/rhodochrosite.yaml` (Johnson et al. `2016`, DOI `10.1021/acs.est.5b04834`), `oxidized_metal_substrate` and `reduced_metal_product` in `causal_graphs[0]` retain generic template wrappers, `oxidized_metal_substrate.description` states `"in Ca-free artificial freshwater medium"` whereas `mechanisms[0].context` specifies `"1 L modified M1 medium"` (`~6.3 mM` freshly synthesized colloidal `MnO2`, `20 mM` lactate, no added phosphate, pH `8`), and `edges[1..3]` in `rhodochrosite.yaml` plus `edges[1..2]` in `data/records/chlorite.yaml` (Brookshaw et al. `2014`, DOI `10.2138/am.2014.4774CCBY`) interpolate capitalized node labels mid-sentence with generic one-line explanations. Remediate both records in Stage 5. |
| `cmmmech-cycle9-stage4-finding-0003` | `cmmmech.geobacter-buchanan-manganese-minerals.template-node-descriptions-and-capitalized-graph-edge-labels` | `minor` | `graph` | `3` (`3` `mineral`: `cmmmech:asbolane`, `cmmmech:feitknechtite`, `cmmmech:pyrochroite`) | Across `data/records/asbolane.yaml`, `data/records/feitknechtite.yaml`, and `data/records/pyrochroite.yaml` (Buchanan `2021/2022` University of Manchester PhD thesis Chapter 4), `nodes[2]` and `nodes[3]` in `causal_graphs[0]` use generic template descriptions repeating their capitalized node labels verbatim in parentheses (`"Starting synthetic Co/Ni-asbolane mineral suspension (<Label>)..."` and `"Reduced product assemblage (<Label>)..."`), and `causal_graphs[0].description` plus `edges[0].description` interpolate those capitalized node labels mid-sentence. Remediate all 3 records in Stage 5. |
