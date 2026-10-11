# Independent scientific review of Spent lithium-ion battery black mass

- Review: 20261011T090808Z-battery-black-mass-round13-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:59:23Z
- Finished UTC: 2026-10-11T09:08:08Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supported material identity and bounded evidence; no actionable findings. Source-specific uncertainty is preserved and no unsupported criticality or industrial-recovery claim is introduced.

## Scope And Provenance

All fields, source claims and linked history of one exact working-tree record.

Selection: Assigned new resource/commodity target; complete per-record review, not a corpus-wide literature census.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14ceff0da3e19d6d36426d33f4cf577b8e64760f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:battery-black-mass | data/records/battery-black-mass.yaml | maintained | Spent lithium-ion battery black mass |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:battery-black-mass | Reviewer executed: 4 records, 0 failed; terminal 0; target included. |
| check final batch gate | passed | True | cmmmech:battery-black-mass | Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-check.log; 101 records / 116 histories; just check: 307 passed, 3 skipped. |
| require final batch gate | passed | True | cmmmech:battery-black-mass | Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-require.log; 101 records / 116 histories; just check: 307 passed, 3 skipped. |
| history final batch gate | passed | True | cmmmech:battery-black-mass | Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-history.log; 101 records / 116 histories; just check: 307 passed, 3 skipped. |

## Scientific And Domain Assessments

### Material boundary, identifiers and criticality omission

identity: supported. Targets: cmmmech:battery-black-mass.

A heterogeneous powder stream produced by pretreatment of spent lithium-ion batteries. Composition depends on battery chemistry and processing; the curated experiment used nickel-manganese-cobalt battery material after discharging, dismantling, thermal treatment, crushing and sorting. This secondary resource is distinct from whole batteries, an individual cathode compound, cobalt or lithium elements, and recovered battery-grade products. Constituent-element criticality is not inherited by this mixed feed.

### Primary claim verification and inference limits

evidence: supported. Targets: cmmmech:battery-black-mass.

The stated evidence supports the deliberately bounded record. No post-adaptation taxonomic authentication or member-specific causal controls. Different abiotic pH/iron chemistry and unresolved adaptation/feed inventories preclude quantitative whole-process recovery. Supplement-only sequence claims not accepted; reviewer read main paper and noted curator404 supplement route, did not independently acquire the workbook.

### Actual changes and retained source base

provenance: supported. Targets: cmmmech:battery-black-mass.

New CREATE sidecar and distinct inline event describe present curation. Trusted base is merged main 14ceff0; no prior records/history/reviews edited. Exact current target hash verified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/battery-black-mass.yaml; Complete target and linked CREATE sidecars, exact inspect capture before assessment | supports | Independently read frozen target and linked history: actual GPT-6/codex attribution, matching target and separate inline event. Current bytes match inspected and gated SHA. No authoring or record edits by reviewer. |
| paper | https://doi.org/10.3389/fmicb.2024.1347072; Sections 2.1–2.7 and3.1–3.3; Tables 1–2; Figures 4–6 | supports | Fresh publisher full HTML and Figure 5 pixels independently read. Pretreated NMC powder, living adapted lake-sediment enrichment, seven-day preculture plus seven-day1% w/v leach, sterile and unadapted comparisons support only condition-specific mobilization. Original enrichment taxonomy does not establish post-adaptation community composition. |
| quantity | https://www.frontiersin.org/files/Articles/1347072/xml-images/fmicb-15-1347072-g005.webp; Figure 5 cobalt bars versus Table1 and Methods 2.5 | supports | Visually confirmed adapted-Co near2 g/L versus nominal1.45 g/L inventory from145 g/kg at10 g/L feed. Table 2 also mismatches stated feed equivalents. Day-zero subtraction is reported but does not supply a reconciled mass balance. Record explicitly withholds complete-recovery and corrected-yield claims. |
| search | /private/tmp/cmm-round13-review-dedup.txt; 572 matching lines; local corpus and named raw roots plus first web query windows | context_only | Ignored-inclusive search locates existing element records and source dossiers; new roots are distinct feeds or a broader explicitly overlapping commodity. Battery/red-mud sources reuse existing element experiments, not independent replications. Exact DOI correction/retraction queries surfaced no applicable notice in first returned results; this is bounded, not exhaustive. |
| gates | /private/tmp/cmm-round13-gate-receipts.json; All three terminal-zero commands;check/require/history logs and gated hash manifest | supports | Root executed 307 passed, 3 skipped in 76.91 s; 101 records, 0 failed; 116 histories, 0 errors. Exact target bytes unchanged since gates. These offline checks do not prove source accuracy. |

## Limits And Additional Notes

