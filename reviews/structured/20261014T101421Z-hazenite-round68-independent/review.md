# Independent scientific review of hazenite

- Review: 20261014T101421Z-hazenite-round68-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T10:08:28.414454Z
- Finished UTC: 2026-10-14T10:14:21.234509Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Hazenite is approved KNaMg2(PO4)2·14H2O, IMA 2007-061, distinct from the ammonium analog, constituent commodities and mixed lake deposits. The exact identifier and formula agree with the current authority and original description. Phosphate supplied by decay and cell-surface nucleation are hypotheses, not experimentally isolated causes. Structure and spatial association do not establish biological exclusivity. The record retains unknown formation-time biomass state, local pH and seasonality; it does not transfer the prior culture identity to the field material.

## Scope And Provenance

Exact maintained record and CREATE history; primary evidence, current identity authority, claimed mechanism boundaries and required checks.

Selection: Assigned frozen path, inspected before final field-by-field judgment; full target reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e8a5f936607481446e4897e3bf2e0d10f0556632.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hazenite | data/records/hazenite.yaml | maintained | Hazenite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:hazenite | Reviewer execution; two records, zero failures. |
| Completed batch gate 1 | passed | True | cmmmech:hazenite | Coordinator execution 2026-10-14T10:07:55.959142+00:00 to 2026-10-14T10:10:54.849862+00:00; actual receipt and log hash checked. |
| Completed batch gate 2 | passed | True | cmmmech:hazenite | Coordinator execution 2026-10-14T10:10:54.849953+00:00 to 2026-10-14T10:11:12.359065+00:00; actual receipt and log hash checked. |
| Completed batch gate 3 | passed | True | cmmmech:hazenite | Coordinator execution 2026-10-14T10:11:12.359194+00:00 to 2026-10-14T10:11:20.211887+00:00; actual receipt and log hash checked. |

## Scientific And Domain Assessments

### Species identity, identifiers and criticality

identity: supported. Targets: cmmmech:hazenite.

Hazenite is approved KNaMg2(PO4)2·14H2O, IMA 2007-061, distinct from the ammonium analog, constituent commodities and mixed lake deposits. The exact identifier and formula agree with the current authority and original description.

### Experimental or observational context

evidence: supported. Targets: cmmmech:hazenite.

The source describes crystals on or in dried or decomposed cyanobacterial material on carbonate tufa. Field organisms are not taxonomically identified. Twenty-point electron-microprobe averages, water calculated by difference, Raman and powder/single-crystal diffraction are accurately distinguished. The Lyngbya culture paragraph is retained only as retrospective context.

### Evidence limits, contradictions and deployment

evidence: supported. Targets: cmmmech:hazenite.

Phosphate supplied by decay and cell-surface nucleation are hypotheses, not experimentally isolated causes. Structure and spatial association do not establish biological exclusivity. The record retains unknown formation-time biomass state, local pH and seasonality; it does not transfer the prior culture identity to the field material.

### Frozen bytes, authorship and gates

provenance: supported. Targets: cmmmech:hazenite.

Record and CREATE history hashes match the pre-assessment native inspection. Actual required checks passed. No supported corrective defect was found in the stated scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/hazenite.yaml; Entire record | supports | Every field read against the primary originals after native inspect; exact target hash rechecked before saving. |
| history | history/records/hazenite/2026-10-14T100415Z-codex-94f0e4.yaml; Entire CREATE session and inline event | supports | Current actor, timestamps and maintained target agree. Reviewer did not author or edit these records or histories. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pages 1–2 and exact rows on PDF pages 89 and 91 | supports | Original retained official PDF rows visually checked: hannayite grandfathered, original description 1879; hazenite approved 2007-061. Formula and mineral-species boundaries agree. |
| dedup | /private/tmp/cmm-round68-phosphate-independent/dedup.txt; Repository records, research, reviews and history | context_only | Hidden and ignored files included, relevant symlinks followed; prior occurrences and source names were checked within these paths. This is not machinewide absence evidence. |
| notices | https://doi.org/10.2138/am.2011.3668; Independent live web searches, 14 October 2026 UTC | context_only | No relevant correction or retraction appeared in the first returned result batches. A 2024 hazenite culture study surfaced and remains a separate source follow-up; absence of a notice is not established universally. |
| named | /private/tmp/cmm-round68-phosphate-independent/named-validation.log; Complete reviewer-executed log | supports | Actual locked named validation of both phosphate records passed, two records and zero failures. |
| batch | /private/tmp/cmm-round68-final-gates.json; Command receipt and matching SHA-256 of complete log | supports | Coordinator ran just check, nonempty corpus validation and trusted-base history validation successfully; receipt and retained log hash independently verified. |
| primary | https://www.rruff.net/odr/view/734/file_download/AM96_675.pdf; Complete seven pages 675–681; Tables 1–6, Figures 1–3 and formation discussion | supports | Read complete scientific body and references and visually inspected all seven original pages. Natural phase identity is supported by chemical, diffraction and Raman characterization; microbial association is observational. The retrospective 2004 culture account is explicitly distinguished. |

