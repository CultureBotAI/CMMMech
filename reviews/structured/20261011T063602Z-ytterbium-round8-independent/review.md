# Independent scientific review of Ytterbium

- Review: 20261011T063602Z-ytterbium-round8-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:27:08Z
- Finished UTC: 2026-10-11T06:36:02Z
- Reviewer: Codex /root/cmm8_pb_bi (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The individual ytterbium assay and identifiers support the narrow record; Dy-only mechanism/precision claims are correctly excluded. No actionable record finding in this scope.

## Scope And Provenance

All scientific fields and curation provenance of this record, with maintained dossier evidence precision.

Selection: Assigned exact record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5b4a463f700bceb441f7b669f58a5e60823d2841.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ytterbium | data/records/ytterbium.yaml | maintained | Ytterbium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict named-record validation | passed | True | cmmmech:ytterbium | Repeated after dossier-only correction: 2 records checked; 0 failed; terminal exit 0 observed. |
| Append-only history validation | passed | True | cmmmech:ytterbium | 58 history records checked; 0 errors. |
| Parent-run full batch gate | passed | True | cmmmech:ytterbium | Parent terminal exit 0 confirmed; complete log independently read: lint passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid. |
| Parent-run nonempty batch gate | passed | True | cmmmech:ytterbium | Parent terminal exit 0 confirmed; separate log independently read: 48 records, 0 failed. |

## Scientific And Domain Assessments

### Element and organism scope; dated criticality

identity: supported. Targets: cmmmech:ytterbium.

Elemental identity, exact US 2025 commodity designation and organism resolution are supported without inheriting claims to salts, minerals or waste.

### Analyte-specific substrate, conditions, outcome and causal limits

evidence: supported. Targets: cmmmech:ytterbium.

The narrow Yb-specific depletion claim is supported. Detailed Dy assays are not transferred, and no phase, localization, purified product or industrial deployment is asserted.

### Actual CREATE events and reviewed state

provenance: supported. Targets: cmmmech:ytterbium.

Canonical CREATE sidecar and later inline event correctly identify codex/GPT-6/codex, target and actual work. Working-tree state and exact target/dossier hashes are retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/ytterbium.yaml; Entire frozen target, linked CREATE session and exact curation dossier inputs | supports | Captured before scientific assessment; species/material/assay boundaries and distinct actual curation events checked. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33381; Live reviewer-acquired HTML title, molecularFormula and Net Charge | supports | Verified neutral ytterbium atom, correct elemental formula and zero charge. Web rendering failed; direct public authority HTML succeeded. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1391704/dataset_report; Live reviewer-acquired NCBI Datasets report, name and rank | supports | Penidiella sp. T9 is the named isolate node, ranked species but not a formally resolved named species. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final named Ytterbium commodity row and table headers; notice date and edition | supports | Official notice acquired live in this reviewer session and reread for Ytterbium. Supports scoped US 2025 designation; byproduct column is not the designation decision. |
| primary | https://doi.org/10.1128/AEM.00300-15; Full retained PMC HTML: Media and cultivation; Specificity of metal bioaccumulation; Measurement of Dy; REE-specific results | supports | Independently read individual Yb assay: nominal 100 mg/L chloride treatment in BSM, pH 2.5, 30 C, 120 rpm; 45% dissolved-Yb depletion at day 3, with textual near-null no-T9 comparison. Separate Yb calibration, control concentrations and biological error estimates are not reported. |
| figures | https://doi.org/10.1128/AEM.00300-15; Primary Figures 4 and 5, direct deposited JPGs visually inspected | supports | Figure 4 time course and independent-experiment standard deviations are Dy-specific; Figure 5 EDX maps Dy/P, not Yb. Record correctly excludes their transfer to Yb phase/localization or precision. |
| search | Live web search and rg --no-ignore --hidden --follow; First result pages and scoped repository/raw evidence trees | context_only | No applicable correction notice identified in these bounded searches. The ASM TOC includes unrelated corrections; its Horiike entry is a research article, so a search-snippet adjacency was not treated as a correction. No second accepted exact Y/Yb root identified in the scoped search. |
| batch | /private/tmp/cmm-round8-batch.log; Complete command log and parent terminal receipt | supports | Parent terminal exit 0 confirmed; complete log independently read: lint passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid. |
| nonempty | /private/tmp/cmm-round8-corpus.log; Complete command log and parent terminal receipt | supports | Parent terminal exit 0 confirmed; separate log independently read: 48 records, 0 failed. |
| dossier | research/ingests/round8-y-yb-20261011.md; Ytterbium evidence and final correction provenance | supports | Final shared dossier retains the Yb-specific measurement/control limits and separates Dy-only figures. The Y-only replication correction does not change Yb claims. |

## Limits And Additional Notes

- Yb-specific analytical calibration, raw control values, error estimates and biological replication are absent from the inspected source; detailed Dy experiments do not fill these gaps.
- No intracellular mechanism, identified retained phase, isolated-product yield or industrial deployment established.
- Correction and duplication searches are bounded; primary sources and fields outside this target are not certified by this review.
- No record, history or dossier edits performed by reviewer. Raw public authority rechecks are retained under /private/tmp/cmm-round8-y-yb-review; original primary artifacts remain under /private/tmp/cmm-round8-y-yb-evidence.
- The final shared dossier includes issue-37 clarification for yttrium only; the Yb scientific narrative, record and history are unchanged. This review captures those final shared dossier bytes.
- Full batch gates preceded the dossier-only clarification. Their record/history inputs remain unchanged; affected named validation and exact input hashing were repeated afterward.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063602Z-ytterbium-round8-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Ytterbium
started_at: '2026-10-11T06:27:08Z'
finished_at: '2026-10-11T06:36:02Z'
reviewer:
  identity: Codex /root/cmm8_pb_bi
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer curated Pb/Bi and did not author or modify these Y/Yb
    records, histories or dossiers. Captured frozen hashes before independently checking
    primary methods/results, figures, identifiers and bounded counterevidence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The individual ytterbium assay and identifiers support the narrow record;
  Dy-only mechanism/precision claims are correctly excluded. No actionable record
  finding in this scope.
source:
  git_revision: 5b4a463f700bceb441f7b669f58a5e60823d2841
  state: working_tree
  inputs:
  - path: data/records/ytterbium.yaml
    sha256: b29100506b873c5262a0d9e186c4442c0286bdb666a13b596a30c5c42910eb7e
    role: target
  - path: history/records/ytterbium/2026-10-11T062417Z-codex-a7602a.yaml
    sha256: 35fabab287b5215fff28b81b8ba8faab543d601c9cdebde3e50801e4925d5ce1
    role: context
  - path: research/ingests/round8-y-yb-20261011.json
    sha256: e4a94110f441a913969b60842ab105486bf33f8aac2c0c77fe5fb22568352746
    role: context
  - path: research/ingests/round8-y-yb-20261011.md
    sha256: 2e29186a39daef63a57051f7551bc5fa5cb18c030ad36d2af366286264745070
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:ytterbium
  path: data/records/ytterbium.yaml
  label: Ytterbium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ytterbium.yaml
    role: maintained_record
scope:
  description: All scientific fields and curation provenance of this record, with
    maintained dossier evidence precision.
  selection: Assigned exact record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ytterbium
checks:
- check_id: records
  name: Strict named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/yttrium.yaml data/records/ytterbium.yaml
  status: passed
  required: true
  summary: 'Repeated after dossier-only correction: 2 records checked; 0 failed; terminal
    exit 0 observed.'
  target_ids:
  - cmmmech:ytterbium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 5b4a463f700bceb441f7b669f58a5e60823d2841
  status: passed
  required: true
  summary: 58 history records checked; 0 errors.
  target_ids:
  - cmmmech:ytterbium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Parent-run full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Parent terminal exit 0 confirmed; complete log independently read: lint
    passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid.'
  target_ids:
  - cmmmech:ytterbium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run by root for final six-record batch; reviewer independently read
    complete log and parent terminal result.
- check_id: nonempty
  name: Parent-run nonempty batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Parent terminal exit 0 confirmed; separate log independently read: 48
    records, 0 failed.'
  target_ids:
  - cmmmech:ytterbium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run by root for final six-record batch; reviewer independently read
    complete log and parent terminal result.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/ytterbium.yaml
  locator: Entire frozen target, linked CREATE session and exact curation dossier
    inputs
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Captured before scientific assessment; species/material/assay boundaries
    and distinct actual curation events checked.
  snapshot_sha256: b29100506b873c5262a0d9e186c4442c0286bdb666a13b596a30c5c42910eb7e
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33381
  locator: Live reviewer-acquired HTML title, molecularFormula and Net Charge
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Verified neutral ytterbium atom, correct elemental formula and zero charge.
    Web rendering failed; direct public authority HTML succeeded.
  snapshot_sha256: 3b3d0e62e828b2db7a893370543ba9c77ae6647188942f9fe1839201de2b4505
- evidence_id: taxon
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1391704/dataset_report
  locator: Live reviewer-acquired NCBI Datasets report, name and rank
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Penidiella sp. T9 is the named isolate node, ranked species but not a formally
    resolved named species.
  snapshot_sha256: 0f67b3a6b4ddcc14eae7c5eb1ae8aea063c4c73d7349faab8ea9fe14b8bcdd08
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final named Ytterbium commodity row and table headers; notice date and
    edition
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Official notice acquired live in this reviewer session and reread for Ytterbium.
    Supports scoped US 2025 designation; byproduct column is not the designation decision.
  snapshot_sha256: 0d3527a735c3fa04765a98d3b9140af0c221e5fd7706b96329b5c7d900591f7e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.00300-15
  locator: 'Full retained PMC HTML: Media and cultivation; Specificity of metal bioaccumulation;
    Measurement of Dy; REE-specific results'
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: 'Independently read individual Yb assay: nominal 100 mg/L chloride treatment
    in BSM, pH 2.5, 30 C, 120 rpm; 45% dissolved-Yb depletion at day 3, with textual
    near-null no-T9 comparison. Separate Yb calibration, control concentrations and
    biological error estimates are not reported.'
  snapshot_sha256: 7c5522aa97feb089ace2fc9b8c312fc2a4f225a5a66adc1f14413d2d3ac9e03d
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.00300-15
  locator: Primary Figures 4 and 5, direct deposited JPGs visually inspected
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Figure 4 time course and independent-experiment standard deviations are
    Dy-specific; Figure 5 EDX maps Dy/P, not Yb. Record correctly excludes their transfer
    to Yb phase/localization or precision.
  snapshot_sha256: 0a04996e3ce14fa2ca1c65318eef03d5fb45164ea46028e177bf1e364c711360
- evidence_id: search
  kind: search
  reference: Live web search and rg --no-ignore --hidden --follow
  locator: First result pages and scoped repository/raw evidence trees
  accessed_at: '2026-10-11T06:30:20Z'
  support: context_only
  summary: No applicable correction notice identified in these bounded searches. The
    ASM TOC includes unrelated corrections; its Horiike entry is a research article,
    so a search-snippet adjacency was not treated as a correction. No second accepted
    exact Y/Yb root identified in the scoped search.
  search_scope: 'Queries: "10.3390/plants11101376" correction retraction; "10.1128/AEM.00300-15"
    correction retraction; "Galdieria" "ACUF 427" yttrium abiotic precipitation. First
    results, no exhaustive pagination. Hidden/ignored-inclusive rg --follow searched
    data, research, reviews, history and /private/tmp/cmm-round8-y-yb-evidence for
    exact roots, ChEBI IDs and DOIs. Existing record/dossier and related primary sources
    found. No machine-wide or exhaustive literature absence claim.'
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round8-batch.log
  locator: Complete command log and parent terminal receipt
  accessed_at: '2026-10-11T06:30:36Z'
  support: supports
  summary: 'Parent terminal exit 0 confirmed; complete log independently read: lint
    passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid.'
  snapshot_sha256: a143a8808e0b322d1a9d95769a824de04bd1f8721483d97d6d69efc07bba081b
- evidence_id: nonempty
  kind: validation
  reference: /private/tmp/cmm-round8-corpus.log
  locator: Complete command log and parent terminal receipt
  accessed_at: '2026-10-11T06:30:36Z'
  support: supports
  summary: 'Parent terminal exit 0 confirmed; separate log independently read: 48
    records, 0 failed.'
  snapshot_sha256: ce967cc4de998d9b6f282ce61c5cc459653297e1684f3519272ed090bbf20d84
- evidence_id: dossier
  kind: record_content
  reference: research/ingests/round8-y-yb-20261011.md
  locator: Ytterbium evidence and final correction provenance
  accessed_at: '2026-10-11T06:36:02Z'
  support: supports
  summary: Final shared dossier retains the Yb-specific measurement/control limits
    and separates Dy-only figures. The Y-only replication correction does not change
    Yb claims.
  snapshot_sha256: 2e29186a39daef63a57051f7551bc5fa5cb18c030ad36d2af366286264745070
assessments:
- assessment_id: identity
  area: identity
  topic: Element and organism scope; dated criticality
  outcome: supported
  summary: Elemental identity, exact US 2025 commodity designation and organism resolution
    are supported without inheriting claims to salts, minerals or waste.
  target_ids:
  - cmmmech:ytterbium
  evidence_ids:
  - record
  - identity
  - taxon
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Analyte-specific substrate, conditions, outcome and causal limits
  outcome: supported
  summary: The narrow Yb-specific depletion claim is supported. Detailed Dy assays
    are not transferred, and no phase, localization, purified product or industrial
    deployment is asserted.
  target_ids:
  - cmmmech:ytterbium
  evidence_ids:
  - record
  - primary
  - figures
  dimensions:
  - name: substrate_and_conditions
    value: Single-element Yb chloride, nominal 100 mg/L; buffered BSM pH 2.5, 30 C,
      120 rpm, day-3 endpoint.
    definition: Conditions actually associated with accepted analyte-specific result.
    evidence_ids:
    - primary
  - name: outcome_and_denominator
    value: 45% depletion of initial dissolved Yb; not percent isolated product or
      Yb per dry biomass.
    definition: Measured or source-reported endpoint and denominator, without cross-arm
      extrapolation.
    evidence_ids:
    - primary
    - figures
  - name: biomass_controls_scale
    value: Cultivated Penidiella T9; textual no-T9 near-null comparison, no numerical
      Yb blank; laboratory assay, unresolved retention chemistry.
    definition: Organism state, comparison basis and demonstrated deployment scale.
    evidence_ids:
    - primary
    - record
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE events and reviewed state
  outcome: supported
  summary: Canonical CREATE sidecar and later inline event correctly identify codex/GPT-6/codex,
    target and actual work. Working-tree state and exact target/dossier hashes are
    retained.
  target_ids:
  - cmmmech:ytterbium
  evidence_ids:
  - record
findings: []
actions: []
limitations:
- Yb-specific analytical calibration, raw control values, error estimates and biological
  replication are absent from the inspected source; detailed Dy experiments do not
  fill these gaps.
- No intracellular mechanism, identified retained phase, isolated-product yield or
  industrial deployment established.
- Correction and duplication searches are bounded; primary sources and fields outside
  this target are not certified by this review.
notes:
- No record, history or dossier edits performed by reviewer. Raw public authority
  rechecks are retained under /private/tmp/cmm-round8-y-yb-review; original primary
  artifacts remain under /private/tmp/cmm-round8-y-yb-evidence.
- The final shared dossier includes issue-37 clarification for yttrium only; the Yb
  scientific narrative, record and history are unchanged. This review captures those
  final shared dossier bytes.
- Full batch gates preceded the dossier-only clarification. Their record/history inputs
  remain unchanged; affected named validation and exact input hashing were repeated
  afterward.
```
