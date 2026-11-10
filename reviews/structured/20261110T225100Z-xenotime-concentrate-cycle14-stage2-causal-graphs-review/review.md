# Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Xenotime concentrate (cmmmech:xenotime-concentrate)

- Review: 20261110T225100Z-xenotime-concentrate-cycle14-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T22:50:00Z
- Finished UTC: 2026-11-10T22:51:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Xenotime concentrate (cmmmech:xenotime-concentrate) passes Cycle 14 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12: Updated data/records/xenotime-concentrate.yaml with 'bacillus_xenotime_monazite_concentrate_bioweathering_graph' (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from he2024: He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible sources of environmental dissolved rare earth elements: Insights from experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186). Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol: mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).

## Scope And Provenance

Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/xenotime-concentrate.yaml (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12) and its canonical EDIT history sidecar (history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol: mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143)), and primary-source evidence fidelity across 'bacillus_xenotime_monazite_concentrate_bioweathering_graph' (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges).

Selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:xenotime-concentrate
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3508503d6abadd52e8bdb9dacd71ebcd26731b83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:xenotime-concentrate | data/records/xenotime-concentrate.yaml | maintained | Xenotime concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:xenotime-concentrate | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:xenotime-concentrate | Checked 1563 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'bacillus_xenotime_monazite_concentrate_bioweathering_graph' (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges)

graph: supported. Targets: cmmmech:xenotime-concentrate.

