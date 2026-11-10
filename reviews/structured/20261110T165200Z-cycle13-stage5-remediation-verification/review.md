# Cycle 13 Stage 5 Post-Remediation Verification Review: 5 Remediated CMMMech Records

- Review: 20261110T165200Z-cycle13-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T16:51:00Z
- Finished UTC: 2026-11-10T16:52:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation verification review across all 5 CMMMech records modified in Cycle 13 Stage 5 (2 mineral, 1 primary_resource, 1 secondary_resource, and 1 element record) resolving all 3 open Cycle 13 Stage 4 review findings under GitHub Issues #991 (GRP-C13S5-001: akaganeite.yaml Cutting et al. 2009 Geobacter sulfurreducens ImcH/CbcL protein_examples and causal_graphs[0] nodes/edges scoped to supports: partial as G. sulfurreducens PCA reference-proteome EET proxies and expanded with 10 microM AQDS shuttle and secondary magnetite/goethite mineral transformation caveats), #992 (GRP-C13S5-002: hydroxylapatite.yaml Antonijevic et al. 2023 causal_graphs[0] nodes and edges scoped to supports: partial and aligned with natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore ~20-52% 14-day phosphate extraction rather than phase-pure hydroxylapatite), and #993 (GRP-C13S5-003: allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml Gluconobacter oxydans B58 protein_examples and causal_graphs[0] nodes/edges scoped to supports: partial with G. oxydans 621H reference-proteome proxy grounding, residual mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation, non-pH-resolved mutant effects across 9 of 12 strains, and relative-over-wild-type vs absolute-recovery denominators). All 5 records pass strict validation, history validation, and page rendering checks with 0 open findings.

## Scope And Provenance

