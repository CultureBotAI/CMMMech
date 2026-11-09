# Cycle 11 Stage 3 protein-examples review of Illite group (cmmmech:illite)

- Review: 20261109T023800Z-illite-cycle11-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T02:35:00Z
- Finished UTC: 2026-11-09T02:38:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Illite group (cmmmech:illite) passes Cycle 11 Stage 3 protein-examples review (scientific_review: true) at SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b: Curated data/records/illite.yaml with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278).

## Scope And Provenance

Cycle 11 Stage 3 protein-examples review of data/records/illite.yaml (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b) and its canonical EDIT history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml) verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot parity, and primary-source evidence fidelity across causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]).

Selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:illite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base df061de720fb9884dcc6e41369a3049cef52a059.
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

### Verification of UniProtKB protein_examples grounding and causal-graph parity across causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)])

graph: supported. Targets: cmmmech:illite.

Curated data/records/illite.yaml (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b) with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:illite.

data/records/illite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506: Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77 (Cycle 11 Stage 3).)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/illite.yaml; Working-tree record data/records/illite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Curated data/records/illite.yaml (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b) with causal_graph 'shewanella_vesiculosa_imt1_illite_reduction_graph' (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77 (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON, UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM, UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM, UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2022.980078; jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078) | supports | Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278). Primary mechanism source (jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml; Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml | supports | Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506): Add live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77 (Cycle 11 Stage 3). |
| validation | data/records/illite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/illite.yaml and history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py for cmmmech:illite following 20261109T004500Z-illite-cycle11-stage2-causal-graphs-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T023800Z-illite-cycle11-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 11 Stage 3 protein-examples review of Illite group (cmmmech:illite)
started_at: '2026-11-09T02:35:00Z'
finished_at: '2026-11-09T02:38:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 11 Stage 3 UniProtKB ProteinExample curation in data/records/illite.yaml
    (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b) against
    live UniProtKB REST API grounding and cited primary source (jung_2022: Jung, Chung,
    Ko, Moon, Suh and Kim (2022). A microbial driver of clay mineral weathering and
    bioavailable Fe source under low-temperature conditions. Frontiers in Microbiology
    13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888. Complete ten-page
    original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: df061de720fb9884dcc6e41369a3049cef52a059
  state: working_tree
  inputs:
  - path: data/records/illite.yaml
    sha256: 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b
    role: target
  - path: history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    sha256: 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506
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
scope:
  description: 'Cycle 11 Stage 3 protein-examples review of data/records/illite.yaml
    (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b) and
    its canonical EDIT history sidecar(s) (history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml)
    verifying live UniProtKB protein grounding, reference-proteome and Swiss-Prot
    parity, and primary-source evidence fidelity across causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
    (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]).'
  selection: Cycle 11 Stage 3 protein_examples curation for cmmmech:illite
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
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Curated data/records/illite.yaml (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b)
    with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph'' (mechanism_ref:
    cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2022.980078
  locator: 'jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022). A microbial driver
    of clay mineral weathering and bioavailable Fe source under low-temperature conditions.
    Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078; PMCID PMC9441888.
    Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables 1-2. (https://doi.org/10.3389/fmicb.2022.980078)'
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM,
    Cytochrome c-type protein, gene_symbol: ABHN84_13755, TREMBL, NCBITaxon:518738
    Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0 (CYMA_SHEON, Tetraheme c-type
    cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586 Shewanella oneidensis
    (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1),
    UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC family decaheme
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
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    (SHA-256 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506): Add
    live-verified reviewed Swiss-Prot Shewanella oneidensis MR-1 reference-proteome
    CymA (UniProtKB:Q8E8S0, CYMA_SHEON, SO_4591, UP000008186, NCBITaxon:211586) to
    illite.yaml (cold_imt1_reduction) alongside S. vesiculosa UP001477278 UniProtKB:A0ABV0FR77
    (Cycle 11 Stage 3).'
  snapshot_sha256: 4ac574831003cf42e87a355294d26c42209cbe421f3b2fc8c43f685188892506
- evidence_id: validation
  kind: validation
  reference: data/records/illite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T02:38:00Z'
  support: supports
  summary: data/records/illite.yaml and history/records/illite/2026-11-09T023713Z-marcin-85dcdb.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b
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
  topic: 'Verification of UniProtKB protein_examples grounding and causal-graph parity
    across causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph'' (mechanism_ref:
    cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)])'
  outcome: supported
  summary: 'Curated data/records/illite.yaml (SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b)
    with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph'' (mechanism_ref:
    cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
    (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
    UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
    UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
    UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim (2022).
    A microbial driver of clay mineral weathering and bioavailable Fe source under
    low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078;
    PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables
    1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding
    across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol:
    ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0
    (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT,
    NCBITaxon:211586 Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686
    / LMG 19005 / NCIMB 14063 / MR-1), UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM,
    OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL,
    NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM,
    OmcA/MtrC family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL,
    NCBITaxon:518738 Shewanella vesiculosa, UP001477278).'
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
    (Cycle 11 Stage 3).)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Illite group (cmmmech:illite) passes Cycle 11 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 08e3271db8471eea6c3f0f175113dec1de16dcb308cdfc80cfde94668591cd5b:
  Curated data/records/illite.yaml with causal_graph ''shewanella_vesiculosa_imt1_illite_reduction_graph''
  (mechanism_ref: cold_imt1_reduction, 5 nodes / 4 edges; cyma_dehydrogenase: [UniProtKB:A0ABV0FR77
  (ABHN84_13755, A0ABV0FR77_9GAMM, UP001477278), UniProtKB:Q8E8S0 (cymA, CYMA_SHEON,
  UP000008186)]; mtrc_reductase: [UniProtKB:A0ABV0FV81 (ABHN84_14495, A0ABV0FV81_9GAMM,
  UP001477278)]; omca_reductase: [UniProtKB:A0ABV0FRM6 (ABHN84_14500, A0ABV0FRM6_9GAMM,
  UP001477278)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from jung_2022: Jung, Chung, Ko, Moon, Suh and Kim
  (2022). A microbial driver of clay mineral weathering and bioavailable Fe source
  under low-temperature conditions. Frontiers in Microbiology 13:980078. DOI 10.3389/fmicb.2022.980078;
  PMCID PMC9441888. Complete ten-page original, Methods pp2-3, Figures 1-6 and Tables
  1-2. (https://doi.org/10.3389/fmicb.2022.980078). Live-verified UniProtKB grounding
  across UniProtKB:A0ABV0FR77 (A0ABV0FR77_9GAMM, Cytochrome c-type protein, gene_symbol:
  ABHN84_13755, TREMBL, NCBITaxon:518738 Shewanella vesiculosa, UP001477278); UniProtKB:Q8E8S0
  (CYMA_SHEON, Tetraheme c-type cytochrome CymA, gene_symbol: cymA, SWISS_PROT, NCBITaxon:211586
  Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 /
  NCIMB 14063 / MR-1), UP000008186); UniProtKB:A0ABV0FV81 (A0ABV0FV81_9GAMM, OmcA/MtrC
  family decaheme c-type cytochrome, gene_symbol: ABHN84_14495, TREMBL, NCBITaxon:518738
  Shewanella vesiculosa, UP001477278); UniProtKB:A0ABV0FRM6 (A0ABV0FRM6_9GAMM, OmcA/MtrC
  family decaheme c-type cytochrome, gene_symbol: ABHN84_14500, TREMBL, NCBITaxon:518738
  Shewanella vesiculosa, UP001477278).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 11 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py
  for cmmmech:illite following 20261109T004500Z-illite-cycle11-stage2-causal-graphs-review.
related_reviews: []
```
