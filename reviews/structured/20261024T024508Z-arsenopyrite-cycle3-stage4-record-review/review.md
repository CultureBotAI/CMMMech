# Cycle 3 Stage 4 record review: cmmmech:arsenopyrite (Arsenopyrite)

- Review: 20261024T024508Z-arsenopyrite-cycle3-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T02:43:00Z
- Finished UTC: 2026-10-24T02:45:08Z
- Reviewer: antigravity / cmmmech-cycle3-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Reviewed data/records/arsenopyrite.yaml (cmmmech:arsenopyrite) at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e following Cycle 3 Stage 2 causal-graph curation and UniProtKB protein grounding. Verified IMA-CNMNC formula FeAsS (1962 s.p. grandfathered/redefined status), mechanism ferrooxidans_arsenic_release_and_surface_films from Liu et al. (2019, DOI:10.3390/met9121320) in Acidithiobacillus ferrooxidans (NCBITaxon:920), causal graph ferrooxidans_arsenic_release_and_surface_films_graph (5 nodes, 4 edges using predicates supplies_substrate_for, produces, and dissolves), and both live-verified reviewed Swiss-Prot reference-proteome groundings in Acidithiobacillus ferrooxidans ATCC 23270 (NCBITaxon:243159, UP000001362): UniProtKB:B7JBP8 (SQRD_ACIF2, AFE_1792, Sulfide-quinone reductase, EC:1.8.5.4) and UniProtKB:B7J3C9 (TTH_ACIF2, tth / AFE_0029, Tetrathionate hydrolase, EC:3.12.1.-). Zero open findings.

## Scope And Provenance

Single-record Cycle 3 Stage 4 audit of cmmmech:arsenopyrite after Cycle 3 Stage 2 causal-graph and UniProtKB grounding updates.

Selection: data/records/arsenopyrite.yaml at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate arsenopyrite.yaml | passed | True | cmmmech:arsenopyrite | data/records/arsenopyrite.yaml passes LinkML structural and semantic validation with 0 errors. |

## Scientific And Domain Assessments

### Arsenopyrite bioleaching causal graph and UniProtKB:B7JBP8 / UniProtKB:B7J3C9 groundings

graph: supported. Targets: cmmmech:arsenopyrite.

Causal graph ferrooxidans_arsenic_release_and_surface_films_graph accurately models reduced-sulfur oxidation (Sqr -&gt; Tth -&gt; 9K lixiviant), oxidative dissolution of Yaogangxian FeAsS particles/cubes (1.3 g/L dissolved As; 30.4% As leaching ratio at 19 d), and secondary realgar/orpiment/sulfur/jarosite formation, with 100% synchronized UniProtKB:B7JBP8 (SQRD_ACIF2) and UniProtKB:B7J3C9 (TTH_ACIF2) protein_examples.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-arsenopyrite-file | data/records/arsenopyrite.yaml; lines 1-224 | supports | Verified mechanism ferrooxidans_arsenic_release_and_surface_films, causal graph ferrooxidans_arsenic_release_and_surface_films_graph, and synchronized UniProtKB:B7JBP8 and UniProtKB:B7J3C9 protein_examples across mechanisms and GENE_OR_PROTEIN nodes. |
| ev-arsenopyrite-liu2019 | DOI:10.3390/met9121320; Liu et al. 2019 Metals 9(12):1320 | supports | Supports inoculated Acidithiobacillus ferrooxidans bioleaching of Yaogangxian natural arsenopyrite (Fe1.00As0.99S0.97) in 9K medium, 1.3 g/L total dissolved As (30.4% As leaching ratio at 19 d), and Rietveld-XRD identification of realgar, orpiment, elemental sulfur, and jarosite. |

## Limits And Additional Notes


## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T024508Z-arsenopyrite-cycle3-stage4-record-review
title: 'Cycle 3 Stage 4 record review: cmmmech:arsenopyrite (Arsenopyrite)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-24T02:43:00Z'
finished_at: '2026-10-24T02:45:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Reviewed data/records/arsenopyrite.yaml (cmmmech:arsenopyrite) at commit
  855e0eba1fa9b8a4a975b7155ec013414e4d437e following Cycle 3 Stage 2 causal-graph
  curation and UniProtKB protein grounding. Verified IMA-CNMNC formula FeAsS (1962
  s.p. grandfathered/redefined status), mechanism ferrooxidans_arsenic_release_and_surface_films
  from Liu et al. (2019, DOI:10.3390/met9121320) in Acidithiobacillus ferrooxidans
  (NCBITaxon:920), causal graph ferrooxidans_arsenic_release_and_surface_films_graph
  (5 nodes, 4 edges using predicates supplies_substrate_for, produces, and dissolves),
  and both live-verified reviewed Swiss-Prot reference-proteome groundings in Acidithiobacillus
  ferrooxidans ATCC 23270 (NCBITaxon:243159, UP000001362): UniProtKB:B7JBP8 (SQRD_ACIF2,
  AFE_1792, Sulfide-quinone reductase, EC:1.8.5.4) and UniProtKB:B7J3C9 (TTH_ACIF2,
  tth / AFE_0029, Tetrathionate hydrolase, EC:3.12.1.-). Zero open findings.'
reviewer:
  identity: antigravity / cmmmech-cycle3-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 3 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
source:
  git_revision: 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  state: git_commit
  inputs:
  - path: data/records/arsenopyrite.yaml
    sha256: 94152683e839a537bc58d23c3bf9fa05fd65447dfb94b032a2a87a5b8cc56020
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:arsenopyrite
  selection: data/records/arsenopyrite.yaml at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  description: Single-record Cycle 3 Stage 4 audit of cmmmech:arsenopyrite after Cycle
    3 Stage 2 causal-graph and UniProtKB grounding updates.
targets:
- target_id: cmmmech:arsenopyrite
  path: data/records/arsenopyrite.yaml
  kind: maintained
  label: Arsenopyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenopyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-arsenopyrite
  name: cmmmech validate arsenopyrite.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/arsenopyrite.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - ev-arsenopyrite-file
  summary: data/records/arsenopyrite.yaml passes LinkML structural and semantic validation
    with 0 errors.
assessments:
- assessment_id: assess-arsenopyrite-causal-graph-and-proteins
  topic: Arsenopyrite bioleaching causal graph and UniProtKB:B7JBP8 / UniProtKB:B7J3C9
    groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - ev-arsenopyrite-file
  - ev-arsenopyrite-liu2019
  summary: Causal graph ferrooxidans_arsenic_release_and_surface_films_graph accurately
    models reduced-sulfur oxidation (Sqr -> Tth -> 9K lixiviant), oxidative dissolution
    of Yaogangxian FeAsS particles/cubes (1.3 g/L dissolved As; 30.4% As leaching
    ratio at 19 d), and secondary realgar/orpiment/sulfur/jarosite formation, with
    100% synchronized UniProtKB:B7JBP8 (SQRD_ACIF2) and UniProtKB:B7J3C9 (TTH_ACIF2)
    protein_examples.
findings: []
actions: []
evidence:
- evidence_id: ev-arsenopyrite-file
  kind: record_content
  reference: data/records/arsenopyrite.yaml
  locator: lines 1-224
  accessed_at: '2026-10-24T02:45:08Z'
  support: supports
  summary: Verified mechanism ferrooxidans_arsenic_release_and_surface_films, causal
    graph ferrooxidans_arsenic_release_and_surface_films_graph, and synchronized UniProtKB:B7JBP8
    and UniProtKB:B7J3C9 protein_examples across mechanisms and GENE_OR_PROTEIN nodes.
- evidence_id: ev-arsenopyrite-liu2019
  kind: primary_source
  reference: DOI:10.3390/met9121320
  locator: Liu et al. 2019 Metals 9(12):1320
  accessed_at: '2026-10-24T02:45:08Z'
  support: supports
  summary: Supports inoculated Acidithiobacillus ferrooxidans bioleaching of Yaogangxian
    natural arsenopyrite (Fe1.00As0.99S0.97) in 9K medium, 1.3 g/L total dissolved
    As (30.4% As leaching ratio at 19 d), and Rietveld-XRD identification of realgar,
    orpiment, elemental sulfur, and jarosite.
limitations: []
notes: []
```
