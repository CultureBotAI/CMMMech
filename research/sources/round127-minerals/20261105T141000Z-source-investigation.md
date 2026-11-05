# Round 127 Source Investigation Dossier (`20261105T141000Z`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 9, Stage 1 (`add_records`)
- **Timestamp (UTC)**: `2026-11-05T14:10:00Z`
- **Corpus Progression**: `683 -> 688` records (`+5`), `1335 -> 1342` history sidecars (`+5` `CREATE`, `+2` `EDIT`), `1062 -> 1069` structured reviews (`+7`)

## 1. Bounded Frontier Search & Citation Verification Protocol

We inspected the five open-access *European Journal of Mineralogy* single-reference critical-element mineral candidates queued in Round 126 (`ginelfite`, `graulichite-la`, `karlseifertite`, `skogbyite`, and `tetrahedrite-cd`) against the September 2026 IMA-CNMNC Master List of Minerals (`IMA_Master_List_(2026-09).pdf`, pages 82, 86, 109, 201, and 215). Direct verification against the Master List resolved four volume/page transcription errors in Round 126's deferred queue (`ginelfite` at *Eur. J. Mineral.* `37 (2025), 319–335` rather than `35 (2023), 795`; `graulichite-la` at `34 (2022), 365–374` rather than `33 (2021), 435`; `karlseifertite` at `36 (2024), 873–878` rather than `36 (2024), 837`; and `skogbyite` at `37 (2025), 269–277` rather than `36 (2024), 459`). We also identified five additional uncurated single-reference *European Journal of Mineralogy* critical-element mineral candidates (`pilanesbergite`, `luxembourgite`, `tancaite-ce`, `argentotennantite-fe`, and `badengzhuite`) to preserve in the Round 128 frontier queue alongside the seven non-EJM single-reference candidates from Round 125.

## 2. Primary PDFs Inspected (`53` Pages, `156` Passages, `10` Table PNGs)

| Mineral (`id`) | IMA ID (Symbol) | Primary Source (EJM) | PDF Size (Bytes) | PDF SHA-256 | Pages (Main) | Passages (Main) | Table PNGs Inspected |
| :--- | :--- | :--- | ---: | :--- | ---: | ---: | :--- |
| **Ginelfite** (`cmmmech:ginelfite`) | `IMA:2022-110` (`Glf`) | Biagioni et al. (2025) *Eur. J. Mineral.* 37:319–335 | `9,245,538` | `284c4425266684530b3580788d4abb6216d3e3700dda288562ceb83a0afda963` | `17 (15)` | `51 (45)` | `ejm-37-319-2025-p4.png`, `ejm-37-319-2025-p6.png` |
| **Graulichite-(La)** (`cmmmech:graulichite-la`) | `IMA:2020-093` (`—`) | Biagioni et al. (2022) *Eur. J. Mineral.* 34:365–374 | `3,468,589` | `1c1909adae0aec18a7e4b98b675801f777b31b8ccdb492b5449e6fb82b8e42af` | `10 (8)` | `29 (23)` | `ejm-34-365-2022-p4.png`, `ejm-34-365-2022-p5.png` |
| **Karlseifertite** (`cmmmech:karlseifertite`) | `IMA:2024-007` (`Karl`) | Kampf et al. (2024) *Eur. J. Mineral.* 36:873–878 | `3,865,473` | `50ba4abe3d60bf80c28fa83d3d6f100293e3d08febf3a2a5ed414c2eae3f9a09` | `6 (5)` | `15 (13)` | `ejm-36-873-2024-p3.png`, `ejm-36-873-2024-p4.png` |
| **Skogbyite** (`cmmmech:skogbyite`) | `IMA:2023-085` (`Skb`) | Jonsson et al. (2025) *Eur. J. Mineral.* 37:269–277 | `1,667,522` | `61604fdc9a43e344c036f8355d0cee71263952cdec241b924b2bf0c93a8ff47b` | `9 (8)` | `27 (25)` | `ejm-37-269-2025-p3.png`, `ejm-37-269-2025-p6.png` |
| **Tetrahedrite-(Cd)** (`cmmmech:tetrahedrite-cd`) | `IMA:2022-115` (`Ttr-Cd`) | Sejkora et al. (2023) *Eur. J. Mineral.* 35:897–907 | `1,290,202` | `1456df9033f2bc95f866b9949954831ce7ca7688366fa2357a3de0e3768b9341` | `11 (9)` | `34 (28)` | `ejm-35-897-2023-p4.png`, `ejm-35-897-2023-p6.png` |

