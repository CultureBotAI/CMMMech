# Independent adversarial review of cerium round-four record

- Review: 20261011T050034Z-cerium-round4-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:58:15Z
- Finished UTC: 2026-10-11T05:00:34Z
- Reviewer: Codex /root/cmm3_cadmium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded element identity, dated criticality and laboratory observation are supported. Preserved source limitations preclude broader causal, recovery or deployment claims; no actionable record defect was found.

## Scope And Provenance

All fields and linked new curation history of the named record.

Selection: Named new record after curator froze history-attached working bytes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c081a749cd63feafcc25414f5ad006d1f78f1e36.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cerium | data/records/cerium.yaml | maintained | Cerium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:cerium | Both named records checked; zero failures. Independently executed by this reviewer. |
| Completed batch checks | passed | True | cmmmech:cerium | Parent-executed final log inspected: 307 tests passed, 3 skipped in 47.17s; all checks passed, 27 records valid and 36 histories valid. |
| Nonempty corpus validation | passed | True | cmmmech:cerium | Parent reported separate terminal exit zero: 27 records checked, zero failures. |
| History content and trusted-base append-only validation | passed | True | cmmmech:cerium | Parent reported separate terminal exit zero against the declared trusted base: 36 histories checked, zero errors. |

## Scientific And Domain Assessments

### Element identity and dated criticality

identity: supported. Targets: cmmmech:cerium.

Element root, authoritative neutral-atom ID and dated material designation are supported. Experimental salts, ions, feed phases and products remain distinct.

### Upstream fungus and cell-free cerium stage

grounding: supported. Targets: cmmmech:cerium.

Microbial involvement correctly refers to preparation of the leachate; cells were removed before the cerium reaction. Resin treatment, pH adjustment and filtration are material steps retained in the record.

### Solution removal and solid phase assignments

evidence: supported. Targets: cmmmech:cerium.

Reported &gt;99% Ce solution removal, residual 27.34 +/- 1.91 micromolar at 50 mM input and SEM basis agree with Results/Figure 3. Arsenazo III at 658 nm is the correct analytical method. XRD/Table 2 and FTIR support phosphate hydrate at 20 mM and phosphate/oxalate phases at higher loading without equating fitted proportions to purity or recovery yield.

### Preserved limits and contrary explanations

scope: supported. Targets: cmmmech:cerium.

The record retains source weaknesses and plausible alternative chemical contributions without erasing the supported narrower observation. Qualified endpoint claims agree with the primary evidence.

### Exact revision, working state and distinct history

provenance: supported. Targets: cmmmech:cerium.

Inspection captured the trusted available base and final working-tree record, dossier, schema and history hashes before scientific assessment. Separate inline and sidecar events describe actual creation, not a fabricated earlier review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cerium.yaml; Whole record, inline CREATE and referenced canonical CREATE sidecar | supports | Inspected final working bytes after history attachment. Separate canonical and inline events describe the actual new record and Codex/GPT-6 authorship. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33369; Name, accession, formula and net charge | supports | Browser-source tool failed; an independent ordinary HTTPS retrieval succeeded, and extracted visible HTML text resolves cerium atom, formula Ce, charge zero. Receipt/raw outside Git at /private/tmp/cmm-round4-pce-independent/chebi-cerium-receipt.json. |
| authority | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 notice heading, 60-material list and Cerium table row | supports | Live official final notice, 7 November 2025, 90 FR 50494-50497, document 2025-19813, names cerium individually. Commodity-to-element scope is explicit and not extended to every compound. |
| organism | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&amp;mode=Info; Current name and no-rank entry | supports | Live entry resolves Aspergillus niger ATCC 1015; the source Methods identify the same strain. This is a strain-labelled no-rank anchor, not a species identifier presented as strain-specific. |
| primary | https://doi.org/10.1007/s00253-021-11721-0; All Methods subsections; Results on struvite and Ce; Tables 1-2; Discussion | supports | Independently read archived Europe PMC full XML and checked live primary PMC evidence. Published online 4 January 2022. Verified mixed feed, preparation, medium background phosphate, culture conditions, control descriptions, leachate pretreatment and analytical methods. Source is CC BY 4.0; no raw article redistributed. |
| figure3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/; Figure 3 original image and caption | supports | Independently visually inspected the downloaded primary image and compared with Results/caption; no pixel digitization, numerical error-bar reconstruction or raw-data reanalysis. |
| figure6 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/; Figure 6 original image and caption | supports | Independently visually inspected the downloaded primary image and compared with Results/caption; no pixel digitization, numerical error-bar reconstruction or raw-data reanalysis. |
| figure9 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/; Figure 9 original image and caption | supports | Independently visually inspected the downloaded primary image and compared with Results/caption; no pixel digitization, numerical error-bar reconstruction or raw-data reanalysis. |
| limits | https://doi.org/10.1007/s00253-021-11721-0; Methods, Figure 2 controls, Tables 1-2 and Discussion | partial | Background Na2HPO4 and struvite/dittmarite feed prevent mineral-specific phosphorus accounting. Pi assay method is not stated in the inspected full Methods; Ce colorimetry gives no explicit detection limit. Neither a pH-matched abiotic dissolution arm nor matched synthetic-chemistry/untreated-filtrate Ce controls are described. These limitations are retained in the relevant record. |
| search | Session web search and local data/research/reviews/history; Bounded correction/conflict and duplicate search | context_only | Returned results identify this paper and related/indexed material; no affecting correction or directly matched refutation was identified in those sets. Local results are the named records and current dossier/source assessment. No exhaustive absence or independent-replication claim is made. |

