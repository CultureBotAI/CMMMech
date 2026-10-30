# Cycle 5 Stage 5 Post-Remediation Verification Review: 15 Remediated CMMMech Records

- Review: 20261030T222000Z-cycle5-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T22:18:00Z
- Finished UTC: 2026-10-30T22:20:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation scientific and structural verification of all 15 CMMMech records remediated in Cycle 5 Stage 5 (run mech-goal-sequence-20261019, cycle 5, stage 5) across GitHub issues #877 (GRP-C5S5-001: cmmmech-cycle5-stage4-finding-0001, 13 records normalized to serialize top-level sources before criticality per CANONICAL_RECORD_KEYS), #878 (GRP-C5S5-002: cmmmech-cycle5-stage4-finding-0002, tetrahedrite-concentrate.yaml causal_graphs[0] tth_hydrolase node label/description and outgoing edge[0] evidence explanation updated to cover both Acidithiobacillus ferrooxidans tth/AFE_0029 and Acidithiobacillus ferrivorans tetH/UniProtKB:A0A060URH6 per Kupka et al. 2025), and #879 (GRP-C5S5-003: cmmmech-cycle5-stage4-finding-0003, waste-liquid-crystal-display-panels.yaml causal_graphs[0] tth_hydrolase node label and description updated to include both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs GCD22_14205 and GCD22_02315 alongside A. ferrooxidans tth/AFE_0029 per Pourhossein &amp; Mousavi 2023). All 3 carried-forward Cycle 5 Stage 4 findings are verified as resolved with 15 append-only EDIT history sidecars.

## Scope And Provenance

