# Chromium curation dossier

Investigation date: 2026-10-11 UTC; dossier timestamp 2026-10-11T04:36:03Z.
Author: Codex (GPT-6; Codex),
subagent `cmm3_chromium`. Worktree: `/private/tmp/CMMMech-expansion-round3-20261011`;
branch `curate/cmm-expansion-round3-20261011`; trusted base
`5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da`.
This is a source assessment and curation handoff, not the independent record review.

## Scope and selection

The previous authority inventory proposed chromium without an accepted element
record. Hidden and ignored files were included in searches of `data`, `research`,
`reviews` and `history` for `chromium`, `chromate`, `28073`, `02463-10` and
`MtrC.*OmcA`. Matches were authority proposals and a nickel inhibition lead;
no chromium root or this experiment was represented within those searched paths
before curation. Relevant existing reports did not identify a chromium-specific
local download. The task download directory is
`/private/tmp/cmm-round3-chromium-evidence-20261011`; this is not a machine-wide
absence claim. No relevant symlink was encountered in those inspected paths.

Selected [Belchik et al. 2011](https://journals.asm.org/doi/full/10.1128/aem.02463-10)
because it combines resting-cell deletion comparisons, a heat-killed control,
microscopy and a separate purified-protein activity experiment. These provide
stronger evidence for a bounded microbial redox contribution than color change,
resistance or expression data alone. The supported endpoint is laboratory Cr(VI)
transformation, not demonstrated chromium-product recovery.

The parent reported the unchanged-base baseline passed: 307 tests passed,
3 skipped, 17 records and 26 histories valid. Curation began after that signal.

## Authority and identity checks

| Source opened on 2026-10-11 | Exact scope and curation decision |
|---|---|
| [ChEBI:28073](https://www.ebi.ac.uk/chebi/CHEBI:28073) | Chromium atom, Cr, atomic number 24, charge 0; identifiers 3678 and 23235 are secondary. Use the primary ID for the element, not chromate or chromite. |
| [NCBI Taxonomy 211586](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586&mode=Info) | Current name *Shewanella oneidensis* MR-1; rank no rank; equivalent `str. MR-1`. Names ATCC 700550 and *Shewanella* sp. MR-1 appear as synonyms. This identifies the parental strain, not separately accessioned engineered mutants. |
| [USGS final 2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm) | Final, November 7, 2025, 90 FR 50494-50497, FR Doc 2025-19813; chromium is in the commodity table on p.50496. Record US jurisdiction and this edition only. No timeless or host-mineral designation. |
| [PubMed 21498755](https://pubmed.ncbi.nlm.nih.gov/21498755/) and ASM article | DOI 10.1128/AEM.02463-10, AEM 77(12):4035-4041, 2011, Belchik and colleagues; PMCID PMC3131624. PubMed lists April 15 e-publication, publisher displays June 7 online date; record uses journal year/volume/pages without conflating these dates. |

## Primary experiment inspected

Read the publisher full text, all Methods and Results, Discussion, Table 1 and
all five figure captions. Downloaded all five publisher JPEG figures and
visually inspected them. Source-local locators are stable section/figure names;
no curve was digitized and no new measurements were computed.

- **Cell assay:** Methods “Bacterial strains and growth conditions” and “Cr(VI)
  reduction” specify aerobic preculture in dextrose-free TSB, 16 h, 30 degrees C,
  100 rpm; one wash in bicarbonate buffer; sealed resting-cell assays, nominal
  pH 8, 30 mM bicarbonate, 0.2 mM potassium chromate, 10 mM lactate,
  2 x 10^8 cells/mL, 30 degrees C and 25 rpm. The source states CO2:N2 80:20;
  that unusual ratio is retained as reported, with post-purge pH unresolved.
  Do not silently reverse the ratio or equate the initial buffer pH with a
  measured final assay pH. Heat-killing protocol details are not supplied.
- **Outcome/control:** Figure 1 shows aqueous Cr(VI) remaining over 24 h,
  triplicate measurements with means and SD, all mutants retaining activity,
  and an approximately stable heat-killed control. The main Results give
  4 h rates and explicitly state that little subsequent reduction occurred
  from 24 to 120 h; those later kinetics are not shown. The record retains
  the reported double-mutant relative rate and incomplete reduction, without
  inventing a quantitative yield from the plot or calling triplicates
  independent biological replicates.
- **Spatial evidence:** Figures 2 and 3 show extracellular/cell-associated
  material and EDX detection of Cr in selected particles. Figure 3B is a
  useful negative compositional observation: not all dark intracellular
  inclusions contain detectable Cr. Most critically, Results “Cellular
  locations of reduced Cr(III) precipitates” expressly **assume** Cr(III)
  from earlier studies. This paper did not perform XANES/XPS/EELS valence
  confirmation; EDX is not such confirmation. No specific crystalline phase
  is curated.
- **Figure-label conflict:** Figure 2C image says delta-mtrC, while its caption
  identifies a mutant without OmcA. Preserve this conflict and avoid using
  that panel as unambiguous single-mutant evidence. The wild-type and double
  mutant comparisons and independent kinetics remain interpretable.
- **Purified-protein support:** Methods “Protein film voltammetry” and Figures
  4-5 show recombinant MtrC/OmcA films, a bare-electrode response, chromate
  dependent catalytic currents and saturation fits. PBS pH 7.4, 273 K,
  30 mV/s, 3000 rpm and -0.33 V versus SHE belong to this assay, not the cell
  assay. Table 1 and main Results give apparent MtrC turnover 1.2 +/- 0.1/s;
  the abstract says +/- 0.2/s. No exact fitted turnover constant is curated,
  and neither value is silently promoted to whole-cell kinetics.
- **Causal limits:** Combined deletion and purified-protein evidence supports
  contributions from both proteins. It does not establish exclusive necessity,
  complete conversion, an isolated-product yield or field performance. No
  complemented-mutant rescue is reported in the inspected main article.

The publisher full-text route had no supplementary-material link or matching
“Supplement” text in this inspection. The inspected Methods support the stated
assay without claiming a separate supplement was acquired. Imported construction
and protein-purification protocols cited in earlier papers were not independently
reconstructed; no new claim about exact deletion boundaries, purity percentage
or gene complementation is made.

## Search log and counterevidence boundary

Provider: live web search, 2026-10-11 UTC. No recency filters; first returned
result set for each query, no pagination. Domain restrictions below are literal
query terms. Exact queries:

1. `Shewanella oneidensis MR-1 chromium reduction OmcA MtrC purified XANES primary 2007 2008`
2. `site.ebi.ac.uk/chebi chromium atom CHEBI`
3. `site.federalregister.gov 2025 final critical minerals list chromium`
4. `site.pmc.ncbi.nlm.nih.gov chromium MtrC OmcA "Cr(VI)" purified`
5. `site.ebi.ac.uk/chebi "chromium atom"`
6. `"Extracellular Reduction of Hexavalent Chromium" Belchik 2011 DOI`
7. `"Extracellular Reduction of Hexavalent Chromium" correction retraction supplement`
8. `"Effects of Incubation Conditions on Cr(VI) Reduction" cytochromes Frontiers`
9. `"10.1128/AEM.02463-10" correction erratum retraction`
10. `Shewanella oneidensis MR-1 Cr(VI) OmcA MtrC no effect alternative reductase conflicting conditions`

No correction/retraction affecting the selected article was identified in those
returned results or the opened publisher page; this is a bounded result, not an
exhaustive guarantee. A different chromium review, *Successive use of
microorganisms to remove chromium from wastewater*, DOI
10.1007/s00253-020-10533-y, was returned with a retraction notice and is **not**
used as evidence. Other returned sources are leads, not accepted measurements:

| Lead and inspected scope | Next step / disposition |
|---|---|
| [Han et al. 2016, DOI 10.3389/fmicb.2016.00746](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00746/full) | Main text opened through Methods; author statement that spectral kinetics were unreplicated and error bars are fit-derived is an important caution. Search results describe oxygen inhibition. Inspect complete results, figures and supplement before adding its condition-dependent evidence. Do not import its unusual reported cell-density scale without investigating it. |
| [Single-cell imaging study, PMC3671764](https://pmc.ncbi.nlm.nih.gov/articles/PMC3671764/) | Indexed primary lead for Raman/phase evidence, but direct open returned a challenge. Not used to upgrade 2011 valence/phase claims. |
| [Cr isotope study, DOI 10.1021/acs.estlett.7b00471](https://pubs.acs.org/doi/abs/10.1021/acs.estlett.7b00471) | Search-result lead with a double mutant; full methods not inspected. Distinguish isotope fractionation from reduction-pathway exclusivity. |
| [Biohybrid study, DOI 10.1016/j.watres.2025.124606](https://www.sciencedirect.com/science/article/pii/S004313542501509X) | Abstract-level lead proposes cell-surface encasement limiting Cr(VI) reduction. No performance values accepted here. |

One attempted PLOS article locator, DOI 10.1371/journal.pone.0062098, resolved
to an unrelated moth receptor paper and was rejected. It is not the chromium
study and contributes no record claim.

## Acquisition provenance and terms

Raw artifacts remain outside Git at
`/private/tmp/cmm-round3-chromium-evidence-20261011/`. The accompanying
`round3-chromium-20261011.json` contains exact URLs, acquisition times, byte
counts, checksums and failure states copied from that directory's receipt.
ASM copyright notice is © 2011 American Society for Microbiology with a
permissions request route; an open redistribution license was not established.
Only original factual curation and provenance are committed, not primary prose
or figures. Reading access does not imply redistribution rights.

The Europe PMC fullTextXML route returned HTTP 500. Direct publisher CLI access
returned HTTP 403 while the web tool exposed the complete primary text. PMC
returned intermittent challenge pages; a retained HTTP 200 HTML response was
verified to be a recaptcha challenge, **not article XML**. Publisher figure URLs
returned actual JPEG content and were inspected visually. This distinction is
recorded in the acquisition JSON. Authority pages and publisher full text were
read live through the web tool rather than represented as locally downloaded
source files.

## Curation and remaining work

Created `data/records/chromium.yaml`, canonical CREATE session
`history/records/chromium/2026-10-11T043602Z-codex-adf9c7.yaml` and a distinct
inline event at 2026-10-11T04:36:03Z. No schema or validator change is needed: numerical conditions
and relative rates remain qualified prose; they do not satisfy the native exact
mg/kg source-cell observation contract. Parent coordinates independent review,
full batch checks and publication. Additional evidence on product valence,
conditional oxygen effects, reactor-scale transformation and actual chromium
separation remains a useful extension; these leads do not imply search saturation.
