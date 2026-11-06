# Cycle 10 Stage 2 causal-graphs review of Jadarite (cmmmech:jadarite)

- Review: 20261106T050600Z-jadarite-cycle10-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-06T05:05:30Z
- Finished UTC: 2026-11-06T05:06:00Z
- Reviewer: antigravity / cmmmech-cycle10-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Jadarite (cmmmech:jadarite) passes Cycle 10 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120: Curated data/records/jadarite.yaml with causal_graph 'acidophile_jadarite_bearing_material_leaching_graph' (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1). Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 10 Stage 2 causal-graphs review of data/records/jadarite.yaml (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120) and its canonical EDIT history sidecar(s) (history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml, history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'acidophile_jadarite_bearing_material_leaching_graph' (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 10 Stage 2 causal_graphs curation for cmmmech:jadarite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0fbb411bcb9bba9d4871d7791d5a13ebc4b50723.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:jadarite | data/records/jadarite.yaml | maintained | Jadarite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:jadarite | Checked 693 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:jadarite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB reference-proteome grounding, and parity across causal_graph 'acidophile_jadarite_bearing_material_leaching_graph' (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:jadarite.

Curated data/records/jadarite.yaml (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120) with causal_graph 'acidophile_jadarite_bearing_material_leaching_graph' (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1). Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:jadarite.

data/records/jadarite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml (SHA-256 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368): Add evidence-backed causal_graphs representation and 4 live-verified Acidithiobacillus ferrooxidans rus-operon protein groundings (UniProtKB:B7JAQ7, UniProtKB:A0A2W1KH68, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) for acidophile_jadarite_bearing_material_leaching, preserving the 13.5 mL cumulative 0.5 M H2SO4 dosing and acid-dominated Li/B dissolution parity (190 vs 210 mg/L Li; 800 vs 860 mg/L B).; history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml (SHA-256 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90): Align jadarite.yaml protein_examples and causal_graphs strictly with curated acidophile_jadarite_bearing_material_leaching evidence (qualitative Jadar Valley jadarite-dolomite-probertite XRD, 2 g in 190 mL medium + 10 mL inoculum pulp-density ambiguity, transient mid-course Li acceleration with day-30 control convergence, and partial support for the 2-theta 27.9 degree XRD peak) (Issue #947).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/jadarite.yaml; Working-tree record data/records/jadarite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/jadarite.yaml (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120) with causal_graph 'acidophile_jadarite_bearing_material_leaching_graph' (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2024.1467408; kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1)) report culture-level mineralization, biosorption, or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml; Canonical EDIT history sidecar history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml | supports | Canonical EDIT history sidecar history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml (SHA-256 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368): Add evidence-backed causal_graphs representation and 4 live-verified Acidithiobacillus ferrooxidans rus-operon protein groundings (UniProtKB:B7JAQ7, UniProtKB:A0A2W1KH68, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) for acidophile_jadarite_bearing_material_leaching, preserving the 13.5 mL cumulative 0.5 M H2SO4 dosing and acid-dominated Li/B dissolution parity (190 vs 210 mg/L Li; 800 vs 860 mg/L B). |
| edit_history_2 | history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml; Canonical EDIT history sidecar history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml | supports | Canonical EDIT history sidecar history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml (SHA-256 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90): Align jadarite.yaml protein_examples and causal_graphs strictly with curated acidophile_jadarite_bearing_material_leaching evidence (qualitative Jadar Valley jadarite-dolomite-probertite XRD, 2 g in 190 mL medium + 10 mL inoculum pulp-density ambiguity, transient mid-course Li acceleration with day-30 control convergence, and partial support for the 2-theta 27.9 degree XRD peak) (Issue #947). |
| validation | data/records/jadarite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/jadarite.yaml and history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml, history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 10 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:jadarite (including Issue #947 review-remediation updates).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T050600Z-jadarite-cycle10-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 10 Stage 2 causal-graphs review of Jadarite (cmmmech:jadarite)
started_at: '2026-11-06T05:05:30Z'
finished_at: '2026-11-06T05:06:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle10-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 10 Stage 2 causal_graphs and ProteinExample curation in data/records/jadarite.yaml
    (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120) against
    live UniProtKB reference-proteome grounding and cited primary source(s) (kirk2024:
    Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite
    using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The
    genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 0fbb411bcb9bba9d4871d7791d5a13ebc4b50723
  state: working_tree
  inputs:
  - path: data/records/jadarite.yaml
    sha256: bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120
    role: target
  - path: history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
    sha256: 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368
    role: context
  - path: history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
    sha256: 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:jadarite
  path: data/records/jadarite.yaml
  label: Jadarite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jadarite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
    role: canonical_history
scope:
  description: 'Cycle 10 Stage 2 causal-graphs review of data/records/jadarite.yaml
    (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120) and
    its canonical EDIT history sidecar(s) (history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml,
    history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml) verifying causal-graph
    node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''acidophile_jadarite_bearing_material_leaching_graph''
    (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges;
    aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)];
    aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).'
  selection: Cycle 10 Stage 2 causal_graphs curation for cmmmech:jadarite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:jadarite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/jadarite.yaml
  locator: Working-tree record data/records/jadarite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Curated data/records/jadarite.yaml (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120)
    with causal_graph ''acidophile_jadarite_bearing_material_leaching_graph'' (mechanism_ref:
    acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1467408
  locator: 'kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene,
    and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology
    15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1)'
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR,
    Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus
    ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s)
    (kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene,
    and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology
    15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1))
    report culture-level mineralization, biosorption, or bioleaching without single-gene
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
  locator: Canonical EDIT history sidecar history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
    (SHA-256 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368): Add
    evidence-backed causal_graphs representation and 4 live-verified Acidithiobacillus
    ferrooxidans rus-operon protein groundings (UniProtKB:B7JAQ7, UniProtKB:A0A2W1KH68,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) for acidophile_jadarite_bearing_material_leaching,
    preserving the 13.5 mL cumulative 0.5 M H2SO4 dosing and acid-dominated Li/B dissolution
    parity (190 vs 210 mg/L Li; 800 vs 860 mg/L B).'
  snapshot_sha256: 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
  locator: Canonical EDIT history sidecar history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
    (SHA-256 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90): Align
    jadarite.yaml protein_examples and causal_graphs strictly with curated acidophile_jadarite_bearing_material_leaching
    evidence (qualitative Jadar Valley jadarite-dolomite-probertite XRD, 2 g in 190
    mL medium + 10 mL inoculum pulp-density ambiguity, transient mid-course Li acceleration
    with day-30 control convergence, and partial support for the 2-theta 27.9 degree
    XRD peak) (Issue #947).'
  snapshot_sha256: 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90
- evidence_id: validation
  kind: validation
  reference: data/records/jadarite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-06T05:05:45Z'
  support: supports
  summary: data/records/jadarite.yaml and history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml,
    history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml pass strict LinkML
    schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 693 record(s); 0 failed.
  target_ids:
  - cmmmech:jadarite
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
  - cmmmech:jadarite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB reference-proteome grounding,
    and parity across causal_graph ''acidophile_jadarite_bearing_material_leaching_graph''
    (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges;
    aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)];
    aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/jadarite.yaml (SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120)
    with causal_graph ''acidophile_jadarite_bearing_material_leaching_graph'' (mechanism_ref:
    acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from kirk2024: Kirk
    et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite
    using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The
    genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1).
    Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2,
    Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C,
    gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans,
    UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT,
    NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6
    (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:jadarite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/jadarite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/jadarite/2026-11-06T045814Z-marcin-24c14f.yaml
    (SHA-256 83c580218afc1582b895b8e5a40ed7caa624afd8840e491c1016f47f37367368): Add
    evidence-backed causal_graphs representation and 4 live-verified Acidithiobacillus
    ferrooxidans rus-operon protein groundings (UniProtKB:B7JAQ7, UniProtKB:A0A2W1KH68,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) for acidophile_jadarite_bearing_material_leaching,
    preserving the 13.5 mL cumulative 0.5 M H2SO4 dosing and acid-dominated Li/B dissolution
    parity (190 vs 210 mg/L Li; 800 vs 860 mg/L B).; history/records/jadarite/2026-11-06T062553Z-marcin-60a033.yaml
    (SHA-256 101061eca788bd572ff83044e95b04f69a0826c68c836a8df68a7c751471fd90): Align
    jadarite.yaml protein_examples and causal_graphs strictly with curated acidophile_jadarite_bearing_material_leaching
    evidence (qualitative Jadar Valley jadarite-dolomite-probertite XRD, 2 g in 190
    mL medium + 10 mL inoculum pulp-density ambiguity, transient mid-course Li acceleration
    with day-30 control convergence, and partial support for the 2-theta 27.9 degree
    XRD peak) (Issue #947).) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:jadarite
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Jadarite (cmmmech:jadarite) passes Cycle 10 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 bad32256dbbfaffcc32222ac940d77da5d502c5b720fb62dba7ebbe1a88b1120:
  Curated data/records/jadarite.yaml with causal_graph ''acidophile_jadarite_bearing_material_leaching_graph''
  (mechanism_ref: acidophile_jadarite_bearing_material_leaching, 4 nodes / 3 edges;
  aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
  UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)];
  aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
  UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between
  mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving
  source-faithful support levels and experimental caveats from kirk2024: Kirk et al.
  (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus
  ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained
  from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1:
  Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite
  using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November
  2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1).
  Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2,
  Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
  ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C,
  gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans,
  UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT,
  NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6
  (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 10 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:jadarite (including Issue #947 review-remediation updates).'
related_reviews: []
```
