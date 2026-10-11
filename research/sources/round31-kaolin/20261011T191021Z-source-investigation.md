# Natural kaolin source investigation — round31

Created 2026-10-11T19:10:21Z; evidence work by `/root`, GPT-6, Codex.
Base `075c1ca032b68162eb8350b7e8d9bfe9530ca143` in the round31 isolated worktree.
Accepted target: `data/records/kaolin.yaml`; linked CREATE sidecar is recorded in the companion JSON.
This is a discovery/curation handoff, not an independent scientific review.

## Selection and identity

The source search found a natural, mixed kaolinite-bearing ore with a complete original fungal experiment and explicit no-fungus controls. That provides a useful primary-resource contrast to the independently curated discarded kaolin mine waste. Natural kaolin is not the pure kaolinite mineral, aluminium, refined alumina, or high-purity alumina. No criticality list claim is made and none is inherited from a constituent. Experimental mineral phases come from the original XRD; bulk oxide equivalents do not determine mineral fractions.

Prior-record dedup searched `data`, `research`, `reviews`, and `history` in both the new worktree and original main checkout, plus referenced `/private/tmp/cmm-round12-aluminium-boron-raw`, `/private/tmp/cmm-expansion-authorities-20261011`, and `/private/tmp/cmm-next-eu`. It used `rg --no-ignore --hidden --follow` with kaolin/kaolen and both exact DOIs; the companion JSON records paths, commands and return codes. An initially overescaped DOI expression was corrected and rerun before claiming deduplication. Self-authored round31 artifacts were excluded from prior-existence assessment. Hits concern high-purity alumina identity, bauxite containing kaolinite, general critical-material lists, and the separate ilmenite investigation. No accepted natural-kaolin record was found within those declared roots. Raw binary PDFs were not globally text-extracted for this search; this is neither machine-wide absence nor source exhaustion.

## Primary evidence accepted

