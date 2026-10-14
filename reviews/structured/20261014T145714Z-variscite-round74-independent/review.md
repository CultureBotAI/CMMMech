# Independent scientific review of Variscite round74

- Review: 20261014T145714Z-variscite-round74-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T14:49:05.818191Z
- Finished UTC: 2026-10-14T14:57:14.273059Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Identity and narrowly scoped abiotic mixed-phase formation are supported. The source timing, thermodynamic omissions and absence of phase-specific recovery remain explicit.

## Scope And Provenance

Entire exact owner/history, primary methods/results/graphics, identity authorities and bounded notice search.

Selection: Independent assigned peer review of both new phosphate owners, saved separately.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a524756f3f4f90d81f89035fa7f85f1e1897b99d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:variscite | data/records/variscite.yaml | maintained | Variscite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:variscite | Actual reviewer execution; two records, zero failed. |
| Terminal batch validation | passed | True | cmmmech:variscite | Coordinator execution 2026-10-14T14:51:48.096045+00:00 to 2026-10-14T14:55:06.998511+00:00; terminal receipt and log hash rechecked. |
| Terminal batch validation | passed | True | cmmmech:variscite | Coordinator execution 2026-10-14T14:55:06.998535+00:00 to 2026-10-14T14:55:15.616870+00:00; terminal receipt and log hash rechecked. |
| Terminal batch validation | passed | True | cmmmech:variscite | Coordinator execution 2026-10-14T14:55:15.616892+00:00 to 2026-10-14T14:55:20.937881+00:00; terminal receipt and log hash rechecked. |

## Scientific And Domain Assessments

### Mineral identity, material boundary and criticality

identity: supported. Targets: cmmmech:variscite.

Species identity is grounded without merging dimorphs, elements or feedstocks. No jurisdiction/list/edition or criticality designation is asserted.

### Substrate, preparation, abiotic conditions, outcome and deployment

evidence: supported. Targets: cmmmech:variscite.

5mL0.1M metal nitrate plus5mL0.1M phosphate/0.09M KOH; solutions preheated98C and mixed in sealed Teflon-lined reactors at100C. Mixed pH about1.6 measured25C, three daily shakes, quench/wash/dry; the characterized endpoint is21days for aluminum and9days for iron. No microorganism, biomass or inoculum, industrial deployment or pure-product yield is inferred.

### Immutable history and reviewed bytes

provenance: supported. Targets: cmmmech:variscite.

CREATE metadata and linked target agree with frozen owner; accepted journal and thesis copy are one experiment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/variscite.yaml; Entire exact owner captured by inspect before scientific assessment | supports | Read all scientific fields and the distinct inline CREATE and canonical reference. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pp.1–2; variscite row p.227 and strengite row p.207; retained official PDF and rendered rows independently checked | supports | Variscite is A/1967 s.p.; strengite is G/1877. Special procedure and original-description year are not invented proposal accessions. |
| handbook | https://www.handbookofmineralogy.org/pdfs/variscite.pdf; Complete one-page text plus current official web PDF | supports | Orthorhombic hydrated phosphate and its distinct monoclinic dimorph, not an element or mixed feed. |
| primary | https://doi.org/10.1021/cg900654m; Complete nine-page coauthor-hosted journal original, all Figures1–10/Tables1–5; Methods p.5198, Results pp.5199–5203 and Conclusion p.5204 | supports | Original text and all nine-page graphics assessed. Shared study has distinct Al and Fe arms, measured pH at25C, preheating/mixing/quenching and washed/dried solids. XRD and microscopy identify mixed polymorph assemblages; phase-specific yields and biological causality are not established. |
| limits | https://doi.org/10.1021/cg900654m; Section3 p.5199 versus3.2 p.5200; Table1 and Figures2/7/8/10; Section3.3/Tables2–3 | partial | Iron-phase timing conflicts between persistence for at least9days and crystallization within5days; the characterized nine-day mixed endpoint is retained. Aluminum endpoint is21days and earlier12day material remains amorphous. PHREEQC omitted relevant polymorph data; modeled stability does not prove exclusive equilibrium. |
| history | history/records/variscite/2026-10-14T144732Z-codex-0fdd34.yaml; Entire canonical CREATE sidecar and linked inline change | supports | Actual GPT-6/codex actor, UTC timestamp, target and new-record scope agree; no history rewriting or review-only curation event. |
| search | /private/tmp/cmm-round74-phosphates-independent/search-summary.json; Bounded live original/notice searches and hidden/ignored-inclusive dedup receipts | context_only | No duplicate owner within searched repository bounds beyond new candidates; no verified affecting notice surfaced in returned windows. Search snippets are leads only. |
| named | /private/tmp/cmm-round74-phosphates-independent/named.log; Independent reviewer execution after inspection | supports | Two named frozen records passed; structural validation does not certify scientific claims. |
| batch | /private/tmp/cmm-round74-final-gates.json; Terminal coordinator receipt, command exits and independently rehashed full log | supports | All three required batch checks passed; source working base and log match this batch. |

