# CMMMech

An evidence-backed knowledge base for **critical minerals and materials**, with
**microbial extraction, transformation, and recovery mechanisms** alongside
their wider resource and material context.

The knowledge base provides a LinkML schema, an offline strict validator,
tests, CI, and a growing reviewed corpus. Each record has a
timestamped scientific review; synthetic test fixtures remain separate.

The catalogue currently contains 231 material records.

| Material record | Curated evidence | Evidence boundary |
|---|---|---|
| [Cobalt](data/records/cobalt.yaml) | Acidophilic consortium bioleaching of spent-battery black mass | Laboratory solubilization, not isolated cobalt product |
| [Neodymium](data/records/neodymium.yaml) | Algal biosorption and *Gluconobacter* biolixiviant bioleaching | Separate magnet-leachate and synthetic mixed-phosphate experiments |
| [Palladium](data/records/palladium.yaml) | Resting *Desulfovibrio desulfuricans* cells reduce Pd(II) | Defined soluble salt assay; hydrogenase causality remains inferred |
| [Manganese](data/records/manganese.yaml) | *Pseudomonas putida* GB-1 oxidation of Mn substrates | Laboratory oxide-equivalent assay, without crystalline phase identification |
| [Lithium](data/records/lithium.yaml) | Conditional acidophile bioleaching of jadarite-bearing material | Transient advantage; controls converge and other feeds show null effects |
| [Uranium](data/records/uranium.yaml) | Laboratory bioelectrochemical observations | Inoculated-cell observations do not isolate microbial enhancement |
| [Vanadium](data/records/vanadium.yaml) | Laboratory bioelectrochemical observations | Inoculated-cell observations do not establish a purified product |
| [Copper](data/records/copper.yaml) | Defined acidophile cultures leach chalcopyrite concentrate | Consortium-dependent release assay includes dissolved and precipitated copper |
| [Nickel](data/records/nickel.yaml) | *Acidithiobacillus thiooxidans* mixture leaches selected laterites | Matched-pH controls and ore-dependent null outcomes limit generalization |
| [Tellurium](data/records/tellurium.yaml) | Resting *Rhodococcus aetherivorans* BCP1 transforms tellurite to nanorods | Partial high-dose depletion and phase evidence do not establish isolated yield |
| [Zinc](data/records/zinc.yaml) | Controlled *Acidithiobacillus ferrooxidans* FC1 sphalerite leaching | Matched-chemistry null results and source figure/text tension limit generalization |
| [Silver](data/records/silver.yaml) | *Shewanella oneidensis* MR-1 forms XRD-identified Ag(0) | Abiotic salt precipitation, feed ambiguity and toxicity constrain the laboratory result |
| [Gallium](data/records/gallium.yaml) | *Acidithiobacillus thiooxidans* sludge leaching | Acid dissolution dominates; microbial enhancement remains provisional |
| [Arsenic](data/records/arsenic.yaml) | Co-mobilization in the same gallium-sludge experiment | Similar abiotic leaching; no demonstrated arsenic redox reaction or microbial advantage |
| [Cadmium](data/records/cadmium.yaml) | Cd-1 culture-associated cadmium-sulfide formation | Spectroscopy and sulfide assay support immobilization, without a matched cell-free comparison or isolated yield |
| [Chromium](data/records/chromium.yaml) | MR-1 MtrC/OmcA contribution to chromate transformation | Residual mutant activity, inferred precipitate valence and incomplete conversion remain explicit |
| [Platinum](data/records/platinum.yaml) | Hydrogen-driven transformation with CH34 biomass | Equivalent chemical-control removal prevents claiming microbial necessity |
| [Selenium](data/records/selenium.yaml) | Non-growing MR-1 selenite transformation | Conditional mutant involvement and different localization reports limit universal pathway claims |
| [Spent lamp phosphor](data/records/fluorescent-lamp-phosphor.yaml) | *Gluconobacter* biolixiviant bioleaching of a secondary resource | Retorted mixed powder; total-REE outcome, not an element-specific yield |
| [Cobaltite](data/records/cobaltite.yaml) | IMA September 2026 mineral identity | Distinct from cobalt; no inherited criticality or microbial mechanism |
| [Monazite-(Nd)](data/records/monazite-nd.yaml) | IMA September 2026 mineral identity | Distinct from neodymium and synthetic mixed experimental feeds |
| [Antimony](data/records/antimony.yaml) | Sulfate-reducing sediment-community transformation | Strong abiotic sorption and indirect sulfide chemistry limit microbial and phase attribution |
| [Phosphorus](data/records/phosphorus.yaml) | Fungal phosphate mobilization from struvite-bearing feed | Mixed mineral feed and background medium phosphate prevent a mineral-specific recovery yield |
| [Cerium](data/records/cerium.yaml) | Precipitation using pretreated fungal culture filtrate | Cell-free Ce stage requires resin and pH treatment; solution removal is not pure-metal yield |
| [Chalcopyrite](data/records/chalcopyrite.yaml) | Acidophile leaching of a chalcopyrite concentrate | Mineral species remains distinct from the impure experimental feed and copper element |
| [Sphalerite](data/records/sphalerite.yaml) | Controlled leaching of iron-bearing sphalerite | Chemistry-matched null results limit claims of universal microbial enhancement |
| [GaAs-production hydroxide sludge](data/records/gaas-production-hydroxide-sludge.yaml) | Acidophile leaching of a characterized secondary resource | Acid dissolution dominates; higher-loading arsenic counterevidence remains explicit |
| [Iron](data/records/iron.yaml) | Thermophilic Ax17 reduction of ferrihydrite to magnetite-rich material | Mixed phases and minor abiotic magnetite prevent an exclusive microbial product claim |
| [Germanium](data/records/germanium.yaml) | Catechol-associated accumulation by *Pseudomonas putida* ATCC 33015 | Low solution depletion and provisional transport interpretation; companion assays remain distinct |
| [Lanthanum](data/records/lanthanum.yaml) | Lanthanum oxalate precipitation using fungal culture supernatant | Cell-free reaction and subsequent thermal processing are separate stages |
| [Dysprosium](data/records/dysprosium.yaml) | Dried brewer's yeast biosorption in a defined solution | Inactive biomass, source condition inconsistencies and limited analytical detail constrain the claim |
| [Magnesium](data/records/magnesium.yaml) | Fungal formation of magnesium oxalate from phosphate feeds | Struvite and synthetic dittmarite stay distinct; identified crystals are not an isolated metal yield |
| [Aluminium](data/records/aluminium.yaml) | Fungal mobilization from a characterized red-mud feed | Acid-only leaching under different conditions and unresolved host phases limit microbial attribution |
| [Indium](data/records/indium.yaml) | Prepared mixed microalgal biomass sorption from synthetic solutions | Iron competition, declining reuse and inaccessible supplementary controls remain explicit |
| [Molybdenum](data/records/molybdenum.yaml) | DRY1 culture-associated molybdenum-blue formation | Optical response, unresolved product chemistry and inconsistent source protocols limit quantitative claims |
| [Tungsten](data/records/tungsten.yaml) | Culture-enhanced release from impure scheelite concentrate | Abiotic release and unknown energy/phase mechanisms prevent a pure-product recovery claim |
| [Europium](data/records/europium.yaml) | Culture-associated europium depletion and particle observations | Non-axenic strain, unlike assay arms and conflicting source values limit causal and product claims |
| [Samarium](data/records/samarium.yaml) | Cyanobacterial culture-associated solution depletion | Unspecified abiotic controls and inconsistent percentage wording limit causal and quantitative claims |
| [Terbium](data/records/terbium.yaml) | Screening with lyophilized *Synechococcus elongatus* UTEX 2973 | Cerium-only mechanistic follow-ups do not establish terbium kinetics or binding chemistry |
| [Holmium](data/records/holmium.yaml) | Element measured in a harvested cyanobacterial fraction | Alkaline medium and unresolved abiotic retention prevent an intracellular-uptake claim |
| [Erbium](data/records/erbium.yaml) | Element measured in a harvested cyanobacterial fraction | Earlier contrasting growth results and different protocols limit generalization |
| [Gadolinium](data/records/gadolinium.yaml) | Element measured in a harvested cyanobacterial fraction | Source graph/text and biochemical discrepancies remain unresolved |
| [Yttrium](data/records/yttrium.yaml) | Yttrium associated with washed ACUF 427 algal biomass | Taxonomic revision, mixture effects and unresolved localization constrain the interpretation |
| [Ytterbium](data/records/ytterbium.yaml) | Culture-associated solution depletion with *Penidiella* T9 | Dysprosium-specific microscopy and capacity do not establish the ytterbium mechanism |
| [Scandium](data/records/scandium.yaml) | Immobilized bacterial lanmodulin capture and malonate elution | Cell-free synthetic-feed separation; source feed discrepancies and limited replication remain explicit |
| [Praseodymium](data/records/praseodymium.yaml) | Immobilized Melba-LanM separates Pr from La in a binary feed | Fraction-based yield and lower repeat performance limit the best single-run result |
| [Lead](data/records/lead.yaml) | *Pseudomonas putida* enhances Pb release from synthetic pyromorphite | Nutrient and pH conditions affect remobilization; no isolated-metal recovery is shown |
| [Bismuth](data/records/bismuth.yaml) | *Fusarium* BI accumulates Bi in phosphorus-rich granules | Soluble-pool depletion does not establish whole-feed recovery, mineral identity or Bi reduction |
| [Cesium](data/records/cesium.yaml) | Cs retained by washed *Bifidobacterium adolescentis* JCM 1275 biomass | Sequential Sr exposure reduces retention; binding chemistry and practical recovery remain unresolved |
| [Strontium](data/records/strontium.yaml) | TK2d culture-associated Sr removal into carbonate-rich material | Salinity dependence, mixed spectral fits and unmatched chemical controls limit generalization |
| [Ruthenium](data/records/ruthenium.yaml) | Oxidized Ru deposits associated with *Bacillus* NCIMB 12555 biomass | Spectral disagreements and missing matched controls prevent claims of Ru(0) or microbial necessity |
| [Rhodium](data/records/rhodium.yaml) | Resting *Geobacter sulfurreducens* forms Rh-bearing nanoparticles | Single-metal and Pd/Rh experiments have different controls; depletion is not purified-metal yield |
| [Silicon](data/records/silicon.yaml) | Joint SIT1/SIT2 knockdown conditionally changes diatom silicon utilization | Uptake and silica-tracer assays differ; no metallic-silicon recovery is shown |
| [Tin](data/records/tin.yaml) | C22-inoculated sediment shows organotin debutylation | Unresolved taxonomy, pooled sampling and calibration limits constrain causal and quantitative claims |
| [Boron](data/records/boron.yaml) | Boron-bearing accretions associated with two *Streptomyces* cultures | Missing matched precipitation controls and uncertain phase/measurement interpretation limit attribution |
| [Fluorine](data/records/fluorine.yaml) | Engineered *Pseudomonas putida* transforms selected fluorinated model acids | Enantiomer specificity leaves a substantial residual fraction; no universal PFAS treatment or fluorine recovery claim |
| [Niobium](data/records/niobium.yaml) | Laboratory leaching of niobium-bearing waste-incineration ashes | Substrate and loading effects, null results and incomplete controls limit microbial attribution |
| [Tantalum](data/records/tantalum.yaml) | Condition-specific unsuccessful acidophile leaching of capacitor material | Tantalum non-detection is preserved without treating it as a measured zero or universal impossibility |
| [Titanium](data/records/titanium.yaml) | *Shewanella algae* alters the titanium oxide passive film | Spectral and protocol limits remain explicit; corrosion is distinct from recovered titanium product |
| [Zirconium](data/records/zirconium.yaml) | HC1 culture-associated preparation followed by calcination | Missing control outcomes and mixed phase evidence prevent claims of microbial necessity or pure zirconia |
| [Natural graphite](data/records/natural-graphite.yaml) | Commodity identity and BGS/CMIC 2024 assessment designation | Natural origin does not establish battery grade; no microbial mechanism is asserted |
| [Beryllium](data/records/beryllium.yaml) | Element identity and US 2025 designation | Primary removal leads remain deferred until full methods and controls are verified |
| [Hafnium](data/records/hafnium.yaml) | Purified bacterial ferric binding protein retains Hf(IV) clusters | Cell-free binding and crystallography do not establish whole-cell uptake or elemental-metal recovery |
| [Helium](data/records/helium.yaml) | Element identity and original EU 2024 designation | Tracer, plasma and analytical use do not establish microbial helium recovery |
| [Iridium](data/records/iridium.yaml) | Lyophilized algal biomass adsorption and acid desorption | Current strain taxonomy, assay differences and source inconsistencies constrain interpretation |
| [Lutetium](data/records/lutetium.yaml) | Washed Bacillus subtilis ATCC 7003 biomass depletes Lu from a mixed solution | Control-relative depletion does not resolve localization or recovered product mass balance |
| [Osmium](data/records/osmium.yaml) | Historical bacterial cell extracts couple hydrogen consumption to Os substrates | Stoichiometrically inferred products lack Os-specific phase and matched-control confirmation |
| [Promethium](data/records/promethium.yaml) | Element identity and explicit Australian 2024 rare-earth group mapping | Historical radiotracer evidence remains deferred pending carrier, background and figure checks |
| [Rhenium](data/records/rhenium.yaml) | Dried brewer's yeast retains Re from synthetic perrhenate feeds | Fraction-specific analysis and source inconsistencies limit mass-balance and redox claims |
| [Rubidium](data/records/rubidium.yaml) | Conditional light-dependent tracer uptake by prepared phototrophic cells | Buffer, ionophore and no-uptake comparisons limit native-transport and recovery claims |
| [Thulium](data/records/thulium.yaml) | Prepared Bacillus powders adsorb Tm with a conditional LTA-mutant comparison | Residual mutant adsorption and limited elution reporting prevent exclusive-mechanism or whole-feed-yield claims |
| [Alumina](data/records/alumina.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Bauxite](data/records/bauxite.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [High-purity alumina](data/records/high-purity-alumina.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [High-purity iron ore](data/records/high-purity-iron-ore.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Borates](data/records/borates.yaml) | Colemanite-bearing ore leaching during fungal culture | Source composition and protocol conflicts, missing abiotic boron series and no isolated-product yield |
| [Baryte commodity](data/records/baryte.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Fluorspar](data/records/fluorspar.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Feldspar commodity](data/records/feldspar.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Magnesite commodity](data/records/magnesite.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Phosphate rock](data/records/phosphate-rock.yaml) | Fungal solubilization of Araxá phosphate rock with fluoride inhibition | Culture arms and missing acid-matched comparisons constrain causal attribution |
| [Potash](data/records/potash.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Sodium compounds](data/records/sodium-compounds.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Magnesium metal](data/records/magnesium-metal.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Silicon metal](data/records/silicon-metal.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Titanium metal](data/records/titanium-metal.yaml) | Dated commodity designation and culture-containing grinding study | Pooled feed outcomes and mixed compounds; no pure-metal yield or demonstrated microbial advantage |
| [Coking coal](data/records/coking-coal.yaml) | Mixed acidophile treatment of a coking-coal feed | Sterile controls and final acid washing complicate sulfur attribution; coking performance untested |
| [Graphite commodity family](data/records/graphite.yaml) | Natural and synthetic graphite commodity family | Distinct from the narrower natural-graphite record and from a certified battery grade |
| [Platinum-group commodities](data/records/platinum-group-commodities.yaml) | Six-member commodity family and Australian 2024 designation | No group-wide microbial mechanism or uniform product specification |
| [Rare-earth-element commodities, Australian list scope](data/records/rare-earth-element-commodities.yaml) | Engineered bacterial lanmodulin separates synthetic Nd/Dy ions | Cell-free pair separation; reported yield uses tabulated eluate, not a verified whole-feed mass balance |
| [Heavy rare-earth commodities, EU assessment convention](data/records/heavy-rare-earth-elements.yaml) | Heavy rare-earth commodity grouping under the named EU convention | Membership conventions differ; no group-wide microbial mechanism |
| [Light rare-earth commodities, EU assessment convention](data/records/light-rare-earth-elements.yaml) | Light rare-earth commodity grouping under the named EU convention | Distinct from individual elements, host minerals and other REE groupings |
| [Rare-earth materials for permanent magnets, EU list scope](data/records/rare-earth-permanent-magnet-materials.yaml) | Seven-element end-use grouping in original EU 2024 Annex I | Raw materials for permanent magnets; no finished-magnet or grade-qualified recovery claim |
| [Pentlandite](data/records/pentlandite.yaml) | Culture-associated nickel release under controlled pH | Mixed mineral feed; different-duration runs are not replicated common endpoints |
| [Jadarite](data/records/jadarite.yaml) | Transient lithium release from jadarite-bearing material | Mixed phases, unmatched acid additions and eventual control convergence |
| [Spodumene](data/records/spodumene.yaml) | Negative acidophile result in a spodumene-bearing feed | No general impossibility claim; source data and loading ambiguities remain |
| [Colemanite](data/records/colemanite.yaml) | Fungal leaching of a colemanite-bearing ore | Reported composition does not close; no verified recovery denominator |
| [Spent lithium-ion battery black mass](data/records/battery-black-mass.yaml) | Adapted acidophile leaching of mixed NMC battery powder | Unmatched chemistry and inconsistent source inventories prevent a complete-recovery claim |
| [Bauxite residue (red mud)](data/records/bauxite-residue.yaml) | Fungal aluminium mobilization from an Ajka residue | Chemical controls use different conditions; aluminium host phases remain unresolved |
| [Phosphogypsum](data/records/phosphogypsum.yaml) | Separate synthetic-feed and actual-residue Gluconobacter assays | Model powders do not establish industrial-feed yields; actual-residue source quantities conflict |
| [Metallurgical coal commodity family](data/records/metallurgical-coal.yaml) | Source-defined coking, blending and injection-coal family | Explicit overlap with coking coal; authority definitions differ |
| [Scheelite](data/records/scheelite.yaml) | Culture-associated W release from scheelite concentrate | Mixed feed and unresolved energy source; not pure-mineral yield |
| [Pyromorphite](data/records/pyromorphite.yaml) | Pseudomonas-associated Pb remobilization from synthetic pyromorphite | Phosphate conditions matter; no unique pathway or field-recovery claim |
| [Struvite](data/records/struvite.yaml) | Fungal acidification and phosphate mobilization | Mixed water-treatment feed; oxalate-specific causality unresolved |
| [Ferrihydrite](data/records/ferrihydrite.yaml) | Ax17 reduction of synthetic two-line ferrihydrite | Assay analogue is not proof of ideal mineral formula or purity |
| [Magnetite](data/records/magnetite.yaml) | Magnetite-rich product from Ax17 ferrihydrite reduction | Mixed, probably cation-deficient product; same study as ferrihydrite and iron |
| [Pyrolusite](data/records/pyrolusite.yaml) | Abiotic Fe(II)-driven beta-MnO2 transformation | Explicitly nonmicrobial chemical alternative; microbial ore lead deferred |
| [Lithium carbonate commodity](data/records/lithium-carbonate.yaml) | Manufactured Li2CO3 product family | Supplier grades do not define a universal battery qualification |
| [Lithium hydroxide monohydrate commodity](data/records/lithium-hydroxide-monohydrate.yaml) | Manufactured LiOH.H2O product family | LiOH assay basis differs from monohydrate purity |
| [Nickel sulfate hexahydrate commodity](data/records/nickel-sulfate-hexahydrate.yaml) | Manufactured NiSO4.6H2O product family | Supplier nickel-content limits and uses remain product-specific |
| [Manganese sulfate monohydrate commodity](data/records/manganese-sulfate-monohydrate.yaml) | Manufactured MnSO4.H2O product family | Agricultural and battery-related uses do not establish universal grade |
| [Ferroboron commodity](data/records/ferroboron.yaml) | Iron-boron master-alloy commodity family | Variable grades; not elemental boron or one FeB stoichiometry |
| [Graphite anode material for lithium-ion batteries](data/records/graphite-anode-material.yaml) | Graphite products for lithium-ion negative electrodes | End-use subset of graphite; not all battery-grade graphite or complete electrodes |
| [Spent fluid catalytic cracking catalyst](data/records/spent-fluid-catalytic-cracking-catalyst.yaml) | Gluconobacter supernatant leaching of one FCC feed | Total-REE inventory endpoint; unequal culture temperatures and acidity constrain comparisons |
| [Coal fly ash](data/records/coal-fly-ash.yaml) | Yeast-supernatant treatment of coal fly ash | Residual-solid inventory loss, not measured recovered-liquid yield |
| [Municipal-waste incineration ash](data/records/municipal-waste-incineration-ash.yaml) | Sludge-culture-associated metal release from ash A | Undefined controls and analytical fraction; no universal recovery yield |
| [Sewage-sludge incineration ash](data/records/sewage-sludge-incineration-ash.yaml) | Condition-dependent metal release from ash B | Lower Nb and control-near In outcomes remain distinct from ash A |
| [Spent hydrocracking catalyst](data/records/spent-hydrocracking-catalyst.yaml) | Pretreated fungal-filtrate metal mobilization | Source pH, loading and control contradictions remain unresolved |
| [Spent NdFeB permanent magnets](data/records/spent-ndfeb-magnets.yaml) | Inactive algal biosorption from prepared magnet leachate | Roasting and acid leaching precede sorption; measured uptake differs from fitted capacity |
| [Dittmarite](data/records/dittmarite.yaml) | Fungal transformation of an XRD-identified synthetic phosphate feed | Source calls the feed struvite; monohydrate identity and no recovery yield remain explicit |
| [Glushinskite](data/records/glushinskite.yaml) | Fungal magnesium oxalate dihydrate formation | Same experiment as dittmarite and magnesium; mixed product is not a pure-phase yield |
| [Lithium-bearing geothermal brine](data/records/lithium-bearing-geothermal-brine.yaml) | Ureolytic carbonate precipitation during brine pretreatment | Natural primary resource; aqueous lithium retention is not isolated lithium recovery |
| [Forsterite](data/records/forsterite.yaml) | Fungal culture-associated dissolution and magnesium oxalate formation | Chemical oxalate also dissolves the feed; solution magnesium is not a recovery yield |
| [Talc](data/records/talc.yaml) | Low magnesium release in the same fungal comparison | No secondary mineral recovered in that assay; no matched abiotic talc trajectory |
| [Lizardite](data/records/lizardite.yaml) | C4-10 culture-associated magnesium and silicon release | Acidification and gene correlations do not establish gene necessity or isolated recovery |
| [Vivianite](data/records/vivianite.yaml) | Culture-associated precipitation from a defined Fe(II) medium | Dominant phase in a mixed product; no demonstrated Fe(III) reduction or pure-product yield |
| [Siderite](data/records/siderite.yaml) | Co-occurring carbonate in the same culture experiment | Separate mineral identity, shared experiment and unquantified phase abundance |
| [Oil and gas produced water](data/records/oil-and-gas-produced-water.yaml) | USGS production-stream identity and resource context | Identity-only secondary resource; microbial treatment evidence remains deferred |
| [Enstatite](data/records/enstatite.yaml) | Bacterial treatment of an olivine/enstatite mixed feed | Modelled phase dissolution differs between culture and cell-free arms; no pure-enstatite assay |
| [Olivine group](data/records/olivine-group.yaml) | Bacterial culture and filtered-biolixiviant comparisons | Natural group feeds remain distinct from pure forsterite; mixed solids and denominator conflicts constrain yields |
| [Biotite mica series](data/records/biotite.yaml) | C4-10 culture-associated iron and silicon mobilization | Unresolved member species, unmatched acidity and expression correlations limit causal claims |
| [Reverse osmosis concentrate](data/records/reverse-osmosis-concentrate.yaml) | Sludge-associated precipitation in river-derived concentrate | Control limitations and tentative solid phases; downstream recovery is a separate process |
| [Dunite](data/records/dunite.yaml) | Bacterial biolixiviant leaching of variably altered rock feeds | Acid-matched and cell-free nulls; modeled carbon demand is not measured net sequestration |
| [Hematite](data/records/hematite.yaml) | Priestia culture assays with a hematite-labelled feed | Bulk oxide composition does not establish phase purity or a pure-mineral release yield |
| [Potassium feldspar](data/records/potassium-feldspar.yaml) | Priestia culture assays with a potassium-feldspar-labelled feed | Informal mineral family; no particular member species or causal gene mechanism assigned |
| [Spent hydrodesulfurization catalyst](data/records/spent-hydrodesulfurization-catalyst.yaml) | Acidophile leaching of raw spent diesel-HDS catalyst | Chemical controls limit microbial advantage; dissolved metals are not isolated products |
| [Electrolytic manganese metal](data/records/electrolytic-manganese-metal.yaml) | Manufactured commodity identity and producer process descriptions | Conflicting grade specifications; no universal battery qualification or microbial production claim |
| [Electrolytic manganese dioxide](data/records/electrolytic-manganese-dioxide.yaml) | Manufactured commodity identity and application-specific product context | Distinct from natural mineral species; no inherited criticality or microbial production claim |
| [Manganese ore](data/records/manganese-ore.yaml) | Biogenic-iron leaching and a separate fungal transformation study of mixed Nkamouna laterite | Historical controls, incomplete transformation and figure/prose conflicts limit phase-specific and recovery claims |
| [Iron-ore tailings](data/records/iron-ore-tailings.yaml) | Anaerobic mixed-culture iron mobilization | Same linked experiment as manganese ore; no phase-specific flux or isolated iron recovery |
| [Electrolytic manganese residue](data/records/electrolytic-manganese-residue.yaml) | Fungal culture-associated manganese mobilization | Accession/strain contradiction and missing solid loading retained |
| [Automotive wastewater-treatment sludge](data/records/automotive-wastewater-treatment-sludge.yaml) | Two-stage biogenic-acid leaching | Loading and pH dependence; no isolated product or matched chemical-acid control |
| [Spent vegetable-oil hydrogenation catalyst](data/records/spent-vegetable-oil-hydrogenation-catalyst.yaml) | Process-defined spent-catalyst identity | Identity only; full experimental methods remain inaccessible |
| [Copper-flotation tailings](data/records/copper-flotation-tailings.yaml) | Indigenous-bacterial treatment for physical stabilization | Control activity and source inconsistencies retained; no metal recovery claimed |
| [Chrysotile-asbestos tailings](data/records/chrysotile-asbestos-tailings.yaml) | Acidophile-assisted magnesium leaching from mill tailings | Existing carbonates and control limits; no measured net carbon storage or asbestos detoxification |
| [Goethite](data/records/goethite.yaml) | Species-grounded acidophile iron-mobilization assays | Natural and synthetic feeds differ; acid confounding, null results and source contradictions retained |
| [Nickel laterite ore](data/records/nickel-laterite-ore.yaml) | Acidophile leaching and separate indigenous-community cobalt mobilization experiments | Ore-dependent nulls, different controls and unresolved source concentrations limit recovery comparisons |
| [Polymetallic nodules](data/records/polymetallic-nodules.yaml) | Enrichment leaching and Baltic microcosm growth/partitioning | Citrate and azide controls, local growth and distinct receiving fractions limit causal and recovery claims |
| [Waste printed circuit boards](data/records/waste-printed-circuit-boards.yaml) | Copper mobilization and separate biogenic ferric regeneration | Synthetic electrowinning, acid-washed residue and unlike controls prevent an actual-board closed-process yield |
| [Cobalt-rich ferromanganese crusts](data/records/cobalt-rich-ferromanganese-crusts.yaml) | Community-associated metal redistribution | Azide chemistry, solution partitioning and differing companion experiments limit causal and recovery claims |
| [Rare-earth-rich deep-sea mud](data/records/rare-earth-rich-deep-sea-mud.yaml) | Inferred microbial contribution to natural diagenesis | Modeled contribution and community associations do not establish extraction or taxon-specific causality |
| [Boron-ore concentration tailings](data/records/boron-ore-concentration-tailings.yaml) | Fungal culture-associated alkali-metal leaching | Unresolved strain, absent abiotic series and kinetic/source-overlap limits; no isolated product |
| [Seafloor massive sulfides](data/records/seafloor-massive-sulfides.yaml) | Thermophilic culture-associated Cu/Zn leaching of natural ore | Sterile comparisons, source inventory/unit conflicts and laboratory scale remain explicit |
| [End-of-life crystalline-silicon photovoltaic modules](data/records/end-of-life-crystalline-silicon-photovoltaic-modules.yaml) | Bioanode-powered silver-bearing cathode deposition from prepared module leachate | Chemical pretreatment, abiotic cathode, missing matched controls and ambiguous blank XRD limit recovery claims |
| [Waste liquid-crystal-display panels](data/records/waste-liquid-crystal-display-panels.yaml) | Mixed acidophile-associated indium/tin mobilization | Unlike pH trajectories, ambiguous replication and source percentage conflicts; no isolated product |
| [Spent automotive three-way catalyst](data/records/spent-automotive-three-way-catalyst.yaml) | Biogenic-acid aluminium-leaching pretreatment | Unlike media and unresolved Pt accounting prevent a measured PGM-recovery claim |
| [Spent sulfuric-acid-production catalyst](data/records/spent-sulfuric-acid-production-catalyst.yaml) | Culture-associated vanadium mobilization | Loading-dependent controls, conflicting source labels and residual leachability; no isolated product |
| [Copper-smelter slag](data/records/copper-smelter-slag.yaml) | Sulfur-oxidizer-associated copper mobilization | Slag-dependent outcomes, acidity and loading conflicts; no isolated product |
| [Coal-mine-drainage treatment solids](data/records/coal-mine-drainage-treatment-solids.yaml) | Isolate-associated REE mobilization | Site-specific sterile release, below-control outcomes and unresolved mass accounting |
| [Spent nickel-metal-hydride batteries](data/records/spent-nickel-metal-hydride-batteries.yaml) | Heterotrophic culture-metabolite leaching | Null treatments, different media and source yield/timing conflicts; no isolated product |
| [Blast-furnace cast-house dust](data/records/blast-furnace-cast-house-dust.yaml) | Sulfur-oxidizer-associated zinc mobilization in repeated reactor cycles | Carryover, unmatched controls and a supplementary value conflict limit cycle-specific yields |
| [Heavy-fuel-oil combustion ash](data/records/heavy-fuel-oil-combustion-ash.yaml) | Fungal spent-medium leaching | Undefined metal assay and unmatched controls; culture reactor scale differs from leaching scale |
| [Discarded LED lamps](data/records/discarded-led-lamps.yaml) | Biogenic-acid leaching of prepared lamp powder | Chemical comparator superiority for Nd and source normalization conflicts remain explicit |
| [Biogas-desulfurization sulfur residue](data/records/biogas-desulfurization-sulfur-residue.yaml) | Mixed-culture acid production from a sulfur-rich residue | Conflicting culture accession and incomplete sulfur balance; battery leaching is a separate downstream use |
| [Spent zinc-manganese button-cell batteries](data/records/spent-zinc-manganese-button-cell-batteries.yaml) | Culture-associated leaching after thermal pretreatment | Inhibited treatments, uncertain strain identity and unmatched chemistry limit generalization |
| [Electric-arc-furnace dust](data/records/electric-arc-furnace-dust.yaml) | Filtered culture-acid leaching followed by microbial electrolysis | Stage-specific depletion and deposit composition do not establish whole-feed recovery |
| [Basic-oxygen-furnace steel slag](data/records/basic-oxygen-furnace-steel-slag.yaml) | Separate UK and Austrian culture-leaching studies with chemical separation assays | Unmatched acidity, retained reactor inventory and synthetic precipitation feeds limit recovery claims |
| [Pharmaceutical blister packaging waste](data/records/pharmaceutical-blister-packaging-waste.yaml) | Culture-derived acid leaching of actual hospital waste | High-temperature null comparison, poor silver-fraction release and lower 1 L results retained |
| [Beverage-carton hydropulping reject](data/records/beverage-carton-hydropulping-reject.yaml) | Separate enzymatic pretreatment, culture-acid leaching and chemical precipitation | Comparable reagent acid, direct-culture limitations and unverified product purity remain explicit |
| [Basic-oxygen-furnace steelmaking dust](data/records/basic-oxygen-furnace-steelmaking-dust.yaml) | Acidophile-associated leaching with hybrid and column comparisons | Abiotic convergence, unlike pretreatments and unresolved inventory accounting; no isolated product |
| [Electroformed copper-silver manufacturing scrap](data/records/electroformed-copper-silver-manufacturing-scrap.yaml) | Culture-associated copper leaching and separate chemical/electrochemical recovery | Confounded operating conditions, pretreatment losses and local EDS do not establish whole-feed yield |
| [Metal grinding sludge](data/records/metal-grinding-sludge.yaml) | Culture-associated acid leaching of metalworking residue | Missing matched abiotic controls and residue mass prevent verified recovery yields |
| [Metalliferous black shale](data/records/metalliferous-black-shale.yaml) | Three separate culture-associated leaching studies | Pretreated-feed denominators, null comparisons and source figure/dose conflicts remain explicit |
| [Ground waste tire rubber](data/records/ground-waste-tire-rubber.yaml) | Partial microbial rubber transformation | Chemical pretreatment is separate; no demonstrated microbial zinc extraction |
| [Oxidized-zinc ore](data/records/oxidized-zinc-ore.yaml) | Culture-associated dissolution of a natural mixed ore | Missing numerical abiotic metal results, strain-name conflict and unreconciled yield accounting remain explicit |
| [Bastnaesite mineral family](data/records/bastnaesite.yaml) | Bacterial dissolution of a characterized natural mineral separate | Species identity is unresolved; contact effects, source-data conflicts and product recovery remain qualified |
| [Basaltic rock](data/records/basalt.yaml) | Culture-associated colonization and aqueous redistribution in six natural core specimens | Sterilization, uptake and varying conditions prevent a universal active-dissolution claim |
| [Chromite](data/records/chromite.yaml) | Nitrate-dependent oxidation of operationally acid-extractable Fe(II) | The reported percentage is not chromite conversion or chromium recovery |
| [Pyrrhotite](data/records/pyrrhotite.yaml) | Culture-associated oxidative weathering and secondary iron minerals | Normalized diffraction depletion is not a dissolved-iron or recovered-product yield |
| [Tungsten skarn tailings](data/records/tungsten-skarn-tailings.yaml) | Nonmicrobial laboratory physical separation and field-weathering context | Prepared-feed tungsten distributions are distinct from concentrate purity and microbial recovery |
| [Natural kaolin feed](data/records/kaolin.yaml) | Fungal culture-associated iron removal from mixed natural kaolin | Unlike control pH and incomplete mass accounting limit attribution and verified yield |
| [Kaolin mine waste](data/records/kaolin-mine-waste.yaml) | Limited bacterial iron leaching in EDTA-containing medium | Medium-only leaching and poor removal constrain biological and beneficiation claims |
| [Stibnite](data/records/stibnite.yaml) | Aerobic culture-associated antimony mobilization and oxidation | Loading conflict, abiotic chemistry and relative phases limit causal and recovery claims |
| [Bornite](data/records/bornite.yaml) | Culture-associated copper leaching and biofilm observations | Mixed specimens, source conflicts and apparatus differences limit mineral-specific yield and causality |
| [Arsenopyrite](data/records/arsenopyrite.yaml) | Culture-associated arsenic release and secondary-solid formation | Missing matched controls and incomplete mass accounting limit passivation and recovery claims |
| [Molybdenite](data/records/molybdenite.yaml) | Controlled limited-leaching observation and a separate concentrate comparison | Censored Mo and ambiguous residue percentages do not establish zero dissolution or extraction yield |
| [Chromite beneficiation tailings](data/records/chromite-beneficiation-tailings.yaml) | Separate bacterial and fungal treatment studies of mixed residues | Source unit conflicts, absent controls and incomplete percentage normalization remain explicit |
| [Pyrite](data/records/pyrite.yaml) | Methanogen growth on a natural specimen with separate synthetic-phase reduction assays | Mineral-access dependence does not resolve electron transfer, uptake or recovered-product yield |
| [Chalcocite](data/records/chalcocite.yaml) | Culture-associated leaching observations in mineral separates and mixtures | Feed composition, controls and an inconsistent extraction equation limit causal and yield claims |
| [Covellite](data/records/covellite.yaml) | Phase formation from mine drainage using biogenic sulfide | Separate chemical precipitation; inconsistent composition values cannot establish purity or recovery yield |
| [Galena](data/records/galena.yaml) | Culture-associated transformation of a galena-rich concentrate | Sulfate precipitation and source accounting limits prevent a dissolved-lead recovery claim |
| [Greigite](data/records/greigite.yaml) | Extracellular phase formation in two Thermococcales studies | Mixed assemblages, bulk detection limits and incomplete controls constrain causal and yield claims |
| [Mackinawite](data/records/mackinawite.yaml) | Sulfate-reducing cultures and inactive biomass influence crystal growth | Abiotic formation, unequal pretreatment and fitted domain sizes do not establish recovery yield |
| [Uraninite](data/records/uraninite.yaml) | MR-1 forms diffraction-identified UO2 nanoparticles | Genetic comparator limits and medium-dependent non-uraninite products prevent universal phase or field claims |
| [Anglesite](data/records/anglesite.yaml) | Culture-associated formation in a galena-concentrate residue | Anglesite also forms in the control; relative phase proportions are not recovery yields |
| [Jarosite](data/records/jarosite.yaml) | Sulfur-oxidizing cultures promote reduction and dissolution of K-jarosite | Sulfur substrates, pH and nonzero abiotic controls limit causal and quantitative comparisons |
| [Ningyoite](data/records/ningyoite.yaml) | U(IV)-phosphate formation in thermophilic cultures and a spore preparation | Species versus strain scope, mixed products and minority-phase detection remain explicit |
| [Schwertmannite](data/records/schwertmannite.yaml) | Resting iron-oxidizing cells form an iron oxyhydroxysulfate material | Matched oxidation controls and biomass perturbations constrain formation and adsorption claims |
| [Uramphite](data/records/uramphite.yaml) | Thermophilic culture transforms a precipitated ammonium uranyl-phosphate analogue | High-loading nulls, dissolved-pathway uncertainty and source discrepancies limit the reduction claim |
| [Moolooite](data/records/moolooite.yaml) | Fungal culture-associated copper oxalate formation on weathered ore surfaces | Variable hydration, mixed phases and missing matched controls prevent pure-product or exclusive biological claims |
| [Humboldtine](data/records/humboldtine.yaml) | Fungal culture-associated iron oxalate formation on siderite- and altered pyrrhotite-bearing rocks | Organism-specific nulls, method-dependent phase assignments and control gaps limit causal and recovery claims |
| [Lindbergite](data/records/lindbergite.yaml) | Fungal formation of source-assigned manganese oxalate dihydrate from natural nodules and synthetic sodium birnessite | Separate studies retain preparation, hydration, polymorph and control limits; no pure-product yield |
| [Falottaite](data/records/falottaite.yaml) | Fungal culture-associated manganese oxalate trihydrate assignment in a hausmannite/arsenate assay | Unresolved onset, mixed phases and absent matched abiotic controls prevent phase-specific recovery or arsenic-capacity claims |
| [Mimetite](data/records/mimetite.yaml) | Fungal transformation of an impure natural mimetite feed with lead oxalate precipitation | Qualitative phase evidence does not establish feed conversion, arsenic fate or recovered-metal yield |
| [Katsarosite](data/records/katsarosite.yaml) | Zinc-dominant monoclinic oxalate formation during source-identified A. niger culture | Mixed phases, conflicting source conditions and a companion-strain accession mismatch remain explicit |
| [Hausmannite](data/records/hausmannite.yaml) | Culture-associated manganese mobilization from synthetic hausmannite with and without selenate | Endpoint measurements, conflicting source units and unmatched abiotic controls limit causal and recovery claims |
| [Malachite](data/records/malachite.yaml) | Brown-rot cultures form source-assigned copper oxalate on synthetic malachite | Species-specific phase detection and missing matched controls prevent quantitative conversion claims |
| [Cerussite](data/records/cerussite.yaml) | Brown-rot cultures form lead oxalate on a natural cerussite specimen | Microscopy-only assignments and conflicting co-product wording remain explicit |
| [Fluorapatite](data/records/fluorapatite.yaml) | Brown-rot cultures form calcium oxalate on a chlorine-bearing fluorapatite specimen | Medium calcium and method-dependent phase detection prevent source-exclusive or phosphorus-recovery claims |
| [Hollandite](data/records/hollandite.yaml) | Brown-rot cultures form source-assigned manganese oxalate phases on a hollandite specimen | Formula and figure/table phase conflicts remain unresolved; no phase-specific recovery yield |
| [Birnessite](data/records/birnessite.yaml) | Separate synthetic-feed transformation, fungal-composite cobalt sorption and binary Co/Ni selectivity | Different strains, phase uncertainty and source capacity/redox conflicts; no isolated metal yield |
| [Todorokite](data/records/todorokite.yaml) | Dated IMA identity and geological occurrence | Variable composition; geological alteration does not make it an industrial secondary resource |
| [Kutnohorite](data/records/kutnohorite.yaml) | Dated IMA identity and natural compositional variation | Distinct carbonate species; no inherited criticality or microbial mechanism |
| [Cemented tungsten carbide scrap](data/records/cemented-tungsten-carbide-scrap.yaml) | Reported culture/ferric binder mobilization and separate chemical powder preparation | Missing matched controls and mass-balance denominators; no numerical extraction yield or WC purity |
| [Petalite](data/records/petalite.yaml) | Dated IMA species identity and Handbook geological context | No accepted microbial mechanism or inherited criticality |
| [Polylithionite](data/records/polylithionite.yaml) | Dated IMA identity and original mica nomenclature | Lepidolite series is not an exact endmember synonym; no accepted microbial mechanism |
| [Germanite](data/records/germanite.yaml) | Dated IMA identity and original crystal chemistry | Source space-group disagreement preserved; no accepted microbial mechanism |
| [Renierite](data/records/renierite.yaml) | Dated IMA identity and original composition study | Coupled composition variation within the species; no inherited criticality |
| [Lithium-mica ore](data/records/lithium-mica-ore.yaml) | Qualified microbial leaching observations on mixed mica-bearing feeds | Source denominator/protocol conflicts and distinct analytical fractions; no mineral-specific transfer |
| [Coal beneficiation waste](data/records/coal-beneficiation-waste.yaml) | Community-associated leaching and 2018 control/apparatus observations | Overlapping studies, inconsistent recipes and incomplete volume accounting; no complete product yield |
| [Tungsten-nickel-iron alloy scrap](data/records/tungsten-nickel-iron-alloy-scrap.yaml) | Ferric-assisted mechanical separation in a complete 2011 study | Proposed microbial regeneration is untested; purity and pressed-surface size claims remain qualified |
| [Argyrodite](data/records/argyrodite.yaml) | Dated IMA identity and natural Ezuri microscopy/microprobe context | Historical alburnite and synthetic lithium electrolytes remain distinct; no recovery claim |
| [Briartite](data/records/briartite.yaml) | Current IMA identity and original natural-mineral observations | Historical Fe/Zn scope and conflicting assay labels retained; zincobriartite is a separate species |
| [Theisen sludge](data/records/theisen-sludge.yaml) | Historical scrubber-residue identity and sampled-feed analytical context | Synthetic membrane feeds and reused bioleaching evidence remain separate; mechanism gap remains open |
| [Alburnite](data/records/alburnite.yaml) | Current IMA identity, original approval and qualified natural-occurrence evidence | Arsenic-bearing occurrence remains unresolved; unavailable full-description detail is deferred |
| [Cassiterite](data/records/cassiterite.yaml) | Laboratory electroflotation using prepared *Rhodococcus opacus* biomass | Post-cultivation sterilization and source condition conflicts; no matched zero-biomass flotation or isolated tin yield |
| [Laforêtite](data/records/laforetite.yaml) | Current IMA identity and original natural-inclusion chemistry and diffraction | Sparse natural sampling and multiphase synthetic comparator remain distinct; no microbial mechanism |
| [Roquesite](data/records/roquesite.yaml) | Current IMA identity and original natural-inclusion analyses | Natural material and synthetic CuInS2 references remain distinct; no extraction or recovery claim |
| [Zincobriartite](data/records/zincobriartite.yaml) | Current IMA identity and original approval announcement | Full description remains unpublished in the dated CNMNC notice; historical briartite is not automatically reassigned |
| [Dzhalindite](data/records/dzhalindite.yaml) | Dated IMA identity and original natural-occurrence microscopy and composition | Failed diffraction, unresolved iron speciation and tentative hypogene origin; no microbial mechanism |
| [Cassiterite-polymetallic sulfide ore](data/records/cassiterite-polymetallic-sulfide-ore.yaml) | Laboratory culture-associated sulfide alteration and iron mobilization in mixed geological ore | Inconsistent composition tables and iron-based proxy; no verified sulfur balance, recovered tin yield or industrial deployment |

Experimental salts, alloys, mineral species and secondary resources retain
their distinct identities. Criticality entries identify a jurisdiction and
edition; none assert timeless status or industrial process deployment. See the
[initial pilot assessment](docs/pilot-session.md),
[first ingest queue](research/ingests/20261009-priorities.md),
[earlier ingest results](research/ingests/20261009T054507Z-followup.md),
[expansion inventory and priorities](research/sources/expansion-authorities/20261011T040103Z.md),
[second expansion review](research/ingests/round2-20261011-publication.md),
[third expansion reviews](research/ingests/round3-20261011-publication.md),
[fourth expansion review and publication preparation](research/ingests/round4-20261011-publication.md),
[fifth expansion reviews](research/ingests/round5-20261011-publication.md),
[sixth expansion reviews](research/ingests/round6-20261011-publication.md),
[seventh expansion reviews](research/ingests/round7-20261011-publication.md),
[eighth expansion reviews](research/ingests/round8-20261011-publication.md),
[ninth expansion reviews](research/ingests/round9-20261011-publication.md),
[tenth expansion reviews](research/ingests/round10-20261011-publication.md),
[eleventh expansion reviews](research/ingests/round11-20261011-publication.md),
[twelfth expansion reviews](research/ingests/round12-20261011-publication.md),
[thirteenth expansion reviews](research/ingests/round13-20261011-publication.md),
[fourteenth expansion reviews](research/ingests/round14-20261011-publication.md),
[fifteenth expansion reviews](research/ingests/round15-20261011-publication.md),
[sixteenth expansion reviews](research/ingests/round16-20261011-publication.md),
[seventeenth expansion reviews](research/ingests/round17-20261011-publication.md),
[eighteenth expansion reviews](research/ingests/round18-20261011-publication.md),
[nineteenth expansion reviews](research/ingests/round19-20261011-publication.md),
[twentieth expansion reviews](research/ingests/round20-20261011-publication.md),
[twenty-first expansion reviews](research/ingests/round21-20261011-publication.md),
[twenty-second expansion reviews](research/ingests/round22-20261011-publication.md),
[twenty-third expansion reviews](research/ingests/round23-20261011-publication.md),
[twenty-fourth expansion reviews](research/ingests/round24-20261011-publication.md),
[twenty-fifth expansion reviews](research/ingests/round25-20261011-publication.md),
[twenty-sixth expansion reviews](research/ingests/round26-20261011-publication.md),
[twenty-seventh expansion reviews](research/ingests/round27-20261011-publication.md),
[twenty-eighth expansion reviews](research/ingests/round28-20261011-publication.md),
[twenty-ninth expansion reviews](research/ingests/round29-20261011-publication.md),
[thirtieth expansion reviews](research/ingests/round30-20261011-publication.md),
[thirty-first expansion reviews](research/ingests/round31-20261011-publication.md),
[thirty-second expansion reviews](research/ingests/round32-20261011-publication.md),
[thirty-third expansion reviews](research/ingests/round33-20261011-publication.md),
[thirty-fourth expansion reviews](research/ingests/round34-20261011-publication.md),
[thirty-fifth expansion reviews](research/ingests/round35-20261011-publication.md),
[thirty-sixth expansion reviews](research/ingests/round36-20261011-publication.md),
[thirty-seventh expansion reviews](research/ingests/round37-20261011-publication.md),
[thirty-eighth expansion reviews](research/ingests/round38-20261011-publication.md),
[thirty-ninth expansion reviews](research/ingests/round39-20261012-publication.md),
[fortieth expansion reviews](research/ingests/round40-20261012-publication.md),
[forty-first expansion reviews](research/ingests/round41-20261012-publication.md),
[forty-second expansion reviews](research/ingests/round42-20261012-publication.md),
[forty-third expansion reviews](research/ingests/round43-20261012-publication.md),
[forty-fourth expansion reviews](research/ingests/round44-20261012-publication.md),
[forty-fifth expansion reviews](research/ingests/round45-20261012-publication.md),
[forty-sixth expansion reviews](research/ingests/round46-20261012-publication.md),
[forty-seventh expansion reviews](research/ingests/round47-20261012-publication.md),
[remaining ingest priorities](research/ingests/round47-frontier-20261012.md), and
[current structured record reviews](reviews/structured/).
Earlier [Markdown reviews](reviews/records/) remain historical evidence.

The U/V mechanisms include eight reviewed, source-linked concentration cells.
The [observation contract](docs/records.md#quantitative-source-observations)
keeps measured values, detection limits, sample dates and analysis dates distinct.

## Scope

- Distinguish elements, mineral species, mineral groups, commodities, and
  primary and secondary resources rather than treating those as synonyms.
- Record criticality by jurisdiction, list name, and edition, with a source.
  There is no universal or timeless `is_critical` flag.
- Represent mechanisms such as bioleaching, biosorption, biomineralization,
  redox transformation, separation, recovery, and recycling.
- Mark microbial involvement explicitly; connect identified organisms and
  experimental context to evidence for the particular mechanism.
- Preserve uncertainty and evidence that supports, partially supports, or
  contradicts a mechanism. Validation is not scientific verification.

## Local Checks

```bash
uv sync --extra dev --locked
just check
uv run cmmmech validate
uv run cmmmech validate path/to/record.yaml
uv run cmmmech validate --require-records
```

The locked development dependencies include `just`; use `uv run just check`
if it is not otherwise on your PATH. CI runs `uv run python scripts/check.py`,
including the recipe argument-forwarding regressions. This local gate uses no
research provider, model, credential, or network
lookup after dependencies are installed. CI also runs the separate canonical
artifact check, which reads the pinned public CLAW revision:

```bash
bash scripts/check_vendored_sync.sh
```

Each record belongs in `data/records/<slug>.yaml`. See
[the record guide](docs/records.md) and the packaged
[LinkML schema](src/cmmmech/schema/cmmmech.yaml). Validation rejects unknown
fields, duplicate YAML keys, malformed references, dangling source references,
and duplicate record identifiers. An empty corpus is reported explicitly;
`--require-records` makes it an error. The shared local/CI gate now uses this
flag so accidental loss of the whole corpus fails `just check`.

Use [cmmmech-add-record](.claude/skills/cmmmech-add-record/SKILL.md) to turn
primary evidence or a source-discovery handoff into curated records, curation
history and saved scientific reviews.

Use the local [record-review skill](.claude/skills/review-record/SKILL.md) for
new or changed scientific records. Review artifacts identify the reviewed
commit and working changes, hash the record bytes, and retain unresolved limits.
New rounds use the [structured review contract](docs/record-reviews.md).
Before publishing through the squash queue, preserve the inspected source
revisions using the [publication procedure](docs/record-review-profile.md#publishing-through-the-squash-queue).

## Sources

Use the local [source-discovery skill](.claude/skills/cmmmech-discover-sources/SKILL.md)
to investigate CMM data sources, reassess known sources, or identify coverage gaps.
It produces a dated search log, source assessment and ranked curation handoff under
`research/sources/`, keeping discovery leads separate from verified evidence.

Criticality is a designation made by a named authority at a particular time.
Useful discovery sources include the [USGS critical-minerals programme](https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals)
and the [EU critical raw materials overview](https://www.consilium.europa.eu/en/policies/the-critical-raw-materials-act/).
These are entry points, not imported datasets or an endorsement of a frozen list.
Curate microbial mechanisms from the underlying research, preserving organism,
substrate, conditions, and the distinction between laboratory results and field
or industrial deployment.

## Integration Status

CLAW [fleet admission](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
registers CMMMech with its measured native capabilities. The 22 applicable
governed artifacts are pinned in `scripts/.vendored_canon_ref`; CI verifies
their bytes and file modes against that immutable public CLAW revision. Use
CLAW's supported synchronizer for updates, never hand-edit governed copies.

The native schema keeps inline `curation_history` events separate from
`history_refs`, which link canonical sidecar sessions. `just new-history` creates
a validated sidecar without rewriting a scientific record; attach its printed
path in a reviewed edit. Both canonical timestamp guards remain unchanged.
History paths reject symlinks, and CI compares committed sessions with the
trusted event base to prevent rewriting or deleting earlier provenance. See
[the history guide](docs/records.md#append-only-curation-history).

The native merge queue is configured for `main` through CLAW's reviewed
plan/apply/check process. Its [receipts and readiness evidence](reviews/integration/queue-20261008/)
distinguish configuration, writer App token readiness, and actual queue execution.
The PR shepherd remains manual and comment-only; its configuration and available
secret names were checked without invoking its model. Other unverified fleet
adapters remain disabled. No research provider is invoked by the native or
canonical-byte validation gates.

The included CI handles pull requests, pushes to `main`, and `merge_group`
events. Operational merge evidence is tracked in [issue #3](https://github.com/CultureBotAI/CMMMech/issues/3).
The [dated integration audit](docs/integration-status.md) records the earlier
pre-admission state, not the current deployment. Coordinated fleet convergence
is tracked in [CLAW issue #580](https://github.com/CultureBotAI/culturebotai-claw/issues/580).

## License

Project-authored code and schemas use BSD-3-Clause. Project-authored data and
narrative documentation use CC-BY-4.0. Third-party materials retain their own
terms. See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), and
[LICENSE-DATA](LICENSE-DATA).
