# Round 122 bounded-frontier verification and Cycle 4 Stage 1 (`add_records`) completion report

Prepared `2026-10-30T04:50:00Z` at trusted base `4f543693bee75b97389de4d4c915a1e451297f1f` (`origin/main`, following Round 120 PR #837 `7918502cee65b588f4e0e7cf5bce94d49ba55e51` and Round 121 PR #841 `2d8ce7a1fee97b74098a1faf5a82481ee115123d`).

## Summary

This Round 122 bounded-frontier verification checkpoint completes the Cycle 4 Stage 1 (`add_records`) discovery goal in continuation conversation `5d564102-201c-473a-960a-1d0caa99b350` (`[MECH-COMMIT-FIRST-20261030-CMMMECH]`):

1. **Cumulative Cycle 4 Stage 1 (`add_records`) Admissions (`17` records across PR #837 + PR #841)**:
   - **Round 120 ([PR #837](https://github.com/CultureBotAI/CMMMech/pull/837), `7918502cee65b588f4e0e7cf5bce94d49ba55e51`)**: Admitted `16` critical-mineral records (`agardite-ce`, `agardite-nd`, `calciouranoite`, `chernovite-y`, `chistyakovaite`, `clarkeite`, `cousinite`, `coutinhoite`, `demesmaekerite`, `fontanite`, `francoisite-ce`, `gasparite-ce`, `gauthierite`, `kamotoite--(y)`, `kimrobinsonite`, `kobeite-y`), expanding the corpus from `646` to `662` records.
   - **Round 121 ([PR #841](https://github.com/CultureBotAI/CMMMech/pull/841), `2d8ce7a1fee97b74098a1faf5a82481ee115123d` / reviewed head `54bce1c96bcc6e5b7fe2f66da0a94bda646038ef`)**: Admitted `1` additional critical-mineral record ([Monteregianite-(Y)](../../data/records/monteregianite-y.yaml), `cmmmech:monteregianite-y`, IMA `1987 s.p.`, status `Rn`, `KNa2YSi8O19·5H2O`), remediated via [issue #842](https://github.com/CultureBotAI/CMMMech/issues/842), expanding the corpus from `662` to `663` records (`1,013` history sidecars, `844` structured review bundles).
   - **Round 122 (this checkpoint)**: `0` additional records admitted after repeated verification of the local source archives (`/private/tmp/cmm-round117-research` through `/private/tmp/cmm-round120-research`, verified at `0` files), `cmm-bounded-source-text/` (`4` extracted source texts, `17` bounded passages `<= 1,907` B), the September 2026 IMA Master List, and all `6,730` files across `data/records`, `research`, `reviews`, and `history`.
2. **Excluded Candidate (`1`)**:
   - `cesstibtantite` (historical `IMA:1980-068`): verified absent as an accepted mineral in the September 2026 IMA Master List (`candidate_text_misses: ["cesstibtantite"]`), having been discredited/reclassified into `hydrokenomicrolite` (`IMA:2011-103`, IMA p. 98) and `hydroxycalciomicrolite` (`IMA:2013-073`, IMA p. 98), neither of which has local primary full-text PDFs on disk.
3. **Explicitly Held Candidates (`7` across Rounds 118–122 pending unacquired external/paywalled primary sources)**:
   - `protasite` (`IMA:1984-001`, status `A`, `Ba(UO2)3O3(OH)2(H2O)3`, IMA p. 178): 1987 structure paper (*Am. Mineral.* 72:1230–1238) inspected in Round 121; held pending full-text acquisition of the 1986 type description (Pagoaga, Appleman, & Stewart 1986, *Mineral. Mag.* 50:125–128).
   - `lepersonnite-gd` (`1987 s.p.`, status `Rn`, `[Ca0.5Gd0.5(H2O)18(OH)1.5][Gd(UO2)12(SiO3OH)2(CO3)4(OH)10O2(H2O)5]`, IMA p. 124): 1982 holotype description (Deliens & Piret 1982, *Can. Mineral.* 20:231–238) inspected in Round 121; held pending full-text acquisition of the 2025 structure/redefinition paper (*Mineral. Mag.* 89:549).
   - `lokkaite-y` (`1987 s.p.`, status `Rn`, `CaY4(CO3)7·9H2O`, IMA p. 127): 1986 Kirigo supplemental study (Nagai & Miyawaki 1986, *Am. Mineral.* 71:1028–1033) inspected in Round 121; held pending full-text acquisition of the sole IMA-cited type description (Perttunen 1970/1971, *Bull. Geol. Soc. Finland* 43:67–72).
   - `haiweeite` (`1962 s.p.`, status `A`, `Ca(UO2)2(Si5O12)(OH)2(H2O)6·2H2O`, IMA p. 89): 1959 description (McBurney & Murdoch 1959, *Am. Mineral.* 44:839–843) inspected in Round 118; held pending full-text acquisition of the 2013 crystal-structure and formula revision (Plášil et al. 2013, *Am. Mineral.* 98:718–723).
   - `fourmarierite` (`G`, `1924`, `Pb1-xO3-2x(UO2)4(OH)4+2x·4H2O`, IMA p. 77): 2000 synthetic crystal-structure paper (Li & Burns 2000, *Can. Mineral.* 38:737–749) inspected in Round 118; held pending full-text acquisition of the 1924 Buttgenbach original type description (*Ann. Soc. Géol. Belgique* 47:C41–C43).
   - `masuyite` (`G`, `1947`, `Pb(UO2)3O3(OH)2(H2O)3`, IMA p. 137): held pending full-text acquisition of the 1947 Vaes original type description (*Ann. Soc. Géol. Belgique* 70:B212–B225) and local full-text verification of the 1999 structure paper (*Can. Mineral.* 37 (1999), 1483 on IMA p. 137 vs Round 118 note citing p. 1003).
   - `tsumoite` (`IMA:1972-010a`, status `A`, `BiTe`, IMA p. 222): 1978 description (Shimazaki & Ozawa 1978, *Am. Mineral.* 63:1162–1165) inspected in Round 118; held pending full-text acquisition of the paywalled 1979 crystal-structure paper (Yamana, Kihara, & Matsumoto 1979, *Acta Crystallogr.* B35:147–149).
4. **Carried-Forward Open Source & Infrastructure Issues**:
   - Open coalbed/coal-waste primary-source issues `#495`, `#496`, `#497`, and `#498`.
   - Open Stage 6 (`implement_infrastructure`) intake items in [INFRA_TASKS.md](../../INFRA_TASKS.md): `cmmmech-infra-0010` ([issue #839](https://github.com/CultureBotAI/CMMMech/issues/839)) and `cmmmech-infra-0011` ([issue #840](https://github.com/CultureBotAI/CMMMech/issues/840)).

## Source and review provenance

- [20261030T044500Z-source-investigation.json](../../research/sources/round122-frontier-verification/20261030T044500Z-source-investigation.json) — SHA-256 `8accc3df2028b798f2c225e2fe64cf517709d8bffe0fa0b79b50c0a9d36e25af`.
- [20261030T044500Z-source-investigation.md](../../research/sources/round122-frontier-verification/20261030T044500Z-source-investigation.md) — SHA-256 `4ff73fb3cec51c72de6f527614d35712d79555e250a9459bfe8ec96af63aa92e`.
- [20261025T055800Z-source-investigation.json](../../research/sources/round121-minerals/20261025T055800Z-source-investigation.json) — SHA-256 `301ec350bec0b21f40f38aafb5a06b1caac82520e11dc72a6682416f8f469f73`.
- [20261025T055800Z-source-investigation.md](../../research/sources/round121-minerals/20261025T055800Z-source-investigation.md) — SHA-256 `0240946d224d472fa2f872d5ab4cdb9b6bf85a9ee6390fedd1ffbf420b4cf6bc`.
- [20261025T065100Z-monteregianite-y-round121-remediated-scientific-review/review.yaml](../../reviews/structured/20261025T065100Z-monteregianite-y-round121-remediated-scientific-review/review.yaml) — SHA-256 `64d50f6f7f3dabc895c0244f46f8e1acdbb798d3c20c6235de967a843ac909df`.
- [20261025T065100Z-monteregianite-y-round121-remediated-scientific-review/review.md](../../reviews/structured/20261025T065100Z-monteregianite-y-round121-remediated-scientific-review/review.md) — SHA-256 `bd8e377a2622aa57f25d775316633981caa8cf4e3017236f8fa12ab0d47ce1d5`.

## Scope and frontier status

The bounded local source frontier for Cycle 4 Stage 1 (`add_records`) is exhausted (`bounded_frontier_exhausted: true`), authorizing Stage 1 completion (`goal_complete: true` after merge and verification of this checkpoint). Global mineralogical and scientific source exhaustion across future cycles is not claimed (`source_exhaustion_claimed: false`).
