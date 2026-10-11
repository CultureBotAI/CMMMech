# Independent scientific review of the holmium expansion record

- Review: 20261011T060517Z-holmium-round7-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:02:15Z
- Finished UTC: 2026-10-11T06:05:17Z
- Reviewer: Codex /root/cmm7_terbium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The holmium identity, dated criticality and element-specific association with a harvested cyanobacterial fraction are supported. The record preserves alkaline-medium/control limits, analytical denominators and contradictory source details without claiming a resolved molecular mechanism or industrial recovery. No actionable defect in the inspected state.

## Scope And Provenance

All scientific and provenance fields of the one frozen holmium record, including primary assay, authority identifiers and relevant counterevidence.

Selection: Assigned named record; no sampling. Companion elements are context for interpreting the shared experiment, not additional review targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58e7aef16a9643438cf621fa9fb402e9d325dc65.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:holmium | data/records/holmium.yaml | maintained | Holmium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict named-record validation | passed | True | cmmmech:holmium | Reviewer executed: 3 records checked; 0 failed. |
| Append-only canonical history validation | passed | True | cmmmech:holmium | Reviewer executed: 52 histories checked; 0 errors. |
| Parent-run full-batch native gate | passed | True | cmmmech:holmium | Parent reported terminal exit 0 for session 78922; reviewer independently read the complete /private/tmp/cmm-round7-check.log: lint passed, 307 tests passed and 3 skipped in 51.17 seconds; 42 records and 52 histories valid. |
| Parent-run nonempty corpus gate | passed | True | cmmmech:holmium | Parent reported separate terminal exit 0 for session 19328: 42 records checked, 0 failed. Its separate trusted-base history command also passed with 52 histories and 0 errors. |

## Scientific And Domain Assessments

### Element, dated commodity designation and organism scope

identity: supported. Targets: cmmmech:holmium.

The record identifies the correct element and dated US authority membership, retaining salt and strain distinctions.

### Harvested-fraction association and causal alternatives

evidence: supported. Targets: cmmmech:holmium.

The retained observation is supported. Process other accurately avoids overclaiming a resolved uptake, sorption or precipitation mechanism.

### Element-specific quantities, counterevidence and source discrepancies

quantity: supported. Targets: cmmmech:holmium.

Source-reported 4780-25,780 mg Ho/kg harvested dried fraction; Figure 1 agrees with dose-associated accumulation and places Ho below Er at 10 mg/L. Figure 2 supports inhibition but its 30 mg/L bars do not reproduce a blanket interpretation of the textual 13.7% at 10 mg/L. Lower phycobiliproteins and raised MDA are preserved.

### Distinct CREATE sidecar, inline change event and final-byte attestation

provenance: supported. Targets: cmmmech:holmium.

