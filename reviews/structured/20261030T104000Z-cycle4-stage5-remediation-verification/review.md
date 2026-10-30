# Cycle 4 Stage 5 Post-Remediation Verification Review: 25 Remediated CMMMech Records

- Review: 20261030T104000Z-cycle4-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T10:36:00Z
- Finished UTC: 2026-10-30T10:40:00Z
- Reviewer: antigravity / cmmmech-cycle4-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation scientific and structural verification of all 25 CMMMech records remediated in Cycle 4 Stage 5 (run mech-goal-sequence-20261019, cycle 4, stage 5) across GitHub issues #862 (GRP-C4S5-001: cmmmech-cycle4-stage4-finding-0001, traction-battery-hydrometallurgical-residue.yaml causal_graphs[0] node solid_feed_substrate label corrected from spurious Borra et al. 2016 bauxite-residue sample codes '(BR1, BR2, BR4)' to '(nickel-line and cobalt-line residues)' per Lu et al. 2025, and nodes[0..1].label plus edges[0].evidence[0].explanation aligned with the five-member acidophile consortium), #863 (GRP-C4S5-002: cmmmech-cycle4-stage4-finding-0002, 8 records normalized to serialize top-level sources and criticality before mechanisms and causal_graphs per CANONICAL_RECORD_KEYS), and #864 (GRP-C4S5-003: cmmmech-cycle4-stage4-finding-0003, 16 records normalized to serialize top-level curation_history before history_refs per CANONICAL_RECORD_KEYS). All 3 carried-forward Cycle 4 Stage 4 findings are verified as resolved with 25 append-only EDIT history sidecars.

## Scope And Provenance