## Limits And Additional Notes

- No explicit Ce assay detection limit; apparent complete removal does not establish literal zero residual Ce.
- Background phosphate and chemical pretreatment prevent assigning all precipitation to struvite or demonstrating microbial necessity.
- Rietveld phase fits are not an independent absolute-purity measurement; high-temperature products are separate from the cell-free microbial-associated precipitation.
- No matched synthetic-chemistry control, REE-selectivity test, real-cerium-waste performance or industrial deployment is established.
- Figures 4-5 morphology and 7-8 thermal data were read as text/captions, not visually reanalyzed; neither supplies the accepted quantitative endpoint or microbial-mechanism claim.
- Inspected primary XML contains no supplementary-material node; no separate supplement or raw replicate dataset was inspected. Search coverage is bounded, not exhaustive.
- Findings by severity: zero blocker, major, minor or informational record defects. Corrections: none required. Scientific limitations are retained as limitations, not fabricated issue findings.
- Both new material records refer to different stages of one Kang 2022 study; they are not independent experimental replications.
- Access timestamps mark completion of the verification interval; all evidence was checked after exact input inspection. Parent executed the final batch/nonempty/history checks and confirmed terminal exit zero; reviewer inspected /private/tmp/cmm-round4-check.log. Named-record validation was executed independently by this reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T050034Z-cerium-round4-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial review of cerium round-four record
started_at: '2026-10-11T04:58:15Z'
finished_at: '2026-10-11T05:00:34Z'
reviewer:
  identity: Codex /root/cmm3_cadmium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Parent /root authored the phosphorus and cerium records/history;
    this reviewer did not edit them and independently read primary evidence, visually
    inspected the relevant figures and verified identifiers/authorities.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded element identity, dated criticality and laboratory observation
  are supported. Preserved source limitations preclude broader causal, recovery or
  deployment claims; no actionable record defect was found.
source:
  git_revision: c081a749cd63feafcc25414f5ad006d1f78f1e36
  state: working_tree
  inputs:
  - path: data/records/cerium.yaml
    sha256: 29f1c4494a293b80908cd8bb49cdbcde3deaabf58b3999a093d2bcdb8c135cae
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/cerium/2026-10-11T045547Z-codex-ed2983.yaml
    sha256: a65d43c930529cc6db96fd7eb6d7e072006426ac46b00eeb4c57b8b24da8f5d0
    role: context
  - path: research/ingests/round4-phosphorus-cerium-20261011.json
    sha256: b14c57f2cd3f8aef9a29bda1d1b7172cb11471d3f1c0a5fba315d5b4451c6956
    role: context
  - path: research/ingests/round4-phosphorus-cerium-20261011.md
    sha256: 446f1d941072e563109e0ac4c2a4aedd1e470799d19fc84dde85f89e5c2348f7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields and linked new curation history of the named record.
  selection: Named new record after curator froze history-attached working bytes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cerium
  exclusions:
  - target: Raw-replicate reanalysis, morphology/thermal figure pixel audit and new
      independent experiments
    reason: Not needed for the bounded curated observation; no numerical claims are
      imported from unaudited morphology/thermal panels.
