# Cycle 6 Stage 3 successor protein_examples review of Hafnium (cmmmech:hafnium)

- Review: 20261031T120800Z-hafnium-cycle6-stage3-protein-examples
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T12:06:00Z
- Finished UTC: 2026-10-31T12:08:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Hafnium (cmmmech:hafnium) passes Cycle 6 Stage 3 successor protein_examples review (scientific_review: true, superseding 20261031T110700Z-hafnium-cycle6-stage3-protein-examples) at SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb: Clarify UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml provenance history (#895). Live-verified UniProtKB metadata across UniProtKB:Q50964 (Q50964_NEIGO, ABC transporter periplasmic binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:485 Neisseria gonorrhoeae, n/a, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]); UniProtKB:Q5FA17 (Q5FA17_NEIG1, Iron ABC transporter substrate-binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA 1090, UP000000535, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]).

## Scope And Provenance

Cycle 6 Stage 3 successor protein_examples review of data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb) and its canonical EDIT correction history sidecar (history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml), superseding 20261031T110700Z-hafnium-cycle6-stage3-protein-examples and verifying UniProtKB accession identity, reference-proteome grounding, EC/InterPro/Pfam cross-reference correspondence, node/mechanism parity, and primary-source evidence fidelity across causal_graph 'gonorrhoeae_fbpa_hafnium_cluster_binding_graph' (mechanism_ref: isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein: [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1, UP000000535)]).

Selection: Cycle 6 Stage 3 successor protein_examples review for cmmmech:hafnium
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f9aa5d290081014a5d337f8ab33c2fcc464646f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hafnium | data/records/hafnium.yaml | maintained | Hafnium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:hafnium | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:hafnium | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of protein_examples UniProtKB accession identity, EC/InterPro/Pfam cross-references, and node/mechanism parity across causal_graph 'gonorrhoeae_fbpa_hafnium_cluster_binding_graph' (mechanism_ref: isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein: [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1, UP000000535)])

graph: supported. Targets: cmmmech:hafnium.

Curated data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb) with causal_graph 'gonorrhoeae_fbpa_hafnium_cluster_binding_graph' (mechanism_ref: isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein: [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1, UP000000535)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and live-verifying UniProtKB metadata across UniProtKB:Q50964 (Q50964_NEIGO, ABC transporter periplasmic binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:485 Neisseria gonorrhoeae, n/a, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]); UniProtKB:Q5FA17 (Q5FA17_NEIG1, Iron ABC transporter substrate-binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA 1090, UP000000535, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]).

### Verification of canonical EDIT correction history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:hafnium.

