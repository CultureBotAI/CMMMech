# Round 50 scientific review and publication report

Add indite, monazite-(Ce) and xenotime-(Y) mineral identities, oil-sands froth-treatment tailings as a secondary resource, and a mixed xenotime-concentrate primary resource. The corpus grows from 241 to 246 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round50-20261012`; branch: `curate/cmm-expansion-round50-20261012`; trusted base: `98e787e8d61593797aef1ed29840b2315a0cc6e5`. Generated at 2026-10-12T07:59:39.418528+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [indite](../../data/records/indite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T075351Z-indite-round50-science/review.md) / [YAML](../../reviews/structured/20261012T075351Z-indite-round50-science/review.yaml) |
| [monazite-ce](../../data/records/monazite-ce.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T075358Z-monazite-ce-round50-science/review.md) / [YAML](../../reviews/structured/20261012T075358Z-monazite-ce-round50-science/review.yaml) |
| [xenotime-y](../../data/records/xenotime-y.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T075547Z-xenotime-y-round50-science/review.md) / [YAML](../../reviews/structured/20261012T075547Z-xenotime-y-round50-science/review.yaml) |
| [oil-sands-froth-treatment-tailings](../../data/records/oil-sands-froth-treatment-tailings.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T075351Z-oil-sands-froth-treatment-tailings-round50-science/review.md) / [YAML](../../reviews/structured/20261012T075351Z-oil-sands-froth-treatment-tailings-round50-science/review.yaml) |
| [xenotime-concentrate](../../data/records/xenotime-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T075254Z-xenotime-concentrate-round50-independent/review.md) / [YAML](../../reviews/structured/20261012T075254Z-xenotime-concentrate-round50-independent/review.yaml) |

All 5 independent final scientific reviews match the current record bytes. The [manifest](round50-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Natural mineral identities remain separate from constituent elements, synthetic analogues and mixed experimental feeds. The tailings record separates chemical acid-column mobilization from field microbial-community associations. The xenotime-concentrate study supports laboratory culture-associated mobilization with qualified organic-acid interpretation, mixed phases and no isolated-product yield or industrial deployment. No new record inherits elemental criticality.

## Findings and corrections

Five independent final scientific reviews cover the exact current record bytes. Review issue #158 corrects one minor xenotime-(Y) synthetic-comparator attribution error, preserving the initial finding, source dossier, actual EDIT history and exact successor lineage. No unresolved corrective finding remains in their assessed scope. Review issues: [#158](https://github.com/CultureBotAI/CMMMech/issues/158).

- `CMMMech.xenotime-y.synthetic-comparator-attribution`: resolved in the final review, retaining [the preceding observation](../../reviews/structured/20261012T074809Z-xenotime-y-round50-initial/review.md) and exact predecessor `F1`.

Scientific source limitations remain documented. For issue #153, newly inspected Bansal2007 original Figures 2, 3 and 5 narrow the missing evidence; original Figures 1 and 4 and complete Hedrich2023 evidence remain outstanding. The issue stays open. Acquisition issues remain open; see the [frontier](round50-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round49-postmerge-20261012-published-terminal.json`, SHA-256 `679df12f7a81172f338da3c6044a1e181fcbfd396ed9a7aecf8d79ebc164fd6a`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `dcc7d1261abfca630c5a13f9ed142b85bb1462960ff410d2072f7b14d4c3908a`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `5599312a3ee08a5df1b1f5d52f06e26aec1513ffe4bc0a5e4ef60dd00ea6e0aa`.
- `uv run --locked cmmmech validate-history --base 98e787e8d61593797aef1ed29840b2315a0cc6e5`: exit 0; log SHA-256 `bf614125e66d58201aeb2a712034842703a4c3090392cb57e00cd260c9c6e79a`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 98e787e8d61593797aef1ed29840b2315a0cc6e5 --require-reviews`: exit 0; log SHA-256 `07bf3bd3c56de032ccd918d2726fb24d5966a587de9cd58ca72c1f8fcab520e0`.

Final `just check`: 317 passed, 3 skipped in 166.09 seconds. The gates accept 246 records, 291 histories and 300 review bundles. Exact-hash coverage verifies 246/246 current scientific reviews and 51 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round50/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round50/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
