# Cycle 9 Stage 2 causal-graphs review of Ammoniojarosite (cmmmech:ammoniojarosite)

- Review: 20261105T172800Z-ammoniojarosite-cycle9-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-05T17:27:30Z
- Finished UTC: 2026-11-05T17:28:00Z
- Reviewer: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ammoniojarosite (cmmmech:ammoniojarosite) passes Cycle 9 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6: Curated data/records/ammoniojarosite.yaml with causal_graph 'iron_oxidation_associated_precipitation_graph' (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex: [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME, UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001). Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME, FoxA, gene_symbol: foxA, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU5 (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol: foxC, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB).

## Scope And Provenance

Cycle 9 Stage 2 causal-graphs review of data/records/ammoniojarosite.yaml (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6) and its canonical EDIT history sidecar (history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'iron_oxidation_associated_precipitation_graph' (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex: [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME, UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]).

Selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:ammoniojarosite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 503b381e1b3aba9d1b2525daf9ebffbfb005d19c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ammoniojarosite | data/records/ammoniojarosite.yaml | maintained | Ammoniojarosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:ammoniojarosite | Checked 688 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:ammoniojarosite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB reference-proteome grounding, and parity across causal_graph 'iron_oxidation_associated_precipitation_graph' (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex: [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME, UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)])

graph: supported. Targets: cmmmech:ammoniojarosite.

Curated data/records/ammoniojarosite.yaml (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6) with causal_graph 'iron_oxidation_associated_precipitation_graph' (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex: [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME, UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001). Live-verified UniProtKB grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME, FoxA, gene_symbol: foxA, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU5 (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol: foxC, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:ammoniojarosite.

data/records/ammoniojarosite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml (SHA-256 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ammoniojarosite.yaml; Working-tree record data/records/ammoniojarosite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/ammoniojarosite.yaml (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6) with causal_graph 'iron_oxidation_associated_precipitation_graph' (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975, A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex: [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME, UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | DOI:10.1016/j.gca.2006.09.001; wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME, FoxA, gene_symbol: foxA, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU5 (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol: foxC, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB). Primary mechanism source(s) (wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001)) report culture-level mineralization or bioleaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml; Canonical EDIT history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml | supports | Canonical EDIT history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml (SHA-256 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84): Add REPRESENTATIVE_EXAMPLE causal graph and dual-organism live-verified protein groundings for Acidithiobacillus ferrooxidans (rus-operon Cyc2 UniProtKB:B7JAQ7/UniProtKB:A0A2W1KH68, Swiss-Prot rusticyanin UniProtKB:B7JAQ0, and Cyc1 UniProtKB:B7JAQ6 in UP000001362/UP000248886) and Sulfuracidifex metallicus (fox-cluster foxA UniProtKB:A4ZGV2, foxB UniProtKB:A4ZGU5, and foxC UniProtKB:A4ZGU4) supporting ammonium-dependent ammoniojarosite precipitation in Wang et al. (2007). |
| validation | data/records/ammoniojarosite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/ammoniojarosite.yaml and history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:ammoniojarosite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T172800Z-ammoniojarosite-cycle9-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 9 Stage 2 causal-graphs review of Ammoniojarosite (cmmmech:ammoniojarosite)
started_at: '2026-11-05T17:27:30Z'
finished_at: '2026-11-05T17:28:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle9-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 9 Stage 2 causal_graphs and ProteinExample curation in data/records/ammoniojarosite.yaml
    (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6) against
    live UniProtKB reference proteomes and cited primary source(s) (wang2007: Wang,
    Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites
    prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica
    et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 503b381e1b3aba9d1b2525daf9ebffbfb005d19c
  state: working_tree
  inputs:
  - path: data/records/ammoniojarosite.yaml
    sha256: 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6
    role: target
  - path: history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
    sha256: 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:ammoniojarosite
  path: data/records/ammoniojarosite.yaml
  label: Ammoniojarosite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ammoniojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
    role: canonical_history
scope:
  description: 'Cycle 9 Stage 2 causal-graphs review of data/records/ammoniojarosite.yaml
    (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6) and
    its canonical EDIT history sidecar (history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''iron_oxidation_associated_precipitation_graph''
    (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex:
    [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME,
    UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]).'
  selection: Cycle 9 Stage 2 causal_graphs curation for cmmmech:ammoniojarosite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ammoniojarosite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ammoniojarosite.yaml
  locator: Working-tree record data/records/ammoniojarosite.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Curated data/records/ammoniojarosite.yaml (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6)
    with causal_graph ''iron_oxidation_associated_precipitation_graph'' (mechanism_ref:
    iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex:
    [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME,
    UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1016/j.gca.2006.09.001
  locator: 'wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties
    of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at
    22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001)'
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR,
    Cytochrome C, gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus
    ferrooxidans, UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME,
    FoxA, gene_symbol: foxA, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB);
    UniProtKB:A4ZGU5 (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303
    Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol:
    foxC, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB). Primary mechanism
    source(s) (wang2007: Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties
    of ammoniojarosites prepared with iron-oxidizing acidophilic microorganisms at
    22-65 degrees C. Geochimica et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001))
    report culture-level mineralization or bioleaching without single-gene knockouts;
    supports: partial is strictly preserved on all enzyme-level edges and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
  locator: Canonical EDIT history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
    (SHA-256 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84): Add
    REPRESENTATIVE_EXAMPLE causal graph and dual-organism live-verified protein groundings
    for Acidithiobacillus ferrooxidans (rus-operon Cyc2 UniProtKB:B7JAQ7/UniProtKB:A0A2W1KH68,
    Swiss-Prot rusticyanin UniProtKB:B7JAQ0, and Cyc1 UniProtKB:B7JAQ6 in UP000001362/UP000248886)
    and Sulfuracidifex metallicus (fox-cluster foxA UniProtKB:A4ZGV2, foxB UniProtKB:A4ZGU5,
    and foxC UniProtKB:A4ZGU4) supporting ammonium-dependent ammoniojarosite precipitation
    in Wang et al. (2007).'
  snapshot_sha256: 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84
- evidence_id: validation
  kind: validation
  reference: data/records/ammoniojarosite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-05T17:27:45Z'
  support: supports
  summary: data/records/ammoniojarosite.yaml and history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 688 record(s); 0 failed.
  target_ids:
  - cmmmech:ammoniojarosite
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
  - cmmmech:ammoniojarosite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB reference-proteome grounding,
    and parity across causal_graph ''iron_oxidation_associated_precipitation_graph''
    (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex:
    [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME,
    UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)])'
  outcome: supported
  summary: 'Curated data/records/ammoniojarosite.yaml (SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6)
    with causal_graph ''iron_oxidation_associated_precipitation_graph'' (mechanism_ref:
    iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
    A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
    UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex:
    [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME,
    UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from wang2007: Wang,
    Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites
    prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica
    et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001).
    Live-verified UniProtKB grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome
    c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C,
    gene_symbol: DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans,
    UP000248886); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT,
    NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6
    (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME, FoxA, gene_symbol:
    foxA, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU5
    (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303 Sulfuracidifex
    metallicus, UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol: foxC,
    TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB).'
  target_ids:
  - cmmmech:ammoniojarosite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: data/records/ammoniojarosite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar history/records/ammoniojarosite/2026-11-05T172709Z-marcin-3b0048.yaml
    (SHA-256 5b5bcb5bffd4a0a04118a6c3f1344588235be60ace1ce5d8e284ce86e9440f84) and
    passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:ammoniojarosite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Ammoniojarosite (cmmmech:ammoniojarosite) passes Cycle 9 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 54626852e9bce17223b1fe19e8276619b5a864954f567e90bc9f9856603f11a6:
  Curated data/records/ammoniojarosite.yaml with causal_graph ''iron_oxidation_associated_precipitation_graph''
  (mechanism_ref: iron_oxidation_associated_precipitation, 4 nodes / 3 edges; aferro_rus_operon_iron_oxidation_complex:
  [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362), UniProtKB:A0A2W1KH68 (DN052_11975,
  A0A2W1KH68_ACIFR, UP000248886), UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362),
  UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]; smet_fox_cluster_iron_oxidation_complex:
  [UniProtKB:A4ZGV2 (foxA, A4ZGV2_SULME, UniProtKB), UniProtKB:A4ZGU5 (foxB, A4ZGU5_SULME,
  UniProtKB), UniProtKB:A4ZGU4 (foxC, A4ZGU4_SULME, UniProtKB)]), achieving 100% parity
  between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from wang2007:
  Wang, Bigham, Jones and Tuovinen (2007). Synthesis and properties of ammoniojarosites
  prepared with iron-oxidizing acidophilic microorganisms at 22-65 degrees C. Geochimica
  et Cosmochimica Acta 71:155-164. (https://doi.org/10.1016/j.gca.2006.09.001). Live-verified
  UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome
  c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
  23270, UP000001362); UniProtKB:A0A2W1KH68 (A0A2W1KH68_ACIFR, Cytochrome C, gene_symbol:
  DN052_11975, TREMBL, NCBITaxon:920 Acidithiobacillus ferrooxidans, UP000248886);
  UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159
  Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2,
  Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
  ATCC 23270, UP000001362); UniProtKB:A4ZGV2 (A4ZGV2_SULME, FoxA, gene_symbol: foxA,
  TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus, UniProtKB); UniProtKB:A4ZGU5
  (A4ZGU5_SULME, FoxB, gene_symbol: foxB, TREMBL, NCBITaxon:47303 Sulfuracidifex metallicus,
  UniProtKB); UniProtKB:A4ZGU4 (A4ZGU4_SULME, FoxC, gene_symbol: foxC, TREMBL, NCBITaxon:47303
  Sulfuracidifex metallicus, UniProtKB).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 9 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:ammoniojarosite.
related_reviews: []
```
