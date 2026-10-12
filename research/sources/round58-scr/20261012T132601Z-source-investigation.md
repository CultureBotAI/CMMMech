# Spent SCR catalyst source investigation

- UTC: 2026-10-12T13:26:01.808273+00:00
- Investigator: `/root/round43_hardmetal`, codex (GPT-6).
- Worktree: `/private/tmp/CMMMech-expansion-round58-20261012`; trusted base `b6014c43b8174904e80f71df22be2251a802b418`.
- Record: `data/records/spent-selective-catalytic-reduction-catalyst.yaml`; SHA256 `8afd57586e305184911ec6fdadc8f6cee8609389e40bf29912a95e1f84ac397f`.
- CREATE: `history/records/spent-selective-catalytic-reduction-catalyst/2026-10-12T132257Z-codex-929b65.yaml`; SHA256 `ff9e46b75faea93fb69332f29fafdb74b617d2e00b8ed5e9159930513b98c2a6`.
- This is a source and curation handoff. Independent scientific acceptance and full batch gates are pending.

## Selection and ownership

Curated one spent selective catalytic reduction catalyst **secondary resource**. The complete Niu2025 primary supports centrifuged microbial-supernatant arsenic leaching from one coal-power-plant catalyst; the separate complete Su2020 primary supports chemical V/W extraction from its spent S3–S5 samples. Subsequent V/W loading, drying and calcination precede Niu's laboratory NO test. Neither mechanism establishes industrial deployment, an isolated metal product, or universal performance for spent catalysts.

The process-defined feed is distinct from the existing spent hydrodesulfurization, hydrocracking, fluid catalytic cracking and sulfuric-acid-production catalysts. Pure V/W/Ti elements, their oxides and mineral species are different concepts. No criticality claim is inferred. Fresh Su S1–S2 are excluded; Niu2021 already-regenerated material remains unadmitted, rather than being silently pooled or multiplied into another owner.

## Search and deduplication bounds

The actual hidden/ignored/symlink-followed inventories used `rg --files --hidden --no-ignore -L` on original-checkout and round58 `data/records`, `research`, `reviews`, `history`, then the referenced raw roots. Final pass read 4380 scientific text files and 8329 total text files across 193 extant referenced raw roots. Text formats were MD/JSON/YAML/TXT/XML/HTML, capped at16MB/file with realpath deduplication. All8 scientific roots were readable; 9 referenced older roots were missing and 14 large-file limits are individually enumerated in the JSON. No unextracted-binary or machine-wide absence claim is made.

Six prior raw-text hits included Wang2018 bibliographic references in the sulfuric-catalyst research and unrelated catalytic-hydrogenation text. No accepted SCR material owner or adopted exact experiment was found within the declared scope. Exact normalized DOI patterns for Niu2025/Niu2021 were added before curation. Source bibliography references are acknowledged prior discovery, not treated as previous full-primary inspection.

Exact retained notice/identity queries, all source URLs, raw web result dumps and acquisition receipts are in the paired JSON. Initial discovery outputs were archived; a complete exact query-string trace for those first exploratory queries was not separately retained. Each subsequent query used one public result set without pagination. No relevant correction was identified; several result sets were dominated by unrelated DOI-suffix hits, so this is a bounded negative observation rather than exhaustive notice clearance.

## Verified sources and original inspection

### niu2025

- Citation: Niu T, Xie X, Zhang X, Ma X, Feng F, Liu D, Tian B. Mild Extraction and Green Regeneration of Arsenic from Spent SCR Catalysts. Nonferrous Metals (Extractive Metallurgy),2025(12):38–45.
- Role: ['primary microbial-lixiviant experiment', 'secondary-resource identity']
- Decision: curate scoped bioacid arsenic removal and separate post-treatment regeneration context
- Version: Complete official original article; all eight pages read and visually inspected, including Figures1–3 and Tables1–7.
- Identity: Original title/authors/printed DOI match official landing and live Chinese DOI resolution; registered2December2025. Crossref returned404, which does not negate the Chinese DOI registration.
- Supplement scope: No supplement link/callout identified in the complete article or acquired official landing page; no inaccessible known supplement is assumed reviewed.
- License: Public official reading access; redistribution license not identified. Original retained outside Git.
- DOI: https://doi.org/10.20237/j.issn.1007-7545.2025.12.004
- Inspected local artifact: `/private/tmp/cmm-round58-scr-research/raw/niu2025-preview`.

