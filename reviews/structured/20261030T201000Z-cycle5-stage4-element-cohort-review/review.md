# Cycle 5 Stage 4 full-cohort review: element records (66/66)

- Review: 20261030T201000Z-cycle5-stage4-element-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T20:03:00Z
- Finished UTC: 2026-10-30T20:10:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 66 element records in data/records/*.yaml at commit 208134600496b954831b125033d33caa508dba8b, including the 4 element records synchronized in Cycle 5 Stage 2 (cerium, lanthanum, neodymium, zinc) and the Cycle 5 Stage 3 Sqr paralog grounding expansion on zinc (UniProtKB:B7J411 and UniProtKB:A0A543Q349). Every element record carries a verified CHEBI atom identifier, dated government/intergovernmental criticality assessments (USGS, DOE, EU, and allied lists), and primary-source-backed microbial mechanisms across 63/66 element records (66 mechanisms total), including 24/66 with multi-step causal_graphs (25 graphs) and 23/66 with live-verified UniProtKB protein_examples (33 unique accessions). Identified 1 minor convention finding (cmmmech-cycle5-stage4-finding-0001: criticality serialized before sources in 9 element records: chromium, hafnium, manganese, praseodymium, scandium, selenium, silicon, uranium, vanadium) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 5 Stage 4 category review of all 66 chemical element records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'element' at 208134600496b954831b125033d33caa508dba8b
Coverage: full; 66 reviewed / 66 in the declared population.
Source: git_commit at Git base 208134600496b954831b125033d33caa508dba8b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:aluminium | data/records/aluminium.yaml | maintained | Aluminium |
| cmmmech:antimony | data/records/antimony.yaml | maintained | Antimony |
| cmmmech:arsenic | data/records/arsenic.yaml | maintained | Arsenic |
| cmmmech:beryllium | data/records/beryllium.yaml | maintained | Beryllium |
| cmmmech:bismuth | data/records/bismuth.yaml | maintained | Bismuth |
| cmmmech:boron | data/records/boron.yaml | maintained | Boron |
| cmmmech:cadmium | data/records/cadmium.yaml | maintained | Cadmium |
| cmmmech:cerium | data/records/cerium.yaml | maintained | Cerium |
| cmmmech:cesium | data/records/cesium.yaml | maintained | Cesium |
| cmmmech:chromium | data/records/chromium.yaml | maintained | Chromium |
| cmmmech:cobalt | data/records/cobalt.yaml | maintained | Cobalt |
| cmmmech:copper | data/records/copper.yaml | maintained | Copper |
| cmmmech:dysprosium | data/records/dysprosium.yaml | maintained | Dysprosium |
| cmmmech:erbium | data/records/erbium.yaml | maintained | Erbium |
| cmmmech:europium | data/records/europium.yaml | maintained | Europium |
| cmmmech:fluorine | data/records/fluorine.yaml | maintained | Fluorine |
| cmmmech:gadolinium | data/records/gadolinium.yaml | maintained | Gadolinium |
| cmmmech:gallium | data/records/gallium.yaml | maintained | Gallium |
| cmmmech:germanium | data/records/germanium.yaml | maintained | Germanium |
| cmmmech:gold | data/records/gold.yaml | maintained | Gold |
| cmmmech:hafnium | data/records/hafnium.yaml | maintained | Hafnium |
| cmmmech:helium | data/records/helium.yaml | maintained | Helium |
| cmmmech:holmium | data/records/holmium.yaml | maintained | Holmium |
| cmmmech:indium | data/records/indium.yaml | maintained | Indium |
| cmmmech:iridium | data/records/iridium.yaml | maintained | Iridium |
| cmmmech:iron | data/records/iron.yaml | maintained | Iron |
| cmmmech:lanthanum | data/records/lanthanum.yaml | maintained | Lanthanum |
| cmmmech:lead | data/records/lead.yaml | maintained | Lead |
| cmmmech:lithium | data/records/lithium.yaml | maintained | Lithium |
| cmmmech:lutetium | data/records/lutetium.yaml | maintained | Lutetium |
| cmmmech:magnesium | data/records/magnesium.yaml | maintained | Magnesium |
| cmmmech:manganese | data/records/manganese.yaml | maintained | Manganese |
| cmmmech:molybdenum | data/records/molybdenum.yaml | maintained | Molybdenum |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |
| cmmmech:nickel | data/records/nickel.yaml | maintained | Nickel |
| cmmmech:niobium | data/records/niobium.yaml | maintained | Niobium |
| cmmmech:osmium | data/records/osmium.yaml | maintained | Osmium |
| cmmmech:palladium | data/records/palladium.yaml | maintained | Palladium |
| cmmmech:phosphorus | data/records/phosphorus.yaml | maintained | Phosphorus |
| cmmmech:platinum | data/records/platinum.yaml | maintained | Platinum |
| cmmmech:praseodymium | data/records/praseodymium.yaml | maintained | Praseodymium |
| cmmmech:promethium | data/records/promethium.yaml | maintained | Promethium |
| cmmmech:rhenium | data/records/rhenium.yaml | maintained | Rhenium |
| cmmmech:rhodium | data/records/rhodium.yaml | maintained | Rhodium |
| cmmmech:rubidium | data/records/rubidium.yaml | maintained | Rubidium |
| cmmmech:ruthenium | data/records/ruthenium.yaml | maintained | Ruthenium |
| cmmmech:samarium | data/records/samarium.yaml | maintained | Samarium |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |
| cmmmech:silicon | data/records/silicon.yaml | maintained | Silicon |
| cmmmech:silver | data/records/silver.yaml | maintained | Silver |
| cmmmech:strontium | data/records/strontium.yaml | maintained | Strontium |
| cmmmech:tantalum | data/records/tantalum.yaml | maintained | Tantalum |
| cmmmech:tellurium | data/records/tellurium.yaml | maintained | Tellurium |
| cmmmech:terbium | data/records/terbium.yaml | maintained | Terbium |
| cmmmech:thallium | data/records/thallium.yaml | maintained | Thallium |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |
| cmmmech:tin | data/records/tin.yaml | maintained | Tin |
| cmmmech:titanium | data/records/titanium.yaml | maintained | Titanium |
| cmmmech:tungsten | data/records/tungsten.yaml | maintained | Tungsten |
| cmmmech:uranium | data/records/uranium.yaml | maintained | Uranium |
| cmmmech:vanadium | data/records/vanadium.yaml | maintained | Vanadium |
| cmmmech:ytterbium | data/records/ytterbium.yaml | maintained | Ytterbium |
| cmmmech:yttrium | data/records/yttrium.yaml | maintained | Yttrium |
| cmmmech:zinc | data/records/zinc.yaml | maintained | Zinc |
| cmmmech:zirconium | data/records/zirconium.yaml | maintained | Zirconium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate element cohort (66 records) | passed | True | cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium | All 66 records in cohort pass LinkML structural and semantic validation with 0 errors. |

## Scientific And Domain Assessments

### Element identity (CHEBI atom CURIEs) and jurisdiction-scoped criticality lists

identity: supported. Targets: cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium.

All 66 element records carry canonical CHEBI atom CURIEs and labels with 0 cross-corpus label conflicts and dated criticality lists.

### Microbial extraction/transformation/recovery mechanisms, causal graphs, and UniProtKB protein examples

evidence: supported. Targets: cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium.

63/66 element records contain primary-source-supported microbial mechanisms (66 mechanisms total); 24/66 contain causal_graphs (25 graphs), with 23/24 grounded to 33 unique UniProtKB accessions and 3 GENE_OR_PROTEIN nodes across cmmmech:iron (ax17_extracellular_fe3_reductase_system), cmmmech:manganese (mopa_heme_peroxidase), and cmmmech:praseodymium (melba_lanm_o36) explicitly marked UNGROUNDED where strain-resolved UniProtKB entries are absent. Nine element records serialize criticality before sources.

## Findings

### cmmmech-cycle5-stage4-finding-0001: Top-level YAML key order places criticality before sources instead of canonical CriticalMineralRecord / CANONICAL_RECORD_KEYS order

minor / open / confirmed; issue key: cmmmech.records.criticality-before-sources-key-order.

Across the 668-record corpus, 13 records (chromium.yaml, electrical-steel.yaml, hafnium.yaml, manganese.yaml, praseodymium.yaml, rare-earth-element-commodities.yaml, scandium.yaml, selenium.yaml, silicon-carbide.yaml, silicon.yaml, synthetic-graphite.yaml, uranium.yaml, vanadium.yaml) serialize top-level 'criticality' before 'sources', whereas CriticalMineralRecord in src/cmmmech/schema/cmmmech.yaml and CANONICAL_RECORD_KEYS in scripts/new_history.py place 'sources' before 'criticality'. In this cohort, 9 record(s) (chromium, hafnium, manganese, praseodymium, scandium, selenium, silicon, uranium, vanadium) exhibit this non-canonical key order.

## Recommended Actions And Acceptance Checks

### act-normalize-criticality-before-sources-key-order

Reorder top-level YAML keys so sources precedes criticality in Stage 5 grouped remediation and record canonical history sidecars.

- All affected records serialize sources before criticality in canonical CriticalMineralRecord / CANONICAL_RECORD_KEYS order.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium. All 66 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'element' at 208134600496b954831b125033d33caa508dba8b with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-element-cohort-audit | data/records/*.yaml (material_kind == 'element'); 66 element YAML files | supports | Full programmatic and source-backed audit of all 66 element records at commit 208134600496b954831b125033d33caa508dba8b. |

## Limits And Additional Notes

- Three element records currently lack curated microbial mechanism entries: cmmmech:beryllium, cmmmech:helium, and cmmmech:promethium are maintained criticality-anchored element records awaiting primary microbial extraction/transformation/recovery evidence. (63/66 element records have curated mechanisms; 3/66 remain identity and criticality records only.)
- Three GENE_OR_PROTEIN nodes in the element cohort remain explicitly UNGROUNDED due to absent strain-resolved sequences in UniProtKB: ax17_extracellular_fe3_reductase_system in cmmmech:iron (Desulfovulcanus ferrireducens Ax17), mopa_heme_peroxidase in cmmmech:manganese, and melba_lanm_o36 in cmmmech:praseodymium (23/24 element records with causal_graphs carry GROUNDED protein_examples; cmmmech:iron has only an UNGROUNDED node).
- Cohort covers 100% (66/66) of target records in data/records/*.yaml at commit 208134600496b954831b125033d33caa508dba8b.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T201000Z-cycle5-stage4-element-cohort-review
title: 'Cycle 5 Stage 4 full-cohort review: element records (66/66)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-30T20:03:00Z'
finished_at: '2026-10-30T20:10:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 66 element records in data/records/*.yaml at commit 208134600496b954831b125033d33caa508dba8b,
  including the 4 element records synchronized in Cycle 5 Stage 2 (cerium, lanthanum,
  neodymium, zinc) and the Cycle 5 Stage 3 Sqr paralog grounding expansion on zinc
  (UniProtKB:B7J411 and UniProtKB:A0A543Q349). Every element record carries a verified
  CHEBI atom identifier, dated government/intergovernmental criticality assessments
  (USGS, DOE, EU, and allied lists), and primary-source-backed microbial mechanisms
  across 63/66 element records (66 mechanisms total), including 24/66 with multi-step
  causal_graphs (25 graphs) and 23/66 with live-verified UniProtKB protein_examples
  (33 unique accessions). Identified 1 minor convention finding (cmmmech-cycle5-stage4-finding-0001:
  criticality serialized before sources in 9 element records: chromium, hafnium, manganese,
  praseodymium, scandium, selenium, silicon, uranium, vanadium) for Stage 5 grouped
  remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 5 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 208134600496b954831b125033d33caa508dba8b.
source:
  git_revision: 208134600496b954831b125033d33caa508dba8b
  state: git_commit
  inputs:
  - path: data/records/aluminium.yaml
    sha256: 8df6aa9f1e6f6b4fdb637c4026cfef6781c286c847e25153d0c126a67503fe13
    role: target
  - path: data/records/antimony.yaml
    sha256: 3854163557ef588e4d570f71e6939b406bef24763d31332afe0741400cd91576
    role: target
  - path: data/records/arsenic.yaml
    sha256: 06c768bddccc43174d06a95b33f01b0858ab1e52ea7d9eba73e5bbb6b2092a62
    role: target
  - path: data/records/beryllium.yaml
    sha256: 3c4490f5b7832808b5683a26d4b93e849647a52ef7d1468cd99c06a79a53aa71
    role: target
  - path: data/records/bismuth.yaml
    sha256: 1df7276c9545a4cc13a9a289e3aca1bb68da4794f59034c04a625cb1f86984ea
    role: target
  - path: data/records/boron.yaml
    sha256: b11782fc3d0f3783af0c4131448cdb38a68063c1fc66df9b956db01fcef8664a
    role: target
  - path: data/records/cadmium.yaml
    sha256: d28086a01df3288beb905cbea3fdc9ebdce8e7b7ae9da9a750e66712ca54d0de
    role: target
  - path: data/records/cerium.yaml
    sha256: 7837cfe3c8dd804673181a9472a069e90cbcb9cba4503c4ce8e485235da5f618
    role: target
  - path: data/records/cesium.yaml
    sha256: 09a7cf90913a87a0fe2ad0c2998e1ed1239c41c4a5b488be2a9db95733f8bf50
    role: target
  - path: data/records/chromium.yaml
    sha256: 1c5b610983ce5970bac085a5a3e32e6bee189acef13192113f6d1b46ff6c3a7f
    role: target
  - path: data/records/cobalt.yaml
    sha256: c37b06ec07bc1e4af7289dc770f3711658ea05a948e22c91b12f6b00130f7037
    role: target
  - path: data/records/copper.yaml
    sha256: 357e81e48e5a480359f485e380a26eecf8d5a125100f328d99b06c0dacaabbfc
    role: target
  - path: data/records/dysprosium.yaml
    sha256: 1a35259d03d043ad627d975c90a19d849141a9f8301167d5ca2eadf8efb42799
    role: target
  - path: data/records/erbium.yaml
    sha256: 9cb11ab193e89153b1fedac0a02a128e2427dae21cbde90c95ea0041b1d1744b
    role: target
  - path: data/records/europium.yaml
    sha256: 2a0e8347906dd98a6fb00147db7f24976cb4ed86df21b65f9e3f2b2dc855d869
    role: target
  - path: data/records/fluorine.yaml
    sha256: 4af0ed94ff108aeb0aac4eab20d104aeb4df731ead7816c7324444bed983a7c2
    role: target
  - path: data/records/gadolinium.yaml
    sha256: fc41a18c90fbcf5e3e28e897b69b726ed1ed3f8a860df239f466ca02e7034374
    role: target
  - path: data/records/gallium.yaml
    sha256: 6d6f89773be97e0af508d485b9270e9f4a7a7afb34de47590c43062d7ca0bf11
    role: target
  - path: data/records/germanium.yaml
    sha256: ab9184e4e7eed9507d67309937e872c7218a5b534acbb7e09eff8036a8e10c05
    role: target
  - path: data/records/gold.yaml
    sha256: 3041e16eaa6cdd500a1784cd9c2461511e0c98e37d218bc29abe56b3c4375bb4
    role: target
  - path: data/records/hafnium.yaml
    sha256: 94398fcf1ddafc2f294a16915b163a675e4bfa623beba10251cb21d293ded3a8
    role: target
  - path: data/records/helium.yaml
    sha256: a2ff0d6c70298786262cd5ceb276ba5c873fe77cf60790a8ceb7be2504371f4c
    role: target
  - path: data/records/holmium.yaml
    sha256: 1abce3e7b19f1f00868f0a1145ae4106c5f12e3b63f6a93246d26aab459a8c15
    role: target
  - path: data/records/indium.yaml
    sha256: 92414434d8f03130dcd8fc225659752c66f9b3b726f9c3598f1dcc2b4aa09aed
    role: target
  - path: data/records/iridium.yaml
    sha256: c77604f4962321302cd6f63ffff86d19463f4769893744c428155c1f6e9cf24c
    role: target
  - path: data/records/iron.yaml
    sha256: 92f6792df8c1b65d3377d91b9cf7817b42a4558cb0618e4db8f2f97382aad62d
    role: target
  - path: data/records/lanthanum.yaml
    sha256: eca2a756a20c63a497823a64fb51fd877f157f4f2c8b9b7479d0a1af925ab930
    role: target
  - path: data/records/lead.yaml
    sha256: f88ea8069eac92b1f21e0923d4c8ffd1ca9931ad7571e1bd20c482e7ce3cade1
    role: target
  - path: data/records/lithium.yaml
    sha256: c02c148a68ae6921e6dfeb5eed4d459212fb6496642a1d9808f6ab7de53405d9
    role: target
  - path: data/records/lutetium.yaml
    sha256: a7962fcca9cdea5dd0c538f7d0f4707439a5241cd49819e93750245bf9a69789
    role: target
  - path: data/records/magnesium.yaml
    sha256: ab57bc5464af299e10481a8a56f0f4161e6bc10cbac35852b82e63caf677ccc2
    role: target
  - path: data/records/manganese.yaml
    sha256: 4e14de8d0bd57869af70e6a8ce02da5c183afdef4715656c3c19c6ca86001749
    role: target
  - path: data/records/molybdenum.yaml
    sha256: 8b6b2790848a967492ed00d204d6f64835cd8ebd2a437a4753715f4e2567d39d
    role: target
  - path: data/records/neodymium.yaml
    sha256: 91a74a542eb1dbd45aeb4cbd24f3ced3f382854dc7e7e3d2292effcded89341f
    role: target
  - path: data/records/nickel.yaml
    sha256: b87ef9b7ab31d74980b5d6c57d7e74ba85a3d7860ca257cd30c0886c85aa47dc
    role: target
  - path: data/records/niobium.yaml
    sha256: 7ff7be01282e1e08c418d81e358ec4459c2890f735476dda52a4950e7f0fe159
    role: target
  - path: data/records/osmium.yaml
    sha256: db219a825da6866d42a86debeeb8c9f2e615ddf7f7a178fcec74f9b55ef0b622
    role: target
  - path: data/records/palladium.yaml
    sha256: 6924903baa0aceaa8361a94198b2d5b42460b34d4d643fa4ffdc6e43c50803c0
    role: target
  - path: data/records/phosphorus.yaml
    sha256: 35de80a71ff8621b74a9d30535f0711356ef4993b8eaf9e0eca5951c57c2edc7
    role: target
  - path: data/records/platinum.yaml
    sha256: 9e53cee8682c7ebaa2c3fe995ffc4c96a034f161a1f35f2be273756d1aed5260
    role: target
  - path: data/records/praseodymium.yaml
    sha256: e31325b8f4667ecb0533eca471c9398942cbcf020c90fa17f34e6a545f71d8d1
    role: target
  - path: data/records/promethium.yaml
    sha256: 147239c35cf5c9aa8d57342dd2c4014d35eddf92da0625cf5928250ad94a3948
    role: target
  - path: data/records/rhenium.yaml
    sha256: 59c1bacd1db51f21812d36386b2cbfd9c9b1bd72e0db247d27f1f4c5b69e66eb
    role: target
  - path: data/records/rhodium.yaml
    sha256: ad7fbf9a2c12d2b9ef411ee23e3ada5698cbb2e6a3ecead2513d881f8d460a18
    role: target
  - path: data/records/rubidium.yaml
    sha256: 62a20be29cbb1a2bd4c750a81fb68916283fbd8388400ceae2022f08b3888979
    role: target
  - path: data/records/ruthenium.yaml
    sha256: f9a164e5b56444aa80eec3a76868f3fe45ccdee8f3f25ed29e2c79dc28fc1fb1
    role: target
  - path: data/records/samarium.yaml
    sha256: 580b317ea1c31ef21c185f2e0c2b935a36de609adbba0a721ed2b756bba40a60
    role: target
  - path: data/records/scandium.yaml
    sha256: 276b76b9d7797f31d0a52c38e85a15568c6b5177a1625d7b39a0fb411308e4ac
    role: target
  - path: data/records/selenium.yaml
    sha256: 9547737220d516390041bd114783a25fd367f28189cc2351c03170aecc89b484
    role: target
  - path: data/records/silicon.yaml
    sha256: 1ccf550155f85ccbe83f3a1aa0895e16e61575fa2f43eeb3056476d9a4fa13e9
    role: target
  - path: data/records/silver.yaml
    sha256: 9e526e8db6b270c515116cb1e3f3adfa9800f1184cf5d5740575a1cf1ce4cfc0
    role: target
  - path: data/records/strontium.yaml
    sha256: d21d19f117baa3c2de01985b956e7bdc4b7a13d37552f7faa28ef626b939f28e
    role: target
  - path: data/records/tantalum.yaml
    sha256: 85c5bca4825c683ebbf4744bd899753c7dbd60808aaae47551645ab77a442383
    role: target
  - path: data/records/tellurium.yaml
    sha256: 8de03e4ddd334be7f6adf1813384529600bdbab2b9b0dec6f0f394fdbab81f38
    role: target
  - path: data/records/terbium.yaml
    sha256: c47181aa12c1c060c9e04e95c96c37552c4ec183032033dbf9f4500c71e40ffb
    role: target
  - path: data/records/thallium.yaml
    sha256: 84fb52f391fc30d3bbdb69815d4b01084c8a889b8d1c309bdb81136810221eef
    role: target
  - path: data/records/thulium.yaml
    sha256: 24456f05fb24d477fbea1aa1584f763bf61506fcdab6837713b105f020730a34
    role: target
  - path: data/records/tin.yaml
    sha256: 138bd40ed9bfb255a13f2f7d3b9997c7e919f34282893d16c18d0bcc3d7e4d19
    role: target
  - path: data/records/titanium.yaml
    sha256: 4705897961d928c731f7b5abda41660c46fdba14aebc9ada2d4738d61ba6413a
    role: target
  - path: data/records/tungsten.yaml
    sha256: d87ad7f8783feba23aace69512babacfd006e26190e49196d446b9b9c7bc40fa
    role: target
  - path: data/records/uranium.yaml
    sha256: f2bcc77e3e01adef0509ae4b5cdb26aee435dae30f2d93cf2ad322c8890c72a0
    role: target
  - path: data/records/vanadium.yaml
    sha256: 335a04a069081e6fb33988bda293f376f379549f2c0101f5f618385b1a2f1487
    role: target
  - path: data/records/ytterbium.yaml
    sha256: b29100506b873c5262a0d9e186c4442c0286bdb666a13b596a30c5c42910eb7e
    role: target
  - path: data/records/yttrium.yaml
    sha256: ad5b7c2e2696c9d96b5e2a48117c2591bd3c301ffba23ce16920331a020c5aa9
    role: target
  - path: data/records/zinc.yaml
    sha256: 169d45a59d2ca47b8f15c03cb7141f1adb445e5b6c6a33d404d15b825dc9ec00
    role: target
  - path: data/records/zirconium.yaml
    sha256: ce1b18c2da980483bdd5b24952de611f429d36b6309b940dd9411c77a095e097
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: d2a31e40b52cee60a86a2897db9b8274b1089c92dd043d83313b7d87e05c6635
    role: context
scope:
  coverage: full
  population_size: 66
  reviewed_target_ids:
  - cmmmech:aluminium
  - cmmmech:antimony
  - cmmmech:arsenic
  - cmmmech:beryllium
  - cmmmech:bismuth
  - cmmmech:boron
  - cmmmech:cadmium
  - cmmmech:cerium
  - cmmmech:cesium
  - cmmmech:chromium
  - cmmmech:cobalt
  - cmmmech:copper
  - cmmmech:dysprosium
  - cmmmech:erbium
  - cmmmech:europium
  - cmmmech:fluorine
  - cmmmech:gadolinium
  - cmmmech:gallium
  - cmmmech:germanium
  - cmmmech:gold
  - cmmmech:hafnium
  - cmmmech:helium
  - cmmmech:holmium
  - cmmmech:indium
  - cmmmech:iridium
  - cmmmech:iron
  - cmmmech:lanthanum
  - cmmmech:lead
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:magnesium
  - cmmmech:manganese
  - cmmmech:molybdenum
  - cmmmech:neodymium
  - cmmmech:nickel
  - cmmmech:niobium
  - cmmmech:osmium
  - cmmmech:palladium
  - cmmmech:phosphorus
  - cmmmech:platinum
  - cmmmech:praseodymium
  - cmmmech:promethium
  - cmmmech:rhenium
  - cmmmech:rhodium
  - cmmmech:rubidium
  - cmmmech:ruthenium
  - cmmmech:samarium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:strontium
  - cmmmech:tantalum
  - cmmmech:tellurium
  - cmmmech:terbium
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:tin
  - cmmmech:titanium
  - cmmmech:tungsten
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:ytterbium
  - cmmmech:yttrium
  - cmmmech:zinc
  - cmmmech:zirconium
  selection: data/records/*.yaml where material_kind == 'element' at 208134600496b954831b125033d33caa508dba8b
  description: Full-population Cycle 5 Stage 4 category review of all 66 chemical
    element records in CMMMech.
targets:
- target_id: cmmmech:aluminium
  path: data/records/aluminium.yaml
  kind: maintained
  label: Aluminium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aluminium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:antimony
  path: data/records/antimony.yaml
  kind: maintained
  label: Antimony
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/antimony.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
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
- target_id: cmmmech:beryllium
  path: data/records/beryllium.yaml
  kind: maintained
  label: Beryllium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/beryllium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bismuth
  path: data/records/bismuth.yaml
  kind: maintained
  label: Bismuth
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bismuth.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:boron
  path: data/records/boron.yaml
  kind: maintained
  label: Boron
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boron.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cadmium
  path: data/records/cadmium.yaml
  kind: maintained
  label: Cadmium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cerium
  path: data/records/cerium.yaml
  kind: maintained
  label: Cerium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cesium
  path: data/records/cesium.yaml
  kind: maintained
  label: Cesium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cesium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chromium
  path: data/records/chromium.yaml
  kind: maintained
  label: Chromium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cobalt
  path: data/records/cobalt.yaml
  kind: maintained
  label: Cobalt
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cobalt.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:copper
  path: data/records/copper.yaml
  kind: maintained
  label: Copper
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dysprosium
  path: data/records/dysprosium.yaml
  kind: maintained
  label: Dysprosium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dysprosium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:erbium
  path: data/records/erbium.yaml
  kind: maintained
  label: Erbium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/erbium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:europium
  path: data/records/europium.yaml
  kind: maintained
  label: Europium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/europium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorine
  path: data/records/fluorine.yaml
  kind: maintained
  label: Fluorine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gadolinium
  path: data/records/gadolinium.yaml
  kind: maintained
  label: Gadolinium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gadolinium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gallium
  path: data/records/gallium.yaml
  kind: maintained
  label: Gallium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gallium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:germanium
  path: data/records/germanium.yaml
  kind: maintained
  label: Germanium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/germanium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gold
  path: data/records/gold.yaml
  kind: maintained
  label: Gold
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gold.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hafnium
  path: data/records/hafnium.yaml
  kind: maintained
  label: Hafnium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hafnium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:helium
  path: data/records/helium.yaml
  kind: maintained
  label: Helium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/helium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:holmium
  path: data/records/holmium.yaml
  kind: maintained
  label: Holmium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/holmium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:indium
  path: data/records/indium.yaml
  kind: maintained
  label: Indium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/indium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:iridium
  path: data/records/iridium.yaml
  kind: maintained
  label: Iridium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/iridium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:iron
  path: data/records/iron.yaml
  kind: maintained
  label: Iron
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/iron.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lanthanum
  path: data/records/lanthanum.yaml
  kind: maintained
  label: Lanthanum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lead
  path: data/records/lead.yaml
  kind: maintained
  label: Lead
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lead.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithium
  path: data/records/lithium.yaml
  kind: maintained
  label: Lithium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lutetium
  path: data/records/lutetium.yaml
  kind: maintained
  label: Lutetium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lutetium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:magnesium
  path: data/records/magnesium.yaml
  kind: maintained
  label: Magnesium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:manganese
  path: data/records/manganese.yaml
  kind: maintained
  label: Manganese
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:molybdenum
  path: data/records/molybdenum.yaml
  kind: maintained
  label: Molybdenum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:neodymium
  path: data/records/neodymium.yaml
  kind: maintained
  label: Neodymium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/neodymium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nickel
  path: data/records/nickel.yaml
  kind: maintained
  label: Nickel
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:niobium
  path: data/records/niobium.yaml
  kind: maintained
  label: Niobium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/niobium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:osmium
  path: data/records/osmium.yaml
  kind: maintained
  label: Osmium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/osmium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:palladium
  path: data/records/palladium.yaml
  kind: maintained
  label: Palladium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/palladium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phosphorus
  path: data/records/phosphorus.yaml
  kind: maintained
  label: Phosphorus
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphorus.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:platinum
  path: data/records/platinum.yaml
  kind: maintained
  label: Platinum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/platinum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:praseodymium
  path: data/records/praseodymium.yaml
  kind: maintained
  label: Praseodymium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/praseodymium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:promethium
  path: data/records/promethium.yaml
  kind: maintained
  label: Promethium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/promethium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhenium
  path: data/records/rhenium.yaml
  kind: maintained
  label: Rhenium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rhodium
  path: data/records/rhodium.yaml
  kind: maintained
  label: Rhodium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhodium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rubidium
  path: data/records/rubidium.yaml
  kind: maintained
  label: Rubidium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rubidium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ruthenium
  path: data/records/ruthenium.yaml
  kind: maintained
  label: Ruthenium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ruthenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:samarium
  path: data/records/samarium.yaml
  kind: maintained
  label: Samarium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:scandium
  path: data/records/scandium.yaml
  kind: maintained
  label: Scandium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:selenium
  path: data/records/selenium.yaml
  kind: maintained
  label: Selenium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:silicon
  path: data/records/silicon.yaml
  kind: maintained
  label: Silicon
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:silver
  path: data/records/silver.yaml
  kind: maintained
  label: Silver
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silver.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:strontium
  path: data/records/strontium.yaml
  kind: maintained
  label: Strontium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tantalum
  path: data/records/tantalum.yaml
  kind: maintained
  label: Tantalum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tantalum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tellurium
  path: data/records/tellurium.yaml
  kind: maintained
  label: Tellurium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tellurium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:terbium
  path: data/records/terbium.yaml
  kind: maintained
  label: Terbium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/terbium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:thallium
  path: data/records/thallium.yaml
  kind: maintained
  label: Thallium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thallium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:thulium
  path: data/records/thulium.yaml
  kind: maintained
  label: Thulium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tin
  path: data/records/tin.yaml
  kind: maintained
  label: Tin
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tin.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:titanium
  path: data/records/titanium.yaml
  kind: maintained
  label: Titanium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tungsten
  path: data/records/tungsten.yaml
  kind: maintained
  label: Tungsten
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tungsten.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uranium
  path: data/records/uranium.yaml
  kind: maintained
  label: Uranium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vanadium
  path: data/records/vanadium.yaml
  kind: maintained
  label: Vanadium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vanadium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ytterbium
  path: data/records/ytterbium.yaml
  kind: maintained
  label: Ytterbium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ytterbium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:yttrium
  path: data/records/yttrium.yaml
  kind: maintained
  label: Yttrium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/yttrium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zinc
  path: data/records/zinc.yaml
  kind: maintained
  label: Zinc
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zirconium
  path: data/records/zirconium.yaml
  kind: maintained
  label: Zirconium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zirconium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-element-cohort
  name: cmmmech validate element cohort (66 records)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:aluminium
  - cmmmech:antimony
  - cmmmech:arsenic
  - cmmmech:beryllium
  - cmmmech:bismuth
  - cmmmech:boron
  - cmmmech:cadmium
  - cmmmech:cerium
  - cmmmech:cesium
  - cmmmech:chromium
  - cmmmech:cobalt
  - cmmmech:copper
  - cmmmech:dysprosium
  - cmmmech:erbium
  - cmmmech:europium
  - cmmmech:fluorine
  - cmmmech:gadolinium
  - cmmmech:gallium
  - cmmmech:germanium
  - cmmmech:gold
  - cmmmech:hafnium
  - cmmmech:helium
  - cmmmech:holmium
  - cmmmech:indium
  - cmmmech:iridium
  - cmmmech:iron
  - cmmmech:lanthanum
  - cmmmech:lead
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:magnesium
  - cmmmech:manganese
  - cmmmech:molybdenum
  - cmmmech:neodymium
  - cmmmech:nickel
  - cmmmech:niobium
  - cmmmech:osmium
  - cmmmech:palladium
  - cmmmech:phosphorus
  - cmmmech:platinum
  - cmmmech:praseodymium
  - cmmmech:promethium
  - cmmmech:rhenium
  - cmmmech:rhodium
  - cmmmech:rubidium
  - cmmmech:ruthenium
  - cmmmech:samarium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:strontium
  - cmmmech:tantalum
  - cmmmech:tellurium
  - cmmmech:terbium
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:tin
  - cmmmech:titanium
  - cmmmech:tungsten
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:ytterbium
  - cmmmech:yttrium
  - cmmmech:zinc
  - cmmmech:zirconium
  evidence_ids:
  - ev-element-cohort-audit
  summary: All 66 records in cohort pass LinkML structural and semantic validation
    with 0 errors.
assessments:
- assessment_id: assess-element-identity-and-criticality
  topic: Element identity (CHEBI atom CURIEs) and jurisdiction-scoped criticality
    lists
  area: identity
  outcome: supported
  target_ids:
  - cmmmech:aluminium
  - cmmmech:antimony
  - cmmmech:arsenic
  - cmmmech:beryllium
  - cmmmech:bismuth
  - cmmmech:boron
  - cmmmech:cadmium
  - cmmmech:cerium
  - cmmmech:cesium
  - cmmmech:chromium
  - cmmmech:cobalt
  - cmmmech:copper
  - cmmmech:dysprosium
  - cmmmech:erbium
  - cmmmech:europium
  - cmmmech:fluorine
  - cmmmech:gadolinium
  - cmmmech:gallium
  - cmmmech:germanium
  - cmmmech:gold
  - cmmmech:hafnium
  - cmmmech:helium
  - cmmmech:holmium
  - cmmmech:indium
  - cmmmech:iridium
  - cmmmech:iron
  - cmmmech:lanthanum
  - cmmmech:lead
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:magnesium
  - cmmmech:manganese
  - cmmmech:molybdenum
  - cmmmech:neodymium
  - cmmmech:nickel
  - cmmmech:niobium
  - cmmmech:osmium
  - cmmmech:palladium
  - cmmmech:phosphorus
  - cmmmech:platinum
  - cmmmech:praseodymium
  - cmmmech:promethium
  - cmmmech:rhenium
  - cmmmech:rhodium
  - cmmmech:rubidium
  - cmmmech:ruthenium
  - cmmmech:samarium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:strontium
  - cmmmech:tantalum
  - cmmmech:tellurium
  - cmmmech:terbium
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:tin
  - cmmmech:titanium
  - cmmmech:tungsten
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:ytterbium
  - cmmmech:yttrium
  - cmmmech:zinc
  - cmmmech:zirconium
  evidence_ids:
  - ev-element-cohort-audit
  summary: All 66 element records carry canonical CHEBI atom CURIEs and labels with
    0 cross-corpus label conflicts and dated criticality lists.
- assessment_id: assess-element-mechanisms-and-grounding
  topic: Microbial extraction/transformation/recovery mechanisms, causal graphs, and
    UniProtKB protein examples
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:aluminium
  - cmmmech:antimony
  - cmmmech:arsenic
  - cmmmech:beryllium
  - cmmmech:bismuth
  - cmmmech:boron
  - cmmmech:cadmium
  - cmmmech:cerium
  - cmmmech:cesium
  - cmmmech:chromium
  - cmmmech:cobalt
  - cmmmech:copper
  - cmmmech:dysprosium
  - cmmmech:erbium
  - cmmmech:europium
  - cmmmech:fluorine
  - cmmmech:gadolinium
  - cmmmech:gallium
  - cmmmech:germanium
  - cmmmech:gold
  - cmmmech:hafnium
  - cmmmech:helium
  - cmmmech:holmium
  - cmmmech:indium
  - cmmmech:iridium
  - cmmmech:iron
  - cmmmech:lanthanum
  - cmmmech:lead
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:magnesium
  - cmmmech:manganese
  - cmmmech:molybdenum
  - cmmmech:neodymium
  - cmmmech:nickel
  - cmmmech:niobium
  - cmmmech:osmium
  - cmmmech:palladium
  - cmmmech:phosphorus
  - cmmmech:platinum
  - cmmmech:praseodymium
  - cmmmech:promethium
  - cmmmech:rhenium
  - cmmmech:rhodium
  - cmmmech:rubidium
  - cmmmech:ruthenium
  - cmmmech:samarium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:strontium
  - cmmmech:tantalum
  - cmmmech:tellurium
  - cmmmech:terbium
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:tin
  - cmmmech:titanium
  - cmmmech:tungsten
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:ytterbium
  - cmmmech:yttrium
  - cmmmech:zinc
  - cmmmech:zirconium
  evidence_ids:
  - ev-element-cohort-audit
  summary: 63/66 element records contain primary-source-supported microbial mechanisms
    (66 mechanisms total); 24/66 contain causal_graphs (25 graphs), with 23/24 grounded
    to 33 unique UniProtKB accessions and 3 GENE_OR_PROTEIN nodes across cmmmech:iron
    (ax17_extracellular_fe3_reductase_system), cmmmech:manganese (mopa_heme_peroxidase),
    and cmmmech:praseodymium (melba_lanm_o36) explicitly marked UNGROUNDED where strain-resolved
    UniProtKB entries are absent. Nine element records serialize criticality before
    sources.
findings:
- finding_id: cmmmech-cycle5-stage4-finding-0001
  issue_key: cmmmech.records.criticality-before-sources-key-order
  title: Top-level YAML key order places criticality before sources instead of canonical
    CriticalMineralRecord / CANONICAL_RECORD_KEYS order
  severity: minor
  category: representation
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:chromium
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:uranium
  - cmmmech:vanadium
  field_paths:
  - sources
  - criticality
  evidence_ids:
  - ev-element-cohort-audit
  description: Across the 668-record corpus, 13 records (chromium.yaml, electrical-steel.yaml,
    hafnium.yaml, manganese.yaml, praseodymium.yaml, rare-earth-element-commodities.yaml,
    scandium.yaml, selenium.yaml, silicon-carbide.yaml, silicon.yaml, synthetic-graphite.yaml,
    uranium.yaml, vanadium.yaml) serialize top-level 'criticality' before 'sources',
    whereas CriticalMineralRecord in src/cmmmech/schema/cmmmech.yaml and CANONICAL_RECORD_KEYS
    in scripts/new_history.py place 'sources' before 'criticality'. In this cohort,
    9 record(s) (chromium, hafnium, manganese, praseodymium, scandium, selenium, silicon,
    uranium, vanadium) exhibit this non-canonical key order.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium.yaml
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
    path: data/records/scandium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/vanadium.yaml
    role: maintained_record
actions:
- action_id: act-normalize-criticality-before-sources-key-order
  finding_ids:
  - cmmmech-cycle5-stage4-finding-0001
  target_ids:
  - cmmmech:chromium
  - cmmmech:hafnium
  - cmmmech:manganese
  - cmmmech:praseodymium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:uranium
  - cmmmech:vanadium
  description: Reorder top-level YAML keys so sources precedes criticality in Stage
    5 grouped remediation and record canonical history sidecars.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium.yaml
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
    path: data/records/scandium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/silicon.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/vanadium.yaml
    role: maintained_record
  acceptance_checks:
  - All affected records serialize sources before criticality in canonical CriticalMineralRecord
    / CANONICAL_RECORD_KEYS order.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-element-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'element')
  locator: 66 element YAML files
  accessed_at: '2026-10-30T20:10:00Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 66 element records at
    commit 208134600496b954831b125033d33caa508dba8b.
limitations:
- 'Three element records currently lack curated microbial mechanism entries: cmmmech:beryllium,
  cmmmech:helium, and cmmmech:promethium are maintained criticality-anchored element
  records awaiting primary microbial extraction/transformation/recovery evidence.
  (63/66 element records have curated mechanisms; 3/66 remain identity and criticality
  records only.)'
- 'Three GENE_OR_PROTEIN nodes in the element cohort remain explicitly UNGROUNDED
  due to absent strain-resolved sequences in UniProtKB: ax17_extracellular_fe3_reductase_system
  in cmmmech:iron (Desulfovulcanus ferrireducens Ax17), mopa_heme_peroxidase in cmmmech:manganese,
  and melba_lanm_o36 in cmmmech:praseodymium (23/24 element records with causal_graphs
  carry GROUNDED protein_examples; cmmmech:iron has only an UNGROUNDED node).'
notes:
- Cohort covers 100% (66/66) of target records in data/records/*.yaml at commit 208134600496b954831b125033d33caa508dba8b.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:aluminium
  - cmmmech:antimony
  - cmmmech:arsenic
  - cmmmech:beryllium
  - cmmmech:bismuth
  - cmmmech:boron
  - cmmmech:cadmium
  - cmmmech:cerium
  - cmmmech:cesium
  - cmmmech:chromium
  - cmmmech:cobalt
  - cmmmech:copper
  - cmmmech:dysprosium
  - cmmmech:erbium
  - cmmmech:europium
  - cmmmech:fluorine
  - cmmmech:gadolinium
  - cmmmech:gallium
  - cmmmech:germanium
  - cmmmech:gold
  - cmmmech:hafnium
  - cmmmech:helium
  - cmmmech:holmium
  - cmmmech:indium
  - cmmmech:iridium
  - cmmmech:iron
  - cmmmech:lanthanum
  - cmmmech:lead
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:magnesium
  - cmmmech:manganese
  - cmmmech:molybdenum
  - cmmmech:neodymium
  - cmmmech:nickel
  - cmmmech:niobium
  - cmmmech:osmium
  - cmmmech:palladium
  - cmmmech:phosphorus
  - cmmmech:platinum
  - cmmmech:praseodymium
  - cmmmech:promethium
  - cmmmech:rhenium
  - cmmmech:rhodium
  - cmmmech:rubidium
  - cmmmech:ruthenium
  - cmmmech:samarium
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:strontium
  - cmmmech:tantalum
  - cmmmech:tellurium
  - cmmmech:terbium
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:tin
  - cmmmech:titanium
  - cmmmech:tungsten
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:ytterbium
  - cmmmech:yttrium
  - cmmmech:zinc
  - cmmmech:zirconium
  rationale: All 66 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where material_kind == 'element' at 208134600496b954831b125033d33caa508dba8b
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-element-cohort-audit
```
