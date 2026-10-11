# Independent scientific review of mixed Horzum oxidized-zinc ore

- Review: 20261011T174859Z-oxidized-zinc-ore-round29-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T17:43:52.833044Z
- Finished UTC: 2026-10-11T17:48:59.167108Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record supports a source-defined natural mixed ore and qualified culture-associated laboratory dissolution. It explicitly limits causal enhancement, strain identity, statistics and yield accounting. No corrective finding was identified in the frozen record.

## Scope And Provenance

Entire new record, all asserted scientific claims and linked CREATE history.

Selection: Independent review of the new round29 mixed oxidized-zinc-ore record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7629ab50846229c87987d7fa0ac12389212bb70f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:oxidized-zinc-ore | data/records/oxidized-zinc-ore.yaml | maintained | Oxidized-zinc ore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:oxidized-zinc-ore | Executed by this reviewer; terminal exit0,1record checked/0failed. |
| Final batch validation | passed | True | cmmmech:oxidized-zinc-ore | Actual root execution reached terminal exit0. Receipt/log hashes verified and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-batch.log |
| Final nonempty validation | passed | True | cmmmech:oxidized-zinc-ore | Actual root execution reached terminal exit0. Receipt/log hashes verified and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-nonempty.log |
| Final history validation | passed | True | cmmmech:oxidized-zinc-ore | Actual root execution reached terminal exit0. Receipt/log hashes verified and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-history.log |

## Scientific And Domain Assessments

### Natural mixed resource boundary

identity: supported. Targets: cmmmech:oxidized-zinc-ore.

Primary-resource scope, mineral-specific exclusions and absent inherited criticality are supported.

### Source culture and explicit species-name uncertainty

identity: supported. Targets: cmmmech:oxidized-zinc-ore.

The record retains the paper accession and authority conflict without false stock authentication.

### Qualified culture-associated aqueous dissolution

evidence: supported. Targets: cmmmech:oxidized-zinc-ore.

Conditions, pretreatment, control limits, reported endpoints and deployment scope are accurately bounded.

### Nulls, contradictory source reporting and alternative explanations

evidence: supported. Targets: cmmmech:oxidized-zinc-ore.

The record explicitly preserves Pb qualitative non-solubilization, replication conflict, incomplete volume/mass accounting and unsupported molecular/phase claims.

Independent total sums of squares from nine printed Table3 outcomes: Zn1193.4561 and Fe845.7418, close to printed1193.55/845.68; printed S/N columns give80.1327/31.0182. This diagnostic does not repair unavailable replicates or certify significance. Unnormalized offset XRD and missing abiotic residue do not prove microbial phase destruction; absence of new peaks does not exclude precipitation.

### Actual curation and immutable exact-state review

provenance: supported. Targets: cmmmech:oxidized-zinc-ore.

Inline CREATE and canonical CREATE accurately describe this new curation; no prior authorship or completed review is fabricated.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/oxidized-zinc-ore.yaml; Entire frozen YAML and linked canonical CREATE history | supports | Canonical inspect captured the merged-main base and exact working bytes before maintained-claim assessment. |
| primary | https://dergipark.org.tr/en/download/article-file/5079644; Complete nine-page article, pp1067–1075; all four tables and seven figures; methods pp1068–1069 and conclusions pp1072–1073 | supports | Original full text and every original rendered page independently inspected. The material is a heterogeneous natural ore, and measurements concern acidified laboratory flasks with a source-named live culture. |
| controls | https://dergipark.org.tr/en/download/article-file/5079644; Methods pp1068–1069; Figures1–4 and Table3 | context_only | Numeric abiotic Zn/Fe release is not supplied. pH/redox controls, bulk cell counts and mixed-phase offset XRD do not establish ferric attack, microbial necessity or pure-smithsonite dissolution. Pb is qualitative without a detection limit. |
| quantitation | https://dergipark.org.tr/en/download/article-file/5079644; Equation2; Table1; Tables3–4; Figures5–7; /private/tmp/cmm-round29-zinc-independent-review/arithmetic.json | context_only | The mL/mg-per-L expression, serial withdrawals, unspecified feed assay basis, duplicate/triplicate conflict and absent raw replicates prevent independent mass reconciliation. Independent Table3 recomputation confirms Table4 total sums approximately match raw percentages rather than printed S/N cells. Derived contour values are not additional measurements. |
| publication | https://dergipark.org.tr/en/pub/dumf/article/1748240; Current official article metadata and acquired Crossref registration; paper front page | supports | Publisher identity confirms Demirci,2025,16(4),1067–1075 and DOI10.24012/dumf.1748240; the PDF prints an erroneous0.24012prefix. Live DOI web opening failed; official publisher and separately acquired Crossref metadata, not that failed request, support resolution. |
| organism | https://www.dsmz.de/collection/catalogue/details/culture/dsm-583; Live DSMZ name/accession and https://bacdive.dsmz.de/strain/111 front matter versus genome table | supports | DSM583 catalog/front matter say A.ferrooxidans; BacDive genome table says A.ferridurans DSM583. The record preserves the accession/name conflict without assigning a definitive species CURIE or authenticating the experimental stock. |
| search | /private/tmp/cmm-round29-zinc-independent-review/web-search.json; Fresh first returned web result sets and local dedup; curator referenced-raw inventory checked as provenance | context_only | No affecting correction/retraction or directly matched controlled counterexperiment was identified in these returned sets. Other DSM583 substrate studies and Ilyas2012 are distinct experiments. Current maintained records have no duplicate Horzum ore identity within the stated search. |
| gates | /private/tmp/cmm-round29-final-terminal.json; Final batch, nonempty and trusted-base history receipts and actual logs; reviewer named-check receipt | supports | All required checks completed with exit0, and all inspected record/history/schema/context hashes remained unchanged. |

