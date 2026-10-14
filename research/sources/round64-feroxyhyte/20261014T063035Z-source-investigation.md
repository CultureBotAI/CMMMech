# Feroxyhyte primary-source investigation and curation handoff

UTC: 2026-10-14T06:30:35.905931+00:00. Curator: codex (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round64-20261014`, branch `curate/cmm-expansion-round64-20261014`, trusted base `0f4d8ff9e4919714e3dd902dc3573e95922a65fb`. Separate curator assessment; independent scientific review is pending.

## Selection and ownership

Created `data/records/feroxyhyte.yaml` from a complete primary laboratory experiment and dated mineral authority. This adds a distinct iron oxyhydroxide species, not an iron-element or mixed-product duplicate. A hidden/ignored-inclusive `rg --no-ignore --hidden -L` scan of maintained data/research/reviews/history and the relevant round 64 iron, round 63 arsenate and magnesium raw caches returned only general IMA and the new primary-paper mentions before creation. Exact queries, paths and postcreation matches are retained. Binary content without extraction and unrelated directories are outside the absence claim. Related iron mineral records remain separate owners; reuse of the 2021 citation would not create an independent replication.

## Primary evidence inspected

[O'Loughlin et al. (2021)](https://doi.org/10.3390/min11020149), *Minerals* 11(2):149, publisher 43-page PDF, published 31 January 2021. The iron curator acquired it at 06:22:20 UTC; this researcher independently read its relevant original methods, results, discussion and references, and rendered and inspected original Figures 22–24 and Tables 4–5. PDF `/private/tmp/cmm-round64-iron-research/oloughlin2021.pdf`, SHA256 `9da3ec0eebfa8b05a9aec4398fa45a80748c9f212b153f6010a695a2d6cdb062`. Page 1 and fresh Crossref state CC BY 4.0. The companion JSON inventories retained material and authority files and actual hashes; original PDFs and images remain outside Git.

Sections 2.1–2.3 establish synthesized, washed, dried and sieved feroxyhyte; duplicate 100 mL suspensions in 160 mL bottles; 80 mM Fe(III), 75 mM formate; initial pH 7.5; argon, 30°C, darkness and roller-drum incubation; and a printed inoculum of 5 × 10^9 cells/mL. AQDS is 100 µM where present; both phosphate arms (500 µM and 5 mM) also contain AQDS. Full inherited basal-medium and inoculum recipes were not reconstructed. Fe(II) is one-week acid-extractable suspension Fe, not a dissolved-metal yield. Figure 23 includes an actual sterile-control diffraction trace, which retains feroxyhyte. The record preserves that matched sterile kinetic series and full control amendment/time information are not supplied alongside these results.

## Supported outcome and adversarial limits

Without phosphate, Table 4 gives 24.28 ± 2.10 mM Fe(II) without AQDS and 24.51 ± 6.02 mM with AQDS at day 78, about 30% of initial Fe. The narrative's essentially-complete-by-day-11 statement describes the plateau/transformation and cannot establish 100% Fe(III) reduction. AQDS increases the fitted initial rate, while Section 4.2 reports no significant endpoint gain for feroxyhyte. This null result is retained.

With 500 µM or 5 mM phosphate, endpoints are 55.07 ± 2.92 and 59.93 ± 1.65 mM at day 156, a different duration. Figure 23 itself labels 78 and 156 days, matching Table 4, but the caption prints 46 days. The record retains the conflict without manufacturing a common harvest date. The lower-phosphate and phosphate-free solids are assigned magnetite/chukanovite; high-phosphate solids are assigned green rust/vivianite. Figure 24 SEM morphology is not phase proof. Table 4 explicitly qualifies high-phosphate SEM green rust as “GR?” and gives no Mössbauer result for that arm. Table 5 selected fits support mixed phases, with relative spectral areas rather than mass recovery fractions. No original XRD nondetection is turned into an exact whole-feed conversion percentage. Morphology suggests reconstruction; no gene or tracer test establishes a unique electron-transfer or dissolution pathway. No product isolation, natural-ore performance or industrial deployment is demonstrated.

## Identity and provenance conflicts

[IMA-CNMNC September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), original pages 1 and 68, confirms Feroxyhyte, Fe3+O(OH), approved 1975-032. Its approval number is not an original-description year. The experiment's synthetic delta-prime FeOOH is kept distinct from natural ore.

[NCBI 319224](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=319224) matches *Shewanella putrefaciens* CN-32. The indexed browser rank “no rank” versus fresh XML rank “strain” is not resolved by changing the label; the named-strain identity agrees. The paper prints ATCC BAA-543, but the authority maps CN-32 to [BAA-453](https://www.atcc.org/products/baa-453); [BAA-543](https://www.atcc.org/products/baa-543) is *Cellulomonas* sp. ES5. These official HTML files were retrieved by the iron curator and independently inspected here after web-reader timeouts. The record explicitly retains the discrepancy and does not claim experimental stock authentication. No criticality designation is inherited.

## Searches, access and deferred sources

Ten exact search queries and live open outcomes are preserved in `search-notice-log.json`. Exact DOI correction/retraction queries and fresh Crossref relationships did not surface an affecting notice; this is a bounded result rather than a global absence claim. Publisher HTML was rate-limited/forbidden while the complete primary PDF was available.

Cutting et al. (2009), DOI [10.1016/j.gca.2009.04.009](https://doi.org/10.1016/j.gca.2009.04.009), was rediscovered as evidence for a different organism and synthesis; only the publisher abstract was inspected, so no physical rates or microbiological claims from that study are imported. The 2021 article's earlier method references (2008 DOI 10.1021/es800686d and 2007 DOI 10.1080/01490450701459333) remain inherited-recipe follow-ups. The 2021 Data Availability Statement says data are available on request; no additional dataset access is claimed. Subsequent source work should resolve control metadata, caption time and stock provenance, then compare independent experiments without merging their feeds.

## Frozen artifacts and checks

Record SHA256: `6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61`. CREATE history: `history/records/feroxyhyte/2026-10-14T062756Z-codex-bd8d5e.yaml`, SHA256 `b762f1dac09b715e8c8c31f8d717011af630da47dc076353bc50809e6f974908`. The actual inline creation event and canonical history are distinct. Named validation passed (1 record, 0 failed). An initial draft used an unsupported process enum; it was changed to `redox_transformation` and the affected validation rerun before freezing. `git diff --check` passed. Companion JSON parses and all retained artifact hashes were rechecked. Independent review and final corpus/history/review gates are coordinator work and are not claimed complete here.
