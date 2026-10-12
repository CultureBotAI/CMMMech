# Clay-recovery source investigation: complete supplements, unavailable main articles

## Scope and provenance

UTC: 2026-10-12T11:14:59.660179+00:00. Investigator: Codex `/root/round43_hardmetal`, GPT-6.
Worktree: `/private/tmp/CMMMech-expansion-round55-20261012`; branch `curate/cmm-expansion-round55-20261012`; base `19d0972767b266f86a256a3f36f0f7177ab4cf25`.
This is a source assessment under the add-record/discover-source contracts, not a scientific acceptance review.

**Decision: defer; no record or history change.** Complete official supplements were newly acquired for Han 2026 and the named alternate Zhao 2025. Their main methods and graphics remain unavailable through the bounded routes checked. Metadata and supplements cannot establish the missing controls, feed provenance or outcome denominators. Shen 2023 was checked at metadata level only; this pass did not expand into another curation attempt.

## Search, acquisition and deduplication

The paired [JSON](20261012T111459Z-source-investigation.json) records exact queries, original URLs, acquisition times, response types, failures and 72 external artifact hashes. Search results were first returned sets only, without pagination or recency filters; institutional exact-title searches were bounded. The raw originals and search responses remain under `/private/tmp/cmm-round55-clay-recovery-research`.

| Route | Observed result on 2026-10-12 UTC | Limit |
| --- | --- | --- |
| Han 2026 publisher and public Elsevier API | Publisher 403; API 200 but only 1946 bytes of metadata | An API root named full-text-retrieval-response is not a complete article |
| Han 2026 title/DOI, institutional and author searches; OpenAlex | Indexed snippets; ResearchGate requests full text; OpenAlex marks closed and supplies no repository PDF | Main methods and figures not acquired or inspected |
| Official Han 2026 PII supplement | DOCX 200, 47,096,562 bytes; complete XML, 10 tables, 7 embedded figures | Supplement adds evidence but does not replace the main article |
| Zhao 2025 publisher/author metadata and SSRN 5139166 | Matching title/author set; SSRN landing and public delivery 403; OpenAlex closed | No full published or preprint article, no version comparison |
| Official Zhao 2025 PII supplement | DOCX 200, 1,935,070 bytes;2 tables and 2 figures | No title/author cover; main unavailable to corroborate the complete supplementary inventory |
| Crossref Zhao 2025 | First request 429; one later request 200 | Original failure receipt retained; no claim that the failed request succeeded |
| Shen 2023 | DOI/title/author metadata and closed OpenAlex location | Retained as a source lead only |

The official supplement endpoints were inferred from the verified publisher PIIs, then their actual contents and formats checked. Han's cover matches all five unique authors and the article title. Zhao's supplement has no bibliographic cover; its PII and experimental topic bind it provisionally to the publisher article, with that limit retained. Both are ZIP DOCX files, not disguised HTML. LibreOffice produced local PDFs for inspection; these are derivatives, not publisher PDFs. The original DOCX bytes are preserved.

Dedup used `rg --no-ignore --hidden --follow` across current and original checkouts' records, research, reviews and history, then 202 existing referenced raw/research/evidence roots. It read 4216 metadata files; nine missing referenced roots and the full command list are in JSON. Hidden/ignored files and relevant symlinks were included. Binary originals were not all decoded for textual dedup; unrelated home/temp trees were excluded. Existing natural clay, prepared leach residue and LanM element/commodity records were found. Zhao 2025 and Shen 2023 were already deferred in earlier dossiers; newly acquired supplements are progress in access, not new independent experiments.

## Candidate evidence and boundaries

### Han 2026: LanM-displaying cells and clay-derived leachate

