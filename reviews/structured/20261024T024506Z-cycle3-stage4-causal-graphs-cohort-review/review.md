# Cycle 3 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples records (104/104)

- Review: 20261024T024506Z-cycle3-stage4-causal-graphs-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T02:41:00Z
- Finished UTC: 2026-10-24T02:45:06Z
- Reviewer: antigravity / cmmmech-cycle3-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 104 records with multi-step causal_graphs at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e (22 element, 54 mineral, 2 mineral_group, 4 commodity, 7 primary_resource, 15 secondary_resource; 111 causal graphs, 492 nodes, 381 edges, 177 GROUNDED and 6 source-limited UNGROUNDED GENE_OR_PROTEIN nodes; 101 records with 223 protein_examples per layer across 57 unique UniProtKB accessions). Verified 100% connectedness and DAG acyclicity, 100% edge evidence coverage with verbatim primary-source snippets, and 100% field-by-field parity between mechanism-level and node-level protein_examples across all 101 grounded records. Recorded one minor consistency finding (cmmmech-cycle3-stage4-finding-0001) on cmmmech:bixbyite-mn where the strain-matched amplicon ProteinExample entry UniProtKB:A0A0K2YWP2 omits gene_symbol: Mesau_02205 present on both the parent GENE_OR_PROTEIN node and its paired reference-proteome homolog UniProtKB:L0KKS2.

## Scope And Provenance

Full-population Cycle 3 Stage 4 category review of all 104 CMMMech records carrying multi-step causal_graphs (111 graphs, 492 nodes, 381 edges) and UniProtKB protein_examples (101 records, 223 protein_examples per layer across 57 unique UniProtKB accessions: 22 SWISS_PROT and 35 TREMBL).

