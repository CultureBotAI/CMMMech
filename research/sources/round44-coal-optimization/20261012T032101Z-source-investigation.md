# Coal-waste medium-composition source investigation

- UTC: 2026-10-12T03:21:01Z; researcher: Codex /root/round27_packaging, GPT-6, codex.
- Worktree: `/private/tmp/CMMMech-expansion-round44-20261012`; branch `curate/cmm-expansion-round44-20261012`; trusted base `3fc8b873487ed2c1c253ecf131d99e09b8b8d452`.
- Scope: append one qualified 2017 experiment to [coal-beneficiation-waste](../../../data/records/coal-beneficiation-waste.yaml). This is an author research handoff awaiting independent scientific review, not acceptance.
- Working changes owned here: one appended source/mechanism, actual inline EDIT and [canonical EDIT](../../../history/records/coal-beneficiation-waste/2026-10-12T031901Z-codex-477e90.yaml), plus this dossier pair. Existing scalar fields and ordered list prefixes are unchanged; old dossiers, reviews and history remain historical.

## Selection, identity and deduplication

The primary concerns material discarded by gravity/flotation beneficiation of Lviv-Volyn coal at Chervonogradska CPP, stored in dumps for a year. This is the existing secondary-resource owner, not natural coal, combustion ash, elemental Ge or a verified Ge mineral. No mineral, taxon or criticality identifier is asserted. The current assay uses an unresolved native community; introductory genus names and previously reported community densities do not identify the organisms performing this experiment.

Fresh bounded dedup used `rg --no-ignore --hidden --follow` on both this worktree and the original checkout, within `data/records`, `research`, `reviews`, and `history`. Cycle-aware textual reference discovery read 3412 metadata files and searched 159 existing cited raw/research/evidence roots. All three search commands returned 0 without stderr; no metadata read errors. Nine cited roots were unavailable and are enumerated in the JSON/receipt. Text extensions were YAML/JSON/Markdown/TXT/HTML/XML/CSV/TSV; unextracted binary contents and unrelated machine directories were not searched. The normalized DOI was already a round43 frontier lead but was not in a curated mechanism before this edit. The existing owner and its 2012/2016 studies were found. An earlier overly broad exploratory regex yielded irrelevant HTML; it was not used as an absence proof. Detailed commands, roots and matches remain outside Git in `dedup-receipt.json`, `dedup-corpus.txt` and `dedup-raw.txt`.

## Primary identity and actual access

