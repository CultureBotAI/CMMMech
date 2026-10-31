# Cycle 6 Stage 2 causal-graphs review of Nickel (cmmmech:nickel)

- Review: 20261031T053300Z-nickel-cycle6-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T05:31:00Z
- Finished UTC: 2026-10-31T05:33:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nickel (cmmmech:nickel) passes Cycle 6 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d: Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) with causal_graph 'thiooxidans_laterite_bioleaching_graph' (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hetz_schippers_2025. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

## Scope And Provenance

Cycle 6 Stage 2 causal-graphs review of data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) and its canonical EDIT history sidecar(s) (history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'thiooxidans_laterite_bioleaching_graph' (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).

Selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:nickel
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f017d7b4d0d62a6cccf0fffa360802bd3cf505cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:nickel | data/records/nickel.yaml | maintained | Nickel |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:nickel | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:nickel | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'thiooxidans_laterite_bioleaching_graph' (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])

graph: supported. Targets: cmmmech:nickel.

Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) with causal_graph 'thiooxidans_laterite_bioleaching_graph' (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hetz_schippers_2025. Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:nickel.

data/records/nickel.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml (SHA-256 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459): Add thiooxidans_laterite_bioleaching_graph causal graph and ground thiooxidans_laterite_bioleaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/nickel.yaml; Working-tree record data/records/nickel.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) with causal_graph 'thiooxidans_laterite_bioleaching_graph' (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hetz_schippers_2025. |
| primary_source | DOI:10.1007/s40831-025-01139-7; hetz_schippers_2025: Hetz SA and Schippers A (2025). Aerobic Bioleaching of Six Brazilian Laterite Ores with Acidithiobacillus thiooxidans, Sulfobacillus species and Archaea at Various Conditions. Journal of Sustainable Metallurgy 11:3732-3747. doi:10.1007/s40831-025-01139-7. (https://doi.org/10.1007/s40831-025-01139-7) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH, Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH, Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus thiooxidans ATCC 19377, UP000363590). Primary mechanism source(s) (hetz_schippers_2025: Hetz SA and Schippers A (2025). Aerobic Bioleaching of Six Brazilian Laterite Ores with Acidithiobacillus thiooxidans, Sulfobacillus species and Archaea at Various Conditions. Journal of Sustainable Metallurgy 11:3732-3747. doi:10.1007/s40831-025-01139-7. (https://doi.org/10.1007/s40831-025-01139-7)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml; Canonical EDIT history sidecar history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml | supports | Canonical EDIT history sidecar history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml (SHA-256 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459): Add thiooxidans_laterite_bioleaching_graph causal graph and ground thiooxidans_laterite_bioleaching to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349, UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) —  |
| validation | data/records/nickel.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/nickel.yaml and history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T053300Z-nickel-cycle6-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 2 causal-graphs review of Nickel (cmmmech:nickel)
started_at: '2026-10-31T05:31:00Z'
finished_at: '2026-10-31T05:33:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 6 Stage 2 causal_graphs and ProteinExample curation in data/records/nickel.yaml
    (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) against
    UniProtKB reference proteomes and cited primary source(s) hetz_schippers_2025.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f017d7b4d0d62a6cccf0fffa360802bd3cf505cc
  state: working_tree
  inputs:
  - path: data/records/nickel.yaml
    sha256: cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d
    role: target
  - path: history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
    sha256: 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:nickel
  path: data/records/nickel.yaml
  label: Nickel
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 2 causal-graphs review of data/records/nickel.yaml (SHA-256
    cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d) and its canonical
    EDIT history sidecar(s) (history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''thiooxidans_laterite_bioleaching_graph''
    (mechanism_ref: thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1
    (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth,
    A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)]).'
  selection: Cycle 6 Stage 2 causal_graphs curation for cmmmech:nickel
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:nickel
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/nickel.yaml
  locator: Working-tree record data/records/nickel.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d)
    with causal_graph ''thiooxidans_laterite_bioleaching_graph'' (mechanism_ref: thiooxidans_laterite_bioleaching,
    5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
    UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
    [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
    (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) hetz_schippers_2025.'
  snapshot_sha256: cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1007/s40831-025-01139-7
  locator: 'hetz_schippers_2025: Hetz SA and Schippers A (2025). Aerobic Bioleaching
    of Six Brazilian Laterite Ores with Acidithiobacillus thiooxidans, Sulfobacillus
    species and Archaea at Various Conditions. Journal of Sustainable Metallurgy 11:3732-3747.
    doi:10.1007/s40831-025-01139-7. (https://doi.org/10.1007/s40831-025-01139-7)'
  accessed_at: '2026-10-31T05:32:30Z'
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
    19377, UP000363590). Primary mechanism source(s) (hetz_schippers_2025: Hetz SA
    and Schippers A (2025). Aerobic Bioleaching of Six Brazilian Laterite Ores with
    Acidithiobacillus thiooxidans, Sulfobacillus species and Archaea at Various Conditions.
    Journal of Sustainable Metallurgy 11:3732-3747. doi:10.1007/s40831-025-01139-7.
    (https://doi.org/10.1007/s40831-025-01139-7)) report culture-level sulfur oxidation
    and leaching without single-gene sqr/tth knockouts; supports: partial is strictly
    preserved on all enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
  locator: Canonical EDIT history sidecar history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
    (SHA-256 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459): Add
    thiooxidans_laterite_bioleaching_graph causal graph and ground thiooxidans_laterite_bioleaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — '
  snapshot_sha256: 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459
- evidence_id: validation
  kind: validation
  reference: data/records/nickel.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T05:32:30Z'
  support: supports
  summary: data/records/nickel.yaml and history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:nickel
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
  - cmmmech:nickel
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''thiooxidans_laterite_bioleaching_graph'' (mechanism_ref:
    thiooxidans_laterite_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349
    (sqr, A0A543Q349_ACITH, UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH,
    UP000363590)]; tth_hydrolase: [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590),
    UniProtKB:A0A5P9XS05 (tth, A0A5P9XS05_ACITH, UP000363590)])'
  outcome: supported
  summary: 'Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d)
    with causal_graph ''thiooxidans_laterite_bioleaching_graph'' (mechanism_ref: thiooxidans_laterite_bioleaching,
    5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
    UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
    [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
    (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) hetz_schippers_2025. Live-verified UniProtKB
    reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine
    nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390
    Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XUB1 (A0A5P9XUB1_ACITH,
    Pyridine nucleotide-disulfide oxidoreductase, gene_symbol: sqor, TREMBL, NCBITaxon:637390
    Acidithiobacillus thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XPU3 (A0A5P9XPU3_ACITH,
    Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus
    thiooxidans ATCC 19377, UP000363590); UniProtKB:A0A5P9XS05 (A0A5P9XS05_ACITH,
    Tetrathionate hydrolase, gene_symbol: tth, TREMBL, NCBITaxon:637390 Acidithiobacillus
    thiooxidans ATCC 19377, UP000363590).'
  target_ids:
  - cmmmech:nickel
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/nickel.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/nickel/2026-10-31T053145Z-marcin-bd7c08.yaml
    (SHA-256 8f62bf446ad12777372e58f1a3f64d287926d928738a4aa21a2da031bb959459): Add
    thiooxidans_laterite_bioleaching_graph causal graph and ground thiooxidans_laterite_bioleaching
    to Acidithiobacillus reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:A0A543Q349,
    UniProtKB:A0A5P9XUB1, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05) — ) and passing
    all LinkML and history validation gates.'
  target_ids:
  - cmmmech:nickel
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Nickel (cmmmech:nickel) passes Cycle 6 Stage 2 causal-graphs review (scientific_review:
  true) at SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d:
  Curated data/records/nickel.yaml (SHA-256 cee651ecb5c980d5c0793fde3fd51edea05e96365d6eee2e6b6d8c7a6252626d)
  with causal_graph ''thiooxidans_laterite_bioleaching_graph'' (mechanism_ref: thiooxidans_laterite_bioleaching,
  5 nodes / 4 edges; sqr_reductase: [UniProtKB:A0A543Q349 (sqr, A0A543Q349_ACITH,
  UP000363590), UniProtKB:A0A5P9XUB1 (sqor, A0A5P9XUB1_ACITH, UP000363590)]; tth_hydrolase:
  [UniProtKB:A0A5P9XPU3 (tth, A0A5P9XPU3_ACITH, UP000363590), UniProtKB:A0A5P9XS05
  (tth, A0A5P9XS05_ACITH, UP000363590)]), achieving 100% parity between mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and caveats from primary source(s) hetz_schippers_2025. Live-verified UniProtKB
  reference-proteome grounding across UniProtKB:A0A543Q349 (A0A543Q349_ACITH, Pyridine
  nucleotide-disulfide oxidoreductase, gene_symbol: sqr, TREMBL, NCBITaxon:637390
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
- Executed during Cycle 6 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
