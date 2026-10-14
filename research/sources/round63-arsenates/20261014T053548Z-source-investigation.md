# CMM source investigation: scorodite

## Scope and provenance

UTC timestamp: 2026-10-14T05:35:48.880327+00:00. Researcher: codex, GPT-6, codex tool, delegated agent `/root/publication_completion_check`. Worktree `/private/tmp/CMMMech-expansion-round63-20261014`, branch `curate/cmm-expansion-round63-20261014`, trusted base `1e3d834112099855c0398459415d0022336055f5`. This investigation supports one new mineral owner, `data/records/scorodite.yaml`, and its CREATE history. Concurrent nickel-resource and dypingite work belongs to other curators. No schema, governance or generated-site changes were made by this investigator.

The question is whether original biological experiments establish formation of the identified scorodite phase, with adequate organism, solution and phase boundaries. Mineral identity is distinct from elemental arsenic, amorphous ferric arsenate, parascorodite and mixed arsenic-bearing wastes. No criticality list is mapped to this mineral. Research is bounded to the selected 2018 primary study, current identity authorities, and explicitly deferred related leads; it is not a systematic literature review.

Before adding an owner, a hidden-, ignored- and symlink-inclusive search used `rg --no-ignore --hidden --follow` within `data`, `research`, `reviews`, `history`, `docs` and `.claude`, plus 379 existing CMM temporary directory roots cited by the repository. It selected Markdown, JSON, YAML and text files up to 8 MB. The 1,488 extracted tokens that were not existing directories include file paths and unavailable paths; they are not all missing directories. The repository search returned 49 lines and the cited-raw search 326 lines, both exit 0. No unrelated home or temporary directories or binary-only PDF contents were exhaustively searched. Exact commands, scope and outputs are retained in `dedup.json`, `dedup-repository.txt` and `dedup-cited-raw.txt` under the raw research root.

The bounded search found no existing scorodite owner. Existing arsenic concerns an element and different sludge experiments; mimetite is a different lead arsenate species; yanomamite mentions scorodite as an impurity. Other mineral dossiers mention proposed or secondary scorodite. Older tennantite/enargite research already cites the 2018 and 2020 studies, so this is not a claim to discovering previously unknown literature. Those references did not supply an accepted owner or the selected experimental claim. `dedup-primary-context.json` preserves relevant citation context.

## Search and acquisition log

All searches and acquisitions occurred on 2026-10-14 UTC. Raw root: `/private/tmp/cmm-round63-arsenates-research`. Exact response bodies, original source files, timestamps, HTTP statuses, sizes and hashes are indexed in the companion manifest and the two acquisition receipts.

| Provider/source | Exact query or URL | Inspected scope | Result/access limit |
|---|---|---|---|
| Web search | `scorodite biomineralization Acidianus brierleyi iron arsenic precipitation original Minerals`; `scorodite biological precipitation Sulfolobus iron arsenite full text`; `scorodite "biogenic" "supplementary" precipitation` | First returned result sets, no date/domain filters or pagination | Selected accessible original 2018 study; retained responses |
| Web search | `"scorodite" "Cummings" "1999" arsenic mobilization pdf`; `"scorodite" "tooeleite" biological precipitation primary` | First result sets only | Counterevidence and alternative-phase leads; no additional accepted study |
| Identity/notice search | `site.ncbi.nlm.nih.gov/Taxonomy "Acidianus brierleyi" "Taxonomy ID"`; `site.dsmz.de "DSM 1651" "Acidianus"`; `"10.3390/min8010023" correction retraction erratum`; `"Factors to Enable Crystallization" "supplementary"` | First result sets plus NCBI and DSMZ pages | Identity confirmed. No affecting correction/retraction found in this bounded result set; not exhaustive clearance |
| Publisher | `https://www.mdpi.com/2075-163X/8/1/23` | HTTP response retained | 403 Access Denied; publisher landing/SI navigation not fully inspectable |
| Institutional original | `https://catalog.lib.kyushu-u.ac.jp/opac_download_md/4737404/4737404.pdf` | Complete 17-page PDF: cover plus all 16 article pages; original rendered pages all inspected | 200; full article including Figures 1-4, Tables 1-3 and Appendix A Tables A1-A2 |
| Crossref | `https://api.crossref.org/works/10.3390/min8010023` | Full metadata response | Author, title, journal, DOI and publication date verification; no update relation in retained response |
| IMA-CNMNC | `https://cnmnc.units.it/index.php`; linked `https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf` | Fresh official PDF, pages 1, 2 and 195 visually inspected | Formula, status and original-description year verified |
| Handbook | `https://handbookofmineralogy.org/pdfs/scorodite.pdf` | Entire one-page original entry | Formula and parascorodite dimorphism corroborated |
| Organism authorities | `https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/41673/dataset_report`; `https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=41673`; `https://www.dsmz.de/collection/catalogue/details/culture/DSM-1651` | API, browser species page and DSM strain catalogue | Species-rank NCBI 41673 and DSM 1651 type strain association verified |
| J-STAGE follow-up | `https://www.jstage.jst.go.jp/article/matertrans/61/2/61_M-M2019858/_pdf`; matching article landing | Entire PDF acquired and rendered, methods text partly read; original image pages not visually assessed | Deferred, not used as accepted experimental evidence |

