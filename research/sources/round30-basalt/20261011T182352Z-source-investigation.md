# Basaltic-rock source investigation and curation handoff

UTC: 2026-10-11T18:23:52.034889+00:00

Author: codex (GPT-6; codex), round27_packaging subagent. This is a curator source assessment, not independent scientific acceptance.

Base: `930ce995269f0ded5df009eb5916162971eb1f58`; branch `curate/cmm-expansion-round30-20261011` in `/private/tmp/CMMMech-expansion-round30-20261011`. This task owns the basalt record, canonical CREATE history and this dossier; other cohort edits may coexist. The parent verified unchanged baseline bytes against the completed fresh-main gate and completed offline locked synchronization; receipt `/private/tmp/cmm-round30-baseline-receipt.json`.

## Decision and identity

Ready for independent review of [basalt.yaml](../../../data/records/basalt.yaml), a `primary_resource` named Basaltic rock. The useful evidence is laboratory colonization and specimen-dependent aqueous redistribution, with explicit inability to prove active dissolution of the natural rocks. `process: other` avoids labelling these outcomes as demonstrated active bioleaching. No jurisdictional criticality, mineral-species identity, recovered commodity or industrial scale is asserted.

The complete primary study is [Stranghoener et al. 2018](https://doi.org/10.3389/fmicb.2018.01252), Frontiers in Microbiology 9:1252, PMID 29963022, PMCID PMC6010528. Six AMNH-provided HSDP2 Hawaiian geological specimens comprise basaltic flows BF1/BF2 (604/2399 m below sea level), hyaloclastites HC1/HC2 (732/1904 m), and pillow basalts PB1/PB2 (2377/2385 m). They contain glass, silicates and variable secondary alteration. BF1/HC1 are mainly cryptocrystalline, while most other specimens are 60–90 vol% glass. Table 1 gives manufactured BAS glass and an older average of natural glasses, not the six specimens' measured bulk grades. The separate manufactured BAS1–BAS3 droplet experiments remain context only.

## Deduplication and research bounds

Both this worktree and the original checkout's `data/records`, `research`, `reviews` and `history` were searched with `rg --hidden --no-ignore --follow`, including ignored and hidden contents, for basalt, the normalized DOI, PMCID and author. Results are retained in `/private/tmp/cmm-round30-basalt-research/dedup-repository-hits.txt`. The existing cobalt-rich-ferromanganese-crusts record mentions geological basalt interfaces but represents the crust; biogas-desulfurization-sulfur-residue mentions a source-labelled medium, not this feed. The round29 frontier is the uncurated lead. No accepted basalt root or adopted HSDP2 experiment was found in that bounded scope before creation.

Referenced raw holdings were also searched with hidden/ignored inclusion: `/private/tmp/cmm-round29-ilmenite-research`, `/private/tmp/cmm-round28-mineral-frontier-search.json`, `/private/tmp/cmm-round21-crusts-raw`, `/private/tmp/cmm-round23-crusts-raw`, and `/private/tmp/cmm-round20-nodule-raw`. Exact command, exit code and paths are retained in `dedup-referenced-raw-receipt.json`; one hit was the earlier uncurated lead. The prior Carlsberg Ridge Mn-coated basalt study (Sujith 2014, DOI 10.1016/j.chemosphere.2013.09.103) is a distinct contextual lead and not adopted as HSDP2 evidence. No machine-wide absence claim is made.

## Search and access

On 2026-10-11 the web search provider's first returned result sets were inspected for these exact queries, without date/domain filters or subsequent pages:

- `"10.3389/fmicb.2018.01252"`
- `"Burkholderia fungorum" "ATCC BAA-463" DSM`
- `"10.3389/fmicb.2018.01252" correction erratum retraction`
- `"Paraburkholderia fungorum" taxonomy 134537`
- `"Experimental Microbial Alteration" "Image_1"`
- `"10.3389/fmicb.2018.01252" figshare`

Publisher HTML, the complete 17-page PDF, Europe PMC JATS and Crossref metadata were acquired freshly. All eight original main figures and Table 1 were inspected in the PDF, including full-page rendered inspection of pp3–5 and pp7–12. Failed PMC OA and Europe PMC supplementary archive routes returned 404; PMC image URLs returned HTML download challenges rather than images and were not misrepresented as successful source acquisition.

The publisher-linked public Figshare API was searched with `{"search_for":"10.3389/fmicb.2018.01252","limit":10}` at `/v2/collections/search` and `/v2/articles/search`. It returned collection 4133297 and exactly three matching supplementary articles. All three original JPEGs were acquired through their public download URLs and individually inspected; each downloaded MD5 matches the API's computed MD5. DOI suffixes `.s001`, `.s002`, `.s003` correspond respectively to Figures S1, S2, S3 (articles 6529445, 6529451, 6529457; files 11997773, 11997779, 11997785), all version 1, originally published 14 June 2018. The portal's 2023 metadata modification dates do not establish a new experimental edition. These files are parts of one study, not independent replication.

The main article states CC BY; Crossref specifies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as do all three Figshare records. Bulk source bytes remain outside Git. Full acquisition URLs, original UTC times, content-type checks, failures and SHA-256 hashes are in the companion JSON; expiring public redirect query strings are omitted there. No inaccessible methods are claimed to have been read. No independent assay workbook or numerical source table was located in this bounded linked supplement inventory; there is no invented dataset dictionary or bulk import.

## Organism identity

[NCBI Taxonomy 134537](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=134537&mode=Info) resolves the current species Paraburkholderia fungorum. The paper calls it Burkholderia fungorum and uses ATCC BAA-463 obtained from DSMZ. [DSMZ DSM 17061](https://www.dsmz.de/collection/catalogue/details/culture/DSM-17061) explicitly equates ATCC BAA-463 and documents isolation from Phanerochaete chrysosporium. The current ATCC product page was also inspected. This collection strain was not isolated from the tested Hawaiian cores; species taxonomy is not a new sequence verification of the experimental stock.

## Assays, controls and actual outcome

Natural-rock assays used 350 mg of 1–2 mm plus 150 mg of 0.2–1 mm washed crushed grains, 50 mL medium in 100 mL flasks, three biotic and three uninoculated parallels at each of 8 and 30 °C, 125 rpm and 41 d. The 5 M HNO3 treatment cleaned flasks, not rock. Rock was sterilized three times at 105 °C, cooled between cycles and washed again. This preparation released nutrients from secondary phases, incompletely removed by washing.

M-minus-P contained per litre glucose 0.2 g, NH4Cl 0.04 g, KCl 0.0005 g and MgSO4 0.0005 g, adjusted to pH 7. Cells were precultured in tryptic soy and then M-plus-P, washed into M-minus-P and inoculated at about 10^5 cells/mL. The phosphate-containing preconditioning medium is not the assay formulation. Cells grew with glucose depletion; controls retained glucose and had no cells detected by the authors' microscopy. Cell counts represent only one parallel. Sterility was not independently sequence-tested.

Withdrawals of 6.5 mL on days 1, 3, 9, 28 and 41 supplied 0.2-µm filtered chemical aliquots, acidified to 0.3 M HNO3 and measured by ICP-OES. Equation 1 corrects serially withdrawn amounts and normalizes to the initial 50 mL. These values are aqueous analytical outcomes, not percentages extracted or isolated-product yields. Evaporation was reported as about 5.5 mL over 41 d; no unreported mass-balance correction is invented. No matched-pH control was maintained.

At 30 °C, Figure 4/Results describe lower cultured Si/Mg/Ca/K/Na/P/Mn than controls at day 1 for HC2/PB1/PB2, but higher cultured Fe/Al; BF1/HC1 generally show the opposite Fe/Al direction while several other elements are higher in culture. BF2 is mixed and many control outcomes exceed culture. Neither all time points nor all elements show enhanced release. The original Figure S1 at 8 °C does not reproduce every generalized 30 °C Fe/Al direction; BF1/HC1 cultured Al exceeds controls at some times, and BF2 endpoint Fe/Al SD bars overlap. No significance test or digitized precise yield is invented.

SEM Figure 5 shows cells preferentially on glass and rough surfaces, but Results p9 explicitly reports no major culture/control surface-morphology difference apart from attached cells. Discussion p12 says the natural-rock experiments do not clearly establish active bacterial dissolution, because cells may simply scavenge previously mobilized nutrients. Possible secondary precipitation and cellular uptake are not quantitatively separated. The abstract's stronger nutrient-depletion interpretation is bounded by that explicit limitation.

## Synthetic analogues and source inconsistencies

Synthetic assays used about 1.5 g BAS glass/50 mL, 30 °C, 80 rpm, 42 d, two biotic and one abiotic flask. Figure 6 reports chemistry from only one parallel. Measured Fe(II)/total Fe fractions were 0.36/0.37/0.86; annealing and quenching differ, but residual stress was not measured. Figures 7–8 and S3 show qualitative surface association/alteration of the manufactured glass, not these natural feeds. S2 joins two measured pH endpoints; dashed lines do not supply an observed intermediate trajectory. Molecular chelator causality, Fe oxidation energy metabolism and product recovery were not established.

Additional explicit source discrepancies are retained: Methods nominally excludes Ca yet Results says Ca was initially detectable; Discussion groups HC2/PB1/PB2 above 30 m²/g although Methods gives PB1 20.23 m²/g; main prose's same-trend statement at 8 °C is overbroad. A provisional concern about Discussion mmol/L versus Figure 4 µmol/L P was rejected after visual inspection: the broken upper axis reaches tens of thousands of µmol/L. No invented 1000-fold typo or reconciled elemental mass balance is asserted.

Exact-DOI correction/erratum/retraction search did not reveal a notice in the bounded returned set. Retrieved Crossref has an empty relation object and no update-to/updated-by fields. This is a bounded metadata/search check, not an independent Crossmark response or proof that no notice exists anywhere.

## Handoff, validation and limits

The schema already supports this narrow `primary_resource` / `other` claim. No schema change, fabricated source identifier, inherited criticality or positive extraction requirement is needed. Numerical aqueous values remain qualified prose because the native mass-based observation contract is not an aqueous time-series contract.

Canonical CREATE: [2026-10-11T182152Z-codex-1ab4c7.yaml](../../../history/records/basalt/2026-10-11T182152Z-codex-1ab4c7.yaml), actual UTC 2026-10-11T18:21:52Z. Named validation completed with exit 0: `Checked 1 record(s); 0 failed.` Receipt `/private/tmp/cmm-round30-basalt-research/named-validation.json`. Record SHA-256 `7a8bf06d203f0bb20d467d458f954d7fc90887ade382895ffdbaf9fdb8e583ac`; history SHA-256 `97ce55ecd6437d4dabc080398362ac224c787cf8f85423094b4751ec2776ceeb`. The first history-helper attempt preceded record creation and correctly refused a missing target; the successful canonical helper was run after the record existed. This did not create a phantom history entry.

Priority 1 is independent review of the complete frozen record and retained evidence, followed by the parent's cohort gates and publication checks. Future studies that resolve active natural-rock dissolution would require better preparation controls, matched pH and closed elemental/biomass/solid balances. Older cited papers were not newly acquired and cannot supply missing causal proof here. This report does not certify its own authored record.

Raw root: `/private/tmp/cmm-round30-basalt-research/raw`. Companion JSON: [20261011T182352Z-source-investigation.json](20261011T182352Z-source-investigation.json) contains all raw-file hashes and acquisition receipts. No bulk PDF/image files are committed.
