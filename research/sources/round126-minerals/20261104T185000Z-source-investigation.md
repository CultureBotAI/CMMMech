# Round 126 Source Investigation Dossier (`20261104T185000Z`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 8, Stage 1 (`add_records`)
- **Timestamp (UTC)**: `2026-11-04T18:50:00Z`
- **Corpus Progression**: `678 -> 683` records (`+5`), `1290 -> 1295` history sidecars (`+5`), `1016 -> 1021` structured reviews (`+5`)

## 1. Bounded Frontier Search & Selection Protocol

We surveyed the September 2026 IMA-CNMNC Master List of Minerals (`IMA_Master_List_(2026-09).pdf`) for uncurated single-reference IMA-approved (`status = A`) critical-element mineral species whose primary type descriptions were published open-access in *European Journal of Mineralogy* (`vol. >= 32`). Ten uncurated single-reference candidates were identified. Following the strict full-PDF + bounded-passage (`<= 1,800` bytes) + single-page PNG table inspection protocol, we selected five species for Round 126 curation and preserved the remaining five EJM candidates (plus the seven non-EJM single-reference candidates from Round 125) in the documented Round 127 frontier queue.

## 2. Primary PDFs Inspected (`62` Pages, `167` Passages, `10` Table PNGs)

| Mineral (`id`) | IMA ID (Symbol) | Primary Source (EJM) | PDF Size (Bytes) | PDF SHA-256 | Pages (Main) | Passages (Main) | Table PNGs Inspected |
| :--- | :--- | :--- | ---: | :--- | ---: | ---: | :--- |
| **Niasite** (`cmmmech:niasite`) | `IMA:2019-105` (`—`) | Kampf et al. (2020) *Eur. J. Mineral.* 32:373–385 | `10,637,805` | `d714ae2487c000a867ff054cd60abe9369a81c2b57a51636e9e9f7c7d56cfdca` | `13 (11)` | `32 (26)` | `niasite-p3.png`, `niasite-p5.png` |
| **Manganoschafarzikite** (`cmmmech:manganoschafarzikite`) | `IMA:2022-129` (`Msfz`) | Holtstam et al. (2024) *Eur. J. Mineral.* 36:311–322 | `4,407,586` | `0049c6a3f4a4a53c7af8e900ceb54cb41fe923eccb04f514e38d9147801c0ddf` | `12 (10)` | `32 (27)` | `manganoschafarzikite-p5.png`, `manganoschafarzikite-p9.png` |
| **Erzwiesite** (`cmmmech:erzwiesite`) | `IMA:2012-082` (`Erw`) | Topa et al. (2026) *Eur. J. Mineral.* 38:237–247 | `23,901,051` | `db770a01b13c037e1a1a3131e5d2512843e94b4186f6eff9cf450e46da9e2796` | `11 (9)` | `31 (25)` | `erzwiesite-p6.png`, `erzwiesite-p7.png` |
| **Kenoargentotetrahedrite-(Zn)** (`cmmmech:kenoargentotetrahedrite-zn`) | `IMA:2020-075` (`Kattr-Zn`) | Qu et al. (2024) *Eur. J. Mineral.* 36:397–409 | `3,150,432` | `621c1204eb5720c1f4b74eff577fb87027324faa8e9618f7ffef409d496d0401` | `13 (10)` | `38 (27)` | `kenoargentotetrahedrite-zn-p4.png`, `kenoargentotetrahedrite-zn-p6.png` |
| **Lopatkaite** (`cmmmech:lopatkaite`) | `IMA:2012-083` (`Lpk`) | Topa et al. (2026) *Eur. J. Mineral.* 38:217–229 | `9,259,446` | `12c1bdd8dc95b9024445f67dbf309140995accbef6d8d9b3dc38aba029163abb` | `13 (11)` | `34 (28)` | `lopatkaite-p4.png`, `lopatkaite-p6.png` |

## 3. Curated Records & Canonical `CREATE` History Sidecars

