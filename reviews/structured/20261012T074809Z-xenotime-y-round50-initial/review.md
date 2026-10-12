# Independent initial scientific review of Xenotime-(Y)

- Review: 20261012T074809Z-xenotime-y-round50-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T07:45:11Z
- Finished UTC: 2026-10-12T07:48:09Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Natural Xenotime-(Y) identity and structural scope are supported, but one synthetic-comparator attribution is not: the primary study does not report a synthetic YPO4 specimen. F1 requires a bounded wording correction. Parent final batch gates remain pending.

## Scope And Provenance

All target fields and explicit history/dossier/schema context; main six-page original, all five figures/three main tables and IMA identity.

Selection: Assigned peer-authored named record
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 98e787e8d61593797aef1ed29840b2315a0cc6e5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:xenotime-y | data/records/xenotime-y.yaml | maintained | xenotime-y |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:xenotime-y | Personally executed; Checked2records;0failed. |
| Parent complete cohort checks | unavailable | True | cmmmech:xenotime-y | Running at initial observation; no terminal success claimed. Corrected target will require affected checks and successor review. |

## Scientific And Domain Assessments

### Natural species versus synthetic comparator

identity: concern. Targets: cmmmech:xenotime-y.

Y-dominant natural phosphate, tetragonal I4_1/amd and eight-coordinate rare-earth site supported; F1 concerns only the claimed synthetic YPO4 arm.

### Measured structure and biological boundaries

evidence: supported. Targets: cmmmech:xenotime-y.

No microbial mechanism, strain, criticality, grade, recovery denominator or industrial deployment asserted. Crystal-structure comparison is not an observed transformation experiment. Missing deposited tables are disclosed.

## Findings

### F1: Synthetic YPO4 is incorrectly attributed to the Ni1995 experimental set

minor / open / confirmed; issue key: CMMMech.xenotime-y.synthetic-comparator-attribution.

Description states that synthetic YPO4 was examined in the same study. Methods specify14synthetic phases and Tables1–2 list La–Gd and Tb–Lu phosphates (excludingPm), with natural Y-dominant xenotime separate. Table3 compares the natural xenotime with syntheticHoPO4. The paper cites earlier syntheticYPO4 work but does not identify a measured syntheticYPO4 comparator. Replace with source-supported synthetic rare-earth phosphate comparators without changing natural identity.

## Recommended Actions And Acceptance Checks

### A1

Correct the comparator phrase, append actual EDIT history/inline event and a source correction note; preserve initial artifacts.

- Original Methods/Tables1–3 support corrected phrase without claiming syntheticYPO4 was tested.
- Repeat named and affected cohort checks; retain original CREATE and initial review.
- Save successor with exact F1 occurrence/key, issue link and final hashes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/xenotime-y.yaml; Complete frozen record and explicit history/dossier/schema inputs | supports | Exact inspected target retains its original bytes. |
| primary | https://www.msaweb.org/MSA/AmMin/TOC/Articles_Free/1995/Ni_p21-26_95.pdf; All six original pages21–26; Figures1–5, Tables1–3 personally inspected | refutes | Methods identify the natural Y-dominant Nanling specimen. Synthetic columns in Table2 are Tb/Dy/Ho/Er/Tm/Yb/Lu phosphates, not YPO4. Table3 compares natural xenotime with synthetic HoPO4; prior syntheticYPO4 appears in cited1982reference. DepositedTables4–5 are not inspected. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions/terms pages1–2 and Xenotime-(Y) row page236 personally viewed | supports | Current authority supports Y(PO4), renamed status,1987special procedure; year is not a unique accession. |
| dedup | /private/tmp/cmm-round50-ree-peer/dedup.json; Independent reviewer names/DOI search | supports | Related elements, monazite-Nd and source leads are distinct from the proposed species owner; no competing accepted owner identified within bounded search. |
| notices | https://www.msaweb.org/MSA/AmMin/TOC/Articles_Free/1995/Ni_p21-26_95.pdf; Fresh exact DOI notice query and title plus syntheticYPO4 query on2026-10-12 | supports | Returned official primary and related later literature, no applicable notice in the first result sets. Primary page/table evidence establishes F1; later unread studies not accepted. |

## Limits And Additional Notes

