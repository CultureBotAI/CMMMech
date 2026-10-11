# Independent scientific review of round 11 rhenium

- Review: 20261011T080559Z-rhenium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:59:30Z
- Finished UTC: 2026-10-11T08:05:59Z
- Reviewer: Codex /root/cmm11_ir_os_hf (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The element identity, dated designation and narrow inactive-yeast association claim are defensible. Primary methods and supplement confirm the record appropriately limits source-reported removal estimates, unwashed-biomass analytical fractions and fitted capacities, and does not claim Re redox, selective product or deployment.

## Scope And Provenance

All scientific and provenance fields of the named frozen record; declared primary evidence and dated authorities.

Selection: Assigned named record; no sampling. Other candidate studies are context or future leads.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:rhenium | data/records/rhenium.yaml | maintained | Rhenium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:rhenium | Reviewer session 43433 terminal exit 0; Checked 3 records, 0 failed. Read /private/tmp/cmm11-independent-named-validation.log. |
| Full batch gate | passed | True | cmmmech:rhenium | Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records and 83 histories valid. Root session 92015 terminal exit 0. |
| Required-record validation | passed | True | cmmmech:rhenium | Final required-record validation passed 71 records, zero failed. Root session 93511 terminal exit 0. |
| Trusted-base history validation | passed | True | cmmmech:rhenium | Final trusted-base history validation passed 83 histories, zero errors. Root session 88115 terminal exit 0. |

## Scientific And Domain Assessments

### Neutral element and dated criticality

identity: supported. Targets: cmmmech:rhenium.

Correct element identity, jurisdiction, list and edition; ion/mineral/resource/grade distinctions preserved.

### Primary assay and scope limits

evidence: supported. Targets: cmmmech:rhenium.

The element identity, dated designation and narrow inactive-yeast association claim are defensible. Primary methods and supplement confirm the record appropriately limits source-reported removal estimates, unwashed-biomass analytical fractions and fitted capacities, and does not claim Re redox, selective product or deployment.

### Actual curation and immutable observation

provenance: supported. Targets: cmmmech:rhenium.

Canonical CREATE sidecar and separate inline event match the target and actual actor/times; reviewed working changes remain uncommitted and are attested by byte hash. Scientific review does not append curation history.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/rhenium.yaml; Entire record, linked CREATE history, inline event, dossier and schema inspected; exact working-tree input hashes captured before judgment. | supports | Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records, dossiers or histories. Shared inspect captured final inputs before scientific assessment. Existing raw evidence was independently read, key primary images checked, authority content independently resolved or read from retained verified captures. No scientific target edits made by reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:49882; Neutral element name/formula/charge, hierarchy and alternate identifiers | supports | Verified 49882 denotes rhenium atom, formula Re, charge 0. Helium live page succeeded; Rb/Re live web route failed, so independently read same-day curator-acquired official HTML rather than claiming a fresh successful reviewer download. Element root does not identify an assay ion or commodity stream. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Official title/date and exact annex or commodity row | supports | United States; DOI/USGS Final 2025 List of Critical Minerals; 7 November 2025; 90 FR 50494–50497; Rhenium row on printed p.50496. Live authority content and retained source text agree. No timeless or universal material designation inferred. |
| primary | https://doi.org/10.3390/ma14164763; Zinicovscaia et al. 2021: complete main methods/results/conclusion text; all nine figure images; PDF methods/equations pp. 3–4, Table 2 p. 10, Table 3 p. 11 and Table 4 p. 12; full two-page supplementary Figures S1–S2. | supports | Independently checked dried brewery biomass, synthetic perrhenate feeds, 500 mg/50 mL and duplicate batches. NAA measures Re/Mo in filtered dried biomass, while Cu is explicitly assayed in solution. Source equation-versus-fraction ambiguity, missing post-contact wash/abiotic control, mg/kg-versus-mg/g conflict, model extrapolation and anomalous S2 scale are correctly retained. |
| search | Bounded independent web and local search; Returned result sets and /private/tmp/cmm11-independent-{local,raw}-search.txt | context_only | Selected primary and authority leads examined within the stated bounded search; no comprehensive absence claim. |
| validation | /private/tmp/cmm-round11-final-batch-receipts.json; Final parent terminal receipts and full logs; reviewer named-validation log | supports | Reviewer independently read parent final checks/logs and own named validation terminal 0; structural checks do not prove scientific truth. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4932&amp;mode=Info; Current species name, basionym and rank | supports | Live official Taxonomy browser and retained datasets JSON identify species 4932 as Saccharomyces cerevisiae. Neither establishes the unknown brewery strain or axenicity, which the record leaves unresolved. |

## Limits And Additional Notes

- The paper does not close the Re analytical mass balance or resolve entrained liquor in unwashed retained biomass.
- All fixed conditions and uncertainty definitions are not supplied for every parameter series.
- Supplementary S2 scale, fitted-concentration basis and source unit inconsistencies limit quantitative reuse; no re-fit performed.
- Separate positive/null Re reduction studies are not direct replications of this inactive-yeast assay and are not adjudicated here.
- No unresolved blocker, major or minor record defect identified. No corrective action required for the inspected scope; listed limitations remain.
- No target content, history, dossier or schema changed by this reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080559Z-rhenium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of round 11 rhenium
started_at: '2026-10-11T07:59:30Z'
finished_at: '2026-10-11T08:05:59Z'
reviewer:
  identity: Codex /root/cmm11_ir_os_hf
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records,
    dossiers or histories. Shared inspect captured final inputs before scientific
    assessment. Existing raw evidence was independently read, key primary images checked,
    authority content independently resolved or read from retained verified captures.
    No scientific target edits made by reviewer.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The element identity, dated designation and narrow inactive-yeast association
  claim are defensible. Primary methods and supplement confirm the record appropriately
  limits source-reported removal estimates, unwashed-biomass analytical fractions
  and fitted capacities, and does not claim Re redox, selective product or deployment.
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: data/records/rhenium.yaml
    sha256: 88ad2d618e9b2468ecd0804d568d4c43303b0488766715f5b605e94b945516a4
    role: target
  - path: history/records/rhenium/2026-10-11T075235Z-codex-7de104.yaml
    sha256: b7c66509712d5d503b746a86acc547432b7902ec3e6f705955ddaa159a4337f7
    role: context
  - path: research/ingests/round11-be-rb-re-20261011.json
    sha256: 640a1bdf8e27ab0ebd87f42949133434970efcd6eefcc12e771a245e966ab554
    role: context
  - path: research/ingests/round11-be-rb-re-20261011.md
    sha256: 4dcf18bcbfd6721ffa40b82969b6198047bfbbc599ba52daba7da960368a175d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:rhenium
  path: data/records/rhenium.yaml
  label: Rhenium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rhenium.yaml
    role: maintained_record
scope:
  description: All scientific and provenance fields of the named frozen record; declared
    primary evidence and dated authorities.
  selection: Assigned named record; no sampling. Other candidate studies are context
    or future leads.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:rhenium
checks:
- check_id: named
  name: Reviewer named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/rubidium.yaml data/records/rhenium.yaml data/records/helium.yaml
    --require-records
  status: passed
  required: true
  summary: Reviewer session 43433 terminal exit 0; Checked 3 records, 0 failed. Read
    /private/tmp/cmm11-independent-named-validation.log.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - validation
- check_id: batch
  name: Full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records
    and 83 histories valid. Root session 92015 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-check.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - validation
- check_id: nonempty
  name: Required-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Final required-record validation passed 71 records, zero failed. Root session
    93511 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-validation.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - validation
- check_id: history
  name: Trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  status: passed
  required: true
  summary: Final trusted-base history validation passed 83 histories, zero errors.
    Root session 88115 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-history.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/rhenium.yaml
  locator: Entire record, linked CREATE history, inline event, dossier and schema
    inspected; exact working-tree input hashes captured before judgment.
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records, dossiers or
    histories. Shared inspect captured final inputs before scientific assessment.
    Existing raw evidence was independently read, key primary images checked, authority
    content independently resolved or read from retained verified captures. No scientific
    target edits made by reviewer.
  snapshot_sha256: 88ad2d618e9b2468ecd0804d568d4c43303b0488766715f5b605e94b945516a4
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:49882
  locator: Neutral element name/formula/charge, hierarchy and alternate identifiers
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Verified 49882 denotes rhenium atom, formula Re, charge 0. Helium live
    page succeeded; Rb/Re live web route failed, so independently read same-day curator-acquired
    official HTML rather than claiming a fresh successful reviewer download. Element
    root does not identify an assay ion or commodity stream.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Official title/date and exact annex or commodity row
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: United States; DOI/USGS Final 2025 List of Critical Minerals; 7 November
    2025; 90 FR 50494–50497; Rhenium row on printed p.50496. Live authority content
    and retained source text agree. No timeless or universal material designation
    inferred.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/ma14164763
  locator: 'Zinicovscaia et al. 2021: complete main methods/results/conclusion text;
    all nine figure images; PDF methods/equations pp. 3–4, Table 2 p. 10, Table 3
    p. 11 and Table 4 p. 12; full two-page supplementary Figures S1–S2.'
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Independently checked dried brewery biomass, synthetic perrhenate feeds,
    500 mg/50 mL and duplicate batches. NAA measures Re/Mo in filtered dried biomass,
    while Cu is explicitly assayed in solution. Source equation-versus-fraction ambiguity,
    missing post-contact wash/abiotic control, mg/kg-versus-mg/g conflict, model extrapolation
    and anomalous S2 scale are correctly retained.
  snapshot_sha256: 47c5b286233fec27c6e18fd8537d6d86c2693181e5830fd0dd5bcccee4b43a07
- evidence_id: search
  kind: search
  reference: Bounded independent web and local search
  locator: Returned result sets and /private/tmp/cmm11-independent-{local,raw}-search.txt
  accessed_at: '2026-10-11T08:05:59Z'
  support: context_only
  summary: Selected primary and authority leads examined within the stated bounded
    search; no comprehensive absence claim.
  search_scope: 'Live web.run on 2026-10-11: exact DOI 10.1128/jb.150.3.1183-1191.1982
    and 10.3390/ma14164763 with correction retraction erratum; rubidium sphaeroides
    valinomycin uptake; rhenium Saccharomyces 4763 control; helium microbial extraction
    recovery tracer; exact ChEBI and taxonomy terms. Selected first returned results,
    no pagination/date filters. No matching correction notice identified in inspected
    returned titles; not an exhaustive registry audit. Hidden/ignored-inclusive rg
    --no-ignore --hidden --follow covered data/research/reviews/history/.claude and
    bounded cited roots /private/tmp/cmm-next-eu, /private/tmp/cmm-expansion-authorities-20261011,
    /private/tmp/cmm-round11-be-rb-re-raw and /private/tmp/cmm-round11-he-raw; all
    46 repository lines read and selected raw hits inspected. No symlinks in the inspected
    repository science/provenance trees or two new raw roots. No machine-wide absence
    claim.'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round11-final-batch-receipts.json
  locator: Final parent terminal receipts and full logs; reviewer named-validation
    log
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Reviewer independently read parent final checks/logs and own named validation
    terminal 0; structural checks do not prove scientific truth.
- evidence_id: taxonomy
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4932&mode=Info
  locator: Current species name, basionym and rank
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Live official Taxonomy browser and retained datasets JSON identify species
    4932 as Saccharomyces cerevisiae. Neither establishes the unknown brewery strain
    or axenicity, which the record leaves unresolved.
assessments:
- assessment_id: identity-authority
  area: identity
  topic: Neutral element and dated criticality
  outcome: supported
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - record
  - identity
  - criticality
  summary: Correct element identity, jurisdiction, list and edition; ion/mineral/resource/grade
    distinctions preserved.
  dimensions:
  - name: criticality-edition
    value: United States; DOI/USGS Final 2025 List of Critical Minerals; 7 November
      2025; 90 FR 50494–50497; Rhenium row on printed p.50496
    definition: Edition-specific designation at original authority, not a perpetual
      property of every derived material.
    evidence_ids:
    - criticality
- assessment_id: scientific-scope
  area: evidence
  topic: Primary assay and scope limits
  outcome: supported
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - record
  - primary
  - taxonomy
  summary: The element identity, dated designation and narrow inactive-yeast association
    claim are defensible. Primary methods and supplement confirm the record appropriately
    limits source-reported removal estimates, unwashed-biomass analytical fractions
    and fitted capacities, and does not claim Re redox, selective product or deployment.
  dimensions:
  - name: organism-strain
    value: Saccharomyces cerevisiae; brewery residues from Chisinau; strain/axenicity
      unknown
    definition: Species mapping is not strain or purity verification.
    evidence_ids:
    - record
    - primary
  - name: biomass-pretreatment
    value: Biomass dried at 105 C and homogenized; post-contact filtered material
      dried at 105 C
    definition: Microbial origin is explicit; no active metabolism inferred.
    evidence_ids:
    - record
    - primary
  - name: substrate-conditions
    value: Synthetic 10 mg/L Re as NaReO4; optional 5 mg/L Cu/Mo; 500 mg biomass/50
      mL at 200 rpm; parameter-specific pH/time/concentration/temperature series
    definition: Separate parameter series are not pooled; not real industrial wastewater.
    evidence_ids:
    - record
    - primary
  - name: controls-outcome
    value: NAA of retained biomass for Re/Mo; solution AAS for Cu; duplicates; FTIR
      untreated comparison
    definition: Reported removal percentage is qualified, not an independently closed
      solution mass balance; no matched no-biomass removal control documented.
    evidence_ids:
    - record
    - primary
  - name: measurements-models
    value: pH 2 source-reported 84/76/80/75% by feed; kinetic qexp 0.74 mg/g versus
      fitted Langmuir qm 13/20/33/7.7 mg/g
    definition: Figure 2/Table 2 observations remain distinct from Table 3 extrapolations;
      conclusion unit conflict is not silently repaired.
    evidence_ids:
    - record
    - primary
  - name: scale-product
    value: Laboratory inactive-biomass association; no desorption product, Re oxidation-state
      determination or industrial deployment
    definition: Empirical fits and FTIR shifts do not establish molecular causality
      or pure metal.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Actual curation and immutable observation
  outcome: supported
  target_ids:
  - cmmmech:rhenium
  evidence_ids:
  - record
  - validation
  summary: Canonical CREATE sidecar and separate inline event match the target and
    actual actor/times; reviewed working changes remain uncommitted and are attested
    by byte hash. Scientific review does not append curation history.
findings: []
actions: []
limitations:
- The paper does not close the Re analytical mass balance or resolve entrained liquor
  in unwashed retained biomass.
- All fixed conditions and uncertainty definitions are not supplied for every parameter
  series.
- Supplementary S2 scale, fitted-concentration basis and source unit inconsistencies
  limit quantitative reuse; no re-fit performed.
- Separate positive/null Re reduction studies are not direct replications of this
  inactive-yeast assay and are not adjudicated here.
notes:
- No unresolved blocker, major or minor record defect identified. No corrective action
  required for the inspected scope; listed limitations remain.
- No target content, history, dossier or schema changed by this reviewer.
tags:
- round11
- independent
- scientific-review
```
