# Issue creator receipt correction — implementation evidence

Saved UTC: 2026-10-15T21:31:06.622316Z

Issue: [#391](https://github.com/CultureBotAI/CMMMech/issues/391). Stable key: `cmmmech:round103-issue-create-reservation`.

Initial finding: [20261015T212926Z-preparation-initial.md](20261015T212926Z-preparation-initial.md).

Narrow correction of previously reproduced pre-mutation receipt-reservation failure in the temporary issue creator. No scientific owner/history/schema change.

- Exclusively opens aggregate output before any external mutation; explicit occupied/symlink refusal plus open(x) handles races.
- Journals active mutation response and post-create verification response, preserving known URL/number on failed verification and verified earlier issues on later failure.
- Writes terminal failed receipt on exceptions using the exclusively reserved file descriptor; successful output remains the established array of six verified issues.

Eight tests passed using exact helper bytes, unique temporary directories and mocked subprocess calls: normal success, occupied regular file, existing symlink, dangling symlink, racing creator, rerun, partial create failure and post-create verification failure.

Corrected helper SHA-256: `55a838aead9338efd18e5bc8ad933aaecf4d5503d91579e92a6e1c3748320a99`. Real successful receipt remained `ffc84e4e262426139f495b574581e9432ae865ded02f47645e5e2ac169b97564`.

Correction implemented and eight isolated regressions passed. The actor implemented this fix after identifying it; this artifact does not claim independent acceptance. Coordinator and separate peer review requested.

## Limitations

- No real issue creation replay was performed. #385–390 retain their original successful receipt.
- A failed mutation may have an ambiguous external result; the terminal receipt retains available stdout/stderr and active stage for manual reconciliation and blocks automatic rerun.
- Process termination beyond Python exception handling may retain in-progress state; exclusive reservation still blocks replay. No distributed transaction guarantee is asserted.
