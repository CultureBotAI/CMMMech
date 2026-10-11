# Independent scientific review: municipal-waste-incineration-ash

- Review: 20261011T093443Z-municipal-waste-incineration-ash-round14-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:28:57.274265Z
- Finished UTC: 2026-10-11T09:34:43Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supported scoped resource identity and qualified laboratory mechanism,with no actionable record defect in reviewed scope.

## Scope And Provenance

All scientific and provenance fields of one new resource record.

Selection: New round14 resource assigned independently; all fields reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:municipal-waste-incineration-ash | data/records/municipal-waste-incineration-ash.yaml | maintained | Municipal-waste incineration ash |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Five reviewed-resource validation | passed | True | cmmmech:municipal-waste-incineration-ash | Root executed and observed terminal0:5 records,0failed. /private/tmp/cmm-round14-root-review/named-validation.log |
| Trusted-base canonical history | passed | True | cmmmech:municipal-waste-incineration-ash | Root observed terminal0:134history records,0errors. /private/tmp/cmm-round14-history.log |
| Required corpus validation | passed | True | cmmmech:municipal-waste-incineration-ash | Root observed terminal0:119records,0failed. /private/tmp/cmm-round14-require.log |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:municipal-waste-incineration-ash | Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |

## Scientific And Domain Assessments

### Secondary-resource boundaries

identity: supported. Targets: cmmmech:municipal-waste-incineration-ash.

Municipal-waste thermal-treatment ashA; fly/bottom fraction and host phases unresolved. No constituent-element criticality is inherited. No unverified resource/mineral identifier or designation is invented.

### Organism,pretreatment,controls and outcome

evidence: supported. Targets: cmmmech:municipal-waste-incineration-ash.

Living activated-sludge-derived mixed culture; no assigned taxon or strain. Sludge:water1:1,1%sulfur basis unspecified,adapt24C120rpm pH&lt;3;150mLculture+10gash,5days. AshA Nb100/0/6.7% versus2.3% averagedcontrol; selected aerated Rh99.2,Cd91.1,In60.7,Cr50.0%. Unknown control composition and analytical fraction, no biological replicate count; finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release, not product recovery or verified complete dissolution.

### Immutable history and exact working state

provenance: supported. Targets: cmmmech:municipal-waste-incineration-ash.

Independent root reviewer did not author this record; inspected target, native contract and actual CREATE sidecar before judging. Reused studies remain linked views, not independent replicates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/municipal-waste-incineration-ash.yaml; All fields and linked CREATE sidecar | supports | Exact working bytes captured before assessment; native schema and docs checked; actual GPT-6/codex CREATE targets this record and issue56, with separate inline event. |
| primary | https://doi.org/10.24425/aep.2019.128643; Research methods printed73-74; Tables1-4; Figures1-9; Results74-77 | supports | Independently read retained original primary PDF acquired by curator this round. Municipal-waste thermal-treatment ashA; fly/bottom fraction and host phases unresolved. Sludge:water1:1,1%sulfur basis unspecified,adapt24C120rpm pH&lt;3;150mLculture+10gash,5days. AshA Nb100/0/6.7% versus2.3% averagedcontrol; selected aerated Rh99.2,Cd91.1,In60.7,Cr50.0%. Unknown control composition and analytical fraction, no biological replicate count; finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release, not product recovery or verified complete dissolution. |
| search | Local corpus and four exact DOI queries; data/records,history,research,reviews plus first web result page | context_only | Ignored-inclusive followed local search establishes bounded identity overlap and repeated-study context. Four DOI correction/retraction queries returned original publications and related leads; no applicable notice in that result window. No exhaustive clearance. |

## Limits And Additional Notes

