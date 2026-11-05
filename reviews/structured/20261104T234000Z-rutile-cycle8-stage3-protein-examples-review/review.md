# Cycle 8 Stage 3 protein-examples review of Rutile (cmmmech:rutile)

- Review: 20261104T234000Z-rutile-cycle8-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T23:39:00Z
- Finished UTC: 2026-11-04T23:40:00Z
- Reviewer: antigravity / cmmmech-cycle8-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Rutile (cmmmech:rutile) passes Cycle 8 Stage 3 protein-examples review (scientific_review: true) at SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1: Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) in Cycle 8 Stage 3 (protein_examples) with causal_graph 'photocatalytic_support_of_iron_cycling_graph' (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) lu2012. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 8 Stage 3 protein-examples review of data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) and its canonical EDIT history sidecar(s) (history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml) verifying UniProtKB reference-proteome grounding, node-to-mechanism protein_examples parity, and primary-source evidence fidelity across causal_graph 'photocatalytic_support_of_iron_cycling_graph' (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 8 Stage 3 protein_examples curation for cmmmech:rutile
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b07aa22901e257f188532a8bee7a658e45c5db5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:rutile | data/records/rutile.yaml | maintained | Rutile |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:rutile | Checked 683 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:rutile | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB reference-proteome ProteinExample grounding and parity across causal_graph 'photocatalytic_support_of_iron_cycling_graph' (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:rutile.

Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) in Cycle 8 Stage 3 (protein_examples) with causal_graph 'photocatalytic_support_of_iron_cycling_graph' (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) lu2012. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:rutile.

data/records/rutile.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml (SHA-256 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b): Add species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome Cyc2 ortholog (UniProtKB:A0A2W1KH68, DN052_11975) to photocatalytic_support_of_iron_cycling_graph and photocatalytic_support_of_iron_cycling — Grounded cyc2_outer_membrane_cytochrome and photocatalytic_support_of_iron_cycling to the second live-verified Acidithiobacillus ferrooxidans reference-proteome rus-operon outer-membrane Cyc2 ortholog UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, DN052_11975, 485 aa, RefSeq WP_012537628.1, UP000248886, NCBITaxon:920) alongside ATCC 23270 UniProtKB:B7JAQ7 (AFE_3153, UP000001362).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/rutile.yaml; Working-tree record data/records/rutile.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) in Cycle 8 Stage 3 (protein_examples) with causal_graph 'photocatalytic_support_of_iron_cycling_graph' (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) lu2012. |
| primary_source | DOI:10.1038/ncomms1768; lu2012: Lu A, Li Y, Jin S and colleagues (2012). Growth of non-phototrophic microorganisms using solar energy through mineral photocatalysis. Nature Communications 3:768. DOI 10.1038/ncomms1768. Complete original eight-page article, especially Figures 1, 2 and 4, Results on pages 2-5 and Methods on pages 6-7; original twelve-page Supplementary Information, especially Figure S2 and pages 5-11. (https://doi.org/10.1038/ncomms1768) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (lu2012: Lu A, Li Y, Jin S and colleagues (2012). Growth of non-phototrophic microorganisms using solar energy through mineral photocatalysis. Nature Communications 3:768. DOI 10.1038/ncomms1768. Complete original eight-page article, especially Figures 1, 2 and 4, Results on pages 2-5 and Methods on pages 6-7; original twelve-page Supplementary Information, especially Figure S2 and pages 5-11. (https://doi.org/10.1038/ncomms1768)) report culture-level iron/sulfur oxidation and mineral transformation/leaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml; Canonical EDIT history sidecar history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml | supports | Canonical EDIT history sidecar history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml (SHA-256 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b): Add species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome Cyc2 ortholog (UniProtKB:A0A2W1KH68, DN052_11975) to photocatalytic_support_of_iron_cycling_graph and photocatalytic_support_of_iron_cycling — Grounded cyc2_outer_membrane_cytochrome and photocatalytic_support_of_iron_cycling to the second live-verified Acidithiobacillus ferrooxidans reference-proteome rus-operon outer-membrane Cyc2 ortholog UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, DN052_11975, 485 aa, RefSeq WP_012537628.1, UP000248886, NCBITaxon:920) alongside ATCC 23270 UniProtKB:B7JAQ7 (AFE_3153, UP000001362). |
| validation | data/records/rutile.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/rutile.yaml and history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 8 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py; supersedes Cycle 8 Stage 2 review 20261104T223900Z-rutile-cycle8-stage2-causal-graphs-rereview.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T234000Z-rutile-cycle8-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 8 Stage 3 protein-examples review of Rutile (cmmmech:rutile)
started_at: '2026-11-04T23:39:00Z'
finished_at: '2026-11-04T23:40:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle8-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 8 Stage 3 ProteinExample enrichment in data/records/rutile.yaml
    (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) against
    live UniProtKB REST API metadata, reference proteomes, and cited primary source(s)
    lu2012.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 9b07aa22901e257f188532a8bee7a658e45c5db5
  state: working_tree
  inputs:
  - path: data/records/rutile.yaml
    sha256: c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1
    role: target
  - path: history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
    sha256: 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:rutile
  path: data/records/rutile.yaml
  label: Rutile
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rutile.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
    role: canonical_history
scope:
  description: 'Cycle 8 Stage 3 protein-examples review of data/records/rutile.yaml
    (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1) and
    its canonical EDIT history sidecar(s) (history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml)
    verifying UniProtKB reference-proteome grounding, node-to-mechanism protein_examples
    parity, and primary-source evidence fidelity across causal_graph ''photocatalytic_support_of_iron_cycling_graph''
    (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).'
  selection: Cycle 8 Stage 3 protein_examples curation for cmmmech:rutile
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:rutile
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/rutile.yaml
  locator: Working-tree record data/records/rutile.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-04T23:39:30Z'
  support: supports
  summary: 'Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1)
    in Cycle 8 Stage 3 (protein_examples) with causal_graph ''photocatalytic_support_of_iron_cycling_graph''
    (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    lu2012.'
  snapshot_sha256: c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1038/ncomms1768
  locator: 'lu2012: Lu A, Li Y, Jin S and colleagues (2012). Growth of non-phototrophic
    microorganisms using solar energy through mineral photocatalysis. Nature Communications
    3:768. DOI 10.1038/ncomms1768. Complete original eight-page article, especially
    Figures 1, 2 and 4, Results on pages 2-5 and Methods on pages 6-7; original twelve-page
    Supplementary Information, especially Figure S2 and pages 5-11. (https://doi.org/10.1038/ncomms1768)'
  accessed_at: '2026-11-04T23:39:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR,
    Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus
    ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s)
    (lu2012: Lu A, Li Y, Jin S and colleagues (2012). Growth of non-phototrophic microorganisms
    using solar energy through mineral photocatalysis. Nature Communications 3:768.
    DOI 10.1038/ncomms1768. Complete original eight-page article, especially Figures
    1, 2 and 4, Results on pages 2-5 and Methods on pages 6-7; original twelve-page
    Supplementary Information, especially Figure S2 and pages 5-11. (https://doi.org/10.1038/ncomms1768))
    report culture-level iron/sulfur oxidation and mineral transformation/leaching
    without single-gene knockouts; supports: partial is strictly preserved on all
    enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
  locator: Canonical EDIT history sidecar history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
  accessed_at: '2026-11-04T23:39:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
    (SHA-256 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b): Add
    species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome Cyc2
    ortholog (UniProtKB:A0A2W1KH68, DN052_11975) to photocatalytic_support_of_iron_cycling_graph
    and photocatalytic_support_of_iron_cycling — Grounded cyc2_outer_membrane_cytochrome
    and photocatalytic_support_of_iron_cycling to the second live-verified Acidithiobacillus
    ferrooxidans reference-proteome rus-operon outer-membrane Cyc2 ortholog UniProtKB:A0A2W1KH68
    (A0A2W1KH68_ACIFR, DN052_11975, 485 aa, RefSeq WP_012537628.1, UP000248886, NCBITaxon:920)
    alongside ATCC 23270 UniProtKB:B7JAQ7 (AFE_3153, UP000001362).'
  snapshot_sha256: 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b
- evidence_id: validation
  kind: validation
  reference: data/records/rutile.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T23:39:30Z'
  support: supports
  summary: data/records/rutile.yaml and history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 683 record(s); 0 failed.
  target_ids:
  - cmmmech:rutile
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
  - cmmmech:rutile
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of UniProtKB reference-proteome ProteinExample grounding and
    parity across causal_graph ''photocatalytic_support_of_iron_cycling_graph'' (mechanism_ref:
    photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1)
    in Cycle 8 Stage 3 (protein_examples) with causal_graph ''photocatalytic_support_of_iron_cycling_graph''
    (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    lu2012. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR,
    Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus
    ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:rutile
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/rutile.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/rutile/2026-11-04T233849Z-marcin-da6291.yaml
    (SHA-256 757367583125ea8421184ce349d6ddb77c04d763ac002307cda1f6b79523402b): Add
    species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome Cyc2
    ortholog (UniProtKB:A0A2W1KH68, DN052_11975) to photocatalytic_support_of_iron_cycling_graph
    and photocatalytic_support_of_iron_cycling — Grounded cyc2_outer_membrane_cytochrome
    and photocatalytic_support_of_iron_cycling to the second live-verified Acidithiobacillus
    ferrooxidans reference-proteome rus-operon outer-membrane Cyc2 ortholog UniProtKB:A0A2W1KH68
    (A0A2W1KH68_ACIFR, DN052_11975, 485 aa, RefSeq WP_012537628.1, UP000248886, NCBITaxon:920)
    alongside ATCC 23270 UniProtKB:B7JAQ7 (AFE_3153, UP000001362).) and passing all
    LinkML and history validation gates.'
  target_ids:
  - cmmmech:rutile
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Rutile (cmmmech:rutile) passes Cycle 8 Stage 3 protein-examples review (scientific_review:
  true) at SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1:
  Curated data/records/rutile.yaml (SHA-256 c7f002f370aff6a597e785627bc0393af0863890854af949a280975b810307d1)
  in Cycle 8 Stage 3 (protein_examples) with causal_graph ''photocatalytic_support_of_iron_cycling_graph''
  (mechanism_ref: photocatalytic_support_of_iron_cycling, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
  [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
  A0A2W1KH68_ACIFR, UP000248886)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0
  (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
  achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  lu2012. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
  (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome
  C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans,
  UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT,
  NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6
  (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 8 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py;
  supersedes Cycle 8 Stage 2 review 20261104T223900Z-rutile-cycle8-stage2-causal-graphs-rereview.
related_reviews: []
```