- No post-adaptation taxonomic authentication or member-specific causal controls.
- Different abiotic pH/iron chemistry and unresolved adaptation/feed inventories preclude quantitative whole-process recovery.
- Supplement-only sequence claims not accepted; reviewer read main paper and noted curator404 supplement route, did not independently acquire the workbook.
- Full-text access limits and bounded source/correction search are explicit; no global absence or exhaustiveness claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T090808Z-battery-black-mass-round13-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Spent lithium-ion battery black mass
started_at: '2026-10-11T08:59:23Z'
finished_at: '2026-10-11T09:08:08Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate agents authored these records and histories. Root independently
    inspected primary text/figures/authorities and exact target bytes; communicated
    source limitations before curation but did not author or edit the records. Root
    also owns batch validation and publication documentation; independence is record-author
    separation, not organizational separation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supported material identity and bounded evidence; no actionable findings.
  Source-specific uncertainty is preserved and no unsupported criticality or industrial-recovery
  claim is introduced.
source:
  git_revision: 14ceff0da3e19d6d36426d33f4cf577b8e64760f
  state: working_tree
  inputs:
  - path: data/records/battery-black-mass.yaml
    sha256: 0e0e045b59f2728e9cdfd2aabcec3848bad611d60dc18599cccf3a824f687a28
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/battery-black-mass/2026-10-11T090220Z-codex-601df7.yaml
    sha256: a0e204f9206a02f080ddff9af8e1246c8825222b7e3a68a958291368a459cc35
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, source claims and linked history of one exact working-tree
    record.
  selection: Assigned new resource/commodity target; complete per-record review, not
    a corpus-wide literature census.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:battery-black-mass
  exclusions:
  - target: Uncurated literature and unrelated records
    reason: Existing records checked only for identity and shared experiment boundaries;
      no claim of fresh comprehensive re-review.
targets:
- target_id: cmmmech:battery-black-mass
  path: data/records/battery-black-mass.yaml
  label: Spent lithium-ion battery black mass
  kind: maintained
  record_class: secondary_resource
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/battery-black-mass.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/battery-black-mass.yaml data/records/bauxite-residue.yaml
    data/records/phosphogypsum.yaml data/records/metallurgical-coal.yaml
  status: passed
  required: true
  summary: 'Reviewer executed: 4 records, 0 failed; terminal 0; target included.'
  target_ids:
  - cmmmech:battery-black-mass
  exit_code: 0
  expected_exit_code: 0
- check_id: check
  name: check final batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-check.log;
    101 records / 116 histories; just check: 307 passed, 3 skipped.'
  target_ids:
  - cmmmech:battery-black-mass
  exit_code: 0
  expected_exit_code: 0
- check_id: require
  name: require final batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-require.log;
    101 records / 116 histories; just check: 307 passed, 3 skipped.'
  target_ids:
  - cmmmech:battery-black-mass
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: history final batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 14ceff0da3e19d6d36426d33f4cf577b8e64760f
  status: passed
  required: true
  summary: 'Root reviewer executed and read actual terminal receipt/log /private/tmp/cmm-round13-history.log;
    101 records / 116 histories; just check: 307 passed, 3 skipped.'
  target_ids:
  - cmmmech:battery-black-mass
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/battery-black-mass.yaml
  locator: Complete target and linked CREATE sidecars, exact inspect capture before
    assessment
  accessed_at: '2026-10-11T09:08:08Z'
  support: supports
  summary: 'Independently read frozen target and linked history: actual GPT-6/codex
    attribution, matching target and separate inline event. Current bytes match inspected
    and gated SHA. No authoring or record edits by reviewer.'
  snapshot_sha256: 0e0e045b59f2728e9cdfd2aabcec3848bad611d60dc18599cccf3a824f687a28
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1347072
  locator: Sections 2.1–2.7 and3.1–3.3; Tables 1–2; Figures 4–6
  accessed_at: '2026-10-11T09:08:08Z'
  support: supports
  summary: Fresh publisher full HTML and Figure 5 pixels independently read. Pretreated
    NMC powder, living adapted lake-sediment enrichment, seven-day preculture plus
    seven-day1% w/v leach, sterile and unadapted comparisons support only condition-specific
    mobilization. Original enrichment taxonomy does not establish post-adaptation
    community composition.
  snapshot_sha256: f1865876cfd586000908f4ba1ef7986347fe8d7272a9ed7432b50a343e93ef9f
