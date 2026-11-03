# Cycle 6 Stage 5 Post-Remediation Verification Review: 19 Remediated CMMMech Records

- Review: 20261103T055100Z-cycle6-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-03T05:50:30Z
- Finished UTC: 2026-11-03T05:51:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation scientific and structural verification of all 19 CMMMech records remediated in Cycle 6 Stage 5 (run mech-goal-sequence-20261019, cycle 6, stage 5) across GitHub issues #901 (GRP-C6S5-001: cmmmech-cycle6-stage4-finding-0001, traction-battery-hydrometallurgical-residue.yaml causal_graphs[0].nodes[1] tth_hydrolase label updated to 'Tth / TetH tetrathionate hydrolase (consortium tth / tetH)' and description updated to reflect all 4 attached consortium protein_examples: Acidithiobacillus ferrooxidans ATCC 23270 tth / AFE_0029 [UniProtKB:B7J3C9], Acidithiobacillus thiooxidans ATCC 19377 tth / GCD22_14205 [UniProtKB:A0A5P9XPU3] and tth / GCD22_02315 [UniProtKB:A0A5P9XS05], and Acidithiobacillus caldus SM-1 Atc_1595 / TetH [UniProtKB:F9ZNI0]), #902 (GRP-C6S5-002: cmmmech-cycle6-stage4-finding-0002, 16 single-species Acidithiobacillus thiooxidans records updated so causal_graphs[0].nodes[1] tth_hydrolase label reads 'Tth tetrathionate hydrolase (tth GCD22_14205; tth GCD22_02315)' and description names both periplasmic pyrroloquinoline-domain tetrathionate hydrolase paralogs [UniProtKB:A0A5P9XPU3 and UniProtKB:A0A5P9XS05]), and #903 (GRP-C6S5-003: cmmmech-cycle6-stage4-finding-0003, vielleaureite-ce.yaml populated with ima_symbol: Vlr-Ce per IMA 2022-134 / Ragu et al. 2025 and xianhuaite-ce.yaml populated with ima_symbol: Xhu-Ce per IMA 2024-091 / Yang et al. 2026). All 3 carried-forward Cycle 6 Stage 4 findings are verified as resolved with 19 append-only EDIT history sidecars.

## Scope And Provenance

