# Issue 479 evidence disposition

Inspected base: `a272f29d32ad36fa0bb398ed866aeb0ab1b3cd8b`.
Issue: <https://github.com/CultureBotAI/CMMMech/issues/479>.

The complete 2026 aluminium salt-slag original supports a separately qualified
laboratory salt-regeneration and remelting mechanism in the existing owner.
The source does not establish reconciled whole-slag recovery, repeated reuse,
or industrial deployment. Feed distinctions, fresh additions, calculated
properties, inconsistent recipes and unresolved yield denominators remain
explicit. The existing 2022 experiment is preserved as a separate mechanism.

The [source assessment](../../research/sources/issue-479-resources/20261019T073452Z.md)
and [acquisition evidence](../../research/sources/issue-479-resources/20261019T073452Z-evidence.json)
record the complete primary versions, hashes, bounded searches and access limits.
The [independent scientific review](../structured/20261019T074137Z-aluminium-salt-slag-issue479-independent/review.md)
has verdict `pass_with_limitations`, no new open findings, and explicit lineage
for the previously resolved mass-balance finding. It binds the exact record
SHA-256 `1124a6d4ec919fb5d12ad08aecf847a599f502587d3d5b6592865da6ea2c3b15`.

The fungal HFC subtask remains incomplete. Current legitimate publisher routes
returned preview HTML, and the documented alternative searches did not acquire
complete methods and figures. No HFC organism or mechanism was imported, no
paid service was used, and no author was contacted. This bounded acquisition
failure is not a claim that a complete copy is unavailable everywhere. The
whole issue must remain open.

## Validation and publication dependency

The baseline `just check` passed 327 tests with three empty-parameter skips,
602 records and 730 histories. After curation, `uv run --no-sync just check`
again exited 0: **327 passed, 3 skipped in 179.51 s; 602 records, 0 failed;
731 histories, 0 errors**. The skips concern empty command-template parameter
sets, not review provenance. Independent named-record validation passed.
`bash scripts/check_vendored_sync.sh` exited 0 for all 22 governed artifacts.
After saving the review, `uv run --no-sync just review-check --require-reviews
--base a272f29d32ad36fa0bb398ed866aeb0ab1b3cd8b` exited 0 with **701 valid
review bundles**, including the new observation.

Local full-check log SHA-256:
`f3e55992044496fb287f1b0b718531109531b8b33b29f2673160727d37c08081`.
Logs and raw source copies remain in the temporary execution workspace; the
committed assessment does not promise permanent availability of those paths.

Standard rendering exposed a separate existing renderer defect: its process
list omits the schema-supported `recycling` category. Three records already on
the inspected main base are affected; this new salt-slag mechanism would be a
fourth. Category navigation and graph nodes are missing while material detail
pages show a process badge. The renderer fix and its regression are prepared
on the separate `codex/render-recycling-process` branch.

This branch retains the required scientific classification and the generated
output of its own renderer. Publication remains dependent on integrating the
separate renderer correction, regenerating these pages, and rerunning the
relevant checks against the resulting base. Passing current tests does not
certify the omitted category. No merge or remote publication has occurred.
