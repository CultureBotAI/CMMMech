# Round89 resource source investigation

Recorded 2026-10-15T06:15:18.513614+00:00; worktree `/private/tmp/CMMMech-expansion-round89-20261015`, trusted base `b797f1be3d9d7b45444e0e3f54f3845d8aeeb1ae`.

## Selection and concept boundary

Selected one new secondary-resource owner: [flue-gas-desulfurization wastewater](../../../data/records/flue-gas-desulfurization-wastewater.yaml). This is a process-generated liquid, not gypsum mineral, solid FGD residue, coal ash or selenium element. A plant-specific experiment is attached to the general feed category without creating a facility-specific alias. Existing gypsum, titanogypsum, phosphogypsum and selenium records have different feed/experiment identities. No commodity or criticality designation is inferred.

The accepted primary is EPRI report3002006089, final March2017, prepared by CH2M Hill. Its full96-page original and embedded20-sheet workbook were acquired through the public EPRI download. All main treatment methods/results were read; all22 numbered main figures and every claim-bearing table were visually inspected, including the analytical Appendix B. Appendix A is the sampling plan; Appendix C's original workbook is actually embedded, not missing. The report is a primary pilot report, not a journal article or a current regulation. No DOI is invented for it.

## Accepted claim boundary

The real feed was Pleasant Prairie Power Plant physical/chemical treatment effluent, diluted1:1 with untreated Lake Michigan service water. Municipal mixed liquor seeded the MBR and an unresolved GE culture seeded the ABMet beds. The pilot therefore supports microbial-treatment-associated concentration changes, while sterile controls and pilot-product phase characterization are absent. Supplier Figure2-4 is contextual imagery, not a new pilot selenium diffraction result. The record does not assign an unsupported taxon or imply that GAC adsorption and filtration were separately excluded.

Condition2 stage averages in Table5-1 are retained as concentration summaries. Conditions3/4 lost the target and never recovered it. The increase in selenium preceded the deliberate flow change on the same day. Sulfate reducers, oxidants, nutrient changes and inhibitory organics are proposed explanations, not isolated causal results. The commercial empty-bed target was never reached. Pilot operation is explicitly distinguished from successful full-scale deployment. Backwash measurements do not establish a pure selenium product or a mass-balanced recovery yield.

## Analytical and internal contradictions preserved

- Table4-8 and original `S7 selenium qc` rows31–46 document the initial13/11/8.2 and corrected15/22/31 micrograms/L total selenium. The source's TableB-1 omits the January19 peroxide result among selected rows; the embedded workbook contains it atE41, with the preparation note atN41. These are alternative assays of the same samples, not independent replication.
- TableB-2's January28 total17.0, dissolved9.28 and summed dissolved species135.4 are unreconciled. Censoring and blank flags remain original; no zero substitution or bulk import was performed.
- Source summary prose can overstate success: the record preserves treatment failure, lost nitrification and the failed attempts to identify a cause.
- Several recipe/summary passages conflict: ferric dosing is labelled Condition3 in Table3-1 but Condition1 in Table4-2 and supported by the narrative; nutrient stage/condition descriptions differ between Table3-2 and Table4-5. The record avoids a falsely precise harmonized dosing schedule.
- The report's approximate75% overall MBR reduction is not the exact ratio of its reported overall mean concentrations; no derived percentage is curated. TDS summary values also differ from Table4-1, so no canonical TDS average is adopted. Historical ELG targets are only source-defined experimental benchmarks, not current legal advice or criticality.

## Primary locators and raw provenance

The record's supported numbers and limits use printed pp3-1–3-8,4-12–4-26,5-2–5-5 andB-1–B-4. The PDF contains18front-matter pages: printed4-23 is PDF65 and B-4 is PDF92. Figures2-1–2-4,3-1–3-3,4-1–4-15 were visually checked; all96pages were rendered outside Git. The JSON binds the actual original PDF and embedded workbook. The latter was parsed as ZIP/XML with stored values preserved; no formulas were executed or independently recalculated. Only the relevant QC/Se sheets were substantively assessed, not every raw cell.