targets:
- target_id: cmmmech:cerium
  path: data/records/cerium.yaml
  label: Cerium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerium.yaml
    role: maintained scientific record
checks:
- check_id: named-records
  name: Named-record validation
  status: passed
  required: true
  summary: Both named records checked; zero failures. Independently executed by this
    reviewer.
  target_ids:
  - cmmmech:cerium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/phosphorus.yaml data/records/cerium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: batch-check
  name: Completed batch checks
  status: passed
  required: true
  summary: 'Parent-executed final log inspected: 307 tests passed, 3 skipped in 47.17s;
    all checks passed, 27 records valid and 36 histories valid.'
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:cerium
- check_id: nonempty-corpus
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: 'Parent reported separate terminal exit zero: 27 records checked, zero
    failures.'
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:cerium
- check_id: history-check
  name: History content and trusted-base append-only validation
  status: passed
  required: true
  summary: 'Parent reported separate terminal exit zero against the declared trusted
    base: 36 histories checked, zero errors.'
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base c081a749cd63feafcc25414f5ad006d1f78f1e36
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:cerium
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cerium.yaml
  locator: Whole record, inline CREATE and referenced canonical CREATE sidecar
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Inspected final working bytes after history attachment. Separate canonical
    and inline events describe the actual new record and Codex/GPT-6 authorship.
  snapshot_sha256: 29f1c4494a293b80908cd8bb49cdbcde3deaabf58b3999a093d2bcdb8c135cae
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33369
  locator: Name, accession, formula and net charge
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Browser-source tool failed; an independent ordinary HTTPS retrieval succeeded,
    and extracted visible HTML text resolves cerium atom, formula Ce, charge zero.
    Receipt/raw outside Git at /private/tmp/cmm-round4-pce-independent/chebi-cerium-receipt.json.
  snapshot_sha256: 132749c13b8ce40eaf69531d0301832c2df3af07d630e2c15662dbe8d55c7a03
- evidence_id: authority
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 notice heading, 60-material list and Cerium table row
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Live official final notice, 7 November 2025, 90 FR 50494-50497, document
    2025-19813, names cerium individually. Commodity-to-element scope is explicit
    and not extended to every compound.
- evidence_id: organism
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&mode=Info
  locator: Current name and no-rank entry
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Live entry resolves Aspergillus niger ATCC 1015; the source Methods identify
    the same strain. This is a strain-labelled no-rank anchor, not a species identifier
    presented as strain-specific.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-021-11721-0
  locator: All Methods subsections; Results on struvite and Ce; Tables 1-2; Discussion
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Independently read archived Europe PMC full XML and checked live primary
    PMC evidence. Published online 4 January 2022. Verified mixed feed, preparation,
    medium background phosphate, culture conditions, control descriptions, leachate
    pretreatment and analytical methods. Source is CC BY 4.0; no raw article redistributed.
  snapshot_sha256: de81edbc2854a8b9b5fae071ca74af0a2bd163c799b3d6786baba9b755ed6c83
- evidence_id: figure3
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/
  locator: Figure 3 original image and caption
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Independently visually inspected the downloaded primary image and compared
    with Results/caption; no pixel digitization, numerical error-bar reconstruction
    or raw-data reanalysis.
  snapshot_sha256: 2292e8de3a951a6e7ccc0385d792e7869873e6fb1c93d9a5103e6a29260e8575
- evidence_id: figure6
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/
  locator: Figure 6 original image and caption
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Independently visually inspected the downloaded primary image and compared
    with Results/caption; no pixel digitization, numerical error-bar reconstruction
    or raw-data reanalysis.
  snapshot_sha256: 92adf013005a1d3b43944a17cf0da97d4c7dd0d5b70de5b21b342fc1fdd70b45
