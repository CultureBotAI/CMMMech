# Independent adversarial review: native curation history, before repair

## Record/path and timestamp

- Scope: native history adapter and its nine owned implementation, schema, test,
  recipe and guide files; no scientific record edits or initial sidecars existed
  in the inspected history tree (hidden/ignored-inclusive inventory).
- UTC snapshot: 2026-10-08T02:17:06Z.
- Reviewer: independent `queue_admission_audit` agent.
- Base: `c32d78e26a15bb67a737700668badaed7da10597`; working changes were uncommitted.

## Reviewed revision and working bytes

| Path | SHA-256 |
|---|---|
| `docs/records.md` | `7c4a19c16139aa9c1e9a2382cd74ac5f459dc4d0d2493f9ef2b6ee174a3e7064` |
| `history/README.md` | `3ab55e49976481dd13a504d0fb9bc32033d8eb285c87fe56c7d4a8fcffb6f6d3` |
| `justfile` | `3d1c28fc16e6f331fa6371f5d4cf97c7b0a5fc257093284df733ed6d18d9e26f` |
| `scripts/check.py` | `69894bbe6480c4dbec56b8e15cf97e3ed6273078dd6ac1b929d73aab3a87301a` |
| `src/cmmmech/cli.py` | `9265c92219045fbf97e5301455bcbf18ee6d07dfd955fe35c1cac2836a166a84` |
| `src/cmmmech/schema/cmmmech.yaml` | `f396fa3578da53a85df38dfcb99ac41e609e0a3c09b2216941fde28cf0171112` |
| `src/cmmmech/validation.py` | `179705eda7f61d43dd3c66a783dd7877a425e7a45e8f75f9b5f5a20f3e369d4c` |
| `src/cmmmech/history.py` | `ebdf83649f5da6fcd3b52de71ae6b635bd346f3703d6d856dcb241230ed3cd9d` |
| `tests/test_history.py` | `e9d41f4dfd634ddf19087ab13d140982a604b5f3ad806e534efc46d45e4ed16d` |

## Scope and evidence checked

Read CMMMech `CLAUDE.md`, the record guide, schema, validator, CLI, scaffold and
tests against CLAW's canonical `HistoryRecord` and scaffold vocabulary at
`73958edb97994bc16c5404443956ee64c47bfe9b`. Checked append-only comparison,
target existence, path/session/actor constraints, record-reference identity,
duplicate sessions, no-clobber creation and migration-provenance wording.

Canonical schemas were used solely in an external isolated test fixture under
`/private/tmp/cmmmech-history-independent-review-20261008`; no governed repository
copy was installed or changed. This validates the native code against canonical
bytes and does not establish supported synchronization or runtime deployment.

The four history/validation/CLI/check test files passed independently: **88 passed
in 50.41s**, using CMMMech's development interpreter. An initial run using CLAW's
interpreter had 87 passes and one environment failure because that interpreter
lacked `ruff`; the corrected complete run above passed.

## Findings by severity

### P1 / major: history-directory aliases bypass immutability

Tracked as [CMMMech #8](https://github.com/CultureBotAI/CMMMech/issues/8).

Reproduction used the actual native CLI in a fresh temporary Git repository:

1. Create `data/records/cobalt.yaml`, an `archive/` directory, and the internal
   directory symlink `history -> archive`.
2. Run `new-history --slug cobalt --actor-name tester --actor-type human
   --summary 'Synthetic test' --details 'Original committed history.'`.
   It exits 0 and prints a `history/records/cobalt/<session>.yaml` path, whose
   physical file is stored under `archive/records/cobalt/`.
3. Commit the repository, then alter the stored session's event details.
   `git diff --name-status` reports `M archive/records/cobalt/<session>.yaml`.
4. Run `validate-history --repo-root <root> --base HEAD`.
   It incorrectly reports **one history record, zero errors, exit 0**.

`safe_relative` permits symlinks that resolve inside the repository;
`validate_history` checks only the final file's `is_symlink()` status. The Git
immutability comparison is restricted to `history/`, so the changed backing file
is outside its scope. A separate reproduction also accepted an external
`history/` directory symlink with zero validation errors. Nested directory
symlinks can be silently omitted by `rglob` rather than rejected.

Required repair: reject every symlink component in sidecar paths before reads
and writes, and explicitly reject symlink entries during discovery. Preserve
ordinary target-path semantics separately. Add a regression using a genuinely
committed aliased history tree whose backing file is then modified.

No other critical or major defect was confirmed in this review round.

## Corrections and unresolved questions

- Reported the complete reproduction before implementation changes. The parent
  filed #8; the history implementer owns the repair and follow-up tests.
- Issue #7's current distinction is sound: new sidecars relative to a supplied
  Git base need current target files, whereas unchanged historical sidecars may
  outlive removed targets. Standalone validation without a base cannot establish
  that historical distinction and documents its limits.
- Guidance correctly describes initial adoption as a present migration, without
  reconstructing earlier actors or pretending to repeat scientific reviews.
  Actual initial sidecars were not yet present, so their concrete provenance is
  outside this round's acceptance.
- Supported governed synchronization, event-specific CI comparison bases and
  end-to-end native checks remain separate integration work.

## Verdict

**Request changes** for #8. The passing pre-existing suite did not cover the
demonstrated immutability bypass. Preserve this report and review the repaired
bytes in a separate timestamped artifact.