## 3. Curated Records & Canonical `CREATE` History Sidecars

| Record Path | Bytes | Record SHA-256 | History Sidecar Path | Bytes | Sidecar SHA-256 |
| :--- | ---: | :--- | :--- | ---: | :--- |
| `data/records/ginelfite.yaml` | `9,011` | `cdf6d406dba0fd315dd664ff1dabd56af504318548cad21beff9148ce41e2c39` | `history/records/ginelfite/2026-11-05T140956Z-antigravity-4caced.yaml` (`CREATE`), `history/records/ginelfite/2026-11-05T150150Z-antigravity-94393d.yaml` (`EDIT`) | `990` / `876` | `2baed4137626d941ae80b3352b746b1ce9101996533ff0b16e09c26207bfbbd9` / `0cb4fa35469c079405b6d79daa435cd603eba1b5f9c0c0a5459e9ade8a01925f` |
| `data/records/graulichite-la.yaml` | `7,323` | `64ceb95365f0cdb3c696047d046ac7e856182c1114970669e0cbc6454b2a4853` | `history/records/graulichite-la/2026-11-05T140958Z-antigravity-e38239.yaml` | `997` | `43906b9b21a81260e3e75862966e20c4cb9f2775f3cb021e18af9850aa839987` |
| `data/records/karlseifertite.yaml` | `7,027` | `5a4f7e8a5c137124a0108d9bdad9bc327c84eb2a358e4d8a0aa527fd70420e2d` | `history/records/karlseifertite/2026-11-05T140444Z-antigravity-3ac85f.yaml` (`CREATE`), `history/records/karlseifertite/2026-11-05T150152Z-antigravity-599e7a.yaml` (`EDIT`) | `1,008` / `807` | `99b821f047d6b1d578dc2a734667f182227f0289b6d2a0171bd9bd83011a4717` / `f3caafe5c14456e0ae3b7f6d435bdcfed9fdc4851de8d625027fe2b7c752f59f` |
| `data/records/skogbyite.yaml` | `6,744` | `285ae181768fd17084cb8b5f4d163134c544a704230cc77aabd7286a0654e19c` | `history/records/skogbyite/2026-11-05T140445Z-antigravity-dc41ae.yaml` | `990` | `bf9f6b15693f0cfff652a15b4e6951ad1148536b2b577a2ad0766fb8303a4aa7` |
| `data/records/tetrahedrite-cd.yaml` | `6,780` | `b587167cf3071664071983bc5e2ce78e952b8e06cf7f6f068a8038381d0b1e6a` | `history/records/tetrahedrite-cd/2026-11-05T140447Z-antigravity-6f1290.yaml` | `1,017` | `fc692d6bd632c2b29a0d1c3b27dc5568246f2b86ec6fe6486f2c5e9b266b9e19` |

## 4. Documented Primary-Source Arithmetic & Typographical Discrepancies

1. **`ginelfite`** (Biagioni et al. 2025):
   - The September 2026 IMA-CNMNC Master List (p. 82) lists the pre-refinement formula `Ag2(Ag0.5Fe2+0.5)TlPb23.5(Sb,As)33.5S76`, whereas the published primary description (title, abstract, Section 4.1, and Table 7) reports `Ag2(Ag0.5Fe2+0.5)TlPb24.5(Sb,As)32.5S75.5` after accounting for the half-occupied `S(71)` site and refined `Pb/(Sb,As)` site populations.
   - Within Biagioni et al. (2025), Table 8 (p. 332) prints the formula of ginelfite with `S76` as `Ag2(Ag0.5Fe0.5)TlPb24.5(Sb,As)32.5S76`, whereas the title, abstract, Section 4.1, and Table 7 print `S75.5`; additionally, the sum of the modular boxwork structural formulae on p. 328 is `(Ag0.51Fe0.49)Ag2(Tl0.65Pb0.35)Pb21(Sb7.59Pb4.41)Sigma12.00(Sb15.52As8.48)Sigma24.00S75.5` with valence equilibrium error `Ev = -1.7%` (compared with empirical `Ev(%) = -1.1(1.0)%` with range `-2.3` to `+1.7%` in Table 2).
