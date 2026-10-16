# Independent scientific review of Vandenbrandeite

- Review: 20261016T071840Z-vandenbrandeite-round114-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T06:55:04.730079Z
- Finished UTC: 2026-10-16T07:18:40.123430Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Narrow accepted scientific claims supported; source uncertainties remain explicit. No corrective owner defect identified in this scope.

## Scope And Provenance

Entire owner and actual history reviewed at claim level; no experiment replication, structure re-refinement or calculated-model reproduction.

Selection: Native capture before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 93f90797512dc8d1db3df9ce2e4994c475b1a4fe.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:vandenbrandeite | data/records/vandenbrandeite.yaml | maintained | Vandenbrandeite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Required final gate | passed | True | cmmmech:vandenbrandeite | Terminal receipt/log verified; exact owner hash matches. |
| Required final gate | passed | True | cmmmech:vandenbrandeite | Terminal receipt/log verified; exact owner hash matches. |
| Required final gate | passed | True | cmmmech:vandenbrandeite | Terminal receipt/log verified; exact owner hash matches. |
| Required final gate | passed | True | cmmmech:vandenbrandeite | Terminal receipt/log verified; exact owner hash matches. |

## Scientific And Domain Assessments

### Natural species versus experimental material

identity: supported. Targets: cmmmech:vandenbrandeite.

Current species formula and separate natural/synthetic specimen populations are supported.

### Abiotic primary observations and limits

evidence: supported. Targets: cmmmech:vandenbrandeite.

Qualitative natural-mineral thermal alteration is supported; product assignments are author-reported, not reindexed. No universal onset temperature, pure recovered phase, extraction yield or repository performance follows from text-only diffraction or computed thermodynamics.

### Actual curation and source inspection

provenance: supported. Targets: cmmmech:vandenbrandeite.

Exact source versions, current history and bounded access/search limitations retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/vandenbrandeite.yaml; Entire exact native-inspected owner; retained /private/tmp/CMMMech-expansion-round114-20261016/data/records/vandenbrandeite.yaml | supports | Material form, claims, conditions and uncertainty independently checked against full primary text and selected original figures. |
| history0 | history/records/vandenbrandeite/2026-10-16T065207Z-codex-c006f0.yaml; Entire canonical session and separate inline event; retained /private/tmp/CMMMech-expansion-round114-20261016/history/records/vandenbrandeite/2026-10-16T065207Z-codex-c006f0.yaml | supports | Actual CREATE target, actor, current timestamps and limited accepted scope agree. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions and visually inspected species rows PDF53/226; retained /private/tmp/cmm-round114-uranium-research/ima202609.pdf | supports | Both mineral formulas and grandfathered status match; historical description dates are not approval numbers. No element criticality inherited. |
| identity | https://doi.org/10.1039/C9RA09047A; Methods p40711 visually checked; structure/axis-setting discussion and Table1 pp40712-40714; theoretical methods versus experiments; retained /private/tmp/cmm-round114-uranium-research/vandenbrandeite2019-publisher-mirror.pdf | supports | Natural Musonoi room-temperature triclinic diffraction and constrained hydrogen refinement are separate from first-principles mechanical/thermodynamic predictions. Experimental and calculated coordinate settings are distinguished. |
| experiment | https://doi.org/10.1023/A:1013182917829; Complete seven-page text; methods pp177-178, thermal discussion pp180-181, Figures4/6 on original PDF5/7 visually inspected; retained /private/tmp/cmm-round114-uranium-research/vandenbrandeite2002.pdf | supports | Selected Kalongwe crystals retain trace impurities. Air furnace, missing protocol details, metal-normalized EDAX, gradual hydroxyl loss and author-reported mixed oxide XRD products agree with the owner. Threshold conflicts and unshown raw curves/patterns remain explicit. |
| search | Independent bounded DOI/title correction/retraction queries; Retrieved first web results on2026-10-16; retained /private/tmp/cmm-round114-uranium-independent-web.json | context_only | Publisher/primary metadata supports source identities. No applicable notice identified among returned results; this is not an exhaustive no-correction claim. |
| dedup | Independent current-owner search; Current data/records recursive hidden/ignored/followed matches; retained /private/tmp/cmm-round114-uranium-independent-dedup.txt | context_only | Only these dedicated owners and contextual references were found in this bounded current-corpus search. Agent dossiers separately retain broader research/raw-download dedup. |
| batch | Final exact-byte batch gates; Terminal command rows and hashed full log; retained /private/tmp/cmm-round114-final-gates-corrected.json | supports | just check, require-records, trusted-base history and generated-page freshness all passed with unchanged owner bytes. |

