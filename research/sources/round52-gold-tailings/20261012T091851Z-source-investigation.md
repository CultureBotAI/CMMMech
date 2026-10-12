# Gold-mine-tailings primary-source investigation

UTC: 2026-10-12T09:18:51Z

Curator: codex (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round52-20261012`; base `79ed7d69ea654d1b67bbf74bb931ff70c4c6913e`.

Decision: curate **gold-mine tailings**, a processing-derived secondary resource, with narrowly qualified chemical pretreatment and culture-associated solution extraction. Independent scientific review is pending. The evidence does not support causal synergy, a particular REE-host mineral, an isolated REE product or industrial deployment. No constituent criticality is inherited.

## Sources and actual inspection

Fereydouni, Naseri and Mousavi (2025), Scientific Reports 15:4478, [DOI10.1038/s41598-025-88594-0](https://doi.org/10.1038/s41598-025-88594-0), published 6 February 2025; PMC11803100. The complete 12-page publisher PDF, full publisher HTML and EuropePMC XML were freshly acquired. All 12 original rendered pages, all 7 figures with their panels, Table 1 and all equations were personally inspected. The originalPDF SHA is `59bded7b2b8b63224d977b1052cbe205ecfa3bd5ee77f3a4dd79927807371bc0`; page images are under `/private/tmp/cmm-round52-gold-tailings-research/raw/pages/`.

No supplementary-material node was present in complete XML and no supplement/MOESM link was identified in the acquired publisher HTML. Data Availability on p. 10 says underlying data are available from the corresponding author on reasonable request; no raw dataset was acquired. A browser re-open hit Nature's identity redirect, while the direct official PDF/HTML acquisition succeeded. Original content has CC BY-NC-ND4.0 terms; bulk artifacts remain outside Git.

NCBI Taxonomy 930 was freshly retrieved from its official XML API and maps to *Acidithiobacillus thiooxidans* at species rank. PTCC 1717/IROST is the primary paper's stock attribution, not independently authenticated by that species mapping or by an acquired PTCC catalogue. Fresh Crossref metadata has no update-to/related notice; exact DOI/title correction/retraction searches returned no applicable notice in the inspected ranked sets. This is bounded notice coverage, not a claim that all notices were exhausted or a separate Crossmark status check.

## Identity and deduplication

The source names the **Mouteh Gold Factory tailings dam** and uses one air-dried, mesh 200-sieved batch below 75 micrometres. This supports a mixed processing-waste owner, not natural gold ore, elemental Au/REEs, a pure mineral or a commodity. Source-assigned XRD phases include quartz, clinochlore, muscovite, albite and gypsum; no unique REE host is established.

Deduplication searched both current and original checkout `data/records`, `research`, `reviews` and `history`, including hidden and ignored files and following relevant symlinks with cycle protection: 4030 text files. It then searched 3476 text files under 181 cited/current raw roots; 9 missing roots and text-format/30MB limits are listed in the paired JSON and external receipt. Unextracted binary contents were not searched. No unrelated home/temp inventory supports an absence claim. An initially overbroad instruction-file search was interrupted and excluded from this evidence.

No existing owner or accepted 2025 experiment was found within that scope. A prior round19 publisher page contains this DOI only as an article recommendation. Other downloaded-text hits cite a 2022 gold-tailings experiment or generic tailings context; numeric false matches were examined. This is material/normalized-source/experiment deduplication, not filename novelty.

## Evidence contract and adversarial limits

| Stage or evidence | Supported observation | Boundary |
|---|---|---|
| Chemical oxalic pretreatment | Methods p.2 specifies500rpm/6h/filtration; Conclusion p. 10 additionally specifies2M/90°C/60mL per g | These conditions are corroborated beyond the abstract; the ratio belongs to pretreatment, not bioleaching. Rinsing/carryover and residue mass are undocumented. |
| Chemical outcomes | p.3 reports at most20% Fe dissolution and Pr/Ce/Eu below0.01mg/L in leachate | Below detection is not zero or complete retention; no closed balance. |
| Culture | PTCC 1717 source attribution; sulfur5g/L, ammoniumsulfate2g/L, listedphosphate/magnesiumsalts0.25g/L each, KCl0.1g/L | Propagation10%v/v and bioassay2%v/v are separate source statements. No experimental-stock or purity authentication. |
| Assay |100mL medium/250mLflask,30°C,140rpm,7dayleaching after claimedday12addition | Bioleach loading, postpretreatment feed assay, replicates/errorbars and filtration cutoff are unavailable. Methods end-log versus Results onset-log is unresolved. |
| Figure 2/Equation 1 | Authors report pretreated Pr57→76%, Ce31→46%, Eu5→14% fromdays3→7; untreated7daybarslower | Equation 1 is leachate amount divided by statedfeedinventory, not isolated recovery. Missing feed mass/residue inventory prevents recomputation. Decimal/rounded improvements are compatible with percentage-point differences, not proven relative gains. |
| Controls | p.4 asserts near-zero no-inoculum controls under same conditions | Values deliberately omitted fromFig2; no displayed matched-acid, cell-free or dead-cell comparison. No quantified microbial advantage or factorial synergy. |
| Growth Figure1 | Panel1a counts decline on14dayaxis; panel1b has7daypH/Eh series | Firstplottedcountaround4e8 vsprose4e6; plottedpH0.8→0.6→0.8 doesnotshowclaimedpreculture3.5→0.7. Countsarehemocytometer,notCFU/deathproof. |
| Structure Figures3–6 | Qualitative phase/FTIR/surface changes | Peak loss doesnotquantifyphasepurity/REEhostflux; source firstclaimsremovedthenpartialclinochlore/gypsum. Figure3labels hydrogenoxalatehydrate withouta newlycuratedspecies. |
| Composition | p.2 bulkFe322743mg/kg; Figure6EDXFe15.65→5.12→1.71Wt.% | p.5 incorrectlyrepeatsFevalueasmg/L; proseEDXv/vconflictswithgraphicWt.%. MiddleAl+Fesum89.47%; EDXAl84.35–98.29% differsgreatlyfrombulkAl527mg/kg. No bulkbalance is inferred. |
| Kinetics Figure7/Table 1 | FittedchemicalmodelhaslargerR² thanitsdiffusioncomparator | p.10 quotesEudiffusion0.9168 aschemical; originalchemicalR²0.9611. Sulfate-adjustedfitsareworseinTable 1despiteproseclaim. Fitsdonotproveunique ratecontrol. |

The laboratory trial used one batch; qualitative morphology and reported extraction cannot establish a general gold-tailings process or industrial performance. The native concentration-observation schema was not used: these feed concentrations occur in prose without source analysis dates and are not its exact numeric-table contract.

## Related experiment and remaining priorities

Reference 19 is [Hosseini et al. (2022), DOI10.1016/j.jtice.2022.104482](https://doi.org/10.1016/j.jtice.2022.104482), an adapted-culture one-step Ce/Sr study. Publisher/Coventry metadata and abstract/introduction were inspected, but its complete methods/graphics/SI were not acquired in this bounded pass. Its abstract yields and2%loading are **not imported** into the 2025 assay. Obtain complete originals and compare feed provenance, stock adaptation and experiment overlap before an extension; independent batch/replication cannot be inferred from different publication dates.

Immediate clarification priorities are the withheld control/raw data, actual bioleaching solids and postpretreatment inventories, residue washing, biological time axis/cell exponent, EDX basis and replicate/error definitions. These limits are preserved in the accepted-record draft rather than silently repaired.

## Maintained output and checks

- Record `data/records/gold-mine-tailings.yaml`, SHA `54f1e3c571e36c08845855ec50cb89f95bb91dd58e71d255e8922b28eecbd7f1`.
- CREATE sidecar `history/records/gold-mine-tailings/2026-10-12T091525Z-codex-622d1c.yaml`, SHA `7823f1f762c0ff2a2625d705dbfa28c654341dd440d5bc860fb23fcafd4b01f1`; actual distinct inline CREATE event retained.
- Named validation terminal 0: `Checked 1 record(s); 0 failed.` The baseline is the parent's explicitly reused exact published-base receipt; this curator did not run whole-corpus gates or claim final independent acceptance.
- Paired JSON lists 20 raw artifacts and exact hashes, acquisition/dedup/freeze receipts and query scope. Bulk originals remain under `/private/tmp/cmm-round52-gold-tailings-research`.

No shared README/schema/governance/Git/GitHub mutation was performed. The independent reviewer must capture the record, history, both dossier formats and schema before assessment.