All 19 CMMMech records affected by the 3 Cycle 6 Stage 4 findings carried into Stage 5 (1 record in GRP-C6S5-001 / #901, 16 records in GRP-C6S5-002 / #902, and 2 records in GRP-C6S5-003 / #903).

Selection: cycle6_stage4_open_finding_targets
Coverage: full; 19 reviewed / 19 in the declared population.
Source: git_commit at Git base 08304a088fc550056e5f85461cd3aa06d727555d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:arsenic | data/records/arsenic.yaml | maintained | Arsenic |
| cmmmech:automotive-wastewater-treatment-sludge | data/records/automotive-wastewater-treatment-sludge.yaml | maintained | Automotive wastewater-treatment sludge |
| cmmmech:blast-furnace-cast-house-dust | data/records/blast-furnace-cast-house-dust.yaml | maintained | Blast-furnace cast-house dust |
| cmmmech:copper-smelter-slag | data/records/copper-smelter-slag.yaml | maintained | Copper smelter slag |
| cmmmech:discarded-led-lamps | data/records/discarded-led-lamps.yaml | maintained | Discarded light-emitting-diode lamps |
| cmmmech:electric-arc-furnace-dust | data/records/electric-arc-furnace-dust.yaml | maintained | Electric-arc-furnace dust |
| cmmmech:gaas-production-hydroxide-sludge | data/records/gaas-production-hydroxide-sludge.yaml | maintained | GaAs wafer-production hydroxide sludge |
| cmmmech:gallium | data/records/gallium.yaml | maintained | Gallium |
| cmmmech:gold-mine-tailings | data/records/gold-mine-tailings.yaml | maintained | Gold-mine tailings |
| cmmmech:metallic-machining-burrs | data/records/metallic-machining-burrs.yaml | maintained | Metallic machining burrs |
| cmmmech:nickel-based-superalloy-residue-powders | data/records/nickel-based-superalloy-residue-powders.yaml | maintained | Nickel-based superalloy residue powders |
| cmmmech:spent-alkaline-zinc-carbon-batteries | data/records/spent-alkaline-zinc-carbon-batteries.yaml | maintained | Spent alkaline and zinc-carbon batteries |
| cmmmech:spent-automotive-three-way-catalyst | data/records/spent-automotive-three-way-catalyst.yaml | maintained | Spent automotive three-way catalyst |
| cmmmech:spent-hydrodesulfurization-catalyst | data/records/spent-hydrodesulfurization-catalyst.yaml | maintained | Spent hydrodesulfurization catalyst |
| cmmmech:spent-selective-catalytic-reduction-catalyst | data/records/spent-selective-catalytic-reduction-catalyst.yaml | maintained | Spent selective catalytic reduction catalyst |
| cmmmech:spent-sulfuric-acid-production-catalyst | data/records/spent-sulfuric-acid-production-catalyst.yaml | maintained | Spent sulfuric-acid-production catalyst |
| cmmmech:traction-battery-hydrometallurgical-residue | data/records/traction-battery-hydrometallurgical-residue.yaml | maintained | Traction-battery hydrometallurgical residue |
| cmmmech:vielleaureite-ce | data/records/vielleaureite-ce.yaml | maintained | Vielleaureite-(Ce) |
| cmmmech:xianhuaite-ce | data/records/xianhuaite-ce.yaml | maintained | Xianhuaite-(Ce) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema and semantic record validation | passed | True | cmmmech:arsenic, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:blast-furnace-cast-house-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gallium, cmmmech:gold-mine-tailings, cmmmech:metallic-machining-burrs, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:vielleaureite-ce, cmmmech:xianhuaite-ce | All 673 records (including all 19 remediated records) pass .venv/bin/python -m cmmmech.cli validate --strict with 0 errors and 0 warnings. |
| Append-only history sidecar validation | passed | True | cmmmech:arsenic, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:blast-furnace-cast-house-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gallium, cmmmech:gold-mine-tailings, cmmmech:metallic-machining-burrs, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:vielleaureite-ce, cmmmech:xianhuaite-ce | All 19 new EDIT history sidecars and existing history sidecars (1245 total) pass .venv/bin/python -m cmmmech.cli validate-history --base main. |
| Consortium Tth / TetH tetrathionate hydrolase label and description fidelity in traction-battery-hydrometallurgical-residue.yaml (#901) | passed | True | cmmmech:traction-battery-hydrometallurgical-residue | In data/records/traction-battery-hydrometallurgical-residue.yaml, causal_graphs[0].nodes[1] (tth_hydrolase) now carries label 'Tth / TetH tetrathionate hydrolase (consortium tth / tetH)' and description naming all 4 attached consortium protein_examples (Acidithiobacillus ferrooxidans ATCC 23270 tth / AFE_0029 [UniProtKB:B7J3C9]; Acidithiobacillus thiooxidans ATCC 19377 tth / GCD22_14205 [UniProtKB:A0A5P9XPU3] and tth / GCD22_02315 [UniProtKB:A0A5P9XS05]; Acidithiobacillus caldus SM-1 Atc_1595 / TetH [UniProtKB:F9ZNI0]). |
| Acidithiobacillus thiooxidans ATCC 19377 tth paralog label and description fidelity across 16 records (#902) | passed | True | cmmmech:arsenic, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:blast-furnace-cast-house-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gallium, cmmmech:gold-mine-tailings, cmmmech:metallic-machining-burrs, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-sulfuric-acid-production-catalyst | Across all 16 single-species Acidithiobacillus thiooxidans records in GRP-C6S5-002 (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge, gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst), causal_graphs[0].nodes[1] (tth_hydrolase) now carries label 'Tth tetrathionate hydrolase (tth GCD22_14205; tth GCD22_02315)' and description 'Periplasmic pyrroloquinoline-domain tetrathionate hydrolase paralogs (tth GCD22_14205 and tth GCD22_02315) disproportionating tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.' |
| IMA-CNMNC mineral symbol completeness on vielleaureite-ce.yaml and xianhuaite-ce.yaml (#903) | passed | True | cmmmech:vielleaureite-ce, cmmmech:xianhuaite-ce | data/records/vielleaureite-ce.yaml (IMA:2022-134, ragu_2025_vielleaureite_ce) now carries top-level ima_symbol: Vlr-Ce and data/records/xianhuaite-ce.yaml (IMA:2024-091, yang_2026_xianhuaite_ce) now carries top-level ima_symbol: Xhu-Ce immediately after material_kind: mineral (2/2 = 100% of GRP-C6S5-003 targets, bringing mineral records in CMMMech whose descriptions state an IMA-CNMNC symbol to 4/4 = 100% across the 422-mineral corpus: andreybulakhite, vielleaureite-ce, xianhuaite-ce, yttrotungstite-nd). |

## Scientific And Domain Assessments

### Consortium Tth / TetH tetrathionate hydrolase label and description fidelity in traction-battery-hydrometallurgical-residue.yaml (#901)

graph: supported. Targets: cmmmech:traction-battery-hydrometallurgical-residue.

causal_graphs[0].nodes[1] (tth_hydrolase) in data/records/traction-battery-hydrometallurgical-residue.yaml now accurately names all 4 attached consortium tetrathionate hydrolase protein_examples across Acidithiobacillus ferrooxidans ATCC 23270, Acidithiobacillus thiooxidans ATCC 19377, and Acidithiobacillus caldus SM-1.

### Acidithiobacillus thiooxidans ATCC 19377 tth paralog label and description fidelity across 16 records (#902)

graph: supported. Targets: cmmmech:arsenic, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:blast-furnace-cast-house-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gallium, cmmmech:gold-mine-tailings, cmmmech:metallic-machining-burrs, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-sulfuric-acid-production-catalyst.

All 16 single-species Acidithiobacillus thiooxidans records in GRP-C6S5-002 now carry causal_graphs[0].nodes[1] (tth_hydrolase) label 'Tth tetrathionate hydrolase (tth GCD22_14205; tth GCD22_02315)' and description naming both periplasmic pyrroloquinoline-domain tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3 and UniProtKB:A0A5P9XS05).

### Top-level ima_symbol completeness across mineral records stating an IMA-CNMNC symbol in description (#903)

completeness: supported. Targets: cmmmech:vielleaureite-ce, cmmmech:xianhuaite-ce.

Adding ima_symbol: Vlr-Ce to vielleaureite-ce.yaml and ima_symbol: Xhu-Ce to xianhuaite-ce.yaml resolves 2/2 (100%) of the GRP-C6S5-003 targets and brings top-level ima_symbol completeness across mineral records in the 422-mineral CMMMech corpus whose descriptions state an IMA-CNMNC symbol to 100% (4/4: andreybulakhite, vielleaureite-ce, xianhuaite-ce, yttrotungstite-nd).

## Findings

### cmmmech-cycle6-stage4-finding-0001: traction-battery-hydrometallurgical-residue.yaml causal_graphs[0].nodes[1] (tth_hydrolase) label and description now reflect all 4 consortium Tth/TetH protein_examples

minor / resolved / confirmed; issue key: cmmmech.traction-battery-hydrometallurgical-residue.tth-hydrolase-consortium-label-and-description-omit-species-and-loci.

Updated causal_graphs[0].nodes[1] (id: tth_hydrolase) in data/records/traction-battery-hydrometallurgical-residue.yaml so label reads 'Tth / TetH tetrathionate hydrolase (consortium tth / tetH)' and description reads 'Periplasmic pyrroloquinoline-domain tetrathionate hydrolase (Acidithiobacillus ferrooxidans ATCC 23270 tth / AFE_0029; Acidithiobacillus thiooxidans ATCC 19377 tth / GCD22_14205 and tth / GCD22_02315; Acidithiobacillus caldus SM-1 Atc_1595 / TetH) disproportionating tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.' with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #901 (group GRP-C6S5-001) by updating causal_graphs[0].nodes[1] (tth_hydrolase) label and description in data/records/traction-battery-hydrometallurgical-residue.yaml to name all 4 attached consortium protein_examples (UniProtKB:B7J3C9, UniProtKB:A0A5P9XPU3, UniProtKB:A0A5P9XS05, UniProtKB:F9ZNI0) with an append-only EDIT history sidecar.

### cmmmech-cycle6-stage4-finding-0002: 16 single-species Acidithiobacillus thiooxidans records now name both tth paralogs (GCD22_14205 and GCD22_02315) on causal_graphs[0].nodes[1] (tth_hydrolase)

minor / resolved / confirmed; issue key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci.

Updated causal_graphs[0].nodes[1] (id: tth_hydrolase) across all 16 single-species Acidithiobacillus thiooxidans records (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge, gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst) so label reads 'Tth tetrathionate hydrolase (tth GCD22_14205; tth GCD22_02315)' and description reads 'Periplasmic pyrroloquinoline-domain tetrathionate hydrolase paralogs (tth GCD22_14205 and tth GCD22_02315) disproportionating tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.' with 16 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #902 (group GRP-C6S5-002) by updating causal_graphs[0].nodes[1] (tth_hydrolase) label and description across all 16 single-species Acidithiobacillus thiooxidans records to name both attached paralogs (tth GCD22_14205 / UniProtKB:A0A5P9XPU3 and tth GCD22_02315 / UniProtKB:A0A5P9XS05) with 16 append-only EDIT history sidecars.

### cmmmech-cycle6-stage4-finding-0003: vielleaureite-ce.yaml and xianhuaite-ce.yaml now carry top-level ima_symbol: Vlr-Ce and ima_symbol: Xhu-Ce

minor / resolved / confirmed; issue key: cmmmech.round124-minerals.missing-ima-symbol-slot.

Populated top-level ima_symbol: Vlr-Ce in data/records/vielleaureite-ce.yaml (IMA:2022-134, ragu_2025_vielleaureite_ce) and top-level ima_symbol: Xhu-Ce in data/records/xianhuaite-ce.yaml (IMA:2024-091, yang_2026_xianhuaite_ce) immediately after material_kind: mineral via scripts/curate_causal_graphs.py with 2 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #903 (group GRP-C6S5-003) by populating ima_symbol: Vlr-Ce in data/records/vielleaureite-ce.yaml and ima_symbol: Xhu-Ce in data/records/xianhuaite-ce.yaml with 2 append-only EDIT history sidecars.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:arsenic, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:blast-furnace-cast-house-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gallium, cmmmech:gold-mine-tailings, cmmmech:metallic-machining-burrs, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:vielleaureite-ce, cmmmech:xianhuaite-ce. All 19 remediated records represent distinct material entities (2 elements, 2 IMA-approved minerals, and 15 secondary resources) with disjoint identifiers and provenance; cohort boundaries from Cycle 6 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-lu2025-doi | https://doi.org/10.1039/D5RA07472J; Lu et al. (2025) RSC Advances 15:45979-45985 (five-member acidophile consortium including A. ferrooxidans, A. thiooxidans, A. caldus) | supports | Lu et al. (2025) report bioleaching of traction-battery hydrometallurgical residues by a five-member acidophile consortium including Acidithiobacillus ferrooxidans, Acidithiobacillus thiooxidans, and Acidithiobacillus caldus. |
| ev-ragu2025-vielleaureite | https://doi.org/10.5194/ejm-37-627-2025; Ragu et al. (2025) European Journal of Mineralogy 37:627-638 (IMA 2022-134, symbol Vlr-Ce) | supports | Ragu et al. (2025) define IMA-CNMNC approved mineral species vielleaureite-(Ce) (IMA 2022-134) with official IMA symbol Vlr-Ce. |
| ev-yang2026-xianhuaite | https://doi.org/10.5194/ejm-38-449-2026; Yang et al. (2026) European Journal of Mineralogy 38:449-459 (IMA 2024-091, symbol Xhu-Ce) | supports | Yang et al. (2026) define IMA-CNMNC approved mineral species xianhuaite-(Ce) (IMA 2024-091) with official IMA symbol Xhu-Ce. |
| ev-cycle6-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/review_findings.yaml; findings[0..2] | supports | Frozen Cycle 6 Stage 4 review findings ledger defining cmmmech-cycle6-stage4-finding-0001, cmmmech-cycle6-stage4-finding-0002, and cmmmech-cycle6-stage4-finding-0003 across the 19 target records. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.CausalGraph, classes.CausalNode | supports | Canonical LinkML schema defining MaterialRecord top-level slots (including ima_symbol) and CausalNode structure. |
| ev-curate-causal-graphs-script | scripts/curate_causal_graphs.py; CANONICAL_RECORD_KEYS, apply_curation_patch, curate_record_file | supports | Native writer scripts/curate_causal_graphs.py enforcing CANONICAL_RECORD_KEYS ordering, ima_symbol and causal_graphs patching, pre/post validation, and atomic history sidecar minting. |

## Limits And Additional Notes

- This verification review is scoped to the 19 records remediated in Cycle 6 Stage 5; the remaining 654 records were verified with 0 open findings in the immutable Cycle 6 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T055100Z-cycle6-stage5-remediation-verification
title: 'Cycle 6 Stage 5 Post-Remediation Verification Review: 19 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-03T05:50:30Z'
finished_at: '2026-11-03T05:51:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation scientific and structural verification of all 19 CMMMech
  records remediated in Cycle 6 Stage 5 (run mech-goal-sequence-20261019, cycle 6,
  stage 5) across GitHub issues #901 (GRP-C6S5-001: cmmmech-cycle6-stage4-finding-0001,
  traction-battery-hydrometallurgical-residue.yaml causal_graphs[0].nodes[1] tth_hydrolase
  label updated to ''Tth / TetH tetrathionate hydrolase (consortium tth / tetH)''
  and description updated to reflect all 4 attached consortium protein_examples: Acidithiobacillus
  ferrooxidans ATCC 23270 tth / AFE_0029 [UniProtKB:B7J3C9], Acidithiobacillus thiooxidans
  ATCC 19377 tth / GCD22_14205 [UniProtKB:A0A5P9XPU3] and tth / GCD22_02315 [UniProtKB:A0A5P9XS05],
  and Acidithiobacillus caldus SM-1 Atc_1595 / TetH [UniProtKB:F9ZNI0]), #902 (GRP-C6S5-002:
  cmmmech-cycle6-stage4-finding-0002, 16 single-species Acidithiobacillus thiooxidans
  records updated so causal_graphs[0].nodes[1] tth_hydrolase label reads ''Tth tetrathionate
  hydrolase (tth GCD22_14205; tth GCD22_02315)'' and description names both periplasmic
  pyrroloquinoline-domain tetrathionate hydrolase paralogs [UniProtKB:A0A5P9XPU3 and
  UniProtKB:A0A5P9XS05]), and #903 (GRP-C6S5-003: cmmmech-cycle6-stage4-finding-0003,
  vielleaureite-ce.yaml populated with ima_symbol: Vlr-Ce per IMA 2022-134 / Ragu
  et al. 2025 and xianhuaite-ce.yaml populated with ima_symbol: Xhu-Ce per IMA 2024-091
  / Yang et al. 2026). All 3 carried-forward Cycle 6 Stage 4 findings are verified
  as resolved with 19 append-only EDIT history sidecars.'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage5-remediation-reviewer
  kind: agent
  independence: self_review
  independence_basis: Cycle 6 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 19 remediated records against the immutable Cycle 6 Stage 4 review bundles.
  model: claude-opus-4-6
