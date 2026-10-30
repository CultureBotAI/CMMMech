# Primary-source scientific review of grimmite (IMA:2020-060, status A, NiCo2S4)

- Review: 20261030T134200Z-grimmite-round123-scientific-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T13:40:00Z
- Finished UTC: 2026-10-30T13:42:00Z
- Reviewer: antigravity / round123-scientific-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Grimmite (IMA:2020-060, status A, NiCo2S4) passes primary-source scientific review (scientific_review: true) at SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf against all 39 bounded passages (13 pages) of Škácha et al. (2021, Eur. J. Mineral. 33:175-187).

## Scope And Provenance

Primary-source scientific review of data/records/grimmite.yaml (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf) and its canonical CREATE history sidecar against all 39 bounded primary-source passages (13 pages) from Škácha et al. (2021, Eur. J. Mineral. 33:175-187) and the September 2026 IMA-CNMNC Master List (PDF p. 86).

Selection: Round 123 newly admitted mineral record grimmite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3684ac763165c2343e93af37c9eef7b21608edd5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:grimmite | data/records/grimmite.yaml | maintained | Grimmite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:grimmite | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:grimmite | Checked 1104 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of IMA:2020-060 identity, Příbram Jerusalem deposit shaft no. 9 cotypes P1P 49/2020 and 3/2020 chemistry, and cubic Fd-3m inverse-thiospinel structure for grimmite

evidence: supported. Targets: cmmmech:grimmite.

All numeric, crystallographic, reflectance, and chemical claims in data/records/grimmite.yaml (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf) match the bounded primary-source passages of Škácha et al. (2021, Eur. J. Mineral. 33:175-187, 13 pages, 39 bounded passages) and the September 2026 IMA Master List (p. 86).

### Verification of 0 mechanisms (abiotic hydrothermal occurrence only) and append-only CREATE provenance

provenance: supported. Targets: cmmmech:grimmite.

data/records/grimmite.yaml accurately omits mechanisms (0 mechanisms) because Škácha et al. (2021) reports a natural hydrothermal carbonate-vein mineral description without any microbial extraction, bioleaching, biomineralization, or synthetic recovery experiment, and explicitly discloses that no criticality designation, microbial mechanism, or industrial recovery yield is asserted. Append-only CREATE history sidecar passes validation with 0 errors.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/grimmite.yaml; Working-tree record data/records/grimmite.yaml | supports | Working-tree record data/records/grimmite.yaml (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf) captures the IMA:2020-060 identity, shaft no. 9 Jerusalem deposit (Příbram) cotypes P1P 49/2020 and 3/2020 WDS chemistry (Table 2, p. 177, n = 13 on SCXRD grain), COM reflectance (Table 1, p. 177), cubic Fd-3m inverse-thiospinel Co[NiCo]S4 single-crystal XRD structure on FIB-extracted grain (Tables 4–6), calculated powder XRD (Table 4, p. 179), and 0 mechanisms (no microbial mechanism or industrial recovery yield asserted). |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List, PDF p. 86 | supports | Confirms Grimmite, formula NiCo2S4, status A, IMA No. 2020-060, country Czechia, and sole reference European Journal of Mineralogy 33 (2021), 175. |
| skacha_2021_primary | https://doi.org/10.5194/ejm-33-175-2021; Škácha P, Sejkora J, Plášil J, Dolníček Z, and Ulmanová J (2021) Eur. J. Mineral. 33:175-187, pp. 175-187, Tables 1-6, Figures 1-9 (passages/ejm-33-175-2021.p1..p13.all-pages.w1.part*.txt; 39 passages) | supports | All 13 pages (39 bounded passages &lt;= 1,800 B in summary.json) inspected: confirms shaft no. 9, Jerusalem deposit, Příbram polymetallic ore district, central Bohemia, Czech Republic, two cotype specimens P1P 49/2020 (National Museum, Prague) and 3/2020 (Mining Museum Příbram), siderite–sphalerite gangue hosting skutterudite-subgroup minerals, nickeline, gersdorffite, glaucodot, arsenopyrite, quartz, pyrite, sphalerite II, galena, Bi-rich ullmannite, bismuthinite, parkerite, and jaipurite, Table 2 (p. 177) WDS chemistry on the SCXRD grain (n = 13: Ni 19.27, Co 38.23, Fe 1.16, Bi 0.62, Pb 0.46, As 0.09, Cu 0.08, Mn 0.03, S 41.05, total 100.99 wt%), empirical formula Ni1.01(Co1.99Fe0.06Pb0.01Bi0.01)Sigma2.07S3.92, COM reflectance in air (42.5% at 470 nm, 45.9% at 546 nm, 47.7% at 589 nm, 50.2% at 650 nm; Table 1, p. 177), cubic Fd-3m SCXRD refinement on a 0.028 x 0.009 x 0.007 mm FIB-SEM extracted fragment (a = 9.3933(9) Å, V = 828.81(14) Å3, Z = 8, Dcalc = 4.96 g/cm3 [empirical] / 4.89 g/cm3 [ideal] / 4.843 g/cm3 [structural formula], Robs = 0.0539 in Table 5 vs 0.0489 in abstract, Tables 4–6), and 7 strongest calculated powder XRD lines at 3.3210 (74.7)(220), 2.7116 (7.2)(222), 2.3483 (80.7)(400), 1.9174 (26.7)(422), 1.6605 (100.0)(440), 1.4852 (10.6)(620), and 1.3558 (15.1)(444) Å (Table 4, p. 179). |
| create_history | history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml; Canonical CREATE history sidecar history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml | supports | Canonical CREATE history sidecar (SHA-256 fe0c1c6544457737e240ecb3bf2c29031b213a9f1c55822bbca74fb31eec627f) preserved untouched as immutable per AGENTS.md; note that its details string cited a preliminary estimate of 40 passages whereas summary.json indexes 39 bounded passages across the 13 pages of ejm-33-175-2021.pdf. |
| validation | data/records/grimmite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | Checked 668 record(s); 0 failed. Checked 1104 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed under the Round 123 bounded source-text workflow (scripts/index_bounded_pdf_passages.py, max 1,800 bytes per passage) and synchronized in response to PR #868 review issue #869.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T134200Z-grimmite-round123-scientific-review
kind: record
repository: CultureBotAI/CMMMech
title: Primary-source scientific review of grimmite (IMA:2020-060, status A, NiCo2S4)
started_at: '2026-10-30T13:40:00Z'
finished_at: '2026-10-30T13:42:00Z'
reviewer:
  identity: antigravity / round123-scientific-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying all scientific claims in data/records/grimmite.yaml (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf)
    against all 39 bounded passages (13 pages) of Škácha P, Sejkora J, Plášil J, Dolníček
    Z, and Ulmanová J (2021, Eur. J. Mineral. 33:175-187, passages/ejm-33-175-2021.p1..p13.all-pages.w1.part*.txt)
    and the September 2026 IMA-CNMNC Master List (PDF p. 86).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3684ac763165c2343e93af37c9eef7b21608edd5
  state: working_tree
  inputs:
  - path: data/records/grimmite.yaml
    sha256: d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf
    role: target
  - path: history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml
    sha256: fe0c1c6544457737e240ecb3bf2c29031b213a9f1c55822bbca74fb31eec627f
    role: context
  - path: research/sources/round123-minerals/20261030T133900Z-source-investigation.json
    sha256: e2c2ef23db32c9385e91e0ba41d24e59f465362d9499231aa45d94f996e8edb2
    role: context
  - path: research/sources/round123-minerals/20261030T133900Z-source-investigation.md
    sha256: 82628141d7f25fa1b66dfc94beaebca00f1ba9c5c408a8571358d5602aba94aa
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:grimmite
  path: data/records/grimmite.yaml
  label: Grimmite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/grimmite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml
    role: canonical_history
