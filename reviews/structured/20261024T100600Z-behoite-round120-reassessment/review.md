# Post-schema-fix scientific and mechanism reassessment of behoite

- Review: 20261024T100600Z-behoite-round120-reassessment
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T10:02:00Z
- Finished UTC: 2026-10-24T10:06:00Z
- Reviewer: antigravity / round120-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Behoite (IMA:1969-031) passes post-schema-fix scientific reassessment (scientific_review: true, linked to 20261024T074000Z-behoite-round120): Rechecked mechanisms[0] (abiotic_dta_dehydroxylation: process=other, microbial=false, description, context, and evidence) against Ehlmann &amp; Mitchell (1970) p. 7: DuPont 900 DTA at 20 °C/min in air shows a two-step endothermic dehydroxylation of natural orthorhombic beta-Be(OH)2 with inflections beginning at ~265 °C and ~290 °C and peaking at 310 °C; no microbial or bioleaching mechanism was tested.

## Scope And Provenance

Scoped scientific reassessment of data/records/behoite.yaml (SHA-256 fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5) following LinkML Mechanism and Source schema updates, linked to prior scientific review 20261024T074000Z-behoite-round120 (pre-edit target SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e).

Selection: Targeted post-fix scientific reassessment of record with updated mechanisms[0] and sources fields.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b18e567096cceeb767514d9cec5d99e75688aef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:behoite | data/records/behoite.yaml | maintained | Behoite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:behoite | Checked 662 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:behoite | Checked 981 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Post-fix primary-source recheck of abiotic mechanism and identity fields for behoite

evidence: supported. Targets: cmmmech:behoite.

Rechecked mechanisms[0] (abiotic_dta_dehydroxylation: process=other, microbial=false, description, context, and evidence) against Ehlmann &amp; Mitchell (1970) p. 7: DuPont 900 DTA at 20 °C/min in air shows a two-step endothermic dehydroxylation of natural orthorhombic beta-Be(OH)2 with inflections beginning at ~265 °C and ~290 °C and peaking at 310 °C; no microbial or bioleaching mechanism was tested.

### LinkML Mechanism/Source schema compliance and provenance integrity

provenance: supported. Targets: cmmmech:behoite.

