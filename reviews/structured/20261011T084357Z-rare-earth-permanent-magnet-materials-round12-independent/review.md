# Independent round12 review of Rare-earth materials for permanent magnets, EU list scope

- Review: 20261011T084357Z-rare-earth-permanent-magnet-materials-round12-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:39:07Z
- Finished UTC: 2026-10-11T08:43:57Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

EU2024seven-member end-use grouping is explicit; no finished magnet, fixed alloy, universal purity or microbial grade-qualified product is asserted.

## Scope And Provenance

Entire named commodity-group record and evidence boundary.

Selection: All fields of one named record, not a corpus sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:rare-earth-permanent-magnet-materials | data/records/rare-earth-permanent-magnet-materials.yaml | maintained | Rare-earth materials for permanent magnets, EU list scope |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named strict record validation | passed | True | cmmmech:rare-earth-permanent-magnet-materials | Checked 1 record(s); 0 failed. |
| Completed batch check | passed | True | cmmmech:rare-earth-permanent-magnet-materials | 307 tests passed, 3 skipped; 93 records and 108 histories valid. |
| Nonempty corpus validation | passed | True | cmmmech:rare-earth-permanent-magnet-materials | 93 records checked; 0 failed. |
| Trusted-base append-only history validation | passed | True | cmmmech:rare-earth-permanent-magnet-materials | 108 history records checked; 0 errors. |

## Scientific And Domain Assessments

### Group boundary, overlap and dated designation

identity: supported. Targets: cmmmech:rare-earth-permanent-magnet-materials.

EU2024seven-member end-use grouping is explicit; no finished magnet, fixed alloy, universal purity or microbial grade-qualified product is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/rare-earth-permanent-magnet-materials.yaml; Entire exact record and attached actual curation histories | supports | Commodity family is explicitly distinguished from member elements, fixed mixtures and host minerals. Working-tree bytes captured before this assessment. |
| authority | https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list ; https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng ; https://rmis.jrc.ec.europa.eu/uploads/CRM_2020_Factsheets_critical_Final.pdf; Australia20Feb2024Table1footnotes16/17; originalEU2024AnnexI1(n),II1(q)/(r); EC2020factsheetp547 andPGMp399 | supports | Australian list explicitly enumerates sixPGM and sixteenREE includingPm/excludingSc. EC2020 economicREE split namesLREE5/HREE10 excludingSc/Pm. EU2024magnetentry explicitlynamesNdPrTbDyGdSmCe. EU2024PGM entry does not enumerate sixmembers; EC2020 assessment separates sixchemicalPGM from fiveassessed metals. |

## Limits And Additional Notes

- Root reviewer supplied early source-acquisition research before a separate agent authored the final YAML. Independence means distinct record curator and reviewer, not separate laboratory evidence or blind research.
- Issuing definitions are convention-dependent. Economic groups are commodity families, not homogeneous materials. No worldwide literature or list exhaustion claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T084357Z-rare-earth-permanent-magnet-materials-round12-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent round12 review of Rare-earth materials for permanent magnets, EU
  list scope
started_at: '2026-10-11T08:39:07Z'
finished_at: '2026-10-11T08:43:57Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate /root/cmm12_carbon_metals agent authored records/history;
    root captured exact record before judging and independently checked final claims.
    Root contributed earlier source discovery, disclosed as a limit.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: EU2024seven-member end-use grouping is explicit; no finished magnet, fixed
  alloy, universal purity or microbial grade-qualified product is asserted.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: data/records/rare-earth-permanent-magnet-materials.yaml
    sha256: 56c2b6ec0eff5dadad9a21d14a74c74c9f52ea370d74a62942fa1c87457126c6
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/rare-earth-permanent-magnet-materials/2026-10-11T083803Z-codex-053023.yaml
    sha256: a9010da821d60806021b84f204f53e0c6fe9939dbabe073c77301f7fb94561d1
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:rare-earth-permanent-magnet-materials
  path: data/records/rare-earth-permanent-magnet-materials.yaml
  label: Rare-earth materials for permanent magnets, EU list scope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-permanent-magnet-materials.yaml
    role: maintained_record
