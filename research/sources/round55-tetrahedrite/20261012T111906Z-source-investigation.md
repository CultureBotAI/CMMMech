# Tetrahedrite concentrate: source investigation

UTC: 2026-10-12T11:19:06.464551Z

Actor: codex / GPT-6 / codex. Trusted base: `19d0972767b266f86a256a3f36f0f7177ab4cf25`.

## Decision and maintained owner

Curated [tetrahedrite-concentrate](../../../data/records/tetrahedrite-concentrate.yaml), a **primary_resource** representing the mixed Rožňava flotation feed. A mineral-group label is not a suffix-species identity, and flotation does not establish a discarded waste stream. No elemental criticality is inherited. The mechanism is qualified culture-associated laboratory leaching, without an isolated metal yield or industrial claim. This is an author handoff; scientific acceptance requires another reviewer.

Record SHA256 `283fbf1d2dc0b4a213a83df193daa33c54c65e9e007116c6947d2a2f3518cb7f`. Canonical CREATE [history](../../../history/records/tetrahedrite-concentrate/2026-10-12T111707Z-codex-f553c9.yaml) SHA256 `6160a466245fc8e2485719a01cf18a8fa5bd5ff96e193bb4466c9b2c6ee12ddd`. Named validation returned0: one checked, zero failed. Parent owns cohort gates and independent review.

## Complete primary access and original inspection

