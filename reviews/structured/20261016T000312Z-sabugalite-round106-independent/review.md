# Independent scientific review of sabugalite

- Review: 20261016T000312Z-sabugalite-round106-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T23:53:03.009403Z
- Finished UTC: 2026-10-16T00:03:12.463210Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Accept sabugalite identity and bounded historical laboratory dehydration; no corrective owner defect supported.

## Scope And Provenance

Entire owner/history; primary evidence relevant to accepted claims, no independent diffraction reanalysis.

Selection: Frozen owner and sidecar captured using native inspect before final adjudication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base af6cbead934deb4667764fa4a325246158ee4a0a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:sabugalite | data/records/sabugalite.yaml | maintained | sabugalite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:sabugalite | Actual two-record validation passed. |
| Batch gate 1 | passed | True | cmmmech:sabugalite | Actual terminal receipt/log and unchanged record hashes verified. |
| Batch gate 2 | passed | True | cmmmech:sabugalite | Actual terminal receipt/log and unchanged record hashes verified. |
| Batch gate 3 | passed | True | cmmmech:sabugalite | Actual terminal receipt/log and unchanged record hashes verified. |
| Batch gate 4 | passed | True | cmmmech:sabugalite | Actual terminal receipt/log and unchanged record hashes verified. |

## Scientific And Domain Assessments

### Material and hydration identity

identity: supported. Targets: cmmmech:sabugalite.

Dated IMA mineral species remains separate from constituent elements and related hydrates; no inherited criticality.

### Primary experiment scope

evidence: supported. Targets: cmmmech:sabugalite.

Natural Mina da Quarta Seira specimens, unheated comparison, reported44/68C unchanged powder patterns,101/117C mixtures and135/165C source-assigned meta-II match the original. Water losses3.4/20/57/63/82/91% refer to original water, not mineral mass or U recovery. Nonequilibrium heating, optical heterogeneity, missing durations/humidity, Kariz admixture and negative syntheses are preserved.

### Measured versus refined or interpreted outcomes

quantity: supported. Targets: cmmmech:sabugalite.

Source denominators and refinement assumptions are explicit; no unverified concentration cell, process optimum or industrial yield added.

### Exact reviewed inputs

provenance: supported. Targets: cmmmech:sabugalite.

Native inspection hashes bind the record and actual canonical CREATE sidecar. Literature access and version limits are explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/sabugalite.yaml; Entire frozen owner. Local artifact: /private/tmp/CMMMech-expansion-round106-20261015/data/records/sabugalite.yaml | supports | All accepted identity, quantitative and mechanism claims independently assessed against the cited originals. |
| history | history/records/sabugalite/2026-10-15T235122Z-codex-d635a6.yaml; Canonical CREATE and separate inline event. Local artifact: /private/tmp/CMMMech-expansion-round106-20261015/history/records/sabugalite/2026-10-15T235122Z-codex-d635a6.yaml | supports | Actual timestamp, actor, target and work agree; no invented prior authorship. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF190 exact rows independently visually checked; authority opened live. Local artifact: /private/tmp/cmm-round106-uranium-research/ima202609.pdf | supports | Distinct mineral identity/formula; G and description year do not represent a numbered IMA approval. |
| primary | https://www.rruff.net/doclib/am/vol36/AM36_671.pdf; Complete nine-page original text read; original chemistry/Table4 and heating/Tables5-6/negative synthesis pp675,677-679 independently visually checked. Local artifact: /private/tmp/cmm-round106-uranium-research/sabugalite1951.pdf | supports | Natural Mina da Quarta Seira specimens, unheated comparison, reported44/68C unchanged powder patterns,101/117C mixtures and135/165C source-assigned meta-II match the original. Water losses3.4/20/57/63/82/91% refer to original water, not mineral mass or U recovery. Nonequilibrium heating, optical heterogeneity, missing durations/humidity, Kariz admixture and negative syntheses are preserved. |
| search | Independent live correction/metadata search; Exact queries and opened authority/repository/publisher pages in retained receipt. Local artifact: /private/tmp/cmm-round106-uranium-independent-search.json | context_only | No applicable notice for accepted2016/1951articles surfaced in returned windows; separate2006publisher Erratum remains deferred. |
| dedup | Bounded hidden/ignored-inclusive source inventory; Curator inventory independently examined, not a new machine-wide search. Local artifact: /private/tmp/cmm-round106-uranium-research/dedup-final.json | context_only | Relevant worktree roots, original-main reports and cited raw roots include hidden/ignored files and followed symlinks; species/hydration boundaries retained. |
| named | Independent named validation; Actual command and output in named_validation. Local artifact: /private/tmp/cmm-round106-uranium-independent-search.json | supports | Two records checked; zero failed. |
| batch | Completed batch gate receipt; Actual root executions and verified log SHA a9a6a4518415a7cf09b170ec21c25ac7ee9e242aac5be1196a4eac7ec00904a2. Local artifact: /private/tmp/cmm-round106-final-gates.json | supports | Check, nonempty corpus, append-only history and rendered pages pass with unchanged record inputs. |

