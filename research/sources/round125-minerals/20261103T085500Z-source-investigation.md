# Round 125 Critical Mineral Source Investigation and Bounded Frontier Audit

- **Investigation ID:** `20261103T085500Z-round125-minerals`
- **Created At:** `2026-11-03T08:55:00Z` (updated `2026-11-03T10:20:00Z`)
- **Cycle / Stage:** Cycle 7, Stage 1 (`add_records`)
- **Corpus Transition:** `673 -> 678` records (`+5` records), `1245 -> 1255` canonical history sidecars (`+5` `CREATE` sidecars, `+5` `EDIT` sidecars)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`61` full-PDF pages total; `52` main-text pages) indexed into `154` UTF-8 text passages (`<= 1,800` bytes each; `217,676` passage bytes / `217,871` raw text bytes total; `130` main-text passages) plus `14` single-page PNG table renders (`150` DPI via `mutool draw`).

## 1. Inspected Primary Sources and Admitted Records (5)

| Slug | Name | IMA ID (Status) | End-Member Formula | Primary Source DOI, Verbatim Title & PDF SHA-256 | Full-PDF & Main-Text Pages / Passages / Table PNGs | Record SHA-256 | History Sidecars (`CREATE` & `EDIT`) & SHA-256 |
|---|---|---|---|---|---|---|---|
| `johanngeorgenstadtite` | Johanngeorgenstadtite | `IMA:2019-122` (`A`) | `Ni2+4.5(AsO4)3` | `10.5194/ejm-32-373-2020` (*Niasite and johanngeorgenstadtite, Ni2+4.5(AsO4)3 dimorphs from Johanngeorgenstadt, Germany*, Kampf, Nash, Plášil, Smith, & Feinglos 2020, `ejm-32-373-2020.pdf`, `10,637,805` B, `d714ae2487c000a867ff054cd60abe9369a81c2b57a51636e9e9f7c7d56cfdca`) | `13` full-PDF pp. / `32` passages (`44,785` passage B / `44,829` raw B; `11` main-text pp. / `26` passages) / pp. 4, 5, 6, 8 | `f736a07ae232dadb3c2bae2d258ddb3d9d64af0d0627e0ce2e1a24d6280c49cd` | `CREATE`: `history/records/johanngeorgenstadtite/2026-11-03T091254Z-antigravity-ee9475.yaml` (`c305dac622731dfe05d794eca2c752672e2ab8186f850c6b5ea619b45e32e4d7`); `EDIT`: `history/records/johanngeorgenstadtite/2026-11-03T101609Z-antigravity-9eb999.yaml` (`abdd24539ac419e7e08087e07e323ee452639816dec7e5e653c0ef2b64d744f9`) |
| `fengruiite` | Fengruiite | `IMA:2024-045` (`A`) | `[Ag6Sb2S7][Ag9CuS2Te2]` | `10.5194/ejm-38-519-2026` (*Fengruiite, [Ag6Sb2S7][Ag9CuS2Te2], a new Ag–Sb–Te sulfosalt mineral from the Haopinggou Ag–Pb–Zn–Au deposit, eastern Qinling, China*, Tian, Li, Sun, Liu, Mao, Dong, Liu, Jian, Yao, Wang, & Ye 2026, `ejm-38-519-2026.pdf`, `4,962,073` B, `da762fa683f8c94f20c1fccb76abf9aae03ebdf1f92004e29b8285180d202745`) | `12` full-PDF pp. / `32` passages (`45,151` passage B / `45,190` raw B; `10` main-text pp. / `27` passages) / pp. 4, 6 | `515efee2f6e88c788af7b97b3b403223291d5a80261d337ae4dcf0c33d427d9e` | `CREATE`: `history/records/fengruiite/2026-11-03T091257Z-antigravity-552763.yaml` (`d5a8fea13aeb7d60f4441112d9343b1ba10f37f910e08dad82101335539a01ef`); `EDIT`: `history/records/fengruiite/2026-11-03T101639Z-antigravity-778d08.yaml` (`5a4dd451f2ffb4b3e5652d4db2698e64ab172ac4289ca479aff9a739bc51d49e`) |
| `igelstromite` | Igelströmite | `IMA:2021-035` (`A`) | `Fe3+(SbPb)O4` | `10.5194/ejm-36-311-2024` (*Igelströmite, Fe3+(Sb3+Pb2+)O4, and manganoschafarzikite, Mn2+Sb3+2O4, two new members of the newly established minium group, from the Långban Mn–Fe deposit, Värmland, Sweden*, Holtstam, Langhof, Friis, Karlsson, & Erambert 2024, `ejm-36-311-2024.pdf`, `4,407,586` B, `0049c6a3f4a4a53c7af8e900ceb54cb41fe923eccb04f514e38d9147801c0ddf`) | `12` full-PDF pp. / `32` passages (`47,416` passage B / `47,455` raw B; `10` main-text pp. / `27` passages) / pp. 4, 5, 6 | `4c635cb707dbbecc9edbcfb330d71ebe43083139f1e77097d48e55acb8ecb5e0` | `CREATE`: `history/records/igelstromite/2026-11-03T091259Z-antigravity-e7affb.yaml` (`7fd21fa696b312027cdbca31aa2f698bab46aae4626156d79c6ef9c136738ebc`); `EDIT`: `history/records/igelstromite/2026-11-03T101706Z-antigravity-8ce276.yaml` (`7fa29ccec09a2e1dbe90cf3b6c3ebd50eb2c6cfc437fa2efa90243a568f96b7f`) |
| `plumbogottlobite` | Plumbogottlobite | `IMA:2025-075` (`A`) | `PbMg(VO4)(OH)` | `10.5194/ejm-38-209-2026` (*Plumbogottlobite, PbMg(VO4)(OH), the Pb analogue of gottlobite and the Mg analogue of descloizite*, Kampf, Désor, & Ma 2026, `ejm-38-209-2026.pdf`, `3,444,368` B, `701a0f29317d7c20f31baacdd671dd2341a00d4a7ff0f0ca4ff81983deb10ef0`) | `8` full-PDF pp. / `17` passages (`22,244` passage B / `22,268` raw B; `7` main-text pp. / `15` passages) / pp. 3, 4 | `3bd29fdbe517900ec60494b52a1d134f4d64c8668fe7ec0816f33f8c481f13af` | `CREATE`: `history/records/plumbogottlobite/2026-11-03T091301Z-antigravity-a67205.yaml` (`0638fda1d5ca3b4ce368ba332fb7fc57dee107417eb10e24ae766e5b51117d81`); `EDIT`: `history/records/plumbogottlobite/2026-11-03T101732Z-antigravity-eaa7f6.yaml` (`2895efb3a99cb6e2daf749ac87a3639ff007057e686232c671c68f01e8cc2031`) |
| `lazerckerite` | Lazerckerite | `IMA:2022-113` (`A`) | `Ag3.75Pb4.50(Sb7.75Bi4)S24` | `10.5194/ejm-36-641-2024` (*Lazerckerite, Ag3.75Pb4.5(Sb7.75Bi4)S24, from Kutná Hora, Czech Republic: a new Sb–Bi member of the andorite branch of the lillianite homologous series*, Pažout, Dušek, Sejkora, Plášil, Ilinca, & Dolníček 2024, `ejm-36-641-2024.pdf`, `10,805,315` B, `42715ed93c98fcac8bcdd97300e5f31e318175857c5abcced5104a3b7a9ee66b`) | `16` full-PDF pp. / `41` passages (`58,080` passage B / `58,129` raw B; `14` main-text pp. / `35` passages) / pp. 4, 5, 6 | `e80ce9a78928a66dd0acee3d3b7b47e8be2b9f7ff9ae90d78bbc07a35cd30bdf` | `CREATE`: `history/records/lazerckerite/2026-11-03T091303Z-antigravity-eb0f1a.yaml` (`f2820621e8f449f058c8ec92a4112700b8bad10f91762be0188df5622271ec30`); `EDIT`: `history/records/lazerckerite/2026-11-03T101757Z-antigravity-bc3b9b.yaml` (`a2da3b95e3d99fbaf01f4f8c6eb8d9774fffa1f2f93f2507e2a003d4a102a352`) |

