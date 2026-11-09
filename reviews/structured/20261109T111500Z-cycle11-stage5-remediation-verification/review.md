# Cycle 11 Stage 5 Post-Remediation Verification Review: 5 Remediated CMMMech Records

- Review: 20261109T111500Z-cycle11-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T11:14:00Z
- Finished UTC: 2026-11-09T11:15:00Z
- Reviewer: antigravity / cmmmech-cycle11-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation verification review across all 5 CMMMech records modified in Cycle 11 Stage 5 (2 mineral, 1 mineral_group, 1 primary_resource, and 1 element record) resolving all 3 open Cycle 11 Stage 4 review findings under GitHub Issues #967 (GRP-C11S5-001: enstatite.yaml, olivine-group.yaml, and dunite.yaml Gluconobacter oxydans whole-culture biolixiviant silicate bioleaching causal graphs and pqqC/gdh protein_examples updated with Klug et al. 2026 and Lee et al. 2025 study-specific prose and supports: partial), #968 (GRP-C11S5-002: metacinnabar.yaml Vazquez-Rodriguez et al. 2015 SoxB protein_examples and causal_graphs[0] updated to distinguish the primary 2 g/L ground natural museum metacinnabar feed from synthetic black HgS and qualify edges[1] aqueous-Hg support to partial), and #969 (GRP-C11S5-003: scandium.yaml Dong et al. 2024 Mex-LanM protein_examples and causal_graphs[0] updated to supports: partial on binding/protein evidence and aligned with the synthetic pH 3.0 16-REE chloride feed and stepwise 30 mM / 50 mM malonate elution at pH 5.0). All 5 records pass strict validation, history validation, and page rendering checks with 0 open findings.

## Scope And Provenance

