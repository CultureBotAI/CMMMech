# Independent review: synthetic history test environment isolation

- Issue: [CMMMech #10](https://github.com/CultureBotAI/CMMMech/issues/10).
- UTC timestamp: 2026-10-08T02:41:57Z.
- Reviewer: independent `claw_register_cmm` agent; implementation by `history_cmm`.
- Reviewed revision: `c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1` plus uncommitted integration changes in `/private/tmp/CMMMech-history-queue-20261008`.
- Scope: module-local synthetic-history environment isolation, the CLI environment default, explicit-base precedence, CI gate propagation, and standalone validation documentation. This is not a replacement for the complete adapter or scientific record reviews.

## Evidence checked

Read issue #10, `tests/conftest.py`, and the six files fingerprinted below. A hidden- and ignored-file-inclusive search (`rg -uu`) of source, scripts, tests, workflow, and record documentation confirmed that environment clearing is confined to the synthetic history test module; the production CLI and gate continue to read `CMMMECH_HISTORY_BASE`.

Independently ran both affected test modules with an intentionally unavailable inherited base:

```sh
CMMMECH_HISTORY_BASE=ffffffffffffffffffffffffffffffffffffffff \
  .venv/bin/python -m pytest tests/test_history.py tests/test_check.py -q \
  -o cache_dir=/private/tmp/cmmmech-issue10-review-pytest-cache
```

Result: **51 passed in 39.56s**, exit 0. Log: `/private/tmp/cmmmech-integration-evidence/issue10-independent-pytest.log`. `git diff --check` also passed.

The new real-Git test captures its own baseline, commits a sidecar rewrite, supplies that baseline through the environment, and requires the specific append-only diagnostic. The same committed bytes pass with explicit `--base HEAD`. This tests both the production environment default and flag precedence, and prevents an unrelated unavailable revision from satisfying the negative assertion.

The existing subprocess regression executes the actual gate with a locally captured CI-style baseline. It requires successful lint, nested tests, and scientific validation before the expected append-only failure; its otherwise identical `HEAD` control passes. The module-local fixture cannot clear the parent gate process environment, and the gate regression lives outside that fixture's module.

Inspected the implementer's separately executed scratch-copy mutation evidence at `/private/tmp/cmmmech-history-issue10-mutation-results.json`. Both mutations have control/mutant/restored exit statuses 0/1/0: removing fixture isolation breaks positive synthetic tests under an external base; removing the CLI environment default breaks the new own-baseline test. Its restored source/test hashes match this review's files. These mutations were not executed by this reviewer.

The implementer reported the actual repository gate with base `c76651d9cb3a88f2a9a3df4924c6449f97dbdfb1` passed: 215 tests passed, 3 skipped, lint passed, three records passed, and three histories passed. The parent coordinator retains the full-gate execution evidence; this review's independently executed result is the 51-test run above.

## Findings by severity

- Critical: none in the reviewed scope.
- Major: none remaining. The inherited external revision no longer contaminates synthetic test defaults, while production enforcement remains enabled.
- Minor: none remaining. Documentation now correctly limits standalone metadata-only validation to invocations with neither the flag nor the environment variable.

## Corrections verified

The autouse fixture removes the inherited variable only inside `tests/test_history.py`; the new test deliberately reintroduces a meaningful local baseline. No production source behavior was weakened for issue #10. The separate actual-gate propagation regression remains meaningful and passed under the hostile inherited environment.

## Unresolved questions

None for issue #10. Final acceptance of the full integration still includes the separate adapter, record, and complete repository gate reviews. No fleet reconciliation or remote publication was performed by this reviewer.

## Reviewed file SHA-256

| File | SHA-256 |
| --- | --- |
| `tests/test_history.py` | `4993e4dc20e87446070eb473e451ea64f849612d5ed26692efe9950af22f8878` |
| `tests/test_check.py` | `258a62bca10025de6e6ddf765d5ee5e4794d157ccbb1a03edb76db1675ccda00` |
| `src/cmmmech/history.py` | `1d20985f4e3b068acb9842ceeb743c32acd297ff7f019e23a1122064a98882b8` |
| `scripts/check.py` | `69894bbe6480c4dbec56b8e15cf97e3ed6273078dd6ac1b929d73aab3a87301a` |
| `docs/records.md` | `4bb9e0c205d3bc7d40e7a3c604ad3ba9eb7cfea0397033ced766e00aa5440b78` |
| `.github/workflows/validate-strict.yaml` | `94e104b93ac4111bb591dc7769da933d98ea661192aac24bfda2acf2af31d918` |

## Verdict

**Accept the issue #10 correction at the reviewed file state.** The fix isolates test fixtures, retains the production environment contract, and has both positive controls and failure-specific regression coverage.
