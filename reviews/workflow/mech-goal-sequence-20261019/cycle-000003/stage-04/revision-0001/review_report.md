# Stage 4 Full-Inventory Record and Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 3)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `3` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `855e0eba1fa9b8a4a975b7155ec013414e4d437e`
- **Eligible Population Reviewed**: `646 / 646` (`100%` full coverage across 6 disjoint `material_kind` cohorts + 1 cross-cohort `causal_graphs` review + 3 single-record deep-dive reviews)
- **Outcome**: `completed` (`3` open minor findings preserved across `3` records and carried forward to Stage 5 `resolve_review_findings`)

## 1. Frozen Inventory Coverage Summary

| Review ID | Kind | Cohort / Target | Reviewed / Population | Verdict | Open Findings |
| --- | --- | --- | --- | --- | --- |
| `20261024T024500Z-cycle3-stage4-element-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: element records (66/66) | `66 / 66` | `pass_with_limitations` | `None` |
| `20261024T024501Z-cycle3-stage4-mineral-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: mineral records (395/395) | `395 / 395` | `pass_with_limitations` | `None` |
| `20261024T024502Z-cycle3-stage4-mineral-group-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: mineral_group records (7/7) | `7 / 7` | `pass_with_limitations` | `cmmmech-cycle3-stage4-finding-0002` |
| `20261024T024503Z-cycle3-stage4-commodity-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: commodity records (36/36) | `36 / 36` | `pass_with_limitations` | `None` |
| `20261024T024504Z-cycle3-stage4-primary-resource-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: primary_resource records (31/31) | `31 / 31` | `pass_with_limitations` | `None` |
| `20261024T024505Z-cycle3-stage4-secondary-resource-cohort-review` | `category` | Cycle 3 Stage 4 full-cohort review: secondary_resource records (111/111) | `111 / 111` | `pass_with_limitations` | `None` |
| `20261024T024506Z-cycle3-stage4-causal-graphs-cohort-review` | `category` | Cycle 3 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (104/104) | `104 / 104` | `pass_with_limitations` | `cmmmech-cycle3-stage4-finding-0001` |
| `20261024T024507Z-humboldtine-cycle3-stage4-record-review` | `record` | Cycle 3 Stage 4 record review: cmmmech:humboldtine (Humboldtine) | `1 / 1` | `pass_with_limitations` | `cmmmech-cycle3-stage4-finding-0003` |
| `20261024T024508Z-arsenopyrite-cycle3-stage4-record-review` | `record` | Cycle 3 Stage 4 record review: cmmmech:arsenopyrite (Arsenopyrite) | `1 / 1` | `pass` | `None` |
| `20261024T024509Z-struvite-cycle3-stage4-record-review` | `record` | Cycle 3 Stage 4 record review: cmmmech:struvite (Struvite) | `1 / 1` | `pass` | `None` |

### Disjoint `material_kind` Cohort Mechanism & Causal-Graph Breakdown

| `material_kind` Cohort | Total Records | Records with `mechanisms` | Total `mechanisms` | Records with `causal_graphs` | Total `causal_graphs` | Records with `protein_examples` | Unique UniProtKB Accessions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `element` | `66` | `63` | `66` | `22` | `23` | `21` | `28` |
| `mineral` | `395` | `279` | `336` | `54` | `57` | `52` | `26` |
| `mineral_group` | `7` | `7` | `7` | `2` | `2` | `2` | `6` |
| `commodity` | `36` | `6` | `6` | `4` | `4` | `4` | `5` |
| `primary_resource` | `31` | `31` | `42` | `7` | `7` | `7` | `13` |
| `secondary_resource` | `111` | `108` | `145` | `15` | `18` | `15` | `18` |
| **Total Corpus** | **`646`** | **`494`** | **`602`** | **`104`** | **`111`** | **`101`** | **`57` (`22` `SWISS_PROT`, `35` `TREMBL`)** |

## 2. Corpus Validation & Cross-Cohort Audit Metrics

- **LinkML structural and semantic validation (`cmmmech validate --require-records`)**: `646 / 646` records passed (`0` errors).
- **Append-only curation history validation (`cmmmech validate-history --base main`)**: `962 / 962` history records passed (`0` errors).
- **Ontology ID-to-label consistency**: `181` distinct ontology CURIEs (`CHEBI`, `NCBITaxon`, `GO`, `ENVO`, `UniProtKB`, `EC`, `InterPro`, `Pfam`) plus `137` external mineral/chemical identifiers (`IMA`, `Wikidata`) audited across all `646` records; `0` cross-corpus label conflicts.
- **Causal graph & UniProtKB grounding (`104` records, `111` graphs, `492` nodes, `381` edges)**: `100%` connected DAGs, `100%` edge evidence coverage with verbatim primary-source snippets, `177` `GROUNDED` and `6` source-limited `UNGROUNDED` `GENE_OR_PROTEIN` nodes, and `223` `protein_examples` per layer across `57` unique UniProtKB accessions (`22` `SWISS_PROT` and `35` `TREMBL`).
- **Historical structured review lineage**: All `766` prior structured review bundles in `reviews/structured/` passed `scripts/record_review.py check --require-reviews --base main`, and all `3` Cycle 2 Stage 4 findings (`cmmmech-cycle2-stage4-finding-0001`, `cmmmech-cycle2-stage4-finding-0002`, `cmmmech-cycle2-stage4-finding-0003`) remain closed by verified Cycle 2 Stage 5 successor reviews.

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

1. **`cmmmech-cycle3-stage4-finding-0001` (`cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol`, `minor`, `open`)**:
   - **Target (`1` mineral record)**: `cmmmech:bixbyite-mn` (`data/records/bixbyite-mn.yaml`).
   - **Observation**: In `data/records/bixbyite-mn.yaml`, the `GENE_OR_PROTEIN` node `tg1_acidic_mn_oxidase_factor` (line 201) and its paired *Mesorhizobium australicum* WSM2073 reference-proteome homolog `UniProtKB:L0KKS2` (`L0KKS2_MESAW`, lines 161 and 240) both explicitly declare `gene_symbol: Mesau_02205`, whereas the strain-matched *Mesorhizobium* sp. TG-1 PCR amplicon entry `UniProtKB:A0A0K2YWP2` (`A0A0K2YWP2_9HYPH`) omits `gene_symbol: Mesau_02205` in both `mechanisms[0].protein_examples[0]` (lines 129-157) and `causal_graphs[0].nodes[0].protein_examples[0]` (lines 208-236).
2. **`cmmmech-cycle3-stage4-finding-0002` (`cmmmech.mineral_group.noncanonical-ima-compendium-source-id`, `minor`, `open`)**:
   - **Target (`1` mineral_group record)**: `cmmmech:olivine-group` (`data/records/olivine-group.yaml`).
   - **Observation**: Out of the `5` `mineral_group` records citing the 2019 IMA-CNMNC Nomenclature Compendium (`https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf`), `4` records (`cmmmech:biotite`, `cmmmech:chlorite`, `cmmmech:illite`, and `cmmmech:potassium-feldspar`) standardize on `id: ima_compendium_2019`, whereas `data/records/olivine-group.yaml` (line 11) keys the identical URL under `id: ima_compendium`.
3. **`cmmmech-cycle3-stage4-finding-0003` (`cmmmech.mineral.noncanonical-ch407-its-source-id`, `minor`, `open`)**:
   - **Target (`1` mineral record)**: `cmmmech:humboldtine` (`data/records/humboldtine.yaml`).
   - **Observation**: Out of the `6` *Aspergillus niger* strain Ch 4/07 oxalate biomineralization `mineral` records citing GenBank ITS accession `KF768341.1` (`https://www.ncbi.nlm.nih.gov/nuccore/KF768341.1`), `5` records (`cmmmech:hopeite`, `cmmmech:katsarosite`, `cmmmech:moolooite`, `cmmmech:wheatleyite`, and `cmmmech:whewellite`) standardize on `id: genbank_ch407`, whereas `data/records/humboldtine.yaml` keys this accession under `sources[4].id: genbank_niger` (line 22) and `mechanisms[0].evidence[3].source_ref: genbank_niger` (line 84).
