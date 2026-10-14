# Independent scientific review of artinite

- Review: 20261014T141419Z-artinite-round73-final
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T14:14:06.765443Z
- Finished UTC: 2026-10-14T14:14:19.924871Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified scientific acceptance with explicit source and causal limits; all required gates passed.

## Scope And Provenance

Full maintained record and history; independent primary-source scientific reassessment.

Selection: Assigned frozen owner, native inspect before final assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:artinite | data/records/artinite.yaml | maintained | Artinite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| named validation | passed | True | cmmmech:artinite | Actual execution completed with exit0. |
| history validation | passed | True | cmmmech:artinite | Actual execution completed with exit0. |
| Completed batch gate | passed | True | cmmmech:artinite | Receipt/log verified, exit0. |
| Completed batch gate | passed | True | cmmmech:artinite | Receipt/log verified, exit0. |
| Completed batch gate | passed | True | cmmmech:artinite | Receipt/log verified, exit0. |

## Scientific And Domain Assessments

### Mineral species boundary

identity: supported. Targets: cmmmech:artinite.

Formula and grandfathered status correctly scoped; no inherited criticality.

### Dissolution versus phase persistence

evidence: supported. Targets: cmmmech:artinite.

Natural artinite remains dominant in sampled exsitu solids; minor impurities and brucite/HCB prevent pure-phase/universal stability claims.

### Separate concentrated-solution experiment

evidence: supported. Targets: cmmmech:artinite.

Table5/S2 mixed phases and time/temperature conditions are correctly distinguished; DY+A at20C/3months retained.

### Measured versus calculated and contradictory labels

scope: supported. Targets: cmmmech:artinite.

Solubility/IAP models, Raman temperature/phase labels and limited causal interpretation remain explicit; no microbial or industrial outcome.

## Findings

### F1: Do not extend the initial shaking duration to daily shaking

minor / resolved / confirmed; issue key: CMMMech.artinite.daily-shaking-duration.

Both mechanism contexts imply one-minute shaking on workdays. Sections2.2–2.3 specify one minute before storage, then daily shaking during workdays without giving its duration. Preserve initial duration and daily frequency separately; do not invent a daily duration.

Disposition: Independently re-read p176 and both corrected context strings. Initial one-minute shaking is separated from daily workday shaking whose duration is explicitly not reported. New EDIT sidecar and inline event appended; initial review and history preserved. Named and corrected batch validation passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/artinite.yaml; Complete maintained owner and distinct inline events | supports | Compared all assertions to original methods, results, authority rows and graphics. |
| history0 | history/records/artinite/2026-10-14T135947Z-codex-a1da31.yaml; Canonical immutable sidecar | supports | Actual actor, event, UTC and target agree with the curation change. |
| history1 | history/records/artinite/2026-10-14T140827Z-codex-dbfd84.yaml; Canonical immutable sidecar | supports | Actual actor, event, UTC and target agree with the curation change. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Official September2026 list definitions and PDF page 16 | supports | Grandfathered species formula and original-description year confirmed; no approval-number or criticality inference. |
| handbook | https://www.handbookofmineralogy.org/pdfs/artinite.pdf; Complete mineral entry | supports | Mineral identity distinct from neighbouring magnesium carbonate phases. |
| main | https://doi.org/10.3151/jact.24.174; Complete17page original; Sections2.1–2.4,3.1–3.4; Figures1–10; Tables1–6 | supports | Original source supports separate water and concentrated precipitation arms, with measured/modelled distinctions and impurity limits. All original page graphics inspected. |
| si | https://www.jstage.jst.go.jp/article/jact/24/4/24_174/_supplement/_download/24_174_1.pdf; Complete18page SI; FiguresS1–S16,TablesS1–S2 | supports | Original figures retain 5C labels versus7C methods and S14 A-label versus TableS2 phase omission. No zero abundance or unique kinetics inferred. |
| namedcheck | /private/tmp/cmm-round73-carbonates-independent/artinite-final-named.log; Actual reviewer execution, terminal exit0 | supports | Named record or trusted-base history validation passed; offline validation does not prove science. |
| historycheck | /private/tmp/cmm-round73-carbonates-independent/artinite-final-history.log; Actual reviewer execution, terminal exit0 | supports | Named record or trusted-base history validation passed; offline validation does not prove science. |
| batch | /private/tmp/cmm-round73-final-gates.json; Actual coordinator finalbatch terminal receipt and retained log | supports | just check,require-records and trusted-base history completed successfully for corrected cohort. |

## Limits And Additional Notes