Updated data/records/xenotime-concentrate.yaml (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12) with causal_graphs ('bacillus_xenotime_monazite_concentrate_bioweathering_graph' (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from he2024: He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible sources of environmental dissolved rare earth elements: Insights from experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186). Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol: mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:xenotime-concentrate.

data/records/xenotime-concentrate.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml (SHA-256 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254: Add bacillus_xenotime_monazite_concentrate_bioweathering_graph causal graph and ground bacillus_concentrate_bioweathering to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0B5XLM5, UniProtKB:A0A0K0QJ28)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/xenotime-concentrate.yaml; Working-tree record data/records/xenotime-concentrate.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/xenotime-concentrate.yaml (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12) with causal_graphs ('bacillus_xenotime_monazite_concentrate_bioweathering_graph' (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1016/j.chemgeo.2024.122186; he2024: He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible sources of environmental dissolved rare earth elements: Insights from experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186) | supports | Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol: mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143). Primary mechanism source (he2024: He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible sources of environmental dissolved rare earth elements: Insights from experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml; Canonical EDIT history sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml | supports | Canonical EDIT history sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml (SHA-256 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254): Add bacillus_xenotime_monazite_concentrate_bioweathering_graph causal graph and ground bacillus_concentrate_bioweathering to Bacillus thuringiensis reference-proteome enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0B5XLM5, UniProtKB:A0A0K0QJ28) |
| validation | data/records/xenotime-concentrate.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/xenotime-concentrate.yaml and history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:xenotime-concentrate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T225100Z-xenotime-concentrate-cycle14-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 2 causal_graphs and UniProtKB grounding review of Xenotime concentrate
  (cmmmech:xenotime-concentrate)
started_at: '2026-11-10T22:50:00Z'
finished_at: '2026-11-10T22:51:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 2 curation of data/records/xenotime-concentrate.yaml
    (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12) against
    live UniProtKB grounding and cited primary source (he2024: He Y, Ma L, Liang X,
    Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible sources
    of environmental dissolved rare earth elements: Insights from experimental bio-weathering
    of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186;
    complete 56-page GFZ author postprint including repository cover, Figures 1-7
    and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3508503d6abadd52e8bdb9dacd71ebcd26731b83
  state: working_tree
  inputs:
  - path: data/records/xenotime-concentrate.yaml
    sha256: 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12
    role: target
  - path: history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
    sha256: 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:xenotime-concentrate
  path: data/records/xenotime-concentrate.yaml
  label: Xenotime concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 2 causal_graphs and protein_examples review of data/records/xenotime-concentrate.yaml
    (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12) and
    its canonical EDIT history sidecar (history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:A0A0K0QI82
    (A0A0K0QI82_BACTU, Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428
    Bacillus thuringiensis, UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU,
    Malate dehydrogenase, gene_symbol: mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
    UP000194143); UniProtKB:A0A0K0QJ28 (A0A0K0QJ28_BACTU, L-lactate dehydrogenase,
    gene_symbol: ldh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143)),
    and primary-source evidence fidelity across ''bacillus_xenotime_monazite_concentrate_bioweathering_graph''
    (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges).'
  selection: Cycle 14 Stage 2 causal_graphs cohort review for cmmmech:xenotime-concentrate
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:xenotime-concentrate
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/xenotime-concentrate.yaml
  locator: Working-tree record data/records/xenotime-concentrate.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Updated data/records/xenotime-concentrate.yaml (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12)
    with causal_graphs (''bacillus_xenotime_monazite_concentrate_bioweathering_graph''
    (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1016/j.chemgeo.2024.122186
  locator: 'he2024: He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare
    earth phosphates as possible sources of environmental dissolved rare earth elements:
    Insights from experimental bio-weathering of xenotime and monazite. Chemical Geology
    661:122186. DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint
    including repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186)'
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU,
    Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
    UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol:
    mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28
    (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428
    Bacillus thuringiensis, UP000194143). Primary mechanism source (he2024: He Y,
    Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as
    possible sources of environmental dissolved rare earth elements: Insights from
    experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186.
    DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including
    repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186))
    parameters and source-level caveats are strictly preserved on all nodes, edges,
    and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
  locator: Canonical EDIT history sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
    (SHA-256 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254): Add
    bacillus_xenotime_monazite_concentrate_bioweathering_graph causal graph and ground
    bacillus_concentrate_bioweathering to Bacillus thuringiensis reference-proteome
    enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0B5XLM5, UniProtKB:A0A0K0QJ28)'
  snapshot_sha256: 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254
- evidence_id: validation
  kind: validation
  reference: data/records/xenotime-concentrate.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T22:51:00Z'
  support: supports
  summary: data/records/xenotime-concentrate.yaml and history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:xenotime-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1563 history record(s); 0 error(s).
  target_ids:
  - cmmmech:xenotime-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''bacillus_xenotime_monazite_concentrate_bioweathering_graph'' (mechanism_ref:
    bacillus_concentrate_bioweathering, 6 nodes / 6 edges)'
  outcome: supported
  summary: 'Updated data/records/xenotime-concentrate.yaml (SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12)
    with causal_graphs (''bacillus_xenotime_monazite_concentrate_bioweathering_graph''
    (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from he2024: He Y, Ma
    L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates as possible
    sources of environmental dissolved rare earth elements: Insights from experimental
    bio-weathering of xenotime and monazite. Chemical Geology 661:122186. DOI 10.1016/j.chemgeo.2024.122186;
    complete 56-page GFZ author postprint including repository cover, Figures 1-7
    and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186). Live-verified
    UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU, Citrate synthase,
    gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143);
    UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol: mdh,
    TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28
    (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428
    Bacillus thuringiensis, UP000194143).'
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/xenotime-concentrate.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar history/records/xenotime-concentrate/2026-11-10T224938Z-marcin-df97f4.yaml
    (SHA-256 2bc36904ad34cf74975a824920385fa9b3d9ee4572449eb135ff76d1658d2254: Add
    bacillus_xenotime_monazite_concentrate_bioweathering_graph causal graph and ground
    bacillus_concentrate_bioweathering to Bacillus thuringiensis reference-proteome
    enzymes (UniProtKB:A0A0K0QI82, UniProtKB:A0A0B5XLM5, UniProtKB:A0A0K0QJ28)) and
    passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Xenotime concentrate (cmmmech:xenotime-concentrate) passes Cycle 14 Stage
  2 causal_graphs review (scientific_review: true) at SHA-256 5be0b485adfcce0bd375a33c249909fb18176bab8f65a5539d69e3e743ee1b12:
  Updated data/records/xenotime-concentrate.yaml with ''bacillus_xenotime_monazite_concentrate_bioweathering_graph''
  (mechanism_ref: bacillus_concentrate_bioweathering, 6 nodes / 6 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from he2024:
  He Y, Ma L, Liang X, Li X, Zhu J and He H (2024). Resistant rare earth phosphates
  as possible sources of environmental dissolved rare earth elements: Insights from
  experimental bio-weathering of xenotime and monazite. Chemical Geology 661:122186.
  DOI 10.1016/j.chemgeo.2024.122186; complete 56-page GFZ author postprint including
  repository cover, Figures 1-7 and Tables 1-3. (https://doi.org/10.1016/j.chemgeo.2024.122186).
  Live-verified UniProtKB grounding across UniProtKB:A0A0K0QI82 (A0A0K0QI82_BACTU,
  Citrate synthase, gene_symbol: CAB88_23625, TREMBL, NCBITaxon:1428 Bacillus thuringiensis,
  UP000194143); UniProtKB:A0A0B5XLM5 (A0A0B5XLM5_BACTU, Malate dehydrogenase, gene_symbol:
  mdh, TREMBL, NCBITaxon:1428 Bacillus thuringiensis, UP000194143); UniProtKB:A0A0K0QJ28
  (A0A0K0QJ28_BACTU, L-lactate dehydrogenase, gene_symbol: ldh, TREMBL, NCBITaxon:1428
  Bacillus thuringiensis, UP000194143).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 2 (causal_graphs) for cmmmech:xenotime-concentrate.
related_reviews: []
```
