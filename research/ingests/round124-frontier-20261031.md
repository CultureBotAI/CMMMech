# Round 124 Frontier Ingest Report (`2026-10-31`)

- **Cycle / Stage:** Cycle 6, Stage 1 (`add_records`)
- **Corpus Transition:** `668 -> 673` records (`+5` mineral records)
- **Canonical History Sidecars:** `1157 -> 1167` (`+5` `CREATE` sidecars, `+5` `EDIT` sidecars)
- **Structured Scientific Reviews:** `906 -> 911` (`+5` per-record review bundles)
- **Bounded Passage Indexing (`scripts/index_bounded_pdf_passages.py`):** `5` open-access *European Journal of Mineralogy* PDFs (`57` full-PDF pages / `48` main-text pages) indexed into `153` UTF-8 text passages (`<= 1,800` bytes each; `222,547` passage bytes / `222,733` raw text bytes; `120` main-text passages) plus `11` single-page PNG table renders (`150` DPI via `mutool draw`).
- **Source Investigation Dossier:**
  - `research/sources/round124-minerals/20261031T015000Z-source-investigation.json` (`e96414f9ad3c4b28ddbfbc8c30d030ad25666e2df2e673fb209ef1ef2d1605b6`)
  - `research/sources/round124-minerals/20261031T015000Z-source-investigation.md` (`fe0a768099b9a6f53cb1f365f5e45cadfe9e5b21ec31e5e8b40ac7325382a1f1`)

## Admitted Mineral Records (5)

| Slug | ID | IMA ID | Formula | Critical Element Link | Record Path & SHA-256 | History Sidecars (`CREATE` & `EDIT`) & SHA-256 | Review Bundle & SHA-256 |
|---|---|---|---|---|---|---|---|
| `laurentthomasite` | `cmmmech:laurentthomasite` | `IMA:2018-157` | `Mg2K(Be2Al)Si12O30` | Be (Sc-bearing) | `data/records/laurentthomasite.yaml` (`145c3ad84325ec6470ebb305ff4648a3b198ad9adda1412116e93f03479cb019`) | `CREATE`: `history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml` (`ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c`); `EDIT`: `history/records/laurentthomasite/2026-10-31T025403Z-antigravity-87d29f.yaml` (`ee1fde809529f4fe835a5bc83d73ed02ae21abbc99ce651162b7576c26c7ed09`) | `reviews/structured/20261031T035200Z-laurentthomasite-round124-scientific-review/review.yaml` (`8297ecb8c814c1856c2cec00538018039cffcfcb9d09b456f70394c2c2b24e2e`) |
| `wumuite` | `cmmmech:wumuite` | `IMA:2017-067a` | `KAl0.33W2.67O9` | W | `data/records/wumuite.yaml` (`303d5e7ca9d113f8db3ca26550f3baa8040bdef50f1dbe0f96a1cb299b056c77`) | `CREATE`: `history/records/wumuite/2026-10-31T014341Z-antigravity-a5dc6c.yaml` (`278dbc89230d8c4d4ed9b7064ddce89829b095c2a0d7e90506ddac40d0733bbd`); `EDIT`: `history/records/wumuite/2026-10-31T025433Z-antigravity-c4f156.yaml` (`a9279a871035ca946d463c371d846eae859293f3a7eae92c8a63d7ea4efe43ae`) | `reviews/structured/20261031T035200Z-wumuite-round124-scientific-review/review.yaml` (`7403bbbfaa08dbfcaa70f1336a219030bce63562f008f13bc6bb40c1264591a4`) |
| `moabite` | `cmmmech:moabite` | `IMA:2020-092` | `NiFe3+(PO4)O` | Ni (Co-bearing) | `data/records/moabite.yaml` (`c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716`) | `CREATE`: `history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml` (`ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587`); `EDIT`: `history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml` (`ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b`) | `reviews/structured/20261031T035200Z-moabite-round124-scientific-review/review.yaml` (`9e017233cff7c2c8d00281a0197aa3fa3b04a65ade1784bc9545dac8e5695aa9`) |
| `vielleaureite-ce` | `cmmmech:vielleaureite-ce` | `IMA:2022-134` | `Mn2+Ce(MgAlMn2+)(Si2O7)(SiO4)F(OH)` | Ce, La, Mn, F | `data/records/vielleaureite-ce.yaml` (`2c503fac8dc7f2eba571a56470c0907358ceab2fbb0ba2a2cabc5c677d8ca5c8`) | `CREATE`: `history/records/vielleaureite-ce/2026-10-31T014425Z-antigravity-97a94c.yaml` (`0440a3673c0c5e1beccb20febc81929cd059a37e3459011601a4fe3ac63e7e4d`); `EDIT`: `history/records/vielleaureite-ce/2026-10-31T025532Z-antigravity-9fb7bf.yaml` (`585153c3917ba0786840f792d0754effba7301ec5588e6ba25a134bc142c2c40`) | `reviews/structured/20261031T035200Z-vielleaureite-ce-round124-scientific-review/review.yaml` (`a85eb88dbd0139bcc27568e09c22634de48ec38d855fbea98d7e4d6cc22cdc82`) |
| `xianhuaite-ce` | `cmmmech:xianhuaite-ce` | `IMA:2024-091` | `K2CeNb5O15` | Nb, Ce, La, Nd | `data/records/xianhuaite-ce.yaml` (`6c10184ccc5d687d3a4ca89b77766c5e5311b50e4696064b8d20626d7d301ec8`) | `CREATE`: `history/records/xianhuaite-ce/2026-10-31T014447Z-antigravity-4ccc72.yaml` (`2ad06ecde6fadc591fd8759cb337f7668905b029749f4aec8599eb5e0c80a744`); `EDIT`: `history/records/xianhuaite-ce/2026-10-31T025602Z-antigravity-e34dd7.yaml` (`2ccf0761406f9542b33af6d12fed0dfaa2d4f6ba9f62466564f5bd3baec603b7`) | `reviews/structured/20261031T035200Z-xianhuaite-ce-round124-scientific-review/review.yaml` (`c9c3b6111b6bf743d4f09b9b8e2221bfbb74419d13926fac5ed95906caed14b7`) |

## Bounded Frontier Accounting

- **Deferred External Single-Reference Candidates (`8`):** `carletonmooreite`, `changesite-y`, `chihmingite`, `ferroberaunite`, `gysinite-la`, `haleniusite-ce`, `ikranite`, `johanngeorgenstadtite`
- **Excluded Non-Critical Candidates (`1`):** `cesstibtantite` (discredited status `D`)
- **Multi-Source Held Candidates (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y`
- **Open Source Issues Tracked (`4`):** `#495`, `#496`, `#497`, `#498`