source:
  git_revision: 08304a088fc550056e5f85461cd3aa06d727555d
  state: git_commit
  inputs:
  - path: data/records/arsenic.yaml
    sha256: db6cce965d9da92e0e467a658aba89650641a2f2d085acc9235c9302c2a082d8
    role: target
  - path: data/records/automotive-wastewater-treatment-sludge.yaml
    sha256: 3ecbb1148dac1955490a9828d000443b12d5b1e36c806f086faf9a3d9aa3e4a0
    role: target
  - path: data/records/blast-furnace-cast-house-dust.yaml
    sha256: 187f2bb3e6b1b377c651fa230ccfa9d51a898fa3ca0ec324d116223d080ae417
    role: target
  - path: data/records/copper-smelter-slag.yaml
    sha256: 43f5812d94ef7f7c40173dbf2b0793a544aa5194522f8163a3e24c695c907b4c
    role: target
  - path: data/records/discarded-led-lamps.yaml
    sha256: 872552ec28cd80bca6dacee0ee4babfa8f571984e24ea729c189de7b03915de4
    role: target
  - path: data/records/electric-arc-furnace-dust.yaml
    sha256: 31557f49a45a894dd499521dedcd75cade1e7b3b1def66f56896540afa4a2c83
    role: target
  - path: data/records/gaas-production-hydroxide-sludge.yaml
    sha256: b9677948646ca58ea26fd2baef613b4f64fbb559cf2dfdc6da46de44e1dbe093
    role: target
  - path: data/records/gallium.yaml
    sha256: ee9aa739bd3c1d87873ba882935859f09e622c6bad8fbd9d3034d91ddc40fe87
    role: target
  - path: data/records/gold-mine-tailings.yaml
    sha256: 7077c6e8a219090d8432c6834fea67516786c14f50507744ef51a9ba4386a30e
    role: target
  - path: data/records/metallic-machining-burrs.yaml
    sha256: 6182f9b2753b47195cc26c94f1772934ae0d987e5c36377ac32fef0427126a46
    role: target
  - path: data/records/nickel-based-superalloy-residue-powders.yaml
    sha256: ba1eabc24f734db33e5a02a2a78b5f1e75490ffaf02f84835a0285b1b8b4bf32
    role: target
  - path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    sha256: c75e9006922469b56de8e557ba85b83af1700f6a1940ec3661b3ad14dd8db49b
    role: target
  - path: data/records/spent-automotive-three-way-catalyst.yaml
    sha256: 1afb2a4aff423eb668648f0ea877d4475f526289648e25e1c1c488bd1f26b3df
    role: target
  - path: data/records/spent-hydrodesulfurization-catalyst.yaml
    sha256: 86bc77dd92c351cc76173dcc22bd17645e1d02256d4d69a34b96f9872ec46f83
    role: target
  - path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
    sha256: a34fbf8bdb8a8b1e0fec3bb38916de7599e56ee98c6e1d81484227d38ef1d9ee
    role: target
  - path: data/records/spent-sulfuric-acid-production-catalyst.yaml
    sha256: 54fa1806a43da00d6969c839113f5dd004086df533153de1ad3f9cb13c1917ad
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: 73d8a1db9c82ee916f08ca2999bf85f83e188ae0e8f303f79fbc931fe2819ab9
    role: target
  - path: data/records/vielleaureite-ce.yaml
    sha256: 5f4d28a543f76359da981ccebd905e7515bfed5e31815e33dbbebe97a00e4fc4
    role: target
  - path: data/records/xianhuaite-ce.yaml
    sha256: 571fccb1b93d3ee08717e4d26e179e2e4cbacea2d4a0d86542bc80c7145df836
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/evidence.yaml
    sha256: 5bfba508f2d5a6d9d49a3f925332602d2f47d3938c8ad5b3edd923bc9b9f4670
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/review_findings.yaml
    sha256: fd273d209a32243394b9a7be4581f3cb9766478c461c461b9c80dca1ad1585d6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
  - path: scripts/curate_causal_graphs.py
    sha256: 6efd202fd19c9690f31024159a27c4c48bad7e9117f238f78c9ac3ed87acd24d
    role: context