scope:
  description: Primary-source scientific review of data/records/grimmite.yaml (SHA-256
    d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf) and its canonical
    CREATE history sidecar against all 39 bounded primary-source passages (13 pages)
    from Škácha et al. (2021, Eur. J. Mineral. 33:175-187) and the September 2026
    IMA-CNMNC Master List (PDF p. 86).
  selection: Round 123 newly admitted mineral record grimmite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:grimmite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/grimmite.yaml
  locator: Working-tree record data/records/grimmite.yaml
  accessed_at: '2026-10-30T13:41:00Z'
  support: supports
  summary: Working-tree record data/records/grimmite.yaml (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf)
    captures the IMA:2020-060 identity, shaft no. 9 Jerusalem deposit (Příbram) cotypes
    P1P 49/2020 and 3/2020 WDS chemistry (Table 2, p. 177, n = 13 on SCXRD grain),
    COM reflectance (Table 1, p. 177), cubic Fd-3m inverse-thiospinel Co[NiCo]S4 single-crystal
    XRD structure on FIB-extracted grain (Tables 4–6), calculated powder XRD (Table
    4, p. 179), and 0 mechanisms (no microbial mechanism or industrial recovery yield
    asserted).
  snapshot_sha256: d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List, PDF p. 86
  accessed_at: '2026-10-30T13:41:00Z'
  support: supports
  summary: Confirms Grimmite, formula NiCo2S4, status A, IMA No. 2020-060, country
    Czechia, and sole reference European Journal of Mineralogy 33 (2021), 175.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: skacha_2021_primary
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-33-175-2021
  locator: Škácha P, Sejkora J, Plášil J, Dolníček Z, and Ulmanová J (2021) Eur. J.
    Mineral. 33:175-187, pp. 175-187, Tables 1-6, Figures 1-9 (passages/ejm-33-175-2021.p1..p13.all-pages.w1.part*.txt;
    39 passages)
  accessed_at: '2026-10-30T13:41:00Z'
  support: supports
  summary: 'All 13 pages (39 bounded passages <= 1,800 B in summary.json) inspected:
    confirms shaft no. 9, Jerusalem deposit, Příbram polymetallic ore district, central
    Bohemia, Czech Republic, two cotype specimens P1P 49/2020 (National Museum, Prague)
    and 3/2020 (Mining Museum Příbram), siderite–sphalerite gangue hosting skutterudite-subgroup
    minerals, nickeline, gersdorffite, glaucodot, arsenopyrite, quartz, pyrite, sphalerite
    II, galena, Bi-rich ullmannite, bismuthinite, parkerite, and jaipurite, Table
    2 (p. 177) WDS chemistry on the SCXRD grain (n = 13: Ni 19.27, Co 38.23, Fe 1.16,
    Bi 0.62, Pb 0.46, As 0.09, Cu 0.08, Mn 0.03, S 41.05, total 100.99 wt%), empirical
    formula Ni1.01(Co1.99Fe0.06Pb0.01Bi0.01)Sigma2.07S3.92, COM reflectance in air
    (42.5% at 470 nm, 45.9% at 546 nm, 47.7% at 589 nm, 50.2% at 650 nm; Table 1,
    p. 177), cubic Fd-3m SCXRD refinement on a 0.028 x 0.009 x 0.007 mm FIB-SEM extracted
    fragment (a = 9.3933(9) Å, V = 828.81(14) Å3, Z = 8, Dcalc = 4.96 g/cm3 [empirical]
    / 4.89 g/cm3 [ideal] / 4.843 g/cm3 [structural formula], Robs = 0.0539 in Table
    5 vs 0.0489 in abstract, Tables 4–6), and 7 strongest calculated powder XRD lines
    at 3.3210 (74.7)(220), 2.7116 (7.2)(222), 2.3483 (80.7)(400), 1.9174 (26.7)(422),
    1.6605 (100.0)(440), 1.4852 (10.6)(620), and 1.3558 (15.1)(444) Å (Table 4, p.
    179).'
  snapshot_sha256: a972dd34d42f93acc53cd3c99b31923398278bf0f47141a4d9d354096429cf11
