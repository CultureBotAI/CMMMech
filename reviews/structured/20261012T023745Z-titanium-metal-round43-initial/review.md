# Independent initial review of titanium-metal extension

- Review: 20261012T023745Z-titanium-metal-round43-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T02:36:20.048613Z
- Finished UTC: 2026-10-12T02:37:45.377120Z
- Reviewer: Codex /root (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The narrow culture-associated workflow is supported, but a source average-size qualifier was dropped. One minor correction is needed; finalbatchgates have not run yet.

## Scope And Provenance

Whole updated record, focus on the new fullprimary experiment and preserved commodity/criticality boundaries.

Selection: Independent peer-authored record review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 59e24ec38d9c7b377dcfeade1637b298aab9623e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:titanium-metal | data/records/titanium-metal.yaml | maintained | Titanium metal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:titanium-metal | Root executed in explicit round43 cwd; 1 record,0failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final batch validation | skipped | True | cmmmech:titanium-metal | Not yet executed; cohort is still being curated. This initial observation is partial, not an acceptance claim. |

## Scientific And Domain Assessments

### Average versus individual particle bound

quantity: concern. Targets: cmmmech:titanium-metal.

One minor qualifier must be restored; original evidence does not justify a maximum over every grain.

### Culture-containing mechanical and chemical workflow

evidence: supported. Targets: cmmmech:titanium-metal.

Source supports a reported workflow with mixed compounds and missing controls, not pureTi yield or established microbial advantage.

## Findings

### F1: Restore the average-grain-size qualifier

minor / open / confirmed; issue key: CMMMech.titanium-metal.average-grain-size.

The source page134 says the average grain size does not exceed150–200nm. The record says grains no larger than150–200nm, dropping average and implying a bound on individual grains. The source supplies no counted distribution. Preserve the reported mean/average qualifier without turning it into a measured maximum.

## Recommended Actions And Acceptance Checks

### A1

Restore source average-grain-size qualifier and append actual correction history; preserve other limitations.

- Wording explicitly attributes150–200nm to the source average estimate, not individual maximum.
- Named/nonempty/history/batch gates pass and successor review binds finalbytes with exact predecessor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/titanium-metal.yaml; Exact inspected fullrecord, evidence item2 in mechanism0 | partial | The text omits average before its grain-size upper-bound wording. |
| primary | https://journal.mmi.kpi.ua/old/article/view/29005/28485; Original printed page134, prose immediately beneath Figure3; complete original pages131–135 visually inspected | refutes | Russian prose explicitly qualifies the150–200nm estimate as average grain size. TEM captions conflict with bars and no particle distribution is supplied. Other record qualifications accurately preserve pooled feeds, compounds, absent matchedcontrols and non-yield composition. |

## Limits And Additional Notes

- Initial scientific review only; full finalcohort checks pending.
- No reprocessing of microscopy or XRD; source lacks displayed diffractogram and matchedcontrols.
- Final independent acceptance and issue disposition require a successor; this artifact remains immutable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T023745Z-titanium-metal-round43-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial review of titanium-metal extension
started_at: '2026-10-12T02:36:20.048613Z'
finished_at: '2026-10-12T02:37:45.377120Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Extension/history/dossier authored by /root/round43_hardmetal.
    Root assigned scope but authored none of its scientific bytes; personally read
    all5original pages and captured native hashes before assessment.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The narrow culture-associated workflow is supported, but a source average-size
  qualifier was dropped. One minor correction is needed; finalbatchgates have not
  run yet.
source:
  git_revision: 59e24ec38d9c7b377dcfeade1637b298aab9623e
  state: working_tree
  inputs:
  - path: data/records/titanium-metal.yaml
    sha256: 627a897cadf7c806be66e6fc0a7b8c0f2928f374f6a8a1c56768409a1016718e
    role: target
  - path: history/records/titanium-metal/2026-10-12T023444Z-codex-ff8e43.yaml
    sha256: 75908fd0a32abbaf58ad8e34cc5e79a43a510a9ff175c5d18dcf38faf8629bf4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:titanium-metal
  path: data/records/titanium-metal.yaml
  label: Titanium metal
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanium-metal.yaml
    role: maintained_record
scope:
  description: Whole updated record, focus on the new fullprimary experiment and preserved
    commodity/criticality boundaries.
  selection: Independent peer-authored record review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:titanium-metal
checks:
- check_id: named
  name: Named record validation
  command: uv run --locked cmmmech validate data/records/titanium-metal.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:titanium-metal
  summary: Root executed in explicit round43 cwd; 1 record,0failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Final batch validation
  command: just check
  status: skipped
  required: true
  target_ids:
  - cmmmech:titanium-metal
  summary: Not yet executed; cohort is still being curated. This initial observation
    is partial, not an acceptance claim.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/titanium-metal.yaml
  locator: Exact inspected fullrecord, evidence item2 in mechanism0
  accessed_at: '2026-10-12T02:37:45.377120Z'
  support: partial
  summary: The text omits average before its grain-size upper-bound wording.
  snapshot_sha256: 627a897cadf7c806be66e6fc0a7b8c0f2928f374f6a8a1c56768409a1016718e
- evidence_id: primary
  kind: primary_source
  reference: https://journal.mmi.kpi.ua/old/article/view/29005/28485
  locator: Original printed page134, prose immediately beneath Figure3; complete original
    pages131–135 visually inspected
  accessed_at: '2026-10-12T02:37:45.377120Z'
  support: refutes
  summary: Russian prose explicitly qualifies the150–200nm estimate as average grain
    size. TEM captions conflict with bars and no particle distribution is supplied.
    Other record qualifications accurately preserve pooled feeds, compounds, absent
    matchedcontrols and non-yield composition.
  snapshot_sha256: 15dc0b0689cd17d66d7cdf9920a56fe5db32b096ab7f739a2f6099072c779602
assessments:
- assessment_id: size
  area: quantity
  topic: Average versus individual particle bound
  outcome: concern
  target_ids:
  - cmmmech:titanium-metal
  evidence_ids:
  - record
  - primary
  summary: One minor qualifier must be restored; original evidence does not justify
    a maximum over every grain.
- assessment_id: scope
  area: evidence
  topic: Culture-containing mechanical and chemical workflow
  outcome: supported
  target_ids:
  - cmmmech:titanium-metal
  evidence_ids:
  - record
  - primary
  summary: Source supports a reported workflow with mixed compounds and missing controls,
    not pureTi yield or established microbial advantage.
findings:
- title: Restore the average-grain-size qualifier
  finding_id: F1
  issue_key: CMMMech.titanium-metal.average-grain-size
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - cmmmech:titanium-metal
  field_paths:
  - mechanisms/0/evidence/2/explanation
  evidence_ids:
  - primary
  - record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanium-metal.yaml
    role: maintained_record
  description: The source page134 says the average grain size does not exceed150–200nm.
    The record says grains no larger than150–200nm, dropping average and implying
    a bound on individual grains. The source supplies no counted distribution. Preserve
    the reported mean/average qualifier without turning it into a measured maximum.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cmmmech:titanium-metal
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanium-metal.yaml
    role: maintained_record
  description: Restore source average-grain-size qualifier and append actual correction
    history; preserve other limitations.
  acceptance_checks:
  - Wording explicitly attributes150–200nm to the source average estimate, not individual
    maximum.
  - Named/nonempty/history/batch gates pass and successor review binds finalbytes
    with exact predecessor.
limitations:
- Initial scientific review only; full finalcohort checks pending.
- No reprocessing of microscopy or XRD; source lacks displayed diffractogram and matchedcontrols.
notes:
- Final independent acceptance and issue disposition require a successor; this artifact
  remains immutable.
```
