# Stibnite: source investigation and curation handoff

- UTC: 2026-10-11T19:13:08.710411+00:00
- Worktree: `/private/tmp/CMMMech-expansion-round31-20261011`; branch `curate/cmm-expansion-round31-20261011`.
- Trusted base: `075c1ca032b68162eb8350b7e8d9bfe9530ca143`.
- Author: codex (GPT-6; codex), round27_superalloy. This is a curator dossier, not independent scientific approval.
- Record: `data/records/stibnite.yaml`, SHA-256 `436111a89c641f24b52e1c42881f554b19598701fc946b20fea75ee9a73d5e97`.
- CREATE history: `history/records/stibnite/2026-10-11T191131Z-codex-afa2f3.yaml`, SHA-256 `110c0c125526e955f64629db15081a2558634de06593c61233d1611a2e379064`.

## Selection and identity

A complete primary paper, original supplement and authority identities support one narrowly scoped stibnite observation. Stibnite is the Sb2S3 mineral species (IMA September2026, page206, grandfathered, original-description1832); it is not elemental antimony, dissolved Sb, mixed ore or mine waste. No criticality claim is inherited. The assay used commercial material fitted as97.19wt% stibnite and2.81wt% quartz. The study's natural5M/25M/27M ore arms remain separate.

NCBI34007 is the species Paracoccus versutus, not an authenticated strain/genome record for XT0.6. The paper identifies XT0.6 with1749single-copy orthologs. DSM582 shown in its comparison tree is not the experimental strain identifier. The author-assigned secondary phase mopungite is consistent with IMA September2026 page148, NaSb5+(OH)6, approved1982-020.

## Primary evidence inspected