- evidence_id: create_history
  kind: record_content
  reference: history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml
  locator: Canonical CREATE history sidecar history/records/grimmite/2026-10-30T132620Z-antigravity-76b8bf.yaml
  accessed_at: '2026-10-30T13:41:00Z'
  support: supports
  summary: Canonical CREATE history sidecar (SHA-256 fe0c1c6544457737e240ecb3bf2c29031b213a9f1c55822bbca74fb31eec627f)
    preserved untouched as immutable per AGENTS.md; note that its details string cited
    a preliminary estimate of 40 passages whereas summary.json indexes 39 bounded
    passages across the 13 pages of ejm-33-175-2021.pdf.
  snapshot_sha256: fe0c1c6544457737e240ecb3bf2c29031b213a9f1c55822bbca74fb31eec627f
- evidence_id: validation
  kind: validation
  reference: data/records/grimmite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T13:41:00Z'
  support: supports
  summary: Checked 668 record(s); 0 failed. Checked 1104 history record(s); 0 error(s).
  snapshot_sha256: d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:grimmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1104 history record(s); 0 error(s).
  target_ids:
  - cmmmech:grimmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_primary_source_verification
  area: evidence
  topic: Verification of IMA:2020-060 identity, Příbram Jerusalem deposit shaft no.
    9 cotypes P1P 49/2020 and 3/2020 chemistry, and cubic Fd-3m inverse-thiospinel
    structure for grimmite
  outcome: supported
  summary: All numeric, crystallographic, reflectance, and chemical claims in data/records/grimmite.yaml
    (SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf) match
    the bounded primary-source passages of Škácha et al. (2021, Eur. J. Mineral. 33:175-187,
    13 pages, 39 bounded passages) and the September 2026 IMA Master List (p. 86).
  target_ids:
  - cmmmech:grimmite
  evidence_ids:
  - owner
  - ima_authority
  - skacha_2021_primary
- assessment_id: mechanism_absence_and_provenance_verification
  area: provenance
  topic: Verification of 0 mechanisms (abiotic hydrothermal occurrence only) and append-only
    CREATE provenance
  outcome: supported
  summary: data/records/grimmite.yaml accurately omits mechanisms (0 mechanisms) because
    Škácha et al. (2021) reports a natural hydrothermal carbonate-vein mineral description
    without any microbial extraction, bioleaching, biomineralization, or synthetic
    recovery experiment, and explicitly discloses that no criticality designation,
    microbial mechanism, or industrial recovery yield is asserted. Append-only CREATE
    history sidecar passes validation with 0 errors.
  target_ids:
  - cmmmech:grimmite
  evidence_ids:
  - owner
  - skacha_2021_primary
  - create_history
  - validation
findings: []
actions: []
summary: 'Grimmite (IMA:2020-060, status A, NiCo2S4) passes primary-source scientific
  review (scientific_review: true) at SHA-256 d4fe726dedc99105182e1d2d95e0a98e387cee8abb7b0bdeb6f5aee162c2cadf
  against all 39 bounded passages (13 pages) of Škácha et al. (2021, Eur. J. Mineral.
  33:175-187).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed under the Round 123 bounded source-text workflow (scripts/index_bounded_pdf_passages.py,
  max 1,800 bytes per passage) and synchronized in response to PR #868 review issue
  #869.'
related_reviews: []
```
