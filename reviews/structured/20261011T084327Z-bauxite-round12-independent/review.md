# Independent round12 scientific review of Bauxite

- Review: 20261011T084327Z-bauxite-round12-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:34:19Z
- Finished UTC: 2026-10-11T08:43:27Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Heterogeneous aluminium ore commodity; its named minerals do not turn it into a single mineral species. Evidence supports this bounded state with explicit limitations.

## Scope And Provenance

Entire one-record scientific and provenance state.

Selection: Named independently assigned record, not a sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bauxite | data/records/bauxite.yaml | maintained | Bauxite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named strict record validation | passed | True | cmmmech:bauxite | Checked 1 record(s); 0 failed. |
| Completed batch check | passed | True | cmmmech:bauxite | 307 tests passed, 3 skipped; 93 records and 108 histories valid. |
| Nonempty corpus validation | passed | True | cmmmech:bauxite | 93 records checked; 0 failed. |
| Trusted-base append-only history validation | passed | True | cmmmech:bauxite | 108 history records checked; 0 errors. |

## Scientific And Domain Assessments

### Material boundary and edition-specific designation

identity: supported. Targets: cmmmech:bauxite.

Heterogeneous aluminium ore commodity; its named minerals do not turn it into a single mineral species.

### Actual curation and immutable working-state capture

provenance: supported. Targets: cmmmech:bauxite.

CREATE sidecar target and actor agree with the new record; inline descriptive event is distinct. No prior committed history was modified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/bauxite.yaml; Entire exact inspected record, attached CREATE history, schema and cohort dossier | supports | New commodity identity has its own root and actual codex/GPT-6/codex history. Root reviewer did not author these scientific bytes or histories. |
| authority | https://www.usgs.gov/centers/national-minerals-information-center/bauxite-and-alumina-statistics-and-information; https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng; USGS Bauxite and Alumina Statistics and Information overview; EU2024 original recital8 and AnnexI1(a)/II1(c). | supports | USGS live overview names gibbsite/boehmite/diaspore with impurities and applications. Both EU entries explicitly cover bauxite. No mechanism or extraction yield is asserted. |
| search | Local bounded identity search and live authority checks; data/records research reviews history; issuing pages | context_only | Search found current proposed roots and historical candidates, not grounds to equate commodities with element/mineral roots. Scientific absence beyond these boundaries is not asserted. |

## Limits And Additional Notes

- Review covers this exact commodity record only. Identity-only entries make no claim that microbial mechanisms do not exist.
- Raw artifacts acquired by curator were independently read; authority pages were also opened live. No independent laboratory replication or product-standard certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T084327Z-bauxite-round12-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent round12 scientific review of Bauxite
started_at: '2026-10-11T08:34:19Z'
finished_at: '2026-10-11T08:43:27Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Curated by separate /root/cmm12_aluminium_boron agent; root
    captured exact state before assessment and independently checked primary content/figures
    and official sources; no scientific record editing before this observation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Heterogeneous aluminium ore commodity; its named minerals do not turn it
  into a single mineral species. Evidence supports this bounded state with explicit
  limitations.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: data/records/bauxite.yaml
    sha256: b3c9fba4b8c46b4ac803dfa076887d49743b0e433804c54f3161788dcd887f7d
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/bauxite/2026-10-11T083001Z-codex-40769d.yaml
    sha256: 8f261841e88d192463aa5d847fb3b0a05352889a70ec7e6b02568846582f2f9d
    role: context
  - path: research/ingests/round12-aluminium-boron-20261011.json
    sha256: 3b71e99149dbc5b38a3b0b206e7a7709fcb08a3aad1db867f3be8903ded581a4
    role: context
  - path: research/ingests/round12-aluminium-boron-20261011.md
    sha256: f8190fbe7ec647b556a01df53ab2755237d79c3563e370036dbe55124f103fce
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:bauxite
  path: data/records/bauxite.yaml
  label: Bauxite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bauxite.yaml
    role: maintained_record
