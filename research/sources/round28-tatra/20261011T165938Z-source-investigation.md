# CMM source investigation and curation: Tatra metal-grinding sludge

## Scope and provenance

UTC: 2026-10-11T16:59:38.514285+00:00. Researcher/curator: Codex /root/round27_superalloy (GPT-6).
Worktree: `/private/tmp/CMMMech-expansion-round28-20261011`; branch `curate/cmm-expansion-round28-20261011`; trusted base `9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3`. This timestamped report carries forward the retained outside-Git investigation `20261011T164108Z-source-investigation.json` and records subsequent authorized curation. It does not replace or backdate the original source investigation.

Record: [`data/records/metal-grinding-sludge.yaml`](../../../data/records/metal-grinding-sludge.yaml), SHA-256 `85d1e8e97a505acbe0bc7898ccd9e9de8ead904062d3042d8a766c54af5978cd`. CREATE sidecar: [`history/records/metal-grinding-sludge/2026-10-11T165828Z-codex-72fcb5.yaml`](../../../history/records/metal-grinding-sludge/2026-10-11T165828Z-codex-72fcb5.yaml), SHA-256 `fe054e70f7b2101f411d04c3cb15d59e7d9f5150268b7abb90f21c4cc1d524e6`. A distinct inline CREATE event is also present. Decision: **curated, pending independent native scientific review and final batch gates**.

Baseline: parent-executed `just check` passed 308 tests with 3 skipped, 171 records and 195 histories on the original round28 tree (146.64 seconds). The base was reconciled from `bd93cd5` to merged-main `9f37042` without a tree change; the reconciliation and fresh-main gate receipts are recorded in the paired JSON. No baseline result is presented as final validation of the new record.

Current-base duplicate searches included hidden/ignored files and followed relevant symlinks across this worktree and the original checkout's records/research/reviews/history, referenced round25/26/27 raw directories and the Tatra raw directory. The receipt is `/private/tmp/cmm-round28-tatra-research/raw/20261011T165704Z-current-base-dedup.json`. Matches were prior research and source artifacts, with no accepted grinding-sludge resource found inside these boundaries before creation. Unrelated home/temp trees, Git internals and dependency trees were excluded; this is not machine-wide.

## Search and acquisition