- evidence_id: quantity
  kind: primary_source
  reference: https://www.frontiersin.org/files/Articles/1347072/xml-images/fmicb-15-1347072-g005.webp
  locator: Figure 5 cobalt bars versus Table1 and Methods 2.5
  accessed_at: '2026-10-11T09:08:08Z'
  support: supports
  summary: Visually confirmed adapted-Co near2 g/L versus nominal1.45 g/L inventory
    from145 g/kg at10 g/L feed. Table 2 also mismatches stated feed equivalents. Day-zero
    subtraction is reported but does not supply a reconciled mass balance. Record
    explicitly withholds complete-recovery and corrected-yield claims.
  snapshot_sha256: 5837d3dd2a582ff54d832e9fb07f56de558bffeef47c8833772333277242ca26
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round13-review-dedup.txt
  locator: 572 matching lines; local corpus and named raw roots plus first web query
    windows
  accessed_at: '2026-10-11T09:08:08Z'
  support: context_only
  summary: Ignored-inclusive search locates existing element records and source dossiers;
    new roots are distinct feeds or a broader explicitly overlapping commodity. Battery/red-mud
    sources reuse existing element experiments, not independent replications. Exact
    DOI correction/retraction queries surfaced no applicable notice in first returned
    results; this is bounded, not exhaustive.
  search_scope: rg --no-ignore --hidden --follow -n -i battery.black.mass|bauxite.residue|red.mud|phosphogypsum|metallurgical.coal|jct.2018.12.034|molecules30030674|fmicb.2024.1347072|jinorgbio.2015.08.022
    across data/records,research,reviews,history and /private/tmp/cmm-round13-{secondary-raw,grade-raw,root-review}.
    Exact DOI web queries with correction/retraction for Lalropuia, Urik, Zhang; Antonick
    DOI and full OSTI manuscript checked. No pagination or complete Crossmark audit.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round13-gate-receipts.json
  locator: All three terminal-zero commands;check/require/history logs and gated hash
    manifest
  accessed_at: '2026-10-11T09:08:08Z'
  support: supports
  summary: Root executed 307 passed, 3 skipped in 76.91 s; 101 records, 0 failed;
    116 histories, 0 errors. Exact target bytes unchanged since gates. These offline
    checks do not prove source accuracy.
  snapshot_sha256: fbebdd5faf0dd81c8ea05bc8abec1b9ce90d96b7c91372195285c690416fcc8a
assessments:
- assessment_id: identity
  area: identity
  topic: Material boundary, identifiers and criticality omission
  outcome: supported
  summary: A heterogeneous powder stream produced by pretreatment of spent lithium-ion
    batteries. Composition depends on battery chemistry and processing; the curated
    experiment used nickel-manganese-cobalt battery material after discharging, dismantling,
    thermal treatment, crushing and sorting. This secondary resource is distinct from
    whole batteries, an individual cathode compound, cobalt or lithium elements, and
    recovered battery-grade products. Constituent-element criticality is not inherited
    by this mixed feed.
  target_ids:
  - cmmmech:battery-black-mass
  evidence_ids:
  - record
  - search
  - paper
  - quantity
  dimensions:
  - name: material_form
    value: Mixed NMC lithium-ion battery black mass
    definition: Pretreated secondary feed, not elemental Co or a qualified battery
      product.
    evidence_ids:
    - record
    - paper
    - quantity
  - name: biomass
    value: Living adapted Lake Hromnice consortium
    definition: Initial enrichment assignments do not authenticate final culture members.
    evidence_ids:
    - record
    - paper
    - quantity
  - name: conditions
    value: 50 mL FeS;50 mM FeSO4;1% S;initial pH 2;10% inoculum;7 d preculture + 7
      d at 1% feed;30 C, 150 rpm
    definition: Specific laboratory protocol, no industrial inference.
    evidence_ids:
    - record
    - paper
    - quantity
  - name: controls_outcome
    value: Unadapted and sterile medium; n=3SD; day 2 mobilization pattern
    definition: Acidity/iron mismatch and nonclosing mass inventory; no yield accepted.
    evidence_ids:
    - record
    - paper
    - quantity
- assessment_id: science
  area: evidence
  topic: Primary claim verification and inference limits
  outcome: supported
  summary: The stated evidence supports the deliberately bounded record. No post-adaptation
    taxonomic authentication or member-specific causal controls. Different abiotic
    pH/iron chemistry and unresolved adaptation/feed inventories preclude quantitative
    whole-process recovery. Supplement-only sequence claims not accepted; reviewer
    read main paper and noted curator404 supplement route, did not independently acquire
    the workbook.
  target_ids:
  - cmmmech:battery-black-mass
  evidence_ids:
  - paper
  - quantity
  - record
- assessment_id: provenance
  area: provenance
  topic: Actual changes and retained source base
  outcome: supported
  summary: New CREATE sidecar and distinct inline event describe present curation.
    Trusted base is merged main 14ceff0; no prior records/history/reviews edited.
    Exact current target hash verified.
  target_ids:
  - cmmmech:battery-black-mass
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- No post-adaptation taxonomic authentication or member-specific causal controls.
- Different abiotic pH/iron chemistry and unresolved adaptation/feed inventories preclude
  quantitative whole-process recovery.
- Supplement-only sequence claims not accepted; reviewer read main paper and noted
  curator404 supplement route, did not independently acquire the workbook.
- Full-text access limits and bounded source/correction search are explicit; no global
  absence or exhaustiveness claim.
tags:
- round13
- independent
- scientific-review
```
