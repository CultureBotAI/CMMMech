# Independent scientific review of hannayite

- Review: 20261014T101416Z-hannayite-round68-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T10:08:24.768997Z
- Finished UTC: 2026-10-14T10:14:16.498106Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Hannayite is the hydrated ammonium magnesium hydrogen-phosphate mineral, distinct from guano, elements and neighboring phosphate phases. The year 1879 is not an invented approval accession. The body reports hannayite dissolution with schertelite crystallization during prolonged concentrated-solution preparation, and newberyite plus struvite replacement in water at 25 degrees C. The conflicting abstract products remain explicit. No microbial or industrial claim, mass yield, rate or universal sequence is inferred.

## Scope And Provenance

Exact maintained record and CREATE history; primary evidence, current identity authority, claimed mechanism boundaries and required checks.

Selection: Assigned frozen path, inspected before final field-by-field judgment; full target reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e8a5f936607481446e4897e3bf2e0d10f0556632.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hannayite | data/records/hannayite.yaml | maintained | Hannayite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:hannayite | Reviewer execution; two records, zero failures. |
| Completed batch gate 1 | passed | True | cmmmech:hannayite | Coordinator execution 2026-10-14T10:07:55.959142+00:00 to 2026-10-14T10:10:54.849862+00:00; actual receipt and log hash checked. |
| Completed batch gate 2 | passed | True | cmmmech:hannayite | Coordinator execution 2026-10-14T10:10:54.849953+00:00 to 2026-10-14T10:11:12.359065+00:00; actual receipt and log hash checked. |
| Completed batch gate 3 | passed | True | cmmmech:hannayite | Coordinator execution 2026-10-14T10:11:12.359194+00:00 to 2026-10-14T10:11:20.211887+00:00; actual receipt and log hash checked. |

## Scientific And Domain Assessments

### Species identity, identifiers and criticality

identity: supported. Targets: cmmmech:hannayite.

Hannayite is the hydrated ammonium magnesium hydrogen-phosphate mineral, distinct from guano, elements and neighboring phosphate phases. The year 1879 is not an invented approval accession.

### Experimental or observational context

evidence: supported. Targets: cmmmech:hannayite.

The two preparation recipes at 25 and 100 degrees C match pages 636–637. Magnesium acetate hydration is unspecified; the record correctly avoids an inferred molar loading. About 50 preparations concern symmetry observations, not yield replicates. The shared pH 3.5–6 range is not presented as a phase-pure window.

### Evidence limits, contradictions and deployment

evidence: supported. Targets: cmmmech:hannayite.

The body reports hannayite dissolution with schertelite crystallization during prolonged concentrated-solution preparation, and newberyite plus struvite replacement in water at 25 degrees C. The conflicting abstract products remain explicit. No microbial or industrial claim, mass yield, rate or universal sequence is inferred.

### Frozen bytes, authorship and gates

provenance: supported. Targets: cmmmech:hannayite.

Record and CREATE history hashes match the pre-assessment native inspection. Actual required checks passed. No supported corrective defect was found in the stated scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/hannayite.yaml; Entire record | supports | Every field read against the primary originals after native inspect; exact target hash rechecked before saving. |
| history | history/records/hannayite/2026-10-14T100352Z-codex-f70b6c.yaml; Entire CREATE session and inline event | supports | Current actor, timestamps and maintained target agree. Reviewer did not author or edit these records or histories. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pages 1–2 and exact rows on PDF pages 89 and 91 | supports | Original retained official PDF rows visually checked: hannayite grandfathered, original description 1879; hazenite approved 2007-061. Formula and mineral-species boundaries agree. |
| dedup | /private/tmp/cmm-round68-phosphate-independent/dedup.txt; Repository records, research, reviews and history | context_only | Hidden and ignored files included, relevant symlinks followed; prior occurrences and source names were checked within these paths. This is not machinewide absence evidence. |
| notices | https://doi.org/10.2138/am.2011.3668; Independent live web searches, 14 October 2026 UTC | context_only | No relevant correction or retraction appeared in the first returned result batches. A 2024 hazenite culture study surfaced and remains a separate source follow-up; absence of a notice is not established universally. |
| named | /private/tmp/cmm-round68-phosphate-independent/named-validation.log; Complete reviewer-executed log | supports | Actual locked named validation of both phosphate records passed, two records and zero failures. |
| batch | /private/tmp/cmm-round68-final-gates.json; Command receipt and matching SHA-256 of complete log | supports | Coordinator ran just check, nonempty corpus validation and trusted-base history validation successfully; receipt and retained log hash independently verified. |
| primary | https://msaweb.org/AmMin/AM48/AM48_635.pdf; Complete seven pages 635–641; Table 1, chemical analyses and both preparation recipes | supports | Read full extracted text and visually inspected every original page. Laboratory chemical preparation and alteration are supported; no organisms were used. Abstract versus body alteration-product discrepancy is visible. |

