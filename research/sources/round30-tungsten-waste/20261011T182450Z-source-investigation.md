# Tungsten mining-waste follow-up and Swedish tailings curation

UTC: 2026-10-11T18:24:50Z. Worktree: `/private/tmp/CMMMech-expansion-round30-20261011`; base `930ce995269f0ded5df009eb5916162971eb1f58`. Author: codex (GPT-6; codex), independent of the forthcoming record reviewer.

## Outcome and identity

**Issue #103 remains open.** New legitimate thesis/preprint/metadata routes did not supply Han2023 full methods. Nothing from that incomplete experiment was promoted into a mining-waste mechanism. The predecessor is `research/sources/round29-tungsten-waste/20261011T174244Z-source-investigation.{md,json}`; all24 listed raw hashes were rechecked unchanged.

The bounded fallback produced `data/records/tungsten-skarn-tailings.yaml`, a secondary resource from ore processing, supported by complete original articles. It identifies historical Smaltjärnen tailings at Yxsjöberg, Sweden, separately from tungsten, scheelite, unprocessed ore and waste rock. One explicitly **nonmicrobial** laboratory physical-separation mechanism is curated; field weathering is contextual evidence. No inherited criticality, organism ID, bulk-repository recovery, mineral-product purity or industrial deployment claim is made. No schema change was needed.

Frozen record SHA-256: `76f7605b69902eacc1b1e36ecd3e953ed0acef1ba62ba30b67d9742ab596576c`. CREATE history: `history/records/tungsten-skarn-tailings/2026-10-11T182401Z-codex-4ba0b0.yaml`, SHA-256 `8c576f62009f056265251da4d6ee880d1dd9b051171bc170216c9f9a77b3fd4a`. Inline CREATE records the actual work. Named validation passed: `Checked 1 record(s); 0 failed.` This source assessment is **not** scientific acceptance; independent native review and parent batch gates are pending.

## Searches, bounds and duplication

The paired JSON records all26 exact web queries, direct request URLs, access timestamps/statuses and retained artifact hashes. Web searches inspected first returned sets only; no exhaustive literature coverage is claimed. Queries covered the three Han publications and alternate author/institutional repositories, notices, reference leads and Yxsjöberg counterevidence. An irrelevant numeric-identifier search returned unrelated personal/financial hits, which were not inspected.

Dedup used `rg --no-ignore --hidden --follow` over corpus/research/reviews/history in both current worktree and original checkout, plus the predecessor's named raw directories and this task's raw directory. All named paths were accessible. Binary PDF/image/Word artifacts were inventoried and extracted text/metadata searched; this is not an OCR/embedded-byte or machinewide search. Exact command,346 matching lines and errors are retained under `/private/tmp/cmm-round30-tungsten-research/raw/dedup-*`. Relevant accepted-record matches were the tungsten element and scheelite mineral, not processing tailings. Mulenshi's DOI already occurs as a Han reference, which is a discovery lead rather than prior curation.

## Han acquisition and experiment overlap