2. **`graulichite-la`** (Biagioni et al. 2022):
   - Table 1 (p. 369) prints the normalized oxide totals for Domain #1 and Domain #2 as `100.00 wt%`, whereas the arithmetic sums of the 13 rounded normalized oxide values are `100.02 wt%` for both domains.
   - Because the porous, fragile lamellae yielded low unpolished EPMA totals (`78.34 wt%` and `83.66 wt%`) and only `47` unique reflections up to `2theta = 31.75 deg`, the isotropic structure refinement (`R1 = 0.0956`) exhibits an apparent inversion of `X–O(1)` (`1.65(9) A`) vs `X–O(2)` (`1.56(5) A x 3`) bond lengths explicitly identified by the authors as a refinement artifact.
3. **`karlseifertite`** (Kampf et al. 2024):
   - Section 1 (p. 874) states `(Warr symbol: Karl)` whereas the IMA Master List (p. 109) assigns `Ksf`.
   - Section 4 (p. 874) prints the simplified formula as `Pb(Ga,Ge,Fe3+,Al)[(As,S,W)O4]2(OH)6`, omitting the subscript `3` on the octahedral `G`-site group `(Ga,Ge,Fe3+,Al)3` corresponding to the alunite-supergroup general formula `DG3(TX4)2X'6`.
   - Table 5 (p. 877) prints the mean bond lengths as `<Pb-O> = 2.802 A`, `<Ga-O> = 1.993 A`, and `<As-O> = 1.694 A`, whereas the multiplicity-weighted arithmetic means of the listed distances (`Pb-O2 2.785(7) x 6`, `Pb-O3 2.838(4) x 6`; `Ga-O2 1.959(7) x 2`, `Ga-O3 1.965(3) x 4`; `As-O1 1.671(13) x 1`, `As-O2 1.699(7) x 3`) are `2.812 A`, `1.963 A`, and `1.692 A`, respectively.
   - Table 6 (p. 877) prints the anion bond-valence sums for `O1` and `O2` as `1.81` and `1.95 v.u.`, whereas the rounded row contributions sum to `1.82` and `1.94 v.u.`.
4. **`skogbyite`** (Jonsson et al. 2025):
   - Table 1 (p. 271) prints the EPMA mean oxide total (`n = 19`) as `98.42 wt%`, whereas the 12 printed mean oxide values sum arithmetically to `98.21 wt%`; additionally, the printed `CaO` mean (`0.06 wt%`) exceeds the printed `CaO` range (`0.02–0.05 wt%`).
   - In the empirical formula (pp. 269, 271, 273), the `A`/`M(1)` site population is written `(Zr4+0.69Ce3+0.10Mg0.06Ca0.01Zn0.01Pb0.01)Sigma0.87`, whereas the rounded subscripts sum to `0.88 apfu`.
   - Section 3 (p. 271) prints `c : a = 0.4999`, which is the inverted ratio `a : c = 9.4914 / 18.9875 = 0.49988` (true `c : a = 2.0005`).
   - The Abstract (p. 269) reports `648` unique reflections with `I > 2sigma(I)`, whereas Section 6.2 (p. 273) and Table 3 (p. 274) report `658`.
   - Table 6 (p. 275) prints `BVS = 2.34` and `2.43 v.u.` for `M(3)` and `M(4)` vs unrounded sums `2.32` and `2.44 v.u.`.
5. **`tetrahedrite-cd`** (Sejkora et al. 2023):
   - The Abstract (p. 897) misprints the mineral name as `"Tennantite-(Cd) is cubic, I-43m, with unit-cell parameters a = 10.504(3) A, V = 1158.9(9) A3, and Z = 2"` when reporting the unit-cell parameters of holotype `tetrahedrite-(Cd)`.
   - Table 3 (p. 901) prints `dcalc` for reflection `4 4 4` (`Icalc = 3`) without a decimal point as `1516` instead of `1.516 A`.
   - Table 6 (p. 903) lists `X(3)-S(1) x 3 = 2.435(3) A`, whereas Section 5.2 prose (p. 903) writes `2.434 A`.

## 5. Preserved Frontier Queue for Round 128

- **Open-Access EJM Single-Reference Candidates (`5`)**: `pilanesbergite` (`IMA:2023-007`), `luxembourgite` (`IMA:2018-154`), `tancaite-ce` (`IMA:2009-097`), `argentotennantite-fe` (`IMA:2023-126`), and `badengzhuite` (`IMA:2019-076`).
- **Preserved Non-EJM Single-Reference Candidates (`7`)**: `carletonmooreite` (`IMA:2018-068`), `changesite-y` (`IMA:2022-023`), `chihmingite` (`IMA:2022-010`), `ferroberaunite` (`IMA:2021-036`), `gysinite-la` (`IMA:2022-008`), `haleniusite-ce` (`IMA:2003-028`), and `ikranite` (`IMA:2000-010`).
