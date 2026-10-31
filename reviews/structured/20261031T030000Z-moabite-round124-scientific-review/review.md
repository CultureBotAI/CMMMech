# Primary-source scientific review of moabite (IMA:2020-092, status A, NiFe3+(PO4)O)

- Review: 20261031T030000Z-moabite-round124-scientific-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T02:58:00Z
- Finished UTC: 2026-10-31T03:00:00Z
- Reviewer: antigravity / round124-scientific-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Moabite (IMA:2020-092, status A, NiFe3+(PO4)O) passes primary-source scientific review (scientific_review: true) at SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716 against all 32 bounded passages (11 full-PDF pages; 8 main-text pages / 21 passages) and rendered table PNGs of Britvin et al. (2025, Eur. J. Mineral. 37:353-363).

## Scope And Provenance

Primary-source scientific review of data/records/moabite.yaml (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716) and its canonical CREATE and EDIT history sidecars against all 32 bounded primary-source passages (11 full-PDF pages; 8 main-text pages / 21 passages) and rendered PNGs of pages 4 and 6 from Britvin et al. (2025, Eur. J. Mineral. 37:353-363) and the September 2026 IMA-CNMNC Master List (PDF p. 145).

Selection: Round 124 newly admitted mineral record moabite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f67a43c3820cb330cdd4f14695c34245645a1a70.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:moabite | data/records/moabite.yaml | maintained | Moabite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:moabite | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:moabite | Checked 1167 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of IMA:2020-092 identity, Jordan pyrometamorphic type locality, EPMA chemistry, orthorhombic Pnma structure, and internal source conventions/discrepancies for moabite

evidence: supported. Targets: cmmmech:moabite.

All numeric, crystallographic, Raman, and chemical claims in data/records/moabite.yaml (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716) match the bounded primary-source passages and rendered table PNGs of Britvin et al. (2025, Eur. J. Mineral. 37:353-363) and the September 2026 IMA Master List (p. 145).

### Verification of 0 mechanisms (abiotic occurrence only) and append-only CREATE + EDIT provenance

provenance: supported. Targets: cmmmech:moabite.

