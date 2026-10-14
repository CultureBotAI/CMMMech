# Round81 resource source investigation

This source assessment is not a completed independent record review. Curated scope is one `secondary_resource`: used photographic fixer solutions, represented by real black-and-white film-processing waste. Raw copyrighted originals and derived full-text snapshots remain outside Git. No criticality claim is made.

## Selection and duplicate boundaries

Pethkar & Paknikar (2003) (DOI 10.1016/S0032-9592(02)00054-7, Process Biochemistry 38:855–860) is the strongest selected primary. It establishes a real liquid feed and a laboratory biological-conditioning/biosorption/chemical-recovery sequence. The material is not the existing solid waste-X-ray-film record or its gelatin-stripping experiments. No root identity ID is invented for this heterogeneous waste.

The current round81 checkout at 623b19fe2ac59b8328d0af3002a6c0da4ee064a7 and main's 384-owner inventory were inspected. Hidden/ignored-inclusive, symlink-following searches covered `data/records`, `research`, `reviews`, `history`, relevant cited `/private/tmp/cmm-round80-resources-research` text/metadata, and the saved three-page all-state issue inventory. `.git` and `.venv` were excluded from scientific text searches. Exact DOI/PII, Pethkar, photographic/fixer and phosphating terms found no existing accepted fixer experiment; broad photographic hits resolve to the preceding film record/report. This is a bounded material/experiment absence finding, not a machine-wide search. The current silver element record uses a separate Shewanella experiment. Automotive treatment sludge has unresolved contributing processes and cannot be equated with isolated phosphating sludge.

## Acquisition and inspection

- The author-shared ResearchGate landing and corrected canonical PDF link expose the complete published six-page original to the web reader. Direct public PDF download and the corresponding CDN PDF returned 403; no local PDF was acquired or hashed. Browser inspection was unavailable because no browser surface was enabled. Web screenshot calls yielded text-only references, so no screenshot inspection is claimed.
- Two raw web-parser output snapshots were preserved. Their merged derivative has all 522 numbered original lines, no missing line numbers and no inconsistent overlaps. It preserves parser/OCR artifacts and is labeled as a generated text snapshot, not original PDF bytes. Title, authors, publication year, DOI, page span, methods, Table 1, all figure captions, results, discussion and references were read.
- All six original publisher GIFs were downloaded successfully from the article's own `ars.els-cdn.com` PII asset routes. Each was visually inspected as an individually expanded PNG derivative. A preliminary composite cropped some graphics and is not the basis for complete figure review. Final individual views preserve the full downloaded image dimensions.
- Elsevier API returned metadata only, despite the response tag `full-text-retrieval-response`; it is not accepted as full text. Crossref verifies 2003 publication; the original's 2002 copyright/acceptance is not a 2002 publication edition. ResearchGate's 2018 upload is a posting date, not a new experiment.
- Current NCBI XML establishes species-level Thiobacillus thioparus 931 and Cladosporium cladosporioides 29917. It does not authenticate MCM B-39 or strain #1, nor authorize transfer from type strains.
- Full original contains no supplementary-material pointer. Exact DOI/title correction, erratum, supplement and conflicting-study searches plus Crossref update/relation fields and OpenAlex retraction metadata identified no direct amendment in this bounded pass. This does not prove that none exists. Citing review text and unrelated model-solution experiments were not promoted to independent replication.

## Claim-level assessment

| Scope | Primary locator | Decision/boundary |
|---|---|---|
| Real used fixer | §2.2 p. 856 | Accepted: black-and-white film-fixer from a local processing unit. Facility identity, sampling date and represented feed variability unknown. |
| Living bacterial pretreatment | §§2.1–2.4 pp. 856–857, Table 1 | Accepted qualified thiosulfate conversion with sulfur/sulfate production before downstream silver removal. Bacterial step itself reports little Ag change. |
| Fungal biomass sorption | §§2.1,2.7 pp. 856–857 and Results pp. 858–859 | Accepted as biomass-bead sorption; no assertion of viable fungal metabolism, defined matrix or molecular binding mechanism. Biomass was harvested, washed and granulated using a proprietary method. |
| Abiotic finish | §2.7 p. 857, Results p. 859 | Cyanide elution followed by 0.8 V/224 mA electrowinning. Source reports 127 mg metallic Ag and 70% overall efficiency, without complete inventory or product-purity/phase characterization. Keep as attributed outcomes. |
| Prepared-solution optimization | §§2.5–2.6, Figures 1–6 pp. 858–859 | Context only; no transfer of synthetic-AgBr optimization to actual-waste removal yields. Figure 2 and Figure 3 plateaus/time ranges differ from textual optimum statements. Figure 4 extends above the Methods' stated 100 mg/L range. Fits are not molecular mechanism proof. |
| Controls/scale | §2.3, entire Results | Uninoculated fixer control stated, separate endpoint not presented. No matched untreated-fixer column, bead-matrix-only series or independent replicate count reported. Column is laboratory apparatus; separate 5 L biomass production is not industrial recovery deployment. |

