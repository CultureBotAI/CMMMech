# Cycle 13 Stage 3 protein_examples grounding review of Bismuth (cmmmech:bismuth)

- Review: 20261110T071000Z-bismuth-cycle13-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T07:09:00Z
- Finished UTC: 2026-11-10T07:10:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Bismuth (cmmmech:bismuth) passes Cycle 13 Stage 3 protein_examples review (scientific_review: true) at SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a: Enriched data/records/bismuth.yaml across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005). Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX, Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663).

## Scope And Provenance

Cycle 13 Stage 3 protein_examples review of data/records/bismuth.yaml (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a) and its canonical EDIT history sidecar (history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml) verifying expanded UniProtKB grounding (UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX, Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663)), 100% mechanism-to-node parity, and primary-source evidence fidelity across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges).

Selection: Cycle 13 Stage 3 protein_examples cohort review for cmmmech:bismuth
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4bdd13ae94fd62127aa6ed0d61a164f175fc4461.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bismuth | data/records/bismuth.yaml | maintained | Bismuth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:bismuth | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:bismuth | Checked 1539 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of expanded UniProtKB protein_examples grounding and parity across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)

graph: supported. Targets: cmmmech:bismuth.

Enriched data/records/bismuth.yaml (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a) across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005). Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX, Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:bismuth.

data/records/bismuth.yaml was updated with append-only history sidecar history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml (SHA-256 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12: Add congeneric Fusarium oxysporum Vacuolar transporter chaperone 1 Vtc1 (FOQG_06655, UniProtKB:X0CAN8) to bismuth.yaml) and passes all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/bismuth.yaml; Working-tree record data/records/bismuth.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/bismuth.yaml (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a) with expanded UniProtKB protein_examples across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), maintaining 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1128/AEM.71.2.876-882.2005; dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005) | supports | Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX, Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663). Primary mechanism source (dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml; Canonical EDIT history sidecar history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml | supports | Canonical EDIT history sidecar history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml (SHA-256 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12): Add congeneric Fusarium oxysporum Vacuolar transporter chaperone 1 Vtc1 (FOQG_06655, UniProtKB:X0CAN8) to bismuth.yaml |
| validation | data/records/bismuth.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/bismuth.yaml and history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 3 (protein_examples) for cmmmech:bismuth.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T071000Z-bismuth-cycle13-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 3 protein_examples grounding review of Bismuth (cmmmech:bismuth)
started_at: '2026-11-10T07:09:00Z'
finished_at: '2026-11-10T07:10:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 3 protein_examples enrichment of data/records/bismuth.yaml
    (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a) against
    live UniProtKB grounding and cited primary source (dodge_2005: Dodge and Wackett
    (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of
    Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2),
    876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 4bdd13ae94fd62127aa6ed0d61a164f175fc4461
  state: working_tree
  inputs:
  - path: data/records/bismuth.yaml
    sha256: ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a
    role: target
  - path: history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
    sha256: 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:bismuth
  path: data/records/bismuth.yaml
  label: Bismuth
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bismuth.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 3 protein_examples review of data/records/bismuth.yaml
    (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a) and
    its canonical EDIT history sidecar (history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml)
    verifying expanded UniProtKB grounding (UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate
    hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum
    f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase,
    gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani
    54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone
    complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX,
    Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458
    Fusarium oxysporum f. sp. raphani 54005, UP000030663)), 100% mechanism-to-node
    parity, and primary-source evidence fidelity across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges).'
  selection: Cycle 13 Stage 3 protein_examples cohort review for cmmmech:bismuth
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bismuth
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/bismuth.yaml
  locator: Working-tree record data/records/bismuth.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Enriched data/records/bismuth.yaml (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a)
    with expanded UniProtKB protein_examples across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), maintaining 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.71.2.876-882.2005
  locator: 'dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate
    and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and
    Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005;
    PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)'
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX,
    Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX,
    Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX,
    Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL,
    NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8
    (X0CAN8_FUSOX, Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL,
    NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663). Primary
    mechanism source (dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth
    Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain
    BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005;
    PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)) parameters
    and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
  locator: Canonical EDIT history sidecar history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
    (SHA-256 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12): Add
    congeneric Fusarium oxysporum Vacuolar transporter chaperone 1 Vtc1 (FOQG_06655,
    UniProtKB:X0CAN8) to bismuth.yaml'
  snapshot_sha256: 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12
- evidence_id: validation
  kind: validation
  reference: data/records/bismuth.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: data/records/bismuth.yaml and history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:bismuth
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1539 history record(s); 0 error(s).
  target_ids:
  - cmmmech:bismuth
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_causal_graph_grounding
  area: graph
  topic: 'Verification of expanded UniProtKB protein_examples grounding and parity
    across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)'
  outcome: supported
  summary: 'Enriched data/records/bismuth.yaml (SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a)
    across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from dodge_2005: Dodge
    and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation
    of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2),
    876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005).
    Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate
    hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum
    f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase,
    gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani
    54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone
    complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX,
    Vacuolar transporter chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458
    Fusarium oxysporum f. sp. raphani 54005, UP000030663).'
  target_ids:
  - cmmmech:bismuth
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/bismuth.yaml was updated with append-only history sidecar
    history/records/bismuth/2026-11-10T070945Z-marcin-beb835.yaml (SHA-256 4f0f4f53694d7705eb2e043b3e5f6c4f9c22e65e0e4e87ff147abdd7e4ed1f12:
    Add congeneric Fusarium oxysporum Vacuolar transporter chaperone 1 Vtc1 (FOQG_06655,
    UniProtKB:X0CAN8) to bismuth.yaml) and passes all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:bismuth
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Bismuth (cmmmech:bismuth) passes Cycle 13 Stage 3 protein_examples review
  (scientific_review: true) at SHA-256 ca19abb5afe250b3558f0a480b3c1c17b49241e893c4fe1a3b17d2fc8639991a:
  Enriched data/records/bismuth.yaml across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
  (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from dodge_2005:
  Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular
  Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology
  71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005).
  Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate
  hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum
  f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase,
  gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani
  54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone
  complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum
  f. sp. raphani 54005, UP000030663); UniProtKB:X0CAN8 (X0CAN8_FUSOX, Vacuolar transporter
  chaperone 1, gene_symbol: FOQG_06655, TREMBL, NCBITaxon:1089458 Fusarium oxysporum
  f. sp. raphani 54005, UP000030663).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 3 (protein_examples) for cmmmech:bismuth.
related_reviews: []
```
