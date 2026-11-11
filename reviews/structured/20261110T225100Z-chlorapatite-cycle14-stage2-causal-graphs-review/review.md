# Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Chlorapatite (cmmmech:chlorapatite)

- Review: 20261110T225100Z-chlorapatite-cycle14-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T22:50:00Z
- Finished UTC: 2026-11-10T22:51:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chlorapatite (cmmmech:chlorapatite) passes Cycle 14 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448: Updated data/records/chlorapatite.yaml with 'putida_chlorapatite_phosphate_scavenging_graph' (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from topolska_2014: Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel, Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556).

## Scope And Provenance

Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/chlorapatite.yaml (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448) and its canonical EDIT history sidecar (history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556)), and primary-source evidence fidelity across 'putida_chlorapatite_phosphate_scavenging_graph' (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges).

Selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:chlorapatite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3508503d6abadd52e8bdb9dacd71ebcd26731b83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chlorapatite | data/records/chlorapatite.yaml | maintained | Chlorapatite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:chlorapatite | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:chlorapatite | Checked 1563 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'putida_chlorapatite_phosphate_scavenging_graph' (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges)

graph: supported. Targets: cmmmech:chlorapatite.

Updated data/records/chlorapatite.yaml (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448) with causal_graphs ('putida_chlorapatite_phosphate_scavenging_graph' (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from topolska_2014: Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel, Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3). Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:chlorapatite.

data/records/chlorapatite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml (SHA-256 e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069: Add putida_chlorapatite_phosphate_scavenging_graph causal graph and ground putida_chlorapatite_nutrient_access to Pseudomonas putida KT2440 reference-proteome proteins (UniProtKB:Q88JJ3, UniProtKB:Q88JJ0, UniProtKB:Q88C63)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/chlorapatite.yaml; Working-tree record data/records/chlorapatite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/chlorapatite.yaml (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448) with causal_graphs ('putida_chlorapatite_phosphate_scavenging_graph' (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1007/s11356-013-1968-3; topolska_2014: Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel, Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3) | supports | Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556). Primary mechanism source (topolska_2014: Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel, Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml; Canonical EDIT history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml | supports | Canonical EDIT history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml (SHA-256 e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069): Add putida_chlorapatite_phosphate_scavenging_graph causal graph and ground putida_chlorapatite_nutrient_access to Pseudomonas putida KT2440 reference-proteome proteins (UniProtKB:Q88JJ3, UniProtKB:Q88JJ0, UniProtKB:Q88C63) |
| validation | data/records/chlorapatite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/chlorapatite.yaml and history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:chlorapatite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T225100Z-chlorapatite-cycle14-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Chlorapatite
  (cmmmech:chlorapatite)
started_at: '2026-11-10T22:50:00Z'
finished_at: '2026-11-10T22:51:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 2 curation of data/records/chlorapatite.yaml (SHA-256
    56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448) against live
    UniProtKB grounding and cited primary source (topolska_2014: Topolska, Justyna;
    Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel, Broder; Rakovan,
    John (2014; online 20 July 2013). Pb remobilization by bacterially mediated dissolution
    of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing Pseudomonas
    putida. Environmental Science and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3;
    PMC3880484. Complete 11-page retained original re-read with chlorapatite comparisons
    in Tables 1-3 and Figures 1-2 independently inspected. Same study also represented
    under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3508503d6abadd52e8bdb9dacd71ebcd26731b83
  state: working_tree
  inputs:
  - path: data/records/chlorapatite.yaml
    sha256: 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448
    role: target
  - path: history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
    sha256: e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:chlorapatite
  path: data/records/chlorapatite.yaml
  label: Chlorapatite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/chlorapatite.yaml
    (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448) and
    its canonical EDIT history sidecar (history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:Q88C63
    (Q88C63_PSEPK, Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol:
    phoB, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3
    (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate
    import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556)), and primary-source evidence fidelity
    across ''putida_chlorapatite_phosphate_scavenging_graph'' (mechanism_ref: putida_chlorapatite_nutrient_access,
    5 nodes / 4 edges).'
  selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:chlorapatite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chlorapatite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/chlorapatite.yaml
  locator: Working-tree record data/records/chlorapatite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Updated data/records/chlorapatite.yaml (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448)
    with causal_graphs (''putida_chlorapatite_phosphate_scavenging_graph'' (mechanism_ref:
    putida_chlorapatite_nutrient_access, 5 nodes / 4 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1007/s11356-013-1968-3
  locator: 'topolska_2014: Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan;
    Manecki, Maciej; Merkel, Broder; Rakovan, John (2014; online 20 July 2013). Pb
    remobilization by bacterially mediated dissolution of pyromorphite Pb5(PO4)3Cl
    in presence of phosphate-solubilizing Pseudomonas putida. Environmental Science
    and Pollution Research 21:1079-1089. DOI 10.1007/s11356-013-1968-3; PMC3880484.
    Complete 11-page retained original re-read with chlorapatite comparisons in Tables
    1-3 and Figures 1-2 independently inspected. Same study also represented under
    lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3)'
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK,
    Phosphate regulon transcriptional regulatory protein PhoB, gene_symbol: phoB,
    TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3
    (Q88JJ3_PSEPK, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate
    import ATP-binding protein PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556). Primary mechanism source (topolska_2014:
    Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel,
    Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially
    mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing
    Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089.
    DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original
    re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently
    inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3))
    parameters and source-level caveats are strictly preserved on all nodes, edges,
    and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
  locator: Canonical EDIT history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
    (SHA-256 e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069): Add
    putida_chlorapatite_phosphate_scavenging_graph causal graph and ground putida_chlorapatite_nutrient_access
    to Pseudomonas putida KT2440 reference-proteome proteins (UniProtKB:Q88JJ3, UniProtKB:Q88JJ0,
    UniProtKB:Q88C63)'
  snapshot_sha256: e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069
- evidence_id: validation
  kind: validation
  reference: data/records/chlorapatite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: data/records/chlorapatite.yaml and history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:chlorapatite
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
  - cmmmech:chlorapatite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''putida_chlorapatite_phosphate_scavenging_graph'' (mechanism_ref: putida_chlorapatite_nutrient_access,
    5 nodes / 4 edges)'
  outcome: supported
  summary: 'Updated data/records/chlorapatite.yaml (SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448)
    with causal_graphs (''putida_chlorapatite_phosphate_scavenging_graph'' (mechanism_ref:
    putida_chlorapatite_nutrient_access, 5 nodes / 4 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from topolska_2014:
    Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel,
    Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially
    mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing
    Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089.
    DOI 10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original
    re-read with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently
    inspected. Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3).
    Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate
    regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488
    Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding
    protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440,
    UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein
    PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440,
    UP000000556).'
  target_ids:
  - cmmmech:chlorapatite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/chlorapatite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/chlorapatite/2026-11-10T224938Z-marcin-ae78a3.yaml
    (SHA-256 e381dda59bd4200ea735f00868c21d5a635c546de88c6fbda71e37e18f394069: Add
    putida_chlorapatite_phosphate_scavenging_graph causal graph and ground putida_chlorapatite_nutrient_access
    to Pseudomonas putida KT2440 reference-proteome proteins (UniProtKB:Q88JJ3, UniProtKB:Q88JJ0,
    UniProtKB:Q88C63)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:chlorapatite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Chlorapatite (cmmmech:chlorapatite) passes Cycle 14 Stage 2 causal_graphs
  review (scientific_review: true) at SHA-256 56917c251b28ec29f7d49e64324fd5104bc683f550f8c7d9989bcd3e0dfe9448:
  Updated data/records/chlorapatite.yaml with ''putida_chlorapatite_phosphate_scavenging_graph''
  (mechanism_ref: putida_chlorapatite_nutrient_access, 5 nodes / 4 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from topolska_2014:
  Topolska, Justyna; Latowski, Dariusz; Kaschabek, Stefan; Manecki, Maciej; Merkel,
  Broder; Rakovan, John (2014; online 20 July 2013). Pb remobilization by bacterially
  mediated dissolution of pyromorphite Pb5(PO4)3Cl in presence of phosphate-solubilizing
  Pseudomonas putida. Environmental Science and Pollution Research 21:1079-1089. DOI
  10.1007/s11356-013-1968-3; PMC3880484. Complete 11-page retained original re-read
  with chlorapatite comparisons in Tables 1-3 and Figures 1-2 independently inspected.
  Same study also represented under lead and pyromorphite. (https://doi.org/10.1007/s11356-013-1968-3).
  Live-verified UniProtKB grounding across UniProtKB:Q88C63 (Q88C63_PSEPK, Phosphate
  regulon transcriptional regulatory protein PhoB, gene_symbol: phoB, TREMBL, NCBITaxon:160488
  Pseudomonas putida KT2440, UP000000556); UniProtKB:Q88JJ3 (Q88JJ3_PSEPK, Phosphate-binding
  protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:160488 Pseudomonas putida KT2440,
  UP000000556); UniProtKB:Q88JJ0 (PSTB1_PSEPK, Phosphate import ATP-binding protein
  PstB 1, gene_symbol: pstB1, SWISS_PROT, NCBITaxon:160488 Pseudomonas putida KT2440,
  UP000000556).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:chlorapatite.
related_reviews: []
```