Selection: data/records/*.yaml where causal_graphs is non-empty at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
Coverage: full; 104 reviewed / 104 in the declared population.
Source: git_commit at Git base 855e0eba1fa9b8a4a975b7155ec013414e4d437e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:allanite-leachate | data/records/allanite-leachate.yaml | maintained | Allanite-derived rare-earth leachate |
| cmmmech:aluminium | data/records/aluminium.yaml | maintained | Aluminium |
| cmmmech:anatase | data/records/anatase.yaml | maintained | Anatase |
| cmmmech:anglesite | data/records/anglesite.yaml | maintained | Anglesite |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |
| cmmmech:asbolane | data/records/asbolane.yaml | maintained | Asbolane |
| cmmmech:bauxite-residue | data/records/bauxite-residue.yaml | maintained | Bauxite residue (red mud) |
| cmmmech:birnessite | data/records/birnessite.yaml | maintained | Birnessite |
| cmmmech:bixbyite-mn | data/records/bixbyite-mn.yaml | maintained | Bixbyite-(Mn) |
| cmmmech:borates | data/records/borates.yaml | maintained | Borates |
| cmmmech:bornite | data/records/bornite.yaml | maintained | Bornite |
| cmmmech:brushite | data/records/brushite.yaml | maintained | Brushite |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |
| cmmmech:cerium | data/records/cerium.yaml | maintained | Cerium |
| cmmmech:cerussite | data/records/cerussite.yaml | maintained | Cerussite |
| cmmmech:chlorite | data/records/chlorite.yaml | maintained | Chlorite group |
| cmmmech:chromite-ore-processing-residue | data/records/chromite-ore-processing-residue.yaml | maintained | Chromite ore processing residue |
| cmmmech:chromium | data/records/chromium.yaml | maintained | Chromium |
| cmmmech:colemanite | data/records/colemanite.yaml | maintained | Colemanite |
| cmmmech:dittmarite | data/records/dittmarite.yaml | maintained | Dittmarite |
| cmmmech:djurleite | data/records/djurleite.yaml | maintained | Djurleite |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |
| cmmmech:electroplating-sludge | data/records/electroplating-sludge.yaml | maintained | Electroplating sludge |
| cmmmech:enstatite | data/records/enstatite.yaml | maintained | Enstatite |
| cmmmech:falottaite | data/records/falottaite.yaml | maintained | Falottaite |
| cmmmech:feitknechtite | data/records/feitknechtite.yaml | maintained | Feitknechtite |
| cmmmech:ferrihydrite | data/records/ferrihydrite.yaml | maintained | Ferrihydrite |
| cmmmech:fluorapatite | data/records/fluorapatite.yaml | maintained | Fluorapatite |
| cmmmech:fluorescent-lamp-phosphor | data/records/fluorescent-lamp-phosphor.yaml | maintained | Spent fluorescent-lamp phosphor powder |
| cmmmech:fluorine | data/records/fluorine.yaml | maintained | Fluorine |
| cmmmech:forsterite | data/records/forsterite.yaml | maintained | Forsterite |
| cmmmech:galena | data/records/galena.yaml | maintained | Galena |
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
| cmmmech:kesterite | data/records/kesterite.yaml | maintained | Kësterite |
| cmmmech:lanthanum | data/records/lanthanum.yaml | maintained | Lanthanum |
| cmmmech:lindbergite | data/records/lindbergite.yaml | maintained | Lindbergite |
| cmmmech:lithium-bearing-geothermal-brine | data/records/lithium-bearing-geothermal-brine.yaml | maintained | Lithium-bearing geothermal brine |
| cmmmech:lithium-mica-ore | data/records/lithium-mica-ore.yaml | maintained | Lithium-mica ore |
| cmmmech:magnesium | data/records/magnesium.yaml | maintained | Magnesium |
| cmmmech:magnetite | data/records/magnetite.yaml | maintained | Magnetite |
| cmmmech:malachite | data/records/malachite.yaml | maintained | Malachite |
| cmmmech:manganese | data/records/manganese.yaml | maintained | Manganese |
| cmmmech:manganese-ore | data/records/manganese-ore.yaml | maintained | Manganese ore |
| cmmmech:marcasite | data/records/marcasite.yaml | maintained | Marcasite |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |
| cmmmech:mimetite | data/records/mimetite.yaml | maintained | Mimetite |
| cmmmech:montmorillonite | data/records/montmorillonite.yaml | maintained | Montmorillonite |
| cmmmech:moolooite | data/records/moolooite.yaml | maintained | Moolooite |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |
| cmmmech:nepheline | data/records/nepheline.yaml | maintained | Nepheline |
| cmmmech:nickel-flotation-tailings | data/records/nickel-flotation-tailings.yaml | maintained | Nickel flotation tailings |
| cmmmech:nontronite | data/records/nontronite.yaml | maintained | Nontronite |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:orpiment | data/records/orpiment.yaml | maintained | Orpiment |
| cmmmech:palladium | data/records/palladium.yaml | maintained | Palladium |
| cmmmech:phosphate-rock | data/records/phosphate-rock.yaml | maintained | Phosphate rock |
| cmmmech:phosphogypsum | data/records/phosphogypsum.yaml | maintained | Phosphogypsum |
| cmmmech:phosphorus | data/records/phosphorus.yaml | maintained | Phosphorus |
| cmmmech:praseodymium | data/records/praseodymium.yaml | maintained | Praseodymium |
| cmmmech:pyrochroite | data/records/pyrochroite.yaml | maintained | Pyrochroite |
| cmmmech:rare-earth-element-commodities | data/records/rare-earth-element-commodities.yaml | maintained | Rare-earth-element commodities, Australian list scope |
| cmmmech:realgar | data/records/realgar.yaml | maintained | Realgar |
| cmmmech:rhodium | data/records/rhodium.yaml | maintained | Rhodium |
| cmmmech:rhodochrosite | data/records/rhodochrosite.yaml | maintained | Rhodochrosite |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |
| cmmmech:silicon | data/records/silicon.yaml | maintained | Silicon |
| cmmmech:silver | data/records/silver.yaml | maintained | Silver |
| cmmmech:smithsonite | data/records/smithsonite.yaml | maintained | Smithsonite |
| cmmmech:spent-fluid-catalytic-cracking-catalyst | data/records/spent-fluid-catalytic-cracking-catalyst.yaml | maintained | Spent fluid catalytic cracking catalyst |
| cmmmech:spent-nickel-metal-hydride-batteries | data/records/spent-nickel-metal-hydride-batteries.yaml | maintained | Spent nickel-metal-hydride batteries |
| cmmmech:spent-silver-oxide-zinc-button-cell-batteries | data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml | maintained | Spent silver-oxide–zinc button-cell batteries |
| cmmmech:sphalerite | data/records/sphalerite.yaml | maintained | Sphalerite |
| cmmmech:stannite | data/records/stannite.yaml | maintained | Stannite |
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
| cmmmech validate (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:anglesite, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:bornite, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electroplating-sludge, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:galena, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-flotation-tailings, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All 104 records in the causal_graphs cohort pass LinkML structural and semantic validation with 0 errors. |
| cmmmech validate-history (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:anglesite, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:bornite, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electroplating-sludge, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:galena, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-flotation-tailings, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All curation_history entries and history_refs sidecars across the 104 causal_graphs records resolve and validate cleanly. |
| Ontology ID-label consistency (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:anglesite, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:bornite, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electroplating-sludge, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:galena, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-flotation-tailings, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 104 causal_graphs records carries a consistent canonical label with 0 cross-corpus conflicts. |

## Scientific And Domain Assessments

### Causal graph connectivity, DAG acyclicity, and verbatim edge evidence coverage

graph: supported. Targets: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:anglesite, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:bornite, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electroplating-sludge, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:galena, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-flotation-tailings, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite.

All 111 causal graphs across 104 records are connected DAGs with valid CausalPredicateEnum predicates, explicit mechanism_ref links, verbatim primary-source edge evidence, and 100% mechanism-to-node ProteinExample parity.

### Consistent gene_symbol annotation across paired ProteinExample entries on GENE_OR_PROTEIN nodes

consistency: concern. Targets: cmmmech:bixbyite-mn.

In data/records/bixbyite-mn.yaml, the strain-matched amplicon entry UniProtKB:A0A0K2YWP2 omits gene_symbol: Mesau_02205 even though the parent GENE_OR_PROTEIN node (tg1_acidic_mn_oxidase_factor) and the paired reference-proteome homolog UniProtKB:L0KKS2 both record gene_symbol: Mesau_02205.

## Findings

### cmmmech-cycle3-stage4-finding-0001: cmmmech:bixbyite-mn omits gene_symbol: Mesau_02205 on UniProtKB:A0A0K2YWP2 ProteinExample entries

minor / open / confirmed; issue key: cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol.

In data/records/bixbyite-mn.yaml, the GENE_OR_PROTEIN node tg1_acidic_mn_oxidase_factor (line 201) explicitly declares gene_symbol: Mesau_02205, and its paired Mesorhizobium australicum WSM2073 reference-proteome homolog UniProtKB:L0KKS2 (L0KKS2_MESAW, lines 161 and 240) also declares gene_symbol: Mesau_02205. However, the strain-matched Mesorhizobium sp. TG-1 PCR amplicon ProteinExample entry UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH) in both mechanisms[0].protein_examples[0] (lines 129-157) and causal_graphs[0].nodes[0].protein_examples[0] (lines 208-236) omits gene_symbol: Mesau_02205.

## Recommended Actions And Acceptance Checks

### action-add-bixbyite-mn-amplicon-gene-symbol

Add gene_symbol: Mesau_02205 to both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml via scripts/curate_causal_graphs.py and record an EDIT history sidecar during Stage 5.

- Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml carry gene_symbol: Mesau_02205 matching parent node tg1_acidic_mn_oxidase_factor and paired homolog UniProtKB:L0KKS2.
- A matching EDIT history sidecar exists in history/records/bixbyite-mn/ and passes cmmmech validate --require-records and cmmmech validate-history --base main.

## Category Boundaries

- retain: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:anatase, cmmmech:anglesite, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:bauxite-residue, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:borates, cmmmech:bornite, cmmmech:brushite, cmmmech:calcite, cmmmech:cerium, cmmmech:cerussite, cmmmech:chlorite, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:colemanite, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electroplating-sludge, cmmmech:enstatite, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:ferrihydrite, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:galena, cmmmech:glushinskite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese, cmmmech:manganese-ore, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:mimetite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-flotation-tailings, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:praseodymium, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:scandium, cmmmech:selenium, cmmmech:silicon, cmmmech:silver, cmmmech:smithsonite, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:sphalerite, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tetrahedrite-concentrate, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite. All 104 records in the causal_graphs cohort denote distinct, non-synonymous entities matching data/records/*.yaml where causal_graphs is non-empty at 855e0eba1fa9b8a4a975b7155ec013414e4d437e with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cmmmech-validate | src/cmmmech/validation.py; cmmmech validate --require-records | supports | LinkML structural and semantic validator passed across all 646 records (including the causal_graphs cohort) with 0 errors. |
| ev-cmmmech-history | src/cmmmech/history.py; cmmmech validate-history --base main | supports | All 962 curation history sidecars in history/records/ and record history_refs passed validation with 0 errors. |
| ev-cohort-audit | src/cmmmech/schema/cmmmech.yaml; Cycle 3 Stage 4 full-inventory cohort audit (causal_graphs) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e | supports | Full-inventory inspection of all records in the causal_graphs cohort verified distinct material identities, source-backed criticality/mechanism claims, and 100% CURIE label consistency across 181 distinct ontology terms. |
| ev-bixbyite-mn-missing-gene-symbol | data/records/bixbyite-mn.yaml; lines 129-157 (mechanisms[0].protein_examples[0]) and lines 208-236 (causal_graphs[0].nodes[0].protein_examples[0]) vs lines 158-193, 201, 237-272 | partial | In data/records/bixbyite-mn.yaml, the GENE_OR_PROTEIN node tg1_acidic_mn_oxidase_factor (line 201) and its reference-proteome homolog UniProtKB:L0KKS2 (L0KKS2_MESAW, lines 161 and 240) both explicitly record gene_symbol: Mesau_02205, whereas the paired strain-matched amplicon ProteinExample entry UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH, lines 129-157 and 208-236) omits gene_symbol. |

## Limits And Additional Notes

- data/records/bixbyite-mn.yaml omits gene_symbol: Mesau_02205 on UniProtKB:A0A0K2YWP2 in mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] (tracked as open finding cmmmech-cycle3-stage4-finding-0001 for Stage 5 remediation).
- 6 GENE_OR_PROTEIN nodes across 6 records (ferrihydrite, iron, lindbergite, magnetite, manganese, praseodymium) remain protein_grounding_status: UNGROUNDED due to unsequenced wild isolates (Bacillus sp. AX17, Serpula himantioides), unindexed locus tag (Pseudomonas putida GB-1 mopA PputGB1_3353), or synthetic engineered EF-hand variant (LanM-O36).
- Both records remediated under Cycle 2 finding cmmmech-cycle2-stage4-finding-0002 (cmmmech:allanite-concentrate and cmmmech:thulium) and cmmmech:katsarosite remediated under cmmmech-cycle2-stage4-finding-0003 were re-verified and remain closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T024506Z-cycle3-stage4-causal-graphs-cohort-review
title: 'Cycle 3 Stage 4 cross-cohort review: causal_graphs and UniProt protein_examples
  records (104/104)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-24T02:41:00Z'
finished_at: '2026-10-24T02:45:06Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 104 records with multi-step causal_graphs at commit 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  (22 element, 54 mineral, 2 mineral_group, 4 commodity, 7 primary_resource, 15 secondary_resource;
  111 causal graphs, 492 nodes, 381 edges, 177 GROUNDED and 6 source-limited UNGROUNDED
  GENE_OR_PROTEIN nodes; 101 records with 223 protein_examples per layer across 57
  unique UniProtKB accessions). Verified 100% connectedness and DAG acyclicity, 100%
  edge evidence coverage with verbatim primary-source snippets, and 100% field-by-field
  parity between mechanism-level and node-level protein_examples across all 101 grounded
  records. Recorded one minor consistency finding (cmmmech-cycle3-stage4-finding-0001)
  on cmmmech:bixbyite-mn where the strain-matched amplicon ProteinExample entry UniProtKB:A0A0K2YWP2
  omits gene_symbol: Mesau_02205 present on both the parent GENE_OR_PROTEIN node and
  its paired reference-proteome homolog UniProtKB:L0KKS2.'
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
  - path: data/records/akaganeite.yaml
    sha256: 7a5214f7def425bbbaf9d0bf440307d817a240e0fd4efe233ae4ca24a4c6c70e
    role: target
  - path: data/records/allanite-concentrate.yaml
    sha256: 7c463c39890290cf837fc3677c078cfbc1f9c6c5acb415ecad2eb83842bf029c
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
  - path: data/records/anglesite.yaml
    sha256: 08bc1794204e47aa6d4ca95fa86de6066ad31fcc6b7d68398eec4f8a785dde2d
    role: target
  - path: data/records/arsenopyrite.yaml
    sha256: 94152683e839a537bc58d23c3bf9fa05fd65447dfb94b032a2a87a5b8cc56020
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
  - path: data/records/bornite.yaml
    sha256: e49b571d3f60035b09e4ef30b5ec2d920a66ecab3039bbc70548b25d9b9b402c
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
  - path: data/records/chromite-ore-processing-residue.yaml
    sha256: 7d9f158c0b08285f9bc2f6e4eb620958078cab63f524dd5eda38ca53cac9c893
    role: target
  - path: data/records/chromium.yaml
    sha256: 1c5b610983ce5970bac085a5a3e32e6bee189acef13192113f6d1b46ff6c3a7f
    role: target
  - path: data/records/colemanite.yaml
    sha256: 0e1e9a2348a08c4dcc420e24f3ec265e309f35f4ed98e46e2bf47eb9124b8550
    role: target
  - path: data/records/dittmarite.yaml
    sha256: 104c3eddcadbbfa75c64cd226f56cff62b4015eee24eeb33e7061e4155ed723c
    role: target
  - path: data/records/djurleite.yaml
    sha256: 0aa56b3fadcab0dd1a99ca1e252d972e466107f5f0acb42531c9987ea8efb2cd
    role: target
  - path: data/records/dunite.yaml
    sha256: c583f03cf1bce75966ef72ad8baa449490dbf3dadad2a0c39614205260fa5eae
    role: target
  - path: data/records/electroplating-sludge.yaml
    sha256: 04570514e0de12580ec5ddaa64510936ed67f8bfdcf7715081d42a65030045f9
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
  - path: data/records/galena.yaml
    sha256: a19704d794633a81e205ab1c04079f1034f23a62520d8f07bc6224ed469dd58e
    role: target
  - path: data/records/glushinskite.yaml
    sha256: 5cb28c72ab6063b388cf1b867a066c462b49912fae71e2cb70a12dd70656c321
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
    sha256: 70f5c37f86e33265051032055fe64e6bf44e9a0f3ef055f4d3b605aa4f70a9c7
    role: target
  - path: data/records/kesterite.yaml
    sha256: 177d99bdf9b943e91a91509cbe9eaefcddad9a9163d654b082dace8f502cb4a0
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
    sha256: ab57bc5464af299e10481a8a56f0f4161e6bc10cbac35852b82e63caf677ccc2
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
  - path: data/records/marcasite.yaml
    sha256: 1b66881cd0fad29c55310120fb062e497ef970fb26028317014ef838b1c0b709
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
  - path: data/records/nickel-flotation-tailings.yaml
    sha256: 28f98c925eddaf86f19daa6e014aaf7e3021e3b27488f0176cf508156a06ece3
    role: target
  - path: data/records/nontronite.yaml
    sha256: 221195a250ebbe6e3c849bc6f949917fefc074a62327a4d930676d6bdc9fa7a1
    role: target
  - path: data/records/olivine-group.yaml
    sha256: 1017cd19a6a93cccff1eeb3d7ababb11eecf12b41e45cbd56f5be48610419af3
    role: target
  - path: data/records/orpiment.yaml
    sha256: 594b90950b64a8e22772dbc045ba1a0a909d591ba4790b3d2fc739b8f102a333
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
    sha256: 35de80a71ff8621b74a9d30535f0711356ef4993b8eaf9e0eca5951c57c2edc7
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
  - path: data/records/realgar.yaml
    sha256: ebe2cfc1b3b13517a813ee07a36843f5d2f15985c2a7ff42a58232eae243f3e9
    role: target
  - path: data/records/rhodium.yaml
    sha256: ad7fbf9a2c12d2b9ef411ee23e3ada5698cbb2e6a3ecead2513d881f8d460a18
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
  - path: data/records/silver.yaml
    sha256: 9e526e8db6b270c515116cb1e3f3adfa9800f1184cf5d5740575a1cf1ce4cfc0
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
  - path: data/records/stannite.yaml
    sha256: 757eee31336ca380c7ed44c5516c506dc3120611ea0945978b59fa302f1d1fd0
    role: target
  - path: data/records/strontianite.yaml
    sha256: fd0ba6d8bd4e69e250e0e0109e01dcccb86771cbcfb8e9b0f6ef6fd890275d66
    role: target
  - path: data/records/struvite.yaml
    sha256: bb00ccd418b9d8eb285a38104a5d0bd243596cfa41cf1d694dc17d9f8de11f78
    role: target
  - path: data/records/talc.yaml
    sha256: 6d6e241f799e6bed57a229bc464ffe6fa7602a6d9581761120a3159047629a3c
    role: target
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: b6dedb99840f10f4b6601ae9cb74877e68cab57ab53e5a978b2362d2d268c629
    role: target
  - path: data/records/thulium.yaml
    sha256: 24456f05fb24d477fbea1aa1584f763bf61506fcdab6837713b105f020730a34
    role: target
  - path: data/records/titanium-metal.yaml
    sha256: 547e4023b359003f82e8178f6adfee0db4424043e9591e268531876a65552622
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: e642dd845eb1959a1ce23c23139d259bcb1df6fa4adf87da316caf18070c7b4a
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
    sha256: f3dc7019b0edddcebee714dca2f359499c03fd042feddeda9f157de0dc1ea487
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
  population_size: 104
  reviewed_target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  selection: data/records/*.yaml where causal_graphs is non-empty at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  description: 'Full-population Cycle 3 Stage 4 category review of all 104 CMMMech
    records carrying multi-step causal_graphs (111 graphs, 492 nodes, 381 edges) and
    UniProtKB protein_examples (101 records, 223 protein_examples per layer across
    57 unique UniProtKB accessions: 22 SWISS_PROT and 35 TREMBL).'
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
- target_id: cmmmech:anglesite
  path: data/records/anglesite.yaml
  kind: maintained
  label: Anglesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anglesite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:arsenopyrite
  path: data/records/arsenopyrite.yaml
  kind: maintained
  label: Arsenopyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenopyrite.yaml
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
- target_id: cmmmech:bornite
  path: data/records/bornite.yaml
  kind: maintained
  label: Bornite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bornite.yaml
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
- target_id: cmmmech:chromite-ore-processing-residue
  path: data/records/chromite-ore-processing-residue.yaml
  kind: maintained
  label: Chromite ore processing residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite-ore-processing-residue.yaml
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
- target_id: cmmmech:djurleite
  path: data/records/djurleite.yaml
  kind: maintained
  label: Djurleite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/djurleite.yaml
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
- target_id: cmmmech:electroplating-sludge
  path: data/records/electroplating-sludge.yaml
  kind: maintained
  label: Electroplating sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electroplating-sludge.yaml
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
- target_id: cmmmech:galena
  path: data/records/galena.yaml
  kind: maintained
  label: Galena
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/galena.yaml
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
- target_id: cmmmech:kesterite
  path: data/records/kesterite.yaml
  kind: maintained
  label: Kësterite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kesterite.yaml
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
- target_id: cmmmech:marcasite
  path: data/records/marcasite.yaml
  kind: maintained
  label: Marcasite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/marcasite.yaml
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
- target_id: cmmmech:nickel-flotation-tailings
  path: data/records/nickel-flotation-tailings.yaml
  kind: maintained
  label: Nickel flotation tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-flotation-tailings.yaml
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
- target_id: cmmmech:orpiment
  path: data/records/orpiment.yaml
  kind: maintained
  label: Orpiment
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/orpiment.yaml
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
- target_id: cmmmech:realgar
  path: data/records/realgar.yaml
  kind: maintained
  label: Realgar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/realgar.yaml
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
- target_id: cmmmech:stannite
  path: data/records/stannite.yaml
  kind: maintained
  label: Stannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stannite.yaml
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
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  summary: All 104 records in the causal_graphs cohort pass LinkML structural and
    semantic validation with 0 errors.
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
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  summary: All curation_history entries and history_refs sidecars across the 104 causal_graphs
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
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  summary: Every CHEBI, NCBITaxon, GO, ENVO, and UniProtKB CURIE used across the 104
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
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  summary: All 111 causal graphs across 104 records are connected DAGs with valid
    CausalPredicateEnum predicates, explicit mechanism_ref links, verbatim primary-source
    edge evidence, and 100% mechanism-to-node ProteinExample parity.
  metrics:
  - name: reviewed_causal_graph_records
    value: 104.0
    unit: records
    definition: Total records with multi-step causal_graphs reviewed.
    minimum: 0.0
    maximum: 104.0
  - name: records_with_grounded_protein_examples
    value: 101.0
    unit: records
    definition: Causal-graph records carrying live-verified UniProtKB protein_examples
      (3 records carry only source-limited UNGROUNDED GENE_OR_PROTEIN nodes).
    minimum: 0.0
    maximum: 104.0
- assessment_id: assess-bixbyite-mn-protein-example-gene-symbol
  topic: Consistent gene_symbol annotation across paired ProteinExample entries on
    GENE_OR_PROTEIN nodes
  area: consistency
  outcome: concern
  target_ids:
  - cmmmech:bixbyite-mn
  evidence_ids:
  - ev-bixbyite-mn-missing-gene-symbol
  summary: 'In data/records/bixbyite-mn.yaml, the strain-matched amplicon entry UniProtKB:A0A0K2YWP2
    omits gene_symbol: Mesau_02205 even though the parent GENE_OR_PROTEIN node (tg1_acidic_mn_oxidase_factor)
    and the paired reference-proteome homolog UniProtKB:L0KKS2 both record gene_symbol:
    Mesau_02205.'
findings:
- finding_id: cmmmech-cycle3-stage4-finding-0001
  issue_key: cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol
  title: 'cmmmech:bixbyite-mn omits gene_symbol: Mesau_02205 on UniProtKB:A0A0K2YWP2
    ProteinExample entries'
  category: consistency
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:bixbyite-mn
  evidence_ids:
  - ev-bixbyite-mn-missing-gene-symbol
  description: 'In data/records/bixbyite-mn.yaml, the GENE_OR_PROTEIN node tg1_acidic_mn_oxidase_factor
    (line 201) explicitly declares gene_symbol: Mesau_02205, and its paired Mesorhizobium
    australicum WSM2073 reference-proteome homolog UniProtKB:L0KKS2 (L0KKS2_MESAW,
    lines 161 and 240) also declares gene_symbol: Mesau_02205. However, the strain-matched
    Mesorhizobium sp. TG-1 PCR amplicon ProteinExample entry UniProtKB:A0A0K2YWP2
    (A0A0K2YWP2_9HYPH) in both mechanisms[0].protein_examples[0] (lines 129-157) and
    causal_graphs[0].nodes[0].protein_examples[0] (lines 208-236) omits gene_symbol:
    Mesau_02205.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
    role: maintained_record
actions:
- action_id: action-add-bixbyite-mn-amplicon-gene-symbol
  finding_ids:
  - cmmmech-cycle3-stage4-finding-0001
  target_ids:
  - cmmmech:bixbyite-mn
  description: 'Add gene_symbol: Mesau_02205 to both mechanisms[0].protein_examples[0]
    and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 in
    data/records/bixbyite-mn.yaml via scripts/curate_causal_graphs.py and record an
    EDIT history sidecar during Stage 5.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
    role: maintained_record
  acceptance_checks:
  - 'Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml carry gene_symbol: Mesau_02205
    matching parent node tg1_acidic_mn_oxidase_factor and paired homolog UniProtKB:L0KKS2.'
  - A matching EDIT history sidecar exists in history/records/bixbyite-mn/ and passes
    cmmmech validate --require-records and cmmmech validate-history --base main.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:bauxite-residue
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chlorite
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:colemanite
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electroplating-sludge
  - cmmmech:enstatite
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:ferrihydrite
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:galena
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
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese
  - cmmmech:manganese-ore
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:mimetite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:praseodymium
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:scandium
  - cmmmech:selenium
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:smithsonite
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:sphalerite
  - cmmmech:stannite
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
  rationale: All 104 records in the causal_graphs cohort denote distinct, non-synonymous
    entities matching data/records/*.yaml where causal_graphs is non-empty at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-cohort-audit
evidence:
- evidence_id: ev-cmmmech-validate
  kind: validation
  reference: src/cmmmech/validation.py
  locator: cmmmech validate --require-records
  accessed_at: '2026-10-24T02:45:06Z'
  support: supports
  summary: LinkML structural and semantic validator passed across all 646 records
    (including the causal_graphs cohort) with 0 errors.
- evidence_id: ev-cmmmech-history
  kind: validation
  reference: src/cmmmech/history.py
  locator: cmmmech validate-history --base main
  accessed_at: '2026-10-24T02:45:06Z'
  support: supports
  summary: All 962 curation history sidecars in history/records/ and record history_refs
    passed validation with 0 errors.
- evidence_id: ev-cohort-audit
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Cycle 3 Stage 4 full-inventory cohort audit (causal_graphs) at 855e0eba1fa9b8a4a975b7155ec013414e4d437e
  accessed_at: '2026-10-24T02:45:06Z'
  support: supports
  summary: Full-inventory inspection of all records in the causal_graphs cohort verified
    distinct material identities, source-backed criticality/mechanism claims, and
    100% CURIE label consistency across 181 distinct ontology terms.
- evidence_id: ev-bixbyite-mn-missing-gene-symbol
  kind: record_content
  reference: data/records/bixbyite-mn.yaml
  locator: lines 129-157 (mechanisms[0].protein_examples[0]) and lines 208-236 (causal_graphs[0].nodes[0].protein_examples[0])
    vs lines 158-193, 201, 237-272
  accessed_at: '2026-10-24T02:45:06Z'
  support: partial
  summary: 'In data/records/bixbyite-mn.yaml, the GENE_OR_PROTEIN node tg1_acidic_mn_oxidase_factor
    (line 201) and its reference-proteome homolog UniProtKB:L0KKS2 (L0KKS2_MESAW,
    lines 161 and 240) both explicitly record gene_symbol: Mesau_02205, whereas the
    paired strain-matched amplicon ProteinExample entry UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH,
    lines 129-157 and 208-236) omits gene_symbol.'
limitations:
- 'data/records/bixbyite-mn.yaml omits gene_symbol: Mesau_02205 on UniProtKB:A0A0K2YWP2
  in mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
  (tracked as open finding cmmmech-cycle3-stage4-finding-0001 for Stage 5 remediation).'
- '6 GENE_OR_PROTEIN nodes across 6 records (ferrihydrite, iron, lindbergite, magnetite,
  manganese, praseodymium) remain protein_grounding_status: UNGROUNDED due to unsequenced
  wild isolates (Bacillus sp. AX17, Serpula himantioides), unindexed locus tag (Pseudomonas
  putida GB-1 mopA PputGB1_3353), or synthetic engineered EF-hand variant (LanM-O36).'
notes:
- Both records remediated under Cycle 2 finding cmmmech-cycle2-stage4-finding-0002
  (cmmmech:allanite-concentrate and cmmmech:thulium) and cmmmech:katsarosite remediated
  under cmmmech-cycle2-stage4-finding-0003 were re-verified and remain closed.
```
