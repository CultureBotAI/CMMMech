# Independent evidence review of Manganese sulfate monohydrate commodity

- Review: 20261011T093556Z-manganese-sulfate-monohydrate-round14-independent
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
| cmmmech:manganese-sulfate-monohydrate | data/records/manganese-sulfate-monohydrate.yaml | maintained | Manganese sulfate monohydrate commodity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named-file validation | passed | True | cmmmech:manganese-sulfate-monohydrate | Reviewer executed session48219, terminal exit0: 6 records, 0 failed; log /private/tmp/cmm-round14-product-review/named-validation.log. |
| Initial completed batch check before unrelated FCC wording correction | passed | True | cmmmech:manganese-sulfate-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-check.log and initial parent receipts: 307 passed, 3 skipped in 80.06s; 119 records, 134 histories. This gate preceded a pending unrelated FCC record wording correction; reviewed product hashes remain unchanged. Root will rerun affected final batch gates separately. |
| Nonempty corpus validation | passed | True | cmmmech:manganese-sulfate-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-require.log and receipts: 119 records, 0 failed. |
| Append-only history validation at trusted base | passed | True | cmmmech:manganese-sulfate-monohydrate | Root executed terminal0; reviewer read /private/tmp/cmm-round14-history.log and receipts: 134 history records, 0 errors. |

## Scientific And Domain Assessments

### Commodity, hydrate and end-use boundaries

identity: supported. Targets: cmmmech:manganese-sulfate-monohydrate.

Manufactured MnSO4.H2O commodity, including agricultural products. Two complete primary product sources establish the hydrated salt and agricultural trade. Walsun is used only for high-purity manganese-sulfate battery context; neither homepage nor standards title is misused to assert universal monohydrate qualification.

### Primary specifications, versions and uncertainty

evidence: supported. Targets: cmmmech:manganese-sulfate-monohydrate.

Two complete primary product sources establish the hydrated salt and agricultural trade. Walsun is used only for high-purity manganese-sulfate battery context; neither homepage nor standards title is misused to assert universal monohydrate qualification. HG/T 4823-2023 full tables were not acquired. Walsun provides homepage context, not a verified product qualification table; no universal purity threshold is asserted.

### Actual CREATE history and exact reviewed working bytes

provenance: supported. Targets: cmmmech:manganese-sulfate-monohydrate.

New inline CREATE event and matching canonical sidecar describe this session honestly with actual GPT-6/codex identity. Trusted main base and exact working hashes remain available and match batch-gated bytes. Record author and reviewer are distinct agents.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/manganese-sulfate-monohydrate.yaml; Complete frozen YAML and exact linked CREATE sidecar | supports | Independent reviewer read record and sidecar after inspect capture. Actual GPT-6/codex attribution, separate inline and canonical timestamps, target and issue56 link match the present creation. Current SHA matches inspected and gated bytes. |
| panchem-monohydrate | https://www.panchemcorp.com/pdf/product/Manganese-Sulfate-Monohydrate-Spec-Sheet.pdf; Complete one-page product sheet, title, table and Application | supports | Fresh PDF read and visually checked: manufactured monohydrate powder is marketed for feed and fertilizer. Numerical grade entries are not imported as universal limits, and the sheet does not qualify a battery product. |
| ihumate-monohydrate | https://www.ihumate.com/manganese-sulfate-monohydrate; Product introduction, formula, specifications and agricultural-use sections | supports | Fresh complete manufacturer HTML inspected. MnSO4.H2O identity and agricultural commodity use corroborate Pan Chem. Product-specific purity and Mn assays are not generalized, and published specifications are not recovered-product measurements. |
| walsun-battery-context | https://www.walsun-nm.com/EN/Home; Homepage Battery Industry section | context_only | Fresh complete homepage independently read. It states high-purity manganese-sulfate cathode-precursor use, supporting context only. No precise composition or monohydrate identity is inferred from the homepage; previous product-route redirect is documented by the curator. |
| samr-4823 | https://std.samr.gov.cn/hb/search/stdHBDetailedCNF?id=037FCC3702C04EF6E06397BE0A0A09CA; HG/T 4823-2023 official registry entry | supports | Fresh registry names manganese sulfate for batteries, a scope not restricted to the monohydrate by its title. Record treats it as metadata and does not invent table limits or collapse every battery manganese product to this salt. |
| search | /private/tmp/cmm-round14-product-review/version-search.json; Eight exact manufacturer/standard search queries, first returned result windows; local dedup.txt and dedup-paths.txt | context_only | Ignored/hidden/followed searches cover records, research, reviews, history and named current raw source paths. Existing element, graphite and broad EU-grade records are not synonymized with these scoped products. Bounded version search found Coremax version6 alongside the cited version8; nickel-sulfate record pins version8 and does not claim all versions share impurity limits. No paper-based mechanism is claimed, so publication retraction screening is not a substitute for product-version checks. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Parent terminal receipts, check/require/history logs and gated-record-hashes.json | supports | Reviewer read all three actual batch logs and parent terminal receipts and compared this record hash to the gated manifest. Offline structure and provenance checks do not independently establish product identity or qualification. |

