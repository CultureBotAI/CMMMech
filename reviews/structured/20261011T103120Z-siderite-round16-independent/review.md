# Independent scientific review of Siderite

- Review: 20261011T103120Z-siderite-round16-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T10:26:47.326134Z
- Finished UTC: 2026-10-11T10:31:20.991492Z
- Reviewer: Codex /root/round16_silicates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Species identity and narrowly scoped culture-associated formation are supported. Missing causal controls, unquantified mixed products and source pH disagreement are honestly retained. No actionable record finding identified in this exact reviewed state.

## Scope And Provenance

Full scientific and provenance review of one new maintained mineral record, including its exact CREATE sidecar. Related companion mineral shares the experiment but is reviewed in its own bundle.

Selection: Named round 16 new mineral assigned to an agent separate from its curator.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b714ce2bd8050d5e19ed9ca072460ba2b8154c3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:siderite | data/records/siderite.yaml | maintained | Siderite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named-record validation | passed | True | cmmmech:siderite | Reviewer terminal session 46514 exited0; log reports2 records,0 failed; exact target hashes are retained in named-receipt.json. |
| Root completed batch validation | passed | True | cmmmech:siderite | Root terminal receipt and complete batch log inspected;308 tests passed,3 skipped,128 records,144 histories. Exact reviewed target bytes remained unchanged. |
| Nonempty corpus validation | passed | True | cmmmech:siderite | Root terminal receipt and require log inspected;128 records,0 failed. This structural check does not prove scientific claims. |
| Append-only canonical history | passed | True | cmmmech:siderite | Root terminal history receipt inspected;144 histories,0 errors at trusted main base. Target CREATE sidecar and inline event independently read. |

## Scientific And Domain Assessments

### Mineral species, list scope and experimental feed/product distinction

identity: supported. Targets: cmmmech:siderite.

Siderite denotes ferrous carbonate, Fe(CO3); IMA species identity is separate from elements and commodity resources. The record transparently reuses the same 2015 mixed-phase experiment as its companion mineral and makes no criticality claim.

### Culture-associated mixed-phase precipitation and control boundaries

evidence: supported. Targets: cmmmech:siderite.

Current wording is scientifically defensible: complementary diffraction/microscopy supports mineral formation in the selected live culture; source uncertainties and absent causal isolations are explicit. The record does not adopt the article introduction incorrect siderite formula, claim Fe(III) reduction, assign every Fe(II) decrease to this phase, or claim deployment.

### Exact current target and distinct CREATE history

provenance: supported. Targets: cmmmech:siderite.

Maintained record, linked sidecar and inline event identify the actual new record and GPT-6/codex author. Trusted-main base and input hashes preserve working-tree provenance. Reviewer was a separate agent and did not author or edit these records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/siderite.yaml; Entire current maintained record and linked CREATE sidecar history/records/siderite/2026-10-11T102441Z-codex-ba014b.yaml | supports | Independent reviewer read scientific fields, curator identity and actual CREATE provenance. Captured exact uncommitted bytes before assessment against trusted main revision; no target edits performed. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 PDF page 199 mineral row; pp 1-2 column definitions and distribution terms | supports | Independently read and visually inspected retained official PDF row: ferrous carbonate, Fe(CO3). Approved 1962 special-procedure entry is not an approval-number CURIE. No criticality designation is inherited. The source was acquired by the author earlier this round and rechecked here, not newly downloaded by the reviewer. |
| primary | https://doi.org/10.3389/fmicb.2015.01024; Complete primary PDF and XML; Methods/Results pp2-3; Figure 1 p4; Figure 2 p5; Figures 3-4 p6; Table 1 p7; Discussion pp3-5 | supports | Independently read full primary methods, results and discussion; visually inspected original rendered Figures 1-4 and Table 1. XRD labels both phases with vivianite dominant, while microscopy and EDX show corresponding cell/EPS-associated materials. Selected living CECT 8385/DSM 27266 anaerobic culture uses FeCl2 feed, initial pH 6, 30 C and up to 45-day observation. Uninoculated/nonviable controls reportedly lack precipitation; no Fe(III)-reduction result is transferred into this Fe(II) medium. |
| limits | https://doi.org/10.3389/fmicb.2015.01024; Culture Medium and crystal methods p2; Results p3; Discussion p4; PHREEQC Table 1 p7; full XML supplementary-material inventory | context_only | Record preserves Results pH~7.5 versus Discussion 7.8, missing replicate count/inoculum volume/nonviable preparation, and unspecified Fe(II) assay fraction. Model supersaturation is not observed abiotic precipitation. No pH-matched control or phosphatase/EPS perturbation proves a molecular mechanism. Mixed phases and bulk Fe(II) decline do not provide pure phase recovery yield or fertilizer performance. Full XML has no supplementary-material nodes; that does not certify no external supplement exists. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1427523&amp;mode=Info; Retained NCBI XML TaxId 1427523, ScientificName, Rank and OtherNames; live LPSN species page | supports | NCBI species is Tessaracoccus lapidicaptus; type-material aliases CECT 8385, DSM 27266 and IPBSL-7 agree with the current LPSN page and primary culture designation. Taxon CURIE remains species-level and is not represented as a strain identifier. Paper alternate Tessarococcus spelling is explicitly separated from accepted name. |
| search | /private/tmp/cmm-round16-vivianite-review/search.txt; Reviewer live correction and contrary-condition searches; ignored/hidden-inclusive local dedup log /private/tmp/cmm-round16-vivianite-review/dedup.txt | context_only | Three first-window unfiltered queries: exact DOI correction/retraction/erratum; Tessaracoccus lapidicaptus vivianite siderite abiotic control; Tessarococcus vivianite contrary phosphate carbonate. No affecting notice surfaced;2025 corrosion application remains a lead, not an accepted extension. Author metadata and mirror articles are one experiment, not independent confirmation. |
| gates | /private/tmp/cmm-round16-gate-receipts.json; Root terminal batch/require/history receipts and complete logs; reviewer named.log and named-receipt.json | supports | Required structural, nonempty corpus and append-only history checks completed successfully. Exact current target and sidecar hashes rechecked before save. These checks do not independently verify mineralogy. |

