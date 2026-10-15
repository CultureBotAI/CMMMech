# CMM source investigation: hydroboracite

UTC: 2026-10-15T22:15:06.821880Z. Researcher: codex (GPT-6), `/root/round104_borates`.
Worktree: `/private/tmp/CMMMech-expansion-round104-20261015`; branch `curate/cmm-expansion-round104-20261015`;
trusted base `6b6ccf160a457ceb5ebc265b55bbc5d515964707`.
This is the record author's source investigation; independent scientific acceptance is pending.

## Scope, selection and deduplication

Hydroboracite fills a distinct natural borate-species gap with accessible natural-crystal identity and two different abiotic laboratory transformations. Neither boron criticality nor microbial activity is transferred to the mineral. The September 2026 IMA row on PDF page 97 gives `CaMg[B3O4(OH)3]2(H2O)3`, grandfathered G and original-description year 1834. The latter is not an approval identifier. IMA pages 1–2 establish the column semantics and CC BY-SA 3.0 distribution terms.

The hidden/ignored/followed search recorded in the [paired JSON](20261015T221506Z-source-investigation.json) covered maintained worktree records, research, reviews, history and local skills, original-main ignored publication reports, five cited raw-source roots and the prior issue snapshot. It found 166 contextual matches and no existing hydroboracite owner. Binary PDFs were not exhaustively indexed; unrelated home/temp paths and issue comments were excluded. The current 277-issue all-state title/body inventory had no hydroboracite/DOI matches. Its hash and the exact search bounds are retained in JSON; no global absence claim is made.

## Search and access

Eight exact web queries on 2026-10-15 are saved in JSON. They combine hydroboracite with the primary titles/authors, microbial terms, correction, erratum and retraction. Searches covered returned results only, without exhaustive pagination. Fresh publisher and Crossref metadata and four supplementary downloads were already acquired in this round and were re-inspected here. Crossref lists seven authors and publication on 2026-02-25; its relation object is empty and `update-to` is absent. No relevant correction or retraction was acquired; that bounded result does not prove absence.

The three full historical/recent PDFs and IMA list were reused from round 103, with source URLs, original acquisition timestamps, reuse checksums and this round's fresh-download receipts distinguished in JSON. The 2026 institutional manuscript is named `hydroboracite_08-01-2026-unmarked.pdf`: 33 PDF pages including supplementary tables and references. The publisher HTML provides metadata, abstract, references and supplements, but its body is subscription-limited; the publisher version-of-record PDF was not acquired. Raw sources remain in `/private/tmp/cmm-round104-borates-research` and are not committed.

## Evidence assessment

