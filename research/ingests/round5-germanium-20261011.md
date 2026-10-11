# Germanium curation handoff — 11 October 2026 UTC

Created `data/records/germanium.yaml` in the isolated round-five worktree,
against trusted base `e305dcc67e526e585349c60f849567f4c2bfc835`. The selection
adds element-specific primary microbial evidence to an identified coverage gap.
This is curation provenance; the independent acceptance review is separate.

The [machine-readable dossier](round5-germanium-20261011.json) records exact
queries, search boundaries, source locators, access failures, retained-file
checksums, download completion times and deferred candidates. Raw files remain
outside Git in `/private/tmp/cmm-round5-germanium-20261011`.

## Identity, criticality and deduplication

Live [ChEBI CHEBI:30441](https://www.ebi.ac.uk/chebi/CHEBI:30441) identifies
the neutral germanium atom. The legacy `searchId.do` entry resolved successfully
after direct web-tool access failed. The explicit Germanium row in the
[USGS final 2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
supports only the stated United States edition and commodity mapping.
[NCBI Taxonomy 303](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=303&mode=Info)
is a species identifier, not the experimental strain accession.

Hidden and ignored files were included in searches of records, research,
reviews, history, the cited authority download directories, and this task's
downloads. Earlier germanium matches were list inventories and priorities;
neither primary DOI nor a germanium record was found before this addition.
This is a bounded repository/download finding, not a machine-wide or exhaustive
literature absence claim. A broad temporary-directory instruction search was
stopped without drawing an absence conclusion.

## Accepted source inspection

- [Chmielowski and Kłapcińska 1986](https://doi.org/10.1128/aem.51.5.1099-1103.1986):
  full publisher PDF text inspected; PMC scan pages 1100–1102 visually checked,
  including all four kinetic figures. Methods and the concluding discussion
  establish the scope retained in the record.
- [Kłapcińska and Chmielowski 1986](https://doi.org/10.1128/aem.51.5.1144-1147.1986):
  full publisher PDF text and all four PMC scanned pages inspected, including
  Table 1 and microscopy controls in Figures 1–3. This is a companion study,
  not an independent replication of the kinetic experiment.

The record keeps the two assay concentrations distinct, represents accumulation
under `process: other`, and preserves the proposed nature of transport causality.
It makes no mineral-phase, redox, isolated-product or deployment claim.
No quantitative observation objects were manufactured from incompatible source
units or missing sample analysis dates.

## Acquisition and remaining evidence

The primary publisher PDF text was available through the web tool. Direct PDF
downloads returned 403 responses; the PMC PDF endpoint returned an HTML download
interstitial despite status 200. These are explicitly failed PDF acquisitions.
Initial Python/subprocess and sandbox scan downloads failed DNS resolution;
network-enabled retrieval then obtained the legitimate PMC scan images.
The receipts use actual file completion times and distinguish every retained
artifact. ASM copyright is stated on both papers; no redistribution license was
established, and third-party full text is not committed.

Exact-title correction/retraction searches returned no relevant notice within
the default results inspected. No supplemental links were observed in the
inspected primary pages. Neither finding implies comprehensive absence.

Van Dyke et al. 1989, DOI `10.1007/BF00425482`, is a useful strain-heterogeneity
and intervention-control lead, but its tables need independent inspection
before expansion. Rezaei et al.'s coal-fly-ash spent-medium study was found through
publisher snippets; complete methods and supplements remain unacquired. A brown
coal proceedings lead also lacks verified original acquisition. These stay
deferred rather than supplying accepted leaching or recovery claims.

## Handoff

Canonical CREATE history was generated using `just new-history` with actual
Codex/GPT-6/Codex metadata and linked separately from the inline event:
`history/records/germanium/2026-10-11T051803Z-codex-f9b5f3.yaml`.
Single-record validation passed before and after history linkage. Batch checks,
independent saved review, publication and final hash coverage are parent-owned.

The independent review
`20261011T052122Z-germanium-round5-independent` found one minor wording defect
(F1; `germanium-analytical-replication-scope`; GitHub issue 30). The correction
preserves the reported two analytical aliquots while narrowing the unknown to
biological replication and statistical uncertainty. It has a distinct EDIT
sidecar, `history/records/germanium/2026-10-11T052259Z-codex-64cadc.yaml`, and
inline event. The CREATE sidecar is unchanged; the parent owns the independent
successor review and issue disposition.
