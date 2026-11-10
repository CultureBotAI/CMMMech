# CMMMech Round 132 Source Investigation Dossier (`20261110T193500Z`)

- **Investigation ID**: `cmmmech-round132-source-investigation-20261110T193500Z`
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 14, Stage 1 (`add_records`)
- **Corpus Transition**: `708 -> 713` records (`+5`), `1544 -> 1549` canonical history sidecars (`+5` `CREATE`), `1285 -> 1290` structured review bundles (`+5` scientific reviews)
- **Primary Authority Catalog**: `IMA_Master_List_(2026-09).pdf` (`3,129,886` B, SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`, pages 21, 76, 78, 84, 242)
- **Bounded Passage Indexing**: 5 open-access *European Journal of Mineralogy* PDFs (`58` full-PDF pages / `51` main-text pages, `162` total passages / `135` main-text passages `<= 1,800` B each, `235,091` passage bytes, plus `30` single-page 150-DPI PNG renders)

## Curated Records and Primary Sources

| Slug | IMA ID | IMA Symbol | Formula | Critical Elements | Primary DOI | Record SHA-256 | History Sidecar |
|---|---|---|---|---|---|---|---|
| `batoniite` | `IMA:2023-008` | none | `[Al8(OH)14(H2O)18](SO4)5 * 5H2O (Al8(SO4)5(OH)14(H2O)18*5H2O in IMA Master List)` | Al | https://doi.org/10.5194/ejm-35-703-2023 | `8b9a2d3b714bf264...` | `history/records/batoniite/2026-11-10T193154Z-antigravity-762ae9.yaml` |
| `fluor-rewitzerite` | `IMA:2023-115` | none | `[(H2O)K]Mn2(Al2Ti)(PO4)4(OF)(H2O)10 * 4H2O` | Mn, Al, Ti, F, Mg | https://doi.org/10.5194/ejm-36-541-2024 | `7e6e8d4fb3c5dfc3...` | `history/records/fluor-rewitzerite/2026-11-10T193156Z-antigravity-8797f5.yaml` |
| `friisite` | `IMA:2024-047` | `Fii` | `Pb8Al3Si8O27Cl3` | Al, Si, Mn, Zn | https://doi.org/10.5194/ejm-38-169-2026 | `5a677b637a8658bc...` | `history/records/friisite/2026-11-10T193158Z-antigravity-fd529c.yaml` |
| `gobelinite` | `IMA:2018-167` | none | `CoCu4(SO4)2(OH)6 * 6H2O (CoCu4(SO4)2(OH)6(H2O)6 in IMA Master List)` | Co, Cu, Ni, Zn | https://doi.org/10.5194/ejm-32-637-2020 | `09f50c3c295cc230...` | `history/records/gobelinite/2026-11-10T193159Z-antigravity-383cc5.yaml` |
| `zinkgruvanite` | `IMA:2020-031` | none | `Ba4Mn2+4Fe3+2(Si2O7)2(SO4)2O2(OH)2` | Ba, Mn, Si, Ti, Al, F, Mg | https://doi.org/10.5194/ejm-33-659-2021 | `1ce522a354582c4a...` | `history/records/zinkgruvanite/2026-11-10T193201Z-antigravity-38afcb.yaml` |

## Documented Primary-Source Discrepancies

### `batoniite` (Batoniite, `IMA:2023-008`)
- The September 2026 IMA Master List (PDF p. 21) writes the formula as Al8(SO4)5(OH)14(H2O)18*5H2O, whereas Mauro et al. (2023) write the structural formula as [Al8(OH)14(H2O)18](SO4)5 * 5H2O.
- The Abstract (p. 703) specifies '811 parameters and 60 restraints' for the single-crystal refinement, whereas Table 2 (p. 706) lists 'Number of least-squares parameters: 811' without a restraints row.
- In the Abstract (p. 703), the fifth strongest powder X-ray diffraction line at dobs = 4.324 A (m) is indexed as '201, -202, 104', whereas in Table S2 (p. 709) it is indexed as '2 0 1, -2 0 2, 1 0 -4' (with dcalc = 4.361, 4.311, 4.294 A), and two additional reflections at dobs = 9.21 A (1 0 0) and 3.679 A (-1 0 5) are also rated 'm' (medium) in Table S2.

### `fluor-rewitzerite` (Fluor-rewitzerite, `IMA:2023-115`)
- The Abstract (p. 541) reports the gamma refractive index as gamma = 1.602(3), whereas Section 3 (p. 542) prints gamma = 1.6021(3) (with an extra fourth decimal digit).
- In Table 3 (p. 547), the row 'Largest diff. peak and hole' prints '0.99 and -1.25 e A2' with a typographical exponent 'A2' instead of 'A-3'.
- In Table 5 (p. 548), the refined site electron counts are A1 = 8.6 e (0.85 H2O + 0.15 K) and A2 = 17.0 e (1.00 K), whereas Table 9 (p. 552) transposes and slightly alters them as 'A1, A2 = 17.1, 8.9'.
- In Section 4 (p. 543), the ideal end-member oxide percentages (K2O 5.04, MnO 15.16, Al2O3 10.90, TiO2 8.54, P2O5 30.34, F 2.03, H2O 28.86, -O = F -0.85) are stated to have 'total 100.00 wt %', whereas their exact arithmetic sum is 100.02 wt%.

### `friisite` (Friisite, `IMA:2024-047`)
- The first sentence of the Abstract (p. 169) misspells the mineral name as 'Friiste'.
- Table 1 (p. 171) prints Total = 98.98 wt%, whereas the exact arithmetic sum of the rounded mean constituents (0.14 + 4.42 + 19.80 + 4.19 + 0.19 + 0.31 + 0.63 + 0.42 + 69.83 - 0.94) is 98.99 wt%.
- Calculated density is reported as 5.54(1) g cm-3 in the Abstract (p. 169) and Section 3 (p. 170) vs 5.54 g cm-3 in Table 3 (p. 173), and unit-cell parameter a is printed as 8.5955(1) A in the Abstract vs 8.59550(10) A in Table 3.
- In Section 5 (p. 171), the intense low-wavenumber Raman bands are listed as '29, 42, 52, 63, 72, 96 123, 179, and ~213 cm-1' (omitting the comma between 96 and 123), whereas the top of p. 172 refers to the two bands as '64 and 73 cm-1' instead of '63, 72 cm-1'.
- In Section 7.1 (p. 176), reaction (R2) prints 'NaAlSi3O8 (albite)' without the stoichiometric coefficient 3 required to balance 3Na+ and Si/Al.

### `gobelinite` (Gobelinite, `IMA:2018-167`)
- Section 4 text (p. 639) states that 'A total of 10 points on two crystals were analysed' for Cap Garonne gobelinite, whereas the Table 1 caption (p. 640) states 'n = 9'.
- The Abstract (p. 637) lists the Cap Garonne WDS constituents as 'CuO 42.45, CoO 6.58, NiO 3.37, ZnO 3.14, SO3 22.12, H2Ocalc 22.62, total 100.30 wt %', omitting Al2O3 0.02 wt% from Table 1 (p. 640) while retaining the 100.30 wt% total.
- For the Eisenzecher Zug single-crystal X-ray refinement, the Abstract (p. 637) reports 'R1 = 0.0280 for 1998 unique reflections with Fo > 4sigma(Fo)', whereas Section 5.2 (p. 641) reports 'R1 = 0.0289 for 1998 Fo > 4sigma(Fo)'.
- In Section 5.2 (p. 640), the dimensions of the Eisenzecher Zug crystal fragment used for laboratory Nonius KappaCCD SCXRD are printed as '0.05 x 0.05 x 0.13 um' (a typographical unit error for mm).
- In Table 2 (p. 640), the six bolded strongest PXRD reflections include three lines with Iobs = 15 (013, 006, 008), while reflection -1 2 3 at dobs = 2.561 A also has Iobs = 15 but is not bolded.

### `zinkgruvanite` (Zinkgruvanite, `IMA:2020-031`)
- In the Abstract (p. 659), the eight strongest powder X-ray diffraction lines are printed as '3.508 (70; 103), 2.980(70; 114), 2.814 (68; 122), 2.777 (70; 121), 2.699 (714; 200), 2.680 (68; 201), 2.125 (100; 124, 204) and 2.107 (96; 221)', where '714' at 2.699 A is a typographical error for I = 71 in Table 4 (p. 665), and '68' at 2.680 A in the Abstract differs from I = 85 (Icalc = 74) at dobs = 2.6804 A in Table 4.
- In Table 6 (p. 667), both inversion-center octahedral sites M(1) Fe and M(3) Fe are printed with identical fractional coordinates x = 0, y = 1/2, z = 1/2, whereas the bond distances in Table 7 (p. 668) place M(1) at (0, 0, 1/2) and M(3) at (0, 1/2, 1/2).
- In Table 7 (p. 668), the third bond entry under octahedral site M(3) is printed as '-O(8) 2.250(3)' without the 'x 2' multiplicity symbol, and the mean Si(2)-O bond distance label is printed with a stray parenthesis as '< Si(2)-O(> 1.620'.
- Section 7.1.1 (p. 665) cites 'minor Na (0.03 apfu; Table 1)', whereas Table 1 (p. 662) contains reflectance values and chemical composition data are in Table 2 (p. 664).
- In Table 8 (p. 669), the assigned site population for [6]M(2) has Mg0.11 (giving an O-sheet sum of 4.00 apfu) and [4]S has S1.62 + Si0.32 + P0.07, whereas the empirical formula in the Abstract (p. 659) and Section 5 (p. 663) has Mg0.14 (sum = 4.03) and S1.61Si0.32P0.07 (sum = 1.99).
- In Table 2 (p. 664), the printed Total for Crystal no. 1 is 98.93 wt% vs an exact sum of rounded constituents (using FeO 7.53 + Fe2O3 11.56) of 98.91 wt%, and for Crystal no. 2 is 98.79 wt% vs an exact sum of rounded constituents of 98.75 wt%.

## Preserved Frontier Queue

- `asgruvanite-(ce) (IMA:2025-004, Ce16Ca5Al(SiO4)6(AsO3)8(CO3)2Cl4F3(OH)2, European Journal of Mineralogy 37 (2025), 937, IMA Master List PDF p. 16)`
- `tomsquarryite (IMA:2022-018, NaMgAl3(PO4)2(OH)6(H2O)8, European Journal of Mineralogy 34 (2022), 375, IMA Master List PDF p. 219)`
- `whiteite-(camnfe) (IMA:2022-072, CaMnFe2Al2(PO4)4(OH)2(H2O)8, European Journal of Mineralogy 35 (2023), 95, IMA Master List PDF p. 234)`
- `zvestovite-(fe) (IMA:2022-092, Ag6(Ag4Fe2)As4S13, European Journal of Mineralogy 36 (2024), 529, IMA Master List PDF p. 243)`
- `cerromojonite (IMA:2018-040, CuPbBiSe3, European Journal of Mineralogy 30 (2018), 1165, IMA Master List PDF p. 41)`
- `espadaite (IMA:2018-089, Na4Ca3Mg2[As5+7As3+3O28](H2O)22, European Journal of Mineralogy 31 (2019), 847, IMA Master List PDF p. 66)`
- `ferriperbøeite-(La) (IMA:2018-106, CaLa3(Fe3+Al2Fe2+)[Si2O7][SiO4]3O(OH)2, European Journal of Mineralogy 32 (2020), 117, IMA Master List PDF p. 69)`
- `ferroefremovaite (IMA:2020-099, (NH4)2Fe2+2Fe3+(SO4)4, European Journal of Mineralogy 33 (2021), 591, IMA Master List PDF p. 71)`
- `freitalite (IMA:2019-116, C14H10, European Journal of Mineralogy 33 (2021), 1, IMA Master List PDF p. 78)`
- `grammatikopoulosite (IMA:2019-090, NiVP, European Journal of Mineralogy 32 (2020), 543, IMA Master List PDF p. 85)`
- `heftetjernite (IMA:2006-056, ScTaO4, European Journal of Mineralogy 22 (2010), 309, IMA Master List PDF p. 91)`
- `tillmannsite (IMA:2001-010, HgAg3(VO4), European Journal of Mineralogy 15 (2003), 177, IMA Master List PDF p. 219)`
- `spanoite (IMA:2025-086, Tl2[(UO2)2(V2O8)], CNMNC Newsletter 89 + European Journal of Mineralogy 38 (2026), 117)`
- `zhaoyuanite (IMA:2026-006, MnZnTe4+4O10, CNMNC Newsletter 92 + European Journal of Mineralogy 38 (2026), 491)`
- `tianhongqiite (IMA:2021-006b, CrTiO3(OH), CNMNC Newsletter 68 + European Journal of Mineralogy 34 (2022), 385)`
- `kidodite (IMA:2025-043, BaMg2Fe16O27, CNMNC Newsletter 88 + European Journal of Mineralogy 37 (2025), 921)`
- `monteneroite (IMA:2020-028, Cu2+Mn2+2(AsO4)2(H2O)2, Mineralogical Magazine 85 (2021), 255, IMA Master List PDF p. 147; previously mislisted under EJM in round131 queue)`
- `paradimorphite (IMA:2020-101, As4S3, Mineralogical Magazine 86 (2022), 83, IMA Master List PDF p. 164; previously mislisted under EJM in round131 queue)`
- `pilawite-(y) (IMA:2013-125, Ca2Y2Al4(SiO4)4O2(OH)2, Mineralogical Magazine 79 (2015), 1143, IMA Master List PDF p. 173; previously mislisted under EJM in round131 queue)`
- `stibiosegnitite (IMA:2024-065, Pb(Fe3+2.5Sb5+0.5)(AsO4)(AsO3OH)(OH)6, Mineralogical Magazine 89 (2025), 399, IMA Master List PDF p. 206; previously mislisted under EJM in round131 queue)`
- `zincochenite (IMA:2022-025, Pb4Zn(OH)6(SO4)2, Canadian Journal of Mineralogy and Petrology 61 (2023), 1075, IMA Master List PDF p. 241; previously mislisted under EJM in round131 queue)`