[Han's author ORCID](https://orcid.org/0000-0002-2286-6222), Crossref thesis DOI registration and [PubMed36473257](https://pubmed.ncbi.nlm.nih.gov/36473257/) distinguish the earlier field-characterization article DOI10.1016/j.jhazmat.2022.130508 (online2022;issue2023) from the later column study DOI10.1016/j.jhazmat.2023.131490. The former is associated with SSRN preprint DOI10.2139/ssrn.4226460. Crossref confirms thesis DOI10.14264/9e55310 and exact official UQ record UQ:9e55310. The thesis abstract includes enriched-culture syringe columns and mineral characterization; overlap is plausible, but exact shared samples/data remain unresolved. Different titles or years do not establish independent experiments.

New public SSRN landing/download requests returned403; thesis DOI returned403. DataCite404 reflects an unsuccessful agency route, not proof the thesis does not exist; Crossref registration succeeded. QUT search was robots-blocked and not retried. No unchanged denied round29 publisher/UQjournal/ElsevierFULL endpoints were repeated. Prior six original figures and Word SI retain useful assay cautions, including microbial signals in +M arms and mixed cumulative-mass units, but do not resolve medium,feed/inoculum,controls,replication or phase-fit methods. No sterile-control, percent-recovery or authenticated-strain inference is adopted.

## Primary Swedish evidence and claim limits

[Mulenshi et al.2019](https://doi.org/10.3390/pr7120895) was acquired from the official MDPI content host as a complete19-page PDF; SHA-256 `606160c22358c53cbb5f9426b6d13d39a0096f541f29d9bb924af4317d1e2725`. The full main text was read; original pages3,6,7,11–17 were visually checked for provenance,methods,Tables2–6 and the relevant mineral/processing figures. The extracted text includes duplicate invisible draft text; visible publisher pages were used to resolve it.

Sections2.1–2.4 establish original processing origin and distinct core1_2 layer feeds. Table3 gives the58mL Knelson operation at1500rpm,60G,3.5L/min water and2kPa. The two cycles are serial separations, not independent replicates. Table6 reports actual feed masses521.42g and499.64g, first-concentrate W distributions60.6% and47.1%, and residual W in second concentrates/tailings. The abstract's~75% combines the first feed's two concentrates; the conclusion's60.6% refers only to its first. Neither number is concentrate purity or an unsieved-repository yield. Methods' minus600/plus38micrometre fraction differs in completeness from Table6's minus600 shorthand and is retained explicitly.

Figure13 supports mixed liberated/unliberated scheelite and surface rims. Figures14–17 and Tables5–6 show incomplete selectivity: magnetic tests retain most W in the paramagnetic product and gravity concentrates retain other assayed elements. Table5 uses calculated magnetic-feed balances, which must not replace Table6's actual gravity-feed basis. W content proxies scheelite recovery; quantitative product mineralogy is future work. Replicated separation outcomes and error estimates are not supplied. Figures18–19 propose a flowsheet, not demonstrated commercial operation.

[Hällström et al.2020](https://doi.org/10.1007/s11356-019-07305-1), online21December2019, was acquired as a complete13-page DiVA publisher PDF and complete EuropePMC XML(PMC7044260). PDF SHA-256 `246371f98e0694d3ac89cc304c91ef748cc8a10b0424fc44fe96afd7fcd05482`. Full methods/discussion were read and pages3,5,10,11 visually inspected for Figures1–3,6–7. P4 core investigation and monthly May–October2018 groundwater/surface-water assays establish field context. Analytical duplicates,blanks and standards are not biological controls. Dissolution/retention pathways remain qualified geochemical hypotheses; no microbial mechanism is isolated. C13 and combined C14/C16 waters receive the separate Morkulltjärnen repository's input.

No precise field equation, rim depth, repository tonnage, contemporary contamination threshold or harmlessness claim is adopted. Reasons include Fig6's HCO3 charge notation and2.6m caption versus3.6m elsewhere;2.2Mt versus2.8Mt repository estimates across articles; and discussion of threshold exceedances at other catchment points that complicates the abstract/conclusion's broad threshold wording. Nearby cores are not assumed identical samples or independent replication.

## Access, reuse and remaining work

Both adopted articles explicitly carry CC BY4.0; raw PDFs/renders/XML remain outside Git at `/private/tmp/cmm-round30-tungsten-research/raw`. Publisher webpage failures did not prevent lawful publisher-content-host acquisition. The separately downloaded Mulenshi2020 thesis is retained with exact provenance but not scientifically adopted or fully inspected; publication steering ended new-lead work. The acquisition batch completed naturally, with full200 receipts, before an attempted termination; a temporary recovery note was corrected to point to authoritative `acquisition-yxsjoberg.json`.

Exact DOI notice searches and current Crossref update fields found no relevant formal correction/retraction within stated bounds. [MDPI version notes](https://www.mdpi.com/2227-9717/7/12/895/notes) show an original2019 PDF and later HTML updates; they do not establish a new experimental edition. Future lead metadata for Nguyen2018 As/Mn bioleaching, Guedes de Carvalho1990 tungsten ore bioleaching and Han2025 characterization remains deferred and is not imported.

1. Complete independent native review of the frozen Swedish record and batch gates.
2. Keep #103 open pending legitimate Han full methods, control definitions, phase fits and experiment-overlap verification.
3. Future microbial claims for Swedish tailings require direct biological primary evidence; field weathering and engineering beneficiation do not supply it.
4. If later using the downloaded thesis, inspect its complete methods/version and experiment overlap before adding claims or counting replication.
