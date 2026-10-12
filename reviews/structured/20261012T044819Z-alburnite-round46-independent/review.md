# Independent scientific review of alburnite

- Review: 20261012T044819Z-alburnite-round46-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T04:43:40Z
- Finished UTC: 2026-10-12T04:48:19Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The approved mineral identity is supported. The disputed arsenian occurrence and the authors’ correction of a separate 2015 analysis are accurately distinguished; unavailable 2014 details are deferred. No corrective findings.

## Scope And Provenance

Whole frozen mineral record and CREATE provenance; original approval, dated IMA status and relevant contradictory primary evidence.

Selection: Independent peer review of new Ge mineral identity.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 94d743a1b8bb3fe595f96e88f4cdb54a4ee72375.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:alburnite | data/records/alburnite.yaml | maintained | Alburnite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:alburnite | Actually completed1record/0failed; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Completed cohort batch | passed | True | cmmmech:alburnite | Coordinator completed; receipt/raw log SHA256 verified: 8caead3980a6da1e7b4d54ea4895572c931741b48ccd353e542e8edf2b876b53. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 236.91s (0:03:56)<br>Checked 229 record(s); 0 failed.<br>Checked 272 history record(s); 0 error(s). |
| Completed cohort nonempty | passed | True | cmmmech:alburnite | Coordinator completed; receipt/raw log SHA256 verified: ff7ed8bc3fc67548605ba5d958c3f8057489701d8221b508c7670b58955b7dba. Checked 229 record(s); 0 failed. |
| Completed cohort history | passed | True | cmmmech:alburnite | Coordinator completed; receipt/raw log SHA256 verified: 17691e066e03358c6eabe98608db086af9b35dcc46fde40810e46ead5f061163. Checked 272 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Species and primary identity

identity: supported. Targets: cmmmech:alburnite.

The approved mineral identity is supported. The disputed arsenian occurrence and the authors’ correction of a separate 2015 analysis are accurately distinguished; unavailable 2014 details are deferred.

### Contradictory evidence and unasserted claims

evidence: supported. Targets: cmmmech:alburnite.

Record retains original source limits rather than treating announcements or uncertain phases as complete experimental evidence.

### History and exact-state review

provenance: supported. Targets: cmmmech:alburnite.

Captured inputs unchanged; actual checks, provenance and bounded searches support qualified pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/alburnite.yaml; Whole captured target | supports | Natural mineral identity, distinct material owner; absent optional mechanisms and criticality are deliberate. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pp1–2 and Alburnite p6 | supports | Current approved name, formula and proposal identifier independently checked against actual row; proposal prefix is not publication year. |
| approval | https://doi.org/10.1180/minmag.2013.077.1.01; Original Newsletter15 pp1 and10, IMA2012-073 | supports | Complete original announcement supports Ag8GeTe2S4, named type locality and approved distinct species. No unavailable 2014 analytical detail is imported. |
| counterevidence | https://igr.ro/wp-content/uploads/2019/10/2016_RJMD_vol_89_1-2.pdf; All six article pages93–98 (PDF97–102), Figures1–5, Table1; analytical correction p96 and unresolved symmetry p97 | supports | Optical/SEM-EDS methods and As-bearing phase are reported, while excess Ag and unresolved F-43m versus P213 identity prevent asserting confirmed composition. The charge-compensation artifact revises the authors’2015 associated-sulfotelluride report, not the2014 original description. |
| history | history/records/alburnite/2026-10-12T044046Z-codex-1643ca.yaml; Whole CREATE sidecar and inline event | supports | Actual actor/model/tool, target and creation details agree; no prior histories rewritten. |
| inspection | /private/tmp/cmm-round46-ge-independent-evidence.json; Independent visual/text checks and raw-byte integrity | supports | All declared curator raw artifacts hash-verified. Original pages and graphics inspected within stated scope; no fresh independent raw download claimed. |
| dedup | /private/tmp/cmm-round46-ge-review-dedup.log; Current bounded ownership search | supports | One maintained owner per species; earlier references are boundaries or deferred leads. Broader curator raw-root receipt retained in dossier. |
| notices | /private/tmp/cmm-round46-ge-review-web.json; Saved exact-name/title notice searches plus official CNMNC90 page | supports | Bounded search did not establish an affecting formal notice beyond the incorporated2016 analytical correction and2026 publication-status statement. Original2013 DOI open failed; downloaded original supports that claim. |
| checks | /private/tmp/cmm-round46-final-terminal.json; Actual terminal cohort receipts | supports | All three commands passed with verified raw hashes; validation does not prove scientific truth. |

