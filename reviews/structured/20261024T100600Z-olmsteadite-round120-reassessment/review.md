# Post-schema-fix provenance reassessment of olmsteadite

- Review: 20261024T100600Z-olmsteadite-round120-reassessment
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T10:02:00Z
- Finished UTC: 2026-10-24T10:06:00Z
- Reviewer: antigravity / round120-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Olmsteadite (IMA:1974-034) passes provenance-only post-schema-fix reassessment (scientific_review: false): all scientific field values are proved unchanged from prior scientific review 20261024T074000Z-olmsteadite-round120 (pre-edit SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b -&gt; post-fix SHA-256 ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b); only sources formatting was updated for LinkML Source schema compliance, and primary literature was not reassessed.

## Scope And Provenance

Scoped provenance/schema-alignment reassessment of data/records/olmsteadite.yaml (SHA-256 ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b) against prior scientific review 20261024T074000Z-olmsteadite-round120 (pre-edit target SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b).

Selection: Targeted post-fix reassessment after LinkML Source schema formatting alignment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b18e567096cceeb767514d9cec5d99e75688aef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:olmsteadite | data/records/olmsteadite.yaml | maintained | Olmsteadite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:olmsteadite | Checked 662 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:olmsteadite | Checked 981 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Provenance-only LinkML Source schema alignment and scientific field invariance for olmsteadite

provenance: supported. Targets: cmmmech:olmsteadite.

Provenance-only follow-up to prior scientific review 20261024T074000Z-olmsteadite-round120: all scientific field values (id, name, material_kind, description, identifiers, relations, history_refs, curation_history) are proved identical to pre-edit SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b, and only sources was reformatted to LinkML Source (id, title, url, accessed_on). Primary literature was not reassessed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/olmsteadite.yaml; Complete post-fix working-tree record data/records/olmsteadite.yaml | supports | Post-fix record data/records/olmsteadite.yaml (SHA-256 ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b) conforms to LinkML Source schema (id, title, url, accessed_on) with zero changes to scientific field values. |
| prior_review | reviews/structured/20261024T074000Z-olmsteadite-round120/review.yaml; Restored initial scientific review reviews/structured/20261024T074000Z-olmsteadite-round120/review.yaml (target SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b) | supports | Prior scientific review 20261024T074000Z-olmsteadite-round120 (review.yaml SHA-256 0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07) established primary-source mineralogical and authority support for IMA:1974-034 Olmsteadite against pre-edit record SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b. |
| field_diff_proof | data/records/olmsteadite.yaml; Deterministic parsed YAML comparison between pre-edit (1f74faf97b8a) and post-fix (ee68842fb782) states of data/records/olmsteadite.yaml | supports | All scientific field values (id, name, material_kind, description, identifiers, relations, history_refs, curation_history) are 100% identical to the prior reviewed state; only sources was reformatted to fold authors/year/notes into title and add accessed_on: 2026-10-24 for LinkML Source schema compliance while preserving id and url verbatim. Primary literature was not reassessed. |
| history | history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml; Canonical CREATE sidecar history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml | supports | Canonical CREATE history sidecar is unchanged and passes validate-history against the Git base. |
| validation | data/records/olmsteadite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history | supports | Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s). |

## Limits And Additional Notes

