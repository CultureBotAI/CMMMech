# Round83 sulfide source assessment

## Scope and provenance

Researcher: codex (GPT-6; codex), `/root/round68_iron_sulfides`. The intended isolated checkout is `/private/tmp/CMMMech-expansion-round83-20261014`, branch `curate/cmm-expansion-round83-20261014`, trusted base `6719e1fc18d122bde9ffa947ff70b6b7266622d3`. Actual assessment UTC: `2026-10-14T22:56:13.982318Z`. Frozen owner/history hashes and successful named validation are in the paired JSON. This assessment does not accept its author's record scientifically; an independent native review remains required.

The bounded search covered bismuthinite, tetradymite, clausthalite and nickeline, then stopped at one supported bismuthinite addition. Elements, nominal compounds, crystalline mineral species and mixed feeds were kept separate. No criticality-list claim is made, so no jurisdiction/list mapping is implied. No schema extension is needed.

Deduplication included hidden and ignored files and followed relevant symlinks in `data/records`, `research`, `reviews` and `history` in both the original main checkout and isolated checkout, plus the cited round8 Pb/Bi, round81 ceria, round82 sulfides and round77 sulfides raw directories. Exact commands, complete outputs and hashes are retained externally. This is a bounded search, not machine-wide absence. One initial raw-directory guess (`round81-cerianite-research`) was invalid and was replaced with the report's actual `round81-ceria-research` path before the final search. The complete issue inventory had 274 all-state entries; exact mineral/DOI title/body terms found no matching source issue. Nickeline's distinct mixed-ore owner already exists, so its experiment is not duplicated.

## Selection and source fitness

| Candidate/source | Evidence actually inspected | Decision |
|---|---|---|
| Bismuthinite; Carrasco-González et al.2024, DOI10.3390/ma17081818 | Complete ten-page original and JATS; all five original figures; issuing IMA row and complete Handbook entry | Curate a qualified abiotic synthetic-phase mechanism, pending independent record review. |
| Barton et al.2019, DOI10.1007/s10534-019-00213-4 | Publisher abstract/subscription HTML and current OpenAlex; no complete original | Existing round8/81 gap, defer microbial claim. |
| Kamaraj et al.2014, DOI10.1016/j.matchemphys.2013.11.042 | Publisher abstract and truncated methods preview; denied downloaded HTML; OpenAlex closed | Defer until complete methods and phase graphics/SI are available. |
| Yue et al.2014, DOI10.1002/btpr.1894 | Publisher abstract/search metadata, valid Crossref; challenge HTML | Existing round8 gap, defer microbial claim. |
| Clausthalite; Opara et al.2023, DOI10.3390/microorganisms11010222 | Complete26-page PDF acquired; pp1–10 text, mineral-residue paragraphs and TablesA10–A11 screened, original p22 checked visually. Official10-page SI acquired/text-extracted, not fully scientifically assessed | Defer mineral owner: no phase-specific leaching or independent structural assignment established. Potential future mixed-resource study. |
| Nickeline; Boroumand et al.2024, DOI10.1016/j.chemosphere.2024.143944 | Existing record/dossier/review and original-study discovery metadata | Duplicate experiment already represented by `nickeline-bearing-ore`; no new owner. |
| Tetradymite | Bounded initial discovery results, no full microbial primary selected | No claim or record; distinguish Bi2Te2S from tellurobismuthite Bi2Te3. |

## Accepted bismuthinite evidence

The September2026 IMA list, PDFp26, identifies Bi2S3, statusG and original-description year1832; page1 defines these fields. The complete Handbook page identifies the orthorhombic species. The IMA artifact is a previously acquired official original re-inspected now, not a new download. No synthetic sample accession or original-description year is used as a mineral identifier. The Handbook's Pbnm and the paper's Pnma labels are not harmonized by copying axes; the record restricts the shared structural description to orthorhombic.

The accepted primary is a 16April2024 Materials communication17(8):1818, DOI10.3390/ma17081818, PMID38673175, PMC11051110. The official PDF and EuropePMC JATS are manifestations of the same study, not replication. Sections2.1–2.2 and Figure1 establish abiotic bismuth-nitrate/TGA/TAA aqueous synthesis at25 or70°C for60min, followed by24h digestion, washing and70°C drying. Section3.2 explicitly says digestion occurred at room temperature. Exact bismuth/TGA quantities and the complete series matrix are not supplied. The0.1M value is a TAA stock; it is not promoted to a final reactor concentration.