## Limits And Additional Notes

- Identity support does not establish extraction, criticality or recovery performance.
- Complete original 2014 alburnite description is outside the inspected source set.
- Bounded duplicate and notice searches do not establish universal absence or source exhaustion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T044819Z-alburnite-round46-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of alburnite
started_at: '2026-10-12T04:43:40Z'
finished_at: '2026-10-12T04:48:19Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Peer /root/round43_hardmetal authored both Ge mineral records,
    histories and shared dossier. Root authored none of those inputs, captured native
    hashes before assessment, independently read relevant primary text and viewed
    original pages. Root curated separate cassiterite and coordinates publication.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The approved mineral identity is supported. The disputed arsenian occurrence
  and the authors’ correction of a separate 2015 analysis are accurately distinguished;
  unavailable 2014 details are deferred. No corrective findings.
source:
  git_revision: 94d743a1b8bb3fe595f96e88f4cdb54a4ee72375
  state: working_tree
  inputs:
  - path: data/records/alburnite.yaml
    sha256: bb980057adbe887790f25c5a357824179470eba8ca1ae21caab24473c7d50c1a
    role: target
  - path: history/records/alburnite/2026-10-12T044046Z-codex-1643ca.yaml
    sha256: f2e7df84e1ee88f36bce99cc3b9b4e5f8a1e4e6210e8cc3435461176a38413a7
    role: context
  - path: research/sources/round46-ge-minerals/20261012T044233Z-source-investigation.json
    sha256: 3ff5a68b78ab314205ef9efe4676221d34c51b11565936ffee1daecc8e55855c
    role: context
  - path: research/sources/round46-ge-minerals/20261012T044233Z-source-investigation.md
    sha256: 7a30e06c3545c262d214da31dc52c3b714526b82355107f8b243fcb988402848
    role: context
targets:
- target_id: cmmmech:alburnite
  path: data/records/alburnite.yaml
  label: Alburnite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/alburnite.yaml
    role: scientific_record
scope:
  description: Whole frozen mineral record and CREATE provenance; original approval,
    dated IMA status and relevant contradictory primary evidence.
  selection: Independent peer review of new Ge mineral identity.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:alburnite
  exclusions:
  - target: Unasserted full-description analytical details and microbial mechanisms
    reason: No unsupported experimental or deployment claim is inferred from mineral
      identity.
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/alburnite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alburnite
  summary: Actually completed1record/0failed; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Completed cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alburnite
  summary: 'Coordinator completed; receipt/raw log SHA256 verified: 8caead3980a6da1e7b4d54ea4895572c931741b48ccd353e542e8edf2b876b53.
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 236.91s (0:03:56)

    Checked 229 record(s); 0 failed.

    Checked 272 history record(s); 0 error(s).'
- check_id: nonempty
  name: Completed cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alburnite
  summary: 'Coordinator completed; receipt/raw log SHA256 verified: ff7ed8bc3fc67548605ba5d958c3f8057489701d8221b508c7670b58955b7dba.
    Checked 229 record(s); 0 failed.'
- check_id: history
  name: Completed cohort history
  command: uv run --locked cmmmech validate-history --base 94d743a1b8bb3fe595f96e88f4cdb54a4ee72375
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:alburnite
  summary: 'Coordinator completed; receipt/raw log SHA256 verified: 17691e066e03358c6eabe98608db086af9b35dcc46fde40810e46ead5f061163.
    Checked 272 history record(s); 0 error(s).'
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/alburnite.yaml
  locator: Whole captured target
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Natural mineral identity, distinct material owner; absent optional mechanisms
    and criticality are deliberate.
  snapshot_sha256: bb980057adbe887790f25c5a357824179470eba8ca1ae21caab24473c7d50c1a
- evidence_id: ima
  kind: primary_source
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pp1–2 and Alburnite p6
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Current approved name, formula and proposal identifier independently checked
    against actual row; proposal prefix is not publication year.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: approval
  kind: primary_source
  reference: https://doi.org/10.1180/minmag.2013.077.1.01
  locator: Original Newsletter15 pp1 and10, IMA2012-073
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Complete original announcement supports Ag8GeTe2S4, named type locality
    and approved distinct species. No unavailable 2014 analytical detail is imported.
  snapshot_sha256: ae0292756677e5ce97b3e6dcf9b717dd00e05aadf7a0046b572267f81c922b38
