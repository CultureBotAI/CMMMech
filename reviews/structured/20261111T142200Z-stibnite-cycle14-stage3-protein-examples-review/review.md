# Cycle 14 Stage 3 protein_examples and causal_graphs review of Stibnite (cmmmech:stibnite)

- Review: 20261111T142200Z-stibnite-cycle14-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-11T14:21:00Z
- Finished UTC: 2026-11-11T14:22:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Stibnite (cmmmech:stibnite) passes Cycle 14 Stage 3 protein_examples review (scientific_review: true) at SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a: Updated data/records/stibnite.yaml with UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794) and 'xt06_aerobic_stibnite_transformation_graph' (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from loni2020: Loni et al. (2020). Mechanism of microbial dissolution and oxidation of antimony in stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561. Complete university-hosted article-in-press version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561).

## Scope And Provenance

Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/stibnite.yaml (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a) and its canonical EDIT history sidecar (history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml) verifying live UniProtKB grounding (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794)), causal-graph node/edge parity across 'xt06_aerobic_stibnite_transformation_graph' (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges), and primary-source evidence fidelity.

Selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:stibnite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 000fd9c1bad8e0de32a55b4bc1554d4a86696dae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:stibnite | data/records/stibnite.yaml | maintained | Stibnite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:stibnite | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:stibnite | Checked 1583 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of UniProtKB protein_examples grounding, causal_graphs structure, and parity across 'xt06_aerobic_stibnite_transformation_graph' (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:stibnite.

Updated data/records/stibnite.yaml (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a) with live-verified protein_examples (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794)) and causal_graphs ('xt06_aerobic_stibnite_transformation_graph' (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from loni2020: Loni et al. (2020). Mechanism of microbial dissolution and oxidation of antimony in stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561. Complete university-hosted article-in-press version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:stibnite.

data/records/stibnite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml (SHA-256 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5: Added Paracoccus versutus reference-proteome protein examples (SoxAX subunit A UniProtKB:A0AAQ0HFG7, sulfurtransferase UniProtKB:A0AAQ0HHU8) and representative causal graph for aerobic stibnite transformation.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/stibnite.yaml; Working-tree record data/records/stibnite.yaml (mechanisms[].protein_examples and causal_graphs) | supports | Updated data/records/stibnite.yaml (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a) with live-verified protein_examples (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794)) and causal_graphs ('xt06_aerobic_stibnite_transformation_graph' (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels. |
| primary_source | https://doi.org/10.1016/j.jhazmat.2019.121561; loni2020: Loni et al. (2020). Mechanism of microbial dissolution and oxidation of antimony in stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561. Complete university-hosted article-in-press version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561) | supports | Live-verified UniProtKB grounding across UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus versutus, UP000256794). Primary mechanism source (loni2020: Loni et al. (2020). Mechanism of microbial dissolution and oxidation of antimony in stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561. Complete university-hosted article-in-press version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml; Canonical EDIT history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml | supports | Canonical EDIT history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml (SHA-256 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5): Added Paracoccus versutus reference-proteome protein examples (SoxAX subunit A UniProtKB:A0AAQ0HFG7, sulfurtransferase UniProtKB:A0AAQ0HHU8) and representative causal graph for aerobic stibnite transformation. |
| validation | data/records/stibnite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/stibnite.yaml and history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:stibnite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T142200Z-stibnite-cycle14-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 3 protein_examples and causal_graphs review of Stibnite (cmmmech:stibnite)
started_at: '2026-11-11T14:21:00Z'
finished_at: '2026-11-11T14:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 3 curation of data/records/stibnite.yaml (SHA-256
    3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a) against live
    UniProtKB grounding and cited primary source (loni2020: Loni et al. (2020). Mechanism
    of microbial dissolution and oxidation of antimony in stibnite under ambient conditions.
    Journal of Hazardous Materials 385, 121561. Complete university-hosted article-in-press
    version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 000fd9c1bad8e0de32a55b4bc1554d4a86696dae
  state: working_tree
  inputs:
  - path: data/records/stibnite.yaml
    sha256: 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a
    role: target
  - path: history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
    sha256: 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:stibnite
  path: data/records/stibnite.yaml
  label: Stibnite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stibnite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/stibnite.yaml
    (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a) and
    its canonical EDIT history sidecar (history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml)
    verifying live UniProtKB grounding (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX
    cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007
    Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate
    sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus
    versutus, UP000256794)), causal-graph node/edge parity across ''xt06_aerobic_stibnite_transformation_graph''
    (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges), and
    primary-source evidence fidelity.'
  selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:stibnite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:stibnite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/stibnite.yaml
  locator: Working-tree record data/records/stibnite.yaml (mechanisms[].protein_examples
    and causal_graphs)
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Updated data/records/stibnite.yaml (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a)
    with live-verified protein_examples (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX
    cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007
    Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate
    sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus
    versutus, UP000256794)) and causal_graphs (''xt06_aerobic_stibnite_transformation_graph''
    (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels.'
  snapshot_sha256: 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1016/j.jhazmat.2019.121561
  locator: 'loni2020: Loni et al. (2020). Mechanism of microbial dissolution and oxidation
    of antimony in stibnite under ambient conditions. Journal of Hazardous Materials
    385, 121561. Complete university-hosted article-in-press version inspected; sections
    2.2-2.4 and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561)'
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE,
    SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007
    Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate
    sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus
    versutus, UP000256794). Primary mechanism source (loni2020: Loni et al. (2020).
    Mechanism of microbial dissolution and oxidation of antimony in stibnite under
    ambient conditions. Journal of Hazardous Materials 385, 121561. Complete university-hosted
    article-in-press version inspected; sections 2.2-2.4 and 3.2-3.4, Table 1, Figures
    1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561)) parameters and source-level
    caveats are strictly preserved on all nodes, edges, and ProteinExample evidence
    items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
  locator: Canonical EDIT history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
    (SHA-256 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5): Added
    Paracoccus versutus reference-proteome protein examples (SoxAX subunit A UniProtKB:A0AAQ0HFG7,
    sulfurtransferase UniProtKB:A0AAQ0HHU8) and representative causal graph for aerobic
    stibnite transformation.'
  snapshot_sha256: 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5
- evidence_id: validation
  kind: validation
  reference: data/records/stibnite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: data/records/stibnite.yaml and history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:stibnite
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
  - cmmmech:stibnite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_causal_graph
  area: graph
  topic: 'Verification of UniProtKB protein_examples grounding, causal_graphs structure,
    and parity across ''xt06_aerobic_stibnite_transformation_graph'' (mechanism_ref:
    xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/stibnite.yaml (SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a)
    with live-verified protein_examples (UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE, SoxAX
    cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007
    Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate
    sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus
    versutus, UP000256794)) and causal_graphs (''xt06_aerobic_stibnite_transformation_graph''
    (mechanism_ref: xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from loni2020: Loni
    et al. (2020). Mechanism of microbial dissolution and oxidation of antimony in
    stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561.
    Complete university-hosted article-in-press version inspected; sections 2.2-2.4
    and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561).'
  target_ids:
  - cmmmech:stibnite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/stibnite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/stibnite/2026-11-11T142112Z-marcin-161e32.yaml
    (SHA-256 53df0d8272e6ba50e1fa4dbca5a73b6529c4ca7857e38c4f4017fe2cc06a8bd5: Added
    Paracoccus versutus reference-proteome protein examples (SoxAX subunit A UniProtKB:A0AAQ0HFG7,
    sulfurtransferase UniProtKB:A0AAQ0HHU8) and representative causal graph for aerobic
    stibnite transformation.) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:stibnite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Stibnite (cmmmech:stibnite) passes Cycle 14 Stage 3 protein_examples review
  (scientific_review: true) at SHA-256 3bf375e9ca0ba225213d8a158e9069925bbc54b5d7f2508ac5b5de18d54a673a:
  Updated data/records/stibnite.yaml with UniProtKB:A0AAQ0HFG7 (A0AAQ0HFG7_PARVE,
  SoxAX cytochrome complex subunit A, gene_symbol: ATH84_103310, TREMBL, NCBITaxon:34007
  Paracoccus versutus, UP000256794); UniProtKB:A0AAQ0HHU8 (A0AAQ0HHU8_PARVE, Thiosulfate/3-mercaptopyruvate
  sulfurtransferase, gene_symbol: ATH84_101652, TREMBL, NCBITaxon:34007 Paracoccus
  versutus, UP000256794) and ''xt06_aerobic_stibnite_transformation_graph'' (mechanism_ref:
  xt06_aerobic_stibnite_transformation, 4 nodes / 3 edges), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from loni2020:
  Loni et al. (2020). Mechanism of microbial dissolution and oxidation of antimony
  in stibnite under ambient conditions. Journal of Hazardous Materials 385, 121561.
  Complete university-hosted article-in-press version inspected; sections 2.2-2.4
  and 3.2-3.4, Table 1, Figures 1 and 4-7. (https://doi.org/10.1016/j.jhazmat.2019.121561).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:stibnite.
related_reviews: []
```
