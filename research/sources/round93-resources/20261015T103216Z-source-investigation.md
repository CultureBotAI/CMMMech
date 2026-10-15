# Round93 secondary-resource source investigation

Assessment saved 2026-10-15T10:32:16.720419+00:00; curator Codex (GPT-6; Codex), lane `/root/round68_new_frontier`.
Worktree `/private/tmp/CMMMech-expansion-round93-20261015`, branch `curate/cmm-expansion-round93-20261015`,
trusted base `e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d`.

## Selection and scope

Selected **pig manure**, an unincinerated agricultural secondary resource, from a directly studied fresh farm sample. It is not municipal sewage sludge, poultry litter, manure ash or an isolated fertilizer product. One resource owner covers the studied material and its diluted slurry; no facility-specific or liquid/solid duplicate is proposed. No criticality designation, material authority identifier or confirmed community species is assigned.

The accepted study is Wei, Liu, Liao, Wang, Li and Huang (2018), *Bioleaching of heavy metals from pig manure with indigenous sulfur-oxidizing bacteria: effects of sulfur concentration*, Heliyon4:e00778, DOI[10.1016/j.heliyon.2018.e00778](https://doi.org/10.1016/j.heliyon.2018.e00778), PMID30211335, PMCIDPMC6129760. The original gives received26December2017, revised25April2018, accepted5September2018, with September2018 publication; repository access in2026 is not its publication date.

## Search bounds and novelty

The dated query list and acquisition receipts are in the paired JSON. Searches used `rg --no-ignore --hidden --follow` across `data/records`, `research`, `reviews` and `history`, with feed terms, aliases and normalized DOI fragments. The current municipal-sewage-sludge and copper-autoclave-slime owners were read, as were relevant round57 and round89 source reports. A broader current-owner search included manure, livestock, poultry, piggery and swine. It found no existing owner for this feed. Exact candidate and related-paper terms found no maintained assay duplication. This is a bounded assessment, not a machinewide or literature-exhaustion claim.

Relevant prior downloaded roots were `/private/tmp/cmm-round86-resources-research`, `/private/tmp/cmm-round57-anode-slime-research` and `/private/tmp/cmm-round89-resources-research`. The only manure-term hits there were unrelated bibliographic/background mentions in round89 Guo2024 and Martin2021 text. The219 all-state issues in `/private/tmp/cmm-round93-initial-issues.json` yielded no matching pig/swine-manure or accepted-DOI issue. No issue was posted by this curator.

## Original evidence and acquisition

The complete official EuropePMC JATS and PMC HTML were acquired and read. All seven original main figure JPGs were visually inspected; all six tables were checked in the original JATS/HTML. The official supplementary-files endpoint delivered **14 members: seven main figures each in JPG and GIF form**, not fourteen independent figures or a separate SI study. The original has no supplementary-material callout and says no additional information is available. This observation does not prove that no unpublished data exist.

The EPMC PDF route returned403. The PMC path ending `main.pdf` returned HTML challenge bytes, retained under its attempted filename but explicitly rejected as a PDF. Complete text and original graphics were available without it; no PDF page-inspection claim is made. The PMC OA API attempts returned404. Initial unprivileged journal requests failed DNS; network-authorized Damietta routes returned429. All attempts and successful original checksums are retained outside Git and listed in JSON. The article states CC BY-NC-ND4.0; full text/graphics stay outside the repository, whose dossier is a paraphrased assessment. NCBI930 XML was freshly read only to verify the reference species name/rank.

## Claim-bearing assessment

**Feed and assay:** Sections2.1-2.4 and Table1 identify fresh manure from a Tianjin pig farm, stored4°C, initially23.57% solids and diluted to2%w/v. Four serial transfers in sulfur-supplemented manure generated the active indigenous enrichment. The assay used200mL slurry in500mL flasks,5%v/v inoculum,2/5/8/10g/L elemental sulfur,28°C,180rpm,12days and triplicates. Evaporation was compensated by added distilled water. Centrifuged0.45µm-filtered liquids were analyzed by atomic absorption. Final volume, sampling mass and inoculum corrections are incompletely specified.

**Organism and controls:** A separate salt-medium enrichment for clone analysis reportedly yielded sequences98%similar to *Acidithiobacillus thiooxidans*. The original cites another Wei2018 study for clone methods; that full related original was not acquired. The current owner therefore describes an unresolved active community, not a confirmed species or pure strain. There is no displayed sterile, uninoculated, no-sulfur or acidity-matched series. Sulfur-dependent culture association is supportable; exclusive microbial causation, growth kinetics and strain-specific contribution are not.

**Measured trend and tradeoffs:** Figures1-4 show dose-dependent acidification, sulfate accumulation and Cu/Zn/Mn mobilization. Section3.3 reports48.5%Cu solubilization at2g/L sulfur after12days, versus around90% or more for the higher doses; the5g/L curve is approximately90%, so the text's strict greater-than90% threshold is not adopted as an exact graphic measurement. The reported12-day Zn and Mn ranges are93.3-97.2% and96.3-97.8%. The8→10g/L increase gives little extra final metal benefit. These are reported solubilization endpoints, not isolated recovered products. Figures3/5 and Tables3-5 are fitted rates and are not independent experiments or proven molecular mechanisms.

**Negative outcomes:** Figure7 and section3.5.3 show substantial residual nutrient-concentration decreases, including reported68.5-71.0% totalP and76.5-78.8%K decreases. Their practical cost is retained. Without a residual-solid/solution mass balance these are not nutrient recovery yields. Residual sulfur and reacidification concerns are source interpretations; no fertilizer safety or field performance was tested. Figure6 uses operational sequential-extraction fractions, not direct mineral or oxidation-state identification. Its post-treatment sulfur dose is not identified, so no precise dose-specific fraction claim is adopted.

**Contradictions preserved:** Section3.1's listed times to ORP>200mV have dose ordering inconsistent with Figure1b. Table4's sulfur heading saysmg/L while Methods/figures sayg/L. Methods2.4 specifies two-day sampling while Figure4 displays daily points. Figure7's caption says nitrate/phosphate whereas its axes and methods say totalnitrogen/totalphosphorus. Table1/Figure7TOC mg/kg and Table6carbon wt% have unresolved assay/unit compatibility. None is silently repaired into exact rates, speciation or closed yields. Dewaterability and safety are inferred in the discussion, not directly demonstrated.

## Corrections, counterevidence and deferred leads

Crossref's retrieved accepted-paper record has an empty relation object and no update-to entry. A bounded exact-DOI correction/retraction/erratum query did not surface an attributable notice. This is not an exhaustive notice guarantee. Related originals on biochar addition (DOI10.1016/j.scitotenv.2018.03.140), solids effects (10.1007/s11270-019-4087-z) and iron/sulfur comparisons (10.1007/s11270-020-4415-3) are further leads only; metadata/abstract values are not adopted or counted as replication. The original study's own nutrient-loss and diminishing-benefit results supply relevant negative evidence.

The poultry-litter Bacillus lead, El-Katony et al.2015, Damietta5(1):101–109, remains deferred: only an author-upload abstract was verified and journal routes returned429. Its RG upload DOI10.13140/RG.2.1.5004.9045 is not assumed to be a journal DOI. A second same-title RG result contained unrelated plant-salinity content and was rejected. Copper-anode-slime leads were mainly abiotic or previously screened LCA/model claims. The existing copper-autoclave-slime organism result belongs to a downstream tellurium-processing residue and is not transferred to raw anode slime.

## Curation and handoff

Owner `data/records/pig-manure.yaml`, SHA256`20caf6979236a7b9464da8e1f43fe1f95547f7d8cc0dc2576ff6b676f418a124`.
Canonical CREATE `history/records/pig-manure/2026-10-15T103022Z-codex-0ab705.yaml`, SHA256`afb4ad70190451f8c3dcfd9b5e0f0e801713c9c8dadbadc545c2aa0c29921681`; distinct actual inline CREATE retained.
The root baseline receipt was verified against its log; all listed commands exited0 before maintained writes. Named strict validation completed with1passed/0failed; raw log `/private/tmp/cmm-round93-resources-research/named-validation.log`, SHA256`6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`. No global suite, page rendering, Git or GitHub mutation was performed in this lane. Independent scientific review and final batch checks remain separate pending work.

The external draft `/private/tmp/cmm-round93-pig-manure-source-followup.md` lists concrete source-clarification questions. It is not a curator corrective finding or a posted issue. A later live issue check is required before posting. All accepted raw artifacts, metadata, failed routes and table-subtree derivations are distinguished in the paired JSON.
