# Primary-source scientific review of laurentthomasite (IMA:2018-157, status A, Mg2K(Be2Al)Si12O30)

- Review: 20261031T015200Z-laurentthomasite-round124-scientific-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T01:50:30Z
- Finished UTC: 2026-10-31T01:52:00Z
- Reviewer: antigravity / round124-scientific-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Laurentthomasite (IMA:2018-157, status A, Mg2K(Be2Al)Si12O30) passes primary-source scientific review (scientific_review: true) at SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859 against all 31 bounded passages (11 pages) and rendered table PNGs of Ferraris et al. (2020, Eur. J. Mineral. 32:355-365).

## Scope And Provenance

Primary-source scientific review of data/records/laurentthomasite.yaml (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) and its canonical CREATE history sidecar against all 31 bounded primary-source passages (11 pages) and rendered PNGs of pages 5 and 8 from Ferraris et al. (2020, Eur. J. Mineral. 32:355-365) and the September 2026 IMA-CNMNC Master List (PDF p. 122).

Selection: Round 124 newly admitted mineral record laurentthomasite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e954c96898ce97da6781984c7da7ea5d4fda9bfa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:laurentthomasite | data/records/laurentthomasite.yaml | maintained | Laurentthomasite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:laurentthomasite | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:laurentthomasite | Checked 1162 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of IMA:2018-157 identity, Madagascar type locality, EPMA/LA-ICP-MS chemistry, hexagonal P6/mcc structure, and internal source discrepancies for laurentthomasite

evidence: supported. Targets: cmmmech:laurentthomasite.

All numeric, crystallographic, optical, and chemical claims in data/records/laurentthomasite.yaml (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) match the bounded primary-source passages and rendered table PNGs of Ferraris et al. (2020, Eur. J. Mineral. 32:355-365) and the September 2026 IMA Master List (p. 122).

### Verification of 0 mechanisms (abiotic occurrence only) and append-only CREATE provenance

provenance: supported. Targets: cmmmech:laurentthomasite.

data/records/laurentthomasite.yaml accurately omits mechanisms (0 mechanisms) and explicitly discloses that no criticality designation, microbial mechanism, or industrial recovery yield is asserted. Append-only CREATE history sidecar passes validation with 0 errors.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/laurentthomasite.yaml; Working-tree record data/records/laurentthomasite.yaml | supports | Working-tree record data/records/laurentthomasite.yaml (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) captures IMA:2018-157 identity, Ambatofinandrahana District (Fianarantsoa Province, Madagascar) type locality, holotype repositories MRSN M/19820 and MSNMI 43018, Table 2 (p. 359) EPMA + LA-ICP-MS chemistry (8 EPMA + 6 LA-ICP-MS spots), hexagonal P6/mcc milarite-group-related structure (Tables 5-8), physical/optical properties, internal primary-source discrepancies (Table 1 Mg2K(Be2Al)Si12O3 typo; Table 2 FeO mean 2.69 wt% vs range 2.50-2.67 and TiO2 range 0.02-0.019; Abstract 9 PXRD lines vs Table 5; Section 5.2 prose c = 14.114916(11) Å vs Table 6 c = 14.14920(10) Å), and 0 mechanisms. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List, PDF p. 122 | supports | Confirms Laurentthomasite, formula Mg2K(Be2Al)Si12O30, status A, IMA No. 2018-157, country Madagascar, and sole reference European Journal of Mineralogy 32 (2020), 355. |
| ferraris_2020_primary | https://doi.org/10.5194/ejm-32-355-2020; Ferraris C, Pignatelli I, Cámara F, Parodi G, Pont S, Schreyer M, and Wei F (2020) Eur. J. Mineral. 32:355-365, pp. 355-365, Tables 1-8, Figures 1-7 (31 bounded passages &lt;= 1,800 B and PNG renders of pages 5 and 8) | supports | All 11 pages (31 bounded passages &lt;= 1,800 B) and PNG renders of pages 5 and 8 inspected, confirming type locality, holotype numbers M/19820 and 43018, Table 2 EPMA/LA-ICP-MS composition (total 99.66 wt%), empirical formula (K0.91Na0.03Ba0.01)(Mg1.02Sc0.46Fe2+0.39Mn0.12Ca0.02)(Be2.04Al0.93Mg0.03)Si12.02O30, hexagonal P6/mcc cell parameters, and all four internal primary-source typographical discrepancies. |
| create_history | history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml; Canonical CREATE history sidecar history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml | supports | Canonical CREATE history sidecar (SHA-256 ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c) matches record curation_history[0].timestamp and top-level record sections. |
| validation | data/records/laurentthomasite.yaml; Real CLI validation via .venv/bin/cmmmech validate --require-records and .venv/bin/cmmmech validate-history --base main | supports | Checked 673 record(s); 0 failed. Checked 1162 history record(s); 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py, max 1,800 bytes per passage) plus single-page PNG renders of Tables 2-6.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T015200Z-laurentthomasite-round124-scientific-review
kind: record
repository: CultureBotAI/CMMMech
title: Primary-source scientific review of laurentthomasite (IMA:2018-157, status
  A, Mg2K(Be2Al)Si12O30)
