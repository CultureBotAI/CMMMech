# Cycle 12 Stage 2 post-remediation review (#975) of Chernikovite (cmmmech:chernikovite)

- Review: 20261109T172200Z-chernikovite-cycle12-stage2-issue975-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T17:20:00Z
- Finished UTC: 2026-11-09T17:22:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chernikovite (cmmmech:chernikovite) passes Cycle 12 Stage 2 post-remediation (#975) review (scientific_review: true) at SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52: Remediated data/records/chernikovite.yaml with causal_graph 'fungal_broth_uranyl_phosphate_precipitation_graph' (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from hu2018: Hu et al. (2018). Utilization of phosphate rock as a sole source of phosphorus for uranium biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full XML and original figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F). Live-verified UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM, Purple acid phosphatase, gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM, Phytase A, gene_symbol: BHQ10_002835, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM, Citrate synthase, gene_symbol: BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363).

## Scope And Provenance

Cycle 12 Stage 2 post-remediation (#975) review of data/records/chernikovite.yaml (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52) and its canonical EDIT history sidecars (history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml, history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source evidence fidelity across causal_graph 'fungal_broth_uranyl_phosphate_precipitation_graph' (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]).

Selection: Cycle 12 Stage 2 Issue #975 post-remediation review for cmmmech:chernikovite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f3b1cc70981859b389d29f02e3f1bafdc0f0ea6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chernikovite | data/records/chernikovite.yaml | maintained | Chernikovite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:chernikovite | Checked 703 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:chernikovite | Checked 1489 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across causal_graph 'fungal_broth_uranyl_phosphate_precipitation_graph' (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]) after Issue #975 remediation

graph: supported. Targets: cmmmech:chernikovite.

Remediated data/records/chernikovite.yaml (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52) under Issue #975 with causal_graph 'fungal_broth_uranyl_phosphate_precipitation_graph' (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from hu2018: Hu et al. (2018). Utilization of phosphate rock as a sole source of phosphorus for uranium biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full XML and original figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F). Live-verified UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM, Purple acid phosphatase, gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM, Phytase A, gene_symbol: BHQ10_002835, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM, Citrate synthase, gene_symbol: BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363).

### Verification of canonical EDIT history sidecars and strict schema validation

provenance: supported. Targets: cmmmech:chernikovite.

data/records/chernikovite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecars (history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml (SHA-256 aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2: Add fungal_broth_uranyl_phosphate_precipitation_graph causal graph and ground fungal_broth_uranyl_phosphate_precipitation to congeneric Talaromyces amestolkiae reference-proteome phosphatase/phytase and citrate synthase entries (UniProtKB:A0A364KM61, UniProtKB:A0A364KTF1, UniProtKB:A0A364KNG2)); history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml (SHA-256 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64: Clarify multi-domain TrEMBL gene-model annotation note for UniProtKB:A0A364KM61 (BHQ10_000639) in chernikovite.yaml (#975))) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/chernikovite.yaml; Working-tree record data/records/chernikovite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Remediated data/records/chernikovite.yaml (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52) under Issue #975 with causal_graph 'fungal_broth_uranyl_phosphate_precipitation_graph' (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1039/C8RA01344F; hu2018: Hu et al. (2018). Utilization of phosphate rock as a sole source of phosphorus for uranium biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full XML and original figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F) | supports | Live-verified UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM, Purple acid phosphatase, gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM, Phytase A, gene_symbol: BHQ10_002835, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM, Citrate synthase, gene_symbol: BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363). Primary mechanism source (hu2018: Hu et al. (2018). Utilization of phosphate rock as a sole source of phosphorus for uranium biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full XML and original figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F)) parameters, RT-qPCR/multi-omics scope, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml; Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml | supports | Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml (SHA-256 aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2): Add fungal_broth_uranyl_phosphate_precipitation_graph causal graph and ground fungal_broth_uranyl_phosphate_precipitation to congeneric Talaromyces amestolkiae reference-proteome phosphatase/phytase and citrate synthase entries (UniProtKB:A0A364KM61, UniProtKB:A0A364KTF1, UniProtKB:A0A364KNG2) |
| edit_history_2 | history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml; Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml | supports | Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml (SHA-256 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64): Clarify multi-domain TrEMBL gene-model annotation note for UniProtKB:A0A364KM61 (BHQ10_000639) in chernikovite.yaml (#975) |
| validation | data/records/chernikovite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/chernikovite.yaml and history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml, history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR re-review is executed prior to merge.
- Executed during Cycle 12 Stage 2 (causal_graphs) following Issue #975 review remediation for cmmmech:chernikovite (PR #974 follow-up to 20261109T163600Z-chernikovite-cycle12-stage2-causal-graphs-review).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T172200Z-chernikovite-cycle12-stage2-issue975-rereview
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 2 post-remediation review (#975) of Chernikovite (cmmmech:chernikovite)
started_at: '2026-11-09T17:20:00Z'
finished_at: '2026-11-09T17:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Issue #975 post-remediation state of data/records/chernikovite.yaml
    (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52) against
    live UniProtKB grounding and cited primary source (hu2018: Hu et al. (2018). Utilization
    of phosphate rock as a sole source of phosphorus for uranium biomineralization
    mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F.
    Complete seven-page original, Figures 1-7 and Tables 1-2 embedded within Figure
    7 inspected; full XML and original figure files independently acquired through
    Europe PMC. (https://doi.org/10.1039/C8RA01344F)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f3b1cc70981859b389d29f02e3f1bafdc0f0ea6c
  state: working_tree
  inputs:
  - path: data/records/chernikovite.yaml
    sha256: 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52
    role: target
  - path: history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
    sha256: aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2
    role: context
  - path: history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml
    sha256: 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:chernikovite
  path: data/records/chernikovite.yaml
  label: Chernikovite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chernikovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml
    role: canonical_history
scope:
  description: 'Cycle 12 Stage 2 post-remediation (#975) review of data/records/chernikovite.yaml
    (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52) and
    its canonical EDIT history sidecars (history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml,
    history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml) verifying
    causal-graph node/edge topology, live UniProtKB grounding, and primary-source
    evidence fidelity across causal_graph ''fungal_broth_uranyl_phosphate_precipitation_graph''
    (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges;
    talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639,
    A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM,
    UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]).'
  selection: 'Cycle 12 Stage 2 Issue #975 post-remediation review for cmmmech:chernikovite'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chernikovite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/chernikovite.yaml
  locator: Working-tree record data/records/chernikovite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Remediated data/records/chernikovite.yaml (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52)
    under Issue #975 with causal_graph ''fungal_broth_uranyl_phosphate_precipitation_graph''
    (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges;
    talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639,
    A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM,
    UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1039/C8RA01344F
  locator: 'hu2018: Hu et al. (2018). Utilization of phosphate rock as a sole source
    of phosphorus for uranium biomineralization mediated by Penicillium funiculosum.
    RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page original,
    Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full XML and original
    figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F)'
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM,
    Purple acid phosphatase, gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081
    Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM,
    Phytase A, gene_symbol: BHQ10_002835, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae,
    UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM, Citrate synthase, gene_symbol:
    BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363).
    Primary mechanism source (hu2018: Hu et al. (2018). Utilization of phosphate rock
    as a sole source of phosphorus for uranium biomineralization mediated by Penicillium
    funiculosum. RSC Advances 8, 13459-13465. DOI 10.1039/C8RA01344F. Complete seven-page
    original, Figures 1-7 and Tables 1-2 embedded within Figure 7 inspected; full
    XML and original figure files independently acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F))
    parameters, RT-qPCR/multi-omics scope, and source-level caveats are strictly preserved
    on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
  locator: Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
    (SHA-256 aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2): Add
    fungal_broth_uranyl_phosphate_precipitation_graph causal graph and ground fungal_broth_uranyl_phosphate_precipitation
    to congeneric Talaromyces amestolkiae reference-proteome phosphatase/phytase and
    citrate synthase entries (UniProtKB:A0A364KM61, UniProtKB:A0A364KTF1, UniProtKB:A0A364KNG2)'
  snapshot_sha256: aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml
  locator: Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml
    (SHA-256 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64): Clarify
    multi-domain TrEMBL gene-model annotation note for UniProtKB:A0A364KM61 (BHQ10_000639)
    in chernikovite.yaml (#975)'
  snapshot_sha256: 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64
- evidence_id: validation
  kind: validation
  reference: data/records/chernikovite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T17:22:00Z'
  support: supports
  summary: data/records/chernikovite.yaml and history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml,
    history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml pass strict
    LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 703 record(s); 0 failed.
  target_ids:
  - cmmmech:chernikovite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1489 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chernikovite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across causal_graph ''fungal_broth_uranyl_phosphate_precipitation_graph'' (mechanism_ref:
    fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges; talaromyces_phosphatase_and_citrate_synthase:
    [UniProtKB:A0A364KM61 (BHQ10_000639, A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1
    (BHQ10_002835, A0A364KTF1_TALAM, UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108,
    A0A364KNG2_TALAM, UP000249363)]) after Issue #975 remediation'
  outcome: supported
  summary: 'Remediated data/records/chernikovite.yaml (SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52)
    under Issue #975 with causal_graph ''fungal_broth_uranyl_phosphate_precipitation_graph''
    (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges;
    talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639,
    A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM,
    UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from hu2018: Hu et al.
    (2018). Utilization of phosphate rock as a sole source of phosphorus for uranium
    biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465.
    DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2
    embedded within Figure 7 inspected; full XML and original figure files independently
    acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F). Live-verified
    UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM, Purple acid
    phosphatase, gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081 Talaromyces
    amestolkiae, UP000249363); UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM, Phytase A,
    gene_symbol: BHQ10_002835, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae,
    UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM, Citrate synthase, gene_symbol:
    BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363).'
  target_ids:
  - cmmmech:chernikovite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecars and strict schema validation
  outcome: supported
  summary: 'data/records/chernikovite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecars (history/records/chernikovite/2026-11-09T161813Z-marcin-60388f.yaml
    (SHA-256 aac71f2e1b8f44c886fa4bbbfd642ac979f506906035c88913843c21a492a1c2: Add
    fungal_broth_uranyl_phosphate_precipitation_graph causal graph and ground fungal_broth_uranyl_phosphate_precipitation
    to congeneric Talaromyces amestolkiae reference-proteome phosphatase/phytase and
    citrate synthase entries (UniProtKB:A0A364KM61, UniProtKB:A0A364KTF1, UniProtKB:A0A364KNG2));
    history/records/chernikovite/2026-11-09T172114Z-marcin-ef9090.yaml (SHA-256 70357387bf32743efcc85ec734fc42e4072b44f177ab5c6f451951ff01aecc64:
    Clarify multi-domain TrEMBL gene-model annotation note for UniProtKB:A0A364KM61
    (BHQ10_000639) in chernikovite.yaml (#975))) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:chernikovite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Chernikovite (cmmmech:chernikovite) passes Cycle 12 Stage 2 post-remediation
  (#975) review (scientific_review: true) at SHA-256 0568a1a962bdf27f932795e8d3e3802ef5d2dd2c4c5a57daa8f8631f649e1f52:
  Remediated data/records/chernikovite.yaml with causal_graph ''fungal_broth_uranyl_phosphate_precipitation_graph''
  (mechanism_ref: fungal_broth_uranyl_phosphate_precipitation, 4 nodes / 3 edges;
  talaromyces_phosphatase_and_citrate_synthase: [UniProtKB:A0A364KM61 (BHQ10_000639,
  A0A364KM61_TALAM, UP000249363), UniProtKB:A0A364KTF1 (BHQ10_002835, A0A364KTF1_TALAM,
  UP000249363), UniProtKB:A0A364KNG2 (BHQ10_001108, A0A364KNG2_TALAM, UP000249363)]),
  achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from hu2018:
  Hu et al. (2018). Utilization of phosphate rock as a sole source of phosphorus for
  uranium biomineralization mediated by Penicillium funiculosum. RSC Advances 8, 13459-13465.
  DOI 10.1039/C8RA01344F. Complete seven-page original, Figures 1-7 and Tables 1-2
  embedded within Figure 7 inspected; full XML and original figure files independently
  acquired through Europe PMC. (https://doi.org/10.1039/C8RA01344F). Live-verified
  UniProtKB grounding across UniProtKB:A0A364KM61 (A0A364KM61_TALAM, Purple acid phosphatase,
  gene_symbol: BHQ10_000639, TREMBL, NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363);
  UniProtKB:A0A364KTF1 (A0A364KTF1_TALAM, Phytase A, gene_symbol: BHQ10_002835, TREMBL,
  NCBITaxon:1196081 Talaromyces amestolkiae, UP000249363); UniProtKB:A0A364KNG2 (A0A364KNG2_TALAM,
  Citrate synthase, gene_symbol: BHQ10_001108, TREMBL, NCBITaxon:1196081 Talaromyces
  amestolkiae, UP000249363).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR re-review is executed prior to merge.'
notes:
- 'Executed during Cycle 12 Stage 2 (causal_graphs) following Issue #975 review remediation
  for cmmmech:chernikovite (PR #974 follow-up to 20261109T163600Z-chernikovite-cycle12-stage2-causal-graphs-review).'
related_reviews: []
```
