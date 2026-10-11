# Selenium independent adversarial scientific review

- Review: 20261011T044131Z-selenium-round3-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:38:30Z
- Finished UTC: 2026-10-11T04:41:31Z
- Reviewer: /root/cmm3_cadmium (Codex) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact selenium record supports a dated Australian designation and a bounded laboratory MR-1 transformation. Conditional mutant involvement, heterogeneous particle localization, analytical recovery limits and supplementary rendering limits are preserved. No actionable record defect was found.

## Scope And Provenance

All fields of one newly curated selenium record, attached CREATE history and primary evidence supporting its stated claims.

Selection: Assigned independent review of final history-attached selenium bytes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record validation | passed | True | cmmmech:selenium | Reviewer executed: 1 record checked; 0 failed. |
| Nonempty corpus validation | passed | True | cmmmech:selenium | Reviewer executed: 21 records checked; 0 failed. |
| History linkage and append-only validation | passed | True | cmmmech:selenium | Reviewer executed against the trusted base: 30 history records checked; 0 errors. |
| Batch local checks | passed | True | cmmmech:selenium | Parent executed and confirmed exit 0; reviewer inspected completed /private/tmp/cmm-round3-check.log: 307 tests passed, 3 skipped, 21 records and 30 histories valid. |
| Independent primary evidence and authority review | passed | True | cmmmech:selenium | Verified identity authorities, dated list, full primary text, Figures 2/4/5, supplement captions/methods, older counterevidence and bounded searches. Scope and remaining access limits are explicit. |

## Scientific And Domain Assessments

### Element, ion and strain boundaries

identity: supported. Targets: cmmmech:selenium.

Element and oxyanion remain distinct. The NCBI MR-1 strain entry is a correct identity anchor for the parent organism.

### Authority, jurisdiction, list and edition

grounding: supported. Targets: cmmmech:selenium.

Dated Australian criticality is supported without transfer to experimental salts or other countries.

### Biomass, substrate, conditions, controls, outcome and scale

evidence: supported. Targets: cmmmech:selenium.

The bounded transformation claim is supported; lower mutant rates do not establish exclusive necessity or direct purified-enzyme catalysis.

### Contradiction and measurement boundaries

consistency: supported. Targets: cmmmech:selenium.

The older localization/mutant observations are preserved with different conditions and data-not-shown limitations. Quantities remain qualified prose rather than incompatible mg/kg observation cells.

### History, primary-source acquisition and reviewed-byte scope

provenance: supported. Targets: cmmmech:selenium.

CREATE history is linked and valid; raw figure/supplement hashes match receipts; working changes are disclosed at the trusted base.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/selenium.yaml; Entire inspected record, all source references, inline event and sidecar link | supports | Inspected before scientific assessment at SHA256 52546c821cad3f8753e4673901e52d804d861e0b44757dcbdedf22b582cae8b3. Working-tree addition at trusted base; reviewer made no record changes. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:27568; Current label, formula and net charge | supports | CHEBI:27568 resolves selenium atom, Se and charge zero; it does not identify the experimental selenite oxyanion. |
| organism | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586&amp;mode=Info; Current name and rank | supports | NCBI211586 resolves Shewanella oneidensis MR-1, no rank; the parent strain is not conflated with a separate accession for each deletion mutant. |
| criticality | https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list; List-revision paragraph and Table 1 Selenium row | supports | The issuing department dates this list to 20 February 2024 and includes selenium. Australia's own row is used, not outdated foreign-comparison columns. |
| primary | https://doi.org/10.1038/srep03735; Retained EuropePMC li2014.xml; Results, Discussion, all Methods, Figures 1-6 captions and Table 1 | supports | Independently read full scientific text and metadata. Conditions, initial-window rates, analytical basis, mutant residual activity and absence of a demonstrated exclusive enzyme pathway match the bounded record. |
| figures | https://doi.org/10.1038/srep03735; Original publisher images nature-f2.jpg, nature-f4.jpg and nature-f5.jpg in /private/tmp/cmm-round3-selenium-evidence-20261011 | supports | Visually inspected mutant curves, later residual reduction, TEM, EDX and Se 3d XPS. Image hashes match the acquisition JSON. No digitization, spectral refitting, periplasm-only localization or phase purity is inferred. |
| supplement | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fsrep03735/MediaObjects/41598_2014_BFsrep03735_MOESM1_ESM.doc; S1/S2 captions and S4 Methods; reviewer reran textutil extraction on the original OLE document | supports | Autoclaved-cell comparison and BSA-equivalent Micro BCA protein assay are supported by extracted text. Embedded graph pixels remain unrendered; qualitative adsorption/no-growth claims are explicitly attributed to main Results rather than newly measured from those graphs. |
| counterevidence | https://doi.org/10.1128/AEM.71.9.5607-5609.2005; Publisher full main text, cellular-localization paragraphs, cymA paragraph and Figure 1 caption | supports | The older study describes external or attached deposits and retained mutant activity with data not shown. Its differing growth context is preserved and it is not made into a matched quantitative refutation. EDX is not accepted as oxidation-state proof. |
| history | history/records/selenium/2026-10-11T043727Z-codex-226369.yaml; Target, actual session metadata and CREATE event | supports | Correctly targets selenium and distinguishes the sidecar event from the inline creation event; no earlier authorship or independent review is invented. |
| batch_log | /private/tmp/cmm-round3-check.log; Completed final output | supports | Read successful parent-run checks: 307 passed, 3 skipped, 21 records valid, 30 histories valid. |
| search | 2026-10-11 live web and ignored-file-inclusive local searches; Returned first web result sets; data/research/history/reviews and cited retained sources | context_only | No affecting correction or retraction appeared in inspected results. Related review and hybrid-material studies were discovery leads, not additional proof for the curated mechanism. Local matches are the accepted target and linked handoffs, not another selenium root. |

