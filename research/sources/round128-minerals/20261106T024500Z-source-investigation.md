# Round 128 Source Investigation Dossier (`20261106T024500Z`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 10, Stage 1 (`add_records`)
- **Timestamp (UTC)**: `2026-11-06T02:45:00Z`
- **Corpus Progression**: `688 -> 693` records (`+5`), `1374 -> 1379` history sidecars (`+5` `CREATE`), `1100 -> 1105` structured reviews (`+5`)

## 1. Bounded Frontier Search & Citation Verification Protocol

We inspected the five open-access *European Journal of Mineralogy* single-reference critical-element mineral candidates preserved in Round 127's frontier queue (`pilanesbergite`, `luxembourgite`, `tancaite-ce`, `argentotennantite-fe`, and `badengzhuite`) against the September 2026 IMA-CNMNC Master List of Minerals (`IMA_Master_List_(2026-09).pdf`, pages 13, 19, 129, 173, and 211). All five primary PDFs were downloaded from *European Journal of Mineralogy* (`https://doi.org/10.5194/ejm-...`), segmented into `168` bounded text passages (`<= 1,800` bytes per file across `58` full-PDF pages / `48` main-text pages) via `scripts/index_bounded_pdf_passages.py`, and accompanied by `10` single-page `150`-DPI PNG table renders (`mutool draw -q -r 150`). We also identified five additional uncurated single-reference *European Journal of Mineralogy* critical-element mineral candidates (`zhiqinite`, `bonacinaite`, `belmonteite`, `dacostaite`, and `fluormacraeite`) to preserve in the Round 129 frontier queue alongside the seven non-EJM single-reference candidates from Round 125.

## 2. Primary PDFs Inspected (`58` Pages, `168` Passages, `10` Table PNGs)

| Mineral (`id`) | IMA ID (Symbol) | Primary Source (EJM) | PDF Size (Bytes) | PDF SHA-256 | Pages (Main) | Passages (Main) | Table PNGs Inspected |
| :--- | :--- | :--- | ---: | :--- | ---: | ---: | :--- |
| **Pilanesbergite** (`cmmmech:pilanesbergite`) | `IMA:2023-007` (`Pbg`) | Dal Bo et al. (2024) *Eur. J. Mineral.* 36:73–85 | `7,670,062` | `3f2036c96dbfed8feccd8e65b5156318bf673b420db0e6d7b42b1f2ee29a307e` | `13 (11)` | `34 (27)` | `ejm-36-73-2024-p5.png`, `ejm-36-73-2024-p8.png` |
| **Luxembourgite** (`cmmmech:luxembourgite`) | `IMA:2018-154` (`Lux`) | Philippo et al. (2020) *Eur. J. Mineral.* 32:449–455 | `4,191,535` | `9e9072c491874e921834315615b67a2305bc57de8137e7c64e08eeb169200254` | `7 (6)` | `20 (17)` | `ejm-32-449-2020-p2.png`, `ejm-32-449-2020-p4.png` |
| **Tancaite-(Ce)** (`cmmmech:tancaite-ce`) | `IMA:2009-097` (`Tnc-Ce`) | Bonaccorsi & Orlandi (2020) *Eur. J. Mineral.* 32:347–354 | `3,862,974` | `091d52e1bf40a05f4dcd4bdad01c840326a8efae576b8c94a59cae35bd0a50b5` | `8 (7)` | `22 (19)` | `ejm-32-347-2020-p2.png`, `ejm-32-347-2020-p6.png` |
| **Argentotennantite-(Fe)** (`cmmmech:argentotennantite-fe`) | `IMA:2023-126` (`Atnt-Fe`) | Sejkora et al. (2026) *Eur. J. Mineral.* 38:325–336 | `5,761,488` | `485ca19fac5d85b2f7d1eebbf7ca5f6542d0d43938a891c7fac53ef0f7de8ee8` | `12 (10)` | `35 (29)` | `ejm-38-325-2026-p5.png`, `ejm-38-325-2026-p6.png` |
| **Badengzhuite** (`cmmmech:badengzhuite`) | `IMA:2019-076` (`Bdz`) | Xiong et al. (2020) *Eur. J. Mineral.* 32:557–574 | `13,146,556` | `12c366bf1f944d91336b55b5f790c5e19038c7f4b33d5b0c2a1d958f5461c86c` | `18 (14)` | `57 (43)` | `ejm-32-557-2020-p7.png`, `ejm-32-557-2020-p10.png` |