| Record Path | Bytes | Record SHA-256 | History Sidecar Path | Bytes | Sidecar SHA-256 |
| :--- | ---: | :--- | :--- | ---: | :--- |
| `data/records/niasite.yaml` | `6,750` | `7368a79dbdab8f0930bdd201e284145930ef8f518935bd0d0fbed4979d40af6f` | `history/records/niasite/2026-11-04T184716Z-antigravity-0c8986.yaml` | `983` | `e77d707b27d5d84298d710ca9240b3c1bfde0d6806a3a81123e055ece3bfcf38` |
| `data/records/manganoschafarzikite.yaml` | `6,258` | `db0dc3ce25a05af92bb167ffa2533760720a25beaf6363a6f0f9137ca0333440` | `history/records/manganoschafarzikite/2026-11-04T184718Z-antigravity-39370f.yaml` | `1,054` | `2f8a9d6d41fc6644b4929550da0d56b3cea32ab0b86da3da1ad09412c2d0b246` |
| `data/records/erzwiesite.yaml` | `6,371` | `5f7ec46a59f6194df9acdb0e36d05c9d3b863dfb86a6f3e905fca76f861f2bd7` | `history/records/erzwiesite/2026-11-04T184719Z-antigravity-c22686.yaml` | `990` | `8a5b3fb694fabd9e4791466e616ff0a5f162aaac33ec0fa42e76f00069ae1917` |
| `data/records/kenoargentotetrahedrite-zn.yaml` | `6,235` | `e57171f3a27ab6d37b0e4721ea2a48c7f3989143b1f171377dbba7bbda20d049` | `history/records/kenoargentotetrahedrite-zn/2026-11-04T184721Z-antigravity-b800cb.yaml` | `1,056` | `10a749e8f04cc1764b693933d184fefcbe087daeedd3adf0c392efd89efc4fbe` |
| `data/records/lopatkaite.yaml` | `5,973` | `971c58ea5199fec6c0cfec4d863c747a0b64b4db5c29c60783bbd765156f4c87` | `history/records/lopatkaite/2026-11-04T184724Z-antigravity-9f176b.yaml` | `992` | `abf6844880b6e6e5019dcb74fe607d10d8c613d8b2864ab7bf3b7b5f28f33a68` |

## 4. Documented Primary-Source Arithmetic & Typographical Discrepancies

1. **`niasite`** (Kampf et al. 2020):
   - Table 3 (p. 380) prints crystal dimensions as `35 mm x 30 mm x 20 mm` via a `mm`-for-`um` unit typo; Section 6 prose (p. 377) gives `35 um x 30 um x 20 um`.
   - Table 6a (p. 383) prints the `O1` bond-valence sum as `1.99 v.u.`, whereas `0.39 (Ni1) + 0.35 (Ni2) + 1.24 (As2) = 1.98 v.u.`.
2. **`manganoschafarzikite`** (Holtstam et al. 2024):
   - Section 5.2 (p. 315) prints the powder XRD unit-cell volume as `V = 442.23(5) A3`, whereas `a = 8.6273(5) A` and `c = 5.9683(5) A` yield `a^2 * c = 444.22(5) A3`.
   - Section 6.1 prints the weak `Sb-O-Sb` bending Raman band as `402 cm-1` on p. 315 vs `405 cm-1` on p. 316 and in Fig. 3.
   - Table 10 (p. 318) prints the mean `Mn-O` bond length as `2.147 A` whereas Section 7.1 prose (p. 318) prints `2.146 A` (exact mean `2.1465 A`).
   - Section 3 (p. 313) prints `"400-70 nm range"` for `400-700 nm`, and Section 5.1 (p. 314) prints `"lambda = 0.71703 A"` for `0.71073 A`.
3. **`erzwiesite`** (Topa et al. 2026):
   - Section 4 (p. 241) and Table 2 column `IF` (p. 242) print the ideal `Ag8Pb12Bi16S40` weight percentages as `Ag 10.82, Pb 31.76, Bi 41.92, S 16.08, total 100.00 wt%`, whereas their arithmetic sum is `100.58 wt%`.
   - Abstract (p. 237) prints `Dcalc = 7.075 g/cm3` vs `7.045 g/cm3` (empirical) and `7.074 g/cm3` (structural) in Section 3 (p. 240).
   - Section 5 (p. 242) includes a copy-paste phrase `"for the available crystal from Madoc"` from the companion lopatkaite paper, and Fig. 8 caption (p. 244) twice spells the mineral `"erwiesite"`.
4. **`kenoargentotetrahedrite-zn`** (Qu et al. 2024):
   - Section 5 prose (p. 401) writes `0.436(9) apfu` for `2 x M(2b)`, whereas `2 x 0.219(9) = 0.438(9)` as printed on p. 402.
5. **`lopatkaite`** (Topa et al. 2026):
   - Table 5 (p. 223) prints the bond-valence sum of site `(Pb,Sb)4` without a decimal point as `2128` for `2.128 v.u.`.

## 5. Preserved Frontier Queue for Round 127

- **Remaining Open-Access EJM Single-Reference Candidates (`5`)**: `ginelfite` (`IMA:2022-110`), `graulichite-la` (`IMA:2020-093`), `karlseifertite` (`IMA:2024-007`), `skogbyite` (`IMA:2023-085`), and `tetrahedrite-cd` (`IMA:2022-115`).
- **Preserved Non-EJM Single-Reference Candidates (`7`)**: `carletonmooreite` (`IMA:2018-068`), `changesite-y` (`IMA:2022-023`), `chihmingite` (`IMA:2022-010`), `ferroberaunite` (`IMA:2021-036`), `gysinite-la` (`IMA:2022-008`), `haleniusite-ce` (`IMA:2003-028`), and `ikranite` (`IMA:2000-010`).
