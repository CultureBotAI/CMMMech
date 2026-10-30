# Round 123 source investigation and Cycle 5 Stage 1 (`add_records`) bounded-frontier dossier

- **Investigation ID**: `round123-minerals-20261030T133900Z`
- **Timestamp (UTC)**: `2026-10-30T13:39:00Z`
- **Cycle / Stage / Round**: Cycle `5`, Stage `1` (`add_records`), Round `123`
- **Trusted Base Commit**: `3684ac763165c2343e93af37c9eef7b21608edd5` (`origin/main`)
- **Logical Goal Identity**: `conversation_id: 5d564102-201c-473a-960a-1d0caa99b350`, `start_step_index: 2956`, `started_at: 2026-10-30T12:41:17.226025+00:00`

## 1. Scope and search limits

In Cycle 5 Stage 1 (`add_records`), Round 123 conducted primary-source discovery and curation for IMA-accepted critical-element mineral species not yet represented in `data/records/`:

- **RRUFF Archive Search Limit**: Direct probes to `https://www.rruff.net/doclib/` and `https://rruff.net/rruff_1.0/` returned `HTTP 502 Bad Gateway` and TCP/TLS connection timeouts on port `443`, blocking retrieval of RRUFF-hosted *American Mineralogist* and *Canadian Mineralogist* PDFs.
- **Pivot to Copernicus EJM and J-STAGE JMPS Gold Open Access Primary PDFs**: Discovery pivoted to open-access mineralogical journals cited directly in the September 2026 IMA-CNMNC Master List of Minerals (`IMA_Master_List_(2026-09).pdf`), retrieving `6` complete vector PDFs (`5` from Copernicus Gold OA *European Journal of Mineralogy* (`ejm.copernicus.org`) and `1` second-listed reference from J-STAGE Gold OA *Journal of Mineralogical and Petrological Sciences* (`jstage.jst.go.jp`)) into `/private/tmp/cmm-round123-research/`.
- **Bounded Source-Text and Single-Page Table Inspection (`cmmmech-infra-0011` / `#840`)**: Rather than reading full multi-page PDFs into chat context, all `6` PDFs (`74` pages total) were indexed via [`scripts/index_bounded_pdf_passages.py`](../../../scripts/index_bounded_pdf_passages.py) (`--max-bytes 1800`) into `189` bounded UTF-8 passage files (`<= 1,800` bytes each; `274,104` bytes total) plus `8` single-page PNG renders (`150 DPI`) for dense multi-column analytical and crystallographic tables.

## 2. Primary source PDF inventory

| Source ID | Local Path | Bytes | Pages | Bounded Passages (`<= 1,800` B) | SHA-256 | Citation & DOI |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `ejm-32-57-2020` | `/private/tmp/cmm-round123-research/ejm-32-57-2020.pdf` | `2,312,040` | `10` | `27` | `7fdd1e65368286dd2e21171c7c20db2bd4845185ce1f51c8a8e823931f5c057a` | Nagashima et al. (2020), *Eur. J. Mineral.* 32:57–66 (`https://doi.org/10.5194/ejm-32-57-2020`) |
| `jmps-119-240509-2024` | `/private/tmp/cmm-round123-research/jmps-119-240509-2024.pdf` | `4,063,093` | `12` | `33` | `55ed32bf7d0159b232e065b606809b22eece239040cf5b5aeb5a205316d8f84d` | Nishio-Hamane et al. (2024), *J. Mineral. Petrol. Sci.* 119:240509 (`https://doi.org/10.2465/jmps.240509`) |
| `ejm-37-63-2025` | `/private/tmp/cmm-round123-research/ejm-37-63-2025.pdf` | `3,718,088` | `12` | `30` | `1d09716db17ad06a157f5992a2b23e478a5ef03ba07abd557c56462352280900` | Vereshchagin et al. (2025), *Eur. J. Mineral.* 37:63–74 (`https://doi.org/10.5194/ejm-37-63-2025`) |
| `ejm-33-175-2021` | `/private/tmp/cmm-round123-research/ejm-33-175-2021.pdf` | `6,815,514` | `13` | `35` | `a972dd34d42f93acc53cd3c99b31923398278bf0f47141a4d9d354096429cf11` | Sejkora et al. (2021), *Eur. J. Mineral.* 33:175–187 (`https://doi.org/10.5194/ejm-33-175-2021`) |
| `ejm-34-95-2022` | `/private/tmp/cmm-round123-research/ejm-34-95-2022.pdf` | `12,975,465` | `14` | `31` | `64e9a5aca65fe7b51b164738652de4cbd4bdc9b122726e68045fff0c7053ebce` | Xue et al. (2022), *Eur. J. Mineral.* 34:95–108 (`https://doi.org/10.5194/ejm-34-95-2022`) |
| `ejm-38-373-2026` | `/private/tmp/cmm-round123-research/ejm-38-373-2026.pdf` | `3,190,914` | `13` | `33` | `d808836aadb6c476d90fd624e23cd145f7fb7933236cbb1f4bdbe523f66e5c53` | Meisser et al. (2026), *Eur. J. Mineral.* 38:373–385 (`https://doi.org/10.5194/ejm-38-373-2026`) |