## Limits And Additional Notes

- The1951meta-II attribution is a historical phase interpretation, not independent modern species identification or a universal equilibrium transition. Unknown heating durations/atmosphere/humidity and replication limit transfer.
- The1983synthesis paper and2006original/correction remain uninspected; the publisher2006Erratum landing is metadata/abstract only. No later numerical values are accepted or treated as matched refutations.
- No microbial activity, isolated uranium product or industrial deployment is established.
- Correction searches are bounded returned windows, not proof of universal absence. Separate publication review and hosted CI remain later gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T000312Z-sabugalite-round106-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of sabugalite
started_at: '2026-10-15T23:53:03.009403Z'
finished_at: '2026-10-16T00:03:12.463210Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored this owner/history. Root authored a separate
    catalyst owner and independently assessed these exact mineral bytes and primary
    evidence without editing the owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Accept sabugalite identity and bounded historical laboratory dehydration;
  no corrective owner defect supported.
source:
  git_revision: af6cbead934deb4667764fa4a325246158ee4a0a
  state: working_tree
  inputs:
  - path: data/records/sabugalite.yaml
    sha256: 246ece1435a6391cf55c8c73691d7cd6d6de5dc5de694bc9958bc84187442705
    role: target
  - path: history/records/sabugalite/2026-10-15T235122Z-codex-d635a6.yaml
    sha256: b2ba304f8b3f0bb2eac34bbc3732aec946eb547c384e38f1078815ed1182a537
    role: context
targets:
- target_id: cmmmech:sabugalite
  path: data/records/sabugalite.yaml
  label: sabugalite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sabugalite.yaml
    role: maintained
scope:
  description: Entire owner/history; primary evidence relevant to accepted claims,
    no independent diffraction reanalysis.
  selection: Frozen owner and sidecar captured using native inspect before final adjudication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:sabugalite
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/saleeite.yaml data/records/sabugalite.yaml
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual two-record validation passed.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - named
- check_id: batch1
  name: Batch gate 1
  command: just check
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal receipt/log and unchanged record hashes verified.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - batch
- check_id: batch2
  name: Batch gate 2
  command: uv run --locked cmmmech validate --require-records
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal receipt/log and unchanged record hashes verified.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - batch
- check_id: batch3
  name: Batch gate 3
  command: uv run --locked cmmmech validate-history --base af6cbead934deb4667764fa4a325246158ee4a0a
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal receipt/log and unchanged record hashes verified.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - batch
- check_id: batch4
  name: Batch gate 4
  command: uv run --locked python scripts/render_pages.py --check
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal receipt/log and unchanged record hashes verified.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/sabugalite.yaml
  locator: 'Entire frozen owner. Local artifact: /private/tmp/CMMMech-expansion-round106-20261015/data/records/sabugalite.yaml'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: 246ece1435a6391cf55c8c73691d7cd6d6de5dc5de694bc9958bc84187442705
  support: supports
  summary: All accepted identity, quantitative and mechanism claims independently
    assessed against the cited originals.
- evidence_id: history
  kind: record_content
  reference: history/records/sabugalite/2026-10-15T235122Z-codex-d635a6.yaml
  locator: 'Canonical CREATE and separate inline event. Local artifact: /private/tmp/CMMMech-expansion-round106-20261015/history/records/sabugalite/2026-10-15T235122Z-codex-d635a6.yaml'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: b2ba304f8b3f0bb2eac34bbc3732aec946eb547c384e38f1078815ed1182a537
  support: supports
  summary: Actual timestamp, actor, target and work agree; no invented prior authorship.
- evidence_id: ima
  kind: database
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'PDF190 exact rows independently visually checked; authority opened live.
    Local artifact: /private/tmp/cmm-round106-uranium-research/ima202609.pdf'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Distinct mineral identity/formula; G and description year do not represent
    a numbered IMA approval.
- evidence_id: primary
  kind: primary_source
  reference: https://www.rruff.net/doclib/am/vol36/AM36_671.pdf
  locator: 'Complete nine-page original text read; original chemistry/Table4 and heating/Tables5-6/negative
    synthesis pp675,677-679 independently visually checked. Local artifact: /private/tmp/cmm-round106-uranium-research/sabugalite1951.pdf'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: 1840596f3e7b58561e1c39650eb3fe16bd56050a2e0fef70771b7e27974406b6
  support: supports
  summary: Natural Mina da Quarta Seira specimens, unheated comparison, reported44/68C
    unchanged powder patterns,101/117C mixtures and135/165C source-assigned meta-II
    match the original. Water losses3.4/20/57/63/82/91% refer to original water, not
    mineral mass or U recovery. Nonequilibrium heating, optical heterogeneity, missing
    durations/humidity, Kariz admixture and negative syntheses are preserved.
