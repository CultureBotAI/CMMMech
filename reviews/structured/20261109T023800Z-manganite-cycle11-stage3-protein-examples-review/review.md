# Cycle 11 Stage 3 protein-examples review of Manganite (cmmmech:manganite)

- Review: 20261109T023800Z-manganite-cycle11-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T02:35:00Z
- Finished UTC: 2026-11-09T02:38:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Manganite (cmmmech:manganite) passes Cycle 11 Stage 3 protein-examples review (scientific_review: true) at SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4: Curated data/records/manganite.yaml with causal_graph 'mr4_manganite_reductive_dissolution_graph' (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from larsen1998: Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original, methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244). Live-verified UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM, Cytochrome c biogenesis ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:Q8EG34 (Q8EG34_SHEON, Extracellular iron oxide respiratory system surface decaheme cytochrome c component MtrC, gene_symbol: mtrC, TREMBL, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186).

## Scope And Provenance

Cycle 11 Stage 3 protein-examples review of data/records/manganite.yaml (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4) and its canonical EDIT history sidecar(s) (history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml) verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot parity, and primary-source evidence fidelity across causal_graph 'mr4_manganite_reductive_dissolution_graph' (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]).

Selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:manganite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base df061de720fb9884dcc6e41369a3049cef52a059.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:manganite | data/records/manganite.yaml | maintained | Manganite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:manganite | Checked 698 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:manganite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'mr4_manganite_reductive_dissolution_graph' (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)])

graph: supported. Targets: cmmmech:manganite.

