# Independent scientific review of boltwoodite

- Review: 20261016T025741Z-boltwoodite-round109-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T02:41:59.956045Z
- Finished UTC: 2026-10-16T02:57:41.405360Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Accepted narrow mineral claims supported; no corrective owner finding. Source omissions and inaccessible later-primary evidence remain explicit.

## Scope And Provenance

Entire assigned owner/history and claim-bearing primary evidence; no experiment replication or raw-data reanalysis.

Selection: Native inspect captured exact working-tree source inputs before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a11e47d1c90806e056bd60610a0edd2cf77813a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:boltwoodite | data/records/boltwoodite.yaml | maintained | boltwoodite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Completed batch gate 1 | passed | True | cmmmech:boltwoodite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 2 | passed | True | cmmmech:boltwoodite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 3 | passed | True | cmmmech:boltwoodite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 4 | passed | True | cmmmech:boltwoodite | Terminal success and retained log verified; final owner hash matches inspected bytes. |

## Scientific And Domain Assessments

### Mineral identity and scope

identity: supported. Targets: cmmmech:boltwoodite.

Current authority and primary material identity agree; mineral/element boundaries and specimen composition retained.

### Accepted primary claims and limits

evidence: supported. Targets: cmmmech:boltwoodite.

The185C7day preparation, calculated1.3MPa and maximum qualitative yield remain separate from water-only conversion and25C nitrogen dissolution. Original1.4micrometre filter and30day endpoint are exact. The totalU g/L values are not free-ion activity, Ksp, rate or recovered percentage. Silica gel, missing loading/volume/replicates, natural/synthetic hydration and incomplete later-primary access remain explicit.

### Actual provenance and bounded search

provenance: supported. Targets: cmmmech:boltwoodite.

Distinct actual CREATE history and inline event; source versions and acquisition limits explicit. No later-study measurements adopted from abstracts.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/boltwoodite.yaml; Entire native-inspected owner; local artifact /private/tmp/CMMMech-expansion-round109-20261016/data/records/boltwoodite.yaml | supports | Current exact bytes and field scope independently assessed. |
| history | history/records/boltwoodite/2026-10-16T024035Z-codex-493ba2.yaml; Canonical CREATE sidecar and separate inline event; local artifact /private/tmp/CMMMech-expansion-round109-20261016/history/records/boltwoodite/2026-10-16T024035Z-codex-493ba2.yaml | supports | Actual actor/model, target, time and change description match this curation. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Current rows PDF28/53 independently visually inspected; definitions from source dossier; local artifact /private/tmp/cmm-round109-uranium-research/ima202609.pdf | supports | Mineral identity, formula and grandfathered year are supported. No invented numbered approval ID or inherited criticality. |
| search | Independent exact-title/DOI correction and related-source search; Four bounded web queries on2026-10-16: Burns1998title, Vochten1997title, PlasilDOI with correction/erratum/retraction; related microbial dissolution; local artifact /private/tmp/cmm-round109-uranium-independent-search.json | context_only | No affecting notice surfaced in returned windows. Related sodium-boltwoodite microbial and mixed-sediment studies do not establish this potassium-rich or copper-mineral mechanism. |
| dossier | research/sources/round109-uranium/20261016T024355Z-source-investigation.json; Curator provenance, source manifest and bounded dedup scope independently read; local artifact /private/tmp/CMMMech-expansion-round109-20261016/research/sources/round109-uranium/20261016T024355Z-source-investigation.json | context_only | Acquisition and hidden/ignored-inclusive scope are retained; this dossier is not itself independent primary evidence. |
| structure | https://www.rruff.net/doclib/cm/vol36/CM36_1069.pdf; Original1069–1075 text; pages1069–1071/1073 visuals and Tables1–2, structural formula; local artifact /private/tmp/cmm-round109-uranium-research/burns1998.pdf | supports | Natural near-Rossing crystal, partial alkali occupancies and calculated microprobe water support specimen-specific structure; proposed radionuclide retention is not accepted. |
| experiment | https://www.rruff.net/doclib/cm/vol35/CM35_735.pdf; Methodspp736–737, originalTable3p739 and discussionp740 independently textually/visually checked; local artifact /private/tmp/cmm-round108-uranium-research/vochten1997.pdf | supports | Synthetic preparation, later soddyite and total filtered uranium observations are source-specific. Seven exact concentration cells and empirical1.30water agree with original images. |
| batch | Completed exact-byte batch receipt; Commands/base/cwd/terminal exits/log checksum and exact record inputs independently verified; local artifact /private/tmp/cmm-round109-final-gates.json | supports | All required batch gates passed on these unchanged owner bytes. |

