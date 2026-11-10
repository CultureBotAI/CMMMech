# Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Kaolin mine waste (cmmmech:kaolin-mine-waste)

- Review: 20261110T225100Z-kaolin-mine-waste-cycle14-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T22:50:00Z
- Finished UTC: 2026-11-10T22:51:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kaolin mine waste (cmmmech:kaolin-mine-waste) passes Cycle 14 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49: Updated data/records/kaolin-mine-waste.yaml with 'bacillus_kaolin_waste_iron_impurity_leaching_graph' (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from sanchez_palencia_2022: Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7). Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).

## Scope And Provenance

Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/kaolin-mine-waste.yaml (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49) and its canonical EDIT history sidecar (history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143)), and primary-source evidence fidelity across 'bacillus_kaolin_waste_iron_impurity_leaching_graph' (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges).

Selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:kaolin-mine-waste
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3508503d6abadd52e8bdb9dacd71ebcd26731b83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:kaolin-mine-waste | data/records/kaolin-mine-waste.yaml | maintained | Kaolin mine waste |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:kaolin-mine-waste | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:kaolin-mine-waste | Checked 1563 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'bacillus_kaolin_waste_iron_impurity_leaching_graph' (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges)

graph: supported. Targets: cmmmech:kaolin-mine-waste.

Updated data/records/kaolin-mine-waste.yaml (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49) with causal_graphs ('bacillus_kaolin_waste_iron_impurity_leaching_graph' (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from sanchez_palencia_2022: Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7). Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:kaolin-mine-waste.

data/records/kaolin-mine-waste.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml (SHA-256 cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241: Add bacillus_kaolin_waste_iron_impurity_leaching_graph causal graph and ground bacillus_iron_impurity_leaching to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0K0QJ28, UniProtKB:A0A0G3E229)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/kaolin-mine-waste.yaml; Working-tree record data/records/kaolin-mine-waste.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/kaolin-mine-waste.yaml (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49) with causal_graphs ('bacillus_kaolin_waste_iron_impurity_leaching_graph' (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1007/s42860-022-00192-7; sanchez_palencia_2022: Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7) | supports | Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143). Primary mechanism source (sanchez_palencia_2022: Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml; Canonical EDIT history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml | supports | Canonical EDIT history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml (SHA-256 cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241): Add bacillus_kaolin_waste_iron_impurity_leaching_graph causal graph and ground bacillus_iron_impurity_leaching to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0K0QJ28, UniProtKB:A0A0G3E229) |
| validation | data/records/kaolin-mine-waste.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/kaolin-mine-waste.yaml and history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:kaolin-mine-waste.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T225100Z-kaolin-mine-waste-cycle14-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Kaolin mine
  waste (cmmmech:kaolin-mine-waste)
started_at: '2026-11-10T22:50:00Z'
finished_at: '2026-11-10T22:51:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 2 curation of data/records/kaolin-mine-waste.yaml
    (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49) against
    live UniProtKB grounding and cited primary source (sanchez_palencia_2022: Sanchez-Palencia
    et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric
    Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404.
    DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022;
    complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref
    online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3508503d6abadd52e8bdb9dacd71ebcd26731b83
  state: working_tree
  inputs:
  - path: data/records/kaolin-mine-waste.yaml
    sha256: b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49
    role: target
  - path: history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
    sha256: cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:kaolin-mine-waste
  path: data/records/kaolin-mine-waste.yaml
  label: Kaolin mine waste
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin-mine-waste.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/kaolin-mine-waste.yaml
    (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49) and
    its canonical EDIT history sidecar (history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A0A0K0QI82
    (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428
    Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU,
    L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
    UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein]
    synthase III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
    UP000194143)), and primary-source evidence fidelity across ''bacillus_kaolin_waste_iron_impurity_leaching_graph''
    (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges).'
  selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:kaolin-mine-waste
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:kaolin-mine-waste
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/kaolin-mine-waste.yaml
  locator: Working-tree record data/records/kaolin-mine-waste.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Updated data/records/kaolin-mine-waste.yaml (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49)
    with causal_graphs (''bacillus_kaolin_waste_iron_impurity_leaching_graph'' (mechanism_ref:
    bacillus_iron_impurity_leaching, 6 nodes / 6 edges)), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1007/s42860-022-00192-7
  locator: 'sanchez_palencia_2022: Sanchez-Palencia et al. (2022). Iron Removal from
    Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and Biological (Bacillus
    Strain) Leaching. Clays and Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7.
    Original Springer version published 7 July 2022; complete 19-page PDF, Tables
    1-4 and Figures 1-12 inspected. The later Cambridge/Crossref online date is not
    a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7)'
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU,
    Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
    UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase,
    gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143);
    UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase
    III, gene_symbol: fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).
    Primary mechanism source (sanchez_palencia_2022: Sanchez-Palencia et al. (2022).
    Iron Removal from Kaolin Waste Dumps by Chemical (Oxalic and Citric Acids) and
    Biological (Bacillus Strain) Leaching. Clays and Clay Minerals 70(3):386-404.
    DOI 10.1007/s42860-022-00192-7. Original Springer version published 7 July 2022;
    complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected. The later Cambridge/Crossref
    online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7))
    parameters and source-level caveats are strictly preserved on all nodes, edges,
    and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
  locator: Canonical EDIT history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
    (SHA-256 cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241): Add
    bacillus_kaolin_waste_iron_impurity_leaching_graph causal graph and ground bacillus_iron_impurity_leaching
    to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0K0QJ28,
    UniProtKB:A0A0G3E229)'
  snapshot_sha256: cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241
