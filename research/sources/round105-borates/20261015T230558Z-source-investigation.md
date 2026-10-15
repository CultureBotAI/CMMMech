# CMM source investigation: inderborite and inderite

## Scope and provenance

- UTC: 2026-10-15T23:05:58.102381Z; codex / GPT-6 / codex.
- Worktree: `/private/tmp/CMMMech-expansion-round105-20261015`; branch `curate/cmm-expansion-round105-20261015`; trusted base `ee4ea8c2efa351a688946660c9ddc70560c3e86e`.
- Scope: two distinct natural borate mineral species, with abiotic laboratory crystallography. No criticality or microbial claim. Quantitative source concentrations are not converted into a recovery dataset.
- Hidden and ignored text files and relevant symlinks were searched across worktree records, research, reviews, histories and local skills; original-main reports; cited round101–104 borate downloads; and the fresh 286-issue title/body inventory. Environment, Git internals, unrelated home/temp paths and binary originals were excluded. No exact owner or alias collision was found; prior matches were contextual mentions and a round104 lead. Names, DOIs and historical lesserite/metahydroboracite aliases were checked. The paired JSON retains exact commands, limits and receipts.

## Search and acquisition log

All retained raw files and UTC acquisition receipts are under `/private/tmp/cmm-round105-borates-research`. The paired JSON enumerates every URL, HTTP outcome, byte count and SHA-256, including unsuccessful endpoints. These are fresh round105 acquisitions, including the IMA authority list even though its bytes match the prior edition already on disk.