## Limits And Additional Notes

- The original is a chemical preparation study, not a microbial assay.
- Abstract and detailed body disagree on hydrolytic alteration products; the record preserves the conflict rather than supplying a guessed correction.
- Water-alteration kinetics, replication and material balance are not reported; source recipes do not define a validated recovery process.
- No supported corrective finding on the frozen record.
- Original PDFs and validation receipts remain outside Git. Source acquisition and inspection are not independent replication of the experiments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T101416Z-hannayite-round68-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of hannayite
started_at: '2026-10-14T10:08:24.768997Z'
finished_at: '2026-10-14T10:14:16.498106Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The phosphate records, histories and dossier were authored by
    /root/round68_phosphates. Reviewer curated only wollastonite and diopside in this
    cohort and made no phosphate record/history edits. Original acquisition artifacts
    and cautions were shared; the reviewer independently read the papers, original
    figures/tables and exact record fields.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Hannayite is the hydrated ammonium magnesium hydrogen-phosphate mineral,
  distinct from guano, elements and neighboring phosphate phases. The year 1879 is
  not an invented approval accession. The body reports hannayite dissolution with
  schertelite crystallization during prolonged concentrated-solution preparation,
  and newberyite plus struvite replacement in water at 25 degrees C. The conflicting
  abstract products remain explicit. No microbial or industrial claim, mass yield,
  rate or universal sequence is inferred.
source:
  git_revision: e8a5f936607481446e4897e3bf2e0d10f0556632
  state: working_tree
  inputs:
  - path: data/records/hannayite.yaml
    sha256: 6a05a0d42bdac6c6a1755ce130733fd9d64e8079471279526157c690159997a4
    role: target
  - path: history/records/hannayite/2026-10-14T100352Z-codex-f70b6c.yaml
    sha256: 4ae501aeea931279411f13b69283fef294631c1a0f2a612520e26cb9b7bd0fc7
    role: context
scope:
  description: Exact maintained record and CREATE history; primary evidence, current
    identity authority, claimed mechanism boundaries and required checks.
  selection: Assigned frozen path, inspected before final field-by-field judgment;
    full target reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hannayite
targets:
- target_id: cmmmech:hannayite
  path: data/records/hannayite.yaml
  label: Hannayite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hannayite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named record validation
  command: uv run --locked cmmmech validate data/records/hannayite.yaml data/records/hazenite.yaml
  status: passed
  required: true
  summary: Reviewer execution; two records, zero failures.
  target_ids:
  - cmmmech:hannayite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Completed batch gate 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T10:07:55.959142+00:00 to 2026-10-14T10:10:54.849862+00:00;
    actual receipt and log hash checked.
  target_ids:
  - cmmmech:hannayite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Completed batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T10:10:54.849953+00:00 to 2026-10-14T10:11:12.359065+00:00;
    actual receipt and log hash checked.
  target_ids:
  - cmmmech:hannayite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Completed batch gate 3
  command: uv run --locked cmmmech validate-history --base e8a5f936607481446e4897e3bf2e0d10f0556632
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T10:11:12.359194+00:00 to 2026-10-14T10:11:20.211887+00:00;
    actual receipt and log hash checked.
  target_ids:
  - cmmmech:hannayite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/hannayite.yaml
  locator: Entire record
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: Every field read against the primary originals after native inspect; exact
    target hash rechecked before saving.
  snapshot_sha256: 6a05a0d42bdac6c6a1755ce130733fd9d64e8079471279526157c690159997a4
- evidence_id: history
  kind: record_content
  reference: history/records/hannayite/2026-10-14T100352Z-codex-f70b6c.yaml
  locator: Entire CREATE session and inline event
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: Current actor, timestamps and maintained target agree. Reviewer did not
    author or edit these records or histories.
  snapshot_sha256: 4ae501aeea931279411f13b69283fef294631c1a0f2a612520e26cb9b7bd0fc7
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pages 1–2 and exact rows on PDF pages 89 and 91
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: 'Original retained official PDF rows visually checked: hannayite grandfathered,
    original description 1879; hazenite approved 2007-061. Formula and mineral-species
    boundaries agree.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round68-phosphate-independent/dedup.txt
  locator: Repository records, research, reviews and history
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: context_only
  summary: Hidden and ignored files included, relevant symlinks followed; prior occurrences
    and source names were checked within these paths. This is not machinewide absence
    evidence.
  search_scope: rg --no-ignore --hidden --follow -n -i hannayite|hazenite|10.2138/am.2011.3668|AM48_635
    data/records research reviews history
  snapshot_sha256: d728a589a8866df07dc957ab7aab633997fbb630011045394477a3371d3c2483