## Limits And Additional Notes

- Supplementary graph pixels were not rendered, and the 2005 image pixels were not reassessed. The narrower accepted claims rely on read captions/methods and explicitly attributed main-text observations; no supplementary numerical values or new older-image analyses are accepted.
- Deletion phenotypes without complementation or purified enzyme assays do not establish unique terminal catalysis; later residual activity prevents an absolute necessity claim.
- The source assays do not demonstrate phase-pure isolated selenium, a recovered-product yield or industrial deployment. Protein measurements do not establish viability.
- The comparison study uses a different medium and growth context and reports its cymA result without displayed data; no matched effect estimate can be derived.
- Correction and counterevidence searches are bounded to the stated returned sets and local files, including ignored/hidden matches. No worldwide literature exhaustion is asserted.
- Review covers the exact captured bytes. Subsequent substantive edits need a successor review; publication and post-merge verification remain parent-owned.
- No corrective issue is proposed: observed scientific limitations are already explicit in the record, and no actionable defect was found.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T044131Z-selenium-round3-independent
kind: record
repository: CultureBotAI/CMMMech
title: Selenium independent adversarial scientific review
started_at: '2026-10-11T04:38:30Z'
finished_at: '2026-10-11T04:41:31Z'
reviewer:
  identity: /root/cmm3_cadmium (Codex)
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer did not author selenium record, history or dossier.
    Independently inspected the curator-acquired primary XML, figure pixels and supplement
    document, reopened authorities and the older primary paper, and ran bounded scientific
    searches.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact selenium record supports a dated Australian designation and a bounded
  laboratory MR-1 transformation. Conditional mutant involvement, heterogeneous particle
  localization, analytical recovery limits and supplementary rendering limits are
  preserved. No actionable record defect was found.
source:
  git_revision: 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da
  state: working_tree
  inputs:
  - path: data/records/selenium.yaml
    sha256: 52546c821cad3f8753e4673901e52d804d861e0b44757dcbdedf22b582cae8b3
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/selenium/2026-10-11T043727Z-codex-226369.yaml
    sha256: dd160061c00f8a43d55f96c69ca2fe7cee66e8164e54652ccec8fa11b78fcd1a
    role: context
  - path: research/ingests/round3-selenium-20261011.json
    sha256: 29df6b58a0fa38a1ac0653d42f3473f4e86e1f7cad45c3c607d462a2d33dec47
    role: context
  - path: research/ingests/round3-selenium-20261011.md
    sha256: 22c4cad28798c3b42eeffbd8ebe909bccead5f6776ca4f0b484fdddb122006b5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:selenium
  path: data/records/selenium.yaml
  label: Selenium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
scope:
  description: All fields of one newly curated selenium record, attached CREATE history
    and primary evidence supporting its stated claims.
  selection: Assigned independent review of final history-attached selenium bytes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:selenium
  exclusions:
  - target: Other selenium materials, experiments and industrial deployment
    reason: This is a record-level claim audit, not a whole-literature or complete
      material frontier review.
  - target: Supplementary graph pixels and new analysis of older microscopy pixels
    reason: Legacy supplement graph rendering was not available. The accepted record
      limits itself to primary main-text statements and read captions/methods; no
      supplementary numeric points or fresh 2005-image interpretations are asserted.
