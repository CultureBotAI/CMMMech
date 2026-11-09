# Cycle 11 Stage 3 Issue #964 remediation review of Illite group (cmmmech:illite)

- Review: 20261109T032700Z-illite-cycle11-stage3-issue964-remediation-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T03:23:00Z
- Finished UTC: 2026-11-09T03:27:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Illite group (cmmmech:illite) passes Cycle 11 Stage 3 Issue #964 remediation review (scientific_review: true) at SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6: Remediated data/records/illite.yaml with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and experimental caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278).

## Scope And Provenance

Cycle 11 Stage 3 Issue #964 remediation review of data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6) and its canonical EDIT history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml, history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml) verifying live UniProtKB protein grounding, source-faithful evidence explanations, reference-proteome and Swiss-Prot parity, and causal-edge descriptions across causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]).

Selection: Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:illite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f622889fbaf868e6f444fa93e4ce9790d45a9514.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:illite | data/records/illite.yaml | maintained | Illite group |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:illite | Checked 698 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:illite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of remediated UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)])

graph: supported. Targets: cmmmech:illite.

Remediated data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6) under Issue #964 with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful support levels and caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:illite.

data/records/illite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506: Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77 (Cycle 11 Stage 3).); history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml (SHA-256 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9: Restore causal_graphs[0].edges[1].description (mtrc_reductase -&gt; imt1_illite_substrate) and fix UniProtKB:Q8E8S0 evidence explanation and NCBITaxon:211586 label in illite.yaml (Issue #964).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/illite.yaml; Working-tree record data/records/illite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated and remediated data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6) with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving strictly entry-specific, source-faithful explanations and caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2022.980078; jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078) | supports | Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278). Primary mechanism source (jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml; Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml | supports | Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506): Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77 (Cycle 11 Stage 3). |
| edit_history_2 | history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml; Canonical EDIT history sidecar history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml | supports | Canonical EDIT history sidecar history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml (SHA-256 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9): Restore causal_graphs[0].edges[1].description (mtrc_reductase -&gt; imt1_illite_substrate) and fix UniProtKB:Q8E8S0 evidence explanation and NCBITaxon:211586 label in illite.yaml (Issue #964). |
| validation | data/records/illite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/illite.yaml and history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml, history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using scripts/curate_causal_graphs.py for cmmmech:illite, succeeding 20261109T023800Z-illite-cycle11-stage3-protein-examples-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T032700Z-illite-cycle11-stage3-issue964-remediation-review
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 11 Stage 3 Issue #964 remediation review of Illite group (cmmmech:illite)'
started_at: '2026-11-09T03:23:00Z'
finished_at: '2026-11-09T03:27:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 Issue #964 remediated UniProtKB ProteinExample
    curation in data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6)
    against live UniProtKB REST API grounding and cited primary source (jung_2022:
    Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral
    weathering and bioavailable Fe source under low-temperature conditions. Frontiers
    in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete
    ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f622889fbaf868e6f444fa93e4ce9790d45a9514
  state: working_tree
  inputs:
  - path: data/records/illite.yaml
    sha256: 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6
    role: target
  - path: history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    sha256: 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506
    role: context
  - path: history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
    sha256: 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:illite
  path: data/records/illite.yaml
  label: Illite group
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/illite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
    role: canonical_history
scope:
  description: 'Cycle 11 Stage 3 Issue #964 remediation review of data/records/illite.yaml
    (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6) and
    its canonical EDIT history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml,
    history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml) verifying live UniProtKB
    protein grounding, source-faithful evidence explanations, reference-proteome and
    Swiss-Prot parity, and causal-edge descriptions across causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
    (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]).'
  selection: 'Cycle 11 Stage 3 Issue #964 protein_examples remediation for cmmmech:illite'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:illite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/illite.yaml
  locator: Working-tree record data/records/illite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Curated and remediated data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6)
    with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph'' (mechanism_ref:
    cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving strictly entry-specific,
    source-faithful explanations and caveats.'
  snapshot_sha256: 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2022.980078
  locator: 'jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver
    of clay mineral weathering and bioavailable Fe source under low-temperature conditions.
    Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888.
    Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)'
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM,
    Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738
    Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type
    cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis
    MR-1, UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme
    c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella
    vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family
    decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738
    Shewanella vesiculosa, UP001477278). Primary mechanism source (jung_2022: Jung,
    Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering
    and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology
    13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page
    original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078))
    parameters, analytical denominators, and source-level caveats are strictly preserved
    on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
  locator: Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506): Add
    live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome
    CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to
    illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77
    (Cycle 11 Stage 3).'
  snapshot_sha256: 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
  locator: Canonical EDIT history sidecar history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
    (SHA-256 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9): Restore
    causal_graphs[0].edges[1].description (mtrc_reductase -> imt1_illite_substrate)
    and fix UniProtKB:Q8E8S0 evidence explanation and NCBITaxon:211586 label in illite.yaml
    (Issue #964).'
  snapshot_sha256: 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9
- evidence_id: validation
  kind: validation
  reference: data/records/illite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T03:27:00Z'
  support: supports
  summary: data/records/illite.yaml and history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml,
    history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml pass strict LinkML
    schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 698 record(s); 0 failed.
  target_ids:
  - cmmmech:illite
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
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_graph_parity
  area: graph
  topic: 'Verification of remediated UniProtKB protein_examples grounding and causal-graph
    parity across causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
    (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)])'
  outcome: supported
  summary: 'Remediated data/records/illite.yaml (SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6)
    under Issue #964 with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
    (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
    support levels and caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim
    (2022). A microbial driver of clay mineral weathering and bioavailable Fe source
    under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078;
    PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables
    1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding
    across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol:
    ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0
    (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT,
    NCBITaxon:211586 Shewanella oneidensis MR-1, UP000008186); UniProtKB:A0ABV0FV81
    (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495,
    TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6
    (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500,
    TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278).'
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/illite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506: Add
    live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome
    CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to
    illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77
    (Cycle 11 Stage 3).); history/records/illite/2026-11-09T032622Z-marcin-ac3b65.yaml
    (SHA-256 6e3ccce6eef5eb5e0080ef61cf1c9aef9aa1c194a080705f51f059878ff34ed9: Restore
    causal_graphs[0].edges[1].description (mtrc_reductase -> imt1_illite_substrate)
    and fix UniProtKB:Q8E8S0 evidence explanation and NCBITaxon:211586 label in illite.yaml
    (Issue #964).)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Illite group (cmmmech:illite) passes Cycle 11 Stage 3 Issue #964 remediation
  review (scientific_review: true) at SHA-256 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6:
  Remediated data/records/illite.yaml with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
  (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
  (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
  UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
  UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
  UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving entry-specific, source-faithful
  support levels and experimental caveats from jung_2022: Jung, Chung, Ko, Moon, Suh
  and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe
  source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI
  10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods
  pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078).
  Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM,
  Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella
  vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome
  CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis MR-1,
  UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme
  c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella
  vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family
  decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738
  Shewanella vesiculosa, UP001477278).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 11 Stage 3 (protein_examples) Issue #964 remediation using
  scripts/curate_causal_graphs.py for cmmmech:illite, succeeding 20261109T023800Z-illite-cycle11-stage3-protein-examples-review.'
related_reviews: []
```
