# Round49 indium mineral source investigation

Recorded UTC: 2026-10-12T06:53:08.296477+00:00
Curator: codex / GPT-6 / codex (`/root/round27_superalloy`).
Worktree: `/private/tmp/CMMMech-expansion-round49-20261012`; trusted base `b701555aa8b06a51f94a4d97bed7f3ebf96ab439`.

## Decision and identity

Add [yanomamite](../../../data/records/yanomamite.yaml) and [cadmoindite](../../../data/records/cadmoindite.yaml) as distinct mineral identities with qualified natural-specimen context. These two original descriptions supply substantial composition, diffraction and occurrence evidence. They do not supply microbial treatment experiments, recovery yields, industrial deployment or dated jurisdictional criticality claims. Indite and the Charrier2022 lead remain deferred. Mineral identity is neither elemental indium nor a bulk resource; natural geological replacement or fumarolic precipitation does not define industrial waste.

The freshly acquired [IMA September2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) was inspected at original pages1–2,34 and237. Cadmoindite is CdIn2S4, approvedA, IMA2003-042. Yanomamite is In(AsO4)(H2O)2, approvedA, IMA1990-052. Exact official labels and identifiers are represented in the records. Current authority status is separate from the publication dates1994 and2004.

## Acquisition breakthrough and exact boundaries

