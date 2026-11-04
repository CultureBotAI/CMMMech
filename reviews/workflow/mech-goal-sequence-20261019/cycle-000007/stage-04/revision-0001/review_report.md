# CMMMech Cycle 7 Stage 4 Full-Corpus Record Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech`
- **Cycle**: `7`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Inventory Commit**: `ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c`
- **Scope Frozen At**: `2026-11-04T12:30:00Z`
- **Timestamp**: `2026-11-04T12:45:09Z`
- **Coverage**: `678 / 678` eligible records (`100.0%`, `0` skipped, `0` failed)

## 1. Frozen Inventory & Cohort Breakdown

At commit `ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c`, the `data/records/*.yaml` corpus contains `678` maintained `MaterialRecord` files across 6 disjoint `material_kind` cohorts plus 1 cross-cohort `causal_graphs` & `protein_examples` slice:

| Cohort / Slice | Eligible Records | Reviewed Records | Coverage Ratio | Records with `mechanisms` (Total `mechanisms`) | Records with `causal_graphs` (Total `causal_graphs`) | Records with `protein_examples` (Unique UniProtKB Accessions) | Structured Review Bundle (`reviews/structured/<id>/`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `element` | `66` | `66` | `1.000` | `63` (`66`) | `26` (`27`) | `25` (`40`) | `20261104T124500Z-cycle7-stage4-element-cohort-review` |
| `mineral` | `427` | `427` | `1.000` | `285` (`343`) | `59` (`62`) | `57` (`39`) | `20261104T124501Z-cycle7-stage4-mineral-cohort-review` |
| `mineral_group` | `7` | `7` | `1.000` | `7` (`7`) | `2` (`2`) | `2` (`7`) | `20261104T124502Z-cycle7-stage4-mineral-group-cohort-review` |
| `commodity` | `36` | `36` | `1.000` | `6` (`6`) | `4` (`4`) | `4` (`6`) | `20261104T124503Z-cycle7-stage4-commodity-cohort-review` |
| `primary_resource` | `31` | `31` | `1.000` | `31` (`42`) | `10` (`11`) | `10` (`26`) | `20261104T124504Z-cycle7-stage4-primary-resource-cohort-review` |
| `secondary_resource` | `111` | `111` | `1.000` | `108` (`107` microbial, `1` abiotic; `145` total) | `41` (`44`) | `41` (`30`) | `20261104T124505Z-cycle7-stage4-secondary-resource-cohort-review` |
| **Total Disjoint Corpus** | **`678`** | **`678`** | **`1.000`** | **`500` (`609`)** | **`142` (`150`)** | **`139` (`72` unique: `22` `SWISS_PROT`, `50` `TREMBL`)** | — |
| Cross-Cohort `causal_graphs` & `protein_examples` | `142` | `142` | `1.000` | `142` | `142` (`150` graphs, `687` nodes, `537` edges, `261` `GENE_OR_PROTEIN`: `255` `GROUNDED`, `6` `UNGROUNDED`) | `139` (`445` `protein_examples` per layer, `890` total) | `20261104T124506Z-cycle7-stage4-causal-graphs-cohort-review` |

### Single-Record Deep-Dive Reviews (`kind: record`)

1. **`20261104T124507Z-fengruiite-cycle7-stage4-record-review`**:
   - Target: `cmmmech:fengruiite` (`data/records/fengruiite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle7-stage4-finding-0001`)
2. **`20261104T124508Z-manganese-ore-cycle7-stage4-record-review`**:
   - Target: `cmmmech:manganese-ore` (`data/records/manganese-ore.yaml`, `primary_resource`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle7-stage4-finding-0003`)
3. **`20261104T124509Z-cassiterite-polymetallic-sulfide-ore-cycle7-stage4-record-review`**:
   - Target: `cmmmech:cassiterite-polymetallic-sulfide-ore` (`data/records/cassiterite-polymetallic-sulfide-ore.yaml`, `primary_resource`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle7-stage4-finding-0002`)

## 2. Verification of Prior Cycle 6 Stage 4 Findings & Cycle 7 Stage 1–3 Additions

- **Cycle 6 Stage 4 Findings (`cmmmech-cycle6-stage4-finding-0001` through `0003`)**:
  - `cmmmech-cycle6-stage4-finding-0001` (`cmmmech:traction-battery-hydrometallurgical-residue` `tth_hydrolase` consortium label and description): **Confirmed resolved** (`PR #904`, commit `b74c527d`).
  - `cmmmech-cycle6-stage4-finding-0002` (16 single-species *Acidithiobacillus thiooxidans* records `tth_hydrolase` paralog loci `GCD22_14205` and `GCD22_02315` in label and description): **Confirmed resolved** (`PR #904`, commit `b74c527d`).
  - `cmmmech-cycle6-stage4-finding-0003` (`cmmmech:vielleaureite-ce` and `cmmmech:xianhuaite-ce` top-level `ima_symbol: Vlr-Ce` and `ima_symbol: Xhu-Ce` slots): **Confirmed resolved** (`PR #904`, commit `b74c527d`).
- **Cycle 7 Stage 1–3 Additions**:
  - **Stage 1 (`PR #910`, commit `fa7431ae`)**: Added 5 IMA-CNMNC Round 125 critical-element mineral species records (`cmmmech:fengruiite`, `cmmmech:igelstromite`, `cmmmech:johanngeorgenstadtite`, `cmmmech:lazerckerite`, `cmmmech:plumbogottlobite`). Formulae, IMA approval numbers, type localities, and empirical compositions match Tian et al. (`2026`, *Eur. J. Mineral.* `38:519-530`, `DOI:10.5194/ejm-38-519-2026`), Holtstam et al. (`2024`, *Eur. J. Mineral.* `36:311-322`, `DOI:10.5194/ejm-36-311-2024`), Kampf et al. (`2020`, *Mineralogical Magazine* `84:761-769`, `DOI:10.1180/mgm.2020.61`), Pazout et al. (`2024`, *Eur. J. Mineral.* `36:641-656`, `DOI:10.5194/ejm-36-641-2024`), and Kampf et al. (`2026`, *Eur. J. Mineral.* `38:209-216`, `DOI:10.5194/ejm-38-209-2026`). Four of these 5 records (`fengruiite`, `igelstromite`, `lazerckerite`, `plumbogottlobite`) state IMA symbols (`Fru`, `Ig`, `Lzc`, `Pgtb`) in `description` but omit the top-level `ima_symbol` slot (`cmmmech-cycle7-stage4-finding-0001`).
  - **Stage 2 (`PR #914`, commit `8bf82c8d`) & Stage 3 (`PR #915`, commit `ff4a9841`)**: Stage 2 added `causal_graphs` and `protein_examples` to 9 sulfur-oxidizing records (`cassiterite-polymetallic-sulfide-ore`, `chalcopyrite`, `coal-beneficiation-waste`, `copper-smelter-flue-dust`, `copper`, `molybdenite`, `ponded-coal-ash`, `pyrite-roasting-cinder`, `skutterudite`), and Stage 3 expanded multi-strain/paralog `protein_examples` across 10 records (`cassiterite-polymetallic-sulfide-ore`, `chalcopyrite-enargite-concentrate`, `chalcopyrite`, `coal-beneficiation-waste`, `copper-smelter-flue-dust`, `copper`, `molybdenite`, `pyrite-roasting-cinder`, `skutterudite`, `waste-x-ray-films`). While `ponded-coal-ash` and `waste-x-ray-films` pass with `0` open findings, the 9 sulfur-oxidizing records updated in Stage 3 require minor edge-description verb number agreement and edge-explanation locus synchronization (`cmmmech-cycle7-stage4-finding-0002`).

## 3. Open Findings Preserved for Cycle 7 Stage 5 (`resolve_review_findings`)

In accordance with the Stage 4 read-only record boundary (`data/records/*.yaml` unmodified during Stage 4), all 3 confirmed minor findings across `16` distinct records are preserved with `status: "open"` and listed in `carry_forward_ids` for grouped remediation in Stage 5:

| Finding ID | Issue Key | Severity | Category | Affected Records (`count`) | Summary & Stage 5 Remediation |
| --- | --- | --- | --- | --- | --- |
| `cmmmech-cycle7-stage4-finding-0001` | `cmmmech.round125-minerals.missing-ima-symbol-slot` | `minor` | `completeness` | `4` (`cmmmech:fengruiite`, `cmmmech:igelstromite`, `cmmmech:lazerckerite`, `cmmmech:plumbogottlobite`) | Four of the five IMA-CNMNC Round 125 mineral records curated in Cycle 7 Stage 1 (`PR #910`, commit `fa7431ae`) state their IMA-CNMNC-approved mineral symbols in `description` (`Fru` in `fengruiite.yaml` line 8; `Ig` in `igelstromite.yaml` line 9; `Lzc` in `lazerckerite.yaml` lines 11–12; `Pgtb` in `plumbogottlobite.yaml` line 8) but omit the top-level `ima_symbol` slot (`ima_symbol: Fru`, `ima_symbol: Ig`, `ima_symbol: Lzc`, `ima_symbol: Pgtb` immediately following `material_kind: mineral`). Populate `ima_symbol` on all 4 records in Stage 5. |
| `cmmmech-cycle7-stage4-finding-0002` | `cmmmech.cycle7-stage3-sulfur-graphs.edge-desc-grammar-and-incomplete-edge-evidence-loci` | `minor` | `graph` | `9` (`1` `element`: `cmmmech:copper`; `3` `mineral`: `cmmmech:chalcopyrite`, `cmmmech:molybdenite`, `cmmmech:skutterudite`; `2` `primary_resource`: `cmmmech:cassiterite-polymetallic-sulfide-ore`, `cmmmech:chalcopyrite-enargite-concentrate`; `3` `secondary_resource`: `cmmmech:coal-beneficiation-waste`, `cmmmech:copper-smelter-flue-dust`, `cmmmech:pyrite-roasting-cinder`) | Across the 9 sulfur-oxidizing causal graphs updated in Cycle 7 Stage 3 (`PR #915`, commit `ff4a9841`), `edges[0]` (`sqr_reductase -> tth_hydrolase`) and `edges[1]` (`tth_hydrolase -> <leach_system>`) had their pluralized node labels substituted into `edge.description` while retaining singular verbs (`"Sqr ... oxidoreductases (...) oxidizes ..."` or `"Sqr ... reductases (...) catalyzes ..."`, and `"TetH/Tth tetrathionate hydrolases (...) disproportionates ..."`), and in 7 of those 9 records (`cassiterite-polymetallic-sulfide-ore`, `chalcopyrite`, `chalcopyrite-enargite-concentrate`, `coal-beneficiation-waste`, `copper`, `molybdenite`, `pyrite-roasting-cinder`) `edges[0].evidence[0].explanation` still lists only the pre-Stage-3 Sqr/TetH/Tth locus subset, omitting the Stage-3-added *Sulfobacillus thermosulfidooxidans* DSM 9293 Sqr (`SAMN00768000_0580`), *Acidithiobacillus caldus* ZBY TetH (`tetH / BAE30_05680`), and *Acidithiobacillus ferrooxidans* DSM 16523 Tth (`DN052_12875`) homologs. Update `edges[0..1].description` across all 9 records and `edges[0].evidence[0].explanation` across the 7 affected records in Stage 5. |
| `cmmmech-cycle7-stage4-finding-0003` | `cmmmech.aspergillus-atcc1015-cexa-node.description-omits-strain-matched-g3y4n5` | `minor` | `graph` | `3` (`2` `mineral`: `cmmmech:birnessite`, `cmmmech:lindbergite`; `1` `primary_resource`: `cmmmech:manganese-ore`) | In `birnessite.yaml` (`causal_graphs[1]`, `fungal_synthetic_cobalt_birnessite_transformation_graph`, lines 316–363), `lindbergite.yaml` (`causal_graphs[0]`, `niger_associated_manganese_oxalate_formation_graph`, lines 151–198), and `manganese-ore.yaml` (`causal_graphs[0]`, `fungal_nkamouna_laterite_transformation_graph`, lines 136–183), node `cexa_citrate_exporter` is grounded to both the strain-matched *Aspergillus niger* ATCC 1015 reference-proteome entry `UniProtKB:G3Y4N5` (`CEXA_ASPNA`, locus `ASPNIDRAFT_56962`) and the species-level reviewed entry `UniProtKB:A0A254TZW7` (`CEXA_ASPNG`), but `cexa_citrate_exporter.description` names only `UniProtKB:A0A254TZW7` and omits `UniProtKB:G3Y4N5` (`CEXA_ASPNA` / `ASPNIDRAFT_56962`). Update `cexa_citrate_exporter.description` across all 3 records in Stage 5. |
