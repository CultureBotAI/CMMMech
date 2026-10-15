# Independent heterosite review: nonexistent methods subsection range

- Review: 20261015T125439Z-heterosite-round95-initial-locator
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T12:49:49Z
- Finished UTC: 2026-10-15T12:54:39.662974Z
- Reviewer: codex /root/round68_iron_sulfides (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor source locator defect: Reich2024 has section 2 and subsection 2.1, not sections 2.1–2.3. This initial observation preserves the current frozen bytes while final batch checks remain pending.

## Scope And Provenance

Scoped initial source-locator finding during independent whole-record assessment.

Selection: Assigned frozen heterosite owner.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 73d4b1c42541ee7ca139effae00b94ddb1c8a631.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:heterosite | data/records/heterosite.yaml | maintained | Heterosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original complete methods and section sequence | passed | True | cmmmech:heterosite | Read the complete 18-page original; page 3 contains section 2 Materials and methods and 2.1 Experimental, then 3 Results/3.1 Material characterization. No methods sections 2.2 or 2.3 occur. |
| Final corrected owner and batch validation | unavailable | True | cmmmech:heterosite | Current root batch is running. No completed final receipt or corrected owner exists at this observation. |

## Scientific And Domain Assessments

### Exact primary methods locator

consistency: concern. Targets: cmmmech:heterosite.

Replace the nonexistent subsection range with section 2 and subsection 2.1 on PDF page 3; scientific values and limitations need no change for this finding.

## Findings

### F1: Correct the nonexistent Reich2024 methods subsection range

minor / open / confirmed; issue key: heterosite-round95-methods-section-locator.

sources[id=reich2024].title says methods sections 2.1–2.3, but the full original has section 2 Materials and methods and only subsection 2.1 Experimental on PDF page 3, followed directly by section 3. Correct that source locator without changing the supported experiments or quantitative caveats.

## Recommended Actions And Acceptance Checks

### A1

After the running baseline-input batch terminates and root releases correction, change only the source methods locator, append actual inline EDIT and canonical history, then independently save a successor resolving this exact F1 occurrence.

- Source identifies section 2 and subsection 2.1 on PDF page 3.
- Supported scientific fields and original CREATE remain unchanged; original review remains immutable.
- Named and required final batch checks pass, and successor binds final owner/history and this exact predecessor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/heterosite.yaml; sources[id=reich2024].title | supports | The source description claims methods sections 2.1–2.3. |
| primary | https://publikationen.bibliothek.kit.edu/1000172429/153604117; Complete original PDF page 3, section 2 Materials and methods and 2.1 Experimental, followed directly by section 3 Results. Actual local artifact: /private/tmp/cmm-round95-minerals-research/reich2024.pdf | refutes | The primary has only subsection 2.1 under section 2. The extra methods subsection numbers are not present. |

## Limits And Additional Notes

- Scoped initial finding, not final whole-record acceptance. Source methods and all main results/graphics were inspected; supplementary workbook assessment and final batch checks continue.
- Natural Eventoff1972 identity and engineered Reich2024 sorbent remain separate; no microbial, criticality or pure recovered-product claim is introduced.
- Two external unsaved drafting attempts were rejected for YAML aliases and target-kind formatting; preserved outside Git, normalized before this sole saved observation. No prior immutable review was altered.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T125439Z-heterosite-round95-initial-locator
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent heterosite review: nonexistent methods subsection range'
started_at: '2026-10-15T12:49:49Z'
finished_at: '2026-10-15T12:54:39.662974Z'
reviewer:
  identity: codex /root/round68_iron_sulfides
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Phosphate agent authored heterosite. I authored separate hauerite/melanterite
    records and independently inspected this owner/history before reading the full
    original and graphics; no owner changes.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One minor source locator defect: Reich2024 has section 2 and subsection
  2.1, not sections 2.1–2.3. This initial observation preserves the current frozen
  bytes while final batch checks remain pending.'
source:
  git_revision: 73d4b1c42541ee7ca139effae00b94ddb1c8a631
  state: working_tree
  inputs:
  - path: data/records/heterosite.yaml
    sha256: ab138bec6a2ec7951640720e6063b42ea253c92409fca4a64cf9b350343c87d4
    role: target
  - path: history/records/heterosite/2026-10-15T124517Z-codex-52e820.yaml
    sha256: cd714f8c462c7748ff19c70b2532b660f3445267f249b0ed10959677297f418a
    role: context
targets:
- target_id: cmmmech:heterosite
  path: data/records/heterosite.yaml
  label: Heterosite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heterosite.yaml
    role: maintained scientific record
scope:
  description: Scoped initial source-locator finding during independent whole-record
    assessment.
  selection: Assigned frozen heterosite owner.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:heterosite
checks:
- check_id: original
  name: Original complete methods and section sequence
  required: true
  status: passed
  summary: Read the complete 18-page original; page 3 contains section 2 Materials
    and methods and 2.1 Experimental, then 3 Results/3.1 Material characterization.
    No methods sections 2.2 or 2.3 occur.
  target_ids:
  - cmmmech:heterosite
  evidence_ids:
  - owner
  - primary
- check_id: final
  name: Final corrected owner and batch validation
  required: true
  status: unavailable
  summary: Current root batch is running. No completed final receipt or corrected
    owner exists at this observation.
  target_ids:
  - cmmmech:heterosite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/heterosite.yaml
  locator: sources[id=reich2024].title
  accessed_at: '2026-10-15T12:54:39.662974Z'
  support: supports
  snapshot_sha256: ab138bec6a2ec7951640720e6063b42ea253c92409fca4a64cf9b350343c87d4
  summary: The source description claims methods sections 2.1–2.3.
- evidence_id: primary
  kind: primary_source
  reference: https://publikationen.bibliothek.kit.edu/1000172429/153604117
  locator: 'Complete original PDF page 3, section 2 Materials and methods and 2.1
    Experimental, followed directly by section 3 Results. Actual local artifact: /private/tmp/cmm-round95-minerals-research/reich2024.pdf'
  accessed_at: '2026-10-15T12:54:39.662974Z'
  support: refutes
  snapshot_sha256: 26a6095b8aef3e0e8ea227dcd3a08b7772de169695b423d5a52d36c91b156286
  summary: The primary has only subsection 2.1 under section 2. The extra methods
    subsection numbers are not present.
assessments:
- assessment_id: locator
  area: consistency
  topic: Exact primary methods locator
  outcome: concern
  target_ids:
  - cmmmech:heterosite
  evidence_ids:
  - owner
  - primary
  summary: Replace the nonexistent subsection range with section 2 and subsection
    2.1 on PDF page 3; scientific values and limitations need no change for this finding.
findings:
- finding_id: F1
  issue_key: heterosite-round95-methods-section-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the nonexistent Reich2024 methods subsection range
  description: sources[id=reich2024].title says methods sections 2.1–2.3, but the
    full original has section 2 Materials and methods and only subsection 2.1 Experimental
    on PDF page 3, followed directly by section 3. Correct that source locator without
    changing the supported experiments or quantitative caveats.
  target_ids:
  - cmmmech:heterosite
  field_paths:
  - sources[id=reich2024].title
  evidence_ids:
  - owner
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heterosite.yaml
    role: maintained scientific record
  rule_id: exact-primary-locator
  native_severity: minor
  normalization_reason: Bounded source-navigation error; this observation does not
    identify an unsupported material identity or quantitative mechanism claim.
actions:
- action_id: A1
  description: After the running baseline-input batch terminates and root releases
    correction, change only the source methods locator, append actual inline EDIT
    and canonical history, then independently save a successor resolving this exact
    F1 occurrence.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:heterosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heterosite.yaml
    role: maintained scientific record
  acceptance_checks:
  - Source identifies section 2 and subsection 2.1 on PDF page 3.
  - Supported scientific fields and original CREATE remain unchanged; original review
    remains immutable.
  - Named and required final batch checks pass, and successor binds final owner/history
    and this exact predecessor.
limitations:
- Scoped initial finding, not final whole-record acceptance. Source methods and all
  main results/graphics were inspected; supplementary workbook assessment and final
  batch checks continue.
- Natural Eventoff1972 identity and engineered Reich2024 sorbent remain separate;
  no microbial, criticality or pure recovered-product claim is introduced.
- Two external unsaved drafting attempts were rejected for YAML aliases and target-kind
  formatting; preserved outside Git, normalized before this sole saved observation.
  No prior immutable review was altered.
```
