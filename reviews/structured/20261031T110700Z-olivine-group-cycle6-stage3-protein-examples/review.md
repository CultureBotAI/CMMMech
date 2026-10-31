# Cycle 6 Stage 3 protein_examples review of Olivine group (cmmmech:olivine-group)

- Review: 20261031T110700Z-olivine-group-cycle6-stage3-protein-examples
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T11:02:00Z
- Finished UTC: 2026-10-31T11:07:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Olivine group (cmmmech:olivine-group) passes Cycle 6 Stage 3 protein_examples review (scientific_review: true) at SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b: Add second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4, locus GOX0920) to psts_phosphate_binding. Live-verified UniProtKB metadata across UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone synthase, gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068, InterPro:IPR004305], pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein glucose dehydrogenase, gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR018391, InterPro:IPR017511, InterPro:IPR002372, InterPro:IPR011047, InterPro:IPR001479], pfam: [Pfam:PF01011]).

## Scope And Provenance

Cycle 6 Stage 3 protein_examples review of data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b) and its canonical EDIT history sidecar (history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml) verifying UniProtKB accession identity, reference-proteome grounding, InterPro/Pfam cross-reference correspondence, node/mechanism parity, and primary-source evidence fidelity across causal_graph 'gluconobacter_olivine_bioleaching_graph' (mechanism_ref: san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1 (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)]; pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase: [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]).

Selection: Cycle 6 Stage 3 protein_examples curation for cmmmech:olivine-group
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a9115e6c42e82a2294937959035366cd22788704.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:olivine-group | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:olivine-group | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of protein_examples UniProtKB accession identity, InterPro/Pfam cross-references, and node/mechanism parity across causal_graph 'gluconobacter_olivine_bioleaching_graph' (mechanism_ref: san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1 (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)]; pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase: [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)])

graph: supported. Targets: cmmmech:olivine-group.

Curated data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b) with causal_graph 'gluconobacter_olivine_bioleaching_graph' (mechanism_ref: san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1 (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)]; pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase: [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and live-verifying UniProtKB metadata across UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone synthase, gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068, InterPro:IPR004305], pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein glucose dehydrogenase, gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR018391, InterPro:IPR017511, InterPro:IPR002372, InterPro:IPR011047, InterPro:IPR001479], pfam: [Pfam:PF01011]).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:olivine-group.

