# Independent scientific review of zinc expansion record

- Review: 20261011T042418Z-zinc-round2-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:21:55Z
- Finished UTC: 2026-10-11T04:24:18Z
- Reviewer: Codex /root/cmm2_silver (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Zinc identity, dated US designation and conditional laboratory bioleaching are supported. Matched-control null outcomes and the primary figure/prose discrepancy are retained. No actionable findings in this exact reviewed state.

## Scope And Provenance

All scientific fields and linked current CREATE provenance in the new zinc record.

Selection: Assigned named record; full review of one record rather than a sample from the corpus.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 268498d0a9748f3a18955e35f175f67115f88b97.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:zinc | data/records/zinc.yaml | maintained | Zinc |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict zinc record validation | passed | True | cmmmech:zinc | One record checked, zero failed. |
| History validation against trusted base | passed | True | cmmmech:zinc | 26 history sessions checked, zero errors. |
| Native batch validation | passed | True | cmmmech:zinc | 307 passed, 3 existing skips; lint passed; 17 records and 26 histories valid. |
| Nonempty corpus validation | passed | True | cmmmech:zinc | Parent reports 17 records checked, zero failures after current four-record curation. |

## Scientific And Domain Assessments

### Element grounding, organism scope and dated designation

identity: supported. Targets: cmmmech:zinc.

Record identity and scoped mappings are supported by issuing authorities.

### Controlled dissolution, null outcomes and inference limits

evidence: supported. Targets: cmmmech:zinc.

The positive and null laboratory observations are represented without universal microbial superiority or isolated recovery claims.

The existing figure/prose caveat is justified by independently inspected figures. The record does not normalize a universal ferrous threshold. Surface/model evidence supports an interpretation, not a demonstrated unique enzyme or direct lattice oxidation pathway.

### Working bytes, history and validation

provenance: supported. Targets: cmmmech:zinc.

The record and sidecar hashes were captured before assessment; actual current curation and structural checks are consistent. No edits to zinc were made by the reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/zinc.yaml; Entire file and linked CREATE sidecar | supports | Exact inspected hash, current actor/model/time and target attachment agree with this new curation; inline event and canonical sidecar remain distinct. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:27363; Displayed ID, label, formula, charge and IUPAC synonym | supports | Live authority resolves neutral zinc atom, Zn, and atomic-number-30 synonym; not Zn(II), sphalerite or concentrate. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Current name, rank and homotypic synonym | supports | Live page confirms Acidithiobacillus ferrooxidans species and historical Thiobacillus name. The record expressly limits this to nomenclatural mapping rather than proof of an FC1 genome assignment. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 notice; complete commodity list and zinc table row on page 50497 | supports | Zinc belongs to the final US 2025 commodity list; the record specifies jurisdiction, list, edition and commodity-to-element mapping. |
| primary1999 | https://journals.asm.org/doi/10.1128/AEM.65.12.5285-5292.1999; Materials and Methods; Results; Figures 2-6 captions; Discussion and model sections | supports | Publisher full text independently inspected. FC1, washed concentrate, controlled iron chemistry, reactor conditions and filtrate zinc assay support conditional dissolution. Early null interval, later enhancement and surface evidence are scoped without enzyme or recovered-product claims. |
| figures1999 | https://journals.asm.org/doi/10.1128/AEM.65.12.5285-5292.1999; Figures 2, 3, 5 and 6; retained original JPEGs in /private/tmp/cmm-round2-zinc-20261011 | partial | Independently viewed curator-acquired images after checksum verification. The 1 g/L paired series deviates at later times despite the sharp low-ferrous boundary in Discussion; record already preserves this uncertainty. SEM/EDAX shows surface differences without proving sulfur oxidation state or enzyme causality. |
| primary1998 | https://journals.asm.org/doi/full/10.1128/aem.64.10.3570-3575.1998; Methods; Results; Figures 4-6 captions; Discussion | supports | Independently read full primary text. Controlled low-ferrous comparison reports broadly similar chemical and bacterial dissolution; it bounds rather than universally refutes the later conditional mechanism. |
| fig6_1998 | https://journals.asm.org/cms/10.1128/AEM.64.10.3570-3575.1998/asset/7705d194-3867-431c-b2a2-dd7a71cef60f/assets/graphic/am1080611006.jpeg; Figure 6 axes, series and equality line | supports | Fresh image retrieved and visually inspected independently. Most comparisons follow the equality line with late scatter; no formal equivalence or numerical effect size is inferred. No points digitized. |
| search | Live web searches and local rg; First returned unfiltered web results; scoped recursive local search | context_only | No affecting correction/retraction notice surfaced in this bounded search. Companion null study inspected. Local results identify this zinc record and its new dossier/history, not another root zinc identity. |

## Limits And Additional Notes

- The 1999 figure/prose discrepancy and uncertain biological replication remain scientific limitations, explicitly retained in the record.
- Neither sulfur mass balance nor a specific causal enzyme is established; no new quantitative effect estimate, curve digitization or industrial extrapolation was performed.
- The 1998 Figure 3 caption differs from its Methods on iron concentrations; that current trace is not the curated null evidence. Figures 4-6 and Methods support the scoped comparison.
- Full-text publisher pages were inspected through web tools; raw publisher HTML was not downloaded by this reviewer. Original 1999 images were acquired by the curator and independently inspected; 1998 Figure 6 was freshly retrieved.
- No exhaustive correction/retraction or worldwide-material search was performed; uninspected follow-up literature is not silently treated as evidence.
- No zinc corrections were needed within this review scope. Empty findings is not a corpus-wide pass.
- Reviewed working-tree revision is the main-history ancestor 268498d0a9748f3a18955e35f175f67115f88b97; the four new records remain uncommitted at inspection.
- 1999 image SHA-256: Figure 2 c9b8073f603a5bb9a93d058ebee6d109da6edfa937f4b3ba893eef9b72314bb4; Figure 3 2d5c64baf75355a9f016c98b501480be1cd0659de4f069c3612a43b99b203d08; Figure 5 a7b4f666ee07b6b3ed7038a34577969c60657c4d5b5ffa9ade076459570c1278; Figure 6 de84818f77a59e7f8e0b3de1cd82e1c7ffc37e37bdce74879fbc4a15d6912e97.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T042418Z-zinc-round2-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of zinc expansion record
started_at: '2026-10-11T04:21:55Z'
finished_at: '2026-10-11T04:24:18Z'
reviewer:
  identity: Codex /root/cmm2_silver
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer curated silver, did not write or edit zinc record/history,
    captured final target bytes before assessment and independently checked primary
    full texts, figures and authority pages.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Zinc identity, dated US designation and conditional laboratory bioleaching
  are supported. Matched-control null outcomes and the primary figure/prose discrepancy
  are retained. No actionable findings in this exact reviewed state.
source:
  git_revision: 268498d0a9748f3a18955e35f175f67115f88b97
  state: working_tree
  inputs:
  - path: data/records/zinc.yaml
    sha256: b4ffa0a1ea5ad265868ca3bbc5e3103193dd67f81e21350b33a91a63dbcd3e9a
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/zinc/2026-10-11T042052Z-codex-227643.yaml
    sha256: 67976a8ea0a011e6d655dc1bf68543c25daa178d726513690591af282d418bf0
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:zinc
  path: data/records/zinc.yaml
  label: Zinc
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc.yaml
    role: maintained scientific record
scope:
  description: All scientific fields and linked current CREATE provenance in the new
    zinc record.
  selection: Assigned named record; full review of one record rather than a sample
    from the corpus.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:zinc
checks:
- check_id: record
  name: Strict zinc record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/zinc.yaml
  status: passed
  required: true
  summary: One record checked, zero failed.
  target_ids:
  - cmmmech:zinc
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: History validation against trusted base
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base 268498d0a9748f3a18955e35f175f67115f88b97
  status: passed
  required: true
  summary: 26 history sessions checked, zero errors.
  target_ids:
  - cmmmech:zinc
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native batch validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 307 passed, 3 existing skips; lint passed; 17 records and 26 histories
    valid.
  target_ids:
  - cmmmech:zinc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Parent executed on this four-record working state; reviewer independently
    read /private/tmp/cmm-round2-check.log and verified zinc hash remained unchanged.
- check_id: nonempty
  name: Nonempty corpus validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  status: passed
  required: true
  summary: Parent reports 17 records checked, zero failures after current four-record
    curation.
  target_ids:
  - cmmmech:zinc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Actual parent execution reported in session; not an independent re-execution
    by this reviewer.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/zinc.yaml
  locator: Entire file and linked CREATE sidecar
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Exact inspected hash, current actor/model/time and target attachment agree
    with this new curation; inline event and canonical sidecar remain distinct.
  snapshot_sha256: b4ffa0a1ea5ad265868ca3bbc5e3103193dd67f81e21350b33a91a63dbcd3e9a
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27363
  locator: Displayed ID, label, formula, charge and IUPAC synonym
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Live authority resolves neutral zinc atom, Zn, and atomic-number-30 synonym;
    not Zn(II), sphalerite or concentrate.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Current name, rank and homotypic synonym
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Live page confirms Acidithiobacillus ferrooxidans species and historical
    Thiobacillus name. The record expressly limits this to nomenclatural mapping rather
    than proof of an FC1 genome assignment.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 notice; complete commodity list and zinc table row on page 50497
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Zinc belongs to the final US 2025 commodity list; the record specifies
    jurisdiction, list, edition and commodity-to-element mapping.
- evidence_id: primary1999
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/AEM.65.12.5285-5292.1999
  locator: Materials and Methods; Results; Figures 2-6 captions; Discussion and model
    sections
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Publisher full text independently inspected. FC1, washed concentrate, controlled
    iron chemistry, reactor conditions and filtrate zinc assay support conditional
    dissolution. Early null interval, later enhancement and surface evidence are scoped
    without enzyme or recovered-product claims.
- evidence_id: figures1999
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/AEM.65.12.5285-5292.1999
  locator: Figures 2, 3, 5 and 6; retained original JPEGs in /private/tmp/cmm-round2-zinc-20261011
  accessed_at: '2026-10-11T04:24:18Z'
  support: partial
  summary: Independently viewed curator-acquired images after checksum verification.
    The 1 g/L paired series deviates at later times despite the sharp low-ferrous
    boundary in Discussion; record already preserves this uncertainty. SEM/EDAX shows
    surface differences without proving sulfur oxidation state or enzyme causality.
- evidence_id: primary1998
  kind: primary_source
  reference: https://journals.asm.org/doi/full/10.1128/aem.64.10.3570-3575.1998
  locator: Methods; Results; Figures 4-6 captions; Discussion
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Independently read full primary text. Controlled low-ferrous comparison
    reports broadly similar chemical and bacterial dissolution; it bounds rather than
    universally refutes the later conditional mechanism.
- evidence_id: fig6_1998
  kind: primary_source
  reference: https://journals.asm.org/cms/10.1128/AEM.64.10.3570-3575.1998/asset/7705d194-3867-431c-b2a2-dd7a71cef60f/assets/graphic/am1080611006.jpeg
  locator: Figure 6 axes, series and equality line
  accessed_at: '2026-10-11T04:24:18Z'
  support: supports
  summary: Fresh image retrieved and visually inspected independently. Most comparisons
    follow the equality line with late scatter; no formal equivalence or numerical
    effect size is inferred. No points digitized.
  snapshot_sha256: 3c448c5ebda30517167de50c0c6a6d89fb1ce5858a5ee8d346ee118fe6dd88bd
- evidence_id: search
  kind: search
  reference: Live web searches and local rg
  locator: First returned unfiltered web results; scoped recursive local search
  accessed_at: '2026-10-11T04:24:18Z'
  support: context_only
  summary: No affecting correction/retraction notice surfaced in this bounded search.
    Companion null study inspected. Local results identify this zinc record and its
    new dossier/history, not another root zinc identity.
  search_scope: 'Queries: "Leaching of Zinc Sulfide" "1999" "Fowler" PMC; same with
    1998; "10.1128/AEM.65.12.5285-5292.1999" correction retraction erratum; "Fowler"
    "Crundwell" "zinc" "contradictory" "1998". No pagination. rg --no-ignore --hidden
    --follow searched data/research/reviews/history/.claude YAML/Markdown/JSON for
    cmmmech:zinc, CHEBI:27363 and selected DOI forms; hidden/ignored included. Not
    a machine-wide or exhaustive literature search.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element grounding, organism scope and dated designation
  outcome: supported
  summary: Record identity and scoped mappings are supported by issuing authorities.
  target_ids:
  - cmmmech:zinc
  evidence_ids:
  - record
  - chebi
  - taxon
  - criticality
  dimensions:
  - name: material
    value: Element Zn, distinct from Zn(II), ZnS, sphalerite and concentrate.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - record
    - chebi
  - name: criticality
    value: United States, USGS final 2025 list, published 7 November 2025.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - criticality
  - name: organism
    value: Species-level historical-name mapping; experimental strain FC1 retained
      without unsupported strain accession.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - taxon
    - primary1999
- assessment_id: mechanism
  area: evidence
  topic: Controlled dissolution, null outcomes and inference limits
  outcome: supported
  summary: The positive and null laboratory observations are represented without universal
    microbial superiority or isolated recovery claims.
  target_ids:
  - cmmmech:zinc
  evidence_ids:
  - record
  - primary1999
  - figures1999
  - primary1998
  - fig6_1998
  dimensions:
  - name: biomass
    value: Living FC1; analytical repeatability distinguished from biological replication.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - primary1999
    - record
  - name: substrate
    value: Sodium-sulfide-washed Gamsberg sphalerite concentrate, 45-53 micrometres.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - primary1999
  - name: conditions
    value: Aerated stirred 2 L electrolysis-controlled assay, pH 1.6, 35 degrees C,
      5 g/L solids.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - primary1999
  - name: controls
    value: Matched dissolved iron conditions with microscopy-checked sterile runs;
      1998 null retained.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - primary1999
    - primary1998
  - name: outcome
    value: Filtrate zinc dissolution with conditional late enhancement; no isolated
      zinc yield.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - primary1999
    - record
  - name: deployment
    value: Laboratory only; commercial feed provenance is not process deployment.
    definition: Experiment and identity scope supported by the cited evidence, without
      extension to untested entities.
    evidence_ids:
    - record
    - primary1999
  details: The existing figure/prose caveat is justified by independently inspected
    figures. The record does not normalize a universal ferrous threshold. Surface/model
    evidence supports an interpretation, not a demonstrated unique enzyme or direct
    lattice oxidation pathway.
- assessment_id: provenance
  area: provenance
  topic: Working bytes, history and validation
  outcome: supported
  summary: The record and sidecar hashes were captured before assessment; actual current
    curation and structural checks are consistent. No edits to zinc were made by the
    reviewer.
  target_ids:
  - cmmmech:zinc
  evidence_ids:
  - record
findings: []
actions: []
limitations:
- The 1999 figure/prose discrepancy and uncertain biological replication remain scientific
  limitations, explicitly retained in the record.
- Neither sulfur mass balance nor a specific causal enzyme is established; no new
  quantitative effect estimate, curve digitization or industrial extrapolation was
  performed.
- The 1998 Figure 3 caption differs from its Methods on iron concentrations; that
  current trace is not the curated null evidence. Figures 4-6 and Methods support
  the scoped comparison.
- Full-text publisher pages were inspected through web tools; raw publisher HTML was
  not downloaded by this reviewer. Original 1999 images were acquired by the curator
  and independently inspected; 1998 Figure 6 was freshly retrieved.
- No exhaustive correction/retraction or worldwide-material search was performed;
  uninspected follow-up literature is not silently treated as evidence.
notes:
- No zinc corrections were needed within this review scope. Empty findings is not
  a corpus-wide pass.
- Reviewed working-tree revision is the main-history ancestor 268498d0a9748f3a18955e35f175f67115f88b97;
  the four new records remain uncommitted at inspection.
- '1999 image SHA-256: Figure 2 c9b8073f603a5bb9a93d058ebee6d109da6edfa937f4b3ba893eef9b72314bb4;
  Figure 3 2d5c64baf75355a9f016c98b501480be1cd0659de4f069c3612a43b99b203d08; Figure
  5 a7b4f666ee07b6b3ed7038a34577969c60657c4d5b5ffa9ade076459570c1278; Figure 6 de84818f77a59e7f8e0b3de1cd82e1c7ffc37e37bdce74879fbc4a15d6912e97.'
```