Curated data/records/manganite.yaml (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4) with causal_graph 'mr4_manganite_reductive_dissolution_graph' (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from larsen1998: Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original, methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244). Live-verified UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM, Cytochrome c biogenesis ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:Q8EG34 (Q8EG34_SHEON, Extracellular iron oxide respiratory system surface decaheme cytochrome c component MtrC, gene_symbol: mtrC, TREMBL, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:manganite.

data/records/manganite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml (SHA-256 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3: Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CcmE (UniProtKB:Q8EK44, CCME_SHEON, SO_0259, UP000008186, NCBITaxon:211586) to manganite.yaml (mr4_associated_manganite_reductive_dissolution) alongside exact-strain MR-4 Swiss-Prot UniProtKB:Q0HNQ9 (Cycle 11 Stage 3).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/manganite.yaml; Working-tree record data/records/manganite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated data/records/manganite.yaml (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4) with causal_graph 'mr4_manganite_reductive_dissolution_graph' (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.2138/am-1998-11-1244; larsen1998: Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original, methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244) | supports | Live-verified UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM, Cytochrome c biogenesis ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:Q8EG34 (Q8EG34_SHEON, Extracellular iron oxide respiratory system surface decaheme cytochrome c component MtrC, gene_symbol: mtrC, TREMBL, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186). Primary mechanism source (larsen1998: Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original, methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml; Canonical EDIT history sidecar history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml | supports | Canonical EDIT history sidecar history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml (SHA-256 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3): Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CcmE (UniProtKB:Q8EK44, CCME_SHEON, SO_0259, UP000008186, NCBITaxon:211586) to manganite.yaml (mr4_associated_manganite_reductive_dissolution) alongside exact-strain MR-4 Swiss-Prot UniProtKB:Q0HNQ9 (Cycle 11 Stage 3). |
| validation | data/records/manganite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/manganite.yaml and history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py for cmmmech:manganite following 20261109T004500Z-manganite-cycle11-stage2-causal-graphs-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T023800Z-manganite-cycle11-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 11 Stage 3 protein-examples review of Manganite (cmmmech:manganite)
started_at: '2026-11-09T02:35:00Z'
finished_at: '2026-11-09T02:38:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 UniProtKB ProteinExample curation in data/records/manganite.yaml
    (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4) against
    live UniProtKB REST API grounding and cited primary source (larsen1998: Larsen,
    Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella
    putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original,
    methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: df061de720fb9884dcc6e41369a3049cef52a059
  state: working_tree
  inputs:
  - path: data/records/manganite.yaml
    sha256: b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4
    role: target
  - path: history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
    sha256: 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:manganite
  path: data/records/manganite.yaml
  label: Manganite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
    role: canonical_history
scope:
  description: 'Cycle 11 Stage 3 protein-examples review of data/records/manganite.yaml
    (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4) and
    its canonical EDIT history sidecar(s) (history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml)
    verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot
    parity, and primary-source evidence fidelity across causal_graph ''mr4_manganite_reductive_dissolution_graph''
    (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges;
    ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation:
    [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE,
    CCME_SHEON, UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]).'
  selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:manganite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:manganite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/manganite.yaml
  locator: Working-tree record data/records/manganite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Curated data/records/manganite.yaml (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4)
    with causal_graph ''mr4_manganite_reductive_dissolution_graph'' (mechanism_ref:
    mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter:
    [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9
    (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)];
    cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase:
    [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.2138/am-1998-11-1244
  locator: 'larsen1998: Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite
    reduction by Shewanella putrefaciens MR-4. American Mineralogist 83:1564-1572.
    Complete nine-page original, methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244)'
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM,
    Cytochrome c biogenesis ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT,
    NCBITaxon:60480 Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome
    c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480
    Shewanella sp. MR-4); UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis
    protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis
    (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1),
    UP000008186); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA,
    gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186);
    UniProtKB:Q8EG34 (Q8EG34_SHEON, Extracellular iron oxide respiratory system surface
    decaheme cytochrome c component MtrC, gene_symbol: mtrC, TREMBL, NCBITaxon:211586
    Shewanella oneidensis MR-1, UP000008186). Primary mechanism source (larsen1998:
    Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella
    putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original,
    methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244)) parameters,
    analytical denominators, and source-level caveats are strictly preserved on all
    nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
  locator: Canonical EDIT history sidecar history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
    (SHA-256 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3): Add
    live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome
    CcmE (UniProtKB:Q8EK44, CCME_SHEON, SO_0259, UP000008186, NCBITaxon:211586) to
    manganite.yaml (mr4_associated_manganite_reductive_dissolution) alongside exact-strain
    MR-4 Swiss-Prot UniProtKB:Q0HNQ9 (Cycle 11 Stage 3).'
  snapshot_sha256: 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3
- evidence_id: validation
  kind: validation
  reference: data/records/manganite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: data/records/manganite.yaml and history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 698 record(s); 0 failed.
  target_ids:
  - cmmmech:manganite
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
  - cmmmech:manganite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_graph_parity
  area: graph
  topic: 'Verification of UniProtKB protein_examples grounding and causal-graph parity
    across causal_graph ''mr4_manganite_reductive_dissolution_graph'' (mechanism_ref:
    mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter:
    [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9
    (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)];
    cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase:
    [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)])'
  outcome: supported
  summary: 'Curated data/records/manganite.yaml (SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4)
    with causal_graph ''mr4_manganite_reductive_dissolution_graph'' (mechanism_ref:
    mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges; ccma_exporter:
    [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation: [UniProtKB:Q0HNQ9
    (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON, UP000008186)];
    cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase:
    [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    preserving source-faithful support levels and caveats from larsen1998: Larsen,
    Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella
    putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original,
    methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244). Live-verified
    UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM, Cytochrome c biogenesis
    ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT, NCBITaxon:60480
    Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome c-type biogenesis
    protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4);
    UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis protein CcmE, gene_symbol:
    ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 /
    JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:Q8E8S0
    (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT,
    NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:Q8EG34 (Q8EG34_SHEON,
    Extracellular iron oxide respiratory system surface decaheme cytochrome c component
    MtrC, gene_symbol: mtrC, TREMBL, NCBITaxon:211586 Shewanella oneidensis MR-1,
    UP000008186).'
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/manganite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/manganite/2026-11-09T023713Z-marcin-36525e.yaml
    (SHA-256 8adacfa3bc597a6e2f820c37bc05bb1c94adeadf8202392701cbb3ca404526a3: Add
    live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome
    CcmE (UniProtKB:Q8EK44, CCME_SHEON, SO_0259, UP000008186, NCBITaxon:211586) to
    manganite.yaml (mr4_associated_manganite_reductive_dissolution) alongside exact-strain
    MR-4 Swiss-Prot UniProtKB:Q0HNQ9 (Cycle 11 Stage 3).)) and passing all LinkML
    and history validation gates.'
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Manganite (cmmmech:manganite) passes Cycle 11 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 b5145a3f630e44dba6af97017c927a9eb919e1e46210393e90e4ddac548c14e4:
  Curated data/records/manganite.yaml with causal_graph ''mr4_manganite_reductive_dissolution_graph''
  (mechanism_ref: mr4_associated_manganite_reductive_dissolution, 6 nodes / 5 edges;
  ccma_exporter: [UniProtKB:Q0HNQ5 (ccmA, CCMA_SHESM, NCBITaxon:60480)]; ccme_maturation:
  [UniProtKB:Q0HNQ9 (ccmE, CCME_SHESM, NCBITaxon:60480), UniProtKB:Q8EK44 (ccmE, CCME_SHEON,
  UP000008186)]; cyma_dehydrogenase: [UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)];
  mtrc_reductase: [UniProtKB:Q8EG34 (mtrC, Q8EG34_SHEON, UP000008186)]), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from larsen1998:
  Larsen, Little, Nealson, Ray, Stone and Tian (1998). Manganite reduction by Shewanella
  putrefaciens MR-4. American Mineralogist 83:1564-1572. Complete nine-page original,
  methods, Figures 1-9 and Table 1. (https://doi.org/10.2138/am-1998-11-1244). Live-verified
  UniProtKB grounding across UniProtKB:Q0HNQ5 (CCMA_SHESM, Cytochrome c biogenesis
  ATP-binding export protein CcmA, gene_symbol: ccmA, SWISS_PROT, NCBITaxon:60480
  Shewanella sp. MR-4); UniProtKB:Q0HNQ9 (CCME_SHESM, Cytochrome c-type biogenesis
  protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:60480 Shewanella sp. MR-4);
  UniProtKB:Q8EK44 (CCME_SHEON, Cytochrome c-type biogenesis protein CcmE, gene_symbol:
  ccmE, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM
  31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:Q8E8S0
  (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586
  Shewanella oneidensis MR-1, UP000008186); UniProtKB:Q8EG34 (Q8EG34_SHEON, Extracellular
  iron oxide respiratory system surface decaheme cytochrome c component MtrC, gene_symbol:
  mtrC, TREMBL, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py
  for cmmmech:manganite following 20261109T004500Z-manganite-cycle11-stage2-causal-graphs-review.
related_reviews: []
```