## Limits And Additional Notes

- Independent agent review is not external human peer review. Original claim-bearing pages/graphics and CIF fields were checked; not every page was independently visually reread.
- No experimental replication, full diffraction re-refinement or universally exhaustive source/notice search.
- Missing later primary papers and experimental details remain follow-up work; no guessed yields, microbial scope or deployment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T025741Z-boltwoodite-round109-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of boltwoodite
started_at: '2026-10-16T02:41:59.956045Z'
finished_at: '2026-10-16T02:57:41.405360Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored this owner/history; root authored a separate
    refinery-resource record and independently inspected the frozen mineral bytes
    and original primary sources without editing this owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Accepted narrow mineral claims supported; no corrective owner finding. Source
  omissions and inaccessible later-primary evidence remain explicit.
source:
  git_revision: a11e47d1c90806e056bd60610a0edd2cf77813a9
  state: working_tree
  inputs:
  - path: data/records/boltwoodite.yaml
    sha256: eb8934a9cd33839c5b2b6fc65993c35643c637e9da731b5fe9790aee83258e9c
    role: target
  - path: history/records/boltwoodite/2026-10-16T024035Z-codex-493ba2.yaml
    sha256: a586e3161ca5f4d0e85958440a1fd0d2f6094d8aa85080d37dedec99c7c5d489
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:boltwoodite
  path: data/records/boltwoodite.yaml
  label: boltwoodite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boltwoodite.yaml
    role: maintained_record
scope:
  description: Entire assigned owner/history and claim-bearing primary evidence; no
    experiment replication or raw-data reanalysis.
  selection: Native inspect captured exact working-tree source inputs before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:boltwoodite
checks:
- check_id: batch1
  name: Completed batch gate 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal success and retained log verified; final owner hash matches inspected
    bytes.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed batch gate 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal success and retained log verified; final owner hash matches inspected
    bytes.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed batch gate 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base a11e47d1c90806e056bd60610a0edd2cf77813a9
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal success and retained log verified; final owner hash matches inspected
    bytes.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed batch gate 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal success and retained log verified; final owner hash matches inspected
    bytes.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/boltwoodite.yaml
  locator: Entire native-inspected owner; local artifact /private/tmp/CMMMech-expansion-round109-20261016/data/records/boltwoodite.yaml
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: eb8934a9cd33839c5b2b6fc65993c35643c637e9da731b5fe9790aee83258e9c
  support: supports
  summary: Current exact bytes and field scope independently assessed.
- evidence_id: history
  kind: record_content
  reference: history/records/boltwoodite/2026-10-16T024035Z-codex-493ba2.yaml
  locator: Canonical CREATE sidecar and separate inline event; local artifact /private/tmp/CMMMech-expansion-round109-20261016/history/records/boltwoodite/2026-10-16T024035Z-codex-493ba2.yaml
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: a586e3161ca5f4d0e85958440a1fd0d2f6094d8aa85080d37dedec99c7c5d489
  support: supports
  summary: Actual actor/model, target, time and change description match this curation.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Current rows PDF28/53 independently visually inspected; definitions from
    source dossier; local artifact /private/tmp/cmm-round109-uranium-research/ima202609.pdf
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Mineral identity, formula and grandfathered year are supported. No invented
    numbered approval ID or inherited criticality.
