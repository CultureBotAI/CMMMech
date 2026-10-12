# Round 49 zirconium and hafnium mineral source investigation

- UTC: 2026-10-12T06:48:55Z; researcher: codex (GPT-6; codex), baddeleyite curator, not its independent reviewer.
- Worktree: `/private/tmp/CMMMech-expansion-round49-20261012`; branch `curate/cmm-expansion-round49-20261012`; base `b701555aa8b06a51f94a4d97bed7f3ebf96ab439`.
- Scope: natural baddeleyite identity and bounded hafnon assessment. Zircon-sand and eudialyte feeds belong to the parent investigation. No criticality lists or microbial assays were curated here.
- The exact unchanged-base baseline is reused through the initialization receipt. I ran named validation only; parent full gates and independent review remain separate.

## Selection and decisions

| Candidate | Evidence actually inspected | Decision |
|---|---|---|
| Baddeleyite, ZrO2 | Current IMA pages 1–2 and 19; complete official Huraiová et al. (2011) PDF, all eight pages, Figures 1–5 and Tables 1–2; complete Handbook page | Curated one mineral owner with bounded natural-specimen context; independent acceptance pending |
| Hafnon, Hf(SiO4) | Current IMA page 88, complete Handbook page, original 1974 publisher abstract/metadata and Crossref | Deferred: complete natural original unavailable; synthetic 1982 structure cannot substitute |
| Baddeleyite 1959 structure | IUCr issue and Crossref metadata for DOI 10.1107/S0365110X59001530 | Deferred structural extension: official full PDF unavailable |

## Duplicate checks and search boundaries

The hidden/ignored-inclusive, symlink-following searches covered `data/records`, `research`, `reviews`, and `history` in this worktree and the user's original checkout, then all 177 existing raw/research/evidence roots cited by their textual files. The cycle-aware inventory read 3,786 metadata/text files with no read errors. The owner search found neither baddeleyite nor hafnon before creation. Prior round 47/48 mentions are discovery leads; other matches concern IMA or resource context. No matching 2011 experiment or 1959/1974 DOI appeared in these text results.

Nine referenced historical raw roots were unavailable; exact paths appear in the JSON. Text-bearing extensions were searched, without decoding every PDF, image or archive. This is not a machine-wide absence claim. The final pattern adds the accepted 2011 title/URL and 2013 hafnon DOI. Commands, return codes, scopes and hit logs are hash-pinned in the JSON. Exact web queries, returned-result bounds and all direct acquisition receipts are also preserved there. No systematic pagination was performed.

## Accepted primary evidence and limitations

[Huraiová, Hurai and Konečný (2011)](https://www.geology.sk/wp-content/uploads/2019/10/MS_3_2011_04_Huraiova-et-al.pdf), *Mineralia Slovaca* 43:255–262, is an original natural-occurrence study hosted by the Slovak state geological survey and linked from its [issue contents](https://www.geology.sk/mineralia-slovaca-3-2011/). No DOI was resolved. Received, revised and accepted dates are 5, 12 and 13 September 2011; the 2019 URL directory is not its publication year.

The complete article is Slovak with an English abstract, figure/table captions and final summary. I read the complete extracted text and viewed every original page. Figure 1 locates the maar. Figure 2 shows CL/BSE textures of a zoned zircon with baddeleyite in pockets and its reaction rim. Table 1 and Figure 3 concern accessory phases; Table 2 distinguishes six representative baddeleyite analyses from host-zircon analyses 6 and 7. Figure 4 compares baddeleyite chemistry, and Figure 5 concerns host zircon. No new diffraction refinement is reported. Methods specify a Cameca SX-100, 15 kV, 40 nA and a 2–5 µm beam for minerals; analyzed melt used different conditions. No supplement callout or separate data link was seen in the article or issue page. That is a bounded inspection, not a portal-wide absence claim.

Table 2 (page 259) labels ZrO2 and HfO2, supporting specimen ranges of 96.65–98.27 and 0.99–1.06 wt.%, respectively. The text on page 258 abbreviates those oxide-equivalent quantities with element names; the record preserves the table denominator. The table's minimum TiO2 is 0.41 wt.%, while the text says 0.44; table Ti reaches 0.015 apfu while the text says 0.012. Those conflicting Ti ranges are not imported. The six analyses are not six deposits. The source's LREE-absence wording is limited by stated 0.01–0.05 wt.% detection limits; zeros are not imported as quantitative observations. The proposed reaction with Si-poor, Al-rich melt is geological interpretation, not a controlled transformation assay. This evidence does not establish microbial mechanisms, recovery or deployment.

The [official September 2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), freshly acquired from the homepage link, confirms baddeleyite, ZrO2, G, 1893, Sri Lanka on PDF page 19. The year is not a unique accession. The Handbook's monoclinic identity is secondary context; its cell parameters are explicitly synthetic and were not assigned to the 2011 specimen.

## Deferred evidence and priorities

1. **Hafnon:** official DOI 10.1007/BF00399111 resolves to Correia Neves, Lopes Nunes and Sahama (1974), 48:73–80. The observed PDF link returned subscription HTML despite HTTP 200; the acquisition is explicitly marked `pdf_magic: false`. The publisher's March 1974 issue and August 1974 received date conflict. Current IMA page 88 gives Hf(SiO4), A, 1974-018. Secondary Handbook natural chemistry does not replace the missing original. Historical terminology using more than 90 mol.% hafnium component requires reconciliation with current species naming; current IMA confirms the ideal species formula but does not by itself settle every solid-solution naming rule. DOI 10.2138/am.2013.4494 is a second natural-study lead, discovered only; public ResearchGate pages request the full text. Obtain complete original text, graphics, tables and any supplements before curation.
2. **Baddeleyite 1959:** Crossref supplies the official IUCr `a02573` PDF route. Direct acquisition returned 403 and the web reader returned 401; no original measurements were used. An earlier guessed `a02602` route returned an internal error and has no evidentiary role. Avoid repeating unchanged failed routes.
3. **Independent review:** verify the current record, natural-study Table 2, oxide basis, detection limits and IMA row before acceptance. No source-specific correction or retraction was found in the bounded returned search results. An unrelated retracted Tall el-Hammam paper does not concern this study.

## Provenance, reuse and actual checks

Raw originals, renders, web snapshots and receipts remain under `/private/tmp/cmm-round49-zr-research`. The paired JSON inventories 53 artifacts with SHA256 and byte counts. IMA page 2 states CC BY-SA 3.0; the Handbooks are all rights reserved. No permissive article redistribution license was identified in the 2011 PDF or landing page, so no raw original is committed. Publisher reading access is not a redistribution grant.

- Record: `data/records/baddeleyite.yaml`; SHA256 `3aa47a953cda6634ef1e4e874a4fd5395e5245340c87d434ea0a52eaeb77f81e`.
- Actual canonical CREATE: `history/records/baddeleyite/2026-10-12T064522Z-codex-e5337d.yaml`; SHA256 `2c1e0dab0f7098b5905906651f3df3f3103e87612509f3bce21a0c47a962a5fc`. The inline creation event remains distinct.
- Named validation: actual exit 0, `Checked 1 record(s); 0 failed.` No schema, validator or test changes.
- Independent scientific review and full cohort gates are pending at this dossier timestamp; this source assessment is not an acceptance review.
