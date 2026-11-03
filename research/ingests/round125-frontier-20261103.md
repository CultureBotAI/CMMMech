# Round 125 Frontier Ingest Report (`2026-11-03`)

- **Cycle / Stage:** Cycle 7, Stage 1 (`add_records`)
- **Corpus Transition:** `673 -> 678` records (`+5` mineral records)
- **Canonical History Sidecars:** `1245 -> 1250` (`+5` `CREATE` sidecars, `0` `EDIT` sidecars)
- **Structured Scientific Reviews:** `981 -> 986` (`+5` per-record review bundles)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`61` full-PDF pages / `52` main-text pages) indexed into `154` UTF-8 text passages (`<= 1,800` bytes each; `217,676` passage bytes / `217,871` raw text bytes; `130` main-text passages) plus `14` single-page PNG table renders (`150` DPI via `mutool draw`).
- **Source Investigation Dossier:**
  - `research/sources/round125-minerals/20261103T085500Z-source-investigation.json` (`447fe421f89639f96ee4b71a90a9b2e057299c30e8ba1e4fd3ee8015c9e1e10d`)
  - `research/sources/round125-minerals/20261103T085500Z-source-investigation.md` (`350a8dca81be160c09ae895aa92b436f1c1d28ad5fdcd99bd2985dc816ec184a`)

## Admitted Mineral Records (5)

| Slug | ID | IMA ID | Formula | Critical Element Link | Record Path & SHA-256 | History Sidecar (`CREATE`) & SHA-256 | Review Bundle & SHA-256 |
|---|---|---|---|---|---|---|---|
| `johanngeorgenstadtite` | `cmmmech:johanngeorgenstadtite` | `IMA:2019-122` | `Ni2+4.5(AsO4)3` | Ni, As (Co-bearing) | `data/records/johanngeorgenstadtite.yaml` (`a4e644095310b2ee7e8b8c24da6bc566b1feb6d5b50e9fc4fc8dcbfdf73571f7`) | `CREATE`: `history/records/johanngeorgenstadtite/2026-11-03T091254Z-antigravity-ee9475.yaml` (`c305dac622731dfe05d794eca2c752672e2ab8186f850c6b5ea619b45e32e4d7`) | `reviews/structured/20261103T091500Z-johanngeorgenstadtite-round125-scientific-review/review.yaml` (`7272ee6a620b308cfdcb184fe72753158680ff48bc813a740294d7617bbd695c`) |
| `fengruiite` | `cmmmech:fengruiite` | `IMA:2024-045` | `[Ag6Sb2S7][Ag9CuS2Te2]` | Sb, Te (As-bearing) | `data/records/fengruiite.yaml` (`7e18b3121c37fcadcff3520ac76562298d4f661bdd1d8c0971c4d64133ed4e21`) | `CREATE`: `history/records/fengruiite/2026-11-03T091257Z-antigravity-552763.yaml` (`d5a8fea13aeb7d60f4441112d9343b1ba10f37f910e08dad82101335539a01ef`) | `reviews/structured/20261103T091500Z-fengruiite-round125-scientific-review/review.yaml` (`accf0cab5882691c2804d76057fed51aa9291a43315bfb3e9bd23ca8f368d523`) |
| `igelstromite` | `cmmmech:igelstromite` | `IMA:2021-035` | `Fe3+(SbPb)O4` | Sb (Mn-, As-bearing) | `data/records/igelstromite.yaml` (`903f0a10421a15dafc4199237de2e0b0ab84e737fd6ad80b6a1e990e213aeb42`) | `CREATE`: `history/records/igelstromite/2026-11-03T091259Z-antigravity-e7affb.yaml` (`7fd21fa696b312027cdbca31aa2f698bab46aae4626156d79c6ef9c136738ebc`) | `reviews/structured/20261103T091500Z-igelstromite-round125-scientific-review/review.yaml` (`9486f6b687af32154c2a34139a1666672794c0b30d2e8de904d565e65cd595dc`) |
| `plumbogottlobite` | `cmmmech:plumbogottlobite` | `IMA:2025-075` | `PbMg(VO4)(OH)` | V, Mg (Mn-bearing) | `data/records/plumbogottlobite.yaml` (`407e4844b3172be2713653d94e7f3837867c041932f6eedb8ddd95d91ceb024b`) | `CREATE`: `history/records/plumbogottlobite/2026-11-03T091301Z-antigravity-a67205.yaml` (`0638fda1d5ca3b4ce368ba332fb7fc57dee107417eb10e24ae766e5b51117d81`) | `reviews/structured/20261103T091500Z-plumbogottlobite-round125-scientific-review/review.yaml` (`ed1369875a30cda17f56ef61f2a2d470ffa91c5b3f729c78697b48f7e7c76ee7`) |
| `lazerckerite` | `cmmmech:lazerckerite` | `IMA:2022-113` | `Ag3.75Pb4.50(Sb7.75Bi4)S24` | Sb, Bi | `data/records/lazerckerite.yaml` (`311b208e76038e8f6bcc247273d4c82f7fa5d8785c9041706838e3b10c04b4b8`) | `CREATE`: `history/records/lazerckerite/2026-11-03T091303Z-antigravity-eb0f1a.yaml` (`f2820621e8f449f058c8ec92a4112700b8bad10f91762be0188df5622271ec30`) | `reviews/structured/20261103T091500Z-lazerckerite-round125-scientific-review/review.yaml` (`9f940f27308ba0dac82b70088032541aeefa308c91b486354018f21687bd7153`) |

## Bounded Frontier Accounting

- **Deferred External Single-Reference Candidates (`9`):** `carletonmooreite`, `changesite-y`, `chihmingite`, `ferroberaunite`, `gysinite-la`, `haleniusite-ce`, `ikranite`, `manganoschafarzikite`, `niasite`
- **Excluded Non-Critical Candidates (`1`):** `cesstibtantite` (discredited status `D`)
- **Multi-Source Held Candidates (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y`
- **Open Source Issues Tracked (`4`):** `#495`, `#496`, `#497`, `#498`
