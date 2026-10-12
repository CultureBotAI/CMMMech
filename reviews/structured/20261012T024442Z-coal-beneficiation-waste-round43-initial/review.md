# Independent coal-beneficiation-waste review: figure scope and author spelling

- Review: 20261012T024442Z-coal-beneficiation-waste-round43-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T02:40:49.168250Z
- Finished UTC: 2026-10-12T02:44:42.893563Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor confirmed source-fidelity defects require correction: Figure 2 is a metal-leaching comparison, not a wheat assay; original author spelling is Kamskaya. The narrow community-associated leaching observations and source limitations are otherwise supported by the two complete originals. Final batch checks and notice/dedup verification remain pending.

## Scope And Provenance

All maintained fields and both primary-source arms of one secondary-resource record; initial finding observation before final gates.

Selection: Parent-assigned independent native scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 59e24ec38d9c7b377dcfeade1637b298aab9623e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:coal-beneficiation-waste | data/records/coal-beneficiation-waste.yaml | maintained | Coal beneficiation waste |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:coal-beneficiation-waste | Reviewer execution session6583 terminal0; Checked 1 record(s); 0 failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Required final batch gate | unavailable | True | cmmmech:coal-beneficiation-waste | Corrected final cohort result not yet available or independently accepted. |
| Required final nonempty gate | unavailable | True | cmmmech:coal-beneficiation-waste | Corrected final cohort result not yet available or independently accepted. |
| Required final history gate | unavailable | True | cmmmech:coal-beneficiation-waste | Corrected final cohort result not yet available or independently accepted. |

## Scientific And Domain Assessments

### Secondary resource and biological scope

identity: supported. Targets: cmmmech:coal-beneficiation-waste.

Coal-processing dumps remain distinct from natural coal, combustion ash, a pure mineral or Ge element. No inherited criticality or authenticated strain assertion.

### Separate leaching measurements and controls

quantity: supported. Targets: cmmmech:coal-beneficiation-waste.

2012 reported 99.9% fractions are not complete recovery or isolated yields. 2016 approximate 1.5 versus0.5mg/L derives from Figure2 seven-day endpoints and is not pooled with2012. No matching sterile controls, closed balances or microbial advantage are demonstrated.

### Methods, uncertainties and source contradictions

evidence: supported. Targets: cmmmech:coal-beneficiation-waste.

Acid reagent concentration is correctly distinguished from final slurry. 2012 missing endpoint and2016 method/time-course mismatch, reagent typos, Eh units and disputed molecular explanations remain qualified.

### Assay attribution

evidence: concern. Targets: cmmmech:coal-beneficiation-waste.

The statement assigning all three2012 figures to germination incorrectly includes the metal-leaching Figure2.

### Original citation spelling

provenance: concern. Targets: cmmmech:coal-beneficiation-waste.

Kamskaya is directly attested in original English header; record Kamenskaya must be corrected.

## Findings

### F1: Assign only Figures 1 and 3 to the wheat assay

minor / open / confirmed; issue key: CMMMech.coal-beneficiation-waste.figure-assay-scope.

The first mechanism evidence[2] assigns Figures1–3 to the separate three-day wheat germination assay. Original2012 Figure2 instead displays metal concentrations before and after bacterial leaching, while Figures1 and3 show germination. Correct the locator to Figures1 and3, preserving the separation of the three-day assay from unspecified leaching duration.

### F2: Preserve original author spelling Kamskaya

minor / open / confirmed; issue key: CMMMech.coal-beneficiation-waste.author-transliteration.

The2012 citation lists Kamenskaya. Original English page43 prints Kamskaya V.L.; Cyrillic page37 reads Камская. Correct to Kamskaya or faithful original Cyrillic.

## Recommended Actions And Acceptance Checks

### A1

Correct the two maintained phrases and append canonical EDIT plus distinct inline event. Preserve original CREATE, initial source dossier and this review; add correction note.