## 3. Admitted Round 123 mineral records (`5`)

1. **[`aluminosugilite`](../../../data/records/aluminosugilite.yaml) (`cmmmech:aluminosugilite`, `IMA:2018-142`, status `A`, `KNa2Al2Li3Si12O30`, IMA p. 8)**:
   - Record SHA-256: `42dc4d62c45c1e829574efeb875377a4749badd63966fc3d3274c8ae1af3a787`
   - History sidecars: [`history/records/aluminosugilite/2026-10-30T132617Z-antigravity-cd5633.yaml`](../../../history/records/aluminosugilite/2026-10-30T132617Z-antigravity-cd5633.yaml) (`866659b41a953115e9b849d95769006869eeb2f46a79bfbbf466588f483b8d86`, `CREATE`) and [`history/records/aluminosugilite/2026-10-30T133717Z-antigravity-073be8.yaml`](../../../history/records/aluminosugilite/2026-10-30T133717Z-antigravity-073be8.yaml) (`938a1fcd31e9eb6d786cd3cdfff2ede6abaa585f8c5d0a854c3001a929274122`, `EDIT`).
   - Curated from both IMA-listed references: Nagashima et al. (2020, *EJM* 32:57–66, Cerchiara mine holotype `NSM-MF-16503` WDS+LIBS chemistry, `P6/mcc` SCXRD `a = 9.9830(4) Å`, `c = 13.9667(5) Å`, `V = 1205.45(7) Å3` in abstract/text vs `1205.45(1) Å3` in Table 2, `R1 = 0.0217`) and Nishio-Hamane et al. (2024, *JMPS* 119:240509, Funakozawa mine boulder/outcrop SEM-EDS, SPring-8 BL02B2 synchrotron PXRD, `P6/mcc` SCXRD `a = 9.9894(7) Å`, `c = 13.9527(9) Å`, `V = 1205.77(14)` / `1205.77(19) Å3`, `R1 = 2.67%`, and outcrop alteration to `swinefordite`).
