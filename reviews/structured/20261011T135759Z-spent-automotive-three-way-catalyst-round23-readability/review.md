# Readability-corrected successor of the independent automotive catalyst review

- Review: 20261011T135759Z-spent-automotive-three-way-catalyst-round23-readability
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T13:57:25Z
- Finished UTC: 2026-10-11T13:57:59.075146Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Corrected readability of the prior independent assessment; unchanged scientific support, limits, evidence and validation are carried forward transparently. This is not a new literature review.

## Scope And Provenance

Formatting-only correction of the linked independent review, preserving its exact-target scientific assessment and original evidence timestamps; literature is not newly reassessed.

Selection: One assigned new automotive catalyst resource.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 80899a3d3ea5c0f7c5d54f1b3583e43768e92767.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-automotive-three-way-catalyst | data/records/spent-automotive-three-way-catalyst.yaml | maintained | Spent automotive three-way catalyst |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:spent-automotive-three-way-catalyst | Checked 1 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:spent-automotive-three-way-catalyst | /private/tmp/cmm-round23-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 93.20s (0:01:33)<br>Checked 156 record(s); 0 failed.<br>Checked 177 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:spent-automotive-three-way-catalyst | /private/tmp/cmm-round23-final-require.log: Checked 156 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:spent-automotive-three-way-catalyst | /private/tmp/cmm-round23-final-history.log: Checked 177 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Distinct use-defined secondary resource

identity: supported. Targets: cmmmech:spent-automotive-three-way-catalyst.

A real spent vehicle catalyst is distinct from fresh catalyst, constituent elements and petroleum-processing catalysts. Selected feed is not universal converter composition.

### Condition-dependent laboratory aluminium leaching

evidence: supported. Targets: cmmmech:spent-automotive-three-way-catalyst.

Narrow culture-associated pretreatment evidence is supported. Source conflicts, chemical comparators and unresolved phase/product accounting are explicit.

### Actual CREATE and independent exact-state review

provenance: supported. Targets: cmmmech:spent-automotive-three-way-catalyst.

Author agent and reviewer differ; actual sidecar/inline event and current byte hashes are retained. No record edit made by reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/spent-automotive-three-way-catalyst.yaml; Entire maintained record and actual CREATE sidecar | supports | Current frozen record read independently after canonical inspection; identity is a real used automotive catalyst resource, with no inherited criticality or invented material CURIE. |
| primary | https://doi.org/10.1016/j.jenvman.2023.118825; Methods 2.1–2.6, Results 3.2–3.5, conclusions and data availability; locally rendered PDF pages 4,6,7,8 (Figures 1–6) visually inspected | supports | Full repository PDF reused with provenance from round 12 and independently read. Day 4/day 14/day 20 media differ in age and pH. Figure 4 supports 54.5% Al leaching for the stationary-culture 5% loading arm, not phase-specific coating removal or isolated product recovery. Figure 4 30% and 60% comparisons conflict with high-loading prose; 57.1% in economics conflicts with 54.5%. Pt enrichment is calculated with assumed retention, and bulk non-detection conflicts with selected EDX Pt signals. No detection limit, complete mass balance or catalyst-arm replicate count is established. |
| authority | https://www.dsmz.de/collection/catalogue/details/culture/DSM-11478; Live DSMZ catalogue plus NCBI Taxonomy 930 page on 2026-10-11 | supports | DSM 11478 strain designation Tth04 is A. thiooxidans; NCBI Taxonomy 930 identifies the species. Neither authority independently authenticates experimental stock or proves strain-specific necessity. |
| search | https://rodin.uca.es/xmlui/handle/10498/30253; Primary repository and publisher metadata; exact DOI/title correction queries | context_only | Primary repository and ScienceDirect bibliographic identity independently checked. Queries "10.1016/j.jenvman.2023.118825" correction OR retraction and "Bioleaching of the α-alumina layer" returned no affecting notice in the inspected first sets; no exhaustive absence claim. Curator bounded supplementary/dataset acquisition and candidate-dedup receipts independently inspected. Reviewer did not acquire missing SI or dataset contents. |
| provenance | research/ingests/round23-identity-gaps-sources-20261011.json; Reused PDF/text artifact hashes, access limitations and source boundaries | supports | PDF reused from round 12, not misrepresented as a fresh round 23 download. Raw files remain outside Git. Missing SI, static-loading dataset routes and metadata-only access cannot support imported supplementary measurements. |
| gates | /private/tmp/cmm-round23-gate-receipts.json; Terminal full checks and frozen current target hash | supports | 308 tests passed, 3 skipped in 93.20 s; 156 records and 177 histories pass. Root executed and read these terminal receipts; all target hashes remain equal to the gated state. |

