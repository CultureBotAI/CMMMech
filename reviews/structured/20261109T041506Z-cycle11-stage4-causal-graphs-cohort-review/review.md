# Cycle 11 Stage 4 cross-cohort review: causal_graphs &amp; protein_examples records (182/182)

- Review: 20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T04:06:00Z
- Finished UTC: 2026-11-09T04:15:06Z
- Reviewer: antigravity / cmmmech-cycle11-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 182 records in data/records/*.yaml that carry causal_graphs at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf (30 element, 78 mineral, 3 mineral_group, 4 commodity, 16 primary_resource, 51 secondary_resource), including the 10 records expanded in Cycle 11 Stage 2 (PR #960, commit df061de7) and Stage 3 (PR #963, commit 79468470): chukanovite, feroxyhyte, illite, lepidocrocite, manganite, palygorskite, plumbojarosite, silica-sand, thallium, and titanium, as well as the 5 records remediated in Cycle 10 Stage 5 (PR #953, commit 09e04a33): calcite, vaterite, lithium-bearing-geothermal-brine, brushite, strontianite, and smithsonite. Across the 182 records, there are 191 causal_graphs, 873 nodes, 682 edges, and 351 GENE_OR_PROTEIN nodes (345 GROUNDED across 179 records and 6 UNGROUNDED across 6 records: erbium, ferrihydrite, gold, lindbergite, magnetite, terbium), with 640 mechanism-level and 640 node-level protein_examples (1,280 total, 100% synchronized) spanning 139 unique live-verified UniProtKB accessions (33 SWISS_PROT, 106 TREMBL). Identified 3 minor graph findings across 5 records (cmmmech-cycle11-stage4-finding-0001 on cmmmech:enstatite, cmmmech:olivine-group, and cmmmech:dunite; cmmmech-cycle11-stage4-finding-0002 on cmmmech:metacinnabar; and cmmmech-cycle11-stage4-finding-0003 on cmmmech:scandium) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 11 Stage 4 cross-cohort review of all 182 records carrying causal_graphs in CMMMech.

Selection: data/records/*.yaml where bool(causal_graphs) is True at 794684703f77385b6e9bca32167f6c8d1e5e29bf
Coverage: full; 182 reviewed / 182 in the declared population.
Source: git_commit at Git base 794684703f77385b6e9bca32167f6c8d1e5e29bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |
| cmmmech:allanite-concentrate | data/records/allanite-concentrate.yaml | maintained | Allanite concentrate |
| cmmmech:allanite-leachate | data/records/allanite-leachate.yaml | maintained | Allanite-derived rare-earth leachate |
| cmmmech:aluminium | data/records/aluminium.yaml | maintained | Aluminium |
| cmmmech:ammoniojarosite | data/records/ammoniojarosite.yaml | maintained | Ammoniojarosite |
| cmmmech:anatase | data/records/anatase.yaml | maintained | Anatase |
| cmmmech:anglesite | data/records/anglesite.yaml | maintained | Anglesite |
| cmmmech:argentojarosite | data/records/argentojarosite.yaml | maintained | Argentojarosite |
| cmmmech:arsenic | data/records/arsenic.yaml | maintained | Arsenic |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |
| cmmmech:asbolane | data/records/asbolane.yaml | maintained | Asbolane |
| cmmmech:automotive-wastewater-treatment-sludge | data/records/automotive-wastewater-treatment-sludge.yaml | maintained | Automotive wastewater-treatment sludge |
| cmmmech:baricite | data/records/baricite.yaml | maintained | Barićite |
| cmmmech:basic-oxygen-furnace-steelmaking-dust | data/records/basic-oxygen-furnace-steelmaking-dust.yaml | maintained | Basic oxygen furnace steelmaking dust |
| cmmmech:bauxite-residue | data/records/bauxite-residue.yaml | maintained | Bauxite residue (red mud) |
| cmmmech:beverage-carton-hydropulping-reject | data/records/beverage-carton-hydropulping-reject.yaml | maintained | Beverage-carton hydropulping reject |
| cmmmech:birnessite | data/records/birnessite.yaml | maintained | Birnessite |
| cmmmech:bixbyite-mn | data/records/bixbyite-mn.yaml | maintained | Bixbyite-(Mn) |
| cmmmech:blast-furnace-cast-house-dust | data/records/blast-furnace-cast-house-dust.yaml | maintained | Blast-furnace cast-house dust |
| cmmmech:borates | data/records/borates.yaml | maintained | Borates |
| cmmmech:bornite | data/records/bornite.yaml | maintained | Bornite |
| cmmmech:boron-ore-concentration-tailings | data/records/boron-ore-concentration-tailings.yaml | maintained | Boron-ore concentration tailings |
| cmmmech:brushite | data/records/brushite.yaml | maintained | Brushite |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |
| cmmmech:cassiterite-polymetallic-sulfide-ore | data/records/cassiterite-polymetallic-sulfide-ore.yaml | maintained | Cassiterite-polymetallic sulfide ore |
| cmmmech:cemented-tungsten-carbide-scrap | data/records/cemented-tungsten-carbide-scrap.yaml | maintained | Cemented tungsten carbide scrap |
| cmmmech:cerium | data/records/cerium.yaml | maintained | Cerium |
| cmmmech:cerussite | data/records/cerussite.yaml | maintained | Cerussite |
| cmmmech:chalcopyrite-enargite-concentrate | data/records/chalcopyrite-enargite-concentrate.yaml | maintained | Chalcopyrite-enargite concentrate |
| cmmmech:chalcopyrite | data/records/chalcopyrite.yaml | maintained | Chalcopyrite |
| cmmmech:chlorite | data/records/chlorite.yaml | maintained | Chlorite group |
| cmmmech:chromite-beneficiation-tailings | data/records/chromite-beneficiation-tailings.yaml | maintained | Chromite beneficiation tailings |
| cmmmech:chromite-ore-processing-residue | data/records/chromite-ore-processing-residue.yaml | maintained | Chromite ore processing residue |
| cmmmech:chromium | data/records/chromium.yaml | maintained | Chromium |
| cmmmech:chukanovite | data/records/chukanovite.yaml | maintained | Chukanovite |
| cmmmech:coal-beneficiation-waste | data/records/coal-beneficiation-waste.yaml | maintained | Coal beneficiation waste |
| cmmmech:colemanite | data/records/colemanite.yaml | maintained | Colemanite |
| cmmmech:copper-smelter-flue-dust | data/records/copper-smelter-flue-dust.yaml | maintained | Copper-smelter flue dust |
| cmmmech:copper-smelter-slag | data/records/copper-smelter-slag.yaml | maintained | Copper smelter slag |
| cmmmech:copper | data/records/copper.yaml | maintained | Copper |
| cmmmech:discarded-led-lamps | data/records/discarded-led-lamps.yaml | maintained | Discarded light-emitting-diode lamps |
| cmmmech:dittmarite | data/records/dittmarite.yaml | maintained | Dittmarite |
| cmmmech:djurleite | data/records/djurleite.yaml | maintained | Djurleite |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |
| cmmmech:electric-arc-furnace-dust | data/records/electric-arc-furnace-dust.yaml | maintained | Electric-arc-furnace dust |
| cmmmech:electroformed-copper-silver-manufacturing-scrap | data/records/electroformed-copper-silver-manufacturing-scrap.yaml | maintained | Electroformed copper-silver manufacturing scrap |
| cmmmech:electroplating-sludge | data/records/electroplating-sludge.yaml | maintained | Electroplating sludge |
| cmmmech:enargite-pyrite-concentrate | data/records/enargite-pyrite-concentrate.yaml | maintained | Enargite-pyrite concentrate |
| cmmmech:enstatite | data/records/enstatite.yaml | maintained | Enstatite |
| cmmmech:eudialyte-ore | data/records/eudialyte-ore.yaml | maintained | Eudialyte ore |
| cmmmech:falottaite | data/records/falottaite.yaml | maintained | Falottaite |
| cmmmech:feitknechtite | data/records/feitknechtite.yaml | maintained | Feitknechtite |
| cmmmech:feroxyhyte | data/records/feroxyhyte.yaml | maintained | Feroxyhyte |
| cmmmech:ferrihydrite | data/records/ferrihydrite.yaml | maintained | Ferrihydrite |
| cmmmech:fish-bone-residues | data/records/fish-bone-residues.yaml | maintained | Fish-bone residues |
| cmmmech:fluorapatite | data/records/fluorapatite.yaml | maintained | Fluorapatite |
| cmmmech:fluorescent-lamp-phosphor | data/records/fluorescent-lamp-phosphor.yaml | maintained | Spent fluorescent-lamp phosphor powder |
| cmmmech:fluorine | data/records/fluorine.yaml | maintained | Fluorine |
| cmmmech:forsterite | data/records/forsterite.yaml | maintained | Forsterite |
| cmmmech:gaas-production-hydroxide-sludge | data/records/gaas-production-hydroxide-sludge.yaml | maintained | GaAs wafer-production hydroxide sludge |
| cmmmech:galena | data/records/galena.yaml | maintained | Galena |
| cmmmech:gallium | data/records/gallium.yaml | maintained | Gallium |
| cmmmech:glushinskite | data/records/glushinskite.yaml | maintained | Glushinskite |
| cmmmech:goethite | data/records/goethite.yaml | maintained | Goethite |
| cmmmech:gold-mine-tailings | data/records/gold-mine-tailings.yaml | maintained | Gold-mine tailings |
| cmmmech:greigite | data/records/greigite.yaml | maintained | Greigite |
| cmmmech:hafnium | data/records/hafnium.yaml | maintained | Hafnium |
| cmmmech:hausmannite | data/records/hausmannite.yaml | maintained | Hausmannite |
| cmmmech:heavy-fuel-oil-combustion-ash | data/records/heavy-fuel-oil-combustion-ash.yaml | maintained | Heavy-fuel-oil combustion ash |
| cmmmech:hollandite | data/records/hollandite.yaml | maintained | Hollandite |
| cmmmech:hopeite | data/records/hopeite.yaml | maintained | Hopeite |
| cmmmech:humboldtine | data/records/humboldtine.yaml | maintained | Humboldtine |
| cmmmech:hydroxylapatite | data/records/hydroxylapatite.yaml | maintained | Hydroxylapatite |
| cmmmech:illite | data/records/illite.yaml | maintained | Illite group |
| cmmmech:ion-adsorption-rare-earth-leach-residue | data/records/ion-adsorption-rare-earth-leach-residue.yaml | maintained | Ion-adsorption rare-earth leach residue |
| cmmmech:iron | data/records/iron.yaml | maintained | Iron |
| cmmmech:jadarite | data/records/jadarite.yaml | maintained | Jadarite |
| cmmmech:jarosite | data/records/jarosite.yaml | maintained | Jarosite |
| cmmmech:kaolin | data/records/kaolin.yaml | maintained | Natural kaolin feed |
| cmmmech:katsarosite | data/records/katsarosite.yaml | maintained | Katsarosite |
| cmmmech:kesterite | data/records/kesterite.yaml | maintained | Kësterite |
| cmmmech:lanthanum | data/records/lanthanum.yaml | maintained | Lanthanum |
| cmmmech:lepidocrocite | data/records/lepidocrocite.yaml | maintained | Lepidocrocite |
| cmmmech:lindbergite | data/records/lindbergite.yaml | maintained | Lindbergite |
| cmmmech:lithium-bearing-geothermal-brine | data/records/lithium-bearing-geothermal-brine.yaml | maintained | Lithium-bearing geothermal brine |
| cmmmech:lithium-mica-ore | data/records/lithium-mica-ore.yaml | maintained | Lithium-mica ore |
| cmmmech:lithium | data/records/lithium.yaml | maintained | Lithium |
| cmmmech:lutetium | data/records/lutetium.yaml | maintained | Lutetium |
| cmmmech:mackinawite | data/records/mackinawite.yaml | maintained | Mackinawite |
| cmmmech:magnesium | data/records/magnesium.yaml | maintained | Magnesium |
| cmmmech:magnetite | data/records/magnetite.yaml | maintained | Magnetite |
| cmmmech:malachite | data/records/malachite.yaml | maintained | Malachite |
| cmmmech:manganese-ore | data/records/manganese-ore.yaml | maintained | Manganese ore |
| cmmmech:manganese | data/records/manganese.yaml | maintained | Manganese |
| cmmmech:manganite | data/records/manganite.yaml | maintained | Manganite |
| cmmmech:marcasite | data/records/marcasite.yaml | maintained | Marcasite |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |
| cmmmech:metal-grinding-sludge | data/records/metal-grinding-sludge.yaml | maintained | Metal grinding sludge |
| cmmmech:metallic-machining-burrs | data/records/metallic-machining-burrs.yaml | maintained | Metallic machining burrs |
| cmmmech:metalliferous-black-shale | data/records/metalliferous-black-shale.yaml | maintained | Metalliferous black shale |
| cmmmech:millerite | data/records/millerite.yaml | maintained | Millerite |
| cmmmech:mimetite | data/records/mimetite.yaml | maintained | Mimetite |
| cmmmech:molybdenite | data/records/molybdenite.yaml | maintained | Molybdenite |
| cmmmech:montmorillonite | data/records/montmorillonite.yaml | maintained | Montmorillonite |
| cmmmech:moolooite | data/records/moolooite.yaml | maintained | Moolooite |
| cmmmech:municipal-sewage-sludge | data/records/municipal-sewage-sludge.yaml | maintained | Municipal sewage sludge |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |
| cmmmech:nepheline | data/records/nepheline.yaml | maintained | Nepheline |
| cmmmech:nickel-based-superalloy-residue-powders | data/records/nickel-based-superalloy-residue-powders.yaml | maintained | Nickel-based superalloy residue powders |
| cmmmech:nickel-flotation-tailings | data/records/nickel-flotation-tailings.yaml | maintained | Nickel flotation tailings |
| cmmmech:nickel-laterite-ore | data/records/nickel-laterite-ore.yaml | maintained | Nickel laterite ore |
| cmmmech:nickel-smelter-slag | data/records/nickel-smelter-slag.yaml | maintained | Nickel smelter slag |
| cmmmech:nickel | data/records/nickel.yaml | maintained | Nickel |
| cmmmech:nontronite | data/records/nontronite.yaml | maintained | Nontronite |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |
| cmmmech:orpiment | data/records/orpiment.yaml | maintained | Orpiment |
| cmmmech:palladium | data/records/palladium.yaml | maintained | Palladium |
| cmmmech:palygorskite | data/records/palygorskite.yaml | maintained | Palygorskite |
| cmmmech:petroleum-coke | data/records/petroleum-coke.yaml | maintained | Petroleum coke |
| cmmmech:pharmaceutical-blister-packaging-waste | data/records/pharmaceutical-blister-packaging-waste.yaml | maintained | Pharmaceutical blister packaging waste |
| cmmmech:phosphate-ore-tailings | data/records/phosphate-ore-tailings.yaml | maintained | Phosphate-ore tailings |
| cmmmech:phosphate-rock | data/records/phosphate-rock.yaml | maintained | Phosphate rock |
| cmmmech:phosphogypsum | data/records/phosphogypsum.yaml | maintained | Phosphogypsum |
| cmmmech:phosphorus | data/records/phosphorus.yaml | maintained | Phosphorus |
| cmmmech:plumbojarosite | data/records/plumbojarosite.yaml | maintained | Plumbojarosite |
| cmmmech:polydymite | data/records/polydymite.yaml | maintained | Polydymite |
| cmmmech:ponded-coal-ash | data/records/ponded-coal-ash.yaml | maintained | Ponded mixed coal ash |
| cmmmech:poultry-bone-residues | data/records/poultry-bone-residues.yaml | maintained | Poultry-bone residues |
| cmmmech:praseodymium | data/records/praseodymium.yaml | maintained | Praseodymium |
| cmmmech:pyrite-roasting-cinder | data/records/pyrite-roasting-cinder.yaml | maintained | Pyrite-roasting cinder |
| cmmmech:pyrochroite | data/records/pyrochroite.yaml | maintained | Pyrochroite |
| cmmmech:rare-earth-element-commodities | data/records/rare-earth-element-commodities.yaml | maintained | Rare-earth-element commodities, Australian list scope |
| cmmmech:realgar | data/records/realgar.yaml | maintained | Realgar |
| cmmmech:rhodium | data/records/rhodium.yaml | maintained | Rhodium |
| cmmmech:rhodochrosite | data/records/rhodochrosite.yaml | maintained | Rhodochrosite |
| cmmmech:rutile | data/records/rutile.yaml | maintained | Rutile |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |
| cmmmech:schwertmannite | data/records/schwertmannite.yaml | maintained | Schwertmannite |
| cmmmech:scorodite | data/records/scorodite.yaml | maintained | Scorodite |
| cmmmech:seafloor-massive-sulfides | data/records/seafloor-massive-sulfides.yaml | maintained | Seafloor massive sulfides |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |
| cmmmech:silica-sand | data/records/silica-sand.yaml | maintained | Natural silica-sand feed |
| cmmmech:silicon | data/records/silicon.yaml | maintained | Silicon |
| cmmmech:silver | data/records/silver.yaml | maintained | Silver |
| cmmmech:skutterudite | data/records/skutterudite.yaml | maintained | Skutterudite |
| cmmmech:smithsonite | data/records/smithsonite.yaml | maintained | Smithsonite |
| cmmmech:spent-alkaline-zinc-carbon-batteries | data/records/spent-alkaline-zinc-carbon-batteries.yaml | maintained | Spent alkaline and zinc-carbon batteries |
| cmmmech:spent-automotive-three-way-catalyst | data/records/spent-automotive-three-way-catalyst.yaml | maintained | Spent automotive three-way catalyst |
| cmmmech:spent-fluid-catalytic-cracking-catalyst | data/records/spent-fluid-catalytic-cracking-catalyst.yaml | maintained | Spent fluid catalytic cracking catalyst |
| cmmmech:spent-hydrodesulfurization-catalyst | data/records/spent-hydrodesulfurization-catalyst.yaml | maintained | Spent hydrodesulfurization catalyst |
| cmmmech:spent-nickel-cadmium-batteries | data/records/spent-nickel-cadmium-batteries.yaml | maintained | Spent nickel-cadmium batteries |
| cmmmech:spent-nickel-metal-hydride-batteries | data/records/spent-nickel-metal-hydride-batteries.yaml | maintained | Spent nickel-metal-hydride batteries |
| cmmmech:spent-selective-catalytic-reduction-catalyst | data/records/spent-selective-catalytic-reduction-catalyst.yaml | maintained | Spent selective catalytic reduction catalyst |
| cmmmech:spent-silver-oxide-zinc-button-cell-batteries | data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml | maintained | Spent silver-oxide–zinc button-cell batteries |
| cmmmech:spent-steel-pickling-liquors | data/records/spent-steel-pickling-liquors.yaml | maintained | Spent steel-pickling liquors |
| cmmmech:spent-sulfuric-acid-production-catalyst | data/records/spent-sulfuric-acid-production-catalyst.yaml | maintained | Spent sulfuric-acid-production catalyst |
| cmmmech:sphalerite | data/records/sphalerite.yaml | maintained | Sphalerite |
| cmmmech:spodumene | data/records/spodumene.yaml | maintained | Spodumene |
| cmmmech:stannite | data/records/stannite.yaml | maintained | Stannite |
| cmmmech:strontianite | data/records/strontianite.yaml | maintained | Strontianite |
| cmmmech:struvite | data/records/struvite.yaml | maintained | Struvite |
| cmmmech:talc | data/records/talc.yaml | maintained | Talc |
| cmmmech:tannery-sludge | data/records/tannery-sludge.yaml | maintained | Tannery sludge |
| cmmmech:tennantite-concentrate | data/records/tennantite-concentrate.yaml | maintained | Tennantite concentrate |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |
| cmmmech:thallium | data/records/thallium.yaml | maintained | Thallium |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |
| cmmmech:titanium-metal | data/records/titanium-metal.yaml | maintained | Titanium metal |
| cmmmech:titanium | data/records/titanium.yaml | maintained | Titanium |
| cmmmech:traction-battery-hydrometallurgical-residue | data/records/traction-battery-hydrometallurgical-residue.yaml | maintained | Traction-battery hydrometallurgical residue |
| cmmmech:uraninite | data/records/uraninite.yaml | maintained | Uraninite |
| cmmmech:uranium | data/records/uranium.yaml | maintained | Uranium |
| cmmmech:used-photographic-fixer-solutions | data/records/used-photographic-fixer-solutions.yaml | maintained | Used photographic fixer solutions |
| cmmmech:vaesite | data/records/vaesite.yaml | maintained | Vaesite |
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
| just validate (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:anglesite, cmmmech:argentojarosite, cmmmech:arsenic, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:baricite, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:blast-furnace-cast-house-dust, cmmmech:borates, cmmmech:bornite, cmmmech:boron-ore-concentration-tailings, cmmmech:brushite, cmmmech:calcite, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:cerium, cmmmech:cerussite, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:chalcopyrite, cmmmech:chlorite, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:chukanovite, cmmmech:coal-beneficiation-waste, cmmmech:colemanite, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:copper, cmmmech:discarded-led-lamps, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electric-arc-furnace-dust, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electroplating-sludge, cmmmech:enargite-pyrite-concentrate, cmmmech:enstatite, cmmmech:eudialyte-ore, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:feroxyhyte, cmmmech:ferrihydrite, cmmmech:fish-bone-residues, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:gaas-production-hydroxide-sludge, cmmmech:galena, cmmmech:gallium, cmmmech:glushinskite, cmmmech:goethite, cmmmech:gold-mine-tailings, cmmmech:greigite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:illite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lepidocrocite, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:lithium, cmmmech:lutetium, cmmmech:mackinawite, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese-ore, cmmmech:manganese, cmmmech:manganite, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:metalliferous-black-shale, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:municipal-sewage-sludge, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-laterite-ore, cmmmech:nickel-smelter-slag, cmmmech:nickel, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:palygorskite, cmmmech:petroleum-coke, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:praseodymium, cmmmech:pyrite-roasting-cinder, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:rutile, cmmmech:scandium, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:seafloor-massive-sulfides, cmmmech:selenium, cmmmech:silica-sand, cmmmech:silicon, cmmmech:silver, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tannery-sludge, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:thallium, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:titanium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:used-photographic-fixer-solutions, cmmmech:vaesite, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All 182 causal_graphs cohort records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (causal_graphs cohort) | passed | True | cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:anglesite, cmmmech:argentojarosite, cmmmech:arsenic, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:baricite, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:blast-furnace-cast-house-dust, cmmmech:borates, cmmmech:bornite, cmmmech:boron-ore-concentration-tailings, cmmmech:brushite, cmmmech:calcite, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:cerium, cmmmech:cerussite, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:chalcopyrite, cmmmech:chlorite, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:chukanovite, cmmmech:coal-beneficiation-waste, cmmmech:colemanite, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:copper, cmmmech:discarded-led-lamps, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electric-arc-furnace-dust, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electroplating-sludge, cmmmech:enargite-pyrite-concentrate, cmmmech:enstatite, cmmmech:eudialyte-ore, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:feroxyhyte, cmmmech:ferrihydrite, cmmmech:fish-bone-residues, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:gaas-production-hydroxide-sludge, cmmmech:galena, cmmmech:gallium, cmmmech:glushinskite, cmmmech:goethite, cmmmech:gold-mine-tailings, cmmmech:greigite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:illite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lepidocrocite, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:lithium, cmmmech:lutetium, cmmmech:mackinawite, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese-ore, cmmmech:manganese, cmmmech:manganite, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:metalliferous-black-shale, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:municipal-sewage-sludge, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-laterite-ore, cmmmech:nickel-smelter-slag, cmmmech:nickel, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:palygorskite, cmmmech:petroleum-coke, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:praseodymium, cmmmech:pyrite-roasting-cinder, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:rutile, cmmmech:scandium, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:seafloor-massive-sulfides, cmmmech:selenium, cmmmech:silica-sand, cmmmech:silicon, cmmmech:silver, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tannery-sludge, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:thallium, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:titanium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:used-photographic-fixer-solutions, cmmmech:vaesite, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite | All 182 causal_graphs cohort records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### Causal-graph DAG topology, mechanism-node protein_examples synchronization, and source-backed edge prose

evidence: supported. Targets: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:anglesite, cmmmech:argentojarosite, cmmmech:arsenic, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:baricite, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:blast-furnace-cast-house-dust, cmmmech:borates, cmmmech:bornite, cmmmech:boron-ore-concentration-tailings, cmmmech:brushite, cmmmech:calcite, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:cerium, cmmmech:cerussite, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:chalcopyrite, cmmmech:chlorite, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:chukanovite, cmmmech:coal-beneficiation-waste, cmmmech:colemanite, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:copper, cmmmech:discarded-led-lamps, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electric-arc-furnace-dust, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electroplating-sludge, cmmmech:enargite-pyrite-concentrate, cmmmech:enstatite, cmmmech:eudialyte-ore, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:feroxyhyte, cmmmech:ferrihydrite, cmmmech:fish-bone-residues, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:gaas-production-hydroxide-sludge, cmmmech:galena, cmmmech:gallium, cmmmech:glushinskite, cmmmech:goethite, cmmmech:gold-mine-tailings, cmmmech:greigite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:illite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lepidocrocite, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:lithium, cmmmech:lutetium, cmmmech:mackinawite, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese-ore, cmmmech:manganese, cmmmech:manganite, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:metalliferous-black-shale, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:municipal-sewage-sludge, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-laterite-ore, cmmmech:nickel-smelter-slag, cmmmech:nickel, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:palygorskite, cmmmech:petroleum-coke, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:praseodymium, cmmmech:pyrite-roasting-cinder, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:rutile, cmmmech:scandium, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:seafloor-massive-sulfides, cmmmech:selenium, cmmmech:silica-sand, cmmmech:silicon, cmmmech:silver, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tannery-sludge, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:thallium, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:titanium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:used-photographic-fixer-solutions, cmmmech:vaesite, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite.

All 182 causal_graphs records pass DAG, reference-closure, and UniProtKB protein_examples synchronization checks (640 mechanism-level and 640 node-level protein_examples across 139 unique accessions). Identified 3 minor graph findings across 5 records (enstatite, olivine-group, dunite, metacinnabar, scandium).

## Findings

### cmmmech-cycle11-stage4-finding-0001: Gluconobacter oxydans silicate bioleaching causal graphs in enstatite.yaml, olivine-group.yaml, and dunite.yaml retain generic template node/edge explanations and unqualified pqqC/gdh support in dunite.yaml

minor / open / confirmed; issue key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support.

Across the three Gluconobacter oxydans whole-culture biolixiviant silicate bioleaching records — data/records/enstatite.yaml (cmmmech:enstatite, mineral, Klug et al. 2026 Scientific Reports 16:25317, DOI:10.1038/s41598-026-63817-0, klug_2026; causal_graphs[0] gluconobacter_enstatite_bioleaching_graph, lines 143-321), data/records/olivine-group.yaml (cmmmech:olivine-group, mineral_group, Klug et al. 2026, klug_2026; causal_graphs[0] gluconobacter_olivine_bioleaching_graph, lines 143-321), and data/records/dunite.yaml (cmmmech:dunite, primary_resource, Lee et al. 2025 Scientific Reports 15:15134, DOI:10.1038/s41598-025-99655-9, lee2025; causal_graphs[0] gluconobacter_dunite_bioleaching_graph, lines 159-337) — data/records/enstatite.yaml nodes[4].description (enstatite_mixed_feed, line 269) retains the generic parenthetical template string repeating the capitalized node label verbatim ('Starting solid substrate (Enstatite-bearing mixed silicate feed) exposed to the acidic biolixiviant.') instead of specifying the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate powder leached at 5% w/v (0.5 g per 10 mL liquid) without a pure-enstatite control (mechanisms[0].context, lines 31-32). Furthermore, edges[1].evidence[0].explanation (line 294 in enstatite.yaml and olivine-group.yaml; line 310 in dunite.yaml) and edges[2].evidence[0].explanation (line 303 in enstatite.yaml and olivine-group.yaml; line 319 in dunite.yaml) retain identical generic one-line template strings ('PQQ-dependent glucose dehydrogenase activity drives gluconic-acid biolixiviant production in Gluconobacter oxydans.' and 'Periplasmic glucose oxidation by G. oxydans generates the acidic gluconic-acid-rich biolixiviant.'), and edges[0].evidence[0].explanation in enstatite.yaml and olivine-group.yaml (line 285) omits that the engineered strain combined pstS deletion with the P112:mgdh promoter swap. Additionally, in data/records/dunite.yaml, mechanisms[0].protein_examples[2..3].evidence[0] (lines 105-107 and 130-132 for UniProtKB:Q9L3B2 pqqC and UniProtKB:P27175 gdh), causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0] (lines 242-244 and 274-276), and causal_graphs[0].edges[1..2].evidence[0] (lines 308-310 and 317-319) assert supports: support with generic template explanations, whereas Lee et al. (2025) compared wild-type G. oxydans NRRL B-58 (initial pH 2.39 +/- 0.02) and engineered B58 delta-pstS, P112:mgdh (initial pH 2.01 +/- 0.02) whole-culture biolixiviants without single-gene knockouts or purified-enzyme assays isolating pqqC or mgdh (supports: partial, matching enstatite.yaml and olivine-group.yaml). In this scope, 3 record(s) (enstatite, olivine-group, dunite) are affected.

### cmmmech-cycle11-stage4-finding-0002: Thiobacillus thioparus metacinnabar record and causal graph misstate primary natural museum metacinnabar feed as synthetic beta-HgS in SoxB protein evidence and assert unqualified soluble-Hg(II) accumulation edge support

minor / open / confirmed; issue key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support.

In data/records/metacinnabar.yaml (cmmmech:metacinnabar, mineral, Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596, vazquez_rodriguez2015), mechanisms[0].protein_examples[0].evidence[0].explanation (lines 118-120) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation (lines 192-194) for UniProtKB:U5TVQ7 (soxB, Thiobacillus thioparus) state that Vazquez-Rodriguez et al. (2015) studied 'axenic Thiobacillus thioparus ATCC 8158 pure-culture dissolution of synthetic metacinnabar (beta-HgS)', whereas mechanisms[0].context (lines 45-51) and mechanisms[0].evidence[0..4] (lines 58-97) establish that the primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural museum metacinnabar (&lt;250 um, containing pyritic inclusions, autoclaved under N2), with commercial synthetic black HgS tested only in the separate daily-thiosulfate-spike comparison (Figures 6-7). Furthermore, in causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph, lines 157-291), nodes[1].description (metacinnabar_substrate, line 198) omits the 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions) versus synthetic black HgS feed distinction; edges[1] (metacinnabar_substrate -&gt; dissolved_hg2_species, lines 265-273) asserts supports: support with description: 'Oxidation of beta-HgS releases soluble Hg(II) into the medium.' and explanation: 'Dissolved Hg(II) accumulates as an intermediate during beta-HgS bio-oxidation.', even though mechanisms[0].evidence[0..2] (lines 58-81) document that aqueous Hg remained relatively low in viable T. thioparus incubations (because mobilized Hg was reduced to volatile Hg(0)) while killed-cell and thiosulfate controls showed substantial chemical Hg release and inoculum elemental-sulfur carryover (supports: partial); and edges[0].evidence[0].explanation (line 264), edges[2].evidence[0].explanation (line 282), and edges[3].evidence[0].explanation (line 291) retain generic one-line strings omitting the Table 1 sulfate-proxy dissolution estimate (48-68% after carryover correction, Figure S3), the 285-bp merA PCR amplicon in Supplementary Data S1 (genetic potential only, without expression or mutagenesis), and gold-trap cold-vapor atomic fluorescence spectroscopy (CVAFS) volatile-Hg measurements. In this scope, 1 record(s) (metacinnabar) are affected.

### cmmmech-cycle11-stage4-finding-0003: Mex-LanM scandium chromatography record and causal graph misdescribe pH 5.0 malonate elution from a synthetic 16-REE chloride feed as mild acid stripping of transition/base metals from a multi-metal leachate

minor / open / confirmed; issue key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording.

In data/records/scandium.yaml (cmmmech:scandium, element, Dong et al. 2024 Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919, dong2024), mechanisms[0].protein_examples[0].evidence[0] (lines 64-66) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0] (lines 109-111) for UniProtKB:C5B164 (lanM / Mex-LanM) assert supports: support with explanation: 'Immobilized Mex-LanM selectively binds Sc(III) over competing transition/base metals and elutes high-purity scandium upon mild acid stripping.', whereas mechanisms[0].description (line 39), mechanisms[0].context (line 40), and mechanisms[0].evidence[0..1] (lines 68-73) establish that Dong et al. (2024) Section 3.4 and Figures 3C and 5E-F tested a synthetic 16-REE chloride-salt mixture at pH 3.0 (nominal 0.4 mM total REE in Figure 5, summing to 0.2430 mM across 16 REEs with 23.8 +/- 1.1 uM Sc in supplement Table S10, labeled Table S9 in the caption) and eluted Sc(III) selectively using stepwise 30 mM and 50 mM malonate at pH 5.0 (not mild acid stripping of transition/base metals), without a matched Sc-only resin-without-LanM control (supports: partial). Furthermore, in causal_graphs[0] (immobilized_mex_lanm_scandium_separation_graph, lines 78-140), causal_graphs[0].description (line 80), nodes[1].label and nodes[1].description (mixed_scandium_feed, lines 113-115), nodes[2].description (purified_scandium_eluate, line 120), and edges[1] (lines 135-140) describe the Figure 5 column input as a 'mixed leachate feed' / 'multi-metal leachate' rather than a synthetic pH 3.0 chloride-salt REE solution resembling selected leachate compositions (mechanisms[0].context, line 40), and edges[0] (mex_lanm_protein -&gt; mixed_scandium_feed, lines 123-131) uses a generic 78-character explanation ('Immobilized LanM columns selectively retain Sc(III) from multi-metal mixtures.') with supports: support that omits the Table S9/S10 feed-concentration discrepancy (0.4 mM nominal vs 0.2430 mM sum) and the absence of a matched Sc-only resin-without-LanM control (mechanisms[0].evidence[1], supports: partial). In this scope, 1 record(s) (scandium) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-gluconobacter-enstatite-olivine-dunite-graphs

Replace the generic parenthetical template description on enstatite.yaml nodes[4].description (enstatite_mixed_feed), replace generic template explanations on edges[0..2].evidence[0].explanation in data/records/enstatite.yaml and data/records/olivine-group.yaml and edges[1..2].evidence[0].explanation in data/records/dunite.yaml with study-specific prose citing Klug et al. (2026) and Lee et al. (2025), and qualify dunite.yaml mechanisms[0].protein_examples[2..3].evidence[0].supports, causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0].supports, and causal_graphs[0].edges[1..2].evidence[0].supports to partial during Stage 5 grouped remediation with canonical history provenance.

- enstatite.yaml causal_graphs[0].nodes[4].description specifies the ~40 um milled, ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate feed (5% w/v) without template label duplication.
- edges[0..2].evidence[0].explanation in enstatite.yaml and olivine-group.yaml and edges[1..2].evidence[0].explanation in dunite.yaml replace generic template strings with study-specific klug_2026 and lee2025 prose.
- dunite.yaml mechanisms[0].protein_examples[2..3], causal_graphs[0].nodes[1..2].protein_examples[0], and causal_graphs[0].edges[1..2] use supports: partial with Synchronized study-specific explanations.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

### act-refine-vazquez-rodriguez2015-metacinnabar-graph-and-soxb-evidence

Update mechanisms[0].protein_examples[0].evidence[0].explanation, causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation, and causal_graphs[0].nodes[1].description in data/records/metacinnabar.yaml to distinguish the primary 2 g/L ground natural museum metacinnabar (&lt;250 um, containing pyritic inclusions, Figures 3-5, Table 1) from the synthetic black HgS daily-thiosulfate-spike comparison (Figures 6-7), qualify causal_graphs[0].edges[1].evidence[0].supports to partial with accurate aqueous-Hg vs volatile-Hg(0) partitioning prose, and replace generic one-line explanations on edges[0..3] during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] in metacinnabar.yaml remain byte-identical and accurately distinguish natural museum metacinnabar (&lt;250 um) from synthetic black HgS.
- causal_graphs[0].nodes[1].description and edges[0..3] in metacinnabar.yaml use vazquez_rodriguez2015-specific prose with supports: partial on edges[1].
- Matching EDIT history sidecar exists in history/records/metacinnabar/ and passes just check.

### act-refine-dong2024-scandium-mex-lanm-graph-and-protein-evidence

Update mechanisms[0].protein_examples[0].evidence[0] and causal_graphs[0].nodes[0].protein_examples[0].evidence[0] in data/records/scandium.yaml to supports: partial with synchronized prose describing selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride mixture and stepwise 30 mM / 50 mM malonate elution at pH 5.0 (above 99 mol% purity among REEs and above 99% two-step yield; ~94.5% Sc yield at 30 mM malonate, Figures 3C and 5E-F, Table S9/S10), and update causal_graphs[0].description, nodes[1..2], and edges[0..1] (with supports: partial on edges[0]) during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] in scandium.yaml are synchronized with supports: partial and specify stepwise pH 5.0 malonate elution (30 mM and 50 mM) from a synthetic 16-REE chloride feed rather than mild acid stripping.
- causal_graphs[0].description, nodes[1..2], and edges[0..1] in scandium.yaml accurately describe the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM sum in Table S9/S10) and qualify edges[0].evidence[0].supports to partial.
- Matching EDIT history sidecar exists in history/records/scandium/ and passes just check.

## Category Boundaries

- retain: cmmmech:akaganeite, cmmmech:allanite-concentrate, cmmmech:allanite-leachate, cmmmech:aluminium, cmmmech:ammoniojarosite, cmmmech:anatase, cmmmech:anglesite, cmmmech:argentojarosite, cmmmech:arsenic, cmmmech:arsenopyrite, cmmmech:asbolane, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:baricite, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:birnessite, cmmmech:bixbyite-mn, cmmmech:blast-furnace-cast-house-dust, cmmmech:borates, cmmmech:bornite, cmmmech:boron-ore-concentration-tailings, cmmmech:brushite, cmmmech:calcite, cmmmech:cassiterite-polymetallic-sulfide-ore, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:cerium, cmmmech:cerussite, cmmmech:chalcopyrite-enargite-concentrate, cmmmech:chalcopyrite, cmmmech:chlorite, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium, cmmmech:chukanovite, cmmmech:coal-beneficiation-waste, cmmmech:colemanite, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:copper, cmmmech:discarded-led-lamps, cmmmech:dittmarite, cmmmech:djurleite, cmmmech:dunite, cmmmech:electric-arc-furnace-dust, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electroplating-sludge, cmmmech:enargite-pyrite-concentrate, cmmmech:enstatite, cmmmech:eudialyte-ore, cmmmech:falottaite, cmmmech:feitknechtite, cmmmech:feroxyhyte, cmmmech:ferrihydrite, cmmmech:fish-bone-residues, cmmmech:fluorapatite, cmmmech:fluorescent-lamp-phosphor, cmmmech:fluorine, cmmmech:forsterite, cmmmech:gaas-production-hydroxide-sludge, cmmmech:galena, cmmmech:gallium, cmmmech:glushinskite, cmmmech:goethite, cmmmech:gold-mine-tailings, cmmmech:greigite, cmmmech:hafnium, cmmmech:hausmannite, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:hollandite, cmmmech:hopeite, cmmmech:humboldtine, cmmmech:hydroxylapatite, cmmmech:illite, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron, cmmmech:jadarite, cmmmech:jarosite, cmmmech:kaolin, cmmmech:katsarosite, cmmmech:kesterite, cmmmech:lanthanum, cmmmech:lepidocrocite, cmmmech:lindbergite, cmmmech:lithium-bearing-geothermal-brine, cmmmech:lithium-mica-ore, cmmmech:lithium, cmmmech:lutetium, cmmmech:mackinawite, cmmmech:magnesium, cmmmech:magnetite, cmmmech:malachite, cmmmech:manganese-ore, cmmmech:manganese, cmmmech:manganite, cmmmech:marcasite, cmmmech:metacinnabar, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:metalliferous-black-shale, cmmmech:millerite, cmmmech:mimetite, cmmmech:molybdenite, cmmmech:montmorillonite, cmmmech:moolooite, cmmmech:municipal-sewage-sludge, cmmmech:neodymium, cmmmech:nepheline, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-laterite-ore, cmmmech:nickel-smelter-slag, cmmmech:nickel, cmmmech:nontronite, cmmmech:olivine-group, cmmmech:orpiment, cmmmech:palladium, cmmmech:palygorskite, cmmmech:petroleum-coke, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphate-rock, cmmmech:phosphogypsum, cmmmech:phosphorus, cmmmech:plumbojarosite, cmmmech:polydymite, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:praseodymium, cmmmech:pyrite-roasting-cinder, cmmmech:pyrochroite, cmmmech:rare-earth-element-commodities, cmmmech:realgar, cmmmech:rhodium, cmmmech:rhodochrosite, cmmmech:rutile, cmmmech:scandium, cmmmech:schwertmannite, cmmmech:scorodite, cmmmech:seafloor-massive-sulfides, cmmmech:selenium, cmmmech:silica-sand, cmmmech:silicon, cmmmech:silver, cmmmech:skutterudite, cmmmech:smithsonite, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:sphalerite, cmmmech:spodumene, cmmmech:stannite, cmmmech:strontianite, cmmmech:struvite, cmmmech:talc, cmmmech:tannery-sludge, cmmmech:tennantite-concentrate, cmmmech:tetrahedrite-concentrate, cmmmech:thallium, cmmmech:thulium, cmmmech:titanium-metal, cmmmech:titanium, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:uraninite, cmmmech:uranium, cmmmech:used-photographic-fixer-solutions, cmmmech:vaesite, cmmmech:vanadium, cmmmech:vaterite, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-x-ray-films, cmmmech:wheatleyite, cmmmech:whewellite, cmmmech:zinc, cmmmech:zincite. All 182 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where bool(causal_graphs) is True at 794684703f77385b6e9bca32167f6c8d1e5e29bf with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-causal-graphs-cohort-audit | data/records/*.yaml (bool(causal_graphs) == True); 182 causal_graphs YAML files | supports | Full programmatic and source-backed audit of all 182 causal_graphs records at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf. |
| ev-gluconobacter-silicate-graphs | data/records/{enstatite,olivine-group,dunite}.yaml; enstatite.yaml lines 143-321; olivine-group.yaml lines 143-321; dunite.yaml lines 83-133, 159-337 | supports | In enstatite.yaml, olivine-group.yaml, and dunite.yaml, Gluconobacter oxydans causal graphs retain generic template node/edge explanations, and dunite.yaml asserts unqualified supports: support on pqqC and gdh protein_examples and edges[1..2]. |
| ev-vazquez-rodriguez2015-metacinnabar-graph | data/records/metacinnabar.yaml; mechanisms[0] (lines 43-120); causal_graphs[0] (lines 157-291) | supports | In data/records/metacinnabar.yaml, SoxB protein_examples[0] states 'synthetic metacinnabar (beta-HgS)' whereas Vazquez-Rodriguez et al. (2015) primarily leached natural museum metacinnabar (&lt;250 um), and edges[1] asserts supports: support for soluble Hg(II) accumulation. |
| ev-dong2024-scandium-graph | data/records/scandium.yaml; mechanisms[0] (lines 36-74); causal_graphs[0] (lines 78-140) | supports | In data/records/scandium.yaml, Mex-LanM protein_examples[0] asserts supports: support with 'mild acid stripping' over 'transition/base metals' instead of stepwise pH 5.0 malonate elution from a synthetic 16-REE chloride feed, and causal_graphs[0] describes the feed as a 'mixed leachate feed'. |

## Limits And Additional Notes

- 6 of 182 causal_graphs records (cmmmech:erbium, cmmmech:ferrihydrite, cmmmech:gold, cmmmech:lindbergite, cmmmech:magnetite, cmmmech:terbium) contain 1 explicitly UNGROUNDED GENE_OR_PROTEIN node each because the cited primary literature did not sequence the strain or resolve a specific protein accession.
- 5 records (enstatite, olivine-group, dunite, metacinnabar, scandium) carry minor causal-graph and protein_examples prose/support findings tracked as open findings cmmmech-cycle11-stage4-finding-0001..0003 for Stage 5 grouped remediation.
- Cohort covers 100% (182/182) of records with causal_graphs in data/records/*.yaml at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T041506Z-cycle11-stage4-causal-graphs-cohort-review
title: 'Cycle 11 Stage 4 cross-cohort review: causal_graphs & protein_examples records
  (182/182)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-11-09T04:06:00Z'
finished_at: '2026-11-09T04:15:06Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 182 records in data/records/*.yaml that carry causal_graphs
  at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf (30 element, 78 mineral, 3 mineral_group,
  4 commodity, 16 primary_resource, 51 secondary_resource), including the 10 records
  expanded in Cycle 11 Stage 2 (PR #960, commit df061de7) and Stage 3 (PR #963, commit
  79468470): chukanovite, feroxyhyte, illite, lepidocrocite, manganite, palygorskite,
  plumbojarosite, silica-sand, thallium, and titanium, as well as the 5 records remediated
  in Cycle 10 Stage 5 (PR #953, commit 09e04a33): calcite, vaterite, lithium-bearing-geothermal-brine,
  brushite, strontianite, and smithsonite. Across the 182 records, there are 191 causal_graphs,
  873 nodes, 682 edges, and 351 GENE_OR_PROTEIN nodes (345 GROUNDED across 179 records
  and 6 UNGROUNDED across 6 records: erbium, ferrihydrite, gold, lindbergite, magnetite,
  terbium), with 640 mechanism-level and 640 node-level protein_examples (1,280 total,
  100% synchronized) spanning 139 unique live-verified UniProtKB accessions (33 SWISS_PROT,
  106 TREMBL). Identified 3 minor graph findings across 5 records (cmmmech-cycle11-stage4-finding-0001
  on cmmmech:enstatite, cmmmech:olivine-group, and cmmmech:dunite; cmmmech-cycle11-stage4-finding-0002
  on cmmmech:metacinnabar; and cmmmech-cycle11-stage4-finding-0003 on cmmmech:scandium)
  for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 11 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
source:
  git_revision: 794684703f77385b6e9bca32167f6c8d1e5e29bf
  state: git_commit
  inputs:
  - path: data/records/akaganeite.yaml
    sha256: 7a5214f7def425bbbaf9d0bf440307d817a240e0fd4efe233ae4ca24a4c6c70e
    role: target
  - path: data/records/allanite-concentrate.yaml
    sha256: ba71a3f46b79fb93a742dcf7449344897cf9e6761d3e1d7750b819ae219fdc54
    role: target
  - path: data/records/allanite-leachate.yaml
    sha256: 32fe127fe3a3ce0400199d40c0545a85345b00bb0fda2a5078a539039c3a4e1c
    role: target
  - path: data/records/aluminium.yaml
    sha256: 8df6aa9f1e6f6b4fdb637c4026cfef6781c286c847e25153d0c126a67503fe13
    role: target
  - path: data/records/ammoniojarosite.yaml
    sha256: cec855c4014d35b9e6cfecd5684f6d730b887866df1751cee3683dfb399375e3
    role: target
  - path: data/records/anatase.yaml
    sha256: e6458835c3c5a41c4613ebe519662b54d1cf77ff5a3a0ebd704f61af5ce958ca
    role: target
  - path: data/records/anglesite.yaml
    sha256: 02a256a423239cd3b1138889233ec9a74fa0afc8450530ed3ce2543752db6a56
    role: target
  - path: data/records/argentojarosite.yaml
    sha256: b9bcc011760f6aa4e1c2740ad62da43d9281969cca41423413bee4be9a1d2044
    role: target
  - path: data/records/arsenic.yaml
    sha256: db6cce965d9da92e0e467a658aba89650641a2f2d085acc9235c9302c2a082d8
    role: target
  - path: data/records/arsenopyrite.yaml
    sha256: b624a3e9de6d7fbeb13d493ea73d78a17e17c48c6e0225fee08b1fa57402574f
    role: target
  - path: data/records/asbolane.yaml
    sha256: 848b70e5da57342f8abd4558de7e52fb666d132a9f4fbef7ebcd460d75f79dd7
    role: target
  - path: data/records/automotive-wastewater-treatment-sludge.yaml
    sha256: 3ecbb1148dac1955490a9828d000443b12d5b1e36c806f086faf9a3d9aa3e4a0
    role: target
  - path: data/records/baricite.yaml
    sha256: 167a929e8e64826814c574afec109e9f01c5af7fc72bd845a7207712b40862b4
    role: target
  - path: data/records/basic-oxygen-furnace-steelmaking-dust.yaml
    sha256: 74024f5da99c53b4f0f51fccd71b7f72833c18cdb7e99cd73a1bb00889c93982
    role: target
  - path: data/records/bauxite-residue.yaml
    sha256: fbad4371b1d3ffed508163dc947332d39f17190aa5b2367c40022caf7f1cab46
    role: target
  - path: data/records/beverage-carton-hydropulping-reject.yaml
    sha256: 017344bcb108e373627b1a02cda46ba1f237ded11640f8cec5281c57e4341828
    role: target
  - path: data/records/birnessite.yaml
    sha256: e00664ab82555de110a68f385089b83431cefa422ae53b115a072d6ce10d6728
    role: target
  - path: data/records/bixbyite-mn.yaml
    sha256: bd546f878977f8954f3c3fafb9ed52ea912984b23c53236452eb843f98ae3b81
    role: target
  - path: data/records/blast-furnace-cast-house-dust.yaml
    sha256: 187f2bb3e6b1b377c651fa230ccfa9d51a898fa3ca0ec324d116223d080ae417
    role: target
  - path: data/records/borates.yaml
    sha256: de224b4334408815751fbddd6892962bcae6eb4bffe628b485bd14780e59801f
    role: target
  - path: data/records/bornite.yaml
    sha256: d5dbb1caf28f566e6120734d16a6e13d1cf4a1d034bed06c7d780da7e64fe86e
    role: target
  - path: data/records/boron-ore-concentration-tailings.yaml
    sha256: f24b9ad8d3d2b37fee2d62f6a035dbf3e13cee4169810f9c5c875414a0bccbf6
    role: target
  - path: data/records/brushite.yaml
    sha256: dec5c219dc7b3718c7362cbc01b4f8fa09be1eac05d2b909ad2ed6fd675811da
    role: target
  - path: data/records/calcite.yaml
    sha256: 248ef894c4ae4443f301609137ac54314ea4acdfd86cb9f4cf4d74d50508bf48
    role: target
  - path: data/records/cassiterite-polymetallic-sulfide-ore.yaml
    sha256: aa9d75f7762e919fd7331ff82cdc90fc6dab9ce09683a38be355430dd5322e42
    role: target
  - path: data/records/cemented-tungsten-carbide-scrap.yaml
    sha256: bd8b37dcd07944d0f276a0f40edf879578c933cf2bf8a14d62b942d2e63c96c0
    role: target
  - path: data/records/cerium.yaml
    sha256: 7837cfe3c8dd804673181a9472a069e90cbcb9cba4503c4ce8e485235da5f618
    role: target
  - path: data/records/cerussite.yaml
    sha256: 28f48a58f6db01e26ef0b9a2e52b3aed0dbccd5cf4704ff14b69fda0e2bbaab8
    role: target
  - path: data/records/chalcopyrite-enargite-concentrate.yaml
    sha256: 2f48356455d8578b2b396225b3ffd728d6194d5453ac8fd41d9c9cd73055dab9
    role: target
  - path: data/records/chalcopyrite.yaml
    sha256: c52e2af1d7c3c96943eac69f3d5d43ed451b7a1b6219285a26edbd0c5a4b5322
    role: target
  - path: data/records/chlorite.yaml
    sha256: f26f20999e3df05bf5ce82b4fb141881e685d7f2a3bd43b69c577283dde26131
    role: target
  - path: data/records/chromite-beneficiation-tailings.yaml
    sha256: ca8ff5d800723ed8c1bb6e5a6d514cbae16ee27dd0d2400b524309fe244e5859
    role: target
  - path: data/records/chromite-ore-processing-residue.yaml
    sha256: 7d9f158c0b08285f9bc2f6e4eb620958078cab63f524dd5eda38ca53cac9c893
    role: target
  - path: data/records/chromium.yaml
    sha256: 2fa5feef5344357886d087965aac5b3449a68d07159aebd07638a085993c1eac
    role: target
  - path: data/records/chukanovite.yaml
    sha256: b81e8e65e9c8975be60c68836aabd8c05e008c9af352ed9a1db68e1a68bbf415
    role: target
  - path: data/records/coal-beneficiation-waste.yaml
    sha256: c2385ff7d5b4feef072886ea3513905ea3d084f78fe99c964a57a66c6459d478
    role: target
  - path: data/records/colemanite.yaml
    sha256: 0e1e9a2348a08c4dcc420e24f3ec265e309f35f4ed98e46e2bf47eb9124b8550
    role: target
  - path: data/records/copper-smelter-flue-dust.yaml
    sha256: 5f0ca8783e168e26296768dbfcafd564b972f12a82d11e8a81e9cc544392566e
    role: target
  - path: data/records/copper-smelter-slag.yaml
    sha256: 43f5812d94ef7f7c40173dbf2b0793a544aa5194522f8163a3e24c695c907b4c
    role: target
  - path: data/records/copper.yaml
    sha256: df7bd558794467c52b776f58a78c64ce12c3cb2da1cbd0da91e192b971da7078
    role: target
  - path: data/records/discarded-led-lamps.yaml
    sha256: 872552ec28cd80bca6dacee0ee4babfa8f571984e24ea729c189de7b03915de4
    role: target
  - path: data/records/dittmarite.yaml
    sha256: 104c3eddcadbbfa75c64cd226f56cff62b4015eee24eeb33e7061e4155ed723c
    role: target
  - path: data/records/djurleite.yaml
    sha256: dc1fd34e105bd5c37d03d4ff3b37277993a4a52e09a84d774641a4d627b85fda
    role: target
  - path: data/records/dunite.yaml
    sha256: 86bb3db03df8d248869605500412f495eae95ae9a408c803cbdeeeb7d0d8b2d7
    role: target
  - path: data/records/electric-arc-furnace-dust.yaml
    sha256: 31557f49a45a894dd499521dedcd75cade1e7b3b1def66f56896540afa4a2c83
    role: target
  - path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
    sha256: 19bf06af57737ec4d9c6ca0332f44a10036f7377e5152c57b9bd849dc0665503
    role: target
  - path: data/records/electroplating-sludge.yaml
    sha256: 52fe4cc69ac0807a77d921c2de8c35a25bf812c345ed1854b4b46c58e6cf281b
    role: target
  - path: data/records/enargite-pyrite-concentrate.yaml
    sha256: a3d694164065ec1746ed52154bd182f8808ace3d484a1d94213db51175e108a0
    role: target
  - path: data/records/enstatite.yaml
    sha256: b3fd3f1258b68a168c6f5ba7e59356b3507fd87ed51644f4f4ec3d4de2704d82
    role: target
  - path: data/records/eudialyte-ore.yaml
    sha256: ece4b1e3405e97cdee81ccb810e3104d9877950f160593e0ba3d0931ab85156f
    role: target
  - path: data/records/falottaite.yaml
    sha256: 0f3c1b1abb6dcbf9b3b5791ddd849cbf92e315cf877197c66686cea7a8236351
    role: target
  - path: data/records/feitknechtite.yaml
    sha256: 16b59b1f1d67f943d0c8c5edd8cd3730ea93bcde0a6e760b900b50bb05247f8a
    role: target
  - path: data/records/feroxyhyte.yaml
    sha256: c3b811cb9353b8b0cc47705a0c6051bb8625bb77cb7a3ccd73605d7a2963b829
    role: target
  - path: data/records/ferrihydrite.yaml
    sha256: 4ef266f47c11833c25999d545382bdc9831259541c720884bd07330f05ee1de3
    role: target
  - path: data/records/fish-bone-residues.yaml
    sha256: 86f8e14fb26f46f9e89c59c4aa164ebfda13ae6dd89fe02c86fe77af3a6e4554
    role: target
  - path: data/records/fluorapatite.yaml
    sha256: 5e9b8424433df9ec5424eaac63bd14abcaff19819a8407994d614cd1a24c7437
    role: target
  - path: data/records/fluorescent-lamp-phosphor.yaml
    sha256: cd27c40ce1c11eae898b561a7adc83373d0f3d228f393025edc2421a58272e03
    role: target
  - path: data/records/fluorine.yaml
    sha256: 4af0ed94ff108aeb0aac4eab20d104aeb4df731ead7816c7324444bed983a7c2
    role: target
  - path: data/records/forsterite.yaml
    sha256: 02e8064c327e7ffaad302ec0ab8cbe772a209b56c48353986a392d0cc6730e4c
    role: target
  - path: data/records/gaas-production-hydroxide-sludge.yaml
    sha256: b9677948646ca58ea26fd2baef613b4f64fbb559cf2dfdc6da46de44e1dbe093
    role: target
  - path: data/records/galena.yaml
    sha256: 0db7562f27bf4291add828abb5e334a832a00aef41a94fdf8b64a2ea1c80d1c7
    role: target
  - path: data/records/gallium.yaml
    sha256: ee9aa739bd3c1d87873ba882935859f09e622c6bad8fbd9d3034d91ddc40fe87
    role: target
  - path: data/records/glushinskite.yaml
    sha256: 5cb28c72ab6063b388cf1b867a066c462b49912fae71e2cb70a12dd70656c321
    role: target
  - path: data/records/goethite.yaml
    sha256: bf9bcd129e9a1cb1183625b474b057133d9b82c8e076a571a98b66c58c3e0309
    role: target
  - path: data/records/gold-mine-tailings.yaml
    sha256: 7077c6e8a219090d8432c6834fea67516786c14f50507744ef51a9ba4386a30e
    role: target
  - path: data/records/greigite.yaml
    sha256: be8b41ecfaff986ee120509637266c5e907547a6af8d2784e7c18a761a000993
    role: target
  - path: data/records/hafnium.yaml
    sha256: 268de25913b83362c0585691549ed9811257f471d50b22155cd3955204a00efb
    role: target
  - path: data/records/hausmannite.yaml
    sha256: 5a14c442064c2dd3b6abd1d796a0855b9c823e0a8de6a1ef2a76233231a8ce24
    role: target
  - path: data/records/heavy-fuel-oil-combustion-ash.yaml
    sha256: 52579409f14e3b9dd2cb8f1505ea1f08515fa2f624353f11e661a2c4f3df7c45
    role: target
  - path: data/records/hollandite.yaml
    sha256: 971768f2eef983c14ee83e068a69b164aba4c338a88ddd5bfd416b414ef719d9
    role: target
  - path: data/records/hopeite.yaml
    sha256: e17ac1f2e993dfd8781643472caba55ee3e8ca845b4c040f14609268cd53826d
    role: target
  - path: data/records/humboldtine.yaml
    sha256: 7f86f2d18e4fd78634462ce704cf6cfa75723720712089c3dbc6d0bca916df1f
    role: target
  - path: data/records/hydroxylapatite.yaml
    sha256: 103556e9bc6f205b72968ba080931fa074095bd00c137157bb4fe5323fdffb25
    role: target
  - path: data/records/illite.yaml
    sha256: 90ae810251dbddd8d43ced4ea2f3a5505d3980cd8cf5e14e693a761a054926a6
    role: target
  - path: data/records/ion-adsorption-rare-earth-leach-residue.yaml
    sha256: a7bc2ba234388913d774a62e95e4ae18bccdfe36069ed4ec0b6f779ef42bf274
    role: target
  - path: data/records/iron.yaml
    sha256: 92f6792df8c1b65d3377d91b9cf7817b42a4558cb0618e4db8f2f97382aad62d
    role: target
  - path: data/records/jadarite.yaml
    sha256: 22ee0126ca92210a18251c583d14218a1685f9521828c017e0991f10db19f9fa
    role: target
  - path: data/records/jarosite.yaml
    sha256: 9009550c542b60b877652b4ebb97a7f834a46639181d87bd53dc5eda761efa5e
    role: target
  - path: data/records/kaolin.yaml
    sha256: 8e754fc3cba67a9b31d2cae9ef8846128fbe6f39c1b3d591d3e5434fb25b29f0
    role: target
  - path: data/records/katsarosite.yaml
    sha256: 70f5c37f86e33265051032055fe64e6bf44e9a0f3ef055f4d3b605aa4f70a9c7
    role: target
  - path: data/records/kesterite.yaml
    sha256: 44706e81d0d250911a5bdb7f51516f9d5a82a9f27bb45602f77b93c1a8a01b8d
    role: target
  - path: data/records/lanthanum.yaml
    sha256: eca2a756a20c63a497823a64fb51fd877f157f4f2c8b9b7479d0a1af925ab930
    role: target
  - path: data/records/lepidocrocite.yaml
    sha256: c3bdb17c5a46fcd20451ee2e969f8b44ec1093d1bb550262d110196841a2ca32
    role: target
  - path: data/records/lindbergite.yaml
    sha256: ce6da3cd503b044e53fc894237c5c7df6c2efb941c16a99c429b92942c69aebc
    role: target
  - path: data/records/lithium-bearing-geothermal-brine.yaml
    sha256: 94d9b81f61dd307f3f3e52e33f036a0a6d6e34b07b7670b3c27360e4505e704c
    role: target
  - path: data/records/lithium-mica-ore.yaml
    sha256: 5476a13cee4f2dd135821975f2d09289e50ea5ecd7b655c81cf805bcc295436e
    role: target
  - path: data/records/lithium.yaml
    sha256: 507b7705fc18b95088e50612586b338370de697b8ed6093d3d74f546b8d90f07
    role: target
  - path: data/records/lutetium.yaml
    sha256: f9881645329d9d18e925a12ca8b858b78a3fec1b806caa37ce465acdabf162fe
    role: target
  - path: data/records/mackinawite.yaml
    sha256: bc0d8e0033344706692550a7ddb79cd4eab080536c47367742ef39e60c7a05b3
    role: target
  - path: data/records/magnesium.yaml
    sha256: ab57bc5464af299e10481a8a56f0f4161e6bc10cbac35852b82e63caf677ccc2
    role: target
  - path: data/records/magnetite.yaml
    sha256: 8a547999e0f10555f6b57013b502a5008fd5afae6d1c2458cbff7659fbe2cb20
    role: target
  - path: data/records/malachite.yaml
    sha256: ef47d79cdcfbece3b0dbe9d3b8cc6f1d5755ca8c8bdbed360764963b4d5db7eb
    role: target
  - path: data/records/manganese-ore.yaml
    sha256: 808286d076a7e344b2423ae035257231ce290eb7cd62535aa79eeade7bc288e8
    role: target
  - path: data/records/manganese.yaml
    sha256: 3d9d759613d889fdf23a6bbb16f35b1ace1f36eed87f39add5a5879992d24906
    role: target
  - path: data/records/manganite.yaml
    sha256: fe6cc2a912d277fb47548aa5834d14b482fc20a567bae9daee78d77e19cc194f
    role: target
  - path: data/records/marcasite.yaml
    sha256: 653e77b4cbb116680bb15a6fd3795af0a7632ccac365eb8a143723f936e03ab7
    role: target
  - path: data/records/metacinnabar.yaml
    sha256: 0bb941fbfa16112b5dddff9d25e414e4a5ce00ce79bf9ab80ee39f4285ca4c31
    role: target
  - path: data/records/metal-grinding-sludge.yaml
    sha256: cfa25dc269529ff524ea1f0edc360a6b6ec7637462069a9a54803c2d82311abd
    role: target
  - path: data/records/metallic-machining-burrs.yaml
    sha256: 6182f9b2753b47195cc26c94f1772934ae0d987e5c36377ac32fef0427126a46
    role: target
  - path: data/records/metalliferous-black-shale.yaml
    sha256: 1dcd46d715c4783fe411626be61cb699a74a158cbfb0bbc4ae2fbc4238f15f41
    role: target
  - path: data/records/millerite.yaml
    sha256: 8fea40dcaf36531a2dc7066100698eb946170dc9ae5974404452ec4632e80e88
    role: target
  - path: data/records/mimetite.yaml
    sha256: fd40abfe61ea182d5c94e424e60dc64422a5c551ba9492340c2d8d8f12b4384f
    role: target
  - path: data/records/molybdenite.yaml
    sha256: 0025daf0a5e920f6ca738cd007767add44bf74f3129277ddb6cf6bed880913d0
    role: target
  - path: data/records/montmorillonite.yaml
    sha256: c25638a1ed8128e31733f560aeea1a0fc1bb73e420425c65422923064efa1c6e
    role: target
  - path: data/records/moolooite.yaml
    sha256: 9006a1b5b2502efbf8b1a3ec90caad7dcfb1bf5469de7ad94791a2f52314fa3f
    role: target
  - path: data/records/municipal-sewage-sludge.yaml
    sha256: a3b578e3cd85a212912adc062c7c209cebd91c5c9d2e125537382882a3134540
    role: target
  - path: data/records/neodymium.yaml
    sha256: 91a74a542eb1dbd45aeb4cbd24f3ced3f382854dc7e7e3d2292effcded89341f
    role: target
  - path: data/records/nepheline.yaml
    sha256: 0b5844e77af50b821f69cd51a74d73a045bfb9913486e46c74604402b6107a75
    role: target
  - path: data/records/nickel-based-superalloy-residue-powders.yaml
    sha256: ba1eabc24f734db33e5a02a2a78b5f1e75490ffaf02f84835a0285b1b8b4bf32
    role: target
  - path: data/records/nickel-flotation-tailings.yaml
    sha256: 92aab61f56f1ac21279db66d814d57f67ca5cee0c1186a7ff27ca3026b922327
    role: target
  - path: data/records/nickel-laterite-ore.yaml
    sha256: a17fd9f852d59f66156b529dbdc8103929f54d275285608005fcf162c39fe42b
    role: target
  - path: data/records/nickel-smelter-slag.yaml
    sha256: e604e1bb496cbf17ea56b787a70eff7b6b269705d830d117d85312a21c54d844
    role: target
  - path: data/records/nickel.yaml
    sha256: 2a4e328318bd222655d17d447cbd3a4ab187293fcc5328b5c2fdca2b976e8bfc
    role: target
  - path: data/records/nontronite.yaml
    sha256: 221195a250ebbe6e3c849bc6f949917fefc074a62327a4d930676d6bdc9fa7a1
    role: target
  - path: data/records/olivine-group.yaml
    sha256: b4c1a036cb88e89e9a7f101f1a68c9a4ea015e2477631ce33b455efa88a7670b
    role: target
  - path: data/records/orpiment.yaml
    sha256: d03de04eb6e55a76ede38f3e73ec7f2ace61dc9fdc22487398ec21e6a2ebca10
    role: target
  - path: data/records/palladium.yaml
    sha256: 6924903baa0aceaa8361a94198b2d5b42460b34d4d643fa4ffdc6e43c50803c0
    role: target
  - path: data/records/palygorskite.yaml
    sha256: 5b7fd498c5cf61bdd6ccdf43b4a12c50a891ba6f48a291269a2fe886953473c9
    role: target
  - path: data/records/petroleum-coke.yaml
    sha256: 1aa38741a5024ffb99744440d65e01e415607cc5fb31817261758ccfe531bb0f
    role: target
  - path: data/records/pharmaceutical-blister-packaging-waste.yaml
    sha256: 2aeecf814499bb4584272696b84f3404ca7d9fc82375ef76e9043cba222967dd
    role: target
  - path: data/records/phosphate-ore-tailings.yaml
    sha256: 98420be39ecd10969b51b74e8c52ef62a5c48bdde216b21093fc9b0dceb6fcc8
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
  - path: data/records/plumbojarosite.yaml
    sha256: 1ec44291578814d2d3152639d78c8718c1a3f47afaa2a6141c73596f293f4b20
    role: target
  - path: data/records/polydymite.yaml
    sha256: 81e42a84168e9d1dcbb28e55b05ea50735ff5c727609806714e605bb963c320b
    role: target
  - path: data/records/ponded-coal-ash.yaml
    sha256: 5a8a4a9b8cc6f35c74566454625c89ef02156970b80ba96a011c0afeec4c2109
    role: target
  - path: data/records/poultry-bone-residues.yaml
    sha256: c89e05a69bc4d15c673934d48aaa96a7900a9768543a1f71cd45410a72ad7035
    role: target
  - path: data/records/praseodymium.yaml
    sha256: 2aeae056f98b9571f9c38cf6bd1fb7249db9217c5f750f3de01c93b9bc594545
    role: target
  - path: data/records/pyrite-roasting-cinder.yaml
    sha256: b06753178eb5ef5d515fb1f60503461ec28c058e658f7d0020216840ff203504
    role: target
  - path: data/records/pyrochroite.yaml
    sha256: cf7faa6d67a88e405e8937aee1f05764333c40bb8f58d8960dfb29b601c18fbd
    role: target
  - path: data/records/rare-earth-element-commodities.yaml
    sha256: e599276f18c442b7fee11ca5638eb0f251e5761e675b5827c7c45963a82b4fe5
    role: target
  - path: data/records/realgar.yaml
    sha256: cc5e82135c715ee7b57c9af44b94dbd0986ba3302c2ed27b70e1d85896191e90
    role: target
  - path: data/records/rhodium.yaml
    sha256: ad7fbf9a2c12d2b9ef411ee23e3ada5698cbb2e6a3ecead2513d881f8d460a18
    role: target
  - path: data/records/rhodochrosite.yaml
    sha256: f45318e8367ef5926dd7886befbd6d6fd43fcbb13777d636c22105cd1bde8f81
    role: target
  - path: data/records/rutile.yaml
    sha256: a8ca4375c7a6a37c6af3c9853e69b1cc09233f8601218c88dd81f3670aed580d
    role: target
  - path: data/records/scandium.yaml
    sha256: a5790221b2863ad14ecb1ef28425f2b95659f818a18b658dcd2f2a70e4e5fe16
    role: target
  - path: data/records/schwertmannite.yaml
    sha256: fa22f8f32e37827a1930e082fec58ac3c51afb8f430fd55266da41b6dccf627e
    role: target
  - path: data/records/scorodite.yaml
    sha256: 52ccbc7843cc1f6a9fe5fe4056f45a21d7aa28a8ec47b3064ae81b87d4af2150
    role: target
  - path: data/records/seafloor-massive-sulfides.yaml
    sha256: d5cb49646b77422d0e6e6ded8d4c6b43f5d06b8bbdf46c087207be2266fbab91
    role: target
  - path: data/records/selenium.yaml
    sha256: 3c88fca92fd61d7c2c88981eb4497eb71b0d4af4bfa8f2d1acd062735d59fca9
    role: target
  - path: data/records/silica-sand.yaml
    sha256: 302ae3df4735d3f55010f2902f11ce285828a6c80014ad475e06d92a0c34f46f
    role: target
  - path: data/records/silicon.yaml
    sha256: f6ac021b6e80e90cae837fcf9726aef132444f34e00cdb368c1fc6c8ef21275a
    role: target
  - path: data/records/silver.yaml
    sha256: 9e526e8db6b270c515116cb1e3f3adfa9800f1184cf5d5740575a1cf1ce4cfc0
    role: target
  - path: data/records/skutterudite.yaml
    sha256: 499412ee4dc144176f6d7fb397db26055d2286f0f9ed49a752033029c10eea45
    role: target
  - path: data/records/smithsonite.yaml
    sha256: f753da8abfec3c533f4db5e21992f4db547c883337d081c2bd0e1f83e6ea6059
    role: target
  - path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    sha256: c75e9006922469b56de8e557ba85b83af1700f6a1940ec3661b3ad14dd8db49b
    role: target
  - path: data/records/spent-automotive-three-way-catalyst.yaml
    sha256: 1afb2a4aff423eb668648f0ea877d4475f526289648e25e1c1c488bd1f26b3df
    role: target
  - path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    sha256: 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0
    role: target
  - path: data/records/spent-hydrodesulfurization-catalyst.yaml
    sha256: 86bc77dd92c351cc76173dcc22bd17645e1d02256d4d69a34b96f9872ec46f83
    role: target
  - path: data/records/spent-nickel-cadmium-batteries.yaml
    sha256: 828cbf378a76ed63922d828b7ac9c28dcee9fd9ef13453394038eb7ff45428be
    role: target
  - path: data/records/spent-nickel-metal-hydride-batteries.yaml
    sha256: 9e07ce9af31462bfb138454b7176106e2d245b0d381a82e3c097cf5df3d2a301
    role: target
  - path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
    sha256: a34fbf8bdb8a8b1e0fec3bb38916de7599e56ee98c6e1d81484227d38ef1d9ee
    role: target
  - path: data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml
    sha256: 199b1a45cdab2fc47d99767df4aec89cb7b9b150de02bc52f72bc826936b2844
    role: target
  - path: data/records/spent-steel-pickling-liquors.yaml
    sha256: 81ed3c945fb436210d910ca994308462c07846d47081599b42e902648949f200
    role: target
  - path: data/records/spent-sulfuric-acid-production-catalyst.yaml
    sha256: 54fa1806a43da00d6969c839113f5dd004086df533153de1ad3f9cb13c1917ad
    role: target
  - path: data/records/sphalerite.yaml
    sha256: 087382e75c89b45d38637c62bc6903a746886210ecada76455ba249ef8d17a2e
    role: target
  - path: data/records/spodumene.yaml
    sha256: a2704917baf98d73456830d7ad0a4d2b1bcc534f63d537491609a691fc5d4412
    role: target
  - path: data/records/stannite.yaml
    sha256: de23091025ee817a1fbb64f79031ae5539cd9dce39d36bd2e9a6ba38d88442a5
    role: target
  - path: data/records/strontianite.yaml
    sha256: 61d2884f0ae85bfe5ae98aa7225f49e17f0bcf0697e30bc95527a3d2db939967
    role: target
  - path: data/records/struvite.yaml
    sha256: bb00ccd418b9d8eb285a38104a5d0bd243596cfa41cf1d694dc17d9f8de11f78
    role: target
  - path: data/records/talc.yaml
    sha256: 6d6e241f799e6bed57a229bc464ffe6fa7602a6d9581761120a3159047629a3c
    role: target
  - path: data/records/tannery-sludge.yaml
    sha256: d8843b3142e54f8ddbded8154f44c3f4a64ca2aa43961045204477476d13e27e
    role: target
  - path: data/records/tennantite-concentrate.yaml
    sha256: 73d880437a46d3746d0d1a2af4a51d0f661505324f0b0c4ca770afc7ee1bdc50
    role: target
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 028970846c1d345fc830dcaec41ed55d2f96b7b523a90646af3c3036276018c0
    role: target
  - path: data/records/thallium.yaml
    sha256: 0183150b963b97fb4331893297061086fdd168bd0c27027f651101233153b260
    role: target
  - path: data/records/thulium.yaml
    sha256: d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62
    role: target
  - path: data/records/titanium-metal.yaml
    sha256: 659d2df56ed93892aa536336b6db7847a9917aad3d9aaa61d455d209bd0acba7
    role: target
  - path: data/records/titanium.yaml
    sha256: 189a9821197d4a2efa9bed95505c51c6b01bc211b08a6599fc2e3ffc17b8ec95
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: 73d8a1db9c82ee916f08ca2999bf85f83e188ae0e8f303f79fbc931fe2819ab9
    role: target
  - path: data/records/uraninite.yaml
    sha256: b530bf1c11b36f0bc3fe5b150cfd33d207d25b1076d352802125771cab3c7d35
    role: target
  - path: data/records/uranium.yaml
    sha256: 02fb0f5a817a13f868dd9ebd0751021f279eafce8f30d7ee618c47f91bfb468e
    role: target
  - path: data/records/used-photographic-fixer-solutions.yaml
    sha256: e9b39928908bb2c2764d26072f264b8f7a3c77f38cd759d86de7984c90f527f6
    role: target
  - path: data/records/vaesite.yaml
    sha256: 834bb7285ea0f0fc1d23ce5003af15bb89cf93fef110d0dd00133ed0e867e916
    role: target
  - path: data/records/vanadium.yaml
    sha256: 0537c316f2f345b570468c97cc79b51bc447585f80a64858f3d7dace6d227c47
    role: target
  - path: data/records/vaterite.yaml
    sha256: b6bd7aa02866b565e3bd787f9bbf4852bd3c89246673b545f173a8970c6acbe8
    role: target
  - path: data/records/waste-liquid-crystal-display-panels.yaml
    sha256: 065252079cfc86daa3c8a770ca62b02c3b5fa691c53688f83a80cfb4bf6725f5
    role: target
  - path: data/records/waste-x-ray-films.yaml
    sha256: 3242ca80051b33f22675a7473e171b25570c1596f03526b2c3b5a7a05971c454
    role: target
  - path: data/records/wheatleyite.yaml
    sha256: 711045eaf9a26e67608bfa4b436edfb07d4ec00d50a2338b12721881e4c25bfb
    role: target
  - path: data/records/whewellite.yaml
    sha256: 11d4a2a0f35c27b763ba6128e40aad957410648673afe3af244a786f2b368ace
    role: target
  - path: data/records/zinc.yaml
    sha256: 169d45a59d2ca47b8f15c03cb7141f1adb445e5b6c6a33d404d15b825dc9ec00
    role: target
  - path: data/records/zincite.yaml
    sha256: f85c711be3858731e2f25b4b6fab45299dfc958f78c1baa7b76737e3e6c7713a
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 182
  reviewed_target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:argentojarosite
  - cmmmech:arsenic
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:baricite
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:chalcopyrite
  - cmmmech:chlorite
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:chukanovite
  - cmmmech:coal-beneficiation-waste
  - cmmmech:colemanite
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:copper
  - cmmmech:discarded-led-lamps
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electroplating-sludge
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:enstatite
  - cmmmech:eudialyte-ore
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:feroxyhyte
  - cmmmech:ferrihydrite
  - cmmmech:fish-bone-residues
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:galena
  - cmmmech:gallium
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:gold-mine-tailings
  - cmmmech:greigite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:illite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lepidocrocite
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:mackinawite
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese-ore
  - cmmmech:manganese
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:metalliferous-black-shale
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:municipal-sewage-sludge
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickel-smelter-slag
  - cmmmech:nickel
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:palygorskite
  - cmmmech:petroleum-coke
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:praseodymium
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:rutile
  - cmmmech:scandium
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:selenium
  - cmmmech:silica-sand
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tannery-sludge
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:titanium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:vaesite
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  selection: data/records/*.yaml where bool(causal_graphs) is True at 794684703f77385b6e9bca32167f6c8d1e5e29bf
  description: Full-population Cycle 11 Stage 4 cross-cohort review of all 182 records
    carrying causal_graphs in CMMMech.
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
- target_id: cmmmech:ammoniojarosite
  path: data/records/ammoniojarosite.yaml
  kind: maintained
  label: Ammoniojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ammoniojarosite.yaml
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
- target_id: cmmmech:argentojarosite
  path: data/records/argentojarosite.yaml
  kind: maintained
  label: Argentojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/argentojarosite.yaml
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
- target_id: cmmmech:automotive-wastewater-treatment-sludge
  path: data/records/automotive-wastewater-treatment-sludge.yaml
  kind: maintained
  label: Automotive wastewater-treatment sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/automotive-wastewater-treatment-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:baricite
  path: data/records/baricite.yaml
  kind: maintained
  label: Barićite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baricite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:basic-oxygen-furnace-steelmaking-dust
  path: data/records/basic-oxygen-furnace-steelmaking-dust.yaml
  kind: maintained
  label: Basic oxygen furnace steelmaking dust
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/basic-oxygen-furnace-steelmaking-dust.yaml
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
- target_id: cmmmech:beverage-carton-hydropulping-reject
  path: data/records/beverage-carton-hydropulping-reject.yaml
  kind: maintained
  label: Beverage-carton hydropulping reject
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/beverage-carton-hydropulping-reject.yaml
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
- target_id: cmmmech:blast-furnace-cast-house-dust
  path: data/records/blast-furnace-cast-house-dust.yaml
  kind: maintained
  label: Blast-furnace cast-house dust
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/blast-furnace-cast-house-dust.yaml
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
- target_id: cmmmech:boron-ore-concentration-tailings
  path: data/records/boron-ore-concentration-tailings.yaml
  kind: maintained
  label: Boron-ore concentration tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boron-ore-concentration-tailings.yaml
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
- target_id: cmmmech:cemented-tungsten-carbide-scrap
  path: data/records/cemented-tungsten-carbide-scrap.yaml
  kind: maintained
  label: Cemented tungsten carbide scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cemented-tungsten-carbide-scrap.yaml
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
- target_id: cmmmech:chalcopyrite
  path: data/records/chalcopyrite.yaml
  kind: maintained
  label: Chalcopyrite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcopyrite.yaml
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
- target_id: cmmmech:chromite-beneficiation-tailings
  path: data/records/chromite-beneficiation-tailings.yaml
  kind: maintained
  label: Chromite beneficiation tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite-beneficiation-tailings.yaml
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
- target_id: cmmmech:chukanovite
  path: data/records/chukanovite.yaml
  kind: maintained
  label: Chukanovite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chukanovite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coal-beneficiation-waste
  path: data/records/coal-beneficiation-waste.yaml
  kind: maintained
  label: Coal beneficiation waste
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
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
- target_id: cmmmech:copper-smelter-flue-dust
  path: data/records/copper-smelter-flue-dust.yaml
  kind: maintained
  label: Copper-smelter flue dust
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-smelter-flue-dust.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:copper-smelter-slag
  path: data/records/copper-smelter-slag.yaml
  kind: maintained
  label: Copper smelter slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-smelter-slag.yaml
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
- target_id: cmmmech:discarded-led-lamps
  path: data/records/discarded-led-lamps.yaml
  kind: maintained
  label: Discarded light-emitting-diode lamps
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/discarded-led-lamps.yaml
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
- target_id: cmmmech:electric-arc-furnace-dust
  path: data/records/electric-arc-furnace-dust.yaml
  kind: maintained
  label: Electric-arc-furnace dust
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electric-arc-furnace-dust.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:electroformed-copper-silver-manufacturing-scrap
  path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
  kind: maintained
  label: Electroformed copper-silver manufacturing scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
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
- target_id: cmmmech:feroxyhyte
  path: data/records/feroxyhyte.yaml
  kind: maintained
  label: Feroxyhyte
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feroxyhyte.yaml
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
- target_id: cmmmech:fish-bone-residues
  path: data/records/fish-bone-residues.yaml
  kind: maintained
  label: Fish-bone residues
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fish-bone-residues.yaml
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
- target_id: cmmmech:gaas-production-hydroxide-sludge
  path: data/records/gaas-production-hydroxide-sludge.yaml
  kind: maintained
  label: GaAs wafer-production hydroxide sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gaas-production-hydroxide-sludge.yaml
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
- target_id: cmmmech:goethite
  path: data/records/goethite.yaml
  kind: maintained
  label: Goethite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/goethite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:gold-mine-tailings
  path: data/records/gold-mine-tailings.yaml
  kind: maintained
  label: Gold-mine tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/gold-mine-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:greigite
  path: data/records/greigite.yaml
  kind: maintained
  label: Greigite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
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
- target_id: cmmmech:illite
  path: data/records/illite.yaml
  kind: maintained
  label: Illite group
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/illite.yaml
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
- target_id: cmmmech:jadarite
  path: data/records/jadarite.yaml
  kind: maintained
  label: Jadarite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jadarite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:jarosite
  path: data/records/jarosite.yaml
  kind: maintained
  label: Jarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jarosite.yaml
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
- target_id: cmmmech:lepidocrocite
  path: data/records/lepidocrocite.yaml
  kind: maintained
  label: Lepidocrocite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lepidocrocite.yaml
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
- target_id: cmmmech:mackinawite
  path: data/records/mackinawite.yaml
  kind: maintained
  label: Mackinawite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mackinawite.yaml
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
- target_id: cmmmech:manganite
  path: data/records/manganite.yaml
  kind: maintained
  label: Manganite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganite.yaml
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
- target_id: cmmmech:metal-grinding-sludge
  path: data/records/metal-grinding-sludge.yaml
  kind: maintained
  label: Metal grinding sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metal-grinding-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:metallic-machining-burrs
  path: data/records/metallic-machining-burrs.yaml
  kind: maintained
  label: Metallic machining burrs
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metallic-machining-burrs.yaml
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
- target_id: cmmmech:millerite
  path: data/records/millerite.yaml
  kind: maintained
  label: Millerite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/millerite.yaml
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
- target_id: cmmmech:molybdenite
  path: data/records/molybdenite.yaml
  kind: maintained
  label: Molybdenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenite.yaml
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
- target_id: cmmmech:municipal-sewage-sludge
  path: data/records/municipal-sewage-sludge.yaml
  kind: maintained
  label: Municipal sewage sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/municipal-sewage-sludge.yaml
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
- target_id: cmmmech:nickel-based-superalloy-residue-powders
  path: data/records/nickel-based-superalloy-residue-powders.yaml
  kind: maintained
  label: Nickel-based superalloy residue powders
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-based-superalloy-residue-powders.yaml
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
- target_id: cmmmech:nickel-smelter-slag
  path: data/records/nickel-smelter-slag.yaml
  kind: maintained
  label: Nickel smelter slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-smelter-slag.yaml
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
- target_id: cmmmech:palygorskite
  path: data/records/palygorskite.yaml
  kind: maintained
  label: Palygorskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/palygorskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:petroleum-coke
  path: data/records/petroleum-coke.yaml
  kind: maintained
  label: Petroleum coke
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/petroleum-coke.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:pharmaceutical-blister-packaging-waste
  path: data/records/pharmaceutical-blister-packaging-waste.yaml
  kind: maintained
  label: Pharmaceutical blister packaging waste
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pharmaceutical-blister-packaging-waste.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:phosphate-ore-tailings
  path: data/records/phosphate-ore-tailings.yaml
  kind: maintained
  label: Phosphate-ore tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-ore-tailings.yaml
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
- target_id: cmmmech:plumbojarosite
  path: data/records/plumbojarosite.yaml
  kind: maintained
  label: Plumbojarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/plumbojarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:polydymite
  path: data/records/polydymite.yaml
  kind: maintained
  label: Polydymite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polydymite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ponded-coal-ash
  path: data/records/ponded-coal-ash.yaml
  kind: maintained
  label: Ponded mixed coal ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ponded-coal-ash.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:poultry-bone-residues
  path: data/records/poultry-bone-residues.yaml
  kind: maintained
  label: Poultry-bone residues
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/poultry-bone-residues.yaml
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
- target_id: cmmmech:pyrite-roasting-cinder
  path: data/records/pyrite-roasting-cinder.yaml
  kind: maintained
  label: Pyrite-roasting cinder
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrite-roasting-cinder.yaml
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
- target_id: cmmmech:rutile
  path: data/records/rutile.yaml
  kind: maintained
  label: Rutile
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rutile.yaml
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
- target_id: cmmmech:schwertmannite
  path: data/records/schwertmannite.yaml
  kind: maintained
  label: Schwertmannite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/schwertmannite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:scorodite
  path: data/records/scorodite.yaml
  kind: maintained
  label: Scorodite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scorodite.yaml
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
- target_id: cmmmech:skutterudite
  path: data/records/skutterudite.yaml
  kind: maintained
  label: Skutterudite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/skutterudite.yaml
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
- target_id: cmmmech:spent-alkaline-zinc-carbon-batteries
  path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
  kind: maintained
  label: Spent alkaline and zinc-carbon batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-automotive-three-way-catalyst
  path: data/records/spent-automotive-three-way-catalyst.yaml
  kind: maintained
  label: Spent automotive three-way catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-automotive-three-way-catalyst.yaml
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
- target_id: cmmmech:spent-hydrodesulfurization-catalyst
  path: data/records/spent-hydrodesulfurization-catalyst.yaml
  kind: maintained
  label: Spent hydrodesulfurization catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-hydrodesulfurization-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-nickel-cadmium-batteries
  path: data/records/spent-nickel-cadmium-batteries.yaml
  kind: maintained
  label: Spent nickel-cadmium batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-nickel-cadmium-batteries.yaml
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
- target_id: cmmmech:spent-selective-catalytic-reduction-catalyst
  path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
  kind: maintained
  label: Spent selective catalytic reduction catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
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
- target_id: cmmmech:spent-steel-pickling-liquors
  path: data/records/spent-steel-pickling-liquors.yaml
  kind: maintained
  label: Spent steel-pickling liquors
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-steel-pickling-liquors.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-sulfuric-acid-production-catalyst
  path: data/records/spent-sulfuric-acid-production-catalyst.yaml
  kind: maintained
  label: Spent sulfuric-acid-production catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-sulfuric-acid-production-catalyst.yaml
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
- target_id: cmmmech:spodumene
  path: data/records/spodumene.yaml
  kind: maintained
  label: Spodumene
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spodumene.yaml
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
- target_id: cmmmech:tannery-sludge
  path: data/records/tannery-sludge.yaml
  kind: maintained
  label: Tannery sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tannery-sludge.yaml
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
- target_id: cmmmech:used-photographic-fixer-solutions
  path: data/records/used-photographic-fixer-solutions.yaml
  kind: maintained
  label: Used photographic fixer solutions
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/used-photographic-fixer-solutions.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:vaesite
  path: data/records/vaesite.yaml
  kind: maintained
  label: Vaesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/vaesite.yaml
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
- check_id: just-validate-causal-graphs
  name: just validate (causal_graphs cohort)
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
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:argentojarosite
  - cmmmech:arsenic
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:baricite
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:chalcopyrite
  - cmmmech:chlorite
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:chukanovite
  - cmmmech:coal-beneficiation-waste
  - cmmmech:colemanite
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:copper
  - cmmmech:discarded-led-lamps
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electroplating-sludge
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:enstatite
  - cmmmech:eudialyte-ore
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:feroxyhyte
  - cmmmech:ferrihydrite
  - cmmmech:fish-bone-residues
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:galena
  - cmmmech:gallium
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:gold-mine-tailings
  - cmmmech:greigite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:illite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lepidocrocite
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:mackinawite
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese-ore
  - cmmmech:manganese
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:metalliferous-black-shale
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:municipal-sewage-sludge
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickel-smelter-slag
  - cmmmech:nickel
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:palygorskite
  - cmmmech:petroleum-coke
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:praseodymium
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:rutile
  - cmmmech:scandium
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:selenium
  - cmmmech:silica-sand
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tannery-sludge
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:titanium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:vaesite
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  summary: All 182 causal_graphs cohort records pass LinkML structural, semantic,
    and canonical top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-causal-graphs
  name: just verify-history (causal_graphs cohort)
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
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:argentojarosite
  - cmmmech:arsenic
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:baricite
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:chalcopyrite
  - cmmmech:chlorite
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:chukanovite
  - cmmmech:coal-beneficiation-waste
  - cmmmech:colemanite
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:copper
  - cmmmech:discarded-led-lamps
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electroplating-sludge
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:enstatite
  - cmmmech:eudialyte-ore
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:feroxyhyte
  - cmmmech:ferrihydrite
  - cmmmech:fish-bone-residues
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:galena
  - cmmmech:gallium
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:gold-mine-tailings
  - cmmmech:greigite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:illite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lepidocrocite
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:mackinawite
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese-ore
  - cmmmech:manganese
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:metalliferous-black-shale
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:municipal-sewage-sludge
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickel-smelter-slag
  - cmmmech:nickel
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:palygorskite
  - cmmmech:petroleum-coke
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:praseodymium
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:rutile
  - cmmmech:scandium
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:selenium
  - cmmmech:silica-sand
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tannery-sludge
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:titanium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:vaesite
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  summary: All 182 causal_graphs cohort records have intact append-only history sidecars
    and matching curation_history metadata.
assessments:
- assessment_id: assess-causal-graphs-and-uniprot-grounding
  topic: Causal-graph DAG topology, mechanism-node protein_examples synchronization,
    and source-backed edge prose
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:argentojarosite
  - cmmmech:arsenic
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:baricite
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:chalcopyrite
  - cmmmech:chlorite
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:chukanovite
  - cmmmech:coal-beneficiation-waste
  - cmmmech:colemanite
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:copper
  - cmmmech:discarded-led-lamps
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electroplating-sludge
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:enstatite
  - cmmmech:eudialyte-ore
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:feroxyhyte
  - cmmmech:ferrihydrite
  - cmmmech:fish-bone-residues
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:galena
  - cmmmech:gallium
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:gold-mine-tailings
  - cmmmech:greigite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:illite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lepidocrocite
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:mackinawite
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese-ore
  - cmmmech:manganese
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:metalliferous-black-shale
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:municipal-sewage-sludge
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickel-smelter-slag
  - cmmmech:nickel
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:palygorskite
  - cmmmech:petroleum-coke
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:praseodymium
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:rutile
  - cmmmech:scandium
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:selenium
  - cmmmech:silica-sand
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tannery-sludge
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:titanium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:vaesite
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  - ev-gluconobacter-silicate-graphs
  - ev-vazquez-rodriguez2015-metacinnabar-graph
  - ev-dong2024-scandium-graph
  summary: All 182 causal_graphs records pass DAG, reference-closure, and UniProtKB
    protein_examples synchronization checks (640 mechanism-level and 640 node-level
    protein_examples across 139 unique accessions). Identified 3 minor graph findings
    across 5 records (enstatite, olivine-group, dunite, metacinnabar, scandium).
findings:
- finding_id: cmmmech-cycle11-stage4-finding-0001
  issue_key: cmmmech.gluconobacter-enstatite-olivine-dunite.template-node-edge-explanations-and-pqqc-gdh-support
  title: Gluconobacter oxydans silicate bioleaching causal graphs in enstatite.yaml,
    olivine-group.yaml, and dunite.yaml retain generic template node/edge explanations
    and unqualified pqqC/gdh support in dunite.yaml
  severity: minor
  category: graph
  certainty: confirmed
  status: open
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
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  - ev-gluconobacter-silicate-graphs
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
- finding_id: cmmmech-cycle11-stage4-finding-0002
  issue_key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support
  title: Thiobacillus thioparus metacinnabar record and causal graph misstate primary
    natural museum metacinnabar feed as synthetic beta-HgS in SoxB protein evidence
    and assert unqualified soluble-Hg(II) accumulation edge support
  severity: minor
  category: graph
  certainty: confirmed
  status: open
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
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  - ev-vazquez-rodriguez2015-metacinnabar-graph
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
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
- finding_id: cmmmech-cycle11-stage4-finding-0003
  issue_key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording
  title: Mex-LanM scandium chromatography record and causal graph misdescribe pH 5.0
    malonate elution from a synthetic 16-REE chloride feed as mild acid stripping
    of transition/base metals from a multi-metal leachate
  severity: minor
  category: graph
  certainty: confirmed
  status: open
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
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].explanation
  evidence_ids:
  - ev-causal-graphs-cohort-audit
  - ev-dong2024-scandium-graph
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
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
actions:
- action_id: act-refine-gluconobacter-enstatite-olivine-dunite-graphs
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0001
  target_ids:
  - cmmmech:enstatite
  - cmmmech:olivine-group
  - cmmmech:dunite
  description: Replace the generic parenthetical template description on enstatite.yaml
    nodes[4].description (enstatite_mixed_feed), replace generic template explanations
    on edges[0..2].evidence[0].explanation in data/records/enstatite.yaml and data/records/olivine-group.yaml
    and edges[1..2].evidence[0].explanation in data/records/dunite.yaml with study-specific
    prose citing Klug et al. (2026) and Lee et al. (2025), and qualify dunite.yaml
    mechanisms[0].protein_examples[2..3].evidence[0].supports, causal_graphs[0].nodes[1..2].protein_examples[0].evidence[0].supports,
    and causal_graphs[0].edges[1..2].evidence[0].supports to partial during Stage
    5 grouped remediation with canonical history provenance.
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
  acceptance_checks:
  - enstatite.yaml causal_graphs[0].nodes[4].description specifies the ~40 um milled,
    ultrasonically washed 69 wt% olivine / 31 wt% enstatite mixed silicate feed (5%
    w/v) without template label duplication.
  - edges[0..2].evidence[0].explanation in enstatite.yaml and olivine-group.yaml and
    edges[1..2].evidence[0].explanation in dunite.yaml replace generic template strings
    with study-specific klug_2026 and lee2025 prose.
  - 'dunite.yaml mechanisms[0].protein_examples[2..3], causal_graphs[0].nodes[1..2].protein_examples[0],
    and causal_graphs[0].edges[1..2] use supports: partial with Synchronized study-specific
    explanations.'
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
- action_id: act-refine-vazquez-rodriguez2015-metacinnabar-graph-and-soxb-evidence
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0002
  target_ids:
  - cmmmech:metacinnabar
  description: Update mechanisms[0].protein_examples[0].evidence[0].explanation, causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation,
    and causal_graphs[0].nodes[1].description in data/records/metacinnabar.yaml to
    distinguish the primary 2 g/L ground natural museum metacinnabar (<250 um, containing
    pyritic inclusions, Figures 3-5, Table 1) from the synthetic black HgS daily-thiosulfate-spike
    comparison (Figures 6-7), qualify causal_graphs[0].edges[1].evidence[0].supports
    to partial with accurate aqueous-Hg vs volatile-Hg(0) partitioning prose, and
    replace generic one-line explanations on edges[0..3] during Stage 5 grouped remediation
    with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  acceptance_checks:
  - mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    in metacinnabar.yaml remain byte-identical and accurately distinguish natural
    museum metacinnabar (<250 um) from synthetic black HgS.
  - 'causal_graphs[0].nodes[1].description and edges[0..3] in metacinnabar.yaml use
    vazquez_rodriguez2015-specific prose with supports: partial on edges[1].'
  - Matching EDIT history sidecar exists in history/records/metacinnabar/ and passes
    just check.
- action_id: act-refine-dong2024-scandium-mex-lanm-graph-and-protein-evidence
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0003
  target_ids:
  - cmmmech:scandium
  description: 'Update mechanisms[0].protein_examples[0].evidence[0] and causal_graphs[0].nodes[0].protein_examples[0].evidence[0]
    in data/records/scandium.yaml to supports: partial with synchronized prose describing
    selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride mixture and
    stepwise 30 mM / 50 mM malonate elution at pH 5.0 (above 99 mol% purity among
    REEs and above 99% two-step yield; ~94.5% Sc yield at 30 mM malonate, Figures
    3C and 5E-F, Table S9/S10), and update causal_graphs[0].description, nodes[1..2],
    and edges[0..1] (with supports: partial on edges[0]) during Stage 5 grouped remediation
    with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  acceptance_checks:
  - 'mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    in scandium.yaml are synchronized with supports: partial and specify stepwise
    pH 5.0 malonate elution (30 mM and 50 mM) from a synthetic 16-REE chloride feed
    rather than mild acid stripping.'
  - causal_graphs[0].description, nodes[1..2], and edges[0..1] in scandium.yaml accurately
    describe the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM
    sum in Table S9/S10) and qualify edges[0].evidence[0].supports to partial.
  - Matching EDIT history sidecar exists in history/records/scandium/ and passes just
    check.
evidence:
- evidence_id: ev-causal-graphs-cohort-audit
  kind: validation
  reference: data/records/*.yaml (bool(causal_graphs) == True)
  locator: 182 causal_graphs YAML files
  accessed_at: '2026-11-09T04:15:06Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 182 causal_graphs records
    at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
- evidence_id: ev-gluconobacter-silicate-graphs
  kind: record_content
  reference: data/records/{enstatite,olivine-group,dunite}.yaml
  locator: enstatite.yaml lines 143-321; olivine-group.yaml lines 143-321; dunite.yaml
    lines 83-133, 159-337
  accessed_at: '2026-11-09T04:15:06Z'
  support: supports
  summary: 'In enstatite.yaml, olivine-group.yaml, and dunite.yaml, Gluconobacter
    oxydans causal graphs retain generic template node/edge explanations, and dunite.yaml
    asserts unqualified supports: support on pqqC and gdh protein_examples and edges[1..2].'
- evidence_id: ev-vazquez-rodriguez2015-metacinnabar-graph
  kind: record_content
  reference: data/records/metacinnabar.yaml
  locator: mechanisms[0] (lines 43-120); causal_graphs[0] (lines 157-291)
  accessed_at: '2026-11-09T04:15:06Z'
  support: supports
  summary: 'In data/records/metacinnabar.yaml, SoxB protein_examples[0] states ''synthetic
    metacinnabar (beta-HgS)'' whereas Vazquez-Rodriguez et al. (2015) primarily leached
    natural museum metacinnabar (<250 um), and edges[1] asserts supports: support
    for soluble Hg(II) accumulation.'
- evidence_id: ev-dong2024-scandium-graph
  kind: record_content
  reference: data/records/scandium.yaml
  locator: mechanisms[0] (lines 36-74); causal_graphs[0] (lines 78-140)
  accessed_at: '2026-11-09T04:15:06Z'
  support: supports
  summary: 'In data/records/scandium.yaml, Mex-LanM protein_examples[0] asserts supports:
    support with ''mild acid stripping'' over ''transition/base metals'' instead of
    stepwise pH 5.0 malonate elution from a synthetic 16-REE chloride feed, and causal_graphs[0]
    describes the feed as a ''mixed leachate feed''.'
limitations:
- 6 of 182 causal_graphs records (cmmmech:erbium, cmmmech:ferrihydrite, cmmmech:gold,
  cmmmech:lindbergite, cmmmech:magnetite, cmmmech:terbium) contain 1 explicitly UNGROUNDED
  GENE_OR_PROTEIN node each because the cited primary literature did not sequence
  the strain or resolve a specific protein accession.
- 5 records (enstatite, olivine-group, dunite, metacinnabar, scandium) carry minor
  causal-graph and protein_examples prose/support findings tracked as open findings
  cmmmech-cycle11-stage4-finding-0001..0003 for Stage 5 grouped remediation.
notes:
- Cohort covers 100% (182/182) of records with causal_graphs in data/records/*.yaml
  at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:akaganeite
  - cmmmech:allanite-concentrate
  - cmmmech:allanite-leachate
  - cmmmech:aluminium
  - cmmmech:ammoniojarosite
  - cmmmech:anatase
  - cmmmech:anglesite
  - cmmmech:argentojarosite
  - cmmmech:arsenic
  - cmmmech:arsenopyrite
  - cmmmech:asbolane
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:baricite
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:birnessite
  - cmmmech:bixbyite-mn
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:borates
  - cmmmech:bornite
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:brushite
  - cmmmech:calcite
  - cmmmech:cassiterite-polymetallic-sulfide-ore
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:cerium
  - cmmmech:cerussite
  - cmmmech:chalcopyrite-enargite-concentrate
  - cmmmech:chalcopyrite
  - cmmmech:chlorite
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium
  - cmmmech:chukanovite
  - cmmmech:coal-beneficiation-waste
  - cmmmech:colemanite
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:copper
  - cmmmech:discarded-led-lamps
  - cmmmech:dittmarite
  - cmmmech:djurleite
  - cmmmech:dunite
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electroplating-sludge
  - cmmmech:enargite-pyrite-concentrate
  - cmmmech:enstatite
  - cmmmech:eudialyte-ore
  - cmmmech:falottaite
  - cmmmech:feitknechtite
  - cmmmech:feroxyhyte
  - cmmmech:ferrihydrite
  - cmmmech:fish-bone-residues
  - cmmmech:fluorapatite
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:fluorine
  - cmmmech:forsterite
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:galena
  - cmmmech:gallium
  - cmmmech:glushinskite
  - cmmmech:goethite
  - cmmmech:gold-mine-tailings
  - cmmmech:greigite
  - cmmmech:hafnium
  - cmmmech:hausmannite
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:hollandite
  - cmmmech:hopeite
  - cmmmech:humboldtine
  - cmmmech:hydroxylapatite
  - cmmmech:illite
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron
  - cmmmech:jadarite
  - cmmmech:jarosite
  - cmmmech:kaolin
  - cmmmech:katsarosite
  - cmmmech:kesterite
  - cmmmech:lanthanum
  - cmmmech:lepidocrocite
  - cmmmech:lindbergite
  - cmmmech:lithium-bearing-geothermal-brine
  - cmmmech:lithium-mica-ore
  - cmmmech:lithium
  - cmmmech:lutetium
  - cmmmech:mackinawite
  - cmmmech:magnesium
  - cmmmech:magnetite
  - cmmmech:malachite
  - cmmmech:manganese-ore
  - cmmmech:manganese
  - cmmmech:manganite
  - cmmmech:marcasite
  - cmmmech:metacinnabar
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:metalliferous-black-shale
  - cmmmech:millerite
  - cmmmech:mimetite
  - cmmmech:molybdenite
  - cmmmech:montmorillonite
  - cmmmech:moolooite
  - cmmmech:municipal-sewage-sludge
  - cmmmech:neodymium
  - cmmmech:nepheline
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-laterite-ore
  - cmmmech:nickel-smelter-slag
  - cmmmech:nickel
  - cmmmech:nontronite
  - cmmmech:olivine-group
  - cmmmech:orpiment
  - cmmmech:palladium
  - cmmmech:palygorskite
  - cmmmech:petroleum-coke
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphate-rock
  - cmmmech:phosphogypsum
  - cmmmech:phosphorus
  - cmmmech:plumbojarosite
  - cmmmech:polydymite
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:praseodymium
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:pyrochroite
  - cmmmech:rare-earth-element-commodities
  - cmmmech:realgar
  - cmmmech:rhodium
  - cmmmech:rhodochrosite
  - cmmmech:rutile
  - cmmmech:scandium
  - cmmmech:schwertmannite
  - cmmmech:scorodite
  - cmmmech:seafloor-massive-sulfides
  - cmmmech:selenium
  - cmmmech:silica-sand
  - cmmmech:silicon
  - cmmmech:silver
  - cmmmech:skutterudite
  - cmmmech:smithsonite
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:sphalerite
  - cmmmech:spodumene
  - cmmmech:stannite
  - cmmmech:strontianite
  - cmmmech:struvite
  - cmmmech:talc
  - cmmmech:tannery-sludge
  - cmmmech:tennantite-concentrate
  - cmmmech:tetrahedrite-concentrate
  - cmmmech:thallium
  - cmmmech:thulium
  - cmmmech:titanium-metal
  - cmmmech:titanium
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:uraninite
  - cmmmech:uranium
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:vaesite
  - cmmmech:vanadium
  - cmmmech:vaterite
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-x-ray-films
  - cmmmech:wheatleyite
  - cmmmech:whewellite
  - cmmmech:zinc
  - cmmmech:zincite
  rationale: All 182 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where bool(causal_graphs) is True at 794684703f77385b6e9bca32167f6c8d1e5e29bf
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-causal-graphs-cohort-audit
```
