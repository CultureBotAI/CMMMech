# Independent review of Baltic nodule evidence extension

- Review: 20261011T132229Z-polymetallic-nodules-round22-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T13:18:35.254334Z
- Finished UTC: 2026-10-11T13:22:29.558783Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two Baltic experiments are appropriately separated and qualified. No corrective finding in the current extension. Unavailable supplements, single azide comparators, local-growth scope and compartment accounting remain explicit.

## Scope And Provenance

Entire exact target inspected, fresh evidence review of two round22 Baltic mechanisms and integration; prior unchanged claims retain verified earlier independent scientific coverage.

Selection: One assigned maintained nodule record; all changed fields and provenance.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b19103bb393096e405bbecd2808a1aa0e01bb200.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:polymetallic-nodules | data/records/polymetallic-nodules.yaml | maintained | Polymetallic nodules |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:polymetallic-nodules | One record checked; zero failures, independently executed by root. |
| Native full checks | passed | True | cmmmech:polymetallic-nodules | /private/tmp/cmm-round22-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 124.01s (0:02:04)<br>Checked 154 record(s); 0 failed.<br>Checked 173 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:polymetallic-nodules | /private/tmp/cmm-round22-final-require.log: Checked 154 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:polymetallic-nodules | /private/tmp/cmm-round22-final-history.log: Checked 173 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Retain broad nodule resource, distinguish flat crust arms

identity: supported. Targets: cmmmech:polymetallic-nodules.

Baltic discoidal and spheroidal natural nodules fit the unchanged marine-concretion root; no locality-only duplicate, mineral-species inference or constituent criticality transfer.

### Observed growth and conditional metal partitioning

evidence: supported. Targets: cmmmech:polymetallic-nodules.

Source supports the narrowed observations with explicit control, compartment, replication and access limitations; no enzyme, taxon-specific, isolated-product or industrial conclusion.

### Actual EDIT and exact reviewed state

provenance: supported. Targets: cmmmech:polymetallic-nodules.

New author differs from reviewer; actual history attached, previous science/provenance retained. Final record matches inspected and gated bytes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/polymetallic-nodules.yaml; All maintained fields and actual EDIT history | supports | Exact current target inspected; only two new Baltic mechanisms, sources and actual provenance appended. No external CURIE or resource criticality claim. |
| primary2025 | https://doi.org/10.1111/gbi.70010; Methods 2.1–2.4, Tables 1–2, Results 3.2–3.4, Discussion 4; visually rendered PDF pp7–10 Figures 5–7 | supports | Main source independently read. Local 4.2/5.2/6.2 micrometre spheroidal patch points agree; not replicate nodules or observed annual growth. Triplicate living microcosms versus single 15 mM azide comparators; CT series lacks matched poisoned CT control. Relative solution trends and site exceptions match record. Original SI numeric cells remain unavailable. |
| primary2026 | https://doi.org/10.1111/1462-2920.70390; Methods 2.1–2.6, Table 2, Results 3.2–3.3 and 3.5, Discussion 4.1–4.3; rendered PDF pp10–12 and16–18, Figures 5–7 and13 | supports | Independent XML/text and selected rendered primary pages confirm 130 mL, 15-week, 50 mM azide design; distinct 2023 collection and reused 2022 community samples. Fe increase versus Mn decline is preserved. Bottle-wall acid wash is separate from solution/nodule mass, Mn comparator pattern differs by nodule type, and 5 mL acid plus three 5 mL rinses conflicts with claimed final10 mL. Community plots show associations, not taxon necessity. |
| carryforward | reviews/structured/20261011T121937Z-polymetallic-nodules-round20-independent/review.yaml; Prior exact-target scientific review plus parsed field comparison to trusted base | supports | Prior identity, original mechanism, original two sources and provenance prefixes are exactly unchanged. Prior target hash equals the trusted-base record hash. That independent review supplies earlier-study scientific coverage; root did not repeat the 2022 leaching literature review this round. |
| search | https://researchportal.helsinki.fi/en/publications/microbially-enhanced-growth-and-metal-capture-by-ferromanganese-c/; Two exact DOI correction/retraction web queries on 2026-10-11; first returned sets | context_only | Queries: "10.1111/gbi.70010" correction retraction; "10.1111/1462-2920.70390" correction retraction. Primary author-repository and PMC metadata corroborate dates/titles. No affecting notice identified in these returned sets; this is not an exhaustive absence claim. Curator acquisition and hidden/ignored-following bounded dedup receipts independently read. No fresh supplementary download by reviewer. |
| gates | /private/tmp/cmm-round22-gate-receipts.json; Terminal full batch/nonempty/history checks and final target hash | supports | 308 passed,3 skipped in124.01 seconds;154 records and173 histories pass. Root executed full batch and read terminal receipts. Scientific bytes are frozen and match inspect/gated hashes. |