[Kale and Çiftçi 2020](https://doi.org/10.35354/tbed.592519), original [seven-page PDF](https://dergipark.org.tr/en/download/article-file/977461), SHA256 `d4d0e551751439933a171f759ba785f634628908ef0701aa9efbf2ebac09107a`. All pages were read visually, including Table1 and Figures1–13; Turkish methods/results were interpreted directly with the English abstract, without claiming a separate human translation. The [official page](https://dergipark.org.tr/tr/pub/tbed/article/592519) lists the full text and no separate experimental supplement in its file listing. This bounded page inspection does not establish that no underlying data exist. Crossref resolves the same DOI, title and 2020-02-20 date. Its returned relation object is empty and update-to/updated-by are absent. The PDF's English header says issue2 whereas Turkish header and official citation say issue1; the record avoids the inconsistent issue number.

| Locator | Curated observation | Limits |
| --- | --- | --- |
| §2, Table1 | Bilecik-Söğüt natural ore; kaolinite/quartz/microcline; ground below106µm; 0.82wt% Fe2O3 oxide equivalent | Not pure kaolinite or a phase-specific iron assay |
| §2, Figs3–6 | Supplied living A.niger culture; 250mL in 500mL flask,30°C125rpm;1–10% solids; medium controls without fungus | No strain/accession or molecular authentication; control pH not matched |
| §3.1, Figs4–6 | At1%solid/10%sucrose,day0 addition: reported52.47% removal at336h vs6.22% control;10%solid gives18.51% | Author-reported percentages; no explicit calculation, serial sampling correction, replicate count, error bars or closed balance |
| §3.2, Figs7–9 | At5%solid,10%sucrose gives34.66% at336h, above5/15/20%sucrose | Nonmonotonic, so not a blanket higher-sugar inhibition rule |
| §3.3, Figs10–13 | With1%solid added at240h,reported61.09% endpoint at504h culture time | 264h mineral contact; no matched504h abiotic endpoint displayed; do not call this a14-day result |
| §§2–4 | Lower cultured pH, analyzed Fe and biomass | Organic acids and Fe valence were not measured; acid mechanism proposed; no recovered iron product or standardized whiteness result |

[NCBI Taxonomy5061](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5061&mode=Info) directly returned current name Aspergillus niger and rank species on2026-10-11. That resolves the asserted species ID only. No culture accession was invented. No new schema field or importer is necessary.

## Additional evidence inspected but not admitted as new mechanism

[Jing et al.2022](https://doi.org/10.1021/acsomega.2c03413), PMCID PMC9608414, was acquired as complete original [EuropePMC JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9608414/fullTextXML) and its [supplementary-file ZIP](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9608414/supplementaryFiles). Full body/captions and all six main original JPEG figures were inspected, followed by all13 original SI pages (nine figures and one primer table). The primary PDF was not acquired; complete JATS was read instead. Exact raw/derived hashes and failed routes are in the companion JSON. The study concerns Jiangxi natural kaolin and separately synthetic Fe2O3; it does not test the Turkish ore or the same fungus.

The bacterial experiment uses source-named B.cereus UKMTAR-4 and S.aureus NCTC6571,1g kaolin/50mL,160rpm,unquantified room temperature,14days,triplicates and4% daily sample withdrawal. It measures phenanthroline-reactive Fe(II); total feed iron is operationally measured after37%w/v HCl treatment for12h plus hydroxylamine. Residual-solid and solution measures do not directly establish a complete mass balance or particular iron phase. Carbon/nitrogen medium composition strongly changes pH and response. Synthetic Fe2O3 results must not be transferred to the natural kaolin arm.

Admission is deferred because the paper's promised uninoculated controls are not separately displayed in the inspected main or SI figures, quantitative removal accounting is not explicit, and growth plots labelled log10 CFU/mL reach roughly16–18 (main Fig1 and SI FigS1), requiring clarification rather than literal curation as credible cell density. The Methods' unusual dilution wording also needs reconciliation. Main B.cereus Results report70.3% removal for0.1LB-starch, not52.0%; the latter was an erroneous preliminary working note and is not in the accepted record. Fe(II) time courses are transient and sometimes below zero, so maximum concentrations and reported removal percentages are not interchangeable. Medium names/recipes also differ between prose and figure labels. qPCR, CAS response, biofilm staining and SEM association do not establish unique gene or siderophore causality without perturbation evidence. A future qualified bacterial extension needs explicit decisions about these source defects, not an automatic import.

[Štyriaková and Štyriak2000](https://www.ceramics-silikaty.cz/2000/pdf/2000_04_135.pdf), seven-page publisher PDF, was acquired and text inspected through the early discussion; not all original pages/figures were independently inspected, so it remains research-only. It studies mixed Slovak natural feeds, not the Turkish feed. Table1 oxide-equivalent versus Table2 elemental labels differ; the reported KS2 initial1.43/residual1.29 cells imply approximately9.8%, whereas15% is printed. KS3 abstract/body53%/52% also differ. Do not silently repair or pool these results. Further full visual review and control/denominator reconciliation are needed.

Hajihoseini and Fakharpour2019 [10.1080/21870764.2019.1571152](https://doi.org/10.1080/21870764.2019.1571152) publisher PDF/full text returned403. Arslan and Bayat2009 [10.1346/CCMN.2009.05706011](https://doi.org/10.1346/CCMN.2009.05706011) UAB repository item is explicitly institution-restricted; no bypass attempted. Neither abstract's numeric claims were admitted. Maurice2001 kaolinite papers and Zegeye2013 are follow-up leads, not inspected evidence.

## Search, notices, access and reuse

Web searches on2026-10-11, first returned result sets with no exhaustive pagination:

- `kaolin bioleaching Aspergillus iron removal full text primary study`
- `kaolinite microbial dissolution mineral bacteria primary experimental study`
- `"Elucidation of Iron(III) Bioleaching Properties of Gram-Positive Bacteria" doi`
- `"10.1080/21870764.2019.1571152" correction retraction`
- `"kaolin" "bioleaching" "abiotic" "Aspergillus" controls`
- `site:acs.figshare.com "Elucidation of Iron" "Bioleaching"`
- `"ao2c03413_si_001.pdf"`
- `"Iron removal from kaolins by bacterial leaching" correction erratum retraction`
- `"10.35354/tbed.592519" erratum correction retraction`
- `"10.1021/acsomega.2c03413" correction retraction`
- `site:ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi "Aspergillus niger" "5061"`
- `"Staphylococcus aureus" "NCTC 6571" "ATCC 9144"`

No correction/retraction was identified in these bounded title/DOI searches or in the returned Kale/Jing Crossref update fields; this is not an exhaustive notice-clearance claim. Different feeds and organisms give conflicting apparent effectiveness and cannot be pooled into universal kaolin performance. The independently investigated mining discard study preserves weak biological removal rather than importing the higher natural-feed result.

Bulk PDFs/XML/JPEGs/ZIP and derived renders remain outside Git under `/private/tmp/cmm-round31-kaolin-research`. Kale Crossref did not state a license; do not infer redistribution rights. Jing JATS/Crossref state CC BY-NC-ND4.0; only factual paraphrases/locators and provenance are committed. Failed ACS/PMC routes and an unverified guessed Figshare address produced no accepted evidence; authoritative EuropePMC subsequently supplied original assets. Acquisitions include UTC timestamps, URLs, response status and SHA256. These materials are review inputs, not promised permanently hosted data.

## Disposition

Admit one natural-kaolin resource with the bounded fungal experiment, append one CREATE history, and obtain an independent structured scientific review of exact final bytes. Keep bacterial mechanisms and unavailable papers in the research frontier. Run named validation now and the full batch gates after all independent reviews and corrections. This investigation does not establish source exhaustion.