2. **[`andreybulakhite`](../../../data/records/andreybulakhite.yaml) (`cmmmech:andreybulakhite`, `IMA:2023-037`, `ima_symbol: Adb`, status `A`, `Ni(C2O4)(H2O)2`, IMA p. 11)**:
   - Record SHA-256: `9fabecebd8a6dbbfe77b93597c5b11663efed3b0999c089771f3cb4d303eab93`
   - History sidecar: [`history/records/andreybulakhite/2026-10-30T132619Z-antigravity-58572a.yaml`](../../../history/records/andreybulakhite/2026-10-30T132619Z-antigravity-58572a.yaml) (`bf4639b2b87b12380ead3468b7280872560c34f613124303eed08d69a3ddf07a`).
   - Curated from Vereshchagin et al. (2025, *EJM* 37:63–74): Nud II deposit holotype (`MM SPbU 19795/1-1` and `19795/1-2`), orthorhombic `Cccm` disorder polytype (`a = 11.842(7) Å`, `b = 5.345(2) Å`, `c = 15.716(7) Å`, `V = 994.8(9) Å3`, `Z = 8`), natural vs synthetic `alpha-Ni(C2O4)·2H2O` (`C2/c`) and `beta-Ni(C2O4)·2H2O` (`Cccm`) comparison (Table 3), and laboratory fungal-mediated `Ni(C2O4)·2H2O` biomineralization on solid Miller's mineral medium by *Aspergillus niger* (`Ch4/07`, `NCBITaxon:5061`) and *Penicillium simplicissimum* (`19F`, `NCBITaxon:5080`) decomposing pentlandite (`(Fe,Ni)9S8`, Table 1 `#1`) and millerite (`NiS`, Table 1 `#2`).
3. **[`grimmite`](../../../data/records/grimmite.yaml) (`cmmmech:grimmite`, `IMA:2020-060`, status `A`, `NiCo2S4`, IMA p. 86)**:
   - Record SHA-256: `d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf`
   - History sidecar: [`history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml`](../../../history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml) (`fe0c1c6544457737e240ecb3bf2c29031b213a9f1c55822bbca74fb31eec627f`).
   - Curated from Sejkora et al. (2021, *EJM* 33:175–187): Příbram shaft `16` (`Háje`) holotype (`P1N 80586`), WDS composition (`Ni0.98Fe0.05Co1.94S4.03`, Table 2), reflectance (`R = 45.7–53.8%`, Table 1), cubic `Fd-3m` inverse thiospinel `Co[NiCo]S4` structure (`a = 9.3933(9) Å` natural PXRD; `a = 9.3834(1) Å` synthetic Rietveld; Tables 3–5), and `57Fe` Mössbauer spectroscopy confirming `Fe2+` substitution at tetrahedral `T(Co3+)` sites.
4. **[`liguowuite`](../../../data/records/liguowuite.yaml) (`cmmmech:liguowuite`, `IMA:2020-097`, status `A`, `WO3`, IMA p. 125)**:
   - Record SHA-256: `8c4b6b0385acd182192d596b3231137beb5acd24dd182d4f71c33697351860a5`
   - History sidecar: [`history/records/liguowuite/2026-10-30T132622Z-antigravity-c7ea8f.yaml`](../../../history/records/liguowuite/2026-10-30T132622Z-antigravity-c7ea8f.yaml) (`a8196bef70201f1dcfdeb8cffb66a33e6bd0f8a1c140708ac9f2b72510bc8932`).
   - Curated from Xue et al. (2022, *EJM* 34:95–108): Panzhihua-Xichang (`Panxi`) granite-pegmatite holotype (`M16107`) and co-type (`202001001`), WDS composition (`(W0.93Mo0.06(Fe,Al,Ca,Mg,Na,K)0.01)Sigma1.00O2.99`, Table 2), reflectance (`R1 = 15.1–19.6%`, `R2 = 16.0–20.9%`, Table 1), and monoclinic `P21/n` A-site vacant `ABX3` perovskite-type structure (`a = 7.3126(4) Å`, `b = 7.5252(4) Å`, `c = 7.6892(5) Å`, `beta = 90.388(5)°`, `V = 423.12(4) Å3`, `Z = 8`, `R1 = 0.0442`; Tables 4–7).
