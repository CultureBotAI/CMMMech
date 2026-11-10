# Cycle 13 Stage 3 protein_examples grounding review of Brochantite (cmmmech:brochantite)

- Review: 20261110T071000Z-brochantite-cycle13-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T07:09:00Z
- Finished UTC: 2026-11-10T07:10:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Brochantite (cmmmech:brochantite) passes Cycle 13 Stage 3 protein_examples review (scientific_review: true) at SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab: Enriched data/records/brochantite.yaml across 'bassiana_oxalate_synthetic_brochantite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); 'bassiana_oxalate_roof_coupon_patina_conversion_graph' (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270). Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).

## Scope And Provenance

Cycle 13 Stage 3 protein_examples review of data/records/brochantite.yaml (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab) and its canonical EDIT history sidecar (history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml) verifying expanded UniProtKB grounding (UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762)), 100% mechanism-to-node parity, and primary-source evidence fidelity across 'bassiana_oxalate_synthetic_brochantite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); 'bassiana_oxalate_roof_coupon_patina_conversion_graph' (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges).

Selection: Cycle 13 Stage 3 protein_examples cohort review for cmmmech:brochantite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4bdd13ae94fd62127aa6ed0d61a164f175fc4461.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:brochantite | data/records/brochantite.yaml | maintained | Brochantite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:brochantite | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:brochantite | Checked 1539 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of expanded UniProtKB protein_examples grounding and parity across 'bassiana_oxalate_synthetic_brochantite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); 'bassiana_oxalate_roof_coupon_patina_conversion_graph' (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges)

graph: supported. Targets: cmmmech:brochantite.

Enriched data/records/brochantite.yaml (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab) across 'bassiana_oxalate_synthetic_brochantite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); 'bassiana_oxalate_roof_coupon_patina_conversion_graph' (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270). Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:brochantite.

