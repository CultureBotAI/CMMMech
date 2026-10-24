# Post-schema-fix provenance reassessment of lucasite-ce

- Review: 20261024T100600Z-lucasite-ce-round120-reassessment
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T10:02:00Z
- Finished UTC: 2026-10-24T10:06:00Z
- Reviewer: antigravity / round120-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Lucasite-(Ce) (IMA:1986-020) passes provenance-only post-schema-fix reassessment (scientific_review: false): all scientific field values are proved unchanged from prior scientific review 20261024T074000Z-lucasite-ce-round120 (pre-edit SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f -&gt; post-fix SHA-256 b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c); only sources formatting was updated for LinkML Source schema compliance, and primary literature was not reassessed.

## Scope And Provenance

Scoped provenance/schema-alignment reassessment of data/records/lucasite-ce.yaml (SHA-256 b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c) against prior scientific review 20261024T074000Z-lucasite-ce-round120 (pre-edit target SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f).

Selection: Targeted post-fix reassessment after LinkML Source schema formatting alignment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b18e567096cceeb767514d9cec5d99e75688aef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lucasite-ce | data/records/lucasite-ce.yaml | maintained | Lucasite-(Ce) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:lucasite-ce | Checked 662 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:lucasite-ce | Checked 981 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Provenance-only LinkML Source schema alignment and scientific field invariance for lucasite-ce

provenance: supported. Targets: cmmmech:lucasite-ce.

Provenance-only follow-up to prior scientific review 20261024T074000Z-lucasite-ce-round120: all scientific field values (id, name, material_kind, description, identifiers, relations, history_refs, curation_history) are proved identical to pre-edit SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f, and only sources was reformatted to LinkML Source (id, title, url, accessed_on). Primary literature was not reassessed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/lucasite-ce.yaml; Complete post-fix working-tree record data/records/lucasite-ce.yaml | supports | Post-fix record data/records/lucasite-ce.yaml (SHA-256 b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c) conforms to LinkML Source schema (id, title, url, accessed_on) with zero changes to scientific field values. |
| prior_review | reviews/structured/20261024T074000Z-lucasite-ce-round120/review.yaml; Restored initial scientific review reviews/structured/20261024T074000Z-lucasite-ce-round120/review.yaml (target SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f) | supports | Prior scientific review 20261024T074000Z-lucasite-ce-round120 (review.yaml SHA-256 585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3) established primary-source mineralogical and authority support for IMA:1986-020 Lucasite-(Ce) against pre-edit record SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f. |
| field_diff_proof | data/records/lucasite-ce.yaml; Deterministic parsed YAML comparison between pre-edit (01af95373ca2) and post-fix (b7bf8101aee5) states of data/records/lucasite-ce.yaml | supports | All scientific field values (id, name, material_kind, description, identifiers, relations, history_refs, curation_history) are 100% identical to the prior reviewed state; only sources was reformatted to fold authors/year/notes into title and add accessed_on: 2026-10-24 for LinkML Source schema compliance while preserving id and url verbatim. Primary literature was not reassessed. |
| history | history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml; Canonical CREATE sidecar history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml | supports | Canonical CREATE history sidecar is unchanged and passes validate-history against the Git base. |
| validation | data/records/lucasite-ce.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history | supports | Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s). |

## Limits And Additional Notes

