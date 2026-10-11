# Independent scientific review of Yttrium

- Review: 20261011T063036Z-yttrium-round8-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:27:08Z
- Finished UTC: 2026-10-11T06:30:36Z
- Reviewer: Codex /root/cmm8_pb_bi (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The scientific record is supported with explicit limits; a minor dossier-only replication qualifier needs correction.

## Scope And Provenance

All scientific fields and curation provenance of this record, with maintained dossier evidence precision.

Selection: Assigned exact record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5b4a463f700bceb441f7b669f58a5e60823d2841.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:yttrium | data/records/yttrium.yaml | maintained | Yttrium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict named-record validation | passed | True | cmmmech:yttrium | 2 records checked; 0 failed. |
| Append-only history validation | passed | True | cmmmech:yttrium | 58 history records checked; 0 errors. |
| Parent-run batch batch gate | passed | True | cmmmech:yttrium | Parent terminal exit 0 confirmed; complete log independently read: lint passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid. |
| Parent-run nonempty batch gate | passed | True | cmmmech:yttrium | Parent terminal exit 0 confirmed; separate log independently read: 48 records, 0 failed. |

## Scientific And Domain Assessments

### Element and organism scope; dated criticality

identity: supported. Targets: cmmmech:yttrium.

Elemental identity, exact US 2025 commodity designation and organism resolution are supported without inheriting claims to salts, minerals or waste.

### Analyte-specific substrate, conditions, outcome and causal limits

evidence: supported. Targets: cmmmech:yttrium.

Washed living-biomass Y association is supported; source-reported pH insensitivity of ACUF 427 and lower mixture association remain explicit. Surface binding, uptake and retained precipitate are unresolved.

### Actual CREATE events and reviewed state

provenance: supported. Targets: cmmmech:yttrium.

Canonical CREATE sidecar and later inline event correctly identify codex/GPT-6/codex, target and actual work. Working-tree state and exact target/dossier hashes are retained.

### Dossier versus source replication precision

evidence: concern. Targets: cmmmech:yttrium.

A minor maintained-dossier qualifier exceeds source support; scientific record wording is already correct.

## Findings

### replicate-independence: Dossier upgrades unspecified triplicates to biological replication

minor / open / confirmed; issue key: yttrium-dossier-replicate-independence.

The Yttrium evidence paragraph calls the assay biological triplicates. Iovinella Methods 4.3-4.4 describe triplicate experiments in wells and a defined culture volume, without documenting independent culture derivation. The record itself correctly says triplicate. Narrow the dossier wording and retain the independence limit; no scientific record change or artificial EDIT session is warranted.

## Recommended Actions And Acceptance Checks

### qualify-dossier-replication

Replace biological triplicates with triplicate experiments and state that independent culture derivation is unspecified. Preserve source-reported mean/SD without strengthening their replication basis.

- Compare revised dossier wording with primary Methods 4.3-4.4; no unsupported independence claim remains.
- Verify record and sidecar bytes remain unchanged; do not invent an EDIT for a dossier-only correction.
- Save a successor observation resolving the same stable issue key and exact predecessor occurrence with updated dossier hashes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/yttrium.yaml; Entire frozen target, linked CREATE session and exact curation dossier inputs | supports | Captured before scientific assessment; species/material/assay boundaries and distinct actual curation events checked. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33331; Live reviewer-acquired HTML title, molecularFormula and Net Charge | supports | Verified neutral yttrium atom, correct elemental formula and zero charge. Web rendering failed; direct public authority HTML succeeded. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/83373/dataset_report; Live reviewer-acquired NCBI Datasets report, name and rank | supports | Galdieria is a genus; exact ACUF 427 remains explicit despite changed species nomenclature. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final named Yttrium commodity row and table headers; notice date and edition | supports | Official notice acquired live in this reviewer session and reread for Yttrium. Supports scoped US 2025 designation; byproduct column is not the designation decision. |
| primary | https://doi.org/10.3390/plants11101376; Full published XML Sections 2.1-2.2 and 4.1-4.4; source formula and controls | supports | Independently read retained primary text: living washed ACUF 427, 178 micromolar Y alone or each element in four-metal mixture, 2 mL, OD550 5, 37 C, 24 h; washed biomass acid digestion/ICP-MS defines the micromol/g dry-mass measurement. |
| figures | https://eprints.whiterose.ac.uk/id/eprint/187397/1/plants_1717589.pdf; Author-manuscript Figures 1 and 3 on PDF pages 6 and 10; both retained renders visually inspected | supports | Single-Y versus mixed-Y bars agree with published text: 22.43 +/- 2.05 versus 5.08 micromol/g at pH 2.5 for ACUF 427. This figure copy is an author manuscript; published XML grounds the accepted text. |
| taxonomy_context | https://doi.org/10.3390/plants14132043; Primary XML author list, Section 2 and strain/methods passages | supports | Author list begins Ciniglia; the article names Galdieria daedala ACUF 427. Genus-level record grounding is consistent, and transporter predictions are not assigned Y causality. |
| replication | https://doi.org/10.3390/plants11101376; Methods 4.3-4.4 and main-text supplementary Figure S1 caption | partial | Experiments are described as triplicate wells; independent culture derivation is not established. The record preserves this correctly, but the frozen dossier upgrades it to biological triplicates. |
| dossier | research/ingests/round8-y-yb-20261011.md; Yttrium evidence, second paragraph: biological triplicates | partial | This unsupported qualifier is a minor evidence-precision issue in the maintained dossier; it does not alter the correctly limited record claim. |
| search | Live web search and rg --no-ignore --hidden --follow; First result pages and scoped repository/raw evidence trees | context_only | No applicable correction notice identified in these bounded searches. The ASM TOC includes unrelated corrections; its Horiike entry is a research article, so a search-snippet adjacency was not treated as a correction. No second accepted exact Y/Yb root identified in the scoped search. |
| batch | /private/tmp/cmm-round8-batch.log; Complete command log and parent terminal receipt | supports | Parent terminal exit 0 confirmed; complete log independently read: lint passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid. |
| nonempty | /private/tmp/cmm-round8-corpus.log; Complete command log and parent terminal receipt | supports | Parent terminal exit 0 confirmed; separate log independently read: 48 records, 0 failed. |

## Limits And Additional Notes

- Y supplementary tables/figure were unavailable to the curator; primary main-text methods/results and author-manuscript figures were inspected, without claiming numerical blank recoveries or complete balances.
- No intracellular mechanism, identified retained phase, isolated-product yield or industrial deployment established.
- Correction and duplication searches are bounded; primary sources and fields outside this target are not certified by this review.
- Reviewer attempted the exact PMC supplementary ZIP path; HTTP 404 prevented acquisition, so no supplementary numerical inspection is claimed.
- No record, history or dossier edits performed by reviewer. Raw public authority rechecks are retained under /private/tmp/cmm-round8-y-yb-review; original primary artifacts remain under /private/tmp/cmm-round8-y-yb-evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063036Z-yttrium-round8-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Yttrium
started_at: '2026-10-11T06:27:08Z'
finished_at: '2026-10-11T06:30:36Z'
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
verdict: needs_curation
scientific_review: true
summary: The scientific record is supported with explicit limits; a minor dossier-only
  replication qualifier needs correction.
source:
  git_revision: 5b4a463f700bceb441f7b669f58a5e60823d2841
  state: working_tree
  inputs:
  - path: data/records/yttrium.yaml
    sha256: ad5b7c2e2696c9d96b5e2a48117c2591bd3c301ffba23ce16920331a020c5aa9
    role: target
  - path: history/records/yttrium/2026-10-11T062414Z-codex-03422f.yaml
    sha256: 33be831c73887e8260b1e8850309259bdccc722474eda269b1dae23e0d5c81a0
    role: context
  - path: research/ingests/round8-y-yb-20261011.json
    sha256: b234157476e734dee63d8a0445d143a15eb6041e6edc52c4ad1b7862438c8cce
    role: context
  - path: research/ingests/round8-y-yb-20261011.md
    sha256: 45c38187d4bdd86b8dc2eeed618cc57a556fbdf86ec189ab44c4808977a7ee97
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:yttrium
  path: data/records/yttrium.yaml
  label: Yttrium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/yttrium.yaml
    role: maintained_record
scope:
  description: All scientific fields and curation provenance of this record, with
    maintained dossier evidence precision.
  selection: Assigned exact record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:yttrium
checks:
- check_id: records
  name: Strict named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/yttrium.yaml data/records/ytterbium.yaml
  status: passed
  required: true
  summary: 2 records checked; 0 failed.
  target_ids:
  - cmmmech:yttrium
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
  - cmmmech:yttrium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Parent-run batch batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Parent terminal exit 0 confirmed; complete log independently read: lint
    passed, 307 tests passed, 3 skipped in 46.87 s; 48 records and 58 histories valid.'
  target_ids:
  - cmmmech:yttrium
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
  - cmmmech:yttrium
  exit_code: 0
  expected_exit_code: 0
  scope_note: Run by root for final six-record batch; reviewer independently read
    complete log and parent terminal result.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/yttrium.yaml
  locator: Entire frozen target, linked CREATE session and exact curation dossier
    inputs
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Captured before scientific assessment; species/material/assay boundaries
    and distinct actual curation events checked.
  snapshot_sha256: ad5b7c2e2696c9d96b5e2a48117c2591bd3c301ffba23ce16920331a020c5aa9
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33331
  locator: Live reviewer-acquired HTML title, molecularFormula and Net Charge
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Verified neutral yttrium atom, correct elemental formula and zero charge.
    Web rendering failed; direct public authority HTML succeeded.
  snapshot_sha256: 9ca0a587cbfc4b1837aa06af2365487b9414b4ea08d2299811a73fa485899c6c
- evidence_id: taxon
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/83373/dataset_report
  locator: Live reviewer-acquired NCBI Datasets report, name and rank
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Galdieria is a genus; exact ACUF 427 remains explicit despite changed species
    nomenclature.
  snapshot_sha256: adc4cc359605ff50393bd7115f511e7f636edd8bf68b56f1ee0f05aa25f61332
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final named Yttrium commodity row and table headers; notice date and edition
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Official notice acquired live in this reviewer session and reread for Yttrium.
    Supports scoped US 2025 designation; byproduct column is not the designation decision.
  snapshot_sha256: 0d3527a735c3fa04765a98d3b9140af0c221e5fd7706b96329b5c7d900591f7e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/plants11101376
  locator: Full published XML Sections 2.1-2.2 and 4.1-4.4; source formula and controls
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: 'Independently read retained primary text: living washed ACUF 427, 178
    micromolar Y alone or each element in four-metal mixture, 2 mL, OD550 5, 37 C,
    24 h; washed biomass acid digestion/ICP-MS defines the micromol/g dry-mass measurement.'
  snapshot_sha256: 6ba783b52677e954966f359d2aabcacdfcfb61526e2fa2b6a55021eab573f225
- evidence_id: figures
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/187397/1/plants_1717589.pdf
  locator: Author-manuscript Figures 1 and 3 on PDF pages 6 and 10; both retained
    renders visually inspected
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: 'Single-Y versus mixed-Y bars agree with published text: 22.43 +/- 2.05
    versus 5.08 micromol/g at pH 2.5 for ACUF 427. This figure copy is an author manuscript;
    published XML grounds the accepted text.'
  snapshot_sha256: 9462823672611d5a45cc0d2d50f99b4e890f19a9f7544c130544363279de3824
- evidence_id: taxonomy_context
  kind: primary_source
  reference: https://doi.org/10.3390/plants14132043
  locator: Primary XML author list, Section 2 and strain/methods passages
  accessed_at: '2026-10-11T06:30:20Z'
  support: supports
  summary: Author list begins Ciniglia; the article names Galdieria daedala ACUF 427.
    Genus-level record grounding is consistent, and transporter predictions are not
    assigned Y causality.
  snapshot_sha256: 8d77e38265bcaf45b38fd7b489e5f2f7b84e0c2d223f724c50c35ffd47c3da04
- evidence_id: replication
  kind: primary_source
  reference: https://doi.org/10.3390/plants11101376
  locator: Methods 4.3-4.4 and main-text supplementary Figure S1 caption
  accessed_at: '2026-10-11T06:30:20Z'
  support: partial
  summary: Experiments are described as triplicate wells; independent culture derivation
    is not established. The record preserves this correctly, but the frozen dossier
    upgrades it to biological triplicates.
  snapshot_sha256: 6ba783b52677e954966f359d2aabcacdfcfb61526e2fa2b6a55021eab573f225
- evidence_id: dossier
  kind: record_content
  reference: research/ingests/round8-y-yb-20261011.md
  locator: 'Yttrium evidence, second paragraph: biological triplicates'
  accessed_at: '2026-10-11T06:30:20Z'
  support: partial
  summary: This unsupported qualifier is a minor evidence-precision issue in the maintained
    dossier; it does not alter the correctly limited record claim.
  snapshot_sha256: 45c38187d4bdd86b8dc2eeed618cc57a556fbdf86ec189ab44c4808977a7ee97
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
assessments:
- assessment_id: identity
  area: identity
  topic: Element and organism scope; dated criticality
  outcome: supported
  summary: Elemental identity, exact US 2025 commodity designation and organism resolution
    are supported without inheriting claims to salts, minerals or waste.
  target_ids:
  - cmmmech:yttrium
  evidence_ids:
  - record
  - identity
  - taxon
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Analyte-specific substrate, conditions, outcome and causal limits
  outcome: supported
  summary: Washed living-biomass Y association is supported; source-reported pH insensitivity
    of ACUF 427 and lower mixture association remain explicit. Surface binding, uptake
    and retained precipitate are unresolved.
  target_ids:
  - cmmmech:yttrium
  evidence_ids:
  - record
  - primary
  - figures
  dimensions:
  - name: substrate_and_conditions
    value: Y chloride alone or four-metal synthetic solution; 178 micromolar each;
      2 mL, OD550 5, 37 C, 24 h, initial pH 2.5-5.5.
    definition: Conditions actually associated with accepted analyte-specific result.
    evidence_ids:
    - primary
  - name: outcome_and_denominator
    value: 22.43 +/- 2.05 and 5.08 micromol Y/g dry biomass in separate single/mixed
      pH-2.5 arms; not recovered metal.
    definition: Measured or source-reported endpoint and denominator, without cross-arm
      extrapolation.
    evidence_ids:
    - primary
    - figures
  - name: biomass_controls_scale
    value: Living ACUF 427; metal-only and biomass-only controls, two washes after
      exposure; laboratory assay, unresolved localization.
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
  - cmmmech:yttrium
  evidence_ids:
  - record
- assessment_id: replication_scope
  area: evidence
  topic: Dossier versus source replication precision
  outcome: concern
  summary: A minor maintained-dossier qualifier exceeds source support; scientific
    record wording is already correct.
  target_ids:
  - cmmmech:yttrium
  evidence_ids:
  - replication
  - dossier
  - record
findings:
- finding_id: replicate-independence
  issue_key: yttrium-dossier-replicate-independence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Dossier upgrades unspecified triplicates to biological replication
  description: The Yttrium evidence paragraph calls the assay biological triplicates.
    Iovinella Methods 4.3-4.4 describe triplicate experiments in wells and a defined
    culture volume, without documenting independent culture derivation. The record
    itself correctly says triplicate. Narrow the dossier wording and retain the independence
    limit; no scientific record change or artificial EDIT session is warranted.
  target_ids:
  - cmmmech:yttrium
  field_paths:
  - research/ingests/round8-y-yb-20261011.md#Yttrium evidence
  evidence_ids:
  - replication
  - dossier
  - record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round8-y-yb-20261011.md
    role: maintained_curation_dossier
  rule_id: preserve-experimental-replication-scope
actions:
- action_id: qualify-dossier-replication
  description: Replace biological triplicates with triplicate experiments and state
    that independent culture derivation is unspecified. Preserve source-reported mean/SD
    without strengthening their replication basis.
  finding_ids:
  - replicate-independence
  target_ids:
  - cmmmech:yttrium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round8-y-yb-20261011.md
    role: maintained_curation_dossier
  acceptance_checks:
  - Compare revised dossier wording with primary Methods 4.3-4.4; no unsupported independence
    claim remains.
  - Verify record and sidecar bytes remain unchanged; do not invent an EDIT for a
    dossier-only correction.
  - Save a successor observation resolving the same stable issue key and exact predecessor
    occurrence with updated dossier hashes.
limitations:
- Y supplementary tables/figure were unavailable to the curator; primary main-text
  methods/results and author-manuscript figures were inspected, without claiming numerical
  blank recoveries or complete balances.
- No intracellular mechanism, identified retained phase, isolated-product yield or
  industrial deployment established.
- Correction and duplication searches are bounded; primary sources and fields outside
  this target are not certified by this review.
- Reviewer attempted the exact PMC supplementary ZIP path; HTTP 404 prevented acquisition,
  so no supplementary numerical inspection is claimed.
notes:
- No record, history or dossier edits performed by reviewer. Raw public authority
  rechecks are retained under /private/tmp/cmm-round8-y-yb-review; original primary
  artifacts remain under /private/tmp/cmm-round8-y-yb-evidence.
```
