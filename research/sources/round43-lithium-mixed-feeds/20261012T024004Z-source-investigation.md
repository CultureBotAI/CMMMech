# Lithium-mica mixed-feed source investigation

UTC: 2026-10-12T02:40:04.268774+00:00

Curator: codex (GPT-6; codex). Worktree: `/private/tmp/CMMMech-expansion-round43-20261012`. Trusted base: `59e24ec38d9c7b377dcfeade1637b298aab9623e`. This dossier is a source assessment and curation handoff, not an independent scientific approval.

## Decision and material ownership

Created `data/records/lithium-mica-ore.yaml` as a **primary_resource**. The accepted experiment is Sedlakova-Kadukova et al.2020, DOI [10.1038/s41598-020-71596-5](https://doi.org/10.1038/s41598-020-71596-5): a crushed natural Beauvoir ore, with source-assigned polylithionite, muscovite and kaolinite in original FigureS2A. This is a mixed-feed resource, not a pure mica species, commodity or processing waste. Existing polylithionite/petalite records remain unchanged. No inherited criticality or industrial use is asserted.

Rieder et al.1998, DOI [10.1346/CCMN.1998.0460513](https://doi.org/10.1346/CCMN.1998.0460513), Table4 printed589, treats lepidolite as a series on/near the trilithionite–polylithionite join. The retained original table was re-inspected. Neither series terminology nor FigureS2's non-ideal reference formulas establish a pure endmember or quantitative phase fraction.

## Acquired and inspected primary evidence

- Complete **8-page2020 publisherPDF**, all original pages, Figures1–4, Table1 and equations1–3: `/private/tmp/cmm-round43-lithium-mixed-feeds-research/raw/2020-main.pdf`, SHA-256 `c8cea97c21912c51c9754de3d559f09275c2102612d74e4661688698700d85d2`.
- Complete **5-page original supplement**, FiguresS1 andS2A–D, acquired through EuropePMC's legitimate supplementaryFiles archive: `/private/tmp/cmm-round43-lithium-mixed-feeds-research/raw/2020-supplement-archive/41598_2020_71596_MOESM1_ESM.pdf`, SHA-256 `158b375df557fb4cef4807f28fd943834bfdcb62b7c6305d388e69dd10f23eea`. All five pages visually inspected; source declares five pages/two figures.
- Original renders: `raw/2020-main-pages/page-01.png` through `page-08.png`, and `raw/2020-si-pages/page-01.png` through `page-05.png`. The archive also retains all four original main JPGs and equation images.
- Fresh Crossref identity/notice relation and four NCBI species responses:920 *Acidithiobacillus ferrooxidans*,930 *A.thiooxidans*,5061 *Aspergillus niger*,5537 *Rhodotorula mucilaginosa*. Names/IDs are species-rank only; experimental strains remain source-reported.
- Prior complete2020/2025XML and mica-nomenclature artifacts are retained byte-identically with a separate reuse receipt; no fresh acquisition is claimed for these copies. Main2020PDF states CCBY4.0. No raw copyrighted pages or bulk artifacts are committed.

## Scientifically supported arms

**Acidophile consortium:** SmolnikLC/SmolnikF culture, two-month ore adaptation,10g/L feed, duplicate250mLflasks with190mLmedium+10mLinoculum,30°C static. Poor medium used sulfuric acid and5g/L sulfur; ore addition followed acidification to pH1.5. Rich iron/sulfur nutrient medium showed the reported null. Figures1/4 report11mg/L liquidLi and8.8% total feedLi extraction in poor medium after approximately336days, not an isolated product. Uninoculated no-Li statements lack an analytical detection limit; controls were not held at the culture's pH history. Individual microbial roles and exclusive proton causation are unproven. Figure2's fitted transformed ordinate has an unexplained approximately0.667 starting offset; no fitted pathway or400-fold-rate claim is adopted.

**Fungus:** An-S, reportedISB1674,2gfeed/200mLmedium+5mLeight-day conidialculture,21°C static, initialpH5.1, paired uninoculated duplicates. Reported0.2% feedLi extraction and77% of extractedLi in harvested biomass remain distinct denominators. S1 shows hyphal association; S2C includes a quartz reference. Acid identity, mechanical contribution, intracellular localization and de novo quartz formation are not established. Ashing/HCl digestion of washed biomass does not exclude sorption or fine mineral carryover.

**Yeast:** CCY20-1-36, five-day preculture,10g/Lfeed, initialpH5.1,21°C, rich/poor media. Reported1.1% total feedLi extraction and92% of extractedLi in biomass are not interchangeable percentages. Centrifuged/ashed/digested biomass is an operational fraction, not proof of intracellular uptake. Source methods say both160rpm and static. Different organisms were assayed under different media, temperatures, agitation and durations; no intrinsic organism-performance ranking is inferred.

## Contradictions and unresolved analytical boundaries

1. Table1 gives3.79%Li2O while Methods gives1.21% elementalLi byAAS. Stoichiometric conversion gives approximately1.76%Li from3.79%Li2O. The discrepancy is unresolved, so reported extraction percentages are author values, not independently reconciled mass balances.
2. Bacterial Methods lists day366 while Results/Figure1B indicate336; fungal and yeast sampling schedules also differ from simplified approximately40-day comparisons. No invented common endpoint is selected.
3. Yeast Figure3 rises at its final point while prose ends nearpH3.5. No exact finalpH is chosen.
4. S2 uses unequal count scales, no quantitative mineralogy or matched uninoculated-residue XRD, non-ideal formulas and two polylithionite-labelled references in panelD. Peak or reference-pattern changes are not complete phase disappearance, pure species identification or mineral-specific yield.
5. Organic-acid species, intracellularLi, selective recovery and industrial performance are unmeasured. The suggested fungal/yeast-then-bacterial sequence and biomass-to-product stage are proposals.
6. Precursor2014/2015 studies cited by2020 may share material/strains; overlap was not fully reconstructed. These three arms are one published study, not three independent replications.

## Second source and counterevidence boundary

Li et al.2025, DOI [10.3390/microorganisms13020415](https://doi.org/10.3390/microorganisms13020415), remains **source-only deferred**. Its completeXML describes a different supplier feed with lepidolite/albite/quartz and a Dabaoshan community, mechanical activation and optional pyrite. Current mainPDF returned403; the EuropePMC archive stream was incomplete. No full original2025 graphics orSI review is claimed. Needed next: all12 originalfigures,6supplementaryfigures,3tables, especiallyTableS1 and the distinction between aqueousLi and laterHCl-extractableLi. The sterile controls omit pyrite, limiting attribution in the pyrite-amended group. Its Introduction describes2020 bacterial8.8% as41-day, conflicting with the actual2020 primary336-day report; that derivative duration is not propagated.

Kirk et al.2024, DOI10.3389/fmicb.2024.1467408, is an already-known conditional lithium-leaching study represented in existing records. The present searches reidentified its contrasting unlike-feed/control context; no new unreviewed Kirk measurement is imported into this record. The2020 assay is not generalized to all lithium micas.

## Deduplication, searches and acquisition limits

The precreation scan included hidden/ignored files and relevant followed symlinks in both current and original-main `data/records`, `research`, `reviews`, `history`, plus **13** existing raw roots cited by matching documents. It found 474 corpus-hit lines and 4414 raw-text-hit lines; all commands completed without search errors. Earlier round42 discovery of theseDOIs is explicit known-source handoff, not novelty. No maintained Beauvoir/2020 experiment owner was found within that boundary. Twelve missing referenced paths and text-only binary limits are logged; this is not machine-wide absence. The postcreation owner search now finds this new record.

Search queries, returned results and timing are retained in `web-notice-search.json`. Bounded exactDOI/title correction/retraction queries and fresh Crossref records did not surface an affecting notice; neither empty relationships nor the returned search sets prove global absence. NatureHTML redirected in the web reader; NaturePDF succeeded. Publisher figure guesses returned404 and the older staticSI host failed DNS. These unchanged failures were not repeatedly retried; EuropePMC supplied the complete2020 archive. Sandbox DNS errors are recorded separately from network-enabled attempts.

## Curation handoff and checks

Record SHA-256: `5fefc582ad08ec87d3f37fde1c7b3faf26a096adc86492006302e41da8d1c808`.

CREATE: `history/records/lithium-mica-ore/2026-10-12T023720Z-codex-9e7491.yaml`, SHA-256 `136f3aaa105a9ce80427a6895c43124198ee4a038b7622498c7b32210f12cb90`. Inline event is distinct, actualUTC/codex/GPT-6/codex. Named validation exited0: **1record checked,0failed**; its exact terminal tool output is transcribed in `frozen.json` rather than represented as a separately captured stdout file.

The companionJSON inventories **57** retained artifact/receipt hashes and exact source/inspection/claim boundaries. Independent native review and final corpus/history/review gates belong to separate reviewers/coordinator and are not claimed completed here. Next priority is independent acceptance of this exact narrow record, then complete2025 evidence acquisition and source-assay clarification.