- Initial observation is partial because parent batch checks are pending and F1 is unresolved.
- DepositedTables4–5 not inspected; no structure re-refinement or comprehensive literature reassessment.
- Searches bounded as stated; no unextracted-binary or global absence claim.
- No target/Git/GitHub mutations by reviewer; initial finding saved before author correction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T074809Z-xenotime-y-round50-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial scientific review of Xenotime-(Y)
started_at: '2026-10-12T07:45:11Z'
finished_at: '2026-10-12T07:48:09Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this target, sidecar and source dossier. Reviewer
    authored separate FTT resource, not either rare-earth mineral. Native inspect
    captured all five inputs before assessment; target-kind metadata was normalized
    from record to maintained with identical source hashes before save. Personally
    inspected complete main original and authority pages; no target edits.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Natural Xenotime-(Y) identity and structural scope are supported, but one
  synthetic-comparator attribution is not: the primary study does not report a synthetic
  YPO4 specimen. F1 requires a bounded wording correction. Parent final batch gates
  remain pending.'
source:
  git_revision: 98e787e8d61593797aef1ed29840b2315a0cc6e5
  state: working_tree
  inputs:
  - path: data/records/xenotime-y.yaml
    sha256: 24c0f45ad501802aa8d8469058f0b3b879ee56383bc45c785fcf5c30a0d5af67
    role: target
  - path: history/records/xenotime-y/2026-10-12T074113Z-codex-6478df.yaml
    sha256: dda137ebe5b66b1162e9561657315982e9f966dbe16454c4273d7805a485de6a
    role: context
  - path: research/sources/round50-ree-minerals/20261012T074105Z-source-investigation.json
    sha256: be51e4698977f3a1190c66d7703a29a1754a19d47b67ee3c02cda1878f87b0a4
    role: context
  - path: research/sources/round50-ree-minerals/20261012T074105Z-source-investigation.md
    sha256: 534fb9f925beca23c0a8cdd62cdacf2d292b5c7aea76ad78497ba4aef9c0ff3f
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:xenotime-y
  path: data/records/xenotime-y.yaml
  label: xenotime-y
  kind: maintained
  ownership_note: Maintained scientific YAML; root authored, reviewer /root/round27_packaging
    did not.
scope:
  description: All target fields and explicit history/dossier/schema context; main
    six-page original, all five figures/three main tables and IMA identity.
  selection: Assigned peer-authored named record
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:xenotime-y
  exclusions:
  - target: Deposited Tables4–5 and deferred microbial-feed literature
    reason: Deposited originals not visually available; no raw refinement values or
      microbial claim adopted.
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/monazite-ce.yaml data/records/xenotime-y.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:xenotime-y
  summary: Personally executed; Checked2records;0failed.
- check_id: batch
  name: Parent complete cohort checks
  command: just check; cmmmech validate --require-records; cmmmech validate-history
    --base 98e787e8d61593797aef1ed29840b2315a0cc6e5
  status: unavailable
  required: true
  target_ids:
  - cmmmech:xenotime-y
  summary: Running at initial observation; no terminal success claimed. Corrected
    target will require affected checks and successor review.
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/xenotime-y.yaml
  locator: Complete frozen record and explicit history/dossier/schema inputs
  accessed_at: '2026-10-12T07:48:09Z'
  support: supports
  summary: Exact inspected target retains its original bytes.
  snapshot_sha256: 24c0f45ad501802aa8d8469058f0b3b879ee56383bc45c785fcf5c30a0d5af67
- evidence_id: primary
  kind: primary_source
  reference: https://www.msaweb.org/MSA/AmMin/TOC/Articles_Free/1995/Ni_p21-26_95.pdf
  locator: All six original pages21–26; Figures1–5, Tables1–3 personally inspected
  accessed_at: '2026-10-12T07:48:09Z'
  support: refutes
  summary: Methods identify the natural Y-dominant Nanling specimen. Synthetic columns
    in Table2 are Tb/Dy/Ho/Er/Tm/Yb/Lu phosphates, not YPO4. Table3 compares natural
    xenotime with synthetic HoPO4; prior syntheticYPO4 appears in cited1982reference.
    DepositedTables4–5 are not inspected.
  snapshot_sha256: d1e4aba888865b3a7cf56409dc14f058db8f6f866095315f073964d44c7a6d24
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions/terms pages1–2 and Xenotime-(Y) row page236 personally viewed
  accessed_at: '2026-10-12T07:48:09Z'
  support: supports
  summary: Current authority supports Y(PO4), renamed status,1987special procedure;
    year is not a unique accession.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round50-ree-peer/dedup.json
  locator: Independent reviewer names/DOI search
  accessed_at: '2026-10-12T07:48:09Z'
  support: supports
  summary: Related elements, monazite-Nd and source leads are distinct from the proposed
    species owner; no competing accepted owner identified within bounded search.
  snapshot_sha256: fed71fcabe7c0416f3b7175721abf44642f58390cccbdee18bc14e582d877948
  search_scope: Two checkouts scientific directories plus181 existing cited raw roots;
    rg --no-ignore --hidden --follow, text formats; nine missing roots and unextracted
    binaries excluded. Results are not a machine-wide absence claim.
