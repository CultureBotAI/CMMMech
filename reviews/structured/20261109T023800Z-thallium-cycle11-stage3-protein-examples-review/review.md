# Cycle 11 Stage 3 protein-examples review of Thallium (cmmmech:thallium)

- Review: 20261109T023800Z-thallium-cycle11-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T02:35:00Z
- Finished UTC: 2026-11-09T02:38:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Thallium (cmmmech:thallium) passes Cycle 11 Stage 3 protein-examples review (scientific_review: true) at SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332: Curated data/records/thallium.yaml with causal_graph 'cn32_tl_jarosite_mobilization_graph' (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from smeaton2012_chapter4: Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

## Scope And Provenance

Cycle 11 Stage 3 protein-examples review of data/records/thallium.yaml (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332) and its canonical EDIT history sidecar(s) (history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml) verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot parity, and primary-source evidence fidelity across causal_graph 'cn32_tl_jarosite_mobilization_graph' (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]).

Selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:thallium
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base df061de720fb9884dcc6e41369a3049cef52a059.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:thallium | data/records/thallium.yaml | maintained | Thallium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:thallium | Checked 698 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:thallium | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'cn32_tl_jarosite_mobilization_graph' (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)])

graph: supported. Targets: cmmmech:thallium.

Curated data/records/thallium.yaml (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332) with causal_graph 'cn32_tl_jarosite_mobilization_graph' (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from smeaton2012_chapter4: Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:thallium.

data/records/thallium.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml (SHA-256 e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a: Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to thallium.yaml (cn32_associated_tl_mobilization / cn32_tl_jarosite_mobilization_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/thallium.yaml; Working-tree record data/records/thallium.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated data/records/thallium.yaml (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332) with causal_graph 'cn32_tl_jarosite_mobilization_graph' (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF; smeaton2012_chapter4: Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF) | supports | Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084). Primary mechanism source (smeaton2012_chapter4: Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml; Canonical EDIT history sidecar history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml | supports | Canonical EDIT history sidecar history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml (SHA-256 e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a): Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to thallium.yaml (cn32_associated_tl_mobilization / cn32_tl_jarosite_mobilization_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3). |
| validation | data/records/thallium.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/thallium.yaml and history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py for cmmmech:thallium following 20261109T004500Z-thallium-cycle11-stage2-causal-graphs-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T023800Z-thallium-cycle11-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 11 Stage 3 protein-examples review of Thallium (cmmmech:thallium)
started_at: '2026-11-09T02:35:00Z'
finished_at: '2026-11-09T02:38:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 UniProtKB ProteinExample curation in data/records/thallium.yaml
    (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332) against
    live UniProtKB REST API grounding and cited primary source (smeaton2012_chapter4:
    Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility
    of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing
    Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF
    138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7.
    Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: df061de720fb9884dcc6e41369a3049cef52a059
  state: working_tree
  inputs:
  - path: data/records/thallium.yaml
    sha256: 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332
    role: target
  - path: history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
    sha256: e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:thallium
  path: data/records/thallium.yaml
  label: Thallium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thallium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
    role: canonical_history
scope:
  description: 'Cycle 11 Stage 3 protein-examples review of data/records/thallium.yaml
    (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332) and
    its canonical EDIT history sidecar(s) (history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml)
    verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot
    parity, and primary-source evidence fidelity across causal_graph ''cn32_tl_jarosite_mobilization_graph''
    (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)]).'
  selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:thallium
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:thallium
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/thallium.yaml
  locator: Working-tree record data/records/thallium.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Curated data/records/thallium.yaml (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332)
    with causal_graph ''cn32_tl_jarosite_mobilization_graph'' (mechanism_ref: cn32_associated_tl_mobilization,
    5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224),
    UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase:
    [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase:
    [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332
- evidence_id: primary_source
  kind: primary_source
  reference: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF
  locator: 'smeaton2012_chapter4: Smeaton CM (2012), University of Windsor PhD dissertation,
    Investigating the Susceptibility of Jarosite Minerals to Reductive Dissolution
    by a Dissimilatory Metal Reducing Bacterium (Shewanella putrefaciens CN32). Chapter
    4, printed pages 113-148 (PDF 138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4
    and Figures S4.1-S4.7. Author primary account of the same experiment, not independent
    replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF)'
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC,
    Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224
    Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome
    c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella
    putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome
    c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme
    c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084). Primary mechanism source (smeaton2012_chapter4: Smeaton CM (2012),
    University of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite
    Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium
    (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173),
    main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary
    account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF))
    parameters, analytical denominators, and source-level caveats are strictly preserved
    on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
  locator: Canonical EDIT history sidecar history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
    (SHA-256 e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a): Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to thallium.yaml (cn32_associated_tl_mobilization
    / cn32_tl_jarosite_mobilization_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).'
  snapshot_sha256: e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a
- evidence_id: validation
  kind: validation
  reference: data/records/thallium.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: data/records/thallium.yaml and history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 698 record(s); 0 failed.
  target_ids:
  - cmmmech:thallium
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
  - cmmmech:thallium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_graph_parity
  area: graph
  topic: 'Verification of UniProtKB protein_examples grounding and causal-graph parity
    across causal_graph ''cn32_tl_jarosite_mobilization_graph'' (mechanism_ref: cn32_associated_tl_mobilization,
    5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224),
    UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase:
    [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase:
    [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)])'
  outcome: supported
  summary: 'Curated data/records/thallium.yaml (SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332)
    with causal_graph ''cn32_tl_jarosite_mobilization_graph'' (mechanism_ref: cn32_associated_tl_mobilization,
    5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224),
    UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase:
    [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase:
    [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from smeaton2012_chapter4:
    Smeaton CM (2012), University of Windsor PhD dissertation, Investigating the Susceptibility
    of Jarosite Minerals to Reductive Dissolution by a Dissimilatory Metal Reducing
    Bacterium (Shewanella putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF
    138-173), main text, Figures 4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7.
    Author primary account of the same experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF).
    Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome
    c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224
    Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome
    c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella
    putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome
    c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme
    c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084).'
  target_ids:
  - cmmmech:thallium
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/thallium.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/thallium/2026-11-09T023713Z-marcin-d3111b.yaml
    (SHA-256 e5104826de8736c5b190f5af54fc46343c8864a84b00c7354a7306b3e2843f6a: Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to thallium.yaml (cn32_associated_tl_mobilization
    / cn32_tl_jarosite_mobilization_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:thallium
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Thallium (cmmmech:thallium) passes Cycle 11 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 85ec0c1565684049438d1e0acf254fde9d21d08ba46595b9a3abbea14357d332:
  Curated data/records/thallium.yaml with causal_graph ''cn32_tl_jarosite_mobilization_graph''
  (mechanism_ref: cn32_associated_tl_mobilization, 5 nodes / 4 edges; ccme_maturation:
  [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
  A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
  A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
  A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from smeaton2012_chapter4: Smeaton CM (2012), University
  of Windsor PhD dissertation, Investigating the Susceptibility of Jarosite Minerals
  to Reductive Dissolution by a Dissimilatory Metal Reducing Bacterium (Shewanella
  putrefaciens CN32). Chapter 4, printed pages 113-148 (PDF 138-173), main text, Figures
  4.1-4.3, Tables S4.1-S4.4 and Figures S4.1-S4.7. Author primary account of the same
  experiment, not independent replication. (https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/002/NR78584.PDF).
  Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome
  c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224
  Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome
  c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella
  putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type
  protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084);
  UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome,
  gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py
  for cmmmech:thallium following 20261109T004500Z-thallium-cycle11-stage2-causal-graphs-review.
related_reviews: []
```
