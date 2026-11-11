# Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Scheelite (cmmmech:scheelite)

- Review: 20261110T225100Z-scheelite-cycle14-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T22:50:00Z
- Finished UTC: 2026-11-10T22:51:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Scheelite (cmmmech:scheelite) passes Cycle 14 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177: Updated data/records/scheelite.yaml with 'metallosphaera_scheelite_concentrate_bioleaching_graph' (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492). Live-verified UniProtKB grounding across UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242).

## Scope And Provenance

Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/scheelite.yaml (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177) and its canonical EDIT history sidecar (history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242)), and primary-source evidence fidelity across 'metallosphaera_scheelite_concentrate_bioleaching_graph' (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges).

Selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:scheelite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3508503d6abadd52e8bdb9dacd71ebcd26731b83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:scheelite | data/records/scheelite.yaml | maintained | Scheelite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:scheelite | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:scheelite | Checked 1563 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'metallosphaera_scheelite_concentrate_bioleaching_graph' (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)

graph: supported. Targets: cmmmech:scheelite.

Updated data/records/scheelite.yaml (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177) with causal_graphs ('metallosphaera_scheelite_concentrate_bioleaching_graph' (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492). Live-verified UniProtKB grounding across UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:scheelite.

data/records/scheelite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml (SHA-256 d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9: Add metallosphaera_scheelite_concentrate_bioleaching_graph causal graph and ground metallosphaera_scheelite_tungsten_release in scheelite.yaml to Metallosphaera sedula DSM 5348 proteins (UniProtKB:A4YE09, UniProtKB:A4YDJ8, UniProtKB:A4YHQ8)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/scheelite.yaml; Working-tree record data/records/scheelite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/scheelite.yaml (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177) with causal_graphs ('metallosphaera_scheelite_concentrate_bioleaching_graph' (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2019.01492; blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492) | supports | Live-verified UniProtKB grounding across UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242). Primary mechanism source (blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml; Canonical EDIT history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml | supports | Canonical EDIT history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml (SHA-256 d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9): Add metallosphaera_scheelite_concentrate_bioleaching_graph causal graph and ground metallosphaera_scheelite_tungsten_release in scheelite.yaml to Metallosphaera sedula DSM 5348 proteins (UniProtKB:A4YE09, UniProtKB:A4YDJ8, UniProtKB:A4YHQ8) |
| validation | data/records/scheelite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/scheelite.yaml and history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:scheelite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T225100Z-scheelite-cycle14-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Scheelite
  (cmmmech:scheelite)
started_at: '2026-11-10T22:50:00Z'
finished_at: '2026-11-10T22:51:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 2 curation of data/records/scheelite.yaml (SHA-256
    8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177) against live
    UniProtKB grounding and cited primary source (blazevic2019: Blazevic et al. (2019).
    Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile Metallosphaera
    sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492; Materials
    and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3508503d6abadd52e8bdb9dacd71ebcd26731b83
  state: working_tree
  inputs:
  - path: data/records/scheelite.yaml
    sha256: 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177
    role: target
  - path: history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
    sha256: d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:scheelite
  path: data/records/scheelite.yaml
  label: Scheelite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scheelite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/scheelite.yaml
    (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177) and
    its canonical EDIT history sidecar (history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A4YE09
    (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549
    Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5,
    Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula
    DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol:
    slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242)),
    and primary-source evidence fidelity across ''metallosphaera_scheelite_concentrate_bioleaching_graph''
    (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges).'
  selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:scheelite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:scheelite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/scheelite.yaml
  locator: Working-tree record data/records/scheelite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Updated data/records/scheelite.yaml (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177)
    with causal_graphs (''metallosphaera_scheelite_concentrate_bioleaching_graph''
    (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2019.01492
  locator: 'blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4
    by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface.
    Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion,
    Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492)'
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A4YE09 (A4YE09_METS5,
    Cytochrome c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera
    sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol:
    Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242);
    UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT,
    NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242). Primary mechanism
    source (blazevic2019: Blazevic et al. (2019). Biotransformation of Scheelite CaWO4
    by the Extreme Thermoacidophile Metallosphaera sedula: Tungsten-Microbial Interface.
    Frontiers in Microbiology 10:1492; Materials and Methods, Results and Discussion,
    Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492)) parameters
    and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
  locator: Canonical EDIT history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
    (SHA-256 d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9): Add
    metallosphaera_scheelite_concentrate_bioleaching_graph causal graph and ground
    metallosphaera_scheelite_tungsten_release in scheelite.yaml to Metallosphaera
    sedula DSM 5348 proteins (UniProtKB:A4YE09, UniProtKB:A4YDJ8, UniProtKB:A4YHQ8)'
  snapshot_sha256: d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9
- evidence_id: validation
  kind: validation
  reference: data/records/scheelite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: data/records/scheelite.yaml and history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:scheelite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1563 history record(s); 0 error(s).
  target_ids:
  - cmmmech:scheelite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''metallosphaera_scheelite_concentrate_bioleaching_graph'' (mechanism_ref:
    metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)'
  outcome: supported
  summary: 'Updated data/records/scheelite.yaml (SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177)
    with causal_graphs (''metallosphaera_scheelite_concentrate_bioleaching_graph''
    (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges)),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from blazevic2019: Blazevic
    et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile
    Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology
    10:1492; Materials and Methods, Results and Discussion, Figures 1-7 and Table
    1. (https://doi.org/10.3389/fmicb.2019.01492). Live-verified UniProtKB grounding
    across UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome c oxidase, subunit I, gene_symbol:
    foxA, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8
    (A4YDJ8_METS5, Sulfocyanin, gene_symbol: Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera
    sedula DSM 5348, UP000000242); UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A,
    gene_symbol: slaA, SWISS_PROT, NCBITaxon:399549 Metallosphaera sedula DSM 5348,
    UP000000242).'
  target_ids:
  - cmmmech:scheelite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/scheelite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/scheelite/2026-11-10T225033Z-marcin-7237d0.yaml
    (SHA-256 d4cbf16529311c7252651b57cc8f426f5258c41dc1263eee329bfb537b0739d9: Add
    metallosphaera_scheelite_concentrate_bioleaching_graph causal graph and ground
    metallosphaera_scheelite_tungsten_release in scheelite.yaml to Metallosphaera
    sedula DSM 5348 proteins (UniProtKB:A4YE09, UniProtKB:A4YDJ8, UniProtKB:A4YHQ8))
    and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:scheelite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Scheelite (cmmmech:scheelite) passes Cycle 14 Stage 2 causal_graphs review
  (scientific_review: true) at SHA-256 8d9dcaf2c3d8890851129c31ad74677991b28d280dfd07954739535d33e77177:
  Updated data/records/scheelite.yaml with ''metallosphaera_scheelite_concentrate_bioleaching_graph''
  (mechanism_ref: metallosphaera_scheelite_tungsten_release, 5 nodes / 4 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from blazevic2019:
  Blazevic et al. (2019). Biotransformation of Scheelite CaWO4 by the Extreme Thermoacidophile
  Metallosphaera sedula: Tungsten-Microbial Interface. Frontiers in Microbiology 10:1492;
  Materials and Methods, Results and Discussion, Figures 1-7 and Table 1. (https://doi.org/10.3389/fmicb.2019.01492).
  Live-verified UniProtKB grounding across UniProtKB:A4YE09 (A4YE09_METS5, Cytochrome
  c oxidase, subunit I, gene_symbol: foxA, TREMBL, NCBITaxon:399549 Metallosphaera
  sedula DSM 5348, UP000000242); UniProtKB:A4YDJ8 (A4YDJ8_METS5, Sulfocyanin, gene_symbol:
  Msed_0323, TREMBL, NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242);
  UniProtKB:A4YHQ8 (SLAA_METS5, S-layer protein A, gene_symbol: slaA, SWISS_PROT,
  NCBITaxon:399549 Metallosphaera sedula DSM 5348, UP000000242).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:scheelite.
related_reviews: []
```
