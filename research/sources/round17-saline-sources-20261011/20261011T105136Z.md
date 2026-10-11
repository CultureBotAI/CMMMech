# Saline process-feed source assessment, round 17

## Scope and provenance

- UTC: 2026-10-11T10:51:36Z; curator codex (GPT-6; codex), /root/round17_saline.
- Worktree `/private/tmp/CMMMech-expansion-round17-20261011`, branch `curate/cmm-expansion-round17-20261011`, trusted base `4504ab1c5a005ea31e65318c3b3f206d6fbf44ed`.
- Followed the round16 produced-water handoff: Hu2021 main-text gap, heavy-oil produced water and Soc1 reverse-osmosis brine. Broadened the RO-feed search to primary government experiments when publisher main texts remained unavailable.
- New maintained target `data/records/reverse-osmosis-concentrate.yaml`; actual CREATE sidecar `history/records/reverse-osmosis-concentrate/2026-10-11T105020Z-codex-b323dc.yaml`. Existing oil-and-gas-produced-water and geothermal-brine records were read and left unchanged. No schema, criticality-list, governance or existing scientific record change.

## Selection and inspected evidence

The accepted candidate is **reverse osmosis concentrate**, a secondary resource defined by its production process. It is not a new name for natural geological brine, oilfield production water, a dissolved element or gypsum. The experiment below tests laboratory-generated concentrate from river water; neither its composition nor its response defines all RO feeds.

