# Round 13 reviewed mineral and resource expansion

Prepared in `/private/tmp/CMMMech-expansion-round13-20261011` on
`curate/cmm-expansion-round13-20261011`, trusted base
`14ceff0da3e19d6d36426d33f4cf577b8e64760f`.
Acceptance issue: [#54](https://github.com/CultureBotAI/CMMMech/issues/54).

Eight new records extend mineral and secondary-resource coverage while preserving
conceptual boundaries. The corpus now has **101 records**: 64 elements,
24 commodities, eight minerals and five secondary resources. Seven additions
have scoped microbial evidence, including a negative spodumene assay; the
metallurgical-coal family is an identity record with explicit coking-coal overlap.
The same study represented under an element and its feed does not become an
independent experimental replication.

## Records and independent reviews

| Record | Kind | Exact-state scientific review |
|---|---|---|
| [Pentlandite](../../data/records/pentlandite.yaml) | mineral | [YAML](../../reviews/structured/20261011T091034Z-pentlandite-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T091034Z-pentlandite-round13-independent/review.md) |
| [Jadarite](../../data/records/jadarite.yaml) | mineral | [YAML](../../reviews/structured/20261011T091034Z-jadarite-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T091034Z-jadarite-round13-independent/review.md) |
| [Spodumene](../../data/records/spodumene.yaml) | mineral | [YAML](../../reviews/structured/20261011T091034Z-spodumene-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T091034Z-spodumene-round13-independent/review.md) |
| [Colemanite](../../data/records/colemanite.yaml) | mineral | [YAML](../../reviews/structured/20261011T091034Z-colemanite-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T091034Z-colemanite-round13-independent/review.md) |
| [Spent lithium-ion battery black mass](../../data/records/battery-black-mass.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T090808Z-battery-black-mass-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T090808Z-battery-black-mass-round13-independent/review.md) |
| [Bauxite residue (red mud)](../../data/records/bauxite-residue.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T090808Z-bauxite-residue-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T090808Z-bauxite-residue-round13-independent/review.md) |
| [Phosphogypsum](../../data/records/phosphogypsum.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T090808Z-phosphogypsum-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T090808Z-phosphogypsum-round13-independent/review.md) |
| [Metallurgical coal commodity family](../../data/records/metallurgical-coal.yaml) | commodity | [YAML](../../reviews/structured/20261011T090808Z-metallurgical-coal-round13-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T090808Z-metallurgical-coal-round13-independent/review.md) |

Each new record has a real canonical CREATE sidecar under
`history/records/<slug>/`, referenced from its `history_refs`, and a separate
inline event. Review YAML and generated Markdown are immutable observations;
all final reviews are completed, independent and `pass_with_limitations`.
No unsupported criticality, pure-product recovery or industrial-scale claim
was introduced. Source problems remain explicit: mixed mineral phases and
unmatched acid additions; null spodumene results; colemanite composition
nonclosure; inconsistent battery inventories; and phosphogypsum model/real-feed
and unit/denominator differences.

## Research and remaining coverage

- [Mineral evidence and acquisition](round13-mineral-sources-20261011.md), with
  [machine-readable provenance](round13-mineral-sources-20261011.json).
- [Secondary-resource evidence](round13-secondary-sources-20261011.md), with
  [machine-readable provenance](round13-secondary-sources-20261011.json).
- [Six deferred commodity boundaries reassessed](round13-grade-boundaries-20261011.md),
  with [machine-readable provenance](round13-grade-boundaries-20261011.json).
- [Remaining ingest priorities](round13-frontier-20261011.md) and
  [current record hashes and historical-inventory reconciliation](round13-frontier-20261011.json).

The unchanged 94-candidate authority inventory now has 88 exact roots represented,
one designation-specific alias and five deferred grade labels. Exact-root
representation is not proof of every historical designation mapping. Further
mineral species, catalyst/ash feeds and narrower product forms remain concrete
leads. The broader discovery goal remains active; this is no global exhaustion
claim. Searches included hidden and ignored files within the stated boundaries.

## Validation and preservation

Baseline on the trusted base: 307 tests passed, three skipped; 93 records and
108 histories valid. Final batch: `just check` passed 307 tests, three skipped,
with 101 records and 116 histories valid. Separate
`uv run --locked cmmmech validate --require-records` and
`uv run --locked cmmmech validate-history --base 14ceff0da3e19d6d36426d33f4cf577b8e64760f`
also passed. The record-byte manifest was captured before those gates and
matched the final scientific reviews. Structured validation passed all 113 review pairs; a separate target/path/hash
audit verified independent scientific coverage for all 101 current records and
availability of all 14 source revisions. The governed sync check passed all
22 artifacts. An independent publication audit accompanies this package.

All 618 previously tracked files under `data`, `history`, `reviews`, and
`research` remain byte-identical to the trusted base. No schema, validator,
dependency, test behavior or governed artifact changed. Existing tests cover
the native contracts; source accuracy was assessed separately.

## Publication procedure

The batch follows the configured native squash queue, without bypassing checks.
All review source revisions must remain available; the existing annotated
`review-base/cmm-source-survey-20261009` tag is preserved. New observations use
the already merged trusted base above. Verify an isolated squash-shaped checkout
before queue admission and fresh remote main after merge and exact topic-branch
deletion. The final PR receipt records actual CI, merge, branch cleanup and
original-workspace preservation rather than retroactively changing these reviews.

Fleet/governance configuration is unchanged. Any future integration uses CLAW's
supported admission/synchronization process. Source curation does not authorize
or imply additional fleet capabilities.
