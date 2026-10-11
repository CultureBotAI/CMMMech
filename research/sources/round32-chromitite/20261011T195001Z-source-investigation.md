# Round32 chromitite and chromite-tailings source investigation

UTC: 2026-10-11T19:50:01.104853+00:00. Researcher: codex (GPT-6; codex), the curator, not an independent reviewer.
Worktree: `/private/tmp/CMMMech-expansion-round32-20261011`; branch `curate/cmm-expansion-round32-20261011`; trusted base `09c15cbfb7699e40ae4648b6b414784a00b488db`.

## Scope and decision

Three previously identified DOI leads were assessed. The useful completed change is an extension of [chromite beneficiation tailings](../../../data/records/chromite-beneficiation-tailings.yaml) with a separately scoped fungal treatment experiment. No new chromitite, olivine, serpentine or synthetic-spinel root was created. The source identities were kept distinct from chromium element, ideal chromite and the earlier Odisha tailings. No criticality, schema, validator or industrial-deployment claim was added.

## Candidate inventory

| Candidate | Evidence actually inspected | Decision |
|---|---|---|
| [Acar et al. 2025](https://doi.org/10.1007/s40831-025-01123-1), Journal of Sustainable Metallurgy 11:2527–2540; online 4 June 2025 | Complete 14-page publisher PDF, every original page, Figures 1–8, Tables 1–3, equations and publisher HTML; fresh NCBI 5325 | Qualified existing-resource extension; no verified yield or incremental microbial-effect claim |
| [Schindler et al. 2018](https://doi.org/10.2138/am-2018-6234), American Mineralogist 103(2):271–283 | DOI metadata, issue page, abstract and original public supplemental archive; relevant text excerpts only, XLSX not scientifically reviewed | Natural chromitite remains deferred because full main methods and original figures were not obtained |
| [Hua et al. 2025](https://doi.org/10.1038/s41467-025-57300-z), Nature Communications 16:1975 | Prior complete XML/PDF rehashed; selected identity/methods text, not full new figure/SI assessment | Research-only substituted-spinel and contaminated-soil/water lead; no new material kind invented |

## Search and acquisition

Exact queries, providers, URLs, UTC times, HTTP status, content type, file sizes and SHA-256 values are recorded in the [paired JSON](20261011T195001Z-source-investigation.json) and its six outside-Git acquisition receipts. Searches covered returned web results, official Crossref/OpenAlex metadata, publisher pages, MSA, author institutional pages and NCBI. This was a bounded lead assessment, not an exhaustive literature census. No author contact, subscription purchase or access-control bypass occurred.

Acar's PDF and HTML were obtained from Springer with valid PDF/HTML content. The PDF is CC BY 4.0; full text and all page renders remain outside Git. The inspected publisher PDF/HTML did not link a supplement. NCBI's species mapping is [5325, Trametes versicolor](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5325&mode=Info); this does not authenticate OG2. Exact DOI correction/retraction searches and publisher/Crossref checks found no notice in the bounded inspected results; no universal absence claim is made.

Schindler's Crossref-linked GSW PDF returned 403 with HTML, and Degruyter HTML/PDF endpoints returned empty 202 responses. The MSA main link is explicitly member-gated. An author/institutional search produced bibliographic records but no complete main. The public [AM-18-26234 supplement](https://msaweb.org/MSA/AmMin/TOC/2018/Feb2018_data/AM-18-26234.zip) was acquired and safely unpacked: eight-page A, four-page B and a workbook. These are one study's associated artifacts. Table A3 gives a 100 mg/25 mL one-month comparison; community profiling details also exist. The main method and original figures remain needed before admitting even the abstract's useful null bacterial-enhancement claim.

Hua's main XML/PDF were originally acquired during round30; this round rechecked their hashes and selected text, not a fresh main download. The PDF's prior successful provenance is `acquisition-network.json`, not the earlier failed receipt. Current Crossref acquisition returned 429. Four supplement requests to the recorded springer-cdn host failed DNS, which does not establish absence of the supplements. A PMC page was readable once, then a later lookup encountered reCAPTCHA; no bypass was attempted. The full SI/source-data and figure review remain pending.

## Acar claim-level assessment

The Materials section identifies both feeds as final chromite-enrichment tailings supplied by Eti Krom. Table 1 and Figure 2 characterize different mixed silicate/spinel assemblages. They are neither pure olivine/serpentine nor the 2018 Odisha feed. The new mechanism is limited to observed metal release during inoculated treatment and detected oxalate in one filtrate.

Experimental pages 2528–2530 report source-labelled living OG2, 20 g solids in 1 L, 20°C, initial pH 4.5/5/5.5/6.3 and 3/7 days. The record preserves the 150/200 rpm contradiction, unitless approximately 10^7 spore density, and the 80 mL nutrient aliquot diluted into the final volume. ITS identification and GenBank accessions are mentioned but no actual accession token is printed. No uninoculated leaching control, matched acid control, replicate number, leaching uncertainty or final-pH trajectory is reported; Table 3's control is a separate growth-tolerance experiment.

Figures 5 and 7 label maximum Ni dissolution as 41.82% and 30.97%. Equation 1 divides solution ppm by solid ppm without explicit solid-mass/liquid-volume scaling. These numbers identify the authors' plotted observations only, and are not curated as validated feed-mass extraction fractions. There are no original solution values or complete normalization calculations from which to repair the result. Figures 6/8 selectivity ratios are not product purity. No standardized concentration observations were added: the source does not supply the required assay dates/verified table contract.

Figure 4 labels 9.562 mg/L oxalate in a treated filtrate; the 100-fold dilution's back-correction remains unclear. Citrate, laccase action, metal-organic complexes and ferric/ferrous routes are discussion-level mechanisms here. No leaching-stage Cr(VI) assay supports the toxicity explanation; chromite abundance is not Cr(VI) evidence. Mineralogy and particle size confound cross-feed comparisons. The pictured nickel product and proposed downstream separation do not demonstrate isolated recovery. The full primary, including these limitations, was inspected rather than adopting the abstract's stronger causal assertions.

## Deduplication and provenance boundaries

Hidden and ignored files were included with `rg --no-ignore --hidden --follow` across current and original-checkout records, research, reviews and history. Exact DOI, chromitite and organism terms found prior research leads but no pre-edit record experiment for these DOIs. Existing chromite/chromium/tailings records were inspected separately to establish the owner. Five semantically relevant prior raw roots referenced by repository research were then traversed with symlink following and cycle prevention: 85 text/HTML/XML/JSON/YAML/PDF files inspected, 0 parse failures, 0 symlinks encountered. Raster images and archive binaries were not text-deduplicated; unrelated home/temp trees were not scanned. This is a declared relevant-source boundary, not machine-wide novelty.

The two pre-existing mechanism values, all prior sources, inline history and history references are unchanged. Only the description's case scope, two sources, one mechanism, one EDIT sidecar and one inline event were added. Record SHA-256: `487513f57385d5f1631967c708e59e43523e6cc4a8f554cf780c6c46334e1a78`. [New EDIT history](../../../history/records/chromite-beneficiation-tailings/2026-10-11T194722Z-codex-669074.yaml) SHA-256: `e2d1417648ade202c5890bfb1a4b8ea03ebeb3861de69e7a600d1baa7d03f761`.

## Validation and handoff

Named-file validation exited 0: 1 record checked, 0 failed. Explicit history validation against the trusted base exited 0: 214 histories, 0 errors at that invocation. `git diff --check` passed for the changed record. The exact-tree baseline was reused via `/private/tmp/cmm-round32-baseline-receipt.json`; no new full batch is claimed here. Parent will run final cohort checks and save an independent scientific review of final bytes.

1. Review the frozen fungal extension against all primary pages and complete the final batch gates.
2. Obtain lawful complete Schindler main text before a natural-rock mechanism record; inspect bacterial preparation, matched controls and every main figure together with the acquired supplement.
3. Resolve Acar's percentage normalization and OG2 accession from original evidence; retain existing uncertainty until then.
4. Complete Hua's SI, original figures and source-data review, including non-endmember phase identity and abiotic comparisons. Its 100 mL bottle and 50 mL on-site tube procedures do not establish industrial deployment. Choose an existing material owner or a defensible identity before curation.

This report is source investigation and curator assessment, not independent acceptance review. Raw files remain at `/private/tmp/cmm-round32-chromitite-research` and the expressly identified round30 reuse paths; their checksums and provenance are in the paired JSON.
