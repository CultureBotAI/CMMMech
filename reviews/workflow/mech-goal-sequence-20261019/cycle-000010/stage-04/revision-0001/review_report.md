# CMMMech Cycle 10 Stage 4 Full-Corpus Record Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/CMMMech`
- **Cycle**: `10`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Inventory Commit**: `0ca12c227e69903577eb76e0ee8d0dbb0314fb20`
- **Scope Frozen At**: `2026-11-06T08:30:00Z`
- **Timestamp**: `2026-11-06T09:00:09Z`
- **Coverage**: `693 / 693` eligible records (`100.0%`, `0` skipped, `0` failed)

## 1. Frozen Inventory & Cohort Breakdown

At commit `0ca12c227e69903577eb76e0ee8d0dbb0314fb20`, the `data/records/*.yaml` corpus contains `693` maintained `MaterialRecord` files across 6 disjoint `material_kind` cohorts plus 1 cross-cohort `causal_graphs` & `protein_examples` slice:

| Cohort / Slice | Eligible Records | Reviewed Records | Coverage Ratio | Records with `mechanisms` (Total `mechanisms`) | Records with `causal_graphs` (Total `causal_graphs`) | Records with `protein_examples` (Unique UniProtKB Accessions) | Structured Review Bundle (`reviews/structured/<id>/`) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `element` | `66` | `66` | `1.000` | `63` (`63` microbial, `0` abiotic-only; `66` microbial mechanisms, `0` abiotic) | `28` (`29`) | `27` (`46`) | `20261106T090000Z-cycle10-stage4-element-cohort-review` |
| `mineral` | `442` | `442` | `1.000` | `285` (`158` microbial, `127` abiotic-only; `343` total: `179` microbial, `164` abiotic) | `72` (`76`) | `70` (`77`) | `20261106T090001Z-cycle10-stage4-mineral-cohort-review` |
| `mineral_group` | `7` | `7` | `1.000` | `7` (`7` microbial, `0` abiotic-only; `7` microbial mechanisms, `0` abiotic) | `2` (`2`) | `2` (`7`) | `20261106T090002Z-cycle10-stage4-mineral-group-cohort-review` |
| `commodity` | `36` | `36` | `1.000` | `6` (`6` microbial, `0` abiotic-only; `6` microbial mechanisms, `0` abiotic) | `4` (`4`) | `4` (`6`) | `20261106T090003Z-cycle10-stage4-commodity-cohort-review` |
| `primary_resource` | `31` | `31` | `1.000` | `31` (`29` microbial, `2` abiotic-only; `42` total: `40` microbial, `2` abiotic) | `15` (`16`) | `15` (`42`) | `20261106T090004Z-cycle10-stage4-primary-resource-cohort-review` |
| `secondary_resource` | `111` | `111` | `1.000` | `108` (`85` microbial, `23` abiotic-only; `145` total: `104` microbial, `41` abiotic) | `51` (`54`) | `51` (`43`) | `20261106T090005Z-cycle10-stage4-secondary-resource-cohort-review` |
| **Total Disjoint Corpus** | **`693`** | **`693`** | **`1.000`** | **`500` (`348` microbial, `152` abiotic-only; `609` total: `402` microbial, `207` abiotic)** | **`172` (`181`)** | **`169` (`124` unique: `28` `SWISS_PROT`, `96` `TREMBL`)** | — |
| Cross-Cohort `causal_graphs` & `protein_examples` | `172` | `172` | `1.000` | `172` | `172` (`181` graphs, `821` nodes, `640` edges, `320` `GENE_OR_PROTEIN`: `314` `GROUNDED`, `6` `UNGROUNDED`) | `169` (`599` `protein_examples` per layer, `1198` total) | `20261106T090006Z-cycle10-stage4-causal-graphs-cohort-review` |

### Single-Record Deep-Dive Reviews (`kind: record`)

1. **`20261106T090007Z-calcite-cycle10-stage4-record-review`**:
   - Target: `cmmmech:calcite` (`data/records/calcite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle10-stage4-finding-0001`)
2. **`20261106T090008Z-brushite-cycle10-stage4-record-review`**:
   - Target: `cmmmech:brushite` (`data/records/brushite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle10-stage4-finding-0002`)
3. **`20261106T090009Z-strontianite-cycle10-stage4-record-review`**:
   - Target: `cmmmech:strontianite` (`data/records/strontianite.yaml`, `mineral`)
   - Verdict: `pass_with_limitations` (`cmmmech-cycle10-stage4-finding-0003`)

## 2. Verification of Prior Cycle 9 Stage 4 Findings & Cycle 10 Stage 1–3 Additions

- **Cycle 9 Stage 4 Findings (`cmmmech-cycle9-stage4-finding-0001` through `0003`)**:
  - `cmmmech-cycle9-stage4-finding-0001` (*Shewanella oneidensis* MR-1 bioelectrochemical causal graphs in `cmmmech:uranium` and `cmmmech:vanadium`): **Confirmed resolved** (`PR #943`, commit `42a12994`).
  - `cmmmech-cycle9-stage4-finding-0002` (*Shewanella oneidensis* MR-1 causal graphs in `cmmmech:rhodochrosite` and `cmmmech:chlorite`): **Confirmed resolved** (`PR #943`, commit `42a12994`).
  - `cmmmech-cycle9-stage4-finding-0003` (*Geobacter sulfurreducens* synthetic Co/Ni-asbolane bioreduction causal graphs in `cmmmech:asbolane`, `cmmmech:feitknechtite`, and `cmmmech:pyrochroite`): **Confirmed resolved** (`PR #943`, commit `42a12994`).
