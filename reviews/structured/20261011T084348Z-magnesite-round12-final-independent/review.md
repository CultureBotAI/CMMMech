# magnesite independent final industrial commodity review

- Review: 20261011T084348Z-magnesite-round12-final-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:34:49.673170Z
- Finished UTC: 2026-10-11T08:43:48Z
- Reviewer: /root/cmm12_aluminium_boron (codex; agent_tool codex) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Source-defined industrial carbonate/magnesia category; not mineral-only magnesite, Mg element or every Mg compound. No microbial mechanism is asserted. Source-locatorF1 corrected and verified.

## Scope And Provenance

All fields, sources and linked history of one industrial commodity record; record-level scientific claim audit.

Selection: Assigned final frozen industrial record from7-recordcohort; separately reported observation.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:magnesite | data/records/magnesite.yaml | maintained | magnesite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:magnesite | After correction reviewer executed:1recordchecked,0failed. |
| Named history validation against trusted base | passed | True | cmmmech:magnesite | After correction reviewer executed:2historyrecordschecked,0errors. |
| Independent authority and primary claim audit | passed | True | cmmmech:magnesite | Material scope, dated designations, sources, identifiers/omissions and claim boundaries inspected; phosphate primary experiment independently checked where applicable. |
| Final batch checks | passed | True | cmmmech:magnesite | Root executed; reviewer read complete log: All checks passed; 307 passed, 3 skipped in70.99s; 93records and108histories valid. |
| Nonempty corpus validation | passed | True | cmmmech:magnesite | Root executed; reviewer read complete log:93records checked,0failed. |
| Whole batch history immutability and linkage | passed | True | cmmmech:magnesite | Root executed against trusted base; reviewer read complete log:108historyrecords checked,0errors. |

## Scientific And Domain Assessments

### Material form and dated authority mapping

identity: supported. Targets: cmmmech:magnesite.

Source-defined industrial carbonate/magnesia category; not mineral-only magnesite, Mg element or every Mg compound.

### Inline events and canonical history

provenance: supported. Targets: cmmmech:magnesite.

Linked CREATE history targets this record and records actual actor; distinct inline event describes creation. New EDIT history and inline event accurately describe issue50 locator correction.

### Mechanism omission and transfer boundary

scope: supported. Targets: cmmmech:magnesite.

No microbial mechanism asserted. Mineral transformation, constituent mobilization or reagent use cannot by itself identify this commodity or establish product manufacture. This is an evidence-bounded identity record, not a claim of absent microbial literature.

## Findings

### F1: USGS locator points to Lithium rather than Magnesium Compounds

minor / resolved / confirmed; issue key: magnesite-usgs-chapter-locator.

Earlier locator pointed to Lithium. Corrected title now identifies Magnesium Compounds printed120-121/PDF124-125; independently compared source pages. Actual EDIT history and inline provenance link issue50.

Disposition: Corrected final bytes match independently inspected Magnesium Compounds pages120-121/PDF124-125. Named record/history checks and root final batch gates passed; exact predecessorF1 retained.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/magnesite.yaml; Entire frozen record, all inline events and linked canonical sidecars | supports | Exact working-tree bytes inspected before assessment and rechecked after magnesite correction. Histories have matching target, actual codex/GPT-6/codex actor and issue links. No record was edited by this reviewer. |
| dedup | /private/tmp/cmm-r12-industrial-review/dedup.txt; 381 matching lines across data,research,reviews,history; raw-dedup.txt1860 matching lines | context_only | Ignored/hidden and symlink-following searches locate the distinct commodity targets; inspected fluorine, magnesium and phosphorus element boundaries. No duplicate identity established within checked scope. |
| mcs | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf; Magnesium Compounds printed120-121/PDF124-125; Domestic Production and Use, crude magnesite and magnesia tariff rows | supports | Source-defined industrial carbonate/magnesia category; not mineral-only magnesite, Mg element or every Mg compound. Retained government PDF independently rehashed and chapter text read; web PDF fetch403, so not represented as a fresh acquisition. |
| bgs | https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf; Cover; Table11 printed44/PDF48 visually inspected; section2.6.3 printed29/PDF33; magnesite HS printed259/PDF263 and sodium HS printed276/PDF280 visually inspected | supports | Source-defined industrial carbonate/magnesia category; not mineral-only magnesite, Mg element or every Mg compound. NORA live metadata confirms OR/24/059. Assessment explicitly is not government policy. Retained PDF rehashed independently. |
| gate_check | /private/tmp/cmm-round12-check.log; Complete root-owned final log, finished2026-10-11T08:43:00.264161+00:00; receipt/private/tmp/cmm-round12-gate-receipts.json | supports | Root executed; reviewer read complete log: All checks passed; 307 passed, 3 skipped in70.99s; 93records and108histories valid. Record hash equals root gated-state receipt; reviewer did not rerun full batch. |
| gate_require | /private/tmp/cmm-round12-require.log; Complete root-owned final log, finished2026-10-11T08:43:03.641511+00:00; receipt/private/tmp/cmm-round12-gate-receipts.json | supports | Root executed; reviewer read complete log:93records checked,0failed. Record hash equals root gated-state receipt; reviewer did not rerun full batch. |
| gate_history | /private/tmp/cmm-round12-history.log; Complete root-owned final log, finished2026-10-11T08:43:06.111227+00:00; receipt/private/tmp/cmm-round12-gate-receipts.json | supports | Root executed against trusted base; reviewer read complete log:108historyrecords checked,0errors. Record hash equals root gated-state receipt; reviewer did not rerun full batch. |
| gated_hash | /private/tmp/cmm-round12-gated-record-hashes.json; data/records/magnesite.yaml | supports | Reviewed target SHA25673cbffddbc86a7f01fe4090a29ed6907c057343cf3acfa4d4acc840c2304520b equals root final gated-state receipt and current bytes. |