started_at: '2026-10-31T01:50:30Z'
finished_at: '2026-10-31T01:52:00Z'
reviewer:
  identity: antigravity / round124-scientific-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying all scientific claims in data/records/laurentthomasite.yaml (SHA-256
    9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) against all
    31 bounded passages (11 pages) and single-page PNG renders of pages 5 and 8 of
    Ferraris C, Pignatelli I, Cámara F, Parodi G, Pont S, Schreyer M, and Wei F (2020,
    Eur. J. Mineral. 32:355-365) and the September 2026 IMA-CNMNC Master List (PDF
    p. 122).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: e954c96898ce97da6781984c7da7ea5d4fda9bfa
  state: working_tree
  inputs:
  - path: data/records/laurentthomasite.yaml
    sha256: 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859
    role: target
  - path: history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml
    sha256: ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c
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
- target_id: cmmmech:laurentthomasite
  path: data/records/laurentthomasite.yaml
  label: Laurentthomasite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/laurentthomasite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml
    role: canonical_history
scope:
  description: Primary-source scientific review of data/records/laurentthomasite.yaml
    (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) and
    its canonical CREATE history sidecar against all 31 bounded primary-source passages
    (11 pages) and rendered PNGs of pages 5 and 8 from Ferraris et al. (2020, Eur.
    J. Mineral. 32:355-365) and the September 2026 IMA-CNMNC Master List (PDF p. 122).
  selection: Round 124 newly admitted mineral record laurentthomasite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:laurentthomasite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/laurentthomasite.yaml
  locator: Working-tree record data/records/laurentthomasite.yaml
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Working-tree record data/records/laurentthomasite.yaml (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859)
    captures IMA:2018-157 identity, Ambatofinandrahana District (Fianarantsoa Province,
    Madagascar) type locality, holotype repositories MRSN M/19820 and MSNMI 43018,
    Table 2 (p. 359) EPMA + LA-ICP-MS chemistry (8 EPMA + 6 LA-ICP-MS spots), hexagonal
    P6/mcc milarite-group-related structure (Tables 5-8), physical/optical properties,
    internal primary-source discrepancies (Table 1 Mg2K(Be2Al)Si12O3 typo; Table 2
    FeO mean 2.69 wt% vs range 2.50-2.67 and TiO2 range 0.02-0.019; Abstract 9 PXRD
    lines vs Table 5; Section 5.2 prose c = 14.114916(11) Å vs Table 6 c = 14.14920(10)
    Å), and 0 mechanisms.
  snapshot_sha256: 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List, PDF p. 122
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Confirms Laurentthomasite, formula Mg2K(Be2Al)Si12O30, status A, IMA No.
    2018-157, country Madagascar, and sole reference European Journal of Mineralogy
    32 (2020), 355.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: ferraris_2020_primary
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-32-355-2020
  locator: Ferraris C, Pignatelli I, Cámara F, Parodi G, Pont S, Schreyer M, and Wei
    F (2020) Eur. J. Mineral. 32:355-365, pp. 355-365, Tables 1-8, Figures 1-7 (31
    bounded passages <= 1,800 B and PNG renders of pages 5 and 8)
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: All 11 pages (31 bounded passages <= 1,800 B) and PNG renders of pages
    5 and 8 inspected, confirming type locality, holotype numbers M/19820 and 43018,
    Table 2 EPMA/LA-ICP-MS composition (total 99.66 wt%), empirical formula (K0.91Na0.03Ba0.01)(Mg1.02Sc0.46Fe2+0.39Mn0.12Ca0.02)(Be2.04Al0.93Mg0.03)Si12.02O30,
    hexagonal P6/mcc cell parameters, and all four internal primary-source typographical
    discrepancies.
  snapshot_sha256: 6ec8ead80c98baae4e5ca0425a1a944d3f707ecec5152d037f8627ac270737d8
