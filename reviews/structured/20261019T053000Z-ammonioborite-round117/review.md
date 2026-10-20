# Scientific review of ammonioborite

- Review: 20261019T053000Z-ammonioborite-round117
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-19T05:26:00Z
- Finished UTC: 2026-10-19T05:30:00Z
- Reviewer: antigravity / round117-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ammonioborite passes with limitations: Grandfathered (1933 s.p., Rn 1999) (NH4)3B15O20(OH)8(H2O)4 IMA identity (Merlino &amp; Sartori 1971 pentadecaborate structural formula), Schaller (1933) Larderello (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water sassolite washing, and negative 20-30 C synthesis trials are supported with zero fabricated processing mechanisms.

## Scope And Provenance

Complete frozen working-tree record data/records/ammonioborite.yaml, canonical CREATE history sidecar history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml, and primary-source evidence boundaries.

Selection: Targeted structured review of newly curated Round 117 CMM record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ammonioborite | data/records/ammonioborite.yaml | maintained | Ammonioborite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:ammonioborite | Checked 616 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:ammonioborite | Checked 744 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Primary-source identity and evidence boundaries for ammonioborite

evidence: supported. Targets: cmmmech:ammonioborite.

Grandfathered (1933 s.p., Rn 1999) (NH4)3B15O20(OH)8(H2O)4 IMA identity (Merlino &amp; Sartori 1971 pentadecaborate structural formula), Schaller (1933) Larderello (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water sassolite washing, and negative 20-30 C synthesis trials are supported with zero fabricated processing mechanisms.

### Provenance, category boundaries, and absence of fabricated claims

provenance: supported. Targets: cmmmech:ammonioborite.

No unmeasured recovery yields, unverified biological interactions, or improper criticality transfers are claimed; CREATE sidecar and inline history match the frozen record.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ammonioborite.yaml; Complete frozen working-tree record data/records/ammonioborite.yaml | supports | All structured claims, identifiers, relations, and qualification notes match the inspected primary sources. |
| history | history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml; Complete canonical CREATE sidecar history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml | supports | Canonical history sidecar and inline history event accurately record actor, UTC timestamp, and scientific scope. |
| dossier | research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json; Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json | context_only | Documents deduplication, primary-source acquisition hashes, and scope boundaries. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Establishes official mineral species nomenclature, formula, approval status, and commodity vs mineral category boundary. |
| primary_study | http://www.minsocam.org/ammin/AM18/AM18_480.pdf; Complete full-text visual inspection of AM 18 (1933) 480-492 (13 pp.), Science 171 (1971) 377-379, and IMA September 2026 Master List (1933 s.p., Rn 1999) | supports | Grandfathered (1933 s.p., Rn 1999) (NH4)3B15O20(OH)8(H2O)4 IMA identity (Merlino &amp; Sartori 1971 pentadecaborate structural formula), Schaller (1933) Larderello (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water sassolite washing, and negative 20-30 C synthesis trials are supported with zero fabricated processing mechanisms. |
| validation | data/records/ammonioborite.yaml; Strict schema and history validation across all 616 records and 744 history sidecars | supports | Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
- No biological processing or pilot-scale extraction yield is reported in the inspected primary sources; unstated process parameters remain null.
- All primary-source PDFs and authority documents were visually inspected in full before record creation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T053000Z-ammonioborite-round117
kind: record
repository: CultureBotAI/CMMMech
title: Scientific review of ammonioborite
started_at: '2026-10-19T05:26:00Z'
finished_at: '2026-10-19T05:30:00Z'
reviewer:
  identity: antigravity / round117-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/cmmmech-add-record/SKILL.md;
    full primary-source PDFs, official authorities (DOE 2023 Federal Register, USGS
    MCS 2026, IMA September 2026 Master List), figures, tables, and record/history/schema
    invariants were verified page-by-page against the frozen working-tree record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34
  state: working_tree
  inputs:
  - path: data/records/ammonioborite.yaml
    sha256: 679150872fd49c31398f5bd6daa6e0d378d96e0a734a0c641f1147d182a25352
    role: target
  - path: history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml
    sha256: 944c07fd9fc0f113ac8c15de86ab031293eb4b42927add68a7857ac328604753
    role: context
  - path: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
    sha256: 1e29992985ffa6ebfad178223550e4a7680fb96b399a07782f1f3fc4b0e4c1d6
    role: context
  - path: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.md
    sha256: 1352dfc950a92c4d6fdcf868e1d9082fe1ac3f7d776eeae19702d0addaad4fe7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
targets:
- target_id: cmmmech:ammonioborite
  path: data/records/ammonioborite.yaml
  label: Ammonioborite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ammonioborite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml
    role: canonical_history
scope:
  description: Complete frozen working-tree record data/records/ammonioborite.yaml,
    canonical CREATE history sidecar history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml,
    and primary-source evidence boundaries.
  selection: Targeted structured review of newly curated Round 117 CMM record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ammonioborite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ammonioborite.yaml
  locator: Complete frozen working-tree record data/records/ammonioborite.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: All structured claims, identifiers, relations, and qualification notes
    match the inspected primary sources.
  snapshot_sha256: 679150872fd49c31398f5bd6daa6e0d378d96e0a734a0c641f1147d182a25352
- evidence_id: history
  kind: record_content
  reference: history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml
  locator: Complete canonical CREATE sidecar history/records/ammonioborite/2026-10-19T052200Z-antigravity-001175.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Canonical history sidecar and inline history event accurately record actor,
    UTC timestamp, and scientific scope.
  snapshot_sha256: 944c07fd9fc0f113ac8c15de86ab031293eb4b42927add68a7857ac328604753
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
  locator: Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
  accessed_at: '2026-10-19T05:30:00Z'
  support: context_only
  summary: Documents deduplication, primary-source acquisition hashes, and scope boundaries.
  snapshot_sha256: 1e29992985ffa6ebfad178223550e4a7680fb96b399a07782f1f3fc4b0e4c1d6
- evidence_id: ima_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA-CNMNC September 2026 Master List (244 pages visually inspected)
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Establishes official mineral species nomenclature, formula, approval status,
    and commodity vs mineral category boundary.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary_study
  kind: primary_source
  reference: http://www.minsocam.org/ammin/AM18/AM18_480.pdf
  locator: Complete full-text visual inspection of AM 18 (1933) 480-492 (13 pp.),
    Science 171 (1971) 377-379, and IMA September 2026 Master List (1933 s.p., Rn
    1999)
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Grandfathered (1933 s.p., Rn 1999) (NH4)3B15O20(OH)8(H2O)4 IMA identity
    (Merlino & Sartori 1971 pentadecaborate structural formula), Schaller (1933) Larderello
    (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water sassolite washing, and negative
    20-30 C synthesis trials are supported with zero fabricated processing mechanisms.
  snapshot_sha256: 3df6c75f8e463a9cdd22eaec551aaf7cdf3d650a09a56ad632805fbe053dd936
- evidence_id: validation
  kind: validation
  reference: data/records/ammonioborite.yaml
  locator: Strict schema and history validation across all 616 records and 744 history
    sidecars
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s).
  snapshot_sha256: 679150872fd49c31398f5bd6daa6e0d378d96e0a734a0c641f1147d182a25352
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 616 record(s); 0 failed.
  target_ids:
  - cmmmech:ammonioborite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34
  status: passed
  required: true
  summary: Checked 744 history record(s); 0 error(s).
  target_ids:
  - cmmmech:ammonioborite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_evidence
  area: evidence
  topic: Primary-source identity and evidence boundaries for ammonioborite
  outcome: supported
  summary: Grandfathered (1933 s.p., Rn 1999) (NH4)3B15O20(OH)8(H2O)4 IMA identity
    (Merlino & Sartori 1971 pentadecaborate structural formula), Schaller (1933) Larderello
    (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water sassolite washing, and negative
    20-30 C synthesis trials are supported with zero fabricated processing mechanisms.
  target_ids:
  - cmmmech:ammonioborite
  evidence_ids:
  - owner
  - ima_authority
  - primary_study
- assessment_id: scope_and_provenance
  area: provenance
  topic: Provenance, category boundaries, and absence of fabricated claims
  outcome: supported
  summary: No unmeasured recovery yields, unverified biological interactions, or improper
    criticality transfers are claimed; CREATE sidecar and inline history match the
    frozen record.
  target_ids:
  - cmmmech:ammonioborite
  evidence_ids:
  - owner
  - history
  - dossier
  - validation
findings: []
actions: []
summary: 'Ammonioborite passes with limitations: Grandfathered (1933 s.p., Rn 1999)
  (NH4)3B15O20(OH)8(H2O)4 IMA identity (Merlino & Sartori 1971 pentadecaborate structural
  formula), Schaller (1933) Larderello (NH4)2O·5B2O3·5H2O oxide-ratio analysis, cold-water
  sassolite washing, and negative 20-30 C synthesis trials are supported with zero
  fabricated processing mechanisms.'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes at base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.'
- No biological processing or pilot-scale extraction yield is reported in the inspected
  primary sources; unstated process parameters remain null.
notes:
- All primary-source PDFs and authority documents were visually inspected in full
  before record creation.
related_reviews: []
```
