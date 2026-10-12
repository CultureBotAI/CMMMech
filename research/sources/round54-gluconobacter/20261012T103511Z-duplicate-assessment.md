# Gluconobacter genome-scale screen: already-curated source assessment

UTC: 2026-10-12T10:35:11Z. Actor: codex (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round54-20261012`, trusted base `5c83f27fa4d916a8432894e07031c2b5c7451a09`. Baseline reuses the completed exact published-base checks recorded in `/private/tmp/cmm-round54-initialization.json`.

## Decision

No record or history change. [Marecos et al.2025](https://doi.org/10.1038/s42003-025-08061-4) is already accepted in [neodymium](../../../data/records/neodymium.yaml), mechanism `gluconobacter_synthetic_phosphate_bioleaching`. Its current SHA-256 `3740247c0a93c9af1e068719aa552b43ead2c62b015f3ae98071972b84d88268` exactly matches the [independent scientific review](../../../reviews/structured/20261010T011852Z-neodymium-pr-science/review.yaml), whose verdict is `pass_with_limitations`. The [2026-10-09 curation handoff](../../ingests/ree-evidence.md) already explains the experiment and source limits. Later frontier mentions were discovery leads, not proof of missing curation.

The synthetic feed does not justify a new primary-resource or secondary-resource owner. Mon2 is explicitly a monazite-Nd/rhabdophane-Nd mixture; this is not pure [monazite-(Nd)](../../../data/records/monazite-nd.yaml). The separate [allanite-concentrate](../../../data/records/allanite-concentrate.yaml) owner concerns Schmitz2025 DOI10.1038/s42003-025-08109-5. Shared researchers, engineered strains and the older knockout collection do not make these the same feed experiment or independent replications of a single assay.

## Actual acquisition and inspection

Freshly acquired the complete12-page original from the [German National Library](https://d-nb.info/1370666926/34), full [EuropePMC JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12041372/fullTextXML), current Crossref metadata, NCBI442 taxonomy and all seven publisher-linked supplements. Exact URLs, response types, UTC times and checksums are in the paired JSON and acquisition receipts. The Nature page initially supplied primary extraction, but a subsequent open redirected to its identity service and failed; no access restriction was bypassed.

Primary main pages2–8 were personally viewed, covering Figures1–5 and Tables1–2. Results, methods and relevant discussion were read in original text/JATS. All seven Supplementary Information pages were viewed, including FiguresS1–S2 and TablesS1–S3. The four XLSX workbooks were inventoried; Data4A's42 bacterial assay rows were parsed and Data4B's separate structure checked. This is not a rerun of the genome-screen analysis, independent strain authentication, a diffraction refinement, or a fresh review of every archived source. Reporting Summary and the full Data1/3 data were acquired but not comprehensively reassessed.

Fresh Data4 SHA-256 `3e9725efe640ee5a510a5f0f733145172b7473c586a54e4fb1b1f2bcd685d07c` exactly equals the previously retained workbook acquired2026-10-08. Earlier HTML/text were separately checksummed, not represented as fresh downloads. NCBITaxon442 again resolves to Gluconobacter oxydans at species rank; it does not authenticate B58 or a mutant.

## Existing claims and retained limits

- Primary page2 distinguishes Mon1 (monazite-Nd, rhabdophane-Nd and Nd3PO7) from Mon2 (the first two). The genome screen and selected-strain direct assays remain separate. Source hydration notation is not adopted as an IMA species determination.
- Page8 methods support cultures diluted to20%glucose,48h biolixiviant production at30°C/200rpm, then Mon2 at1%pulp for24h at30°C/200rpm. Filtration is after contact; no precontact cell-removal claim is justified.
- Figure3 and Data4A compare twelve selected mutants with WT/pWT. Eight reported significant improvements of56–111% are relative to pWT, not substrate recovery. The fresh Data4 recheck gives110.79% for the GO_1598/pWT means and pH2.17–2.84, matching the current qualified record. Original units are micrograms Nd per gram NdPO4; no new structured concentration or yield is manufactured.
- Methods name no-bacteria controls, but Data4A's42 populated assayrows contain14 bacterial labels and no no-bacteria rows. Background-corrected absolute dissolution remains unreconstructable from that workbook alone.
- Figure5's clean GO_1096 deletion lacks the severe transposon-disruption effect; the record already preserves this. Supplementary FigureS1 uses WT, whereas main Figure3 uses pWT. TableS1 applies a different cell-density normalization and significance calculation; it is not a substitute for the main comparison.
- Similar final pH does not identify a specific chelator, redox compound or unique non-acid pathway. The paper explicitly discusses unresolved regulation and indirect effects. No isolated product, natural-ore performance or industrial deployment follows.
- Marecos Reference15 retains the2023 preprint citation text while JATS links the final Schmitz2025 allanite paper. Those are a publication lineage, not additional independent allanite experiments.

## Deduplication and notices

The fresh bounded search includes hidden and ignored files and follows relevant symlinks in both current and original records/research/reviews/history. It also searches118 existing exact files/directories referenced by the relevant Marecos/rhabdophane reports; one cited historical file is unavailable. There are32 matching corpus paths and7 matching raw paths. The complete search commands, boundaries and matches are retained in `dedup.json`. Unrelated home/temp directories and unextracted binary contents are excluded; no machine-wide absence claim is made.

Exact DOI searches with PMC and correction/retraction terms used the first returned result sets, without pagination. Current Crossref has no `update-to` entry and JATS has no related-article notice. No affecting correction was identified within this bounded scope. Existing internal counterevidence is retained rather than replaced by an invented refutation.

## Provenance, validation and handoff

The source states CC BY4.0 with potential third-party exceptions. Bulk originals, graphics and workbook cells remain outside Git under `/private/tmp/cmm-round54-gluconobacter-research`; the paired JSON pins34 raw artifacts and the acquisition/dedup/acceptance receipts. Named validation checked the unchanged neodymium record with zero failures. No CREATE/EDIT sidecar, inline event or new record-review bundle was fabricated for a no-change outcome.

The parent can retire this exact paper from the unreviewed frontier and link its existing accepted owner. Additional mechanistic chemistry would require separately verified matched-pH/metabolite evidence; genome annotations alone cannot supply it. This assessment does not re-review unchanged neodymium criticality or the separate Chlorella mechanism and does not claim publication.
