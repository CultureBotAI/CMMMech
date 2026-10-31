# Round 124 Critical Mineral Source Investigation and Bounded Frontier Audit

- **Investigation ID:** `20261031T015000Z-round124-minerals`
- **Created At:** `2026-10-31T01:50:00Z` (updated `2026-10-31T02:58:00Z`)
- **Cycle / Stage:** Cycle 6, Stage 1 (`add_records`)
- **Corpus Transition:** `668 -> 673` records (`+5` records), `1157 -> 1167` canonical history sidecars (`+5` `CREATE` sidecars, `+5` `EDIT` sidecars)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`57` full-PDF pages total; `48` main-text pages) indexed into `153` UTF-8 text passages (`<= 1,800` bytes each; `222,547` passage bytes / `222,733` raw text bytes total; `120` main-text passages) plus `11` single-page PNG table renders (`150` DPI via `mutool draw`).

## 1. Inspected Primary Sources and Admitted Records (5)

| Slug | Name | IMA ID (Status) | End-Member Formula | Primary Source DOI, Verbatim Title & PDF SHA-256 | Full-PDF & Main-Text Pages / Passages / Table PNGs | Record SHA-256 | History Sidecars (`CREATE` & `EDIT`) & SHA-256 |
|---|---|---|---|---|---|---|---|
| `laurentthomasite` | Laurentthomasite | `IMA:2018-157` (`A`) | `Mg2K(Be2Al)Si12O30` | `10.5194/ejm-32-355-2020` (*Laurentthomasite, Mg2K(Be2Al)Si12O30: a new milarite-group-type member from the Ihorombe region, Fianarantsoa Province, Madagascar*, `ejm-32-355-2020.pdf`, `4,244,267` B, `6ec8ead80c98baae4e5ca0425a1a944d3f707ecec5152d037f8627ac270737d8`) | `11` full-PDF pp. / `31` passages (`43,631` passage B / `43,670` raw B; `9` main-text pp. / `21` passages) / pp. 5, 8 | `145c3ad84325ec6470ebb305ff4648a3b198ad9adda1412116e93f03479cb019` | `CREATE`: `history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml` (`ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c`); `EDIT`: `history/records/laurentthomasite/2026-10-31T025403Z-antigravity-87d29f.yaml` (`ee1fde809529f4fe835a5bc83d73ed02ae21abbc99ce651162b7576c26c7ed09`) |
| `wumuite` | Wumuite | `IMA:2017-067a` (`A`) | `KAl0.33W2.67O9` | `10.5194/ejm-32-483-2020` (*Wumuite (KAl0.33W2.67O9) – a new mineral with an HTB-type structure from the Panzhihua–Xichang region in China*, `ejm-32-483-2020.pdf`, `4,649,288` B, `1ee1fcd925ad830ab3df485c984ab969714ade6c45f1f8871ea49112a141dd72`) | `12` full-PDF pp. / `29` passages (`43,172` passage B / `43,210` raw B; `11` main-text pp. / `26` passages) / pp. 3, 6 | `303d5e7ca9d113f8db3ca26550f3baa8040bdef50f1dbe0f96a1cb299b056c77` | `CREATE`: `history/records/wumuite/2026-10-31T014341Z-antigravity-a5dc6c.yaml` (`278dbc89230d8c4d4ed9b7064ddce89829b095c2a0d7e90506ddac40d0733bbd`); `EDIT`: `history/records/wumuite/2026-10-31T025433Z-antigravity-c4f156.yaml` (`a9279a871035ca946d463c371d846eae859293f3a7eae92c8a63d7ea4efe43ae`) |
| `moabite` | Moabite | `IMA:2020-092` (`A`) | `NiFe3+(PO4)O` | `10.5194/ejm-37-353-2025` (*Moabite, NiFe3+(PO4)O, a new natural oxyphosphate*, `ejm-37-353-2025.pdf`, `1,885,515` B, `7340e0f9c6213775801d2987bbd165285831bca467ae671b48275cecfdcf1602`) | `11` full-PDF pp. / `32` passages (`47,902` passage B / `47,935` raw B; `8` main-text pp. / `21` passages) / pp. 4, 6 | `c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716` | `CREATE`: `history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml` (`ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587`); `EDIT`: `history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml` (`ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b`) |
| `vielleaureite-ce` | Vielleaureite-(Ce) | `IMA:2022-134` (`A`) | `Mn2+Ce(MgAlMn2+)(Si2O7)(SiO4)F(OH)` | `10.5194/ejm-37-627-2025` (*Vielleaureite-(Ce), a new epidote of the dollaseite group, coexisting with Mn-dominant hellandite in Mn deposits of the central Pyrenees*, `ejm-37-627-2025.pdf`, `5,520,335` B, `72fa2e6ebb9ed43c7b2fe61067a5d910df199870b732d7b499fe0fcdb58fdf9e`) | `12` full-PDF pp. / `35` passages (`49,791` passage B / `49,829` raw B; `11` main-text pp. / `31` passages) / pp. 5, 6 | `2c503fac8dc7f2eba571a56470c0907358ceab2fbb0ba2a2cabc5c677d8ca5c8` | `CREATE`: `history/records/vielleaureite-ce/2026-10-31T014425Z-antigravity-97a94c.yaml` (`0440a3673c0c5e1beccb20febc81929cd059a37e3459011601a4fe3ac63e7e4d`); `EDIT`: `history/records/vielleaureite-ce/2026-10-31T025532Z-antigravity-9fb7bf.yaml` (`585153c3917ba0786840f792d0754effba7301ec5588e6ba25a134bc142c2c40`) |
| `xianhuaite-ce` | Xianhuaite-(Ce) | `IMA:2024-091` (`A`) | `K2CeNb5O15` | `10.5194/ejm-38-449-2026` (*Xianhuaite-(Ce), K2CeNb5O15, a new niobium mineral from the Bayan Obo deposit, China*, `ejm-38-449-2026.pdf`, `5,716,810` B, `872617555378d4463559b187a9a4b4acdfc0dbdac6ba4b4545521a69032a5805`) | `11` full-PDF pp. / `26` passages (`38,051` passage B / `38,089` raw B; `9` main-text pp. / `21` passages) / pp. 4, 6, 7 | `6c10184ccc5d687d3a4ca89b77766c5e5311b50e4696064b8d20626d7d301ec8` | `CREATE`: `history/records/xianhuaite-ce/2026-10-31T014447Z-antigravity-4ccc72.yaml` (`2ad06ecde6fadc591fd8759cb337f7668905b029749f4aec8599eb5e0c80a744`); `EDIT`: `history/records/xianhuaite-ce/2026-10-31T025602Z-antigravity-e34dd7.yaml` (`2ccf0761406f9542b33af6d12fed0dfaa2d4f6ba9f62466564f5bd3baec603b7`) |