- evidence_id: figure9
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8763747/
  locator: Figure 9 original image and caption
  accessed_at: '2026-10-11T05:00:34Z'
  support: supports
  summary: Independently visually inspected the downloaded primary image and compared
    with Results/caption; no pixel digitization, numerical error-bar reconstruction
    or raw-data reanalysis.
  snapshot_sha256: 8c8cf6b37041502d80ca43045cb02d24a0b4d41c382bd77ef54b6c5a02f49a4b
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-021-11721-0
  locator: Methods, Figure 2 controls, Tables 1-2 and Discussion
  accessed_at: '2026-10-11T05:00:34Z'
  support: partial
  summary: Background Na2HPO4 and struvite/dittmarite feed prevent mineral-specific
    phosphorus accounting. Pi assay method is not stated in the inspected full Methods;
    Ce colorimetry gives no explicit detection limit. Neither a pH-matched abiotic
    dissolution arm nor matched synthetic-chemistry/untreated-filtrate Ce controls
    are described. These limitations are retained in the relevant record.
- evidence_id: search
  kind: search
  reference: Session web search and local data/research/reviews/history
  locator: Bounded correction/conflict and duplicate search
  accessed_at: '2026-10-11T05:00:34Z'
  support: context_only
  summary: Returned results identify this paper and related/indexed material; no affecting
    correction or directly matched refutation was identified in those sets. Local
    results are the named records and current dossier/source assessment. No exhaustive
    absence or independent-replication claim is made.
  search_scope: '2026-10-11 web queries: "10.1007/s00253-021-11721-0" correction retraction
    erratum; "Solubilization of struvite and biorecovery of cerium" control phosphate
    oxalate; "Kang" "struvite" "cerium" "contradict". First returned sets, no date/domain
    filters or subsequent pagination. Local rg --no-ignore --hidden -l -i CHEBI:(28659|33369)|cmmmech:(phosphorus|cerium)|11721-0|8763747
    data research reviews history; cited raw directory searched including hidden/ignored
    XML/HTML/JSON. Boundary excludes other home/temp trees.'
assessments:
- assessment_id: identity-scope
  area: identity
  topic: Element identity and dated criticality
  outcome: supported
  summary: Element root, authoritative neutral-atom ID and dated material designation
    are supported. Experimental salts, ions, feed phases and products remain distinct.
  target_ids:
  - cmmmech:cerium
  evidence_ids:
  - record
  - identity
  - authority
  dimensions:
  - name: material
    value: element
    definition: Root concept differs from experimental compounds and resource feed.
    evidence_ids:
    - record
    - identity
  - name: criticality
    value: United States; Interior/USGS final 2025 list; 7 November 2025
    definition: Jurisdiction, authority, named list and edition are explicit.
    evidence_ids:
    - authority
- assessment_id: grounding
  area: grounding
  topic: Upstream fungus and cell-free cerium stage
  outcome: supported
  summary: Microbial involvement correctly refers to preparation of the leachate;
    cells were removed before the cerium reaction. Resin treatment, pH adjustment
    and filtration are material steps retained in the record.
  target_ids:
  - cmmmech:cerium
  evidence_ids:
  - record
  - organism
  - primary
  dimensions:
  - name: organism
    value: Aspergillus niger ATCC 1015; NCBITaxon:380704, no rank
    definition: Verified experimental strain and database entry scope.
    evidence_ids:
    - organism
    - primary
  - name: feed
    value: Natural struvite/dittmarite fragments, Exeter Veolia site; pulverized;
      105 C for 48 h
    definition: Preconditioned mixed feed, not proven pure struvite.
    evidence_ids:
    - primary
  - name: culture
    value: 1% w/v feed, 200 mL modified Czapek-Dox, 1e6 spores/mL, 14 days, 25 C,
      125 rpm, darkness
    definition: Upstream laboratory culture; medium contains 1 g/L Na2HPO4.
    evidence_ids:
    - primary
  - name: biomass
    value: Cell-free cerium reaction following upstream living fungal culture
    definition: Does not assert fungal growth or cerium reduction at the tested Ce
      doses.
    evidence_ids:
    - primary
    - record
  - name: pretreatment
    value: 0.5 g H-form AG 50W-X8 per 5 mL, 24 h; 4 M NaOH to pH 7.5; 0.25 micrometer
      filtration
    definition: Chemical conditioning between fungal leaching and cerium precipitation.
    evidence_ids:
    - primary
  - name: reaction
    value: 5/20/40/50 mM Ce3+ as CeCl3, 10 mL, 24 h, room-temperature roller, triplicate
    definition: Synthetic soluble cerium challenge, not a real waste stream.
    evidence_ids:
    - primary
