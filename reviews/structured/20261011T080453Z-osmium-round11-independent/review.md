# Independent scientific review of osmium round11 record

- Review: 20261011T080453Z-osmium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:59:48Z
- Finished UTC: 2026-10-11T08:04:53Z
- Reviewer: Codex /root/cmm11_lu_tm_pm (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The elemental identity and explicit Australian platinum-group mapping are supported. Historical crude-extract hydrogen uptake is represented with author-inferred products, absent matched controls and no pure-metal-yield or deployment claim.

## Scope And Provenance

All scientific and provenance fields of this named frozen record, its linked source evidence and authority scope.

Selection: Assigned named record; no sampling. Other materials are excluded from this record verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:osmium | data/records/osmium.yaml | maintained | Osmium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:osmium | Reviewer executed, terminal exit 0; 3 records, 0 failed. |
| Full batch gate | passed | True | cmmmech:osmium | Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records and 83 histories valid. Root session 92015 terminal exit 0. |
| Required-record validation | passed | True | cmmmech:osmium | Final required-record validation passed 71 records, zero failed. Root session 93511 terminal exit 0. |
| Trusted-base history validation | passed | True | cmmmech:osmium | Final trusted-base history validation passed 83 histories, zero errors. Root session 88115 terminal exit 0. |

## Scientific And Domain Assessments

### Material identity, source evidence and bounded experimental interpretation

evidence: supported. Targets: cmmmech:osmium.

The elemental identity and explicit Australian platinum-group mapping are supported. Historical crude-extract hydrogen uptake is represented with author-inferred products, absent matched controls and no pure-metal-yield or deployment claim.

### Frozen inputs and actual curation events

provenance: supported. Targets: cmmmech:osmium.

Record CREATE sidecar actor codex/GPT-6/codex, timestamp and issue44 link agree with the later separate inline event. All inspected hashes remain unchanged. No scientific record or history changes by this reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/osmium.yaml; Entire frozen record, actual CREATE sidecar, shared dossier and inspected local field contract | supports | Successful shared inspect bound these uncommitted bytes before conclusions. This reviewer curated the separate Lu/Tm/Pm trio and made no changes to these targets or their source dossier. |
| identity | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30687; Fresh independent EBI OLS response: identifier, preferred label, charge, formula, obsolete status | supports | CHEBI:30687 resolves osmium atom with neutral element formula. This is not the experimental salt, oxide, mineral, commodity or resource. |
| primary | https://doi.org/10.1128/jb.84.4.647-658.1962; Complete primary scan experimental sections, Methods 648–649, Results 651–654, Discussion 655–656; rendered PDF pages 2,5,8 independently inspected for Methods and Tables 4–5 | supports | Table 4 reports separate OsO4/OsO2/Os(III)-chloride inputs and H2 uptake. The OsO4 arm supports a proposed osmate endpoint, not complete reduction to metal. Os(0) assignments in the other arms depend on stoichiometry and author interpretation; modern phase confirmation and causal controls are not reported. |
| search | /private/tmp/cmm-round11-ir-os-hf-review-web.json; Independent bounded web searches and scoped local review search | context_only | Exact DOI correction/retraction/control searches and strain lookup were inspected. The Hf affiliation erratum was checked in full; no additional applicable correction appeared in these first result sets. This is not an exhaustive absence claim. |
| criticality | https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list; Australia; DISR Critical Minerals List updated 20 February 2024, Table 1 PGE entry and footnote 16 | supports | Independent live official page explicitly lists Os among six platinum-group elements. This is a named group-member mapping, not an individual US designation or criticality of every Os compound. |
| validation | /private/tmp/cmm-round11-final-check.log; Full final batch, nonempty and trusted-base history logs; reviewer named validation | supports | Reviewer read final root gate logs and terminal receipts; own named validation exited 0 with 3 records checked and 0 failed. Structural validity is not proof of scientific truth. |

## Limits And Additional Notes

- Historical strain resolution, replicate counts, uncertainty and Os-specific matched controls are not supplied in the inspected paper.
- The OsO4 H2 uptake is substoichiometric; product assignments have no Os-specific phase spectroscopy/diffraction or isolated-product assay.
- Specific proteins and physiological necessity are not established. No modern taxonomy was inferred from the historical synonym.
- Independent web and local searches are bounded as stated. No author contact, exhaustive correction-registry search or raw experimental reproduction was performed.
- No corrective issue was manufactured: no actionable defect was established in these exact reviewed bytes. Limitations are explicitly retained in the record.
- All 69 raw/acquisition/render artifacts in the curator dossier were independently rehashed and matched. Raw literature remains outside Git. Some web-reader identifier routes failed; independent direct EBI OLS and NCBI requests succeeded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080453Z-osmium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of osmium round11 record
started_at: '2026-10-11T07:59:48Z'
finished_at: '2026-10-11T08:04:53Z'
reviewer:
  identity: Codex /root/cmm11_lu_tm_pm
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: I authored the separate Lu/Tm/Pm records and corrected Tm after
    its independent review. A different agent authored Ir/Os/Hf, their sidecars and
    dossier; I did not edit those inputs. After one failed inspect invocation named
    an incorrect history path, successful inspect captured unchanged frozen bytes
    before scientific judgment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The elemental identity and explicit Australian platinum-group mapping are
  supported. Historical crude-extract hydrogen uptake is represented with author-inferred
  products, absent matched controls and no pure-metal-yield or deployment claim.
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: .claude/skills/review-record/SKILL.md
    sha256: abe8f0aebf9540aaaf5d2e2c2b43a4b17b7d5963d04e084b65e1ada19f4eb6be
    role: context
  - path: data/records/osmium.yaml
    sha256: db219a825da6866d42a86debeeb8c9f2e615ddf7f7a178fcec74f9b55ef0b622
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/osmium/2026-10-11T075422Z-codex-a98024.yaml
    sha256: eeb1bd3d50e1d578f58b6e9a53c1171adf5020bb2389e99832f0260b00b2b182
    role: context
  - path: research/ingests/round11-ir-os-hf-20261011.json
    sha256: 4667921f018418a919a21f885dbfc6b3b2eed96fe596fd6e8aed9ac7ab42219d
    role: context
  - path: research/ingests/round11-ir-os-hf-20261011.md
    sha256: 11511aaacd1bb01590db2826dce966c058330570c1ea66b09296b817270e2bc5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
  - path: src/cmmmech/validation.py
    sha256: 510e7ed92887ea6e8c8e5828af378ffe0aa737772f8188ade6b42bde14bb5dfa
    role: context
targets:
- target_id: cmmmech:osmium
  path: data/records/osmium.yaml
  label: Osmium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/osmium.yaml
    role: Maintained scientific record
scope:
  description: All scientific and provenance fields of this named frozen record, its
    linked source evidence and authority scope.
  selection: Assigned named record; no sampling. Other materials are excluded from
    this record verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:osmium
checks:
- check_id: named
  name: Reviewer named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/iridium.yaml data/records/osmium.yaml data/records/hafnium.yaml
  status: passed
  required: true
  summary: Reviewer executed, terminal exit 0; 3 records, 0 failed.
  scope_note: /private/tmp/cmm-round11-ir-os-hf-review-validation.log
  target_ids:
  - cmmmech:osmium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: batch
  name: Full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records
    and 83 histories valid. Root session 92015 terminal exit 0.
  scope_note: /private/tmp/cmm-round11-final-check.log
  target_ids:
  - cmmmech:osmium
  exit_code: 0
  expected_exit_code: 0
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
  scope_note: /private/tmp/cmm-round11-final-validation.log
  target_ids:
  - cmmmech:osmium
  exit_code: 0
  expected_exit_code: 0
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
  scope_note: /private/tmp/cmm-round11-final-history.log
  target_ids:
  - cmmmech:osmium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/osmium.yaml
  locator: Entire frozen record, actual CREATE sidecar, shared dossier and inspected
    local field contract
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Successful shared inspect bound these uncommitted bytes before conclusions.
    This reviewer curated the separate Lu/Tm/Pm trio and made no changes to these
    targets or their source dossier.
  snapshot_sha256: db219a825da6866d42a86debeeb8c9f2e615ddf7f7a178fcec74f9b55ef0b622
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30687
  locator: 'Fresh independent EBI OLS response: identifier, preferred label, charge,
    formula, obsolete status'
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: CHEBI:30687 resolves osmium atom with neutral element formula. This is
    not the experimental salt, oxide, mineral, commodity or resource.
  snapshot_sha256: 1dff3f1a56dffcf350674aebbedcdb68313b4a921bbe4fb0dd57a2367635ffd4
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/jb.84.4.647-658.1962
  locator: Complete primary scan experimental sections, Methods 648–649, Results 651–654,
    Discussion 655–656; rendered PDF pages 2,5,8 independently inspected for Methods
    and Tables 4–5
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Table 4 reports separate OsO4/OsO2/Os(III)-chloride inputs and H2 uptake.
    The OsO4 arm supports a proposed osmate endpoint, not complete reduction to metal.
    Os(0) assignments in the other arms depend on stoichiometry and author interpretation;
    modern phase confirmation and causal controls are not reported.
  snapshot_sha256: e45d037c1c6dc49a069c23afd8175689cc37d153e6eedd76e5f8f0b699b99c8d
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round11-ir-os-hf-review-web.json
  locator: Independent bounded web searches and scoped local review search
  accessed_at: '2026-10-11T08:04:53Z'
  support: context_only
  summary: Exact DOI correction/retraction/control searches and strain lookup were
    inspected. The Hf affiliation erratum was checked in full; no additional applicable
    correction appeared in these first result sets. This is not an exhaustive absence
    claim.
  snapshot_sha256: 56d7e6e5051a12175ec102aeb6cb870b4b20d8641d3d14dd90f0c98ae8031745
  search_scope: 'Four queries: exact Ir DOI with correction retraction; exact Hf DOI
    with correction retraction hafnium; exact Os DOI with osmium controls; NIES-3638
    with Galdieria javensis. No date filters or exhaustive pagination. rg --no-ignore
    --hidden --follow searched target IDs, ChEBI IDs and accepted DOI strings in data/records,
    research, reviews, history and .claude; 55 matching lines were read. Raw dossier
    inventory included hidden files and all 69 hashes matched. No machine-wide or
    citation-network completeness claim.'
- evidence_id: criticality
  kind: authority
  reference: https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list
  locator: Australia; DISR Critical Minerals List updated 20 February 2024, Table
    1 PGE entry and footnote 16
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Independent live official page explicitly lists Os among six platinum-group
    elements. This is a named group-member mapping, not an individual US designation
    or criticality of every Os compound.
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round11-final-check.log
  locator: Full final batch, nonempty and trusted-base history logs; reviewer named
    validation
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Reviewer read final root gate logs and terminal receipts; own named validation
    exited 0 with 3 records checked and 0 failed. Structural validity is not proof
    of scientific truth.
  snapshot_sha256: c77a6c80e36a0fc706ea157d0a79dc84cabdd120f3952e93f950832cb3b881be
assessments:
- assessment_id: science
  area: evidence
  topic: Material identity, source evidence and bounded experimental interpretation
  outcome: supported
  summary: The elemental identity and explicit Australian platinum-group mapping are
    supported. Historical crude-extract hydrogen uptake is represented with author-inferred
    products, absent matched controls and no pure-metal-yield or deployment claim.
  target_ids:
  - cmmmech:osmium
  evidence_ids:
  - record
  - identity
  - primary
  - search
  - criticality
  - validation
  dimensions:
  - name: material-form
    value: Osmium element; CHEBI:30687
    definition: Neutral atom grounding distinct from assay materials.
    evidence_ids:
    - identity
  - name: criticality
    value: Australia; DISR Critical Minerals List updated 20 February 2024, Table
      1 PGE entry and footnote 16
    definition: Named jurisdiction/list/edition, with explicit group mapping where
      applicable.
    evidence_ids:
    - criticality
  - name: organism
    value: Historical Micrococcus lactilyticus; Veillonella alcalescens synonym in
      source
    definition: No strain/accession supplied or modern strain node inferred.
    evidence_ids:
    - primary
  - name: biomass-state
    value: Cell-free crude extract after washing, sonication and cold centrifugation
    definition: Not whole-cell growth or a purified hydrogenase assay.
    evidence_ids:
    - primary
  - name: conditions
    value: Warburg vessel, 30 C, oxygen-scrubbed H2; routine 2.2 mL, Tris pH 7, about
      30 mg protein
    definition: Assays end when gas uptake ceases; Os-specific elapsed time absent.
    evidence_ids:
    - primary
  - name: substrate-outcome
    value: OsO4 15.6/12.0; OsO2 12.7/25.0; Os(III) chloride 7.3/10.7 micromol substrate/H2
    definition: Amounts from Table 4, not isolated Os yield; suspended oxide differs
      from dissolved chloride.
    evidence_ids:
    - primary
  - name: controls
    value: No Os-specific no-extract, inactive-extract or no-H2 comparison reported
    definition: Other-metal controls do not establish Os-specific enzymatic necessity.
    evidence_ids:
    - primary
  - name: deployment
    value: Historical laboratory extract transformation
    definition: Physiological respiration, environmental prevalence and industrial
      recovery remain unestablished.
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Frozen inputs and actual curation events
  outcome: supported
  summary: Record CREATE sidecar actor codex/GPT-6/codex, timestamp and issue44 link
    agree with the later separate inline event. All inspected hashes remain unchanged.
    No scientific record or history changes by this reviewer.
  target_ids:
  - cmmmech:osmium
  evidence_ids:
  - record
  - validation
findings: []
actions: []
limitations:
- Historical strain resolution, replicate counts, uncertainty and Os-specific matched
  controls are not supplied in the inspected paper.
- The OsO4 H2 uptake is substoichiometric; product assignments have no Os-specific
  phase spectroscopy/diffraction or isolated-product assay.
- Specific proteins and physiological necessity are not established. No modern taxonomy
  was inferred from the historical synonym.
- Independent web and local searches are bounded as stated. No author contact, exhaustive
  correction-registry search or raw experimental reproduction was performed.
notes:
- 'No corrective issue was manufactured: no actionable defect was established in these
  exact reviewed bytes. Limitations are explicitly retained in the record.'
- All 69 raw/acquisition/render artifacts in the curator dossier were independently
  rehashed and matched. Raw literature remains outside Git. Some web-reader identifier
  routes failed; independent direct EBI OLS and NCBI requests succeeded.
```
