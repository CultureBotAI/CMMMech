# Bastnaesite source investigation and curation handoff

UTC: 2026-10-11T17:48:24.998657+00:00
Curator: codex (GPT-6), author of the new record; this is **not** its independent scientific review.
Worktree: `/private/tmp/CMMMech-expansion-round29-20261011`
Trusted base: `7629ab50846229c87987d7fa0ac12389212bb70f`.

## Decision and identity

Ready for independent review of [bastnaesite.yaml](../../../data/records/bastnaesite.yaml), frozen SHA-256 `719dafc38a258c140dafa5c718a651d19c7300c9aa0643fe293898d56f1b6448`. Canonical CREATE history: [2026-10-11T174551Z-codex-b64d41.yaml](../../../history/records/bastnaesite/2026-10-11T174551Z-codex-b64d41.yaml), SHA-256 `4b6f618c7e59982983f37a60a4ef3c95b40e1f9ea3c53073ba014c6b30b148a7`. Named validation passed: one record checked, zero failed. Parent baseline passed; final batch and scientific acceptance remain separate obligations.

The accepted concept is the F-dominant bastnaesite fluorocarbonate family, ideal REE(CO3)F, represented as `mineral_group`. It includes separately named bastnäsite-(Ce), -(La), -(Nd) and -(Y); it does not assert the experimental material is a specific endmember or equate the family to a whole rock, REE element, commodity, or the broader structural group. The issuing IMA-CNMNC September 2026 list was freshly acquired and its p21 species rows inspected. The natural material's Ce-rich bulk oxide analysis is insufficient for a formal species assignment. No external mineral identifier or criticality is assigned.

NCBI 1428 resolves *Bacillus thuringiensis* at species level. It does not establish identity of the study's unnamed wild isolate. No deposit code or sequence accession is supplied in the inspected 2025 main/SI. Mindat's own indexed profile 563 independently describes a related-mineral family, but direct HTML routes returned 403; no successful HTML download is claimed and no Mindat ID is asserted in the record.

## Primary source and actual access