### su2020

- Citation: Su Q, Yi X, Miao J, Chen Y, Chen J, Wang J. A Comparative Study in Vanadium and Tungsten Leaching from Various Sources of SCR Catalysts with Local Difference. Sustainability12(4):1499,18February2020.
- Role: ['primary abiotic extraction experiment', 'secondary-resource identity']
- Decision: curate S3–S5 spent-feed results only; keep S1–S2 fresh comparators separate
- Version: Complete official12-page PDF plus publisher XML; all pages and Figures1–9/Tables1–4 read and visually inspected.
- Identity: Original bibliographic identity matches fresh Crossref metadata. Crossref relation object empty; no correction marker in inspected XML.
- Supplement scope: Complete PDF/XML inspected; no supplementary-material callout or linked supplemental asset identified within these artifacts.
- License: CC BY4.0 in original article; originals nevertheless retained outside Git.
- DOI: https://doi.org/10.3390/su12041499
- Inspected local artifact: `/private/tmp/cmm-round58-scr-research/raw/su2020-primary.pdf`.

### ncbi637390

- Role: ['organism identity']
- Decision: exact source-reported strain designation resolves; no independent authentication of culture
- Identity: Acidithiobacillus thiooxidans ATCC19377, taxon637390. No accession for the experimental culture or genome inferred.
- Inspected local artifact: `/private/tmp/cmm-round58-scr-research/raw/ncbi637390.html`.

### wang2018

- Role: ['deferred primary microbial vanadium-leaching lead']
- Decision: defer all numerical, organism-specific and molecular mechanism claims pending complete original evidence
- Identity: Wang S,Xie Y,Yan W,Wu X,Wang C,Zhao F. Leaching of vanadium from waste V2O5-WO3/TiO2 catalyst catalyzed by functional microorganisms. Science of the Total Environment639:497–503(2018); PII S0048969718318163; PMID29800843.
- Access: Fresh official CAS article metadata, Crossref, OpenAlex and public Elsevier API inspected. API200 contains coredata only, not full text. ScienceDirect403; CAS HTTPS certificate failed but its public HTTP metadata route succeeded. No full PDF/figures/SI acquired.
- Limits: Publisher API coverDate15October2018 and other date representations are not silently harmonized; exact DOI/title/pages identify the lead. Abstract/citing-paper summaries do not verify original methods. OpenAlex reported closed with no repository PDF, a dated service observation rather than proof of universal unavailability.
- DOI: https://doi.org/10.1016/j.scitotenv.2018.05.168

### niu2021

- Role: ['deferred regenerated-product bioleaching lead']
- Decision: defer; do not merge regenerated-feed results or molecular explanation into Niu2025
- Identity: Niu T and colleagues. Deep removal of arsenic from regenerated products of spent V2O5-WO3/TiO2 SCR catalysts and its concurrent activation by bioleaching through a novel mechanism. Chemical Engineering Journal420:127722(2021); online16November2020.
- Access: Official University of Dundee repository landing and Crossref acquired. Its actual linked accepted manuscript https://discovery.dundee.ac.uk/files/55024594/Manuscript_Tianqi_CEJ.pdf and separate https://discovery.dundee.ac.uk/files/55024597/Figures.pdf both returned403; web-reader main route also403.
- Limits: Repository abstract describes already regenerated product after alkali/acid treatment; full original methods, graphics, supplements and experiment relationship remain unverified. Niu2025 cites it as reference15; citation and shared author do not establish independent replication or authorize transplanting results.
- License: Repository declares CC BY-NC-ND accepted version, but the manuscript and figure bytes were not acquired.
- DOI: https://doi.org/10.1016/j.cej.2020.127722

## Claim mapping and source contradictions

The bioacid mechanism retains source conditions, ATCC19377 identity, cell/sulfur separation, the concentration step, matched initial-pH acid comparators, NaOH arsenic/W tradeoff, and n=3 uncertainty. Supernatant sterility and a medium-only processed control are not demonstrated. Molecular thiol causality is qualified separately from observed As transfer. NO conversion is assigned to the combined regeneration treatment, not to bioacid alone. The chemical mechanism retains only spent S3–S5 arms and source-defined dissolved fractions.

