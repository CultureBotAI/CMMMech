# Bornite source investigation

UTC: 2026-10-11T19:49:42.368916+00:00. Curator: Codex `/root` (GPT-6). Worktree `/private/tmp/CMMMech-expansion-round32-20261011`, branch `curate/cmm-expansion-round32-20261011`, trusted main base `09c15cbfb7699e40ae4648b6b414784a00b488db`. The [record](../../../data/records/bornite.yaml) and [CREATE history](../../../history/records/bornite/2026-10-11T194734Z-codex-824206.yaml) are working changes; independent scientific review is pending. The [paired JSON](20261011T194942Z-source-investigation.json) pins their exact bytes and every retained local source/receipt/render artifact.

## Scope and existing coverage

Assess bornite mineral identity and defensible microbial extraction/transformation evidence, with no jurisdictional criticality claim and no assumed industrial deployment. The IMA September 2026 list identifies Cu5FeS4 on PDF p29 with status A and notation `1962 s.p.`. Page1 explains the special-procedure notation. It is not a conventional accession such as YYYY-NNN, and no invented mineral CURIE is added. Copper metal, bornite, chalcocite, chalcopyrite, marmatite as Fe-bearing sphalerite, mixed ore and waste are distinct objects.

Ignored/hidden-inclusive, symlink-following `rg` searched `data`, `research`, `reviews`, `.claude`, and the prior reports' referenced `/private/tmp/cmm-expansion-copper-20261011`, `/private/tmp/cmm-round4-mineral-hosts-20261011`, and `/private/tmp/cmm-round2-zinc-20261011`. These bounded searches completed with no inaccessible-path warnings. Nine bornite/marmatite lines concerned prior copper/chalcopyrite context and follow-up leads; the three target study DOIs were absent within these searched text boundaries. This is not a search of unrelated home/temp trees or proof of absence inside every binary artifact. The exact commands and results are in the pinned dedup receipt.

## Search and acquisition

All eight exact search queries and first-result-set limits are in the JSON. Live acquisition receipts record URL, UTC time, actual status/content type, bytes and SHA256. Direct PMC web opens were challenge pages. Direct RSC primary HTML and PDF downloads returned403 HTML; the `.pdf` filename is not a valid PDF and was not analyzed as one. The legacy OA metadata route returned404. Europe PMC returned complete original JATS and a valid ZIP containing all five original figures, the graphical abstract, thumbnails and the two-page original supplement. The publisher PDF was readable via the web tool's cached original but is not represented as a successful local download. Frontiers supplied a valid original 10-page PDF and Europe PMC supplied its JATS. The IMA original244-page PDF and NCBI organism authority were acquired live.

The reader inspected complete primary texts and methods, all five RSC figures, the original supplementary TableS1 and FigureS1, and all six Frontiers figures, including the separate chalcopyrite figure to avoid transferring its outcomes. Frontiers PDF pages3-8 were visually checked for methods and Figures1-6; remaining full text was read through JATS and PDF extraction. The inspected Frontiers article/JATS has no supplementary section or linked supplementary artifact; it offers author-supplied raw data, which were not acquired. Rendering used the existing cached PyMuPDF tool through `uv --with pymupdf`, with no project dependency change.

## Candidate inventory and decisions

