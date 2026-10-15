# Round90 resource investigation: coal gasification slag

UTC assessment saved: 2026-10-15T07:18:41.202274Z. Curator: Codex (GPT-6; Codex). Worktree: `/private/tmp/CMMMech-expansion-round90-20261015`; trusted base `2d9fe2b6aa62fed3385111929dee3c4ea1f1b2a1`.

## Selection and conceptual boundary

One new owner is selected: **coal gasification slag**, `secondary_resource`. The complete primary original supports a laboratory chemical treatment of its source-defined crude slag (CGCS), followed by manufacture of a mixed Al/Fe/Ca flocculant. The source distinguishes crude and fine gasification slag; one umbrella owner avoids splitting related feed fractions to inflate coverage. Every accepted experimental statement remains restricted to the supplied CGCS. Coal combustion fly ash, coal-beneficiation waste and coal bottom ash are separate processes or feed identities. No element/mineral/commodity identifier, criticality designation, microbial extraction, or industrial deployment is inherited.

This is the strongest complete evidence recovered in the bounded pass. Searches for direct microbial extraction of gasification slag did not establish an inspectable original with metal-recovery outcomes. A historical review mentions sulfur oxidation without a metal-dissolution measurement; a patent and newer biocarbonation papers remain leads. These are not imported microbial mechanisms.

## Scope and duplicate checks

Hidden and ignored files were included and relevant links followed in `data/records`, `research`, `reviews` and `history` of both current main and the round90 worktree. Normalized DOI `10.1039/d3ra07232k`, PMID38229713, PMCID10790280, gasification/gasifier names, and concept boundaries were checked. The same bounded search checked the all-state issue inventory and the prior round77 resource raw directory cited by the coal-bottom-ash deferral. Search commands, return codes, matches and exclusions are in `/private/tmp/cmm-round90-resources-research/dedup.json` and companion text files. No current owner or accepted study matched these gasification identities in those roots. Coal-fly-ash and coal-beneficiation-waste owners were explicitly distinguished; round77's coal-bottom-ash deferral was retained, not rebranded as this feed. This is not a machine-wide or literature-wide exhaustion claim.

## Accepted primary source and acquisition