### Primary-Source Discrepancies Documented in Admitted Records

1. **`johanngeorgenstadtite` (`Kampf et al. 2020`, *Eur. J. Mineral.* 32:373–385):**
   - Table 3 (p. 380) prints crystal dimensions as `40 mm x 30 mm x 20 mm` via a `mm`-for-`um` unit typo (`~70 um` grains in Section 3.1, p. 375) and reports crystallographic density `Dx = 4.880 g/cm3` for the refined cell contents `Ni4.61(AsO4)3` versus `Dcalc = 4.801 g/cm3` (empirical formula) and `4.808 g/cm3` (ideal formula) in Section 3.2 (p. 376).
   - Table 5b (p. 382) labels the six-bond octahedral mean distances as `<M1–O4> = 2.113 Å` and `<M2–O4> = 2.061 Å` instead of `<M1–O>` and `<M2–O>`.
   - Table 6b (p. 383) lists bond-valence sums for `A1'` (`2.04 v.u.`) and `A2'` (`0.50 v.u.`) that differ by `0.01 v.u.` from Section 7.2 prose on p. 384 (`2.03` and `0.49 v.u.`).
2. **`fengruiite` (`Tian et al. 2026`, *Eur. J. Mineral.* 38:519–530):**
   - The Abstract (p. 519) describes macroscopic color as `gray`, whereas Section 4.1 (p. 522) describes it as `black-gray`; the Fig. 3 caption (p. 523) prints the mineral abbreviation as `Frui` whereas the official IMA symbol is `Fru` (p. 519).
   - The Abstract (p. 519) and Section 4.2 (p. 522) print the empirical formula as `[(Ag5.87Cu0.29)Sigma6.16(Sb1.89As0.03)Sigma1.92S7][Ag9CuS2(Te1.28S0.63)S1.91]` with a typographical `S1.91` in place of `Sigma1.91`.
   - Section 4.3 prose (p. 524) prints `R1 = 0.0667`, whereas Table 2 (p. 524) rounds it to `R1 = 0.067`.