checks:
- check_id: record
  name: Single-record validation
  status: passed
  required: true
  summary: 'Reviewer executed: 1 record checked; 0 failed.'
  target_ids:
  - cmmmech:selenium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/selenium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: corpus
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: 'Reviewer executed: 21 records checked; 0 failed.'
  target_ids:
  - cmmmech:selenium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: History linkage and append-only validation
  status: passed
  required: true
  summary: 'Reviewer executed against the trusted base: 30 history records checked;
    0 errors.'
  target_ids:
  - cmmmech:selenium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base 5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Batch local checks
  status: passed
  required: true
  summary: 'Parent executed and confirmed exit 0; reviewer inspected completed /private/tmp/cmm-round3-check.log:
    307 tests passed, 3 skipped, 21 records and 30 histories valid.'
  target_ids:
  - cmmmech:selenium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_log
- check_id: science
  name: Independent primary evidence and authority review
  status: passed
  required: true
  summary: Verified identity authorities, dated list, full primary text, Figures 2/4/5,
    supplement captions/methods, older counterevidence and bounded searches. Scope
    and remaining access limits are explicit.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - identity
  - organism
  - criticality
  - primary
  - figures
  - supplement
  - counterevidence
  - search
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/selenium.yaml
  locator: Entire inspected record, all source references, inline event and sidecar
    link
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: Inspected before scientific assessment at SHA256 52546c821cad3f8753e4673901e52d804d861e0b44757dcbdedf22b582cae8b3.
    Working-tree addition at trusted base; reviewer made no record changes.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27568
  locator: Current label, formula and net charge
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: CHEBI:27568 resolves selenium atom, Se and charge zero; it does not identify
    the experimental selenite oxyanion.
- evidence_id: organism
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586&mode=Info
  locator: Current name and rank
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: NCBI211586 resolves Shewanella oneidensis MR-1, no rank; the parent strain
    is not conflated with a separate accession for each deletion mutant.
- evidence_id: criticality
  kind: authority
  reference: https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list
  locator: List-revision paragraph and Table 1 Selenium row
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: The issuing department dates this list to 20 February 2024 and includes
    selenium. Australia's own row is used, not outdated foreign-comparison columns.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1038/srep03735
  locator: Retained EuropePMC li2014.xml; Results, Discussion, all Methods, Figures
    1-6 captions and Table 1
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: Independently read full scientific text and metadata. Conditions, initial-window
    rates, analytical basis, mutant residual activity and absence of a demonstrated
    exclusive enzyme pathway match the bounded record.
  snapshot_sha256: 76de6506252b8883844bebcf649b069cb7cc49a0d9d77b9bc916c7b92219c3a2
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1038/srep03735
  locator: Original publisher images nature-f2.jpg, nature-f4.jpg and nature-f5.jpg
    in /private/tmp/cmm-round3-selenium-evidence-20261011
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: Visually inspected mutant curves, later residual reduction, TEM, EDX and
    Se 3d XPS. Image hashes match the acquisition JSON. No digitization, spectral
    refitting, periplasm-only localization or phase purity is inferred.
- evidence_id: supplement
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fsrep03735/MediaObjects/41598_2014_BFsrep03735_MOESM1_ESM.doc
  locator: S1/S2 captions and S4 Methods; reviewer reran textutil extraction on the
    original OLE document
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: Autoclaved-cell comparison and BSA-equivalent Micro BCA protein assay are
    supported by extracted text. Embedded graph pixels remain unrendered; qualitative
    adsorption/no-growth claims are explicitly attributed to main Results rather than
    newly measured from those graphs.
  snapshot_sha256: 8c9a1d5ef53cde5fd5b10523d583b849427004c364eeec988eef9b95e57dcca0
- evidence_id: counterevidence
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.71.9.5607-5609.2005
  locator: Publisher full main text, cellular-localization paragraphs, cymA paragraph
    and Figure 1 caption
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: The older study describes external or attached deposits and retained mutant
    activity with data not shown. Its differing growth context is preserved and it
    is not made into a matched quantitative refutation. EDX is not accepted as oxidation-state
    proof.
- evidence_id: history
  kind: record_content
  reference: history/records/selenium/2026-10-11T043727Z-codex-226369.yaml
  locator: Target, actual session metadata and CREATE event
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: Correctly targets selenium and distinguishes the sidecar event from the
    inline creation event; no earlier authorship or independent review is invented.
- evidence_id: batch_log
  kind: validation
  reference: /private/tmp/cmm-round3-check.log
  locator: Completed final output
  accessed_at: '2026-10-11T04:40:24Z'
  support: supports
  summary: 'Read successful parent-run checks: 307 passed, 3 skipped, 21 records valid,
    30 histories valid.'
