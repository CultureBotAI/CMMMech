# Coal-mine-drainage treatment solids: primary-source assessment

Investigated at 2026-10-11T14:22:33.131628+00:00 by codex (GPT-6), agent `round24_identity_frontier`, against base `d7183efeb2e528d6d88f0b69da41323642b8fa85` in `/private/tmp/CMMMech-expansion-round24-20261011`. [Machine-readable provenance](round24-amd-solids-sources-20261011.json) and the [bounded discovery report](../sources/round24-amd-solids/20261011T142233Z-source-investigation.md) preserve searches and acquisition limits. The record is [coal-mine-drainage-treatment-solids.yaml](../../data/records/coal-mine-drainage-treatment-solids.yaml). This assessment does not substitute for independent review.

## Identity and source

Vietmeier, Beebe, Flett, Trun and Gulliver, *Minerals* 16(9):930, published 11 September 2026, DOI [10.3390/min16090930](https://doi.org/10.3390/min16090930), investigates real solids accumulated in five Pennsylvania coal-mine-drainage passive remediation systems. Methods 2.1 and Figure 1 establish treatment origin, while Figure 2 documents heterogeneous feeds. The resource is neither natural ore, untreated drainage water, coal ash nor pure Mn/Fe/Al oxide. Different site samples belong to one treatment-origin record. Neither constituent criticality nor economic-reserve status is inherited.

The complete 16-page publisher PDF and its four-page supplement were acquired from the public publisher CDN. All main methods/results/discussion were read; Figures 1–7 and supplementary Figures S1–S2/Tables S1–S2 were visually inspected in local rendered pages. Main HTML and supplement landing routes returned 403 or 429; successful CDN artifacts have file signatures and SHA256 values in the JSON. A ZIP contained exactly one supplementary PDF. CC BY 4.0 is printed in the article. Raw PDFs, page images, full text and web responses stay outside Git.

## Experiment and controls

Methods 2.3 removes coatings from limestone by sterile-water washing, drying at 60 °C for approximately 24–48 h, mortar grinding and 121 °C/30 min autoclaving, then uses 1% w/v prepared solids for 3 d at 30 °C with individual living isolates. The modified medium contains 3 g/L peptone, 2.5 g/L glucose and 0.010 g/L FePO4, recipe pH 7.6 adjusted with NaOH. JR07 and KB7 are author-assigned *B. mycoides* and *B. pseudomycoides*; NCBI species IDs 1405 and 64104 were resolved at their authority. These IDs do not verify experimental strains, and no genome accession is assigned.

Sterile samples for each feed occur in Figure 3/Table S1. The paper does not specify REE-assay working volume, inoculum dose, number of replicates, final pH, oxygen conditions, or filtration/digestion of the decanted ICP supernatant. The 0.2 µm filtration is specified for the separate HPLC assay, not automatically for metal analysis. Likewise the 10% solid / unaerated stationary Mn assay and 10% inoculum / 2 mL SEM wells are separate preparations. The pH approximately 4 statement is attributed to prior Mn experiments and is not a measured pH profile for every REE-feed treatment.

## Outcomes and counterevidence

| Feed | JR07 TREE ppb | KB7 TREE ppb | Sterile TREE ppb | Table S1 rows |
|---|---:|---:|---:|---|
| Glasgow |92.29|36.37|7.27|GJ/GK/GS|
| Scootac |260.42|136.58|3.36|SJ/SK/SS|
| Kentucky Hollow |466.11|400.80|228.08|KJ/KK/KS|
| Sterrett |317.65|302.82|3.97|StJ/StK/StS|
| Wingfield Pines |0.82|4.30|1.59|WJ/WK/WS|

These are reported supernatant totals, not recovery yields. Kentucky Hollow's substantial sterile release must remain visible: the prose's approximately 40-fold statement compares selected other isolates, not sterile control, and K1 is 69.77 ppb whereas K0 is 10.20 ppb. JR07 is below sterile in Wingfield Pines; Kentucky Hollow AV20/AV21 are below sterile. AV22/AV24 rows are missing for Kentucky Hollow/Sterrett/Wingfield Pines, not negative measurements. Table S1 has 29 unique sample rows, 15 individual analyte columns plus TREE, with source-defined BDL tokens. Its caption includes Pm in a 16-element definition but supplies no Pm column; Figure 2 also has no Pm column. Censored cells must not become zero and no unsupplied sum convention is asserted. No statistical significance is assigned to TREE comparisons because its replication/uncertainty is not given.

Discussion says extraction is <1%, but does not show the mass balance. Nominal interpretation of 1% w/v and solid/solution ppm/ppb gives, for example, 466.11 µg/L over 810 mg/kg × 0.01 kg/L ≈ 5.75% gross for Kentucky Hollow, before control subtraction. That conditional calculation is an audit diagnostic, not a replacement measurement: source analytical bases need clarification. The record therefore preserves the conflict without adopting either a verified percentage or a density conversion. Table S1's solution units and unreported analysis dates preclude native exact mg/kg observations; none are imported.

## Mechanism and scale boundaries

Figure 4/HPLC provides elevated lactate for JR07/KB7; Figures 5–6 support staining/surface association. These are correlations. There is no matched-pH abiotic acid series, lactate perturbation, causal gene intervention or phase-specific flux measurement. Gene annotations and Table S2 genome summary cannot prove pathway necessity. SEM-EDS Mn/O co-occurrence cannot establish a particular MnO2 phase. Figure 3 is column-normalized, so comparing its colors across elements as raw concentrations would be wrong. Figure 7 is a proposed schematic, not an additional experiment. No purified REE product, whole-process mass balance, economic demonstration or industrial extraction deployment is established by the laboratory assays or the operational origin of the passive systems.

The separate 10% w/v FAD Mn assay (Methods 2.2,Figure S1) has n = 3 and an overall ANOVA p = 0.03; it is not merged with the 1% REE experiment. Related Research Square preprint DOI 10.21203/rs.3.rs-9065662/v1 was identified but not fully inspected here and is not imported as independent REE replication. The article says additional data are available on request; no author was contacted.

## Search, checks and unresolved evidence

All 156 baseline records were inventoried by name/kind/hash. Bounded `rg --no-ignore --hidden --follow` searches covered `data`,`research`,`reviews`,`history`; no matching AMD-treatment-solid root or study reference was found before writing, including ignored files. Local download searches were restricted to this task directory and the prior referenced source reports, not unrelated home/temp trees. Broader discovery found distinct dust/ash candidates documented in the report. NiMH 2022 was already a deferred DOI in the 20261008 landscape report and was handed to the root author.

Exact DOI/title correction/retraction/erratum searches inspected first returned web sets without pagination, date or domain filters; no matching notice was returned in those sets. Crossmark failed to open. This is bounded checking, not a certificate of no correction. Final pH/replicate/fraction metadata, original uncensored analytical data, deposit accessions, source mass accounting and matched acid controls remain priorities. Named prehistory validation passed (1 record, 0 failed); CREATE history is attached and final named validation also passed; independent review and final batch gates follow separately. No schema or validator change is needed.