Pan, Sun, Shen, Sun, He, Li and Lu (2024), *Coal gasification crude slag based complex flocculants by two-step acid leaching process: synthesis, flocculation and mechanisms*, RSC Advances14:2705–2719, [DOI10.1039/D3RA07232K](https://doi.org/10.1039/D3RA07232K), PMID38229713 / PMCID10790280.

- Complete original15-page publisher-layout PDF acquired from the indexed Semantic Scholar mirror: `/private/tmp/cmm-round90-resources-research/pan2024-mirror.pdf`; SHA256 `d0aea7e870649a7c70c226b20a1f65b7cafe8ab3ef94121e91659e93524e1a79`. It identifies the DOI/authors/volume/page range and CC BY-NC3.0 license. All15pages were extracted and rendered; all14main figures and all5tables were inspected, including high-resolution individual pages3,5–13 for the accepted claims and conflicts.
- Original archived JATS acquired from [EuropePMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10790280/fullTextXML): `pan2024.xml`; SHA256 `b17b20a5ffb0cf58513871232a175c4c71a9c180c0afff1c1ed4a3d883da4f08`. Main-text identity, methods and table contents corroborate the PDF.
- EuropePMC `supplementaryFiles` archive was downloaded and enumerated: `pan2024-supplement.zip`; SHA256 `d8032bf310df6e40ab1547f311e6382d761c3ae67952f2a6a176db8b7a6404ec`. Its 30 members comprise 28 paired JPG/GIF assets for Figures 1–14, plus the graphical abstract and Table 1 JPG. Neither inspected full text/JATS nor archive announces a separate SI document. This is a bounded source check, not an assertion that no additional data can exist. The guessed publisher supplement route returned404 and is not treated as an acquired supplement.
- Direct publisher PDF returned403; publisher HTML in the web reader initially failed but the indexed original text/landing page corroborated bibliographic identity. The NCBI OA-package endpoint returned404. Exact acquisition URLs/statuses/times/types/byte counts/hashes are in the paired JSON and raw acquisition receipts. Failed requests did not become primary files.
- Crossref original metadata gives an empty relation mapping and no update-to/updated-by fields. The explicit DOI/title correction/retraction search did not surface a notice in this bounded pass. This does not establish absence from every notice service. Full original graphical evidence, rather than abstract text, supports the record.

## Claim-level findings and limits

1. **Feed:** §2.1 names the Yankuang National Engineering Research Center of Coal Water Slurry Gasification and Coal Chemical Industry supplier in Shandong. Coal type, gasifier conditions, date and size distribution are not specified. This establishes industrial origin, not an industrial treatment deployment.
2. **Parallel arms:** §2.2.1–2.2.3 and Figure1/PDFp3 show independent HCl and acetic-acid contacts on fresh CGCS portions and later liquor blending. Despite “two-step” in the title, the accepted treatment is not a sequential residue-leaching cascade. Selected conditions are3mol/L HCl,40°C,1.5h and5mol/L HAc,40°C,2h, each15mL/g, in stirred500mLbeakers. Actual charge masses are not stated.
3. **Endpoint:** Equation1/PDFp3 defines85.76% and44.32% as initial-minus-dried-residue mass divided by initial mass for the separate arms. These values cannot be called aluminium, iron or combined metal recovery. More acid/longer contact did not consistently improve the endpoint;50–60°C reduced the reported loss relative to40°C (Figure2/PDFp5).
4. **Mixed recovered product:** Liquors at3:2HCl:HAc volume ratio, pH3.5 adjusted byNaOH,70°C3h,24h aging and unspecified-temperature oven drying yielded PAFAC. Section2.4/PDFp4 ashes the feed at815°C1h only for XRF; this is not an established treatment of the reaction feed. Tables2–3/PDFp7 compare ashed oxide-basis feed and unashed elemental-basis product. Na and Cl include reagent-derived constituents; Figure5A/PDFp8 identifies NaCl. Neither composition table closes a feed-to-product balance or proves elemental product purity.
5. **Reuse and negative result:** Sections2.3/3.4, Figures6–7/PDFpp8–9 report200mL jar tests. At250mg/L PAFAC in domestic sewage, the dose assay reports89.62% turbidity/58.95%COD/76.76%TP removal; ammonia-N remains below10%. The separate three-flocculant comparator assay gives91.42%/59.94%/78.77%. These are not pooled, converted to metal recovery, or represented as a plant result.
6. **Missing controls/balances:** No matched water-only slag-leach blank, acid/reagent-only flocculation blank, full dissolved-element inventory, product mass yield or quantified trace-contaminant safety assessment is supplied for the accepted claim. Washed-residue loss can include nonspecific soluble losses. No species/strain is involved in the accepted process.
7. **Preserved source conflicts:** At2:3liquor ratio, §3.2.1 states84.15% turbidity removal but Figure3B/PDFp6 places the bar above90%; the discrepant nonselected value is not imported. Figure8/PDFp10 caption assigns panels by equation but Table5 assigns rows by acid, although each graph contains both acids; no fitted parameter is imported as causal proof. Section4.2.1 describes decreasing zeta potential whereas Figure10/PDFp11 becomes less negative up to250mg/L. The source labels a third water “aquaculture wastewater” yet §2.1 says cow pasture; no broad aquaculture claim is made. These are uncertainties in the primary source, not silently corrected measurements.

## Deferred and duplicate leads

- Coal-bottom-ash bioleaching: already bounded/deferred in round77; no newly verified microbial study in this pass. No owner addition.
- [Xiang et al., *Mechanism of bio-carbonation on leaching behavior: a case study of coal gasification slag-based binder*](https://www.sciencedirect.com/science/article/pii/S0950061826003417): publisher discovery text describes carbonic-anhydrase bacteria and element immobilization. Complete original methods/graphics/SI were not acquired or accepted; a useful follow-up must resolve organism identity, actual feed, controls, carbonation and leach-denominator scope.
- [*Microbial carbonation reshapes hydration-carbonation reaction pathways in coal gasification slag-derived low-alkalinity geopolymers*](https://www.sciencedirect.com/science/article/pii/S0950061826028849): discovered late as a related ureolytic-carbonation lead; no measurements or taxon claims imported.
- Francis1990 review [archived government PDF](https://www.wipp.energy.gov/library/cra/2009_cra/references/Others/Francis_1990_Microbial_Dissolution_and_Stabilz_of_Toxic_Metals.pdf): discovery text explicitly says metal dissolution from the cited gasification waste was not investigated; needs the original reference before any mechanism claim.
- Danková et al.2013 DOI10.13189/bb.2013.010302, bacterial regeneration of Cu-loaded montmorillonite/composite: laboratory-loaded sorbents and an existing montmorillonite owner; not treated as a new industrial waste feed merely because used in an experiment. Full mechanism not imported.

## Curation handoff and next actions

Created `data/records/coal-gasification-slag.yaml` SHA256 `eb3030529d996be96b29e4adc4bdd37dfa81c68084fe77dc64817ab01c0b4fba` with canonical CREATE `history/records/coal-gasification-slag/2026-10-15T071639Z-codex-2bd5d7.yaml` SHA256 `ea3e12a37ddb23b035ea6f647024e5ec25b3590221293b5862ddcf77d588f893` and actual inlineevent. Named strict validation completed1record/0failures; raw receipt`named-validation.json`. Baseline proof explicitly reuses the just-completed fresh postmerge checks at the exact base/tree; no fresh round90 baseline execution is claimed. Independent scientific review and root-owned batch gates remain required and are not preclaimed here.

Priorities: independently review the original parallel-arm and gravimetric-denominator scope; obtain original mass-balance/control data and resolve the source's diagram/text inconsistencies if expanding quantitative claims; acquire complete microbial-carbonation originals before adding a microbial mechanism. No schema change or automatic importer is needed. Raw copyrighted originals and derived page images remain outside Git. The source's CC BY-NC3.0 license is recorded, without claiming unrestricted commercial redistribution.

## Search log

Provider: web search tool; date2026-10-15UTC; no domain/recency filter; returned result sets inspected, no claimed exhaustive pagination. Exact queries:

- `"coal gasification slag" bioleaching microbial metals`
- `"coal gasification fine slag" bacteria extraction`
- `"coal bottom ash" bioleaching fungi aluminum iron`
- `"coal gasification slag" "bioleaching"`
- `"gasification fine slag" "bioleaching"`
- `"coal gasification" "bacteria" "metal" leaching`
- `"coal gasification slag" "Pseudomonas"`
- `"coal gasification crude slag" "two-step" leaching PMC`
- `"bioleaching" "spent" "adsorbent" metal recovery`
- `"bioleaching" "spent" "sorbent"`
- `"10.1039/D3RA07232K" PMC`
- `"coal gasification" "microbial" ash slag sulfur 1980`
- `"Coal gasification crude slag based complex flocculants" supplementary`
- `"10.1039/d3ra07232k" correction OR erratum OR retraction`
- `"coal gasification slag" "leaching" "bacteria" extraction`
- `"Coal gasification crude slag based complex flocculants" "supplementary"`
