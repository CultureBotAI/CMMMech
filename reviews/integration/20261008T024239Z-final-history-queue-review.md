# Final history and queue integration adversarial review

## Record of review

UTC timestamp: **2026-10-08T02:42:39Z**, read from the system UTC clock. Independent reviewer: `/root/queue_admission_audit` (Codex, GPT-6), separate from native implementation/adoption curator `/root/history_cmm` and coordinating publisher `/root`.

Worktree: `/private/tmp/CMMMech-history-queue-20261008`; branch `integration/history-queue-20261008`; HEAD `c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1`. The reviewed implementation and adoption are working changes, including new untracked native files, sessions and review artifacts; they are not claimed to be committed at HEAD. HEAD and published main `842edc17fc603831c6ab56fd0ef1d813416d3ea5` have identical tree `f1031f7f18d5da43681d6f1ac2791f7c3a3bfe9b`. The current tracked binary diff SHA-256 is `e528075a36610601c18b691b492983a1ea5057341678e2ccb9abf87d659ce2e5`. The file hashes below additionally identify untracked implementation/session bytes.

## Scope and authority

Reviewed the combined native history implementation, CLI/schema/validator changes, tests, local record-review skill, `CLAUDE.md`, `README.md`, record guide, local gate and CI trusted-base wiring; reviewed all three actual adoption records/sessions through separate per-record artifacts. Reviewed the queue plan and current dossier against published CLAW governance/queue policy at `849f336e025510316a5f235eb0af8547b8bd50cc`, retained as the repository pin. Supported governance, shepherd and merge-queue workflows were inspected without editing their canonical copies. This review makes no claim of new literature acquisition, fleet-wide rollout completion, OAuth/model liveness, automatic admission, or already-completed native merge execution.

Earlier integration artifacts are immutable snapshots. In particular, [the combined 02:32 review](20261008T023200Z-combined-history-review.md) preceded discovery of inherited CI-base interference in synthetic tests. This final round includes that subsequent finding and its repair; its earlier acceptance is not treated as proof of the later state.

## Findings and corrections

