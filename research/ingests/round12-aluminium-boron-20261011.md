# Round 12: aluminium-chain and borate commodities

Prepared 2026-10-11 UTC by codex / GPT-6 / codex in
`/private/tmp/CMMMech-expansion-round12-20261011`, trusted base
`1e52585c9019a32d37f959e0dafa00ae431f28c4`, issue #48. This assessment was
followed by the parent's explicit assignment to curate five records. The
[JSON receipt](round12-aluminium-boron-20261011.json) preserves exact queries,
URLs, retrieval times, content checks, raw hashes, record hashes and validation.
It is separate from the independent scientific reviews.

## Material decisions

| Proposal | Decision and accepted boundary | Dated designation |
|---|---|---|
| [Bauxite](../../data/records/bauxite.yaml) | Create an ore **commodity**, a heterogeneous mineral assemblage; no mineral-species or element identifier. | Original EU 2024/1252, Annex I 1(a) strategic and Annex II 1(c) critical. |
| [Alumina](../../data/records/alumina.yaml) | Create the refined aluminium-oxide **commodity**; distinct from hydroxide, metal, ore, residue and a specified purity grade. | Same explicitly named EU value-chain component. |
| [High-purity alumina](../../data/records/high-purity-alumina.yaml) | Create the refined purity-defined Al2O3 product. GA's 99.99% description is retained without inventing a universal product standard. | Australia's 20 February 2024 Critical Minerals List, Table 1. |
| [High-purity iron ore](../../data/records/high-purity-iron-ore.yaml) | Create Canada's ore/concentrate category for green steel. It is not high-purity Fe metal. No universal numerical cutoff is asserted. | Canadian 2024 list; announcement dated 10 June 2024. |
| [Borates](../../data/records/borates.yaml) | Create the commercial natural/refined borate category. Boric acid is an associated product, not a synonym for every borate. Include one narrowly qualified colemanite experiment. | BGS/CMIC UK 2024 assessment OR/24/059, Table 11, with its non-policy disclaimer. |
| Boron — metallurgy grade | Defer. The EU label is verified, but a material/product specification sufficient to delimit this grade remains unresolved. Do not treat it as a boron-element or all-borate alias. | Original EU Annex I 1(c) is a valid designation, not a composition or impurity specification. |