## Limits And Additional Notes

- The 2011 field study establishes identity and spatial association, not a controlled microbial formation mechanism.
- Yang and Sun 2004 was not independently acquired; its culture paragraph remains context only.
- The 2024 K/Na-hazenite culture lead PMC11150794 was located but its methods were not reviewed here; it is a separate prioritized source follow-up.
- No measured recovery efficiency, isolated product yield, phosphate-source tracing or industrial process is demonstrated.
- No supported corrective finding on the frozen record.
- Original PDFs and validation receipts remain outside Git. Source acquisition and inspection are not independent replication of the experiments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T101421Z-hazenite-round68-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of hazenite
started_at: '2026-10-14T10:08:28.414454Z'
finished_at: '2026-10-14T10:14:21.234509Z'
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
summary: Hazenite is approved KNaMg2(PO4)2·14H2O, IMA 2007-061, distinct from the
  ammonium analog, constituent commodities and mixed lake deposits. The exact identifier
  and formula agree with the current authority and original description. Phosphate
  supplied by decay and cell-surface nucleation are hypotheses, not experimentally
  isolated causes. Structure and spatial association do not establish biological exclusivity.
  The record retains unknown formation-time biomass state, local pH and seasonality;
  it does not transfer the prior culture identity to the field material.
source:
  git_revision: e8a5f936607481446e4897e3bf2e0d10f0556632
  state: working_tree
  inputs:
  - path: data/records/hazenite.yaml
    sha256: 4b9049e0aad226c9c33e762744aef155584aa6ae783d129d0d0f66ebb20ef7c1
    role: target
  - path: history/records/hazenite/2026-10-14T100415Z-codex-94f0e4.yaml
    sha256: 1a22046c32dbfe57b6acb9ce8d43ad52565da2aeb9bfad0e0168a6948723105d
    role: context
scope:
  description: Exact maintained record and CREATE history; primary evidence, current
    identity authority, claimed mechanism boundaries and required checks.
  selection: Assigned frozen path, inspected before final field-by-field judgment;
    full target reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hazenite
targets:
- target_id: cmmmech:hazenite
  path: data/records/hazenite.yaml
  label: Hazenite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hazenite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named record validation
  command: uv run --locked cmmmech validate data/records/hannayite.yaml data/records/hazenite.yaml
  status: passed
  required: true
  summary: Reviewer execution; two records, zero failures.
  target_ids:
  - cmmmech:hazenite
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
  - cmmmech:hazenite
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
  - cmmmech:hazenite
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
  - cmmmech:hazenite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/hazenite.yaml
  locator: Entire record
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: Every field read against the primary originals after native inspect; exact
    target hash rechecked before saving.
  snapshot_sha256: 4b9049e0aad226c9c33e762744aef155584aa6ae783d129d0d0f66ebb20ef7c1
