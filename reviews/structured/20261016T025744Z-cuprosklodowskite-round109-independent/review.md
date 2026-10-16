# Independent scientific review of cuprosklodowskite

- Review: 20261016T025744Z-cuprosklodowskite-round109-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T02:41:59.943670Z
- Finished UTC: 2026-10-16T02:57:44.253649Z
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
| cmmmech:cuprosklodowskite | data/records/cuprosklodowskite.yaml | maintained | cuprosklodowskite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Completed batch gate 1 | passed | True | cmmmech:cuprosklodowskite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 2 | passed | True | cmmmech:cuprosklodowskite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 3 | passed | True | cmmmech:cuprosklodowskite | Terminal success and retained log verified; final owner hash matches inspected bytes. |
| Completed batch gate 4 | passed | True | cmmmech:cuprosklodowskite | Terminal success and retained log verified; final owner hash matches inspected bytes. |

## Scientific And Domain Assessments

### Mineral identity and scope

identity: supported. Targets: cmmmech:cuprosklodowskite.

Current authority and primary material identity agree; mineral/element boundaries and specimen composition retained.

### Accepted primary claims and limits

evidence: supported. Targets: cmmmech:cuprosklodowskite.

Identity-only natural Cu uranyl silicate record. P-1, distorted sixfold Cu linkage, formula and reported refinement agree with originalarticle/CIF. Two temperature fields295(11)K and287K are retained without inventing a unified experimental temperature. No dissolution, microorganism, criticality or deployment is inferred from chemistry or related-mineral studies.

### Actual provenance and bounded search

provenance: supported. Targets: cmmmech:cuprosklodowskite.

Distinct actual CREATE history and inline event; source versions and acquisition limits explicit. No later-study measurements adopted from abstracts.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/cuprosklodowskite.yaml; Entire native-inspected owner; local artifact /private/tmp/CMMMech-expansion-round109-20261016/data/records/cuprosklodowskite.yaml | supports | Current exact bytes and field scope independently assessed. |
| history | history/records/cuprosklodowskite/2026-10-16T024054Z-codex-9655ac.yaml; Canonical CREATE sidecar and separate inline event; local artifact /private/tmp/CMMMech-expansion-round109-20261016/history/records/cuprosklodowskite/2026-10-16T024054Z-codex-9655ac.yaml | supports | Actual actor/model, target, time and change description match this curation. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Current rows PDF28/53 independently visually inspected; definitions from source dossier; local artifact /private/tmp/cmm-round109-uranium-research/ima202609.pdf | supports | Mineral identity, formula and grandfathered year are supported. No invented numbered approval ID or inherited criticality. |
| search | Independent exact-title/DOI correction and related-source search; Four bounded web queries on2026-10-16: Burns1998title, Vochten1997title, PlasilDOI with correction/erratum/retraction; related microbial dissolution; local artifact /private/tmp/cmm-round109-uranium-independent-search.json | context_only | No affecting notice surfaced in returned windows. Related sodium-boltwoodite microbial and mixed-sediment studies do not establish this potassium-rich or copper-mineral mechanism. |
| dossier | research/sources/round109-uranium/20261016T024355Z-source-investigation.json; Curator provenance, source manifest and bounded dedup scope independently read; local artifact /private/tmp/CMMMech-expansion-round109-20261016/research/sources/round109-uranium/20261016T024355Z-source-investigation.json | context_only | Acquisition and hidden/ignored-inclusive scope are retained; this dossier is not itself independent primary evidence. |
| structure | https://doi.org/10.3390/min8120551; New diffractionsection2.1/Table2; section3.1 and originalFigures2/4; pages2/4/7 visually checked; local artifact /private/tmp/cmm-round108-uranium-research/plasil2018.pdf | supports | Review-labelled article contains original new natural-crystal data. Museum diffraction provenance is not assumed to match separately photographed Musunoi specimen; Cu coordination distinction supported. |
| experiment | Original Plasil2018 supplementary cuprosklodowskite_final.cif; Formula, cell, twin, temperature and refinement fields directly read; local artifact /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/cuprosklodowskite_final.cif | supports | Cell/R1/1033observed reflections match Table2; differing temperature entries and incomplete template are disclosed; no independent re-refinement claimed. |
| batch | Completed exact-byte batch receipt; Commands/base/cwd/terminal exits/log checksum and exact record inputs independently verified; local artifact /private/tmp/cmm-round109-final-gates.json | supports | All required batch gates passed on these unchanged owner bytes. |

## Limits And Additional Notes