- evidence_id: counterevidence
  kind: primary_source
  reference: https://igr.ro/wp-content/uploads/2019/10/2016_RJMD_vol_89_1-2.pdf
  locator: All six article pages93–98 (PDF97–102), Figures1–5, Table1; analytical
    correction p96 and unresolved symmetry p97
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Optical/SEM-EDS methods and As-bearing phase are reported, while excess
    Ag and unresolved F-43m versus P213 identity prevent asserting confirmed composition.
    The charge-compensation artifact revises the authors’2015 associated-sulfotelluride
    report, not the2014 original description.
  snapshot_sha256: a6dd0942238a9e6bdc25b9caa66dff6fe8680dff1ebd9aefd9dc6994cc7b93b7
- evidence_id: history
  kind: record_content
  reference: history/records/alburnite/2026-10-12T044046Z-codex-1643ca.yaml
  locator: Whole CREATE sidecar and inline event
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Actual actor/model/tool, target and creation details agree; no prior histories
    rewritten.
  snapshot_sha256: f2e7df84e1ee88f36bce99cc3b9b4e5f8a1e4e6210e8cc3435461176a38413a7
- evidence_id: inspection
  kind: record_content
  reference: /private/tmp/cmm-round46-ge-independent-evidence.json
  locator: Independent visual/text checks and raw-byte integrity
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: All declared curator raw artifacts hash-verified. Original pages and graphics
    inspected within stated scope; no fresh independent raw download claimed.
  snapshot_sha256: fdb25801b5b3dca4147afb355d41e275ba453a492f9ed82635ca3554d078dfda
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round46-ge-review-dedup.log
  locator: Current bounded ownership search
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: One maintained owner per species; earlier references are boundaries or
    deferred leads. Broader curator raw-root receipt retained in dossier.
  snapshot_sha256: 5b25987db3606f8ea53657cb6ebf95bf17a87f32d78edab2203663f015c22df9
  search_scope: rg --no-ignore --hidden --follow over current data/records,research,reviews,history;
    max-column preview; raw curator search not rerun; unrelated trees and unextracted
    binaries excluded.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round46-ge-review-web.json
  locator: Saved exact-name/title notice searches plus official CNMNC90 page
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: Bounded search did not establish an affecting formal notice beyond the
    incorporated2016 analytical correction and2026 publication-status statement. Original2013
    DOI open failed; downloaded original supports that claim.
  snapshot_sha256: 8a7090ab7f0d83ed08b8bf157071db859cca71714fae51f96e913feff984bed3
  search_scope: First returned sets for three saved title/name queries on2026-10-12,
    plus named direct opens; no exhaustive pagination.
- evidence_id: checks
  kind: validation
  reference: /private/tmp/cmm-round46-final-terminal.json
  locator: Actual terminal cohort receipts
  accessed_at: '2026-10-12T04:48:19Z'
  support: supports
  summary: All three commands passed with verified raw hashes; validation does not
    prove scientific truth.
  snapshot_sha256: 4e2d9f922583839cb1e67c765f44ed644126bc8cd7d72691734b7a34d79e8531
assessments:
- assessment_id: identity
  area: identity
  topic: Species and primary identity
  outcome: supported
  target_ids:
  - cmmmech:alburnite
  evidence_ids:
  - record
  - ima
  - approval
  summary: The approved mineral identity is supported. The disputed arsenian occurrence
    and the authors’ correction of a separate 2015 analysis are accurately distinguished;
    unavailable 2014 details are deferred.
- assessment_id: limits
  area: evidence
  topic: Contradictory evidence and unasserted claims
  outcome: supported
  target_ids:
  - cmmmech:alburnite
  evidence_ids:
  - counterevidence
  - record
  summary: Record retains original source limits rather than treating announcements
    or uncertain phases as complete experimental evidence.
- assessment_id: provenance
  area: provenance
  topic: History and exact-state review
  outcome: supported
  target_ids:
  - cmmmech:alburnite
  evidence_ids:
  - history
  - inspection
  - dedup
  - notices
  - checks
  summary: Captured inputs unchanged; actual checks, provenance and bounded searches
    support qualified pass.
findings: []
actions: []
limitations:
- Identity support does not establish extraction, criticality or recovery performance.
- Complete original 2014 alburnite description is outside the inspected source set.
- Bounded duplicate and notice searches do not establish universal absence or source
  exhaustion.
tags:
- round46
- independent
- mineral
- identity
```