Canonical history and inline event have actual codex/GPT-6/codex metadata, distinct purposes, valid target paths and current hashes; no historic sidecar is rewritten.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/holmium.yaml; Entire frozen record; linked CREATE sidecar; both curation dossiers | supports | Target and maintained ownership inspected before final assessment. Scientific record was authored by /root/cmm7_ho_er_gd, not this reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:49648; Live official ChEBI page: ID, label, formula, net charge | supports | CHEBI:49648 resolves holmium atom, formula Ho, net charge zero. Element identity is not extended to ions, salts, minerals or secondary resources. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 table, Holmium row, page 50496; notice title/date/pages | supports | Live authority page and retained HTML inspected. USGS Final 2025 List, United States, 7 November 2025, FR 90:50494-50497, names this mineral commodity. Byproduct Yes is not itself a criticality classification. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562&amp;mode=Info; Live NCBI species node and retained EFetch XML OtherNames/Rank | supports | Limnospira platensis, species, has Arthrospira platensis and Spirulina platensis as synonyms. This taxid does not prove a strain-specific CB-02 genome or accession. |
| collection | https://cnmn.utm.md/collections_list; Official catalog indexed result: Spirulina platensis, Cianobacterii, CNMN CB-02 | supports | The official catalog search result independently matches CB-02 to Spirulina platensis. Direct detail-page and catalog opens failed in this reviewer session; no fresh HTML acquisition or inspection of unavailable genome details is claimed. |
| primary | https://doi.org/10.3390/microorganisms12010122; 2024 full-text XML Sections 2.1-2.7, 3 and 4; publisher PDF metadata; original Figures 1-5 | supports | Retained primary files independently read and acquisition hashes verified. The experiment measures total element in dried material retained with growing cultures, with separate element treatments and REE-free culture controls. NAA and the study design support the bounded association observation, not resolved uptake causality. |
| figures | https://doi.org/10.3390/microorganisms12010122; Original JPGs microorganisms-12-00122-g001.jpg through g005.jpg, each visually inspected | supports | Legend colors and axes were checked independently. Figure 1 has element-specific biomass concentrations; Figures 2-4 reveal the physiological differences and source-text inconsistencies retained in the record; Figure 5 is an extract antioxidant assay, not a recovery measurement. |
| limits | https://doi.org/10.3390/microorganisms12010122; Sections 2.2-2.3; full XML supplementary nodes and data-availability statement; acquired supplementaryFiles ZIP inventory | partial | Methods describe filtration followed by drying but no post-filtration washing, matched biomass-free exposure or subcellular separation. The pH 10 bicarbonate/EDTA medium permits unresolved chemical partitioning. The XML has no supplementary-material node and the ZIP contains only five main figures as JPG/GIF pairs; no raw replicate table closes these gaps. |
| search | Live web search and local rg --no-ignore --hidden -L; Named repository trees and referenced local raw directories; first web result sets | context_only | No duplicate accepted element root or actual correction/retraction notice surfaced within this bounded review search. The three records share one primary study and are not treated as independent experiments. |
| validation | /private/tmp/cmm-round7-check.log; Complete parent batch log and separate terminal validator receipts | supports | Complete log independently read: lint passed, 307 tests passed, 3 skipped, 42 records valid and 52 histories valid. Parent also supplied terminal completion receipts for the separate nonempty-corpus and trusted-base history commands. |

## Limits And Additional Notes

- The assay cannot separate intracellular element from surface association, retained medium or co-retained precipitate; pH 10 chemical partitioning remains unresolved.
- Reference-material agreement supports analytical quality but does not establish biological causality or an isolated-product yield.
- The primary source contains figure/text discrepancies. The record preserves them without repairing raw values or claiming a universal toxicity/selectivity result.
- No raw replicate table, subcellular localization, sterile exposure control, post-filtration wash or final aqueous mass balance was acquired from this study.
- PMC web access returned a browser challenge and publisher HTML opens failed; assessment used independently read curator-acquired primary XML/PDF and original figure assets with verified hashes.
- CNMN direct detail/catalog opens failed; reviewer verification of the stated collection label uses the indexed official catalog result, not an invented fresh HTML capture.
- Correction and novelty searches are bounded. No actionable findings in this record does not certify the entire literature or repository.
- No record/history/dossier edits were made by this independent reviewer. Each element receives a separate bundle although all three share a primary study.
- Raw literature remains outside Git. Source hashes and acquisition receipts were independently rechecked; live page access is distinguished from retained-artifact inspection.
- Parent executes the full shared gate; its complete log and terminal receipt are inspected before saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T060517Z-holmium-round7-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the holmium expansion record
started_at: '2026-10-11T06:02:15Z'
finished_at: '2026-10-11T06:05:17Z'
reviewer:
  identity: Codex /root/cmm7_terbium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: This reviewer authored terbium but did not author or edit the
    Ho/Er/Gd records, histories or dossiers. Curator-supplied primary artifacts were
    independently read, original figures visually checked and authority identifiers
    independently resolved. Frozen targets/schema/history/dossiers were inspected
    before final assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The holmium identity, dated criticality and element-specific association
  with a harvested cyanobacterial fraction are supported. The record preserves alkaline-medium/control
  limits, analytical denominators and contradictory source details without claiming
  a resolved molecular mechanism or industrial recovery. No actionable defect in the
  inspected state.