### Primary-Source Discrepancies Documented in Admitted Records

1. **`laurentthomasite` (`Ferraris et al. 2020`, *Eur. J. Mineral.* 32:355–365):**
   - Table 1 (p. 357) prints the ideal formula of laurentthomasite as `Mg2K(Be2Al)Si12O3` (missing the trailing `0` on `O30`), whereas the title, Abstract, and text print `Mg2K(Be2Al)Si12O30`.
   - Table 2 (p. 359) prints the `FeO` average as `2.69 wt%` (`SD 0.08`) above a reported range of `2.50–2.67` (mean exceeds upper range bound) and prints the `TiO2` range as `0.02–0.019` (for `0.02–0.19`).
   - The Abstract (p. 355) lists 9 strongest PXRD lines printing `2.732 – (8) – 204` in place of `2.881 – (8) – 114` before `2.732 – (4) – 204` and omitting `1.825 (2)(315)` (vs Table 5, p. 361).
   - Section 5.2 prose (pp. 359–360) prints single-crystal XRD unit-cell parameters `a = 9.95800(7) Å`, `c = 14.114916(11) Å` (digit-duplication typo for `14.14916(11) Å`), `V = 1215.081(15) Å3` for crystal size `39.6 x 28.7 x 16.9 um`, whereas Table 6 (p. 362) prints `a = 9.95800(10) Å`, `c = 14.14920(10) Å`, `V = 1215.085(19) Å3` for crystal size `0.40 x 0.29 x 0.17 mm`.
2. **`wumuite` (`Xue, Li, & Xie 2020`, *Eur. J. Mineral.* 32:483–494):**
   - The Abstract (p. 483) prints type-locality coordinates `26°46'8.21" N, 101°27'13.86" E`, whereas Section 2 (p. 484) prints `26°46'18.21" N, 101°27'13.86" E`.
   - Table 3 (p. 488) reports the single-crystal XRD unit-cell parameter `c = 3.7711(3) Å` (`V = 229.66(4) Å3`), whereas the Abstract (p. 483) and Section 6.2 prose (p. 487) print `c = 3.7713 Å`.
   - Section 6.2 prose (p. 487) prints the space group as `P4/mbm` (a tetragonal symbol), whereas the Abstract (p. 483), Table 3 (p. 488), and Section 6.2 heading (p. 487) report orthorhombic space group `Pbam` (`No. 55`).
3. **`moabite` (`Britvin et al. 2025`, *Eur. J. Mineral.* 37:353–363):**
   - The Abstract (p. 353) reports `Dcalc = 4.324 g/cm3` (calculated from the empirical formula) and prints PXRD line `3,321(37)(102)` with a comma decimal separator, whereas Table 5 (p. 358) reports `Dx = 4.338 g/cm3` (crystallographic density for ideal `NiFe(PO4)O`) and Table 4 (p. 357) prints `3.321 (37) (102)`.
   - Table 2 (p. 356) labels the iron oxide column header `FeO*` with footnote `* Total iron calculated as Fe2O3` for trivalent `Fe3+` (`89.9 % Fe2O3 + 1.4 % Co2O3 + 0.7 % Cr2O3 + 8.0 % Al2O3 = 100.0 %`).
4. **`vielleaureite-ce` (`Ragu et al. 2025`, *Eur. J. Mineral.* 37:627–638):**
   - In the empirical formula, the rounded `A2` cations (`Ce0.66La0.32Nd0.02Er0.01`) sum to `1.01 apfu` while printed as `Sigma1.00`, and Table 5 (p. 633) prints the proposed `M1` site population with combined `Mn0.09` (`Mn2+0.08 + Mn3+0.02`).
   - Section 4.1 (p. 631) reports `V2O3 0.04 wt%` (`0.00–0.12`, `SD 0.04`) and `PbO 0.06 wt%` (`0.00–0.15`, `SD 0.05`) in the text while omitting those trace oxides from Table 2 (p. 631).
5. **`xianhuaite-ce` (`Yang et al. 2026`, *Eur. J. Mineral.* 38:449–459):**
   - Table 1 (p. 452) prints `Pr2O3` mean `0.28 wt%` (`SD 0.08`) with a range of `0.00–0.23` (mean exceeds upper range bound) and includes `Ta2O5 0.08 wt%` (`0.00–0.20`, `SD 0.09`), which rounds to `0.003 apfu` on `15 O` and is omitted from the printed empirical formula.
   - Section 3 text (p. 451) reports `U (562 ppm)` and `Pb (325 ppm)` whereas Table 2 (p. 452) prints `U = 561 ppm` and `Pb = 326 ppm`.

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
