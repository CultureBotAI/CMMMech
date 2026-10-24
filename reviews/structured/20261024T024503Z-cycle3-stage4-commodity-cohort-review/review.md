# Cycle 3 Stage 4 full-cohort review: commodity records (36/36)

- Review: 20261024T024503Z-cycle3-stage4-commodity-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T02:38:00Z
- Finished UTC: 2026-10-24T02:45:03Z
- Reviewer: antigravity / cmmmech-cycle3-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 36 commodity records in data/records/*.yaml at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e. All 36 commodity records carry clear commercial/metallurgical specification descriptions, dated criticality list provenance (26/36) or upstream critical-element relationships, and primary-source microbial mechanisms across 6/36 commodity records (with 4/36 carrying multi-step causal_graphs and live-verified UniProtKB protein_examples across 5 unique UniProtKB accessions: borates, phosphate-rock, rare-earth-element-commodities, and titanium-metal). Zero open findings.

## Scope And Provenance

Full-population Cycle 3 Stage 4 category review of all 36 traded chemical/metallurgical commodity records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'commodity' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
Coverage: full; 36 reviewed / 36 in the declared population.
Source: git_commit at Git base 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:alumina | data/records/alumina.yaml | maintained | Alumina |
| cmmmech:baryte | data/records/baryte.yaml | maintained | Baryte commodity |
| cmmmech:bauxite | data/records/bauxite.yaml | maintained | Bauxite |
| cmmmech:borates | data/records/borates.yaml | maintained | Borates |
| cmmmech:coking-coal | data/records/coking-coal.yaml | maintained | Coking coal |
| cmmmech:electrical-steel | data/records/electrical-steel.yaml | maintained | Electrical steel |
| cmmmech:electrolytic-manganese-dioxide | data/records/electrolytic-manganese-dioxide.yaml | maintained | Electrolytic manganese dioxide commodity |
| cmmmech:electrolytic-manganese-metal | data/records/electrolytic-manganese-metal.yaml | maintained | Electrolytic manganese metal commodity |
| cmmmech:feldspar | data/records/feldspar.yaml | maintained | Feldspar commodity |
| cmmmech:ferroboron | data/records/ferroboron.yaml | maintained | Ferroboron commodity |
| cmmmech:fluorspar | data/records/fluorspar.yaml | maintained | Fluorspar |
| cmmmech:graphite | data/records/graphite.yaml | maintained | Graphite commodity family |
| cmmmech:graphite-anode-material | data/records/graphite-anode-material.yaml | maintained | Graphite anode material for lithium-ion batteries |
| cmmmech:heavy-rare-earth-elements | data/records/heavy-rare-earth-elements.yaml | maintained | Heavy rare-earth commodities, EU assessment convention |
| cmmmech:high-purity-alumina | data/records/high-purity-alumina.yaml | maintained | High-purity alumina |
| cmmmech:high-purity-iron-ore | data/records/high-purity-iron-ore.yaml | maintained | High-purity iron ore |
| cmmmech:light-rare-earth-elements | data/records/light-rare-earth-elements.yaml | maintained | Light rare-earth commodities, EU assessment convention |
| cmmmech:lithium-carbonate | data/records/lithium-carbonate.yaml | maintained | Lithium carbonate commodity |
| cmmmech:lithium-hydroxide-monohydrate | data/records/lithium-hydroxide-monohydrate.yaml | maintained | Lithium hydroxide monohydrate commodity |
| cmmmech:magnesite | data/records/magnesite.yaml | maintained | Magnesite commodity |
| cmmmech:magnesium-metal | data/records/magnesium-metal.yaml | maintained | Magnesium metal |
| cmmmech:manganese-sulfate-monohydrate | data/records/manganese-sulfate-monohydrate.yaml | maintained | Manganese sulfate monohydrate commodity |
| cmmmech:metallurgical-coal | data/records/metallurgical-coal.yaml | maintained | Metallurgical coal commodity family |
| cmmmech:natural-graphite | data/records/natural-graphite.yaml | maintained | Natural graphite |
| cmmmech:nickel-sulfate-hexahydrate | data/records/nickel-sulfate-hexahydrate.yaml | maintained | Nickel sulfate hexahydrate commodity |
| cmmmech:phosphate-rock | data/records/phosphate-rock.yaml | maintained | Phosphate rock |
| cmmmech:platinum-group-commodities | data/records/platinum-group-commodities.yaml | maintained | Platinum-group commodities |
| cmmmech:potash | data/records/potash.yaml | maintained | Potash |
| cmmmech:rare-earth-element-commodities | data/records/rare-earth-element-commodities.yaml | maintained | Rare-earth-element commodities, Australian list scope |
| cmmmech:rare-earth-permanent-magnet-materials | data/records/rare-earth-permanent-magnet-materials.yaml | maintained | Rare-earth materials for permanent magnets, EU list scope |
| cmmmech:silicon-carbide | data/records/silicon-carbide.yaml | maintained | Silicon carbide |
| cmmmech:silicon-metal | data/records/silicon-metal.yaml | maintained | Silicon metal |
| cmmmech:sodium-compounds | data/records/sodium-compounds.yaml | maintained | Sodium compounds |
| cmmmech:synthetic-graphite | data/records/synthetic-graphite.yaml | maintained | Synthetic graphite |
| cmmmech:tin-copper-solder | data/records/tin-copper-solder.yaml | maintained | Tin-copper solder |
| cmmmech:titanium-metal | data/records/titanium-metal.yaml | maintained | Titanium metal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate (commodity cohort) | passed | True | cmmmech:alumina, cmmmech:baryte, cmmmech:bauxite, cmmmech:borates, cmmmech:coking-coal, cmmmech:electrical-steel, cmmmech:electrolytic-manganese-dioxide, cmmmech:electrolytic-manganese-metal, cmmmech:feldspar, cmmmech:ferroboron, cmmmech:fluorspar, cmmmech:graphite, cmmmech:graphite-anode-material, cmmmech:heavy-rare-earth-elements, cmmmech:high-purity-alumina, cmmmech:high-purity-iron-ore, cmmmech:light-rare-earth-elements, cmmmech:lithium-carbonate, cmmmech:lithium-hydroxide-monohydrate, cmmmech:magnesite, cmmmech:magnesium-metal, cmmmech:manganese-sulfate-monohydrate, cmmmech:metallurgical-coal, cmmmech:natural-graphite, cmmmech:nickel-sulfate-hexahydrate, cmmmech:phosphate-rock, cmmmech:platinum-group-commodities, cmmmech:potash, cmmmech:rare-earth-element-commodities, cmmmech:rare-earth-permanent-magnet-materials, cmmmech:silicon-carbide, cmmmech:silicon-metal, cmmmech:sodium-compounds, cmmmech:synthetic-graphite, cmmmech:tin-copper-solder, cmmmech:titanium-metal | All 36 records in the commodity cohort pass LinkML structural and semantic validation with 0 errors. |
| cmmmech validate-history (commodity cohort) | passed | True | cmmmech:alumina, cmmmech:baryte, cmmmech:bauxite, cmmmech:borates, cmmmech:coking-coal, cmmmech:electrical-steel, cmmmech:electrolytic-manganese-dioxide, cmmmech:electrolytic-manganese-metal, cmmmech:feldspar, cmmmech:ferroboron, cmmmech:fluorspar, cmmmech:graphite, cmmmech:graphite-anode-material, cmmmech:heavy-rare-earth-elements, cmmmech:high-purity-alumina, cmmmech:high-purity-iron-ore, cmmmech:light-rare-earth-elements, cmmmech:lithium-carbonate, cmmmech:lithium-hydroxide-monohydrate, cmmmech:magnesite, cmmmech:magnesium-metal, cmmmech:manganese-sulfate-monohydrate, cmmmech:metallurgical-coal, cmmmech:natural-graphite, cmmmech:nickel-sulfate-hexahydrate, cmmmech:phosphate-rock, cmmmech:platinum-group-commodities, cmmmech:potash, cmmmech:rare-earth-element-commodities, cmmmech:rare-earth-permanent-magnet-materials, cmmmech:silicon-carbide, cmmmech:silicon-metal, cmmmech:sodium-compounds, cmmmech:synthetic-graphite, cmmmech:tin-copper-solder, cmmmech:titanium-metal | All curation_history entries and history_refs sidecars across the 36 commodity records resolve and validate cleanly. |
| Ontology ID-label consistency (commodity cohort) | passed | True | cmmmech:alumina, cmmmech:baryte, cmmmech:bauxite, cmmmech:borates, cmmmech:coking-coal, cmmmech:electrical-steel, cmmmech:electrolytic-manganese-dioxide, cmmmech:electrolytic-manganese-metal, cmmmech:feldspar, cmmmech:ferroboron, cmmmech:fluorspar, cmmmech:graphite, cmmmech:graphite-anode-material, cmmmech:heavy-rare-earth-elements, cmmmech:high-purity-alumina, cmmmech:high-purity-iron-ore, cmmmech:light-rare-earth-elements, cmmmech:lithium-carbonate, cmmmech:lithium-hydroxide-monohydrate, cmmmech:magnesite, cmmmech:magnesium-metal, cmmmech:manganese-sulfate-monohydrate, cmmmech:metallurgical-coal, cmmmech:natural-graphite, cmmmech:nickel-sulfate-hexahydrate, cmmmech:phosphate-rock, cmmmech:platinum-group-commodities, cmmmech:potash, cmmmech:rare-earth-element-commodities, cmmmech:rare-earth-permanent-magnet-materials, cmmmech:silicon-carbide, cmmmech:silicon-metal, cmmmech:sodium-compounds, cmmmech:synthetic-graphite, cmmmech:tin-copper-solder, cmmmech:titanium-metal | Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 36 commodity records carries a consistent canonical label with 0 cross-corpus conflicts. |

## Scientific And Domain Assessments

### Commodity specification identity, criticality provenance, and microbial mechanisms

identity: supported. Targets: cmmmech:alumina, cmmmech:baryte, cmmmech:bauxite, cmmmech:borates, cmmmech:coking-coal, cmmmech:electrical-steel, cmmmech:electrolytic-manganese-dioxide, cmmmech:electrolytic-manganese-metal, cmmmech:feldspar, cmmmech:ferroboron, cmmmech:fluorspar, cmmmech:graphite, cmmmech:graphite-anode-material, cmmmech:heavy-rare-earth-elements, cmmmech:high-purity-alumina, cmmmech:high-purity-iron-ore, cmmmech:light-rare-earth-elements, cmmmech:lithium-carbonate, cmmmech:lithium-hydroxide-monohydrate, cmmmech:magnesite, cmmmech:magnesium-metal, cmmmech:manganese-sulfate-monohydrate, cmmmech:metallurgical-coal, cmmmech:natural-graphite, cmmmech:nickel-sulfate-hexahydrate, cmmmech:phosphate-rock, cmmmech:platinum-group-commodities, cmmmech:potash, cmmmech:rare-earth-element-commodities, cmmmech:rare-earth-permanent-magnet-materials, cmmmech:silicon-carbide, cmmmech:silicon-metal, cmmmech:sodium-compounds, cmmmech:synthetic-graphite, cmmmech:tin-copper-solder, cmmmech:titanium-metal.

All 36 commodity records accurately distinguish refined or industrial chemical commodities from natural minerals and chemical elements, with 6/36 carrying primary-source microbial mechanisms and 4/36 carrying grounded causal_graphs.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:alumina, cmmmech:baryte, cmmmech:bauxite, cmmmech:borates, cmmmech:coking-coal, cmmmech:electrical-steel, cmmmech:electrolytic-manganese-dioxide, cmmmech:electrolytic-manganese-metal, cmmmech:feldspar, cmmmech:ferroboron, cmmmech:fluorspar, cmmmech:graphite, cmmmech:graphite-anode-material, cmmmech:heavy-rare-earth-elements, cmmmech:high-purity-alumina, cmmmech:high-purity-iron-ore, cmmmech:light-rare-earth-elements, cmmmech:lithium-carbonate, cmmmech:lithium-hydroxide-monohydrate, cmmmech:magnesite, cmmmech:magnesium-metal, cmmmech:manganese-sulfate-monohydrate, cmmmech:metallurgical-coal, cmmmech:natural-graphite, cmmmech:nickel-sulfate-hexahydrate, cmmmech:phosphate-rock, cmmmech:platinum-group-commodities, cmmmech:potash, cmmmech:rare-earth-element-commodities, cmmmech:rare-earth-permanent-magnet-materials, cmmmech:silicon-carbide, cmmmech:silicon-metal, cmmmech:sodium-compounds, cmmmech:synthetic-graphite, cmmmech:tin-copper-solder, cmmmech:titanium-metal. All 36 records in the commodity cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'commodity' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cmmmech-validate | src/cmmmech/validation.py; cmmmech validate --require-records | supports | LinkML structural and semantic validator passed across all 646 records (including the commodity cohort) with 0 errors. |
| ev-cmmmech-history | src/cmmmech/history.py; cmmmech validate-history --base main | supports | All 962 curation history sidecars in history/records/ and record history_refs passed validation with 0 errors. |
| ev-cohort-audit | src/cmmmech/schema/cmmmech.yaml; Cycle 3 Stage 4 full-inventory cohort audit (commodity) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e | supports | Full-inventory inspection of all records in the commodity cohort verified distinct material identities, source-backed criticality/mechanism claims, and 100% CURIE label consistency across 181 distinct ontology terms. |

## Limits And Additional Notes

- 30 of 36 commodity records represent refined industrial metals, alloys, or chemical products (e.g., battery-grade lithium carbonate, ferro-alloys, electrical steel, silicon carbide) listed on government criticality schedules for which no direct microbial processing study is reported.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T024503Z-cycle3-stage4-commodity-cohort-review
title: 'Cycle 3 Stage 4 full-cohort review: commodity records (36/36)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-24T02:38:00Z'
finished_at: '2026-10-24T02:45:03Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 36 commodity records in data/records/*.yaml at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
  All 36 commodity records carry clear commercial/metallurgical specification descriptions,
  dated criticality list provenance (26/36) or upstream critical-element relationships,
  and primary-source microbial mechanisms across 6/36 commodity records (with 4/36
  carrying multi-step causal_graphs and live-verified UniProtKB protein_examples across
  5 unique UniProtKB accessions: borates, phosphate-rock, rare-earth-element-commodities,
  and titanium-metal). Zero open findings.'
reviewer:
  identity: antigravity / cmmmech-cycle3-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 3 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
source:
  git_revision: 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  state: git_commit
  inputs:
  - path: data/records/alumina.yaml
    sha256: 491bc7dee86b538d037f8d230167cc4c351aeb98e302202b4556b6a0cdae565c
    role: target
  - path: data/records/baryte.yaml
    sha256: 5b4a2dbff08a7a96b66dcaea5445be8d734ac57b3c1933fcf72cfb5687c67267
    role: target
  - path: data/records/bauxite.yaml
    sha256: b3c9fba4b8c46b4ac803dfa076887d49743b0e433804c54f3161788dcd887f7d
    role: target
  - path: data/records/borates.yaml
    sha256: de224b4334408815751fbddd6892962bcae6eb4bffe628b485bd14780e59801f
    role: target
  - path: data/records/coking-coal.yaml
    sha256: c6a10946b8617678052512de77c670f6648caa34b11186e056d92312ddccb2a2
    role: target
  - path: data/records/electrical-steel.yaml
    sha256: 59da8ecf893962b414662cbb51092fc68dfd0f6bb18b09a74cad475ae00930b1
    role: target
  - path: data/records/electrolytic-manganese-dioxide.yaml
    sha256: 83512a974c0dba9ec59a2cb7f26503bfe509c6816b8cc0f37ab1fa24b8700ccd
    role: target
  - path: data/records/electrolytic-manganese-metal.yaml
    sha256: 93983902a44daf4ec939bc6603ff6761a3b8954500c2903b40f5983577ab151e
    role: target
  - path: data/records/feldspar.yaml
    sha256: c6ef53daac9fe05dd09d9e2cf7b8a4883814f2978117b73289ac0946c5134310
    role: target
  - path: data/records/ferroboron.yaml
    sha256: 3b9d4fa94eee8f3f6b443e7d73af93d2dafaa58e7e2f1b58621c6afb1611df0d
    role: target
  - path: data/records/fluorspar.yaml
    sha256: e052269eef1c135d11266973169d6ea4a52832b9f8202a532828c1eb4b3e086a
    role: target
  - path: data/records/graphite-anode-material.yaml
    sha256: 608c23661e1f2b5cbffef9cd391b9c7ecc36d20815533f8dcb34c2b17b4afe1b
    role: target
  - path: data/records/graphite.yaml
    sha256: a31f18565b3b15c366d1587b88f1f70f047f865bf73591a3bd618a05d37f9a80
    role: target
  - path: data/records/heavy-rare-earth-elements.yaml
    sha256: 075322b154c9b1b904b08944f4f65221cd8970d6fbbd0410c313805dd8ef72b1
    role: target
  - path: data/records/high-purity-alumina.yaml
    sha256: 236a531d0c33808e429b9d26b90f5e86802dbbbd2af42e558500a510d0005501
    role: target
  - path: data/records/high-purity-iron-ore.yaml
    sha256: 3d9cacdea15ce942e4d2f341544e4bbb1621ca71e62c2bb9bafb05e6f00ff77b
    role: target
  - path: data/records/light-rare-earth-elements.yaml
    sha256: 97462d0c3c0066cfb4ff2cca4c22382e094834d7b0a35ef7e9c3091b4b90f735
    role: target
  - path: data/records/lithium-carbonate.yaml
    sha256: 78c7773d6bf0764a6bbb51bf4fa50f6468638ba1312d5f93ba324d6c6b99c2f5
    role: target
  - path: data/records/lithium-hydroxide-monohydrate.yaml
    sha256: 682207c7f5d201d066b3a79c7d64c49360f867500c9ce4ca162f1a236acd1c49
    role: target
  - path: data/records/magnesite.yaml
    sha256: 73cbffddbc86a7f01fe4090a29ed6907c057343cf3acfa4d4acc840c2304520b
    role: target
  - path: data/records/magnesium-metal.yaml
    sha256: c7da69e741115329d4a5e260d19929767ab0af11e38c497f92d737b358b4fe45
    role: target
  - path: data/records/manganese-sulfate-monohydrate.yaml
    sha256: 22a095812cd5f0add14f5c2007f47defd68ea263334690ecc946784da3e9f2dc
    role: target
  - path: data/records/metallurgical-coal.yaml
    sha256: 0e29f90b88c69ece7febeccc3ad8c58d4336b4e6457610633bac25a3365b8f2a
    role: target
  - path: data/records/natural-graphite.yaml
    sha256: e6d403add676fb3ae70b64fffcd698328165f4a98a0500442daa851f8c6828b8
    role: target
  - path: data/records/nickel-sulfate-hexahydrate.yaml
    sha256: 468df9c5da237f38f0263ce32bb06275e7572999d73387a96456d9892a053c9d
    role: target
  - path: data/records/phosphate-rock.yaml
    sha256: a20bd2ef094165632904b57d4592bec51b3ab27960605e3eeb030b31462c74f8
    role: target
  - path: data/records/platinum-group-commodities.yaml
    sha256: c66ea35815e9f41eaeeaae450ee3af000ef463b706c5e9f7290e958e699b03d9
    role: target
  - path: data/records/potash.yaml
    sha256: 9aa88b6823e0a38c7be9ac6798c401d7f36d2e28ed6f47fad2dbc54472f7e6a2
    role: target
  - path: data/records/rare-earth-element-commodities.yaml
    sha256: 08b78b26fcfe9b718385dee29be591eea523da30ae82e522e16c011f7795302b
    role: target
  - path: data/records/rare-earth-permanent-magnet-materials.yaml
    sha256: 56c2b6ec0eff5dadad9a21d14a74c74c9f52ea370d74a62942fa1c87457126c6
    role: target
  - path: data/records/silicon-carbide.yaml
    sha256: ed7f62903970accb41ced35e0af8afd2066cbafb6d5af367be75cdabfd4dfb4c
    role: target
  - path: data/records/silicon-metal.yaml
    sha256: dcb0c82db6b3d98b5585b4d740ac10ed5cf2711467ebafadf76d85f7f2e87ced
    role: target
  - path: data/records/sodium-compounds.yaml
    sha256: 1d662bdbd0dd2b4759cb5189a34374dbba032d62dd4bf6464827200a1c43653e
    role: target
  - path: data/records/synthetic-graphite.yaml
    sha256: 3fa93145c452cfbf4bd1a027668d4c51a63a20adb1daaacc0dbad4262e5999b1
    role: target
  - path: data/records/tin-copper-solder.yaml
    sha256: 017b16672161b117c2ab07300342e3f1ba861036f10c2dfad8d994a7419f8c8b
    role: target
  - path: data/records/titanium-metal.yaml
    sha256: 547e4023b359003f82e8178f6adfee0db4424043e9591e268531876a65552622
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 36
  reviewed_target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  selection: data/records/*.yaml where material_kind == 'commodity' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  description: Full-population Cycle 3 Stage 4 category review of all 36 traded chemical/metallurgical
    commodity records in CMMMech.
targets:
- target_id: cmmmech:alumina
  path: data/records/alumina.yaml
  kind: maintained
  label: Alumina
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alumina.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:baryte
  path: data/records/baryte.yaml
  kind: maintained
  label: Baryte commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baryte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bauxite
  path: data/records/bauxite.yaml
  kind: maintained
  label: Bauxite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bauxite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:borates
  path: data/records/borates.yaml
  kind: maintained
  label: Borates
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/borates.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coking-coal
  path: data/records/coking-coal.yaml
  kind: maintained
  label: Coking coal
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coking-coal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:electrical-steel
  path: data/records/electrical-steel.yaml
  kind: maintained
  label: Electrical steel
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrical-steel.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:electrolytic-manganese-dioxide
  path: data/records/electrolytic-manganese-dioxide.yaml
  kind: maintained
  label: Electrolytic manganese dioxide commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrolytic-manganese-dioxide.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:electrolytic-manganese-metal
  path: data/records/electrolytic-manganese-metal.yaml
  kind: maintained
  label: Electrolytic manganese metal commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrolytic-manganese-metal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:feldspar
  path: data/records/feldspar.yaml
  kind: maintained
  label: Feldspar commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feldspar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferroboron
  path: data/records/ferroboron.yaml
  kind: maintained
  label: Ferroboron commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferroboron.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorspar
  path: data/records/fluorspar.yaml
  kind: maintained
  label: Fluorspar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorspar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:graphite
  path: data/records/graphite.yaml
  kind: maintained
  label: Graphite commodity family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/graphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:graphite-anode-material
  path: data/records/graphite-anode-material.yaml
  kind: maintained
  label: Graphite anode material for lithium-ion batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/graphite-anode-material.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:heavy-rare-earth-elements
  path: data/records/heavy-rare-earth-elements.yaml
  kind: maintained
  label: Heavy rare-earth commodities, EU assessment convention
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heavy-rare-earth-elements.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:high-purity-alumina
  path: data/records/high-purity-alumina.yaml
  kind: maintained
  label: High-purity alumina
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/high-purity-alumina.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:high-purity-iron-ore
  path: data/records/high-purity-iron-ore.yaml
  kind: maintained
  label: High-purity iron ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/high-purity-iron-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:light-rare-earth-elements
  path: data/records/light-rare-earth-elements.yaml
  kind: maintained
  label: Light rare-earth commodities, EU assessment convention
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/light-rare-earth-elements.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithium-carbonate
  path: data/records/lithium-carbonate.yaml
  kind: maintained
  label: Lithium carbonate commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium-carbonate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithium-hydroxide-monohydrate
  path: data/records/lithium-hydroxide-monohydrate.yaml
  kind: maintained
  label: Lithium hydroxide monohydrate commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium-hydroxide-monohydrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:magnesite
  path: data/records/magnesite.yaml
  kind: maintained
  label: Magnesite commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:magnesium-metal
  path: data/records/magnesium-metal.yaml
  kind: maintained
  label: Magnesium metal
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesium-metal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:manganese-sulfate-monohydrate
  path: data/records/manganese-sulfate-monohydrate.yaml
  kind: maintained
  label: Manganese sulfate monohydrate commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese-sulfate-monohydrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metallurgical-coal
  path: data/records/metallurgical-coal.yaml
  kind: maintained
  label: Metallurgical coal commodity family
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metallurgical-coal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:natural-graphite
  path: data/records/natural-graphite.yaml
  kind: maintained
  label: Natural graphite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/natural-graphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nickel-sulfate-hexahydrate
  path: data/records/nickel-sulfate-hexahydrate.yaml
  kind: maintained
  label: Nickel sulfate hexahydrate commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-sulfate-hexahydrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phosphate-rock
  path: data/records/phosphate-rock.yaml
  kind: maintained
  label: Phosphate rock
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-rock.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:platinum-group-commodities
  path: data/records/platinum-group-commodities.yaml
  kind: maintained
  label: Platinum-group commodities
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/platinum-group-commodities.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:potash
  path: data/records/potash.yaml
  kind: maintained
  label: Potash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/potash.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rare-earth-element-commodities
  path: data/records/rare-earth-element-commodities.yaml
  kind: maintained
  label: Rare-earth-element commodities, Australian list scope
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-element-commodities.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rare-earth-permanent-magnet-materials
  path: data/records/rare-earth-permanent-magnet-materials.yaml
  kind: maintained
  label: Rare-earth materials for permanent magnets, EU list scope
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-permanent-magnet-materials.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:silicon-carbide
  path: data/records/silicon-carbide.yaml
  kind: maintained
  label: Silicon carbide
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon-carbide.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:silicon-metal
  path: data/records/silicon-metal.yaml
  kind: maintained
  label: Silicon metal
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon-metal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sodium-compounds
  path: data/records/sodium-compounds.yaml
  kind: maintained
  label: Sodium compounds
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sodium-compounds.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:synthetic-graphite
  path: data/records/synthetic-graphite.yaml
  kind: maintained
  label: Synthetic graphite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/synthetic-graphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tin-copper-solder
  path: data/records/tin-copper-solder.yaml
  kind: maintained
  label: Tin-copper solder
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tin-copper-solder.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:titanium-metal
  path: data/records/titanium-metal.yaml
  kind: maintained
  label: Titanium metal
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanium-metal.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-cohort
  name: cmmmech validate (commodity cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  evidence_ids:
  - ev-cmmmech-validate
  summary: All 36 records in the commodity cohort pass LinkML structural and semantic
    validation with 0 errors.
- check_id: cmmmech-validate-history-cohort
  name: cmmmech validate-history (commodity cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  evidence_ids:
  - ev-cmmmech-history
  summary: All curation_history entries and history_refs sidecars across the 36 commodity
    records resolve and validate cleanly.
- check_id: curie-label-consistency-cohort
  name: Ontology ID-label consistency (commodity cohort)
  status: passed
  required: true
  target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  evidence_ids:
  - ev-cohort-audit
  summary: Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 36
    commodity records carries a consistent canonical label with 0 cross-corpus conflicts.
assessments:
- assessment_id: assess-commodity-cohort
  topic: Commodity specification identity, criticality provenance, and microbial mechanisms
  area: identity
  outcome: supported
  target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  evidence_ids:
  - ev-cmmmech-validate
  - ev-cmmmech-history
  - ev-cohort-audit
  summary: All 36 commodity records accurately distinguish refined or industrial chemical
    commodities from natural minerals and chemical elements, with 6/36 carrying primary-source
    microbial mechanisms and 4/36 carrying grounded causal_graphs.
  metrics:
  - name: reviewed_commodities
    value: 36.0
    unit: records
    definition: Total commodity records reviewed in the cohort.
    minimum: 0.0
    maximum: 36.0
  - name: commodities_with_mechanisms
    value: 6.0
    unit: records
    definition: Commodity records carrying primary-source microbial mechanisms.
    minimum: 0.0
    maximum: 36.0
  - name: commodities_with_causal_graphs
    value: 4.0
    unit: records
    definition: Commodity records carrying multi-step causal_graphs and UniProtKB
      protein_examples.
    minimum: 0.0
    maximum: 36.0
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:alumina
  - cmmmech:baryte
  - cmmmech:bauxite
  - cmmmech:borates
  - cmmmech:coking-coal
  - cmmmech:electrical-steel
  - cmmmech:electrolytic-manganese-dioxide
  - cmmmech:electrolytic-manganese-metal
  - cmmmech:feldspar
  - cmmmech:ferroboron
  - cmmmech:fluorspar
  - cmmmech:graphite
  - cmmmech:graphite-anode-material
  - cmmmech:heavy-rare-earth-elements
  - cmmmech:high-purity-alumina
  - cmmmech:high-purity-iron-ore
  - cmmmech:light-rare-earth-elements
  - cmmmech:lithium-carbonate
  - cmmmech:lithium-hydroxide-monohydrate
  - cmmmech:magnesite
  - cmmmech:magnesium-metal
  - cmmmech:manganese-sulfate-monohydrate
  - cmmmech:metallurgical-coal
  - cmmmech:natural-graphite
  - cmmmech:nickel-sulfate-hexahydrate
  - cmmmech:phosphate-rock
  - cmmmech:platinum-group-commodities
  - cmmmech:potash
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rare-earth-permanent-magnet-materials
  - cmmmech:silicon-carbide
  - cmmmech:silicon-metal
  - cmmmech:sodium-compounds
  - cmmmech:synthetic-graphite
  - cmmmech:tin-copper-solder
  - cmmmech:titanium-metal
  rationale: All 36 records in the commodity cohort denote distinct, non-synonymous
    entities matching data/records/*.yaml where material_kind == 'commodity' at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-cohort-audit
evidence:
- evidence_id: ev-cmmmech-validate
  kind: validation
  reference: src/cmmmech/validation.py
  locator: cmmmech validate --require-records
  accessed_at: '2026-10-24T02:45:03Z'
  support: supports
  summary: LinkML structural and semantic validator passed across all 646 records
    (including the commodity cohort) with 0 errors.
- evidence_id: ev-cmmmech-history
  kind: validation
  reference: src/cmmmech/history.py
  locator: cmmmech validate-history --base main
  accessed_at: '2026-10-24T02:45:03Z'
  support: supports
  summary: All 962 curation history sidecars in history/records/ and record history_refs
    passed validation with 0 errors.
- evidence_id: ev-cohort-audit
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Cycle 3 Stage 4 full-inventory cohort audit (commodity) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  accessed_at: '2026-10-24T02:45:03Z'
  support: supports
  summary: Full-inventory inspection of all records in the commodity cohort verified
    distinct material identities, source-backed criticality/mechanism claims, and
    100% CURIE label consistency across 181 distinct ontology terms.
limitations:
- 30 of 36 commodity records represent refined industrial metals, alloys, or chemical
  products (e.g., battery-grade lithium carbonate, ferro-alloys, electrical steel,
  silicon carbide) listed on government criticality schedules for which no direct
  microbial processing study is reported.
notes: []
```
