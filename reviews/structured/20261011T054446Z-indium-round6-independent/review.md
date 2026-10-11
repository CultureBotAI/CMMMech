# Independent scientific review of the indium expansion record

- Review: 20261011T054446Z-indium-round6-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T05:40:50Z
- Finished UTC: 2026-10-11T05:44:46Z
- Reviewer: Codex /root/cmm6_aluminium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The element identity, dated US designation and bounded inactive mixed-microalgal biosorption claims are supported by the inspected authorities and accepted manuscript. The record explicitly retains unacquired supplementary controls, fitted-capacity status, Fe competition, declining reuse and the distinction between solution depletion and isolated product. No actionable finding in the reviewed state.

## Scope And Provenance

All scientific fields, source identities and current CREATE provenance of the single indium record.

Selection: Assigned named record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d09a5611767d94fd196393b31d44cb8cf6657f7f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:indium | data/records/indium.yaml | maintained | Indium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict named-record validation | passed | True | cmmmech:indium | 1 record checked; 0 failed. |
| Append-only canonical history validation | passed | True | cmmmech:indium | 45 histories checked; 0 errors. Contemporaneous batch history count; later final gate remains required. |
| Parent-run native full-batch gate | passed | True | cmmmech:indium | Root reported terminal exit 0; reviewer independently read /private/tmp/cmm-round6-check.log: lint passed; 307 tests passed, 3 skipped in 46.67 s; 36 records valid; 46 histories valid. |
| Parent-run nonempty corpus gate | passed | True | cmmmech:indium | Root reported separate terminal exit 0: 36 records checked, 0 failed. The shared batch log independently confirms the same corpus count. |

## Scientific And Domain Assessments

### Element, mixed-biomass organism scope and dated commodity designation

identity: supported. Targets: cmmmech:indium.

Neutral indium identity and US2025 designation are grounded. No organism CURIE is invented for the unresolved mixed biomass, and experimental InCl3 is not equated to the element.

### Biosorption preparation, analytical basis and attribution limits

evidence: supported. Targets: cmmmech:indium.

The narrow claim of indium removal with prepared biomass is supported; it does not require verification of an exclusive molecular binding mechanism or attribution to a single taxon.

### Measured versus fitted outcomes, selectivity and regeneration

quantity: supported. Targets: cmmmech:indium.

The record correctly separates modelled capacity, distinct solution arms and declining reuse; the source counterevidence is retained rather than averaged away.

### Maintained inputs and distinct actual CREATE events

provenance: supported. Targets: cmmmech:indium.