- evidence_id: notices
  kind: search
  reference: https://doi.org/10.2138/am.2011.3668
  locator: Independent live web searches, 14 October 2026 UTC
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: context_only
  summary: No relevant correction or retraction appeared in the first returned result
    batches. A 2024 hazenite culture study surfaced and remains a separate source
    follow-up; absence of a notice is not established universally.
  search_scope: 'Queries: "10.2138/am.2011.3668" correction OR retraction; "hannayite"
    "Frazier" "1963" correction; "hazenite" "abiotic" synthesis. No date/domain filters
    or pagination. The 2024 PMC11150794 lead was not assessed as mechanism evidence
    here.'
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round68-phosphate-independent/named-validation.log
  locator: Complete reviewer-executed log
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: Actual locked named validation of both phosphate records passed, two records
    and zero failures.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round68-final-gates.json
  locator: Command receipt and matching SHA-256 of complete log
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: Coordinator ran just check, nonempty corpus validation and trusted-base
    history validation successfully; receipt and retained log hash independently verified.
  snapshot_sha256: 98a8895b0aa6cd7c11a3a0e92d34f985e8d6985a2de3b3a6bcaf7842a578f477
- evidence_id: primary
  kind: primary_source
  reference: https://msaweb.org/AmMin/AM48/AM48_635.pdf
  locator: Complete seven pages 635–641; Table 1, chemical analyses and both preparation
    recipes
  accessed_at: '2026-10-14T10:14:16.498106Z'
  support: supports
  summary: Read full extracted text and visually inspected every original page. Laboratory
    chemical preparation and alteration are supported; no organisms were used. Abstract
    versus body alteration-product discrepancy is visible.
  snapshot_sha256: 977255a47ea9842bbb6e69d551ddaa1b299a6ba4475157ec705e03de6d049225
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, identifiers and criticality
  outcome: supported
  summary: Hannayite is the hydrated ammonium magnesium hydrogen-phosphate mineral,
    distinct from guano, elements and neighboring phosphate phases. The year 1879
    is not an invented approval accession.
  target_ids:
  - cmmmech:hannayite
  evidence_ids:
  - record
  - ima
  - primary
  dimensions:
  - name: criticality
    value: No jurisdiction, list or edition designation asserted
    definition: No constituent criticality is inherited; omission is not a universal
      noncriticality claim.
    evidence_ids:
    - record
- assessment_id: experiment
  area: evidence
  topic: Experimental or observational context
  outcome: supported
  summary: The two preparation recipes at 25 and 100 degrees C match pages 636–637.
    Magnesium acetate hydration is unspecified; the record correctly avoids an inferred
    molar loading. About 50 preparations concern symmetry observations, not yield
    replicates. The shared pH 3.5–6 range is not presented as a phase-pure window.
  target_ids:
  - cmmmech:hannayite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biological_status
    value: Abiotic reagent preparation and alteration; microbial false
    definition: Guano association is geological context and does not establish biological
      causality.
    evidence_ids:
    - record
    - primary
  - name: conditions
    value: Separate 25 and 100 degrees C concentrated-solution preparations; separate
      water alteration at 25 degrees C
    definition: Exact recipe masses are source values; magnesium acetate hydration,
      water-alteration loading and kinetic replication remain unspecified.
    evidence_ids:
    - primary
  - name: substrate
    value: Magnesium acetate and ammonium phosphate solutions; synthetic hannayite
    definition: This is not a measured extraction process for guano or a secondary
      waste resource.
    evidence_ids:
    - primary
- assessment_id: outcomes
  area: evidence
  topic: Evidence limits, contradictions and deployment
  outcome: supported
  summary: The body reports hannayite dissolution with schertelite crystallization
    during prolonged concentrated-solution preparation, and newberyite plus struvite
    replacement in water at 25 degrees C. The conflicting abstract products remain
    explicit. No microbial or industrial claim, mass yield, rate or universal sequence
    is inferred.
  target_ids:
  - cmmmech:hannayite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: deployment
    value: Laboratory chemical work or field mineral characterization only
    definition: Neither record asserts industrial extraction or material recovery.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Frozen bytes, authorship and gates
  outcome: supported
  summary: Record and CREATE history hashes match the pre-assessment native inspection.
    Actual required checks passed. No supported corrective defect was found in the
    stated scope.
  target_ids:
  - cmmmech:hannayite
  evidence_ids:
  - record
  - history
  - named
  - batch
  - dedup
  - notices
findings: []
actions: []
limitations:
- The original is a chemical preparation study, not a microbial assay.
- Abstract and detailed body disagree on hydrolytic alteration products; the record
  preserves the conflict rather than supplying a guessed correction.
- Water-alteration kinetics, replication and material balance are not reported; source
  recipes do not define a validated recovery process.
notes:
- No supported corrective finding on the frozen record.
- Original PDFs and validation receipts remain outside Git. Source acquisition and
  inspection are not independent replication of the experiments.
tags:
- round68
- independent
- primary-figures
- hannayite
```
