# Round 26 source investigation: electric-arc-furnace dust

UTC: 2026-10-11T15:32:04.058234+00:00. Researcher: Codex (GPT-6; round24_copper_slag). Trusted base: `d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`; branch `curate/cmm-expansion-round26-20261011`. Tracking issue: [#93](https://github.com/CultureBotAI/CMMMech/issues/93). This assessment accompanies new record `data/records/electric-arc-furnace-dust.yaml` and its CREATE history; independent acceptance and final batch gates are separate.

## Scope and selection

The round 25 frontier identified a new EAF-dust lead. The [2025 primary](https://doi.org/10.1016/j.rcradv.2025.200278) supplies actual dust origin, duplicate leaching assays and a downstream microbial electrolysis experiment. It extends coverage beyond cast-house dust with a distinct process-defined secondary resource. Dust, constituent zinc, mineral phases and slag remain distinct. No criticality claim is made, so no list edition or jurisdiction is inferred.

Hidden, ignored and relevant symlink-following searches covered `data/records`, `research`, `reviews` and `history`, plus the three named prior raw directories in the paired JSON. The exact pattern and receipts are preserved there. Existing frontier leads and explicit cast-house exclusions were found; no pre-existing EAF-dust root was found in that scope. Unrelated home/temp trees were excluded.

## Search and acquisition

The paired JSON preserves all 12 exact web queries, first-result-set bounds, dates, acquisition URLs/timestamps/statuses and hashes. No pagination or implicit exhaustive review is claimed. Exact DOI/title searches checked corrections, errata and retractions; none appeared in those returned sets. Crossref independently matches the title/DOI and reports neither update-to nor related correction, which does not prove notice absence.

The [K1-MET full PDF](https://www.k1-met.com/fileadmin/user_upload/Publications/Journal_articles_open_access/Frueholz_et_al__2025__Zn_recovery_EAF_dust_biotechnological_ResCons_RecyclAdv_27_paper_200278.pdf) was freshly downloaded at 2026-10-11T15:25:36Z. SHA256: `546dd93365556668101e219980f2b6d02301757385331caabd50bddc4a012139`. All nine pages and Figures 1-9/Tables 1-5 were visually inspected. It is the September 2025 issue article, available online 16 July 2025; the Crossref license-start date of 15 July is kept separate. CC BY-NC 4.0 applies; full text and renderings remain outside Git.

Direct publisher HTML returned 403. Three conventional publisher `mmc1` extension probes (DOCX/PDF/XLSX) returned 404; these were probes, not observed supplement links. No supplemental appendix was identified in the inspected main article or indexed publisher output. Data are available on request according to the paper. No raw data deposit, complete balance or data dictionary was acquired; this is not a claim that none exists. Initial sandbox DNS failures and successful legitimate retries are in the acquisition log.

The [cited 2023 primary](https://doi.org/10.3389/fmicb.2023.1238853) was downloaded to verify Equation 1 and Equation 2 on page 3. Its complete 11-page PDF is retained, but this investigation visually inspected only the method page and read the relevant methods/calculation text. It is method context, not a newly accepted blast-furnace experiment. DSMZ [DSM 504](https://www.dsmz.de/collection/catalogue/details/culture/DSM-504) and NCBI [species 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info) were checked live; neither authenticates the experimental stock.

## Claim-level assessment

The primary uses two EAF dusts supplied by a steelmaking company. Supplier country and exact mineral phases are not stated for these samples. Acidithiobacillus thiooxidans DSM 504 grows upstream on elemental sulfur; the acid is filtered before dust contact. Duplicate 50-mL assays are distinct from the 3-L acid generator. At 30 degrees C, 100 g/L and 10 minutes, Table 5 Dust 2 Zn 29900 mg/L and Fe 3.0 mg/L approximately reproduce the abstract's 76.67% and 0.02% using Table 4 inventories. No matched reagent-acid or uninoculated acid-generation control establishes a biological advantage.

A separate mixed-culture MEC anode is fed simulated wastewater and externally held at -100 mV versus Ag/AgCl. This is an anode potential, not a cell voltage or passive power-generation claim. Purified, diluted Dust 2 leachate enters the cathode; seven weekly serial cycles share the same operating system. No taxon identifier is assigned to the unresolved anode community. The near-total Zn percentage is explicitly a catholyte-depletion metric. Acid-dissolved electrode deposits were analyzed for selected metals, but a complete deposited-mass balance, zinc phase/oxidation-state analysis, independent MEC replication and matched abiotic/open-circuit controls are not supplied.

## Contradictions and limits retained

- **Abstract versus Results 3.2 and Figure 7B:** Abstract Fe precipitation is 48%; Results and the plotted bar give about 42% at pH 3.8. No corrected number is invented.
- **Tables 4-5 versus Figure 6, Dust 1 at 100 g/L and 10 minutes:** 9745 mg/L divided by the Table 4 dust inventory, 161000 mg/kg times 0.1 kg/L, implies about 60.5% Zn extraction. Figure 6 instead depicts about 30%. The 2-minute textual value 28.9 +/- 0.2% is not a replacement for the 10-minute datum. Other Dust 1 table/figure pairings also fail to agree; its extraction is not silently harmonized.
- **Methods 2.5-2.6, Table 3 versus Table 5:** The purified, stated 1:1-diluted MEC feed contains 1785 mg/L Zn, whereas the best Dust 2 leachate contains 29900 mg/L. The particular preliminary batch and losses/dilution connecting them are insufficiently specified. No overall dust-to-product yield is computed.
- **Methods 2.7 and cited Spiess 2023 Equation 1; Results 3.3:** 99.9 +/- 0.1% is catholyte concentration depletion over seven serial cycles, not weighed electrode yield or recovery of all dust zinc. The selected-metal ICP composition is 99.15% Zn, not a complete elemental/phase/product purity certificate.
- **Methods 2.5:** The hydrogen peroxide wording 30 vol% does not unambiguously distinguish stock strength from amount added. No invented final peroxide concentration is assigned.
- **Methods 2.7 and Results 3.1:** Acidity is calculated rather than titrated, reported as approximately 0.5 M with average sulfate around 50 g/L and pH 0.3. Exact per-assay acid inventories and the concentration/speciation convention are unavailable; no curator-recalibrated acidity is supplied.
- **Methods 2.3 and 2.6; Results 3.3:** Duplicate leaching assays and seven serial MEC cycles do not establish independent reactor replication. No matched reagent-acid, abiotic-anode or open-circuit comparator is reported. Broader energy and reuse comparisons are not measured advantages for this system.

The paper labels liquid analysis ICP-OES while citing ISO 17294-2, a method-label/standard combination that is not independently resolved here. Neither that citation nor the selected-metal assay is promoted to a phase or complete-purity measurement. Reuse of recovered zinc and iron-rich residue, comparative energy savings and industrial operation remain proposals/context rather than verified outcomes of this laboratory experiment.

## Curation mapping and handoff

The new record uses `secondary_resource`, one `bioleaching` mechanism and one `recovery` mechanism. Required claim context and limitations fit the existing schema. Numeric outcomes remain qualified prose; Table 4 has no analysis date for the native exact-concentration contract. No schema/validator edits or manufactured quantitative observations are justified.

Record SHA256: `528841c1923db4f091500d3de5d57d5a13274f8886f9f0a610eafd05e89217b7`. History: `history/records/electric-arc-furnace-dust/2026-10-11T153000Z-codex-86367d.yaml`; SHA256 `f23e97d1512683cc39f82f54911dccfc8eed6cf3521bb104c02386902d813521`. Named validation completed with terminal 0 and one record/zero failures (`/private/tmp/cmm-round26-eaf-dust-validate.log`). The parent baseline passed 308 tests with three skips, 165 records and 186 histories; this report does not substitute for the final batch or independent review.

## Ranked priorities

1. Independently review the new record against complete primary figures, staged denominators, strain authority and source conflicts, then run batch/history/review gates. Ready for independent review.
2. Obtain author clarification or deposited raw tables for Dust 1 table/figure disagreement, Fe precipitation discrepancy, exact MEC feed provenance and a full deposit mass balance. Unresolved; no contact authorized in this author lane.
3. Assess the 2023 blast-furnace-dust MEC primary as a distinct feed/possible existing-root extension only after resolving exact dust origin and auditing all results. Methods context checked only; not accepted as additional material evidence.
4. If comparative performance is needed, acquire and audit the 2026 acidic/brine EAF-dust paper before comparing it with microbial processing. Primary publisher metadata lead only. No full methods, measurements or equivalence claim assessed.

Raw artifacts, text and page renderings are retained under `/private/tmp/cmm-round26-eaf-dust-raw`; all file hashes and precise acquisition provenance are in the paired JSON. Author clarification, per-cycle raw balances and matched controls are the main remaining scientific dependencies. No author contact or GitHub publication was performed in this author lane.
