# CMM source investigation: round107 borates

## Scope and provenance

UTC: 2026-10-16T00:39:10.728696Z. Researcher: codex (GPT-6; codex).
Worktree `/private/tmp/CMMMech-expansion-round107-20261016`, branch `curate/cmm-expansion-round107-20261016`, trusted base `27d842b3e6239bf60565f93c958d3f2cad395037`.
Two new owners: calcioveatchite mineral identity and mixed ludwigite-ore primary resource with a bounded abiotic laboratory separation. No other owner, schema, validator, Git or GitHub mutations.

Calcioveatchite was deferred as its own species owner in round106; this round rechecks its complete original and approved identity. Ludwigite ore fills a processing gap while keeping mixed geological feed separate from a mineral species. No criticality claim is inferred from boron or from the authors’ strategic-material language.

## Search and acquisition log

All searches below were performed on 2026-10-16 UTC. Each search used its first returned result set; exact queries, acquisition timestamps, response files, HTTP errors and checksums are retained in the paired JSON. The first web response was not retained; its exact queries and subsequently acquired primary leads are recorded explicitly.

- **web search**: First returned result set. Raw first response was not retained; selected primary leads were subsequently acquired. No exhaustive search claim.
  - `boracite mineral dissolution extraction thermal behavior original article PDF`
  - `ludwigite boron extraction roasting leaching Mg2FeBO5 primary open access`
  - `calcioveatchite mineral 2024 Minerals 14 901 crystallography`
- **web search**: First returned result set; metadata and primary acquisition leads, not proof of a microbial mechanism.
  - `"Water Leaching Kinetics of Boron from the Alkali-Activated Ludwigite Ore"`
  - `"ludwigite" bioleaching microbial`
  - `"10.3390/min14090901" correction erratum retraction`
- **web search**: First returned result set. No affecting notice identified. 2017 publisher preview and 2014 metadata are not complete originals.
  - `"10.3390/molecules29040826" correction retraction erratum`
  - `"10.3390/min14090901" correction erratum retraction`
  - `"Water leaching of boron from soda-ash-activated ludwigite ore" pdf`
  - `"An innovative process for extracting boron" ludwigite pdf 2014`
- **web search**: First returned result set. No accessible complete 2017 primary or affecting correction identified; bounded result only.
  - `"10.1016/j.hydromet.2016.11.004" filetype:pdf`
  - `"Water leaching of boron" "Liang" pdf 2017 -site:sciencedirect.com -site:mindat.org`
  - `"10.3390/molecules29040826" erratum correction retraction site:mdpi.com`
  - `"10.3390/min14090901" correction retraction site:mdpi.com`
- **web open/find**: PMC browser challenge; publisher calcioveatchite full text and official IMA homepage accessible. PDF and Europe PMC XML subsequently acquired through public URLs.
  - `https://pmc.ncbi.nlm.nih.gov/articles/PMC10893144/`
  - `https://www.mdpi.com/2075-163X/14/9/901`
  - `https://cnmnc.units.it/`
- **web open/find**: Molecules publisher HTML returned 429. No supplementary/CIF match in inspected calcioveatchite publisher text. Official raw homepage separately confirms September 2026 list. No claim of universal deposit absence.
  - `https://www.mdpi.com/1420-3049/29/4/826`

Initial sandbox requests failed DNS; the bounded public fetches were retried with approved network access. Publisher PDF and Europe PMC XML succeeded; calcioveatchite direct HTML returned 403 and Molecules web HTML 429, while calcioveatchite web text was available. These failures were retained rather than treated as missing science.

The official IMA homepage was freshly fetched and still linked September 2026. The exact list PDF and calcioveatchite PDF were reused from round106 with matching SHA-256, not presented as fresh PDF acquisitions. Both complete 18-page primary originals were read and every page visually inspected; IMA pages 1 and 35 were checked. No original CIF/reflection dataset was acquired.

## Deduplication and existing work

