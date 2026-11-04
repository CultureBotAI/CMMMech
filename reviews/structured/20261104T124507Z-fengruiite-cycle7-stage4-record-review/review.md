# Cycle 7 Stage 4 record review: cmmmech:fengruiite (Fengruiite)

- Review: 20261104T124507Z-fengruiite-cycle7-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T12:35:00Z
- Finished UTC: 2026-11-04T12:45:07Z
- Reviewer: antigravity / cmmmech-cycle7-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Adversarial single-record review of data/records/fengruiite.yaml (cmmmech:fengruiite, added in Cycle 7 Stage 1 PR #910) at commit ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c. Verified IMA-CNMNC mineral identity (IMA:2024-045, symbol Fru; silver-copper-antimony-tellurium sulfosalt of the pearceite-polybasite group, polybasite-Tac 111 polytype), September 2026 IMA-CNMNC Master List ideal formula [Ag6Sb2S7][Ag9CuS2Te2] (ideal composition Ag 67.20 wt%, S 12.84 wt%, Sb 10.11 wt%, Te 7.21 wt%, Cu 2.64 wt%; empirical WDS formula [(Ag5.87Cu0.29)Sigma6.16(Sb1.89As0.03)Sigma1.92S7][Ag9CuS2(Te1.28S0.63)Sigma1.91]), trigonal symmetry (space group P-3m1, #164, a = 7.6087(9) A, c = 11.970(2) A, V = 600.13(17) A3, Z = 1, Dcalc = 6.62 g/cm3), and holotype occurrence (GMCTM2024004 from a galena-quartz vein at 380 m elevation of the H5 polymetallic sulfide orebody, Haopinggou Ag-Pb-Zn-Au deposit, Xiayu orefield, ~60 km SW of Luoning County, Henan Province, eastern Qinling, China) against Tian et al. (2026, Eur. J. Mineral. 38:519-530, DOI:10.5194/ejm-38-519-2026) and the September 2026 IMA-CNMNC List of Mineral Names (PDF p. 71). Confirmed one minor completeness finding (cmmmech-cycle7-stage4-finding-0001: top-level ima_symbol: Fru is omitted despite symbol Fru being explicitly stated in description) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 7 Stage 4 audit of cmmmech:fengruiite after Cycle 7 Stage 1 curation.

Selection: data/records/fengruiite.yaml at ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:fengruiite | data/records/fengruiite.yaml | maintained | Fengruiite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate fengruiite.yaml | passed | True | cmmmech:fengruiite | data/records/fengruiite.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### IMA 2024-045 fengruiite identity, formula, type locality, and ima_symbol slot completeness

completeness: supported. Targets: cmmmech:fengruiite.

Identity, ideal and empirical formulas ([Ag6Sb2S7][Ag9CuS2Te2]; [(Ag5.87Cu0.29)Sigma6.16(Sb1.89As0.03)Sigma1.92S7][Ag9CuS2(Te1.28S0.63)Sigma1.91]), trigonal P-3m1 unit-cell parameters, holotype repository (GMCTM2024004, Geological Museum of China), and Haopinggou Ag-Pb-Zn-Au deposit type-locality metadata match Tian et al. (2026, DOI:10.5194/ejm-38-519-2026) and the September 2026 IMA-CNMNC Master List (p. 71); top-level ima_symbol: Fru slot is omitted.

## Findings

### cmmmech-cycle7-stage4-finding-0001: Four Cycle 7 Stage 1 (Round 125) IMA mineral records state IMA-approved symbols (Fru, Ig, Lzc, Pgtb) in description but omit the top-level ima_symbol slot

minor / open / confirmed; issue key: cmmmech.round125-minerals.missing-ima-symbol-slot.

Four of the five IMA-CNMNC Round 125 mineral records curated in Cycle 7 Stage 1 (PR #910, commit fa7431ae) — data/records/fengruiite.yaml (cmmmech:fengruiite, IMA 2024-045), data/records/igelstromite.yaml (cmmmech:igelstromite, IMA 2021-035), data/records/lazerckerite.yaml (cmmmech:lazerckerite, IMA 2022-113), and data/records/plumbogottlobite.yaml (cmmmech:plumbogottlobite, IMA 2025-075) — explicitly state their IMA-CNMNC-approved mineral symbols in description ('IMA symbol Fru' in fengruiite.yaml line 8 from Tian et al. 2026 Eur. J. Mineral. 38:519-530, p. 519; 'IMA symbol Ig' in igelstromite.yaml line 9 from Holtstam et al. 2024 Eur. J. Mineral. 36:311-322, p. 311; 'official IMA symbol Lzc' in lazerckerite.yaml lines 11-12 from Pazout et al. 2024 Eur. J. Mineral. 36:641-656, p. 641; and 'official IMA symbol Pgtb' in plumbogottlobite.yaml line 8 from Kampf et al. 2026 Eur. J. Mineral. 38:209-216, p. 209), but omit the top-level ima_symbol slot (ima_symbol: Fru, ima_symbol: Ig, ima_symbol: Lzc, and ima_symbol: Pgtb immediately following material_kind: mineral), unlike peer IMA mineral records such as data/records/andreybulakhite.yaml (ima_symbol: Adb), data/records/vielleaureite-ce.yaml (ima_symbol: Vlr-Ce), data/records/xianhuaite-ce.yaml (ima_symbol: Xhu-Ce), and data/records/yttrotungstite-nd.yaml (ima_symbol: Ytgs-Nd). In this scope, 1 record(s) (fengruiite) omit ima_symbol.

## Recommended Actions And Acceptance Checks

### act-populate-ima-symbol-on-round125-minerals

Add top-level ima_symbol: Fru (fengruiite.yaml), ima_symbol: Ig (igelstromite.yaml), ima_symbol: Lzc (lazerckerite.yaml), and ima_symbol: Pgtb (plumbogottlobite.yaml) in canonical key order (immediately following material_kind: mineral) during Stage 5 grouped remediation with canonical history provenance.

- fengruiite.yaml, igelstromite.yaml, lazerckerite.yaml, and plumbogottlobite.yaml carry top-level ima_symbol in CANONICAL_RECORD_KEYS order.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fengruiite-file | data/records/fengruiite.yaml; lines 1-116 | supports | Inspected all 116 lines of data/records/fengruiite.yaml, verifying description ('IMA 2024-045, IMA symbol Fru') and absence of top-level ima_symbol. |
| ev-tian2026-fengruiite | DOI:10.5194/ejm-38-519-2026; Tian et al. 2026 Eur. J. Mineral. 38:519-530, p. 519 (abstract) | supports | Tian et al. (2026) report IMA 2024-045 approval and symbol Fru for fengruiite. |

## Limits And Additional Notes

- data/records/fengruiite.yaml states IMA symbol Fru in description but omits top-level ima_symbol: Fru (tracked as open finding cmmmech-cycle7-stage4-finding-0001 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T124507Z-fengruiite-cycle7-stage4-record-review
title: 'Cycle 7 Stage 4 record review: cmmmech:fengruiite (Fengruiite)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-11-04T12:35:00Z'
finished_at: '2026-11-04T12:45:07Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Adversarial single-record review of data/records/fengruiite.yaml (cmmmech:fengruiite,
  added in Cycle 7 Stage 1 PR #910) at commit ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c.
  Verified IMA-CNMNC mineral identity (IMA:2024-045, symbol Fru; silver-copper-antimony-tellurium
  sulfosalt of the pearceite-polybasite group, polybasite-Tac 111 polytype), September
  2026 IMA-CNMNC Master List ideal formula [Ag6Sb2S7][Ag9CuS2Te2] (ideal composition
  Ag 67.20 wt%, S 12.84 wt%, Sb 10.11 wt%, Te 7.21 wt%, Cu 2.64 wt%; empirical WDS
  formula [(Ag5.87Cu0.29)Sigma6.16(Sb1.89As0.03)Sigma1.92S7][Ag9CuS2(Te1.28S0.63)Sigma1.91]),
  trigonal symmetry (space group P-3m1, #164, a = 7.6087(9) A, c = 11.970(2) A, V
  = 600.13(17) A3, Z = 1, Dcalc = 6.62 g/cm3), and holotype occurrence (GMCTM2024004
  from a galena-quartz vein at 380 m elevation of the H5 polymetallic sulfide orebody,
  Haopinggou Ag-Pb-Zn-Au deposit, Xiayu orefield, ~60 km SW of Luoning County, Henan
  Province, eastern Qinling, China) against Tian et al. (2026, Eur. J. Mineral. 38:519-530,
  DOI:10.5194/ejm-38-519-2026) and the September 2026 IMA-CNMNC List of Mineral Names
  (PDF p. 71). Confirmed one minor completeness finding (cmmmech-cycle7-stage4-finding-0001:
  top-level ima_symbol: Fru is omitted despite symbol Fru being explicitly stated
  in description) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle7-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 7 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c.
source:
  git_revision: ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c
  state: git_commit
  inputs:
  - path: data/records/fengruiite.yaml
    sha256: 515efee2f6e88c788af7b97b3b403223291d5a80261d337ae4dcf0c33d427d9e
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
  - cmmmech:fengruiite
  selection: data/records/fengruiite.yaml at ff4a9841deb7e4f6e9fff025eccd2ffa07b5493c
  description: Single-record Cycle 7 Stage 4 audit of cmmmech:fengruiite after Cycle
    7 Stage 1 curation.
targets:
- target_id: cmmmech:fengruiite
  path: data/records/fengruiite.yaml
  kind: maintained
  label: Fengruiite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fengruiite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-fengruiite
  name: cmmmech validate fengruiite.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/fengruiite.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:fengruiite
  evidence_ids:
  - ev-fengruiite-file
  summary: data/records/fengruiite.yaml passes LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-fengruiite-ima-identity-and-completeness
  topic: IMA 2024-045 fengruiite identity, formula, type locality, and ima_symbol
    slot completeness
  area: completeness
  outcome: supported
  target_ids:
  - cmmmech:fengruiite
  evidence_ids:
  - ev-fengruiite-file
  - ev-tian2026-fengruiite
  summary: 'Identity, ideal and empirical formulas ([Ag6Sb2S7][Ag9CuS2Te2]; [(Ag5.87Cu0.29)Sigma6.16(Sb1.89As0.03)Sigma1.92S7][Ag9CuS2(Te1.28S0.63)Sigma1.91]),
    trigonal P-3m1 unit-cell parameters, holotype repository (GMCTM2024004, Geological
    Museum of China), and Haopinggou Ag-Pb-Zn-Au deposit type-locality metadata match
    Tian et al. (2026, DOI:10.5194/ejm-38-519-2026) and the September 2026 IMA-CNMNC
    Master List (p. 71); top-level ima_symbol: Fru slot is omitted.'
findings:
- finding_id: cmmmech-cycle7-stage4-finding-0001
  issue_key: cmmmech.round125-minerals.missing-ima-symbol-slot
  title: Four Cycle 7 Stage 1 (Round 125) IMA mineral records state IMA-approved symbols
    (Fru, Ig, Lzc, Pgtb) in description but omit the top-level ima_symbol slot
  severity: minor
  category: completeness
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:fengruiite
  field_paths:
  - ima_symbol
  - description
  evidence_ids:
  - ev-fengruiite-file
  - ev-tian2026-fengruiite
  description: 'Four of the five IMA-CNMNC Round 125 mineral records curated in Cycle
    7 Stage 1 (PR #910, commit fa7431ae) — data/records/fengruiite.yaml (cmmmech:fengruiite,
    IMA 2024-045), data/records/igelstromite.yaml (cmmmech:igelstromite, IMA 2021-035),
    data/records/lazerckerite.yaml (cmmmech:lazerckerite, IMA 2022-113), and data/records/plumbogottlobite.yaml
    (cmmmech:plumbogottlobite, IMA 2025-075) — explicitly state their IMA-CNMNC-approved
    mineral symbols in description (''IMA symbol Fru'' in fengruiite.yaml line 8 from
    Tian et al. 2026 Eur. J. Mineral. 38:519-530, p. 519; ''IMA symbol Ig'' in igelstromite.yaml
    line 9 from Holtstam et al. 2024 Eur. J. Mineral. 36:311-322, p. 311; ''official
    IMA symbol Lzc'' in lazerckerite.yaml lines 11-12 from Pazout et al. 2024 Eur.
    J. Mineral. 36:641-656, p. 641; and ''official IMA symbol Pgtb'' in plumbogottlobite.yaml
    line 8 from Kampf et al. 2026 Eur. J. Mineral. 38:209-216, p. 209), but omit the
    top-level ima_symbol slot (ima_symbol: Fru, ima_symbol: Ig, ima_symbol: Lzc, and
    ima_symbol: Pgtb immediately following material_kind: mineral), unlike peer IMA
    mineral records such as data/records/andreybulakhite.yaml (ima_symbol: Adb), data/records/vielleaureite-ce.yaml
    (ima_symbol: Vlr-Ce), data/records/xianhuaite-ce.yaml (ima_symbol: Xhu-Ce), and
    data/records/yttrotungstite-nd.yaml (ima_symbol: Ytgs-Nd). In this scope, 1 record(s)
    (fengruiite) omit ima_symbol.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fengruiite.yaml
    role: maintained_record
actions:
- action_id: act-populate-ima-symbol-on-round125-minerals
  finding_ids:
  - cmmmech-cycle7-stage4-finding-0001
  target_ids:
  - cmmmech:fengruiite
  description: 'Add top-level ima_symbol: Fru (fengruiite.yaml), ima_symbol: Ig (igelstromite.yaml),
    ima_symbol: Lzc (lazerckerite.yaml), and ima_symbol: Pgtb (plumbogottlobite.yaml)
    in canonical key order (immediately following material_kind: mineral) during Stage
    5 grouped remediation with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fengruiite.yaml
    role: maintained_record
  acceptance_checks:
  - fengruiite.yaml, igelstromite.yaml, lazerckerite.yaml, and plumbogottlobite.yaml
    carry top-level ima_symbol in CANONICAL_RECORD_KEYS order.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-fengruiite-file
  kind: record_content
  reference: data/records/fengruiite.yaml
  locator: lines 1-116
  accessed_at: '2026-11-04T12:45:07Z'
  support: supports
  summary: Inspected all 116 lines of data/records/fengruiite.yaml, verifying description
    ('IMA 2024-045, IMA symbol Fru') and absence of top-level ima_symbol.
- evidence_id: ev-tian2026-fengruiite
  kind: primary_source
  reference: DOI:10.5194/ejm-38-519-2026
  locator: Tian et al. 2026 Eur. J. Mineral. 38:519-530, p. 519 (abstract)
  accessed_at: '2026-11-04T12:45:07Z'
  support: supports
  summary: Tian et al. (2026) report IMA 2024-045 approval and symbol Fru for fengruiite.
limitations:
- 'data/records/fengruiite.yaml states IMA symbol Fru in description but omits top-level
  ima_symbol: Fru (tracked as open finding cmmmech-cycle7-stage4-finding-0001 for
  Stage 5 remediation).'
notes: []
```
