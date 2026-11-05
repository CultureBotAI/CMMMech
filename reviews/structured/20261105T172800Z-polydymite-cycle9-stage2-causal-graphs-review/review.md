# Cycle 9 Stage 2 causal-graphs review of Polydymite (cmmmech:polydymite)

- Review: 20261105T172800Z-polydymite-cycle9-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-05T17:27:30Z
- Finished UTC: 2026-11-05T17:28:00Z
- Reviewer: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Polydymite (cmmmech:polydymite) passes Cycle 9 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd: Curated data/records/polydymite.yaml with causal_graph 'hildenborough_nickel_sulfide_formation_graph' (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation: [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2, UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase: [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2, UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151); mansor2019_si: Supplementary Material.. Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q72CI8 (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol: sat, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT2 (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol: aprA, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta subunit, gene_symbol: aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase, dissimilatory-type subunit alpha, gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45575 (DSVB_NITV2, Sulfite reductase, dissimilatory-type subunit beta, gene_symbol: dsvB, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194).

## Scope And Provenance

Cycle 9 Stage 2 causal-graphs review of data/records/polydymite.yaml (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd) and its canonical EDIT history sidecar (history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'hildenborough_nickel_sulfide_formation_graph' (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation: [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2, UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase: [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2, UP000002194)]).

Selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:polydymite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 503b381e1b3aba9d1b2525daf9ebffbfb005d19c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:polydymite | data/records/polydymite.yaml | maintained | Polydymite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:polydymite | Checked 688 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:polydymite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB reference-proteome grounding, and parity across causal_graph 'hildenborough_nickel_sulfide_formation_graph' (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation: [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2, UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase: [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2, UP000002194)])

graph: supported. Targets: cmmmech:polydymite.

Curated data/records/polydymite.yaml (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd) with causal_graph 'hildenborough_nickel_sulfide_formation_graph' (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation: [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2, UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase: [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2, UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151); mansor2019_si: Supplementary Material.. Live-verified UniProtKB grounding across UniProtKB:Q72CI8 (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol: sat, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT2 (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol: aprA, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta subunit, gene_symbol: aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase, dissimilatory-type subunit alpha, gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45575 (DSVB_NITV2, Sulfite reductase, dissimilatory-type subunit beta, gene_symbol: dsvB, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:polydymite.

data/records/polydymite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml (SHA-256 a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/polydymite.yaml; Working-tree record data/records/polydymite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/polydymite.yaml (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd) with causal_graph 'hildenborough_nickel_sulfide_formation_graph' (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation: [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2, UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase: [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2, UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | DOI:10.3389/feart.2019.00151; mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151); mansor2019_si: Supplementary Material. | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q72CI8 (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol: sat, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT2 (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol: aprA, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta subunit, gene_symbol: aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase, dissimilatory-type subunit alpha, gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45575 (DSVB_NITV2, Sulfite reductase, dissimilatory-type subunit beta, gene_symbol: dsvB, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194). Primary mechanism source(s) (mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151); mansor2019_si: Supplementary Material.) report culture-level mineralization or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml; Canonical EDIT history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml | supports | Canonical EDIT history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml (SHA-256 a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d): Add REPRESENTATIVE_EXAMPLE causal graph and live-verified Nitratidesulfovibrio vulgaris str. Hildenborough (NCBITaxon:882; UP000002194) dissimilatory sulfate-reduction protein groundings (sat DVU_1295 UniProtKB:Q72CI8, aprA DVU_0847 UniProtKB:Q72DT2, aprB DVU_0846 UniProtKB:Q72DT3, and Swiss-Prot dsvA/dsvB DVU_0402-DVU_0403 UniProtKB:P45574/UniProtKB:P45575) for minor polydymite-assigned Ni3S4 occurrence in Mansor et al. (2019). |
| validation | data/records/polydymite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/polydymite.yaml and history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:polydymite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T172800Z-polydymite-cycle9-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 9 Stage 2 causal-graphs review of Polydymite (cmmmech:polydymite)
started_at: '2026-11-05T17:27:30Z'
finished_at: '2026-11-05T17:28:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 9 Stage 2 causal_graphs and ProteinExample curation in data/records/polydymite.yaml
    (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd) against
    live UniProtKB reference proteomes and cited primary source(s) (mansor2019: Mansor
    et al. (2019). Biogenic and Abiogenic Nanoparticulate Nickel Sulfide Synthesis,
    Transformation and Crystal Growth in Aqueous Systems. Frontiers in Earth Science
    7:151. (https://doi.org/10.3389/feart.2019.00151); mansor2019_si: Supplementary
    Material.).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 503b381e1b3aba9d1b2525daf9ebffbfb005d19c
  state: working_tree
  inputs:
  - path: data/records/polydymite.yaml
    sha256: 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd
    role: target
  - path: history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
    sha256: a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:polydymite
  path: data/records/polydymite.yaml
  label: Polydymite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polydymite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
    role: canonical_history
scope:
  description: 'Cycle 9 Stage 2 causal-graphs review of data/records/polydymite.yaml
    (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd) and
    its canonical EDIT history sidecar (history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''hildenborough_nickel_sulfide_formation_graph''
    (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation:
    [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2,
    UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase:
    [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2,
    UP000002194)]).'
  selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:polydymite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:polydymite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/polydymite.yaml
  locator: Working-tree record data/records/polydymite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Curated data/records/polydymite.yaml (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd)
    with causal_graph ''hildenborough_nickel_sulfide_formation_graph'' (mechanism_ref:
    hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation:
    [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2,
    UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase:
    [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2,
    UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3389/feart.2019.00151
  locator: 'mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate
    Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems.
    Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151);
    mansor2019_si: Supplementary Material.'
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:Q72CI8
    (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol: sat, TREMBL, NCBITaxon:882
    Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:Q72DT2
    (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol: aprA,
    TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194);
    UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta subunit, gene_symbol:
    aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough,
    UP000002194); UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase, dissimilatory-type
    subunit alpha, gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio
    vulgaris str. Hildenborough, UP000002194); UniProtKB:P45575 (DSVB_NITV2, Sulfite
    reductase, dissimilatory-type subunit beta, gene_symbol: dsvB, SWISS_PROT, NCBITaxon:882
    Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194). Primary mechanism
    source(s) (mansor2019: Mansor et al. (2019). Biogenic and Abiogenic Nanoparticulate
    Nickel Sulfide Synthesis, Transformation and Crystal Growth in Aqueous Systems.
    Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151);
    mansor2019_si: Supplementary Material.) report culture-level mineralization or
    bioleaching without single-gene knockouts; supports: partial is strictly preserved
    on all enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
  locator: Canonical EDIT history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
    (SHA-256 a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d): Add
    REPRESENTATIVE_EXAMPLE causal graph and live-verified Nitratidesulfovibrio vulgaris
    str. Hildenborough (NCBITaxon:882; UP000002194) dissimilatory sulfate-reduction
    protein groundings (sat DVU_1295 UniProtKB:Q72CI8, aprA DVU_0847 UniProtKB:Q72DT2,
    aprB DVU_0846 UniProtKB:Q72DT3, and Swiss-Prot dsvA/dsvB DVU_0402-DVU_0403 UniProtKB:P45574/UniProtKB:P45575)
    for minor polydymite-assigned Ni3S4 occurrence in Mansor et al. (2019).'
  snapshot_sha256: a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d
- evidence_id: validation
  kind: validation
  reference: data/records/polydymite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: data/records/polydymite.yaml and history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 688 record(s); 0 failed.
  target_ids:
  - cmmmech:polydymite
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
  - cmmmech:polydymite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB reference-proteome grounding,
    and parity across causal_graph ''hildenborough_nickel_sulfide_formation_graph''
    (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation:
    [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2,
    UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase:
    [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2,
    UP000002194)])'
  outcome: supported
  summary: 'Curated data/records/polydymite.yaml (SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd)
    with causal_graph ''hildenborough_nickel_sulfide_formation_graph'' (mechanism_ref:
    hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation:
    [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2,
    UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase:
    [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2,
    UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from mansor2019: Mansor et al. (2019). Biogenic and Abiogenic
    Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal Growth in
    Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151);
    mansor2019_si: Supplementary Material.. Live-verified UniProtKB grounding across
    UniProtKB:Q72CI8 (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol: sat,
    TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194);
    UniProtKB:Q72DT2 (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol:
    aprA, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough,
    UP000002194); UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta
    subunit, gene_symbol: aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris
    str. Hildenborough, UP000002194); UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase,
    dissimilatory-type subunit alpha, gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882
    Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194); UniProtKB:P45575
    (DSVB_NITV2, Sulfite reductase, dissimilatory-type subunit beta, gene_symbol:
    dsvB, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough,
    UP000002194).'
  target_ids:
  - cmmmech:polydymite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: data/records/polydymite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/polydymite/2026-11-05T171248Z-marcin-0624fa.yaml
    (SHA-256 a5166f2160c430d0c3a047b6e971d55a645abb8b62c4c305a55cb23fa236b10d) and
    passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:polydymite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Polydymite (cmmmech:polydymite) passes Cycle 9 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 7090d5c378ac2c6e654608cbf6150f0a7b87287099d0db6b6bc426db9a69d4fd:
  Curated data/records/polydymite.yaml with causal_graph ''hildenborough_nickel_sulfide_formation_graph''
  (mechanism_ref: hildenborough_nickel_sulfide_formation, 4 nodes / 3 edges; dvh_sat_aprba_sulfate_activation:
  [UniProtKB:Q72CI8 (sat, Q72CI8_NITV2, UP000002194), UniProtKB:Q72DT2 (aprA, Q72DT2_NITV2,
  UP000002194), UniProtKB:Q72DT3 (aprB, Q72DT3_NITV2, UP000002194)]; dvh_dsvab_sulfite_reductase:
  [UniProtKB:P45574 (dsvA, DSVA_NITV2, UP000002194), UniProtKB:P45575 (dsvB, DSVB_NITV2,
  UP000002194)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and experimental caveats from mansor2019: Mansor et al. (2019). Biogenic
  and Abiogenic Nanoparticulate Nickel Sulfide Synthesis, Transformation and Crystal
  Growth in Aqueous Systems. Frontiers in Earth Science 7:151. (https://doi.org/10.3389/feart.2019.00151);
  mansor2019_si: Supplementary Material.. Live-verified UniProtKB reference-proteome
  grounding across UniProtKB:Q72CI8 (Q72CI8_NITV2, sulfate adenylyltransferase, gene_symbol:
  sat, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194);
  UniProtKB:Q72DT2 (Q72DT2_NITV2, Adenylyl-sulphate reductase, alpha subunit, gene_symbol:
  aprA, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194);
  UniProtKB:Q72DT3 (Q72DT3_NITV2, Adenylylsulphate reductase, beta subunit, gene_symbol:
  aprB, TREMBL, NCBITaxon:882 Nitratidesulfovibrio vulgaris str. Hildenborough, UP000002194);
  UniProtKB:P45574 (DSVA_NITV2, Sulfite reductase, dissimilatory-type subunit alpha,
  gene_symbol: dsvA, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio vulgaris str.
  Hildenborough, UP000002194); UniProtKB:P45575 (DSVB_NITV2, Sulfite reductase, dissimilatory-type
  subunit beta, gene_symbol: dsvB, SWISS_PROT, NCBITaxon:882 Nitratidesulfovibrio
  vulgaris str. Hildenborough, UP000002194).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:polydymite.
related_reviews: []
```