All 5 distinct CMMMech records affected by the 3 Cycle 11 Stage 4 findings carried into Stage 5 (3 Gluconobacter oxydans silicate bioleaching records in GRP-C11S5-001 / #967, 1 Thiobacillus thioparus metacinnabar record in GRP-C11S5-002 / #968, and 1 Mex-LanM scandium chromatography record in GRP-C11S5-003 / #969).

Selection: cycle11_stage4_open_finding_targets
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base e5435802649ba486fc86d883ffed926e23fa8719.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |
| cmmmech:enstatite | data/records/enstatite.yaml | maintained | Enstatite |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML and semantic record validation | passed | True | cmmmech:dunite, cmmmech:enstatite, cmmmech:metacinnabar, cmmmech:olivine-group, cmmmech:scandium | All 698 records (including all 5 remediated records) pass .venv/bin/python -m cmmmech.cli validate --require-records with 0 errors. |
| Append-only history sidecar validation | passed | True | cmmmech:dunite, cmmmech:enstatite, cmmmech:metacinnabar, cmmmech:olivine-group, cmmmech:scandium | All 5 new EDIT history sidecars and existing history sidecars pass .venv/bin/python -m cmmmech.cli validate-history --base main with 0 errors. |
| Klug et al. (2026) and Lee et al. (2025) enstatite, olivine-group, and dunite concordance (#967) | passed | True | cmmmech:dunite, cmmmech:enstatite, cmmmech:olivine-group | Verified that enstatite.yaml causal_graphs[0].nodes[4].description specifies the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed feed (5% w/v), edges[0..2] in enstatite.yaml and olivine-group.yaml and edges[1..2] in dunite.yaml use study-specific prose, and dunite.yaml pqqC/gdh protein_examples and edges[1..2] use supports: partial. |
| Vazquez-Rodriguez et al. (2015) metacinnabar.yaml SoxB and causal_graphs[0] concordance (#968) | passed | True | cmmmech:metacinnabar | Verified that metacinnabar.yaml UniProtKB:U5TVQ7 (soxB) protein_examples and causal_graphs[0].nodes[1] distinguish the primary 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions) from the synthetic black HgS comparator, and edges[0..3] use study-specific prose with supports: partial on edges[1]. |
| Dong et al. (2024) scandium.yaml Mex-LanM and causal_graphs[0] concordance (#969) | passed | True | cmmmech:scandium | Verified that scandium.yaml UniProtKB:C5B164 (lanM / Mex-LanM) protein_examples and causal_graphs[0] use supports: partial on binding/protein evidence and specify the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM sum in Table S9/S10) and stepwise 30 mM / 50 mM malonate elution at pH 5.0. |

## Scientific And Domain Assessments

### Gluconobacter oxydans enstatite.yaml, olivine-group.yaml, and dunite.yaml remediation (GRP-C11S5-001, #967)

graph: supported. Targets: cmmmech:dunite, cmmmech:enstatite, cmmmech:olivine-group.

All 3 Gluconobacter oxydans silicate bioleaching records now carry study-specific node and edge descriptions without template wrappers, and dunite.yaml qualifies pqqC/gdh protein_examples and edges[1..2] to supports: partial.

### Vazquez-Rodriguez et al. (2015) metacinnabar.yaml remediation (GRP-C11S5-002, #968)

graph: supported. Targets: cmmmech:metacinnabar.

metacinnabar.yaml now distinguishes the primary 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions) from the synthetic black HgS comparator in SoxB protein_examples and nodes[1], qualifies edges[1] to supports: partial, and replaces generic one-line explanations on edges[0..3].

### Dong et al. (2024) scandium.yaml Mex-LanM remediation (GRP-C11S5-003, #969)

graph: supported. Targets: cmmmech:scandium.

scandium.yaml now qualifies Mex-LanM protein_examples and edges[0] to supports: partial and describes the synthetic pH 3.0 16-REE chloride feed (Table S9/S10) and stepwise 30 mM / 50 mM malonate elution at pH 5.0 across protein_examples and causal_graphs[0].

## Findings

### cmmmech-cycle11-stage4-finding-0001: Gluconobacter oxydans silicate bioleaching records in enstatite.yaml, olivine-group.yaml, and dunite.yaml now have study-specific node/edge explanations and supports: partial on pqqC/gdh in dunite.yaml

minor / resolved / confirmed; issue key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support.

Across the three Gluconobacter oxydans whole-culture biolixiviant silicate bioleaching records — data/records/enstatite.yaml (cmmmech:enstatite, mineral, Klug et al. 2026 Scientific Reports 16:25317, DOI:10.1038/s41598-026-63817-0, klug_2026; causal_graphs[0] gluconobacter_enstatite_bioleaching_graph, lines 143-321), data/records/olivine-group.yaml (cmmmech:olivine-group, mineral_group, Klug et al. 2026, klug_2026; causal_graphs[0] gluconobacter_olivine_bioleaching_graph, lines 143-321), and data/records/dunite.yaml (cmmmech:dunite, primary_resource, Lee et al. 2025 Scientific Reports 15:15134, DOI:10.1038/s41598-025-99655-9, lee2025; causal_graphs[0] gluconobacter_dunite_bioleaching_graph, lines 159-337) — data/records/enstatite.yaml nodes[4].description (enstatite_mixed_feed, line 269) retains the generic parenthetical template string repeating the capitalized node label verbatim ('Starting solid substrate (Enstatite-bearing mixed silicate feed) exposed to the acidic biolixiviant.') instead of specifying the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate powder leached at 5% w/v (0.5 g per 10 mL liquid) without a pure-enstatite control (mechanisms[0].context, lines 31-32). Furthermore, edges[1].evidence[0].explanation (line 294 in enstatite.yaml and olivine-group.yaml; line 310 in dunite.yaml) and edges[2].evidence[0].explanation (line 303 in enstatite.yaml and olivine-group.yaml; line 319 in dunite.yaml) retain identical generic one-line template strings ('PQQ-dependent glucose dehydrogenase activity drives gluconic-acid biolixiviant production in Gluconobacter oxydans.' and 'Periplasmic glucose oxidation by G. oxydans generates the acidic gluconic-acid-rich biolixiviant.'), and edges[0].evidence[0].explanation in enstatite.yaml and olivine-group.yaml (line 285) omits that the engineered strain combined pstS deletion with the P112:mgdh promoter swap. Additionally, in data/records/dunite.yaml, mechanisms[0].protein_examples[2..3].evidence[0] (lines 105-107 and 130-132 for UniProtKB:Q9L3B2 pqqC and UniProtKB:P27175 gdh), causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0] (lines 242-244 and 274-276), and causal_graphs[0].edges[1..2].evidence[0] (lines 308-310 and 317-319) assert supports: support with generic template explanations, whereas Lee et al. (2025) compared wild-type G. oxydans NRRL B-58 (initial pH 2.39 +/- 0.02) and engineered B58 delta-pstS, P112:mgdh (initial pH 2.01 +/- 0.02) whole-culture biolixiviants without single-gene knockouts or purified-enzyme assays isolating pqqC or mgdh (supports: partial, matching enstatite.yaml and olivine-group.yaml). In this scope, 3 record(s) (enstatite, olivine-group, dunite) are affected.

Disposition: Resolved under GitHub Issue #967 (GRP-C11S5-001): replaced the generic parenthetical template description on enstatite.yaml causal_graphs[0].nodes[4].description, replaced generic one-line template explanations on edges[0..2] in enstatite.yaml and olivine-group.yaml and edges[1..2] in dunite.yaml with Klug et al. (2026) and Lee et al. (2025) prose, and qualified dunite.yaml pqqC/gdh protein_examples and edges[1..2] to supports: partial with 3 append-only EDIT history sidecars.

### cmmmech-cycle11-stage4-finding-0002: Vazquez-Rodriguez et al. (2015) metacinnabar.yaml now distinguishes natural museum metacinnabar feed from synthetic black HgS and qualifies edges[1] aqueous-Hg support to partial

minor / resolved / confirmed; issue key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support.

In data/records/metacinnabar.yaml (cmmmech:metacinnabar, mineral, Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596, vazquez_rodriguez2015), mechanisms[0].protein_examples[0].evidence[0].explanation (lines 118-120) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation (lines 192-194) for UniProtKB:U5TVQ7 (soxB, Thiobacillus thioparus) state that Vazquez-Rodriguez et al. (2015) studied 'axenic Thiobacillus thioparus ATCC 8158 pure-culture dissolution of synthetic metacinnabar (beta-HgS)', whereas mechanisms[0].context (lines 45-51) and mechanisms[0].evidence[0..4] (lines 58-97) establish that the primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural museum metacinnabar (&lt;250 um, containing pyritic inclusions, autoclaved under N2), with commercial synthetic black HgS tested only in the separate daily-thiosulfate-spike comparison (Figures 6-7). Furthermore, in causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph, lines 157-291), nodes[1].description (metacinnabar_substrate, line 198) omits the 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions) versus synthetic black HgS feed distinction; edges[1] (metacinnabar_substrate -&gt; dissolved_hg2_species, lines 265-273) asserts supports: support with description: 'Oxidation of beta-HgS releases soluble Hg(II) into the medium.' and explanation: 'Dissolved Hg(II) accumulates as an intermediate during beta-HgS bio-oxidation.', even though mechanisms[0].evidence[0..2] (lines 58-81) document that aqueous Hg remained relatively low in viable T. thioparus incubations (because mobilized Hg was reduced to volatile Hg(0)) while killed-cell and thiosulfate controls showed substantial chemical Hg release and inoculum elemental-sulfur carryover (supports: partial); and edges[0].evidence[0].explanation (line 264), edges[2].evidence[0].explanation (line 282), and edges[3].evidence[0].explanation (line 291) retain generic one-line strings omitting the Table 1 sulfate-proxy dissolution estimate (48-68% after carryover correction, Figure S3), the 285-bp merA PCR amplicon in Supplementary Data S1 (genetic potential only, without expression or mutagenesis), and gold-trap cold-vapor atomic fluorescence spectroscopy (CVAFS) volatile-Hg measurements. In this scope, 1 record(s) (metacinnabar) are affected.

