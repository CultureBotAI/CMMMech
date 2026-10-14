# Independent scientific review of Powellite

- Review: 20261014T220216Z-powellite-round82-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T21:50:46.846544Z
- Finished UTC: 2026-10-14T22:02:16.336495Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of Powellite identity and narrowly scoped natural-specimen evidence, without microbial, criticality or recovery extrapolation. No supported corrective defect found.

## Scope And Provenance

Complete frozen mineral identity/natural-characterization owner, source claims and canonical/inline provenance.

Selection: Assigned exact owner; native inspection before final scientific assessment. Primary-source preparation began before the captured inspection timestamp.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d26b03c7e8346b0caabb106f1aaf8acc3ed51623.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:powellite | data/records/powellite.yaml | maintained | Powellite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:powellite | Actual execution 2026-10-14T21:50:52.298411+00:00 through 2026-10-14T21:51:03.831144+00:00; two records, zero failures. |
| Actual batch gate 1 | passed | True | cmmmech:powellite | Coordinator execution 2026-10-14T21:51:56.716709+00:00 through 2026-10-14T22:00:29.305177+00:00; terminal result and log verified. |
| Actual batch gate 2 | passed | True | cmmmech:powellite | Coordinator execution 2026-10-14T22:00:29.305226+00:00 through 2026-10-14T22:00:57.771048+00:00; terminal result and log verified. |
| Actual batch gate 3 | passed | True | cmmmech:powellite | Coordinator execution 2026-10-14T22:00:57.771079+00:00 through 2026-10-14T22:01:05.397188+00:00; terminal result and log verified. |
| Actual batch gate 4 | passed | True | cmmmech:powellite | Coordinator execution 2026-10-14T22:01:05.397219+00:00 through 2026-10-14T22:01:14.509668+00:00; terminal result and log verified. |

## Scientific And Domain Assessments

### Mineral species, formula and claim boundary

identity: supported. Targets: cmmmech:powellite.

Current IMA authority supports Powellite as Ca(MoO4), grandfathered, distinct from its constituent element and mixed ore or unspecified precipitate. Criticality is unrecorded; no list membership is inherited.

### Two natural specimen arms and phase identification

evidence: supported. Targets: cmmmech:powellite.

The Bota-Burum specimens have similar Ca/Mo microprobe composition but different structural evidence. The uranophane-beta arm is anisotropic, has a powellite powder pattern and characteristic IR bands; the uramarsite-associated arm is isotropic and X-ray amorphous without characteristic powellite bands. The record distinguishes directly characterized crystalline powellite from the authors’ metamict interpretation.

### Contradictory phase-state discussion and graphic layout

evidence: supported. Targets: cmmmech:powellite.

Page 29 alternately retains diffraction and describes disappearance of anisotropy/diffraction for the silicate arm. Pages 23–27 provide the explicit characterization on which the qualified record rests. Several graphic captions are displaced or absent in the official PDF layout; no invented figure assignment or measurement was imported. The record preserves the contradiction.

### Radiation and heating boundaries

evidence: supported. Targets: cmmmech:powellite.

No controlled irradiation or direct exposure chronology establishes radiation as the unique cause of black colour or amorphization. Heating pertains to the crystalline arm; page 29 explicitly says the amorphous arm lacked enough material for thermal analysis. The record does not transfer heating results, assert microbial transformation or infer metal recovery.

### Exact reviewed state and actual checks

provenance: supported. Targets: cmmmech:powellite.

