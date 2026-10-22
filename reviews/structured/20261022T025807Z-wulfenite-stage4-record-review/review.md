# Stage 4 record review: cmmmech:wulfenite (Wulfenite)

- Review: 20261022T025807Z-wulfenite-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T02:51:00Z
- Finished UTC: 2026-10-22T02:58:07Z
- Reviewer: antigravity / cmmmech-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/wulfenite.yaml (cmmmech:wulfenite) at commit 4d878383c92b44876df3bf166d96637c7581a59e. Wulfenite (PbMoO4) carries an accurate mineral description (noting unrecorded criticality), Handbook of Mineralogy source support (handbook_wulfenite), crystal-growth characterization sources (gracanin2024, gracanin2024_correction), and abiotic sulfidization/molybdenum-leaching mechanism sources (cai2024, cai2024_supplement), but is the only mineral record among all 365 mineral records in CMMMech that omits the September 2026 IMA-CNMNC Master List (ima_2026_09) from sources. Recorded open minor finding cmmmech-stage4-finding-0002 for Stage 5 remediation.

## Scope And Provenance

Single-record Stage 4 audit of cmmmech:wulfenite.

Selection: data/records/wulfenite.yaml at 4d878383c92b44876df3bf166d96637c7581a59e
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4d878383c92b44876df3bf166d96637c7581a59e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:wulfenite | data/records/wulfenite.yaml | maintained | Wulfenite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate wulfenite.yaml | passed | True | cmmmech:wulfenite | data/records/wulfenite.yaml passes LinkML structural and semantic validation. |

## Scientific And Domain Assessments

### Wulfenite formula (PbMoO4), crystal-growth characterization, and abiotic leaching mechanism

identity: supported. Targets: cmmmech:wulfenite.

Wulfenite description stoichiometry (PbMoO4, with unrecorded criticality) and abiotic sulfidization/molybdenum-leaching mechanism (abiotic_sulfidization_and_molybdenum_leaching) are accurately supported by handbook_wulfenite, gracanin2024, gracanin2024_correction, cai2024, and cai2024_supplement.

### IMA-CNMNC Master List (ima_2026_09) citation completeness

provenance: concern. Targets: cmmmech:wulfenite.

cmmmech:wulfenite is the only mineral record out of 365 mineral records that omits ima_2026_09 from its sources list.

## Findings

### cmmmech-stage4-finding-0002: cmmmech:wulfenite is the only mineral record omitting ima_2026_09 from sources

minor / open / confirmed; issue key: cmmmech.wulfenite.missing-ima-master-list-source.

