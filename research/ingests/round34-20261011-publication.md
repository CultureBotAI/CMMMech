# Round 34 scientific review and publication report

Four new mineral records bring the corpus from 190 to 194: galena, greigite, mackinawite and uraninite. They add distinct phase-resolved transformation and biomineralization observations. Experimental feeds, strains, media, controls, fitted quantities and source contradictions remain explicit. No criticality is inherited from constituent elements and no industrial recovery claim is added.

Worktree: `/private/tmp/CMMMech-expansion-round34-20261011`; branch: `curate/cmm-expansion-round34-20261011`; trusted base: `38cef46aabbcb2b49536ed8c265c63646ff1da3d`. Unrelated work, including the older dirty add-record-skill worktree, is outside this change. The add-record skill is already maintained on main.

## Scientific reviews

| Record | Independent reviewer | Verdict | Saved Markdown / YAML |
|---|---|---|---|
| [galena](../../data/records/galena.yaml) | Codex /root | pass_with_limitations | [Markdown](../../reviews/structured/20261011T211457Z-galena-round34-independent/review.md) / [YAML](../../reviews/structured/20261011T211457Z-galena-round34-independent/review.yaml) |
| [greigite](../../data/records/greigite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T211823Z-greigite-round34-independent/review.md) / [YAML](../../reviews/structured/20261011T211823Z-greigite-round34-independent/review.yaml) |
| [mackinawite](../../data/records/mackinawite.yaml) | Codex /root/round27_superalloy | pass_with_limitations | [Markdown](../../reviews/structured/20261011T211510Z-mackinawite-round34-independent/review.md) / [YAML](../../reviews/structured/20261011T211510Z-mackinawite-round34-independent/review.yaml) |
| [uraninite](../../data/records/uraninite.yaml) | Codex /root/round27_eaf_slag | pass_with_limitations | [Markdown](../../reviews/structured/20261011T211455Z-uraninite-round34-independent/review.md) / [YAML](../../reviews/structured/20261011T211455Z-uraninite-round34-independent/review.yaml) |

The reviewers captured the exact record, history and schema inputs before judgment. All final scientific reviews match the final record hashes. No corrective record finding was identified in these reviews; already disclosed source limitations are not fabricated GitHub defects. The [manifest](round34-frontier-20261011.json) supplies exact paths, hashes, histories, dossiers and actual gate receipts.

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
308 passed, 3 skipped in 195.87s (0:03:15)
Checked 194 record(s); 0 failed.
Checked 224 history record(s); 0 error(s).
exit 0; log SHA256 84e966930d55b1bbc3527e149d252fd1dfe7f3ec0454f71b71aaceb517ebf5c8
```

```text
uv run --locked cmmmech validate --require-records
Checked 194 record(s); 0 failed.
exit 0; log SHA256 9a1c693b6ef6256da07b28e732785b92b62fc090e964b3303620f782db991cd9
```

```text
uv run --locked cmmmech validate-history --base 38cef46aabbcb2b49536ed8c265c63646ff1da3d
Checked 224 history record(s); 0 error(s).
exit 0; log SHA256 70d4c90358c71eeb843da5b2f1b671d7ee9275ecd4d3c4dcb3330d4db4ed3d6f
```

```text
just review-check --base 38cef46aabbcb2b49536ed8c265c63646ff1da3d --require-reviews
uv run python scripts/record_review.py check "$@"
topClass is deprecated - use top_class
{
  "repository": "CultureBotAI/CMMMech",
  "valid_reviews": 228,
  "coverage": "declared_scopes_only"
}
exit 0; log SHA256 feb898ad626427cb4277d04ba5ec3172bae329691801508b8878ddd76eee0c72
```

An additional hidden/ignored-inclusive inventory verifies 194/194 current records have completed positive scientific reviews with matching exact hashes. There are 224 canonical histories, 228 structured reviews and 35 available review-base commits. Offline validation verifies structure and provenance, not scientific truth.

No schema, validator, test, skill or governance behavior changed. The existing contract represents these observations without new fields. Raw source articles, figures and supplementary files remain outside Git.

## Publication and follow-up

CLAW fleet admission, canonical history, vendored governance, PR shepherd and native merge-queue configuration are installed. The active queue uses SQUASH/ALLGREEN; the shepherd remains manual/comment-only. Future governance updates must use CLAW’s supported synchronizer and immutable pin. This curation does not alter those controls.

Every new review uses the trusted main base above, which survives a squash. Historical bases remain available through main history plus the existing annotated `review-base/cmm-source-survey-20261009` tag. Before queue admission, the exact committed tree must pass an isolated squash-shaped checkout without the topic commit. After merge and owned-branch deletion, fresh remote main must pass full checks again; those actual results belong in the PR closeout receipt rather than a pre-merge claim.

Source-acquisition issues [#103](https://github.com/CultureBotAI/CMMMech/issues/103) and [#104](https://github.com/CultureBotAI/CMMMech/issues/104) remain open. [Remaining priorities](round34-frontier-20261011.md) include anglesite and ningyoite candidates plus source-specific extensions of the four mineral owners. The investigated frontier is not exhausted.
