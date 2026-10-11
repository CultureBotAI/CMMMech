# Independent scientific review of Electrolytic manganese residue

- Review: 20261011T114810Z-electrolytic-manganese-residue-round19-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:43:00Z
- Finished UTC: 2026-10-11T11:48:10Z
- Reviewer: Codex /root/round19_hydrogenation_catalyst (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The process-defined resource identity and bounded laboratory claims are supported. No actionable defect was identified in these inspected bytes; source contradictions, incomplete controls and deployment limits remain explicit.

## Scope And Provenance

Every field and linked CREATE sidecar of the assigned frozen record, including identity, criticality, organisms, conditions, controls, outcomes and limitations.

Selection: One assigned new round19 maintained record, independent of reviewer authorship.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:electrolytic-manganese-residue | data/records/electrolytic-manganese-residue.yaml | maintained | Electrolytic manganese residue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:electrolytic-manganese-residue | Reviewer observed terminal exit 0: Checked 3 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:electrolytic-manganese-residue | Parent executed and confirmed terminal completion; reviewer independently read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 122.38s (0:02:02)<br>Checked 145 record(s); 0 failed.<br>Checked 161 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:electrolytic-manganese-residue | Parent executed and confirmed terminal completion; reviewer independently read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-require.log: Checked 145 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:electrolytic-manganese-residue | Parent executed and confirmed terminal completion; reviewer independently read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-history.log: Checked 161 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Resource and criticality boundaries

identity: supported. Targets: cmmmech:electrolytic-manganese-residue.

Electrolytic-manganese process residue from the Jishou-area disposal dam is distinct from manganese ore, elemental manganese and manufactured electrolytic metal or dioxide. Broad source industry context is not used to conflate all manganese wastes.

### Source-specific organisms, assay, controls and outcome

evidence: supported. Targets: cmmmech:electrolytic-manganese-residue.

The primary assay supports culture-associated solution-phase Mn mobilization from a process residue. The 71.6% at 72 h is medium Mn mass divided by initial slag Mn mass; later decline and nonzero lower uninoculated release are retained. Organic-acid causation is explicitly unverified.

### Frozen reviewed inputs and real CREATE provenance

provenance: supported. Targets: cmmmech:electrolytic-manganese-residue.

Canonical inspect captured target, history and schema before assessment; final hashes still agree. Actual Codex/GPT-6 author session and matching resource target are retained, with inline and sidecar provenance distinct. Named validation and required batch/history checks passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/electrolytic-manganese-residue.yaml; Complete frozen YAML and linked CREATE history | supports | Resource boundaries, source-limited mechanisms and provenance inspected; no constituent criticality is inherited. |
| search | /private/tmp/cmm-round19-cross-review/search.json; Exact DOI correction/retraction queries and bounded local dedup search | context_only | No affecting notice surfaced in the searched first-result sets; bounded results do not prove absence of conflicting literature. |
| primary | https://doi.org/10.1080/09593330.2011.624125; Full six-page article plus cover; Sections 2.1-2.5 and 3.1-3.2.5, Figures 1-6. Actual figure pages in PDF pages 4-6 viewed. | supports | The primary assay supports culture-associated solution-phase Mn mobilization from a process residue. The 71.6% at 72 h is medium Mn mass divided by initial slag Mn mass; later decline and nonzero lower uninoculated release are retained. Organic-acid causation is explicitly unverified. |
| gates | /private/tmp/cmm-round19-gate-receipts.json; Completed native batch, require-records and trusted-base history receipts; all three logs independently read | supports | Parent observed terminal exit 0; 308 passed, 3 skipped, 145 records and 161 histories. Reviewer independently read receipts/logs and rechecked frozen input hashes. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5506&amp;mode=Info; Live NCBI label/rank and saved official HTML | supports | NCBITaxon:5506 resolves to Fusarium at genus rank, not an experimental strain. |
| sequence | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FJ532369.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; Complete official 538-bp GenBank entry, locus, organism, strain and gene fields | supports | FJ532369.1 identifies CJB1 partial 28S. Figure 1 also names CJB1, but neither source proves identity with text-designated J62. |

## Limits And Additional Notes

- J62/CJB1 equivalence and ribosomal-marker wording remain unresolved; a genus identifier does not establish a strain.
- Missing loading, ambiguous inoculum wording, and lack of matched-acidity controls prevent a fully reproducible optimum or verified organic-acid mechanism.
- The pH series upper limit differs between Figure 4 and prose; AAS does not establish Mn oxidation state, and BCR fractions do not give complete mass balance.
- Single-site laboratory evidence does not establish industrial recovery or broad residue performance.
- Bounded correction/retraction and local duplicate searches do not establish literature exhaustion.
- The actual UTC review-start boundary is the filesystem timestamp of the canonical inspect output written before assessment; finish is captured when authoring this immutable review. All inspected input hashes were rechecked before save.
- No scientific edit or additional curation-history event was introduced by this review. No blocker, major or minor finding was identified; limitations are scientific scope, not unaddressed record errors.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T114810Z-electrolytic-manganese-residue-round19-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Electrolytic manganese residue
started_at: '2026-10-11T11:43:00Z'
finished_at: '2026-10-11T11:48:10Z'
reviewer:
  identity: Codex /root/round19_hydrogenation_catalyst
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate agent /root/round19_manganese_residue authored the
    record and its CREATE history. Reviewer independently inspected primary methods,
    results, figures and authorities after canonical byte inspection, with shared
    worktree/raw-source access disclosed. No target edits made.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The process-defined resource identity and bounded laboratory claims are supported.
  No actionable defect was identified in these inspected bytes; source contradictions,
  incomplete controls and deployment limits remain explicit.
source:
  git_revision: c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a
  state: working_tree
  inputs:
  - path: data/records/electrolytic-manganese-residue.yaml
    sha256: 2b049bbf4af80158c48fb0e26398894a3879ecdc26fa1df023893e21c7197fe7
    role: target
  - path: history/records/electrolytic-manganese-residue/2026-10-11T114147Z-codex-794cf9.yaml
    sha256: 4aad6686ad1ae6a735f992e5f514b0b6a94f8f71ff220ac1d9ac8273100b5238
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every field and linked CREATE sidecar of the assigned frozen record,
    including identity, criticality, organisms, conditions, controls, outcomes and
    limitations.
  selection: One assigned new round19 maintained record, independent of reviewer authorship.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:electrolytic-manganese-residue
  exclusions:
  - target: Other corpus records, raw instrument recalibration and experimental replication
    reason: Contextual companion arms and related sources do not receive a separate
      record verdict; no experimental replication is asserted.
targets:
- target_id: cmmmech:electrolytic-manganese-residue
  path: data/records/electrolytic-manganese-residue.yaml
  label: Electrolytic manganese residue
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrolytic-manganese-residue.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/electrolytic-manganese-residue.yaml data/records/chrysotile-asbestos-tailings.yaml
    data/records/copper-flotation-tailings.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer observed terminal exit 0: Checked 3 record(s); 0 failed.'
  target_ids:
  - cmmmech:electrolytic-manganese-residue
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-batch.log:
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 122.38s (0:02:02)

    Checked 145 record(s); 0 failed.

    Checked 161 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:electrolytic-manganese-residue
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-require.log:
    Checked 145 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:electrolytic-manganese-residue
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read the completed receipt and corresponding log. /private/tmp/cmm-round19-final-history.log:
    Checked 161 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:electrolytic-manganese-residue
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/electrolytic-manganese-residue.yaml
  locator: Complete frozen YAML and linked CREATE history
  accessed_at: '2026-10-11T11:48:10Z'
  support: supports
  summary: Resource boundaries, source-limited mechanisms and provenance inspected;
    no constituent criticality is inherited.
  snapshot_sha256: 2b049bbf4af80158c48fb0e26398894a3879ecdc26fa1df023893e21c7197fe7
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round19-cross-review/search.json
  locator: Exact DOI correction/retraction queries and bounded local dedup search
  accessed_at: '2026-10-11T11:48:10Z'
  support: context_only
  summary: No affecting notice surfaced in the searched first-result sets; bounded
    results do not prove absence of conflicting literature.
  snapshot_sha256: a774bd3b4cad74636b71e2af5f24e741ee93d2ee4062cdd686c9eb876c4d52c2
  search_scope: Hidden and ignored files included, relevant symlinks followed, named
    raw directories searched; binary scientific artifacts inspected separately. Related
    prior mentions are not duplicate records or independent experiments by themselves.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1080/09593330.2011.624125
  locator: Full six-page article plus cover; Sections 2.1-2.5 and 3.1-3.2.5, Figures
    1-6. Actual figure pages in PDF pages 4-6 viewed.
  accessed_at: '2026-10-11T11:48:10Z'
  support: supports
  summary: The primary assay supports culture-associated solution-phase Mn mobilization
    from a process residue. The 71.6% at 72 h is medium Mn mass divided by initial
    slag Mn mass; later decline and nonzero lower uninoculated release are retained.
    Organic-acid causation is explicitly unverified.
  snapshot_sha256: bdd76ab25db308b772726fad375a9b9d06a3352fab986eacdc5dab0f7ec6625c
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round19-gate-receipts.json
  locator: Completed native batch, require-records and trusted-base history receipts;
    all three logs independently read
  accessed_at: '2026-10-11T11:48:10Z'
  support: supports
  summary: Parent observed terminal exit 0; 308 passed, 3 skipped, 145 records and
    161 histories. Reviewer independently read receipts/logs and rechecked frozen
    input hashes.
  snapshot_sha256: 73640a84a624b3375df302586a36481457dbdc3e045f50101b67fe811860b6db
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5506&mode=Info
  locator: Live NCBI label/rank and saved official HTML
  accessed_at: '2026-10-11T11:48:10Z'
  support: supports
  summary: NCBITaxon:5506 resolves to Fusarium at genus rank, not an experimental
    strain.
  snapshot_sha256: e0167d629e33f3b199650e5b49dc1aa06be92f4c69c99038337c69b24e499c87
- evidence_id: sequence
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FJ532369.1&db=nuccore&report=genbank&retmode=text
  locator: Complete official 538-bp GenBank entry, locus, organism, strain and gene
    fields
  accessed_at: '2026-10-11T11:48:10Z'
  support: supports
  summary: FJ532369.1 identifies CJB1 partial 28S. Figure 1 also names CJB1, but neither
    source proves identity with text-designated J62.
  snapshot_sha256: 0183c741368a935dfdfbd4fe26f8261dd0a74f5adc4eda9a7f1b681bfc66932f
assessments:
- assessment_id: identity
  area: identity
  topic: Resource and criticality boundaries
  outcome: supported
  summary: Electrolytic-manganese process residue from the Jishou-area disposal dam
    is distinct from manganese ore, elemental manganese and manufactured electrolytic
    metal or dioxide. Broad source industry context is not used to conflate all manganese
    wastes.
  target_ids:
  - cmmmech:electrolytic-manganese-residue
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Process-defined mixed material, distinct from an element, ion, pure
      mineral and commodity.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority, jurisdiction, list or edition designation is inherited
      from constituent elements.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Source-specific organisms, assay, controls and outcome
  outcome: supported
  summary: The primary assay supports culture-associated solution-phase Mn mobilization
    from a process residue. The 71.6% at 72 h is medium Mn mass divided by initial
    slag Mn mass; later decline and nonzero lower uninoculated release are retained.
    Organic-acid causation is explicitly unverified.
  target_ids:
  - cmmmech:electrolytic-manganese-residue
  evidence_ids:
  - record
  - primary
  - taxon
  - sequence
  dimensions:
  - name: organism_and_biomass
    value: Live Fusarium culture, source isolate called J62; genus NCBITaxon:5506
      only. The cited FJ532369.1 sequence is CJB1 partial 28S, with Figure 1 itself
      labeling CJB1; the paper also uses 26S and 16S wording. Same-isolate equivalence
      remains unresolved.
    definition: Organism and biomass state are limited to the actual source-level
      identification; taxonomy does not establish strain or causal exclusivity.
    evidence_ids:
    - primary
    - taxon
    - sequence
  - name: substrate_and_conditions
    value: 100 mL sterilized sucrose-containing Czapek medium, nominal 2% v/v inoculum,
      initial pH 4, 28 degrees C and 150 rpm through 144 h; triplicates. Solid loading
      and pretreatment are insufficiently specified, and dry/wet inoculum-mass wording
      is ambiguous.
    definition: Preparation, assay duration, loading and culture temperature remain
      arm-specific; source discrepancies are preserved.
    evidence_ids:
    - primary
  - name: controls_and_fraction
    value: Uninoculated cultures show nonzero lower Mn release. No abiotic control
      matches the changing pH trajectory. Centrifuged supernatant AAS measures elemental
      Mn rather than oxidation state; BCR fractions are operational, not mineral identifications.
    definition: Measured analytical fractions and abiotic/null comparisons constrain
      the causal interpretation.
    evidence_ids:
    - primary
  - name: outcome_and_scale
    value: Laboratory Mn mobilization; no isolated manganese product or industrial
      deployment. The reported 71.6% at 72 h has an explicit feed-Mn denominator and
      is not product yield.
    definition: Aqueous mobilization or laboratory physical stabilization is not equivalent
      to isolated product recovery or industrial deployment.
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Frozen reviewed inputs and real CREATE provenance
  outcome: supported
  summary: Canonical inspect captured target, history and schema before assessment;
    final hashes still agree. Actual Codex/GPT-6 author session and matching resource
    target are retained, with inline and sidecar provenance distinct. Named validation
    and required batch/history checks passed.
  target_ids:
  - cmmmech:electrolytic-manganese-residue
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- J62/CJB1 equivalence and ribosomal-marker wording remain unresolved; a genus identifier
  does not establish a strain.
- Missing loading, ambiguous inoculum wording, and lack of matched-acidity controls
  prevent a fully reproducible optimum or verified organic-acid mechanism.
- The pH series upper limit differs between Figure 4 and prose; AAS does not establish
  Mn oxidation state, and BCR fractions do not give complete mass balance.
- Single-site laboratory evidence does not establish industrial recovery or broad
  residue performance.
- Bounded correction/retraction and local duplicate searches do not establish literature
  exhaustion.
tags:
- round19
- independent
- scientific-review
- resource
notes:
- The actual UTC review-start boundary is the filesystem timestamp of the canonical
  inspect output written before assessment; finish is captured when authoring this
  immutable review. All inspected input hashes were rechecked before save.
- No scientific edit or additional curation-history event was introduced by this review.
  No blocker, major or minor finding was identified; limitations are scientific scope,
  not unaddressed record errors.
```
