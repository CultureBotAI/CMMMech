# Cycle 5 Stage 3 protein-examples review of Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate)

- Review: 20261030T191200Z-tetrahedrite-concentrate-cycle5-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T19:10:00Z
- Finished UTC: 2026-10-30T19:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate) passes Cycle 5 Stage 3 protein-examples review (scientific_review: true) at SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f: Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) across causal_graph 'ferrooxidans_tetrahedrite_bioleaching_graph' (mechanism_ref: acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) kupka_2025. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992) and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name: Sulfide quinone oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa, TREMBL, NCBITaxon:160808 Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

## Scope And Provenance

Cycle 5 Stage 3 protein-examples review of data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) and its canonical EDIT history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml) verifying exact UniProtKB accession, proteome, organism, domain, and partial-support scope across causal_graph 'ferrooxidans_tetrahedrite_bioleaching_graph' (mechanism_ref: acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925)).

Selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:tetrahedrite-concentrate
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 887cb85593a3bf412dad024896bfff8e5e5b232d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:tetrahedrite-concentrate | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:tetrahedrite-concentrate | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB ProteinExample grounding and parity across causal_graph 'ferrooxidans_tetrahedrite_bioleaching_graph' (mechanism_ref: acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925))

graph: supported. Targets: cmmmech:tetrahedrite-concentrate.

Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) across causal_graph 'ferrooxidans_tetrahedrite_bioleaching_graph' (mechanism_ref: acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) kupka_2025. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992) and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name: Sulfide quinone oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa, TREMBL, NCBITaxon:160808 Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:tetrahedrite-concentrate.

data/records/tetrahedrite-concentrate.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml (SHA-256 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e): Added live-verified Acidithiobacillus ferrooxidans Sqr (UniProtKB:B7J411, sqr / AFE_0267) and Acidithiobacillus ferrivorans Sqr2 (UniProtKB:A0A060UMZ1, sqr2 / AFERRI_20483) paralogs to sqr_reductase in tetrahedrite-concentrate.yaml. — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/tetrahedrite-concentrate.yaml; Working-tree record data/records/tetrahedrite-concentrate.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) across causal_graph 'ferrooxidans_tetrahedrite_bioleaching_graph' (mechanism_ref: acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) kupka_2025. |
| primary_source | DOI:10.1007/s40831-025-01089-0; kupka_2025: Kupka D et al. (2025). Bioleaching of Tetrahedrite by Iron- and Sulfur-Oxidizing Bacteria. Journal of Sustainable Metallurgy 11:3685-3699. DOI 10.1007/s40831-025-01089-0. Complete 15-page original article, Figures 1-8, Tables 1-2 and seven-page supplement with Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0) | supports | Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992) and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name: Sulfide quinone oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa, TREMBL, NCBITaxon:160808 Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992). Primary mechanism source(s) (kupka_2025: Kupka D et al. (2025). Bioleaching of Tetrahedrite by Iron- and Sulfur-Oxidizing Bacteria. Journal of Sustainable Metallurgy 11:3685-3699. DOI 10.1007/s40831-025-01089-0. Complete 15-page original article, Figures 1-8, Tables 1-2 and seven-page supplement with Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0)) report whole-cell or culture-level sulfur/iron oxidation without gene-level sqr knockouts or proteomics; therefore supports: partial is strictly preserved on all added ProteinExample evidence items. |
| edit_history | history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml; Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml | supports | Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml (SHA-256 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e): Added live-verified Acidithiobacillus ferrooxidans Sqr (UniProtKB:B7J411, sqr / AFE_0267) and Acidithiobacillus ferrivorans Sqr2 (UniProtKB:A0A060UMZ1, sqr2 / AFERRI_20483) paralogs to sqr_reductase in tetrahedrite-concentrate.yaml. —  |
| validation | data/records/tetrahedrite-concentrate.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/tetrahedrite-concentrate.yaml and history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T191200Z-tetrahedrite-concentrate-cycle5-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 3 protein-examples review of Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate)
started_at: '2026-10-30T19:10:00Z'
finished_at: '2026-10-30T19:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 3 ProteinExample enrichment in data/records/tetrahedrite-concentrate.yaml
    (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) against
    live UniProtKB REST API metadata and cited primary source(s) kupka_2025.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 887cb85593a3bf412dad024896bfff8e5e5b232d
  state: working_tree
  inputs:
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f
    role: target
  - path: history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
    sha256: 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:tetrahedrite-concentrate
  path: data/records/tetrahedrite-concentrate.yaml
  label: Tetrahedrite concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
    role: canonical_history
