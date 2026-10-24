# Post-schema-fix scientific and mechanism reassessment of petscheckite

- Review: 20261024T100600Z-petscheckite-round120-reassessment
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T10:02:00Z
- Finished UTC: 2026-10-24T10:06:00Z
- Reviewer: antigravity / round120-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Petscheckite (IMA:1975-038) passes post-schema-fix scientific reassessment (scientific_review: true, linked to 20261024T074000Z-petscheckite-round120): Rechecked mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other, microbial=false, description, context, and evidence) against Mücke &amp; Strunz (1978) pp. 941-945: heating metamict oxy-petscheckite at red heat (~650 °C) restores trigonal P-31m crystallinity (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity from 5.0 to 5.5, whereas heating hydroxy-petscheckite for 24 h at 1000 °C dehydrates and disproportionates it into cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus oxy-petscheckite and 3 H2O.

## Scope And Provenance

Scoped scientific reassessment of data/records/petscheckite.yaml (SHA-256 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44) following LinkML Mechanism and Source schema updates, linked to prior scientific review 20261024T074000Z-petscheckite-round120 (pre-edit target SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d).

Selection: Targeted post-fix scientific reassessment of record with updated mechanisms[0] and sources fields.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2b18e567096cceeb767514d9cec5d99e75688aef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:petscheckite | data/records/petscheckite.yaml | maintained | Petscheckite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:petscheckite | Checked 662 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:petscheckite | Checked 981 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Post-fix primary-source recheck of abiotic mechanism and identity fields for petscheckite

evidence: supported. Targets: cmmmech:petscheckite.

Rechecked mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other, microbial=false, description, context, and evidence) against Mücke &amp; Strunz (1978) pp. 941-945: heating metamict oxy-petscheckite at red heat (~650 °C) restores trigonal P-31m crystallinity (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity from 5.0 to 5.5, whereas heating hydroxy-petscheckite for 24 h at 1000 °C dehydrates and disproportionates it into cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus oxy-petscheckite and 3 H2O.

### LinkML Mechanism/Source schema compliance and provenance integrity

provenance: supported. Targets: cmmmech:petscheckite.

Species-level fields (id, name, material_kind, description, identifiers, history_refs, curation_history) match prior review 20261024T074000Z-petscheckite-round120 (pre-edit SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d); updated mechanisms[0] and sources fields pass strict LinkML validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/petscheckite.yaml; Complete post-fix working-tree record data/records/petscheckite.yaml | supports | Post-fix record data/records/petscheckite.yaml (SHA-256 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44) conforms to LinkML Source and Mechanism schemas with unchanged species-level identity fields and primary-source-verified abiotic mechanism fields. |
| prior_review | reviews/structured/20261024T074000Z-petscheckite-round120/review.yaml; Restored initial scientific review reviews/structured/20261024T074000Z-petscheckite-round120/review.yaml (target SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d) | supports | Prior scientific review 20261024T074000Z-petscheckite-round120 (review.yaml SHA-256 e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1) assessed pre-edit record SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d; id, name, material_kind, description, identifiers, relations, history_refs, and curation_history are unchanged. |
| primary_study | https://www.rruff.net/doclib/am/vol63/AM63_941.pdf; AM 63 (1978) 941-946, pp. 941-945, Tables 3-6 (650 °C red-heat annealing and 1000 °C 24-hour calcination) | supports | Rechecked mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other, microbial=false, description, context, and evidence) against Mücke &amp; Strunz (1978) pp. 941-945: heating metamict oxy-petscheckite at red heat (~650 °C) restores trigonal P-31m crystallinity (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity from 5.0 to 5.5, whereas heating hydroxy-petscheckite for 24 h at 1000 °C dehydrates and disproportionates it into cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus oxy-petscheckite and 3 H2O. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Confirms official mineral species identity, formula, and IMA approval tag (IMA:1975-038) for Petscheckite. |
| history | history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml; Canonical CREATE sidecar history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml | supports | Canonical CREATE history sidecar is unchanged and passes validate-history against the Git base. |
| validation | data/records/petscheckite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history | supports | Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.
- Reported mechanism is strictly abiotic laboratory thermal/topotactic behavior (microbial: false); no biological processing or industrial recovery yield is reported in the primary source.
- Prior scientific review 20261024T074000Z-petscheckite-round120 was restored to its exact 092942 SHA-256 (e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1) before appending this reassessment bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T100600Z-petscheckite-round120-reassessment
kind: record
repository: CultureBotAI/CMMMech
title: Post-schema-fix scientific and mechanism reassessment of petscheckite
started_at: '2026-10-24T10:02:00Z'
finished_at: '2026-10-24T10:06:00Z'
reviewer:
  identity: antigravity / round120-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    following LinkML Source and Mechanism schema edits to data/records/petscheckite.yaml;
    rechecked updated mechanisms[0] fields (process, microbial, description, context,
    evidence) directly against the primary source PDF (AM 63 (1978) 941-946, pp. 941-945,
    Tables 3-6 (650 °C red-heat annealing and 1000 °C 24-hour calcination)) and verified
    species-level field invariance against prior review 20261024T074000Z-petscheckite-round120
    (pre-edit SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 2b18e567096cceeb767514d9cec5d99e75688aef
  state: working_tree
  inputs:
  - path: data/records/petscheckite.yaml
    sha256: 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44
    role: target
  - path: history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml
    sha256: 7b763c9f4acfc7d60cb8f7e205709e0c04bb2e47cdcbcf6a65e80dae7b4a1b18
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.json
    sha256: bb159c4337de6f01565d04f1e0690b34aec0ed43a722b7004d95515f41c6f0cc
    role: context
  - path: research/sources/round120-minerals/20261024T073500Z-source-investigation.md
    sha256: 4be24aeb244eccde8a9fb1335608d162ce50544319b3480b1e8acd0cf171cacf
    role: context
  - path: reviews/structured/20261024T074000Z-petscheckite-round120/review.yaml
    sha256: e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:petscheckite
  path: data/records/petscheckite.yaml
  label: Petscheckite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/petscheckite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml
    role: canonical_history
scope:
  description: Scoped scientific reassessment of data/records/petscheckite.yaml (SHA-256
    7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44) following LinkML
    Mechanism and Source schema updates, linked to prior scientific review 20261024T074000Z-petscheckite-round120
    (pre-edit target SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d).
  selection: Targeted post-fix scientific reassessment of record with updated mechanisms[0]
    and sources fields.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:petscheckite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/petscheckite.yaml
  locator: Complete post-fix working-tree record data/records/petscheckite.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Post-fix record data/records/petscheckite.yaml (SHA-256 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44)
    conforms to LinkML Source and Mechanism schemas with unchanged species-level identity
    fields and primary-source-verified abiotic mechanism fields.
  snapshot_sha256: 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44
- evidence_id: prior_review
  kind: record_content
  reference: reviews/structured/20261024T074000Z-petscheckite-round120/review.yaml
  locator: Restored initial scientific review reviews/structured/20261024T074000Z-petscheckite-round120/review.yaml
    (target SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d)
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Prior scientific review 20261024T074000Z-petscheckite-round120 (review.yaml
    SHA-256 e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1) assessed
    pre-edit record SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d;
    id, name, material_kind, description, identifiers, relations, history_refs, and
    curation_history are unchanged.
  snapshot_sha256: e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1
- evidence_id: primary_study
  kind: primary_source
  reference: https://www.rruff.net/doclib/am/vol63/AM63_941.pdf
  locator: AM 63 (1978) 941-946, pp. 941-945, Tables 3-6 (650 °C red-heat annealing
    and 1000 °C 24-hour calcination)
  accessed_at: '2026-10-24T10:05:00Z'
  support: supports
  summary: 'Rechecked mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other,
    microbial=false, description, context, and evidence) against Mücke & Strunz (1978)
    pp. 941-945: heating metamict oxy-petscheckite at red heat (~650 °C) restores
    trigonal P-31m crystallinity (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity
    from 5.0 to 5.5, whereas heating hydroxy-petscheckite for 24 h at 1000 °C dehydrates
    and disproportionates it into cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus
    oxy-petscheckite and 3 H2O.'
  snapshot_sha256: 50e2b26aa61b68f2299fc5fed93eaf78220c6332e1187cf710339ca14f24d45e
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List (244 pages visually inspected)
  accessed_at: '2026-10-24T10:05:00Z'
  support: supports
  summary: Confirms official mineral species identity, formula, and IMA approval tag
    (IMA:1975-038) for Petscheckite.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: history
  kind: record_content
  reference: history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml
  locator: Canonical CREATE sidecar history/records/petscheckite/2026-10-24T073000Z-antigravity-00120b.yaml
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Canonical CREATE history sidecar is unchanged and passes validate-history
    against the Git base.
  snapshot_sha256: 7b763c9f4acfc7d60cb8f7e205709e0c04bb2e47cdcbcf6a65e80dae7b4a1b18
- evidence_id: validation
  kind: validation
  reference: data/records/petscheckite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history
  accessed_at: '2026-10-24T10:06:00Z'
  support: supports
  summary: Checked 662 record(s); 0 failed. Checked 981 history record(s); 0 error(s).
  snapshot_sha256: 7c91292b84e94cf61446493922896bdb5a27f7357fb99c627bab12f9a8321b44
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 662 record(s); 0 failed.
  target_ids:
  - cmmmech:petscheckite
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
  - cmmmech:petscheckite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: mechanism_and_evidence_reassessment
  area: evidence
  topic: Post-fix primary-source recheck of abiotic mechanism and identity fields
    for petscheckite
  outcome: supported
  summary: 'Rechecked mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other,
    microbial=false, description, context, and evidence) against Mücke & Strunz (1978)
    pp. 941-945: heating metamict oxy-petscheckite at red heat (~650 °C) restores
    trigonal P-31m crystallinity (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity
    from 5.0 to 5.5, whereas heating hydroxy-petscheckite for 24 h at 1000 °C dehydrates
    and disproportionates it into cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus
    oxy-petscheckite and 3 H2O.'
  target_ids:
  - cmmmech:petscheckite
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
    history_refs, curation_history) match prior review 20261024T074000Z-petscheckite-round120
    (pre-edit SHA-256 b6306b83e89a6ee11134bf58278d4de1446ec86aa04a65dc2292a280b24c895d);
    updated mechanisms[0] and sources fields pass strict LinkML validation.
  target_ids:
  - cmmmech:petscheckite
  evidence_ids:
  - owner
  - prior_review
  - history
  - validation
findings: []
actions: []
summary: 'Petscheckite (IMA:1975-038) passes post-schema-fix scientific reassessment
  (scientific_review: true, linked to 20261024T074000Z-petscheckite-round120): Rechecked
  mechanisms[0] (abiotic_metamict_thermal_recrystallization: process=other, microbial=false,
  description, context, and evidence) against Mücke & Strunz (1978) pp. 941-945: heating
  metamict oxy-petscheckite at red heat (~650 °C) restores trigonal P-31m crystallinity
  (a=6.42 Å, c=4.02 Å, Z=1) and raises specific gravity from 5.0 to 5.5, whereas heating
  hydroxy-petscheckite for 24 h at 1000 °C dehydrates and disproportionates it into
  cubic uranpyrochlore U4+(Nb,Ta)2O7 (a=10.36 Å) plus oxy-petscheckite and 3 H2O.'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes at base 2b18e567096cceeb767514d9cec5d99e75688aef.'
- 'Reported mechanism is strictly abiotic laboratory thermal/topotactic behavior (microbial:
  false); no biological processing or industrial recovery yield is reported in the
  primary source.'
notes:
- Prior scientific review 20261024T074000Z-petscheckite-round120 was restored to its
  exact 092942 SHA-256 (e2fdf43068b1dfbf9f2c4b1d815415de596328ea9dc989db399845759be2c7b1)
  before appending this reassessment bundle.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261024T074000Z-petscheckite-round120
  relationship: post_schema_fix_scientific_reassessment
```