[Loni et al., DOI10.1016/j.jhazmat.2019.121561](https://doi.org/10.1016/j.jhazmat.2019.121561) is Journal of Hazardous Materials385(2020),121561, online2019. The inspected [university-hosted complete PDF](https://eniec.cug.edu.cn/__local/9/73/1A/16702EAED267B1B0B103625C0FB_74D3AD58_387DD0.pdf) is a10-page typeset article-in-press with xxx headers, not claimed final publisher pagination. Read full methods/results/references and visually inspected all10 original rendered pages, all8 figures and Table1. Main original SHA-256: `2c214467f21b59ee316395aabdea64cefca209adca45dc0fc191b76621ea0451`.

The [original publisher supplement](https://ars.els-cdn.com/content/image/1-s2.0-S0304389419315158-mmc1.docx) is genuine DOCX despite its application/word HTTP content type. Full OOXML body, all3 tables and all5 original embedded figures were inspected; printed DOCX pagination was not rendered. TIFF figures were decoded toPNG without redrawing. Its self-description is9pages,5figures,3tables. Supplement SHA-256: `96e815d8c5f72afa4d70c34623725ec579309db21f62dc02e03cb54defe307d8`. Hidden EndNote fields are not experimental results.

The dated IMA PDF was reused byte-for-byte from a same-day official acquisition, with prior source/receipt and original17:41:04Z fetch time retained; this is not a fresh authority retrieval. The original page images148/206 and headers were inspected. NCBI species34007 was freshly fetched at19:07:51Z. Complete request times, URLs, HTTP outcomes, content types and hashes appear in the paired JSON/raw receipts.

## Defensible observation

Main section2.3.3 specifies commercial200mesh solid,0.1g in100mLCDM, sterilization120°C20min, cooling and1%v/v culture grown without Sb(III). Incubations were aerobic,30°C,150rpm,dark,duplicates, with a13-day time course. The mineral assay does not state washed inoculum or cell density; these are not imported from the separate washed-cell kinetics assay. The prior medium recipe is cited without a complete recipe here.

In Figure4A/section3.2, culturepH rises7.2 toward9.3. The source reports dissolvedSb(V) peaking at68mg/L on day4, declining to about20mg/L byday13; Sb(III) is reported below detection afterday1 without a numerical detection limit. HPLC/hydride-generation AFS analyzed centrifuged/filtered liquid, not total recovered Sb. Filter pore size is unspecified. Error bars represent duplicate-experiment standard deviations.

Table1/Figure6A assigns8.25wt% mopungite in the biotic commercial-stibnite residue. This is a fitted relative XRD mineral fraction. No isolated-product yield, closed antimony mass balance, industrial process or absolute stibnite-consumption percentage is established. SEM/EDS roughening and Na enrichment do not independently identify an enzyme or prove direct mineral contact.

## Contradictions and causal limits

- **Main section2.3.3 vs supplement TableS3 header**: 0.1g per100mL equals0.1%w/v in main; SI says1%w/v. Tenfold loading inconsistency unresolved. Both retained explicitly; no feed-normalized extraction/recovery yield calculated.
- **Main sections3.2-3.3, Figures4A/5E and TableS3**: Biotic pH rises7.2 toward9.3; initial-pH7.2 abiotic control acidifies. Additional high-pH abiotic controls release and oxidize substantial Sb and can exceed culture peak. No matched pH trajectory or pH-stat design. Narrow culture-associated transformation, not uniquely proven direct enzymatic mineral attack or superiority over all abiotic arms.
- **Main Figure5E, section3.3 and SI TableS3**: Prose/SI quote high-pH total88mg/L and70.12%SbV. Visual Figure5E day13 SbV near62mg/L and SbIII near36mg/L appear to sum near98mg/L. This is a visual estimate, not digitized exact data. Exact alkaline total and percentage not adopted; qualitative substantial abiotic release retained.
- **Main Table1 and section3.4**: Commercial stibnite normalized XRD phase fraction97.19% initially and74.45% in biotic residue; quartz2.81% and17.30%; mopungite8.25%. The22.74 percentage-point shift is not absolute mineral mass loss. Only fitted relative mopungite fraction retained, no recovery or mineral-consumption percentage.
- **Main section2.4**: Biotic residual solids received10%SDS before freeze drying; abiotic solids were freeze dried directly. Preparation difference disclosed; lack of assigned control mopungite bounded by XRD.
- **Main Table1 vs section3.4 natural25M arm**: Table1 initial25M calcite23.69% conflicts with prose around33%. Natural ore arms excluded from this commercial-stibnite mechanism.
- **Supplement TableS3 natural5M pH9.3 arm**: Reported percentages53.04 and56.96 sum to110 rather than100. Natural ore percentages not adopted.
- **Main Figure2 caption and supplement FigureS2 caption**: Main caption refers to panelsB-D despite main plottedA/B; SI dissolved300M Sb(V) label differs from main Sb(III) setup, with unit-symbol ambiguity in extracted text. Separate soluble-Sb/anaerobic experiments not imported as mineral conditions or outcomes.

## Coverage, counterevidence and unfinished work

The current observation is explicitly aerobic. Later XT0.6 papers DOI10.1016/j.jhazmat.2024.133731 (contact pathways) and DOI10.1016/j.jhazmat.2025.140532 (aerobic promotion versus anaerobic inhibition) are documented primary-abstract followups. The2025 publisher request returned403; third-party indexed text was not accepted as a complete original. Their methods, measurements and exact experiment overlap remain unverified, so they are not used to backfill the2020 record. The2022 acidic-culture paper DOI10.3390/ijms23073580 was acquired as fullPMCXML but has not completed figure/method assessment; it remains a future mechanism candidate. The2024 iron-assisted DOI10.1016/j.eti.2024.103640 is an unacquired accepted-PDF lead only.

Bounded exact-title/DOI correction/retraction searches and Crossref update/relation inspection identified no affecting notice in checked coverage; this is not an exhaustive absence claim. The paired JSON lists all queries and access limits.

Hidden/ignored-inclusive `rg --no-ignore --hidden --follow` covered current and original records/research/reviews/history, all existing non-cache raw roots from the prior round30 referenced-path inventory, and current raw evidence. The search found115 lines but no existing stibnite record hit before creation. Exact command/roots/results are preserved in the paired JSON and outside-Git dedup receipt. PDF, image, Office and ZIP bytes were excluded from text search; extracted text/metadata was searched and accepted original artifacts were read separately. No global binary/OCR completeness claim is made.

Issue103 Han2023 tungsten-waste methods remains independently open. Its new-route deferral is saved under `research/sources/round31-tungsten-mining-waste/20261011T190610Z-source-investigation.{md,json}`. Stibnite curation neither supplies those missing methods nor closes that source issue.

## Validation and handoff

Named-file validation completed exit0: `Checked1record(s);0failed.` Exact command/session/result are recorded in JSON. The new record and canonical CREATE history are frozen at the hashes above for independent scientific review. Full batch gates and independent review are coordinated separately; this dossier does not assert their completion. No schema or validator change was needed.

Raw copyrighted article/supplement files stay outside Git at `/private/tmp/cmm-round31-stibnite-research/raw`. The paired JSON contains hashes for every retained raw artifact and acquisition receipts. IMA distribution terms are CC BY-SA3.0; no raw documents or images are committed.