scope:
  description: 'Cycle 5 Stage 3 protein-examples review of data/records/tetrahedrite-concentrate.yaml
    (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f) and
    its canonical EDIT history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml)
    verifying exact UniProtKB accession, proteome, organism, domain, and partial-support
    scope across causal_graph ''ferrooxidans_tetrahedrite_bioleaching_graph'' (mechanism_ref:
    acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT,
    UP000193925)).'
  selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:tetrahedrite-concentrate
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tetrahedrite-concentrate
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/tetrahedrite-concentrate.yaml
  locator: Working-tree record data/records/tetrahedrite-concentrate.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f)
    across causal_graph ''ferrooxidans_tetrahedrite_bioleaching_graph'' (mechanism_ref:
    acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT,
    UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
    preserving supports: partial and explicit representational-grounding caveats from
    primary source(s) kupka_2025.'
  snapshot_sha256: 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1007/s40831-025-01089-0
  locator: 'kupka_2025: Kupka D et al. (2025). Bioleaching of Tetrahedrite by Iron-
    and Sulfur-Oxidizing Bacteria. Journal of Sustainable Metallurgy 11:3685-3699.
    DOI 10.1007/s40831-025-01089-0. Complete 15-page original article, Figures 1-8,
    Tables 1-2 and seven-page supplement with Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0)'
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name:
    B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
    sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992) and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name:
    Sulfide quinone oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa,
    TREMBL, NCBITaxon:160808 Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992). Primary mechanism source(s) (kupka_2025: Kupka D et al. (2025).
    Bioleaching of Tetrahedrite by Iron- and Sulfur-Oxidizing Bacteria. Journal of
    Sustainable Metallurgy 11:3685-3699. DOI 10.1007/s40831-025-01089-0. Complete
    15-page original article, Figures 1-8, Tables 1-2 and seven-page supplement with
    Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0)) report whole-cell
    or culture-level sulfur/iron oxidation without gene-level sqr knockouts or proteomics;
    therefore supports: partial is strictly preserved on all added ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
  locator: Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
    (SHA-256 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e): Added
    live-verified Acidithiobacillus ferrooxidans Sqr (UniProtKB:B7J411, sqr / AFE_0267)
    and Acidithiobacillus ferrivorans Sqr2 (UniProtKB:A0A060UMZ1, sqr2 / AFERRI_20483)
    paralogs to sqr_reductase in tetrahedrite-concentrate.yaml. — '
  snapshot_sha256: 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e
- evidence_id: validation
  kind: validation
  reference: data/records/tetrahedrite-concentrate.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: data/records/tetrahedrite-concentrate.yaml and history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
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
  - cmmmech:tetrahedrite-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_example_grounding_and_scope
  area: graph
  topic: 'Verification of UniProtKB ProteinExample grounding and parity across causal_graph
    ''ferrooxidans_tetrahedrite_bioleaching_graph'' (mechanism_ref: acidophile_associated_metal_mobilization,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362),
    UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT, UP000193925))'
  outcome: supported
  summary: 'Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f)
    across causal_graph ''ferrooxidans_tetrahedrite_bioleaching_graph'' (mechanism_ref:
    acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT,
    UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
    preserving supports: partial and explicit representational-grounding caveats from
    primary source(s) kupka_2025. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411
    (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative,
    gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992) and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name:
    Sulfide quinone oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa,
    TREMBL, NCBITaxon:160808 Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992).'
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/tetrahedrite-concentrate.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T191018Z-claude-d8e9c5.yaml
    (SHA-256 3c643ba9c3cf023d401fd2aa76ced9f15ea21dbe3f76f85bbe722fee02baad8e): Added
    live-verified Acidithiobacillus ferrooxidans Sqr (UniProtKB:B7J411, sqr / AFE_0267)
    and Acidithiobacillus ferrivorans Sqr2 (UniProtKB:A0A060UMZ1, sqr2 / AFERRI_20483)
    paralogs to sqr_reductase in tetrahedrite-concentrate.yaml. — ) and passing all
    LinkML and history validation gates.'
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate) passes Cycle
  5 Stage 3 protein-examples review (scientific_review: true) at SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f:
  Enriched data/records/tetrahedrite-concentrate.yaml (SHA-256 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f)
  across causal_graph ''ferrooxidans_tetrahedrite_bioleaching_graph'' (mechanism_ref:
  acidophile_associated_metal_mobilization, sqr_reductase node grounded with UniProtKB:B7J411
  (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A060UMZ1 (sqr2, A0A060UMZ1_9PROT,
  UP000193925)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
  preserving supports: partial and explicit representational-grounding caveats from
  primary source(s) kupka_2025. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411
  (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
  sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992)
  and UniProtKB:A0A060UMZ1 (entry_name: A0A060UMZ1_9PROT, protein_name: Sulfide quinone
  oxidoreductase, gene_symbol: sqr2, locus AFERRI_20483, 435 aa, TREMBL, NCBITaxon:160808
  Acidithiobacillus ferrivorans, UP000193925, InterPro:IPR036188/IPR023753/IPR052541,
  Pfam:PF07992).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.
related_reviews: []
```
