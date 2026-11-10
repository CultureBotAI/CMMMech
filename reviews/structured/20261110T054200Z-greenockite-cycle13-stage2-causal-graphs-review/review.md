# Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Greenockite (cmmmech:greenockite)

- Review: 20261110T054200Z-greenockite-cycle13-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T05:40:00Z
- Finished UTC: 2026-11-10T05:42:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Greenockite (cmmmech:greenockite) passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795: Updated data/records/greenockite.yaml with 'x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph' (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3). Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3, Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3, Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156).

## Scope And Provenance

Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/greenockite.yaml (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795) and its canonical EDIT history sidecar (history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3, Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3, Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156)), and primary-source evidence fidelity across 'x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph' (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges).

Selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:greenockite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:greenockite | data/records/greenockite.yaml | maintained | Greenockite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:greenockite | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:greenockite | Checked 1529 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph' (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:greenockite.

Updated data/records/greenockite.yaml (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795) with causal_graphs ('x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph' (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3). Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3, Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3, Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:greenockite.

data/records/greenockite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml (SHA-256 ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601: Add x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph causal graph and ground x513_cds_formation to congeneric Thermoanaerobacter pseudethanolicus reference-proteome sulfur-metabolism enzymes (UniProtKB:B0KC13, UniProtKB:B0KCT7, UniProtKB:B0KC12)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/greenockite.yaml; Working-tree record data/records/greenockite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/greenockite.yaml (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795) with causal_graphs ('x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph' (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1007/s10295-013-1321-3; moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3) | supports | Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3, Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3, Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156). Primary mechanism source (moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml; Canonical EDIT history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml | supports | Canonical EDIT history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml (SHA-256 ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601): Add x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph causal graph and ground x513_cds_formation to congeneric Thermoanaerobacter pseudethanolicus reference-proteome sulfur-metabolism enzymes (UniProtKB:B0KC13, UniProtKB:B0KCT7, UniProtKB:B0KC12) |
| validation | data/records/greenockite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/greenockite.yaml and history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:greenockite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T054200Z-greenockite-cycle13-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Greenockite
  (cmmmech:greenockite)
started_at: '2026-11-10T05:40:00Z'
finished_at: '2026-11-10T05:42:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 2 curation of data/records/greenockite.yaml (SHA-256
    67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795) against live
    UniProtKB grounding and cited primary source (moon2013: Moon, J.-W. et al. (2013).
    Scalable economic extracellular synthesis of CdS nanostructured particles by a
    non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology
    40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials
    and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5
  state: working_tree
  inputs:
  - path: data/records/greenockite.yaml
    sha256: 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795
    role: target
  - path: history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
    sha256: ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:greenockite
  path: data/records/greenockite.yaml
  label: Greenockite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greenockite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/greenockite.yaml
    (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795) and
    its canonical EDIT history sidecar (history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:B0KC13
    (B0KC13_THEP3, Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099
    Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7
    (B0KCT7_THEP3, Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099
    Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12
    (B0KC12_THEP3, Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099
    Thermoanaerobacter pseudethanolicus (strain ATCC 33223 / 39E), UP000002156)),
    and primary-source evidence fidelity across ''x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph''
    (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges).'
  selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:greenockite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:greenockite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/greenockite.yaml
  locator: Working-tree record data/records/greenockite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Updated data/records/greenockite.yaml (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795)
    with causal_graphs (''x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph''
    (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1007/s10295-013-1321-3
  locator: 'moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis
    of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial
    Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3.
    Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table
    1. (https://doi.org/10.1007/s10295-013-1321-3)'
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3,
    Cysteine desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3,
    Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3,
    Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156). Primary mechanism source
    (moon2013: Moon, J.-W. et al. (2013). Scalable economic extracellular synthesis
    of CdS nanostructured particles by a non-pathogenic thermophile. Journal of Industrial
    Microbiology and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3.
    Complete publisher HTML, Materials and methods, Results, Figures 1–6 and Table
    1. (https://doi.org/10.1007/s10295-013-1321-3)) parameters and source-level caveats
    are strictly preserved on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
  locator: Canonical EDIT history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
    (SHA-256 ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601): Add
    x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph causal graph and
    ground x513_cds_formation to congeneric Thermoanaerobacter pseudethanolicus reference-proteome
    sulfur-metabolism enzymes (UniProtKB:B0KC13, UniProtKB:B0KCT7, UniProtKB:B0KC12)'
  snapshot_sha256: ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601
- evidence_id: validation
  kind: validation
  reference: data/records/greenockite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: data/records/greenockite.yaml and history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:greenockite
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
  - cmmmech:greenockite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph'' (mechanism_ref:
    x513_cds_formation, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/greenockite.yaml (SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795)
    with causal_graphs (''x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph''
    (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges)), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from moon2013: Moon,
    J.-W. et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured
    particles by a non-pathogenic thermophile. Journal of Industrial Microbiology
    and Biotechnology 40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher
    HTML, Materials and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3).
    Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine
    desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3,
    Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3,
    Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter
    pseudethanolicus (strain ATCC 33223 / 39E), UP000002156).'
  target_ids:
  - cmmmech:greenockite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/greenockite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/greenockite/2026-11-10T054033Z-marcin-8f65e9.yaml
    (SHA-256 ec159b0989ab1f193ed44908ab454ecc8d5402c394f655d81cf7d83150005601: Add
    x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph causal graph and
    ground x513_cds_formation to congeneric Thermoanaerobacter pseudethanolicus reference-proteome
    sulfur-metabolism enzymes (UniProtKB:B0KC13, UniProtKB:B0KCT7, UniProtKB:B0KC12))
    and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:greenockite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Greenockite (cmmmech:greenockite) passes Cycle 13 Stage 2 causal_graphs
  review (scientific_review: true) at SHA-256 67ff0ac3b6222c069d067f959ecf157858a67fc632d7a0b1c58d4135a7e29795:
  Updated data/records/greenockite.yaml with ''x513_thermophilic_sulfidogenic_greenockite_cds_formation_graph''
  (mechanism_ref: x513_cds_formation, 4 nodes / 3 edges), achieving 100% parity between
  mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving
  source-faithful support levels and experimental caveats from moon2013: Moon, J.-W.
  et al. (2013). Scalable economic extracellular synthesis of CdS nanostructured particles
  by a non-pathogenic thermophile. Journal of Industrial Microbiology and Biotechnology
  40(11):1263–1271. DOI 10.1007/s10295-013-1321-3. Complete publisher HTML, Materials
  and methods, Results, Figures 1–6 and Table 1. (https://doi.org/10.1007/s10295-013-1321-3).
  Live-verified UniProtKB grounding across UniProtKB:B0KC13 (B0KC13_THEP3, Cysteine
  desulfurase IscS, gene_symbol: iscS, TREMBL, NCBITaxon:340099 Thermoanaerobacter
  pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KCT7 (B0KCT7_THEP3,
  Cysteine desulfurase, gene_symbol: Teth39_1911, TREMBL, NCBITaxon:340099 Thermoanaerobacter
  pseudethanolicus (strain ATCC 33223 / 39E), UP000002156); UniProtKB:B0KC12 (B0KC12_THEP3,
  Cysteine synthase, gene_symbol: Teth39_0279, TREMBL, NCBITaxon:340099 Thermoanaerobacter
  pseudethanolicus (strain ATCC 33223 / 39E), UP000002156).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:greenockite.
related_reviews: []
```
