# Round97 runtime-helper successor review

- Reviewer: codex /root/round97_phosphates (GPT-6); independent of fixes.
- UTC: 2026-10-15T15:36:02.990239+00:00 to 2026-10-15T15:37:55.558869Z
- Reviewed base: `9272005a590c9fa1e5fbb75b30f914ce38c3924a`; exact corrected external helper and test bytes.
- Verdict: **Pass with limitations for static and isolated regression scope.**
- Findings: OP97-01, OP97-02 and OP97-03 resolved; no unresolved findings in this review.

Predecessor: [20261015T152425Z-runtime-static-initial](20261015T152425Z-runtime-static-initial.md), JSON SHA256 `af7c2e7157468d3af1ebbf585ccb4cadb6c56d560e70f292db401bebe5217ac0`.

## Dispositions

### OP97-01 — resolved ([#354](https://github.com/CultureBotAI/CMMMech/issues/354))

Current hosted-five authorship now describes root coordination of four mineral species and two bone residues authored/reviewed by distinct agents, and Markdown heading is Round97. No bassanite/wood-ash authorship is emitted for this cohort.

### OP97-02 — resolved ([#355](https://github.com/CultureBotAI/CMMMech/issues/355))

Shared ensure_unoccupied rejects existing files, directories and dangling symlinks before action. ExclusiveReceipt atomically reserves an exclusive open descriptor before mutation, checks its inode, writes through that descriptor, fsyncs terminal results and preserves explicit failure receipts. Commit/publish/enqueue/cleanup/sync use the guard; inspected tests cover all five occupied-output paths, late collision and replaced symlink without changing a victim.

### OP97-03 — resolved ([#356](https://github.com/CultureBotAI/CMMMech/issues/356))

Shared verified_handoff checks current config/body/runtime-helper hashes against both prepared and committed bindings, preparation digest/base/file map, and commit config identity. Publish verifies exact branch/base/head/tree and live main before reserving output/pushing, rechecks the handoff after push, and submits verified body bytes through stdin. Enqueue repeats these original bindings and requires matching preflight/creation receipt digests; preflight retains and rechecks bindings. Stale config, body, helper and prepared inputs fail before fake subprocess calls in the inspected tests.

## Evidence checked

- All thirteen reviewed helper files parse as Python. Unchanged helpers retain the initial hashes. Seven sulfate-edited originals match preserved snapshots and initial review hashes; initial archive snapshot also matches. Initial lineage is retained as a historical substitution-only snapshot, not falsely relabeled current.
- Independent target regressions: 8 tests,0 failures,0 errors. They exercise occupied outputs for commit/publish/enqueue/cleanup/sync; stale config/body/helper/prepared inputs for publish/enqueue; missing bindings; normal bound-stdin publication; changed body after fake push; late collision; failure and path-replacement handling; and read-only commit check-only. Every subprocess entry is mocked, and files are confined to disposable fixtures.
- The root-owned archive now verifies the current prepared/commit handoff before mkdir, reconciles preflight/postmerge/hosted/cleanup/sync base/head/tree/merge and PR identities, checks log hashes and command outcomes, and retains all twelve helper sources plus shared guards. This closes the limited archival caveats in the initial review; no separate scientific claim or original finding is overwritten.
- Existing exact base/head/tree and sole-parent checks, branch-only lease cleanup, original-main hidden/ignored file/mode/symlink preservation, retained tag checks and fresh-clone topic-object absence gates remain intact.
- Publication binding set includes the directly executed isolated-coverage helper and shared guard, in addition to config/body and mutating/verification/archive helpers. Runtime handoffs must be generated only after all these bytes are frozen.

## Exact current helper hashes

| Helper | SHA256 |
| --- | --- |
| commit | `e21c662afacc9873072b60a7f3e12d2aa227562dd4fa8ff3cdf73caf567d74a7` |
| publish | `b56940f438ce4756df11e5d507e8c2d9da173b6f53a70d11b34fafd9c16b3131` |
| enqueue | `94bfec10b3d523968b6e5a0f92cdc8f459224af320356ec5e14fd3abca6bd07d` |
| cleanup | `7fbdab84a12361c860b61e929e163a737878d2d81ed00e9d0b5601d4456294b2` |
| sync-main | `f2dcefcc0dc802d9846a121a54965ff5acb893b14433d2b399c0ec4413b1b332` |
| isolated-coverage | `2976fa37edb6f1fd50dd5aaf600133a07149388fe098fef68c03354b51afd844` |
| isolated-verification | `ecc70523a1420583317a27b9f45a0b46500feaadfc7f611e1a25b8ac9eae30f4` |
| hosted-five | `cae146f2d5afae7d02b16bf1e6714fce29665e52966cb3846c189cecbe1e1557` |
| preservation-check | `5ba7e641845710767b9d35c9a4460ef2639fd42d24946c8d2befac9edc1b0038` |
| review-check-final | `f19787384f01c3c8b4dfe911584f04be12faa4321fc80a2eeac6eda1d5a6ca4a` |
| final-gates | `d1c4db7a2728a74d789445eecbfa7fcc765a9ff4686add9b124830d955503754` |
| archive | `7b29bd83d095a849431155d33c9d620bc32b93e5b25f065a150c4df17fcf3cdd` |
| shared-guards | `681dc8476e6bf868a67b11258121840db49cf9c8a9f204b59dae349004c0c6c7` |

## Unresolved questions and limits

- This is static/helper-regression acceptance, not acceptance of a live PR, actual publication, merge result or current hosted workflow success. Fresh final counts, package audit, immutable preparation, commit, hosted peer review, preflight, queue and postmerge evidence remain mandatory.
- Native queue live-base observation is not atomic locking. Actual merge tree/sole parent, five hosted workflow roles and fresh remote-main checks still govern completion.
- A failed action after a completed remote step preserves a failed receipt; coordinator must reconcile it rather than rerun blindly. Tests do not simulate every possible external provider failure or malicious receipt forgery.
- No full suite rerun was duplicated for external helper changes. The independently reviewed scientific owners remain unchanged and have separate saved native reviews.
- The helper contract intentionally uses exact hashes: any subsequent helper/body/config edit invalidates these exact-byte results and requires affected re-review and fresh handoff/test evidence.

Full predecessor links, original/current hashes, test source and regression evidence: [20261015T153755Z-runtime-static-successor.json](20261015T153755Z-runtime-static-successor.json).
