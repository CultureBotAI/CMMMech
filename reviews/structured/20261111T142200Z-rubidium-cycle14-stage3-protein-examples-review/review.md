# Cycle 14 Stage 3 protein_examples and causal_graphs review of Rubidium (cmmmech:rubidium)

- Review: 20261111T142200Z-rubidium-cycle14-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-11T14:21:00Z
- Finished UTC: 2026-11-11T14:22:00Z
- Reviewer: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Rubidium (cmmmech:rubidium) passes Cycle 14 Stage 3 protein_examples review (scientific_review: true) at SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11: Updated data/records/rubidium.yaml with UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703) and 'sphaeroides_241_light_dependent_rb_uptake_graph' (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from primary: Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982).

## Scope And Provenance

Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/rubidium.yaml (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11) and its canonical EDIT history sidecar (history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml) verifying live UniProtKB grounding (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703)), causal-graph node/edge parity across 'sphaeroides_241_light_dependent_rb_uptake_graph' (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges), and primary-source evidence fidelity.

Selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:rubidium
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 000fd9c1bad8e0de32a55b4bc1554d4a86696dae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:rubidium | data/records/rubidium.yaml | maintained | Rubidium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:rubidium | Checked 713 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:rubidium | Checked 1583 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of UniProtKB protein_examples grounding, causal_graphs structure, and parity across 'sphaeroides_241_light_dependent_rb_uptake_graph' (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:rubidium.

Updated data/records/rubidium.yaml (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11) with live-verified protein_examples (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703)) and causal_graphs ('sphaeroides_241_light_dependent_rb_uptake_graph' (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary: Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:rubidium.

data/records/rubidium.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml (SHA-256 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a: Added strain-exact Cereibacter sphaeroides 2.4.1 reference-proteome protein examples (PufL UniProtKB:Q3J1A5, TrkA UniProtKB:Q3J2L5) and representative causal graph for light-dependent Rb+ uptake.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/rubidium.yaml; Working-tree record data/records/rubidium.yaml (mechanisms[].protein_examples and causal_graphs) | supports | Updated data/records/rubidium.yaml (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11) with live-verified protein_examples (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703)) and causal_graphs ('sphaeroides_241_light_dependent_rb_uptake_graph' (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels. |
| primary_source | https://doi.org/10.1128/jb.150.3.1183-1191.1982; primary: Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982) | supports | Live-verified UniProtKB grounding across UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides 2.4.1, UP000002703). Primary mechanism source (primary: Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml; Canonical EDIT history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml | supports | Canonical EDIT history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml (SHA-256 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a): Added strain-exact Cereibacter sphaeroides 2.4.1 reference-proteome protein examples (PufL UniProtKB:Q3J1A5, TrkA UniProtKB:Q3J2L5) and representative causal graph for light-dependent Rb+ uptake. |
| validation | data/records/rubidium.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/rubidium.yaml and history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:rubidium.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T142200Z-rubidium-cycle14-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 14 Stage 3 protein_examples and causal_graphs review of Rubidium (cmmmech:rubidium)
started_at: '2026-11-11T14:21:00Z'
finished_at: '2026-11-11T14:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle14-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 14 Stage 3 curation of data/records/rubidium.yaml (SHA-256
    678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11) against live
    UniProtKB grounding and cited primary source (primary: Hellingwerf, Friedberg,
    Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated Transport
    of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology 150(3):1183-1191.
    DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339. Full nine-page article
    scans, especially pp. 1183-1184 and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 000fd9c1bad8e0de32a55b4bc1554d4a86696dae
  state: working_tree
  inputs:
  - path: data/records/rubidium.yaml
    sha256: 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11
    role: target
  - path: history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
    sha256: 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:rubidium
  path: data/records/rubidium.yaml
  label: Rubidium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rubidium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
    role: canonical_history
scope:
  description: 'Cycle 14 Stage 3 protein_examples and causal_graphs review of data/records/rubidium.yaml
    (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11) and
    its canonical EDIT history sidecar (history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml)
    verifying live UniProtKB grounding (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center
    protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake
    protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703)), causal-graph node/edge parity across ''sphaeroides_241_light_dependent_rb_uptake_graph''
    (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges), and
    primary-source evidence fidelity.'
  selection: Cycle 14 Stage 3 protein_examples cohort review for cmmmech:rubidium
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:rubidium
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/rubidium.yaml
  locator: Working-tree record data/records/rubidium.yaml (mechanisms[].protein_examples
    and causal_graphs)
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Updated data/records/rubidium.yaml (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11)
    with live-verified protein_examples (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center
    protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake
    protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703)) and causal_graphs (''sphaeroides_241_light_dependent_rb_uptake_graph''
    (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels.'
  snapshot_sha256: 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/jb.150.3.1183-1191.1982
  locator: 'primary: Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982).
    Energy Coupling of Facilitated Transport of Inorganic Ions in Rhodopseudomonas
    sphaeroides. Journal of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982;
    PMID 6281239; PMC216339. Full nine-page article scans, especially pp. 1183-1184
    and 1187-1190, Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982)'
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:Q3J1A5 (RCEL_CERS4,
    Reaction center protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943
    Cereibacter sphaeroides 2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk
    system potassium uptake protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943
    Cereibacter sphaeroides 2.4.1, UP000002703). Primary mechanism source (primary:
    Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of
    Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal
    of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239;
    PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190,
    Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982)) parameters and
    source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
  locator: Canonical EDIT history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
    (SHA-256 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a): Added
    strain-exact Cereibacter sphaeroides 2.4.1 reference-proteome protein examples
    (PufL UniProtKB:Q3J1A5, TrkA UniProtKB:Q3J2L5) and representative causal graph
    for light-dependent Rb+ uptake.'
  snapshot_sha256: 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a
- evidence_id: validation
  kind: validation
  reference: data/records/rubidium.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-11T14:22:00Z'
  support: supports
  summary: data/records/rubidium.yaml and history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 713 record(s); 0 failed.
  target_ids:
  - cmmmech:rubidium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1583 history record(s); 0 error(s).
  target_ids:
  - cmmmech:rubidium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_grounding_and_causal_graph
  area: graph
  topic: 'Verification of UniProtKB protein_examples grounding, causal_graphs structure,
    and parity across ''sphaeroides_241_light_dependent_rb_uptake_graph'' (mechanism_ref:
    sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/rubidium.yaml (SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11)
    with live-verified protein_examples (UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center
    protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake
    protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides
    2.4.1, UP000002703)) and causal_graphs (''sphaeroides_241_light_dependent_rb_uptake_graph''
    (mechanism_ref: sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary: Hellingwerf,
    Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of Facilitated
    Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal of Bacteriology
    150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239; PMC216339.
    Full nine-page article scans, especially pp. 1183-1184 and 1187-1190, Figures
    4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982).'
  target_ids:
  - cmmmech:rubidium
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/rubidium.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/rubidium/2026-11-11T142118Z-marcin-360277.yaml
    (SHA-256 5ab0840270e095853e65f490856a8f72f5b548a76aca37021f7a7a3611fcff1a: Added
    strain-exact Cereibacter sphaeroides 2.4.1 reference-proteome protein examples
    (PufL UniProtKB:Q3J1A5, TrkA UniProtKB:Q3J2L5) and representative causal graph
    for light-dependent Rb+ uptake.) and passing all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:rubidium
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Rubidium (cmmmech:rubidium) passes Cycle 14 Stage 3 protein_examples review
  (scientific_review: true) at SHA-256 678ba63cfe4a7a7ffd7aa8c6beabbc53ea4229b69deeffea934cf27cef0ead11:
  Updated data/records/rubidium.yaml with UniProtKB:Q3J1A5 (RCEL_CERS4, Reaction center
  protein L chain, gene_symbol: pufL, SWISS_PROT, NCBITaxon:272943 Cereibacter sphaeroides
  2.4.1, UP000002703); UniProtKB:Q3J2L5 (Q3J2L5_CERS4, Trk system potassium uptake
  protein TrkA, gene_symbol: trkA, TREMBL, NCBITaxon:272943 Cereibacter sphaeroides
  2.4.1, UP000002703) and ''sphaeroides_241_light_dependent_rb_uptake_graph'' (mechanism_ref:
  sphaeroides_light_dependent_rb_uptake, 4 nodes / 3 edges), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from primary:
  Hellingwerf, Friedberg, Lolkema, Michels and Konings (1982). Energy Coupling of
  Facilitated Transport of Inorganic Ions in Rhodopseudomonas sphaeroides. Journal
  of Bacteriology 150(3):1183-1191. DOI 10.1128/jb.150.3.1183-1191.1982; PMID 6281239;
  PMC216339. Full nine-page article scans, especially pp. 1183-1184 and 1187-1190,
  Figures 4-5. (https://doi.org/10.1128/jb.150.3.1183-1191.1982).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 14 Stage 3 (protein_examples) for cmmmech:rubidium.
related_reviews: []
```
