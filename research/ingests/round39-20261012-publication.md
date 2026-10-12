# Round 39 scientific review and publication report

This batch adds malachite, cerussite, fluorapatite and hollandite and extends the existing lindbergite record with a separate primary study. The corpus grows from 206 to 210 records. Four mineral feeds share the Vlasov2023 experiment; separate material owners do not imply independent replication. All accepted mechanisms are bounded laboratory observations. No criticality designation is inherited from a constituent element, and no isolated-metal yield or industrial deployment is asserted.

Worktree: `/private/tmp/CMMMech-expansion-round39-20261012`; branch: `curate/cmm-expansion-round39-20261012`; trusted base: `bf1f7000014287805ea7c44341a3ce9e112e6689`.

## Scientific review

| Record | Action | Verdict | Review artifacts |
|---|---|---|---|
| [cerussite](../../data/records/cerussite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T002256Z-cerussite-round39-independent/review.md) / [YAML](../../reviews/structured/20261012T002256Z-cerussite-round39-independent/review.yaml) |
| [fluorapatite](../../data/records/fluorapatite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T002355Z-fluorapatite-round39-independent/review.md) / [YAML](../../reviews/structured/20261012T002355Z-fluorapatite-round39-independent/review.yaml) |
| [hollandite](../../data/records/hollandite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T002355Z-hollandite-round39-independent/review.md) / [YAML](../../reviews/structured/20261012T002355Z-hollandite-round39-independent/review.yaml) |
| [lindbergite](../../data/records/lindbergite.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T002249Z-lindbergite-round39-independent/review.md) / [YAML](../../reviews/structured/20261012T002249Z-lindbergite-round39-independent/review.yaml) |
| [malachite](../../data/records/malachite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T002250Z-malachite-round39-independent/review.md) / [YAML](../../reviews/structured/20261012T002250Z-malachite-round39-independent/review.yaml) |

Each final independent review matches its record bytes. The [manifest](round39-frontier-20261012.json) pins records, histories, reviews, dossiers and gate receipts. The five reviews found zero corrective record defects. The lindbergite review freshly assesses Wei2012 and proves preservation of earlier fields against their prior independent scientific review; it does not claim a fresh re-review of unchanged older papers.

The records preserve organism-specific phase detection, microscopy-versus-diffraction distinctions, source formula and figure/table contradictions, weak controls, preparation effects and missing mass balances. Raw originals remain outside Git. Four canonical CREATE histories and one EDIT were appended; prior sidecars and reviews remain unchanged. No schema, validator, test, skill or governed artifact changed.

## Deferred evidence and issues

Independent publication review found a stale README link to the round38 priority list. [Issue #131](https://github.com/CultureBotAI/CMMMech/issues/131) tracks the correction to the round39 frontier; the initial finding is retained and the final review verifies its resolution. No scientific record or history changed for this navigation fix.

[Issue #129](https://github.com/CultureBotAI/CMMMech/issues/129) tracks vanadinite's still-missing original phase/control graphics after partial acquisition. [Issue #130](https://github.com/CultureBotAI/CMMMech/issues/130) tracks the complete yeast cerium-phosphate primary article and unresolved particle identity. Both are open source tasks, not defects in admitted records. The source-only dossiers record the acquisition work and deferrals; no speculative record or CREATE history was added. Earlier source issues #103, #104 and #120 also remain open.

## Validation and preservation

The baseline reuses the just-completed fresh remote-main full gate at this exact unmodified base/tree; no new baseline execution is claimed. That receipt is `/private/tmp/cmm-round38-postmerge-20261011-published-terminal.json`, SHA-256 `3b4dd99d47bc41ac6155632311f5db97f23bf6a596dc0be6840d0159b9a15527`. The frozen round39 cohort was then checked separately:

- `just check`: exit0; log SHA-256 `97728f73d7f6f23423c32ceb6fe3e9688ef9fc83a4fbbdb185675bcafef84793`.
- `uv run --locked cmmmech validate --require-records`: exit0; log SHA-256 `8088527a34a0b38dfa3a5e7dc9ba7acbb2db5645f2022a0277c19fbc93b5c23f`.
- `uv run --locked cmmmech validate-history --base bf1f7000014287805ea7c44341a3ce9e112e6689`: exit0; log SHA-256 `248ff272d20e51f3c8767e9de06bb1481564fc01d11b353d8e0570f1628918e3`.
- `just review-check --base bf1f7000014287805ea7c44341a3ce9e112e6689 --require-reviews`: exit0; log SHA-256 `442bb3d218e95870771d793a4ef57f2ca317010ba157da46c327db1b8c73da2a`.

`just check` passed 308 tests with 3 skipped, validating 210 records and 242 histories. The separate canonical review gate and exact-hash coverage audit found 246 valid structured reviews, 40 available review bases and completed scientific coverage for all 210 current records. These structural gates do not themselves prove scientific truth.

The [independent preservation receipt](../../reviews/publication/20261012-round39/independent-preservation.json) verifies all 7,187 hidden/ignored original-main entries and eight bounded unrelated skill-worktree entries against the untouched initial snapshot, including symlink destinations and original Git state. All project commands used the isolated worktree. The [operational helper audit](../../reviews/publication/20261012-round39/helper-independent-audit-20261012T002546Z.md) found no actionable defects in the eight reviewed temporary helpers; final publication execution remains separately verified.

## Publication process and remaining work

The [live status snapshot](../../reviews/publication/20261012-round39/current-status.json) confirms merged CLAW admission, four active workflows and the effective native SQUASH/ALLGREEN queue with required `validate-strict` and no ruleset bypass actors. Canonical history and immutable pinned governance are installed. Workflow presence does not prove PR-shepherd credential readiness or a fresh fleet-wide audit; future governance changes use CLAW's supported admission and synchronization process.

All new reviews use the trusted main base. The existing `review-base/cmm-source-survey-20261009` tag preserves the earlier otherwise-lost revision. Exact-tree isolated squash-shaped validation must pass before push/queue admission. After the actual queue merge and deletion of only the owned topic branch, a fresh remote-main clone must pass the full checks with tags fetched; original main is fast-forwarded only after preservation guards. Those future results belong in the PR closeout receipt.

[Remaining priorities](round39-frontier-20261012.md) include manganese-ore oxalates, synthetic birnessite identity and unresolved primary access. The source frontier remains open.
