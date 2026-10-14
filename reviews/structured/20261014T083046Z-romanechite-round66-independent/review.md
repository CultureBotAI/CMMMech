# Independent scientific review of romanechite

- Review: 20261014T083046Z-romanechite-round66-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T08:26:31.208849Z
- Finished UTC: 2026-10-14T08:30:46.390753Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record supports mineral identity and carefully limited mixed-ore context. It does not assert mineral-specific microbial causality, a strain accession, recovery yield or deployment; no supported curation defect was found.

## Scope And Provenance

Exact final record and CREATE sidecar assessed against claimed original evidence.

Selection: Assigned frozen path; inspect preceded final field-by-field judgment. Preliminary source assessment and initial record read occurred earlier and are disclosed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d57f45621cbe465eb13dfb6cc26cc4197d98f90e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:romanechite | data/records/romanechite.yaml | maintained | Romanèchite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:romanechite | Reviewer execution exit0; locked offline environment. |
| Batch gate 1 | passed | True | cmmmech:romanechite | Coordinator execution 2026-10-14T08:26:37.417759+00:00 to 2026-10-14T08:30:04.266682+00:00; receipt and log hash checked. |
| Batch gate 2 | passed | True | cmmmech:romanechite | Coordinator execution 2026-10-14T08:30:04.266767+00:00 to 2026-10-14T08:30:11.880507+00:00; receipt and log hash checked. |
| Batch gate 3 | passed | True | cmmmech:romanechite | Coordinator execution 2026-10-14T08:30:11.880596+00:00 to 2026-10-14T08:30:17.021271+00:00; receipt and log hash checked. |

## Scientific And Domain Assessments

### Mineral identity and naming boundary

identity: supported. Targets: cmmmech:romanechite.

Romanèchite is a barium-bearing manganese oxide species, distinct from psilomelane as a historical collective term, other Mn oxides, elements and mixed ores.

### Mixed-ore microbial context is not phase-specific causality

evidence: supported. Targets: cmmmech:romanechite.

Record correctly withholds a mineral-specific mechanism. Appendix I.3.2 describes Enterobacter species with no resolved strain, 1.89 g heat-sterilized ore, 8 mL 1% molasses, 32 degrees C and weekly acid addition before AAS in a 21-week series.

### Exact bytes, source identity and execution evidence

provenance: supported. Targets: cmmmech:romanechite.

CREATE sidecar, inline event, named validation and actual batch gates agree with the inspected working changes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/romanechite.yaml; Entire frozen record | supports | Field-by-field assessment after native inspect; record and CREATE sidecar remain unchanged. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 pages 1–2 and 186 | supports | Original retained authority row and field definitions visually inspected. Approved status A and special-procedure notation are retained without inventing a YYYY-NNN accession. |
| handbook | https://handbookofmineralogy.org/pdfs/romanechite.pdf; Complete one-page entry | supports | Original identity, formula and crystal data visually inspected; mineral identity does not inherit commodity criticality. |
| history | history/records/romanechite/2026-10-14T082212Z-codex-849047.yaml; Complete CREATE session and corresponding inline event | supports | Actual codex/GPT-6/codex actor, target and timestamps agree. No historical authorship was inferred and reviewer made no record or sidecar edit. |
| dedup | /private/tmp/cmm-round66-mn-root-review/dedup.txt; Scoped repository inventory including hidden and ignored files | context_only | Maintained owners, prior research and history references checked. Related manganese owners and prior handoffs are not mistaken for duplicate species records. |
| named | /private/tmp/cmm-round66-mn-root-review/romanechite-validation.log; Entire reviewer-executed named validation log | supports | Locked offline named validation passed with one record and zero failures. |
| batch | /private/tmp/cmm-round66-final-gates.json; Actual final gate receipt and original log | supports | Coordinator just check, nonempty validation and trusted-base history validation passed. Reviewer checked command results, receipt identity and log hash. |
| thesis | https://digital.library.adelaide.edu.au/server/api/core/bitstreams/1863f55b-77d9-42b3-a31a-b052d263fc4f/content; Sections 5.1–5.2 printed pp90–94; section 5.5 pp125–127/Figures 5.12–5.13; Appendix I.3.2 AI-16; Appendix V.2 AV.2-1/2 | context_only | Reviewer visually inspected PDF pages 115–119, 150–152, 275, 327–328 and read the bounded corresponding text. Norm calculations allocate Ba to romanèchite while ignoring variable K and intergrowths. The experiment uses mixed cemented pisolites and weekly acid additions; figures correlate calculated norm proportions with aggregate dissolved Mn. No pure-phase bacterial dissolution yield follows. |
| metadata | https://digital.library.adelaide.edu.au/items/a58699f2-d1e7-47e3-9520-2290c1371031; Live university repository landing and retained thesis title | supports | Repository verifies Bernhard Pracejus, 1989 PhD thesis and title. The search-engine crawl date is not the study publication date. |
| notices | https://digital.library.adelaide.edu.au/items/a58699f2-d1e7-47e3-9520-2290c1371031; Live bounded searches 2026-10-14 UTC | context_only | No affecting correction surfaced in the returned thesis search. Bohu2016 is an unresolved separate original-access lead, not verified phase-specific microbial evidence. Search snippets were not adopted as mechanism evidence. |

