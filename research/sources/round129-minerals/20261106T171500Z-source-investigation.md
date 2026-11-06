# Round 129 Source Investigation Dossier (`20261106T171500Z`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 11, Stage 1 (`add_records`)
- **Timestamp (UTC)**: `2026-11-06T17:15:00Z`
- **Corpus Progression**: `693 -> 698` records (`+5`), `1414 -> 1419` history sidecars (`+5` `CREATE`), `1137 -> 1142` structured reviews (`+5`)

## 1. Bounded Frontier Search & Citation Verification Protocol

We inspected the open-access *European Journal of Mineralogy* single-reference critical-element mineral candidates preserved in Round 128's frontier queue against the September 2026 IMA-CNMNC Master List of Minerals (`IMA_Master_List_(2026-09).pdf`, pages 22, 27, 53, 72, 131, and 239). Upon checking the IMA Master List entry for `bonacinaite` (`IMA:2018-056`, page 27), we verified that it cites two primary references (`Mineralogical Magazine 84 (2020), 568` and `European Journal of Mineralogy 36 (2024), 863`) and therefore reclassified `bonacinaite` into the multi-reference queue, substituting single-reference paulkeitite-group congener `macraeite` (`IMA:2023-065`, page 131, *European Journal of Mineralogy* 36 (2024), 267–278) alongside `zhiqinite`, `belmonteite`, `dacostaite`, and `fluormacraeite`. All five primary PDFs were downloaded from *European Journal of Mineralogy* (`https://doi.org/10.5194/ejm-...`), segmented into `196` bounded text passages (`<= 1,800` bytes per file across `68` full-PDF pages / `56` main-text pages and `152` main-text passages) via `scripts/index_bounded_pdf_passages.py`, and accompanied by `11` single-page `150`-DPI PNG table renders (`mutool draw -q -r 150`). We also identified five additional uncurated single-reference *European Journal of Mineralogy* critical-element mineral candidates (`spaltiite`, `tianhuixinite`, `zhenruite`, `keutschite`, and `heimite`) to preserve in the Round 130 frontier queue alongside `bonacinaite` (multi-reference queue) and the seven non-EJM single-reference candidates from Round 125.

## 2. Primary PDFs Inspected (`68` Pages, `196` Passages, `11` Table PNGs)

| Mineral (`id`) | IMA ID (Symbol) | Primary Source (EJM) | PDF Size (Bytes) | PDF SHA-256 | Pages (Main) | Passages (Main) | Table PNGs Inspected |
| :--- | :--- | :--- | ---: | :--- | ---: | ---: | :--- |
| **Zhiqinite** (`cmmmech:zhiqinite`) | `IMA:2019-077` (`Zqn`) | Xiong et al. (2020) *Eur. J. Mineral.* 32:557–574 | `13,146,556` | `12c366bf1f944d91336b55b5f790c5e19038c7f4b33d5b0c2a1d958f5461c86c` | `18 (14)` | `57 (43)` | `zhiqinite-p8-chem.png`, `zhiqinite-p10-struct.png` |
| **Belmonteite** (`cmmmech:belmonteite`) | `IMA:2024-040` (`Bmo`) | Biagioni et al. (2026) *Eur. J. Mineral.* 38:531–543 | `6,245,239` | `bc4240014f8067a727de189e861efdcf3b6590e56d234754f2506b186517d4f8` | `13 (11)` | `35 (27)` | `belmonteite-p4-chem.png`, `belmonteite-p8-struct.png` |
| **Dacostaite** (`cmmmech:dacostaite`) | `IMA:2024-015` (`Dco`) | Biagioni et al. (2025) *Eur. J. Mineral.* 37:39–52 | `6,041,860` | `ec6741ca8042912abf9977f3919c3e38382a4e6e463a45def571e6cb18f13df5` | `14 (11)` | `41 (30)` | `dacostaite-p4-chem.png`, `dacostaite-p6-struct.png` |
| **Fluormacraeite** (`cmmmech:fluormacraeite`) | `IMA:2024-054` (`Fmac`) | Grey et al. (2025) *Eur. J. Mineral.* 37:169–179 | `5,256,173` | `689507e22de88069e6a32dff43eb4f21c448c5be4fafb280c0d38d432c74ef32` | `11 (10)` | `30 (26)` | `fluormacraeite-p3-chem.png`, `fluormacraeite-p4-pxrd.png`, `fluormacraeite-p5-struct.png` |
| **Macraeite** (`cmmmech:macraeite`) | `IMA:2023-065` (`Mac`) | Grey et al. (2024) *Eur. J. Mineral.* 36:267–278 | `7,405,708` | `6e0abe558c782b2619a2fe0d50e1ff14e863f57ff98a751e2ec78cdc3b3920de` | `12 (10)` | `33 (26)` | `macraeite-p3-chem.png`, `macraeite-p7-struct.png` |