## Limits And Additional Notes

- Independent agent assessment is not external human peer review.
- Claim-bearing full text and selected original figures checked; not every primary page independently visually reread.
- Unacquired supplementary coordinates, original thermal/diffraction datasets and later2023 article remain evidence gaps; no deposited-data reanalysis claimed.
- Bounded notice searches and offline validation cannot settle retained source contradictions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T071840Z-vandenbrandeite-round114-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Vandenbrandeite
started_at: '2026-10-16T06:55:04.730079Z'
finished_at: '2026-10-16T07:18:40.123430Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored owner/history. Root independently inspected
    final hashes, claim-bearing full primary text, selected original figures, current
    IMA rows and bounded notice searches; shared acquisition did not substitute for
    assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Narrow accepted scientific claims supported; source uncertainties remain
  explicit. No corrective owner defect identified in this scope.
source:
  git_revision: 93f90797512dc8d1db3df9ce2e4994c475b1a4fe
  state: working_tree
  inputs:
  - path: data/records/vandenbrandeite.yaml
    sha256: 7e2fe85151c9023197b7933d178a6681138a2c4ff76a8178905c32cec42dceb9
    role: target
  - path: history/records/vandenbrandeite/2026-10-16T065207Z-codex-c006f0.yaml
    sha256: 2076802bbee34969ac368eca7394d2af8c80ae1e1a0764e0845ccd69af6bc9f9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- kind: maintained
  label: Vandenbrandeite
  owner_paths:
  - path: data/records/vandenbrandeite.yaml
    repository: CultureBotAI/CMMMech
    role: scientific_record
  path: data/records/vandenbrandeite.yaml
  target_id: cmmmech:vandenbrandeite
scope:
  description: Entire owner and actual history reviewed at claim level; no experiment
    replication, structure re-refinement or calculated-model reproduction.
  selection: Native capture before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:vandenbrandeite
checks:
- check_id: gate0
  name: Required final gate
  required: true
  status: passed
  command: just check
  exit_code: 0
  summary: Terminal receipt/log verified; exact owner hash matches.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - batch
- check_id: gate1
  name: Required final gate
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  summary: Terminal receipt/log verified; exact owner hash matches.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - batch
- check_id: gate2
  name: Required final gate
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 93f90797512dc8d1db3df9ce2e4994c475b1a4fe
  exit_code: 0
  summary: Terminal receipt/log verified; exact owner hash matches.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - batch
- check_id: gate3
  name: Required final gate
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  summary: Terminal receipt/log verified; exact owner hash matches.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/vandenbrandeite.yaml
  locator: Entire exact native-inspected owner; retained /private/tmp/CMMMech-expansion-round114-20261016/data/records/vandenbrandeite.yaml
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 7e2fe85151c9023197b7933d178a6681138a2c4ff76a8178905c32cec42dceb9
  support: supports
  summary: Material form, claims, conditions and uncertainty independently checked
    against full primary text and selected original figures.
- evidence_id: history0
  kind: record_content
  reference: history/records/vandenbrandeite/2026-10-16T065207Z-codex-c006f0.yaml
  locator: Entire canonical session and separate inline event; retained /private/tmp/CMMMech-expansion-round114-20261016/history/records/vandenbrandeite/2026-10-16T065207Z-codex-c006f0.yaml
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 2076802bbee34969ac368eca7394d2af8c80ae1e1a0764e0845ccd69af6bc9f9
  support: supports
  summary: Actual CREATE target, actor, current timestamps and limited accepted scope
    agree.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions and visually inspected species rows PDF53/226; retained /private/tmp/cmm-round114-uranium-research/ima202609.pdf
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Both mineral formulas and grandfathered status match; historical description
    dates are not approval numbers. No element criticality inherited.