## Limits And Additional Notes

- Published mineral assignments are supported by presented diffraction and microscopy; raw patterns were not refitted and phase mass fractions remain unquantified.
- Live/nonviable/sterile contrasts lack matched-pH controls and do not isolate EPS, phosphatase or any specific metabolic cause.
- pH ~7.5 versus 7.8 and omitted replicate/inoculum/nonviable preparation details remain source limitations already represented by the record.
- The two mineral roots reuse one experiment and must not be counted as independent studies.
- Bounded searches and local inventories are not exhaustive; 2025 corrosion and other mineral experiments remain research leads.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T103120Z-siderite-round16-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Siderite
started_at: '2026-10-11T10:26:47.326134Z'
finished_at: '2026-10-11T10:31:20.991492Z'
reviewer:
  identity: Codex /root/round16_silicates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate /root/round16_vivianite agent authored target records
    and canonical histories. Reviewer independently read primary PDF/XML, figures,
    authority rows, taxonomy and current bytes; made no target edits. Shared project/worktree
    does not imply organizational independence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Species identity and narrowly scoped culture-associated formation are supported.
  Missing causal controls, unquantified mixed products and source pH disagreement
  are honestly retained. No actionable record finding identified in this exact reviewed
  state.
source:
  git_revision: b714ce2bd8050d5e19ed9ca072460ba2b8154c3b
  state: working_tree
  inputs:
  - path: data/records/siderite.yaml
    sha256: 664cc364a07cd83345b7d2b7cff2ac6a30403e6a93b3e7cb153418737a835ba0
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/siderite/2026-10-11T102441Z-codex-ba014b.yaml
    sha256: 6892d61075685f25e95c5d0350a3bd175eff38f88f8bbfc98b02d8a19c77ac33
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full scientific and provenance review of one new maintained mineral
    record, including its exact CREATE sidecar. Related companion mineral shares the
    experiment but is reviewed in its own bundle.
  selection: Named round 16 new mineral assigned to an agent separate from its curator.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:siderite
  exclusions:
  - target: Other corpus records, raw crystallographic refinement, new external replication
      and industrial processes
    reason: Out of the named record scope; published phase assignments and assay boundaries
      reviewed, not remeasured.
targets:
- target_id: cmmmech:siderite
  path: data/records/siderite.yaml
  label: Siderite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/siderite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Reviewer named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/vivianite.yaml data/records/siderite.yaml
  status: passed
  required: true
  summary: Reviewer terminal session 46514 exited0; log reports2 records,0 failed;
    exact target hashes are retained in named-receipt.json.
  target_ids:
  - cmmmech:siderite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Root completed batch validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Root terminal receipt and complete batch log inspected;308 tests passed,3
    skipped,128 records,144 histories. Exact reviewed target bytes remained unchanged.
  target_ids:
  - cmmmech:siderite
  exit_code: 0
  expected_exit_code: 0
