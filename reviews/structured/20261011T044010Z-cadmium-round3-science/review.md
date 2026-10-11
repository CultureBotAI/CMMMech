# Independent adversarial scientific review of cadmium expansion record

- Review: 20261011T044010Z-cadmium-round3-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:37:13Z
- Finished UTC: 2026-10-11T04:40:10Z
- Reviewer: Codex /root/cmm3_chromium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Cadmium element identity, historical India committee designation and culture-associated CdS formation are supported at the captured file state. Species-level grounding, unresolved incubation details, unquantified abiotic contributions and sulfide-assay limits are explicit. No actionable record defect was identified.

## Scope And Provenance

All fields of the new cadmium record and linked canonical CREATE session; fresh independent primary/authority checks.

Selection: Named final record assigned by coordinating parent after curation/history completion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cadmium | data/records/cadmium.yaml | maintained | Cadmium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Cadmium record validation | passed | True | cmmmech:cadmium | One record checked; zero failed. |
| Append-only canonical history validation | passed | True | cmmmech:cadmium | 30 histories checked; zero errors against captured main-history base. |
| Nonempty corpus validation | passed | True | cmmmech:cadmium | 21 records checked; zero failed. |
| Completed batch checks | passed | True | cmmmech:cadmium | Coordinator executed the final batch check and confirmed terminal exit 0; reviewer independently read its completed log: 307 tests passed, 3 skipped, 21 records valid and 30 histories valid. |

## Scientific And Domain Assessments

### Element, species anchor and dated committee designation

identity: supported. Targets: cmmmech:cadmium.

The record preserves elemental identity and species-versus-strain scope. Official committee-list membership is correctly dated and explicitly distinguished from statutory designation.

### Culture-associated precipitation and assay interpretation

evidence: supported. Targets: cmmmech:cadmium.

Primary spectroscopy supports CdS-associated solids with residual unresolved Cd-O coordination. The approximate 1 mM endpoint derives from sulfide after pellet washing and is not a measured isolated cadmium-product yield.

### Controls, missing conditions and mechanistic limits

scope: supported. Targets: cmmmech:cadmium.

Narrow culture association is defensible despite incomplete isolation of biological versus abiotic contributions. No enzyme, mineral polymorph, phase purity, universal taxon phenotype or recovered yield is asserted.

### Actual CREATE history and review ownership

provenance: supported. Targets: cmmmech:cadmium.

Sidecar/inline events describe current work without retrospective authorship claims. Exact record/context hashes and trusted base were captured; reviewer made no target edits.