Native inspect captured owner, schema and canonical history before final judgment. Final hashes remain unchanged, provenance is accurate, named checks and actual four-command batch gates passed. No reviewer owner/history edit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/powellite.yaml; Whole final maintained owner. Actual local artifact: /private/tmp/CMMMech-expansion-round82-20261014/data/records/powellite.yaml | supports | Exact native-inspected identity, source scope and inline provenance reassessed. |
| history | history/records/powellite/2026-10-14T215006Z-codex-7421f4.yaml; Whole canonical CREATE sidecar. Actual local artifact: /private/tmp/CMMMech-expansion-round82-20261014/history/records/powellite/2026-10-14T215006Z-codex-7421f4.yaml | supports | Target, actual codex/GPT-6 actor, timestamp and bounded CREATE content agree with the distinct inline event. |
| primary | https://fmm.ru/images/2/23/NDM_2008_43_Sidorenko_eng.pdf; Complete eight-page original, printed pages 23–30, all page graphics independently viewed. Chemical/optical comparisons pp.23–24, powder diffraction and IR results pp.25–27, amorphous-arm characterization pp.27–28 and conflicting interpretation p.29. Actual local artifact: /private/tmp/cmm-round82-stolzite-research/sidorenko2008.pdf | supports | The uranophane-beta arm has crystalline powellite characterization; the chemically similar uramarsite arm is optically isotropic and X-ray amorphous. Radiation origin remains inferred. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Retained September2026 master list; definitions page1 and exact powellite row page177 visually checked. Actual local artifact: /private/tmp/cmm-round47-indium-research/raw/ima2026.pdf | supports | Ca(MoO4), status G and description year 1891 confirmed. The year is not a unique IMA approval accession. Existing PDF bytes rechecked, not claimed freshly downloaded. |
| notices | /private/tmp/cmm-round82-root-minerals-review-search.json; Actual returned search results. Actual local artifact: /private/tmp/cmm-round82-root-minerals-review-search.json | context_only | No affecting notice identified in the bounded exact-title correction/erratum search; not a global absence claim. |
| dedup | /private/tmp/cmm-round82-root-minerals-independent/dedup.txt; Current-worktree material/source lineage search. Actual local artifact: /private/tmp/cmm-round82-root-minerals-independent/dedup.txt | context_only | Existing source mentions and dzhalindite publication linkage retained; no independent replication inferred. |
| named | /private/tmp/cmm-round82-root-minerals-independent/named-validation.json; Actual independent two-file strict validation receipt. Actual local artifact: /private/tmp/cmm-round82-root-minerals-independent/named-validation.json | supports | Both files passed, zero failures; terminal output log hash 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042 independently verified. |
| batch | /private/tmp/cmm-round82-final-gates.json; Actual root terminal four-command batch receipt; log /private/tmp/cmm-round82-final-gates.log SHA256 df800072c55c68b58b2d641a7d4be91fce3688f8d018a528ddaad8490410ddd7. Actual local artifact: /private/tmp/cmm-round82-final-gates.json | supports | All four actual commands exited0; exact command sequence, trusted base and log hash verified. No hosted CI or publication assertion. |

## Limits And Additional Notes

- The metamict assignment is an interpretation of shape, chemistry, isotropy and amorphism, not a refined crystalline structure of the amorphous material.
- Radiation cause and exposure chronology are inferred; the record does not present a controlled irradiation mechanism.
- The page29 phase-state contradiction and displaced/absent graphic captions limit interpretation; no quantitative phase yield or heating result is transferred to the amorphous arm.
- Bounded notice searches and source inventory do not establish universal absence of corrections or additional data.
- Review timing starts at the actual native-inspection capture; preliminary full-source reading occurred earlier and is disclosed rather than backdated.
- Primary PDFs are nonempty verified originals. No supplementary experiment is asserted; complete articles and relevant official source inventory disclose no separate SI within the checked boundary.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/CMMMech
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
review_id: 20261014T220216Z-powellite-round82-independent
title: Independent scientific review of Powellite
started_at: '2026-10-14T21:50:46.846544Z'
finished_at: '2026-10-14T22:02:16.336495Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this mineral owner and history. This reviewer
    authored the unrelated electroplating-bath-effluents record, independently inspected
    the mineral originals and authorities, and made no target/history edits. Shared
    acquisition does not imply independent experiments.
source:
  git_revision: d26b03c7e8346b0caabb106f1aaf8acc3ed51623
  state: working_tree
  inputs:
  - path: data/records/powellite.yaml
    sha256: ae48266be7b108ee15d203db366f7388aae8a8623f46e1e118740f1aba2d1853
    role: target
  - path: history/records/powellite/2026-10-14T215006Z-codex-7421f4.yaml
    sha256: 6732fb62b81ce28878bb805bcbeedcaf978f43904ad98539e70be9e649da4038
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:powellite
  path: data/records/powellite.yaml
  label: Powellite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/powellite.yaml
    role: maintained_record
scope:
  description: Complete frozen mineral identity/natural-characterization owner, source
    claims and canonical/inline provenance.
  selection: Assigned exact owner; native inspection before final scientific assessment.
    Primary-source preparation began before the captured inspection timestamp.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:powellite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/powellite.yaml
  locator: 'Whole final maintained owner. Actual local artifact: /private/tmp/CMMMech-expansion-round82-20261014/data/records/powellite.yaml'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: Exact native-inspected identity, source scope and inline provenance reassessed.
  snapshot_sha256: ae48266be7b108ee15d203db366f7388aae8a8623f46e1e118740f1aba2d1853
