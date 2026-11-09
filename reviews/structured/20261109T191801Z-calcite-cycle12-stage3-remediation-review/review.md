# Cycle 12 Stage 3 post-remediation scientific review of cmmmech:calcite (Calcite)

- Review: 20261109T191801Z-calcite-cycle12-stage3-remediation-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T19:17:31Z
- Finished UTC: 2026-11-09T19:18:01Z
- Reviewer: marcin (antigravity claude-opus-4-6) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Verified post-remediation state of cmmmech:calcite (Calcite) for Issue #977 (PR #976): Aligned ureC (UniProtKB:A0ACG7VEY6) evidence explanation and causal_graphs[1].edges[0] with the UreABC-UreG complex (#977). Confirmed exact parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples for UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI, Urease accessory protein UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis UP000318769) and canonical history sidecar history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml.

## Scope And Provenance

Single-record scientific and structural review of data/records/calcite.yaml after Cycle 12 Stage 3 remediation (#977).

Selection: Remediated record data/records/calcite.yaml in Cycle 12 Stage 3 (#977).
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base f6fb0663d893c4fe03c82d3fb75fb3c12194252d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CMMMech schema and reference validation | passed | True | cmmmech:calcite | uv run cmmmech validate --require-records passed (703 records, 0 failed). |
| CMMMech history sidecar validation | passed | True | cmmmech:calcite | uv run cmmmech validate-history --base main passed with history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml. |

## Scientific And Domain Assessments

### UniProtKB protein_examples grounding, causal-graph node parity, and causal-edge consistency

grounding: supported. Targets: cmmmech:calcite.

Aligned ureC (UniProtKB:A0ACG7VEY6) evidence explanation and causal_graphs[1].edges[0] with the UreABC-UreG complex (#977). Verified UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI, Urease accessory protein UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis UP000318769) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with identical metadata and supports: partial qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_record | data/records/calcite.yaml | supports | Inspected data/records/calcite.yaml (sha256 ba7311155b2428b3953ad2a37e8de4deca29c54f324a42c36850b302d7264702) and history sidecar history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml. |
| ev_uniprot | sources[uniprot_lysinibacillus_ureabc] and sources[bian2024] in data/records/calcite.yaml | supports | Verified UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI, Urease accessory protein UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis UP000318769) and causal-edge alignment against bian2024 and uniprot_lysinibacillus_ureabc (#977). |

## Limits And Additional Notes

- Primary experimental source (bian2024) does not perform single-gene knockout or purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE scope are explicitly preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T191801Z-calcite-cycle12-stage3-remediation-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 3 post-remediation scientific review of cmmmech:calcite (Calcite)
started_at: '2026-11-09T19:17:31Z'
finished_at: '2026-11-09T19:18:01Z'
reviewer:
  identity: marcin (antigravity claude-opus-4-6)
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Post-remediation structured review of Cycle 12 Stage 3 record
    state after resolving Issue #977, prior to independent subagent re-review.'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Verified post-remediation state of cmmmech:calcite (Calcite) for Issue #977
  (PR #976): Aligned ureC (UniProtKB:A0ACG7VEY6) evidence explanation and causal_graphs[1].edges[0]
  with the UreABC-UreG complex (#977). Confirmed exact parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples for UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI,
  Urease accessory protein UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis
  UP000318769) and canonical history sidecar history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml.'
source:
  git_revision: f6fb0663d893c4fe03c82d3fb75fb3c12194252d
  state: git_commit
  inputs:
  - path: data/records/calcite.yaml
    sha256: ba7311155b2428b3953ad2a37e8de4deca29c54f324a42c36850b302d7264702
    role: target
  - path: history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml
    sha256: 76cafefe3b46fe4e42c8e52e92878ea6c1b88b7756aafb52b7e411426aa00632
    role: context
scope:
  description: Single-record scientific and structural review of data/records/calcite.yaml
    after Cycle 12 Stage 3 remediation (#977).
  selection: Remediated record data/records/calcite.yaml in Cycle 12 Stage 3 (#977).
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:calcite
targets:
- target_id: cmmmech:calcite
  path: data/records/calcite.yaml
  label: Calcite
  record_class: CriticalMineralRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcite.yaml
    role: record
checks:
- check_id: cmmmech_validate
  name: CMMMech schema and reference validation
  status: passed
  required: true
  summary: uv run cmmmech validate --require-records passed (703 records, 0 failed).
  target_ids:
  - cmmmech:calcite
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
  summary: uv run cmmmech validate-history --base main passed with history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml.
  target_ids:
  - cmmmech:calcite
  command: uv run cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
evidence:
- evidence_id: ev_record
  kind: record_content
  reference: data/records/calcite.yaml
  accessed_at: '2026-11-09T19:18:01Z'
  support: supports
  summary: Inspected data/records/calcite.yaml (sha256 ba7311155b2428b3953ad2a37e8de4deca29c54f324a42c36850b302d7264702)
    and history sidecar history/records/calcite/2026-11-09T191545Z-marcin-fd3845.yaml.
  snapshot_sha256: ba7311155b2428b3953ad2a37e8de4deca29c54f324a42c36850b302d7264702
- evidence_id: ev_uniprot
  kind: database
  reference: sources[uniprot_lysinibacillus_ureabc] and sources[bian2024] in data/records/calcite.yaml
  accessed_at: '2026-11-09T19:18:01Z'
  support: supports
  summary: Verified UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI, Urease accessory protein
    UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis UP000318769) and causal-edge
    alignment against bian2024 and uniprot_lysinibacillus_ureabc (#977).
assessments:
- assessment_id: assess_grounding
  area: grounding
  topic: UniProtKB protein_examples grounding, causal-graph node parity, and causal-edge
    consistency
  outcome: supported
  summary: 'Aligned ureC (UniProtKB:A0ACG7VEY6) evidence explanation and causal_graphs[1].edges[0]
    with the UreABC-UreG complex (#977). Verified UniProtKB:A0ACG7VDN2 (A0ACG7VDN2_9BACI,
    Urease accessory protein UreG, ureG, ORF FOH38_22940, Lysinibacillus fusiformis
    UP000318769) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    with identical metadata and supports: partial qualification.'
  target_ids:
  - cmmmech:calcite
  evidence_ids:
  - ev_record
  - ev_uniprot
findings: []
actions: []
limitations:
- 'Primary experimental source (bian2024) does not perform single-gene knockout or
  purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE
  scope are explicitly preserved.'
```
