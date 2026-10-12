# Enargite-pyrite concentrate source investigation

UTC: 2026-10-12T11:18:12.739286Z

Author: Codex /root/round27_packaging; GPT-6; codex. Worktree `/private/tmp/CMMMech-expansion-round55-20261012`, trusted base `19d0972767b266f86a256a3f36f0f7177ab4cf25`. This is an author investigation and handoff, not an independent scientific review.

## Decision and identity

Curated [enargite-pyrite-concentrate.yaml](../../../data/records/enargite-pyrite-concentrate.yaml) as `primary_resource`, with [CREATE history](../../../history/records/enargite-pyrite-concentrate/2026-10-12T111529Z-codex-1c9c39.yaml). It denotes the characterized concentrated geological feed. The source describes “dirty” flotation wastes generally and three high-As concentrates specifically, but does not establish a discarded stockpile or spent-material history for these supplied specimens. No pure-mineral ID, constituent criticality, industrial operation or isolated product claim is inherited.

Figure 1 assigns enargite/pyrite at 51.8/34.6,37.4/47.3 and26.1/63.1 wt% in DC-I/II/III. Figures2/S2 independently show source-assigned enargite and pyrite diffraction, with tennantite inDCIII; this does not quantify phase purity. Table1 reports Cu27.3±0.5/20.4±0.9/14.7±0.2 wt%, As8.5±0.2/6.6±0.4/4.7±0.1 wt% and D50 57.7/62.8/81.2µm. Minor Cu-bearing phases prevent a mineral-specific copper yield. Suppliers are Sumitomo forI/III and JXNippon forII; exact mine/batch/flotation provenance is unresolved.

## Acquisition and personally inspected originals

