# Cycle 12 Stage 3 protein_examples scientific review of cmmmech:hematite (Hematite)

- Review: 20261109T183924Z-hematite-cycle12-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T18:38:54Z
- Finished UTC: 2026-11-09T18:39:24Z
- Reviewer: marcin (antigravity claude-opus-4-6) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:hematite (Hematite): added UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2, Stage 0 sporulation protein A, spo0A, ORF BG04_1367, Priestia megaterium NBRC 15308 = ATCC 14581 UP000031829) to both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with exact UniProt REST API metadata, qualified supports: partial evidence on dong_2026 and uniprot_priestia_megaterium_mineral_genes, and canonical history sidecar history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml.

## Scope And Provenance

Single-record scientific and structural review of data/records/hematite.yaml after Cycle 12 Stage 3 protein_examples enrichment.

Selection: Modified record data/records/hematite.yaml in Cycle 12 Stage 3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 58ca607539fede2288c3bc368978e6c8cd086c5a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hematite | data/records/hematite.yaml | maintained | Hematite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CMMMech schema and reference validation | passed | True | cmmmech:hematite | uv run cmmmech validate --require-records passed (703 records, 0 failed). |
| CMMMech history sidecar validation | passed | True | cmmmech:hematite | uv run cmmmech validate-history --base main passed with history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml. |

## Scientific And Domain Assessments

### UniProtKB protein_examples grounding and causal-graph node parity

grounding: supported. Targets: cmmmech:hematite.

Verified UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2, Stage 0 sporulation protein A, spo0A, ORF BG04_1367, Priestia megaterium NBRC 15308 = ATCC 14581 UP000031829) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with identical metadata and supports: partial qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_record | data/records/hematite.yaml | supports | Inspected data/records/hematite.yaml (sha256 af9194eb8ca64a3a361a766ae9a0c7254b37652b075c34ac0358b29e5e3fb57b) and history sidecar history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml. |
| ev_uniprot | sources[uniprot_priestia_megaterium_mineral_genes] and sources[dong_2026] in data/records/hematite.yaml | supports | Live-queried UniProt REST API for UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2, Stage 0 sporulation protein A, spo0A, ORF BG04_1367, Priestia megaterium NBRC 15308 = ATCC 14581 UP000031829) and verified accession, entry_name, entry_status, target_organism, reference_proteome_id, EC/InterPro/Pfam/NCBIfam/GO cross-references, and partial evidence qualification against dong_2026. |

## Limits And Additional Notes

- Primary experimental source (dong_2026) does not perform single-gene knockout or purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE scope are explicitly preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T183924Z-hematite-cycle12-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 3 protein_examples scientific review of cmmmech:hematite (Hematite)
started_at: '2026-11-09T18:38:54Z'
finished_at: '2026-11-09T18:39:24Z'
reviewer:
  identity: marcin (antigravity claude-opus-4-6)
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Post-curation structured review of Cycle 12 Stage 3 protein_examples
    enrichment prior to independent subagent adversarial review.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:hematite
  (Hematite): added UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2, Stage 0 sporulation protein
  A, spo0A, ORF BG04_1367, Priestia megaterium NBRC 15308 = ATCC 14581 UP000031829)
  to both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  with exact UniProt REST API metadata, qualified supports: partial evidence on dong_2026
  and uniprot_priestia_megaterium_mineral_genes, and canonical history sidecar history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml.'
source:
  git_revision: 58ca607539fede2288c3bc368978e6c8cd086c5a
  state: git_commit
  inputs:
  - path: data/records/hematite.yaml
    sha256: af9194eb8ca64a3a361a766ae9a0c7254b37652b075c34ac0358b29e5e3fb57b
    role: target
  - path: history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml
    sha256: 62f523ea8adf8ebf2c6c5d4bae1149a64376a0f8c4a29c580d2c919c9b8bb209
    role: context
scope:
  description: Single-record scientific and structural review of data/records/hematite.yaml
    after Cycle 12 Stage 3 protein_examples enrichment.
  selection: Modified record data/records/hematite.yaml in Cycle 12 Stage 3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hematite
targets:
- target_id: cmmmech:hematite
  path: data/records/hematite.yaml
  label: Hematite
  record_class: CriticalMineralRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hematite.yaml
    role: record
checks:
- check_id: cmmmech_validate
  name: CMMMech schema and reference validation
  status: passed
  required: true
  summary: uv run cmmmech validate --require-records passed (703 records, 0 failed).
  target_ids:
  - cmmmech:hematite
  command: uv run cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
  - ev_uniprot
- check_id: cmmmech_validate_history
  name: CMMMech history sidecar validation
  status: passed
  required: true
  summary: uv run cmmmech validate-history --base main passed with history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml.
  target_ids:
  - cmmmech:hematite
  command: uv run cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
evidence:
- evidence_id: ev_record
  kind: record_content
  reference: data/records/hematite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Inspected data/records/hematite.yaml (sha256 af9194eb8ca64a3a361a766ae9a0c7254b37652b075c34ac0358b29e5e3fb57b)
    and history sidecar history/records/hematite/2026-11-09T183630Z-marcin-3f77bb.yaml.
  snapshot_sha256: af9194eb8ca64a3a361a766ae9a0c7254b37652b075c34ac0358b29e5e3fb57b
- evidence_id: ev_uniprot
  kind: database
  reference: sources[uniprot_priestia_megaterium_mineral_genes] and sources[dong_2026]
    in data/records/hematite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Live-queried UniProt REST API for UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2,
    Stage 0 sporulation protein A, spo0A, ORF BG04_1367, Priestia megaterium NBRC
    15308 = ATCC 14581 UP000031829) and verified accession, entry_name, entry_status,
    target_organism, reference_proteome_id, EC/InterPro/Pfam/NCBIfam/GO cross-references,
    and partial evidence qualification against dong_2026.
assessments:
- assessment_id: assess_grounding
  area: grounding
  topic: UniProtKB protein_examples grounding and causal-graph node parity
  outcome: supported
  summary: 'Verified UniProtKB:A0A0B6ANB3 (A0A0B6ANB3_PRIM2, Stage 0 sporulation protein
    A, spo0A, ORF BG04_1367, Priestia megaterium NBRC 15308 = ATCC 14581 UP000031829)
    in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    with identical metadata and supports: partial qualification.'
  target_ids:
  - cmmmech:hematite
  evidence_ids:
  - ev_record
  - ev_uniprot
findings: []
actions: []
limitations:
- 'Primary experimental source (dong_2026) does not perform single-gene knockout or
  purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE
  scope are explicitly preserved.'
```