- No experimental replication,raw diffraction refit or measurement uncertainty reconstruction.
- Source contradictions are preserved,not repaired. No criticality designation or industrial deployment inferred.
- Current exactDOI correction/erratum/retraction searches on2026-10-14 returned original publisher pages and related references but no applicable notice; first returned windows only,no exhaustive pagination.
- Raw originals independently read from shared curator downloads,not independently downloaded.
- Initial owner-only inspection retained separately; this observation adds exact canonical history inputs after reading those files.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T141419Z-artinite-round73-final
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of artinite
started_at: '2026-10-14T14:14:06.765443Z'
finished_at: '2026-10-14T14:14:19.924871Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record and canonical histories authored by round68_phosphates;
    reviewer authored CIGS and made no edits to either carbonate owner/history. Shared
    acquired originals were independently read and visually inspected.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified scientific acceptance with explicit source and causal limits; all
  required gates passed.
source:
  git_revision: ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3
  state: working_tree
  inputs:
  - path: data/records/artinite.yaml
    sha256: 54de7013ba0cef8aa1976fa8bb5e9ddcbc7979bff33c6db137e20d02223235c4
    role: target
  - path: history/records/artinite/2026-10-14T135947Z-codex-a1da31.yaml
    sha256: b532a5a513ae03f4be3e5b0b4e094de0dbc28910997b353156035a19de3d34de
    role: context
  - path: history/records/artinite/2026-10-14T140827Z-codex-dbfd84.yaml
    sha256: 1015c069a28e772c0d78d5058cab880ce5aed5b67ff5d5890ab3bff2ca27b978
    role: context
scope:
  description: Full maintained record and history; independent primary-source scientific
    reassessment.
  selection: Assigned frozen owner, native inspect before final assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:artinite
targets:
- target_id: cmmmech:artinite
  path: data/records/artinite.yaml
  label: Artinite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/artinite.yaml
    role: maintained_record
checks:
- check_id: named
  name: named validation
  command: uv run --locked cmmmech validate data/records/artinite.yaml
  status: passed
  required: true
  summary: Actual execution completed with exit0.
  target_ids:
  - cmmmech:artinite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - namedcheck
- check_id: history
  name: history validation
  command: uv run --locked cmmmech validate-history --base ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3
  status: passed
  required: true
  summary: Actual execution completed with exit0.
  target_ids:
  - cmmmech:artinite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - historycheck
- check_id: batch0
  name: Completed batch gate
  command: just check
  status: passed
  required: true
  summary: Receipt/log verified, exit0.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - batch
- check_id: batch1
  name: Completed batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Receipt/log verified, exit0.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed batch gate
  command: uv run --locked cmmmech validate-history --base ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3
  status: passed
  required: true
  summary: Receipt/log verified, exit0.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/artinite.yaml
  locator: Complete maintained owner and distinct inline events
  accessed_at: '2026-10-14T14:14:19.886406Z'
  support: supports
  summary: Compared all assertions to original methods, results, authority rows and
    graphics.
  snapshot_sha256: 54de7013ba0cef8aa1976fa8bb5e9ddcbc7979bff33c6db137e20d02223235c4
- evidence_id: history0
  kind: record_content
  reference: history/records/artinite/2026-10-14T135947Z-codex-a1da31.yaml
  locator: Canonical immutable sidecar
  accessed_at: '2026-10-14T14:14:19.888514Z'
  support: supports
  summary: Actual actor, event, UTC and target agree with the curation change.
  snapshot_sha256: b532a5a513ae03f4be3e5b0b4e094de0dbc28910997b353156035a19de3d34de
- evidence_id: history1
  kind: record_content
  reference: history/records/artinite/2026-10-14T140827Z-codex-dbfd84.yaml
  locator: Canonical immutable sidecar
  accessed_at: '2026-10-14T14:14:19.890415Z'
  support: supports
  summary: Actual actor, event, UTC and target agree with the curation change.
  snapshot_sha256: 1015c069a28e772c0d78d5058cab880ce5aed5b67ff5d5890ab3bff2ca27b978
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Official September2026 list definitions and PDF page 16
  accessed_at: '2026-10-14T14:14:19.890557Z'
  support: supports
  summary: Grandfathered species formula and original-description year confirmed;
    no approval-number or criticality inference.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/artinite.pdf
  locator: Complete mineral entry
  accessed_at: '2026-10-14T14:14:19.899590Z'
  support: supports
  summary: Mineral identity distinct from neighbouring magnesium carbonate phases.
  snapshot_sha256: a08816173ed21f953a195c2273b4d9136954f4fb35f45953ca172ef025d6ef7d
- evidence_id: main
  kind: primary_source
  reference: https://doi.org/10.3151/jact.24.174
  locator: Complete17page original; Sections2.1–2.4,3.1–3.4; Figures1–10; Tables1–6
  accessed_at: '2026-10-14T14:14:19.899946Z'
  support: supports
  summary: Original source supports separate water and concentrated precipitation
    arms, with measured/modelled distinctions and impurity limits. All original page
    graphics inspected.
  snapshot_sha256: cdbb12dfa60e0850189dab5203e00ca7d1b71575f258ffe12c35cf208bb5abba