[Blayda, N. Yu. Vasylieva, T. V. Vasylieva and Sliusarenko (2017)](https://doi.org/10.15407/biotech10.04.044), *Biotechnologia Acta* 10(4):44–52, August 2017. Received 17 May is a manuscript date. The four printed authors are used; Crossref has an incomplete/malformed author list including the university as an author. The official [nine-page PDF](https://biotechnology.kiev.ua/images/BTA/2017/4_2017/blayd_4_2017.pdf) and resolved publisher landing were downloaded successfully on 12 October 2026 UTC, with original URL, time, status and checksum in `raw/acquisition2.json`. The initial sandbox DNS failures remain separately in `raw/acquisition1.json`; the successful network-enabled retry is not concealed. The file is a real PDF, SHA256 `c7769514936772bd11cac670db9b2fcbfa6217a5b98dc6d96a6a0acff9b16697`.

All nine original page renders were visually inspected, including Tables 1–7, the sole Figure, conclusions and final bilingual abstracts. Full extracted text was read alongside the graphics. The complete publisher HTML link inventory and PDF identify no separate supplement/data workbook; that bounded observation is not a universal absence claim. Crossref supplies no license or update-to notice. The landing has a licence-policy navigation link but no article-specific licence observed; redistribution rights remain unverified, and bulk full text/graphics stay outside Git. No metadata/index posting date is adopted as a new article edition.

Five web queries and their exact scope are in the paired JSON and `search-log.json`. The notice/supplement and counterevidence searches did not locate a correction or a missing matched-control dataset within their returned first-result sets. Source-internal contradictions are retained rather than silently repaired.

## Experimental contract and original locators

| Item | Direct source evidence and limit |
|---|---|
| Feed | Methods p45: predominantly 5–7 mm particles, Ge 2.60×10^-3 percent, one-year dump storage. Coal up to17 percent and 'organic weight' up to2 percent are source descriptions whose basis is not reconciled. Ge host phase was not measured. |
| Community | Native acidophilic chemolithotrophs. Mesophile/moderate-thermophile densities on p45 are quoted from reference5, not current assay counts. No strain accession or molecular community identification is established. |
| Conditions | p46: stationary cultivation seven days, S:L1:10, pH≤2.0,30±2°C. Working volume, inoculum handling, replicate count and measured pH time course are unspecified. |
| Design | Tables1–2: four factors/four levels in16 combinations, not256 full-factorial runs. A=KH2PO4, B=K2HPO4, C=(NH4)2SO4; D changes both reagent identity and dose among ferrous sulfate, ferric sulfate and thiosulfate. Fixed additives are given separately. |
| Measurement and denominator | Atomic absorption (AAS-1/S-115PK). p46 defines percent transferred into solution relative to the original amount in solid feed. No sampling-corrected closed solid/liquid balance is available. These are not isolated-product yields. |
| Controls/causality | Sole Figure caption names 'control(0)' but does not define a matched sterile or killed-cell arm. Neither actual biomass trajectories nor direct redox/enzyme measurements establish the hypothesized growth phases or mechanism. |

## Quantitative findings and preserved contradictions

1. Tables1–3 map **row10 A3B2C4D3** to KH2PO4 2,K2HPO4 0.5,(NH4)2SO4 5,Na2S2O3 5g/L. Its day4/5/6/7 Ge percentages are **93.50/93.50/80.25/70.00**. The claimed recommended **row5 A2B1C2D3** instead uses1/0/2/5g/L and reports **82.60/62.18/86.87/76.34**. Conclusionp51 explicitly attributes93.5percent in four days to the recommended combination, but no separate confirming dataset reconciles that claim. The record preserves both mappings.
2. Methodsp45 fixed KCl1.0 and NH4Cl0.9g/L differ from the abstract/conclusion recipe KCl0.1 and NH4Cl0.5g/L. MgSO4 remains0.5g/L. Table1 ferrous-salt44.0g/L is distinct from introduction-level older9K44.5g/L; no corrected dose is inferred.
3. The sole Figure plots per-day maxima and means across the16 conditions; its maximum curve can switch condition. It is not a single treatment trajectory or comparison with sterile controls. Later declines are not cumulative extraction. No precipitation/repartitioning explanation is experimentally supplied.
4. Table4 day7 largest Fisher statistic is D8.47 (A0.43), but Table5 day7 gives A73.1percent influence and D4.71percent. Table7 also differs from Table6's chosen day4 levels (its largest A effect is A3, largest C effect C4), while p50 describes A2–A3 as2–3g/L contrary to Table1's1–2g/L. Table7 day6 B1 prints−3.9586. These source anomalies are not silently standardized or statistically reproduced without raw replicates/workbook.
5. Source prose proposes contact/indirect pyrite oxidation and a shift from ferric to thiosulfate importance. Neither a taxonomically assigned catalyst nor actual pyrite phase conversion is demonstrated by these data. The record accepts only community-associated solution-transfer observations with reagent confounding, not exclusive microbial causality or industrial deployment.

## Relationship to retained studies

The2017 reference7 is the existing2016 DOI10.18524/2307-4663.2016.3(35).77956. The studies share authors/locality and feed-family terminology. Reported2017 particle size5–7mm differs from2016's1–3mm, and2017 provides16 combinations and source-defined percentages, whereas2016 graphs concentrations. The earlier2012 endpoint is insufficiently specified. None establishes independent sample batches, a pooled recovery yield or successful replication. The prior mechanisms, sources, inline events and sidecar references were preserved exactly as list prefixes against the trusted base. No new organism identity or inherited criticality was added.

## Curation, checks and handoff

- Record freeze SHA256: `8b501cd41eee90e356096b7680166240e30bc9f918de6c450e156c37be5743b4`.
- New sidecar SHA256: `8a54b1e498a4eaefa575099afcaa4a3b6911e5cb4cd1f1369e39a719fec91f8b`; actor codex/GPT-6/codex, actual UTC event.
- Named command: `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1 uv run --locked cmmmech validate data/records/coal-beneficiation-waste.yaml`; terminal0, **1 checked/0 failed**. Log retained and hashed in JSON.
- Prior scientific fields and list prefixes passed the explicit comparison in `preservation-and-freeze.json`. The baseline is parent reuse of the just-completed fresh published-main gate at this exact unchanged base; this author did not rerun a baseline or a full batch.
- Independent reviewer receives the frozen record, sidecar and original source assets. Parent owns full cohort/review gates and publication. This source handoff does not declare those future gates or review passed.

Priority follow-up is the original raw replicate workbook or author/publisher clarification reconciling recipe, Table3 and statistical outputs, followed by matched abiotic/time-course controls and explicit sample-batch provenance. The observed data support the narrow current extension without claiming those gaps are solved. No additional source lead was expanded during this bounded cohort.
