# CMM source investigation: mackinawite

UTC: 2026-10-11T21:11:57Z

Curator: codex (GPT-6; codex). This is a curation handoff, not an independent scientific acceptance review.

## Scope and provenance

Worktree `/private/tmp/CMMMech-expansion-round34-20261011`, branch `curate/cmm-expansion-round34-20261011`, trusted base `38cef46aabbcb2b49536ed8c265c63646ff1da3d`. Own additions are the mackinawite record, CREATE history and this dossier. The parent explicitly reuses the exact published-base baseline in `/private/tmp/cmm-round34-baseline-reuse.json`; no fresh baseline execution is claimed here.

Read the current add-record and source-discovery skills, CLAUDE, record contract, schema and relevant validator/test conventions. Local skill copies match installed copies. Exact ancestor AGENTS file probes found no files; the user-supplied ignored-inclusive search instruction applies.

The selected identity is mackinawite mineral species. Generic FeS, elemental iron, pyrrhotite, greigite, pyrite, a natural ore and a laboratory precipitate are not interchangeable. Selection of the Picard primary was communicated before writing the record. No constituent criticality, natural-feed extraction or industrial deployment is inferred.

### Deduplication boundary

Searched current and original checkout `data/records`, `research`, `reviews` and `history` using `rg --hidden --no-ignore --follow`, for mackinawite, the normalized selected DOI and both dataset IDs. The existing antimony record includes an abiotic mackinawite comparator; pyrite mentions proposed secondary mackinawite. Neither owns this mineral identity or the Picard experiment. No selected DOI or dataset match was found in this stated corpus boundary, including hidden and ignored files and followed links.

Also searched referenced raw roots `/private/tmp/cmm-round33-pyrite-research`, `/private/tmp/cmm-round4-antimony-evidence-20261011` and `/private/tmp/cmm-round32-molybdenite-research`. All seven PDFs encountered in those roots were text-extracted with PyMuPDF, without errors; directory links were followed with resolved-path cycle prevention. Existing Payne FeS, antimony comparator, pyrite synthesis and IMA matches were treated as related context. Images and binary archives were not claimed to be searchable text. Retained extractions and source identities support experiment deduplication. Full search receipts and hashes are in the JSON companion; this is not a machine-wide absence claim.

## Search and acquisition log

The JSON companion records exact live search queries, 2026-10-11 UTC, and acquisition URLs/times/results. Searches used the first returned results without exhaustive pagination, covering source access, phase identity, strain identity and bounded notice/counterevidence discovery.

