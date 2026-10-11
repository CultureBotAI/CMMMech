# CMM source investigation: nickel laterite geological feeds

Research completed 2026-10-11T12:14:37.131050Z by Codex (GPT-6; codex), laterite lane. This is a
source assessment and curation handoff, separate from scientific record acceptance.
Worktree: `/private/tmp/CMMMech-expansion-round20-20261011`; branch
`curate/cmm-expansion-round20-20261011`; trusted base
`e98bdfaba62869faf5112ef281a9371d2a04d78e`.
The coordinating agent reported baseline `just check` passing (308 passed,
3 skipped; 145 records; 162 history sessions) before authoring was cleared.

## Identity and deduplication boundary

Selected one new record, `data/records/nickel-laterite-ore.yaml`, using the existing
`primary_resource` kind. USGS's official 2013 deposit-model summary independently
grounds a naturally weathered, heterogeneous geological feed. Unprocessed excavated
and stockpiled ore remains this resource. Limonite/saprolite or site/sample names
are not introduced as separate records. Processing-generated Caron tailings are
outside this identity. No element or mineral identifier, constituent criticality,
trade specification or guaranteed extraction performance is inherited.

Before authoring, ran `rg --no-ignore --hidden --follow -n -i` across actual
`data`, `research`, `reviews`, `history` and the referenced retained raw directory
`/private/tmp/cmmmech-nickel-evidence-20261011`, searching laterit, limonit,
802991, 8352580, 8787160, sir20105070H and s40831-025-01139-7. Earlier search also
covered schema/scripts/tests. Hidden and ignored files and relevant symlinks were
included. Binary PDF/PNG files were separately inventoried, checksummed and
inspected instead of treated as absent by text search. The new raw directory is
`/private/tmp/cmm-round20-laterite-raw`. No machine-wide absence is asserted.

The existing nickel element record and its ingest/review/history were the sole
maintained laterite mechanism coverage in those boundaries. The 2025 experiment
is therefore a known study reused at a distinct ore identity, not a newly
discovered experiment. The 2022 and 2021 papers were prior research leads, now
read in full publisher text. No prior geological-feed record was found in the
hidden/ignored-inclusive search. Pure goethite is handled by a separate lane;
whole-ore metal release is not assigned to that mineral.

## Search log and acquisition

Provider: live web search, 2026-10-11 UTC, first returned result page only, no
pagination, date or domain filters beyond terms in each query. Exact queries:

1. `site.usgs.gov nickel cobalt laterite deposits weathering ultramafic deposit model`
2. `nickel laterite bioleaching reductive 2021 2022 chromium inhibition PMC8787160 PMC8352580`
3. `"10.1007/s40831-025-01139-7" correction retraction`
4. `"PMC8352580"`
5. `"10.3389/fmicb.2021.802991" correction retraction`
6. `"10.3389/fmicb.2021.703177" correction retraction`
7. `"10.3389/fmicb.2021.802991" supplementary material`
8. `"laterite" "bioleaching" "abiotic" "inhibition" "2026"`

PMC full pages initially returned reCAPTCHA; legitimate publisher full pages were
used. USGS publication-warehouse/PDF routes failed (web internal errors; direct
PDF HTTP 403); its official full publication summary was read. The USGS report's
entire PDF was not inspected. The summary suffices for the narrow identity claim,
not deposit-by-deposit mining or production statistics. Springer table-3 web
subpage failed; the retained main PDF table was read locally instead.

Initial Python downloader lacked requests, then standard-library urllib attempts
failed sandbox DNS. Approved network retry acquired complete HTML for the two
Frontiers studies, Springer study and NCBI taxonomy. Response types/content and
publication titles were checked. Main 2025 PDF, supplement and Figure 6 were
previously acquired and rechecked; no fresh PDF-download claim is made. Temporary
pypdf retrieval initially failed sandbox DNS then succeeded on approved retry;
PDF extraction did not change repository dependencies. The shared evidence
Python with PyMuPDF was also used for main-PDF extraction. The prior Figure 6
image was viewed directly. Raw HTML/PDF/image bytes and text extractions stay
outside Git; acquisition and hash receipts accompany the paired JSON.

