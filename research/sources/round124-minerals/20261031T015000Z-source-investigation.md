# Round 124 Critical Mineral Source Investigation and Bounded Frontier Audit

- **Investigation ID:** `20261031T015000Z-round124-minerals`
- **Created At:** `2026-10-31T01:50:00Z`
- **Cycle / Stage:** Cycle 6, Stage 1 (`add_records`)
- **Corpus Transition:** `668 -> 673` records (`+5` records), `1157 -> 1162` canonical history sidecars (`+5` `CREATE` sidecars)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`57` pages total) indexed into `153` UTF-8 text passages (`<= 1,800` bytes each; `222,547` bytes total) plus `11` single-page PNG table renders (`150` DPI via `mutool draw`).

## 1. Inspected Primary Sources and Admitted Records (5)

| Slug | Name | IMA ID (Status) | End-Member Formula | Primary Source DOI & PDF SHA-256 | Pages / Passages / Table PNGs | Record SHA-256 | History Sidecar & SHA-256 |
|---|---|---|---|---|---|---|---|
| `laurentthomasite` | Laurentthomasite | `IMA:2018-157` (`A`) | `Mg2K(Be2Al)Si12O30` | `10.5194/ejm-32-355-2020` (`ejm-32-355-2020.pdf`, `4,244,267` B, `6ec8ead80c98baae4e5ca0425a1a944d3f707ecec5152d037f8627ac270737d8`) | `11` pp. / `31` passages (`49,127` B) / pp. 5, 8 | `9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859` | `history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml` (`ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c`) |
| `wumuite` | Wumuite | `IMA:2017-067a` (`A`) | `KAl0.33W2.67O9` | `10.5194/ejm-32-483-2020` (`ejm-32-483-2020.pdf`, `4,649,288` B, `1ee1fcd925ad830ab3df485c984ab969714ade6c45f1f8871ea49112a141dd72`) | `12` pp. / `29` passages (`38,821` B) / pp. 3, 6 | `6e7b83dce7f2776e5bd313041f98ee79401d003789765a9a52c747d58927d1bb` | `history/records/wumuite/2026-10-31T014341Z-antigravity-a5dc6c.yaml` (`278dbc89230d8c4d4ed9b7064ddce89829b095c2a0d7e90506ddac40d0733bbd`) |
| `moabite` | Moabite | `IMA:2020-092` (`A`) | `NiFe3+(PO4)O` | `10.5194/ejm-37-353-2025` (`ejm-37-353-2025.pdf`, `1,885,515` B, `7340e0f9c6213775801d2987bbd165285831bca467ae671b48275cecfdcf1602`) | `11` pp. / `32` passages (`46,200` B) / pp. 4, 6 | `e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410` | `history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml` (`ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587`) |
| `vielleaureite-ce` | Vielleaureite-(Ce) | `IMA:2022-134` (`A`) | `Mn2+Ce(MgAlMn2+)(Si2O7)(SiO4)F(OH)` | `10.5194/ejm-37-627-2025` (`ejm-37-627-2025.pdf`, `5,520,335` B, `72fa2e6ebb9ed43c7b2fe61067a5d910df199870b732d7b499fe0fcdb58fdf9e`) | `12` pp. / `35` passages (`51,936` B) / pp. 5, 6 | `5d184d309fa5d055701bf94b33a3cdd98f3f07cad6d89da68db26055905bd6d1` | `history/records/vielleaureite-ce/2026-10-31T014425Z-antigravity-97a94c.yaml` (`0440a3673c0c5e1beccb20febc81929cd059a37e3459011601a4fe3ac63e7e4d`) |
| `xianhuaite-ce` | Xianhuaite-(Ce) | `IMA:2024-091` (`A`) | `K2CeNb5O15` | `10.5194/ejm-38-449-2026` (`ejm-38-449-2026.pdf`, `5,716,810` B, `872617555378d4463559b187a9a4b4acdfc0dbdac6ba4b4545521a69032a5805`) | `11` pp. / `26` passages (`36,463` B) / pp. 4, 6, 7 | `bded1436940de7290ef097aae277bae82aa543529d685bdb8c80c6a8be067f36` | `history/records/xianhuaite-ce/2026-10-31T014447Z-antigravity-4ccc72.yaml` (`2ad06ecde6fadc591fd8759cb337f7668905b029749f4aec8599eb5e0c80a744`) |

### Primary-Source Discrepancies Documented in Admitted Records

1. **`laurentthomasite` (`Ferraris et al. 2020`, *Eur. J. Mineral.* 32:355–365):**
   - Table 1 (p. 357) prints the ideal formula of laurentthomasite as `Mg2K(Be2Al)Si12O3` (missing the trailing `0` on `O30`), whereas the title, Abstract, and text print `Mg2K(Be2Al)Si12O30`.
   - Table 2 (p. 359) prints the `FeO` average as `2.69 wt%` (`SD 0.08`) above a reported range of `2.50–2.67` (mean exceeds upper range bound) and prints the `TiO2` range as `0.02–0.019` (for `0.02–0.19`).
   - The Abstract (p. 355) lists 9 strongest PXRD lines printing `2.732 – (8) – 204` in place of `2.881 – (8) – 114` before `2.732 – (4) – 204` and omitting `1.825 (2)(315)` (vs Table 5, p. 361).
   - Section 5.2 prose (pp. 359–360) prints single-crystal XRD unit-cell parameters `a = 9.95800(7) Å`, `c = 14.114916(11) Å` (digit-duplication typo for `14.14916(11) Å`), `V = 1215.081(15) Å3` for crystal size `39.6 x 28.7 x 16.9 um`, whereas Table 6 (p. 362) prints `a = 9.95800(10) Å`, `c = 14.14920(10) Å`, `V = 1215.085(19) Å3` for crystal size `0.40 x 0.29 x 0.17 mm`.