- Wheat assay reference includes Figures1 and3 only; Figure2 not misattributed.
- Original source author spelling is Kamskaya.
- Other scientific fields remain unchanged except supported correction; named/nonempty/history validation pass after correction.
- Save successor with exact previous occurrence links and stable issue keys after actual required gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/coal-beneficiation-waste.yaml; All frozen fields | supports | Secondary-resource owner separates laboratory native-community association from demonstrated biological causation; two bounded source fidelity defects. |
| primary2012 | https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f; Complete original seven pages, printed37–43; Methods39, Tables1–2, Figures1–3 | supports | Feed, solution treatments and reported percentages supported. Only Figures1 and3 show wheat germination; Figure2 is metal concentrations before/after leaching. Original page43 English author list prints Kamskaya V.L. |
| figure2012 | https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f; Original printed page41, Figures2–3, visually inspected | refutes | Figure2 explicitly compares metal content before and after bacterial leaching in mg/kg. Figure3 is the wheat assay. Thus the maintained Figures1–3 assignment is false. |
| author2012 | https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f; Original printed43 English author list, plus printed37 Cyrillic header | refutes | English Kamskaya V.L. agrees with Cyrillic Камская; Kamenskaya in the record is a transcription error. |
| primary2016 | https://doi.org/10.18524/2307-4663.2016.3(35).77956; Complete original fourteen pages43–56, Methods44–45, Table1p46, Figures1–4pp47–49, Discussion50–52 | supports | Originals substantiate 1–3mm material, native community, nominal treatment ranges, approximate Figure2 concentration comparison and nonzero cell counts despite no observed ferric liquid growth. Reagent/units/percent/prose conflicts and missing sterile comparisons are honestly retained. |
| history | history/records/coal-beneficiation-waste/2026-10-12T023644Z-codex-ef668b.yaml; Canonical CREATE and inline event | supports | Actual codex/GPT-6/tool metadata and supported creation scope, distinct timestamps; no earlier authorship invented. |

## Limits And Additional Notes

- Final required cohort gates, independent notice search and bounded duplicate audit are not yet accepted in this initial observation.
- Missing matched abiotic controls prevent attribution of measured leaching to microorganisms; no isolated product or industrial process established.
- Source reagent, units, time-window and numerical inconsistencies remain explicitly qualified.
- No maintained scientific edits by reviewer.
- Initial native inspect timestamp is the actual inspect receipt modification timestamp.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T024442Z-coal-beneficiation-waste-round43-initial
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent coal-beneficiation-waste review: figure scope and author spelling'
started_at: '2026-10-12T02:40:49.168250Z'
finished_at: '2026-10-12T02:44:42.893563Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record/history/dossier authored by /root/round27_packaging.
    Reviewer authored lithium-mica-ore in this cohort, not this record. Native inspect
    preceded judgment. Curator-acquired primary originals were independently read;
    complete original seven-page 2012 and fourteen-page 2016 articles and all their
    figures/tables inspected. Shared worktree and acquisition disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Two minor confirmed source-fidelity defects require correction: Figure 2
  is a metal-leaching comparison, not a wheat assay; original author spelling is Kamskaya.
  The narrow community-associated leaching observations and source limitations are
  otherwise supported by the two complete originals. Final batch checks and notice/dedup
  verification remain pending.'
source:
  git_revision: 59e24ec38d9c7b377dcfeade1637b298aab9623e
  state: working_tree
  inputs:
  - path: data/records/coal-beneficiation-waste.yaml
    sha256: d66baa5a261df19b446a1689dd00222e5be5a603439f28f4b344482a65c0dd20
    role: target
  - path: docs/record-review-profile.md
    sha256: 93f65e8f516a9b7756afd89e4823c1b64e493a46ecbcb3ca5e54a5aa599b10f2
    role: context
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/coal-beneficiation-waste/2026-10-12T023644Z-codex-ef668b.yaml
    sha256: b1ebae42277506d336b2e573d01427b50550f66dfcfcf97c6477ea02f37076c7
    role: context
scope:
  description: All maintained fields and both primary-source arms of one secondary-resource
    record; initial finding observation before final gates.
  selection: Parent-assigned independent native scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:coal-beneficiation-waste
  exclusions:
  - target: New mechanisms, industrial feasibility and source-only 2019 study
    reason: Not asserted by maintained record; no raw analytical reprocessing or numerical
      extraction beyond displayed source precision.