scope:
  description: Entire named commodity-group record and evidence boundary.
  selection: All fields of one named record, not a corpus sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:rare-earth-permanent-magnet-materials
checks:
- check_id: record
  name: Named strict record validation
  command: uv run --locked cmmmech validate data/records/rare-earth-permanent-magnet-materials.yaml
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rare-earth-permanent-magnet-materials
- check_id: check
  name: Completed batch check
  command: just check
  status: passed
  required: true
  summary: 307 tests passed, 3 skipped; 93 records and 108 histories valid.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rare-earth-permanent-magnet-materials
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
  - cmmmech:rare-earth-permanent-magnet-materials
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
  - cmmmech:rare-earth-permanent-magnet-materials
  scope_note: Root executed this gate and read its terminal log /private/tmp/cmm-round12-history.log;
    record hashes remained fixed throughout. Not a separate execution per review.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/rare-earth-permanent-magnet-materials.yaml
  locator: Entire exact record and attached actual curation histories
  accessed_at: '2026-10-11T08:43:57Z'
  support: supports
  summary: Commodity family is explicitly distinguished from member elements, fixed
    mixtures and host minerals. Working-tree bytes captured before this assessment.
- evidence_id: authority
  kind: authority
  reference: https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list
    ; https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng ; https://rmis.jrc.ec.europa.eu/uploads/CRM_2020_Factsheets_critical_Final.pdf
  locator: Australia20Feb2024Table1footnotes16/17; originalEU2024AnnexI1(n),II1(q)/(r);
    EC2020factsheetp547 andPGMp399
  accessed_at: '2026-10-11T08:43:57Z'
  support: supports
  summary: Australian list explicitly enumerates sixPGM and sixteenREE includingPm/excludingSc.
    EC2020 economicREE split namesLREE5/HREE10 excludingSc/Pm. EU2024magnetentry explicitlynamesNdPrTbDyGdSmCe.
    EU2024PGM entry does not enumerate sixmembers; EC2020 assessment separates sixchemicalPGM
    from fiveassessed metals.
assessments:
- assessment_id: identity
  area: identity
  topic: Group boundary, overlap and dated designation
  outcome: supported
  summary: EU2024seven-member end-use grouping is explicit; no finished magnet, fixed
    alloy, universal purity or microbial grade-qualified product is asserted.
  target_ids:
  - cmmmech:rare-earth-permanent-magnet-materials
  evidence_ids:
  - record
  - authority
  dimensions:
  - name: material_scope
    value: 'This end-use commodity family follows the seven-member entry in EU 2024
      Annex I: neodymium, praseodymium, terbium, dysprosium, gadolinium, samarium
      and cerium for permanent magnets. The qualification for permanent magnets is
      part of the identity and designation. This record does not identify a finished
      magnet, a single alloy composition, a numeric purity grade, or every use of
      those elements. It overlaps the broader rare-earth commodity family and both
      EU light and heavy rare-earth subgroups, while remaining distinct from each
      individual element and from magnet-bearing waste. No microbial recovery mechanism
      or performance for a magnet feedstock is inferred from an assay of synthetic
      dissolved rare-earth ions.'
    definition: Named convention and actual adopted group; overlap does not imply
      equivalent identities or collective microbial performance.
    evidence_ids:
    - record
    - authority
findings: []
actions: []
limitations:
- Root reviewer supplied early source-acquisition research before a separate agent
  authored the final YAML. Independence means distinct record curator and reviewer,
  not separate laboratory evidence or blind research.
- Issuing definitions are convention-dependent. Economic groups are commodity families,
  not homogeneous materials. No worldwide literature or list exhaustion claim.
```
