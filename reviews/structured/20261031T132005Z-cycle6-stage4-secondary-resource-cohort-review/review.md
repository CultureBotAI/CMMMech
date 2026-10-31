# Cycle 6 Stage 4 full-cohort review: secondary_resource records (111/111)

- Review: 20261031T132005Z-cycle6-stage4-secondary-resource-cohort-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T13:10:00Z
- Finished UTC: 2026-10-31T13:20:05Z
- Reviewer: antigravity / cmmmech-cycle6-stage4-cohort-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed all 111 secondary_resource records in data/records/*.yaml at commit fab0682688678750d7da4e5357dda11592d5fac3, including the 8 Cycle 6 Stage 2 (PR #888, commit a9115e6c) secondary_resource causal-graph and UniProtKB grounding additions (cmmmech:beverage-carton-hydropulping-reject, cmmmech:chromite-beneficiation-tailings, cmmmech:fish-bone-residues, cmmmech:municipal-sewage-sludge, cmmmech:petroleum-coke, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:poultry-bone-residues, cmmmech:tannery-sludge), the Cycle 6 Stage 3 (PR #893, commit fab06826) UniProtKB grounding addition on cmmmech:allanite-leachate, and the Cycle 5 Stage 5 (PR #880, commit b9ef4149) remediation of cmmmech:waste-liquid-crystal-display-panels. 108/111 secondary_resource records contain primary-source-backed mechanisms (107/111 with microbial: true mechanisms and 1/111, cmmmech:ferrochrome-slag, with an abiotic microbial: false mechanism hydrochloric_acid_magnesium_extraction; 145 mechanisms total), and 37/111 contain multi-step causal_graphs (40 graphs) and live-verified UniProtKB protein_examples across 25 unique accessions. Identified 2 minor graph node label/description findings (cmmmech-cycle6-stage4-finding-0001 on cmmmech:traction-battery-hydrometallurgical-residue and cmmmech-cycle6-stage4-finding-0002 across 14 single-species A. thiooxidans secondary_resource records) for Stage 5 grouped remediation.

## Scope And Provenance

Full-population Cycle 6 Stage 4 category review of all 111 secondary_resource records in CMMMech.

Selection: data/records/*.yaml where material_kind == 'secondary_resource' at fab0682688678750d7da4e5357dda11592d5fac3
Coverage: full; 111 reviewed / 111 in the declared population.
Source: git_commit at Git base fab0682688678750d7da4e5357dda11592d5fac3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:acid-mine-drainage | data/records/acid-mine-drainage.yaml | maintained | Acid mine drainage |
| cmmmech:allanite-leachate | data/records/allanite-leachate.yaml | maintained | Allanite-derived rare-earth leachate |
| cmmmech:aluminium-salt-slag | data/records/aluminium-salt-slag.yaml | maintained | Aluminium salt slag |
| cmmmech:automotive-wastewater-treatment-sludge | data/records/automotive-wastewater-treatment-sludge.yaml | maintained | Automotive wastewater-treatment sludge |
| cmmmech:basic-oxygen-furnace-steel-slag | data/records/basic-oxygen-furnace-steel-slag.yaml | maintained | Basic-oxygen-furnace steel slag |
| cmmmech:basic-oxygen-furnace-steelmaking-dust | data/records/basic-oxygen-furnace-steelmaking-dust.yaml | maintained | Basic oxygen furnace steelmaking dust |
| cmmmech:battery-black-mass | data/records/battery-black-mass.yaml | maintained | Spent lithium-ion battery black mass |
| cmmmech:bauxite-residue | data/records/bauxite-residue.yaml | maintained | Bauxite residue (red mud) |
| cmmmech:beverage-carton-hydropulping-reject | data/records/beverage-carton-hydropulping-reject.yaml | maintained | Beverage-carton hydropulping reject |
| cmmmech:biogas-desulfurization-sulfur-residue | data/records/biogas-desulfurization-sulfur-residue.yaml | maintained | Biogas-desulfurization sulfur residue |
| cmmmech:blast-furnace-cast-house-dust | data/records/blast-furnace-cast-house-dust.yaml | maintained | Blast-furnace cast-house dust |
| cmmmech:boron-ore-concentration-tailings | data/records/boron-ore-concentration-tailings.yaml | maintained | Boron-ore concentration tailings |
| cmmmech:cadmium-telluride-photovoltaic-module-scrap | data/records/cadmium-telluride-photovoltaic-module-scrap.yaml | maintained | Cadmium telluride photovoltaic module scrap |
| cmmmech:cathode-ray-tube-glass | data/records/cathode-ray-tube-glass.yaml | maintained | Waste lead-bearing cathode-ray-tube glass |
| cmmmech:cemented-tungsten-carbide-scrap | data/records/cemented-tungsten-carbide-scrap.yaml | maintained | Cemented tungsten carbide scrap |
| cmmmech:chromite-beneficiation-tailings | data/records/chromite-beneficiation-tailings.yaml | maintained | Chromite beneficiation tailings |
| cmmmech:chromite-ore-processing-residue | data/records/chromite-ore-processing-residue.yaml | maintained | Chromite ore processing residue |
| cmmmech:chromium-tanned-leather-shavings | data/records/chromium-tanned-leather-shavings.yaml | maintained | Chromium-tanned leather shavings |
| cmmmech:chrysotile-asbestos-tailings | data/records/chrysotile-asbestos-tailings.yaml | maintained | Chrysotile asbestos tailings |
| cmmmech:coal-beneficiation-waste | data/records/coal-beneficiation-waste.yaml | maintained | Coal beneficiation waste |
| cmmmech:coal-fly-ash | data/records/coal-fly-ash.yaml | maintained | Coal fly ash |
| cmmmech:coal-gasification-slag | data/records/coal-gasification-slag.yaml | maintained | Coal gasification slag |
| cmmmech:coal-mine-drainage-treatment-solids | data/records/coal-mine-drainage-treatment-solids.yaml | maintained | Coal-mine-drainage treatment solids |
| cmmmech:copper-anode-slime | data/records/copper-anode-slime.yaml | maintained | Copper anode slime |
| cmmmech:copper-autoclave-slime | data/records/copper-autoclave-slime.yaml | maintained | Copper autoclave slime |
| cmmmech:copper-flotation-tailings | data/records/copper-flotation-tailings.yaml | maintained | Copper flotation tailings |
| cmmmech:copper-smelter-flue-dust | data/records/copper-smelter-flue-dust.yaml | maintained | Copper-smelter flue dust |
| cmmmech:copper-smelter-slag | data/records/copper-smelter-slag.yaml | maintained | Copper smelter slag |
| cmmmech:discarded-led-lamps | data/records/discarded-led-lamps.yaml | maintained | Discarded light-emitting-diode lamps |
| cmmmech:electric-arc-furnace-dust | data/records/electric-arc-furnace-dust.yaml | maintained | Electric-arc-furnace dust |
| cmmmech:electrical-cable-recycling-residues | data/records/electrical-cable-recycling-residues.yaml | maintained | Electrical-cable recycling residues |
| cmmmech:electroformed-copper-silver-manufacturing-scrap | data/records/electroformed-copper-silver-manufacturing-scrap.yaml | maintained | Electroformed copper-silver manufacturing scrap |
| cmmmech:electrolytic-manganese-residue | data/records/electrolytic-manganese-residue.yaml | maintained | Electrolytic manganese residue |
| cmmmech:electroplating-bath-effluents | data/records/electroplating-bath-effluents.yaml | maintained | Electroplating-bath effluents |
| cmmmech:electroplating-sludge | data/records/electroplating-sludge.yaml | maintained | Electroplating sludge |
| cmmmech:end-of-life-cigs-photovoltaic-modules | data/records/end-of-life-cigs-photovoltaic-modules.yaml | maintained | End-of-life CIGS photovoltaic modules |
| cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules | data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml | maintained | End-of-life crystalline-silicon photovoltaic modules |
| cmmmech:ferrochrome-slag | data/records/ferrochrome-slag.yaml | maintained | Ferrochrome slag |
| cmmmech:fish-bone-residues | data/records/fish-bone-residues.yaml | maintained | Fish-bone residues |
| cmmmech:flue-gas-desulfurization-wastewater | data/records/flue-gas-desulfurization-wastewater.yaml | maintained | Flue-gas-desulfurization wastewater |
| cmmmech:fluorescent-lamp-phosphor | data/records/fluorescent-lamp-phosphor.yaml | maintained | Spent fluorescent-lamp phosphor powder |
| cmmmech:gaas-production-hydroxide-sludge | data/records/gaas-production-hydroxide-sludge.yaml | maintained | GaAs wafer-production hydroxide sludge |
| cmmmech:gold-mine-tailings | data/records/gold-mine-tailings.yaml | maintained | Gold-mine tailings |
| cmmmech:ground-waste-tire-rubber | data/records/ground-waste-tire-rubber.yaml | maintained | Ground waste tire rubber |
| cmmmech:heavy-fuel-oil-combustion-ash | data/records/heavy-fuel-oil-combustion-ash.yaml | maintained | Heavy-fuel-oil combustion ash |
| cmmmech:ion-adsorption-rare-earth-leach-residue | data/records/ion-adsorption-rare-earth-leach-residue.yaml | maintained | Ion-adsorption rare-earth leach residue |
| cmmmech:iron-ore-tailings | data/records/iron-ore-tailings.yaml | maintained | Iron-ore tailings |
| cmmmech:kaolin-mine-waste | data/records/kaolin-mine-waste.yaml | maintained | Kaolin mine waste |
| cmmmech:lead-blast-furnace-slag | data/records/lead-blast-furnace-slag.yaml | maintained | Lead blast-furnace slag |
| cmmmech:metal-grinding-sludge | data/records/metal-grinding-sludge.yaml | maintained | Metal grinding sludge |
| cmmmech:metallic-machining-burrs | data/records/metallic-machining-burrs.yaml | maintained | Metallic machining burrs |
| cmmmech:municipal-sewage-sludge | data/records/municipal-sewage-sludge.yaml | maintained | Municipal sewage sludge |
| cmmmech:municipal-waste-incineration-ash | data/records/municipal-waste-incineration-ash.yaml | maintained | Municipal-waste incineration ash |
| cmmmech:nickel-based-superalloy-residue-powders | data/records/nickel-based-superalloy-residue-powders.yaml | maintained | Nickel-based superalloy residue powders |
| cmmmech:nickel-flotation-tailings | data/records/nickel-flotation-tailings.yaml | maintained | Nickel flotation tailings |
| cmmmech:nickel-smelter-slag | data/records/nickel-smelter-slag.yaml | maintained | Nickel smelter slag |
| cmmmech:oil-and-gas-produced-water | data/records/oil-and-gas-produced-water.yaml | maintained | Oil and gas produced water |
| cmmmech:oil-sands-froth-treatment-tailings | data/records/oil-sands-froth-treatment-tailings.yaml | maintained | Oil-sands froth-treatment tailings |
| cmmmech:petroleum-coke | data/records/petroleum-coke.yaml | maintained | Petroleum coke |
| cmmmech:petroleum-oily-sludge | data/records/petroleum-oily-sludge.yaml | maintained | Petroleum oily sludge |
| cmmmech:pharmaceutical-blister-packaging-waste | data/records/pharmaceutical-blister-packaging-waste.yaml | maintained | Pharmaceutical blister packaging waste |
| cmmmech:phosphate-ore-tailings | data/records/phosphate-ore-tailings.yaml | maintained | Phosphate-ore tailings |
| cmmmech:phosphogypsum | data/records/phosphogypsum.yaml | maintained | Phosphogypsum |
| cmmmech:pig-manure | data/records/pig-manure.yaml | maintained | Pig manure |
| cmmmech:ponded-coal-ash | data/records/ponded-coal-ash.yaml | maintained | Ponded mixed coal ash |
| cmmmech:poultry-bone-residues | data/records/poultry-bone-residues.yaml | maintained | Poultry-bone residues |
| cmmmech:pyrite-roasting-cinder | data/records/pyrite-roasting-cinder.yaml | maintained | Pyrite-roasting cinder |
| cmmmech:reverse-osmosis-concentrate | data/records/reverse-osmosis-concentrate.yaml | maintained | Reverse osmosis concentrate |
| cmmmech:samarium-cobalt-magnet-scrap | data/records/samarium-cobalt-magnet-scrap.yaml | maintained | Samarium-cobalt magnet scrap |
| cmmmech:secondary-aluminium-dross | data/records/secondary-aluminium-dross.yaml | maintained | Secondary aluminium dross |
| cmmmech:sewage-sludge-incineration-ash | data/records/sewage-sludge-incineration-ash.yaml | maintained | Sewage-sludge incineration ash |
| cmmmech:spent-alkaline-zinc-carbon-batteries | data/records/spent-alkaline-zinc-carbon-batteries.yaml | maintained | Spent alkaline and zinc-carbon batteries |
| cmmmech:spent-automotive-three-way-catalyst | data/records/spent-automotive-three-way-catalyst.yaml | maintained | Spent automotive three-way catalyst |
| cmmmech:spent-cerium-glass-polishing-slurry | data/records/spent-cerium-glass-polishing-slurry.yaml | maintained | Spent cerium-based glass-polishing slurry |
| cmmmech:spent-copper-zinc-alumina-catalyst | data/records/spent-copper-zinc-alumina-catalyst.yaml | maintained | Spent copper-zinc-alumina catalyst |
| cmmmech:spent-fluid-catalytic-cracking-catalyst | data/records/spent-fluid-catalytic-cracking-catalyst.yaml | maintained | Spent fluid catalytic cracking catalyst |
| cmmmech:spent-hydrocracking-catalyst | data/records/spent-hydrocracking-catalyst.yaml | maintained | Spent hydrocracking catalyst |
| cmmmech:spent-hydrodesulfurization-catalyst | data/records/spent-hydrodesulfurization-catalyst.yaml | maintained | Spent hydrodesulfurization catalyst |
| cmmmech:spent-iron-molybdate-oxidation-catalyst | data/records/spent-iron-molybdate-oxidation-catalyst.yaml | maintained | Spent iron-molybdate oxidation catalyst |
| cmmmech:spent-ito-targets | data/records/spent-ito-targets.yaml | maintained | Spent indium-tin oxide targets |
| cmmmech:spent-lead-acid-battery-electrolyte | data/records/spent-lead-acid-battery-electrolyte.yaml | maintained | Spent lead-acid battery electrolyte |
| cmmmech:spent-ndfeb-magnets | data/records/spent-ndfeb-magnets.yaml | maintained | Spent NdFeB permanent magnets |
| cmmmech:spent-nickel-cadmium-batteries | data/records/spent-nickel-cadmium-batteries.yaml | maintained | Spent nickel-cadmium batteries |
| cmmmech:spent-nickel-metal-hydride-batteries | data/records/spent-nickel-metal-hydride-batteries.yaml | maintained | Spent nickel-metal-hydride batteries |
| cmmmech:spent-nickel-steam-reforming-catalyst | data/records/spent-nickel-steam-reforming-catalyst.yaml | maintained | Spent nickel steam-reforming catalyst |
| cmmmech:spent-platinum-petroleum-reforming-catalyst | data/records/spent-platinum-petroleum-reforming-catalyst.yaml | maintained | Spent platinum petroleum-reforming catalyst |
| cmmmech:spent-potlining | data/records/spent-potlining.yaml | maintained | Spent potlining |
| cmmmech:spent-selective-catalytic-reduction-catalyst | data/records/spent-selective-catalytic-reduction-catalyst.yaml | maintained | Spent selective catalytic reduction catalyst |
| cmmmech:spent-silver-oxide-zinc-button-cell-batteries | data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml | maintained | Spent silver-oxide–zinc button-cell batteries |
| cmmmech:spent-steel-pickling-liquors | data/records/spent-steel-pickling-liquors.yaml | maintained | Spent steel-pickling liquors |
| cmmmech:spent-sulfuric-acid-production-catalyst | data/records/spent-sulfuric-acid-production-catalyst.yaml | maintained | Spent sulfuric-acid-production catalyst |
| cmmmech:spent-tantalum-capacitors | data/records/spent-tantalum-capacitors.yaml | maintained | Spent tantalum capacitors |
| cmmmech:spent-vanadium-flow-battery-electrolyte | data/records/spent-vanadium-flow-battery-electrolyte.yaml | maintained | Spent vanadium-flow-battery electrolyte |
| cmmmech:spent-vegetable-oil-hydrogenation-catalyst | data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml | maintained | Spent vegetable-oil hydrogenation catalyst |
| cmmmech:spent-zinc-manganese-button-cell-batteries | data/records/spent-zinc-manganese-button-cell-batteries.yaml | maintained | Spent zinc-manganese button-cell batteries |
| cmmmech:tannery-sludge | data/records/tannery-sludge.yaml | maintained | Tannery sludge |
| cmmmech:tannery-wastewater | data/records/tannery-wastewater.yaml | maintained | Tannery wastewater |
| cmmmech:theisen-sludge | data/records/theisen-sludge.yaml | maintained | Theisen sludge |
| cmmmech:titanogypsum | data/records/titanogypsum.yaml | maintained | Titanogypsum |
| cmmmech:traction-battery-hydrometallurgical-residue | data/records/traction-battery-hydrometallurgical-residue.yaml | maintained | Traction-battery hydrometallurgical residue |
| cmmmech:tungsten-nickel-iron-alloy-scrap | data/records/tungsten-nickel-iron-alloy-scrap.yaml | maintained | Tungsten-nickel-iron alloy scrap |
| cmmmech:tungsten-skarn-tailings | data/records/tungsten-skarn-tailings.yaml | maintained | Tungsten skarn-processing tailings |
| cmmmech:uranium-mine-tailings | data/records/uranium-mine-tailings.yaml | maintained | Uranium mine tailings |
| cmmmech:used-photographic-fixer-solutions | data/records/used-photographic-fixer-solutions.yaml | maintained | Used photographic fixer solutions |
| cmmmech:waste-liquid-crystal-display-panels | data/records/waste-liquid-crystal-display-panels.yaml | maintained | Waste liquid-crystal display panels |
| cmmmech:waste-multilayer-ceramic-capacitors | data/records/waste-multilayer-ceramic-capacitors.yaml | maintained | Waste multilayer ceramic capacitors |
| cmmmech:waste-printed-circuit-boards | data/records/waste-printed-circuit-boards.yaml | maintained | Waste printed circuit boards |
| cmmmech:waste-x-ray-films | data/records/waste-x-ray-films.yaml | maintained | Waste X-ray films |
| cmmmech:wood-ash | data/records/wood-ash.yaml | maintained | Wood ash |
| cmmmech:zinc-leach-residue | data/records/zinc-leach-residue.yaml | maintained | Zinc leach residue |
| cmmmech:zinc-purification-hot-filter-cake | data/records/zinc-purification-hot-filter-cake.yaml | maintained | Zinc purification hot filter cake |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate (secondary_resource cohort) | passed | True | cmmmech:acid-mine-drainage, cmmmech:allanite-leachate, cmmmech:aluminium-salt-slag, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:basic-oxygen-furnace-steel-slag, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:battery-black-mass, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:blast-furnace-cast-house-dust, cmmmech:boron-ore-concentration-tailings, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium-tanned-leather-shavings, cmmmech:chrysotile-asbestos-tailings, cmmmech:coal-beneficiation-waste, cmmmech:coal-fly-ash, cmmmech:coal-gasification-slag, cmmmech:coal-mine-drainage-treatment-solids, cmmmech:copper-anode-slime, cmmmech:copper-autoclave-slime, cmmmech:copper-flotation-tailings, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:electrical-cable-recycling-residues, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electrolytic-manganese-residue, cmmmech:electroplating-bath-effluents, cmmmech:electroplating-sludge, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ferrochrome-slag, cmmmech:fish-bone-residues, cmmmech:flue-gas-desulfurization-wastewater, cmmmech:fluorescent-lamp-phosphor, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gold-mine-tailings, cmmmech:ground-waste-tire-rubber, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron-ore-tailings, cmmmech:kaolin-mine-waste, cmmmech:lead-blast-furnace-slag, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:municipal-sewage-sludge, cmmmech:municipal-waste-incineration-ash, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-smelter-slag, cmmmech:oil-and-gas-produced-water, cmmmech:oil-sands-froth-treatment-tailings, cmmmech:petroleum-coke, cmmmech:petroleum-oily-sludge, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphogypsum, cmmmech:pig-manure, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:pyrite-roasting-cinder, cmmmech:reverse-osmosis-concentrate, cmmmech:samarium-cobalt-magnet-scrap, cmmmech:secondary-aluminium-dross, cmmmech:sewage-sludge-incineration-ash, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-cerium-glass-polishing-slurry, cmmmech:spent-copper-zinc-alumina-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrocracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-iron-molybdate-oxidation-catalyst, cmmmech:spent-ito-targets, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-ndfeb-magnets, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-nickel-steam-reforming-catalyst, cmmmech:spent-platinum-petroleum-reforming-catalyst, cmmmech:spent-potlining, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:spent-tantalum-capacitors, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:spent-vegetable-oil-hydrogenation-catalyst, cmmmech:spent-zinc-manganese-button-cell-batteries, cmmmech:tannery-sludge, cmmmech:tannery-wastewater, cmmmech:theisen-sludge, cmmmech:titanogypsum, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:tungsten-nickel-iron-alloy-scrap, cmmmech:tungsten-skarn-tailings, cmmmech:uranium-mine-tailings, cmmmech:used-photographic-fixer-solutions, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-multilayer-ceramic-capacitors, cmmmech:waste-printed-circuit-boards, cmmmech:waste-x-ray-films, cmmmech:wood-ash, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake | All 111 secondary_resource records pass LinkML structural, semantic, and canonical top-level key-order validation with 0 errors and 0 warnings. |
| just verify-history (secondary_resource cohort) | passed | True | cmmmech:acid-mine-drainage, cmmmech:allanite-leachate, cmmmech:aluminium-salt-slag, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:basic-oxygen-furnace-steel-slag, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:battery-black-mass, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:blast-furnace-cast-house-dust, cmmmech:boron-ore-concentration-tailings, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium-tanned-leather-shavings, cmmmech:chrysotile-asbestos-tailings, cmmmech:coal-beneficiation-waste, cmmmech:coal-fly-ash, cmmmech:coal-gasification-slag, cmmmech:coal-mine-drainage-treatment-solids, cmmmech:copper-anode-slime, cmmmech:copper-autoclave-slime, cmmmech:copper-flotation-tailings, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:electrical-cable-recycling-residues, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electrolytic-manganese-residue, cmmmech:electroplating-bath-effluents, cmmmech:electroplating-sludge, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ferrochrome-slag, cmmmech:fish-bone-residues, cmmmech:flue-gas-desulfurization-wastewater, cmmmech:fluorescent-lamp-phosphor, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gold-mine-tailings, cmmmech:ground-waste-tire-rubber, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron-ore-tailings, cmmmech:kaolin-mine-waste, cmmmech:lead-blast-furnace-slag, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:municipal-sewage-sludge, cmmmech:municipal-waste-incineration-ash, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-smelter-slag, cmmmech:oil-and-gas-produced-water, cmmmech:oil-sands-froth-treatment-tailings, cmmmech:petroleum-coke, cmmmech:petroleum-oily-sludge, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphogypsum, cmmmech:pig-manure, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:pyrite-roasting-cinder, cmmmech:reverse-osmosis-concentrate, cmmmech:samarium-cobalt-magnet-scrap, cmmmech:secondary-aluminium-dross, cmmmech:sewage-sludge-incineration-ash, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-cerium-glass-polishing-slurry, cmmmech:spent-copper-zinc-alumina-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrocracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-iron-molybdate-oxidation-catalyst, cmmmech:spent-ito-targets, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-ndfeb-magnets, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-nickel-steam-reforming-catalyst, cmmmech:spent-platinum-petroleum-reforming-catalyst, cmmmech:spent-potlining, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:spent-tantalum-capacitors, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:spent-vegetable-oil-hydrogenation-catalyst, cmmmech:spent-zinc-manganese-button-cell-batteries, cmmmech:tannery-sludge, cmmmech:tannery-wastewater, cmmmech:theisen-sludge, cmmmech:titanogypsum, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:tungsten-nickel-iron-alloy-scrap, cmmmech:tungsten-skarn-tailings, cmmmech:uranium-mine-tailings, cmmmech:used-photographic-fixer-solutions, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-multilayer-ceramic-capacitors, cmmmech:waste-printed-circuit-boards, cmmmech:waste-x-ray-films, cmmmech:wood-ash, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake | All 111 secondary_resource records have intact append-only history sidecars and matching curation_history metadata. |

## Scientific And Domain Assessments

### Secondary-resource waste/tailings/slag/scrap mechanisms, causal graphs, and UniProtKB protein groundings

evidence: supported. Targets: cmmmech:acid-mine-drainage, cmmmech:allanite-leachate, cmmmech:aluminium-salt-slag, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:basic-oxygen-furnace-steel-slag, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:battery-black-mass, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:blast-furnace-cast-house-dust, cmmmech:boron-ore-concentration-tailings, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium-tanned-leather-shavings, cmmmech:chrysotile-asbestos-tailings, cmmmech:coal-beneficiation-waste, cmmmech:coal-fly-ash, cmmmech:coal-gasification-slag, cmmmech:coal-mine-drainage-treatment-solids, cmmmech:copper-anode-slime, cmmmech:copper-autoclave-slime, cmmmech:copper-flotation-tailings, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:electrical-cable-recycling-residues, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electrolytic-manganese-residue, cmmmech:electroplating-bath-effluents, cmmmech:electroplating-sludge, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ferrochrome-slag, cmmmech:fish-bone-residues, cmmmech:flue-gas-desulfurization-wastewater, cmmmech:fluorescent-lamp-phosphor, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gold-mine-tailings, cmmmech:ground-waste-tire-rubber, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron-ore-tailings, cmmmech:kaolin-mine-waste, cmmmech:lead-blast-furnace-slag, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:municipal-sewage-sludge, cmmmech:municipal-waste-incineration-ash, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-smelter-slag, cmmmech:oil-and-gas-produced-water, cmmmech:oil-sands-froth-treatment-tailings, cmmmech:petroleum-coke, cmmmech:petroleum-oily-sludge, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphogypsum, cmmmech:pig-manure, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:pyrite-roasting-cinder, cmmmech:reverse-osmosis-concentrate, cmmmech:samarium-cobalt-magnet-scrap, cmmmech:secondary-aluminium-dross, cmmmech:sewage-sludge-incineration-ash, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-cerium-glass-polishing-slurry, cmmmech:spent-copper-zinc-alumina-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrocracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-iron-molybdate-oxidation-catalyst, cmmmech:spent-ito-targets, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-ndfeb-magnets, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-nickel-steam-reforming-catalyst, cmmmech:spent-platinum-petroleum-reforming-catalyst, cmmmech:spent-potlining, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:spent-tantalum-capacitors, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:spent-vegetable-oil-hydrogenation-catalyst, cmmmech:spent-zinc-manganese-button-cell-batteries, cmmmech:tannery-sludge, cmmmech:tannery-wastewater, cmmmech:theisen-sludge, cmmmech:titanogypsum, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:tungsten-nickel-iron-alloy-scrap, cmmmech:tungsten-skarn-tailings, cmmmech:uranium-mine-tailings, cmmmech:used-photographic-fixer-solutions, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-multilayer-ceramic-capacitors, cmmmech:waste-printed-circuit-boards, cmmmech:waste-x-ray-films, cmmmech:wood-ash, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake.

108/111 secondary_resource records contain primary-source-backed mechanisms (107/111 with microbial: true mechanisms and 1/111, cmmmech:ferrochrome-slag, with an abiotic microbial: false mechanism hydrochloric_acid_magnesium_extraction; 145 mechanisms total) and 37/111 contain grounded causal_graphs (40 graphs) and UniProtKB protein_examples across 25 unique accessions. In cmmmech:traction-battery-hydrometallurgical-residue, tth_hydrolase omits tetH from the parenthetical label and omits grounded consortium species/loci in description; in 14 single-species A. thiooxidans secondary_resource records, tth_hydrolase retains a pre-expansion singular label and omits paralog loci GCD22_14205 and GCD22_02315.

## Findings

### cmmmech-cycle6-stage4-finding-0001: tth_hydrolase node in traction-battery-hydrometallurgical-residue.yaml omits tetH from parenthetical label and omits grounded consortium species and locus tags in description

minor / open / confirmed; issue key: cmmmech.traction-battery-hydrometallurgical-residue.tth-hydrolase-consortium-label-and-description-omit-species-and-loci.

In data/records/traction-battery-hydrometallurgical-residue.yaml (cmmmech:traction-battery-hydrometallurgical-residue), causal_graphs[0] (acidophile_culture_associated_leaching_graph) node tth_hydrolase (lines 496-500) is grounded to 4 consortium tetrathionate hydrolase protein_examples across 3 species (Acidithiobacillus ferrooxidans ATCC 23270 UniProtKB:B7J3C9 tth / AFE_0029, Acidithiobacillus thiooxidans ATCC 19377 UniProtKB:A0A5P9XPU3 tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315, and Acidithiobacillus caldus SM-1 UniProtKB:F9ZNI0 Atc_1595 / TetH), but retains label 'Tth / TetH tetrathionate hydrolase (consortium tth)' (omitting tetH from the parenthetical) and a generic description 'Periplasmic pyrroloquinoline-domain hydrolase disproportionating tetrathionate into sulfate and protons.' that omits all grounded consortium species and locus tags, whereas sibling node sqr_reductase (lines 318-322) explicitly lists all grounded consortium species and locus tags in its description.

### cmmmech-cycle6-stage4-finding-0002: 16 single-species Acidithiobacillus thiooxidans causal_graphs retain singular tth_hydrolase node label and omit grounded paralog loci (GCD22_14205, GCD22_02315) in description

minor / open / confirmed; issue key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci.

Across the 673-record corpus, 16 single-species Acidithiobacillus thiooxidans records (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge, gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst) whose tth_hydrolase causal-graph nodes were expanded in Cycle 5 Stage 3 (PR #872) to include both A. thiooxidans ATCC 19377 tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3 tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315) still retain the pre-expansion singular label 'Tth tetrathionate hydrolase (tth)' and generic description 'Periplasmic tetrathionate hydrolase disproportionating tetrathionate into thiosulfate, elemental sulfur, sulfate, and protons.' without naming the two grounded paralog loci (GCD22_14205 and GCD22_02315), whereas sibling node sqr_reductase in all 16 graphs has label 'Sqr/Sqor sulfide-quinone reductase (sqr / sqor)' and explicitly names '(Sqr/Sqor; GCD22_02301 / GCD22_03207)' in its description, and the 8 Cycle 6 Stage 2 (PR #888, commit a9115e6c) single-species A. thiooxidans records (beverage-carton-hydropulping-reject, chromite-beneficiation-tailings, goethite, jarosite, nickel-laterite-ore, nickel, petroleum-coke, pharmaceutical-blister-packaging-waste) explicitly name '(tth GCD22_14205; tth GCD22_02315)' in tth_hydrolase.label and '(tth GCD22_14205 and tth GCD22_02315)' in tth_hydrolase.description. In this scope, 14 record(s) (automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust, copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders, spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst, spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst) exhibit this node label/description lag.

## Recommended Actions And Acceptance Checks

### act-align-traction-battery-tth-hydrolase-consortium-label-and-description

Update causal_graphs[0].nodes[1].label to 'Tth / TetH tetrathionate hydrolase (consortium tth / tetH)' and update causal_graphs[0].nodes[1].description in data/records/traction-battery-hydrometallurgical-residue.yaml to list the grounded consortium tetrathionate hydrolase loci across Acidithiobacillus ferrooxidans (tth / AFE_0029), A. thiooxidans (tth GCD22_14205 / GCD22_02315), and A. caldus (Atc_1595 / TetH) during Stage 5 grouped remediation with canonical history provenance.

- causal_graphs[0].nodes[1].label in data/records/traction-battery-hydrometallurgical-residue.yaml includes '(consortium tth / tetH)'.
- causal_graphs[0].nodes[1].description names the grounded consortium tetrathionate hydrolase species and locus tags (A. ferrooxidans tth / AFE_0029, A. thiooxidans tth GCD22_14205 / GCD22_02315, A. caldus Atc_1595 / TetH).
- A matching EDIT history sidecar exists in history/records/traction-battery-hydrometallurgical-residue/ and passes just check.

### act-align-thiooxidans-tth-hydrolase-paralog-loci-labels-and-descriptions

Update causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description in the affected single-species Acidithiobacillus thiooxidans records to explicitly name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci (tth GCD22_14205 and tth GCD22_02315) during Stage 5 grouped remediation with canonical history provenance.

- All affected records name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci (GCD22_14205 and GCD22_02315) in causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries

- retain: cmmmech:acid-mine-drainage, cmmmech:allanite-leachate, cmmmech:aluminium-salt-slag, cmmmech:automotive-wastewater-treatment-sludge, cmmmech:basic-oxygen-furnace-steel-slag, cmmmech:basic-oxygen-furnace-steelmaking-dust, cmmmech:battery-black-mass, cmmmech:bauxite-residue, cmmmech:beverage-carton-hydropulping-reject, cmmmech:biogas-desulfurization-sulfur-residue, cmmmech:blast-furnace-cast-house-dust, cmmmech:boron-ore-concentration-tailings, cmmmech:cadmium-telluride-photovoltaic-module-scrap, cmmmech:cathode-ray-tube-glass, cmmmech:cemented-tungsten-carbide-scrap, cmmmech:chromite-beneficiation-tailings, cmmmech:chromite-ore-processing-residue, cmmmech:chromium-tanned-leather-shavings, cmmmech:chrysotile-asbestos-tailings, cmmmech:coal-beneficiation-waste, cmmmech:coal-fly-ash, cmmmech:coal-gasification-slag, cmmmech:coal-mine-drainage-treatment-solids, cmmmech:copper-anode-slime, cmmmech:copper-autoclave-slime, cmmmech:copper-flotation-tailings, cmmmech:copper-smelter-flue-dust, cmmmech:copper-smelter-slag, cmmmech:discarded-led-lamps, cmmmech:electric-arc-furnace-dust, cmmmech:electrical-cable-recycling-residues, cmmmech:electroformed-copper-silver-manufacturing-scrap, cmmmech:electrolytic-manganese-residue, cmmmech:electroplating-bath-effluents, cmmmech:electroplating-sludge, cmmmech:end-of-life-cigs-photovoltaic-modules, cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules, cmmmech:ferrochrome-slag, cmmmech:fish-bone-residues, cmmmech:flue-gas-desulfurization-wastewater, cmmmech:fluorescent-lamp-phosphor, cmmmech:gaas-production-hydroxide-sludge, cmmmech:gold-mine-tailings, cmmmech:ground-waste-tire-rubber, cmmmech:heavy-fuel-oil-combustion-ash, cmmmech:ion-adsorption-rare-earth-leach-residue, cmmmech:iron-ore-tailings, cmmmech:kaolin-mine-waste, cmmmech:lead-blast-furnace-slag, cmmmech:metal-grinding-sludge, cmmmech:metallic-machining-burrs, cmmmech:municipal-sewage-sludge, cmmmech:municipal-waste-incineration-ash, cmmmech:nickel-based-superalloy-residue-powders, cmmmech:nickel-flotation-tailings, cmmmech:nickel-smelter-slag, cmmmech:oil-and-gas-produced-water, cmmmech:oil-sands-froth-treatment-tailings, cmmmech:petroleum-coke, cmmmech:petroleum-oily-sludge, cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:phosphate-ore-tailings, cmmmech:phosphogypsum, cmmmech:pig-manure, cmmmech:ponded-coal-ash, cmmmech:poultry-bone-residues, cmmmech:pyrite-roasting-cinder, cmmmech:reverse-osmosis-concentrate, cmmmech:samarium-cobalt-magnet-scrap, cmmmech:secondary-aluminium-dross, cmmmech:sewage-sludge-incineration-ash, cmmmech:spent-alkaline-zinc-carbon-batteries, cmmmech:spent-automotive-three-way-catalyst, cmmmech:spent-cerium-glass-polishing-slurry, cmmmech:spent-copper-zinc-alumina-catalyst, cmmmech:spent-fluid-catalytic-cracking-catalyst, cmmmech:spent-hydrocracking-catalyst, cmmmech:spent-hydrodesulfurization-catalyst, cmmmech:spent-iron-molybdate-oxidation-catalyst, cmmmech:spent-ito-targets, cmmmech:spent-lead-acid-battery-electrolyte, cmmmech:spent-ndfeb-magnets, cmmmech:spent-nickel-cadmium-batteries, cmmmech:spent-nickel-metal-hydride-batteries, cmmmech:spent-nickel-steam-reforming-catalyst, cmmmech:spent-platinum-petroleum-reforming-catalyst, cmmmech:spent-potlining, cmmmech:spent-selective-catalytic-reduction-catalyst, cmmmech:spent-silver-oxide-zinc-button-cell-batteries, cmmmech:spent-steel-pickling-liquors, cmmmech:spent-sulfuric-acid-production-catalyst, cmmmech:spent-tantalum-capacitors, cmmmech:spent-vanadium-flow-battery-electrolyte, cmmmech:spent-vegetable-oil-hydrogenation-catalyst, cmmmech:spent-zinc-manganese-button-cell-batteries, cmmmech:tannery-sludge, cmmmech:tannery-wastewater, cmmmech:theisen-sludge, cmmmech:titanogypsum, cmmmech:traction-battery-hydrometallurgical-residue, cmmmech:tungsten-nickel-iron-alloy-scrap, cmmmech:tungsten-skarn-tailings, cmmmech:uranium-mine-tailings, cmmmech:used-photographic-fixer-solutions, cmmmech:waste-liquid-crystal-display-panels, cmmmech:waste-multilayer-ceramic-capacitors, cmmmech:waste-printed-circuit-boards, cmmmech:waste-x-ray-films, cmmmech:wood-ash, cmmmech:zinc-leach-residue, cmmmech:zinc-purification-hot-filter-cake. All 111 records in this cohort denote distinct, non-synonymous entities matching data/records/*.yaml where material_kind == 'secondary_resource' at fab0682688678750d7da4e5357dda11592d5fac3 with no duplicate IDs, names, or external identifier collisions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-secondary-resource-cohort-audit | data/records/*.yaml (material_kind == 'secondary_resource'); 111 secondary_resource YAML files | supports | Full programmatic and source-backed audit of all 111 secondary_resource records at commit fab0682688678750d7da4e5357dda11592d5fac3. |
| ev-traction-battery-lu2025 | DOI:10.1039/D5RA07472J; Lu et al. 2025 RSC Advances 15:45979-45985, Sections 2.1-2.3 and SI Table S1 | supports | Lu et al. (2025) studied separate acid-leached nickel-line and cobalt-line traction-battery hydrometallurgical residues leached by five acidophilic cultures (Af, Lf, Tt, Ac, St) and consortia (MC40-25St, MC45-40AS), with tetrathionate hydrolase grounded across A. ferrooxidans (tth / AFE_0029), A. thiooxidans (tth GCD22_14205 / GCD22_02315), and A. caldus (Atc_1595 / TetH). |

## Limits And Additional Notes

- Three secondary_resource records currently lack curated mechanisms (and one additional record carries an abiotic mechanism only): cmmmech:oil-and-gas-produced-water, cmmmech:spent-vegetable-oil-hydrogenation-catalyst, and cmmmech:theisen-sludge are maintained secondary-resource records without mechanisms (and cmmmech:ferrochrome-slag currently carries only an abiotic microbial: false HCl leaching mechanism) awaiting primary experimental microbial bioleaching/recovery studies. (108/111 secondary_resource records carry mechanisms (107/111 microbial, 1/111 abiotic); 3/111 document feedstock identity and composition only.)
- Cohort covers 100% (111/111) of secondary_resource records in data/records/*.yaml at commit fab0682688678750d7da4e5357dda11592d5fac3.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T132005Z-cycle6-stage4-secondary-resource-cohort-review
title: 'Cycle 6 Stage 4 full-cohort review: secondary_resource records (111/111)'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-31T13:10:00Z'
finished_at: '2026-10-31T13:20:05Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed all 111 secondary_resource records in data/records/*.yaml at commit
  fab0682688678750d7da4e5357dda11592d5fac3, including the 8 Cycle 6 Stage 2 (PR #888,
  commit a9115e6c) secondary_resource causal-graph and UniProtKB grounding additions
  (cmmmech:beverage-carton-hydropulping-reject, cmmmech:chromite-beneficiation-tailings,
  cmmmech:fish-bone-residues, cmmmech:municipal-sewage-sludge, cmmmech:petroleum-coke,
  cmmmech:pharmaceutical-blister-packaging-waste, cmmmech:poultry-bone-residues, cmmmech:tannery-sludge),
  the Cycle 6 Stage 3 (PR #893, commit fab06826) UniProtKB grounding addition on cmmmech:allanite-leachate,
  and the Cycle 5 Stage 5 (PR #880, commit b9ef4149) remediation of cmmmech:waste-liquid-crystal-display-panels.
  108/111 secondary_resource records contain primary-source-backed mechanisms (107/111
  with microbial: true mechanisms and 1/111, cmmmech:ferrochrome-slag, with an abiotic
  microbial: false mechanism hydrochloric_acid_magnesium_extraction; 145 mechanisms
  total), and 37/111 contain multi-step causal_graphs (40 graphs) and live-verified
  UniProtKB protein_examples across 25 unique accessions. Identified 2 minor graph
  node label/description findings (cmmmech-cycle6-stage4-finding-0001 on cmmmech:traction-battery-hydrometallurgical-residue
  and cmmmech-cycle6-stage4-finding-0002 across 14 single-species A. thiooxidans secondary_resource
  records) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 6 Stage 4 record_review
    (.claude/skills/review-yaml-category/SKILL.md) against frozen commit fab0682688678750d7da4e5357dda11592d5fac3.
source:
  git_revision: fab0682688678750d7da4e5357dda11592d5fac3
  state: git_commit
  inputs:
  - path: data/records/acid-mine-drainage.yaml
    sha256: cb7c908b4eb6482de97abed1d0f6a3501d9e04abd9ff8c9ae6f20c431ebff6e6
    role: target
  - path: data/records/allanite-leachate.yaml
    sha256: 32fe127fe3a3ce0400199d40c0545a85345b00bb0fda2a5078a539039c3a4e1c
    role: target
  - path: data/records/aluminium-salt-slag.yaml
    sha256: 0c5300af9596a26357f8e043367182dab0b9bb1df26e8eaba81a76fc5f431c09
    role: target
  - path: data/records/automotive-wastewater-treatment-sludge.yaml
    sha256: 864f0adb7f6e73d06c2aea215b3ec63046f553486281dc9e37c6eec0aa92326e
    role: target
  - path: data/records/basic-oxygen-furnace-steel-slag.yaml
    sha256: 88e0d8b3c9ce06a1d70cf1ab5a34059259c28eac1904cf9589a9dd9364575ea4
    role: target
  - path: data/records/basic-oxygen-furnace-steelmaking-dust.yaml
    sha256: 79c2f6499166f317766618a25684e1f639499e919fbcfc291c1c0f27b92b702f
    role: target
  - path: data/records/battery-black-mass.yaml
    sha256: 0e0e045b59f2728e9cdfd2aabcec3848bad611d60dc18599cccf3a824f687a28
    role: target
  - path: data/records/bauxite-residue.yaml
    sha256: fbad4371b1d3ffed508163dc947332d39f17190aa5b2367c40022caf7f1cab46
    role: target
  - path: data/records/beverage-carton-hydropulping-reject.yaml
    sha256: 017344bcb108e373627b1a02cda46ba1f237ded11640f8cec5281c57e4341828
    role: target
  - path: data/records/biogas-desulfurization-sulfur-residue.yaml
    sha256: 6cd930791244eec71896f7919e40daea23e1e0ba5a1b0993bed6a0a2b5b49b70
    role: target
  - path: data/records/blast-furnace-cast-house-dust.yaml
    sha256: ccc46cf9f7da3a4cf4cb4bde911ad7abce4eaf720c465d9f042b7cd7a6bb21f7
    role: target
  - path: data/records/boron-ore-concentration-tailings.yaml
    sha256: ade7411923a81921cd55f980c8ff48c53a7dc32c652672621e1fb361859c5fa7
    role: target
  - path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
    sha256: 0831e5c256868ee34c60c03c900ee65b3de8291f6336430e0f8eb3967956ad65
    role: target
  - path: data/records/cathode-ray-tube-glass.yaml
    sha256: 9aeab2c8c5914e8f224fae483f3cbdcbebb599e131ca4a57f2c23b1236aecfad
    role: target
  - path: data/records/cemented-tungsten-carbide-scrap.yaml
    sha256: 16210c05938ea5d7486a5450dcf2c7e8d04192a82fbc991bb62c1c84699ed422
    role: target
  - path: data/records/chromite-beneficiation-tailings.yaml
    sha256: ca8ff5d800723ed8c1bb6e5a6d514cbae16ee27dd0d2400b524309fe244e5859
    role: target
  - path: data/records/chromite-ore-processing-residue.yaml
    sha256: 7d9f158c0b08285f9bc2f6e4eb620958078cab63f524dd5eda38ca53cac9c893
    role: target
  - path: data/records/chromium-tanned-leather-shavings.yaml
    sha256: 1c0401c080f369e1c83721177a675018ad70c78145fc0932ce4d2163165e620d
    role: target
  - path: data/records/chrysotile-asbestos-tailings.yaml
    sha256: 00984956be6f2c83bd5cbe22e7e2fac227e874ed78a5063468d0c200cc5f101d
    role: target
  - path: data/records/coal-beneficiation-waste.yaml
    sha256: 62a71592ae8b49f146f154435b6715a939de4127fd2cf141414e6b2496588516
    role: target
  - path: data/records/coal-fly-ash.yaml
    sha256: cf34e4290d857ff173b845ab1ea3e77a37c54c289e5326bf40cb015110b2901d
    role: target
  - path: data/records/coal-gasification-slag.yaml
    sha256: eb3030529d996be96b29e4adc4bdd37dfa81c68084fe77dc64817ab01c0b4fba
    role: target
  - path: data/records/coal-mine-drainage-treatment-solids.yaml
    sha256: 9fce0c00b764999d6dd324311b30ec492d3b8cd9e3ff869f618e587d06e0baa9
    role: target
  - path: data/records/copper-anode-slime.yaml
    sha256: 2bfe9e35d282c686fb5352e77db3da5aadbc2b69c409cceca5fe8ff64281f373
    role: target
  - path: data/records/copper-autoclave-slime.yaml
    sha256: f3ac236a434e2ede82ca9a98f84c942dafba680194ff56b0f0897316becef594
    role: target
  - path: data/records/copper-flotation-tailings.yaml
    sha256: f0b1e1e1ef7608409d07381a29588802f7712793541e6545b811eaa2accefd7a
    role: target
  - path: data/records/copper-smelter-flue-dust.yaml
    sha256: 1667faf39bf234c10b4cd88e2ab1ea3d0b1ca77bfd74d10e29fc9c76595091b0
    role: target
  - path: data/records/copper-smelter-slag.yaml
    sha256: c24ca5deee97785fa49ed77f1cc1ec2e8d93eaed766168d12054443a011ceb78
    role: target
  - path: data/records/discarded-led-lamps.yaml
    sha256: 18c4093596efaa65f532b4d52c404fbbce1c975ee5fcac2c4025d928991f2b7b
    role: target
  - path: data/records/electric-arc-furnace-dust.yaml
    sha256: 59b8596c8ad743a78ffd53d4b3c759fdf9c4c52924148be74ec9657f69433cbb
    role: target
  - path: data/records/electrical-cable-recycling-residues.yaml
    sha256: 67878d2b2136825ededf6c52f80812d7ce508d34a9193f571cbaf5f5e0f28a0f
    role: target
  - path: data/records/electroformed-copper-silver-manufacturing-scrap.yaml
    sha256: d6ca2fdab6864ea98e0cb0e5a687426da356559e9cd77b90af7089752ab5aa38
    role: target
  - path: data/records/electrolytic-manganese-residue.yaml
    sha256: 2b049bbf4af80158c48fb0e26398894a3879ecdc26fa1df023893e21c7197fe7
    role: target
  - path: data/records/electroplating-bath-effluents.yaml
    sha256: 0e8234fc7f0f969c442f8085fadb4748725d9ff85bd2ebe3190c4070583d135b
    role: target
  - path: data/records/electroplating-sludge.yaml
    sha256: 52fe4cc69ac0807a77d921c2de8c35a25bf812c345ed1854b4b46c58e6cf281b
    role: target
  - path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
    sha256: c795734bd44968f4bd3344b85f08d73579c83cfaca5e52a441a7f6884ac2913a
    role: target
  - path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
    sha256: 3ba90fe05d6a643cba04da24caed02a479588236256ef8b0589e62cc791b1539
    role: target
  - path: data/records/ferrochrome-slag.yaml
    sha256: e0fb45e628bffe1b413f06a098f54ad34c4fe47e094d2b35880cef9a7a28e9c9
    role: target
  - path: data/records/fish-bone-residues.yaml
    sha256: 86f8e14fb26f46f9e89c59c4aa164ebfda13ae6dd89fe02c86fe77af3a6e4554
    role: target
  - path: data/records/flue-gas-desulfurization-wastewater.yaml
    sha256: 7765854c5dfb2ce86f5fe516bf19b63e59978b21e3b3da822118769b36a5a8e3
    role: target
  - path: data/records/fluorescent-lamp-phosphor.yaml
    sha256: cd27c40ce1c11eae898b561a7adc83373d0f3d228f393025edc2421a58272e03
    role: target
  - path: data/records/gaas-production-hydroxide-sludge.yaml
    sha256: a4b899947ef638b1e561b2d12994503dac87cff9181f68d941ac28ceff3bd2da
    role: target
  - path: data/records/gold-mine-tailings.yaml
    sha256: 2c7a2a67888f3a32a8e9046e02cb206377affaa9b73803151b2ecfaba528fd06
    role: target
  - path: data/records/ground-waste-tire-rubber.yaml
    sha256: 73d1bbb5d61980816468cc5830ccaeb845d25c130e6ca662d93573fce51d04f6
    role: target
  - path: data/records/heavy-fuel-oil-combustion-ash.yaml
    sha256: 52579409f14e3b9dd2cb8f1505ea1f08515fa2f624353f11e661a2c4f3df7c45
    role: target
  - path: data/records/ion-adsorption-rare-earth-leach-residue.yaml
    sha256: a7bc2ba234388913d774a62e95e4ae18bccdfe36069ed4ec0b6f779ef42bf274
    role: target
  - path: data/records/iron-ore-tailings.yaml
    sha256: 98414fa5f270d8814225c1ae9d2538e312d6a6887de12e05c92c37c6e429ab85
    role: target
  - path: data/records/kaolin-mine-waste.yaml
    sha256: bbbda01b75a9a4bfa2721c030c3458b2f9873aa6cf02fe1624c6eb61a1a576c2
    role: target
  - path: data/records/lead-blast-furnace-slag.yaml
    sha256: 6d02347365ea9fc8cd7eab4d5f0683634e7e35eced09b3e3d5fed8b92a49bbdc
    role: target
  - path: data/records/metal-grinding-sludge.yaml
    sha256: 85d1e8e97a505acbe0bc7898ccd9e9de8ead904062d3042d8a766c54af5978cd
    role: target
  - path: data/records/metallic-machining-burrs.yaml
    sha256: 7b0698dddd68fa46ae22cc99a7ad35687d1675e4a9e7a7cca874018414ea9589
    role: target
  - path: data/records/municipal-sewage-sludge.yaml
    sha256: a3b578e3cd85a212912adc062c7c209cebd91c5c9d2e125537382882a3134540
    role: target
  - path: data/records/municipal-waste-incineration-ash.yaml
    sha256: 3677ebff576d161d1ad015d57f7ca27c810a17bc81a4166feb7efbdf8d154d52
    role: target
  - path: data/records/nickel-based-superalloy-residue-powders.yaml
    sha256: ec2fefe832f810b3cb6f7a0b6c15109753718b942d6bf6d68d49507e5a5604cf
    role: target
  - path: data/records/nickel-flotation-tailings.yaml
    sha256: 92aab61f56f1ac21279db66d814d57f67ca5cee0c1186a7ff27ca3026b922327
    role: target
  - path: data/records/nickel-smelter-slag.yaml
    sha256: 7dd113070944069fc2c4c8ab1096407587759570dc0a16c99f4bd53dc7947f71
    role: target
  - path: data/records/oil-and-gas-produced-water.yaml
    sha256: 83d79172269bb7ea45169a0c4bc1e1a268c77c356d79ba37e7564be88a1af077
    role: target
  - path: data/records/oil-sands-froth-treatment-tailings.yaml
    sha256: 0a7ce5b2525c4e3e5a4250d048262ecb4511bc1b7098e8d27241cf081c4d5fed
    role: target
  - path: data/records/petroleum-coke.yaml
    sha256: 1aa38741a5024ffb99744440d65e01e415607cc5fb31817261758ccfe531bb0f
    role: target
  - path: data/records/petroleum-oily-sludge.yaml
    sha256: 26a080b95e4c3f0fe62dae4718cbc8bf622726fa58f1107d4c3b27202f798fe0
    role: target
  - path: data/records/pharmaceutical-blister-packaging-waste.yaml
    sha256: 2aeecf814499bb4584272696b84f3404ca7d9fc82375ef76e9043cba222967dd
    role: target
  - path: data/records/phosphate-ore-tailings.yaml
    sha256: 50362c4b71b2aa4a5c2fa184ee9333ea90ca07c40dcd90554a24bef01409cc59
    role: target
  - path: data/records/phosphogypsum.yaml
    sha256: 3abec770a259f6f0ed305210918c0cf6c7d18fb52bbaf4fea300abfcd80b42e2
    role: target
  - path: data/records/pig-manure.yaml
    sha256: 20caf6979236a7b9464da8e1f43fe1f95547f7d8cc0dc2576ff6b676f418a124
    role: target
  - path: data/records/ponded-coal-ash.yaml
    sha256: 5d5712cdde4b4afd85e499953016b93b9bf64ab0d286d2f26f94020d65f08d70
    role: target
  - path: data/records/poultry-bone-residues.yaml
    sha256: c89e05a69bc4d15c673934d48aaa96a7900a9768543a1f71cd45410a72ad7035
    role: target
  - path: data/records/pyrite-roasting-cinder.yaml
    sha256: 2f0285c341ab210862675b6e438ed7067234ecbaf4f074a0ee7a2b3799e51838
    role: target
  - path: data/records/reverse-osmosis-concentrate.yaml
    sha256: 19cad077f7e6536be6cb051af5fdfb3f0d6fe6c72d40cccbe3c3e18b51b1fe73
    role: target
  - path: data/records/samarium-cobalt-magnet-scrap.yaml
    sha256: 794b64eec162fb182c5fef373478ee0962c32a710748524469266aac34588e4d
    role: target
  - path: data/records/secondary-aluminium-dross.yaml
    sha256: 7b93f8a63f5a8f39ba2e14b08ee020a50918a7343342aadd92d6f0527c15b4f8
    role: target
  - path: data/records/sewage-sludge-incineration-ash.yaml
    sha256: 2c63142c818ba0e3309df50b45f614b0a6ff2c0d39e370a9e0651d3b5d999a0a
    role: target
  - path: data/records/spent-alkaline-zinc-carbon-batteries.yaml
    sha256: 05e5341fb892b6c233e828ff8c355599a6e184fae5cde9ce4dfdf02e4921bcfb
    role: target
  - path: data/records/spent-automotive-three-way-catalyst.yaml
    sha256: cd6d8f72398dd494f45335abe36e6db0e5e1e3ea95b85e7a4b1db6c78aaf6f7d
    role: target
  - path: data/records/spent-cerium-glass-polishing-slurry.yaml
    sha256: 7fa0a45984674b3e2e944ad0de064a1013ee3abd7cb6bed910db5d3a7d5da750
    role: target
  - path: data/records/spent-copper-zinc-alumina-catalyst.yaml
    sha256: 9524794b431d61034e75019f4198991b57cd031a8bb17a7dff7525fbdbd1f576
    role: target
  - path: data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    sha256: 9fb9aeaf3295130949239a3b9342523dd5f602b2ec1fa716f1866056a0a8b5e0
    role: target
  - path: data/records/spent-hydrocracking-catalyst.yaml
    sha256: 8bb94dfd26a8e4ad935a3337314ca4d7b96dbb50f857d8ca7405140b7df82e95
    role: target
  - path: data/records/spent-hydrodesulfurization-catalyst.yaml
    sha256: c82183671ae85b34674fe418617345ebf78b24aed6339fd1240a926cdc21fcf2
    role: target
  - path: data/records/spent-iron-molybdate-oxidation-catalyst.yaml
    sha256: 4011a75d4fede3ab20e8317630fe4adfa770c16485a797962fc81a92549a9b7f
    role: target
  - path: data/records/spent-ito-targets.yaml
    sha256: 0fdb179b3857ce3ab42360c6bc15fab14e80d041f087a404c18e81ad0df169b0
    role: target
  - path: data/records/spent-lead-acid-battery-electrolyte.yaml
    sha256: e7c1729cb7d7bef64858cdc6e78ef7d48da7081e96e2d842f32e54d93345149c
    role: target
  - path: data/records/spent-ndfeb-magnets.yaml
    sha256: 9a55438ef82ebcb1a7568878377e0ccb9c5762e2370f154b2c76902ad8c34697
    role: target
  - path: data/records/spent-nickel-cadmium-batteries.yaml
    sha256: 3ab36654c99842e481666088f5cf0b402ba7a2598ffb4bea8a448af021deeffe
    role: target
  - path: data/records/spent-nickel-metal-hydride-batteries.yaml
    sha256: 9e07ce9af31462bfb138454b7176106e2d245b0d381a82e3c097cf5df3d2a301
    role: target
  - path: data/records/spent-nickel-steam-reforming-catalyst.yaml
    sha256: 3c29f06900b5194a74d457ebbe68f6b010ef59c7ca1cef34fdc98fad6a99cce4
    role: target
  - path: data/records/spent-platinum-petroleum-reforming-catalyst.yaml
    sha256: 9ef7ee0ef80cba2bbd8b470a9bac008b6ddc7e47fa1f472e1f52ba02c9b28a74
    role: target
  - path: data/records/spent-potlining.yaml
    sha256: 28a700b73213bd244b8d3c3d5a52c74393e5ef6d5e1d77b23863fcbfa05b67b5
    role: target
  - path: data/records/spent-selective-catalytic-reduction-catalyst.yaml
    sha256: a212d7f2947fe0d66e0719fa44cf340bfb59084ca49324310b8dcebc5efa4b5f
    role: target
  - path: data/records/spent-silver-oxide-zinc-button-cell-batteries.yaml
    sha256: 199b1a45cdab2fc47d99767df4aec89cb7b9b150de02bc52f72bc826936b2844
    role: target
  - path: data/records/spent-steel-pickling-liquors.yaml
    sha256: 7f6bf922bc7a09f2056f11c52084dcfd2ab563c550efe7dd253b661f0d3420e2
    role: target
  - path: data/records/spent-sulfuric-acid-production-catalyst.yaml
    sha256: 91d42e2c4da17ddb0bc9c47dd55045473b6d33178d599bdc95ce5320fdef0d49
    role: target
  - path: data/records/spent-tantalum-capacitors.yaml
    sha256: 4d586a10e5166b8c3a49b34770f9584cf96968a8e74031d0a6f4a7d20468398f
    role: target
  - path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    sha256: 7aac22892924322ff61a41160d000a7c283c7291c133872aa9a53affac822e90
    role: target
  - path: data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml
    sha256: 4805ee17fbc683dc7cd6cd1a314493ab3a770b20987c4853dbb330eb2b61cbe4
    role: target
  - path: data/records/spent-zinc-manganese-button-cell-batteries.yaml
    sha256: 654b80d40921f1115811bde3a2f71b11d0ee337ce49835cd4779b87492f7e217
    role: target
  - path: data/records/tannery-sludge.yaml
    sha256: d8843b3142e54f8ddbded8154f44c3f4a64ca2aa43961045204477476d13e27e
    role: target
  - path: data/records/tannery-wastewater.yaml
    sha256: 8597e28a89aa444285118e1ccf08f83b8c68f124ec73c1fdc32020f10748d5b1
    role: target
  - path: data/records/theisen-sludge.yaml
    sha256: 9b06fd03d106e687f5618d9a5faf1601e80b0c88f5fc908e0d5604d5d10a96d5
    role: target
  - path: data/records/titanogypsum.yaml
    sha256: da978617d7f84a63f2904ee3e78a682c3ff8d0644e85b64d86ff1da5ab409f72
    role: target
  - path: data/records/traction-battery-hydrometallurgical-residue.yaml
    sha256: 84833b4223378cffeb4ad7013b19727824d47dcd0f88663707b2d6bacd3b7c94
    role: target
  - path: data/records/tungsten-nickel-iron-alloy-scrap.yaml
    sha256: ffc93d35f6dba2ec9a4dd3123687ee2d35142d7c4ab0e875680bb43140cfda60
    role: target
  - path: data/records/tungsten-skarn-tailings.yaml
    sha256: 76f7605b69902eacc1b1e36ecd3e953ed0acef1ba62ba30b67d9742ab596576c
    role: target
  - path: data/records/uranium-mine-tailings.yaml
    sha256: a217692da8148f706ce40260f18f1cd83d56b01e60eb3f3e21ba01c52535dfca
    role: target
  - path: data/records/used-photographic-fixer-solutions.yaml
    sha256: 7563b9891d5c3395802edc595210856ed3cf1c317db71503ff34d0a7a4b5fbe9
    role: target
  - path: data/records/waste-liquid-crystal-display-panels.yaml
    sha256: 065252079cfc86daa3c8a770ca62b02c3b5fa691c53688f83a80cfb4bf6725f5
    role: target
  - path: data/records/waste-multilayer-ceramic-capacitors.yaml
    sha256: eb82b9234b68ff42b1fbe376d9471c40399a24aeef1e1d5e87d376bead63d5b0
    role: target
  - path: data/records/waste-printed-circuit-boards.yaml
    sha256: 7f7f5fd7a65e2d2aa31bbd749a755e24bfdb167a515fdec7abd86a159228e58d
    role: target
  - path: data/records/waste-x-ray-films.yaml
    sha256: e221e4cfb6f0a3105cf2138a82c93aef199c245e157228e7ac80ed4a594f1575
    role: target
  - path: data/records/wood-ash.yaml
    sha256: 95b555c5a2a665dcb44fc245b59b3c639b6c008d3536f760cf02bb3c02dbf920
    role: target
  - path: data/records/zinc-leach-residue.yaml
    sha256: d64d9222f66148173474919996974a4e10b31d4665e382b3037fa30492555580
    role: target
  - path: data/records/zinc-purification-hot-filter-cake.yaml
    sha256: 909cb9279b6ebd29cce82bd0fdfb3d0b7e090b0fb4654d2c609c785294d36a0e
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 111
  reviewed_target_ids:
  - cmmmech:acid-mine-drainage
  - cmmmech:allanite-leachate
  - cmmmech:aluminium-salt-slag
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:basic-oxygen-furnace-steel-slag
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:battery-black-mass
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium-tanned-leather-shavings
  - cmmmech:chrysotile-asbestos-tailings
  - cmmmech:coal-beneficiation-waste
  - cmmmech:coal-fly-ash
  - cmmmech:coal-gasification-slag
  - cmmmech:coal-mine-drainage-treatment-solids
  - cmmmech:copper-anode-slime
  - cmmmech:copper-autoclave-slime
  - cmmmech:copper-flotation-tailings
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electrical-cable-recycling-residues
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electrolytic-manganese-residue
  - cmmmech:electroplating-bath-effluents
  - cmmmech:electroplating-sludge
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ferrochrome-slag
  - cmmmech:fish-bone-residues
  - cmmmech:flue-gas-desulfurization-wastewater
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron-ore-tailings
  - cmmmech:kaolin-mine-waste
  - cmmmech:lead-blast-furnace-slag
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:municipal-sewage-sludge
  - cmmmech:municipal-waste-incineration-ash
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-smelter-slag
  - cmmmech:oil-and-gas-produced-water
  - cmmmech:oil-sands-froth-treatment-tailings
  - cmmmech:petroleum-coke
  - cmmmech:petroleum-oily-sludge
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphogypsum
  - cmmmech:pig-manure
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:reverse-osmosis-concentrate
  - cmmmech:samarium-cobalt-magnet-scrap
  - cmmmech:secondary-aluminium-dross
  - cmmmech:sewage-sludge-incineration-ash
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-cerium-glass-polishing-slurry
  - cmmmech:spent-copper-zinc-alumina-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrocracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-iron-molybdate-oxidation-catalyst
  - cmmmech:spent-ito-targets
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-ndfeb-magnets
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-nickel-steam-reforming-catalyst
  - cmmmech:spent-platinum-petroleum-reforming-catalyst
  - cmmmech:spent-potlining
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:spent-tantalum-capacitors
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  - cmmmech:spent-zinc-manganese-button-cell-batteries
  - cmmmech:tannery-sludge
  - cmmmech:tannery-wastewater
  - cmmmech:theisen-sludge
  - cmmmech:titanogypsum
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:tungsten-nickel-iron-alloy-scrap
  - cmmmech:tungsten-skarn-tailings
  - cmmmech:uranium-mine-tailings
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-multilayer-ceramic-capacitors
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:waste-x-ray-films
  - cmmmech:wood-ash
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  selection: data/records/*.yaml where material_kind == 'secondary_resource' at fab0682688678750d7da4e5357dda11592d5fac3
  description: Full-population Cycle 6 Stage 4 category review of all 111 secondary_resource
    records in CMMMech.
targets:
- target_id: cmmmech:acid-mine-drainage
  path: data/records/acid-mine-drainage.yaml
  kind: maintained
  label: Acid mine drainage
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/acid-mine-drainage.yaml
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
- target_id: cmmmech:aluminium-salt-slag
  path: data/records/aluminium-salt-slag.yaml
  kind: maintained
  label: Aluminium salt slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aluminium-salt-slag.yaml
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
- target_id: cmmmech:basic-oxygen-furnace-steel-slag
  path: data/records/basic-oxygen-furnace-steel-slag.yaml
  kind: maintained
  label: Basic-oxygen-furnace steel slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/basic-oxygen-furnace-steel-slag.yaml
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
- target_id: cmmmech:battery-black-mass
  path: data/records/battery-black-mass.yaml
  kind: maintained
  label: Spent lithium-ion battery black mass
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/battery-black-mass.yaml
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
- target_id: cmmmech:biogas-desulfurization-sulfur-residue
  path: data/records/biogas-desulfurization-sulfur-residue.yaml
  kind: maintained
  label: Biogas-desulfurization sulfur residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/biogas-desulfurization-sulfur-residue.yaml
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
- target_id: cmmmech:cadmium-telluride-photovoltaic-module-scrap
  path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
  kind: maintained
  label: Cadmium telluride photovoltaic module scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmium-telluride-photovoltaic-module-scrap.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:cathode-ray-tube-glass
  path: data/records/cathode-ray-tube-glass.yaml
  kind: maintained
  label: Waste lead-bearing cathode-ray-tube glass
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cathode-ray-tube-glass.yaml
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
- target_id: cmmmech:chromium-tanned-leather-shavings
  path: data/records/chromium-tanned-leather-shavings.yaml
  kind: maintained
  label: Chromium-tanned leather shavings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium-tanned-leather-shavings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:chrysotile-asbestos-tailings
  path: data/records/chrysotile-asbestos-tailings.yaml
  kind: maintained
  label: Chrysotile asbestos tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chrysotile-asbestos-tailings.yaml
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
- target_id: cmmmech:coal-fly-ash
  path: data/records/coal-fly-ash.yaml
  kind: maintained
  label: Coal fly ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-fly-ash.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coal-gasification-slag
  path: data/records/coal-gasification-slag.yaml
  kind: maintained
  label: Coal gasification slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-gasification-slag.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:coal-mine-drainage-treatment-solids
  path: data/records/coal-mine-drainage-treatment-solids.yaml
  kind: maintained
  label: Coal-mine-drainage treatment solids
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-mine-drainage-treatment-solids.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:copper-anode-slime
  path: data/records/copper-anode-slime.yaml
  kind: maintained
  label: Copper anode slime
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-anode-slime.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:copper-autoclave-slime
  path: data/records/copper-autoclave-slime.yaml
  kind: maintained
  label: Copper autoclave slime
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-autoclave-slime.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:copper-flotation-tailings
  path: data/records/copper-flotation-tailings.yaml
  kind: maintained
  label: Copper flotation tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-flotation-tailings.yaml
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
- target_id: cmmmech:electrical-cable-recycling-residues
  path: data/records/electrical-cable-recycling-residues.yaml
  kind: maintained
  label: Electrical-cable recycling residues
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrical-cable-recycling-residues.yaml
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
- target_id: cmmmech:electrolytic-manganese-residue
  path: data/records/electrolytic-manganese-residue.yaml
  kind: maintained
  label: Electrolytic manganese residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrolytic-manganese-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:electroplating-bath-effluents
  path: data/records/electroplating-bath-effluents.yaml
  kind: maintained
  label: Electroplating-bath effluents
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electroplating-bath-effluents.yaml
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
- target_id: cmmmech:end-of-life-cigs-photovoltaic-modules
  path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
  kind: maintained
  label: End-of-life CIGS photovoltaic modules
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-cigs-photovoltaic-modules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
  kind: maintained
  label: End-of-life crystalline-silicon photovoltaic modules
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:ferrochrome-slag
  path: data/records/ferrochrome-slag.yaml
  kind: maintained
  label: Ferrochrome slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
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
- target_id: cmmmech:flue-gas-desulfurization-wastewater
  path: data/records/flue-gas-desulfurization-wastewater.yaml
  kind: maintained
  label: Flue-gas-desulfurization wastewater
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/flue-gas-desulfurization-wastewater.yaml
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
- target_id: cmmmech:ground-waste-tire-rubber
  path: data/records/ground-waste-tire-rubber.yaml
  kind: maintained
  label: Ground waste tire rubber
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ground-waste-tire-rubber.yaml
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
- target_id: cmmmech:iron-ore-tailings
  path: data/records/iron-ore-tailings.yaml
  kind: maintained
  label: Iron-ore tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/iron-ore-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:kaolin-mine-waste
  path: data/records/kaolin-mine-waste.yaml
  kind: maintained
  label: Kaolin mine waste
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin-mine-waste.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:lead-blast-furnace-slag
  path: data/records/lead-blast-furnace-slag.yaml
  kind: maintained
  label: Lead blast-furnace slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lead-blast-furnace-slag.yaml
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
- target_id: cmmmech:municipal-waste-incineration-ash
  path: data/records/municipal-waste-incineration-ash.yaml
  kind: maintained
  label: Municipal-waste incineration ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/municipal-waste-incineration-ash.yaml
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
- target_id: cmmmech:oil-and-gas-produced-water
  path: data/records/oil-and-gas-produced-water.yaml
  kind: maintained
  label: Oil and gas produced water
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/oil-and-gas-produced-water.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:oil-sands-froth-treatment-tailings
  path: data/records/oil-sands-froth-treatment-tailings.yaml
  kind: maintained
  label: Oil-sands froth-treatment tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/oil-sands-froth-treatment-tailings.yaml
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
- target_id: cmmmech:petroleum-oily-sludge
  path: data/records/petroleum-oily-sludge.yaml
  kind: maintained
  label: Petroleum oily sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/petroleum-oily-sludge.yaml
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
- target_id: cmmmech:pig-manure
  path: data/records/pig-manure.yaml
  kind: maintained
  label: Pig manure
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pig-manure.yaml
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
- target_id: cmmmech:reverse-osmosis-concentrate
  path: data/records/reverse-osmosis-concentrate.yaml
  kind: maintained
  label: Reverse osmosis concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/reverse-osmosis-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:samarium-cobalt-magnet-scrap
  path: data/records/samarium-cobalt-magnet-scrap.yaml
  kind: maintained
  label: Samarium-cobalt magnet scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium-cobalt-magnet-scrap.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:secondary-aluminium-dross
  path: data/records/secondary-aluminium-dross.yaml
  kind: maintained
  label: Secondary aluminium dross
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/secondary-aluminium-dross.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:sewage-sludge-incineration-ash
  path: data/records/sewage-sludge-incineration-ash.yaml
  kind: maintained
  label: Sewage-sludge incineration ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sewage-sludge-incineration-ash.yaml
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
- target_id: cmmmech:spent-cerium-glass-polishing-slurry
  path: data/records/spent-cerium-glass-polishing-slurry.yaml
  kind: maintained
  label: Spent cerium-based glass-polishing slurry
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-cerium-glass-polishing-slurry.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-copper-zinc-alumina-catalyst
  path: data/records/spent-copper-zinc-alumina-catalyst.yaml
  kind: maintained
  label: Spent copper-zinc-alumina catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-copper-zinc-alumina-catalyst.yaml
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
- target_id: cmmmech:spent-hydrocracking-catalyst
  path: data/records/spent-hydrocracking-catalyst.yaml
  kind: maintained
  label: Spent hydrocracking catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-hydrocracking-catalyst.yaml
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
- target_id: cmmmech:spent-iron-molybdate-oxidation-catalyst
  path: data/records/spent-iron-molybdate-oxidation-catalyst.yaml
  kind: maintained
  label: Spent iron-molybdate oxidation catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-iron-molybdate-oxidation-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-ito-targets
  path: data/records/spent-ito-targets.yaml
  kind: maintained
  label: Spent indium-tin oxide targets
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-ito-targets.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-lead-acid-battery-electrolyte
  path: data/records/spent-lead-acid-battery-electrolyte.yaml
  kind: maintained
  label: Spent lead-acid battery electrolyte
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-lead-acid-battery-electrolyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-ndfeb-magnets
  path: data/records/spent-ndfeb-magnets.yaml
  kind: maintained
  label: Spent NdFeB permanent magnets
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-ndfeb-magnets.yaml
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
- target_id: cmmmech:spent-nickel-steam-reforming-catalyst
  path: data/records/spent-nickel-steam-reforming-catalyst.yaml
  kind: maintained
  label: Spent nickel steam-reforming catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-nickel-steam-reforming-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-platinum-petroleum-reforming-catalyst
  path: data/records/spent-platinum-petroleum-reforming-catalyst.yaml
  kind: maintained
  label: Spent platinum petroleum-reforming catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-platinum-petroleum-reforming-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-potlining
  path: data/records/spent-potlining.yaml
  kind: maintained
  label: Spent potlining
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-potlining.yaml
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
- target_id: cmmmech:spent-tantalum-capacitors
  path: data/records/spent-tantalum-capacitors.yaml
  kind: maintained
  label: Spent tantalum capacitors
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-tantalum-capacitors.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-vanadium-flow-battery-electrolyte
  path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
  kind: maintained
  label: Spent vanadium-flow-battery electrolyte
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  path: data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml
  kind: maintained
  label: Spent vegetable-oil hydrogenation catalyst
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:spent-zinc-manganese-button-cell-batteries
  path: data/records/spent-zinc-manganese-button-cell-batteries.yaml
  kind: maintained
  label: Spent zinc-manganese button-cell batteries
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-zinc-manganese-button-cell-batteries.yaml
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
- target_id: cmmmech:tannery-wastewater
  path: data/records/tannery-wastewater.yaml
  kind: maintained
  label: Tannery wastewater
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tannery-wastewater.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:theisen-sludge
  path: data/records/theisen-sludge.yaml
  kind: maintained
  label: Theisen sludge
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/theisen-sludge.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:titanogypsum
  path: data/records/titanogypsum.yaml
  kind: maintained
  label: Titanogypsum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanogypsum.yaml
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
- target_id: cmmmech:tungsten-nickel-iron-alloy-scrap
  path: data/records/tungsten-nickel-iron-alloy-scrap.yaml
  kind: maintained
  label: Tungsten-nickel-iron alloy scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tungsten-nickel-iron-alloy-scrap.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:tungsten-skarn-tailings
  path: data/records/tungsten-skarn-tailings.yaml
  kind: maintained
  label: Tungsten skarn-processing tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tungsten-skarn-tailings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:uranium-mine-tailings
  path: data/records/uranium-mine-tailings.yaml
  kind: maintained
  label: Uranium mine tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranium-mine-tailings.yaml
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
- target_id: cmmmech:waste-multilayer-ceramic-capacitors
  path: data/records/waste-multilayer-ceramic-capacitors.yaml
  kind: maintained
  label: Waste multilayer ceramic capacitors
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-multilayer-ceramic-capacitors.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:waste-printed-circuit-boards
  path: data/records/waste-printed-circuit-boards.yaml
  kind: maintained
  label: Waste printed circuit boards
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-printed-circuit-boards.yaml
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
- target_id: cmmmech:wood-ash
  path: data/records/wood-ash.yaml
  kind: maintained
  label: Wood ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wood-ash.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zinc-leach-residue
  path: data/records/zinc-leach-residue.yaml
  kind: maintained
  label: Zinc leach residue
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-leach-residue.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
- target_id: cmmmech:zinc-purification-hot-filter-cake
  path: data/records/zinc-purification-hot-filter-cake.yaml
  kind: maintained
  label: Zinc purification hot filter cake
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-purification-hot-filter-cake.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: just-validate-secondary-resources
  name: just validate (secondary_resource cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:acid-mine-drainage
  - cmmmech:allanite-leachate
  - cmmmech:aluminium-salt-slag
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:basic-oxygen-furnace-steel-slag
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:battery-black-mass
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium-tanned-leather-shavings
  - cmmmech:chrysotile-asbestos-tailings
  - cmmmech:coal-beneficiation-waste
  - cmmmech:coal-fly-ash
  - cmmmech:coal-gasification-slag
  - cmmmech:coal-mine-drainage-treatment-solids
  - cmmmech:copper-anode-slime
  - cmmmech:copper-autoclave-slime
  - cmmmech:copper-flotation-tailings
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electrical-cable-recycling-residues
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electrolytic-manganese-residue
  - cmmmech:electroplating-bath-effluents
  - cmmmech:electroplating-sludge
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ferrochrome-slag
  - cmmmech:fish-bone-residues
  - cmmmech:flue-gas-desulfurization-wastewater
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron-ore-tailings
  - cmmmech:kaolin-mine-waste
  - cmmmech:lead-blast-furnace-slag
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:municipal-sewage-sludge
  - cmmmech:municipal-waste-incineration-ash
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-smelter-slag
  - cmmmech:oil-and-gas-produced-water
  - cmmmech:oil-sands-froth-treatment-tailings
  - cmmmech:petroleum-coke
  - cmmmech:petroleum-oily-sludge
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphogypsum
  - cmmmech:pig-manure
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:reverse-osmosis-concentrate
  - cmmmech:samarium-cobalt-magnet-scrap
  - cmmmech:secondary-aluminium-dross
  - cmmmech:sewage-sludge-incineration-ash
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-cerium-glass-polishing-slurry
  - cmmmech:spent-copper-zinc-alumina-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrocracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-iron-molybdate-oxidation-catalyst
  - cmmmech:spent-ito-targets
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-ndfeb-magnets
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-nickel-steam-reforming-catalyst
  - cmmmech:spent-platinum-petroleum-reforming-catalyst
  - cmmmech:spent-potlining
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:spent-tantalum-capacitors
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  - cmmmech:spent-zinc-manganese-button-cell-batteries
  - cmmmech:tannery-sludge
  - cmmmech:tannery-wastewater
  - cmmmech:theisen-sludge
  - cmmmech:titanogypsum
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:tungsten-nickel-iron-alloy-scrap
  - cmmmech:tungsten-skarn-tailings
  - cmmmech:uranium-mine-tailings
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-multilayer-ceramic-capacitors
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:waste-x-ray-films
  - cmmmech:wood-ash
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-secondary-resource-cohort-audit
  summary: All 111 secondary_resource records pass LinkML structural, semantic, and
    canonical top-level key-order validation with 0 errors and 0 warnings.
- check_id: just-verify-history-secondary-resources
  name: just verify-history (secondary_resource cohort)
  status: passed
  required: true
  command: .venv/bin/cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:acid-mine-drainage
  - cmmmech:allanite-leachate
  - cmmmech:aluminium-salt-slag
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:basic-oxygen-furnace-steel-slag
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:battery-black-mass
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium-tanned-leather-shavings
  - cmmmech:chrysotile-asbestos-tailings
  - cmmmech:coal-beneficiation-waste
  - cmmmech:coal-fly-ash
  - cmmmech:coal-gasification-slag
  - cmmmech:coal-mine-drainage-treatment-solids
  - cmmmech:copper-anode-slime
  - cmmmech:copper-autoclave-slime
  - cmmmech:copper-flotation-tailings
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electrical-cable-recycling-residues
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electrolytic-manganese-residue
  - cmmmech:electroplating-bath-effluents
  - cmmmech:electroplating-sludge
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ferrochrome-slag
  - cmmmech:fish-bone-residues
  - cmmmech:flue-gas-desulfurization-wastewater
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron-ore-tailings
  - cmmmech:kaolin-mine-waste
  - cmmmech:lead-blast-furnace-slag
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:municipal-sewage-sludge
  - cmmmech:municipal-waste-incineration-ash
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-smelter-slag
  - cmmmech:oil-and-gas-produced-water
  - cmmmech:oil-sands-froth-treatment-tailings
  - cmmmech:petroleum-coke
  - cmmmech:petroleum-oily-sludge
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphogypsum
  - cmmmech:pig-manure
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:reverse-osmosis-concentrate
  - cmmmech:samarium-cobalt-magnet-scrap
  - cmmmech:secondary-aluminium-dross
  - cmmmech:sewage-sludge-incineration-ash
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-cerium-glass-polishing-slurry
  - cmmmech:spent-copper-zinc-alumina-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrocracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-iron-molybdate-oxidation-catalyst
  - cmmmech:spent-ito-targets
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-ndfeb-magnets
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-nickel-steam-reforming-catalyst
  - cmmmech:spent-platinum-petroleum-reforming-catalyst
  - cmmmech:spent-potlining
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:spent-tantalum-capacitors
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  - cmmmech:spent-zinc-manganese-button-cell-batteries
  - cmmmech:tannery-sludge
  - cmmmech:tannery-wastewater
  - cmmmech:theisen-sludge
  - cmmmech:titanogypsum
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:tungsten-nickel-iron-alloy-scrap
  - cmmmech:tungsten-skarn-tailings
  - cmmmech:uranium-mine-tailings
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-multilayer-ceramic-capacitors
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:waste-x-ray-films
  - cmmmech:wood-ash
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-secondary-resource-cohort-audit
  summary: All 111 secondary_resource records have intact append-only history sidecars
    and matching curation_history metadata.
assessments:
- assessment_id: assess-secondary-resource-mechanisms-and-graphs
  topic: Secondary-resource waste/tailings/slag/scrap mechanisms, causal graphs, and
    UniProtKB protein groundings
  area: evidence
  outcome: supported
  target_ids:
  - cmmmech:acid-mine-drainage
  - cmmmech:allanite-leachate
  - cmmmech:aluminium-salt-slag
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:basic-oxygen-furnace-steel-slag
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:battery-black-mass
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium-tanned-leather-shavings
  - cmmmech:chrysotile-asbestos-tailings
  - cmmmech:coal-beneficiation-waste
  - cmmmech:coal-fly-ash
  - cmmmech:coal-gasification-slag
  - cmmmech:coal-mine-drainage-treatment-solids
  - cmmmech:copper-anode-slime
  - cmmmech:copper-autoclave-slime
  - cmmmech:copper-flotation-tailings
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electrical-cable-recycling-residues
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electrolytic-manganese-residue
  - cmmmech:electroplating-bath-effluents
  - cmmmech:electroplating-sludge
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ferrochrome-slag
  - cmmmech:fish-bone-residues
  - cmmmech:flue-gas-desulfurization-wastewater
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron-ore-tailings
  - cmmmech:kaolin-mine-waste
  - cmmmech:lead-blast-furnace-slag
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:municipal-sewage-sludge
  - cmmmech:municipal-waste-incineration-ash
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-smelter-slag
  - cmmmech:oil-and-gas-produced-water
  - cmmmech:oil-sands-froth-treatment-tailings
  - cmmmech:petroleum-coke
  - cmmmech:petroleum-oily-sludge
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphogypsum
  - cmmmech:pig-manure
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:reverse-osmosis-concentrate
  - cmmmech:samarium-cobalt-magnet-scrap
  - cmmmech:secondary-aluminium-dross
  - cmmmech:sewage-sludge-incineration-ash
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-cerium-glass-polishing-slurry
  - cmmmech:spent-copper-zinc-alumina-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrocracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-iron-molybdate-oxidation-catalyst
  - cmmmech:spent-ito-targets
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-ndfeb-magnets
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-nickel-steam-reforming-catalyst
  - cmmmech:spent-platinum-petroleum-reforming-catalyst
  - cmmmech:spent-potlining
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:spent-tantalum-capacitors
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  - cmmmech:spent-zinc-manganese-button-cell-batteries
  - cmmmech:tannery-sludge
  - cmmmech:tannery-wastewater
  - cmmmech:theisen-sludge
  - cmmmech:titanogypsum
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:tungsten-nickel-iron-alloy-scrap
  - cmmmech:tungsten-skarn-tailings
  - cmmmech:uranium-mine-tailings
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-multilayer-ceramic-capacitors
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:waste-x-ray-films
  - cmmmech:wood-ash
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  evidence_ids:
  - ev-secondary-resource-cohort-audit
  - ev-traction-battery-lu2025
  summary: '108/111 secondary_resource records contain primary-source-backed mechanisms
    (107/111 with microbial: true mechanisms and 1/111, cmmmech:ferrochrome-slag,
    with an abiotic microbial: false mechanism hydrochloric_acid_magnesium_extraction;
    145 mechanisms total) and 37/111 contain grounded causal_graphs (40 graphs) and
    UniProtKB protein_examples across 25 unique accessions. In cmmmech:traction-battery-hydrometallurgical-residue,
    tth_hydrolase omits tetH from the parenthetical label and omits grounded consortium
    species/loci in description; in 14 single-species A. thiooxidans secondary_resource
    records, tth_hydrolase retains a pre-expansion singular label and omits paralog
    loci GCD22_14205 and GCD22_02315.'
findings:
- finding_id: cmmmech-cycle6-stage4-finding-0001
  issue_key: cmmmech.traction-battery-hydrometallurgical-residue.tth-hydrolase-consortium-label-and-description-omit-species-and-loci
  title: tth_hydrolase node in traction-battery-hydrometallurgical-residue.yaml omits
    tetH from parenthetical label and omits grounded consortium species and locus
    tags in description
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  evidence_ids:
  - ev-secondary-resource-cohort-audit
  - ev-traction-battery-lu2025
  description: In data/records/traction-battery-hydrometallurgical-residue.yaml (cmmmech:traction-battery-hydrometallurgical-residue),
    causal_graphs[0] (acidophile_culture_associated_leaching_graph) node tth_hydrolase
    (lines 496-500) is grounded to 4 consortium tetrathionate hydrolase protein_examples
    across 3 species (Acidithiobacillus ferrooxidans ATCC 23270 UniProtKB:B7J3C9 tth
    / AFE_0029, Acidithiobacillus thiooxidans ATCC 19377 UniProtKB:A0A5P9XPU3 tth
    / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315, and Acidithiobacillus
    caldus SM-1 UniProtKB:F9ZNI0 Atc_1595 / TetH), but retains label 'Tth / TetH tetrathionate
    hydrolase (consortium tth)' (omitting tetH from the parenthetical) and a generic
    description 'Periplasmic pyrroloquinoline-domain hydrolase disproportionating
    tetrathionate into sulfate and protons.' that omits all grounded consortium species
    and locus tags, whereas sibling node sqr_reductase (lines 318-322) explicitly
    lists all grounded consortium species and locus tags in its description.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
- finding_id: cmmmech-cycle6-stage4-finding-0002
  issue_key: cmmmech.thiooxidans-causal-graphs.tth-hydrolase-node-omits-paralog-loci
  title: 16 single-species Acidithiobacillus thiooxidans causal_graphs retain singular
    tth_hydrolase node label and omit grounded paralog loci (GCD22_14205, GCD22_02315)
    in description
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
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
  evidence_ids:
  - ev-secondary-resource-cohort-audit
  description: 'Across the 673-record corpus, 16 single-species Acidithiobacillus
    thiooxidans records (arsenic, automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust,
    copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge,
    gallium, gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders,
    spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst,
    spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst)
    whose tth_hydrolase causal-graph nodes were expanded in Cycle 5 Stage 3 (PR #872)
    to include both A. thiooxidans ATCC 19377 tetrathionate hydrolase paralogs (UniProtKB:A0A5P9XPU3
    tth / GCD22_14205 and UniProtKB:A0A5P9XS05 tth / GCD22_02315) still retain the
    pre-expansion singular label ''Tth tetrathionate hydrolase (tth)'' and generic
    description ''Periplasmic tetrathionate hydrolase disproportionating tetrathionate
    into thiosulfate, elemental sulfur, sulfate, and protons.'' without naming the
    two grounded paralog loci (GCD22_14205 and GCD22_02315), whereas sibling node
    sqr_reductase in all 16 graphs has label ''Sqr/Sqor sulfide-quinone reductase
    (sqr / sqor)'' and explicitly names ''(Sqr/Sqor; GCD22_02301 / GCD22_03207)''
    in its description, and the 8 Cycle 6 Stage 2 (PR #888, commit a9115e6c) single-species
    A. thiooxidans records (beverage-carton-hydropulping-reject, chromite-beneficiation-tailings,
    goethite, jarosite, nickel-laterite-ore, nickel, petroleum-coke, pharmaceutical-blister-packaging-waste)
    explicitly name ''(tth GCD22_14205; tth GCD22_02315)'' in tth_hydrolase.label
    and ''(tth GCD22_14205 and tth GCD22_02315)'' in tth_hydrolase.description. In
    this scope, 14 record(s) (automotive-wastewater-treatment-sludge, blast-furnace-cast-house-dust,
    copper-smelter-slag, discarded-led-lamps, electric-arc-furnace-dust, gaas-production-hydroxide-sludge,
    gold-mine-tailings, metallic-machining-burrs, nickel-based-superalloy-residue-powders,
    spent-alkaline-zinc-carbon-batteries, spent-automotive-three-way-catalyst, spent-hydrodesulfurization-catalyst,
    spent-selective-catalytic-reduction-catalyst, spent-sulfuric-acid-production-catalyst)
    exhibit this node label/description lag.'
  owner_paths:
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
actions:
- action_id: act-align-traction-battery-tth-hydrolase-consortium-label-and-description
  finding_ids:
  - cmmmech-cycle6-stage4-finding-0001
  target_ids:
  - cmmmech:traction-battery-hydrometallurgical-residue
  description: Update causal_graphs[0].nodes[1].label to 'Tth / TetH tetrathionate
    hydrolase (consortium tth / tetH)' and update causal_graphs[0].nodes[1].description
    in data/records/traction-battery-hydrometallurgical-residue.yaml to list the grounded
    consortium tetrathionate hydrolase loci across Acidithiobacillus ferrooxidans
    (tth / AFE_0029), A. thiooxidans (tth GCD22_14205 / GCD22_02315), and A. caldus
    (Atc_1595 / TetH) during Stage 5 grouped remediation with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/traction-battery-hydrometallurgical-residue.yaml
    role: maintained_record
  acceptance_checks:
  - causal_graphs[0].nodes[1].label in data/records/traction-battery-hydrometallurgical-residue.yaml
    includes '(consortium tth / tetH)'.
  - causal_graphs[0].nodes[1].description names the grounded consortium tetrathionate
    hydrolase species and locus tags (A. ferrooxidans tth / AFE_0029, A. thiooxidans
    tth GCD22_14205 / GCD22_02315, A. caldus Atc_1595 / TetH).
  - A matching EDIT history sidecar exists in history/records/traction-battery-hydrometallurgical-residue/
    and passes just check.
- action_id: act-align-thiooxidans-tth-hydrolase-paralog-loci-labels-and-descriptions
  finding_ids:
  - cmmmech-cycle6-stage4-finding-0002
  target_ids:
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:metallic-machining-burrs
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-sulfuric-acid-production-catalyst
  description: Update causal_graphs[0].nodes[1].label and causal_graphs[0].nodes[1].description
    in the affected single-species Acidithiobacillus thiooxidans records to explicitly
    name both grounded A. thiooxidans ATCC 19377 tetrathionate hydrolase paralog loci
    (tth GCD22_14205 and tth GCD22_02315) during Stage 5 grouped remediation with
    canonical history provenance.
  owner_paths:
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
  acceptance_checks:
  - All affected records name both grounded A. thiooxidans ATCC 19377 tetrathionate
    hydrolase paralog loci (GCD22_14205 and GCD22_02315) in causal_graphs[0].nodes[1].label
    and causal_graphs[0].nodes[1].description.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-secondary-resource-cohort-audit
  kind: validation
  reference: data/records/*.yaml (material_kind == 'secondary_resource')
  locator: 111 secondary_resource YAML files
  accessed_at: '2026-10-31T13:20:05Z'
  support: supports
  summary: Full programmatic and source-backed audit of all 111 secondary_resource
    records at commit fab0682688678750d7da4e5357dda11592d5fac3.
- evidence_id: ev-traction-battery-lu2025
  kind: primary_source
  reference: DOI:10.1039/D5RA07472J
  locator: Lu et al. 2025 RSC Advances 15:45979-45985, Sections 2.1-2.3 and SI Table
    S1
  accessed_at: '2026-10-31T13:20:05Z'
  support: supports
  summary: Lu et al. (2025) studied separate acid-leached nickel-line and cobalt-line
    traction-battery hydrometallurgical residues leached by five acidophilic cultures
    (Af, Lf, Tt, Ac, St) and consortia (MC40-25St, MC45-40AS), with tetrathionate
    hydrolase grounded across A. ferrooxidans (tth / AFE_0029), A. thiooxidans (tth
    GCD22_14205 / GCD22_02315), and A. caldus (Atc_1595 / TetH).
limitations:
- 'Three secondary_resource records currently lack curated mechanisms (and one additional
  record carries an abiotic mechanism only): cmmmech:oil-and-gas-produced-water, cmmmech:spent-vegetable-oil-hydrogenation-catalyst,
  and cmmmech:theisen-sludge are maintained secondary-resource records without mechanisms
  (and cmmmech:ferrochrome-slag currently carries only an abiotic microbial: false
  HCl leaching mechanism) awaiting primary experimental microbial bioleaching/recovery
  studies. (108/111 secondary_resource records carry mechanisms (107/111 microbial,
  1/111 abiotic); 3/111 document feedstock identity and composition only.)'
notes:
- Cohort covers 100% (111/111) of secondary_resource records in data/records/*.yaml
  at commit fab0682688678750d7da4e5357dda11592d5fac3.
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:acid-mine-drainage
  - cmmmech:allanite-leachate
  - cmmmech:aluminium-salt-slag
  - cmmmech:automotive-wastewater-treatment-sludge
  - cmmmech:basic-oxygen-furnace-steel-slag
  - cmmmech:basic-oxygen-furnace-steelmaking-dust
  - cmmmech:battery-black-mass
  - cmmmech:bauxite-residue
  - cmmmech:beverage-carton-hydropulping-reject
  - cmmmech:biogas-desulfurization-sulfur-residue
  - cmmmech:blast-furnace-cast-house-dust
  - cmmmech:boron-ore-concentration-tailings
  - cmmmech:cadmium-telluride-photovoltaic-module-scrap
  - cmmmech:cathode-ray-tube-glass
  - cmmmech:cemented-tungsten-carbide-scrap
  - cmmmech:chromite-beneficiation-tailings
  - cmmmech:chromite-ore-processing-residue
  - cmmmech:chromium-tanned-leather-shavings
  - cmmmech:chrysotile-asbestos-tailings
  - cmmmech:coal-beneficiation-waste
  - cmmmech:coal-fly-ash
  - cmmmech:coal-gasification-slag
  - cmmmech:coal-mine-drainage-treatment-solids
  - cmmmech:copper-anode-slime
  - cmmmech:copper-autoclave-slime
  - cmmmech:copper-flotation-tailings
  - cmmmech:copper-smelter-flue-dust
  - cmmmech:copper-smelter-slag
  - cmmmech:discarded-led-lamps
  - cmmmech:electric-arc-furnace-dust
  - cmmmech:electrical-cable-recycling-residues
  - cmmmech:electroformed-copper-silver-manufacturing-scrap
  - cmmmech:electrolytic-manganese-residue
  - cmmmech:electroplating-bath-effluents
  - cmmmech:electroplating-sludge
  - cmmmech:end-of-life-cigs-photovoltaic-modules
  - cmmmech:end-of-life-crystalline-silicon-photovoltaic-modules
  - cmmmech:ferrochrome-slag
  - cmmmech:fish-bone-residues
  - cmmmech:flue-gas-desulfurization-wastewater
  - cmmmech:fluorescent-lamp-phosphor
  - cmmmech:gaas-production-hydroxide-sludge
  - cmmmech:gold-mine-tailings
  - cmmmech:ground-waste-tire-rubber
  - cmmmech:heavy-fuel-oil-combustion-ash
  - cmmmech:ion-adsorption-rare-earth-leach-residue
  - cmmmech:iron-ore-tailings
  - cmmmech:kaolin-mine-waste
  - cmmmech:lead-blast-furnace-slag
  - cmmmech:metal-grinding-sludge
  - cmmmech:metallic-machining-burrs
  - cmmmech:municipal-sewage-sludge
  - cmmmech:municipal-waste-incineration-ash
  - cmmmech:nickel-based-superalloy-residue-powders
  - cmmmech:nickel-flotation-tailings
  - cmmmech:nickel-smelter-slag
  - cmmmech:oil-and-gas-produced-water
  - cmmmech:oil-sands-froth-treatment-tailings
  - cmmmech:petroleum-coke
  - cmmmech:petroleum-oily-sludge
  - cmmmech:pharmaceutical-blister-packaging-waste
  - cmmmech:phosphate-ore-tailings
  - cmmmech:phosphogypsum
  - cmmmech:pig-manure
  - cmmmech:ponded-coal-ash
  - cmmmech:poultry-bone-residues
  - cmmmech:pyrite-roasting-cinder
  - cmmmech:reverse-osmosis-concentrate
  - cmmmech:samarium-cobalt-magnet-scrap
  - cmmmech:secondary-aluminium-dross
  - cmmmech:sewage-sludge-incineration-ash
  - cmmmech:spent-alkaline-zinc-carbon-batteries
  - cmmmech:spent-automotive-three-way-catalyst
  - cmmmech:spent-cerium-glass-polishing-slurry
  - cmmmech:spent-copper-zinc-alumina-catalyst
  - cmmmech:spent-fluid-catalytic-cracking-catalyst
  - cmmmech:spent-hydrocracking-catalyst
  - cmmmech:spent-hydrodesulfurization-catalyst
  - cmmmech:spent-iron-molybdate-oxidation-catalyst
  - cmmmech:spent-ito-targets
  - cmmmech:spent-lead-acid-battery-electrolyte
  - cmmmech:spent-ndfeb-magnets
  - cmmmech:spent-nickel-cadmium-batteries
  - cmmmech:spent-nickel-metal-hydride-batteries
  - cmmmech:spent-nickel-steam-reforming-catalyst
  - cmmmech:spent-platinum-petroleum-reforming-catalyst
  - cmmmech:spent-potlining
  - cmmmech:spent-selective-catalytic-reduction-catalyst
  - cmmmech:spent-silver-oxide-zinc-button-cell-batteries
  - cmmmech:spent-steel-pickling-liquors
  - cmmmech:spent-sulfuric-acid-production-catalyst
  - cmmmech:spent-tantalum-capacitors
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  - cmmmech:spent-vegetable-oil-hydrogenation-catalyst
  - cmmmech:spent-zinc-manganese-button-cell-batteries
  - cmmmech:tannery-sludge
  - cmmmech:tannery-wastewater
  - cmmmech:theisen-sludge
  - cmmmech:titanogypsum
  - cmmmech:traction-battery-hydrometallurgical-residue
  - cmmmech:tungsten-nickel-iron-alloy-scrap
  - cmmmech:tungsten-skarn-tailings
  - cmmmech:uranium-mine-tailings
  - cmmmech:used-photographic-fixer-solutions
  - cmmmech:waste-liquid-crystal-display-panels
  - cmmmech:waste-multilayer-ceramic-capacitors
  - cmmmech:waste-printed-circuit-boards
  - cmmmech:waste-x-ray-films
  - cmmmech:wood-ash
  - cmmmech:zinc-leach-residue
  - cmmmech:zinc-purification-hot-filter-cake
  rationale: All 111 records in this cohort denote distinct, non-synonymous entities
    matching data/records/*.yaml where material_kind == 'secondary_resource' at fab0682688678750d7da4e5357dda11592d5fac3
    with no duplicate IDs, names, or external identifier collisions.
  evidence_ids:
  - ev-secondary-resource-cohort-audit
```
