# Coquimbite and rozenite source investigation

Prepared 2026-10-15T15:13:07Z by codex (GPT-6; codex), curator of the two proposed records. This source assessment is separate from the independent scientific reviews. Worktree `/private/tmp/CMMMech-expansion-round97-20261015`, trusted base `9272005a590c9fa1e5fbb75b30f914ce38c3924a`. Actual creation/validation metadata and final owner hashes are in the paired JSON.

## Selection and boundaries

Coquimbite closes the explicit round96 deferred current-identity gap: the 2019 IMA redefinition makes Al essential and distinguishes it from paracoquimbite and aluminocoquimbite. The full 2020 original and deposited CIF support an identity-focused record. No mechanism field is manufactured from a static crystal structure.

Rozenite adds a separate ferrous sulfate tetrahydrate species, with directly observed abiotic transient-phase behavior in the complete 2021 melanterite heating study. Natural specimen origin is not biological causality. No criticality, taxon, external material CURIE, recovery yield, quantitative concentration observation or industrial deployment is inferred for either mineral.

## Deduplication and searches

A hidden- and ignored-inclusive `rg --no-ignore --hidden -L` search covered maintained `data/records`, `research`, `reviews` and `history`, following relevant symlinks, for coquimbite, rozenite, szomolnokite and both normalized DOIs. `dedup-maintained.txt` retains results. Coquimbite occurs as a round96 deferred lead and in titles of ferricopiapite/rhomboclase references; neither selected mineral had a maintained owner at selection. Directly relevant prior downloads in `/private/tmp/cmm-round96-sulfates-research` and `/private/tmp/cmm-round95-sulfates-research` were also searched, including ignored/hidden text, JSON and Markdown; `dedup-prior-downloads.txt` retains results. This is bounded cited-download coverage, not machine-wide absence. Broad downloaded mineral lists mention many species without constituting accepted records. The 2020 original and supplement are the same experiment; mirrors are not separate evidence.

`gh issue list --repo CultureBotAI/CMMMech --state all --limit 1000 --json number,title,body,state,url` retrieved 244 issues on 2026-10-15. No selected-name or normalized-DOI match occurred in title/body. The response is retained as `issues-all-state.json`; the 1000-item limit is explicit.

Live web searches used the following exact queries on 2026-10-15, without date/domain filters or exhaustive pagination. Query results were inspected in the tool; original responses were not saved verbatim. Resulting accepted URLs, failed routes and decisions are retained below and in acquisition receipts:

- `rozenite szomolnokite crystal structure thermal dehydration full text mineral`
- `coquimbite redefinition 2019 2020 Al Fe sulfate crystal structure`
- `"Redefinition of coquimbite" pdf Mauro 2020`
- `"10.1180/mgm.2020.15" correction erratum retraction`
- `"10.3390/min11040392" correction erratum retraction`
- `"Rozenite" "microbial" mineral experiment`
- `"Redefinition of coquimbite" "arpi"`
- `"Thermodynamic Properties of Coquimbite and Aluminocoquimbite"`
- `"Mauro" "coquimbite" "11568"`
- `"Redefinition of coquimbite" repository pdf`
- `"MM84_275.pdf"`

The last filename query found the official new RRUFF endpoint `/odr/view/downloadfile/83969`, avoiding the unusable legacy host. No affecting correction/retraction was found in the bounded DOI notice searches. Crossref metadata was separately requested; both returned the expected titles, no update-to field and empty relation objects; retrieval outcomes are retained in acquisition-05 and the two DOI JSON files. This does not establish exhaustive correction coverage. The original articles themselves contain scientific limitations retained below.

## Coquimbite: accepted evidence

