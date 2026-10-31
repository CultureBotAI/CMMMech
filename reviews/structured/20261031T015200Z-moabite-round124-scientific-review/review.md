# Primary-source scientific review of moabite (IMA:2020-092, status A, NiFe3+(PO4)O)

- Review: 20261031T015200Z-moabite-round124-scientific-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T01:50:50Z
- Finished UTC: 2026-10-31T01:52:00Z
- Reviewer: antigravity / round124-scientific-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Moabite (IMA:2020-092, status A, NiFe3+(PO4)O) passes primary-source scientific review (scientific_review: true) at SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410 against all 32 bounded passages (11 pages) and rendered table PNGs of Britvin et al. (2025, Eur. J. Mineral. 37:353-363).

## Scope And Provenance

Primary-source scientific review of data/records/moabite.yaml (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410) and its canonical CREATE history sidecar against all 32 bounded primary-source passages (11 pages) and rendered PNGs of pages 4 and 6 from Britvin et al. (2025, Eur. J. Mineral. 37:353-363) and the September 2026 IMA-CNMNC Master List (PDF p. 145).

Selection: Round 124 newly admitted mineral record moabite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e954c96898ce97da6781984c7da7ea5d4fda9bfa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:moabite | data/records/moabite.yaml | maintained | Moabite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:moabite | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:moabite | Checked 1162 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of IMA:2020-092 identity, Jordan pyrometamorphic type locality, EPMA chemistry, trigonal R-3 structure, and internal source notes for moabite

evidence: supported. Targets: cmmmech:moabite.

All numeric, crystallographic, Raman, optical, and chemical claims in data/records/moabite.yaml (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410) match the bounded primary-source passages and rendered table PNGs of Britvin et al. (2025, Eur. J. Mineral. 37:353-363) and the September 2026 IMA Master List (p. 145).

### Verification of 0 mechanisms (abiotic occurrence only) and append-only CREATE provenance

provenance: supported. Targets: cmmmech:moabite.

data/records/moabite.yaml accurately omits mechanisms (0 mechanisms) and explicitly discloses that no criticality designation, microbial mechanism, or industrial recovery yield is asserted. Append-only CREATE history sidecar passes validation with 0 errors.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/moabite.yaml; Working-tree record data/records/moabite.yaml | supports | Working-tree record data/records/moabite.yaml (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410) captures IMA:2020-092 identity, Daba-Siwaqa pyrometamorphic complex (Hatrurim Basin, Jordan) type locality, holotype repository FMM No. 5567/1, Table 3 (p. 356) 9-point EPMA chemistry, trigonal R-3 tavorite-group-related structure (Tables 4-8), Raman spectrum, physical/optical properties, internal primary-source notes (Abstract Dcalc = 4.324 g/cm3 and comma decimal separator 3,321(37)(102) vs Table 5 Dx = 4.338 g/cm3 and Table 4 3.321 (37) (102)), and 0 mechanisms. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List, PDF p. 145 | supports | Confirms Moabite, formula NiFe3+(PO4)O, status A, IMA No. 2020-092, country Jordan, and sole reference European Journal of Mineralogy 37 (2025), 353. |
| britvin_2025_primary | https://doi.org/10.5194/ejm-37-353-2025; Britvin SN et al. (2025) Eur. J. Mineral. 37:353-363, pp. 353-363, Tables 1-8, Figures 1-6 (32 bounded passages &lt;= 1,800 B and PNG renders of pages 4 and 6) | supports | All 11 pages (32 bounded passages &lt;= 1,800 B) and PNG renders of pages 4 and 6 inspected, confirming type locality, holotype specimen 5567/1, Table 3 9-point EPMA composition (Fe2O3 35.42, NiO 31.11, CoO 0.59, MgO 0.67, CaO 0.69, ZnO 0.14, P2O5 31.34, V2O5 0.09, SO3 0.27, total 100.32 wt%), empirical formula (Ni0.92Mg0.04Ca0.03Co0.02)(Fe3+0.98Ca0.02)([P0.98S0.01]O4)O, trigonal R-3 cell parameters, and Abstract vs Table 4/5 notes. |
| create_history | history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml; Canonical CREATE history sidecar history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml | supports | Canonical CREATE history sidecar (SHA-256 ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587) matches record curation_history[0].timestamp and top-level record sections. |
| validation | data/records/moabite.yaml; Real CLI validation via .venv/bin/cmmmech validate --require-records and .venv/bin/cmmmech validate-history --base main | supports | Checked 673 record(s); 0 failed. Checked 1162 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py, max 1,800 bytes per passage) plus single-page PNG renders of Tables 3-7.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T015200Z-moabite-round124-scientific-review
kind: record
repository: CultureBotAI/CMMMech
title: Primary-source scientific review of moabite (IMA:2020-092, status A, NiFe3+(PO4)O)
started_at: '2026-10-31T01:50:50Z'
finished_at: '2026-10-31T01:52:00Z'
reviewer:
  identity: antigravity / round124-scientific-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying all scientific claims in data/records/moabite.yaml (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410)
    against all 32 bounded passages (11 pages) and single-page PNG renders of pages
    4 and 6 of Britvin SN, Murashko MN, Krzhizhanovskaya MG, Vapnik Y, Vlasenko NS,
    Vereshchagin OS, Pankin DV, and Vasiliev EA (2025, Eur. J. Mineral. 37:353-363)
    and the September 2026 IMA-CNMNC Master List (PDF p. 145).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: e954c96898ce97da6781984c7da7ea5d4fda9bfa
  state: working_tree
  inputs:
  - path: data/records/moabite.yaml
    sha256: e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410
    role: target
  - path: history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
    sha256: ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587
    role: context
  - path: research/sources/round124-minerals/20261031T015000Z-source-investigation.json
    sha256: 896abccad090d9bb3f258cc2b6144323e1b1aae69e88550611b2eb5d59a5266e
    role: context
  - path: research/sources/round124-minerals/20261031T015000Z-source-investigation.md
    sha256: 8f3b2d8438f251351d1a566cc19c320f6f77257d13b30a3cf394b237e25feb3e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:moabite
  path: data/records/moabite.yaml
  label: Moabite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/moabite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
    role: canonical_history