- evidence_id: search
  kind: search
  reference: Independent live correction/metadata search
  locator: 'Exact queries and opened authority/repository/publisher pages in retained
    receipt. Local artifact: /private/tmp/cmm-round106-uranium-independent-search.json'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: d9a9a61e334639a4a15e6b34a3d456f2e0248b4c822fd7b885245f04bd8a3173
  support: context_only
  summary: No applicable notice for accepted2016/1951articles surfaced in returned
    windows; separate2006publisher Erratum remains deferred.
  search_scope: Three exact-topic web queries, returned top-result windows, no exhaustive
    paging; primary authority/repository pages opened live.
- evidence_id: dedup
  kind: search
  reference: Bounded hidden/ignored-inclusive source inventory
  locator: 'Curator inventory independently examined, not a new machine-wide search.
    Local artifact: /private/tmp/cmm-round106-uranium-research/dedup-final.json'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: 12fbe0f27a4993e716bcc6e6b03974cf5eb9a4878c0815f81104a7eea87edcef
  support: context_only
  summary: Relevant worktree roots, original-main reports and cited raw roots include
    hidden/ignored files and followed symlinks; species/hydration boundaries retained.
  search_scope: The listed worktree/main/cited raw roots in dedup-final.json, including
    hidden and ignored files and followed relevant symlinks;293 issue titles/bodies,
    comments excluded. Curator inventory reused and independently inspected.
- evidence_id: named
  kind: validation
  reference: Independent named validation
  locator: 'Actual command and output in named_validation. Local artifact: /private/tmp/cmm-round106-uranium-independent-search.json'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: d9a9a61e334639a4a15e6b34a3d456f2e0248b4c822fd7b885245f04bd8a3173
  support: supports
  summary: Two records checked; zero failed.
- evidence_id: batch
  kind: validation
  reference: Completed batch gate receipt
  locator: 'Actual root executions and verified log SHA a9a6a4518415a7cf09b170ec21c25ac7ee9e242aac5be1196a4eac7ec00904a2.
    Local artifact: /private/tmp/cmm-round106-final-gates.json'
  accessed_at: '2026-10-16T00:03:12.463210Z'
  snapshot_sha256: 07e2c865ebe0631473c42a0559d1ee5828246210a380a119ab2e8d5a78518aaf
  support: supports
  summary: Check, nonempty corpus, append-only history and rendered pages pass with
    unchanged record inputs.
assessments:
- assessment_id: identity
  area: identity
  topic: Material and hydration identity
  outcome: supported
  summary: Dated IMA mineral species remains separate from constituent elements and
    related hydrates; no inherited criticality.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - ima
  - owner
  - dedup
- assessment_id: science
  area: evidence
  topic: Primary experiment scope
  outcome: supported
  summary: Natural Mina da Quarta Seira specimens, unheated comparison, reported44/68C
    unchanged powder patterns,101/117C mixtures and135/165C source-assigned meta-II
    match the original. Water losses3.4/20/57/63/82/91% refer to original water, not
    mineral mass or U recovery. Nonequilibrium heating, optical heterogeneity, missing
    durations/humidity, Kariz admixture and negative syntheses are preserved.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - primary
  - owner
- assessment_id: quantity
  area: quantity
  topic: Measured versus refined or interpreted outcomes
  outcome: supported
  summary: Source denominators and refinement assumptions are explicit; no unverified
    concentration cell, process optimum or industrial yield added.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - primary
  - owner
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed inputs
  outcome: supported
  summary: Native inspection hashes bind the record and actual canonical CREATE sidecar.
    Literature access and version limits are explicit.
  target_ids:
  - cmmmech:sabugalite
  evidence_ids:
  - history
  - owner
  - search
  - named
  - batch
findings: []
actions: []
limitations:
- The1951meta-II attribution is a historical phase interpretation, not independent
  modern species identification or a universal equilibrium transition. Unknown heating
  durations/atmosphere/humidity and replication limit transfer.
- The1983synthesis paper and2006original/correction remain uninspected; the publisher2006Erratum
  landing is metadata/abstract only. No later numerical values are accepted or treated
  as matched refutations.
- No microbial activity, isolated uranium product or industrial deployment is established.
- Correction searches are bounded returned windows, not proof of universal absence.
  Separate publication review and hosted CI remain later gates.
```
