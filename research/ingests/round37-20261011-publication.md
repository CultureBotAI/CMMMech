# Round 37 scientific review and publication report

This batch adds 3 mineral records (falottaite, humboldtine, lindbergite), bringing the corpus from 200 to 203. Phase-resolved primary evidence is qualified by the actual organism, medium, controls and outcome. Related material owners can represent different aspects of the same experiment; source reuse is not independent replication. No criticality is inherited from constituent elements and no industrial recovery claim is added.

Worktree: `/private/tmp/CMMMech-expansion-round37-20261011`; branch: `curate/cmm-expansion-round37-20261011`; trusted base: `dcfbedb78bfd682ad06f2ff4517241f490e4f401`. Unrelated work, including the older dirty add-record-skill worktree, is outside this change. The add-record skill is already maintained on main.

## Scientific reviews

| Record | Independent reviewer | Verdict | Saved Markdown / YAML |
|---|---|---|---|
| [falottaite](../../data/records/falottaite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T230405Z-falottaite-round37-independent/review.md) / [YAML](../../reviews/structured/20261011T230405Z-falottaite-round37-independent/review.yaml) |
| [humboldtine](../../data/records/humboldtine.yaml) | Codex /root/round27_eaf_slag | pass_with_limitations | [Markdown](../../reviews/structured/20261011T230710Z-humboldtine-round37-independent/review.md) / [YAML](../../reviews/structured/20261011T230710Z-humboldtine-round37-independent/review.yaml) |
| [lindbergite](../../data/records/lindbergite.yaml) | Codex /root | pass_with_limitations | [Markdown](../../reviews/structured/20261011T230525Z-lindbergite-round37-independent/review.md) / [YAML](../../reviews/structured/20261011T230525Z-lindbergite-round37-independent/review.yaml) |

The independent scientific reviews found no corrective record defect. Source-specific phase, control and causal limitations remain explicit.

The [manifest](round37-frontier-20261011.json) supplies exact paths, hashes, canonical histories, source dossiers and gate receipts. Each reviewer captured the exact inputs before judgment. Final scientific reviews match final record hashes.

## Validation

A fresh baseline just check passed at the trusted base before record edits: 308 tests passed, 3 skipped, 200 records and 231 histories valid. Final batch commands below were separately executed on the frozen three-record cohort.

```text
just check
uv run --locked --extra dev python scripts/check.py
All checks passed!
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
....................................................sss................. [ 92%]
.......................                                                  [100%]
308 passed, 3 skipped in 169.92s (0:02:49)
Checked 203 record(s); 0 failed.
Checked 234 history record(s); 0 error(s).
exit 0; log SHA256 66cd8ce7b2befd361157ae7ca4451bc53e7af52ad8b471ef3e6c8de404f7ce76
```

```text
uv run --locked cmmmech validate --require-records
Checked 203 record(s); 0 failed.
exit 0; log SHA256 fb8749bf338f8365b7257600e0f9027811928450edb84261927b6c183f100968
```

```text
uv run --locked cmmmech validate-history --base dcfbedb78bfd682ad06f2ff4517241f490e4f401
Checked 234 history record(s); 0 error(s).
exit 0; log SHA256 32939b2f20f8cf7bff98cb0d67e9dd288f58f0b9e3cbe88ad81ace21c1b8ccdc
```

```text
just review-check --base dcfbedb78bfd682ad06f2ff4517241f490e4f401 --require-reviews
uv run python scripts/record_review.py check "$@"
topClass is deprecated - use top_class
{
  "repository": "CultureBotAI/CMMMech",
  "valid_reviews": 238,
  "coverage": "declared_scopes_only"
}
exit 0; log SHA256 476cf6991af17596e4e5718bd76dc22b1a671db2ac171cec57be6abf1ff14c56
```

An additional hidden/ignored-inclusive inventory verifies 203/203 current records have completed positive scientific reviews with matching exact hashes. There are 234 canonical histories, 238 structured reviews and 38 available review-base commits. Offline validation verifies structure and provenance, not scientific truth.

No schema, validator, test, skill or governance behavior changed. Raw source articles, figures and supplementary files remain outside Git.

## Publication and follow-up

Live read-only checks verified merged CLAW admission PR 581, the active SQUASH/ALLGREEN main queue with no ruleset bypass actors, four active workflows and open source issues 103/104/120. Canonical history and pinned governance artifacts are installed locally. The shepherd is manual/comment-only and defaults to dry run; installed configuration does not establish credential readiness. Future governance updates must use CLAW’s supported admission/synchronization process. This batch does not configure governance.

All new review bases are on main. The existing annotated `review-base/cmm-source-survey-20261009` reference preserves the earlier otherwise-lost source-survey base. Publication requires explicit tag fetching and an isolated squash-shaped checkout without the topic commit. After native queue merge and owned-branch deletion, a fresh remote-main clone must pass full checks again; actual postmerge results belong in the PR closeout receipt.

Source-acquisition issues [#103](https://github.com/CultureBotAI/CMMMech/issues/103), [#104](https://github.com/CultureBotAI/CMMMech/issues/104) and [#120](https://github.com/CultureBotAI/CMMMech/issues/120) remain open. Issue #120 tracks the earlier missing meta-autunite figure verification. This round also retains a source-only rhabdophane deferral: structural identity and microbial causality were not established, so no rhabdophane record or CREATE history was added. [Remaining priorities](round37-frontier-20261011.md) include precise rare-earth phosphate phases, additional oxalate studies, source-access tasks and exploratory mineral leads. The source frontier is not exhausted.