5. **[`yttrotungstite-nd`](../../../data/records/yttrotungstite-nd.yaml) (`cmmmech:yttrotungstite-nd`, `IMA:2023-064`, `ima_symbol: Ytgs-Nd`, status `A`, `NdW2O7(OH)(H2O)`, IMA p. 238)**:
   - Record SHA-256: `6c7e4579bf2bae64f7d38fc87dd0a28e29984fd3f78fcfc840200cce8edeac89`
   - History sidecar: [`history/records/yttrotungstite-nd/2026-10-30T132624Z-antigravity-a8e673.yaml`](../../../history/records/yttrotungstite-nd/2026-10-30T132624Z-antigravity-a8e673.yaml) (`c59d8198e4fda6d990228c95c73281f34b722e5a160bb79a9b6badf4023f1285`).
   - Curated from Meisser et al. (2026, *EJM* 38:373–385): Nyakabingo holotype (`MGL 080168`) and Gifurwe reference specimen (`MGL 093280`) in the Rwandan Tungsten Belt, WDS composition (`(Nd0.20Y0.19Ce0.17La0.13Pr0.06Sm0.06Gd0.05Dy0.05Er0.02Yb0.01Ca0.01)Sigma0.95(W1.98Fe3+0.02Al0.02Ti0.01Si0.01)Sigma2.04O7(OH)0.99·1.01H2O`, Table 2), monoclinic `P21/m` structure (`a = 5.8390(7) Å`, `b = 8.6606(8) Å`, `c = 6.9963(10) Å`, `beta = 105.252(13)°`, `V = 341.33(7) Å3`, `Z = 2`, `R1 = 0.0365`; Tables 4–7), and supergene acidic tropical weathering mechanism of ferberite (`FeWO4`) + monazite-(Nd)/bastnäsite-(Nd) with `Ce4+` cerianite fractionation (`Ce/Ce* ~ 0.45`).

## 4. Repeated bounded-frontier verification and candidate ledger

- **Local Source Directories (`/private/tmp/cmm-round117-research` through `/private/tmp/cmm-round123-research`)**:
  - `/private/tmp/cmm-round117-research` through `/private/tmp/cmm-round120-research`: `0` PDFs on disk.
  - `/private/tmp/cmm-round123-research`: `6` PDFs on disk (`ejm-32-57-2020.pdf`, `jmps-119-240509-2024.pdf`, `ejm-37-63-2025.pdf`, `ejm-33-175-2021.pdf`, `ejm-34-95-2022.pdf`, `ejm-38-373-2026.pdf`), all `6` indexed into `189` bounded passages (`<= 1,800` B) and `100%` curated into the `5` admitted Round 123 records (`0` uncurated local PDFs remaining).
- **Preserved Excluded Candidate (`1`)**: `cesstibtantite` (historical `IMA:1980-068`), discredited/reclassified into `hydrokenomicrolite` (`IMA:2011-103`) and `hydroxycalciomicrolite` (`IMA:2013-073`) on IMA p. 98.
- **Preserved Multi-Source Held Candidates (`7`)**: `protasite` (`IMA:1984-001`), `lepersonnite-gd` (`1987 s.p.`), `lokkaite-y` (`1987 s.p.`), `haiweeite` (`1962 s.p.`), `fourmarierite` (`G 1924`), `masuyite` (`G 1947`), and `tsumoite` (`IMA:1972-010a`), held pending acquisition of missing external/paywalled primary type or structure papers.
- **Deferred External EJM Candidates Outside Round 123 Cohort (`13`)**: `erzwiesite`, `fengruiite`, `igelstromite`, `kenoargentotetrahedrite-zn`, `laurentthomasite`, `lazerckerite`, `lopatkaite`, `moabite`, `plumbogottlobite`, `tetrahedrite-cd`, `vielleaureite-ce`, `wumuite`, and `xianhuaite-ce` (listed in `/private/tmp/cmm-round123-research/ejm_candidates.json` for future cycles; no PDFs downloaded in Round 123).
- **Carried-Forward Open Source Issues**: `#495`, `#496`, `#497`, `#498`.
- **Frontier Status**: `bounded_frontier_exhausted: true`, `source_exhaustion_claimed: false`.
