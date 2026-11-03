# Round 125 Frontier Ingest Report (`2026-11-03`)

- **Cycle / Stage:** Cycle 7, Stage 1 (`add_records`)
- **Corpus Transition:** `673 -> 678` records (`+5` mineral records)
- **Canonical History Sidecars:** `1245 -> 1255` (`+5` `CREATE` sidecars, `+5` `EDIT` sidecars)
- **Structured Scientific Reviews:** `981 -> 986` (`+5` per-record review bundles)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`61` full-PDF pages / `52` main-text pages) indexed into `154` UTF-8 text passages (`<= 1,800` bytes each; `217,676` passage bytes / `217,871` raw text bytes; `130` main-text passages) plus `14` single-page PNG table renders (`150` DPI via `mutool draw`).
- **Source Investigation Dossier:**
  - `research/sources/round125-minerals/20261103T085500Z-source-investigation.json` (`bfa3569cb5599a4ce0ae5c0550271a84710ab5de03b4b534d9a3547507142f9e`)
  - `research/sources/round125-minerals/20261103T085500Z-source-investigation.md` (`527929d6f847c40e10158d89d13d9cfede8516975ad141de8d9f95e9a9e627bf`)

## Admitted Mineral Records (5)

| Slug | ID | IMA ID | Formula | Critical Element Link | Record Path & SHA-256 | History Sidecars (`CREATE` & `EDIT`) & SHA-256 | Review Bundle & SHA-256 |
|---|---|---|---|---|---|---|---|
| `johanngeorgenstadtite` | `cmmmech:johanngeorgenstadtite` | `IMA:2019-122` | `Ni2+4.5(AsO4)3` | Ni, As (Co-bearing) | `data/records/johanngeorgenstadtite.yaml` (`f736a07ae232dadb3c2bae2d258ddb3d9d64af0d0627e0ce2e1a24d6280c49cd`) | `CREATE`: `history/records/johanngeorgenstadtite/2026-11-03T091254Z-antigravity-ee9475.yaml` (`c305dac622731dfe05d794eca2c752672e2ab8186f850c6b5ea619b45e32e4d7`); `EDIT`: `history/records/johanngeorgenstadtite/2026-11-03T101609Z-antigravity-9eb999.yaml` (`abdd24539ac419e7e08087e07e323ee452639816dec7e5e653c0ef2b64d744f9`) | `reviews/structured/20261103T091500Z-johanngeorgenstadtite-round125-scientific-review/review.yaml` (`6685e60d73658d9a35a60f8c2b70a90df41cc29cc6a7c052156aee2754db1f72`) |
| `fengruiite` | `cmmmech:fengruiite` | `IMA:2024-045` | `[Ag6Sb2S7][Ag9CuS2Te2]` | Sb, Te (As-bearing) | `data/records/fengruiite.yaml` (`515efee2f6e88c788af7b97b3b403223291d5a80261d337ae4dcf0c33d427d9e`) | `CREATE`: `history/records/fengruiite/2026-11-03T091257Z-antigravity-552763.yaml` (`d5a8fea13aeb7d60f4441112d9343b1ba10f37f910e08dad82101335539a01ef`); `EDIT`: `history/records/fengruiite/2026-11-03T101639Z-antigravity-778d08.yaml` (`5a4dd451f2ffb4b3e5652d4db2698e64ab172ac4289ca479aff9a739bc51d49e`) | `reviews/structured/20261103T091500Z-fengruiite-round125-scientific-review/review.yaml` (`039f78b46983e2718cd0959c1aba2c346d4bff6737127b34f90c0f1253e32e36`) |
| `igelstromite` | `cmmmech:igelstromite` | `IMA:2021-035` | `Fe3+(SbPb)O4` | Sb (Mn-, As-bearing) | `data/records/igelstromite.yaml` (`4c635cb707dbbecc9edbcfb330d71ebe43083139f1e77097d48e55acb8ecb5e0`) | `CREATE`: `history/records/igelstromite/2026-11-03T091259Z-antigravity-e7affb.yaml` (`7fd21fa696b312027cdbca31aa2f698bab46aae4626156d79c6ef9c136738ebc`); `EDIT`: `history/records/igelstromite/2026-11-03T101706Z-antigravity-8ce276.yaml` (`7fa29ccec09a2e1dbe90cf3b6c3ebd50eb2c6cfc437fa2efa90243a568f96b7f`) | `reviews/structured/20261103T091500Z-igelstromite-round125-scientific-review/review.yaml` (`9fb7917c17f5142f0c31735ce3420c04b5b33946f55a33c52663bb55e18cc1cb`) |
| `plumbogottlobite` | `cmmmech:plumbogottlobite` | `IMA:2025-075` | `PbMg(VO4)(OH)` | V, Mg (Mn-bearing) | `data/records/plumbogottlobite.yaml` (`3bd29fdbe517900ec60494b52a1d134f4d64c8668fe7ec0816f33f8c481f13af`) | `CREATE`: `history/records/plumbogottlobite/2026-11-03T091301Z-antigravity-a67205.yaml` (`0638fda1d5ca3b4ce368ba332fb7fc57dee107417eb10e24ae766e5b51117d81`); `EDIT`: `history/records/plumbogottlobite/2026-11-03T101732Z-antigravity-eaa7f6.yaml` (`2895efb3a99cb6e2daf749ac87a3639ff007057e686232c671c68f01e8cc2031`) | `reviews/structured/20261103T091500Z-plumbogottlobite-round125-scientific-review/review.yaml` (`72dc6c76c72daa3b3ac8bb12bec5f3da0a9d3adb366cb3fb7e30d3659748fa87`) |
| `lazerckerite` | `cmmmech:lazerckerite` | `IMA:2022-113` | `Ag3.75Pb4.50(Sb7.75Bi4)S24` | Sb, Bi | `data/records/lazerckerite.yaml` (`e80ce9a78928a66dd0acee3d3b7b47e8be2b9f7ff9ae90d78bbc07a35cd30bdf`) | `CREATE`: `history/records/lazerckerite/2026-11-03T091303Z-antigravity-eb0f1a.yaml` (`f2820621e8f449f058c8ec92a4112700b8bad10f91762be0188df5622271ec30`); `EDIT`: `history/records/lazerckerite/2026-11-03T101757Z-antigravity-bc3b9b.yaml` (`a2da3b95e3d99fbaf01f4f8c6eb8d9774fffa1f2f93f2507e2a003d4a102a352`) | `reviews/structured/20261103T091500Z-lazerckerite-round125-scientific-review/review.yaml` (`280fc286d8df33508a469cd92eb81a5e4e9b8b50ee7150d4a6e669a14d9cb6ce`) |

## Bounded Frontier Accounting

- **Deferred External Single-Reference Candidates (`9`):** `carletonmooreite`, `changesite-y`, `chihmingite`, `ferroberaunite`, `gysinite-la`, `haleniusite-ce`, `ikranite`, `manganoschafarzikite`, `niasite`
- **Excluded Non-Critical Candidates (`1`):** `cesstibtantite` (discredited status `D`)
- **Multi-Source Held Candidates (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y`
- **Open Source Issues Tracked (`4`):** `#495`, `#496`, `#497`, `#498`