## Candidate inventory

| Candidate | Identifier/version | Role and actually inspected evidence | Decision |
|---|---|---|---|
| Tanaka and Okibe 2018 | DOI `10.3390/min8010023`, Minerals 8(1), 23; published 15 January 2018 | Complete original article and graphics, plus fresh Crossref | Curate bounded phase-formation and solution-removal evidence |
| IMA September 2026 | Current official linked mineral-list PDF | Page 195 species row and pages 1-2 definitions | Curate identity only |
| Handbook scorodite | One-page species entry | Entire original page | Supporting mineral identity, not experimental purity |
| NCBI / DSMZ | NCBITaxon:41673; DSM 1651 | Species and strain catalogue | Taxonomic grounding only |
| Okibe, Nishi, Era and Sugiyama 2020 | DOI `10.2320/matertrans.M-M2019858`; Materials Transactions 61(2), 387-395; online 20 December 2019, issue 2020 | Full original acquired, all nine pages rendered, only introductory/methods text partly inspected | Defer original-figure/results review; no accepted claims |
| González-Contreras et al. 2010 | DOI `10.1021/es902063t` | Publisher abstract/metadata and supplement existence, no complete original acquired | Defer alternate-organism crystallization study |
| Cummings et al. 1999 | DOI `10.1021/es980541c` | Publisher abstract/metadata only | Counterevidence lead on reductive mobilization; full original needed before a mechanism is curated |
| Révész et al. 2015 | Publisher PII `S0883292715300500` | Discovery metadata only | Defer reductive dissolution follow-up |
| Biological tooeleite / other arsenates | DOI/metadata discovery leads | No complete assessed original for this scope | Excluded from this bounded one-owner curation |

## Source assessment: Tanaka and Okibe 2018

The institutional repository contains the complete published original, not a new independent experiment or a new edition. Crossref and the original identify Masahito Tanaka and Naoko Okibe, Minerals 8(1), 23, DOI `10.3390/min8010023`. A prior citation list's incorrect journal label is not reused. The cover is not article page 1; raw PDF pages 2-17 correspond to article pages 1-16. All original pages were visually inspected, including the complete plots, diffraction pattern, micrographs, tables and Appendix A. No separate supplement is cited in the complete PDF; Appendix A is present. The blocked publisher landing prevents an exhaustive supplementary-file availability claim.

Sections 2.1-2.2 provide the cleanest phase-formation evidence: living Acidianus brierleyi DSM 1651T was grown without added scorodite seeds for 14 days at 70 degrees C and 100 rpm, in 200 mL heterotrophic basal salts medium in 500 mL flasks, initial pH 1.5, 18 mM Fe(II), 13 mM As(III) and 0.02% w/v yeast extract. The salts are FeSO4.7H2O and NaAsO2. Figure 1a presents original XRD identifying the collected bioscorodite material against JCPDS 37-0468; Figure 2 presents the morphology. Acidianus is an archaeon. NCBI 41673 is a species identifier, not a strain or genome identifier; the experimental DSM designation is retained in prose.

Subsequent Section 2.3 cultures begin at 1.0 x 10^7 cells/mL, initial pH 1.5 or 1.2, and variable Fe(II)/As(III) feeds; 0.15% w/v biogenic or chemical seeds are used where indicated. All experiments are duplicates. Fe(II) uses o-phenanthroline, As(III) stripping voltammetry, and total soluble Fe/As ICP-OES. The text does not define a culture-liquid separation filter here; the 0.45 micrometer filter is explicitly described for TCLP and must not be transferred to the culture assays. Initial pH is not a continuously controlled set point. Selected Table 3 rows at 3.3 mM As(III), 4.5 mM Fe(II), pH 1.5 and 24 days report 11% removal with amorphous material without seeds versus 95% removal with scorodite assignment and bioscorodite seeds. This is disappearance of initial dissolved arsenic, not product mass, mineral-specific yield or newly formed scorodite fraction. Original final XRD patterns are not shown separately for every Table 3 arm. The 13 mM As(III)/18 mM Fe(II), 99%, 14-day Table 3 row is attributed to Okibe et al. 2014; it is not silently promoted to a new 2018 observation.

