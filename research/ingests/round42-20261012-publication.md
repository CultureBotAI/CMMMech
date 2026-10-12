# Round 42 scientific review and publication report

This batch adds cemented tungsten carbide scrap, petalite and polylithionite, and extends birnessite with the separate Sasaki2009 binary cobalt/nickel sorption study. The corpus grows from 213 to 216 records. The two lithium minerals have identity and geological context only. Hardmetal culture/ferric treatment is kept separate from chemical powder preparation; undefined percentages and missing controls preclude a numerical recovery or microbial-advantage claim. No criticality designation or industrial deployment is inferred.

Worktree: `/private/tmp/CMMMech-expansion-round42-20261012`; branch: `curate/cmm-expansion-round42-20261012`; trusted base: `a5528a4807ba14fd8088a557ad105ac10ca62965`. Report generated at 2026-10-12T02:07:51.304026+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [birnessite](../../data/records/birnessite.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T020409Z-birnessite-round42-independent/review.md) / [YAML](../../reviews/structured/20261012T020409Z-birnessite-round42-independent/review.yaml) |
| [cemented-tungsten-carbide-scrap](../../data/records/cemented-tungsten-carbide-scrap.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T020432Z-cemented-tungsten-carbide-scrap-round42-independent/review.md) / [YAML](../../reviews/structured/20261012T020432Z-cemented-tungsten-carbide-scrap-round42-independent/review.yaml) |
| [petalite](../../data/records/petalite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T020333Z-petalite-round42-independent/review.md) / [YAML](../../reviews/structured/20261012T020333Z-petalite-round42-independent/review.yaml) |
| [polylithionite](../../data/records/polylithionite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T020335Z-polylithionite-round42-independent/review.md) / [YAML](../../reviews/structured/20261012T020335Z-polylithionite-round42-independent/review.yaml) |

All four completed independent scientific reviews match final record bytes. The [manifest](round42-frontier-20261012.json) pins each record, history chain, review, source dossier and completed gate receipt. Three CREATE and one EDIT history sessions were added. No corrective scientific-record findings remain. Earlier birnessite science is preserved; Sasaki2009 is a separate assay, not an extra replicate of 2008.

The birnessite extension retains the phase-distribution definition of the reported selectivity coefficient, source oxidation-state conflicts, unmatched phase/area comparator and ex situ XPS limits. Co(III) surface interpretation is not an isolated-product yield. The hardmetal study lacks matched sterile controls, culture-stock authentication and a complete mass balance; the publisher-declared DOI failed DOI/Crossref resolution, while two original PDF sources matched exactly. Its relative W content cannot establish WC phase purity. Petalite and polylithionite use dated IMA and original Handbook authorities; original mica nomenclature distinguishes lepidolite-series labels from a confirmed polylithionite specimen.

## Review correction and source deferral

[Issue #139](https://github.com/CultureBotAI/CMMMech/issues/139) tracks a genuine source-dossier provenance overstatement. The original Theisen paragraph assigned manuscript versions to differing publication dates without authority. The corrected wording preserves Wiley's First published 23 March 2016, Crossref's published-online 25 April 2016 and Oxford's June issue label, leaving version relationships unresolved. The [initial finding](../../reviews/publication/20261012-round42/20261012T015921Z-theisen-source-initial.md) and [independent successor](../../reviews/publication/20261012-round42/20261012T020112Z-theisen-source-resolution.md) retain the exact finding key and predecessor hash. This documentation correction changes no accepted record. Issue 139 is locally resolved and intended to close through the future PR.

[Issue #140](https://github.com/CultureBotAI/CMMMech/issues/140) separately tracks unavailable complete Theisen methods, original figures/tables and supplements. The source remains deferred; partial indexed text is not experimental acceptance. Earlier source issues #103, #104, #120, #129, #130, #133, #134 and #137 remain open. The [frontier](round42-frontier-20261012.md) gives concrete next work. No source exhaustion is claimed.

## Checks and preservation

The baseline reuses the freshly validated published base/tree: `/private/tmp/cmm-round41-postmerge-20261012-published-terminal.json`, SHA-256 `e4419f9b81546a9958657f3afd3ce255788addf5a35e34cb8d971819bdb2ae28`. It was not rerun before this curation. Actual final gates:

- `just check`: exit 0; log SHA-256 `4980aedbe1b677797b96f68809ecd197fb335257db08dd5e42f8677eca30b98f`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `253a7b1f24733e2960a5844348786b1f7b8c035bb10af8e25c914e2d5234e023`.
- `uv run --locked cmmmech validate-history --base a5528a4807ba14fd8088a557ad105ac10ca62965`: exit 0; log SHA-256 `c2a1a9ebbab06d77f85879fede0494f78da78b43ff3500e7c095428e8f54ba35`.
- `just review-check --base a5528a4807ba14fd8088a557ad105ac10ca62965 --require-reviews`: exit 0; log SHA-256 `687ef93ef9c4960abb5bba4d1543c066eb14c9769a5f7cdc1171bb7bceaac658`.

`just check` passed 308 tests with 3 skipped in 174.24 seconds, with 216 records and 252 histories valid. The separate native review checker validates 256 bundles; exact-hash coverage finds current completed positive scientific reviews for all 216 records, with 43 available review bases. Structural validation is distinct from scientific evidence assessment.

The [preservation receipt](../../reviews/publication/20261012-round42/preservation-prepublication.json) confirms 7,187 hidden/ignored original-main entries and eight bounded unrelated skill-worktree entries, including symlinks and Git states, against the initial snapshot. It describes prepublication state; fresh postmerge preservation is still required. Raw copyrighted originals remain outside Git with source-provenance manifests. No schema, validator, tests, skills or governed files changed in this batch.

## Integration and publication

The [live status summary](../../reviews/publication/20261012-round42/current-status.json) retains merged CLAW admission, the immutable governance pin, four active workflows and effective native SQUASH/ALLGREEN queue rules with required validate-strict and no bypass actors. These installed capabilities do not prove PR-shepherd credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Operational helper ports and the complete document package require [independent publication review](../../reviews/publication/20261012-round42). This report does not claim that commit, isolated squash-shaped validation, hosted PR/queue checks, merge, branch deletion or fresh-main validation have occurred. Those are subsequent guarded steps; actual outcomes belong in the PR closeout. The existing provenance tag retains the otherwise-lost historical review base, and all current bases must remain available in fresh-main checks.
