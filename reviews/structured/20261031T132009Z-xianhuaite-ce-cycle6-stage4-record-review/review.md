# Cycle 6 Stage 4 record review: cmmmech:xianhuaite-ce (Xianhuaite-(Ce))

- Review: 20261031T132009Z-xianhuaite-ce-cycle6-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T13:15:00Z
- Finished UTC: 2026-10-31T13:20:09Z
- Reviewer: antigravity / cmmmech-cycle6-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/xianhuaite-ce.yaml (cmmmech:xianhuaite-ce) at commit fab0682688678750d7da4e5357dda11592d5fac3 following Cycle 6 Stage 1 curation. Verified IMA-CNMNC September 2026 species identity (IMA 2024-091, symbol Xhu-Ce, ideal formula K2CeNb5O15, tetragonal tungsten bronze group, Bayan Obo Fe-Nb-REE deposit type locality) against IMA-CNMNC September 2026 PDF p. 236 and Yang et al. (2026, Eur. J. Mineral. 38:449-459, DOI:10.5194/ejm-38-449-2026). Identified 1 minor completeness finding (cmmmech-cycle6-stage4-finding-0003: description states IMA symbol Xhu-Ce, but top-level ima_symbol: Xhu-Ce slot is omitted) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 6 Stage 4 audit of cmmmech:xianhuaite-ce after Cycle 6 Stage 1 curation.

Selection: data/records/xianhuaite-ce.yaml at fab0682688678750d7da4e5357dda11592d5fac3
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base fab0682688678750d7da4e5357dda11592d5fac3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:xianhuaite-ce | data/records/xianhuaite-ce.yaml | maintained | Xianhuaite-(Ce) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate xianhuaite-ce.yaml | passed | True | cmmmech:xianhuaite-ce | data/records/xianhuaite-ce.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### IMA 2024-091 xianhuaite-(Ce) identity, formula, type locality, and ima_symbol slot completeness

completeness: supported. Targets: cmmmech:xianhuaite-ce.

Xianhuaite-(Ce) formula (K2CeNb5O15), IMA 2024-091 approval, Bayan Obo type locality, and empirical composition are accurately curated from Yang et al. (2026, Eur. J. Mineral. 38:449-459) and IMA-CNMNC September 2026 PDF p. 236, but top-level ima_symbol: Xhu-Ce is omitted despite being stated in description.

## Findings

### cmmmech-cycle6-stage4-finding-0003: vielleaureite-ce.yaml and xianhuaite-ce.yaml state IMA-approved mineral symbols (Vlr-Ce, Xhu-Ce) in description but omit the top-level ima_symbol slot

minor / open / confirmed; issue key: cmmmech.round124-minerals.missing-ima-symbol-slot.