Disposition: Resolved under GitHub Issue #968 (GRP-C11S5-002): updated UniProtKB:U5TVQ7 (soxB) protein_examples evidence explanation and causal_graphs[0].nodes[1].description in metacinnabar.yaml to distinguish the primary 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions, Figures 3-5, Table 1) from the separate commercial synthetic black HgS daily-thiosulfate-spike comparison (Figures 6-7), set edges[1] supports to partial, and replaced generic one-line explanations on edges[0..3] with an append-only EDIT history sidecar.

### cmmmech-cycle11-stage4-finding-0003: Dong et al. (2024) scandium.yaml Mex-LanM protein_examples and causal_graphs[0] now specify the synthetic pH 3.0 16-REE chloride feed and stepwise pH 5.0 malonate elution with supports: partial

minor / resolved / confirmed; issue key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording.

In data/records/scandium.yaml (cmmmech:scandium, element, Dong et al. 2024 Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919, dong2024), mechanisms[0].protein_examples[0].evidence[0] (lines 64-66) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0] (lines 109-111) for UniProtKB:C5B164 (lanM / Mex-LanM) assert supports: support with explanation: 'Immobilized Mex-LanM selectively binds Sc(III) over competing transition/base metals and elutes high-purity scandium upon mild acid stripping.', whereas mechanisms[0].description (line 39), mechanisms[0].context (line 40), and mechanisms[0].evidence[0..1] (lines 68-73) establish that Dong et al. (2024) Section 3.4 and Figures 3C and 5E-F tested a synthetic 16-REE chloride-salt mixture at pH 3.0 (nominal 0.4 mM total REE in Figure 5, summing to 0.2430 mM across 16 REEs with 23.8 +/- 1.1 uM Sc in supplement Table S10, labeled Table S9 in the caption) and eluted Sc(III) selectively using stepwise 30 mM and 50 mM malonate at pH 5.0 (not mild acid stripping of transition/base metals), without a matched Sc-only resin-without-LanM control (supports: partial). Furthermore, in causal_graphs[0] (immobilized_mex_lanm_scandium_separation_graph, lines 78-140), causal_graphs[0].description (line 80), nodes[1].label and nodes[1].description (mixed_scandium_feed, lines 113-115), nodes[2].description (purified_scandium_eluate, line 120), and edges[1] (lines 135-140) describe the Figure 5 column input as a 'mixed leachate feed' / 'multi-metal leachate' rather than a synthetic pH 3.0 chloride-salt REE solution resembling selected leachate compositions (mechanisms[0].context, line 40), and edges[0] (mex_lanm_protein -&gt; mixed_scandium_feed, lines 123-131) uses a generic 78-character explanation ('Immobilized LanM columns selectively retain Sc(III) from multi-metal mixtures.') with supports: support that omits the Table S9/S10 feed-concentration discrepancy (0.4 mM nominal vs 0.2430 mM sum) and the absence of a matched Sc-only resin-without-LanM control (mechanisms[0].evidence[1], supports: partial). In this scope, 1 record(s) (scandium) are affected.

