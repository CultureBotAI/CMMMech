# REE phosphate source investigation

- UTC: 2026-10-15T21:22:04.460040+00:00
- Curator: codex, GPT-6, codex.
- Worktree: `/private/tmp/CMMMech-expansion-round103-20261015`; trusted base `44d5b468519eb862b32ef54bf7c066bc0f79ba62`.
- Scope: two distinct mineral species, with bounded abiotic laboratory transformations. This dossier is a curation handoff, not independent acceptance.
- Baseline: coordinator `just check` passed at 21:16:41Z, receipt `/private/tmp/cmm-round103-baseline.json` (SHA-256 `055301d51e660aa998823e6e0dff120958d594c6fcca0cd3d7d03a73de04245d`).

## Ranked selection and ownership

1. **Rhabdophane-(Ce)**: `data/records/rhabdophane-ce.yaml`. IMA identity plus the full 2024 controlled replacement study and analytical supplement make a useful Ce-specific transformation record.
2. **Rhabdophane-(La)**: `data/records/rhabdophane-la.yaml`. IMA identity, corrected natural microprobe/Raman context and the full 2018 synthetic thermal study support a distinct La owner.

No element identifier, commodity designation or criticality status is transferred to either mineral. IMA page 184 lists Ce as Rn/1966 s.p. and La as Rn/1987 s.p.; these are nomenclature entries, not numbered approval IDs. Current ideal formulas contain one water, while the experimental powders have preparation-specific total-water estimates and fitted structural models.

## Search, deduplication and provenance

Hidden and ignored files and relevant symlinks were included across records, research, reviews and history, then cited local research/raw roots. The external receipt `/private/tmp/cmm-round103-ree-research/dedup.json` preserves exact command, matches, errors and boundaries; SHA-256 `fabfddf97f13246e33c994b4778aba4fb7e816b2bb63d2678ec01abedea412b1`. Three prior owner hits (`xenotime-concentrate`, `churchite-y`, `neodymium`) describe comparison or mixed material, not either distinct species. The older round37/39/40 dossiers and their referenced raw evidence were checked; no absence is asserted for binary PDF content not represented by extracted text. The current supplied open-issue title/body inventory has 105 entries; #130 and #133 remain evidence gaps.

The paired JSON logs all exact search queries, bounded coverage, successful downloads and failures, artifact hashes, source roles and adoption decisions. Public full originals were acquired legitimately; raw PDFs, spreadsheets and XML remain outside Git at `/private/tmp/cmm-round103-ree-research`. HTTP-success content was checked as the expected file type. Crossref confirms the 2024 PII `S0009254124003875`; guessed earlier PII/landing routes were not treated as source identity. Official erratum metadata and full publisher correction were verified. Reading access is not blanket redistribution permission.

## Accepted primary evidence and limits

**Bamforth et al. (2024), DOI 10.1016/j.chemgeo.2024.122307.** Complete 17-page original, all experimental figures/tables, methods and discussion, plus `mmc1.xlsx` were inspected. Figures 2–3 and Table 1 support Ce-rich rhabdophane replacement at 180 degrees C/8 hours: nominal-pH-1 phosphoric acid gives 98.6% relative crystalline replacement versus 6.4% in hydrochloric acid. These are fitted phase fractions, not recovered cerium yields. The eleven preparative runs supply pooled material, not eleven replicates per condition. Microscopy supports dissolution/precipitation; Figure 9 is a proposed pathway. Figure 10 and section 4.3.2 show why porous monazite and rhabdophane cannot be distinguished by low microprobe totals alone. The analytical workbook contains standards/limits and elemental WT% cells with computed oxygen; repeated sample labels and section headings preclude treating physical worksheet rows as unique specimens. No quantitative import was made.

Unresolved source conflicts are retained in the owner: section 2.1.2 says 20 +/- 0.1 mg, while Table 1 lists 20.9–21.1 mg; section 3.1 says pH-3 conversion below 5%, while Figure 3 labels 4.4/4.7/6.4%. The source's complete-replacement prose is narrowed to the numerical near-complete values. The printed Equation 2 water coefficient is not imported as a balanced reaction.

**Shelyug et al. (2018), DOI 10.3389/fchem.2018.00604.** Complete 11-page original, Figures 1–10/Tables 1–5 and supplementary Tables A1a–c/A2 were checked. La-specific preparation, 200 mg/1100 degrees C/6-hour air treatment and PXRD support the thermal conversion. La 0.804 and Ce 0.732 water coefficients include adsorbed and structural water, not resolved site occupancy. The study reuses the Mesbah 2017 material series. General water-content and temperature-trend wording conflicts with tabulated/graphical data, so those trends are not adopted. The transformation is irreversible in this experiment; no exact equilibrium threshold is inferred. The Ce Table 5 Gibbs-energy uncertainty spans zero; no universal stability claim is adopted. Oxidation in the calorimetric solvent is separate from initial phosphate valence.

**Ondrejka et al. (2018), DOI 10.1180/mgm.2018.137, and the 2019 erratum DOI 10.1180/mgm.2019.13.** The complete 24-page natural study, Figures 1–10/Tables 1–6, methods and relevant discussion were inspected. Natural Velence Hills grains include La-dominant members but are compositionally zoned and substituted, with some Nd-dominant analyses in the generally La-rich group. Raman supports group/phase discrimination but does not individually measure every grain's hydration; no universal pure end-member assay or microbial experiment is inferred. The actual 2019publisher correction says Fe must be included in formula calculations while not defining a valid Fe end-member. This supersedes the erroneous p.1296 wording. No separate supplement is cited in the inspected original; publisher-wide absence was not asserted.

## Contradictions, adjacent work and rejected transfers

The full 2024 Dy 3D-electron-diffraction paper (DOI 10.1107/S2053229624007885; original 8 pages, Figures 1–5/Table 1) favors a trigonal average model with disordered water. It studies synthetic Dy, so its result is not an automatic reclassification of Ce or La. Its SI ZIP timed out and official CIF/PDF links returned403; detailed water modeling is not adopted. The 2021 natural Ce conference structure lead's official PDF route returned404; unread formula/symmetry claims are not imported.

The 2025 vivianite study DOI 10.1039/D4RA08110B was text-screened from full XML; supplementary assets were acquired, but original graphics/SI remain unassessed for admission. It uses mixed La/Ce/Pr/Nd/Dy solutions and group-level phase labels. It is a useful future lead for a distinct material/phase investigation, not an established Ce- or La-specific microbial experiment. RSC PDF returned403.

Existing #130 (2010 yeast Ce phosphate) remains unresolved: monazite-like labels and the later 2017qualification do not establish rhabdophane. Existing #133 concerns Sm with original-graphics and protocol gaps; it supplies no Ce/La mechanism. These historical failed routes were not blindly retried. The bounded current correction search located the real 2019erratum; no additional formal correction/retraction was located for the adopted experiments, which is not an exhaustive absence claim.

## Curation handoff and remaining work

The two owners have canonical CREATE histories and actual inline events. No schema or validator change was needed. Independent reviewers must inspect exact frozen bytes, primary evidence, source conflicts and limits; final corpus/history/review gates remain the coordinator's responsibility. Named validation is separately captured in the external freeze receipt.

Next priorities: source-level clarification of 2024 loading/pH-3 conflicts; 2018 trend wording; natural Ce 2021 original and Dy 2024 supplements before structural generalization; full 2025 mixed-REE review; and missing microbial primary evidence in #130/#133. None of those gaps warrants inventing measurements, hydration, microbial causation or industrial recovery.
