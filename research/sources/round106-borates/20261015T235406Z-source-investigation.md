# CMM source investigation: round106 pinnoite and veatchite

## Scope and provenance

- UTC: 2026-10-15T23:54:06Z; curator codex (GPT-6; codex). This is a source assessment and curation handoff, not an independent scientific review.
- Worktree: `/private/tmp/CMMMech-expansion-round106-20261015`; branch `curate/cmm-expansion-round106-20261015`; retained base `af6cbead934deb4667764fa4a325246158ee4a0a`.
- Scope: two new mineral identity and characterization records. No microbial or processing mechanism, criticality designation, quantitative assay cells, schema change or validator change.
- Elements, mineral species, polytypes and commodities remain distinct. Grandfathered years 1884 and 1938 are not IMA approval identifiers. Calcioveatchite is a separate species and future candidate.

## Search and acquisition log

The paired JSON records search groups, fifteen URL acquisition attempts, dates, versions, paths, hashes and access failures. Raw evidence remains in `/private/tmp/cmm-round106-borates-research`. Searches covered identities, processing and microbial leads, original PDFs and CIFs, and corrections/retractions.

Deduplication included hidden and ignored files and followed relevant symlinks across the worktree records, research, reviews, history and skills; original main; and eight cited prior raw roots. Git metadata, environments/caches and unextracted binary content were outside the declared scope. Nine raw context/reference/authority paths matched the corrected name/DOI search; no pre-existing maintained owner was found. An initial DOI regex escaping error was corrected and retained in the audit. The later literal formula search found the two newly added owners and raw context; these expected self-matches do not imply prior duplicates. No machine-wide absence claim is made.

Issue dedup checked 293 all-state titles/bodies in `/private/tmp/cmm-round106-issues-start.json`, SHA256 `2bb14b523069a58f790586c937a8c5e9dc99d1991a5143b2288e38f0e4a19956`. No matching name/DOI issue was found. Comments were not supplied or searched.

## Candidate inventory

| Source | Evidence inspected | Decision |
|---|---|---|
| [Frost and Xi 2014](https://doi.org/10.1016/j.saa.2013.08.047) | Complete 18-page QUT author manuscript; specimen, methods, results, Table 1 and Figures 1–5. | Pinnoite identity and bounded spectral observations. |
| [Grice and Pring 2012](https://doi.org/10.2138/am.2012.3889) | Complete seven-page publisher original; all pages visually checked, including Tables 1–3 and Figures 1–4. | Veatchite species/polytypes with specimen and chemistry limits. |
| [Pekov et al. 2024](https://doi.org/10.3390/min14090901) | Complete 18-page publisher original; main text/tables read and relevant chemical/structural figures checked visually. | Modern species boundary; no third owner. |
| September 2026 IMA-CNMNC list | Fresh official PDF and homepage edition link; pages 1, 35, 173 and 228 visually checked. | Identity authority, not a criticality list. |
| Clark and Christ 1971 | Complete 21-page original downloaded/extracted; not fully reviewed this round. | Historical lead, not cited in owners. |
| [Zheng et al. 2020](https://doi.org/10.1155/2020/6181356) | Crossref metadata and indexed publisher-supplied text; original PDF access blocked. | Defer calorimetry/synthesis claims. |
| [Lin et al. 2016](https://doi.org/10.1080/01411594.2015.1077524), [Peng et al. 2017](https://doi.org/10.1080/01411594.2017.1288230) | Indexed or primary-reference leads; complete originals unavailable. | Defer processing claims. |

## Source assessments

Pinnoite is the IMA-listed MgB2O(OH)6 species. The QUT cover warns that its author manuscript may differ from the version of record; the 2013 online/DOI date is distinct from the 2014 journal year. Manuscript page 3 identifies natural Inder material and specifies 633-nm Raman excitation, nominal 2 cm-1 resolution and at least ten crystals; ATR-IR uses 128 scans at 4 cm-1 resolution. Figures 2a, 3a and 4a support the retained spectral features. No new bulk chemical-purity assay or diffraction refinement is reported.

Manuscript page 5 says the OH region provides no water-band evidence; page 7 and Figure 5 assign bending bands to water and consider surface adsorption. The 745 cm-1 assignment and 3543/3513 cm-1 infrared values differ across passages. Empirically calculated bond distances and inconsistent strength/cutoff wording are not promoted to direct atomic measurements. Nanomaterial proposals are not performance tests. The publisher version and separately mentioned supplementary infrared material remain unavailable. Direct observations are retained while stronger water, coordination and processing claims are withheld.

Veatchite is one mineral species with three named polytypes. Grice and Pring's Table 1 distinguishes Emet NMNH 145911 (1A), Reyershausen NMNH 113264 (1M) and Sussex RG701/1 (2M). The last substitutes for a preserved California type crystal. Diffraction supports P-1, P21 and Cc, respectively; the 1A crystal required twin treatment. Hydrogen sites were located by difference Fourier maps and refined. No new chemical analyses were made on the two type specimens.

Table 2c and page 491 report slight Ca dominance at the smaller 2M cation site and already raise possible new-species status. Pekov et al. establish distinct calcioveatchite and clarify the site-occupancy boundary, without directly reanalysing RG701/1. Their Penobsquis zone inference does not substitute for reassessment of that exact crystal. No pure-Sr metrics or definitive modern reassignment of that crystal are claimed. Abstract/Table 1 discrepancies in the 1M c parameter and 1A beta uncertainty remain unselected numerical values. Original AM-12-015 CIFs were not acquired. Geological pressure/temperature associations on page 494 have no measured transition parameters and do not produce a mechanism field.

The 2024 Table 1 contains both empirical analyses and calculated ideal compositions. Its water results distinguish a gross-sample Penfield measurement from calculated water for individual grains. Dissolving host salts to collect insoluble residue is specimen preparation, not a quantified recovery trial. No qualifying microbial experiment was identified in the bounded searches; this does not establish that none exists.

## Corrections, reuse and limits

Exact DOI/title notice searches and inspected Crossref relations did not identify an affecting correction or retraction in returned results. Coverage is bounded and current publisher access was incomplete. Conflicting evidence is preserved explicitly.

Raw PDFs, text and renders remain external. The QUT cover gives CC BY-NC-ND 2.5; the 2024 original is CC BY 4.0; redistribution terms for the 2012/1971 originals were not established. Committed artifacts contain authored assessments and provenance. No importer, pooled dataset or digitized raw spectrum was created.

## Priorities and handoff

1. Independently review both owners and linked canonical CREATE histories against the exact hashes in `owner-freeze.json`.
2. Resolve pinnoite water/band interpretations using the final article and original spectra. Acquire complete processing/calorimetry originals before adding measurements or mechanisms. The indexed 2020 purity text/table discrepancy remains an unverified original-source lead.
3. Recover the 2012 CIF deposit and obtain specimen-linked modern Sr/Ca reassessment. Preserve historical study names separately from modern classification.
4. Consider calcioveatchite as a separately curated future owner. DOI 10.1016/j.apgeochem.2026.106732 is an unassessed isotope-study lead, not evidence admitted this round.

Concrete source follow-up drafts are `source-issue-pinnoite.md` and `source-issue-veatchite.md` in the external raw root. These concern qualified source limits, not fabricated maintained-record defects.

## Checks actually completed

The root baseline `just check` passed before writes: 317 tests passed, three skipped, 520 records and 592 histories. Named validation then passed both records with zero failures (tool session 20930; receipt and byte hashes in the paired JSON). Independent scientific reviews and final corpus/history/review gates remain pending at this dossier timestamp.