[Picard et al.](https://doi.org/10.1016/j.gca.2017.10.006), GCA 220:367–384, is a 2018 issue publication, available online 16 October 2017. The complete 18-page author-hosted PDF text was read through the web reader. Seven saved chunks cover every numbered line 0–1344; `picard2018-complete-webtext.txt` is their derived union, not a downloaded PDF. Public direct download returned 403 with urllib and one curl attempt. Publisher API supplied metadata only; full view returned 401 and requested PDF returned 406. These failures are retained.

All seven original publisher figure images were downloaded and visually inspected. The original four-page supplement has the matching title/authors and three figures, S1–S3; all were inspected. Tables 1–3 were inspected in full-text extraction. Web screenshot calls did not expose usable images in this runtime, so they are not counted as visual inspection. Main PDF bytes were not retained and no checksum for them is claimed.

Crossref and publisher metadata confirm title, authors, DOI, issue and the article's CC BY-NC-ND 4.0 license. Full text/images remain outside Git. Crossref explicitly links the two BCO-DMO datasets. Its retrieved response contains no linked correction/retraction; exact-DOI notice searches found no notice. This is bounded evidence, not proof that no notice exists, and no independent Crossmark status response was obtained.

## Candidate inventory

| Candidate | Evidence actually inspected | Decision |
|---|---|---|
| [Picard 2018](https://doi.org/10.1016/j.gca.2017.10.006) | Complete primary text, Tables 1–3, all seven original figures and complete SI | Curate narrow phase formation and biomass-associated growth. |
| [IMA September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Authority PDF, opening definitions and original page 130 row | Mackinawite, FeS, approved A, 1967 s.p.; no invented CURIE. |
| [NCBI 1121451](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1121451&mode=Info) | Live authority HTML | Current Maridesulfovibrio hydrothermalis AM13 = DSM 14728; source Desulfovibrio synonym retained. |
| [BCO-DMO XRD](https://www.bco-dmo.org/dataset/684634) and [sulfide](https://www.bco-dmo.org/dataset/684417) | Landing pages, dictionaries and complete CSV files | Related observations, not additional independent studies; no quantitative import. |
| [Thiel 2019](https://doi.org/10.1073/pnas.1814412116) | Complete JATS/media/SI acquired; selected methods and phase lead examined | Defer complete assessment; do not assign mackinawite from FeS formula. |
| [Rapid pyritization 2020](https://doi.org/10.1038/s41598-020-64990-6) | JATS acquired; discovery passages/metadata examined | Defer full review of distinct consortium and controls. |
| [Frontiers 2020](https://doi.org/10.3389/feart.2020.588310) | Discovery result only | Follow-up for conditional pyrite versus mackinawite formation; not accepted evidence. |
| Payne 2021 FeS and Johnson 2021 antimony comparator | Existing reports and retained extractions searched | Related existing context, not the selected experiment. |

## Claim-level assessment

Sections 2.1–2.2, Table 1 and S1 identify DSM 14728 AM13, washed stationary cells, sulfate/lactate marine bicarbonate medium, 50 mL in 110 mL bottles, 35 degrees C, nominal 4 mM Fe(II), initial pH 7.03. Live arms began near 10^6 or 10^8 cells/mL. Gamma-inactivated cells received 2 Gy/min for 48–72 hours, were washed, then spent two weeks in Fe medium before reagent sulfide addition. Cell-free controls received sulfide once or daily over six days. Another arm received Fe after a live culture had already produced sulfide. The record does not conflate these arms.

Figure 1 and S2 expose differences in sulfide delivery. Table 2 reports mean initial Fe 3.81 ± 0.17 mM and final pH about 7.06, 7.30 and 7.37 for live, abiotic and inactive-cell conditions. Controls approximate rather than exactly match exposure and pH. The extra dead-cell pretreatment permits vivianite formation, also seen in selected abiotic samples.

Figure 2A/B identifies mackinawite after one week and two months in all arms. Reference diffraction patterns are actually in panel D, although the caption says B. Chemical controls also form mackinawite. Figure 2C detects greigite in the five-month live Fe treatment; Section 4.2 says greater than five months and reports residual mackinawite at eleven months. The record preserves conditional phase evolution without asserting complete conversion or direct enzymatic Fe oxidation.

Table 3/Figure 3 compare Scherrer-derived domain sizes across pooled results: 10 live (1–11 months), 5 inactive (1–5), 11 abiotic (1–6), 5 post-growth Fe-addition (1–5). These are not counts at every time point. Inactive-cell c-axis size is 18.5 ± 7.7 nm in Table 3 versus 18.7 ± 7.7 in Results 3.2; no reconciled point estimate is adopted. DLS aggregate size and selected microscopy dimensions measure different properties, not recovery fractions.

Figure 4 supports texture and aggregation differences. One prose sentence calls C/D abiotic, but the caption and panel row assign abiotic material to E–H; no quantitative claim is extracted from this slip. Figure 5 SEM surfaces appear smooth, while Figure 6 thin sections show encrustation, an imaging difference explicitly discussed in Section 3.4. Fe/S maps do not resolve mineralogy at each cell surface; local phase attribution is inferred from bulk XRD. Figure 7 shows damaged, encrusted inactive cells. Biomass effects do not imply metabolism in dead cells. EPS and cell-binding pathways are proposed explanations without isolated-polymer or gene-disruption assays. Approximately 60% FeS in crusts is a geometric estimate, not measured recovery.

No pyrite or marcasite was detected in the tested samples. Section 4.5 limits extrapolation from high reagent concentrations to natural sediments. Different conditions in other studies can support pyrite formation without refuting this conditional null. No criticality, ore extraction, purified-product yield or deployment claim is added.

## Dataset reuse assessment

BCO-DMO associates the paper with DOI `10.1575/1912/bco-dmo.684634.1` and `10.1575/1912/bco-dmo.684417.1`, version 1, final/no updates expected, CC BY 4.0. Exact landing-page metadata is retained in each dictionary JSON. Portal and acquisition dates are not publication or experiment dates.

The XRD file has 1,978 observed rows and three columns: 989 rows each for biotic and abiotic 4 mM Fe treatments, described as one-week observations. `(experiment_type, angle_2Theta)` is unique in this file. There is one `nd` token and 340 negative intensity values. Negative processed intensities are not negative concentrations or detection-limit codes. The dictionary labels angle unitless, whereas the primary plot specifies 2-Theta degrees. No raw-data refit or reconstruction of all time points is claimed.

The sulfide file has 65 observed rows and 12 columns, 50 biotic and 15 abiotic rows, and 469 `nd` tokens. Named culture columns distinguish replicates. `(experiment_type, time)` is not unique, including before/after sulfide additions at the same time. A future import must retain row identity/order and culture column. The dictionary describes concentration units as `micromolar (mM)`, internally inconsistent; primary Figure 1 labels mM. No silent correction, unit conversion or zero substitution is made. These observations do not fit the current mg/kg concentration-cell contract and are not imported.

## Handoff and validation

Frozen [record](../../../data/records/mackinawite.yaml) SHA256 `8710787a7c9658a26b83d6fe7306f7e338f31ee823747ac3b259b26d9367e507`.

Canonical [CREATE history](../../../history/records/mackinawite/2026-10-11T210936Z-codex-4cb40f.yaml) SHA256 `099842aa60a4d74cab11be1caab19c5c6fab46bb31f78cd406abedc31b60c538`. A distinct actual UTC inline event is attached. Named validation exited 0: one checked, zero failed. No schema or validator change was required. Another agent conducts scientific review; parent batch gates remain separate.

Priorities: complete independent review of the frozen record; then, if desired, assess the retained Payne FeS arm and Thiel/2020 phase-formation studies with their own controls and strain resolution. Do not pool those experiments with Picard AM13. Quantitative dataset reuse needs unit-dictionary clarification and stable row keys.

## Artifact receipt and limits

Raw files remain under `/private/tmp/cmm-round34-mackinawite-research/raw`. The JSON companion pins all raw/derived artifacts, bytes, SHA256, acquisition URLs/times and bounded dedup receipts. No raw bulk source is committed. Dataset links do not independently confirm the experiment. Exact acquisition failures and source discrepancies remain visible. Source access, curation and independent acceptance are separate claims.