## Limits And Additional Notes

- 2025/2026 supplementary raw tables could not be acquired by curator after bounded routes; reviewer inspected those receipts, not the missing tables. No exact SI concentration or recipe import.
- Single poisoned controls do not isolate pure biological causality; azide chemistry, pH/loading differences and variable biotic replicates remain.
- CT thickness is local and selected; solution loss does not identify all receiving compartments; bottle wash volume is internally inconsistent.
- No raw image registration, sequencing reanalysis, independent mass-balance reconstruction or deployment assessment.
- Prior unchanged mechanism retains earlier independent coverage; current review is not a claim of fresh full-corpus literature reassessment.
- Target/dossier orientation preceded canonical inspect; judgments and primary assessment followed inspect.
- Initial local preservation helper used system Python without PyYAML and failed; rerun in project .venv succeeded. This did not change target bytes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T132229Z-polymetallic-nodules-round22-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent review of Baltic nodule evidence extension
started_at: '2026-10-11T13:18:35.254334Z'
finished_at: '2026-10-11T13:22:29.558783Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round22_shallow_concretions authored the round22
    changes. Root independently assessed primary main evidence and figures and made
    no target edits. Shared worktree and curator downloads are disclosed. Root authored
    the original round20 record, whose unchanged fields retain a separate nonauthor
    independent review; fresh literature assessment here covers the round22 additions
    and integration.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Two Baltic experiments are appropriately separated and qualified. No corrective
  finding in the current extension. Unavailable supplements, single azide comparators,
  local-growth scope and compartment accounting remain explicit.
source:
  git_revision: b19103bb393096e405bbecd2808a1aa0e01bb200
  state: working_tree
  inputs:
  - path: data/records/polymetallic-nodules.yaml
    sha256: ac8458db0730c8064ccf42d4db53459861a95370567747be2d1fd3d3b8065751
    role: target
  - path: history/records/polymetallic-nodules/2026-10-11T131517Z-codex-d9bfef.yaml
    sha256: 1d643167cfc9f995704da95170d3acbedd890d5fa2d44f0166c3deae4d82666f
    role: context
  - path: research/ingests/round22-concretions-sources-20261011.json
    sha256: 0fc5c2bcee684abb1e6a59b55e9b04f9b558240890e6e61cf07282ed81e2e19b
    role: context
  - path: research/ingests/round22-concretions-sources-20261011.md
    sha256: 0fdb392a94656ce471ed82e49af7aba97756ac94a13c921e2c1d0c59cefc0323
    role: context
scope:
  description: Entire exact target inspected, fresh evidence review of two round22
    Baltic mechanisms and integration; prior unchanged claims retain verified earlier
    independent scientific coverage.
  selection: One assigned maintained nodule record; all changed fields and provenance.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:polymetallic-nodules
  exclusions:
  - target: Earlier unchanged 2022 leaching experiment and unavailable supplements
    reason: Prior experiment has exact independent coverage; fresh reassessment limited
      to new Baltic evidence. SI cells and raw sequencing are not newly imported or
      independently analysed.
