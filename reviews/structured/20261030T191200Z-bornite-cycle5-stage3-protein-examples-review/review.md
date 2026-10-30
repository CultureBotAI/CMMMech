# Cycle 5 Stage 3 protein-examples review of Bornite (cmmmech:bornite)

- Review: 20261030T191200Z-bornite-cycle5-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T19:10:00Z
- Finished UTC: 2026-10-30T19:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Bornite (cmmmech:bornite) passes Cycle 5 Stage 3 protein-examples review (scientific_review: true) at SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e: Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) across causal_graph 'ferrooxidans_associated_copper_release_graph' (mechanism_ref: ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) zhang2019. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

## Scope And Provenance

Cycle 5 Stage 3 protein-examples review of data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) and its canonical EDIT history sidecar(s) (history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml) verifying exact UniProtKB accession, proteome, organism, domain, and partial-support scope across causal_graph 'ferrooxidans_associated_copper_release_graph' (mechanism_ref: ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)).

Selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:bornite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 887cb85593a3bf412dad024896bfff8e5e5b232d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bornite | data/records/bornite.yaml | maintained | Bornite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:bornite | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:bornite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB ProteinExample grounding and parity across causal_graph 'ferrooxidans_associated_copper_release_graph' (mechanism_ref: ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))

graph: supported. Targets: cmmmech:bornite.

Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) across causal_graph 'ferrooxidans_associated_copper_release_graph' (mechanism_ref: ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) zhang2019. Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:bornite.

