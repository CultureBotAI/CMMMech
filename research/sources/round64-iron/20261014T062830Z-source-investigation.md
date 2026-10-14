# Iron oxyhydroxides: round64 source investigation

Created **2026-10-14T06:28:30.628477+00:00** by Codex (GPT-6), agent `/root/round64_iron`, in
`/private/tmp/CMMMech-expansion-round64-20261014` on
`curate/cmm-expansion-round64-20261014`, trusted base
`0f4d8ff9e4919714e3dd902dc3573e95922a65fb`.
This is a curator dossier; scientific acceptance requires separate independent
record-review observations. Coordinator confirmed the baseline before record writes.

## Selection and identity

1. **Akaganeite:** strongest selected causal comparison. Levar et al.2017 provides
   a complete original, XRD-assigned synthetic substrate, PCA wild type and
   deletion mutants, cell-free controls and separate pH/autoclave comparisons.
2. **Lepidocrocite:** O'Loughlin et al.2019 provides complete donor survey and
   formate-arm chemistry, multiple analytical fractions and phase-specific
   diffraction/Mossbauer comparisons. Its weaker causal controls and two source
   identity ambiguities are preserved rather than hidden.

The fresh official [IMA September2026 master list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf),
pp1–2,5,124, distinguishes akaganeite (Rn,IMA1962-004,
(Fe(III),Ni(II))8(OH,O)16Cl1.25·nH2O) from lepidocrocite
(A,Fe(III)O(OH),1980 s.p.). The latter date is special-procedure history, not an
approval identifier. Synthetic beta-FeOOH shorthand does not establish the
ideal IMA formula or Ni concentration of an experimental preparation. Neither
record inherits elemental iron criticality; no jurisdiction/list claim is made.

Live NCBI taxonomy XML grounds PCA at243231 and CN-32 at319224, each now reported
as strain rank. Indexed browser excerpts can report no rank; the retained live
XML is the version actually checked. ATCC51573 explicitly identifies PCA.
ATCCBAA-453 identifies CN-32, while **BAA-543 identifies Cellulomonas sp.ES5**.
The2019 paper repeatedly names CN32 but prints BAA-543. The record follows the
reported name and explicitly declines to authenticate its experimental stock.

## Evidence actually inspected

### Akaganeite