- Independent agent review is not external human peer review. Original claim-bearing pages/graphics and CIF fields were checked; not every page was independently visually reread.
- No experimental replication, full diffraction re-refinement or universally exhaustive source/notice search.
- Missing later primary papers and experimental details remain follow-up work; no guessed yields, microbial scope or deployment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T025744Z-cuprosklodowskite-round109-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of cuprosklodowskite
started_at: '2026-10-16T02:41:59.943670Z'
finished_at: '2026-10-16T02:57:44.253649Z'
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
  - path: data/records/cuprosklodowskite.yaml
    sha256: dff1fe6924c4e99765ee8a433dc4e63a64f5bae8e65fc4ade4f0976ad99db3a6
    role: target
  - path: history/records/cuprosklodowskite/2026-10-16T024054Z-codex-9655ac.yaml
    sha256: d478e7877210a8fe30e9a068360f179bc188c735f8fc079543ce55d73e0e9011
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:cuprosklodowskite
  path: data/records/cuprosklodowskite.yaml
  label: cuprosklodowskite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprosklodowskite.yaml
    role: maintained_record
scope:
  description: Entire assigned owner/history and claim-bearing primary evidence; no
    experiment replication or raw-data reanalysis.
  selection: Native inspect captured exact working-tree source inputs before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cuprosklodowskite
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
  - cmmmech:cuprosklodowskite
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
  - cmmmech:cuprosklodowskite
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
  - cmmmech:cuprosklodowskite
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
  - cmmmech:cuprosklodowskite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/cuprosklodowskite.yaml
  locator: Entire native-inspected owner; local artifact /private/tmp/CMMMech-expansion-round109-20261016/data/records/cuprosklodowskite.yaml
  accessed_at: '2026-10-16T02:57:44.253649Z'
  snapshot_sha256: dff1fe6924c4e99765ee8a433dc4e63a64f5bae8e65fc4ade4f0976ad99db3a6
  support: supports
  summary: Current exact bytes and field scope independently assessed.
- evidence_id: history
  kind: record_content
  reference: history/records/cuprosklodowskite/2026-10-16T024054Z-codex-9655ac.yaml
  locator: Canonical CREATE sidecar and separate inline event; local artifact /private/tmp/CMMMech-expansion-round109-20261016/history/records/cuprosklodowskite/2026-10-16T024054Z-codex-9655ac.yaml
  accessed_at: '2026-10-16T02:57:44.253649Z'
  snapshot_sha256: d478e7877210a8fe30e9a068360f179bc188c735f8fc079543ce55d73e0e9011
  support: supports
  summary: Actual actor/model, target, time and change description match this curation.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Current rows PDF28/53 independently visually inspected; definitions from
    source dossier; local artifact /private/tmp/cmm-round109-uranium-research/ima202609.pdf
  accessed_at: '2026-10-16T02:57:44.253649Z'
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
  accessed_at: '2026-10-16T02:57:44.253649Z'
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
  accessed_at: '2026-10-16T02:57:44.253649Z'
  snapshot_sha256: 3b96f8e43520e757d0f662b9b91aba49668eedeee12c6da28239c6df01fcc2e1
  support: context_only
  summary: Acquisition and hidden/ignored-inclusive scope are retained; this dossier
    is not itself independent primary evidence.
- evidence_id: structure
  kind: primary_source
  reference: https://doi.org/10.3390/min8120551
  locator: New diffractionsection2.1/Table2; section3.1 and originalFigures2/4; pages2/4/7
    visually checked; local artifact /private/tmp/cmm-round108-uranium-research/plasil2018.pdf
  accessed_at: '2026-10-16T02:57:44.253649Z'
  snapshot_sha256: f96034e17b57086c19566d0f63f9b28bc94bc8c47de52e368c391204ba87e3d4
  support: supports
  summary: Review-labelled article contains original new natural-crystal data. Museum
    diffraction provenance is not assumed to match separately photographed Musunoi
    specimen; Cu coordination distinction supported.
- evidence_id: experiment
  kind: primary_source
  reference: Original Plasil2018 supplementary cuprosklodowskite_final.cif
  locator: Formula, cell, twin, temperature and refinement fields directly read; local
    artifact /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/cuprosklodowskite_final.cif
  accessed_at: '2026-10-16T02:57:44.253649Z'
  snapshot_sha256: 87a2fd325e3ef0e48ca9c3491a5f2896ba9424d686b4c9ac8c9cf36da6860f00
  support: supports
  summary: Cell/R1/1033observed reflections match Table2; differing temperature entries
    and incomplete template are disclosed; no independent re-refinement claimed.
- evidence_id: batch
  kind: validation
  reference: Completed exact-byte batch receipt
  locator: Commands/base/cwd/terminal exits/log checksum and exact record inputs independently
    verified; local artifact /private/tmp/cmm-round109-final-gates.json
  accessed_at: '2026-10-16T02:57:44.253649Z'
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
  - cmmmech:cuprosklodowskite
  evidence_ids:
  - owner
  - ima
  - structure
- assessment_id: science
  area: evidence
  topic: Accepted primary claims and limits
  outcome: supported
  summary: Identity-only natural Cu uranyl silicate record. P-1, distorted sixfold
    Cu linkage, formula and reported refinement agree with originalarticle/CIF. Two
    temperature fields295(11)K and287K are retained without inventing a unified experimental
    temperature. No dissolution, microorganism, criticality or deployment is inferred
    from chemistry or related-mineral studies.
  target_ids:
  - cmmmech:cuprosklodowskite
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
  - cmmmech:cuprosklodowskite
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
