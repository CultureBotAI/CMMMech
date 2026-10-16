# Round 111 publication helper audit

UTC: 2026-10-16T04:36:10.039040+00:00. Reviewer: codex /root/round104_ree (GPT-6; codex).

Base `6a43774bf15a206b04e59c7525e93fdb334325d6`; worktree `/private/tmp/CMMMech-expansion-round111-20261016`. Precommit working tree at base; six external helper bytes bound below. The reviewer authored unrelated REE owners and this audit, but did not author or edit these helpers. Final config/report and corrected-batch acceptance are not yet available.

Independent static publication-helper review with pure negative guard tests; not record science, actual hosted acceptance or permission to bypass pending gates.

## Evidence checked

- `/private/tmp/cmm-round111-publish.py` SHA256 `23f38dd7a51e0c2ecc9fd4f254979e9bf4a19af06933382b2744563b9ac7e925`.
- `/private/tmp/cmm-round111-queue.py` SHA256 `15e0ec0d077c7ab3e10b15f16a134cf102eb087e310d90577055d8bb2ddf6428`.
- `/private/tmp/cmm-round111-isolated-verification.py` SHA256 `a0d97546551999552b5f691da4d5733454a8004069c3a05732b9a0734c5518b4`.
- `/private/tmp/cmm-round111-isolated-coverage.py` SHA256 `ce2304d7428c85ac1fddc15ce5fa9e9fac5023c58a43dcba09087cc57f5c9acd`.
- `/private/tmp/cmm-round111-post-review.py` SHA256 `0178520be89d26f5f33c01e5c5fc46e23ee511e68162e58b0158704974e26f01`.
- `/private/tmp/cmm-round111-review-bases.py` SHA256 `7e5258c40f15a2e3070f097fcee6ffca5275144e0326fc45229cc10875aa89b1`.

Six in-memory syntax checks passed. The AST-extracted publish prerequisite guard passed 23 inert positive/negative cases; evidence `/private/tmp/cmm-round111-ree-research/publication-guard-tests.json` SHA256 `efa8ed1bc0e3d527506a07b357164f26967381d44adb1aa6790b189b9f984bd2`. The separate 59-case queue receipt and exact test/helper hashes were verified; its synthetic fixture counts are not a corpus result.

## Findings by severity

No supported corrective defect found in the inspected helper bytes.

- Round identity and paths: All operational W/base/branch/helper/report prefixes target round111/base6a43774. Counts and PR number are read from later measured config/receipts rather than hardcoded production values. Original main is not a project-command cwd.
- Publish prerequisites: Commit requires exact base/branch/origin, terminal four-command science receipt, successful native-review receipt, exact log digests, matching owner/review coverage, stage allowlist, whitespace check and clean state. Push requires exact committed tree/helper/config digests, fresh main base and absent topic ref.
- Fresh squash verification: Single-branch main clone, explicit retained tags, unavailable topic commit checks, preflight synthetic single-parent tree and postmerge exact single-parent tree. Required validators run with clone cwd, offline uv and isolated environment; unchanged config/helper digests, clean clone and log/coverage hashes are retained.
- Exact review coverage: Hidden/ignored filesystem enumeration with cycle-protected symlink traversal; current owner ID/path/hash must match completed positive scientific review scope/inputs. Canonical native checker remains separately required; all review bases checked as commits.
- Queue admission: Positive completed independent exact-head assessment, posted assessment hash/live review equality, current required CI and native SQUASH/ALLGREEN rules, unique successful preflight commands at clone cwd, exact coverage/helper/log digests, unchanged input snapshots, and immediately preceding live-main base read. Match-head merge request has no bypass flag.
- Posted review and retained bases: Review is COMMENT on the accepted exact head; body and assessment hashes retained. Base inventory checks every saved revision and main ancestry or annotated retained tags; the historical special tag has explicit remote object/peeled bindings. Later isolated clone verifies practical availability.

## Corrections and unresolved questions

No helper edits or mutation execution were performed.
- Final config counts, report, corrected science receipt, native-review coverage, committed head/tree and actual PR do not exist yet or remain in progress; they must be checked before publication acceptance.
- Read-only/preflight/queue checks do not provide an atomic lock on remote main. Native queue checks and actual merged parent/tree plus fresh postmerge verification remain required.
- Comment posting can succeed before a receipt write fails; if interrupted, reconcile the actual hosted review before retrying. No such event occurred in this static audit.

## Verdict

Pass with limitations for prepared helper logic only. Final config/report/receipt and exact committed-head review remain pending; this is not a publication result.