source:
  git_revision: 58e7aef16a9643438cf621fa9fb402e9d325dc65
  state: working_tree
  inputs:
  - path: data/records/holmium.yaml
    sha256: 1abce3e7b19f1f00868f0a1145ae4106c5f12e3b63f6a93246d26aab459a8c15
    role: target
  - path: history/records/holmium/2026-10-11T060018Z-codex-7c7d08.yaml
    sha256: cdae1690933f71d537f4bf36ad1c8ef82f7e3fd0c0f13b20bdf628461f651a20
    role: context
  - path: research/ingests/round7-ho-er-gd-20261011.json
    sha256: 092b826da5c99ebb20667872bff6ee5b029937c2f1dd5c85cfb06ec4b0525210
    role: context
  - path: research/ingests/round7-ho-er-gd-20261011.md
    sha256: 00601f78083f42d84844c3ac690917a271a60fa3209c28a3a98177978d31c422
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:holmium
  path: data/records/holmium.yaml
  label: Holmium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/holmium.yaml
    role: maintained_record
scope:
  description: All scientific and provenance fields of the one frozen holmium record,
    including primary assay, authority identifiers and relevant counterevidence.
  selection: Assigned named record; no sampling. Companion elements are context for
    interpreting the shared experiment, not additional review targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:holmium
checks:
- check_id: record
  name: Strict named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/holmium.yaml data/records/erbium.yaml data/records/gadolinium.yaml
  status: passed
  required: true
  summary: 'Reviewer executed: 3 records checked; 0 failed.'
  target_ids:
  - cmmmech:holmium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only canonical history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 58e7aef16a9643438cf621fa9fb402e9d325dc65
  status: passed
  required: true
  summary: 'Reviewer executed: 52 histories checked; 0 errors.'
  target_ids:
  - cmmmech:holmium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Parent-run full-batch native gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Parent reported terminal exit 0 for session 78922; reviewer independently
    read the complete /private/tmp/cmm-round7-check.log: lint passed, 307 tests passed
    and 3 skipped in 51.17 seconds; 42 records and 52 histories valid.'
  target_ids:
  - cmmmech:holmium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Parent executed the shared final six-record batch. Reviewer read the
    full log and rechecked that all inspected record/schema/history/dossier hashes
    remain current.
- check_id: nonempty
  name: Parent-run nonempty corpus gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Parent reported separate terminal exit 0 for session 19328: 42 records
    checked, 0 failed. Its separate trusted-base history command also passed with
    52 histories and 0 errors.'
  target_ids:
  - cmmmech:holmium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Separate parent-run command and receipt; not represented as reviewer
    execution.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/holmium.yaml
  locator: Entire frozen record; linked CREATE sidecar; both curation dossiers
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: Target and maintained ownership inspected before final assessment. Scientific
    record was authored by /root/cmm7_ho_er_gd, not this reviewer.
  snapshot_sha256: 1abce3e7b19f1f00868f0a1145ae4106c5f12e3b63f6a93246d26aab459a8c15
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:49648
  locator: 'Live official ChEBI page: ID, label, formula, net charge'
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: CHEBI:49648 resolves holmium atom, formula Ho, net charge zero. Element
    identity is not extended to ions, salts, minerals or secondary resources.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 table, Holmium row, page 50496; notice title/date/pages
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: Live authority page and retained HTML inspected. USGS Final 2025 List,
    United States, 7 November 2025, FR 90:50494-50497, names this mineral commodity.
    Byproduct Yes is not itself a criticality classification.
  snapshot_sha256: 95d29893a5b7e4f7c2bb76350747f76619f485e60d88a7db451c6d4ec158cd1c
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=118562&mode=Info
  locator: Live NCBI species node and retained EFetch XML OtherNames/Rank
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: Limnospira platensis, species, has Arthrospira platensis and Spirulina
    platensis as synonyms. This taxid does not prove a strain-specific CB-02 genome
    or accession.
  snapshot_sha256: 94b44b5c4e60d929d2de087d71fcf63809492d7f29c10449b4c9d3e261a60c79