All 15 CMMMech records affected by the 3 Cycle 5 Stage 4 findings carried into Stage 5 (13 records in GRP-C5S5-001 / #877, 1 record in GRP-C5S5-002 / #878, and 1 record in GRP-C5S5-003 / #879).

Selection: cycle5_stage4_open_finding_targets
Coverage: full; 15 reviewed / 15 in the declared population.
Source: working_tree at Git base 35a238bcbe1239d32e401f11976481f3e3cb1f5f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chromium | data/records/chromium.yaml | maintained | Chromium |
| cmmmech:electrical-steel | data/records/electrical-steel.yaml | maintained | Electrical steel |
| cmmmech:hafnium | data/records/hafnium.yaml | maintained | Hafnium |
| cmmmech:manganese | data/records/manganese.yaml | maintained | Manganese |
| cmmmech:praseodymium | data/records/praseodymium.yaml | maintained | Praseodymium |
| cmmmech:rare-earth-element-commodities | data/records/rare-earth-element-commodities.yaml | maintained | Rare-earth-element commodities, Australian list scope |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |
| cmmmech:silicon | data/records/silicon.yaml | maintained | Silicon |
| cmmmech:silicon-carbide | data/records/silicon-carbide.yaml | maintained | Silicon carbide |
| cmmmech:synthetic-graphite | data/records/synthetic-graphite.yaml | maintained | Synthetic graphite |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |
| cmmmech:uranium | data/records/uranium.yaml | maintained | Uranium |
| cmmmech:vanadium | data/records/vanadium.yaml | maintained | Vanadium |
| cmmmech:waste-liquid-crystal-display-panels | data/records/waste-liquid-crystal-display-panels.yaml | maintained | Waste liquid-crystal display panels |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema and semantic record validation | passed | True | cmmmech:chromium, cmmmech:electrical-steel, cmmmech:hafnium, cmmmech:manganese, cmmmech:praseodymium, cmmmech:rare-earth-element-commodities, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silicon-carbide, cmmmech:synthetic-graphite, cmmmech:tetrahedrite-concentrate, cmmmech:uranium, cmmmech:vanadium, cmmmech:waste-liquid-crystal-display-panels | All 668 records (including all 15 remediated records) pass .venv/bin/python -m cmmmech.cli validate --strict with 0 errors and 0 warnings. |
| Append-only history sidecar validation | passed | True | cmmmech:chromium, cmmmech:electrical-steel, cmmmech:hafnium, cmmmech:manganese, cmmmech:praseodymium, cmmmech:rare-earth-element-commodities, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silicon-carbide, cmmmech:synthetic-graphite, cmmmech:tetrahedrite-concentrate, cmmmech:uranium, cmmmech:vanadium, cmmmech:waste-liquid-crystal-display-panels | All 15 new EDIT history sidecars and existing history sidecars (1,157 total) pass .venv/bin/python -m cmmmech.cli validate-history --base main. |
| Canonical top-level key ordering (sources before criticality) across 13 records (#877) | passed | True | cmmmech:chromium, cmmmech:electrical-steel, cmmmech:hafnium, cmmmech:manganese, cmmmech:praseodymium, cmmmech:rare-earth-element-commodities, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon-carbide, cmmmech:silicon, cmmmech:synthetic-graphite, cmmmech:uranium, cmmmech:vanadium | All 13 records in GRP-C5S5-001 (chromium, electrical-steel, hafnium, manganese, praseodymium, rare-earth-element-commodities, scandium, selenium, silicon-carbide, silicon, synthetic-graphite, uranium, vanadium) now serialize top-level sources before criticality in exact CANONICAL_RECORD_KEYS order. |
| Shared tth_hydrolase node and edge label/description parity in tetrahedrite-concentrate.yaml (#878) | passed | True | cmmmech:tetrahedrite-concentrate | In data/records/tetrahedrite-concentrate.yaml, causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) now labels node tth_hydrolase as 'Tth / TetH tetrathionate hydrolase (tth / AFE_0029 / tetH)', describes both A. ferrooxidans tth/AFE_0029 and A. ferrivorans tetH (UniProtKB:A0A060URH6), and updates edges[0].evidence[0].explanation to cover both culture arms per Kupka et al. (2025). |
| Shared tth_hydrolase node label/description paralog parity in waste-liquid-crystal-display-panels.yaml (#879) | passed | True | cmmmech:waste-liquid-crystal-display-panels | In data/records/waste-liquid-crystal-display-panels.yaml, causal_graphs[0] (ferrooxidans_lcd_indium_bioleaching_graph) now labels node tth_hydrolase as 'Tth tetrathionate hydrolase (tth AFE_0029 / tth GCD22_14205 / tth GCD22_02315)' and describes both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs (GCD22_14205 and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029). |

## Scientific And Domain Assessments

### Canonical top-level key ordering (sources before criticality) across 13 records (#877)

consistency: supported. Targets: cmmmech:chromium, cmmmech:electrical-steel, cmmmech:hafnium, cmmmech:manganese, cmmmech:praseodymium, cmmmech:rare-earth-element-commodities, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon-carbide, cmmmech:silicon, cmmmech:synthetic-graphite, cmmmech:uranium, cmmmech:vanadium.

All 13 records in GRP-C5S5-001 now serialize top-level keys in exact CANONICAL_RECORD_KEYS order with sources preceding criticality, achieving 100% corpus-wide uniformity across all 668 records.

### Shared tth_hydrolase node and edge parity across A. ferrooxidans and A. ferrivorans in tetrahedrite-concentrate.yaml (#878)

graph: supported. Targets: cmmmech:tetrahedrite-concentrate.

causal_graphs[0] in data/records/tetrahedrite-concentrate.yaml now accurately reflects both Acidithiobacillus ferrooxidans (tth / AFE_0029) and Acidithiobacillus ferrivorans (tetH / UniProtKB:A0A060URH6) across node tth_hydrolase label, description, and outgoing edge[0] evidence explanation.

### Shared tth_hydrolase node label and description parity across A. ferrooxidans and both A. thiooxidans paralogs in waste-liquid-crystal-display-panels.yaml (#879)

graph: supported. Targets: cmmmech:waste-liquid-crystal-display-panels.

causal_graphs[0] in data/records/waste-liquid-crystal-display-panels.yaml now accurately names both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs (GCD22_14205 and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029) in node tth_hydrolase label and description.

## Findings

### cmmmech-cycle5-stage4-finding-0001: 13 records now serialize top-level sources before criticality per CANONICAL_RECORD_KEYS

minor / resolved / confirmed; issue key: cmmmech.records.criticality-before-sources-key-order.

Normalized top-level YAML key ordering across all 13 affected records (chromium, electrical-steel, hafnium, manganese, praseodymium, rare-earth-element-commodities, scandium, selenium, silicon-carbide, silicon, synthetic-graphite, uranium, vanadium) to CANONICAL_RECORD_KEYS with 13 append-only EDIT history sidecars.

Disposition: Resolved under GitHub issue #877 (group GRP-C5S5-001) by normalizing top-level YAML key order to CANONICAL_RECORD_KEYS across all 13 records with append-only EDIT history sidecars.

### cmmmech-cycle5-stage4-finding-0002: tetrahedrite-concentrate.yaml causal_graphs[0] tth_hydrolase node and edge labels now cover both A. ferrooxidans and A. ferrivorans

minor / resolved / confirmed; issue key: cmmmech.tetrahedrite-concentrate.causal-node-tth-hydrolase-species-label-scope.

Updated causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) in data/records/tetrahedrite-concentrate.yaml so nodes[1].label (tth_hydrolase) reads 'Tth / TetH tetrathionate hydrolase (tth / AFE_0029 / tetH)', nodes[1].description names both A. ferrooxidans tth/AFE_0029 and A. ferrivorans CF27 tetH (UniProtKB:A0A060URH6), and edges[0].evidence[0].explanation covers both separate culture arms per Kupka et al. (2025) with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #878 (group GRP-C5S5-002) by updating nodes[1].label, nodes[1].description, and edges[0].evidence[0].explanation in data/records/tetrahedrite-concentrate.yaml with an append-only EDIT history sidecar.

### cmmmech-cycle5-stage4-finding-0003: waste-liquid-crystal-display-panels.yaml causal_graphs[0] tth_hydrolase node label and description now name both A. thiooxidans tth paralogs

minor / resolved / confirmed; issue key: cmmmech.waste-liquid-crystal-display-panels.causal-node-tth-hydrolase-paralog-label-scope.

Updated causal_graphs[0] (ferrooxidans_lcd_indium_bioleaching_graph) in data/records/waste-liquid-crystal-display-panels.yaml so nodes[1].label (tth_hydrolase) reads 'Tth tetrathionate hydrolase (tth AFE_0029 / tth GCD22_14205 / tth GCD22_02315)' and nodes[1].description names both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs (GCD22_14205 and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029) with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #879 (group GRP-C5S5-003) by updating nodes[1].label and nodes[1].description in data/records/waste-liquid-crystal-display-panels.yaml with an append-only EDIT history sidecar.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:chromium, cmmmech:electrical-steel, cmmmech:hafnium, cmmmech:manganese, cmmmech:praseodymium, cmmmech:rare-earth-element-commodities, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silicon-carbide, cmmmech:synthetic-graphite, cmmmech:tetrahedrite-concentrate, cmmmech:uranium, cmmmech:vanadium, cmmmech:waste-liquid-crystal-display-panels. All 15 remediated records represent distinct material entities (9 elements, 4 commodities, 1 primary resource, and 1 secondary resource) with disjoint identifiers and provenance; cohort boundaries from Cycle 5 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-kupka2025-doi | https://doi.org/10.3390/min15050499; Kupka et al. (2025) Minerals 15(5):499, Sections 2-3 (separate A. ferrooxidans DSM 14882 and A. ferrivorans SS3 DSM 17398 bioleaching arms) | supports | Kupka et al. (2025) evaluate alkaline-pretreated and untreated tetrahedrite concentrate bioleaching in separate Acidithiobacillus ferrooxidans DSM 14882 and Acidithiobacillus ferrivorans SS3 (DSM 17398) culture arms. |
| ev-pourhossein2023-doi | https://doi.org/10.1016/j.resconrec.2022.106732; Pourhossein &amp; Mousavi (2023) Resources, Conservation and Recycling 189:106732 (adapted A. ferrooxidans and A. thiooxidans LCD bioleaching) | supports | Pourhossein &amp; Mousavi (2023) characterize biogenic sulfuric acid generation and indium solubilization from waste LCD panels by Acidithiobacillus ferrooxidans and Acidithiobacillus thiooxidans. |
| ev-cycle5-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/review_findings.yaml; findings[0..2] | supports | Frozen Cycle 5 Stage 4 review findings ledger defining cmmmech-cycle5-stage4-finding-0001, cmmmech-cycle5-stage4-finding-0002, and cmmmech-cycle5-stage4-finding-0003 across the 15 target records. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge | supports | Canonical LinkML schema defining MaterialRecord top-level slot order and CausalGraph structure. |
| ev-curate-script | scripts/curate_causal_graphs.py; CANONICAL_RECORD_KEYS | supports | Canonical top-level YAML key ordering tuple CANONICAL_RECORD_KEYS placing sources before criticality, mechanisms, causal_graphs, curation_history, and history_refs. |

## Limits And Additional Notes

- This verification review is scoped to the 15 records remediated in Cycle 5 Stage 5; the remaining 653 records were verified with 0 open findings in the immutable Cycle 5 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T222000Z-cycle5-stage5-remediation-verification
title: 'Cycle 5 Stage 5 Post-Remediation Verification Review: 15 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-30T22:18:00Z'
finished_at: '2026-10-30T22:20:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation scientific and structural verification of all 15 CMMMech
  records remediated in Cycle 5 Stage 5 (run mech-goal-sequence-20261019, cycle 5,
  stage 5) across GitHub issues #877 (GRP-C5S5-001: cmmmech-cycle5-stage4-finding-0001,
  13 records normalized to serialize top-level sources before criticality per CANONICAL_RECORD_KEYS),
  #878 (GRP-C5S5-002: cmmmech-cycle5-stage4-finding-0002, tetrahedrite-concentrate.yaml
  causal_graphs[0] tth_hydrolase node label/description and outgoing edge[0] evidence
  explanation updated to cover both Acidithiobacillus ferrooxidans tth/AFE_0029 and
  Acidithiobacillus ferrivorans tetH/UniProtKB:A0A060URH6 per Kupka et al. 2025),
  and #879 (GRP-C5S5-003: cmmmech-cycle5-stage4-finding-0003, waste-liquid-crystal-display-panels.yaml
  causal_graphs[0] tth_hydrolase node label and description updated to include both
  Acidithiobacillus thiooxidans ATCC 19377 tth paralogs GCD22_14205 and GCD22_02315
  alongside A. ferrooxidans tth/AFE_0029 per Pourhossein & Mousavi 2023). All 3 carried-forward
  Cycle 5 Stage 4 findings are verified as resolved with 15 append-only EDIT history
  sidecars.'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage5-remediation-reviewer
  kind: agent
  independence: self_review
  independence_basis: Cycle 5 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 15 remediated records against the immutable Cycle 5 Stage 4 review bundles.
  model: claude-opus-4-6
