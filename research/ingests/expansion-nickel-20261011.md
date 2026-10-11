# Nickel expansion evidence dossier

Created 2026-10-11T04:01:36Z by Codex (GPT-6; Codex), in
`/private/tmp/CMMMech-expansion-20261011`. This is a curation handoff and source
assessment, not independent scientific acceptance. Target:
`data/records/nickel.yaml`; baseline supplied by the coordinating agent is
`76cd81d` (298 tests passed, 3 skipped, 10 records, 19 histories).

## Identity, selection and search boundary

Nickel is a new element record in this checkout. Before editing, searched
`data`, `research`, `reviews`, `history` and `.claude` with
`rg --no-ignore --hidden` for nickel, CHEBI:28112, and the candidate DOIs.
Only the existing cobalt record's nickel-manganese-cobalt battery description
matched nickel; no nickel record or candidate DOI was found within those
boundaries. Hidden and ignored files were included. No referenced local nickel
download existed in the inspected reports; this pass used its own temporary
evidence directory, not an unbounded machine-wide search.

The 2025 study was selected over the initially examined 2024 study because it
includes chemical controls that follow the biotic pH trajectories and retains
ore-dependent negative outcomes. It adds laterite evidence to a corpus whose
cobalt record currently describes spent-battery black mass. The laterite feed,
nickel element, dissolved nickel and an isolated nickel product remain distinct.

## Verified sources and precise locators