- evidence_id: notices
  kind: search
  reference: https://www.msaweb.org/MSA/AmMin/TOC/Articles_Free/1995/Ni_p21-26_95.pdf
  locator: Fresh exact DOI notice query and title plus syntheticYPO4 query on2026-10-12
  accessed_at: '2026-10-12T07:48:09Z'
  support: supports
  summary: Returned official primary and related later literature, no applicable notice
    in the first result sets. Primary page/table evidence establishes F1; later unread
    studies not accepted.
  search_scope: Live web first relevance-ranked results for "10.2138/am-1995-1-203"
    correction erratum retraction and "Crystal chemistry of the monazite and xenotime
    structures" synthetic YPO4. No pagination or exhaustive notice-index claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural species versus synthetic comparator
  outcome: concern
  target_ids:
  - cmmmech:xenotime-y
  evidence_ids:
  - target
  - primary
  - ima
  - dedup
  summary: Y-dominant natural phosphate, tetragonal I4_1/amd and eight-coordinate
    rare-earth site supported; F1 concerns only the claimed synthetic YPO4 arm.
- assessment_id: scope
  area: evidence
  topic: Measured structure and biological boundaries
  outcome: supported
  target_ids:
  - cmmmech:xenotime-y
  evidence_ids:
  - target
  - primary
  - ima
  summary: No microbial mechanism, strain, criticality, grade, recovery denominator
    or industrial deployment asserted. Crystal-structure comparison is not an observed
    transformation experiment. Missing deposited tables are disclosed.
findings:
- finding_id: F1
  issue_key: CMMMech.xenotime-y.synthetic-comparator-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Synthetic YPO4 is incorrectly attributed to the Ni1995 experimental set
  description: Description states that synthetic YPO4 was examined in the same study.
    Methods specify14synthetic phases and Tables1–2 list La–Gd and Tb–Lu phosphates
    (excludingPm), with natural Y-dominant xenotime separate. Table3 compares the
    natural xenotime with syntheticHoPO4. The paper cites earlier syntheticYPO4 work
    but does not identify a measured syntheticYPO4 comparator. Replace with source-supported
    synthetic rare-earth phosphate comparators without changing natural identity.
  target_ids:
  - cmmmech:xenotime-y
  field_paths:
  - description
  evidence_ids:
  - target
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-y.yaml
    role: maintained scientific record
  rule_id: primary-source-specimen-attribution
  native_severity: minor
  normalization_reason: Bounded comparator-identity error; accepted natural species
    identity and structural conclusions remain supported.
actions:
- action_id: A1
  description: Correct the comparator phrase, append actual EDIT history/inline event
    and a source correction note; preserve initial artifacts.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:xenotime-y
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-y.yaml
    role: maintained scientific record
  acceptance_checks:
  - Original Methods/Tables1–3 support corrected phrase without claiming syntheticYPO4
    was tested.
  - Repeat named and affected cohort checks; retain original CREATE and initial review.
  - Save successor with exact F1 occurrence/key, issue link and final hashes.
limitations:
- Initial observation is partial because parent batch checks are pending and F1 is
  unresolved.
- DepositedTables4–5 not inspected; no structure re-refinement or comprehensive literature
  reassessment.
- Searches bounded as stated; no unextracted-binary or global absence claim.
notes:
- No target/Git/GitHub mutations by reviewer; initial finding saved before author
  correction.
tags:
- round50
- xenotime-y
- independent
- initial
```
