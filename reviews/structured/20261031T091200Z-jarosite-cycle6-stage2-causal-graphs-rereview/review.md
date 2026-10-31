# Cycle 6 Stage 2 causal-graphs post-remediation re-review of Jarosite (cmmmech:jarosite)

- Review: 20261031T091200Z-jarosite-cycle6-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T09:10:00Z
- Finished UTC: 2026-10-31T09:12:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Jarosite (cmmmech:jarosite) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9: Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) with causal_graph 'thiooxidans_sulfur_assisted_dissolution_graph' (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) chen2022. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) and its canonical EDIT history sidecar(s) (history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml, history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'thiooxidans_sulfur_assisted_dissolution_graph' (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:jarosite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a95666ff720f0bf09bb41f721104776318f01ee1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:jarosite | data/records/jarosite.yaml | maintained | Jarosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:jarosite | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:jarosite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'thiooxidans_sulfur_assisted_dissolution_graph' (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])

graph: supported. Targets: cmmmech:jarosite.

Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) with causal_graph 'thiooxidans_sulfur_assisted_dissolution_graph' (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) chen2022. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:jarosite.

data/records/jarosite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml (SHA-256 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99): Add thiooxidans_sulfur_assisted_dissolution_graph causal graph and ground thiooxidans_sulfur_assisted_dissolution to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ; history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml (SHA-256 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b): Remediate thiooxidans_sulfur_assisted_dissolution_graph and thiooxidans_sulfur_assisted_dissolution protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/jarosite.yaml; Working-tree record data/records/jarosite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) with causal_graph 'thiooxidans_sulfur_assisted_dissolution_graph' (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) chen2022. |
| primary_source | DOI:10.1016/j.hydromet.2022.105908; chen2022: Chen et al. (2022). Reductive dissolution of jarosite by inorganic sulfur compounds catalyzed by Acidithiobacillus thiooxidans. Hydrometallurgy 212, 105908. Complete Coventry accepted manuscript, methods sections 2.1-2.4, Table 1, Figures 1-8, and appended Supplementary Figures S1-S4. (https://doi.org/10.1016/j.hydromet.2022.105908) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590). Primary mechanism source(s) (chen2022: Chen et al. (2022). Reductive dissolution of jarosite by inorganic sulfur compounds catalyzed by Acidithiobacillus thiooxidans. Hydrometallurgy 212, 105908. Complete Coventry accepted manuscript, methods sections 2.1-2.4, Table 1, Figures 1-8, and appended Supplementary Figures S1-S4. (https://doi.org/10.1016/j.hydromet.2022.105908)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml; Canonical EDIT history sidecar history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml | supports | Canonical EDIT history sidecar history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml (SHA-256 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99): Add thiooxidans_sulfur_assisted_dissolution_graph causal graph and ground thiooxidans_sulfur_assisted_dissolution to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) —  |
| edit_history_2 | history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml; Canonical EDIT history sidecar history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml | supports | Canonical EDIT history sidecar history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml (SHA-256 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b): Remediate thiooxidans_sulfur_assisted_dissolution_graph and thiooxidans_sulfur_assisted_dissolution protein_examples to match primary-source experimental conditions, strains, and outcomes (#892) —  |
| validation | data/records/jarosite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/jarosite.yaml and history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml, history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-jarosite-cycle6-stage2-causal-graphs-review).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T091200Z-jarosite-cycle6-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs post-remediation re-review of Jarosite (cmmmech:jarosite)
started_at: '2026-10-31T09:10:00Z'
finished_at: '2026-10-31T09:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/jarosite.yaml
    (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) against
    UniProtKB reference proteomes and cited primary source(s) chen2022.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a95666ff720f0bf09bb41f721104776318f01ee1
  state: working_tree
  inputs:
  - path: data/records/jarosite.yaml
    sha256: 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9
    role: target
  - path: history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
    sha256: 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99
    role: context
  - path: history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
    sha256: 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:jarosite
  path: data/records/jarosite.yaml
  label: Jarosite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/jarosite.yaml
    (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9) and
    its canonical EDIT history sidecar(s) (history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml,
    history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml) verifying causal-graph
    node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''thiooxidans_sulfur_assisted_dissolution_graph''
    (mechanism_ref: thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1
    (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:jarosite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:jarosite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/jarosite.yaml
  locator: Working-tree record data/records/jarosite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9)
    with causal_graph ''thiooxidans_sulfur_assisted_dissolution_graph'' (mechanism_ref:
    thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    chen2022.'
  snapshot_sha256: 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1016/j.hydromet.2022.105908
  locator: 'chen2022: Chen et al. (2022). Reductive dissolution of jarosite by inorganic
    sulfur compounds catalyzed by Acidithiobacillus thiooxidans. Hydrometallurgy 212,
    105908. Complete Coventry accepted manuscript, methods sections 2.1-2.4, Table
    1, Figures 1-8, and appended Supplementary Figures S1-S4. (https://doi.org/10.1016/j.hydromet.2022.105908)'
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
    19377, UP000363590). Primary mechanism source(s) (chen2022: Chen et al. (2022).
    Reductive dissolution of jarosite by inorganic sulfur compounds catalyzed by Acidithiobacillus
    thiooxidans. Hydrometallurgy 212, 105908. Complete Coventry accepted manuscript,
    methods sections 2.1-2.4, Table 1, Figures 1-8, and appended Supplementary Figures
    S1-S4. (https://doi.org/10.1016/j.hydromet.2022.105908)) report culture-level
    sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports:
    partial is strictly preserved on all enzyme-level edges and ProteinExample evidence
    items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
  locator: Canonical EDIT history sidecar history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
    (SHA-256 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99): Add
    thiooxidans_sulfur_assisted_dissolution_graph causal graph and ground thiooxidans_sulfur_assisted_dissolution
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — '
  snapshot_sha256: 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
  locator: Canonical EDIT history sidecar history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
    (SHA-256 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b): Remediate
    thiooxidans_sulfur_assisted_dissolution_graph and thiooxidans_sulfur_assisted_dissolution
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — '
  snapshot_sha256: 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b
- evidence_id: validation
  kind: validation
  reference: data/records/jarosite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T09:11:30Z'
  support: supports
  summary: data/records/jarosite.yaml and history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml,
    history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml pass strict LinkML
    schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:jarosite
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
  - cmmmech:jarosite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''thiooxidans_sulfur_assisted_dissolution_graph'' (mechanism_ref:
    thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])'
  outcome: supported
  summary: 'Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9)
    with causal_graph ''thiooxidans_sulfur_assisted_dissolution_graph'' (mechanism_ref:
    thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
    between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    chen2022. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
    (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol:
    sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
    UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
    gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase,
    gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC
    19377, UP000363590).'
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/jarosite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/jarosite/2026-10-31T053145Z-marcin-de6e62.yaml
    (SHA-256 8f380d92e5f4f307e67fe6046e75a2e85933bf1ec9ae045f29b98fcd5ad71e99): Add
    thiooxidans_sulfur_assisted_dissolution_graph causal graph and ground thiooxidans_sulfur_assisted_dissolution
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ; history/records/jarosite/2026-10-31T090424Z-marcin-92112a.yaml
    (SHA-256 5c8f5764329d3ad77665da17df17fffe8c956111d8a5f565b310a5294031117b): Remediate
    thiooxidans_sulfur_assisted_dissolution_graph and thiooxidans_sulfur_assisted_dissolution
    protein_examples to match primary-source experimental conditions, strains, and
    outcomes (#892) — ) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Jarosite (cmmmech:jarosite) passes Cycle 6 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9:
  Curated data/records/jarosite.yaml (SHA-256 5055ddd080238ff4e0de373ffe2a56c0dec6181097c1929edf55d2807ce46ad9)
  with causal_graph ''thiooxidans_sulfur_assisted_dissolution_graph'' (mechanism_ref:
  thiooxidans_sulfur_assisted_dissolution, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
  (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
  UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
  UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  chen2022. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349
  (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr,
  TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
  UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase,
  gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377,
  UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol:
  tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590);
  UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth,
  TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 6 Stage 2 (causal_graphs) after Issue #892 remediation using
  scripts/curate_causal_graphs.py (supersedes 20261031T053300Z-jarosite-cycle6-stage2-causal-graphs-review).'
related_reviews: []
```