source:
  git_revision: 35a238bcbe1239d32e401f11976481f3e3cb1f5f
  state: working_tree
  inputs:
  - path: data/records/chromium.yaml
    sha256: 2e50c5c5458f8c8775db64a97d5ebda883dc45e302e1f6a5e764962f98d00d45
    role: target
  - path: data/records/electrical-steel.yaml
    sha256: 4bdb429a081ea86e470a7c6c6f2e2994eed18caaa8b2c72dcc7541d9d2a4b32e
    role: target
  - path: data/records/hafnium.yaml
    sha256: 6c3d45608b170e149decfa21f2afa6030c11c0a7decda26553d3d1ff652d2fd2
    role: target
  - path: data/records/manganese.yaml
    sha256: 3d9d759613d889fdf23a6bbb16f35b1ace1f36eed87f39add5a5879992d24906
    role: target
  - path: data/records/praseodymium.yaml
    sha256: 2aeae056f98b9571f9c38cf6bd1fb7249db9217c5f750f3de01c93b9bc594545
    role: target
  - path: data/records/rare-earth-element-commodities.yaml
    sha256: e599276f18c442b7fee11ca5638eb0f251e5761e675b5827c7c45963a82b4fe5
    role: target
  - path: data/records/scandium.yaml
    sha256: a5790221b2863ad14ecb1ef28425f2b95659f818a18b658dcd2f2a70e4e5fe16
    role: target
  - path: data/records/selenium.yaml
    sha256: 3c88fca92fd61d7c2c88981eb4497eb71b0d4af4bfa8f2d1acd062735d59fca9
    role: target
  - path: data/records/silicon.yaml
    sha256: f6ac021b6e80e90cae837fcf9726aef132444f34e00cdb368c1fc6c8ef21275a
    role: target
  - path: data/records/silicon-carbide.yaml
    sha256: d1b79510520a2d700f645c33344eacf37e29b80bc0dd0a4b0184ad860b408180
    role: target
  - path: data/records/synthetic-graphite.yaml
    sha256: 50cf7c12dfaff700205d346accacf70195159d308171d7080f89bb4da9ecec4f
    role: target
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 028970846c1d345fc830dcaec41ed55d2f96b7b523a90646af3c3036276018c0
    role: target
  - path: data/records/uranium.yaml
    sha256: 826c448b4b6345f9105a7172edb4e596406b396f38797f0e147ba0e9d1a17249
    role: target
  - path: data/records/vanadium.yaml
    sha256: bc3f67e18b142dd93e5c8d03d89eadd3551efa4b085a74ff4e63b2e366134144
    role: target
  - path: data/records/waste-liquid-crystal-display-panels.yaml
    sha256: 065252079cfc86daa3c8a770ca62b02c3b5fa691c53688f83a80cfb4bf6725f5
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml
    sha256: d77d6b46b063baee49ecc557266e16a8f3b08fbaa55c8ad43543c42df65c57dc
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/review_findings.yaml
    sha256: 0f6b6c28ffeeb331796856984db47e730a531393b844d55e79b3def915843afa
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: d2a31e40b52cee60a86a2897db9b8274b1089c92dd043d83313b7d87e05c6635
    role: context
  - path: scripts/curate_causal_graphs.py
    sha256: 6efd202fd19c9690f31024159a27c4c48bad7e9117f238f78c9ac3ed87acd24d
    role: context