| Source | Role / actual access | Decision |
| --- | --- | --- |
| [Zhang2019](https://doi.org/10.1039/C9RA03658J), RSC Advances9,26609-26618 | Original main text, all figures, originalSI; laboratory mechanism | Curate culture-associated leaching of the characterized natural specimen; preserve endpoint/unit conflicts and external pH control. |
| [Publisher correction](https://doi.org/10.1039/C9RA90072A), RSC Advances9,33428 | Full original notice and JATS | Record Hussnain Ahmed Janjua's corrected spelling. No scientific result is revised by this notice. |
| [Bobadilla-Fazzini and Poblete-Castro2021](https://doi.org/10.3389/fmicb.2021.761997) | Complete originalPDF/JATS, all six figures | Curate mixed-specimen biofilm association with apparatus, control, taxonomy and mineral-detection limitations. |
| [Bevilaqua2010](https://doi.org/10.1016/j.procbio.2009.08.013) | Primary abstract/metadata only | Defer full claim curation; important reported absence of A.thiooxidans-alone bornite oxidation requires complete methods. |
| [Phosphate/mixed-ore2019](https://doi.org/10.1016/j.apgeochem.2019.03.003) | Primary abstract/snippets only | Defer distinct bornite-chalcocite ore and pH/phosphate study; do not transfer its denominators or apparent phase-selective behavior. |

## RSC experiment: supported observations and conflicts

Sections2.1-2.3 establish a natural Guangxi museum specimen, powder preparation/UV treatment, source-labelled unaccessioned A.ferrooxidans, basal9K medium, culture pre-growth and washing, 30C/170rpm/14days and sulfuric-acid pH maintenance. Figure1b,d supports greater dissolved copper in inoculated assays than in the abiotic-labelled arms. The source's greater-than90% purity claim uses XRF; supplementary TableS1 is elemental composition, not quantitative phase mineralogy. NCBI Taxonomy/Datasets resolves species920 as Acidithiobacillus ferrooxidans but does not identify or authenticate this stock.

Original Figure1d is material counterevidence to section3.1.1: the text calls final copper extraction greater than90%, whereas curves peak around day12 and end below90% at day14. The record adopts no single final yield, and preserves the unresolved decline instead of treating it as monotonic cumulative recovery. TableS1 raw percent units stay percent prose; they are not converted into schema concentration observations. Slashes in that table are not zeros. Source Figure4c biomass units disagree with discussion cell-per-mL units; the values are not harmonized or used to reconstruct biomass. Figure1f's separate Cu-addition experiment concerns marmatite, not a direct bornite extraction assay.

Figure4 labels mass quantities in grams while the methods call them ratios; total pulp density across mixture arms is not presumed constant. The methods replace sampling losses with water but do not specify cumulative mass correction. Three microscopic counts do not establish three independent leaching flasks or define plotted error bars. The record distinguishes external acid control from measured biological acid production, and pre-growth ferrous medium from a verified assay iron concentration. Iron cycling is a supported interpretation, not an isolated enzyme mechanism. Figure2 tests separate graphite/paraffin electrodes; its weak galvanic-current interpretation is not universal exclusion of interparticle currents. Figures3 andS1 supply residual phase/spectral context without an absolute mineral mass balance. Figure5 is a conceptual heap/AMD diagram, not deployment evidence.

## Frontiers experiment: association and causal limits

The reported natural specimen is optically74.91% bornite but QEMSCAN detects approximately32%, with a large unclassified fraction. The source-labelled Cc and other phases prevent pure-bornite copper accounting. Surface masking/relative abundance cannot establish complete mineral conversion. The specimen was deliberately unsterilized; enrichment and unidentified organisms coexist. FISH targets Acidithiobacillus at genus level, so the record does not turn attached red fluorescence into strain- or species-specific causation.

Figures3-5 support biofilm, iron profiles and solution-copper observations under the two apparatus conditions. The reported54% byday32 versus30% byday48 comparison is a feed-level observation at different times, not an isolated rate effect of biofilm. The wells and flow cells differ in liquid volume, orientation, geometry and flow; initial biomass is per gram of specimen, whose exact masses are not supplied. Methods report0.7g/L Fe(II), but Figure1 labels0.5g/L. Figure3C/its caption ends atday46; prose mentionsday48. Both differences remain explicit. Screening methods mention uninoculated arms, but separate bornite control curves are not shown; nonsterility prevents an assumed sterile comparator. No isolated product or industrial/pilot process is established. Figure6 and the proposed idaite/acid-generation pathway remain interpretations; no selective biofilm/organism removal intervention establishes their necessity.

## Notices, reuse and data fitness

A bounded DOI-specific correction/retraction search found the actual RSC author-name correction and it was read in full. Crossref's original-work response has no update relation even though the separate correction exists; empty metadata therefore was not treated as absence evidence. No additional Frontiers correction/retraction surfaced in the returned exact-DOI search, which is not an exhaustive notice audit. The 2010 A.thiooxidans-alone null and the 2019 phosphate/ore study are concrete contextual leads, not accepted full-method evidence or independent replicas of these studies.

RSC original main/SI indicate CC BY-NC3.0; the correction is CC BY3.0; Frontiers is CC BY4.0; IMA distribution is CC BY-SA3.0. Raw PDFs/XML/images remain outside Git regardless of reading access; maintained reports contain curation, locators and hashes. No bulk reusable quantitative dataset was acquired. The plot percentages, elemental-percent SI and assay outcomes do not fit CMMMech's exact-source-cell mg/kg observation contract, so no synthetic concentration observations or importer are created.

## Handoff, checks and next priorities

Named validation passed for the frozen bornite record (one checked, zero failures). Canonical CREATE history is attached; actual inline provenance is separate. The immediately preceding exact-base fresh-main baseline passed308 tests/3skipped plus184records/210histories/214reviews, recorded in `/private/tmp/cmm-round32-baseline-receipt.json`; that is reused baseline evidence, not a new run. Batch validation and independent scientific review remain the acceptance steps. This report does not self-approve the record.

1. Independently assess the exact record and source conflicts before acceptance.
2. Obtain full2010 primary methods to assess the A.thiooxidans-alone null and stock identity without importing an abstract's numerical claim.
3. Inspect the complete2019 bornite-chalcocite/phosphate experiment, preserving mixed-ore identity and phase contributions; it may support a distinct resource or a carefully bounded mineral extension.
4. Consider complete primary studies for chalcocite, covellite and related copper-mineral interactions after exact experiment/material deduplication. Existing chalcopyrite science is unchanged in this cohort.

The missing raw denominators, conflicting source labels and unavailable external full texts remain named limitations. Neither this first-result-set survey nor the bounded local searches establishes source exhaustion.
