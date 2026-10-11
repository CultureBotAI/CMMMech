# Independent round 11 publication review

- Reviewer: Codex /root/round11_pr_adversary, GPT-6; a fresh agent distinct from the record curators and scientific reviewers.
- Scope: publication integrity, source receipts, coverage, preservation, navigation and claim boundaries. This is **not a fresh primary-literature scientific review** (`scientific_review: false`).
- Formal snapshot audit began: 2026-10-11T08:09:16Z; completed: 2026-10-11T08:13:06Z.
- Worktree: `/private/tmp/CMMMech-expansion-round11-20261011`.
- Branch: `curate/cmm-expansion-round11-20261011`.
- HEAD and trusted comparison base: `a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c`.
- Reviewed state: 55 staged paths, each byte-identical to its working-tree file; no unstaged tracked changes. This artifact was written afterward and is excluded from that 55-path manifest.

## Verdict

**Pass for the inspected local publication package, with the scientific limitations already recorded in the individual reviews.** No unresolved blocker, major or minor publication finding remains. The one minor presentation finding from preliminary orientation was corrected and verified below. Actual PR committed-head matching, CI, squash-shaped checkout and post-merge verification are later publication steps; this artifact does not claim they have occurred.

## Evidence and checks

Read `CLAUDE.md`, `README.md`, `docs/records.md`, `docs/record-reviews.md`, `docs/record-review-profile.md`, and the native curation and scientific-review instructions. Inspected the staged diff, publication report, frontier, dossier summaries/receipts, every new review's source inputs and reviewer-independence statement, the Tm finding and successor, and actual final validation logs.

An independently authored audit, `/private/tmp/cmm-round11-independent-publication-audit.py`, ran to terminal exit 0. Its detailed local receipt is `/private/tmp/cmm-round11-independent-publication-audit.json`. It established:

- All 55 index blobs match working bytes and are regular files. The change is limited to README, ten records, eleven history sidecars, research material and eleven structured review pairs; no code, schema, tests, dependencies or governance artifacts change.
- All **339 prior record/history/review files** are byte-identical to the trusted base in both index and worktree. Old scientific reviews and history were preserved.
- There are **71 records**: 64 elements, four minerals, two secondary resources and one commodity; **83 history sidecars** and **80 structured YAML/Markdown pairs**, including eleven new pairs.
- All **71/71 current records** have at least one completed independent scientific `kind: record` review with passing/qualified verdict, exact target ID and path, inclusion in `reviewed_target_ids`, a positive evidence-linked assessment, and a `role: target` SHA-256 matching current bytes. All ten final new records are qualified passes. Reviewer independence was inspected, rather than inferred from the count of bundles.
- All **63 current source-input assertions** in the eleven new reviews match. The initial Tm review's three historical inputs are the sole expected mismatches; all match the exact archived bytes and archive manifest, as detailed below.
- **411 current path/SHA-256 assertions** in the five staged research JSON receipts match actual bytes (319 unique paths), plus the three archived Tm assertions. Raw papers and image assets remain outside the staged package. Hash integrity verifies retained acquisition bytes, not the truth of every primary-source claim.
- All **173 relative Markdown file/directory links** in the staged Markdown resolve within the checkout. The README has one contiguous header, separator and **71 record rows**, whose links exactly cover the record inventory. Remote article availability and every heading fragment were not rechecked by this path audit.
- The unchanged historical inventory has **94 proposals**. Recomputing membership using exact `cmmmech:<candidate_key>` **and material kind** yields **65 represented and 29 remaining commodity proposals**; remaining proposal objects preserve original mapping notes. The frontier's current record metadata and hashes, ten newly represented keys, and explicit `exhaustion_claim: false` agree. These commodities overlap; this is not global exhaustion of material or mechanism evidence.
- Enumeration used `rg --files -uu --follow data/records research reviews history` and direct filesystem traversal, so hidden and ignored files were included. No symlinks were found within those bounded repository trees. Recorded external acquisition paths were read directly and their hashes checked. No machine-wide absence claim is made.

