# Independent scientific review of sphalerite mineral record

- Review: 20261011T050418Z-sphalerite-round4-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:59:52Z
- Finished UTC: 2026-10-11T05:04:18Z
- Reviewer: Codex /root/cmm3_platinum (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Official sphalerite identity and conditional laboratory dissolution are supported. The record distinguishes ideal ZnS from iron-bearing concentrate, retains low-ferrous null and within-paper contradictions, and scopes the analytical fraction and study reuse honestly. No actionable defect identified.

## Scope And Provenance

Whole new sphalerite record, identifiers, evidence links, limits and CREATE provenance.

Selection: Assigned named record; all fields reviewed, not a corpus sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c081a749cd63feafcc25414f5ad006d1f78f1e36.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:sphalerite | data/records/sphalerite.yaml | maintained | Sphalerite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict mineral record validation | passed | True | cmmmech:sphalerite | 2 records checked; 0 failed. |
| History validation at trusted base | passed | True | cmmmech:sphalerite | 36 history records checked; 0 errors. |
| Nonempty corpus validation | passed | True | cmmmech:sphalerite | 27 records checked; 0 failed. |
| Completed batch gate | passed | True | cmmmech:sphalerite | 307 tests passed, 3 skipped in 47.17s; 27 records and 36 histories valid. |

## Scientific And Domain Assessments

### Mineral identity, experimental scope and conflicting evidence

evidence: supported. Targets: cmmmech:sphalerite.

Official sphalerite identity and conditional laboratory dissolution are supported. The record distinguishes ideal ZnS from iron-bearing concentrate, retains low-ferrous null and within-paper contradictions, and scopes the analytical fraction and study reuse honestly. No actionable defect identified.

### Exact working state, history and acquisition provenance

provenance: supported. Targets: cmmmech:sphalerite.

Current target and all inspection-context hashes match. Actual CREATE sidecar remains distinct from inline event, and base-aware history validation passes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/sphalerite.yaml; Entire record, actual CREATE sidecar and distinct inline event | supports | Target and context hashes captured before assessment remain unchanged. Correct current actor, target and linked sidecar; no fabricated historical authorship. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 edition; dictionary page 1, terms page 2; sphalerite row page 203 | supports | ZnS, A approved, 1980 s.p. special-procedure action. This is not an original-discovery date or sequential approval identifier. Mineral identity does not inherit elemental commodity criticality. Official PDF text independently opened; local PDF receipt rehashed. |
| taxa | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Current name, homotypic synonym and species rank | supports | NCBI resolves Acidithiobacillus ferrooxidans, with Thiobacillus ferrooxidans as a homotypic synonym. It does not establish FC1 strain identity or a modern genome-based reassignment. |
| primary | https://doi.org/10.1128/AEM.65.12.5285-5292.1999; Methods, Results, Discussion; Figures 2–6 captions | supports | Publisher full text supports FC1, washed Gamsberg feed, controlled bulk iron and filtered zinc assay. Later enhancement and surface observations support a conditional sulfur-layer interpretation, not lattice-specific enzyme action. Analytical replicates are not reactor replication. |
| null | https://doi.org/10.1128/AEM.64.10.3570-3575.1998; Methods; Results; Figures 3–6; Discussion | supports | Fixed low-ferrous, varied-ferric comparison reports broadly similar chemical and bacterial dissolution despite growth and attachment. Figure 3 conditions conflict with the main experiment; record retains this without assigning quantitative currents. This bounds the mechanism rather than proving universal absence. |
| figures | https://doi.org/10.1128/AEM.65.12.5285-5292.1999; Visually inspected 1999 Figures 2, 3, 5, 6 and 1998 Figures 4, 5, 6; rehashed original files listed in dossier | partial | 1999 1 g/L ferrous series diverges at later times, confirming tension with the sharp Discussion threshold. SEM/EDAX shows surface differences without oxidation-state proof; imaging endpoints differ. 1998 paired data lie broadly near equality with scatter, not a formal equivalence test. |
| receipts | research/ingests/round4-mineral-hosts-20261011.json; Fresh acquisition receipts and reused_artifacts | supports | Reviewer recalculated byte lengths and SHA256 for all 12 successful local assets; all matched. Raw articles/images remain outside Git. Source access limits and terms are explicit; curator acquisition is not misrepresented as reviewer acquisition. |
| search | Live web search and scoped local rg; Returned first search results; existing records, dossiers, histories and review artifacts | context_only | No target-specific correction identified among returned exact-DOI results and opened primary pages. Broader results provide conditional-mechanism leads not fully assessed here. Hidden/ignored-inclusive local results confirm distinct mineral identities and shared evidence with copper/zinc, not new independent experiments. |

## Limits And Additional Notes

- Historical FC1 identification is retained without a genomic reassignment. XRD feed purity and solid-solution interpretation do not establish pure ideal ZnS.
- Surface imaging and elemental spectra support a sulfur-layer interpretation without a direct mineral-lattice enzyme, sulfur valence determination or recovered-product purity claim. Model curves were not recomputed.
- The 1999 low-ferrous series and 1998 Figure 3 conditions conflict with broad prose claims. These unresolved source tensions remain explicitly in the record. No formal statistical equivalence or general threshold inferred.
- Both Fowler papers are from the same investigators and are already represented in zinc.yaml; the 1999 model reuses 1998 data. This is additional mineral identity coverage, not independent experimental replication.
- Source/correction search is bounded. Newer studies remain unverified extension leads; this review does not claim the literature contains no contrary result.
- No record corrections required; empty findings applies only to this exact reviewed file state.
- Review started with target inspection at 04:59:52 UTC and finished after evidence, source-asset hashes and validation checks. Maintains uncommitted working-tree provenance at base c081a749cd63feafcc25414f5ad006d1f78f1e36.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T050418Z-sphalerite-round4-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of sphalerite mineral record
started_at: '2026-10-11T04:59:52Z'
finished_at: '2026-10-11T05:04:18Z'
reviewer:
  identity: Codex /root/cmm3_platinum
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer curated antimony in this batch and did not author or
    modify either mineral record, history or dossier. Captured target/context hashes
    before assessment; independently opened authorities and primary text, visually
    checked source figures and rehashed acquired assets.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Official sphalerite identity and conditional laboratory dissolution are supported.
  The record distinguishes ideal ZnS from iron-bearing concentrate, retains low-ferrous
  null and within-paper contradictions, and scopes the analytical fraction and study
  reuse honestly. No actionable defect identified.
source:
  git_revision: c081a749cd63feafcc25414f5ad006d1f78f1e36
  state: working_tree
  inputs:
  - path: data/records/sphalerite.yaml
    sha256: 72097281d609abe00c1c46c133f9967d93950bfd5b0e8c03f1fb2bfc47391b8d
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/sphalerite/2026-10-11T045604Z-codex-dc28a1.yaml
    sha256: f28fa3d8331afc949a06e60db5ef68ab785889a344a8f5984251055f91c11b80
    role: context
  - path: research/ingests/round4-mineral-hosts-20261011.json
    sha256: 136490355bee879209a4a1380516bae9ff5a4441aca85438e13d956a1d55635d
    role: context
  - path: research/ingests/round4-mineral-hosts-20261011.md
    sha256: 964fb6e18e5325b98a826e2d3c4a7cad51da9177319097f380763ad7380f54f4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:sphalerite
  path: data/records/sphalerite.yaml
  label: Sphalerite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sphalerite.yaml
    role: maintained_record
scope:
  description: Whole new sphalerite record, identifiers, evidence links, limits and
    CREATE provenance.
  selection: Assigned named record; all fields reviewed, not a corpus sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:sphalerite
checks:
- check_id: record
  name: Strict mineral record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/chalcopyrite.yaml data/records/sphalerite.yaml
  status: passed
  required: true
  summary: 2 records checked; 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:sphalerite
- check_id: history
  name: History validation at trusted base
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base c081a749cd63feafcc25414f5ad006d1f78f1e36
  status: passed
  required: true
  summary: 36 history records checked; 0 errors.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:sphalerite
- check_id: nonempty
  name: Nonempty corpus validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  status: passed
  required: true
  summary: 27 records checked; 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:sphalerite
- check_id: batch
  name: Completed batch gate
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 307 tests passed, 3 skipped in 47.17s; 27 records and 36 histories valid.
  exit_code: 0
  expected_exit_code: 0
  scope_note: Parent executed the terminal-success batch gate. Reviewer independently
    read /private/tmp/cmm-round4-check.log and reverified unchanged target/context
    hashes; not a second execution.
  target_ids:
  - cmmmech:sphalerite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/sphalerite.yaml
  locator: Entire record, actual CREATE sidecar and distinct inline event
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: Target and context hashes captured before assessment remain unchanged.
    Correct current actor, target and linked sidecar; no fabricated historical authorship.
  snapshot_sha256: 72097281d609abe00c1c46c133f9967d93950bfd5b0e8c03f1fb2bfc47391b8d
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 edition; dictionary page 1, terms page 2; sphalerite row
    page 203
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: ZnS, A approved, 1980 s.p. special-procedure action. This is not an original-discovery
    date or sequential approval identifier. Mineral identity does not inherit elemental
    commodity criticality. Official PDF text independently opened; local PDF receipt
    rehashed.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxa
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Current name, homotypic synonym and species rank
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: NCBI resolves Acidithiobacillus ferrooxidans, with Thiobacillus ferrooxidans
    as a homotypic synonym. It does not establish FC1 strain identity or a modern
    genome-based reassignment.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.65.12.5285-5292.1999
  locator: Methods, Results, Discussion; Figures 2–6 captions
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: Publisher full text supports FC1, washed Gamsberg feed, controlled bulk
    iron and filtered zinc assay. Later enhancement and surface observations support
    a conditional sulfur-layer interpretation, not lattice-specific enzyme action.
    Analytical replicates are not reactor replication.
- evidence_id: 'null'
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.64.10.3570-3575.1998
  locator: Methods; Results; Figures 3–6; Discussion
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: Fixed low-ferrous, varied-ferric comparison reports broadly similar chemical
    and bacterial dissolution despite growth and attachment. Figure 3 conditions conflict
    with the main experiment; record retains this without assigning quantitative currents.
    This bounds the mechanism rather than proving universal absence.
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.65.12.5285-5292.1999
  locator: Visually inspected 1999 Figures 2, 3, 5, 6 and 1998 Figures 4, 5, 6; rehashed
    original files listed in dossier
  accessed_at: '2026-10-11T05:04:18Z'
  support: partial
  summary: 1999 1 g/L ferrous series diverges at later times, confirming tension with
    the sharp Discussion threshold. SEM/EDAX shows surface differences without oxidation-state
    proof; imaging endpoints differ. 1998 paired data lie broadly near equality with
    scatter, not a formal equivalence test.
- evidence_id: receipts
  kind: validation
  reference: research/ingests/round4-mineral-hosts-20261011.json
  locator: Fresh acquisition receipts and reused_artifacts
  accessed_at: '2026-10-11T05:04:18Z'
  support: supports
  summary: Reviewer recalculated byte lengths and SHA256 for all 12 successful local
    assets; all matched. Raw articles/images remain outside Git. Source access limits
    and terms are explicit; curator acquisition is not misrepresented as reviewer
    acquisition.
- evidence_id: search
  kind: search
  reference: Live web search and scoped local rg
  locator: Returned first search results; existing records, dossiers, histories and
    review artifacts
  accessed_at: '2026-10-11T05:04:18Z'
  support: context_only
  summary: No target-specific correction identified among returned exact-DOI results
    and opened primary pages. Broader results provide conditional-mechanism leads
    not fully assessed here. Hidden/ignored-inclusive local results confirm distinct
    mineral identities and shared evidence with copper/zinc, not new independent experiments.
  search_scope: '"10.1128/AEM.65.12.5285-5292.1999" correction retraction erratum;
    "10.1128/AEM.64.10.3570-3575.1998" correction retraction erratum; "sphalerite"
    "Fowler" "Crundwell" sulfur layer direct mechanism contrary; no date filters or
    pagination. rg --no-ignore --hidden -n -g *.yaml -g *.md -g *.json for cmmmech:(chalcopyrite|sphalerite),
    03059, 3570-3575 and 5285-5292 across data/research/reviews/history. Hidden and
    ignored included; bounded, not an exhaustive literature or machine-wide search.'
assessments:
- assessment_id: science
  area: evidence
  topic: Mineral identity, experimental scope and conflicting evidence
  outcome: supported
  summary: Official sphalerite identity and conditional laboratory dissolution are
    supported. The record distinguishes ideal ZnS from iron-bearing concentrate, retains
    low-ferrous null and within-paper contradictions, and scopes the analytical fraction
    and study reuse honestly. No actionable defect identified.
  target_ids:
  - cmmmech:sphalerite
  evidence_ids:
  - record
  - ima
  - taxa
  - primary
  - 'null'
  - figures
  - receipts
  - search
  dimensions:
  - name: material
    value: Mineral ZnS; Gamsberg feed is 98% sphalerite by XRD, iron-bearing and not
      chemically pure ZnS.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - ima
    - primary
  - name: criticality
    value: No mineral-specific designation asserted; zinc commodity status is not
      inherited.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - record
    - ima
  - name: organism
    value: Living FC1, historical Thiobacillus name; current species CURIE only.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - primary
    - taxa
  - name: pretreatment
    value: 45–53 micrometre concentrate washed with 0.5 M sodium sulfide; treatment
      changes the initial surface.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - primary
  - name: conditions
    value: 2 L stirred, aerated cell; 5 g/L feed, 10% inoculum, pH 1.6, 35 +/- 0.1
      C, oxygen 5.9 mg/L; controlled bulk iron.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - primary
  - name: controls
    value: Matched chemical/biotic iron conditions with microscopic contamination
      check; 1998 low-ferrous null retained.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - primary
    - 'null'
    - figures
  - name: outcome
    value: 0.45 micrometre filtrate zinc assay; conditional later enhancement, surface
      evidence and no isolated-product yield. Ten analytical replicates do not mean
      ten reactors.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - primary
    - figures
  - name: deployment
    value: Laboratory cell only; same Fowler studies as zinc.yaml; 1999 model Figure
      10 reuses earlier data.
    definition: Bounded to the inspected record and evidence; no extrapolation to
      other feeds, strains, conditions or deployment.
    evidence_ids:
    - record
    - primary
    - 'null'
- assessment_id: provenance
  area: provenance
  topic: Exact working state, history and acquisition provenance
  outcome: supported
  summary: Current target and all inspection-context hashes match. Actual CREATE sidecar
    remains distinct from inline event, and base-aware history validation passes.
  target_ids:
  - cmmmech:sphalerite
  evidence_ids:
  - record
  - receipts
findings: []
actions: []
limitations:
- Historical FC1 identification is retained without a genomic reassignment. XRD feed
  purity and solid-solution interpretation do not establish pure ideal ZnS.
- Surface imaging and elemental spectra support a sulfur-layer interpretation without
  a direct mineral-lattice enzyme, sulfur valence determination or recovered-product
  purity claim. Model curves were not recomputed.
- The 1999 low-ferrous series and 1998 Figure 3 conditions conflict with broad prose
  claims. These unresolved source tensions remain explicitly in the record. No formal
  statistical equivalence or general threshold inferred.
- Both Fowler papers are from the same investigators and are already represented in
  zinc.yaml; the 1999 model reuses 1998 data. This is additional mineral identity
  coverage, not independent experimental replication.
- Source/correction search is bounded. Newer studies remain unverified extension leads;
  this review does not claim the literature contains no contrary result.
notes:
- No record corrections required; empty findings applies only to this exact reviewed
  file state.
- Review started with target inspection at 04:59:52 UTC and finished after evidence,
  source-asset hashes and validation checks. Maintains uncommitted working-tree provenance
  at base c081a749cd63feafcc25414f5ad006d1f78f1e36.
```