Figure2 and Section3.1 assign detected peaks to bismuthinite reference00-006-0333. Neither absence of other peaks nor the authors' purity language supplies a detection limit, amorphous fraction, Rietveld phase proportion or mass recovery. The15–40nm range is a Scherrer diffraction crystallite estimate; SEM shows larger aggregated morphologies. Figures3–4 show representative structures, and Figure5 is a proposed pathway schematic. Assembly, Ostwald ripening, redissolution and ligand-directed morphology are not established as separate causal steps by these images. The source itself says TGA's directing role is unclear. Methods' minimum reported time~3min and discussion's early aliquot~1min remain unresolved. No experimental replication counts or omission controls are specified in the inspected article. Final-powder washing/drying prevents an unqualified assertion about the original wet precipitate.

No microorganisms, natural ore or waste feed, recovered-metal mass balance or industrial implementation were studied. The introductory toxicity, conclusion surface-area and prospective catalytic/sensing claims are not accepted as measurements. No separate SI is listed in the complete PDF/JATS; the Data Availability statement says data are in the article. This is an inspected-artifact result, not proof that unpublished supplementary data do not exist. Original article license is CC BY4.0; full originals remain external rather than being committed.

A bounded exact DOI/title correction/retraction/erratum search returned the original and indexing/citing pages, with no affecting notice in those returned batches. Crossref had an empty relation object and no update-to field. This does not prove universal absence. The original explicitly contrasts its interpretation of TGA's role with earlier literature, but those earlier originals were not accepted as independent contrary experiments here.

## Deferred microbial originals and access history

Barton2019 concerns D. desulfuricans ATCC27774 and Bi2S3/Bi0, but abstract HRTEM/EDX claims do not establish a verified bismuthinite mechanism. Its nominal PDF request returned subscription HTML, and OpenAlex had no open full-text route. This was an accidental repeated route before normalized DOI dedup exposed the round8/81 lineage; it provides no new access and is disclosed rather than labelled new discovery. The returned HTML is not treated as a PDF.

Kamaraj2014's abstract says orthorhombic crystal structure and hexagonal morphology; those concepts are not interchangeable. The accessible culture/methods preview is truncated and cannot verify the full experiment. Its direct download response is denied HTML. Yue2014's water–oil, SRB-mediated synthesis is an existing round8 lead; the current publisher request returned challenge HTML. Empty429 Crossref files for Barton/Kamaraj are retained failed attempts, never metadata evidence. Complete phase characterization, control arms, strain scope and processing/SI must be inspected before adding any microbial mechanism. A coherent proposed acquisition issue is retained externally for the coordinator; no source contact occurred.

## Clausthalite boundary and useful reuse

Opara2023's TableA10 assigns3.2% of elemental Pb in NC_01 to clausthalite; it does not report3.2wt% clausthalite in bulk rock. MLA-GXMAP uses SEM/EDX rather than independent structural identification in the screened material. The bioleaching assays use a mixed mine-waste feed, and TableA11 groups minor sulfides with no clausthalite-specific before/after value. Mixed-feed Pb mobilization cannot be allocated to clausthalite. Water-only controls also differ from the live/spent nutrient media. This study could support a separately scoped resource record after complete source review; it is not an accepted clausthalite transformation experiment. The official SI ZIP was successfully acquired after a distinct EuropePMC media request timed out; both outcomes are retained. No claim that the full SI was reviewed is made.

## Reproducibility and next actions

The paired JSON binds acquisitions with actual time/URL/type/status/bytes/SHA256; source originals, renders, search outputs, dedup, issue inventory, accepted owner/history and actual named-validation evidence. Bulk PDFs/challenges remain `/private/tmp/cmm-round83-sulfides-research`. Some initial web-search request strings were not separately serialized before compaction; the returned batches are preserved and the key repeated/exact query strings are explicitly recorded, without claiming a complete replayable query history.

1. Independently review the frozen bismuthinite identity/abiotic mechanism and current canonical history against the complete original and authorities.
2. Acquire the three named microbial originals through a new legitimate source route; prioritize material phase, biomass and control evidence rather than nominal compound labels. The abiotic owner does not resolve these gaps.
3. Reassess Opara's complete main/SI for a distinct mixed-resource owner only if that resource is a desired scope. Do not assign mixed-feed extraction to clausthalite.

No additional candidate expansion, source contact, GitHub mutation, schema change or global exhaustion claim occurred in this lane. Batch checks and scientific acceptance remain the coordinator/reviewer's separate actual receipts.

Named strict nonempty validation completed: one record, zero failures. Full batch gates and independent acceptance are still pending.
