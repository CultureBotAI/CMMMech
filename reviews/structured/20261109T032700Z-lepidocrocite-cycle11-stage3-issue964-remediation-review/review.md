# Cycle 11 Stage 3 Issue #964 remediation review of Lepidocrocite (cmmmech:lepidocrocite)

- Review: 20261109T032700Z-lepidocrocite-cycle11-stage3-issue964-remediation-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T03:23:00Z
- Finished UTC: 2026-11-09T03:27:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Lepidocrocite (cmmmech:lepidocrocite) passes Cycle 11 Stage 3 Issue #964 remediation review (scientific_review: true) at SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32: Remediated data/records/lepidocrocite.yaml with causal_graph 'cn32_lepidocrocite_reduction_graph' (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and experimental caveats from oloughlin_2019: O'Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher copy. (https://doi.org/10.3390/min9070434). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

## Scope And Provenance

Cycle 11 Stage 3 Issue #964 remediation review of data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32) and its canonical EDIT history sidecar(s) (history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml, history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml) verifying live UniProtKB protein grounding, source-faithful evidence explanations, reference-proteome and Swiss-Prot parity, and causal-edge descriptions across causal_graph 'cn32_lepidocrocite_reduction_graph' (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]).

Selection: Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:lepidocrocite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f622889fbaf868e6f444fa93e4ce9790d45a9514.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lepidocrocite | data/records/lepidocrocite.yaml | maintained | Lepidocrocite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:lepidocrocite | Checked 698 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:lepidocrocite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of remediated UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'cn32_lepidocrocite_reduction_graph' (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)])

graph: supported. Targets: cmmmech:lepidocrocite.

Remediated data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32) under Issue #964 with causal_graph 'cn32_lepidocrocite_reduction_graph' (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and caveats from oloughlin_2019: O'Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher copy. (https://doi.org/10.3390/min9070434). Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:lepidocrocite.

