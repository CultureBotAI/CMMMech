# Coal-beneficiation waste: source investigation and author handoff

UTC: 2026-10-12T02:41:05Z

Reviewer role: Codex /root/round27_packaging, GPT-6, codex — source investigator and record author. This document is not an independent scientific acceptance review.

Worktree: `/private/tmp/CMMMech-expansion-round43-20261012`. Trusted base: `59e24ec38d9c7b377dcfeade1637b298aab9623e`.

## Decision and identity

Curated [coal-beneficiation-waste](../../../data/records/coal-beneficiation-waste.yaml) as a `secondary_resource`, with two separate qualified native-community leaching observations from complete 2012 and 2016 primary studies. The material is discarded gravity/flotation beneficiation material from the Lviv-Volyn coal basin and Chervonogradska concentrating works. It is not natural coal, combustion ash, mine-drainage treatment solids, germanium metal or an identified Ge mineral. Neither constituent criticality nor a mineral/taxon accession is inherited. The papers' native communities are insufficiently identified to assert species or strain IDs. Laboratory leach-liquor measurements do not demonstrate isolated products or industrial deployment.

The initially supplied 2019 electrochemical lead was fully acquired, but remains dossier-only context: possible bacteria are not measured biological activity. Its original primary evidence is useful, rather than inaccessible; its microbial causality is inadequate for a new mechanism.

## Search and duplicate boundary

The acquisition and duplicate search covered current round43 and original main `data/records`, `research`, `reviews` and `history`, including hidden and ignored entries and followed relevant symlinks. Cycle-aware path discovery read 3,324 textual metadata files and located 154 existing referenced raw directories. The exact commands, boundaries and all missing roots are retained in `dedup-receipt.json`; nine historical referenced roots were missing, so no machine-wide or unavailable-download absence claim is made. Searches used `rg --no-ignore --hidden --follow` over YAML/JSON/Markdown/text/HTML/XML/CSV/TSV, not arbitrary binary decoding. No unrelated home or temporary-tree scan established the scientific duplicate result.

Broad material/author/Ge searches found the existing germanium description and bibliography/raw leads, but no coal-beneficiation-waste owner in the searched corpus. Exact DOI/item/slug search also found the 2019 lead in round42 Theisen search receipts and the parallel round43 Ge identity dossier's reference to this planned owner. The 2019 source therefore is a known lead. Existing coal fly ash, mine-drainage treatment solids, coking coal and metallurgical coal owners were inspected and concern different material identities/assays. No curated 2012/2016 experiment duplicate was found within this bounded textual scope. The two accepted papers concern the same regional family and overlapping authors; unknown sample independence prevents treating them as independent replication.

Live searches used the web provider on 2026-10-12, without domain/recency filters or exhaustive pagination. Exact queries:

- `"08e30b59-49fe-4188-9cf7-141584c1b6b8"`
- `site:dspace.onu.edu.ua germanium coal dumps bioleaching`
- `"08e30b59" germanium`
- `"UTILIZATION" "coal beneficiation waste dumps" Blayda 2012`
- `"Бактериальное выщелачивание" "германия" "2012" Блайда`
- `"10.18524/2304-0947.2019.1(69).158498" correction erratum`
- `"10.18524/2307-4663.2016.3(35).77956" correction retraction`
- `"Блайда" "Комплексная оценка отходов углеобогащения" исправление`
- `"germanium" "Chervonogradska" leaching sterile control`

No paper-specific formal correction/retraction appeared in these bounded results. Fresh Crossref records for 2016 and 2019 have no `update-to` and empty relations; this is a metadata/search observation, not an exhaustive guarantee. Theisen #140 blocked routes were not retried.

## Acquisition, original graphics, version and reuse

Full source locators and file checksums are in the paired JSON. All 27 original primary pages were visually inspected: seven for Blayda2012 (Tables1–2, Figures1–3), fourteen for Vasyleva2016 (Table1, Figures1–4), six for Dzhambek2019 (Tables1–2, no figures). Text extraction supplemented, rather than substituted for, original-page inspection.