## Limits And Additional Notes

- HG/T 4823-2023 full tables were not acquired. Walsun provides homepage context, not a verified product qualification table; no universal purity threshold is asserted.
- Manufacturer examples and catalogue metadata establish product scope; they do not independently certify each supplied lot or a recovered product.
- No criticality or microbial mechanism claim is added. Omission does not assert that such evidence cannot exist.
- Searches and source-version checks are bounded; this is not exhaustive absence certification or a review of every possible supplier.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093556Z-manganese-sulfate-monohydrate-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent evidence review of Manganese sulfate monohydrate commodity
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
  - path: data/records/manganese-sulfate-monohydrate.yaml
    sha256: 22a095812cd5f0add14f5c2007f47defd68ea263334690ecc946784da3e9f2dc
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/manganese-sulfate-monohydrate/2026-10-11T092626Z-codex-71843a.yaml
    sha256: 7efdb335aaa148a0a3f0c5098c5bddd5ff78621dee38e205b5d14ac02729c9f8
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
  - cmmmech:manganese-sulfate-monohydrate
  exclusions:
  - target: Uncurated mechanisms, other records and inaccessible full standards
    reason: No new mechanism or criticality is asserted. Related records inform boundary
      checks only; standards catalogues do not establish unseen numerical qualification
      tables.
targets:
- target_id: cmmmech:manganese-sulfate-monohydrate
  path: data/records/manganese-sulfate-monohydrate.yaml
  label: Manganese sulfate monohydrate commodity
  kind: maintained
  record_class: commodity
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese-sulfate-monohydrate.yaml
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
  - cmmmech:manganese-sulfate-monohydrate
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
  - cmmmech:manganese-sulfate-monohydrate
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
  - cmmmech:manganese-sulfate-monohydrate
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
  - cmmmech:manganese-sulfate-monohydrate
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/manganese-sulfate-monohydrate.yaml
  locator: Complete frozen YAML and exact linked CREATE sidecar
  accessed_at: '2026-10-11T09:35:56Z'
  support: supports
  summary: Independent reviewer read record and sidecar after inspect capture. Actual
    GPT-6/codex attribution, separate inline and canonical timestamps, target and
    issue56 link match the present creation. Current SHA matches inspected and gated
    bytes.
  snapshot_sha256: 22a095812cd5f0add14f5c2007f47defd68ea263334690ecc946784da3e9f2dc
- evidence_id: panchem-monohydrate
  kind: primary_source
  reference: https://www.panchemcorp.com/pdf/product/Manganese-Sulfate-Monohydrate-Spec-Sheet.pdf
  locator: Complete one-page product sheet, title, table and Application
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: 'Fresh PDF read and visually checked: manufactured monohydrate powder is
    marketed for feed and fertilizer. Numerical grade entries are not imported as
    universal limits, and the sheet does not qualify a battery product.'
  snapshot_sha256: efb8879e29299123b4d0a43ed58cb4cc229bcac2a25ba57d6b1bd2f1533780ae
