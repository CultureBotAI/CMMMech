# Round 36 scientific review and publication report

This batch adds 2 mineral records (moolooite, uramphite), bringing the corpus from 198 to 200. Phase-resolved primary evidence is qualified by the actual organism, medium, controls and outcome. Related material owners can represent different aspects of the same experiment; source reuse is not independent replication. No criticality is inherited from constituent elements and no industrial recovery claim is added.

Worktree: `/private/tmp/CMMMech-expansion-round36-20261011`; branch: `curate/cmm-expansion-round36-20261011`; trusted base: `1ef6fdde620a4053fbfff99c51065082dce32d39`. Unrelated work, including the older dirty add-record-skill worktree, is outside this change. The add-record skill is already maintained on main.

## Scientific reviews

| Record | Independent reviewer | Verdict | Saved Markdown / YAML |
|---|---|---|---|
| [moolooite](../../data/records/moolooite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T223107Z-moolooite-round36-independent/review.md) / [YAML](../../reviews/structured/20261011T223107Z-moolooite-round36-independent/review.yaml) |
| [uramphite](../../data/records/uramphite.yaml) | Codex /root | pass_with_limitations | [Markdown](../../reviews/structured/20261011T222903Z-uramphite-round36-independent/review.md) / [YAML](../../reviews/structured/20261011T222903Z-uramphite-round36-independent/review.yaml) |

The independent scientific reviews found no corrective record defect. The publication audit identified a minor closeout-receipt binding gap, tracked in issue #121; explicit guards and mismatch tests corrected it before any closeout post. The initial finding and verified successor disposition are retained.

The [manifest](round36-frontier-20261011.json) supplies exact paths, hashes, canonical histories, source dossiers and gate receipts. Each reviewer captured the exact inputs before judgment. Final scientific reviews match final record hashes.

## Validation

The baseline reused the exact unchanged main commit/tree freshly tested after the previous merge; this is not a newly executed baseline. Final batch commands below were newly executed for this batch.

```text
just check
uv run --locked --extra dev python scripts/check.py
All checks passed!
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
....................................................sss................. [ 92%]
.......................                                                  [100%]
308 passed, 3 skipped in 134.59s (0:02:14)
Checked 200 record(s); 0 failed.
Checked 231 history record(s); 0 error(s).
exit 0; log SHA256 cac731be567d421580f78dafc063be4b2ca406ca450d98bb15c72eab76e37b57
```

```text
uv run --locked cmmmech validate --require-records
Checked 200 record(s); 0 failed.
exit 0; log SHA256 0ed97773d44e6b06c1b7964ea58e27e8370bf048dd0a7c0384cf9f7681603b10
```

```text
uv run --locked cmmmech validate-history --base 1ef6fdde620a4053fbfff99c51065082dce32d39
Checked 231 history record(s); 0 error(s).
exit 0; log SHA256 75168340cd2362ddc1a2cc07d98f1a645893ffaa1d3d3f678ad3141c78cf40c4
```

```text
just review-check --base 1ef6fdde620a4053fbfff99c51065082dce32d39 --require-reviews
uv run python scripts/record_review.py check "$@"
topClass is deprecated - use top_class
{
  "repository": "CultureBotAI/CMMMech",
  "valid_reviews": 235,
  "coverage": "declared_scopes_only"
}
exit 0; log SHA256 a6e9265442b2025832b0465a748ef9986c61c96e257cba1214d7fe272df46ee0
```

An additional hidden/ignored-inclusive inventory verifies 200/200 current records have completed positive scientific reviews with matching exact hashes. There are 231 canonical histories, 235 structured reviews and 37 available review-base commits. Offline validation verifies structure and provenance, not scientific truth.

No schema, validator, test, skill or governance behavior changed. Raw source articles, figures and supplementary files remain outside Git.

## Publication and follow-up

CLAW fleet admission, canonical history, vendored governance, PR shepherd and native merge-queue configuration are installed. The shepherd is manual/comment-only and defaults to dry run; installed configuration does not establish credential readiness. Future governance updates must use CLAW’s supported admission/synchronization process. This batch does not configure governance.

All new review bases are on main. The existing annotated `review-base/cmm-source-survey-20261009` reference preserves the earlier otherwise-lost source-survey base. Publication requires explicit tag fetching and an isolated squash-shaped checkout without the topic commit. After native queue merge and owned-branch deletion, a fresh remote-main clone must pass full checks again; actual postmerge results belong in the PR closeout receipt.

Source-acquisition issues [#103](https://github.com/CultureBotAI/CMMMech/issues/103), [#104](https://github.com/CultureBotAI/CMMMech/issues/104) and [#120](https://github.com/CultureBotAI/CMMMech/issues/120) remain open. New #120 tracks the missing meta-autunite figure verification; no meta-autunite record/history was admitted. [Remaining priorities](round36-frontier-20261011.md) include manganese and iron oxalates, precise rare-earth phosphate phases and carried-forward source extensions. The source frontier is not exhausted.