3. **`igelstromite` (`Holtstam et al. 2024`, *Eur. J. Mineral.* 36:311–322):**
   - Section 3 (p. 313) prints the optical reflectance spectral range as `400–70 nm range` (typo for `400–700 nm`), and Section 5.1 (p. 314) prints the MoKalpha wavelength as `lambda = 0.71703 Å` (transposition typo for `0.71073 Å`).
   - Table 3 (p. 315) prints the analytical total as `98.17 wt%` whereas the arithmetic sum of rounded oxide means (`Sb2O3 42.89 + PbO 34.42 + Fe2O3 11.05 + MnO 4.78 + As2O3 3.88 + FeO 1.14`) is `98.16 wt%`.
   - Table 5 (p. 316) prints the fractional-coordinate header as `Site | x | y | x` (with a duplicate `x` in place of `z`), and Table 6 (p. 316) lists the `X(Sb,Pb)` site population as `Sb0.625Pb0.325As0.055`, which sums to `1.005` per site (`2.01 pfu`).
4. **`plumbogottlobite` (`Kampf, Désor, & Ma 2026`, *Eur. J. Mineral.* 38:209–216):**
   - Section 1 (p. 209) lists `Warr symbol: Pgot`, whereas the September 2026 IMA Master List (p. 174) assigns official IMA symbol `Pgtb`.
   - Section 3 (p. 210) writes `Optically, plumbogottlobite is uniaxial (–)` in the sentence immediately preceding `2V = 84(1)°` and `Y = c` (which define a biaxial (–) crystal).
   - The Abstract (p. 209) places all `Mn2+` at the octahedral site as `(Pb0.89[]0.11)Sigma1.00(Mg0.77Cu2+0.19Mn2+0.09)Sigma1.05(VO4)(OH)` (`+0.12 H`), whereas Section 4 (p. 210) partitions `Mn2+` across both cation sites as `(Pb0.89Mn2+0.05[]0.06)Sigma1.00(Mg0.77Cu2+0.19Mn2+0.04)Sigma1.00(VO4)(OH)` (`+0.12 H`).
   - Table 3 (p. 212) prints `c = 9.3986(8) Å` (digit transposition of `c = 9.3968(8) Å` reported in the Abstract, p. 209, and Table 7, p. 215, which yields `V = 436.88 Å3`) and transposes index ranges `l` and `k` (`-7 <= l <= 7`, `-11 <= k <= 11` for `b = 6.11 Å`, `c = 9.40 Å`).
   - Table 5 (p. 214) prints the six-bond octahedral mean distance as `<Mg–O> = 2.157 Å` whereas the arithmetic mean of `2.025(6) x 2`, `2.156(7) x 2`, and `2.187(7) x 2 Å` is `2.123 Å` (and prints `<V–O> = 1.722 Å` vs true four-bond mean `1.731 Å` of `1.651(10)`, `1.756(9)`, and `1.758(8) x 2 Å`), and Table 6 (p. 214) misplaces the `x2` multiplier onto `V–O3` instead of `V–O1`.
