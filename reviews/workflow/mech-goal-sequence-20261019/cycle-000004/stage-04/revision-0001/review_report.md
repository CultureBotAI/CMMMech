# Stage 4 Full-Inventory Record and Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 4)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `4` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `b527ecdabb331c0ff10764032306ed3fd4a05c53`
- **Eligible Population Reviewed**: `663 / 663` (`100%` full coverage across 6 disjoint `material_kind` cohorts + 1 cross-cohort `causal_graphs` review + 3 single-record deep-dive reviews)
- **Outcome**: `completed` (`3` open minor findings preserved across `25` records and carried forward to Stage 5 `resolve_review_findings`)

## 1. Frozen Inventory Coverage Summary

| Review ID | Kind | Cohort / Target | Reviewed / Population | Verdict | Open Findings |
| --- | --- | --- | --- | --- | --- |
| `20261030T084500Z-cycle4-stage4-element-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: element records (66/66) | `66 / 66` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0003` |
| `20261030T084501Z-cycle4-stage4-mineral-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: mineral records (412/412) | `412 / 412` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0002` |
| `20261030T084502Z-cycle4-stage4-mineral-group-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: mineral_group records (7/7) | `7 / 7` | `pass_with_limitations` | `None` |
| `20261030T084503Z-cycle4-stage4-commodity-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: commodity records (36/36) | `36 / 36` | `pass_with_limitations` | `None` |
| `20261030T084504Z-cycle4-stage4-primary-resource-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: primary_resource records (31/31) | `31 / 31` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0002`, `cmmmech-cycle4-stage4-finding-0003` |
| `20261030T084505Z-cycle4-stage4-secondary-resource-cohort-review` | `category` | Cycle 4 Stage 4 full-cohort review: secondary_resource records (111/111) | `111 / 111` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0001`, `cmmmech-cycle4-stage4-finding-0002`, `cmmmech-cycle4-stage4-finding-0003` |
| `20261030T084506Z-cycle4-stage4-causal-graphs-cohort-review` | `category` | Cycle 4 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (120/120) | `120 / 120` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0001` |
| `20261030T084507Z-palladium-cycle4-stage4-record-review` | `record` | Cycle 4 Stage 4 record review: cmmmech:palladium (Palladium) | `1 / 1` | `pass` | `None` |
| `20261030T084508Z-traction-battery-hydrometallurgical-residue-cycle4-stage4-record-review` | `record` | Cycle 4 Stage 4 record review: cmmmech:traction-battery-hydrometallurgical-residue (Traction-battery hydrometallurgical residue) | `1 / 1` | `pass_with_limitations` | `cmmmech-cycle4-stage4-finding-0001` |
| `20261030T084509Z-bornite-cycle4-stage4-record-review` | `record` | Cycle 4 Stage 4 record review: cmmmech:bornite (Bornite) | `1 / 1` | `pass` | `None` |

### Disjoint `material_kind` Cohort Mechanism & Causal-Graph Breakdown

| `material_kind` Cohort | Total Records | Records with `mechanisms` | Total `mechanisms` | Records with `causal_graphs` | Total `causal_graphs` | Records with `protein_examples` | Unique UniProtKB Accessions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `element` | `66` | `63` | `66` | `24` | `25` | `23` | `32` |
| `mineral` | `412` | `284` | `341` | `54` | `57` | `52` | `26` |
| `mineral_group` | `7` | `7` | `7` | `2` | `2` | `2` | `6` |
| `commodity` | `36` | `6` | `6` | `4` | `4` | `4` | `5` |
| `primary_resource` | `31` | `31` | `42` | `7` | `7` | `7` | `13` |
| `secondary_resource` | `111` | `108` | `145` | `29` | `32` | `29` | `21` |
| **Total Corpus** | **`663`** | **`499`** | **`607`** | **`120`** | **`127`** | **`117`** | **`60` (`22` `SWISS_PROT`, `38` `TREMBL`)** |

## 2. Corpus Validation & Cross-Cohort Audit Metrics