## Limits And Additional Notes

- One laboratory study of one heterogeneous geological sample; broader ore-family performance is unestablished.
- Numeric abiotic metal time courses, iron/sulfur speciation, organism stock authentication and preculture carryover chemistry are unresolved.
- Source percentages cannot be independently reconciled with serial sampling or a verified feed denominator. Duplicate versus triplicate and ANOVA response labeling are contradictory.
- Pb non-solubilization has no published concentration/detection limit; phase precipitation and passivation remain interpretations.
- No isolated product, environmental advantage, economic benefit or pilot/industrial deployment is demonstrated.
- Literature/notice searches are bounded. Shared primary acquisition/rendering is disclosed, and broader taxonomic reassignment literature was not independently fully reviewed.
- Original-source preparation preceded canonical inspect; the exact maintained record was assessed only after inspect.
- No corrective issue is warranted for this frozen record. Structural validation does not certify scientific truth.
- The reviewer performed no maintained-record/history edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T174859Z-oxidized-zinc-ore-round29-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of mixed Horzum oxidized-zinc ore
started_at: '2026-10-11T17:43:52.833044Z'
finished_at: '2026-10-11T17:48:59.167108Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The maintained record and canonical CREATE history were authored
    by /root/round27_eaf_slag. This reviewer coordinated scope selection but authored
    or edited neither. The complete primary text and all nine original rendered pages
    were independently read, with fresh publisher/DSMZ/BacDive searches and independent
    arithmetic. Original PDF acquisition/rendering were shared curator artifacts;
    the curator dossier was not the sole evidence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record supports a source-defined natural mixed ore and qualified culture-associated
  laboratory dissolution. It explicitly limits causal enhancement, strain identity,
  statistics and yield accounting. No corrective finding was identified in the frozen
  record.
source:
  git_revision: 7629ab50846229c87987d7fa0ac12389212bb70f
  state: working_tree
  inputs:
  - path: data/records/oxidized-zinc-ore.yaml
    sha256: a7b4bca381fce99518963f2ea3d8228c0cf19a7923ec7fe438ca17ee7163fc22
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/oxidized-zinc-ore/2026-10-11T174319Z-codex-9eed32.yaml
    sha256: 9bd8897b0e4fb90a2ae7a15cc0626034166a375d02bd025ae0edcedbc408460b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire new record, all asserted scientific claims and linked CREATE
    history.
  selection: Independent review of the new round29 mixed oxidized-zinc-ore record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:oxidized-zinc-ore
  exclusions:
  - target: Distinct Ilyas2012 mixed-ore column experiment and adjacent substrates
    reason: Leads only; no full-primary evidence or cross-study efficacy claim is
      imported.
targets:
- target_id: cmmmech:oxidized-zinc-ore
  path: data/records/oxidized-zinc-ore.yaml
  label: Oxidized-zinc ore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/oxidized-zinc-ore.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: uv run --locked cmmmech validate data/records/oxidized-zinc-ore.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Executed by this reviewer; terminal exit0,1record checked/0failed.
  target_ids:
  - cmmmech:oxidized-zinc-ore
- check_id: batch
  name: Final batch validation
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual root execution reached terminal exit0. Receipt/log hashes verified
    and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-batch.log'
  target_ids:
  - cmmmech:oxidized-zinc-ore
- check_id: nonempty
  name: Final nonempty validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual root execution reached terminal exit0. Receipt/log hashes verified
    and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-nonempty.log'
  target_ids:
  - cmmmech:oxidized-zinc-ore