- **Cycle 10 Stage 1–3 Additions**:
  - **Stage 1 (`PR #945`, commit `0fbb411b`)**: Added 5 IMA-CNMNC Round 128 critical-element mineral species records (`cmmmech:bojarite`, `cmmmech:ferroberaunite`, `cmmmech:kufahrite`, `cmmmech:nannoniite`, `cmmmech:scandio-fluoro-eckermannite`). Formulae, IMA approval numbers, type localities, crystal structures, and top-level `ima_symbol` slots (`Boj`, `Fbru`, `Kuf`, `Nan`, `Sfeck`) pass with `0` open findings.
  - **Stage 2 (`PR #946`, commit `d9589c0f`) & Stage 3 (`PR #948`, commit `0ca12c22`)**: Stage 2 added `causal_graphs` (10 graphs) and initial `protein_examples` (38 entries per layer across 10 unique UniProtKB accessions) across 10 microbial records (`boron-ore-concentration-tailings`, `greigite`, `jadarite`, `lithium`, `lutetium`, `metalliferous-black-shale`, `phosphate-ore-tailings`, `seafloor-massive-sulfides`, `spodumene`, `used-photographic-fixer-solutions`), and Stage 3 added 13 companion subunit/paralog/strain `ProteinExample` entries across those 10 records (12 additional unique UniProtKB accessions). All 10 records updated in Cycle 10 Stages 2 and 3 pass with `0` open findings.

## 3. Open Findings Preserved for Cycle 10 Stage 5 (`resolve_review_findings`)

In accordance with the Stage 4 read-only record boundary (`data/records/*.yaml` unmodified during Stage 4), all 3 confirmed minor findings across `6` distinct records are preserved with `status: "open"` and listed in `carry_forward_ids` for grouped remediation in Stage 5:

| Finding ID | Issue Key | Severity | Category | Affected Records (`count`) | Summary & Stage 5 Remediation |
| --- | --- | --- | --- | --- | --- |
| `cmmmech-cycle10-stage4-finding-0001` | `cmmmech.pasteurii-rehmanji2025-geothermal-brine.template-node-edge-descriptions-and-phosphate-mislabelling` | `minor` | `graph` | `3` (`2` `mineral`: `cmmmech:calcite`, `cmmmech:vaterite`; `1` `primary_resource`: `cmmmech:lithium-bearing-geothermal-brine`) | In `data/records/calcite.yaml`, `data/records/vaterite.yaml`, and `data/records/lithium-bearing-geothermal-brine.yaml` (`rehmanji2025` / `rehmanji2025_si`, DOI `10.1039/d5ra06824j`), `nodes[2..3].description` in `causal_graphs[0]` retain generic template descriptions repeating their capitalized labels verbatim in parentheses and mentioning `/phosphate` in a phosphate-free geothermal carbonate brine (also on `edges[2].relationship`), `edges[0].evidence[0].explanation` uses a generic 70-character string, and `edges[1..2]` interpolate capitalized node labels mid-sentence with singular verb `precipitates` and `supports: support` without noting the ex situ mixed-phase XRD assignment (Figure S7 p. 24) and control/aliquot caveats (`supports: partial`). Remediate all 3 records in Stage 5. |
| `cmmmech-cycle10-stage4-finding-0002` | `cmmmech.heveran2019-brushite.template-descriptions-and-cell-free-brushite-directionality` | `minor` | `graph` | `1` (`1` `mineral`: `cmmmech:brushite`) | In `data/records/brushite.yaml` (`heveran2019`, DOI `10.1038/s41598-019-51133-9`), `nodes[2..3].description` and `edges[0..2]` in `causal_graphs[0]` retain generic template descriptions, portray brushite as formed via ureolytic alkalinization (`supports: support`) rather than precipitating initially (including in cell-free and nonureolytic *E. coli* HB101 controls, Figure 2D-E) and being replaced in bulk XRD by calcite with dissolved phosphorus returning to solution (`supports: partial`), interpolate capitalized labels mid-sentence with singular verb `precipitates`, and cite `XRD/SEM-EDS` instead of XRD, SEM, Raman, and WDS. Remediate `brushite.yaml` in Stage 5. |
| `cmmmech-cycle10-stage4-finding-0003` | `cmmmech.pasteurii-strontianite-smithsonite.template-descriptions-and-uncharacterized-modality-claims` | `minor` | `graph` | `2` (`2` `mineral`: `cmmmech:strontianite`, `cmmmech:smithsonite`) | In `data/records/strontianite.yaml` (`natalio2024`, DOI `10.1021/acsami.3c13665`) and `data/records/smithsonite.yaml` (`huang2025`, DOI `10.1016/j.bgtech.2024.100106`), `nodes[2..3].description` and `edges[0..2]` in `causal_graphs[0]` retain generic template descriptions repeating their capitalized labels in parentheses, state `carbonate/phosphate` on chloride-urea (`SrCl2`, `ZnCl2`) systems, interpolate capitalized labels mid-sentence with `supports: support` on `edges[1]` despite absent urease-inhibition or matched-pH controls (`supports: partial`), and `smithsonite.yaml` `edges[2].evidence[0].explanation` cites `FTIR, SEM-EDS` not present in `huang2025`. Remediate both records in Stage 5. |