- evidence_id: search
  kind: search
  reference: Independent exact-title/DOI correction and related-source search
  locator: 'Four bounded web queries on2026-10-16: Burns1998title, Vochten1997title,
    PlasilDOI with correction/erratum/retraction; related microbial dissolution; local
    artifact /private/tmp/cmm-round109-uranium-independent-search.json'
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: 466ba9d7e22582bc734e871f41f2c2bb80f637765ade8373fb75237fd9697933
  support: context_only
  summary: No affecting notice surfaced in returned windows. Related sodium-boltwoodite
    microbial and mixed-sediment studies do not establish this potassium-rich or copper-mineral
    mechanism.
  search_scope: First returned result sets, no exhaustive citation search; primary
    leads separated from secondary search results; no author outreach.
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round109-uranium/20261016T024355Z-source-investigation.json
  locator: Curator provenance, source manifest and bounded dedup scope independently
    read; local artifact /private/tmp/CMMMech-expansion-round109-20261016/research/sources/round109-uranium/20261016T024355Z-source-investigation.json
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: 3b96f8e43520e757d0f662b9b91aba49668eedeee12c6da28239c6df01fcc2e1
  support: context_only
  summary: Acquisition and hidden/ignored-inclusive scope are retained; this dossier
    is not itself independent primary evidence.
- evidence_id: structure
  kind: primary_source
  reference: https://www.rruff.net/doclib/cm/vol36/CM36_1069.pdf
  locator: Original1069–1075 text; pages1069–1071/1073 visuals and Tables1–2, structural
    formula; local artifact /private/tmp/cmm-round109-uranium-research/burns1998.pdf
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: dc89f42a3024fd5a7f2f96c9de7134bed011f5724747ccbae1c2dbc16fd39c7c
  support: supports
  summary: Natural near-Rossing crystal, partial alkali occupancies and calculated
    microprobe water support specimen-specific structure; proposed radionuclide retention
    is not accepted.
- evidence_id: experiment
  kind: primary_source
  reference: https://www.rruff.net/doclib/cm/vol35/CM35_735.pdf
  locator: Methodspp736–737, originalTable3p739 and discussionp740 independently textually/visually
    checked; local artifact /private/tmp/cmm-round108-uranium-research/vochten1997.pdf
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: e1318999e81c0e2da373a60798c71675b279b42c6ac4c29fa4a2af188cd5658d
  support: supports
  summary: Synthetic preparation, later soddyite and total filtered uranium observations
    are source-specific. Seven exact concentration cells and empirical1.30water agree
    with original images.
- evidence_id: batch
  kind: validation
  reference: Completed exact-byte batch receipt
  locator: Commands/base/cwd/terminal exits/log checksum and exact record inputs independently
    verified; local artifact /private/tmp/cmm-round109-final-gates.json
  accessed_at: '2026-10-16T02:57:41.405360Z'
  snapshot_sha256: bcc373fdff60063fbe3c70df3634ea3532fbe628ed76f1be61dcbc8b7174150d
  support: supports
  summary: All required batch gates passed on these unchanged owner bytes.
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity and scope
  outcome: supported
  summary: Current authority and primary material identity agree; mineral/element
    boundaries and specimen composition retained.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - owner
  - ima
  - structure
- assessment_id: science
  area: evidence
  topic: Accepted primary claims and limits
  outcome: supported
  summary: The185C7day preparation, calculated1.3MPa and maximum qualitative yield
    remain separate from water-only conversion and25C nitrogen dissolution. Original1.4micrometre
    filter and30day endpoint are exact. The totalU g/L values are not free-ion activity,
    Ksp, rate or recovered percentage. Silica gel, missing loading/volume/replicates,
    natural/synthetic hydration and incomplete later-primary access remain explicit.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - owner
  - structure
  - experiment
- assessment_id: provenance
  area: provenance
  topic: Actual provenance and bounded search
  outcome: supported
  summary: Distinct actual CREATE history and inline event; source versions and acquisition
    limits explicit. No later-study measurements adopted from abstracts.
  target_ids:
  - cmmmech:boltwoodite
  evidence_ids:
  - history
  - dossier
  - search
findings: []
actions: []
limitations:
- Independent agent review is not external human peer review. Original claim-bearing
  pages/graphics and CIF fields were checked; not every page was independently visually
  reread.
- No experimental replication, full diffraction re-refinement or universally exhaustive
  source/notice search.
- Missing later primary papers and experimental details remain follow-up work; no
  guessed yields, microbial scope or deployment.
```
