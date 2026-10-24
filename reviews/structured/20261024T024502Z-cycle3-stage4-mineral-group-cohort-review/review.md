# Cycle 3 Stage 4 full-cohort review: mineral_group records (7/7)

- Review: 20261024T024502Z-cycle3-stage4-mineral-group-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T02:37:00Z
- Finished UTC: 2026-10-24T02:45:02Z
- Reviewer: antigravity / cmmmech-cycle3-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 7 mineral_group records in data/records/*.yaml at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite). All 7/7 mineral_group records carry primary-source-backed microbial mechanisms, and 2/7 (chlorite and olivine-group) carry grounded multi-step causal_graphs with live-verified UniProtKB protein_examples across 6 unique UniProtKB accessions. Recorded one minor consistency finding (cmmmech-cycle3-stage4-finding-0002) on cmmmech:olivine-group, which keys the 2019 IMA-CNMNC Nomenclature Compendium under id: ima_compendium instead of canonical id: ima_compendium_2019 used by the other 4 mineral_group records citing that compilation.

## Scope And Provenance

Full-population Cycle 3 Stage 4 category review of all 7 mineral_group records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral_group' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
Coverage: full; 7 reviewed / 7 in the declared population.
Source: git_commit at Git base 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
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
| cmmmech validate (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 records in the mineral_group cohort pass LinkML structural and semantic validation with 0 errors. |
| cmmmech validate-history (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All curation_history entries and history_refs sidecars across the 7 mineral_group records resolve and validate cleanly. |
| Ontology ID-label consistency (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 7 mineral_group records carries a consistent canonical label with 0 cross-corpus conflicts. |

## Scientific And Domain Assessments

### Mineral group boundaries, member mineral cross-references, and microbial mechanisms

completeness: supported. Targets: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite.

All 7 mineral_group records pass LinkML validation and history checks, linking group-level critical mineral designations and member mineral species to primary microbial extraction/dissolution literature (7/7 with microbial mechanisms; 2/7 with multi-step causal_graphs and UniProtKB protein_examples).

### Canonical 2019 IMA-CNMNC Nomenclature Compendium source key (ima_compendium_2019) across mineral_group records

consistency: concern. Targets: cmmmech:olivine-group.

data/records/olivine-group.yaml keys the 2019 IMA-CNMNC Nomenclature Compendium under id: ima_compendium instead of canonical id: ima_compendium_2019 used across biotite, chlorite, illite, and potassium-feldspar.

## Findings

### cmmmech-cycle3-stage4-finding-0002: cmmmech:olivine-group keys the 2019 IMA-CNMNC Nomenclature Compendium under ima_compendium instead of ima_compendium_2019

minor / open / confirmed; issue key: cmmmech.mineral_group.noncanonical-ima-compendium-source-id.

Across the 5 mineral_group records citing the 2019 IMA-CNMNC Nomenclature Compendium (https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf), 4 records (cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, and cmmmech:potassium-feldspar) key this compilation under id: ima_compendium_2019, whereas data/records/olivine-group.yaml (line 11) keys the identical URL under id: ima_compendium.

## Recommended Actions And Acceptance Checks

### action-normalize-olivine-group-ima-compendium-source-id

Normalize sources[0].id in data/records/olivine-group.yaml from ima_compendium to ima_compendium_2019 and record an EDIT history sidecar during Stage 5.

- data/records/olivine-group.yaml keys the 2019 IMA-CNMNC Nomenclature Compendium source under id: ima_compendium_2019, matching biotite, chlorite, illite, and potassium-feldspar.
- A matching EDIT history sidecar exists in history/records/olivine-group/ and passes cmmmech validate --require-records and cmmmech validate-history --base main.

## Category Boundaries

- retain: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite. All 7 records in the mineral_group cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral_group' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cmmmech-validate | src/cmmmech/validation.py; cmmmech validate --require-records | supports | LinkML structural and semantic validator passed across all 646 records (including the mineral_group cohort) with 0 errors. |
| ev-cmmmech-history | src/cmmmech/history.py; cmmmech validate-history --base main | supports | All 962 curation history sidecars in history/records/ and record history_refs passed validation with 0 errors. |
| ev-cohort-audit | src/cmmmech/schema/cmmmech.yaml; Cycle 3 Stage 4 full-inventory cohort audit (mineral_group) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e | supports | Full-inventory inspection of all records in the mineral_group cohort verified distinct material identities, source-backed criticality/mechanism claims, and 100% CURIE label consistency across 181 distinct ontology terms. |
| ev-olivine-group-ima-compendium-source-id | data/records/olivine-group.yaml; lines 11-14 (sources[0].id: ima_compendium) vs data/records/{biotite,chlorite,illite,potassium-feldspar}.yaml (id: ima_compendium_2019) | partial | 4 of 5 mineral_group records citing the 2019 IMA-CNMNC Nomenclature Compendium (https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf) key it under id: ima_compendium_2019 (biotite, chlorite, illite, potassium-feldspar), whereas data/records/olivine-group.yaml keys the same URL under id: ima_compendium. |

## Limits And Additional Notes

- data/records/olivine-group.yaml uses source key ima_compendium instead of canonical ima_compendium_2019 (tracked as open finding cmmmech-cycle3-stage4-finding-0002 for Stage 5 remediation).
- 5 of 7 mineral_group records document group-level microbial bioleaching or mineral-weathering studies without resolved multi-step enzymatic intermediates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T024502Z-cycle3-stage4-mineral-group-cohort-review
title: 'Cycle 3 Stage 4 full-cohort review: mineral_group records (7/7)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-24T02:37:00Z'
finished_at: '2026-10-24T02:45:02Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 7 mineral_group records in data/records/*.yaml at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite).
  All 7/7 mineral_group records carry primary-source-backed microbial mechanisms,
  and 2/7 (chlorite and olivine-group) carry grounded multi-step causal_graphs with
  live-verified UniProtKB protein_examples across 6 unique UniProtKB accessions. Recorded
  one minor consistency finding (cmmmech-cycle3-stage4-finding-0002) on cmmmech:olivine-group,
  which keys the 2019 IMA-CNMNC Nomenclature Compendium under id: ima_compendium instead
  of canonical id: ima_compendium_2019 used by the other 4 mineral_group records citing
  that compilation.'
reviewer:
  identity: antigravity / cmmmech-cycle3-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 3 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
source:
  git_revision: 855e0eba1fa9b8a4a975b7155ec013414e4d437e
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
    sha256: 1017cd19a6a93cccff1eeb3d7ababb11eecf12b41e45cbd56f5be48610419af3
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
  selection: data/records/*.yaml where material_kind == 'mineral_group' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  description: Full-population Cycle 3 Stage 4 category review of all 7 mineral_group
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
- check_id: cmmmech-validate-cohort
  name: cmmmech validate (mineral_group cohort)
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
  - ev-cmmmech-validate
  summary: All 7 records in the mineral_group cohort pass LinkML structural and semantic
    validation with 0 errors.
- check_id: cmmmech-validate-history-cohort
  name: cmmmech validate-history (mineral_group cohort)
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
  - ev-cmmmech-history
  summary: All curation_history entries and history_refs sidecars across the 7 mineral_group
    records resolve and validate cleanly.
- check_id: curie-label-consistency-cohort
  name: Ontology ID-label consistency (mineral_group cohort)
  status: passed
  required: true
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-cohort-audit
  summary: Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 7
    mineral_group records carries a consistent canonical label with 0 cross-corpus
    conflicts.
assessments:
- assessment_id: assess-mineral-group-cohort
  topic: Mineral group boundaries, member mineral cross-references, and microbial
    mechanisms
  area: completeness
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
  - ev-cmmmech-validate
  - ev-cmmmech-history
  - ev-cohort-audit
  summary: All 7 mineral_group records pass LinkML validation and history checks,
    linking group-level critical mineral designations and member mineral species to
    primary microbial extraction/dissolution literature (7/7 with microbial mechanisms;
    2/7 with multi-step causal_graphs and UniProtKB protein_examples).
  metrics:
  - name: reviewed_mineral_groups
    value: 7.0
    unit: records
    definition: Total mineral_group records reviewed in the cohort.
    minimum: 0.0
    maximum: 7.0
  - name: mineral_groups_with_mechanisms
    value: 7.0
    unit: records
    definition: Mineral group records carrying primary-source microbial mechanisms.
    minimum: 0.0
    maximum: 7.0
  - name: mineral_groups_with_causal_graphs
    value: 2.0
    unit: records
    definition: Mineral group records carrying multi-step causal_graphs and UniProtKB
      protein_examples.
    minimum: 0.0
    maximum: 7.0
- assessment_id: assess-mineral-group-ima-compendium-source-id
  topic: Canonical 2019 IMA-CNMNC Nomenclature Compendium source key (ima_compendium_2019)
    across mineral_group records
  area: consistency
  outcome: concern
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - ev-olivine-group-ima-compendium-source-id
  summary: 'data/records/olivine-group.yaml keys the 2019 IMA-CNMNC Nomenclature Compendium
    under id: ima_compendium instead of canonical id: ima_compendium_2019 used across
    biotite, chlorite, illite, and potassium-feldspar.'
findings:
- finding_id: cmmmech-cycle3-stage4-finding-0002
  issue_key: cmmmech.mineral_group.noncanonical-ima-compendium-source-id
  title: cmmmech:olivine-group keys the 2019 IMA-CNMNC Nomenclature Compendium under
    ima_compendium instead of ima_compendium_2019
  category: consistency
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - ev-olivine-group-ima-compendium-source-id
  description: 'Across the 5 mineral_group records citing the 2019 IMA-CNMNC Nomenclature
    Compendium (https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf),
    4 records (cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, and cmmmech:potassium-feldspar)
    key this compilation under id: ima_compendium_2019, whereas data/records/olivine-group.yaml
    (line 11) keys the identical URL under id: ima_compendium.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
actions:
- action_id: action-normalize-olivine-group-ima-compendium-source-id
  finding_ids:
  - cmmmech-cycle3-stage4-finding-0002
  target_ids:
  - cmmmech:olivine-group
  description: Normalize sources[0].id in data/records/olivine-group.yaml from ima_compendium
    to ima_compendium_2019 and record an EDIT history sidecar during Stage 5.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  acceptance_checks:
  - 'data/records/olivine-group.yaml keys the 2019 IMA-CNMNC Nomenclature Compendium
    source under id: ima_compendium_2019, matching biotite, chlorite, illite, and
    potassium-feldspar.'
  - A matching EDIT history sidecar exists in history/records/olivine-group/ and passes
    cmmmech validate --require-records and cmmmech validate-history --base main.
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
  rationale: All 7 records in the mineral_group cohort denote distinct, non-synonymous
    entities matching data/records/*.yaml where material_kind == 'mineral_group' at
    855e0eba1fa9b8a4a975b7155ec013414e4d437e with no duplicate IDs, names, or external
    identifier collisions.
  evidence_ids:
  - ev-cohort-audit
evidence:
- evidence_id: ev-cmmmech-validate
  kind: validation
  reference: src/cmmmech/validation.py
  locator: cmmmech validate --require-records
  accessed_at: '2026-10-24T02:45:02Z'
  support: supports
  summary: LinkML structural and semantic validator passed across all 646 records
    (including the mineral_group cohort) with 0 errors.
- evidence_id: ev-cmmmech-history
  kind: validation
  reference: src/cmmmech/history.py
  locator: cmmmech validate-history --base main
  accessed_at: '2026-10-24T02:45:02Z'
  support: supports
  summary: All 962 curation history sidecars in history/records/ and record history_refs
    passed validation with 0 errors.
- evidence_id: ev-cohort-audit
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Cycle 3 Stage 4 full-inventory cohort audit (mineral_group) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  accessed_at: '2026-10-24T02:45:02Z'
  support: supports
  summary: Full-inventory inspection of all records in the mineral_group cohort verified
    distinct material identities, source-backed criticality/mechanism claims, and
    100% CURIE label consistency across 181 distinct ontology terms.
- evidence_id: ev-olivine-group-ima-compendium-source-id
  kind: record_content
  reference: data/records/olivine-group.yaml
  locator: 'lines 11-14 (sources[0].id: ima_compendium) vs data/records/{biotite,chlorite,illite,potassium-feldspar}.yaml
    (id: ima_compendium_2019)'
  accessed_at: '2026-10-24T02:45:02Z'
  support: partial
  summary: '4 of 5 mineral_group records citing the 2019 IMA-CNMNC Nomenclature Compendium
    (https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf)
    key it under id: ima_compendium_2019 (biotite, chlorite, illite, potassium-feldspar),
    whereas data/records/olivine-group.yaml keys the same URL under id: ima_compendium.'
limitations:
- data/records/olivine-group.yaml uses source key ima_compendium instead of canonical
  ima_compendium_2019 (tracked as open finding cmmmech-cycle3-stage4-finding-0002
  for Stage 5 remediation).
- 5 of 7 mineral_group records document group-level microbial bioleaching or mineral-weathering
  studies without resolved multi-step enzymatic intermediates.
notes: []
```