The record is uncommitted working-tree content above 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da. The source-hash attestation is not a claim that these bytes were already committed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cadmium.yaml; Complete YAML, inline CREATE event and history_refs | supports | Final working-tree bytes were read and captured before assessment. Linked history names codex/GPT-6 and actual CREATE at 04:34:43 UTC; inline and sidecar structures remain distinct. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:22977; Entry label, formula, charge and element classification | supports | CHEBI:22977 labels cadmium atom, Cd, net charge zero, with atomic-number 48 symbol synonym. This is not an ion, CdS or mineral-species identifier. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=575&amp;mode=Info; Current name, rank and homotypic synonym | supports | NCBITaxon:575 currently names Klebsiella planticola at species rank, with Raoultella planticola as a homotypic synonym. Record explicitly says this is not a verified Cd-1 strain identifier. |
| india-report | https://mines.gov.in/admin/storage/app/uploads/649d4212cceb01688027666.pdf; PDF pages 1, 11, 40; printed page 32 Chapter 9, final committee list item 4 | supports | Rehashed the previously acquired official 52-page PDF, extracted the specified pages and visually inspected the Chapter 9 list. Cadmium is item 4; cover dates report June 2023. Live PDF open failed during this review; this is local reinspection with provenance from the curation receipt, not a fresh download. |
| india-launch | https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1936083&amp;lang=2&amp;reg=48; Release 1936083 heading/date/body and report link | supports | Live official notice dated28June 2023 states the Ministry launched its expert-committee 30-material report and links the exact PDF. Record limits the designation to that report rather than a separate statutory schedule. |
| primary | https://journals.asm.org/doi/10.1128/AEM.66.7.3083-3087.2000; Growth-medium subsection; Transformation of cadmium to cadmium sulfide subsections(i)-(iii); Figures 2-3; conclusion and accession declarations | supports | Read the primary publisher text, including organism identification, medium, phase-dependent growth, XANES/EXAFS, methylene-blue assay, comparisons and limitations. It supports anaerobic Cd-1 culture-associated CdS, 5 mM spectroscopy samples and separate 5/10 mM thiosulfate-amended assay. No matched cell-free precipitation comparison or exact harvest elapsed time/temperature/volume is supplied for the characterized samples. |
| figure-2 | https://journals.asm.org/cms/10.1128/AEM.66.7.3083-3087.2000/asset/ed13c0fe-9dd1-4aa0-9d44-ec76a0763d06/assets/graphic/am0700108002.jpeg; Sulfur K-edge XANES Figure 2 and caption | supports | Independently visually inspected the acquired image: Cd-containing cells, CdS reference, cadmium-free biomass and fitted sum are distinguished. This is coordination/speciation evidence, not a cadmium recovery yield. |
| figure-3 | https://journals.asm.org/cms/10.1128/AEM.66.7.3083-3087.2000/asset/2ed99a1e-5c69-467a-bb73-5bba7f6e63d9/assets/graphic/am0700108003.jpeg; Cadmium K-edge EXAFS Figure 3a-b and caption | supports | Independently visually inspected acquired EXAFS curves, references and fit. Cd-S support does not exclude Cd-O coordination; the source says the oxygenated ligand identity remains unresolved. No crystallographic polymorph or phase-pure product is inferred. |
| search | Live web search and publisher page; Bounded correction/retraction and abiotic-counterevidence checks | context_only | No affecting correction/retraction or direct contrary matched experiment was identified in the returned relevant results. Publisher returned no Supplement label. These checks do not establish exhaustive absence. |
| local-search | data/ research/ reviews/ history/; Hidden and ignored identity/DOI search | supports | Only the new cadmium record represents this root identity within the inspected maintained corpus; research proposals and current dossier/history references are expected matches. |
| batch-log | /private/tmp/cmm-round3-check.log; Completed final batch output; coordinator separately confirmed process exit 0 | supports | Read 307 passed, 3 skipped in 56.44 seconds; 21 records checked with zero failures and 30 histories with zero errors. Offline checks establish structural integrity, not scientific truth. |

## Limits And Additional Notes

- Missing matched cell-free precipitation controls, exact incubation temperature/time/volume, and incomplete cadmium mass balance remain explicit source limitations.
- The source species identification and live NCBI species anchor were checked; no new sequence analysis or exact Cd-1 accession verification was performed.
- Raw XANES/EXAFS data were not refitted. Visual/reference comparisons support the narrow source-derived assignment without proving a pure mineral polymorph.
- Official India PDF was rechecked from the previously acquired artifact after live PDF access failed; current legal status and alternative national lists were outside this dated claim.
- Searches were bounded first-result checks; no exhaustive correction, conflict or cadmium-literature saturation claim.
- Findings by severity: zero blocker, major, minor or informational defects. Corrections: none made; no curation action proposed.
- Evidence accessed_at marks completion of the verification interval beginning 04:37:13 UTC, not simultaneous network retrieval.
- PDF skill was applied read-only to the India report; no source PDF or publisher figure was committed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T044010Z-cadmium-round3-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial scientific review of cadmium expansion record
started_at: '2026-10-11T04:37:13Z'
finished_at: '2026-10-11T04:40:10Z'
reviewer:
  identity: Codex /root/cmm3_chromium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent curated cadmium. This reviewer curated chromium,
    did not edit cadmium or its history, and independently read the primary study,
    source figures, identities and criticality authority.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Cadmium element identity, historical India committee designation and culture-associated
  CdS formation are supported at the captured file state. Species-level grounding,
  unresolved incubation details, unquantified abiotic contributions and sulfide-assay
  limits are explicit. No actionable record defect was identified.
