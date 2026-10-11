# Phosphorus and cerium: one fungal study, two distinct material outcomes

Investigation and curation: 2026-10-11 UTC, Codex (GPT-6), working tree based
on `c081a749cd63feafcc25414f5ad006d1f78f1e36`. Acquisition times and hashes
are in [the receipt](round4-phosphorus-cerium-20261011.json). This is a
curation dossier; acceptance requires separate independent record reviews.

## Selection and identity

The round3 frontier named phosphorus and individual REEs as research priorities.
Kang et al. provide accessible primary evidence for phosphate mobilization and
subsequent cerium precipitation. These are two stages of **one study**, not
independent replication or two new experimental datasets. Element roots remain
distinct from the mixed mineral feed, ions and precipitated compounds.

- [Phosphorus](../../data/records/phosphorus.yaml): live ChEBI:28659 resolves
  phosphorus atom, formula P, charge 0. Canada's official 34-entry list contains
  Phosphorus; its announcement establishes the **10 June 2024** update. The
  page's later modification date is not a new list edition. The announcement's
  isolated spelling “phosphorous” does not override the list's phosphorus label.
  The US 2025 **phosphate** designation is not mapped onto elemental phosphorus.
- [Cerium](../../data/records/cerium.yaml): live ChEBI:33369 HTML resolves
  cerium atom, formula Ce, charge 0. Web-tool opening failed, but ordinary HTTPS
  acquisition succeeded and the rendered text was inspected; this is not an
  identifier guessed from a neighboring accession. The final US 2025 list,
  Federal Register document 2025-19813, names Cerium individually.
- NCBI Taxonomy 380704 resolves *Aspergillus niger* ATCC 1015, a no-rank strain
  entry matching the primary Methods. No species ID is represented as a strain ID.

## Primary evidence inspected

