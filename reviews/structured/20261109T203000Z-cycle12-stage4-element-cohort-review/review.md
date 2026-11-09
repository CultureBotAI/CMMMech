# Cycle 12 Stage 4 full-cohort review: element records (66/66)

- Review: 20261109T203000Z-cycle12-stage4-element-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T20:20:00Z
- Finished UTC: 2026-11-09T20:30:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 66 element records in data/records/*.yaml at commit f145e25990270f79cb760bb68e900595df4d308c, including the Cycle 12 Stage 2 (PR #974) and Stage 3 (PR #976) causal-graph and UniProtKB grounding expansion on cmmmech:strontium (pasteurii_strontium_carbonate_ureolytic_graph grounded to Sporosarcina pasteurii UreABC P04173, Q9Z369, Q9Z370 and UreE Q9Z368) and verifying resolution of Cycle 11 Stage 4 finding 0003 on cmmmech:scandium (PR #970). Verified CHEBI identifiers, dated jurisdiction-scoped criticality entries across 64/66 records, primary-source-supported microbial mechanisms across 63/66 records (66 microbial mechanisms total, 0 abiotic), causal_graphs across 31/66 records (32 graphs, 61 GENE_OR_PROTEIN nodes: 58 GROUNDED across 30 records and 3 UNGROUNDED across cmmmech:erbium, cmmmech:gold, and cmmmech:terbium, plus UNGROUNDED nodes in manganese and praseodymium paired with GROUNDED nodes), and live-verified UniProtKB protein_examples across 30/31 records (58 unique accessions). Identified 2 minor graph findings across 2 element records (cmmmech-cycle12-stage4-finding-0002 on cmmmech:selenium and cmmmech-cycle12-stage4-finding-0003 on cmmmech:praseodymium) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 12 Stage 4 category review of all 66 element records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'element' at f145e25990270f79cb760bb68e900595df4d308c
Coverage: full; 66 reviewed / 66 in the declared population.
Source: git_commit at Git base f145e25990270f79cb760bb68e900595df4d308c.
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
| just validate (element cohort) | passed | True | cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium | All 66 element cohort records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (element cohort) | passed | True | cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium | All 66 element cohort records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### CHEBI identity, jurisdiction-scoped criticality, primary-source microbial mechanisms, and causal graphs

evidence: supported. Targets: cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium.

64/66 element records carry dated jurisdiction-scoped criticality assessments; 63/66 carry primary-source-supported microbial mechanisms (66 total); and 31/66 carry causal_graphs (32 graphs, 30 grounded to 58 unique UniProtKB accessions). Identified 2 minor graph findings on cmmmech:selenium and cmmmech:praseodymium.

## Findings

### cmmmech-cycle12-stage4-finding-0002: Selenium Shewanella oneidensis MR-1 FccA/CymA causal graph and protein examples use abbreviated one-line explanations and unqualified direct-catalysis / periplasmic-localization claims

minor / open / confirmed; issue key: cmmmech.li2014-selenium-mr1.abbreviated-graph-evidence-and-localization-catalysis-qualifications.

In data/records/selenium.yaml (cmmmech:selenium, element, Li et al. 2014 Scientific Reports 4:3735, DOI:10.1038/srep03735, li_2014 / li_2014_supplement, and Klonowska et al. 2005 Appl. Environ. Microbiol. 71:5607-5609, klonowska_2005; mechanisms[0] mr1_selenite_reduction, lines 40-135; causal_graphs[0] mr1_fcca_cyma_selenite_reduction_graph, lines 137-283), mechanisms[0].description (line 43) and mechanisms[0].evidence[0..1,3] (lines 124-135) explicitly establish that gene-deletion phenotypes in washed non-growing Shewanella oneidensis MR-1 suspensions (OD600 1.0 in 40 mL anaerobic mineral medium under N2 with 0.5 mM selenite and 20 mM lactate at 30 C; declining Micro BCA protein biomass in Figure S2/S4) support conditional FccA and CymA involvement rather than an exclusive pathway or direct catalysis by purified FccA (no complementation or purified-FccA enzyme assay is reported; initial 12 h selenite-depletion rate drops from 1.35 +/- 0.05 umol/h in WT to 0.54 +/- 0.13 umol/h in delta-fccA [Figure 2, triplicate SE], while Figure 4 preserves substantial later residual reduction in delta-cymA and klonowska_2005 reports selenite reduction by a cymA mutant in LB), and that 48 h TEM/EDX and Se 3d XPS (Figure 5) show predominantly intracellular plus smaller surface Se(0)-assigned particles rather than exclusive periplasmic localization or an isolated phase-pure product (Table 1 provides an acid-digestion/ICP-AES selenium balance). By contrast, in causal_graphs[0] and protein_examples: nodes[0].description (line 147, 81 chars), nodes[1].description (line 178, 90 chars), and edges[1].description (line 261) assert unqualified electron transfer and direct periplasmic catalysis ('FccA directly reduces soluble selenite in the periplasm.'); nodes[4].description (elemental_se0_nanoparticles, line 245, 85 chars) states 'Red elemental selenium nanoparticles accumulated in the periplasm and cell envelope.', omitting the predominantly intracellular plus surface particle distribution in Figure 5 TEM/EDX (and extracellular/cell-attached deposits at 2 mM selenite in LB in klonowska_2005 Figure 1); and edges[0..3] (lines 248-283) carry abbreviated 75-to-87-character one-sentence evidence[0].explanation strings with supports: support on edges[0], edges[1], and edges[3] (as well as protein_examples[0..1].evidence[0] on UniProtKB:P83223 and UniProtKB:Q8E8S0, lines 75, 99, 172, 206) despite the absence of complementation or purified-FccA assays, substantial residual reduction in delta-cymA, and mixed intracellular/surface localization. In this scope, 1 record(s) (selenium) are affected.

### cmmmech-cycle12-stage4-finding-0003: Immobilized-lanmodulin column causal graphs in praseodymium.yaml and rare-earth-element-commodities.yaml retain abbreviated node/edge explanations and omit replicate-batch, immobilized-dimer minority, and summed-eluate denominator caveats

minor / open / confirmed; issue key: cmmmech.diep2026-mattocks2023-lanmodulin-graphs.abbreviated-edge-evidence-and-batch-dimer-qualifications.

In data/records/praseodymium.yaml (cmmmech:praseodymium, element, Diep et al. 2026 Nature Chemical Biology 22:829-839, DOI:10.1038/s41589-026-02176-3, diep2026; causal_graphs[0] melba_mex_lanm_pr_la_separation_graph, lines 71-148) and data/records/rare-earth-element-commodities.yaml (cmmmech:rare-earth-element-commodities, commodity, Mattocks et al. 2023 Nature 618:87-93, DOI:10.1038/s41586-023-05945-5, mattocks_2023 / mattocks_2023_si / mattocks_2023_fig4_data; causal_graphs[0] hans_lanm_r100k_nd_dy_separation_graph, lines 101-198), immobilized-lanmodulin causal-graph nodes and edges retain abbreviated 71-to-119-character descriptions and evidence explanations that omit key experimental parameters and partial-support caveats documented in mechanisms[0]: (1) in praseodymium.yaml, nodes[2].description (equimolar_pr_la_feed, line 114, 86 chars) and nodes[3].description (resolved_pr3_eluate, line 119, 77 chars) omit the 0.8 mL agarose column (0.5 x 5 cm, pre-equilibrated with 10 mM glycine pH 3.0), 0.4 mM Pr(III) + 0.4 mM La(III) synthetic binary feed (loaded 2 min at ~0.32 mL/min, 10% capacity), pH 2.4 (140 min) then pH 1.5 (25 min) elution, and the single-run Figure 6d Pr fraction result (99.97 mol% Pr purity / 83.16% fraction recovery across bed volumes 48-80) versus the three independent 0.4 mL repeat columns with a new protein batch at pH 2.5 then pH 1.5 (96.5 +/- 0.2 mol% Pr purity and 72.0 +/- 5.8% yield across fractions 53-93 in Extended Data Figure 8d), while edges[0..2] (lines 122-148) carry 82-to-87-character evidence[0].explanation strings with supports: support on edges[0] and edges[2] that omit the Extended Data Figure 8d batch/scale conditionality, the summed-eluate denominator in Source Data Figure 6 (sheet o36 Agarose La-Pr) rather than an independent feed-to-product mass balance, and comparator Mex-LanM (o-621) co-elution of Pr and La; and (2) in rare-earth-element-commodities.yaml, mechanisms[0].protein_examples[0].evidence[0] (lines 63-65), nodes[0].protein_examples[0].evidence[0] (lines 130-132), and edges[0] (lines 172-180, 119-char explanation) assert supports: support and cooperative dimer/EF-hand discrimination without the qualification in mechanisms[0].evidence[1] (lines 92-93, supports: partial) that Page 92 and Extended Data Figure 6 explicitly distinguish solution dimerization from column behavior because functional dimers may occur in only a minority of immobilized protein units and no bare-agarose control is reported, edges[1].evidence[0].explanation (line 189, 71 chars) omits the Extended Data Figure 6 wild-type Hans-LanM (83.6% Dy purity / 98.1% yield; 99.8% Nd purity / 98.5% yield) and monomeric Mex-LanM comparisons, and edges[2].evidence[0] (lines 196-198) asserts supports: support without noting the mattocks_2023_fig4_data summed-eluate yield denominator (SUM(H32:H43)/SUM(H32:H51) = 99.3964% vs printed 99.3% for Dy; SUM(G44:G51)/SUM(G32:G51) = 99.8% for Nd), binary molar-share purity definition, and Table S16 vs workbook Nd SD discrepancy (4.4 vs ~15.1942) documented in mechanisms[0].evidence[0,3]. In this scope, 1 record(s) (praseodymium) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-li2014-selenium-mr1-graph-and-protein-evidence

Update mechanisms[0].protein_examples[0..1].evidence[0] and causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0] (UniProtKB:P83223 FccA and UniProtKB:Q8E8S0 CymA) in data/records/selenium.yaml to supports: partial with synchronized deletion-mutant kinetic prose (0.54 +/- 0.13 vs 1.35 +/- 0.05 umol/h in Figure 2; 20 mM fumarate competition; residual delta-cymA reduction in Figure 4 and klonowska_2005; no complementation or purified-FccA assay), expand nodes[0..4].description to reflect non-growing washed-cell conditions and predominantly intracellular plus surface Se(0)-assigned particles (Figure 5 TEM/EDX, 48 h Se 3d XPS, Table 1 ICP-AES balance), and expand edges[0..3] (setting edges[0], edges[1], and edges[3] to supports: partial) during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0..1] and causal_graphs[0].nodes[0..1].protein_examples[0] in selenium.yaml are byte-identical with supports: partial and study-specific kinetic/control prose.
- causal_graphs[0].nodes[0..4].description and edges[0..3] in selenium.yaml align with mechanisms[0].evidence[0..3] and use supports: partial on edges[0..3].
- Matching EDIT history sidecar exists in history/records/selenium/ and passes just check.

### act-refine-diep2026-mattocks2023-lanmodulin-column-graphs

Update data/records/praseodymium.yaml (nodes[2..3] and edges[0..2], setting edges[0] and edges[2] to supports: partial) and data/records/rare-earth-element-commodities.yaml (mechanisms[0].protein_examples[0].evidence[0], nodes[0].protein_examples[0].evidence[0], and edges[0..2], setting protein_examples[0], edges[0], and edges[2] to supports: partial) so that node descriptions and edge evidence explanations incorporate full column parameters, replicate-column/batch variance (Extended Data Figure 8d in diep2026), immobilized-dimer minority and bare-agarose control caveats (Page 92 and Extended Data Figure 6 in mattocks_2023), and summed-eluate yield denominator / binary molar-share purity qualifications during Stage 5 grouped remediation with canonical history provenance.

- praseodymium.yaml causal_graphs[0].nodes[2..3] and edges[0..2] specify the 0.8 mL vs 0.4 mL column parameters, Figure 6d vs Extended Data Figure 8d Pr purity/yield metrics, and summed-eluate denominator with supports: partial on edges[0..2].
- rare-earth-element-commodities.yaml mechanisms[0].protein_examples[0], causal_graphs[0].nodes[0].protein_examples[0], and causal_graphs[0].edges[0..2] are synchronized with supports: partial and include the Page 92 immobilized-dimer minority, Extended Data Figure 6 wild-type comparator, and mattocks_2023_fig4_data summed-eluate denominator caveats.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:aluminium, cmmmech:antimony, cmmmech:arsenic, cmmmech:beryllium, cmmmech:bismuth, cmmmech:boron, cmmmech:cadmium, cmmmech:cerium, cmmmech:cesium, cmmmech:chromium, cmmmech:cobalt, cmmmech:copper, cmmmech:dysprosium, cmmmech:erbium, cmmmech:europium, cmmmech:fluorine, cmmmech:gadolinium, cmmmech:gallium, cmmmech:germanium, cmmmech:gold, cmmmech:hafnium, cmmmech:helium, cmmmech:holmium, cmmmech:indium, cmmmech:iridium, cmmmech:iron, cmmmech:lanthanum, cmmmech:lead, cmmmech:lithium, cmmmech:lutetium, cmmmech:magnesium, cmmmech:manganese, cmmmech:molybdenum, cmmmech:neodymium, cmmmech:nickel, cmmmech:niobium, cmmmech:osmium, cmmmech:palladium, cmmmech:phosphorus, cmmmech:platinum, cmmmech:praseodymium, cmmmech:promethium, cmmmech:rhenium, cmmmech:rhodium, cmmmech:rubidium, cmmmech:ruthenium, cmmmech:samarium, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:strontium, cmmmech:tantalum, cmmmech:tellurium, cmmmech:terbium, cmmmech:thallium, cmmmech:thulium, cmmmech:tin, cmmmech:titanium, cmmmech:tungsten, cmmmech:uranium, cmmmech:vanadium, cmmmech:ytterbium, cmmmech:yttrium, cmmmech:zinc, cmmmech:zirconium. All 66 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'element' at f145e25990270f79cb760bb68e900595df4d308c with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-element-cohort-audit | data/records/*.yaml (material_kind == 'element'); 66 element YAML files | supports | Full programmatic and source-backed audit of all 66 element records at commit f145e25990270f79cb760bb68e900595df4d308c. |
| ev-li2014-selenium-graph | data/records/selenium.yaml; mechanisms[0] (lines 40-135); causal_graphs[0] (lines 137-283) | supports | In data/records/selenium.yaml, causal_graphs[0] and protein_examples[0..1] use abbreviated 75-90 char explanations and supports: support stating direct periplasmic FccA catalysis and periplasmic/cell-envelope Se(0) accumulation, omitting conditional deletion kinetics, absence of complementation/purified-FccA assays, residual delta-cymA reduction, and predominantly intracellular plus surface particle distribution. |
| ev-diep2026-praseodymium-graph | data/records/praseodymium.yaml; mechanisms[0] (lines 32-69); causal_graphs[0] (lines 71-148) | supports | In data/records/praseodymium.yaml, causal_graphs[0].nodes[2..3] and edges[0..2] retain 77-87 char strings and supports: support on edges[0,2] omitting the 0.8 mL vs 0.4 mL repeat-column variance (Figure 6d vs Extended Data Figure 8d), summed-eluate yield denominator, and Mex-LanM co-elution. |

## Limits And Additional Notes

- 3 of 66 element records (beryllium, helium, promethium) currently lack published microbial extraction, bioleaching, or biotransformation mechanism entries in the corpus.
- Cohort covers 100% (66/66) of element records in data/records/*.yaml at commit f145e25990270f79cb760bb68e900595df4d308c.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T203000Z-cycle12-stage4-element-cohort-review
title: 'Cycle 12 Stage 4 full-cohort review: element records (66/66)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-09T20:20:00Z'
finished_at: '2026-11-09T20:30:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 66 element records in data/records/*.yaml at commit f145e25990270f79cb760bb68e900595df4d308c,
  including the Cycle 12 Stage 2 (PR #974) and Stage 3 (PR #976) causal-graph and
  UniProtKB grounding expansion on cmmmech:strontium (pasteurii_strontium_carbonate_ureolytic_graph
  grounded to Sporosarcina pasteurii UreABC P04173, Q9Z369, Q9Z370 and UreE Q9Z368)
  and verifying resolution of Cycle 11 Stage 4 finding 0003 on cmmmech:scandium (PR
  #970). Verified CHEBI identifiers, dated jurisdiction-scoped criticality entries
  across 64/66 records, primary-source-supported microbial mechanisms across 63/66
  records (66 microbial mechanisms total, 0 abiotic), causal_graphs across 31/66 records
  (32 graphs, 61 GENE_OR_PROTEIN nodes: 58 GROUNDED across 30 records and 3 UNGROUNDED
  across cmmmech:erbium, cmmmech:gold, and cmmmech:terbium, plus UNGROUNDED nodes
  in manganese and praseodymium paired with GROUNDED nodes), and live-verified UniProtKB
  protein_examples across 30/31 records (58 unique accessions). Identified 2 minor
  graph findings across 2 element records (cmmmech-cycle12-stage4-finding-0002 on
  cmmmech:selenium and cmmmech-cycle12-stage4-finding-0003 on cmmmech:praseodymium)
  for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 12 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit f145e25990270f79cb760bb68e900595df4d308c.
source:
  git_revision: f145e25990270f79cb760bb68e900595df4d308c
  state: git_commit
  inputs:
  - path: data/records/aluminium.yaml
    sha256: 8df6aa9f1e6f6b4fdb637c4026cfef6781c286c847e25153d0c126a67503fe13
    role: target
  - path: data/records/antimony.yaml
    sha256: 3854163557ef588e4d570f71e6939b406bef24763d31332afe0741400cd91576
    role: target
  - path: data/records/arsenic.yaml
    sha256: db6cce965d9da92e0e467a658aba89650641a2f2d085acc9235c9302c2a082d8
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
    sha256: 2fa5feef5344357886d087965aac5b3449a68d07159aebd07638a085993c1eac
    role: target
  - path: data/records/cobalt.yaml
    sha256: c37b06ec07bc1e4af7289dc770f3711658ea05a948e22c91b12f6b00130f7037
    role: target
  - path: data/records/copper.yaml
    sha256: df7bd558794467c52b776f58a78c64ce12c3cb2da1cbd0da91e192b971da7078
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
    sha256: ee9aa739bd3c1d87873ba882935859f09e622c6bad8fbd9d3034d91ddc40fe87
    role: target
  - path: data/records/germanium.yaml
    sha256: ab9184e4e7eed9507d67309937e872c7218a5b534acbb7e09eff8036a8e10c05
    role: target
  - path: data/records/gold.yaml
    sha256: 3041e16eaa6cdd500a1784cd9c2461511e0c98e37d218bc29abe56b3c4375bb4
    role: target
  - path: data/records/hafnium.yaml
    sha256: 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb
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
    sha256: 507b7705fc18b95088e50612586b338370de697b8ed6093d3d74f546b8d90f07
    role: target
  - path: data/records/lutetium.yaml
    sha256: f9881645329d9d18e925a12ca8b858b78a3fec1b806caa37ce465acdabf162fe
    role: target
  - path: data/records/magnesium.yaml
    sha256: ab57bc5464af299e10481a8a56f0f4161e6bc10cbac35852b82e63caf677ccc2
    role: target
  - path: data/records/manganese.yaml
    sha256: 3d9d759613d889fdf23a6bbb16f35b1ace1f36eed87f39add5a5879992d24906
    role: target
  - path: data/records/molybdenum.yaml
    sha256: 8b6b2790848a967492ed00d204d6f64835cd8ebd2a437a4753715f4e2567d39d
    role: target
  - path: data/records/neodymium.yaml
    sha256: 91a74a542eb1dbd45aeb4cbd24f3ced3f382854dc7e7e3d2292effcded89341f
    role: target
  - path: data/records/nickel.yaml
    sha256: 2a4e328318bd222655d17d447cbd3a4ab187293fcc5328b5c2fdca2b976e8bfc
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
    sha256: 2aeae056f98b9571f9c38cf6bd1fb7249db9217c5f750f3de01c93b9bc594545
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
    sha256: 76ae7bf5070596859d74737c8a4fcb3544b08278d8ff2b3ed1f9d8a9675b10bc
    role: target
  - path: data/records/selenium.yaml
    sha256: 3c88fca92fd61d7c2c88981eb4497eb71b0d4af4bfa8f2d1acd062735d59fca9
    role: target
  - path: data/records/silicon.yaml
    sha256: f6ac021b6e80e90cae837fcf9726aef132444f34e00cdb368c1fc6c8ef21275a
    role: target
  - path: data/records/silver.yaml
    sha256: 9e526e8db6b270c515116cb1e3f3adfa9800f1184cf5d5740575a1cf1ce4cfc0
    role: target
  - path: data/records/strontium.yaml
    sha256: 707127cf033ec918fba7e3ca97676521c51afcc8848ad38a577a50941f9c14b8
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
    sha256: 0183150b963b97fb4331893297061086fdd168bd0c27027f651101233153b260
    role: target
  - path: data/records/thulium.yaml
    sha256: d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62
    role: target
  - path: data/records/tin.yaml
    sha256: 138bd40ed9bfb255a13f2f7d3b9997c7e919f34282893d16c18d0bcc3d7e4d19
    role: target
  - path: data/records/titanium.yaml
    sha256: 189a9821197d4a2efa9bed95505c51c6b01bc211b08a6599fc2e3ffc17b8ec95
    role: target
  - path: data/records/tungsten.yaml
    sha256: d87ad7f8783feba23aace69512babacfd006e26190e49196d446b9b9c7bc40fa
    role: target
  - path: data/records/uranium.yaml
    sha256: 02fb0f5a817a13f868dd9ebd0751021f279eafce8f30d7ee618c47f91bfb468e
    role: target
  - path: data/records/vanadium.yaml
    sha256: 0537c316f2f345b570468c97cc79b51bc447585f80a64858f3d7dace6d227c47
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
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
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
  selection: data/records/*.yaml where material_kind == 'element' at f145e25990270f79cb760bb68e900595df4d308c
  description: Full-population Cycle 12 Stage 4 category review of all 66 element
    records in CMMMech.
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
- check_id: just-validate-elements
  name: just validate (element cohort)
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
  summary: All 66 element cohort records pass LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-elements
  name: just verify-history (element cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
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
  summary: All 66 element cohort records have intact append-only history sidecars
    and matching curation_history metadata.
assessments:
- assessment_id: assess-element-identity-criticality-and-mechanisms
  topic: CHEBI identity, jurisdiction-scoped criticality, primary-source microbial
    mechanisms, and causal graphs
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
  - ev-li2014-selenium-graph
  - ev-diep2026-praseodymium-graph
  summary: 64/66 element records carry dated jurisdiction-scoped criticality assessments;
    63/66 carry primary-source-supported microbial mechanisms (66 total); and 31/66
    carry causal_graphs (32 graphs, 30 grounded to 58 unique UniProtKB accessions).
    Identified 2 minor graph findings on cmmmech:selenium and cmmmech:praseodymium.
findings:
- finding_id: cmmmech-cycle12-stage4-finding-0002
  issue_key: cmmmech.li2014-selenium-mr1.abbreviated-graph-evidence-and-localization-catalysis-qualifications
  title: Selenium Shewanella oneidensis MR-1 FccA/CymA causal graph and protein examples
    use abbreviated one-line explanations and unqualified direct-catalysis / periplasmic-localization
    claims
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:selenium
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - mechanisms[0].protein_examples[1].evidence[0].supports
  - mechanisms[0].protein_examples[1].evidence[0].explanation
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].nodes[4].description
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].description
  - causal_graphs[0].edges[3].evidence[0].supports
  - causal_graphs[0].edges[3].evidence[0].explanation
  evidence_ids:
  - ev-element-cohort-audit
  - ev-li2014-selenium-graph
  description: 'In data/records/selenium.yaml (cmmmech:selenium, element, Li et al.
    2014 Scientific Reports 4:3735, DOI:10.1038/srep03735, li_2014 / li_2014_supplement,
    and Klonowska et al. 2005 Appl. Environ. Microbiol. 71:5607-5609, klonowska_2005;
    mechanisms[0] mr1_selenite_reduction, lines 40-135; causal_graphs[0] mr1_fcca_cyma_selenite_reduction_graph,
    lines 137-283), mechanisms[0].description (line 43) and mechanisms[0].evidence[0..1,3]
    (lines 124-135) explicitly establish that gene-deletion phenotypes in washed non-growing
    Shewanella oneidensis MR-1 suspensions (OD600 1.0 in 40 mL anaerobic mineral medium
    under N2 with 0.5 mM selenite and 20 mM lactate at 30 C; declining Micro BCA protein
    biomass in Figure S2/S4) support conditional FccA and CymA involvement rather
    than an exclusive pathway or direct catalysis by purified FccA (no complementation
    or purified-FccA enzyme assay is reported; initial 12 h selenite-depletion rate
    drops from 1.35 +/- 0.05 umol/h in WT to 0.54 +/- 0.13 umol/h in delta-fccA [Figure
    2, triplicate SE], while Figure 4 preserves substantial later residual reduction
    in delta-cymA and klonowska_2005 reports selenite reduction by a cymA mutant in
    LB), and that 48 h TEM/EDX and Se 3d XPS (Figure 5) show predominantly intracellular
    plus smaller surface Se(0)-assigned particles rather than exclusive periplasmic
    localization or an isolated phase-pure product (Table 1 provides an acid-digestion/ICP-AES
    selenium balance). By contrast, in causal_graphs[0] and protein_examples: nodes[0].description
    (line 147, 81 chars), nodes[1].description (line 178, 90 chars), and edges[1].description
    (line 261) assert unqualified electron transfer and direct periplasmic catalysis
    (''FccA directly reduces soluble selenite in the periplasm.''); nodes[4].description
    (elemental_se0_nanoparticles, line 245, 85 chars) states ''Red elemental selenium
    nanoparticles accumulated in the periplasm and cell envelope.'', omitting the
    predominantly intracellular plus surface particle distribution in Figure 5 TEM/EDX
    (and extracellular/cell-attached deposits at 2 mM selenite in LB in klonowska_2005
    Figure 1); and edges[0..3] (lines 248-283) carry abbreviated 75-to-87-character
    one-sentence evidence[0].explanation strings with supports: support on edges[0],
    edges[1], and edges[3] (as well as protein_examples[0..1].evidence[0] on UniProtKB:P83223
    and UniProtKB:Q8E8S0, lines 75, 99, 172, 206) despite the absence of complementation
    or purified-FccA assays, substantial residual reduction in delta-cymA, and mixed
    intracellular/surface localization. In this scope, 1 record(s) (selenium) are
    affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
- finding_id: cmmmech-cycle12-stage4-finding-0003
  issue_key: cmmmech.diep2026-mattocks2023-lanmodulin-graphs.abbreviated-edge-evidence-and-batch-dimer-qualifications
  title: Immobilized-lanmodulin column causal graphs in praseodymium.yaml and rare-earth-element-commodities.yaml
    retain abbreviated node/edge explanations and omit replicate-batch, immobilized-dimer
    minority, and summed-eluate denominator caveats
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:praseodymium
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].supports
  - causal_graphs[0].edges[2].evidence[0].explanation
  evidence_ids:
  - ev-element-cohort-audit
  - ev-diep2026-praseodymium-graph
  description: 'In data/records/praseodymium.yaml (cmmmech:praseodymium, element,
    Diep et al. 2026 Nature Chemical Biology 22:829-839, DOI:10.1038/s41589-026-02176-3,
    diep2026; causal_graphs[0] melba_mex_lanm_pr_la_separation_graph, lines 71-148)
    and data/records/rare-earth-element-commodities.yaml (cmmmech:rare-earth-element-commodities,
    commodity, Mattocks et al. 2023 Nature 618:87-93, DOI:10.1038/s41586-023-05945-5,
    mattocks_2023 / mattocks_2023_si / mattocks_2023_fig4_data; causal_graphs[0] hans_lanm_r100k_nd_dy_separation_graph,
    lines 101-198), immobilized-lanmodulin causal-graph nodes and edges retain abbreviated
    71-to-119-character descriptions and evidence explanations that omit key experimental
    parameters and partial-support caveats documented in mechanisms[0]: (1) in praseodymium.yaml,
    nodes[2].description (equimolar_pr_la_feed, line 114, 86 chars) and nodes[3].description
    (resolved_pr3_eluate, line 119, 77 chars) omit the 0.8 mL agarose column (0.5
    x 5 cm, pre-equilibrated with 10 mM glycine pH 3.0), 0.4 mM Pr(III) + 0.4 mM La(III)
    synthetic binary feed (loaded 2 min at ~0.32 mL/min, 10% capacity), pH 2.4 (140
    min) then pH 1.5 (25 min) elution, and the single-run Figure 6d Pr fraction result
    (99.97 mol% Pr purity / 83.16% fraction recovery across bed volumes 48-80) versus
    the three independent 0.4 mL repeat columns with a new protein batch at pH 2.5
    then pH 1.5 (96.5 +/- 0.2 mol% Pr purity and 72.0 +/- 5.8% yield across fractions
    53-93 in Extended Data Figure 8d), while edges[0..2] (lines 122-148) carry 82-to-87-character
    evidence[0].explanation strings with supports: support on edges[0] and edges[2]
    that omit the Extended Data Figure 8d batch/scale conditionality, the summed-eluate
    denominator in Source Data Figure 6 (sheet o36 Agarose La-Pr) rather than an independent
    feed-to-product mass balance, and comparator Mex-LanM (o-621) co-elution of Pr
    and La; and (2) in rare-earth-element-commodities.yaml, mechanisms[0].protein_examples[0].evidence[0]
    (lines 63-65), nodes[0].protein_examples[0].evidence[0] (lines 130-132), and edges[0]
    (lines 172-180, 119-char explanation) assert supports: support and cooperative
    dimer/EF-hand discrimination without the qualification in mechanisms[0].evidence[1]
    (lines 92-93, supports: partial) that Page 92 and Extended Data Figure 6 explicitly
    distinguish solution dimerization from column behavior because functional dimers
    may occur in only a minority of immobilized protein units and no bare-agarose
    control is reported, edges[1].evidence[0].explanation (line 189, 71 chars) omits
    the Extended Data Figure 6 wild-type Hans-LanM (83.6% Dy purity / 98.1% yield;
    99.8% Nd purity / 98.5% yield) and monomeric Mex-LanM comparisons, and edges[2].evidence[0]
    (lines 196-198) asserts supports: support without noting the mattocks_2023_fig4_data
    summed-eluate yield denominator (SUM(H32:H43)/SUM(H32:H51) = 99.3964% vs printed
    99.3% for Dy; SUM(G44:G51)/SUM(G32:G51) = 99.8% for Nd), binary molar-share purity
    definition, and Table S16 vs workbook Nd SD discrepancy (4.4 vs ~15.1942) documented
    in mechanisms[0].evidence[0,3]. In this scope, 1 record(s) (praseodymium) are
    affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/praseodymium.yaml
    role: maintained_record
actions:
- action_id: act-refine-li2014-selenium-mr1-graph-and-protein-evidence
  finding_ids:
  - cmmmech-cycle12-stage4-finding-0002
  target_ids:
  - cmmmech:selenium
  description: 'Update mechanisms[0].protein_examples[0..1].evidence[0] and causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0]
    (UniProtKB:P83223 FccA and UniProtKB:Q8E8S0 CymA) in data/records/selenium.yaml
    to supports: partial with synchronized deletion-mutant kinetic prose (0.54 +/-
    0.13 vs 1.35 +/- 0.05 umol/h in Figure 2; 20 mM fumarate competition; residual
    delta-cymA reduction in Figure 4 and klonowska_2005; no complementation or purified-FccA
    assay), expand nodes[0..4].description to reflect non-growing washed-cell conditions
    and predominantly intracellular plus surface Se(0)-assigned particles (Figure
    5 TEM/EDX, 48 h Se 3d XPS, Table 1 ICP-AES balance), and expand edges[0..3] (setting
    edges[0], edges[1], and edges[3] to supports: partial) during Stage 5 grouped
    remediation with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  acceptance_checks:
  - 'mechanisms[0].protein_examples[0..1] and causal_graphs[0].nodes[0..1].protein_examples[0]
    in selenium.yaml are byte-identical with supports: partial and study-specific
    kinetic/control prose.'
  - 'causal_graphs[0].nodes[0..4].description and edges[0..3] in selenium.yaml align
    with mechanisms[0].evidence[0..3] and use supports: partial on edges[0..3].'
  - Matching EDIT history sidecar exists in history/records/selenium/ and passes just
    check.
- action_id: act-refine-diep2026-mattocks2023-lanmodulin-column-graphs
  finding_ids:
  - cmmmech-cycle12-stage4-finding-0003
  target_ids:
  - cmmmech:praseodymium
  description: 'Update data/records/praseodymium.yaml (nodes[2..3] and edges[0..2],
    setting edges[0] and edges[2] to supports: partial) and data/records/rare-earth-element-commodities.yaml
    (mechanisms[0].protein_examples[0].evidence[0], nodes[0].protein_examples[0].evidence[0],
    and edges[0..2], setting protein_examples[0], edges[0], and edges[2] to supports:
    partial) so that node descriptions and edge evidence explanations incorporate
    full column parameters, replicate-column/batch variance (Extended Data Figure
    8d in diep2026), immobilized-dimer minority and bare-agarose control caveats (Page
    92 and Extended Data Figure 6 in mattocks_2023), and summed-eluate yield denominator
    / binary molar-share purity qualifications during Stage 5 grouped remediation
    with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/praseodymium.yaml
    role: maintained_record
  acceptance_checks:
  - 'praseodymium.yaml causal_graphs[0].nodes[2..3] and edges[0..2] specify the 0.8
    mL vs 0.4 mL column parameters, Figure 6d vs Extended Data Figure 8d Pr purity/yield
    metrics, and summed-eluate denominator with supports: partial on edges[0..2].'
  - 'rare-earth-element-commodities.yaml mechanisms[0].protein_examples[0], causal_graphs[0].nodes[0].protein_examples[0],
    and causal_graphs[0].edges[0..2] are synchronized with supports: partial and include
    the Page 92 immobilized-dimer minority, Extended Data Figure 6 wild-type comparator,
    and mattocks_2023_fig4_data summed-eluate denominator caveats.'
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-element-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'element')
  locator: 66 element YAML files
  accessed_at: '2026-11-09T20:30:00Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 66 element records at
    commit f145e25990270f79cb760bb68e900595df4d308c.
- evidence_id: ev-li2014-selenium-graph
  kind: record_content
  reference: data/records/selenium.yaml
  locator: mechanisms[0] (lines 40-135); causal_graphs[0] (lines 137-283)
  accessed_at: '2026-11-09T20:30:00Z'
  support: supports
  summary: 'In data/records/selenium.yaml, causal_graphs[0] and protein_examples[0..1]
    use abbreviated 75-90 char explanations and supports: support stating direct periplasmic
    FccA catalysis and periplasmic/cell-envelope Se(0) accumulation, omitting conditional
    deletion kinetics, absence of complementation/purified-FccA assays, residual delta-cymA
    reduction, and predominantly intracellular plus surface particle distribution.'
- evidence_id: ev-diep2026-praseodymium-graph
  kind: record_content
  reference: data/records/praseodymium.yaml
  locator: mechanisms[0] (lines 32-69); causal_graphs[0] (lines 71-148)
  accessed_at: '2026-11-09T20:30:00Z'
  support: supports
  summary: 'In data/records/praseodymium.yaml, causal_graphs[0].nodes[2..3] and edges[0..2]
    retain 77-87 char strings and supports: support on edges[0,2] omitting the 0.8
    mL vs 0.4 mL repeat-column variance (Figure 6d vs Extended Data Figure 8d), summed-eluate
    yield denominator, and Mex-LanM co-elution.'
limitations:
- 3 of 66 element records (beryllium, helium, promethium) currently lack published
  microbial extraction, bioleaching, or biotransformation mechanism entries in the
  corpus.
notes:
- Cohort covers 100% (66/66) of element records in data/records/*.yaml at commit f145e25990270f79cb760bb68e900595df4d308c.
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
    matching data/records/*.yaml where material_kind == 'element' at f145e25990270f79cb760bb68e900595df4d308c
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-element-cohort-audit
```