data/records/olivine-group.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml (SHA-256 e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d: Add second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4, locus GOX0920) to psts_phosphate_binding) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/olivine-group.yaml; Working-tree record data/records/olivine-group.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b) with causal_graph 'gluconobacter_olivine_bioleaching_graph' (mechanism_ref: san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1 (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)]; pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase: [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) klug_2026. |
| primary_source | https://doi.org/10.1038/s41598-026-63817-0; klug_2026: Klug et al. (2026). Bioleaching of olivine and enstatite with formation of Mg-oxalate mediated by engineered Gluconobacter oxydans. Scientific Reports 16:25317. DOI 10.1038/s41598-026-63817-0; Methods, Figures 2-6 and Discussion. (https://doi.org/10.1038/s41598-026-63817-0) | supports | Live-verified UniProtKB reference-proteome and domain cross-reference grounding across UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone synthase, gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068, InterPro:IPR004305], pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein glucose dehydrogenase, gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR018391, InterPro:IPR017511, InterPro:IPR002372, InterPro:IPR011047, InterPro:IPR001479], pfam: [Pfam:PF01011]). Primary mechanism source(s) (klug_2026) support the stated organism, substrate, and partial/direct support levels on all ProteinExample evidence items. |
| edit_history | history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml; Canonical EDIT history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml | supports | Canonical EDIT history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml (SHA-256 e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d): Add second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4, locus GOX0920) to psts_phosphate_binding — Cycle 6 Stage 3 protein_examples curation: added the second Gluconobacter oxydans 621H reference-proteome (UP000006375) periplasmic phosphate-binding protein PstS paralog UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, locus GOX0920) alongside GOX0537 (UniProtKB:Q5FTI1) on node psts_phosphate_binding and mirrored both paralogs onto mechanism san_carlos_olivine_bioleaching, because the engineered strain B58 delta-pstS source does not resolve which 621H pstS locus corresponds to the deleted allele. |
| validation | data/records/olivine-group.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/olivine-group.yaml and history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T110700Z-olivine-group-cycle6-stage3-protein-examples
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 3 protein_examples review of Olivine group (cmmmech:olivine-group)
started_at: '2026-10-31T11:02:00Z'
finished_at: '2026-10-31T11:07:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying Cycle 6 Stage 3 protein_examples curation and live UniProtKB cross-reference
    synchronization in data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b)
    against live UniProtKB REST API metadata and cited primary source(s) klug_2026.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a9115e6c42e82a2294937959035366cd22788704
  state: working_tree
  inputs:
  - path: data/records/olivine-group.yaml
    sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
    role: target
  - path: history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
    sha256: e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:olivine-group
  path: data/records/olivine-group.yaml
  label: Olivine group
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 3 protein_examples review of data/records/olivine-group.yaml
    (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b) and
    its canonical EDIT history sidecar (history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml)
    verifying UniProtKB accession identity, reference-proteome grounding, InterPro/Pfam
    cross-reference correspondence, node/mechanism parity, and primary-source evidence
    fidelity across causal_graph ''gluconobacter_olivine_bioleaching_graph'' (mechanism_ref:
    san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1
    (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)];
    pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase:
    [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]).'
  selection: Cycle 6 Stage 3 protein_examples curation for cmmmech:olivine-group
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:olivine-group
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/olivine-group.yaml
  locator: Working-tree record data/records/olivine-group.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-10-31T11:06:30Z'
  support: supports
  summary: 'Curated data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b)
    with causal_graph ''gluconobacter_olivine_bioleaching_graph'' (mechanism_ref:
    san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1
    (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)];
    pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase:
    [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    preserving source-faithful support levels and caveats from primary source(s) klug_2026.'
  snapshot_sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-026-63817-0
  locator: 'klug_2026: Klug et al. (2026). Bioleaching of olivine and enstatite with
    formation of Mg-oxalate mediated by engineered Gluconobacter oxydans. Scientific
    Reports 16:25317. DOI 10.1038/s41598-026-63817-0; Methods, Figures 2-6 and Discussion.
    (https://doi.org/10.1038/s41598-026-63817-0)'
  accessed_at: '2026-10-31T11:06:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome and domain cross-reference
    grounding across UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding protein PstS,
    gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375,
    interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam:
    [Pfam:PF12849]); UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, Phosphate-binding protein PstS,
    gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375,
    interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962], pfam:
    [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone synthase,
    gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375,
    interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068, InterPro:IPR004305],
    pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein glucose dehydrogenase,
    gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375,
    interpro: [InterPro:IPR018391, InterPro:IPR017511, InterPro:IPR002372, InterPro:IPR011047,
    InterPro:IPR001479], pfam: [Pfam:PF01011]). Primary mechanism source(s) (klug_2026)
    support the stated organism, substrate, and partial/direct support levels on all
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
  locator: Canonical EDIT history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
  accessed_at: '2026-10-31T11:06:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
    (SHA-256 e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d): Add
    second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4,
    locus GOX0920) to psts_phosphate_binding — Cycle 6 Stage 3 protein_examples curation:
    added the second Gluconobacter oxydans 621H reference-proteome (UP000006375) periplasmic
    phosphate-binding protein PstS paralog UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, locus GOX0920)
    alongside GOX0537 (UniProtKB:Q5FTI1) on node psts_phosphate_binding and mirrored
    both paralogs onto mechanism san_carlos_olivine_bioleaching, because the engineered
    strain B58 delta-pstS source does not resolve which 621H pstS locus corresponds
    to the deleted allele.'
  snapshot_sha256: e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d
