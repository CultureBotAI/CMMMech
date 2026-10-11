# Independent publication audit: round 16

- UTC timestamp: 2026-10-11T10:35:53.832078+00:00.
- Reviewer: Codex `/root/round16_publication_adversary`, GPT-6 / codex.
- Independence: this reviewer authored none of the six records, CREATE histories, source dossiers, canonical record reviews, README changes or publication/frontier reports. Only this publication audit was authored here. Separation is within one collaborating workflow, not organizational independence.
- Worktree: `/private/tmp/CMMMech-expansion-round16-20261011`.
- Branch: `curate/cmm-expansion-round16-20261011`.
- Trusted reviewed revision: `b714ce2bd8050d5e19ed9ca072460ba2b8154c3b`.
- Reviewed state: uncommitted working changes on that already merged base. Exact SHA-256 values of all 37 proposed publication inputs are listed below. This audit is an additional output, not its own scientific input.

## Scope and approach

Reviewed all fields of `cmmmech:forsterite`, `cmmmech:talc`, `cmmmech:lizardite`, `cmmmech:vivianite`, `cmmmech:siderite` and `cmmmech:oil-and-gas-produced-water`, their six actual CREATE sessions and six independent canonical review pairs. Checked source dossiers, acquisition ledgers, timestamped source assessments, README additions, frontier and publication report against source limits and actual validation receipts. Read CLAUDE, local add/review skills, record contract, structured-review contract and routing/publication profile. No native schema, validator, test, governed artifact or installed skill changes are proposed.

The audit checks scientific attribution, organism and material identity, experiment boundaries, controls and nulls, source access honesty, exact review coverage, history preservation, package claims and retained review bases. It is not raw diffraction refitting, reproduction of experiments, an exhaustive literature survey or a completed remote publication receipt.

## Evidence checked

