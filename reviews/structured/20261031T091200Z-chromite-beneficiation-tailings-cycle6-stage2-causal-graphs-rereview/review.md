# Cycle 6 Stage 2 causal-graphs post-remediation re-review of Chromite beneficiation tailings (cmmmech:chromite-beneficiation-tailings)

- Review: 20261031T091200Z-chromite-beneficiation-tailings-cycle6-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T09:10:00Z
- Finished UTC: 2026-10-31T09:12:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chromite beneficiation tailings (cmmmech:chromite-beneficiation-tailings) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a: Curated data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) with causal_graph 'thiooxidans_acid_associated_leaching_graph' (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) bolanos2018, bolanos2018_supplement. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) and its canonical EDIT history sidecar(s) (history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml, history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'thiooxidans_acid_associated_leaching_graph' (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:chromite-beneficiation-tailings
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a95666ff720f0bf09bb41f721104776318f01ee1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chromite-beneficiation-tailings | data/records/chromite-beneficiation-tailings.yaml | maintained | Chromite beneficiation tailings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:chromite-beneficiation-tailings | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:chromite-beneficiation-tailings | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'thiooxidans_acid_associated_leaching_graph' (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])

graph: supported. Targets: cmmmech:chromite-beneficiation-tailings.

Curated data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) with causal_graph 'thiooxidans_acid_associated_leaching_graph' (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) bolanos2018, bolanos2018_supplement. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:chromite-beneficiation-tailings.

data/records/chromite-beneficiation-tailings.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml (SHA-256 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba): Add thiooxidans_acid_associated_leaching_graph causal graph and ground thiooxidans_acid_associated_leaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ; history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml (SHA-256 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80): Remediate thiooxidans_acid_associated_leaching_graph and thiooxidans_acid_associated_leaching protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/chromite-beneficiation-tailings.yaml; Working-tree record data/records/chromite-beneficiation-tailings.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) with causal_graph 'thiooxidans_acid_associated_leaching_graph' (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) bolanos2018, bolanos2018_supplement. |
| primary_source | DOI:10.3390/min8060261; bolanos2018: Bolaños-Benítez, van Hullebusch, Lens, Quantin, van de Vossenberg, Subramanian and Sivry (2018). (Bio)leaching Behavior of Chromite Tailings. Minerals 8(6):261, published 20 June 2018. DOI 10.3390/min8060261. Complete 23-page primary; Sections 2-4, Tables 1-2 and Figures 1-8. (https://doi.org/10.3390/min8060261); bolanos2018_supplement: Supplementary Materials to Bolaños-Benítez et al. (2018), (Bio)leaching Behavior of Chromite Tailings. Original seven-page publisher PDF, final page blank; Figures S1-S5 and Tables S1-S3. Tables S1-S3 are visual MINTEQ calculations, not measured product speciation or mineral recovery. (https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590). Primary mechanism source(s) (bolanos2018: Bolaños-Benítez, van Hullebusch, Lens, Quantin, van de Vossenberg, Subramanian and Sivry (2018). (Bio)leaching Behavior of Chromite Tailings. Minerals 8(6):261, published 20 June 2018. DOI 10.3390/min8060261. Complete 23-page primary; Sections 2-4, Tables 1-2 and Figures 1-8. (https://doi.org/10.3390/min8060261); bolanos2018_supplement: Supplementary Materials to Bolaños-Benítez et al. (2018), (Bio)leaching Behavior of Chromite Tailings. Original seven-page publisher PDF, final page blank; Figures S1-S5 and Tables S1-S3. Tables S1-S3 are visual MINTEQ calculations, not measured product speciation or mineral recovery. (https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml; Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml | supports | Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml (SHA-256 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba): Add thiooxidans_acid_associated_leaching_graph causal graph and ground thiooxidans_acid_associated_leaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) —  |
| edit_history_2 | history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml; Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml | supports | Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml (SHA-256 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80): Remediate thiooxidans_acid_associated_leaching_graph and thiooxidans_acid_associated_leaching protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) —  |
| validation | data/records/chromite-beneficiation-tailings.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/chromite-beneficiation-tailings.yaml and history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml, history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-chromite-beneficiation-tailings-cycle6-stage2-causal-graphs-review).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T091200Z-chromite-beneficiation-tailings-cycle6-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs post-remediation re-review of Chromite beneficiation
  tailings (cmmmech:chromite-beneficiation-tailings)