source:
  git_revision: 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da
  state: working_tree
  inputs:
  - path: data/records/cadmium.yaml
    sha256: d28086a01df3288beb905cbea3fdc9ebdce8e7b7ae9da9a750e66712ca54d0de
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/cadmium/2026-10-11T043443Z-codex-9ca538.yaml
    sha256: e2fcc2d3cb14023a15c04cd29819bcab931176ebf600778bbeb96da046fa8451
    role: context
  - path: research/ingests/round3-cadmium-20261011.json
    sha256: e7e488fa9435a170842d1a8b73231c2dc67df601e81b4a75dbc0a2cf46d1033e
    role: context
  - path: research/ingests/round3-cadmium-20261011.md
    sha256: bdfaee9143d87f7f1c12fecaccfa5663d7ff010fea8fc5c7c39a55ce12fc6df2
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields of the new cadmium record and linked canonical CREATE session;
    fresh independent primary/authority checks.
  selection: Named final record assigned by coordinating parent after curation/history
    completion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cadmium
  exclusions:
  - target: Uncurated cadmium mechanisms, raw XAS data and modern statutory designation
    reason: Not asserted in the target; no full-corpus scientific review, raw spectroscopy
      refit or current-law assessment is claimed.
targets:
- target_id: cmmmech:cadmium
  path: data/records/cadmium.yaml
  label: Cadmium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cadmium.yaml
    role: maintained_record
checks:
- check_id: record-validation
  name: Cadmium record validation
  status: passed
  required: true
  summary: One record checked; zero failed.
  target_ids:
  - cmmmech:cadmium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/cadmium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history-validation
  name: Append-only canonical history validation
  status: passed
  required: true
  summary: 30 histories checked; zero errors against captured main-history base.
  target_ids:
  - cmmmech:cadmium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty-corpus
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: 21 records checked; zero failed.
  target_ids:
  - cmmmech:cadmium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch-check
  name: Completed batch checks
  status: passed
  required: true
  summary: 'Coordinator executed the final batch check and confirmed terminal exit
    0; reviewer independently read its completed log: 307 tests passed, 3 skipped,
    21 records valid and 30 histories valid.'
  target_ids:
  - cmmmech:cadmium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cadmium.yaml
  locator: Complete YAML, inline CREATE event and history_refs
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Final working-tree bytes were read and captured before assessment. Linked
    history names codex/GPT-6 and actual CREATE at 04:34:43 UTC; inline and sidecar
    structures remain distinct.
  snapshot_sha256: d28086a01df3288beb905cbea3fdc9ebdce8e7b7ae9da9a750e66712ca54d0de
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:22977
  locator: Entry label, formula, charge and element classification
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: CHEBI:22977 labels cadmium atom, Cd, net charge zero, with atomic-number
    48 symbol synonym. This is not an ion, CdS or mineral-species identifier.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=575&mode=Info
  locator: Current name, rank and homotypic synonym
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: NCBITaxon:575 currently names Klebsiella planticola at species rank, with
    Raoultella planticola as a homotypic synonym. Record explicitly says this is not
    a verified Cd-1 strain identifier.
- evidence_id: india-report
  kind: authority
  reference: https://mines.gov.in/admin/storage/app/uploads/649d4212cceb01688027666.pdf
  locator: PDF pages 1, 11, 40; printed page 32 Chapter 9, final committee list item
    4
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Rehashed the previously acquired official 52-page PDF, extracted the specified
    pages and visually inspected the Chapter 9 list. Cadmium is item 4; cover dates
    report June 2023. Live PDF open failed during this review; this is local reinspection
    with provenance from the curation receipt, not a fresh download.
  snapshot_sha256: 462757cbb91ace35da6ac4a96ad84558a4b78598a8197c9edc53d17f9949bb44
- evidence_id: india-launch
  kind: authority
  reference: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1936083&lang=2&reg=48
  locator: Release 1936083 heading/date/body and report link
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Live official notice dated28June 2023 states the Ministry launched its
    expert-committee 30-material report and links the exact PDF. Record limits the
    designation to that report rather than a separate statutory schedule.
- evidence_id: primary
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/AEM.66.7.3083-3087.2000
  locator: Growth-medium subsection; Transformation of cadmium to cadmium sulfide
    subsections(i)-(iii); Figures 2-3; conclusion and accession declarations
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Read the primary publisher text, including organism identification, medium,
    phase-dependent growth, XANES/EXAFS, methylene-blue assay, comparisons and limitations.
    It supports anaerobic Cd-1 culture-associated CdS, 5 mM spectroscopy samples and
    separate 5/10 mM thiosulfate-amended assay. No matched cell-free precipitation
    comparison or exact harvest elapsed time/temperature/volume is supplied for the
    characterized samples.
