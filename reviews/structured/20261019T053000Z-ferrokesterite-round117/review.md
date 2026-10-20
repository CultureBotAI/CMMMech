# Scientific review of ferrokesterite

- Review: 20261019T053000Z-ferrokesterite-round117
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-19T05:26:00Z
- Finished UTC: 2026-10-19T05:30:00Z
- Reviewer: antigravity / round117-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Ferrokesterite passes with limitations: IMA1985-012 Cu2(Fe,Zn)SnS4 identity, I-4 tetragonal stannite-group symmetry (a = 5.433(36), c = 10.884(89) A, Z = 2) differentiating low-T ferrokesterite from high-T I-42m stannite, and Cligga Mine cotype GSC 65048 / BM 1984, 844 WDS composition are supported.

## Scope And Provenance

Complete frozen working-tree record data/records/ferrokesterite.yaml, canonical CREATE history sidecar history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml, and primary-source evidence boundaries.

Selection: Targeted structured review of newly curated Round 117 CMM record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ferrokesterite | data/records/ferrokesterite.yaml | maintained | Ferrokesterite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:ferrokesterite | Checked 616 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:ferrokesterite | Checked 744 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Primary-source identity and evidence boundaries for ferrokesterite

evidence: supported. Targets: cmmmech:ferrokesterite.

IMA1985-012 Cu2(Fe,Zn)SnS4 identity, I-4 tetragonal stannite-group symmetry (a = 5.433(36), c = 10.884(89) A, Z = 2) differentiating low-T ferrokesterite from high-T I-42m stannite, and Cligga Mine cotype GSC 65048 / BM 1984, 844 WDS composition are supported.

### Provenance, category boundaries, and absence of fabricated claims

provenance: supported. Targets: cmmmech:ferrokesterite.

No unmeasured recovery yields, unverified biological interactions, or improper criticality transfers are claimed; CREATE sidecar and inline history match the frozen record.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ferrokesterite.yaml; Complete frozen working-tree record data/records/ferrokesterite.yaml | supports | All structured claims, identifiers, relations, and qualification notes match the inspected primary sources. |
| history | history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml; Complete canonical CREATE sidecar history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml | supports | Canonical history sidecar and inline history event accurately record actor, UTC timestamp, and scientific scope. |
| dossier | research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json; Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json | context_only | Documents deduplication, primary-source acquisition hashes, and scope boundaries. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Establishes official mineral species nomenclature, formula, approval status, and commodity vs mineral category boundary. |
| primary_study | https://rruff.info/rruff_1.0/uploads/CM27_673.pdf; Complete full-text visual inspection of CM 27 (1989) 673-688 (16 pp.) and IMA September 2026 Master List (IMA1985-012) | supports | IMA1985-012 Cu2(Fe,Zn)SnS4 identity, I-4 tetragonal stannite-group symmetry (a = 5.433(36), c = 10.884(89) A, Z = 2) differentiating low-T ferrokesterite from high-T I-42m stannite, and Cligga Mine cotype GSC 65048 / BM 1984, 844 WDS composition are supported. |
| validation | data/records/ferrokesterite.yaml; Strict schema and history validation across all 616 records and 744 history sidecars | supports | Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
- No biological processing or pilot-scale extraction yield is reported in the inspected primary sources; unstated process parameters remain null.
- All primary-source PDFs and authority documents were visually inspected in full before record creation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T053000Z-ferrokesterite-round117
kind: record
repository: CultureBotAI/CMMMech
title: Scientific review of ferrokesterite
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
  - path: data/records/ferrokesterite.yaml
    sha256: 6437798cc26e2fa214de18dd4d90115dd9ae16a5536ffa5a0fa2f6b8ac35797a
    role: target
  - path: history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml
    sha256: 457750ae39e448da95b3918357fa357f9aaf9efd953f98a26d97ff53ae379b59
    role: context
  - path: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
    sha256: f2c03dc0aab6800e9233d6d465e49b5ed80f4cc546b2d87c03ec891f699b750b
    role: context
  - path: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.md
    sha256: edefffa05d10ba6d36a2f7a396c8b6eceb50290b6c2964414240ca120015535d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
