# Independent scientific review of iridium round11 record

- Review: 20261011T080453Z-iridium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:59:48Z
- Finished UTC: 2026-10-11T08:04:53Z
- Reviewer: Codex /root/cmm11_lu_tm_pm (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Neutral element identity, dated US designation, current strain mapping and laboratory biomass sorption/desorption are supported. The record retains source contradictions and distinguishes solution depletion, elution, model fits and proposed ligands.

## Scope And Provenance

All scientific and provenance fields of this named frozen record, its linked source evidence and authority scope.

Selection: Assigned named record; no sampling. Other materials are excluded from this record verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:iridium | data/records/iridium.yaml | maintained | Iridium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:iridium | Reviewer executed, terminal exit 0; 3 records, 0 failed. |
| Full batch gate | passed | True | cmmmech:iridium | Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records and 83 histories valid. Root session 92015 terminal exit 0. |
| Required-record validation | passed | True | cmmmech:iridium | Final required-record validation passed 71 records, zero failed. Root session 93511 terminal exit 0. |
| Trusted-base history validation | passed | True | cmmmech:iridium | Final trusted-base history validation passed 83 histories, zero errors. Root session 88115 terminal exit 0. |

## Scientific And Domain Assessments

### Material identity, source evidence and bounded experimental interpretation

evidence: supported. Targets: cmmmech:iridium.

Neutral element identity, dated US designation, current strain mapping and laboratory biomass sorption/desorption are supported. The record retains source contradictions and distinguishes solution depletion, elution, model fits and proposed ligands.

### Frozen inputs and actual curation events

provenance: supported. Targets: cmmmech:iridium.

Record CREATE sidecar actor codex/GPT-6/codex, timestamp and issue44 link agree with the later separate inline event. All inspected hashes remain unchanged. No scientific record or history changes by this reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/iridium.yaml; Entire frozen record, actual CREATE sidecar, shared dossier and inspected local field contract | supports | Successful shared inspect bound these uncommitted bytes before conclusions. This reviewer curated the separate Lu/Tm/Pm trio and made no changes to these targets or their source dossier. |
| identity | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49666; Fresh independent EBI OLS response: identifier, preferred label, charge, formula, obsolete status | supports | CHEBI:49666 resolves iridium atom with neutral element formula. This is not the experimental salt, oxide, mineral, commodity or resource. |
| primary | https://doi.org/10.1039/D3RA01249B; Full main text, Methods 2.1–2.5, Results 3.1–3.2; Table 1 and Figures 1–7 independently read/viewed on PDF pages 2–5; complete eight-page supplement text and visual methods/Table S1/Table S2/Figure S3 | supports | No-adsorbent controls support inactive-biomass adsorption. Table 1 reports 98 +/- 7 percent HCl desorption and low nonzero thiourea desorption. Reuse acid strength differs between abstract and main text; mixed-feed bars differ from quoted Fe/Cd percentages. These conflicts are explicit in the record. |
| search | /private/tmp/cmm-round11-ir-os-hf-review-web.json; Independent bounded web searches and scoped local review search | context_only | Exact DOI correction/retraction/control searches and strain lookup were inspected. The Hf affiliation erratum was checked in full; no additional applicable correction appeared in these first result sets. This is not an exhaustive absence claim. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; United States; Department of the Interior/USGS Final 2025 List of Critical Minerals, 7 November 2025, 90 FR 50494–50497 | supports | Independent official notice explicitly names iridium on page 50496. Its Yes column concerns byproduct production. The record does not turn every experimental compound into a designated mineral. |
| supplement | https://doi.org/10.1039/D3RA01249B; Complete eight-page supplementary text; methods and Tables S1–S2 / Figure S3 visually checked | supports | Coefficient 1.3 represents Ir/Fe enrichment, not purity. XAFS supplemental loading is 200 mg/L, separate from main methods. The displayed Langmuir equation is defective and b rounds to 0.00; fitted capacity is properly not adopted. |
| taxonomy | https://mcc.nbrp.jp/strainList.do?strainId=3636&amp;strainNumberEn=NIES-3638; Fresh NIES strain mapping; independent fresh NCBI node 3569544 | supports | NIES links current Galdieria javensis, former G. sulphuraria and alias 074W to NIES-3638. NCBI independently resolves the current species, not a universal strain identifier. |
| validation | /private/tmp/cmm-round11-final-check.log; Full final batch, nonempty and trusted-base history logs; reviewer named validation | supports | Reviewer read final root gate logs and terminal receipts; own named validation exited 0 with 3 records checked and 0 failed. Structural validity is not proof of scientific truth. |

## Limits And Additional Notes

- The 4 versus 6 M reuse-acid discrepancy, mixed-feed text/bar disagreement and differing analytical loadings remain unresolved; no reconciled value is invented.
- No raw-data refitting, ligand perturbation experiment or demonstration of a unique cellular binding site. The printed isotherm equation and rounded coefficient prevent reliable independent reconstruction.
- Table 1 does not separately define replicate number or its uncertainty measure; main figure captions specify three replicate assays and SD.
- Independent web and local searches are bounded as stated. No author contact, exhaustive correction-registry search or raw experimental reproduction was performed.
- No corrective issue was manufactured: no actionable defect was established in these exact reviewed bytes. Limitations are explicitly retained in the record.
- All 69 raw/acquisition/render artifacts in the curator dossier were independently rehashed and matched. Raw literature remains outside Git. Some web-reader identifier routes failed; independent direct EBI OLS and NCBI requests succeeded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080453Z-iridium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of iridium round11 record
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
summary: Neutral element identity, dated US designation, current strain mapping and
  laboratory biomass sorption/desorption are supported. The record retains source
  contradictions and distinguishes solution depletion, elution, model fits and proposed
  ligands.
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: .claude/skills/review-record/SKILL.md
    sha256: abe8f0aebf9540aaaf5d2e2c2b43a4b17b7d5963d04e084b65e1ada19f4eb6be
    role: context
  - path: data/records/iridium.yaml
    sha256: c77604f4962321302cd6f63ffff86d19463f4769893744c428155c1f6e9cf24c
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/iridium/2026-10-11T075703Z-codex-5aade4.yaml
    sha256: f7196b893e65b64d3307086b9a7cb4b56843909a44333d6200773242d1234bfe
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
- target_id: cmmmech:iridium
  path: data/records/iridium.yaml
  label: Iridium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/iridium.yaml
    role: Maintained scientific record
scope:
  description: All scientific and provenance fields of this named frozen record, its
    linked source evidence and authority scope.
  selection: Assigned named record; no sampling. Other materials are excluded from
    this record verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:iridium
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
  - cmmmech:iridium
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
  - cmmmech:iridium
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
  - cmmmech:iridium
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
  - cmmmech:iridium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/iridium.yaml
  locator: Entire frozen record, actual CREATE sidecar, shared dossier and inspected
    local field contract
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Successful shared inspect bound these uncommitted bytes before conclusions.
    This reviewer curated the separate Lu/Tm/Pm trio and made no changes to these
    targets or their source dossier.
  snapshot_sha256: c77604f4962321302cd6f63ffff86d19463f4769893744c428155c1f6e9cf24c
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49666
  locator: 'Fresh independent EBI OLS response: identifier, preferred label, charge,
    formula, obsolete status'
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: CHEBI:49666 resolves iridium atom with neutral element formula. This is
    not the experimental salt, oxide, mineral, commodity or resource.
  snapshot_sha256: a04afb5ccfa1d76d6d784facd1dd41caed95cfe81d4859d33db199607e91adba
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1039/D3RA01249B
  locator: Full main text, Methods 2.1–2.5, Results 3.1–3.2; Table 1 and Figures 1–7
    independently read/viewed on PDF pages 2–5; complete eight-page supplement text
    and visual methods/Table S1/Table S2/Figure S3
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: No-adsorbent controls support inactive-biomass adsorption. Table 1 reports
    98 +/- 7 percent HCl desorption and low nonzero thiourea desorption. Reuse acid
    strength differs between abstract and main text; mixed-feed bars differ from quoted
    Fe/Cd percentages. These conflicts are explicit in the record.
  snapshot_sha256: e77269041b4e1eacaf08ab900d8c55505144f5575c025dc3f5ff88e462484a3b
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
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: United States; Department of the Interior/USGS Final 2025 List of Critical
    Minerals, 7 November 2025, 90 FR 50494–50497
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Independent official notice explicitly names iridium on page 50496. Its
    Yes column concerns byproduct production. The record does not turn every experimental
    compound into a designated mineral.
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.1039/D3RA01249B
  locator: Complete eight-page supplementary text; methods and Tables S1–S2 / Figure
    S3 visually checked
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Coefficient 1.3 represents Ir/Fe enrichment, not purity. XAFS supplemental
    loading is 200 mg/L, separate from main methods. The displayed Langmuir equation
    is defective and b rounds to 0.00; fitted capacity is properly not adopted.
  snapshot_sha256: f15f8158b514fb4d57cb45fd15eac39c7ec6457dbafd4f5f800996bf07207b30
- evidence_id: taxonomy
  kind: database
  reference: https://mcc.nbrp.jp/strainList.do?strainId=3636&strainNumberEn=NIES-3638
  locator: Fresh NIES strain mapping; independent fresh NCBI node 3569544
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: NIES links current Galdieria javensis, former G. sulphuraria and alias
    074W to NIES-3638. NCBI independently resolves the current species, not a universal
    strain identifier.
  snapshot_sha256: cfae3e4d32b1fb3611e50832153a3d833fb7f1bc537e1e93efcc22bb9741637c
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
  summary: Neutral element identity, dated US designation, current strain mapping
    and laboratory biomass sorption/desorption are supported. The record retains source
    contradictions and distinguishes solution depletion, elution, model fits and proposed
    ligands.
  target_ids:
  - cmmmech:iridium
  evidence_ids:
  - record
  - identity
  - primary
  - search
  - criticality
  - supplement
  - taxonomy
  - validation
  dimensions:
  - name: material-form
    value: Iridium element; CHEBI:49666
    definition: Neutral atom grounding distinct from assay materials.
    evidence_ids:
    - identity
  - name: criticality
    value: United States; Department of the Interior/USGS Final 2025 List of Critical
      Minerals, 7 November 2025, 90 FR 50494–50497
    definition: Named jurisdiction/list/edition, with explicit group mapping where
      applicable.
    evidence_ids:
    - criticality
  - name: organism
    value: Galdieria 074W / NIES-3638; now G. javensis, NCBITaxon:3569544 species
    definition: Historical paper name G. sulphuraria is retained as source usage;
      current strain mapping verified in collection.
    evidence_ids:
    - primary
    - taxonomy
  - name: biomass-state
    value: Lyophilized cells cultivated at 40 C, pH 2.5; synthetic H2IrCl6 feed
    definition: Inactive adsorbent, not living metabolism or ore.
    evidence_ids:
    - primary
  - name: conditions
    value: 20 mg/mL biomass, 1 mL; 25 C, 30 min; low-feed assays 10 mg/L Ir
    definition: High-loading imaging and separate XAFS/supplement preparations are
      not pooled.
    evidence_ids:
    - primary
    - supplement
  - name: controls
    value: No-adsorbent solutions; resin and activated-carbon comparators
    definition: ICP-MS solution depletion relative to no-adsorbent control; comparator
      adsorbents are not metabolic controls.
    evidence_ids:
    - primary
  - name: outcome
    value: Sorption followed by chemical elution; Ir/Fe coefficient 1.3
    definition: Desorption denominator is the adsorbed pool. Supplement defines coefficient
      as after/before metal ratio, not purity.
    evidence_ids:
    - primary
    - supplement
  - name: deployment
    value: Laboratory synthetic-acid solutions
    definition: No isolated Ir(0), waste-feed deployment or industrial operation.
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
  - cmmmech:iridium
  evidence_ids:
  - record
  - validation
findings: []
actions: []
limitations:
- The 4 versus 6 M reuse-acid discrepancy, mixed-feed text/bar disagreement and differing
  analytical loadings remain unresolved; no reconciled value is invented.
- No raw-data refitting, ligand perturbation experiment or demonstration of a unique
  cellular binding site. The printed isotherm equation and rounded coefficient prevent
  reliable independent reconstruction.
- Table 1 does not separately define replicate number or its uncertainty measure;
  main figure captions specify three replicate assays and SD.
- Independent web and local searches are bounded as stated. No author contact, exhaustive
  correction-registry search or raw experimental reproduction was performed.
notes:
- 'No corrective issue was manufactured: no actionable defect was established in these
  exact reviewed bytes. Limitations are explicitly retained in the record.'
- All 69 raw/acquisition/render artifacts in the curator dossier were independently
  rehashed and matched. Raw literature remains outside Git. Some web-reader identifier
  routes failed; independent direct EBI OLS and NCBI requests succeeded.
```
