# Scientific review of piilonenite-nd

- Review: 20261019T053000Z-piilonenite-nd-round117
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-19T05:26:00Z
- Finished UTC: 2026-10-19T05:30:00Z
- Reviewer: antigravity / round117-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Piilonenite-(Nd) passes with limitations: IMA:2025-031 (IMA Master List 2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium carbonate identity and chemical analogy to adamsite-(Y) and shomiokite-(Y) are supported without inheriting REE criticality or attributing unverified crystal-structure refinements.

## Scope And Provenance

Complete frozen working-tree record data/records/piilonenite-nd.yaml, canonical CREATE history sidecar history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml, and primary-source evidence boundaries.

Selection: Targeted structured review of newly curated Round 117 CMM record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:piilonenite-nd | data/records/piilonenite-nd.yaml | maintained | Piilonenite-(Nd) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:piilonenite-nd | Checked 616 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:piilonenite-nd | Checked 744 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Primary-source identity and evidence boundaries for piilonenite-nd

evidence: supported. Targets: cmmmech:piilonenite-nd.

IMA:2025-031 (IMA Master List 2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium carbonate identity and chemical analogy to adamsite-(Y) and shomiokite-(Y) are supported without inheriting REE criticality or attributing unverified crystal-structure refinements.

### Provenance, category boundaries, and absence of fabricated claims

provenance: supported. Targets: cmmmech:piilonenite-nd.

No unmeasured recovery yields, unverified biological interactions, or improper criticality transfers are claimed; CREATE sidecar and inline history match the frozen record.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/piilonenite-nd.yaml; Complete frozen working-tree record data/records/piilonenite-nd.yaml | supports | All structured claims, identifiers, relations, and qualification notes match the inspected primary sources. |
| history | history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml; Complete canonical CREATE sidecar history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml | supports | Canonical history sidecar and inline history event accurately record actor, UTC timestamp, and scientific scope. |
| dossier | research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json; Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json | context_only | Documents deduplication, primary-source acquisition hashes, and scope boundaries. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Establishes official mineral species nomenclature, formula, approval status, and commodity vs mineral category boundary. |
| primary_study | https://rruff.info/rruff_1.0/uploads/CM38_1457.pdf; IMA September 2026 Master List (p. 172, IMA:2025-031 / 2025-031b) and comparator CM 38 (2000) 1457-1466 (10 pp.) | supports | IMA:2025-031 (IMA Master List 2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium carbonate identity and chemical analogy to adamsite-(Y) and shomiokite-(Y) are supported without inheriting REE criticality or attributing unverified crystal-structure refinements. |
| validation | data/records/piilonenite-nd.yaml; Strict schema and history validation across all 616 records and 744 history sidecars | supports | Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
- No biological processing or pilot-scale extraction yield is reported in the inspected primary sources; unstated process parameters remain null.
- All primary-source PDFs and authority documents were visually inspected in full before record creation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T053000Z-piilonenite-nd-round117
kind: record
repository: CultureBotAI/CMMMech
title: Scientific review of piilonenite-nd
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
  - path: data/records/piilonenite-nd.yaml
    sha256: ea51cc5ca1cfa3a9493accd3be16c32e3c22b1a9d4030b3155a703703c1fb9d2
    role: target
  - path: history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml
    sha256: 22ac08ba60389e59474f1560ef877a845399aad4f03edd1d999a4bed9d9815c9
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
- target_id: cmmmech:piilonenite-nd
  path: data/records/piilonenite-nd.yaml
  label: Piilonenite-(Nd)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/piilonenite-nd.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml
    role: canonical_history
scope:
  description: Complete frozen working-tree record data/records/piilonenite-nd.yaml,
    canonical CREATE history sidecar history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml,
    and primary-source evidence boundaries.
  selection: Targeted structured review of newly curated Round 117 CMM record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:piilonenite-nd
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/piilonenite-nd.yaml
  locator: Complete frozen working-tree record data/records/piilonenite-nd.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: All structured claims, identifiers, relations, and qualification notes
    match the inspected primary sources.
  snapshot_sha256: ea51cc5ca1cfa3a9493accd3be16c32e3c22b1a9d4030b3155a703703c1fb9d2
- evidence_id: history
  kind: record_content
  reference: history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml
  locator: Complete canonical CREATE sidecar history/records/piilonenite-nd/2026-10-19T052200Z-antigravity-00117e.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Canonical history sidecar and inline history event accurately record actor,
    UTC timestamp, and scientific scope.
  snapshot_sha256: 22ac08ba60389e59474f1560ef877a845399aad4f03edd1d999a4bed9d9815c9
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
  reference: https://rruff.info/rruff_1.0/uploads/CM38_1457.pdf
  locator: IMA September 2026 Master List (p. 172, IMA:2025-031 / 2025-031b) and comparator
    CM 38 (2000) 1457-1466 (10 pp.)
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: IMA:2025-031 (IMA Master List 2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium
    carbonate identity and chemical analogy to adamsite-(Y) and shomiokite-(Y) are
    supported without inheriting REE criticality or attributing unverified crystal-structure
    refinements.
  snapshot_sha256: b222d739191160a36c07de3a8430a086decacf420b13d4a894c2ff6c1c1bebbe
- evidence_id: validation
  kind: validation
  reference: data/records/piilonenite-nd.yaml
  locator: Strict schema and history validation across all 616 records and 744 history
    sidecars
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s).
  snapshot_sha256: ea51cc5ca1cfa3a9493accd3be16c32e3c22b1a9d4030b3155a703703c1fb9d2
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 616 record(s); 0 failed.
  target_ids:
  - cmmmech:piilonenite-nd
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
  - cmmmech:piilonenite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_evidence
  area: evidence
  topic: Primary-source identity and evidence boundaries for piilonenite-nd
  outcome: supported
  summary: IMA:2025-031 (IMA Master List 2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium
    carbonate identity and chemical analogy to adamsite-(Y) and shomiokite-(Y) are
    supported without inheriting REE criticality or attributing unverified crystal-structure
    refinements.
  target_ids:
  - cmmmech:piilonenite-nd
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
  - cmmmech:piilonenite-nd
  evidence_ids:
  - owner
  - history
  - dossier
  - validation
findings: []
actions: []
summary: 'Piilonenite-(Nd) passes with limitations: IMA:2025-031 (IMA Master List
  2025-031b) NaNd(CO3)2(H2O)3 hydrated sodium-neodymium carbonate identity and chemical
  analogy to adamsite-(Y) and shomiokite-(Y) are supported without inheriting REE
  criticality or attributing unverified crystal-structure refinements.'
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
