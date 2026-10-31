# Cycle 6 Stage 2 causal-graphs post-remediation re-review of Fish-bone residues (cmmmech:fish-bone-residues)

- Review: 20261031T091200Z-fish-bone-residues-cycle6-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T09:10:00Z
- Finished UTC: 2026-10-31T09:12:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fish-bone residues (cmmmech:fish-bone-residues) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761: Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) with causal_graph 'acidophile_broth_phosphorus_mobilization_graph' (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wyciszkiewicz_2017_acidophile. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) and its canonical EDIT history sidecar(s) (history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml, history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'acidophile_broth_phosphorus_mobilization_graph' (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:fish-bone-residues
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a95666ff720f0bf09bb41f721104776318f01ee1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:fish-bone-residues | data/records/fish-bone-residues.yaml | maintained | Fish-bone residues |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:fish-bone-residues | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:fish-bone-residues | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'acidophile_broth_phosphorus_mobilization_graph' (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:fish-bone-residues.

Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) with causal_graph 'acidophile_broth_phosphorus_mobilization_graph' (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wyciszkiewicz_2017_acidophile. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:fish-bone-residues.

data/records/fish-bone-residues.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml (SHA-256 f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2): Add acidophile_broth_phosphorus_mobilization_graph causal graph and ground acidophile_broth_phosphorus_mobilization to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) — ; history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml (SHA-256 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86): Remediate acidophile_broth_phosphorus_mobilization_graph and acidophile_broth_phosphorus_mobilization protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/fish-bone-residues.yaml; Working-tree record data/records/fish-bone-residues.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) with causal_graph 'acidophile_broth_phosphorus_mobilization_graph' (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wyciszkiewicz_2017_acidophile. |
| primary_source | DOI:10.3390/molecules22030473; wyciszkiewicz_2017_acidophile: Wyciszkiewicz, Saeid, Malinowski and Chojnacka (2017). Valorization of Phosphorus Secondary Raw Materials by Acidithiobacillus ferrooxidans. Molecules 22:473. DOI 10.3390/molecules22030473. Complete 13-page original publisher PDF and official JATS, Tables 1-4 and Figures 1-3 inspected; no separate supplement is announced in the inspected original. (https://doi.org/10.3390/molecules22030473) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (wyciszkiewicz_2017_acidophile: Wyciszkiewicz, Saeid, Malinowski and Chojnacka (2017). Valorization of Phosphorus Secondary Raw Materials by Acidithiobacillus ferrooxidans. Molecules 22:473. DOI 10.3390/molecules22030473. Complete 13-page original publisher PDF and official JATS, Tables 1-4 and Figures 1-3 inspected; no separate supplement is announced in the inspected original. (https://doi.org/10.3390/molecules22030473)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml; Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml | supports | Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml (SHA-256 f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2): Add acidophile_broth_phosphorus_mobilization_graph causal graph and ground acidophile_broth_phosphorus_mobilization to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) —  |
| edit_history_2 | history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml; Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml | supports | Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml (SHA-256 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86): Remediate acidophile_broth_phosphorus_mobilization_graph and acidophile_broth_phosphorus_mobilization protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) —  |
| validation | data/records/fish-bone-residues.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/fish-bone-residues.yaml and history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml, history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-fish-bone-residues-cycle6-stage2-causal-graphs-review).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T091200Z-fish-bone-residues-cycle6-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs post-remediation re-review of Fish-bone residues
  (cmmmech:fish-bone-residues)
started_at: '2026-10-31T09:10:00Z'
finished_at: '2026-10-31T09:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/fish-bone-residues.yaml
    (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) against
    UniProtKB reference proteomes and cited primary source(s) wyciszkiewicz_2017_acidophile.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a95666ff720f0bf09bb41f721104776318f01ee1
  state: working_tree
  inputs:
  - path: data/records/fish-bone-residues.yaml
    sha256: bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761
    role: target
  - path: history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
    sha256: f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2
    role: context
  - path: history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
    sha256: 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:fish-bone-residues
  path: data/records/fish-bone-residues.yaml
  label: Fish-bone residues
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fish-bone-residues.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/fish-bone-residues.yaml
    (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761) and
    its canonical EDIT history sidecar(s) (history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml,
    history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml) verifying
    causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''acidophile_broth_phosphorus_mobilization_graph''
    (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr,
    B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2,
    UP000001362)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:fish-bone-residues
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:fish-bone-residues
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/fish-bone-residues.yaml
  locator: Working-tree record data/records/fish-bone-residues.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761)
    with causal_graph ''acidophile_broth_phosphorus_mobilization_graph'' (mechanism_ref:
    acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
    (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
    tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    wyciszkiewicz_2017_acidophile.'
  snapshot_sha256: bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3390/molecules22030473
  locator: 'wyciszkiewicz_2017_acidophile: Wyciszkiewicz, Saeid, Malinowski and Chojnacka
    (2017). Valorization of Phosphorus Secondary Raw Materials by Acidithiobacillus
    ferrooxidans. Molecules 22:473. DOI 10.3390/molecules22030473. Complete 13-page
    original publisher PDF and official JATS, Tables 1-4 and Figures 1-3 inspected;
    no separate supplement is announced in the inspected original. (https://doi.org/10.3390/molecules22030473)'
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
    (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
    Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2,
    Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (wyciszkiewicz_2017_acidophile:
    Wyciszkiewicz, Saeid, Malinowski and Chojnacka (2017). Valorization of Phosphorus
    Secondary Raw Materials by Acidithiobacillus ferrooxidans. Molecules 22:473. DOI
    10.3390/molecules22030473. Complete 13-page original publisher PDF and official
    JATS, Tables 1-4 and Figures 1-3 inspected; no separate supplement is announced
    in the inspected original. (https://doi.org/10.3390/molecules22030473)) report
    culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts;
    supports: partial is strictly preserved on all enzyme-level edges and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
  locator: Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
    (SHA-256 f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2): Add
    acidophile_broth_phosphorus_mobilization_graph causal graph and ground acidophile_broth_phosphorus_mobilization
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9) — '
  snapshot_sha256: f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
  locator: Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
    (SHA-256 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86): Remediate
    acidophile_broth_phosphorus_mobilization_graph and acidophile_broth_phosphorus_mobilization
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — '
  snapshot_sha256: 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86
- evidence_id: validation
  kind: validation
  reference: data/records/fish-bone-residues.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: data/records/fish-bone-residues.yaml and history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml,
    history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml pass
    strict LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:fish-bone-residues
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
  - cmmmech:fish-bone-residues
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''acidophile_broth_phosphorus_mobilization_graph''
    (mechanism_ref: acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr,
    B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2,
    UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761)
    with causal_graph ''acidophile_broth_phosphorus_mobilization_graph'' (mechanism_ref:
    acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
    (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
    tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    wyciszkiewicz_2017_acidophile. Live-verified UniProtKB reference-proteome grounding
    across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792,
    SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol:
    sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT,
    NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:fish-bone-residues
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/fish-bone-residues.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/fish-bone-residues/2026-10-31T053146Z-marcin-7c80b9.yaml
    (SHA-256 f8b8a2a21fda93955166e8e342377bdd21d25880edff28beae7d7b1d17f8cdc2): Add
    acidophile_broth_phosphorus_mobilization_graph causal graph and ground acidophile_broth_phosphorus_mobilization
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9) — ; history/records/fish-bone-residues/2026-10-31T090429Z-marcin-5e603d.yaml
    (SHA-256 915a541b1fef75f69220c9001995e9dd726777d2079613a1b07f0514b9832c86): Remediate
    acidophile_broth_phosphorus_mobilization_graph and acidophile_broth_phosphorus_mobilization
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — ) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:fish-bone-residues
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Fish-bone residues (cmmmech:fish-bone-residues) passes Cycle 6 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761:
  Curated data/records/fish-bone-residues.yaml (SHA-256 bb2fe835aade0e44cb9fead637b222e6c9b4942b2625cc8fb38f08e721cc6761)
  with causal_graph ''acidophile_broth_phosphorus_mobilization_graph'' (mechanism_ref:
  acidophile_broth_phosphorus_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
  (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
  tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  wyciszkiewicz_2017_acidophile. Live-verified UniProtKB reference-proteome grounding
  across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792,
  SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
  UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol:
  sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
  UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT,
  NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using
  scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-fish-bone-residues-cycle6-stage2-causal-graphs-review).'
related_reviews: []
```