targets:
- target_id: cmmmech:arsenic
  path: data/records/arsenic.yaml
  label: Arsenic
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 31823074eb018d4c45180bca8a6075de05a4d6b8b307fa1879924c11cb4a914d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenic.yaml
    role: maintained_record
- target_id: cmmmech:automotive-wastewater-treatment-sludge
  path: data/records/automotive-wastewater-treatment-sludge.yaml
  label: Automotive wastewater-treatment sludge
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 4c128412fceccb098d2e1565fc1eaa0d3b4f40ad71bc4210dcd77f724b0979e0
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/automotive-wastewater-treatment-sludge.yaml
    role: maintained_record
- target_id: cmmmech:blast-furnace-cast-house-dust
  path: data/records/blast-furnace-cast-house-dust.yaml
  label: Blast-furnace cast-house dust
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 07835e59381f2aecbafa6c650161193d368eb0ba3d43a81f3db2c5d158551097
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/blast-furnace-cast-house-dust.yaml
    role: maintained_record
- target_id: cmmmech:copper-smelter-slag
  path: data/records/copper-smelter-slag.yaml
  label: Copper smelter slag
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: d1be15116987cbdde0632164dad7f748297b9ec10851bf7d29892e1845ea1c8b
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-smelter-slag.yaml
    role: maintained_record