targets:
- target_id: cmmmech:polymetallic-nodules
  path: data/records/polymetallic-nodules.yaml
  label: Polymetallic nodules
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polymetallic-nodules.yaml
    role: maintained_input
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/polymetallic-nodules.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One record checked; zero failures, independently executed by root.
  target_ids:
  - cmmmech:polymetallic-nodules
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round22-final-batch.log: uv run --locked --extra dev
    python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 124.01s (0:02:04)

    Checked 154 record(s); 0 failed.

    Checked 173 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:polymetallic-nodules
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round22-final-require.log: Checked 154 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:polymetallic-nodules
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base b19103bb393096e405bbecd2808a1aa0e01bb200
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round22-final-history.log: Checked 173 history record(s);
    0 error(s).

    '
  target_ids:
  - cmmmech:polymetallic-nodules
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/polymetallic-nodules.yaml
  locator: All maintained fields and actual EDIT history
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: supports
  summary: Exact current target inspected; only two new Baltic mechanisms, sources
    and actual provenance appended. No external CURIE or resource criticality claim.
  snapshot_sha256: ac8458db0730c8064ccf42d4db53459861a95370567747be2d1fd3d3b8065751
- evidence_id: primary2025
  kind: primary_source
  reference: https://doi.org/10.1111/gbi.70010
  locator: Methods 2.1–2.4, Tables 1–2, Results 3.2–3.4, Discussion 4; visually rendered
    PDF pp7–10 Figures 5–7
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: supports
  summary: Main source independently read. Local 4.2/5.2/6.2 micrometre spheroidal
    patch points agree; not replicate nodules or observed annual growth. Triplicate
    living microcosms versus single 15 mM azide comparators; CT series lacks matched
    poisoned CT control. Relative solution trends and site exceptions match record.
    Original SI numeric cells remain unavailable.
  snapshot_sha256: 7f6268cf02a0a8eceff05e20a4c88ed3247c83717f498a27b1067670c1483847
- evidence_id: primary2026
  kind: primary_source
  reference: https://doi.org/10.1111/1462-2920.70390
  locator: Methods 2.1–2.6, Table 2, Results 3.2–3.3 and 3.5, Discussion 4.1–4.3;
    rendered PDF pp10–12 and16–18, Figures 5–7 and13
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: supports
  summary: Independent XML/text and selected rendered primary pages confirm 130 mL,
    15-week, 50 mM azide design; distinct 2023 collection and reused 2022 community
    samples. Fe increase versus Mn decline is preserved. Bottle-wall acid wash is
    separate from solution/nodule mass, Mn comparator pattern differs by nodule type,
    and 5 mL acid plus three 5 mL rinses conflicts with claimed final10 mL. Community
    plots show associations, not taxon necessity.
  snapshot_sha256: 7ef7356c2db1d35773b309ebb5adc773f2584ecdf3cc3dec08bb4de5e6bbe44d
- evidence_id: carryforward
  kind: record_content
  reference: reviews/structured/20261011T121937Z-polymetallic-nodules-round20-independent/review.yaml
  locator: Prior exact-target scientific review plus parsed field comparison to trusted
    base
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: supports
  summary: Prior identity, original mechanism, original two sources and provenance
    prefixes are exactly unchanged. Prior target hash equals the trusted-base record
    hash. That independent review supplies earlier-study scientific coverage; root
    did not repeat the 2022 leaching literature review this round.
  snapshot_sha256: 1a3eea068247d2293b8bd2d3e65b72d0a0a95f95b8aeb376d86665f17c332b15
