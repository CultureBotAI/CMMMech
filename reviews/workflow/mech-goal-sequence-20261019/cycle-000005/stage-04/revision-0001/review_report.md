# Stage 4 Full-Inventory Record and Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 5)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `5` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `208134600496b954831b125033d33caa508dba8b`
- **Eligible Population Reviewed**: `668 / 668` (`100%` full coverage across 6 disjoint `material_kind` cohorts + 1 cross-cohort `causal_graphs` review + 3 single-record deep-dive reviews)
- **Outcome**: `completed` (`3` open minor findings preserved across `15` records and carried forward to Stage 5 `resolve_review_findings`)

## 1. Frozen Inventory Coverage Summary

| Review ID | Kind | Cohort / Target | Reviewed / Population | Verdict | Open Findings |
| --- | --- | --- | --- | --- | --- |
| `20261030T201000Z-cycle5-stage4-element-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: element records (66/66) | `66 / 66` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0001` |
| `20261030T201001Z-cycle5-stage4-mineral-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: mineral records (417/417) | `417 / 417` | `pass_with_limitations` | `None` |
| `20261030T201002Z-cycle5-stage4-mineral-group-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: mineral_group records (7/7) | `7 / 7` | `pass_with_limitations` | `None` |
| `20261030T201003Z-cycle5-stage4-commodity-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: commodity records (36/36) | `36 / 36` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0001` |
| `20261030T201004Z-cycle5-stage4-primary-resource-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: primary_resource records (31/31) | `31 / 31` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0002` |
| `20261030T201005Z-cycle5-stage4-secondary-resource-cohort-review` | `category` | Cycle 5 Stage 4 full-cohort review: secondary_resource records (111/111) | `111 / 111` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0003` |
| `20261030T201006Z-cycle5-stage4-causal-graphs-cohort-review` | `category` | Cycle 5 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (120/120) | `120 / 120` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0002`, `cmmmech-cycle5-stage4-finding-0003` |
| `20261030T201007Z-andreybulakhite-cycle5-stage4-record-review` | `record` | Cycle 5 Stage 4 record review: cmmmech:andreybulakhite (Andreybulakhite) | `1 / 1` | `pass` | `None` |
| `20261030T201008Z-tetrahedrite-concentrate-cycle5-stage4-record-review` | `record` | Cycle 5 Stage 4 record review: cmmmech:tetrahedrite-concentrate (Tetrahedrite concentrate) | `1 / 1` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0002` |
| `20261030T201009Z-waste-liquid-crystal-display-panels-cycle5-stage4-record-review` | `record` | Cycle 5 Stage 4 record review: cmmmech:waste-liquid-crystal-display-panels (Waste liquid crystal display panels) | `1 / 1` | `pass_with_limitations` | `cmmmech-cycle5-stage4-finding-0003` |

### Disjoint `material_kind` Cohort Mechanism & Causal-Graph Breakdown

| `material_kind` Cohort | Total Records | Records with `mechanisms` | Total `mechanisms` | Records with `causal_graphs` | Total `causal_graphs` | Records with `protein_examples` | Unique UniProtKB Accessions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `element` | `66` | `63` | `66` | `24` | `25` | `23` | `33` |
| `mineral` | `417` | `285` | `343` | `54` | `57` | `52` | `27` |
| `mineral_group` | `7` | `7` | `7` | `2` | `2` | `2` | `6` |
| `commodity` | `36` | `6` | `6` | `4` | `4` | `4` | `6` |
| `primary_resource` | `31` | `31` | `42` | `7` | `7` | `7` | `15` |
| `secondary_resource` | `111` | `108` | `145` | `29` | `32` | `29` | `23` |
| **Total Corpus** | **`668`** | **`500`** | **`609`** | **`120`** | **`127`** | **`117`** | **`63` (`22` `SWISS_PROT`, `41` `TREMBL`)** |

## 2. Corpus Validation & Cross-Cohort Audit Metrics

- **LinkML structural and semantic validation (`cmmmech validate --require-records`)**: `668 / 668` records passed (`0` errors, `0` warnings).
- **Append-only curation history validation (`cmmmech validate-history --base main`)**: `1142 / 1142` history records passed (`0` errors).
- **Ontology ID-to-label consistency**: All ontology CURIEs (`CHEBI`, `NCBITaxon`, `GO`, `ENVO`, `UniProtKB`, `EC`, `InterPro`, `Pfam`) audited across all `668` records; `0` cross-corpus label conflicts.
- **Causal graph & UniProtKB grounding (`120` records, `127` graphs, `572` nodes, `445` edges)**: `100%` connected DAGs, `100%` edge evidence coverage with verbatim primary-source support, `209` `GROUNDED` and `6` source-limited `UNGROUNDED` `GENE_OR_PROTEIN` nodes, and `316` `protein_examples` per layer across `63` unique UniProtKB accessions (`22` `SWISS_PROT` and `41` `TREMBL`).
- **Historical structured review lineage**: All `895` prior structured review bundles in `reviews/structured/` (`905` total including the `10` Cycle 5 Stage 4 review bundles) passed `scripts/record_review.py check --require-reviews --base main`, and all `3` Cycle 4 Stage 4 findings (`cmmmech-cycle4-stage4-finding-0001` on `cmmmech:traction-battery-hydrometallurgical-residue`, `cmmmech-cycle4-stage4-finding-0002` across `8` records, and `cmmmech-cycle4-stage4-finding-0003` across `16` records) remain closed by verified Cycle 4 Stage 5 successor reviews.

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

1. **`cmmmech-cycle5-stage4-finding-0001` (`cmmmech.records.criticality-before-sources-key-order`, `minor`, `open`)**:
   - **Targets (`13` records: `9` element, `4` commodity)**: `cmmmech:chromium`, `cmmmech:electrical-steel`, `cmmmech:hafnium`, `cmmmech:manganese`, `cmmmech:praseodymium`, `cmmmech:rare-earth-element-commodities`, `cmmmech:scandium`, `cmmmech:selenium`, `cmmmech:silicon-carbide`, `cmmmech:silicon`, `cmmmech:synthetic-graphite`, `cmmmech:uranium`, and `cmmmech:vanadium`.
   - **Observation**: Out of `668` corpus records, `13` records serialize top-level `criticality` before `sources`, whereas `CriticalMineralRecord` in `src/cmmmech/schema/cmmmech.yaml` and `CANONICAL_RECORD_KEYS` in `scripts/new_history.py` place `sources` before `criticality`.
2. **`cmmmech-cycle5-stage4-finding-0002` (`cmmmech.tetrahedrite-concentrate.tth-hydrolase-label-and-edge-explanation`, `minor`, `open`)**:
   - **Target (`1` primary_resource record)**: `cmmmech:tetrahedrite-concentrate` (`data/records/tetrahedrite-concentrate.yaml`).
   - **Observation**: In `data/records/tetrahedrite-concentrate.yaml`, `causal_graphs[0]` (`ferrooxidans_tetrahedrite_bioleaching_graph`) node `tth_hydrolase` (lines 304-307) retains single-species label `'Tth tetrathionate hydrolase (tth / AFE_0029)'` and generic description without `Acidithiobacillus ferrivorans` `tetH` (`UniProtKB:A0A060URH6`, reference proteome `UP000193925` strain CF27), whereas sibling node `sqr_reductase` (lines 209-212) and `edges[0].evidence[0].explanation` (line 380) explicitly name both experimental species arms (`A. ferrooxidans` and `A. ferrivorans`). In addition, `edges[0].evidence[0].explanation` (line 380) states `'individual sqr/tth/tetH genes were not mutated'`, omitting `sqr2` (`AFERRI_20483`, `UniProtKB:A0A060UMZ1`).
3. **`cmmmech-cycle5-stage4-finding-0003` (`cmmmech.waste-liquid-crystal-display-panels.tth-hydrolase-dual-species-label`, `minor`, `open`)**:
   - **Target (`1` secondary_resource record)**: `cmmmech:waste-liquid-crystal-display-panels` (`data/records/waste-liquid-crystal-display-panels.yaml`).
   - **Observation**: In `data/records/waste-liquid-crystal-display-panels.yaml`, `causal_graphs[0]` (`ferrooxidans_lcd_indium_bioleaching_graph`) node `tth_hydrolase` (lines 297-300) retains single-species label `'Tth tetrathionate hydrolase (tth / AFE_0029)'` and generic description without the two grounded `Acidithiobacillus thiooxidans` ATCC 19377 `tth` paralogs (`GCD22_14205` `UniProtKB:A0A5P9XPU3` and `GCD22_02315` `UniProtKB:A0A5P9XS05`), whereas sibling node `sqr_reductase` (lines 204-207) explicitly lists both `A. ferrooxidans` and `A. thiooxidans` paralog loci.