Both data/records/vielleaureite-ce.yaml (cmmmech:vielleaureite-ce) and data/records/xianhuaite-ce.yaml (cmmmech:xianhuaite-ce), curated in Cycle 6 Stage 1 (PR #884), state their IMA-CNMNC-approved mineral symbols in description ('Vielleaureite-(Ce) (IMA 2022-134, symbol Vlr-Ce; ...)' from Ragu et al. 2025 Eur. J. Mineral. 37:627-638, p. 627 and IMA-CNMNC September 2026 PDF p. 228; and 'Xianhuaite-(Ce) (IMA 2024-091, symbol Xhu-Ce)' from Yang et al. 2026 Eur. J. Mineral. 38:449-459, p. 449 and IMA-CNMNC September 2026 PDF p. 236), but omit the top-level ima_symbol slot (ima_symbol: Vlr-Ce and ima_symbol: Xhu-Ce after material_kind: mineral), unlike peer IMA mineral records such as data/records/andreybulakhite.yaml (ima_symbol: Adb) and data/records/yttrotungstite-nd.yaml (ima_symbol: Ytgs-Nd). In this scope, 1 record(s) (xianhuaite-ce) omit ima_symbol.

## Recommended Actions And Acceptance Checks

### act-populate-ima-symbol-on-vielleaureite-ce-and-xianhuaite-ce

Add top-level ima_symbol: Vlr-Ce to data/records/vielleaureite-ce.yaml and top-level ima_symbol: Xhu-Ce to data/records/xianhuaite-ce.yaml in canonical key order (immediately following material_kind: mineral) during Stage 5 grouped remediation with canonical history provenance.

- data/records/vielleaureite-ce.yaml has ima_symbol: Vlr-Ce and data/records/xianhuaite-ce.yaml has ima_symbol: Xhu-Ce in CANONICAL_RECORD_KEYS order.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-xianhuaite-ce-file | data/records/xianhuaite-ce.yaml; lines 1-123 | supports | Inspected all 123 lines of data/records/xianhuaite-ce.yaml, verifying description ('Xianhuaite-(Ce) (IMA 2024-091, symbol Xhu-Ce)') and absence of top-level ima_symbol. |
| ev-yang2026-xianhuaite-ce-rec | DOI:10.5194/ejm-38-449-2026; Yang et al. 2026 Eur. J. Mineral. 38:449-459, p. 449 (abstract); IMA-CNMNC September 2026 PDF p. 236 | supports | Yang et al. (2026) and IMA-CNMNC September 2026 (PDF p. 236) report IMA 2024-091 approval and symbol Xhu-Ce for xianhuaite-(Ce). |

## Limits And Additional Notes

- data/records/xianhuaite-ce.yaml states IMA symbol Xhu-Ce in description but omits top-level ima_symbol: Xhu-Ce (tracked as open finding cmmmech-cycle6-stage4-finding-0003 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T132009Z-xianhuaite-ce-cycle6-stage4-record-review
title: 'Cycle 6 Stage 4 record review: cmmmech:xianhuaite-ce (Xianhuaite-(Ce))'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-31T13:15:00Z'
finished_at: '2026-10-31T13:20:09Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/xianhuaite-ce.yaml (cmmmech:xianhuaite-ce) at commit
  fab0682688678750d7da4e5357dda11592d5fac3 following Cycle 6 Stage 1 curation. Verified
  IMA-CNMNC September 2026 species identity (IMA 2024-091, symbol Xhu-Ce, ideal formula
  K2CeNb5O15, tetragonal tungsten bronze group, Bayan Obo Fe-Nb-REE deposit type locality)
  against IMA-CNMNC September 2026 PDF p. 236 and Yang et al. (2026, Eur. J. Mineral.
  38:449-459, DOI:10.5194/ejm-38-449-2026). Identified 1 minor completeness finding
  (cmmmech-cycle6-stage4-finding-0003: description states IMA symbol Xhu-Ce, but top-level
  ima_symbol: Xhu-Ce slot is omitted) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 6 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit fab0682688678750d7da4e5357dda11592d5fac3.
source:
  git_revision: fab0682688678750d7da4e5357dda11592d5fac3
  state: git_commit
  inputs:
  - path: data/records/xianhuaite-ce.yaml
    sha256: 6c10184ccc5d687d3a4ca89b77766c5e5311b50e4696064b8d20626d7d301ec8
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:xianhuaite-ce
  selection: data/records/xianhuaite-ce.yaml at fab0682688678750d7da4e5357dda11592d5fac3
  description: Single-record Cycle 6 Stage 4 audit of cmmmech:xianhuaite-ce after
    Cycle 6 Stage 1 curation.
targets:
- target_id: cmmmech:xianhuaite-ce
  path: data/records/xianhuaite-ce.yaml
  kind: maintained
  label: Xianhuaite-(Ce)
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xianhuaite-ce.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-xianhuaite-ce
  name: cmmmech validate xianhuaite-ce.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/xianhuaite-ce.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xianhuaite-ce
  evidence_ids:
  - ev-xianhuaite-ce-file
  summary: data/records/xianhuaite-ce.yaml passes LinkML structural, semantic, and
    canonical top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-xianhuaite-ce-ima-identity-and-completeness
  topic: IMA 2024-091 xianhuaite-(Ce) identity, formula, type locality, and ima_symbol
    slot completeness
  area: completeness
  outcome: supported
  target_ids:
  - cmmmech:xianhuaite-ce
  evidence_ids:
  - ev-xianhuaite-ce-file
  - ev-yang2026-xianhuaite-ce-rec
  summary: 'Xianhuaite-(Ce) formula (K2CeNb5O15), IMA 2024-091 approval, Bayan Obo
    type locality, and empirical composition are accurately curated from Yang et al.
    (2026, Eur. J. Mineral. 38:449-459) and IMA-CNMNC September 2026 PDF p. 236, but
    top-level ima_symbol: Xhu-Ce is omitted despite being stated in description.'
findings:
- finding_id: cmmmech-cycle6-stage4-finding-0003
  issue_key: cmmmech.round124-minerals.missing-ima-symbol-slot
  title: vielleaureite-ce.yaml and xianhuaite-ce.yaml state IMA-approved mineral symbols
    (Vlr-Ce, Xhu-Ce) in description but omit the top-level ima_symbol slot
  severity: minor
  category: completeness
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:xianhuaite-ce
  field_paths:
  - ima_symbol
  - description
  evidence_ids:
  - ev-xianhuaite-ce-file
  - ev-yang2026-xianhuaite-ce-rec
  description: 'Both data/records/vielleaureite-ce.yaml (cmmmech:vielleaureite-ce)
    and data/records/xianhuaite-ce.yaml (cmmmech:xianhuaite-ce), curated in Cycle
    6 Stage 1 (PR #884), state their IMA-CNMNC-approved mineral symbols in description
    (''Vielleaureite-(Ce) (IMA 2022-134, symbol Vlr-Ce; ...)'' from Ragu et al. 2025
    Eur. J. Mineral. 37:627-638, p. 627 and IMA-CNMNC September 2026 PDF p. 228; and
    ''Xianhuaite-(Ce) (IMA 2024-091, symbol Xhu-Ce)'' from Yang et al. 2026 Eur. J.
    Mineral. 38:449-459, p. 449 and IMA-CNMNC September 2026 PDF p. 236), but omit
    the top-level ima_symbol slot (ima_symbol: Vlr-Ce and ima_symbol: Xhu-Ce after
    material_kind: mineral), unlike peer IMA mineral records such as data/records/andreybulakhite.yaml
    (ima_symbol: Adb) and data/records/yttrotungstite-nd.yaml (ima_symbol: Ytgs-Nd).
    In this scope, 1 record(s) (xianhuaite-ce) omit ima_symbol.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xianhuaite-ce.yaml
    role: maintained_record
actions:
- action_id: act-populate-ima-symbol-on-vielleaureite-ce-and-xianhuaite-ce
  finding_ids:
  - cmmmech-cycle6-stage4-finding-0003
  target_ids:
  - cmmmech:xianhuaite-ce
  description: 'Add top-level ima_symbol: Vlr-Ce to data/records/vielleaureite-ce.yaml
    and top-level ima_symbol: Xhu-Ce to data/records/xianhuaite-ce.yaml in canonical
    key order (immediately following material_kind: mineral) during Stage 5 grouped
    remediation with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xianhuaite-ce.yaml
    role: maintained_record
  acceptance_checks:
  - 'data/records/vielleaureite-ce.yaml has ima_symbol: Vlr-Ce and data/records/xianhuaite-ce.yaml
    has ima_symbol: Xhu-Ce in CANONICAL_RECORD_KEYS order.'
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-xianhuaite-ce-file
  kind: record_content
  reference: data/records/xianhuaite-ce.yaml
  locator: lines 1-123
  accessed_at: '2026-10-31T13:20:09Z'
  support: supports
  summary: Inspected all 123 lines of data/records/xianhuaite-ce.yaml, verifying description
    ('Xianhuaite-(Ce) (IMA 2024-091, symbol Xhu-Ce)') and absence of top-level ima_symbol.
- evidence_id: ev-yang2026-xianhuaite-ce-rec
  kind: primary_source
  reference: DOI:10.5194/ejm-38-449-2026
  locator: Yang et al. 2026 Eur. J. Mineral. 38:449-459, p. 449 (abstract); IMA-CNMNC
    September 2026 PDF p. 236
  accessed_at: '2026-10-31T13:20:09Z'
  support: supports
  summary: Yang et al. (2026) and IMA-CNMNC September 2026 (PDF p. 236) report IMA
    2024-091 approval and symbol Xhu-Ce for xianhuaite-(Ce).
limitations:
- 'data/records/xianhuaite-ce.yaml states IMA symbol Xhu-Ce in description but omits
  top-level ima_symbol: Xhu-Ce (tracked as open finding cmmmech-cycle6-stage4-finding-0003
  for Stage 5 remediation).'
notes: []
```