[Kang, Csetenyi, Gao and Gadd (2022)](https://doi.org/10.1007/s00253-021-11721-0),
*Solubilization of struvite and biorecovery of cerium by Aspergillus niger*,
Applied Microbiology and Biotechnology 106:821–833; PMC8763747, PMID34981166.
Online publication is 4 January 2022; acceptance/copyright and DOI string include
2021, which is not the publication year used here. PMC/Europe PMC full text and
publisher HTML contain the Methods, Results and Discussion. Tables 1–2 and all
figure captions were read. Figures **1, 2, 3, 6 and 9** were downloaded and
visually inspected; no graph points were digitized. Figures 4–5 morphology and
7–8 thermal analysis were read as text/captions, not independently pixel-audited;
records do not rely on their morphology or thermal measurements.

XML contains no supplementary-material node, and full-text PMC/publisher HTML
searches found no supplementary-information link/section. This is bounded to
the acquired article artifacts, not a claim that no supporting data exist anywhere.
The article's CC BY 4.0 statement was inspected; raw article/figures remain in
`/private/tmp/cmm-round4-phosphorus-cerium-evidence-20261011`, outside Git.
Other authority reuse terms were not separately assessed; only paraphrases,
identifiers and provenance are committed.

### Phosphorus stage

Methods “Solubilization of struvite” describes natural fragments from Veolia
Water Outsourcing, Exeter, pulverization and 105 °C/48 h oven sterilization.
Figure 1 and Results identify a **struvite/dittmarite mixture**. Table 1's
48.782 wt% P2O5 is an XRF oxide expression, not elemental-P percentage or feed
purity; the three reported oxides sum to 75.970%, not a closed composition.

The 200 mL/500 mL flask experiment used 1% w/v feed, 10^6 spores/mL, 25 °C,
125 rpm, darkness and 14 days. MCD medium includes **1 g/L Na2HPO4**; its
pre-autoclave pH 5.5 must not be called measured initial post-feed pH. Endpoint
Pi 51.37 ± 0.59 mM, pH 2.46 ± 0.11 and oxalic acid 26.49 ± 3.43 mM are
Results/Figure 2 values with SEM, at least three replicates. Figure 2's control
is **inoculated struvite-free medium**, even though Methods also names
uninoculated flasks. No acid-matched comparison is presented there.

Full Methods describes oxalic acid HPLC, Ce colorimetry and solid analyses,
but does not specify a Pi determination procedure. Inspection included every
Methods subsection and full-text searches for phosphate/Pi determination;
we do not import an assay from a different paper. These values are source
operational Pi results, without an invented method or detection limit. Background
P, mixed mineral phases and the control limitations prevent adopting the source's
“complete” dissolution wording as a measured mineral-specific fraction.

### Cerium stage

Methods “Biorecovery of Ce phosphate” specifies **cell-free filtrate**, followed
by 0.5 g H-form AG 50W-X8 resin/5 mL for 24 h, pH adjustment to 7.5 with 4 M
NaOH and 0.25 µm filtration. Then 5/20/40/50 mM Ce3+ as CeCl3 was reacted in
10 mL for 24 h at room temperature on a roller. The upstream fungus did not
experience these cerium doses. This is precipitation from a prepared biogenic
leachate, not a live-cell reduction experiment.

Figure 3/Results reports >99% solution removal; the 50 mM arm has residual
Ce 27.34 ± 1.91 µM. The Ce method uses Arsenazo III, 658 nm, with diluted
samples and 0–1 mg/L calibration standards, but no explicit LOD. Apparent
100% removal at lower loadings is not literal zero. Solid mass is washed,
dried precipitate, not pure Ce mass. Figure 6/Table 2 XRD-Rietveld assigns
phosphate hydrate at 20 mM and phosphate plus oxalate at 50 mM; the fitted
100% and 78.3/21.7% phase proportions are not recovery percentages or an
independent purity assay. Figure 9 FTIR corroborates the phase interpretation.
Thermal conversion to CePO4/CeO2 is a separate process and is not curated as
microbial redox. No matched synthetic phosphate/oxalate or untreated-leachate
control for the Ce stage is described in the inspected text. Selectivity among
REEs and industrial waste performance were not tested here.

## Search, contrary evidence and reuse boundaries

Search provider: live web search, 2026-10-11 UTC; first returned sets, no domain,
date or pagination filters unless explicit in query. Exact queries are retained
in the JSON receipt. Local duplicate checks included hidden and ignored files in
`data`, `research`, `reviews` and `history`, plus this task's cited raw directory.
No machine-wide or literature-exhaustion claim is made. Exact DOI/PMC/P ID checks
found no earlier accepted record for this study within that boundary before creation.

Title/DOI correction/retraction searches returned the paper and related/indexed
items, with no affecting notice in the returned sets. This is not an exhaustive
correction registry search. No direct matched replication/refutation was found in
those sets. The paper itself discusses different biomass outcomes in AP1 medium
in [Suyamud et al. 2020](https://doi.org/10.1111/1462-2920.14949). Live primary
indexed text confirms that study's natural/synthetic struvite experiments and
background medium phosphate, but its complete tables, controls, figures and
supplement were not accepted in this pass. Its molybdenum-blue assay cannot be
silently assigned to Kang 2022. Retain it as the first enrichment lead, with
medium-dependent effects and magnesium oxalate formation requiring fresh review.

Other screened leads (indexed evidence only; not accepted): PMC12700948 on
microbial struvite precipitation has feed/control comparability questions;
PMC4025044 contrasts artificial and wastewater media; PMC4968544 concerns
PQQ-dependent glucose dehydrogenase regulation; PMC4510416 and PMC7242446 are
plant/soil contexts; PMC6091953 is pathological urine struvite. None supplies
extra measurements or organism assignments to these records.

## Acceptance and next work

Use the existing bioleaching/biomineralization contracts; mM/percent results stay
qualified prose, not fabricated mg/kg observation cells. No schema/validator
change is demonstrated. Both records receive CREATE sidecars and distinct inline
events before independent review captures their bytes. Validate records, full
corpus, append-only history and structured reviews before publication.

Priorities: (1) independent review of these precise claims; (2) inspect Suyamud
2020 full evidence for a separate conditional P mechanism or magnesium outcome;
(3) seek a defined synthetic-chemistry control and real mixed-REE/waste tests for
the cerium route. Industrial deployment and mineral-specific P mass balance
remain unestablished by this source.