- **Critical:** none outstanding in the reviewed scope.
- **Major:** none outstanding in the reviewed scope. [Issue #8](https://github.com/CultureBotAI/CMMMech/issues/8) previously demonstrated an actual ancestor-symlink bypass of Git's append-only comparison. The repaired reader, creator and discovery reject all lexical sidecar symlink components before reading/writing, including in-repository and dangling aliases. The committed-backing-file regression is retained. Earlier reproduction and independent repair results are preserved in the 02:17 and 02:20 artifacts.
- **Major, corrected:** [issue #10](https://github.com/CultureBotAI/CMMMech/issues/10) was exposed when the complete gate inherited a real repository `CMMMECH_HISTORY_BASE`; standalone synthetic repositories could not resolve that unrelated SHA. The module-local autouse fixture now removes inherited state only for isolated history tests. A new real-Git regression explicitly sets its own reviewed base, proves a committed rewrite fails through the CLI environment default, and proves explicit `--base HEAD` overrides it. The separate `tests/test_check.py` integration regression still supplies its own event base to the actual child gate, so this repair does not disable or mock production enforcement. Documentation now accurately defines standalone mode as having neither a flag nor the environment variable. No production behavior or record/session bytes changed for this repair.
- **Minor:** no additional required correction identified.
- **Informational:** [issue #7](https://github.com/CultureBotAI/CMMMech/issues/7) semantics remain explicit: new sidecars must identify an existing current file when a reviewed base is supplied; immutable historical sessions may remain after a target is removed. Unattached sessions remain allowed during the documented scaffold-then-attach workflow. This is advisory history coverage, not an invented mandatory completeness claim.

No artificial review issue is proposed where no further defect was found. The reviewer changed only review artifacts.

## Code and provenance assessment

The schema preserves PR #9's native inline `CurationEvent` contract and adds a distinct `history_refs` list. Canonical history/shared schemas are imported as governed resources. Validation checks duplicate references, strict sidecar content, exact kind/slug/target correspondence, current UTC-compatible session metadata, closed nested objects and complete details. Scaffolding requires a real target, records actual current UTC, and atomically links a complete temporary file without clobbering an existing session. Appending its printed reference is a separate reviewed record edit.

Git comparison rejects modifications/deletions of published YAML history with rename detection disabled; it fails on unavailable bases. CI provides the PR base, merge-group base or push-before SHA and fetches complete history. The workflow retains combined-event checkout behavior, unconditional `validate-strict`, `pull_request`, `push` and `merge_group` triggers. The local gate propagates the trusted base and defaults to HEAD locally. The actual-gate regression commits a historical rewrite and demonstrates that the baseline fails while identical HEAD-controlled bytes pass, proving why the event base is required.

The three actual records preserve all original baseline bytes as exact prefixes, and all scientific values are identical after removing only the two new metadata fields. Sessions record present Codex/GPT-6 adoption, not invented earlier authorship, and link unchanged earlier scientific reviews through immutable URLs and verified hashes. Separate reviews:

- [Cobalt](../records/cobalt/20261008T024127Z.md): accept with limitations.
- [Neodymium](../records/neodymium/20261008T024127Z.md): accept with limitations.
- [Palladium](../records/palladium/20261008T024127Z.md): accept with limitations.

`README.md`, `CLAUDE.md` and the updated local skill correctly distinguish inline events, canonical sessions and scientific reviews. They require present truthful provenance and preserve limitations on unverified capabilities. No fresh scientific verification is implied by this metadata-only adoption.

## Queue evidence assessment

The exact independently reviewed plan is retained in [queue-20261008](queue-20261008/README.md), with plan SHA-256 `c5f301d7bf2cd71bb110378bd1ad77f21575a5e7e73ae5fb0cdd07c398a25bd5`. The supported apply receipt and check confirm active main-only ruleset **24692449**, required Actions check **validate-strict** (integration 15368), pull-request requirement, **no bypass actors**, squash/ALLGREEN merge queue and enabled auto-merge. Approval count remains zero; this review does not invent a platform approval requirement or substitute the writer App for independent review. Previously measured real push run **37717750857**, job **113118075562**, passed `validate-strict` on published main. Effective-main API rules were independently checked after apply and came from this managed ruleset; the supported check reports `unchanged`.

The readiness dossier confines credentials to names and installation/permission metadata. Secret presence alone was not treated as installation proof. Controlled deterministic [run 37718300374](https://github.com/CultureBotAI/CMMMech/actions/runs/37718300374) independently showed `rows: []`, `errors: []`, `admitted: 0`, `main_integrity: passed`, and the token-revocation post step. It proves a repository-scoped writer App token could be minted and revoked, with no open-PR admission. It does not prove an automatic admission or merge-group run. The canonical shepherd remains manual and comment-only; configured model/OAuth-secret-name availability is distinct from liveness. No model/provider invocation was performed. Reviewer App selection for CMMMech remains unestablished and is not claimed.

## Validation evidence

- Independent affected checks under `CMMMECH_HISTORY_BASE=c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1`: `uv run --locked pytest -q tests/test_history.py tests/test_check.py` — **51 passed in 35.65 s**.
- Independent three-file record validation — **3 records, 0 failures**.
- Independent `uv run --locked cmmmech validate-history --base 842edc17fc603831c6ab56fd0ef1d813416d3ea5` — **3 sidecars, 0 errors**.
- Independent `uv run --locked cmmmech validate --require-records` — **3 records, 0 failures**.
- Independent `bash scripts/check_vendored_sync.sh` — **18 governed artifacts match** the pinned revision; canonical payloads remain unchanged.
- Independent `git diff --check` — passed.
- Implementer-reported complete gate with actual `CMMMECH_HISTORY_BASE=c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check` — lint passed, **215 passed, 3 skipped**, 3 records with 0 failures, 3 histories with 0 errors. Skips are empty optional-command parameter cases, not history gates. Independent affected checks above corroborate the repaired history/CI behavior without claiming the reviewer reran this full suite.

## Remaining operational work and verdict

**Accept for PR publication and native queue verification**, with no outstanding critical/major code or provenance finding. This is not a claim that the integration is already merged. After publishing the reviewed bytes, retain passing required CI, the exact reviewed PR head, actual queue admission, merge-group SHA and successful `merge_group` Actions run, final merged commit, post-merge integrity/configuration check and branch cleanup in issue #3. If subsequent source/record edits occur, review their changed state before queue admission. Fleet-wide convergence belongs to CLAW #580 and the separate worker; it is not silently declared complete here. Canonical shepherd/model execution is not required to fabricate proof for this bounded integration.

## Reviewed file hashes

| Path | SHA-256 |
| --- | --- |
| `.claude/skills/review-record/SKILL.md` | `cdd500f4953cc25efd46031128f09b45d3fe7bae3775e4641981ec9a8a3d5382` |
| `.github/workflows/validate-strict.yaml` | `94e104b93ac4111bb591dc7769da933d98ea661192aac24bfda2acf2af31d918` |
| `CLAUDE.md` | `9b6cb043b24b9088b140197ad060b1433145bf4140a745c816c80a4b32bdc161` |
| `README.md` | `8d4498007704dbd86e2c73e0df510989e416cf7fc088082437b9ddb8c49c826a` |
| `data/records/cobalt.yaml` | `970507a914218ca8bbb0e0dfb5b25021df7b22e0aa7839bf5fcdf44ec3492cc3` |
| `data/records/neodymium.yaml` | `62a30f718b54f236a2036491ec805cbd63f14ec29bccb73660b05767916b5e73` |
| `data/records/palladium.yaml` | `e0279891f5d589890c6872062e2fcf9e141c21cf9bec5d85ee7c142ec84e2d06` |
| `docs/records.md` | `4bb9e0c205d3bc7d40e7a3c604ad3ba9eb7cfea0397033ced766e00aa5440b78` |
| `history/records/cobalt/2026-10-08T023557Z-codex-7b6548.yaml` | `a7ce591674d5581325c7af3e7d7a1e6b80af29ca837c52b704c4c92e012a4345` |
| `history/records/neodymium/2026-10-08T023605Z-codex-131e84.yaml` | `8f7956e9b75412067b985f4ecb8020e0945b385af6cadd9d90a00f035174c51b` |
| `history/records/palladium/2026-10-08T023612Z-codex-97c17b.yaml` | `c299713c970a89aace0cb3db79de9b6e26e23cb42455cc443a5a96232cebdfb2` |
| `justfile` | `3d1c28fc16e6f331fa6371f5d4cf97c7b0a5fc257093284df733ed6d18d9e26f` |
| `reviews/integration/queue-20261008/README.md` | `56ce73c94911e50a96bca4736d93668b841d31786f72a215a9bf4ec98fcd49e2` |
| `reviews/integration/queue-20261008/apply.json` | `fe3c71a093e1d13eb419fee8c1680e53c079b7d5b6c45bbcb30327094fa18c72` |
| `reviews/integration/queue-20261008/automation-readiness.json` | `ec3b2acf068a77478c0d8b443d9705a3b4e2e7ba183f5b3139567e1638973c82` |
| `reviews/integration/queue-20261008/check.json` | `3a29daf8fe966a53485d112fddef2a121a1aaf642e5c8ca8acd21c54a2c12748` |
| `reviews/integration/queue-20261008/plan.json` | `c5f301d7bf2cd71bb110378bd1ad77f21575a5e7e73ae5fb0cdd07c398a25bd5` |
| `reviews/integration/queue-20261008/writer-token-run.json` | `22c01fe9c33f9060aad9115effdc811917d8b627df55d520b7acc41b0557a425` |
| `scripts/check.py` | `69894bbe6480c4dbec56b8e15cf97e3ed6273078dd6ac1b929d73aab3a87301a` |
| `src/cmmmech/cli.py` | `9265c92219045fbf97e5301455bcbf18ee6d07dfd955fe35c1cac2836a166a84` |
| `src/cmmmech/history.py` | `1d20985f4e3b068acb9842ceeb743c32acd297ff7f019e23a1122064a98882b8` |
| `src/cmmmech/schema/cmmmech.yaml` | `0251b807a70ac39d97fb680ec037e60a4bd8378c1fde5989ee84e4d62ac66b11` |
| `src/cmmmech/validation.py` | `249f23e1bfc3a184a663220bf9a930ff23cb021c75bb84029dc2d909b7a40f85` |
| `tests/test_check.py` | `258a62bca10025de6e6ddf765d5ee5e4794d157ccbb1a03edb76db1675ccda00` |
| `tests/test_history.py` | `4993e4dc20e87446070eb473e451ea64f849612d5ed26692efe9950af22f8878` |
