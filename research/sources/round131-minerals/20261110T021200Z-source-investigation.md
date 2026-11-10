# CMMMech Round 131 Source Investigation Dossier (`20261110T021200Z`)

- **Investigation ID**: `cmmmech-round131-source-investigation-20261110T021200Z`
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 13, Stage 1 (`add_records`)
- **Corpus Transition**: `703 -> 708` records (`+5`), `1510 -> 1515` canonical history sidecars (`+5` `CREATE`), `1244 -> 1249` structured review bundles (`+5`)
- **Primary Authority Catalog**: `IMA_Master_List_(2026-09).pdf` (`3,129,886` B, SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`, pages 55, 91, 106, 136, 151)
- **Bounded Passage Indexing**: 5 open-access *European Journal of Mineralogy* PDFs (`61` full-PDF pages / `52` main-text pages, `170` total passages / `134` main-text passages `<= 1,799` B each, `244,729` passage bytes, plus `28` single-page 150-DPI PNG renders)

## Curated Records and Primary Sources

| Slug | IMA ID | Formula | Critical Elements | Primary DOI | Record SHA-256 | History Sidecar |
|---|---|---|---|---|---|---|
| `heimaeyite` | `IMA:2023-127a` | `Na3Al(SO4)3 (also written Na3AlS3O12 in Section 3, p. 81)` | Al | https://doi.org/10.5194/ejm-37-79-2025 | `c9d3ff564edd8a35...` | `history/records/heimaeyite/2026-11-10T015229Z-antigravity-36f503.yaml` |
| `delchiaroite` | `IMA:2025-076` | `Cu3I(CH3S)2` | Cu | https://doi.org/10.5194/ejm-38-153-2026 | `14e12fd32e237ab0...` | `history/records/delchiaroite/2026-11-10T015231Z-antigravity-3d1e6e.yaml` |
| `marioantofilliite` | `IMA:2025-012` | `[Cu4Al2(OH)12](CO3)(H2O)3 ([Cu4Al2(OH)12](CO3)*3H2O in primary paper)` | Cu, Al, Zn | https://doi.org/10.5194/ejm-37-733-2025 | `15bfcf39a0edb18b...` | `history/records/marioantofilliite/2026-11-10T015232Z-antigravity-6dbb10.yaml` |
| `jonlarsenite` | `IMA:2024-078a` | `Al4Cu9` | Al, Cu | https://doi.org/10.5194/ejm-37-783-2025 | `45de05cd8368cbaa...` | `history/records/jonlarsenite/2026-11-10T021137Z-antigravity-5741ff.yaml` |
| `nannoniite` | `IMA:2024-010` | `Al2(OH)5F` | Al, F, Mg | https://doi.org/10.5194/ejm-36-1011-2024 | `0df1c6a5bf7d5883...` | `history/records/nannoniite/2026-11-10T021139Z-antigravity-b2f891.yaml` |

## Documented Primary-Source Discrepancies

### `heimaeyite` (Heimaeyite, `IMA:2023-127a`)
- Three different calculated density values appear across the primary paper: 2.783 g cm-3 in the Abstract (p. 79) and Section 2 (p. 80, from empirical chemical analysis and SCXRD unit-cell dimensions), 2.747 g cm-3 in Section 2 (p. 80, from crystal structure analysis results), and 2.7411 in Table 3 (p. 84, where the row header prints a typographical unit error 'Calculated density (g cm-1)' instead of 'g cm-3').
- Table 1 (p. 80) prints Total = 92.89 wt%, whereas the exact arithmetic sum of the eight rounded mean wt% values (4.18 + 0.43 + 0.98 + 56.72 + 0.10 + 10.10 + 1.00 + 19.39) is 92.90 wt%.
- The Abstract (p. 79) describes the streak of natural Fe-bearing heimaeyite as 'yellowish streak', whereas Section 2 (p. 80) states 'The streak is yellow' (and white for pure synthetic Na3Al(SO4)3).
- Section 4.1 (p. 81) reports multiphase PXRD weight fractions of 41 wt% heimaeyite, 18 wt% tamarugite, 15 wt% koryakite, 11 wt% langbeinite, 9 wt% EA, and 7 wt% hexahydrite, whose rounded integer values sum to 101 wt%.
- Section 6 (p. 87) prints the reagent aluminium sulfate hydrate formula as 'Al3(SO4)2(H2O)17' (transposing the Al and SO4 subscripts of Al2(SO4)3*17H2O).

### `delchiaroite` (Delchiaroite, `IMA:2025-076`)
- The Abstract (p. 153) reports 'The calculated density is 3.702 g cm-3', whereas Section 2 (p. 155) explains that 3.702 g cm-3 is calculated from the empirical formula and SCXRD unit-cell volume and 3.705 g cm-3 is calculated from the ideal formula Cu3I(CH3S)2.
- Table 5 (p. 158) prints the three Cu(1)-S(2) bond lengths as 2.283(3), 2.340(2) (x 2), and the Cu(1)-I bond length as 2.8639(13) A, with an arithmetic average of (2.283 + 2.340 + 2.340 + 2.8639)/4 = 2.4567 A, whereas the table row prints Average = 2.529 A.
- Section 4.1 (p. 157) prints 'three sharper features at 2911, 2989, and 3001 cm-1' in the C-H stretching region, whereas Figure 4b (p. 157) labels the peak as 2912 cm-1.

### `marioantofilliite` (Marioantofilliite, `IMA:2025-012`)
- The September 2026 IMA Master List (PDF p. 136) writes the formula as [Cu4Al2(OH)12](CO3)(H2O)3, whereas Biagioni et al. (2025) write [Cu4Al2(OH)12](CO3)*3H2O.
- The Abstract (p. 733) prints the empirical formula with Cu3.99 and Al1.85 ('[(Cu3.99Zn0.04)Sigma4.03Al1.85(OH)11.62]...') whereas Section 4.3 (p. 737) prints Cu3.99 and Al1.85 in the first formula and then writes 'Considering the sum of M2+ and M3+ cations as equal to 6 apfu, the empirical formula of marioantofilliite can thus be written (with rounding errors) as [(Cu4.08Zn0.04)Sigma4.12Al1.88(OH)12][(CO3)0.90(SiO3(OH))0.03(SO4)0.01(PO4)0.01Cl0.01(OH)0.01]*3H2O' with a two-step normalization.
- Section 2 (p. 734) reports two calculated densities: 2.550 g cm-3 from the empirical formula and SCXRD unit-cell volume, and 2.591 g cm-3 from the ideal formula (which appears rounded as 2.59 g cm-3 in Table 7, p. 742).

### `jonlarsenite` (Jonlarsenite, `IMA:2024-078a`)
- Table 2 (p. 789) caption prints 'Atoms, Wyckoff letter, and fractional atom coordinates (A) for synthetic Al4Cu9 (Arnberg and Westman, 1978)', appending the unit '(A)' even though the tabulated coordinates x, y, z are dimensionless fractional coordinates.
- Table 3 (p. 789) caption states 'Calculated X-ray powder diffraction data for jonlarsenite (Icalc > 3)', but includes reflection 332 (d = 1.8548 A) with Icalc = 3.

### `nannoniite` (Nannoniite, `IMA:2024-010`)
- Under shortwave UV radiation (lambda = 254 nm), the Abstract (p. 1011) describes the fluorescence of nannoniite as 'bluish-yellow', whereas Section 2 (pp. 1012-1013) and Section 4.4.2 (p. 1020) describe it as 'bluish-white' (matching Jambor et al., 1990 for UM1990-28-OHF:Al).
- Three sets of monoclinic unit-cell parameters are reported across the study: 3DED (PETS2, Table 3, p. 1016) a = 8.688(3), b = 5.024(2), c = 9.734(4) A, beta = 90.77(2) deg, V = 424.9(3) A3 (rounded in Table 8, p. 1019, to 8.69, 5.02, 9.73 A, 90.8 deg, 424.9 A3); Gandolfi-like PXRD (Section 3.3, p. 1013) a = 8.680(3), b = 5.018(4), c = 9.711(4) A, beta = 90.26(9) deg, V = 423.0(4) A3; and weak SCXRD (Section 3.3, p. 1013) a = 8.672(7), b = 5.009(4), c = 9.673(8) A, beta = 90.50(3) deg, V = 420.2(6) A3.

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