Disposition: Resolved under GitHub Issue #969 (GRP-C11S5-003): updated UniProtKB:C5B164 (lanM / Mex-LanM) protein_examples evidence to supports: partial with synchronized prose specifying selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride mixture and stepwise 30 mM / 50 mM malonate elution at pH 5.0 (Figures 3C and 5E-F, Table S9/S10), and updated causal_graphs[0].description, nodes[1..2], and edges[0..1] (with supports: partial on edges[0]) with an append-only EDIT history sidecar.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:dunite, cmmmech:enstatite, cmmmech:metacinnabar, cmmmech:olivine-group, cmmmech:scandium. All 5 remediated records represent distinct material entities (2 IMA-approved minerals, 1 IMA mineral group, 1 ultramafic rock primary resource, and 1 chemical element) with disjoint identifiers and provenance; cohort boundaries from Cycle 11 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-stage4-evidence | reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml; findings[0..2] (cmmmech-cycle11-stage4-finding-0001..0003) | supports | Verified the 3 open Cycle 11 Stage 4 review findings and their 5 distinct target records. |
| ev-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/review_findings.yaml; findings[0..2] root-cause groups, issue_keys, and structured_reviews | supports | Confirmed exact Stage 4 finding IDs, issue_key identifiers, previous review_id occurrences, and target record lists. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge | supports | Canonical LinkML schema defining MaterialRecord and CausalGraph/CausalNode/CausalEdge structure. |
| ev-klug2026-lee2025 | https://doi.org/10.1038/s41598-026-63817-0; Klug et al. (2026) Scientific Reports 16:25317 (Methods, Figures 2-6, Table S1, Figures S1-S4) and Lee et al. (2025) Scientific Reports 15:15134 (DOI:10.1038/s41598-025-99655-9, Figures 2-7) | supports | Confirms whole-culture G. oxydans B58 delta-pstS, P112:mgdh biolixiviant assays on the 69 wt% olivine / 31 wt% enstatite mixed feed and 100% olivine San Carlos powder in Klug et al. (2026) and wild-type NRRL B-58 vs B58 delta-pstS, P112:mgdh Day Brook dunite bioleaching in Lee et al. (2025) without single-gene pqqC or mgdh knockouts. |
| ev-vazquez-rodriguez2015 | https://doi.org/10.3389/fmicb.2015.00596; Vazquez-Rodriguez et al. (2015) Frontiers in Microbiology 6:596, Methods, Figures 1-7, Table 1, Figure S3, Supplementary Data S1 | supports | Confirms primary T. thioparus ATCC 8158 incubations with 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions; Figures 3-5, Table 1), synthetic black HgS comparison in Figures 6-7, low aqueous Hg in viable cultures vs volatile Hg(0) recovery by gold-trap CVAFS, and the 285-bp merA PCR fragment in Data S1. |
| ev-dong2024 | https://doi.org/10.1016/j.seppur.2023.125919; Dong et al. (2024) Separation and Purification Technology 333:125919, Section 3.4, Figures 3C, 4, 5E-F, and supplement Table S10 (labeled Table S9 in caption) | supports | Confirms agarose-immobilized Mex-LanM-GSGC column capture of Sc(III) from a synthetic pH 3.0 16-REE chloride mixture (0.4 mM nominal / 0.2430 mM sum in Table S9/S10) and stepwise 30 mM and 50 mM malonate elution at pH 5.0 (&gt;99 mol% purity among REEs, &gt;99% two-step yield; ~94.5% Sc yield at 30 mM malonate in Figure 3C) without a matched Sc-only resin-without-LanM control. |

## Limits And Additional Notes

- This verification review is scoped to the 5 records remediated in Cycle 11 Stage 5; the remaining 693 records were verified with 0 open findings in the immutable Cycle 11 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T111500Z-cycle11-stage5-remediation-verification
title: 'Cycle 11 Stage 5 Post-Remediation Verification Review: 5 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-09T11:14:00Z'
finished_at: '2026-11-09T11:15:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation verification review across all 5 CMMMech records modified
  in Cycle 11 Stage 5 (2 mineral, 1 mineral_group, 1 primary_resource, and 1 element
  record) resolving all 3 open Cycle 11 Stage 4 review findings under GitHub Issues
  #967 (GRP-C11S5-001: enstatite.yaml, olivine-group.yaml, and dunite.yaml Gluconobacter
  oxydans whole-culture biolixiviant silicate bioleaching causal graphs and pqqC/gdh
  protein_examples updated with Klug et al. 2026 and Lee et al. 2025 study-specific
  prose and supports: partial), #968 (GRP-C11S5-002: metacinnabar.yaml Vazquez-Rodriguez
  et al. 2015 SoxB protein_examples and causal_graphs[0] updated to distinguish the
  primary 2 g/L ground natural museum metacinnabar feed from synthetic black HgS and
  qualify edges[1] aqueous-Hg support to partial), and #969 (GRP-C11S5-003: scandium.yaml
  Dong et al. 2024 Mex-LanM protein_examples and causal_graphs[0] updated to supports:
  partial on binding/protein evidence and aligned with the synthetic pH 3.0 16-REE
  chloride feed and stepwise 30 mM / 50 mM malonate elution at pH 5.0). All 5 records
  pass strict validation, history validation, and page rendering checks with 0 open
  findings.'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Cycle 11 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 5 remediated records against the immutable Cycle 11 Stage 4 review bundles.