## 3. Curated Records & Canonical `CREATE` History Sidecars

| Record Path | Bytes | Record SHA-256 | History Sidecar Path | Bytes | Sidecar SHA-256 |
| :--- | ---: | :--- | :--- | ---: | :--- |
| `data/records/zhiqinite.yaml` | `6,663` | `c595c90a689c93e5506201a356ad8b6a9f46577e326389244b52fba7e6466c50` | `history/records/zhiqinite/2026-11-06T171100Z-antigravity-a1e4c9.yaml` | `975` | `ef47495c1d0dfd92305b43b2fc8ffd1bf77efacc33e0a184532018567bed586d` |
| `data/records/belmonteite.yaml` | `7,932` | `2934d320b26310b34d86189140f3a466ef4dc13220f30fb18a16543bdbd61012` | `history/records/belmonteite/2026-11-06T171105Z-antigravity-b2f5d8.yaml` | `1,015` | `86e12e820d1e952c01e4c376e5a27ce383b7d7235c73f386145d3c31d20d0052` |
| `data/records/dacostaite.yaml` | `8,476` | `f68cebd5614b16798da37084a258ad7e89b0692e872049d491a3add96053f356` | `history/records/dacostaite/2026-11-06T171110Z-antigravity-c3a6e7.yaml` | `992` | `3af313ea7863b833ec326ce476088155a4cd5a7a2f6928cf684db077a4d791ad` |
| `data/records/fluormacraeite.yaml` | `7,222` | `45fd1fb6d0e32f403592314e20585b1ca8da0e0ed5aa3543b97548aa1bb94837` | `history/records/fluormacraeite/2026-11-06T171115Z-antigravity-d4b7f6.yaml` | `992` | `30cc42dafd07941c2c5a4d021c8a26e923edfacd2f959555573838fd6a77971c` |
| `data/records/macraeite.yaml` | `7,570` | `1d06cfe408539e3b3eabb7611c0145110428d6706b4fec4b7942519b2f7ca822` | `history/records/macraeite/2026-11-06T171120Z-antigravity-e5c8a1.yaml` | `974` | `e72352428ed8466bcbc739cc8f32fe85dbba4b7b66e43bebb90937006a941968` |

## 4. Documented Primary-Source Arithmetic & Typographical Discrepancies

1. **`zhiqinite`** (Xiong et al. 2020):
   - The Abstract (p. 557) reports the 3D ED unit cell of zhiqinite as `a = 8.24(16) A, b = 4.78(10) A, c = 8.52(17) A, V = 336(11) A3`, whereas Section 5.4 (p. 566) and Table 4 (p. 566) round the cell axes to `a = 8.2(2) A, b = 4.8(1) A, c = 8.5(2) A` and Table 4 prints `V = 335(11) A3`.
   - Table 3 (p. 564) prints the grain `302-4` average weight-percent sum (`Si 52.89 + P 0.14 + Ti 43.25 + Cr 0.15 + Mn 0.28 + Fe 2.41 + Zr 0.44 + Ca 0.08 + Al 0.21`) as `Sum 100.00`, whereas the arithmetic sum of the 9 printed mean values is `99.85 wt%` (and the grain `302-4` average atomic-percent values sum to `99.83 at.%` vs printed `100.00`). Similarly, in grain `409-3`, point 1 wt% values sum to `100.02 wt%` (at.% sum `100.01`), point 4 wt% values sum to `100.01 wt%` (at.% sum `100.02`), and the grain `409-3` average wt% values (`Si 55.26 + P 0.02 + Ti 44.33 + Cr 0.17 + Fe 0.23`) sum to `100.01 wt%` (at.% sum `100.01`) vs printed `100.00`.