- Provenance-only reassessment (scientific_review: false); primary literature was not reassessed because all scientific field values were proved identical to prior scientific review 20261024T074000Z-lucasite-ce-round120.
- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.
- Prior scientific review 20261024T074000Z-lucasite-ce-round120 was restored to its exact 092942 SHA-256 (585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3) before appending this reassessment bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T100600Z-lucasite-ce-round120-reassessment
kind: record
repository: CultureBotAI/CMMMech
title: Post-schema-fix provenance reassessment of lucasite-ce
started_at: '2026-10-24T10:02:00Z'
finished_at: '2026-10-24T10:06:00Z'
reviewer:
  identity: antigravity / round120-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    following LinkML Source schema formatting edits to data/records/lucasite-ce.yaml;
    verifies field-by-field equality of all scientific fields against the prior reviewed
    state (20261024T074000Z-lucasite-ce-round120, pre-edit SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
source:
  git_revision: 2b18e567096cceeb767514d9cec5d99e75688aef
  state: working_tree
  inputs:
  - path: data/records/lucasite-ce.yaml
    sha256: b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c
    role: target
  - path: history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml
    sha256: 1e98d4e0a2d9d0255ace799b243b354cea86c61985dd448275ff94704f20e942
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.json
    sha256: bb159c4337de6f01565d04f1e0690b34aec0ed43a722b7004d95515f41c6f0cc
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.md
    sha256: 4be24aeb244eccde8a9fb1335608d162ce50544319b3480b1e8acd0cf171cacf
    role: context
  - path: reviews/structured/20261024T074000Z-lucasite-ce-round120/review.yaml
    sha256: 585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:lucasite-ce
  path: data/records/lucasite-ce.yaml
  label: Lucasite-(Ce)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lucasite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml
    role: canonical_history
scope:
  description: Scoped provenance/schema-alignment reassessment of data/records/lucasite-ce.yaml
    (SHA-256 b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c) against
    prior scientific review 20261024T074000Z-lucasite-ce-round120 (pre-edit target
    SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f).
  selection: Targeted post-fix reassessment after LinkML Source schema formatting
    alignment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lucasite-ce
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/lucasite-ce.yaml
  locator: Complete post-fix working-tree record data/records/lucasite-ce.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Post-fix record data/records/lucasite-ce.yaml (SHA-256 b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c)
    conforms to LinkML Source schema (id, title, url, accessed_on) with zero changes
    to scientific field values.
  snapshot_sha256: b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c
- evidence_id: prior_review
  kind: record_content
  reference: reviews/structured/20261024T074000Z-lucasite-ce-round120/review.yaml
  locator: Restored initial scientific review reviews/structured/20261024T074000Z-lucasite-ce-round120/review.yaml
    (target SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f)
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Prior scientific review 20261024T074000Z-lucasite-ce-round120 (review.yaml
    SHA-256 585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3) established
    primary-source mineralogical and authority support for IMA:1986-020 Lucasite-(Ce)
    against pre-edit record SHA-256 01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f.
  snapshot_sha256: 585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3
- evidence_id: field_diff_proof
  kind: validation
  reference: data/records/lucasite-ce.yaml
  locator: Deterministic parsed YAML comparison between pre-edit (01af95373ca2) and
    post-fix (b7bf8101aee5) states of data/records/lucasite-ce.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: 'All scientific field values (id, name, material_kind, description, identifiers,
    relations, history_refs, curation_history) are 100% identical to the prior reviewed
    state; only sources was reformatted to fold authors/year/notes into title and
    add accessed_on: 2026-10-24 for LinkML Source schema compliance while preserving
    id and url verbatim. Primary literature was not reassessed.'
  snapshot_sha256: b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c
- evidence_id: history
  kind: record_content
  reference: history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml
  locator: Canonical CREATE sidecar history/records/lucasite-ce/2026-10-24T073000Z-antigravity-001207.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Canonical CREATE history sidecar is unchanged and passes validate-history
    against the Git base.
  snapshot_sha256: 1e98d4e0a2d9d0255ace799b243b354cea86c61985dd448275ff94704f20e942
- evidence_id: validation
  kind: validation
  reference: data/records/lucasite-ce.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s).
  snapshot_sha256: b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 662 record(s); 0 failed.
  target_ids:
  - cmmmech:lucasite-ce
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
  - cmmmech:lucasite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: provenance_schema_reassessment
  area: provenance
  topic: Provenance-only LinkML Source schema alignment and scientific field invariance
    for lucasite-ce
  outcome: supported
  summary: 'Provenance-only follow-up to prior scientific review 20261024T074000Z-lucasite-ce-round120:
    all scientific field values (id, name, material_kind, description, identifiers,
    relations, history_refs, curation_history) are proved identical to pre-edit SHA-256
    01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f, and only sources
    was reformatted to LinkML Source (id, title, url, accessed_on). Primary literature
    was not reassessed.'
  target_ids:
  - cmmmech:lucasite-ce
  evidence_ids:
  - owner
  - prior_review
  - field_diff_proof
  - history
  - validation
findings: []
actions: []
summary: 'Lucasite-(Ce) (IMA:1986-020) passes provenance-only post-schema-fix reassessment
  (scientific_review: false): all scientific field values are proved unchanged from
  prior scientific review 20261024T074000Z-lucasite-ce-round120 (pre-edit SHA-256
  01af95373ca200cb85c25e47f9e5589da9fcaf4961ec7116807b84eacd282e1f -> post-fix SHA-256
  b7bf8101aee52fd57fc74f4790f416d6178526a03a0be8fb5a0d3946de6aba9c); only sources
  formatting was updated for LinkML Source schema compliance, and primary literature
  was not reassessed.'
limitations:
- 'Provenance-only reassessment (scientific_review: false); primary literature was
  not reassessed because all scientific field values were proved identical to prior
  scientific review 20261024T074000Z-lucasite-ce-round120.'
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.'
notes:
- Prior scientific review 20261024T074000Z-lucasite-ce-round120 was restored to its
  exact 092942 SHA-256 (585d96ca390fef894900f84af2d5263394bf7b5c174ab7684adab70661898dd3)
  before appending this reassessment bundle.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261024T074000Z-lucasite-ce-round120
  relationship: post_schema_fix_provenance_reassessment
```
