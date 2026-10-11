# Independent scientific review: spent-hydrocracking-catalyst

- Review: 20261011T093443Z-spent-hydrocracking-catalyst-round14-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:28:57.274265Z
- Finished UTC: 2026-10-11T09:34:43Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supported scoped resource identity and qualified laboratory mechanism,with no actionable record defect in reviewed scope.

## Scope And Provenance

All scientific and provenance fields of one new resource record.

Selection: New round14 resource assigned independently; all fields reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-hydrocracking-catalyst | data/records/spent-hydrocracking-catalyst.yaml | maintained | Spent hydrocracking catalyst |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Five reviewed-resource validation | passed | True | cmmmech:spent-hydrocracking-catalyst | Root executed and observed terminal0:5 records,0failed. /private/tmp/cmm-round14-root-review/named-validation.log |
| Trusted-base canonical history | passed | True | cmmmech:spent-hydrocracking-catalyst | Root observed terminal0:134history records,0errors. /private/tmp/cmm-round14-history.log |
| Required corpus validation | passed | True | cmmmech:spent-hydrocracking-catalyst | Root observed terminal0:119records,0failed. /private/tmp/cmm-round14-require.log |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:spent-hydrocracking-catalyst | Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |

## Scientific And Domain Assessments

### Secondary-resource boundaries

identity: supported. Targets: cmmmech:spent-hydrocracking-catalyst.

Used hydrocracking catalyst from Thai refineries via NICS; distinct from FCC/hydrotreating classes. No constituent-element criticality is inherited. No unverified resource/mineral identifier or designation is invented.

### Organism,pretreatment,controls and outcome

evidence: supported. Targets: cmmmech:spent-hydrocracking-catalyst.

Thai soil isolate reported Aspergillus aculeatus; NCBITaxon:5053 species;NR_111412.1 refers to CBS172.66 reference. 600C6h decoking&lt;150um;9dayPDB30-35C150rpm;filtered/centrifuged,pH-adjusted,autoclaved;100mL,180min,nominal10%50C148rpm. Table7 Mo22.95+/-0.80% experimental versus24.55% predicted, normalized to incompletely digested feed. pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent conflicts,Al lackoffit. No experimental isolate accession,unique enzymatic proof or isolated product. Laboratory only.

### Immutable history and exact working state

provenance: supported. Targets: cmmmech:spent-hydrocracking-catalyst.

Independent root reviewer did not author this record; inspected target, native contract and actual CREATE sidecar before judging. Reused studies remain linked views, not independent replicates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/spent-hydrocracking-catalyst.yaml; All fields and linked CREATE sidecar | supports | Exact working bytes captured before assessment; native schema and docs checked; actual GPT-6/codex CREATE targets this record and issue56, with separate inline event. |
| primary | https://doi.org/10.48048/tis.2026.13063; Methods PDF3-5; Results6-12; Tables2-8; Figures1-4 | supports | Independently read retained original primary PDF acquired by curator this round. Used hydrocracking catalyst from Thai refineries via NICS; distinct from FCC/hydrotreating classes. 600C6h decoking&lt;150um;9dayPDB30-35C150rpm;filtered/centrifuged,pH-adjusted,autoclaved;100mL,180min,nominal10%50C148rpm. Table7 Mo22.95+/-0.80% experimental versus24.55% predicted, normalized to incompletely digested feed. pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent conflicts,Al lackoffit. No experimental isolate accession,unique enzymatic proof or isolated product. Laboratory only. |
| search | Local corpus and four exact DOI queries; data/records,history,research,reviews plus first web result page | context_only | Ignored-inclusive followed local search establishes bounded identity overlap and repeated-study context. Four DOI correction/retraction queries returned original publications and related leads; no applicable notice in that result window. No exhaustive clearance. |
| taxonomy | https://www.ncbi.nlm.nih.gov/taxonomy; NCBI XML ScientificName/Rank/OtherNames; RefSeq NR_111412.1 LOCUS,DEFINITION,source features when applicable | supports | Independently parsed retained NCBI original XML;442=G.oxydans,5053=A.aculeatus,75736=S.bombicola at species rank. Candida synonym and ATCC22214 type-material scope checked; RefSeq CBS172.66 is not experimental Thai isolate. No species identifier establishes strain provenance. |
| reference | https://www.ncbi.nlm.nih.gov/nuccore/NR_111412.1; DEFINITION and source strain/type qualifiers | supports | Original reference sequence explicitly CBS172.66 type material; independently read complete retained GenBank text. |

## Limits And Additional Notes

- pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent conflicts,Al lackoffit. No experimental isolate accession,unique enzymatic proof or isolated product. Laboratory only.
- Primary artifacts freshly acquired by curator were independently read by root; not claimed as independent root downloads. Visual checks: ReedPDF18/22;ParkPDF5/8;ashPDF2-5;hydroPDF6/8-11, with other relevant methods/results read as PDF text.
- Correction searches covered only listed exact-DOI queries and first returned results. Source weaknesses retained explicitly are not fabricated review issues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093443Z-spent-hydrocracking-catalyst-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent scientific review: spent-hydrocracking-catalyst'
started_at: '2026-10-11T09:28:57.274265Z'
finished_at: '2026-10-11T09:34:43Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate resource agent authored this target. Root independently
    inspected original full text, methods, tables and rendered figures, original taxonomy
    exports and record/history bytes. Root authored only a different magnet record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supported scoped resource identity and qualified laboratory mechanism,with
  no actionable record defect in reviewed scope.
source:
  git_revision: 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  state: working_tree
  inputs:
  - path: data/records/spent-hydrocracking-catalyst.yaml
    sha256: 8bb94dfd26a8e4ad935a3337314ca4d7b96dbb50f857d8ca7405140b7df82e95
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/spent-hydrocracking-catalyst/2026-10-11T092624Z-codex-4b894e.yaml
    sha256: 76936fd774aa49210934c1e07b826e8e917ab9c001759ab09e1a64169cdf043c
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific and provenance fields of one new resource record.
  selection: New round14 resource assigned independently; all fields reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-hydrocracking-catalyst
  exclusions:
  - target: Other corpus records and uncurated literature
    reason: Checked only for duplicate/scope context; no corpus-wide scientific clearance.
targets:
- target_id: cmmmech:spent-hydrocracking-catalyst
  path: data/records/spent-hydrocracking-catalyst.yaml
  label: Spent hydrocracking catalyst
  kind: maintained
  ownership_note: Maintained native CMMMech YAML; future corrections belong to this
    record, not saved reviews.
checks:
- check_id: named
  name: Five reviewed-resource validation
  command: uv run --locked cmmmech validate data/records/spent-fluid-catalytic-cracking-catalyst.yaml
    data/records/coal-fly-ash.yaml data/records/municipal-waste-incineration-ash.yaml
    data/records/sewage-sludge-incineration-ash.yaml data/records/spent-hydrocracking-catalyst.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
  summary: Root executed and observed terminal0:5 records,0failed. /private/tmp/cmm-round14-root-review/named-validation.log
- check_id: history
  name: Trusted-base canonical history
  command: uv run --locked cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root observed terminal0:134history records,0errors. /private/tmp/cmm-round14-history.log
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
- check_id: records
  name: Required corpus validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root observed terminal0:119records,0failed. /private/tmp/cmm-round14-require.log
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
- check_id: batch
  name: Native full batch checks before FCC wording correction
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories
    valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending;
    this gate covers other unchanged targets.
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/spent-hydrocracking-catalyst.yaml
  locator: All fields and linked CREATE sidecar
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Exact working bytes captured before assessment; native schema and docs
    checked; actual GPT-6/codex CREATE targets this record and issue56, with separate
    inline event.
  snapshot_sha256: 8bb94dfd26a8e4ad935a3337314ca4d7b96dbb50f857d8ca7405140b7df82e95
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.48048/tis.2026.13063
  locator: Methods PDF3-5; Results6-12; Tables2-8; Figures1-4
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Independently read retained original primary PDF acquired by curator this
    round. Used hydrocracking catalyst from Thai refineries via NICS; distinct from
    FCC/hydrotreating classes. 600C6h decoking<150um;9dayPDB30-35C150rpm;filtered/centrifuged,pH-adjusted,autoclaved;100mL,180min,nominal10%50C148rpm.
    Table7 Mo22.95+/-0.80% experimental versus24.55% predicted, normalized to incompletely
    digested feed. pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent
    conflicts,Al lackoffit. No experimental isolate accession,unique enzymatic proof
    or isolated product. Laboratory only.
  snapshot_sha256: 5dceed6121da4c7b247e760ad90c0e7530d328ab9d313742247c62e19e310d94