source:
  git_revision: e5435802649ba486fc86d883ffed926e23fa8719
  state: working_tree
  inputs:
  - path: data/records/dunite.yaml
    sha256: e80e1f6aec45acb1ccbb15eb8ea9f75d436611cbc216e66210470b46d2c13183
    role: target
  - path: data/records/enstatite.yaml
    sha256: 0f5724853a1300c8449f747501091541694ad1f404cb1ece8b9d6d69bd57e941
    role: target
  - path: data/records/metacinnabar.yaml
    sha256: 9e0ce3d99b1bbeb9c0a4ac45212bfd5d4406ef79693c1688dbf50422b1d24a6a
    role: target
  - path: data/records/olivine-group.yaml
    sha256: 17c93e090645a2f5f35e87da50d9e4be35c9e15f76643babd418481ea799ef11
    role: target
  - path: data/records/scandium.yaml
    sha256: 76ae7bf5070596859d74737c8a4fcb3544b08278d8ff2b3ed1f9d8a9675b10bc
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml
    sha256: 99de4737c419ba8a1368933e1f7221be4aae1affccaef5d220e4867680c45750
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/review_findings.yaml
    sha256: dad2a81c17845edcfcbacfdb59eaa9575c8b0f11b9ba28d5b8af1eb6d82061a7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