## 3. Curated Records & Canonical `CREATE` History Sidecars

| Record Path | Bytes | Record SHA-256 | History Sidecar Path | Bytes | Sidecar SHA-256 |
| :--- | ---: | :--- | :--- | ---: | :--- |
| `data/records/pilanesbergite.yaml` | `6,839` | `9dd912aa9464c6064c17acd326af1a34572ebb99857d4266f4eca53a0d4c620b` | `history/records/pilanesbergite/2026-11-06T024318Z-antigravity-7389b1.yaml` | `1,008` | `4fbc7ddfb4dad89ec6f99b2da5862d8920661a839d7533f4cd013e624362b26d` |
| `data/records/luxembourgite.yaml` | `5,966` | `025aa43b48e777f0d30e9e8f4e88e88054bbaeaa835cf91877e60bbd9bdf0646` | `history/records/luxembourgite/2026-11-06T024320Z-antigravity-583019.yaml` | `1,008` | `5dd20a298c1980a114416cdd491d22925f035b7298d74e9462e7b1dab1034e9c` |
| `data/records/tancaite-ce.yaml` | `5,911` | `d1dbec31c0288a209372b342a339c0ed9a063d5756b33e8debe48621bd8f17e2` | `history/records/tancaite-ce/2026-11-06T024322Z-antigravity-f716a6.yaml` | `1,009` | `45cd0b2b8629e7cfd5cdf3368d0dfcbc1110d235d9b5d5bb96c6f8fde33dd1cd` |
| `data/records/argentotennantite-fe.yaml` | `6,170` | `f916d62155c5f593cc96f4cd99a5bc2c723b328d371d93326d282837d2c87c47` | `history/records/argentotennantite-fe/2026-11-06T024323Z-antigravity-e20b4d.yaml` | `1,036` | `f1d707c4b8ea562ee0548c10f7f1c23e8aad1d6c3cef15c8f3f38476550e8cf7` |
| `data/records/badengzhuite.yaml` | `5,624` | `6ff8b0742c4f3406ff54057167349025a28ebc2752aa63fa05b4d0197fa94704` | `history/records/badengzhuite/2026-11-06T024325Z-antigravity-9d7fae.yaml` | `1,000` | `afe1e64d6ff7917e48725a24fdf8eaadd1fe5e8c0bcc6a7f9efd1ddeeeeadd75` |

## 4. Documented Primary-Source Arithmetic & Typographical Discrepancies

1. **`pilanesbergite`** (Dal Bo et al. 2024):
   - Figure 2 (p. 76) uses the mineral symbol `Pbt` for pilanesbergite, whereas the September 2026 IMA-CNMNC Master List (p. 173) assigns `Pbg`.
   - Table 1 (p. 77) prints the EPMA mean oxide/halogen total (`n = 15` points on 7 grains) as `102.13 wt%` and `99.80 wt%` after `-O=F` (`2.33 wt%`), whereas the arithmetic sum of the 14 printed mean constituent values is `102.15 wt%` and `99.82 wt%` after `-O=F`.
   - Section 6.1 (p. 77) refers to the anionic sites as `"The W1 (O4) and W2 (F) sites"`, whereas Tables 4 (p. 80) and 7 (p. 81) identify `W1` as `O8 (W1)`.
   - Table 4 (p. 80) prints `Ueq` for site `X3 (Fe)` as `0.349(4)` Å², a decimal-place typographical error relative to `X1 (Ti) = 0.00650(5)`, `X2 (Ca) = 0.00926(7)`, and `X4 (Na) = 0.0120(1)` Å².
2. **`luxembourgite`** (Philippo et al. 2020):
   - Section 4 (p. 450) prints the ideal composition of `AgCuPbBi4Se8` as `Ag 5.58, Cu 3.44, Pb 11.22, Bi 45.28, and Se 34.22 for a total of 100.00 wt %`, where `Ag 5.58 wt%` is a digit transposition of the true stoichiometric value `5.84 wt%` (`107.8682 / 1846.3038 = 5.8424%`), causing the five printed ideal values to sum to `99.74 wt%`.
   - Calculated density is reported as `8.00 g cm-3` in the Abstract (p. 449), Section 3 (p. 450), and Table 6 (p. 454) from the chemical analysis and unit-cell parameters, whereas Table 3 (p. 452) reports `Dcalc = 7.397 g cm-3`.
   - Section 6 (p. 454) writes `(average M-O bond lengths = 2.544 A in luxembourgite and 2.730 A in litochlebite)`, misprinting `M-O` for `M-Se` in an oxygen-free selenide.