Canonical sidecar and inline event are separately represented with actual codex/GPT-6/codex metadata. Record and history checks pass; source field explicitly identifies accepted-manuscript evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/indium.yaml; Entire record, canonical CREATE sidecar and curation dossier | supports | Frozen target and linked provenance independently inspected; no reviewer edit to record. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:30430; Live curl HTML title, structured molecularFormula and Net Charge row | supports | Official authority gives indium atom, In and charge zero. Web open failed; fresh curl HTML succeeded and was inspected. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 list table, Indium row, page 50496; title/date | supports | Live GovInfo page and retained actual HTML independently inspected. The dated US critical-mineral commodity maps to elemental indium without inheriting designation to salts, minerals or waste. |
| primary | https://upcommons.upc.edu/server/api/core/bitstreams/e2c160fc-f3c7-4279-8931-d298426d9b78/content; Nicomel 2020 accepted manuscript, Sections 2.1-2.10 and 3.1-3.9; Table 2; PDF pp. 6-29 (numbered manuscript pp. 5-28) | supports | Curator-acquired 36-page PDF independently read, SHA verified. Source supports mixed biomass preparation, duplicate synthetic-solution assays, ICP-MS filtration basis, separate pH/kinetics/isotherm/competition/regeneration protocols and their stated limits. |
| figures | https://doi.org/10.1039/C9GC03073E; Accepted-manuscript Figures 2, 5, 9; retained renders nicomel-p15.png, nicomel-p22.png, nicomel-p29.png independently visually inspected | supports | The final-pH response, Fe-associated decrease and progressive loss of adsorption on reuse agree with the record. The Figure 5 asterisk attributes most tin loss to precipitation. |
| metadata | https://pubs.rsc.org/en/content/articlelanding/2020/gc/c9gc03073e; RSC publication metadata, authors, DOI, acceptance/publication dates and supplementary-file listing | context_only | Live publisher landing result confirms article identity, accepted 20 February 2020 and published 21 February 2020. This is metadata/abstract access, not inspection of the final published full text. |
| controls | https://doi.org/10.1039/C9GC03073E; Main-text Section 2.6 and Figure 5 caption; supplementary S2 not acquired | partial | Main text reports precipitation onset near pH 2.7 from controls, but reviewer supplement acquisition at https://www.rsc.org/suppdata/c9/gc/c9gc03073e/c9gc03073e1.pdf returned 404. The control protocol/values remain unverified; record explicitly reports that limit, so no claim of exhaustive precipitation exclusion is accepted. |
| search | Live web search and local rg --no-ignore --hidden; First results only; stated repository trees | context_only | No correction or retraction notice surfaced in the bounded DOI query. No second indium root was found within the searched corpus; new record/provenance and historical frontier candidates were present. |
| validation | /private/tmp/cmm-round6-check.log; Complete final batch log and parent terminal completion receipt | supports | Log read independently: lint passes; 307 tests pass, 3 skip; 36 records and 46 histories validate. Root also reports separate nonempty and trusted-base history gates passed. |

## Limits And Additional Notes

- Final published full text was not acquired; assessment is based on the explicitly cited accepted manuscript with publisher metadata confirmation.
- Supplementary Figure S2, its precipitation-control protocol/values, and other supplementary figures/tables were not acquired. Main-text reports are attributed as such; this review does not establish that all nonbiological losses were excluded.
- Mixed prepared biomass prevents attribution to individual taxa, and surface titration/marginal FTIR changes do not identify one molecular binding mechanism.
- Synthetic solution assays and a pilot biomass source do not establish an actual indium waste-stream process, pure product or industrial deployment.
- Correction and duplication searches are bounded; no new findings in this exact record does not establish an exhaustive literature or corpus-wide pass.
- No indium record/history/dossier edits were made by this reviewer. Exact indium SHA-256 was rechecked unchanged at completion.
- Parent batch gate was shared among reviewers; this reviewer read its full log and parent terminal result. Separate nonempty gate receipt is explicitly parent-reported.
- Raw primary PDF, authority HTML and figure renders remain outside Git. Supplement and final-version access limits are preserved rather than silently omitted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T054446Z-indium-round6-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the indium expansion record
started_at: '2026-10-11T05:40:50Z'
finished_at: '2026-10-11T05:44:46Z'
reviewer:
  identity: Codex /root/cmm6_aluminium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: This reviewer authored aluminium but neither authored nor edited
    indium. The indium curator supplied a retained primary PDF; reviewer independently
    read the complete relevant methods/results and figures, resolved the authority
    identity, and captured frozen target hashes before formal assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The element identity, dated US designation and bounded inactive mixed-microalgal
  biosorption claims are supported by the inspected authorities and accepted manuscript.
  The record explicitly retains unacquired supplementary controls, fitted-capacity
  status, Fe competition, declining reuse and the distinction between solution depletion
  and isolated product. No actionable finding in the reviewed state.
