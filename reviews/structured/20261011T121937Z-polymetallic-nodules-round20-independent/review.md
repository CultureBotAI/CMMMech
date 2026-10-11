# Independent scientific review of polymetallic nodules

- Review: 20261011T121937Z-polymetallic-nodules-round20-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T12:15:43.590084Z
- Finished UTC: 2026-10-11T12:19:37.141798Z
- Reviewer: Codex /root/round20_goethite (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The primary-resource identity and narrowly stated laboratory leachate observations are supported. Record preserves missing matched controls, citrate chemistry, unresolved culture composition, source inconsistencies, residue-mass issues and proposed rather than measured 25-cycle completion. No corrective findings identified in this scope.

## Scope And Provenance

Complete assigned new marine resource record and actual CREATE provenance; primary identity, mechanism, analytical, outcome and scale verification.

Selection: One assigned maintained record from round20; all target fields inspected.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e98bdfaba62869faf5112ef281a9371d2a04d78e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:polymetallic-nodules | data/records/polymetallic-nodules.yaml | maintained | Polymetallic nodules |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:polymetallic-nodules | Checked 1 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:polymetallic-nodules | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round20-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 80.63s (0:01:20)<br>Checked 149 record(s); 0 failed.<br>Checked 166 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:polymetallic-nodules | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round20-final-require.log: Checked 149 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:polymetallic-nodules | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round20-final-history.log: Checked 166 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Marine resource boundary and dated authority

identity: supported. Targets: cmmmech:polymetallic-nodules.

The root denotes natural nodules rather than constituent minerals, processing residues or traded product grades. Geological source and handling support primary_resource; no constituent criticality is inherited.

### Culture-associated leachate observations and causal limits

evidence: supported. Targets: cmmmech:polymetallic-nodules.

The record supports the observed conditional leachate concentrations while explicitly withholding untested microbial enhancement, taxon necessity, direct reduction and industrial claims.

### Exact target state and actual history

provenance: supported. Targets: cmmmech:polymetallic-nodules.

Canonical inspect preceded scientific assessment and captured target, history and schema at the trusted base. CREATE describes actual work by parent; no record edits by reviewer. Completed required batch and history gates passed; exact target matches gated bytes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/polymetallic-nodules.yaml; Complete maintained YAML and linked CREATE history | supports | All fields and actual actor/timestamp/history linkage independently read. No external material/taxon identifier or constituent criticality is asserted. |
| identity | https://pubs.usgs.gov/fs/2025/3017/fs20253017.pdf; USGS Fact Sheet 2025-3017 version 1.1 April 2025, pp1-4, rendered p2 Table 1 | supports | Official authority distinguishes abyssal sediment nodules from rock-surface ferromanganese crusts. Constituent criticality asterisks refer to2022 elements and are not a designation for the nodules. |
| primary | https://doi.org/10.3390/min12111373; Full Methods 2.1-2.4, Results 3.1-3.3, Discussion 4; Tables 2-4 and rendered PDF pp9-12 Figures 2-5 | supports | Independently read IOM-hosted 14-page primary. Actual 2014 trawl sample 3521-1-TR1, room drying/grinding, mass loadings, nominal medium/bottle conditions and sample 3 fourth-collection 2120 mg/L Mn agree with record. Total-element leachate/XRF measurement is not isolated product or demonstrated dissolved Mn(II). |
| limits | https://doi.org/10.3390/min12111373; Methods 2.1-2.4; Figure 3, Table 4 and Figures 4-5; Discussion 4 and Conclusions | partial | No matched sterile MD control isolates a microbial increment from added 4 g/L citrate. 16S taxonomic profile concerns inoculating mud, not isolated causal strains. Analytical replicates are not biological replication. Figure 3/Discussion 22% Ni conflicts with blanket below 20% prose. Table 4 concentration decline and 13.3% solid-mass loss are distinct. Figure 5 reports numerical collections 1-5 only; 6-25 is an unquantified combined box, not evidence of measured complete recovery. |
| search | /private/tmp/cmm-round20-nodule-independent/search.json; Three bounded live queries and independent hidden/ignored-following dedup receipt | context_only | Returned first result sets identified no affecting correction or retraction. Official USGS metadata and author-organization primary corroborate title/version. This is bounded notice/identity discovery, not exhaustive literature coverage. |
| gates | /private/tmp/cmm-round20-gate-receipts.json; Completed final batch/require/history logs and frozen target hashes | supports | Actual terminal gates pass: 308 tests, 3 skips, 149 records, 166 histories; require-records and trusted-base history each exit 0. Reviewed target matches both inspect and batch hash. Reviewer independently read these receipts. |

## Limits And Additional Notes

- Missing matched sterile/acid controls, pre-added citrate and variable pH prevent a quantified microbial increment or unique pathway inference.
- Final carbon concentration, culture composition, biological replication and precise timing are not fully resolved by the source.
- Raw instrument calibration/uncertainty and full metal mass balance were not reconstructed. Concentration decline in a changing residue mass is not a recovered yield.
- No numerical 25-cycle completion series, characterized isolated product, pilot or industrial implementation is established.
- Notice searches are bounded first-result sets; historical cited studies and additional independent nodule assays were not comprehensively assessed.
- Initial inspect failed because the default uv cache was inaccessible; rerun with UV_OFFLINE=1 and temporary cache succeeded before assessment. Named validation also completed successfully with this configuration.
- Target orientation preceded the successful canonical inspect. Scientific judgments followed its timestamp. Retained curator-acquired primary PDFs were independently read, not described as reviewer downloads.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T121937Z-polymetallic-nodules-round20-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of polymetallic nodules
started_at: '2026-10-11T12:15:43.590084Z'
finished_at: '2026-10-11T12:19:37.141798Z'
reviewer:
  identity: Codex /root/round20_goethite
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Parent /root authored the record and CREATE history. This reviewer
    independently inspected the full primary text, rendered figures and official identity
    authority, executed named validation and notice/dedup searches, and made no target
    edits. Shared worktree and curator-acquired raw sources are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The primary-resource identity and narrowly stated laboratory leachate observations
  are supported. Record preserves missing matched controls, citrate chemistry, unresolved
  culture composition, source inconsistencies, residue-mass issues and proposed rather
  than measured 25-cycle completion. No corrective findings identified in this scope.
source:
  git_revision: e98bdfaba62869faf5112ef281a9371d2a04d78e
  state: working_tree
  inputs:
  - path: data/records/polymetallic-nodules.yaml
    sha256: b93250c8309b4505b59f0b6ffb3120474515af7fd953555cf8d62bad757ab616
    role: target
  - path: history/records/polymetallic-nodules/2026-10-11T121503Z-codex-8c4777.yaml
    sha256: 66d96700671d0350ddae0051ca353b7cbebd7a4114db6d02328e2a30c7ac4bd6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Complete assigned new marine resource record and actual CREATE provenance;
    primary identity, mechanism, analytical, outcome and scale verification.
  selection: One assigned maintained record from round20; all target fields inspected.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:polymetallic-nodules
  exclusions:
  - target: Other records and raw analytical reprocessing
    reason: Review applies only to the named target. Historical cited studies were
      not reanalysed and instrument data are unavailable.
targets:
- target_id: cmmmech:polymetallic-nodules
  path: data/records/polymetallic-nodules.yaml
  label: Polymetallic nodules
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polymetallic-nodules.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/polymetallic-nodules.yaml
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:polymetallic-nodules
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round20-final-batch.log: uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 80.63s (0:01:20)

    Checked 149 record(s); 0 failed.

    Checked 166 history record(s); 0 error(s).

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
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round20-final-require.log: Checked 149 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:polymetallic-nodules
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base e98bdfaba62869faf5112ef281a9371d2a04d78e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round20-final-history.log: Checked 166 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:polymetallic-nodules
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/polymetallic-nodules.yaml
  locator: Complete maintained YAML and linked CREATE history
  accessed_at: '2026-10-11T12:18:34.013433Z'
  support: supports
  summary: All fields and actual actor/timestamp/history linkage independently read.
    No external material/taxon identifier or constituent criticality is asserted.
  snapshot_sha256: b93250c8309b4505b59f0b6ffb3120474515af7fd953555cf8d62bad757ab616
- evidence_id: identity
  kind: primary_source
  reference: https://pubs.usgs.gov/fs/2025/3017/fs20253017.pdf
  locator: USGS Fact Sheet 2025-3017 version 1.1 April 2025, pp1-4, rendered p2 Table
    1
  accessed_at: '2026-10-11T12:18:34.013433Z'
  support: supports
  summary: Official authority distinguishes abyssal sediment nodules from rock-surface
    ferromanganese crusts. Constituent criticality asterisks refer to2022 elements
    and are not a designation for the nodules.
  snapshot_sha256: 881d2703e3e0d5425789859a9403175e8cceed44093167480bcb3c820c46439f
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min12111373
  locator: Full Methods 2.1-2.4, Results 3.1-3.3, Discussion 4; Tables 2-4 and rendered
    PDF pp9-12 Figures 2-5
  accessed_at: '2026-10-11T12:18:34.013433Z'
  support: supports
  summary: Independently read IOM-hosted 14-page primary. Actual 2014 trawl sample
    3521-1-TR1, room drying/grinding, mass loadings, nominal medium/bottle conditions
    and sample 3 fourth-collection 2120 mg/L Mn agree with record. Total-element leachate/XRF
    measurement is not isolated product or demonstrated dissolved Mn(II).
  snapshot_sha256: 72d753664b4dce91211376e4828a028d517e620a5628dc46078205bb7a370ed9
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.3390/min12111373
  locator: Methods 2.1-2.4; Figure 3, Table 4 and Figures 4-5; Discussion 4 and Conclusions
  accessed_at: '2026-10-11T12:18:34.013433Z'
  support: partial
  summary: No matched sterile MD control isolates a microbial increment from added
    4 g/L citrate. 16S taxonomic profile concerns inoculating mud, not isolated causal
    strains. Analytical replicates are not biological replication. Figure 3/Discussion
    22% Ni conflicts with blanket below 20% prose. Table 4 concentration decline and
    13.3% solid-mass loss are distinct. Figure 5 reports numerical collections 1-5
    only; 6-25 is an unquantified combined box, not evidence of measured complete
    recovery.
  snapshot_sha256: 72d753664b4dce91211376e4828a028d517e620a5628dc46078205bb7a370ed9
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round20-nodule-independent/search.json
  locator: Three bounded live queries and independent hidden/ignored-following dedup
    receipt
  accessed_at: '2026-10-11T12:18:34.013433Z'
  support: context_only
  summary: Returned first result sets identified no affecting correction or retraction.
    Official USGS metadata and author-organization primary corroborate title/version.
    This is bounded notice/identity discovery, not exhaustive literature coverage.
  search_scope: Hidden and ignored files included with symlink following across data/records,research,reviews,history
    and the named raw nodule directory. Primary PDF independently inspected. Web first-result
    sets without pagination or date filters.
  snapshot_sha256: 4f1871d671f2912abc9835ff9b32950bc9a09fafffd36dc3bce7f6d48aa3c19b
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round20-gate-receipts.json
  locator: Completed final batch/require/history logs and frozen target hashes
  accessed_at: '2026-10-11T12:19:37.141798Z'
  support: supports
  summary: 'Actual terminal gates pass: 308 tests, 3 skips, 149 records, 166 histories;
    require-records and trusted-base history each exit 0. Reviewed target matches
    both inspect and batch hash. Reviewer independently read these receipts.'
  snapshot_sha256: f59d8f098925a9b4adf1ee2ff887e11d8fe86bfdfa1e2b328e4a4f617664f26a
assessments:
- assessment_id: identity
  area: identity
  topic: Marine resource boundary and dated authority
  outcome: supported
  summary: The root denotes natural nodules rather than constituent minerals, processing
    residues or traded product grades. Geological source and handling support primary_resource;
    no constituent criticality is inherited.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - identity
  - primary
  - search
  dimensions:
  - name: material_kind
    value: primary_resource
    definition: Natural marine geological feed remains a primary resource after collection,
      drying and milling.
    evidence_ids:
    - record
    - identity
    - primary
  - name: criticality
    value: Not asserted
    definition: USGS constituent 2022 asterisks are not silently mapped to a resource
      designation.
    evidence_ids:
    - record
    - identity
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated leachate observations and causal limits
  outcome: supported
  summary: The record supports the observed conditional leachate concentrations while
    explicitly withholding untested microbial enhancement, taxon necessity, direct
    reduction and industrial claims.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - primary
  - limits
  dimensions:
  - name: organism_and_biomass
    value: Living mixed heterotrophic enrichment from natural Fe/Mn-weathering mud
    definition: Starting-mud 16S profile does not authenticate strains or final community
      causality; no taxon ID assigned.
    evidence_ids:
    - record
    - primary
    - limits
  - name: substrate_and_pretreatment
    value: Ground Clarion-Clipperton Zone nodules, sample 3521-1-TR1
    definition: Approximately 2 kg trawl collection from 4265-4291 m; room drying
      and 0.1-1 mm bowl milling; sample-specific mixed bulk composition.
    evidence_ids:
    - record
    - primary
  - name: conditions_controls
    value: Sealed bottles, 38 +/- 0.5 degrees C, nominal pH 5.5 +/- 0.5,variable loads
      and 150 mL replacement
    definition: Medium contains citrate; carbon formulation and timing differ across
      source passages. Bottle 5 is another inoculated recipe, not a matched sterile
      control.
    evidence_ids:
    - record
    - primary
    - limits
  - name: measurement_basis
    value: Reported sample 3 fourth-collection 2120 mg/L Mn
    definition: Portable XRF liquid analysis with no established filtered dissolved-ion
      fraction or valence; ICP-OES confirms solid residue.
    evidence_ids:
    - record
    - primary
  - name: outcome_and_scale
    value: Laboratory mobilization; five quantified collections; no isolated product
    definition: Proposed 25 changes and precipitation diagram do not establish measured
      complete recovery, material purity or industrial operation.
    evidence_ids:
    - record
    - limits
- assessment_id: provenance
  area: provenance
  topic: Exact target state and actual history
  outcome: supported
  summary: Canonical inspect preceded scientific assessment and captured target, history
    and schema at the trusted base. CREATE describes actual work by parent; no record
    edits by reviewer. Completed required batch and history gates passed; exact target
    matches gated bytes.
  target_ids:
  - cmmmech:polymetallic-nodules
  evidence_ids:
  - record
  - gates
  dimensions: []
findings: []
limitations:
- Missing matched sterile/acid controls, pre-added citrate and variable pH prevent
  a quantified microbial increment or unique pathway inference.
- Final carbon concentration, culture composition, biological replication and precise
  timing are not fully resolved by the source.
- Raw instrument calibration/uncertainty and full metal mass balance were not reconstructed.
  Concentration decline in a changing residue mass is not a recovered yield.
- No numerical 25-cycle completion series, characterized isolated product, pilot or
  industrial implementation is established.
- Notice searches are bounded first-result sets; historical cited studies and additional
  independent nodule assays were not comprehensively assessed.
notes:
- Initial inspect failed because the default uv cache was inaccessible; rerun with
  UV_OFFLINE=1 and temporary cache succeeded before assessment. Named validation also
  completed successfully with this configuration.
- Target orientation preceded the successful canonical inspect. Scientific judgments
  followed its timestamp. Retained curator-acquired primary PDFs were independently
  read, not described as reviewer downloads.
tags:
- round20
- independent
- scientific-review
- primary-resource
actions: []
```
