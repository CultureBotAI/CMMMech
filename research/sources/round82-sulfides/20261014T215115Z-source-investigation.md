# Round82 mercury sulfide and selenide source investigation

This source assessment supports one new owner, **metacinnabar**, from a complete primary microbial-transformation study. **Tiemannite** remains a promising source-access deferral. It is not a scientific acceptance review; an independent reviewer must assess final maintained bytes.

## Scope and deduplication

Applied the repository add-record and discover-sources skills, record contract/schema, validation tests and local review workflow. The round82 base is `d26b03c7e8346b0caabb106f1aaf8acc3ed51623`. Searches included hidden and ignored files and followed relevant symbolic links in `data`, `research`, `reviews` and `history` in the main checkout. Exact mineral names and normalized study DOIs were checked, with bounded raw follow-up in the round3 selenium and rounds75–77 sulfide acquisition roots. No matching maintained owner or accepted experiment was found. One round77 raw search result contains a general list mentioning tiemannite and clausthalite; this is a contextual name hit, not an earlier curated experiment. The separate selenium element record concerns selenite reduction and does not identify either Hg mineral. Search boundaries and outputs are retained in `dedup-assessment.json`; the filesystem beyond these roots is not claimed exhausted.

## Ranked selection and identity

1. **Metacinnabar (cubic beta-HgS)** — accepted for proposed curation. The September2026 IMA list, page141, gives HgS, grandfathered status and original-description year1870. Page1 explicitly distinguishes that year from an approval accession. The Handbook identifies cubic symmetry and distinguishes cinnabar/hypercinnabar. No invented mineral CURIE or inherited criticality is supplied.
2. **Tiemannite (cubic HgSe)** — deferred because phase-defining original figures and full SI could not be inspected. IMA page217 gives grandfathered status/year1855; the Handbook supplies the cubic species identity. Generic HgSe composition or indexed prose is not enough to accept the experiment.
3. **Cinnabar/clausthalite** — screened in initial discovery only. No extra owner is forced to satisfy a count. Cinnabar is a distinct HgS polymorph, not a synonym of metacinnabar.

## Accepted primary: Vázquez-Rodríguez et al. 2015

*Microbial- and thiosulfate-mediated dissolution of mercury sulfide minerals and transformation to gaseous mercury*. Frontiers in Microbiology6:596, DOI **10.3389/fmicb.2015.00596**. Complete11-page original PDF and official JATS acquired, together with the official11-page SI (cover plus ten numbered pages) through EuropePMC's article media archive. All seven original main figures, Table1, five SI figures, three SI tables and DataS1 were inspected; complete text and claim-bearing page graphics were read. The unrelated `unassigned-ja93SI.pdf` obtained from an early search is actually a supplement to Zhang et al.'s different *Microbial methylation of mercury sulfide nanoparticles* paper. It is retained as a screened acquisition, **not** evidence for the accepted study.

The study combines six-week field slab exposure with separate axenic laboratory incubations. Natural museum-assigned metacinnabar contains pyritic inclusions, and sulfur XANES comparisons support the source assignment locally; no whole-feed quantitative diffraction or post-autoclave pure-phase proof is claimed. Thiobacillus thioparus ATCC8158 was tested in pH7-buffered freshwater medium, aerobic/dark/room-temperature, unshaken100mL serum vials at2g/L mineral loading. Cells were pregrown with thiosulfate and the inoculum carries residual elemental sulfur; low-thiosulfate arms use variable carryover. Live/killed/no-mineral and some cell-free controls, sulfate assays, aqueous Hg and trapped gaseous Hg support coupled chemical dissolution and microbial reduction. This is transformation and potential mobilization, not industrial recovery or demonstrated environmental detoxification.

### Claim and limitation locators

