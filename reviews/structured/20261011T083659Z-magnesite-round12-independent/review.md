# Magnesite independent industrial commodity review, initial finding

- Review: 20261011T083659Z-magnesite-round12-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:34:49.673170Z
- Finished UTC: 2026-10-11T08:36:59Z
- Reviewer: /root/cmm12_aluminium_boron (codex; agent_tool codex) (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Source-defined magnesite/magnesia commodity and dated BGS assessment are supported. One minor source-page error requires correction. Final batch gates remain pending.

## Scope And Provenance

All fields and linked history of one magnesite record.

Selection: Assigned frozen final bytes from seven industrial records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:magnesite | data/records/magnesite.yaml | maintained | magnesite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:magnesite | Reviewer executed validation for seven assigned files:7checked,0failed. |
| Named history validation against trusted base | passed | True | cmmmech:magnesite | Reviewer executed:7historyrecordschecked,0errors. |
| Final batch gates delegated to root | unavailable | True | cmmmech:magnesite | Root final batch gate receipt not yet available; parent baseline307passed3skipped71records83histories is not a final changed-state check. |

## Scientific And Domain Assessments

### Source-defined industrial category

identity: supported. Targets: cmmmech:magnesite.

Broad processed commodity is correctly separated from mineral species, elemental Mg and all Mg compounds. No external identifiers or mechanism are asserted.

### USGS supporting chapter location

evidence: concern. Targets: cmmmech:magnesite.

Locator resolves to Lithium rather than Magnesium Compounds.

## Findings

### F1: USGS locator points to Lithium rather than Magnesium Compounds

minor / open / confirmed; issue key: magnesite-usgs-chapter-locator.

The cited MCS2026 title gives printed118-119/PDF122-123, which are Lithium. The supported crude magnesite and processed magnesia context is printed120-121/PDF124-125. The correct chapter exists in the same cited PDF; the commodity identity and criticality are not invalidated.

## Recommended Actions And Acceptance Checks

### A1

Correct title to printed120-121/PDF124-125 and add actual edit provenance; retain this review and save successor on corrected bytes.

- Read the cited MCS pages and confirm Magnesium Compounds heading and crude magnesite context.
- Validate named record and history; complete delegated final batch gates; save successor review linked to F1.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/magnesite.yaml; All fields, especially sources[1].title; linked CREATE sidecar | partial | Inspected frozen working-tree bytes before assessment. Source title points to pages for Lithium; commodity identity and BGS category remain supported. |
| mcs | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf; Printed118-119/PDF122-123 Lithium; printed120-121/PDF124-125 Magnesium Compounds; independently extracted pages and visually inspected PDF124 | refutes | The frozen record gives the Lithium locator. Magnesium Compounds and the crude magnesite/processed magnesia context are on printed120-121. Reused raw /private/tmp/cmm-round9-graphite-evidence/usgs-mcs2026.pdf rehashed independently. |
| bgs | https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf; Cover; Table11 printed44/PDF48; Appendix HS table printed259/PDF263 (visual inspection); live NORA metadata539735 | supports | Corrected OR/24/059 lists Magnesite and its HS category includes natural carbonate, MgO and sintered/fused magnesia. Cover excludes government-policy status. Reused PDF independently rehashed. |

## Limits And Additional Notes

- Final batch checks have not yet been supplied; this is intentionally partial.
- No microbial mechanism is asserted or accepted; this review does not establish absence of applicable microbial literature.
- Criticality is the BGS/CMIC2024 assessment, expressly not a government-policy assertion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T083659Z-magnesite-round12-independent
kind: record
repository: CultureBotAI/CMMMech
title: Magnesite independent industrial commodity review, initial finding
started_at: '2026-10-11T08:34:49.673170Z'
finished_at: '2026-10-11T08:36:59Z'
reviewer:
  identity: /root/cmm12_aluminium_boron (codex; agent_tool codex)
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from industrial-record curator; authored none
    of the seven targets or their histories. Independently inspected official sources
    and rehashed retained raw PDFs. Same model family and shared workspace; dossier
    used as leads, not as proof.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Source-defined magnesite/magnesia commodity and dated BGS assessment are
  supported. One minor source-page error requires correction. Final batch gates remain
  pending.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: data/records/magnesite.yaml
    sha256: 48c71ab081a88afb6cfbfd447a8c9c45e85324413c2e36172aa2f7f3e56d6ba1
    role: target
  - path: history/records/magnesite/2026-10-11T082911Z-codex-03059a.yaml
    sha256: 30cbab13938a930a5c2a90537591ff7c4984c8e5337dbf3f5fab4a91b914acf4
    role: context
  - path: research/ingests/round12-industrial-minerals-20261011.json
    sha256: 1de9c0f4abcf7e81dce849d71cb52151a20b11347f9568c6569b66d7c7785c9c
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields and linked history of one magnesite record.
  selection: Assigned frozen final bytes from seven industrial records.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:magnesite
  exclusions:
  - target: Other six records and whole literature
    reason: Receive separate per-record observations; no corpus-wide scientific claim.
targets:
- target_id: cmmmech:magnesite
  path: data/records/magnesite.yaml
  label: magnesite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
  record_class: commodity
checks:
- check_id: record
  name: Named record validation
  status: passed
  required: true
  target_ids:
  - cmmmech:magnesite
  summary: Reviewer executed validation for seven assigned files:7checked,0failed.
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/baryte.yaml data/records/fluorspar.yaml data/records/feldspar.yaml
    data/records/magnesite.yaml data/records/phosphate-rock.yaml data/records/potash.yaml
    data/records/sodium-compounds.yaml
  exit_code: 0
- check_id: history
  name: Named history validation against trusted base
  status: passed
  required: true
  target_ids:
  - cmmmech:magnesite
  summary: Reviewer executed:7historyrecordschecked,0errors.
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4 history/records/baryte
    history/records/fluorspar history/records/feldspar history/records/magnesite history/records/phosphate-rock
    history/records/potash history/records/sodium-compounds
  exit_code: 0
- check_id: batch
  name: Final batch gates delegated to root
  status: unavailable
  required: true
  target_ids:
  - cmmmech:magnesite
  summary: Root final batch gate receipt not yet available; parent baseline307passed3skipped71records83histories
    is not a final changed-state check.
  scope_note: Do not interpret this partial observation as completed publication acceptance.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/magnesite.yaml
  locator: All fields, especially sources[1].title; linked CREATE sidecar
  accessed_at: '2026-10-11T08:36:59Z'
  support: partial
  summary: Inspected frozen working-tree bytes before assessment. Source title points
    to pages for Lithium; commodity identity and BGS category remain supported.
- evidence_id: mcs
  kind: authority
  reference: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf
  locator: Printed118-119/PDF122-123 Lithium; printed120-121/PDF124-125 Magnesium
    Compounds; independently extracted pages and visually inspected PDF124
  accessed_at: '2026-10-11T08:36:59Z'
  support: refutes
  summary: The frozen record gives the Lithium locator. Magnesium Compounds and the
    crude magnesite/processed magnesia context are on printed120-121. Reused raw /private/tmp/cmm-round9-graphite-evidence/usgs-mcs2026.pdf
    rehashed independently.
  snapshot_sha256: 595e6e66674236dea40125a03eb1ea6b347f331c0bcf3411a1e77eba53c0d391
- evidence_id: bgs
  kind: authority
  reference: https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf
  locator: Cover; Table11 printed44/PDF48; Appendix HS table printed259/PDF263 (visual
    inspection); live NORA metadata539735
  accessed_at: '2026-10-11T08:36:59Z'
  support: supports
  summary: Corrected OR/24/059 lists Magnesite and its HS category includes natural
    carbonate, MgO and sintered/fused magnesia. Cover excludes government-policy status.
    Reused PDF independently rehashed.
  snapshot_sha256: e5708ffb1080c874cc57f0e20aad8f99aea746977971280434a1cfbb37f28c9e
assessments:
- assessment_id: identity
  area: identity
  topic: Source-defined industrial category
  outcome: supported
  summary: Broad processed commodity is correctly separated from mineral species,
    elemental Mg and all Mg compounds. No external identifiers or mechanism are asserted.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
  - bgs
- assessment_id: locator
  area: evidence
  topic: USGS supporting chapter location
  outcome: concern
  summary: Locator resolves to Lithium rather than Magnesium Compounds.
  target_ids:
  - cmmmech:magnesite
  evidence_ids:
  - record
  - mcs
findings:
- finding_id: F1
  issue_key: magnesite-usgs-chapter-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: USGS locator points to Lithium rather than Magnesium Compounds
  description: The cited MCS2026 title gives printed118-119/PDF122-123, which are
    Lithium. The supported crude magnesite and processed magnesia context is printed120-121/PDF124-125.
    The correct chapter exists in the same cited PDF; the commodity identity and criticality
    are not invalidated.
  target_ids:
  - cmmmech:magnesite
  field_paths:
  - sources[1].title
  evidence_ids:
  - record
  - mcs
  rule_id: primary-source-locator
  native_severity: minor
  normalization_reason: Bounded citation locator error; no change to identity or criticality.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
actions:
- action_id: A1
  description: Correct title to printed120-121/PDF124-125 and add actual edit provenance;
    retain this review and save successor on corrected bytes.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:magnesite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/magnesite.yaml
    role: maintained_record
  acceptance_checks:
  - Read the cited MCS pages and confirm Magnesium Compounds heading and crude magnesite
    context.
  - Validate named record and history; complete delegated final batch gates; save
    successor review linked to F1.
limitations:
- Final batch checks have not yet been supplied; this is intentionally partial.
- No microbial mechanism is asserted or accepted; this review does not establish absence
  of applicable microbial literature.
- Criticality is the BGS/CMIC2024 assessment, expressly not a government-policy assertion.
```
