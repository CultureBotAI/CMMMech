# Hydrocerussite source investigation, round 72

Recorded UTC 2026-10-14T13:12:16.279357+00:00. Trusted base `a2f08edab1307aba4281ce1e2a54d84bca88a889`; worktree `/private/tmp/CMMMech-expansion-round72-20261014`. Curated owner: `data/records/hydrocerussite.yaml`, pending independent scientific acceptance. This is a new mineral owner for a known experiment, not a new discovery or an independent replication of its appearances under lead and pyromorphite.

## Selection and identity

The official September 2026 IMA-CNMNC master list, PDF page 97, names Hydrocerussite, Pb3(CO3)2(OH)2, grandfathered status and original-description year 1877. Pages 1–2 define the fields and distribution terms. Original round71 acquisition at 2026-10-14T12:15:54.337356+00:00 was reused and reinspected, not described as a fresh round72 download. The SHA256 is `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`. No approval-number identifier was fabricated from the historical year, and no criticality was inherited from elemental lead or a commodity list.

Hidden/ignored-inclusive followed searches covered records, research, reviews, history, docs and local skills in both main and the new worktree, plus the named round8/14/71 raw roots. The recorded query returned 51 paths without errors. Lead and pyromorphite already contextualize Kato2022; mixed galena/anglesite feeds also mention hydrocerussite. No dedicated hydrocerussite owner was found within these boundaries before curation. This is not a machine-wide inventory, and binary PDFs were not asserted text-searchable by `rg`.

## Primary evidence acquired and inspected

[Kato et al. 2022](https://doi.org/10.3390/ijms23052483), *International Journal of Molecular Sciences* 23(5), 2483, was verified against [PubMed](https://pubmed.ncbi.nlm.nih.gov/35269625/) and Crossref. The complete EuropePMC JATS matched the earlier XML hash `2739a8c13f82541cd677f82e162468f5513e43bac73e03146c0872da71d75778`. All fourteen original graphics were fetched from the publisher-deposited PMC CDN links in the retained article HTML and inspected directly. Tables 1–2 were read in original structured XML; they concern other metals and qPCR primers and do not supply a hydrocerussite recovery yield.

The [publisher supplementary ZIP](https://mdpi-res.com/d_attachment/ijms/ijms-23-02483/article_deploy/ijms-23-02483-s001.zip) is a valid 4,001,708-byte archive. Its single eight-page PDF, `ijms-1594131-supplementary.pdf`, is 4,095,673 bytes, SHA256 `f12a25ac1e5ba726812a04f4de348a493d29a50e8eb9884999fdbd506ab15f55`. All eight pages were rendered and inspected. HTTP200 from the PMC supplement route was HTML rather than a ZIP; EuropePMC's supplementaryFiles route timed out. These failures are preserved alongside the successful publisher route. No main PDF acquisition is claimed.

## Claim-level assessment

The accepted observation is a hydrocerussite-assigned component in freeze-dried, crushed cell products after a laboratory lead-acetate assay. Results 2.3 and Figure 7 show H-labelled peaks alongside P-labelled pyromorphite peaks and calculated references. Figure 11 also contains hydrocerussite-assigned peaks, but its condition mapping is internally inconsistent. A mixed ex situ assemblage does not establish a pure product, quantitative phase abundance or in-reactor kinetics.

Methods 4.4 describes washed cells shaken for 24 h at 25 degrees C. Results 2.2 selects 5.0 mM lead acetate and 1000 mg/L biomass, while that section and Methods 4.8 also print mg/mL. SI S2–S3 label mg/L; SI S1 labels dry weight g/mL. The record records this conflict rather than repairing it by plausibility. pH, shaker speed and a complete synthetic phosphate-medium recipe are not supplied for the phase experiment.

Results 2.6 and Figure 10 assign A–D to ascending phosphate concentrations; Figure 11's caption assigns them in descending order. The Discussion's low/high-phosphate phase interpretation reverses the Results prose. The original curves verify A/P and D/H labels but cannot determine which phosphate condition was actually used. No threshold or optimal phosphate setting is accepted.

Figure 6's SAED and lattice spacing identify pyromorphite, not hydrocerussite. Figure 8 section images are not phase-specific and were prepared with uranyl acetate and lead citrate stains. Figure 9 membrane-integrity staining is not proof of continued growth or metabolic necessity. The proposed respiratory source of carbonate in the Discussion/Figure 14 is not independently demonstrated by the phosphate-gene expression measurements.

SI S3 includes zero-biomass solution comparisons (caption n=3, mean/SD), retaining the limited response at 5 mM Pb with lower biomass. Its caption describes a no-metal-solution normalization despite zero-biomass comparison bars. No numerical removal fraction is transferred into a hydrocerussite yield. Centrifuged/filtered supernatant Pb is a different measurement from isolated mineral mass; matched phase controls and closed mass accounting remain absent from the reported evidence.

KKY-29 remains *Pseudomonas* sp. The [NCBI genus record 286](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/286/dataset_report) was acquired and verifies rank GENUS and label Pseudomonas. Similarity to *P. koreensis* in Figure 5 does not authorize species or strain identification. The article's data-availability statement is “Not applicable”; no sequence or raw diffraction accession was supplied there.

## Search, counterevidence and next work

The JSON records the five exact web queries, date and first-window scope. No applicable correction/retraction appeared in those returned results; Crossref update/relation fields were empty. These observations are not an exhaustive absence claim. The original's null/limited solution responses, mixed phases, processing and label conflicts are retained as direct counterweights to broad recovery or causal claims.

Further leads include the 2017 fungal carbonate study, a 2023 tailings paper and a 2026 CO2-assisted lead-fixation paper (PMID42331897). Their complete originals were not assessed here and no mechanisms were imported. An indexed author thesis abstract describes the same KKY-29 experiment and is not independent replication or a resolution of the conflicting original labels. Aluminium-dross queries returned broader bauxite/aluminium evidence in the inspected window and remain a source-discovery lead.

Priority follow-up is reconciliation of Kato2022's original phosphate-run labels, units and associated raw data through a legitimate deposited dataset or corrected original. It need not block the narrower mixed-product record, but it does block stronger phase-control and recovery claims. Independent review, batch validation and publication checks remain subsequent gates. Raw originals stay outside Git; the accompanying JSON binds nonempty source bytes and acquisition states.
