# Round 124 Frontier Ingest Report (`2026-10-31`)

- **Cycle / Stage:** Cycle 6, Stage 1 (`add_records`)
- **Corpus Transition:** `668 -> 673` records (`+5` mineral records)
- **Canonical History Sidecars:** `1157 -> 1162` (`+5` `CREATE` sidecars)
- **Structured Scientific Reviews:** `906 -> 911` (`+5` per-record review bundles)
- **Source Investigation Dossier:**
  - `research/sources/round124-minerals/20261031T015000Z-source-investigation.json` (`896abccad090d9bb3f258cc2b6144323e1b1aae69e88550611b2eb5d59a5266e`)
  - `research/sources/round124-minerals/20261031T015000Z-source-investigation.md` (`8f3b2d8438f251351d1a566cc19c320f6f77257d13b30a3cf394b237e25feb3e`)

## Admitted Mineral Records (5)

| Slug | ID | IMA ID | Formula | Critical Element Link | Record Path & SHA-256 | History Sidecar & SHA-256 | Review Bundle & SHA-256 |
|---|---|---|---|---|---|---|---|
| `laurentthomasite` | `cmmmech:laurentthomasite` | `IMA:2018-157` | `Mg2K(Be2Al)Si12O30` | Be (Sc-bearing) | `data/records/laurentthomasite.yaml` (`9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859`) | `history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml` (`ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c`) | `reviews/structured/20261031T015200Z-laurentthomasite-round124-scientific-review/review.yaml` (`845c1ba753722395b9e4094dca00b962a35147945e7d86f92cfff6cfc8ea2b68`) |
| `wumuite` | `cmmmech:wumuite` | `IMA:2017-067a` | `KAl0.33W2.67O9` | W | `data/records/wumuite.yaml` (`6e7b83dce7f2776e5bd313041f98ee79401d003789765a9a52c747d58927d1bb`) | `history/records/wumuite/2026-10-31T014341Z-antigravity-a5dc6c.yaml` (`278dbc89230d8c4d4ed9b7064ddce89829b095c2a0d7e90506ddac40d0733bbd`) | `reviews/structured/20261031T015200Z-wumuite-round124-scientific-review/review.yaml` (`56ffcde51051cc9c9c6290a6e166e5ec18ac385e0544c826f6e4cbfe7f57fb30`) |
| `moabite` | `cmmmech:moabite` | `IMA:2020-092` | `NiFe3+(PO4)O` | Ni (Co-bearing) | `data/records/moabite.yaml` (`e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410`) | `history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml` (`ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587`) | `reviews/structured/20261031T015200Z-moabite-round124-scientific-review/review.yaml` (`84ee73047c504cebb863809dfd86ecd67ff9c6877d29899541b82d9892d69389`) |
| `vielleaureite-ce` | `cmmmech:vielleaureite-ce` | `IMA:2022-134` | `Mn2+Ce(MgAlMn2+)(Si2O7)(SiO4)F(OH)` | Ce, La, Mn, F | `data/records/vielleaureite-ce.yaml` (`5d184d309fa5d055701bf94b33a3cdd98f3f07cad6d89da68db26055905bd6d1`) | `history/records/vielleaureite-ce/2026-10-31T014425Z-antigravity-97a94c.yaml` (`0440a3673c0c5e1beccb20febc81929cd059a37e3459011601a4fe3ac63e7e4d`) | `reviews/structured/20261031T015200Z-vielleaureite-ce-round124-scientific-review/review.yaml` (`1ccb737ea56e20414a479e687da85b706ee1a0f1bbfd0ba1d31b7021ca459bb0`) |
| `xianhuaite-ce` | `cmmmech:xianhuaite-ce` | `IMA:2024-091` | `K2CeNb5O15` | Nb, Ce, La, Nd | `data/records/xianhuaite-ce.yaml` (`bded1436940de7290ef097aae277bae82aa543529d685bdb8c80c6a8be067f36`) | `history/records/xianhuaite-ce/2026-10-31T014447Z-antigravity-4ccc72.yaml` (`2ad06ecde6fadc591fd8759cb337f7668905b029749f4aec8599eb5e0c80a744`) | `reviews/structured/20261031T015200Z-xianhuaite-ce-round124-scientific-review/review.yaml` (`706b5cc2fe3a8fb50ab80ddae7064b6445af4cc61a076ae4686c6f34cb1b445c`) |

## Bounded Frontier Accounting

- **Deferred External Single-Reference Candidates (`8`):** `carletonmooreite`, `changesite-y`, `chihmingite`, `ferroberaunite`, `gysinite-la`, `haleniusite-ce`, `ikranite`, `johanngeorgenstadtite`
- **Excluded Non-Critical Candidates (`1`):** `cesstibtantite` (discredited status `D`)
- **Multi-Source Held Candidates (`7`):** `ashcroftine-y`, `priceite`, `franklinphilite`, `hydrokenomicrolite`, `irinarassite`, `monazite-gd`, `tveitite-y`
- **Open Source Issues Tracked (`4`):** `#495`, `#496`, `#497`, `#498`
