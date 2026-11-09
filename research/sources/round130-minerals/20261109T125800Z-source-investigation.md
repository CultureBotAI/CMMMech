# CMMMech Round 130 Source Investigation Dossier (`20261109T125800Z`)

- **Investigation ID**: `cmmmech-round130-source-investigation-20261109T125800Z`
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 12, Stage 1 (`add_records`)
- **Corpus Transition**: `698 -> 703` records (`+5`), `1464 -> 1469` canonical history sidecars (`+5`), `1191 -> 1196` structured review bundles (`+5`)
- **Primary Authority Catalog**: `IMA_Master_List_(2026-09).pdf` (`3,129,886` B, SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`, pages 91, 112, 203, 217, 240)
- **Bounded Passage Indexing**: 4 open-access *European Journal of Mineralogy* PDFs (`44` full-PDF pages / `38` main-text pages, `111` total passages / `96` main-text passages `<= 1,800` B each, `156,668` passage bytes, plus `17` single-page 150-DPI PNG renders)

## Curated Records and Primary Sources

| Slug | IMA ID | Formula | Critical Elements | Primary DOI | Record SHA-256 | History Sidecar |
|---|---|---|---|---|---|---|
| `spaltiite` | `IMA:2014-012` | `Tl2Cu2As2S5 (Cu2As2Tl2S5 in Table 4, p. 33)` | Tl, Cu, As, Ag, Sb | https://doi.org/10.5194/ejm-38-27-2026 | `475c18a22cf52cd4...` | `history/records/spaltiite/2026-11-09T125719Z-antigravity-f8757a.yaml` |
| `tianhuixinite` | `IMA:2022-081` | `(MoO3)3*H2O` | Mo | https://doi.org/10.5194/ejm-38-39-2026 | `db5456c3dbf09090...` | `history/records/tianhuixinite/2026-11-09T125721Z-antigravity-749d6b.yaml` |
| `zhenruite` | `IMA:2022-050` | `(MoO3)2(H2O) ((MoO3)2*H2O in primary paper)` | Mo | https://doi.org/10.5194/ejm-38-39-2026 | `769c42ebb798fb77...` | `history/records/zhenruite/2026-11-09T125723Z-antigravity-5c8750.yaml` |
| `keutschite` | `IMA:2014-038` | `Cu2AgAsS4` | Cu, Ag, As, Sb, Mn, Pb | https://doi.org/10.5194/ejm-38-1-2026 | `d69b9a8958bd17bb...` | `history/records/keutschite/2026-11-09T125724Z-antigravity-54d4a3.yaml` |
| `heimite` | `IMA:2022-019` | `PbCu2(AsO4)(OH)3(H2O)2 (PbCu2(AsO4)(OH)3*2H2O in primary paper)` | Cu, As, Pb | https://doi.org/10.5194/ejm-36-153-2024 | `e63c28ebd97b9d11...` | `history/records/heimite/2026-11-09T125726Z-antigravity-d17c84.yaml` |

## Documented Primary-Source Discrepancies

### `spaltiite` (Spaltiite, `IMA:2014-012`)
- The Abstract (p. 27) and Section 5 (p. 30) print the empirical formula on the basis of 11 apfu as Tl1.94Cu2.04Ag0.01As1.95Sb0.03S5.03 and Cu2.04Ag0.01Tl1.94As1.95Sb0.03S5.03, respectively, swapping the Tl = 1.95(1) and As = 1.94(1) apfu coefficients printed in Table 2 (p. 31; where 47.41 wt% Tl / 204.383 = 0.23197 and 17.36 wt% As / 74.9216 = 0.23171 confirm Tl1.95 and As1.94 apfu).
- Section 1 (p. 28) and the Figure 3b caption (p. 30) print the mineral symbol as Spti, whereas the Figure 3a caption (p. 30) prints Spli.
- Table 4 (p. 33) prints the row label 'R1(F): all, observed' alongside '12.18 %, 14.08 %', transposing the 'all' and 'observed' labels relative to the Abstract (p. 27), which confirms R1 = 12.18 % for the 4753 observed reflections with Fo > 4sigma(Fo).
- Section 4 (p. 30) prints the Vickers micro-indentation hardness units as 'kg mm2' ('with a mean of 47 kg mm2') instead of 'kg mm-2' (printed in the Abstract on p. 27).

### `tianhuixinite` (Tianhuixinite, `IMA:2022-081`)
- The Abstract (p. 39) and Section 2.2 (p. 41) report Dcalc = 4.131 g/cm3 (calculated from the empirical formula and powder XRD unit-cell volume V = 361.74(2) A3), whereas Table 3 (p. 47) reports rho_cal = 4.11 g/cm3 from the single-crystal XRD unit-cell volume V = 361.88(9) A3 with Z = 2.
- Table 1 (p. 41) reports H2O* = 4.04 wt% with footnote '* Added in ideal value' (giving Total = 100.85 wt% with MoO3 = 96.81 wt%), whereas Section 2.2 (p. 42) states that ideal (MoO3)3*H2O requires MoO3 96.00 wt% and H2O 4.00 wt% (4.04 wt% is the stoichiometric H2O scaled to the measured 96.81 wt% MoO3).

### `zhenruite` (Zhenruite, `IMA:2022-050`)
- The September 2026 IMA Master List (PDF p. 240) formats the ideal formula as (MoO3)2(H2O), whereas Gu et al. (2026) write (MoO3)2*H2O.
- Table 3 (p. 47) prints Z = 2 for natural zhenruite ((MoO3)2*H2O, V = 248.89(2) A3) alongside Z = 4 under the same header '(MoO3)2*H2O' for synthetic zhenruite from Benard et al. (1994, V = 248.4 A3), where Z = 4 corresponds to the hemihydrate formula unit MoO3*1/2H2O rather than (MoO3)2*H2O.

### `keutschite` (Keutschite, `IMA:2014-038`)
- The Abstract (p. 1) reports the axial ratio for a = 5.5834(15), c = 10.021(3) A as 'a : b : c = 1 : 1 : 0.897', which equals c/(2a) = 0.8974 rather than c/a = 1.7948.
- Section 3 (p. 3) prints the empirical formula 'calculated on the basis of eight atoms' as Cu2.05Ag0.96(As0.95Sb0.04)Sigma0.99S4.00 (printing Cu2.05 instead of Cu1.99 on the 4 S apfu basis), whereas the Abstract (p. 1) prints Cu2.00Ag0.97(As0.95Sb0.04)Sigma0.99S4.03 on 8 apfu.
- Table 2 (p. 4) footnote prints the (As + Sb) site sums as (As0.95Sb0.04)Sigma1.99 (for both 8 apfu and 4 S apfu) and (As0.96Sb0.04)Sigma2.00 (for 4 Me apfu), printing Sigma1.99 instead of Sigma0.99 and Sigma2.00 instead of Sigma1.00.
- Section 3 (p. 3) prints a comma decimal separator in the ideal Ag weight percentage ('29.01 Cu, 24,62 Ag, 17.10 As, and 29.28 S, for a total of 100.00', where the four rounded values sum to 100.01 wt%).
- Section 4 (p. 3) prints the MoKalpha X-ray wavelength as 'lambda = 0.7173 A', omitting the zero present in 'lambda = 0.71073 A' on p. 4 and in Table 3.

### `heimite` (Heimite, `IMA:2022-019`)
- The September 2026 IMA Master List (PDF p. 91) formats the ideal formula as PbCu2(AsO4)(OH)3(H2O)2, whereas Malcherek et al. (2024) write PbCu2(AsO4)(OH)3*2H2O (and PbCu2(AsO4)(OH)3*2(H2O) in Section 4, p. 155, and Table 2, p. 157).
- The Abstract (p. 153) reports the unit-cell volume uncertainty as V = 780.33(8) A3, whereas Table 2 (p. 157) reports V = 780.33(11) A3 for both the monoclinic P21/n and orthorhombic Pnma refinements.
- The Abstract (p. 153) prints the empirical formula on the basis of 9 O apfu as Pb1.04Ca0.03Cu2.10As1.10H6.14O9, whereas Section 4 (p. 155) omits the trailing zeroes on Cu and As (Pb1.04Ca0.03Cu2.1As1.1H6.14O9) and also gives Pb0.97Ca0.02Cu1.95As1.02H7O9 when H is fixed at 7 apfu.

## Preserved Frontier Queue

- `heftetjernite (IMA:2006-056, ScTaO4, European Journal of Mineralogy 22 (2010), 309)`
- `heimaeyite (IMA:2023-127a, Na3Al(SO4)3, European Journal of Mineralogy 37 (2025), 79)`
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