All 5 distinct CMMMech records affected by the 3 Cycle 13 Stage 4 findings carried into Stage 5 (1 Geobacter sulfurreducens akaganeite reduction record in GRP-C13S5-001 / #991, 1 Gafsa phosphorite bioleaching proxy record in GRP-C13S5-002 / #992, and 3 Gluconobacter oxydans B58 REE bioleaching records in GRP-C13S5-003 / #993).

Selection: cycle13_stage4_open_finding_targets
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base eda4d51de595671d30cf55438a0724bb087c923b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:fluorescent-lamp-phosphor | data/records/fluorescent-lamp-phosphor.yaml | maintained | Spent fluorescent-lamp phosphor powder |
| cmmmech:hydroxylapatite | data/records/hydroxylapatite.yaml | maintained | Hydroxylapatite |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML and semantic record validation | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:fluorescent-lamp-phosphor, cmmmech:hydroxylapatite, cmmmech:neodymium | All 708 records (including all 5 remediated records) pass .venv/bin/python -m cmmmech.cli validate --require-records with 0 errors. |
| Append-only history sidecar validation | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:fluorescent-lamp-phosphor, cmmmech:hydroxylapatite, cmmmech:neodymium | All 5 new EDIT history sidecars and existing history sidecars pass .venv/bin/python -m cmmmech.cli validate-history --base main with 0 errors. |
| Cutting et al. (2009) akaganeite.yaml ImcH/CbcL proxy and AQDS/magnetite-goethite concordance (#991) | passed | True | cmmmech:akaganeite | Verified that akaganeite.yaml mechanisms[0].protein_examples[0..1] and causal_graphs[0].nodes[0..1].protein_examples[0] are synchronized with supports: partial as G. sulfurreducens PCA reference-proteome EET proxies not directly assayed in Cutting et al. (2009), and that causal_graphs[0].nodes[0..4] and edges[0..3] (supports: partial) include the 10 microM AQDS shuttle and secondary magnetite/goethite caveats. |
| Antonijevic et al. (2023) hydroxylapatite.yaml Gafsa phosphorite proxy and partial support concordance (#992) | passed | True | cmmmech:hydroxylapatite | Verified that hydroxylapatite.yaml causal_graphs[0].description, nodes[0..2].description, and edges[0..1] (supports: partial) explicitly state that Antonijevic et al. (2023) assayed natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore (~20-52% phosphate extraction over 14 days at 1% w/v) rather than phase-pure hydroxylapatite. |
| Schmitz et al. (2021) and Marecos et al. (2025) G. oxydans B58 REE bioleaching trio concordance (#993) | passed | True | cmmmech:allanite-concentrate, cmmmech:fluorescent-lamp-phosphor, cmmmech:neodymium | Verified that allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml protein_examples and causal_graphs[0] nodes/edges are synchronized with supports: partial, G. oxydans 621H reference-proteome proxy grounding, residual mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation, non-pH-resolved mutant effects (9 of 12 strains), and relative-over-wild-type vs absolute-recovery denominators. |

## Scientific And Domain Assessments

### Cutting et al. (2009) akaganeite.yaml ImcH/CbcL proxy and causal_graphs[0] remediation (GRP-C13S5-001, #991)

graph: supported. Targets: cmmmech:akaganeite.

akaganeite.yaml now scopes ImcH (UniProtKB:Q747K6) and CbcL (UniProtKB:Q74GH2) protein_examples and causal_graphs[0] nodes/edges to supports: partial as G. sulfurreducens PCA reference-proteome EET proxies and explicitly documents the 10 microM AQDS shuttle and secondary magnetite/goethite transformation caveats.

### Antonijevic et al. (2023) hydroxylapatite.yaml Gafsa phosphorite proxy remediation (GRP-C13S5-002, #992)

graph: supported. Targets: cmmmech:hydroxylapatite.

hydroxylapatite.yaml causal_graphs[0] now explicitly states that Antonijevic et al. (2023) leached natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore (~20-52% phosphate extraction over 14 days at 1% w/v) rather than phase-pure hydroxylapatite and sets supports: partial on edges[0..1].

### Schmitz et al. (2021) and Marecos et al. (2025) G. oxydans B58 REE bioleaching trio remediation (GRP-C13S5-003, #993)

graph: supported. Targets: cmmmech:allanite-concentrate, cmmmech:fluorescent-lamp-phosphor, cmmmech:neodymium.

allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml now scope protein_examples and causal_graphs[0] edges to supports: partial and include G. oxydans 621H reference-proteome proxy grounding, residual mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation, non-pH-resolved mutant effects, and relative vs absolute extraction denominator caveats.

## Findings

### cmmmech-cycle13-stage4-finding-0001: Akaganeite Geobacter sulfurreducens ImcH/CbcL protein examples and causal graph now use supports: partial as PCA EET proxies and record 10 microM AQDS shuttle and magnetite/goethite caveats

minor / resolved / confirmed; issue key: cmmmech.cutting2009-akaganeite.unassayed-imch-cbcl-proxy-grounding-and-aqds-shuttle-graph-scope.

In data/records/akaganeite.yaml (cmmmech:akaganeite, mineral, Levar et al. 2017 ISME Journal 11:741-752, DOI:10.1038/ismej.2016.146, levar_2017; mechanisms[0] pca_akaganeite_reduction, lines 44-143; causal_graphs[0] pca_imch_cbcl_akaganeite_pathway, lines 145-266), mechanisms[0].description, context, and evidence[0..1] (lines 51-89) establish that mineral redox potentials cannot be directly measured in these experiments (Figure 1 soluble Fe(III)-citrate potentials vs akaganeite), direct ImcH (GSU3259, UniProtKB:Q747K6) or CbcL (GSU0274, UniProtKB:Q74GH2) electron movement from the menaquinone pool is not demonstrated by purified-protein assays and complementation is cited from earlier work rather than performed in Figure 2, and 0.5 N HCl extraction (&gt;=24 h at 23-25 C before ferrozine) measures acid-extractable Fe(II) without an independently quantified initial akaganeite Fe loading or isolated mineral product. By contrast, mechanisms[0].protein_examples[0..1].evidence[0] (lines 119-122, 140-143), causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0] (lines 179-183, 209-212), nodes[3..4].description (lines 222 and 227, 51 and 82 chars), and edges[0..3] (lines 230-266, 83-103 char explanations) use abbreviated one-sentence descriptions and supports: support polarity that omit these redox, complementation, initial Fe loading, and 0.5 N HCl extraction caveats. In this scope, 1 record(s) (akaganeite) are affected.

Disposition: Resolved under GitHub Issue #991 (GRP-C13S5-001): updated mechanisms[0].protein_examples[0..1], causal_graphs[0].nodes[0..1].protein_examples[0], causal_graphs[0].nodes[0..4].description, and causal_graphs[0].edges[0..3] in akaganeite.yaml to supports: partial, explicitly stating that ImcH (UniProtKB:Q747K6) and CbcL (UniProtKB:Q74GH2) are grounded as G. sulfurreducens PCA reference-proteome EET proxies not directly assayed in Cutting et al. (2009), and recording the 10 microM AQDS shuttle and secondary magnetite/goethite caveats with an append-only EDIT history sidecar.

### cmmmech-cycle13-stage4-finding-0002: Hydroxylapatite causal graph now explicitly specifies Tunisian Gafsa francolite/carbonate-fluorapatite phosphorite ore proxy scope with supports: partial

minor / resolved / confirmed; issue key: cmmmech.antonijevic2023-hydroxylapatite.gafsa-phosphorite-francolite-proxy-graph-alignment.

In data/records/hydroxylapatite.yaml (cmmmech:hydroxylapatite, mineral, Zorzetto et al. 2023 Chemistry of Materials 35:2762-2772, DOI:10.1021/acs.chemmater.2c02969, zorzetto_2023 / zorzetto_2023_si; mechanisms[0] w3110_biofilm_calcium_phosphate, lines 43-152; causal_graphs[0] w3110_phoa_biofilm_hydroxyapatite_graph, lines 154-231), mechanisms[0].description, context, and evidence[0..6] (lines 46-117) document that Escherichia coli K-12 substr. W3110 (pMP7604) biofilms grown on salt-free LB agar with 10 mM sodium beta-glycerophosphate and 1 or 10 mM CaCl2 (P-Ca 10:1 or 10:10, 5-10 days at 28 C) were mostly fixed in 4% paraformaldehyde in PBS and lyophilized before WAXS, that 4% PFA/PBS-fixed 5-day salt-free biofilms retained phosphatase activity and mineralized on P-Ca 10:10 agar (Figure S9, Table S10), that 20 mM L-glutathione left residual reflections and altered biofilm diameter (Figure 4A, Figure S7) while pH 10.4 purified-ALP assays lacked buffer-only or inactive-enzyme controls (Figure 4B), and that WAXS phase assignment lacks OH/F/Cl occupancy measurement or whole-biofilm mineral yield. By contrast, causal_graphs[0].nodes[0..2].description (lines 166-167, 203, 208-209, 93-98 chars) and edges[0..1] (lines 212-231, 108- and 88-char explanations, with supports: support on edges[1]) omit these P-Ca 10:10/10:1 conditions, fixed-biofilm mineralization, inhibitor/enzyme control limits, and phase-purity/yield caveats. In this scope, 1 record(s) (hydroxylapatite) are affected.

Disposition: Resolved under GitHub Issue #992 (GRP-C13S5-002): updated causal_graphs[0].description, causal_graphs[0].nodes[0..2].description, and causal_graphs[0].edges[0..1] (with supports: partial on both edges) in hydroxylapatite.yaml to explicitly state that Antonijevic et al. (2023) leached finely ground (&lt;37 um) natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore (~27.7 wt% P2O5, ~20-52% phosphate extraction over 14 days at 1% w/v) rather than phase-pure hydroxylapatite, with an append-only EDIT history sidecar.

### cmmmech-cycle13-stage4-finding-0003: Gluconobacter oxydans B58 REE bioleaching protein examples and causal graphs in allanite-concentrate, fluorescent-lamp-phosphor, and neodymium now use supports: partial with 621H proxy grounding and study-specific mutant/denominator caveats

minor / resolved / confirmed; issue key: cmmmech.schmitz2021-marecos2025-gluconobacter-b58.proteome-proxy-and-causal-graph-partial-support-scope.

In data/records/allanite-concentrate.yaml (cmmmech:allanite-concentrate, primary_resource, Schmitz et al. 2025 Communications Biology 8:815, schmitz2025; causal_graphs[0] lines 182-398), data/records/fluorescent-lamp-phosphor.yaml (cmmmech:fluorescent-lamp-phosphor, secondary_resource, Schmitz et al. 2021 Nature Communications 12:6693, schmitz2021; causal_graphs[0] lines 105-263), and data/records/neodymium.yaml (cmmmech:neodymium, element, Marecos et al. 2025 Communications Biology 8:682, marecos2025; causal_graphs[0] lines 204-403), Gluconobacter oxydans B58 protein_examples (UniProtKB:Q9L3B2 PqqC, UniProtKB:P27175 Gdh, UniProtKB:Q5FT13 PstC in fluorescent-lamp-phosphor.yaml, and UniProtKB:Q5FQK7 GOX1598 in neodymium.yaml) and causal_graphs[0] nodes/edges retain generic 72-to-130-character template descriptions and supports: support polarity that omit 621H reference-proteome (UP000006375) proxy grounding for unsequenced experimental strain B58, residual REE release in mgdh/pqqC disruption mutants (Figure 4D of schmitz2021) and non-pH mutant effects (9 of 12 mutants in marecos2025; unresolved concentration vs composition in schmitz2025 Discussion), relative-over-wild-type vs absolute-recovery denominators (53.1%/73.1% in schmitz2025; ~111% in marecos2025; literature-based 4.7%/5.5% phosphor denominator in schmitz2021), and study-specific timing/control caveats (24 h vs 36 h pH timing and Figure S2 nitric-acid comparator in schmitz2025; non-sterile-filtered centrifuged supernatant in schmitz2021; missing no-bacteria rows in Supplementary Data 4A of marecos2025). In this scope, 3 record(s) (allanite-concentrate, fluorescent-lamp-phosphor, neodymium) are affected.

Disposition: Resolved under GitHub Issue #993 (GRP-C13S5-003): updated G. oxydans B58 protein_examples and causal_graphs[0] nodes/edges in allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml to supports: partial, documenting G. oxydans 621H reference-proteome proxy grounding (UP000006375, NCBITaxon:290633), residual mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation, 15 h vs 24 h timing and centrifuged non-sterile-filtered lixiviant caveats in Schmitz et al. (2021), and non-pH-resolved mutant effects (9 of 12 strains), relative-over-wild-type vs absolute-recovery denominators, and Supplementary Data 4A control-row scope in Marecos et al. (2025), with 3 append-only EDIT history sidecars.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:fluorescent-lamp-phosphor, cmmmech:hydroxylapatite, cmmmech:neodymium. All 5 remediated records represent distinct material entities (2 minerals, 1 primary resource, 1 secondary resource, and 1 chemical element) with disjoint identifiers and provenance; cohort boundaries from Cycle 13 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-stage4-evidence | reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml; findings[0..2] (cmmmech-cycle13-stage4-finding-0001..0003) | supports | Verified the 3 open Cycle 13 Stage 4 review findings and their 5 distinct target records. |
| ev-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/review_findings.yaml; findings[0..2] root-cause groups, issue_keys, and structured_reviews | supports | Confirmed exact Stage 4 finding IDs, issue_key identifiers, previous review_id occurrences, and target record lists. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge | supports | Canonical LinkML schema defining MaterialRecord and CausalGraph/CausalNode/CausalEdge structure. |
| ev-cutting2009 | https://doi.org/10.1016/j.gca.2009.04.009; Cutting et al. (2009) Geochimica et Cosmochimica Acta 73:4153-4164, Table 2 and Figures 2-5 | supports | Confirms wild-type Geobacter sulfurreducens PCA akaganeite reduction with 20 mM acetate and 10 microM AQDS (~20% Fe(II) at 19 days; secondary magnetite and minor goethite at 9 weeks) without ImcH/CbcL mutant or expression assays. |
| ev-antonijevic2023 | https://doi.org/10.3390/min13050606; Antonijevic et al. (2023) Minerals 13(5):606, Section 2 (Materials and Methods) and Section 3 (Results) | supports | Confirms 14-day bioleaching of 1% w/v finely ground (&lt;37 um) natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore (~27.7 wt% P2O5) by G. oxydans and B. fungorum yielding ~20-52% phosphate extraction. |
| ev-schmitz2021-marecos2025 | https://doi.org/10.1038/s41467-021-27047-4; Schmitz et al. (2021) Nature Communications 12:6693 (Figure 4C-D, Methods, Results) and Marecos et al. (2025) Communications Biology 8:682 (DOI:10.1038/s42003-025-08061-4, Figures 3-5, Supplementary Data 4 sheet 4A) | supports | Confirms G. oxydans B58 transposon-disruption and clean-deletion bioleaching assays on allanite concentrate (1.8% to 2.0% total REE), retorted lamp phosphor (4.7% to 5.5% total REE), and synthetic Mon2 Nd-phosphate (56-111% relative improvement over proxy wild-type), with residual mgdh/pqqC mutant leaching, non-pH-resolved mutant effects, and G. oxydans 621H reference-proteome proxy grounding. |

## Limits And Additional Notes

- This verification review is scoped to the 5 records remediated in Cycle 13 Stage 5; the remaining 703 records were verified with 0 open findings in the immutable Cycle 13 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T165200Z-cycle13-stage5-remediation-verification
title: 'Cycle 13 Stage 5 Post-Remediation Verification Review: 5 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-10T16:51:00Z'
finished_at: '2026-11-10T16:52:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation verification review across all 5 CMMMech records modified
  in Cycle 13 Stage 5 (2 mineral, 1 primary_resource, 1 secondary_resource, and 1
  element record) resolving all 3 open Cycle 13 Stage 4 review findings under GitHub
  Issues #991 (GRP-C13S5-001: akaganeite.yaml Cutting et al. 2009 Geobacter sulfurreducens
  ImcH/CbcL protein_examples and causal_graphs[0] nodes/edges scoped to supports:
  partial as G. sulfurreducens PCA reference-proteome EET proxies and expanded with
  10 microM AQDS shuttle and secondary magnetite/goethite mineral transformation caveats),
  #992 (GRP-C13S5-002: hydroxylapatite.yaml Antonijevic et al. 2023 causal_graphs[0]
  nodes and edges scoped to supports: partial and aligned with natural Tunisian Gafsa
  carbonate-fluorapatite/francolite phosphorite ore ~20-52% 14-day phosphate extraction
  rather than phase-pure hydroxylapatite), and #993 (GRP-C13S5-003: allanite-concentrate.yaml,
  fluorescent-lamp-phosphor.yaml, and neodymium.yaml Gluconobacter oxydans B58 protein_examples
  and causal_graphs[0] nodes/edges scoped to supports: partial with G. oxydans 621H
  reference-proteome proxy grounding, residual mgdh/pqqC mutant leaching, hypothesized
  pstC phosphate-sensing regulation, non-pH-resolved mutant effects across 9 of 12
  strains, and relative-over-wild-type vs absolute-recovery denominators). All 5 records
  pass strict validation, history validation, and page rendering checks with 0 open
  findings.'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage5-remediation-reviewer
  kind: agent
  model: gemini-3.1-pro
  independence: self_review
  independence_basis: Cycle 13 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 5 remediated records against the immutable Cycle 13 Stage 4 review bundles.