[Han and colleagues, DOI 10.1016/j.jece.2026.123113](https://doi.org/10.1016/j.jece.2026.123113), Journal of Environmental Chemical Engineering 14(3),123113, June2026, is a primary engineered-cell recovery lead. Crossref and the original supplement identify Zebin Han, Zhu Chen, Guanzhou Qiu, Li Shen and Hongbo Zhao. Affiliation rows and automated author profiles are not additional authors or verified identities.

The complete extracted supplement text, all 10 tables and captions were read. All seven original figures were visually inspected on local rendering pages 14–20; Tables S2 and S10 were also viewed on pages 4 and 12. Remaining rendering pages were not individually viewed, and no main-figure inspection is claimed. Table S1 distinguishes host, empty vector, intracellular LanM and displayed Lpp-OmpA-LanM constructs. It does not authenticate a strain accession.

Table S2 labels the liquid bio-leachate while describing 0.1 M sodium gluconate, 2.5 wt% pulp and 2 h leaching. That caption does not demonstrate microbial production of the lixiviant. Figure S3's biomass-dose optimization and Figure S7's declining reuse experiment use different OD conditions. Neither is sufficient to infer purified-product yield, industrial deployment or a general regeneration advantage. The missing main is needed to resolve feed identity, culture/adsorption controls, reaction conditions, biomass basis, separation and regeneration methods. Fitted kinetic/isotherm quantities must remain separate from measured uptake and product recovery.

Original supplement SHA256: `451fe5e54fe6a9f93bdd96543ddade8d2add87d6111a9aef9b0c1a8ebfd1ef0d`.

### Zhao 2025: a potential existing-clay extension

[Zhao and colleagues, DOI 10.1016/j.jenvman.2025.125422](https://doi.org/10.1016/j.jenvman.2025.125422), Journal of Environmental Management 382,125422, May2025, has the same title and author set as [SSRN 5139166](https://doi.org/10.2139/ssrn.5139166). The preprint metadata reverses the first author's name as Zhao Yu. This supports likely related versions, not two independent experiments; exact version and experimental overlap remain unverified without the originals.

All supplement text, tables and both local rendering pages were inspected. Tables S1–S2 distinguish water-soluble and colloidal sediment inventories. Figure S1 shows fungal adsorption and Figure S2 shows FTIR/Raman spectra before and after biosorption. These do not provide the missing strain provenance, full feed inventory, culture/leach conditions, controls or mass balance. The adsorption-ratio axis alone does not establish its denominator. No numbers or mechanisms were imported into a record.

Original supplement SHA256: `458167aa10b55f0813211709c5435a5ec97312a93e4ddc66fe1c738f187ee29c`.

### Ownership and supporting-source limits

The [natural ion-adsorption clay](../../../data/records/ion-adsorption-rare-earth-clay.yaml) and [laboratory-prepared salt-leach residue](../../../data/records/ion-adsorption-rare-earth-leach-residue.yaml) already have distinct owners. The 2026 aqueous leachate is not automatically that residue, an element, a mineral species or a purified rare-earth product. A new leachate owner requires verified preparation/composition and useful conceptual distinction; the 2025 natural-clay study would most likely extend the existing clay owner after full review.

Existing purified-LanM studies concern different systems from the displayed live cells in this lead. They cannot supply its missing controls. No criticality, taxon identifier, enzyme causality or deployment claim was added. [Shen 2023 DOI 10.1016/j.hydromet.2023.106019](https://doi.org/10.1016/j.hydromet.2023.106019) remains a metadata-only comparison lead; its abstract is not accepted evidence.

## Priorities, notices and checks

1. Acquire the complete Han 2026 original through legitimate publisher/author access. Inspect all main methods, figures and tables; resolve chemical-versus-biogenic feed, matched host/vector/abiotic controls, adsorption-versus-product outcome, and regeneration. The complete supplement makes these review questions concrete.
2. Acquire Zhao 2025 and, if available, its SSRN version; compare experimental identity and matched controls before considering an EDIT to the existing clay record. Do not count the preprint, article and supplement separately.
3. Retain Shen 2023 for later full-primary acquisition; do not import missing methods or measurements.

Exact-DOI correction/retraction/erratum queries identified no notice in the returned sets, and the fetched Crossref payloads contain no update-to/updated-by values. The inaccessible complete publisher notice history prevents an exhaustive absence claim. This pass did not contact authors, request files from third-party document-sharing services or use access-control workarounds.

Raw copyrighted sources and derivatives remain outside Git. Crossref's TDM/STM policy links do not establish open bulk-redistribution rights; supplement redistribution rights remain unresolved. Publication month, metadata creation/deposit dates and this session's acquisition date remain separate in JSON. No schema changes or named-record validation were necessary because this investigation changed no record. This report is a curation handoff, not independent scientific acceptance or a claim that parent-owned batch gates have run.