## Claim-level source inventory

| Normalized key | Role and inspected evidence | Decision and limits |
|---|---|---|
| [10.3133/sir20105070H](https://www.usgs.gov/publications/nickel-cobalt-laterites-a-deposit-model), Marsh, Anderson and Gray 2013 | Official complete publication summary: weathering of ultramafic rocks, hydrous Mg-silicate/smectite/oxide subtypes and heterogeneous horizons | Ground primary-resource identity only. Full report PDF access blocked; no composition ranges or contemporary reserve statistics imported. Government publication; no explicit artifact-specific reuse license verified in this pass. |
| [10.1007/s40831-025-01139-7](https://link.springer.com/article/10.1007/s40831-025-01139-7), Hetz and Schippers 2025 | Full HTML; retained main PDF Methods, Tables 1–3, Results/Figures 1–10/captions, Discussion; retained Figure 6 image; retained supplement captions S1–S10 | Curate aerobic sulfur-oxidizer mechanism. Known study, new resource-level coverage. CC BY 4.0 as stated by publisher; retain raw outside Git. |
| [10.3389/fmicb.2021.802991](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.802991/full), Santos et al. 2022 | Complete publisher Methods, Tables 1–4, Figures 1–11 captions, Results and Discussion; distinct January 2022 publication in volume 12 (2021) | Curate conditional anoxic NC1 mechanism and NC2 chemical counterevidence, preserving differing assays. CC BY stated by publisher. Data statement generically mentions article/supplement; no separate supplement link found by hidden-inclusive search of the acquired full HTML or bounded web query. No raw replicate dataset acquired. |
| [10.3389/fmicb.2021.703177](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.703177/full), Johnson, Smith and Santos 2021 | Full Methods/Results/Discussion, Table 1 and Figures 1–6 captions | Retain as further mechanistic evidence and caution; not copied as a third mechanism. Distinguishes ore leaching from soluble-iron experiments and culture-prepared, sterilized sulfur. CC BY; raw data available by request according to source, not acquired here. |
| [NCBI Taxonomy 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) | Official current label Acidithiobacillus thiooxidans, rank species, DSM 14887 among type-strain designations | Supports species ID only, not the six-strain mixture or individual causal contributions. No strain/genome accession invented. Page reuse terms not assessed; HTML retained outside Git. |

## Curated assay boundaries

**2025 aerobic experiment.** Six equal-volume cultures (DSM 14887T, 504, 622,
103717, 9463, BGR RAM8) were grown four days before adding unwashed <2-mm
homogenized ore at 10% w/v. The stirred 2-L reactors contained 1.5 L medium at
30 degrees C, initially pH 3, 1% w/v sulfur and 10% v/v inoculum. Air was
supplied. Source statements about 3 mM ferrous iron in medium and 3 mM before
ore addition do not unambiguously specify a cumulative dose. Uninoculated
controls followed the corresponding biotic pH curves. ICP-OES measured filtered,
acid-stabilized solution metals. BaSt pH-not-maintained Ni extraction after
15 days was 83.0 +/- 5.7% (four reactors) versus 33.6 +/- 0.1% (two controls);
Co was 83.0 +/- 3.0% versus 23.9 +/- 0.1%. These source means and SD were not
recomputed; percentage denominators are feed metal, not isolated-product yield.

Figure 6 was visually rechecked and agrees with reported directions. Table 3
shows mixed mineralogy (BaSt includes goethite, chlorite and other phases); the
ore is not a pure-goethite assay. The same study contains an important 1P5 null,
similar Piaui Ni outcomes, low JacF extraction, and JacC Results/abstract tension.
Supplement S1 labels JacF biotic n=1 while S3 labels n=2; Piaui S2 labels control
n=1 where main Figure 8 gives n=2 for maintained pH. These inconsistencies are
retained in research and no general replicate count is inferred. Molecular
reduction proposals in Discussion are not presented as established enzymes.

**2022 anoxic experiment.** Penamax NC1/NC2 were ground and screened <100 micrometers.
NC1 used the source-reported mesophilic consortium (type strains of A.
ferrooxidans, provisionally quoted 'A. ferruginosus', A. ferriphilus, A.
ferridurans, S. thermosulfidooxidans). No organism identifier is fabricated for
the mixture. Starter medium is described, but the separate reactor inoculum
volume/sulfur dose is not independently specified. Source Table 1 and Methods
establish 2-L working volume, 150 rpm, 35 degrees C, pH 1.5, oxygen-free N2 for
NC1. Experiment I added 10% w/v ore once and ran 30 days; II added 1,4,5,5% on
days 0,15,29,43 to 15% final, with Results through day 50. Iron speciation used
ferrozine; other solution metals used AAS. No reactor replicate count is stated.
Table 3 gives Ni/Co extraction 12/41% (I) and 31/94% (II). Both ultimately lost
microscopically observable cells. Different duration/loading prevents a matched
causal treatment-effect claim or sustained-growth claim.

NC2 experiments III–IV use a different consortium: Acidianus brierleyiT,
A. sulfidivoransT and Acidithiobacillus caldus BRGM3; the NC1 list must not be
transferred. IV at 50 degrees C, pH 1.5, initial 5 mM Fe(II), staged 15% final
ore gave Ni/Co 12/72%. Abiotic V used 1-L working volume, 15% all at day zero,
three 10-mM Fe(II) additions over four days and gave Ni/Co 10/70%. Thus V shows
substantial chemical leachability but is not fully matched to IV. Fe(II) removal
of Cr(VI) does not remove all toxicity: Table 4 and Discussion describe a
separate ferrous-sulfate leachate more inhibitory despite Cr(VI) below detection.
XRD residue descriptions show no major goethite-pattern changes, reinforcing
that whole-ore extraction is not pure-phase proof. The abstract's broad >90%
cobalt wording applies to the strongest NC1 incremented case, not every Fe-added
NC2 experiment.

No assay was imported into concentration observations: yields are percentages,
2022 composition uses g/kg and source analysis dates required by the current
mg/kg observation contract are not established. No schema change is necessary.
All curated experimental scale is laboratory; papers' introductions about pilot
work elsewhere do not establish deployment of these runs.

## Additional checked evidence and ranked next actions

1. Johnson et al. 2021 describes Shevchenko 5% ore reactors and a separate Penamax
   assay with culture-prepared hydrophilic sulfur sterilized at 110 degrees C
   for 60 minutes. No viable acidophiles were detected by microscopy/plating in
   the latter assay. Acid-only, ordinary sulfur and bio-ZVS arms differed; the
   ore itself was not sterilized to avoid mineral alteration. Figure 5/Results
   report strong Co/Mn extraction with bio-ZVS but leave residual killed-cell
   and reactive-sulfur contributions unresolved. This is useful for a future
   separately scoped mechanism; do not call it living-cell recovery or imply
   purified elemental nickel production.
2. The 2021 soluble ferric-iron tests on A. thiooxidans DSM 103717 grown on
   hydrogen, tetrathionate or sulfur support uncertainty about a unique sulfur
   intermediate. They are not direct ore-leaching assays. Raw data by request
   remain unavailable; no author contact made.
3. The preexisting 2024 lead DOI 10.3389/fmicb.2024.1359019 and 2015 Caron
   tailings DOI 10.1021/acs.est.5b00944 remain separate leads. The latter needs
   a processing-generated secondary-resource identity if later curated. Neither
   was re-read in this bounded round; no measurements transferred.
4. The 2025 Discussion points to goethite-specific DOI
   10.3389/fmicb.2024.1360018, shared with the separate goethite lane; it must
   be assessed in its own substrate scope.

The exact-DOI correction/retraction searches and opened publisher pages returned
no specific notice in this pass. This is a bounded search result, not an
exhaustive registry audit. No author contact, raw-data requests, economic
assessment or industrial performance validation was performed. The paired JSON
provides machine-readable receipts, source dispositions and target/history links.

Timestamped discovery report: `research/sources/round20-nickel-laterite/20261011T121437Z.md`.
