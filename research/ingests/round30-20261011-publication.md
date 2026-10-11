# Round30 curation and publication review

Worktree: `/private/tmp/CMMMech-expansion-round30-20261011`; branch: `curate/cmm-expansion-round30-20261011`; trusted base: `930ce995269f0ded5df009eb5916162971eb1f58`.

The batch adds basaltic rock, chromite, pyrrhotite and tungsten skarn tailings.
The first and last are natural and secondary resources; the others are mineral
species. Complete primary evidence supports conditional laboratory observations,
including negative dissolution limits and explicitly nonmicrobial separation.
No constituent criticality, recovery purity or industrial deployment is inherited.

All four final independent scientific reviews are completed qualified passes
matching the final record hashes. One minor review finding was corrected and
explicitly resolved: [issue #107](https://github.com/CultureBotAI/CMMMech/issues/107)
distinguishes the basalt assay's HNO3 reagent concentration from an unspecified
final sample concentration. The original CREATE history, source assessment and
initial review remain immutable; a new EDIT session, source correction and linked
successor review document the fix.

| Record | Final exact-state review |
|---|---|
| [Basaltic rock](../../data/records/basalt.yaml) | [YAML](../../reviews/structured/20261011T183306Z-basalt-round30-independent-final/review.yaml) · [Markdown](../../reviews/structured/20261011T183306Z-basalt-round30-independent-final/review.md) |
| [Chromite](../../data/records/chromite.yaml) | [YAML](../../reviews/structured/20261011T183417Z-chromite-round30-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T183417Z-chromite-round30-independent/review.md) |
| [Pyrrhotite](../../data/records/pyrrhotite.yaml) | [YAML](../../reviews/structured/20261011T183248Z-pyrrhotite-round30-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T183248Z-pyrrhotite-round30-independent/review.md) |
| [Tungsten skarn-processing tailings](../../data/records/tungsten-skarn-tailings.yaml) | [YAML](../../reviews/structured/20261011T183308Z-tungsten-skarn-tailings-round30-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T183308Z-tungsten-skarn-tailings-round30-independent/review.md) |

`just check` passed **308 tests, 3 skipped in 129.68 seconds**. Separate validation
with `--require-records` and trusted-base history validation passed: **180 records,
205 canonical history entries**, zero failures/errors. The structured-review gate
passed **209 bundles**. Current scientific review coverage is **180/180** with
exact record hashes; **31 review bases** remain available. This coverage check
supplements the canonical gate rather than treating a nonempty review directory
as complete scientific review.

The [manifest](round30-frontier-20261011.json) pins records, histories, reviews,
source assessments and terminal receipts. The [frontier](round30-frontier-20261011.md)
prioritizes remaining evidence acquisition. The unchanged 176-record starting
tree reused the immediately completed fresh-main baseline on that exact commit
and tree, with a hash-verified receipt; identical baseline tests were not rerun.
All required gates were executed after the new records and correction.

## Publication and preservation

A separate minor publication-helper finding, [issue #108](https://github.com/CultureBotAI/CMMMech/issues/108),
added a missing after-sync branch-identity assertion for the unrelated skill
worktree. The initial audit and independently checked correction are preserved
in [publication review artifacts](../../reviews/publication/20261011-round30).
This is a safeguard correction, not a scientific-record defect; synchronization
and its actual preservation receipt remain pending fresh postmerge validation.

No schema, validator, test or governed-file change was needed. All **1248**
previously tracked record, history, research and review files remain byte-identical
to the trusted base. Original main is clean and unrelated dirty skill work is
preserved; hidden and ignored files are included in the recorded preservation
boundaries. New source dossiers state their bounded deduplication searches and
access failures. This batch does not claim source exhaustion.

Before queue admission, enumerate all saved review bases, preserve any otherwise
lost commit under an annotated provenance tag, and verify the exact committed
tree in an isolated main-only squash-shaped checkout. Every new round30 review
uses the durable trusted main base. The existing `review-base/cmm-source-survey-20261009`
tag retains the older non-main base. After merge and topic-branch deletion, repeat
validation in a fresh remote-main clone. External publication and cleanup are
reported from subsequent actual receipts, not asserted by this prepublication file.

## Integration and remaining work

Live checks confirmed [fleet admission PR #581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
is merged and [fleet convergence issue #580](https://github.com/CultureBotAI/culturebotai-claw/issues/580)
is closed. Shared history and governed artifacts are installed; all **22** copies
match pinned CLAW revision `a5d562962c75a2ad9efd8160b548df5944315422`.
The PR shepherd remains manual and comment-only. The active native queue requires
`validate-strict` (App 15368), uses **SQUASH/ALLGREEN**, and has no bypass actors.
Future governance or adapter integration must use CLAW's supported admission and
synchronization processes; no fleet configuration is changed in this batch.

Evidence issues [#103](https://github.com/CultureBotAI/CMMMech/issues/103) and
[#104](https://github.com/CultureBotAI/CMMMech/issues/104) remain open. The distinct
tungsten-tailings resource does not resolve unavailable Han microbial methods,
and basalt evidence does not settle ilmenite's positive/null literature. Concrete
next work is full-text acquisition and experiment-overlap/control reconciliation,
followed by the prioritized chromite-tailings, basalt and pyrrhotite extensions.
Stronger PR-shepherd powers or additional adapters need separate reviewed fleet
capability work, not inferred enablement from successful curation or merge.
