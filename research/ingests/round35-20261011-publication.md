# Round 35 scientific review and publication report

Four new mineral records bring the corpus from 194 to 198: anglesite, jarosite, ningyoite and schwertmannite. They add phase-resolved formation and reduction observations, with source reuse disclosed where another material owner represents the same experiment. Experimental feeds, strains, media, controls, fitted quantities and source contradictions remain explicit. No criticality is inherited from constituent elements and no industrial recovery claim is added.

Worktree: `/private/tmp/CMMMech-expansion-round35-20261011`; branch: `curate/cmm-expansion-round35-20261011`; trusted base: `f83cf867a38c470b4347f721d9ea9370c3019eaf`. Unrelated work, including the older dirty add-record-skill worktree, is outside this change. The add-record skill is already maintained on main.

## Scientific reviews

| Record | Independent reviewer | Verdict | Saved Markdown / YAML |
|---|---|---|---|
| [anglesite](../../data/records/anglesite.yaml) | Codex /root | pass_with_limitations | [Markdown](../../reviews/structured/20261011T215350Z-anglesite-round35-independent/review.md) / [YAML](../../reviews/structured/20261011T215350Z-anglesite-round35-independent/review.yaml) |
| [jarosite](../../data/records/jarosite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T215421Z-jarosite-round35-independent/review.md) / [YAML](../../reviews/structured/20261011T215421Z-jarosite-round35-independent/review.yaml) |
| [ningyoite](../../data/records/ningyoite.yaml) | Codex /root/round27_eaf_slag | pass_with_limitations | [Markdown](../../reviews/structured/20261011T215426Z-ningyoite-round35-independent/review.md) / [YAML](../../reviews/structured/20261011T215426Z-ningyoite-round35-independent/review.yaml) |
| [schwertmannite](../../data/records/schwertmannite.yaml) | Codex /root/round27_superalloy | pass_with_limitations | [Markdown](../../reviews/structured/20261011T215440Z-schwertmannite-round35-resolution/review.md) / [YAML](../../reviews/structured/20261011T215440Z-schwertmannite-round35-resolution/review.yaml) |

The reviewers captured the exact record, history and schema inputs before judgment. All final scientific reviews match the final record hashes. The first schwertmannite review identified one minor denominator-wording error, tracked in [issue #118](https://github.com/CultureBotAI/CMMMech/issues/118). The curator corrected the numerator/denominator wording, appended an EDIT history, and obtained a successor review that explicitly resolves the original occurrence. Both review rounds are retained, including the [initial finding](../../reviews/structured/20261011T214956Z-schwertmannite-round35-initial/review.md); the other three records had no corrective findings. Already disclosed source limitations remain separate research work. The [manifest](round35-frontier-20261011.json) supplies exact paths, hashes, histories, dossiers and actual gate receipts.

## Validation

The baseline reused the exact unchanged main commit/tree freshly tested after the previous merge; it is not reported as a newly executed baseline. Final batch commands below were newly executed for this batch.

```text
just check
uv run --locked --extra dev python scripts/check.py
All checks passed!
........................................................................ [ 23%]
........................................................................ [ 46%]
........................................................................ [ 69%]
....................................................sss................. [ 92%]
.......................                                                  [100%]
308 passed, 3 skipped in 119.23s (0:01:59)
Checked 198 record(s); 0 failed.
Checked 229 history record(s); 0 error(s).
exit 0; log SHA256 9801e41c5e7f39c58f9711c4b6a36747750740f6e2ccc7ea055ebc0db408af91
```

```text
uv run --locked cmmmech validate --require-records
Checked 198 record(s); 0 failed.
exit 0; log SHA256 1a7af2b5ea572ea7e356525122eadd4bbd64b3ce247bc0c1a7b3eb3b71865ae1
```

```text
uv run --locked cmmmech validate-history --base f83cf867a38c470b4347f721d9ea9370c3019eaf
Checked 229 history record(s); 0 error(s).
exit 0; log SHA256 6a35723bdc6888001561b265c4859a17d59b55bb8c460f13518e2b9d72d87b64
```

```text
just review-check --base f83cf867a38c470b4347f721d9ea9370c3019eaf --require-reviews
uv run python scripts/record_review.py check "$@"
topClass is deprecated - use top_class
{
  "repository": "CultureBotAI/CMMMech",
  "valid_reviews": 233,
  "coverage": "declared_scopes_only"
}
exit 0; log SHA256 fb52d81df6681925388db7ec93dd9e50644a4ad8c5d51fed50ddf75f810093ce
```

An additional hidden/ignored-inclusive inventory verifies 198/198 current records have completed positive scientific reviews with matching exact hashes. There are 229 canonical histories, 233 structured reviews and 36 available review-base commits. Offline validation verifies structure and provenance, not scientific truth.

No schema, validator, test, skill or governance behavior changed. The existing contract represents these observations without new fields. Raw source articles, figures and supplementary files remain outside Git.

## Publication and follow-up

CLAW fleet admission, canonical history, vendored governance, PR shepherd and native merge-queue configuration are installed. The active queue uses SQUASH/ALLGREEN; the shepherd remains manual/comment-only. Future governance updates must use CLAW’s supported synchronizer and immutable pin. This curation does not alter those controls.

Every new review uses the trusted main base above, which survives a squash. Historical bases remain available through main history plus the existing annotated `review-base/cmm-source-survey-20261009` tag. Before queue admission, the exact committed tree must pass an isolated squash-shaped checkout without the topic commit. After merge and owned-branch deletion, fresh remote main must pass full checks again; those actual results belong in the PR closeout receipt rather than a pre-merge claim.

Source-acquisition issues [#103](https://github.com/CultureBotAI/CMMMech/issues/103) and [#104](https://github.com/CultureBotAI/CMMMech/issues/104) remain open. [Remaining priorities](round35-frontier-20261011.md) include a uramphite identity candidate plus source-specific extensions of the four mineral owners. The investigated frontier is not exhausted.
