# Cycle 14 Stage 2 causal_graphs and UniProtKB grounding re-review of Pyromorphite (cmmmech:pyromorphite) after Issue #1000 alignment

- Review: 20261111T124100Z-pyromorphite-cycle14-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-11T12:40:00Z
- Finished UTC: 2026-11-11T12:41:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pyromorphite (cmmmech:pyromorphite) passes Cycle 14 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e: Updated data/records/pyromorphite.yaml with 'putida_pyromorphite_mineral_dissolution_graph' (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from topolska_2014: Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556).

## Scope And Provenance

Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/pyromorphite.yaml (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e) and its canonical EDIT history sidecar (history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556)), and primary-source evidence fidelity across 'putida_pyromorphite_mineral_dissolution_graph' (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges).

Selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:pyromorphite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 82a39149d4ef1a53b156989b8eaa220e3c809415.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pyromorphite | data/records/pyromorphite.yaml | maintained | Pyromorphite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:pyromorphite | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:pyromorphite | Checked 1573 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'putida_pyromorphite_mineral_dissolution_graph' (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges)

graph: supported. Targets: cmmmech:pyromorphite.

Updated data/records/pyromorphite.yaml (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e) with causal_graphs ('putida_pyromorphite_mineral_dissolution_graph' (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from topolska_2014: Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:pyromorphite.

data/records/pyromorphite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml (SHA-256 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4: Align putida_pyromorphite_mineral_dissolution_graph and protein_examples in pyromorphite.yaml with Topolska et al. (2014) parameters (fixes #1000)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/pyromorphite.yaml; Working-tree record data/records/pyromorphite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/pyromorphite.yaml (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e) with causal_graphs ('putida_pyromorphite_mineral_dissolution_graph' (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1007/s11356-013-1968-3; topolska_2014: Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3) | supports | Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556). Primary mechanism source (topolska_2014: Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml; Canonical EDIT history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml | supports | Canonical EDIT history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml (SHA-256 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4): Align putida_pyromorphite_mineral_dissolution_graph and protein_examples in pyromorphite.yaml with Topolska et al. (2014) parameters (fixes #1000) |
| validation | data/records/pyromorphite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/pyromorphite.yaml and history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:pyromorphite; supersedes initial review 20261110T225100Z-pyromorphite-cycle14-stage2-causal-graphs-review after Issue #1000 alignment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T124100Z-pyromorphite-cycle14-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 14 Stage 2 causal_graphs and UniProtKB grounding re-review of Pyromorphite
  (cmmmech:pyromorphite) after Issue #1000 alignment'
started_at: '2026-11-11T12:40:00Z'
finished_at: '2026-11-11T12:41:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 2 curation of data/records/pyromorphite.yaml (SHA-256
    7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e) against live
    UniProtKB grounding and cited primary source (topolska_2014: Topolska, Latowski,
    Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20, 2013). Pb remobilization
    by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of
    phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution
    Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890; PMC3880484.
    (https://doi.org/10.1007/s11356-013-1968-3)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 82a39149d4ef1a53b156989b8eaa220e3c809415
  state: working_tree
  inputs:
  - path: data/records/pyromorphite.yaml
    sha256: 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e
    role: target
  - path: history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
    sha256: 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:pyromorphite
  path: data/records/pyromorphite.yaml
  label: Pyromorphite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyromorphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/pyromorphite.yaml
    (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e) and
    its canonical EDIT history sidecar (history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:Q88C63
    (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol:
    phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3
    (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate
    import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556)), and primary-source evidence fidelity
    across ''putida_pyromorphite_mineral_dissolution_graph'' (mechanism_ref: putida_pyromorphite_remobilization,
    5 nodes / 4 edges).'
  selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:pyromorphite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pyromorphite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/pyromorphite.yaml
  locator: Working-tree record data/records/pyromorphite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-11T12:41:00Z'
  support: supports
  summary: 'Updated data/records/pyromorphite.yaml (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e)
    with causal_graphs (''putida_pyromorphite_mineral_dissolution_graph'' (mechanism_ref:
    putida_pyromorphite_remobilization, 5 nodes / 4 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1007/s11356-013-1968-3
  locator: 'topolska_2014: Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan
    (2014; online July 20, 2013). Pb remobilization by bacterially mediated dissolution
    of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas
    putida. Environmental Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3;
    PMID 23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3)'
  accessed_at: '2026-11-11T12:41:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK,
    Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB,
    TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3
    (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate
    import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556). Primary mechanism source (topolska_2014:
    Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July
    20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite
    Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental
    Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID
    23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3)) parameters
    and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
  locator: Canonical EDIT history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
  accessed_at: '2026-11-11T12:41:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
    (SHA-256 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4): Align
    putida_pyromorphite_mineral_dissolution_graph and protein_examples in pyromorphite.yaml
    with Topolska et al. (2014) parameters (fixes #1000)'
  snapshot_sha256: 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4
- evidence_id: validation
  kind: validation
  reference: data/records/pyromorphite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-11T12:41:00Z'
  support: supports
  summary: data/records/pyromorphite.yaml and history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:pyromorphite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1573 history record(s); 0 error(s).
  target_ids:
  - cmmmech:pyromorphite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''putida_pyromorphite_mineral_dissolution_graph'' (mechanism_ref: putida_pyromorphite_remobilization,
    5 nodes / 4 edges)'
  outcome: supported
  summary: 'Updated data/records/pyromorphite.yaml (SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e)
    with causal_graphs (''putida_pyromorphite_mineral_dissolution_graph'' (mechanism_ref:
    putida_pyromorphite_remobilization, 5 nodes / 4 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from topolska_2014:
    Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July
    20, 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite
    Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental
    Science and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID
    23872890; PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified
    UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional
    regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas
    putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding
    protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440,
    UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein
    PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440,
    UP000000556).'
  target_ids:
  - cmmmech:pyromorphite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/pyromorphite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/pyromorphite/2026-11-11T124010Z-marcin-466de8.yaml
    (SHA-256 88ef2d54daf4985a7aa187bf096f65bd01faf8aabc5d8b836e5654b01b6d29d4: Align
    putida_pyromorphite_mineral_dissolution_graph and protein_examples in pyromorphite.yaml
    with Topolska et al. (2014) parameters (fixes #1000)) and passing all LinkML and
    history validation gates.'
  target_ids:
  - cmmmech:pyromorphite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Pyromorphite (cmmmech:pyromorphite) passes Cycle 14 Stage 2 causal_graphs
  review (scientific_review: true) at SHA-256 7cfd2481402d057ccb64a88238a5874c0b35902796e590431a8876cab1025a0e:
  Updated data/records/pyromorphite.yaml with ''putida_pyromorphite_mineral_dissolution_graph''
  (mechanism_ref: putida_pyromorphite_remobilization, 5 nodes / 4 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from topolska_2014:
  Topolska, Latowski, Kaschabek, Manecki, Merkel and Rakovan (2014; online July 20,
  2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl
  in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science
  and Pollution Research 21, 1079-1089. DOI 10.1007/s11356-013-1968-3; PMID 23872890;
  PMC3880484. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified UniProtKB
  grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional
  regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas
  putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein
  PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556);
  UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol:
  pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:pyromorphite; supersedes
  initial review 20261110T225100Z-pyromorphite-cycle14-stage2-causal-graphs-review
  after Issue #1000 alignment.'
related_reviews: []
```
