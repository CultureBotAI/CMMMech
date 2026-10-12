# Round49 titanium minerals: completed curation handoff

UTC: 2026-10-12T06:50:18Z

Author: Codex /root/round27_packaging; GPT-6; codex. This is source investigation and curation, not independent scientific approval.

Working revision: b701555aa8b06a51f94a4d97bed7f3ebf96ab439 in `/private/tmp/CMMMech-expansion-round49-20261012`. Baseline is the exact-base fresh-main result explicitly reused by `/private/tmp/cmm-round49-initialization.json`, not a newly executed baseline. Named validation of the two new records passed (2 checked, 0 failed). Parent cohort gates and independent reviews remain separate.

## Decision and material boundaries

- [Anatase](../../../data/records/anatase.yaml): IMA species identity and an engineered bacterial-template/synthetic-reagent experiment, followed by abiotic thermal crystallization. No natural Ti feed, biological Ti redox claim, extraction yield or natural anatase biogenesis is inferred.
- [Brookite](../../../data/records/brookite.yaml): current IMA identity and complete primary characterization of a natural Magnet Cove specimen. No microbial mechanism is supplied merely because a mineral record can contain one.
- Existing rutile, titanium and titanium-metal owners are distinct. No new concentrate owner or existing-record edit is justified from the unavailable 2015 desilication main article.

## Search scope and experiment deduplication

`dedup-receipt.json` searches current and original checkout `data/records`, `research`, `reviews`, and `history`, including hidden/ignored files and relevant symlinks. Cycle-aware discovery read 3786 textual metadata files and found 177 existing referenced raw/research/evidence roots. Missing historical roots are enumerated, not silently searched. Text-bearing YAML/JSON/Markdown/text/HTML/XML/CSV/TSV files were searched; this is not a claim to decode every binary archive, PDF or image or search unrelated machine directories.

Material/title/lead patterns returned prior titanium/rutile context and authority mentions, without an existing anatase or brookite record owner. A second exact DOI/experiment search used `C6SC02311H|8b00213|10\.2110/jsr\.2016\.1|INP.5R5|8115.*brookite` over those same roots. It returned zero matches (rg exit1, no errors), including ignored files. Full commands, root lists, matches and errors remain in the outside-Git receipts. The newly acquired raw directory was excluded from the pre-curation novelty search to avoid treating the investigator's own downloads as earlier curation.

## Acquired primary sources and provenance