Critical limitations and counterevidence are retained:

- The chemical seed preparation uses different arsenic valence, concentrations, medium and duration. It is not a matched abiotic culture control; a complete uninoculated/killed-cell series is not reported. Association with the living culture is supported, but an exclusive biological pathway or microbial necessity for every reaction is not isolated.
- Pre-existing scorodite carries arsenic into seeded cultures. Figure 4 cross-sectional images of coating/infill do not close a seed-corrected mineral mass balance.
- Table 3 identifies jarosite at high iron/arsenic ratios, with substantial arsenic removal, and amorphous material under other conditions. Dissolved arsenic removal alone is not phase proof.
- At initial pH 1.5 the time series shows an amorphous-to-crystalline sequence; at pH 1.2 precipitation follows a different course, with slower/lower removal. Thus a universal obligatory two-stage pathway is not adopted.
- Figure 1b infers 1.55 versus 1.91 waters per formula unit in bio versus chemical material, rather than exact ideal hydration. FTIR and thermal data indicate associated organics. Some final bulk Fe/As ratios exceed one. Ideal species identity does not establish bulk purity; sulfate incorporation is proposed rather than proven by those ratios.
- Section 2.4 TCLP uses acetate pH 4.9, 5% w/v solids, 25 degrees C, 30 rpm and 18 hours, in duplicate. Table 2's final biogenic-seeded pH 1.5 product is 0.59 +/- 0.20 mg/L arsenic; narrative/conclusion gives +/- 0.08 for the same endpoint. This unresolved source contradiction is explicit in the record. No error-statistic definition is invented. TCLP liquid is not reactor effluent, and this short test is not a claim of permanent safety or environmental stability.
- IAP/speciation calculations and inferred sulfate incorporation are not direct molecular observations. Appendix A2 is a literature comparison, not independent new experiments. The proposed continuous reactor is prospective; no industrial deployment is inferred.

The original article explicitly uses CC BY 4.0. The institutional copy preserves the published license. The IMA document states CC BY-SA 3.0; Handbook is copyright Mineral Data Publishing, all rights reserved. Retained originals and images remain outside Git; the repository receives citations, analysis and hashes. Rights for the deferred J-STAGE article have not been established and no redistribution is proposed. This is a literature-curation source, not a reusable bulk dataset with a published row schema, API release cadence or comprehensive machine-readable assay table. Extracted text is not substituted for original graphics.

## Identity and deferred-source boundaries

IMA page 195 lists Scorodite as Fe3+(AsO4)(H2O)2, status G, original-description year 1818. The year is not an IMA approval accession. Handbook distinguishes its dimorph parascorodite. Biological products assigned by XRD need not be perfectly pure or ideally hydrated to support the bounded phase-presence statement. No elemental criticality claim transfers to the mineral.

The deferred 2020 article is by Okibe, Nishi, Era and Sugiyama, not Tanaka. The retained raw basename `tanaka2020-jstage` is an early acquisition alias, not bibliographic attribution. Fresh Crossref confirms the authors and separates December 2019 online publication from the 2020 issue. All nine pages are available and rendered, but original graphics/results were not fully assessed in this bounded round. Its heterogeneous seeds, negative phase outcomes and lower-temperature organisms are future questions, not accepted evidence here.

Cummings et al. 1999 is a useful reductive-mobilization counterevidence lead. The exact DOI is `10.1021/es980541c`. An abstract is insufficient to curate its organism/phase/mechanism details. Its existence reinforces the need to avoid universal stability claims, but no full-study result from it is represented as checked in this record.

## Priorities and handoff

1. The scorodite owner has been created only after the coordinator's baseline `just check` passed. Named nonempty validation completed successfully; the companion manifest pins the command receipt, accepted record and CREATE sidecar. This is curator validation, not independent scientific acceptance. A separate reviewer will inspect the frozen bytes and sources.
2. Assess the complete 2020 J-STAGE follow-up's original figures/tables and controls before adding any heterogeneous-seed or alternate-organism claim. Acquisition is already available; scientific assessment remains incomplete.
3. Acquire and inspect the 1999 reductive-mobilization primary study and later dissolution work before representing conditions that reverse immobilization. Acquire the 2010 crystallization original and supplement before curating its different organism.

## Limits and unresolved questions

Unresolved questions include the inconsistent TCLP uncertainty, the exact contribution of living cells versus chemical oxidation/precipitation, seed-corrected mineral mass balance, product purity/hydration and longer-term release under changing geochemistry. No claim is made that source searches are exhaustive. Publisher landing access was blocked, but the original institutional full text was accessible. Candidate authorship and source filenames are explicitly separated. No formal self-review or Git/GitHub publication was performed by this investigator. Named record validation does not replace the coordinator's full gates or independent review.
