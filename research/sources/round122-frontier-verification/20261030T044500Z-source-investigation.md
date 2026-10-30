# Round 122 Source Investigation & Bounded-Frontier Verification (`round122-frontier-verification-20261030T044500Z`)

- **Generated at:** `2026-10-30T04:45:00Z`
- **Cycle / Stage:** Cycle 4, Stage 1 (`add_records`) — Round 122
- **Trusted base commit:** `4f543693bee75b97389de4d4c915a1e451297f1f` (`Unify agent instructions for Claude Code, Codex and Antigravity (#853)`)
- **Predecessor Cycle 4 Stage 1 checkpoints:**
  - **Round 120 (PR #837):** `7918502cee65b588f4e0e7cf5bce94d49ba55e51` (`16` records admitted)
  - **Round 121 (PR #841):** `2d8ce7a1fee97b74098a1faf5a82481ee115123d` / reviewed head `54bce1c96bcc6e5b7fe2f66da0a94bda646038ef` (`1` record admitted: `monteregianite-y`; remediation issue `#842` closed)

## 1. Investigation Scope

This investigation executes the repeated bounded-frontier verification required by `.claude/skills/cmmmech-discover-sources/SKILL.md` and `.claude/skills/cmmmech-add-record/SKILL.md` to determine whether any further evidence-backed critical mineral or material candidate in the Cycle 4 Stage 1 bounded local frontier can be admitted following Round 120 (PR #837, `16` records) and Round 121 (PR #841, `1` record: `monteregianite-y`).

Specifically, this audit verifies:
1. All local primary-source download directories (`/private/tmp/cmm-round117-research`, `/private/tmp/cmm-round118-research`, `/private/tmp/cmm-round119-research`, `/private/tmp/cmm-round120-research`) and `/private/tmp/**/*.pdf`.
2. All extracted source texts and bounded passages (`<= 1,907` bytes each) in `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/reports/mech-resume-20261024/cmm-bounded-source-text/`.
3. A complete `6,730`-file repository deduplication inventory across `data/records`, `research`, `reviews`, and `history` (including hidden and `.gitignore`-ignored files and resolving symlinks via Python `os.walk(..., followlinks=True)`, documented alongside the host `rg` binary check).
4. Exact September 2026 IMA Master List entries (`ima-round118.full.txt` pages `77`, `89`, `98`, `124`, `127`, `137`, `147`, `178`, `222`) and primary-literature availability for every remaining deferred or excluded candidate across Rounds 118–121.

## 2. Local Primary-Source Archive & Bounded-Text Audit

| Archive / Directory | Files Present | Status & Disposition |
| --- | --- | --- |
| `/private/tmp/cmm-round117-research` | `0` files (`0` PDFs) | Cleared by macOS periodic `/tmp` cleanup prior to `2026-10-30`; all `15` admissible candidates curated in Round 118 (PR #810). |
| `/private/tmp/cmm-round118-research` | `0` files (`0` PDFs) | Cleared by macOS periodic `/tmp` cleanup prior to `2026-10-30`; all `15` admissible candidates curated in Round 118 (PR #810). |
| `/private/tmp/cmm-round119-research` | `0` files (`0` PDFs) | Cleared by macOS periodic `/tmp` cleanup prior to `2026-10-30`; all `15` admissible candidates curated in Round 119 (PR #824). |
| `/private/tmp/cmm-round120-research` | `0` files (`0` PDFs) | Cleared by macOS periodic `/tmp` cleanup on `2026-10-27`; all `16` Round 120 candidates curated in PR #837 and remaining Round 120/121 sources extracted to `cmm-bounded-source-text/` prior to cleanup. |
| `cmm-bounded-source-text/cm16-561` (`CM16_561.pdf`, Chao 1978, *Can. Mineral.* 16:561–565) | `9` bounded passages (`<= 1,907` B) + `5`-page text | Curated and merged in Round 121 (PR #841, `data/records/monteregianite-y.yaml`). |
| `cmm-bounded-source-text/am72-365` (`AM72_365.pdf`, Ghose, Sen Gupta, & Campana 1987, *Am. Mineral.* 72:365–374) | `10`-page text (lines `1–50` bounded excerpt `<= 2` KB) | Marked with `candidate_text_misses: ["monteregianite-y"]` in `summary.json` because the embedded OCR layer dropped the accented `é` in `montérégianite` (`Montregianite, Nao&YrSiruOrr. 10H2O`). Verified and curated into `data/records/monteregianite-y.yaml` in Round 121 (PR #841). |
| `cmm-bounded-source-text/ima-round118` & `ima-round119` (`ima_pages_round118.pdf` / `ima_pages_round119.pdf`, September 2026) | `8` bounded passages (`<= 857` B) + `244`-page text | Bounded single-entry extracts verified for pages `77`, `89`, `98`, `124`, `127`, `137`, `147`, `178`, and `222`. |

## 3. Repository Deduplication Inventory (`6,730` Files)

Because `rg` (`ripgrep`) is not installed on this macOS host (`rg`, `/usr/local/bin/rg`, `/opt/homebrew/bin/rg`, and `/usr/local/Caskroom/miniforge/base/bin/rg` all return `exit 127`), we executed the equivalent complete inventory required by `.claude/skills/cmmmech-discover-sources/SKILL.md` using Python `os.walk(..., followlinks=True)` across `data/records`, `research`, `reviews`, and `history` (including hidden and `.gitignore`-ignored files, with `0` inaccessible paths):
- **Total files scanned:** `6,730`
- **Curated material records (`data/records/*.yaml`):** `663`
- **History sidecars (`history/records/**/*.yaml`):** `1,013`
- **Structured review bundles (`reviews/structured/*`):** `844`

## 4. Complete Candidate Verification Ledger (Rounds 118–122)

| Candidate ID | Preferred Label | IMA Identifier & Status | IMA Formula (Sept 2026) | IMA Page | Standalone Record in `data/records/` | Associated Mentions in `data/records/` | Disposition & Evidence Basis |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `monteregianite-y` | `monteregianite-(Y)` | `1987 s.p.` (`Rn`) | `KNa2YSi8O19·5H2O` | p. 147 | Yes (`data/records/monteregianite-y.yaml`) | Self (`monteregianite-y.yaml`) | **Admitted in Round 121 (PR #841)** (`2d8ce7a1fee97b74098a1faf5a82481ee115123d`). |
| `cesstibtantite` | `cesstibtantite` | Historical `IMA:1980-068` (discredited/reclassified) | Discredited / reclassified into `hydrokenomicrolite` (`IMA:2011-103`, `(☐,H2O)2Ta2(O,OH)6(H2O)`) and `hydroxycalciomicrolite` (`IMA:2013-073`, `Ca1.5Ta2O6(OH)`) | p. 98 | No | `data/records/kimrobinsonite.yaml` | **Excluded (discredited species):** Absent as an accepted mineral in the Sept 2026 IMA Master List; replacement species (`hydrokenomicrolite`, `hydroxycalciomicrolite`) have no local primary full-text PDFs on disk. |
| `protasite` | `protasite` | `IMA:1984-001` (`A`) | `Ba(UO2)3O3(OH)2(H2O)3` | p. 178 | No | None | **Held pending primary source:** 1987 structure paper (*Am. Mineral.* 72:1230–1238) inspected in Round 121; 1986 type description (Pagoaga, Appleman, & Stewart 1986, *Mineral. Mag.* 50:125–128) is not locally available. |
| `lepersonnite-gd` | `lepersonnite-(Gd)` | `1987 s.p.` (`Rn`) | `[Ca0.5Gd0.5(H2O)18(OH)1.5][Gd(UO2)12(SiO3OH)2(CO3)4(OH)10O2(H2O)5]` | p. 124 | No | None | **Held pending primary source:** 1982 description (Deliens & Piret 1982, *Can. Mineral.* 20:231–238) inspected in Round 121; 2025 structure/formula redefinition (*Mineral. Mag.* 89 (2025), 549) is not locally available. |
| `lokkaite-y` | `lokkaite-(Y)` | `1987 s.p.` (`Rn`) | `CaY4(CO3)7·9H2O` | p. 127 | No | None | **Held pending primary source:** 1986 Kirigo supplemental study (Nagai & Miyawaki 1986, *Am. Mineral.* 71:1028–1033) inspected in Round 121; sole IMA-cited type description (Perttunen 1970/1971, *Bull. Geol. Soc. Finland* 43:67–72) is not locally available. |
| `haiweeite` | `haiweeite` | `1962 s.p.` (`A`) | `Ca(UO2)2(Si5O12)(OH)2(H2O)6·2H2O` | p. 89 | No | `data/records/coutinhoite.yaml`, `data/records/weeksite.yaml` | **Held pending primary source:** 1959 description (McBurney & Murdoch 1959, *Am. Mineral.* 44:839–843) inspected in Round 118; 2013 structure/formula revision (Plášil et al. 2013, *Am. Mineral.* 98:718–723) is not locally available. |
| `fourmarierite` | `fourmarierite` | `G` (`1924`) | `Pb1-xO3-2x(UO2)4(OH)4+2x·4H2O` | p. 77 | No | `data/records/richetite.yaml` | **Held pending primary source:** 2000 synthetic structure paper (Li & Burns 2000, *Can. Mineral.* 38:737–749) inspected in Round 118; 1924 Buttgenbach original type description (*Ann. Soc. Géol. Belgique* 47:C41–C43) is not locally available. |
| `masuyite` | `masuyite` | `G` (`1947`) | `Pb(UO2)3O3(OH)2(H2O)3` | p. 137 | No | `data/records/richetite.yaml` | **Held pending primary source:** 1947 Vaes original type description (*Ann. Soc. Géol. Belgique* 70:B212–B225) and local full-text verification of the 1999 structure paper (*Can. Mineral.* 37 (1999), 1483 on IMA p. 137 vs Round 118 note citing p. 1003) are not locally available. |
| `tsumoite` | `tsumoite` | `IMA:1972-010a` (`A`) | `BiTe` | p. 222 | No | None | **Held pending primary source:** 1978 description (Shimazaki & Ozawa 1978, *Am. Mineral.* 63:1162–1165) inspected in Round 118; paywalled 1979 crystal-structure paper (Yamana, Kihara, & Matsumoto 1979, *Acta Crystallogr.* B35:147–149) is not locally available. |

## 5. Carried-Forward Open Source & Infrastructure Issues

- **Open Source-Tracking Issues (`research` / `data`):**
  - `#495` — Dry Creek, Montana coalbed methane produced-water and coal-interburden study
  - `#496` — Lower Kittanning coal bed microbial consortium / `16S rRNA` primary source
  - `#497` — Fort Union Formation PRB coal and produced-water primary source
  - `#498` — Illinois Basin coal / coal-waste primary source
- **Open Stage 6 (`implement_infrastructure`) Intake Tasks (`INFRA_TASKS.md`):**
  - `cmmmech-infra-0010` (`#839`) — Claim-evidence pre-commit check for verbatim source quotes, locator tokens, and unit/temperature/pH/recovery parity
  - `cmmmech-infra-0011` (`#840`) — Bounded page/passage PDF extractor and context-budget guard for primary-source curation

## 6. Bounded-Frontier Exhaustion Determination

- **`bounded_frontier_exhausted`: `true`** — All locally available primary-source PDFs and bounded text passages in the Cycle 4 Stage 1 frontier have been audited and curated (`16` records in Round 120 PR #837 + `1` record in Round 121 PR #841 = `17` records admitted in Cycle 4 Stage 1, bringing `data/records/` to `663` records). Zero uncurated local primary-source PDFs remain on disk, and every remaining candidate is either discredited (`cesstibtantite`) or explicitly held pending unacquired external/paywalled primary literature (`protasite`, `lepersonnite-gd`, `lokkaite-y`, `haiweeite`, `fourmarierite`, `masuyite`, `tsumoite`; plus `#495`–`#498`).
- **`source_exhaustion_claimed`: `false`** — Global mineralogical and scientific source exhaustion across future cycles is not claimed.
