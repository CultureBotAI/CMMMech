# Round87 source investigation: secondary aluminium dross

## Scope and provenance

UTC: 2026-10-15T03:52:25.879093+00:00. Researcher: codex /root/round68_new_frontier (GPT-6). Working base `9deef8843b7efcf2dd2586c2a13f47b72231e336`, branch `curate/cmm-expansion-round87-20261015`. This bounded search prioritized a distinct industrial residue with complete primary evidence. The selected feed is secondary aluminium dross after previous metallic-Al recovery, not all aluminium dross, a mineral species, elemental aluminium, bauxite residue, spent potlining, or unspecified smelting slag. No criticality claim or microbial mechanism is inferred. The accepted experiment is laboratory chemical extraction.

Deduplication included hidden and ignored files and followed relevant symlinks in `data/records`, `history`, `research`, and `reviews`, then the existing downloaded roots cited by relevant earlier reports (rounds25/27/60/72/77/83/86 and the bounded inventory of their references). The raw `dedup.json` enumerates those roots and actual errors; this is not an entire-machine absence claim. Binary PDFs were not searched as if they were text; relevant extracted text and original documents were inspected separately. The material query and a companion literal DOI query are preserved. The initial regex escaped DOI fragments too strongly, so its DOI portion is not used for novelty; `exact-doi-dedup.json` records the corrected literal query. No accepted Lv study or equivalent post-metal-recovery feed owner was found in these bounded maintained/current issue searches. Existing aluminium and spent-potlining owners are conceptually distinct. An existing pharmaceutical-blister-packaging-waste record excludes that search hit.

## Search and acquisition log

The companion JSON reproduces all14 exact queries from `search-log.json`, actual URLs, UTC acquisition times, HTTP results, byte counts and SHA256 values from `acquisition.json`. Searches used first returned web result sets, not an exhaustive literature review. Main queries covered aluminium/aluminum dross bioleaching, Aspergillus, gallium smelting slag, petroleum coke and exact DOI/title supplement/correction searches.

The MDPI landing route returned429, but the publisher's own `mdpi-res.com` original PDF returned200. The correct PMC9414100 full XML and Crossref DOI response also returned200. A guessed incorrect PMC9414625 was rejected as evidence. No authentication bypass or author contact occurred. The accepted complete original has16pages, Figures1–11 and Tables1–4; every page was rendered and visually inspected. The full XML has no supplementary-material node, and the original has no separate SI section. This is a bounded inspection result, not a claim that no external data could exist. Article data availability says not applicable.

## Candidate inventory

| Candidate | Original identifier | Evidence acquired and inspected | Decision |
|---|---|---|---|
| Secondary aluminium dross | Lv et al.2022, DOI10.3390/ma15165686, PMC9414100 | Publisher original16-page PDF, complete JATS, all figures/tables and metadata | Ready for narrowly qualified abiotic record; independent native review remains required |
| Gallium-rich aluminium-smelting slag | Wang et al.2018, DOI10.1016/j.hydromet.2018.03.009 | Publisher abstract/introduction/section excerpts and Crossref metadata only | Defer direct bioleaching claims until complete original methods/results/graphics; do not equate its feed with secondary dross |
| Pharmaceutical blister packaging | Shukla et al.2024, DOI10.1016/j.seppur.2024.127760 | Legitimate Aalto original acquired for material identity verification; full graphical review not undertaken | Duplicate existing resource identity; not a dross study despite contextual search hit |
| Petroleum coke | Tripathi et al.2019, DOI10.1016/j.fuel.2018.08.072 | Prior round86 documented restricted Greenwich item23905; no newly accessible complete route established | Retain known source gap; unchanged restricted endpoint not retried |
| GaAs production hydroxide sludge | DOI10.3389/fmicb.2026.1807986 | Existing record and prior source documentation | Duplicate; not newly curated |

## Accepted original and claim-level assessment

Han Lv, Mingzhuang Xie, Zegang Wu, Lili Li, Runjie Yang, Jinshan Han, Fengqin Liu and Hongliang Zhao (2022), *Effective Extraction of the Al Element from Secondary Aluminum Dross Using a Combined Dry Pressing and Alkaline Roasting Process*, Materials15(16):5686. Published18August2022. DOI10.3390/ma15165686. Initial research shorthand calling it Li2022 was corrected before record creation; title page and Crossref establish Lv as first author. Original version and PMC mirror represent the same experiment, not independent replication.

