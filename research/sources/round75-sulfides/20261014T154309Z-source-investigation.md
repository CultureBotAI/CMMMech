# Round 75 copper sulfide source investigation

UTC: 2026-10-14T15:43:09.165051+00:00. Curator: codex (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round75-20261014`; branch `curate/cmm-expansion-round75-20261014`; trusted base `4cb10d22d5542370cf5fac27288907ec0d42308c`. This is source curation, not its independent scientific acceptance.

## Decision and identity

Add [djurleite](../../../data/records/djurleite.yaml) as a distinct mineral owner, with one narrowly qualified laboratory culture-associated mobilization mechanism. Keep digenite and anilite deferred. Mineral names, copper element, industrial commodities and mixed ore are different concepts; no criticality is inherited from copper.

The issuing [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), original PDF page58, lists Djurleite, Cu31S16, status A, `1967 s.p.`. Pages1-2 explain status/special procedures. This is not an invented numbered approval accession. Page57 lists Digenite, Cu1.8S, A, `1962 s.p.`. The reused original PDF, its actual source path and hash are retained in `ima-reuse.json`; the issuing URL was also opened live. The [Handbook djurleite sheet](https://handbookofmineralogy.org/pdfs/djurleite.pdf) independently gives monoclinic Cu31S16 and common association with other copper sulfides. No unverified mineral CURIE is assigned. Issuing NCBI Taxonomy XML verifies species-level `NCBITaxon:920`, Acidithiobacillus ferrooxidans; it does not authenticate Atf.6 or equate it with LD-1.

## Search, duplicates and access

The paired JSON preserves exact live queries, provider, date, first-result-set coverage and acquisition failures. Hidden/ignored-inclusive `rg --hidden --no-ignore --follow --text` searched records, research, reviews and history in both original main and isolated worktree before creation, by mineral names and exact selected/adjacent DOI fragments. Existing chalcocite owner/report mentions digenite contextually; no separate candidate owner or accepted selected-study DOI occurred in that search. Prior bornite/chalcocite raw files contain intermediacy and mixed-feed mentions, which are not phase-pure experiments.

Five relevant cited raw roots were traversed with symlink following and cycle prevention: round33-chalcocite, round32-bornite, round4-mineral-hosts, expansion-copper and round2-zinc. Fifty-nine readable text/metadata/PDF files were searched; fourteen contained one or more candidate words. No selected Fu2014 DOI or Fu2013 DOI match was found in those files. Two PDF-named failure responses were excluded explicitly. Raster images and Office/archive binaries were not text/OCR deduplicated. These are bounded relevant-source searches, not machine-wide or global novelty claims; hashes and matches are in `dedup.json`.

| Family | Actual access and decision |
| --- | --- |
| [Fu et al. 2014, DOI10.5897/AJB2013.13023](https://doi.org/10.5897/AJB2013.13023) | Complete nine-page publisher original, all pages/figures/tables inspected. Journal full-text route and journal-linked backup return identical475444-byte PDF, SHA`410bbe806aa813d8819b9ad805700514f2fd0383c983ada8e109df4538a9427a`. Accepted sole mechanism source. |
| [Fu et al. 2013](https://doi.org/10.1016/j.mineng.2012.09.018) | DOI/title and indexed original-text excerpt screened; four-page original/graphics not acquired. Related same-group study cited by2014, not accepted as independent replication. |
| [Ruan et al. 2013 Zijinshan kinetics](https://doi.org/10.1016/j.mineng.2013.01.002) | Indexed publisher sections/abstract only; direct open403. Potential abiotic digenite-separate evidence remains deferred pending original methods/figures/SI. Industrial plant context does not establish microbial phase-specific kinetics. |
| [van der Graaf et al. 2020](https://doi.org/10.3390/microorganisms8091275) | Original26-page PDF+JATS acquired. Relevant mineral text pp8-9, original Figure4/p10 and SI inventory/p20 screened only. Text suggests several Cu-sulfide species, while displayed Figure4d-f explicitly identifies chalcocite; no digenite mechanism accepted. Full main/SI assessment remains future work. |
| Anilite | IMA/Handbook association and broad searches only; no complete selected microbial primary. Deferred without owner. |

The2014 publication date is29January2014 on originalPDF, publisher and Crossref. AJOL's later11May2015 hosting date is not a second experiment or revised edition. Accepted full main and publisher landing expose no supplementary-material section/link; no external supplementary corpus is claimed absent. Initial web403/429 routes are retained; successful legitimate publisher/static/EuropePMC routes supplied actual inspected files. No access restriction was bypassed.

## Accepted experiment and scientific limits

| Dimension | Original locator and retained scope |
| --- | --- |
| Feed identity | p665/Table1: handpicked Bofang mine material, Cu71.94%, Fe1.22%, S20.53%, reported purity90.65%; XRD text names djurleite plus chalcocite, bornite, quartz. No displayed trace or quantitative phase refinement; purity calculation unspecified. Other Cu minerals prevent djurleite-only yield attribution. |
| Preparation | Porcelain milling below74µm, nitrogen storage; laboratory20g/L solids in100mL solution/250mL flask. |
| Organism | p665: adapted mine isolate Atf.6, reported A.ferrooxidans, late-log growth in optimized4.5K. No collection/sequence accession; LD-1 in related2013 is not silently equated. Hemocytometer counts do not independently establish viability. |
| Conditions | InitialpH2,30°C,160rpm,48days; distilled water compensates evaporation. NominalFe(II) series0/1.5/2.5/4.5g/L; inoculumseries0.5/1.0/1.5×10^8cells. Growth medium contains FeSO4.7H2O22g/L; leach inoculum washing/carryover is unresolved. Separate adsorption washing is not transferred. |
| Inoculum contradiction | p666 says1.0×10^8cells best for djurleite, p669 labels0.5×10^8 optimal. Do not assign Figure3 endpoint to one uniquely verified inoculum. |
| Observation | Figures1a/2a/3a and p668 show specimen-level copper mobilization and source-reported95.12% at48days with1.5g/L initialFe(II). AAS measures solutionCu; explicit fraction accounting, sampling correction and closed balance absent. Treat endpoint as reported index, not independently verified yield/product. |
| Chemical baseline/control | p665 reports36.45% on adjustment topH2; Figures1a/2a start nearthat. No matched uninoculated timecourse/verifiedsterility. Figure3a begins from a different baseline; no reconciliation supplied. Chemical release and mixedfeed preclude an exclusivelymicrobial increment. |
| Reproducibility/units | No replicationcount or uncertainty estimate stated. Figure3c and prose useeV forEh, electrode reference absent; no numerical threshold adopted. Figure2 andTable1 are repeated layouts, not replication. |
| Attachment | Separatep665 assay: washed cells,50mL0.001M KCl,pH2,30°C,120rpm,0.5g nominal50µm mineral. Figures4-5/Table2 support attachment observations/fits. Cell-depletion estimates andSEM do not causally prove direct enzymatic dissolution; no contactseparation/selective inhibition/chemistrymatched controls. |
| Scale | Laboratory flasks only; no isolated Cu product, pilot deployment or industrial recovery claim. |

The publication's Cu-sulfide ranking and universal direct-attack narrative are not promoted into a mineral law. Ferrous iron was not uniformly beneficial in Figure2a. Similar2013/2014 composition and reported endpoint plus shared authorship warrant lineage checking, not a claim of independent replication or misconduct. No quantitative `observations` cells are added: percentages and cellcounts are outside the native mg/kg contract.

## Corrections, contradictions and deferred next work

Exact accepted DOI/title correction/retraction searches and related abiotic/strain queries found no affecting notice in the checked result sets. Crossref `update-to` was absent and `relation` empty. This is a bounded present check, not exhaustive clearance. Source-internal contradictions are retained explicitly rather than silently corrected.

1. Independently assess final djurleite bytes against the nine-page original, especially pp665-669 and Figures1-3. Preserve the same-group lineage and unresolved inoculum/control limitations.
2. For digenite, obtain phase-specific diffraction/source data rather than infer identity from Cu/S ratios or a text range. The2020 displayed pattern is chalcocite. Complete its entire main/SI assessment before any adoptedfieldclaim. Alternatively obtain full Ruan2013 original and examine its abiotic separate purity/kinetics.
3. Acquire Fu2013 original figures and clarify Atf.6/LD-1 identity and experiment overlap. The2014 experiment stands as a single qualified source regardless.
4. Anilite remains an unselected discovery lead; no claim that all possible literature has been exhausted.

## Provenance, validation and reuse

Root's newly executed baseline completed15:40:37Z:317passed/3skipped,354records/409histories; baseline log SHA`3f9864f0655654660f602cdb78dc80724dc9bed1b40b5e8f4a2ca86106a6215c`. Curation began after its green signal. Named validation exited0:one record checked,zero failed. Final batch/review checks and independent scientific acceptance are still pending and belong to the root/reviewer workflow.

Record SHA`5535b966be63e1c98e20698f9eb4615f1917d3db7159276fbfb158ad3c81101f`; canonical CREATE [history/records/djurleite/2026-10-14T154126Z-codex-2adec1.yaml](../../../history/records/djurleite/2026-10-14T154126Z-codex-2adec1.yaml) SHA`2d6d3332e136d69afb221e19c0248a157210a8844069a80cd901f968432675c6`. A separate actual-time inline CREATE and the helper-generated history reference are attached. No schema, validator, test or shared-document change was required.

Bulk originals and rendered pages remain outsideGit at `/private/tmp/cmm-round75-sulfides-research`. Publisher landing linksCCBY4.0 while original2014PDF bears journalcopyright; no bulk redistribution is performed. Handbook is allrightsreserved; IMA statesCCBY-SA3.0; MDPI2020original isCCBY. The [paired JSON](20261014T154309Z-source-investigation.json) preserves exact source paths, nonempty sizes and hashes, failure receipts, dedup boundaries and the freeze manifest. Do not confuse downloaded-but-screened material with complete primary review.