- check_id: require
  name: Nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Root terminal receipt and require log inspected;128 records,0 failed. This
    structural check does not prove scientific claims.
  target_ids:
  - cmmmech:siderite
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only canonical history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base b714ce2bd8050d5e19ed9ca072460ba2b8154c3b
  status: passed
  required: true
  summary: Root terminal history receipt inspected;144 histories,0 errors at trusted
    main base. Target CREATE sidecar and inline event independently read.
  target_ids:
  - cmmmech:siderite
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/siderite.yaml
  locator: Entire current maintained record and linked CREATE sidecar history/records/siderite/2026-10-11T102441Z-codex-ba014b.yaml
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: supports
  summary: Independent reviewer read scientific fields, curator identity and actual
    CREATE provenance. Captured exact uncommitted bytes before assessment against
    trusted main revision; no target edits performed.
  snapshot_sha256: 664cc364a07cd83345b7d2b7cff2ac6a30403e6a93b3e7cb153418737a835ba0
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 PDF page 199 mineral row; pp 1-2 column definitions and
    distribution terms
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: supports
  summary: 'Independently read and visually inspected retained official PDF row: ferrous
    carbonate, Fe(CO3). Approved 1962 special-procedure entry is not an approval-number
    CURIE. No criticality designation is inherited. The source was acquired by the
    author earlier this round and rechecked here, not newly downloaded by the reviewer.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2015.01024
  locator: Complete primary PDF and XML; Methods/Results pp2-3; Figure 1 p4; Figure
    2 p5; Figures 3-4 p6; Table 1 p7; Discussion pp3-5
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: supports
  summary: Independently read full primary methods, results and discussion; visually
    inspected original rendered Figures 1-4 and Table 1. XRD labels both phases with
    vivianite dominant, while microscopy and EDX show corresponding cell/EPS-associated
    materials. Selected living CECT 8385/DSM 27266 anaerobic culture uses FeCl2 feed,
    initial pH 6, 30 C and up to 45-day observation. Uninoculated/nonviable controls
    reportedly lack precipitation; no Fe(III)-reduction result is transferred into
    this Fe(II) medium.
  snapshot_sha256: 0a57eb35bc370ce8f86c830eb7255fe3c3df369160907a38838a05a32fd7c8ef
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2015.01024
  locator: Culture Medium and crystal methods p2; Results p3; Discussion p4; PHREEQC
    Table 1 p7; full XML supplementary-material inventory
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: context_only
  summary: Record preserves Results pH~7.5 versus Discussion 7.8, missing replicate
    count/inoculum volume/nonviable preparation, and unspecified Fe(II) assay fraction.
    Model supersaturation is not observed abiotic precipitation. No pH-matched control
    or phosphatase/EPS perturbation proves a molecular mechanism. Mixed phases and
    bulk Fe(II) decline do not provide pure phase recovery yield or fertilizer performance.
    Full XML has no supplementary-material nodes; that does not certify no external
    supplement exists.
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1427523&mode=Info
  locator: Retained NCBI XML TaxId 1427523, ScientificName, Rank and OtherNames; live
    LPSN species page
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: supports
  summary: NCBI species is Tessaracoccus lapidicaptus; type-material aliases CECT
    8385, DSM 27266 and IPBSL-7 agree with the current LPSN page and primary culture
    designation. Taxon CURIE remains species-level and is not represented as a strain
    identifier. Paper alternate Tessarococcus spelling is explicitly separated from
    accepted name.
  snapshot_sha256: 647667516d655891be991425a95f1161c94108c32e105edbc0f5620f428eea49
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round16-vivianite-review/search.txt
  locator: Reviewer live correction and contrary-condition searches; ignored/hidden-inclusive
    local dedup log /private/tmp/cmm-round16-vivianite-review/dedup.txt
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: context_only
  summary: 'Three first-window unfiltered queries: exact DOI correction/retraction/erratum;
    Tessaracoccus lapidicaptus vivianite siderite abiotic control; Tessarococcus vivianite
    contrary phosphate carbonate. No affecting notice surfaced;2025 corrosion application
    remains a lead, not an accepted extension. Author metadata and mirror articles
    are one experiment, not independent confirmation.'
  search_scope: 2026-10-11 web search, first returned results only without pagination
    or date filters. Local rg --no-ignore --hidden --follow over data/research/reviews/history/.claude
    and the named round16-vivianite-raw directory. Exact DOI occurs in both new mineral
    roots and their supporting reports; no machine-wide novelty or exhaustive literature
    claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round16-gate-receipts.json
  locator: Root terminal batch/require/history receipts and complete logs; reviewer
    named.log and named-receipt.json
  accessed_at: '2026-10-11T10:31:20.991492Z'
  support: supports
  summary: Required structural, nonempty corpus and append-only history checks completed
    successfully. Exact current target and sidecar hashes rechecked before save. These
    checks do not independently verify mineralogy.
  snapshot_sha256: 263a0f7e628e4fe4a4b77dd731b52a9f17ca7b155ecfef8f0913367d4057543b
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species, list scope and experimental feed/product distinction
  outcome: supported
  summary: Siderite denotes ferrous carbonate, Fe(CO3); IMA species identity is separate
    from elements and commodity resources. The record transparently reuses the same
    2015 mixed-phase experiment as its companion mineral and makes no criticality
    claim.
  target_ids:
  - cmmmech:siderite
  evidence_ids:
  - record
  - ima
  - primary
  - search
  dimensions:
  - name: material_form
    value: ferrous carbonate, Fe(CO3)
    definition: IMA mineral species; not elemental iron/phosphorus or a pure commercial
      recovery product.
    evidence_ids:
    - ima
    - record
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition designation inherited from constituent
      elements.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated mixed-phase precipitation and control boundaries
  outcome: supported
  summary: 'Current wording is scientifically defensible: complementary diffraction/microscopy
    supports mineral formation in the selected live culture; source uncertainties
    and absent causal isolations are explicit. The record does not adopt the article
    introduction incorrect siderite formula, claim Fe(III) reduction, assign every
    Fe(II) decrease to this phase, or claim deployment.'
  target_ids:
  - cmmmech:siderite
  evidence_ids:
  - record
  - primary
  - limits
  - taxon
  dimensions:
  - name: organism_biomass
    value: Living Tessaracoccus lapidicaptus CECT 8385 = DSM 27266 = IPBSL-7; species
      taxon 1427523
    definition: Reported experimental culture and authority alias linkage, not new
      independent strain authentication.
    evidence_ids:
    - primary
    - taxon
  - name: substrate_conditions
    value: Defined Fe(II) FE medium; pH 6 initially; anaerobic 30 C; observation up
      to 45 days
    definition: Laboratory culture conditions; experiment is not Fe(III)-reduction
      or industrial wastewater recovery.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Uninoculated and nonviable-cell controls; no reported precipitation or
      pH change
    definition: Published controls support conditional association; nonviable preparation
      and matched-pH causal separation remain unknown.
    evidence_ids:
    - primary
    - limits
  - name: outcome_scale
    value: Vivianite-dominant mixture with siderite; no quantified phase-specific
      isolated yield
    definition: Published phase assignment checked visually, without raw diffraction
      refitting or industrial extrapolation.
    evidence_ids:
    - primary
    - limits
- assessment_id: provenance
  area: provenance
  topic: Exact current target and distinct CREATE history
  outcome: supported
  summary: Maintained record, linked sidecar and inline event identify the actual
    new record and GPT-6/codex author. Trusted-main base and input hashes preserve
    working-tree provenance. Reviewer was a separate agent and did not author or edit
    these records.
  target_ids:
  - cmmmech:siderite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Published mineral assignments are supported by presented diffraction and microscopy;
  raw patterns were not refitted and phase mass fractions remain unquantified.
- Live/nonviable/sterile contrasts lack matched-pH controls and do not isolate EPS,
  phosphatase or any specific metabolic cause.
- pH ~7.5 versus 7.8 and omitted replicate/inoculum/nonviable preparation details
  remain source limitations already represented by the record.
- The two mineral roots reuse one experiment and must not be counted as independent
  studies.
- Bounded searches and local inventories are not exhaustive; 2025 corrosion and other
  mineral experiments remain research leads.
tags:
- round16
- independent
- scientific-review
- mineral
links:
- https://github.com/CultureBotAI/CMMMech/issues/63
```