## Limits And Additional Notes

- Single-record scientific observation; not a whole-literature completeness or no-microbes claim.
- Raw artifacts retained outside Git; some primary material was initially acquired by curator and independently inspected by reviewer. Official list pages were also checked live.
- Dated criticality assessment only; no claim to current consolidated legislation, current market purity specification, industrial deployment or product certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T084348Z-magnesite-round12-final-independent
kind: record
repository: CultureBotAI/CMMMech
title: magnesite independent final industrial commodity review
started_at: '2026-10-11T08:34:49.673170Z'
finished_at: '2026-10-11T08:43:48Z'
reviewer:
  identity: /root/cmm12_aluminium_boron (codex; agent_tool codex)
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from industrial-record curator; authored none
    of the seven targets or their histories. Independently inspected official sources
    and rehashed retained raw PDFs. Same model family and shared workspace; dossier
    used as leads, not as proof.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Source-defined industrial carbonate/magnesia category; not mineral-only magnesite,
  Mg element or every Mg compound. No microbial mechanism is asserted. Source-locatorF1
  corrected and verified.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: .claude/skills/review-record/SKILL.md
    sha256: abe8f0aebf9540aaaf5d2e2c2b43a4b17b7d5963d04e084b65e1ada19f4eb6be
    role: context
  - path: data/records/magnesite.yaml
    sha256: 73cbffddbc86a7f01fe4090a29ed6907c057343cf3acfa4d4acc840c2304520b
    role: target
  - path: docs/record-review-profile.md
    sha256: 93f65e8f516a9b7756afd89e4823c1b64e493a46ecbcb3ca5e54a5aa599b10f2
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/magnesite/2026-10-11T082911Z-codex-03059a.yaml
    sha256: 30cbab13938a930a5c2a90537591ff7c4984c8e5337dbf3f5fab4a91b914acf4
    role: context
  - path: history/records/magnesite/2026-10-11T083913Z-codex-06dbdb.yaml
    sha256: c858a88932e7758fd46e5542188e3fa51c46485233e52908133e30adc9c2564e
    role: context
  - path: research/ingests/round12-industrial-minerals-20261011.json
    sha256: bdd49307b60bc1487777674672e77eb9e9abd467c7728ce7c733f5a41b3fd2a5
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, sources and linked history of one industrial commodity
    record; record-level scientific claim audit.
  selection: Assigned final frozen industrial record from7-recordcohort; separately
    reported observation.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:magnesite
  exclusions:
  - target: Other six assigned records and full external literature
    reason: Other records receive separate observations; no exhaustive literature/marketplace
      claim.
targets:
- target_id: cmmmech:magnesite
  path: data/records/magnesite.yaml
  label: magnesite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
  record_class: commodity
checks:
- check_id: record
  name: Named record validation
  status: passed
  required: true
  target_ids:
  - cmmmech:magnesite
  summary: After correction reviewer executed:1recordchecked,0failed.
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/magnesite.yaml
  exit_code: 0
- check_id: history
  name: Named history validation against trusted base
  status: passed
  required: true
  target_ids:
  - cmmmech:magnesite
  summary: After correction reviewer executed:2historyrecordschecked,0errors.
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4 history/records/magnesite
  exit_code: 0
- check_id: science
  name: Independent authority and primary claim audit
  status: passed
  required: true
  summary: Material scope, dated designations, sources, identifiers/omissions and
    claim boundaries inspected; phosphate primary experiment independently checked
    where applicable.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
  - dedup
  - mcs
  - bgs