- [Okibe et al.2022](https://doi.org/10.3390/min12040449): fresh official CDN PDF/XML, 11pages, all6figures/2tables, complete declared ZIP and2-pageS1/S2. Every main/SI page and original graphic was visually inspected. A high-resolution Figure3c crop retained the disputed endpoint labels.
- [Oyama et al.2021](https://doi.org/10.3390/min11040432): fresh official CDN PDF/XML, all13pages/6figures and3-pageSI containing S1–S4 visually inspected. Used for comparison and experiment dedup only.
- [NCBI28034](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=28034&mode=Info): current official browser opened and HTML retained; species name and DSM9293/AT-1 aliases verified. This one reported community member is not the whole consortium or proof of its causal role. Other source-labelled members remain prose without invented accession mappings.

Initial MDPI landing requests returned429, while official CDN downloads succeeded with matching article titles/DOIs. The CDN endpoints were constructed from verified article numbers; SI basenames were observed in complete XML. Both version-notes pages remained inaccessible. Exact URLs, acquisition times, file types and hashes are in acquisition1–3 receipts. Both main articles state CC BY4.0; raw articles, XML, ZIPs, extracted SI, page renders and authorityHTML remain outsideGit. No third-party mirror was needed for accepted evidence. No unavailable source is described as fully read.

## Assays, controls and quantitative bases

Methods2.1–2.3: each as-received unwashed/nonsterile concentrate, 20%w/v solids in200mL ABS medium/500mL duplicateflasks; initialmedium pH1.5 withH2SO4,0.01%yeast extract,10%v/v pre-grown mixture,45°C/150rpm,60days. Six introduced acidophiles are explicitly named in record context. Repeated adaptation on each nonsterile feed allows different final communities; no time-resolved community assay is provided. ACShirasagiDO-5D50=10.9µm;0,.025,.05,.1% doses described but only0/.05% plotted. No complete dose matrix or source-data workbook is supplied; dataavailability says notapplicable.

| Feed | Cu% withoutAC | Cu% with0.05%AC | Interpretation |
|---|---:|---:|---|
| DC-I |35|29|Carbon reduced the measured endpoint.|
| DC-II |25|29|Modest increase; inoculum-free endpoints14/15%, respectively.|
| DC-III |22|27|Increase accompanied by elevatedEh and more dissolvedAs.|

Figure3 caption defines day60 dissolved-metal amounts relative to each feed's corresponding total-element inventory. These percentages are not isolated-product yields. S1 controls are inoculum-free, not sterile, and onlyDCII; control pH/Eh evolve differently. No causal fraction for individual cells, carbon detoxification, or a mineral-ratio optimum is isolated. Comparisons among feeds confound composition/particle size/unmeasured reagent carryover. Higher solids loading remains a laboratory feasibility test.

ICP-OES measures total-element solutions, not As(III)/As(V). Figure4 reuses the same solution trajectories; it is not a new experiment. Figure5 examinesDCI/noAC, Figure6DCII/.05%AC, Table2DCIII/noAC after60days. Original residues containAs/Fe/O/Cu/S secondary material; S2 does not identify a crystallineAs precipitate. Tentative ferric/cupricarsenate/basicferricsulfate/sulfur mixture remains a proposal. No pure scorodite, closed arsenic balance, complete metallurgical recovery or long-term stability was established.

## Contradictions and boundary decisions

1. DCII/noAC arsenic: §3.2.2 says5.0%; Figure3c redAs label is6.6%, with5.0% printed for greenFe. Both retained; no numerical harmonization.
2. The abstract's lowestAs wording forDCI/noAC is not adopted as an all-arm ranking: §3.2.1 andFigure3a give6.5%noAC versus1.0%withAC forDCI.
3. §3.3 uses spot12 for both brightenargite andgel-like secondary material, whereasTable2 labels12enargite and11secondaryprecipitates. No spot-specific formula adopted.
4. Initialmedium pH1.5 differs from plotted initial suspensionpH near2.4 in some arms; trajectories rather than continuouspH1.5 assumed. Methods print0.45mm digestion membrane and(NH4)SO4; neither silently repaired nor used as a validated reproducible recipe.
5. §3.2.3 describesDCIII Eh risingto700mV, conclusion says>700mV, andFigure3f approaches700. Record keeps directional response, not an exact universal threshold claim. Speculative growth inhibition/detoxification and galvanic explanations are qualified.

## Deduplication and prior experiment relationships

Before record creation, `rg --hidden --no-ignore --follow` searched current and original records/research/reviews/history, then203 existing cited cmm research/raw/evidence roots, including current downloads. Metadata/text and available extracted fulltext were searched without size cap; unextracted binary figures/archives were not semantically searched. Unrelated home/temp directories were excluded. Eight genuinely unavailable directory candidates and13 file-stem false candidates are distinguished in dedup-assessment.json; the full roots and errors are retained. No machine-wide absence is claimed.

Corpus hits were the round54 discovery handoff and unrelated round46 bibliographic boundary. Exact-DOI olderrawhits are references in Kondo2024 and its metadata/dedup output. Existing tennantite-concentrate has different60%tennantite mixedfeed and5%pulp experiments, not these2022DCfeeds. No accepted duplicate owner was found within the stated search scope.

2021D3/Eb/Ea have distinctly differentMLA compositions,1%pulp, fourintroducedmembers, externalFe/S and feed-specific acid adjustment. Their greater/variable endpoints are not pooled with2022 or treated as replication. The2021introduction cites2020feed37.4%enargite/47.3%pyrite, matching2022DCII nominalcomposition; batchidentity and reuse need primary2020comparison, not an assumption of independentnewmaterial. The2022Figure1 source-suppliedMLA itself may reflect recurring material characterization rather than an independentexperiment.

## Search, notice limits and next work

Exact DOI correction/erratum/retraction queries, a carbon/inhibition/control counterevidence query and NCBI query were run with first-result-set coverage, no pagination. No affecting notice surfaced; inaccessible publishernotes prevent a categorical all-version clearance. Complete2021 comparison provides contrastingcarbon responses under differentconditions rather than a universal refutation.

New primary lead [Oyama andOkibe2025, DOI10.1016/j.jece.2025.116581](https://doi.org/10.1016/j.jece.2025.116581) is openly indexed and contrasts carbon activation/graphiticity. Its complete methods/originalgraphics/SI were not acquired in this boundedbatch; no abstract measurements are accepted. Next acquire those and compare actualfeed/control/batch overlap. [2020author manuscript candidate](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/4737402/4737402.pdf) likewise remains a named future acquisition route, not fully assessed evidence. Source-providedraw curves, matching controls forDCI/III and long-termAs stability would improve interpretation.

## Validation and handoff

Named record validation completed exit0,1checked/0failed. The parent's exact-base baseline reuse is disclosed; this lane did not rerun globalchecks. CanonicalCREATE and distinctinlineevent record actual work. No existingrecord/schema/sharedpage changes. Independent scientific review and parentfinalgates remain required.

FinalrecordSHA256 `95d205d0feb7212875387fa5ddba9e88f32765eb8e1c502926eb681643f35c1a`; CREATEhistorySHA256 `f89113fd34cbe69078597cb98070375a30acd79edf3e674a126711b8bf1d6233`. PairedJSON pins 45 rawartifacts and 13 receipts, with acquisitiontimes/locators in the boundreceipts. Source originals are under `/private/tmp/cmm-round55-enargite-research/raw`.