| Source | Access and role | Checked scope |
|---|---|---|
| [ChEBI CHEBI:28112](https://www.ebi.ac.uk/chebi/CHEBI:28112) | Live official entry, 2026-10-11; identity | Label nickel atom; Ni; atomic number 28; neutral atom. The record does not use it to identify an ion or ore. |
| [USGS final 2025 list on GovInfo](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm) | Full official HTML notice, 2026-10-11; criticality | Federal Register 90:50494-50497, 7 November 2025, document 2025-19813. Complete 60-item list and nickel row checked. The row's “No” is the byproduct/co-product column, not a noncritical designation. This records that edition, not an assertion about all jurisdictions or later editions. |
| [NCBI Taxonomy 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) | Official entry, 2026-10-11; species grounding | Acidithiobacillus thiooxidans, species rank; DSM 14887 is among type-strain designations. Individual strains and their contributions are supplied by the experiment, not inferred from the species ID. |
| [Hetz and Schippers 2025](https://doi.org/10.1007/s40831-025-01139-7) | Publisher full HTML, PDF text and Figure 6 image inspected live; primary experiment | Methods: Laterite Samples, Microorganisms Used in Bioleaching Experiments, Laterite Bioleaching Experiments, Liquid Samples Analyses. Results for Barro Alto and Jacare/Piaui; Figures 1-10 and captions; Discussion on reductive dissolution. Journal of Sustainable Metallurgy 11:3732-3747, first published 17 June 2025. |
| [2025 supplementary PDF](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs40831-025-01139-7/MediaObjects/40831_2025_1139_MOESM1_ESM.pdf) | PDF text/captions checked live and file acquired | Figures S1-S10; particularly S1-S3 for Jacare/Piaui. No machine-readable replicate dataset imported. Supplement S1 gives JacF biotic n=1 while S3 gives n=2; main captions generally give n=2. Do not normalize this inconsistency into a single replicate count. |

The species entry initially returned internal errors through two web routes;
the exact official Taxonomy Browser URL succeeded after search and reopening.
A guessed, unasserted NCBI identifier 104631 resolved to Lampetra ayresii and
was rejected; it appears in no curated record. Alternative Leptospirillum
ferriphilum and A. caldus identities were verified for evaluating the 2024
lead but were not copied into the selected mechanism.

## Claim assessment and limits

The maintained record holds the strain list, substrate handling, reactor scale,
medium supplements, temperatures, inoculum and pre-growth, pH treatments,
durations, measurement method and main numerical comparison. Figure 6 was
visually checked: white bars denote Ni, panels A/B/C represent BaSt/BaC/1P5;
the plotted direction agrees with the stated Results. Its percentages describe
the paper's reported metal extraction, not purified-product recovery. No
percentage is represented as an mg/kg concentration observation.

The important negative evidence is in the same experiment, so it remains a
second `partial` evidence item. Do not average the heterogeneous feeds, infer
all laterites improve with inoculation, or equate the species with a single
demonstrated causal strain. The molecular reduction route remains debated in
Discussion. Species involvement and observed dissolution are stronger claims
than a particular reductase mechanism.

Two source ambiguities are retained rather than silently repaired:

- Ferrous iron is specified at medium setup and again before adding ore; the
  exact cumulative dose cannot safely be inferred as either 3 or 6 mM.
- The abstract/discussion group the Jacare outcomes broadly with acid-only
  dissolution, while Results identify some enhancement for JacC. The record
  retains the distinction and avoids a blanket Jacare null claim.

The published means and SDs have not been recalculated from raw replicates.
Numerical significance statements are not independently recomputed. The record
does not claim a genome/strain identifier, isolated product, economic performance
or industrial deployment. The downloaded full text is CC BY 4.0 according to
the publisher; local excerpts here are paraphrases with attribution, and bulk
source files remain outside the repository.

## Acquisition receipts

Temporary directory: `/private/tmp/cmmmech-nickel-evidence-20261011`.
Successful downloads were checked as PDF or image content. Initial sandbox DNS
failure for the PDF was followed by an authorized network retry. `pdftotext`
was unavailable locally; PDF text was inspected using the web provider, and
Figure 6 was opened as a local image. Web screenshots returned citations only
and were not counted as visual inspections.

| Artifact | URL | SHA-256 | Acquisition UTC |
|---|---|---|---|
| `hetz2025.pdf` | https://link.springer.com/content/pdf/10.1007/s40831-025-01139-7.pdf | `3b6586fb3ce385b519929b0c35fbd2e7c9159e6089b9d88f6700a52af04c706e` | 2026-10-11, approximately 03:59Z |
| `hetz2025-supplement.pdf` | Publisher supplementary URL above | `46100c34e9acb70e99293a0ae228981bbf82136e7bae223736aafd95f7ff9f07` | 2026-10-11, approximately 04:00Z |
| `fig6.png` | https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40831-025-01139-7/MediaObjects/40831_2025_1139_Fig6_HTML.png | `170397f5b3d8b585e6f3fa744ca39d1032c0d92dbdf072f1ec2632cb6801dff1` | 2026-10-11, approximately 04:00Z |

## Search log and next leads

Live provider: the web search tool, 2026-10-11 UTC; first returned results only,
no pagination or date/domain filters except where specified in query text.
Exact queries:

1. `nickel bioleaching full text primary Acidithiobacillus nickel laterite bacteria 2023 2024`
2. `nickel atom ChEBI`
3. `2025 final list critical minerals nickel 2025-19813`
4. `site.ncbi.nlm.nih.gov/Taxonomy "Acidithiobacillus caldus" "33059"`
5. `"1359019" correction retraction` (broad numeric query had irrelevant hits)
6. `nickel laterite Acidithiobacillus caldus no abiotic bioleaching control inhibition nickel`
7. `"10.3389/fmicb.2024.1359019" correction`
8. `"10.3389/fmicb.2024.1359019" retraction`
9. `site.ncbi.nlm.nih.gov/Taxonomy "Leptospirillum ferriphilum" "Taxonomy ID"`
10. `"Aerobic Bioleaching of Six Brazilian Laterite Ores"`
11. `site.ncbi.nlm.nih.gov/Taxonomy "Acidithiobacillus thiooxidans" "Taxonomy ID"`
12. `"10.1007/s40831-025-01139-7" correction`
13. `"10.1007/s40831-025-01139-7" retraction`
14. `"s40831-025-01139-7" correction retraction`

No specific correction/retraction notice for the selected 2025 paper appeared
in these bounded searches or its opened publisher page. This is not an
exhaustive retraction-registry audit. Conflicting/null outcomes were searched
and retained from the primary source rather than interpreted as refuting all
nickel bioleaching.

Ranked further work:

1. **Gallium and arsenic / GaAs hydroxide sludge:**
   [Fritze et al. 2026](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1807986/full)
   surfaced as a citing primary experiment. This is a discovery lead only in
   this pass; independently inspect methods/controls and identify which
   element-specific claims are supported. A sludge resource must have its own
   identity, not inherit an element identifier or criticality.
2. **Further nickel mechanism:**
   [Hetz and Schippers 2024](https://doi.org/10.3389/fmicb.2024.1359019),
   full Frontiers text and PDF text examined, Methods 2.1-2.3, Results 3.3,
   Figures 8-10, Discussion. The Leptospirillum addition tests are useful
   counterevidence to a simple ferrous-iron requirement, but there is no
   uninoculated arm described for these runs. Keep separate from the 2025
   six-strain experiment; neither study represents a duplicate record identity.
3. **Nickel chromium inhibition:**
   [primary 2022 full-text lead](https://pmc.ncbi.nlm.nih.gov/articles/PMC8787160/),
   search results report lethal/inhibitory conditions in New Caledonian
   laterites. Full text was not assessed here, so no measurements were imported.
4. **Mechanistic counterevidence and distinct feeds:**
   [2021 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8352580/) and
   [2015 laterite tailings study](https://doi.org/10.1021/acs.est.5b00944)
   remain leads. Only snippets/abstracts were checked, not their full methods;
   do not silently transfer their outcomes into the current mechanism.

This pass establishes one reviewed-input candidate, not source exhaustion.
The coordinating agent is responsible for independent record review and the
batch gates before acceptance or publication.
