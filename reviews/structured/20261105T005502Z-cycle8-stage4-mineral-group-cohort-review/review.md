# Cycle 8 Stage 4 full-cohort review: mineral_group records (7/7)

- Review: 20261105T005502Z-cycle8-stage4-mineral-group-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-05T00:38:00Z
- Finished UTC: 2026-11-05T00:55:02Z
- Reviewer: antigravity / cmmmech-cycle8-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 7 mineral_group records in data/records/*.yaml at commit 573410374de4d10b2595b6bf75a1f2138ea33ed7 (apatite-group, chlorite-group, eudialyte-group, illite-group, monazite-group, pyrochlore-group, smectite-group). All 7/7 mineral_group records contain primary-source-supported microbial mechanisms (7 mechanisms total), and 2/7 (cmmmech:illite-group and cmmmech:smectite-group) contain causal_graphs (2 graphs, 6 GENE_OR_PROTEIN nodes: 6 GROUNDED and 0 UNGROUNDED) grounded to 7 unique Shewanella oneidensis MR-1 UniProtKB accessions (CymA, MtrA, MtrB, MtrC, OmcA, CctA, FccA). Confirmed 0 open findings in this cohort.

## Scope And Provenance

Full-population Cycle 8 Stage 4 category review of all 7 mineral_group records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral_group' at 573410374de4d10b2595b6bf75a1f2138ea33ed7
Coverage: full; 7 reviewed / 7 in the declared population.
Source: git_commit at Git base 573410374de4d10b2595b6bf75a1f2138ea33ed7.
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
| just validate (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### Mineral group vs endmember species distinction, microbial mechanisms, and Shewanella MR-1 causal graphs

evidence: supported. Targets: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite.

All 7 mineral_group records pass all schema, semantic, key-order, and primary-source mechanism checks with 0 open findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite. All 7 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral_group' at 573410374de4d10b2595b6bf75a1f2138ea33ed7 with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-mineral-group-cohort-audit | data/records/*.yaml (material_kind == 'mineral_group'); 7 mineral_group YAML files | supports | Full programmatic and source-backed audit of all 7 mineral_group records at commit 573410374de4d10b2595b6bf75a1f2138ea33ed7. |

## Limits And Additional Notes

- 5 of 7 mineral_group records (apatite-group, chlorite-group, eudialyte-group, monazite-group, pyrochlore-group) have organic-acid or heterotrophic bioleaching mechanisms without strain-resolved enzymatic causal graphs in the cited primary studies.
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit 573410374de4d10b2595b6bf75a1f2138ea33ed7.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T005502Z-cycle8-stage4-mineral-group-cohort-review
title: 'Cycle 8 Stage 4 full-cohort review: mineral_group records (7/7)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-05T00:38:00Z'
finished_at: '2026-11-05T00:55:02Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 7 mineral_group records in data/records/*.yaml at commit 573410374de4d10b2595b6bf75a1f2138ea33ed7
  (apatite-group, chlorite-group, eudialyte-group, illite-group, monazite-group, pyrochlore-group,
  smectite-group). All 7/7 mineral_group records contain primary-source-supported
  microbial mechanisms (7 mechanisms total), and 2/7 (cmmmech:illite-group and cmmmech:smectite-group)
  contain causal_graphs (2 graphs, 6 GENE_OR_PROTEIN nodes: 6 GROUNDED and 0 UNGROUNDED)
  grounded to 7 unique Shewanella oneidensis MR-1 UniProtKB accessions (CymA, MtrA,
  MtrB, MtrC, OmcA, CctA, FccA). Confirmed 0 open findings in this cohort.'
reviewer:
  identity: antigravity / cmmmech-cycle8-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 8 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 573410374de4d10b2595b6bf75a1f2138ea33ed7.
source:
  git_revision: 573410374de4d10b2595b6bf75a1f2138ea33ed7
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
    sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
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
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
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
  selection: data/records/*.yaml where material_kind == 'mineral_group' at 573410374de4d10b2595b6bf75a1f2138ea33ed7
  description: Full-population Cycle 8 Stage 4 category review of all 7 mineral_group
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
  command: .venv/bin/cmmmech validate --require-records
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
  summary: All 7 mineral_group records pass LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-mineral-groups
  name: just verify-history (mineral_group cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
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
  topic: Mineral group vs endmember species distinction, microbial mechanisms, and
    Shewanella MR-1 causal graphs
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
  summary: All 7 mineral_group records pass all schema, semantic, key-order, and primary-source
    mechanism checks with 0 open findings.
findings: []
actions: []
evidence:
- evidence_id: ev-mineral-group-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'mineral_group')
  locator: 7 mineral_group YAML files
  accessed_at: '2026-11-05T00:55:02Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 7 mineral_group records
    at commit 573410374de4d10b2595b6bf75a1f2138ea33ed7.
limitations:
- 5 of 7 mineral_group records (apatite-group, chlorite-group, eudialyte-group, monazite-group,
  pyrochlore-group) have organic-acid or heterotrophic bioleaching mechanisms without
  strain-resolved enzymatic causal graphs in the cited primary studies.
notes:
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit
  573410374de4d10b2595b6bf75a1f2138ea33ed7.
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
    matching data/records/*.yaml where material_kind == 'mineral_group' at 573410374de4d10b2595b6bf75a1f2138ea33ed7
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-mineral-group-cohort-audit
```
