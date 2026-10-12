# Enargite carbon-source investigation and next-study handoff

UTC: 2026-10-12T11:46:58.514599+00:00. Investigator: Codex `/root`, GPT-6. Worktree `/private/tmp/CMMMech-expansion-round56-20261012`; base `934bb36319e857321840c0ae145664ca6910c382`. This is a source-discovery handoff, not a completed scientific review.

**No record or history change.** The complete official supplement for [Oyama and Okibe2025](https://doi.org/10.1016/j.jece.2025.116581) was acquired, but the main methods and graphics remain unavailable through the checked routes. The newer [2026 two-stage study](https://doi.org/10.3390/pr14060923) was newly acquired for subsequent complete assessment. These sources are not imported as measurements or mechanisms in this batch.

## Acquisition and verification

The paired [JSON](20261012T114658Z-source-investigation.json) preserves exact requests, timestamps, status/content signatures, source metadata, searches and external artifact hashes. Publisher HTML and PDF routes returned403 challenge HTML. Elsevier's public API returned200 but only2054bytes of metadata, despite its full-text-retrieval-response root and open-access flag. Crossref and OpenAlex identify the2025 DOI, title and authors; OpenAlex's open-access status supplies no repository original. A named Kyushu institutional route for the2020 predecessor timed out. That timeout does not prove the file is absent.

The official PII-specific supplement endpoint was inferred, then its actual DOCX title verified. Original SHA256: `630ec7467c52f06fba080d95128f96f95e07bda1a17a6c8380bb2c50dc2f0710`. All extracted captions and four embedded original figures were inspected. FiguresS1–S3 show separate carbon-dose trajectories for A-p, B-p and B-g, including dissolved metals, pH, redox potential, ferrous iron, immobilized arsenic and planktonic density. Their caption reports duplicate cultures. Dose-specific outcomes cannot be generalized across carbons.

FigureS4 contains a material internal inconsistency: the caption states that fitting duration was extended while R² remained above0.96, but all displayed R² values are below0.96 (0.842–0.944). The missing main may help explain this difference; the discrepancy must remain explicit. The supplement alone cannot establish feed identity, culture authentication, matching abiotic controls, carbon characterization or purified-product recovery. No numerical endpoint is accepted into a record.

## Ownership and search limits

The existing [enargite-pyrite concentrate](../../../data/records/enargite-pyrite-concentrate.yaml) remains unchanged. Complete2025 methods must establish whether its feed belongs to that owner before an EDIT or justified new owner. A separate paper or carbon dose does not define another resource. The2021 chalcopyrite/enargite feed is curated separately in this batch.

Dedup searched current and original checkouts' records, research, reviews and history and206 available referenced raw/research roots using `rg --hidden --no-ignore --follow`. Hidden/ignored files and relevant symlinks were included. The receipt lists21 unavailable regex-derived root candidates, some potentially file stems rather than actual directories; none is silently counted as searched. Available text and extracted text were searched; unextracted binary graphics and unrelated home/temp trees were outside scope. Matches include the existing owner and prior deferred2025 lead. This is no machine-wide or literature-wide absence claim.

Exact DOI/title and correction/erratum/retraction searches used the first returned web result sets without pagination or a recency filter. No affecting notice was found in those bounded results, and the fetched Crossref payload has no update-to/updated-by value. Publisher notice history remains unavailable; absence is not established.

## Acquired next candidate

The official original PDF and XML for [A Two-Stage Hybrid Bioleaching Process for Selective Copper Extraction from Low-Grade, High-Arsenic Enargite Concentrates](https://doi.org/10.3390/pr14060923) are retained outsideGit. The XML verifies DOI10.3390/pr14060923. Initial materials/methods distinguish a purified electrode fraction, an enriched fraction for chemical experiments and a flotation concentrate for biological experiments. These material boundaries require complete assessment against existing owners.

Only metadata and initial materials/methods text were triaged here; all figures/tables, full methods/results, supplementary inventory and notices still need scientific review. The full original's availability is an acquisition result, not evidence acceptance. Priorities are to assess exact feed identity, culture and matched controls, staged reaction conditions, denominators, arsenic fate and laboratory versus cost-scenario claims before any curation.

## Follow-up and validation scope

Acquire the complete2025 main through a legitimate public or licensed route, bind all source components and resolve the S4 discrepancy. Independently assess the newly acquired2026 study in the next curation batch. Raw originals remain outsideGit; no author contact or access-control workaround was used. No record/history event was invented for this unchanged outcome, and no named-record validation or independent acceptance is claimed for this dossier.
