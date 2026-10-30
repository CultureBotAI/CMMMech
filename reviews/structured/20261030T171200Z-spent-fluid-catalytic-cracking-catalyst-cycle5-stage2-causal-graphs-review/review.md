# Cycle 5 Stage 2 causal-graph review of Spent fluid catalytic cracking catalyst (cmmmech:spent-fluid-catalytic-cracking-catalyst)

- Review: 20261030T171200Z-spent-fluid-catalytic-cracking-catalyst-cycle5-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T17:10:00Z
- Finished UTC: 2026-10-30T17:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Spent fluid catalytic cracking catalyst (cmmmech:spent-fluid-catalytic-cracking-catalyst) passes Cycle 5 Stage 2 causal-graph review (scientific_review: true) at SHA-256 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0: Synchronized causal_graphs[0] (gluconobacter_fcc_catalyst_bioleaching_graph) in data/records/spent-fluid-catalytic-cracking-catalyst.yaml with mechanisms[0]: replaced 'leached La and Ce' with 'leached ~49% of total digestible REEs', replaced generic organic-acid prose on the substrate/product edges with the exact Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce recovery), refined the substrate edge predicate from acts_on to solubilizes, and aligned supports: partial on gluconic_acid_biolixiviant -&gt; spent_fcc_catalyst_feed.

## Scope And Provenance

Cycle 5 Stage 2 causal-graph review of data/records/spent-fluid-catalytic-cracking-catalyst.yaml (SHA-256 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0) and its canonical EDIT history sidecar (history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml) verifying full synchronization between causal_graphs[0] and mechanisms[0].

Selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:spent-fluid-catalytic-cracking-catalyst
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9e3221733b5efe6fb1be27fcc03692abc3a0de44.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-fluid-catalytic-cracking-catalyst | data/records/spent-fluid-catalytic-cracking-catalyst.yaml | maintained | Spent fluid catalytic cracking catalyst |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:spent-fluid-catalytic-cracking-catalyst | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:spent-fluid-catalytic-cracking-catalyst | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Synchronization of causal_graphs[0] with mechanisms[0] and primary source (DOI:10.1016/j.hydromet.2016.01.031)

graph: supported. Targets: cmmmech:spent-fluid-catalytic-cracking-catalyst.

Synchronized causal_graphs[0] (gluconobacter_fcc_catalyst_bioleaching_graph) in data/records/spent-fluid-catalytic-cracking-catalyst.yaml with mechanisms[0]: replaced 'leached La and Ce' with 'leached ~49% of total digestible REEs', replaced generic organic-acid prose on the substrate/product edges with the exact Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce recovery), refined the substrate edge predicate from acts_on to solubilizes, and aligned supports: partial on gluconic_acid_biolixiviant -&gt; spent_fcc_catalyst_feed.

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:spent-fluid-catalytic-cracking-catalyst.

data/records/spent-fluid-catalytic-cracking-catalyst.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/spent-fluid-catalytic-cracking-catalyst.yaml; Working-tree record data/records/spent-fluid-catalytic-cracking-catalyst.yaml | supports | Synchronized causal_graphs[0] (gluconobacter_fcc_catalyst_bioleaching_graph) in data/records/spent-fluid-catalytic-cracking-catalyst.yaml with mechanisms[0]: replaced 'leached La and Ce' with 'leached ~49% of total digestible REEs', replaced generic organic-acid prose on the substrate/product edges with the exact Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce recovery), refined the substrate edge predicate from acts_on to solubilizes, and aligned supports: partial on gluconic_acid_biolixiviant -&gt; spent_fcc_catalyst_feed. |
| primary_source | DOI:10.1016/j.hydromet.2016.01.031; Reed DW et al. (2016) Hydrometallurgy 166:34-40, Sections 2-3, Figures 1-5, Tables 1-2 | supports | Reed et al. (2016) demonstrated that cell-free supernatant of Gluconobacter oxydans strain B58 grown on glucose produces organic acids (predominantly gluconic acid) that leach ~49% of total digestible REEs (La and Ce) from spent fluid catalytic cracking (FCC) catalyst (~1.5% rare earth oxide, &gt;99% La and Ce withLa:Ce ~44:1) at 1.5% (w/v) pulp density over 24 h at 30 degrees C, with La preferentially leached over Ce (~51% vs ~35%) and 12.5 mM abiotic gluconic acid at pH 2.3 tested only against higher-pH controls (pH 3.2, 2.9, and 2.5). |
| edit_history | history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml; Canonical EDIT history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml | supports | Canonical EDIT history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml (SHA-256 a989008200a1412bf7960dd6fb847f75595dd5ec85f319f9aafc952dd658bfe6) records the Cycle 5 Stage 2 causal_graphs[0] update via scripts/curate_causal_graphs.py. |
| validation | data/records/spent-fluid-catalytic-cracking-catalyst.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/spent-fluid-catalytic-cracking-catalyst.yaml and history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml pass strict LinkML schema and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T171200Z-spent-fluid-catalytic-cracking-catalyst-cycle5-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 2 causal-graph review of Spent fluid catalytic cracking catalyst
  (cmmmech:spent-fluid-catalytic-cracking-catalyst)