- Unknown control composition and analytical fraction, no biological replicate count; finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release, not product recovery or verified complete dissolution.
- Primary artifacts freshly acquired by curator were independently read by root; not claimed as independent root downloads. Visual checks: ReedPDF18/22;ParkPDF5/8;ashPDF2-5;hydroPDF6/8-11, with other relevant methods/results read as PDF text.
- Correction searches covered only listed exact-DOI queries and first returned results. Source weaknesses retained explicitly are not fabricated review issues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093443Z-municipal-waste-incineration-ash-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent scientific review: municipal-waste-incineration-ash'
started_at: '2026-10-11T09:28:57.274265Z'
finished_at: '2026-10-11T09:34:43Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate resource agent authored this target. Root independently
    inspected original full text, methods, tables and rendered figures, original taxonomy
    exports and record/history bytes. Root authored only a different magnet record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supported scoped resource identity and qualified laboratory mechanism,with
  no actionable record defect in reviewed scope.
source:
  git_revision: 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  state: working_tree
  inputs:
  - path: data/records/municipal-waste-incineration-ash.yaml
    sha256: 3677ebff576d161d1ad015d57f7ca27c810a17bc81a4166feb7efbdf8d154d52
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/municipal-waste-incineration-ash/2026-10-11T092619Z-codex-f202ce.yaml
    sha256: b703bfd68829e66d83059806bed305e373bac68feec9c0c5cee49f62c2f64ef5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific and provenance fields of one new resource record.
  selection: New round14 resource assigned independently; all fields reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:municipal-waste-incineration-ash
  exclusions:
  - target: Other corpus records and uncurated literature
    reason: Checked only for duplicate/scope context; no corpus-wide scientific clearance.
targets:
- target_id: cmmmech:municipal-waste-incineration-ash
  path: data/records/municipal-waste-incineration-ash.yaml
  label: Municipal-waste incineration ash
  kind: maintained
  ownership_note: Maintained native CMMMech YAML; future corrections belong to this
    record, not saved reviews.
checks:
- check_id: named
  name: Five reviewed-resource validation
  command: uv run --locked cmmmech validate data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    data/records/coal-fly-ash.yaml data/records/municipal-waste-incineration-ash.yaml
    data/records/sewage-sludge-incineration-ash.yaml data/records/spent-hydrocracking-catalyst.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
  summary: Root executed and observed terminal0:5 records,0failed. /private/tmp/cmm-round14-root-review/named-validation.log
- check_id: history
  name: Trusted-base canonical history
  command: uv run --locked cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root observed terminal0:134history records,0errors. /private/tmp/cmm-round14-history.log
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
- check_id: records
  name: Required corpus validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root observed terminal0:119records,0failed. /private/tmp/cmm-round14-require.log
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
- check_id: batch
  name: Native full batch checks before FCC wording correction
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories
    valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending;
    this gate covers other unchanged targets.
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/municipal-waste-incineration-ash.yaml
  locator: All fields and linked CREATE sidecar
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Exact working bytes captured before assessment; native schema and docs
    checked; actual GPT-6/codex CREATE targets this record and issue56, with separate
    inline event.
  snapshot_sha256: 3677ebff576d161d1ad015d57f7ca27c810a17bc81a4166feb7efbdf8d154d52
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.24425/aep.2019.128643
  locator: Research methods printed73-74; Tables1-4; Figures1-9; Results74-77
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Independently read retained original primary PDF acquired by curator this
    round. Municipal-waste thermal-treatment ashA; fly/bottom fraction and host phases
    unresolved. Sludge:water1:1,1%sulfur basis unspecified,adapt24C120rpm pH<3;150mLculture+10gash,5days.
    AshA Nb100/0/6.7% versus2.3% averagedcontrol; selected aerated Rh99.2,Cd91.1,In60.7,Cr50.0%.
    Unknown control composition and analytical fraction, no biological replicate count;
    finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release,
    not product recovery or verified complete dissolution.
  snapshot_sha256: 9f7ac95ce6f552b2473aa1c42ee5d7000fa4eec60ac1e6e0c5116aba91bb31f0