- **Forsterite/talc:** retained web-extracted full primary text of [Cai et al. (2013)](https://doi.org/10.1080/01490451.2012.688924), methods pp. 303–304, Tables 1–2 and results/discussion. Mineral cleaning, minus-200-mesh Mg-source assay, inoculum, initial pH, temperature, agitation, ten-day endpoint and Mg/oxalate table values agree with the records. Chemical oxalate controls also dissolve forsterite; talc lacks a matched no-cell trajectory and has a reported secondary-mineral null. The separate size and cell-free-supernatant experiments are not pooled. Visual Cai diffraction figures were unavailable to the curators/reviewers, and this auditor did not obtain them; only the published assignment is accepted. Replication and total-product yield remain unresolved.
- **Lizardite:** retained primary XML, methods/results and supplementary pp. 1–2 of [Sheng et al. (2026)](https://doi.org/10.1128/aem.02554-25), plus independently viewed Figure 2. The medium modification, inoculation, triplicate assay and Mg/Si contrast match. The plotted pH dip/rebound, preparation-versus-observed pH distinction, siderophore threshold and gene-correlation limitations are preserved. Independently opened the live publisher page. Retained NCBI assembly `GCA_039631325.1` links C4-10, taxon 412384 and BioSample SAMN41260351; the assembly-method/completeness discrepancy remains in research, without an unsupported record claim.
- **Vivianite/siderite:** retained [Sánchez-Román et al. (2015)](https://doi.org/10.3389/fmicb.2015.01024) PDF/XML, complete methods and relevant results/discussion; independently viewed Figure 1 diffraction and Figures 3–4 microscopy. Fe(II) was supplied in FE medium. Mixed vivianite/siderite assignment, live/no-cell/nonviable contrasts, unspecified nonviable preparation/replication, final-pH disagreement and unknown Fe analytical fraction support the narrow records. Fe(III) reduction, pure-product yield and isolated EPS/phosphatase causality are not asserted. The live NCBI page independently confirms species 1427523 and equivalent type-strain designations.
- **Identity authorities:** retained IMA September 2026 list and exact five species/formula/status rows, plus retained taxonomy XML for 5061, 412384 and 1427523 and LPSN type-strain context. Original-description and special-procedure years are not invented approval-number identifiers. Species taxonomy is not presented as a strain accession.
- **Produced water:** retained [USGS Fact Sheet 2014-3104](https://pubs.usgs.gov/fs/2014/3104/pdf/fs2014-3104.pdf) definitions and historical USGS resource-opportunity HTML. Generated hydrocarbon-production byproduct scope supports `secondary_resource`, while variable composition and the distinct natural geothermal resource are explicit. No Hu2021 mechanism, lithium recovery, criticality or universal concentration is imported from incomplete primary access.

The three source ledgers' 22 hashed acquisitions were independently compared with retained local bytes, including error responses correctly classified as unavailable text. Raw roots were `/private/tmp/cmm-round16-silicate-raw`, `/private/tmp/cmm-round16-vivianite-raw` and `/private/tmp/cmm-round16-produced-water-raw`. Representative primary hashes: IMA PDF `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`; Sheng XML `964dca1e8190032f5d1241c843ee052b642bd949ddc917e7245569975a64a344`; Sánchez-Román PDF `0a57eb35bc370ce8f86c830eb7255fe3c3df369160907a38838a05a32fd7c8ef`; USGS PDF `9e180cef5ba29cd24b693ba59ee3ed34ba125747aeff7f77abff9979e09c3485`. No Cai PDF-byte hash is invented. Direct live Frontiers DOI and USGS PDF opens failed in this audit; authentic retained bytes supplied the inspected evidence.

## Search boundaries and conceptual separation

Independent exact-DOI searches used `"10.3389/fmicb.2015.01024" correction OR retraction OR erratum`, `"10.1128/aem.02554-25" correction OR retraction OR erratum`, and `"10.1080/01490451.2012.688924" correction OR retraction OR erratum` on 11 October 2026. No applicable notice surfaced in these first returned result sets; the AEM.02554-13 retraction is a different article. This is not proof of absence of all corrections or contradictory evidence.

Local discovery/duplicate checks included hidden and ignored files and followed relevant links with `rg --no-ignore --hidden --follow` across data, history, research, reviews, local skills and docs; the three named raw directories were inventoried and relevant primary files inspected separately. Boundaries were local and explicit, not machine-wide. Forsterite/talc share one study; vivianite/siderite share another. Species, elements, commodities and resource streams remain distinct. None of the additions inherits constituent criticality. Primary literature copies, abstracts and supplements are not counted as independent experiments.

## Validation and preservation

Independently read actual root terminal logs and durable receipts rather than treating a running command as success:

| Check | Observed completed result |
|---|---|
| Baseline `just check` | 308 passed, 3 skipped; 122 records, 138 histories valid |
| Final `just check` | 308 passed, 3 skipped in 123.11 s; 128 records, 144 histories valid |
| `cmmmech validate --require-records` | 128 checked, 0 failed |
| `cmmmech validate-history --base b714ce2bd8050d5e19ed9ca072460ba2b8154c3b` | 144 checked, 0 errors |
| Structured check against trusted base with `--require-reviews` | 143 valid YAML/Markdown pairs; terminal exit 0 |
| Vendored synchronization | Root package receipt reports terminal exit 0 and 22 artifacts matching CLAW pin; governed bytes are unchanged by this batch |
| Independent manifest, links and byte checks | All six current target/history/schema hashes match saved reviews; frontier counts and record hashes agree; checked relative Markdown links resolve; `git diff --check` passes |

Independent enumeration confirms **128/128** current records have an exact-hash passing scientific review marked independent. All **773** previously tracked files under `data`, `history`, `reviews` and `research` remain byte-identical to the trusted base, compared directly with its Git archive. All **17** review bases remain available: 16 are ancestors of trusted main; the remaining `c0adc2c0763e1515ed07dc712b024974d98fb342` is retained by `review-base/cmm-source-survey-20261009`. The remote tag was independently checked: annotated object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit `c0adc2c0763e1515ed07dc712b024974d98fb342`. No topic-only base was introduced.

Receipt files independently inspected include `/private/tmp/cmm-round16-gate-receipts.json`, `/private/tmp/cmm-round16-package-terminal-receipt.json`, `/private/tmp/cmm-round16-coverage-audit.json` and the final batch/require/history/review logs. Independent coverage/preservation computation is in `/private/tmp/cmm-round16-adversary-inspection.json`. The checked ruleset receipt agrees with active SQUASH/ALLGREEN, required `validate-strict` App15368 and no bypass actors. Governance status is not expanded by this curation batch.

## Findings by severity

- Blocker: none found in this scope.
- Major: none found in this scope.
- Minor: none found in the final reviewed package.
- Informational defects: none. Source and acquisition limitations are preserved as limits, not manufactured review issues.

## Corrections and unresolved questions

No correction was required by this independent final audit. The earlier package assembly corrections described in the publication report are present in the final bytes: timestamped silicate assessment, working relative links and corrected follow-up attribution. This audit did not rewrite any record, canonical review or curation history, and does not invent a previous finding or correction event.

Cai visual diffraction access, strain collection provenance and assay uncertainty remain unresolved; lizardite feed purity, acid-matched controls and causal gene tests remain unresolved; Fe-mineral phase proportions, analytical fractions and separate pH/surface causes remain unresolved. Hu2021 main text is still needed before a produced-water mechanism can be curated. These limits do not contradict the narrower accepted records. Enstatite, biotite group identity, other saline feeds and retained earlier leads remain concrete future work; global material/source exhaustion is not established.

## Verdict

**Pass with limitations for this exact local publication package.** No actionable blocker, major or minor defect remains in the assessed state. This verdict does not claim remote CI, squash-shaped preflight, queue admission, merge or branch cleanup has already happened. Those subsequent steps must verify the frozen paths, preserved bases and exact published tree, then check fresh remote main after branch deletion. The original checkout's ignored/untracked preservation is a later guarded closeout check, not a claim inferred from this worktree audit.

## Exact reviewed input manifest

| Repository-relative input | SHA-256 |
|---|---|
| `README.md` | `3459f5bc1cfde095c69aa84c8df08242887def1bf152010b1ea63a27b272a30e` |
| `data/records/forsterite.yaml` | `fe9d20cf24f94fa19731b0a864e00cd5c199ae807ecbe346e8239d52133cd30c` |
| `data/records/lizardite.yaml` | `535a6f4a0c3f74f254ab0f3d19c4ead03774d16a8c83f7769d1c4aeac0092684` |
| `data/records/oil-and-gas-produced-water.yaml` | `83d79172269bb7ea45169a0c4bc1e1a268c77c356d79ba37e7564be88a1af077` |
| `data/records/siderite.yaml` | `664cc364a07cd83345b7d2b7cff2ac6a30403e6a93b3e7cb153418737a835ba0` |
| `data/records/talc.yaml` | `a3cea92e8e5a83897af7919880c059b2f5ec94e2a7930f87a6d26eba3ad706f6` |
| `data/records/vivianite.yaml` | `8d820242970cd8a50d54ce1644caee79cdc508ba7a7c575f556dbe9f94dfc3d7` |
| `history/records/forsterite/2026-10-11T102433Z-codex-ff90a8.yaml` | `ca3f7aeb7ce8b7a7fe178f02a694f4609e4c32494415cd620faa65968f65094d` |
| `history/records/lizardite/2026-10-11T102453Z-codex-c8e63a.yaml` | `3fb097343dffa36aa2a0b12de8978cfd45ab8239a235d3d234ec87f1ac1f4559` |
| `history/records/oil-and-gas-produced-water/2026-10-11T102408Z-codex-39636b.yaml` | `16925c90f6741d0c68e7cc6e7b0bfc67e7fb985a73effa0eae9a718d63af0c10` |
| `history/records/siderite/2026-10-11T102441Z-codex-ba014b.yaml` | `6892d61075685f25e95c5d0350a3bd175eff38f88f8bbfc98b02d8a19c77ac33` |
| `history/records/talc/2026-10-11T102447Z-codex-d0e525.yaml` | `7d430fa15cc4ebd4d226232eac18087faade5b2c3e59e837a02dfdecf616469b` |
| `history/records/vivianite/2026-10-11T102429Z-codex-0b28a8.yaml` | `91f07e2289f8a42d70f13cf26917c03ef3e2185859a1b7337591b47faf59012d` |
| `research/ingests/round16-20261011-publication.md` | `f333417eb339c556460410121c6b1d54c7b5e6e07a35a62da0f8121cbf3a6d99` |
| `research/ingests/round16-frontier-20261011.json` | `7acd7fab11da2987a1c649bdbb44f94aa857a460fac7fddf80a7d3fd3b372a68` |
| `research/ingests/round16-frontier-20261011.md` | `176be6b9421b6b506abd00f830b253ee81f862ee0bd864cde68208a7e2bf8043` |
| `research/ingests/round16-produced-water-sources-20261011.json` | `d259bf1289f550ee30f7db55fcbce8c5264450b72c1bd093695b571ddb1d618e` |
| `research/ingests/round16-produced-water-sources-20261011.md` | `812a512ef774fac21e34988b9f9b1785ba8fb5e00cb87f377cc2390ce5d0542c` |
| `research/ingests/round16-silicate-sources-20261011.json` | `628175f621c62d0255bd2869fd72f9094b5e09fe5af561bb514e4391a1f4af12` |
| `research/ingests/round16-silicate-sources-20261011.md` | `1a25998d54648decf6214986ed1d4f8b2baf8a87a77ebe730e5bd9125eded28d` |
| `research/ingests/round16-vivianite-sources-20261011.json` | `c2881bccd2e928e364162f05e50256b6fc6297a278ff5a81eb88a780625b43a5` |
| `research/ingests/round16-vivianite-sources-20261011.md` | `420f3765653a24ace74dc2e395bada8e19102358b746839d2ffadb8e962081ee` |
| `research/sources/round16-produced-water-sources-20261011/20261011T102517Z.md` | `812a512ef774fac21e34988b9f9b1785ba8fb5e00cb87f377cc2390ce5d0542c` |
| `research/sources/round16-silicate-sources-20261011/20261011T102740Z.md` | `0c66a85cb34f90dfd02727ea6010dfc1e984a78bac07169a8ccf643be6813918` |
| `research/sources/round16-vivianite-sources-20261011/20261011T102545Z.md` | `0db9a693d11f81e155a9df0a0835f184bbc640291463ad3bedc818d2e4e06275` |
| `reviews/structured/20261011T102918Z-oil-and-gas-produced-water-round16-independent/review.md` | `18fccc82713aad60f36036bd2b6a92193fbbf445cedcd87358f2adec5044ef03` |
| `reviews/structured/20261011T102918Z-oil-and-gas-produced-water-round16-independent/review.yaml` | `9cd8d2d44110d4fa0b69ea42e78443d8ab1df1613238cad6037ebf18ba94b11e` |
| `reviews/structured/20261011T102935Z-forsterite-round16-independent/review.md` | `3c2d0436e1153b2ba0fb8e6d28ecdda8bef9c215c7e01f6ab946887182487583` |
| `reviews/structured/20261011T102935Z-forsterite-round16-independent/review.yaml` | `ba3469ca385d260c5eaf639ddc24545af87f3e50b5fb8cab7afcb311046f55e9` |
| `reviews/structured/20261011T102939Z-talc-round16-independent/review.md` | `df118c4dea892f7d3ea4b7cc3f6d3d92cc42168c5438348c4de85cb8e8965c89` |
| `reviews/structured/20261011T102939Z-talc-round16-independent/review.yaml` | `5f57e06dd6f16a4c81a72b7f16347870f2d597f6f8939dc40667fc2b34d53a41` |
| `reviews/structured/20261011T102943Z-lizardite-round16-independent/review.md` | `206ce8b03de56110efe5a2f94ecc45866486fd9fdd2f8dd9e9e4792335e8d816` |
| `reviews/structured/20261011T102943Z-lizardite-round16-independent/review.yaml` | `c54fb32de750a96bcc28df07b3402695ed2733d00d4011093b2bba2471727676` |
| `reviews/structured/20261011T103120Z-siderite-round16-independent/review.md` | `e9f889c892d415a0f302d432d95907aa27aa6aecba03b37916c5b946d8a2240a` |
| `reviews/structured/20261011T103120Z-siderite-round16-independent/review.yaml` | `2e322d04a2f755df59864e4322198c5a056f735295fd3fdc90e29c989a2a5ebc` |
| `reviews/structured/20261011T103120Z-vivianite-round16-independent/review.md` | `2f305eeffcad129672ec2a6865a6297b7bf7f8dde8e9c26e9bae98dfc456e90e` |
| `reviews/structured/20261011T103120Z-vivianite-round16-independent/review.yaml` | `a13bb193e7c4af6601f398a171b19294cb86f0bb1887d50e1e3e68b5f5bb1001` |