Primary: Fečko and Kučerová, *Bacterial leaching of waste materials at the “Tatra” joint stock company, Kopřivnice*, Mineralia Slovaca 28(5), 1996, pp388–390. [Original publisher issue PDF](https://www.geology.sk/wp-content/uploads/documents/foto/MS/MS-1996-28-5.pdf); [publisher index](https://www.geology.sk/mineralia-slovaca-5-1996/).

Web opening the issue exceeded its renderer's 48.9 MB limit; the publisher index timed out. Initial sandbox URL acquisition failed DNS. A permitted network-enabled download succeeded at 2026-10-11T16:36:08Z: HTTP200, 48,947,857 bytes, PDF1.6, SHA-256 `e8b3a8a85fe28c43ea19edd21d9c72c85ffdf8ebf70769423263155186d5ca1d`. Exact HTTP receipt: `raw/acquisition-network.json`.

The issue contains 158 PDF pages. The article is PDF pages82–84 (zero-based81–83); all three pages, all seven micrographs and all four tables were read and visually inspected. OCR was cross-checked against original pixels. Rendered files `raw/tatra-page-82.png` through `84.png` and corresponding extracted text are retained. Poppler was unavailable; temporary PyMuPDF rendered the pages. The 2012 creation and 2020 modification/HTTP dates describe digitization, not a new scientific edition.

The 1996 imprint on PDF page2 states copyright Geocomplex, a.s., Bratislava. No redistribution license was located in the issue text. Reading access is verified; redistribution is not. Keep the PDF, rendered pages and extracted full text outside Git.

Six exact queries are preserved in the JSON. Search coverage is each first returned result set without pagination or date filters. Exact-title correction/retraction/erratum searches did not surface an affecting notice; this is bounded, not proof of absence. No DOI was verified; cite the original journal URL without inventing one.

## Evidence handoff

| Scope | Original locator | Verified basis |
|---|---|---|
| Resource | pp388–389; Figures1–3 | Sludge from coolant-assisted grinding of metal workpieces, collected from traps. Iron-rich mixed processing waste; separate from coal cinder/slag. |
| Culture | p388 methods | Source-called pure *Thiobacillus ferrooxidans*, Slovak Academy Mining Institute, Košice; no accession. |
| Experiment | p388 | 10g feed +180mL FeSO4-free9K +20mL inoculum; 28d; pH1.8–2.0; 26–30°C; sterilized flasks. |
| Analysis | pp388–390 | ICP elemental analysis; EDAX/RTG characterization; Fe(II) solution series; MPN dilution assay. |
| Outcome | Table1/Figures1–3/Table3 | Changed solid composition/morphology, rising reported Fe(II) and MPN; Fe and Fe3O4 persist. |
| Other feed | Table2/Figures4–7/Table4 | Coal-combustion cinder/slag only; exclude its data from this record. |

The [live NCBI species page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info) explicitly maps the historical name to *Acidithiobacillus ferrooxidans*, NCBITaxon:920. This resolves the species synonym only; it cannot establish a strain, culture purity or mechanism. No external material identifier or criticality designation is proposed.

## Adversarial scientific assessment

The complete article reports no matched abiotic leaching arm and no leaching-flask replication. The five parallel arrays described for MPN must not become five experimental replicates. Sterilization applies explicitly to flasks; waste sterilization is unresolved. Inoculum carry-over, medium details beyond the stated FeSO4 omission, agitation, pH-adjusting reagent and added quantity, sampling losses and analytical uncertainty remain unreported. These prevent isolating a microbial contribution from chemical dissolution.

Do not equate the MPN iron-oxidizing growth readout with direct observation of the leaching mechanism. Do not infer cell attachment, sulfur oxidation, enzymes or strain-specific causality. A rising Fe(II) solution concentration is distinct from total-iron dissolution or an isolated-metal product. The source's proposed benefit from longer incubation or adaptation was not an experimental optimization series.

Original Table1 has incompatible arithmetic if its recovery row is interpreted as simple concentration depletion:

| Element | Before/after content (%) | Printed recovery (%) | Independently calculated concentration depletion (%) |
|---|---|---|---|
| Pb | 0.0082 /0.0013 |98.41 |84.1463 |
| Mn |0.776 /0.663 |13.45 |14.5619 |
| Fe |79.831 /62.320 |18.89 |21.9351 |
| Ni, comparison |0.7773 /0.1290 |83.40 |83.4041 |

This audit uses `100*(before-after)/before`; it diagnoses tension and **does not provide corrected extraction yields**. No residual solid-mass accounting or recovery equation establishes the intended denominator. The original pixels confirm these tokens; they are not OCR substitution. Restrict curation to qualitative observations and explain the inconsistency. Increased relative Ti/Al concentrations likewise do not establish net accumulation. No native concentration observations are proposed: the source lacks analysis dates, uses percent in these tables, and does not justify silently converting the cells.

Figures1–3 document morphology and persistent solid phases; they cannot independently prove microbiological causation. Industrial origin of the feed does not establish an operating bioleaching plant. The companion coal-cinder feed's production tonnage, growth results, phase assignments and leaching outcomes must remain separate.

## Related sources and unresolved questions

The author's institutional bibliography lists a same-year symposium item on Tatra waste under another title. It may overlap this study; without original proceedings it is not an independent experiment. No follow-up request to authors was sent.

A 2002 original paper, [Research of metallurgical wastes as pigments](https://actamont.tuke.sk/pdf/2002/n2/4feckoetal.pdf), was consulted as adjacent context. Its ironmaking sludges differ from grinding sludge; it cannot validate or refute this feed's result. Its full figures were not independently reassessed and no curation is proposed from it in this dossier.

The assigned `metal-grinding-sludge` record now represents this secondary resource and its conditional culture-associated laboratory mechanism. Numerical recovery percentages, criticality and fabricated strain IDs are absent. The source limitations and table tension remain explicit. An independent reviewer must recheck original pages and frozen record claims; unresolved mass-balance/control gaps require additional primary evidence. No schema or validator change is demonstrated.

## Curation verification

The source files retained by the original investigation were rehashed; this curation pass does not claim another PDF download. Full article pages, all seven micrographs and all four tables were previously inspected by this curator against original image pixels. The original imprint was also visually checked. Exact raw file paths, sizes and SHA-256 hashes are in the paired JSON; full text and renders remain outside Git.

The record separates ICP elemental analysis from the paper's separately reported Fe(II) series, whose specific assay method is unresolved. It also preserves the abstract/results difference in best-leached-element examples without adopting a performance ranking. Native concentration cells were not added because dates and a supported source-cell basis are missing. No criticality claim or material identifier was inferred.

Named-file validation completed with terminal exit0: `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate data/records/metal-grinding-sludge.yaml`; one record checked, zero failures. The exact receipt is in the paired JSON. Independent review and final whole-batch/history gates are assigned separately; this source report is not an acceptance verdict.