The prior legacy RRUFF routes remained unsuitable: changed academic-host routes timed out; old `rruff.info` direct routes refused connection; `rruff.net/uploads` variants returned404. The legacy web redirect searched a PDF filename as a mineral name, returning no records; that is a migration/search mismatch, not evidence that the publication is absent. The public [RRUFF reference interface](https://www.rruff.net/odr/rruff_reference) exposed its normal reference-title search (`dt_id=734`, ArticleTitle field7036). Actual title results supplied ordinary public download links. No authentication or access-control bypass was used.

- **Botelho etal.1994:** [DOI10.1127/ejm/6/2/0245](https://doi.org/10.1127/ejm/6/2/0245), EJM6(2),245–254; [public original PDF](https://www.rruff.net/odr/view/downloadfile/68222), reference record616849. Acquired200 at2026-10-12T06:45:59.998523Z,901864bytes, SHA256`46cf9ce71181752f278262a8c0a8aaad25f7aae16d9a228056d18dd95d8d45bd`.
- **Chaplygin etal.2004:** ZVMO133(4),21–27; [public original PDF](https://www.rruff.net/odr/view/downloadfile/72003), reference record620642. Acquired200 at2026-10-12T06:45:59.926366Z,471642bytes, SHA256`573f3cb7341594c0e2d90416ff532c66e7826df9d5ef1eff36772c8e3f844e18`. The [official journal metadata](https://zrmo.org/archives/2004/vyipusk-4/cadmoindite-cdin2s4-a-new-mineral-from-kudriavy-volcano-iturup-isle-kurily-islands.html) independently agrees on authors, language, volume and pages. No DOI was invented.

Both PDFs were verified by magic/content and include all original pages. Local full PDF and all page renders were personally inspected; author-platform extracted text is not substituted for missing graphics. Complete originals, public reference-file listings and official article metadata expose no separate supplement in this inspected boundary. No unseen SI is claimed inspected. Publisher access does not establish redistribution rights: copyrighted originals, complete text and images remain outsideGit.

The two official Handbook PDFs were acquired and their complete one-page originals viewed. Yanomamite is version1/copyright2001–2005; cadmoindite explicitly says revisedJuly27,2015. The originalIMA PDF is September2026, not the incorrect first guessed subdirectory that returned404. Every attempt, including failed or zero-byte artifacts, has status/time/hash in the pairedJSON.

## Primary evidence and limitations

### Yanomamite

All ten pages245–254, Figures1–6 and Tables1–4 were read and visually inspected. Figures1–2 give locality and interpreted paragenesis; Figure3 shows natural mixed-mineral textures and scorodite coating; Figure4 is a semiquantitative elemental traverse; Figure5 shows Fe/In compositional relations; Figure6/Table4 compare cell volumes across natural and synthetic compounds. Table1 reports twelve microprobe spots, standards, analytical settings and calculated water. Tables2–3 explicitly separate natural single-crystal/powder measurements from synthetic comparators.

The three selected natural single crystals still contained minor scorodite; the selected powder material showed no significant scorodite reflections. Those are different specimens/method observations, not a universal purity claim. Water was not measured directly because of impurities. The original abstract says crystals are always coated, while page248 says often; the record describes observed intergrowth/coating without selecting an unsupported prevalence. Calculated density is3.876(3)g/cm3 onpage248 but3.882 in the Gladstone–Dale discussion onpage250; density is not imported. Empirical composition and ideal mineral formula remain distinct.

The original discussion explicitly calls origin speculative, compares supergene and hydrothermal hypotheses and prefers the latter in association with the principal cassiterite stage. It does not directly establish the indium source, transport, temperature or reaction mechanism. The Handbook's geological secondary-mineral wording and a later overview's supergene terminology are not evidence of microbial causality or a processing-waste identity. Earlier1990/1992 descriptions and later overview citations may reuse the occurrence; they are not counted as independent experiments. IMA's second reference, J.Chem.Cryst.31(2002),45, is a future bibliographic/full-source follow-up rather than an imported refinement claim.

### Cadmoindite

All seven original pages21–27, Figures1–3 and Tables1–3 were read and visually inspected. Russian text was checked against the printed English abstract/captions; no outside translation service is asserted. Figure1 locates the volcano; all four Figure2 SEM panels show crystals and assemblages; Figure3/Table1 show reflectance. Full Table2 contains fifteen electron-microprobe analyses, empirical formulas and a separate theoretical end member. Table3 separates natural cadmoindite powder diffraction from synthetic CdIn2S4 and historical indite data. FirstauthorI.V.Chaplygin agrees between full original and official journal; the secondary2006 AmericanMineralogist names summary's S.V. initials are not used.

Natural grains contain Fe/Zn and smaller Ge/Se contributions and coexist with other phases. Grain compositions are not bulk fumarolic-crust grades; the introductory51-sample crust values are citations to another work and are not imported. Sampling approximately15–30cm below the crust at outgoing-gas450–600°C is field context, not a directly observed crystallization interval or biological incubation. Proposed chloride breakdown during cooling follows occurrence, cited gas modelling and synthetic analogies; no controlled natural-mineral transformation experiment is reported. Synthetic semiconductor uses do not establish recovery or deployment of this mineral.

Two source details remain unimported: the abstract labels the3.87Å reflection002 whereas Table3 labels it220; reflectance methods mention420–700nm while Table1/Figure3 include400nm. Neither discrepancy affects the narrow formula/identity/context record. No reflection-index or reflectance-value claim is curated.

## Search, duplicate assessment and controls

The standalone cycle-safe `dedup.py` followed relevant symlinks and included hidden/ignored files in current and original checkout `data`, `research`, `reviews` and `history`. It searched names, bothIMAIDs, the DOI and observed originalfilenames, then followed cited raw roots. The saved receipt contains3786 corpus text files,160 existing cited raw roots,6871 total unique text files and70 hit files. Their paths and bounded excerpts were inspected: prior deferrals, authority rows, citations/overviews and an existing dzhalindite contrast; neither selected owner/original characterization was already curated within this boundary. Earlier occurrence references are not new independent experiments.

Limits are explicit: nine cited raw directories were missing; ten oversized nested text logs exceeded16MB; unextracted PDF/image/binary content was not semantically searched. Exact paths are in the pairedJSON and outsideGitdedup receipt. This is not machine-wide absence or an exhaustive literature claim.

Exact discovery, correction/retraction and microbial queries are in the pairedJSON and `search-log.json`, dated2026-10-12UTC. Only initial returned result sets were assessed; no pagination/exhaustion is claimed. No affecting notice or species-specific microbial experiment was identified in those returned sets. Official journal pages and yanomamiteCrossref metadata showed no correction relation; that does not prove none exists. The actual natural specimen studies contain no microbial experimental arms, so there are no invented organisms, culture controls or extraction denominators.

## Reuse and verification handoff

Raw root: `/private/tmp/cmm-round49-in-research/raw`. Originals: `yanomamite1994-primary.pdf` and `cadmoindite2004-primary.pdf`; full-text derivatives share their basenames; `*-pages/page-001.png` onward contain every original page. IMA originals/renders are `ima2026.pdf` and `ima2026-pages/page-001.png`,002,034,237. All53 raw file sizes/hashes and acquisition receipts are in the pairedJSON. Supporting outsideGit receipts also retain named validator logs and frozen record/history hashes.

Both actual named validators terminated0 with `Checked1record(s);0failed.` Canonical CREATE sidecars were generated with the actual helper and codex/GPT-6/codex actor, then attached as separate history references; inline events are distinct. Baseline was honestly reused at the exact published base via the initialization receipt. Parent owns full cohort/history/review checks and independent scientific assessments; this author dossier is not self-approval. No schema, validator, README, site or governance files were changed.

Remaining priorities are bounded: acquire original indite evidence through a genuinely new route if pursued later; resolve the prior Charrier lead separately; inspect any later yanomamite refinement before expanding structural claims; and require actual primary culture/controls/substrate evidence before adding a microbial mechanism.
