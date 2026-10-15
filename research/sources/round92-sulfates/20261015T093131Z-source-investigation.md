# Round 92 source investigation: plumbojarosite

UTC 2026-10-15T09:31:31.130579+00:00; codex /root; base `b5deea86aa8b3872df521b9483541cf1205403ed` in the isolated round92 worktree. This is a source handoff, not a scientific acceptance review.

## Scope and identity

Plumbojarosite is a separate lead ferric sulfate species, not lead metal, generic jarosite or a residue. The September 2026 IMA page 174 and complete Handbook entry agree on Pb0.5Fe3(SO4)2(OH)6. NCBI 319224 resolves CN-32; no constituent criticality is inherited. Hidden/ignored-inclusive followed-link searches across maintained records/research/reviews/history found only round91 deferred mentions; the current 215-entry all-state issue inventory had no exact name/DOI match. Referenced round91 sulfate downloads and the new round92 root download directory were included; unrelated machine directories were not searched.

## Primary evidence and versions

[Smeaton 2009](https://doi.org/10.1021/es901629c) was inspected through its author's [2012 dissertation Chapter 2](https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF), printed pages 25-60/PDF pages 50-85, and the [original ACS supplement](https://doi.org/10.1021/es901629c.s001). All 3 main figures, all 5 supporting tables and 6 supporting figures were visually assessed. The final journal PDF returned HTTP 403, so byte-equivalence to the final article is not asserted. The thesis frontmatter gives incorrect journal pagination; authority metadata supplies 8086-8091. The SI deposited 16-page PDF retains revision markup, a drafting note and a duplicate deleted-table page. Its cover's 15-page count is inaccurate. These artifacts represent one experiment, not independent replication. The old local thesis filename `jones-thesis.pdf` is misleading; author/title were checked as Smeaton.

## Supported claim and limits

Triplicate synthetic mineral tubes plus sterile and mineral-free controls support CN32-associated filtered Fe(II) accumulation under anaerobic, initially pH 7.3 conditions. The strain was washed after aerobic growth; 32°C is its growth temperature, not a verified dissolution-incubation temperature. SI S1-S3 establishes preparation and assay fractions. The early lead pulse and later below-detection values do not establish an isolated product yield.

Main Figure 2.1, Table S3 and prose disagree in times and final Fe(III); sulfur cannot track dissolution because PIPES dominates its assay. Secondary phases in Tables S2/S4 are geochemical predictions, not identified products. Figures S2/S3 include precipitates in sterile controls. Figure S5 is an ATP proxy and does not match several prose assignments.

TEM Figures 2.3/S6 demonstrate electron-dense granules in processed cell sections, but SI S5 uses 0.1 M phosphate buffer during fixation. Therefore the P signal does not independently prove metabolic phosphate origin; a phosphate-free fixation control is missing. SEM before TEM processing supports cell-associated particles but cannot resolve intracellular chemistry. Local EDS spot totals in Table S5 are not normalized bulk product stoichiometry. Proposed ATPase roles lack expression/perturbation tests. The record preserves these limits.

## Search and acquisition

The paired JSON records exact queries, first-result-set coverage, URLs, actual dates, hashes and prior-versus-new acquisitions. Bounded exact DOI/title correction/retraction searches and Crossref relation fields did not reveal an authoritative correction; this is not an exhaustive absence claim. Current abstract-only Pb-As jarosite/Desulfovibrio work (10.1016/j.envpol.2024.125516) concerns a different system. Mixed natural jarosite and abiotic soil studies remain separate leads, not transferred measurements or direct refutations.

## Priorities and handoff

1. Curate the qualified controlled synthetic-feed reduction record and obtain independent review of its final bytes.
2. Seek a clean final experimental source/data clarification for time/value assignments, assay temperature, microscopy fixation effects and a solid/liquid lead balance before strengthening mechanistic or recovery claims.
3. Assess other dissertation chapters and the newly located original studies independently; this bounded search has not exhausted the material frontier.

Raw originals remain outside Git. Dissertation and Handbook redistribution is not assumed; official SI metadata states CC BY-NC 4.0. Only original synthesis/provenance is committed.