- target_id: cmmmech:discarded-led-lamps
  path: data/records/discarded-led-lamps.yaml
  label: Discarded light-emitting-diode lamps
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: ad785cf996b50b79480c991c9461bc539d289eea15a8de66557254cd3126b382
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/discarded-led-lamps.yaml
    role: maintained_record
- target_id: cmmmech:electric-arc-furnace-dust
  path: data/records/electric-arc-furnace-dust.yaml
  label: Electric-arc-furnace dust
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 69dbd565271e55c01fbf2c7c23050a81d5172b8fcbf388f85ddff19d387cf5cb
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electric-arc-furnace-dust.yaml
    role: maintained_record
- target_id: cmmmech:gaas-production-hydroxide-sludge
  path: data/records/gaas-production-hydroxide-sludge.yaml
  label: GaAs wafer-production hydroxide sludge
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 59cd71562e6b3a98587cbbd08357b0cb415c7989ed8656c537a0985e6b821de0
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gaas-production-hydroxide-sludge.yaml
    role: maintained_record
- target_id: cmmmech:gallium
  path: data/records/gallium.yaml
  label: Gallium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 49e752858350d3cd8445751ff8cc625e28c2b606d8e85a343b00772b8899c95e
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gallium.yaml
    role: maintained_record
- target_id: cmmmech:gold-mine-tailings
  path: data/records/gold-mine-tailings.yaml
  label: Gold-mine tailings
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c3c47decb38b455ef1e0a7862c1866785b530f4496d7e62af69f7478c7925225
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gold-mine-tailings.yaml
    role: maintained_record
- target_id: cmmmech:metallic-machining-burrs
  path: data/records/metallic-machining-burrs.yaml
  label: Metallic machining burrs
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: e43d9a4cc848442a95075751a399788f593233f6dc29796734d21ca456129f6d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metallic-machining-burrs.yaml
    role: maintained_record
- target_id: cmmmech:nickel-based-superalloy-residue-powders
  path: data/records/nickel-based-superalloy-residue-powders.yaml
  label: Nickel-based superalloy residue powders
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 03f339776c07e742d50c9540e6c9471921e39fefe35d7b34450b344f9b460a0c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-based-superalloy-residue-powders.yaml
    role: maintained_record
- target_id: cmmmech:spent-alkaline-zinc-carbon-batteries
  path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
  label: Spent alkaline and zinc-carbon batteries
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 8f0f68d4a572743969c638b31045992d98212dac279da2733219e1ea048cd0d7
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    role: maintained_record
- target_id: cmmmech:spent-automotive-three-way-catalyst
  path: data/records/spent-automotive-three-way-catalyst.yaml
  label: Spent automotive three-way catalyst
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 43fa227c7864eb08209b402c5a15f792f159d8a4036eb4546f17d4678be6910c
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-automotive-three-way-catalyst.yaml
    role: maintained_record
- target_id: cmmmech:spent-hydrodesulfurization-catalyst
  path: data/records/spent-hydrodesulfurization-catalyst.yaml
  label: Spent hydrodesulfurization catalyst
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: cb8cc29c2b27e50260103ee540f53d43d55b138b3d3fea4ff31901d3b433833f
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-hydrodesulfurization-catalyst.yaml
    role: maintained_record
- target_id: cmmmech:spent-selective-catalytic-reduction-catalyst
  path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
  label: Spent selective catalytic reduction catalyst
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: bf3952c1abff5365fbb10969a20900695600ccb5e8029da6781cb53037310f48
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
    role: maintained_record