3. **`tancaite-ce`** (Bonaccorsi & Orlandi 2020):
   - The Abstract (p. 347) reports `R1 = 0.038 for 192 unique reflections with I > 2sigma(I)`, whereas Section 5 (p. 350) writes `R1 = 0.038 for 200 unique reflections` and Table 4 (p. 352) reports `200` total independent reflections with `Final R indices [I > 2sigma(I)]: R1 = 0.0387, wR2 = 0.0792` and `R indices (all data): R1 = 0.0424, wR2 = 0.0815`.
   - The Table 4 caption (p. 352) states that the third column lists the trigonal `R-3` unit cell `"as refined on the basis of X-ray powder diffraction data"`, whereas the values printed in that column (`a = 19.2901(3), c = 47.2510(5) A, V = 15226.9(7) A3`) are the single-crystal Bruker SMART BREEZE unit-cell parameters from Section 4 (p. 349), while the powder-diffraction refined `R-3` cell in Section 4 and Table 3 (p. 350) is `a = 19.305(1), c = 47.438(5) A, V = 15311(3) A3`.
   - Calculated density is reported as `3.834 g cm-3` from the empirical formula (Abstract and Section 2, p. 348) vs `3.738 Mg m-3` (`g cm-3`) from the ideal formula `CeFe(MoO4)3·3H2O` in Table 4 (p. 352).
4. **`argentotennantite-fe`** (Sejkora et al. 2026):
   - Section 4.1 (p. 329) reports the ideal composition of `Ag6(Cu4Fe2)As4S13` as `Cu 14.70, Ag 37.42, Fe 6.46, As 17.33, S 24.10, and total 100.00` wt%, where the five rounded constituent values sum to `100.01 wt%`.
   - Section 4.2 (p. 332) states `"The tetrahedrally coordinated M(1) site has an average <M(1)–S> bond distance of 2.329 A"`, whereas Table 5 (p. 330) and Table 8 (p. 333) report `M(1)–S(1) x 4 = 2.328(3) A`.
   - Section 3.2 (p. 329) states that calculated powder X-ray diffraction data were obtained with `PowderCell 2.3 (Kraus and Nolze, 1996)`, whereas the Table 7 caption (p. 331) cites `PowderCell 2.4 (Kraus and Nolze, 1996)`.
5. **`badengzhuite`** (Xiong et al. 2020):
   - The Abstract (p. 557) reports the 3D ED unit cell of badengzhuite as `a = 3.49(7) A, c = 11.70(23) A, V = 124(4) A3`, whereas Section 5.4 (p. 566) rounds `c` to `c = 11.7(2) A`.
   - Table 2 (p. 563) prints the average atomic percentages of the two EDX analyses (`426`: `P 50.17, Ti 49.83 at.%`; `427`: `P 47.86, Ti 52.14 at.%`) as `P 49.02` and `Ti 50.99 at.%` with `Sum 100`, where rounding both `49.015` and `50.985` upward yields an arithmetic sum of `100.01 at.%`.

## 5. Preserved Frontier Queue for Round 129

- **Open-Access EJM Single-Reference Candidates (`5`)**: `zhiqinite` (`IMA:2019-077`), `bonacinaite` (`IMA:2018-056`), `belmonteite` (`IMA:2024-040`), `dacostaite` (`IMA:2024-015`), and `fluormacraeite` (`IMA:2024-054`).
- **Preserved Non-EJM Single-Reference Candidates (`7`)**: `carletonmooreite` (`IMA:2018-068`), `changesite-y` (`IMA:2022-023`), `chihmingite` (`IMA:2022-010`), `ferroberaunite` (`IMA:2021-036`), `gysinite-la` (`IMA:2022-008`), `haleniusite-ce` (`IMA:2003-028`), and `ikranite` (`IMA:2000-010`).