- evidence_id: history
  kind: record_content
  reference: history/records/hazenite/2026-10-14T100415Z-codex-94f0e4.yaml
  locator: Entire CREATE session and inline event
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: Current actor, timestamps and maintained target agree. Reviewer did not
    author or edit these records or histories.
  snapshot_sha256: 1a22046c32dbfe57b6acb9ce8d43ad52565da2aeb9bfad0e0168a6948723105d
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pages 1–2 and exact rows on PDF pages 89 and 91
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: 'Original retained official PDF rows visually checked: hannayite grandfathered,
    original description 1879; hazenite approved 2007-061. Formula and mineral-species
    boundaries agree.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round68-phosphate-independent/dedup.txt
  locator: Repository records, research, reviews and history
  accessed_at: '2026-10-14T10:14:21.234509Z'
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
  accessed_at: '2026-10-14T10:14:21.234509Z'
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
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: Actual locked named validation of both phosphate records passed, two records
    and zero failures.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round68-final-gates.json
  locator: Command receipt and matching SHA-256 of complete log
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: Coordinator ran just check, nonempty corpus validation and trusted-base
    history validation successfully; receipt and retained log hash independently verified.
  snapshot_sha256: 98a8895b0aa6cd7c11a3a0e92d34f985e8d6985a2de3b3a6bcaf7842a578f477
- evidence_id: primary
  kind: primary_source
  reference: https://www.rruff.net/odr/view/734/file_download/AM96_675.pdf
  locator: Complete seven pages 675–681; Tables 1–6, Figures 1–3 and formation discussion
  accessed_at: '2026-10-14T10:14:21.234509Z'
  support: supports
  summary: Read complete scientific body and references and visually inspected all
    seven original pages. Natural phase identity is supported by chemical, diffraction
    and Raman characterization; microbial association is observational. The retrospective
    2004 culture account is explicitly distinguished.
  snapshot_sha256: 9ea07598d99c05c4b3d37c18e016b89f12d856721e7479f5d92eb08383f65af9
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, identifiers and criticality
  outcome: supported
  summary: Hazenite is approved KNaMg2(PO4)2·14H2O, IMA 2007-061, distinct from the
    ammonium analog, constituent commodities and mixed lake deposits. The exact identifier
    and formula agree with the current authority and original description.
  target_ids:
  - cmmmech:hazenite
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
  summary: The source describes crystals on or in dried or decomposed cyanobacterial
    material on carbonate tufa. Field organisms are not taxonomically identified.
    Twenty-point electron-microprobe averages, water calculated by difference, Raman
    and powder/single-crystal diffraction are accurately distinguished. The Lyngbya
    culture paragraph is retained only as retrospective context.
  target_ids:
  - cmmmech:hazenite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biological_status
    value: Natural field association with dried or decomposed cyanobacterial remains;
      metabolic state during formation unknown
    definition: No causal requirement for living cells or exclusive biological formation
      is asserted.
    evidence_ids:
    - record
    - primary
  - name: organism
    value: Unidentified field cyanobacterial material
    definition: Source wording green algae is retained as terminology; Lyngbya sp.
      in an earlier study is not an identity for these specimens.
    evidence_ids:
    - primary
  - name: controls
    value: No matched sterile substrate, live/dead contrast, phosphate tracer or formation
      time series for the field material
    definition: Mineral identity methods are strong but do not supply causal controls.
    evidence_ids:
    - primary
  - name: substrate
    value: Calcite/aragonite-rich porous tufa at Mono Lake; associated remains
    definition: Lake-wide literature pH and salinity are context, not specimen-specific
      formation measurements.
    evidence_ids:
    - primary
- assessment_id: outcomes
  area: evidence
  topic: Evidence limits, contradictions and deployment
  outcome: supported
  summary: Phosphate supplied by decay and cell-surface nucleation are hypotheses,
    not experimentally isolated causes. Structure and spatial association do not establish
    biological exclusivity. The record retains unknown formation-time biomass state,
    local pH and seasonality; it does not transfer the prior culture identity to the
    field material.
  target_ids:
  - cmmmech:hazenite
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
  - cmmmech:hazenite
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
- The 2011 field study establishes identity and spatial association, not a controlled
  microbial formation mechanism.
- Yang and Sun 2004 was not independently acquired; its culture paragraph remains
  context only.
- The 2024 K/Na-hazenite culture lead PMC11150794 was located but its methods were
  not reviewed here; it is a separate prioritized source follow-up.
- No measured recovery efficiency, isolated product yield, phosphate-source tracing
  or industrial process is demonstrated.
notes:
- No supported corrective finding on the frozen record.
- Original PDFs and validation receipts remain outside Git. Source acquisition and
  inspection are not independent replication of the experiments.
tags:
- round68
- independent
- primary-figures
- hazenite
```