targets:
- target_id: cmmmech:chromium
  path: data/records/chromium.yaml
  label: Chromium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 323e0eac891eae7e673f62cb1d66024641ce2092435cd15ab27f5eef8b8f07d1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium.yaml
    role: maintained_record
- target_id: cmmmech:electrical-steel
  path: data/records/electrical-steel.yaml
  label: Electrical steel
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: de7aa64ed5caf0d44594a4316f7d6d41c43218d83b9f8702d79fe2725c6272f3
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrical-steel.yaml
    role: maintained_record
- target_id: cmmmech:hafnium
  path: data/records/hafnium.yaml
  label: Hafnium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 804ce58b121b40ee42fe2840d40e400ea78b4d5379e6e4b6efe97a96cdb10dea
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hafnium.yaml
    role: maintained_record
- target_id: cmmmech:manganese
  path: data/records/manganese.yaml
  label: Manganese
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 2c1132b328504f10b86c0ed5732849ce8291954aa4fe5583d55f492ad245eaac
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese.yaml
    role: maintained_record
- target_id: cmmmech:praseodymium
  path: data/records/praseodymium.yaml
  label: Praseodymium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 9a8424411ca14b17313fbe24637f8a6b2cbe29703dbd34fa86118e61851f73b0
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/praseodymium.yaml
    role: maintained_record