## Preserved source conflicts

1. §2.2 places 2.8 g Ag/L and 18.5 g thiosulfate/L before 1:10 dilution; Table 1 calls those same initial values a 1:10 diluted sample; §2.7 gives approximately 280 mg Ag/L after pretreatment. No concentration or total inventory is silently reconstructed.
2. Sulfate values differ: abstract 31.2, Results 31.16 and Table 1 final 32.25 g/L. Table 1's `Nil` has no reported detection limit and is not converted to numeric zero.
3. §2.5 eluent ethanol is 1% v/v, Results 10%. Neither recipe is selected as an established optimum.
4. Cumulative column uptake 43 mg/g is labeled biomass in Results, versus per gram beads in Methods. The biomass fraction is unknown. Fitted single-equilibrium Qmax 3.08 mg/g and repeated-contact 45 mg/g are distinct assay definitions, not interchangeable capacities.
5. Five-day fungal biomass is called stationary-phase in Results but late-log in Discussion. The accepted record does not choose one growth phase. No new measurement is digitized from a graph.

## Deferred candidates

- Phosphating sludge: original-specific sources include Kuo (2012) DOI 10.1016/j.jhazmat.2011.11.081 (abiotic vitrification) and LiFePO4-related DOI 10.1021/acssuschemeng.6b02681. They remain metadata leads; no complete original mechanism assessment was made. Phosphating wastewater DOI 10.1016/j.cej.2017.02.112 is a separate liquid feed and cannot be used as sludge evidence. Do not duplicate the unresolved automotive-sludge process scope.
- Bioelectrochemical silver study DOI 10.1016/j.biortech.2012.02.029 uses simulated photographic wastewater; this does not establish real fixer provenance. No record imported.
- Patent US4155810A and Chen (2012) DOI 10.1016/j.apenergy.2012.06.026 are possible future used-fixer sources, not independently accepted experiments in this pass. Neither substitutes for verifying the current study's contradictions.
- ITO-etching wastewater issue 265 remains unresolved; unchanged denied routes were not retried.

## Reuse, schema and handoff

The original states copyright2002 Elsevier, all rights reserved; author sharing is reading access, not redistribution permission. No raw full text, PDF or figure is committed. Only paraphrased curation, exact source locators, URLs and checksums enter the report. No bulk dataset or new importer is proposed. Native concentration observations accept mg/kg cells; these assays' g/L,mg/L,mg/g and process percentages remain qualified prose. Existing recovery process and two organism identities suffice; no schema/validator change is demonstrated.

Completed curation: verified the actual baseline PASS receipt and log hash, created one narrow resource record, appended canonical CREATE and inline history, and ran named strict validation (1 checked, 0 failed). The frozen owner awaits independent scientific review and final batch gates. The planned curator's source check is not the independent review. Source clarification draft `/private/tmp/cmm-round81-fixer-followup.md` requests actual dilution, formulation and mass-balance evidence; it is not a record defect. Other candidates remain deferred rather than filling a quota.

## Actual curation provenance

- Report UTC: 2026-10-14T20:49:29.528771+00:00; researcher: Codex (GPT-6), round68_new_frontier.
- Worktree: `/private/tmp/CMMMech-expansion-round81-20261014`; branch: `curate/cmm-expansion-round81-20261014`; trusted base: `623b19fe2ac59b8328d0af3002a6c0da4ee064a7`.
- Owner: `data/records/used-photographic-fixer-solutions.yaml`; SHA256 `7563b9891d5c3395802edc595210856ed3cf1c317db71503ff34d0a7a4b5fbe9`.
- Canonical CREATE: `history/records/used-photographic-fixer-solutions/2026-10-14T204823Z-codex-6c081d.yaml`; SHA256 `604d2547182660d5e4d0d3215528bb9c0a7818548fc489a11210968633e9d91f`.
- Named command: `uv run --locked cmmmech validate data/records/used-photographic-fixer-solutions.yaml --require-records`; observed exit0 and `Checked 1 record(s); 0 failed.` Log: `/private/tmp/cmm-round81-resources-research/named-validation.log`, SHA256 `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`.
- Baseline: `/private/tmp/cmm-round81-baseline.json`, actual UV sync and just check both0, 317 passed/3 skipped, 384 records/442 histories; log digest independently checked before writing. Final batch gates and independent review are pending.
- Search log, raw acquisition receipts and full file bindings are in the paired JSON; no complete original is redistributed.