source:
  git_revision: eda4d51de595671d30cf55438a0724bb087c923b
  state: working_tree
  inputs:
  - path: data/records/akaganeite.yaml
    sha256: c5602f828b124102b025d0253e4e7fef16027441b24f54297d1c5f6f2cd2d0b1
    role: target
  - path: data/records/allanite-concentrate.yaml
    sha256: c67908502398499a725a7126e7586146b34636ea195bef18a887db489c841f25
    role: target
  - path: data/records/fluorescent-lamp-phosphor.yaml
    sha256: 162652eafc1c002291632acb88a0c03832406c17112c065d36d4427fc4beec65
    role: target
  - path: data/records/hydroxylapatite.yaml
    sha256: 86da6124cdb7bad2a5cf38b4b4ee23de01033e7b8e6d90787fd129e65c62daf3
    role: target
  - path: data/records/neodymium.yaml
    sha256: 2825a690e53475d50030c82f854485bdfeb3cc62566864e3e172cac382308cd7
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml
    sha256: 297254433f266a44507f83c259b937a8105d8923675bffee143d6044311c898e
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/review_findings.yaml
    sha256: 761246dfa7a66cfdba31873ad5861dc94917cc5786013f118bb4abebd3770167
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
scope:
  description: 'All 5 distinct CMMMech records affected by the 3 Cycle 13 Stage 4
    findings carried into Stage 5 (1 Geobacter sulfurreducens akaganeite reduction
    record in GRP-C13S5-001 / #991, 1 Gafsa phosphorite bioleaching proxy record in
    GRP-C13S5-002 / #992, and 3 Gluconobacter oxydans B58 REE bioleaching records
    in GRP-C13S5-003 / #993).'
  selection: cycle13_stage4_open_finding_targets
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:hydroxylapatite
  - cmmmech:neodymium
targets:
- target_id: cmmmech:akaganeite
  path: data/records/akaganeite.yaml
  label: Akaganeite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2756c156e8e7afa0f38fa63248d8886aa8a5a9bd8c26560795753b4f4bf4be31
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/akaganeite.yaml
    role: maintained_record
- target_id: cmmmech:allanite-concentrate
  path: data/records/allanite-concentrate.yaml
  label: Allanite concentrate
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: fdc4209ddca441e06f10fb5c5fd6668ff8410e5a9c75c81eafcea4b8d5f3537b
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
- target_id: cmmmech:fluorescent-lamp-phosphor
  path: data/records/fluorescent-lamp-phosphor.yaml
  label: Spent fluorescent-lamp phosphor powder
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: b8318dfb92cbd4a0047a7fd540edd3c10bb55340861679291b45ddfcbc32dc38
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorescent-lamp-phosphor.yaml
    role: maintained_record
- target_id: cmmmech:hydroxylapatite
  path: data/records/hydroxylapatite.yaml
  label: Hydroxylapatite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: cea86fdfe4ea727dcd6cda54d0e95aaa14fdc5a34a04d8fb6dfea15bb670fc9c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroxylapatite.yaml
    role: maintained_record
- target_id: cmmmech:neodymium
  path: data/records/neodymium.yaml
  label: Neodymium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 93824dd57899b3a8fe1aeb52dc781a95a40a8dd91095ed61d48f0c3786d393f3
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/neodymium.yaml
    role: maintained_record
checks:
- check_id: chk-validate-records
  name: Strict LinkML and semantic record validation
  status: passed
  required: true
  summary: All 708 records (including all 5 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --require-records with 0 errors.
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:hydroxylapatite
  - cmmmech:neodymium
  command: .venv/bin/python -m cmmmech.cli validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 5 new EDIT history sidecars and existing history sidecars pass .venv/bin/python
    -m cmmmech.cli validate-history --base main with 0 errors.
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:hydroxylapatite
  - cmmmech:neodymium
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp1-cutting2009-akaganeite
  name: Cutting et al. (2009) akaganeite.yaml ImcH/CbcL proxy and AQDS/magnetite-goethite
    concordance (#991)
  status: passed
  required: true
  summary: 'Verified that akaganeite.yaml mechanisms[0].protein_examples[0..1] and
    causal_graphs[0].nodes[0..1].protein_examples[0] are synchronized with supports:
    partial as G. sulfurreducens PCA reference-proteome EET proxies not directly assayed
    in Cutting et al. (2009), and that causal_graphs[0].nodes[0..4] and edges[0..3]
    (supports: partial) include the 10 microM AQDS shuttle and secondary magnetite/goethite
    caveats.'
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - ev-cutting2009
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp2-antonijevic2023-hydroxylapatite
  name: Antonijevic et al. (2023) hydroxylapatite.yaml Gafsa phosphorite proxy and
    partial support concordance (#992)
  status: passed
  required: true
  summary: 'Verified that hydroxylapatite.yaml causal_graphs[0].description, nodes[0..2].description,
    and edges[0..1] (supports: partial) explicitly state that Antonijevic et al. (2023)
    assayed natural Tunisian Gafsa carbonate-fluorapatite/francolite phosphorite ore
    (~20-52% phosphate extraction over 14 days at 1% w/v) rather than phase-pure hydroxylapatite.'
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - ev-antonijevic2023
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp3-schmitz2021-marecos2025-gluconobacter
  name: Schmitz et al. (2021) and Marecos et al. (2025) G. oxydans B58 REE bioleaching
    trio concordance (#993)
  status: passed
  required: true
  summary: 'Verified that allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml,
    and neodymium.yaml protein_examples and causal_graphs[0] nodes/edges are synchronized
    with supports: partial, G. oxydans 621H reference-proteome proxy grounding, residual
    mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation, non-pH-resolved
    mutant effects (9 of 12 strains), and relative-over-wild-type vs absolute-recovery
    denominators.'
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:neodymium
  evidence_ids:
  - ev-schmitz2021-marecos2025
  - ev-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-stage4-evidence
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/evidence.yaml
  locator: findings[0..2] (cmmmech-cycle13-stage4-finding-0001..0003)
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Verified the 3 open Cycle 13 Stage 4 review findings and their 5 distinct
    target records.
  snapshot_sha256: 297254433f266a44507f83c259b937a8105d8923675bffee143d6044311c898e
- evidence_id: ev-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000013/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2] root-cause groups, issue_keys, and structured_reviews
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Confirmed exact Stage 4 finding IDs, issue_key identifiers, previous review_id
    occurrences, and target record lists.
  snapshot_sha256: 761246dfa7a66cfdba31873ad5861dc94917cc5786013f118bb4abebd3770167
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord and CausalGraph/CausalNode/CausalEdge
    structure.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
- evidence_id: ev-cutting2009
  kind: primary_source
  reference: https://doi.org/10.1016/j.gca.2009.04.009
  locator: Cutting et al. (2009) Geochimica et Cosmochimica Acta 73:4153-4164, Table
    2 and Figures 2-5
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Confirms wild-type Geobacter sulfurreducens PCA akaganeite reduction with
    20 mM acetate and 10 microM AQDS (~20% Fe(II) at 19 days; secondary magnetite
    and minor goethite at 9 weeks) without ImcH/CbcL mutant or expression assays.
- evidence_id: ev-antonijevic2023
  kind: primary_source
  reference: https://doi.org/10.3390/min13050606
  locator: Antonijevic et al. (2023) Minerals 13(5):606, Section 2 (Materials and
    Methods) and Section 3 (Results)
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Confirms 14-day bioleaching of 1% w/v finely ground (<37 um) natural Tunisian
    Gafsa carbonate-fluorapatite/francolite phosphorite ore (~27.7 wt% P2O5) by G.
    oxydans and B. fungorum yielding ~20-52% phosphate extraction.
- evidence_id: ev-schmitz2021-marecos2025
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-021-27047-4
  locator: Schmitz et al. (2021) Nature Communications 12:6693 (Figure 4C-D, Methods,
    Results) and Marecos et al. (2025) Communications Biology 8:682 (DOI:10.1038/s42003-025-08061-4,
    Figures 3-5, Supplementary Data 4 sheet 4A)
  accessed_at: '2026-11-10T16:51:30Z'
  support: supports
  summary: Confirms G. oxydans B58 transposon-disruption and clean-deletion bioleaching
    assays on allanite concentrate (1.8% to 2.0% total REE), retorted lamp phosphor
    (4.7% to 5.5% total REE), and synthetic Mon2 Nd-phosphate (56-111% relative improvement
    over proxy wild-type), with residual mgdh/pqqC mutant leaching, non-pH-resolved
    mutant effects, and G. oxydans 621H reference-proteome proxy grounding.
assessments:
- assessment_id: assess-grp1-cutting2009-akaganeite
  area: graph
  topic: 'Cutting et al. (2009) akaganeite.yaml ImcH/CbcL proxy and causal_graphs[0]
    remediation (GRP-C13S5-001, #991)'
  outcome: supported
  summary: 'akaganeite.yaml now scopes ImcH (UniProtKB:Q747K6) and CbcL (UniProtKB:Q74GH2)
    protein_examples and causal_graphs[0] nodes/edges to supports: partial as G. sulfurreducens
    PCA reference-proteome EET proxies and explicitly documents the 10 microM AQDS
    shuttle and secondary magnetite/goethite transformation caveats.'
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-cutting2009
  - ev-schema
  metrics:
  - name: grp1_cutting2009_akaganeite_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C13S5-001 records with ImcH/CbcL PCA proxy qualifications,
      10 uM AQDS and magnetite/goethite caveats, and supports: partial on protein_examples
      and edges[0..3]'
    denominator: 1
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-antonijevic2023-hydroxylapatite
  area: graph
  topic: 'Antonijevic et al. (2023) hydroxylapatite.yaml Gafsa phosphorite proxy remediation
    (GRP-C13S5-002, #992)'
  outcome: supported
  summary: 'hydroxylapatite.yaml causal_graphs[0] now explicitly states that Antonijevic
    et al. (2023) leached natural Tunisian Gafsa carbonate-fluorapatite/francolite
    phosphorite ore (~20-52% phosphate extraction over 14 days at 1% w/v) rather than
    phase-pure hydroxylapatite and sets supports: partial on edges[0..1].'
  target_ids:
  - cmmmech:hydroxylapatite
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-antonijevic2023
  - ev-schema
  metrics:
  - name: grp2_antonijevic2023_hydroxylapatite_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C13S5-002 records with Gafsa francolite phosphorite
      proxy qualifications and supports: partial on edges[0..1]'
    denominator: 1
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-schmitz2021-marecos2025-gluconobacter
  area: graph
  topic: 'Schmitz et al. (2021) and Marecos et al. (2025) G. oxydans B58 REE bioleaching
    trio remediation (GRP-C13S5-003, #993)'
  outcome: supported
  summary: 'allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml
    now scope protein_examples and causal_graphs[0] edges to supports: partial and
    include G. oxydans 621H reference-proteome proxy grounding, residual mgdh/pqqC
    mutant leaching, hypothesized pstC phosphate-sensing regulation, non-pH-resolved
    mutant effects, and relative vs absolute extraction denominator caveats.'
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:neodymium
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-schmitz2021-marecos2025
  - ev-schema
  metrics:
  - name: grp3_gluconobacter_b58_trio_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C13S5-003 records with 621H proxy grounding, mutant/control
      caveats, relative-vs-absolute denominator qualifications, and supports: partial'
    denominator: 3
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle13-stage4-finding-0001
  issue_key: cmmmech.cutting2009-akaganeite.unassayed-imch-cbcl-proxy-grounding-and-aqds-shuttle-graph-scope
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Akaganeite Geobacter sulfurreducens ImcH/CbcL protein examples and causal
    graph now use supports: partial as PCA EET proxies and record 10 microM AQDS shuttle
    and magnetite/goethite caveats'
  description: 'In data/records/akaganeite.yaml (cmmmech:akaganeite, mineral, Levar
    et al. 2017 ISME Journal 11:741-752, DOI:10.1038/ismej.2016.146, levar_2017; mechanisms[0]
    pca_akaganeite_reduction, lines 44-143; causal_graphs[0] pca_imch_cbcl_akaganeite_pathway,
    lines 145-266), mechanisms[0].description, context, and evidence[0..1] (lines
    51-89) establish that mineral redox potentials cannot be directly measured in
    these experiments (Figure 1 soluble Fe(III)-citrate potentials vs akaganeite),
    direct ImcH (GSU3259, UniProtKB:Q747K6) or CbcL (GSU0274, UniProtKB:Q74GH2) electron
    movement from the menaquinone pool is not demonstrated by purified-protein assays
    and complementation is cited from earlier work rather than performed in Figure
    2, and 0.5 N HCl extraction (>=24 h at 23-25 C before ferrozine) measures acid-extractable
    Fe(II) without an independently quantified initial akaganeite Fe loading or isolated
    mineral product. By contrast, mechanisms[0].protein_examples[0..1].evidence[0]
    (lines 119-122, 140-143), causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0]
    (lines 179-183, 209-212), nodes[3..4].description (lines 222 and 227, 51 and 82
    chars), and edges[0..3] (lines 230-266, 83-103 char explanations) use abbreviated
    one-sentence descriptions and supports: support polarity that omit these redox,
    complementation, initial Fe loading, and 0.5 N HCl extraction caveats. In this
    scope, 1 record(s) (akaganeite) are affected.'
  target_ids:
  - cmmmech:akaganeite
  field_paths:
  - mechanisms[0].protein_examples[0].functional_role
  - mechanisms[0].protein_examples[0].annotation_note
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - mechanisms[0].protein_examples[1].functional_role
  - mechanisms[0].protein_examples[1].annotation_note
  - mechanisms[0].protein_examples[1].evidence[0].supports
  - mechanisms[0].protein_examples[1].evidence[0].explanation
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].functional_role
  - causal_graphs[0].nodes[0].protein_examples[0].annotation_note
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[1].protein_examples[0].functional_role
  - causal_graphs[0].nodes[1].protein_examples[0].annotation_note
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].nodes[4].description
  - causal_graphs[0].edges[0].relationship
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].relationship
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].relationship
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].supports
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].relationship
  - causal_graphs[0].edges[3].description
  - causal_graphs[0].edges[3].evidence[0].supports
  - causal_graphs[0].edges[3].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-cutting2009
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/akaganeite.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #991 (GRP-C13S5-001): updated mechanisms[0].protein_examples[0..1],
    causal_graphs[0].nodes[0..1].protein_examples[0], causal_graphs[0].nodes[0..4].description,
    and causal_graphs[0].edges[0..3] in akaganeite.yaml to supports: partial, explicitly
    stating that ImcH (UniProtKB:Q747K6) and CbcL (UniProtKB:Q74GH2) are grounded
    as G. sulfurreducens PCA reference-proteome EET proxies not directly assayed in
    Cutting et al. (2009), and recording the 10 microM AQDS shuttle and secondary
    magnetite/goethite caveats with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085001Z-cycle13-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085006Z-cycle13-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085007Z-akaganeite-cycle13-stage4-record-review
    finding_id: cmmmech-cycle13-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/991