- target_id: cmmmech:rare-earth-element-commodities
  path: data/records/rare-earth-element-commodities.yaml
  label: Rare-earth-element commodities, Australian list scope
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: f9168378f02431f7305ac55fb802755e0a6f8073dba25d67c1575d5d4e2c92d4
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-element-commodities.yaml
    role: maintained_record
- target_id: cmmmech:scandium
  path: data/records/scandium.yaml
  label: Scandium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: c07e3685b4bf6a9afb85fb99d35a29529e77029e0e82e73259d58e84e4bae46d
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
- target_id: cmmmech:selenium
  path: data/records/selenium.yaml
  label: Selenium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 72e60a1321772cd5aa48cccdfddd30adc305ecac8ab31e16c62ccc2e2d79ce28
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
- target_id: cmmmech:silicon
  path: data/records/silicon.yaml
  label: Silicon
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 8eabbacc0f6585f16d22f3bf14acce40a74b0bc66062e078385e7b999cd6eeb5
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon.yaml
    role: maintained_record
- target_id: cmmmech:silicon-carbide
  path: data/records/silicon-carbide.yaml
  label: Silicon carbide
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 476c782df81c423951952cc3d4392fff2973698a10fd24073393e38a10754211
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon-carbide.yaml
    role: maintained_record
- target_id: cmmmech:synthetic-graphite
  path: data/records/synthetic-graphite.yaml
  label: Synthetic graphite
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 5a8241962c3e603a92d8bc417a20e64934384c4691c02c377f34dec0ee6daca1
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/synthetic-graphite.yaml
    role: maintained_record
- target_id: cmmmech:tetrahedrite-concentrate
  path: data/records/tetrahedrite-concentrate.yaml
  label: Tetrahedrite concentrate
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 427719fb9a1413c370dbf822487ebdc48bf15cba35a14c5e2bdc708e6b1d5de2
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
- target_id: cmmmech:uranium
  path: data/records/uranium.yaml
  label: Uranium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 761dbd8470dc15591aa86fcb4aca13d53dcd934dea0c195178c7e5f6fcaf8b88
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium.yaml
    role: maintained_record
- target_id: cmmmech:vanadium
  path: data/records/vanadium.yaml
  label: Vanadium
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 11d9c430e07a974e72c40fa490bb6161f65edd0cf062f3739ece07a592aadfb2
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vanadium.yaml
    role: maintained_record
- target_id: cmmmech:waste-liquid-crystal-display-panels
  path: data/records/waste-liquid-crystal-display-panels.yaml
  label: Waste liquid-crystal display panels
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 4776059804767d8d97ee4e7e83f7bcc414c5100de6615b1d16ed1fb6bfdbe9bf
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-liquid-crystal-display-panels.yaml
    role: maintained_record
