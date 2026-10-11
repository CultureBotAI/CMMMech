# Moolooite source investigation

UTC: 2026-10-11T22:22:17.903955+00:00

Repository: CultureBotAI/CMMMech; base `1ef6fdde620a4053fbfff99c51065082dce32d39` plus working changes. Author: codex (GPT-6; codex). This is a curator handoff, not an independent scientific review. The paired JSON contains exact search/acquisition receipts and every raw-file checksum.

## Decision and scope

Add one mineral owner, `data/records/moolooite.yaml`, with qualified fungal culture-associated crystallization. Moolooite is distinct from copper, wheatleyite and the weathered experimental ore. The complete 2021 primary was chosen for inspectable methods, original phase figures and supplementary tables. No criticality, recovery yield or industrial deployment is asserted. No schema change is needed.

IMA September 2026, original page 147, lists approved moolooite, approval 1980-082, with `Cu(C2O4)·nH2O`. The original 1986 description is not the approval year. The retained authority PDF was rechecked rather than freshly downloaded; the live official homepage links this same dated release. Its introduction and row were inspected. The main 2021 paper uses monohydrate notation, while its own Tables S1–S2 use variable hydration. The record preserves this uncertainty without assigning measured specimen water content.

## Primary evidence actually inspected

[Frank-Kamenetskaya et al. (2021), Scientific Reports 11:24239](https://doi.org/10.1038/s41598-021-03600-5): the complete nine-page publisher PDF, HTML and original JATS were acquired. All main text and references were read. Figures 1–6 were visually inspected on original pages 2 and 4–6; all six original publisher image files are also retained. The original DOCX supplement was acquired and every cell of Tables S1–S3 read from its XML; it contains no embedded image. The original paper states CC BY 4.0 on page 9. Raw full text stays outside Git.

The experiment used roughly 5 by 5 mm secondary Cu-bearing surface fragments from naturally weathered chalcopyrite-bearing Voronov Bor ore, submerged in 15 mL Czapek-Dox. The medium's exact salt recipe and 30 g/L glucose are preserved in the record. Conidia from ten-day A. niger Ch4/07 culture were added, with initial pH 5.5, 20–25°C, five to six days and triplicate assays. Live [NCBI Taxonomy 5061](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5061&mode=Info) identifies the species. [KF768341.1](https://www.ncbi.nlm.nih.gov/nuccore/KF768341.1) explicitly identifies Ch 4/07, a marble source and the same species; it is a 598-base ribosomal/ITS sequence, not a genome or strain-specific TaxID.

Figure 5b–c gives laboratory PXRD on malachite-bearing material: moolooite is assigned, with wheatleyite also present on day five and not assigned at day six. Substrate phases remain. Figure 6c–f gives corresponding morphology comparisons. Figure 5d Raman belongs to field-lichen material, so it is not transferred to every laboratory precipitate. These observations do not establish product purity, quantitative conversion or isolated copper recovery.

The separate July 2019 field survey sampled 25 weathered fragments. Figures 4, 5a,d and 6a,b support moolooite occurrence in source-identified Lecidea inops thalli/apothecia. This is kept as environmental context. Associated fungi in Table S3 are not made causal assay organisms. The field material and inoculated laboratory culture remain separate observations from the same paper.

## Controls, uncertainty and source discrepancies

- Matched sterile, killed-biomass and cell-free-metabolite arms, fragment sterilization, inoculum density and a numerical pH trajectory are not provided for this assay. Oxalate-mediated formation is proposed; no direct oxalate assay isolates live metabolism in this run.
- Residual mineral phases and transient wheatleyite prevent a pure moolooite or complete-conversion claim. Water content was not measured specimen by specimen.
- Morphology differs between carbonate and ferruginous surfaces. The proposed iron inhibition does not come from an independently varied iron-dose or rate experiment. Substitution versus adsorption is unresolved.
- Field wetting/drying dissolution and lower supersaturation are hypotheses from morphology, not a measured kinetic series.
- Main text counts five lichens, but Table S3 lists four lichen names. No count is adopted. The paper's use of “industrial sources” before its literature Table S2 is not deployment evidence.

## Search and deduplication boundary

Hidden and ignored files were included with `rg --no-ignore --hidden --follow` across 117 declared roots: current and original checkout records, research, reviews and history, plus referenced cmm research/raw directories. The search returned 228 lines, exit 0, no stderr. Full commands/roots are in `raw/dedup.json`; extracted text and metadata were searched, but binary PDFs/images/Office/ZIP contents were excluded from this text pass. This is not a machine-wide or unextracted-download absence claim.

No existing maintained moolooite record or selected 2021 experiment was found within that boundary. Prior raw matches were IMA rows and an unrelated abiotic copper-oxalate citation in Suyamud2020. Current acquired source files are distinguished from earlier coverage. The five exact live queries in the paired JSON used first returned results only, no filters or pagination. No affecting notice surfaced in the bounded exact-DOI notice search, publisher metadata or Crossref relations; no exhaustive absence is claimed.

Direct PMC web opening returned a browser check. Complete original content was obtained through legitimate publisher and Europe PMC routes instead. The first IMA landing guess returned404; the official root succeeded. DOI/title/authors were verified against primary/Crossref. Early raw filenames used second-author shorthand `zelenskaya2021`; `filename-correction.json` maps the byte-identical files to `frank2021`. Historical acquisition receipts remain immutable.

## Deferred leads and priorities

The 2023 synthetic moolooite structure paper (DOI10.3390/ijms24076786) has complete JATS retained, but its13 original figures, tables and crystallographic ZIP have not received full independent inspection here. It is not a fungal experiment, and no quantitative structure claim is imported. Current IMA plus the adopted paper's own supplement suffice to retain variable hydration.

The institutional Glukhova2018 lead contains indexed excerpts about heat-killed biomass and a Cu-oxalate phase. Its full methods and supplement remain to be checked; it usefully challenges universal claims that living cells are necessary, but no additional result is accepted from a snippet. Fomina2005, Zhao2020 metal-sheet work and the2023 brown-rot comparison are separate future leads, not replications verified in this handoff. Root owns other oxalate minerals.

First priority is independent native review of the frozen record and original artifacts. Future extensions should inspect the full inactive-biomass comparison and exact culture/feed distinctions before curation.

## Frozen outputs and checks

Record: `data/records/moolooite.yaml`, SHA256 `72144841927e02ab54655961f051db7b7d013a36dec5ca4274602bc7e0c03777`.

CREATE: `history/records/moolooite/2026-10-11T222034Z-codex-1ba2ba.yaml`, SHA256 `48cd5d3518374edb4a8a13899e5b6e68c835daa3cc3d372d01918e5801602df5`. Actual codex/GPT-6 metadata and distinct inline event are retained. Named validation exited0: `Checked 1 record(s); 0 failed.`. Batch checks and independent review remain parent-coordinated and pending at this author handoff. Baseline reuse is explicitly documented in `/private/tmp/cmm-round36-baseline-reuse.json`.

Raw artifacts: `/private/tmp/cmm-round36-moolooite-research/raw`, 39 files with sizes/checksums in the paired JSON. No external messages or Git mutations were made by this curator.
