# CMM source investigation: waste printed circuit boards

## Scope and provenance

- UTC timestamp: 2026-10-11T12:43:14.834553+00:00; researcher: codex (GPT-6; codex).
- Worktree `/private/tmp/CMMMech-expansion-round21-20261011`, branch `curate/cmm-expansion-round21-20261011`, base `55fd1947e80f67ec91dfe63e7bf15f72d822cefb`.
- Question: does an end-of-life board feed support a distinct secondary-resource record with measured microbial extraction evidence? This lane covers waste-computer boards and recycler-supplied board mixtures; it does not attempt an exhaustive electronic-waste survey, latest criticality assessment, or industrial deployment audit.
- Final lane changes: one record, one CREATE history, this paired source dossier, and a timestamped discovery report. Root manages batch gates and independent scientific review. Record creation was cleared after the baseline passed; that baseline result was communicated by root rather than executed by this author.
- Related records inspected: copper, iron-ore tailings and tantalum. The existing Ta record curates separated capacitors from [Sikander et al. (2022)](https://doi.org/10.3390/ijerph191610006), not the identity of all waste boards. Its PCB experiment is a known future extension, not a new independent study of Ta.
- Identity boundary: discarded circuit layers on insulating boards, potentially retaining mounted components/solders; distinct from whole electronic waste, isolated components, elemental copper, processing sludge and mineral species. Board source and composition vary; no constituent-metal criticality is inherited. No external material or taxon CURIE is asserted. KCTC4516 is retained as the organism designation reported by An, not a newly authority-resolved strain identifier.

## Hidden/ignored duplicate search

Before curation, `rg --no-ignore --hidden --follow` searched all `data/records`, `research`, `reviews`, `history` and this lane's `/private/tmp/cmm-round21-pcb-raw` for material synonyms/PCB and exact accepted-study DOIs. Actual final receipt: `/private/tmp/cmm-round21-pcb-raw/dedup-final-receipt.json`; stdout SHA-256 `58c5d113e3b1a449be165a21f8c1b6dc915eef92e4ad41e9589be06bd80758be`, 292 matching lines, exit 0, no stderr. Only maintained record matching this bounded material/DOI search was `data/records/tantalum.yaml`; identity inspection distinguishes its elemental/capacitor scope from the proposed board feed. Earlier narrower exploratory patterns are superseded by this receipt.

The relevant prior downloaded artifacts cited by the Ta review, `/private/tmp/cmm-round10-nb-ta-raw`, were also searched with hidden/ignored inclusion and symlink following. That supplemental search returned 86 lines (exit 0, no stderr), stdout SHA-256 `d2e5db4122ec9d107f8e5ecd2b161f32fc316812d3ef211ebf602183b73f0a1f`; it confirms known PCB material in the old study and references. This is a bounded repository/referenced-download claim, not machine-wide or literature-wide absence. Duplicate search receipts including exact commands/times are retained in the JSON dossier.

## Search and acquisition log

All web searches ran on 2026-10-11 through the web search provider, without date/domain filters, first returned result sets only; no pagination was requested. Exact query times were not retained. Exact queries:

- `printed circuit boards microbial bioleaching Acidithiobacillus ferrooxidans control open access copper study`
- `waste printed circuit boards Chromobacterium violaceum bioleaching gold PMC`
- `"10.3390/min11020224" correction retraction`
- `"Characteristics of Metals Leached" "Karwowska"`
- `"printed circuit boards" bioleaching "abiotic" "2021"`
- `"10.1016/j.mineng.2022.107471" correction retraction`
- `"10.3390/min11020224" "supplementary"`
- `"Copper recovery from unground printed circuit board" "supplementary"`
- `"Characteristics of Metals Leached from Waste Printed Circuit Boards" correction retraction erratum`
- `"Copper recovery from unground printed circuit board" correction retraction erratum`

The Karwowska query was an early author-name hypothesis; publisher PDF and Crossref establish **Jinsung An**, and no Karwowska attribution is accepted. The local first PDF filename `karwowska2021.pdf` is a misleading acquisition alias only; its verified DOI, title, author, checksum and content identify An (2021).

Direct web opens of MDPI returned 429; PMC displayed a browser challenge; the two university PDF routes returned 403 through web. Initial restricted Python network requests failed DNS resolution at 12:37:23Z. Authorized network acquisition then successfully retrieved real PDF/XML/JSON artifacts. Direct publisher HTML acquisition later returned 403 for MDPI and ScienceDirect. Successful HTTP status was checked against PDF magic/XML or JSON content, rather than assumed to mean full text.

| Source artifact | Canonical identity and acquisition | Evidence actually inspected | Decision |
|---|---|---|---|
| An primary PDF | [10.3390/min11020224](https://doi.org/10.3390/min11020224), Minerals 11(2):224, published 22 February 2021; publisher PDF/CDN, 8 pages | All primary text; Methods 2.1–2.2; Results 3.1–3.3; all Figures 1–4 rendered and visually inspected | Accept narrowly scoped culture-associated Cu concentration result and limitations |
| Iglesias-Gonzalez et al. primary PDF | [10.1016/j.mineng.2022.107471](https://doi.org/10.1016/j.mineng.2022.107471), Minerals Engineering 180:107471, April 2022 issue; university repository holds published 8-page article | All text; Methods 2.1–2.4; Results/discussion; all Figures 1–6 rendered and visually inspected | Accept separate ferric-regeneration system with unequal-comparison and mass-balance qualifications |
| Benzal et al. author manuscript | [10.1007/s12649-020-01036-y](https://doi.org/10.1007/s12649-020-01036-y), title confirmed by manuscript and Iglesias reference | Title/abstract/introduction only; 12-page PDF acquired | Defer claims until full methods, toxicity and column evidence reviewed |
| Anaya-Garzon et al. | [10.3389/fmicb.2021.669738](https://doi.org/10.3389/fmicb.2021.669738), PMC8416503 | Europe PMC XML and selected methods/results on PCB-leachate inhibition; figure/SI unverified | Promising contrary/complementary evidence; not adopted quantitatively this round |
| Precious-metal RSM study | [PMC10079379](https://pmc.ncbi.nlm.nih.gov/articles/PMC10079379/), title Optimization of Precious Metals Recovery from Electronic Waste by Chromobacterium violaceum Using Response Surface Methodology (RSM) | XML acquired/title checked; assay/figure evidence unreviewed | Defer; must distinguish experimental versus predicted optima and confirm controls/status before adoption |
| Sikander et al. PCB/capacitor study | [10.3390/ijerph191610006](https://doi.org/10.3390/ijerph191610006) | Existing Ta record/review and bounded local duplicate search | Known source, no re-curation or claimed independent replication |

## An 2021: claim-level assessment

The waste-computer origin supports the secondary-resource identity. The laboratory experiment used 5 g washed/dried fragments below 1 cm2 with 50 mL liquid, 30 degrees C, seven days, three repetitions. Culture was reported as A. ferrooxidans KCTC4516; pre-growth in 9K is separate from the board stage using 0K without added ferrous sulfate. The author estimated 1.4 × 10^6 cells/mL after inoculation. Section 3.2 describes starting 0K pH 2; a board pH series and board shaking speed are not supplied. 180 rpm applies explicitly to preculture. A 50 mL stated tube plus 50 mL liquid and solids leaves oxygen/headspace handling unresolved.

- **Support, Figure 2a and Section 3.2:** day-seven filtered Cu 1047 mg/L in the inoculated treatment versus 413 mg/L in 0K alone; day-one values 18 versus 41 mg/L. These are measured source concentrations in 0.2 micrometre filtrates by ICP-OES. They are not a fitted maximum, metal-product yield or native mg/kg concentration observation.
- **Control limitations:** 0K and water comparators exist, but washing of the seven-day iron-rich inoculum and equivalent sterile spent-medium addition are not specified. Consequently iron carryover and culture-medium chemistry are not excluded. No starting PCB copper inventory is measured for a Cu extraction percentage.
- **Iron contradiction:** Section 3.2 says inoculation increases filtered Fe, but Figure 2b generally has inoculated squares below uninoculated triangles. No 76%-increase claim is imported. Figure 1 measures Fe oxidation and redox during separate 9K preculture, not a direct PCB-stage iron oxidation balance.
- **Nickel and lead limits:** Ni rises strongly in both acidic treatments (Figure 2c); curves differ numerically, so neither complete equivalence nor exclusive microbial Ni release is asserted. Late Pb is lower in inoculated filtrate (Figure 2d), with Pb-bearing retained material by EDS; that is not a tolerance assay or unique Pb-phase identification.
- **Precipitate scrutiny:** Figure 3 marks libethenite in the uninoculated 0K residue. Lack of assigned peaks in the inoculated trace does not show all copper solids absent. Figure 4 labels/caption identify water a/b, 0K c/d and inoculated e/f; Section 3.3 prose incorrectly assigns several panel letters. SEM-EDS cannot alone identify amorphous iron oxide species or jarosite. The Zr label is explicitly discussed by the source as Pt-coating overlap, not accepted as zirconium recovery.
- **Scope:** laboratory filtration/solubilization/precipitation observations only. No cost, environmental-superiority or industrial-deployment claim adopted.

The eight-page PDF contains a data-within-article statement, no cited supplementary item in its full text. Publisher HTML remained inaccessible, so this is not an exhaustive assertion that no hosted supplement exists. No accepted claim depends on an unavailable supplement. Crossref metadata matched title/author/date/DOI and had no `update-to`, `updated-by` or nonempty relation entry in the retrieved response. Title/DOI correction/retraction searches returned the original source and ordinary citing records, without a specific notice found in these first result sets; that bounded negative does not certify permanent publication status.

## Iglesias-Gonzalez et al. 2022: claim-level assessment

The primary article gives an explicit recycling-company board feed. Introductory composition ranges are context, not measured composition for every board. Boards were cut to mean 4.4 cm2 without pulverization/coating removal. The connected configuration uses a living immobilized Rio Tinto drainage community, described as mainly A. ferrooxidans and L. ferrooxidans with Acidiphilium-related heterotrophs. No member-specific causal assignment or taxon/strain accession is inferred.

- **Methods 2.1–2.4/Figure 1:** the connected run used 100 g boards and 736 mL total liquid, initial Fe(III) 20 g/L, 0.8 L/h circulation and stated 750 mL/h air. The whole-system solid/liquid ratio is 13.6%; 65.4% is column-specific. The unconnected run is explicitly at room temperature; a numerical connected-system temperature is not supplied.
- **Methods/results/Figures 5–6:** 90% Cu dissolution at 25 days, initial grade reconstructed as about 30% from liquid/wash/residue fractions. It is an empirical extraction calculation, not a fitted optimum and not a purified-metal product yield. No repeat-column uncertainty is given. Copper-bearing liquor was purged/replaced four times, including at 18 hours, with acidified evaporation replacement and pH adjustments.
- **Unequal comparator:** the separate unconnected run used 124 g boards, 2 L solution, three biogenic-ferric batches (reported starting concentrations 12.7/13.1/13.8 g/L), approximately 25% reconstructed Cu grade and reached 62.2% Cu dissolution in 25 days. It is not a matched sterile control; initial oxidant, loading, liquid volume, grade and replacement regime differ. Stored biologically generated liquor is not shown sterile.
- **Acid-only control:** preliminary flasks at pH 1.25 are described as giving no observed metal solubilization, without a numeric detection limit or a comparable 25-day column control. This does not establish universal zero acid leaching.
- **Figure-level contradictions:** Figure 2 displays ferrous concentration in panel B and copper in C, whereas its caption reverses these panel assignments; no quantitative panel-specific concentration is imported from that caption. Figure 5 includes pH above 2 despite Section 3.2's below-2 description. Outlet redox rises after an initial transient toward about 700 mV versus Ag/AgCl, rather than being constant from time zero.
- **Mechanism and scope:** sustained high outlet redox supports functioning regeneration under these conditions; it is a proxy, not direct taxon-specific kinetics or proof of complete cell exclusion from boards. The 5–12 day slower release interval correlates with higher dissolved Cu but liquor exchange also changes chemistry. No zero-reagent-use claim is adopted; acid and fresh liquor were used. Solvent extraction/electrowinning remain proposed downstream operations. Lab operation is not industrial deployment or general PCB toxicity immunity.

The full article ends with references and provides no named supplementary item; no accepted claim depends on SI. Direct publisher HTML was blocked, and the first supplementary-search results did not expose a source-specific supplement; hosted-SI absence is not certified. PDF states available online 4 March 2022; Crossref gives April issue publication and a 2 March VOR license-start date. License timing is not silently substituted for publication date. Retrieved Crossref had no correction relation/update fields; first title/DOI correction-result sets disclosed no specific notice, within their stated search limit.

## Reuse, files and quantitative mapping

An PDF declares CC BY 4.0. Iglesias PDF declares CC BY-NC-ND 4.0. Reading access and retained local copies are distinct from redistribution; neither PDF, XML nor figure image is committed. The Benzal repository manuscript's reuse terms were not verified. Anaya XML includes open-access attribution text; its supplementary attachment is identified but not acquired/verified. The RSM XML license and publication-status details remain unchecked and no results are adopted.

This pass uses article-level experimental evidence, not a bulk dataset. No machine-readable observation dataset or version/update guarantee is established. Native CMMMech observations require exact mg/kg cells with analysis dates: the reported mg/L time-course values and percentages lack that contract and remain precisely qualified prose. No density conversion, invented dates, pooled replicate or digitized pseudo-precision is introduced. Raw URLs, actual acquisition UTC times, file types, bytes and SHA-256 checksums appear in the paired JSON and acquisition manifests. Derivative text and page images are local working aids, not independent sources.

## Priorities and handoff

1. Independently review `data/records/waste-printed-circuit-boards.yaml` against these two full primary studies and exact final hash. The entry is scientifically limited; schema validation alone does not accept it.
2. Extend the same board record with [Anaya-Garzon et al.](https://doi.org/10.3389/fmicb.2021.669738) after Figure 2, culture composition and supplementary material are checked. Chemically prepared PCB leachates caused concentration-dependent delays and an apparent highest-loading null in selected text, but whole solid-feed exposure differs; do not transfer its limits numerically without full verification.
3. Review the full Benzal 2020 manuscript, then compare mobile-phone board pretreatment and time-dependent metal toxicity with the current assays. Different assays need independent contexts, not averaging.
4. Reassess the known [Sikander 2022](https://doi.org/10.3390/ijerph191610006) PCB branch separately from its already curated Ta-capacitor branch, preserving its medium controls and source/SI inconsistencies.
5. Investigate fungal and cyanogenic precious-metal studies, starting with acquired PMC10079379 only after publication status, actual board feed, control structure, measured/fitted yields and full figures are checked. Their mere appearance in a search does not justify mechanism ingestion or a new material root.

No new species/component record is generated simply to increase count. No claim of exhaustion is made: several concrete, accessible extension candidates remain.

## Local result and limits

- Record: `data/records/waste-printed-circuit-boards.yaml`, SHA-256 `1c4084c10b590efcbef858e3a37a74bbfc7bb1687c7635a0337ec3a09f870e93`.
- CREATE sidecar: `history/records/waste-printed-circuit-boards/2026-10-11T124047Z-codex-fd23ae.yaml`, SHA-256 `b5ee90ea4961aba93941dbde5f68872e19609831c2cb366f55b9d4455d5f94bb`. The helper ran with actual GPT-6/codex metadata and the printed path was attached; the inline event is distinct. History was created before root announced batch issue #77, so no retrospective issue-link rewrite was made.
- Named record validation: `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate data/records/waste-printed-circuit-boards.yaml`, terminal exit 0, `Checked 1 record(s); 0 failed.`
- Scientific review: pending independent rotation at report creation; this report is discovery/curation provenance, not a saved acceptance review. Root runs final corpus/history/review gates.
- Remaining questions: precise 2021 inoculum iron carryover and PCB-stage redox/pH, actual board starting composition, reproducibility of 2022 column yields, connected-system temperature and Figure 5 pH discrepancy, matched oxidant/feed controls, long-run toxicity and measured downstream product recovery.
