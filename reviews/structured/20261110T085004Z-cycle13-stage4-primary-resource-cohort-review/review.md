# Cycle 13 Stage 4 full-cohort review: primary_resource records (31/31)

- Review: 20261110T085004Z-cycle13-stage4-primary-resource-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T08:47:00Z
- Finished UTC: 2026-11-10T08:50:04Z
- Reviewer: antigravity / cmmmech-cycle13-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 31 primary_resource records in data/records/*.yaml at commit 01de2d17fc49adec7f67da17266cbc82713d0df1. All 31/31 primary_resource records contain primary-source-supported mechanisms (29 records with microbial mechanisms and 2 records with abiotic-only mechanisms; 42 mechanisms total: 40 microbial and 2 abiotic), and 16/31 contain causal_graphs (17 graphs, 34 GENE_OR_PROTEIN nodes: 34 GROUNDED and 0 UNGROUNDED) grounded to 46 unique UniProtKB accessions. Identified 1 minor graph finding (cmmmech-cycle13-stage4-finding-0003 on cmmmech:allanite-concentrate) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 13 Stage 4 category review of all 31 primary_resource records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'primary_resource' at 01de2d17fc49adec7f67da17266cbc82713d0df1
Coverage: full; 31 reviewed / 31 in the declared population.
Source: git_commit at Git base 01de2d17fc49adec7f67da17266cbc82713d0df1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:basalt | data/records/basalt.yaml | maintained | Basaltic rock |
| cmmmech:carbonatite-associated-rare-earth-ore | data/records/carbonatite-associated-rare-earth-ore.yaml | maintained | Carbonatite-associated rare-earth ore |
| cmmmech:cassiterite-polymetallic-sulfide-ore | data/records/cassiterite-polymetallic-sulfide-ore.yaml | maintained | Cassiterite-polymetallic sulfide ore |
| cmmmech:chalcopyrite-enargite-concentrate | data/records/chalcopyrite-enargite-concentrate.yaml | maintained | Chalcopyrite-enargite concentrate |
| cmmmech:cobalt-rich-ferromanganese-crusts | data/records/cobalt-rich-ferromanganese-crusts.yaml | maintained | Cobalt-rich ferromanganese crusts |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |
| cmmmech:enargite-pyrite-concentrate | data/records/enargite-pyrite-concentrate.yaml | maintained | Enargite-pyrite concentrate |
| cmmmech:eucrite-meteorite | data/records/eucrite-meteorite.yaml | maintained | Eucrite meteorite |
| cmmmech:eudialyte-concentrate | data/records/eudialyte-concentrate.yaml | maintained | Eudialyte concentrate |
| cmmmech:eudialyte-ore | data/records/eudialyte-ore.yaml | maintained | Eudialyte ore |
| cmmmech:ion-adsorption-rare-earth-clay | data/records/ion-adsorption-rare-earth-clay.yaml | maintained | Ion-adsorption rare-earth clay |
| cmmmech:kaolin | data/records/kaolin.yaml | maintained | Natural kaolin feed |
| cmmmech:l-chondrite-meteorite | data/records/l-chondrite-meteorite.yaml | maintained | L-chondrite meteorite |
| cmmmech:lithium-bearing-geothermal-brine | data/records/lithium-bearing-geothermal-brine.yaml | maintained | Lithium-bearing geothermal brine |
| cmmmech:lithium-mica-ore | data/records/lithium-mica-ore.yaml | maintained | Lithium-mica ore |
| cmmmech:ludwigite-ore | data/records/ludwigite-ore.yaml | maintained | Ludwigite boron-iron ore |
| cmmmech:manganese-ore | data/records/manganese-ore.yaml | maintained | Manganese ore |
| cmmmech:metalliferous-black-shale | data/records/metalliferous-black-shale.yaml | maintained | Metalliferous black shale |
| cmmmech:monazite-ore | data/records/monazite-ore.yaml | maintained | Monazite ore |
| cmmmech:nickel-laterite-ore | data/records/nickel-laterite-ore.yaml | maintained | Nickel laterite ore |
| cmmmech:nickeline-bearing-ore | data/records/nickeline-bearing-ore.yaml | maintained | Nickeline-bearing ore |
| cmmmech:oxidized-zinc-ore | data/records/oxidized-zinc-ore.yaml | maintained | Oxidized zinc ore |
| cmmmech:polymetallic-nodules | data/records/polymetallic-nodules.yaml | maintained | Polymetallic nodules |
| cmmmech:rare-earth-rich-deep-sea-mud | data/records/rare-earth-rich-deep-sea-mud.yaml | maintained | Rare-earth-rich deep-sea mud |
| cmmmech:seafloor-massive-sulfides | data/records/seafloor-massive-sulfides.yaml | maintained | Seafloor massive sulfides |
| cmmmech:seawater | data/records/seawater.yaml | maintained | Seawater |
| cmmmech:silica-sand | data/records/silica-sand.yaml | maintained | Natural silica-sand feed |
| cmmmech:tennantite-concentrate | data/records/tennantite-concentrate.yaml | maintained | Tennantite concentrate |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |
| cmmmech:xenotime-concentrate | data/records/xenotime-concentrate.yaml | maintained | Xenotime concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate (primary_resource cohort) | passed | True | cmmmech:allanite-concentrate, cmmmech:basalt, cmmmech:carbonatite-associated-rare-earth-ore, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:cobalt-rich-ferromanganese-crusts, cmmmech:dunite, cmmmech:enargite-pyrite-concentrate, cmmmech:eucrite-meteorite, cmmmech:eudialyte-concentrate, cmmmech:eudialyte-ore, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:kaolin, cmmmech:l-chondrite-meteorite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:ludwigite-ore, cmmmech:manganese-ore, cmmmech:metalliferous-black-shale, cmmmech:monazite-ore, cmmmech:nickel-laterite-ore, cmmmech:nickeline-bearing-ore, cmmmech:oxidized-zinc-ore, cmmmech:polymetallic-nodules, cmmmech:rare-earth-rich-deep-sea-mud, cmmmech:seafloor-massive-sulfides, cmmmech:seawater, cmmmech:silica-sand, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:xenotime-concentrate | All 31 primary_resource cohort records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (primary_resource cohort) | passed | True | cmmmech:allanite-concentrate, cmmmech:basalt, cmmmech:carbonatite-associated-rare-earth-ore, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:cobalt-rich-ferromanganese-crusts, cmmmech:dunite, cmmmech:enargite-pyrite-concentrate, cmmmech:eucrite-meteorite, cmmmech:eudialyte-concentrate, cmmmech:eudialyte-ore, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:kaolin, cmmmech:l-chondrite-meteorite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:ludwigite-ore, cmmmech:manganese-ore, cmmmech:metalliferous-black-shale, cmmmech:monazite-ore, cmmmech:nickel-laterite-ore, cmmmech:nickeline-bearing-ore, cmmmech:oxidized-zinc-ore, cmmmech:polymetallic-nodules, cmmmech:rare-earth-rich-deep-sea-mud, cmmmech:seafloor-massive-sulfides, cmmmech:seawater, cmmmech:silica-sand, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:xenotime-concentrate | All 31 primary_resource cohort records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### ENVO/CHEBI grounding, primary ore/brine/concentrate mechanisms, and causal graphs

evidence: supported. Targets: cmmmech:allanite-concentrate, cmmmech:basalt, cmmmech:carbonatite-associated-rare-earth-ore, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:cobalt-rich-ferromanganese-crusts, cmmmech:dunite, cmmmech:enargite-pyrite-concentrate, cmmmech:eucrite-meteorite, cmmmech:eudialyte-concentrate, cmmmech:eudialyte-ore, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:kaolin, cmmmech:l-chondrite-meteorite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:ludwigite-ore, cmmmech:manganese-ore, cmmmech:metalliferous-black-shale, cmmmech:monazite-ore, cmmmech:nickel-laterite-ore, cmmmech:nickeline-bearing-ore, cmmmech:oxidized-zinc-ore, cmmmech:polymetallic-nodules, cmmmech:rare-earth-rich-deep-sea-mud, cmmmech:seafloor-massive-sulfides, cmmmech:seawater, cmmmech:silica-sand, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:xenotime-concentrate.

31/31 primary_resource records carry primary-source-supported mechanisms (40 microbial and 2 abiotic mechanisms across 31 records), and 16/31 carry causal_graphs (17 graphs) grounded to 46 unique UniProtKB accessions. Identified 1 minor graph finding on cmmmech:allanite-concentrate.

## Findings

### cmmmech-cycle13-stage4-finding-0003: Gluconobacter oxydans B58 causal graphs and protein examples in allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml retain template PqqC/Gdh descriptions and supports: support polarity omitting 621H proxy grounding, residual mutant leaching, and relative extraction denominators

minor / open / confirmed; issue key: cmmmech.schmitz-marecos-gluconobacter-graphs.template-pqqc-gdh-nodes-edges-and-relative-denominator-qualifications.

In data/records/allanite-concentrate.yaml (cmmmech:allanite-concentrate, primary_resource, Schmitz et al. 2025 Communications Biology 8:815, schmitz2025; causal_graphs[0] lines 182-398), data/records/fluorescent-lamp-phosphor.yaml (cmmmech:fluorescent-lamp-phosphor, secondary_resource, Schmitz et al. 2021 Nature Communications 12:6693, schmitz2021; causal_graphs[0] lines 105-263), and data/records/neodymium.yaml (cmmmech:neodymium, element, Marecos et al. 2025 Communications Biology 8:682, marecos2025; causal_graphs[0] lines 204-403), Gluconobacter oxydans B58 protein_examples (UniProtKB:Q9L3B2 PqqC, UniProtKB:P27175 Gdh, UniProtKB:Q5FT13 PstC in fluorescent-lamp-phosphor.yaml, and UniProtKB:Q5FQK7 GOX1598 in neodymium.yaml) and causal_graphs[0] nodes/edges retain generic 72-to-130-character template descriptions and supports: support polarity that omit 621H reference-proteome (UP000006375) proxy grounding for unsequenced experimental strain B58, residual REE release in mgdh/pqqC disruption mutants (Figure 4D of schmitz2021) and non-pH mutant effects (9 of 12 mutants in marecos2025; unresolved concentration vs composition in schmitz2025 Discussion), relative-over-wild-type vs absolute-recovery denominators (53.1%/73.1% in schmitz2025; ~111% in marecos2025; literature-based 4.7%/5.5% phosphor denominator in schmitz2021), and study-specific timing/control caveats (24 h vs 36 h pH timing and Figure S2 nitric-acid comparator in schmitz2025; non-sterile-filtered centrifuged supernatant in schmitz2021; missing no-bacteria rows in Supplementary Data 4A of marecos2025). In this scope, 1 record(s) (allanite-concentrate) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-schmitz-marecos-gluconobacter-graphs-and-proteins

Update protein_examples and causal_graphs[0] nodes/edges across data/records/allanite-concentrate.yaml, data/records/fluorescent-lamp-phosphor.yaml, and data/records/neodymium.yaml to supports: partial with study-specific prose documenting 621H reference-proteome proxy grounding for strain B58, residual mgdh/pqqC mutant leaching and non-pH mutant effects, relative-over-wild-type vs absolute-recovery denominators, and study-specific timing/control caveats during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[].protein_examples and causal_graphs[0].nodes[].protein_examples across allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml are byte-identical with supports: partial and study-specific prose.
- causal_graphs[0].nodes and edges across all 3 records replace template PqqC/Gdh/biolixiviant text with study-specific conditions, relative denominators, and control caveats with supports: partial.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:allanite-concentrate, cmmmech:basalt, cmmmech:carbonatite-associated-rare-earth-ore, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:cobalt-rich-ferromanganese-crusts, cmmmech:dunite, cmmmech:enargite-pyrite-concentrate, cmmmech:eucrite-meteorite, cmmmech:eudialyte-concentrate, cmmmech:eudialyte-ore, cmmmech:ion-adsorption-rare-earth-clay, cmmmech:kaolin, cmmmech:l-chondrite-meteorite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:ludwigite-ore, cmmmech:manganese-ore, cmmmech:metalliferous-black-shale, cmmmech:monazite-ore, cmmmech:nickel-laterite-ore, cmmmech:nickeline-bearing-ore, cmmmech:oxidized-zinc-ore, cmmmech:polymetallic-nodules, cmmmech:rare-earth-rich-deep-sea-mud, cmmmech:seafloor-massive-sulfides, cmmmech:seawater, cmmmech:silica-sand, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:xenotime-concentrate. All 31 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'primary_resource' at 01de2d17fc49adec7f67da17266cbc82713d0df1 with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-primary-resource-cohort-audit | data/records/*.yaml (material_kind == 'primary_resource'); 31 primary_resource YAML files | supports | Full programmatic and source-backed audit of all 31 primary_resource records at commit 01de2d17fc49adec7f67da17266cbc82713d0df1. |
| ev-schmitz2025-allanite-graph | data/records/allanite-concentrate.yaml; mechanisms[0] (lines 35-180); causal_graphs[0] (lines 182-398) | supports | In data/records/allanite-concentrate.yaml, Gluconobacter oxydans B58 PqqC/Gdh protein_examples[3..4] and causal_graphs[0] nodes/edges retain template 72-130 char descriptions and supports: support polarity omitting 621H proxy grounding, 24 h vs 36 h pH timing discrepancy, relative 53.1%/73.1% denominators, and Figure S2 nitric-acid comparator caveats. |

## Limits And Additional Notes

- 2 of 31 primary_resource records (eudialyte-concentrate and ludwigite-ore) currently carry abiotic acid/hydrometallurgical baseline mechanisms without published microbial bioleaching counterparts.
- 13 of 31 primary_resource records (13 of 29 with microbial mechanisms) have microbial mechanisms that do not yet have multi-node enzymatic causal graphs.
- Cohort covers 100% (31/31) of primary_resource cohort records at commit 01de2d17fc49adec7f67da17266cbc82713d0df1.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T085004Z-cycle13-stage4-primary-resource-cohort-review
title: 'Cycle 13 Stage 4 full-cohort review: primary_resource records (31/31)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-10T08:47:00Z'
finished_at: '2026-11-10T08:50:04Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 31 primary_resource records in data/records/*.yaml at commit
  01de2d17fc49adec7f67da17266cbc82713d0df1. All 31/31 primary_resource records contain
  primary-source-supported mechanisms (29 records with microbial mechanisms and 2
  records with abiotic-only mechanisms; 42 mechanisms total: 40 microbial and 2 abiotic),
  and 16/31 contain causal_graphs (17 graphs, 34 GENE_OR_PROTEIN nodes: 34 GROUNDED
  and 0 UNGROUNDED) grounded to 46 unique UniProtKB accessions. Identified 1 minor
  graph finding (cmmmech-cycle13-stage4-finding-0003 on cmmmech:allanite-concentrate)
  for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 13 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 01de2d17fc49adec7f67da17266cbc82713d0df1.
source:
  git_revision: 01de2d17fc49adec7f67da17266cbc82713d0df1
  state: git_commit
  inputs:
  - path: data/records/allanite-concentrate.yaml
    sha256: ba71a3f46b79fb93a742dcf7449344897cf9e6761d3e1d7750b819ae219fdc54
    role: target
  - path: data/records/basalt.yaml
    sha256: e7f999badce7c3ebca3fe28a56827f602d4162b5b6e4b00729b06b019001e1e5
    role: target
  - path: data/records/carbonatite-associated-rare-earth-ore.yaml
    sha256: 9e856c3d9aa14c56fb3a7b70ae3ec0a97da48045debc569dcdf832a7258e0be2
    role: target
  - path: data/records/cassiterite-polymetallic-sulfide-ore.yaml
    sha256: aa9d75f7762e919fd7331ff82cdc90fc6dab9ce09683a38be355430dd5322e42
    role: target
  - path: data/records/chalcopyrite-enargite-concentrate.yaml
    sha256: 2f48356455d8578b2b396225b3ffd728d6194d5453ac8fd41d9c9cd73055dab9
    role: target
  - path: data/records/cobalt-rich-ferromanganese-crusts.yaml
    sha256: 2fb1a8680f44580a73bd26c503266ff645f03c3fef01380f23ad15db532a04f1
    role: target
  - path: data/records/dunite.yaml
    sha256: e80e1f6aec45acb1ccbb15eb8ea9f75d436611cbc216e66210470b46d2c13183
    role: target
  - path: data/records/enargite-pyrite-concentrate.yaml
    sha256: a3d694164065ec1746ed52154bd182f8808ace3d484a1d94213db51175e108a0
    role: target
  - path: data/records/eucrite-meteorite.yaml
    sha256: 92a87d16eb94ca6965bc030fc3ea541135f7e7b56c7559c50dd73c5733f6d0c8
    role: target
  - path: data/records/eudialyte-concentrate.yaml
    sha256: afa309420e2e20f08868b5708c24e08ba612088643b9c484d9c53d755846b647
    role: target
  - path: data/records/eudialyte-ore.yaml
    sha256: ece4b1e3405e97cdee81ccb810e3104d9877950f160593e0ba3d0931ab85156f
    role: target
  - path: data/records/ion-adsorption-rare-earth-clay.yaml
    sha256: 3a3c3cd05e03e27a3cb97e31d3ebc9c1f9b4c89747a48b029257cc02570ecf1d
    role: target
  - path: data/records/kaolin.yaml
    sha256: 8e754fc3cba67a9b31d2cae9ef8846128fbe6f39c1b3d591d3e5434fb25b29f0
    role: target
  - path: data/records/l-chondrite-meteorite.yaml
    sha256: 34584d2e958a41003f07514974d96899043cc729ea68c621ebef65254875601f
    role: target
  - path: data/records/lithium-bearing-geothermal-brine.yaml
    sha256: 94d9b81f61dd307f3f3e52e33f036a0a6d6e34b07b7670b3c27360e4505e704c
    role: target
  - path: data/records/lithium-mica-ore.yaml
    sha256: 5476a13cee4f2dd135821975f2d09289e50ea5ecd7b655c81cf805bcc295436e
    role: target
  - path: data/records/ludwigite-ore.yaml
    sha256: c55996420abc0062e76e4f91370f9dd2d28e508d77604fe17d23f6dba38ff5c5
    role: target
  - path: data/records/manganese-ore.yaml
    sha256: 808286d076a7e344b2423ae035257231ce290eb7cd62535aa79eeade7bc288e8
    role: target
  - path: data/records/metalliferous-black-shale.yaml
    sha256: 1dcd46d715c4783fe411626be61cb699a74a158cbfb0bbc4ae2fbc4238f15f41
    role: target
  - path: data/records/monazite-ore.yaml
    sha256: 8b2de973c88b9156995737a0b9314600c0b9eaebb1808444db9019fc7213a82b
    role: target
  - path: data/records/nickel-laterite-ore.yaml
    sha256: a17fd9f852d59f66156b529dbdc8103929f54d275285608005fcf162c39fe42b
    role: target
  - path: data/records/nickeline-bearing-ore.yaml
    sha256: ed5380b36177b247c2adbb0b63444f8663c7bbad02ea438c29800e05a270a47a
    role: target
  - path: data/records/oxidized-zinc-ore.yaml
    sha256: a7b4bca381fce99518963f2ea3d8228c0cf19a7923ec7fe438ca17ee7163fc22
    role: target
  - path: data/records/polymetallic-nodules.yaml
    sha256: 1fb81047e94d62e7af4cf218733f32692e8cd90443acd64c4c60c4dbbef8f20d
    role: target
  - path: data/records/rare-earth-rich-deep-sea-mud.yaml
    sha256: 82896cb3ce5eb02dfaee2a537582b6a414c192332fffb582ce30ba1b31154151
    role: target
  - path: data/records/seafloor-massive-sulfides.yaml
    sha256: d5cb49646b77422d0e6e6ded8d4c6b43f5d06b8bbdf46c087207be2266fbab91
    role: target
  - path: data/records/seawater.yaml
    sha256: 3eca7555a6f0a9f377001f5968a9924b73d014179255a4c1d4a6bcf412850ec5
    role: target
  - path: data/records/silica-sand.yaml
    sha256: 302ae3df4735d3f55010f2902f11ce285828a6c80014ad475e06d92a0c34f46f
    role: target
  - path: data/records/tennantite-concentrate.yaml
    sha256: 73d880437a46d3746d0d1a2af4a51d0f661505324f0b0c4ca770afc7ee1bdc50
    role: target
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 028970846c1d345fc830dcaec41ed55d2f96b7b523a90646af3c3036276018c0
    role: target
  - path: data/records/xenotime-concentrate.yaml
    sha256: 8e1d30e8c05053055fc352625e894a6575f3ed288c5c702d0aff702cdb9290ea
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 31
  reviewed_target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:basalt
  - cmmmech:carbonatite-associated-rare-earth-ore
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:cobalt-rich-ferromanganese-crusts
  - cmmmech:dunite
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:eucrite-meteorite
  - cmmmech:eudialyte-concentrate
  - cmmmech:eudialyte-ore
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:kaolin
  - cmmmech:l-chondrite-meteorite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:ludwigite-ore
  - cmmmech:manganese-ore
  - cmmmech:metalliferous-black-shale
  - cmmmech:monazite-ore
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickeline-bearing-ore
  - cmmmech:oxidized-zinc-ore
  - cmmmech:polymetallic-nodules
  - cmmmech:rare-earth-rich-deep-sea-mud
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:seawater
  - cmmmech:silica-sand
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:xenotime-concentrate
  selection: data/records/*.yaml where material_kind == 'primary_resource' at 01de2d17fc49adec7f67da17266cbc82713d0df1
  description: Full-population Cycle 13 Stage 4 category review of all 31 primary_resource
    records in CMMMech.
targets:
- target_id: cmmmech:allanite-concentrate
  path: data/records/allanite-concentrate.yaml
  kind: maintained
  label: Allanite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:basalt
  path: data/records/basalt.yaml
  kind: maintained
  label: Basaltic rock
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/basalt.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:carbonatite-associated-rare-earth-ore
  path: data/records/carbonatite-associated-rare-earth-ore.yaml
  kind: maintained
  label: Carbonatite-associated rare-earth ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/carbonatite-associated-rare-earth-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cassiterite-polymetallic-sulfide-ore
  path: data/records/cassiterite-polymetallic-sulfide-ore.yaml
  kind: maintained
  label: Cassiterite-polymetallic sulfide ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cassiterite-polymetallic-sulfide-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chalcopyrite-enargite-concentrate
  path: data/records/chalcopyrite-enargite-concentrate.yaml
  kind: maintained
  label: Chalcopyrite-enargite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcopyrite-enargite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cobalt-rich-ferromanganese-crusts
  path: data/records/cobalt-rich-ferromanganese-crusts.yaml
  kind: maintained
  label: Cobalt-rich ferromanganese crusts
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cobalt-rich-ferromanganese-crusts.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dunite
  path: data/records/dunite.yaml
  kind: maintained
  label: Dunite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dunite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:enargite-pyrite-concentrate
  path: data/records/enargite-pyrite-concentrate.yaml
  kind: maintained
  label: Enargite-pyrite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/enargite-pyrite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:eucrite-meteorite
  path: data/records/eucrite-meteorite.yaml
  kind: maintained
  label: Eucrite meteorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eucrite-meteorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:eudialyte-concentrate
  path: data/records/eudialyte-concentrate.yaml
  kind: maintained
  label: Eudialyte concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eudialyte-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:eudialyte-ore
  path: data/records/eudialyte-ore.yaml
  kind: maintained
  label: Eudialyte ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eudialyte-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ion-adsorption-rare-earth-clay
  path: data/records/ion-adsorption-rare-earth-clay.yaml
  kind: maintained
  label: Ion-adsorption rare-earth clay
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ion-adsorption-rare-earth-clay.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kaolin
  path: data/records/kaolin.yaml
  kind: maintained
  label: Natural kaolin feed
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:l-chondrite-meteorite
  path: data/records/l-chondrite-meteorite.yaml
  kind: maintained
  label: L-chondrite meteorite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/l-chondrite-meteorite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithium-bearing-geothermal-brine
  path: data/records/lithium-bearing-geothermal-brine.yaml
  kind: maintained
  label: Lithium-bearing geothermal brine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium-bearing-geothermal-brine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lithium-mica-ore
  path: data/records/lithium-mica-ore.yaml
  kind: maintained
  label: Lithium-mica ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium-mica-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ludwigite-ore
  path: data/records/ludwigite-ore.yaml
  kind: maintained
  label: Ludwigite boron-iron ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ludwigite-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:manganese-ore
  path: data/records/manganese-ore.yaml
  kind: maintained
  label: Manganese ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metalliferous-black-shale
  path: data/records/metalliferous-black-shale.yaml
  kind: maintained
  label: Metalliferous black shale
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metalliferous-black-shale.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:monazite-ore
  path: data/records/monazite-ore.yaml
  kind: maintained
  label: Monazite ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nickel-laterite-ore
  path: data/records/nickel-laterite-ore.yaml
  kind: maintained
  label: Nickel laterite ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-laterite-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nickeline-bearing-ore
  path: data/records/nickeline-bearing-ore.yaml
  kind: maintained
  label: Nickeline-bearing ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickeline-bearing-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:oxidized-zinc-ore
  path: data/records/oxidized-zinc-ore.yaml
  kind: maintained
  label: Oxidized zinc ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/oxidized-zinc-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:polymetallic-nodules
  path: data/records/polymetallic-nodules.yaml
  kind: maintained
  label: Polymetallic nodules
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polymetallic-nodules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:rare-earth-rich-deep-sea-mud
  path: data/records/rare-earth-rich-deep-sea-mud.yaml
  kind: maintained
  label: Rare-earth-rich deep-sea mud
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-rich-deep-sea-mud.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:seafloor-massive-sulfides
  path: data/records/seafloor-massive-sulfides.yaml
  kind: maintained
  label: Seafloor massive sulfides
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/seafloor-massive-sulfides.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:seawater
  path: data/records/seawater.yaml
  kind: maintained
  label: Seawater
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/seawater.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:silica-sand
  path: data/records/silica-sand.yaml
  kind: maintained
  label: Natural silica-sand feed
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/silica-sand.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tennantite-concentrate
  path: data/records/tennantite-concentrate.yaml
  kind: maintained
  label: Tennantite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tennantite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tetrahedrite-concentrate
  path: data/records/tetrahedrite-concentrate.yaml
  kind: maintained
  label: Tetrahedrite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:xenotime-concentrate
  path: data/records/xenotime-concentrate.yaml
  kind: maintained
  label: Xenotime concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: just-validate-primary-resources
  name: just validate (primary_resource cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:basalt
  - cmmmech:carbonatite-associated-rare-earth-ore
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:cobalt-rich-ferromanganese-crusts
  - cmmmech:dunite
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:eucrite-meteorite
  - cmmmech:eudialyte-concentrate
  - cmmmech:eudialyte-ore
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:kaolin
  - cmmmech:l-chondrite-meteorite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:ludwigite-ore
  - cmmmech:manganese-ore
  - cmmmech:metalliferous-black-shale
  - cmmmech:monazite-ore
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickeline-bearing-ore
  - cmmmech:oxidized-zinc-ore
  - cmmmech:polymetallic-nodules
  - cmmmech:rare-earth-rich-deep-sea-mud
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:seawater
  - cmmmech:silica-sand
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - ev-primary-resource-cohort-audit
  summary: All 31 primary_resource cohort records pass LinkML structural, semantic,
    and canonical top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-primary-resources
  name: just verify-history (primary_resource cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:basalt
  - cmmmech:carbonatite-associated-rare-earth-ore
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:cobalt-rich-ferromanganese-crusts
  - cmmmech:dunite
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:eucrite-meteorite
  - cmmmech:eudialyte-concentrate
  - cmmmech:eudialyte-ore
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:kaolin
  - cmmmech:l-chondrite-meteorite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:ludwigite-ore
  - cmmmech:manganese-ore
  - cmmmech:metalliferous-black-shale
  - cmmmech:monazite-ore
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickeline-bearing-ore
  - cmmmech:oxidized-zinc-ore
  - cmmmech:polymetallic-nodules
  - cmmmech:rare-earth-rich-deep-sea-mud
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:seawater
  - cmmmech:silica-sand
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - ev-primary-resource-cohort-audit
  summary: All 31 primary_resource cohort records have intact append-only history
    sidecars and matching curation_history metadata.
assessments:
- assessment_id: assess-primary-resource-identity-and-mechanisms
  topic: ENVO/CHEBI grounding, primary ore/brine/concentrate mechanisms, and causal
    graphs
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:basalt
  - cmmmech:carbonatite-associated-rare-earth-ore
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:cobalt-rich-ferromanganese-crusts
  - cmmmech:dunite
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:eucrite-meteorite
  - cmmmech:eudialyte-concentrate
  - cmmmech:eudialyte-ore
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:kaolin
  - cmmmech:l-chondrite-meteorite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:ludwigite-ore
  - cmmmech:manganese-ore
  - cmmmech:metalliferous-black-shale
  - cmmmech:monazite-ore
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickeline-bearing-ore
  - cmmmech:oxidized-zinc-ore
  - cmmmech:polymetallic-nodules
  - cmmmech:rare-earth-rich-deep-sea-mud
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:seawater
  - cmmmech:silica-sand
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - ev-primary-resource-cohort-audit
  - ev-schmitz2025-allanite-graph
  summary: 31/31 primary_resource records carry primary-source-supported mechanisms
    (40 microbial and 2 abiotic mechanisms across 31 records), and 16/31 carry causal_graphs
    (17 graphs) grounded to 46 unique UniProtKB accessions. Identified 1 minor graph
    finding on cmmmech:allanite-concentrate.
findings:
- finding_id: cmmmech-cycle13-stage4-finding-0003
  issue_key: cmmmech.schmitz-marecos-gluconobacter-graphs.template-pqqc-gdh-nodes-edges-and-relative-denominator-qualifications
  title: 'Gluconobacter oxydans B58 causal graphs and protein examples in allanite-concentrate.yaml,
    fluorescent-lamp-phosphor.yaml, and neodymium.yaml retain template PqqC/Gdh descriptions
    and supports: support polarity omitting 621H proxy grounding, residual mutant
    leaching, and relative extraction denominators'
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:allanite-concentrate
  field_paths:
  - mechanisms[0].protein_examples[3].evidence[0].supports
  - mechanisms[0].protein_examples[3].evidence[0].explanation
  - mechanisms[0].protein_examples[4].evidence[0].supports
  - mechanisms[0].protein_examples[4].evidence[0].explanation
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].evidence[0].supports
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].evidence[0].supports
  - causal_graphs[0].edges[3].evidence[0].explanation
  - causal_graphs[0].edges[4].evidence[0].supports
  - causal_graphs[0].edges[4].evidence[0].explanation
  evidence_ids:
  - ev-primary-resource-cohort-audit
  - ev-schmitz2025-allanite-graph
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
    no-bacteria rows in Supplementary Data 4A of marecos2025). In this scope, 1 record(s)
    (allanite-concentrate) are affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
actions:
- action_id: act-refine-schmitz-marecos-gluconobacter-graphs-and-proteins
  finding_ids:
  - cmmmech-cycle13-stage4-finding-0003
  target_ids:
  - cmmmech:allanite-concentrate
  description: 'Update protein_examples and causal_graphs[0] nodes/edges across data/records/allanite-concentrate.yaml,
    data/records/fluorescent-lamp-phosphor.yaml, and data/records/neodymium.yaml to
    supports: partial with study-specific prose documenting 621H reference-proteome
    proxy grounding for strain B58, residual mgdh/pqqC mutant leaching and non-pH
    mutant effects, relative-over-wild-type vs absolute-recovery denominators, and
    study-specific timing/control caveats during Stage 5 grouped remediation with
    canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  acceptance_checks:
  - 'mechanisms[].protein_examples and causal_graphs[0].nodes[].protein_examples across
    allanite-concentrate.yaml, fluorescent-lamp-phosphor.yaml, and neodymium.yaml
    are byte-identical with supports: partial and study-specific prose.'
  - 'causal_graphs[0].nodes and edges across all 3 records replace template PqqC/Gdh/biolixiviant
    text with study-specific conditions, relative denominators, and control caveats
    with supports: partial.'
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-primary-resource-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'primary_resource')
  locator: 31 primary_resource YAML files
  accessed_at: '2026-11-10T08:50:04Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 31 primary_resource records
    at commit 01de2d17fc49adec7f67da17266cbc82713d0df1.
- evidence_id: ev-schmitz2025-allanite-graph
  kind: record_content
  reference: data/records/allanite-concentrate.yaml
  locator: mechanisms[0] (lines 35-180); causal_graphs[0] (lines 182-398)
  accessed_at: '2026-11-10T08:50:04Z'
  support: supports
  summary: 'In data/records/allanite-concentrate.yaml, Gluconobacter oxydans B58 PqqC/Gdh
    protein_examples[3..4] and causal_graphs[0] nodes/edges retain template 72-130
    char descriptions and supports: support polarity omitting 621H proxy grounding,
    24 h vs 36 h pH timing discrepancy, relative 53.1%/73.1% denominators, and Figure
    S2 nitric-acid comparator caveats.'
limitations:
- 2 of 31 primary_resource records (eudialyte-concentrate and ludwigite-ore) currently
  carry abiotic acid/hydrometallurgical baseline mechanisms without published microbial
  bioleaching counterparts.
- 13 of 31 primary_resource records (13 of 29 with microbial mechanisms) have microbial
  mechanisms that do not yet have multi-node enzymatic causal graphs.
notes:
- Cohort covers 100% (31/31) of primary_resource cohort records at commit 01de2d17fc49adec7f67da17266cbc82713d0df1.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:basalt
  - cmmmech:carbonatite-associated-rare-earth-ore
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:cobalt-rich-ferromanganese-crusts
  - cmmmech:dunite
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:eucrite-meteorite
  - cmmmech:eudialyte-concentrate
  - cmmmech:eudialyte-ore
  - cmmmech:ion-adsorption-rare-earth-clay
  - cmmmech:kaolin
  - cmmmech:l-chondrite-meteorite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:ludwigite-ore
  - cmmmech:manganese-ore
  - cmmmech:metalliferous-black-shale
  - cmmmech:monazite-ore
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickeline-bearing-ore
  - cmmmech:oxidized-zinc-ore
  - cmmmech:polymetallic-nodules
  - cmmmech:rare-earth-rich-deep-sea-mud
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:seawater
  - cmmmech:silica-sand
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:xenotime-concentrate
  rationale: All 31 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where material_kind == 'primary_resource' at 01de2d17fc49adec7f67da17266cbc82713d0df1
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-primary-resource-cohort-audit
```
