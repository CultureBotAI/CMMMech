# Publication helper correction: independent successor

UTC: 2026-10-15T18:43:09.948582Z. Reviewer: codex `/root/round100_pentagonite` (GPT-6), independent of the correction author.

Predecessor: [initial audit](20261015T184111Z-publication-helpers-independent.md). Issue: [#367](https://github.com/CultureBotAI/CMMMech/issues/367). Stable finding key: `CMMMech:round100:coverage-receipt-exclusivity`.

**Pass with limitations: the receipt-exclusivity code finding is resolved.** The issue remains subject to actual completed scientific coverage; no issue closure or executed preflight is claimed.

## Exact correction and evidence

- Original preserved: `/private/tmp/cmm-round100-isolated-coverage-before-exclusive.py`, SHA256 `a7233d12b1f245d4c073933da755765d63d02dcdb15359797557fa6c4f9506ca`.
- Corrected helper: `/private/tmp/cmm-round100-isolated-coverage.py`, SHA256 `58715e5e3c924c1a16a3bb3393a612bf94ee4e6c733c16edc405c057f91ea75b`.
- Diff changes only the receipt block: explicit existing-file/symlink refusal and exclusive `open('x')`. Scientific coverage selection is unchanged.
- Independently executed five regression tests with exit 0. Log: `/private/tmp/cmm-round100-sulfates-independent-review/coverage-receipt-tests-independent.log`, SHA256 `39db24e5f81afd8acf9e0bb55983b5cca58d1bbc506e37249bd2ee3a97be2a6f`. Cases cover normal creation, occupied regular file, existing/dangling symlinks and a racing creator.
- Full-helper reproduction: `/private/tmp/cmm-round100-helper-successor-c5l698nd/reproduction.json`, SHA256 `2ed213cb1e5acba11df6f329fd5c2c6b33720397621d7645f361155a7680562e`. The new unique empty fixture received the expected `FileExistsError` exit 1; no symlink target was created.

## Remaining verification

- Finalize and reconcile counts after native scientific reviews are saved.
- Run actual exact-tree preflight and exact-hash scientific coverage using corrected helper bytes; retain receipt before closing the review issue.
- Verify remote retained review-base tags and eventual main-only postmerge clone separately.

This is a supplementary publication audit of exact temporary-helper bytes. Scientific owner bytes were not edited, and no historical audit was overwritten.