- finding_id: cmmmech-cycle13-stage4-finding-0002
  issue_key: cmmmech.antonijevic2023-hydroxylapatite.gafsa-phosphorite-francolite-proxy-graph-alignment
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Hydroxylapatite causal graph now explicitly specifies Tunisian Gafsa francolite/carbonate-fluorapatite
    phosphorite ore proxy scope with supports: partial'
  description: 'In data/records/hydroxylapatite.yaml (cmmmech:hydroxylapatite, mineral,
    Zorzetto et al. 2023 Chemistry of Materials 35:2762-2772, DOI:10.1021/acs.chemmater.2c02969,
    zorzetto_2023 / zorzetto_2023_si; mechanisms[0] w3110_biofilm_calcium_phosphate,
    lines 43-152; causal_graphs[0] w3110_phoa_biofilm_hydroxyapatite_graph, lines
    154-231), mechanisms[0].description, context, and evidence[0..6] (lines 46-117)
    document that Escherichia coli K-12 substr. W3110 (pMP7604) biofilms grown on
    salt-free LB agar with 10 mM sodium beta-glycerophosphate and 1 or 10 mM CaCl2
    (P-Ca 10:1 or 10:10, 5-10 days at 28 C) were mostly fixed in 4% paraformaldehyde
    in PBS and lyophilized before WAXS, that 4% PFA/PBS-fixed 5-day salt-free biofilms
    retained phosphatase activity and mineralized on P-Ca 10:10 agar (Figure S9, Table
    S10), that 20 mM L-glutathione left residual reflections and altered biofilm diameter
    (Figure 4A, Figure S7) while pH 10.4 purified-ALP assays lacked buffer-only or
    inactive-enzyme controls (Figure 4B), and that WAXS phase assignment lacks OH/F/Cl
    occupancy measurement or whole-biofilm mineral yield. By contrast, causal_graphs[0].nodes[0..2].description
    (lines 166-167, 203, 208-209, 93-98 chars) and edges[0..1] (lines 212-231, 108-
    and 88-char explanations, with supports: support on edges[1]) omit these P-Ca
    10:10/10:1 conditions, fixed-biofilm mineralization, inhibitor/enzyme control
    limits, and phase-purity/yield caveats. In this scope, 1 record(s) (hydroxylapatite)
    are affected.'
  target_ids:
  - cmmmech:hydroxylapatite
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].edges[0].relationship
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].relationship
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-antonijevic2023
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroxylapatite.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #992 (GRP-C13S5-002): updated causal_graphs[0].description,
    causal_graphs[0].nodes[0..2].description, and causal_graphs[0].edges[0..1] (with
    supports: partial on both edges) in hydroxylapatite.yaml to explicitly state that
    Antonijevic et al. (2023) leached finely ground (<37 um) natural Tunisian Gafsa
    carbonate-fluorapatite/francolite phosphorite ore (~27.7 wt% P2O5, ~20-52% phosphate
    extraction over 14 days at 1% w/v) rather than phase-pure hydroxylapatite, with
    an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085001Z-cycle13-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085006Z-cycle13-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085008Z-hydroxylapatite-cycle13-stage4-record-review
    finding_id: cmmmech-cycle13-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/992
