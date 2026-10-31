# Cycle 6 Stage 2 causal-graphs review of Tannery sludge (cmmmech:tannery-sludge)

- Review: 20261031T053300Z-tannery-sludge-cycle6-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T05:31:00Z
- Finished UTC: 2026-10-31T05:33:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Tannery sludge (cmmmech:tannery-sludge) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d: Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) with causal_graph 'xiamen_acidophile_associated_chromium_leaching_graph' (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wang2019. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) and its canonical EDIT history sidecar(s) (history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'xiamen_acidophile_associated_chromium_leaching_graph' (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:tannery-sludge
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f017d7b4d0d62a6cccf0fffa360802bd3cf505cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tannery-sludge | data/records/tannery-sludge.yaml | maintained | Tannery sludge |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:tannery-sludge | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:tannery-sludge | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'xiamen_acidophile_associated_chromium_leaching_graph' (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])

graph: supported. Targets: cmmmech:tannery-sludge.

Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) with causal_graph 'xiamen_acidophile_associated_chromium_leaching_graph' (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wang2019. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:tannery-sludge.

data/records/tannery-sludge.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml (SHA-256 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767): Add xiamen_acidophile_associated_chromium_leaching_graph causal graph and ground xiamen_acidophile_associated_chromium_leaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9, UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/tannery-sludge.yaml; Working-tree record data/records/tannery-sludge.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) with causal_graph 'xiamen_acidophile_associated_chromium_leaching_graph' (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) wang2019. |
| primary_source | DOI:10.5004/dwt.2019.24500; wang2019: Wenhao Wang, Jianlei Gao, Yonghong Li and Jingqing Gao (2019). Enhanced Cr bioleaching efficiency from tannery sludge with Acidithiobacillus ferrooxidans and Acidithiobacillus thiooxidans. Desalination and Water Treatment 165:134–140. DOI 10.5004/dwt.2019.24500. Complete official seven-page original, Table 1, Figures 1–4 and Equations 1–8 inspected. (https://doi.org/10.5004/dwt.2019.24500) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590). Primary mechanism source(s) (wang2019: Wenhao Wang, Jianlei Gao, Yonghong Li and Jingqing Gao (2019). Enhanced Cr bioleaching efficiency from tannery sludge with Acidithiobacillus ferrooxidans and Acidithiobacillus thiooxidans. Desalination and Water Treatment 165:134–140. DOI 10.5004/dwt.2019.24500. Complete official seven-page original, Table 1, Figures 1–4 and Equations 1–8 inspected. (https://doi.org/10.5004/dwt.2019.24500)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml; Canonical EDIT history sidecar history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml | supports | Canonical EDIT history sidecar history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml (SHA-256 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767): Add xiamen_acidophile_associated_chromium_leaching_graph causal graph and ground xiamen_acidophile_associated_chromium_leaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9, UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) —  |
| validation | data/records/tannery-sludge.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/tannery-sludge.yaml and history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T053300Z-tannery-sludge-cycle6-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs review of Tannery sludge (cmmmech:tannery-sludge)
started_at: '2026-10-31T05:31:00Z'
finished_at: '2026-10-31T05:33:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/tannery-sludge.yaml
    (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) against
    UniProtKB reference proteomes and cited primary source(s) wang2019.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f017d7b4d0d62a6cccf0fffa360802bd3cf505cc
  state: working_tree
  inputs:
  - path: data/records/tannery-sludge.yaml
    sha256: 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d
    role: target
  - path: history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
    sha256: 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:tannery-sludge
  path: data/records/tannery-sludge.yaml
  label: Tannery sludge
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tannery-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/tannery-sludge.yaml
    (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d) and
    its canonical EDIT history sidecar(s) (history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''xiamen_acidophile_associated_chromium_leaching_graph''
    (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges;
    sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
    UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
    [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH,
    UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:tannery-sludge
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tannery-sludge
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/tannery-sludge.yaml
  locator: Working-tree record data/records/tannery-sludge.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d)
    with causal_graph ''xiamen_acidophile_associated_chromium_leaching_graph'' (mechanism_ref:
    xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr,
    B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590),
    UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9
    (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    wang2019.'
  snapshot_sha256: 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.5004/dwt.2019.24500
  locator: 'wang2019: Wenhao Wang, Jianlei Gao, Yonghong Li and Jingqing Gao (2019).
    Enhanced Cr bioleaching efficiency from tannery sludge with Acidithiobacillus
    ferrooxidans and Acidithiobacillus thiooxidans. Desalination and Water Treatment
    165:134–140. DOI 10.5004/dwt.2019.24500. Complete official seven-page original,
    Table 1, Figures 1–4 and Equations 1–8 inspected. (https://doi.org/10.5004/dwt.2019.24500)'
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
    (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
    Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol:
    tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol:
    tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol:
    tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).
    Primary mechanism source(s) (wang2019: Wenhao Wang, Jianlei Gao, Yonghong Li and
    Jingqing Gao (2019). Enhanced Cr bioleaching efficiency from tannery sludge with
    Acidithiobacillus ferrooxidans and Acidithiobacillus thiooxidans. Desalination
    and Water Treatment 165:134–140. DOI 10.5004/dwt.2019.24500. Complete official
    seven-page original, Table 1, Figures 1–4 and Equations 1–8 inspected. (https://doi.org/10.5004/dwt.2019.24500))
    report culture-level sulfur oxidation and leaching without single-gene sqr/tth
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
  locator: Canonical EDIT history sidecar history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
    (SHA-256 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767): Add
    xiamen_acidophile_associated_chromium_leaching_graph causal graph and ground xiamen_acidophile_associated_chromium_leaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9, UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1,
    UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — '
  snapshot_sha256: 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767
- evidence_id: validation
  kind: validation
  reference: data/records/tannery-sludge.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: data/records/tannery-sludge.yaml and history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:tannery-sludge
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
  - cmmmech:tannery-sludge
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''xiamen_acidophile_associated_chromium_leaching_graph''
    (mechanism_ref: xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges;
    sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411
    (sqr, B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
    UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
    [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH,
    UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])'
  outcome: supported
  summary: 'Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d)
    with causal_graph ''xiamen_acidophile_associated_chromium_leaching_graph'' (mechanism_ref:
    xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr,
    B7J411_ACIF2, UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590),
    UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9
    (tth, TTH_ACIF2, UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    wang2019. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
    (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
    Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol:
    tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol:
    tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol:
    tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).'
  target_ids:
  - cmmmech:tannery-sludge
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/tannery-sludge.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/tannery-sludge/2026-10-31T053146Z-marcin-92d3e4.yaml
    (SHA-256 3e3aaaccc128d7eb6adc0e4c5628888e9f06beef2493d4a41352efc45b165767): Add
    xiamen_acidophile_associated_chromium_leaching_graph causal graph and ground xiamen_acidophile_associated_chromium_leaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9, UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1,
    UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:tannery-sludge
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Tannery sludge (cmmmech:tannery-sludge) passes Cycle 6 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d:
  Curated data/records/tannery-sludge.yaml (SHA-256 39bf819461129f1df0df60aae6000f367d3f37a4944375777f6d85c58e68989d)
  with causal_graph ''xiamen_acidophile_associated_chromium_leaching_graph'' (mechanism_ref:
  xiamen_acidophile_associated_chromium_leaching, 5 nodes / 4 edges; sqr_reductase:
  [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2,
  UP000001362), UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1
  (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2,
  UP000001362), UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
  (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and caveats from primary source(s) wang2019. Live-verified UniProtKB reference-proteome
  grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol:
  AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270,
  UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative,
  gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270,
  UP000001362); UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide
  oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans
  ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide
  oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans
  ATCC 19377, UP000363590); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase,
  gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
  23270, UP000001362); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase,
  gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377,
  UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol:
  tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
