# CMM source investigation: spent sulfuric-acid-production catalyst

## Scope and provenance

- UTC: 2026-10-11T14:20:53.281845+00:00; researcher Codex (GPT-6; Codex), agent `round24_sulfuric_catalyst`.
- Worktree `/private/tmp/CMMMech-expansion-round24-20261011`, branch `curate/cmm-expansion-round24-20261011`, trusted base `d7183efeb2e528d6d88f0b69da41323642b8fa85`.
- Scope: a process-defined spent catalyst from SO2 oxidation in an acid-production unit; primary laboratory V mobilization and related residual-material evidence. No criticality-list assignment, inherited constituent designation, or industrial bioleaching claim.
- Read the local add-record, discover-sources and review-record skills, source guide/template, CLAUDE.md, README.md, record contract, authoritative schema, validation logic/tests and adjacent petroleum-HDS and automotive-catalyst records. Baseline was run by the coordinating agent before corpus writes: 308 passed, 3 skipped, 156 records and 177 histories (`/private/tmp/cmm-round24-baseline.log`).
- Before creation, `rg --no-ignore --hidden --follow` searched `data/records`, `research`, `reviews`, `history` for both study DOIs, Mikoda and sulfuric-acid catalyst variants. It found the round23 handoff, without an existing acid-production catalyst root in those boundaries. The named earlier raw directory `/private/tmp/cmm-round23-identity-gaps-raw` (28 files) and its cited sulfuric-catalyst dedup report were inspected; older aluminium/automotive references were discovery pointers. Hidden and ignored files were included and relevant links followed. Unrelated home/temp trees were not exhaustively searched.

## Search and acquisition log

Web searches on 2026-10-11 used the following exact queries, first returned result set only, without date filters or pagination:

- `"10.1007/s43452-020-00136-9" correction OR retraction`
- `"spent sulfuric acid plant catalyst" "bioleaching" control`
- `"DSM 9463" Acidithiobacillus thiooxidans`
- `"10.1007/s11356-020-11349-z" correction OR retraction`
- `"Vanadium removal from spent sulfuric acid plant catalyst" correction`
- `"spent sulfuric acid" "Acidithiobacillus" inhibition`

No correction/retraction notice appeared in the returned DOI/title result sets or inspected primary landing pages. This is bounded coverage, not proof that no notice exists. The broader control/inhibition queries recovered the companion study and chemical alternatives; unrelated feed systems were not imported.

