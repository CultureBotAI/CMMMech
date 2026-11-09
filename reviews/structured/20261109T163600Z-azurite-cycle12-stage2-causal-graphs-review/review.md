# Cycle 12 Stage 2 causal-graphs review of Azurite (cmmmech:azurite)

- Review: 20261109T163600Z-azurite-cycle12-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T16:15:00Z
- Finished UTC: 2026-11-09T16:36:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Azurite (cmmmech:azurite) passes Cycle 12 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061: Curated data/records/azurite.yaml with causal_graph 'b22_mixed_carbonate_azurite_precipitation_graph' (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL, UP001596109)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration of copper by bacteria isolated from an abandoned mine by using microbially induced calcite precipitation. Journal of General and Applied Microbiology 62:206–212. Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001). Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0 (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109).

## Scope And Provenance

Cycle 12 Stage 2 causal-graphs review of data/records/azurite.yaml (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061) and its canonical EDIT history sidecar(s) (history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source evidence fidelity across causal_graph 'b22_mixed_carbonate_azurite_precipitation_graph' (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL, UP001596109)]).

Selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:azurite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7449fa912e2d92f8aff400481ee75b49edbb685e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:azurite | data/records/azurite.yaml | maintained | Azurite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:azurite | Checked 703 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:azurite | Checked 1484 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across causal_graph 'b22_mixed_carbonate_azurite_precipitation_graph' (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL, UP001596109)])

graph: supported. Targets: cmmmech:azurite.