## Limits And Additional Notes

- Normative mineral amounts are model allocations, not direct quantitative phase measurements.
- Weekly sulfuric acid addition and missing matched comparator outcomes limit microbial attribution.
- The full 351-page thesis was not exhaustively reviewed; exact claim-bearing sections were inspected.
- Bohu2016 original-access and phase-attribution work remains a separate handoff.
- Reviewer corrections: none. Frozen hashes remain unchanged.
- Raw copyrighted originals and figures remain outside Git.
- Native review-check and exact corpus scientific coverage are subsequent publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T083046Z-romanechite-round66-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of romanechite
started_at: '2026-10-14T08:26:31.208849Z'
finished_at: '2026-10-14T08:30:46.390753Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record, history and Mn dossier authored by /root/round66_manganese.
    Reviewer independently read originals and made no record/history edits. Reviewer
    shared newly acquired Yin2022 SI with curator; acquisition was shared, assessment
    independent. Root authored batch documentation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record supports mineral identity and carefully limited mixed-ore
  context. It does not assert mineral-specific microbial causality, a strain accession,
  recovery yield or deployment; no supported curation defect was found.
source:
  git_revision: d57f45621cbe465eb13dfb6cc26cc4197d98f90e
  state: working_tree
  inputs:
  - path: data/records/romanechite.yaml
    sha256: d3f4c0ab0c19ac3b8881248c867cdca60268e176aa1ae7a04770777270ac2ac8
    role: target
  - path: history/records/romanechite/2026-10-14T082212Z-codex-849047.yaml
    sha256: 76ccc29fb7d202720fa20fa1badb7c3bfa9dca7de6de2538039554e486dbaf35
    role: context
scope:
  description: Exact final record and CREATE sidecar assessed against claimed original
    evidence.
  selection: Assigned frozen path; inspect preceded final field-by-field judgment.
    Preliminary source assessment and initial record read occurred earlier and are
    disclosed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:romanechite
targets:
- kind: maintained
  label: Romanèchite
  owner_paths:
  - path: data/records/romanechite.yaml
    repository: CultureBotAI/CMMMech
    role: maintained_record
  path: data/records/romanechite.yaml
  target_id: cmmmech:romanechite