- Niu2025 Table2: NaOH80.62% As extraction exceeds unconcentrated bioacid35.30%, but NaOH loses28.93% W versus reported0 for bioacid. Abstract unqualified bioacid superiority is not adopted.
- Niu2025 Table1 labels Ti(K),Ca(K),W(K) under common g/t units without defining K; Ti(K)664.3 is not corrected into kg/t or treated as a normalized feed inventory.
- Niu2025 Tables2–7 tungsten0 has no reporting detection limit; no exact-zero chemistry, complete tungsten retention, or V/Ti retention is inferred.
- Niu2025 Table7 C-Ats means twofold volume concentration from1L to0.5L, despite source single-concentration phrasing. Its81.63% is a liquid-derived As leaching fraction, not an isolated product.
- Niu2025 residual<200g/t is asserted without a separate residual-solid table or total solids balance. It is not certified against an independently checked current industrial standard.
- Niu2025 mechanistic thiol/metabolite identification is proposed and cites Niu2021. No direct metabolite assay is presented here. Claimed thiol deprotonation promoted by lowerpH is not adopted as established chemistry; equations and molecular interpretation are not imported.
- Niu2025 selected8h/50C conditions are pragmatic rather than absolute maxima;10h and65C arms separately exceed chosen extraction. Same44.74% mean recurs with differingSD across Tables3–7; no pooled estimate generated.
- Niu2025 Figure3 only compares spent, spent+V/W and bioacid-treated+V/W; it does not isolate bioacid-only catalyst performance. V/W loadings and final calcination temperature are unspecified. Original0.1g fixed-bed study is not industrial deployment.
- Su2020 Methods2.2 say120minutes, conclusion says240; no unique dwell time asserted. S1/S2 are fresh and excluded from spent results. Liquid/solid15 lacks explicit unit, and working liquid/solid mass and replicate uncertainty are absent.
- Su2020 Table2 oxide equivalents are not phase fractions; non-detection ofV/W crystalline peaks does not establish pureTiO2. Surface XPS fits and spectral associations do not isolate causal oxidation-state effects.

## Provenance, reuse and acquisition limits

The paired JSON pins every retained raw artifact, page render, extracted text and supporting receipt. Full originals remain outside Git. Niu2025 is public publisher reading access with unspecified reuse license; Su2020 declares CC BY4.0. No raw copyrighted full text or new importer is committed. Niu's DOI resolves through Chinese DOI registration with the matching title/authors; a failed Crossref lookup is not misrepresented as an invalid DOI.

The initial fourth-acquisition script had a local syntax error before any network request; it was corrected and actually executed, producing acquisition-fourth.json. Only the completed receipt is represented as acquisition evidence. HTTP403, a certificate failure, metadata-only200 responses and Crossref404 are preserved distinctly in the receipts. No blocked download is claimed inspected. Bulk replication/uncertainty and chemical-molecular claims are not reconstructed from pictures.

## Validation and handoff

Named command `uv run --locked cmmmech validate data/records/spent-selective-catalytic-reduction-catalyst.yaml` exited0 at 2026-10-12T13:23:27.819217+00:00: **1record checked,0failed**. Log SHA256 `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`. No shared suite was run by this curator; parent owns cohort gates. Canonical history and distinct inline CREATE were appended before the frozen hash. No schema, validator, README, rendering, governance, Git or GitHub mutation was performed.

## Prioritized follow-up

1. **Wang2018** — Acquire complete legitimate original PDF/all relevant figures/tables and any SI. Verify five reported culture arms, actual organisms/community provenance, catalyst feed, pH/loading/time/controls, V denominator and biological versus chemical contributions before extending microbial V extraction in this owner. No abstract numerical import.
2. **Niu2021** — Acquire the institutionally linked accepted manuscript and separate Figures PDF through a legitimate accessible route plus all SI. Establish regenerated-product preparation and relationship to Niu2025 experimentally; only then decide whether this is a context-specific extension or a genuinely separate derived-feed owner. No automatic new record.
3. **Niu2025/Su2020** — Resolve Table1K units, zeroW reporting/detection limits, regeneration loading/calcination details, bioacid processed-medium controls, and120/240minute discrepancy from original supporting data or an authoritative correction. Preserve present uncertainty meanwhile.

Paired machine-readable dossier: `research/sources/round58-scr/20261012T132601Z-source-investigation.json`; SHA256 `06594f9b992bac78d90688a61c40ae0fdffbd27870b3052c22752e8d6de76636`. Raw artifact count: 42; receipt count: 10.
