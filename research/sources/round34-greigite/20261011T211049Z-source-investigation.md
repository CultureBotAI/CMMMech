# Greigite primary-source investigation

- UTC: 2026-10-11T21:10:49.233173+00:00
- Trusted base: `38cef46aabbcb2b49536ed8c265c63646ff1da3d`; worktree `/private/tmp/CMMMech-expansion-round34-20261011`.
- Decision: curated `data/records/greigite.yaml`, pending independent scientific review.
- Frozen record SHA-256: `ff4d81433f6a854621fa16213167ed62120b7aa73bc0e2dd684e76200c35a8e4`.
- CREATE: `history/records/greigite/2026-10-11T210905Z-codex-c1e0b6.yaml`, SHA-256 `a4aeb2146ae2f930aaf2b02cd9c8928589db36d89b550c89d198b5106eff3e9c`.
- Raw artifacts: `/private/tmp/cmm-round34-greigite-research/raw`. The paired JSON records every retained artifact hash, exact acquisition URL/time/result and the full dedup command.

## Selection and identity

Greigite is IMA-approved Fe2+Fe3+2S4, approval1963-007 (September2026 masterlist, originalPDFpage86). This mineral is distinct from Fe element, poorly ordered FeS, mackinawite, pyrite, magnetite and a mixed precipitate. Two defined Thermococcales laboratory assays offer diffraction-supported extracellular greigite and informative control/detection limits. No criticality claim is made. Live NCBI resolves T.prieurii to species1128108; its2018 strain is not assigned. The2022 methods name KOD1(JCM12380), matching NCBI69014.

## Complete primary evidence and actual access

1. Gorlas etal2018, DOI10.1371/journal.pone.0201549: complete10-page publisherPDF and EuropePMC XML; all five original figures visually inspected, with diffraction specifically Figure2D and latticeimage2E (some prose crossreferences differ). Both original supplementary DOCX files are textual CHESS equilibrium model outputs, read in full; pyrite is allowed inS1 and suppressed inS2. They are not experimental controls. LicenseCC BY4.0.
2. Gorlas etal2022, DOI10.1111/1462-2920.15915: complete archived XML and originalTable1, all six original main figures, all eight original TIFF supplements and full AppendixS1 read/visually inspected. PublisherPDF403; no completePDF claimed. Source-specific original media and table cells establish the retained claims. LicenseCC BY-NC-ND4.0. Initial acquisition basename gorlas2021.xml was corrected to gorlas2022.xml without changing bytes; acquisition1 preserves that history.
3. Later2026 Mariotte etal DOI10.1111/1462-2920.70242: full XML retained and greigite/source-family scope checked. Its primary emphasis is pyrite/FeS and iron-stress response. No greigite measurement is transferred; figures/SI not reviewed for acceptance.

## Mechanism and measurement assessment

2018 T.prieurii cultures (5×10^7cells/mL;5mMFeSO4;85°C;anoxic;through192h) yielded extracellular greigite identified by more than30 electron-diffraction patterns and HRTEM, alongside separate pyrite cells/vesicles and organic/phosphate material. Greigite appeared after96h; no-cell absence is reported. Diffraction/particle counts are not flask replication. Fe/S is only complementary semiquantitative evidence. The oxidant and exact phosphate/cell-material pathway remain unresolved.

2022 KOD1 cultures compared S0 and L-cystine growth sources before5mMFeSO4 addition at85°C. OriginalFigure3 supplies local greigite diffraction/HRTEM in the144h L-cystine arm, while160h bulkXANES does not detect it. Sulfur160h fits contain greigite/pyrite/FeS; originalTable1 printed41/49/11% totals101%. These are fitted Fe-species fractions, not recovered mineral mass or iron conversion. Controls and synthetic reference standards are separate experiments. All main and SI figures were checked, including S6control timing and S8higheriron ATP responses, without assigning unmeasured greigite-specific survival causality.

## Preserved limits and contradictions

- Culture-associated laboratory mineralization is supported; no isolated product, extraction yield, industrial deployment or inherited criticality.
- 2018 mixed bulk assemblage contains pyrite plus extracellular greigite and organic/phosphate material; locally pure nanocrystals do not establish bulk purity.
- 2018 no-cell greigite absence is reported without a quantified phase-control time series; active metabolism versus altered chemistry/debris is unresolved.
- 2018 growth-medium phosphate additions versus discussion of nominally phosphate-free mineralization leave transfer/carryover unclear; Fe/P is not direct Fe-valence determination; oxidant unknown.
- 2022 microscopy identifies sparse L-cystine greigite at144h but bulk XANES does not resolve it at160h; approximate5% analytical detection boundary is not a biological absence.
- 2022 sulfur160h Table1 relative Fe-species fit fractions41%greigite49%pyrite11%FeS sum101%; neither bulk-solid composition nor recovery yield. Table98%versusmethods99.7%confidence conflict is retained.
- 2022 illustrated S6 cell-free control is70h S0; text covers both sulfur-source controls, not a fully shown matched144–160h phase-quantified time series.
- Phosphate release, exclusive precursor pathway and greigite-specific survival causality are unmeasured/proposed. Biological replication of mineralization/phase assays is not supplied by triplicate growth kinetics.
- 2018 and2022 are distinct experiments in one research program, not independent research-group replications.

## Search, deduplication and notices

The bounded search used the eleven exact queries in pairedJSON, web provider,2026-10-11, nofilters and firstresultsets only. ExactDOI/title notice searches and Crossref relations/update fields yielded no notice in that coverage; this is not an exhaustive retraction check. Broader results include2026abiotic greigite transformation,2020thermodynamic work,2011magnetotacticBW-1 and2018Picard sulfate-reducer assays. None is silently merged with these experiments or used to assert universal biogenicity. Packaging owns the separate mackinawite/Picard assessment.

Dedup used rg --no-ignore --hidden --follow across484 declared roots, including both checkouts' records/research/reviews/history and cited raw artifacts. BinaryPDF/images/Office/ZIP files were excluded from textgrep; available extracted text and metadata were searched. Matches were authority rows and contextual citations, not the selected source experiments or a maintained greigite record. Exact command, returncode0, empty stderr and output hash are retained in pairedJSON and local dedup.json/txt. This is a declared-boundary finding, not machine-wide absence.

## Curation handoff and checks

Schema/validator changes were unnecessary. The mineral, extracellular laboratory process, organisms, assay conditions and evidence qualifications fit the current contract. CREATE and inline events are distinct. Named record validation completed exit0:1checked,0failed. Baseline reused exact tested main via /private/tmp/cmm-round34-baseline-reuse.json; no new baseline execution is claimed. Parent owns final cohort/history/review gates and assigns an independent reviewer. Raw primary materials remain outside Git.

## Remaining priorities

Independent review of retained source claims; broader magnetotactic/SRB evidence can later expand this owner after complete source-specific controls and organism identities are verified. Do not convert the reported model fractions into recovery observations or inherit criticality. Newsource acquisition is not needed to publish the bounded two-observation record.