data/records/lepidocrocite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml (SHA-256 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d: Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to lepidocrocite.yaml (cn32_formate_lepidocrocite_transformation / cn32_lepidocrocite_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3).); history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml (SHA-256 e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105: Fix UniProtKB:A0ABX8XC47 evidence explanation in lepidocrocite.yaml to accurately describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975) (Issue #964).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/lepidocrocite.yaml; Working-tree record data/records/lepidocrocite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated and remediated data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32) with causal_graph 'cn32_lepidocrocite_reduction_graph' (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving strictly entry-specific, source-faithful explanations and caveats. |
| primary_source | https://doi.org/10.3390/min9070434; oloughlin_2019: O'Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher copy. (https://doi.org/10.3390/min9070434) | supports | Live-verified UniProtKB grounding across UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47 (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9 (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084). Primary mechanism source (oloughlin_2019: O'Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher copy. (https://doi.org/10.3390/min9070434)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml; Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml | supports | Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml (SHA-256 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d): Add live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47, K3G22_00975, UP000827084, NCBITaxon:24) to lepidocrocite.yaml (cn32_formate_lepidocrocite_transformation / cn32_lepidocrocite_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6 (Cycle 11 Stage 3). |
| edit_history_2 | history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml; Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml | supports | Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml (SHA-256 e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105): Fix UniProtKB:A0ABX8XC47 evidence explanation in lepidocrocite.yaml to accurately describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE entry (K3G22_00975) (Issue #964). |
| validation | data/records/lepidocrocite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/lepidocrocite.yaml and history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml, history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using scripts/curate_causal_graphs.py for cmmmech:lepidocrocite, succeeding 20261109T023800Z-lepidocrocite-cycle11-stage3-protein-examples-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T032700Z-lepidocrocite-cycle11-stage3-issue964-remediation-review
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 11 Stage 3 Issue #964 remediation review of Lepidocrocite (cmmmech:lepidocrocite)'
started_at: '2026-11-09T03:23:00Z'
finished_at: '2026-11-09T03:27:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 Issue #964 remediated UniProtKB ProteinExample
    curation in data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32)
    against live UniProtKB REST API grounding and cited primary source (oloughlin_2019:
    O''Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization
    and Secondary Mineral Formation during the Bioreduction of Lepidocrocite by Shewanella
    putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher
    PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6,
    Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in
    the 30-page publisher copy. (https://doi.org/10.3390/min9070434)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f622889fbaf868e6f444fa93e4ce9790d45a9514
  state: working_tree
  inputs:
  - path: data/records/lepidocrocite.yaml
    sha256: c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32
    role: target
  - path: history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
    sha256: 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d
    role: context
  - path: history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
    sha256: e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:lepidocrocite
  path: data/records/lepidocrocite.yaml
  label: Lepidocrocite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lepidocrocite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
    role: canonical_history
scope:
  description: 'Cycle 11 Stage 3 Issue #964 remediation review of data/records/lepidocrocite.yaml
    (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32) and
    its canonical EDIT history sidecar(s) (history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml,
    history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml) verifying
    live UniProtKB protein grounding, source-faithful evidence explanations, reference-proteome
    and Swiss-Prot parity, and causal-edge descriptions across causal_graph ''cn32_lepidocrocite_reduction_graph''
    (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges;
    ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47
    (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9
    (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6
    (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]).'
  selection: 'Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:lepidocrocite'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lepidocrocite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/lepidocrocite.yaml
  locator: Working-tree record data/records/lepidocrocite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Curated and remediated data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32)
    with causal_graph ''cn32_lepidocrocite_reduction_graph'' (mechanism_ref: cn32_formate_lepidocrocite_transformation,
    5 nodes / 4 edges; ccme_maturation: [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224),
    UniProtKB:A0ABX8XC47 (ccmE, A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase:
    [UniProtKB:A0ABX8XAW9 (cymA, A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase:
    [UniProtKB:A0ABX8XFE6 (K3G22_06995, A0ABX8XFE6_SHEPU, UP000827084)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving strictly entry-specific, source-faithful explanations and caveats.'
  snapshot_sha256: c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3390/min9070434
  locator: 'oloughlin_2019: O''Loughlin EJ, Gorski CA, Flynn TM and Scherer MM (2019).
    Electron Donor Utilization and Secondary Mineral Formation during the Bioreduction
    of Lepidocrocite by Shewanella putrefaciens CN32. Minerals 9:434. DOI 10.3390/min9070434.
    Original complete publisher PDF and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3,
    Tables 1-3, Figures 1-6, Discussion. The 29-page OSTI copy preserves the full-width
    Table 1 cropped in the 30-page publisher copy. (https://doi.org/10.3390/min9070434)'
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
    UP000827084). Primary mechanism source (oloughlin_2019: O''Loughlin EJ, Gorski
    CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral
    Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens
    CN32. Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF
    and OSTI 1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6,
    Discussion. The 29-page OSTI copy preserves the full-width Table 1 cropped in
    the 30-page publisher copy. (https://doi.org/10.3390/min9070434)) parameters,
    analytical denominators, and source-level caveats are strictly preserved on all
    nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
  locator: Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
    (SHA-256 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d): Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to lepidocrocite.yaml (cn32_formate_lepidocrocite_transformation
    / cn32_lepidocrocite_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).'
  snapshot_sha256: 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
  locator: Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
    (SHA-256 e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105): Fix
    UniProtKB:A0ABX8XC47 evidence explanation in lepidocrocite.yaml to accurately
    describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE
    entry (K3G22_00975) (Issue #964).'
  snapshot_sha256: e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105
- evidence_id: validation
  kind: validation
  reference: data/records/lepidocrocite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: data/records/lepidocrocite.yaml and history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml,
    history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml pass strict
    LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 698 record(s); 0 failed.
  target_ids:
  - cmmmech:lepidocrocite
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
  - cmmmech:lepidocrocite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_graph_parity
  area: graph
  topic: 'Verification of remediated UniProtKB protein_examples grounding and causal-graph
    parity across causal_graph ''cn32_lepidocrocite_reduction_graph'' (mechanism_ref:
    cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)])'
  outcome: supported
  summary: 'Remediated data/records/lepidocrocite.yaml (SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32)
    under Issue #964 with causal_graph ''cn32_lepidocrocite_reduction_graph'' (mechanism_ref:
    cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation:
    [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
    A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
    A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
    A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
    support levels and caveats from oloughlin_2019: O''Loughlin EJ, Gorski CA, Flynn
    TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral Formation
    during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32. Minerals
    9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI 1560537
    copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion. The 29-page
    OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher copy.
    (https://doi.org/10.3390/min9070434). Live-verified UniProtKB grounding across
    UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol:
    ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47
    (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE,
    TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9
    (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24
    Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU,
    OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL,
    NCBITaxon:24 Shewanella putrefaciens, UP000827084).'
  target_ids:
  - cmmmech:lepidocrocite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/lepidocrocite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/lepidocrocite/2026-11-09T023712Z-marcin-205f69.yaml
    (SHA-256 3be10dc6e25dd37065ef994ff60daeab66d4c14584316116bdc79c16b616304d: Add
    live-verified species-level Shewanella putrefaciens reference-proteome CcmE (UniProtKB:A0ABX8XC47,
    K3G22_00975, UP000827084, NCBITaxon:24) to lepidocrocite.yaml (cn32_formate_lepidocrocite_transformation
    / cn32_lepidocrocite_reduction_graph) alongside exact-strain Swiss-Prot UniProtKB:A4YBV6
    (Cycle 11 Stage 3).); history/records/lepidocrocite/2026-11-09T032336Z-marcin-61cc93.yaml
    (SHA-256 e723f103c211e9fec268747a78f85dd9ab316c32294c30b90fa1e862b703a105: Fix
    UniProtKB:A0ABX8XC47 evidence explanation in lepidocrocite.yaml to accurately
    describe the unreviewed TrEMBL UP000827084 species-level S. putrefaciens CcmE
    entry (K3G22_00975) (Issue #964).)) and passing all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:lepidocrocite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Lepidocrocite (cmmmech:lepidocrocite) passes Cycle 11 Stage 3 Issue #964
  remediation review (scientific_review: true) at SHA-256 c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32:
  Remediated data/records/lepidocrocite.yaml with causal_graph ''cn32_lepidocrocite_reduction_graph''
  (mechanism_ref: cn32_formate_lepidocrocite_transformation, 5 nodes / 4 edges; ccme_maturation:
  [UniProtKB:A4YBV6 (ccmE, CCME_SHEPC, NCBITaxon:319224), UniProtKB:A0ABX8XC47 (ccmE,
  A0ABX8XC47_SHEPU, UP000827084)]; cyma_dehydrogenase: [UniProtKB:A0ABX8XAW9 (cymA,
  A0ABX8XAW9_SHEPU, UP000827084)]; mtrc_reductase: [UniProtKB:A0ABX8XFE6 (K3G22_06995,
  A0ABX8XFE6_SHEPU, UP000827084)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
  support levels and experimental caveats from oloughlin_2019: O''Loughlin EJ, Gorski
  CA, Flynn TM and Scherer MM (2019). Electron Donor Utilization and Secondary Mineral
  Formation during the Bioreduction of Lepidocrocite by Shewanella putrefaciens CN32.
  Minerals 9:434. DOI 10.3390/min9070434. Original complete publisher PDF and OSTI
  1560537 copy: Sections 2.1-2.3 and 3.1-3.3, Tables 1-3, Figures 1-6, Discussion.
  The 29-page OSTI copy preserves the full-width Table 1 cropped in the 30-page publisher
  copy. (https://doi.org/10.3390/min9070434). Live-verified UniProtKB grounding across
  UniProtKB:A4YBV6 (CCME_SHEPC, Cytochrome c-type biogenesis protein CcmE, gene_symbol:
  ccmE, SWISS_PROT, NCBITaxon:319224 Shewanella putrefaciens CN-32); UniProtKB:A0ABX8XC47
  (A0ABX8XC47_SHEPU, Cytochrome c-type biogenesis protein CcmE, gene_symbol: ccmE,
  TREMBL, NCBITaxon:24 Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XAW9
  (A0ABX8XAW9_SHEPU, Cytochrome c-type protein, gene_symbol: cymA, TREMBL, NCBITaxon:24
  Shewanella putrefaciens, UP000827084); UniProtKB:A0ABX8XFE6 (A0ABX8XFE6_SHEPU, OmcA/MtrC
  family decaheme c-type cytochrome, gene_symbol: K3G22_06995, TREMBL, NCBITaxon:24
  Shewanella putrefaciens, UP000827084).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using
  scripts/curate_causal_graphs.py for cmmmech:lepidocrocite, succeeding 20261109T023800Z-lepidocrocite-cycle11-stage3-protein-examples-review.'
related_reviews: []
```