data/records/bornite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml (SHA-256 d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in bornite.yaml. — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/bornite.yaml; Working-tree record data/records/bornite.yaml (mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples) | supports | Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) across causal_graph 'ferrooxidans_associated_copper_release_graph' (mechanism_ref: ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit representational-grounding caveats from primary source(s) zhang2019. |
| primary_source | DOI:10.1039/C9RA03658J; zhang2019: Zhang et al. (2019). Interactions between marmatite and bornite during the oxidative dissolution process in abiotic and biotic systems. RSC Advances 9, 26609-26618. Sections 2-3, Figures 1-5 and original supplementary Table S1 and Figure S1; author-name correction cited separately. (https://doi.org/10.1039/C9RA03658J) | supports | Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992). Primary mechanism source(s) (zhang2019: Zhang et al. (2019). Interactions between marmatite and bornite during the oxidative dissolution process in abiotic and biotic systems. RSC Advances 9, 26609-26618. Sections 2-3, Figures 1-5 and original supplementary Table S1 and Figure S1; author-name correction cited separately. (https://doi.org/10.1039/C9RA03658J)) report whole-cell or culture-level sulfur/iron oxidation without gene-level sqr knockouts or proteomics; therefore supports: partial is strictly preserved on all added ProteinExample evidence items. |
| edit_history | history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml; Canonical EDIT history sidecar history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml | supports | Canonical EDIT history sidecar history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml (SHA-256 d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671): Added live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411, sqr / AFE_0267) to sqr_reductase in bornite.yaml. —  |
| validation | data/records/bornite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/bornite.yaml and history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T191200Z-bornite-cycle5-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 3 protein-examples review of Bornite (cmmmech:bornite)
started_at: '2026-10-30T19:10:00Z'
finished_at: '2026-10-30T19:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 3 ProteinExample enrichment in data/records/bornite.yaml
    (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) against
    live UniProtKB REST API metadata and cited primary source(s) zhang2019.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 887cb85593a3bf412dad024896bfff8e5e5b232d
  state: working_tree
  inputs:
  - path: data/records/bornite.yaml
    sha256: d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e
    role: target
  - path: history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
    sha256: d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:bornite
  path: data/records/bornite.yaml
  label: Bornite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bornite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
    role: canonical_history
scope:
  description: 'Cycle 5 Stage 3 protein-examples review of data/records/bornite.yaml
    (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e) and
    its canonical EDIT history sidecar(s) (history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml)
    verifying exact UniProtKB accession, proteome, organism, domain, and partial-support
    scope across causal_graph ''ferrooxidans_associated_copper_release_graph'' (mechanism_ref:
    ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362)).'
  selection: Cycle 5 Stage 3 protein_examples enrichment for cmmmech:bornite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bornite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/bornite.yaml
  locator: Working-tree record data/records/bornite.yaml (mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples)
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e)
    across causal_graph ''ferrooxidans_associated_copper_release_graph'' (mechanism_ref:
    ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples, preserving supports: partial and
    explicit representational-grounding caveats from primary source(s) zhang2019.'
  snapshot_sha256: d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1039/C9RA03658J
  locator: 'zhang2019: Zhang et al. (2019). Interactions between marmatite and bornite
    during the oxidative dissolution process in abiotic and biotic systems. RSC Advances
    9, 26609-26618. Sections 2-3, Figures 1-5 and original supplementary Table S1
    and Figure S1; author-name correction cited separately. (https://doi.org/10.1039/C9RA03658J)'
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name:
    B7J411_ACIF2, protein_name: Sulfide quinone reductase, putative, gene_symbol:
    sqr, ordered locus AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541,
    Pfam:PF07992). Primary mechanism source(s) (zhang2019: Zhang et al. (2019). Interactions
    between marmatite and bornite during the oxidative dissolution process in abiotic
    and biotic systems. RSC Advances 9, 26609-26618. Sections 2-3, Figures 1-5 and
    original supplementary Table S1 and Figure S1; author-name correction cited separately.
    (https://doi.org/10.1039/C9RA03658J)) report whole-cell or culture-level sulfur/iron
    oxidation without gene-level sqr knockouts or proteomics; therefore supports:
    partial is strictly preserved on all added ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
  locator: Canonical EDIT history sidecar history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
    (SHA-256 d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in bornite.yaml. — '
  snapshot_sha256: d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671
- evidence_id: validation
  kind: validation
  reference: data/records/bornite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T19:11:30Z'
  support: supports
  summary: data/records/bornite.yaml and history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:bornite
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
  - cmmmech:bornite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_example_grounding_and_scope
  area: graph
  topic: 'Verification of UniProtKB ProteinExample grounding and parity across causal_graph
    ''ferrooxidans_associated_copper_release_graph'' (mechanism_ref: ferrooxidans_associated_copper_release,
    sqr_reductase node grounded with UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362))'
  outcome: supported
  summary: 'Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e)
    across causal_graph ''ferrooxidans_associated_copper_release_graph'' (mechanism_ref:
    ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples, preserving supports: partial and
    explicit representational-grounding caveats from primary source(s) zhang2019.
    Live-verified UniProtKB REST API metadata for UniProtKB:B7J411 (entry_name: B7J411_ACIF2,
    protein_name: Sulfide quinone reductase, putative, gene_symbol: sqr, ordered locus
    AFE_0267, 375 aa, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
    23270, UP000001362, InterPro:IPR036188/IPR023753/IPR052541, Pfam:PF07992).'
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/bornite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/bornite/2026-10-30T191017Z-claude-72a7b7.yaml
    (SHA-256 d492a019d056c2f03976ac0d8d69e4bf37e63476214f219cdbaf3a8eccfb0671): Added
    live-verified Acidithiobacillus ferrooxidans ATCC 23270 Sqr paralog (UniProtKB:B7J411,
    sqr / AFE_0267) to sqr_reductase in bornite.yaml. — ) and passing all LinkML and
    history validation gates.'
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Bornite (cmmmech:bornite) passes Cycle 5 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e:
  Enriched data/records/bornite.yaml (SHA-256 d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e)
  across causal_graph ''ferrooxidans_associated_copper_release_graph'' (mechanism_ref:
  ferrooxidans_associated_copper_release, sqr_reductase node grounded with UniProtKB:B7J411
  (sqr, B7J411_ACIF2, UP000001362)) with 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples, preserving supports: partial and explicit
  representational-grounding caveats from primary source(s) zhang2019. Live-verified
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