## Limits And Additional Notes

- The same original study supports the two distinct phosphate arms; this is not independent replication.
- Timing conflicts, incomplete phase fractions and omitted thermodynamic polymorph data limit onset, purity and recovery claims.
- Bounded source/notice searches and local originals do not establish exhaustive literature coverage. No supplement was indicated in inspected original or metadata; a complete publisher attachment audit was not available.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T145714Z-variscite-round74-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Variscite round74
started_at: '2026-10-14T14:49:05.818191Z'
finished_at: '2026-10-14T14:57:14.273059Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The phosphates peer authored this owner/history and dossier.
    Reviewer authored the separate CdTe owner and batch coordination, did not edit
    either phosphate owner, and captured native inspection before assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Identity and narrowly scoped abiotic mixed-phase formation are supported.
  The source timing, thermodynamic omissions and absence of phase-specific recovery
  remain explicit.
source:
  git_revision: a524756f3f4f90d81f89035fa7f85f1e1897b99d
  state: working_tree
  inputs:
  - path: data/records/variscite.yaml
    sha256: 3c272778de8dc7b867ffca8fe5bc10d210de3938315f57b898f3d95ab7efb59f
    role: target
  - path: history/records/variscite/2026-10-14T144732Z-codex-0fdd34.yaml
    sha256: e0776a894a5e56c3428b5f09d4f269ab39ca8030c539f842ea964d192f6e5f1c
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire exact owner/history, primary methods/results/graphics, identity
    authorities and bounded notice search.
  selection: Independent assigned peer review of both new phosphate owners, saved
    separately.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:variscite
targets:
- target_id: cmmmech:variscite
  path: data/records/variscite.yaml
  label: Variscite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/variscite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate --require-records data/records/variscite.yaml
    data/records/strengite.yaml
  status: passed
  required: true
  summary: Actual reviewer execution; two records, zero failed.
  target_ids:
  - cmmmech:variscite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Terminal batch validation
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T14:51:48.096045+00:00 to 2026-10-14T14:55:06.998511+00:00;
    terminal receipt and log hash rechecked.
  target_ids:
  - cmmmech:variscite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Terminal batch validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T14:55:06.998535+00:00 to 2026-10-14T14:55:15.616870+00:00;
    terminal receipt and log hash rechecked.
  target_ids:
  - cmmmech:variscite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Terminal batch validation
  command: uv run --locked cmmmech validate-history --base a524756f3f4f90d81f89035fa7f85f1e1897b99d
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T14:55:15.616892+00:00 to 2026-10-14T14:55:20.937881+00:00;
    terminal receipt and log hash rechecked.
  target_ids:
  - cmmmech:variscite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/variscite.yaml
  locator: Entire exact owner captured by inspect before scientific assessment
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Read all scientific fields and the distinct inline CREATE and canonical
    reference.
  snapshot_sha256: 3c272778de8dc7b867ffca8fe5bc10d210de3938315f57b898f3d95ab7efb59f
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pp.1–2; variscite row p.227 and strengite row p.207; retained
    official PDF and rendered rows independently checked
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Variscite is A/1967 s.p.; strengite is G/1877. Special procedure and original-description
    year are not invented proposal accessions.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/variscite.pdf
  locator: Complete one-page text plus current official web PDF
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Orthorhombic hydrated phosphate and its distinct monoclinic dimorph, not
    an element or mixed feed.
  snapshot_sha256: 0aa97f7aac8eb1b020bc78d728f74b92aae6b4ff448645abdffbb6d57d9d5a5c
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/cg900654m
  locator: Complete nine-page coauthor-hosted journal original, all Figures1–10/Tables1–5;
    Methods p.5198, Results pp.5199–5203 and Conclusion p.5204
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Original text and all nine-page graphics assessed. Shared study has distinct
    Al and Fe arms, measured pH at25C, preheating/mixing/quenching and washed/dried
    solids. XRD and microscopy identify mixed polymorph assemblages; phase-specific
    yields and biological causality are not established.
  snapshot_sha256: c16f03a75cb1e564c0f2fe50c5d51757e5a032800e7a39dcede91ce192bf34bf
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1021/cg900654m
  locator: Section3 p.5199 versus3.2 p.5200; Table1 and Figures2/7/8/10; Section3.3/Tables2–3
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: partial
  summary: Iron-phase timing conflicts between persistence for at least9days and crystallization
    within5days; the characterized nine-day mixed endpoint is retained. Aluminum endpoint
    is21days and earlier12day material remains amorphous. PHREEQC omitted relevant
    polymorph data; modeled stability does not prove exclusive equilibrium.
  snapshot_sha256: c16f03a75cb1e564c0f2fe50c5d51757e5a032800e7a39dcede91ce192bf34bf