- evidence_id: ihumate-monohydrate
  kind: primary_source
  reference: https://www.ihumate.com/manganese-sulfate-monohydrate
  locator: Product introduction, formula, specifications and agricultural-use sections
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: Fresh complete manufacturer HTML inspected. MnSO4.H2O identity and agricultural
    commodity use corroborate Pan Chem. Product-specific purity and Mn assays are
    not generalized, and published specifications are not recovered-product measurements.
  snapshot_sha256: f4f54ca586fbeb7a281469a05f70dcd2b4e7b82f196444d8fa926e8b9f146a49
- evidence_id: walsun-battery-context
  kind: primary_source
  reference: https://www.walsun-nm.com/EN/Home
  locator: Homepage Battery Industry section
  accessed_at: '2026-10-11T09:29:40Z'
  support: context_only
  summary: Fresh complete homepage independently read. It states high-purity manganese-sulfate
    cathode-precursor use, supporting context only. No precise composition or monohydrate
    identity is inferred from the homepage; previous product-route redirect is documented
    by the curator.
  snapshot_sha256: d8dbf1db12766831a0617948d3234966669d8c8bbc98d0f996ee5be7ba4711d2
- evidence_id: samr-4823
  kind: authority
  reference: https://std.samr.gov.cn/hb/search/stdHBDetailedCNF?id=037FCC3702C04EF6E06397BE0A0A09CA
  locator: HG/T 4823-2023 official registry entry
  accessed_at: '2026-10-11T09:29:40Z'
  support: supports
  summary: Fresh registry names manganese sulfate for batteries, a scope not restricted
    to the monohydrate by its title. Record treats it as metadata and does not invent
    table limits or collapse every battery manganese product to this salt.
  snapshot_sha256: 5e80dabc2a1c7e9c275d84e34da5e37a994ccefc6c6dbfc2f643d8913fdeca16
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
  summary: Manufactured MnSO4.H2O commodity, including agricultural products. Two
    complete primary product sources establish the hydrated salt and agricultural
    trade. Walsun is used only for high-purity manganese-sulfate battery context;
    neither homepage nor standards title is misused to assert universal monohydrate
    qualification.
  target_ids:
  - cmmmech:manganese-sulfate-monohydrate
  evidence_ids:
  - record
  - search
  - panchem-monohydrate
  - ihumate-monohydrate
  - walsun-battery-context
  - samr-4823
  dimensions:
  - name: material_form
    value: Manufactured MnSO4.H2O commodity, including agricultural products
    definition: Maintained commodity scope, distinct from constituent element, ions,
      mineral specimen or source feed.
    evidence_ids:
    - record
    - panchem-monohydrate
    - ihumate-monohydrate
    - walsun-battery-context
    - samr-4823
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
    - panchem-monohydrate
    - ihumate-monohydrate
    - walsun-battery-context
    - samr-4823
- assessment_id: evidence
  area: evidence
  topic: Primary specifications, versions and uncertainty
  outcome: supported
  summary: Two complete primary product sources establish the hydrated salt and agricultural
    trade. Walsun is used only for high-purity manganese-sulfate battery context;
    neither homepage nor standards title is misused to assert universal monohydrate
    qualification. HG/T 4823-2023 full tables were not acquired. Walsun provides homepage
    context, not a verified product qualification table; no universal purity threshold
    is asserted.
  target_ids:
  - cmmmech:manganese-sulfate-monohydrate
  evidence_ids:
  - panchem-monohydrate
  - ihumate-monohydrate
  - walsun-battery-context
  - samr-4823
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
  - cmmmech:manganese-sulfate-monohydrate
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- HG/T 4823-2023 full tables were not acquired. Walsun provides homepage context,
  not a verified product qualification table; no universal purity threshold is asserted.
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
