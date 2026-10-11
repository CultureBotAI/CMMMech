# Round 11: beryllium, rubidium and rhenium evidence handoff

Curation on 2026-10-11 UTC in `curate/cmm-expansion-round11-20261011`, based on
`a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c`; acceptance [issue 44](https://github.com/CultureBotAI/CMMMech/issues/44).
This is the curator's dossier, not the independent scientific review. The
[JSON receipt](round11-be-rb-re-20261011.json) contains exact searches, acquisition
URLs and UTC times, file types, failures, hashes and final record/history paths.
Bulk articles and scans remain outside Git in `/private/tmp/cmm-round11-be-rb-re-raw`.

## Selection and identity boundaries

| Record | Accepted scope | Why this scope |
|---|---|---|
| [Beryllium](../../data/records/beryllium.yaml) | Element identity and dated US criticality | Strong removal leads lack inspected full methods; available tolerance work does not measure recovery. |
| [Rubidium](../../data/records/rubidium.yaml) | Light-dependent ion transport in prepared intact phototrophic cells | Complete primary scans include light/dark, ionophore and inhibitor comparisons and informative null conditions. |
| [Rhenium](../../data/records/rhenium.yaml) | Inactive brewer's-yeast association with synthetic perrhenate | Full article and supplement identify biomass preparation, feed, analytical fractions, and serious limits on quantitative/molecular interpretation. |

ChEBI authority pages were freshly acquired and read: **30501 beryllium atom**,
**33322 rubidium atom**, **49882 rhenium atom**, each with the appropriate
single-element formula and zero charge. These roots do not identify Be(II),
86Rb+, perrhenate, beryl, copper-beryllium alloy, a radionuclide or waste feed.
The fresh [USGS final 2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm)
was checked at its heading, publication metadata, summary and final commodity
table. All three names occur. Its Yes/No column concerns byproduct production,
not criticality. Records state United States, authority/list and 2025 edition;
no timeless or latest-edition claim is made, and no status is inherited by hosts.

The initial local search included hidden/ignored files and followed symlinks in
`data`, `research`, `reviews`, `history` and `.claude`. All 67 returned lines were
read: matches were inventory/frontier proposals, not accepted records. The two
cited authority raw roots `/private/tmp/cmm-next-eu` and
`/private/tmp/cmm-expansion-authorities-20261011` were inventoried and searched;
UK/India/EU references contextualize the inventory but are not recertified or
copied into these records. Matching DOI/CURIE checks also distinguish studies
and entities rather than counting mirrors as new experiments. No claim is made
about unrelated home or temporary directories. No symlink was found in the
new raw-evidence directory; raw captures are not corpus fixtures.

## Beryllium: justified identity-only curation

The main promising experimental leads are:

- [Gatewood and Sneddon 1990](https://doi.org/10.1080/10934529009375537), *Removal and recovery of beryllium in waters by Chlorella vulgaris*, Journal of Environmental Science and Health A 25:21–28. Publisher/EPA metadata and the abstract were located; Crossref confirms identity. The publisher full-text request returned 403. OpenAlex identified no repository/full-text location in its returned record. Strain, biomass preparation, solution handling, precipitation controls, exact analytical fractions and desorption mass balance remain unverified. Abstract percentages are not accepted measurements.
- [Sun et al. 2011](https://doi.org/10.1016/j.cej.2011.06.062), *Biosorption behavior and mechanism of beryllium from aqueous solution by aerobic granule*, Chemical Engineering Journal 172:783–791. Publisher preview includes abstract/introduction and partial conclusions; direct publisher request returned 403. The publisher API gave bibliographic coredata only and a FULL request returned 401. OpenAlex's returned locations contained only the closed publisher record. The preview itself names precipitation and ion exchange, reinforcing the need for full control/phase assessment before accepting a biological removal mechanism. Its headline capacity is not curated.
- [Baselga-Cervera et al. 2016](https://doi.org/10.7717/peerj.1823), *Adaptation prevents the extinction of Chlamydomonas reinhardtii under toxic beryllium*, PMC4806628. Full XML was acquired; Discussion and Conclusion were specifically read for claim eligibility. They explicitly say intracellular Be analysis could not be performed with their XEDS method and describe recovery as a possibility. Tolerance/adaptation is not proof of Be accumulation or removal. This was an eligibility check, not a complete audit of its fluctuation-analysis data or supplements.
- [Song and colleagues, 2026 issue](https://doi.org/10.1016/j.corsci.2025.113421), *Corrosion behavior and mechanism of beryllium bronze induced by Aspergillus brasiliensis in space*. Publisher preview describes a Cu-rich QBe 2.0 alloy and predominantly copper corrosion chemistry. The DOI's 2025 string is not the issue year. Full methods and element-specific Be behavior remain uninspected, so neither alloy corrosion nor space exposure is promoted to elemental Be recovery.

Wheat/lotus biochar and modified chitosan papers were separated from microbial
biomass rather than inferring microbial action from the word “bio”. No accepted
Be mechanism is currently justified by the inspected evidence. This is an
access and claim-scope outcome, not an assertion that no microbial Be mechanism
exists. Next work: acquire the 1990 or 2011 full article and relevant supporting
information, resolve abiotic precipitation versus biomass retention, then add an
EDIT history and new independent scientific review if supported.

## Rubidium: full primary scanned article

[Hellingwerf et al. 1982](https://doi.org/10.1128/jb.150.3.1183-1191.1982),
Journal of Bacteriology 150:1183–1191, PMID 6281239, PMC216339, was acquired as
PMC HTML plus **all nine original page images** and every page was visually
read. The nominal PMC PDF request actually returned a 1,817-byte HTML challenge;
it is recorded as failed PDF acquisition, not misreported as a paper. The
Europe PMC full-text XML route returned 500. The complete scans supply the
primary source without bypassing those failed routes. The PMC article has a
copyright notice; scans remain outside Git. No separate supplement was linked
in the inspected article/PMC record; this is a bounded source check.

The source calls the organism *Rhodopseudomonas sphaeroides* strain 2.4.1.
Fresh NCBI Taxonomy 1063 resolves to species *Cereibacter sphaeroides* with that
historical basionym. A species identifier is used; strain identity is preserved
as paper-reported, without claiming an independently verified strain accession.

Methods (pp. 1183–1184) distinguish growth at 30 °C in anaerobic light/Sistrom
medium, pre-harvest chloramphenicol, phosphate assays, isolated chromatophores,
and automated flow dialysis for sodium/rubidium. The record does not transplant
the phosphate assay's detailed loading or 30 °C temperature into the Rb traces.
Figures 4–5 (pp. 1187–1189) concern extensively washed intact cells and explicitly
different buffers. Figure 4 includes valinomycin preincubation at 25 °C; that is
not a statement of the measurement temperature. Figure 4A uses sodium sulfate,
MES/HEPES, magnesium, EDTA and chloramphenicol; 4B uses choline chloride/PIPES
with magnesium and chloramphenicol. Figure 5 varies illumination in sodium
sulfate/phosphate buffer at pH 8. Doses, wash frequency and time course are kept
attached to their own experiment. The exact Rb loading, assay temperature and
replicate count are unresolved for these graphs.

Results and Discussion (pp. 1187–1190) support conditional light-driven uptake,
with inhibition by competing K/Rb and uncouplers. They retain an important null:
choline-chloride-buffered cells without valinomycin initially accumulated no Rb
until formate addition. Valinomycin provides an artificial ion conductance and
increases efflux, so its arm does not prove a native transporter. Arsenate and
DCCD comparisons support a proposed coupling interpretation; ATP inhibition is
reported as data not shown. The paper cautions that absolute voltage thresholds
depend on unproven assumptions about unbound intracellular Rb and vary with pH.
The molecular explanation remains unresolved. Tracer translocation is not a
Rb redox reaction, and no real-feed separation, desorption product or deployment
was demonstrated. Physiological K/Rb analogies are not universal equivalence.

A 1955 polysaccharide-producing-bacteria study (DOI
10.1128/jb.70.6.691-701.1955, PMC386273), later transport/chemotaxis work and
2025 Rb resource-recovery reviews remain follow-up leads. The 1955 study was
located, not fully assessed in this pass. Modern chemical ion exchange and
brine-extraction studies do not validate microbial uptake. Exact-DOI correction/
retraction and transport-inhibition searches returned no matching correction
notice in the inspected first result sets; the JB issue's two correction items
concern other articles. This is not a comprehensive retraction registry audit.

## Rhenium: dried yeast, with the limits retained

[Zinicovscaia et al. 2021](https://doi.org/10.3390/ma14164763), *Materials*
14:4763, PMID 34443283, PMC8400443, was acquired as full Europe PMC XML,
PMC HTML, publisher 16-page PDF, all nine figure images and a publisher ZIP
containing **materials-1323029-supplementary.pdf** (two pages, Figures S1–S2).
Main methods/results/discussion/conclusion, all tables and all nine figures
were read; the relevant table/figure PDF pages and both supplement pages were
visually checked. Main and supplement title/DOI agree. The PMC supplement route
returned HTML despite status 200; the legitimate publisher archive succeeded.
The main article explicitly states CC BY 4.0 and data sharing not available.
The artifacts are retained outside Git; no new claim of access to raw data.

Sections 2.1–2.5 specify synthetic salts, dried/homogenized brewery residue,
500 mg in 50 mL at 200 rpm, duplicated batches, parameter series and the
fraction-specific analysis. Fresh NCBI Taxonomy 4932 verifies the species
*Saccharomyces cerevisiae*, not an unreported strain or axenic preparation.
“Microbial” means biomass origin: drying at 105 °C is explicit. Re/Mo were
measured by neutron activation of the filtered, dried biomass; only Cu was
explicitly measured in solution. No post-contact biomass wash or no-biomass
vessel/filter control is described in these inspected materials. Equations
use solution concentrations, creating an unresolved link between the declared
calculation and the measured Re fraction. The accepted claim is biomass
association, not an independently established whole-feed mass balance.

Figure 2 and Section 3.2 report high association at pH 2 and much lower values
at pH 6. Source-reported percentages remain qualified estimates. The capacity
in Table 2/Figure 4 is distinguished from Table 3's **fitted** Langmuir maxima.
The authors themselves say the latter exceed experimental values. The
Conclusion's mg/kg disagrees with the mg/g in the abstract and Tables 3–4;
no unit conversion repairs it silently. Figure 8's generic C axis and the
Ce equilibrium-model definitions leave the actual fitting basis unclear.
FTIR differences in Figure 9 support changed chemical environments, not a
unique coordination state or a Re valence change. Empirical kinetic/isotherm
preferences do not establish molecular causality. S2's three-metal panel uses
an anomalous lnKd scale; thermodynamic numbers and spontaneous/irreversible
mechanism claims are not accepted. Figure 3 and the pH/kinetic experiments are
not pooled as one identical protocol because all fixed settings are not given.
No Re desorption cycle or pure product is reported in this experiment.

### Separate contradictory/adjacent Re research

- [Dolor, Gilmour and Helz 2009](https://doi.org/10.1080/01490450903060822), *Distinct Microbial Behavior of Re Compared to Tc*, is verified by the Smithsonian SERC record; publisher full text returned 403. The author's [2009 dissertation](https://drum.lib.umd.edu/items/08e422fe-4fca-420e-aa55-3df87abc5c97) was acquired from the UMD repository (178 PDF pages). Chapter 4, printed pp. 66–85, was read in extracted text; it contains the submitted-study account, **not a verified byte-equivalent version of the published paper**. One-week cultures of two sulfate and two iron reducers showed no significant change to nonfilterable Re under those organic-donor conditions; it discusses measurement uncertainty and possible soluble transformed species. No blanket impossibility of Re reduction is inferred. Its figures/appendix have not received a complete independent visual/data audit here, so a separate null mechanism is deferred rather than imported from an abstract or thesis summary.
- [Zhang et al. 2024](https://doi.org/10.1016/j.watres.2024.122089), *Pyrite-stimulated bio-reductive immobilization of perrhenate*, concerns *Desulfovibrio vulgaris* plus pyrite and reports positive reduction at the abstract level. Publisher access failed; Crossref and publisher coredata verify identity and CC BY-NC 4.0, but coredata is not full text and the FULL API request returned 401. OpenAlex supplied no alternative repository location. Full control, spectroscopy, transcript and supplement assessment remains necessary. Different strains, substrates and abiotic partners could explain differences from the 2009 null; no reconciliation is asserted without methods.
- [Arthrospira study, PMC9695948](https://pmc.ncbi.nlm.nih.gov/articles/PMC9695948/) concerns living cyanobacteria in separate mono/mixed synthetic feeds; only indexed primary text was examined as a lead, not its complete methods/figures. It is neither this dried yeast assay nor an independent replication.
- [Spirulina 2018, DOI 10.1002/clen.201700576](https://doi.org/10.1002/clen.201700576) and the paper's Bacillus GT-83-23 reference are promising distinct biosorption/desorption leads. Abstract/headline capacities are not copied into the new record. The newer 2025 pyrite/pertechnetate follow-on measures Tc and is not automatically Re evidence.

No matching correction/retraction notice was identified in the bounded
exact-DOI searches for the selected Rb/Re studies and Be leads. Related
publications and unrelated correction results remain distinguished. Absence
of a result in these searches is not proof of absence elsewhere.

## Validation and handoff

The parent completed the baseline before any record/history write:
307 passed, 3 skipped; 61 records and 72 histories. Named validation of these
three new records passed before and after attaching the actual canonical
CREATE sidecars (3 records, 0 failed). Paths and terminal receipts are in the
JSON. Actor metadata is codex / GPT-6 / codex; inline CREATE events were stamped
at attachment time and remain distinct from sidecar creation. No schema,
validator, test, dependency or governed-file change is needed.

Independent reviews, final whole-batch gates and publication are root-owned
next steps. This dossier does not certify their completion. The independent
review must cover the exact final hashes, particularly the identity-only Be
scope, Rb buffer/ionophore boundaries and the analytical ambiguity in the Re
paper. New supported findings require maintained-record corrections, a real
correction history and successor reviews rather than rewriting observations.
