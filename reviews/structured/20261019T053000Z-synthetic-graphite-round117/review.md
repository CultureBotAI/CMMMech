# Scientific review of synthetic-graphite

- Review: 20261019T053000Z-synthetic-graphite-round117
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-19T05:26:00Z
- Finished UTC: 2026-10-19T05:30:00Z
- Reviewer: antigravity / round117-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Synthetic Graphite passes with limitations: Synthetic graphite commodity boundary, DOE 2023 energy criticality, 231,000 t US 2021 production, and 2,500-3,000 C graphitization of calcined petroleum coke and coal-tar pitch are supported while keeping natural graphite distinct.

## Scope And Provenance

Complete frozen working-tree record data/records/synthetic-graphite.yaml, canonical CREATE history sidecar history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml, and primary-source evidence boundaries.

Selection: Targeted structured review of newly curated Round 117 CMM record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:synthetic-graphite | data/records/synthetic-graphite.yaml | maintained | Synthetic Graphite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:synthetic-graphite | Checked 616 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:synthetic-graphite | Checked 744 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Primary-source identity and evidence boundaries for synthetic-graphite

evidence: supported. Targets: cmmmech:synthetic-graphite.

Synthetic graphite commodity boundary, DOE 2023 energy criticality, 231,000 t US 2021 production, and 2,500-3,000 C graphitization of calcined petroleum coke and coal-tar pitch are supported while keeping natural graphite distinct.

### Provenance, category boundaries, and absence of fabricated claims

provenance: supported. Targets: cmmmech:synthetic-graphite.

No unmeasured recovery yields, unverified biological interactions, or improper criticality transfers are claimed; CREATE sidecar and inline history match the frozen record.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/synthetic-graphite.yaml; Complete frozen working-tree record data/records/synthetic-graphite.yaml | supports | All structured claims, identifiers, relations, and qualification notes match the inspected primary sources. |
| history | history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml; Complete canonical CREATE sidecar history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml | supports | Canonical history sidecar and inline history event accurately record actor, UTC timestamp, and scientific scope. |
| dossier | research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json; Paired Round 117 source investigation dossier research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json | context_only | Documents deduplication, primary-source acquisition hashes, and scope boundaries. |
| ima_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA-CNMNC September 2026 Master List (244 pages visually inspected) | supports | Establishes official mineral species nomenclature, formula, approval status, and commodity vs mineral category boundary. |
| primary_study | https://pubs.usgs.gov/myb/vol1/2021/myb1-2021-graphite.pdf; Complete full-text visual inspection of US DOE 2023 Final Critical Materials List (88 FR 51792, 51797), USGS 2021 Minerals Yearbook Graphite (18 pp.), and USGS MCS 2026 Graphite | supports | Synthetic graphite commodity boundary, DOE 2023 energy criticality, 231,000 t US 2021 production, and 2,500-3,000 C graphitization of calcined petroleum coke and coal-tar pitch are supported while keeping natural graphite distinct. |
| validation | data/records/synthetic-graphite.yaml; Strict schema and history validation across all 616 records and 744 history sidecars | supports | Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s). |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes at base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34.
- No biological processing or pilot-scale extraction yield is reported in the inspected primary sources; unstated process parameters remain null.
- All primary-source PDFs and authority documents were visually inspected in full before record creation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T053000Z-synthetic-graphite-round117
kind: record
repository: CultureBotAI/CMMMech
title: Scientific review of synthetic-graphite
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
  - path: data/records/synthetic-graphite.yaml
    sha256: 3fa93145c452cfbf4bd1a027668d4c51a63a20adb1daaacc0dbad4262e5999b1
    role: target
  - path: history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml
    sha256: 1dc3ba9beecd1107e3f4447c0a2abafa1766523816828789aa14f9cf3d86739d
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
- target_id: cmmmech:synthetic-graphite
  path: data/records/synthetic-graphite.yaml
  label: Synthetic Graphite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/synthetic-graphite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml
    role: canonical_history
scope:
  description: Complete frozen working-tree record data/records/synthetic-graphite.yaml,
    canonical CREATE history sidecar history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml,
    and primary-source evidence boundaries.
  selection: Targeted structured review of newly curated Round 117 CMM record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:synthetic-graphite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/synthetic-graphite.yaml
  locator: Complete frozen working-tree record data/records/synthetic-graphite.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: All structured claims, identifiers, relations, and qualification notes
    match the inspected primary sources.
  snapshot_sha256: 3fa93145c452cfbf4bd1a027668d4c51a63a20adb1daaacc0dbad4262e5999b1
- evidence_id: history
  kind: record_content
  reference: history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml
  locator: Complete canonical CREATE sidecar history/records/synthetic-graphite/2026-10-19T052200Z-antigravity-00117c.yaml
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Canonical history sidecar and inline history event accurately record actor,
    UTC timestamp, and scientific scope.
  snapshot_sha256: 1dc3ba9beecd1107e3f4447c0a2abafa1766523816828789aa14f9cf3d86739d
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
  reference: https://pubs.usgs.gov/myb/vol1/2021/myb1-2021-graphite.pdf
  locator: Complete full-text visual inspection of US DOE 2023 Final Critical Materials
    List (88 FR 51792, 51797), USGS 2021 Minerals Yearbook Graphite (18 pp.), and
    USGS MCS 2026 Graphite
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Synthetic graphite commodity boundary, DOE 2023 energy criticality, 231,000
    t US 2021 production, and 2,500-3,000 C graphitization of calcined petroleum coke
    and coal-tar pitch are supported while keeping natural graphite distinct.
  snapshot_sha256: 4f9f98fca68e8f58c4a297f6734d3ecead402fc3f4ea8337b89637bdeab098bc
- evidence_id: validation
  kind: validation
  reference: data/records/synthetic-graphite.yaml
  locator: Strict schema and history validation across all 616 records and 744 history
    sidecars
  accessed_at: '2026-10-19T05:30:00Z'
  support: supports
  summary: Checked 616 record(s), 0 failed; Checked 744 history record(s), 0 error(s).
  snapshot_sha256: 3fa93145c452cfbf4bd1a027668d4c51a63a20adb1daaacc0dbad4262e5999b1
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 616 record(s); 0 failed.
  target_ids:
  - cmmmech:synthetic-graphite
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
  - cmmmech:synthetic-graphite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: identity_and_evidence
  area: evidence
  topic: Primary-source identity and evidence boundaries for synthetic-graphite
  outcome: supported
  summary: Synthetic graphite commodity boundary, DOE 2023 energy criticality, 231,000
    t US 2021 production, and 2,500-3,000 C graphitization of calcined petroleum coke
    and coal-tar pitch are supported while keeping natural graphite distinct.
  target_ids:
  - cmmmech:synthetic-graphite
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
  - cmmmech:synthetic-graphite
  evidence_ids:
  - owner
  - history
  - dossier
  - validation
findings: []
actions: []
summary: 'Synthetic Graphite passes with limitations: Synthetic graphite commodity
  boundary, DOE 2023 energy criticality, 231,000 t US 2021 production, and 2,500-3,000
  C graphitization of calcined petroleum coke and coal-tar pitch are supported while
  keeping natural graphite distinct.'
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
