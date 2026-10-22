# Cycle 2 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (89/89)

- Review: 20261022T115006Z-cycle2-stage4-causal-graphs-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T11:46:00Z
- Finished UTC: 2026-10-22T11:50:06Z
- Reviewer: antigravity / cmmmech-cycle2-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 89 records with multi-step causal_graphs at commit 547283a882c1d657f934434f2eb5ea9a1418771a (20 element, 44 mineral, 2 mineral_group, 4 commodity, 7 primary_resource, 12 secondary_resource; 94 causal graphs, 410 nodes, 316 edges, 143 GROUNDED and 6 source-limited UNGROUNDED GENE_OR_PROTEIN nodes; 86 records with 177 protein_examples across 50 unique UniProtKB accessions). Verified 100% connectedness and DAG acyclicity, 100% edge evidence coverage with verbatim primary-source snippets, and 100% UniProtKB accession/label/organism/domain synchronization between mechanism-level and node-level protein_examples. Recorded one minor consistency finding (cmmmech-cycle2-stage4-finding-0002) on cmmmech:allanite-concentrate and cmmmech:thulium where node-level protein_examples[].evidence[].explanation strings are slightly abbreviated relative to mechanism-level protein_examples[].evidence[].explanation strings (and see companion single-record review 20261022T115007Z-katsarosite-cycle2-stage4-record-review for cmmmech-cycle2-stage4-finding-0003 on cmmmech:katsarosite).

## Scope And Provenance

Full-population Cycle 2 Stage 4 category review of all 89 CMMMech records carrying multi-step causal_graphs (94 graphs, 410 nodes, 316 edges) and UniProtKB protein_examples (86 records, 177 protein_examples across 50 unique UniProtKB accessions).