- evidence_id: create_history
  kind: record_content
  reference: history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml
  locator: Canonical CREATE history sidecar history/records/laurentthomasite/2026-10-31T014320Z-antigravity-d9a148.yaml
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Canonical CREATE history sidecar (SHA-256 ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c)
    matches record curation_history[0].timestamp and top-level record sections.
  snapshot_sha256: ceff24ee5b7f169edcbf62a81402b82f3af490c465b6a29be323736116c6422c
- evidence_id: validation
  kind: validation
  reference: data/records/laurentthomasite.yaml
  locator: Real CLI validation via .venv/bin/cmmmech validate --require-records and
    .venv/bin/cmmmech validate-history --base main
  accessed_at: '2026-10-31T01:51:00Z'
  support: supports
  summary: Checked 673 record(s); 0 failed. Checked 1162 history record(s); 0 error(s).
  snapshot_sha256: 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: .venv/bin/cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:laurentthomasite
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
  - cmmmech:laurentthomasite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_primary_source_verification
  area: evidence
  topic: Verification of IMA:2018-157 identity, Madagascar type locality, EPMA/LA-ICP-MS
    chemistry, hexagonal P6/mcc structure, and internal source discrepancies for laurentthomasite
  outcome: supported
  summary: All numeric, crystallographic, optical, and chemical claims in data/records/laurentthomasite.yaml
    (SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859) match
    the bounded primary-source passages and rendered table PNGs of Ferraris et al.
    (2020, Eur. J. Mineral. 32:355-365) and the September 2026 IMA Master List (p.
    122).
  target_ids:
  - cmmmech:laurentthomasite
  evidence_ids:
  - owner
  - ima_authority
  - ferraris_2020_primary
- assessment_id: mechanism_absence_and_provenance_verification
  area: provenance
  topic: Verification of 0 mechanisms (abiotic occurrence only) and append-only CREATE
    provenance
  outcome: supported
  summary: data/records/laurentthomasite.yaml accurately omits mechanisms (0 mechanisms)
    and explicitly discloses that no criticality designation, microbial mechanism,
    or industrial recovery yield is asserted. Append-only CREATE history sidecar passes
    validation with 0 errors.
  target_ids:
  - cmmmech:laurentthomasite
  evidence_ids:
  - owner
  - ferraris_2020_primary
  - create_history
  - validation
findings: []
actions: []
summary: 'Laurentthomasite (IMA:2018-157, status A, Mg2K(Be2Al)Si12O30) passes primary-source
  scientific review (scientific_review: true) at SHA-256 9a042b43edc7216216e23232f52230305101a5b7755e4de30a018d5ae0708859
  against all 31 bounded passages (11 pages) and rendered table PNGs of Ferraris et
  al. (2020, Eur. J. Mineral. 32:355-365).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed under the Round 124 bounded source-text workflow (scripts/index_bounded_pdf_passages.py,
  max 1,800 bytes per passage) plus single-page PNG renders of Tables 2-6.
related_reviews: []
```