- Provenance-only reassessment (scientific_review: false); primary literature was not reassessed because all scientific field values were proved identical to prior scientific review 20261024T074000Z-olmsteadite-round120.
- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.
- Prior scientific review 20261024T074000Z-olmsteadite-round120 was restored to its exact 092942 SHA-256 (0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07) before appending this reassessment bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T100600Z-olmsteadite-round120-reassessment
kind: record
repository: CultureBotAI/CMMMech
title: Post-schema-fix provenance reassessment of olmsteadite
started_at: '2026-10-24T10:02:00Z'
finished_at: '2026-10-24T10:06:00Z'
reviewer:
  identity: antigravity / round120-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    following LinkML Source schema formatting edits to data/records/olmsteadite.yaml;
    verifies field-by-field equality of all scientific fields against the prior reviewed
    state (20261024T074000Z-olmsteadite-round120, pre-edit SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
source:
  git_revision: 2b18e567096cceeb767514d9cec5d99e75688aef
  state: working_tree
  inputs:
  - path: data/records/olmsteadite.yaml
    sha256: ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b
    role: target
  - path: history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml
    sha256: 2c13dc32adf1c163618f05d24ca62529802e53c221829aa0ad5a84036386ad22
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.json
    sha256: bb159c4337de6f01565d04f1e0690b34aec0ed43a722b7004d95515f41c6f0cc
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.md
    sha256: 4be24aeb244eccde8a9fb1335608d162ce50544319b3480b1e8acd0cf171cacf
    role: context
  - path: reviews/structured/20261024T074000Z-olmsteadite-round120/review.yaml
    sha256: 0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:olmsteadite
  path: data/records/olmsteadite.yaml
  label: Olmsteadite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olmsteadite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml
    role: canonical_history
scope:
  description: Scoped provenance/schema-alignment reassessment of data/records/olmsteadite.yaml
    (SHA-256 ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b) against
    prior scientific review 20261024T074000Z-olmsteadite-round120 (pre-edit target
    SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b).
  selection: Targeted post-fix reassessment after LinkML Source schema formatting
    alignment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:olmsteadite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/olmsteadite.yaml
  locator: Complete post-fix working-tree record data/records/olmsteadite.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Post-fix record data/records/olmsteadite.yaml (SHA-256 ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b)
    conforms to LinkML Source schema (id, title, url, accessed_on) with zero changes
    to scientific field values.
  snapshot_sha256: ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b
- evidence_id: prior_review
  kind: record_content
  reference: reviews/structured/20261024T074000Z-olmsteadite-round120/review.yaml
  locator: Restored initial scientific review reviews/structured/20261024T074000Z-olmsteadite-round120/review.yaml
    (target SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b)
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Prior scientific review 20261024T074000Z-olmsteadite-round120 (review.yaml
    SHA-256 0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07) established
    primary-source mineralogical and authority support for IMA:1974-034 Olmsteadite
    against pre-edit record SHA-256 1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b.
  snapshot_sha256: 0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07
- evidence_id: field_diff_proof
  kind: validation
  reference: data/records/olmsteadite.yaml
  locator: Deterministic parsed YAML comparison between pre-edit (1f74faf97b8a) and
    post-fix (ee68842fb782) states of data/records/olmsteadite.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: 'All scientific field values (id, name, material_kind, description, identifiers,
    relations, history_refs, curation_history) are 100% identical to the prior reviewed
    state; only sources was reformatted to fold authors/year/notes into title and
    add accessed_on: 2026-10-24 for LinkML Source schema compliance while preserving
    id and url verbatim. Primary literature was not reassessed.'
  snapshot_sha256: ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b
- evidence_id: history
  kind: record_content
  reference: history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml
  locator: Canonical CREATE sidecar history/records/olmsteadite/2026-10-24T073000Z-antigravity-00120a.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Canonical CREATE history sidecar is unchanged and passes validate-history
    against the Git base.
  snapshot_sha256: 2c13dc32adf1c163618f05d24ca62529802e53c221829aa0ad5a84036386ad22
- evidence_id: validation
  kind: validation
  reference: data/records/olmsteadite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s).
  snapshot_sha256: ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 662 record(s); 0 failed.
  target_ids:
  - cmmmech:olmsteadite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base 2b18e567096cceeb767514d9cec5d99e75688aef
  status: passed
  required: true
  summary: Checked 981 history record(s); 0 error(s).
  target_ids:
  - cmmmech:olmsteadite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: provenance_schema_reassessment
  area: provenance
  topic: Provenance-only LinkML Source schema alignment and scientific field invariance
    for olmsteadite
  outcome: supported
  summary: 'Provenance-only follow-up to prior scientific review 20261024T074000Z-olmsteadite-round120:
    all scientific field values (id, name, material_kind, description, identifiers,
    relations, history_refs, curation_history) are proved identical to pre-edit SHA-256
    1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b, and only sources
    was reformatted to LinkML Source (id, title, url, accessed_on). Primary literature
    was not reassessed.'
  target_ids:
  - cmmmech:olmsteadite
  evidence_ids:
  - owner
  - prior_review
  - field_diff_proof
  - history
  - validation
findings: []
actions: []
summary: 'Olmsteadite (IMA:1974-034) passes provenance-only post-schema-fix reassessment
  (scientific_review: false): all scientific field values are proved unchanged from
  prior scientific review 20261024T074000Z-olmsteadite-round120 (pre-edit SHA-256
  1f74faf97b8a0132177562705b69aefb2ea8a716514ec1de8e29969f0756263b -> post-fix SHA-256
  ee68842fb7825e74cfb176d8c674d69620503a00e35e7e69e0fc0c142059c28b); only sources
  formatting was updated for LinkML Source schema compliance, and primary literature
  was not reassessed.'
limitations:
- 'Provenance-only reassessment (scientific_review: false); primary literature was
  not reassessed because all scientific field values were proved identical to prior
  scientific review 20261024T074000Z-olmsteadite-round120.'
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.'
notes:
- Prior scientific review 20261024T074000Z-olmsteadite-round120 was restored to its
  exact 092942 SHA-256 (0ac2c64a06be8fd5d88fc38e9c093ccd2bf8b7b8617af8579a28d40075007e07)
  before appending this reassessment bundle.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261024T074000Z-olmsteadite-round120
  relationship: post_schema_fix_provenance_reassessment
```