Selection: data/records/*.yaml where causal_graphs is non-empty at 547283a882c1d657f934434f2eb5ea9a1418771a
Coverage: full; 89 reviewed / 89 in the declared population.
Source: git_commit at Git base 547283a882c1d657f934434f2eb5ea9a1418771a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:allanite-leachate | data/records/allanite-leachate.yaml | maintained | Allanite-derived rare-earth leachate |
| cmmmech:aluminium | data/records/aluminium.yaml | maintained | Aluminium |
| cmmmech:anatase | data/records/anatase.yaml | maintained | Anatase |
| cmmmech:asbolane | data/records/asbolane.yaml | maintained | Asbolane |
| cmmmech:bauxite-residue | data/records/bauxite-residue.yaml | maintained | Bauxite residue (red mud) |
| cmmmech:birnessite | data/records/birnessite.yaml | maintained | Birnessite |
| cmmmech:bixbyite-mn | data/records/bixbyite-mn.yaml | maintained | Bixbyite-(Mn) |
| cmmmech:borates | data/records/borates.yaml | maintained | Borates |
| cmmmech:brushite | data/records/brushite.yaml | maintained | Brushite |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |
| cmmmech:cerium | data/records/cerium.yaml | maintained | Cerium |
| cmmmech:cerussite | data/records/cerussite.yaml | maintained | Cerussite |
| cmmmech:chlorite | data/records/chlorite.yaml | maintained | Chlorite group |
| cmmmech:chromium | data/records/chromium.yaml | maintained | Chromium |
| cmmmech:colemanite | data/records/colemanite.yaml | maintained | Colemanite |
| cmmmech:dittmarite | data/records/dittmarite.yaml | maintained | Dittmarite |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |
| cmmmech:enstatite | data/records/enstatite.yaml | maintained | Enstatite |
| cmmmech:falottaite | data/records/falottaite.yaml | maintained | Falottaite |
| cmmmech:feitknechtite | data/records/feitknechtite.yaml | maintained | Feitknechtite |
| cmmmech:ferrihydrite | data/records/ferrihydrite.yaml | maintained | Ferrihydrite |
| cmmmech:fluorapatite | data/records/fluorapatite.yaml | maintained | Fluorapatite |
| cmmmech:fluorescent-lamp-phosphor | data/records/fluorescent-lamp-phosphor.yaml | maintained | Spent fluorescent-lamp phosphor powder |
| cmmmech:fluorine | data/records/fluorine.yaml | maintained | Fluorine |
| cmmmech:forsterite | data/records/forsterite.yaml | maintained | Forsterite |
| cmmmech:glushinskite | data/records/glushinskite.yaml | maintained | Glushinskite |
| cmmmech:hafnium | data/records/hafnium.yaml | maintained | Hafnium |
| cmmmech:hausmannite | data/records/hausmannite.yaml | maintained | Hausmannite |
| cmmmech:heavy-fuel-oil-combustion-ash | data/records/heavy-fuel-oil-combustion-ash.yaml | maintained | Heavy-fuel-oil combustion ash |
| cmmmech:hollandite | data/records/hollandite.yaml | maintained | Hollandite |
| cmmmech:hopeite | data/records/hopeite.yaml | maintained | Hopeite |
| cmmmech:humboldtine | data/records/humboldtine.yaml | maintained | Humboldtine |
| cmmmech:hydroxylapatite | data/records/hydroxylapatite.yaml | maintained | Hydroxylapatite |
| cmmmech:ion-adsorption-rare-earth-leach-residue | data/records/ion-adsorption-rare-earth-leach-residue.yaml | maintained | Ion-adsorption rare-earth leach residue |
| cmmmech:iron | data/records/iron.yaml | maintained | Iron |
| cmmmech:kaolin | data/records/kaolin.yaml | maintained | Natural kaolin feed |
| cmmmech:katsarosite | data/records/katsarosite.yaml | maintained | Katsarosite |
| cmmmech:lanthanum | data/records/lanthanum.yaml | maintained | Lanthanum |
| cmmmech:lindbergite | data/records/lindbergite.yaml | maintained | Lindbergite |
| cmmmech:lithium-bearing-geothermal-brine | data/records/lithium-bearing-geothermal-brine.yaml | maintained | Lithium-bearing geothermal brine |
| cmmmech:lithium-mica-ore | data/records/lithium-mica-ore.yaml | maintained | Lithium-mica ore |
| cmmmech:magnesium | data/records/magnesium.yaml | maintained | Magnesium |
| cmmmech:magnetite | data/records/magnetite.yaml | maintained | Magnetite |
| cmmmech:malachite | data/records/malachite.yaml | maintained | Malachite |
| cmmmech:manganese | data/records/manganese.yaml | maintained | Manganese |
| cmmmech:manganese-ore | data/records/manganese-ore.yaml | maintained | Manganese ore |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |
| cmmmech:mimetite | data/records/mimetite.yaml | maintained | Mimetite |
| cmmmech:montmorillonite | data/records/montmorillonite.yaml | maintained | Montmorillonite |
| cmmmech:moolooite | data/records/moolooite.yaml | maintained | Moolooite |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |
| cmmmech:nepheline | data/records/nepheline.yaml | maintained | Nepheline |
| cmmmech:nontronite | data/records/nontronite.yaml | maintained | Nontronite |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:palladium | data/records/palladium.yaml | maintained | Palladium |
| cmmmech:phosphate-rock | data/records/phosphate-rock.yaml | maintained | Phosphate rock |
| cmmmech:phosphogypsum | data/records/phosphogypsum.yaml | maintained | Phosphogypsum |
| cmmmech:phosphorus | data/records/phosphorus.yaml | maintained | Phosphorus |
| cmmmech:praseodymium | data/records/praseodymium.yaml | maintained | Praseodymium |
| cmmmech:pyrochroite | data/records/pyrochroite.yaml | maintained | Pyrochroite |
| cmmmech:rare-earth-element-commodities | data/records/rare-earth-element-commodities.yaml | maintained | Rare-earth-element commodities, Australian list scope |
| cmmmech:rhodochrosite | data/records/rhodochrosite.yaml | maintained | Rhodochrosite |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |
| cmmmech:silicon | data/records/silicon.yaml | maintained | Silicon |
| cmmmech:smithsonite | data/records/smithsonite.yaml | maintained | Smithsonite |
| cmmmech:spent-fluid-catalytic-cracking-catalyst | data/records/spent-fluid-catalytic-cracking-catalyst.yaml | maintained | Spent fluid catalytic cracking catalyst |
| cmmmech:spent-nickel-metal-hydride-batteries | data/records/spent-nickel-metal-hydride-batteries.yaml | maintained | Spent nickel-metal-hydride batteries |
| cmmmech:spent-silver-oxide-zinc-button-cell-batteries | data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml | maintained | Spent silver-oxide–zinc button-cell batteries |
| cmmmech:sphalerite | data/records/sphalerite.yaml | maintained | Sphalerite |
| cmmmech:strontianite | data/records/strontianite.yaml | maintained | Strontianite |
| cmmmech:struvite | data/records/struvite.yaml | maintained | Struvite |
| cmmmech:talc | data/records/talc.yaml | maintained | Talc |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |
| cmmmech:titanium-metal | data/records/titanium-metal.yaml | maintained | Titanium metal |
| cmmmech:traction-battery-hydrometallurgical-residue | data/records/traction-battery-hydrometallurgical-residue.yaml | maintained | Traction-battery hydrometallurgical residue |
| cmmmech:uraninite | data/records/uraninite.yaml | maintained | Uraninite |
| cmmmech:uranium | data/records/uranium.yaml | maintained | Uranium |
| cmmmech:vanadium | data/records/vanadium.yaml | maintained | Vanadium |
| cmmmech:vaterite | data/records/vaterite.yaml | maintained | Vaterite |
| cmmmech:waste-liquid-crystal-display-panels | data/records/waste-liquid-crystal-display-panels.yaml | maintained | Waste liquid-crystal display panels |
| cmmmech:waste-x-ray-films | data/records/waste-x-ray-films.yaml | maintained | Waste X-ray films |
| cmmmech:wheatleyite | data/records/wheatleyite.yaml | maintained | Wheatleyite |
| cmmmech:whewellite | data/records/whewellite.yaml | maintained | Whewellite |
| cmmmech:zinc | data/records/zinc.yaml | maintained | Zinc |
| cmmmech:zincite | data/records/zincite.yaml | maintained | Zincite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:dunite, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All 89 records in the causal_graphs cohort pass LinkML structural and semantic validation with 0 errors. |
| cmmmech validate-history (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:dunite, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All curation_history entries and history_refs sidecars across the 89 causal_graphs records resolve and validate cleanly. |
| Ontology ID-label consistency (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:dunite, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 89 causal_graphs records carries a consistent canonical label with 0 cross-corpus conflicts. |

## Scientific And Domain Assessments

### Causal graph connectivity, DAG acyclicity, and verbatim edge evidence coverage

graph: supported. Targets: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:dunite, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite.

All 94 causal graphs across 89 records are connected DAGs with valid CausalPredicateEnum predicates, explicit mechanism_ref links, and verbatim primary-source edge evidence.

### Field-by-field parity between mechanism-level and node-level ProteinExample entries

consistency: concern. Targets: cmmmech:allanite-concentrate, cmmmech:thulium.

2 of 86 protein-example records (cmmmech:allanite-concentrate and cmmmech:thulium) have abbreviated evidence[].explanation strings on causal_graphs[].nodes[].protein_examples compared to mechanisms[].protein_examples.

## Findings

### cmmmech-cycle2-stage4-finding-0002: 2 causal-graph records have abbreviated node-level protein_examples evidence explanations relative to mechanisms

minor / open / confirmed; issue key: cmmmech.protein_examples.mechanism-node-evidence-explanation-drift.

Across 84 of 86 records carrying protein_examples, every ProteinExample entry on a GENE_OR_PROTEIN node in causal_graphs[].nodes[].protein_examples is identical across all fields to its paired mechanisms[].protein_examples entry. In data/records/allanite-concentrate.yaml (UniProtKB:Q5FT13 and UniProtKB:Q5FTI1 on gluconobacter_allanite_bioleaching_graph), the node-level evidence[].explanation omits the Figure S2 Panel B vs main-text pstS label discrepancy documented in mechanisms[].protein_examples. In data/records/thulium.yaml (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, and UniProtKB:O32206 on bsubtilis_ltas_thulium_biosorption_graph), the node-level evidence[].explanation omits the trailing 'alongside non-LTA cell-wall binding' qualification present in mechanisms[].protein_examples.

## Recommended Actions And Acceptance Checks

### action-sync-node-protein-example-explanations

Synchronize causal_graphs[].nodes[].protein_examples[].evidence[].explanation with mechanisms[].protein_examples[].evidence[].explanation in data/records/allanite-concentrate.yaml and data/records/thulium.yaml, and record EDIT history sidecars during Stage 5.

- Every ProteinExample on a GENE_OR_PROTEIN node in allanite-concentrate.yaml and thulium.yaml matches its paired mechanism ProteinExample across all fields including evidence[].explanation.
- Both records have matching EDIT history sidecars and pass cmmmech validate --require-records and cmmmech validate-history --base main.

## Category Boundaries

- retain: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:dunite, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite. All 89 records in the causal_graphs cohort denote distinct, non-synonymous entities matching data/records/*.yaml where causal_graphs is non-empty at 547283a882c1d657f934434f2eb5ea9a1418771a with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cmmmech-validate | src/cmmmech/validation.py; cmmmech validate --require-records | supports | LinkML structural and semantic validator passed across all 631 records (including the causal_graphs cohort) with 0 errors. |
| ev-cmmmech-history | src/cmmmech/history.py; cmmmech validate-history --base main | supports | All 891 curation history sidecars in history/records/ and record history_refs passed validation with 0 errors. |
| ev-cohort-audit | src/cmmmech/schema/cmmmech.yaml; Cycle 2 Stage 4 full-inventory cohort audit (causal_graphs) at 547283a882c1d657f934434f2eb5ea9a1418771a | supports | Full-inventory inspection of all records in the causal_graphs cohort verified distinct material identities, source-backed criticality/mechanism claims, and 100% CURIE label consistency across 165 distinct ontology terms. |
| ev-pe-explanation-drift | data/records/allanite-concentrate.yaml; Comparison of mechanisms[].protein_examples[].evidence[].explanation vs causal_graphs[].nodes[].protein_examples[].evidence[].explanation in allanite-concentrate.yaml and thulium.yaml | partial | In 87 of 89 causal_graphs records, every ProteinExample entry on a GENE_OR_PROTEIN node matches its paired mechanism's ProteinExample entry across all fields. In cmmmech:allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and cmmmech:thulium (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206), the node-level protein_examples[].evidence[].explanation strings are abbreviated relative to the mechanism-level strings. |

## Limits And Additional Notes

- 2 records (allanite-concentrate and thulium) have minor text drift between mechanism-level and node-level protein_examples[].evidence[].explanation (tracked as open finding cmmmech-cycle2-stage4-finding-0002 for Stage 5 remediation).
- 6 GENE_OR_PROTEIN nodes across 6 records (ferrihydrite, iron, lindbergite, magnetite, manganese, praseodymium) remain protein_grounding_status: UNGROUNDED due to unsequenced wild isolates (Bacillus sp. AX17, Serpula himantioides), unindexed locus tag (Pseudomonas putida GB-1 mopA PputGB1_3353), or synthetic engineered EF-hand variant (LanM-O36).
- Companion single-record review 20261022T115007Z-katsarosite-cycle2-stage4-record-review tracks open minor finding cmmmech-cycle2-stage4-finding-0003 on cmmmech:katsarosite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T115006Z-cycle2-stage4-causal-graphs-cohort-review
title: 'Cycle 2 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples
  records (89/89)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-22T11:46:00Z'
finished_at: '2026-10-22T11:50:06Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reviewed all 89 records with multi-step causal_graphs at commit 547283a882c1d657f934434f2eb5ea9a1418771a
  (20 element, 44 mineral, 2 mineral_group, 4 commodity, 7 primary_resource, 12 secondary_resource;
  94 causal graphs, 410 nodes, 316 edges, 143 GROUNDED and 6 source-limited UNGROUNDED
  GENE_OR_PROTEIN nodes; 86 records with 177 protein_examples across 50 unique UniProtKB
  accessions). Verified 100% connectedness and DAG acyclicity, 100% edge evidence
  coverage with verbatim primary-source snippets, and 100% UniProtKB accession/label/organism/domain
  synchronization between mechanism-level and node-level protein_examples. Recorded
  one minor consistency finding (cmmmech-cycle2-stage4-finding-0002) on cmmmech:allanite-concentrate
  and cmmmech:thulium where node-level protein_examples[].evidence[].explanation strings
  are slightly abbreviated relative to mechanism-level protein_examples[].evidence[].explanation
  strings (and see companion single-record review 20261022T115007Z-katsarosite-cycle2-stage4-record-review
  for cmmmech-cycle2-stage4-finding-0003 on cmmmech:katsarosite).
reviewer:
  identity: antigravity / cmmmech-cycle2-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 2 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 547283a882c1d657f934434f2eb5ea9a1418771a.
source:
  git_revision: 547283a882c1d657f934434f2eb5ea9a1418771a
  state: git_commit
  inputs:
  - path: data/records/akaganeite.yaml
    sha256: 7a5214f7def425bbbaf9d0bf440307d817a240e0fd4efe233ae4ca24a4c6c70e
    role: target
  - path: data/records/allanite-concentrate.yaml
    sha256: 600630c8a867238668f6d57c637400b985942e244b826c860ddba1755c59f06e
    role: target
  - path: data/records/allanite-leachate.yaml
    sha256: 049060cadf31403bc3c58bf820774b74b66c75e406c9d85484731efd28612f42
    role: target
  - path: data/records/aluminium.yaml
    sha256: 8df6aa9f1e6f6b4fdb637c4026cfef6781c286c847e25153d0c126a67503fe13
    role: target
  - path: data/records/anatase.yaml
    sha256: e6458835c3c5a41c4613ebe519662b54d1cf77ff5a3a0ebd704f61af5ce958ca
    role: target
  - path: data/records/asbolane.yaml
    sha256: fc303916b2a7c64bfb657a7fc73f75e9db2146ac1ad4d2476024a5455fb56594
    role: target
  - path: data/records/bauxite-residue.yaml
    sha256: fbad4371b1d3ffed508163dc947332d39f17190aa5b2367c40022caf7f1cab46
    role: target
  - path: data/records/birnessite.yaml
    sha256: 5b88a0d7bd9fdc9c735f24709520addb0c462decc45b6fe9fcdf7ec2e7740fa1
    role: target
  - path: data/records/bixbyite-mn.yaml
    sha256: c8f7fcc10cb5a1d6b7965e1441a075c6be889de9eeaea7c271973def6459a797
    role: target
  - path: data/records/borates.yaml
    sha256: de224b4334408815751fbddd6892962bcae6eb4bffe628b485bd14780e59801f
    role: target
  - path: data/records/brushite.yaml
    sha256: 5fa1540a07d369151fcb28abea980998c964745f3bbd5f2ee7fa6ef0c2400f8c
    role: target
  - path: data/records/calcite.yaml
    sha256: 8c1378d02bf991926c80747de98d6db4caed0248fd105c70832cbd1d60964b7f
    role: target
  - path: data/records/cerium.yaml
    sha256: 06ec0e354669126b029210b5f511ebf6c235acbec9890a4f30c1d293eed95844
    role: target
  - path: data/records/cerussite.yaml
    sha256: 3ef139bfab9a93d71ef13f6a299aa8dc93ff3e2ae67131afb3ea80159549c565
    role: target
  - path: data/records/chlorite.yaml
    sha256: ed608d1ef84bd29949d0f6f8e130e147d7896a0abb84d9120a53b51a5ca2a7aa
    role: target
  - path: data/records/chromium.yaml
    sha256: 1c5b610983ce5970bac085a5a3e32e6bee189acef13192113f6d1b46ff6c3a7f
    role: target
  - path: data/records/colemanite.yaml
    sha256: 0e1e9a2348a08c4dcc420e24f3ec265e309f35f4ed98e46e2bf47eb9124b8550
    role: target
  - path: data/records/dittmarite.yaml
    sha256: c12b265e41c26f370f23729e76c74dfe86a8e574889cdb7f7ae2ceff5eb44fd5
    role: target
  - path: data/records/dunite.yaml
    sha256: c583f03cf1bce75966ef72ad8baa449490dbf3dadad2a0c39614205260fa5eae
    role: target
  - path: data/records/enstatite.yaml
    sha256: 5af1b751e9b6ff378f70a487f29e8d6c8616101b7b7ec41dd659d4dc93a50ce1
    role: target
  - path: data/records/falottaite.yaml
    sha256: 0f3c1b1abb6dcbf9b3b5791ddd849cbf92e315cf877197c66686cea7a8236351
    role: target
  - path: data/records/feitknechtite.yaml
    sha256: a3112a6a8266a718abf3c794a2de3ccf8c084d0eb67afc6ad21eda47c8133dbc
    role: target
  - path: data/records/ferrihydrite.yaml
    sha256: 4ef266f47c11833c25999d545382bdc9831259541c720884bd07330f05ee1de3
    role: target
  - path: data/records/fluorapatite.yaml
    sha256: bdf18967aa4d7e99f3838762123c3e766ed0914b7c110b2c951ebf28d33b0095
    role: target
  - path: data/records/fluorescent-lamp-phosphor.yaml
    sha256: ce46ed2cbef45cdb428fb97414a938577df9beb08ebc6ff00f6a44823488f38b
    role: target
  - path: data/records/fluorine.yaml
    sha256: 4af0ed94ff108aeb0aac4eab20d104aeb4df731ead7816c7324444bed983a7c2
    role: target
  - path: data/records/forsterite.yaml
    sha256: 02e8064c327e7ffaad302ec0ab8cbe772a209b56c48353986a392d0cc6730e4c
    role: target
  - path: data/records/glushinskite.yaml
    sha256: 1d2ac15ed1c10a1f6a0bd3e4224440e99fc7e3b8e93e1114a3a90004870c925f
    role: target
  - path: data/records/hafnium.yaml
    sha256: 94398fcf1ddafc2f294a16915b163a675e4bfa623beba10251cb21d293ded3a8
    role: target
  - path: data/records/hausmannite.yaml
    sha256: 5a14c442064c2dd3b6abd1d796a0855b9c823e0a8de6a1ef2a76233231a8ce24
    role: target
  - path: data/records/heavy-fuel-oil-combustion-ash.yaml
    sha256: 52579409f14e3b9dd2cb8f1505ea1f08515fa2f624353f11e661a2c4f3df7c45
    role: target
  - path: data/records/hollandite.yaml
    sha256: 64162baaa25d3cf3fc9b5290c3c4130655063e214a92fe8ff90b77710f695113
    role: target
  - path: data/records/hopeite.yaml
    sha256: e17ac1f2e993dfd8781643472caba55ee3e8ca845b4c040f14609268cd53826d
    role: target
  - path: data/records/humboldtine.yaml
    sha256: 120fdb51b0729eacb1fa76fcfdd0e4e53ff124b265cc2f8dfd105bfcb372222c
    role: target
  - path: data/records/hydroxylapatite.yaml
    sha256: 103556e9bc6f205b72968ba080931fa074095bd00c137157bb4fe5323fdffb25
    role: target
  - path: data/records/ion-adsorption-rare-earth-leach-residue.yaml
    sha256: a7bc2ba234388913d774a62e95e4ae18bccdfe36069ed4ec0b6f779ef42bf274
    role: target
  - path: data/records/iron.yaml
    sha256: 92f6792df8c1b65d3377d91b9cf7817b42a4558cb0618e4db8f2f97382aad62d
    role: target
  - path: data/records/kaolin.yaml
    sha256: 8e754fc3cba67a9b31d2cae9ef8846128fbe6f39c1b3d591d3e5434fb25b29f0
    role: target
  - path: data/records/katsarosite.yaml
    sha256: 2b5712225072094be6d4d42379dbd9a796c6f94b5b063349fbea290b655e31c9
    role: target
  - path: data/records/lanthanum.yaml
    sha256: 625ebc045461d40ac1234394ee1fe3aaa43a2b6fb213893d1cf993498c09e963
    role: target
  - path: data/records/lindbergite.yaml
    sha256: 1d3ec878b2baa8c5978eb6ffafd1bbe7c9384b348b60399efa80078e04ad2ac6
    role: target
  - path: data/records/lithium-bearing-geothermal-brine.yaml
    sha256: 53dc79243621d802befd7d309d8b12a079c57e81b1b5c9fabb3b25511c70dfa8
    role: target
  - path: data/records/lithium-mica-ore.yaml
    sha256: 48a2f772fe3feb00eab2dee2b5d80e8daa45f5605ddb504282571ef7d5a925cf
    role: target
  - path: data/records/magnesium.yaml
    sha256: 931d640f20af7ef12fd20175aa3d515d514089f42c368b24514dd37af642822f
    role: target
  - path: data/records/magnetite.yaml
    sha256: 8a547999e0f10555f6b57013b502a5008fd5afae6d1c2458cbff7659fbe2cb20
    role: target
  - path: data/records/malachite.yaml
    sha256: b9ca1433cda88dbe887bdc03e586891eefd50dae21d58801f0a318b976b1e421
    role: target
  - path: data/records/manganese-ore.yaml
    sha256: 94180086908103d6ef736b9e61e4fdea69c07e65a12f1fb11981bd5b46fb3d1a
    role: target
  - path: data/records/manganese.yaml
    sha256: 4e14de8d0bd57869af70e6a8ce02da5c183afdef4715656c3c19c6ca86001749
    role: target
  - path: data/records/metacinnabar.yaml
    sha256: 0bb941fbfa16112b5dddff9d25e414e4a5ce00ce79bf9ab80ee39f4285ca4c31
    role: target
  - path: data/records/mimetite.yaml
    sha256: fd40abfe61ea182d5c94e424e60dc64422a5c551ba9492340c2d8d8f12b4384f
    role: target
  - path: data/records/montmorillonite.yaml
    sha256: c25638a1ed8128e31733f560aeea1a0fc1bb73e420425c65422923064efa1c6e
    role: target
  - path: data/records/moolooite.yaml
    sha256: 9006a1b5b2502efbf8b1a3ec90caad7dcfb1bf5469de7ad94791a2f52314fa3f
    role: target
  - path: data/records/neodymium.yaml
    sha256: f1b949b4cb0bc909368d75ec7404c143b5c449d71f7ee968745af42f959636d3
    role: target
  - path: data/records/nepheline.yaml
    sha256: 0b5844e77af50b821f69cd51a74d73a045bfb9913486e46c74604402b6107a75
    role: target
  - path: data/records/nontronite.yaml
    sha256: 221195a250ebbe6e3c849bc6f949917fefc074a62327a4d930676d6bdc9fa7a1
    role: target
  - path: data/records/olivine-group.yaml
    sha256: 1017cd19a6a93cccff1eeb3d7ababb11eecf12b41e45cbd56f5be48610419af3
    role: target
  - path: data/records/palladium.yaml
    sha256: 6924903baa0aceaa8361a94198b2d5b42460b34d4d643fa4ffdc6e43c50803c0
    role: target
  - path: data/records/phosphate-rock.yaml
    sha256: a20bd2ef094165632904b57d4592bec51b3ab27960605e3eeb030b31462c74f8
    role: target
  - path: data/records/phosphogypsum.yaml
    sha256: 3abec770a259f6f0ed305210918c0cf6c7d18fb52bbaf4fea300abfcd80b42e2
    role: target
  - path: data/records/phosphorus.yaml
    sha256: 83c3a7e583bab72905d3d6017fda5174f2ca5a89ba0c63df70015575ed4fb728
    role: target
  - path: data/records/praseodymium.yaml
    sha256: e31325b8f4667ecb0533eca471c9398942cbcf020c90fa17f34e6a545f71d8d1
    role: target
  - path: data/records/pyrochroite.yaml
    sha256: 1ca16d4224942cd258a256563f1f5c8d711b5328c2f95d70d76a032e4097d4d0
    role: target
  - path: data/records/rare-earth-element-commodities.yaml
    sha256: 08b78b26fcfe9b718385dee29be591eea523da30ae82e522e16c011f7795302b
    role: target
  - path: data/records/rhodochrosite.yaml
    sha256: d120d1c277b742539d55e731708b4d4b628017d5b6298a70f408d6e54b30eb0c
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
  - path: data/records/smithsonite.yaml
    sha256: 1a2d72e7da1d873806570c0cf2a34a6216d0c8821fc7fd57f1c14326e2c67cb2
    role: target
  - path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    sha256: 958771acc23b8947e194344ca260ece74733599a7935cb07a5e4f894e8b43055
    role: target
  - path: data/records/spent-nickel-metal-hydride-batteries.yaml
    sha256: 9e07ce9af31462bfb138454b7176106e2d245b0d381a82e3c097cf5df3d2a301
    role: target
  - path: data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml
    sha256: 199b1a45cdab2fc47d99767df4aec89cb7b9b150de02bc52f72bc826936b2844
    role: target
  - path: data/records/sphalerite.yaml
    sha256: 9744a05cddd16fd19033a937b37d9231b63d9b46d20884965f6e617336d97ae5
    role: target
  - path: data/records/strontianite.yaml
    sha256: fd0ba6d8bd4e69e250e0e0109e01dcccb86771cbcfb8e9b0f6ef6fd890275d66
    role: target
  - path: data/records/struvite.yaml
    sha256: 48c215816ba65046aeaeed7a15bd80130a31d62420857a09c5e46ddf762cc266
    role: target
  - path: data/records/talc.yaml
    sha256: 6d6e241f799e6bed57a229bc464ffe6fa7602a6d9581761120a3159047629a3c
    role: target
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 75bc83e27a7f1e418752b8c31571434e0719b35ae99e76e88f59b919899232dc
    role: target
  - path: data/records/thulium.yaml
    sha256: a6c50ec0889e52be36abca1c07f57673b03adc78caf4749562ebf5dea441e0a0
    role: target
  - path: data/records/titanium-metal.yaml
    sha256: 547e4023b359003f82e8178f6adfee0db4424043e9591e268531876a65552622
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: b738413bfdcf25e4645514ce893b9b3bcf231a24671a2a4f914357a5216d7194
    role: target
  - path: data/records/uraninite.yaml
    sha256: a09be0d68b606fd0c87b75569b5c7f95211f132533bf8b8d415880cc84b97912
    role: target
  - path: data/records/uranium.yaml
    sha256: f2bcc77e3e01adef0509ae4b5cdb26aee435dae30f2d93cf2ad322c8890c72a0
    role: target
  - path: data/records/vanadium.yaml
    sha256: 335a04a069081e6fb33988bda293f376f379549f2c0101f5f618385b1a2f1487
    role: target
  - path: data/records/vaterite.yaml
    sha256: 7ffcf6f5bc1904774bf9382c8900c1481722ad4514418157813a907b09dfa656
    role: target
  - path: data/records/waste-liquid-crystal-display-panels.yaml
    sha256: 2c8c0664b91097e22ad787991874fffea68754b7caedc64dee5b13e6e76b72ca
    role: target
  - path: data/records/waste-x-ray-films.yaml
    sha256: e221e4cfb6f0a3105cf2138a82c93aef199c245e157228e7ac80ed4a594f1575
    role: target
  - path: data/records/wheatleyite.yaml
    sha256: 1947f067cdac1fa94eb4b5c5fb689c4cb673502566c9f724a432a9f32a3559c5
    role: target
  - path: data/records/whewellite.yaml
    sha256: 8981fa7f60b431b893935fe0bc197993ccb7a4651ef46283f4e046005350a79e
    role: target
  - path: data/records/zinc.yaml
    sha256: 0066316a486c391eceb35ea6ac821f2643942ca97dbc0f7bd88d2e0b3fa47532
    role: target
  - path: data/records/zincite.yaml
    sha256: b5636b992ce917a20726534cb4e9178dac2251043c32762f22988ecff74334e1
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 89
  reviewed_target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  selection: data/records/*.yaml where causal_graphs is non-empty at 547283a882c1d657f934434f2eb5ea9a1418771a
  description: Full-population Cycle 2 Stage 4 category review of all 89 CMMMech records
    carrying multi-step causal_graphs (94 graphs, 410 nodes, 316 edges) and UniProtKB
    protein_examples (86 records, 177 protein_examples across 50 unique UniProtKB
    accessions).
targets:
- target_id: cmmmech:akaganeite
  path: data/records/akaganeite.yaml
  kind: maintained
  label: Akaganeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/akaganeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
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
- target_id: cmmmech:allanite-leachate
  path: data/records/allanite-leachate.yaml
  kind: maintained
  label: Allanite-derived rare-earth leachate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-leachate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
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
- target_id: cmmmech:anatase
  path: data/records/anatase.yaml
  kind: maintained
  label: Anatase
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anatase.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:asbolane
  path: data/records/asbolane.yaml
  kind: maintained
  label: Asbolane
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/asbolane.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bauxite-residue
  path: data/records/bauxite-residue.yaml
  kind: maintained
  label: Bauxite residue (red mud)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bauxite-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:birnessite
  path: data/records/birnessite.yaml
  kind: maintained
  label: Birnessite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/birnessite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:bixbyite-mn
  path: data/records/bixbyite-mn.yaml
  kind: maintained
  label: Bixbyite-(Mn)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
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
- target_id: cmmmech:brushite
  path: data/records/brushite.yaml
  kind: maintained
  label: Brushite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/brushite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:calcite
  path: data/records/calcite.yaml
  kind: maintained
  label: Calcite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcite.yaml
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
- target_id: cmmmech:cerussite
  path: data/records/cerussite.yaml
  kind: maintained
  label: Cerussite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerussite.yaml
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
- target_id: cmmmech:colemanite
  path: data/records/colemanite.yaml
  kind: maintained
  label: Colemanite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/colemanite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:dittmarite
  path: data/records/dittmarite.yaml
  kind: maintained
  label: Dittmarite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dittmarite.yaml
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
- target_id: cmmmech:enstatite
  path: data/records/enstatite.yaml
  kind: maintained
  label: Enstatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/enstatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:falottaite
  path: data/records/falottaite.yaml
  kind: maintained
  label: Falottaite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/falottaite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:feitknechtite
  path: data/records/feitknechtite.yaml
  kind: maintained
  label: Feitknechtite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feitknechtite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferrihydrite
  path: data/records/ferrihydrite.yaml
  kind: maintained
  label: Ferrihydrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrihydrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorapatite
  path: data/records/fluorapatite.yaml
  kind: maintained
  label: Fluorapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:fluorescent-lamp-phosphor
  path: data/records/fluorescent-lamp-phosphor.yaml
  kind: maintained
  label: Spent fluorescent-lamp phosphor powder
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorescent-lamp-phosphor.yaml
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
- target_id: cmmmech:forsterite
  path: data/records/forsterite.yaml
  kind: maintained
  label: Forsterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/forsterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:glushinskite
  path: data/records/glushinskite.yaml
  kind: maintained
  label: Glushinskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/glushinskite.yaml
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
- target_id: cmmmech:hausmannite
  path: data/records/hausmannite.yaml
  kind: maintained
  label: Hausmannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hausmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:heavy-fuel-oil-combustion-ash
  path: data/records/heavy-fuel-oil-combustion-ash.yaml
  kind: maintained
  label: Heavy-fuel-oil combustion ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heavy-fuel-oil-combustion-ash.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hollandite
  path: data/records/hollandite.yaml
  kind: maintained
  label: Hollandite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hollandite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hopeite
  path: data/records/hopeite.yaml
  kind: maintained
  label: Hopeite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hopeite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:humboldtine
  path: data/records/humboldtine.yaml
  kind: maintained
  label: Humboldtine
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/humboldtine.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:hydroxylapatite
  path: data/records/hydroxylapatite.yaml
  kind: maintained
  label: Hydroxylapatite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hydroxylapatite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ion-adsorption-rare-earth-leach-residue
  path: data/records/ion-adsorption-rare-earth-leach-residue.yaml
  kind: maintained
  label: Ion-adsorption rare-earth leach residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ion-adsorption-rare-earth-leach-residue.yaml
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
- target_id: cmmmech:katsarosite
  path: data/records/katsarosite.yaml
  kind: maintained
  label: Katsarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
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
- target_id: cmmmech:lindbergite
  path: data/records/lindbergite.yaml
  kind: maintained
  label: Lindbergite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lindbergite.yaml
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
- target_id: cmmmech:magnetite
  path: data/records/magnetite.yaml
  kind: maintained
  label: Magnetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:malachite
  path: data/records/malachite.yaml
  kind: maintained
  label: Malachite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/malachite.yaml
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
- target_id: cmmmech:metacinnabar
  path: data/records/metacinnabar.yaml
  kind: maintained
  label: Metacinnabar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:mimetite
  path: data/records/mimetite.yaml
  kind: maintained
  label: Mimetite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mimetite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:montmorillonite
  path: data/records/montmorillonite.yaml
  kind: maintained
  label: Montmorillonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/montmorillonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:moolooite
  path: data/records/moolooite.yaml
  kind: maintained
  label: Moolooite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/moolooite.yaml
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
- target_id: cmmmech:nepheline
  path: data/records/nepheline.yaml
  kind: maintained
  label: Nepheline
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nepheline.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:nontronite
  path: data/records/nontronite.yaml
  kind: maintained
  label: Nontronite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nontronite.yaml
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
- target_id: cmmmech:phosphogypsum
  path: data/records/phosphogypsum.yaml
  kind: maintained
  label: Phosphogypsum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphogypsum.yaml
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
- target_id: cmmmech:pyrochroite
  path: data/records/pyrochroite.yaml
  kind: maintained
  label: Pyrochroite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrochroite.yaml
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
- target_id: cmmmech:rhodochrosite
  path: data/records/rhodochrosite.yaml
  kind: maintained
  label: Rhodochrosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhodochrosite.yaml
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
- target_id: cmmmech:smithsonite
  path: data/records/smithsonite.yaml
  kind: maintained
  label: Smithsonite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/smithsonite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-fluid-catalytic-cracking-catalyst
  path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
  kind: maintained
  label: Spent fluid catalytic cracking catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-nickel-metal-hydride-batteries
  path: data/records/spent-nickel-metal-hydride-batteries.yaml
  kind: maintained
  label: Spent nickel-metal-hydride batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-nickel-metal-hydride-batteries.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  path: data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml
  kind: maintained
  label: Spent silver-oxide–zinc button-cell batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sphalerite
  path: data/records/sphalerite.yaml
  kind: maintained
  label: Sphalerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sphalerite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:strontianite
  path: data/records/strontianite.yaml
  kind: maintained
  label: Strontianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:struvite
  path: data/records/struvite.yaml
  kind: maintained
  label: Struvite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/struvite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:talc
  path: data/records/talc.yaml
  kind: maintained
  label: Talc
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/talc.yaml
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
- target_id: cmmmech:traction-battery-hydrometallurgical-residue
  path: data/records/traction-battery-hydrometallurgical-residue.yaml
  kind: maintained
  label: Traction-battery hydrometallurgical residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uraninite
  path: data/records/uraninite.yaml
  kind: maintained
  label: Uraninite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uraninite.yaml
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
- target_id: cmmmech:vaterite
  path: data/records/vaterite.yaml
  kind: maintained
  label: Vaterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vaterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:waste-liquid-crystal-display-panels
  path: data/records/waste-liquid-crystal-display-panels.yaml
  kind: maintained
  label: Waste liquid-crystal display panels
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-liquid-crystal-display-panels.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:waste-x-ray-films
  path: data/records/waste-x-ray-films.yaml
  kind: maintained
  label: Waste X-ray films
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-x-ray-films.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:wheatleyite
  path: data/records/wheatleyite.yaml
  kind: maintained
  label: Wheatleyite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wheatleyite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:whewellite
  path: data/records/whewellite.yaml
  kind: maintained
  label: Whewellite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/whewellite.yaml
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
- target_id: cmmmech:zincite
  path: data/records/zincite.yaml
  kind: maintained
  label: Zincite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zincite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-cohort
  name: cmmmech validate (causal_graphs cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-cmmmech-validate
  summary: All 89 records in the causal_graphs cohort pass LinkML structural and semantic
    validation with 0 errors.
- check_id: cmmmech-validate-history-cohort
  name: cmmmech validate-history (causal_graphs cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-cmmmech-history
  summary: All curation_history entries and history_refs sidecars across the 89 causal_graphs
    records resolve and validate cleanly.
- check_id: curie-label-consistency-cohort
  name: Ontology ID-label consistency (causal_graphs cohort)
  status: passed
  required: true
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-cohort-audit
  summary: Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 89
    causal_graphs records carries a consistent canonical label with 0 cross-corpus
    conflicts.
assessments:
- assessment_id: assess-causal-graphs-connectivity-and-evidence
  topic: Causal graph connectivity, DAG acyclicity, and verbatim edge evidence coverage
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-cmmmech-validate
  - ev-cmmmech-history
  - ev-cohort-audit
  summary: All 94 causal graphs across 89 records are connected DAGs with valid CausalPredicateEnum
    predicates, explicit mechanism_ref links, and verbatim primary-source edge evidence.
  metrics:
  - name: reviewed_causal_graph_records
    value: 89.0
    unit: records
    definition: Total records with multi-step causal_graphs reviewed.
    minimum: 0.0
    maximum: 89.0
  - name: records_with_grounded_protein_examples
    value: 86.0
    unit: records
    definition: Causal-graph records carrying live-verified UniProtKB protein_examples
      (3 records carry only source-limited UNGROUNDED GENE_OR_PROTEIN nodes).
    minimum: 0.0
    maximum: 89.0
- assessment_id: assess-protein-examples-evidence-explanation-sync
  topic: Field-by-field parity between mechanism-level and node-level ProteinExample
    entries
  area: consistency
  outcome: concern
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:thulium
  evidence_ids:
  - ev-pe-explanation-drift
  summary: 2 of 86 protein-example records (cmmmech:allanite-concentrate and cmmmech:thulium)
    have abbreviated evidence[].explanation strings on causal_graphs[].nodes[].protein_examples
    compared to mechanisms[].protein_examples.
findings:
- finding_id: cmmmech-cycle2-stage4-finding-0002
  issue_key: cmmmech.protein_examples.mechanism-node-evidence-explanation-drift
  title: 2 causal-graph records have abbreviated node-level protein_examples evidence
    explanations relative to mechanisms
  category: consistency
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:thulium
  evidence_ids:
  - ev-pe-explanation-drift
  description: Across 84 of 86 records carrying protein_examples, every ProteinExample
    entry on a GENE_OR_PROTEIN node in causal_graphs[].nodes[].protein_examples is
    identical across all fields to its paired mechanisms[].protein_examples entry.
    In data/records/allanite-concentrate.yaml (UniProtKB:Q5FT13 and UniProtKB:Q5FTI1
    on gluconobacter_allanite_bioleaching_graph), the node-level evidence[].explanation
    omits the Figure S2 Panel B vs main-text pstS label discrepancy documented in
    mechanisms[].protein_examples. In data/records/thulium.yaml (UniProtKB:O34952,
    UniProtKB:Q797B3, UniProtKB:P54496, and UniProtKB:O32206 on bsubtilis_ltas_thulium_biosorption_graph),
    the node-level evidence[].explanation omits the trailing 'alongside non-LTA cell-wall
    binding' qualification present in mechanisms[].protein_examples.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
actions:
- action_id: action-sync-node-protein-example-explanations
  finding_ids:
  - cmmmech-cycle2-stage4-finding-0002
  target_ids:
  - cmmmech:allanite-concentrate
  - cmmmech:thulium
  description: Synchronize causal_graphs[].nodes[].protein_examples[].evidence[].explanation
    with mechanisms[].protein_examples[].evidence[].explanation in data/records/allanite-concentrate.yaml
    and data/records/thulium.yaml, and record EDIT history sidecars during Stage 5.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
  acceptance_checks:
  - Every ProteinExample on a GENE_OR_PROTEIN node in allanite-concentrate.yaml and
    thulium.yaml matches its paired mechanism ProteinExample across all fields including
    evidence[].explanation.
  - Both records have matching EDIT history sidecars and pass cmmmech validate --require-records
    and cmmmech validate-history --base main.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:dunite
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:glushinskite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  rationale: All 89 records in the causal_graphs cohort denote distinct, non-synonymous
    entities matching data/records/*.yaml where causal_graphs is non-empty at 547283a882c1d657f934434f2eb5ea9a1418771a
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-cohort-audit
evidence:
- evidence_id: ev-cmmmech-validate
  kind: validation
  reference: src/cmmmech/validation.py
  locator: cmmmech validate --require-records
  accessed_at: '2026-10-22T11:50:06Z'
  support: supports
  summary: LinkML structural and semantic validator passed across all 631 records
    (including the causal_graphs cohort) with 0 errors.
- evidence_id: ev-cmmmech-history
  kind: validation
  reference: src/cmmmech/history.py
  locator: cmmmech validate-history --base main
  accessed_at: '2026-10-22T11:50:06Z'
  support: supports
  summary: All 891 curation history sidecars in history/records/ and record history_refs
    passed validation with 0 errors.
- evidence_id: ev-cohort-audit
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Cycle 2 Stage 4 full-inventory cohort audit (causal_graphs) at 547283a882c1d657f934434f2eb5ea9a1418771a
  accessed_at: '2026-10-22T11:50:06Z'
  support: supports
  summary: Full-inventory inspection of all records in the causal_graphs cohort verified
    distinct material identities, source-backed criticality/mechanism claims, and
    100% CURIE label consistency across 165 distinct ontology terms.
- evidence_id: ev-pe-explanation-drift
  kind: record_content
  reference: data/records/allanite-concentrate.yaml
  locator: Comparison of mechanisms[].protein_examples[].evidence[].explanation vs
    causal_graphs[].nodes[].protein_examples[].evidence[].explanation in allanite-concentrate.yaml
    and thulium.yaml
  accessed_at: '2026-10-22T11:50:06Z'
  support: partial
  summary: In 87 of 89 causal_graphs records, every ProteinExample entry on a GENE_OR_PROTEIN
    node matches its paired mechanism's ProteinExample entry across all fields. In
    cmmmech:allanite-concentrate (UniProtKB:Q5FT13, UniProtKB:Q5FTI1) and cmmmech:thulium
    (UniProtKB:O34952, UniProtKB:Q797B3, UniProtKB:P54496, UniProtKB:O32206), the
    node-level protein_examples[].evidence[].explanation strings are abbreviated relative
    to the mechanism-level strings.
limitations:
- 2 records (allanite-concentrate and thulium) have minor text drift between mechanism-level
  and node-level protein_examples[].evidence[].explanation (tracked as open finding
  cmmmech-cycle2-stage4-finding-0002 for Stage 5 remediation).
- '6 GENE_OR_PROTEIN nodes across 6 records (ferrihydrite, iron, lindbergite, magnetite,
  manganese, praseodymium) remain protein_grounding_status: UNGROUNDED due to unsequenced
  wild isolates (Bacillus sp. AX17, Serpula himantioides), unindexed locus tag (Pseudomonas
  putida GB-1 mopA PputGB1_3353), or synthetic engineered EF-hand variant (LanM-O36).'
notes:
- Companion single-record review 20261022T115007Z-katsarosite-cycle2-stage4-record-review
  tracks open minor finding cmmmech-cycle2-stage4-finding-0003 on cmmmech:katsarosite.
```
