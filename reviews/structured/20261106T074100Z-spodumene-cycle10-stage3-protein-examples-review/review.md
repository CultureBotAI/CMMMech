# Cycle 10 Stage 3 protein-examples review of Spodumene (cmmmech:spodumene)

- Review: 20261106T074100Z-spodumene-cycle10-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-06T07:40:30Z
- Finished UTC: 2026-11-06T07:41:00Z
- Reviewer: antigravity / cmmmech-cycle10-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Spodumene (cmmmech:spodumene) passes Cycle 10 Stage 3 protein-examples review (scientific_review: true) at SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412: Enriched data/records/spodumene.yaml with causal_graph 'acidophile_spodumene_leaching_limit_graph' (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1). Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KP86 (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 10 Stage 3 protein-examples review of data/records/spodumene.yaml (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412) and its canonical EDIT history sidecar (history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml) verifying live UniProtKB reference-proteome grounding, exact organism/sequence/claim scope, and parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples across causal_graph 'acidophile_spodumene_leaching_limit_graph' (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 10 Stage 3 protein_examples enrichment for cmmmech:spodumene
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d9589c0f34e49bfc6d5ed8fa193c9584ac878367.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spodumene | data/records/spodumene.yaml | maintained | Spodumene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:spodumene | Checked 693 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:spodumene | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of UniProtKB reference-proteome grounding and parity across causal_graph 'acidophile_spodumene_leaching_limit_graph' (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:spodumene.

Enriched data/records/spodumene.yaml (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412) with causal_graph 'acidophile_spodumene_leaching_limit_graph' (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1). Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KP86 (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:spodumene.

data/records/spodumene.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar (history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml (SHA-256 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64): Add live-verified species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome rusticyanin ortholog (UniProtKB:A0A2W1KP86, DN052_11940, UP000248886, NCBITaxon:920) to spodumene.yaml (acidophile-spodumene-leaching-limit).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/spodumene.yaml; Working-tree record data/records/spodumene.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Enriched data/records/spodumene.yaml (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412) with causal_graph 'acidophile_spodumene_leaching_limit_graph' (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.3389/fmicb.2024.1467408; kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KP86 (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408); kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1, published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1)) report culture-level mineralization, biosorption, or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml; Canonical EDIT history sidecar history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml | supports | Canonical EDIT history sidecar history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml (SHA-256 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64): Add live-verified species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome rusticyanin ortholog (UniProtKB:A0A2W1KP86, DN052_11940, UP000248886, NCBITaxon:920) to spodumene.yaml (acidophile-spodumene-leaching-limit). |
| validation | data/records/spodumene.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/spodumene.yaml and history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 10 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py for cmmmech:spodumene.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T074100Z-spodumene-cycle10-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 10 Stage 3 protein-examples review of Spodumene (cmmmech:spodumene)
started_at: '2026-11-06T07:40:30Z'
finished_at: '2026-11-06T07:41:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle10-stage3-protein-examples-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 10 Stage 3 ProteinExample grounding enrichment in data/records/spodumene.yaml
    (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412) against
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
  git_revision: d9589c0f34e49bfc6d5ed8fa193c9584ac878367
  state: working_tree
  inputs:
  - path: data/records/spodumene.yaml
    sha256: a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412
    role: target
  - path: history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
    sha256: 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:spodumene
  path: data/records/spodumene.yaml
  label: Spodumene
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spodumene.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
    role: canonical_history
scope:
  description: 'Cycle 10 Stage 3 protein-examples review of data/records/spodumene.yaml
    (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412) and
    its canonical EDIT history sidecar (history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml)
    verifying live UniProtKB reference-proteome grounding, exact organism/sequence/claim
    scope, and parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    across causal_graph ''acidophile_spodumene_leaching_limit_graph'' (mechanism_ref:
    acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR,
    UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).'
  selection: Cycle 10 Stage 3 protein_examples enrichment for cmmmech:spodumene
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spodumene
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/spodumene.yaml
  locator: Working-tree record data/records/spodumene.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-06T07:40:45Z'
  support: supports
  summary: 'Enriched data/records/spodumene.yaml (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412)
    with causal_graph ''acidophile_spodumene_leaching_limit_graph'' (mechanism_ref:
    acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR,
    UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1467408
  locator: 'kirk2024: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene,
    and lepidolite using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology
    15:1467408. The genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1)'
  accessed_at: '2026-11-06T07:40:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR,
    Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus
    ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:A0A2W1KP86 (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940,
    TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6
    (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (kirk2024:
    Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite
    using Acidiothiobacillus ferrooxidans. Frontiers in Microbiology 15:1467408. The
    genus spelling is retained from the published title. (https://doi.org/10.3389/fmicb.2024.1467408);
    kirk2024_data_v1: Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene
    and lepidolite using Acidiothiobacillus ferrooxidans. Mendeley Data, version 1,
    published 14 November 2024; CC BY 4.0. Published genus spelling retained. (https://doi.org/10.17632/djkf7tkm8d.1))
    report culture-level mineralization, biosorption, or bioleaching without single-gene
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
  locator: Canonical EDIT history sidecar history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
  accessed_at: '2026-11-06T07:40:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
    (SHA-256 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64): Add
    live-verified species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome
    rusticyanin ortholog (UniProtKB:A0A2W1KP86, DN052_11940, UP000248886, NCBITaxon:920)
    to spodumene.yaml (acidophile-spodumene-leaching-limit).'
  snapshot_sha256: 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64
- evidence_id: validation
  kind: validation
  reference: data/records/spodumene.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-06T07:40:45Z'
  support: supports
  summary: data/records/spodumene.yaml and history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 693 record(s); 0 failed.
  target_ids:
  - cmmmech:spodumene
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
  - cmmmech:spodumene
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_causal_graph_grounding
  area: graph
  topic: 'Verification of UniProtKB reference-proteome grounding and parity across
    causal_graph ''acidophile_spodumene_leaching_limit_graph'' (mechanism_ref: acidophile-spodumene-leaching-limit,
    4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase: [UniProtKB:B7JAQ7
    (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR,
    UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2,
    UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR, UP000248886),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])'
  outcome: supported
  summary: 'Enriched data/records/spodumene.yaml (SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412)
    with causal_graph ''acidophile_spodumene_leaching_limit_graph'' (mechanism_ref:
    acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
    (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR,
    UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
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
    NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KP86
    (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940, TREMBL, NCBITaxon:920
    Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2,
    Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:spodumene
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/spodumene.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar (history/records/spodumene/2026-11-06T073942Z-marcin-b8aef0.yaml
    (SHA-256 4f9ed28674ef4fcf3a5f0b269cb45b5ce1e7c52406a3d292000a8c9ae6804d64): Add
    live-verified species-level Acidithiobacillus ferrooxidans DSM 16523 reference-proteome
    rusticyanin ortholog (UniProtKB:A0A2W1KP86, DN052_11940, UP000248886, NCBITaxon:920)
    to spodumene.yaml (acidophile-spodumene-leaching-limit).) and passing all LinkML
    and history validation gates.'
  target_ids:
  - cmmmech:spodumene
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Spodumene (cmmmech:spodumene) passes Cycle 10 Stage 3 protein-examples review
  (scientific_review: true) at SHA-256 a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412:
  Enriched data/records/spodumene.yaml with causal_graph ''acidophile_spodumene_leaching_limit_graph''
  (mechanism_ref: acidophile-spodumene-leaching-limit, 4 nodes / 3 edges; aferro_cyc2_outer_membrane_iron_oxidase:
  [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
  A0A2W1KH68_ACIFR, UP000248886)]; aferro_rus_cyc1_periplasmic_relay: [UniProtKB:B7JAQ0
  (rus, RUS_ACIF2, UP000001362), UniProtKB:A0A2W1KP86 (DN052_11940, A0A2W1KP86_ACIFR,
  UP000248886), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from kirk2024:
  Kirk et al. (2024). Bioleaching of lithium from jadarite, spodumene, and lepidolite
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
  NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KP86
  (A0A2W1KP86_ACIFR, Rusticyanin, gene_symbol: DN052_11940, TREMBL, NCBITaxon:920
  Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome
  c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
  ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 10 Stage 3 (protein_examples) using scripts/curate_causal_graphs.py
  for cmmmech:spodumene.
related_reviews: []
```