Kupka et al. (2025), [Bioleaching of Tetrahedrite by Iron- and Sulfur-Oxidizing Bacteria](https://doi.org/10.1007/s40831-025-01089-0), Journal of Sustainable Metallurgy11:3685–3699, published23April2025. Crossref and publisher identity match. The original [German National Library copy](https://d-nb.info/1370174764/34) supplied a complete15-page PDF: `/private/tmp/cmm-round55-tetrahedrite-research/raw/kupka2025-dnb.pdf`, SHA256`5967395754b051635f6aa660c61e1378b39bf7391e2500c0d9d7fa884b32f402`. This is the original online-first layout without final printed pagination; use PDF-page locators. All15 pages, eight main figures, graphical abstract and both tables were personally inspected. Official full HTML and separate original figures/table HTML were also retained.

The official seven-page supplement (`raw/kupka2025-supplement.pdf`, SHA256`7130190b56a1ae89a3ad4d0005d528a97fd4c5b26227952c11956142817d232c`) has12 figures and no tables. All seven pages/all figures were inspected. The shorter SI title is bound to the main paper by the original publisher link and identical author list. Render paths are `raw/main-pages/page-01.png` through15 and `raw/supplement-pages/page-01.png` through07. Original publisher figures are `raw/40831_2025_1089_Fig*_HTML.*`.

Earlier Springer PDF routes returned400/404, and the Thuringia repository returned an HTML proof-of-work challenge. The misleading `raw/kupka2025.pdf` extension is preserved as an **unsuccessful HTML response**, never treated as evidence. The DNB route newly resolved the local-main-PDF gap; failures were not retried indefinitely. Acquisition1–5 JSON receipts retain exactURLs, UTCs, response status and checksums. CC-BY4.0 is stated in original page13. Raw originals remain outside Git.

## Feed, conditions and measured outcomes

The source identifies the Strieborná vein, Mária Mine, Rožňava ore field, eastern Slovakia. Crushing/milling nominally below100micrometres preceded flotation; occasional larger quartz grains were described. Tetrahedrite is the principal sulfide with siderite/quartz and minor other sulfides. Bulk Table1 gives Cu25.59, Sb19.68, Ag0.57wt%. Table2 comprises24 selected electron-microprobe analyses, not a bulk phase census. Current IMA September2026 page215 distinguishes modern tetrahedrite suffix species; no phase ID is assigned to the whole concentrate.

Separate A. ferrooxidans DSM14882 and A. ferrivorans SS3 DSM17398 assays used washed late-exponential iron-grown cultures resuspended in iron-free basal salts, initialpH1.5,2%pulp,25C,150rpm,120days, triplicate flasks. No externalFe was supplied to leaching medium, but the feed containedFe/siderite. Abiotic medium+feed was autoclaved105C15min. Copper and sulfate rose markedly in cultures compared with abiotic treatment. Antimony rose then partly declined, while abioticFe/Mnrelease exceeded inoculated release atday35. Figure5Zn/Ag is only ferrooxidans versus abiotic. Filtered liquid concentrations are not isolated recovered metals. Grain images show heterogeneous altered rims with residual cores. Oxygen-consumption and Fe-speciation observations support the authors' iron-cycling interpretation without a gene/enzyme intervention.

## Preserved uncertainties and contradictions

- Figure 2a labels Cu/Fe g/L while 2b-c label mg/L. The generic >4 g/L and >80% Cu extraction prose does not fit both plotted culture endpoints equally. No numeric dissolved-Cu endpoint or yield is curated.
- Siderite is described as about 20% and quartz in similar proportion, but Table 1 reports 1.00 wt% SiO2. The assemblage is not quantitatively reconciled.
- Table 2 gives n=24 analyses, As minimum 0, maximum 1.59 and mean0.03 wt%. Those values cannot all describe the same nonnegative24-point population (1.59/24>0.03); no synthetic correction or precise phase composition is derived.
- Figure 5 is only A. ferrooxidans vs abiotic, Zn mg/L and Ag micrograms/L. Graphical abstract maxima lack an explicit sampling-corrected denominator and are not imported as yields.
- The source says all Cu/sulfate originate in tetrahedrite despite mixed sulfides and sulfate-containing medium. This record avoids exclusive phase attribution.
- Control medium+concentrate were autoclaved105 C15min; identical treatment of inoculated feed is not explicit. pH and iron-speciation exposure differ among treatments. No pH/ferric matched control, enzyme-specific test or gene evidence.
- No explicit pulp-percentage basis, flask working volume, inoculum dose/density, sampling volume/replacement correction or full elemental mass balance. Nominal<100micrometre milling coexists with occasional~300micrometre quartz grains.
- As/Sb discussion points to Fig5b but actual profiles are4a-b. SI Fe-XPS referenceS2 is actuallyS9; S2 is starting ore with secondary covellite. Main7 andSI6-7 reuse images.
- XPS is surface chemistry, including initial FeIII/SbV; it cannot establish dissolved speciation or bulk quantitative transformation. Scorodite was not detected; tripuhyite is proposed, not identified. Residual cores and heterogeneous rims remain.
- Fig8 uses Cu9.95apfu to infer reacted tetrahedrite then compares oxygen use with idealized stoichiometry; this is not an independent phase-yield assay. Four parallel gas experiments are described separately from triplicate flask methods. Siderite complicates CO2 balance.
- NCBI species160808 type strain is not SS3. DSM17398 confirms SS3; DSM14882 confirms the other named culture. DSM14882 catalogue discourages shaking, whereas this experiment uses150rpm; different medium/protocol contexts, not independently demonstrated falsification.
- Laboratory only; source authors explicitly acknowledge rates may be too low for practical application. No isolated metal, phase-pure product or deployment.

## Authorities, corrections and bounded novelty

Fresh official NCBI species pages920 and160808 and DSMZ cultures14882/17398 were read. They support labels/strain aliases, not authentication of the experimental stock. IMA September2026 official PDF bytes were transparently reused and the definitions/page215 re-inspected; the failed broad search did not establish a newer edition. Species accessions and type-strain distinctions are not transferred indiscriminately.

The paired JSON records nine actual web queries, including exactDOI correction/retraction/erratum searches. No affecting notice appeared in those returned sets; Crossref has no update-to and empty relation. This is a bounded negative result, not a claim that no notice exists anywhere.

Hidden and ignored files were included with cycle-safe symlink-following traversal of current and original checkout data/research/reviews/history and185 existing referenced raw roots. The census searched4216 corpus text files and7909 total unique text files;130 files matched the declared terms. Nine raw roots were missing,12 older text logs exceeded the16MB cap, and unextracted binaries were not semantically searched. Exact roots, missing paths, skipped files, pattern and matching-line excerpts are in the paired JSON and `/private/tmp/cmm-round55-tetrahedrite-research/dedup.json`. No already accepted owner of this specific concentrate/experiment was found within those bounds. Existing tennantite concentrate and the concurrent Okibe enargite feed have different sources/compositions. Shared main/SI images are counted as one experiment.

## Useful next evidence, not accepted extensions

The original reference list verifies Aghazadeh2023 DOI10.1007/s40831-023-00675-4 and10.1016/j.hydromet.2023.106075. Their full originals, feed differences and alkaline/mechanical pretreatments still require inspection before importing numerical comparisons. A2026 consortium study with publisherPII S0013935126007620 and a2025 antimony-bioleaching chapter are search leads only; exact overlap remains unresolved. No extra owner is admitted from these leads.

## Artifact provenance and handoff

The paired JSON contains 57 raw artifact hashes and 7 receipt hashes, exact acquisition responses, authority inventory, dedup boundaries, experimental caveats and named-validation command. Copies of source PDFs/graphics are outside Git. Independent review should particularly challenge the culture/control contrast, Figure2units, phase attribution, XPS-versus-bulk scope and any tendency to interpret mobilization as recovered product. No schema/validator/shared-document changes were needed.