- evidence_id: validation
  kind: validation
  reference: data/records/olivine-group.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T11:06:30Z'
  support: supports
  summary: data/records/olivine-group.yaml and history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:olivine-group
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
  - cmmmech:olivine-group
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_uniprot_grounding
  area: graph
  topic: 'Verification of protein_examples UniProtKB accession identity, InterPro/Pfam
    cross-references, and node/mechanism parity across causal_graph ''gluconobacter_olivine_bioleaching_graph''
    (mechanism_ref: san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding:
    [UniProtKB:Q5FTI1 (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX,
    UP000006375)]; pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)];
    gdh_dehydrogenase: [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)])'
  outcome: supported
  summary: 'Curated data/records/olivine-group.yaml (SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b)
    with causal_graph ''gluconobacter_olivine_bioleaching_graph'' (mechanism_ref:
    san_carlos_olivine_bioleaching, 6 nodes / 5 edges; psts_phosphate_binding: [UniProtKB:Q5FTI1
    (pstS, Q5FTI1_GLUOX, UP000006375), UniProtKB:Q5FSF4 (pstS, Q5FSF4_GLUOX, UP000006375)];
    pqqc_synthase: [UniProtKB:Q9L3B2 (pqqC, PQQC_GLUOX, UP000006375)]; gdh_dehydrogenase:
    [UniProtKB:P27175 (gdh, DHG_GLUOX, UP000006375)]), achieving 100% parity between
    mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and
    live-verifying UniProtKB metadata across UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding
    protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans
    621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962],
    pfam: [Pfam:PF12849]); UniProtKB:Q5FSF4 (Q5FSF4_GLUOX, Phosphate-binding protein
    PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H,
    UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370, InterPro:IPR050962],
    pfam: [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone
    synthase, gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans
    621H, UP000006375, interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068,
    InterPro:IPR004305], pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein
    glucose dehydrogenase, gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter
    oxydans 621H, UP000006375, interpro: [InterPro:IPR018391, InterPro:IPR017511,
    InterPro:IPR002372, InterPro:IPR011047, InterPro:IPR001479], pfam: [Pfam:PF01011]).'
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/olivine-group.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/olivine-group/2026-10-31T110151Z-marcin-fe6f91.yaml
    (SHA-256 e3d676bd126a1b565ec0adaf12354f91fa34ac7f0038c14ae4185851b53a3d2d: Add
    second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4,
    locus GOX0920) to psts_phosphate_binding) and passing all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Olivine group (cmmmech:olivine-group) passes Cycle 6 Stage 3 protein_examples
  review (scientific_review: true) at SHA-256 b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b:
  Add second Gluconobacter oxydans 621H reference-proteome PstS paralog (UniProtKB:Q5FSF4,
  locus GOX0920) to psts_phosphate_binding. Live-verified UniProtKB metadata across
  UniProtKB:Q5FTI1 (Q5FTI1_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS,
  TREMBL, NCBITaxon:290633 Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673,
  InterPro:IPR024370, InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q5FSF4
  (Q5FSF4_GLUOX, Phosphate-binding protein PstS, gene_symbol: pstS, TREMBL, NCBITaxon:290633
  Gluconobacter oxydans 621H, UP000006375, interpro: [InterPro:IPR005673, InterPro:IPR024370,
  InterPro:IPR050962], pfam: [Pfam:PF12849]); UniProtKB:Q9L3B2 (PQQC_GLUOX, Pyrroloquinoline-quinone
  synthase, gene_symbol: pqqC, SWISS_PROT, NCBITaxon:290633 Gluconobacter oxydans
  621H, UP000006375, interpro: [InterPro:IPR016084, InterPro:IPR011845, InterPro:IPR039068,
  InterPro:IPR004305], pfam: [Pfam:PF03070]); UniProtKB:P27175 (DHG_GLUOX, Quinoprotein
  glucose dehydrogenase, gene_symbol: gdh, SWISS_PROT, NCBITaxon:290633 Gluconobacter
  oxydans 621H, UP000006375, interpro: [InterPro:IPR018391, InterPro:IPR017511, InterPro:IPR002372,
  InterPro:IPR011047, InterPro:IPR001479], pfam: [Pfam:PF01011]).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 6 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.
related_reviews: []
```