- evidence_id: figure-2
  kind: primary_source
  reference: https://journals.asm.org/cms/10.1128/AEM.66.7.3083-3087.2000/asset/ed13c0fe-9dd1-4aa0-9d44-ec76a0763d06/assets/graphic/am0700108002.jpeg
  locator: Sulfur K-edge XANES Figure 2 and caption
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: 'Independently visually inspected the acquired image: Cd-containing cells,
    CdS reference, cadmium-free biomass and fitted sum are distinguished. This is
    coordination/speciation evidence, not a cadmium recovery yield.'
  snapshot_sha256: 41e144cff8adf9c7c3210b6ffb981beec9d77c6a1f417c76f69a3536d46ab9e4
- evidence_id: figure-3
  kind: primary_source
  reference: https://journals.asm.org/cms/10.1128/AEM.66.7.3083-3087.2000/asset/2ed99a1e-5c69-467a-bb73-5bba7f6e63d9/assets/graphic/am0700108003.jpeg
  locator: Cadmium K-edge EXAFS Figure 3a-b and caption
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Independently visually inspected acquired EXAFS curves, references and
    fit. Cd-S support does not exclude Cd-O coordination; the source says the oxygenated
    ligand identity remains unresolved. No crystallographic polymorph or phase-pure
    product is inferred.
  snapshot_sha256: 3286c5b3d760bc27aa546283b99e5a6fb3d32375569c2a3e64c7f3cdd30b3d65
- evidence_id: search
  kind: search
  reference: Live web search and publisher page
  locator: Bounded correction/retraction and abiotic-counterevidence checks
  accessed_at: '2026-10-11T04:38:37Z'
  support: context_only
  summary: No affecting correction/retraction or direct contrary matched experiment
    was identified in the returned relevant results. Publisher returned no Supplement
    label. These checks do not establish exhaustive absence.
  search_scope: 'Queries on 2026-10-11: "10.1128/AEM.66.7.3083-3087.2000" correction
    retraction; "Klebsiella planticola" "Cd-1" cadmium "abiotic". First returned result
    sets only, no recency filters or pagination. Main source control gaps assessed
    directly; returned reviews not used to establish mechanism.'
- evidence_id: local-search
  kind: search
  reference: data/ research/ reviews/ history/
  locator: Hidden and ignored identity/DOI search
  accessed_at: '2026-10-11T04:38:37Z'
  support: supports
  summary: Only the new cadmium record represents this root identity within the inspected
    maintained corpus; research proposals and current dossier/history references are
    expected matches.
  search_scope: rg --no-ignore --hidden -n cadmium|22977|3083-3087.2000|PMC92115 across
    data research reviews history YAML/Markdown/JSON. Hidden/ignored paths included;
    unrelated external directories not searched. Local figures and the cited India
    PDF were inspected separately.
- evidence_id: batch-log
  kind: validation
  reference: /private/tmp/cmm-round3-check.log
  locator: Completed final batch output; coordinator separately confirmed process
    exit 0
  accessed_at: '2026-10-11T04:40:10Z'
  support: supports
  summary: Read 307 passed, 3 skipped in 56.44 seconds; 21 records checked with zero
    failures and 30 histories with zero errors. Offline checks establish structural
    integrity, not scientific truth.
  snapshot_sha256: 19c7af320a5328a3fb8f1eb5b4686b97b273c521f3b2dac411479d450f1b8c77
