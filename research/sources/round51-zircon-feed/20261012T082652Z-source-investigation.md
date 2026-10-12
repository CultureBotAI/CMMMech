# Zircon-feed source investigation: resolved author PDF, unresolved graphics

## Scope and provenance

UTC: 2026-10-12T08:26:52Z. Investigator: Codex `/root/round43_hardmetal`, GPT-6.
Worktree: `/private/tmp/CMMMech-expansion-round51-20261012`; branch `curate/cmm-expansion-round51-20261012`; base `466cb14cbc271ba73ba05e89ed188cfd113d06ea`.
This is a bounded successor to the [round50 assessment](../round50-zircon-feed/20261012T073447Z-source-investigation.md), concerning [source issue153](https://github.com/CultureBotAI/CMMMech/issues/153). It is a source investigation, not a scientific record review.

**Decision: defer both zircon-feed records.** A newly resolved public author-PDF route exposes Bansal's original text but does not yet provide viewable Figures1 and4 through this session's tools. Hedrich's complete original methods, graphics and supplement remain unavailable in this bounded pass. No record or canonical history was created; no existing scientific record changed.

## Search and acquisition log

Exact queries, raw responses, access results, checksums and the bounded dedup receipt are in the paired JSON and its external raw-artifact inventory. Searches used exact DOI/title, author/institutional repositories and correction/retraction terms, first returned sets only, no pagination or recency filter. The first four queries' complete response was not retained; subsequent search batches and PDF-reader outputs were saved. This distinction prevents claiming an unretained full search transcript.

| Route checked on 2026-10-12 UTC | Actual result | Evidence limit |
| --- | --- | --- |
| Coauthor Suresh Bhargava's ResearchGate full-text download link | Web reader incorrectly resolved the relative URL under `/publication/profile/`; correcting it to the observed public `/profile/` route exposed a six-page PDF's text | Direct local GET returned403HTML; no complete local PDF or new image pixels acquired |
| PDF screenshot calls through both available web wrappers | Responses contained textual image placeholders or an error, with no image content available to inspect | Neither a placeholder nor its caption is visual evidence for Figure1 or4 |
| Public browser entry point | CUA reported no browser available | No browser visual inspection occurred |
| Monash institutional Bansal record | Correct title/authors/DOI/pages; access section links DOI and Scopus only | Metadata corroboration, no observed manuscript download |
| NCL institutional repository | Web reader access error; bounded indexed search did not supply this original | No exhaustive repository absence claim |
| Leibniz Society project-volume URL `SB166.pdf` | Search result mentions Hedrich and overlapping project authors; direct request returned404HTML | Not acquired or inspected as a source of experimental claims |
| Hedrich publisher, Hannover/Freiberg and ResearchGate entries | DOI/title/author metadata consistent; author entry explicitly offers request-full-text | No author contact, purchase or unsupported methods import |

The correctly resolved author PDF is [Bansal2007](https://www.researchgate.net/profile/Suresh-Bhargava/publication/262842698_Zirconia_Enrichment_in_Zircon_Sand_by_Selective_Fungus-Mediated_Bioleaching_of_Silica/links/0c96053901ca706d23000000/Zirconia-Enrichment-in-Zircon-Sand-by-Selective-Fungus-Mediated-Bioleaching-of-Silica.pdf). It identifies DOI10.1021/la062535x and Langmuir23(9):4993–4998, agreeing with publisher/PubMed17375939. The author upload date2014-06-05 is not the original publication date2007-03-22 online/2007-04-24 issue.

## Candidate inventory and evidence boundaries

| Candidate | Source role and identity | Actual evidence state | Decision |
| --- | --- | --- | --- |
| Zircon sand | Bansal2007 primary fungal experiment, DOI10.1021/la062535x | Resolved six-page original text; prior Figures2,3,5 and two S1 artifacts hash-rechecked; Figure1 TEM/SAED and Figure4 paired sandXPS still not visually inspectable | Defer resource owner until those original images can be inspected |
| Zircon and eudialyte concentrates | Hedrich2023, Hydrometallurgy219:106068, DOI10.1016/j.hydromet.2023.106068 | Metadata/abstract; full methods, feed characterization, figures/tables and SI not acquired | Defer; preserve matched chemical/biological null result during future assessment |

The resolved Bansal text makes the remaining review targets more precise: original Figure1 is on printed4995 and Figure4 on4996. Printed4997 reverses the curve assignments when describing the two Si2p components; a future reviewer must compare the actual Figure4 before assigning either fitted component. The prose also switches Figure2B curve numbers between descriptions of as-formed and calcined material. These source inconsistencies remain unresolved, not silently repaired.

The existing [zircon](../../../data/records/zircon.yaml) species and [zirconium](../../../data/records/zirconium.yaml) element are different owners from a natural sand or concentrate. No criticality designation, microbial deployment, purified zirconia yield or closed bulk mass balance is inferred. Bansal's enzyme explanation remains a proposal; surface ratios and repeated exposures are not isolated product recovery. Hedrich's matched-pH chemical comparison must not be omitted or replaced by abstract percentages. A mechanical pilot is not a microbial industrial process.

## Deduplication, retention and checks

Ignored and hidden files were included, relevant symlinks followed, across current and original `data/records`, `research`, `reviews` and `history`, plus all existing raw/research/evidence roots cited by those textual artifacts. This pass read 3958 metadata files and searched 186 existing referenced raw roots; 9 missing referenced roots are explicitly listed in JSON. Within this scope, assigned feed owners were not found; zircon and zirconium owners were found. Binary PDFs/images/archives were not all decoded for this textual dedup, and unrelated machine directories were excluded.

Previously acquired Figures2,3,5 and both original ACS S1 files remain byte-identical. Their earlier acquisition and visual-review dates are retained; this pass's byte checks are not fresh acquisition or fresh visual review. No unchanged failed RMIT `files[]` probe or prior failed figure URL was retried as scientific progress. The two new direct downloads contain HTML, despite `.pdf` filenames, and are marked `is_pdf:false` in the acquisition receipt.

Copyrighted raw text and responses stay outsideGit. Reading access does not grant redistribution rights; the main article bears ACS2007 copyright. No bulk dataset was acquired, so dictionary/key sampling is inapplicable. No dated criticality list was assessed because no criticality claim is proposed. No applicable correction/retraction appeared in the bounded query result sets; this is not proof of absence.

The exact-base initialization receipt reuses completed round50 postmerge checks honestly. No named record validator is applicable because no record changed. The paired assessment JSON parses and both output files were checked for trailing whitespace; scientific acceptance is still deferred.

## Ranked handoff

1. Use the resolved public author PDF in an environment that can actually display or legitimately download all six pages; inspect Figures1 and4, then reassess the complete study with prior Figures2,3,5 and S1. Preserve the curve-number contradictions and distinguish surface enrichment from recovery.
2. Obtain Hedrich2023's complete original and declared supplements through legitimate publisher or repository access; resolve each feed's mineralogy, organisms, assay controls and scale before mapping any mechanism.
3. Keep issue153 open until these independent gaps are resolved. The project-volume URL is a contextual lead requiring a working publisher link, not a substitute experiment or a new accepted source.
