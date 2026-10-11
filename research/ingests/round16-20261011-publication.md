# Round 16 reviewed silicates, iron minerals and produced-water identity

Worktree: `/private/tmp/CMMMech-expansion-round16-20261011`.
Branch: `curate/cmm-expansion-round16-20261011`.
Trusted base: `b714ce2bd8050d5e19ed9ca072460ba2b8154c3b`.
Acceptance: [issue #63](https://github.com/CultureBotAI/CMMMech/issues/63).

Six additions bring the corpus to **128 records**. Forsterite and talc retain
substrate-specific dissolution and a precipitation null in the same Cai2013
experiment. Lizardite records a separate C4-10 culture assay without assigning
causal necessity to correlated gene expression. Vivianite and siderite are
distinct phases from one Fe(II)-feed experiment, without a pure-product or
Fe(III)-reduction claim. Oil and gas produced water is an **identity-only
secondary resource** supported by USGS definitions and resource context.
No new criticality designation or industrial microbial deployment is asserted.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Forsterite](../../data/records/forsterite.yaml) | mineral | [YAML](../../reviews/structured/20261011T102935Z-forsterite-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T102935Z-forsterite-round16-independent/review.md) |
| [Lizardite](../../data/records/lizardite.yaml) | mineral | [YAML](../../reviews/structured/20261011T102943Z-lizardite-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T102943Z-lizardite-round16-independent/review.md) |
| [Oil and gas produced water](../../data/records/oil-and-gas-produced-water.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T102918Z-oil-and-gas-produced-water-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T102918Z-oil-and-gas-produced-water-round16-independent/review.md) |
| [Siderite](../../data/records/siderite.yaml) | mineral | [YAML](../../reviews/structured/20261011T103120Z-siderite-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T103120Z-siderite-round16-independent/review.md) |
| [Talc](../../data/records/talc.yaml) | mineral | [YAML](../../reviews/structured/20261011T102939Z-talc-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T102939Z-talc-round16-independent/review.md) |
| [Vivianite](../../data/records/vivianite.yaml) | mineral | [YAML](../../reviews/structured/20261011T103120Z-vivianite-round16-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T103120Z-vivianite-round16-independent/review.md) |


Every new record has a distinct inline CREATE event and canonical CREATE history
sidecar. The independent reviewers did not author their review targets. Their
reviews are qualified passes with zero actionable record findings, rather than
claims that source limitations have been resolved. See the
[record/hash/history manifest](round16-frontier-20261011.json).

The Cai2013 full-text methods and numerical tables were inspected, but visual
figures were unavailable through the acquisition routes tried. The records retain
the published phase assignment and do not claim diffraction reanalysis. The
Sheng2026 record preserves the pH pattern, uncertain feed purity and limitations
of siderophore and gene-expression interpretation. Its genome-method discrepancy
remains in the source dossier; no unsupported sequencing claim is curated.

The vivianite/siderite records preserve mixed phases, missing pH-matched controls,
the source's final-pH inconsistency, and unresolved fraction handling. Produced
water has no curated microbial mechanism: the acquired Hu2021 supplement cannot
replace unavailable main methods, and ND outcomes are not measured zero.

A package inspection caught the missing timestamped silicate discovery artifact;
it was saved with its actual persistence time before publication. Readability
corrections and a dossier-only follow-up attribution correction were completed
before final acceptance. No invented scientific finding, record edit or history
event was added merely to populate an issue list. Later publication-audit findings,
if any, require correction before queue admission and will be recorded on the PR.

## Sources and remaining work

- [Silicate source assessment](round16-silicate-sources-20261011.md) and [JSON receipt](round16-silicate-sources-20261011.json).
- [Vivianite/siderite source assessment](round16-vivianite-sources-20261011.md) and [JSON receipt](round16-vivianite-sources-20261011.json).
- [Produced-water source assessment](round16-produced-water-sources-20261011.md) and [JSON receipt](round16-produced-water-sources-20261011.json).
- [Prioritized remaining ingests](round16-frontier-20261011.md).

Timestamped source assessments are also retained under `research/sources/`.
The dossiers report actual acquisitions, source checks, hidden/ignored search
boundaries and access failures. Raw full text remains outside Git. Enstatite,
biotite group scope, produced-water mechanisms, other saline process feeds and
earlier catalyst/mineral-feed/grade leads remain concrete follow-up work; this
batch does not establish global source or material exhaustion.

## Validation and preservation

Baseline: **308 tests passed, three skipped**, 122 records and 138 histories valid.
Final native batch: **308 tests passed, three skipped** in 123.11 seconds,
128 records and 144 histories valid. Separate nonempty-corpus and trusted-base
history commands passed. No schema or validator behavior changed, so no new
behavioral regression was needed.

Structured review checks passed for 143 YAML/Markdown pairs. Every current record,
including all six additions, has independent scientific coverage matching its
exact current SHA-256. All **773** earlier tracked files under `data`, `history`,
`reviews` and `research` remain byte-identical to the trusted base. Saved reviews
and history remain append-only. All **17** distinct review bases resolve; the
annotated `review-base/cmm-source-survey-20261009` tag remains unchanged.
New observations use the already merged trusted base.

All 22 governed artifacts match CLAW pin
`a5d562962c75a2ad9efd8160b548df5944315422`. The checked main ruleset remains
active SQUASH/ALLGREEN with `validate-strict` from App15368 and no bypass actors.
Fleet admission and shared history are installed; PR shepherd remains manual
and comment-only. Future integration changes must use CLAW's supported process.
No governance or installed-skill change was needed in this batch.

An independent publication audit follows package assembly. An isolated
squash-shaped checkout must pass before queue admission, and a fresh remote-main
checkout after merge and branch deletion. Their actual results, CI runs and
cleanup receipts will be retained on the PR. The original checkout is advanced
only after collision checks and matching before/after snapshots that include
ignored and untracked files; unrelated worktrees and branches are preserved.