- evidence_id: search
  kind: search
  reference: Local corpus and four exact DOI queries
  locator: data/records,history,research,reviews plus first web result page
  accessed_at: '2026-10-11T09:34:43Z'
  support: context_only
  summary: Ignored-inclusive followed local search establishes bounded identity overlap
    and repeated-study context. Four DOI correction/retraction queries returned original
    publications and related leads; no applicable notice in that result window. No
    exhaustive clearance.
  snapshot_sha256: db9cb5c3009827426a8eeac8ba9a3e3d7a5ce7f1a61204484aac61e7a32dc15b
  search_scope: rg --no-ignore --hidden --follow matching four DOIs and five resource
    slugs across data/records history research reviews. Web queries exact quoted DOI
    for each cited paper plus correction retraction; no domain/date filters or pagination.
    Sources were independently read, not inferred from snippets.
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/taxonomy
  locator: NCBI XML ScientificName/Rank/OtherNames; RefSeq NR_111412.1 LOCUS,DEFINITION,source
    features when applicable
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Independently parsed retained NCBI original XML;442=G.oxydans,5053=A.aculeatus,75736=S.bombicola
    at species rank. Candida synonym and ATCC22214 type-material scope checked; RefSeq
    CBS172.66 is not experimental Thai isolate. No species identifier establishes
    strain provenance.
  snapshot_sha256: e02f85740e0fc7ea43e95ff6615aa1e26f942c57954cd03a3307fb8e09a16aac
- evidence_id: reference
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/NR_111412.1
  locator: DEFINITION and source strain/type qualifiers
  accessed_at: '2026-10-11T09:34:43Z'
  support: supports
  summary: Original reference sequence explicitly CBS172.66 type material; independently
    read complete retained GenBank text.
  snapshot_sha256: c1a7c60378f41bee76e940abbea3cf51593cc9b7be58031279ffaf6d44e1db2e
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary-resource boundaries
  outcome: supported
  summary: Used hydrocracking catalyst from Thai refineries via NICS; distinct from
    FCC/hydrotreating classes. No constituent-element criticality is inherited. No
    unverified resource/mineral identifier or designation is invented.
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
  evidence_ids:
  - target
  - primary
  dimensions:
  - name: material_form
    value: secondary_resource
    definition: Industrial waste/feed class, not elemental or mineral identity.
    evidence_ids:
    - primary
    - target
  - name: criticality
    value: No designation asserted
    definition: No jurisdiction/list/edition transferred from constituents.
    evidence_ids:
    - primary
    - target
- assessment_id: mechanism
  area: evidence
  topic: Organism,pretreatment,controls and outcome
  outcome: supported
  summary: Thai soil isolate reported Aspergillus aculeatus; NCBITaxon:5053 species;NR_111412.1
    refers to CBS172.66 reference. 600C6h decoking<150um;9dayPDB30-35C150rpm;filtered/centrifuged,pH-adjusted,autoclaved;100mL,180min,nominal10%50C148rpm.
    Table7 Mo22.95+/-0.80% experimental versus24.55% predicted, normalized to incompletely
    digested feed. pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent
    conflicts,Al lackoffit. No experimental isolate accession,unique enzymatic proof
    or isolated product. Laboratory only.
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
  evidence_ids:
  - target
  - primary
  dimensions:
  - name: organism
    value: Thai soil isolate reported Aspergillus aculeatus; NCBITaxon:5053 species;NR_111412.1
      refers to CBS172.66 reference
    definition: Taxon,experimentalstrain or mixedcommunity scope.
    evidence_ids:
    - primary
    - target
  - name: conditions
    value: 600C6h decoking<150um;9dayPDB30-35C150rpm;filtered/centrifuged,pH-adjusted,autoclaved;100mL,180min,nominal10%50C148rpm
    definition: Selected laboratory assay and prior preparation.
    evidence_ids:
    - primary
    - target
  - name: outcome
    value: Table7 Mo22.95+/-0.80% experimental versus24.55% predicted, normalized
      to incompletely digested feed
    definition: Measured source endpoint and denominator, not isolated product.
    evidence_ids:
    - primary
    - target
  - name: deployment
    value: Laboratory only
    definition: Supplier industrial origin is not industrial biological deployment.
    evidence_ids:
    - primary
    - target
- assessment_id: provenance
  area: provenance
  topic: Immutable history and exact working state
  outcome: supported
  summary: Independent root reviewer did not author this record; inspected target,
    native contract and actual CREATE sidecar before judging. Reused studies remain
    linked views, not independent replicates.
  target_ids:
  - cmmmech:spent-hydrocracking-catalyst
  evidence_ids:
  - target
  - search
findings: []
actions: []
limitations:
- pH3.5 versus HCl adjustment to6.5,mg/L versus%w/v,controlrpm andpercent conflicts,Al
  lackoffit. No experimental isolate accession,unique enzymatic proof or isolated
  product. Laboratory only.
- 'Primary artifacts freshly acquired by curator were independently read by root;
  not claimed as independent root downloads. Visual checks: ReedPDF18/22;ParkPDF5/8;ashPDF2-5;hydroPDF6/8-11,
  with other relevant methods/results read as PDF text.'
- Correction searches covered only listed exact-DOI queries and first returned results.
  Source weaknesses retained explicitly are not fabricated review issues.
tags:
- round14
- independent
- scientific-review
```
