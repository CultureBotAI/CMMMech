# Cycle 5 Stage 3 protein-examples review of Realgar (cmmmech:realgar)

- Review: 20261030T191200Z-realgar-cycle5-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T19:10:00Z
- Finished UTC: 2026-10-30T19:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Realgar (cmmmech:realgar) passes Cycle 5 Stage 3 protein-examples review (scientific_review: true) at SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90: Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) across causal_graph 'by3_realgar_culture_leaching_graph' (mechanism_ref: by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) chen2012. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

## Scope And Provenance

Cycle 5 Stage 3 protein-examples review of data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) and its canonical EDIT history sidecar(s) (history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml) verifying exact UniProtKB accession, proteome, organism, domain, and partial-support scope across causal_graph 'by3_realgar_culture_leaching_graph' (mechanism_ref: by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)).

Selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:realgar
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 887cb85593a3bf412dad024896bfff8e5e5b232d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:realgar | data/records/realgar.yaml | maintained | Realgar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:realgar | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:realgar | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB ProteinExample grounding and parity across causal_graph 'by3_realgar_culture_leaching_graph' (mechanism_ref: by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))

graph: supported. Targets: cmmmech:realgar.

Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) across causal_graph 'by3_realgar_culture_leaching_graph' (mechanism_ref: by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) chen2012. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:realgar.

data/records/realgar.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml (SHA-256 cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in realgar.yaml. — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/realgar.yaml; Working-tree record data/records/realgar.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) across causal_graph 'by3_realgar_culture_leaching_graph' (mechanism_ref: by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) chen2012. |
| primary_source | DOI:10.2436/20.1501.01.154; chen2012: Chen, Yan, Wang, Li and Li (2012). Surface alteration of realgar (As4S4) by Acidithiobacillus ferrooxidans. International Microbiology 15, 9-15. Complete original; methods page 10, results pages 11-14, Figures 1-3 and Table 1. (https://doi.org/10.2436/20.1501.01.154) | supports | Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992). Primary mechanism source(s) (chen2012: Chen, Yan, Wang, Li and Li (2012). Surface alteration of realgar (As4S4) by Acidithiobacillus ferrooxidans. International Microbiology 15, 9-15. Complete original; methods page 10, results pages 11-14, Figures 1-3 and Table 1. (https://doi.org/10.2436/20.1501.01.154)) report whole-cell or culture-level sulfur/iron oxidation without gene-level sqr knockouts or proteomics; therefore supports: partial is strictly preserved on all added ProteinExample evidence items. |
| edit_history | history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml; Canonical EDIT history sidecar history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml | supports | Canonical EDIT history sidecar history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml (SHA-256 cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in realgar.yaml. —  |
| validation | data/records/realgar.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/realgar.yaml and history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T191200Z-realgar-cycle5-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 3 protein-examples review of Realgar (cmmmech:realgar)
started_at: '2026-10-30T19:10:00Z'
finished_at: '2026-10-30T19:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 3 ProteinExample enrichment in data/records/realgar.yaml
    (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) against
    live UniProtKB REST API metadata and cited primary source(s) chen2012.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 887cb85593a3bf412dad024896bfff8e5e5b232d
  state: working_tree
  inputs:
  - path: data/records/realgar.yaml
    sha256: cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90
    role: target
  - path: history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
    sha256: cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:realgar
  path: data/records/realgar.yaml
  label: Realgar
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/realgar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
    role: canonical_history
scope:
  description: 'Cycle 5 Stage 3 protein-examples review of data/records/realgar.yaml
    (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90) and
    its canonical EDIT history sidecar(s) (history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml)
    verifying exact UniProtKB accession, proteome, organism, domain, and partial-support
    scope across causal_graph ''by3_realgar_culture_leaching_graph'' (mechanism_ref:
    by3_realgar_culture_leaching, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362)).'
  selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:realgar
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:realgar
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/realgar.yaml
  locator: Working-tree record data/records/realgar.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90)
    across causal_graph ''by3_realgar_culture_leaching_graph'' (mechanism_ref: by3_realgar_culture_leaching,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))
    with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
    preserving supports: partial and explicit representational-grounding caveats from
    primary source(s) chen2012.'
  snapshot_sha256: cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.2436/20.1501.01.154
  locator: 'chen2012: Chen, Yan, Wang, Li and Li (2012). Surface alteration of realgar
    (As4S4) by Acidithiobacillus ferrooxidans. International Microbiology 15, 9-15.
    Complete original; methods page 10, results pages 11-14, Figures 1-3 and Table
    1. (https://doi.org/10.2436/20.1501.01.154)'
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name:
    B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
    sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992). Primary mechanism source(s) (chen2012: Chen, Yan, Wang, Li and
    Li (2012). Surface alteration of realgar (As4S4) by Acidithiobacillus ferrooxidans.
    International Microbiology 15, 9-15. Complete original; methods page 10, results
    pages 11-14, Figures 1-3 and Table 1. (https://doi.org/10.2436/20.1501.01.154))
    report whole-cell or culture-level sulfur/iron oxidation without gene-level sqr
    knockouts or proteomics; therefore supports: partial is strictly preserved on
    all added ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
  locator: Canonical EDIT history sidecar history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
    (SHA-256 cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in realgar.yaml. — '
  snapshot_sha256: cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5
- evidence_id: validation
  kind: validation
  reference: data/records/realgar.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: data/records/realgar.yaml and history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:realgar
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
  - cmmmech:realgar
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_example_grounding_and_scope
  area: graph
  topic: 'Verification of UniProtKB ProteinExample grounding and parity across causal_graph
    ''by3_realgar_culture_leaching_graph'' (mechanism_ref: by3_realgar_culture_leaching,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))'
  outcome: supported
  summary: 'Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90)
    across causal_graph ''by3_realgar_culture_leaching_graph'' (mechanism_ref: by3_realgar_culture_leaching,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))
    with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
    preserving supports: partial and explicit representational-grounding caveats from
    primary source(s) chen2012. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411
    (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative,
    gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992).'
  target_ids:
  - cmmmech:realgar
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/realgar.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/realgar/2026-10-30T191017Z-claude-45468b.yaml
    (SHA-256 cd02b56b2f03177c791e5b49c806c069a249524bce076b3cd89c9be1d47574d5): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in realgar.yaml. — ) and passing all LinkML and
    history validation gates.'
  target_ids:
  - cmmmech:realgar
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Realgar (cmmmech:realgar) passes Cycle 5 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90:
  Enriched data/records/realgar.yaml (SHA-256 cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90)
  across causal_graph ''by3_realgar_culture_leaching_graph'' (mechanism_ref: by3_realgar_culture_leaching,
  sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))
  with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples,
  preserving supports: partial and explicit representational-grounding caveats from
  primary source(s) chen2012. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411
  (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
  sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.
related_reviews: []
```
