# Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Atacamite (cmmmech:atacamite)

- Review: 20261110T054200Z-atacamite-cycle13-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T05:40:00Z
- Finished UTC: 2026-11-10T05:42:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Atacamite (cmmmech:atacamite) passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f: Updated data/records/atacamite.yaml with 'bassiana_oxalate_synthetic_atacamite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270). Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).

## Scope And Provenance

Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/atacamite.yaml (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f) and its canonical EDIT history sidecar (history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762)), and primary-source evidence fidelity across 'bassiana_oxalate_synthetic_atacamite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges).

Selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:atacamite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:atacamite | data/records/atacamite.yaml | maintained | Atacamite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:atacamite | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:atacamite | Checked 1529 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'bassiana_oxalate_synthetic_atacamite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges)

graph: supported. Targets: cmmmech:atacamite.

Updated data/records/atacamite.yaml (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f) with causal_graphs ('bassiana_oxalate_synthetic_atacamite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270). Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:atacamite.

data/records/atacamite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml (SHA-256 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8: Add bassiana_oxalate_synthetic_atacamite_transformation_graph causal graph and ground bassiana_associated_oxalate_formation to Beauveria bassiana reference-proteome oxalate-pathway enzymes (UniProtKB:J4UKL8, UniProtKB:J5JXL6, UniProtKB:J4KMZ7)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/atacamite.yaml; Working-tree record data/records/atacamite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/atacamite.yaml (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f) with causal_graphs ('bassiana_oxalate_synthetic_atacamite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2011.00270; joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270) | supports | Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762). Primary mechanism source (joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml; Canonical EDIT history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml | supports | Canonical EDIT history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml (SHA-256 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8): Add bassiana_oxalate_synthetic_atacamite_transformation_graph causal graph and ground bassiana_associated_oxalate_formation to Beauveria bassiana reference-proteome oxalate-pathway enzymes (UniProtKB:J4UKL8, UniProtKB:J5JXL6, UniProtKB:J4KMZ7) |
| validation | data/records/atacamite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/atacamite.yaml and history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:atacamite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T054200Z-atacamite-cycle13-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Atacamite
  (cmmmech:atacamite)
started_at: '2026-11-10T05:40:00Z'
finished_at: '2026-11-10T05:42:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 2 curation of data/records/atacamite.yaml (SHA-256
    448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f) against live
    UniProtKB grounding and cited primary source (joseph2012: Joseph et al. (2012).
    Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by
    Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012,
    eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially
    mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5
  state: working_tree
  inputs:
  - path: data/records/atacamite.yaml
    sha256: 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f
    role: target
  - path: history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
    sha256: 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:atacamite
  path: data/records/atacamite.yaml
  label: Atacamite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/atacamite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/atacamite.yaml
    (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f) and
    its canonical EDIT history sidecar (history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:J4UKL8
    (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819
    Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2,
    Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria
    bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate
    dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana
    (strain ARSEF 2860), UP000002762)), and primary-source evidence fidelity across
    ''bassiana_oxalate_synthetic_atacamite_transformation_graph'' (mechanism_ref:
    bassiana_associated_oxalate_formation, 4 nodes / 3 edges).'
  selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:atacamite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:atacamite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/atacamite.yaml
  locator: Working-tree record data/records/atacamite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Updated data/records/atacamite.yaml (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f)
    with causal_graphs (''bassiana_oxalate_synthetic_atacamite_transformation_graph''
    (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2011.00270
  locator: 'joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the
    Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology
    2:270; published 9 January 2012, eCollection 2011. Complete eight-page article,
    Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid
    assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)'
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2,
    Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819
    Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2,
    Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria
    bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate
    dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana
    (strain ARSEF 2860), UP000002762). Primary mechanism source (joseph2012: Joseph
    et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates
    Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9
    January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures
    1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3.
    (https://doi.org/10.3389/fmicb.2011.00270)) parameters and source-level caveats
    are strictly preserved on all nodes, edges, and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
  locator: Canonical EDIT history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
    (SHA-256 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8): Add
    bassiana_oxalate_synthetic_atacamite_transformation_graph causal graph and ground
    bassiana_associated_oxalate_formation to Beauveria bassiana reference-proteome
    oxalate-pathway enzymes (UniProtKB:J4UKL8, UniProtKB:J5JXL6, UniProtKB:J4KMZ7)'
  snapshot_sha256: 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8
- evidence_id: validation
  kind: validation
  reference: data/records/atacamite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: data/records/atacamite.yaml and history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:atacamite
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
  - cmmmech:atacamite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''bassiana_oxalate_synthetic_atacamite_transformation_graph'' (mechanism_ref:
    bassiana_associated_oxalate_formation, 4 nodes / 3 edges)'
  outcome: supported
  summary: 'Updated data/records/atacamite.yaml (SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f)
    with causal_graphs (''bassiana_oxalate_synthetic_atacamite_transformation_graph''
    (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges)), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from joseph2012: Joseph
    et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates
    Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9
    January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures
    1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3.
    (https://doi.org/10.3389/fmicb.2011.00270). Live-verified UniProtKB grounding
    across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol:
    BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762);
    UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309,
    TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762);
    UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393,
    TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).'
  target_ids:
  - cmmmech:atacamite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/atacamite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/atacamite/2026-11-10T054033Z-marcin-f8b342.yaml
    (SHA-256 694c137b0e5aa1d9cb17f740930b34f47f0269ce87048f86e17ec998f86167b8: Add
    bassiana_oxalate_synthetic_atacamite_transformation_graph causal graph and ground
    bassiana_associated_oxalate_formation to Beauveria bassiana reference-proteome
    oxalate-pathway enzymes (UniProtKB:J4UKL8, UniProtKB:J5JXL6, UniProtKB:J4KMZ7))
    and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:atacamite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Atacamite (cmmmech:atacamite) passes Cycle 13 Stage 2 causal_graphs review
  (scientific_review: true) at SHA-256 448a5810f2469499ba19420b5fee109cc1264b9190b9476306ee4eac8afde92f:
  Updated data/records/atacamite.yaml with ''bassiana_oxalate_synthetic_atacamite_transformation_graph''
  (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges), achieving
  100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from joseph2012:
  Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates
  Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January
  2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially
  mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270).
  Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate
  acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana
  (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase,
  gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF
  2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol:
  BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:atacamite.
related_reviews: []
```