- **LinkML structural and semantic validation (`cmmmech validate --require-records`)**: `663 / 663` records passed (`0` errors, `0` warnings).
- **Append-only curation history validation (`cmmmech validate-history --base main`)**: `1073 / 1073` history records passed (`0` errors).
- **Ontology ID-to-label consistency**: `189` distinct ontology CURIEs (`CHEBI`, `NCBITaxon`, `GO`, `ENVO`, `UniProtKB`, `EC`, `InterPro`, `Pfam`) audited across all `663` records; `0` cross-corpus label conflicts.
- **Causal graph & UniProtKB grounding (`120` records, `127` graphs, `572` nodes, `445` edges)**: `100%` connected DAGs, `100%` edge evidence coverage with verbatim primary-source snippets, `209` `GROUNDED` and `6` source-limited `UNGROUNDED` `GENE_OR_PROTEIN` nodes, and `295` `protein_examples` per layer across `60` unique UniProtKB accessions (`22` `SWISS_PROT` and `38` `TREMBL`).
- **Historical structured review lineage**: All `844` prior structured review bundles in `reviews/structured/` (`854` total including the `10` Cycle 4 Stage 4 review bundles) passed `scripts/record_review.py check --require-reviews --base main`, and all `3` Cycle 3 Stage 4 findings (`cmmmech-cycle3-stage4-finding-0001` on `cmmmech:bixbyite-mn`, `cmmmech-cycle3-stage4-finding-0002` on `cmmmech:olivine-group`, `cmmmech-cycle3-stage4-finding-0003` on `cmmmech:humboldtine`) remain closed by verified Cycle 3 Stage 5 successor reviews.

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

1. **`cmmmech-cycle4-stage4-finding-0001` (`cmmmech.traction-battery-hydrometallurgical-residue.causal-node-spurious-br-sample-codes-and-consortium-label`, `minor`, `open`)**:
   - **Target (`1` secondary_resource record)**: `cmmmech:traction-battery-hydrometallurgical-residue` (`data/records/traction-battery-hydrometallurgical-residue.yaml`).
   - **Observation**: In `data/records/traction-battery-hydrometallurgical-residue.yaml`, `causal_graphs[0]` (`ferrooxidans_battery_residue_bioleaching_graph`) node `solid_feed_substrate` (line 521) carries `label: Industrial traction-battery hydrometallurgical residues (BR1, BR2, BR4)`, where `(BR1, BR2, BR4)` are bauxite-residue sample codes from Borra et al. (2016) rather than the separate nickel-line and cobalt-line traction-battery hydrometallurgical residues in Lu et al. (2025, `lu2025`). In addition, `nodes[0].label` (`Sqr sulfide-quinone reductase (AFE_1792)`), `nodes[1].label` (`Tth tetrathionate hydrolase (tth / AFE_0029)`), and `edges[0].evidence[0].explanation` (`Reduced sulfur oxidation in A. ferrooxidans couples Sqr and polythionate hydrolysis to proton generation.`) retain single-species *A. ferrooxidans* labels whereas `sqr_reductase` and `tth_hydrolase` are grounded across the five-member acidophile consortium.
2. **`cmmmech-cycle4-stage4-finding-0002` (`cmmmech.records.mechanisms-before-sources-key-order`, `minor`, `open`)**:
   - **Targets (`8` records: `1` mineral, `1` primary_resource, `6` secondary_resource)**: `cmmmech:cadmium-telluride-photovoltaic-module-scrap`, `cmmmech:cathode-ray-tube-glass`, `cmmmech:churchite-y`, `cmmmech:end-of-life-cigs-photovoltaic-modules`, `cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules`, `cmmmech:iron-ore-tailings`, `cmmmech:polymetallic-nodules`, and `cmmmech:waste-printed-circuit-boards`.
   - **Observation**: Out of `663` corpus records, `8` records serialize top-level `mechanisms` before `sources` (and in `churchite-y` before `sources` and `criticality`), whereas `CANONICAL_RECORD_KEYS` in `scripts/new_history.py` and the LinkML `MaterialRecord` class place `sources` and `criticality` before `mechanisms` and `causal_graphs`.
3. **`cmmmech-cycle4-stage4-finding-0003` (`cmmmech.records.history-refs-before-curation-history-key-order`, `minor`, `open`)**:
   - **Targets (`16` records: `5` element, `1` primary_resource, `10` secondary_resource)**: `cmmmech:aluminium-salt-slag`, `cmmmech:beryllium`, `cmmmech:beverage-carton-hydropulping-reject`, `cmmmech:biogas-desulfurization-sulfur-residue`, `cmmmech:cesium`, `cmmmech:electroformed-copper-silver-manufacturing-scrap`, `cmmmech:ground-waste-tire-rubber`, `cmmmech:ion-adsorption-rare-earth-clay`, `cmmmech:pharmaceutical-blister-packaging-waste`, `cmmmech:rhenium`, `cmmmech:rubidium`, `cmmmech:spent-lead-acid-battery-electrolyte`, `cmmmech:spent-vanadium-flow-battery-electrolyte`, `cmmmech:strontium`, `cmmmech:zinc-leach-residue`, and `cmmmech:zinc-purification-hot-filter-cake`.
   - **Observation**: Out of `663` corpus records, `16` records serialize top-level `history_refs` before `curation_history`, whereas `CANONICAL_RECORD_KEYS` in `scripts/new_history.py` and the LinkML `MaterialRecord` class place `curation_history` before `history_refs`.
