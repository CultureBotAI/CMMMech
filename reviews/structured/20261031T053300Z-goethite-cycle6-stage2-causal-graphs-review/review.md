# Cycle 6 Stage 2 causal-graphs review of Goethite (cmmmech:goethite)

- Review: 20261031T053300Z-goethite-cycle6-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T05:31:00Z
- Finished UTC: 2026-10-31T05:33:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Goethite (cmmmech:goethite) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536: Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) with causal_graph 'sulfur_oxidizer_goethite_mobilization_graph' (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) stankovic_2024. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) and its canonical EDIT history sidecar(s) (history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'sulfur_oxidizer_goethite_mobilization_graph' (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:goethite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f017d7b4d0d62a6cccf0fffa360802bd3cf505cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:goethite | data/records/goethite.yaml | maintained | Goethite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:goethite | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:goethite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'sulfur_oxidizer_goethite_mobilization_graph' (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)])

graph: supported. Targets: cmmmech:goethite.

Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) with causal_graph 'sulfur_oxidizer_goethite_mobilization_graph' (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) stankovic_2024. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:goethite.

data/records/goethite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml (SHA-256 c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8): Add sulfur_oxidizer_goethite_mobilization_graph causal graph and ground sulfur_oxidizer_goethite_mobilization to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05, UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:F9ZNI0) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/goethite.yaml; Working-tree record data/records/goethite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) with causal_graph 'sulfur_oxidizer_goethite_mobilization_graph' (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) stankovic_2024. |
| primary_source | DOI:10.3389/fmicb.2024.1360018; stankovic_2024: Stankovic S and Schippers A (2024). Goethite dissolution by acidophilic bacteria. Frontiers in Microbiology 15:1360018. DOI 10.3389/fmicb.2024.1360018; Methods 2.1-2.3, Tables 1-2, Results 3.1 and 3.3-3.4, Figures 1-2 and 6-9, Discussion and Conclusion. Publisher PDF and Europe PMC full-text XML inspected, including rendered PDF pp3-4 and 8-10. (https://doi.org/10.3389/fmicb.2024.1360018) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135). Primary mechanism source(s) (stankovic_2024: Stankovic S and Schippers A (2024). Goethite dissolution by acidophilic bacteria. Frontiers in Microbiology 15:1360018. DOI 10.3389/fmicb.2024.1360018; Methods 2.1-2.3, Tables 1-2, Results 3.1 and 3.3-3.4, Figures 1-2 and 6-9, Discussion and Conclusion. Publisher PDF and Europe PMC full-text XML inspected, including rendered PDF pp3-4 and 8-10. (https://doi.org/10.3389/fmicb.2024.1360018)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml; Canonical EDIT history sidecar history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml | supports | Canonical EDIT history sidecar history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml (SHA-256 c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8): Add sulfur_oxidizer_goethite_mobilization_graph causal graph and ground sulfur_oxidizer_goethite_mobilization to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05, UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:F9ZNI0) —  |
| validation | data/records/goethite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/goethite.yaml and history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T053300Z-goethite-cycle6-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs review of Goethite (cmmmech:goethite)
started_at: '2026-10-31T05:31:00Z'
finished_at: '2026-10-31T05:33:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/goethite.yaml
    (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) against
    UniProtKB reference proteomes and cited primary source(s) stankovic_2024.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f017d7b4d0d62a6cccf0fffa360802bd3cf505cc
  state: working_tree
  inputs:
  - path: data/records/goethite.yaml
    sha256: 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536
    role: target
  - path: history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
    sha256: c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:goethite
  path: data/records/goethite.yaml
  label: Goethite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/goethite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/goethite.yaml
    (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536) and
    its canonical EDIT history sidecar(s) (history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''sulfur_oxidizer_goethite_mobilization_graph''
    (mechanism_ref: sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1
    (sqor, A0A5P9XUB1_ACITH, UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS,
    UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase:
    [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
    (tth, A0A5P9XS05_ACITH, UP000363590), UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS,
    UP000006135)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:goethite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:goethite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/goethite.yaml
  locator: Working-tree record data/records/goethite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536)
    with causal_graph ''sulfur_oxidizer_goethite_mobilization_graph'' (mechanism_ref:
    sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43
    (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590),
    UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    stankovic_2024.'
  snapshot_sha256: 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3389/fmicb.2024.1360018
  locator: 'stankovic_2024: Stankovic S and Schippers A (2024). Goethite dissolution
    by acidophilic bacteria. Frontiers in Microbiology 15:1360018. DOI 10.3389/fmicb.2024.1360018;
    Methods 2.1-2.3, Tables 1-2, Results 3.1 and 3.3-3.4, Figures 1-2 and 6-9, Discussion
    and Conclusion. Publisher PDF and Europe PMC full-text XML inspected, including
    rendered PDF pp3-4 and 8-10. (https://doi.org/10.3389/fmicb.2024.1360018)'
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase,
    gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative,
    gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH,
    gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135). Primary mechanism source(s) (stankovic_2024: Stankovic S and Schippers
    A (2024). Goethite dissolution by acidophilic bacteria. Frontiers in Microbiology
    15:1360018. DOI 10.3389/fmicb.2024.1360018; Methods 2.1-2.3, Tables 1-2, Results
    3.1 and 3.3-3.4, Figures 1-2 and 6-9, Discussion and Conclusion. Publisher PDF
    and Europe PMC full-text XML inspected, including rendered PDF pp3-4 and 8-10.
    (https://doi.org/10.3389/fmicb.2024.1360018)) report culture-level sulfur oxidation
    and leaching without single-gene sqr/tth knockouts; supports: partial is strictly
    preserved on all enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
  locator: Canonical EDIT history sidecar history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
    (SHA-256 c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8): Add
    sulfur_oxidizer_goethite_mobilization_graph causal graph and ground sulfur_oxidizer_goethite_mobilization
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05, UniProtKB:F9ZQD6,
    UniProtKB:F9ZN43, UniProtKB:F9ZNI0) — '
  snapshot_sha256: c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8
- evidence_id: validation
  kind: validation
  reference: data/records/goethite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: data/records/goethite.yaml and history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:goethite
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
  - cmmmech:goethite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''sulfur_oxidizer_goethite_mobilization_graph'' (mechanism_ref:
    sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43
    (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590),
    UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)])'
  outcome: supported
  summary: 'Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536)
    with causal_graph ''sulfur_oxidizer_goethite_mobilization_graph'' (mechanism_ref:
    sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43
    (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590),
    UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    stankovic_2024. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase,
    gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative,
    gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH,
    gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135).'
  target_ids:
  - cmmmech:goethite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/goethite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/goethite/2026-10-31T053145Z-marcin-b99169.yaml
    (SHA-256 c2141f059683746ec1d8f05279af5574899179baca002f8b0cbfa8c060074fc8): Add
    sulfur_oxidizer_goethite_mobilization_graph causal graph and ground sulfur_oxidizer_goethite_mobilization
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05, UniProtKB:F9ZQD6,
    UniProtKB:F9ZN43, UniProtKB:F9ZNI0) — ) and passing all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:goethite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Goethite (cmmmech:goethite) passes Cycle 6 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536:
  Curated data/records/goethite.yaml (SHA-256 0e96fdbd19f7c23812aeab4c9ba2fc445ed7123e91db82fb430bfc1740d01536)
  with causal_graph ''sulfur_oxidizer_goethite_mobilization_graph'' (mechanism_ref:
  sulfur_oxidizer_goethite_mobilization, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
  (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
  UP000363590), UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43
  (Atc_1437, F9ZN43_ACICS, UP000006135)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
  A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590),
  UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  stankovic_2024. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
  (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr,
  TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
  UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
  gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377,
  UP000363590); UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol:
  Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135);
  UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol:
  Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135);
  UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth,
  TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
  UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth,
  TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
  UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595,
  TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