Initial institution UI/legacy PDF routes returned identical 724-byte HTML application shells (SHA256 `dcd13c0c07f3ae6c065aea780ea3f378d235b804a5a61cf8b884346f6401ca94`). The misleading `raw/blayda2012.pdf` and `raw/vasyleva2016.pdf`, their single-page renders/text and `rendered-pages.json` are retained failed-acquisition artifacts, not source evidence. Public DSpace item/bundle/ORIGINAL-bitstream metadata then supplied actual `%PDF` files named `*-primary.pdf`; `acquisition-1.json` through `acquisition-4.json` record URLs, UTC times, statuses, types, hashes and failures. No login or access restriction was bypassed.

The 2016 publisher PDF was additionally obtained. All fourteen page texts and rendered pixel bytes match the institution PDF despite different container hashes (`vasyleva2016-version-comparison.json`). Publisher metadata dates it 22 September2016, with CC BY-NC4.0 rights. The 2012 article is printed2012; no DOI is asserted. The 2019 article was published4 March2019; the institution's5 April2019 accession date does not create a new edition. Its publisher metadata was read through web search, but direct landing returned403 and PDF retrieval timed out; the actual full text came from the public institution bitstream. No complete publisher PDF access is claimed for2019. Source2012/2019 explicit redistribution licenses remain unverified; all bulk files remain outside Git.

No supplement pointer was found in the complete three articles or inspected original bundles; the2016 publisher page exposes one PDF and no supplement string/link, and2019's observed publisher metadata exposes its PDF. This is a bounded inspection, not a claim that unpublished data cannot exist. No separate reusable numerical dataset or data dictionary was acquired.

## Accepted study A: Blayda2012

The original Methods p39 describes0.5 L flasks at30.0±2.0°C, solid:liquid1:10, pHabout1.8 maintained **with**0.5mol/L sulfuric-acid reagent. That is reagent concentration, not a reported final slurry molarity. Native sulfur-oxidizing community material was treated with basal9K (solution1) or Fe(II), thiosulfate, thiourea or sulfur additions (solutions2–5). Addition doses, leaching duration, working volume, agitation, pretreatment, biological replicate number and culture accession are unspecified. The separate wheat assay lasts three days; that duration cannot be transferred to leaching.

Table1 gives selected waste Ge25.8mg/kg and Ga12.1mg/kg. Solid analysis used emission spectrometry; solution Ge used extraction-photometry as germanomolybdate with impurity separation, while other metals used atomic absorption. Table2 reports fractions transferred to solution: Ge99.9% for basal/Fe(II)/thiourea/sulfur and55.0% for thiosulfate; Ga99.9% for basal/Fe(II),90.5% for thiosulfate/thiourea,70.6% for sulfur. These are source-reported leaching fractions, not isolated-product yields. Basal Ge is already99.9%; additives do not show an advantage on this endpoint.

There is no matched sterile/killed/acidity-only control, percentage formula, complete solution/residue mass balance or leaching error bar. Basal9K retains the native community and is not sterile. Repeated99.9 values do not establish recovery beyond reported precision. Introductory mineral proportions are not phase measurements of each aliquot; Ge host and oxidation state are unresolved. Table1 Mn44,500mg/kg differs markedly from the introduction's MnO≤0.2% description. Figure3 exceeds100 on a germination-percent axis and its untreated value differs from Figure1; normalization is unclear. Economic/detoxification/safety claims are therefore not adopted.

## Accepted study B: Vasyleva2016

Methods pp44–45 identify Chervonogradska coal-flotation waste, crushed1–3mm,0.5 L vessels, solid:liquid1:10, a9K mineral background, pH≤2 and1–4 weeks; displayed trajectories run seven days with pH later above2. Table1 Ge is26.0±0.1mg/kg. Nominal ferrous salt is44.5g/L in Methods,44.4 in captions, with8.96g/L Fe(II) stated. Ferric sulfate is3/6/9/15g/L; sulfur reagent5g/L. Hydrates and elemental-Fe equivalents are not independently reconciled. Ca-nitrate dose, incubation temperature, mixing, inoculum preparation and biological replication are absent. Microscopy/dilution counts describe the native community, not an authenticated species. Dissolved metals were measured by atomic absorption.