2. **`belmonteite`** (Biagioni et al. 2026):
   - Section 3 (p. 533) reports the calculated Gladstone-Dale compatibility index as `1 - (Kp/Kc) = -0.020 (superior)`, whereas direct evaluation from the reported `nmean = 1.564`, `Dcalc = 2.662 g cm-3`, and empirical composition yields `1 - (Kp/Kc) = +0.020` (opposite sign).
   - Section 5.1 (p. 535) reports `R1 = 0.0226` for `1933` reflections with `Fo > 4sigma(Fo)`, whereas Table 3 (p. 538) prints the header `Fo > 4sigma(Fo)` as `1938` and the text in Section 5.1 lists `1938` as the total number of unique reflections.
3. **`dacostaite`** (Biagioni et al. 2025):
   - Section 3 (p. 40) reports the unit-cell volume refined from powder X-ray diffraction data (`a = 12.2385(13), b = 13.6660(19), c = 7.2130(8) A, beta = 94.716(12) deg`) as `V = 1202.2(2) A3`, whereas direct evaluation `V = a*b*c*sin(beta)` from those four refined parameters yields `1202.31 A3`.
   - Table 2 (p. 44) lists the reference card for the strongest powder X-ray diffraction lines of metavoltine as `PDF 20-0453`, whereas page 42 (end of Section 3) cites `PDF 29-0703`.
4. **`fluormacraeite`** (Grey et al. 2025):
   - The Abstract (p. 169) identifies the holotype specimen at Museums Victoria as `M56607`, whereas Section 2 (p. 170) reports the holotype registration number as `MM 44675`.
   - Table 2 (p. 172) prints index `hkl = -2 2 1` for two consecutive reflections at `dmeas = 4.544 A` (`dcalc = 4.545 A, I = 11`) and `dmeas = 4.499 A` (`dcalc = 4.497 A, I = 18`).
5. **`macraeite`** (Grey et al. 2024):
   - Section 3 (p. 269) reports the calculated density for the empirical formula with `Z = 4` as `2.38 g cm-3` (and `2.39 g cm-3` for the ideal formula), whereas Table 3 (p. 273) lists `Dcalc = 2.426 g cm-3` for the structural formula with `Z = 4`.
   - Table 1 (p. 269) prints the analytical total before the `-O=F` correction as `100.38 wt%`, whereas the arithmetic sum of the 11 printed mean constituent values (`K2O 4.52 + MnO 11.49 + CaO 0.13 + MgO 1.38 + ZnO 0.65 + Al2O3 0.59 + Fe2O3 15.86 + TiO2 7.51 + P2O5 29.55 + F 0.89 + H2O 27.80`) is `100.37 wt%` (giving `100.00 wt%` after subtracting `-O=F = 0.37 wt%`, vs printed `100.01 wt%`).

## 5. Preserved Frontier Queue for Round 130 (`13` Candidates)

- **Open-Access EJM Single-Reference Candidates (`5`)**: `spaltiite` (`IMA:2014-012`), `tianhuixinite` (`IMA:2022-081`), `zhenruite` (`IMA:2022-050`), `keutschite` (`IMA:2014-038`), and `heimite` (`IMA:2022-019`).
- **Multi-Reference Candidates (`1`)**: `bonacinaite` (`IMA:2018-056`, `Mineralogical Magazine 84 (2020), 568; European Journal of Mineralogy 36 (2024), 863`).
- **Preserved Non-EJM Single-Reference Candidates (`7`)**: `carletonmooreite` (`IMA:2018-068`), `changesite-y` (`IMA:2022-023`), `chihmingite` (`IMA:2022-010`), `ferroberaunite` (`IMA:2021-036`), `gysinite-la` (`IMA:2022-008`), `haleniusite-ce` (`IMA:2003-028`), and `ikranite` (`IMA:2000-010`).