5. **`lazerckerite` (`Pažout et al. 2024`, *Eur. J. Mineral.* 36:641–656):**
   - Official IMA symbol is `Lzc` (IMA Master List, p. 122), whereas Figs. 2 and 3 (p. 643) label the mineral `Lze`; Table 1 (p. 644) prints `Rmax` at `500 nm` as `39-2` for `39.2%`.
   - The Abstract (p. 641) and Section 4 (p. 646) print the empirical formula with `Pb4.55Fe0.01Cd0.01` and `S24.15Se0.01` (`Sigma24.16`), whereas Table 12 (p. 654) prints `Pb4.54Fe0.02Cd0.01` and `S24.14Se0.01` (`Sigma24.15`).
   - Table 4 (p. 646) lists `26,345` measured reflections, `Rint = 0.0839`, `GOF(all) = 2.097`, and refined structural formula `Ag3.65Pb4.72Sb7.42Bi4.11S24` (from Table 5 refined SOFs), whereas Section 5 prose (p. 646) writes `25,883` measured reflections, `Rint = 0.0852`, `GOF = 2.10`, Section 5 prose (p. 648) gives an EPMA-adjusted site-population formula summing to `Ag3.61Pb4.54Sb7.87Bi3.75S24`, and Section 7 prose (p. 650) prints `M9` with `0.835Ag + 0.125Bi` (vs `0.825(14)Ag + 0.125(14)Bi` in Table 5).

## 2. Remaining Deferred External Single-Reference Candidates (9)

The following 9 IMA-approved single-reference candidates remain deferred for bounded PDF acquisition and passage indexing in subsequent rounds (including `niasite` and `manganoschafarzikite`, which are co-described in the primary papers inspected in Round 125 and ready for curation in Round 126):

1. `carletonmooreite` (`IMA:2018-068`, `Ni3Si`, IMA p. 37, *American Mineralogist* 106 (2021), 1828)
2. `changesite-y` (`IMA:2022-023a`, `(Ca,Y)8(Fe2+,Mg)2(PO4)7`, IMA p. 41, *Matter and Radiation at Extremes* 9 (2024), 027401)
3. `chihmingite` (`IMA:2022-010`, `NiAl2O4`, IMA p. 43, *European Journal of Mineralogy* 34 (2022), 359)
4. `ferroberaunite` (`IMA:2021-036`, `Fe2+Fe3+5(PO4)4(OH)5·6H2O`, IMA p. 70, *Mineralogical Magazine* 86 (2022), 363)
5. `gysinite-la` (`IMA:2022-008`, `PbLa(CO3)2(OH)·H2O`, IMA p. 88, *Mineralogical Magazine* 87 (2023), 143)
6. `haleniusite-ce` (`IMA:2021-042`, `CeOF`, IMA p. 89, *The Canadian Mineralogist* 60 (2022), 713)
7. `ikranite` (`IMA:2000-010`, `(Na,H3O)15(Ca,Mn,REE)6Fe3+2Zr3([],Zr)([],Si)Si24O66(O,OH)6Cl·nH2O`, IMA p. 100, *Zapiski Vserossijskogo Mineralogicheskogo Obshchestva* 132(5) (2003), 22 / *Crystallography Reports* 48 (2003), 717)
8. `manganoschafarzikite` (`IMA:2022-129`, `Mn2+Sb3+2O4`, IMA p. 135, *European Journal of Mineralogy* 36 (2024), 311–322)
9. `niasite` (`IMA:2019-105`, `Ni2+4.5(AsO4)3`, IMA p. 154, *European Journal of Mineralogy* 32 (2020), 373–385)

## 3. Excluded Non-Critical & Multi-Source Held Candidates

- **Excluded (`1`):** `cesstibtantite` (`(Cs,Na)SbTa4O12`, IMA p. 41, discredited species status `D`, redefined as `hydroxykenomicrolite`).
- **Multi-Source Held (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y` (require multiple historical or paywalled references before curation).
- **Open Source Issues Tracked (`4`):** `#495` (`uniprot_metal_cofactors`), `#496` (`bacdive_metal_utilization`), `#497` (`brenda_metal_enzymes`), `#498` (`rhea_metal_reactions`).
