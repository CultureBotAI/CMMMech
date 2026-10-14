# Initial independent SmCo scrap precipitation source-locator review

- Review: 20261014T185757Z-samarium-cobalt-magnet-scrap-round79-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T18:55:59.376651Z
- Finished UTC: 2026-10-14T18:57:57.381848Z
- Reviewer: codex /root/round68_phosphates (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed minor source-section locator error, preserved before correction. This scoped initial observation is not complete scientific acceptance of the resource.

## Scope And Provenance

Exact whole owner read, with adjudication restricted to precipitation source-section locator; full methods/graphics assessment continues separately.

Selection: Assigned exact owner; native inspect before judgment; author flagged the possible error and reviewer independently verified original section labels.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e3ac010053a78aad7650bb2608a1f0110e4cd8bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:samarium-cobalt-magnet-scrap | data/records/samarium-cobalt-magnet-scrap.yaml | maintained | Samarium Cobalt Magnet Scrap |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:samarium-cobalt-magnet-scrap | Actual named validation completed with one record and zero failures. |
| Final batch checks pending | unavailable | True | cmmmech:samarium-cobalt-magnet-scrap | Current cohort and correction are not yet frozen; coordinator has not supplied a final terminal receipt. |

## Scientific And Domain Assessments

### Precipitation methods source locator

provenance: concern. Targets: cmmmech:samarium-cobalt-magnet-scrap.

Section 2.3.2 denotes solvent extraction, while precipitation methods are Section 2.3.3. The retained Section 3.3 correctly identifies precipitation results; conditions are not adjudicated changed by this locator finding.

## Findings

### F1: Correct the precipitation methods section locator

minor / open / confirmed; issue key: CMMMech.samarium-cobalt-magnet-scrap.precipitation-section-locator.

The second mechanism context cites Sections 2.3.2 and 3.3. Original Section 2.3.2 is Solvent Extraction; Section 2.3.3 is Precipitation. Replace only 2.3.2 with 2.3.3, preserving 3.3 and supported conditions. Tracked as https://github.com/CultureBotAI/CMMMech/issues/260.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-section number, append canonical EDIT and inline history, preserve initial owner evidence and this observation, then save an explicit resolution successor after affected checks.

- Context cites Sections 2.3.3 and 3.3; conditions unchanged unless independently supported new findings arise.
- Canonical EDIT and inline event link issue 260; original CREATE remains unchanged.
- Affected validation and final batch gates pass; successor retains issue_key and exact previous_occurrences.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/samarium-cobalt-magnet-scrap.yaml; mechanisms[id=samarium_precipitation_and_oxide_conversion].context | supports | Entire exact owner read after native inspect; the precipitation context cites Sections 2.3.2 and 3.3. |
| primary | https://doi.org/10.1021/acsomega.0c04132; Original JATS sec2.3.2, sec2.3.3 and sec3.3; actual artifact /private/tmp/cmm-round79-frontier-research/smco2021.xml | supports | Original section 2.3.2 is Solvent Extraction; 2.3.3 is Precipitation. Section 3.3 provides the detailed samarium precipitation results. |
| named | /private/tmp/cmm-round79-resource-reviews/smco-initial-named.log; Actual named command ['uv', 'run', '--locked', 'cmmmech', 'validate', 'data/records/samarium-cobalt-magnet-scrap.yaml', '--require-records']; started 2026-10-14T18:57:53.790499Z finished 2026-10-14T18:57:57.381848Z | supports | One record passed, zero failures; actual exit 0. |

## Limits And Additional Notes

- Partial observation limited to source locator; full original graphics, source recipe conflicts and recovery denominator assessment remains in progress.
- No completed batch, hosted CI or publication acceptance is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T185757Z-samarium-cobalt-magnet-scrap-round79-initial
kind: record
repository: CultureBotAI/CMMMech
title: Initial independent SmCo scrap precipitation source-locator review
started_at: '2026-10-14T18:55:59.376651Z'
finished_at: '2026-10-14T18:57:57.381848Z'
reviewer:
  identity: codex /root/round68_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Resource authored by round68_new_frontier. Reviewer authored
    only stevensite and sauconite, independently inspected the exact owner and original
    section labels; no owner or history edit.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Confirmed minor source-section locator error, preserved before correction.
  This scoped initial observation is not complete scientific acceptance of the resource.
source:
  git_revision: e3ac010053a78aad7650bb2608a1f0110e4cd8bf
  state: working_tree
  inputs:
  - path: data/records/samarium-cobalt-magnet-scrap.yaml
    sha256: b451f6a75dee9631629426aadc9d1fb157cdbb9502daca7c1029d63b26db628e
    role: target
  - path: history/records/samarium-cobalt-magnet-scrap/2026-10-14T184942Z-codex-b95702.yaml
    sha256: f5d9e2a1270047c69fa880a8209f0bf9aba08267530d3ce5377dbb2e4c7b28c7
    role: context
scope:
  description: Exact whole owner read, with adjudication restricted to precipitation
    source-section locator; full methods/graphics assessment continues separately.
  selection: Assigned exact owner; native inspect before judgment; author flagged
    the possible error and reviewer independently verified original section labels.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
targets:
- target_id: cmmmech:samarium-cobalt-magnet-scrap
  path: data/records/samarium-cobalt-magnet-scrap.yaml
  label: Samarium Cobalt Magnet Scrap
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium-cobalt-magnet-scrap.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/samarium-cobalt-magnet-scrap.yaml
    --require-records
  status: passed
  required: true
  summary: Actual named validation completed with one record and zero failures.
  target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Final batch checks pending
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base e3ac010053a78aad7650bb2608a1f0110e4cd8bf
  status: unavailable
  required: true
  summary: Current cohort and correction are not yet frozen; coordinator has not supplied
    a final terminal receipt.
  target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/samarium-cobalt-magnet-scrap.yaml
  locator: mechanisms[id=samarium_precipitation_and_oxide_conversion].context
  accessed_at: '2026-10-14T18:57:57.381848Z'
  support: supports
  summary: Entire exact owner read after native inspect; the precipitation context
    cites Sections 2.3.2 and 3.3.
  snapshot_sha256: b451f6a75dee9631629426aadc9d1fb157cdbb9502daca7c1029d63b26db628e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/acsomega.0c04132
  locator: Original JATS sec2.3.2, sec2.3.3 and sec3.3; actual artifact /private/tmp/cmm-round79-frontier-research/smco2021.xml
  accessed_at: '2026-10-14T18:57:57.381848Z'
  support: supports
  summary: Original section 2.3.2 is Solvent Extraction; 2.3.3 is Precipitation. Section
    3.3 provides the detailed samarium precipitation results.
  snapshot_sha256: bb5a3553c82d2b50d38025b7dbf5e2a532e75274baac739523d44286de8bf7e5
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round79-resource-reviews/smco-initial-named.log
  locator: Actual named command ['uv', 'run', '--locked', 'cmmmech', 'validate', 'data/records/samarium-cobalt-magnet-scrap.yaml',
    '--require-records']; started 2026-10-14T18:57:53.790499Z finished 2026-10-14T18:57:57.381848Z
  accessed_at: '2026-10-14T18:57:57.381848Z'
  support: supports
  summary: One record passed, zero failures; actual exit 0.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
assessments:
- assessment_id: locator
  area: provenance
  topic: Precipitation methods source locator
  outcome: concern
  summary: Section 2.3.2 denotes solvent extraction, while precipitation methods are
    Section 2.3.3. The retained Section 3.3 correctly identifies precipitation results;
    conditions are not adjudicated changed by this locator finding.
  evidence_ids:
  - record
  - primary
  target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
findings:
- finding_id: F1
  issue_key: CMMMech.samarium-cobalt-magnet-scrap.precipitation-section-locator
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the precipitation methods section locator
  description: The second mechanism context cites Sections 2.3.2 and 3.3. Original
    Section 2.3.2 is Solvent Extraction; Section 2.3.3 is Precipitation. Replace only
    2.3.2 with 2.3.3, preserving 3.3 and supported conditions. Tracked as https://github.com/CultureBotAI/CMMMech/issues/260.
  target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
  field_paths:
  - mechanisms[id=samarium_precipitation_and_oxide_conversion].context
  evidence_ids:
  - record
  - primary
  rule_id: precise-primary-source-locator
  native_severity: minor
  normalization_reason: Bounded incorrect source-section number; material identity
    and stated precipitation conditions are not shown false by this finding.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium-cobalt-magnet-scrap.yaml
    role: maintained_record
actions:
- action_id: A1
  description: Correct the source-section number, append canonical EDIT and inline
    history, preserve initial owner evidence and this observation, then save an explicit
    resolution successor after affected checks.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:samarium-cobalt-magnet-scrap
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium-cobalt-magnet-scrap.yaml
    role: maintained_record
  acceptance_checks:
  - Context cites Sections 2.3.3 and 3.3; conditions unchanged unless independently
    supported new findings arise.
  - Canonical EDIT and inline event link issue 260; original CREATE remains unchanged.
  - Affected validation and final batch gates pass; successor retains issue_key and
    exact previous_occurrences.
limitations:
- Partial observation limited to source locator; full original graphics, source recipe
  conflicts and recovery denominator assessment remains in progress.
- No completed batch, hosted CI or publication acceptance is asserted.
```
