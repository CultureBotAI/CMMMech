# Terbium source assessment and curation handoff

Created 2026-10-11T06:00:22.603474+00:00 by codex / GPT-6 / codex. Worktree
`/private/tmp/CMMMech-expansion-round7-20261011`, branch `curate/cmm-expansion-round7-20261011`,
trusted base `58e7aef16a9643438cf621fa9fb402e9d325dc65`.
This is curation provenance; the independent scientific review is separate.

## Selection and identity

The [round6 handoff](round6-frontier-20261011.md) already identified
[Paper et al. 2023](https://doi.org/10.3389/fbioe.2023.1130939).
The primary screen directly tested individual terbium with named cyanobacterial
strains, making it a stronger starting point than a total-REE result. The record
selects **Synechococcus elongatus UTEX 2973**, whose strain identifier can be
verified directly, rather than inheriting detailed cerium assays into terbium.
Nostoc sp. 20.02 is another positive screen result, but its taxonomic placement
is explicitly uncertain in Section 4.1; no guessed species identifier was added.

The root is the element, [CHEBI:33376, terbium atom](https://www.ebi.ac.uk/chebi/CHEBI:33376),
formula Tb and charge zero. It does not identify its dissolved experimental ion,
salt, phosphor, mineral or waste. [NCBI Taxonomy 1350461](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1350461)
resolves the exact UTEX 2973 strain. The [USGS Final 2025 List](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
Federal Register 90:50494-50497, 7 November 2025, names terbium on **page 50497**.
That named mineral commodity is mapped explicitly to the elemental root; no
claim about every Tb-bearing material or timeless criticality is made.

## Experiment and analyte boundaries

The primary article is by Paper, Koch, Jung, Lakatos, Nilges and Brück,
Frontiers in Bioengineering and Biotechnology 11:1130939, published
28 February 2023; PMID 36926689, PMC10011134. Publisher HTML and acquired
EuropePMC full-text XML agree. Table 1 and Sections 2.1-2.5 establish:

- UTEX 2973 biomass cultivation in BG11 at 37 degrees C, constant illumination
  of 300 micromol photons per square metre per second, pH 8 maintained with CO2,
  in a 3.7 L photobioreactor; stationary-phase centrifugation harvest.
- Three demineralized-water washes, freezing at -80 degrees C and lyophilization
  before the separate sorption assay. No viability measurement is reported.
- Single-metal screening at 10 mM and initial pH 5 +/- 0.2, with 10-20 mg dry
  biomass in 2 mL solution for 3 h, shaken at room temperature. Numerical room
  temperature, strain-specific biomass mass and Tb counter-ion are unspecified.
- Triplicate experiments, without distinguishing independent biomass preparations
  from technical replicates; centrifugation at 10,000 rcf for 5 min followed by
  supernatant ICP-OES with multielement calibration standards.

The original publisher Figure 2 was visually inspected, including its legend:
the third bar in each strain group is **terbium**, and UTEX 2973 has a positive
apparent-uptake endpoint. Its Qmax axis is mg REE per g dry biomass. The record
retains this qualitative result without inventing an exact digitized value,
error-bar definition or a fitted maximum. The abstract's range across four
REEs does not supply a separate precise Tb measurement. An uptake percentage
cannot be inferred without the exact strain-specific biomass mass.

Sections 2.6-2.10 and 3.3-3.7, Figures 3-7, and the acquired **Table1.DOCX**
Supplementary Tables S1-S2 describe cerium follow-up assays. All supplement
cell text was inspected: Table S1 gives Ce Langmuir parameters and Table S2
Ce Freundlich parameters. No Tb fit or per-replicate Tb table was found there.
The Ce kinetic equilibrium, pH optimum, ion exchange, competing-metal behavior
and FTIR assignment therefore remain outside the accepted Tb mechanism.
The water-only ion-release comparator belongs to the Ce/Al/Pb/Ni/Zn assay;
it is not a biomass-free Tb solution control.

## Adversarial limits preserved during curation

The inspected primary article and two supplementary tables report no matched
biomass-free Tb result. Apparent uptake from the concentration difference does
not isolate every possible loss pathway; no direct Tb-phase or exclusive
surface-binding interpretation is asserted. Lyophilized microbial biomass is
represented as microbial material without claiming a living, growth-dependent
or sterilized system. This laboratory screen demonstrates neither Tb-selective
separation from other REEs, regeneration, purified-product yield, nor industrial
deployment. Section 4.2 explicitly places desorption and product extraction in
future work and recommends further assays with other REEs.

A bounded live correction/retraction search, including the exact DOI and title,
returned the original article, institutional copies and unrelated material.
No actual correction or retraction notice surfaced. A generic Frontiers
Correction filter is not such a notice. This is not proof of universal absence.
Other Tb biosorbent studies surfaced but use different strains and conditions;
their snippets are neither confirmation nor refutation of the selected assay.

## Search, acquisition and reuse

Hidden and ignored files were included with `rg --no-ignore --hidden -L` over
`data/records`, `research`, `reviews`, and `history`, plus the referenced round5
REE and round4 phosphorus/cerium raw-download directories and this task's raw
directory. Search keys included terbium, CHEBI:33376, the exact DOI and PMC
accessions. The accepted root was absent before creation within those bounds;
authority candidates and the known deferred paper were present. This is not a
machine-wide novelty claim. The companion [JSON dossier](round7-terbium-20261011.json)
lists exact queries, all acquisition URLs, UTC receipts, file hashes, derived
assets, terms, access failures and deferred leads. Web searches used the first
returned result sets, no date filters and no exhaustive pagination.

Raw files remain outside Git in `/private/tmp/cmm-round7-terbium-raw`.
The article specifies **CC BY 4.0**. Its article XML, complete supplementary ZIP,
15 extracted figure/DOCX assets and extracted text are individually hashed in
the JSON. Authority pages remain local; separate bulk-redistribution terms were
not assessed. An initial sandbox DNS failure was resolved by authorized network
access. A premature ZIP read while the same download was live failed; that
handle then completed and the full ZIP was successfully inspected. No failed
or partial file is treated as acquired evidence.

## Handoff and next work

[Terbium record](../../data/records/terbium.yaml), SHA-256
`c47181aa12c1c060c9e04e95c96c37552c4ec183032033dbf9f4500c71e40ffb`, and
[CREATE history](../../history/records/terbium/2026-10-11T055851Z-codex-8457ec.yaml)
are ready for an independent scientific review. The baseline had 307 passing
tests and 3 skips with 36 records and 46 histories; single-record validation
passed. Parent-owned batch validation and acceptance issue #34 remain separate.
No schema or validator change was needed.

Follow-up sources are ranked by the evidence gap they could close, and were
**not** fully audited or accepted in this pass:

1. [Jurkowski et al. 2022](https://doi.org/10.3389/fbioe.2022.833122), cited by
   Paper et al.: inspect Calothrix-derived Tb-binding compounds and controls
   before assigning a molecular mechanism to any strain.
2. [Galdieria ACUF427 biosorption](https://doi.org/10.3390/microorganisms10112138):
   inspect individual Y/Eu/Ce/Tb tables and selectivity for a possible new
   yttrium record; a group result would not suffice.
3. [Bacillus/Sporosarcina Tb enrichment](https://doi.org/10.1128/spectrum.00760-24)
   and [2025 Bacillus study](https://doi.org/10.3390/microorganisms13081753):
   independently assess controls, phase/EDS evidence and measured versus fitted
   outcomes before extending the Tb record.

Primary per-replicate Tb values, matched solution blanks and a real-product
mass balance remain concrete unresolved questions. They cannot be manufactured
from this screen or replaced by its cerium measurements.
