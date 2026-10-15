# Round92 source investigation: industrial machining burrs

Recorded 2026-10-15T09:34:35.377762+00:00 by Codex (GPT-6), `/root/round68_new_frontier`. Base `b5deea86aa8b3872df521b9483541cf1205403ed` on `curate/cmm-expansion-round92-20261015`. This is author curation/source assessment, not independent scientific acceptance.

## Decision and identity

One new secondary-resource owner, `data/records/metallic-machining-burrs.yaml`, is ready for independent review. The 2020 original explicitly identifies metal burrs from an unnamed Mexico City industry, cut/crushed to 10–15 mm by 1–2 mm (Section4.2, p8). These solid machining offcuts differ from the existing coolant-trap `metal-grinding-sludge` owner and from smelting slags. No facility-specific or alloy-specific extra owner is created. No criticality or deployed industrial process is inferred.

## Evidence and source lineage

| Original source | Actual inspection | Use |
|---|---|---|
| [Gomez-Ramirez et al.2020, DOI10.3390/catal10111230](https://doi.org/10.3390/catal10111230) | Complete official11-page PDF, all text, Figures1–4 pp3–4, Table1 p8, Methods4.1–4.4 pp7–9; publisher PDF byte-identical to first SemanticScholar mirror | Accepted primary feed and culture-associated sulfur oxidation/limited leaching evidence |
| [Gomez-Ramirez et al.2021, DOI10.24275/rmiq/Bio2079](https://doi.org/10.24275/rmiq/Bio2079) | Complete official9-page PDF, Figures1–2/Tables1–2 PDFpp4–6, complete methods/results | Context only: distinct IW-steel/IW-scrap feeds and null acidification in Al-rich arm; same research group and method lineage |
| [NCBI930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) | Fresh original XML; species rank/name read | Species authority only, not DSM26636 authentication |

The2020 experiment used0.33g burrs+0.33g sublimed sulfur in30mL medium+3mL four-day inoculum (33mL nominal total),125mL flasks,30°C,150rpm,21days. Six inoculated and three uninoculated flasks were destructively sampled at each of7/14/21days. Figures1–3 show culture-associated sulfate/acidity/pH changes versus controls; the late14/21day contrasts are not significant. Figure4 reports only small metal-mobilization outcomes. The stronger observation is metabolic acid generation in this feed, not a high-yield recovery process.

## Contradictions and limits retained

- 2020 Section4.4 prints control metal content divided by metal removal for percentage calculation. Do not silently invert it or turn Figure4 source values into validated extraction yields. Liquid-to-mg/kg normalization and full mass balance are not given.
- 2020 Figure3 time axis says hours, whereas Methods4.3 and surrounding results specify21 days. Preserve conflict. Abstract/Figure2 approximately0.16M versus text0.15M acidity.
- 2020 Figure3 starts inoculated/control pH differently; inoculum/medium contain Fe,Mg,Mo and sulfate. Controls exist but no pH-matched acid, medium-only, washed-inoculum, killed-cell or sulfur-free factorial comparison is reported.
- Chamber-counted inoculum is called CFU/mL; no direct burr-assay growth series authenticates viable counts. DSMZ specific route redirected and stock/alias remains source-assigned. Current species930 is independently verified.
- Sulfate method designation NMX-K-436-1977 in Section4.3 differs from reference36 NMX-AA-074-1981. No raw calibration/QC or measured uncertainty definition resolves all endpoints.
- Brown precipitates and ferrous-sulfate interpretation lack composition/metal accounting. No isolated-product recovery, validated detoxification or deployment is demonstrated.
- 2021 distinct same-group feeds provide counter-context: Al-rich IW-scrap does not acidify, unlike IW-steel. Do not transfer either outcome to the2020 burr sample or call this independent replication. Its own3mLinoculum/30mLreportedcollection inconsistency, 2.8-foldacid claim vsTable2, reversedAl-comparison sentence and duplicatedMgcontrol label remain unadopted.
- No supplemental document is announced in the complete inspected2020 or2021 originals or returned publisher text. Publisher2020HTML/XML direct requests were403; no claim that all publisher ancillary resources were exhaustively excluded.
- No dated criticality assessment or quantitative-concentration observations were created; resource criticality is not inherited and source assay dates/normalization are missing.

## Discovery, deduplication and acquisition bounds

Hidden/ignored text and relevant symlinks were included across `data/records`, `research`, `reviews`, `history`; exact material/DOI searches and related prior raw roots are preserved in the paired JSON and `/private/tmp/cmm-round92-resources-research/dedup-20261015.json`. No machining-burr or Bio2079/catal10111230 match was returned in these maintained boundaries. The directly inspected `metal-grinding-sludge`, `copper-smelter-slag` and `nickel-smelter-slag` owners are different feeds. Prior round91 resource and round53 REE-clay reports retain Pb/Zn-slag leads; they do not supply accepted burr evidence. Raw-root text searches covered round91 resource and round24 sulfuric-catalyst directories, not unrelated temp/home trees. The initial overbroad slag search was truncated and is excluded from absence evidence. Issue inventory contained215 all-state items; exact material/DOI patterns returned no match. This is a bounded result, not universal novelty.

Exact web query strings, provider, date and first-result-set limits are in the paired JSON. Literature notice searches and live Crossref records yielded no retrieved correction/retraction notice for the accepted2020 original; the2020/2021 relation objects were empty and had no update-to fields. This is limited search coverage, not a guarantee. A2025 cast-house-dust citation led to the2021 companion; the dust paper itself was not adopted. A web strain query surfaced a patent-level alias suggestion, but it was not inspected as authority or adopted; exact stock authentication remains unresolved.

Acquisition receipts retain every failed route: initial sandbox DNS failures, guessed-v2PDF404, direct publisherHTML/XML403, and DSMZ redirect. The actual unversioned official PDF was then acquired successfully and matched the mirror exactly. Files retain original bytes, source URLs, response type and hashes; raw PDFs/text/renders stay outsideGit. The2020 original and Crossref identify CC-BY4.0;2021 redistribution terms remain unverified. Neither entire article nor graphics are redistributed in this report.

## Deferred candidates

- Wang2015 [10.1016/j.jenvman.2015.05.013](https://doi.org/10.1016/j.jenvman.2015.05.013), Guo2010 [10.1016/j.hydromet.2010.04.006](https://doi.org/10.1016/j.hydromet.2010.04.006), and Cheng2009 [10.1016/j.biortech.2008.12.038](https://doi.org/10.1016/j.biortech.2008.12.038): metadata/abstract lead-zinc-smelting-slag leads only; full originals not acquired in this pass. No measurements imported and no repeated blind access retries.
- Sabitova et al.2025 [10.30919/es1579](https://doi.org/10.30919/es1579): priorround91 complete PDF available, text partly rechecked this round; full graphics not assessed here. Lead-slag/copper-slag assignment, pH/organism/assay mapping and abstract/conclusion enhancement percentages remain conflicting. Deferred rather than forced into a new owner.
- Mikoda2019 [10.1016/j.jenvman.2019.02.032](https://doi.org/10.1016/j.jenvman.2019.02.032): primary-looking lead-recovery slag versus shaft/granulated copper slags, but accessible metadata/author-upload search text does not complete all-original graphical assessment; overlap with copper-smelter-slag requires explicit process-origin review. Its related characterization has a2019erratum (10.1016/j.apgeochem.2019.03.002), so that lineage must be checked before reuse. Deferred.

## Validation and handoff

Root's actual baseline receipt/log were checked: exactbase, terminal0, tracked unchanged, logSHA`18688de617b0370da3f8c0f1d091a935c10e6ec92a998b7e3f91e98b3e573c98`. Maintained owner writes occurred only after baseline clearance. Canonical CREATE `history/records/metallic-machining-burrs/2026-10-15T093227Z-codex-4c2035.yaml` and a distinct actual inline CREATE are attached. Named strict validation reports1passed0failed; its raw log is bound in JSON. No full-batch or independent scientific acceptance is claimed here. Root handles shared pages/gates and a separate reviewer must accept exact final owner/history bytes.

OwnerSHA`628c79d49547a2ef347c77a73af94d02f61f845b7d43c059d98f9643d21f38eb`; historySHA`32d0263372ea3e8d735ea34772f7629c95aa4c1eadc0c59d502d4445f294a4d0`. A source-clarification draft will request the correct normalization equation, time units, measured-control/raw-balance data and assay-standard mapping without treating source ambiguity as a curator defect. It will be posted only by root under existing authorization after live dedup.