data/records/moabite.yaml accurately omits mechanisms (0 mechanisms) and explicitly discloses that no criticality designation, microbial mechanism, or industrial recovery yield is asserted. Append-only CREATE and EDIT history sidecars pass validation with 0 errors.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/moabite.yaml; Working-tree record data/records/moabite.yaml | supports | Working-tree record data/records/moabite.yaml (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716) captures IMA:2020-092 identity, Daba-Siwaqa pyrometamorphic complex (Hatrurim Basin / Dead Sea transform region, Jordan) type locality, holotype repository FMM_1_97015 (Fersman Mineralogical Museum), Table 2 (p. 356) EPMA chemistry (5 spots, FeO* column header with footnote Total iron calculated as Fe2O3), orthorhombic Pnma structure (Tables 4-7), internal primary-source discrepancies (Abstract Dcalc = 4.324 g/cm3 for empirical formula vs Table 5 Dx = 4.338 g/cm3 for ideal NiFe(PO4)O; Abstract comma decimal 3,321(37)(102) vs Table 4 3.321 (37) (102)), and 0 mechanisms. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List, PDF p. 145 | supports | Confirms Moabite, formula NiFe3+(PO4)O, status A, IMA No. 2020-092, country Jordan, and sole reference European Journal of Mineralogy 37 (2025), 353. |
| britvin_2025_primary | https://doi.org/10.5194/ejm-37-353-2025; Britvin SN, Murashko MN, Krzhizhanovskaya MG, Vapnik Y, Vlasenko NS, Vereshchagin OS, Pankin DV, and Vasiliev EA (2025) Moabite, NiFe3+(PO4)O, a new natural oxyphosphate, Eur. J. Mineral. 37:353-363, pp. 353-363, Tables 1-7, Figures 1-6 (32 bounded passages &lt;= 1,800 B across 11 full-PDF pages; 8 main-text pages / 21 passages, plus PNG renders of pages 4 and 6) | supports | All 11 full-PDF pages (32 bounded passages &lt;= 1,800 B, 47,902 passage bytes / 47,935 raw text bytes; 8 main-text pages pp. 353-360, 21 passages) and PNG renders of pages 4 and 6 inspected, confirming verbatim title, type locality, holotype FMM_1_97015, Table 2 EPMA composition (total 99.66 wt%), empirical formula (Ni0.92Mg0.03Co2+0.03Zn0.02Cu0.01Ca0.01)Sigma1.02(Fe3+0.89Al0.08Co3+0.01Cr0.01Ti0.01)Sigma1.00(P0.99V0.01)Sigma1.00O5, orthorhombic Pnma cell parameters, and all internal primary-source conventions/discrepancies. |
| create_history | history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml; Canonical CREATE history sidecar history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml | supports | Canonical CREATE history sidecar (SHA-256 ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587) matches record curation_history[0].timestamp and top-level record sections. |
| edit_history | history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml; Canonical EDIT history sidecar history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml | supports | Canonical EDIT history sidecar (SHA-256 ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b) records PR |
| validation | data/records/moabite.yaml; Real CLI validation via .venv/bin/cmmmech validate --require-records and .venv/bin/cmmmech validate-history --base main | supports | Checked 673 record(s); 0 failed. Checked 1167 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py, max 1,800 bytes per passage) plus single-page PNG renders of Tables 2, 4, and 5.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T030000Z-moabite-round124-scientific-review
kind: record
repository: CultureBotAI/CMMMech
title: Primary-source scientific review of moabite (IMA:2020-092, status A, NiFe3+(PO4)O)
started_at: '2026-10-31T02:58:00Z'
finished_at: '2026-10-31T03:00:00Z'
reviewer:
  identity: antigravity / round124-scientific-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying all scientific claims in data/records/moabite.yaml (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716)
    and its CREATE + EDIT history sidecars against all 32 bounded passages (11 full-PDF
    pages; 8 main-text pages / 21 passages) and single-page PNG renders of pages 4
    and 6 of Britvin SN, Murashko MN, Krzhizhanovskaya MG, Vapnik Y, Vlasenko NS,
    Vereshchagin OS, Pankin DV, and Vasiliev EA (2025, Eur. J. Mineral. 37:353-363)
    and the September 2026 IMA-CNMNC Master List (PDF p. 145).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: f67a43c3820cb330cdd4f14695c34245645a1a70
  state: working_tree
  inputs:
  - path: data/records/moabite.yaml
    sha256: c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716
    role: target
  - path: history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
    sha256: ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587
    role: context
  - path: history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml
    sha256: ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b
    role: context
  - path: research/sources/round124-minerals/20261031T015000Z-source-investigation.json
    sha256: 9f97d3454585a593332f939a491d8dd7cc23adbe4fffee67dbdb057e822e4b1e
    role: context
  - path: research/sources/round124-minerals/20261031T015000Z-source-investigation.md
    sha256: 5dd0aa6ee7ad095cc1bc94868a377707cacfd15ad6d7f368899148861403a7eb
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
  - repository: CultureBotAI/CMMMech
    path: history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml
    role: canonical_history