checks:
- check_id: named
  name: Named record validation
  command: uv run --locked cmmmech validate data/records/romanechite.yaml
  status: passed
  required: true
  summary: Reviewer execution exit0; locked offline environment.
  target_ids:
  - cmmmech:romanechite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Batch gate 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:26:37.417759+00:00 to 2026-10-14T08:30:04.266682+00:00;
    receipt and log hash checked.
  target_ids:
  - cmmmech:romanechite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:30:04.266767+00:00 to 2026-10-14T08:30:11.880507+00:00;
    receipt and log hash checked.
  target_ids:
  - cmmmech:romanechite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Batch gate 3
  command: uv run --locked cmmmech validate-history --base d57f45621cbe465eb13dfb6cc26cc4197d98f90e
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:30:11.880596+00:00 to 2026-10-14T08:30:17.021271+00:00;
    receipt and log hash checked.
  target_ids:
  - cmmmech:romanechite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/romanechite.yaml
  locator: Entire frozen record
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Field-by-field assessment after native inspect; record and CREATE sidecar
    remain unchanged.
  snapshot_sha256: d3f4c0ab0c19ac3b8881248c867cdca60268e176aa1ae7a04770777270ac2ac8
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 pages 1–2 and 186
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Original retained authority row and field definitions visually inspected.
    Approved status A and special-procedure notation are retained without inventing
    a YYYY-NNN accession.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://handbookofmineralogy.org/pdfs/romanechite.pdf
  locator: Complete one-page entry
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Original identity, formula and crystal data visually inspected; mineral
    identity does not inherit commodity criticality.
  snapshot_sha256: 0e72cd702c3cd9d08bde7bf55297d7b6078609881910870fbe76094d6ea669c8
- evidence_id: history
  kind: record_content
  reference: history/records/romanechite/2026-10-14T082212Z-codex-849047.yaml
  locator: Complete CREATE session and corresponding inline event
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Actual codex/GPT-6/codex actor, target and timestamps agree. No historical
    authorship was inferred and reviewer made no record or sidecar edit.
  snapshot_sha256: 76ccc29fb7d202720fa20fa1badb7c3bfa9dca7de6de2538039554e486dbaf35
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round66-mn-root-review/dedup.txt
  locator: Scoped repository inventory including hidden and ignored files
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: context_only
  summary: Maintained owners, prior research and history references checked. Related
    manganese owners and prior handoffs are not mistaken for duplicate species records.
  search_scope: rg --no-ignore --hidden --follow -n -i 'cryptomelane|roman.chite|GCA.2022.07.014'
    data/records research history; no machinewide absence claim.
  snapshot_sha256: ecc92eb86dbed18cb7ab623cdcd7de45a23a4b7cf5a20fcb8fc43e2ca7621979
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round66-mn-root-review/romanechite-validation.log
  locator: Entire reviewer-executed named validation log
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Locked offline named validation passed with one record and zero failures.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round66-final-gates.json
  locator: Actual final gate receipt and original log
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Coordinator just check, nonempty validation and trusted-base history validation
    passed. Reviewer checked command results, receipt identity and log hash.
  snapshot_sha256: f770d6a65bb5b55e55ec2ef08ddfa02330dab31a1f87a26af94b2b92150a28dc
- evidence_id: thesis
  kind: primary_source
  reference: https://digital.library.adelaide.edu.au/server/api/core/bitstreams/1863f55b-77d9-42b3-a31a-b052d263fc4f/content
  locator: Sections 5.1–5.2 printed pp90–94; section 5.5 pp125–127/Figures 5.12–5.13;
    Appendix I.3.2 AI-16; Appendix V.2 AV.2-1/2
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: context_only
  summary: Reviewer visually inspected PDF pages 115–119, 150–152, 275, 327–328 and
    read the bounded corresponding text. Norm calculations allocate Ba to romanèchite
    while ignoring variable K and intergrowths. The experiment uses mixed cemented
    pisolites and weekly acid additions; figures correlate calculated norm proportions
    with aggregate dissolved Mn. No pure-phase bacterial dissolution yield follows.
  snapshot_sha256: eed717c2737e90892366054f2f217b9aa15644526711923ec832c52ae08724a1