started_at: '2026-10-31T09:10:00Z'
finished_at: '2026-10-31T09:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/chromite-beneficiation-tailings.yaml
    (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) against
    UniProtKB reference proteomes and cited primary source(s) bolanos2018, bolanos2018_supplement.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a95666ff720f0bf09bb41f721104776318f01ee1
  state: working_tree
  inputs:
  - path: data/records/chromite-beneficiation-tailings.yaml
    sha256: 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a
    role: target
  - path: history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
    sha256: 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba
    role: context
  - path: history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
    sha256: 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:chromite-beneficiation-tailings
  path: data/records/chromite-beneficiation-tailings.yaml
  label: Chromite beneficiation tailings
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite-beneficiation-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/chromite-beneficiation-tailings.yaml
    (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) and
    its canonical EDIT history sidecar(s) (history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml,
    history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''thiooxidans_acid_associated_leaching_graph''
    (mechanism_ref: thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1
    (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:chromite-beneficiation-tailings
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chromite-beneficiation-tailings
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/chromite-beneficiation-tailings.yaml
  locator: Working-tree record data/records/chromite-beneficiation-tailings.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Curated data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a)
    with causal_graph ''thiooxidans_acid_associated_leaching_graph'' (mechanism_ref:
    thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    bolanos2018, bolanos2018_supplement.'
  snapshot_sha256: 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3390/min8060261
  locator: 'bolanos2018: Bolaños-Benítez, van Hullebusch, Lens, Quantin, van de Vossenberg,
    Subramanian and Sivry (2018). (Bio)leaching Behavior of Chromite Tailings. Minerals
    8(6):261, published 20 June 2018. DOI 10.3390/min8060261. Complete 23-page primary;
    Sections 2-4, Tables 1-2 and Figures 1-8. (https://doi.org/10.3390/min8060261);
    bolanos2018_supplement: Supplementary Materials to Bolaños-Benítez et al. (2018),
    (Bio)leaching Behavior of Chromite Tailings. Original seven-page publisher PDF,
    final page blank; Figures S1-S5 and Tables S1-S3. Tables S1-S3 are visual MINTEQ
    calculations, not measured product speciation or mineral recovery. (https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf)'
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590). Primary mechanism source(s) (bolanos2018: Bolaños-Benítez,
    van Hullebusch, Lens, Quantin, van de Vossenberg, Subramanian and Sivry (2018).
    (Bio)leaching Behavior of Chromite Tailings. Minerals 8(6):261, published 20 June
    2018. DOI 10.3390/min8060261. Complete 23-page primary; Sections 2-4, Tables 1-2
    and Figures 1-8. (https://doi.org/10.3390/min8060261); bolanos2018_supplement:
    Supplementary Materials to Bolaños-Benítez et al. (2018), (Bio)leaching Behavior
    of Chromite Tailings. Original seven-page publisher PDF, final page blank; Figures
    S1-S5 and Tables S1-S3. Tables S1-S3 are visual MINTEQ calculations, not measured
    product speciation or mineral recovery. (https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf))
    report culture-level sulfur oxidation and leaching without single-gene sqr/tth
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
  locator: Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
    (SHA-256 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba): Add
    thiooxidans_acid_associated_leaching_graph causal graph and ground thiooxidans_acid_associated_leaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — '
  snapshot_sha256: 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
  locator: Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
    (SHA-256 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80): Remediate
    thiooxidans_acid_associated_leaching_graph and thiooxidans_acid_associated_leaching
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — '
  snapshot_sha256: 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80
- evidence_id: validation
  kind: validation
  reference: data/records/chromite-beneficiation-tailings.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: data/records/chromite-beneficiation-tailings.yaml and history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml,
    history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
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
  - cmmmech:chromite-beneficiation-tailings
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''thiooxidans_acid_associated_leaching_graph'' (mechanism_ref:
    thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])'
  outcome: supported
  summary: 'Curated data/records/chromite-beneficiation-tailings.yaml (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a)
    with causal_graph ''thiooxidans_acid_associated_leaching_graph'' (mechanism_ref:
    thiooxidans_acid_associated_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    bolanos2018, bolanos2018_supplement. Live-verified UniProtKB reference-proteome
    grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide
    oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans
    ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide
    oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus
    thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH,
    Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus
    thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH,
    Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus
    thiooxidans ATCC 19377, UP000363590).'
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/chromite-beneficiation-tailings.yaml was updated exclusively
    through scripts/curate_causal_graphs.py (curate_record_file), producing append-only
    history sidecar(s) (history/records/chromite-beneficiation-tailings/2026-10-31T053145Z-marcin-a9df10.yaml
    (SHA-256 69852e063b75af04e5d5c7e2b43d70aff20a397f1a47c498946116d097832dba): Add
    thiooxidans_acid_associated_leaching_graph causal graph and ground thiooxidans_acid_associated_leaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ; history/records/chromite-beneficiation-tailings/2026-10-31T090424Z-marcin-008637.yaml
    (SHA-256 6f7592c61593ad89e8a39dab63f37fac9509470f1124b9eeabacdf3b2a190f80): Remediate
    thiooxidans_acid_associated_leaching_graph and thiooxidans_acid_associated_leaching
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — ) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Chromite beneficiation tailings (cmmmech:chromite-beneficiation-tailings)
  passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256
  91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a: Curated data/records/chromite-beneficiation-tailings.yaml
  (SHA-256 91a68a7aa94cad9282cd34d638ea4d7061e2b0f847e92499dddf9aee0e90b83a) with
  causal_graph ''thiooxidans_acid_associated_leaching_graph'' (mechanism_ref: thiooxidans_acid_associated_leaching,
  5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
  UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
  [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
  (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and caveats from primary source(s) bolanos2018, bolanos2018_supplement. Live-verified
  UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH,
  Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390
  Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH,
  Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390
  Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH,
  Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus
  thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate
  hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans
  ATCC 19377, UP000363590).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using
  scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-chromite-beneficiation-tailings-cycle6-stage2-causal-graphs-review).'
related_reviews: []
```
