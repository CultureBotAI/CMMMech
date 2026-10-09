# Independent concentration-observation implementation review

## Target, reviewer and UTC timestamp

Target: native concentration-observation schema, validator, documentation and
synthetic regression tests. Reviewer: `/root/ingest_ree`, Codex (GPT-6),
independent of `/root/ingest_bes`, who implemented these changes. This reviewer
curated concurrent EU criticality additions, which are excluded from this
implementation acceptance.

UTC timestamp: **2026-10-09T05:55:52Z**, read from the UTC clock.

## Reviewed revision and working changes

Worktree `/private/tmp/CMMMech-source-survey-20261008`, branch
`research/cmm-source-survey-20261008`, HEAD
`610d27a40d89861961052f0e0bebfaa7882e35cf` plus the uncommitted implementation
listed below. The test file is new/untracked. The implementation owner confirmed
these bytes are final; this review does not claim they are contained in HEAD.

| Path | SHA-256 |
| --- | --- |
| `src/cmmmech/schema/cmmmech.yaml` | `861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c` |
| `src/cmmmech/validation.py` | `510e7ed92887ea6e8c8e5828af378ffe0aa737772f8188ade6b42bde14bb5dfa` |
| `docs/records.md` | `8317d5eea81d1d609155e56621bf954486e528f57f9e061b92757a99f8a9739c` |
| `tests/test_observations.py` | `e1d48c5b449d54689207e0e0ad160b8e2e9531e890f7d024982d2b9f607130b8` |

Concurrent changes to six records, new history sessions and research/review
artifacts were visible and preserved. No implementation or record file was
edited by this review.

## Scope and evidence checked

Read applicable `CLAUDE.md`, record documentation and review skill; inspected
the full implementation diff, surrounding validation code, synthetic fixture,
all new tests and the
[BES concentration dossier](../../research/ingests/bes-concentration-observations-20261009.md).
The dossier establishes the concrete eight-cell curation need and source
interpretation; independent record reviews by the coordinator cover those
actual U/V cells. This review assesses behavior and adequacy of the native
contract, not a second independent scientific acceptance of those cells.

Hidden/ignored-inclusive searches of `src`, `tests` and `docs` located the
new observation type and implementation references. Review checks included:

- Optional mechanism nesting and backward compatibility; a nonempty list when
  supplied; closed fields and required source/sample/analyte/fraction context.
- Measured versus censored states, exclusion of the other numeric field,
  nonnegative measured values, strictly positive detection limits and finite
  values. A censored boundary cannot silently become a measured zero.
- Exact decimal comparison to the retained numeric source token. Finite large
  integers avoid forced float conversion; unrepresentable source exponents
  report errors; `copy_abs` preserves a long censored mantissa without rounding.
- Schema/type checks occur before record-local logic, preventing missing-key,
  incompatible-type and malformed-date paths from entering assumptions used
  by the business rules. YAML NaN/infinity handling is explicitly covered.
- Source resolution to both the record and parent evidence; record-wide
  observation-ID and source-cell uniqueness, including across mechanisms.
- Collection date/provenance pairing, collection-before-analysis ordering and
  preservation of unresolved dates. An analysis date is never silently used
  as collection time or experiment ordering.
- Documentation keeps mg/kg distinct from mg/L, elemental analyte identifiers
  distinct from oxidation-state measurements, assigned arms distinct from
  actual cell presence, and observations distinct from microbial effects or
  purified recovery yields.

## Findings by severity

- **Critical:** none identified within implementation scope.
- **Major:** none identified within implementation scope.
- **Minor:** none requiring correction identified in the final bytes.
- **Informational:** the class intentionally accepts only numeric-token,
  mass-based mg/kg concentration observations. It is not a general measurement
  or statistics model. Other units, comparator strings, rates, percentages,
  missing cells and aggregate estimates require later evidence-led design.
- **Informational:** a matching negative token and positive boundary alone
  cannot prove the publisher used a detection-limit convention. The reviewer
  must inspect the dataset dictionary and distinguish sentinels such as
  `-9999`. Documentation explicitly retains this obligation; a universal
  negative-value interpretation is not automated.
- **Informational:** exact sample labels and date locators remain curator
  assertions. Local uniqueness checks prevent duplication of a declared cell,
  but cannot establish that two labels denote the same physical sample or that
  treatments are scientifically comparable. These remain record-review duties.

## Corrections and validation

No corrections were made in this independent round. The coordinator had
previously identified three numeric edge cases; the final implementation and
regression tests address large finite integers, unrepresentable source exponents
and unrounded censored mantissas. This reviewer independently reran the tests
containing those cases.

Commands executed by this reviewer in the shared worktree:

- `.venv/bin/pytest -q tests/test_observations.py tests/test_validation.py`:
  **104 passed**.
- `git diff --check`: passed.
- `.venv/bin/cmmmech validate --require-records`: **10 checked, 0 failed**.

The coordinator separately reports the completed combined `just check` gate:
lint passed, **280 tests passed, 3 existing optional-command skips**, ten
valid records and 19 valid histories. That full-suite result is attributed to
the coordinator; this reviewer did not duplicate it after the targeted pass.

## Unresolved questions and verdict

**Accept with the documented contract limits.** No blocking implementation
finding remains. Future sources with other units, less-than strings, replicate
statistics or different missing-value conventions require an explicit extension
with evidence and tests. Validation establishes local consistency, not source
truth or biological causality. U/V scientific acceptance and acceptance of
concurrent EU/Li curation remain in their separate per-record review artifacts.
