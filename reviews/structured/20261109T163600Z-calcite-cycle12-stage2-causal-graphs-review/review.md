# Cycle 12 Stage 2 causal-graphs review of Calcite (cmmmech:calcite)

- Review: 20261109T163600Z-calcite-cycle12-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T16:15:00Z
- Finished UTC: 2026-11-09T16:36:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Calcite (cmmmech:calcite) passes Cycle 12 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e: Curated data/records/calcite.yaml with causal_graph 'dw018_calcite_in_terbium_assay_graph' (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731). Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769).

## Scope And Provenance

Cycle 12 Stage 2 causal-graphs review of data/records/calcite.yaml (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e) and its canonical EDIT history sidecar(s) (history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source evidence fidelity across causal_graph 'dw018_calcite_in_terbium_assay_graph' (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]).

Selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:calcite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7449fa912e2d92f8aff400481ee75b49edbb685e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:calcite | Checked 703 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:calcite | Checked 1484 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across causal_graph 'dw018_calcite_in_terbium_assay_graph' (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)])

graph: supported. Targets: cmmmech:calcite.

Curated data/records/calcite.yaml (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e) with causal_graph 'dw018_calcite_in_terbium_assay_graph' (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731). Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:calcite.

data/records/calcite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml (SHA-256 c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897: Add dw018_calcite_in_terbium_assay_graph causal graph and ground dw018_calcite_in_terbium_assay to Lysinibacillus reference-proteome UreABC subunits (UniProtKB:A0ACG7VEY6, UniProtKB:A0ACG7VDY8, UniProtKB:A0ACG7VDH1))) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/calcite.yaml; Working-tree record data/records/calcite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/calcite.yaml (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e) with causal_graph 'dw018_calcite_in_terbium_assay_graph' (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2024.1416731; bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731) | supports | Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769); UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769). Primary mechanism source (bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml; Canonical EDIT history sidecar history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml | supports | Canonical EDIT history sidecar history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml (SHA-256 c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897): Add dw018_calcite_in_terbium_assay_graph causal graph and ground dw018_calcite_in_terbium_assay to Lysinibacillus reference-proteome UreABC subunits (UniProtKB:A0ACG7VEY6, UniProtKB:A0ACG7VDY8, UniProtKB:A0ACG7VDH1) |
| validation | data/records/calcite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/calcite.yaml and history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:calcite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T163600Z-calcite-cycle12-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 2 causal-graphs review of Calcite (cmmmech:calcite)
started_at: '2026-11-09T16:15:00Z'
finished_at: '2026-11-09T16:36:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 12 Stage 2 causal_graphs and ProteinExample curation in data/records/calcite.yaml
    (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e) against
    live UniProtKB grounding and cited primary source (bian2024: Bian, Dong, Ning,
    Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018 isolated from
    ionic rare earth tailings based on microbial induced calcium carbonate precipitation.
    Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures
    1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 7449fa912e2d92f8aff400481ee75b49edbb685e
  state: working_tree
  inputs:
  - path: data/records/calcite.yaml
    sha256: 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e
    role: target
  - path: history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
    sha256: c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:calcite
  path: data/records/calcite.yaml
  label: Calcite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
    role: canonical_history
scope:
  description: 'Cycle 12 Stage 2 causal-graphs review of data/records/calcite.yaml
    (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e) and
    its canonical EDIT history sidecar(s) (history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source
    evidence fidelity across causal_graph ''dw018_calcite_in_terbium_assay_graph''
    (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex:
    [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8
    (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI,
    UP000318769)]).'
  selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:calcite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:calcite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/calcite.yaml
  locator: Working-tree record data/records/calcite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Curated data/records/calcite.yaml (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e)
    with causal_graph ''dw018_calcite_in_terbium_assay_graph'' (mechanism_ref: dw018_calcite_in_terbium_assay,
    4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC,
    A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI,
    UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1416731
  locator: 'bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by
    Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial
    induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731.
    Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731)'
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI,
    Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus
    fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit
    beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769);
    UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA,
    TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769). Primary mechanism
    source (bian2024: Bian, Dong, Ning, Song and Hu (2024). Recovery of terbium by
    Lysinibacillus sp. DW018 isolated from ionic rare earth tailings based on microbial
    induced calcium carbonate precipitation. Frontiers in Microbiology 15:1416731.
    Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731))
    parameters, analytical denominators, and source-level caveats are strictly preserved
    on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
  locator: Canonical EDIT history sidecar history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
    (SHA-256 c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897): Add
    dw018_calcite_in_terbium_assay_graph causal graph and ground dw018_calcite_in_terbium_assay
    to Lysinibacillus reference-proteome UreABC subunits (UniProtKB:A0ACG7VEY6, UniProtKB:A0ACG7VDY8,
    UniProtKB:A0ACG7VDH1)'
  snapshot_sha256: c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897
