# Round44 lithium mixed-feed extension

UTC: 2026-10-12T03:23:18.313980+00:00

Base: `3fc8b873487ed2c1c253ecf131d99e09b8b8d452`. Author: codex / GPT-6 / codex.

## Decision and ownership

Extend [lithium-mica ore](../../../data/records/lithium-mica-ore.yaml) with a separate Li et al.2025 laboratory assay. This supplier-provided heterogeneous feed fits the existing primary-resource category. It does not identify a pure polylithionite/trilithionite mineral or transfer the 2020 Beauvoir result. The existing three mechanisms, sources and old history remain unchanged; only the description was expanded, and one source/mechanism/EDIT event/reference appended. No criticality or industrial claim is added.

## Complete primary acquisition

[Li et al.2025](https://doi.org/10.3390/microorganisms13020415), Microorganisms13(2):415, is now available as the complete23-page publisher PDF and original4-page supplement through [official PMC Cloud metadata](https://pmc-oa-opendata.s3.amazonaws.com/PMC11858582.1/PMC11858582.1.json). The [official bucket README](https://pmc-oa-opendata.s3.amazonaws.com/README.txt) documents the versioned object structure. All four metadata checksums for XML/PDF/TXT/supplement matched their deposited MD5 values; SHA-256 receipts are in the paired JSON. This closes the prior43 source-access gap for this study.

Raw evidence: `/private/tmp/cmm-round44-lithium-mixed-feeds-research/raw`. Complete main: `cloud-PMC11858582.1.pdf`; SI: `supplement/microorganisms-3462615-supplementary.pdf`; all12original figure JPEGs and page renders retained. Acquisition1-4 receipts preserve exact URLs/status/times/hashes. Direct PMC PDF/SI endpoints returned HTML preparation pages and are explicitly non-evidence; no challenge was executed. The obsolete oa.fcgi route returned404, followed by official retirement documentation and the changed Cloud route. Previously denied MDPI endpoints were not repeatedly retried.

## Inspection and maintained claim boundary

Read the complete primary text. Visually inspected all12original main figures, main page rasters3-7,10-13,19,21 for methods and conflicts, and all4SI page rasters with six figures and three tables. Other main figure content was examined using the original JPEGs; this is not a claim of viewing every23page raster.

The retained result is culture-associated solution lithium mobilization after mechanical activation. It is supported by the direct ICP-OES timecourses and qualified experimental context. The percentages combining post-HCl extracts are not adopted as verified biological recovery yields.

- Feed is a supplier-provided mixed ore, not an authenticated lepidolite species. Figure1 adds celadonite labels to the prose list of mica/albite/quartz. No quantitative phase proportions or mine provenance.
- Methods2.2.3 says sterile controls without pyrite; Figure2 explicitly draws FeS2 in sterile arm and Figures9/S5 label pyrite peaks. Control composition unresolved, so matched-pyrite attribution is not claimed.
- Figure6d contains direct solution total elemental Li by ICP-OES. Same initial pH is not matched acidity through incubation; Figure6a pyrite cultures acidify much further. No independent metabolite/killed-cell control.
- Equation1 sums direct solution Li and a culture-minus-sterile post-HCl increment; FigureS1 shows residue extraction1MHCl24h. HCl coextracts feed and associated phases; not specific EPS or secondary-mineral adsorption.
- Equation1 CF is printed mg/L feed concentration from XRF, multiplied by MF grams; denominator is dimensionally inconsistent. Section2.1.2 instead reports ICP-MS3.20%Li/5.05%Al/0.04%Fe; TableS1 has noLi/Fe and26.35%Al2O3. No silent correction or independently reproduced yield.
- Figure11/3.6: sterile11.3%, oligotrophic20.8%, eutrophic24.9%; Conclusions11.3%,16.75%,19.24%. Figure7 sterile and oligo bars near69/86mg/L differ from adjacent62.33/79.40mg/L prose; approximate graph readings are diagnostic, not imported concentrations.
- TableS3 operational thermal-extract Li units are micrograms/L (1.13,3.83); no equivalent purified-EPS binding balance. Thermal80C30min and cell-disruption description limit fraction specificity.
- Figure12 is proposed mechanism, not proof of uptake, Li substitution in jarosite, EPS-specific release or individual species causality. 16S labels do not authenticate isolates; sequence accession unavailable in inspected source/SI.
- 2025 comparison with Sedlakova2020 uses41d whereas previous bacterial result is336d Results/366d Methods. No pooled threefold advantage is accepted.
- Supplement citations in body are shifted: SEM120min isS3 notS2; EDS isS4 notS3; residueXRD isS5 notS4; aluminum percentage isS6 notS5. Correct original locators retained.
- No isolated product, pilot-scale recovery, process economics or industrial deployment is demonstrated. Source economic/environmental assertions excluded.

## Deduplication, notices and boundaries

Hidden/ignored-inclusive, symlink-following searches covered current and original-main records/research/reviews/history plus15existing referenced raw roots, with exact-owner and DOI/experiment terms. Three commands exited0, with no read errors. Existing lithium-mica-ore, petalite and polylithionite owners were identified; the2025 study was already a deferred handoff. The raw receipt records unavailable and malformed references rather than claiming universal absence. Binary files without retained text were outside the text-search boundary.

Two fresh exact-source correction/retraction queries returned the primary and indexing pages, with no affecting notice in those result sets; fresh official PMC metadata identifies version1 and is_retracted:false. This bounded observation does not prove absence of every notice. A related Bioresource Technology source is a future lead only.

## Frozen files and checks

- Record SHA-256: `30166629bd2c161767efb3824c5c5c582ca2ab100ecf98f509d49eeb143734db`.
- EDIT: `history/records/lithium-mica-ore/2026-10-12T032137Z-codex-47f29b.yaml`, SHA-256 `f07d567afd2b4fd2bad6099ae85463bfb25875d3980e9411767458796d0eef85`.
- Named validation: exit0, one record checked, zero failed.
- Preservation proof: `/private/tmp/cmm-round44-lithium-mixed-feeds-research/preservation-and-freeze.json`.
- Full cohort gates and independent scientific review are handled separately; this dossier is not a self-review approval.

The paired JSON pins 69 retained artifacts, acquisition evidence, search scope and preserved limitations.
