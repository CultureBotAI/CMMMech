# Independent evidence review of Ferroboron commodity

- Review: 20261011T093556Z-ferroboron-round14-independent
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
| cmmmech:ferroboron | data/records/ferroboron.yaml | maintained | Ferroboron commodity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named-file validation | passed | True | cmmmech:ferroboron | Reviewer executed session48219, terminal exit0: 6 records, 0 failed; log /private/tmp/cmm-round14-product-review/named-validation.log. |
| Initial completed batch check before unrelated FCC wording correction | passed | True | cmmmech:ferroboron | Root executed terminal0; reviewer read /private/tmp/cmm-round14-check.log and initial parent receipts: 307 passed, 3 skipped in 80.06s; 119 records, 134 histories. This gate preceded a pending unrelated FCC record wording correction; reviewed product hashes remain unchanged. Root will rerun affected final batch gates separately. |
| Nonempty corpus validation | passed | True | cmmmech:ferroboron | Root executed terminal0; reviewer read /private/tmp/cmm-round14-require.log and receipts: 119 records, 0 failed. |
| Append-only history validation at trusted base | passed | True | cmmmech:ferroboron | Root executed terminal0; reviewer read /private/tmp/cmm-round14-history.log and receipts: 134 history records, 0 errors. |

## Scientific And Domain Assessments

### Commodity, hydrate and end-use boundaries

identity: supported. Targets: cmmmech:ferroboron.

Grade-dependent iron-boron master-alloy commodity family. ISO catalogue supports steelmaking/foundry scope and Bomet supports multiple enterprise grades and other alloying applications. Formula FeB would incorrectly imply one stoichiometric compound; the record deliberately makes no such assignment.

### Primary specifications, versions and uncertainty

evidence: supported. Targets: cmmmech:ferroboron.

ISO catalogue supports steelmaking/foundry scope and Bomet supports multiple enterprise grades and other alloying applications. Formula FeB would incorrectly imply one stoichiometric compound; the record deliberately makes no such assignment. The ISO full standard was not acquired. Enterprise grades do not replace ISO requirements or exhaust an EU metallurgy-grade boron designation, and no criticality mapping is assigned.

### Actual CREATE history and exact reviewed working bytes

provenance: supported. Targets: cmmmech:ferroboron.

New inline CREATE event and matching canonical sidecar describe this session honestly with actual GPT-6/codex identity. Trusted main base and exact working hashes remain available and match batch-gated bytes. Record author and reviewer are distinct agents.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/ferroboron.yaml; Complete frozen YAML and exact linked CREATE sidecar | supports | Independent reviewer read record and sidecar after inspect capture. Actual GPT-6/codex attribution, separate inline and canonical timestamps, target and issue56 link match the present creation. Current SHA matches inspected and gated bytes. |
| iso-10386 | https://www.iso.org/standard/18450.html; Official catalogue abstract, edition1 September1994 and confirmation2022; web reader | supports | Fresh official web-reader page confirms ferroboron for steelmaking/foundry delivery and the named edition. Direct download403; full standard was not acquired. Catalogue evidence is not represented as inspection of full technical requirements. |
| bomet-2016 | https://www.ferroboron.net/product/feijingcailiao/gaojingchunpengtie.html; Product details and complete enterprise table BMTQB2016, BMT16-204 | supports | Fresh official manufacturer HTML inspected. Boron-iron master alloy has multiple grade-dependent compositions and steel/foundry, permanent-magnet and amorphous-material applications. No single FeB formula or boron cutoff is generalized. Ambiguous table heading SL is not interpreted or imported. |
| search | /private/tmp/cmm-round14-product-review/version-search.json; Eight exact manufacturer/standard search queries, first returned result windows; local dedup.txt and dedup-paths.txt | context_only | Ignored/hidden/followed searches cover records, research, reviews, history and named current raw source paths. Existing element, graphite and broad EU-grade records are not synonymized with these scoped products. Bounded version search found Coremax version6 alongside the cited version8; nickel-sulfate record pins version8 and does not claim all versions share impurity limits. No paper-based mechanism is claimed, so publication retraction screening is not a substitute for product-version checks. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Parent terminal receipts, check/require/history logs and gated-record-hashes.json | supports | Reviewer read all three actual batch logs and parent terminal receipts and compared this record hash to the gated manifest. Offline structure and provenance checks do not independently establish product identity or qualification. |

## Limits And Additional Notes

