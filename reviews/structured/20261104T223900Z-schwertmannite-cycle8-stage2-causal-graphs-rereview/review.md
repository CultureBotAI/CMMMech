# Cycle 8 Stage 2 causal-graphs re-review of Schwertmannite (cmmmech:schwertmannite) after Issue #925 fixes

- Review: 20261104T223900Z-schwertmannite-cycle8-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T22:38:00Z
- Finished UTC: 2026-11-04T22:39:00Z
- Reviewer: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Schwertmannite (cmmmech:schwertmannite) passes Cycle 8 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2: Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) with causal_graph 'lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph' (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph 'lx5_eps_removal_perturbation_graph' (mechanism_ref: lx5_eps_removal_perturbation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) song2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 8 Stage 2 causal-graphs review of data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) and its canonical EDIT history sidecar(s) (history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml, history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph' (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph 'lx5_eps_removal_perturbation_graph' (mechanism_ref: lx5_eps_removal_perturbation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:schwertmannite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e299e1aca151b2192b36a718acf832b137818789.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:schwertmannite | data/records/schwertmannite.yaml | maintained | Schwertmannite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:schwertmannite | Checked 683 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:schwertmannite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph' (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph 'lx5_eps_removal_perturbation_graph' (mechanism_ref: lx5_eps_removal_perturbation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:schwertmannite.

Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) with causal_graph 'lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph' (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph 'lx5_eps_removal_perturbation_graph' (mechanism_ref: lx5_eps_removal_perturbation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) song2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:schwertmannite.

data/records/schwertmannite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml (SHA-256 eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c): Add lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph causal graphs and ground both mechanisms to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and both causal graphs (lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph) to schwertmannite.yaml.; history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml (SHA-256 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e): Align both schwertmannite causal_graphs and protein_examples annotations with Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 in Song et al. (2018) (Issue #925) — Updated lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph, lx5_eps_removal_perturbation_graph, and protein_examples in schwertmannite.yaml to match Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 of Song et al. (2018) (225 mL + 11.12 g FeSO4.7H2O, initial pH 3.0, 6.0 x 10^6 cells/mL, 28 C, 180 rpm; 35.0% biological vs 47.9% H2O2 total-Fe precipitation at 60 h; 20,000 g 20 min 4 C EPS removal increasing dry schwertmannite yield from 0.89 g and 0.96 g to 1.29 g and BET area from 68.23 and 56.76 m2/g to 86.43 m2/g) (Issue #925).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/schwertmannite.yaml; Working-tree record data/records/schwertmannite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) with causal_graph 'lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph' (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph 'lx5_eps_removal_perturbation_graph' (mechanism_ref: lx5_eps_removal_perturbation, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) song2018. |
| primary_source | DOI:10.3390/ma11091739; song2018: Song, Liu and Wang (2018). Comparison of the Biological and Chemical Synthesis of Schwertmannite at a Consistent Fe2+ Oxidation Efficiency and the Effect of Extracellular Polymeric Substances of Acidithiobacillus ferrooxidans on Biomineralization. Materials 11(9):1739. Sections 2-3, Figures 1-7 and Table 1; complete 13-page primary article. (https://doi.org/10.3390/ma11091739) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (song2018: Song, Liu and Wang (2018). Comparison of the Biological and Chemical Synthesis of Schwertmannite at a Consistent Fe2+ Oxidation Efficiency and the Effect of Extracellular Polymeric Substances of Acidithiobacillus ferrooxidans on Biomineralization. Materials 11(9):1739. Sections 2-3, Figures 1-7 and Table 1; complete 13-page primary article. (https://doi.org/10.3390/ma11091739)) report culture-level iron/sulfur oxidation and mineral transformation/leaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml; Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml | supports | Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml (SHA-256 eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c): Add lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph causal graphs and ground both mechanisms to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and both causal graphs (lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph) to schwertmannite.yaml. |
| edit_history_2 | history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml; Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml | supports | Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml (SHA-256 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e): Align both schwertmannite causal_graphs and protein_examples annotations with Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 in Song et al. (2018) (Issue #925) — Updated lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph, lx5_eps_removal_perturbation_graph, and protein_examples in schwertmannite.yaml to match Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 of Song et al. (2018) (225 mL + 11.12 g FeSO4.7H2O, initial pH 3.0, 6.0 x 10^6 cells/mL, 28 C, 180 rpm; 35.0% biological vs 47.9% H2O2 total-Fe precipitation at 60 h; 20,000 g 20 min 4 C EPS removal increasing dry schwertmannite yield from 0.89 g and 0.96 g to 1.29 g and BET area from 68.23 and 56.76 m2/g to 86.43 m2/g) (Issue #925). |
| validation | data/records/schwertmannite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/schwertmannite.yaml and history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml, history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 8 Stage 2 (causal_graphs) after addressing Issue #925 internal-consistency findings using scripts/curate_causal_graphs.py; supersedes initial review 20261104T210700Z-schwertmannite-cycle8-stage2-causal-graphs-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T223900Z-schwertmannite-cycle8-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 8 Stage 2 causal-graphs re-review of Schwertmannite (cmmmech:schwertmannite)
  after Issue #925 fixes'
started_at: '2026-11-04T22:38:00Z'
finished_at: '2026-11-04T22:39:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 8 Stage 2 causal_graphs and ProteinExample curation in data/records/schwertmannite.yaml
    (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) against
    UniProtKB reference proteomes and cited primary source(s) song2018.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: e299e1aca151b2192b36a718acf832b137818789
  state: working_tree
  inputs:
  - path: data/records/schwertmannite.yaml
    sha256: 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2
    role: target
  - path: history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
    sha256: eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c
    role: context
  - path: history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
    sha256: 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:schwertmannite
  path: data/records/schwertmannite.yaml
  label: Schwertmannite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/schwertmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
    role: canonical_history
scope:
  description: 'Cycle 8 Stage 2 causal-graphs review of data/records/schwertmannite.yaml
    (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2) and
    its canonical EDIT history sidecar(s) (history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml,
    history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml) verifying
    causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph''
    (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes
    / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]);
    causal_graph ''lx5_eps_removal_perturbation_graph'' (mechanism_ref: lx5_eps_removal_perturbation,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).'
  selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:schwertmannite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:schwertmannite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/schwertmannite.yaml
  locator: Working-tree record data/records/schwertmannite.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2)
    with causal_graph ''lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph''
    (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes
    / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]);
    causal_graph ''lx5_eps_removal_perturbation_graph'' (mechanism_ref: lx5_eps_removal_perturbation,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    song2018.'
  snapshot_sha256: 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3390/ma11091739
  locator: 'song2018: Song, Liu and Wang (2018). Comparison of the Biological and
    Chemical Synthesis of Schwertmannite at a Consistent Fe2+ Oxidation Efficiency
    and the Effect of Extracellular Polymeric Substances of Acidithiobacillus ferrooxidans
    on Biomineralization. Materials 11(9):1739. Sections 2-3, Figures 1-7 and Table
    1; complete 13-page primary article. (https://doi.org/10.3390/ma11091739)'
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
    gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
    cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).
    Primary mechanism source(s) (song2018: Song, Liu and Wang (2018). Comparison of
    the Biological and Chemical Synthesis of Schwertmannite at a Consistent Fe2+ Oxidation
    Efficiency and the Effect of Extracellular Polymeric Substances of Acidithiobacillus
    ferrooxidans on Biomineralization. Materials 11(9):1739. Sections 2-3, Figures
    1-7 and Table 1; complete 13-page primary article. (https://doi.org/10.3390/ma11091739))
    report culture-level iron/sulfur oxidation and mineral transformation/leaching
    without single-gene knockouts; supports: partial is strictly preserved on all
    enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
  locator: Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
    (SHA-256 eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c): Add
    lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph
    causal graphs and ground both mechanisms to Acidithiobacillus ferrooxidans ATCC
    23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6)
    — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples
    (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6
    cyc1/AFE_3152) and both causal graphs (lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph
    and lx5_eps_removal_perturbation_graph) to schwertmannite.yaml.'
  snapshot_sha256: eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
  locator: Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
    (SHA-256 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e): Align
    both schwertmannite causal_graphs and protein_examples annotations with Sections
    2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 in Song et al. (2018) (Issue
    #925) — Updated lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph,
    lx5_eps_removal_perturbation_graph, and protein_examples in schwertmannite.yaml
    to match Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 of Song
    et al. (2018) (225 mL + 11.12 g FeSO4.7H2O, initial pH 3.0, 6.0 x 10^6 cells/mL,
    28 C, 180 rpm; 35.0% biological vs 47.9% H2O2 total-Fe precipitation at 60 h;
    20,000 g 20 min 4 C EPS removal increasing dry schwertmannite yield from 0.89
    g and 0.96 g to 1.29 g and BET area from 68.23 and 56.76 m2/g to 86.43 m2/g) (Issue
    #925).'
  snapshot_sha256: 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e
- evidence_id: validation
  kind: validation
  reference: data/records/schwertmannite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: data/records/schwertmannite.yaml and history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml,
    history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml pass strict
    LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 683 record(s); 0 failed.
  target_ids:
  - cmmmech:schwertmannite
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
  - cmmmech:schwertmannite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph''
    (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes
    / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]);
    causal_graph ''lx5_eps_removal_perturbation_graph'' (mechanism_ref: lx5_eps_removal_perturbation,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2)
    with causal_graph ''lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph''
    (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes
    / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]);
    causal_graph ''lx5_eps_removal_perturbation_graph'' (mechanism_ref: lx5_eps_removal_perturbation,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    song2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
    gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
    cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:schwertmannite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/schwertmannite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/schwertmannite/2026-11-04T210559Z-marcin-714018.yaml
    (SHA-256 eeb833ff409bec2efb2c4bdefdd19a9577b8a54737c0ee5368f20ab34d58976c): Add
    lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph and lx5_eps_removal_perturbation_graph
    causal graphs and ground both mechanisms to Acidithiobacillus ferrooxidans ATCC
    23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6)
    — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples
    (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6
    cyc1/AFE_3152) and both causal graphs (lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph
    and lx5_eps_removal_perturbation_graph) to schwertmannite.yaml.; history/records/schwertmannite/2026-11-04T223801Z-marcin-4b4b71.yaml
    (SHA-256 36cf4f4ee1fc14098024f7fbecce00e4a1642a9d7c85df2a2ca5fa4f0b8c6e0e): Align
    both schwertmannite causal_graphs and protein_examples annotations with Sections
    2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 in Song et al. (2018) (Issue
    #925) — Updated lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph,
    lx5_eps_removal_perturbation_graph, and protein_examples in schwertmannite.yaml
    to match Sections 2.2.1, 2.2.3, and 3.1-3.4, Table 1, and Figures 1-7 of Song
    et al. (2018) (225 mL + 11.12 g FeSO4.7H2O, initial pH 3.0, 6.0 x 10^6 cells/mL,
    28 C, 180 rpm; 35.0% biological vs 47.9% H2O2 total-Fe precipitation at 60 h;
    20,000 g 20 min 4 C EPS removal increasing dry schwertmannite yield from 0.89
    g and 0.96 g to 1.29 g and BET area from 68.23 and 56.76 m2/g to 86.43 m2/g) (Issue
    #925).) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:schwertmannite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Schwertmannite (cmmmech:schwertmannite) passes Cycle 8 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2:
  Curated data/records/schwertmannite.yaml (SHA-256 35e46d0512d571fb1d38b99331842578cf3dbdf3bbd4d9fa909627f88a6e85a2)
  with causal_graph ''lx5_ferrous_oxidation_and_schwertmannite_precipitation_graph''
  (mechanism_ref: lx5_ferrous_oxidation_and_schwertmannite_precipitation, 5 nodes
  / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
  UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2,
  UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]); causal_graph
  ''lx5_eps_removal_perturbation_graph'' (mechanism_ref: lx5_eps_removal_perturbation,
  5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
  UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2,
  UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  song2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
  (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
  gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
  23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
  cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 8 Stage 2 (causal_graphs) after addressing Issue #925 internal-consistency
  findings using scripts/curate_causal_graphs.py; supersedes initial review 20261104T210700Z-schwertmannite-cycle8-stage2-causal-graphs-review.'
related_reviews: []
```