scope:
  description: Primary-source scientific review of data/records/moabite.yaml (SHA-256
    e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410) and its canonical
    CREATE history sidecar against all 32 bounded primary-source passages (11 pages)
    and rendered PNGs of pages 4 and 6 from Britvin et al. (2025, Eur. J. Mineral.
    37:353-363) and the September 2026 IMA-CNMNC Master List (PDF p. 145).
  selection: Round 124 newly admitted mineral record moabite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:moabite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/moabite.yaml
  locator: Working-tree record data/records/moabite.yaml
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Working-tree record data/records/moabite.yaml (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410)
    captures IMA:2020-092 identity, Daba-Siwaqa pyrometamorphic complex (Hatrurim
    Basin, Jordan) type locality, holotype repository FMM No. 5567/1, Table 3 (p.
    356) 9-point EPMA chemistry, trigonal R-3 tavorite-group-related structure (Tables
    4-8), Raman spectrum, physical/optical properties, internal primary-source notes
    (Abstract Dcalc = 4.324 g/cm3 and comma decimal separator 3,321(37)(102) vs Table
    5 Dx = 4.338 g/cm3 and Table 4 3.321 (37) (102)), and 0 mechanisms.
  snapshot_sha256: e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List, PDF p. 145
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Confirms Moabite, formula NiFe3+(PO4)O, status A, IMA No. 2020-092, country
    Jordan, and sole reference European Journal of Mineralogy 37 (2025), 353.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: britvin_2025_primary
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-37-353-2025
  locator: Britvin SN et al. (2025) Eur. J. Mineral. 37:353-363, pp. 353-363, Tables
    1-8, Figures 1-6 (32 bounded passages <= 1,800 B and PNG renders of pages 4 and
    6)
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: All 11 pages (32 bounded passages <= 1,800 B) and PNG renders of pages
    4 and 6 inspected, confirming type locality, holotype specimen 5567/1, Table 3
    9-point EPMA composition (Fe2O3 35.42, NiO 31.11, CoO 0.59, MgO 0.67, CaO 0.69,
    ZnO 0.14, P2O5 31.34, V2O5 0.09, SO3 0.27, total 100.32 wt%), empirical formula
    (Ni0.92Mg0.04Ca0.03Co0.02)(Fe3+0.98Ca0.02)([P0.98S0.01]O4)O, trigonal R-3 cell
    parameters, and Abstract vs Table 4/5 notes.
  snapshot_sha256: 7340e0f9c6213775801d2987bbd165285831bca467ae671b48275cecfdcf1602
- evidence_id: create_history
  kind: record_content
  reference: history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
  locator: Canonical CREATE history sidecar history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Canonical CREATE history sidecar (SHA-256 ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587)
    matches record curation_history[0].timestamp and top-level record sections.
  snapshot_sha256: ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587
- evidence_id: validation
  kind: validation
  reference: data/records/moabite.yaml
  locator: Real CLI validation via .venv/bin/cmmmech validate --require-records and
    .venv/bin/cmmmech validate-history --base main
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Checked 673 record(s); 0 failed. Checked 1162 history record(s); 0 error(s).
  snapshot_sha256: e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: .venv/bin/cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:moabite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: .venv/bin/cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1162 history record(s); 0 error(s).
  target_ids:
  - cmmmech:moabite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_primary_source_verification
  area: evidence
  topic: Verification of IMA:2020-092 identity, Jordan pyrometamorphic type locality,
    EPMA chemistry, trigonal R-3 structure, and internal source notes for moabite
  outcome: supported
  summary: All numeric, crystallographic, Raman, optical, and chemical claims in data/records/moabite.yaml
    (SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410) match
    the bounded primary-source passages and rendered table PNGs of Britvin et al.
    (2025, Eur. J. Mineral. 37:353-363) and the September 2026 IMA Master List (p.
    145).
  target_ids:
  - cmmmech:moabite
  evidence_ids:
  - owner
  - ima_authority
  - britvin_2025_primary
- assessment_id: mechanism_absence_and_provenance_verification
  area: provenance
  topic: Verification of 0 mechanisms (abiotic occurrence only) and append-only CREATE
    provenance
  outcome: supported
  summary: data/records/moabite.yaml accurately omits mechanisms (0 mechanisms) and
    explicitly discloses that no criticality designation, microbial mechanism, or
    industrial recovery yield is asserted. Append-only CREATE history sidecar passes
    validation with 0 errors.
  target_ids:
  - cmmmech:moabite
  evidence_ids:
  - owner
  - britvin_2025_primary
  - create_history
  - validation
findings: []
actions: []
summary: 'Moabite (IMA:2020-092, status A, NiFe3+(PO4)O) passes primary-source scientific
  review (scientific_review: true) at SHA-256 e0d7755155674610bbf16d2365c058a87f8021426eeba22e28db77a20bd13410
  against all 32 bounded passages (11 pages) and rendered table PNGs of Britvin et
  al. (2025, Eur. J. Mineral. 37:353-363).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py,
  max 1,800 bytes per passage) plus single-page PNG renders of Tables 3-7.
related_reviews: []
```
