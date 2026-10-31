# CMMMech Cycle 6 Stage 4 Full-Corpus Record Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech`
- **Cycle**: `6`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Inventory Commit**: `fab0682688678750d7da4e5357dda11592d5fac3`
- **Scope Frozen At**: `2026-10-31T13:05:00Z`
- **Timestamp**: `2026-10-31T13:20:09Z`
- **Coverage**: `673 / 673` eligible records (`100.0%`, `0` skipped, `0` failed)

## 1. Frozen Inventory & Cohort Breakdown

At commit `fab0682688678750d7da4e5357dda11592d5fac3`, the `data/records/*.yaml` corpus contains `673` maintained `MaterialRecord` files across 6 disjoint `material_kind` cohorts plus 1 cross-cohort `causal_graphs` & `protein_examples` slice:

| Cohort / Slice | Eligible Records | Reviewed Records | Coverage Ratio | Records with `mechanisms` (Total `mechanisms`) | Records with `causal_graphs` (Total `causal_graphs`) | Records with `protein_examples` (Unique UniProtKB Accessions) | Structured Review Bundle (`reviews/structured/<id>/`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `element` | `66` | `66` | `1.000` | `63` (`66`) | `25` (`26`) | `24` (`34`) | `20261031T132000Z-cycle6-stage4-element-cohort-review` |
| `mineral` | `422` | `422` | `1.000` | `285` (`343`) | `56` (`59`) | `54` (`35`) | `20261031T132001Z-cycle6-stage4-mineral-cohort-review` |
| `mineral_group` | `7` | `7` | `1.000` | `7` (`7`) | `2` (`2`) | `2` (`7`) | `20261031T132002Z-cycle6-stage4-mineral-group-cohort-review` |
| `commodity` | `36` | `36` | `1.000` | `6` (`6`) | `4` (`4`) | `4` (`6`) | `20261031T132003Z-cycle6-stage4-commodity-cohort-review` |
| `primary_resource` | `31` | `31` | `1.000` | `31` (`42`) | `9` (`10`) | `9` (`23`) | `20261031T132004Z-cycle6-stage4-primary-resource-cohort-review` |
| `secondary_resource` | `111` | `111` | `1.000` | `108` (`145`) | `37` (`40`) | `37` (`25`) | `20261031T132005Z-cycle6-stage4-secondary-resource-cohort-review` |
| **Total Disjoint Corpus** | **`673`** | **`673`** | **`1.000`** | **`500` (`609`)** | **`133` (`141`)** | **`130` (`67` unique: `22` `SWISS_PROT`, `45` `TREMBL`)** | — |
| Cross-Cohort `causal_graphs` & `protein_examples` | `133` | `133` | `1.000` | `133` | `133` (`141` graphs, `642` nodes, `501` edges, `243` `GENE_OR_PROTEIN`: `237` `GROUNDED`, `6` `UNGROUNDED`) | `130` (`394` `protein_examples` per layer, `788` total) | `20261031T132006Z-cycle6-stage4-causal-graphs-cohort-review` |

### Single-Record Deep-Dive Reviews (`kind: record`)

1. **`20261031T132007Z-traction-battery-hydrometallurgical-residue-cycle6-stage4-record-review`**:
   - Target: `cmmmech:traction-battery-hydrometallurgical-residue` (`data/records/traction-battery-hydrometallurgical-residue.yaml`, `secondary_resource`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle6-stage4-finding-0001`)
2. **`20261031T132008Z-arsenic-cycle6-stage4-record-review`**:
   - Target: `cmmmech:arsenic` (`data/records/arsenic.yaml`, `element`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle6-stage4-finding-0002`)
3. **`20261031T132009Z-xianhuaite-ce-cycle6-stage4-record-review`**:
   - Target: `cmmmech:xianhuaite-ce` (`data/records/xianhuaite-ce.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle6-stage4-finding-0003`)

## 2. Verification of Prior Cycle 5 Stage 4 Findings & Cycle 6 Stage 1–3 Additions

- **Cycle 5 Stage 4 Findings (`cmmmech-cycle5-stage4-finding-0001` through `0003`)**:
  - `cmmmech-cycle5-stage4-finding-0001` (13 records with non-canonical top-level YAML key ordering): **Confirmed resolved** (`0 / 673` records violate `CANONICAL_RECORD_KEYS`, enforced by `src/cmmmech/validation.py` from `cmmmech-infra-0013` / `PR #883`).
  - `cmmmech-cycle5-stage4-finding-0002` (`cmmmech:tetrahedrite-concentrate` `ferrooxidans_tetrahedrite_bioleaching_graph` `tth_hydrolase` label/description and edge explanation): **Confirmed resolved**.
  - `cmmmech-cycle5-stage4-finding-0003` (`cmmmech:waste-liquid-crystal-display-panels` `ferrooxidans_lcd_indium_bioleaching_graph` `tth_hydrolase` dual-species label/description): **Confirmed resolved**.
- **Cycle 6 Stage 1–3 Additions**:
  - **Stage 1 (`PR #884`)**: Added 5 IMA-CNMNC Round 124 critical-element mineral species records (`cmmmech:laurentthomasite`, `cmmmech:moabite`, `cmmmech:vielleaureite-ce`, `cmmmech:wumuite`, `cmmmech:xianhuaite-ce`). Formulae, IMA approval numbers, type localities, and empirical compositions match IMA-CNMNC September 2026 (`pp. 129, 152, 246, 255, 256`), Wilson (`2025`, *Mineralogical Magazine* `89:177-182`), Ragu et al. (`2025`, *European Journal of Mineralogy* `37:627-643`), Xue et al. (`2026`, *Journal of Geosciences*), and Yang et al. (`2026`, *American Mineralogist* `111(3):449-459`). Two of these 5 records (`vielleaureite-ce.yaml` and `xianhuaite-ce.yaml`) state IMA symbols (`Vlr-Ce`, `Xhu-Ce`) in `description` but omit the top-level `ima_symbol` slot (`cmmmech-cycle6-stage4-finding-0003`).
  - **Stage 2 (`PR #888`) & Stage 3 (`PR #893`)**: Expanded 5 `Acidithiobacillus` sulfur/iron-oxidation records (`cmmmech:chromite-beneficiation-tailings`, `cmmmech:jarosite`, `cmmmech:nickel-laterite-ore`, `cmmmech:nickel`, `cmmmech:petroleum-coke`) with multi-step `causal_graphs` (26 nodes, 21 edges, 11 `GENE_OR_PROTEIN` nodes) and 24 synchronized UniProtKB `protein_examples` per layer (48 total across `mechanisms` and `causal_graphs`). All 5 records pass with `0` open findings.

## 3. Open Findings Preserved for Cycle 6 Stage 5 (`resolve_review_findings`)

In accordance with the Stage 4 read-only record boundary (`data/records/*.yaml` unmodified during Stage 4), all 3 confirmed minor findings across `19` distinct records are preserved with `status: "open"` and listed in `carry_forward_ids` for grouped remediation in Stage 5:

| Finding ID | Issue Key | Severity | Category | Affected Records (`count`) | Summary & Stage 5 Remediation |
| --- | --- | --- | --- | --- | --- |
| `cmmmech-cycle6-stage4-finding-0001` | `cmmmech.traction-battery-hydrometallurgical-residue.tth-hydrolase-consortium-label-and-description-omit-species-and-loci` | `minor` | `graph` | `1` (`cmmmech:traction-battery-hydrometallurgical-residue`) | `causal_graphs[0].nodes[1]` (`tth_hydrolase`) is grounded to 4 consortium `protein_examples` across *A. ferrooxidans* (`tth` / `AFE_0029`), *A. thiooxidans* (`tth` `GCD22_14205` / `GCD22_02315`), and *A. caldus* (`Atc_1595` / `TetH`), but uses `label: "Tth / TetH tetrathionate hydrolase (consortium tth)"` (omitting `tetH` from the parenthetical) and a generic `description` that omits all grounded consortium species and locus tags, whereas sibling node `sqr_reductase` explicitly lists all grounded consortium species and locus tags. Update `label` and `description` in Stage 5. |
| `cmmmech-cycle6-stage4-finding-0002` | `cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci` | `minor` | `graph` | `16` (`2` `element`: `cmmmech:arsenic`, `cmmmech:gallium`; `14` `secondary_resource`: `automotive-wastewater-treatment-sludge`, `blast-furnace-cast-house-dust`, `copper-smelter-slag`, `discarded-led-lamps`, `electric-arc-furnace-dust`, `gaas-production-hydroxide-sludge`, `gold-mine-tailings`, `metallic-machining-burrs`, `nickel-based-superalloy-residue-powders`, `spent-alkaline-zinc-carbon-batteries`, `spent-automotive-three-way-catalyst`, `spent-hydrodesulfurization-catalyst`, `spent-selective-catalytic-reduction-catalyst`, `spent-sulfuric-acid-production-catalyst`) | Across 16 single-species *A. thiooxidans* records whose `tth_hydrolase` node was expanded in Cycle 5 Stage 3 (`PR #872`) to include both *A. thiooxidans* ATCC 19377 paralogs (`UniProtKB:A0A5P9XPU3` `tth` / `GCD22_14205` and `UniProtKB:A0A5P9XS05` `tth` / `GCD22_02315`), `causal_graphs[0].nodes[1]` still retains the pre-expansion singular `label: "Tth tetrathionate hydrolase (tth)"` and generic `description` without naming `GCD22_14205` and `GCD22_02315`, whereas sibling node `sqr_reductase` explicitly names `(Sqr/Sqor; GCD22_02301 / GCD22_03207)` and the 5 Cycle 6 Stage 2/3 *A. thiooxidans* records explicitly name `(tth GCD22_14205; tth GCD22_02315)`. Update `label` and `description` across all 16 records in Stage 5. |
| `cmmmech-cycle6-stage4-finding-0003` | `cmmmech.round124-minerals.missing-ima-symbol-slot` | `minor` | `completeness` | `2` (`cmmmech:vielleaureite-ce`, `cmmmech:xianhuaite-ce`) | Both Cycle 6 Stage 1 (`PR #884`) records state their IMA-CNMNC-approved mineral symbols in `description` (`Vlr-Ce` from Ragu et al. 2025 p. 627; `Xhu-Ce` from Yang et al. 2026 p. 449) but omit the top-level `ima_symbol` slot (`ima_symbol: Vlr-Ce` and `ima_symbol: Xhu-Ce` after `material_kind: mineral`). Populate `ima_symbol` on both records in Stage 5. |