- evidence_id: si
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/jact/24/4/24_174/_supplement/_download/24_174_1.pdf
  locator: Complete18page SI; FiguresS1–S16,TablesS1–S2
  accessed_at: '2026-10-14T14:14:19.905141Z'
  support: supports
  summary: Original figures retain 5C labels versus7C methods and S14 A-label versus
    TableS2 phase omission. No zero abundance or unique kinetics inferred.
  snapshot_sha256: 3d5fab52975f1b567e61c5ed35e4983c08322e01f5726a4ebf93c45914b49c45
- evidence_id: namedcheck
  kind: validation
  reference: /private/tmp/cmm-round73-carbonates-independent/artinite-final-named.log
  locator: Actual reviewer execution, terminal exit0
  accessed_at: '2026-10-14T14:14:19.923955Z'
  support: supports
  summary: Named record or trusted-base history validation passed; offline validation
    does not prove science.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: historycheck
  kind: validation
  reference: /private/tmp/cmm-round73-carbonates-independent/artinite-final-history.log
  locator: Actual reviewer execution, terminal exit0
  accessed_at: '2026-10-14T14:14:19.924126Z'
  support: supports
  summary: Named record or trusted-base history validation passed; offline validation
    does not prove science.
  snapshot_sha256: cbe1c412b034fed957a71444acd4ab863bafc724db0b5a2c01ee4aa66af71fbd
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round73-final-gates.json
  locator: Actual coordinator finalbatch terminal receipt and retained log
  accessed_at: '2026-10-14T14:14:19.924509Z'
  support: supports
  summary: just check,require-records and trusted-base history completed successfully
    for corrected cohort.
  snapshot_sha256: 484909cb53410de5f4e1def132320739ec1c26f81c24f575fa23e9c03aa31791
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species boundary
  outcome: supported
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - record
  - ima
  - handbook
  summary: Formula and grandfathered status correctly scoped; no inherited criticality.
- assessment_id: water
  area: evidence
  topic: Dissolution versus phase persistence
  outcome: supported
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - record
  - main
  - si
  summary: Natural artinite remains dominant in sampled exsitu solids; minor impurities
    and brucite/HCB prevent pure-phase/universal stability claims.
- assessment_id: precipitation
  area: evidence
  topic: Separate concentrated-solution experiment
  outcome: supported
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - record
  - main
  - si
  summary: Table5/S2 mixed phases and time/temperature conditions are correctly distinguished;
    DY+A at20C/3months retained.
- assessment_id: uncertainty
  area: scope
  topic: Measured versus calculated and contradictory labels
  outcome: supported
  target_ids:
  - cmmmech:artinite
  evidence_ids:
  - record
  - main
  - si
  summary: Solubility/IAP models, Raman temperature/phase labels and limited causal
    interpretation remain explicit; no microbial or industrial outcome.
findings:
- finding_id: F1
  issue_key: CMMMech.artinite.daily-shaking-duration
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Do not extend the initial shaking duration to daily shaking
  description: Both mechanism contexts imply one-minute shaking on workdays. Sections2.2–2.3
    specify one minute before storage, then daily shaking during workdays without
    giving its duration. Preserve initial duration and daily frequency separately;
    do not invent a daily duration.
  target_ids:
  - cmmmech:artinite
  field_paths:
  - mechanisms[id=natural_artinite_water_dissolution].context
  - mechanisms[id=oversaturation_artinite_intermediate].context
  evidence_ids:
  - record
  - main
  rule_id: conditions-match-primary-methods
  native_severity: minor
  normalization_reason: Bounded methods wording overstatement; phase identities and
    outcomes remain supported.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/artinite.yaml
    role: maintained_record
  disposition_reason: Independently re-read p176 and both corrected context strings.
    Initial one-minute shaking is separated from daily workday shaking whose duration
    is explicitly not reported. New EDIT sidecar and inline event appended; initial
    review and history preserved. Named and corrected batch validation passed.
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261014T140422Z-artinite-round73-initial
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/236
actions: []
limitations:
- No experimental replication,raw diffraction refit or measurement uncertainty reconstruction.
- Source contradictions are preserved,not repaired. No criticality designation or
  industrial deployment inferred.
- Current exactDOI correction/erratum/retraction searches on2026-10-14 returned original
  publisher pages and related references but no applicable notice; first returned
  windows only,no exhaustive pagination.
- Raw originals independently read from shared curator downloads,not independently
  downloaded.
notes:
- Initial owner-only inspection retained separately; this observation adds exact canonical
  history inputs after reading those files.
tags:
- round73
- artinite
- independent
- final
```
