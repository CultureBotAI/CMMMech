# Cycle 5 Stage 2 causal-graph review of Allanite concentrate (cmmmech:allanite-concentrate)

- Review: 20261030T171200Z-allanite-concentrate-cycle5-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T17:10:00Z
- Finished UTC: 2026-10-30T17:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Allanite concentrate (cmmmech:allanite-concentrate) passes Cycle 5 Stage 2 causal-graph review (scientific_review: true) at SHA-256 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9: Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph) in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and product edges with supports: refutes and explicit explanations that neither reed_2016 nor borra_2016 tested allanite concentrate.

## Scope And Provenance

Cycle 5 Stage 2 causal-graph review of data/records/allanite-concentrate.yaml (SHA-256 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9) and its canonical EDIT history sidecar (history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml) verifying full synchronization between causal_graphs[0] and mechanisms[0].

Selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:allanite-concentrate
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9e3221733b5efe6fb1be27fcc03692abc3a0de44.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:allanite-concentrate | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:allanite-concentrate | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Synchronization of causal_graphs[0] with mechanisms[0] and primary source (DOI:10.1016/j.hydromet.2016.01.031)

graph: supported. Targets: cmmmech:allanite-concentrate.

Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph) in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and product edges with supports: refutes and explicit explanations that neither reed_2016 nor borra_2016 tested allanite concentrate.

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:allanite-concentrate.

data/records/allanite-concentrate.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/allanite-concentrate.yaml; Working-tree record data/records/allanite-concentrate.yaml | supports | Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph) in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and product edges with supports: refutes and explicit explanations that neither reed_2016 nor borra_2016 tested allanite concentrate. |
| primary_source | DOI:10.1016/j.hydromet.2016.01.031; red. 2016 / Borra CR et al. (2016) Hydrometallurgy 162:73-80, Sections 2-3, Tables 1-4, Figures 1-9 | supports | The record's mechanisms[0] entry explicitly documents that no allanite concentrate experiments are reported in the attached references (reed_2016 tested retorted phosphor powder and fluid catalytic cracking catalyst; borra_2016 tested Greek bauxite residue samples BR1, BR2, and BR4) and sets mechanisms[0].evidence[0].supports to refutes. |
| edit_history | history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml; Canonical EDIT history sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml | supports | Canonical EDIT history sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml (SHA-256 b7ec7393d13e3e9464bde054fddf9e5e874b0b3e20cb3fd22f5420777389a087) records the Cycle 5 Stage 2 causal_graphs[0] update via scripts/curate_causal_graphs.py. |
| validation | data/records/allanite-concentrate.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/allanite-concentrate.yaml and history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml pass strict LinkML schema and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T171200Z-allanite-concentrate-cycle5-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 2 causal-graph review of Allanite concentrate (cmmmech:allanite-concentrate)
started_at: '2026-10-30T17:10:00Z'
finished_at: '2026-10-30T17:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 2 causal_graphs[0] update in data/records/allanite-concentrate.yaml
    (SHA-256 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9) against
    mechanisms[0] and its cited primary source (DOI:10.1016/j.hydromet.2016.01.031).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 9e3221733b5efe6fb1be27fcc03692abc3a0de44
  state: working_tree
  inputs:
  - path: data/records/allanite-concentrate.yaml
    sha256: 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9
    role: target
  - path: history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
    sha256: b7ec7393d13e3e9464bde054fddf9e5e874b0b3e20cb3fd22f5420777389a087
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:allanite-concentrate
  path: data/records/allanite-concentrate.yaml
  label: Allanite concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
    role: canonical_history
scope:
  description: Cycle 5 Stage 2 causal-graph review of data/records/allanite-concentrate.yaml
    (SHA-256 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9) and
    its canonical EDIT history sidecar (history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml)
    verifying full synchronization between causal_graphs[0] and mechanisms[0].
  selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:allanite-concentrate
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:allanite-concentrate
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/allanite-concentrate.yaml
  locator: Working-tree record data/records/allanite-concentrate.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph)
    in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific
    BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and
    product edges with supports: refutes and explicit explanations that neither reed_2016
    nor borra_2016 tested allanite concentrate.'
  snapshot_sha256: 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1016/j.hydromet.2016.01.031
  locator: red. 2016 / Borra CR et al. (2016) Hydrometallurgy 162:73-80, Sections
    2-3, Tables 1-4, Figures 1-9
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: The record's mechanisms[0] entry explicitly documents that no allanite
    concentrate experiments are reported in the attached references (reed_2016 tested
    retorted phosphor powder and fluid catalytic cracking catalyst; borra_2016 tested
    Greek bauxite residue samples BR1, BR2, and BR4) and sets mechanisms[0].evidence[0].supports
    to refutes.
- evidence_id: edit_history
  kind: record_content
  reference: history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
  locator: Canonical EDIT history sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: Canonical EDIT history sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
    (SHA-256 b7ec7393d13e3e9464bde054fddf9e5e874b0b3e20cb3fd22f5420777389a087) records
    the Cycle 5 Stage 2 causal_graphs[0] update via scripts/curate_causal_graphs.py.
  snapshot_sha256: b7ec7393d13e3e9464bde054fddf9e5e874b0b3e20cb3fd22f5420777389a087
- evidence_id: validation
  kind: validation
  reference: data/records/allanite-concentrate.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: data/records/allanite-concentrate.yaml and history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
    pass strict LinkML schema and history validation with 0 errors.
  snapshot_sha256: 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:allanite-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: All history sidecars pass validation with 0 errors.
  target_ids:
  - cmmmech:allanite-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_mechanism_synchronization
  area: graph
  topic: Synchronization of causal_graphs[0] with mechanisms[0] and primary source
    (DOI:10.1016/j.hydromet.2016.01.031)
  outcome: supported
  summary: 'Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph)
    in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific
    BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and
    product edges with supports: refutes and explicit explanations that neither reed_2016
    nor borra_2016 tested allanite concentrate.'
  target_ids:
  - cmmmech:allanite-concentrate
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: data/records/allanite-concentrate.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar history/records/allanite-concentrate/2026-10-30T171003Z-marcin-894052.yaml
    and passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:allanite-concentrate
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Allanite concentrate (cmmmech:allanite-concentrate) passes Cycle 5 Stage
  2 causal-graph review (scientific_review: true) at SHA-256 5ff8f325fe6c9edb11534431427b11a2c617145e9a97d7de1b2449143b8b0ad9:
  Synchronized causal_graphs[0] (aspergillus_allanite_concentrate_bioleaching_graph)
  in data/records/allanite-concentrate.yaml with mechanisms[0]: replaced over-specific
  BR1/BR2/BR4 bauxite residue labels and supports: support on the substrate and product
  edges with supports: refutes and explicit explanations that neither reed_2016 nor
  borra_2016 tested allanite concentrate.'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
