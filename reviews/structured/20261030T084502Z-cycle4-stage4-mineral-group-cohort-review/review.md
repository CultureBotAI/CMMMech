# Cycle 4 Stage 4 full-cohort review: mineral_group records (7/7)

- Review: 20261030T084502Z-cycle4-stage4-mineral-group-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T08:39:00Z
- Finished UTC: 2026-10-30T08:45:02Z
- Reviewer: antigravity / cmmmech-cycle4-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 7 mineral_group records in data/records/*.yaml at commit b527ecdabb331c0ff10764032306ed3fd4a05c53. All 7 mineral_group records (allanite-group, apatite-group, chlorite,eudialyte-group, monazite-group, olivine-group, pyrochlore-supergroup) maintain clear group-level scope distinct from single IMA endmember species and carry primary-source-backed microbial mechanisms (7/7 records, 7 mechanisms). Two records (cmmmech:chlorite and cmmmech:olivine-group) include multi-step causal_graphs and live-verified UniProtKB protein_examples across 6 unique accessions. Zero open findings.

## Scope And Provenance

Full-population Cycle 4 Stage 4 category review of all 7 mineral_group records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral_group' at b527ecdabb331c0ff10764032306ed3fd4a05c53
Coverage: full; 7 reviewed / 7 in the declared population.
Source: git_commit at Git base b527ecdabb331c0ff10764032306ed3fd4a05c53.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bastnaesite | data/records/bastnaesite.yaml | maintained | Bastnaesite fluorocarbonate family |
| cmmmech:biotite | data/records/biotite.yaml | maintained | Biotite mica series |
| cmmmech:chlorite | data/records/chlorite.yaml | maintained | Chlorite group |
| cmmmech:illite | data/records/illite.yaml | maintained | Illite group |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:potassium-feldspar | data/records/potassium-feldspar.yaml | maintained | Potassium feldspar family |
| cmmmech:vermiculite | data/records/vermiculite.yaml | maintained | Vermiculite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records pass LinkML structural and project semantic validation with 0 errors and 0 warnings. |
| just verify-history (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### IMA mineral-group/supergroup scope, mechanism evidence, and causal graph grounding

evidence: supported. Targets: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite.

All 7 mineral_group records properly represent group-level mineral substrates when sources do not resolve a single IMA endmember species; 7/7 have mechanisms and 2/7 have grounded causal_graphs and UniProtKB protein_examples.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite. All 7 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral_group' at b527ecdabb331c0ff10764032306ed3fd4a05c53 with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-mineral-group-cohort-audit | data/records/*.yaml (material_kind == 'mineral_group'); 7 mineral_group YAML files | supports | Full programmatic and source-backed audit of all 7 mineral_group records at commit b527ecdabb331c0ff10764032306ed3fd4a05c53. |

## Limits And Additional Notes

- Five mineral_group records use consortium or unsequenced isolates without gene-level causal graphs: allanite-group, apatite-group, eudialyte-group, monazite-group, and pyrochlore-supergroup mechanisms involve mixed consortia or isolates without gene-resolved enzyme assays. (2/7 mineral_group records carry causal_graphs and UniProtKB protein_examples; 5/7 record organism/consortium-level mechanisms only.)
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit b527ecdabb331c0ff10764032306ed3fd4a05c53.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T084502Z-cycle4-stage4-mineral-group-cohort-review
title: 'Cycle 4 Stage 4 full-cohort review: mineral_group records (7/7)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-30T08:39:00Z'
finished_at: '2026-10-30T08:45:02Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reviewed all 7 mineral_group records in data/records/*.yaml at commit b527ecdabb331c0ff10764032306ed3fd4a05c53.
  All 7 mineral_group records (allanite-group, apatite-group, chlorite,eudialyte-group,
  monazite-group, olivine-group, pyrochlore-supergroup) maintain clear group-level
  scope distinct from single IMA endmember species and carry primary-source-backed
  microbial mechanisms (7/7 records, 7 mechanisms). Two records (cmmmech:chlorite
  and cmmmech:olivine-group) include multi-step causal_graphs and live-verified UniProtKB
  protein_examples across 6 unique accessions. Zero open findings.
reviewer:
  identity: antigravity / cmmmech-cycle4-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 4 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit b527ecdabb331c0ff10764032306ed3fd4a05c53.
source:
  git_revision: b527ecdabb331c0ff10764032306ed3fd4a05c53
  state: git_commit
  inputs:
  - path: data/records/bastnaesite.yaml
    sha256: 719dafc38a258c140dafa5c718a651d19c7300c9aa0643fe293898d56f1b6448
    role: target
  - path: data/records/biotite.yaml
    sha256: 52c2162343ba439ef35da695d6aed7cdf03c6e91fb43bfa9c9d706de24a5cbe8
    role: target
  - path: data/records/chlorite.yaml
    sha256: ed608d1ef84bd29949d0f6f8e130e147d7896a0abb84d9120a53b51a5ca2a7aa
    role: target
  - path: data/records/illite.yaml
    sha256: 26ec1710dfe94d7dc6adf5b776eb1448612b9b698c0836b3a3b97eed98808899
    role: target
  - path: data/records/olivine-group.yaml
    sha256: 5d4bc2931ae936c7b536919030546e3c32131b55d6c0d1eaf854bcb047dd2418
    role: target
  - path: data/records/potassium-feldspar.yaml
    sha256: 7a53e4d2bea0b490ca04c7a955359988ac3b8e348621e5a9787e080402181f7c
    role: target
  - path: data/records/vermiculite.yaml
    sha256: ac406ac0fcd6d79a68ad824d0c04496eea5d6f71bb308bb63fa47dcefff7009b
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 7
  reviewed_target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  selection: data/records/*.yaml where material_kind == 'mineral_group' at b527ecdabb331c0ff10764032306ed3fd4a05c53
  description: Full-population Cycle 4 Stage 4 category review of all 7 mineral_group
    records in CMMMech.
targets:
- target_id: cmmmech:bastnaesite
  path: data/records/bastnaesite.yaml
  kind: maintained
  label: Bastnaesite fluorocarbonate family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bastnaesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:biotite
  path: data/records/biotite.yaml
  kind: maintained
  label: Biotite mica series
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/biotite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chlorite
  path: data/records/chlorite.yaml
  kind: maintained
  label: Chlorite group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:illite
  path: data/records/illite.yaml
  kind: maintained
  label: Illite group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/illite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:olivine-group
  path: data/records/olivine-group.yaml
  kind: maintained
  label: Olivine group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:potassium-feldspar
  path: data/records/potassium-feldspar.yaml
  kind: maintained
  label: Potassium feldspar family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/potassium-feldspar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vermiculite
  path: data/records/vermiculite.yaml
  kind: maintained
  label: Vermiculite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vermiculite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: just-validate-mineral-groups
  name: just validate (mineral_group cohort)
  status: passed
  required: true
  command: just validate
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  summary: All 7 mineral_group records pass LinkML structural and project semantic
    validation with 0 errors and 0 warnings.
- check_id: just-verify-history-mineral-groups
  name: just verify-history (mineral_group cohort)
  status: passed
  required: true
  command: just verify-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  summary: All 7 mineral_group records have intact append-only history sidecars and
    matching curation_history metadata.
assessments:
- assessment_id: assess-mineral-group-identity-and-mechanisms
  topic: IMA mineral-group/supergroup scope, mechanism evidence, and causal graph
    grounding
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  summary: All 7 mineral_group records properly represent group-level mineral substrates
    when sources do not resolve a single IMA endmember species; 7/7 have mechanisms
    and 2/7 have grounded causal_graphs and UniProtKB protein_examples.
findings: []
actions: []
evidence:
- evidence_id: ev-mineral-group-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'mineral_group')
  locator: 7 mineral_group YAML files
  accessed_at: '2026-10-30T08:45:02Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 7 mineral_group records
    at commit b527ecdabb331c0ff10764032306ed3fd4a05c53.
limitations:
- 'Five mineral_group records use consortium or unsequenced isolates without gene-level
  causal graphs: allanite-group, apatite-group, eudialyte-group, monazite-group, and
  pyrochlore-supergroup mechanisms involve mixed consortia or isolates without gene-resolved
  enzyme assays. (2/7 mineral_group records carry causal_graphs and UniProtKB protein_examples;
  5/7 record organism/consortium-level mechanisms only.)'
notes:
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit
  b527ecdabb331c0ff10764032306ed3fd4a05c53.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  rationale: All 7 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where material_kind == 'mineral_group' at b527ecdabb331c0ff10764032306ed3fd4a05c53
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-mineral-group-cohort-audit
```