- evidence_id: search
  kind: search
  reference: Local corpus and four exact DOI queries
  locator: data/records,history,research,reviews plus first web result page
  accessed_at: '2026-10-11T09:34:43Z'
  support: context_only
  summary: Ignored-inclusive followed local search establishes bounded identity overlap
    and repeated-study context. Four DOI correction/retraction queries returned original
    publications and related leads; no applicable notice in that result window. No
    exhaustive clearance.
  snapshot_sha256: db9cb5c3009827426a8eeac8ba9a3e3d7a5ce7f1a61204484aac61e7a32dc15b
  search_scope: rg --no-ignore --hidden --follow matching four DOIs and five resource
    slugs across data/records history research reviews. Web queries exact quoted DOI
    for each cited paper plus correction retraction; no domain/date filters or pagination.
    Sources were independently read, not inferred from snippets.
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary-resource boundaries
  outcome: supported
  summary: Municipal-waste thermal-treatment ashA; fly/bottom fraction and host phases
    unresolved. No constituent-element criticality is inherited. No unverified resource/mineral
    identifier or designation is invented.
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
  evidence_ids:
  - target
  - primary
  dimensions:
  - name: material_form
    value: secondary_resource
    definition: Industrial waste/feed class, not elemental or mineral identity.
    evidence_ids:
    - primary
    - target
  - name: criticality
    value: No designation asserted
    definition: No jurisdiction/list/edition transferred from constituents.
    evidence_ids:
    - primary
    - target
- assessment_id: mechanism
  area: evidence
  topic: Organism,pretreatment,controls and outcome
  outcome: supported
  summary: Living activated-sludge-derived mixed culture; no assigned taxon or strain.
    Sludge:water1:1,1%sulfur basis unspecified,adapt24C120rpm pH<3;150mLculture+10gash,5days.
    AshA Nb100/0/6.7% versus2.3% averagedcontrol; selected aerated Rh99.2,Cd91.1,In60.7,Cr50.0%.
    Unknown control composition and analytical fraction, no biological replicate count;
    finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release,
    not product recovery or verified complete dissolution.
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
  evidence_ids:
  - target
  - primary
  dimensions:
  - name: organism
    value: Living activated-sludge-derived mixed culture; no assigned taxon or strain
    definition: Taxon,experimentalstrain or mixedcommunity scope.
    evidence_ids:
    - primary
    - target
  - name: conditions
    value: Sludge:water1:1,1%sulfur basis unspecified,adapt24C120rpm pH<3;150mLculture+10gash,5days
    definition: Selected laboratory assay and prior preparation.
    evidence_ids:
    - primary
    - target
  - name: outcome
    value: AshA Nb100/0/6.7% versus2.3% averagedcontrol; selected aerated Rh99.2,Cd91.1,In60.7,Cr50.0%
    definition: Measured source endpoint and denominator, not isolated product.
    evidence_ids:
    - primary
    - target
  - name: deployment
    value: Laboratory only
    definition: Supplier industrial origin is not industrial biological deployment.
    evidence_ids:
    - primary
    - target
- assessment_id: provenance
  area: provenance
  topic: Immutable history and exact working state
  outcome: supported
  summary: Independent root reviewer did not author this record; inspected target,
    native contract and actual CREATE sidecar before judging. Reused studies remain
    linked views, not independent replicates.
  target_ids:
  - cmmmech:municipal-waste-incineration-ash
  evidence_ids:
  - target
  - search
findings: []
actions: []
limitations:
- Unknown control composition and analytical fraction, no biological replicate count;
  finalpH10/6/10, mixing-table conflict. Reported100% is feed-normalized release,
  not product recovery or verified complete dissolution.
- 'Primary artifacts freshly acquired by curator were independently read by root;
  not claimed as independent root downloads. Visual checks: ReedPDF18/22;ParkPDF5/8;ashPDF2-5;hydroPDF6/8-11,
  with other relevant methods/results read as PDF text.'
- Correction searches covered only listed exact-DOI queries and first returned results.
  Source weaknesses retained explicitly are not fabricated review issues.
tags:
- round14
- independent
- scientific-review
```