Original Figure2 shows approximately1.5mg/L Ge at day7 for15g/L ferric sulfate versus approximately0.5mg/L for ferrous treatment. These are visual approximate concentrations, not percentages or digitized raw data. Page50 reports strong ferrous growth and no observed ferric-liquid growth while also reporting nonzero counts; that is neither a sterile arm nor proof of surface attachment. No matched sterile reagent or acid control isolates a microbial advantage. The source itself treats mechanisms as debated; proposed contact, sulfur-inclusion and redox explanations are not direct Ge phase/enzyme measurements.

Conflicts are retained rather than repaired: abstract Na2S2O5, Figure1 Na2S2O3, Figure2 caption Na2S3O5 and prose thiosulfate; final sulfur-labelled Figure2 curve exceeds ferrous despite a broad inefficiency statement; p48's15.0% is not reconciled with Figures1–2; Eh is labelledmV with0.25–0.65 values and no resolved reference, while initial pH/Eh prose differs from graphs. No corrected formula, unified percentage or calibrated redox value is inferred. Earlier2012 fractions do not calibrate the2016 graphs, and sample independence is unknown.

## Fully inspected but excluded mechanism: Dzhambek2019

This original six-page electrochemical paper describes red long-stored and black short-stored coal-beneficiation dumps, without precise locality, sampling age or phase analysis. It says bacteria may be present but supplies no culture, viability, count, sequence or matched sterile evidence. No microbial claim is accepted from it.

Methods p75 use a two-chamber three-electrode system, PI50.1.1/PR8, Ag/AgCl reference, acetylene-black working/counter electrodes, impermeable polyethylene or porous polypropylene separator, solid:liquid1:10,30°C and aeration. The medium lists g/L3 ammonium sulfate,0.1KCl,0.5K2HPO4,0.5MgSO4,0.01 calcium nitrate,44.5FeSO4 and0.001N sulfuric acid (hydrates unresolved), with pH≤1.6–1.7. Nominal0.65V is versus Ag/AgCl; Table2 spans three calendar days but only14.69–16.76 total discharge hours.

Table2 accumulated Ge increments are1.37,1.45 and1.43mg/L for red-impermeable, black-impermeable and black-permeable setups. Reported rates0.0817,0.087,0.097mg/L/h use active discharge time, not72h. Feed Ge inventory, working liquid volume and product mass balance are unavailable. Abstract `(8±2)×10^-2` and body `(8.5±0.3)×10^-2` rate summaries differ without a replication/uncertainty definition. Table1 does not support uniformly improved rate with higher Fe(II): its red0.25V comparison decreases, while a0.65V contrast increases. Page77 reports no linear charge/Ge relationship. Proposed activation/destruction is not demonstrated phase conversion. These details delimit a useful chemical/electrochemical follow-up rather than establish microbial extraction.

## Curation, validation and ranked next work

Frozen record SHA256: `d66baa5a261df19b446a1689dd00222e5be5a603439f28f4b344482a65c0dd20`. Canonical CREATE [history](../../../history/records/coal-beneficiation-waste/2026-10-12T023644Z-codex-ef668b.yaml) SHA256: `b1ebae42277506d336b2e573d01427b50550f66dfcfcf97c6477ea02f37076c7`. The inline event has its own actual UTC timestamp. Named validation returned0, `Checked1 record(s);0 failed`; the complete log and checksum are in JSON. Round43 initialization reuses the actually passed fresh round42 postmerge gate at the exact unchanged base; no new baseline execution is claimed. Parent will run final corpus/history/review gates; this author handoff does not claim those future results or independent acceptance.

1. Complete independent review of the frozen record against all original pages, controls and quantity bases; no schema change is required.
2. For stronger Ge attribution, obtain matched sterile reagent/acid controls, exact leaching duration/doses for2012, authenticated community data and closed mass balances. Resolve sample overlap before pooling these studies.
3. Investigate the unacquired related primary [lead-zinc production waste study](https://dspace.onu.edu.ua/items/1bd9e57e-71e8-4b30-bb8a-caf210dad8fc) as a potentially distinct resource, after acquiring its original methods/graphics; abstract percentages are not accepted here. A separate2012 Biotechnology5(3) lead also needs complete originals and overlap checks.
4. Retain2019 as fully accessible chemical context unless direct biological evidence is supplied. Existing Theisen issue140 remains a separate open acquisition task; no unsupported late record is added.