- check_id: gate_check
  name: Final batch checks
  status: passed
  required: true
  summary: 'Root executed; reviewer read complete log: All checks passed; 307 passed,
    3 skipped in70.99s; 93records and108histories valid.'
  target_ids:
  - cmmmech:magnesite
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gate_check
  scope_note: Executed by root, independently read receipt and output; final target
    bytes match gated hashes.
- check_id: gate_require
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: Root executed; reviewer read complete log:93records checked,0failed.
  target_ids:
  - cmmmech:magnesite
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gate_require
  scope_note: Executed by root, independently read receipt and output; final target
    bytes match gated hashes.
- check_id: gate_history
  name: Whole batch history immutability and linkage
  status: passed
  required: true
  summary: Root executed against trusted base; reviewer read complete log:108historyrecords
    checked,0errors.
  target_ids:
  - cmmmech:magnesite
  command: uv run --locked cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gate_history
  scope_note: Executed by root, independently read receipt and output; final target
    bytes match gated hashes.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/magnesite.yaml
  locator: Entire frozen record, all inline events and linked canonical sidecars
  accessed_at: '2026-10-11T08:41:57Z'
  support: supports
  summary: Exact working-tree bytes inspected before assessment and rechecked after
    magnesite correction. Histories have matching target, actual codex/GPT-6/codex
    actor and issue links. No record was edited by this reviewer.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-r12-industrial-review/dedup.txt
  locator: 381 matching lines across data,research,reviews,history; raw-dedup.txt1860
    matching lines
  accessed_at: '2026-10-11T08:41:57Z'
  support: context_only
  summary: Ignored/hidden and symlink-following searches locate the distinct commodity
    targets; inspected fluorine, magnesium and phosphorus element boundaries. No duplicate
    identity established within checked scope.
  search_scope: rg --no-ignore --hidden -L -n -i 'baryte|barite|fluorspar|feldspar|magnesite|phosphate.rock|potash|sodium.compounds'
    data research reviews history; same query in /private/tmp/cmm-round12-industrial-minerals-raw,/private/tmp/cmm-round9-graphite-evidence,/private/tmp/cmm-round10-graphite-raw.
    This is bounded, not machine-wide absence.
- evidence_id: mcs
  kind: authority
  reference: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf
  locator: Magnesium Compounds printed120-121/PDF124-125; Domestic Production and
    Use, crude magnesite and magnesia tariff rows
  accessed_at: '2026-10-11T08:41:57Z'
  support: supports
  summary: Source-defined industrial carbonate/magnesia category; not mineral-only
    magnesite, Mg element or every Mg compound. Retained government PDF independently
    rehashed and chapter text read; web PDF fetch403, so not represented as a fresh
    acquisition.
  snapshot_sha256: 595e6e66674236dea40125a03eb1ea6b347f331c0bcf3411a1e77eba53c0d391
- evidence_id: bgs
  kind: authority
  reference: https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf
  locator: Cover; Table11 printed44/PDF48 visually inspected; section2.6.3 printed29/PDF33;
    magnesite HS printed259/PDF263 and sodium HS printed276/PDF280 visually inspected
  accessed_at: '2026-10-11T08:41:57Z'
  support: supports
  summary: Source-defined industrial carbonate/magnesia category; not mineral-only
    magnesite, Mg element or every Mg compound. NORA live metadata confirms OR/24/059.
    Assessment explicitly is not government policy. Retained PDF rehashed independently.
  snapshot_sha256: e5708ffb1080c874cc57f0e20aad8f99aea746977971280434a1cfbb37f28c9e
- evidence_id: gate_check
  kind: validation
  reference: /private/tmp/cmm-round12-check.log
  locator: Complete root-owned final log, finished2026-10-11T08:43:00.264161+00:00;
    receipt/private/tmp/cmm-round12-gate-receipts.json
  accessed_at: '2026-10-11T08:43:48Z'
  support: supports
  summary: 'Root executed; reviewer read complete log: All checks passed; 307 passed,
    3 skipped in70.99s; 93records and108histories valid. Record hash equals root gated-state
    receipt; reviewer did not rerun full batch.'
  snapshot_sha256: a093602a1e96ab91673b951c13ef691df8bc9fa67ecab8e54bd0d0aeeddbb337