targets:
- target_id: cmmmech:coal-beneficiation-waste
  path: data/records/coal-beneficiation-waste.yaml
  label: Coal beneficiation waste
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/coal-beneficiation-waste.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer execution session6583 terminal0; Checked 1 record(s); 0 failed.
    Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:coal-beneficiation-waste
- check_id: batch
  name: Required final batch gate
  command: just check
  status: unavailable
  required: true
  summary: Corrected final cohort result not yet available or independently accepted.
  target_ids:
  - cmmmech:coal-beneficiation-waste
- check_id: nonempty
  name: Required final nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: unavailable
  required: true
  summary: Corrected final cohort result not yet available or independently accepted.
  target_ids:
  - cmmmech:coal-beneficiation-waste
- check_id: history
  name: Required final history gate
  command: uv run --locked cmmmech validate-history --base 59e24ec38d9c7b377dcfeade1637b298aab9623e
  status: unavailable
  required: true
  summary: Corrected final cohort result not yet available or independently accepted.
  target_ids:
  - cmmmech:coal-beneficiation-waste
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/coal-beneficiation-waste.yaml
  locator: All frozen fields
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: supports
  summary: Secondary-resource owner separates laboratory native-community association
    from demonstrated biological causation; two bounded source fidelity defects.
  snapshot_sha256: d66baa5a261df19b446a1689dd00222e5be5a603439f28f4b344482a65c0dd20
- evidence_id: primary2012
  kind: primary_source
  reference: https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f
  locator: Complete original seven pages, printed37–43; Methods39, Tables1–2, Figures1–3
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: supports
  summary: Feed, solution treatments and reported percentages supported. Only Figures1
    and3 show wheat germination; Figure2 is metal concentrations before/after leaching.
    Original page43 English author list prints Kamskaya V.L.
  snapshot_sha256: d00048bcf19a3e8e567dccbfdd8020facd3d1d4d1d2f4cfe9dcda80fea8e45be
- evidence_id: figure2012
  kind: primary_source
  reference: https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f
  locator: Original printed page41, Figures2–3, visually inspected
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: refutes
  summary: Figure2 explicitly compares metal content before and after bacterial leaching
    in mg/kg. Figure3 is the wheat assay. Thus the maintained Figures1–3 assignment
    is false.
  snapshot_sha256: b542f2a0da0f1b2c29026d9c794fcc40a1f4024112ab02a4a4eb018683bbf0cb
- evidence_id: author2012
  kind: primary_source
  reference: https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f
  locator: Original printed43 English author list, plus printed37 Cyrillic header
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: refutes
  summary: English Kamskaya V.L. agrees with Cyrillic Камская; Kamenskaya in the record
    is a transcription error.
  snapshot_sha256: 5b1db437625a52c446fde949505cbc6c4b8373497ca3647a211f3732b21d9dbe
- evidence_id: primary2016
  kind: primary_source
  reference: https://doi.org/10.18524/2307-4663.2016.3(35).77956
  locator: Complete original fourteen pages43–56, Methods44–45, Table1p46, Figures1–4pp47–49,
    Discussion50–52
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: supports
  summary: Originals substantiate 1–3mm material, native community, nominal treatment
    ranges, approximate Figure2 concentration comparison and nonzero cell counts despite
    no observed ferric liquid growth. Reagent/units/percent/prose conflicts and missing
    sterile comparisons are honestly retained.
  snapshot_sha256: 160e68a4d73a2bd96b8385a7c941b5e04142d4ad7f83d731bdf1dbceff8f4e89
- evidence_id: history
  kind: record_content
  reference: history/records/coal-beneficiation-waste/2026-10-12T023644Z-codex-ef668b.yaml
  locator: Canonical CREATE and inline event
  accessed_at: '2026-10-12T02:44:42.893563Z'
  support: supports
  summary: Actual codex/GPT-6/tool metadata and supported creation scope, distinct
    timestamps; no earlier authorship invented.
  snapshot_sha256: b1ebae42277506d336b2e573d01427b50550f66dfcfcf97c6477ea02f37076c7
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary resource and biological scope
  outcome: supported
  summary: Coal-processing dumps remain distinct from natural coal, combustion ash,
    a pure mineral or Ge element. No inherited criticality or authenticated strain
    assertion.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - record
  - primary2012
  - primary2016