- evidence_id: search
  kind: search
  reference: https://researchportal.helsinki.fi/en/publications/microbially-enhanced-growth-and-metal-capture-by-ferromanganese-c/
  locator: Two exact DOI correction/retraction web queries on 2026-10-11; first returned
    sets
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: context_only
  summary: 'Queries: "10.1111/gbi.70010" correction retraction; "10.1111/1462-2920.70390"
    correction retraction. Primary author-repository and PMC metadata corroborate
    dates/titles. No affecting notice identified in these returned sets; this is not
    an exhaustive absence claim. Curator acquisition and hidden/ignored-following
    bounded dedup receipts independently read. No fresh supplementary download by
    reviewer.'
  search_scope: No filters or pagination; exact query timestamp not retained. Author
    dedup included data/records,research,reviews,history and named raw directories,
    hidden/ignored and relevant symlinks. Reviewer carried forward that explicitly
    scoped receipt, not a machine-wide absence claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round22-gate-receipts.json
  locator: Terminal full batch/nonempty/history checks and final target hash
  accessed_at: '2026-10-11T13:22:29.558783Z'
  support: supports
  summary: 308 passed,3 skipped in124.01 seconds;154 records and173 histories pass.
    Root executed full batch and read terminal receipts. Scientific bytes are frozen
    and match inspect/gated hashes.
  snapshot_sha256: ee1b6156ba8df516f968a764970052ed3ec86221a56f7a182b4d2a374766fbfb
assessments:
- assessment_id: identity
  area: identity
  topic: Retain broad nodule resource, distinguish flat crust arms
  outcome: supported
  summary: Baltic discoidal and spheroidal natural nodules fit the unchanged marine-concretion
    root; no locality-only duplicate, mineral-species inference or constituent criticality
    transfer.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - primary2025
  - primary2026
  - carryforward
  dimensions:
  - name: material_kind
    value: primary_resource
    definition: Natural geological nodules remain primary resources after collection.
    evidence_ids:
    - record
    - primary2025
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim is added.
    evidence_ids:
    - record
- assessment_id: mechanisms
  area: evidence
  topic: Observed growth and conditional metal partitioning
  outcome: supported
  summary: Source supports the narrowed observations with explicit control, compartment,
    replication and access limitations; no enzyme, taxon-specific, isolated-product
    or industrial conclusion.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - primary2025
  - primary2026
  dimensions:
  - name: organism_and_biomass
    value: Native living mixed communities
    definition: No isolated strains or taxon CURIE; molecular associations are not
      causality.
    evidence_ids:
    - primary2025
    - primary2026
  - name: substrate
    value: Rinsed Baltic discoidal and spheroidal nodules
    definition: Flat crust comparison excluded from accepted nodule mechanisms.
    evidence_ids:
    - primary2025
    - primary2026
  - name: conditions_controls
    value: 3.5 degrees C, dark,100 rpm; distinct12/15-week experiments
    definition: Triplicate biotic bottles and single azide comparator;15 versus50
      mM and changed Fe/Mn inputs prevent treating studies as identical replication.
    evidence_ids:
    - primary2025
    - primary2026
  - name: outcome
    value: Local CT patch growth; filtered-solution and bottle-wall fractions
    definition: Local thickness is not whole-nodule production; lower endpoint versus
      control is not necessarily net capture; no product mass balance.
    evidence_ids:
    - primary2025
    - primary2026
  - name: deployment
    value: Laboratory microcosms
    definition: No field extraction, pilot or industrial process demonstrated.
    evidence_ids:
    - record
    - primary2025
    - primary2026
- assessment_id: provenance
  area: provenance
  topic: Actual EDIT and exact reviewed state
  outcome: supported
  summary: New author differs from reviewer; actual history attached, previous science/provenance
    retained. Final record matches inspected and gated bytes.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - carryforward
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- 2025/2026 supplementary raw tables could not be acquired by curator after bounded
  routes; reviewer inspected those receipts, not the missing tables. No exact SI concentration
  or recipe import.
- Single poisoned controls do not isolate pure biological causality; azide chemistry,
  pH/loading differences and variable biotic replicates remain.
- CT thickness is local and selected; solution loss does not identify all receiving
  compartments; bottle wash volume is internally inconsistent.
- No raw image registration, sequencing reanalysis, independent mass-balance reconstruction
  or deployment assessment.
- Prior unchanged mechanism retains earlier independent coverage; current review is
  not a claim of fresh full-corpus literature reassessment.
notes:
- Target/dossier orientation preceded canonical inspect; judgments and primary assessment
  followed inspect.
- Initial local preservation helper used system Python without PyYAML and failed;
  rerun in project .venv succeeded. This did not change target bytes.
tags:
- round22
- independent
- scientific-review
- primary-resource
```