- **Feed identity:** Introductionp1 distinguishes primary dross and the residual secondary material after metallic-Al recovery by screening or flux-assisted remelting. Section2.1, Figure2 and Table1pp3–4 describe a real Guangxi aluminium-remelting-plant specimen. Mixed metal Al, Al oxides/nitride, Mg–Al spinel and process salts are not a pure phase. Bulk38.23wt.%Al is total elementalAl, not metallic-Al content. The exact plant/sample lot is unspecified. Source use of totalN to estimate AlN does not establish independently measured phase fraction.
- **Laboratory process:** Section2.2p4 describes100g dross/alkali mixtures pressed at30MPa into20mm-diameter,40mm-long cylinders; corundum crucibles, air furnace,10°C/min,1h hold, desiccator cooling,200mesh crushing, caustic leaching, filtration and repeated boiling-water rinsing. No biological arm was used.
- **Recipe conflict:** The abstract and Section3.5/Table4p13 specify1150°C roasting, carbonate/alumina molar ratio1.3, then90°C leaching for30min at10mL/g. Table2p6 uses1100°C and60min for its carbonate-ratio series. These can represent different arms and are not flattened into one universal recipe. The60g/L caustic condition is expressed as C(Na2O), with alpha_k=3.0 and an incomplete preparation recipe; it is not silently relabelled60g/LNaOH.
- **Outcome denominator:** Section3.2.1/Figure5d and Section3.5/Table4 report90.79%Al and92.03%Na. Section2.3 Equations1–2p5 use Mg-normalized clinker/residue composition changes, with incomplete printed brackets. A conserved solidMg tracer is assumed, and no independently closed original-feed/solution/wash/loss/product mass balance is supplied. Added carbonate/caustic contributesNa. These percentages are not isolated metal/alumina yields or original-waste overall recovery.
- **Phase and causal limits:** Figures6–7pp8–9 support source-assigned sodium aluminate in clinkers and residual MgO/spinel/aluminosilicate phases. They do not quantify conversion or prove purity. Figure8p10 indicates time/temperature and liquid-to-solid effects; its L/Sseries is at60°C. NaOH gave slightly higher selected extraction but was rejected for moisture uptake, AlN hydrolysis/ammonia and collapse of pressed cylinders. Untreated-dross matched leaching controls, independent replicate counts and error bars are not reported. No quantitative ammonia comparison is adopted.
- **Graphical reporting conflicts:** Figure5caption swaps panelsb/c relative to actual plotted axes/alkali labels. Figure7caption says mass ratios while plot/text use molar n(N/A). The method's10–60°XRD range differs from Figure2's90° extent. Figure10TG annotations and prose also differ (1.43vs1.24%); that measurement is not curated. No corrected graph or invented harmonized dataset is supplied.
- **Interpretations and exclusions:** Figures8–9 kinetics and9.69kJ/mol activation energy remain model dependent. Table4 N/Cl concentration decreases after reagent addition do not close total mass or gas balances; the source alternates chlorate/chloride terminology despite chloride-ion assay. Complete detoxification, purified condensate and harmless-gas proof are excluded. Figure1's alumina endpoint is proposed; Conclusionspp14–15 leave desilication/crystal-seed decomposition for future work. No isolated alumina or industrial deployment is asserted.

## Source terms, identifiers and reusability

The publisher original is CC BY4.0; copyright-bearing full text and figures remain external despite the open licence. The maintained dossier stores original analysis and provenance, not copied article text. DOI/title/author/date are verified with the full original, JATS and Crossref. This heterogeneous waste has no asserted mineral/taxon authority ID; no organism was used. No source concentration table is imported into quantitative observations, because these wt.% and recovery estimates do not fit the current exact mg/kg concentration-cell contract.

Exact DOI correction/retraction searches and retrieved Crossref metadata (empty relation, no update-to) did not identify a formal notice within inspected results. This bounded negative finding does not establish worldwide absence. No separate dataset, machine-readable raw assay table or versioned supplement was identified. PDF/XML versions are bound by their bytes and acquisition time, not by a guessed update date.

## Priorities and handoff

1. Add the narrow secondary-aluminium-dross owner only after the actual root baseline succeeds, canonical CREATE history and named validation, then obtain independent review. Raw source paths, hashes and precise locators are in the paired JSON; author/curator acceptance does not replace that review.
2. Preserve a concrete source clarification follow-up for Lv's arm mapping, caustic recipe, magnesium tracer balance and true product yield. Draft `/private/tmp/cmm-round87-dross-source-issue.md` is external for parent dedup/posting; unresolved source questions are not corrected by rewriting numbers.
3. Pursue Wang2018 only via a new legitimate complete-original route. Its Ga-rich smelting-slag feed and microbial conditions need independent assessment before any new owner or update.

## Limits

This is one complete laboratory experiment, not comparative proof of optimal processing, industrial adoption or microbial activity. Searches are bounded and raw references include historical derived search logs; irrelevant nested hits do not count as independent evidence. Source acquisition, rendering and curator inspection are complete for adopted claims. Record validation and independent scientific review will be reported only after actual completion; publication/runtime gates are parent-owned.

## Curation handoff

The actual baseline passed before maintained writes; its receipt and log digest were verified. Named command `uv run --locked cmmmech validate data/records/secondary-aluminium-dross.yaml --require-records` completed with1record and0failures. Canonical CREATE and a distinct inline event are attached. Independent scientific review and whole-batch gates remain pending.

- Owner: `data/records/secondary-aluminium-dross.yaml`, SHA256 `7b93f8a63f5a8f39ba2e14b08ee020a50918a7343342aadd92d6f0527c15b4f8`.
- CREATE: `history/records/secondary-aluminium-dross/2026-10-15T035130Z-codex-1557d9.yaml`, SHA256 `9c6ebd6f472f2d0641e7b9aa12f0023c34da4f95ae963724297948ad0fd18773`.
- Full accepted original: `/private/tmp/cmm-round87-resources-research/lv2022.pdf`, SHA256 `868d2a28e26beddd8fa5c761f454108f2d325c575b976854fcf528657b20ff93`; all16 original pages and all Figures1–11/Tables1–4 were inspected.