Species-level fields (id, name, material_kind, description, identifiers, history_refs, curation_history) match prior review 20261024T074000Z-behoite-round120 (pre-edit SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e); updated mechanisms[0] and sources fields pass strict LinkML validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/behoite.yaml; Complete post-fix working-tree record data/records/behoite.yaml | supports | Post-fix record data/records/behoite.yaml (SHA-256 fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5) conforms to LinkML Source and Mechanism schemas with unchanged species-level identity fields and primary-source-verified abiotic mechanism fields. |
| prior_review | reviews/structured/20261024T074000Z-behoite-round120/review.yaml; Restored initial scientific review reviews/structured/20261024T074000Z-behoite-round120/review.yaml (target SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e) | supports | Prior scientific review 20261024T074000Z-behoite-round120 (review.yaml SHA-256 6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139) assessed pre-edit record SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e; id, name, material_kind, description, identifiers, relations, history_refs, and curation_history are unchanged. |
| primary_study | https://www.rruff.net/doclib/am/vol55/AM55_1.pdf; AM 55 (1970) 1-9, p. 7 and Fig. 4 (DTA of Rode Ranch behoite on DuPont 900 analyzer at 20 °C/min in air flow) | supports | Rechecked mechanisms[0] (abiotic_dta_dehydroxylation: process=other, microbial=false, description, context, and evidence) against Ehlmann &amp; Mitchell (1970) p. 7: DuPont 900 DTA at 20 °C/min in air shows a two-step endothermic dehydroxylation of natural orthorhombic beta-Be(OH)2 with inflections beginning at ~265 °C and ~290 °C and peaking at 310 °C; no microbial or bioleaching mechanism was tested. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Confirms official mineral species identity, formula, and IMA approval tag (IMA:1969-031) for Behoite. |
| history | history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml; Canonical CREATE sidecar history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml | supports | Canonical CREATE history sidecar is unchanged and passes validate-history against the Git base. |
| validation | data/records/behoite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history | supports | Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.
- Reported mechanism is strictly abiotic laboratory thermal/topotactic behavior (microbial: false); no biological processing or industrial recovery yield is reported in the primary source.
- Prior scientific review 20261024T074000Z-behoite-round120 was restored to its exact 092942 SHA-256 (6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139) before appending this reassessment bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T100600Z-behoite-round120-reassessment
kind: record
repository: CultureBotAI/CMMMech
title: Post-schema-fix scientific and mechanism reassessment of behoite
started_at: '2026-10-24T10:02:00Z'
finished_at: '2026-10-24T10:06:00Z'
reviewer:
  identity: antigravity / round120-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    following LinkML Source and Mechanism schema edits to data/records/behoite.yaml;
    rechecked updated mechanisms[0] fields (process, microbial, description, context,
    evidence) directly against the primary source PDF (AM 55 (1970) 1-9, p. 7 and
    Fig. 4 (DTA of Rode Ranch behoite on DuPont 900 analyzer at 20 °C/min in air flow))
    and verified species-level field invariance against prior review 20261024T074000Z-behoite-round120
    (pre-edit SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 2b18e567096cceeb767514d9cec5d99e75688aef
  state: working_tree
  inputs:
  - path: data/records/behoite.yaml
    sha256: fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5
    role: target
  - path: history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml
    sha256: 9b4bc4ea429702ab93b8f2cad1cc5518d7a9b8ec75ffb9cc86b37652e3aa0fe7
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.json
    sha256: bb159c4337de6f01565d04f1e0690b34aec0ed43a722b7004d95515f41c6f0cc
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.md
    sha256: 4be24aeb244eccde8a9fb1335608d162ce50544319b3480b1e8acd0cf171cacf
    role: context
  - path: reviews/structured/20261024T074000Z-behoite-round120/review.yaml
    sha256: 6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:behoite
  path: data/records/behoite.yaml
  label: Behoite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/behoite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml
    role: canonical_history
scope:
  description: Scoped scientific reassessment of data/records/behoite.yaml (SHA-256
    fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5) following LinkML
    Mechanism and Source schema updates, linked to prior scientific review 20261024T074000Z-behoite-round120
    (pre-edit target SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e).
  selection: Targeted post-fix scientific reassessment of record with updated mechanisms[0]
    and sources fields.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:behoite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/behoite.yaml
  locator: Complete post-fix working-tree record data/records/behoite.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Post-fix record data/records/behoite.yaml (SHA-256 fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5)
    conforms to LinkML Source and Mechanism schemas with unchanged species-level identity
    fields and primary-source-verified abiotic mechanism fields.
  snapshot_sha256: fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5
- evidence_id: prior_review
  kind: record_content
  reference: reviews/structured/20261024T074000Z-behoite-round120/review.yaml
  locator: Restored initial scientific review reviews/structured/20261024T074000Z-behoite-round120/review.yaml
    (target SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e)
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Prior scientific review 20261024T074000Z-behoite-round120 (review.yaml
    SHA-256 6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139) assessed
    pre-edit record SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e;
    id, name, material_kind, description, identifiers, relations, history_refs, and
    curation_history are unchanged.
  snapshot_sha256: 6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139
- evidence_id: primary_study
  kind: primary_source
  reference: https://www.rruff.net/doclib/am/vol55/AM55_1.pdf
  locator: AM 55 (1970) 1-9, p. 7 and Fig. 4 (DTA of Rode Ranch behoite on DuPont
    900 analyzer at 20 °C/min in air flow)
  accessed_at: '2026-10-24T10:05:00Z'
  support: supports
  summary: 'Rechecked mechanisms[0] (abiotic_dta_dehydroxylation: process=other, microbial=false,
    description, context, and evidence) against Ehlmann & Mitchell (1970) p. 7: DuPont
    900 DTA at 20 °C/min in air shows a two-step endothermic dehydroxylation of natural
    orthorhombic beta-Be(OH)2 with inflections beginning at ~265 °C and ~290 °C and
    peaking at 310 °C; no microbial or bioleaching mechanism was tested.'
  snapshot_sha256: 55b96a29f37e83fa65031512839d76b4a953d2d757fd17ec03c7c3d74d0911da
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List (244 pages visually inspected)
  accessed_at: '2026-10-24T10:05:00Z'
  support: supports
  summary: Confirms official mineral species identity, formula, and IMA approval tag
    (IMA:1969-031) for Behoite.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: history
  kind: record_content
  reference: history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml
  locator: Canonical CREATE sidecar history/records/behoite/2026-10-24T073000Z-antigravity-001201.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Canonical CREATE history sidecar is unchanged and passes validate-history
    against the Git base.
  snapshot_sha256: 9b4bc4ea429702ab93b8f2cad1cc5518d7a9b8ec75ffb9cc86b37652e3aa0fe7
