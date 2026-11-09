# Cycle 12 Stage 2 post-remediation review (#975) of Potassium feldspar family (cmmmech:potassium-feldspar)

- Review: 20261109T172200Z-potassium-feldspar-cycle12-stage2-issue975-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T17:20:00Z
- Finished UTC: 2026-11-09T17:22:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Potassium feldspar family (cmmmech:potassium-feldspar) passes Cycle 12 Stage 2 post-remediation (#975) review (scientific_review: true) at SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b: Remediated data/records/potassium-feldspar.yaml with causal_graph 'pma2_2_potassium_feldspar_dissolution_graph' (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module: [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses, and metabolic activities determine functional divergence in mineral dissolution between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals, and media; Biotite dissolution experiment; Dissolution of other minerals and gene expression analysis; Results: Generalizability; Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26). Live-verified UniProtKB grounding across UniProtKB:P52932 (SP0A_PRIMG, Stage 0 sporulation protein A, gene_symbol: spo0A, SWISS_PROT, NCBITaxon:1404 Priestia megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1, acetate--CoA ligase, gene_symbol: acsA, TREMBL, NCBITaxon:545693 Priestia megaterium QM B1551, UP000000935); UniProtKB:A0A0B6ASU1 (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine dehydrogenase, gene_symbol: wecC, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate decarboxylase, gene_symbol: lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar basal-body rod protein FlgF, gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2, Glycerol phosphate lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829).

## Scope And Provenance

Cycle 12 Stage 2 post-remediation (#975) review of data/records/potassium-feldspar.yaml (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b) and its canonical EDIT history sidecars (history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml, history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source evidence fidelity across causal_graph 'pma2_2_potassium_feldspar_dissolution_graph' (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module: [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]).

Selection: Cycle 12 Stage 2 Issue #975 post-remediation review for cmmmech:potassium-feldspar
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f3b1cc70981859b389d29f02e3f1bafdc0f0ea6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:potassium-feldspar | data/records/potassium-feldspar.yaml | maintained | Potassium feldspar family |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:potassium-feldspar | Checked 703 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:potassium-feldspar | Checked 1489 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across causal_graph 'pma2_2_potassium_feldspar_dissolution_graph' (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module: [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]) after Issue #975 remediation

graph: supported. Targets: cmmmech:potassium-feldspar.

Remediated data/records/potassium-feldspar.yaml (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b) under Issue #975 with causal_graph 'pma2_2_potassium_feldspar_dissolution_graph' (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module: [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses, and metabolic activities determine functional divergence in mineral dissolution between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals, and media; Biotite dissolution experiment; Dissolution of other minerals and gene expression analysis; Results: Generalizability; Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26). Live-verified UniProtKB grounding across UniProtKB:P52932 (SP0A_PRIMG, Stage 0 sporulation protein A, gene_symbol: spo0A, SWISS_PROT, NCBITaxon:1404 Priestia megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1, acetate--CoA ligase, gene_symbol: acsA, TREMBL, NCBITaxon:545693 Priestia megaterium QM B1551, UP000000935); UniProtKB:A0A0B6ASU1 (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine dehydrogenase, gene_symbol: wecC, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate decarboxylase, gene_symbol: lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar basal-body rod protein FlgF, gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2, Glycerol phosphate lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829).

### Verification of canonical EDIT history sidecars and strict schema validation

provenance: supported. Targets: cmmmech:potassium-feldspar.

data/records/potassium-feldspar.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecars (history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml (SHA-256 dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e: Add pma2_2_potassium_feldspar_dissolution_graph causal graph and ground pma2_2_potassium_feldspar_dissolution to Priestia megaterium Figure 5 RT-qPCR mineral-dissolution proteins (UniProtKB:P52932, UniProtKB:D5DTY8, UniProtKB:A0A0B6ASU1, UniProtKB:A0A0B6ACY5, UniProtKB:A0A0B6AS33, UniProtKB:A0A0B6APG1)); history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml (SHA-256 ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67: Align UniProtKB:P52932 species-proxy support level to partial and add Fig. S6D/S8 ltaS context in potassium-feldspar.yaml (#975))) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/potassium-feldspar.yaml; Working-tree record data/records/potassium-feldspar.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Remediated data/records/potassium-feldspar.yaml (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b) under Issue #975 with causal_graph 'pma2_2_potassium_feldspar_dissolution_graph' (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module: [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1128/aem.01201-26; dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses, and metabolic activities determine functional divergence in mineral dissolution between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals, and media; Biotite dissolution experiment; Dissolution of other minerals and gene expression analysis; Results: Generalizability; Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26) | supports | Live-verified UniProtKB grounding across UniProtKB:P52932 (SP0A_PRIMG, Stage 0 sporulation protein A, gene_symbol: spo0A, SWISS_PROT, NCBITaxon:1404 Priestia megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1, acetate--CoA ligase, gene_symbol: acsA, TREMBL, NCBITaxon:545693 Priestia megaterium QM B1551, UP000000935); UniProtKB:A0A0B6ASU1 (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine dehydrogenase, gene_symbol: wecC, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate decarboxylase, gene_symbol: lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar basal-body rod protein FlgF, gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2, Glycerol phosphate lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829). Primary mechanism source (dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses, and metabolic activities determine functional divergence in mineral dissolution between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals, and media; Biotite dissolution experiment; Dissolution of other minerals and gene expression analysis; Results: Generalizability; Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26)) parameters, RT-qPCR/multi-omics scope, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml; Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml | supports | Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml (SHA-256 dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e): Add pma2_2_potassium_feldspar_dissolution_graph causal graph and ground pma2_2_potassium_feldspar_dissolution to Priestia megaterium Figure 5 RT-qPCR mineral-dissolution proteins (UniProtKB:P52932, UniProtKB:D5DTY8, UniProtKB:A0A0B6ASU1, UniProtKB:A0A0B6ACY5, UniProtKB:A0A0B6AS33, UniProtKB:A0A0B6APG1) |
| edit_history_2 | history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml; Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml | supports | Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml (SHA-256 ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67): Align UniProtKB:P52932 species-proxy support level to partial and add Fig. S6D/S8 ltaS context in potassium-feldspar.yaml (#975) |
| validation | data/records/potassium-feldspar.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/potassium-feldspar.yaml and history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml, history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR re-review is executed prior to merge.
- Executed during Cycle 12 Stage 2 (causal_graphs) following Issue #975 review remediation for cmmmech:potassium-feldspar (PR #974 follow-up to 20261109T163600Z-potassium-feldspar-cycle12-stage2-causal-graphs-review).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T172200Z-potassium-feldspar-cycle12-stage2-issue975-rereview
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 2 post-remediation review (#975) of Potassium feldspar family
  (cmmmech:potassium-feldspar)
started_at: '2026-11-09T17:20:00Z'
finished_at: '2026-11-09T17:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Issue #975 post-remediation state of data/records/potassium-feldspar.yaml
    (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b) against
    live UniProtKB grounding and cited primary source (dong_2026: Dong, Zhang, Yu,
    Sheng, He and Sheng (2026). Genomic traits, transcriptional responses, and metabolic
    activities determine functional divergence in mineral dissolution between Priestia
    megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental Microbiology
    92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals,
    and media; Biotite dissolution experiment; Dissolution of other minerals and gene
    expression analysis; Results: Generalizability; Figure 5; supplement Tables S6-S7
    (pp11-12). (https://doi.org/10.1128/aem.01201-26)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f3b1cc70981859b389d29f02e3f1bafdc0f0ea6c
  state: working_tree
  inputs:
  - path: data/records/potassium-feldspar.yaml
    sha256: e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b
    role: target
  - path: history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
    sha256: dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e
    role: context
  - path: history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
    sha256: ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:potassium-feldspar
  path: data/records/potassium-feldspar.yaml
  label: Potassium feldspar family
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/potassium-feldspar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
    role: canonical_history
scope:
  description: 'Cycle 12 Stage 2 post-remediation (#975) review of data/records/potassium-feldspar.yaml
    (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b) and
    its canonical EDIT history sidecars (history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml,
    history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml) verifying
    causal-graph node/edge topology, live UniProtKB grounding, and primary-source
    evidence fidelity across causal_graph ''pma2_2_potassium_feldspar_dissolution_graph''
    (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module:
    [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA,
    D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829),
    UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33
    (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2,
    UP000031829)]).'
  selection: 'Cycle 12 Stage 2 Issue #975 post-remediation review for cmmmech:potassium-feldspar'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:potassium-feldspar
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/potassium-feldspar.yaml
  locator: Working-tree record data/records/potassium-feldspar.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Remediated data/records/potassium-feldspar.yaml (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b)
    under Issue #975 with causal_graph ''pma2_2_potassium_feldspar_dissolution_graph''
    (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module:
    [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA,
    D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829),
    UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33
    (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2,
    UP000031829)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/aem.01201-26
  locator: 'dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits,
    transcriptional responses, and metabolic activities determine functional divergence
    in mineral dissolution between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1.
    Applied and Environmental Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26;
    Methods: Bacterial strains, minerals, and media; Biotite dissolution experiment;
    Dissolution of other minerals and gene expression analysis; Results: Generalizability;
    Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26)'
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:P52932 (SP0A_PRIMG,
    Stage 0 sporulation protein A, gene_symbol: spo0A, SWISS_PROT, NCBITaxon:1404
    Priestia megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1, acetate--CoA ligase, gene_symbol:
    acsA, TREMBL, NCBITaxon:545693 Priestia megaterium QM B1551, UP000000935); UniProtKB:A0A0B6ASU1
    (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine dehydrogenase, gene_symbol: wecC,
    TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829);
    UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate decarboxylase, gene_symbol:
    lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829);
    UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar basal-body rod protein FlgF,
    gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 =
    ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2, Glycerol phosphate
    lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623 Priestia
    megaterium NBRC 15308 = ATCC 14581, UP000031829). Primary mechanism source (dong_2026:
    Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses,
    and metabolic activities determine functional divergence in mineral dissolution
    between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental
    Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains,
    minerals, and media; Biotite dissolution experiment; Dissolution of other minerals
    and gene expression analysis; Results: Generalizability; Figure 5; supplement
    Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26)) parameters, RT-qPCR/multi-omics
    scope, and source-level caveats are strictly preserved on all nodes, edges, and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
  locator: Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
    (SHA-256 dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e): Add
    pma2_2_potassium_feldspar_dissolution_graph causal graph and ground pma2_2_potassium_feldspar_dissolution
    to Priestia megaterium Figure 5 RT-qPCR mineral-dissolution proteins (UniProtKB:P52932,
    UniProtKB:D5DTY8, UniProtKB:A0A0B6ASU1, UniProtKB:A0A0B6ACY5, UniProtKB:A0A0B6AS33,
    UniProtKB:A0A0B6APG1)'
  snapshot_sha256: dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
  locator: Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
    (SHA-256 ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67): Align
    UniProtKB:P52932 species-proxy support level to partial and add Fig. S6D/S8 ltaS
    context in potassium-feldspar.yaml (#975)'
  snapshot_sha256: ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67
- evidence_id: validation
  kind: validation
  reference: data/records/potassium-feldspar.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: data/records/potassium-feldspar.yaml and history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml,
    history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml pass
    strict LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 703 record(s); 0 failed.
  target_ids:
  - cmmmech:potassium-feldspar
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1489 history record(s); 0 error(s).
  target_ids:
  - cmmmech:potassium-feldspar
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across causal_graph ''pma2_2_potassium_feldspar_dissolution_graph'' (mechanism_ref:
    pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module:
    [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA,
    D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829),
    UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33
    (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2,
    UP000031829)]) after Issue #975 remediation'
  outcome: supported
  summary: 'Remediated data/records/potassium-feldspar.yaml (SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b)
    under Issue #975 with causal_graph ''pma2_2_potassium_feldspar_dissolution_graph''
    (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module:
    [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA,
    D5DTY8_PRIM1, UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829),
    UniProtKB:A0A0B6ACY5 (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33
    (flgF, A0A0B6AS33_PRIM2, UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2,
    UP000031829)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from dong_2026: Dong, Zhang, Yu, Sheng, He and Sheng (2026).
    Genomic traits, transcriptional responses, and metabolic activities determine
    functional divergence in mineral dissolution between Priestia megaterium PMA2-2
    and Priestia flexa PMD1-1. Applied and Environmental Microbiology 92(9):e01201-26.
    DOI 10.1128/aem.01201-26; Methods: Bacterial strains, minerals, and media; Biotite
    dissolution experiment; Dissolution of other minerals and gene expression analysis;
    Results: Generalizability; Figure 5; supplement Tables S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26).
    Live-verified UniProtKB grounding across UniProtKB:P52932 (SP0A_PRIMG, Stage 0
    sporulation protein A, gene_symbol: spo0A, SWISS_PROT, NCBITaxon:1404 Priestia
    megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1, acetate--CoA ligase, gene_symbol:
    acsA, TREMBL, NCBITaxon:545693 Priestia megaterium QM B1551, UP000000935); UniProtKB:A0A0B6ASU1
    (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine dehydrogenase, gene_symbol: wecC,
    TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829);
    UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate decarboxylase, gene_symbol:
    lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829);
    UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar basal-body rod protein FlgF,
    gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia megaterium NBRC 15308 =
    ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2, Glycerol phosphate
    lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623 Priestia
    megaterium NBRC 15308 = ATCC 14581, UP000031829).'
  target_ids:
  - cmmmech:potassium-feldspar
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecars and strict schema validation
  outcome: supported
  summary: 'data/records/potassium-feldspar.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecars (history/records/potassium-feldspar/2026-11-09T163432Z-marcin-b8911d.yaml
    (SHA-256 dda41c16a4b58b85797e3f2402d01808ab04dc730d9e98072f507b50907e825e: Add
    pma2_2_potassium_feldspar_dissolution_graph causal graph and ground pma2_2_potassium_feldspar_dissolution
    to Priestia megaterium Figure 5 RT-qPCR mineral-dissolution proteins (UniProtKB:P52932,
    UniProtKB:D5DTY8, UniProtKB:A0A0B6ASU1, UniProtKB:A0A0B6ACY5, UniProtKB:A0A0B6AS33,
    UniProtKB:A0A0B6APG1)); history/records/potassium-feldspar/2026-11-09T172114Z-marcin-445cab.yaml
    (SHA-256 ffc4f97dfd5c8c4ab95a0f95bd59d0e6a8b46b79b13a7b919f1d227083188b67: Align
    UniProtKB:P52932 species-proxy support level to partial and add Fig. S6D/S8 ltaS
    context in potassium-feldspar.yaml (#975))) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:potassium-feldspar
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Potassium feldspar family (cmmmech:potassium-feldspar) passes Cycle 12 Stage
  2 post-remediation (#975) review (scientific_review: true) at SHA-256 e461910671f3a22fdb3c5ae4a86d3f0be7fb6b3356eec2c68c2fc0ba8e315b3b:
  Remediated data/records/potassium-feldspar.yaml with causal_graph ''pma2_2_potassium_feldspar_dissolution_graph''
  (mechanism_ref: pma2_2_potassium_feldspar_dissolution, 4 nodes / 3 edges; pma2_2_kfeldspar_induced_gene_module:
  [UniProtKB:P52932 (spo0A, SP0A_PRIMG, NCBITaxon:1404), UniProtKB:D5DTY8 (acsA, D5DTY8_PRIM1,
  UP000000935), UniProtKB:A0A0B6ASU1 (wecC, A0A0B6ASU1_PRIM2, UP000031829), UniProtKB:A0A0B6ACY5
  (lysA, A0A0B6ACY5_PRIM2, UP000031829), UniProtKB:A0A0B6AS33 (flgF, A0A0B6AS33_PRIM2,
  UP000031829), UniProtKB:A0A0B6APG1 (ltaS1, A0A0B6APG1_PRIM2, UP000031829)]), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from dong_2026:
  Dong, Zhang, Yu, Sheng, He and Sheng (2026). Genomic traits, transcriptional responses,
  and metabolic activities determine functional divergence in mineral dissolution
  between Priestia megaterium PMA2-2 and Priestia flexa PMD1-1. Applied and Environmental
  Microbiology 92(9):e01201-26. DOI 10.1128/aem.01201-26; Methods: Bacterial strains,
  minerals, and media; Biotite dissolution experiment; Dissolution of other minerals
  and gene expression analysis; Results: Generalizability; Figure 5; supplement Tables
  S6-S7 (pp11-12). (https://doi.org/10.1128/aem.01201-26). Live-verified UniProtKB
  grounding across UniProtKB:P52932 (SP0A_PRIMG, Stage 0 sporulation protein A, gene_symbol:
  spo0A, SWISS_PROT, NCBITaxon:1404 Priestia megaterium); UniProtKB:D5DTY8 (D5DTY8_PRIM1,
  acetate--CoA ligase, gene_symbol: acsA, TREMBL, NCBITaxon:545693 Priestia megaterium
  QM B1551, UP000000935); UniProtKB:A0A0B6ASU1 (A0A0B6ASU1_PRIM2, UDP-N-acetyl-D-mannosamine
  dehydrogenase, gene_symbol: wecC, TREMBL, NCBITaxon:1348623 Priestia megaterium
  NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6ACY5 (A0A0B6ACY5_PRIM2, Diaminopimelate
  decarboxylase, gene_symbol: lysA, TREMBL, NCBITaxon:1348623 Priestia megaterium
  NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6AS33 (A0A0B6AS33_PRIM2, Flagellar
  basal-body rod protein FlgF, gene_symbol: flgF, TREMBL, NCBITaxon:1348623 Priestia
  megaterium NBRC 15308 = ATCC 14581, UP000031829); UniProtKB:A0A0B6APG1 (A0A0B6APG1_PRIM2,
  Glycerol phosphate lipoteichoic acid synthase 1, gene_symbol: ltaS1, TREMBL, NCBITaxon:1348623
  Priestia megaterium NBRC 15308 = ATCC 14581, UP000031829).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR re-review is executed prior to merge.'
notes:
- 'Executed during Cycle 12 Stage 2 (causal_graphs) following Issue #975 review remediation
  for cmmmech:potassium-feldspar (PR #974 follow-up to 20261109T163600Z-potassium-feldspar-cycle12-stage2-causal-graphs-review).'
related_reviews: []
```