| Source and role | Route and evidence actually inspected | Decision |
|---|---|---|
| Mikoda et al. 2020, DOI [10.1007/s43452-020-00136-9](https://doi.org/10.1007/s43452-020-00136-9), resource identity and primary mechanism | Live publisher HTML; newly acquired 14-page PDF; Methods 2.1-2.5, Results 3.1-3.3, conclusions; all Figures 1-9 and Tables 1-3 visually inspected on rendered PDF pages 4-11 | Curate low-loading culture-associated V mobilization, retaining contrary high-loading controls and quantitative conflicts |
| Same study supplementary material | Publisher-linked DOCX, 1,222,505 bytes, valid ZIP; text extracted directly and all three embedded images visually inspected (S1 feed, S2 activity proxy, S3 colors) | Same experiment, not independent evidence; preserve sieve disagreement and proxy limits |
| Mikoda et al. residue study, DOI [10.1007/s11356-020-11349-z](https://doi.org/10.1007/s11356-020-11349-z) | Live PMC full text, newly acquired 10-page publisher PDF, all Methods/results/conclusions; Figures 1-3 and Tables 1-4 visually inspected on pp.3-7 | Context for overlap and residual leachability; no new recovered-yield or harmless-residue claim |
| [DSMZ DSM 9463](https://www.dsmz.de/collection/catalogue/details/culture/DSM-9463) | Live catalogue identifies A. thiooxidans B-S2 from an Australian bioleaching reactor | Strain catalogue identity; does not verify the paper's stock |
| [NCBI Taxonomy 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) | Live identifier, current name and species rank read | Species CURIE only; no strain-specific genome identity |

The initial sandboxed urllib acquisition failed DNS resolution. Authorized network acquisition succeeded for both publisher PDFs, main HTML, companion PMC HTML and DOCX. Redirect URLs included a cookies-not-supported query, but content magic and successful PDF/ZIP parsers confirmed actual documents, not challenge pages. The web supplementary click itself returned an internal error; the public publisher CDN download succeeded. Initial cached renderer access needed a sandbox override; later rendering used the accessible isolated uv cache. No unavailable image was described as visually inspected.

Raw files and acquisition JSON remain outside Git under `/private/tmp/cmm-round24-sulfuric-raw`. Exact URLs, UTC timestamps, byte counts and SHA-256 values are preserved in the paired JSON. This round downloaded the files anew; earlier round23 access is not represented as this acquisition. Both primary articles explicitly carry CC BY 4.0, with their third-party credit-line exception; the linked supplement has no separate conflicting credit visible. The catalogue carries DSMZ copyright. Only curator-authored assessments and source metadata enter Git.

## Source assessments

### Identity, preparation and organism

The feed originated from a sulfuric-acid production unit at a copper smelter, where the catalyst is used to oxidize SO2 to SO3. This establishes a secondary resource separate from petroleum HDS, FCC, hydrocracking and automotive converters. Main Methods 2.1 describes approximately 10-mm granules comminuted and sieved through 100/200 micrometre sieves; supplementary S1 says 250 micrometres. Neither main bioleaching subsection assigns one fraction unambiguously to every arm. Do not silently take the companion's 100-200 micrometre protocol as proof of the original bioleach fraction.

Main Table 3 characterizes one feed at 65.5 wt% SiO2 and 5.50 wt% V2O5 on an oxide basis. The 30,836 mg/kg V figure is the source's conversion from the oxide result, not a separate direct elemental assay. Figures 1-2 identify mixed silica and salt/vanadium-bearing components. No element, mineral-species or universal catalyst-grade identifier is assigned to this mixture.

DSM 9463 was obtained from DSMZ according to Methods 2.3.1. Live DSMZ identifies B-S2; NCBI 930 identifies the species A. thiooxidans. Neither catalogue nor species CURIE establishes the genotype/purity of the experimental stock. No inferred strain accession is added.

### Conditions, controls and outcome

Main study: pregrowth mineral medium with 1% w/v elemental S, initial pH 2.5 adjusted with sulfuric acid, reportedly grown twice over a week to pH 1.7. Bioleaching used 2% v/v inoculum, fresh pH 2.5 mineral medium and 2% w/v S, 28 C, 100 rpm, autoclaved feed/materials, 50-cm3 flasks and at least duplicate inoculated/uninoculated batches. Working liquid volume is not clearly reported; percentages for pulp density (1, 2, 5, 10, 20%) lack an explicit basis in the methods, unlike explicitly w/v sulfur and v/v inoculum. The mineral recipe includes ammonium sulfate; measured sulfate can arise from several pools, so sulfate increase is supportive but not a tracer-based sulfur-source allocation.

Samples on days 1, 7, 14, 21, 28 were filtered at 0.22 micrometres, diluted and acidified before ICP-MS V analysis (quantification limit 0.001 mg/L). No acid control matched to the evolving biotic pH trajectory isolates living-cell action from acidification. Low-loading comparisons nevertheless support a conditional culture association: main Results/Figure 7 and Perspectives give 93% and 85.5% of feed V in liquid at day 21 for 1% and 2% PD, versus at most 17% in uninoculated low-loading series. The curves decline by day 28. Figure 8 shows no high-loading advantage: uninoculated values often exceed culture values. The text reports final biotic 12%, 12%, 8.5% for 5, 10, 20% PD. Those endpoints do not support monotonic or complete extraction.

### Contradictions and causal limits retained

1. Abstract says 93% at 2% PD; main Results/Figure 7/Perspectives say 93% at 1% and 85.5% at 2%. Final Results sentence gives 80% and 74% both as 1%; the figure labels distinct arms. The record does not silently repair the source or select an uncontested optimum.
2. Main 100/200 micrometre versus SI 250 micrometre preparation and unassigned bioleach fraction remain unresolved.
3. Figures 6/S3 color and pH/Eh support suggested speciation, not direct V oxidation-state measurements. Qualitative S2 transfer after 14 days in fresh medium reports sulfur settling/floating; it does not quantify cell survival or validate a direct microbial-reduction pathway.
4. Figure 9 sulfate trajectories and mineral/sulfur feed do not identify which sulfur pool was oxidized. High-loading oxygen limitation/mixing and reprecipitation are hypotheses, not controlled causal tests. The paper's blanket inference of bacterial sulfur dissolution in the abiotic-discussion paragraph is not adopted.
5. Kinetic models in Table 2 use incomplete datasets explicitly selected to improve R-squared (Methods 2.5). Very similar fits do not demonstrate a unique controlling step. No fitted rate or model is imported as measurement.
6. Main Table 3 raw-to-residue concentration differences lack residue masses; a 96.5% concentration reduction is not a verified total mass recovery. XRD non-detection is not proof of zero residual V. Figure 2 local SEM/EDS does not measure bulk product recovery or a uniquely identified precipitate amount.
7. Citric acid was reagent grade, not biosynthesized by DSM 9463. Chemical comparison uses 22 ±1 C, 48-72 h and differing vessels/agitation, versus 28 C cultures over 28 days. It provides a distinct abiotic alternative, not matched microbial causality.

### Companion evidence and overlap

The companion was published online 27 October 2020 and in the 2021 volume 28 issue; these dates are retained distinctly. Its methods explicitly apply conditions attributed to the earlier study again. It reuses the same apparent feed photographs/XRD/microscopy and exactly matching Table 2/main Table 3 oxide composition. The relationship is documented as related evidence, not independent replication or misconduct.

Its reported 21 days/2% PD/93% contradicts main Figure 7 attribution. Its chemical shaking 150 rpm differs from original 100/300 rpm. Its statement of 50 cm3 working medium must not resolve the earlier flask-volume ambiguity retroactively. Approximately 96% removal from solid V concentrations cannot be pooled with solution percentages without mass accounting.

SPLP Methods and Table 3 support residual mobility: 1 g residue, 20 mL water acidified to pH 4.20 ±0.05, 18 h at 150 rpm, followed by 0.45-micrometre filtration and ICP-MS. Bioleached residue gives V 6.4 and Al 4.8 mg/dm3, raw feed 438 and 63 mg/dm3. These are a separate leachability assay, not extraction-process product yields or current regulatory advice. The cited Polish thresholds are not independently adjudicated in this curation; the record asserts no regulatory compliance.

Additional companion issues remain in the dossier rather than importing a new quantitative fractionation model: Table 1/prose disagree over acetic acid 1 M versus 0.11 M and hydroxylamine 0.1 M versus 0.11 M; Figure 3/prose raw V exchangeable fraction is about 81%, whereas Table 4 RAC is 35% despite RAC being defined from that fraction. The printed IR definition uses percentages while bounds require fractions. No raw workbook reconciles these. Concrete reuse and new-catalyst use are proposals, with low measured surface area; no safe reuse or deployment is curated.

## Data fitness and handoff

No independent machine-readable underlying measurements were deposited on the inspected primary page; the supplement contains three images/captions, not raw numerical tables. Companion data availability is 'Not applicable'. This bounded inspection does not establish that no author-held data exist. Exact mg/kg source-cell observations are not imported: selected percentages are feed-normalized outcomes, residue composition is oxide wt%, assay dates are absent, and the native concentration-observation contract does not represent these forms. Qualified prose and source locators fit the current schema without modification.

Ready for independent record review: `data/records/spent-sulfuric-acid-production-catalyst.yaml`. Curation is a new identity and one scoped mechanism, with a canonical CREATE sidecar and distinct inline event. This source report is not the independent acceptance review; named-file and batch gate receipts belong to the review/publication package.

## Priorities and unresolved questions

1. Independently review the final record against the acquired main/SI/companion files, especially the 93% arm, high-loading controls, volume/loading ambiguities and source overlap.
2. Future enrichment requires raw leach-volume/mass accounting, pH-matched controls, quantitative viability/speciation and clarification of sieve/arm labels. Do not invent corrected values.
3. Further source lead: [Frontiers 2026 DOI 10.3389/fmicb.2026.1921494](https://doi.org/10.3389/fmicb.2026.1921494), indirect LIB-black-mass leaching with acid generated from biogas-plant sulfur. Search metadata suggests a distinct secondary sulfur resource; full methods, supplier provenance, deduplication, controls and figures remain unchecked in this pass. This is a handoff only, not a record or independent validation of yields.
4. Nonbiological sulfuric-catalyst work (e.g. DOI 10.1016/j.seppur.2020.116854) was discovered but not quantitatively curated. Other feedstocks cited in the 2020 papers cannot substitute for evidence on this resource.

Searches are bounded by the named material and returned result sets. This report makes no corpus-exhaustion claim and no source-wide absence claim beyond explicitly inspected routes.
