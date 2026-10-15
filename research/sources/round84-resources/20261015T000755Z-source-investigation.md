# Round 84 source investigation: natural silica-sand feed

UTC: 2026-10-15T00:07:55.451400+00:00. Researcher: codex /root/round68_new_frontier (GPT-6; codex).
Worktree `/private/tmp/CMMMech-expansion-round84-20261014`, branch `curate/cmm-expansion-round84-20261014`, trusted base `57b84777066e9c0c43adcc92602dbd1021f52b48`. Research began before the baseline; maintained creation followed the actual successful baseline receipt, completed 2026-10-15T00:05:38Z. The round namespace retains October 14 while these actual artifacts use October 15 UTC.

## Scope and selection

The initial secondary-resource survey considered foundry sand, phosphating sludge and silicon kerf. Full experimental evidence was weaker or previously deferred. With parent authorization, the selected **natural silica-sand feed** is a `primary_resource`: quartz-rich quarry sand/disaggregated sandstone, distinct from quartz species, silicon element, spent casting sand and a purity-defined silica product. One owner is sufficient. No criticality list was assessed or inherited; no schema change is needed.

The accepted evidence is the [official Newcastle thesis](https://theses.ncl.ac.uk/jspui/handle/10443/1346), Sani Yahaya, repository year 2012 and cover/declaration September 2011. Its full 297-page original was acquired, but the scientific scope read here is Chapter 2 relevant methods and Chapter 5 silica microcosms, not every thesis chapter. All fifteen Chapter 5 figures and both EDX tables were visually inspected, together with claim-bearing methods/identity graphics. Source code, raw graphics, query captures and acquisition records remain at `/private/tmp/cmm-round84-resources-research`; exact paths/digests are in the paired JSON.

## Search, identity and lineage

Hidden/ignored-inclusive, symlink-following `rg` searched current records, research, reviews and history, plus cited round 77 resource, round 78 frontier and round 81 resource raw metadata/text. Near owners `kaolin` and `kaolin-mine-waste` were read; neither denotes silica-sand feed. Exact feed names, normalized DOI 10.4314/bajopas.v11i1.16s, handle 10443/1346 and Yahaya were checked. An initial raw path was wrong; its error receipt is preserved and the corrected search used the actual round78-frontier directory, without missing-path errors. No matching owner/study appeared within that bound. The 280-object all-state initial issue inventory likewise had no exact source/feed match. This is not machine-wide or exhaustive literature absence.

Searches combined foundry waste, bioleaching and Acidithiobacillus; silica sand, Shewanella and Yahaya; exact titles/DOIs; and correction/retraction terms. The paired JSON lists every query, providers, dates and bounds. Search-result capture, official repository/Crossref/HAL metadata and current NCBI/JCM authorities are retained externally. No correction/retraction notice surfaced within the bounded exact-title/DOI query and inspected official metadata; this does not prove none exists.

## Accepted evidence and limitations

- **Material:** §2.2.2, printed 31–33/PDF 50–52, Table 2.1 and Figures 2.2–2.3 distinguish purple-red Oakamoor Silica 2 from yellow uncemented Grandcourt Silica 3. Sand 2 XRF composition cannot be assigned to Sand 3. The unutilized Sand 1 collection is not an additional accepted assay.
- **Organism:** current NCBI 24 resolves *Shewanella putrefaciens*, with CIP 80.40 listed among type-material names. JCM 20190 independently lists CIP 80.40 equivalence. This verifies nomenclature, not experimental genome sequencing or chain-of-custody. Other screen cultures remain source-designated context.
- **Assay:** §§2.4.3–2.4.5 and 2.5.7, printed 35–40/PDF 54–59, describe washed viable stationary-phase cells used without growth, saline/lactate medium, N2, near-neutral pH, dark shaking, and HCl extraction before FeII colorimetry. The cell-density Sand 3 experiment used 2.5 g feed, 3.5 or 7 mL stock and 30°C; the AQDS arm used 2.4 g and 4 mL stock. Stock density is not final vessel density.
- **Outcome:** Figure 5.2, printed 111/PDF 130, supports a greater HCl-extractable FeII response with 7 mL cells than 3.5 mL and a lower nonzero blank. Day-one values 0.24/0.12 mmol/L are concentrations, not rates or recovered percentages. General methods alternately describe cell-free and cell-and-donor-free blanks, without fully mapping them to plots. Pure microbial causation over every chemical/control contribution is therefore not claimed.
- **Null/limited effects:** Figures 5.3 and 5.5 show weak early AQDS benefit and modest later differences. Figure 5.4's Sand 2 caption conflicts with surrounding Sand 3 discussion and is excluded from quantitative feed attribution. The 20°C Sand 2 strain screen Figure 5.1 is separate from the 30°C Sand 3 assay and includes low source-designated *S. loihica* response.
- **Endpoint:** unfiltered slurry was mixed with HCl before filtration. The graphs' wording about solution does not make this a dissolved-only Fe measurement. Solid-associated acid-extractable FeII may contribute. No isolated iron yield, complete mass balance or industrial application is established by this accepted microcosm scope.
- **Mineralogy:** Figures 5.10–5.15/Tables 5.1–5.2, printed 121–126/PDF 140–145, show quartz-dominated XRD without an obvious new crystalline product, FTIR changes also in the blank, local EDX Fe nondetection after treatment, and an untreated-only Mossbauer spectrum. These do not prove complete iron removal, a unique iron-bearing phase or before/after oxidation-state conversion. SEM is qualitative.
- **Document version:** the original PDF visibly retains tracked edits and editorial questions, with overlapping numbering. Printed-page locators prevent ambiguous references. Subculture-duration disagreement and disputed kinetic-order discussion are not silently resolved. This limits confidence and motivates a clean-version/journal follow-up without negating the narrower displayed assay observation.

The repository supplies a CC BY-NC-ND 3.0 licence. Raw originals and reading derivatives remain outside Git; maintained records/reports contain original claim-level paraphrases and source locators.

## Related and deferred sources

| Lead | Evidence available | Decision |
|---|---|---|
| [Yahaya et al., journal DOI 10.4314/bajopas.v11i1.16s](https://doi.org/10.4314/bajopas.v11i1.16s) | Indexed abstract and verified Crossref/HAL metadata; AJOL public landing returned 202 with empty body; HAL supplied no fileMain_s | Full journal original still needed. Its 17.6% / 117 mg Fe2O3 per 100 g claim is **not** imported. Issue 2018 and online 2019-02-07 are distinct dates. Likely shared thesis lineage, not independent replication. |
| [Jadhav et al. casting-sand metal reclamation](https://dergipark.org.tr/en/download/article-file/2885650) | Conference-abstract lead 2250/p39; no complete methods/SI verified | Defer quantified recovery. |
| [Fungal-treated foundry-sand concrete](https://doi.org/10.1016/j.conbuildmat.2012.07.112) | Discovery metadata only in this pass | Do not transfer concrete outcomes to purified sand recovery. |
| [Phosphating sludge](https://doi.org/10.1016/j.jhazmat.2011.11.081) | Prior round 81 abiotic lead | No new microbial original accepted; no repeat of unchanged blocked route. |
| [Silicon kerf](https://www.mdpi.com/2313-4321/9/4/66) | Prior round 78 query and current abiotic lead | Outside selected one-owner scope. |

A web-open of a guessed AJOL download suffix failed; it is explicitly not a verified article-file URL or evidence that no official PDF exists. One sandbox DNS failure preceded successful public metadata/authority retrieval; both receipts are retained. No access controls were bypassed.

## Curation handoff and next priorities

Created `data/records/silica-sand.yaml`, SHA256 `5bbd5618ce6bb4cdf9738e4fe16386517e204ac6752abd6182b2e4864d356808`. CREATE sidecar `history/records/silica-sand/2026-10-15T000631Z-codex-5ebae5.yaml`, SHA256 `758091b4637338784a053e4608b099e8c3ab14e043ad416e2b38c558ed2d5bdc`, with distinct inline provenance. Named strict validation passed 1 record / 0 failures. Independent iron-agent review and root batch gates remain pending at this report time; this source report is not scientific acceptance.

1. Independently review this narrow owner against exact original pages and final hashes.
2. Acquire the full journal article/any supplement through a legitimate publisher or repository route and determine its overlap with the thesis, actual feed and denominator; obtain a clean thesis revision if available. Preserve both source versions rather than overwriting acquired bytes.
3. Only after separate complete assessment consider the thesis's 4.5 L reactor chapter and product-quality claims. They are excluded from the current accepted microcosm mechanism.
4. Resume the foundry-waste candidate only when full experimental evidence is available; no arbitrary extra resource record is justified now.
