# Spent vanadium-flow-battery electrolyte: source investigation

UTC: 2026-10-15T21:18:43.154276+00:00. Curator: Codex (GPT-6; codex), root.

## Scope and provenance

Worktree `/private/tmp/CMMMech-expansion-round103-20261015`, branch `curate/cmm-expansion-round103-20261015`, trusted base `44d5b468519eb862b32ef54bf7c066bc0f79ba62`. The baseline passed before record creation (317 tests passed, 3 skipped; 501 original records and 572 histories). The paired JSON preserves the actual receipt hash, exact search queries, primary acquisition times and raw-file checksums. Concurrent mineral curation is outside this authorship.

The selected resource is sulfuric-acid vanadium electrolyte after battery use. It is not the element, a fresh electrolyte commodity, spent catalyst or solid scrap. This search spans chemical recovery and electrochemical regeneration; no primary microbial experiment was accepted. Criticality lists and biological identifiers are inapplicable to the claims being curated, so neither is inherited.

## Search and acquisition log

On 2026-10-15, bounded web searches combined spent vanadium electrolyte, microbial recovery, bioleaching and chlorate; subsequent exact DOI/title searches included English correction/erratum/retraction and Chinese correction terms. Exact queries and top-result scope are in JSON. These searches are not exhaustive. A preliminary vanadinite search returned already known routes; its decisive old figure-access gap was not resolved or repeatedly retried.

Both primary PDFs were freshly acquired from publisher-linked endpoints, passed PDF signature/open checks, and were rendered for visual examination. All five pages of Yang2016 and seven pages of Peng2024, including all figures/tables, were read. No previous cached acquisition is presented as a fresh download. Crossref returned404 for both DOIs. Yang's DOI resolved through the Chinese DOI registry to matching title/authors; Peng's DOI resolved to the official publisher. These registry results do not invalidate the publisher originals. Peng's publisher page lists zero resource attachments; this is a bounded site observation, not proof that no unpublished supplement exists.

## Candidate inventory

| Candidate | Evidence inspected | Decision |
|---|---|---|
| [Yang and Wang2016](https://hgjz.cip.com.cn/EN/abstract/abstract4251.shtml), DOI10.16085/j.issn.1000-6613.2016.09.047 | Complete five-page original, Figures1–5, Tables1–5, methods and pilot-product report | Curate qualified chemical recovery from a company-supplied used liquid |
| [Peng et al.2024](https://doi.org/10.7513/j.issn.1004-7638.2024.03.002), 45(3):9–15 | Complete seven-page original, Figures1–7, Tables1–2 and all four laboratory protocols | Curate functional regeneration separately from product recovery |
| Catalyst-to-electrolyte publications, patents and industry brochures | Search metadata only | Different feed or insufficient experimental/deployment verification; no imported claim |

Yang2016 PDF SHA256 `3418860ee1e3c7366c540ed392f1f444e340be765fcebcb6cc02b5bf00326399`; Peng2024 PDF SHA256 `1e542492ac1f08d17e615f7fd3cdb50e90828c201d9b8b83d5095543b2573c25`. Raw originals/images remain in `/private/tmp/cmm-round103-electrolyte-research`, outside Git. Yang's landing states All Rights Reserved; redistribution permission was not established. Peng's HTML metadata declares CC BY3.0; the original still remains outside Git. No bulk dataset is claimed or imported.

## Scientific assessment

Yang2016 has a defined material supplier and separate positive/negative oxidation assays. Section3 reports a 1-m3 positive-feed pilot batch, a harvested148.30-kg powder and99.58% dry-basis NH4VO3. Those are author-reported pilot product observations, not independently verified commercial deployment or purity-standard compliance. Product phase is not demonstrated by an included diffraction pattern, and its exact NH4VO3 assay procedure is not supplied. Table4 precipitation percentages follow liquid concentration differences; they are not product yields or closed balances. Figure2 and nearby prose use V2O5-equivalent concentration, while generic wording calls it vanadium concentration. Printed zero low-valent-V cells lack detection limits.

The 2016 conclusion's pH2.0–2.5 conflicts with methods, Figure3 and abstracts at8.0–8.5. Methods use100–120min precipitation; abstract/conclusion give80–120min, despite distinct Table4 endpoints. These conflicts are retained. The standards cited for analytical methods were not independently assessed, and historical costs/environmental claims are not adopted.

Peng2024 explicitly creates aged electrolyte by cycling purchased fluid until capacity falls below50% of rated capacity. It studies laboratory28-cm2 cells, not returned commercial waste. Figures3–7 support partial capacity restoration, with new/aged comparators and declining energy/voltage efficiencies as current increases. Sequential cycles are not independent replicates. The direct and sulfuric-acid percentages reverse between Results and abstract/conclusion; the asymmetric paragraph misnames another arm. A stated1190-mAh target conflicts with2238mA for30min, which equals1119mAh arithmetically. No corrected value is guessed. UV-visible assay values follow a50-fold dilution and are not undiluted feed concentrations.

The direct protocol regenerates only one compartment. The sulfuric-acid protocol corrodes collectors and replaces them and graphite felt before testing, so hardware differs. The asymmetric route requires about5h. These observations limit whole-feed accounting, comparative efficiency and durability claims. Functional capacity percentages must not be pooled with the different 2016 precipitation percentages. Both papers support abiotic processes; no organism, microbial necessity or isolated metal yield is invented.

## Deduplication

Hidden and ignored text artifacts, following symlinks, were searched across main data/research/reviews/.claude/reports. The broad vanadium/electrolyte search found four labels in the existing [vanadium element record](../../../data/records/vanadium.yaml); its defined bicarbonate/PIPES bioelectrochemical feed and USGS source differ from spent sulfuric-acid flow-battery electrolyte. Target DOI/title searches found no duplicate owner or study in that scope. Fourteen existing raw roots referenced by23 relevant reports were searched (314 text-like files, no missing roots/errors), with inode cycle prevention; no target match was found. Binary PDFs/images were not universally decoded, and this is not a machine-wide absence claim.

## Handoff and unresolved work

[The curated owner](../../../data/records/spent-vanadium-flow-battery-electrolyte.yaml) and canonical CREATE sidecar are ready for independent review. The JSON pins the current owner hash; a later material correction requires renewed review. No schema change or mg/kg observation import is needed: these measurements use other units and outcome definitions.

1. Independently review the full originals against the final record and save the native YAML/Markdown review bundle.
2. Obtain attributable clarification of2016 pH, concentration bases, assay/replication details and a complete phase/element balance before stronger recovery claims.
3. Resolve2024 percentage-arm assignments and charge programme from original data; distinguish replaced hardware and discarded compartments in any extended comparison.
4. Reassess the older inaccessible microbial mineral studies only through a new legitimate acquisition route. No source-exhaustion claim is made.

No corrective notice was identified in the bounded exact-source searches and inspected publisher material. This does not establish that none exists. This dossier is a source assessment, not independent scientific acceptance. Raw artifact hashes and JSON parsing were checked when saved; final corpus and provenance gates remain separate.