Copyright2017 EPRI, allrightsreserved; raw PDFs, graphics, workbook and full derived transcripts remain outside Git. This maintained report contains original paraphrase and provenance only. Live acquisition details including URLs, final HTTP state, sizes and hashes are retained in the paired JSON and external acquisition receipts.

## Deduplication and search bounds

`rg --no-ignore --hidden --follow` covered `data/records`, `research`, `reviews`, `history` for FGD identity terms and exact report/DOI identifiers. It found the existing round3selenium handoff's uncurated PMC12016495 lead, not a wastewater owner or this pilot. Relevant referenced raw roots `/private/tmp/cmm-round3-selenium-evidence-20261011` and `/private/tmp/cmm-round85-resources-research` were searched with the same hidden/ignored/followed scope; no exact FGD pilot match appeared there. This is a bounded relevant-root search, not a machinewide absence claim. Broad candidate search logs also retain prior pickling/anode/kerf matches. The parent-supplied all-state issue snapshot was refreshed before final handoff:206issues searched for FGD/ABMet/report3002006089; no matching issue appeared in that bounded snapshot. The external issue-dedup receipt binds its exact hash; this is not a timeless absence claim.

Live queries are enumerated in the JSON. The exact report/correction search found this primary and later EPRI technical reports but no affecting correction notice in the inspected first result sets; this is not exhaustive absence. A later EPRI2018 review and2014pilot citation are follow-up leads, not accepted independent counterexperiments. The primary itself supplies the strong negative/limiting evidence.

## Deferred leads and priority

1. Acquire and separately assess the complete2014EPRI ABMet pilot report3002004550 and later source-specific studies to compare feed effects without generalizing this PRB pilot's failure. The report is cited in the original; no2014experimental values are adopted.
2. PMC12016495 / DOI10.1128/aem.01222-24 remains a distinct2025community/defined-medium lead already identified in round3. Isolation from FGD wastewater alone does not prove treatment of actual effluent.
3. Solid FGD gypsum is conceptually distinct but deferred this round. Kaufman1997 DOI10.1007/BF02920467 and Graves2017 DOI10.1016/j.jenvman.2017.06.013 remained abstract/metadata-only after bounded legitimate routes and OpenAlex checks. Related1996Kaufman may share lineage. Chen DOI10.1016/j.watres.2025.124872 is also not accepted from abstract. Guo2024 DOI10.25165/j.ijabe.20241704.8227 original9pages was acquired but not fully assessed; it is abiotic precipitation, not proof of microbial FGD conversion.
4. Martin2021 DOI10.3389/fmicb.2021.675628 original11pages was acquired and its full web methods screened; actual slurry respiration is not automatically mineral recovery. NETL2021 DOI10.2172/1766571 was acquired as36-page background report, not substituted for a new primary pilot.
5. Stainless pickling sludge retains earlier acquisition gaps, and no unchanged denied publisher route was retried. Silicon kerf and raw copper anode slime require further complete-source/feed assessment; no owner is created from a search snippet.

One mistaken unverified OSTI purl445248 request returned no content and was discarded; it is not evidence or a verified route. An initial owner-writing preparation script had a quoting syntax error and the immediately following history helper rejected the nonexistent target. Neither wrote a record/history. The corrected preparation then produced the sole CREATE and valid owner; no saved artifact was rewritten.

## Curation handoff

Named strict validation passed1record/0failed. Canonical CREATE `history/records/flue-gas-desulfurization-wastewater/2026-10-15T061241Z-codex-fc9da3.yaml` is attached alongside a distinct inline event. Owner SHA256 `7765854c5dfb2ce86f5fe516bf19b63e59978b21e3b3da822118769b36a5a8e3`; history SHA256 `7745dfdb1d299a3140352cfeb1dff282a4e15c43e795faed6134b2c5a1aff215`. No schema/validator change was needed. Independent science acceptance and actual batch checks belong to the next workflow, not this source assessment.