- evidence_id: metadata
  kind: authority
  reference: https://digital.library.adelaide.edu.au/items/a58699f2-d1e7-47e3-9520-2290c1371031
  locator: Live university repository landing and retained thesis title
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: supports
  summary: Repository verifies Bernhard Pracejus, 1989 PhD thesis and title. The search-engine
    crawl date is not the study publication date.
- evidence_id: notices
  kind: search
  reference: https://digital.library.adelaide.edu.au/items/a58699f2-d1e7-47e3-9520-2290c1371031
  locator: Live bounded searches 2026-10-14 UTC
  accessed_at: '2026-10-14T08:30:46.390753Z'
  support: context_only
  summary: No affecting correction surfaced in the returned thesis search. Bohu2016
    is an unresolved separate original-access lead, not verified phase-specific microbial
    evidence. Search snippets were not adopted as mechanism evidence.
  search_scope: 'Queries: "Pracejus" "1989" "romanèchite" leaching; "Nature and Formation
    of Supergene Manganese Deposits" correction; "10.1128/AEM.03844-15" romanechite.
    First returned sets, no explicit domain/date filters or pagination; no exhaustive
    notice-absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity and naming boundary
  outcome: supported
  summary: Romanèchite is a barium-bearing manganese oxide species, distinct from
    psilomelane as a historical collective term, other Mn oxides, elements and mixed
    ores.
  target_ids:
  - cmmmech:romanechite
  evidence_ids:
  - record
  - ima
  - handbook
  dimensions:
  - name: material_form
    value: Mineral species (Ba,H2O)2(Mn4+,Mn3+)5O10
    definition: Current IMA formula; historical norm formula is not substituted as
      the modern ideal.
    evidence_ids:
    - ima
    - thesis
  - name: criticality
    value: No jurisdiction/list/edition claim
    definition: No commodity designation is inherited.
    evidence_ids:
    - record
- assessment_id: context
  area: evidence
  topic: Mixed-ore microbial context is not phase-specific causality
  outcome: supported
  summary: Record correctly withholds a mineral-specific mechanism. Appendix I.3.2
    describes Enterobacter species with no resolved strain, 1.89 g heat-sterilized
    ore, 8 mL 1% molasses, 32 degrees C and weekly acid addition before AAS in a 21-week
    series.
  target_ids:
  - cmmmech:romanechite
  evidence_ids:
  - record
  - thesis
  dimensions:
  - name: controls
    value: No matched uninoculated or acid-only results in inspected sections
    definition: Scope is explicitly bounded to methods, figures and Appendix V.2;
      not an unsupported whole-thesis absence claim.
    evidence_ids:
    - thesis
  - name: outcome
    value: Aggregate dissolved manganese versus calculated normative proportions
    definition: Ba allocation and neglected hosts/intergrowths preclude a pure-romanèchite
      yield or time-resolved direct phase measure.
    evidence_ids:
    - thesis
  - name: deployment
    value: Laboratory mixed-ore context only
    definition: No isolated commodity recovery or industrial use asserted.
    evidence_ids:
    - record
    - thesis
- assessment_id: provenance
  area: provenance
  topic: Exact bytes, source identity and execution evidence
  outcome: supported
  summary: CREATE sidecar, inline event, named validation and actual batch gates agree
    with the inspected working changes.
  target_ids:
  - cmmmech:romanechite
  evidence_ids:
  - record
  - history
  - named
  - batch
  - dedup
  - metadata
  - notices
findings: []
actions: []
limitations:
- Normative mineral amounts are model allocations, not direct quantitative phase measurements.
- Weekly sulfuric acid addition and missing matched comparator outcomes limit microbial
  attribution.
- The full 351-page thesis was not exhaustively reviewed; exact claim-bearing sections
  were inspected.
- Bohu2016 original-access and phase-attribution work remains a separate handoff.
notes:
- 'Reviewer corrections: none. Frozen hashes remain unchanged.'
- Raw copyrighted originals and figures remain outside Git.
- Native review-check and exact corpus scientific coverage are subsequent publication
  gates.
tags:
- round66
- independent
- romanechite
- primary-figures
```