## Limits And Additional Notes

- Full supplementary composition, pH plots and underlying dataset contents were unavailable; main evidence supports the narrower claims only.
- Different initial pH, culture age and residual chemistry prevent a matched live-cell causal comparison; independent leaching-arm replication is unspecified.
- Figure/text percentages, economic optimum and bulk-versus-local Pt observations remain inconsistent; no repaired numerical optimum is asserted.
- Total liquid Al does not isolate coating dissolution; microscopy and EDX do not prove an EPS pathway, intracellular uptake, bulk recovery or purity.
- Bounded correction search does not establish universal absence of notices or contradictory publications.
- Record/dossier orientation preceded canonical inspection; formal assessment and primary review followed it.
- Initial named-validation attempt hit the default uv cache sandbox restriction before checking data; rerun using the task-local cache completed successfully.
- Publication review found joined words and quantities in the prior saved review. This successor corrects those presentation defects without altering evidence values, verdict, target bytes, limitations or original evidence/check timestamps. The prior YAML/Markdown pair is retained byte-for-byte. Primary literature was not newly reassessed for this formatting correction; the earlier independent assessment is carried forward after verifying every input hash remains unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T135759Z-spent-automotive-three-way-catalyst-round23-readability
kind: record
repository: CultureBotAI/CMMMech
title: Readability-corrected successor of the independent automotive catalyst review
started_at: '2026-10-11T13:57:25Z'
finished_at: '2026-10-11T13:57:59.075146Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round23_identity_gaps authored the record. Root
    independently inspected primary full text, Figures 1–6 and identity authorities,
    and did not edit the target. Shared worktree, curator dossier and reused primary
    PDF are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Corrected readability of the prior independent assessment; unchanged scientific
  support, limits, evidence and validation are carried forward transparently. This
  is not a new literature review.
source:
  git_revision: 80899a3d3ea5c0f7c5d54f1b3583e43768e92767
  state: working_tree
  inputs:
  - path: data/records/spent-automotive-three-way-catalyst.yaml
    sha256: 779ed92c36f0ed35d3dd6a48f0b2771c49630b27744ef87137b258422553a6eb
    role: target
  - path: history/records/spent-automotive-three-way-catalyst/2026-10-11T134655Z-codex-971fce.yaml
    sha256: 6b4fc7020a7432ea161c8804865266ceed423aa9366dcec09b93c22eace7fcc0
    role: context
  - path: research/ingests/round23-identity-gaps-sources-20261011.json
    sha256: ef19bf9755f82f3815646bd329f153be55f77c57bb8c1bba0a59f04537a12583
    role: context
  - path: research/ingests/round23-identity-gaps-sources-20261011.md
    sha256: 22fd7518cdfc713345544166534676b8024ae57fe36391e886522596f031d911
    role: context
  - path: reviews/structured/20261011T135351Z-spent-automotive-three-way-catalyst-round23-independent/review.yaml
    sha256: e98fc714b58477ba3d068aef69091183fc312104e521f5f73cf1412888537fc0
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Formatting-only correction of the linked independent review, preserving
    its exact-target scientific assessment and original evidence timestamps; literature
    is not newly reassessed.
  selection: One assigned new automotive catalyst resource.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
  exclusions:
  - target: Unavailable supplementary files and underlying experimental dataset
    reason: Main PDF and bounded access receipts inspected; no missing cells or images
      inferred.