scope:
  description: Entire one-record scientific and provenance state.
  selection: Named independently assigned record, not a sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bauxite
checks:
- check_id: record
  name: Named strict record validation
  command: uv run --locked cmmmech validate data/records/bauxite.yaml
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bauxite
- check_id: check
  name: Completed batch check
  command: just check
  status: passed
  required: true
  summary: 307 tests passed, 3 skipped; 93 records and 108 histories valid.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bauxite
  scope_note: Root executed this gate and read its terminal log /private/tmp/cmm-round12-check.log;
    record hashes remained fixed throughout. Not a separate execution per review.
- check_id: require
  name: Nonempty corpus validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: 93 records checked; 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bauxite
  scope_note: Root executed this gate and read its terminal log /private/tmp/cmm-round12-require.log;
    record hashes remained fixed throughout. Not a separate execution per review.
- check_id: history
  name: Trusted-base append-only history validation
  command: uv run --locked cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4
  status: passed
  required: true
  summary: 108 history records checked; 0 errors.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:bauxite
  scope_note: Root executed this gate and read its terminal log /private/tmp/cmm-round12-history.log;
    record hashes remained fixed throughout. Not a separate execution per review.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/bauxite.yaml
  locator: Entire exact inspected record, attached CREATE history, schema and cohort
    dossier
  accessed_at: '2026-10-11T08:43:27Z'
  support: supports
  summary: New commodity identity has its own root and actual codex/GPT-6/codex history.
    Root reviewer did not author these scientific bytes or histories.
- evidence_id: authority
  kind: authority
  reference: https://www.usgs.gov/centers/national-minerals-information-center/bauxite-and-alumina-statistics-and-information;
    https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng
  locator: USGS Bauxite and Alumina Statistics and Information overview; EU2024 original
    recital8 and AnnexI1(a)/II1(c).
  accessed_at: '2026-10-11T08:43:27Z'
  support: supports
  summary: USGS live overview names gibbsite/boehmite/diaspore with impurities and
    applications. Both EU entries explicitly cover bauxite. No mechanism or extraction
    yield is asserted.
- evidence_id: search
  kind: search
  reference: Local bounded identity search and live authority checks
  locator: data/records research reviews history; issuing pages
  accessed_at: '2026-10-11T08:43:27Z'
  support: context_only
  summary: Search found current proposed roots and historical candidates, not grounds
    to equate commodities with element/mineral roots. Scientific absence beyond these
    boundaries is not asserted.
  search_scope: rg --no-ignore --hidden --follow for five exact roots and vol14-issue3-fulltext-7
    across data/records,research,reviews,history; ignored files included. Primary
    paper/source PDFs read separately, not assumed text-searchable.
assessments:
- assessment_id: identity
  area: identity
  topic: Material boundary and edition-specific designation
  outcome: supported
  summary: Heterogeneous aluminium ore commodity; its named minerals do not turn it
    into a single mineral species.
  target_ids:
  - cmmmech:bauxite
  evidence_ids:
  - record
  - authority
  dimensions:
  - name: criticality
    value: European Union / Regulation (EU) 2024/1252, Annex II, section 1 / Original
      act; OJ L 2024/1252, 3 May 2024 / critical; European Union / Regulation (EU)
      2024/1252, Annex I, section 1 / Original act; OJ L 2024/1252, 3 May 2024 / strategic
    definition: Exact adopted issuing assessment and edition, not timeless global
      status.
    evidence_ids:
    - authority
- assessment_id: provenance
  area: provenance
  topic: Actual curation and immutable working-state capture
  outcome: supported
  summary: CREATE sidecar target and actor agree with the new record; inline descriptive
    event is distinct. No prior committed history was modified.
  target_ids:
  - cmmmech:bauxite
  evidence_ids:
  - record
findings: []
actions: []
limitations:
- Review covers this exact commodity record only. Identity-only entries make no claim
  that microbial mechanisms do not exist.
- Raw artifacts acquired by curator were independently read; authority pages were
  also opened live. No independent laboratory replication or product-standard certification.
```
