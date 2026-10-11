# Lutetium, thulium and promethium curation dossier

Created 2026-10-11T07:55:13Z by codex / GPT-6 / codex in
`/private/tmp/CMMMech-expansion-round11-20261011`, branch
`curate/cmm-expansion-round11-20261011`, trusted base
`a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c`.
[Acceptance issue 44](https://github.com/CultureBotAI/CMMMech/issues/44).
This is a curation dossier, separate from the independent scientific reviews.
The [JSON receipt](round11-lu-tm-pm-20261011.json) supplies exact searches,
acquisition timestamps, file checksums, access failures and final record hashes.

## Selection and decisions

- [Lutetium](../../data/records/lutetium.yaml): accept an element record with
  the Lu-specific, controlled mixed-solution assay in Breuker et al. (2020).
- [Thulium](../../data/records/thulium.yaml): accept an element record with
  Moriwaki et al.'s comparison of prepared wild-type and LTA-defective bacterial
  powders. The genetic comparison, explicit biomass processing and acid elution
  make it useful, while substantial residual adsorption limits causal claims.
- [Promethium](../../data/records/promethium.yaml): accept verified identity and
  Australia's explicitly enumerated group designation. Defer a microbial
  mechanism because the promising radiotracer report could not be visually
  inspected and its carrier/background calculations remain unresolved.

These are elemental roots, not ions, chlorides, isotopes, minerals or commodity
mixtures. Fresh ChEBI pages and public API records resolved **CHEBI:33382**
(lutetium atom), **CHEBI:33380** (thulium atom) and **CHEBI:33373** (promethium
atom), each a neutral entity. No ion identifier is substituted for the root.

The [USGS Final 2025 List](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
Federal Register notice of 7 November 2025, names Lu and Tm explicitly. The
summary enumeration establishes list membership; the later table's Yes/No
column concerns byproduct production, not critical/noncritical status.
[Australia's department page](https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list)
was inspected live through the web reader, including its 20 February 2024
revision statement, Table 1 rare-earth group and footnote 17. That footnote
explicitly includes Pm. This supports a source-specific group mapping, not an
individual score or an inference from generic lanthanide membership. Direct
HTML downloads timed out twice; the retained web extraction is identified as
such. Neither record asserts these editions remain the latest for all purposes.

## Lutetium: what the primary experiment establishes

[Breuker, Ritter and Schippers, Metals 2020, 10, 954](https://doi.org/10.3390/met10070954)
and its [five-page supplement](https://mdpi-res.com/d_attachment/metals/metals-10-00954/article_deploy/metals-10-00954-s001.pdf)
were acquired from the publisher's asset host. All article methods/results and
supplement text were read. Rendered main pages 3, 5, 6, 8 and 11 and supplemental
pages 1 and 4 were checked, covering the organism table, Figures 1, 2, 4 and 7,
Table S1, Figure S1 and the separate immobilization arm.

Table 1 identifies **B. subtilis ATCC 7003**, grown in FP medium at 30 °C,
120 rpm for two to four days. The [ATCC authority](https://www.atcc.org/products/7003)
confirms B. subtilis, NRS 730; this is not strain 168. NCBI Taxonomy 1423
resolves the species only. Washed, non-autoclaved biomass was contacted with
acidified chloride solutions containing eight REEs, each at 15 µmol/L, using
5 g dry biomass/L at pH 2.5 and room temperature. Centrifuged, filtered
supernatants were measured by ICP-MS, with concurrent no-biomass controls.

Table S1's **eight-element experiment 2** reports Lu means of 74% at both
2 h and 4 h from two parallel assays. The denominator is the contemporaneous
no-biomass control concentration, following Methods 2.2. Neither independent
culture replication nor a recovered product mass balance follows from this
percentage. The four-element experiment 1 and Figure S1 have no Lu column or
series. The previous Horiike T9 study likewise has no Lu, Tm or Pm assay;
its REE class membership cannot supply those missing observations.

The accepted interpretation is biomass-associated biosorption as operationally
measured by control-relative aqueous depletion. It leaves cell-surface binding,
cell-associated precipitation and intracellular retention unresolved. The paper
calls untreated biomass living, without an assay-specific viability result.
Figure 7's separately prepared autoclaved comparison at 4 g/L cannot isolate
metabolism from changed cell integrity. Figure 1 shows lower fractional Lu
removal at higher loading. Figure 4's Fe/Zr comparison has different baseline
Lu percentages from Figure 2 and supports only its paired condition. Proposed
phosphate/carboxyl explanations are not demonstrated Lu-specific ligand
assignments. The wastewater experiment is Gd-specific and is not adopted as
Lu recovery or deployment evidence.

## Thulium: inactive biomass, conditional mutant and elution boundary

[Moriwaki et al.](https://doi.org/10.1007/s00253-012-4200-3) appeared online on
12 June 2012 and in Applied Microbiology and Biotechnology 97, 3721–3728 (2013).
The [Shinshu repository](https://soar-ir.repo.nii.ac.jp/records/13337) marks its
24-page file as an **accepted manuscript**, deposited in 2014. The publisher
page provides metadata/abstract and subscription access, not full text. All
manuscript methods/results/discussion, Tables 1–3 and Figures 1–3 were read;
Table 1, Table 3 and all three figures were visually checked. Referenced
**Table 4 is absent** from this deposited manuscript, so no fitted capacity
is accepted as a measured endpoint. No supplementary file was identified in
this bounded manuscript/repository/publisher inspection or exact-DOI search.

NCBI Taxonomy **224308** resolves the parental *B. subtilis subsp. subtilis*
strain 168. It does not uniquely identify engineered **RY1604**. The methods
construct three deletions plus IPTG-dependent ltaS expression; cells were
prepared after IPTG removal. Table 1 prints `yvyJ` while methods use `yvgJ`;
the record preserves this source discrepancy. No complemented adsorption
comparison is reported.

Both powders were boiled for 20 min, washed, freeze-dried, crushed and sieved
to 53–100 µm. At 25 °C, 20 mg powder contacted 20 mL of Tm solution at pH 3
for 30 min at 10 rpm, followed by filtration, centrifugation and ICP-AES.
Table 3's visually checked concentration unit is **µg/mL**; text extraction
misread it as mg/mL. At 20 µg/mL, Table 3 reports 90% WT and 74% defective
removal. At 100 µg/mL, the respective outcomes are 35% and 29%, preserving
loading dependence. Figure 2 supports rapid depletion but does not supply
replicate precision. The paper reports filter-associated metal retention below
10%; it does not specify a blank-correction calculation or Table 3 uncertainty.

Removal persisted in the defective preparation, so the comparison does not
establish an exclusive LTA-mediated route or quantify LTA's contribution.
Residual LTA was not measured; the conditional preparation cannot establish
that LTA is unnecessary. Surface morphology and ligand discussion do not quantify contributions
from LTA, WTA or other groups. Both adsorption-isotherm models fit; the authors
explicitly decline to use that fit to distinguish mechanisms. A separate acid
step used two 20-mL portions of 2.7 M nitric acid. The greater-than-94% recovery
statement is across La/Eu/Tm adsorbed ions, without a per-element elution table;
it is not recovery of that fraction of the starting Tm feed. No purified
Tm metal, ore treatment, reusable process lifetime or industrial deployment is
established by the accepted study.

## Promethium: valuable source lead, incomplete acquisition

The 1991 paper [DOI 10.1524/ract.1991.54.2.91](https://doi.org/10.1524/ract.1991.54.2.91)
was resolved through Crossref and the authors' Chalmers publication record.
Their page range differs: Crossref 91–96, Chalmers 91–95. DOI/publisher HTML
and PDF requests yielded empty HTTP 202 responses. These are not acquired full
text. Tracing references located the authors' primary **SKB TR90-26, June 1990**:
[official report](https://skb.se/publikation/5749/TR90-26_OCR.pdf).
The report's full prose, method descriptions, results, table extraction and
figure captions were inspected through the web reader. Direct downloads from
`skb.se`, `www.skb.com`, and one alternate official archive route failed;
web screenshot attempts timed out. No binary-PDF checksum or visual examination
of the figures/Table 1 is claimed.

The report describes washed **CCUG-22948**, historically called *Shewanella
putrefaciens*, held in saline before radiotracer assays. It uses **147Pm plus
inactive neodymium carrier**, so its nominal concentrations cannot silently
be treated as independently verified pure-Pm concentrations. Partitioning is
calculated from pre/post-centrifugation radioactivity, with appreciable no-cell
background and pH/cell-density effects. Desorption after saline resuspension
is incomplete; biological specificity, phase identity and irreversible uptake
are not established. The report itself discusses precipitation as an alternative.
These are research observations requiring primary figure and calculation
review, not accepted mechanism measurements. The [CCUG page](https://www.ccug.se/strain?id=22948)
withholds strain details, and earlier isolation-report text calls the isolate
atypical. No modern taxon ID is assigned. The report and related journal paper
form one study lineage, not two independent validations.

A future mechanism addition requires accessible figures/Table 1, reconciliation
of carrier use, units and background corrections, and an assessment of the
historical isolate's taxonomic resolution. The identity/designation-only record
remains useful CMM coverage without representing this gap as evidence of no
microbial interaction.

## Search, source terms and provenance

The JSON logs 34 exact queries across identity, authority, biosorption,
acquisition, corrections/retractions and contrary evidence. Results were
bounded first-page sets without pagination. No applicable correction notice was
identified there; that is not an exhaustive negative claim. Separate Tm
macroalgal studies, Lu/REY fractionation and lanmodulin-decorated microbes remain
unassessed leads. An abstract cannot supply uninspected controls or methods.

Deduplication used `rg --no-ignore --hidden --follow` in `data/records`,
`research`, `reviews`, `history`, `.claude`, and bounded cited raw roots
`/private/tmp/cmm-next-eu`, `/private/tmp/cmm-expansion-authorities-20261011`,
`/private/tmp/cmm-round8-y-yb-evidence`, and this task's raw directory.
No relevant symlinks were found in these trees. Existing authority proposals
and prior research were present, but no earlier exact accepted Lu/Tm/Pm root
was found. Follow-up identifier/study search after drafting found only these
new owned records. Relevant PDFs were inspected separately from text searches;
no machine-wide absence is claimed.

Raw evidence is retained at `/private/tmp/cmm-round11-lu-tm-pm-raw`.
Breuker states CC BY 4.0. The Moriwaki repository provides a reading copy but
no identified redistribution license; primary source bytes remain outside Git.
SKB reuse terms and bulk authority reuse were not established. Only original
factual curation and acquisition metadata are committed. Expiring repository
redirect query strings are omitted from the committed receipt; the stable
source URL and actual local SHA-256 remain recorded.

## Curation and verification

Root's baseline completed before writes: 307 passed, 3 skipped; 61 records and
72 histories valid. Named validation before history passed for Lu/Tm (2/0)
and Pm (1/0). After actual CREATE sidecars and separate inline events were
attached, all three named records passed (3/0, terminal exit 0).

- [Lu history](../../history/records/lutetium/2026-10-11T075300Z-codex-aa9d5e.yaml)
- [Tm history](../../history/records/thulium/2026-10-11T075320Z-codex-34a805.yaml)
- [Pm history](../../history/records/promethium/2026-10-11T075338Z-codex-e70863.yaml)

No schema, validator, tests, dependency or governance edits were needed.
The parent coordinates full-batch gates and separate independent scientific
reviews. This dossier does not claim those later checks are already complete.

## Independent review correction

At 2026-10-11T08:02:40Z, [issue 45](https://github.com/CultureBotAI/CMMMech/issues/45)
was addressed after the saved [initial Tm review](../../reviews/structured/20261011T080136Z-thulium-round11-independent/review.md)
identified a minor causal overstatement. The record and this dossier now state
that residual removal in the LTA-defective preparation cannot establish an
exclusive LTA route or quantify its contribution. Unmeasured residual LTA means
the comparison does not show LTA is unnecessary. Measurements and other
uncertainties are unchanged. Actual [EDIT history](../../history/records/thulium/2026-10-11T080225Z-codex-327926.yaml)
and a separate inline event preserve this correction; CREATE history and the
initial review remain unchanged. Successor independent disposition is separate.
