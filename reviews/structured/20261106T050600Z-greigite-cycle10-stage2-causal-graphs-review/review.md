# Cycle 10 Stage 2 causal-graphs review of Greigite (cmmmech:greigite)

- Review: 20261106T050600Z-greigite-cycle10-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-06T05:05:30Z
- Finished UTC: 2026-11-06T05:06:00Z
- Reviewer: antigravity / cmmmech-cycle10-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Greigite (cmmmech:greigite) passes Cycle 10 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122: Curated data/records/greigite.yaml with causal_graph 'kod1_sulfur_source_comparison_graph' (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from gorlas2022: Gorlas et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915). Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4 (NSR_THEKO, NAD(P)H sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299, SWISS_PROT, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3 (A0ACM8PXE3_THEKO, Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3 (Q8NKS3_THEKO, Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4 (Q8NKS4_THEKO, Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5 (Q8NKS5_THEKO, Cytosolic NiFe-hydrogenase, beta subunit, gene_symbol: TK2072, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4 (Q5JIL4_THEKO, Membrane bound hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol: TK2090, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536).

## Scope And Provenance

Cycle 10 Stage 2 causal-graphs review of data/records/greigite.yaml (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122) and its canonical EDIT history sidecar(s) (history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml, history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'kod1_sulfur_source_comparison_graph' (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]).

Selection: Cycle 10 Stage 2 causal_graphs curation for cmmmech:greigite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0fbb411bcb9bba9d4871d7791d5a13ebc4b50723.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:greigite | data/records/greigite.yaml | maintained | Greigite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:greigite | Checked 693 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:greigite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB reference-proteome grounding, and parity across causal_graph 'kod1_sulfur_source_comparison_graph' (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)])

graph: supported. Targets: cmmmech:greigite.

Curated data/records/greigite.yaml (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122) with causal_graph 'kod1_sulfur_source_comparison_graph' (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from gorlas2022: Gorlas et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915). Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4 (NSR_THEKO, NAD(P)H sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299, SWISS_PROT, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3 (A0ACM8PXE3_THEKO, Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3 (Q8NKS3_THEKO, Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4 (Q8NKS4_THEKO, Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5 (Q8NKS5_THEKO, Cytosolic NiFe-hydrogenase, beta subunit, gene_symbol: TK2072, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4 (Q5JIL4_THEKO, Membrane bound hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol: TK2090, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:greigite.

data/records/greigite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml (SHA-256 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0): Add evidence-backed causal_graphs representation and 7 live-verified Thermococcus kodakarensis KOD1 (NCBITaxon:69014; UP000000536) protein groundings (Swiss-Prot NSR TK1299 UniProtKB:Q5JGP4 and sulfhydrogenase/MBH subunits UniProtKB:A0ACM8PXE3, UniProtKB:Q8NKS2, UniProtKB:Q8NKS3, UniProtKB:Q8NKS4, UniProtKB:Q8NKS5, UniProtKB:Q5JIL4) for kod1_sulfur_source_comparison.; history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml (SHA-256 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718): Remove redundant unannotated-proteome TrEMBL entry UniProtKB:Q8NKS2 (hydA, duplicating UP000000536 entry UniProtKB:A0ACM8PXE3 TK2069) from greigite.yaml, retaining the 6 reference-proteome UP000000536 groundings (Issue #947).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/greigite.yaml; Working-tree record data/records/greigite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/greigite.yaml (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122) with causal_graph 'kod1_sulfur_source_comparison_graph' (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1111/1462-2920.15915; gorlas2022: Gorlas et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4 (NSR_THEKO, NAD(P)H sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299, SWISS_PROT, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3 (A0ACM8PXE3_THEKO, Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3 (Q8NKS3_THEKO, Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4 (Q8NKS4_THEKO, Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5 (Q8NKS5_THEKO, Cytosolic NiFe-hydrogenase, beta subunit, gene_symbol: TK2072, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4 (Q5JIL4_THEKO, Membrane bound hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol: TK2090, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536). Primary mechanism source(s) (gorlas2022: Gorlas et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915)) report culture-level mineralization, biosorption, or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml; Canonical EDIT history sidecar history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml | supports | Canonical EDIT history sidecar history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml (SHA-256 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0): Add evidence-backed causal_graphs representation and 7 live-verified Thermococcus kodakarensis KOD1 (NCBITaxon:69014; UP000000536) protein groundings (Swiss-Prot NSR TK1299 UniProtKB:Q5JGP4 and sulfhydrogenase/MBH subunits UniProtKB:A0ACM8PXE3, UniProtKB:Q8NKS2, UniProtKB:Q8NKS3, UniProtKB:Q8NKS4, UniProtKB:Q8NKS5, UniProtKB:Q5JIL4) for kod1_sulfur_source_comparison. |
| edit_history_2 | history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml; Canonical EDIT history sidecar history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml | supports | Canonical EDIT history sidecar history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml (SHA-256 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718): Remove redundant unannotated-proteome TrEMBL entry UniProtKB:Q8NKS2 (hydA, duplicating UP000000536 entry UniProtKB:A0ACM8PXE3 TK2069) from greigite.yaml, retaining the 6 reference-proteome UP000000536 groundings (Issue #947). |
| validation | data/records/greigite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/greigite.yaml and history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml, history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 10 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:greigite (including Issue #947 review-remediation updates).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T050600Z-greigite-cycle10-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 10 Stage 2 causal-graphs review of Greigite (cmmmech:greigite)
started_at: '2026-11-06T05:05:30Z'
finished_at: '2026-11-06T05:06:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle10-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 10 Stage 2 causal_graphs and ProteinExample curation in data/records/greigite.yaml
    (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122) against
    live UniProtKB reference-proteome grounding and cited primary source(s) (gorlas2022:
    Gorlas et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales
    - an advantage to live in Fe- and S-rich environments? Environmental Microbiology
    24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary
    Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 0fbb411bcb9bba9d4871d7791d5a13ebc4b50723
  state: working_tree
  inputs:
  - path: data/records/greigite.yaml
    sha256: 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122
    role: target
  - path: history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
    sha256: 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0
    role: context
  - path: history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
    sha256: 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:greigite
  path: data/records/greigite.yaml
  label: Greigite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
    role: canonical_history
scope:
  description: 'Cycle 10 Stage 2 causal-graphs review of data/records/greigite.yaml
    (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122) and
    its canonical EDIT history sidecar(s) (history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml,
    history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml) verifying causal-graph
    node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''kod1_sulfur_source_comparison_graph''
    (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase:
    [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex:
    [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3
    (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536),
    UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090,
    Q5JIL4_THEKO, UP000000536)]).'
  selection: Cycle 10 Stage 2 causal_graphs curation for cmmmech:greigite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:greigite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/greigite.yaml
  locator: Working-tree record data/records/greigite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Curated data/records/greigite.yaml (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122)
    with causal_graph ''kod1_sulfur_source_comparison_graph'' (mechanism_ref: kod1_sulfur_source_comparison,
    4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299,
    NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3
    (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO,
    UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5
    (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1111/1462-2920.15915
  locator: 'gorlas2022: Gorlas et al. (2022). Precipitation of greigite and pyrite
    induced by Thermococcales - an advantage to live in Fe- and S-rich environments?
    Environmental Microbiology 24(2), 626-642. Complete archived article, Figures
    1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915)'
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4
    (NSR_THEKO, NAD(P)H sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299,
    SWISS_PROT, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3
    (A0ACM8PXE3_THEKO, Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069,
    TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3
    (Q8NKS3_THEKO, Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070,
    TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4
    (Q8NKS4_THEKO, Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071,
    TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5
    (Q8NKS5_THEKO, Cytosolic NiFe-hydrogenase, beta subunit, gene_symbol: TK2072,
    TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4
    (Q5JIL4_THEKO, Membrane bound hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol:
    TK2090, TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536).
    Primary mechanism source(s) (gorlas2022: Gorlas et al. (2022). Precipitation of
    greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and
    S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived
    article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915))
    report culture-level mineralization, biosorption, or bioleaching without single-gene
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
  locator: Canonical EDIT history sidecar history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
    (SHA-256 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0): Add
    evidence-backed causal_graphs representation and 7 live-verified Thermococcus
    kodakarensis KOD1 (NCBITaxon:69014; UP000000536) protein groundings (Swiss-Prot
    NSR TK1299 UniProtKB:Q5JGP4 and sulfhydrogenase/MBH subunits UniProtKB:A0ACM8PXE3,
    UniProtKB:Q8NKS2, UniProtKB:Q8NKS3, UniProtKB:Q8NKS4, UniProtKB:Q8NKS5, UniProtKB:Q5JIL4)
    for kod1_sulfur_source_comparison.'
  snapshot_sha256: 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
  locator: Canonical EDIT history sidecar history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
    (SHA-256 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718): Remove
    redundant unannotated-proteome TrEMBL entry UniProtKB:Q8NKS2 (hydA, duplicating
    UP000000536 entry UniProtKB:A0ACM8PXE3 TK2069) from greigite.yaml, retaining the
    6 reference-proteome UP000000536 groundings (Issue #947).'
  snapshot_sha256: 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718
- evidence_id: validation
  kind: validation
  reference: data/records/greigite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: data/records/greigite.yaml and history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml,
    history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml pass strict LinkML
    schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 693 record(s); 0 failed.
  target_ids:
  - cmmmech:greigite
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
  - cmmmech:greigite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB reference-proteome grounding,
    and parity across causal_graph ''kod1_sulfur_source_comparison_graph'' (mechanism_ref:
    kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase:
    [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex:
    [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3
    (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536),
    UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090,
    Q5JIL4_THEKO, UP000000536)])'
  outcome: supported
  summary: 'Curated data/records/greigite.yaml (SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122)
    with causal_graph ''kod1_sulfur_source_comparison_graph'' (mechanism_ref: kod1_sulfur_source_comparison,
    4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase: [UniProtKB:Q5JGP4 (TK1299,
    NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex: [UniProtKB:A0ACM8PXE3
    (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3 (TK2070, Q8NKS3_THEKO,
    UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536), UniProtKB:Q8NKS5
    (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090, Q5JIL4_THEKO, UP000000536)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from gorlas2022: Gorlas
    et al. (2022). Precipitation of greigite and pyrite induced by Thermococcales
    - an advantage to live in Fe- and S-rich environments? Environmental Microbiology
    24(2), 626-642. Complete archived article, Figures 1-6, Table 1, supplementary
    Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915). Live-verified
    UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4 (NSR_THEKO, NAD(P)H
    sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299, SWISS_PROT, NCBITaxon:69014
    Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3 (A0ACM8PXE3_THEKO,
    Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069, TREMBL, NCBITaxon:69014
    Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3 (Q8NKS3_THEKO,
    Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070, TREMBL, NCBITaxon:69014
    Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4 (Q8NKS4_THEKO,
    Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071, TREMBL, NCBITaxon:69014
    Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5 (Q8NKS5_THEKO,
    Cytosolic NiFe-hydrogenase, beta subunit, gene_symbol: TK2072, TREMBL, NCBITaxon:69014
    Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4 (Q5JIL4_THEKO,
    Membrane bound hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol: TK2090,
    TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536).'
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/greigite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/greigite/2026-11-06T050407Z-marcin-e33eed.yaml
    (SHA-256 03994f964bb2d8f365ab1ebb6b6767741aceb02d02640c5f33d98428e44525c0): Add
    evidence-backed causal_graphs representation and 7 live-verified Thermococcus
    kodakarensis KOD1 (NCBITaxon:69014; UP000000536) protein groundings (Swiss-Prot
    NSR TK1299 UniProtKB:Q5JGP4 and sulfhydrogenase/MBH subunits UniProtKB:A0ACM8PXE3,
    UniProtKB:Q8NKS2, UniProtKB:Q8NKS3, UniProtKB:Q8NKS4, UniProtKB:Q8NKS5, UniProtKB:Q5JIL4)
    for kod1_sulfur_source_comparison.; history/records/greigite/2026-11-06T062133Z-marcin-8fefe2.yaml
    (SHA-256 178222db997f6370dfcb7f5d17e11eb322634cc7605fda99cc528fb295a84718): Remove
    redundant unannotated-proteome TrEMBL entry UniProtKB:Q8NKS2 (hydA, duplicating
    UP000000536 entry UniProtKB:A0ACM8PXE3 TK2069) from greigite.yaml, retaining the
    6 reference-proteome UP000000536 groundings (Issue #947).) and passing all LinkML
    and history validation gates.'
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Greigite (cmmmech:greigite) passes Cycle 10 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 936045e5c8683db7695806e8b9bf45e7d6f9af1c845245a082a52d6d8accc122:
  Curated data/records/greigite.yaml with causal_graph ''kod1_sulfur_source_comparison_graph''
  (mechanism_ref: kod1_sulfur_source_comparison, 4 nodes / 3 edges; kod1_nsr_sulfur_oxidoreductase:
  [UniProtKB:Q5JGP4 (TK1299, NSR_THEKO, UP000000536)]; kod1_sulfhydrogenase_and_mbh_complex:
  [UniProtKB:A0ACM8PXE3 (TK2069, A0ACM8PXE3_THEKO, UP000000536), UniProtKB:Q8NKS3
  (TK2070, Q8NKS3_THEKO, UP000000536), UniProtKB:Q8NKS4 (TK2071, Q8NKS4_THEKO, UP000000536),
  UniProtKB:Q8NKS5 (TK2072, Q8NKS5_THEKO, UP000000536), UniProtKB:Q5JIL4 (TK2090,
  Q5JIL4_THEKO, UP000000536)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from gorlas2022: Gorlas et al. (2022). Precipitation
  of greigite and pyrite induced by Thermococcales - an advantage to live in Fe- and
  S-rich environments? Environmental Microbiology 24(2), 626-642. Complete archived
  article, Figures 1-6, Table 1, supplementary Figures S1-S8 and Appendix S1. (https://doi.org/10.1111/1462-2920.15915).
  Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q5JGP4 (NSR_THEKO,
  NAD(P)H sulfur oxidoreductase (CoA-dependent), gene_symbol: TK1299, SWISS_PROT,
  NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:A0ACM8PXE3
  (A0ACM8PXE3_THEKO, Cytosolic NiFe-hydrogenase, alpha subunit, gene_symbol: TK2069,
  TREMBL, NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS3
  (Q8NKS3_THEKO, Cytosolic NiFe-hydrogenase, delta subunit, gene_symbol: TK2070, TREMBL,
  NCBITaxon:69014 Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS4 (Q8NKS4_THEKO,
  Cytosolic NiFe-hydrogenase, gamma subunit, gene_symbol: TK2071, TREMBL, NCBITaxon:69014
  Thermococcus kodakarensis KOD1, UP000000536); UniProtKB:Q8NKS5 (Q8NKS5_THEKO, Cytosolic
  NiFe-hydrogenase, beta subunit, gene_symbol: TK2072, TREMBL, NCBITaxon:69014 Thermococcus
  kodakarensis KOD1, UP000000536); UniProtKB:Q5JIL4 (Q5JIL4_THEKO, Membrane bound
  hydrogenase, NiFe-hydrogenase large subunit 1, gene_symbol: TK2090, TREMBL, NCBITaxon:69014
  Thermococcus kodakarensis KOD1, UP000000536).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 10 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:greigite (including Issue #947 review-remediation updates).'
related_reviews: []
```