- assessment_id: measurements
  area: quantity
  topic: Separate leaching measurements and controls
  outcome: supported
  summary: 2012 reported 99.9% fractions are not complete recovery or isolated yields.
    2016 approximate 1.5 versus0.5mg/L derives from Figure2 seven-day endpoints and
    is not pooled with2012. No matching sterile controls, closed balances or microbial
    advantage are demonstrated.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - record
  - primary2012
  - primary2016
- assessment_id: conditions
  area: evidence
  topic: Methods, uncertainties and source contradictions
  outcome: supported
  summary: Acid reagent concentration is correctly distinguished from final slurry.
    2012 missing endpoint and2016 method/time-course mismatch, reagent typos, Eh units
    and disputed molecular explanations remain qualified.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - record
  - primary2012
  - primary2016
- assessment_id: figure_scope
  area: evidence
  topic: Assay attribution
  outcome: concern
  summary: The statement assigning all three2012 figures to germination incorrectly
    includes the metal-leaching Figure2.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - record
  - figure2012
- assessment_id: author
  area: provenance
  topic: Original citation spelling
  outcome: concern
  summary: Kamskaya is directly attested in original English header; record Kamenskaya
    must be corrected.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - record
  - author2012
findings:
- finding_id: F1
  issue_key: CMMMech.coal-beneficiation-waste.figure-assay-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Assign only Figures 1 and 3 to the wheat assay
  description: The first mechanism evidence[2] assigns Figures1–3 to the separate
    three-day wheat germination assay. Original2012 Figure2 instead displays metal
    concentrations before and after bacterial leaching, while Figures1 and3 show germination.
    Correct the locator to Figures1 and3, preserving the separation of the three-day
    assay from unspecified leaching duration.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  field_paths:
  - mechanisms[id=native_community_associated_acid_leaching].evidence[2].explanation
  evidence_ids:
  - record
  - figure2012
  - primary2012
  rule_id: primary-source-fidelity
  native_severity: minor
  normalization_reason: Bounded source-locator or citation transcription defect; material
    identity and narrow laboratory leaching observations remain supportable.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
    role: maintained_record
- finding_id: F2
  issue_key: CMMMech.coal-beneficiation-waste.author-transliteration
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve original author spelling Kamskaya
  description: The2012 citation lists Kamenskaya. Original English page43 prints Kamskaya
    V.L.; Cyrillic page37 reads Камская. Correct to Kamskaya or faithful original
    Cyrillic.
  target_ids:
  - cmmmech:coal-beneficiation-waste
  field_paths:
  - sources[id=blayda2012].title
  evidence_ids:
  - record
  - author2012
  - primary2012
  rule_id: primary-source-fidelity
  native_severity: minor
  normalization_reason: Bounded source-locator or citation transcription defect; material
    identity and narrow laboratory leaching observations remain supportable.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
    role: maintained_record
actions:
- action_id: A1
  description: Correct the two maintained phrases and append canonical EDIT plus distinct
    inline event. Preserve original CREATE, initial source dossier and this review;
    add correction note.
  finding_ids:
  - F1
  - F2
  target_ids:
  - cmmmech:coal-beneficiation-waste
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
    role: maintained_record
  acceptance_checks:
  - Wheat assay reference includes Figures1 and3 only; Figure2 not misattributed.
  - Original source author spelling is Kamskaya.
  - Other scientific fields remain unchanged except supported correction; named/nonempty/history
    validation pass after correction.
  - Save successor with exact previous occurrence links and stable issue keys after
    actual required gates.
limitations:
- Final required cohort gates, independent notice search and bounded duplicate audit
  are not yet accepted in this initial observation.
- Missing matched abiotic controls prevent attribution of measured leaching to microorganisms;
  no isolated product or industrial process established.
- Source reagent, units, time-window and numerical inconsistencies remain explicitly
  qualified.
notes:
- No maintained scientific edits by reviewer.
- Initial native inspect timestamp is the actual inspect receipt modification timestamp.
links:
- https://doi.org/10.18524/2307-4663.2016.3(35).77956
- https://dspace.onu.edu.ua/items/1db891e3-f8fc-4e42-862f-520085833a0f
tags:
- round43
- coal-beneficiation-waste
- independent
- scientific
```