| Source | Version / acquisition | Decision |
|---|---|---|
| [Comboni et al. 2024](https://doi.org/10.1180/mgm.2024.29) | Publisher 9-page PDF; original 6-page SI; ZIP with four CIFs | Inderborite pressure evidence, bounded |
| [Gatta et al. 2024](https://doi.org/10.2138/am-2023-9162) | Institutional 25-page Revision_1; final PDF inaccessible | Inderborite natural identity; disclose version |
| [Gatta et al. 2024](https://doi.org/10.1007/s00269-024-01281-w) | Complete publisher 18-page PDF from DNB; original publisher CIF | Inderite chemistry / neutron identity |
| [Comboni et al. 2023](https://doi.org/10.1016/j.solidstatesciences.2023.107187) | Institutional 25-page accepted Revision_1; embedded Figure S1; separate pressure SI/CIF not obtained | Narrow inderite pressure evidence |
| [IMA-CNMNC September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | 244-page official list; definitions pp.1–2 and species rows p.101 | Species identity / status authority |

Cambridge and Springer articles display CC-BY4.0; the IMA list displays CC-BY-SA3.0. Repository copyright notices do not justify wholesale manuscript redistribution. Raw scientific originals and page images remain external. Crossref dates identify 2024 publication for both neutron articles; the 2023 string in the inderborite neutron DOI is not the publication year. PDF metadata dates and manuscript labels are not substituted for issue dates.

## Evidence and limits

### Inderborite

IMA lists **G / 1941**, an original-description year. The natural Inder sample's sheets and hydrogen-bond connections are supported by the neutron Revision_1 methods pp.5–9, Tables1–2 and Figures1–2. Three EPMA crystals contained quartz micro-inclusions and showed modest beam damage. No general purity, ore grade or minor-element recovery claim follows. Separate neutron CIFs and the final publisher PDF remain unavailable.

The complete 2024 pressure study used two tiny crystals in separate helium-loaded diamond-anvil cells at ESRF ID15b. Table1 gives distinct sampled brackets: **8.11(5)–8.80(5) GPa** for arm1 and **7.45(5)–8.96(5) GPa** for arm2. The reported ~7% first-arm volume discontinuity and fitted **41(1)GPa** starting-phase bulk modulus are different quantities. High-pressure reflections deteriorated strongly (Figure3), and neither a unique space group nor a structure was solved. Non-recovery is limited to experimental duration and crystal damage.

Retained conflicts: p.475 maximum9.84(5)GPa versus Table1/abstract10.10(5); opposite prose versus Table2 angle directions; first CIF pressure tag330000 versus cell metrics matching the0.43GPa point; unexplained near10/19.919 quadratic elongations in SI TableS1. Four CIFs contain H-free starting-phase models; their doubled non-H formula with Z2 is consistent with site counts and is not evidence of dehydration. Neutron manuscript p.12 confuses an O···O distance with the H···O value2.271(4)Å from Table2; that detail is excluded. Hydrogen-bond deformation under pressure remains an inference from oxygen geometry. FigureS3's comparative water-content trend explicitly has an inderite exception.

### Inderite

IMA lists **A / 1962 s.p.**, a special procedure rather than a sequential approval number. The complete 2024 study characterizes Kramer material with EPMA, LA-ICP-MS and neutron diffraction at280/10K. Two EPMA crystals and an assumed B/H stoichiometry are not a bulk resource survey. Table1 Li2.23±1.22wtppm is a mean with1σ uncertainty, not a hard universal upper limit. Tables2–5 and Figures1–2 show molecular clusters linked by hydrogen bonds; the O9w split model0.60(10)/0.40(10) at280K is unsupported at10K, and its physical cause remains uncertain.

The original three-model CIF labels its blocks “inderborite”, but its mineral-name fields, formula, cells and symmetry consistently match inderite. A malformed Mg token and extra underscore in a radiation-source tag preclude calling it a validated automatic-ingestion input.

The 2023 pressure manuscript directly supports a single-crystal transition and ambient recovery. **Table1 / §§4.1,4.3 / conclusions:6.15(5)–6.45(5)GPa**; **abstract / §3.1 / 2024p.16:6.45–6.94GPa**, even while showing the high-pressure cell at6.45GPa. Abstract HPbulk modulus37(4)GPa conflicts with Table2/results41(5); §4.3 maximum17.41(5) conflicts with Table1's17.04(5). The doubled cell volume is normalized by2 in the ~7% transition comparison. The high-pressure cell persists at5.43(5)GPa on decompression; ambient recovery does not locate a reverse threshold or eliminate hysteresis. Separate pressure TablesS1–S2/CIFs remain unavailable, so detailed water-site/bond changes are not independently verified. Boron coordination change is not a redox claim.

## Review and correction checks

Full texts were read with complete extraction and page rendering; relevant methods, figures and tables were visually inspected. Exact page lists are in the paired JSON, without claiming every rendered page was individually viewed. Original CIF identity/chemical/symmetry/cell/temperature/pressure and atom loops were compared against their parent articles. These deposits and repository mirrors are not independent experiments.

Bounded DOI/name searches for corrections, corrigenda and retractions found no separate correction; the four fresh Crossref objects had no update-to entry and empty relation maps. This does not prove worldwide absence. Source inconsistencies remain in the owners. ScienceDirect / GeoScienceWorld routes returned403; the Elsevier API returned metadata only, not full text. An old mineral-society archive endpoint refused connection. Legitimate openly released manuscripts support narrower claims. No access failure was represented as evidence that a source does not exist.

## Priorities and handoff

1. Independently review both owner/history snapshots. Named validation passed: **2 records,0 failed**. Parent confirmed baselinePASS before writes. Separate final corpus/history/native-review gates remain pending at this dossier timestamp.
2. Obtain authoritative clarification of inderborite pressure/angle/CIF and SI-distortion discrepancies, preserving arm-specific evidence. Acquire the neutron final version/deposit before extending detailed H geometry.
3. Obtain inderite pressure final text and original pressure SI/CIFs to resolve bracket, modulus and maximum-pressure contradictions; correct neutron CIF labeling/syntax through authoritative evidence before automated reuse.

The all-state issue title/body inventory had no matching issue; issue comments were not searched. New source-clarification issue drafts are external for the root agent to deduplicate/post. Existing hydroboracite issue393 concerns a different experiment and is not claimed resolved. No third candidate is introduced. Schema and validator behavior were unchanged.
