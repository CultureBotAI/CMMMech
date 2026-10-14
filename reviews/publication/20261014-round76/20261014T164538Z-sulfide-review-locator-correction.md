# Sulfide review artifact locator correction

Actual UTC interval: 2026-10-14T16:45:37.924895+00:00 to 2026-10-14T16:45:38.002093+00:00. Author self-correction; metadata only.

Minor finding RL1 (`round76-sulfide-review-local-artifact-locator`), tracked by [issue251](https://github.com/CultureBotAI/CMMMech/issues/251): `actual raw/<filename>` in the two immutable reviews was shorthand for a local variable, not a literal directory. Hidden/ignored-inclusive, symlink-following enumeration of the two bounded source/reviewer folders confirms the actual original PDFs reside directly under `/private/tmp/cmm-round76-sulfides-research`.

The corrected exact locators are:

- Anilite evidence `primary`: `/private/tmp/cmm-round76-sulfides-research/goble1981.pdf`.
- Anilite evidence `whiteside` and digenite evidence `whiteside`: `/private/tmp/cmm-round76-sulfides-research/whiteside1986-doclib.pdf`.

Both PDF signatures, nonzero sizes and original SHA256 values were independently rechecked. The JSON binds each exact original review YAML/Markdown hash, target/hash, source URL and evidence ID to its corrected full locator. The original native bundles remain unchanged.

Qualified scientific verdicts, evidence support roles and all record/history bytes remain unchanged. This addendum is not a new independent scientific review and makes no live issue-state or hosted runtime claim. No unresolved locator correction remains.
