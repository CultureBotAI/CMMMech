# REE curation handoff — 2026-10-09

Curator: Codex (GPT-6), assigned to neodymium and fluorescent-lamp phosphor.
This is a curation evidence handoff, not an independent acceptance review.
Input: [source landscape](../sources/cmm-landscape/20261008T073140Z.md), M1/M2/A1.
Worktree: `/private/tmp/CMMMech-source-survey-20261008`, base `905388523b6e9184783989484896e4cc20297832`.
The machine UTC clock showed 2026-10-09; the shell's local date was October 8.

## Decisions and evidence locators

- [Neodymium](../../data/records/neodymium.yaml): retained existing biosorption,
  the 2022 designation and immutable history. Added a separate bioleaching
  mechanism from [Marecos et al. 2025](https://doi.org/10.1038/s42003-025-08061-4).
  Read the Results describing Mon1/Mon2, Figs. 3–5, Discussion, and Methods
  “Direct REE-bioleaching measurements.” Mon2 contains both monazite-Nd and
  rhabdophane-Nd; the method does not specify removal of cells before leaching.
  Accordingly the record calls this a biolixiviant assay without calling it
  sterile or cell-free. The twelve-mutant experiment has three replicates per
  strain, WT, pWT and a method-described no-bacteria control. No-bacteria rows
  are not in the inspected Supplementary Data 4A workbook; this limits
  reconstruction of absolute background-corrected dissolution from that file.
  No absolute extraction units are converted to a percent recovery. Eight
  statistically significant improvements of 56–111% relative to pWT are the
  paper's reported comparisons, not yields from the substrate. The GO_1096
  transposon/clean-deletion disagreement is retained as partial causal evidence.
- Inspected both sheets of
  [Supplementary Data 4](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42003-025-08061-4/MediaObjects/42003_2025_8061_MOESM6_ESM.xlsx)
  using XML values from the XLSX archive. Sheet 4A has 42 bacterial observations
  (14 strain labels, three each); final pH spans 2.17–2.84. Sheet 4B has nine
  observations (WT, clean deletion and overexpression, three each). The two
  experiments and controls are not pooled. Workbook cells contain extraction,
  final pH and final OD; no-bacteria absolute-background correction cannot be
  reconstructed from those columns alone.
- [Fluorescent-lamp phosphor](../../data/records/fluorescent-lamp-phosphor.yaml):
  new `secondary_resource`, based on
  [Schmitz et al. 2021](https://doi.org/10.1038/s41467-021-27047-4), Results
  “Disrupting the phosphate transport system increases bioleaching,” Fig. 4,
  and Methods “Direct measurement of biolixiviant pH” and “Direct measurement
  of REE bioleaching.” The assay uses clarified microbial culture liquid on
  retorted powder; it is not direct treatment of whole lamps. Retorting
  conditions are not in these assay methods. The reported 5.5% and 4.7% values
  are total-REE extraction efficiencies, with a denominator based on previously
  published feed composition, not a batch-specific digest verified in this pass.
  They are not Nd-specific, not product purity, and do not imply an 18
  percentage-point improvement. The record retains the multiple-comparison
  limitation and avoids a definitive phosphate-sensing causal mechanism.
- [USGS final US2025 list](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
  checked live on 2026-10-09: neodymium appears in the summary and p. 50496
  commodity table. Added the dated edition alongside 2022, with commodity scope
  explicit; no designation is transferred to the lamp waste.
- [ChEBI:33372](https://www.ebi.ac.uk/chebi/CHEBI:33372) was rechecked live as
  neodymium atom. The existing source date is retained because the source entry
  itself was not newly introduced. NCBITaxon:442 was resolved through
  [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=442&retmode=xml):
  `TaxId=442`, `ScientificName=Gluconobacter oxydans`, `Rank=species`.
  This identifier is not claimed to resolve B58 or an individual mutant.

## Acquisition and limits

The primary full texts and 2025 workbook were previously acquired by the
source-discovery run. They were read and checksummed again here on 2026-10-09,
not falsely described as fresh downloads:

| Retained path | SHA-256 |
|---|---|
| `/private/tmp/cmm-source-gluco2025.html` | `3010ce6ce2448298d1a649ab227e80639feb3c43faf6f59742b5781f48c56f9e` |
| `/private/tmp/cmm-source-gluco2021.html` | `c3b84ee60688329cf32d07ce957479081550f00b902180a346a3cf70bd9dd6a5` |
| `/private/tmp/cmm-source-gluco2025-supp4.xlsx` | `3e9725efe640ee5a510a5f0f733145172b7473c586a54e4fb1b1f2bcd685d07c` |

Fresh acquisitions are recorded with origin, exact acquisition UTC and hash
in [ree-acquisition.json](ree-acquisition.json). The 2021 Supplementary Data 6
was read as XLSX XML: it is an acidification-screen hit table, not the raw
Fig. 4 bioleaching assay. Sheet “A. Notable Hits Validation”, row 124, identifies
`GO_1166`/`pstC` as phosphate transport system permease protein PstC. This local
locus tag was not promoted to an external identifier. The supplementary-file
description PDF was acquired but text extraction was unavailable; no claim
rests on its uninspected contents. No large original files are committed.

Fresh web opens of the two Nature articles redirected to the publisher's
identity service; PMC opens returned a browser check. Search results resolved
both titles and DOIs, while scientific details were inspected in the retained
full texts. A live NCBI browser page had incomplete rendering; its supported
E-utilities XML endpoint supplied the verified name and rank.

## Bounded searches and deduplication

On 2026-10-09, web searches used these exact queries (first returned result set,
no pagination):

- `site.ncbi.nlm.nih.gov/Taxonomy/Browser Gluconobacter oxydans 442`
- `"10.1038/s42003-025-08061-4" correction retraction`
- `"10.1038/s41467-021-27047-4" correction retraction`
- `"Generation of a Gluconobacter oxydans knockout collection" correction retraction`
- `"Direct genome-scale screening" "Gluconobacter" correction retraction`

No formal correction/retraction notice was identified in these bounded results;
that is not an exhaustive retraction audit. The primary 2025 paper itself
supplies the relevant contrary GO_1096 deletion observation and contrasts
substrate-dependent outcomes from the 2021 waste assay; these experiments are
not treated as interchangeable replications.

Before adding records, `rg --no-ignore --hidden` searched `data`, `research`,
`reviews` and `.claude` for the two DOI suffixes, fluorescent-lamp terms and
Gluconobacter. Only the source landscape/search log matched; JSON receipts were
excluded from that text search and inspected separately. This is repository
curation deduplication, not a claim about the entire machine. No new schema
fields were needed for these narrative claims.

## Validation and handoff

Before provenance attachment, `.venv/bin/cmmmech validate
data/records/neodymium.yaml data/records/fluorescent-lamp-phosphor.yaml` checked
two records with zero failures. History was then created using `cmmmech
new-history` with actual actor/model and current UTC, and the printed paths
were attached. Final validation and independent per-record reviews cover the
completed bytes; this evidence note does not imply acceptance.