- evidence_id: validation
  kind: validation
  reference: data/records/kaolin-mine-waste.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: data/records/kaolin-mine-waste.yaml and history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:kaolin-mine-waste
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
  - cmmmech:kaolin-mine-waste
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''bacillus_kaolin_waste_iron_impurity_leaching_graph'' (mechanism_ref:
    bacillus_iron_impurity_leaching, 6 nodes / 6 edges)'
  outcome: supported
  summary: 'Updated data/records/kaolin-mine-waste.yaml (SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49)
    with causal_graphs (''bacillus_kaolin_waste_iron_impurity_leaching_graph'' (mechanism_ref:
    bacillus_iron_impurity_leaching, 6 nodes / 6 edges)), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    preserving source-faithful support levels and caveats from sanchez_palencia_2022:
    Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical
    (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and
    Clay Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer
    version published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12
    inspected. The later Cambridge/Crossref online date is not a separate experiment.
    (https://doi.org/10.1007/s42860-022-00192-7). Live-verified UniProtKB grounding
    across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol:
    CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28
    (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428
    Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229 (A0A0G3E229_BACTU,
    Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol: fabH, TREMBL,
    NCBITaxon:1428 Bacillus thuringiensis, UP000194143).'
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/kaolin-mine-waste.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/kaolin-mine-waste/2026-11-10T224938Z-marcin-515733.yaml
    (SHA-256 cec5fc8aa99674122014a5b459deacfd61edd26c76262ac810aece922b771241: Add
    bacillus_kaolin_waste_iron_impurity_leaching_graph causal graph and ground bacillus_iron_impurity_leaching
    to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0K0QJ28,
    UniProtKB:A0A0G3E229)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Kaolin mine waste (cmmmech:kaolin-mine-waste) passes Cycle 14 Stage 2 causal_graphs
  review (scientific_review: true) at SHA-256 b6ac21e2dce87947a8b79f05ceb0ba917ee6cf23dc5dca5c6381a03285b74c49:
  Updated data/records/kaolin-mine-waste.yaml with ''bacillus_kaolin_waste_iron_impurity_leaching_graph''
  (mechanism_ref: bacillus_iron_impurity_leaching, 6 nodes / 6 edges), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from sanchez_palencia_2022:
  Sanchez-Palencia et al. (2022). Iron Removal from Kaolin Waste Dumps by Chemical
  (Oxalic and Citric Acids) and Biological (Bacillus Strain) Leaching. Clays and Clay
  Minerals 70(3):386-404. DOI 10.1007/s42860-022-00192-7. Original Springer version
  published 7 July 2022; complete 19-page PDF, Tables 1-4 and Figures 1-12 inspected.
  The later Cambridge/Crossref online date is not a separate experiment. (https://doi.org/10.1007/s42860-022-00192-7).
  Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU,
  Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
  UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol:
  ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0G3E229
  (A0A0G3E229_BACTU, Beta-ketoacyl-[acyl-carrier-protein] synthase III, gene_symbol:
  fabH, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:kaolin-mine-waste.
related_reviews: []
```