Out of 365 mineral records in data/records/*.yaml, 364 include ima_2026_09 (The New IMA List of Minerals, September 2026, https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) in sources to anchor their IMA-CNMNC species status and formula; data/records/wulfenite.yaml cites handbook_wulfenite, gracanin2024, gracanin2024_correction, cai2024, and cai2024_supplement, omitting ima_2026_09.

## Recommended Actions And Acceptance Checks

### action-add-ima-2026-09-to-wulfenite

Add the standard ima_2026_09 source entry and an EDIT history sidecar to data/records/wulfenite.yaml during Stage 5.

- data/records/wulfenite.yaml includes ima_2026_09 in sources with its canonical title, URL, and 2026 year.
- A matching EDIT history sidecar exists in history/records/wulfenite/ and passes cmmmech validate-history --base main.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-wulfenite-file | data/records/wulfenite.yaml; lines 1-117 | supports | Inspected data/records/wulfenite.yaml: description notes PbMoO4 and unrecorded criticality, sources contains handbook_wulfenite, gracanin2024, gracanin2024_correction, cai2024, and cai2024_supplement, omitting ima_2026_09. |
| ev-handbook-wulfenite | https://www.handbookofmineralogy.org/pdfs/wulfenite.pdf; Handbook of Mineralogy entry for Wulfenite (PbMoO4) | supports | Confirms Wulfenite formula PbMoO4 and tetragonal symmetry. |

## Limits And Additional Notes

- Omits ima_2026_09 from sources (tracked as open finding cmmmech-stage4-finding-0002 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025807Z-wulfenite-stage4-record-review
title: 'Stage 4 record review: cmmmech:wulfenite (Wulfenite)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-22T02:51:00Z'
finished_at: '2026-10-22T02:58:07Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reviewed data/records/wulfenite.yaml (cmmmech:wulfenite) at commit 4d878383c92b44876df3bf166d96637c7581a59e.
  Wulfenite (PbMoO4) carries an accurate mineral description (noting unrecorded criticality),
  Handbook of Mineralogy source support (handbook_wulfenite), crystal-growth characterization
  sources (gracanin2024, gracanin2024_correction), and abiotic sulfidization/molybdenum-leaching
  mechanism sources (cai2024, cai2024_supplement), but is the only mineral record
  among all 365 mineral records in CMMMech that omits the September 2026 IMA-CNMNC
  Master List (ima_2026_09) from sources. Recorded open minor finding cmmmech-stage4-finding-0002
  for Stage 5 remediation.
reviewer:
  identity: antigravity / cmmmech-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Stage 4 record_review (.claude/skills/review-yaml-record/SKILL.md)
    against frozen commit 4d878383c92b44876df3bf166d96637c7581a59e.
source:
  git_revision: 4d878383c92b44876df3bf166d96637c7581a59e
  state: git_commit
  inputs:
  - path: data/records/wulfenite.yaml
    sha256: fd87a4a48ae6ee7ae37a86d2c2f613fde65fd2080b40f44e0ad6830f68df43c7
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:wulfenite
  selection: data/records/wulfenite.yaml at 4d878383c92b44876df3bf166d96637c7581a59e
  description: Single-record Stage 4 audit of cmmmech:wulfenite.
targets:
- target_id: cmmmech:wulfenite
  path: data/records/wulfenite.yaml
  kind: maintained
  label: Wulfenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wulfenite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-wulfenite
  name: cmmmech validate wulfenite.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/wulfenite.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:wulfenite
  evidence_ids:
  - ev-wulfenite-file
  summary: data/records/wulfenite.yaml passes LinkML structural and semantic validation.
assessments:
- assessment_id: assess-wulfenite-identity
  topic: Wulfenite formula (PbMoO4), crystal-growth characterization, and abiotic
    leaching mechanism
  area: identity
  outcome: supported
  target_ids:
  - cmmmech:wulfenite
  evidence_ids:
  - ev-wulfenite-file
  - ev-handbook-wulfenite
  summary: Wulfenite description stoichiometry (PbMoO4, with unrecorded criticality)
    and abiotic sulfidization/molybdenum-leaching mechanism (abiotic_sulfidization_and_molybdenum_leaching)
    are accurately supported by handbook_wulfenite, gracanin2024, gracanin2024_correction,
    cai2024, and cai2024_supplement.
- assessment_id: assess-wulfenite-ima-source
  topic: IMA-CNMNC Master List (ima_2026_09) citation completeness
  area: provenance
  outcome: concern
  target_ids:
  - cmmmech:wulfenite
  evidence_ids:
  - ev-wulfenite-file
  summary: cmmmech:wulfenite is the only mineral record out of 365 mineral records
    that omits ima_2026_09 from its sources list.
findings:
- finding_id: cmmmech-stage4-finding-0002
  issue_key: cmmmech.wulfenite.missing-ima-master-list-source
  title: cmmmech:wulfenite is the only mineral record omitting ima_2026_09 from sources
  category: provenance
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:wulfenite
  evidence_ids:
  - ev-wulfenite-file
  description: Out of 365 mineral records in data/records/*.yaml, 364 include ima_2026_09
    (The New IMA List of Minerals, September 2026, https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf)
    in sources to anchor their IMA-CNMNC species status and formula; data/records/wulfenite.yaml
    cites handbook_wulfenite, gracanin2024, gracanin2024_correction, cai2024, and
    cai2024_supplement, omitting ima_2026_09.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wulfenite.yaml
    role: maintained_record
actions:
- action_id: action-add-ima-2026-09-to-wulfenite
  finding_ids:
  - cmmmech-stage4-finding-0002
  target_ids:
  - cmmmech:wulfenite
  description: Add the standard ima_2026_09 source entry and an EDIT history sidecar
    to data/records/wulfenite.yaml during Stage 5.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wulfenite.yaml
    role: maintained_record
  acceptance_checks:
  - data/records/wulfenite.yaml includes ima_2026_09 in sources with its canonical
    title, URL, and 2026 year.
  - A matching EDIT history sidecar exists in history/records/wulfenite/ and passes
    cmmmech validate-history --base main.
evidence:
- evidence_id: ev-wulfenite-file
  kind: record_content
  reference: data/records/wulfenite.yaml
  locator: lines 1-117
  accessed_at: '2026-10-22T02:58:07Z'
  support: supports
  summary: 'Inspected data/records/wulfenite.yaml: description notes PbMoO4 and unrecorded
    criticality, sources contains handbook_wulfenite, gracanin2024, gracanin2024_correction,
    cai2024, and cai2024_supplement, omitting ima_2026_09.'
- evidence_id: ev-handbook-wulfenite
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/wulfenite.pdf
  locator: Handbook of Mineralogy entry for Wulfenite (PbMoO4)
  accessed_at: '2026-10-22T02:58:07Z'
  support: supports
  summary: Confirms Wulfenite formula PbMoO4 and tetragonal symmetry.
limitations:
- Omits ima_2026_09 from sources (tracked as open finding cmmmech-stage4-finding-0002
  for Stage 5 remediation).
notes: []
```
