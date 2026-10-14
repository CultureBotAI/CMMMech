# Manganese source investigation and ramsdellite handoff

UTC: 2026-10-14T07:26:50.416256+00:00. Researcher: Codex (GPT-6; codex), `/root/round65_manganese`.
Base: `4aed29a1ed91171b9491bc3be2f6f003b2a4289a`.
Worktree: `/private/tmp/CMMMech-expansion-round65-20261014`. This source assessment is separate from independent scientific review.

## Selection and identity

Ramsdellite adds a distinct MnO2 species with a documented abiotic cobalt-sorption experiment alongside the corpus's microbial birnessite evidence. [IMA September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), page 182, lists the species as grandfathered, original-description year 1943. Pages 1-2 define that status and the CC BY-SA 3.0 terms. The year is not an approval accession. The [Handbook entry](https://www.handbookofmineralogy.org/pdfs/ramsdellite.pdf) confirms orthorhombic identity and distinction from pyrolusite. No mineral CURIE or inherited commodity criticality is invented.

The original [Sasaki et al.2008 paper](https://doi.org/10.2320/matertrans.M-MRA2007888) assigns the chemically synthesized comparator to ramsdellite by four XRD peaks. Its fungal product is poorly crystalline birnessite, already owned by `data/records/birnessite.yaml`. These are distinct materials from one experiment, not independent replications. The new ramsdellite mechanism explicitly uses `microbial: false`; it does not assert biogenic ramsdellite.

Hidden/ignored-inclusive searches followed relevant symlinks within `data/records`, `research`, `reviews`, `history` and the three retained raw roots named in the JSON. They found the existing comparator references and no pre-existing ramsdellite owner; no machine-wide absence claim is made. Binary PDFs were decoded only where named. The new 2025 DOI/PMC was absent from the scoped maintained metadata at the initial check.

## Accepted evidence and limitations

The complete seven-page Sasaki 2008 original was read and all eleven figures visually inspected. A fresh official PDF matches the retained original SHA-256 `28c4babe0dc984ac07f6660069f0a43f95fc7490ab6b4c560bdbac3db54ebbac`. The current publisher page reports zero supplementary files. Crossref confirms publication identity and has no update-to entry; bounded correction/retraction searches returned no identifiable notice, not proof that none exists.

The comparator was made by chemical oxidation of MnSO4 with ammonium peroxodisulfate, followed by filtration and freeze-drying. The solid had 54.1 wt% Mn and BET area 11.3 m2/g; XRD assignment is not quantitative phase purity. The experiment used 0.015 g in 0.150 L synthetic cobalt-nitrate solution, nominal 1 mM solid Mn, 100 mM KNO3/PIPES, initial pH 6.5, 25°C and 100 rpm. It was described as duplicate. The record distinguishes 0.2 µm-filtered elemental analysis from valence measurement and surface spectra from bulk composition.

Figure 7b supports cobalt depletion toward approximately 0.15 mM, not an isolated recovery yield. Figure 8b includes with-Co and no-Co comparisons and little additional Mn release. The surface Co 2p/Mn 2s overlap and exchangeable Co fraction prevent a complete-valence-conversion or unique lattice-site claim. A no-sorbent blank time series is not displayed. The fungal-tissue control is a separate biomass control.

The paper's numerical recipes and capacity comparisons need caution: method feed ceiling 175 µM conflicts with the approximately 0.21 mM initial graph and separate 0.55 mM statement. The printed 28.7 mmol Co/mol solid Mn and 5.6-fold comparison are not reconciled with the graph and nominal loading. Preparation concentrations 18.2 mol/L and the 500 dm3 flask wording are not silently corrected. The record does not adopt these as validated protocols/performance. These bounded source problems do not negate the narrower qualitative solution-depletion observation.

Fungal birnessite and synthetic ramsdellite differ in phase, surface area, pore structure, retained organics and Mn composition. Their comparison cannot isolate biological origin. No microbial ramsdellite, actual-waste treatment, industrial deployment or purified product is claimed. No quantitative concentration observations were added because the contract is for source-table mg/kg cells, not these solution/ratio measurements.

## Acquisitions that expand the next frontier

1. [Boothe-Lordon et al. 2025](https://doi.org/10.1021/acsomega.5c04278), PMC12461413: complete EuropePMC XML acquired; Methods and relevant phase passages screened. It describes an abiotic H+birnessite-to-ramsdellite endpoint and fungal poorly crystalline phases. Main-PDF route returned challenge HTML, publisher PDF403; EuropePMC supplement requests timed out twice. Both DOI-linked publisher Figshare PDF and XLSX supplements were subsequently acquired successfully; checksums and stable download routes are in the JSON. Full figure/data/control assessment remains pending, so no experiment values are imported. Current IMA p228 labels vernadite **Q (questionable)**, year 1944; this prevents treating its name as unqualified approved-species evidence. A future record must retain that identity uncertainty and distinguish δ-MnO2 experimental analogues.
2. [Fredrickson et al. 2002](https://doi.org/10.1016/S0016-7037(02)00928-6): retained 16-page original screened in selected methods/identity/implications sections. It studies existing-owner pyrolusite, K-birnessite, bixbyite with hausmannite impurity, uraninite and rhodochrosite; no ramsdellite experiment was identified in that scope. Full graphical/control and U/Mn-fraction assessment is the next step; no new species is fabricated from a different experiment.
3. [Pracejus 1989 thesis](https://digital.library.adelaide.edu.au/server/api/core/bitstreams/1863f55b-77d9-42b3-a31a-b052d263fc4f/content): complete 351-page University of Adelaide original acquired. Title/contents and section 5.5 (pp125 onward; PDF150 onward) screened. Appendix I.3.2 contains experimental methods; Appendix V.2 has leaching data. Mixed-ore normative mineral proportions and correlations must not become pure cryptomelane/romanechite causal yields. This is acquired but not fully assessed evidence.
4. [Min et al. 2022](https://doi.org/10.1021/acs.est.2c00342): full original remains inaccessible in this pass. DOI-filtered official Figshare metadata resolved the real eleven-page [SI](https://doi.org/10.1021/acs.est.2c00342.s001), acquired successfully; its cover declares two tables/six figures. Full original plus SI must be reviewed together under existing bixbyite-mn ownership. Publisher snippets and a SI alone do not establish a curation-ready mechanism.

## Provenance and delivery

Raw artifacts remain outside Git at `/private/tmp/cmm-round65-manganese-research`. JSON logs exact queries, first-result-set coverage, failures, stable acquisition URLs, UTC times, hashes and named retained rechecks. Signed download query strings are omitted from committed provenance. Initial restricted-network attempts failed before retrieval; successful official acquisitions followed. Originals are not redistributed. Sasaki 2008 and Handbook PDFs state copyright; IMA has CC BY-SA 3.0 terms; Boothe 2025 XML declares CC BY 4.0. Other source terms need artifact-specific assessment before redistribution.

Curated: `data/records/ramsdellite.yaml`, SHA-256 `8ae85741406c1dff3a460f8da2bb9c6a6135cf90760727345be491384477d570`.
Canonical history: `history/records/ramsdellite/2026-10-14T072208Z-codex-3bc22b.yaml`, SHA-256 `195b72ed8ff8cd3c9a76e4f400eee59ed0b80ba2c6230d6ccbf97d0d22360485`.
Single-record validation passed (one checked, zero failed). Baseline `just check` passed before record creation. Independent review and batch gates follow; no schema/validator change was needed. The named acquired sources show that the broader frontier is not exhausted.
