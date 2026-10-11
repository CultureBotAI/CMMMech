# Round 22 photovoltaic waste source assessment

Created 2026-10-11T13:14:21Z by codex (GPT-6; codex). Base `b19103bb393096e405bbecd2808a1aa0e01bb200`; worktree `/private/tmp/CMMMech-expansion-round22-20261011`, branch `curate/cmm-expansion-round22-20261011`. Author assessment; independent record review remains required.

## Scope and selection

The accepted identity is [end-of-life crystalline-silicon photovoltaic modules](../../data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml), including separated cell fractions while preserving the actual feed in each experiment. CdTe/CIGS thin-film modules, manufacturing scrap of unknown origin, constituent elements, and generic electronic waste are distinct. The selected primary study uses a real Hyundai m-Si module-derived acid extract in a sludge-inoculated microbial fuel cell. It supports a narrower claim than direct bioleaching or complete module recycling. No criticality list designation is asserted; constituent designations are not inherited.

## Search and acquisition

Exact queries, acquisition times, failures and SHA-256 checksums are in the [paired JSON](round22-pv-sources-20261011.json). Web searches ran on 2026-10-11 UTC with the first returned result set and no pagination; exact individual query times were not retained. Queries covered photovoltaic waste bioleaching, silver recovery, the four study identifiers, controls, corrections/retractions, and legitimate repository access. Publisher full text, PubMed and Crossref were checked where available. Correction/retraction queries and the acquired Crossref `update-to` fields did not identify a notice for the selected study within these routes; this is bounded coverage, not proof of universal absence.

Initial shell downloads failed DNS resolution in the restricted environment. Approved network acquisitions then returned actual full publisher HTML and PDFs, verified by PDF parsing (12 and 14 pages). Their final Springer URLs include a `cookies_not_supported` query, but the bodies are the actual articles, not challenge placeholders. A web-tool SI request returned an internal error; direct download subsequently acquired a valid DOCX ZIP. No login, payment or author contact occurred.

Hidden and ignored files and relevant symlinks were included using `rg --no-ignore --hidden --follow` across `data`, `research`, `reviews`, `history`, and the cited `/private/tmp/cmm-round10-ti-zr-raw` artifacts. The only initial photovoltaic hit in repository scientific files was a titanium-dioxide solar-cell synthesis URL, which does not describe PV waste recovery. DOI/experiment searches found no existing accepted PV recycling record in those bounds before this addition. The new raw directory was also inspected directly. Other unrelated home/temp trees and image binary contents were outside the textual dedup search; this is not a machine-wide absence claim.

## Candidate inventory

