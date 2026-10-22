# Stage 4 Full-Inventory Record and Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 1)

- **Repository**: `CultureBotAI/CMMMech` (`cmmmech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `1` / Stage `4` (`record_review`) / Revision `1`
- **Frozen Source Revision**: `4d878383c92b44876df3bf166d96637c7581a59e`
- **Eligible Population Reviewed**: `616 / 616` (`100%` full coverage across 6 disjoint `material_kind` cohorts + 1 cross-cohort `causal_graphs` review + 3 single-record deep-dive reviews)
- **Outcome**: `completed` (`3` open minor findings preserved and carried forward to Stage 5 `resolve_review_findings`)

## 1. Frozen Inventory Coverage Summary

| Review ID | Kind | Cohort / Target | Reviewed / Population | Verdict | Open Findings |
| --- | --- | --- | --- | --- | --- |
| `20261022T025800Z-stage4-element-cohort-review` | `category` | Stage 4 full-cohort review: element records (66/66) | `66 / 66` | `pass_with_limitations` | `None` |
| `20261022T025801Z-stage4-mineral-cohort-review` | `category` | Stage 4 full-cohort review: mineral records (365/365) | `365 / 365` | `pass_with_limitations` | `cmmmech-stage4-finding-0001` |
| `20261022T025802Z-stage4-mineral-group-cohort-review` | `category` | Stage 4 full-cohort review: mineral_group records (7/7) | `7 / 7` | `pass_with_limitations` | `None` |
| `20261022T025803Z-stage4-commodity-cohort-review` | `category` | Stage 4 full-cohort review: commodity records (36/36) | `36 / 36` | `pass_with_limitations` | `None` |
| `20261022T025804Z-stage4-primary-resource-cohort-review` | `category` | Stage 4 full-cohort review: primary_resource records (31/31) | `31 / 31` | `pass_with_limitations` | `cmmmech-stage4-finding-0003` |
| `20261022T025805Z-stage4-secondary-resource-cohort-review` | `category` | Stage 4 full-cohort review: secondary_resource records (111/111) | `111 / 111` | `pass_with_limitations` | `None` |
| `20261022T025806Z-stage4-causal-graphs-cohort-review` | `category` | Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (63/63) | `63 / 63` | `pass_with_limitations` | `None` |
| `20261022T025807Z-wulfenite-stage4-record-review` | `record` | Stage 4 record review: cmmmech:wulfenite (Wulfenite) | `1 / 1` | `pass_with_limitations` | `cmmmech-stage4-finding-0002` |
| `20261022T025808Z-phosphogypsum-stage4-record-review` | `record` | Stage 4 record review: cmmmech:phosphogypsum (Phosphogypsum) | `1 / 1` | `pass` | `None` |
| `20261022T025809Z-palladium-stage4-record-review` | `record` | Stage 4 record review: cmmmech:palladium (Palladium) | `1 / 1` | `pass` | `None` |

## 2. Corpus Validation & Cross-Cohort Audit Metrics

- **LinkML structural and semantic validation (`cmmmech validate --require-records`)**: `616 / 616` records passed (`0` errors).
- **Append-only curation history validation (`cmmmech validate-history --base main`)**: `810 / 810` history records passed (`0` errors).
- **Ontology ID-to-label consistency**: `270` distinct ontology CURIEs (`CHEBI`, `NCBITaxon`, `GO`, `ENVO`, `UniProtKB`) audited across all `616` records; `0` cross-corpus label conflicts.
- **Causal graph & UniProtKB grounding (`63` records)**: `100%` connected DAGs, `100%` edge evidence coverage with verbatim primary-source snippets, and `100%` synchronization between `mechanisms[].protein_examples` and `causal_graphs[].nodes[].protein_examples`.
- **Historical structured review lineage**: All `714` prior structured review bundles in `reviews/structured/` passed `scripts/record_review.py check --require-reviews --base main`, and all `63` historical open issue keys from earlier rounds (`round5` through `round114`) remain closed by verified successor reviews.

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

1. **`cmmmech-stage4-finding-0001` (`cmmmech.mineral.missing-ima-identifiers-on-cited-species`, `minor`, `open`)**:
   - **Targets (`17` mineral records)**: `cmmmech:alburnite` (`IMA:2012-073`), `cmmmech:briartite` (`IMA:1965-018`), `cmmmech:cavansite` (`IMA:1967-019`), `cmmmech:compreignacite` (`IMA:1964-026`), `cmmmech:falottaite` (`IMA:2013-044`), `cmmmech:greigite` (`IMA:1963-007`), `cmmmech:katsarosite` (`IMA:2020-014`), `cmmmech:lindbergite` (`IMA:2003-029`), `cmmmech:metavivianite` (`IMA:1973-049`), `cmmmech:moolooite` (`IMA:1980-082`), `cmmmech:pentagonite` (`IMA:1971-039`), `cmmmech:pertlikite` (`IMA:2005-055`), `cmmmech:regerite` (`IMA:2023-028`), `cmmmech:schwertmannite` (`IMA:1990-006`), `cmmmech:struvite-k` (`IMA:2003-048`), `cmmmech:wheatleyite` (`IMA:1984-040`), `cmmmech:zincobriartite` (`IMA:2015-094`).
   - **Observation**: Each record explicitly states its approved IMA-CNMNC species number in `description` and cites `ima_2026_09` in `sources`, but omits the structured `identifiers: [{id: IMA:YYYY-NNN, label: <Name>}]` entry present on the other 43 IMA-numbered mineral records.
2. **`cmmmech-stage4-finding-0002` (`cmmmech.wulfenite.missing-ima-master-list-source`, `minor`, `open`)**:
   - **Target (`1` mineral record)**: `cmmmech:wulfenite` (`data/records/wulfenite.yaml`).
   - **Observation**: Out of all `365` mineral records in `data/records/*.yaml`, `cmmmech:wulfenite` is the only mineral record that omits `ima_2026_09` (`The New IMA List of Minerals`, September 2026) from `sources`.
3. **`cmmmech-stage4-finding-0003` (`cmmmech.records.trailing-mechanisms-after-history`, `minor`, `open`)**:
   - **Targets (`2` primary_resource records)**: `cmmmech:cobalt-rich-ferromanganese-crusts` (`data/records/cobalt-rich-ferromanganese-crusts.yaml`) and `cmmmech:rare-earth-rich-deep-sea-mud` (`data/records/rare-earth-rich-deep-sea-mud.yaml`).
   - **Observation**: Both records serialize their top-level `mechanisms` list at the bottom of the YAML file after `curation_history` and `history_refs`, inverting the canonical section ordering used across the other `614` records.