[Levar et al.2017, DOI10.1038/ismej.2016.146](https://doi.org/10.1038/ismej.2016.146):
complete12-page publisher PDF, EuropePMC XML, publisher HTML, Table1,
Methods pp742–744, Results pp745–749 and Figure2 (PDFp6) inspected.
Initial slow precipitation, wash, <24h age, modified medium,1:9 mineral/medium
mix, acetate, phosphate, absence of added fumarate/chelator, gas, inoculation,
pH6.8vs6.3 and freshvsautoclaved status are recorded. The source gives the
**acid-extraction temperature**, not a mineral incubation temperature; none is
invented. The nearby20mMFe sentence follows the goethite recipe and is not
transferred into the akaganeite loading.

Wild type reduces the substrate; delta-cbcL begins but stalls, and fresh pH6.8
delta-imcH has a roughly7-day lag. Autoclaving shortens that lag atpH6.8 but does
not restore the strongly suppressed pH6.3 phenotype. The reported14-day
cell-free control has no observable reduction, while Figure2 cultures extend
approximately14–15days; those times are not silently equated. Replication is
triplicate and at least duplicated incubations. FeII is the0.5NHCl extract,
not dissolved-only Fe. No percentage or digitized figure endpoint is invented.
Fumarate pH-growth comparisons help constrain a gross growth-defect explanation.

Mineral redox potential was **inferred**, whereas Figure1 measured soluble
FeIII-citrate potentials. Similar powderXRD does not rule out short-range/surface
changes. Direct ImcH/CbcL quinone transfer and a universal threshold are not
asserted; cited prior complementation is not a new Figure2 control. No pure
product, feed-conversion percentage, metal recovery or deployment is claimed.

### Lepidocrocite

[O'Loughlin et al.2019, DOI10.3390/min9070434](https://doi.org/10.3390/min9070434):
complete30-page publisher PDF plus the [OSTI1560537 deposited original](https://www.osti.gov/servlets/purl/1560537)
(29pages), Methods2.1–2.3, Results3.1–3.3, Figures1–6, Tables1–3 and Discussion
inspected. OSTI's landscape Table1 is fully visible; the publisher file clips
the right side. Both are the same experiment and retain the accession typo.
Table1 endpoints used here are62days for formate,64days for hydrogen, and72days
is the separate survey window; endpoints are never pooled. Pyruvate prose
mentions106days while its Table1 footnote gives49days; no pyruvate endpoint
measurement is curated. Rates are fitted and have their source's mmol/day
label; no rate or kinetic comparison is imported.

Formate-arm setup: Bayferrox943 lepidocrocite,80mMFeIII,75mMformate,100µMAQDS,
25mMNaCl or Na2SO4,200mL/250mL serum bottles, initialpH7.5,triplicate,
5×10^9cells/mL,30°C,dark rolling,62days. TotalFeII is the one-week0.75MHCl
extract; aqueousFeII is the0.22µm filtrate. Table1 formate endpoints are
57.6±0.2/55.1±2.4mM total and0.8±0.1/0.7±0.1mM aqueous respectively.
These are assay-defined concentrations, not isolated recovery yields.
Figures5–6 and Tables2–3 support formate consumption, loss of detected
lepidocrocite and carbonate-green-rust formation; transient sulfate-green-rust
appears in the sulfate arm. PlateauedFeII is not total FeIII reduction because
green rust retains ferric Fe. Nondetection is not a measured zero or purity.

The donor-free survey still produced3.6mMFeII, and several other donors
produced<7mM. Separate H2/Pd/AQDS/carbonate abiotic treatment exceeded the
H2 biological arms and also formed carbonate green rust. It is not a matched
formate control. No uninoculated matched formate series is reported in the
inspected original. Thus the record says culture-associated transformation,
not unique biology, direct cell contact or a proven enzyme.

Inherited DMM/inoculum recipes were not independently recovered; their exact
components are not asserted. The lepidocrocite-characterization reference28
resolves to an **akaganeite**2015 paper. Contemporaneous starting Figure6
patterns support phase identity, but no exact surface area or chemical purity
is inferred. Thermodynamic carbonate activities were modeled, not measured.

### Comparative context and contradictions

The retained [Sklute et al.2023 original](https://doi.org/10.3389/fmicb.2023.1272245)
was reinspected, not newly downloaded. Methods, akaganeite/lepidocrocite results,
Discussion, supplementaryS8,S12,S16 and their rendered pages12,16,20 constrain
universal interpretations. Hydrogen-fed Ax17 at55°C yielded dark nonmagnetic
solids and amorphous iron-rich nanospheres. Oxalate-extractableFeII was not
significantly above controls for either mineral, but this is an analytical
fraction limit, not a universal no-reduction result. Akaganeite has new ferric
and ferrous Mossbauer components with nonunique fits; lepidocrocite spectra
are nearly unchanged and only allow hidden small green-rust amounts.
Main-text lepidocrocite bulkXRD is explicitly unavailable. SupplementaryS16
erroneously labels lepidocrocite while describing akaganeite/NaCl and matching
its main-text assignment; it is not treated as confirmed lepidocrocite data.
These are different assays, organisms, feeds and extractions, retained as
`context_only`, not direct replication or refutation of the selected experiments.
No Ax17 quantitative yield is imported and no new recognized green-rust species
is inferred from unresolved assay labels.

## Search, acquisition, reuse and limits

The companion JSON records exact queries, dates, paths, URLs, acquisition
failures, raw hashes and validation. Web coverage is first returned result sets
plus selected primary/authority follows, without pagination. Search-engine
publication freshness labels were not used as article dates. DOI metadata
agrees with primary identity and has no update-to/updated-by fields; Levar's
preprint relation is not independent replication. ExactDOI/title correction,
erratum and retraction searches returned no identified matching notice in this
bounded inspection. This is not a universal no-notice claim. MDPIHTML/XML
returned403/429; PDF/OSTI copies supplied originals. Initial sandbox DNS failures
are recorded separately from successful authorized downloads. ACS inherited
methods remained unavailable; no paywall circumvention or author contact occurred.

Deduplication used hidden-and-ignored-inclusive `rg` over this worktree's
records,research,reviews,history and cited raw roots
`/private/tmp/cmm-round5-iron-evidence-20261011`,
`/private/tmp/cmm-round14-mineral-raw`, and
`/private/tmp/cmm-round20-goethite-raw`.
Existing iron/ferrihydrite/magnetite/goethite/pyrolusite records mention these
phases, but neither species owns an existing record. Names, IMA1962-004,
selected DOI/PMC identifiers and source experiments were checked; DOI duplicates
from mirrors are not additional studies. This is not a machine-wide absence claim.

Originals stay outsideGit. Levar declaresCCBY-NC-SA4.0, O'Loughlin2019 and
Sklute2023CCBY4.0, IMACCBY-SA3.0. Authority webpage reuse terms were not assessed;
only identifiers and original curation descriptions enter records.
The schema already represents these claims; mM values remain prose and no
mg/kg observations, schema changes or synthetic corpus fixtures are introduced.

## Handoff and next priorities

Both records have canonical CREATE sidecars and distinct inline creation events.
Final byte hashes, paths and affected validation are in JSON; coordinator owns
fullbatch gates and independently assigned scientific reviews. This dossier is
not their acceptance verdict.

- Assess feroxyhyte from acquired O'Loughlin2021 DOI10.3390/min11020149;
  coordinator assigned a separate curator after this lead emerged. Its43-page
  original and methods are retained; no claims from it silently broaden these records.
- Recover exact inherited2008DMM and2015characterization originals before
  expanding the2019 method claims. Resolve its strain accession discrepancy if
  provenance evidence becomes available; do not silently replace it.
- Assess Mo-bearing akaganeite2017 DOI10.1039/C7CE01569K from complete original
  before attributing Mo fate. Abstract-only lead remains uncurated.
- Resolve recognized green-rust species identity before any new product owner.

