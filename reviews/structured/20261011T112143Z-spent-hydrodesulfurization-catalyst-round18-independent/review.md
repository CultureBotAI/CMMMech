# Independent scientific review of Spent hydrodesulfurization catalyst

- Review: 20261011T112143Z-spent-hydrodesulfurization-catalyst-round18-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:16:41Z
- Finished UTC: 2026-10-11T11:21:43Z
- Reviewer: Codex /root/round18_mineral_feeds (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded resource identity and laboratory mechanism claims are supported. No actionable defect was identified in the inspected bytes. Source contradictions and experimental limits remain explicit.

## Scope And Provenance

All fields and linked CREATE history of the assigned final record, including resource boundary, assay conditions, controls, quantitative claims and limitations.

Selection: One assigned new maintained record in the round18 batch, reviewed against its frozen inspected hash.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26cb0688effb2f71e4a570c416f6f43ff858c5ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-hydrodesulfurization-catalyst | data/records/spent-hydrodesulfurization-catalyst.yaml | maintained | Spent hydrodesulfurization catalyst |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:spent-hydrodesulfurization-catalyst | Reviewer observed terminal exit 0: Checked 2 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:spent-hydrodesulfurization-catalyst | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 86.49s (0:01:26)<br>Checked 138 record(s); 0 failed.<br>Checked 154 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:spent-hydrodesulfurization-catalyst | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-require.log: Checked 138 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:spent-hydrodesulfurization-catalyst | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-history.log: Checked 154 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Resource, organism and criticality boundaries

identity: supported. Targets: cmmmech:spent-hydrodesulfurization-catalyst.

The record retains a process-defined HDS secondary resource distinct from spent FCC and hydrocracking catalysts, fresh catalysts and constituent elements.

### Assay-specific mechanism, controls and quantitative limits

evidence: supported. Targets: cmmmech:spent-hydrodesulfurization-catalyst.

The original evidence supports FG-01 culture-associated acid leaching, with commercial-acid comparability or superiority. The record does not claim proven microbial enhancement, biosurfactant activity or isolated recovery.

### Exact reviewed bytes and CREATE history

provenance: supported. Targets: cmmmech:spent-hydrodesulfurization-catalyst.

Canonical inspect hashes, final byte comparison and actual CREATE session agree. Named validation and completed batch/history gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/spent-hydrodesulfurization-catalyst.yaml; Complete final YAML and linked CREATE sidecar | supports | All content and provenance inspected. Criticality is not asserted for this resource; no constituent-element designation is inherited. |
| search | /private/tmp/cmm-round18-cross-review/search.json; Exact DOI correction/retraction/erratum queries, related-source query and dedup-receipt.json | context_only | No affecting notice surfaced in the checked first-result sets. Related and reused publications are not assumed independent replication. |
| gates | /private/tmp/cmm-round18-gate-receipts.json; Completed receipt and final-batch.log, final-require.log, final-history.log | supports | All required gates finished with exit 0: 308 tests passed, 3 skipped; 138 records and 154 histories validated. Final target hashes match the initial canonical inspection. |
| primary | https://doi.org/10.1590/0104-6632.20170341s20150208; Original 11-page article; Methods pp120-122, Tables 1-4, Figures 1-4; visually inspected printed pp123-127 | supports | Original tables and figures support culture-associated metal mobilization and commercial-acid comparability or superiority. Table 2 seven-day Mo is 65+/-5% commercial acid versus 39+/-4% and 37+/-3% culture arms. Table 3 two-stage endpoint and final acidity are unspecified. Feed-mass-incompatible p126 concentrations, inoculum wording and Al/Ni contradictions are explicitly retained. |
| related | https://doi.org/10.5419/bjpg2015-0014; Author-hosted full text and captions, Methods 2.1-2.5, Results, SEM discussion and conclusion; publisher abstract checked live | context_only | The related paper uses a distinct 27.5 g/L, four-day protocol. Methods filter culture broth before leaching, while SEM discussion assigns attached cells; abstract/body yields conflict. The record correctly treats this as context with unresolved inconsistencies and no assumed independent feed batch. Publisher full-PDF retrieval timed out during review; full-resolution images were not independently acquired. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&amp;mode=Info; Live NCBI taxonomy species entry | supports | NCBITaxon:930 identifies Acidithiobacillus thiooxidans at species rank. The paper supplies FG-01 provenance; no exact-strain accession is invented. |

## Limits And Additional Notes

- The exact FG-01 strain lacks an independently verified accession; species identity is verified but does not prove strain identity.
- The 2017 two-stage final acid concentration and endpoint are not explicitly supplied; no fully specified optimum is claimed.
- Source quantity, inoculum and abstract/table/conclusion inconsistencies remain unresolved and are not silently repaired. Surface EDS is not a bulk mass balance.
- The related 2015 paper is contextual, with contradictory filtration/SEM and abstract/body statements; publisher PDF retrieval timed out and full-resolution figures were unavailable to this review.
- One refinery feed and the related same-group paper do not establish independent replication, general HDS-catalyst performance, industrial deployment or economic benefit. Bounded searches do not prove absence of further conflicting studies.
- Canonical inspect captured exact working-tree target, history and schema hashes before target assessment. All hashes were rechecked after completed batch gates. No source contradiction was silently repaired, and no new curation history event was invented for this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112143Z-spent-hydrodesulfurization-catalyst-round18-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Spent hydrodesulfurization catalyst
started_at: '2026-10-11T11:16:41Z'
finished_at: '2026-10-11T11:21:43Z'
reviewer:
  identity: Codex /root/round18_mineral_feeds
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A separate /root/round18_catalyst agent authored the target
    and its CREATE history. Reviewer independently read primary methods, results,
    original figures/tables and identity authorities after canonical target inspection;
    no target changes were made. Shared worktree and source dossier access are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded resource identity and laboratory mechanism claims are supported.
  No actionable defect was identified in the inspected bytes. Source contradictions
  and experimental limits remain explicit.
source:
  git_revision: 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  state: working_tree
  inputs:
  - path: data/records/spent-hydrodesulfurization-catalyst.yaml
    sha256: a4925767899690a23f67441bce8f6e5eb331ebd28beb4cc23d0ecb369f8e45a3
    role: target
  - path: history/records/spent-hydrodesulfurization-catalyst/2026-10-11T111316Z-codex-824afe.yaml
    sha256: bf5d2bac07afea916e1d02a401be2e83ea5c7c7ce23b815ac2ee984e14f4b8e6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields and linked CREATE history of the assigned final record,
    including resource boundary, assay conditions, controls, quantitative claims and
    limitations.
  selection: One assigned new maintained record in the round18 batch, reviewed against
    its frozen inspected hash.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
  exclusions:
  - target: Other corpus records, original instrument recalibration and industrial
      deployment
    reason: Related records and companion assay arms are contextual; no verdict beyond
      the assigned target or independent replication is asserted.
targets:
- target_id: cmmmech:spent-hydrodesulfurization-catalyst
  path: data/records/spent-hydrodesulfurization-catalyst.yaml
  label: Spent hydrodesulfurization catalyst
  kind: maintained
  ownership_note: Scientific changes belong in this maintained record; reviewed independently
    of its curator.
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/dunite.yaml data/records/spent-hydrodesulfurization-catalyst.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer observed terminal exit 0: Checked 2 record(s); 0 failed.'
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-batch.log:
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 86.49s (0:01:26)

    Checked 138 record(s); 0 failed.

    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-require.log:
    Checked 138 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-history.log:
    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/spent-hydrodesulfurization-catalyst.yaml
  locator: Complete final YAML and linked CREATE sidecar
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: All content and provenance inspected. Criticality is not asserted for this
    resource; no constituent-element designation is inherited.
  snapshot_sha256: a4925767899690a23f67441bce8f6e5eb331ebd28beb4cc23d0ecb369f8e45a3
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round18-cross-review/search.json
  locator: Exact DOI correction/retraction/erratum queries, related-source query and
    dedup-receipt.json
  accessed_at: '2026-10-11T11:21:43Z'
  support: context_only
  summary: No affecting notice surfaced in the checked first-result sets. Related
    and reused publications are not assumed independent replication.
  snapshot_sha256: e9c9daf65089a5855c8afeabf303c80c2d9491cead1f4cfce314d7ba366898fe
  search_scope: Hidden and ignored files included with relevant symlinks followed
    across data, history, research, reviews, .claude and named round18 dunite/catalyst
    raw directories. Relevant binaries inspected separately. Search exit 0 and empty
    stderr; no machine-wide or exhaustive literature absence claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round18-gate-receipts.json
  locator: Completed receipt and final-batch.log, final-require.log, final-history.log
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: 'All required gates finished with exit 0: 308 tests passed, 3 skipped;
    138 records and 154 histories validated. Final target hashes match the initial
    canonical inspection.'
  snapshot_sha256: f77f5decb184fd5e6544b9d89c9699a95621e2a83749524526f6283fb5be2f66
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1590/0104-6632.20170341s20150208
  locator: Original 11-page article; Methods pp120-122, Tables 1-4, Figures 1-4; visually
    inspected printed pp123-127
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: Original tables and figures support culture-associated metal mobilization
    and commercial-acid comparability or superiority. Table 2 seven-day Mo is 65+/-5%
    commercial acid versus 39+/-4% and 37+/-3% culture arms. Table 3 two-stage endpoint
    and final acidity are unspecified. Feed-mass-incompatible p126 concentrations,
    inoculum wording and Al/Ni contradictions are explicitly retained.
  snapshot_sha256: 251f45b4676ce46f8f226cc09684c265b0d9ba449487103a257ecfc9fd96a7f1
- evidence_id: related
  kind: primary_source
  reference: https://doi.org/10.5419/bjpg2015-0014
  locator: Author-hosted full text and captions, Methods 2.1-2.5, Results, SEM discussion
    and conclusion; publisher abstract checked live
  accessed_at: '2026-10-11T11:21:43Z'
  support: context_only
  summary: The related paper uses a distinct 27.5 g/L, four-day protocol. Methods
    filter culture broth before leaching, while SEM discussion assigns attached cells;
    abstract/body yields conflict. The record correctly treats this as context with
    unresolved inconsistencies and no assumed independent feed batch. Publisher full-PDF
    retrieval timed out during review; full-resolution images were not independently
    acquired.
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info
  locator: Live NCBI taxonomy species entry
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: NCBITaxon:930 identifies Acidithiobacillus thiooxidans at species rank.
    The paper supplies FG-01 provenance; no exact-strain accession is invented.
assessments:
- assessment_id: identity
  area: identity
  topic: Resource, organism and criticality boundaries
  outcome: supported
  summary: The record retains a process-defined HDS secondary resource distinct from
    spent FCC and hydrocracking catalysts, fresh catalysts and constituent elements.
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
  evidence_ids:
  - record
  - primary
  - search
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Material identity remains separate from constituent elements, mineral
      phases, commercial products and other resource types.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority/jurisdiction/list/edition designation is inherited from
      constituent elements or generic source terminology.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Assay-specific mechanism, controls and quantitative limits
  outcome: supported
  summary: The original evidence supports FG-01 culture-associated acid leaching,
    with commercial-acid comparability or superiority. The record does not claim proven
    microbial enhancement, biosurfactant activity or isolated recovery.
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
  evidence_ids:
  - record
  - primary
  - taxon
  - related
  dimensions:
  - name: organism_and_biomass
    value: Acidithiobacillus thiooxidans FG-01; one-stage culture versus previously
      grown culture solution in a separate two-stage arm
    definition: The 2017 source does not establish pre-leach cell removal. Analytical
      aliquot filtration is distinct from preparation of a cell-free lixiviant.
    evidence_ids:
    - primary
    - taxon
    - related
  - name: substrate_and_conditions
    value: Raw spent diesel HDS CoMo/alumina catalyst from one Brazilian refinery;
      no leach grinding, washing or decoking
    definition: Characterization digestion and SEM preparation are not feed pretreatments.
      General 100-mL assays at 29+/-1 degrees C and 150 rpm differ from the Table
      2 30-degree label.
    evidence_ids:
    - primary
  - name: controls_and_fraction
    value: Autoclaved-medium and commercial sulfuric-acid controls; 0.22-micrometre-filtered
      liquid AAS
    definition: Medium-control release below 0.5% is reported without underlying data.
      Stronger acid-only controls limit enhancement claims; percentage denominators
      derive from feed contents and liquid analysis.
    evidence_ids:
    - primary
  - name: outcome_and_scale
    value: Laboratory mobilization percentages for selected metals, no isolated product
    definition: Low Co/Cu/Ni release, missing Table 3 endpoint, surface EDS limitations
      and untested economic claims remain explicit.
    evidence_ids:
    - primary
    - related
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed bytes and CREATE history
  outcome: supported
  summary: Canonical inspect hashes, final byte comparison and actual CREATE session
    agree. Named validation and completed batch/history gates passed.
  target_ids:
  - cmmmech:spent-hydrodesulfurization-catalyst
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- The exact FG-01 strain lacks an independently verified accession; species identity
  is verified but does not prove strain identity.
- The 2017 two-stage final acid concentration and endpoint are not explicitly supplied;
  no fully specified optimum is claimed.
- Source quantity, inoculum and abstract/table/conclusion inconsistencies remain unresolved
  and are not silently repaired. Surface EDS is not a bulk mass balance.
- The related 2015 paper is contextual, with contradictory filtration/SEM and abstract/body
  statements; publisher PDF retrieval timed out and full-resolution figures were unavailable
  to this review.
- One refinery feed and the related same-group paper do not establish independent
  replication, general HDS-catalyst performance, industrial deployment or economic
  benefit. Bounded searches do not prove absence of further conflicting studies.
tags:
- round18
- independent
- scientific-review
- resource
notes:
- Canonical inspect captured exact working-tree target, history and schema hashes
  before target assessment. All hashes were rechecked after completed batch gates.
  No source contradiction was silently repaired, and no new curation history event
  was invented for this review.
```