- check_id: history
  name: Final history validation
  command: uv run --locked cmmmech validate-history --base 7629ab50846229c87987d7fa0ac12389212bb70f
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual root execution reached terminal exit0. Receipt/log hashes verified
    and frozen input hashes unchanged; log: /private/tmp/cmm-round29-final-history.log'
  target_ids:
  - cmmmech:oxidized-zinc-ore
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/oxidized-zinc-ore.yaml
  locator: Entire frozen YAML and linked canonical CREATE history
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: supports
  summary: Canonical inspect captured the merged-main base and exact working bytes
    before maintained-claim assessment.
  snapshot_sha256: a7b4bca381fce99518963f2ea3d8228c0cf19a7923ec7fe438ca17ee7163fc22
- evidence_id: primary
  kind: primary_source
  reference: https://dergipark.org.tr/en/download/article-file/5079644
  locator: Complete nine-page article, pp1067–1075; all four tables and seven figures;
    methods pp1068–1069 and conclusions pp1072–1073
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: supports
  summary: Original full text and every original rendered page independently inspected.
    The material is a heterogeneous natural ore, and measurements concern acidified
    laboratory flasks with a source-named live culture.
  snapshot_sha256: b4a5bb6855b9c8a48c61bd925646d110f8df84634b0879ee20c69632281792d8
- evidence_id: controls
  kind: primary_source
  reference: https://dergipark.org.tr/en/download/article-file/5079644
  locator: Methods pp1068–1069; Figures1–4 and Table3
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: context_only
  summary: Numeric abiotic Zn/Fe release is not supplied. pH/redox controls, bulk
    cell counts and mixed-phase offset XRD do not establish ferric attack, microbial
    necessity or pure-smithsonite dissolution. Pb is qualitative without a detection
    limit.
  snapshot_sha256: b4a5bb6855b9c8a48c61bd925646d110f8df84634b0879ee20c69632281792d8
- evidence_id: quantitation
  kind: primary_source
  reference: https://dergipark.org.tr/en/download/article-file/5079644
  locator: Equation2; Table1; Tables3–4; Figures5–7; /private/tmp/cmm-round29-zinc-independent-review/arithmetic.json
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: context_only
  summary: The mL/mg-per-L expression, serial withdrawals, unspecified feed assay
    basis, duplicate/triplicate conflict and absent raw replicates prevent independent
    mass reconciliation. Independent Table3 recomputation confirms Table4 total sums
    approximately match raw percentages rather than printed S/N cells. Derived contour
    values are not additional measurements.
  snapshot_sha256: b4a5bb6855b9c8a48c61bd925646d110f8df84634b0879ee20c69632281792d8
- evidence_id: publication
  kind: primary_source
  reference: https://dergipark.org.tr/en/pub/dumf/article/1748240
  locator: Current official article metadata and acquired Crossref registration; paper
    front page
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: supports
  summary: Publisher identity confirms Demirci,2025,16(4),1067–1075 and DOI10.24012/dumf.1748240;
    the PDF prints an erroneous0.24012prefix. Live DOI web opening failed; official
    publisher and separately acquired Crossref metadata, not that failed request,
    support resolution.
- evidence_id: organism
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/dsm-583
  locator: Live DSMZ name/accession and https://bacdive.dsmz.de/strain/111 front matter
    versus genome table
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: supports
  summary: DSM583 catalog/front matter say A.ferrooxidans; BacDive genome table says
    A.ferridurans DSM583. The record preserves the accession/name conflict without
    assigning a definitive species CURIE or authenticating the experimental stock.
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round29-zinc-independent-review/web-search.json
  locator: Fresh first returned web result sets and local dedup; curator referenced-raw
    inventory checked as provenance
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: context_only
  summary: No affecting correction/retraction or directly matched controlled counterexperiment
    was identified in these returned sets. Other DSM583 substrate studies and Ilyas2012
    are distinct experiments. Current maintained records have no duplicate Horzum
    ore identity within the stated search.
  search_scope: 'Exact queries: "10.24012/dumf.1748240" correction OR erratum OR retraction;
    "oxidized zinc ore" "Demirci" "bioleaching" control; "DSM 583" ferrooxidans ferridurans.
    No filters/pagination. rg --no-ignore --hidden --follow searched current records/history/reviews/research
    for oxidized-zinc-ore, Horzum and DOI/article-ID aliases. Curator manifest covers181referenced
    directories and228PDF text-layer attempts,223parsed; root independently checked
    the current primary and authority files, not every historical PDF. No machine-wide
    or exhaustive literature claim.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round29-final-terminal.json
  locator: Final batch, nonempty and trusted-base history receipts and actual logs;
    reviewer named-check receipt
  accessed_at: '2026-10-11T17:48:59.167108Z'
  support: supports
  summary: All required checks completed with exit0, and all inspected record/history/schema/context
    hashes remained unchanged.
  snapshot_sha256: a29de5329c0c561e5c47297bbffe85ba796faeccb33e1520233753a20cd0d776