- evidence_id: validation
  kind: validation
  reference: data/records/calcite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: data/records/calcite.yaml and history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 703 record(s); 0 failed.
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1484 history record(s); 0 error(s).
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across causal_graph ''dw018_calcite_in_terbium_assay_graph'' (mechanism_ref: dw018_calcite_in_terbium_assay,
    4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC,
    A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI,
    UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)])'
  outcome: supported
  summary: 'Curated data/records/calcite.yaml (SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e)
    with causal_graph ''dw018_calcite_in_terbium_assay_graph'' (mechanism_ref: dw018_calcite_in_terbium_assay,
    4 nodes / 3 edges; lysinibacillus_ureabc_complex: [UniProtKB:A0ACG7VEY6 (ureC,
    A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8 (ureB, A0ACG7VDY8_9BACI,
    UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI, UP000318769)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from bian2024: Bian,
    Dong, Ning, Song and Hu (2024). Recovery of terbium by Lysinibacillus sp. DW018
    isolated from ionic rare earth tailings based on microbial induced calcium carbonate
    precipitation. Frontiers in Microbiology 15:1416731. Sections 2.1-2.9, 3.2-3.5
    and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731).
    Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI,
    Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus
    fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit
    beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769);
    UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA,
    TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769).'
  target_ids:
  - cmmmech:calcite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/calcite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/calcite/2026-11-09T161813Z-marcin-9b2ff3.yaml
    (SHA-256 c09b49b1df37ea9f61e6bd6a493869aee9dc4c5a48d18ecac4bb992caf3ac897: Add
    dw018_calcite_in_terbium_assay_graph causal graph and ground dw018_calcite_in_terbium_assay
    to Lysinibacillus reference-proteome UreABC subunits (UniProtKB:A0ACG7VEY6, UniProtKB:A0ACG7VDY8,
    UniProtKB:A0ACG7VDH1))) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:calcite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Calcite (cmmmech:calcite) passes Cycle 12 Stage 2 causal-graphs review (scientific_review:
  true) at SHA-256 5cac274467036e9050d12d5295f8e16aa2d6c50aa2b92d1e388455d9eab1a56e:
  Curated data/records/calcite.yaml with causal_graph ''dw018_calcite_in_terbium_assay_graph''
  (mechanism_ref: dw018_calcite_in_terbium_assay, 4 nodes / 3 edges; lysinibacillus_ureabc_complex:
  [UniProtKB:A0ACG7VEY6 (ureC, A0ACG7VEY6_9BACI, UP000318769), UniProtKB:A0ACG7VDY8
  (ureB, A0ACG7VDY8_9BACI, UP000318769), UniProtKB:A0ACG7VDH1 (ureA, A0ACG7VDH1_9BACI,
  UP000318769)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from bian2024: Bian, Dong, Ning, Song and Hu (2024).
  Recovery of terbium by Lysinibacillus sp. DW018 isolated from ionic rare earth tailings
  based on microbial induced calcium carbonate precipitation. Frontiers in Microbiology
  15:1416731. Sections 2.1-2.9, 3.2-3.5 and 4; Figures 1-10, Tables 1-2. (https://doi.org/10.3389/fmicb.2024.1416731).
  Live-verified UniProtKB grounding across UniProtKB:A0ACG7VEY6 (A0ACG7VEY6_9BACI,
  Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:28031 Lysinibacillus
  fusiformis, UP000318769); UniProtKB:A0ACG7VDY8 (A0ACG7VDY8_9BACI, Urease subunit
  beta, gene_symbol: ureB, TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769);
  UniProtKB:A0ACG7VDH1 (A0ACG7VDH1_9BACI, Urease subunit gamma, gene_symbol: ureA,
  TREMBL, NCBITaxon:28031 Lysinibacillus fusiformis, UP000318769).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:calcite.
related_reviews: []
```