data/records/brochantite.yaml was updated with append-only history sidecar history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml (SHA-256 dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474: Add Beauveria bassiana Citrate synthase (BBA_06310, UniProtKB:J5JPA1) to both mechanisms and causal graphs in brochantite.yaml) and passes all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/brochantite.yaml; Working-tree record data/records/brochantite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/brochantite.yaml (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab) with expanded UniProtKB protein_examples across 'bassiana_oxalate_synthetic_brochantite_transformation_graph' (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); 'bassiana_oxalate_roof_coupon_patina_conversion_graph' (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), maintaining 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2011.00270; joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270) | supports | Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762). Primary mechanism source (joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012, eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml; Canonical EDIT history sidecar history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml | supports | Canonical EDIT history sidecar history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml (SHA-256 dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474): Add Beauveria bassiana Citrate synthase (BBA_06310, UniProtKB:J5JPA1) to both mechanisms and causal graphs in brochantite.yaml |
| validation | data/records/brochantite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/brochantite.yaml and history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 3 (protein_examples) for cmmmech:brochantite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T071000Z-brochantite-cycle13-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 3 protein_examples grounding review of Brochantite (cmmmech:brochantite)
started_at: '2026-11-10T07:09:00Z'
finished_at: '2026-11-10T07:10:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 3 protein_examples enrichment of data/records/brochantite.yaml
    (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab) against
    live UniProtKB grounding and cited primary source (joseph2012: Joseph et al. (2012).
    Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by
    Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012,
    eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially
    mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 4bdd13ae94fd62127aa6ed0d61a164f175fc4461
  state: working_tree
  inputs:
  - path: data/records/brochantite.yaml
    sha256: 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab
    role: target
  - path: history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
    sha256: dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:brochantite
  path: data/records/brochantite.yaml
  label: Brochantite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brochantite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 3 protein_examples review of data/records/brochantite.yaml
    (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab) and
    its canonical EDIT history sidecar (history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml)
    verifying expanded UniProtKB grounding (UniProtKB:J4UKL8 (J4UKL8_BEAB2, Oxaloacetate
    acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819 Beauveria bassiana
    (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2, Pyruvate carboxylase,
    gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF
    2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate dehydrogenase, gene_symbol:
    BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762);
    UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL,
    NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762)), 100% mechanism-to-node
    parity, and primary-source evidence fidelity across ''bassiana_oxalate_synthetic_brochantite_transformation_graph''
    (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); ''bassiana_oxalate_roof_coupon_patina_conversion_graph''
    (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges).'
  selection: Cycle 13 Stage 3 protein_examples cohort review for cmmmech:brochantite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:brochantite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/brochantite.yaml
  locator: Working-tree record data/records/brochantite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Enriched data/records/brochantite.yaml (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab)
    with expanded UniProtKB protein_examples across ''bassiana_oxalate_synthetic_brochantite_transformation_graph''
    (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); ''bassiana_oxalate_roof_coupon_patina_conversion_graph''
    (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), maintaining
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2011.00270
  locator: 'joseph2012: Joseph et al. (2012). Protection of Metal Artifacts with the
    Formation of Metal-Oxalates Complexes by Beauveria bassiana. Frontiers in Microbiology
    2:270; published 9 January 2012, eCollection 2011. Complete eight-page article,
    Table 1 and Figures 1-8, especially mineral assays in Figure 1 and separate acid
    assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270)'
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:J4UKL8 (J4UKL8_BEAB2,
    Oxaloacetate acetylhydrolase, gene_symbol: BBA_06346, TREMBL, NCBITaxon:655819
    Beauveria bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J5JXL6 (J5JXL6_BEAB2,
    Pyruvate carboxylase, gene_symbol: BBA_04309, TREMBL, NCBITaxon:655819 Beauveria
    bassiana (strain ARSEF 2860), UP000002762); UniProtKB:J4KMZ7 (J4KMZ7_BEAB2, Malate
    dehydrogenase, gene_symbol: BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana
    (strain ARSEF 2860), UP000002762); UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase,
    gene_symbol: BBA_06310, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF
    2860), UP000002762). Primary mechanism source (joseph2012: Joseph et al. (2012).
    Protection of Metal Artifacts with the Formation of Metal-Oxalates Complexes by
    Beauveria bassiana. Frontiers in Microbiology 2:270; published 9 January 2012,
    eCollection 2011. Complete eight-page article, Table 1 and Figures 1-8, especially
    mineral assays in Figure 1 and separate acid assay in Figure 3. (https://doi.org/10.3389/fmicb.2011.00270))
    parameters and source-level caveats are strictly preserved on all nodes, edges,
    and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
  locator: Canonical EDIT history sidecar history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
    (SHA-256 dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474): Add
    Beauveria bassiana Citrate synthase (BBA_06310, UniProtKB:J5JPA1) to both mechanisms
    and causal graphs in brochantite.yaml'
  snapshot_sha256: dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474
- evidence_id: validation
  kind: validation
  reference: data/records/brochantite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T07:10:00Z'
  support: supports
  summary: data/records/brochantite.yaml and history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:brochantite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1539 history record(s); 0 error(s).
  target_ids:
  - cmmmech:brochantite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_causal_graph_grounding
  area: graph
  topic: 'Verification of expanded UniProtKB protein_examples grounding and parity
    across ''bassiana_oxalate_synthetic_brochantite_transformation_graph'' (mechanism_ref:
    bassiana_associated_oxalate_formation, 4 nodes / 3 edges); ''bassiana_oxalate_roof_coupon_patina_conversion_graph''
    (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges)'
  outcome: supported
  summary: 'Enriched data/records/brochantite.yaml (SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab)
    across ''bassiana_oxalate_synthetic_brochantite_transformation_graph'' (mechanism_ref:
    bassiana_associated_oxalate_formation, 4 nodes / 3 edges); ''bassiana_oxalate_roof_coupon_patina_conversion_graph''
    (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), achieving
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
    TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762);
    UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL,
    NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).'
  target_ids:
  - cmmmech:brochantite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/brochantite.yaml was updated with append-only history sidecar
    history/records/brochantite/2026-11-10T070945Z-marcin-d9c01d.yaml (SHA-256 dfab671a8595f571b642e7aedbaa759d8e6ffd63928d569e84f29f9fd529f474:
    Add Beauveria bassiana Citrate synthase (BBA_06310, UniProtKB:J5JPA1) to both
    mechanisms and causal graphs in brochantite.yaml) and passes all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:brochantite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Brochantite (cmmmech:brochantite) passes Cycle 13 Stage 3 protein_examples
  review (scientific_review: true) at SHA-256 92708ab3c847c196ab98e053e96a4c07455b638a1564b732df9ea52407f030ab:
  Enriched data/records/brochantite.yaml across ''bassiana_oxalate_synthetic_brochantite_transformation_graph''
  (mechanism_ref: bassiana_associated_oxalate_formation, 4 nodes / 3 edges); ''bassiana_oxalate_roof_coupon_patina_conversion_graph''
  (mechanism_ref: bassiana_roof_patina_conversion, 3 nodes / 2 edges), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
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
  BBA_06393, TREMBL, NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762);
  UniProtKB:J5JPA1 (J5JPA1_BEAB2, Citrate synthase, gene_symbol: BBA_06310, TREMBL,
  NCBITaxon:655819 Beauveria bassiana (strain ARSEF 2860), UP000002762).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 3 (protein_examples) for cmmmech:brochantite.
related_reviews: []
```