The recorded `rg --no-ignore --hidden --follow` search covered worktree records, research, reviews, history and skills; the original main including ignored reports; and cited raw roots from rounds10,12,76,101–106. Git internals, environments and caches and unextracted binary content were excluded. There were 59 context matches, no command errors, and no distinct pre-existing calcioveatchite or ludwigite-ore owner in those bounds. Existing veatchite and its modern-boundary notes remain separate.

The all-state issue inventory contains 299 titles/bodies; comments were not supplied. Only related issue #412 matched. It concerns the 2012 veatchite specimen/CIF and does not resolve the 2024 calcioveatchite measured-range discrepancy or the ore-study questions.

## Candidate inventory and source assessments

### ima_2026_09: pursue

Role: current mineral identity authority. 

September 2026 official 244-page list; reused exact round106 PDF, current homepage independently fetched

Calcioveatchite SrCaB11O16(OH)5(H2O), approved A, 2020-011. Authority corroborates species identity, not criticality or recovery. No IMA identifier applied to mixed ludwigite ore.

Inspected locators: PDF page 1 definitions; PDF page 35 Calcioveatchite row.

Retained file: `/private/tmp/cmm-round107-borates-research/reused-ima2026-09.pdf`; SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`.

### pekov2024: pursue narrowly

Role: primary natural-mineral characterization. DOI: `10.3390/min14090901`.

18-page publisher original, published 2 September 2024; CC BY 4.0; reused round106 acquisition and newly reviewed throughout

Nepskoe natural holotype 97013; four-spot EMPA and single-crystal diffraction. Eleven-coordinate site is Sr dominant and ten-coordinate site is Ca dominant. This supports a distinct ordered mineral species; it is not a pure ideal end member. The specific 2012 veatchite RG701/1 sample was not reanalyzed here.

Inspected locators: pp. 3-6 specimens and methods; p. 7 water determination; p. 8 Table 1 and Figure 6; pp. 10-13 Tables 3-7; pp. 14-16 species boundary and Figures 7-8; p. 17 data availability.

Limits:
- 10.22 wt% holotype water is calculated; 10.07 wt% is a separate gross multi-crystal Penfield mean of three analyses.
- Prose minimum SrO 17.1 wt% appears to use ideal calculated Table 1 column 2, not a measured endpoint. Table 1 measured columns and spot ranges are kept separate.
- Complete structure tables and images inspected; original CIF/reflections not acquired. Refinement not rerun.
- IR doublet interpretation is not used to infer extra formula waters or additional independent water sites.
- Rock dissolution is preparation; no microbial, extraction yield, criticality or deployment claim.

Retained file: `/private/tmp/cmm-round107-borates-research/reused-calcioveatchite2024.pdf`; SHA-256 `1623370d85fe10bd2fd7a719ca8c07fdf854e841696ed1b9a678aa449df702c1`.

### liang2024: pursue narrowly

Role: primary laboratory processing study. DOI: `10.3390/molecules29040826`.

18-page publisher original, published 12 February 2024; CC BY 4.0; Europe PMC XML version 1 is the same study

Mixed geological boron-iron concentrate, subsequently soda-ash-roasted at 1050 degrees C for 60 min with 20 wt% reagent per concentrate. Author-reported boron leaching 93.71% at 180 degrees C, 6 h, 8 mL/g, representative size 52.31 micrometres. Table 2 is reduced feed, not original ore. Leachate evaporite includes metaborate dihydrate and carbonate monohydrate; no pure isolated-product yield.

Inspected locators: pp. 3-5 sections 2.1.1-2.1.3/Figures 1-3; pp. 6-8 Figures 4-6; pp. 9-14 equations 4-11/Table 1; pp. 14-15 Table 2/Figure 9/methods; pp. 15-16 conclusions/data availability.

Limits:
- Exact mine/sample identifier and original phase proportions not established. Original ore is not a pure mineral and has no assigned external mineral ID.
- Specific analytical calculation and leach procedure explicitly referred to unacquired 2017 full original; gas/flow, denominator, sampling and replicates are not reconstructed.
- Low-temperature prose calls boron unextractable despite reported ~72% results and nonzero Figure 1 curves.
- All-under-74-micrometre method conflicts with a 92.94-micrometre representative size. Section 3.2.4 defines representative size as D50 although earlier text calls it average.
- Equation 11 and conclusion print positive outer exponent, unlike Equation 4. Not silently repaired or used predictively. Rate-constant/time units and global intercept derivation not independently reconstructed.
- 8.812 kJ/mol is fitted apparent activation energy; diffusion control is an inference, not unique elementary-mechanism proof.
- Figure 4 uses 60.16 micrometres rather than best-result 52.31; Figure 5 uses a 60-min residue and unequal magnifications. No pooling these arms.
- No demonstrated microbial activity, industrial operation, complete mass balance or mineral-specific extraction.

Retained file: `/private/tmp/cmm-round107-borates-research/ludwigite2024.pdf`; SHA-256 `35e5f52adead0ffbfb519c99e51c82ef9fb5285398fc9abb11036324f36ec101`.

### liang2017: defer

Role: cited prior analytical/roasting methods. DOI: `10.1016/j.hydromet.2016.11.004`.

Publisher abstract and partial Materials preview only; bounded exact-title/DOI PDF searches did not recover full original.



Limits:
- Preview concerns 25 wt% Na2CO3 and 100% CO optimum; cannot supply missing conditions for 2024 20 wt% batch. No recipe or quantitative outcome imported.

### li2014: defer

Role: cited earlier ore characterization. DOI: `10.1016/j.mineng.2013.10.030`.

Metadata/reference and search lead only; complete primary not acquired.



Limits:
- No sample composition, recovery yield or process condition imported.

### later_scaleup: defer

Role: later processing lead. DOI: `10.1016/j.jece.2025.119518`.

Search metadata/abstract lead only; not acquired or reviewed in full.



Limits:
- No scale-up or industrial deployment claims transferred to the 2024 laboratory record.

## Correction checks, reuse and representation

Exact DOI/title correction, retraction and erratum searches, including publisher-restricted queries; both Crossref relation/update fields and Europe PMC XML inspected. No affecting notice identified in these bounded results. Not exhaustive.
Both DOI metadata have empty relation and absent update-to/updated-by fields; publication dates verified against original pages.

Full PDFs/XML, extracted text and page images retained outside Git. Only original assessments and provenance enter repository.
Both 2024 papers are CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Official IMA list used for bounded identity verification; no bulk redistribution.
No automated importer, dataset join or digitized measurement table. All percentages, wt% values and fitted kinetic values stay qualified prose; native concentration-observation contract is not stretched.

The two 2024 originals each state that data are available on request. Metadata, publisher text and Europe PMC XML supplement searches did not provide independent underlying measurements. The XML and publisher PDF are representations of one study, not replicate experiments.

## Curation and checks

Baseline `just check` completed with exit 0 at 2026-10-16T00:35:16.079460+00:00. Its retained log hash was independently verified before this dossier was saved.
Named validation: `uv run --locked cmmmech validate data/records/calcioveatchite.yaml data/records/ludwigite-ore.yaml`, exit 0. Checked 2 record(s); 0 failed.

Exact owner and canonical CREATE history hashes are retained in the paired JSON. No schema/validator changes were needed. Final batch/history/native-review gates and independent scientific reviews remain pending at this timestamp.

## Priorities and unresolved questions

- Independent review of both exact owners and histories.
- Resolve calcioveatchite measured SrO endpoint and acquire original refinement data; distinct from issue 412.
- Recover specimen-linked 2017 methods and resolve 2024 analytical/model/grain-size conflicts before strengthening the ore record.
- Assess later scale-up primary originals separately before any deployment claim.

Concrete source-follow-up drafts: `/private/tmp/cmm-round107-borates-research/source-followups.md`. These source uncertainties do not constitute a fabricated corrective defect in the newly bounded owner claims.

Paired machine-readable dossier: [20261016T003910Z-source-investigation.json](20261016T003910Z-source-investigation.json).