source:
  git_revision: d09a5611767d94fd196393b31d44cb8cf6657f7f
  state: working_tree
  inputs:
  - path: data/records/indium.yaml
    sha256: 92414434d8f03130dcd8fc225659752c66f9b3b726f9c3598f1dcc2b4aa09aed
    role: target
  - path: history/records/indium/2026-10-11T053922Z-codex-ce07d4.yaml
    sha256: 6d1b1fda5fceac3741a4a2d274308db1d93893611eb99e56f05435c07ad1f7f7
    role: context
  - path: research/ingests/round6-indium-20261011.json
    sha256: a8491f1dff709c182903eb268ed2f35bee9a37ae95c6163f1ac44e821b2304c7
    role: context
  - path: research/ingests/round6-indium-20261011.md
    sha256: 5a5df92c0a05e66da261bb9da9f6666c2a9e6aa096e940f7e337a0d69488dc39
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:indium
  path: data/records/indium.yaml
  label: Indium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/indium.yaml
    role: maintained_record
scope:
  description: All scientific fields, source identities and current CREATE provenance
    of the single indium record.
  selection: Assigned named record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:indium
checks:
- check_id: record
  name: Strict named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/indium.yaml
  status: passed
  required: true
  summary: 1 record checked; 0 failed.
  target_ids:
  - cmmmech:indium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only canonical history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base d09a5611767d94fd196393b31d44cb8cf6657f7f
  status: passed
  required: true
  summary: 45 histories checked; 0 errors. Contemporaneous batch history count; later
    final gate remains required.
  target_ids:
  - cmmmech:indium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Parent-run native full-batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root reported terminal exit 0; reviewer independently read /private/tmp/cmm-round6-check.log:
    lint passed; 307 tests passed, 3 skipped in 46.67 s; 36 records valid; 46 histories
    valid.'
  target_ids:
  - cmmmech:indium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by root for the final four-record batch; log inspected by this
    reviewer. No target changes after inspect.
- check_id: nonempty
  name: Parent-run nonempty corpus gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Root reported separate terminal exit 0: 36 records checked, 0 failed.
    The shared batch log independently confirms the same corpus count.'
  target_ids:
  - cmmmech:indium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Executed by root and communicated as a receipt; not rerun by this reviewer.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/indium.yaml
  locator: Entire record, canonical CREATE sidecar and curation dossier
  accessed_at: '2026-10-11T05:42:02Z'
  support: supports
  summary: Frozen target and linked provenance independently inspected; no reviewer
    edit to record.
  snapshot_sha256: 92414434d8f03130dcd8fc225659752c66f9b3b726f9c3598f1dcc2b4aa09aed
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30430
  locator: Live curl HTML title, structured molecularFormula and Net Charge row
  accessed_at: '2026-10-11T05:42:02Z'
  support: supports
  summary: Official authority gives indium atom, In and charge zero. Web open failed;
    fresh curl HTML succeeded and was inspected.
  snapshot_sha256: 07366535d2f95baa68358036a45a60ca19e9eef6dc0c491dd2b6555cdb07e0c4
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 list table, Indium row, page 50496; title/date
  accessed_at: '2026-10-11T05:42:02Z'
  support: supports
  summary: Live GovInfo page and retained actual HTML independently inspected. The
    dated US critical-mineral commodity maps to elemental indium without inheriting
    designation to salts, minerals or waste.
  snapshot_sha256: 1e3a4b5373608f1e700f1f46d848c47e06f6184aa3fdbc8863260d28c995a81f
- evidence_id: primary
  kind: primary_source
  reference: https://upcommons.upc.edu/server/api/core/bitstreams/e2c160fc-f3c7-4279-8931-d298426d9b78/content
  locator: Nicomel 2020 accepted manuscript, Sections 2.1-2.10 and 3.1-3.9; Table
    2; PDF pp. 6-29 (numbered manuscript pp. 5-28)
  accessed_at: '2026-10-11T05:42:02Z'
  support: supports
  summary: Curator-acquired 36-page PDF independently read, SHA verified. Source supports
    mixed biomass preparation, duplicate synthetic-solution assays, ICP-MS filtration
    basis, separate pH/kinetics/isotherm/competition/regeneration protocols and their
    stated limits.
  snapshot_sha256: f50b5218357e0b0ddf31fbfa4052bee796aa1c83e08f7180763a6d1dc9b20573
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1039/C9GC03073E
  locator: Accepted-manuscript Figures 2, 5, 9; retained renders nicomel-p15.png,
    nicomel-p22.png, nicomel-p29.png independently visually inspected
  accessed_at: '2026-10-11T05:42:02Z'
  support: supports
  summary: The final-pH response, Fe-associated decrease and progressive loss of adsorption
    on reuse agree with the record. The Figure 5 asterisk attributes most tin loss
    to precipitation.
