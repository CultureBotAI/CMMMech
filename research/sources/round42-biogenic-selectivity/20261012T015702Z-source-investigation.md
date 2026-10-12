# Source investigation: biogenic birnessite Co/Ni selectivity

UTC: 2026-10-12T01:57:02.605617+00:00. Curator: codex / GPT-6 / codex, `/root/round27_packaging`. This is an author investigation and curation handoff, not independent scientific review.

Worktree `/private/tmp/CMMMech-expansion-round42-20261012`; branch `curate/cmm-expansion-round42-20261012`; trusted base `a5528a4807ba14fd8088a557ad105ac10ca62965`. The exact preceding fresh-main baseline is honestly reused through `/private/tmp/cmm-round42-initialization.json`; no redundant baseline execution is claimed.

## Decision and source identity

Extend [birnessite](../../../data/records/birnessite.yaml) with a distinct mixed-Co/Ni sorption assay from Sasaki, Kaseyama and Hirajima, [Selective Sorption of Co2+ over Ni2+ Using Biogenic Manganese Oxides](https://doi.org/10.2320/matertrans.M-M2009821), Materials Transactions50(11):2643–2648(2009). The official final six-page PDF, all12 original figures and both tables were acquired and inspected. The source says advance publication7October2009; publisher issue date1November2009 and availability25October are separate events. Crossref metadata corroborates title/authors/DOI/year. J-STAGE explicitly lists zero supplementary files; no SI access is invented.

This continues the existing owner rather than creating a second mineral. The 2009 paper calls its product poorly crystalline birnessite but prints no new diffraction pattern or quantitative phase analysis. Its characterization citation points to reference15(Murray1984); the related WL-2 characterization appears separately as source7(Sasaki2008). Prior uncertain phase attribution remains important. Dated IMA/Handbook identity and earlier experiments are preserved, not falsely claimed as fresh authority research.

## Acquisition, deduplication and notices

The first network attempt failed with sandbox DNS errors; a permitted network-enabled retry downloaded the official PDF, publisherHTML, Crossref and NCBI443224. Both receipts are retained. PDF SHA-256: `eb7ecae442f557dc472c2fe06c2ac7699f7ff1e7f7b1029a319605ea35ef6cb2`. Original files and all six rendered pages remain outside Git at `/private/tmp/cmm-round42-biogenic-selectivity-research/raw`; the paired JSON records source URLs, actual access times and all hashes. Free reading access does not establish redistribution rights: the PDF bears2009Mining and Materials Processing Institute of Japan copyright, and no open license was verified.

Fresh bounded dedup included both the current and original checkout `data/records`, `research`, `reviews` and `history` trees, hidden/ignored files and followed relevant symlinks, then132 referenced existing research/raw/assist directories. A3,248-file metadata pass identified those roots. Raw searching used retained text, HTML/XML/JSON and PDF extractions, not recognition of unextracted binary figures; unrelated home/temp areas were excluded. The DOI occurs only as a frontier lead in the maintained corpus. WL-2 and birnessite already have owners/studies; the2008Co-only,2009binary and2022fungal-transformation experiments are not pooled. Two checkout copies are not two studies.

Five exact bibliographic/notice/counterevidence queries are recorded in JSON. Returned results and current publisher/Crossref fields identified no specific correction or retraction; this bounded negative result is not exhaustive. Current source inconsistencies below remain unresolved. A broader structural counterevidence lead is only a future investigation, not accepted evidence. Yu2012 source gap[#137](https://github.com/CultureBotAI/CMMMech/issues/137) remains open.

## Assay, controls and quantities

Section2(p2643) uses freeze-dried WL-2 fungal oxide0.020g or chemical oxide0.015g in0.150L, nominally1mmol/LsolidMn,100mmol/LKNO3,PIPES-buffered initialpH6.5,25degreesC,100rpm and300hours; assays are duplicated. PIPES concentration is not stated. Co-only and Ni-only assays precede separate binary mixtures. For the latter, methods nominally fixCo0.3mmol/L andNi0.1–1.0; Figures7–8/Table2 specify actual(Co,Ni) initial pairs(0.31,0.10),(0.35,0.35),(0.34,1.00)mmol/L plusCo-only comparison. ICP-MS examines0.2micrometre filtrates; originalµg/L detection units were visually checked, not mistaken for mg/L extracted text.

The fungal powder’s origin warrants `microbial:true`, while no viability or metabolic sorption requirement is demonstrated. Fresh NCBI443224 retains `Paraconiothyrium sp. WL-2`; species rank does not resolve a named species or authenticate the culture stock. A preliminary tissue-only null is stated without a displayed dataset. There is no displayed no-sorbent timecourse or sterile formation series. The chemical comparator is ramsdellite, with11.5m2/g versus81.4m2/g; phase, area, oxidation composition and biomass are confounded.

Figures7–8 support preferential fractionalCo depletion, weakerNi uptake andNi inhibition ofCo uptake. Table2 reports dimensionlessalphaCo7.92,7.47,17.7 forbiogenic and5.65,2.23,2.65 forchemicalmaterial at the listed pairs. Equation3 definesalphaCo=(XCo/CCo)/(XNi/CNi), using sorbed/aqueous molefractions. These are source-reported phase-distribution coefficients, not percentages, isolatedproductpurity or recoveryyield; no replicate-level dataset independently reproduces their uncertainty. Mn is also released and subsequently decreases, including no-Co/no-Ni backgrounds in Figures1/3. No closed massbalance follows.

## Original graphics and conflicts

All six pages were read and visually inspected: p2643methods; p2644Table1/Figure1; p2645Figures2–4; p2646Figures5–7/Equation3; p2647Figures8–10/Table2; p2648Figures11–12/references. Figure12 is a proposed site diagram, not occupancy imaging. Figures9–11 provide exsitu surfaceXPS interpreted asCoIIIandNiII; collected0.45micrometre residues were lyophilized overnight. This does not establish all-sorbedCo oxidation, bulkCoOOH identity, purity or yield. Real leachates, desorption/regeneration and industrial operation were not demonstrated.

- Table1 givesMnAOS3.09/3.68; adjacent prose3.17/3.70. The prose invokes lackofsyntheticMnIII although Table1 givesMnIII molefraction0.296. No single reconciled redoxinventory or unique preferredoxidant is adopted.
- Methods single-ion maximaCo1.7/Ni2.11mmol/L differ from Fig2Co2.19 andFig3Ni2.31. Binary pairs are kept separate. The biogenic Mn-release paragraph citesFig8a/c even thoughFig8 is the chemical comparator; Fig7c is the actual biogenic panel.
- Figure5 uses sorbed amount perMnIII/IVmass excludingMnII, nottotalcomposite. Figures5–6 are fittedisotherms, not independent observations. No fittedcapacity or universal biologicallycaused advantage is imported.
- AbstractNi-edge-site language differs from the body’s layer-substitution/no-edge-competition discussion. Site-specific causal claims remain proposals, and the2008Mnoxidant discrepancy is not erased by the2009interpretation.
- The2009post-sorption lyophilization differs from the2008air-drying step. Same strain/material lineage is not demonstrated independent batch production or identical-assay replication.

## Curation, checks and handoff

Appended one source, one mechanism, one actual inlineEDIT event and [one canonicalEDIT history](../../../history/records/birnessite/2026-10-12T015436Z-codex-a24dff.yaml). Every previous field and ordered list prefix—including introduction—and both old history byte hashes remain unchanged. The initial in-memory fragment failed its preservation assertion before a record write; its indentation was corrected before integration. No failed scientific record was frozen or accepted.

Frozen record SHA-256: `68f1ff968be471ba2095191414df2e51608002b5d34285dadde2814825ac65f4`. New history SHA-256: `76bac25843cd385f3fac82ac6bbd486c95561de7e1b615c6b5eef99550accaa4`. Named validation completed exit0 with1record checked/0failed. The paired JSON contains the preservation proof, exact raw manifest and validation log hash. No schema/validator/test changes were needed. Parent owns full cohort gates; an independent agent must inspect the final record and save native scientific review before acceptance. No self-review verdict is claimed.

Next: independently review this narrow arm; keepYu2012access/overlap questions open; acquire complete primary originals before any further selectivity or structural extension. This bounded result does not exhaust sources.