- **Methods, Pure Culture Incubations; Figures3–5:** preparation, live/killed/no-mineral comparisons and volatile versus aqueous Hg outcomes. Figure5 uses2–4 biological replicates; Figures3–4 show method-duplicate variability. Cumulative volatileHg is integrated/interpolated from sampled emission rates; it is not a closed complete Hg balance.
- **Table1 and FigureS3:** sulfate-difference proxy attributes a portion of dissolution to microbial activity after correction for inoculum sulfur/sulfate and killed-arm release. The48–68percent denominator is estimated dissolution contribution, not total mineral or isolated Hg recovery. Pyritic inclusions and residual sulfur restrict phase-specific inference.
- **Figures1–2/S1–S2 and field Methods:** local beta-HgS signatures and sulfur oxidation products, with pyrite included. Genus percentages refer to classified reads, not total cells. The sterile freshwater reference lasted4weeks versus6weeks in the field and is not a fully matched field causal control.
- **Figure4:** thiosulfate-enhanced release also occurs with killed cells; an EDTA-containing series is explicitly separate. Biology is not necessary for all dissolution.
- **Figures6–7 and Methods:** natural versus synthetic commercial blackHgS differ in surface area/impurities; no variable is individually isolated. The label “100micromolar daily spike” abbreviates actual125–132micromolar additions due to volume changes. Variability and timing are preserved.
- **Supplementary DataS1:** 285bp merA fragment supports genetic potential only; no expression, protein assay, mutant or complementation proves that this enzyme caused the transformation.
- **FigureS5 versus main text/TableS3:** SI axis/caption says nanograms per cell per day, while the main text/TableS3 give attograms. This unresolved unit disagreement is not silently corrected; no normalized rate is adopted.
- **TableS3:** its low-thiosulfate scenario prose says40mM where S4–S5/main use40micromolar. The global emissions calculation is an extrapolation with strong assumptions, not an observed flux, and is excluded from accepted outcome claims.

NCBI Taxonomy931 is the current species entry for T.thioparus, with ATCC8158 and DSM505 in type material. This is a species mapping and does not independently authenticate the actual culture. No criticality entry is required or inferred.

## Deferred primary: Chang et al. 2021

*Natural organic matter facilitates formation and microbial methylation of mercury selenide nanoparticles*. Environmental Science: Nano8:67–75, DOI **10.1039/D0EN00992J**. An early shortlist message accidentally said Wang; Crossref/publisher bibliographic verification corrected this to **Chang** before any maintained record or history was written.

Indexed publisher text describes NOM-associated chemical HgSe precipitation and subsequent bacterial methylation, with HRTEM/XRD assigned to tiemannite, bulk/NOM and aging comparisons. This is an attractive distinct record, but search-index availability is not equivalent to inspected complete primary evidence. Public publisher HTML/landing access returned403; the indexed official SI URL `https://www.rsc.org/suppdata/d0/en/d0en00992j/d0en00992j1.pdf` returned404 in direct and web-tool retrieval. ResearchGate offered request-only access. No authenticated access, challenge bypass or repeated unchanged blind retry was attempted. Crossref metadata, IMA/Handbook identity and current NCBI641491 were acquired. ND132 is now Pseudodesulfovibrio mercurii, though the paper uses Desulfovibrio desulfuricans ND132; the generic D.desulfuricans species ID would be misleading.

A concrete acquisition issue draft is retained externally as `tiemannite-source-issue.md`, with missing main/SI methods and phase/control graphics, access routes and acceptance checks. The root-provided all-state issue inventory had no matching DOI/material acquisition issue; publication coordinator must verify the live queue before posting. No tiemannite record was created.

## Corrections, competing evidence and access scope

Exact-title/DOI correction/erratum/retraction searches and broader metacinnabar dissolution searches are listed in `query-log.json`. No explicit correction notice surfaced in that bounded search, and acquired Crossref records have empty relation/update fields; neither establishes universal absence. The accepted study's own controls, mixed feed, source-unit conflicts and extrapolation limits are retained as partial evidence. Older acidic microbial dissolution (Jew2014; Baldi1987), abiotic oxidative dissolution (Barnett2001; Holley2007) and the screened Zhang nanoparticle study are follow-up leads; their uninspected experiments are not adopted as replication or contradicting measurements.

Bulk originals and rendered figures remain outside Git under `/private/tmp/cmm-round82-sulfides-research`. Source URLs, acquired times, file types, byte sizes and SHA256 hashes are in the paired JSON and original acquisition receipts. Initial sandbox DNS failures are preserved separately from successful authorized public retrievals. No schema/validator change was demonstrated necessary; measurements remain qualified evidence prose because the optional numeric observation contract represents mg/kg cells, not these Hg/sulfate assays or rates.

## Completed local curation

UTC assessment: `2026-10-14T21:51:15Z`. Created `data/records/metacinnabar.yaml` and canonical `history/records/metacinnabar/2026-10-14T215020Z-codex-91f7bf.yaml`, with a separate actual-time inline CREATE event. Named strict validation checked one record with zero failures. Exact owner/history/source/acquisition hashes are in the paired JSON. Independent scientific acceptance and whole-batch checks are pending; this dossier does not claim them completed.