scope:
  description: 'All 5 distinct CMMMech records affected by the 3 Cycle 11 Stage 4
    findings carried into Stage 5 (3 Gluconobacter oxydans silicate bioleaching records
    in GRP-C11S5-001 / #967, 1 Thiobacillus thioparus metacinnabar record in GRP-C11S5-002
    / #968, and 1 Mex-LanM scandium chromatography record in GRP-C11S5-003 / #969).'
  selection: cycle11_stage4_open_finding_targets
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:metacinnabar
  - cmmmech:olivine-group
  - cmmmech:scandium
targets:
- target_id: cmmmech:dunite
  path: data/records/dunite.yaml
  label: Dunite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 33842f51481611f5b90e8b897ad904ed18fcf14bcaca32f325fdec71bd11d0de
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dunite.yaml
    role: maintained_record
- target_id: cmmmech:enstatite
  path: data/records/enstatite.yaml
  label: Enstatite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: fea7cab52bfe54e5b6af0be314bfba83495d8a5fc8e7f24fbda1253cd8d5e7fd
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/enstatite.yaml
    role: maintained_record
- target_id: cmmmech:metacinnabar
  path: data/records/metacinnabar.yaml
  label: Metacinnabar
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: db0586961221d6944db76811ed6dc5e97c772e3633c68534c9221830f589a3f7
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
- target_id: cmmmech:olivine-group
  path: data/records/olivine-group.yaml
  label: Olivine group
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: ed648a6d1d60648ed0b513e60a830705d5e5638bbf9ebf80e2c65d553715fb5c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
- target_id: cmmmech:scandium
  path: data/records/scandium.yaml
  label: Scandium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 34f116f5e1f63089f0a979d6f14ef6b1c332da2dad36f46e8471cf8ebce55c3e
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
checks:
- check_id: chk-validate-records
  name: Strict LinkML and semantic record validation
  status: passed
  required: true
  summary: All 698 records (including all 5 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --require-records with 0 errors.
  target_ids:
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:metacinnabar
  - cmmmech:olivine-group
  - cmmmech:scandium
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
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:metacinnabar
  - cmmmech:olivine-group
  - cmmmech:scandium
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp1-gluconobacter-silicate-graphs
  name: Klug et al. (2026) and Lee et al. (2025) enstatite, olivine-group, and dunite
    concordance (#967)
  status: passed
  required: true
  summary: 'Verified that enstatite.yaml causal_graphs[0].nodes[4].description specifies
    the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed
    feed (5% w/v), edges[0..2] in enstatite.yaml and olivine-group.yaml and edges[1..2]
    in dunite.yaml use study-specific prose, and dunite.yaml pqqC/gdh protein_examples
    and edges[1..2] use supports: partial.'
  target_ids:
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:olivine-group
  evidence_ids:
  - ev-klug2026-lee2025
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp2-vazquez-rodriguez2015-metacinnabar
  name: Vazquez-Rodriguez et al. (2015) metacinnabar.yaml SoxB and causal_graphs[0]
    concordance (#968)
  status: passed
  required: true
  summary: 'Verified that metacinnabar.yaml UniProtKB:U5TVQ7 (soxB) protein_examples
    and causal_graphs[0].nodes[1] distinguish the primary 2 g/L ground natural museum
    metacinnabar (<250 um, with pyritic inclusions) from the synthetic black HgS comparator,
    and edges[0..3] use study-specific prose with supports: partial on edges[1].'
  target_ids:
  - cmmmech:metacinnabar
  evidence_ids:
  - ev-vazquez-rodriguez2015
  - ev-stage4-findings
  - ev-schema
- check_id: chk-grp3-dong2024-scandium-mex-lanm
  name: Dong et al. (2024) scandium.yaml Mex-LanM and causal_graphs[0] concordance
    (#969)
  status: passed
  required: true
  summary: 'Verified that scandium.yaml UniProtKB:C5B164 (lanM / Mex-LanM) protein_examples
    and causal_graphs[0] use supports: partial on binding/protein evidence and specify
    the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM sum in Table
    S9/S10) and stepwise 30 mM / 50 mM malonate elution at pH 5.0.'
  target_ids:
  - cmmmech:scandium
  evidence_ids:
  - ev-dong2024
  - ev-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-stage4-evidence
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml
  locator: findings[0..2] (cmmmech-cycle11-stage4-finding-0001..0003)
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Verified the 3 open Cycle 11 Stage 4 review findings and their 5 distinct
    target records.
  snapshot_sha256: 99de4737c419ba8a1368933e1f7221be4aae1affccaef5d220e4867680c45750
- evidence_id: ev-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2] root-cause groups, issue_keys, and structured_reviews
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Confirmed exact Stage 4 finding IDs, issue_key identifiers, previous review_id
    occurrences, and target record lists.
  snapshot_sha256: dad2a81c17845edcfcbacfdb59eaa9575c8b0f11b9ba28d5b8af1eb6d82061a7
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord and CausalGraph/CausalNode/CausalEdge
    structure.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
- evidence_id: ev-klug2026-lee2025
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-026-63817-0
  locator: Klug et al. (2026) Scientific Reports 16:25317 (Methods, Figures 2-6, Table
    S1, Figures S1-S4) and Lee et al. (2025) Scientific Reports 15:15134 (DOI:10.1038/s41598-025-99655-9,
    Figures 2-7)
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Confirms whole-culture G. oxydans B58 delta-pstS, P112:mgdh biolixiviant
    assays on the 69 wt% olivine / 31 wt% enstatite mixed feed and 100% olivine San
    Carlos powder in Klug et al. (2026) and wild-type NRRL B-58 vs B58 delta-pstS,
    P112:mgdh Day Brook dunite bioleaching in Lee et al. (2025) without single-gene
    pqqC or mgdh knockouts.
- evidence_id: ev-vazquez-rodriguez2015
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2015.00596
  locator: Vazquez-Rodriguez et al. (2015) Frontiers in Microbiology 6:596, Methods,
    Figures 1-7, Table 1, Figure S3, Supplementary Data S1
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Confirms primary T. thioparus ATCC 8158 incubations with 2 g/L ground natural
    museum metacinnabar (<250 um, with pyritic inclusions; Figures 3-5, Table 1),
    synthetic black HgS comparison in Figures 6-7, low aqueous Hg in viable cultures
    vs volatile Hg(0) recovery by gold-trap CVAFS, and the 285-bp merA PCR fragment
    in Data S1.
- evidence_id: ev-dong2024
  kind: primary_source
  reference: https://doi.org/10.1016/j.seppur.2023.125919
  locator: Dong et al. (2024) Separation and Purification Technology 333:125919, Section
    3.4, Figures 3C, 4, 5E-F, and supplement Table S10 (labeled Table S9 in caption)
  accessed_at: '2026-11-09T11:14:30Z'
  support: supports
  summary: Confirms agarose-immobilized Mex-LanM-GSGC column capture of Sc(III) from
    a synthetic pH 3.0 16-REE chloride mixture (0.4 mM nominal / 0.2430 mM sum in
    Table S9/S10) and stepwise 30 mM and 50 mM malonate elution at pH 5.0 (>99 mol%
    purity among REEs, >99% two-step yield; ~94.5% Sc yield at 30 mM malonate in Figure
    3C) without a matched Sc-only resin-without-LanM control.
assessments:
- assessment_id: assess-grp1-gluconobacter-silicate
  area: graph
  topic: 'Gluconobacter oxydans enstatite.yaml, olivine-group.yaml, and dunite.yaml
    remediation (GRP-C11S5-001, #967)'
  outcome: supported
  summary: 'All 3 Gluconobacter oxydans silicate bioleaching records now carry study-specific
    node and edge descriptions without template wrappers, and dunite.yaml qualifies
    pqqC/gdh protein_examples and edges[1..2] to supports: partial.'
  target_ids:
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:olivine-group
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-klug2026-lee2025
  - ev-schema
  metrics:
  - name: grp1_gluconobacter_silicate_graph_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C11S5-001 records with study-specific node/edge explanations
      and supports: partial on whole-culture pqqC/gdh evidence'
    denominator: 3
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-vazquez-rodriguez2015-metacinnabar
  area: graph
  topic: 'Vazquez-Rodriguez et al. (2015) metacinnabar.yaml remediation (GRP-C11S5-002,
    #968)'
  outcome: supported
  summary: 'metacinnabar.yaml now distinguishes the primary 2 g/L ground natural museum
    metacinnabar (<250 um, with pyritic inclusions) from the synthetic black HgS comparator
    in SoxB protein_examples and nodes[1], qualifies edges[1] to supports: partial,
    and replaces generic one-line explanations on edges[0..3].'
  target_ids:
  - cmmmech:metacinnabar
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-vazquez-rodriguez2015
  - ev-schema
  metrics:
  - name: grp2_vazquez_rodriguez2015_metacinnabar_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C11S5-002 records with aligned natural vs synthetic
      feed descriptions and supports: partial on edges[1]'
    denominator: 1
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-dong2024-scandium
  area: graph
  topic: 'Dong et al. (2024) scandium.yaml Mex-LanM remediation (GRP-C11S5-003, #969)'
  outcome: supported
  summary: 'scandium.yaml now qualifies Mex-LanM protein_examples and edges[0] to
    supports: partial and describes the synthetic pH 3.0 16-REE chloride feed (Table
    S9/S10) and stepwise 30 mM / 50 mM malonate elution at pH 5.0 across protein_examples
    and causal_graphs[0].'
  target_ids:
  - cmmmech:scandium
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-dong2024
  - ev-schema
  metrics:
  - name: grp3_dong2024_scandium_concordance
    value: 1.0
    unit: fraction
    definition: 'Fraction of GRP-C11S5-003 records with synthetic pH 3.0 16-REE chloride
      feed, stepwise pH 5.0 malonate elution, and supports: partial on protein_examples/edges[0]'
    denominator: 1
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle11-stage4-finding-0001
  issue_key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Gluconobacter oxydans silicate bioleaching records in enstatite.yaml, olivine-group.yaml,
    and dunite.yaml now have study-specific node/edge explanations and supports: partial
    on pqqC/gdh in dunite.yaml'
  description: 'Across the three Gluconobacter oxydans whole-culture biolixiviant
    silicate bioleaching records — data/records/enstatite.yaml (cmmmech:enstatite,
    mineral, Klug et al. 2026 Scientific Reports 16:25317, DOI:10.1038/s41598-026-63817-0,
    klug_2026; causal_graphs[0] gluconobacter_enstatite_bioleaching_graph, lines 143-321),
    data/records/olivine-group.yaml (cmmmech:olivine-group, mineral_group, Klug et
    al. 2026, klug_2026; causal_graphs[0] gluconobacter_olivine_bioleaching_graph,
    lines 143-321), and data/records/dunite.yaml (cmmmech:dunite, primary_resource,
    Lee et al. 2025 Scientific Reports 15:15134, DOI:10.1038/s41598-025-99655-9, lee2025;
    causal_graphs[0] gluconobacter_dunite_bioleaching_graph, lines 159-337) — data/records/enstatite.yaml
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
    In this scope, 3 record(s) (enstatite, olivine-group, dunite) are affected.'
  target_ids:
  - cmmmech:enstatite
  - cmmmech:olivine-group
  - cmmmech:dunite
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
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-klug2026-lee2025
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/enstatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/dunite.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #967 (GRP-C11S5-001): replaced
    the generic parenthetical template description on enstatite.yaml causal_graphs[0].nodes[4].description,
    replaced generic one-line template explanations on edges[0..2] in enstatite.yaml
    and olivine-group.yaml and edges[1..2] in dunite.yaml with Klug et al. (2026)
    and Lee et al. (2025) prose, and qualified dunite.yaml pqqC/gdh protein_examples
    and edges[1..2] to supports: partial with 3 append-only EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041501Z-cycle11-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041502Z-cycle11-stage4-mineral-group-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041504Z-cycle11-stage4-primary-resource-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041507Z-enstatite-cycle11-stage4-record-review
    finding_id: cmmmech-cycle11-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/967
- finding_id: cmmmech-cycle11-stage4-finding-0002
  issue_key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: Vazquez-Rodriguez et al. (2015) metacinnabar.yaml now distinguishes natural
    museum metacinnabar feed from synthetic black HgS and qualifies edges[1] aqueous-Hg
    support to partial
  description: 'In data/records/metacinnabar.yaml (cmmmech:metacinnabar, mineral,
    Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596,
    vazquez_rodriguez2015), mechanisms[0].protein_examples[0].evidence[0].explanation
    (lines 118-120) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
    (lines 192-194) for UniProtKB:U5TVQ7 (soxB, Thiobacillus thioparus) state that
    Vazquez-Rodriguez et al. (2015) studied ''axenic Thiobacillus thioparus ATCC 8158
    pure-culture dissolution of synthetic metacinnabar (beta-HgS)'', whereas mechanisms[0].context
    (lines 45-51) and mechanisms[0].evidence[0..4] (lines 58-97) establish that the
    primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural
    museum metacinnabar (<250 um, containing pyritic inclusions, autoclaved under
    N2), with commercial synthetic black HgS tested only in the separate daily-thiosulfate-spike
    comparison (Figures 6-7). Furthermore, in causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph,
    lines 157-291), nodes[1].description (metacinnabar_substrate, line 198) omits
    the 2 g/L ground natural museum metacinnabar (<250 um, with pyritic inclusions)
    versus synthetic black HgS feed distinction; edges[1] (metacinnabar_substrate
    -> dissolved_hg2_species, lines 265-273) asserts supports: support with description:
    ''Oxidation of beta-HgS releases soluble Hg(II) into the medium.'' and explanation:
    ''Dissolved Hg(II) accumulates as an intermediate during beta-HgS bio-oxidation.'',
    even though mechanisms[0].evidence[0..2] (lines 58-81) document that aqueous Hg
    remained relatively low in viable T. thioparus incubations (because mobilized
    Hg was reduced to volatile Hg(0)) while killed-cell and thiosulfate controls showed
    substantial chemical Hg release and inoculum elemental-sulfur carryover (supports:
    partial); and edges[0].evidence[0].explanation (line 264), edges[2].evidence[0].explanation
    (line 282), and edges[3].evidence[0].explanation (line 291) retain generic one-line
    strings omitting the Table 1 sulfate-proxy dissolution estimate (48-68% after
    carryover correction, Figure S3), the 285-bp merA PCR amplicon in Supplementary
    Data S1 (genetic potential only, without expression or mutagenesis), and gold-trap
    cold-vapor atomic fluorescence spectroscopy (CVAFS) volatile-Hg measurements.
    In this scope, 1 record(s) (metacinnabar) are affected.'
  target_ids:
  - cmmmech:metacinnabar
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-vazquez-rodriguez2015
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #968 (GRP-C11S5-002): updated UniProtKB:U5TVQ7
    (soxB) protein_examples evidence explanation and causal_graphs[0].nodes[1].description
    in metacinnabar.yaml to distinguish the primary 2 g/L ground natural museum metacinnabar
    (<250 um, with pyritic inclusions, Figures 3-5, Table 1) from the separate commercial
    synthetic black HgS daily-thiosulfate-spike comparison (Figures 6-7), set edges[1]
    supports to partial, and replaced generic one-line explanations on edges[0..3]
    with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041501Z-cycle11-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041508Z-metacinnabar-cycle11-stage4-record-review
    finding_id: cmmmech-cycle11-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/968
- finding_id: cmmmech-cycle11-stage4-finding-0003
  issue_key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'Dong et al. (2024) scandium.yaml Mex-LanM protein_examples and causal_graphs[0]
    now specify the synthetic pH 3.0 16-REE chloride feed and stepwise pH 5.0 malonate
    elution with supports: partial'
  description: 'In data/records/scandium.yaml (cmmmech:scandium, element, Dong et
    al. 2024 Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919,
    dong2024), mechanisms[0].protein_examples[0].evidence[0] (lines 64-66) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0]
    (lines 109-111) for UniProtKB:C5B164 (lanM / Mex-LanM) assert supports: support
    with explanation: ''Immobilized Mex-LanM selectively binds Sc(III) over competing
    transition/base metals and elutes high-purity scandium upon mild acid stripping.'',
    whereas mechanisms[0].description (line 39), mechanisms[0].context (line 40),
    and mechanisms[0].evidence[0..1] (lines 68-73) establish that Dong et al. (2024)
    Section 3.4 and Figures 3C and 5E-F tested a synthetic 16-REE chloride-salt mixture
    at pH 3.0 (nominal 0.4 mM total REE in Figure 5, summing to 0.2430 mM across 16
    REEs with 23.8 +/- 1.1 uM Sc in supplement Table S10, labeled Table S9 in the
    caption) and eluted Sc(III) selectively using stepwise 30 mM and 50 mM malonate
    at pH 5.0 (not mild acid stripping of transition/base metals), without a matched
    Sc-only resin-without-LanM control (supports: partial). Furthermore, in causal_graphs[0]
    (immobilized_mex_lanm_scandium_separation_graph, lines 78-140), causal_graphs[0].description
    (line 80), nodes[1].label and nodes[1].description (mixed_scandium_feed, lines
    113-115), nodes[2].description (purified_scandium_eluate, line 120), and edges[1]
    (lines 135-140) describe the Figure 5 column input as a ''mixed leachate feed''
    / ''multi-metal leachate'' rather than a synthetic pH 3.0 chloride-salt REE solution
    resembling selected leachate compositions (mechanisms[0].context, line 40), and
    edges[0] (mex_lanm_protein -> mixed_scandium_feed, lines 123-131) uses a generic
    78-character explanation (''Immobilized LanM columns selectively retain Sc(III)
    from multi-metal mixtures.'') with supports: support that omits the Table S9/S10
    feed-concentration discrepancy (0.4 mM nominal vs 0.2430 mM sum) and the absence
    of a matched Sc-only resin-without-LanM control (mechanisms[0].evidence[1], supports:
    partial). In this scope, 1 record(s) (scandium) are affected.'
  target_ids:
  - cmmmech:scandium
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].relationship
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-dong2024
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub Issue #969 (GRP-C11S5-003): updated UniProtKB:C5B164
    (lanM / Mex-LanM) protein_examples evidence to supports: partial with synchronized
    prose specifying selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride
    mixture and stepwise 30 mM / 50 mM malonate elution at pH 5.0 (Figures 3C and
    5E-F, Table S9/S10), and updated causal_graphs[0].description, nodes[1..2], and
    edges[0..1] (with supports: partial on edges[0]) with an append-only EDIT history
    sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041500Z-cycle11-stage4-element-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle11-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261109T041509Z-scandium-cycle11-stage4-record-review
    finding_id: cmmmech-cycle11-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/969
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:metacinnabar
  - cmmmech:olivine-group
  - cmmmech:scandium
  evidence_ids:
  - ev-stage4-evidence
  - ev-stage4-findings
  - ev-schema
  rationale: All 5 remediated records represent distinct material entities (2 IMA-approved
    minerals, 1 IMA mineral group, 1 ultramafic rock primary resource, and 1 chemical
    element) with disjoint identifiers and provenance; cohort boundaries from Cycle
    11 Stage 4 are retained unchanged.
limitations:
- This verification review is scoped to the 5 records remediated in Cycle 11 Stage
  5; the remaining 693 records were verified with 0 open findings in the immutable
  Cycle 11 Stage 4 review bundles.
```
