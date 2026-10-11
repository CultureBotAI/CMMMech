# Independent adversarial scientific review of copper expansion record

- Review: 20261011T040915Z-copper-expansion-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:03:14Z
- Finished UTC: 2026-10-11T04:09:15Z
- Reviewer: Codex /root/cmm_curate_nickel (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The element identity, dated US criticality, and conditional laboratory copper-release mechanism are supported. Controls, strain scope, endpoint definition, assay fraction, contamination caveat and deployment limits remain explicit. No record corrections or actionable scientific findings are required within this reviewed scope.

## Scope And Provenance

All fields of the new copper record plus linked CREATE provenance, with fresh primary-source and identifier verification.

Selection: Named record assigned by the coordinating curator after its history was finalized.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 76cd81d310a6ccb4cf7bdebcc61be050d0863222.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:copper | data/records/copper.yaml | maintained | Copper |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Copper validation | passed | True | cmmmech:copper | One record checked; zero failures. |
| Canonical history validation | passed | True | cmmmech:copper | 22 histories checked; zero errors against the inspected base. |
| Nonempty corpus validation | passed | True | cmmmech:copper | 13 records checked; zero failures. |
| Completed batch checks | passed | True | cmmmech:copper | Lint, 307 tests passed, 3 skipped; 13 records and 22 histories validated without errors. This repeats the full check after the coordinating agent completed the recipe argument-preservation fix. |

## Scientific And Domain Assessments

### Material form and dated list membership

identity: supported. Targets: cmmmech:copper.

The element anchor, experimental ore substrate and authority commodity scope remain distinct. The asserted US final 2025 edition was checked directly.

### Strain scope, living biomass and pretreated ore

grounding: supported. Targets: cmmmech:copper.

Species identifiers are appropriate species anchors and source strain labels remain explicit. The mixture evidence does not establish each member as independently sufficient.

### Controls, units and interpretation of measured copper

evidence: supported. Targets: cmmmech:copper.

The result is a conditional laboratory release comparison, with inferred redox contribution and no unsupported product-isolation claim.

### Contradiction and transfer limits

scope: supported. Targets: cmmmech:copper.

The record preserves uncertain A-only contamination, unequal durations and conditional interpretation. A different later consortium result motivates follow-up rather than broad rejection or broad confirmation.

Mechanistic transcript and redox associations are kept distinct from experimentally proven causal genes. The primary publication purity wording is not promoted to a pure-mineral assertion. The record need not represent every later copper study to support this bounded observation.

### Working-tree state and CREATE session

provenance: supported. Targets: cmmmech:copper.

Exact byte hashes and the main-history base were captured before assessment. Inline history agrees with the linked canonical session and its actual actor/time; validation passed.

No scientific or provenance bytes were changed by this reviewer. The review covers uncommitted changes above 76cd81d310a6ccb4cf7bdebcc61be050d0863222, not an assertion of committed-byte provenance.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/copper.yaml; Whole record including inline CREATE and history_refs | supports | Inspected exact uncommitted bytes and linked actual codex/GPT-6 CREATE event at 2026-10-11T04:02:09Z. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:28694; Entry label, formula, charge, definition and element classification | supports | CHEBI:28694 identifies copper atom with symbol Cu and neutral charge; it is not a chalcopyrite, solution-ion, ore or commodity identifier. |
| us-2025 | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 List of Critical Minerals; 60-item summary and complete listing table, Copper row | supports | The US Interior/USGS final notice dated 7 November 2025, 90 FR 50494-50497, lists Copper. Commodity list membership is explicitly mapped to this element record; the table byproduct flag is not interpreted as membership. |
| taxon-a | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=33059&amp;mode=Info; Scientific name, rank, type material | supports | NCBITaxon:33059 is species Acidithiobacillus caldus; DSM 8584 is listed as type material. Species identity is not strain identity. |
| taxon-s | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=28034&amp;mode=Info; Scientific name, rank, type material | supports | NCBITaxon:28034 is species Sulfobacillus thermosulfidooxidans; DSM 9293 is listed as type material. |
| taxon-l | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=178606&amp;mode=Info; Scientific name, rank, type material | supports | NCBITaxon:178606 is species Leptospirillum ferriphilum; DSM 14647 is listed as type material. |
| primary | https://doi.org/10.3389/fmicb.2018.03059; Materials and Methods: Mineral, Bacterial Strains and Growth Conditions, Bioleaching Experiments; Results and Discussion: Bioleaching of Chalcopyrite Concentrate; conclusion | supports | Read the publisher full text and the Europe PMC XML. Methods and results support the recorded conditions, controls and conditional release comparison. The acid digest measures released dissolved plus precipitated copper; the record does not call it purified product. No raw transcriptome reanalysis or causal gene assignment was made. |
| figure-1 | https://www.frontiersin.org/files/Articles/421883/xml-images/fmicb-09-03059-g001.webp; Figure 1 panels A-C and caption; visual inspection of downloaded image | supports | The plotted total-release trajectories, AS ranking, varying durations and n=4 mean/SD caption agree with the text. Exact reported values were checked against the Results, not inferred by pixel digitization. |
| source-caveats | https://doi.org/10.3389/fmicb.2018.03059; Results and Discussion: Bioleaching of Chalcopyrite Concentrate, repeat AS experiment; Conclusion | partial | A. caldus-only late iron oxidation is attributed to probable contamination; the repeat AS experiment does not preserve a universal low-redox ceiling. The record qualifies outcomes to the initial comparison and does not generalize to all consortia or industrial deployment. |
| new-context | https://doi.org/10.1007/s40831-026-01540-w; Rios et al. 2026; abstract and Methods/Results opening sections | context_only | A newer primary study reports a benefit from adding L. ferriphilum to a different consortium under a longer experiment. This is a follow-up lead for testing transferability, not a refutation of the scoped 2018 observation. Only the abstract and relevant opening methods/results were assessed; full independent curation is pending. |
| literature-search | Web search and live publisher/authority pages; Correction/retraction and conflicting-result discovery | context_only | No correction or retraction notice appeared in the inspected bounded search results. A differing-context 2026 primary study was identified and passed to the coordinating curator. |
| local-dedup | data/; research/; reviews/; history/; gitignore-independent local exact identity and DOI search | supports | No second maintained copper identity record was found in the inspected tree; current dossier, receipt and history references were expected matches. |

## Limits And Additional Notes

- Supplement assets were not independently read: the publisher link resolved to an anchor and the public PMC download returned HTML. Main-text Methods/Results and Figure 1 independently support the curated quantities; no supplementary-only claim was accepted.
- Raw replicate values, AAS calibration and sequencing data were not reanalyzed. Published means/SD were checked against source text and plotted trends, not recomputed.
- Probable contamination of the A. caldus-only condition, varying experiment durations, conditional redox interpretation and lack of industrial deployment evidence remain source limitations explicitly retained in the record.
- The 2026 consortium paper is a screened follow-up lead, not a completed supplemental record curation or an exhaustive literature synthesis.
- Findings by severity: no blocker, major, minor or informational record defect identified. Corrections: none made. Verdict is limited to the named copper record and its captured bytes.
- An initial just check during the coordinating agent's deliberate regression-test red phase failed six recipe argument-preservation tests (301 passed, 3 skipped). The unrelated justfile fix was completed before the passing final batch check; copper scientific bytes remained unchanged.
- Evidence accessed_at records completion of this review verification interval (04:03:14-04:09:15 UTC), not a claim that every network request occurred in the same second.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040915Z-copper-expansion-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial scientific review of copper expansion record
started_at: '2026-10-11T04:03:14Z'
finished_at: '2026-10-11T04:09:15Z'
reviewer:
  identity: Codex /root/cmm_curate_nickel
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent authored copper. This reviewer curated nickel,
    did not edit copper or its history, and independently opened the primary article,
    authority and identifiers and inspected Figure 1.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The element identity, dated US criticality, and conditional laboratory copper-release
  mechanism are supported. Controls, strain scope, endpoint definition, assay fraction,
  contamination caveat and deployment limits remain explicit. No record corrections
  or actionable scientific findings are required within this reviewed scope.
source:
  git_revision: 76cd81d310a6ccb4cf7bdebcc61be050d0863222
  state: working_tree
  inputs:
  - path: data/records/copper.yaml
    sha256: 357e81e48e5a480359f485e380a26eecf8d5a125100f328d99b06c0dacaabbfc
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/copper/2026-10-11T040209Z-codex-558c98.yaml
    sha256: f53837b64ae6c21addafff734b117280869fa830a7cc4739feee4f7b2e2d483d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields of the new copper record plus linked CREATE provenance,
    with fresh primary-source and identifier verification.
  selection: Named record assigned by the coordinating curator after its history was
    finalized.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:copper
  exclusions:
  - target: Raw transcriptomics and uncurated supplementary measurements
    reason: No causal gene or supplementary-only quantitative claim is asserted by
      this record; no raw sequence reanalysis was performed.
targets:
- target_id: cmmmech:copper
  path: data/records/copper.yaml
  label: Copper
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper.yaml
    role: maintained scientific record
checks:
- check_id: record-validation
  name: Copper validation
  status: passed
  required: true
  summary: One record checked; zero failures.
  target_ids:
  - cmmmech:copper
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/copper.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history-validation
  name: Canonical history validation
  status: passed
  required: true
  summary: 22 histories checked; zero errors against the inspected base.
  target_ids:
  - cmmmech:copper
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base 76cd81d
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty-corpus
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: 13 records checked; zero failures.
  target_ids:
  - cmmmech:copper
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch-check
  name: Completed batch checks
  status: passed
  required: true
  summary: Lint, 307 tests passed, 3 skipped; 13 records and 22 histories validated
    without errors. This repeats the full check after the coordinating agent completed
    the recipe argument-preservation fix.
  target_ids:
  - cmmmech:copper
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/copper.yaml
  locator: Whole record including inline CREATE and history_refs
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: Inspected exact uncommitted bytes and linked actual codex/GPT-6 CREATE
    event at 2026-10-11T04:02:09Z.
  snapshot_sha256: 357e81e48e5a480359f485e380a26eecf8d5a125100f328d99b06c0dacaabbfc
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28694
  locator: Entry label, formula, charge, definition and element classification
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: CHEBI:28694 identifies copper atom with symbol Cu and neutral charge; it
    is not a chalcopyrite, solution-ion, ore or commodity identifier.
- evidence_id: us-2025
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 List of Critical Minerals; 60-item summary and complete listing
    table, Copper row
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: The US Interior/USGS final notice dated 7 November 2025, 90 FR 50494-50497,
    lists Copper. Commodity list membership is explicitly mapped to this element record;
    the table byproduct flag is not interpreted as membership.
- evidence_id: taxon-a
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=33059&mode=Info
  locator: Scientific name, rank, type material
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: NCBITaxon:33059 is species Acidithiobacillus caldus; DSM 8584 is listed
    as type material. Species identity is not strain identity.
- evidence_id: taxon-s
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=28034&mode=Info
  locator: Scientific name, rank, type material
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: NCBITaxon:28034 is species Sulfobacillus thermosulfidooxidans; DSM 9293
    is listed as type material.
- evidence_id: taxon-l
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=178606&mode=Info
  locator: Scientific name, rank, type material
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: NCBITaxon:178606 is species Leptospirillum ferriphilum; DSM 14647 is listed
    as type material.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2018.03059
  locator: 'Materials and Methods: Mineral, Bacterial Strains and Growth Conditions,
    Bioleaching Experiments; Results and Discussion: Bioleaching of Chalcopyrite Concentrate;
    conclusion'
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: Read the publisher full text and the Europe PMC XML. Methods and results
    support the recorded conditions, controls and conditional release comparison.
    The acid digest measures released dissolved plus precipitated copper; the record
    does not call it purified product. No raw transcriptome reanalysis or causal gene
    assignment was made.
  snapshot_sha256: 78bc2cc1d5990d5f151e3bb67114f5a850473a1f10eb92f7eca824c503a1039b
- evidence_id: figure-1
  kind: primary_source
  reference: https://www.frontiersin.org/files/Articles/421883/xml-images/fmicb-09-03059-g001.webp
  locator: Figure 1 panels A-C and caption; visual inspection of downloaded image
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: The plotted total-release trajectories, AS ranking, varying durations and
    n=4 mean/SD caption agree with the text. Exact reported values were checked against
    the Results, not inferred by pixel digitization.
  snapshot_sha256: 0fc7e157d352a02b07acd2dfdf0e6a650bebccd13e289564c5b5b7e4becf071b
- evidence_id: source-caveats
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2018.03059
  locator: 'Results and Discussion: Bioleaching of Chalcopyrite Concentrate, repeat
    AS experiment; Conclusion'
  accessed_at: '2026-10-11T04:09:15Z'
  support: partial
  summary: A. caldus-only late iron oxidation is attributed to probable contamination;
    the repeat AS experiment does not preserve a universal low-redox ceiling. The
    record qualifies outcomes to the initial comparison and does not generalize to
    all consortia or industrial deployment.
- evidence_id: new-context
  kind: primary_source
  reference: https://doi.org/10.1007/s40831-026-01540-w
  locator: Rios et al. 2026; abstract and Methods/Results opening sections
  accessed_at: '2026-10-11T04:09:15Z'
  support: context_only
  summary: A newer primary study reports a benefit from adding L. ferriphilum to a
    different consortium under a longer experiment. This is a follow-up lead for testing
    transferability, not a refutation of the scoped 2018 observation. Only the abstract
    and relevant opening methods/results were assessed; full independent curation
    is pending.
- evidence_id: literature-search
  kind: search
  reference: Web search and live publisher/authority pages
  locator: Correction/retraction and conflicting-result discovery
  accessed_at: '2026-10-11T04:09:15Z'
  support: context_only
  summary: No correction or retraction notice appeared in the inspected bounded search
    results. A differing-context 2026 primary study was identified and passed to the
    coordinating curator.
  search_scope: 'Queries: "10.3389/fmicb.2018.03059" correction retraction; "Sulfobacillus
    thermosulfidooxidans" chalcopyrite "Leptospirillum" "contrary". Search result
    set and returned primary pages only; no exhaustive database or citation-network
    claim. Supplement attempts: Frontiers Supplementary File 1 anchor returned main
    article; PMC Data_Sheet_1.PDF failed in web access and direct public download
    returned HTML instead of a PDF.'
- evidence_id: local-dedup
  kind: search
  reference: data/; research/; reviews/; history/
  locator: gitignore-independent local exact identity and DOI search
  accessed_at: '2026-10-11T04:09:15Z'
  support: supports
  summary: No second maintained copper identity record was found in the inspected
    tree; current dossier, receipt and history references were expected matches.
  search_scope: rg --no-ignore --hidden -n -i (cmmmech:copper|CHEBI:28694|2018.03059)
    data research reviews history; ignored and hidden files included within these
    directories; this is not a claim about files outside those boundaries.
assessments:
- assessment_id: identity-criticality
  area: identity
  topic: Material form and dated list membership
  outcome: supported
  summary: The element anchor, experimental ore substrate and authority commodity
    scope remain distinct. The asserted US final 2025 edition was checked directly.
  target_ids:
  - cmmmech:copper
  evidence_ids:
  - record
  - chebi
  - us-2025
  dimensions:
  - name: material-form
    value: element; copper atom
    definition: Root record identity, distinct from ionic analyte and chalcopyrite-bearing
      concentrate.
    evidence_ids:
    - chebi
    - record
  - name: criticality
    value: United States; Interior/USGS; Final 2025 List of Critical Minerals; 2025
    definition: Dated jurisdiction/list/edition asserted, without a timeless global
      criticality claim.
    evidence_ids:
    - us-2025
- assessment_id: organisms-substrate
  area: grounding
  topic: Strain scope, living biomass and pretreated ore
  outcome: supported
  summary: Species identifiers are appropriate species anchors and source strain labels
    remain explicit. The mixture evidence does not establish each member as independently
    sufficient.
  target_ids:
  - cmmmech:copper
  evidence_ids:
  - record
  - primary
  - taxon-a
  - taxon-s
  - taxon-l
  dimensions:
  - name: biomass
    value: Living cultures harvested from axenic continuous cultures
    definition: Biomass state used for inoculation.
    evidence_ids:
    - primary
  - name: organisms
    value: A. caldus DSM 8584; S. thermosulfidooxidans DSM 9293; L. ferriphilum DSM
      14647
    definition: Three source strains with species-level database anchors.
    evidence_ids:
    - primary
    - taxon-a
    - taxon-s
    - taxon-l
  - name: substrate
    value: Aitik chalcopyrite concentrate, 29.5% copper; 50-100 micrometre fraction
    definition: Experimental substrate rather than a claim that elemental copper was
      leached.
    evidence_ids:
    - primary
  - name: pretreatment
    value: EDTA/NaOH washing, repeated acetone wash, drying and heat treatment under
      nitrogen
    definition: Prepared material whose transfer to untreated ore is not established.
    evidence_ids:
    - primary
- assessment_id: mechanism-quantity
  area: evidence
  topic: Controls, units and interpretation of measured copper
  outcome: supported
  summary: The result is a conditional laboratory release comparison, with inferred
    redox contribution and no unsupported product-isolation claim.
  target_ids:
  - cmmmech:copper
  evidence_ids:
  - record
  - primary
  - figure-1
  - source-caveats
  dimensions:
  - name: conditions
    value: 100 mL MAC in 250 mL flasks; initial pH 1.8; 2% w/v solids; 10^7 cells/mL
      per species; 38 +/- 2 C; 120 rpm
    definition: Recorded experimental regime; endpoint is source-defined 14 days after
      oxidation onset, with variable total times.
    evidence_ids:
    - primary
  - name: controls
    value: All single/binary/ternary combinations and uninoculated controls; n=4
    definition: Comparison set rather than an assertion of equal starting total biomass
      across mixtures.
    evidence_ids:
    - primary
    - figure-1
  - name: outcome
    value: Initial AS comparison 14.2 +/- 0.3 mM released copper; sterile control
      2.4 +/- 0.3 mM at 15 days
    definition: Reported concentration with means and SD, not a fitted capacity or
      directly comparable fixed-time rate.
    evidence_ids:
    - primary
    - figure-1
  - name: assay
    value: Heated HCl slurry digestion followed by atomic absorption spectroscopy
    definition: Released dissolved plus precipitated copper fraction; no isolated
      recovery product.
    evidence_ids:
    - primary
  - name: deployment
    value: Laboratory flask experiment
    definition: Mine-derived material does not establish industrial deployment of
      this specific defined consortium.
    evidence_ids:
    - record
    - primary
- assessment_id: limits-conflicts
  area: scope
  topic: Contradiction and transfer limits
  outcome: supported
  summary: The record preserves uncertain A-only contamination, unequal durations
    and conditional interpretation. A different later consortium result motivates
    follow-up rather than broad rejection or broad confirmation.
  target_ids:
  - cmmmech:copper
  evidence_ids:
  - record
  - source-caveats
  - new-context
  details: Mechanistic transcript and redox associations are kept distinct from experimentally
    proven causal genes. The primary publication purity wording is not promoted to
    a pure-mineral assertion. The record need not represent every later copper study
    to support this bounded observation.
- assessment_id: provenance
  area: provenance
  topic: Working-tree state and CREATE session
  outcome: supported
  summary: Exact byte hashes and the main-history base were captured before assessment.
    Inline history agrees with the linked canonical session and its actual actor/time;
    validation passed.
  target_ids:
  - cmmmech:copper
  evidence_ids:
  - record
  details: No scientific or provenance bytes were changed by this reviewer. The review
    covers uncommitted changes above 76cd81d310a6ccb4cf7bdebcc61be050d0863222, not
    an assertion of committed-byte provenance.
findings: []
actions: []
limitations:
- 'Supplement assets were not independently read: the publisher link resolved to an
  anchor and the public PMC download returned HTML. Main-text Methods/Results and
  Figure 1 independently support the curated quantities; no supplementary-only claim
  was accepted.'
- Raw replicate values, AAS calibration and sequencing data were not reanalyzed. Published
  means/SD were checked against source text and plotted trends, not recomputed.
- Probable contamination of the A. caldus-only condition, varying experiment durations,
  conditional redox interpretation and lack of industrial deployment evidence remain
  source limitations explicitly retained in the record.
- The 2026 consortium paper is a screened follow-up lead, not a completed supplemental
  record curation or an exhaustive literature synthesis.
notes:
- 'Findings by severity: no blocker, major, minor or informational record defect identified.
  Corrections: none made. Verdict is limited to the named copper record and its captured
  bytes.'
- An initial just check during the coordinating agent's deliberate regression-test
  red phase failed six recipe argument-preservation tests (301 passed, 3 skipped).
  The unrelated justfile fix was completed before the passing final batch check; copper
  scientific bytes remained unchanged.
- Evidence accessed_at records completion of this review verification interval (04:03:14-04:09:15
  UTC), not a claim that every network request occurred in the same second.
links:
- research/ingests/expansion-copper-20261011.md
- research/ingests/expansion-copper-20261011-acquisition.json
tags:
- copper
- independent-scientific-review
- expansion-20261011
```
