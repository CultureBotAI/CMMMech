# PR

- Review: 20261115T042221Z-acanthite-pr1004-fix-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-15T04:20:23Z
- Finished UTC: 2026-11-15T04:22:21Z
- Reviewer: codex / cmmmech-pr1004-fix-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Acanthite passes the focused PR

## Scope And Provenance

Review of the final PR

Selection: PR
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a71f064a761609077b865bdb9bcc892c567d3a68.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:acanthite | data/records/acanthite.yaml | maintained | Acanthite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict affected-record validation | passed | True | cmmmech:acanthite | Checked 6 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:acanthite | Checked 1589 history record(s); 0 error(s). |
| Static page freshness | passed | True | cmmmech:acanthite | pages/ is current. |

## Scientific And Domain Assessments

### CopA NCBIfam and CysI edge repair

graph: supported. Targets: cmmmech:acanthite.

The record uses the live CopA NCBIfam assignments and no longer asserts that proxy CysI directly transforms the AgNO3 agar substrate.

### Correction sidecar and validation

provenance: supported. Targets: cmmmech:acanthite.

The correction is represented by a new append-only history sidecar and the final bytes pass affected validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/acanthite.yaml | supports | The record now carries live CopA NCBIfam values at mechanism and causal-node scope and routes CysI through an endogenous_h2s_generation node before proposed Ag2S formation. |
| history | history/records/acanthite/2026-11-15T042023Z-codex-104f01.yaml | supports | Canonical sidecar records the PR review correction of CopA NCBIfam metadata and the CysI/H2S graph route. |
| uniprot | https://rest.uniprot.org/uniprotkb/search | supports | Live UniProtKB returned F8H4S1 with NCBIfam TIGR01480 and TIGR01409. |
| validation | local validation commands | supports | The repaired record passed strict record validation, history validation, and regenerated-page freshness checks. |

## Limits And Additional Notes

- This successor review focuses on PR

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T042221Z-acanthite-pr1004-fix-review
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
  - path: data/records/acanthite.yaml
    sha256: a3bad04e8e6bd9eec7efd44375afbb8fbcf8d32d99669399de1fa90251120f36
    role: target
  - path: history/records/acanthite/2026-11-15T042023Z-codex-104f01.yaml
    sha256: a2f72cd30035226c6790a1375daebbf05198e4029c8db16675760275f24facf3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:acanthite
  path: data/records/acanthite.yaml
  label: Acanthite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/acanthite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/acanthite/2026-11-15T042023Z-codex-104f01.yaml
    role: canonical_history
scope:
  description: Review of the final PR
  selection: PR
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:acanthite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/acanthite.yaml
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: The record now carries live CopA NCBIfam values at mechanism and causal-node
    scope and routes CysI through an endogenous_h2s_generation node before proposed
    Ag2S formation.
  snapshot_sha256: a3bad04e8e6bd9eec7efd44375afbb8fbcf8d32d99669399de1fa90251120f36
- evidence_id: history
  kind: record_content
  reference: history/records/acanthite/2026-11-15T042023Z-codex-104f01.yaml
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: Canonical sidecar records the PR review correction of CopA NCBIfam metadata
    and the CysI/H2S graph route.
  snapshot_sha256: a2f72cd30035226c6790a1375daebbf05198e4029c8db16675760275f24facf3
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search
  accessed_at: '2026-11-15T04:22:21Z'
  support: supports
  summary: Live UniProtKB returned F8H4S1 with NCBIfam TIGR01480 and TIGR01409.
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
  - cmmmech:acanthite
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
  - cmmmech:acanthite
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
  - cmmmech:acanthite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_and_graph_fix
  area: graph
  topic: CopA NCBIfam and CysI edge repair
  outcome: supported
  summary: The record uses the live CopA NCBIfam assignments and no longer asserts
    that proxy CysI directly transforms the AgNO3 agar substrate.
  target_ids:
  - cmmmech:acanthite
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
  - cmmmech:acanthite
  evidence_ids:
  - history
  - validation
findings: []
actions: []
summary: Acanthite passes the focused PR
limitations:
- This successor review focuses on PR
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261111T142200Z-acanthite-cycle14-stage3-protein-examples-review
  relationship: supersedes the pre-fix PR
links:
- https://github.com/CultureBotAI/CMMMech/issues/1005
- https://github.com/CultureBotAI/CMMMech/issues/1006
tags:
- pr1004
- cycle14-stage3
```