Independent command results:

| Check | Actual result |
|---|---|
| `git diff --cached --check` | Exit 0 |
| `.venv/bin/python /private/tmp/cmm-round11-independent-publication-audit.py` | Exit 0; exact manifest and receipt checks above |
| `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just review-check --base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c --require-reviews` | Exit 0; 80 valid pairs; `/private/tmp/cmm-round11-adversary-review-check.log` |
| `bash scripts/check_vendored_sync.sh` | Exit 0; 22 governed artifacts match pin `a5d562962c75a2ad9efd8160b548df5944315422`; `/private/tmp/cmm-round11-adversary-governance.log` |
| `git ls-remote origin 'refs/tags/review-base/cmm-source-survey-20261009*'` | Exit 0; annotated object and peeled commit match below; initial sandbox DNS failure was followed by successful authorized read-only verification |

I separately read the complete final native-check log and root terminal receipts: **307 tests passed, three skipped, 61.95 seconds**; 71 records valid; 83 histories valid. Required-record validation and history validation against the trusted base both terminated with exit 0. These are the curator coordinator's executed full-suite results, not a claim that this publication reviewer reran 307 tests. Receipt: `/private/tmp/cmm-round11-final-batch-receipts.json`; logs: `/private/tmp/cmm-round11-final-check.log`, `/private/tmp/cmm-round11-final-validation.log`, `/private/tmp/cmm-round11-final-history.log`.

## Findings and verified corrections

### Minor, resolved: README table separation — issue 46

