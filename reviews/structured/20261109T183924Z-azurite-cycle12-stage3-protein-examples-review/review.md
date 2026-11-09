# Cycle 12 Stage 3 protein_examples scientific review of cmmmech:azurite (Azurite)

- Review: 20261109T183924Z-azurite-cycle12-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T18:38:54Z
- Finished UTC: 2026-11-09T18:39:24Z
- Reviewer: marcin (antigravity claude-opus-4-6) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:azurite (Azurite): added UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL, Urease accessory protein UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109) to both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with exact UniProt REST API metadata, qualified supports: partial evidence on kang2016 and uniprot_sporosarcina_soli_ureabc, and canonical history sidecar history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml.

## Scope And Provenance

Single-record scientific and structural review of data/records/azurite.yaml after Cycle 12 Stage 3 protein_examples enrichment.

Selection: Modified record data/records/azurite.yaml in Cycle 12 Stage 3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 58ca607539fede2288c3bc368978e6c8cd086c5a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:azurite | data/records/azurite.yaml | maintained | Azurite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CMMMech schema and reference validation | passed | True | cmmmech:azurite | uv run cmmmech validate --require-records passed (703 records, 0 failed). |
| CMMMech history sidecar validation | passed | True | cmmmech:azurite | uv run cmmmech validate-history --base main passed with history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml. |

## Scientific And Domain Assessments

### UniProtKB protein_examples grounding and causal-graph node parity

grounding: supported. Targets: cmmmech:azurite.

Verified UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL, Urease accessory protein UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with identical metadata and supports: partial qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_record | data/records/azurite.yaml | supports | Inspected data/records/azurite.yaml (sha256 a7df54d9969be1fadbd60460ecca36a3fbf870660e8977211febe1f7f1c23e85) and history sidecar history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml. |
| ev_uniprot | sources[uniprot_sporosarcina_soli_ureabc] and sources[kang2016] in data/records/azurite.yaml | supports | Live-queried UniProt REST API for UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL, Urease accessory protein UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109) and verified accession, entry_name, entry_status, target_organism, reference_proteome_id, EC/InterPro/Pfam/NCBIfam/GO cross-references, and partial evidence qualification against kang2016. |

## Limits And Additional Notes

- Primary experimental source (kang2016) does not perform single-gene knockout or purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE scope are explicitly preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T183924Z-azurite-cycle12-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 3 protein_examples scientific review of cmmmech:azurite (Azurite)
started_at: '2026-11-09T18:38:54Z'
finished_at: '2026-11-09T18:39:24Z'
reviewer:
  identity: marcin (antigravity claude-opus-4-6)
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Post-curation structured review of Cycle 12 Stage 3 protein_examples
    enrichment prior to independent subagent adversarial review.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:azurite
  (Azurite): added UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL, Urease accessory protein
  UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109) to both mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples with exact UniProt REST API metadata,
  qualified supports: partial evidence on kang2016 and uniprot_sporosarcina_soli_ureabc,
  and canonical history sidecar history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml.'
source:
  git_revision: 58ca607539fede2288c3bc368978e6c8cd086c5a
  state: git_commit
  inputs:
  - path: data/records/azurite.yaml
    sha256: a7df54d9969be1fadbd60460ecca36a3fbf870660e8977211febe1f7f1c23e85
    role: target
  - path: history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml
    sha256: 7ff2b8bdb8c3d3eb3d3105f0476559523cd89152342b0fde5b850ab4e67dfb9a
    role: context
scope:
  description: Single-record scientific and structural review of data/records/azurite.yaml
    after Cycle 12 Stage 3 protein_examples enrichment.
  selection: Modified record data/records/azurite.yaml in Cycle 12 Stage 3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:azurite
targets:
- target_id: cmmmech:azurite
  path: data/records/azurite.yaml
  label: Azurite
  record_class: CriticalMineralRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/azurite.yaml
    role: record
checks:
- check_id: cmmmech_validate
  name: CMMMech schema and reference validation
  status: passed
  required: true
  summary: uv run cmmmech validate --require-records passed (703 records, 0 failed).
  target_ids:
  - cmmmech:azurite
  command: uv run cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
  - ev_uniprot
- check_id: cmmmech_validate_history
  name: CMMMech history sidecar validation
  status: passed
  required: true
  summary: uv run cmmmech validate-history --base main passed with history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml.
  target_ids:
  - cmmmech:azurite
  command: uv run cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
evidence:
- evidence_id: ev_record
  kind: record_content
  reference: data/records/azurite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Inspected data/records/azurite.yaml (sha256 a7df54d9969be1fadbd60460ecca36a3fbf870660e8977211febe1f7f1c23e85)
    and history sidecar history/records/azurite/2026-11-09T183630Z-marcin-220682.yaml.
  snapshot_sha256: a7df54d9969be1fadbd60460ecca36a3fbf870660e8977211febe1f7f1c23e85
- evidence_id: ev_uniprot
  kind: database
  reference: sources[uniprot_sporosarcina_soli_ureabc] and sources[kang2016] in data/records/azurite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Live-queried UniProt REST API for UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL,
    Urease accessory protein UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109)
    and verified accession, entry_name, entry_status, target_organism, reference_proteome_id,
    EC/InterPro/Pfam/NCBIfam/GO cross-references, and partial evidence qualification
    against kang2016.
assessments:
- assessment_id: assess_grounding
  area: grounding
  topic: UniProtKB protein_examples grounding and causal-graph node parity
  outcome: supported
  summary: 'Verified UniProtKB:A0ABW0TNU4 (A0ABW0TNU4_9BACL, Urease accessory protein
    UreG, ureG, ORF ACFPRA_14270, Sporosarcina soli UP001596109) in both mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples with identical metadata and supports:
    partial qualification.'
  target_ids:
  - cmmmech:azurite
  evidence_ids:
  - ev_record
  - ev_uniprot
findings: []
actions: []
limitations:
- 'Primary experimental source (kang2016) does not perform single-gene knockout or
  purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE
  scope are explicitly preserved.'
```
