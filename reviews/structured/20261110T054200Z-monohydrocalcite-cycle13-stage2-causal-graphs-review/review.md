# Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Monohydrocalcite (cmmmech:monohydrocalcite)

- Review: 20261110T054200Z-monohydrocalcite-cycle13-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T05:40:00Z
- Finished UTC: 2026-11-10T05:42:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Monohydrocalcite (cmmmech:monohydrocalcite) passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05: Updated data/records/monohydrocalcite.yaml with 'wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph' (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from han2022: Han et al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443). Live-verified UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707).

## Scope And Provenance

Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/monohydrocalcite.yaml (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05) and its canonical EDIT history sidecar (history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707)), and primary-source evidence fidelity across 'wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph' (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges).

Selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:monohydrocalcite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:monohydrocalcite | data/records/monohydrocalcite.yaml | maintained | Monohydrocalcite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:monohydrocalcite | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:monohydrocalcite | Checked 1529 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph' (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:monohydrocalcite.

Updated data/records/monohydrocalcite.yaml (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05) with causal_graphs ('wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph' (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from han2022: Han et al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443). Live-verified UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:monohydrocalcite.

data/records/monohydrocalcite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml (SHA-256 f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e: Add wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph causal graph and ground wms2_monohydrocalcite_precipitation to congeneric Halomonas elongata reference-proteome carbonic anhydrase and deaminase entries (UniProtKB:E1VCW5, UniProtKB:E1V6X3, UniProtKB:E1VB74)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/monohydrocalcite.yaml; Working-tree record data/records/monohydrocalcite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/monohydrocalcite.yaml (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05) with causal_graphs ('wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph' (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1021/acsomega.2c02443; han2022: Han et al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443) | supports | Live-verified UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707). Primary mechanism source (han2022: Han et al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml; Canonical EDIT history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml | supports | Canonical EDIT history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml (SHA-256 f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e): Add wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph causal graph and ground wms2_monohydrocalcite_precipitation to congeneric Halomonas elongata reference-proteome carbonic anhydrase and deaminase entries (UniProtKB:E1VCW5, UniProtKB:E1V6X3, UniProtKB:E1VB74) |
| validation | data/records/monohydrocalcite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/monohydrocalcite.yaml and history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:monohydrocalcite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T054200Z-monohydrocalcite-cycle13-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Monohydrocalcite
  (cmmmech:monohydrocalcite)
started_at: '2026-11-10T05:40:00Z'
finished_at: '2026-11-10T05:42:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 2 curation of data/records/monohydrocalcite.yaml
    (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05) against
    live UniProtKB grounding and cited primary source (han2022: Han et al. (2022).
    Mineralogy of Bioprecipitate Evolution over Induction Times Mediated by Halophilic
    Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772. Sections
    2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original figure
    images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5
  state: working_tree
  inputs:
  - path: data/records/monohydrocalcite.yaml
    sha256: 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05
    role: target
  - path: history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
    sha256: f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:monohydrocalcite
  path: data/records/monohydrocalcite.yaml
  label: Monohydrocalcite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monohydrocalcite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/monohydrocalcite.yaml
    (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05) and
    its canonical EDIT history sidecar (history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:E1VCW5
    (E1VCW5_HALED, Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066
    Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9),
    UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol:
    sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581
    / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED,
    D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas
    elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707)),
    and primary-source evidence fidelity across ''wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph''
    (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges).'
  selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:monohydrocalcite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:monohydrocalcite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/monohydrocalcite.yaml
  locator: Working-tree record data/records/monohydrocalcite.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Updated data/records/monohydrocalcite.yaml (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05)
    with causal_graphs (''wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph''
    (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1021/acsomega.2c02443
  locator: 'han2022: Han et al. (2022). Mineralogy of Bioprecipitate Evolution over
    Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca Molar Ratios.
    ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures 1-10; complete
    primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443)'
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED,
    Carbonic anhydrase, gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata
    (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707);
    UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine dehydratase, gene_symbol: sdaA, TREMBL,
    NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536
    / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid
    dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066 Halomonas elongata
    (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707).
    Primary mechanism source (han2022: Han et al. (2022). Mineralogy of Bioprecipitate
    Evolution over Induction Times Mediated by Halophilic Bacteria under Various Mg/Ca
    Molar Ratios. ACS Omega 7(34):29755-29772. Sections 2-5, Tables 1-2 and Figures
    1-10; complete primary JATS text and original figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443))
    parameters and source-level caveats are strictly preserved on all nodes, edges,
    and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
  locator: Canonical EDIT history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
    (SHA-256 f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e): Add
    wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph causal graph and ground
    wms2_monohydrocalcite_precipitation to congeneric Halomonas elongata reference-proteome
    carbonic anhydrase and deaminase entries (UniProtKB:E1VCW5, UniProtKB:E1V6X3,
    UniProtKB:E1VB74)'
  snapshot_sha256: f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e
- evidence_id: validation
  kind: validation
  reference: data/records/monohydrocalcite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: data/records/monohydrocalcite.yaml and history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:monohydrocalcite
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
  - cmmmech:monohydrocalcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph'' (mechanism_ref:
    wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/monohydrocalcite.yaml (SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05)
    with causal_graphs (''wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph''
    (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from han2022: Han et
    al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated
    by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772.
    Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original
    figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443). Live-verified
    UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase,
    gene_symbol: can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173
    / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED,
    L-serine dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata
    (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707);
    UniProtKB:E1VB74 (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA,
    TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC
    15536 / NCIMB 2198 / 1H9), UP000008707).'
  target_ids:
  - cmmmech:monohydrocalcite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/monohydrocalcite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/monohydrocalcite/2026-11-10T054033Z-marcin-e1b019.yaml
    (SHA-256 f404421e2aa37a58a0c1ef81b2e8c8fbd57a4fd65feea16b1b4a3dc961ca6d6e: Add
    wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph causal graph and ground
    wms2_monohydrocalcite_precipitation to congeneric Halomonas elongata reference-proteome
    carbonic anhydrase and deaminase entries (UniProtKB:E1VCW5, UniProtKB:E1V6X3,
    UniProtKB:E1VB74)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:monohydrocalcite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Monohydrocalcite (cmmmech:monohydrocalcite) passes Cycle 13 Stage 2 causal_graphs
  review (scientific_review: true) at SHA-256 9f6d69b0a543745406e201fb87badb261740cc0146d7607397e49b834e5b6a05:
  Updated data/records/monohydrocalcite.yaml with ''wms2_halomonas_mg_ca_monohydrocalcite_precipitation_graph''
  (mechanism_ref: wms2_monohydrocalcite_precipitation, 4 nodes / 3 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from han2022:
  Han et al. (2022). Mineralogy of Bioprecipitate Evolution over Induction Times Mediated
  by Halophilic Bacteria under Various Mg/Ca Molar Ratios. ACS Omega 7(34):29755-29772.
  Sections 2-5, Tables 1-2 and Figures 1-10; complete primary JATS text and original
  figure images in PMC9435042. (https://doi.org/10.1021/acsomega.2c02443). Live-verified
  UniProtKB grounding across UniProtKB:E1VCW5 (E1VCW5_HALED, Carbonic anhydrase, gene_symbol:
  can, TREMBL, NCBITaxon:768066 Halomonas elongata (strain ATCC 33173 / DSM 2581 /
  NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1V6X3 (E1V6X3_HALED, L-serine
  dehydratase, gene_symbol: sdaA, TREMBL, NCBITaxon:768066 Halomonas elongata (strain
  ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9), UP000008707); UniProtKB:E1VB74
  (E1VB74_HALED, D-amino acid dehydrogenase, gene_symbol: dadA, TREMBL, NCBITaxon:768066
  Halomonas elongata (strain ATCC 33173 / DSM 2581 / NBRC 15536 / NCIMB 2198 / 1H9),
  UP000008707).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:monohydrocalcite.
related_reviews: []
```
