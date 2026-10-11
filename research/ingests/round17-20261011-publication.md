# Round 17 reviewed mineral groups, enstatite and RO concentrate

Worktree: `/private/tmp/CMMMech-expansion-round17-20261011`.
Branch: `curate/cmm-expansion-round17-20261011`.
Trusted base: `4504ab1c5a005ea31e65318c3b3f206d6fbf44ed`.
Acceptance: [issue #65](https://github.com/CultureBotAI/CMMMech/issues/65).

Four additions bring the corpus to **132 records**: enstatite as a mineral
species, olivine and biotite as mineral groups, and reverse-osmosis concentrate
as a process-generated secondary resource. No new criticality designation or
industrial microbial deployment is asserted. Every addition has a genuine
CREATE sidecar and distinct inline event.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Biotite mica series](../../data/records/biotite.yaml) | mineral_group | [YAML](../../reviews/structured/20261011T105429Z-biotite-round17-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T105429Z-biotite-round17-independent/review.md) |
| [Enstatite](../../data/records/enstatite.yaml) | mineral | [YAML](../../reviews/structured/20261011T105423Z-enstatite-round17-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T105423Z-enstatite-round17-independent/review.md) |
| [Olivine group](../../data/records/olivine-group.yaml) | mineral_group | [YAML](../../reviews/structured/20261011T105423Z-olivine-group-round17-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T105423Z-olivine-group-round17-independent/review.md) |
| [Reverse osmosis concentrate](../../data/records/reverse-osmosis-concentrate.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T105455Z-reverse-osmosis-concentrate-round17-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T105455Z-reverse-osmosis-concentrate-round17-independent/review.md) |


The reviewers did not author their targets. Review verdicts and limitations are
preserved in the linked immutable YAML/Markdown observations. The
[manifest](round17-frontier-20261011.json) records exact final hashes and history
references. Any actionable finding requires correction and a successor review
before queue admission; source limitations alone do not justify invented issues.

Publication-package self-review found incorrect fungal wording in the two new
README rows for the bacterial Klug study. [Review issue #66](https://github.com/CultureBotAI/CMMMech/issues/66)
tracks the correction to bacterial wording and independent verification. The
record YAML already identified Gluconobacter correctly, so no artificial record
edit or history event was added for that summary correction.

Enstatite and olivine share the Klug2026 experiment. Phase-specific modeled
dissolution cannot be treated as directly measured pure-mineral recovery; the
mixed feed, technical replication, unmatched pH, and conflicting magnesium
denominators remain explicit. Biotite denotes the mica series rather than a
guessed member species. Its source's siderophore threshold conflict and gene
expression correlations do not establish a molecular cause.

The RO-concentrate mechanism comes from the full USBR report and accepted-paper
appendix. Sludge plus glycerin was compared with controls lacking both; their
individual contributions remain unresolved. SEM/EDS and modeling do not establish
pure gypsum or calcite recovery. Three-liter experiments remain distinct from
modeled million-liter process projections and subsequent nonmicrobial ion exchange.

## Sources and remaining work

- [Enstatite and olivine dossier](round17-enstatite-sources-20261011.md) and [JSON receipt](round17-enstatite-sources-20261011.json).
- [Biotite dossier](round17-biotite-sources-20261011.md) and [JSON receipt](round17-biotite-sources-20261011.json).
- [Saline-feed dossier](round17-saline-sources-20261011.md) and [JSON receipt](round17-saline-sources-20261011.json).
- [Prioritized remaining ingests](round17-frontier-20261011.md).

Timestamped discovery artifacts under `research/sources/` retain acquisition,
authority, search and access boundaries. Raw full text stays outside Git.
Further silicate studies, process-specific catalysts, produced-water main-text
gaps and earlier feed/grade leads remain concrete work. This publication does
not establish global source or material exhaustion.

## Validation and preservation

Baseline: **308 tests passed, three skipped**, 128 records and 144 histories.
Final native check: **308 passed, 3 skipped in 98.20s (0:01:38)**; 132 records and 148 histories valid.
Separate nonempty-corpus and trusted-base history checks passed. No schema or
validator behavior changed; no new behavioral regression was needed.

Structured review validation passed for 147 review pairs. All 132 current records
have independent scientific coverage matching their exact current hashes.
All **810** earlier tracked scientific-tree files (`data`, `history`, `reviews`,
`research`) remain byte-identical to the trusted base. All **18** distinct saved
review bases resolve; the annotated source-survey provenance tag is unchanged.
New observations use the already merged trusted base.

All 22 governed artifacts match CLAW pin
`a5d562962c75a2ad9efd8160b548df5944315422`. The checked main ruleset remains
active SQUASH/ALLGREEN, requires `validate-strict` from App15368, and has no
bypass actors. Fleet admission and shared history are installed. PR shepherd
remains manual and comment-only; extending its permissions or schedule needs
the supported CLAW process and separate writer/reviewer identity readiness.
No governance or installed-skill changes are part of this batch.

Independent publication audit, exact-tree squash-shaped verification, required
queue CI, and fresh remote-main validation after branch deletion complete the
publication process. Their terminal receipts will be posted on the PR. Original
main advances only after ignored/untracked collision checks and matching
before/after snapshots; unrelated worktrees and branches remain intact.