assessments:
- assessment_id: identity
  area: identity
  topic: Natural mixed resource boundary
  outcome: supported
  summary: Primary-resource scope, mineral-specific exclusions and absent inherited
    criticality are supported.
  target_ids:
  - cmmmech:oxidized-zinc-ore
  evidence_ids:
  - record
  - primary
  - search
  dimensions:
  - name: material_form
    value: 'primary_resource: Fe-rich Kozan-Horzum oxidized zinc ore'
    definition: XRD source labels include smithsonite and hemimorphite with gangue;
      neither a pure mineral nor a processing waste.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim or constituent-element designation
      is inherited.
    evidence_ids:
    - record
- assessment_id: culture
  area: identity
  topic: Source culture and explicit species-name uncertainty
  outcome: supported
  summary: The record retains the paper accession and authority conflict without false
    stock authentication.
  target_ids:
  - cmmmech:oxidized-zinc-ore
  evidence_ids:
  - primary
  - organism
  dimensions:
  - name: organism_and_biomass
    value: Source-named live A.ferrooxidans DSM583; definitive species CURIE absent
    definition: Collection context differs from identity of the actual inoculated
      stock.
    evidence_ids:
    - primary
    - organism
- assessment_id: experiment
  area: evidence
  topic: Qualified culture-associated aqueous dissolution
  outcome: supported
  summary: Conditions, pretreatment, control limits, reported endpoints and deployment
    scope are accurately bounded.
  target_ids:
  - cmmmech:oxidized-zinc-ore
  evidence_ids:
  - primary
  - controls
  - quantitation
  dimensions:
  - name: pretreatment
    value: Oven-dried, jaw-crushed below1cm, ball-milled, sieved below75µm
    definition: Natural mixed ore; medium sterilization does not establish sterile
      ore.
    evidence_ids:
    - primary
  - name: conditions
    value: 250mLflasks,100mLworking liquid,90mLmedium+10mLstarter,150rpm,25±5°C,initialpH1.8–2
    definition: Acidified nominally Fe-free9K; solid ratios10/15/20% have unspecified
      mass/volume basis;6/12/18days.
    evidence_ids:
    - primary
  - name: controls
    value: Abiotic pH/redox curves; numeric abiotic metal dissolution unavailable
    definition: Unspecified preculture chemistry and no matched-pH metal comparison
      limit causality.
    evidence_ids:
    - controls
  - name: outcome_and_scale
    value: Source-reported54.70%Zn/63.14%Fe at10%/12days; laboratory only
    definition: Author-defined dissolution percentages are not reconciled mass yield,
      microbial increment or recovered product;18day decrease retained.
    evidence_ids:
    - primary
    - quantitation
- assessment_id: limits
  area: evidence
  topic: Nulls, contradictory source reporting and alternative explanations
  outcome: supported
  summary: The record explicitly preserves Pb qualitative non-solubilization, replication
    conflict, incomplete volume/mass accounting and unsupported molecular/phase claims.
  target_ids:
  - cmmmech:oxidized-zinc-ore
  evidence_ids:
  - record
  - controls
  - quantitation
  dimensions: []
  details: 'Independent total sums of squares from nine printed Table3 outcomes: Zn1193.4561
    and Fe845.7418, close to printed1193.55/845.68; printed S/N columns give80.1327/31.0182.
    This diagnostic does not repair unavailable replicates or certify significance.
    Unnormalized offset XRD and missing abiotic residue do not prove microbial phase
    destruction; absence of new peaks does not exclude precipitation.'
- assessment_id: provenance
  area: provenance
  topic: Actual curation and immutable exact-state review
  outcome: supported
  summary: Inline CREATE and canonical CREATE accurately describe this new curation;
    no prior authorship or completed review is fabricated.
  target_ids:
  - cmmmech:oxidized-zinc-ore
  evidence_ids:
  - record
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- One laboratory study of one heterogeneous geological sample; broader ore-family
  performance is unestablished.
- Numeric abiotic metal time courses, iron/sulfur speciation, organism stock authentication
  and preculture carryover chemistry are unresolved.
- Source percentages cannot be independently reconciled with serial sampling or a
  verified feed denominator. Duplicate versus triplicate and ANOVA response labeling
  are contradictory.
- Pb non-solubilization has no published concentration/detection limit; phase precipitation
  and passivation remain interpretations.
- No isolated product, environmental advantage, economic benefit or pilot/industrial
  deployment is demonstrated.
- Literature/notice searches are bounded. Shared primary acquisition/rendering is
  disclosed, and broader taxonomic reassignment literature was not independently fully
  reviewed.
notes:
- Original-source preparation preceded canonical inspect; the exact maintained record
  was assessed only after inspect.
- No corrective issue is warranted for this frozen record. Structural validation does
  not certify scientific truth.
- The reviewer performed no maintained-record/history edits.
tags:
- round29
- independent
- scientific-review
- primary-resource
```
