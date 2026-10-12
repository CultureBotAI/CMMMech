# Round 52 scientific review and publication report

Add four distinct owners: allanite concentrate and eudialyte ore primary resources, gold-mine tailings as a secondary resource, and yusupovite mineral identity. The corpus grows from 249 to 253 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round52-20261012`; branch: `curate/cmm-expansion-round52-20261012`; trusted base: `79ed7d69ea654d1b67bbf74bb931ff70c4c6913e`. Generated at 2026-10-12T09:32:36.991592+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [allanite-concentrate](../../data/records/allanite-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T092909Z-allanite-concentrate-round52-independent/review.md) / [YAML](../../reviews/structured/20261012T092909Z-allanite-concentrate-round52-independent/review.yaml) |
| [eudialyte-ore](../../data/records/eudialyte-ore.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T092440Z-eudialyte-ore-round52-science/review.md) / [YAML](../../reviews/structured/20261012T092440Z-eudialyte-ore-round52-science/review.yaml) |
| [gold-mine-tailings](../../data/records/gold-mine-tailings.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T092631Z-gold-mine-tailings-round52-science/review.md) / [YAML](../../reviews/structured/20261012T092631Z-gold-mine-tailings-round52-science/review.yaml) |
| [yusupovite](../../data/records/yusupovite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T092506Z-yusupovite-round52-science/review.md) / [YAML](../../reviews/structured/20261012T092506Z-yusupovite-round52-science/review.yaml) |

All 4 independent final scientific reviews match the current record bytes. The [manifest](round52-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

The three microbial feed studies retain genotype/organism uncertainty, pretreatment, mismatched chemistry controls, stronger chemical comparators and the distinction between solution extraction and isolated products. Yusupovite is grounded in the original natural mineral description and dated IMA identity, without inheriting proposed ion-exchange behavior. No constituent criticality or industrial deployment is inferred.

## Findings and corrections

Four independent scientific reviews assess final record bytes; source discrepancies and experimental limitations remain explicit.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. New source follow-up #163 tracks the fully acquired but not yet completely reviewed Lu2026 yeast-oxalate/allanite-leachate evidence. Existing acquisition issues remain open; narrow accepted records do not close their separate experimental gaps. Acquisition issues remain open; see the [frontier](round52-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round51-postmerge-20261012-published-terminal.json`, SHA-256 `0336230f47520b1b5039e5e8acb9b7770073916607828a72a7e27e9690880130`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `98c9a3c5b08e68cefe8dc71e984bff78ca3b8320a49f048a43ca0402489f5685`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `4a50f2f93e44bfb9e2561b166775c22abe8b3fb410bdcd90d2c75a2ff66d406a`.
- `uv run --locked cmmmech validate-history --base 79ed7d69ea654d1b67bbf74bb931ff70c4c6913e`: exit 0; log SHA-256 `6fab9a1f2f422f605fd0b242200596b27558aa866fa8b2dffabac4718cbce617`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 79ed7d69ea654d1b67bbf74bb931ff70c4c6913e --require-reviews`: exit 0; log SHA-256 `ddf63429afaf44ab229b9f39e582094bdde7014dea00de0377acbe95629cb1ed`.

Final `just check`: 317 passed, 3 skipped in 179.41 seconds. The gates accept 253 records, 299 histories and 309 review bundles. Exact-hash coverage verifies 253/253 current scientific reviews and 53 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round52/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round52/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