1. Ping H, Xie H, Xiang M et al. (2016), *Confined-space synthesis of nanostructured anatase, directed by genetically engineered living organisms for lithium-ion batteries*, Chemical Science7:6330–6336, [DOI10.1039/C6SC02311H](https://doi.org/10.1039/C6SC02311H). Complete deposited publisher article is seven pages; original ESI is fourteen pages. Europe PMC complete JATS and PMC HTML were acquired first. Direct RSC PDF returned403; PMC bin returned an HTML download shell despite a `.pdf` filename. Those responses were not treated as readable PDFs. The changed legitimate official PMC Open Data route yielded actual PDF and ESI objects with MD5 values matching the version1 metadata. The source metadata identifies PMCID5450446, PMID28567245, DOI and `is_retracted:false`; this is a repository metadata observation, not a claim of an independent Crossmark query.
2. Liu W, Chen J, Zhang X et al. (2019), *Pressure-Induced Phase Transitions of Natural Brookite*, ACS Earth and Space Chemistry3(5):844–853, [DOI10.1021/acsearthspacechem.8b00213](https://doi.org/10.1021/acsearthspacechem.8b00213). Complete ten-page published PDF was obtained from coauthor Dongzhou Zhang's public publication host. ACS landing/direct PDF access was restricted; an eScholarship manuscript link also returned403 locally. The actual author-hosted published PDF is the inspected main. Original nine-page SI was acquired from the ACS Figshare deposit, article7999103/file14894039; resource DOI matches the main and downloaded MD5 matches its deposit metadata. Canonical [SI download](https://ndownloader.figshare.com/files/14894039), not the transient signed delivery URL, is retained as the source locator.
3. Current official [IMA September2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf): definitions and terms pages1–2, Anatase page10, Brookite page31 personally inspected. Anatase row is TiO2, A, `1962 s.p.`; Brookite is TiO2, G,1825. Neither year string is invented into a numbered IMA identifier.
4. Official [NCBI562](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=562) returned Escherichia coli with rank species. This verifies the asserted species identifier only; BL21(DE3) and recombinant constructs are source-reported identities without independent stock authentication.

Exact main and SI SHA256:

| Artifact | SHA256 |
| --- | --- |
| Anatase original main | e022ad627cb847c673dae3c31a86b2cd82a812c01ed8b57c444453e779c4c3e0 |
| Anatase original ESI | 133e3d5066b86ccf51c9aac6cb9ff076dee0f3b851e1f5bf080d6d0722e8da20 |
| Brookite original main | 35952fc0406efdf9a512b0ba21c3e7b0e571e9d4d1186e3d25e37d9b59b97027 |
| Brookite original SI | 886517ebd9788f6a3d1561acc460b283835eb1bc816cf37782c0959fe010f906 |
| Current IMA list | 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973 |

## Anatase: inspected assays, controls and limitations

All seven original main pages and Figures1–7 were personally viewed, plus all fourteen original SI pages, FiguresS1–S13 and TablesS1–S2. Complete text was read alongside the images. Main Figures1–5 and SI methods/S1–S9 support the adopted synthesis claims; battery Figures6–7/S10–S13 and tables are inspected contextual evidence, not extraction endpoints.

The source specifies E. coli BL21(DE3), engineered INP-nR5 surface-display constructs (n=1,3,5), a synthetic TiBALDH reagent and cell-pellet synthesis. Membrane isolation/French-press steps belong to protein characterization, not a substituted cell-free synthesis protocol. SIpage2 supplies10mL buffer (50mM Tris-HCl,pH7.0;300mM NaCl),2mL precursor solution,37°C24h then80°C24h, washing/freeze-drying, and600°C4h in air orAr. Precursor stock molarity, pellet biomass loading, viability trajectory, reaction pH trajectory and isolated Ti mass balance are not supplied. The initial growth OD is not a synthesis biomass dose.

The37°C product is largely amorphous by Figure1b/S2g. A weak broad~26°feature in S2h after80°C is interpreted by the authors as anatase nuclei, without the stronger phase characterization of the final calcined material. MainFigure2 and S5/S6 show the crystalline anatase-assigned product after heating. MainFigure2/prose uses powder card21-1271 whereas S6 prints21-1272; no card ID is asserted independently. Approximate5nm in prose and5.8±0.8nm in Figure3 are retained as distinct source descriptions; sample-size/uncertainty basis is unspecified.

INP-only cells remain smoother in S2 but produce aggregated particles after calcination in S4b. This supports a morphology comparison, not the claim that R5 or metabolic activity is necessary for all Ti solid formation. A separate matched cell-free precursor or live/dead comparison is not reported in the complete inspected main/ESI. One/three/five-repeat arms are within the same study, not independent replications. The molecular scheme in1d/3d/5 is proposed explanation, not direct causal measurement of every catalytic intermediate. Carbon-coated Ar product is a composite. Figure4f~13wt%TG estimate and S9's15.8wt%geometric model are distinct, not equivalent yield measurements. SI TableS1 prints1C=168mAh/g whereas experimental methods say167mA/g; battery performance is outside the accepted mechanism's endpoints. No numeric Ti recovery or commercial deployment is inferred.

## Brookite: inspected natural-specimen evidence

All ten original main pages, Figures1–7/Table1, and nine SI pages, FiguresS1–S4/TablesS1–S4 were personally inspected. Starting specimen8115 is natural Magnet Cove material from the Berkeley collection. Acid cleaning with1mol/L HNO3, washing/drying/grinding precede ambient XRD. Figure1 and Pbca indexing establish source-assigned brookite; two EDS spots on a particle yield Table1's O38.64/Ti59.23/Nb2.13wt%, not bulk ore grade or proven purity. SI S2 compares before/after~8MPa pressing, with no apparent preparation-induced phase change.

Subsequent diamond-anvil compression up to~60GPa and decompression in He,Ne,or4:1methanol/ethanol are abiotic materials experiments. Figure5 phase fractions and SI TableS2 are fitted phase mixtures, not extraction yields; the paper explicitly calls them kinetic/non-equilibrium. High-pressure 'baddeleyite' denotes a TiO2 structure, not ZrO2 mineral production. Raman/XRD onset and disappearance estimates vary with method/medium; they are not generalized into exact geological boundaries. Figure7/DFT and SI enthalpy/shear-modulus calculations remain model-based. Text extraction appends reference superscripts to ICSD numbers (e.g.15409 plus reference32); those concatenations are not imported as identifiers. The conclusion/abstract compress phase ranges relative to detailed paths, so no universal transition threshold is adopted. No microbial organism, control or recovery assay exists in this source.

## Notices, counterevidence and deferred leads

Bounded live searches on2026-10-12 combined each selected DOI/title with correction/retraction/erratum and a separate anatase criticism query. Results returned primary publisher records and later citations, without a relevant correction/retraction notice in the inspected results. This is search coverage, not proof no notice can exist. Crossref brookite metadata was acquired; anatase Crossref returned429, so no successful Crossref verification is claimed for that request. Actual primary controls and amorphous/thermal-phase distinctions provide the main counterevidence to overstated biological claims.

The GFZ accepted manuscript by Schulz,Wirth,Schreiber(2016), DOI10.2110/jsr.2016.1, was legitimately acquired as42pages and rendered. Only opening text was inspected, not its complete original graphics; it is a future natural-geological extension, not accepted evidence here. The2015 rutile-concentrate desilication DOI10.1016/S1003-6326(15)63855-9 remains metadata/abstract-level after bounded new search; no unavailable methods, figures, denominators or measured recovery are asserted. Previously blocked ilmenite issue104 routes were not retried unchanged, and that issue's acceptance criteria are not met by these new TiO2 records.

## Artifacts and review readiness

The paired JSON contains all 119 raw file paths/SHA256 values, acquisition receipts and explicit inspection scope. Full article/graphics/bulk raw data remain outside Git; published ACS main is copyrighted, Ping main/ESI carriesCCBY-NC3.0, ACS SI deposit reportsCCBY-NC4.0 and IMA reportsCCBY-SA3.0. Retention does not imply general redistribution permission. Failed HTML-shell downloads are labeled non-evidence.

Canonical CREATE sidecars and distinct actual inline events are attached. Record/history hashes below are the frozen author handoff, pending independent review, not an author-issued acceptance verdict.

- `anatase` record SHA256 `1b75b2c9a7bc922bd7503a2a3415478e77498df6db23c6385e8a612a547db60e`; `history/records/anatase/2026-10-12T064814Z-codex-810f65.yaml` SHA256 `0235c06c755d2e23ed39210e179588216fc0585127be6af493cb6cacfaad6800`.

- `brookite` record SHA256 `39978526ff9e4fe8233cbcbb6c2dc2e8d73b994054cac0b4d109cabc6bf6fd98`; `history/records/brookite/2026-10-12T064821Z-codex-147a2e.yaml` SHA256 `52bf491f3c4170c62cae27609e036917374a9dda685c36caed4d59b829fea119`.

No schema, validator, existing record, shared README, website, Git or GitHub mutation was made by this curation task.