All 25 CMMMech records affected by the 3 Cycle 4 Stage 4 findings carried into Stage 5 (1 record in GRP-C4S5-001 / #862, 8 records in GRP-C4S5-002 / #863, and 16 records in GRP-C4S5-003 / #864).

Selection: cycle4_stage4_open_finding_targets
Coverage: full; 25 reviewed / 25 in the declared population.
Source: working_tree at Git base cfbf9053da1f950d6c2f6c7bac55f8bb38a5116f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:aluminium-salt-slag | data/records/aluminium-salt-slag.yaml | maintained | Aluminium salt slag |
| cmmmech:beryllium | data/records/beryllium.yaml | maintained | Beryllium |
| cmmmech:beverage-carton-hydropulping-reject | data/records/beverage-carton-hydropulping-reject.yaml | maintained | Beverage-carton hydropulping reject |
| cmmmech:biogas-desulfurization-sulfur-residue | data/records/biogas-desulfurization-sulfur-residue.yaml | maintained | Biogas-desulfurization sulfur residue |
| cmmmech:cadmium-telluride-photovoltaic-module-scrap | data/records/cadmium-telluride-photovoltaic-module-scrap.yaml | maintained | Cadmium telluride photovoltaic module scrap |
| cmmmech:cathode-ray-tube-glass | data/records/cathode-ray-tube-glass.yaml | maintained | Waste lead-bearing cathode-ray-tube glass |
| cmmmech:cesium | data/records/cesium.yaml | maintained | Cesium |
| cmmmech:churchite-y | data/records/churchite-y.yaml | maintained | Churchite-(Y) |
| cmmmech:electroformed-copper-silver-manufacturing-scrap | data/records/electroformed-copper-silver-manufacturing-scrap.yaml | maintained | Electroformed copper-silver manufacturing scrap |
| cmmmech:end-of-life-cigs-photovoltaic-modules | data/records/end-of-life-cigs-photovoltaic-modules.yaml | maintained | End-of-life CIGS photovoltaic modules |
| cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules | data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml | maintained | End-of-life crystalline-silicon photovoltaic modules |
| cmmmech:ground-waste-tire-rubber | data/records/ground-waste-tire-rubber.yaml | maintained | Ground waste tire rubber |
| cmmmech:ion-adsorption-rare-earth-clay | data/records/ion-adsorption-rare-earth-clay.yaml | maintained | Ion-adsorption rare-earth clay |
| cmmmech:iron-ore-tailings | data/records/iron-ore-tailings.yaml | maintained | Iron-ore tailings |
| cmmmech:pharmaceutical-blister-packaging-waste | data/records/pharmaceutical-blister-packaging-waste.yaml | maintained | Pharmaceutical blister packaging waste |
| cmmmech:polymetallic-nodules | data/records/polymetallic-nodules.yaml | maintained | Polymetallic nodules |
| cmmmech:rhenium | data/records/rhenium.yaml | maintained | Rhenium |
| cmmmech:rubidium | data/records/rubidium.yaml | maintained | Rubidium |
| cmmmech:spent-lead-acid-battery-electrolyte | data/records/spent-lead-acid-battery-electrolyte.yaml | maintained | Spent lead-acid battery electrolyte |
| cmmmech:spent-vanadium-flow-battery-electrolyte | data/records/spent-vanadium-flow-battery-electrolyte.yaml | maintained | Spent vanadium-flow-battery electrolyte |
| cmmmech:strontium | data/records/strontium.yaml | maintained | Strontium |
| cmmmech:traction-battery-hydrometallurgical-residue | data/records/traction-battery-hydrometallurgical-residue.yaml | maintained | Traction-battery hydrometallurgical residue |
| cmmmech:waste-printed-circuit-boards | data/records/waste-printed-circuit-boards.yaml | maintained | Waste printed circuit boards |
| cmmmech:zinc-leach-residue | data/records/zinc-leach-residue.yaml | maintained | Zinc leach residue |
| cmmmech:zinc-purification-hot-filter-cake | data/records/zinc-purification-hot-filter-cake.yaml | maintained | Zinc purification hot filter cake |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema and semantic record validation | passed | True | cmmmech:aluminium-salt-slag, cmmmech:beryllium, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cesium, cmmmech:churchite-y, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ground-waste-tire-rubber, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:iron-ore-tailings, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:polymetallic-nodules, cmmmech:rhenium, cmmmech:rubidium, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:strontium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:waste-printed-circuit-boards, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake | All 663 records (including all 25 remediated records) pass .venv/bin/python -m cmmmech.cli validate --strict with 0 errors and 0 warnings. |
| Append-only history sidecar validation | passed | True | cmmmech:aluminium-salt-slag, cmmmech:beryllium, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cesium, cmmmech:churchite-y, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ground-waste-tire-rubber, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:iron-ore-tailings, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:polymetallic-nodules, cmmmech:rhenium, cmmmech:rubidium, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:strontium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:waste-printed-circuit-boards, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake | All 25 new EDIT history sidecars and existing history sidecars (1,098 total) pass .venv/bin/python -m cmmmech.cli validate-history --base main. |
| Lu et al. (2025) substrate and five-member consortium causal-graph alignment in traction-battery-hydrometallurgical-residue.yaml (#862) | passed | True | cmmmech:traction-battery-hydrometallurgical-residue | In data/records/traction-battery-hydrometallurgical-residue.yaml, causal_graphs[0] (ferrooxidans_battery_residue_bioleaching_graph) now labels node solid_feed_substrate as 'Industrial traction-battery hydrometallurgical residues (nickel-line and cobalt-line residues)', nodes[0] as 'Sqr / Sqor sulfide-quinone reductase (consortium sqr / sqor)', nodes[1] as 'Tth / TetH tetrathionate hydrolase (consortium tth)', and edges[0].evidence[0].explanation as 'Reduced sulfur oxidation in the five-member acidophile consortium couples Sqr/Sqor and tetrathionate hydrolysis to sulfuric acid proton generation.' |
| Canonical top-level key ordering (sources/criticality before mechanisms/causal_graphs) across 8 records (#863) | passed | True | cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:churchite-y, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:iron-ore-tailings, cmmmech:polymetallic-nodules, cmmmech:waste-printed-circuit-boards | All 8 records in GRP-C4S5-002 (cadmium-telluride-photovoltaic-module-scrap, cathode-ray-tube-glass, churchite-y, end-of-life-cigs-photovoltaic-modules, end-of-life-crystalline-silicon-photovoltaic-modules, iron-ore-tailings, polymetallic-nodules, waste-printed-circuit-boards) now serialize top-level sources and criticality before mechanisms and causal_graphs in exact CANONICAL_RECORD_KEYS order. |
| Canonical top-level key ordering (curation_history before history_refs) across 16 records (#864) | passed | True | cmmmech:aluminium-salt-slag, cmmmech:beryllium, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:cesium, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:ground-waste-tire-rubber, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:rhenium, cmmmech:rubidium, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:strontium, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake | All 16 records in GRP-C4S5-003 (aluminium-salt-slag, beryllium, beverage-carton-hydropulping-reject, biogas-desulfurization-sulfur-residue, cesium, electroformed-copper-silver-manufacturing-scrap, ground-waste-tire-rubber, ion-adsorption-rare-earth-clay, pharmaceutical-blister-packaging-waste, rhenium, rubidium, spent-lead-acid-battery-electrolyte, spent-vanadium-flow-battery-electrolyte, strontium, zinc-leach-residue, zinc-purification-hot-filter-cake) now serialize top-level curation_history before history_refs in exact CANONICAL_RECORD_KEYS order. |

## Scientific And Domain Assessments

### Lu et al. (2025) substrate and consortium label fidelity in traction-battery-hydrometallurgical-residue.yaml (#862)

graph: supported. Targets: cmmmech:traction-battery-hydrometallurgical-residue.

causal_graphs[0] in data/records/traction-battery-hydrometallurgical-residue.yaml now accurately names the nickel-line and cobalt-line traction-battery hydrometallurgical residues from Lu et al. (2025) without spurious bauxite-residue sample codes (BR1, BR2, BR4) and reflects the five-member acidophile consortium across nodes[0..1].label and edges[0].evidence[0].explanation.

### Canonical top-level key ordering (sources/criticality before mechanisms/causal_graphs) across 8 records (#863)

consistency: supported. Targets: cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:churchite-y, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:iron-ore-tailings, cmmmech:polymetallic-nodules, cmmmech:waste-printed-circuit-boards.

All 8 records in GRP-C4S5-002 now serialize top-level keys in exact CANONICAL_RECORD_KEYS order with sources and criticality preceding mechanisms and causal_graphs, achieving 100% corpus-wide uniformity across all 663 records.

### Canonical top-level key ordering (curation_history before history_refs) across 16 records (#864)

consistency: supported. Targets: cmmmech:aluminium-salt-slag, cmmmech:beryllium, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:cesium, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:ground-waste-tire-rubber, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:rhenium, cmmmech:rubidium, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:strontium, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake.

All 16 records in GRP-C4S5-003 now serialize top-level keys in exact CANONICAL_RECORD_KEYS order with curation_history preceding history_refs, achieving 100% corpus-wide uniformity across all 663 records.

## Findings

### cmmmech-cycle4-stage4-finding-0001: traction-battery-hydrometallurgical-residue.yaml causal_graphs[0] node and edge labels now match Lu et al. (2025) substrate and consortium scope

minor / resolved / confirmed; issue key: cmmmech.traction-battery-hydrometallurgical-residue.causal-node-spurious-br-sample-codes-and-consortium-label.

Updated causal_graphs[0] (ferrooxidans_battery_residue_bioleaching_graph) in data/records/traction-battery-hydrometallurgical-residue.yaml so nodes[3].label (solid_feed_substrate) reads 'Industrial traction-battery hydrometallurgical residues (nickel-line and cobalt-line residues)', nodes[0].label reads 'Sqr / Sqor sulfide-quinone reductase (consortium sqr / sqor)', nodes[1].label reads 'Tth / TetH tetrathionate hydrolase (consortium tth)', and edges[0].evidence[0].explanation reads 'Reduced sulfur oxidation in the five-member acidophile consortium couples Sqr/Sqor and tetrathionate hydrolysis to sulfuric acid proton generation.' with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #862 (group GRP-C4S5-001) by replacing spurious '(BR1, BR2, BR4)' sample codes on solid_feed_substrate and aligning Sqr/Sqor and Tth/TetH labels and edge[0] evidence explanation with the five-member acidophile consortium in data/records/traction-battery-hydrometallurgical-residue.yaml with an append-only EDIT history sidecar.

### cmmmech-cycle4-stage4-finding-0002: 8 records now serialize top-level sources and criticality before mechanisms and causal_graphs per CANONICAL_RECORD_KEYS

minor / resolved / confirmed; issue key: cmmmech.records.mechanisms-before-sources-key-order.

Normalized top-level YAML key ordering across all 8 affected records (cadmium-telluride-photovoltaic-module-scrap, cathode-ray-tube-glass, churchite-y, end-of-life-cigs-photovoltaic-modules, end-of-life-crystalline-silicon-photovoltaic-modules, iron-ore-tailings, polymetallic-nodules, waste-printed-circuit-boards) to CANONICAL_RECORD_KEYS with 8 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #863 (group GRP-C4S5-002) by normalizing top-level YAML key order to CANONICAL_RECORD_KEYS across all 8 records with append-only EDIT history sidecars.

### cmmmech-cycle4-stage4-finding-0003: 16 records now serialize top-level curation_history before history_refs per CANONICAL_RECORD_KEYS

minor / resolved / confirmed; issue key: cmmmech.records.history-refs-before-curation-history-key-order.

Normalized top-level YAML key ordering across all 16 affected records (aluminium-salt-slag, beryllium, beverage-carton-hydropulping-reject, biogas-desulfurization-sulfur-residue, cesium, electroformed-copper-silver-manufacturing-scrap, ground-waste-tire-rubber, ion-adsorption-rare-earth-clay, pharmaceutical-blister-packaging-waste, rhenium, rubidium, spent-lead-acid-battery-electrolyte, spent-vanadium-flow-battery-electrolyte, strontium, zinc-leach-residue, zinc-purification-hot-filter-cake) to CANONICAL_RECORD_KEYS with 16 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #864 (group GRP-C4S5-003) by normalizing top-level YAML key order to CANONICAL_RECORD_KEYS across all 16 records with append-only EDIT history sidecars.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:aluminium-salt-slag, cmmmech:beryllium, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cesium, cmmmech:churchite-y, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ground-waste-tire-rubber, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:iron-ore-tailings, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:polymetallic-nodules, cmmmech:rhenium, cmmmech:rubidium, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:strontium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:waste-printed-circuit-boards, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake. All 25 remediated records represent distinct material entities (5 elements, 1 mineral, 2 primary resources, and 17 secondary resources) with disjoint identifiers and provenance; cohort boundaries from Cycle 4 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-lu2025-doi | https://doi.org/10.3390/recycling10030113; Lu et al. (2025) Recycling 10(3):113, Section 2.1-2.2 &amp; Results (nickel-line and cobalt-line residues; five-member acidophile consortium) | supports | Lu et al. (2025) characterize separate nickel-line and cobalt-line hydrometallurgical residues from traction-battery recycling bioleached by a five-member acidophile consortium (Acidithiobacillus ferrooxidans, Acidithiobacillus caldus, Leptospirillum ferriphilum, Sulfobacillus thermosulfidooxidans, Ferroplasma thermophilum). |
| ev-cycle4-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/review_findings.yaml; findings[0..2] | supports | Frozen Cycle 4 Stage 4 review findings ledger defining cmmmech-cycle4-stage4-finding-0001, cmmmech-cycle4-stage4-finding-0002, and cmmmech-cycle4-stage4-finding-0003 across the 25 target records. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge | supports | Canonical LinkML schema defining MaterialRecord top-level slot order and CausalGraph structure. |
| ev-new-history-script | scripts/curate_causal_graphs.py; CANONICAL_RECORD_KEYS | supports | Canonical top-level YAML key ordering tuple CANONICAL_RECORD_KEYS placing sources and criticality before mechanisms and causal_graphs, and curation_history before history_refs. |

## Limits And Additional Notes

- This verification review is scoped to the 25 records remediated in Cycle 4 Stage 5; the remaining 638 records were verified with 0 open findings in the immutable Cycle 4 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T104000Z-cycle4-stage5-remediation-verification
title: 'Cycle 4 Stage 5 Post-Remediation Verification Review: 25 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-30T10:36:00Z'
finished_at: '2026-10-30T10:40:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation scientific and structural verification of all 25 CMMMech
  records remediated in Cycle 4 Stage 5 (run mech-goal-sequence-20261019, cycle 4,
  stage 5) across GitHub issues #862 (GRP-C4S5-001: cmmmech-cycle4-stage4-finding-0001,
  traction-battery-hydrometallurgical-residue.yaml causal_graphs[0] node solid_feed_substrate
  label corrected from spurious Borra et al. 2016 bauxite-residue sample codes ''(BR1,
  BR2, BR4)'' to ''(nickel-line and cobalt-line residues)'' per Lu et al. 2025, and
  nodes[0..1].label plus edges[0].evidence[0].explanation aligned with the five-member
  acidophile consortium), #863 (GRP-C4S5-002: cmmmech-cycle4-stage4-finding-0002,
  8 records normalized to serialize top-level sources and criticality before mechanisms
  and causal_graphs per CANONICAL_RECORD_KEYS), and #864 (GRP-C4S5-003: cmmmech-cycle4-stage4-finding-0003,
  16 records normalized to serialize top-level curation_history before history_refs
  per CANONICAL_RECORD_KEYS). All 3 carried-forward Cycle 4 Stage 4 findings are verified
  as resolved with 25 append-only EDIT history sidecars.'
reviewer:
  identity: antigravity / cmmmech-cycle4-stage5-remediation-reviewer
  kind: agent
  independence: self_review
  independence_basis: Cycle 4 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 25 remediated records against the immutable Cycle 4 Stage 4 review bundles.
  model: claude-opus-4-6
source:
  git_revision: cfbf9053da1f950d6c2f6c7bac55f8bb38a5116f
  state: working_tree
  inputs:
  - path: data/records/aluminium-salt-slag.yaml
    sha256: 0c5300af9596a26357f8e043367182dab0b9bb1df26e8eaba81a76fc5f431c09
    role: target
  - path: data/records/beryllium.yaml
    sha256: 3c4490f5b7832808b5683a26d4b93e849647a52ef7d1468cd99c06a79a53aa71
    role: target
  - path: data/records/beverage-carton-hydropulping-reject.yaml
    sha256: ac7b0855a33f0d1193d92c846595c38a1dfb8d4b1d3e1b229d3e091c1c7c4a7c
    role: target
  - path: data/records/biogas-desulfurization-sulfur-residue.yaml
    sha256: 6cd930791244eec71896f7919e40daea23e1e0ba5a1b0993bed6a0a2b5b49b70
    role: target
  - path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
    sha256: 0831e5c256868ee34c60c03c900ee65b3de8291f6336430e0f8eb3967956ad65
    role: target
  - path: data/records/cathode-ray-tube-glass.yaml
    sha256: 9aeab2c8c5914e8f224fae483f3cbdcbebb599e131ca4a57f2c23b1236aecfad
    role: target
  - path: data/records/cesium.yaml
    sha256: 09a7cf90913a87a0fe2ad0c2998e1ed1239c41c4a5b488be2a9db95733f8bf50
    role: target
  - path: data/records/churchite-y.yaml
    sha256: 7440237c99bf73b14d8d44667c2936afb034ea5bca6a00572f49ff669e1bdfa0
    role: target
  - path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
    sha256: d6ca2fdab6864ea98e0cb0e5a687426da356559e9cd77b90af7089752ab5aa38
    role: target
  - path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
    sha256: c795734bd44968f4bd3344b85f08d73579c83cfaca5e52a441a7f6884ac2913a
    role: target
  - path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
    sha256: 3ba90fe05d6a643cba04da24caed02a479588236256ef8b0589e62cc791b1539
    role: target
  - path: data/records/ground-waste-tire-rubber.yaml
    sha256: 73d1bbb5d61980816468cc5830ccaeb845d25c130e6ca662d93573fce51d04f6
    role: target
  - path: data/records/ion-adsorption-rare-earth-clay.yaml
    sha256: 3a3c3cd05e03e27a3cb97e31d3ebc9c1f9b4c89747a48b029257cc02570ecf1d
    role: target
  - path: data/records/iron-ore-tailings.yaml
    sha256: 98414fa5f270d8814225c1ae9d2538e312d6a6887de12e05c92c37c6e429ab85
    role: target
  - path: data/records/pharmaceutical-blister-packaging-waste.yaml
    sha256: 36ac8dcc787e0b2aeecf15fb69fa958139ddf434570e72adad8ab0396bb07314
    role: target
  - path: data/records/polymetallic-nodules.yaml
    sha256: 1fb81047e94d62e7af4cf218733f32692e8cd90443acd64c4c60c4dbbef8f20d
    role: target
  - path: data/records/rhenium.yaml
    sha256: 59c1bacd1db51f21812d36386b2cbfd9c9b1bd72e0db247d27f1f4c5b69e66eb
    role: target
  - path: data/records/rubidium.yaml
    sha256: 62a20be29cbb1a2bd4c750a81fb68916283fbd8388400ceae2022f08b3888979
    role: target
  - path: data/records/spent-lead-acid-battery-electrolyte.yaml
    sha256: e7c1729cb7d7bef64858cdc6e78ef7d48da7081e96e2d842f32e54d93345149c
    role: target
  - path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    sha256: 7aac22892924322ff61a41160d000a7c283c7291c133872aa9a53affac822e90
    role: target
  - path: data/records/strontium.yaml
    sha256: d21d19f117baa3c2de01985b956e7bdc4b7a13d37552f7faa28ef626b939f28e
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: 4c74d42f39dd4d6262a1d8badae5476c1f4e83786fb1e4817f161985752ba585
    role: target
  - path: data/records/waste-printed-circuit-boards.yaml
    sha256: 7f7f5fd7a65e2d2aa31bbd749a755e24bfdb167a515fdec7abd86a159228e58d
    role: target
  - path: data/records/zinc-leach-residue.yaml
    sha256: d64d9222f66148173474919996974a4e10b31d4665e382b3037fa30492555580
    role: target
  - path: data/records/zinc-purification-hot-filter-cake.yaml
    sha256: 909cb9279b6ebd29cce82bd0fdfb3d0b7e090b0fb4654d2c609c785294d36a0e
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml
    sha256: 757e91d63f85ce1e0a97b5f05f7150273dff631c57ea0a65d4fa9333afbc48ee
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/review_findings.yaml
    sha256: 16f18d1c01170e0ca9338b0840e6896a53d3d690ab06b1944003e3bba82c0c12
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
  - path: scripts/curate_causal_graphs.py
    sha256: 494f015ce04021225b4028e8e3e19f236abba52533d3892577e8a33a3e2e632b
    role: context
targets:
- target_id: cmmmech:aluminium-salt-slag
  path: data/records/aluminium-salt-slag.yaml
  label: Aluminium salt slag
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: f31a28c98f2c037a2ee9e37da497dcab6cd06a72b27b10222292c36f1f659de4
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aluminium-salt-slag.yaml
    role: maintained_record
- target_id: cmmmech:beryllium
  path: data/records/beryllium.yaml
  label: Beryllium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 0ff626937b20c67f599e0535e2dadb1e36ce609c67cb6f3f23ddacf23f70ad39
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/beryllium.yaml
    role: maintained_record
- target_id: cmmmech:beverage-carton-hydropulping-reject
  path: data/records/beverage-carton-hydropulping-reject.yaml
  label: Beverage-carton hydropulping reject
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 05b031168a5d5252480c761d8086efc17da3148ad93a853d1c24d2c8438a49a6
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/beverage-carton-hydropulping-reject.yaml
    role: maintained_record
- target_id: cmmmech:biogas-desulfurization-sulfur-residue
  path: data/records/biogas-desulfurization-sulfur-residue.yaml
  label: Biogas-desulfurization sulfur residue
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 4eaadd285f03fceea5d7585dd4b6fc1c3f1518a5de7860c19554aa34bda665bf
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/biogas-desulfurization-sulfur-residue.yaml
    role: maintained_record
- target_id: cmmmech:cadmium-telluride-photovoltaic-module-scrap
  path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
  label: Cadmium telluride photovoltaic module scrap
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 065a221c1de73f390e7b7f08cf1391f5c62999256ce36c855818edddecba17bd
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
    role: maintained_record
- target_id: cmmmech:cathode-ray-tube-glass
  path: data/records/cathode-ray-tube-glass.yaml
  label: Waste lead-bearing cathode-ray-tube glass
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: cea5a34fa657ba00099095e5637b00ba1930b6e94be929fac38de23e411a3bd3
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cathode-ray-tube-glass.yaml
    role: maintained_record
- target_id: cmmmech:cesium
  path: data/records/cesium.yaml
  label: Cesium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2aecf6989d43185ffe6159c78608b2ef7ebed9e385d0f011729ce6f49e2eb837
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cesium.yaml
    role: maintained_record
- target_id: cmmmech:churchite-y
  path: data/records/churchite-y.yaml
  label: Churchite-(Y)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: e073d16091cb57b9731f52bcc6cbdc4320bb945b834d68455114c3eb05b8d1bc
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/churchite-y.yaml
    role: maintained_record
- target_id: cmmmech:electroformed-copper-silver-manufacturing-scrap
  path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
  label: Electroformed copper-silver manufacturing scrap
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 87bd1a5ff7b1c17609b424e0e8a6a7067a2915e1274fe705fce49a4bc2b90264
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
    role: maintained_record
- target_id: cmmmech:end-of-life-cigs-photovoltaic-modules
  path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
  label: End-of-life CIGS photovoltaic modules
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 198e37f10fb40f72829f6ebc9be9f7a98de65edb24a2c2f4a9a0d170e4f702a3
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
    role: maintained_record
- target_id: cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
  label: End-of-life crystalline-silicon photovoltaic modules
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: cd3c53e1a586a308bbce2493dbe065e47ea1fd5cc73166ef1a79b9be50743d6a
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
    role: maintained_record
- target_id: cmmmech:ground-waste-tire-rubber
  path: data/records/ground-waste-tire-rubber.yaml
  label: Ground waste tire rubber
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: a9958fa3441ffef8f998e474e233f4573f40b18983044723c956a75c49af250b
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ground-waste-tire-rubber.yaml
    role: maintained_record
- target_id: cmmmech:ion-adsorption-rare-earth-clay
  path: data/records/ion-adsorption-rare-earth-clay.yaml
  label: Ion-adsorption rare-earth clay
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3c9fc670d1fd3f68ce5be64ed433f4d250fc15101a5be6fb5ce3e196788b6d46
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ion-adsorption-rare-earth-clay.yaml
    role: maintained_record
- target_id: cmmmech:iron-ore-tailings
  path: data/records/iron-ore-tailings.yaml
  label: Iron-ore tailings
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 0eaf4b26a5f5d0240ca02c1c7d9e18a3f46a419e6cea0a90eee55bae97e72d6d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/iron-ore-tailings.yaml
    role: maintained_record
- target_id: cmmmech:pharmaceutical-blister-packaging-waste
  path: data/records/pharmaceutical-blister-packaging-waste.yaml
  label: Pharmaceutical blister packaging waste
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 0f4dc7ca1e11037b4ce5a8fb7f162c545d9d82c42947980e307f2ca405187cc1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pharmaceutical-blister-packaging-waste.yaml
    role: maintained_record
- target_id: cmmmech:polymetallic-nodules
  path: data/records/polymetallic-nodules.yaml
  label: Polymetallic nodules
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: fab97753b23ebebb810b5a3f4e263f59f382f5da59205a0cfd0ff414c3b81427
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polymetallic-nodules.yaml
    role: maintained_record
- target_id: cmmmech:rhenium
  path: data/records/rhenium.yaml
  label: Rhenium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 7c08650cdaf81a985aefbce6bab5c295955fc27131331875637889311a69b36d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhenium.yaml
    role: maintained_record
- target_id: cmmmech:rubidium
  path: data/records/rubidium.yaml
  label: Rubidium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c17ae5337a61868cec53c1e20e333c7fcc5b3d4b5b365c31300ad63ba34c781c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rubidium.yaml
    role: maintained_record
- target_id: cmmmech:spent-lead-acid-battery-electrolyte
  path: data/records/spent-lead-acid-battery-electrolyte.yaml
  label: Spent lead-acid battery electrolyte
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: f86cc902287d59085e8c14c2741d762a13db05d62dcf114815682640eba41d5c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-lead-acid-battery-electrolyte.yaml
    role: maintained_record
- target_id: cmmmech:spent-vanadium-flow-battery-electrolyte
  path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
  label: Spent vanadium-flow-battery electrolyte
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 917e69030fccb0ad8102149c6c96efb317d838acb5d609fbc15762d8727e71ea
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    role: maintained_record
- target_id: cmmmech:strontium
  path: data/records/strontium.yaml
  label: Strontium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: beb81fcbf1f1b607090a6fd4a61e49ce8bac0bcc744e2884176b3c09e05b201a
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontium.yaml
    role: maintained_record
- target_id: cmmmech:traction-battery-hydrometallurgical-residue
  path: data/records/traction-battery-hydrometallurgical-residue.yaml
  label: Traction-battery hydrometallurgical residue
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 297c045e370e01fba95d2084eea94e0172007568d7f636faf0e6b9dbe745fec7
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
- target_id: cmmmech:waste-printed-circuit-boards
  path: data/records/waste-printed-circuit-boards.yaml
  label: Waste printed circuit boards
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 052ba050d0b82cc88fdf8e570469723163a9ee29544a8f88e2571a2de01cd9fe
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-printed-circuit-boards.yaml
    role: maintained_record
- target_id: cmmmech:zinc-leach-residue
  path: data/records/zinc-leach-residue.yaml
  label: Zinc leach residue
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: dc67d8ee174142efddf66e2f5678e98169c42a1195db170521d7b4c5e6c4c1d8
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-leach-residue.yaml
    role: maintained_record
- target_id: cmmmech:zinc-purification-hot-filter-cake
  path: data/records/zinc-purification-hot-filter-cake.yaml
  label: Zinc purification hot filter cake
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: accdea40a7f88794ead6c6b5cf25dc088c7015345888b7191646d45ddc66fde3
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-purification-hot-filter-cake.yaml
    role: maintained_record
scope:
  description: 'All 25 CMMMech records affected by the 3 Cycle 4 Stage 4 findings
    carried into Stage 5 (1 record in GRP-C4S5-001 / #862, 8 records in GRP-C4S5-002
    / #863, and 16 records in GRP-C4S5-003 / #864).'
  selection: cycle4_stage4_open_finding_targets
  coverage: full
  population_size: 25
  reviewed_target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cesium
  - cmmmech:churchite-y
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:iron-ore-tailings
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:polymetallic-nodules
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
checks:
- check_id: chk-validate-records
  name: Schema and semantic record validation
  status: passed
  required: true
  summary: All 663 records (including all 25 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --strict with 0 errors and 0 warnings.
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cesium
  - cmmmech:churchite-y
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:iron-ore-tailings
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:polymetallic-nodules
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  command: .venv/bin/python -m cmmmech.cli validate --strict
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle4-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 25 new EDIT history sidecars and existing history sidecars (1,098 total)
    pass .venv/bin/python -m cmmmech.cli validate-history --base main.
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cesium
  - cmmmech:churchite-y
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:iron-ore-tailings
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:polymetallic-nodules
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle4-stage4-findings
  - ev-new-history-script
- check_id: chk-traction-battery-causal-graph-fidelity
  name: Lu et al. (2025) substrate and five-member consortium causal-graph alignment
    in traction-battery-hydrometallurgical-residue.yaml (#862)
  status: passed
  required: true
  summary: In data/records/traction-battery-hydrometallurgical-residue.yaml, causal_graphs[0]
    (ferrooxidans_battery_residue_bioleaching_graph) now labels node solid_feed_substrate
    as 'Industrial traction-battery hydrometallurgical residues (nickel-line and cobalt-line
    residues)', nodes[0] as 'Sqr / Sqor sulfide-quinone reductase (consortium sqr
    / sqor)', nodes[1] as 'Tth / TetH tetrathionate hydrolase (consortium tth)', and
    edges[0].evidence[0].explanation as 'Reduced sulfur oxidation in the five-member
    acidophile consortium couples Sqr/Sqor and tetrathionate hydrolysis to sulfuric
    acid proton generation.'
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle4-stage4-findings
  - ev-schema
- check_id: chk-canonical-key-order-mechanisms-after-sources
  name: Canonical top-level key ordering (sources/criticality before mechanisms/causal_graphs)
    across 8 records (#863)
  status: passed
  required: true
  summary: All 8 records in GRP-C4S5-002 (cadmium-telluride-photovoltaic-module-scrap,
    cathode-ray-tube-glass, churchite-y, end-of-life-cigs-photovoltaic-modules, end-of-life-crystalline-silicon-photovoltaic-modules,
    iron-ore-tailings, polymetallic-nodules, waste-printed-circuit-boards) now serialize
    top-level sources and criticality before mechanisms and causal_graphs in exact
    CANONICAL_RECORD_KEYS order.
  target_ids:
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:churchite-y
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:iron-ore-tailings
  - cmmmech:polymetallic-nodules
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
- check_id: chk-canonical-key-order-curation-history-before-history-refs
  name: Canonical top-level key ordering (curation_history before history_refs) across
    16 records (#864)
  status: passed
  required: true
  summary: All 16 records in GRP-C4S5-003 (aluminium-salt-slag, beryllium, beverage-carton-hydropulping-reject,
    biogas-desulfurization-sulfur-residue, cesium, electroformed-copper-silver-manufacturing-scrap,
    ground-waste-tire-rubber, ion-adsorption-rare-earth-clay, pharmaceutical-blister-packaging-waste,
    rhenium, rubidium, spent-lead-acid-battery-electrolyte, spent-vanadium-flow-battery-electrolyte,
    strontium, zinc-leach-residue, zinc-purification-hot-filter-cake) now serialize
    top-level curation_history before history_refs in exact CANONICAL_RECORD_KEYS
    order.
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cesium
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-lu2025-doi
  kind: primary_source
  reference: https://doi.org/10.3390/recycling10030113
  locator: Lu et al. (2025) Recycling 10(3):113, Section 2.1-2.2 & Results (nickel-line
    and cobalt-line residues; five-member acidophile consortium)
  accessed_at: '2026-10-30T10:36:00Z'
  support: supports
  summary: Lu et al. (2025) characterize separate nickel-line and cobalt-line hydrometallurgical
    residues from traction-battery recycling bioleached by a five-member acidophile
    consortium (Acidithiobacillus ferrooxidans, Acidithiobacillus caldus, Leptospirillum
    ferriphilum, Sulfobacillus thermosulfidooxidans, Ferroplasma thermophilum).
- evidence_id: ev-cycle4-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2]
  accessed_at: '2026-10-30T10:36:00Z'
  support: supports
  summary: Frozen Cycle 4 Stage 4 review findings ledger defining cmmmech-cycle4-stage4-finding-0001,
    cmmmech-cycle4-stage4-finding-0002, and cmmmech-cycle4-stage4-finding-0003 across
    the 25 target records.
  snapshot_sha256: 16f18d1c01170e0ca9338b0840e6896a53d3d690ab06b1944003e3bba82c0c12
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge
  accessed_at: '2026-10-30T10:36:00Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord top-level slot order and
    CausalGraph structure.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
- evidence_id: ev-new-history-script
  kind: record_content
  reference: scripts/curate_causal_graphs.py
  locator: CANONICAL_RECORD_KEYS
  accessed_at: '2026-10-30T10:36:00Z'
  support: supports
  summary: Canonical top-level YAML key ordering tuple CANONICAL_RECORD_KEYS placing
    sources and criticality before mechanisms and causal_graphs, and curation_history
    before history_refs.
  snapshot_sha256: 494f015ce04021225b4028e8e3e19f236abba52533d3892577e8a33a3e2e632b
assessments:
- assessment_id: assess-grp1-traction-battery-causal-graph
  area: graph
  topic: Lu et al. (2025) substrate and consortium label fidelity in traction-battery-hydrometallurgical-residue.yaml
    (#862)
  outcome: supported
  summary: causal_graphs[0] in data/records/traction-battery-hydrometallurgical-residue.yaml
    now accurately names the nickel-line and cobalt-line traction-battery hydrometallurgical
    residues from Lu et al. (2025) without spurious bauxite-residue sample codes (BR1,
    BR2, BR4) and reflects the five-member acidophile consortium across nodes[0..1].label
    and edges[0].evidence[0].explanation.
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle4-stage4-findings
  - ev-schema
  metrics:
  - name: traction_battery_causal_graph_node_edge_label_fidelity
    value: 1.0
    unit: fraction
    definition: Fraction of causal_graphs[0] nodes and edges in traction-battery-hydrometallurgical-residue.yaml
      aligned with Lu et al. (2025)
    denominator: 7
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-sources-before-mechanisms-order
  area: consistency
  topic: Canonical top-level key ordering (sources/criticality before mechanisms/causal_graphs)
    across 8 records (#863)
  outcome: supported
  summary: All 8 records in GRP-C4S5-002 now serialize top-level keys in exact CANONICAL_RECORD_KEYS
    order with sources and criticality preceding mechanisms and causal_graphs, achieving
    100% corpus-wide uniformity across all 663 records.
  target_ids:
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:churchite-y
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:iron-ore-tailings
  - cmmmech:polymetallic-nodules
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
  metrics:
  - name: corpus_sources_before_mechanisms_key_order_uniformity
    value: 1.0
    unit: fraction
    definition: Fraction of CMMMech records serializing sources and criticality before
      mechanisms and causal_graphs
    denominator: 663
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-curation-history-before-history-refs-order
  area: consistency
  topic: Canonical top-level key ordering (curation_history before history_refs) across
    16 records (#864)
  outcome: supported
  summary: All 16 records in GRP-C4S5-003 now serialize top-level keys in exact CANONICAL_RECORD_KEYS
    order with curation_history preceding history_refs, achieving 100% corpus-wide
    uniformity across all 663 records.
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cesium
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
  metrics:
  - name: corpus_curation_history_before_history_refs_key_order_uniformity
    value: 1.0
    unit: fraction
    definition: Fraction of CMMMech records serializing curation_history before history_refs
    denominator: 663
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle4-stage4-finding-0001
  issue_key: cmmmech.traction-battery-hydrometallurgical-residue.causal-node-spurious-br-sample-codes-and-consortium-label
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: traction-battery-hydrometallurgical-residue.yaml causal_graphs[0] node and
    edge labels now match Lu et al. (2025) substrate and consortium scope
  description: Updated causal_graphs[0] (ferrooxidans_battery_residue_bioleaching_graph)
    in data/records/traction-battery-hydrometallurgical-residue.yaml so nodes[3].label
    (solid_feed_substrate) reads 'Industrial traction-battery hydrometallurgical residues
    (nickel-line and cobalt-line residues)', nodes[0].label reads 'Sqr / Sqor sulfide-quinone
    reductase (consortium sqr / sqor)', nodes[1].label reads 'Tth / TetH tetrathionate
    hydrolase (consortium tth)', and edges[0].evidence[0].explanation reads 'Reduced
    sulfur oxidation in the five-member acidophile consortium couples Sqr/Sqor and
    tetrathionate hydrolysis to sulfuric acid proton generation.' with an append-only
    EDIT history sidecar.
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  field_paths:
  - causal_graphs[0].nodes[0].label
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[3].label
  - causal_graphs[0].edges[0].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle4-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #862 (group GRP-C4S5-001) by replacing
    spurious ''(BR1, BR2, BR4)'' sample codes on solid_feed_substrate and aligning
    Sqr/Sqor and Tth/TetH labels and edge[0] evidence explanation with the five-member
    acidophile consortium in data/records/traction-battery-hydrometallurgical-residue.yaml
    with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084505Z-cycle4-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084506Z-cycle4-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084508Z-traction-battery-hydrometallurgical-residue-cycle4-stage4-record-review
    finding_id: cmmmech-cycle4-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/862
- finding_id: cmmmech-cycle4-stage4-finding-0002
  issue_key: cmmmech.records.mechanisms-before-sources-key-order
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: 8 records now serialize top-level sources and criticality before mechanisms
    and causal_graphs per CANONICAL_RECORD_KEYS
  description: Normalized top-level YAML key ordering across all 8 affected records
    (cadmium-telluride-photovoltaic-module-scrap, cathode-ray-tube-glass, churchite-y,
    end-of-life-cigs-photovoltaic-modules, end-of-life-crystalline-silicon-photovoltaic-modules,
    iron-ore-tailings, polymetallic-nodules, waste-printed-circuit-boards) to CANONICAL_RECORD_KEYS
    with 8 append-only EDIT history sidecars.
  target_ids:
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:churchite-y
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:iron-ore-tailings
  - cmmmech:polymetallic-nodules
  - cmmmech:waste-printed-circuit-boards
  field_paths:
  - sources
  - criticality
  - mechanisms
  - causal_graphs
  - curation_history
  - history_refs
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cathode-ray-tube-glass.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/churchite-y.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/iron-ore-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/polymetallic-nodules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-printed-circuit-boards.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #863 (group GRP-C4S5-002) by normalizing
    top-level YAML key order to CANONICAL_RECORD_KEYS across all 8 records with append-only
    EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084501Z-cycle4-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084504Z-cycle4-stage4-primary-resource-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084505Z-cycle4-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/863
- finding_id: cmmmech-cycle4-stage4-finding-0003
  issue_key: cmmmech.records.history-refs-before-curation-history-key-order
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: 16 records now serialize top-level curation_history before history_refs per
    CANONICAL_RECORD_KEYS
  description: Normalized top-level YAML key ordering across all 16 affected records
    (aluminium-salt-slag, beryllium, beverage-carton-hydropulping-reject, biogas-desulfurization-sulfur-residue,
    cesium, electroformed-copper-silver-manufacturing-scrap, ground-waste-tire-rubber,
    ion-adsorption-rare-earth-clay, pharmaceutical-blister-packaging-waste, rhenium,
    rubidium, spent-lead-acid-battery-electrolyte, spent-vanadium-flow-battery-electrolyte,
    strontium, zinc-leach-residue, zinc-purification-hot-filter-cake) to CANONICAL_RECORD_KEYS
    with 16 append-only EDIT history sidecars.
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cesium
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  field_paths:
  - curation_history
  - history_refs
  evidence_ids:
  - ev-new-history-script
  - ev-cycle4-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aluminium-salt-slag.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/beryllium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/beverage-carton-hydropulping-reject.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/biogas-desulfurization-sulfur-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/cesium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/ground-waste-tire-rubber.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/ion-adsorption-rare-earth-clay.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/pharmaceutical-blister-packaging-waste.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/rhenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/rubidium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-lead-acid-battery-electrolyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/strontium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-leach-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-purification-hot-filter-cake.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #864 (group GRP-C4S5-003) by normalizing
    top-level YAML key order to CANONICAL_RECORD_KEYS across all 16 records with append-only
    EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084500Z-cycle4-stage4-element-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084504Z-cycle4-stage4-primary-resource-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T084505Z-cycle4-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle4-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/864
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:aluminium-salt-slag
  - cmmmech:beryllium
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cesium
  - cmmmech:churchite-y
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:iron-ore-tailings
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:polymetallic-nodules
  - cmmmech:rhenium
  - cmmmech:rubidium
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:strontium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle4-stage4-findings
  - ev-schema
  - ev-new-history-script
  rationale: All 25 remediated records represent distinct material entities (5 elements,
    1 mineral, 2 primary resources, and 17 secondary resources) with disjoint identifiers
    and provenance; cohort boundaries from Cycle 4 Stage 4 are retained unchanged.
limitations:
- This verification review is scoped to the 25 records remediated in Cycle 4 Stage
  5; the remaining 638 records were verified with 0 open findings in the immutable
  Cycle 4 Stage 4 review bundles.
```
