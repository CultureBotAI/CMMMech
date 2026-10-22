# Stage 4 record review: cmmmech:phosphogypsum (Phosphogypsum)

- Review: 20261022T025808Z-phosphogypsum-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T02:52:00Z
- Finished UTC: 2026-10-22T02:58:08Z
- Reviewer: antigravity / cmmmech-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Reviewed data/records/phosphogypsum.yaml (cmmmech:phosphogypsum) at commit 4d878383c92b44876df3bf166d96637c7581a59e following Stage 3 UniProtKB grounding and PR #790 remediation. Verified both Gluconobacter oxydans (NCBITaxon:442) rare-earth bioleaching mechanisms (spent_medium_synthetic_pg_leaching from Antonick et al. 2019 DOI:10.1016/j.jct.2018.12.034 and culture_associated_xifeng_pg_release from Zhang et al. 2025 DOI:10.3390/molecules30030674), causal graph gluconobacter_synthetic_pg_leaching_graph, and both verified Swiss-Prot protein examples in Gluconobacter oxydans 621H (NCBITaxon:290633, UP000006375): UniProtKB:P27175 (DHG_GLUOX, gdh, Quinoprotein glucose dehydrogenase, EC:1.1.5.2) and UniProtKB:Q9L3B2 (PQQC_GLUOX, pqqC, Pyrroloquinoline-quinone synthase, EC:1.3.3.11) synchronized across mechanisms and causal_graphs. Zero open findings.

## Scope And Provenance

Single-record Stage 4 audit of cmmmech:phosphogypsum after Stage 3 UniProtKB protein grounding.

Selection: data/records/phosphogypsum.yaml at 4d878383c92b44876df3bf166d96637c7581a59e
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 4d878383c92b44876df3bf166d96637c7581a59e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:phosphogypsum | data/records/phosphogypsum.yaml | maintained | Phosphogypsum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate phosphogypsum.yaml | passed | True | cmmmech:phosphogypsum | data/records/phosphogypsum.yaml passes LinkML structural and semantic validation with 0 errors. |

## Scientific And Domain Assessments

### Phosphogypsum Gluconobacter oxydans REE-bioleaching mechanisms, causal graph, and UniProtKB groundings

graph: supported. Targets: cmmmech:phosphogypsum.

All nodes, edges, and Swiss-Prot protein examples (UniProtKB:P27175 DHG_GLUOX / gdh and UniProtKB:Q9L3B2 PQQC_GLUOX / pqqC in Gluconobacter oxydans 621H NCBITaxon:290633) are verified against primary literature (DOI:10.1016/j.jct.2018.12.034 and DOI:10.3390/molecules30030674) and live UniProtKB entries.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-phosphogypsum-file | data/records/phosphogypsum.yaml; lines 1-236 | supports | Verified mechanisms (spent_medium_synthetic_pg_leaching, culture_associated_xifeng_pg_release), causal_graphs (gluconobacter_synthetic_pg_leaching_graph), and synchronized Swiss-Prot protein_examples (UniProtKB:P27175, UniProtKB:Q9L3B2) plus history sidecars. |
| ev-phosphogypsum-doi-antonick | DOI:10.1016/j.jct.2018.12.034; Antonick et al. 2019 J. Chem. Thermodyn. 132:491-496 | supports | Supports gluconic-acid biolixiviant leaching of rare earth elements from synthetic phosphogypsum by Gluconobacter oxydans. |
| ev-phosphogypsum-doi-zhang | DOI:10.3390/molecules30030674; Zhang et al. 2025 Molecules 30(3):674 | supports | Supports culture-associated organic-acid bioleaching of rare earth elements from Xifeng phosphogypsum by Gluconobacter oxydans. |

## Limits And Additional Notes


## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025808Z-phosphogypsum-stage4-record-review
title: 'Stage 4 record review: cmmmech:phosphogypsum (Phosphogypsum)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-22T02:52:00Z'
finished_at: '2026-10-22T02:58:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Reviewed data/records/phosphogypsum.yaml (cmmmech:phosphogypsum) at commit
  4d878383c92b44876df3bf166d96637c7581a59e following Stage 3 UniProtKB grounding and
  PR #790 remediation. Verified both Gluconobacter oxydans (NCBITaxon:442) rare-earth
  bioleaching mechanisms (spent_medium_synthetic_pg_leaching from Antonick et al.
  2019 DOI:10.1016/j.jct.2018.12.034 and culture_associated_xifeng_pg_release from
  Zhang et al. 2025 DOI:10.3390/molecules30030674), causal graph gluconobacter_synthetic_pg_leaching_graph,
  and both verified Swiss-Prot protein examples in Gluconobacter oxydans 621H (NCBITaxon:290633,
  UP000006375): UniProtKB:P27175 (DHG_GLUOX, gdh, Quinoprotein glucose dehydrogenase,
  EC:1.1.5.2) and UniProtKB:Q9L3B2 (PQQC_GLUOX, pqqC, Pyrroloquinoline-quinone synthase,
  EC:1.3.3.11) synchronized across mechanisms and causal_graphs. Zero open findings.'
reviewer:
  identity: antigravity / cmmmech-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Stage 4 record_review (.claude/skills/review-yaml-record/SKILL.md)
    against frozen commit 4d878383c92b44876df3bf166d96637c7581a59e.
source:
  git_revision: 4d878383c92b44876df3bf166d96637c7581a59e
  state: git_commit
  inputs:
  - path: data/records/phosphogypsum.yaml
    sha256: 5a1074dea15771196b6a2ebddf655da3dbb2ce9dd3bab2ee6c5d20e5ef78540a
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:phosphogypsum
  selection: data/records/phosphogypsum.yaml at 4d878383c92b44876df3bf166d96637c7581a59e
  description: Single-record Stage 4 audit of cmmmech:phosphogypsum after Stage 3
    UniProtKB protein grounding.
targets:
- target_id: cmmmech:phosphogypsum
  path: data/records/phosphogypsum.yaml
  kind: maintained
  label: Phosphogypsum
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphogypsum.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-phosphogypsum
  name: cmmmech validate phosphogypsum.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/phosphogypsum.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:phosphogypsum
  evidence_ids:
  - ev-phosphogypsum-file
  summary: data/records/phosphogypsum.yaml passes LinkML structural and semantic validation
    with 0 errors.
assessments:
- assessment_id: assess-phosphogypsum-mechanisms-and-proteins
  topic: Phosphogypsum Gluconobacter oxydans REE-bioleaching mechanisms, causal graph,
    and UniProtKB groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:phosphogypsum
  evidence_ids:
  - ev-phosphogypsum-file
  - ev-phosphogypsum-doi-antonick
  - ev-phosphogypsum-doi-zhang
  summary: All nodes, edges, and Swiss-Prot protein examples (UniProtKB:P27175 DHG_GLUOX
    / gdh and UniProtKB:Q9L3B2 PQQC_GLUOX / pqqC in Gluconobacter oxydans 621H NCBITaxon:290633)
    are verified against primary literature (DOI:10.1016/j.jct.2018.12.034 and DOI:10.3390/molecules30030674)
    and live UniProtKB entries.
findings: []
actions: []
evidence:
- evidence_id: ev-phosphogypsum-file
  kind: record_content
  reference: data/records/phosphogypsum.yaml
  locator: lines 1-236
  accessed_at: '2026-10-22T02:58:08Z'
  support: supports
  summary: Verified mechanisms (spent_medium_synthetic_pg_leaching, culture_associated_xifeng_pg_release),
    causal_graphs (gluconobacter_synthetic_pg_leaching_graph), and synchronized Swiss-Prot
    protein_examples (UniProtKB:P27175, UniProtKB:Q9L3B2) plus history sidecars.
- evidence_id: ev-phosphogypsum-doi-antonick
  kind: primary_source
  reference: DOI:10.1016/j.jct.2018.12.034
  locator: Antonick et al. 2019 J. Chem. Thermodyn. 132:491-496
  accessed_at: '2026-10-22T02:58:08Z'
  support: supports
  summary: Supports gluconic-acid biolixiviant leaching of rare earth elements from
    synthetic phosphogypsum by Gluconobacter oxydans.
- evidence_id: ev-phosphogypsum-doi-zhang
  kind: primary_source
  reference: DOI:10.3390/molecules30030674
  locator: Zhang et al. 2025 Molecules 30(3):674
  accessed_at: '2026-10-22T02:58:08Z'
  support: supports
  summary: Supports culture-associated organic-acid bioleaching of rare earth elements
    from Xifeng phosphogypsum by Gluconobacter oxydans.
limitations: []
notes: []
```
