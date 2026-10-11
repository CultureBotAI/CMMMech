# Independent evidence review of Lithium hydroxide monohydrate commodity

- Review: 20261011T093556Z-lithium-hydroxide-monohydrate-round14-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:30:12Z
- Finished UTC: 2026-10-11T09:35:56Z
- Reviewer: Codex /root/round14_minerals (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supported commodity identity and carefully bounded source claims; no actionable findings. Product-specific specifications remain distinct from universal grade rules, criticality and microbial recovery evidence.

## Scope And Provenance

All fields, cited source claims and linked history of one exact new working-tree record.

Selection: One assigned member of six product-boundary records; full per-record assessment, not a corpus-wide scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lithium-hydroxide-monohydrate | data/records/lithium-hydroxide-monohydrate.yaml | maintained | Lithium hydroxide monohydrate commodity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named-file validation | passed | True | cmmmech:lithium-hydroxide-monohydrate | Reviewer executed session48219, terminal exit0: 6 records, 0 failed; log /private/tmp/cmm-round14-product-review/named-validation.log. |
| Initial completed batch check before unrelated FCC wording correction | passed | True | cmmmech:lithium-hydroxide-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-check.log and initial parent receipts: 307 passed, 3 skipped in 80.06s; 119 records, 134 histories. This gate preceded a pending unrelated FCC record wording correction; reviewed product hashes remain unchanged. Root will rerun affected final batch gates separately. |
| Nonempty corpus validation | passed | True | cmmmech:lithium-hydroxide-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-require.log and receipts: 119 records, 0 failed. |
| Append-only history validation at trusted base | passed | True | cmmmech:lithium-hydroxide-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-history.log and receipts: 134 history records, 0 errors. |

## Scientific And Domain Assessments

### Commodity, hydrate and end-use boundaries

identity: supported. Targets: cmmmech:lithium-hydroxide-monohydrate.

Manufactured LiOH.H2O commodity, with hydration state preserved. The at-least-55% assay measures LiOH, not purity of the hydrate. The source table, formulation and applications support the text, while the separate narrower standard is metadata-only.

### Primary specifications, versions and uncertainty

evidence: supported. Targets: cmmmech:lithium-hydroxide-monohydrate.

The at-least-55% assay measures LiOH, not purity of the hydrate. The source table, formulation and applications support the text, while the separate narrower standard is metadata-only. No anhydrous/hydrated equivalence or automatic lithium-ion cathode qualification is inferred; complete GB/T 26008-2020 tables remain unread.

### Actual CREATE history and exact reviewed working bytes

provenance: supported. Targets: cmmmech:lithium-hydroxide-monohydrate.

New inline CREATE event and matching canonical sidecar describe this session honestly with actual GPT-6/codex identity. Trusted main base and exact working hashes remain available and match batch-gated bytes. Record author and reviewer are distinct agents.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lithium-hydroxide-monohydrate.yaml; Complete frozen YAML and exact linked CREATE sidecar | supports | Independent reviewer read record and sidecar after inspect capture. Actual GPT-6/codex attribution, separate inline and canonical timestamps, target and issue56 link match the present creation. Current SHA matches inspected and gated bytes. |
| albemarle-401106 | https://www.albemarle.com/sites/default/files/documents/t401106_tds_002.pdf; Three-page data sheet; p1 formula, application and specification table, issue 2018/07/06 | supports | Fresh complete PDF read and p1 visually checked. Product 401106 is LiOH.H2O, with at least 55.0% LiOH by acidimetric titration. The record correctly distinguishes this assay basis from monohydrate purity and preserves grease/alkaline-battery applications without declaring universal lithium-ion qualification. |
| samr-26008 | https://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FE9172E3E05397BE0A0A6CEB; GB/T 26008-2020 official registry entry | supports | Fresh official registry names battery-grade lithium hydroxide monohydrate. Only identity and edition are used; no implementation date or unseen qualification table is imported. |
| search | /private/tmp/cmm-round14-product-review/version-search.json; Eight exact manufacturer/standard search queries, first returned result windows; local dedup.txt and dedup-paths.txt | context_only | Ignored/hidden/followed searches cover records, research, reviews, history and named current raw source paths. Existing element, graphite and broad EU-grade records are not synonymized with these scoped products. Bounded version search found Coremax version6 alongside the cited version8; nickel-sulfate record pins version8 and does not claim all versions share impurity limits. No paper-based mechanism is claimed, so publication retraction screening is not a substitute for product-version checks. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Parent terminal receipts, check/require/history logs and gated-record-hashes.json | supports | Reviewer read all three actual batch logs and parent terminal receipts and compared this record hash to the gated manifest. Offline structure and provenance checks do not independently establish product identity or qualification. |

## Limits And Additional Notes

- No anhydrous/hydrated equivalence or automatic lithium-ion cathode qualification is inferred; complete GB/T 26008-2020 tables remain unread.
- Manufacturer examples and catalogue metadata establish product scope; they do not independently certify each supplied lot or a recovered product.
- No criticality or microbial mechanism claim is added. Omission does not assert that such evidence cannot exist.
- Searches and source-version checks are bounded; this is not exhaustive absence certification or a review of every possible supplier.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093556Z-lithium-hydroxide-monohydrate-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent evidence review of Lithium hydroxide monohydrate commodity
started_at: '2026-10-11T09:30:12Z'
finished_at: '2026-10-11T09:35:56Z'
reviewer:
  identity: Codex /root/round14_minerals
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate /root/round14_products agent authored this record and
    history. Reviewer acquired and read primary sources independently and made no
    product-record edits. Both agents share the task and worktree; this is record-author
    separation, not organizational independence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supported commodity identity and carefully bounded source claims; no actionable
  findings. Product-specific specifications remain distinct from universal grade rules,
  criticality and microbial recovery evidence.
source:
  git_revision: 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  state: working_tree
  inputs:
  - path: data/records/lithium-hydroxide-monohydrate.yaml
    sha256: 682207c7f5d201d066b3a79c7d64c49360f867500c9ce4ca162f1a236acd1c49
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/lithium-hydroxide-monohydrate/2026-10-11T092622Z-codex-1dc891.yaml
    sha256: 61d18189529246ab42ca0414fa89aff23db6e99e9dbdf365e306dc6db89825b5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, cited source claims and linked history of one exact new
    working-tree record.
  selection: One assigned member of six product-boundary records; full per-record
    assessment, not a corpus-wide scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  exclusions:
  - target: Uncurated mechanisms, other records and inaccessible full standards
    reason: No new mechanism or criticality is asserted. Related records inform boundary
      checks only; standards catalogues do not establish unseen numerical qualification
      tables.
targets:
- target_id: cmmmech:lithium-hydroxide-monohydrate
  path: data/records/lithium-hydroxide-monohydrate.yaml
  label: Lithium hydroxide monohydrate commodity
  kind: maintained
  record_class: commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lithium-hydroxide-monohydrate.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent reviewer named-file validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/lithium-carbonate.yaml data/records/lithium-hydroxide-monohydrate.yaml
    data/records/nickel-sulfate-hexahydrate.yaml data/records/manganese-sulfate-monohydrate.yaml
    data/records/ferroboron.yaml data/records/graphite-anode-material.yaml
  status: passed
  required: true
  summary: 'Reviewer executed session48219, terminal exit0: 6 records, 0 failed; log
    /private/tmp/cmm-round14-product-review/named-validation.log.'
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Initial completed batch check before unrelated FCC wording correction
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root executed terminal0; reviewer read /private/tmp/cmm-round14-check.log
    and initial parent receipts: 307 passed, 3 skipped in 80.06s; 119 records, 134
    histories. This gate preceded a pending unrelated FCC record wording correction;
    reviewed product hashes remain unchanged. Root will rerun affected final batch
    gates separately.'
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  exit_code: 0
  expected_exit_code: 0
- check_id: require
  name: Nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Root executed terminal0; reviewer read /private/tmp/cmm-round14-require.log
    and receipts: 119 records, 0 failed.'
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history validation at trusted base
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  summary: 'Root executed terminal0; reviewer read /private/tmp/cmm-round14-history.log
    and receipts: 134 history records, 0 errors.'
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lithium-hydroxide-monohydrate.yaml
  locator: Complete frozen YAML and exact linked CREATE sidecar
  accessed_at: '2026-10-11T09:35:56Z'
  support: supports
  summary: Independent reviewer read record and sidecar after inspect capture. Actual
    GPT-6/codex attribution, separate inline and canonical timestamps, target and
    issue56 link match the present creation. Current SHA matches inspected and gated
    bytes.
  snapshot_sha256: 682207c7f5d201d066b3a79c7d64c49360f867500c9ce4ca162f1a236acd1c49
- evidence_id: albemarle-401106
  kind: primary_source
  reference: https://www.albemarle.com/sites/default/files/documents/t401106_tds_002.pdf
  locator: Three-page data sheet; p1 formula, application and specification table,
    issue 2018/07/06
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: Fresh complete PDF read and p1 visually checked. Product 401106 is LiOH.H2O,
    with at least 55.0% LiOH by acidimetric titration. The record correctly distinguishes
    this assay basis from monohydrate purity and preserves grease/alkaline-battery
    applications without declaring universal lithium-ion qualification.
  snapshot_sha256: f930458a946ef22ec7904b0fcf605c62c671051dc5f399587be386d7319cf3e0
- evidence_id: samr-26008
  kind: authority
  reference: https://std.samr.gov.cn/gb/search/gbDetailed?id=A73D6262FE9172E3E05397BE0A0A6CEB
  locator: GB/T 26008-2020 official registry entry
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: Fresh official registry names battery-grade lithium hydroxide monohydrate.
    Only identity and edition are used; no implementation date or unseen qualification
    table is imported.
  snapshot_sha256: 32243b3e2d56df4ccc594fe494a27593ea64f035592a09a0eab6703a38387ec9
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round14-product-review/version-search.json
  locator: Eight exact manufacturer/standard search queries, first returned result
    windows; local dedup.txt and dedup-paths.txt
  accessed_at: '2026-10-11T09:35:56Z'
  support: context_only
  summary: Ignored/hidden/followed searches cover records, research, reviews, history
    and named current raw source paths. Existing element, graphite and broad EU-grade
    records are not synonymized with these scoped products. Bounded version search
    found Coremax version6 alongside the cited version8; nickel-sulfate record pins
    version8 and does not claim all versions share impurity limits. No paper-based
    mechanism is claimed, so publication retraction screening is not a substitute
    for product-version checks.
  search_scope: rg --no-ignore --hidden --follow across data/records, research, reviews,
    history, /private/tmp/cmm-round14-product-raw and /private/tmp/cmm-round14-product-review;
    eight queries retained in version-search.json. First web result windows only,
    no global product-version or absence claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round14-gate-receipts-initial.json
  locator: Parent terminal receipts, check/require/history logs and gated-record-hashes.json
  accessed_at: '2026-10-11T09:35:56Z'
  support: supports
  summary: Reviewer read all three actual batch logs and parent terminal receipts
    and compared this record hash to the gated manifest. Offline structure and provenance
    checks do not independently establish product identity or qualification.
  snapshot_sha256: cd1d462bdeea6cc6174ffa7ccff29bf6f49a9037541c6b3327fb923fc64106bb
assessments:
- assessment_id: identity
  area: identity
  topic: Commodity, hydrate and end-use boundaries
  outcome: supported
  summary: Manufactured LiOH.H2O commodity, with hydration state preserved. The at-least-55%
    assay measures LiOH, not purity of the hydrate. The source table, formulation
    and applications support the text, while the separate narrower standard is metadata-only.
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  evidence_ids:
  - record
  - search
  - albemarle-401106
  - samr-26008
  dimensions:
  - name: material_form
    value: Manufactured LiOH.H2O commodity, with hydration state preserved
    definition: Maintained commodity scope, distinct from constituent element, ions,
      mineral specimen or source feed.
    evidence_ids:
    - record
    - albemarle-401106
    - samr-26008
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition or elemental criticality is inherited
      into this product.
    evidence_ids:
    - record
  - name: mechanism_deployment
    value: Not asserted
    definition: No organism, biomass, substrate, assay controls, microbial yield or
      laboratory/industrial mechanism is represented by these manufacturer descriptions.
    evidence_ids:
    - record
    - albemarle-401106
    - samr-26008
- assessment_id: evidence
  area: evidence
  topic: Primary specifications, versions and uncertainty
  outcome: supported
  summary: The at-least-55% assay measures LiOH, not purity of the hydrate. The source
    table, formulation and applications support the text, while the separate narrower
    standard is metadata-only. No anhydrous/hydrated equivalence or automatic lithium-ion
    cathode qualification is inferred; complete GB/T 26008-2020 tables remain unread.
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  evidence_ids:
  - albemarle-401106
  - samr-26008
  - record
  - search
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE history and exact reviewed working bytes
  outcome: supported
  summary: New inline CREATE event and matching canonical sidecar describe this session
    honestly with actual GPT-6/codex identity. Trusted main base and exact working
    hashes remain available and match batch-gated bytes. Record author and reviewer
    are distinct agents.
  target_ids:
  - cmmmech:lithium-hydroxide-monohydrate
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- No anhydrous/hydrated equivalence or automatic lithium-ion cathode qualification
  is inferred; complete GB/T 26008-2020 tables remain unread.
- Manufacturer examples and catalogue metadata establish product scope; they do not
  independently certify each supplied lot or a recovered product.
- No criticality or microbial mechanism claim is added. Omission does not assert that
  such evidence cannot exist.
- Searches and source-version checks are bounded; this is not exhaustive absence certification
  or a review of every possible supplier.
tags:
- round14
- independent
- scientific-review
- commodity
```