targets:
- target_id: cmmmech:spent-automotive-three-way-catalyst
  path: data/records/spent-automotive-three-way-catalyst.yaml
  label: Spent automotive three-way catalyst
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-automotive-three-way-catalyst.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/spent-automotive-three-way-catalyst.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round23-final-batch.log: uv run --locked --extra dev
    python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 93.20s (0:01:33)

    Checked 156 record(s); 0 failed.

    Checked 177 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round23-final-require.log: Checked 156 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 80899a3d3ea5c0f7c5d54f1b3583e43768e92767
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round23-final-history.log: Checked 177 history record(s);
    0 error(s).

    '
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/spent-automotive-three-way-catalyst.yaml
  locator: Entire maintained record and actual CREATE sidecar
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: supports
  summary: Current frozen record read independently after canonical inspection; identity
    is a real used automotive catalyst resource, with no inherited criticality or
    invented material CURIE.
  snapshot_sha256: 779ed92c36f0ed35d3dd6a48f0b2771c49630b27744ef87137b258422553a6eb
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.jenvman.2023.118825
  locator: Methods 2.1–2.6, Results 3.2–3.5, conclusions and data availability; locally
    rendered PDF pages 4,6,7,8 (Figures 1–6) visually inspected
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: supports
  summary: Full repository PDF reused with provenance from round 12 and independently
    read. Day 4/day 14/day 20 media differ in age and pH. Figure 4 supports 54.5%
    Al leaching for the stationary-culture 5% loading arm, not phase-specific coating
    removal or isolated product recovery. Figure 4 30% and 60% comparisons conflict
    with high-loading prose; 57.1% in economics conflicts with 54.5%. Pt enrichment
    is calculated with assumed retention, and bulk non-detection conflicts with selected
    EDX Pt signals. No detection limit, complete mass balance or catalyst-arm replicate
    count is established.
  snapshot_sha256: a32ef09a4ad14394dc7f01bb74c731a0434fcdb408ec6f411606b29cec8c4838
- evidence_id: authority
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-11478
  locator: Live DSMZ catalogue plus NCBI Taxonomy 930 page on 2026-10-11
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: supports
  summary: DSM 11478 strain designation Tth04 is A. thiooxidans; NCBI Taxonomy 930
    identifies the species. Neither authority independently authenticates experimental
    stock or proves strain-specific necessity.
- evidence_id: search
  kind: search
  reference: https://rodin.uca.es/xmlui/handle/10498/30253
  locator: Primary repository and publisher metadata; exact DOI/title correction queries
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: context_only
  summary: Primary repository and ScienceDirect bibliographic identity independently
    checked. Queries "10.1016/j.jenvman.2023.118825" correction OR retraction and
    "Bioleaching of the α-alumina layer" returned no affecting notice in the inspected
    first sets; no exhaustive absence claim. Curator bounded supplementary/dataset
    acquisition and candidate-dedup receipts independently inspected. Reviewer did
    not acquire missing SI or dataset contents.
  search_scope: No filters or pagination; exact query timestamp not retained. Dedup
    receipt covers relevant records, research, reviews, history and named raw directories,
    including hidden/ignored files and relevant symlinks; not machine-wide.