assessments:
- assessment_id: identity-criticality
  area: identity
  topic: Element, species anchor and dated committee designation
  outcome: supported
  summary: The record preserves elemental identity and species-versus-strain scope.
    Official committee-list membership is correctly dated and explicitly distinguished
    from statutory designation.
  target_ids:
  - cmmmech:cadmium
  evidence_ids:
  - record
  - chebi
  - taxon
  - india-report
  - india-launch
  dimensions:
  - name: material-form
    value: Element Cd; experimental CdCl2 and CdS distinct
    definition: Root concept and experimental forms are not interchangeable.
    evidence_ids:
    - record
    - chebi
  - name: criticality
    value: India; Ministry of Mines; committee list of 30 Critical Minerals for India;
      June 2023
    definition: Historical committee edition and launch date, with no current-law
      assertion.
    evidence_ids:
    - india-report
    - india-launch
  - name: organism
    value: Klebsiella planticola Cd-1; NCBITaxon:575 species anchor
    definition: Source strain label is explicit; exact strain accession is not asserted.
    evidence_ids:
    - primary
    - taxon
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated precipitation and assay interpretation
  outcome: supported
  summary: Primary spectroscopy supports CdS-associated solids with residual unresolved
    Cd-O coordination. The approximate 1 mM endpoint derives from sulfide after pellet
    washing and is not a measured isolated cadmium-product yield.
  target_ids:
  - cmmmech:cadmium
  evidence_ids:
  - record
  - primary
  - figure-2
  - figure-3
  dimensions:
  - name: biomass
    value: Living anaerobic cultures; washed and freeze-dried late-stationary material
      for spectroscopy
    definition: Growth state differs from analytical sample preparation.
    evidence_ids:
    - primary
  - name: substrate-conditions
    value: Synthetic CdCl2, pyruvate/glucose and Trizma buffer initially around pH
      7.1; 5 mM Cd(II) spectroscopy samples; separate 5/10 mM thiosulfate assay
    definition: Unreported precipitation incubation temperature, harvest elapsed time
      and vessel volume remain unresolved rather than borrowed from isolation/growth
      tests.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Cd-free biomass and reference spectra; no matched cell-free precipitation
      comparison reported
    definition: Analytical comparison supports speciation, while missing abiotic controls
      limit causal attribution.
    evidence_ids:
    - primary
    - figure-2
    - figure-3
  - name: outcome
    value: Cd-S-associated solids; approximately 1 mM CdS inferred from sulfide assay
    definition: Qualified laboratory immobilization, not a complete cadmium mass balance.
    evidence_ids:
    - primary
    - record
  - name: deployment
    value: Laboratory cultures
    definition: Environmental isolate origin and proposed bioremediation do not establish
      industrial application.
    evidence_ids:
    - primary
    - record
- assessment_id: uncertainty
  area: scope
  topic: Controls, missing conditions and mechanistic limits
  outcome: supported
  summary: Narrow culture association is defensible despite incomplete isolation of
    biological versus abiotic contributions. No enzyme, mineral polymorph, phase purity,
    universal taxon phenotype or recovered yield is asserted.
  target_ids:
  - cmmmech:cadmium
  evidence_ids:
  - record
  - primary
  - figure-2
  - figure-3
  - search
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE history and review ownership
  outcome: supported
  summary: Sidecar/inline events describe current work without retrospective authorship
    claims. Exact record/context hashes and trusted base were captured; reviewer made
    no target edits.
  target_ids:
  - cmmmech:cadmium
  evidence_ids:
  - record
  - local-search
  - batch-log
  details: The record is uncommitted working-tree content above 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da.
    The source-hash attestation is not a claim that these bytes were already committed.
findings: []
actions: []
limitations:
- Missing matched cell-free precipitation controls, exact incubation temperature/time/volume,
  and incomplete cadmium mass balance remain explicit source limitations.
- The source species identification and live NCBI species anchor were checked; no
  new sequence analysis or exact Cd-1 accession verification was performed.
- Raw XANES/EXAFS data were not refitted. Visual/reference comparisons support the
  narrow source-derived assignment without proving a pure mineral polymorph.
- Official India PDF was rechecked from the previously acquired artifact after live
  PDF access failed; current legal status and alternative national lists were outside
  this dated claim.
- Searches were bounded first-result checks; no exhaustive correction, conflict or
  cadmium-literature saturation claim.
notes:
- 'Findings by severity: zero blocker, major, minor or informational defects. Corrections:
  none made; no curation action proposed.'
- Evidence accessed_at marks completion of the verification interval beginning 04:37:13
  UTC, not simultaneous network retrieval.
- PDF skill was applied read-only to the India report; no source PDF or publisher
  figure was committed.
links:
- research/ingests/round3-cadmium-20261011.md
- research/ingests/round3-cadmium-20261011.json
tags:
- cadmium
- independent-scientific-review
- round3-20261011
```