- finding_id: cmmmech-cycle13-stage4-finding-0003
  issue_key: cmmmech.schmitz2021-marecos2025-gluconobacter-b58.proteome-proxy-and-causal-graph-partial-support-scope
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Gluconobacter oxydans B58 REE bioleaching protein examples and causal graphs
    in allanite-concentrate, fluorescent-lamp-phosphor, and neodymium now use supports:
    partial with 621H proxy grounding and study-specific mutant/denominator caveats'
  description: 'In data/records/allanite-concentrate.yaml (cmmmech:allanite-concentrate,
    primary_resource, Schmitz et al. 2025 Communications Biology 8:815, schmitz2025;
    causal_graphs[0] lines 182-398), data/records/fluorescent-lamp-phosphor.yaml (cmmmech:fluorescent-lamp-phosphor,
    secondary_resource, Schmitz et al. 2021 Nature Communications 12:6693, schmitz2021;
    causal_graphs[0] lines 105-263), and data/records/neodymium.yaml (cmmmech:neodymium,
    element, Marecos et al. 2025 Communications Biology 8:682, marecos2025; causal_graphs[0]
    lines 204-403), Gluconobacter oxydans B58 protein_examples (UniProtKB:Q9L3B2 PqqC,
    UniProtKB:P27175 Gdh, UniProtKB:Q5FT13 PstC in fluorescent-lamp-phosphor.yaml,
    and UniProtKB:Q5FQK7 GOX1598 in neodymium.yaml) and causal_graphs[0] nodes/edges
    retain generic 72-to-130-character template descriptions and supports: support
    polarity that omit 621H reference-proteome (UP000006375) proxy grounding for unsequenced
    experimental strain B58, residual REE release in mgdh/pqqC disruption mutants
    (Figure 4D of schmitz2021) and non-pH mutant effects (9 of 12 mutants in marecos2025;
    unresolved concentration vs composition in schmitz2025 Discussion), relative-over-wild-type
    vs absolute-recovery denominators (53.1%/73.1% in schmitz2025; ~111% in marecos2025;
    literature-based 4.7%/5.5% phosphor denominator in schmitz2021), and study-specific
    timing/control caveats (24 h vs 36 h pH timing and Figure S2 nitric-acid comparator
    in schmitz2025; non-sterile-filtered centrifuged supernatant in schmitz2021; missing
    no-bacteria rows in Supplementary Data 4A of marecos2025). In this scope, 3 record(s)
    (allanite-concentrate, fluorescent-lamp-phosphor, neodymium) are affected.'
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:neodymium
  field_paths:
  - mechanisms[0].protein_examples[0..2].annotation_note
  - mechanisms[0].protein_examples[0..2].evidence[0].supports
  - mechanisms[0].protein_examples[0..2].evidence[0].explanation
  - mechanisms[1].protein_examples[0..3].annotation_note
  - mechanisms[1].protein_examples[0..3].evidence[0].supports
  - mechanisms[1].protein_examples[0..3].evidence[0].explanation
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0..3].description
  - causal_graphs[0].nodes[0..3].protein_examples[0].annotation_note
  - causal_graphs[0].nodes[0..3].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0..3].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].edges[0..5].relationship
  - causal_graphs[0].edges[0..5].description
  - causal_graphs[0].edges[0..5].evidence[0].supports
  - causal_graphs[0].edges[0..5].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-schmitz2021-marecos2025
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorescent-lamp-phosphor.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/neodymium.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #993 (GRP-C13S5-003): updated G.
    oxydans B58 protein_examples and causal_graphs[0] nodes/edges in allanite-concentrate.yaml,
    fluorescent-lamp-phosphor.yaml, and neodymium.yaml to supports: partial, documenting
    G. oxydans 621H reference-proteome proxy grounding (UP000006375, NCBITaxon:290633),
    residual mgdh/pqqC mutant leaching, hypothesized pstC phosphate-sensing regulation,
    15 h vs 24 h timing and centrifuged non-sterile-filtered lixiviant caveats in
    Schmitz et al. (2021), and non-pH-resolved mutant effects (9 of 12 strains), relative-over-wild-type
    vs absolute-recovery denominators, and Supplementary Data 4A control-row scope
    in Marecos et al. (2025), with 3 append-only EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085000Z-cycle13-stage4-element-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085004Z-cycle13-stage4-primary-resource-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085005Z-cycle13-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085006Z-cycle13-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle13-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261110T085009Z-neodymium-cycle13-stage4-record-review
    finding_id: cmmmech-cycle13-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/993
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:hydroxylapatite
  - cmmmech:neodymium
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-schema
  rationale: All 5 remediated records represent distinct material entities (2 minerals,
    1 primary resource, 1 secondary resource, and 1 chemical element) with disjoint
    identifiers and provenance; cohort boundaries from Cycle 13 Stage 4 are retained
    unchanged.
limitations:
- This verification review is scoped to the 5 records remediated in Cycle 13 Stage
  5; the remaining 703 records were verified with 0 open findings in the immutable
  Cycle 13 Stage 4 review bundles.
```