2. **`wumuite` (`Xue, Li, & Xie 2020`, *Eur. J. Mineral.* 32:483–494):**
   - The Abstract (p. 483) prints type-locality coordinates `26°46'8.21" N, 101°27'13.86" E`, whereas Section 2 (p. 484) prints `26°46'18.21" N, 101°27'13.86" E`.
   - Table 3 (p. 488) reports the single-crystal XRD unit-cell parameter `c = 3.7711(3) Å` (`V = 229.66(4) Å3`), whereas the Abstract (p. 483) and Section 6.2 prose (p. 487) print `c = 3.7713 Å`.
3. **`moabite` (`Britvin et al. 2025`, *Eur. J. Mineral.* 37:353–363):**
   - The Abstract (p. 353) reports `Dcalc = 4.324 g/cm3` (calculated from the empirical formula) and prints PXRD line `3,321(37)(102)` with a comma decimal separator, whereas Table 5 (p. 358) reports `Dx = 4.338 g/cm3` (crystallographic density for ideal `NiFe(PO4)O`) and Table 4 (p. 357) prints `3.321 (37) (102)`.
4. **`vielleaureite-ce` (`Ragu et al. 2025`, *Eur. J. Mineral.* 37:627–638):**
   - In the empirical formula, the rounded `A2` cations (`Ce0.66La0.32Nd0.02Er0.01`) sum to `1.01 apfu` while printed as `Sigma1.00`, and Table 5 (p. 633) prints the proposed `M1` site population with combined `Mn0.09` (`Mn2+0.08 + Mn3+0.02`).
5. **`xianhuaite-ce` (`Yang et al. 2026`, *Eur. J. Mineral.* 38:449–459):**
   - Table 1 (p. 452) prints `Pr2O3` mean `0.28 wt%` (`SD 0.08`) with a range of `0.00–0.23` (mean exceeds upper range bound) and includes `Ta2O5 0.08 wt%` (`0.00–0.20`, `SD 0.09`), which rounds to `0.003 apfu` on `15 O` and is omitted from the printed empirical formula.

## 2. Remaining Deferred External Single-Reference Candidates (8)

The following 8 IMA-approved single-reference *European Journal of Mineralogy* candidates remain deferred for bounded PDF acquisition and passage indexing in subsequent rounds:

1. `carletonmooreite` (`IMA:2018-068`, `Ni3Si`, IMA p. 45, *Eur. J. Mineral.* 33 (2021), 193–201)
2. `changesite-y` (`IMA:2022-023a`, `(Ca,Y)8(Fe2+,Mg)2(PO4)7`, IMA p. 49, *Eur. J. Mineral.* 35 (2023), 457–466)
3. `chihmingite` (`IMA:2022-010`, `NiAl2O4`, IMA p. 51, *Eur. J. Mineral.* 34 (2022), 385–391)
4. `ferroberaunite` (`IMA:2021-036`, `Fe2+Fe3+5(PO4)4(OH)5·6H2O`, IMA p. 78, *Eur. J. Mineral.* 33 (2021), 735–746)
5. `gysinite-la` (`IMA:2022-008`, `PbLa(CO3)2(OH)·H2O`, IMA p. 96, *Eur. J. Mineral.* 35 (2023), 189–199)
6. `haleniusite-ce` (`IMA:2021-046`, `(Ce,La)OF`, IMA p. 98, *Eur. J. Mineral.* 33 (2021), 547–558)
7. `ikranite` (`IMA:2000-010`, `(Na,H3O)15(Ca,Mn,REE)6Fe3+2Zr3([],Zr)([],Si)Si24O66(O,OH)6Cl·nH2O`, IMA p. 107, *Eur. J. Mineral.* 33 (2021), 229–243)
8. `johanngeorgenstadtite` (`IMA:2019-122`, `Ni2+4.5(AsO4)3`, IMA p. 112, *Eur. J. Mineral.* 32 (2020), 467–481)

## 3. Excluded Non-Critical & Multi-Source Held Candidates

- **Excluded (`1`):** `cesstibtantite` (`(Cs,Na)SbTa4O12`, IMA p. 48, discredited species status `D`, redefined as `hydroxykenomicrolite`).
- **Multi-Source Held (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y` (require multiple historical or paywalled references before curation).
- **Open Source Issues Tracked (`4`):** `#495` (`uniprot_metal_cofactors`), `#496` (`bacdive_metal_utilization`), `#497` (`brenda_metal_enzymes`), `#498` (`rhea_metal_reactions`).