- evidence_id: metadata
  kind: primary_source
  reference: https://pubs.rsc.org/en/content/articlelanding/2020/gc/c9gc03073e
  locator: RSC publication metadata, authors, DOI, acceptance/publication dates and
    supplementary-file listing
  accessed_at: '2026-10-11T05:42:02Z'
  support: context_only
  summary: Live publisher landing result confirms article identity, accepted 20 February
    2020 and published 21 February 2020. This is metadata/abstract access, not inspection
    of the final published full text.
- evidence_id: controls
  kind: primary_source
  reference: https://doi.org/10.1039/C9GC03073E
  locator: Main-text Section 2.6 and Figure 5 caption; supplementary S2 not acquired
  accessed_at: '2026-10-11T05:42:02Z'
  support: partial
  summary: Main text reports precipitation onset near pH 2.7 from controls, but reviewer
    supplement acquisition at https://www.rsc.org/suppdata/c9/gc/c9gc03073e/c9gc03073e1.pdf
    returned 404. The control protocol/values remain unverified; record explicitly
    reports that limit, so no claim of exhaustive precipitation exclusion is accepted.
- evidence_id: search
  kind: search
  reference: Live web search and local rg --no-ignore --hidden
  locator: First results only; stated repository trees
  accessed_at: '2026-10-11T05:42:02Z'
  support: context_only
  summary: No correction or retraction notice surfaced in the bounded DOI query. No
    second indium root was found within the searched corpus; new record/provenance
    and historical frontier candidates were present.
  search_scope: 'Queries: "10.1039/C9GC03073E" correction retraction; "Nicomel" indium
    microalgae supplementary information precipitation. No filters or pagination.
    Hidden/ignored-inclusive rg for indium|30430|c9gc03073e covered data/records,research,reviews,history;
    primary raw PDF and authority payloads were inspected independently. No unrelated
    home/temp or exhaustive literature absence claim.'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round6-check.log
  locator: Complete final batch log and parent terminal completion receipt
  accessed_at: '2026-10-11T05:44:46Z'
  support: supports
  summary: 'Log read independently: lint passes; 307 tests pass, 3 skip; 36 records
    and 46 histories validate. Root also reports separate nonempty and trusted-base
    history gates passed.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element, mixed-biomass organism scope and dated commodity designation
  outcome: supported
  summary: Neutral indium identity and US2025 designation are grounded. No organism
    CURIE is invented for the unresolved mixed biomass, and experimental InCl3 is
    not equated to the element.
  target_ids:
  - cmmmech:indium
  evidence_ids:
  - record
  - identity
  - criticality
  - primary
  dimensions:
  - name: material
    value: Element In, distinct from InCl3 feed, indium ions, ITO and host minerals.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - identity
    - record
  - name: criticality
    value: United States; USGS Final List of Critical Minerals; 2025 final, 7 November
      2025, 90 FR 50494-50497.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - criticality
  - name: organism
    value: 'Mixed microalgae: Chlorella sp., Nitzschia/Navicula-dominated diatoms,
      with grazers; no resolved strain or causal community-member claim.'
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - record
- assessment_id: mechanism
  area: evidence
  topic: Biosorption preparation, analytical basis and attribution limits
  outcome: supported
  summary: The narrow claim of indium removal with prepared biomass is supported;
    it does not require verification of an exclusive molecular binding mechanism or
    attribution to a single taxon.
  target_ids:
  - cmmmech:indium
  evidence_ids:
  - primary
  - figures
  - controls
  - record
  dimensions:
  - name: biomass
    value: Harvested June 2017; thickened, centrifuged, frozen, lyophilized, washed,
      dried at 50 C for 24 h and ground below 1 mm; inactive microbial biomass.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
  - name: substrate
    value: Synthetic InCl3 in ultrapure water; actual In waste-stream treatment not
      demonstrated.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - record
  - name: conditions
    value: Duplicate 100 mg / 10 mL batches, 115 rpm, room temperature; 0.15 mM In,
      initial pH 1-2 and 24 h for the pH assay; separate kinetics from 30 min to 24
      h.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
  - name: controls
    value: Main-text precipitation-control report near pH 2.7; S2 control protocol
      and values inaccessible and not treated as independently verified.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - controls
    - record
  - name: assay
    value: 0.45 micrometre filtered aqueous ICP-MS; initial/final concentration difference
      defines removal and uptake per biomass mass; no isolated-product yield.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
  - name: scale
    value: Biomass originated in a 0.5 m3 pilot wastewater pond; indium sorption itself
      remains laboratory batch testing.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - record