The strongest complete source is Scarim, Bernardino-McCloud and Arias-Paic, *Biological and Ion Exchange Mining of Reverse Osmosis Concentrate: Enhancing Water and Mineral Extraction from a Salinity Impaired Surface Water*, USBR report ST-2024-20092, [public PDF](https://data.usbr.gov/rise/content-rise-public/rise/catalog-item/binary/S%26T%20Final%20Report%2020092%20Signed.pdf). The 54-page file includes the accepted manuscript and supplements corresponding to [DOI 10.1061/JOEEDU.EEENG-8371](https://doi.org/10.1061/JOEEDU.EEENG-8371). These are one experiment, not independent replications. The PDF cover and signatures say December2025, its documentation page says 7November2025, the RISE item publication date is 7November2025 and last-update date 29January2026. The journal was online25October2025 and in the January2026 issue; these dates are not interchangeable editions.

Read the complete text, AppendixA methods/results and incorporated SI. Rendered and inspected PDF pages42-45,50-53 for Table2, Figures1/3-6/S2-S3 and TablesS3-S4; no pixel-derived measurements were manufactured. Further main figures were text-screened. Important locators:

- Sections2.1-2.4 and Table2: river collection27March2024, UF plus laboratory RO at85% water recovery,3mg/L proprietary antiscalant in feed,22-23April2024 tests. Three-liter concentrate batches received filtered activated-sludge solids from100mL Boulder mixed liquor and325mg/L glycerin. Eighteen-hour mixed/aerated treatment n3, stagnant control n2, mixed/aerated control n1; both controls lack seed and glycerin. Reported temperature and pH trajectories are in TableS3.
- Section2.7: aqueous samples filtered0.45micrometer before analyses. Sludge origin and activity are explicit but no taxon-specific causal claim is supported. FigureS2 includes a community in the unseeded control, so it is not an abiotic comparison.
- Sections3.2.1/3.2.4 and Figures3-5: more solids and lower filtered calcium/sulfate in the amended treatment. The accepted record preserves source-reported41%/10% reductions and12%/5% control calcium reductions; neither is a pure-product yield. Total phosphorus reduction is an antiscalant surrogate, not a direct carbon-phosphorus cleavage assay.
- Sections3.2.1-3.2.3: no glycerin-only, killed-biomass or matched-pH control; carbonic-acid stripping, endogenous organisms and sorption remain alternatives. C-P cleavage and causal genes remain hypotheses. An additional orthophosphate-richer drainage concentrate reportedly precipitated poorly, with data not shown.
- Sections3.2.4-3.2.6: SEM/EDS elemental co-location and thermodynamic modeling suggest gypsum/calcite, but authors explicitly require additional solids analysis. The64% gypsum estimate assumes its formula. No new gypsum species record is justified from this phase evidence alone.
- Figure1 and Sections2.6/3.3: million-liter normalization and proposed downstream water recoveries are not experiments at that volume. Cation exchange is separate and nonmicrobial; co-elution prevents high-purity products. TableS4 identifies modeled and assumed-conserved columns and ND values; none were converted to zero or mg/kg observations.
- Preserved conflicts: Section3.3 uranium0.422mg/L versus TableS4 0.444mg/L; no uranium removal efficiency accepted. Section2.7 sequencing batch2 versus FigureS2 batch1; no precise batch-level community claim. FigureS3 caption has a gypsum water-stoichiometry typo; phase confirmation remains unresolved.

## Deferred literature and new leads

| Source | Evidence acquired | Disposition |
|---|---|---|
| Arias etal2026, DOI10.1016/j.jwpe.2026.110282, PII S2214714426008408 | Crossref metadata, indexed publisher abstract/introduction,5-page SI PDF | Main methods/results unavailable; do not add Soc1 mechanism. SI verifies free-cell versus immobilized-cell phase assignments but not complete assay controls. |
| Lei etal2025, DOI10.1016/j.jhazmat.2025.140317, PII S0304389425032376 | Publisher metadata-only XML, institutional abstract, valid37-page-equivalent DOCX SI text | Main PDF link exists at Delft under Taverne access but returned403; no PW mechanism accepted. |
| Hu etal2021, DOI10.1016/j.watres.2020.116753 | Rechecked publisher403 and author university citation page; earlier SI and round16 dossier remain available | Full main evidence gap persists; existing identity-only PW record is unchanged. |

Arias SI FiguresS2/S3 distinguish free-cell+growth-medium assays from immobilized-cell assays. Its TableS1 assigns numerous minor phases and predominant hydromagnesite; mineral names are not accepted as independently confirmed recoverable products. The indexed abstract attributes struvite to phosphate carry-over rather than raw brine. TableS2 gives draft-genome accession JBUQDG01, not independently resolved this pass. Neither that genome nor strain-level causality is curated.

Lei SI TextS2 establishes3.14L sequencing-batch reactors, not industrial microbial deployment. TextS6 states PICRUSt inference from16S data, which must not be recast as directly measured gene regulation. TableS3 and other SI were text-screened; not every SI image rendered, and fullmain is still required. Its references reveal PW follow-up DOI10.1016/j.watres.2025.123252 and RO-concentrate Zobellella study DOI10.1016/j.envres.2023.117484. These remain unverified leads, not records.

Additional report references to pursue: microbial scaling DOI10.1016/j.watres.2020.115863 (possible mechanistic alternative, mainnotacquired); algal ROC nutrient/hardness study DOI10.1016/j.watres.2016.02.062; Gao2025 diatom-based RO treatment (resolve full bibliographicidentity). They would normally extend the existing new RO root rather than duplicate it.

## Acquisition, search and reuse

Raw root `/private/tmp/cmm-round17-saline-raw`. PairedJSON records exact requests, UTC acquisition times, HTTP states, paths, byte counts and SHA256. Key complete source hash: USBR PDF `73b4679610dc9a3ef02be4efedd686ecf45fa603f9bdf7f96733e0eabc0a7ec2`. Arias SI `4f70a258eec16fdf4de2d1e5965cefec5f8b65f8717bb630ef72be1741378d5d`; Lei SI `50f1ea611146fa0c11aa0a00920a4fe82d790c98b672ee2214cc33388f6c735a`.

The initial shell requests failed DNS in the restricted environment; successful metadata/SI/report retrieval followed authorized network access. Failed PDF requests contain HTML, and Lei's200 XML contains only coremetadata, not a fullpaper. The Arias guessed DOCX404 preceded successful PDF SI acquisition. Publisher main access was not bypassed; no author contact, payment or library-account operation occurred. Raw copyrighted files are outsideGit. USBR report is government-authored public research with explicit agency disclaimer, not an endorsement. Publisher redistribution rights are unverified; Taverne availability does not imply a general reuse license. Only curation, provenance and review material are committed.

Live searches used the exact21 queries in pairedJSON on2026-10-11, firstreturned result sets only, no exhaustive pagination. Correction/retraction searches yielded no relevant notices in those returned sets. Crossref Arias metadata has no `update-to` and an empty relation; this is bounded negative evidence, not proof of no future or unindexed correction. The USBR report itself supplies contrary and limiting evidence above.

Deduplication used `rg --no-ignore --hidden --follow` over the complete worktree excluding only `.git` and `.venv`, plus named prior raw roots `/private/tmp/cmm-round16-produced-water-raw`, `/private/tmp/cmm-round15-brine-raw` and this raw root. No ignore filters were used for file contents in the final search; binary matches were supplemented by extracted PDF/DOCX text. The pre-change records had no reverse-osmosis root under these bounds, while research already contained the deferred saline leads. The previous original checkout and unrelated temp/home trees were not searched, so no machine-wide novelty claim is made.

## Handoff and validation

The named record validator completed exit0: `Checked 1 record(s); 0 failed.` Final initial record SHA256 `19cad077f7e6536be6cb051af5fdfb3f0d6fe6c72d40cccbe3c3e18b51b1fe73`. Independent scientific review and parent whole-batch/history/review checks follow; this source assessment is not that review. Parent baseline passed308 tests with3 skips,128 records and144 histories before authoring.

Priority1: independently review the complete source and final record bytes. Priority2: acquire the legitimate Delft fullpaper then evaluate extension of the existing produced-water record, particularly inferred-versus-observed microbial functions. Priority3: acquire Soc1 mainmethods before adding its brine mechanism; reconcile SI minor phases and phosphate carry-over. Priority4: inspect the linked USBR data inventory and report references for additional ROC mechanisms and source-defined quantities. Priority5: continue the named Hu2021 evidence gap without inventing an unchanged record edit. The source landscape remains open; this bounded pass does not establish exhaustion.