| Source | Inspected evidence | Accepted scope and limitations |
|---|---|---|
| [Sabelli and Stoppioni (1978)](https://www.rruff.net/doclib/cm/vol16/CM16_75.pdf) | Complete six-page paper, Tables 1–8, Figures 1–3, all six rendered pages | Natural Bigadiç crystal, P2/c and Z=2. Hydrogen positions were geometrically assigned after diffuse residual peaks and were not refined. The cited CISTI structure-factor deposit was not acquired. |
| [Demircioğlu (1973)](https://dergipark.org.tr/tr/download/article-file/44391) | Complete 26-page English PDF, Tables 1–3, Graphs 1–12 and Photos 1–23, with visual checks of scanned tables and plates | Laboratory heating of the Table 1 column 8 natural feed, not a pure hydroboracite standard. No isolated boron recovery claim. |
| [Comboni et al. (2026)](https://doi.org/10.1007/s00269-026-01339-x) | Complete institutional manuscript text and rendered pages, especially Table 1 on pp. 10–11, Figures 2–6 and supplementary pp. 20–30 | Two separate natural crystals in helium diamond-anvil cells; measured pressure brackets retained separately. High-pressure structure unsolved, recovery of starting crystal unsuccessful, hydrogen positions omitted. |
| Same 2026 study's four deposits | Three complete CIFs and DOCX tables/embedded Figure S1 inspected, cell contents recomputed | Same experiment, not independent replications. CIFs are starting-phase refinements; Z/density metadata inconsistent with atom-site contents. |

### Thermal experiment and mixed feed

The tested material from Büyük Günevi mine, Yolbaşı, Bigadiç contains 46.39% B2O3 and 4.46% SiO2 (Table 1 column 8). The 100, 150 and 200 °C samples were heated in ovens; settings 250–600 °C were applied overnight in furnaces. Atmosphere, heating ramp, exact overnight hours and replicate uncertainties are missing. The authors report unchanged structure at 100/150 °C, weakening peaks from 200 °C and decomposition of the starting phase by 400 °C. Some peaks remain in higher-temperature mixed-feed patterns without quantitative assignment; those peaks cannot be assigned wholesale to intrinsic hydroboracite behavior.

Table 3 reports water losses of 22.37%, 24.46% and 25.26% at 400, 500 and 600 °C. These endpoints differ from the qualitative diffraction endpoint. The prose claims all crystal water is lost at 500 °C despite the continuing listed increase. Neither gas-specific speciation nor a phase/water mass balance resolves that discrepancy. Higher residual B2O3 percentages are not isolated recovery yields. The concluding 1.5–2-fold solubility statement lacks assay conditions and is not adopted as an experimental recovery result.

The current MTA journal landing page identifies volume 80/1973; the acquired English PDF is printed pp. 104–117 with photographic plates. MTA and Dergipark metadata have differing page ranges. The 2026 article's citation year 2023 for this source is not treated as a new experiment. The original 1978 bibliography confirms the 1973 date. Historical hardness 5–6 for the mixed nodular material is also not generalized to the pure species.

### Pressure arms and unresolved structure

The 2026 study uses two approximately 20 × 5 × 4 µm natural Bigadiç crystals supplied by the Sorbonne museum, in separate membrane-driven cells at ESRF ID15B with helium, ruby calibration ±0.05 GPa and room temperature (293 K in CIFs). No complete chemical assay was possible. Structural agreement with ideal composition cannot replace chemistry.

Table 1 brackets starting-phase/high-pressure-phase observations at 14.40(5)–14.72(5) GPa in the first arm and 14.08(5)–14.51(5) GPa in the second. Their maxima are 15.18(5) and 15.45(5) GPa. These are sampled brackets, not equilibrium thresholds. The abstract uses 14.51–14.72; Results use 14.40–14.51; Conclusions use 14.40–14.50 and 14.45 ±0.2 GPa. The reported 0.9(6)% volume comparison combines the first arm's 14.40-GPa point with the second arm's 14.51-GPa point, so it is not a paired change in one crystal.

Diffraction deteriorated severely after transition, preventing a solved high-pressure structure or confident space-group assignment; triclinic symmetry was not excluded. The starting crystalline state was not recovered on decompression. Hydrogen-bond deformation is an interpretation of non-hydrogen geometry, not direct H tracking. The paper's broader shielding-concrete suggestions are not concrete performance or deployment experiments.

The three official CIFs match first-arm cell metrics at 0.32, 14.40 and 7.35 GPa in file order. Each has 14 non-hydrogen atom rows. Multiplicity × occupancy independently recomputes Ca2Mg2B12O34; the formula field contains one formula unit and `_cell_formula_units_Z` is 1. This discrepancy makes the calculated density fields unsuitable for adoption without source correction. Hydrogen site rows are absent, despite a template hydrogen-treatment field. These CIFs do not describe hydroboracite-II. DOCX Tables S1/S2 and Figure S1 describe model geometry and equation-of-state behavior; they provide no concentration observations in the schema's mg/kg contract.

## Handoff, checks and remaining work

The authored owner is [hydroboracite.yaml](../../../data/records/hydroboracite.yaml), SHA-256 `db1e645ae3e36e7b9a77826fa9a6b1542f9a7603406dabef9cafac97d552b5a9`. Its canonical CREATE sidecar is [2026-10-15T221240Z-codex-885932.yaml](../../../history/records/hydroboracite/2026-10-15T221240Z-codex-885932.yaml). Inline history is distinct. The pre-change baseline completed with exit 0 before curation authorization. Single-file validation completed with **1 record checked, 0 failed**. No schema or validator change is needed. Batch gates and independent review are still separate requirements.

1. Independently review the final owner and history bytes against primary sources.
2. Track a source clarification for the pressure brackets, cross-arm volume comparison and CIF Z/density metadata. Require a corrected original source/deposit or unambiguous original per-crystal data before narrowing uncertainty. The current record already preserves these limits; no external source correction is claimed.
3. Investigate **inderborite** next: [Comboni et al. (2024), DOI 10.1180/mgm.2024.29](https://doi.org/10.1180/mgm.2024.29) has accessible publisher HTML and two listed supplementary files. Full PDF/supplement/IMA/chemistry checks and full identity dedup remain. An exact-ID search including hidden/ignored/followed files found no data/records owner for inderborite, inderite, meyerhofferite, kurnakovite, probertite or tunellite; this is a lead check, not completed scientific assessment.

A [boron-tolerant soil-isolate study](https://pubmed.ncbi.nlm.nih.gov/23686918/) was assessed only through metadata/abstract. It does not establish a hydroboracite-specific microbial transformation, and none is curated. A broad patent mineral enumeration is likewise not experimental evidence. The cited 2010 thermal book chapter remains an unacquired lead. No claim is made that the CMM frontier is exhausted.

IMA explicitly supplies CC BY-SA 3.0 terms. Open redistribution rights for the other full texts and deposits were not established. Only original summaries/provenance are committed; bulk source files, extracted tables and renders remain outside Git.
