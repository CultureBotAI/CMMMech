# Round 129 Source Investigation Dossier — Open-Access EJM Critical-Element Minerals (Cycle 11, Stage 1)

- **Investigation ID**: `cmmmech-round129-source-investigation-20261106T171500Z`
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 11, Stage 1 (`add_records`)
- **Timestamp (UTC)**: `2026-11-06T18:35:00Z`
- **Corpus Progression**: `693 -> 698` records (`+5`), `1414 -> 1421` history sidecars (`+5` `CREATE`, `+2` `EDIT`), `1137 -> 1142` structured reviews (`+5`)
- **Primary Authority**: IMA-CNMNC List of Minerals (September 2026, `ima_2026_09`, pages 23, 27, 54, 75, 130, 240)
- **Bounded Source-Text Indexing**: 5 open-access *European Journal of Mineralogy* PDFs (`68` full-PDF pages, `56` main-text pages, `196` bounded passages `<= 1,800 B`, `11` single-page 150-DPI PNG table renders)

## 1. Curated Mineral Species and Primary Sources (`+5`)

### 1.1 `zhiqinite` (`cmmmech:zhiqinite`, `IMA:2019-077`, symbol: `none assigned`)
- **IMA Master List (September 2026)**: Page `240`, status `A (Approved 2019; full paper published November 2020)`, ideal formula `TiSi2`
- **Constituent Critical Elements**: `Ti, Si`
- **Type Locality**: Inclusion in a corundum grain (>200 um) separated from podiform chromitite orebody Cr-11, Luobusa ophiolite, Yarlung Zangbo suture zone, ~200 km ESE of Lhasa, Tibet, China
- **Type Specimens**: Holotype M13817 (source of focused-ion-beam TEM foil no. 5358) and FIB foil no. 5358, deposited at the Chinese Geological Museum, Xisiyangrouhutong 15th, Xicheng District, Beijing, China
- **Primary Reference**: Xiong F, Xu X, Mugnaioli E, Gemmi M, Wirth R, Grew ES, Robinson PT, Yang J (2020) Two new minerals, badengzhuite, TiP, and zhiqinite, TiSi2, from the Cr-11 chromitite orebody, Luobusa ophiolite, Tibet, China: is this evidence for super-reduced mantle-derived fluids? European Journal of Mineralogy 32:557-574 (`https://doi.org/10.5194/ejm-32-557-2020`, `ejm-32-557-2020.pdf`, `13146556` B, SHA-256 `12c366bf1f944d91336b55b5f790c5e19038c7f4b33d5b0c2a1d958f5461c86c`)
- **Chemical Analysis**: Table 3 (p. 564) standardless TEM-EDX chemistry (n = 4 analyses at points 428, 429, 430, and 431 in foil no. 5358: mean Si 57.61 wt% [SD 2.15, range 55.21-60.42 wt%; 69.84 at.%, SD 1.85], Ti 42.39 wt% [SD 2.15, range 39.58-44.79 wt%; 30.16 at.%, SD 1.85], sum 100 wt%, empirical formula Ti0.905Si2.095 on the basis of 3 cations/atoms)
- **Crystallography & Structure**: orthorhombic Fddd (#70) 3D electron diffraction structure (Table 5 and Figure 7, p. 566-567; a = 8.18(16) A, b = 4.85(10) A, c = 8.42(17) A, V = 334(12) A3, Z = 8, 65 of 81 patterns over 80 deg tilt at 1 deg steps, dynamical refinement R(3sigma) = 0.1015 at point 428; Dcalc = 4.136 g/cm3 vs 3.85 g/cm3 for C49 polymorph and 4.07 g/cm3 measured on synthetic TiSi2; 10-coordinated Ti with Ti-Si = 2.51(8)-2.80(5) A)
- **Documented Primary-Source Discrepancies**:
  - The Abstract (p. 557) describes zhiqinite as having 'a primitive orthorhombic cell' with space group Fddd, whereas Section 5.4 and Figure 6 (p. 566) confirm that space group Fddd (#70) has an F-centered orthorhombic lattice with characteristic chess-board extinctions and hk0: h + k = 4n d-glide conditions.
  - Section 4.1 (pp. 560-563) and Section 6.2 (pp. 568-569) document the scientific controversy raised by Litasov et al. (2019a,b) alleging that the Cr-11 corundum grains and enclosed ultra-reduced phases represent anthropogenic brown fused alumina abrasive, which Xiong et al. (2020) rebut on the basis of mineralogical and textural differences.
- **Curated Record**: `data/records/zhiqinite.yaml` (`8966` B, SHA-256 `b6c6a35f0478450ff1782c685f1fc417495a3327891792a082c0811a11d1f21c`)
- **History Sidecars**:
  - `history/records/zhiqinite/2026-11-06T171100Z-antigravity-a1e4c9.yaml` (`975` B, SHA-256 `ef47495c1d0dfd92305b43b2fc8ffd1bf77efacc33e0a184532018567bed586d`)
  - `history/records/zhiqinite/2026-11-06T183100Z-antigravity-f1a2b3.yaml` (`1003` B, SHA-256 `d4f9a0de77e620b7165593bcb3c5d2f1137de5912254d64ec3de1cfd12d83022`)

### 1.2 `belmonteite` (`cmmmech:belmonteite`, `IMA:2024-040`, symbol: `Bmo`)
- **IMA Master List (September 2026)**: Page `23`, status `A (Approved 2024; full paper published August 2026)`, ideal formula `CaMn2(AsO4)2(H2O)5*2H2O (CaMn2(AsO4)2(H2O)6*H2O in IMA Master List; CaMn2(AsO4)2*7H2O in Section 4 & Table 8)`
- **Constituent Critical Elements**: `Mn, As, Cu, Al`
- **Type Locality**: Dumps of the Gambatesa mine (44 deg 21 min 34 sec N, 9 deg 26 min 59 sec E), Graveglia Valley, Ne, Genoa Province, Liguria, Italy
- **Type Specimens**: Holotype MO720 (mineralogical collection of the Dipartimento di Scienze della Terra dell'Ambiente e della Vita, DISTAV, University of Genoa, Italy); Holotype SCXRD grain 20076 (Museo di Storia Naturale, University of Pisa, Via Roma 79, Calci, Pisa, Italy)
- **Primary Reference**: Biagioni C, Sejkora J, Dolnicek Z (2026) Belmonteite, CaMn2(AsO4)2(H2O)5*2H2O, a new arsenate mineral from the Mn ore deposits of the Graveglia Valley, eastern Liguria, Italy. European Journal of Mineralogy 38:531-543 (`https://doi.org/10.5194/ejm-38-531-2026`, `ejm-38-531-2026.pdf`, `6245239` B, SHA-256 `bc4240014f8067a727de189e861efdcf3b6590e56d234754f2506b186517d4f8`)
- **Chemical Analysis**: Table 1 (p. 534) EPMA chemistry (n = 8 spot analyses: As2O5 48.57, MnO 29.94, CaO 10.12, CuO 1.28, Al2O3 0.22, K2O 0.10, H2Ocalc 26.51, unnormalized total 116.74 wt%, normalized total 100.00 wt%, empirical formula (Ca0.86Mn0.11K0.01)Sigma0.98(Mn1.90Cu0.08Al0.02)Sigma2.00As2.01O8*7H2O on the basis of 15 O apfu)
- **Crystallography & Structure**: orthorhombic Cmce (#64) single-crystal structure (Tables 3-7, pp. 538-540; a = 8.8418(9) A, b = 23.031(2) A, c = 13.5270(14) A, V = 2754.6(5) A3, Z = 8, R1 = 0.0385 for 1195 reflections with F > 4sigma(F), wR2 = 0.1047, Goof = 1.069; powder cell a = 8.854(7) A, b = 23.02(2) A, c = 13.533(13) A, V = 2759(3) A3; Dcalc = 2.677 g/cm3; six-fold distorted octahedral Ca(2)O3(H2O)3 coordination across all 8 ordered ligand configurations in Table 7)
- **Documented Primary-Source Discrepancies**:
  - Section 4 (p. 533) reports the ideal oxide composition for stoichiometric CaMn2(AsO4)2*7H2O as As2O5 41.49, CaO 10.12, MnO 25.61, and H2O 22.77 wt% for a printed sum of 100.00 wt%, whereas the four rounded constituent values sum to 99.99 wt%.
  - Table 2 (p. 537) prints both calculated d-spacing column headers as 'd*calc' instead of 'd*calc' and 'dcalc' and misprints d*calc = 2.224 A for reflection (0 4 5) alongside dobs = 2.446 A and dcalc = 2.449 A (where the true powder-cell spacing is 2.450 A).
- **Curated Record**: `data/records/belmonteite.yaml` (`9125` B, SHA-256 `d6af627cccdc903feaf71a74ad71d1f597ebcfb2f38341023c9d674258b458bb`)
- **History Sidecars**:
  - `history/records/belmonteite/2026-11-06T171105Z-antigravity-b2f5d8.yaml` (`1015` B, SHA-256 `86e12e820d1e952c01e4c376e5a27ce383b7d7235c73f386145d3c31d20d0052`)
  - `history/records/belmonteite/2026-11-06T183105Z-antigravity-e4d5c6.yaml` (`843` B, SHA-256 `632eb949449238bcf27ed28f1624b8fbe048c038531ef4af1a4e51d6c826c74b`)

### 1.3 `dacostaite` (`cmmmech:dacostaite`, `IMA:2024-015`, symbol: `Dcs`)
- **IMA Master List (September 2026)**: Page `54`, status `A (Approved 2024; full paper published January 2025)`, ideal formula `K(Mg2Al)[Mg(H2O)6]2(AsO4)2F6*2H2O`
- **Constituent Critical Elements**: `Mg, Al, As, F, Cu, Zn, P`
- **Type Locality**: Stanza Santoni underground exploitation void, Cetine di Cotorniano Mine (43 deg 13 min N, 11 deg 09 min E), Chiusdino, Siena province, Tuscany, Italy
- **Type Specimens**: Holotype 20073 (Museo di Storia Naturale, University of Pisa, Via Roma 79, Calci, Pisa, Italy)
- **Primary Reference**: Biagioni C, Mauro D, Sejkora J, Dolnicek Z, Dini A, Skoda R (2025) Dacostaite, K(Mg2Al)[Mg(H2O)6]2(AsO4)2F6 * 2H2O, a new fluoride-arsenate mineral from the Cetine di Cotorniano Mine (Tuscany, Italy). European Journal of Mineralogy 37:39-52 (`https://doi.org/10.5194/ejm-37-39-2025`, `ejm-37-39-2025.pdf`, `6041860` B, SHA-256 `ec6741ca8042912abf9977f3919c3e38382a4e6e463a45def571e6cb18f13df5`)
- **Chemical Analysis**: Table 1 (p. 42) EPMA chemistry (n = 10 spot analyses: As2O5 35.42, MgO 21.13, F 13.15, Al2O3 12.23, K2O 4.13, CuO 0.42, CaO 0.36, ZnO 0.34, P2O5 0.17, Na2O 0.15, MnO 0.04, FeO 0.04, sum 87.58, O=-F -5.54, H2Ocalc 41.40, unnormalized total 123.44 wt%, normalized total 100.00 wt%, empirical formula (K0.56Ca0.04Na0.03[]0.37)Sigma1.00(Al1.54Mg1.38Cu0.03Zn0.03)Sigma2.98[Mg(H2O)6]2[(As0.99P0.01)O4]2[F4.46(OH)1.46O0.08]Sigma6.00*2H2O)
- **Crystallography & Structure**: monoclinic C2/m (#12) single-crystal structure (Tables 3-7, pp. 43-46; a = 12.474(5) A, b = 7.198(3) A, c = 13.724(6) A, beta = 99.518(13) deg, V = 1215.3(8) A3, Z = 2, R1 = 0.0927 for 1022 reflections with Fo > 4sigma(Fo), wR2 = 0.2574, GoF = 1.055; powder cell a = 12.4760(18) A, b = 7.1974(11) A, c = 13.7211(18) A, beta = 99.549(12) deg, V = 1215.0(2) A3; Dcalc = 2.162 g/cm3)
- **Documented Primary-Source Discrepancies**:
  - Table 3 (p. 43) prints the h index range as '-15 <=h15' with a missing '<=' symbol.
  - Section 4.3.2 (pp. 43 and 45) cites bond-valence sums of 5.14 v.u. for As(1) and 2.52 and 2.53 v.u. for M(1) and M(2), whereas Table 6 (p. 45) lists 5.11, 2.54, and 2.54 v.u., respectively.
  - Section 4.3.3 (p. 46) states that 'O(2) accepts H bonds from two Ow(2) groups', whereas Tables 6 and 7 show that O(2) accepts two H bonds from Ow(3) at 2.670(13) A while Ow(2) donates H bonds to O(1) at 2.763(10) A.
- **Curated Record**: `data/records/dacostaite.yaml` (`8476` B, SHA-256 `f68cebd5614b16798da37084a258ad7e89b0692e872049d491a3add96053f356`)
- **History Sidecars**:
  - `history/records/dacostaite/2026-11-06T171110Z-antigravity-c3a6e7.yaml` (`992` B, SHA-256 `3af313ea7863b833ec326ce476088155a4cd5a7a2f6928cf684db077a4d791ad`)

### 1.4 `fluormacraeite` (`cmmmech:fluormacraeite`, `IMA:2024-054`, symbol: `none assigned`)
- **IMA Master List (September 2026)**: Page `75`, status `A (Approved 2024; full paper published March 2025)`, ideal formula `[(H2O)K]Mn2(Fe2Ti)(PO4)4[OF](H2O)10*4H2O`
- **Constituent Critical Elements**: `Mn, Ti, P, F, Mg, Al`
- **Type Locality**: Plossberg phosphate pegmatite (Lindner Mine / Lindner Quarry dumps), Tirschenreuth district, Upper Palatinate, Bavaria, Germany
- **Type Specimens**: Holotype MSM38573 (Mineralogical State Collection, SNSB, Munich, Germany); Cotype 76422 (Natural History Museum of Los Angeles County, USA)
- **Primary Reference**: Grey IE, Rewitzer C, Hochleitner R, Kampf AR, Boer S, Mumme WG, Wilson NC, Davidson CJ (2025) Fluormacraeite, [(H2O)K]Mn2(Fe2Ti)(PO4)4[OF](H2O)10 * 4H2O, the first type mineral from the Plossberg pegmatite, Upper Palatinate, Bavaria, Germany. European Journal of Mineralogy 37:169-179 (`https://doi.org/10.5194/ejm-37-169-2025`, `ejm-37-169-2025.pdf`, `5256173` B, SHA-256 `689507e22de88069e6a32dff43eb4f21c448c5be4fafb280c0d38d432c74ef32`)
- **Chemical Analysis**: Table 1 (p. 171) cold-stage EPMA chemistry (n = 8 analyses on 2 crystals: P2O5 28.51, Fe2O3 14.74, MnO 12.49, TiO2 8.19, K2O 4.41, F 1.55, MgO 1.07, Al2O3 0.65, H2Ocalc 27.13, -O=F -0.65, printed Total 98.10 wt%, exact arithmetic sum 98.09 wt%, structural empirical formula A1[K0.14(H2O)0.76]Sigma0.90A2[K0.79(H2O)0.21]Sigma1.00M1(Mn2+1.75Mg0.25)Sigma2.00M2+M3(Fe3+1.84Al0.13Ti4+1.02Mg0.01)Sigma3.00(PO4)4.00X[O0.94F0.81(OH)0.25]Sigma2.00(H2O)10*3.90H2O)
- **Crystallography & Structure**: monoclinic P21/c (#14) synchrotron 100 K single-crystal structure (Tables 3-8, pp. 173-177; a = 10.546(2) A, b = 20.655(1) A, c = 12.405(1) A, beta = 90.09(1) deg, V = 2702.1(6) A3, Z = 4, Robs = 0.0559, wRobs = 0.0700 for 5646 reflections with I > 3sigma(I), GoF = 2.43; powder cell a = 10.531(17) A, b = 20.652(18) A, c = 12.408(17) A, beta = 90.1(2) deg, V = 2699(6) A3; Dcalc = 2.39 g/cm3)
- **Documented Primary-Source Discrepancies**:
  - Section 1 (p. 170) reports the Plossberg locality as 18 km from Hagendorf, whereas Section 2 (p. 170) states 15 km north-northeast of Hagendorf.
  - Table 1 (p. 171) prints Total = 98.10 wt%, whereas the exact arithmetic sum of the printed mean constituents (P2O5 28.51 + Fe2O3 14.74 + MnO 12.49 + TiO2 8.19 + K2O 4.41 + F 1.55 + MgO 1.07 + Al2O3 0.65 + H2Ocalc 27.13 - O=F 0.65) is 98.09 wt%.
  - The Abstract (p. 169) mislabels Robs = 0.0559 as 'wRobs = 0.0559' for 5646 reflections with I > 3sigma(I), whereas Table 3 (p. 173) and Section 6.2 confirm Robs = 0.0559 and wRobs = 0.0700.
- **Curated Record**: `data/records/fluormacraeite.yaml` (`7222` B, SHA-256 `45fd1fb6d0e32f403592314e20585b1ca8da0e0ed5aa3543b97548aa1bb94837`)
- **History Sidecars**:
  - `history/records/fluormacraeite/2026-11-06T171115Z-antigravity-d4b7f6.yaml` (`992` B, SHA-256 `30cc42dafd07941c2c5a4d021c8a26e923edfacd2f959555573838fd6a77971c`)

### 1.5 `macraeite` (`cmmmech:macraeite`, `IMA:2023-065`, symbol: `none assigned`)
- **IMA Master List (September 2026)**: Page `130`, status `A (Approved 2023; full paper published March 2024)`, ideal formula `[(H2O)K]Mn2(Fe2Ti)(PO4)4[O(OH)](H2O)10*4H2O`
- **Constituent Critical Elements**: `Mn, Ti, P, F, Mg, Al`
- **Type Locality**: Chao do Castanheiro mining concession dumps, Cubos-Mesquitela-Mangualde pegmatite (40 deg 35 min 13.7 sec N, 7 deg 45 min 04.3 sec W), Viseu district, Portugal
- **Type Specimens**: Holotype 76293 (Natural History Museum of Los Angeles County, USA); Cotype MSM 38050 (Bavarian State Collection for Mineralogy, SNSB, Munich, Germany)
- **Primary Reference**: Grey IE, Rewitzer C, Hochleitner R, Kampf AR, Boer S, Mumme WG, Wilson NC (2024) Macraeite, [(H2O)K]Mn2(Fe2Ti)(PO4)4[O(OH)](H2O)10 * 4H2O, a new monoclinic paulkerrite-group mineral, from the Cubos-Mesquitela-Mangualde pegmatite, Portugal. European Journal of Mineralogy 36:267-278 (`https://doi.org/10.5194/ejm-36-267-2024`, `ejm-36-267-2024.pdf`, `7405708` B, SHA-256 `6e0abe558c782b2619a2fe0d50e1ff14e863f57ff98a751e2ec78cdc3b3920de`)
- **Chemical Analysis**: Table 1 (p. 269) EPMA chemistry (n = 17 analyses on 17 crystals: P2O5 29.55, MnO 14.63, Fe2O3 11.80, TiO2 9.85, K2O 4.14, Al2O3 1.65, F 1.04, MgO 0.35, H2Ocalc 28.90, -O=F -0.44, mean Total 101.47 wt%, bulk empirical formula K0.84Mn1.98Mg0.08Al0.31Fe3+1.42Ti4+1.18P4.00F0.53O32.63H30.92, structural formula A1[(H2O)0.83K0.17]Sigma1.00A2[K0.65(H2O)0.35]Sigma1.00M1(Mn2+1.98[]0.02)Sigma2.00M2(Fe3+1.09Al0.31Ti4+0.52Mg0.08)Sigma2.00M3(Ti4+0.66Fe3+0.34)Sigma1.00(PO4)4X[O0.87F0.53(OH)0.60]Sigma2.00(H2O)10*4H2O)
- **Crystallography & Structure**: monoclinic P21/c (#14) synchrotron 100 K single-crystal structure (Tables 3-7, pp. 273-277; a = 10.562(2) A, b = 20.725(4) A, c = 12.416(2) A, beta = 90.09(3) deg, V = 2717.8(9) A3, Z = 4, Robs = 0.047, wRobs = 0.063 for 4990 reflections with Io > 3sigma(I); 300 K cell a = 10.5383(4) A, b = 20.7316(7) A, c = 12.4658(5) A, beta = 90.144(5) deg; powder cell a = 10.56(3) A, b = 20.70(3) A, c = 12.39(3) A, beta = 90.1(5) deg, V = 2708(11) A3; Dcalc = 2.39 g/cm3)
- **Documented Primary-Source Discrepancies**:
  - Table 7 (p. 277) misprints the ideal formula of macraeite as '[(H2O)K]Mn2(Fe2Ti)(PO4)4[(O(OH)]2(H2O)10*4H2O'.
  - Section 5 (p. 270) prints 3460 cm-1 twice in the list of O-H stretching shoulder wavenumbers ('shoulders at 3580, 3460 and 3250 cm-1' on the band centred at 3460 cm-1).
  - The Abstract (p. 267), Section 6.2 (pp. 270 and 272), and Table 3 (p. 273) exhibit minor internal differences in wRobs (0.065 vs 0.063), synchrotron wavelength (0.7109 vs 0.7107 A), and observed reflection count (4979 vs 4990).
- **Curated Record**: `data/records/macraeite.yaml` (`7570` B, SHA-256 `1d06cfe408539e3b3eabb7611c0145110428d6706b4fec4b7942519b2f7ca822`)
- **History Sidecars**:
  - `history/records/macraeite/2026-11-06T171120Z-antigravity-e5c8a1.yaml` (`974` B, SHA-256 `e72352428ed8466bcbc739cc8f32fe85dbba4b7b66e43bebb90937006a941968`)

## 2. Preserved Frontier Candidates

- **Open-Access EJM Single-Reference Queue (`5`)**: `spaltiite` (`IMA:2014-012`), `tianhuixinite` (`IMA:2022-081`), `zhenruite` (`IMA:2022-050`), `keutschite` (`IMA:2014-038`), `heimite` (`IMA:2022-019`).
- **Multi-Reference Queue (`1`)**: `bonacinaite` (`IMA:2018-056`, *Mineralogical Magazine* 84 (2020), 568; *European Journal of Mineralogy* 36 (2024), 863).
- **Non-EJM Single-Reference Queue (`7`)**: `carletonmooreite` (`IMA:2018-068`), `changesite-y` (`IMA:2022-023`), `chihmingite` (`IMA:2022-010`), `ferroberaunite` (`IMA:2021-036`), `gysinite-la` (`IMA:2022-008`), `haleniusite-ce` (`IMA:2003-028`), `ikranite` (`IMA:2000-010`).