Preliminary orientation found a blank line separating the ten new rows from the original table, which would leave them without the table header. I reported it before staging; the coordinator tracked [issue 46](https://github.com/CultureBotAI/CMMMech/issues/46) and removed the separator. The staged state now contains one contiguous 71-row table with the exact record-link set. No scientific target or saved review changed for this correction. No further edit is required in the inspected package; GitHub issue disposition belongs to the publisher.

### Existing scientific finding, resolved successor verified: thulium — issue 45

The immutable [initial Tm review](../../structured/20261011T080136Z-thulium-round11-independent/review.yaml) retains open finding `F1`, key `thulium-lta-necessity-overstatement`, and its original `needs_curation` verdict. The [successor](../../structured/20261011T080453Z-thulium-round11-resolution/review.yaml) resolves **that exact repository/review/finding occurrence** with the same issue key and a reason grounded in the corrected record and independent evidence assessment. It does not silently replace the original observation. The record links the actual [EDIT sidecar](../../../history/records/thulium/2026-10-11T080225Z-codex-327926.yaml), while preserving CREATE history; [issue 45](https://github.com/CultureBotAI/CMMMech/issues/45) is explicit.

The initial working-tree attestation legitimately differs from the corrected current target and shared dossier. I matched all three original SHA-256 values to actual archived bytes under `/private/tmp/cmm-round11-pre-correction-inputs/`, rather than treating historical currentness as a provenance defect:

| Original input | Verified archived SHA-256 |
|---|---|
| `data/records/thulium.yaml` | `d498820bc424bbdcf22ede740759d950328f8cad47ef14aa762be06c6a9c1837` |
| `research/ingests/round11-lu-tm-pm-20261011.json` | `f051782badf744dcb00ec98fec77177cc09990945b9f8db3e227f6cac917522a` |
| `research/ingests/round11-lu-tm-pm-20261011.md` | `090a4fda9a7fc5d47110fc7f200ffd4088cbf091564b8d07ea5a8d475e1ce7a2` |

The successor's stored hash of the initial YAML also matches the preserved initial review. Local archive availability is a verification aid; it is not represented as a committed reconstruction of earlier working-tree source bytes.

## Provenance retention and unresolved limits

All **12 distinct review bases** resolve. Eleven are ancestors of the trusted main base. The sole other revision, `c0adc2c0763e1515ed07dc712b024974d98fb342`, resolves locally and remotely through annotated tag `review-base/cmm-source-survey-20261009`, tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit `c0adc2c0763e1515ed07dc712b024974d98fb342`. No review base depends solely on this topic branch. A fresh checkout must fetch retained tags as documented; these working-tree scientific attestations remain working-tree attestations after publication.

The package clearly separates Be/He/Pm identity and dated designation from the seven accepted, narrowly scoped laboratory mechanisms. Deferred access, strain, control, analytical-fraction, phase and causal-attribution limits remain in records/dossiers/reviews; neither this publication pass nor deterministic checks remove them. I have not repeated the underlying primary-literature review, re-resolved every scientific authority, audited global literature absence, or recertified all remote fleet configuration. No further publication defect was established within the inspected scope.

## Frozen 55-path manifest

Manifest digest: `6b6d60fb688b9c82c21ddd0a2c84c89141203195fad2cc2a5f055b878f536d2a`. Computation: SHA-256 of the UTF-8 JSON array of the rows below as dictionaries with keys `path`, `sha256`, `bytes`, sorted JSON keys and separators `(',', ':')`, in the listed path order. Each row is the exact staged file and identical working-tree file. The reviewer artifact itself is intentionally excluded, avoiding a self-referential hash. A later committed-head verification must compare all these rows and separately verify this artifact's hash.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 21810 | `130661302bd6a728b1c2f8722f684e46d55e524b00af7eca7f1a94ebdffbf788` |
| `data/records/beryllium.yaml` | 1768 | `5a6288159ac129d07892cccdb7653e15ec80806e314bf51a48016945ff6f485f` |
| `data/records/hafnium.yaml` | 6789 | `9540ed730f70feb221b7bcb30cec4d729c14bb5c2da172825bd3e4dd00fd95f7` |
| `data/records/helium.yaml` | 2425 | `a2ff0d6c70298786262cd5ceb276ba5c873fe77cf60790a8ceb7be2504371f4c` |
| `data/records/iridium.yaml` | 7998 | `c77604f4962321302cd6f63ffff86d19463f4769893744c428155c1f6e9cf24c` |
| `data/records/lutetium.yaml` | 6015 | `a7962fcca9cdea5dd0c538f7d0f4707439a5241cd49819e93750245bf9a69789` |
| `data/records/osmium.yaml` | 6337 | `db219a825da6866d42a86debeeb8c9f2e615ddf7f7a178fcec74f9b55ef0b622` |
| `data/records/promethium.yaml` | 2006 | `147239c35cf5c9aa8d57342dd2c4014d35eddf92da0625cf5928250ad94a3948` |
| `data/records/rhenium.yaml` | 7911 | `88ad2d618e9b2468ecd0804d568d4c43303b0488766715f5b605e94b945516a4` |
| `data/records/rubidium.yaml` | 7077 | `d05bc7d114e08fc9c5715a7a4618562e22215104fbc93f7c8292394856cd6a07` |
| `data/records/thulium.yaml` | 6516 | `d61c9e4186bb38a8ed8c9bb3a4e9ac711163afc70e980a36f647dad5f4fab62f` |
| `history/records/beryllium/2026-10-11T075207Z-codex-97228e.yaml` | 872 | `bf5826ac88edf176555e9fafa41490cd2efab08445897f8d46dc689eb94b6d95` |
| `history/records/hafnium/2026-10-11T075415Z-codex-3cf591.yaml` | 911 | `d5a4ebf330075de3762d18a3c69930eee8d99cf3131f27a857aa9477cdd5ae51` |
| `history/records/helium/2026-10-11T075135Z-codex-c80080.yaml` | 903 | `f7dde6fac58f95661f56a3a1796de5037ca5abd645250ff98ffad0a6e080e000` |
| `history/records/iridium/2026-10-11T075703Z-codex-5aade4.yaml` | 885 | `f7196b893e65b64d3307086b9a7cb4b56843909a44333d6200773242d1234bfe` |
| `history/records/lutetium/2026-10-11T075300Z-codex-aa9d5e.yaml` | 949 | `64ea6d42d4ca519103a55b4a68f033bcd80376bb8ecefe4b9095d3ff2a9f3aea` |
| `history/records/osmium/2026-10-11T075422Z-codex-a98024.yaml` | 879 | `eeb1bd3d50e1d578f58b6e9a53c1171adf5020bb2389e99832f0260b00b2b182` |
| `history/records/promethium/2026-10-11T075338Z-codex-e70863.yaml` | 1026 | `bfb93a46b81acb457b33b2d8d7d9d1a79ba697e3e1bac41d9713af03bfd32c01` |
| `history/records/rhenium/2026-10-11T075235Z-codex-7de104.yaml` | 1064 | `b7c66509712d5d503b746a86acc547432b7902ec3e6f705955ddaa159a4337f7` |
| `history/records/rubidium/2026-10-11T075221Z-codex-dfa1a8.yaml` | 950 | `8165d628163b7a96631a97f3ad160f5007ef004752fcc033adc8eaa4702c4d6c` |
| `history/records/thulium/2026-10-11T075320Z-codex-34a805.yaml` | 1056 | `16ede09afc0dfa37afe3846b54b626fcb3ccc95c39eb0dc759c4fc52dbccb082` |
| `history/records/thulium/2026-10-11T080225Z-codex-327926.yaml` | 1116 | `53e0fc1ebac3cb04b85a37608902009f2a2f70bf33d4c9e0ea91800dba6cf1a2` |
| `research/ingests/round11-20261011-publication.md` | 11519 | `e36747e5ad3299e17f230b0b05c08ca3193204725b6e7080bb52dcc5657613ee` |
| `research/ingests/round11-be-rb-re-20261011.json` | 55939 | `640a1bdf8e27ab0ebd87f42949133434970efcd6eefcc12e771a245e966ab554` |
| `research/ingests/round11-be-rb-re-20261011.md` | 15650 | `4dcf18bcbfd6721ffa40b82969b6198047bfbbc599ba52daba7da960368a175d` |
| `research/ingests/round11-frontier-20261011.json` | 50095 | `67e6b231d99f47e1de815486358f17c0a86cf61d4cec545660c9402759eb4282` |
| `research/ingests/round11-frontier-20261011.md` | 4539 | `8bb62bbb32d679c13f1fe03ab37b50b8000ab6730590ed231c400a3ec922a31b` |
| `research/ingests/round11-helium-20261011.json` | 6830 | `9e1a3e83b71c346c3b8b9217e3cd8a6664c9100c9d8ee64c89d57772696f4c01` |
| `research/ingests/round11-helium-20261011.md` | 6337 | `0dc18402b3abf6f5c87b57dc8f55234149f4c4e86a2a1253d0c4a24a0cad1295` |
| `research/ingests/round11-ir-os-hf-20261011.json` | 43540 | `4667921f018418a919a21f885dbfc6b3b2eed96fe596fd6e8aed9ac7ab42219d` |
| `research/ingests/round11-ir-os-hf-20261011.md` | 11864 | `11511aaacd1bb01590db2826dce966c058330570c1ea66b09296b817270e2bc5` |
| `research/ingests/round11-lu-tm-pm-20261011.json` | 54835 | `aa6f8e56272c8b2396c532eddd36bbb96eb4bc8d16bb5ecfb6e71d97fc2bae77` |
| `research/ingests/round11-lu-tm-pm-20261011.md` | 13343 | `6859b6dbb806348045fae5c2234217c226c494dc7bacbc5ef38296b749630398` |
| `reviews/structured/20261011T080033Z-beryllium-round11-independent/review.md` | 19521 | `094a36e04d61a7bcb822e587ef6b44b80868b0dc21a8fc110614946692ecd77b` |
| `reviews/structured/20261011T080033Z-beryllium-round11-independent/review.yaml` | 11994 | `a58768e59c37089f8d10bdc6432885246a81860c34173ac8f54b81b9337fd737` |
| `reviews/structured/20261011T080136Z-thulium-round11-independent/review.md` | 24811 | `9cdf69dc02b6e9cb5281114cecf91cae3abc8fede72e4a7c9a19c828afd96c56` |
| `reviews/structured/20261011T080136Z-thulium-round11-independent/review.yaml` | 16548 | `594084831bf3cd018c8a88dd465e621274686afaae959d55dd14ffde7fa1ff5e` |
| `reviews/structured/20261011T080453Z-hafnium-round11-independent/review.md` | 21318 | `9c14a47a86125929ac831f0a802a3e5b0de9281576ad857b6ea3f349d55b09bf` |
| `reviews/structured/20261011T080453Z-hafnium-round11-independent/review.yaml` | 14217 | `ce26c22fd71479bf2f96ea5e3acdc92a837fbaad84f93e742d293ad31c2fe199` |
| `reviews/structured/20261011T080453Z-iridium-round11-independent/review.md` | 21502 | `a0f0b38c32292537ff756278ee02b53299966aacd67df4a3c16c5767f52c00d3` |
| `reviews/structured/20261011T080453Z-iridium-round11-independent/review.yaml` | 14246 | `9a4c48a6bcf3356f39659998285536ce01c4a8f23985406a77aa26df5e827c93` |
| `reviews/structured/20261011T080453Z-lutetium-round11-independent/review.md` | 21754 | `f0ca593dc37315b97f95c518269e56f76769068adcba82c03d3d6ec8d8980d2e` |
| `reviews/structured/20261011T080453Z-lutetium-round11-independent/review.yaml` | 14325 | `5a950a052e219e30233cd574772fb20b110b35f054b614a1f9c5be80c6078d62` |
| `reviews/structured/20261011T080453Z-osmium-round11-independent/review.md` | 19244 | `75472f0cb23610b35a4221d6d6e8d3edd5a7c5325497a25bdab6f9521b4f5827` |
| `reviews/structured/20261011T080453Z-osmium-round11-independent/review.yaml` | 12859 | `0fda7fe8c334bd47f212346f93e5ed961f5fb23b3ef49e6c15f7e76cb8b32225` |
| `reviews/structured/20261011T080453Z-promethium-round11-independent/review.md` | 19034 | `e1b059d6a290a400540a3fe1dce91743c293794cca9a485ffe1c2b311a2ded3e` |
| `reviews/structured/20261011T080453Z-promethium-round11-independent/review.yaml` | 12181 | `dd7e9e59f94538ae34945256d9a5eefcf3f88cf1df8d2de08ccfd74894f2d52c` |
| `reviews/structured/20261011T080453Z-thulium-round11-resolution/review.md` | 27899 | `82ffa44cfb10648204543110ee022228e03facf2e6c0819a1c67a9fdb0cf52ac` |
| `reviews/structured/20261011T080453Z-thulium-round11-resolution/review.yaml` | 18473 | `f072364de03de0e75cdac3a7c2132a295336117d776914565ca58cea242c7a25` |
| `reviews/structured/20261011T080559Z-helium-round11-independent/review.md` | 20176 | `ac7bc5056ed001e96b9987697890d68c1782892913b5671b04e7ba74dd49579a` |
| `reviews/structured/20261011T080559Z-helium-round11-independent/review.yaml` | 13137 | `69b8038c08f5cbc4dd84c296e9640c7355b07a7e0f5be15c62877cbbe9cab0f0` |
| `reviews/structured/20261011T080559Z-rhenium-round11-independent/review.md` | 21256 | `96279161045f1e032220d5c35635320daa6ea159522392d74a1de4f32a1873c1` |
| `reviews/structured/20261011T080559Z-rhenium-round11-independent/review.yaml` | 14154 | `0e47e1d931cea153798ecabf8aaa7ba927bef326e12562a16a5242ad74799cbf` |
| `reviews/structured/20261011T080559Z-rubidium-round11-independent/review.md` | 20814 | `92eec08960e2683851f668f601913b8862a2c4ebea653083ef614e176c3789e8` |
| `reviews/structured/20261011T080559Z-rubidium-round11-independent/review.yaml` | 13825 | `95554fd40ceb76f492682f170f4609e74c8f076d5a3b837511aade0c5b8aa8b0` |
