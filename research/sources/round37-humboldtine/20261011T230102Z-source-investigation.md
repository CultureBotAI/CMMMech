# Humboldtine source investigation and curation handoff

UTC: 2026-10-11T23:01:02.298600+00:00. Curator: codex, GPT-6, codex (`/root/round27_superalloy`).
Worktree: `/private/tmp/CMMMech-expansion-round37-20261011`.
Trusted base: `dcfbedb78bfd682ad06f2ff4517241f490e4f401`.
This is the author's source dossier, not an independent scientific review.

## Decision and identity

Add one mineral owner, `data/records/humboldtine.yaml`. The IMA September 2026 list gives Fe2+(C2O4)(H2O)2, status G and year 1821 (original PDF page 97). Its introductory key identifies G as grandfathered and 1821 as the original-description year. Humboldtine is distinct from iron, other oxalates and the siderite- or pyrrhotite-bearing experimental feeds. No criticality designation or invented mineral CURIE is added.

Two complete primary articles support bounded laboratory formation: [Zelenskaya et al. (2021)](https://doi.org/10.3390/cryst11121591) and [Vlasov et al. (2023)](https://doi.org/10.3390/cryst13030432). Official publisher PDFs and XML were acquired. All five original 2021 figures and all seven original 2023 figures plus Tables 1–5 were inspected. Complete PDF/XML inspection found no declared supplementary material; this does not rule out undisclosed data. Both articles state CC BY 4.0. Raw full text and images remain outside Git.

## Search and duplicate boundary

`raw/dedup.json` preserves the exact `rg --no-ignore --hidden --follow` command, 120 resolved roots, timestamps and 26 hit lines; exit 0, no stderr. It covers current worktree and original checkout records, research, reviews and history, their existing referenced CMM research/raw directories, and this task's raw directory. PDF, image, Office and ZIP binaries were excluded from the text scan; retained extracted text and metadata were included, and the selected original PDFs were inspected separately. This is not a machine-wide absence claim.

Matches were existing IMA/research citations, the round 36 frontier and a deferred 2023 source lead. No existing humboldtine record or accepted claims from these experiments were found within that boundary. Similar feed localities do not establish identical individual specimens. A shared paper may support multiple mineral owners; its PDF, XML and figures are not independent experiments.

## Evidence assessment

| Primary study | Supported humboldtine evidence | Essential boundary |
|---|---|---|
| 2021 A. niger Ch 4/07 | Figure 1 shows day-five siderite and day-seven altered-pyrrhotite PXRD; Figures 2–3 show morphology. Figure 4 and Results report no iron-oxalate crystals in uninoculated controls. | Day-three pyrrhotite prisms are preliminary SEM/EDX evidence, not a day-three diffraction confirmation. Controls have no quantitative phase balance. |
| 2023 S. himantioides LE-BIN 1368 | Table 4 assigns humboldtine by SEM/EDX and PXRD on both iron feeds; Figures 6b–c show crystals. | Substrate reflections remain; no isolated product purity or yield. |
| 2023 C. puteana LE-BIN 1370 | Table 4 assigns humboldtine by both methods on pyrrhotite, with calcium oxalates also reported by PXRD. | Siderite assignment is microscopy/EDX only; the PXRD cell is a dash. |
| 2023 source-named A. xantha LE-BIN 1029 | Table 4 and Figure 3f support humboldtine on siderite. | Pyrrhotite instead has whewellite. Figure 7b labels whewellite with humboldtine on siderite, whereas Table 4 lists only humboldtine. |
| 2023 S. lacrymans LE-BIN 1192 | Tested comparator. | Both iron-feed arms have dashes, including pH: not invented zero yields or permanent biological incapacity. |

The 2021 methods specify autoclaved heterogeneous rocks and Czapek-Dox medium, 15 mL, initial pH 5.5, room temperature, triplicates and 3–18 days. Medium FeSO4 supplies some iron; a no-rock control and iron-source balance are missing. No killed-biomass, cell-free-metabolite or matched-pH series isolates the causal step. The later pH 3.5 ± 0.5 is called an initial value in Results, although Methods begins at 5.5; this wording difference is preserved.

The 2023 assays use 20 mL liquid glucose-peptone medium, approximately 1 × 0.5 × 0.5 cm blocks, initial pH 5.5, room temperature, triplicates and 30 days. The agar formulation includes iron; the liquid recipe is not separately tabulated. Controls are described, but no separate iron-arm control outcomes or phase plots are supplied. Inoculum density and substrate sterilization are unspecified. The comparison with A. niger relies on earlier studies with different media, volumes and durations. It does not establish superior rates or recovery.

Neither article provides the iron/oxalate mass balance, redox time series or independently varied impurity controls needed to establish the proposed molecular and kinetic explanations. Product morphology, mixtures and endpoint assignments do not establish complete conversion, isolated recovery or industrial use.

## Counterevidence and notice checks

The 2021 field search found no iron oxalates in the studied lichen-dominated iron-ore biofilms and reported goethite instead (Section 4, Figure 5). This limits environmental transfer without refuting the laboratory phase evidence. The 2023 field Figures 1–2 concern calcium oxalates, not humboldtine. Earlier disputed lichen iron-oxalate assignments cited by the 2021 Introduction are not accepted from secondary descriptions.

Exact queries and coverage limits are in `raw/search-log.json` and the paired JSON. DOI correction/retraction searches and live Crossref update/relation checks found no relevant notices within the returned result sets. This bounded result is not a guarantee of absence. Abiotic humboldtine synthesis and hematite–oxalate studies surfaced as useful future leads; their measurements were not imported because their original methods and figures were not independently inspected this round.

## Identifiers and acquisition provenance

Live official taxonomy XML verifies species IDs 5061, 80602, 80637, 85982 and 1333629. GenBank KF768341.1, KY352492.1, KY433978.1, KY433983.1 and KY352493.1 match the reported strain labels. These are ITS/ribosomal sequences, not strain TaxIDs, genomes or independent culture authentication. Taxonomy XML and KY433983.1 use Amyloporia xantha. The browser heading agrees but its current-name field retains Antrodia xantha; the record states the discrepancy.

Publisher landing pages returned HTTP 403 directly and 429 through the web reader; official PDF/XML routes succeeded. Two GenBank requests returned transient 429 responses; a spaced sequential retry succeeded. Acquisition receipts 1–4 retain URLs, actual UTC times, status, bytes and hashes. The IMA PDF was reused from round 33 with its original provenance and hash; it was not freshly downloaded. A live check confirms the authority homepage links to the September 2026 edition. Its reuse terms are CC BY-SA 3.0.

The paired JSON lists all 62 raw artifacts, sizes and SHA-256 hashes under `/private/tmp/cmm-round37-humboldtine-research/raw`. `inspection.json` records full-text and original figure/table coverage. No bulk source file is committed.

## Frozen handoff and checks

- Record: `data/records/humboldtine.yaml`, SHA-256 `537b5a65c0bc55bd9d59da264df9d22a2651cb759fc68331ec69bb2e339e86a7`.
- CREATE: `history/records/humboldtine/2026-10-11T225911Z-codex-2e6da1.yaml`, SHA-256 `44474d03e0728e4b4a73eb39a2ee6106735b17564ea714e67b077b8b778a334d`. Actual actor/model/tool and a distinct inline event are recorded.
- Parent baseline receipt `/private/tmp/cmm-round37-baseline-terminal.json` was read and its log hash verified: exit 0, 308 passed, 3 skipped, 200 records and 231 histories.
- Named validation passed: `Checked 1 record(s); 0 failed.` Actual session 56560; captured terminal receipt in `raw/named-validation.json`.
- Independent review and final cohort gates are pending at this dossier timestamp. No self-approval is asserted.
- No schema, validator, governance, README or unrelated record changes.

## Next priorities

Independently review the frozen scientific record. Further mechanistic work would need matched chemical controls and quantitative iron/oxalate balances. Other oxalate arms from the 2023 paper should remain under separately coordinated mineral owners and should not be counted as independent replication of this experiment.
