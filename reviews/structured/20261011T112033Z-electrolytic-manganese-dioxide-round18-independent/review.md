# Independent scientific review of Electrolytic manganese dioxide commodity

- Review: 20261011T112033Z-electrolytic-manganese-dioxide-round18-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:17:49.121121Z
- Finished UTC: 2026-10-11T11:20:33.499594Z
- Reviewer: Codex /root/round18_dunite (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The manufactured product identity and explicit limits are evidence-backed. No actionable blocker, major, minor or informational finding was identified in this scoped review; unresolved grade/source limits are already represented.

## Scope And Provenance

Every scientific, identity, source and history field of one new commodity-only maintained record.

Selection: Assigned final frozen product record within round18; direct evidence review, not a sample of all manganese materials.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26cb0688effb2f71e4a570c416f6f43ff858c5ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:electrolytic-manganese-dioxide | data/records/electrolytic-manganese-dioxide.yaml | maintained | electrolytic-manganese-dioxide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:electrolytic-manganese-dioxide | Reviewer execution completed with Checked 2 records; 0 failed. Actual terminal result and named-validation.log inspected. |
| Native full checks | passed | True | cmmmech:electrolytic-manganese-dioxide | Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round 18-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 86.49s (0:01:26)<br>Checked 138 record(s); 0 failed.<br>Checked 154 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:electrolytic-manganese-dioxide | Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round 18-final-require.log: Checked 138 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:electrolytic-manganese-dioxide | Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round 18-final-history.log: Checked 154 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Manufactured commodity and material-form distinction

identity: supported. Targets: cmmmech:electrolytic-manganese-dioxide.

Electrolytically manufactured MnO2 commodity family; distinct from chemical-route MnO2, natural ore/mineral pyrolusite, elemental Mn, manganese metal, spent batteries and finished electrodes.

### Grade, criticality, microbial and deployment boundaries

scope: supported. Targets: cmmmech:electrolytic-manganese-dioxide.

The record supports identity and stated uses without inheriting elemental criticality, microbial production, universal grade limits or deployment claims. Producer-specific specifications remain contextual.

### Source assays, versions and numerical qualification

quantity: supported. Targets: cmmmech:electrolytic-manganese-dioxide.

Producer properties are representative and the page is undated. Identity does not specify a unique MnO2 crystal phase, certify every member for battery use, or settle the broad battery-grade manganese boundary.

### Exact reviewed revision, working state and canonical CREATE

provenance: supported. Targets: cmmmech:electrolytic-manganese-dioxide.

Native inline CREATE event and linked genuine GPT-6/codex sidecar identify the maintained record. Review source is the trusted main base with exact working-tree hashes; structural, corpus and append-only history checks passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/electrolytic-manganese-dioxide.yaml; Complete record and linked CREATE sidecar | supports | All fields and actor/timestamp/target linkage read independently; canonical inspection precedes judgment, and current record/schema/history bytes match captured hashes. Maintained product scope has no asserted external material/taxon CURIE, criticality designation, or microbial mechanism. |
| tosoh | https://www.tosoh.co.jp/product/functionality/electrolytic_manganese_dioxide.html; Japanese Features, Applications and representative alkaline/lithium-battery property tables | supports | Independently read complete retained HTML and live primary page. Electrolysis-derived MnO2 and alkaline primary battery/ lithium-manganate precursor applications are explicit. The available/active oxygen assay is expressed as MnO2; representative assay and size/impurity data do not establish universal crystal-phase purity or certification. |
| usgs | https://pubs.usgs.gov/myb/vol1/2020/myb1-2020-manga.pdf; Cover; printed 47.1 and 47.6 Table 3, corresponding PDF 2/PDF 7 | supports | Cover dates the 2020 Minerals Yearbook advance release to September 2024. Visually inspected printed 47.1 historical electrolytic-metal context and Table 3 distinction between chemically and electrolytically manufactured synthetic MnO2. Historical statistics are not presented as current market totals. |
| search | /private/tmp/cmm-round18-products-review/search.json; Independent exact queries, live page outcomes, dedup.log and nearby Mn/pyrolusite/sulfate reads | context_only | Bounded searches and direct producer-document comparison support identity distinctions and expose the already-retained LO oxygen difference. No affecting identity correction surfaced in these checks; no exhaustive source-change or literature claim is made. |
| gates | /private/tmp/cmm-round18-gate-receipts.json; Terminal finished_at receipt and final-batch/final-require/final-history logs; independent named-validation.log | supports | Reviewer ran named validation to terminal exit 0 for both products. Parent ran final native suite, nonempty corpus and trusted-base history to terminal exit 0; reviewer independently inspected completed receipt/logs.308 passed, 3 skipped; 138 records and 154 histories. Current targets still match canonical inspected hashes. |

## Limits And Additional Notes

- Producer properties are representative and the page is undated. Identity does not specify a unique MnO2 crystal phase, certify every member for battery use, or settle the broad battery-grade manganese boundary.
- Manufacturer statements and historical USGS context establish identity/use scope, not independent product-batch certification or exhaustive market coverage.
- Offline validators establish structural integrity rather than scientific truth; no newly discovered mechanism was curated in this review.
- No record edits or curation-history sessions were created by the reviewer. No earlier saved finding was silently retired.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112033Z-electrolytic-manganese-dioxide-round18-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Electrolytic manganese dioxide commodity
started_at: '2026-10-11T11:17:49.121121Z'
finished_at: '2026-10-11T11:20:33.499594Z'
reviewer:
  identity: Codex /root/round18_dunite
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root agent authored the product record and history. This separate
    reviewer captured canonical targets before judgment, independently read primary
    manufacturer documents and USGS pages, checked image/table evidence and exact
    hashes, and made no target edits. Shared worktree and curator acquisition reuse
    are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The manufactured product identity and explicit limits are evidence-backed.
  No actionable blocker, major, minor or informational finding was identified in this
  scoped review; unresolved grade/source limits are already represented.
source:
  git_revision: 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  state: working_tree
  inputs:
  - path: data/records/electrolytic-manganese-dioxide.yaml
    sha256: 83512a974c0dba9ec59a2cb7f26503bfe509c6816b8cc0f37ab1fa24b8700ccd
    role: target
  - path: history/records/electrolytic-manganese-dioxide/2026-10-11T111719Z-codex-53adc8.yaml
    sha256: 6208b0be321f130f97d5a612a2a5ce8cba3e64a49107c7a066df9ff968f308be
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every scientific, identity, source and history field of one new commodity-only
    maintained record.
  selection: Assigned final frozen product record within round18; direct evidence
    review, not a sample of all manganese materials.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  exclusions:
  - target: Other manganese records, production audits and microbial mechanism discovery
    reason: Nearby materials contextualize identity only. No new microbial mechanism,
      current producer certification or universal grade acceptance is assessed.
targets:
- target_id: cmmmech:electrolytic-manganese-dioxide
  path: data/records/electrolytic-manganese-dioxide.yaml
  label: electrolytic-manganese-dioxide
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electrolytic-manganese-dioxide.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/electrolytic-manganese-metal.yaml data/records/electrolytic-manganese-dioxide.yaml
  status: passed
  required: true
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer execution completed with Checked 2 records; 0 failed. Actual terminal
    result and named-validation.log inspected.
  evidence_ids:
  - gates
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round
    18-final-batch.log: uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 86.49s (0:01:26)

    Checked 138 record(s); 0 failed.

    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - gates
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round
    18-final-require.log: Checked 138 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - gates
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer read completed receipt and actual log. /private/tmp/cmm-round
    18-final-history.log: Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - gates
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/electrolytic-manganese-dioxide.yaml
  locator: Complete record and linked CREATE sidecar
  accessed_at: '2026-10-11T11:20:33.499594Z'
  support: supports
  summary: All fields and actor/timestamp/target linkage read independently; canonical
    inspection precedes judgment, and current record/schema/history bytes match captured
    hashes. Maintained product scope has no asserted external material/taxon CURIE,
    criticality designation, or microbial mechanism.
  snapshot_sha256: 83512a974c0dba9ec59a2cb7f26503bfe509c6816b8cc0f37ab1fa24b8700ccd
- evidence_id: tosoh
  kind: primary_source
  reference: https://www.tosoh.co.jp/product/functionality/electrolytic_manganese_dioxide.html
  locator: Japanese Features, Applications and representative alkaline/lithium-battery
    property tables
  accessed_at: '2026-10-11T11:20:33.499594Z'
  support: supports
  summary: Independently read complete retained HTML and live primary page. Electrolysis-derived
    MnO2 and alkaline primary battery/ lithium-manganate precursor applications are
    explicit. The available/active oxygen assay is expressed as MnO2; representative
    assay and size/impurity data do not establish universal crystal-phase purity or
    certification.
  snapshot_sha256: 26004acd2fae4d3228450721eea6acf1e3bacfce467ac14b5421c103f2bb803c
- evidence_id: usgs
  kind: authority
  reference: https://pubs.usgs.gov/myb/vol1/2020/myb1-2020-manga.pdf
  locator: Cover; printed 47.1 and 47.6 Table 3, corresponding PDF 2/PDF 7
  accessed_at: '2026-10-11T11:20:33.499594Z'
  support: supports
  summary: Cover dates the 2020 Minerals Yearbook advance release to September 2024.
    Visually inspected printed 47.1 historical electrolytic-metal context and Table
    3 distinction between chemically and electrolytically manufactured synthetic MnO2.
    Historical statistics are not presented as current market totals.
  snapshot_sha256: aea1a9012b644f05c73ada993032ffb8f576e8b007a885d799492bbe22cae438
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round18-products-review/search.json
  locator: Independent exact queries, live page outcomes, dedup.log and nearby Mn/pyrolusite/sulfate
    reads
  accessed_at: '2026-10-11T11:20:33.499594Z'
  support: context_only
  summary: Bounded searches and direct producer-document comparison support identity
    distinctions and expose the already-retained LO oxygen difference. No affecting
    identity correction surfaced in these checks; no exhaustive source-change or literature
    claim is made.
  snapshot_sha256: 58d4adc9bbc79d696346ab169495001d134f541ab4ab9289ece982166e48af13
  search_scope: Hidden and ignored files included with followed links across data/research/reviews/history/.claude
    and named products raw directory. First web result sets only. Nearby records and
    prior product proposals checked; no machine-wide or global exhaustion claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round18-gate-receipts.json
  locator: Terminal finished_at receipt and final-batch/final-require/final-history
    logs; independent named-validation.log
  accessed_at: '2026-10-11T11:20:33.499594Z'
  support: supports
  summary: Reviewer ran named validation to terminal exit 0 for both products. Parent
    ran final native suite, nonempty corpus and trusted-base history to terminal exit
    0; reviewer independently inspected completed receipt/logs.308 passed, 3 skipped;
    138 records and 154 histories. Current targets still match canonical inspected
    hashes.
  snapshot_sha256: f77f5decb184fd5e6544b9d89c9699a95621e2a83749524526f6283fb5be2f66
assessments:
- assessment_id: identity
  area: identity
  topic: Manufactured commodity and material-form distinction
  outcome: supported
  summary: Electrolytically manufactured MnO2 commodity family; distinct from chemical-route
    MnO2, natural ore/mineral pyrolusite, elemental Mn, manganese metal, spent batteries
    and finished electrodes.
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - record
  - tosoh
  - usgs
  dimensions:
  - name: material_kind
    value: commodity
    definition: A manufactured product family defined by electrolysis and material
      form, not the element or a natural mineral species.
    evidence_ids:
    - record
    - tosoh
    - usgs
- assessment_id: evidence_scope
  area: scope
  topic: Grade, criticality, microbial and deployment boundaries
  outcome: supported
  summary: The record supports identity and stated uses without inheriting elemental
    criticality, microbial production, universal grade limits or deployment claims.
    Producer-specific specifications remain contextual.
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - record
  - tosoh
  - usgs
  dimensions:
  - name: criticality_scope
    value: No designation asserted
    definition: Jurisdiction/list/edition fields are omitted rather than inferred
      from manganese element or battery use.
    evidence_ids:
    - record
  - name: mechanism_scope
    value: No microbial mechanism asserted
    definition: Organism, biomass, assay and recovery fields are intentionally absent
      because these sources establish product identity and ordinary manufacturing
      context.
    evidence_ids:
    - record
- assessment_id: uncertainty
  area: quantity
  topic: Source assays, versions and numerical qualification
  outcome: supported
  summary: Producer properties are representative and the page is undated. Identity
    does not specify a unique MnO2 crystal phase, certify every member for battery
    use, or settle the broad battery-grade manganese boundary.
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - tosoh
  - usgs
- assessment_id: history
  area: provenance
  topic: Exact reviewed revision, working state and canonical CREATE
  outcome: supported
  summary: Native inline CREATE event and linked genuine GPT-6/codex sidecar identify
    the maintained record. Review source is the trusted main base with exact working-tree
    hashes; structural, corpus and append-only history checks passed.
  target_ids:
  - cmmmech:electrolytic-manganese-dioxide
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Producer properties are representative and the page is undated. Identity does not
  specify a unique MnO2 crystal phase, certify every member for battery use, or settle
  the broad battery-grade manganese boundary.
- Manufacturer statements and historical USGS context establish identity/use scope,
  not independent product-batch certification or exhaustive market coverage.
- Offline validators establish structural integrity rather than scientific truth;
  no newly discovered mechanism was curated in this review.
notes:
- No record edits or curation-history sessions were created by the reviewer. No earlier
  saved finding was silently retired.
tags:
- round18
- independent
- commodity
- identity-only
```