- target_id: cmmmech:spent-sulfuric-acid-production-catalyst
  path: data/records/spent-sulfuric-acid-production-catalyst.yaml
  label: Spent sulfuric-acid-production catalyst
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: d410746c54f991a4a04ef8b0d0621a285984c2b19189cf080ffe945b13aed01d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-sulfuric-acid-production-catalyst.yaml
    role: maintained_record
- target_id: cmmmech:traction-battery-hydrometallurgical-residue
  path: data/records/traction-battery-hydrometallurgical-residue.yaml
  label: Traction-battery hydrometallurgical residue
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: ab761af5f5da7749af6ad7d39a6d1a84d4e10b77dd0c200ddf7c08bb577ac60a
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
- target_id: cmmmech:vielleaureite-ce
  path: data/records/vielleaureite-ce.yaml
  label: Vielleaureite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 755387309635da1e588a6c8e49699723e764ec1853f0537c5d42f3b5f3a0f2bc
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vielleaureite-ce.yaml
    role: maintained_record
- target_id: cmmmech:xianhuaite-ce
  path: data/records/xianhuaite-ce.yaml
  label: Xianhuaite-(Ce)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 96babb9c222e2bb62a78648e173c6a6cd2a40d8335f12150a6da0d049eed9bc7
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xianhuaite-ce.yaml
    role: maintained_record