started_at: '2026-10-30T17:10:00Z'
finished_at: '2026-10-30T17:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 2 causal_graphs[0] update in data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    (SHA-256 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0) against
    mechanisms[0] and its cited primary source (DOI:10.1016/j.hydromet.2016.01.031).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 9e3221733b5efe6fb1be27fcc03692abc3a0de44
  state: working_tree
  inputs:
  - path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    sha256: 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0
    role: target
  - path: history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
    sha256: a989008200a1412bf7960dd6fb847f75595dd5ec85f319f9aafc952dd658bfe6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:spent-fluid-catalytic-cracking-catalyst
  path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  label: Spent fluid catalytic cracking catalyst
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
    role: canonical_history
scope:
  description: Cycle 5 Stage 2 causal-graph review of data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    (SHA-256 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0) and
    its canonical EDIT history sidecar (history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml)
    verifying full synchronization between causal_graphs[0] and mechanisms[0].
  selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:spent-fluid-catalytic-cracking-catalyst
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  locator: Working-tree record data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Synchronized causal_graphs[0] (gluconobacter_fcc_catalyst_bioleaching_graph)
    in data/records/spent-fluid-catalytic-cracking-catalyst.yaml with mechanisms[0]:
    replaced ''leached La and Ce'' with ''leached ~49% of total digestible REEs'',
    replaced generic organic-acid prose on the substrate/product edges with the exact
    Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce recovery), refined
    the substrate edge predicate from acts_on to solubilizes, and aligned supports:
    partial on gluconic_acid_biolixiviant -> spent_fcc_catalyst_feed.'
  snapshot_sha256: 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1016/j.hydromet.2016.01.031
  locator: Reed DW et al. (2016) Hydrometallurgy 166:34-40, Sections 2-3, Figures
    1-5, Tables 1-2
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: Reed et al. (2016) demonstrated that cell-free supernatant of Gluconobacter
    oxydans strain B58 grown on glucose produces organic acids (predominantly gluconic
    acid) that leach ~49% of total digestible REEs (La and Ce) from spent fluid catalytic
    cracking (FCC) catalyst (~1.5% rare earth oxide, >99% La and Ce withLa:Ce ~44:1)
    at 1.5% (w/v) pulp density over 24 h at 30 degrees C, with La preferentially leached
    over Ce (~51% vs ~35%) and 12.5 mM abiotic gluconic acid at pH 2.3 tested only
    against higher-pH controls (pH 3.2, 2.9, and 2.5).
- evidence_id: edit_history
  kind: record_content
  reference: history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
  locator: Canonical EDIT history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: Canonical EDIT history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
    (SHA-256 a989008200a1412bf7960dd6fb847f75595dd5ec85f319f9aafc952dd658bfe6) records
    the Cycle 5 Stage 2 causal_graphs[0] update via scripts/curate_causal_graphs.py.
  snapshot_sha256: a989008200a1412bf7960dd6fb847f75595dd5ec85f319f9aafc952dd658bfe6
- evidence_id: validation
  kind: validation
  reference: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: data/records/spent-fluid-catalytic-cracking-catalyst.yaml and history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
    pass strict LinkML schema and history validation with 0 errors.
  snapshot_sha256: 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
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
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
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
  summary: 'Synchronized causal_graphs[0] (gluconobacter_fcc_catalyst_bioleaching_graph)
    in data/records/spent-fluid-catalytic-cracking-catalyst.yaml with mechanisms[0]:
    replaced ''leached La and Ce'' with ''leached ~49% of total digestible REEs'',
    replaced generic organic-acid prose on the substrate/product edges with the exact
    Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce recovery), refined
    the substrate edge predicate from acts_on to solubilizes, and aligned supports:
    partial on gluconic_acid_biolixiviant -> spent_fcc_catalyst_feed.'
  target_ids:
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: data/records/spent-fluid-catalytic-cracking-catalyst.yaml was updated exclusively
    through scripts/curate_causal_graphs.py (curate_record_file), producing append-only
    history sidecar history/records/spent-fluid-catalytic-cracking-catalyst/2026-10-30T171004Z-marcin-fa7380.yaml
    and passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Spent fluid catalytic cracking catalyst (cmmmech:spent-fluid-catalytic-cracking-catalyst)
  passes Cycle 5 Stage 2 causal-graph review (scientific_review: true) at SHA-256
  9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0: Synchronized causal_graphs[0]
  (gluconobacter_fcc_catalyst_bioleaching_graph) in data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  with mechanisms[0]: replaced ''leached La and Ce'' with ''leached ~49% of total
  digestible REEs'', replaced generic organic-acid prose on the substrate/product
  edges with the exact Reed et al. (2016) FCC catalyst findings (~51% La vs ~35% Ce
  recovery), refined the substrate edge predicate from acts_on to solubilizes, and
  aligned supports: partial on gluconic_acid_biolixiviant -> spent_fcc_catalyst_feed.'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