- evidence_id: validation
  kind: validation
  reference: data/records/behoite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s).
  snapshot_sha256: fbf0a40a0a08f20ac40f1d9ae7ed47a42da8c36c528eda622a45fda2c663d4e5
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 662 record(s); 0 failed.
  target_ids:
  - cmmmech:behoite
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
  - cmmmech:behoite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: mechanism_and_evidence_reassessment
  area: evidence
  topic: Post-fix primary-source recheck of abiotic mechanism and identity fields
    for behoite
  outcome: supported
  summary: 'Rechecked mechanisms[0] (abiotic_dta_dehydroxylation: process=other, microbial=false,
    description, context, and evidence) against Ehlmann & Mitchell (1970) p. 7: DuPont
    900 DTA at 20 °C/min in air shows a two-step endothermic dehydroxylation of natural
    orthorhombic beta-Be(OH)2 with inflections beginning at ~265 °C and ~290 °C and
    peaking at 310 °C; no microbial or bioleaching mechanism was tested.'
  target_ids:
  - cmmmech:behoite
  evidence_ids:
  - owner
  - prior_review
  - primary_study
  - ima_authority
- assessment_id: scope_and_provenance
  area: provenance
  topic: LinkML Mechanism/Source schema compliance and provenance integrity
  outcome: supported
  summary: Species-level fields (id, name, material_kind, description, identifiers,
    history_refs, curation_history) match prior review 20261024T074000Z-behoite-round120
    (pre-edit SHA-256 f2cda541297f491444c609d688fd6fda124112deeb8ebf25bd473a786908861e);
    updated mechanisms[0] and sources fields pass strict LinkML validation.
  target_ids:
  - cmmmech:behoite
  evidence_ids:
  - owner
  - prior_review
  - history
  - validation
findings: []
actions: []
summary: 'Behoite (IMA:1969-031) passes post-schema-fix scientific reassessment (scientific_review:
  true, linked to 20261024T074000Z-behoite-round120): Rechecked mechanisms[0] (abiotic_dta_dehydroxylation:
  process=other, microbial=false, description, context, and evidence) against Ehlmann
  & Mitchell (1970) p. 7: DuPont 900 DTA at 20 °C/min in air shows a two-step endothermic
  dehydroxylation of natural orthorhombic beta-Be(OH)2 with inflections beginning
  at ~265 °C and ~290 °C and peaking at 310 °C; no microbial or bioleaching mechanism
  was tested.'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.'
- 'Reported mechanism is strictly abiotic laboratory thermal/topotactic behavior (microbial:
  false); no biological processing or industrial recovery yield is reported in the
  primary source.'
notes:
- Prior scientific review 20261024T074000Z-behoite-round120 was restored to its exact
  092942 SHA-256 (6440e46e58cc544a0a26ad17cbb39e84060974233fc955d2fa6d87dbe08ec139)
  before appending this reassessment bundle.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261024T074000Z-behoite-round120
  relationship: post_schema_fix_scientific_reassessment
```
