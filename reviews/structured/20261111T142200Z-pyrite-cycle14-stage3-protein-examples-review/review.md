# Cycle 14 Stage 3 protein_examples and causal_graphs review of Pyrite (cmmmech:pyrite)

- Review: 20261111T142200Z-pyrite-cycle14-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-11T14:21:00Z
- Finished UTC: 2026-11-11T14:22:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pyrite (cmmmech:pyrite) passes Cycle 14 Stage 3 protein_examples review (scientific_review: true) at SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb: Updated data/records/pyrite.yaml with UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722) and 'voltae_a3_pyrite_reductive_dissolution_graph' (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from payne2021: Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods, Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3).

## Scope And Provenance

Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb) and its canonical EDIT history sidecar (history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml) verifying live UniProtKB grounding (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722)), causal-graph node/edge parity across 'voltae_a3_pyrite_reductive_dissolution_graph' (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges), and primary-source evidence fidelity.

Selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:pyrite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 000fd9c1bad8e0de32a55b4bc1554d4a86696dae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pyrite | data/records/pyrite.yaml | maintained | Pyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:pyrite | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:pyrite | Checked 1583 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of UniProtKB protein_examples grounding, causal_graphs structure, and parity across 'voltae_a3_pyrite_reductive_dissolution_graph' (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:pyrite.

Updated data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb) with live-verified protein_examples (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722)) and causal_graphs ('voltae_a3_pyrite_reductive_dissolution_graph' (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from payne2021: Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods, Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:pyrite.

data/records/pyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml (SHA-256 b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423: Added strain-exact Methanococcus voltae A3 reference-proteome protein examples (Mvol_0819 UniProtKB:D7DTL8, Mvol_1128 UniProtKB:D7DUH5) and representative causal graph for pyrite-associated growth and synthesized-FeS2 reduction.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/pyrite.yaml; Working-tree record data/records/pyrite.yaml (mechanisms[].protein_examples and causal_graphs) | supports | Updated data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb) with live-verified protein_examples (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722)) and causal_graphs ('voltae_a3_pyrite_reductive_dissolution_graph' (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels. |
| primary_source | https://doi.org/10.1038/s41396-021-01028-3; payne2021: Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods, Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3) | supports | Live-verified UniProtKB grounding across UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae A3, UP000007722). Primary mechanism source (payne2021: Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods, Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml; Canonical EDIT history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml | supports | Canonical EDIT history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml (SHA-256 b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423): Added strain-exact Methanococcus voltae A3 reference-proteome protein examples (Mvol_0819 UniProtKB:D7DTL8, Mvol_1128 UniProtKB:D7DUH5) and representative causal graph for pyrite-associated growth and synthesized-FeS2 reduction. |
| validation | data/records/pyrite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/pyrite.yaml and history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:pyrite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T142200Z-pyrite-cycle14-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 3 protein_examples and causal_graphs review of Pyrite (cmmmech:pyrite)
started_at: '2026-11-11T14:21:00Z'
finished_at: '2026-11-11T14:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 3 curation of data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb)
    against live UniProtKB grounding and cited primary source (payne2021: Payne, Spietz
    and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The
    ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods,
    Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables
    S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 000fd9c1bad8e0de32a55b4bc1554d4a86696dae
  state: working_tree
  inputs:
  - path: data/records/pyrite.yaml
    sha256: 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb
    role: target
  - path: history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
    sha256: b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:pyrite
  path: data/records/pyrite.yaml
  label: Pyrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/pyrite.yaml
    (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb) and
    its canonical EDIT history sidecar (history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml)
    verifying live UniProtKB grounding (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase
    (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase
    subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722)), causal-graph node/edge parity across ''voltae_a3_pyrite_reductive_dissolution_graph''
    (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges),
    and primary-source evidence fidelity.'
  selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:pyrite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pyrite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/pyrite.yaml
  locator: Working-tree record data/records/pyrite.yaml (mechanisms[].protein_examples
    and causal_graphs)
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Updated data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb)
    with live-verified protein_examples (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase
    (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase
    subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722)) and causal_graphs (''voltae_a3_pyrite_reductive_dissolution_graph''
    (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels.'
  snapshot_sha256: 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1038/s41396-021-01028-3
  locator: 'payne2021: Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite
    by methanogenic archaea. The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3.
    Materials and methods, Results and discussion, Figures 1-4; original supplementary
    Figures S1-S8, Tables S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3)'
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:D7DTL8 (D7DTL8_METV3,
    formate dehydrogenase (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320
    Methanococcus voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme
    M reductase subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722). Primary mechanism source (payne2021: Payne, Spietz and
    Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea. The ISME
    Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods, Results
    and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables S1-S3
    and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3)) parameters and source-level
    caveats are strictly preserved on all nodes, edges, and ProteinExample evidence
    items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
  locator: Canonical EDIT history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
    (SHA-256 b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423): Added
    strain-exact Methanococcus voltae A3 reference-proteome protein examples (Mvol_0819
    UniProtKB:D7DTL8, Mvol_1128 UniProtKB:D7DUH5) and representative causal graph
    for pyrite-associated growth and synthesized-FeS2 reduction.'
  snapshot_sha256: b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423
- evidence_id: validation
  kind: validation
  reference: data/records/pyrite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: data/records/pyrite.yaml and history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:pyrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1583 history record(s); 0 error(s).
  target_ids:
  - cmmmech:pyrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_causal_graph
  area: graph
  topic: 'Verification of UniProtKB protein_examples grounding, causal_graphs structure,
    and parity across ''voltae_a3_pyrite_reductive_dissolution_graph'' (mechanism_ref:
    voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/pyrite.yaml (SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb)
    with live-verified protein_examples (UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase
    (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase
    subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus
    voltae A3, UP000007722)) and causal_graphs (''voltae_a3_pyrite_reductive_dissolution_graph''
    (mechanism_ref: voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges)),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from payne2021: Payne,
    Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea.
    The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods,
    Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables
    S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3).'
  target_ids:
  - cmmmech:pyrite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/pyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/pyrite/2026-11-11T142116Z-marcin-aeee3a.yaml
    (SHA-256 b345bb280311ef87971b966192ae3327645e16736667a8c1705a5b26b1b28423: Added
    strain-exact Methanococcus voltae A3 reference-proteome protein examples (Mvol_0819
    UniProtKB:D7DTL8, Mvol_1128 UniProtKB:D7DUH5) and representative causal graph
    for pyrite-associated growth and synthesized-FeS2 reduction.) and passing all
    LinkML and history validation gates.'
  target_ids:
  - cmmmech:pyrite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Pyrite (cmmmech:pyrite) passes Cycle 14 Stage 3 protein_examples review
  (scientific_review: true) at SHA-256 73448dfad233c1f97f43a70a7978358a894bf3020e2f0c9e8f903c64bceef7bb:
  Updated data/records/pyrite.yaml with UniProtKB:D7DTL8 (D7DTL8_METV3, formate dehydrogenase
  (coenzyme F420), gene_symbol: Mvol_0819, TREMBL, NCBITaxon:456320 Methanococcus
  voltae A3, UP000007722); UniProtKB:D7DUH5 (D7DUH5_METV3, Methyl-coenzyme M reductase
  subunit alpha, gene_symbol: Mvol_1128, TREMBL, NCBITaxon:456320 Methanococcus voltae
  A3, UP000007722) and ''voltae_a3_pyrite_reductive_dissolution_graph'' (mechanism_ref:
  voltae-pyrite-associated-growth-and-reduction, 4 nodes / 3 edges), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from payne2021:
  Payne, Spietz and Boyd (2021). Reductive dissolution of pyrite by methanogenic archaea.
  The ISME Journal 15:3498-3507. DOI 10.1038/s41396-021-01028-3. Materials and methods,
  Results and discussion, Figures 1-4; original supplementary Figures S1-S8, Tables
  S1-S3 and Data Set 1. (https://doi.org/10.1038/s41396-021-01028-3).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:pyrite.
related_reviews: []
```
