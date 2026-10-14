# Hydroxylapatite SI evidence provenance finding

- Review: 20261014T114338Z-hydroxylapatite-round70-si-provenance-finding
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T11:41:40Z
- Finished UTC: 2026-10-14T11:43:38.009590Z
- Reviewer: codex /root/round68_iron_sulfides (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

The original scientific review describes the complete ten-page supporting PDF but its si evidence SHA256 is the empty failed download. Correct source provenance through an immutable successor; no scientific record error is demonstrated.

## Scope And Provenance

Provenance-only examination of the prior review SI evidence binding, exact unchanged record/history and corresponding failed/successful raw artifacts. Literature support and experimental claims were not reassessed.

Selection: Specific discrepancy found during final publication audit; native inspect captured inputs before formal assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hydroxylapatite | data/records/hydroxylapatite.yaml | maintained | Hydroxylapatite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named unchanged-record validation | passed | True | cmmmech:hydroxylapatite | Executed during this provenance review: Checked1record;0failed. |
| Completed coordinator batch gate | passed | True | cmmmech:hydroxylapatite | Completed actual round70 command before this observation; unchanged scientific owner/history. 2026-10-14T11:33:43.296738+00:00 to 2026-10-14T11:37:15.611892+00:00 |
| Completed coordinator batch gate | passed | True | cmmmech:hydroxylapatite | Completed actual round70 command before this observation; unchanged scientific owner/history. 2026-10-14T11:37:15.611913+00:00 to 2026-10-14T11:37:23.980116+00:00 |
| Completed coordinator batch gate | passed | True | cmmmech:hydroxylapatite | Completed actual round70 command before this observation; unchanged scientific owner/history. 2026-10-14T11:37:23.980141+00:00 to 2026-10-14T11:37:29.732952+00:00 |

## Scientific And Domain Assessments

### Supporting-PDF identity in scientific review

provenance: concern. Targets: cmmmech:hydroxylapatite.

The evidence hash identifies a failed empty file rather than the full supporting PDF. The record/history remain byte-identical, but review provenance requires correction.

## Findings

### F1: Scientific review SI hash identifies an empty failed download

major / open / confirmed; issue key: hydroxylapatite-round70-review-si-empty-download-hash.

The prior completed scientific review binds its claimed ten-page SI inspection to a zero-byte failed file. The genuine inspected supporting PDF is a different artifact. Resolve the evidence binding through a new linked observation without rewriting prior review or inventing a record correction.

## Recommended Actions And Acceptance Checks

### A1

Independent scientific reviewer must verify the genuine supporting PDF and save an immutable successor resolving this exact occurrence with correct artifact hash and locator; preserve original observation.

- Recheck full10-page original SI and match DOI/Figshare file identity, size and SHA256.
- Save a native successor with the same issue_key and exact previous_occurrences repository/review_id/finding_id; retain the unchanged scientific record/history hashes.
- Canonical review checks pass and final publication explicitly binds the corrected evidence disposition. No original review is rewritten.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/hydroxylapatite.yaml; Exact unchanged owner and canonical history hashes in native inspection | context_only | Owner SHAaa1a4d7f and history SHA0fb305f3 match the prior review. This observation does not change or independently reaccept the mineral science. |
| prior | reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml; evidence_id si, snapshot_sha256 at line169 | refutes | Evidence describes complete10-page PDF and claim-bearing figures/tables, but records e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. |
| empty | /private/tmp/cmm-round70-phosphates-research/zorzetto2023-si.pdf; Entire0-byte failed download | supports | File size zero and SHA256 equals the hash incorrectly used by prior review. It cannot contain the described supporting text/graphics. |
| actual | /private/tmp/cmm-round70-phosphates-research/zorzetto2023-original-cm2c02969_si_001.pdf; Successful1,179,442-byte supporting PDF, filename matched to Figshare39913176 | supports | Actual successful source has different SHA256 db317e6c7d16f67d7adafe6c93b4cac78bafea04245f925298e26c8fb6a93cfd. This provenance observation verifies bytes; the independent scientific reviewer must reassess source correspondence. |
| named | /private/tmp/cmm-round70-hydroxylapatite-provenance-validation.log; Complete named execution output | supports | Named record structurally valid; validation does not verify external evidence hashes. |
| gates | /private/tmp/cmm-round70-final-gates.json; Actual completed round70 gates and matching log | supports | just check, nonempty validation and trusted-base history completed successfully before this provenance observation. |

## Limits And Additional Notes

- Literature support, scientific mechanisms and measurements were not reassessed in this provenance-only observation.
- No record or history edit is warranted solely to fix the review artifact.
- Affected canonical review checks and publication audit must run after successor resolution.
- Initial save rejected YAML aliases generated by shared Python objects; serialized without aliases before any repository review was created. Exact inspected inputs were unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T114338Z-hydroxylapatite-round70-si-provenance-finding
kind: record
repository: CultureBotAI/CMMMech
title: Hydroxylapatite SI evidence provenance finding
started_at: '2026-10-14T11:41:40Z'
finished_at: '2026-10-14T11:43:38.009590Z'
reviewer:
  identity: codex /root/round68_iron_sulfides
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Did not author hydroxylapatite record, history or original scientific
    review. Operational final-package assessment identified wrong evidence binding;
    no literature reassessment or record edit is claimed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: The original scientific review describes the complete ten-page supporting
  PDF but its si evidence SHA256 is the empty failed download. Correct source provenance
  through an immutable successor; no scientific record error is demonstrated.
source:
  git_revision: 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7
  state: working_tree
  inputs:
  - path: data/records/hydroxylapatite.yaml
    sha256: aa1a4d7fa01015a81f2624cb696adf166e62814fd348d7b06bab23d81969ac12
    role: target
  - path: history/records/hydroxylapatite/2026-10-14T112716Z-codex-aed1c2.yaml
    sha256: 0fb305f3906bc0f8c70ceb143b63d71a0f6200488ff39f2f7d4a843d90974cc9
    role: context
  - path: reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml
    sha256: 9e9ef7258afdc5a9d220d23a423a08b62bec1bab4f0dc25127f09d559b4348d6
    role: context
scope:
  description: Provenance-only examination of the prior review SI evidence binding,
    exact unchanged record/history and corresponding failed/successful raw artifacts.
    Literature support and experimental claims were not reassessed.
  selection: Specific discrepancy found during final publication audit; native inspect
    captured inputs before formal assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hydroxylapatite
targets:
- target_id: cmmmech:hydroxylapatite
  path: data/records/hydroxylapatite.yaml
  label: Hydroxylapatite
  kind: maintained
  ownership_note: The maintained mineral record is unchanged. This review concerns
    the linked scientific-review SI evidence hash; correction belongs in an immutable
    successor review, not an owner edit.
checks:
- check_id: named
  name: Named unchanged-record validation
  command: uv run --locked cmmmech validate --require-records data/records/hydroxylapatite.yaml
  status: passed
  required: true
  summary: 'Executed during this provenance review: Checked1record;0failed.'
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - named
- check_id: batch_0
  name: Completed coordinator batch gate
  command: just check
  status: passed
  required: true
  summary: Completed actual round70 command before this observation; unchanged scientific
    owner/history. 2026-10-14T11:33:43.296738+00:00 to 2026-10-14T11:37:15.611892+00:00
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - gates
- check_id: batch_1
  name: Completed coordinator batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Completed actual round70 command before this observation; unchanged scientific
    owner/history. 2026-10-14T11:37:15.611913+00:00 to 2026-10-14T11:37:23.980116+00:00
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - gates
- check_id: batch_2
  name: Completed coordinator batch gate
  command: uv run --locked cmmmech validate-history --base 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7
  status: passed
  required: true
  summary: Completed actual round70 command before this observation; unchanged scientific
    owner/history. 2026-10-14T11:37:23.980141+00:00 to 2026-10-14T11:37:29.732952+00:00
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - gates
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/hydroxylapatite.yaml
  locator: Exact unchanged owner and canonical history hashes in native inspection
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: context_only
  summary: Owner SHAaa1a4d7f and history SHA0fb305f3 match the prior review. This
    observation does not change or independently reaccept the mineral science.
  snapshot_sha256: aa1a4d7fa01015a81f2624cb696adf166e62814fd348d7b06bab23d81969ac12
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml
  locator: evidence_id si, snapshot_sha256 at line169
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: refutes
  summary: Evidence describes complete10-page PDF and claim-bearing figures/tables,
    but records e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
  snapshot_sha256: 9e9ef7258afdc5a9d220d23a423a08b62bec1bab4f0dc25127f09d559b4348d6
- evidence_id: empty
  kind: record_content
  reference: /private/tmp/cmm-round70-phosphates-research/zorzetto2023-si.pdf
  locator: Entire0-byte failed download
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: supports
  summary: File size zero and SHA256 equals the hash incorrectly used by prior review.
    It cannot contain the described supporting text/graphics.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: actual
  kind: record_content
  reference: /private/tmp/cmm-round70-phosphates-research/zorzetto2023-original-cm2c02969_si_001.pdf
  locator: Successful1,179,442-byte supporting PDF, filename matched to Figshare39913176
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: supports
  summary: Actual successful source has different SHA256 db317e6c7d16f67d7adafe6c93b4cac78bafea04245f925298e26c8fb6a93cfd.
    This provenance observation verifies bytes; the independent scientific reviewer
    must reassess source correspondence.
  snapshot_sha256: db317e6c7d16f67d7adafe6c93b4cac78bafea04245f925298e26c8fb6a93cfd
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round70-hydroxylapatite-provenance-validation.log
  locator: Complete named execution output
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: supports
  summary: Named record structurally valid; validation does not verify external evidence
    hashes.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round70-final-gates.json
  locator: Actual completed round70 gates and matching log
  accessed_at: '2026-10-14T11:43:38.009590Z'
  support: supports
  summary: just check, nonempty validation and trusted-base history completed successfully
    before this provenance observation.
  snapshot_sha256: 901e0e7e3ecaf5f364fa05b6c1f5dfcfb231dca506ef61e77988b19f9ee39cfb
assessments:
- assessment_id: si_binding
  area: provenance
  topic: Supporting-PDF identity in scientific review
  outcome: concern
  summary: The evidence hash identifies a failed empty file rather than the full supporting
    PDF. The record/history remain byte-identical, but review provenance requires
    correction.
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - prior
  - empty
  - actual
  - record
findings:
- finding_id: F1
  issue_key: hydroxylapatite-round70-review-si-empty-download-hash
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Scientific review SI hash identifies an empty failed download
  description: The prior completed scientific review binds its claimed ten-page SI
    inspection to a zero-byte failed file. The genuine inspected supporting PDF is
    a different artifact. Resolve the evidence binding through a new linked observation
    without rewriting prior review or inventing a record correction.
  target_ids:
  - cmmmech:hydroxylapatite
  field_paths:
  - reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml#evidence[si].snapshot_sha256
  evidence_ids:
  - prior
  - empty
  - actual
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml
    role: immutable_prior_review_context
  rule_id: native-review-exact-evidence-provenance
  native_severity: major
  normalization_reason: 'Major retained: the complete supporting-evidence attestation
    binds a file with no evidence content. This is a review-provenance defect, not
    a demonstrated scientific claim error.'
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/222
actions:
- action_id: A1
  description: Independent scientific reviewer must verify the genuine supporting
    PDF and save an immutable successor resolving this exact occurrence with correct
    artifact hash and locator; preserve original observation.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:hydroxylapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: reviews/structured/20261014T113824Z-hydroxylapatite-round70-independent/review.yaml
    role: immutable_prior_review_context
  acceptance_checks:
  - Recheck full10-page original SI and match DOI/Figshare file identity, size and
    SHA256.
  - Save a native successor with the same issue_key and exact previous_occurrences
    repository/review_id/finding_id; retain the unchanged scientific record/history
    hashes.
  - Canonical review checks pass and final publication explicitly binds the corrected
    evidence disposition. No original review is rewritten.
limitations:
- Literature support, scientific mechanisms and measurements were not reassessed in
  this provenance-only observation.
- No record or history edit is warranted solely to fix the review artifact.
- Affected canonical review checks and publication audit must run after successor
  resolution.
tags:
- round70
- provenance-only
- evidence-hash
notes:
- Initial save rejected YAML aliases generated by shared Python objects; serialized
  without aliases before any repository review was created. Exact inspected inputs
  were unchanged.
```
