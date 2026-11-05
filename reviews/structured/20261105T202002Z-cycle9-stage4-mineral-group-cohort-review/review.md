# Cycle 9 Stage 4 full-cohort review: mineral_group records (7/7)

- Review: 20261105T202002Z-cycle9-stage4-mineral-group-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-05T20:08:00Z
- Finished UTC: 2026-11-05T20:20:02Z
- Reviewer: antigravity / cmmmech-cycle9-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 7 mineral_group records in data/records/*.yaml at commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite). All 7/7 mineral_group records contain primary-source-supported microbial mechanisms (7 mechanisms total), and 2/7 (cmmmech:chlorite and cmmmech:olivine-group) contain causal_graphs (2 graphs, 6 GENE_OR_PROTEIN nodes: 6 GROUNDED and 0 UNGROUNDED) grounded to 7 unique UniProtKB accessions across Shewanella oneidensis MR-1 (CymA UniProtKB:Q8E8S0, MtrC UniProtKB:Q8EG34, OmcA UniProtKB:Q8EG33 in chlorite) and Gluconobacter oxydans 621H (PstS paralogs UniProtKB:Q5FTI1 and UniProtKB:Q5FSF4, PqqC UniProtKB:Q9L3B2, Gdh UniProtKB:P27175 in olivine-group). Identified 1 minor graph edge description finding (cmmmech-cycle9-stage4-finding-0002 in 1 mineral_group record: cmmmech:chlorite) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 9 Stage 4 category review of all 7 mineral_group records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'mineral_group' at f8f0d8e724bcc013b5e9d98e3d12d5c7557587af
Coverage: full; 7 reviewed / 7 in the declared population.
Source: git_commit at Git base f8f0d8e724bcc013b5e9d98e3d12d5c7557587af.
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
| just validate (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (mineral_group cohort) | passed | True | cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite | All 7 mineral_group records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### Mineral group vs endmember species distinction, microbial mechanisms, and Shewanella MR-1 / Gluconobacter oxydans causal graphs

evidence: supported. Targets: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite.

All 7 mineral_group records pass all schema, semantic, key-order, and primary-source mechanism checks. In cmmmech:chlorite, causal_graphs[0].edges[1..2] interpolate capitalized 'Chlorite-associated Fe(III) (ferroan clinochlore)' mid-sentence with generic one-line explanations.

## Findings

### cmmmech-cycle9-stage4-finding-0002: Shewanella oneidensis MR-1 causal graphs in rhodochrosite.yaml and chlorite.yaml contain a medium-name mismatch ('Ca-free artificial freshwater medium' vs 'modified M1 medium'), template node wrappers, and mid-sentence capitalized edge labels

minor / open / confirmed; issue key: cmmmech.shewanella-mr1-rhodochrosite-chlorite.medium-mismatch-template-descriptions-and-capitalized-edge-labels.

In data/records/rhodochrosite.yaml (cmmmech:rhodochrosite, mineral, Johnson et al. 2016 Environ. Sci. Technol. 50(8):4248-4258, DOI:10.1021/acs.est.5b04834; causal_graphs[0] mr1_mn_oxide_rhodochrosite_graph, lines 203-362), nodes[3].description (oxidized_metal_substrate, lines 313-314) and nodes[4].description (reduced_metal_product, lines 319-320) retain generic template wrappers ('Terminal electron acceptor substrate (...) in johnson2016.' and 'Resulting reduced product state (...) in johnson2016.'), nodes[3].description states 'in Ca-free artificial freshwater medium' whereas mechanisms[0].context (line 55) and Johnson et al. (2016) Methods pp. C-D specify a stirred 1 L modified M1 medium (~6.3 mM freshly synthesized poorly ordered colloidal MnO2, 20 mM lactate, no added phosphate, pH 8 under N2), and edges[1..3] (lines 338, 342, 347, 351, 356-357) interpolate capitalized 'Colloidal Mn(IV) oxide' and 'Biogenic rhodochrosite (MnCO3) precipitates and dissolved Mn(II)' mid-sentence with generic one-line explanations on edges[1..2]. Similarly, in data/records/chlorite.yaml (cmmmech:chlorite, mineral_group, Brookshaw et al. 2014 Am. Mineral. 99(8-9):1746-1754, DOI:10.2138/am.2014.4774CCBY; causal_graphs[0] mr1_chlorite_fe_reduction_graph, lines 168-335), edges[1..2] (lines 305-306, 310-311, 316-317, 321-322) interpolate capitalized 'Chlorite-associated Fe(III) (ferroan clinochlore)' mid-sentence with generic one-line explanations. In this scope, 1 record(s) (chlorite) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-shewanella-mr1-rhodochrosite-and-chlorite-graphs

Replace the generic template wrappers and 'Ca-free artificial freshwater medium' mismatch on oxidized_metal_substrate and reduced_metal_product in rhodochrosite.yaml with the exact modified M1 medium and XAS/XRD product details from Johnson et al. (2016), and replace mid-sentence capitalized node labels and generic edge explanations in rhodochrosite.yaml and chlorite.yaml during Stage 5 grouped remediation with canonical history provenance.

- oxidized_metal_substrate and reduced_metal_product in rhodochrosite.yaml accurately describe the ~6.3 mM freshly synthesized colloidal MnO2 in 1 L modified M1 medium (20 mM lactate, no added phosphate, pH 8) and the 73% rhodochrosite / 27% aqueous Mn(II) XAS fit and synchrotron XRD product without template wrappers.
- All mid-sentence node-label interpolations in edges[1..3] of rhodochrosite.yaml and edges[1..2] of chlorite.yaml use lowercase prose and study-specific evidence explanations.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:bastnaesite, cmmmech:biotite, cmmmech:chlorite, cmmmech:illite, cmmmech:olivine-group, cmmmech:potassium-feldspar, cmmmech:vermiculite. All 7 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'mineral_group' at f8f0d8e724bcc013b5e9d98e3d12d5c7557587af with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-mineral-group-cohort-audit | data/records/*.yaml (material_kind == 'mineral_group'); 7 mineral_group YAML files | supports | Full programmatic and source-backed audit of all 7 mineral_group records at commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af. |
| ev-chlorite-mr1-graph | data/records/chlorite.yaml; causal_graphs[0].edges[1..2] (lines 301-322) | supports | In data/records/chlorite.yaml, causal_graphs[0].edges[1..2] (lines 305-306, 310-311, 316-317, 321-322) interpolate capitalized 'Chlorite-associated Fe(III) (ferroan clinochlore)' mid-sentence with generic one-line explanations. |

## Limits And Additional Notes

- 5 of 7 mineral_group records (bastnaesite, biotite, illite, potassium-feldspar, vermiculite) have organic-acid or heterotrophic bioleaching/bioweathering mechanisms without strain-resolved enzymatic causal graphs in the cited primary studies.
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T202002Z-cycle9-stage4-mineral-group-cohort-review
title: 'Cycle 9 Stage 4 full-cohort review: mineral_group records (7/7)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-05T20:08:00Z'
finished_at: '2026-11-05T20:20:02Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 7 mineral_group records in data/records/*.yaml at commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af
  (bastnaesite, biotite, chlorite, illite, olivine-group, potassium-feldspar, vermiculite).
  All 7/7 mineral_group records contain primary-source-supported microbial mechanisms
  (7 mechanisms total), and 2/7 (cmmmech:chlorite and cmmmech:olivine-group) contain
  causal_graphs (2 graphs, 6 GENE_OR_PROTEIN nodes: 6 GROUNDED and 0 UNGROUNDED) grounded
  to 7 unique UniProtKB accessions across Shewanella oneidensis MR-1 (CymA UniProtKB:Q8E8S0,
  MtrC UniProtKB:Q8EG34, OmcA UniProtKB:Q8EG33 in chlorite) and Gluconobacter oxydans
  621H (PstS paralogs UniProtKB:Q5FTI1 and UniProtKB:Q5FSF4, PqqC UniProtKB:Q9L3B2,
  Gdh UniProtKB:P27175 in olivine-group). Identified 1 minor graph edge description
  finding (cmmmech-cycle9-stage4-finding-0002 in 1 mineral_group record: cmmmech:chlorite)
  for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle9-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 9 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af.
source:
  git_revision: f8f0d8e724bcc013b5e9d98e3d12d5c7557587af
  state: git_commit
  inputs:
  - path: data/records/bastnaesite.yaml
    sha256: 719dafc38a258c140dafa5c718a651d19c7300c9aa0643fe293898d56f1b6448
    role: target
  - path: data/records/biotite.yaml
    sha256: 52c2162343ba439ef35da695d6aed7cdf03c6e91fb43bfa9c9d706de24a5cbe8
    role: target
  - path: data/records/chlorite.yaml
    sha256: ed608d1ef84bd29949d0f6f8e130e147d7896a0abb84d9120a53b51a5ca2a7aa
    role: target
  - path: data/records/illite.yaml
    sha256: 26ec1710dfe94d7dc6adf5b776eb1448612b9b698c0836b3a3b97eed98808899
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
  selection: data/records/*.yaml where material_kind == 'mineral_group' at f8f0d8e724bcc013b5e9d98e3d12d5c7557587af
  description: Full-population Cycle 9 Stage 4 category review of all 7 mineral_group
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
  summary: All 7 mineral_group records pass LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors and 0 warnings.
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
  summary: All 7 mineral_group records have intact append-only history sidecars and
    matching curation_history metadata.
assessments:
- assessment_id: assess-mineral-group-identity-and-mechanisms
  topic: Mineral group vs endmember species distinction, microbial mechanisms, and
    Shewanella MR-1 / Gluconobacter oxydans causal graphs
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
  - ev-chlorite-mr1-graph
  summary: All 7 mineral_group records pass all schema, semantic, key-order, and primary-source
    mechanism checks. In cmmmech:chlorite, causal_graphs[0].edges[1..2] interpolate
    capitalized 'Chlorite-associated Fe(III) (ferroan clinochlore)' mid-sentence with
    generic one-line explanations.
findings:
- finding_id: cmmmech-cycle9-stage4-finding-0002
  issue_key: cmmmech.shewanella-mr1-rhodochrosite-chlorite.medium-mismatch-template-descriptions-and-capitalized-edge-labels
  title: Shewanella oneidensis MR-1 causal graphs in rhodochrosite.yaml and chlorite.yaml
    contain a medium-name mismatch ('Ca-free artificial freshwater medium' vs 'modified
    M1 medium'), template node wrappers, and mid-sentence capitalized edge labels
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:chlorite
  field_paths:
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].explanation
  evidence_ids:
  - ev-mineral-group-cohort-audit
  - ev-chlorite-mr1-graph
  description: In data/records/rhodochrosite.yaml (cmmmech:rhodochrosite, mineral,
    Johnson et al. 2016 Environ. Sci. Technol. 50(8):4248-4258, DOI:10.1021/acs.est.5b04834;
    causal_graphs[0] mr1_mn_oxide_rhodochrosite_graph, lines 203-362), nodes[3].description
    (oxidized_metal_substrate, lines 313-314) and nodes[4].description (reduced_metal_product,
    lines 319-320) retain generic template wrappers ('Terminal electron acceptor substrate
    (...) in johnson2016.' and 'Resulting reduced product state (...) in johnson2016.'),
    nodes[3].description states 'in Ca-free artificial freshwater medium' whereas
    mechanisms[0].context (line 55) and Johnson et al. (2016) Methods pp. C-D specify
    a stirred 1 L modified M1 medium (~6.3 mM freshly synthesized poorly ordered colloidal
    MnO2, 20 mM lactate, no added phosphate, pH 8 under N2), and edges[1..3] (lines
    338, 342, 347, 351, 356-357) interpolate capitalized 'Colloidal Mn(IV) oxide'
    and 'Biogenic rhodochrosite (MnCO3) precipitates and dissolved Mn(II)' mid-sentence
    with generic one-line explanations on edges[1..2]. Similarly, in data/records/chlorite.yaml
    (cmmmech:chlorite, mineral_group, Brookshaw et al. 2014 Am. Mineral. 99(8-9):1746-1754,
    DOI:10.2138/am.2014.4774CCBY; causal_graphs[0] mr1_chlorite_fe_reduction_graph,
    lines 168-335), edges[1..2] (lines 305-306, 310-311, 316-317, 321-322) interpolate
    capitalized 'Chlorite-associated Fe(III) (ferroan clinochlore)' mid-sentence with
    generic one-line explanations. In this scope, 1 record(s) (chlorite) are affected.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorite.yaml
    role: maintained_record
actions:
- action_id: act-refine-shewanella-mr1-rhodochrosite-and-chlorite-graphs
  finding_ids:
  - cmmmech-cycle9-stage4-finding-0002
  target_ids:
  - cmmmech:chlorite
  description: Replace the generic template wrappers and 'Ca-free artificial freshwater
    medium' mismatch on oxidized_metal_substrate and reduced_metal_product in rhodochrosite.yaml
    with the exact modified M1 medium and XAS/XRD product details from Johnson et
    al. (2016), and replace mid-sentence capitalized node labels and generic edge
    explanations in rhodochrosite.yaml and chlorite.yaml during Stage 5 grouped remediation
    with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chlorite.yaml
    role: maintained_record
  acceptance_checks:
  - oxidized_metal_substrate and reduced_metal_product in rhodochrosite.yaml accurately
    describe the ~6.3 mM freshly synthesized colloidal MnO2 in 1 L modified M1 medium
    (20 mM lactate, no added phosphate, pH 8) and the 73% rhodochrosite / 27% aqueous
    Mn(II) XAS fit and synchrotron XRD product without template wrappers.
  - All mid-sentence node-label interpolations in edges[1..3] of rhodochrosite.yaml
    and edges[1..2] of chlorite.yaml use lowercase prose and study-specific evidence
    explanations.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-mineral-group-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'mineral_group')
  locator: 7 mineral_group YAML files
  accessed_at: '2026-11-05T20:20:02Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 7 mineral_group records
    at commit f8f0d8e724bcc013b5e9d98e3d12d5c7557587af.
- evidence_id: ev-chlorite-mr1-graph
  kind: record_content
  reference: data/records/chlorite.yaml
  locator: causal_graphs[0].edges[1..2] (lines 301-322)
  accessed_at: '2026-11-05T20:20:02Z'
  support: supports
  summary: In data/records/chlorite.yaml, causal_graphs[0].edges[1..2] (lines 305-306,
    310-311, 316-317, 321-322) interpolate capitalized 'Chlorite-associated Fe(III)
    (ferroan clinochlore)' mid-sentence with generic one-line explanations.
limitations:
- 5 of 7 mineral_group records (bastnaesite, biotite, illite, potassium-feldspar,
  vermiculite) have organic-acid or heterotrophic bioleaching/bioweathering mechanisms
  without strain-resolved enzymatic causal graphs in the cited primary studies.
notes:
- Cohort covers 100% (7/7) of mineral_group records in data/records/*.yaml at commit
  f8f0d8e724bcc013b5e9d98e3d12d5c7557587af.
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
    matching data/records/*.yaml where material_kind == 'mineral_group' at f8f0d8e724bcc013b5e9d98e3d12d5c7557587af
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-mineral-group-cohort-audit
```