scope:
  description: 'All 19 CMMMech records affected by the 3 Cycle 6 Stage 4 findings
    carried into Stage 5 (1 record in GRP-C6S5-001 / #901, 16 records in GRP-C6S5-002
    / #902, and 2 records in GRP-C6S5-003 / #903).'
  selection: cycle6_stage4_open_finding_targets
  coverage: full
  population_size: 19
  reviewed_target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
checks:
- check_id: chk-validate-records
  name: Schema and semantic record validation
  status: passed
  required: true
  summary: All 673 records (including all 19 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --strict with 0 errors and 0 warnings.
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  command: .venv/bin/python -m cmmmech.cli validate --strict
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle6-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 19 new EDIT history sidecars and existing history sidecars (1245 total)
    pass .venv/bin/python -m cmmmech.cli validate-history --base main.
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle6-stage4-findings
  - ev-curate-causal-graphs-script
- check_id: chk-traction-battery-tth-hydrolase-consortium-fidelity
  name: Consortium Tth / TetH tetrathionate hydrolase label and description fidelity
    in traction-battery-hydrometallurgical-residue.yaml (#901)
  status: passed
  required: true
  summary: In data/records/traction-battery-hydrometallurgical-residue.yaml, causal_graphs[0].nodes[1]
    (tth_hydrolase) now carries label 'Tth / TetH tetrathionate hydrolase (consortium
    tth / tetH)' and description naming all 4 attached consortium protein_examples
    (Acidithiobacillus ferrooxidans ATCC 23270 tth / AFE_0029 [UniProtKB:B7J3C9];
    Acidithiobacillus thiooxidans ATCC 19377 tth / GCD22_14205 [UniProtKB:A0A5P9XPU3]
    and tth / GCD22_02315 [UniProtKB:A0A5P9XS05]; Acidithiobacillus caldus SM-1 Atc_1595
    / TetH [UniProtKB:F9ZNI0]).
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle6-stage4-findings
  - ev-schema
- check_id: chk-single-species-thiooxidans-tth-paralog-fidelity
  name: Acidithiobacillus thiooxidans ATCC 19377 tth paralog label and description
    fidelity across 16 records (#902)
  status: passed
  required: true
  summary: Across all 16 single-species Acidithiobacillus thiooxidans records in GRP-C6S5-002
    (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust,
    copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge,
    gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders,
    spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst,
    spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst),
    causal_graphs[0].nodes[1] (tth_hydrolase) now carries label 'Tth tetrathionate
    hydrolase (tth GCD22_14205; tth GCD22_02315)' and description 'Periplasmic pyrroloquinoline-domain
    tetrathionate hydrolase paralogs (tth GCD22_14205 and tth GCD22_02315) disproportionating
    tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.'
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  evidence_ids:
  - ev-cycle6-stage4-findings
  - ev-schema
  - ev-curate-causal-graphs-script
- check_id: chk-ima-symbol-completeness-vielleaureite-xianhuaite
  name: IMA-CNMNC mineral symbol completeness on vielleaureite-ce.yaml and xianhuaite-ce.yaml
    (#903)
  status: passed
  required: true
  summary: 'data/records/vielleaureite-ce.yaml (IMA:2022-134, ragu_2025_vielleaureite_ce)
    now carries top-level ima_symbol: Vlr-Ce and data/records/xianhuaite-ce.yaml (IMA:2024-091,
    yang_2026_xianhuaite_ce) now carries top-level ima_symbol: Xhu-Ce immediately
    after material_kind: mineral (2/2 = 100% of GRP-C6S5-003 targets, bringing mineral
    records in CMMMech whose descriptions state an IMA-CNMNC symbol to 4/4 = 100%
    across the 422-mineral corpus: andreybulakhite, vielleaureite-ce, xianhuaite-ce,
    yttrotungstite-nd).'
  target_ids:
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  evidence_ids:
  - ev-ragu2025-vielleaureite
  - ev-yang2026-xianhuaite
  - ev-cycle6-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-lu2025-doi
  kind: primary_source
  reference: https://doi.org/10.1039/D5RA07472J
  locator: Lu et al. (2025) RSC Advances 15:45979-45985 (five-member acidophile consortium
    including A. ferrooxidans, A. thiooxidans, A. caldus)
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Lu et al. (2025) report bioleaching of traction-battery hydrometallurgical
    residues by a five-member acidophile consortium including Acidithiobacillus ferrooxidans,
    Acidithiobacillus thiooxidans, and Acidithiobacillus caldus.
- evidence_id: ev-ragu2025-vielleaureite
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-37-627-2025
  locator: Ragu et al. (2025) European Journal of Mineralogy 37:627-638 (IMA 2022-134,
    symbol Vlr-Ce)
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Ragu et al. (2025) define IMA-CNMNC approved mineral species vielleaureite-(Ce)
    (IMA 2022-134) with official IMA symbol Vlr-Ce.
- evidence_id: ev-yang2026-xianhuaite
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-38-449-2026
  locator: Yang et al. (2026) European Journal of Mineralogy 38:449-459 (IMA 2024-091,
    symbol Xhu-Ce)
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Yang et al. (2026) define IMA-CNMNC approved mineral species xianhuaite-(Ce)
    (IMA 2024-091) with official IMA symbol Xhu-Ce.
- evidence_id: ev-cycle6-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2]
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Frozen Cycle 6 Stage 4 review findings ledger defining cmmmech-cycle6-stage4-finding-0001,
    cmmmech-cycle6-stage4-finding-0002, and cmmmech-cycle6-stage4-finding-0003 across
    the 19 target records.
  snapshot_sha256: fd273d209a32243394b9a7be4581f3cb9766478c461c461b9c80dca1ad1585d6
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.CausalGraph, classes.CausalNode
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord top-level slots (including
    ima_symbol) and CausalNode structure.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
- evidence_id: ev-curate-causal-graphs-script
  kind: record_content
  reference: scripts/curate_causal_graphs.py
  locator: CANONICAL_RECORD_KEYS, apply_curation_patch, curate_record_file
  accessed_at: '2026-11-03T05:50:30Z'
  support: supports
  summary: Native writer scripts/curate_causal_graphs.py enforcing CANONICAL_RECORD_KEYS
    ordering, ima_symbol and causal_graphs patching, pre/post validation, and atomic
    history sidecar minting.
  snapshot_sha256: 6efd202fd19c9690f31024159a27c4c48bad7e9117f238f78c9ac3ed87acd24d
assessments:
- assessment_id: assess-grp1-traction-battery-tth-hydrolase
  area: graph
  topic: Consortium Tth / TetH tetrathionate hydrolase label and description fidelity
    in traction-battery-hydrometallurgical-residue.yaml (#901)
  outcome: supported
  summary: causal_graphs[0].nodes[1] (tth_hydrolase) in data/records/traction-battery-hydrometallurgical-residue.yaml
    now accurately names all 4 attached consortium tetrathionate hydrolase protein_examples
    across Acidithiobacillus ferrooxidans ATCC 23270, Acidithiobacillus thiooxidans
    ATCC 19377, and Acidithiobacillus caldus SM-1.
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle6-stage4-findings
  - ev-schema
  metrics:
  - name: traction_battery_tth_hydrolase_protein_examples_prose_coverage
    value: 1.0
    unit: fraction
    definition: Fraction of attached protein_examples on tth_hydrolase represented
      in node label and description
    denominator: 4
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-single-species-thiooxidans-tth-paralogs
  area: graph
  topic: Acidithiobacillus thiooxidans ATCC 19377 tth paralog label and description
    fidelity across 16 records (#902)
  outcome: supported
  summary: All 16 single-species Acidithiobacillus thiooxidans records in GRP-C6S5-002
    now carry causal_graphs[0].nodes[1] (tth_hydrolase) label 'Tth tetrathionate hydrolase
    (tth GCD22_14205; tth GCD22_02315)' and description naming both periplasmic pyrroloquinoline-domain
    tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3 and UniProtKB:A0A5P9XS05).
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  evidence_ids:
  - ev-cycle6-stage4-findings
  - ev-schema
  - ev-curate-causal-graphs-script
  metrics:
  - name: single_species_thiooxidans_tth_hydrolase_prose_alignment
    value: 1.0
    unit: fraction
    definition: Fraction of single-species A. thiooxidans records whose tth_hydrolase
      node label and description name both tth paralogs
    denominator: 16
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-mineral-ima-symbol-completeness
  area: completeness
  topic: Top-level ima_symbol completeness across mineral records stating an IMA-CNMNC
    symbol in description (#903)
  outcome: supported
  summary: 'Adding ima_symbol: Vlr-Ce to vielleaureite-ce.yaml and ima_symbol: Xhu-Ce
    to xianhuaite-ce.yaml resolves 2/2 (100%) of the GRP-C6S5-003 targets and brings
    top-level ima_symbol completeness across mineral records in the 422-mineral CMMMech
    corpus whose descriptions state an IMA-CNMNC symbol to 100% (4/4: andreybulakhite,
    vielleaureite-ce, xianhuaite-ce, yttrotungstite-nd).'
  target_ids:
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  evidence_ids:
  - ev-ragu2025-vielleaureite
  - ev-yang2026-xianhuaite
  - ev-cycle6-stage4-findings
  - ev-schema
  metrics:
  - name: mineral_cohort_ima_symbol_completeness
    value: 1.0
    unit: fraction
    definition: Fraction of mineral records in CMMMech whose descriptions state an
      IMA-CNMNC symbol that carry a populated top-level ima_symbol slot
    denominator: 4
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle6-stage4-finding-0001
  issue_key: cmmmech.traction-battery-hydrometallurgical-residue.tth-hydrolase-consortium-label-and-description-omit-species-and-loci
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: traction-battery-hydrometallurgical-residue.yaml causal_graphs[0].nodes[1]
    (tth_hydrolase) label and description now reflect all 4 consortium Tth/TetH protein_examples
  description: 'Updated causal_graphs[0].nodes[1] (id: tth_hydrolase) in data/records/traction-battery-hydrometallurgical-residue.yaml
    so label reads ''Tth / TetH tetrathionate hydrolase (consortium tth / tetH)''
    and description reads ''Periplasmic pyrroloquinoline-domain tetrathionate hydrolase
    (Acidithiobacillus ferrooxidans ATCC 23270 tth / AFE_0029; Acidithiobacillus thiooxidans
    ATCC 19377 tth / GCD22_14205 and tth / GCD22_02315; Acidithiobacillus caldus SM-1
    Atc_1595 / TetH) disproportionating tetrathionate into thiosulfate, elemental
    sulfur, sulfate, and protons.'' with an append-only EDIT history sidecar.'
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - curation_history
  - history_refs
  evidence_ids:
  - ev-lu2025-doi
  - ev-cycle6-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #901 (group GRP-C6S5-001) by updating
    causal_graphs[0].nodes[1] (tth_hydrolase) label and description in data/records/traction-battery-hydrometallurgical-residue.yaml
    to name all 4 attached consortium protein_examples (UniProtKB:B7J3C9, UniProtKB:A0A5P9XPU3,
    UniProtKB:A0A5P9XS05, UniProtKB:F9ZNI0) with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132005Z-cycle6-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132006Z-cycle6-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132007Z-traction-battery-hydrometallurgical-residue-cycle6-stage4-record-review
    finding_id: cmmmech-cycle6-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/901
- finding_id: cmmmech-cycle6-stage4-finding-0002
  issue_key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: 16 single-species Acidithiobacillus thiooxidans records now name both tth
    paralogs (GCD22_14205 and GCD22_02315) on causal_graphs[0].nodes[1] (tth_hydrolase)
  description: 'Updated causal_graphs[0].nodes[1] (id: tth_hydrolase) across all 16
    single-species Acidithiobacillus thiooxidans records (arsenic, automotive-wastewater-treatment-sludge,
    blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust,
    gaas-production-hydroxide-sludge, gallium, gold-mine-tailings, metallic-machining-burrs,
    nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries,
    spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst,
    spent-sulfuric-acid-production-catalyst) so label reads ''Tth tetrathionate hydrolase
    (tth GCD22_14205; tth GCD22_02315)'' and description reads ''Periplasmic pyrroloquinoline-domain
    tetrathionate hydrolase paralogs (tth GCD22_14205 and tth GCD22_02315) disproportionating
    tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.'' with
    16 append-only EDIT history sidecars.'
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - curation_history
  - history_refs
  evidence_ids:
  - ev-cycle6-stage4-findings
  - ev-schema
  - ev-curate-causal-graphs-script
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenic.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/automotive-wastewater-treatment-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/blast-furnace-cast-house-dust.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-smelter-slag.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/discarded-led-lamps.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/electric-arc-furnace-dust.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/gaas-production-hydroxide-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/gallium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/gold-mine-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/metallic-machining-burrs.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-based-superalloy-residue-powders.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-automotive-three-way-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-hydrodesulfurization-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-sulfuric-acid-production-catalyst.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #902 (group GRP-C6S5-002) by updating
    causal_graphs[0].nodes[1] (tth_hydrolase) label and description across all 16
    single-species Acidithiobacillus thiooxidans records to name both attached paralogs
    (tth GCD22_14205 / UniProtKB:A0A5P9XPU3 and tth GCD22_02315 / UniProtKB:A0A5P9XS05)
    with 16 append-only EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132000Z-cycle6-stage4-element-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132005Z-cycle6-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132006Z-cycle6-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132008Z-arsenic-cycle6-stage4-record-review
    finding_id: cmmmech-cycle6-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/902
- finding_id: cmmmech-cycle6-stage4-finding-0003
  issue_key: cmmmech.round124-minerals.missing-ima-symbol-slot
  category: completeness
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'vielleaureite-ce.yaml and xianhuaite-ce.yaml now carry top-level ima_symbol:
    Vlr-Ce and ima_symbol: Xhu-Ce'
  description: 'Populated top-level ima_symbol: Vlr-Ce in data/records/vielleaureite-ce.yaml
    (IMA:2022-134, ragu_2025_vielleaureite_ce) and top-level ima_symbol: Xhu-Ce in
    data/records/xianhuaite-ce.yaml (IMA:2024-091, yang_2026_xianhuaite_ce) immediately
    after material_kind: mineral via scripts/curate_causal_graphs.py with 2 append-only
    EDIT history sidecars.'
  target_ids:
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  field_paths:
  - ima_symbol
  - curation_history
  - history_refs
  evidence_ids:
  - ev-ragu2025-vielleaureite
  - ev-yang2026-xianhuaite
  - ev-cycle6-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vielleaureite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/xianhuaite-ce.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #903 (group GRP-C6S5-003) by populating
    ima_symbol: Vlr-Ce in data/records/vielleaureite-ce.yaml and ima_symbol: Xhu-Ce
    in data/records/xianhuaite-ce.yaml with 2 append-only EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132001Z-cycle6-stage4-mineral-cohort-review
    finding_id: cmmmech-cycle6-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261031T132009Z-xianhuaite-ce-cycle6-stage4-record-review
    finding_id: cmmmech-cycle6-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/903
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:arsenic
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gallium
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:vielleaureite-ce
  - cmmmech:xianhuaite-ce
  evidence_ids:
  - ev-lu2025-doi
  - ev-ragu2025-vielleaureite
  - ev-yang2026-xianhuaite
  - ev-cycle6-stage4-findings
  - ev-schema
  rationale: All 19 remediated records represent distinct material entities (2 elements,
    2 IMA-approved minerals, and 15 secondary resources) with disjoint identifiers
    and provenance; cohort boundaries from Cycle 6 Stage 4 are retained unchanged.
limitations:
- This verification review is scoped to the 19 records remediated in Cycle 6 Stage
  5; the remaining 654 records were verified with 0 open findings in the immutable
  Cycle 6 Stage 4 review bundles.
```