[He et al. 2025, DOI 10.1016/j.gca.2025.02.027](https://doi.org/10.1016/j.gca.2025.02.027), *Geochimica et Cosmochimica Acta* 394:43–52,April 2025, is the sole accepted experiment. Authors are Yilin He, Lingya Ma, Xurui Li, Xun Liu, Xiaoliang Liang, Jianxi Zhu and Hongping He. Crossref and the repository identify this publication.

The complete [GFZ institutional postprint](https://gfzpublic.gfz.de/pubman/item/item_5034287_3/component/file_5034752/5034287.pdf) was downloaded: `raw/gca2025-primary.pdf`,39 pages, SHA-256 `9f9d2b33987fb6ec9eee22de866f743fdbd0402bf69c66aa6a510315f2995a81`. Full text was read, and all 8 main figures plus both tables visually inspected: PDF pages9,14,16,18,20,22,29,39. Cover and text-only pages are not all claimed as visually inspected. The publisher main PDF was not acquired. Repository metadata calls this public/greenOA/postprint; no explicit reuse license was found in the inspected metadata. Full text stays outside Git.

The complete [publisher supplement](https://ars.els-cdn.com/content/image/1-s2.0-S001670372500105X-mmc1.pdf) was downloaded and all 5 pages visually inspected: `raw/gca2025-supplement-1.pdf`, SHA-256 `5ca2571afac44acd054c4f90568309e04c07902fb772fa2dfad5999569d7409e`. It contains Texts S1/S2, Table S1 and Figures S1/S2. Source URL/redirect/status/bytes/hash and actual acquisition timestamps are retained in acquisition logs 1–6. The first sandbox DNS failures are also preserved; subsequent permitted public-network requests succeeded for these sources.

The complete [Mendeley dataset v1](https://data.mendeley.com/datasets/6n6d3fkkpc/1), DOI 10.17632/6n6d3fkkpc.1, was published 29 October 2024 and licenses the data CC BY 4.0. Its one deposited `ResearchData.xlsx` file was acquired,512898 bytes, SHA-256 `fac8f9bbf5fe5c081ea0a1ce58c3d204e698b7848be350c459246fdc407f2654`, matching the deposit manifest. All7sheets were inspected: XRD; pH; planktonic CFU; normalized metabolomics; aqueous REE; chemical leaching; SEM-EDX. This is supporting data for the same 2025 paper, not a second independent experiment. The JSON companion lists all raw artifact hashes, including complete extracted workbook cells retained outside Git.

## Experimental contract and evidence boundaries

| Aspect | Exact supported scope |
|---|---|
| Feed | Mineral grains selected from Maoniuping bastnaesite-bearing rock, western Sichuan. Agate crushing;48–74micrometres;more than 10 washes;freeze-dried. SemiquantitativeXRD~97wt%bastnaesite/~3wt%quartz. XRF CeO2 36.1%,La2O3 30.1%,Nd2O3 7.40%,Pr6O11 2.57%. |
| Organism/biomass | Living wild Bt isolate from Renju regolith-hosted REE deposit, Guangdong. LB-plate exponential-phase cells, washed and resuspended. Earlier isolation/identification paper referenced but not independently acquired in this round. |
| Biotic assay |0.5gmineral/100mL in250mLflasks;100microlitre inoculum/~10^6CFU/mL;initialpH6;MgSO4·7H2O1g/L,KCl0.2g/L,NH4Cl1g/L,glucose10g/L;noP reagent added;roomtemperature,180rpm,30days,triplicate.|
| Comparators | Unbuffered Exp-Biow;20mMMES Buffered-Biow;uninoculated mineral controls;mineral-free cell controls;Exp-bags with mineral in10kDaMWCO dialysis bag. Methods Sterile and Results Control labels refer to the corresponding uninoculated arms.|
| Fraction/endpoint |0.22micrometre filtrate diluted in2%HNO3,ICP-MS. Day30totalREE~1698,84,490micrograms/L for unbuffered,buffered,dialysis arms. UnbufferedLa~643 andCe~805micrograms/L. These are aqueous concentrations, not mineral extraction percentages.|
| Null/controls | Sterile and no-mineral controls reported near ICP-MS detection limits. NumericDL and control-series concentrations are absent from inspected sources; Data 5 contains only the three inoculated mineral arms.|
| Chemical assay |0.1g/20mL sterileHClororganicacid in50mLtubes;1or0.02mM;initialpH3,5,6;roomtemperature,180rpm,96hours. Different matrix/duration from30daycultures. AtpH6,20micromolar tartaric/gluconic acids yield~130.9/~134.8micrograms/LtotalREE.|
| Proposed mechanism | Acidification plus ligand-mediated mobilization is plausible. UHPLC-MS signals are relative annotations, not absolute acid molarities. No specific acid necessity, cellular pathway, or standalone direct-contact contribution is demonstrated.|
| Surface/scale | SEM shows cells,etching and fineREE-bearing material. EDS does not uniquely identify its phase; SI XRD shows no obvious new phase. Closedmassbalance,isolatedproduct and industrialdeployment are absent. Clayretention inweatheringprofiles is inference, not direct adsorption measurement.|

## Conflicts and nulls preserved

1. Source late unbuffered pH~3.5 differs from Figure 2/Figure 8 and Data 2 nearer3.7. Day30means are3.7567unbuffered,5.7567buffered,4.44dialysis; nominalpH6 is not exact constancy.
2. Discussion growth increments below tenfold conflict with the early Data 3/Figure 2 increase from~1.23million to70millionCFU/mL. Counts exclude attached cells.
3. XRD's~3wt%quartz and XRF's0.635wt%SiO2 are unreconciled estimates; exact phase purity is not inferred.
4. Main pH3organic-acid range1915–2180micrograms/L omits Data 6crotonic mean1793.76. AtpH6, the prose's nonmobilization statement coexists with lowmeans up to~2.8micrograms/L and blank cells; neither blanks nor near-background measurements become exact zeros.
5. Dialysis changes pH,cellcounts and possibly transport. Lower filteredREE cannot quantify an isolated direct-contact effect. Sorbed and precipitated REE inventories were not separated, so concentrations do not provide a closed extraction yield.
6. Chemical leaching is96hours and the culture assay30days; culture metabolomics have no absolute molarity calibration. Exogenous strong-ligand efficacy therefore does not establish the identity or quantitative contribution of the active endogenous ligand.

No native quantitative observations were added: the endpoint is aqueous micrograms/L and the current native contract is source concentration cells in mg/kg with an actual analysis date. Qualified prose preserves the reported denominator without fabricating a conversion.

## Deferred sources and acquisition stopping points

- [Zhang et al., DOI 10.1016/j.chemgeo.2018.03.023](https://doi.org/10.1016/j.chemgeo.2018.03.023), *Chemical Geology*483:544–557(2018): publisher main access blocked; metadata APIs did not supply full text; bounded institutional/exact-title searches found no usable full main. Complete publisherSI DOCX acquired (`raw/2018-supplement-1.docx`); all captions read, only FigureS3 visually inspected. LabelsFXJ1.172,FXJ5.006,R171,FXJ1.532 are strain labels, not independently resolved species. The four organisms,media,matched-pHcontrols,rockvsmineralassays and quantitative denominators require main-text verification. No abstract values were adopted.
- [Liang et al., DOI 10.1016/j.jre.2025.03.025](https://doi.org/10.1016/j.jre.2025.03.025): Crossref identifies *Journal of Rare Earths*44(1):290–298,January 2026;2025 in the DOI/online lead is not the issue year. Complete publisherSI DOCX was acquired (`raw/2025-supplement-1.docx`), text/captions read; its embedded figures were not visually reviewed. Publisher indexed preview is not complete primary access. Full main and figures, proposedGQ984157 identity,preparedfeed/pyrite and abioticcomparators remain required.
- DOI 10.1016/j.biortech.2025.132680 is an additional distinct2025 lead, not the JRE article and not curated from its abstract.

No author messages, purchases or bypass of access controls occurred. The He 2025 complete experiment supports the narrow record without these deferred studies.

## Deduplication, search and notice coverage

Hidden and ignored files were included with `rg --hidden --no-ignore --follow`. Record/research/review/history trees in both the round29 worktree and original checkout were searched for bastnaesite/bastnasite/bastnäsite, normalized targetDOIs, PIIs and strainlabels. Referenced raw scope: round13-mineral-raw,round12-aluminium-boron-raw,round4-mineral-hosts-20261011,cmm-next-li,cmm-source-li2024.html and round28-mineral-frontier search/hit receipts. Existing hits were prior research/frontier leads; no accepted family record or accepted2025 experiment was found before this addition within these boundaries. This is not a machine-wide absence claim. See `dedup-hits.txt` and `dedup-prefreeze.txt` outsideGit; the JSON lists exact boundaries.

Bounded public search covered DOI/exact-title acquisition leads, repository metadata, primarypublisher supplements, Mendeley, IMA and NCBI. The final reproducible queries are preserved in `final-search-assessment.json` and the companion JSON. No relevant correction/retraction notice was located in the first-result search batch; inspected Crossref metadata supplied no update notices. This is a bounded notice check, not proof that no notice can exist. Direct publisher 403/429, Mindat 403 and Mendeley version-route 404 are explicitly logged. No metadata-only response is described as fulltext.

## Handoff and follow-up

The parent owns batch gates and publication; an independent agent has the frozen record,history, primary PDF, SI, all figures, dataset and issuing-authority receipts. Source disagreements are retained as limitations, not corrected by guessing. The separate formal review must decide acceptance against these exact bytes. All bulk sources remain under `/private/tmp/cmm-round29-bastnaesite-research`. Companion JSON records artifact SHA-256 values and acquisition results; the maintained files contain only the authored assessment and metadata.
