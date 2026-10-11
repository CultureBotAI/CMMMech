# Round 7: holmium, erbium and gadolinium evidence

Created 2026-10-11 UTC by codex (GPT-6; codex). The companion
[JSON receipt](round7-ho-er-gd-20261011.json) records the actual UTC completion
time, source acquisition times/hashes, searches, failures and final record hashes.
Trusted base: `58e7aef16a9643438cf621fa9fb402e9d325dc65`.
Worktree: `/private/tmp/CMMMech-expansion-round7-20261011`.
Branch: `curate/cmm-expansion-round7-20261011`. Acceptance issue: [#34](https://github.com/CultureBotAI/CMMMech/issues/34).

## Selection and identity

These three previously unrepresented individual elements have separate analytical
results in one accessible primary study. They are therefore suitable additions
without inferring individual uptake from an undifferentiated REE total. They do
not constitute three independent studies. Their mechanism is deliberately
recorded as **association with a harvested cyanobacterial fraction**, because the
experiment cannot resolve passive binding, active uptake and retained abiotic
material.

| Record | Live ChEBI identity | Dated criticality |
|---|---|---|
| [Holmium](../../data/records/holmium.yaml) | CHEBI:49648, holmium atom, Ho, charge 0 | USGS Final 2025 List, holmium row |
| [Erbium](../../data/records/erbium.yaml) | CHEBI:33379, erbium atom, Er, charge 0 | USGS Final 2025 List, erbium row |
| [Gadolinium](../../data/records/gadolinium.yaml) | CHEBI:33375, gadolinium atom, Gd, charge 0 | USGS Final 2025 List, gadolinium row |

The primary [GovInfo notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
was acquired and each named row checked on page 50496, Federal Register
90:50494–50497, 7 November 2025. The table's “Yes” column denotes byproduct
production, not criticality; membership in this named final list establishes the
2025 designation. No timeless or latest-edition claim is made. The element roots
remain distinct from their ions, nitrate reagents, minerals, commodities and
manufactured materials.

The experimental strain is reported as *Arthrospira platensis* CNMN-CB-02.
The [official collection entry](https://cnmn.utm.md/collection_page/21) identifies
CNMN CB-02 as *Spirulina platensis*, with genomic information shown as a dash.
Live NCBI Taxonomy XML maps both published names to the current species node
118562, *Limnospira platensis*. This supports the species-name mapping, not a
strain-specific genome accession or verified strain-level NCBI identity.

## Primary evidence inspected

[Zinicovscaia et al. (2024), Microorganisms 12:122](https://doi.org/10.3390/microorganisms12010122),
PMCID PMC10818318, PMID 38257949, published **7 January 2024**. The publisher PDF,
full JATS XML and all five original figure JPGs were inspected. The article is
CC BY 4.0. Its EuropePMC “supplementaryFiles” package contains ten assets: five
main figures in JPG/GIF pairs. The full XML has no supplementary-material node;
the data statement says data are within the article. No separately deposited
replicate data were obtained. Raw files remain outside Git at
`/private/tmp/cmm-round7-ho-er-gd-raw`.

The relevant experiment used separate Ho, Er and Gd series, each at 10, 20 and
30 mg/L elemental concentration, introduced as the stated nitrate hydrate.
A mixed-element competition/selectivity experiment is not reported. Cultures
received the element on day 1 with 0.4 g/L inoculum and grew for five more days
in 500 mL working volumes, pH 10.0 and 30 °C. Medium included 8 g/L bicarbonate
and 0.08 g/L EDTA. The source's nonstandard illumination unit,
“55 µM photons/m2/s,” is retained as printed. Shaking was at 100 rpm for 45 min,
twice daily, 12 h apart. Experiments are described as triplicate, with Student
t-tests against cultures grown without REEs.

Biomass was collected on 5–8 µm filters and part dried for neutron activation
analysis. The analytical result is **mg element/kg of this dried harvested
fraction**, not an aqueous residual concentration or isolated recovery yield.
The source reports analytical reference-material agreement. It does not describe
post-filtration washing, a matched biomass-free exposure control, subcellular
fractionation or a final aqueous mass balance. The nutrient medium's alkalinity
makes unmeasured chemical partitioning an important alternative; no particular
precipitate is established. All three records use `process: other` and explain
these limits rather than asserting a resolved transport or binding pathway.

| Element | Accepted observation | Important qualification |
|---|---|---|
| Ho | Source-reported 4780–25,780 mg/kg; increase across exposure series | Ho is below Er at 10 mg/L in Figure 1, so the paper's general Gd > Ho > Er rank is not universal |
| Er | Source-reported 5470–21,400 mg/kg; increase across exposure series | Growth inhibition in this protocol is not a universal strain response |
| Gd | Biomass-fraction concentration increases across exposure series | The textual maximum 27,400 mg/kg does not visually match the highest Figure 1 bar; exact endpoint agreement is unresolved |

No numerical values were digitized from plot pixels. No structured concentration
observations were added: the contract requires exact source table cells and
analysis dates, which are unavailable for this graph-only series.

## Contradictions and negative outcomes preserved

- Figure 2 shows lower Ho/Er biomass quantities, while the exact declines in
  the prose are not clearly reproduced by the corresponding plotted control
  and treatment heights. Records retain the direction and flag this issue;
  they do not report reconciled inhibition percentages.
- The Gd conclusion broadly says protein content was unaffected, whereas
  Section 3 and Figure 3a show a decline at 30 mg/L. Figure 3d's Gd bar at
  10 mg/L is above control, contrary to the prose's blanket at-or-below-control
  description. Declining carbohydrates and phycobiliproteins also prevent a
  blanket physiological-safety claim.
- [Yushin et al. (2022), Materials 15:6101](https://doi.org/10.3390/ma15176101),
  PMCID PMC9458052, PMID 36079481, reports no significant Er-related biomass
  change under a different living-culture protocol. The complete XML methods
  and results were read, and Figure 6 on publisher PDF page 10 was rendered
  and visually checked. Its Er sulfate treatment, pH 8–9, 25–28 °C and lower
  illumination differ from the 2024 nitrate experiment; the outcomes are not
  direct replications. The 2022 control is printed in mg/L in the prose but
  g/L on the graph, so its numerical biomass value is not reused.
- The 2022 paper's separate dried-biomass experiments avoided pH above 6
  because of Er(OH)3 formation. This supplies primary context for precipitation
  risk; it does not prove what phases occurred in the 2024 alkaline medium.
  Its dried-biomass removal experiments are a separate possible future
  mechanism, not imported without further figure/control reconciliation.

No tested desorption, purified-product yield, real-effluent remediation or
industrial operation is asserted. A laboratory culture growth experiment is
not evidence of deployment.

## Search, novelty and acquisition limits

Before writes, `rg --no-ignore --hidden -L` searched `data/records`, `research`,
`reviews` and `history` for the three names, DOI tokens and PMCIDs; `.git` and
`.venv` were excluded. Names were already present in authority/frontier
inventories, but no accepted target root was found in those bounded searches.
The earlier Er paper was already cited within the round 5 Dy source XML in
`/private/tmp/cmmmech-round5-ree-raw`; it was not a curated Er root. The current
study was a parent-provided lead, not an asserted novel discovery. Relevant raw
files were checked by DOI/PMCID. This is not a machine-wide absence claim.

The JSON records all exact queries. Search provider: web search, 11 October
2026 UTC, first returned result sets, no filters or pagination. Title/DOI plus
correction/retraction searches surfaced no matching notice; that is not proof
of absence. The 2024 XML explicitly says `is-retracted=no`. Searches for the
strain and for alkaline/precipitation controls surfaced the 2022 comparison,
which changed the Er record's interpretation.

Access failures were retained: PMC recaptcha, publisher HTML HTTP 429,
sandbox DNS failure, an earlier-PDF web-open error, and CNMN direct-download
HTTP 403. Legitimate EuropePMC/publisher transfers supplied both primary
papers. CNMN was read via the web tool, with no retained HTML claimed. A
provisional round 6 raw-directory guess did not exist; a bounded temporary
folder inventory encountered an unrelated inaccessible daemon directory.
Neither is used as evidence that scientific material is absent elsewhere.

## Curation and validation

Parent reported the terminal baseline before record edits: **307 tests passed,
3 skipped; 36 records and 46 history sessions valid**. Each new record was
created before its canonical CREATE session using actor `codex`, model `GPT-6`,
tool `codex` and issue 34. Distinct actual inline events and sidecar references
were added before final hashes.

- [Ho CREATE history](../../history/records/holmium/2026-10-11T060018Z-codex-7c7d08.yaml)
- [Er CREATE history](../../history/records/erbium/2026-10-11T060023Z-codex-39384e.yaml)
- [Gd CREATE history](../../history/records/gadolinium/2026-10-11T060028Z-codex-538546.yaml)

Named-record validation passed: **3 checked, 0 failed**. Full-batch checks and
independent scientific reviews are coordinated by the parent. This dossier is
curation evidence, not a self-issued scientific review. No schema, validator,
tests, dependencies, governance or shared history was modified.

## Remaining work

1. Obtain source replicate data and reconcile exact growth percentages, Gd
   endpoint concentration and contradictory biochemical summaries.
2. Distinguish dissolved, precipitated, surface-bound and intracellular
   fractions with matched sterile controls, washes and speciation analyses.
3. Assess the 2022 Er dried-biomass arm as a separate mechanism, including its
   fitted versus measured capacities and analytical/control limits.
4. Follow primary reference 26, DOI `10.1016/j.jre.2020.07.019`, for individual
   Yb/Tb/other REE assays. A citation alone does not support those records.