- evidence_id: history
  kind: record_content
  reference: history/records/powellite/2026-10-14T215006Z-codex-7421f4.yaml
  locator: 'Whole canonical CREATE sidecar. Actual local artifact: /private/tmp/CMMMech-expansion-round82-20261014/history/records/powellite/2026-10-14T215006Z-codex-7421f4.yaml'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: Target, actual codex/GPT-6 actor, timestamp and bounded CREATE content
    agree with the distinct inline event.
  snapshot_sha256: 6732fb62b81ce28878bb805bcbeedcaf978f43904ad98539e70be9e649da4038
- evidence_id: primary
  kind: primary_source
  reference: https://fmm.ru/images/2/23/NDM_2008_43_Sidorenko_eng.pdf
  locator: 'Complete eight-page original, printed pages 23–30, all page graphics independently
    viewed. Chemical/optical comparisons pp.23–24, powder diffraction and IR results
    pp.25–27, amorphous-arm characterization pp.27–28 and conflicting interpretation
    p.29. Actual local artifact: /private/tmp/cmm-round82-stolzite-research/sidorenko2008.pdf'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: The uranophane-beta arm has crystalline powellite characterization; the
    chemically similar uramarsite arm is optically isotropic and X-ray amorphous.
    Radiation origin remains inferred.
  snapshot_sha256: f01dab88b65d08e729ead37deeacdbc8af35522517749f2594721183bc64afc3
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'Retained September2026 master list; definitions page1 and exact powellite
    row page177 visually checked. Actual local artifact: /private/tmp/cmm-round47-indium-research/raw/ima2026.pdf'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: Ca(MoO4), status G and description year 1891 confirmed. The year is not
    a unique IMA approval accession. Existing PDF bytes rechecked, not claimed freshly
    downloaded.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round82-root-minerals-review-search.json
  locator: 'Actual returned search results. Actual local artifact: /private/tmp/cmm-round82-root-minerals-review-search.json'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: context_only
  summary: No affecting notice identified in the bounded exact-title correction/erratum
    search; not a global absence claim.
  snapshot_sha256: 6d2011ec07dc6dd9038e527be6f066ed298a9e06d684a06d0396f0259da7281c
  search_scope: Exact original article-title queries with correction/erratum terms
    on2026-10-14; returned web search result sets only.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round82-root-minerals-independent/dedup.txt
  locator: 'Current-worktree material/source lineage search. Actual local artifact:
    /private/tmp/cmm-round82-root-minerals-independent/dedup.txt'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: context_only
  summary: Existing source mentions and dzhalindite publication linkage retained;
    no independent replication inferred.
  snapshot_sha256: 5a08bf0f6ce5a2f043049457338ee11198daf4ab07f975aa598b19c1cd9c91aa
  search_scope: rg --no-ignore --hidden --follow -n -i stolzite|powellite|NDM_2008_43_Kiseleva|NDM_2008_43_Sidorenko
    data/records research/sources reviews history. Bounded current textual repository,
    including ignored files; no machine-wide absence assertion.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round82-root-minerals-independent/named-validation.json
  locator: 'Actual independent two-file strict validation receipt. Actual local artifact:
    /private/tmp/cmm-round82-root-minerals-independent/named-validation.json'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: Both files passed, zero failures; terminal output log hash 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
    independently verified.
  snapshot_sha256: 32b019fd7062047f95be3c3b0c9399422160cbae76c0af5b5399d704340f4a85
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round82-final-gates.json
  locator: 'Actual root terminal four-command batch receipt; log /private/tmp/cmm-round82-final-gates.log
    SHA256 df800072c55c68b58b2d641a7d4be91fce3688f8d018a528ddaad8490410ddd7. Actual
    local artifact: /private/tmp/cmm-round82-final-gates.json'
  accessed_at: '2026-10-14T22:02:16.336495Z'
  support: supports
  summary: All four actual commands exited0; exact command sequence, trusted base
    and log hash verified. No hosted CI or publication assertion.
  snapshot_sha256: 1a86c9240ba0fabaf4ea06457e54a319f19f4849b336263b695d4376b661bb5d
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate data/records/stolzite.yaml data/records/powellite.yaml
    --require-records
  status: passed
  required: true
  summary: Actual execution 2026-10-14T21:50:52.298411+00:00 through 2026-10-14T21:51:03.831144+00:00;
    two records, zero failures.
  target_ids:
  - cmmmech:powellite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch0
  name: Actual batch gate 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T21:51:56.716709+00:00 through 2026-10-14T22:00:29.305177+00:00;
    terminal result and log verified.
  target_ids:
  - cmmmech:powellite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch1
  name: Actual batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T22:00:29.305226+00:00 through 2026-10-14T22:00:57.771048+00:00;
    terminal result and log verified.
  target_ids:
  - cmmmech:powellite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Actual batch gate 3
  command: uv run --locked cmmmech validate-history --base d26b03c7e8346b0caabb106f1aaf8acc3ed51623
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T22:00:57.771079+00:00 through 2026-10-14T22:01:05.397188+00:00;
    terminal result and log verified.
  target_ids:
  - cmmmech:powellite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Actual batch gate 4
  command: uv run --locked python scripts/render_pages.py --check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T22:01:05.397219+00:00 through 2026-10-14T22:01:14.509668+00:00;
    terminal result and log verified.
  target_ids:
  - cmmmech:powellite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
