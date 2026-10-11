# CMMMech

An evidence-backed knowledge base for **critical minerals and materials**, with
**microbial extraction, transformation, and recovery mechanisms** alongside
their wider resource and material context.

The knowledge base provides a LinkML schema, an offline strict validator,
tests, CI, and a growing reviewed corpus. Each record has a
timestamped scientific review; synthetic test fixtures remain separate.

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
| [Titanium metal](data/records/titanium-metal.yaml) | Commodity identity and explicitly dated designation | Distinct material form; no microbial mechanism is asserted |
| [Coking coal](data/records/coking-coal.yaml) | Mixed acidophile treatment of a coking-coal feed | Sterile controls and final acid washing complicate sulfur attribution; coking performance untested |
| [Graphite commodity family](data/records/graphite.yaml) | Natural and synthetic graphite commodity family | Distinct from the narrower natural-graphite record and from a certified battery grade |
| [Platinum-group commodities](data/records/platinum-group-commodities.yaml) | Six-member commodity family and Australian 2024 designation | No group-wide microbial mechanism or uniform product specification |
| [Rare-earth-element commodities, Australian list scope](data/records/rare-earth-element-commodities.yaml) | Engineered bacterial lanmodulin separates synthetic Nd/Dy ions | Cell-free pair separation; reported yield uses tabulated eluate, not a verified whole-feed mass balance |
| [Heavy rare-earth commodities, EU assessment convention](data/records/heavy-rare-earth-elements.yaml) | Heavy rare-earth commodity grouping under the named EU convention | Membership conventions differ; no group-wide microbial mechanism |
| [Light rare-earth commodities, EU assessment convention](data/records/light-rare-earth-elements.yaml) | Light rare-earth commodity grouping under the named EU convention | Distinct from individual elements, host minerals and other REE groupings |
| [Rare-earth materials for permanent magnets, EU list scope](data/records/rare-earth-permanent-magnet-materials.yaml) | Seven-element end-use grouping in original EU 2024 Annex I | Raw materials for permanent magnets; no finished-magnet or grade-qualified recovery claim |

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
[remaining ingest priorities](research/ingests/round12-frontier-20261011.md), and
[current structured record reviews](reviews/structured/).
Earlier [Markdown reviews](reviews/records/) remain historical evidence.

The U/V mechanisms include eight reviewed, source-linked concentration cells.
The [observation contract](docs/records.md#quantitative-source-observations)
keeps measured values, detection limits, sample dates and analysis dates distinct.

## Scope

- Distinguish elements, mineral species, mineral groups, commodities, and
  secondary resources rather than treating those as synonyms.
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
