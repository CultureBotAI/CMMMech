# Round 15 lithium-bearing geothermal-brine source assessment

Researcher: codex (GPT-6; codex). Saved 2026-10-11T09:59:33Z.
Worktree `/private/tmp/CMMMech-expansion-round15-20261011`; branch `curate/cmm-expansion-round15-20261011`;
trusted base `a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0`; acceptance
[issue 59](https://github.com/CultureBotAI/CMMMech/issues/59).
Exact acquisition timestamps, hashes, URLs and search queries are in the
[paired JSON dossier](round15-brine-sources-20261011.json).

## Identity, coverage and selection

The [new resource record](../../data/records/lithium-bearing-geothermal-brine.yaml)
is a natural geological extraction feed: lithium-bearing geothermal saline water.
[Rehmanji et al. 2025](https://doi.org/10.1039/d5ra06824j), Section 4.2, directly
identifies the experimental feed as natural geothermal brine from an unnamed
Cornish geothermal project. It is not sold lithium carbonate or spent process
waste. This concrete candidate demonstrates the missing `primary_resource`
kind; root is adding that narrow schema/documentation change with regression
coverage, rather than disguising the natural feed as `secondary_resource` or
`commodity`. No criticality, finished-product grade, universal composition,
material CURIE or industrial deployment is inferred.

This resolves the prior round14 product-boundaries handoff. The existing
lithium element and lithium-carbonate commodity records were read, including
their evidence boundaries. This study is a new curated experiment relative to
those records; its institutional PDF, PMC XML and supplement are one study,
not independent replications. The broader identity is not evidence that all
geothermal brines respond alike.

The local novelty search included hidden and ignored files and relevant links:
`rg --no-ignore --hidden --follow` with `brine|d5ra06824j|pasteurii` across
`data`, `research`, `reviews`, `history`, and the prior cited
`/private/tmp/cmm-round14-product-raw` and `cmm-round14-product-review` directories.
The first search preceded this record; the retained repeated search includes
this new work. No machine-wide absence or global source exhaustion is claimed.
The inspected earlier hits were research leads and boundary statements rather
than an existing geothermal-brine root.

## Search, acquisition and reuse

Six exact searches in JSON covered DOI/title, controls, supplements, inhibition
and correction/erratum/retraction terms on 2026-10-11. Each inspected the returned
first result set only, with no date/domain filters. No affecting correction
notice or directly conflicting independent brine experiment was returned in
this bounded search; that is not exhaustive scientific clearance.

Publisher HTML/landing returned403 to the reader and PMC returned a browser
challenge. Initial sandbox downloads failed DNS. Authorized public requests
acquired the full 12-page Oxford institutional published PDF and EuropePMC XML.
The guessed RSC supplement route returned404. Europe's PMC `supplementaryFiles`
endpoint returned a valid ZIP, from which the 27-page SI PDF was extracted. The
alternative PMC direct supplement route returned HTTP 200 but contained an HTML
challenge and was rejected as scientific evidence. Neither access controls nor
paywalls were bypassed. The raw DOI paper, supplement and taxonomy artifacts
remain outside Git at `/private/tmp/cmm-round15-brine-raw`. The publication reports 6 November 2025; source
posting/crawl dates were not treated as new editions.

The primary paper states Creative Commons Attribution 3.0 Unported licensing.
The supplement carries RSC 2025 copyright; this report does not assume separate
redistribution rights beyond the documented article license. DSMZ/NCBI pages
were used for identifier resolution; catalogue bulk reuse rights were not
assessed. No full article, figure, bulk export or contact details are committed.
The paper's data statement says manuscript plus SI and no additional deposited
dataset; graphs are not treated as downloadable raw replicate measurements.

## Primary evidence and limitations

Sections 4.1-4.2 specify mid-log DSM 33 biomass grown in TSB plus 500 mM urea,
28 degrees C and 180 rpm; harvested at 3200 g for 15 min, PBS-washed, and added to
unsterilized natural brine under reported non-growth conditions. Triplicate
100 mL cultures in 250 mL flasks, OD600 0.05-0.4,500 mM urea,28 degrees C static 24 h
were used. The reported B. subtilis ATCC-2385 control is retained as an unverified
source strain designation, not silently corrected. DSMZ confirms DSM 33 as
S. pasteurii, and NCBI species 1474 resolves that name; species identity does not
independently authenticate the culture used.

Figure 1 and Section 2.1 support differential cation depletion while lithium
remains largely in the measured solution. Figure S5 contains the separate
brine-plus-urea/no-added-cell comparison. Table S1 reports lithium 75.2 ± 1.8 mg/L
(mean ± SEM, n = 3), with high calcium and a variable ion mixture; that value is
experimental context, not a universal brine definition or an `mg/kg` observation.
No density conversion, graph digitization, pooled yield or rate was imported.

The authors characterize mixed precipitates by SEM/EDS and XRD. Actual Figure S7
(p.24) labels calcite, vaterite and magnesite; Section 2.2 mistakenly cites S6,
which is growth/pH. This is an author phase assignment, not independent peak
re-refinement or proof of pure recovered minerals. Mn/Sr phase incorporation
remains proposed. No dissolved-lithium-to-product recovery is demonstrated;
Table S9's label of lithium retention as recovery is not adopted.

Source tensions preserved in the record:

- Section 2.1 says initial 10 minutes, whereas Figure 1 and Section 4.2 use hours.
  No 10-minute removal rate is accepted.
- Figure 1 Mg/Mn curves do not consistently match the text's removal percentages;
  its B. subtilis Mn comparator also declines despite the blanket no-precipitation
  statement. No removal percentage is curated.
- Inoculated Mn/Sr trajectories in Figure S5 differ from Figure 1. They are separate
  comparisons, not pooled or presented as an identical replicated series.
- Table S7 magnesite saturation indices are negative while Section 2.2 describes
  positive values. Modeling is not accepted as independent phase confirmation.
- Section 4.4 describes ICP-OES dilution in nitric acid but does not clearly define
  the solid/liquid separation for every elemental time-point sample. Explicit
  filtration concerns anions; explicit supernatants concern the urea assay.
  No filtered-dissolved-only analytical fraction is invented. Table S2 omits Li
  wavelength despite the main text naming Li analysis.
- Nonsterile brine and absence of a matched-pH chemical or killed-biomass control
  limit exclusive cellular attribution. The study supports the scoped treatment
  comparison, not proof that all mineral precipitation requires living cells.
- The cow-urine assay used synthetic CaCl2 solution, whereas SYE-grown cells were
  tested in natural brine. They are not combined into one natural-brine protocol.
- Flask tests, slurry preparation and cost arithmetic do not establish industrial
  deployment or proven compatibility/performance of downstream DLE.

The examiner visually inspected main Figure 1 and SI Table S1, Figure S5 and
Figure S7 after PDF rendering, and read full methods/results plus SI text/tables.
The precise retained PDF hashes are available for independent reinspection.

## Handoff and priorities

1. Accept only the reviewed primary-resource root plus its qualified laboratory
   pretreatment mechanism, after independent record review and root batch gates.
   Per-file strict validation passed on 2026-10-11; canonical CREATE history is
   `history/records/lithium-bearing-geothermal-brine/2026-10-11T095832Z-codex-9ee06e.yaml`.
   This dossier is not a substitute for the independent review.
2. Resolve raw timing, Mg/Mn percentages, Mn/Sr arm provenance and ICP-OES sample
   fraction/lithium wavelength from a public correction or raw data if released.
   Source weaknesses are preserved, not repaired with invented measurements.
3. Investigate SI reference 10, Hu et al., Water Research 190 (2021) 116753,
   on hypersaline produced water: acquire full primary methods, determine exact
   feed provenance, consortium and lithium relevance before creating another root.
4. A separate search lead, patent WO2025208228A1, describes biological brine
   pretreatment. Only discovery text was inspected; primary patent examples and
   status were not assessed and no claims are imported. Patent wording is not
   deployment evidence.

No author contact, schema work by this lane, existing-record edits or publication
was performed. The root owns the narrowly motivated schema change and acceptance.
