# Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Bismuth (cmmmech:bismuth)

- Review: 20261110T054200Z-bismuth-cycle13-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T05:40:00Z
- Finished UTC: 2026-11-10T05:42:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Bismuth (cmmmech:bismuth) passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92: Updated data/records/bismuth.yaml with 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005). Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663).

## Scope And Provenance

Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/bismuth.yaml (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92) and its canonical EDIT history sidecar (history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663)), and primary-source evidence fidelity across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges).

Selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:bismuth
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bismuth | data/records/bismuth.yaml | maintained | Bismuth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:bismuth | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:bismuth | Checked 1529 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)

graph: supported. Targets: cmmmech:bismuth.

Updated data/records/bismuth.yaml (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92) with causal_graphs ('fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005). Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:bismuth.

data/records/bismuth.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml (SHA-256 a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06: Add fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph causal graph and ground fusarium_bi_accumulation to congeneric Fusarium oxysporum reference-proteome enzymes (UniProtKB:X0BR20, UniProtKB:X0CKS8, UniProtKB:X0D0Y4)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/bismuth.yaml; Working-tree record data/records/bismuth.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/bismuth.yaml (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92) with causal_graphs ('fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph' (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1128/AEM.71.2.876-882.2005; dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005) | supports | Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX, Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX, Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL, NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663). Primary mechanism source (dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml; Canonical EDIT history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml | supports | Canonical EDIT history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml (SHA-256 a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06): Add fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph causal graph and ground fusarium_bi_accumulation to congeneric Fusarium oxysporum reference-proteome enzymes (UniProtKB:X0BR20, UniProtKB:X0CKS8, UniProtKB:X0D0Y4) |
| validation | data/records/bismuth.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/bismuth.yaml and history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:bismuth.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T054200Z-bismuth-cycle13-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Bismuth (cmmmech:bismuth)
started_at: '2026-11-10T05:40:00Z'
finished_at: '2026-11-10T05:42:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 2 curation of data/records/bismuth.yaml (SHA-256
    fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92) against live
    UniProtKB grounding and cited primary source (dodge_2005: Dodge and Wackett (2005).
    Metabolism of Bismuth Subsalicylate and Intracellular Accumulation of Bismuth
    by Fusarium sp. Strain BI. Applied and Environmental Microbiology 71(2), 876-882.
    DOI 10.1128/AEM.71.2.876-882.2005; PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5
  state: working_tree
  inputs:
  - path: data/records/bismuth.yaml
    sha256: fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92
    role: target
  - path: history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
    sha256: a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06
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
    path: history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/bismuth.yaml
    (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92) and
    its canonical EDIT history sidecar (history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:X0BR20
    (X0BR20_FUSOX, Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458
    Fusarium oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX,
    Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX,
    Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL,
    NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663)), and
    primary-source evidence fidelity across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges).'
  selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:bismuth
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bismuth
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/bismuth.yaml
  locator: Working-tree record data/records/bismuth.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Updated data/records/bismuth.yaml (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92)
    with causal_graphs (''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.71.2.876-882.2005
  locator: 'dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth Subsalicylate
    and Intracellular Accumulation of Bismuth by Fusarium sp. Strain BI. Applied and
    Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005;
    PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)'
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:X0BR20 (X0BR20_FUSOX,
    Salicylate hydroxylase, gene_symbol: FOQG_11564, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0CKS8 (X0CKS8_FUSOX,
    Catechol 1,2-dioxygenase, gene_symbol: FOQG_12499, TREMBL, NCBITaxon:1089458 Fusarium
    oxysporum f. sp. raphani 54005, UP000030663); UniProtKB:X0D0Y4 (X0D0Y4_FUSOX,
    Vacuolar transporter chaperone complex subunit 4, gene_symbol: FOQG_08633, TREMBL,
    NCBITaxon:1089458 Fusarium oxysporum f. sp. raphani 54005, UP000030663). Primary
    mechanism source (dodge_2005: Dodge and Wackett (2005). Metabolism of Bismuth
    Subsalicylate and Intracellular Accumulation of Bismuth by Fusarium sp. Strain
    BI. Applied and Environmental Microbiology 71(2), 876-882. DOI 10.1128/AEM.71.2.876-882.2005;
    PMID 15691943; PMC546758. (https://doi.org/10.1128/AEM.71.2.876-882.2005)) parameters
    and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
  locator: Canonical EDIT history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
    (SHA-256 a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06): Add
    fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph causal graph
    and ground fusarium_bi_accumulation to congeneric Fusarium oxysporum reference-proteome
    enzymes (UniProtKB:X0BR20, UniProtKB:X0CKS8, UniProtKB:X0D0Y4)'
  snapshot_sha256: a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06
- evidence_id: validation
  kind: validation
  reference: data/records/bismuth.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: data/records/bismuth.yaml and history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92
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
  summary: Checked 1529 history record(s); 0 error(s).
  target_ids:
  - cmmmech:bismuth
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)'
  outcome: supported
  summary: 'Updated data/records/bismuth.yaml (SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92)
    with causal_graphs (''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
    (mechanism_ref: fusarium_bi_accumulation, 6 nodes / 5 edges)), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
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
    oxysporum f. sp. raphani 54005, UP000030663).'
  target_ids:
  - cmmmech:bismuth
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/bismuth.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/bismuth/2026-11-10T054033Z-marcin-a4c985.yaml
    (SHA-256 a1563f986b7930504181ce0af8d10f224cc1830d6a98b79f6138b00dc7843f06: Add
    fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph causal graph
    and ground fusarium_bi_accumulation to congeneric Fusarium oxysporum reference-proteome
    enzymes (UniProtKB:X0BR20, UniProtKB:X0CKS8, UniProtKB:X0D0Y4)) and passing all
    LinkML and history validation gates.'
  target_ids:
  - cmmmech:bismuth
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Bismuth (cmmmech:bismuth) passes Cycle 13 Stage 2 causal_graphs review (scientific_review:
  true) at SHA-256 fd6264da92fa86b96ec62f816883df0d99e0e0d035b3e8e901849bb3d179ee92:
  Updated data/records/bismuth.yaml with ''fusarium_bi_subsalicylate_catabolism_and_granule_accumulation_graph''
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
  f. sp. raphani 54005, UP000030663).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:bismuth.
related_reviews: []
```
