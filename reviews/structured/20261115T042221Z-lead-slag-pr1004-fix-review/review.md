# PR

- Review: 20261115T042221Z-lead-slag-pr1004-fix-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-15T04:20:23Z
- Finished UTC: 2026-11-15T04:22:21Z
- Reviewer: codex / cmmmech-pr1004-fix-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Lead blast-furnace slag passes the focused PR

## Scope And Provenance

Review of the final PR

Selection: PR
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a71f064a761609077b865bdb9bcc892c567d3a68.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lead-blast-furnace-slag | data/records/lead-blast-furnace-slag.yaml | maintained | Lead blast-furnace slag |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict affected-record validation | passed | True | cmmmech:lead-blast-furnace-slag | Checked 6 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:lead-blast-furnace-slag | Checked 1589 history record(s); 0 error(s). |
| Static page freshness | passed | True | cmmmech:lead-blast-furnace-slag | pages/ is current. |

## Scientific And Domain Assessments

### FpvA NCBIfam repair

grounding: supported. Targets: cmmmech:lead-blast-furnace-slag.

Both FpvA protein-example copies now match the live UniProtKB NCBIfam metadata.

### Correction sidecar and validation

provenance: supported. Targets: cmmmech:lead-blast-furnace-slag.

The correction is represented by a new append-only history sidecar and the final bytes pass affected validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lead-blast-furnace-slag.yaml | supports | FpvA now carries live NCBIfam:TIGR01783 at mechanism and causal-node scope. |
| history | history/records/lead-blast-furnace-slag/2026-11-15T042023Z-codex-cf2ce7.yaml | supports | Canonical sidecar records the FpvA NCBIfam metadata correction. |
| uniprot | https://rest.uniprot.org/uniprotkb/search | supports | Live UniProtKB returned P48632 with NCBIfam TIGR01783. |
| validation | local validation commands | supports | The repaired record passed strict record validation, history validation, and regenerated-page freshness checks. |

## Limits And Additional Notes

- This successor review focuses on PR

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T042221Z-lead-slag-pr1004-fix-review
kind: record
repository: CultureBotAI/CMMMech
title: PR
started_at: '2026-11-15T04:20:23Z'
finished_at: '2026-11-15T04:22:21Z'
reviewer:
  identity: codex / cmmmech-pr1004-fix-reviewer
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Fresh final-state review after independent PR
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a71f064a761609077b865bdb9bcc892c567d3a68
  state: working_tree
  inputs:
  - path: data/records/lead-blast-furnace-slag.yaml
    sha256: 23bbd0da785fc54a83699c19efda5285a3c589a1200d265f7ef4244d96aa20a1
    role: target
  - path: history/records/lead-blast-furnace-slag/2026-11-15T042023Z-codex-cf2ce7.yaml
    sha256: b52e8252a2f06730a71893c2dfb5d6c27e70500174f06ffaaa8e2a144abb8c7b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:lead-blast-furnace-slag
  path: data/records/lead-blast-furnace-slag.yaml
  label: Lead blast-furnace slag
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lead-blast-furnace-slag.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/lead-blast-furnace-slag/2026-11-15T042023Z-codex-cf2ce7.yaml
    role: canonical_history
scope:
  description: Review of the final PR
  selection: PR
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lead-blast-furnace-slag
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lead-blast-furnace-slag.yaml
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: FpvA now carries live NCBIfam:TIGR01783 at mechanism and causal-node scope.
  snapshot_sha256: 23bbd0da785fc54a83699c19efda5285a3c589a1200d265f7ef4244d96aa20a1
- evidence_id: history
  kind: record_content
  reference: history/records/lead-blast-furnace-slag/2026-11-15T042023Z-codex-cf2ce7.yaml
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: Canonical sidecar records the FpvA NCBIfam metadata correction.
  snapshot_sha256: b52e8252a2f06730a71893c2dfb5d6c27e70500174f06ffaaa8e2a144abb8c7b
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: Live UniProtKB returned P48632 with NCBIfam TIGR01783.
- evidence_id: validation
  kind: validation
  reference: local validation commands
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: The repaired record passed strict record validation, history validation,
    and regenerated-page freshness checks.
checks:
- check_id: validate_record
  name: Strict affected-record validation
  command: uv run --locked cmmmech validate data/records/acanthite.yaml data/records/lead-blast-furnace-slag.yaml
    data/records/monazite-ore.yaml data/records/pyrite.yaml data/records/kornelite.yaml
    data/records/stibnite.yaml
  status: passed
  required: true
  summary: Checked 6 record(s); 0 failed.
  target_ids:
  - cmmmech:lead-blast-furnace-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: uv run --locked cmmmech validate-history --base origin/main
  status: passed
  required: true
  summary: Checked 1589 history record(s); 0 error(s).
  target_ids:
  - cmmmech:lead-blast-furnace-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: render_check
  name: Static page freshness
  command: just render-check
  status: passed
  required: true
  summary: pages/ is current.
  target_ids:
  - cmmmech:lead-blast-furnace-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_metadata_fix
  area: grounding
  topic: FpvA NCBIfam repair
  outcome: supported
  summary: Both FpvA protein-example copies now match the live UniProtKB NCBIfam metadata.
  target_ids:
  - cmmmech:lead-blast-furnace-slag
  evidence_ids:
  - record
  - uniprot
- assessment_id: provenance
  area: provenance
  topic: Correction sidecar and validation
  outcome: supported
  summary: The correction is represented by a new append-only history sidecar and
    the final bytes pass affected validation.
  target_ids:
  - cmmmech:lead-blast-furnace-slag
  evidence_ids:
  - history
  - validation
findings: []
actions: []
summary: Lead blast-furnace slag passes the focused PR
limitations:
- This successor review focuses on PR
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261111T142200Z-lead-blast-furnace-slag-cycle14-stage3-protein-examples-review
  relationship: supersedes the pre-fix PR
links:
- https://github.com/CultureBotAI/CMMMech/issues/1005
tags:
- pr1004
- cycle14-stage3
```
