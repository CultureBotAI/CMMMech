# Cycle 6 Stage 4 record review: cmmmech:arsenic (Arsenic)

- Review: 20261031T132008Z-arsenic-cycle6-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T13:14:00Z
- Finished UTC: 2026-10-31T13:20:08Z
- Reviewer: antigravity / cmmmech-cycle6-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/arsenic.yaml (cmmmech:arsenic) at commit fab0682688678750d7da4e5357dda11592d5fac3. Verified CHEBI:27563 (arsenic atom) identity, USGS 2025, DOE 2023, and EU 2024 Annex II criticality entries, mechanism thiooxidans_arsenic_bioleaching (Lee et al. 2015, DOI:10.1007/s11356-014-3516-x), causal graph thiooxidans_arsenic_bioleaching_graph (5 nodes, 4 edges), and all 4 synchronized Acidithiobacillus thiooxidans ATCC 19377 UniProtKB protein_examples (Sqr/Sqor UniProtKB:A0A543Q349 GCD22_02301 and UniProtKB:A0A5P9XUB1 GCD22_03207; Tth UniProtKB:A0A5P9XPU3 tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315). Identified 1 minor graph node label/description finding (cmmmech-cycle6-stage4-finding-0002: causal_graphs[0].nodes[1] tth_hydrolase retains singular label 'Tth tetrathionate hydrolase (tth)' and generic description omitting paralog loci GCD22_14205 and GCD22_02315, whereas sibling node sqr_reductase explicitly names '(Sqr/Sqor; GCD22_02301 / GCD22_03207)') for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 6 Stage 4 audit of cmmmech:arsenic.

Selection: data/records/arsenic.yaml at fab0682688678750d7da4e5357dda11592d5fac3
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base fab0682688678750d7da4e5357dda11592d5fac3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:arsenic | data/records/arsenic.yaml | maintained | Arsenic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate arsenic.yaml | passed | True | cmmmech:arsenic | data/records/arsenic.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### Acidithiobacillus thiooxidans arsenic bioleaching mechanism, causal graph, and Sqr/Sqor + Tth paralog groundings

graph: supported. Targets: cmmmech:arsenic.

All 4 A. thiooxidans ATCC 19377 UniProtKB protein_examples (2 Sqr/Sqor and 2 Tth paralogs) are accurately grounded and synchronized between mechanisms[0] and causal_graphs[0]. However, causal_graphs[0].nodes[1] (tth_hydrolase) retains pre-expansion singular label and description omitting paralog loci GCD22_14205 and GCD22_02315.

## Findings

### cmmmech-cycle6-stage4-finding-0002: 16 single-species Acidithiobacillus thiooxidans causal_graphs retain singular tth_hydrolase node label and omit grounded paralog loci (GCD22_14205, GCD22_02315) in description

minor / open / confirmed; issue key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci.