scope:
  description: Primary-source scientific review of data/records/moabite.yaml (SHA-256
    c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716) and its canonical
    CREATE and EDIT history sidecars against all 32 bounded primary-source passages
    (11 full-PDF pages; 8 main-text pages / 21 passages) and rendered PNGs of pages
    4 and 6 from Britvin et al. (2025, Eur. J. Mineral. 37:353-363) and the September
    2026 IMA-CNMNC Master List (PDF p. 145).
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
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: Working-tree record data/records/moabite.yaml (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716)
    captures IMA:2020-092 identity, Daba-Siwaqa pyrometamorphic complex (Hatrurim
    Basin / Dead Sea transform region, Jordan) type locality, holotype repository
    FMM_1_97015 (Fersman Mineralogical Museum), Table 2 (p. 356) EPMA chemistry (5
    spots, FeO* column header with footnote Total iron calculated as Fe2O3), orthorhombic
    Pnma structure (Tables 4-7), internal primary-source discrepancies (Abstract Dcalc
    = 4.324 g/cm3 for empirical formula vs Table 5 Dx = 4.338 g/cm3 for ideal NiFe(PO4)O;
    Abstract comma decimal 3,321(37)(102) vs Table 4 3.321 (37) (102)), and 0 mechanisms.
  snapshot_sha256: c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List, PDF p. 145
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: Confirms Moabite, formula NiFe3+(PO4)O, status A, IMA No. 2020-092, country
    Jordan, and sole reference European Journal of Mineralogy 37 (2025), 353.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: britvin_2025_primary
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-37-353-2025
  locator: Britvin SN, Murashko MN, Krzhizhanovskaya MG, Vapnik Y, Vlasenko NS, Vereshchagin
    OS, Pankin DV, and Vasiliev EA (2025) Moabite, NiFe3+(PO4)O, a new natural oxyphosphate,
    Eur. J. Mineral. 37:353-363, pp. 353-363, Tables 1-7, Figures 1-6 (32 bounded
    passages <= 1,800 B across 11 full-PDF pages; 8 main-text pages / 21 passages,
    plus PNG renders of pages 4 and 6)
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: All 11 full-PDF pages (32 bounded passages <= 1,800 B, 47,902 passage bytes
    / 47,935 raw text bytes; 8 main-text pages pp. 353-360, 21 passages) and PNG renders
    of pages 4 and 6 inspected, confirming verbatim title, type locality, holotype
    FMM_1_97015, Table 2 EPMA composition (total 99.66 wt%), empirical formula (Ni0.92Mg0.03Co2+0.03Zn0.02Cu0.01Ca0.01)Sigma1.02(Fe3+0.89Al0.08Co3+0.01Cr0.01Ti0.01)Sigma1.00(P0.99V0.01)Sigma1.00O5,
    orthorhombic Pnma cell parameters, and all internal primary-source conventions/discrepancies.
  snapshot_sha256: 7340e0f9c6213775801d2987bbd165285831bca467ae671b48275cecfdcf1602
- evidence_id: create_history
  kind: record_content
  reference: history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
  locator: Canonical CREATE history sidecar history/records/moabite/2026-10-31T014403Z-antigravity-b23957.yaml
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: Canonical CREATE history sidecar (SHA-256 ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587)
    matches record curation_history[0].timestamp and top-level record sections.
  snapshot_sha256: ff50d9856da730c1b2b8e2b3111cca3cc3c1d1f091bd8b9d010c5dfd086b6587
- evidence_id: edit_history
  kind: record_content
  reference: history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml
  locator: Canonical EDIT history sidecar history/records/moabite/2026-10-31T025504Z-antigravity-a45570.yaml
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: Canonical EDIT history sidecar (SHA-256 ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b)
    records PR
  snapshot_sha256: ec079c663c99dc0fe66ae5f835af8e206f5335b832681d0c5d54d8b03492a53b
- evidence_id: validation
  kind: validation
  reference: data/records/moabite.yaml
  locator: Real CLI validation via .venv/bin/cmmmech validate --require-records and
    .venv/bin/cmmmech validate-history --base main
  accessed_at: '2026-10-31T02:59:00Z'
  support: supports
  summary: Checked 673 record(s); 0 failed. Checked 1167 history record(s); 0 error(s).
  snapshot_sha256: c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716
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
  summary: Checked 1167 history record(s); 0 error(s).
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
    EPMA chemistry, orthorhombic Pnma structure, and internal source conventions/discrepancies
    for moabite
  outcome: supported
  summary: All numeric, crystallographic, Raman, and chemical claims in data/records/moabite.yaml
    (SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716) match
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
    + EDIT provenance
  outcome: supported
  summary: data/records/moabite.yaml accurately omits mechanisms (0 mechanisms) and
    explicitly discloses that no criticality designation, microbial mechanism, or
    industrial recovery yield is asserted. Append-only CREATE and EDIT history sidecars
    pass validation with 0 errors.
  target_ids:
  - cmmmech:moabite
  evidence_ids:
  - owner
  - britvin_2025_primary
  - create_history
  - edit_history
  - validation
findings: []
actions: []
summary: 'Moabite (IMA:2020-092, status A, NiFe3+(PO4)O) passes primary-source scientific
  review (scientific_review: true) at SHA-256 c17fe15c00245194554bcd806f0d8c985aea1d67e4c41d80cf631de6a986b716
  against all 32 bounded passages (11 full-PDF pages; 8 main-text pages / 21 passages)
  and rendered table PNGs of Britvin et al. (2025, Eur. J. Mineral. 37:353-363).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py,
  max 1,800 bytes per passage) plus single-page PNG renders of Tables 2, 4, and 5.
related_reviews: []
```
