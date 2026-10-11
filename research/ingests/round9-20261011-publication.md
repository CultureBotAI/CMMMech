# Round 9 review and publication preparation

This batch adds cesium, strontium, ruthenium, rhodium, silicon and tin, bringing
the corpus to 54 records. Work was performed by codex / GPT-6 / codex in
`/private/tmp/CMMMech-expansion-round9-20261011`, branch
`curate/cmm-expansion-round9-20261011`, against trusted base
`9fa187ff5a455f495cfa2635e60c413b6763370d`.
[Issue 39](https://github.com/CultureBotAI/CMMMech/issues/39) tracks acceptance.
The original checkout and unrelated worktrees were preserved during curation.

## Scientific scope and reviews

The records cover washed-biomass Cs retention, Sr-bearing carbonate formation,
oxidized Ru deposition, separate single-metal and mixed-metal Rh experiments,
conditional diatom silicon utilization and organotin debutylation. They retain
organism/strain scope, feed chemistry, controls, assay denominators, conflicting
source details and laboratory limits. None converts solution depletion or
analytical recovery into an isolated-metal yield or industrial deployment.
Five records cite the named US 2025 list; strontium cites the original EU 2024
act. Those designations are scoped to their named editions and material mappings.

Different agents from the curators independently reviewed every final record.
All six final verdicts are **pass with limitations**, with no unresolved
corrective findings. Every review has an immutable YAML/Markdown pair:

| Final record | Independent scientific review |
|---|---|
| [Cesium](../../data/records/cesium.yaml) | [Markdown](../../reviews/structured/20261011T065833Z-cesium-round9-independent/review.md) · [YAML](../../reviews/structured/20261011T065833Z-cesium-round9-independent/review.yaml) |
| [Strontium](../../data/records/strontium.yaml) | [Markdown](../../reviews/structured/20261011T065833Z-strontium-round9-independent/review.md) · [YAML](../../reviews/structured/20261011T065833Z-strontium-round9-independent/review.yaml) |
| [Ruthenium](../../data/records/ruthenium.yaml) | [Markdown](../../reviews/structured/20261011T070023Z-ruthenium-round9-independent/review.md) · [YAML](../../reviews/structured/20261011T070023Z-ruthenium-round9-independent/review.yaml) |
| [Rhodium](../../data/records/rhodium.yaml) | [Markdown](../../reviews/structured/20261011T070023Z-rhodium-round9-independent/review.md) · [YAML](../../reviews/structured/20261011T070023Z-rhodium-round9-independent/review.yaml) |
| [Silicon](../../data/records/silicon.yaml) | [Markdown](../../reviews/structured/20261011T065917Z-silicon-round9-independent/review.md) · [YAML](../../reviews/structured/20261011T065917Z-silicon-round9-independent/review.yaml) |
| [Tin](../../data/records/tin.yaml) | [Markdown](../../reviews/structured/20261011T070409Z-tin-round9-resolution/review.md) · [YAML](../../reviews/structured/20261011T070409Z-tin-round9-resolution/review.yaml) |

The three curation dossiers provide evidence locators, search coverage,
identity checks, local raw-file receipts, source terms and unresolved questions:
[Cs/Sr](round9-cs-sr-20261011.md), [Ru/Rh](round9-ru-rh-20261011.md), and
[Si/Sn](round9-si-sn-20261011.md), each with a JSON companion.
The [graphite handoff](round9-graphite-handoff-20261011.md) is research for a
later commodity decision, not a seventh accepted record.

## Adversarial finding and correction

[Issue 40](https://github.com/CultureBotAI/CMMMech/issues/40) records one minor
tin overstatement. The initial review remains available as
[Markdown](../../reviews/structured/20261011T065917Z-tin-round9-independent/review.md)
and [YAML](../../reviews/structured/20261011T065917Z-tin-round9-independent/review.yaml).
It found that the source reports spike-recovery accuracy over 5–60 ng/g despite
documenting linear calibration curves only through 50 ng/g. The record and
dossier now distinguish those validations and preserve the narrower uncertainty
about dilution or a higher calibration range. Analytical recovery remains
separate from microbial extraction yield.

The linked final tin review explicitly resolves
`tin-calibration-recovery-validation` through exact predecessor occurrence
`20261011T065917Z-tin-round9-independent` / `tin-recovery-validation-scope`.
The CREATE session and initial reviews are unchanged; a new EDIT records the
actual correction. Initial tin/dossier bytes were retained outside Git with
hashes. Silicon's scientific record and dossier source section stayed unchanged;
its earlier review honestly attests the shared dossier state before the
Tin-only correction, while still covering the current silicon record hash.

## History and checks

Six actual CREATE sessions and one tin EDIT are linked in the records:

- [history/records/cesium/2026-10-11T065053Z-codex-6510dc.yaml](../../history/records/cesium/2026-10-11T065053Z-codex-6510dc.yaml)
- [history/records/strontium/2026-10-11T065059Z-codex-390f8d.yaml](../../history/records/strontium/2026-10-11T065059Z-codex-390f8d.yaml)
- [history/records/ruthenium/2026-10-11T065054Z-codex-52117e.yaml](../../history/records/ruthenium/2026-10-11T065054Z-codex-52117e.yaml)
- [history/records/rhodium/2026-10-11T065056Z-codex-dc19af.yaml](../../history/records/rhodium/2026-10-11T065056Z-codex-dc19af.yaml)
- [history/records/silicon/2026-10-11T065000Z-codex-0bbe5d.yaml](../../history/records/silicon/2026-10-11T065000Z-codex-0bbe5d.yaml)
- [history/records/tin/2026-10-11T065147Z-codex-9c1b8e.yaml](../../history/records/tin/2026-10-11T065147Z-codex-9c1b8e.yaml)
- [history/records/tin/2026-10-11T070055Z-codex-fdb5e2.yaml](../../history/records/tin/2026-10-11T070055Z-codex-fdb5e2.yaml)

Baseline: 307 tests passed, 3 skipped, with 48 records and 58 histories valid.
The final corrected record state passed `just check`: **307 passed, 3 skipped**
in 60.36 seconds. Separate `cmmmech validate --require-records` passed all
**54 records**, and trusted-base `validate-history` passed all **65 sessions**.
The structured-review check passed **61 pairs** against the trusted base.
The nonempty review gate is supplemented by explicit current-record hash
coverage, finding-lineage, prior-file preservation and source-receipt audits.
There are no schema, validator, dependency, test or governance changes.

## Publication and integration boundaries

All new reviews use the trusted main ancestor above. Across the complete corpus,
ten review bases must remain available: nine through main ancestry and
`c0adc2c0763e1515ed07dc712b024974d98fb342` through the existing annotated tag
`review-base/cmm-source-survey-20261009`. Its remote tag object
`fc4040c3abcd28f0a9cc52467e308100144ad1fd` and peeled target were verified.
No new tag or rewritten review base is needed.

The final governed-artifact check verified all 22 copies against immutable CLAW
pin `a5d562962c75a2ad9efd8160b548df5944315422`.
[CLAW admission PR 581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
was verified merged. The live main ruleset remains active with SQUASH/ALLGREEN,
required `validate-strict` and no bypass actors. The PR shepherd's governed
workflow remains manual and comment-only; its queried run list was empty.
A scoped dry run and verified writer/reviewer App separation remain concrete
operational follow-ups through CLAW's supported process, not local edits to
governed copies.

This report records local preparation, not an advance claim of a remote merge.
The PR's publication receipts will record its exact committed tree, fresh
independent PR review, isolated squash-shaped validation, queue checks, actual
merge, exact branch deletion and fresh-main verification. Original-checkout
advancement must first check collisions and preserve ignored/untracked bytes.

The [updated frontier](round9-frontier-20261011.md) retains **16 element and
30 overlapping commodity proposals**, plus opportunities beyond the historical
inventory. Natural graphite identity and commodity overlap are a concrete next
priority. Access gaps, unresolved controls and source inconsistencies remain
explicit research questions; no corpus-exhaustion claim is made.