- assessment_id: limits
  area: quantity
  topic: Measured versus fitted outcomes, selectivity and regeneration
  outcome: supported
  summary: The record correctly separates modelled capacity, distinct solution arms
    and declining reuse; the source counterevidence is retained rather than averaged
    away.
  target_ids:
  - cmmmech:indium
  evidence_ids:
  - primary
  - figures
  - record
  dimensions:
  - name: outcome
    value: 94.7% removal at initial pH 2, 24 h, in the pH series with 0.15 mM In;
      separate kinetics about 80% at 30 min.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - figures
  - name: model
    value: 0.14 mmol/g is a Langmuir fitted qmax over 0.05-10 mM In; Freundlich fits
      better; not a measured maximum.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
  - name: competition
    value: At 1 mM In with 10 mM Fe(III), removal drops from 67% to 5%; separate Sn
      loss is dominated by precipitation.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - figures
  - name: reuse
    value: 'HCl screen: 80% desorption at 100 mL/g, 24 h; reuse used 60 mL/g, 30 min.
      Adsorption fell from 91.3% to 60.7% across five cycles.'
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - figures
  - name: recovery
    value: Concentration ratio about 1.5; burning to In-rich ash proposed only; no
      isolated metal.
    definition: Evidence-bounded scope of the reviewed claim.
    evidence_ids:
    - primary
    - record
- assessment_id: provenance
  area: provenance
  topic: Maintained inputs and distinct actual CREATE events
  outcome: supported
  summary: Canonical sidecar and inline event are separately represented with actual
    codex/GPT-6/codex metadata. Record and history checks pass; source field explicitly
    identifies accepted-manuscript evidence.
  target_ids:
  - cmmmech:indium
  evidence_ids:
  - record
  - primary
  - metadata
  - validation
findings: []
actions: []
limitations:
- Final published full text was not acquired; assessment is based on the explicitly
  cited accepted manuscript with publisher metadata confirmation.
- Supplementary Figure S2, its precipitation-control protocol/values, and other supplementary
  figures/tables were not acquired. Main-text reports are attributed as such; this
  review does not establish that all nonbiological losses were excluded.
- Mixed prepared biomass prevents attribution to individual taxa, and surface titration/marginal
  FTIR changes do not identify one molecular binding mechanism.
- Synthetic solution assays and a pilot biomass source do not establish an actual
  indium waste-stream process, pure product or industrial deployment.
- Correction and duplication searches are bounded; no new findings in this exact record
  does not establish an exhaustive literature or corpus-wide pass.
notes:
- No indium record/history/dossier edits were made by this reviewer. Exact indium
  SHA-256 was rechecked unchanged at completion.
- Parent batch gate was shared among reviewers; this reviewer read its full log and
  parent terminal result. Separate nonempty gate receipt is explicitly parent-reported.
- Raw primary PDF, authority HTML and figure renders remain outside Git. Supplement
  and final-version access limits are preserved rather than silently omitted.
```
