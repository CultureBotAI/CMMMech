# Xenotime concentrate source investigation

UTC: 2026-10-12T07:43:39Z
Investigator: codex (GPT-6), `/root/round43_hardmetal`
Base: `98e787e8d61593797aef1ed29840b2315a0cc6e5`
Decision: curated, pending independent scientific review.

## Owner and evidence decision

`data/records/xenotime-concentrate.yaml` is a mixed **primary_resource**, not a mineral species, elemental commodity or waste. He et al. (2024), DOI [10.1016/j.chemgeo.2024.122186](https://doi.org/10.1016/j.chemgeo.2024.122186), supplies complete primary methods and outcomes for bacterial mobilization from a xenotime-rich concentrate that also contains monazite, zircon, almandine and ilmenite. No criticality, purified recovery or industrial deployment is inferred. Parent-curated xenotime-(Y) and monazite-(Ce) species identities remain separate; this experiment is owned only by the mixed concentrate record.

The [56-page GFZ postprint](https://gfzpublic.gfz.de/pubman/item/item_5026015_4/component/file_5026048/5026015.pdf) was acquired by the parent and reused with exact hash verification: `8b269c3ef6c76060ea8b73c5e5129978f2272de74e34611b8ebb1fb5f4256ab7`. The newly acquired [16-page original publisher supplement](https://ars.els-cdn.com/content/image/1-s2.0-S0009254124002663-mmc1.pdf) has SHA256 `9c9e72c594a0f136fc7bc299eecaf91054de43d2f17cee12db696536a84863d0`. Its cover title and six authors match the main article; the publisher PII matches Crossref and the public article API. The API response itself contains metadata, not complete article text. The standard candidate PDF URI returned the matching PDF; the DOCX candidate returned404XML and is not treated as a supplement. GFZ says it hosts no public supplementary material, which does not mean the article lacks SI.

## Deduplication and selection

Hidden and ignored files were included, relevant symlinks followed: 3877 text metadata files across the current and original checkout records/research/reviews/history, plus 182 existing referenced raw/research/evidence roots. The exact commands, roots, hits and nine missing historical roots are retained in the paired JSON and external dedup receipt. Search terms cover xenotime concentrate, exact DOI/article PII/title and organism. Existing references are source leads or distinct materials, not an existing owner for this mixed-feed experiment. Only monazite-nd was an exact mineral-name owner match at the snapshot; concurrently created species are separate. Binary PDFs/images/archives were not indiscriminately decoded by text dedup; unrelated machine directories were outside scope. No universal absence claim is made.

## Primary inspection and scientific boundaries

Methods/results/discussion/conclusion text were examined. Every main Figure1–7 and Table1–3 was personally viewed on PDF pages17,19,22,24,25,26,36,55,56. All16supplement pages were personally viewed, including FiguresS1–S7, TablesS1–S8 andTextS1. This is not a claim that all56main pages were visually inspected.

The source identifies the culture as Bacillus thuringiensis from Renju topsoil. The current [NCBI1428](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1428&mode=Info) mapping was checked; no isolate accession or sequence was independently verified. Renju is not assumed to be the concentrate origin. Feed was48–74micrometres;100mLmedium/0.5gfeed in250mLflasks,25–28degreesC,180rpm,30days. Buffered and unbuffered biotic arms each had abiotic-feed and cells-only controls. Matched initial medium is not a matched30daypHtrajectory. Separate96hchemical assays used HCl or individual organic acids and support conditional acid/ligand activity, not each metabolite's causal share in live culture.

MainFigure2 and text support enhanced aqueous REE concentrations, with unbuffered peak about716micrograms/L onday15 and buffered about343micrograms/L onday30; these are not cumulative yield. Figures1/4–6 support acidification, normalized metabolite patterns and condition-dependent organic-acid leaching. Figure7 shows attached cells/material and secondary precipitates with REE/P signals. Section4.3 expressly cannot identify secondary phases by micro-XRD/TEM/Raman; rhabdophane/churchite types remain analogies.

TableS2 phase percentages are particle-count/density estimates. Table3's0.03%xenotime/0.3%monazite dissolved fractions are inferred from two-component aqueous chemistry and assume negligible differential re-sorption/precipitation. TableS7/TextS1 assign the whole-concentrate1.38m2/garea to both phosphates. No phase-specific measured rate or closed material balance is imported.

## Contradictions retained

- Figure5 caption calls the cells-only comparator Exp-Control although its legend/Methods say Exp-Bt; the abiotic feed control is distinct.
- Section2.4prints0.22mmfilters; analyticalSection2.5.1prints0.22micrometres. They are not silently harmonized.
- MainEquation1 calls the material a prepared granite sample despite the concentrate study.
- ActualSI FigureS6 is saturation modeling andFigureS7 composition comparison; the contents list reverses them. ContentsTableS5–S7descriptions also do not match actual captions.
- FigureS1 repeats PDF09-0427 for almandine and ilmenite. Source phase assignments remain qualified, with no fabricated replacement card.
- TableS3xenotimeYb2O3/Lu2O3 versusTableS4elementalYb/Lu fail straightforward conversion. MainTable1TiO2does not close againstTableS2/S3phase estimates; itsP2O3/U2O3labels are uncertain. Whole-feedYis over the XRF upper bound, not below detection. No silent table repair or recalculated purity.
- Section4.1 claimsY-Obondenergies exceedCe-O, whileTableS8numbers order them oppositely. This causal explanation is not accepted into the record.
- MainTable3 uses rounded0.01gmonazite, while0.5g×2.7%=0.0135g. Exact model fractions are not promoted to independently measured mass loss.

## Source status, reproducibility and reuse

The bounded exact-DOI correction/erratum/retraction query returned no applicable notice; this is a first-result-set observation, not an exhaustive negative. Search logs and all downloaded source bytes/render hashes are listed in JSON. [MendeleyData10.17632/pkvvkj4y85.1](https://data.mendeley.com/datasets/pkvvkj4y85/1) is verified landing metadata for version1, published2023-11-13,CCBY4.0. Its individual files were not acquired/reanalyzed; no raw-data statistical reproduction is claimed. The main article/postprint and publisher SI retain their source rights; raw PDFs, images and failed responses stay outsideGit. Nobulkredistribution.

## Frozen curation and validation

Record SHA256: `8e1d30e8c05053055fc352625e894a6575f3ed288c5c702d0aff702cdb9290ea`.
Canonical actual CREATE: `history/records/xenotime-concentrate/2026-10-12T074155Z-codex-66bb20.yaml`, SHA256 `87c774cecb3f231387c6f8dfd604b7c39cd0b5c2bfeb1add3d85b3355cb2b5a1`. Inline timestamp and sidecar are actual current events, not backdated publication dates.
Named validation exited0: `Checked 1 record(s); 0 failed.` The external named receipt records the exact completed tool result. No full cohort gates or independent scientific acceptance are claimed here. No schema/validator/Git/GH changes by this curator.

Remaining work is independent review, shared cohort gates and publication by the parent. Quantitative reuse should separately reconcile archived raw data/source inconsistencies; it is not needed to pretend this bounded mobilization evidence establishes economic recovery.