- evidence_id: identity
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA09047A
  locator: Methods p40711 visually checked; structure/axis-setting discussion and
    Table1 pp40712-40714; theoretical methods versus experiments; retained /private/tmp/cmm-round114-uranium-research/vandenbrandeite2019-publisher-mirror.pdf
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 0b37e39aeb52375d6bbfc4da697c75130bda9cb2be645dab4a503cf10d7e698b
  support: supports
  summary: Natural Musonoi room-temperature triclinic diffraction and constrained
    hydrogen refinement are separate from first-principles mechanical/thermodynamic
    predictions. Experimental and calculated coordinate settings are distinguished.
- evidence_id: experiment
  kind: primary_source
  reference: https://doi.org/10.1023/A:1013182917829
  locator: Complete seven-page text; methods pp177-178, thermal discussion pp180-181,
    Figures4/6 on original PDF5/7 visually inspected; retained /private/tmp/cmm-round114-uranium-research/vandenbrandeite2002.pdf
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 49c5c43c0848f193fdca9dd7602864bda73d847e66f97643de7b216d82b14040
  support: supports
  summary: Selected Kalongwe crystals retain trace impurities. Air furnace, missing
    protocol details, metal-normalized EDAX, gradual hydroxyl loss and author-reported
    mixed oxide XRD products agree with the owner. Threshold conflicts and unshown
    raw curves/patterns remain explicit.
- evidence_id: search
  kind: search
  reference: Independent bounded DOI/title correction/retraction queries
  locator: Retrieved first web results on2026-10-16; retained /private/tmp/cmm-round114-uranium-independent-web.json
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 390fc3fb680c1bdaa4f266462c99c4f394161b1611708af4888240e8291d1710
  support: context_only
  summary: Publisher/primary metadata supports source identities. No applicable notice
    identified among returned results; this is not an exhaustive no-correction claim.
  search_scope: Four exact primary DOI correction/retraction searches; publisher RSC
    and original articles checked. No global literature absence claim.
- evidence_id: dedup
  kind: search
  reference: Independent current-owner search
  locator: Current data/records recursive hidden/ignored/followed matches; retained
    /private/tmp/cmm-round114-uranium-independent-dedup.txt
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 66840fbd2f24750377002ab15f6e29ad7d6dff8c81b04c0cf7d47677d690bf98
  support: context_only
  summary: Only these dedicated owners and contextual references were found in this
    bounded current-corpus search. Agent dossiers separately retain broader research/raw-download
    dedup.
  search_scope: Current data/records, hidden and ignored files included, relevant
    symlinks followed; names and four exact DOIs.
- evidence_id: batch
  kind: validation
  reference: Final exact-byte batch gates
  locator: Terminal command rows and hashed full log; retained /private/tmp/cmm-round114-final-gates-corrected.json
  accessed_at: '2026-10-16T07:18:40.123430Z'
  snapshot_sha256: 8628b01c993c722bbf1b0cdbe9e17a71e23eb1da1c0b7081dbc147d9e53d513d
  support: supports
  summary: just check, require-records, trusted-base history and generated-page freshness
    all passed with unchanged owner bytes.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural species versus experimental material
  outcome: supported
  summary: Current species formula and separate natural/synthetic specimen populations
    are supported.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - owner
  - ima
  - identity
- assessment_id: science
  area: evidence
  topic: Abiotic primary observations and limits
  outcome: supported
  summary: Qualitative natural-mineral thermal alteration is supported; product assignments
    are author-reported, not reindexed. No universal onset temperature, pure recovered
    phase, extraction yield or repository performance follows from text-only diffraction
    or computed thermodynamics.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - owner
  - experiment
  - identity
- assessment_id: provenance
  area: provenance
  topic: Actual curation and source inspection
  outcome: supported
  summary: Exact source versions, current history and bounded access/search limitations
    retained.
  target_ids:
  - cmmmech:vandenbrandeite
  evidence_ids:
  - history0
  - search
  - dedup
  - batch
findings: []
actions: []
limitations:
- Independent agent assessment is not external human peer review.
- Claim-bearing full text and selected original figures checked; not every primary
  page independently visually reread.
- Unacquired supplementary coordinates, original thermal/diffraction datasets and
  later2023 article remain evidence gaps; no deposited-data reanalysis claimed.
- Bounded notice searches and offline validation cannot settle retained source contradictions.
```