scope:
  description: 'All 15 CMMMech records affected by the 3 Cycle 5 Stage 4 findings
    carried into Stage 5 (13 records in GRP-C5S5-001 / #877, 1 record in GRP-C5S5-002
    / #878, and 1 record in GRP-C5S5-003 / #879).'
  selection: cycle5_stage4_open_finding_targets
  coverage: full
  population_size: 15
  reviewed_target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silicon-carbide
  - cmmmech:synthetic-graphite
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:waste-liquid-crystal-display-panels
checks:
- check_id: chk-validate-records
  name: Schema and semantic record validation
  status: passed
  required: true
  summary: All 668 records (including all 15 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --strict with 0 errors and 0 warnings.
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silicon-carbide
  - cmmmech:synthetic-graphite
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:waste-liquid-crystal-display-panels
  command: .venv/bin/python -m cmmmech.cli validate --strict
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle5-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 15 new EDIT history sidecars and existing history sidecars (1,157 total)
    pass .venv/bin/python -m cmmmech.cli validate-history --base main.
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silicon-carbide
  - cmmmech:synthetic-graphite
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:waste-liquid-crystal-display-panels
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle5-stage4-findings
  - ev-curate-script
- check_id: chk-canonical-key-order-sources-before-criticality
  name: Canonical top-level key ordering (sources before criticality) across 13 records
    (#877)
  status: passed
  required: true
  summary: All 13 records in GRP-C5S5-001 (chromium, electrical-steel, hafnium, manganese,
    praseodymium, rare-earth-element-commodities, scandium, selenium, silicon-carbide,
    silicon, synthetic-graphite, uranium, vanadium) now serialize top-level sources
    before criticality in exact CANONICAL_RECORD_KEYS order.
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon-carbide
  - cmmmech:silicon
  - cmmmech:synthetic-graphite
  - cmmmech:uranium
  - cmmmech:vanadium
  evidence_ids:
  - ev-curate-script
  - ev-cycle5-stage4-findings
  - ev-schema
- check_id: chk-tetrahedrite-concentrate-tth-hydrolase-parity
  name: Shared tth_hydrolase node and edge label/description parity in tetrahedrite-concentrate.yaml
    (#878)
  status: passed
  required: true
  summary: In data/records/tetrahedrite-concentrate.yaml, causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph)
    now labels node tth_hydrolase as 'Tth / TetH tetrathionate hydrolase (tth / AFE_0029
    / tetH)', describes both A. ferrooxidans tth/AFE_0029 and A. ferrivorans tetH
    (UniProtKB:A0A060URH6), and updates edges[0].evidence[0].explanation to cover
    both culture arms per Kupka et al. (2025).
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - ev-kupka2025-doi
  - ev-cycle5-stage4-findings
  - ev-schema
- check_id: chk-waste-lcd-panels-tth-hydrolase-parity
  name: Shared tth_hydrolase node label/description paralog parity in waste-liquid-crystal-display-panels.yaml
    (#879)
  status: passed
  required: true
  summary: In data/records/waste-liquid-crystal-display-panels.yaml, causal_graphs[0]
    (ferrooxidans_lcd_indium_bioleaching_graph) now labels node tth_hydrolase as 'Tth
    tetrathionate hydrolase (tth AFE_0029 / tth GCD22_14205 / tth GCD22_02315)' and
    describes both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs (GCD22_14205
    and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029).
  target_ids:
  - cmmmech:waste-liquid-crystal-display-panels
  evidence_ids:
  - ev-pourhossein2023-doi
  - ev-cycle5-stage4-findings
  - ev-schema
evidence:
- evidence_id: ev-kupka2025-doi
  kind: primary_source
  reference: https://doi.org/10.3390/min15050499
  locator: Kupka et al. (2025) Minerals 15(5):499, Sections 2-3 (separate A. ferrooxidans
    DSM 14882 and A. ferrivorans SS3 DSM 17398 bioleaching arms)
  accessed_at: '2026-10-30T22:20:00Z'
  support: supports
  summary: Kupka et al. (2025) evaluate alkaline-pretreated and untreated tetrahedrite
    concentrate bioleaching in separate Acidithiobacillus ferrooxidans DSM 14882 and
    Acidithiobacillus ferrivorans SS3 (DSM 17398) culture arms.
- evidence_id: ev-pourhossein2023-doi
  kind: primary_source
  reference: https://doi.org/10.1016/j.resconrec.2022.106732
  locator: Pourhossein & Mousavi (2023) Resources, Conservation and Recycling 189:106732
    (adapted A. ferrooxidans and A. thiooxidans LCD bioleaching)
  accessed_at: '2026-10-30T22:20:00Z'
  support: supports
  summary: Pourhossein & Mousavi (2023) characterize biogenic sulfuric acid generation
    and indium solubilization from waste LCD panels by Acidithiobacillus ferrooxidans
    and Acidithiobacillus thiooxidans.
- evidence_id: ev-cycle5-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2]
  accessed_at: '2026-10-30T22:20:00Z'
  support: supports
  summary: Frozen Cycle 5 Stage 4 review findings ledger defining cmmmech-cycle5-stage4-finding-0001,
    cmmmech-cycle5-stage4-finding-0002, and cmmmech-cycle5-stage4-finding-0003 across
    the 15 target records.
  snapshot_sha256: 0f6b6c28ffeeb331796856984db47e730a531393b844d55e79b3def915843afa
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.CausalGraph, classes.CausalNode, classes.CausalEdge
  accessed_at: '2026-10-30T22:20:00Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord top-level slot order and
    CausalGraph structure.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
- evidence_id: ev-curate-script
  kind: record_content
  reference: scripts/curate_causal_graphs.py
  locator: CANONICAL_RECORD_KEYS
  accessed_at: '2026-10-30T22:20:00Z'
  support: supports
  summary: Canonical top-level YAML key ordering tuple CANONICAL_RECORD_KEYS placing
    sources before criticality, mechanisms, causal_graphs, curation_history, and history_refs.
  snapshot_sha256: 6efd202fd19c9690f31024159a27c4c48bad7e9117f238f78c9ac3ed87acd24d
assessments:
- assessment_id: assess-grp1-sources-before-criticality-order
  area: consistency
  topic: Canonical top-level key ordering (sources before criticality) across 13 records
    (#877)
  outcome: supported
  summary: All 13 records in GRP-C5S5-001 now serialize top-level keys in exact CANONICAL_RECORD_KEYS
    order with sources preceding criticality, achieving 100% corpus-wide uniformity
    across all 668 records.
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon-carbide
  - cmmmech:silicon
  - cmmmech:synthetic-graphite
  - cmmmech:uranium
  - cmmmech:vanadium
  evidence_ids:
  - ev-curate-script
  - ev-cycle5-stage4-findings
  - ev-schema
  metrics:
  - name: corpus_sources_before_criticality_key_order_uniformity
    value: 1.0
    unit: fraction
    definition: Fraction of CMMMech records serializing sources before criticality
    denominator: 668
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-tetrahedrite-tth-hydrolase-parity
  area: graph
  topic: Shared tth_hydrolase node and edge parity across A. ferrooxidans and A. ferrivorans
    in tetrahedrite-concentrate.yaml (#878)
  outcome: supported
  summary: causal_graphs[0] in data/records/tetrahedrite-concentrate.yaml now accurately
    reflects both Acidithiobacillus ferrooxidans (tth / AFE_0029) and Acidithiobacillus
    ferrivorans (tetH / UniProtKB:A0A060URH6) across node tth_hydrolase label, description,
    and outgoing edge[0] evidence explanation.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - ev-kupka2025-doi
  - ev-cycle5-stage4-findings
  - ev-schema
  metrics:
  - name: tetrahedrite_tth_hydrolase_protein_example_label_parity
    value: 1.0
    unit: fraction
    definition: Fraction of grounded protein_examples on tetrahedrite-concentrate
      tth_hydrolase represented in node label, description, and edge explanation
    denominator: 2
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-waste-lcd-tth-hydrolase-parity
  area: graph
  topic: Shared tth_hydrolase node label and description parity across A. ferrooxidans
    and both A. thiooxidans paralogs in waste-liquid-crystal-display-panels.yaml (#879)
  outcome: supported
  summary: causal_graphs[0] in data/records/waste-liquid-crystal-display-panels.yaml
    now accurately names both Acidithiobacillus thiooxidans ATCC 19377 tth paralogs
    (GCD22_14205 and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029) in node
    tth_hydrolase label and description.
  target_ids:
  - cmmmech:waste-liquid-crystal-display-panels
  evidence_ids:
  - ev-pourhossein2023-doi
  - ev-cycle5-stage4-findings
  - ev-schema
  metrics:
  - name: waste_lcd_tth_hydrolase_protein_example_label_parity
    value: 1.0
    unit: fraction
    definition: Fraction of grounded protein_examples on waste-liquid-crystal-display-panels
      tth_hydrolase represented in node label and description
    denominator: 3
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle5-stage4-finding-0001
  issue_key: cmmmech.records.criticality-before-sources-key-order
  category: representation
  severity: minor
  status: resolved
  certainty: confirmed
  title: 13 records now serialize top-level sources before criticality per CANONICAL_RECORD_KEYS
  description: Normalized top-level YAML key ordering across all 13 affected records
    (chromium, electrical-steel, hafnium, manganese, praseodymium, rare-earth-element-commodities,
    scandium, selenium, silicon-carbide, silicon, synthetic-graphite, uranium, vanadium)
    to CANONICAL_RECORD_KEYS with 13 append-only EDIT history sidecars.
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon-carbide
  - cmmmech:silicon
  - cmmmech:synthetic-graphite
  - cmmmech:uranium
  - cmmmech:vanadium
  field_paths:
  - sources
  - criticality
  - curation_history
  - history_refs
  evidence_ids:
  - ev-curate-script
  - ev-cycle5-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/electrical-steel.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/hafnium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/praseodymium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-element-commodities.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon-carbide.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/synthetic-graphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/vanadium.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #877 (group GRP-C5S5-001) by normalizing
    top-level YAML key order to CANONICAL_RECORD_KEYS across all 13 records with append-only
    EDIT history sidecars.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201000Z-cycle5-stage4-element-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0001
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201003Z-cycle5-stage4-commodity-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/877
- finding_id: cmmmech-cycle5-stage4-finding-0002
  issue_key: cmmmech.tetrahedrite-concentrate.causal-node-tth-hydrolase-species-label-scope
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: tetrahedrite-concentrate.yaml causal_graphs[0] tth_hydrolase node and edge
    labels now cover both A. ferrooxidans and A. ferrivorans
  description: Updated causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph)
    in data/records/tetrahedrite-concentrate.yaml so nodes[1].label (tth_hydrolase)
    reads 'Tth / TetH tetrathionate hydrolase (tth / AFE_0029 / tetH)', nodes[1].description
    names both A. ferrooxidans tth/AFE_0029 and A. ferrivorans CF27 tetH (UniProtKB:A0A060URH6),
    and edges[0].evidence[0].explanation covers both separate culture arms per Kupka
    et al. (2025) with an append-only EDIT history sidecar.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  - curation_history
  - history_refs
  evidence_ids:
  - ev-kupka2025-doi
  - ev-cycle5-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #878 (group GRP-C5S5-002) by updating
    nodes[1].label, nodes[1].description, and edges[0].evidence[0].explanation in
    data/records/tetrahedrite-concentrate.yaml with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201004Z-cycle5-stage4-primary-resource-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201006Z-cycle5-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0002
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201008Z-tetrahedrite-concentrate-cycle5-stage4-record-review
    finding_id: cmmmech-cycle5-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/878
- finding_id: cmmmech-cycle5-stage4-finding-0003
  issue_key: cmmmech.waste-liquid-crystal-display-panels.causal-node-tth-hydrolase-paralog-label-scope
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: waste-liquid-crystal-display-panels.yaml causal_graphs[0] tth_hydrolase node
    label and description now name both A. thiooxidans tth paralogs
  description: Updated causal_graphs[0] (ferrooxidans_lcd_indium_bioleaching_graph)
    in data/records/waste-liquid-crystal-display-panels.yaml so nodes[1].label (tth_hydrolase)
    reads 'Tth tetrathionate hydrolase (tth AFE_0029 / tth GCD22_14205 / tth GCD22_02315)'
    and nodes[1].description names both Acidithiobacillus thiooxidans ATCC 19377 tth
    paralogs (GCD22_14205 and GCD22_02315) alongside A. ferrooxidans tth (AFE_0029)
    with an append-only EDIT history sidecar.
  target_ids:
  - cmmmech:waste-liquid-crystal-display-panels
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - curation_history
  - history_refs
  evidence_ids:
  - ev-pourhossein2023-doi
  - ev-cycle5-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-liquid-crystal-display-panels.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #879 (group GRP-C5S5-003) by updating
    nodes[1].label and nodes[1].description in data/records/waste-liquid-crystal-display-panels.yaml
    with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201005Z-cycle5-stage4-secondary-resource-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201006Z-cycle5-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle5-stage4-finding-0003
  - repository: CultureBotAI/CMMMech
    review_id: 20261030T201009Z-waste-liquid-crystal-display-panels-cycle5-stage4-record-review
    finding_id: cmmmech-cycle5-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/879
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:chromium
  - cmmmech:electrical-steel
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:rare-earth-element-commodities
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silicon-carbide
  - cmmmech:synthetic-graphite
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:waste-liquid-crystal-display-panels
  evidence_ids:
  - ev-kupka2025-doi
  - ev-pourhossein2023-doi
  - ev-cycle5-stage4-findings
  - ev-schema
  - ev-curate-script
  rationale: All 15 remediated records represent distinct material entities (9 elements,
    4 commodities, 1 primary resource, and 1 secondary resource) with disjoint identifiers
    and provenance; cohort boundaries from Cycle 5 Stage 4 are retained unchanged.
limitations:
- This verification review is scoped to the 15 records remediated in Cycle 5 Stage
  5; the remaining 653 records were verified with 0 open findings in the immutable
  Cycle 5 Stage 4 review bundles.
```