summary: Qualified acceptance of Powellite identity and narrowly scoped natural-specimen
  evidence, without microbial, criticality or recovery extrapolation. No supported
  corrective defect found.
limitations:
- The metamict assignment is an interpretation of shape, chemistry, isotropy and amorphism,
  not a refined crystalline structure of the amorphous material.
- Radiation cause and exposure chronology are inferred; the record does not present
  a controlled irradiation mechanism.
- The page29 phase-state contradiction and displaced/absent graphic captions limit
  interpretation; no quantitative phase yield or heating result is transferred to
  the amorphous arm.
- Bounded notice searches and source inventory do not establish universal absence
  of corrections or additional data.
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species, formula and claim boundary
  outcome: supported
  summary: Current IMA authority supports Powellite as Ca(MoO4), grandfathered, distinct
    from its constituent element and mixed ore or unspecified precipitate. Criticality
    is unrecorded; no list membership is inherited.
  target_ids:
  - cmmmech:powellite
  evidence_ids:
  - record
  - ima
- assessment_id: specimen
  area: evidence
  topic: Two natural specimen arms and phase identification
  outcome: supported
  summary: The Bota-Burum specimens have similar Ca/Mo microprobe composition but
    different structural evidence. The uranophane-beta arm is anisotropic, has a powellite
    powder pattern and characteristic IR bands; the uramarsite-associated arm is isotropic
    and X-ray amorphous without characteristic powellite bands. The record distinguishes
    directly characterized crystalline powellite from the authors’ metamict interpretation.
  target_ids:
  - cmmmech:powellite
  evidence_ids:
  - primary
  - record
- assessment_id: conflicts
  area: evidence
  topic: Contradictory phase-state discussion and graphic layout
  outcome: supported
  summary: Page 29 alternately retains diffraction and describes disappearance of
    anisotropy/diffraction for the silicate arm. Pages 23–27 provide the explicit
    characterization on which the qualified record rests. Several graphic captions
    are displaced or absent in the official PDF layout; no invented figure assignment
    or measurement was imported. The record preserves the contradiction.
  target_ids:
  - cmmmech:powellite
  evidence_ids:
  - primary
  - record
- assessment_id: causality
  area: evidence
  topic: Radiation and heating boundaries
  outcome: supported
  summary: No controlled irradiation or direct exposure chronology establishes radiation
    as the unique cause of black colour or amorphization. Heating pertains to the
    crystalline arm; page 29 explicitly says the amorphous arm lacked enough material
    for thermal analysis. The record does not transfer heating results, assert microbial
    transformation or infer metal recovery.
  target_ids:
  - cmmmech:powellite
  evidence_ids:
  - primary
  - record
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed state and actual checks
  outcome: supported
  summary: Native inspect captured owner, schema and canonical history before final
    judgment. Final hashes remain unchanged, provenance is accurate, named checks
    and actual four-command batch gates passed. No reviewer owner/history edit.
  target_ids:
  - cmmmech:powellite
  evidence_ids:
  - record
  - history
  - named
  - batch
findings: []
actions: []
notes:
- Review timing starts at the actual native-inspection capture; preliminary full-source
  reading occurred earlier and is disclosed rather than backdated.
- Primary PDFs are nonempty verified originals. No supplementary experiment is asserted;
  complete articles and relevant official source inventory disclose no separate SI
  within the checked boundary.
```