- evidence_id: gate_require
  kind: validation
  reference: /private/tmp/cmm-round12-require.log
  locator: Complete root-owned final log, finished2026-10-11T08:43:03.641511+00:00;
    receipt/private/tmp/cmm-round12-gate-receipts.json
  accessed_at: '2026-10-11T08:43:48Z'
  support: supports
  summary: Root executed; reviewer read complete log:93records checked,0failed. Record
    hash equals root gated-state receipt; reviewer did not rerun full batch.
  snapshot_sha256: 5c98c2e81d5699e56e4603cf13c61a6e946d93b16be04e7a3cb5e8858664ba23
- evidence_id: gate_history
  kind: validation
  reference: /private/tmp/cmm-round12-history.log
  locator: Complete root-owned final log, finished2026-10-11T08:43:06.111227+00:00;
    receipt/private/tmp/cmm-round12-gate-receipts.json
  accessed_at: '2026-10-11T08:43:48Z'
  support: supports
  summary: Root executed against trusted base; reviewer read complete log:108historyrecords
    checked,0errors. Record hash equals root gated-state receipt; reviewer did not
    rerun full batch.
  snapshot_sha256: 6015018bcf313e8ec2bbd4d06fe336eebcd52bd0e8a877e2dee97ef769a5ddf2
- evidence_id: gated_hash
  kind: validation
  reference: /private/tmp/cmm-round12-gated-record-hashes.json
  locator: data/records/magnesite.yaml
  accessed_at: '2026-10-11T08:43:48Z'
  support: supports
  summary: Reviewed target SHA25673cbffddbc86a7f01fe4090a29ed6907c057343cf3acfa4d4acc840c2304520b
    equals root final gated-state receipt and current bytes.
  snapshot_sha256: 63d9af22c021e1d76e68be063c7c4288869ded8b9687d8c965b52010cd5cf37c
assessments:
- assessment_id: identity
  area: identity
  topic: Material form and dated authority mapping
  outcome: supported
  summary: Source-defined industrial carbonate/magnesia category; not mineral-only
    magnesite, Mg element or every Mg compound.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
  - mcs
  - bgs
  dimensions:
  - name: material_form
    value: commodity
    definition: Maintained industrial material rather than element, ion or taxonomic
      mineral species.
    evidence_ids:
    - record
    - mcs
    - bgs
  - name: criticality
    value: United Kingdom; British Geological Survey / CMIC UK 2024 Criticality Assessment,
      Table 11; 2024; Open Report OR/24/059; critical
    definition: Exact asserted jurisdiction, authority, list and edition; no global
      timeless claim.
    evidence_ids:
    - mcs
    - bgs
  - name: identifiers
    value: No external material or organism CURIE asserted
    definition: No identifier resolution claim or transfer from constituent to commodity.
    evidence_ids:
    - record
- assessment_id: provenance
  area: provenance
  topic: Inline events and canonical history
  outcome: supported
  summary: Linked CREATE history targets this record and records actual actor; distinct
    inline event describes creation. New EDIT history and inline event accurately
    describe issue50 locator correction.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
- assessment_id: mechanism
  area: scope
  topic: Mechanism omission and transfer boundary
  outcome: supported
  summary: No microbial mechanism asserted. Mineral transformation, constituent mobilization
    or reagent use cannot by itself identify this commodity or establish product manufacture.
    This is an evidence-bounded identity record, not a claim of absent microbial literature.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
findings:
- finding_id: F1
  issue_key: magnesite-usgs-chapter-locator
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: USGS locator points to Lithium rather than Magnesium Compounds
  description: Earlier locator pointed to Lithium. Corrected title now identifies
    Magnesium Compounds printed120-121/PDF124-125; independently compared source pages.
    Actual EDIT history and inline provenance link issue50.
  target_ids:
  - cmmmech:magnesite
  field_paths:
  - sources[1].title
  evidence_ids:
  - record
  - mcs
  rule_id: primary-source-locator
  native_severity: minor
  normalization_reason: Bounded citation locator error; no change to identity or criticality.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261011T083659Z-magnesite-round12-independent
    finding_id: F1
  disposition_reason: Corrected final bytes match independently inspected Magnesium
    Compounds pages120-121/PDF124-125. Named record/history checks and root final
    batch gates passed; exact predecessorF1 retained.
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/50
actions: []
limitations:
- Single-record scientific observation; not a whole-literature completeness or no-microbes
  claim.
- Raw artifacts retained outside Git; some primary material was initially acquired
  by curator and independently inspected by reviewer. Official list pages were also
  checked live.
- Dated criticality assessment only; no claim to current consolidated legislation,
  current market purity specification, industrial deployment or product certification.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261011T083659Z-magnesite-round12-independent
  relationship: Successor rechecks final corrected magnesite bytes and explicitly
    resolves same F1.
tags:
- round12
- independent
- commodity
```
