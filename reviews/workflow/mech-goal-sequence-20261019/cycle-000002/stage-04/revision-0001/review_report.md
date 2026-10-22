# Stage 4 Full-Inventory Record and Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 2)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `2` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `547283a882c1d657f934434f2eb5ea9a1418771a`
- **Eligible Population Reviewed**: `631 / 631` (`100%` full coverage across 6 disjoint `material_kind` cohorts + 1 cross-cohort `causal_graphs` review + 3 single-record deep-dive reviews)
- **Outcome**: `completed` (`3` open minor findings preserved across `33` records and carried forward to Stage 5 `resolve_review_findings`)

## 1. Frozen Inventory Coverage Summary

| Review ID | Kind | Cohort / Target | Reviewed / Population | Verdict | Open Findings |
| --- | --- | --- | --- | --- | --- |
| `20261022T115000Z-cycle2-stage4-element-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: element records (66/66) | `66 / 66` | `pass_with_limitations` | `None` |
| `20261022T115001Z-cycle2-stage4-mineral-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: mineral records (380/380) | `380 / 380` | `pass_with_limitations` | `cmmmech-cycle2-stage4-finding-0001` |
| `20261022T115002Z-cycle2-stage4-mineral-group-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: mineral_group records (7/7) | `7 / 7` | `pass_with_limitations` | `None` |
| `20261022T115003Z-cycle2-stage4-commodity-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: commodity records (36/36) | `36 / 36` | `pass_with_limitations` | `None` |
| `20261022T115004Z-cycle2-stage4-primary-resource-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: primary_resource records (31/31) | `31 / 31` | `pass_with_limitations` | `None` |
| `20261022T115005Z-cycle2-stage4-secondary-resource-cohort-review` | `category` | Cycle 2 Stage 4 full-cohort review: secondary_resource records (111/111) | `111 / 111` | `pass_with_limitations` | `None` |
| `20261022T115006Z-cycle2-stage4-causal-graphs-cohort-review` | `category` | Cycle 2 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (89/89) | `89 / 89` | `pass_with_limitations` | `cmmmech-cycle2-stage4-finding-0002` |
| `20261022T115007Z-katsarosite-cycle2-stage4-record-review` | `record` | Cycle 2 Stage 4 record review: cmmmech:katsarosite (Katsarosite) | `1 / 1` | `pass_with_limitations` | `cmmmech-cycle2-stage4-finding-0003` |
| `20261022T115008Z-birnessite-cycle2-stage4-record-review` | `record` | Cycle 2 Stage 4 record review: cmmmech:birnessite (Birnessite) | `1 / 1` | `pass` | `None` |
| `20261022T115009Z-allanite-leachate-cycle2-stage4-record-review` | `record` | Cycle 2 Stage 4 record review: cmmmech:allanite-leachate (Allanite leachate) | `1 / 1` | `pass` | `None` |

### Disjoint `material_kind` Cohort Mechanism & Causal-Graph Breakdown

| `material_kind` Cohort | Total Records | Records with `mechanisms` | Records with `microbial: true` Mechanisms | Records with `causal_graphs` | Records with `protein_examples` |
| --- | --- | --- | --- | --- | --- |
| `element` | `66` | `63` | `63` | `20` | `19` |
| `mineral` | `380` | `274` | `157` | `44` | `42` |
| `mineral_group` | `7` | `7` | `7` | `2` | `2` |
| `commodity` | `36` | `6` | `6` | `4` | `4` |
| `primary_resource` | `31` | `31` | `29` | `7` | `7` |
| `secondary_resource` | `111` | `108` | `85` | `12` | `12` |
| **Total Corpus** | **`631`** | **`489`** | **`347`** | **`89`** | **`86`** |

## 2. Corpus Validation & Cross-Cohort Audit Metrics

- **LinkML structural and semantic validation (`cmmmech validate --require-records`)**: `631 / 631` records passed (`0` errors).
- **Append-only curation history validation (`cmmmech validate-history --base main`)**: `891 / 891` history records passed (`0` errors).
- **Ontology ID-to-label consistency**: `165` distinct ontology CURIEs (`CHEBI`, `NCBITaxon`, `GO`, `ENVO`, `UniProtKB`, `EC`) audited across all `631` records; `0` cross-corpus label conflicts.
- **Causal graph & UniProtKB grounding (`89` records, `94` graphs, `410` nodes, `316` edges)**: `100%` connected DAGs, `100%` edge evidence coverage with verbatim primary-source snippets, `143` `GROUNDED` and `6` source-limited `UNGROUNDED` `GENE_OR_PROTEIN` nodes, and `177` `protein_examples` across `50` unique UniProtKB accessions.
- **Historical structured review lineage**: All `740` prior structured review bundles in `reviews/structured/` passed `scripts/record_review.py check --require-reviews --base main`, and all `3` Cycle 1 Stage 4 findings (`cmmmech-stage4-finding-0001`, `cmmmech-stage4-finding-0002`, `cmmmech-stage4-finding-0003`) remain closed by verified Cycle 1 Stage 5 successor reviews.

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

1. **`cmmmech-cycle2-stage4-finding-0001` (`cmmmech.mineral.noncanonical-ima-master-list-source-ids`, `minor`, `open`)**:
   - **Targets (`30` mineral records)**: `14` using `ima2026` (`cmmmech:alicewilsonite-yce`, `cmmmech:alicewilsonite-yla`, `cmmmech:ancylite-ce`, `cmmmech:bainbridgeite-yce`, `cmmmech:burbankite`, `cmmmech:calcioancylite-la`, `cmmmech:calcioburbankite`, `cmmmech:caysichite-y`, `cmmmech:cordylite-ce`, `cmmmech:donnayite-y`, `cmmmech:gysinite-nd`, `cmmmech:kukharenkoite-ce`, `cmmmech:kuliokite-y`, `cmmmech:synchysite-ce`), `9` using `ima202609` (`cmmmech:greenockite`, `cmmmech:hawleyite`, `cmmmech:hydrotalcite`, `cmmmech:ilmenite`, `cmmmech:lorenzenite`, `cmmmech:millerite`, `cmmmech:perovskite`, `cmmmech:polydymite`, `cmmmech:pyroaurite`), and `7` using `ima_202609` (`cmmmech:azurite`, `cmmmech:brucite`, `cmmmech:cerianite-ce`, `cmmmech:dolomite`, `cmmmech:tenorite`, `cmmmech:titanite`, `cmmmech:vaesite`).
   - **Observation**: Out of `380` `mineral` records in `data/records/*.yaml`, `350` key the September 2026 IMA-CNMNC Master List (`https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf`) under the canonical source key `id: ima_2026_09`, whereas these `30` mineral records use non-canonical variant source IDs (`ima2026`, `ima202609`, or `ima_202609`).
2. **`cmmmech-cycle2-stage4-finding-0002` (`cmmmech.protein_examples.mechanism-node-evidence-explanation-drift`, `minor`, `open`)**:
   - **Targets (`2` records)**: `cmmmech:allanite-concentrate` (`data/records/allanite-concentrate.yaml`) and `cmmmech:thulium` (`data/records/thulium.yaml`).
   - **Observation**: Across `84 / 86` records carrying `protein_examples`, every `ProteinExample` entry on a `GENE_OR_PROTEIN` node in `causal_graphs[].nodes[].protein_examples` matches its paired `mechanisms[].protein_examples` entry across all fields. In `allanite-concentrate.yaml` (`UniProtKB:Q5FT13`, `UniProtKB:Q5FTI1`) and `thulium.yaml` (`UniProtKB:O34952`, `UniProtKB:Q797B3`, `UniProtKB:P54496`, `UniProtKB:O32206`), the node-level `evidence[].explanation` strings are slightly abbreviated relative to the mechanism-level `evidence[].explanation` strings.
3. **`cmmmech-cycle2-stage4-finding-0003` (`cmmmech.katsarosite.legacy-chelates-predicate-on-hopeite-solubilization`, `minor`, `open`)**:
   - **Target (`1` mineral record)**: `cmmmech:katsarosite` (`data/records/katsarosite.yaml`).
   - **Observation**: While sibling *Aspergillus niger* oxalate biomineralization causal graphs (`falottaite`, `lindbergite`, `moolooite`, `hopeite`, `humboldtine`, `whewellite`) were updated in Cycle 2 Stage 2 to use `predicate: solubilizes` (added in Cycle 1 Stage 6 under `cmmmech-infra-0003`), `niger_associated_zinc_oxalate_formation_graph` in `data/records/katsarosite.yaml` still uses `predicate: chelates` on `secreted_organic_acids -> znso4_hopeite_culture_substrate`.