- assessment_id: outcome
  area: evidence
  topic: Solution removal and solid phase assignments
  outcome: supported
  summary: Reported >99% Ce solution removal, residual 27.34 +/- 1.91 micromolar at
    50 mM input and SEM basis agree with Results/Figure 3. Arsenazo III at 658 nm
    is the correct analytical method. XRD/Table 2 and FTIR support phosphate hydrate
    at 20 mM and phosphate/oxalate phases at higher loading without equating fitted
    proportions to purity or recovery yield.
  target_ids:
  - cmmmech:cerium
  evidence_ids:
  - primary
  - figure3
  - figure6
  - figure9
  - record
  dimensions:
  - name: measurement
    value: Arsenazo III supernatant Ce; XRD-Rietveld and FTIR of washed/dried solids
    definition: Solution removal and phase identification are separate endpoints.
    evidence_ids:
    - primary
    - figure3
    - figure6
    - figure9
  - name: controls
    value: No matched synthetic phosphate/oxalate or untreated-filtrate Ce arm described
      in inspected text
    definition: Prepared-leachate performance is supported; microbial necessity and
      REE selectivity are not.
    evidence_ids:
    - primary
    - limits
  - name: scale
    value: Laboratory 10 mL precipitation from CeCl3
    definition: No elemental cerium isolation or industrial waste recovery is demonstrated.
    evidence_ids:
    - primary
    - record
- assessment_id: uncertainty
  area: scope
  topic: Preserved limits and contrary explanations
  outcome: supported
  summary: The record retains source weaknesses and plausible alternative chemical
    contributions without erasing the supported narrower observation. Qualified endpoint
    claims agree with the primary evidence.
  target_ids:
  - cmmmech:cerium
  evidence_ids:
  - record
  - primary
  - limits
  - search
- assessment_id: provenance
  area: provenance
  topic: Exact revision, working state and distinct history
  outcome: supported
  summary: Inspection captured the trusted available base and final working-tree record,
    dossier, schema and history hashes before scientific assessment. Separate inline
    and sidecar events describe actual creation, not a fabricated earlier review.
  target_ids:
  - cmmmech:cerium
  evidence_ids:
  - record
findings: []
actions: []
limitations:
- No explicit Ce assay detection limit; apparent complete removal does not establish
  literal zero residual Ce.
- Background phosphate and chemical pretreatment prevent assigning all precipitation
  to struvite or demonstrating microbial necessity.
- Rietveld phase fits are not an independent absolute-purity measurement; high-temperature
  products are separate from the cell-free microbial-associated precipitation.
- No matched synthetic-chemistry control, REE-selectivity test, real-cerium-waste
  performance or industrial deployment is established.
- Figures 4-5 morphology and 7-8 thermal data were read as text/captions, not visually
  reanalyzed; neither supplies the accepted quantitative endpoint or microbial-mechanism
  claim.
- Inspected primary XML contains no supplementary-material node; no separate supplement
  or raw replicate dataset was inspected. Search coverage is bounded, not exhaustive.
notes:
- 'Findings by severity: zero blocker, major, minor or informational record defects.
  Corrections: none required. Scientific limitations are retained as limitations,
  not fabricated issue findings.'
- Both new material records refer to different stages of one Kang 2022 study; they
  are not independent experimental replications.
- Access timestamps mark completion of the verification interval; all evidence was
  checked after exact input inspection. Parent executed the final batch/nonempty/history
  checks and confirmed terminal exit zero; reviewer inspected /private/tmp/cmm-round4-check.log.
  Named-record validation was executed independently by this reviewer.
links:
- research/ingests/round4-phosphorus-cerium-20261011.md
- research/ingests/round4-phosphorus-cerium-20261011.json
tags:
- cerium
- round4
- independent-scientific-review
```