- evidence_id: provenance
  kind: record_content
  reference: research/ingests/round23-identity-gaps-sources-20261011.json
  locator: Reused PDF/text artifact hashes, access limitations and source boundaries
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: supports
  summary: PDF reused from round 12, not misrepresented as a fresh round 23 download.
    Raw files remain outside Git. Missing SI, static-loading dataset routes and metadata-only
    access cannot support imported supplementary measurements.
  snapshot_sha256: ef19bf9755f82f3815646bd329f153be55f77c57bb8c1bba0a59f04537a12583
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round23-gate-receipts.json
  locator: Terminal full checks and frozen current target hash
  accessed_at: '2026-10-11T13:53:51.065478Z'
  support: supports
  summary: 308 tests passed, 3 skipped in 93.20 s; 156 records and 177 histories pass.
    Root executed and read these terminal receipts; all target hashes remain equal
    to the gated state.
  snapshot_sha256: 1642db5c291aad5a85764aef2e8ad13b1c4511bc3cfd60c25123461f5dbd0096
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct use-defined secondary resource
  outcome: supported
  summary: A real spent vehicle catalyst is distinct from fresh catalyst, constituent
    elements and petroleum-processing catalysts. Selected feed is not universal converter
    composition.
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Used vehicle-treatment-centre catalytic-converter material.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority, jurisdiction, list or edition is inherited from constituent
      elements.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Condition-dependent laboratory aluminium leaching
  outcome: supported
  summary: Narrow culture-associated pretreatment evidence is supported. Source conflicts,
    chemical comparators and unresolved phase/product accounting are explicit.
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
  evidence_ids:
  - record
  - primary
  - authority
  dimensions:
  - name: organism_strain
    value: Acidithiobacillus thiooxidans DSM 11478 (Tth04)
    definition: Species CURIE is 930; strain provenance is separately source-defined.
    evidence_ids:
    - primary
    - authority
  - name: biomass_state
    value: Living culture-containing and centrifuged culture-derived media
    definition: Day 20 source-labelled bacteria-free medium was not independently
      shown sterile.
    evidence_ids:
    - primary
  - name: substrate
    value: Cryomilled real spent automotive three-way catalyst
    definition: El Caimán vehicle-treatment-centre feed; complete composition in unavailable
      Table S1.
    evidence_ids:
    - primary
  - name: conditions_controls
    value: 5/30/60% w/v; 14 days; 30 degrees C; 150 rpm
    definition: Unlike culture ages and initial pH; commercial acid comparator and
      absent leaching-arm replication detail limit causality.
    evidence_ids:
    - primary
  - name: outcome
    value: Liquid aluminium release; reported feed-normalized leaching percentage
    definition: 54.5% is the source 5% loading stationary-culture result, not purified
      recovery. Local EDX is not bulk Pt recovery.
    evidence_ids:
    - primary
  - name: deployment
    value: Laboratory pretreatment
    definition: Industrial waste origin does not demonstrate pilot or industrial deployment.
    evidence_ids:
    - record
    - primary
- assessment_id: history
  area: provenance
  topic: Actual CREATE and independent exact-state review
  outcome: supported
  summary: Author agent and reviewer differ; actual sidecar/inline event and current
    byte hashes are retained. No record edit made by reviewer.
  target_ids:
  - cmmmech:spent-automotive-three-way-catalyst
  evidence_ids:
  - record
  - provenance
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- Full supplementary composition, pH plots and underlying dataset contents were unavailable;
  main evidence supports the narrower claims only.
- Different initial pH, culture age and residual chemistry prevent a matched live-cell
  causal comparison; independent leaching-arm replication is unspecified.
- Figure/text percentages, economic optimum and bulk-versus-local Pt observations
  remain inconsistent; no repaired numerical optimum is asserted.
- Total liquid Al does not isolate coating dissolution; microscopy and EDX do not
  prove an EPS pathway, intracellular uptake, bulk recovery or purity.
- Bounded correction search does not establish universal absence of notices or contradictory
  publications.
notes:
- Record/dossier orientation preceded canonical inspection; formal assessment and
  primary review followed it.
- Initial named-validation attempt hit the default uv cache sandbox restriction before
  checking data; rerun using the task-local cache completed successfully.
- Publication review found joined words and quantities in the prior saved review.
  This successor corrects those presentation defects without altering evidence values,
  verdict, target bytes, limitations or original evidence/check timestamps. The prior
  YAML/Markdown pair is retained byte-for-byte. Primary literature was not newly reassessed
  for this formatting correction; the earlier independent assessment is carried forward
  after verifying every input hash remains unchanged.
tags:
- round23
- independent
- scientific-review
- secondary-resource
- readability-correction
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261011T135351Z-spent-automotive-three-way-catalyst-round23-independent
  relationship: Formatting-only successor; carries forward the same exact-target independent
    scientific assessment and preserves the prior observation unchanged.
```