- evidence_id: collection
  kind: database
  reference: https://cnmn.utm.md/collections_list
  locator: 'Official catalog indexed result: Spirulina platensis, Cianobacterii, CNMN
    CB-02'
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: The official catalog search result independently matches CB-02 to Spirulina
    platensis. Direct detail-page and catalog opens failed in this reviewer session;
    no fresh HTML acquisition or inspection of unavailable genome details is claimed.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms12010122
  locator: 2024 full-text XML Sections 2.1-2.7, 3 and 4; publisher PDF metadata; original
    Figures 1-5
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: Retained primary files independently read and acquisition hashes verified.
    The experiment measures total element in dried material retained with growing
    cultures, with separate element treatments and REE-free culture controls. NAA
    and the study design support the bounded association observation, not resolved
    uptake causality.
  snapshot_sha256: fffaf3e7d3cdcb407d0690c6c527af37397550690b126f1b488d274782e6d117
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms12010122
  locator: Original JPGs microorganisms-12-00122-g001.jpg through g005.jpg, each visually
    inspected
  accessed_at: '2026-10-11T06:04:25Z'
  support: supports
  summary: Legend colors and axes were checked independently. Figure 1 has element-specific
    biomass concentrations; Figures 2-4 reveal the physiological differences and source-text
    inconsistencies retained in the record; Figure 5 is an extract antioxidant assay,
    not a recovery measurement.
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms12010122
  locator: Sections 2.2-2.3; full XML supplementary nodes and data-availability statement;
    acquired supplementaryFiles ZIP inventory
  accessed_at: '2026-10-11T06:04:25Z'
  support: partial
  summary: Methods describe filtration followed by drying but no post-filtration washing,
    matched biomass-free exposure or subcellular separation. The pH 10 bicarbonate/EDTA
    medium permits unresolved chemical partitioning. The XML has no supplementary-material
    node and the ZIP contains only five main figures as JPG/GIF pairs; no raw replicate
    table closes these gaps.
- evidence_id: search
  kind: search
  reference: Live web search and local rg --no-ignore --hidden -L
  locator: Named repository trees and referenced local raw directories; first web
    result sets
  accessed_at: '2026-10-11T06:04:25Z'
  support: context_only
  summary: No duplicate accepted element root or actual correction/retraction notice
    surfaced within this bounded review search. The three records share one primary
    study and are not treated as independent experiments.
  search_scope: 'Queries: "10.3390/microorganisms12010122" correction retraction;
    "Arthrospira" "holmium" precipitation control; "Arthrospira" "erbium" "growth"
    2022 2024; "Arthrospira" gadolinium uptake alkaline abiotic; "10.3390/ma15176101"
    correction retraction; site:cnmn.utm.md/collection_page/21 "Spirulina" "CB-02".
    No date/domain filters beyond literal syntax and no pagination. Hidden/ignored-inclusive
    rg over data/records, research, reviews, history and readable files in /private/tmp/cmm-round7-ho-er-gd-raw
    and /private/tmp/cmmmech-round5-ree-raw used root IDs, ChEBI IDs and DOI/PMCID
    tokens. Archives checked after extraction. No machine-wide or exhaustive literature
    absence claim.'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round7-check.log
  locator: Complete parent batch log and separate terminal validator receipts
  accessed_at: '2026-10-11T06:05:17Z'
  support: supports
  summary: 'Complete log independently read: lint passed, 307 tests passed, 3 skipped,
    42 records valid and 52 histories valid. Parent also supplied terminal completion
    receipts for the separate nonempty-corpus and trusted-base history commands.'
  snapshot_sha256: 5078af9116b9809379c012fba4caaa84d909f6b70c71f680be2e8793afd7b755
assessments:
- assessment_id: identity
  area: identity
  topic: Element, dated commodity designation and organism scope
  outcome: supported
  summary: The record identifies the correct element and dated US authority membership,
    retaining salt and strain distinctions.
  target_ids:
  - cmmmech:holmium
  evidence_ids:
  - record
  - identity
  - criticality
  - taxon
  - collection
  dimensions:
  - name: material
    value: Element Ho; experimental Ho(NO3)3·5H2O and harvested biomass are different
      entities.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - identity
    - record
  - name: criticality
    value: United States; USGS Final List of Critical Minerals; 2025 final notice
      dated 7 November 2025, FR 90:50494-50497.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - criticality
  - name: organism
    value: Reported Arthrospira platensis CNMN-CB-02; official catalog Spirulina platensis
      CB-02; NCBI species Limnospira platensis 118562; no strain-specific genome asserted.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - taxon
    - collection
    - primary
