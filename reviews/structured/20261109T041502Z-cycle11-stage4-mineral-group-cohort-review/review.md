# Cycle 11 Stage 4 full-cohort review: mineral_group records (7/7)

- Review: 20261109T041502Z-cycle11-stage4-mineral-group-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T04:02:00Z
- Finished UTC: 2026-11-09T04:15:02Z
- Reviewer: antigravity / cmmmech-cycle11-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 7 mineral_group records in data/records/*.yaml at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite), including the Cycle 11 Stage 2 (PR #960, commit df061de7) and Stage 3 (PR #963, commit 79468470) causal-graph and UniProtKB grounding expansion on cmmmech:illite. All 7/7 mineral_group records contain primary-source-supported microbial mechanisms (7 mechanisms total), and 3/7 (cmmmech:chlorite, cmmmech:illite, and cmmmech:olivine-group) contain causal_graphs (3 graphs, 9 GENE_OR_PROTEIN nodes: 9 GROUNDED and 0 UNGROUNDED) grounded to 10 unique UniProtKB accessions across Shewanella oneidensis MR-1 (CymA UniProtKB:Q8E8S0, MtrC UniProtKB:Q8EG34, OmcA UniProtKB:Q8EG33 in chlorite), Shewanella putrefaciens CN32 (CymA UniProtKB:A4Y2B9, OmcA UniProtKB:A4Y626, UndA UniProtKB:A4Y627 in illite), and Gluconobacter oxydans 621H (PstS paralogs UniProtKB:Q5FTI1 and UniProtKB:Q5FSF4, PqqC UniProtKB:Q9L3B2, Gdh UniProtKB:P27175 in olivine-group). Identified 1 minor graph finding (cmmmech-cycle11-stage4-finding-0001 on cmmmech:olivine-group) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 11 Stage 4 category review of all 7 mineral_group records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral_group' at 794684703f77385b6e9bca32167f6c8d1e5e29bf
Coverage: full; 7 reviewed / 7 in the declared population.
Source: git_commit at Git base 794684703f77385b6e9bca32167f6c8d1e5e29bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bastnaesite | data/records/bastnaesite.yaml | maintained | Bastnaesite fluorocarbonate family |
| cmmmech:biotite | data/records/biotite.yaml | maintained | Biotite mica series |
| cmmmech:chlorite | data/records/chlorite.yaml | maintained | Chlorite group |
| cmmmech:illite | data/records/illite.yaml | maintained | Illite group |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:potassium-feldspar | data/records/potassium-feldspar.yaml | maintained | Potassium feldspar family |
| cmmmech:vermiculite | data/records/vermiculite.yaml | maintained | Vermiculite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group cohort records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group cohort records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### Mineral group vs endmember species distinction, microbial mechanisms, and Shewanella / Gluconobacter causal graphs

evidence: supported. Targets: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite.

All 7 mineral_group records contain primary-source-supported microbial mechanisms; 3/7 (chlorite, illite, olivine-group) contain causal_graphs grounded to 10 unique UniProtKB accessions. Identified 1 minor graph finding on cmmmech:olivine-group (edges[0..2] generic template explanations).

## Findings

### cmmmech-cycle11-stage4-finding-0001: Gluconobacter oxydans silicate bioleaching causal graphs in enstatite.yaml, olivine-group.yaml, and dunite.yaml retain generic template node/edge explanations and unqualified pqqC/gdh support in dunite.yaml

minor / open / confirmed; issue key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support.

Across the three Gluconobacter oxydans whole-culture biolixiviant silicate bioleaching records — data/records/enstatite.yaml (cmmmech:enstatite, mineral, Klug et al. 2026 Scientific Reports 16:25317, DOI:10.1038/s41598-026-63817-0, klug_2026; causal_graphs[0] gluconobacter_enstatite_bioleaching_graph, lines 143-321), data/records/olivine-group.yaml (cmmmech:olivine-group, mineral_group, Klug et al. 2026, klug_2026; causal_graphs[0] gluconobacter_olivine_bioleaching_graph, lines 143-321), and data/records/dunite.yaml (cmmmech:dunite, primary_resource, Lee et al. 2025 Scientific Reports 15:15134, DOI:10.1038/s41598-025-99655-9, lee2025; causal_graphs[0] gluconobacter_dunite_bioleaching_graph, lines 159-349) — data/records/enstatite.yaml nodes[4].description (enstatite_mixed_feed, line 269) retains the generic parenthetical template string repeating the capitalized node label verbatim ('Starting solid substrate (Enstatite-bearing mixed silicate feed) exposed to the acidic biolixiviant.') instead of specifying the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate powder leached at 5% w/v (0.5 g per 10 mL liquid) without a pure-enstatite control (mechanisms[0].context, lines 31-32). Furthermore, edges[1].evidence[0].explanation (line 294 in enstatite.yaml and olivine-group.yaml; line 310 in dunite.yaml) and edges[2].evidence[0].explanation (line 303 in enstatite.yaml and olivine-group.yaml; line 319 in dunite.yaml) retain identical generic one-line template strings ('PQQ-dependent glucose dehydrogenase activity drives gluconic-acid biolixiviant production in Gluconobacter oxydans.' and 'Periplasmic glucose oxidation by G. oxydans generates the acidic gluconic-acid-rich biolixiviant.'), and edges[0].evidence[0].explanation in enstatite.yaml and olivine-group.yaml (line 285) omits that the engineered strain combined pstS deletion with the P112:mgdh promoter swap. Additionally, in data/records/dunite.yaml, mechanisms[0].protein_examples[2..3].evidence[0] (lines 105-107 and 130-132 for UniProtKB:Q9L3B2 pqqC and UniProtKB:P27175 gdh), causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0] (lines 242-244 and 274-276), and causal_graphs[0].edges[1..2].evidence[0] (lines 308-310 and 317-319) assert supports: support with generic template explanations, whereas Lee et al. (2025) compared wild-type G. oxydans NRRL B-58 (initial pH 2.39 +/- 0.02) and engineered B58 delta-pstS, P112:mgdh (initial pH 2.01 +/- 0.02) whole-culture biolixiviants without single-gene knockouts or purified-enzyme assays isolating pqqC or mgdh (supports: partial, matching enstatite.yaml and olivine-group.yaml). In this scope, 1 record(s) (olivine-group) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-gluconobacter-enstatite-olivine-dunite-graphs

Replace the generic parenthetical template description on enstatite.yaml nodes[4].description (enstatite_mixed_feed), replace generic template explanations on edges[0..2].evidence[0].explanation in data/records/enstatite.yaml and data/records/olivine-group.yaml and edges[1..2].evidence[0].explanation in data/records/dunite.yaml with study-specific prose citing Klug et al. (2026) and Lee et al. (2025), and qualify dunite.yaml mechanisms[0].protein_examples[2..3].evidence[0].supports, causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0].supports, and causal_graphs[0].edges[1..2].evidence[0].supports to partial during Stage 5 grouped remediation with canonical history provenance.

- enstatite.yaml causal_graphs[0].nodes[4].description specifies the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate feed (5% w/v) without template label duplication.
- edges[0..2].evidence[0].explanation in enstatite.yaml and olivine-group.yaml and edges[1..2].evidence[0].explanation in dunite.yaml replace generic template strings with study-specific klug_2026 and lee2025 prose.
- dunite.yaml mechanisms[0].protein_examples[2..3], causal_graphs[0].nodes[1..2].protein_examples[0], and causal_graphs[0].edges[1..2] use supports: partial with Synchronized study-specific explanations.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite. All 7 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral_group' at 794684703f77385b6e9bca32167f6c8d1e5e29bf with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-mineral-group-cohort-audit | data/records/*.yaml (material_kind == 'mineral_group'); 7 mineral_group YAML files | supports | Full programmatic and source-backed audit of all 7 mineral_group records at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf. |
| ev-gluconobacter-olivine-group-graph | data/records/olivine-group.yaml; causal_graphs[0] (lines 143-321) | supports | In data/records/olivine-group.yaml, causal_graphs[0].edges[0..2] retain generic one-line template explanations. |

## Limits And Additional Notes

- 4 of 7 mineral_group records (bastnaesite, biotite, potassium-feldspar, vermiculite) have organic-acid or heterotrophic bioleaching/bioweathering mechanisms without strain-resolved enzymatic causal graphs in the cited primary studies.
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T041502Z-cycle11-stage4-mineral-group-cohort-review
title: 'Cycle 11 Stage 4 full-cohort review: mineral_group records (7/7)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-09T04:02:00Z'
finished_at: '2026-11-09T04:15:02Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 7 mineral_group records in data/records/*.yaml at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf
  (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite),
  including the Cycle 11 Stage 2 (PR #960, commit df061de7) and Stage 3 (PR #963,
  commit 79468470) causal-graph and UniProtKB grounding expansion on cmmmech:illite.
  All 7/7 mineral_group records contain primary-source-supported microbial mechanisms
  (7 mechanisms total), and 3/7 (cmmmech:chlorite, cmmmech:illite, and cmmmech:olivine-group)
  contain causal_graphs (3 graphs, 9 GENE_OR_PROTEIN nodes: 9 GROUNDED and 0 UNGROUNDED)
  grounded to 10 unique UniProtKB accessions across Shewanella oneidensis MR-1 (CymA
  UniProtKB:Q8E8S0, MtrC UniProtKB:Q8EG34, OmcA UniProtKB:Q8EG33 in chlorite), Shewanella
  putrefaciens CN32 (CymA UniProtKB:A4Y2B9, OmcA UniProtKB:A4Y626, UndA UniProtKB:A4Y627
  in illite), and Gluconobacter oxydans 621H (PstS paralogs UniProtKB:Q5FTI1 and UniProtKB:Q5FSF4,
  PqqC UniProtKB:Q9L3B2, Gdh UniProtKB:P27175 in olivine-group). Identified 1 minor
  graph finding (cmmmech-cycle11-stage4-finding-0001 on cmmmech:olivine-group) for
  Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 11 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
source:
  git_revision: 794684703f77385b6e9bca32167f6c8d1e5e29bf
  state: git_commit
  inputs:
  - path: data/records/bastnaesite.yaml
    sha256: 719dafc38a258c140dafa5c718a651d19c7300c9aa0643fe293898d56f1b6448
    role: target
  - path: data/records/biotite.yaml
    sha256: 52c2162343ba439ef35da695d6aed7cdf03c6e91fb43bfa9c9d706de24a5cbe8
    role: target
  - path: data/records/chlorite.yaml
    sha256: f26f20999e3df05bf5ce82b4fb141881e685d7f2a3bd43b69c577283dde26131
    role: target
  - path: data/records/illite.yaml
    sha256: 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6
    role: target
  - path: data/records/olivine-group.yaml
    sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
    role: target
  - path: data/records/potassium-feldspar.yaml
    sha256: 7a53e4d2bea0b490ca04c7a955359988ac3b8e348621e5a9787e080402181f7c
    role: target
  - path: data/records/vermiculite.yaml
    sha256: ac406ac0fcd6d79a68ad824d0c04496eea5d6f71bb308bb63fa47dcefff7009b
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 7
  reviewed_target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  selection: data/records/*.yaml where material_kind == 'mineral_group' at 794684703f77385b6e9bca32167f6c8d1e5e29bf
  description: Full-population Cycle 11 Stage 4 category review of all 7 mineral_group
    records in CMMMech.
targets:
- target_id: cmmmech:bastnaesite
  path: data/records/bastnaesite.yaml
  kind: maintained
  label: Bastnaesite fluorocarbonate family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bastnaesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:biotite
  path: data/records/biotite.yaml
  kind: maintained
  label: Biotite mica series
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/biotite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chlorite
  path: data/records/chlorite.yaml
  kind: maintained
  label: Chlorite group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:illite
  path: data/records/illite.yaml
  kind: maintained
  label: Illite group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/illite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:olivine-group
  path: data/records/olivine-group.yaml
  kind: maintained
  label: Olivine group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:potassium-feldspar
  path: data/records/potassium-feldspar.yaml
  kind: maintained
  label: Potassium feldspar family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/potassium-feldspar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vermiculite
  path: data/records/vermiculite.yaml
  kind: maintained
  label: Vermiculite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vermiculite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: just-validate-mineral-groups
  name: just validate (mineral_group cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  summary: All 7 mineral_group cohort records pass LinkML structural, semantic, and
    canonical top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-mineral-groups
  name: just verify-history (mineral_group cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  summary: All 7 mineral_group cohort records have intact append-only history sidecars
    and matching curation_history metadata.
assessments:
- assessment_id: assess-mineral-group-identity-and-mechanisms
  topic: Mineral group vs endmember species distinction, microbial mechanisms, and
    Shewanella / Gluconobacter causal graphs
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  evidence_ids:
  - ev-mineral-group-cohort-audit
  - ev-gluconobacter-olivine-group-graph
  summary: All 7 mineral_group records contain primary-source-supported microbial
    mechanisms; 3/7 (chlorite, illite, olivine-group) contain causal_graphs grounded
    to 10 unique UniProtKB accessions. Identified 1 minor graph finding on cmmmech:olivine-group
    (edges[0..2] generic template explanations).
findings:
- finding_id: cmmmech-cycle11-stage4-finding-0001
  issue_key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support
  title: Gluconobacter oxydans silicate bioleaching causal graphs in enstatite.yaml,
    olivine-group.yaml, and dunite.yaml retain generic template node/edge explanations
    and unqualified pqqC/gdh support in dunite.yaml
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:olivine-group
  field_paths:
  - mechanisms[0].protein_examples[2].evidence[0].supports
  - mechanisms[0].protein_examples[2].evidence[0].explanation
  - mechanisms[0].protein_examples[3].evidence[0].supports
  - mechanisms[0].protein_examples[3].evidence[0].explanation
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[2].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[4].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].evidence[0].supports
  - causal_graphs[0].edges[2].evidence[0].explanation
  evidence_ids:
  - ev-mineral-group-cohort-audit
  - ev-gluconobacter-olivine-group-graph
  description: 'Across the three Gluconobacter oxydans whole-culture biolixiviant
    silicate bioleaching records — data/records/enstatite.yaml (cmmmech:enstatite,
    mineral, Klug et al. 2026 Scientific Reports 16:25317, DOI:10.1038/s41598-026-63817-0,
    klug_2026; causal_graphs[0] gluconobacter_enstatite_bioleaching_graph, lines 143-321),
    data/records/olivine-group.yaml (cmmmech:olivine-group, mineral_group, Klug et
    al. 2026, klug_2026; causal_graphs[0] gluconobacter_olivine_bioleaching_graph,
    lines 143-321), and data/records/dunite.yaml (cmmmech:dunite, primary_resource,
    Lee et al. 2025 Scientific Reports 15:15134, DOI:10.1038/s41598-025-99655-9, lee2025;
    causal_graphs[0] gluconobacter_dunite_bioleaching_graph, lines 159-349) — data/records/enstatite.yaml
    nodes[4].description (enstatite_mixed_feed, line 269) retains the generic parenthetical
    template string repeating the capitalized node label verbatim (''Starting solid
    substrate (Enstatite-bearing mixed silicate feed) exposed to the acidic biolixiviant.'')
    instead of specifying the ~40 um milled, ultrasonically washed 69 wt% olivine
    / 31 wt% enstatite mixed silicate powder leached at 5% w/v (0.5 g per 10 mL liquid)
    without a pure-enstatite control (mechanisms[0].context, lines 31-32). Furthermore,
    edges[1].evidence[0].explanation (line 294 in enstatite.yaml and olivine-group.yaml;
    line 310 in dunite.yaml) and edges[2].evidence[0].explanation (line 303 in enstatite.yaml
    and olivine-group.yaml; line 319 in dunite.yaml) retain identical generic one-line
    template strings (''PQQ-dependent glucose dehydrogenase activity drives gluconic-acid
    biolixiviant production in Gluconobacter oxydans.'' and ''Periplasmic glucose
    oxidation by G. oxydans generates the acidic gluconic-acid-rich biolixiviant.''),
    and edges[0].evidence[0].explanation in enstatite.yaml and olivine-group.yaml
    (line 285) omits that the engineered strain combined pstS deletion with the P112:mgdh
    promoter swap. Additionally, in data/records/dunite.yaml, mechanisms[0].protein_examples[2..3].evidence[0]
    (lines 105-107 and 130-132 for UniProtKB:Q9L3B2 pqqC and UniProtKB:P27175 gdh),
    causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0] (lines 242-244 and
    274-276), and causal_graphs[0].edges[1..2].evidence[0] (lines 308-310 and 317-319)
    assert supports: support with generic template explanations, whereas Lee et al.
    (2025) compared wild-type G. oxydans NRRL B-58 (initial pH 2.39 +/- 0.02) and
    engineered B58 delta-pstS, P112:mgdh (initial pH 2.01 +/- 0.02) whole-culture
    biolixiviants without single-gene knockouts or purified-enzyme assays isolating
    pqqC or mgdh (supports: partial, matching enstatite.yaml and olivine-group.yaml).
    In this scope, 1 record(s) (olivine-group) are affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
actions:
- action_id: act-refine-gluconobacter-enstatite-olivine-dunite-graphs
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0001
  target_ids:
  - cmmmech:olivine-group
  description: Replace the generic parenthetical template description on enstatite.yaml
    nodes[4].description (enstatite_mixed_feed), replace generic template explanations
    on edges[0..2].evidence[0].explanation in data/records/enstatite.yaml and data/records/olivine-group.yaml
    and edges[1..2].evidence[0].explanation in data/records/dunite.yaml with study-specific
    prose citing Klug et al. (2026) and Lee et al. (2025), and qualify dunite.yaml
    mechanisms[0].protein_examples[2..3].evidence[0].supports, causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0].supports,
    and causal_graphs[0].edges[1..2].evidence[0].supports to partial during Stage
    5 grouped remediation with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  acceptance_checks:
  - enstatite.yaml causal_graphs[0].nodes[4].description specifies the ~40 um milled,
    ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate feed (5%
    w/v) without template label duplication.
  - edges[0..2].evidence[0].explanation in enstatite.yaml and olivine-group.yaml and
    edges[1..2].evidence[0].explanation in dunite.yaml replace generic template strings
    with study-specific klug_2026 and lee2025 prose.
  - 'dunite.yaml mechanisms[0].protein_examples[2..3], causal_graphs[0].nodes[1..2].protein_examples[0],
    and causal_graphs[0].edges[1..2] use supports: partial with Synchronized study-specific
    explanations.'
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-mineral-group-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'mineral_group')
  locator: 7 mineral_group YAML files
  accessed_at: '2026-11-09T04:15:02Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 7 mineral_group records
    at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
- evidence_id: ev-gluconobacter-olivine-group-graph
  kind: record_content
  reference: data/records/olivine-group.yaml
  locator: causal_graphs[0] (lines 143-321)
  accessed_at: '2026-11-09T04:15:02Z'
  support: supports
  summary: In data/records/olivine-group.yaml, causal_graphs[0].edges[0..2] retain
    generic one-line template explanations.
limitations:
- 4 of 7 mineral_group records (bastnaesite, biotite, potassium-feldspar, vermiculite)
  have organic-acid or heterotrophic bioleaching/bioweathering mechanisms without
  strain-resolved enzymatic causal graphs in the cited primary studies.
notes:
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit
  794684703f77385b6e9bca32167f6c8d1e5e29bf.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:bastnaesite
  - cmmmech:biotite
  - cmmmech:chlorite
  - cmmmech:illite
  - cmmmech:olivine-group
  - cmmmech:potassium-feldspar
  - cmmmech:vermiculite
  rationale: All 7 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where material_kind == 'mineral_group' at 794684703f77385b6e9bca32167f6c8d1e5e29bf
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-mineral-group-cohort-audit
```
