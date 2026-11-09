# Cycle 11 Stage 3 Issue #964 remediation review of Feroxyhyte (cmmmech:feroxyhyte)

- Review: 20261109T032700Z-feroxyhyte-cycle11-stage3-issue964-remediation-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T03:23:00Z
- Finished UTC: 2026-11-09T03:27:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Feroxyhyte (cmmmech:feroxyhyte) passes Cycle 11 Stage 3 Issue #964 remediation review (scientific_review: true) at SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829: Remediated data/records/feroxyhyte.yaml with causal_graph 'cn32_feroxyhyte_reduction_graph' (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and experimental caveats from oloughlin_2021: O'Loughlin, Boyanov, Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

## Scope And Provenance

Cycle 11 Stage 3 Issue #964 remediation review of data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829) and its canonical EDIT history sidecar(s) (history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml, history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml) verifying live UniProtKB protein grounding, source-faithful evidence explanations, reference-proteome and Swiss-Prot parity, and causal-edge descriptions across causal_graph 'cn32_feroxyhyte_reduction_graph' (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]).

Selection: Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:feroxyhyte
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f622889fbaf868e6f444fa93e4ce9790d45a9514.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:feroxyhyte | data/records/feroxyhyte.yaml | maintained | Feroxyhyte |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:feroxyhyte | Checked 698 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:feroxyhyte | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of remediated UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'cn32_feroxyhyte_reduction_graph' (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)])

graph: supported. Targets: cmmmech:feroxyhyte.

Remediated data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829) under Issue #964 with causal_graph 'cn32_feroxyhyte_reduction_graph' (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and caveats from oloughlin_2021: O'Loughlin, Boyanov, Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:feroxyhyte.