- evidence_id: history
  kind: record_content
  reference: history/records/variscite/2026-10-14T144732Z-codex-0fdd34.yaml
  locator: Entire canonical CREATE sidecar and linked inline change
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Actual GPT-6/codex actor, UTC timestamp, target and new-record scope agree;
    no history rewriting or review-only curation event.
  snapshot_sha256: e0776a894a5e56c3428b5f09d4f269ab39ca8030c539f842ea964d192f6e5f1c
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round74-phosphates-independent/search-summary.json
  locator: Bounded live original/notice searches and hidden/ignored-inclusive dedup
    receipts
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: context_only
  summary: No duplicate owner within searched repository bounds beyond new candidates;
    no verified affecting notice surfaced in returned windows. Search snippets are
    leads only.
  snapshot_sha256: 166f56c11ade533cae653d3c0dbe2ad367c0f0a64f211b96877354d17f9765ce
  search_scope: Exact DOI/author/time-conflict queries, first returned windows only;
    local data/records,research,reviews,history with hidden and ignored files and
    followed symlinks. No machine-wide or exhaustive literature assertion.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round74-phosphates-independent/named.log
  locator: Independent reviewer execution after inspection
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: Two named frozen records passed; structural validation does not certify
    scientific claims.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round74-final-gates.json
  locator: Terminal coordinator receipt, command exits and independently rehashed
    full log
  accessed_at: '2026-10-14T14:57:14.273059Z'
  support: supports
  summary: All three required batch checks passed; source working base and log match
    this batch.
  snapshot_sha256: 54fa72f75c13ce01a699c7b09f54e794c10d9cc6165d8bc93d4d08d37ccb7c35
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity, material boundary and criticality
  outcome: supported
  summary: Species identity is grounded without merging dimorphs, elements or feedstocks.
    No jurisdiction/list/edition or criticality designation is asserted.
  target_ids:
  - cmmmech:variscite
  evidence_ids:
  - record
  - ima
  - handbook
  dimensions:
  - name: material_form
    value: Orthorhombic AlPO4·2H2O; mixed variscite/metavariscite endpoint
    definition: Ideal species identity distinguished from actual mixed experimental
      solids.
    evidence_ids:
    - ima
    - handbook
    - primary
  - name: criticality
    value: No claim
    definition: Absence of a designation is not universal noncriticality.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Substrate, preparation, abiotic conditions, outcome and deployment
  outcome: supported
  summary: 5mL0.1M metal nitrate plus5mL0.1M phosphate/0.09M KOH; solutions preheated98C
    and mixed in sealed Teflon-lined reactors at100C. Mixed pH about1.6 measured25C,
    three daily shakes, quench/wash/dry; the characterized endpoint is21days for aluminum
    and9days for iron. No microorganism, biomass or inoculum, industrial deployment
    or pure-product yield is inferred.
  target_ids:
  - cmmmech:variscite
  evidence_ids:
  - record
  - primary
  - limits
  dimensions:
  - name: biomass_and_controls
    value: Abiotic chemical precipitation; no inoculated arm or biological control
    definition: No microbial necessity or biogenic phase assignment.
    evidence_ids:
    - primary
  - name: outcome
    value: Mixed polymorph endpoint with modeled chemistry kept separate
    definition: Crystalline identification is not a recovered-product yield or proof
      of unique equilibrium.
    evidence_ids:
    - primary
    - limits
- assessment_id: provenance
  area: provenance
  topic: Immutable history and reviewed bytes
  outcome: supported
  summary: CREATE metadata and linked target agree with frozen owner; accepted journal
    and thesis copy are one experiment.
  target_ids:
  - cmmmech:variscite
  evidence_ids:
  - history
  - record
  - primary
findings: []
actions: []
limitations:
- The same original study supports the two distinct phosphate arms; this is not independent
  replication.
- Timing conflicts, incomplete phase fractions and omitted thermodynamic polymorph
  data limit onset, purity and recovery claims.
- Bounded source/notice searches and local originals do not establish exhaustive literature
  coverage. No supplement was indicated in inspected original or metadata; a complete
  publisher attachment audit was not available.
```
