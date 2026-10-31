# Issue 509: fresh-clone provenance verification

Inspected 2026-10-19 UTC for [issue 509](https://github.com/CultureBotAI/CMMMech/issues/509).
All clone comparisons below use remote `main` at
`a272f29d32ad36fa0bb398ed866aeb0ab1b3cd8b`.

## Finding and change

The issue's assertion that no published reference retains the source revision
does not hold at this inspection. The remote already publishes the annotated
tag `refs/tags/review-base/cmm-source-survey-20261009`. Its tag object is
`fc4040c3abcd28f0a9cc52467e308100144ad1fd`; its peeled commit is
`c0adc2c0763e1515ed07dc712b024974d98fb342`.
An ordinary full clone acquires that reference and passes the existing review
test. This establishes current availability, not when the tag became available
or the exact options used in the issue reporter's checkout.

A separate clone created with `--no-tags --single-branch --branch main`
reproduces the missing-source failure at the same main revision. It is not
shallow, but its `remote.origin.tagOpt` is `--no-tags` and the retained source
commit is unavailable. Fetching the published tags makes that same clone pass
the complete test suite. No per-SHA fetch or new remote reference is needed.

The README now includes the retained-reference fetch in local setup, and the
review profile explains tagless/shallow recovery and exact-revision diagnostics.
These documentation changes make the existing prerequisite visible at the
normal contributor entry point. The checker still requires verifiable source
provenance; no saved bundle, governed artifact, or test skip is changed.

## Controlled verification

The work ran in isolated clones under
`/private/tmp/cmmmech-backlog-20261019-fmj36s`, using Python 3.14.7 and the locked
development dependencies. CI specifies Python 3.13; hosted CI has not run for
this branch. `UV_CACHE_DIR` pointed inside the scratch directory. `--no-sync`
was used for outer `uv run` calls after installing the locked dependencies.

| Checkout and command | Observed result |
| --- | --- |
| Ordinary full clone: focused `test_every_saved_structured_bundle_is_valid` | 1 passed in 96.67 s |
| Ordinary full clone: `uv run --no-sync just check` | 327 passed, 3 skipped; 602 records and 730 histories valid |
| Ordinary full clone: `bash scripts/check_vendored_sync.sh` | All 22 governed artifacts match the pinned CLAW revision |
| Full, single-branch, tagless clone: focused review test | 1 failed in 64.18 s with `source provenance unverified`; retained source commit absent |
| Same tagless clone after `git fetch origin --tags`: `PYTEST_ADDOPTS=-rs uv run --no-sync just test` | 327 passed, 3 skipped in 78.24 s |

The three skips are empty command-template parameter sets in
`tests/test_skill_frontmatter.py` at lines 190, 195 and 201. The saved-review
provenance test is executed and passes after recovery. The negative control
uses the preexisting assertion and demonstrates that missing evidence still
fails; the documentation change does not need a new implementation-mirroring
test. Shallow-clone recovery is documented but was not a separate measured
clone experiment in this investigation.

Reproduction of the measured failure and recovery, in an unused directory:

```sh
git clone --no-tags --single-branch --branch main https://github.com/CultureBotAI/CMMMech.git cmmmech-no-tags
cd cmmmech-no-tags
uv sync --locked --extra dev
uv run pytest -q tests/test_record_review_contract.py::test_every_saved_structured_bundle_is_valid
# Expected failure while the retained source commit is unavailable.
git fetch origin --tags
uv run just test
```

These results are specific to the inspected main revision. Recheck the base
when reproducing later.

## Final branch checks and review

The documentation branch also passed `PYTEST_ADDOPTS=-rs uv run --no-sync just
check` (exit 0): 327 tests passed in 234.48 s, the same three empty-parameter
skips, 602 records with zero failures and 730 histories with zero errors.
`bash scripts/check_vendored_sync.sh` passed again with all 22 artifacts matching.
The longer test runtime coincided with other active jobs on the shared machine;
it did not produce a failing or skipped provenance assertion.

A separate read-only review pass by the same agent inspected every changed
file, the proposed PR claims, the negative control, skip reasons, CI's lack of
path filters, and the canonical-artifact result. No confirmed finding remained.
This was a single-agent review, not an independent scientific record review;
no scientific record was changed. The README anchor and staged whitespace were
also checked. Hosted CI remains pending publication.

## Retained local evidence

The following logs are outside Git in the scratch directory above. Hashes
identify the measured local evidence; these machine-local paths are not a
promise of public log availability.

| File | SHA-256 |
| --- | --- |
| `baseline-509.log` | `f42016ae83278cdf1d9fcca48bcb9745d4ed03948ce78abae0802302b1fe3f3e` |
| `baseline-check.log` | `12ee4b19f3bf8a5adf833804d485ca2b9d8dd2dfb5417bb2e30086e806ba97a6` |
| `canon-check.log` | `3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e` |
| `no-tags-failure.log` | `b616c19aba2b0feec871c21bba323dae9e2cd5ba5cc168f13c084c4cfba4a05f` |
| `no-tags-recovered-test.log` | `835739f81d1050e82bbff966b0741c8a6d6817d1e76d09198223365235827187` |
| `issue-509-check.log` | `66847ae04eecd2948920b648220ee58dea98b7d585f103b640ced74f94bc725f` |
| `issue-509-canon.log` | `3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e` |
