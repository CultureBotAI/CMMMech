# CMMMech Round 131 Source Investigation Dossier (`20261110T021200Z`)

- **Investigation ID**: `cmmmech-round131-source-investigation-20261110T021200Z`
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 13, Stage 1 (`add_records`)
- **Corpus Transition**: `703 -> 708` records (`+5`), `1510 -> 1519` canonical history sidecars (`+5` `CREATE`, `+4` `EDIT`), `1244 -> 1254` structured review bundles (`+5` initial, `+5` post-remediation)
- **Primary Authority Catalog**: `IMA_Master_List_(2026-09).pdf` (`3,129,886` B, SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`, pages 55, 91, 106, 136, 151)
- **Bounded Passage Indexing**: 5 open-access *European Journal of Mineralogy* PDFs (`61` full-PDF pages / `52` main-text pages, `170` total passages / `134` main-text passages `<= 1,799` B each, `244,729` passage bytes, plus `28` single-page 150-DPI PNG renders)

## Curated Records and Primary Sources

| Slug | IMA ID | IMA Symbol | Formula | Critical Elements | Primary DOI | Record SHA-256 | Latest History Sidecar |
|---|---|---|---|---|---|---|---|
| `heimaeyite` | `IMA:2023-127a` | none | `Na3Al(SO4)3 (also written Na3AlS3O12 in Section 3, p. 81)` | Al | https://doi.org/10.5194/ejm-37-79-2025 | `b654bf22f87bcb03...` | `history/records/heimaeyite/2026-11-10T034829Z-antigravity-1ce5eb.yaml` |
| `delchiaroite` | `IMA:2025-076` | `Dch` | `Cu3I(CH3S)2` | Cu | https://doi.org/10.5194/ejm-38-153-2026 | `4d8c2370a39ddb7f...` | `history/records/delchiaroite/2026-11-10T034831Z-antigravity-07c2a2.yaml` |
| `marioantofilliite` | `IMA:2025-012` | `Maf` | `[Cu4Al2(OH)12](CO3)(H2O)3 ([Cu4Al2(OH)12](CO3)*3H2O in primary paper)` | Cu, Al, Mg, Si | https://doi.org/10.5194/ejm-37-733-2025 | `65bfcba42fee181f...` | `history/records/marioantofilliite/2026-11-10T034833Z-antigravity-451ae9.yaml` |
| `jonlarsenite` | `IMA:2024-078a` | none | `Al4Cu9` | Al, Cu | https://doi.org/10.5194/ejm-37-783-2025 | `45de05cd8368cbaa...` | `history/records/jonlarsenite/2026-11-10T021137Z-antigravity-5741ff.yaml` |
| `nannoniite` | `IMA:2024-010` | `Nnn` | `Al2(OH)5F` | Al, F, Mg | https://doi.org/10.5194/ejm-36-1011-2024 | `14baa8383feacad8...` | `history/records/nannoniite/2026-11-10T034835Z-antigravity-32840c.yaml` |

## Documented Primary-Source Discrepancies

### `heimaeyite` (Heimaeyite, `IMA:2023-127a`)
- Three different calculated density values appear across the primary paper: 2.783 g cm-3 in the Abstract (p. 79) and Section 2 (p. 80, from empirical chemical analysis and SCXRD unit-cell dimensions), 2.747 g cm-3 in Section 2 (p. 80, from crystal structure analysis results), and 2.7411 in Table 3 (p. 84, where the row header prints a typographical unit error 'Calculated density (g cm-1)' instead of 'g cm-3').
- Table 1 (p. 80) prints Total = 92.89 wt%, whereas the exact arithmetic sum of the eight rounded mean wt% values (4.18 + 0.43 + 0.98 + 56.72 + 0.10 + 10.10 + 1.00 + 19.39) is 92.90 wt%.
- The Abstract (p. 79) describes the streak of natural Fe-bearing heimaeyite as 'yellowish streak', whereas Section 2 (p. 80) states 'The streak is yellow' (and white for pure synthetic Na3Al(SO4)3).
- Section 4.1 (p. 81) reports multiphase PXRD weight fractions of 41 wt% heimaeyite, 18 wt% tamarugite, 15 wt% koryakite, 11 wt% langbeinite, 9 wt% EA, and 7 wt% hexahydrite, whose rounded integer values sum to 101 wt%.
- Section 6 (p. 87) prints the reagent aluminium sulfate hydrate formula as 'Al3(SO4)2(H2O)17' (transposing the Al and SO4 subscripts of Al2(SO4)3*17H2O).
- Table 2 (p. 82) footnote states '* The intensities of the eight strongest maxima are in bold', whereas only seven Imeas values (40, 17, 32, 100, 55, 10 at 2.72 A, and 11) are typeset in bold and the tied eighth at 2.026 A (Imeas = 10) is typeset in regular font.

### `delchiaroite` (Delchiaroite, `IMA:2025-076`)
- Section 1 (p. 154) designates two cotype specimens (Museo di Storia Naturale of the University of Pisa catalogue no. 20083 and National Museum Prague catalogue no. P1P 29/2025), whereas the Figure 2 caption (p. 155) refers to MSNP catalogue no. 20083 as 'Holotype specimen'.
- In Table 1 (p. 155, reflectance values measured in air from 400 to 700 nm), at 400 nm the column labelled Rmax is 18.5% while Rmin is 18.8%, crossing over at 420 nm where both equal 19.7%.
- In Table 7 (p. 160, powder X-ray diffraction data), for the four consecutive rows dobs = 2.362, 2.310, 2.289, and 2.222 A, the dcalc and Icalc columns are transposed (printing 13 under dcalc and 2.363 under Icalc for the bold dobs = 2.362 A reflection).

### `marioantofilliite` (Marioantofilliite, `IMA:2025-012`)
- The September 2026 IMA Master List (PDF p. 136) writes the formula as [Cu4Al2(OH)12](CO3)(H2O)3, whereas Biagioni et al. (2025) write [Cu4Al2(OH)12](CO3)*3H2O.
- Section 7.4 (p. 741) prints the 6-cation recalculation 'with rounding errors' as [(Cu3.72Al2.28)(OH)12](CO3)1.10*3.06H2O, whereas 6 x [(Cu0.613Al0.387)(OH)2](CO3)0.194*0.486H2O equals [(Cu3.68Al2.32)(OH)12](CO3)1.16*2.92H2O.
- Section 7.2 and Table 5 (p. 740) report the interlayer carbonate C-O(1i) distance as 1.28(6) A, whereas Section 7.3 (p. 741) prints 1.28(2) A.

### `jonlarsenite` (Jonlarsenite, `IMA:2024-078a`)
- Table 2 (p. 789) caption prints 'Atoms, Wyckoff letter, and fractional atom coordinates (A) for synthetic Al4Cu9 (Arnberg and Westman, 1978)', appending the unit '(A)' even though the tabulated coordinates x, y, z are dimensionless fractional coordinates.
- Table 3 (p. 789) caption states 'Calculated X-ray powder diffraction data for jonlarsenite (Icalc > 3)', but includes reflection 332 (d = 1.8548 A) with Icalc = 3.

### `nannoniite` (Nannoniite, `IMA:2024-010`)
- Under shortwave UV radiation (lambda = 254 nm), the Abstract (p. 1011) describes the fluorescence of nannoniite as 'bluish-yellow', whereas Section 2 (pp. 1012-1013) and Section 4.4.2 (p. 1020) describe it as 'bluish-white' (matching Jambor et al., 1990 for UM1990-28-OHF:Al).
- Three sets of monoclinic unit-cell parameters are reported across the study: 3DED (PETS2, Table 3, p. 1016) a = 8.688(3), b = 5.024(2), c = 9.734(4) A, beta = 90.77(2) deg, V = 424.9(3) A3 (rounded in Table 8, p. 1019, to 8.69, 5.02, 9.73 A, 90.8 deg, 424.9 A3); Gandolfi-like PXRD (Section 3.3, p. 1013) a = 8.680(3), b = 5.018(4), c = 9.711(4) A, beta = 90.26(9) deg, V = 423.0(4) A3; and weak SCXRD (Section 3.3, p. 1013) a = 8.672(7), b = 5.009(4), c = 9.673(8) A, beta = 90.50(3) deg, V = 420.2(6) A3.
- Section 4.5 (p. 1020) prints the formula of associated dacostaite (IMA 2024-015) as K(Mg2Al)[Mg(H2O)6](AsO4)2F6*2H2O, omitting the subscript 2 on [Mg(H2O)6]2 relative to its charge-balanced ideal formula K(Mg2Al)[Mg(H2O)6]2(AsO4)2F6*2H2O.

## Preserved Frontier Queue

- `monteneroite (IMA:2020-028, Cu2+Mn2+2(AsO4)2(H2O)2, European Journal of Mineralogy 32 (2020), 413)`
- `paradimorphite (IMA:2020-101, As4S3, European Journal of Mineralogy 34 (2022), 75)`
- `pilawite-(y) (IMA:2014-075, Ca2Y2Al4(SiO4)4O2(OH)2, European Journal of Mineralogy 35 (2023), 429)`
- `stibiosegnitite (IMA:2025-024, Pb(Fe3+2.5Sb5+0.5)(AsO4)(AsO3OH)(OH)6, European Journal of Mineralogy 37 (2025), 559)`
- `zincochenite (IMA:2022-063, Pb4Zn(OH)6(SO4)2, European Journal of Mineralogy 35 (2023), 253)`
- `zinkgruvanite (IMA:2020-031, Ba4Mn2+4Fe3+2(Si2O7)2(SO4)2O2(OH)2, European Journal of Mineralogy 33 (2021), 383)`
- `heftetjernite (IMA:2006-056, ScTaO4, European Journal of Mineralogy 22 (2010), 309)`
- `tillmannsite (IMA:2001-010, HgAg3(VO4), European Journal of Mineralogy 15 (2003), 177)`
- `spanoite (IMA:2025-086, Tl2[(UO2)2(V2O8)], CNMNC Newsletter 89 + European Journal of Mineralogy 38 (2026), 117)`
- `zhaoyuanite (IMA:2026-006, MnZnTe4+4O10, CNMNC Newsletter 92 + European Journal of Mineralogy 38 (2026), 491)`
- `tianhongqiite (IMA:2021-006b, CrTiO3(OH), CNMNC Newsletter 68 + European Journal of Mineralogy 34 (2022), 385)`
- `kidodite (IMA:2025-043, BaMg2Fe16O27, CNMNC Newsletter 88 + European Journal of Mineralogy 37 (2025), 921)`
- `bonacinaite (IMA:2018-056, multi-reference: Mineralogical Magazine 84 (2020), 568; European Journal of Mineralogy 36 (2024), 863)`
- `carletonmooreite (IMA:2018-068)`
- `changesite-y (IMA:2022-023)`
- `chihmingite (IMA:2022-010)`
- `ferroberaunite (IMA:2021-036)`
- `gysinite-la (IMA:2022-008)`
- `haleniusite-ce (IMA:2003-028)`
- `ikranite (IMA:2000-010)`