Curated data/records/azurite.yaml (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061) with causal_graph 'b22_mixed_carbonate_azurite_precipitation_graph' (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL, UP001596109)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration of copper by bacteria isolated from an abandoned mine by using microbially induced calcite precipitation. Journal of General and Applied Microbiology 62:206–212. Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001). Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0 (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:azurite.

data/records/azurite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml (SHA-256 b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551: Add b22_mixed_carbonate_azurite_precipitation_graph causal graph and ground culture_associated_mixed_carbonate_precipitation to Sporosarcina soli reference-proteome UreABC subunits (UniProtKB:A0ABW0TKM3, UniProtKB:A0ABW0TKX1, UniProtKB:A0ABW0TMB0))) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/azurite.yaml; Working-tree record data/records/azurite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/azurite.yaml (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061) with causal_graph 'b22_mixed_carbonate_azurite_precipitation_graph' (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL, UP001596109)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.2323/jgam.2016.03.001; kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration of copper by bacteria isolated from an abandoned mine by using microbially induced calcite precipitation. Journal of General and Applied Microbiology 62:206–212. Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001) | supports | Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL, Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta, gene_symbol: ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0 (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109). Primary mechanism source (kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration of copper by bacteria isolated from an abandoned mine by using microbially induced calcite precipitation. Journal of General and Applied Microbiology 62:206–212. Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml; Canonical EDIT history sidecar history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml | supports | Canonical EDIT history sidecar history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml (SHA-256 b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551): Add b22_mixed_carbonate_azurite_precipitation_graph causal graph and ground culture_associated_mixed_carbonate_precipitation to Sporosarcina soli reference-proteome UreABC subunits (UniProtKB:A0ABW0TKM3, UniProtKB:A0ABW0TKX1, UniProtKB:A0ABW0TMB0) |
| validation | data/records/azurite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/azurite.yaml and history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:azurite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T163600Z-azurite-cycle12-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 2 causal-graphs review of Azurite (cmmmech:azurite)
started_at: '2026-11-09T16:15:00Z'
finished_at: '2026-11-09T16:36:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 12 Stage 2 causal_graphs and ProteinExample curation in data/records/azurite.yaml
    (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061) against
    live UniProtKB grounding and cited primary source (kang2016: Kang, Shin, Anbu,
    Nam and So (2016). Biosequestration of copper by bacteria isolated from an abandoned
    mine by using microbially induced calcite precipitation. Journal of General and
    Applied Microbiology 62:206–212. Complete seven-page original, Methods pp. 207–208
    and Figures 1–8, especially mixed-phase Figure 7 and distinct solution assay Figure
    8. (https://doi.org/10.2323/jgam.2016.03.001)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 7449fa912e2d92f8aff400481ee75b49edbb685e
  state: working_tree
  inputs:
  - path: data/records/azurite.yaml
    sha256: b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061
    role: target
  - path: history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
    sha256: b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:azurite
  path: data/records/azurite.yaml
  label: Azurite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/azurite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
    role: canonical_history
scope:
  description: 'Cycle 12 Stage 2 causal-graphs review of data/records/azurite.yaml
    (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061) and
    its canonical EDIT history sidecar(s) (history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source
    evidence fidelity across causal_graph ''b22_mixed_carbonate_azurite_precipitation_graph''
    (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3
    edges; sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL,
    UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0
    (ureA, A0ABW0TMB0_9BACL, UP001596109)]).'
  selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:azurite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:azurite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/azurite.yaml
  locator: Working-tree record data/records/azurite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Curated data/records/azurite.yaml (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061)
    with causal_graph ''b22_mixed_carbonate_azurite_precipitation_graph'' (mechanism_ref:
    culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex:
    [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1
    (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL,
    UP001596109)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.2323/jgam.2016.03.001
  locator: 'kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration of copper
    by bacteria isolated from an abandoned mine by using microbially induced calcite
    precipitation. Journal of General and Applied Microbiology 62:206–212. Complete
    seven-page original, Methods pp. 207–208 and Figures 1–8, especially mixed-phase
    Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001)'
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL,
    Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina
    soli, UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta,
    gene_symbol: ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0
    (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736
    Sporosarcina soli, UP001596109). Primary mechanism source (kang2016: Kang, Shin,
    Anbu, Nam and So (2016). Biosequestration of copper by bacteria isolated from
    an abandoned mine by using microbially induced calcite precipitation. Journal
    of General and Applied Microbiology 62:206–212. Complete seven-page original,
    Methods pp. 207–208 and Figures 1–8, especially mixed-phase Figure 7 and distinct
    solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001)) parameters,
    analytical denominators, and source-level caveats are strictly preserved on all
    nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
  locator: Canonical EDIT history sidecar history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
    (SHA-256 b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551): Add
    b22_mixed_carbonate_azurite_precipitation_graph causal graph and ground culture_associated_mixed_carbonate_precipitation
    to Sporosarcina soli reference-proteome UreABC subunits (UniProtKB:A0ABW0TKM3,
    UniProtKB:A0ABW0TKX1, UniProtKB:A0ABW0TMB0)'
  snapshot_sha256: b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551
- evidence_id: validation
  kind: validation
  reference: data/records/azurite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: data/records/azurite.yaml and history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 703 record(s); 0 failed.
  target_ids:
  - cmmmech:azurite
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
  - cmmmech:azurite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across causal_graph ''b22_mixed_carbonate_azurite_precipitation_graph'' (mechanism_ref:
    culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex:
    [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1
    (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL,
    UP001596109)])'
  outcome: supported
  summary: 'Curated data/records/azurite.yaml (SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061)
    with causal_graph ''b22_mixed_carbonate_azurite_precipitation_graph'' (mechanism_ref:
    culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges; sporosarcina_soli_ureabc_complex:
    [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL, UP001596109), UniProtKB:A0ABW0TKX1
    (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0 (ureA, A0ABW0TMB0_9BACL,
    UP001596109)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from kang2016: Kang, Shin, Anbu, Nam and So (2016). Biosequestration
    of copper by bacteria isolated from an abandoned mine by using microbially induced
    calcite precipitation. Journal of General and Applied Microbiology 62:206–212.
    Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially
    mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001).
    Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL,
    Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina
    soli, UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta,
    gene_symbol: ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0
    (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736
    Sporosarcina soli, UP001596109).'
  target_ids:
  - cmmmech:azurite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/azurite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/azurite/2026-11-09T161812Z-marcin-c02523.yaml
    (SHA-256 b297a52a06b3d761b65adf06207ac44c96d039b6ddc298c28ceac8f749a0d551: Add
    b22_mixed_carbonate_azurite_precipitation_graph causal graph and ground culture_associated_mixed_carbonate_precipitation
    to Sporosarcina soli reference-proteome UreABC subunits (UniProtKB:A0ABW0TKM3,
    UniProtKB:A0ABW0TKX1, UniProtKB:A0ABW0TMB0))) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:azurite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Azurite (cmmmech:azurite) passes Cycle 12 Stage 2 causal-graphs review (scientific_review:
  true) at SHA-256 b640bf91d374655f636442389d189c801eb92711924479f3b2f4b8d3a8850061:
  Curated data/records/azurite.yaml with causal_graph ''b22_mixed_carbonate_azurite_precipitation_graph''
  (mechanism_ref: culture_associated_mixed_carbonate_precipitation, 4 nodes / 3 edges;
  sporosarcina_soli_ureabc_complex: [UniProtKB:A0ABW0TKM3 (ureC, A0ABW0TKM3_9BACL,
  UP001596109), UniProtKB:A0ABW0TKX1 (ureB, A0ABW0TKX1_9BACL, UP001596109), UniProtKB:A0ABW0TMB0
  (ureA, A0ABW0TMB0_9BACL, UP001596109)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from kang2016: Kang, Shin, Anbu, Nam and So (2016).
  Biosequestration of copper by bacteria isolated from an abandoned mine by using
  microbially induced calcite precipitation. Journal of General and Applied Microbiology
  62:206–212. Complete seven-page original, Methods pp. 207–208 and Figures 1–8, especially
  mixed-phase Figure 7 and distinct solution assay Figure 8. (https://doi.org/10.2323/jgam.2016.03.001).
  Live-verified UniProtKB grounding across UniProtKB:A0ABW0TKM3 (A0ABW0TKM3_9BACL,
  Urease subunit alpha, gene_symbol: ureC, TREMBL, NCBITaxon:334736 Sporosarcina soli,
  UP001596109); UniProtKB:A0ABW0TKX1 (A0ABW0TKX1_9BACL, Urease subunit beta, gene_symbol:
  ureB, TREMBL, NCBITaxon:334736 Sporosarcina soli, UP001596109); UniProtKB:A0ABW0TMB0
  (A0ABW0TMB0_9BACL, Urease subunit gamma, gene_symbol: ureA, TREMBL, NCBITaxon:334736
  Sporosarcina soli, UP001596109).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:azurite.
related_reviews: []
```
