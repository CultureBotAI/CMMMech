# Independent argentojarosite review: separated-phase Table 9 locator

- Review: 20261015T114339Z-argentojarosite-round94-initial-locator
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T11:40:38.069803Z
- Finished UTC: 2026-10-15T11:43:39.543196Z
- Reviewer: codex /root (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Minor incorrect page scope for Table 9. Experimental interpretation is supported with explicit limits; final acceptance awaits correction and final batch checks.

## Scope And Provenance

Initial exact source-locator finding from whole-record scientific assessment.

Selection: Assigned frozen argentojarosite owner.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1d40007a3309d6c6f8c845363f96ef0e407306d0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:argentojarosite | data/records/argentojarosite.yaml | maintained | Argentojarosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original table and page inspection | passed | True | cmmmech:argentojarosite | Original PDF page 50 visibly contains Table 9 on printed page 40; sections 3.3-3.5 occupy printed45-51. |
| Corrected final owner and final batch validation | unavailable | True | cmmmech:argentojarosite | Correction and final batch checks have not yet completed. |

## Scientific And Domain Assessments

### Exact primary table location

consistency: concern. Targets: cmmmech:argentojarosite.

A bounded citation locator must separately identify Table9 on printed40.

## Findings

### F1: Separate Table 9 page40 from the sections3.3-3.5 page range

minor / open / confirmed; issue key: argentojarosite-round94-table9-locator.

The evidence cites sections3.3-3.5, Figures14-16 and Table9 row as printed45-51; Table9 is actually on printed40/PDF50. State the separate table page without altering scientific claims.

## Recommended Actions And Acceptance Checks

### A1

Correct only the page scope; append inline EDIT and canonical sidecar, then save an independent successor explicitly resolving F1.

- Table9 printed40/PDF50 is separately located from sections3.3-3.5 printed45-51.
- All scientific values and limits unchanged; original CREATE and review immutable.
- Named, history and final batch checks pass; final successor matches exact owner/history hashes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/argentojarosite.yaml; mechanisms[0].evidence[2].explanation | supports | The locator associates sections3.3-3.5, Figures14-16 and the separate Table9 row with printed pages45-51. |
| primary | https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1374139251&amp;disposition=inline; Original PDF50/printed40 Table9; PDF55-61/printed45-51 separated-phase sections/figures. Actual local artifact: /private/tmp/cmm-round94-sulfates-research/argento2013-thesis.pdf | refutes | Table9 is printed40, outside the owner page range; the experimental result and quantity are correct. |

## Limits And Additional Notes

- This is a scoped initial finding, not final whole-record acceptance. Complete original thesis and claim-bearing figures were inspected; complete2016 journal original remains unacquired.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T114339Z-argentojarosite-round94-initial-locator
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent argentojarosite review: separated-phase Table 9 locator'
started_at: '2026-10-15T11:40:38.069803Z'
finished_at: '2026-10-15T11:43:39.543196Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Iron-sulfides agent authored this owner. Root authored separate
    hydroniumjarosite and independently inspected the argentojarosite owner, history
    and original thesis text/graphics before this finding; no owner edits.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Minor incorrect page scope for Table 9. Experimental interpretation is supported
  with explicit limits; final acceptance awaits correction and final batch checks.
source:
  git_revision: 1d40007a3309d6c6f8c845363f96ef0e407306d0
  state: working_tree
  inputs:
  - path: data/records/argentojarosite.yaml
    sha256: 55913ab2c8f544dc92542c5e6fece98543b41398b2b481c2750aa5321ee0d205
    role: target
  - path: history/records/argentojarosite/2026-10-15T113825Z-codex-e9b5f2.yaml
    sha256: 088a54f3ba1a9fc7cd43c4d391bf60b4f159ceb6e9d27dc32b31d16686c342d4
    role: context
targets:
- target_id: cmmmech:argentojarosite
  path: data/records/argentojarosite.yaml
  label: Argentojarosite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argentojarosite.yaml
    role: maintained record
scope:
  description: Initial exact source-locator finding from whole-record scientific assessment.
  selection: Assigned frozen argentojarosite owner.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:argentojarosite
checks:
- check_id: original
  name: Original table and page inspection
  required: true
  status: passed
  summary: Original PDF page 50 visibly contains Table 9 on printed page 40; sections
    3.3-3.5 occupy printed45-51.
  target_ids:
  - cmmmech:argentojarosite
  evidence_ids:
  - primary
  - owner
- check_id: final
  name: Corrected final owner and final batch validation
  required: true
  status: unavailable
  summary: Correction and final batch checks have not yet completed.
  target_ids:
  - cmmmech:argentojarosite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/argentojarosite.yaml
  locator: mechanisms[0].evidence[2].explanation
  accessed_at: '2026-10-15T11:43:39.543196Z'
  support: supports
  snapshot_sha256: 55913ab2c8f544dc92542c5e6fece98543b41398b2b481c2750aa5321ee0d205
  summary: The locator associates sections3.3-3.5, Figures14-16 and the separate Table9
    row with printed pages45-51.
- evidence_id: primary
  kind: primary_source
  reference: https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1374139251&disposition=inline
  locator: 'Original PDF50/printed40 Table9; PDF55-61/printed45-51 separated-phase
    sections/figures. Actual local artifact: /private/tmp/cmm-round94-sulfates-research/argento2013-thesis.pdf'
  accessed_at: '2026-10-15T11:43:39.543196Z'
  support: refutes
  snapshot_sha256: 6af32243666fc93b40085e6696f48ecb56d5efcd71799404fa0dfbfc39c2a4ca
  summary: Table9 is printed40, outside the owner page range; the experimental result
    and quantity are correct.
assessments:
- assessment_id: locator
  area: consistency
  topic: Exact primary table location
  outcome: concern
  target_ids:
  - cmmmech:argentojarosite
  evidence_ids:
  - owner
  - primary
  summary: A bounded citation locator must separately identify Table9 on printed40.
findings:
- finding_id: F1
  issue_key: argentojarosite-round94-table9-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate Table 9 page40 from the sections3.3-3.5 page range
  description: The evidence cites sections3.3-3.5, Figures14-16 and Table9 row as
    printed45-51; Table9 is actually on printed40/PDF50. State the separate table
    page without altering scientific claims.
  target_ids:
  - cmmmech:argentojarosite
  field_paths:
  - mechanisms[0].evidence[2].explanation
  evidence_ids:
  - owner
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argentojarosite.yaml
    role: maintained scientific owner
  rule_id: exact-primary-locator
  native_severity: minor
  normalization_reason: Minor bibliographic locator defect; identity, experimental
    outcome and source limits remain supported.
actions:
- action_id: A1
  description: Correct only the page scope; append inline EDIT and canonical sidecar,
    then save an independent successor explicitly resolving F1.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:argentojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argentojarosite.yaml
    role: maintained scientific owner
  acceptance_checks:
  - Table9 printed40/PDF50 is separately located from sections3.3-3.5 printed45-51.
  - All scientific values and limits unchanged; original CREATE and review immutable.
  - Named, history and final batch checks pass; final successor matches exact owner/history
    hashes.
limitations:
- This is a scoped initial finding, not final whole-record acceptance. Complete original
  thesis and claim-bearing figures were inspected; complete2016 journal original remains
  unacquired.
```