- evidence_id: search
  kind: search
  reference: 2026-10-11 live web and ignored-file-inclusive local searches
  locator: Returned first web result sets; data/research/history/reviews and cited
    retained sources
  accessed_at: '2026-10-11T04:40:24Z'
  support: context_only
  summary: No affecting correction or retraction appeared in inspected results. Related
    review and hybrid-material studies were discovery leads, not additional proof
    for the curated mechanism. Local matches are the accepted target and linked handoffs,
    not another selenium root.
  search_scope: 'Exact web queries: "10.1038/srep03735" correction retraction; "selenite"
    "FccA" "CymA" contradictory mutant. First result sets only; no full pagination.
    Local rg --no-ignore --hidden across data, research, history and reviews for cmmmech:selenium,27568,srep03735,5607-5609.2005,
    including ignored/hidden files. Cited raw directories were inspected; no machine-wide
    or exhaustive literature absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element, ion and strain boundaries
  outcome: supported
  summary: Element and oxyanion remain distinct. The NCBI MR-1 strain entry is a correct
    identity anchor for the parent organism.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - record
  - identity
  - organism
- assessment_id: criticality
  area: grounding
  topic: Authority, jurisdiction, list and edition
  outcome: supported
  summary: Dated Australian criticality is supported without transfer to experimental
    salts or other countries.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - record
  - criticality
  dimensions:
  - name: criticality
    value: Australia; Department of Industry, Science and Resources Critical Minerals
      List; 20 February 2024
    definition: Specific authority and edition for the listed material mapped to selenium
      element.
    evidence_ids:
    - criticality
- assessment_id: mechanism
  area: evidence
  topic: Biomass, substrate, conditions, controls, outcome and scale
  outcome: supported
  summary: The bounded transformation claim is supported; lower mutant rates do not
    establish exclusive necessity or direct purified-enzyme catalysis.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - record
  - primary
  - figures
  - supplement
  dimensions:
  - name: biomass
    value: LB-grown, washed MR-1 cells; authors report no growth
    definition: Protein-based biomass decline is not a viable-cell count.
    evidence_ids:
    - primary
    - supplement
  - name: substrate_conditions
    value: 0.5 mM selenite,20 mM lactate;40 mL anaerobic mineral medium,OD6001.0,30
      C
    definition: The context preserves pretreatment and the separate fumarate competition
      condition; measured pH remains unknown.
    evidence_ids:
    - primary
  - name: controls_outcome
    value: WT/deletion comparisons, autoclaved-cell adsorption comparison; TEM/EDX/XPS
      and analytical selenium balance
    definition: Distinct methods support particle composition and reduction without
      an isolated product yield.
    evidence_ids:
    - primary
    - figures
    - supplement
  - name: scale
    value: Laboratory transformation
    definition: No industrial extraction, purification or deployment claim.
    evidence_ids:
    - record
    - primary
- assessment_id: uncertainty
  area: consistency
  topic: Contradiction and measurement boundaries
  outcome: supported
  summary: The older localization/mutant observations are preserved with different
    conditions and data-not-shown limitations. Quantities remain qualified prose rather
    than incompatible mg/kg observation cells.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - record
  - primary
  - counterevidence
- assessment_id: provenance
  area: provenance
  topic: History, primary-source acquisition and reviewed-byte scope
  outcome: supported
  summary: CREATE history is linked and valid; raw figure/supplement hashes match
    receipts; working changes are disclosed at the trusted base.
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - record
  - history
  - primary
  - supplement
  - batch_log
findings: []
actions: []
limitations:
- Supplementary graph pixels were not rendered, and the 2005 image pixels were not
  reassessed. The narrower accepted claims rely on read captions/methods and explicitly
  attributed main-text observations; no supplementary numerical values or new older-image
  analyses are accepted.
- Deletion phenotypes without complementation or purified enzyme assays do not establish
  unique terminal catalysis; later residual activity prevents an absolute necessity
  claim.
- The source assays do not demonstrate phase-pure isolated selenium, a recovered-product
  yield or industrial deployment. Protein measurements do not establish viability.
- The comparison study uses a different medium and growth context and reports its
  cymA result without displayed data; no matched effect estimate can be derived.
- Correction and counterevidence searches are bounded to the stated returned sets
  and local files, including ignored/hidden matches. No worldwide literature exhaustion
  is asserted.
- Review covers the exact captured bytes. Subsequent substantive edits need a successor
  review; publication and post-merge verification remain parent-owned.
notes:
- 'No corrective issue is proposed: observed scientific limitations are already explicit
  in the record, and no actionable defect was found.'
```