data/records/feroxyhyte.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml (SHA-256 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf: Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to feroxyhyte.yaml (cn32_feroxyhyte_reductive_transformation / cn32_feroxyhyte_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3).); history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml (SHA-256 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666: Fix UniProtKB:A0ABX8XC47 evidence explanation in feroxyhyte.yaml to accurately describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975) (Issue #964).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/feroxyhyte.yaml; Working-tree record data/records/feroxyhyte.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated and remediated data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829) with causal_graph 'cn32_feroxyhyte_reduction_graph' (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving strictly entry-specific, source-faithful explanations and caveats. |
| primary_source | https://doi.org/10.3390/min11020149; oloughlin_2021: O'Loughlin, Boyanov, Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149) | supports | Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084). Primary mechanism source (oloughlin_2021: O'Loughlin, Boyanov, Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml; Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml | supports | Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml (SHA-256 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf): Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to feroxyhyte.yaml (cn32_feroxyhyte_reductive_transformation / cn32_feroxyhyte_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3). |
| edit_history_2 | history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml; Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml | supports | Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml (SHA-256 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666): Fix UniProtKB:A0ABX8XC47 evidence explanation in feroxyhyte.yaml to accurately describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975) (Issue #964). |
| validation | data/records/feroxyhyte.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/feroxyhyte.yaml and history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml, history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using scripts/curate_causal_graphs.py for cmmmech:feroxyhyte, succeeding 20261109T023800Z-feroxyhyte-cycle11-stage3-protein-examples-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T032700Z-feroxyhyte-cycle11-stage3-issue964-remediation-review
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 11 Stage 3 Issue #964 remediation review of Feroxyhyte (cmmmech:feroxyhyte)'
started_at: '2026-11-09T03:23:00Z'
finished_at: '2026-11-09T03:27:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 Issue #964 remediated UniProtKB ProteinExample
    curation in data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829)
    against live UniProtKB REST API grounding and cited primary source (oloughlin_2021:
    O''Loughlin, Boyanov, Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide
    Mineralogy and Phosphate on Fe(II) Secondary Mineral Formation during Microbial
    Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149. Complete 43-page
    original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables
    4-5. (https://doi.org/10.3390/min11020149)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f622889fbaf868e6f444fa93e4ce9790d45a9514
  state: working_tree
  inputs:
  - path: data/records/feroxyhyte.yaml
    sha256: c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829
    role: target
  - path: history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
    sha256: 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf
    role: context
  - path: history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
    sha256: 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:feroxyhyte
  path: data/records/feroxyhyte.yaml
  label: Feroxyhyte
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feroxyhyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
    role: canonical_history
scope:
  description: 'Cycle 11 Stage 3 Issue #964 remediation review of data/records/feroxyhyte.yaml
    (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829) and
    its canonical EDIT history sidecar(s) (history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml,
    history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml) verifying live
    UniProtKB protein grounding, source-faithful evidence explanations, reference-proteome
    and Swiss-Prot parity, and causal-edge descriptions across causal_graph ''cn32_feroxyhyte_reduction_graph''
    (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)]).'
  selection: 'Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:feroxyhyte'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:feroxyhyte
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/feroxyhyte.yaml
  locator: Working-tree record data/records/feroxyhyte.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Curated and remediated data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829)
    with causal_graph ''cn32_feroxyhyte_reduction_graph'' (mechanism_ref: cn32_feroxyhyte_reductive_transformation,
    5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224),
    UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase:
    [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase:
    [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving strictly entry-specific, source-faithful explanations and caveats.'
  snapshot_sha256: c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3390/min11020149
  locator: 'oloughlin_2021: O''Loughlin, Boyanov, Gorski, Scherer and Kemner (2021).
    Effects of Fe(III) Oxide Mineralogy and Phosphate on Fe(II) Secondary Mineral
    Formation during Microbial Iron Reduction. Minerals 11(2):149. DOI 10.3390/min11020149.
    Complete 43-page original publisher PDF; Sections 2.1-2.3, 3.7 and 4.1-4.4; Figures
    22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149)'
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC,
    Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224
    Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome
    c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella
    putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome
    c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme
    c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens,
    UP000827084). Primary mechanism source (oloughlin_2021: O''Loughlin, Boyanov,
    Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate
    on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals
    11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections
    2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149))
    parameters, analytical denominators, and source-level caveats are strictly preserved
    on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
  locator: Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
    (SHA-256 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf): Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to feroxyhyte.yaml (cn32_feroxyhyte_reductive_transformation
    / cn32_feroxyhyte_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).'
  snapshot_sha256: 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
  locator: Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
    (SHA-256 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666): Fix
    UniProtKB:A0ABX8XC47 evidence explanation in feroxyhyte.yaml to accurately describe
    the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975)
    (Issue #964).'
  snapshot_sha256: 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666
- evidence_id: validation
  kind: validation
  reference: data/records/feroxyhyte.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: data/records/feroxyhyte.yaml and history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml,
    history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml pass strict LinkML
    schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 698 record(s); 0 failed.
  target_ids:
  - cmmmech:feroxyhyte
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
  - cmmmech:feroxyhyte
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_graph_parity
  area: graph
  topic: 'Verification of remediated UniProtKB protein_examples grounding and causal-graph
    parity across causal_graph ''cn32_feroxyhyte_reduction_graph'' (mechanism_ref:
    cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)])'
  outcome: supported
  summary: 'Remediated data/records/feroxyhyte.yaml (SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829)
    under Issue #964 with causal_graph ''cn32_feroxyhyte_reduction_graph'' (mechanism_ref:
    cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
    support levels and caveats from oloughlin_2021: O''Loughlin, Boyanov, Gorski,
    Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate on
    Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals 11(2):149.
    DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections 2.1-2.3,
    3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149).
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
  - cmmmech:feroxyhyte
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/feroxyhyte.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/feroxyhyte/2026-11-09T023712Z-marcin-90dfc9.yaml
    (SHA-256 8206aaca85d9c455fdb0cb636ec5432e21c19950a61c11ea72f33822808a85bf: Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to feroxyhyte.yaml (cn32_feroxyhyte_reductive_transformation
    / cn32_feroxyhyte_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).); history/records/feroxyhyte/2026-11-09T032336Z-marcin-691f9d.yaml
    (SHA-256 3e79d71fd97084b67f38d545f53a26ed318e695eb2058cef7889b805b3ff4666: Fix
    UniProtKB:A0ABX8XC47 evidence explanation in feroxyhyte.yaml to accurately describe
    the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975)
    (Issue #964).)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Feroxyhyte (cmmmech:feroxyhyte) passes Cycle 11 Stage 3 Issue #964 remediation
  review (scientific_review: true) at SHA-256 c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829:
  Remediated data/records/feroxyhyte.yaml with causal_graph ''cn32_feroxyhyte_reduction_graph''
  (mechanism_ref: cn32_feroxyhyte_reductive_transformation, 5 nodes / 4 edges; ccme_maturation:
  [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
  A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
  A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
  A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
  support levels and experimental caveats from oloughlin_2021: O''Loughlin, Boyanov,
  Gorski, Scherer and Kemner (2021). Effects of Fe(III) Oxide Mineralogy and Phosphate
  on Fe(II) Secondary Mineral Formation during Microbial Iron Reduction. Minerals
  11(2):149. DOI 10.3390/min11020149. Complete 43-page original publisher PDF; Sections
  2.1-2.3, 3.7 and 4.1-4.4; Figures 22-24 and Tables 4-5. (https://doi.org/10.3390/min11020149).
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
- 'Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using
  scripts/curate_causal_graphs.py for cmmmech:feroxyhyte, succeeding 20261109T023800Z-feroxyhyte-cycle11-stage3-protein-examples-review.'
related_reviews: []
```
