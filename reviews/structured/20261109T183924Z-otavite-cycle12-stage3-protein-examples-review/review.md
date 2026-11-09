# Cycle 12 Stage 3 protein_examples scientific review of cmmmech:otavite (Otavite)

- Review: 20261109T183924Z-otavite-cycle12-stage3-protein-examples-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T18:38:54Z
- Finished UTC: 2026-11-09T18:39:24Z
- Reviewer: marcin (antigravity claude-opus-4-6) (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:otavite (Otavite): added UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM, Urease accessory protein UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872) to both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with exact UniProt REST API metadata, qualified supports: partial evidence on yang2026 and uniprot_serratia_ureilytica_ureabc, and canonical history sidecar history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml.

## Scope And Provenance

Single-record scientific and structural review of data/records/otavite.yaml after Cycle 12 Stage 3 protein_examples enrichment.

Selection: Modified record data/records/otavite.yaml in Cycle 12 Stage 3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 58ca607539fede2288c3bc368978e6c8cd086c5a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:otavite | data/records/otavite.yaml | maintained | Otavite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| CMMMech schema and reference validation | passed | True | cmmmech:otavite | uv run cmmmech validate --require-records passed (703 records, 0 failed). |
| CMMMech history sidecar validation | passed | True | cmmmech:otavite | uv run cmmmech validate-history --base main passed with history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml. |

## Scientific And Domain Assessments

### UniProtKB protein_examples grounding and causal-graph node parity

grounding: supported. Targets: cmmmech:otavite.

Verified UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM, Urease accessory protein UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872) in both mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples with identical metadata and supports: partial qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_record | data/records/otavite.yaml | supports | Inspected data/records/otavite.yaml (sha256 a01e9c2d5c3fed37a3d164ee0dc38f9630c8ecc080281bee70d457de5d7fcb77) and history sidecar history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml. |
| ev_uniprot | sources[uniprot_serratia_ureilytica_ureabc] and sources[yang2026] in data/records/otavite.yaml | supports | Live-queried UniProt REST API for UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM, Urease accessory protein UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872) and verified accession, entry_name, entry_status, target_organism, reference_proteome_id, EC/InterPro/Pfam/NCBIfam/GO cross-references, and partial evidence qualification against yang2026. |

## Limits And Additional Notes

- Primary experimental source (yang2026) does not perform single-gene knockout or purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE scope are explicitly preserved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T183924Z-otavite-cycle12-stage3-protein-examples-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 3 protein_examples scientific review of cmmmech:otavite (Otavite)
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
summary: 'Verified Cycle 12 Stage 3 protein_examples enrichment for cmmmech:otavite
  (Otavite): added UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM, Urease accessory protein
  UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872) to both mechanisms[].protein_examples
  and causal_graphs[].nodes[].protein_examples with exact UniProt REST API metadata,
  qualified supports: partial evidence on yang2026 and uniprot_serratia_ureilytica_ureabc,
  and canonical history sidecar history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml.'
source:
  git_revision: 58ca607539fede2288c3bc368978e6c8cd086c5a
  state: git_commit
  inputs:
  - path: data/records/otavite.yaml
    sha256: a01e9c2d5c3fed37a3d164ee0dc38f9630c8ecc080281bee70d457de5d7fcb77
    role: target
  - path: history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml
    sha256: 4990d720c626a37bc1cc081a6c817cf455f31bc1a5d8b249889bcd01ef15351e
    role: context
scope:
  description: Single-record scientific and structural review of data/records/otavite.yaml
    after Cycle 12 Stage 3 protein_examples enrichment.
  selection: Modified record data/records/otavite.yaml in Cycle 12 Stage 3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:otavite
targets:
- target_id: cmmmech:otavite
  path: data/records/otavite.yaml
  label: Otavite
  record_class: CriticalMineralRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/otavite.yaml
    role: record
checks:
- check_id: cmmmech_validate
  name: CMMMech schema and reference validation
  status: passed
  required: true
  summary: uv run cmmmech validate --require-records passed (703 records, 0 failed).
  target_ids:
  - cmmmech:otavite
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
  summary: uv run cmmmech validate-history --base main passed with history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml.
  target_ids:
  - cmmmech:otavite
  command: uv run cmmmech validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_record
evidence:
- evidence_id: ev_record
  kind: record_content
  reference: data/records/otavite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Inspected data/records/otavite.yaml (sha256 a01e9c2d5c3fed37a3d164ee0dc38f9630c8ecc080281bee70d457de5d7fcb77)
    and history sidecar history/records/otavite/2026-11-09T183630Z-marcin-63efad.yaml.
  snapshot_sha256: a01e9c2d5c3fed37a3d164ee0dc38f9630c8ecc080281bee70d457de5d7fcb77
- evidence_id: ev_uniprot
  kind: database
  reference: sources[uniprot_serratia_ureilytica_ureabc] and sources[yang2026] in
    data/records/otavite.yaml
  accessed_at: '2026-11-09T18:39:24Z'
  support: supports
  summary: Live-queried UniProt REST API for UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM,
    Urease accessory protein UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872)
    and verified accession, entry_name, entry_status, target_organism, reference_proteome_id,
    EC/InterPro/Pfam/NCBIfam/GO cross-references, and partial evidence qualification
    against yang2026.
assessments:
- assessment_id: assess_grounding
  area: grounding
  topic: UniProtKB protein_examples grounding and causal-graph node parity
  outcome: supported
  summary: 'Verified UniProtKB:A0ABU0VEJ2 (A0ABU0VEJ2_9GAMM, Urease accessory protein
    UreG, ureG, ORF Q6237_00195, Serratia ureilytica UP001177872) in both mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples with identical metadata and supports:
    partial qualification.'
  target_ids:
  - cmmmech:otavite
  evidence_ids:
  - ev_record
  - ev_uniprot
findings: []
actions: []
limitations:
- 'Primary experimental source (yang2026) does not perform single-gene knockout or
  purified-enzyme assays for the grounded protein example; supports: partial and REPRESENTATIVE_EXAMPLE
  scope are explicitly preserved.'
```