Across the 673-record corpus, 16 single-species Acidithiobacillus thiooxidans records (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge, gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst) whose tth_hydrolase causal-graph nodes were expanded in Cycle 5 Stage 3 (PR #872) to include both A. thiooxidans ATCC 19377 tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3 tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315) still retain the pre-expansion singular label 'Tth tetrathionate hydrolase (tth)' and generic description 'Periplasmic tetrathionate hydrolase disproportionating tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.' without naming the two grounded paralog loci (GCD22_14205 and GCD22_02315), whereas sibling node sqr_reductase in all 16 graphs explicitly names '(Sqr/Sqor; GCD22_02301 / GCD22_03207)' in its description and the 5 Cycle 6 Stage 2/3 A. thiooxidans records (chromite-beneficiation-tailings, jarosite, nickel-laterite-ore, nickel, petroleum-coke) explicitly name '(tth GCD22_14205; tth GCD22_02315)'. In this scope, 1 record(s) (arsenic) exhibit this node label/description lag.

## Recommended Actions And Acceptance Checks

### act-align-thiooxidans-tth-hydrolase-paralog-loci-labels-and-descriptions

Update causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description in the affected single-species Acidithiobacillus thiooxidans records to explicitly name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci (tth GCD22_14205 and tth GCD22_02315) during Stage 5 grouped remediation with canonical history provenance.

- All affected records name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci (GCD22_14205 and GCD22_02315) in causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-arsenic-file | data/records/arsenic.yaml; lines 1-355 (nodes[0] lines 199-203, nodes[1] lines 259-264) | supports | Inspected all 355 lines of data/records/arsenic.yaml, verifying sqr_reductase vs tth_hydrolase node labels and descriptions. |
| ev-arsenic-lee2015 | DOI:10.1007/s11356-014-3516-x; Lee et al. 2015 Environ. Sci. Pollut. Res. 22:2853-2860 | supports | Lee et al. (2015) report sulfur-driven bioleaching of arsenic-contaminated soil/tailings by Acidithiobacillus thiooxidans. |

## Limits And Additional Notes

- data/records/arsenic.yaml node tth_hydrolase retains pre-expansion singular label and description omitting paralog loci GCD22_14205 and GCD22_02315 (tracked as open finding cmmmech-cycle6-stage4-finding-0002 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T132008Z-arsenic-cycle6-stage4-record-review
title: 'Cycle 6 Stage 4 record review: cmmmech:arsenic (Arsenic)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-31T13:14:00Z'
finished_at: '2026-10-31T13:20:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/arsenic.yaml (cmmmech:arsenic) at commit fab0682688678750d7da4e5357dda11592d5fac3.
  Verified CHEBI:27563 (arsenic atom) identity, USGS 2025, DOE 2023, and EU 2024 Annex
  II criticality entries, mechanism thiooxidans_arsenic_bioleaching (Lee et al. 2015,
  DOI:10.1007/s11356-014-3516-x), causal graph thiooxidans_arsenic_bioleaching_graph
  (5 nodes, 4 edges), and all 4 synchronized Acidithiobacillus thiooxidans ATCC 19377
  UniProtKB protein_examples (Sqr/Sqor UniProtKB:A0A543Q349 GCD22_02301 and UniProtKB:A0A5P9XUB1
  GCD22_03207; Tth UniProtKB:A0A5P9XPU3 tth / GCD22_14205 and UniProtKB:A0A5P9XS05
  tth / GCD22_02315). Identified 1 minor graph node label/description finding (cmmmech-cycle6-stage4-finding-0002:
  causal_graphs[0].nodes[1] tth_hydrolase retains singular label ''Tth tetrathionate
  hydrolase (tth)'' and generic description omitting paralog loci GCD22_14205 and
  GCD22_02315, whereas sibling node sqr_reductase explicitly names ''(Sqr/Sqor; GCD22_02301
  / GCD22_03207)'') for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 6 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit fab0682688678750d7da4e5357dda11592d5fac3.
source:
  git_revision: fab0682688678750d7da4e5357dda11592d5fac3
  state: git_commit
  inputs:
  - path: data/records/arsenic.yaml
    sha256: 06c768bddccc43174d06a95b33f01b0858ab1e52ea7d9eba73e5bbb6b2092a62
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:arsenic
  selection: data/records/arsenic.yaml at fab0682688678750d7da4e5357dda11592d5fac3
  description: Single-record Cycle 6 Stage 4 audit of cmmmech:arsenic.
targets:
- target_id: cmmmech:arsenic
  path: data/records/arsenic.yaml
  kind: maintained
  label: Arsenic
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenic.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-arsenic
  name: cmmmech validate arsenic.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/arsenic.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:arsenic
  evidence_ids:
  - ev-arsenic-file
  summary: data/records/arsenic.yaml passes LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-arsenic-thiooxidans-graph-and-proteins
  topic: Acidithiobacillus thiooxidans arsenic bioleaching mechanism, causal graph,
    and Sqr/Sqor + Tth paralog groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:arsenic
  evidence_ids:
  - ev-arsenic-file
  - ev-arsenic-lee2015
  summary: All 4 A. thiooxidans ATCC 19377 UniProtKB protein_examples (2 Sqr/Sqor
    and 2 Tth paralogs) are accurately grounded and synchronized between mechanisms[0]
    and causal_graphs[0]. However, causal_graphs[0].nodes[1] (tth_hydrolase) retains
    pre-expansion singular label and description omitting paralog loci GCD22_14205
    and GCD22_02315.
findings:
- finding_id: cmmmech-cycle6-stage4-finding-0002
  issue_key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci
  title: 16 single-species Acidithiobacillus thiooxidans causal_graphs retain singular
    tth_hydrolase node label and omit grounded paralog loci (GCD22_14205, GCD22_02315)
    in description
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:arsenic
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  evidence_ids:
  - ev-arsenic-file
  - ev-arsenic-lee2015
  description: 'Across the 673-record corpus, 16 single-species Acidithiobacillus
    thiooxidans records (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust,
    copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge,
    gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders,
    spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst,
    spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst)
    whose tth_hydrolase causal-graph nodes were expanded in Cycle 5 Stage 3 (PR #872)
    to include both A. thiooxidans ATCC 19377 tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3
    tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315) still retain the
    pre-expansion singular label ''Tth tetrathionate hydrolase (tth)'' and generic
    description ''Periplasmic tetrathionate hydrolase disproportionating tetrathionate
    into thiosulfate, elemental sulfur, sulfate, and protons.'' without naming the
    two grounded paralog loci (GCD22_14205 and GCD22_02315), whereas sibling node
    sqr_reductase in all 16 graphs explicitly names ''(Sqr/Sqor; GCD22_02301 / GCD22_03207)''
    in its description and the 5 Cycle 6 Stage 2/3 A. thiooxidans records (chromite-beneficiation-tailings,
    jarosite, nickel-laterite-ore, nickel, petroleum-coke) explicitly name ''(tth
    GCD22_14205; tth GCD22_02315)''. In this scope, 1 record(s) (arsenic) exhibit
    this node label/description lag.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenic.yaml
    role: maintained_record
actions:
- action_id: act-align-thiooxidans-tth-hydrolase-paralog-loci-labels-and-descriptions
  finding_ids:
  - cmmmech-cycle6-stage4-finding-0002
  target_ids:
  - cmmmech:arsenic
  description: Update causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description
    in the affected single-species Acidithiobacillus thiooxidans records to explicitly
    name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci
    (tth GCD22_14205 and tth GCD22_02315) during Stage 5 grouped remediation with
    canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenic.yaml
    role: maintained_record
  acceptance_checks:
  - All affected records name both grounded A. thiooxidans ATCC 19377 tetrathionate
    hydrolase paralog loci (GCD22_14205 and GCD22_02315) in causal_graphs[0].nodes[1].label
    and causal_graphs[0].nodes[1].description.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-arsenic-file
  kind: record_content
  reference: data/records/arsenic.yaml
  locator: lines 1-355 (nodes[0] lines 199-203, nodes[1] lines 259-264)
  accessed_at: '2026-10-31T13:20:08Z'
  support: supports
  summary: Inspected all 355 lines of data/records/arsenic.yaml, verifying sqr_reductase
    vs tth_hydrolase node labels and descriptions.
- evidence_id: ev-arsenic-lee2015
  kind: primary_source
  reference: DOI:10.1007/s11356-014-3516-x
  locator: Lee et al. 2015 Environ. Sci. Pollut. Res. 22:2853-2860
  accessed_at: '2026-10-31T13:20:08Z'
  support: supports
  summary: Lee et al. (2015) report sulfur-driven bioleaching of arsenic-contaminated
    soil/tailings by Acidithiobacillus thiooxidans.
limitations:
- data/records/arsenic.yaml node tth_hydrolase retains pre-expansion singular label
  and description omitting paralog loci GCD22_14205 and GCD22_02315 (tracked as open
  finding cmmmech-cycle6-stage4-finding-0002 for Stage 5 remediation).
notes: []
```