The [USGS commodity overview](https://www.usgs.gov/centers/national-minerals-information-center/bauxite-and-alumina-statistics-and-information)
defines bauxite as heterogeneous ore containing aluminium hydroxide minerals.
The [2025 chapter](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-bauxite-alumina.pdf),
printed pp. 42–43, separately identifies aluminium oxide and hydroxide tariff
items and the processing chain. [EU recital 8](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng)
explicitly explains why the ore and intermediate alumina are named alongside
aluminium. These are distinct records, not copied elemental mechanisms.

[Geoscience Australia's HPA description](https://www.ga.gov.au/scientific-topics/minerals/critical-minerals/critical-minerals-and-their-uses)
distinguishes the refined powder from feedstocks. The
[Australian list](https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list)
was read through the web provider; its stated update is 20 February 2024.
Direct HTML acquisition failed, so there is no invented raw-page checksum.

The [Canadian list](https://www.canada.ca/en/campaign/critical-minerals-in-canada/critical-minerals-an-opportunity-for-canada.html)
and [dated announcement](https://www.canada.ca/en/natural-resources-canada/news/2024/06/government-of-canada-releases-updated-critical-minerals-list.html)
support the named high-purity iron-ore category. They do not give a numerical
grade cutoff. The [Julienne Lake government brochure](https://www.gov.nl.ca/iet/files/2024_JulienneLake_InvestmentBrochure.pdf)
describes an ore-to-concentrate example exceeding 66% Fe with less than 5%
silica. Those project figures cannot establish a universal 67% threshold.

The historical frontier used BGS OR/24/047. The existing round10 report and
review identified its supersession; this pass reopened the
[replacement NORA item](https://nora.nerc.ac.uk/id/eprint/539735/) and rehashed
the previously acquired OR/24/059 PDF. Its cover and Tables 1/11 were inspected.
The borates record uses **OR/24/059**, not the superseded inventory edition.
This does not silently refresh the historical frontier or assert latest status.
The official UK policy annex also names borates, but this record adopts only
the specified BGS/CMIC assessment.

## Primary experiments and acceptance limits

### Borates: a limited colemanite leaching observation

[Bayat, Arslan and Bayat (2011)](https://doi.org/10.2225/vol14-issue3-fulltext-7)
was acquired as the complete ten-page primary PDF, cross-checked against SciELO
HTML and DOI metadata. Methods pp. 3–4, Tables 1/3 and Figures 1–4 were read;
the assay plots and tables were visually inspected. The record preserves
growing *A. niger*, reported ATCC 11414, and the mixed Kütahya-Emet
colemanite-bearing feed. Species-level NCBI 5061 was checked live; the ATCC
catalog request timed out, so strain authentication is not claimed.

The defensible observation is soluble-boron release during fungal culture,
with organic-acid production and acidification relative to the stated
no-organism control. It is not a demonstrated purified boric-acid product.
The source's protocol is internally inconsistent: Methods give 30 ± 2 °C
and initial pH 5.5, whereas the abstract/optimum text gives 25 ± 2 °C and
about pH 7. The 5% endpoint pH differs among Table 3, Results and the optimum
listing. Figure 4's fitted line has slope 0.111 but the text reports
`k = 0.030 day^-1`, matching the magnitude of the plotted intercept. Table 3
does not supply abiotic boron-release values. The record therefore omits
extraction percentages and kinetic constants and explicitly leaves the
microbial increment in dissolution unresolved. No separately linked supplement
was observed in the inspected PDF/HTML.

### Bauxite: mechanisms deferred after primary inspection

[Zhou et al. (2010)](https://doi.org/10.1007/s11707-010-0021-9) is a promising
contact-versus-dialysis study of *Paenibacillus polymyxa*. The publisher landing
page and Crossref metadata were acquired, but its purported PDF returned
HTTP 200 with a 21-byte permission-denial message. The alternate publisher
host returned 403. That payload is not treated as a paper; methods and
quantitative results remain unverified.

The complete open primary [Gurevich et al. (2015)](https://nopr.niscpr.res.in/handle/123456789/33526)
was read. The experimental section describes selected consortia and later
purified *Bacillus aryabhattai*, without clearly assigning that isolate to
every assay. Tables 1–2 use residual ore composition and assumed nonleached
reference constituents; the zeros are not direct null measurements. The
headline approximately 50% alumina result is not reproduced by the displayed
table. An unambiguous uninoculated comparator, microbial assay duration and
replication remain unresolved. These limits justify keeping bauxite
identity-only while preserving the research lead. No supplement was referenced
in the inspected five-page PDF.

### Alumina: mixed-catalyst evidence is not phase-resolved evidence

[Compagnone et al. (2023)](https://doi.org/10.1016/j.jenvman.2023.118825)
was acquired from the University of Cádiz repository as an eleven-page
version of record. Methods 2.1–2.6 and Results 3.4 were read, and Figure 4 was
visually checked. It compares total-Al release from milled spent automotive
catalyst using *A. thiooxidans* DSM 11478 and different biogenic/commercial
acid solutions. Cordierite and alumina are mixed in that feed; the measured
total Al does not establish phase-specific Al2O3 dissolution. Initial acidity
also differs among treatments. At higher loadings the bacteria-free treatment
performs best, so a universal cell benefit would misstate the experiment.
No mechanism is transferred to the alumina commodity record.

Appendix A links supplementary information, but publisher access returned
403. [Mendeley dataset version 1](https://data.mendeley.com/datasets/c96gpb6zpm/1),
published 23 January 2024, was verified at metadata level; the HTML file list
was still loading and a file-endpoint attempt returned 404. Its data and
the publisher supplement remain unverified. The deposit's later date is not
a new independent experiment. The primary PDF declares CC BY-NC 4.0 and the
dataset metadata CC BY 4.0; neither is committed as raw content.

No grade-achieving microbial result was accepted for HPA or high-purity iron
ore in the bounded queries. This is a coverage limit, not a claim that none
exists. Red-mud leaching already curated for aluminium and boric-acid culture
experiments already curated for boron do not identify these new commodities.

## Search, provenance and local checks

Ignored and hidden files were included with `rg -uu -L` in `data/records`,
`research`, `reviews` and `history` before additions. Exact root IDs and
selected study DOI/accession keys had no text matches in those roots at that
point. Broad queries found proposals, element records and prior authority
work. The bounded cited raw directories are enumerated in JSON; relevant
symlinks were followed, and `find` found none in those roots. Binary PDFs
were not assumed text-searchable. This is not a machine-wide novelty claim.

Live queries covered official definitions, dated lists, microbial activity,
access routes and selected DOI/title correction/retraction terms. Only first
returned sets and linked pages were examined. Crossref responses for the
three DOI-bearing experiments had no `update-to` and empty `relation` fields;
no correction/retraction notice appeared in those bounded searches. This is
not a complete Crossmark or retraction audit. Source-internal contradictions
were retained rather than replaced with cleaner estimates.

Raw artifacts are outside Git at
`/private/tmp/cmm-round12-aluminium-boron-raw`. The JSON records successful
and failed acquisitions, content types and SHA-256 hashes. Initial sandbox
DNS failures were followed by authorized public downloads; subsequent
permission responses, HTTP 403/404/429 and the Australian HTTP/2 failure are
explicit. The reused UK replacement PDF is marked reused, not freshly
downloaded. Primary material without established redistribution permission
remains uncommitted. The DOI, repository mirror and figures are one experiment,
not separate evidence counts.

Five CREATE histories were generated through `just new-history` with actual
codex / GPT-6 / codex metadata and issue 48, and their paths were attached:

- `history/records/bauxite/2026-10-11T083001Z-codex-40769d.yaml`
- `history/records/alumina/2026-10-11T083005Z-codex-1e7975.yaml`
- `history/records/high-purity-alumina/2026-10-11T083009Z-codex-d1801a.yaml`
- `history/records/high-purity-iron-ore/2026-10-11T083013Z-codex-00413d.yaml`
- `history/records/borates/2026-10-11T083018Z-codex-7e7166.yaml`

Each named record passed `uv run --locked cmmmech validate <record>` with
**1 checked, 0 failed**, using the parent-provided offline environment.
The parent reported the pre-edit baseline as 307 passed, 3 skipped, 71 valid
records and 83 valid histories. This agent did not rerun that baseline or
the batch gates. Independent review and final batch acceptance remain the
parent's next step; local validation alone is not scientific approval.

## Independent review correction, issue #49

At 2026-10-11T08:37:48Z, independent review `20261011T083609Z-borates-round12-independent`
F1 identified that Bayat2011 Table1 oxide cells total126.8wt%. The borates record
now attributes 28.05wt%B2O3 as reported, explicitly retains the nonclosing total,
and excludes normalization or use as a validated recovery denominator. The
qualitative mechanism is unchanged. Original record hash `8ada117c96a66f38b372418e3a0297f2e2a7ee720b5eb73180eb58babfc49c35` is retained
in JSON; corrected hash `697069a6fe66a825ec54081ead08f77109c57a6cdf3917a45b624b12abf6478c`. New actual EDIT sidecar:
`history/records/borates/2026-10-11T083733Z-codex-3ef868.yaml`.
Named record validation:1checked,0failed; named history validation against the
trusted base:2records,0errors. Final independent successor and batch gates
remain root-owned.
