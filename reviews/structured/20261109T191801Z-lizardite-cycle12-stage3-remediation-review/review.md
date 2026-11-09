# Cycle 12 Stage 3 post-remediation scientific review of cmmmech:lizardite (Lizardite)

- Review: 20261109T191801Z-lizardite-cycle12-stage3-remediation-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T19:17:31Z
- Finished UTC: 2026-11-09T19:18:01Z
- Reviewer: marcin (antigravity claude-opus-4-6) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Verified post-remediation state of cmmmech:lizardite (Lizardite) for Issue #977 (PR #976): Aligned causal_graphs[0].edges[0] description and evidence explanation with co-localized TCA-cycle Malate dehydrogenase (mdh / HNP21_003257) (#977). Confirmed exact parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples for UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase, mdh, ORF HNP21_003257, EC:1.1.1.37, Priestia aryabhattai UP000543174) and canonical history sidecar history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml.

## Scope And Provenance

Single-record scientific and structural review of data/records/lizardite.yaml after Cycle 12 Stage 3 remediation (#977).

Selection: Remediated record data/records/lizardite.yaml in Cycle 12 Stage 3 (#977).
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base f6fb0663d893c4fe03c82d3fb75fb3c12194252d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lizardite | data/records/lizardite.yaml | maintained | Lizardite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CMMMech schema and reference validation | passed | True | cmmmech:lizardite | uv run cmmmech validate --require-records passed (703 records, 0 failed). |
| CMMMech history sidecar validation | passed | True | cmmmech:lizardite | uv run cmmmech validate-history --base main passed with history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml. |

## Scientific And Domain Assessments

### UniProtKB protein_examples grounding, causal-graph node parity, and causal-edge consistency

grounding: supported. Targets: cmmmech:lizardite.

Aligned causal_graphs[0].edges[0] description and evidence explanation with co-localized TCA-cycle Malate dehydrogenase (mdh / HNP21_003257) (#977). Verified UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase, mdh, ORF HNP21_003257, EC:1.1.1.37, Priestia aryabhattai UP000543174) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with identical metadata and supports: partial qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_record | data/records/lizardite.yaml | supports | Inspected data/records/lizardite.yaml (sha256 240bca3e417fcbcfe7e199e80abcd7ada35bdf44aabea1befd33f067849a9f9e) and history sidecar history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml. |
| ev_uniprot | sources[uniprot_priestia_aryabhattai_acids] and sources[sheng_2026] in data/records/lizardite.yaml | supports | Verified UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase, mdh, ORF HNP21_003257, EC:1.1.1.37, Priestia aryabhattai UP000543174) and causal-edge alignment against sheng_2026 and uniprot_priestia_aryabhattai_acids (#977). |

## Limits And Additional Notes

- Primary experimental source (sheng_2026) does not perform single-gene knockout or purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE scope are explicitly preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T191801Z-lizardite-cycle12-stage3-remediation-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 3 post-remediation scientific review of cmmmech:lizardite (Lizardite)
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
summary: 'Verified post-remediation state of cmmmech:lizardite (Lizardite) for Issue
  #977 (PR #976): Aligned causal_graphs[0].edges[0] description and evidence explanation
  with co-localized TCA-cycle Malate dehydrogenase (mdh / HNP21_003257) (#977). Confirmed
  exact parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  for UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase, mdh, ORF HNP21_003257,
  EC:1.1.1.37, Priestia aryabhattai UP000543174) and canonical history sidecar history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml.'
source:
  git_revision: f6fb0663d893c4fe03c82d3fb75fb3c12194252d
  state: git_commit
  inputs:
  - path: data/records/lizardite.yaml
    sha256: 240bca3e417fcbcfe7e199e80abcd7ada35bdf44aabea1befd33f067849a9f9e
    role: target
  - path: history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml
    sha256: 70f7ab36b8ab9a67df767adcd7c742cc6fb68d2d615f7048c755d68bbf56227b
    role: context
scope:
  description: Single-record scientific and structural review of data/records/lizardite.yaml
    after Cycle 12 Stage 3 remediation (#977).
  selection: Remediated record data/records/lizardite.yaml in Cycle 12 Stage 3 (#977).
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lizardite
targets:
- target_id: cmmmech:lizardite
  path: data/records/lizardite.yaml
  label: Lizardite
  record_class: CriticalMineralRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lizardite.yaml
    role: record
checks:
- check_id: cmmmech_validate
  name: CMMMech schema and reference validation
  status: passed
  required: true
  summary: uv run cmmmech validate --require-records passed (703 records, 0 failed).
  target_ids:
  - cmmmech:lizardite
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
  summary: uv run cmmmech validate-history --base main passed with history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml.
  target_ids:
  - cmmmech:lizardite
  command: uv run cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
evidence:
- evidence_id: ev_record
  kind: record_content
  reference: data/records/lizardite.yaml
  accessed_at: '2026-11-09T19:18:01Z'
  support: supports
  summary: Inspected data/records/lizardite.yaml (sha256 240bca3e417fcbcfe7e199e80abcd7ada35bdf44aabea1befd33f067849a9f9e)
    and history sidecar history/records/lizardite/2026-11-09T191545Z-marcin-6fac51.yaml.
  snapshot_sha256: 240bca3e417fcbcfe7e199e80abcd7ada35bdf44aabea1befd33f067849a9f9e
- evidence_id: ev_uniprot
  kind: database
  reference: sources[uniprot_priestia_aryabhattai_acids] and sources[sheng_2026] in
    data/records/lizardite.yaml
  accessed_at: '2026-11-09T19:18:01Z'
  support: supports
  summary: Verified UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase,
    mdh, ORF HNP21_003257, EC:1.1.1.37, Priestia aryabhattai UP000543174) and causal-edge
    alignment against sheng_2026 and uniprot_priestia_aryabhattai_acids (#977).
assessments:
- assessment_id: assess_grounding
  area: grounding
  topic: UniProtKB protein_examples grounding, causal-graph node parity, and causal-edge
    consistency
  outcome: supported
  summary: 'Aligned causal_graphs[0].edges[0] description and evidence explanation
    with co-localized TCA-cycle Malate dehydrogenase (mdh / HNP21_003257) (#977).
    Verified UniProtKB:A0A0J6SZC4 (A0A0J6SZC4_PRIAR, Malate dehydrogenase, mdh, ORF
    HNP21_003257, EC:1.1.1.37, Priestia aryabhattai UP000543174) in both mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples with identical metadata and supports:
    partial qualification.'
  target_ids:
  - cmmmech:lizardite
  evidence_ids:
  - ev_record
  - ev_uniprot
findings: []
actions: []
limitations:
- 'Primary experimental source (sheng_2026) does not perform single-gene knockout
  or purified-enzyme assays for the grounded protein example; supports: partial and
  REPRESENTATIVE_EXAMPLE scope are explicitly preserved.'
```