data/records/hafnium.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml (SHA-256 df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3: Clarify UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml provenance history (#895)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/hafnium.yaml; Working-tree record data/records/hafnium.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb) with causal_graph 'gonorrhoeae_fbpa_hafnium_cluster_binding_graph' (mechanism_ref: isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein: [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1, UP000000535)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) alexeev_2003. |
| primary_source | https://doi.org/10.1038/nsb903; alexeev_2003: Alexeev et al. A novel protein-mineral interface. Nature Structural Biology 10, 297-302 (2003). DOI 10.1038/nsb903; Tables 1-2, Figures 1-3 and Methods. The publisher's correction concerns author affiliations. (https://doi.org/10.1038/nsb903) | supports | Live-verified UniProtKB reference-proteome and domain cross-reference grounding across UniProtKB:Q50964 (Q50964_NEIGO, ABC transporter periplasmic binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:485 Neisseria gonorrhoeae, n/a, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]); UniProtKB:Q5FA17 (Q5FA17_NEIG1, Iron ABC transporter substrate-binding protein, gene_symbol: fbpA, TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA 1090, UP000000535, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]). Primary mechanism source(s) (alexeev_2003) support the stated organism, substrate, and partial/direct support levels on all ProteinExample evidence items. |
| edit_history | history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml; Canonical EDIT correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml | supports | Canonical EDIT correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml (SHA-256 df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3): Clarify UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml provenance history (#895) — Appends a canonical correction session for history/records/hafnium/2026-10-31T110150Z-marcin-3be82a.yaml (#895): clarifies that the existing species-level Neisseria gonorrhoeae (NCBITaxon:485) ferric-binding periplasmic protein anchor UniProtKB:Q50964 in data/records/hafnium.yaml has uniprot_entry_name Q50964_NEIGO and review_status TREMBL (matching live UniProtKB REST API metadata), alongside the newly added Neisseria gonorrhoeae FA 1090 reference-proteome (UP000000535, NCBITaxon:242231) entry UniProtKB:Q5FA17 (Q5FA17_NEIG1, TREMBL, fbpA / NGO_0217). |
| validation | data/records/hafnium.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/hafnium.yaml and history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Successor scientific review superseding immutable bundle 20261031T110700Z-hafnium-cycle6-stage3-protein-examples after remediating independent review findings (#894/#895/#896).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T120800Z-hafnium-cycle6-stage3-protein-examples
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 3 successor protein_examples review of Hafnium (cmmmech:hafnium)
started_at: '2026-10-31T12:06:00Z'
finished_at: '2026-10-31T12:08:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying Cycle 6 Stage 3 successor protein_examples curation and provenance remediation
    (#894/#895/#896) in data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb)
    against live UniProtKB REST API metadata and cited primary source(s) alexeev_2003.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 0f9aa5d290081014a5d337f8ab33c2fcc464646f
  state: working_tree
  inputs:
  - path: data/records/hafnium.yaml
    sha256: 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb
    role: target
  - path: history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
    sha256: df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:hafnium
  path: data/records/hafnium.yaml
  label: Hafnium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hafnium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 3 successor protein_examples review of data/records/hafnium.yaml
    (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb) and
    its canonical EDIT correction history sidecar (history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml),
    superseding 20261031T110700Z-hafnium-cycle6-stage3-protein-examples and verifying
    UniProtKB accession identity, reference-proteome grounding, EC/InterPro/Pfam cross-reference
    correspondence, node/mechanism parity, and primary-source evidence fidelity across
    causal_graph ''gonorrhoeae_fbpa_hafnium_cluster_binding_graph'' (mechanism_ref:
    isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein:
    [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1,
    UP000000535)]).'
  selection: Cycle 6 Stage 3 successor protein_examples review for cmmmech:hafnium
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hafnium
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/hafnium.yaml
  locator: Working-tree record data/records/hafnium.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Curated data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb)
    with causal_graph ''gonorrhoeae_fbpa_hafnium_cluster_binding_graph'' (mechanism_ref:
    isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein:
    [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1,
    UP000000535)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) alexeev_2003.'
  snapshot_sha256: 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1038/nsb903
  locator: 'alexeev_2003: Alexeev et al. A novel protein-mineral interface. Nature
    Structural Biology 10, 297-302 (2003). DOI 10.1038/nsb903; Tables 1-2, Figures
    1-3 and Methods. The publisher''s correction concerns author affiliations. (https://doi.org/10.1038/nsb903)'
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome and domain cross-reference
    grounding across UniProtKB:Q50964 (Q50964_NEIGO, ABC transporter periplasmic binding
    protein, gene_symbol: fbpA, TREMBL, NCBITaxon:485 Neisseria gonorrhoeae, n/a,
    ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061],
    pfam: [Pfam:PF01547]); UniProtKB:Q5FA17 (Q5FA17_NEIG1, Iron ABC transporter substrate-binding
    protein, gene_symbol: fbpA, TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA
    1090, UP000000535, ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059,
    InterPro:IPR006061], pfam: [Pfam:PF01547]). Primary mechanism source(s) (alexeev_2003)
    support the stated organism, substrate, and partial/direct support levels on all
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
  locator: Canonical EDIT correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Canonical EDIT correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
    (SHA-256 df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3): Clarify
    UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml
    provenance history (#895) — Appends a canonical correction session for history/records/hafnium/2026-10-31T110150Z-marcin-3be82a.yaml
    (#895): clarifies that the existing species-level Neisseria gonorrhoeae (NCBITaxon:485)
    ferric-binding periplasmic protein anchor UniProtKB:Q50964 in data/records/hafnium.yaml
    has uniprot_entry_name Q50964_NEIGO and review_status TREMBL (matching live UniProtKB
    REST API metadata), alongside the newly added Neisseria gonorrhoeae FA 1090 reference-proteome
    (UP000000535, NCBITaxon:242231) entry UniProtKB:Q5FA17 (Q5FA17_NEIG1, TREMBL,
    fbpA / NGO_0217).'
  snapshot_sha256: df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3
- evidence_id: validation
  kind: validation
  reference: data/records/hafnium.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: data/records/hafnium.yaml and history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:hafnium
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
  - cmmmech:hafnium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_uniprot_grounding
  area: graph
  topic: 'Verification of protein_examples UniProtKB accession identity, EC/InterPro/Pfam
    cross-references, and node/mechanism parity across causal_graph ''gonorrhoeae_fbpa_hafnium_cluster_binding_graph''
    (mechanism_ref: isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein:
    [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1,
    UP000000535)])'
  outcome: supported
  summary: 'Curated data/records/hafnium.yaml (SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb)
    with causal_graph ''gonorrhoeae_fbpa_hafnium_cluster_binding_graph'' (mechanism_ref:
    isolated_fbp_hafnium_cluster_binding, 3 nodes / 2 edges; fbpa_ferric_binding_protein:
    [UniProtKB:Q50964 (fbpA, Q50964_NEIGO, n/a), UniProtKB:Q5FA17 (fbpA, Q5FA17_NEIG1,
    UP000000535)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and live-verifying UniProtKB metadata
    across UniProtKB:Q50964 (Q50964_NEIGO, ABC transporter periplasmic binding protein,
    gene_symbol: fbpA, TREMBL, NCBITaxon:485 Neisseria gonorrhoeae, n/a, ec: [], interpro:
    [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]);
    UniProtKB:Q5FA17 (Q5FA17_NEIG1, Iron ABC transporter substrate-binding protein,
    gene_symbol: fbpA, TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA 1090, UP000000535,
    ec: [], interpro: [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061],
    pfam: [Pfam:PF01547]).'
  target_ids:
  - cmmmech:hafnium
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT correction history sidecar and strict schema
    validation
  outcome: supported
  summary: 'data/records/hafnium.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only correction history sidecar history/records/hafnium/2026-10-31T120502Z-marcin-70646e.yaml
    (SHA-256 df4d3f07d0214b13c983391c39bd1a4e562b73d31b882f0c94ec9f4af9f30dc3: Clarify
    UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml
    provenance history (#895)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:hafnium
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Hafnium (cmmmech:hafnium) passes Cycle 6 Stage 3 successor protein_examples
  review (scientific_review: true, superseding 20261031T110700Z-hafnium-cycle6-stage3-protein-examples)
  at SHA-256 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb: Clarify
  UniProtKB:Q50964 entry name (Q50964_NEIGO) and review status (TREMBL) in hafnium.yaml
  provenance history (#895). Live-verified UniProtKB metadata across UniProtKB:Q50964
  (Q50964_NEIGO, ABC transporter periplasmic binding protein, gene_symbol: fbpA, TREMBL,
  NCBITaxon:485 Neisseria gonorrhoeae, n/a, ec: [], interpro: [InterPro:IPR026045,
  InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]); UniProtKB:Q5FA17
  (Q5FA17_NEIG1, Iron ABC transporter substrate-binding protein, gene_symbol: fbpA,
  TREMBL, NCBITaxon:242231 Neisseria gonorrhoeae FA 1090, UP000000535, ec: [], interpro:
  [InterPro:IPR026045, InterPro:IPR006059, InterPro:IPR006061], pfam: [Pfam:PF01547]).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Successor scientific review superseding immutable bundle 20261031T110700Z-hafnium-cycle6-stage3-protein-examples
  after remediating independent review findings (#894/#895/#896).
related_reviews: []
```
