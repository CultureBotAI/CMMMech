# Cycle 9 Stage 2 causal-graphs review of Barićite (cmmmech:baricite)

- Review: 20261105T172800Z-baricite-cycle9-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-05T17:27:30Z
- Finished UTC: 2026-11-05T17:28:00Z
- Reviewer: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Barićite (cmmmech:baricite) passes Cycle 9 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2: Curated data/records/baricite.yaml with causal_graph 'g20_baricite_assignment_graph' (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from han_2016: Han et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734). Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q30Z34 (Q30Z34_OLEA2, sulfate adenylyltransferase, gene_symbol: Dde_2265, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I5 (Q313I5_OLEA2, Adenylylsulfate reductase, alpha subunit, gene_symbol: Dde_1110, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I6 (Q313I6_OLEA2, Adenylylsulfate reductase, beta subunit, gene_symbol: Dde_1109, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R9 (Q315R9_OLEA2, Sulfite reductase, dissimilatory-type alpha subunit, gene_symbol: Dde_0526, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R8 (Q315R8_OLEA2, Sulfite reductase, dissimilatory-type beta subunit, gene_symbol: Dde_0527, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710).

## Scope And Provenance

Cycle 9 Stage 2 causal-graphs review of data/records/baricite.yaml (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2) and its canonical EDIT history sidecar (history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'g20_baricite_assignment_graph' (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]).

Selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:baricite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 503b381e1b3aba9d1b2525daf9ebffbfb005d19c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:baricite | data/records/baricite.yaml | maintained | Barićite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:baricite | Checked 688 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:baricite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB reference-proteome grounding, and parity across causal_graph 'g20_baricite_assignment_graph' (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)])

graph: supported. Targets: cmmmech:baricite.

Curated data/records/baricite.yaml (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2) with causal_graph 'g20_baricite_assignment_graph' (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from han_2016: Han et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734). Live-verified UniProtKB grounding across UniProtKB:Q30Z34 (Q30Z34_OLEA2, sulfate adenylyltransferase, gene_symbol: Dde_2265, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I5 (Q313I5_OLEA2, Adenylylsulfate reductase, alpha subunit, gene_symbol: Dde_1110, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I6 (Q313I6_OLEA2, Adenylylsulfate reductase, beta subunit, gene_symbol: Dde_1109, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R9 (Q315R9_OLEA2, Sulfite reductase, dissimilatory-type alpha subunit, gene_symbol: Dde_0526, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R8 (Q315R8_OLEA2, Sulfite reductase, dissimilatory-type beta subunit, gene_symbol: Dde_0527, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:baricite.

data/records/baricite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml (SHA-256 bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/baricite.yaml; Working-tree record data/records/baricite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/baricite.yaml (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2) with causal_graph 'g20_baricite_assignment_graph' (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | DOI:10.1038/srep25734; han_2016: Han et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q30Z34 (Q30Z34_OLEA2, sulfate adenylyltransferase, gene_symbol: Dde_2265, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I5 (Q313I5_OLEA2, Adenylylsulfate reductase, alpha subunit, gene_symbol: Dde_1110, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I6 (Q313I6_OLEA2, Adenylylsulfate reductase, beta subunit, gene_symbol: Dde_1109, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R9 (Q315R9_OLEA2, Sulfite reductase, dissimilatory-type alpha subunit, gene_symbol: Dde_0526, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R8 (Q315R8_OLEA2, Sulfite reductase, dissimilatory-type beta subunit, gene_symbol: Dde_0527, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710). Primary mechanism source(s) (han_2016: Han et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734)) report culture-level mineralization or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml; Canonical EDIT history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml | supports | Canonical EDIT history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml (SHA-256 bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff): Add REPRESENTATIVE_EXAMPLE causal graph and live-verified Oleidesulfovibrio alaskensis G20 (NCBITaxon:207559; UP000002710) dissimilatory sulfate-reduction protein groundings (Sat Dde_2265 UniProtKB:Q30Z34, AprBA Dde_1110/Dde_1109 UniProtKB:Q313I5/UniProtKB:Q313I6, and DsrAB Dde_0526/Dde_0527 UniProtKB:Q315R9/UniProtKB:Q315R8) for H2-fed barićite-assigned phosphate precipitation in Han et al. (2016). |
| validation | data/records/baricite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/baricite.yaml and history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:baricite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T172800Z-baricite-cycle9-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 9 Stage 2 causal-graphs review of Barićite (cmmmech:baricite)
started_at: '2026-11-05T17:27:30Z'
finished_at: '2026-11-05T17:28:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 9 Stage 2 causal_graphs and ProteinExample curation in data/records/baricite.yaml
    (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2) against
    live UniProtKB reference proteomes and cited primary source(s) (han_2016: Han
    et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate
    in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports
    6:25734. (https://doi.org/10.1038/srep25734)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 503b381e1b3aba9d1b2525daf9ebffbfb005d19c
  state: working_tree
  inputs:
  - path: data/records/baricite.yaml
    sha256: c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2
    role: target
  - path: history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
    sha256: bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:baricite
  path: data/records/baricite.yaml
  label: Barićite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baricite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
    role: canonical_history
scope:
  description: 'Cycle 9 Stage 2 causal-graphs review of data/records/baricite.yaml
    (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2) and
    its canonical EDIT history sidecar (history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''g20_baricite_assignment_graph''
    (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation:
    [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110,
    Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)];
    g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710),
    UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]).'
  selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:baricite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:baricite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/baricite.yaml
  locator: Working-tree record data/records/baricite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Curated data/records/baricite.yaml (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2)
    with causal_graph ''g20_baricite_assignment_graph'' (mechanism_ref: g20_baricite_assignment,
    4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265,
    Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710),
    UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase:
    [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527,
    Q315R8_OLEA2, UP000002710)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1038/srep25734
  locator: 'han_2016: Han et al. (2016). Bio-precipitation of Crystalline Magnesium
    Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing Bacteria.
    Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734)'
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q30Z34
    (Q30Z34_OLEA2, sulfate adenylyltransferase, gene_symbol: Dde_2265, TREMBL, NCBITaxon:207559
    Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I5 (Q313I5_OLEA2,
    Adenylylsulfate reductase, alpha subunit, gene_symbol: Dde_1110, TREMBL, NCBITaxon:207559
    Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q313I6 (Q313I6_OLEA2,
    Adenylylsulfate reductase, beta subunit, gene_symbol: Dde_1109, TREMBL, NCBITaxon:207559
    Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R9 (Q315R9_OLEA2,
    Sulfite reductase, dissimilatory-type alpha subunit, gene_symbol: Dde_0526, TREMBL,
    NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R8
    (Q315R8_OLEA2, Sulfite reductase, dissimilatory-type beta subunit, gene_symbol:
    Dde_0527, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710).
    Primary mechanism source(s) (han_2016: Han et al. (2016). Bio-precipitation of
    Crystalline Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by
    Sulfate-reducing Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734))
    report culture-level mineralization or bioleaching without single-gene knockouts;
    supports: partial is strictly preserved on all enzyme-level edges and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
  locator: Canonical EDIT history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
    (SHA-256 bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff): Add
    REPRESENTATIVE_EXAMPLE causal graph and live-verified Oleidesulfovibrio alaskensis
    G20 (NCBITaxon:207559; UP000002710) dissimilatory sulfate-reduction protein groundings
    (Sat Dde_2265 UniProtKB:Q30Z34, AprBA Dde_1110/Dde_1109 UniProtKB:Q313I5/UniProtKB:Q313I6,
    and DsrAB Dde_0526/Dde_0527 UniProtKB:Q315R9/UniProtKB:Q315R8) for H2-fed barićite-assigned
    phosphate precipitation in Han et al. (2016).'
  snapshot_sha256: bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff
- evidence_id: validation
  kind: validation
  reference: data/records/baricite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: data/records/baricite.yaml and history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 688 record(s); 0 failed.
  target_ids:
  - cmmmech:baricite
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
  - cmmmech:baricite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB reference-proteome grounding,
    and parity across causal_graph ''g20_baricite_assignment_graph'' (mechanism_ref:
    g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation:
    [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110,
    Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)];
    g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710),
    UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)])'
  outcome: supported
  summary: 'Curated data/records/baricite.yaml (SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2)
    with causal_graph ''g20_baricite_assignment_graph'' (mechanism_ref: g20_baricite_assignment,
    4 nodes / 3 edges; g20_sat_aprba_sulfate_activation: [UniProtKB:Q30Z34 (Dde_2265,
    Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110, Q313I5_OLEA2, UP000002710),
    UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)]; g20_dsrab_sulfite_reductase:
    [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710), UniProtKB:Q315R8 (Dde_0527,
    Q315R8_OLEA2, UP000002710)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from han_2016: Han et al. (2016). Bio-precipitation of Crystalline
    Magnesium Phosphate and Carbonate in Synthetic Marine Pore-water by Sulfate-reducing
    Bacteria. Scientific Reports 6:25734. (https://doi.org/10.1038/srep25734). Live-verified
    UniProtKB grounding across UniProtKB:Q30Z34 (Q30Z34_OLEA2, sulfate adenylyltransferase,
    gene_symbol: Dde_2265, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20,
    UP000002710); UniProtKB:Q313I5 (Q313I5_OLEA2, Adenylylsulfate reductase, alpha
    subunit, gene_symbol: Dde_1110, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis
    G20, UP000002710); UniProtKB:Q313I6 (Q313I6_OLEA2, Adenylylsulfate reductase,
    beta subunit, gene_symbol: Dde_1109, TREMBL, NCBITaxon:207559 Oleidesulfovibrio
    alaskensis G20, UP000002710); UniProtKB:Q315R9 (Q315R9_OLEA2, Sulfite reductase,
    dissimilatory-type alpha subunit, gene_symbol: Dde_0526, TREMBL, NCBITaxon:207559
    Oleidesulfovibrio alaskensis G20, UP000002710); UniProtKB:Q315R8 (Q315R8_OLEA2,
    Sulfite reductase, dissimilatory-type beta subunit, gene_symbol: Dde_0527, TREMBL,
    NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710).'
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: data/records/baricite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/baricite/2026-11-05T171248Z-marcin-0b1453.yaml
    (SHA-256 bddd35ff0ca234387f7510e9f3fc1efb57493c04765a8024c19afbdaf4c798ff) and
    passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Barićite (cmmmech:baricite) passes Cycle 9 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 c13af761df9b78e689225baf7e670b9796ce7a78692ce8b891f9d030323d07a2:
  Curated data/records/baricite.yaml with causal_graph ''g20_baricite_assignment_graph''
  (mechanism_ref: g20_baricite_assignment, 4 nodes / 3 edges; g20_sat_aprba_sulfate_activation:
  [UniProtKB:Q30Z34 (Dde_2265, Q30Z34_OLEA2, UP000002710), UniProtKB:Q313I5 (Dde_1110,
  Q313I5_OLEA2, UP000002710), UniProtKB:Q313I6 (Dde_1109, Q313I6_OLEA2, UP000002710)];
  g20_dsrab_sulfite_reductase: [UniProtKB:Q315R9 (Dde_0526, Q315R9_OLEA2, UP000002710),
  UniProtKB:Q315R8 (Dde_0527, Q315R8_OLEA2, UP000002710)]), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from han_2016:
  Han et al. (2016). Bio-precipitation of Crystalline Magnesium Phosphate and Carbonate
  in Synthetic Marine Pore-water by Sulfate-reducing Bacteria. Scientific Reports
  6:25734. (https://doi.org/10.1038/srep25734). Live-verified UniProtKB reference-proteome
  grounding across UniProtKB:Q30Z34 (Q30Z34_OLEA2, sulfate adenylyltransferase, gene_symbol:
  Dde_2265, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710);
  UniProtKB:Q313I5 (Q313I5_OLEA2, Adenylylsulfate reductase, alpha subunit, gene_symbol:
  Dde_1110, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710);
  UniProtKB:Q313I6 (Q313I6_OLEA2, Adenylylsulfate reductase, beta subunit, gene_symbol:
  Dde_1109, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20, UP000002710);
  UniProtKB:Q315R9 (Q315R9_OLEA2, Sulfite reductase, dissimilatory-type alpha subunit,
  gene_symbol: Dde_0526, TREMBL, NCBITaxon:207559 Oleidesulfovibrio alaskensis G20,
  UP000002710); UniProtKB:Q315R8 (Q315R8_OLEA2, Sulfite reductase, dissimilatory-type
  beta subunit, gene_symbol: Dde_0527, TREMBL, NCBITaxon:207559 Oleidesulfovibrio
  alaskensis G20, UP000002710).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:baricite.
related_reviews: []
```
