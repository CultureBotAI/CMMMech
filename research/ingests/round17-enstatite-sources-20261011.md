# Round 17 enstatite and olivine sources

Prepared 2026-10-11T10:51:51.904235+00:00 by codex / GPT-6 / codex (`/root/round17_enstatite`). Trusted base `4504ab1c5a005ea31e65318c3b3f206d6fbf44ed`; branch `curate/cmm-expansion-round17-20261011`. This dossier records authorship and source assessment; independent acceptance reviews are separate.

## Selection and identity

[Klug et al. (2026)](https://doi.org/10.1038/s41598-026-63817-0) offers paired cell-containing and cell-free bioleaching experiments with explicit feed characterization. New records capture **enstatite** as a mineral species and **olivine** as a mineral group. They do not duplicate the existing forsterite endmember or glushinskite product identity, and two records do not make two independent studies. No criticality designation is inherited from magnesium or nickel.

The freshly acquired [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), visually checked PDF p63, gives enstatite Mg2Si2O6 with status A and a 1988 special procedure. That year is not a unique approval ID. The [CNMNC-hosted compendium](https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf) is the Melbourne 2018 compilation, copyright 2019; its Whitney and Evans table at PDF p35 marks olivine GROUP and defines that label. Pages 10/16 discuss the forsterite-fayalite series. No guessed mineral CURIE or complete group-membership list is asserted.

Fresh NCBI taxonomy XML verifies [442](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=442&mode=Info) as *Gluconobacter oxydans*, species only. An initial 621 probe returned *Shigella boydii* and was rejected before authoring; the raw receipt is retained. The experimental B58 delta-pstS, P112:mgdh genotype is specified by the primary Methods, not inferred from species taxonomy.

## Primary evidence inspected

Article full XML, Methods, Discussion, Figures 2/3/6 and all seven sheets of supplementary XLSX were inspected. The DOCX text and embedded figures were extracted. Main diffraction/time-course/mass-allocation figures, supplemental S3/S4 TIFFs and IMA rows were viewed. DOCX embedded EMF rendering initially failed because local ImageMagick was incompatible; native QuickLook produced inspectable PDF images for **Table S1, Raman Figure S1 and feed Figure S2**, all subsequently rendered and viewed. Thus no visual-access gap remains for these selected supplemental objects. The manuscript's SI title differs from the final article title and its contents list mentions S1-S2 while it actually also contains S3-S4; it remains the publisher-linked supplement of this study.

The bulk feed is 69 wt% olivine / 31 wt% enstatite, while the selected hand-separated powder is 100% olivine by XRD. Table S1's assumed 90.68% Fo commercial composition comes from earlier measurements, not this exact batch. Phase purity is not chemical endmember purity. There is **no pure-enstatite experiment**.

All flasks originated from a single colony/culture, with technical triplicates per arm/day. Following two-day growth and two-day glucose biolixiviant preparation, 0.5 g of approximately 40 µm powder was exposed to 10 mL liquid at 30 C without mixing for 0/5/10/15 days. The direct and 0.2 µm-filtered biolixiviant arms are separate. Controls contained 20% glucose and mineral, without cells/biolixiviant or pH adjustment. Treated initial pH about 2.4-2.5 differs sharply from control pH about 8.7; trajectories diverge further. No matched chemistry or wild-type mineral-leaching comparison isolates a genotype or physical-contact cause.

ICP-MS measured centrifuged, frozen/thawed, 0.45 µm-filtered liquid diluted 10,000-fold. Source blank corrections are about 1043 ppm Mg and 3.2 ppm Ni. The data workbook's mass-balance sheet defines ppm as mg/L; values remain contextual prose, never native mg/kg observations or presumed isolated yields. Row 6 of ICP-MS data supports final Mg means for the exact arms cited in the records. Figure 2 and source tables show controls release small amounts; cell-free biolixiviant also works.

**Enstatite counterpoint:** Figure 6c/d and Mg mass-balance worksheet rows 16/19/23/26 allocate about 26% of total initial Mg to enstatite at day 0; day 15 values are about 13% with cells and 10% without cells. Therefore larger total mixed-feed release in direct cultures cannot demonstrate better enstatite-specific dissolution. Those phase allocations rely on assumed compositions and XRD/ICP-MS; they are not measured phase-specific fluxes. Residue-phase shares are likewise not yields from original feed.

**Olivine denominator conflict:** Figure 6a and Discussion allocate 64% of initial Mg to solution plus 11% to secondary oxalate, explaining roughly 75% liberated from olivine. The Abstract instead labels 11% as a fraction of leached Mg. Records retain the conflict and do not call 75% dissolved Mg or a product yield. Fe oxidation is inferred largely from color, with proposed ROS/siderophore chemistry; no enzyme cause is accepted. Oxalic acid was detected in one mutant sample and was not quantified. Carbon likely comes from glucose; net atmospheric capture, durability and industrial deployment are unestablished.

## Dataset and source reuse

[Zenodo 10.5281/zenodo.15658356](https://zenodo.org/records/15658356), version 1 published 13 June 2025, is the same experiment's XRD deposit, not an independent replication. API metadata lists 28 files, 14 BRML / 14 XLSX, with CC BY 4.0. One sampled bulk-direct-day-15 XLSX contains 2828 numeric rows/two columns spanning approximately 5.0001-60.0071 in the angle-like column; its columns have no headers in the inspected sheet. The landing-page filename convention identifies BULK/DIRECT/DAY15. No independent phase refinement was performed or claimed. The complete downloadable supplementary workbook supports condition/replicate/day cells but is not imported wholesale; source measurement dates needed for native concentration cells are unestablished.

Raw files remain `/private/tmp/cmm-round17-enstatite-raw`. The paired JSON preserves exact acquisition URLs, UTC times, HTTP/media outcomes and SHA256 hashes, plus extracted/rendered artifact hashes. Original publisher page and direct PMC supplement links challenged access; EuropePMC supplied valid XML, ZIP, XLSX and DOCX. Article XML states CC BY 4.0; IMA master is CC BY-SA 3.0 and the compendium reserves rights. No raw article or data binary is committed.

## Search coverage, limits and handoff

The paired JSON contains exact queries and bounded first-result/unpaginated coverage. Two separate exact-DOI correction/retraction queries surfaced no affecting notice; this is a bounded negative result, not exhaustive proof. Adjacent primary literature returned different organisms/feeds/controls; it does not directly refute these particular assays. Hidden/ignored-inclusive, symlink-following searches covered data/research/reviews plus named retained round 15 mineral and round 16 silicate directories. Existing Klug frontier, forsterite and glushinskite were checked before creation. No new-root absence claim extends beyond that corpus boundary.

Root confirmed baseline terminal success before record writes: 308 passed, 3 skipped, 128 records, 144 histories. Individual record checks passed as recorded in JSON. CREATE histories describe actual work and use GPT-6 / codex; no schema change was needed. Independent final-hash reviews and final corpus/history/review checks are root-coordinated.

- [enstatite](../../data/records/enstatite.yaml), CREATE `history/records/enstatite/2026-10-11T105143Z-codex-e2c308.yaml`, SHA256 `94b7451a26318dfb63100b86b88ac692ec4a577db8ca77edd797b1cba9a8c36e`.
- [olivine-group](../../data/records/olivine-group.yaml), CREATE `history/records/olivine-group/2026-10-11T105148Z-codex-b09182.yaml`, SHA256 `2db3527893e6449e4c99491853a28132952a313a6c7f20462560f22dccbcf3e3`.

## Further priorities

1. [Bio-accelerated weathering of ultramafic minerals with Gluconobacter oxydans](https://doi.org/10.1038/s41598-025-99655-9): Primary publisher text opened; dunite resource and varied controls need full assay/supplement review. Assess a distinct dunite primary-resource root only after authoritative rock identity and exact feed evidence; keep any mineral species inference separate.
2. [Bacterial use of siderophores increases olivine dissolution rates by nearly an order of magnitude](https://doi.org/10.7185/geochemlet.2315): Primary journal full-text results and linked SI lead surfaced; complete SI not yet acquired. Potential extension of olivine-group: MR-1 deletion mutant, killed control and dose-matched DFOB comparisons; no new duplicate root.
3. [Engineered bacterial siderophore production accelerates rock weathering for carbon removal](https://doi.org/10.1038/s41587-026-03288-w): Primary journal result surfaced; not a full assay review. Coordinate with biotite agent, who owns this forward lead for frontier; assess Alteromonas macleodii assay/scale before adding mechanism.
4. [Bioleaching of ultramafic tailings by Acidithiobacillus spp. for CO2 sequestration](https://doi.org/10.1021/es900986n): Reference DOI resolved; publisher HTTP 403. Acquire full primary methods and characterized tailings provenance; do not infer actual feed or microbial recovery from title.

The next leads remain open. This is bounded progress, not global exhaustion of CMM identities or sources.
