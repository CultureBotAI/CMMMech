# Cycle 5 Stage 3 protein-examples review of Arsenopyrite (cmmmech:arsenopyrite)

- Review: 20261030T191200Z-arsenopyrite-cycle5-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T19:10:00Z
- Finished UTC: 2026-10-30T19:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Arsenopyrite (cmmmech:arsenopyrite) passes Cycle 5 Stage 3 protein-examples review (scientific_review: true) at SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f: Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) across causal_graph 'ferrooxidans_arsenic_release_and_surface_films_graph' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) liu2019. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

## Scope And Provenance

Cycle 5 Stage 3 protein-examples review of data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) and its canonical EDIT history sidecar(s) (history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml) verifying exact UniProtKB accession, proteome, organism, domain, and partial-support scope across causal_graph 'ferrooxidans_arsenic_release_and_surface_films_graph' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)).

Selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:arsenopyrite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 887cb85593a3bf412dad024896bfff8e5e5b232d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:arsenopyrite | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:arsenopyrite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB ProteinExample grounding and parity across causal_graph 'ferrooxidans_arsenic_release_and_surface_films_graph' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))

graph: supported. Targets: cmmmech:arsenopyrite.

Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) across causal_graph 'ferrooxidans_arsenic_release_and_surface_films_graph' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) liu2019. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:arsenopyrite.

data/records/arsenopyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml (SHA-256 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in arsenopyrite.yaml. — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/arsenopyrite.yaml; Working-tree record data/records/arsenopyrite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) across causal_graph 'ferrooxidans_arsenic_release_and_surface_films_graph' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) liu2019. |
| primary_source | DOI:10.3390/met9121320; liu2019: Liu, Li, Zhang, Yang, Xu and Jiang (2019). Formation Process of the Passivating Products from Arsenopyrite Bioleaching by Acidithiobacillus ferrooxidans in 9K Culture Medium. Metals 9(12), 1320. Complete publisher PDF and XML; sections 2-4, Figures 1-6, Tables 1-2 and Appendix A. (https://doi.org/10.3390/met9121320) | supports | Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992). Primary mechanism source(s) (liu2019: Liu, Li, Zhang, Yang, Xu and Jiang (2019). Formation Process of the Passivating Products from Arsenopyrite Bioleaching by Acidithiobacillus ferrooxidans in 9K Culture Medium. Metals 9(12), 1320. Complete publisher PDF and XML; sections 2-4, Figures 1-6, Tables 1-2 and Appendix A. (https://doi.org/10.3390/met9121320)) report whole-cell or culture-level sulfur/iron oxidation without gene-level sqr knockouts or proteomics; therefore supports: partial is strictly preserved on all added ProteinExample evidence items. |
| edit_history | history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml; Canonical EDIT history sidecar history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml | supports | Canonical EDIT history sidecar history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml (SHA-256 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in arsenopyrite.yaml. —  |
| validation | data/records/arsenopyrite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/arsenopyrite.yaml and history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T191200Z-arsenopyrite-cycle5-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 3 protein-examples review of Arsenopyrite (cmmmech:arsenopyrite)
started_at: '2026-10-30T19:10:00Z'
finished_at: '2026-10-30T19:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 3 ProteinExample enrichment in data/records/arsenopyrite.yaml
    (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) against
    live UniProtKB REST API metadata and cited primary source(s) liu2019.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 887cb85593a3bf412dad024896bfff8e5e5b232d
  state: working_tree
  inputs:
  - path: data/records/arsenopyrite.yaml
    sha256: b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f
    role: target
  - path: history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
    sha256: 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:arsenopyrite
  path: data/records/arsenopyrite.yaml
  label: Arsenopyrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenopyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
    role: canonical_history
scope:
  description: 'Cycle 5 Stage 3 protein-examples review of data/records/arsenopyrite.yaml
    (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f) and
    its canonical EDIT history sidecar(s) (history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml)
    verifying exact UniProtKB accession, proteome, organism, domain, and partial-support
    scope across causal_graph ''ferrooxidans_arsenic_release_and_surface_films_graph''
    (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films, sqr_reductase
    node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)).'
  selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:arsenopyrite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:arsenopyrite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/arsenopyrite.yaml
  locator: Working-tree record data/records/arsenopyrite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f)
    across causal_graph ''ferrooxidans_arsenic_release_and_surface_films_graph'' (mechanism_ref:
    ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with
    UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples, preserving supports: partial and
    explicit representational-grounding caveats from primary source(s) liu2019.'
  snapshot_sha256: b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3390/met9121320
  locator: 'liu2019: Liu, Li, Zhang, Yang, Xu and Jiang (2019). Formation Process
    of the Passivating Products from Arsenopyrite Bioleaching by Acidithiobacillus
    ferrooxidans in 9K Culture Medium. Metals 9(12), 1320. Complete publisher PDF
    and XML; sections 2-4, Figures 1-6, Tables 1-2 and Appendix A. (https://doi.org/10.3390/met9121320)'
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name:
    B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
    sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992). Primary mechanism source(s) (liu2019: Liu, Li, Zhang, Yang, Xu
    and Jiang (2019). Formation Process of the Passivating Products from Arsenopyrite
    Bioleaching by Acidithiobacillus ferrooxidans in 9K Culture Medium. Metals 9(12),
    1320. Complete publisher PDF and XML; sections 2-4, Figures 1-6, Tables 1-2 and
    Appendix A. (https://doi.org/10.3390/met9121320)) report whole-cell or culture-level
    sulfur/iron oxidation without gene-level sqr knockouts or proteomics; therefore
    supports: partial is strictly preserved on all added ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
  locator: Canonical EDIT history sidecar history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
    (SHA-256 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in arsenopyrite.yaml. — '
  snapshot_sha256: 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2
- evidence_id: validation
  kind: validation
  reference: data/records/arsenopyrite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: data/records/arsenopyrite.yaml and history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:arsenopyrite
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
  - cmmmech:arsenopyrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_example_grounding_and_scope
  area: graph
  topic: 'Verification of UniProtKB ProteinExample grounding and parity across causal_graph
    ''ferrooxidans_arsenic_release_and_surface_films_graph'' (mechanism_ref: ferrooxidans_arsenic_release_and_surface_films,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))'
  outcome: supported
  summary: 'Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f)
    across causal_graph ''ferrooxidans_arsenic_release_and_surface_films_graph'' (mechanism_ref:
    ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with
    UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples, preserving supports: partial and
    explicit representational-grounding caveats from primary source(s) liu2019. Live-verified
    UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name:
    Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267,
    375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362,
    InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).'
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/arsenopyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/arsenopyrite/2026-10-30T191016Z-claude-36a701.yaml
    (SHA-256 8402128231522599e48698781f93cab0a9663f0f7b9e6bb992cbf8b1a8347db2): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in arsenopyrite.yaml. — ) and passing all LinkML
    and history validation gates.'
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Arsenopyrite (cmmmech:arsenopyrite) passes Cycle 5 Stage 3 protein-examples
  review (scientific_review: true) at SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f:
  Enriched data/records/arsenopyrite.yaml (SHA-256 b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f)
  across causal_graph ''ferrooxidans_arsenic_release_and_surface_films_graph'' (mechanism_ref:
  ferrooxidans_arsenic_release_and_surface_films, sqr_reductase node grounded with
  UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit
  representational-grounding caveats from primary source(s) liu2019. Live-verified
  UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name:
  Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375
  aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362,
  InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.
related_reviews: []
```