[Mauro et al. 2020](https://doi.org/10.1180/mgm.2020.15), Mineralogical Magazine 84:275–282, is an eight-page complete original. All text, Tables 1–7, Figures 1–5 and references were inspected; figures/tables were also rendered and visually checked. The publisher directly links a 624,290-byte CIF, `S0026461X20000158sup001.cif`, also inspected for identity, analytical/structural formula, space group, temperature, lattice, mixed-site occupancy, H-site treatment and refinement metadata. It contains refinement/structure-factor data, not independent specimen replication. No raw-intensity re-refinement was performed.

- Printed page 277/PDF page 3 identifies the natural Monte Arsiccio specimen and powder-XRD confirmation. Figure 2 distinguishes coquimbite from associated krausite rather than treating the whole intergrowth as chemically homogeneous.
- Printed page 278/PDF page 4 gives 20 WDS spot analyses at 15 kV, 10 nA, 10 micrometre beam diameter; SO3 = 42.88(45), Al2O3 = 4.38(7), Fe2O3 = 22.28(38) wt%; H2O 29.10 wt% was calculated from 18 structural water groups, not directly measured. Empirical Al0.96Fe3.11S5.97O24·18H2O is distinct from the ideal species formula and from the structural occupancy model. No loss-on-ignition or recovery denominator is inferred.
- Table 3, printed page 279/PDF page 5 and CIF agree on mixed-site Al0.946(7)Fe0.054(7). CIF gives trigonal P -3 1 c, 293(2) K, Z = 2, and formula sum Al0.95Fe3.05H36O42S6. Table 2 prints (Al0.94Fe0.06)Fe3; that rounded presentation differs slightly from the CIF formula sum and exact Table 3 occupancies. The record uses exact Table 3 occupancies and preserves sample/ideal distinction.
- Printed pages 279–280/PDF pages 5–6 describe difference-Fourier H-position refinement with soft O–H restraints. Table 2 labels the 1307 selected reflections Fo>4σ(Fo); CIF `_reflns_threshold_expression` says I>2σ(I). That reporting discrepancy remains unresolved; no threshold equivalence or independent fit replication is asserted. Table 5/CIF H-bond uncertainties also use different displayed precision in places; those measurements are not imported.
- Table 7/Figure 5/Discussion, printed pages 280–281/PDF pages 6–7 establish distinct mineral and group scopes. Coquimbite has finite Fe-sulfate clusters and isolated Al-water octahedra; paracoquimbite is related but compositionally distinct, while aluminocoquimbite has a different topology. Proposed Al stabilization of the structure is not treated as a measured synthetic mechanism.
- The article's Table 1 is explicitly based on the pre-redefinition 2019 IMA list and still prints the Al-free formula. The older 2001–2005 Handbook likewise retains that obsolete formula. These are historical evidence, not the current accepted definition.

The current [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF page 49, gives AlFe3+3(SO4)6(H2O)12·6H2O, Rd, 2019 s.p. Definitions on PDF page 1 explain special-procedure redefinition years rather than new mineral numbers. [CNMNC Newsletter 52](https://doi.org/10.5194/ejm-32-1-2020), section 3, records approval of 19-F in October 2019; the 2020 publication date is not the approval date. The notice and original distinguish Smithsonian neotype 12548 from the newly analyzed Pisa specimen 19914. These museum numbers are not used as material-wide CURIEs.

## Rozenite: accepted evidence

[Lacalamita et al. 2021](https://doi.org/10.3390/min11040392), Minerals 11(4):392, is a complete 15-page original. All text, Table 1, Figures 1–9 and references were inspected; relevant original graphical pages were rendered. The original announces no separate supplement. The MDPI landing page gave 403/429 on attempted routes, so this pass cannot claim a complete live supplement inventory or any unavailable raw-pattern access.

- Methods, PDF page 3: natural Fornovolasco melanterite ground in agate mortar on corundum holder; air-XRPD at 25–775 degrees C, at 25-degree intervals with 5 min equilibration, 10–82 degrees 2theta, 0.0263-degree step and reported 257 s/step. The latter is transcribed as stated, not reinterpreted as a total acquisition duration. Discussion, PDF page 9 refers to about 50% RH for RT–50 degrees C; it does not document a full controlled RH history for the heating run.
- Section 3.2/PDF pages 5–6/Figures 2–3: Rietveld baseline of 78 wt% melanterite and 22 wt% rozenite. Rozenite's initial presence is hypothesized to result from grinding based on its reported absence at the mine; no separate grinding-control experiment demonstrates that cause.
- Figure 7/PDF page 9 and discussion, PDF pages 9–10: rozenite increases during RT–50°C heating, persists in the 75-degree C pattern and is absent in the 100-degree C pattern while poorly crystalline szomolnokite appears. Refined phase amounts are not isolated-product yields. The plotted intermediates and inferred bonding rearrangements do not establish each microscopic atomic step. No independent run count or replicate-variance estimate is supplied.
- TG/DTA is a separate experiment on approximately 13 mg under N2 at 10 degrees C/min; air-XRPD temperatures must not be merged with DTA events. Discussion PDF page 12 explicitly compares complete melanterite-to-rozenite dehydration near 50 degrees C by XRPD with an approximately 70-degree DTA event. Temperature/path differences depend on the measurement protocol and sample; no universal stability limit is accepted.
- Infrared methods, PDF page 3 compare KBr pellet, pressed powder and tiny crystal arrangements. Detector saturation for some pure-sample regions and possible pellet artifacts are explicitly discussed PDF pages 3/12. These corroborating spectra do not yield a microbial activity measurement.
- Source-language inconsistencies extend beyond the accepted rozenite endpoint: section 3.2 first says additional szomolnokite/FeOHSO4 phases from 100 degrees C, whereas discussion/PDF page 10 identifies a szomolnokite peak already at 75 degrees C. The record retains only the common rozenite observations and does not force one onset for the other phases. The Figure 9b caption points to Figure 4, which is an FTIR figure; the actual structural comparison is FeOHSO4. This caption cross-reference is not used as evidence for a different phase.

The [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF page 188, gives Fe2+(SO4)(H2O)4, Rd, 1963 s.p. The complete one-page [Rozenite Handbook](https://handbookofmineralogy.org/pdfs/rozenite.pdf) supports monoclinic identity while distinguishing synthetic cell/density measurements from natural occurrences. No material CURIE is invented from crystallography database numbers.

## Access, provenance and reuse

All bulk originals, HTML, CIF, text extraction and rendered pages remain outside Git in `/private/tmp/cmm-round97-sulfates-research`. Acquisition 01–05 receipts record exact URLs, actual request times, redirects/media types, failures, byte counts and SHA256. Successful HTTP 200 was inspected for actual content: the Cambridge PDF route returned 960450 bytes of HTML, retained with its attempted filename and explicitly not used as a PDF. Legacy RRUFF refused connections, Arizona archive timed out and GSW returned 403 before the independently discovered new RRUFF endpoint succeeded. No certificate bypass, credential circumvention or arbitrary access restriction bypass was attempted.

Accepted primary hashes: coquimbite original `fc34e62d3a8c1cc6051e92acf206ed96ca28d3f0a8b8e286eafaa79ae6f1d2b6`; CIF `9bd5ef8b8243a33d585d565c341bb1621ea53793875aa4a62f9cf3f79fc0db88`; thermal original `8ce0f570ecdcbc11b3854a4ba1bbdbfef1b534a5a34ba6336e785881d5e52c14`; IMA `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`.

The 2021 original is CC BY 4.0; IMA is CC BY-SA 3.0. The 2020 article is copyrighted by the Mineralogical Society of Great Britain and Ireland; redistribution permission for that original/CIF was not established. Handbooks reserve rights. Access to a public copy is not a bulk redistribution license. Only the curator's summaries/provenance are committed.

## Remaining frontier and handoff

Szomolnokite is a genuine next candidate with primary thermal evidence already acquired, but is outside this two-record slice. Its natural-species identity and latest authority references still require their own assessment. The new 2023 coquimbite/aluminocoquimbite thermochemistry lead (English DOI 10.1134/S0016702923050051; Russian DOI 10.31857/S0016752523050059) is one translated study, not two independent experiments; this pass inspected metadata/search excerpts only and imports no calorimetry claims. Obtain and inspect the original before considering an extension. Current IMA's recent-reference column also points to American Mineralogist 110 (2025):1815 for coquimbite and 108 (2023):1080 for rozenite; these have not been reviewed in this bounded pass.

Microbial searches found field-associated salts/biosignature studies, including the Brick Flat gossan study, rather than a verified controlled rozenite-specific mechanism. That lead remains research, not proof that no microbial mechanism exists. No source or species exhaustion is claimed. Root coordinates independent reviews of exact final bytes and full-batch gates. Only these two owners, their CREATE histories and this paired source dossier are authored by this agent.

## Local curation checks

The coordinator baseline `just check` passed before owner creation at 2026-10-15T15:09:40Z. Both final records and CREATE sidecars were authored after that result. The two-record validation completed with exit 0 (`Checked 2 record(s); 0 failed.`). Its external log, exact owner and history hashes are in the paired JSON. These file checks do not replace the coordinator’s full-corpus, append-only history and independent scientific-review gates.