- assessment_id: assay
  area: evidence
  topic: Harvested-fraction association and causal alternatives
  outcome: supported
  summary: The retained observation is supported. Process other accurately avoids
    overclaiming a resolved uptake, sorption or precipitation mechanism.
  target_ids:
  - cmmmech:holmium
  evidence_ids:
  - record
  - primary
  - limits
  dimensions:
  - name: biomass
    value: Growing cultures exposed before 5-8 micrometre filtration; part of harvested
      fraction dried for NAA; washing and localization not described.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
    - limits
  - name: substrate
    value: Separate synthetic Ho(III) nitrate treatments at nominal 10, 20 and 30
      mg/L elemental concentration.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
  - name: conditions
    value: 0.4 g/L inoculum, REE addition on day 1, five further days, 500 mL medium,
      30 C, pH 10.0, bicarbonate 8 g/L and EDTA 0.08 g/L; source-printed nonstandard
      illumination retained.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
  - name: controls
    value: REE-free growing culture control; no matched biomass-free exposure result,
      post-filtration wash or cellular fractionation; initial solution ICP-OES, harvested
      fraction NAA.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
    - limits
  - name: scale
    value: Laboratory culture experiment; no desorption, isolated product or industrial
      operation.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
    - record
- assessment_id: outcomes
  area: quantity
  topic: Element-specific quantities, counterevidence and source discrepancies
  outcome: supported
  summary: Source-reported 4780-25,780 mg Ho/kg harvested dried fraction; Figure 1
    agrees with dose-associated accumulation and places Ho below Er at 10 mg/L. Figure
    2 supports inhibition but its 30 mg/L bars do not reproduce a blanket interpretation
    of the textual 13.7% at 10 mg/L. Lower phycobiliproteins and raised MDA are preserved.
  target_ids:
  - cmmmech:holmium
  evidence_ids:
  - primary
  - figures
  - record
  dimensions:
  - name: analytical_denominator
    value: mg element/kg of dried harvested biomass fraction, not percent recovery
      or intracellular concentration; no graph digitization/structured observation.
    definition: Evidence-bounded scope of this record and experiment.
    evidence_ids:
    - primary
    - figures
    - record
- assessment_id: provenance
  area: provenance
  topic: Distinct CREATE sidecar, inline change event and final-byte attestation
  outcome: supported
  summary: Canonical history and inline event have actual codex/GPT-6/codex metadata,
    distinct purposes, valid target paths and current hashes; no historic sidecar
    is rewritten.
  target_ids:
  - cmmmech:holmium
  evidence_ids:
  - record
  - validation
  dimensions: []
findings: []
actions: []
limitations:
- The assay cannot separate intracellular element from surface association, retained
  medium or co-retained precipitate; pH 10 chemical partitioning remains unresolved.
- Reference-material agreement supports analytical quality but does not establish
  biological causality or an isolated-product yield.
- The primary source contains figure/text discrepancies. The record preserves them
  without repairing raw values or claiming a universal toxicity/selectivity result.
- No raw replicate table, subcellular localization, sterile exposure control, post-filtration
  wash or final aqueous mass balance was acquired from this study.
- PMC web access returned a browser challenge and publisher HTML opens failed; assessment
  used independently read curator-acquired primary XML/PDF and original figure assets
  with verified hashes.
- CNMN direct detail/catalog opens failed; reviewer verification of the stated collection
  label uses the indexed official catalog result, not an invented fresh HTML capture.
- Correction and novelty searches are bounded. No actionable findings in this record
  does not certify the entire literature or repository.
notes:
- No record/history/dossier edits were made by this independent reviewer. Each element
  receives a separate bundle although all three share a primary study.
- Raw literature remains outside Git. Source hashes and acquisition receipts were
  independently rechecked; live page access is distinguished from retained-artifact
  inspection.
- Parent executes the full shared gate; its complete log and terminal receipt are
  inspected before saving.
```