targets:
- target_id: cmmmech:ferrokesterite
  path: data/records/ferrokesterite.yaml
  label: Ferrokesterite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrokesterite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml
    role: canonical_history
scope:
  description: Complete frozen working-tree record data/records/ferrokesterite.yaml,
    canonical CREATE history sidecar history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml,
    and primary-source evidence boundaries.
  selection: Targeted structured review of newly curated Round 117 CMM record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ferrokesterite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ferrokesterite.yaml
  locator: Complete frozen working-tree record data/records/ferrokesterite.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: All structured claims, identifiers, relations, and qualification notes
    match the inspected primary sources.
  snapshot_sha256: 6437798cc26e2fa214de18dd4d90115dd9ae16a5536ffa5a0fa2f6b8ac35797a
- evidence_id: history
  kind: record_content
  reference: history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml
  locator: Complete canonical CREATE sidecar history/records/ferrokesterite/2026-10-19T052200Z-antigravity-001173.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Canonical history sidecar and inline history event accurately record actor,
    UTC timestamp, and scientific scope.
  snapshot_sha256: 457750ae39e448da95b3918357fa357f9aaf9efd953f98a26d97ff53ae379b59
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
  locator: Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json
  accessed_at: '2026-10-19T05:30:00Z'
  support: context_only
  summary: Documents deduplication, primary-source acquisition hashes, and scope boundaries.
  snapshot_sha256: f2c03dc0aab6800e9233d6d465e49b5ed80f4cc546b2d87c03ec891f699b750b
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
  reference: https://rruff.info/rruff_1.0/uploads/CM27_673.pdf
  locator: Complete full-text visual inspection of CM 27 (1989) 673-688 (16 pp.) and
    IMA September 2026 Master List (IMA1985-012)
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: IMA1985-012 Cu2(Fe,Zn)SnS4 identity, I-4 tetragonal stannite-group symmetry
    (a = 5.433(36), c = 10.884(89) A, Z = 2) differentiating low-T ferrokesterite
    from high-T I-42m stannite, and Cligga Mine cotype GSC 65048 / BM 1984, 844 WDS
    composition are supported.
  snapshot_sha256: ffdf661f44c46b494d666a353956dba432805f834707f5a50145d31a334ae616
- evidence_id: validation
  kind: validation
  reference: data/records/ferrokesterite.yaml
  locator: Strict schema and history validation across all 616 records and 744 history
    sidecars
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s).
  snapshot_sha256: 6437798cc26e2fa214de18dd4d90115dd9ae16a5536ffa5a0fa2f6b8ac35797a
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 616 record(s); 0 failed.
  target_ids:
  - cmmmech:ferrokesterite
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
  - cmmmech:ferrokesterite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_evidence
  area: evidence
  topic: Primary-source identity and evidence boundaries for ferrokesterite
  outcome: supported
  summary: IMA1985-012 Cu2(Fe,Zn)SnS4 identity, I-4 tetragonal stannite-group symmetry
    (a = 5.433(36), c = 10.884(89) A, Z = 2) differentiating low-T ferrokesterite
    from high-T I-42m stannite, and Cligga Mine cotype GSC 65048 / BM 1984, 844 WDS
    composition are supported.
  target_ids:
  - cmmmech:ferrokesterite
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
  - cmmmech:ferrokesterite
  evidence_ids:
  - owner
  - history
  - dossier
  - validation
findings: []
actions: []
summary: 'Ferrokesterite passes with limitations: IMA1985-012 Cu2(Fe,Zn)SnS4 identity,
  I-4 tetragonal stannite-group symmetry (a = 5.433(36), c = 10.884(89) A, Z = 2)
  differentiating low-T ferrokesterite from high-T I-42m stannite, and Cligga Mine
  cotype GSC 65048 / BM 1984, 844 WDS composition are supported.'
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