- The ISO full standard was not acquired. Enterprise grades do not replace ISO requirements or exhaust an EU metallurgy-grade boron designation, and no criticality mapping is assigned.
- Manufacturer examples and catalogue metadata establish product scope; they do not independently certify each supplied lot or a recovered product.
- No criticality or microbial mechanism claim is added. Omission does not assert that such evidence cannot exist.
- Searches and source-version checks are bounded; this is not exhaustive absence certification or a review of every possible supplier.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093556Z-ferroboron-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent evidence review of Ferroboron commodity
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
  - path: data/records/ferroboron.yaml
    sha256: 3b9d4fa94eee8f3f6b443e7d73af93d2dafaa58e7e2f1b58621c6afb1611df0d
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/ferroboron/2026-10-11T092628Z-codex-84f3de.yaml
    sha256: d03953b18bddfd9811d2c909b287c4486a380bf707d01a0bb0bbd0f9f0fbd956
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
  - cmmmech:ferroboron
  exclusions:
  - target: Uncurated mechanisms, other records and inaccessible full standards
    reason: No new mechanism or criticality is asserted. Related records inform boundary
      checks only; standards catalogues do not establish unseen numerical qualification
      tables.
targets:
- target_id: cmmmech:ferroboron
  path: data/records/ferroboron.yaml
  label: Ferroboron commodity
  kind: maintained
  record_class: commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferroboron.yaml
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
  - cmmmech:ferroboron
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
  - cmmmech:ferroboron
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
  - cmmmech:ferroboron
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
  - cmmmech:ferroboron
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/ferroboron.yaml
  locator: Complete frozen YAML and exact linked CREATE sidecar
  accessed_at: '2026-10-11T09:35:56Z'
  support: supports
  summary: Independent reviewer read record and sidecar after inspect capture. Actual
    GPT-6/codex attribution, separate inline and canonical timestamps, target and
    issue56 link match the present creation. Current SHA matches inspected and gated
    bytes.
  snapshot_sha256: 3b9d4fa94eee8f3f6b443e7d73af93d2dafaa58e7e2f1b58621c6afb1611df0d
- evidence_id: iso-10386
  kind: authority
  reference: https://www.iso.org/standard/18450.html
  locator: Official catalogue abstract, edition1 September1994 and confirmation2022;
    web reader
  accessed_at: '2026-10-11T09:35:56Z'
  support: supports
  summary: Fresh official web-reader page confirms ferroboron for steelmaking/foundry
    delivery and the named edition. Direct download403; full standard was not acquired.
    Catalogue evidence is not represented as inspection of full technical requirements.
- evidence_id: bomet-2016
  kind: primary_source
  reference: https://www.ferroboron.net/product/feijingcailiao/gaojingchunpengtie.html
  locator: Product details and complete enterprise table BMTQB2016, BMT16-204
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: Fresh official manufacturer HTML inspected. Boron-iron master alloy has
    multiple grade-dependent compositions and steel/foundry, permanent-magnet and
    amorphous-material applications. No single FeB formula or boron cutoff is generalized.
    Ambiguous table heading SL is not interpreted or imported.
  snapshot_sha256: 1d53ade0edfdb10d744a78cbbc6f574f5266a7a8bcfa7779538854ad36efc389
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
  summary: Grade-dependent iron-boron master-alloy commodity family. ISO catalogue
    supports steelmaking/foundry scope and Bomet supports multiple enterprise grades
    and other alloying applications. Formula FeB would incorrectly imply one stoichiometric
    compound; the record deliberately makes no such assignment.
  target_ids:
  - cmmmech:ferroboron
  evidence_ids:
  - record
  - search
  - iso-10386
  - bomet-2016
  dimensions:
  - name: material_form
    value: Grade-dependent iron-boron master-alloy commodity family
    definition: Maintained commodity scope, distinct from constituent element, ions,
      mineral specimen or source feed.
    evidence_ids:
    - record
    - iso-10386
    - bomet-2016
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
    - iso-10386
    - bomet-2016
- assessment_id: evidence
  area: evidence
  topic: Primary specifications, versions and uncertainty
  outcome: supported
  summary: ISO catalogue supports steelmaking/foundry scope and Bomet supports multiple
    enterprise grades and other alloying applications. Formula FeB would incorrectly
    imply one stoichiometric compound; the record deliberately makes no such assignment.
    The ISO full standard was not acquired. Enterprise grades do not replace ISO requirements
    or exhaust an EU metallurgy-grade boron designation, and no criticality mapping
    is assigned.
  target_ids:
  - cmmmech:ferroboron
  evidence_ids:
  - iso-10386
  - bomet-2016
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
  - cmmmech:ferroboron
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- The ISO full standard was not acquired. Enterprise grades do not replace ISO requirements
  or exhaust an EU metallurgy-grade boron designation, and no criticality mapping
  is assigned.
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