| Study | Evidence actually inspected | Decision |
|---|---|---|
| [Kanellos et al., DOI 10.1007/s12649-023-02128-1](https://doi.org/10.1007/s12649-023-02128-1) | Full publisher HTML and 12-page PDF; Methods, all R1–R4 results, Figures 5–10 visually inspected | Curate real-leachate cathode deposition, with controls and product limits |
| [Pang et al. 2026, DOI 10.1007/s43979-026-00160-3](https://doi.org/10.1007/s43979-026-00160-3) | Main methods/PV-related results; full acquired SI texts S1–S3 and tables; Figures S1–S2 visually checked | Defer direct-PV mechanism pending feed and denominator reconciliation |
| [Lin et al. 2024, DOI 10.1016/j.wasman.2024.10.031](https://doi.org/10.1016/j.wasman.2024.10.031) | PubMed metadata/abstract, indexed publisher introduction and section excerpts; Crossref | Defer until full methods, results and SI available |
| [Pang et al. 2025, DOI 10.1016/j.seppur.2024.128999](https://doi.org/10.1016/j.seppur.2024.128999) | Publisher metadata/abstract and Crossref | Defer until full main/SI available |
| [Theocharis et al. 2022, DOI 10.1007/s12649-022-01754-5](https://doi.org/10.1007/s12649-022-01754-5) | Publisher subscription preview, abstract and metadata | Upstream chemical-processing context; no microbial claim |
| [Kanellos preprint, DOI 10.21203/rs.3.rs-2337564/v1](https://doi.org/10.21203/rs.3.rs-2337564/v1) | Crossref relationship and search metadata | Earlier version of accepted study, not another experiment |

## Accepted claim and scientific boundaries

Kanellos appeared online on 11 April 2023 and in volume 15, pages 75–86, January 2024. Its Methods (pp. 77–78) explicitly report the used Hyundai m-Si source, thermal separation and nitric-acid leaching before R4 treatment. Sludge-derived living biomass is confined to the glucose-fed anode; panel-derived catholyte and cathode deposition are separate. No taxon identifier is invented for the unresolved sludge community.

The curated record retains the actual 70/140 mL chambers, 30 degrees C operation, 100-ohm resistor, pretreated pH 1.5 leachate, fresh graphite cathodes and two consecutive seven-hour R4 batches. It distinguishes these from independent reactor replication and from synthetic single-metal R1–R3 comparators. AAS tracks dissolved metals; SEM-EDS and XRD characterize electrode deposits. It does not invent a matched sterile/open-circuit control, a whole-module denominator, an AAS detection limit or a weighed purified product.

Figures 7 and 9 support silver solution depletion and silver-bearing deposits. Local EDS percentages are not the separate solution-derived bulk-purity estimate. Crucially, Figure 5's carbon-paper trace contains the same labelled diffraction positions used for the authors' fcc-silver assignment. The record therefore preserves the authors' assignment as uncertain rather than independently certifying the phase. EDS elemental signals cannot by themselves prove particular oxide species. Table 1's silicon-dominated percentage composition is not reconciled with aqueous R4 concentrations and is not used as an extraction denominator. Slower real-feed silver removal, incomplete Cu/Al removal and proposed passivation remain explicit. No industrial deployment or reusable solar-grade silver product is demonstrated.

The publisher displays CC BY 4.0 with the usual third-party-material qualification. No supplementary-material link was found in a full href search of the acquired HTML; the paper says data are available on request. Raw papers remain outside the repository. No concentration observations are imported: the source does not provide the exact dated mg/kg elemental cells required by the native contract.

## Deferred direct-bioleaching evidence

Pang 2026's main Methods 2.2 add 500 mg silver powder to 250 mL medium. That model is not a waste-module assay merely because the title refers to PV cells. SI Text S1 and Figure S2 do report a separate cell-feed multimetal experiment, but feed provenance and pretreatment are unclear. S1 gives Ag at 2.13% whereas S3 gives 10,980 mg/kg. S3 uses a 2 g PV-cell batch, while Table S3 lists 1 g/L. These might describe distinct fractions or experiments, but the source does not reconcile them; the main liquid volume cannot silently be imposed on the SI assay. The reported 83.5% is based on decreased solid Ag concentration without a displayed closed mass balance. The economic calculation assumes a 95% reduction in reagent cost and excludes collection, transport, crushing/separation and final refining. It is not industrial validation.

The SI names no strain accession for its mixed culture; genus-level community enrichment and amino-acid/DFT associations do not independently prove each proposed causal step. Its Table S3 describes Lin 2024 as Pseudomonas fluorescens, but this secondary description is not a substitute for that paper's unavailable primary Methods. Pang 2026 reference 17 prints article number 128998 while its linked DOI and the publisher for the earlier Pang paper use 128999; the DOI identifies one study, not two.

Lin 2024 full text remains unavailable after publisher access and bounded title/DOI/repository searches. A publisher web open returned an internal error; PubMed PMID 39499967 supplies metadata and abstract only. Pang 2025 likewise remained at abstract/metadata level. Claims about their yields, cultures and controls are not accepted from snippets. Neither paper is rejected as scientifically false; the missing evidence is concrete follow-up work. Their reuse licenses were not established.

## Priorities and handoff

1. Independently review the accepted record and actual [CREATE sidecar](../../history/records/end-of-life-crystalline-silicon-photovoltaic-modules/2026-10-11T131218Z-codex-f1d8d9.yaml) against the final bytes and the acquired Kanellos full text. Single-file validation passed (`Checked 1 record(s); 0 failed.`); batch gates remain root-owned.
2. Reconcile Pang 2026's actual PV feed, pretreatment, loading, silver inventories and yield denominator. Main and SI are available locally, so acquisition is no longer the blocker.
3. Acquire Lin 2024 and Pang 2025 full main/SI through legitimate author or institutional access, then inspect organism, controls and actual used-cell provenance before extending the same material record.
4. Obtain raw Kanellos diffraction/blank and deposit-mass data before strengthening phase/purity or recovery-yield claims; seek matched abiotic/open-circuit comparisons.
5. Search CdTe/CIGS feeds independently. This c-Si pass makes no exhaustive claim about other technologies or all remaining CMMs.

## Artifacts and reproducibility

The paired JSON records raw acquisition receipts, hashes and the selected target's SHA-256. Retained files are under `/private/tmp/cmm-round22-pv-raw`; raw copyrighted artifacts are not committed. A timestamped source-skill report is saved at [`research/sources/round22-pv/20261011T131421Z.md`](../../research/sources/round22-pv/20261011T131421Z.md). This dossier is not the separate independent scientific verdict.
