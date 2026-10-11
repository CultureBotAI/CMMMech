# Independent adversarial review of anglesite formation evidence

- Review: 20261011T215350Z-anglesite-round35-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T21:44:16.432598Z
- Finished UTC: 2026-10-11T21:53:50.874639Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified culture-associated anglesite formation is supported; chemical-control formation and recovery limits are preserved. No corrective record defect identified.

## Scope And Provenance

One new anglesite record, all fields, CREATE history and claim-specific evidence.

Selection: Independent review of a round35 record by another agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f83cf867a38c470b4347f721d9ea9370c3019eaf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:anglesite | data/records/anglesite.yaml | maintained | Anglesite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:anglesite | Root executed the named validation: one record checked, zero failed. |
| Final batch batch | passed | True | cmmmech:anglesite | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 119.23s (0:01:59)<br>Checked 198 record(s); 0 failed.<br>Checked 229 history record(s); 0 error(s).; log SHA256 9801e41c5e7f39c58f9711c4b6a36747750740f6e2ccc7ea055ebc0db408af91 |
| Final batch nonempty | passed | True | cmmmech:anglesite | Checked 198 record(s); 0 failed.; log SHA256 1a7af2b5ea572ea7e356525122eadd4bbd64b3ce247bc0c1a7b3eb3b71865ae1 |
| Final batch history | passed | True | cmmmech:anglesite | Checked 229 history record(s); 0 error(s).; log SHA256 6a35723bdc6888001561b265c4859a17d59b55bb8c460f13518e2b9d72d87b64 |

## Scientific And Domain Assessments

### Mineral versus feed and constituent

identity: supported. Targets: cmmmech:anglesite.

Anglesite has a distinct mineral owner. Elemental lead, galena-rich concentrate, synthetic lead salt and battery paste are not conflated. No criticality inherited.

### Organism, substrate and conditions

evidence: supported. Targets: cmmmech:anglesite.

Natural concentrate, live F3-02, sulfate medium,25C/130rpm and288h residue endpoint match methods. Nominal versus tabulated starting chemistry, replicate and final-volume uncertainty remain explicit.

### Culture-associated formation and abiotic controls

evidence: supported. Targets: cmmmech:anglesite.

Figure1 marks anglesite in both residues. Approximately40% versus25% phase proportions are retained as source estimates; different denominators and unspecified quantification prevent a conversion or recovery claim. Cell-like morphology does not prove taxon or crystal chemistry.

### Contradictory quantities and causal limits

evidence: supported. Targets: cmmmech:anglesite.

Original Tables2/3 checked:288h dissolvedPb0.0021 versus0.0022g/L; early control sulfate/residualsulfur printed ratios disagree. Sulfate-rich medium and other sulfides prevent attributing all product sulfate to galena. SyntheticPbS atpHnear5 is not a matched low-pH control.

### Study reuse, history and exact validation

provenance: supported. Targets: cmmmech:anglesite.

Same experiment already appears under galena, explicitly identified as reuse rather than replication. History and exact-byte validation pass; narrow search and source limits remain disclosed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/anglesite.yaml; Every frozen field | supports | Record inspected after native exact-state capture. |
| primary | https://www.journalssystem.com/ppmp/Bioleaching-of-galena-flotation-concentrate,79494,0,2.html; Complete ten-page text pp281-290; original Tables1-3, Figures1-3 | supports | Fresh independent fulltext reading and original table/figure visual checks. XRD identifies anglesite in inoculated and control residues; approximate phase percentages refer to different mixed residues. SEM and solution chemistry do not demonstrate exclusively biological precipitation or a recovered product. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original page11 Anglesite row, definitions pages1-2 | supports | Dated original visually checked: Pb(SO4),grandfatheredG,1832. Formula/year are not a minted ontology identifier. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/920; Retained current official JSON, scientific name/rank | supports | Independently read curator-acquired live response: Acidithiobacillus ferrooxidans,species. This does not verify a separate F3-02 strain accession. |
| history | history/records/anglesite/2026-10-11T213956Z-codex-692a3f.yaml; Whole CREATE history and distinct inline event | supports | Actual actor/model, target, time and narrow source scope match the recorded change. |
| search | Independent web.run and local rg on2026-10-11; Exact-title notice query, organism/material context and Weijma2002 discovery | supports | No specific correction/retraction identified in the returned bounded results. Weijma2002 and other reducing-media studies remain full-evidence leads and do not invalidate this qualified sulfate-medium observation. |

## Limits And Additional Notes

- Original phase proportions have no reported quantitative fitting method or uncertainty.
- Biological replicate counts and detailed sterilization are unavailable; control chemistry diverges.
- Anglesite in the control prevents microbial-necessity or direct-enzymatic crystallization claims.
- No recovered lead/anglesite yield or industrial deployment; no raw diffraction reanalysis or independent experiment.
- Notice searches are bounded; deferred full-text leads remain unresolved.
- No maintained correction needed. Batch receipts refer to the same frozen record/history inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T215350Z-anglesite-round35-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial review of anglesite formation evidence
started_at: '2026-10-11T21:44:16.432598Z'
finished_at: '2026-10-11T21:53:50.874639Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Authored by /root/round27_eaf_slag; root did not author/edit
    the record. Root captured hashes before judgment and independently read primary
    text and original figures/tables plus authority responses. Shared acquired originals
    and prior review of the same study for galena are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified culture-associated anglesite formation is supported; chemical-control
  formation and recovery limits are preserved. No corrective record defect identified.
source:
  git_revision: f83cf867a38c470b4347f721d9ea9370c3019eaf
  state: working_tree
  inputs:
  - path: data/records/anglesite.yaml
    sha256: 5bc650c2efb91ffc664d20a8c3b6967b88e7959ebcc0cd6a19837f201d5d2303
    role: target
  - path: history/records/anglesite/2026-10-11T213956Z-codex-692a3f.yaml
    sha256: f414af073b328ccad402913af7009e28612bcc28144b7dc8ffd9bad172f92c7e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: One new anglesite record, all fields, CREATE history and claim-specific
    evidence.
  selection: Independent review of a round35 record by another agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:anglesite
  exclusions:
  - target: Weijma2002 and other potential reducing-media extensions
    reason: Full methods not accepted into this record; require separate complete
      source assessment.
targets:
- target_id: cmmmech:anglesite
  path: data/records/anglesite.yaml
  label: Anglesite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anglesite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/anglesite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Root executed the named validation: one record checked, zero failed.'
  target_ids:
  - cmmmech:anglesite
- check_id: batch
  name: Final batch batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 119.23s (0:01:59)

    Checked 198 record(s); 0 failed.

    Checked 229 history record(s); 0 error(s).; log SHA256 9801e41c5e7f39c58f9711c4b6a36747750740f6e2ccc7ea055ebc0db408af91'
  target_ids:
  - cmmmech:anglesite
- check_id: nonempty
  name: Final batch nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 198 record(s); 0 failed.; log SHA256 1a7af2b5ea572ea7e356525122eadd4bbd64b3ce247bc0c1a7b3eb3b71865ae1
  target_ids:
  - cmmmech:anglesite
- check_id: history
  name: Final batch history
  command: uv run --locked cmmmech validate-history --base f83cf867a38c470b4347f721d9ea9370c3019eaf
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 229 history record(s); 0 error(s).; log SHA256 6a35723bdc6888001561b265c4859a17d59b55bb8c460f13518e2b9d72d87b64
  target_ids:
  - cmmmech:anglesite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/anglesite.yaml
  locator: Every frozen field
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: Record inspected after native exact-state capture.
  snapshot_sha256: 5bc650c2efb91ffc664d20a8c3b6967b88e7959ebcc0cd6a19837f201d5d2303
- evidence_id: primary
  kind: primary_source
  reference: https://www.journalssystem.com/ppmp/Bioleaching-of-galena-flotation-concentrate,79494,0,2.html
  locator: Complete ten-page text pp281-290; original Tables1-3, Figures1-3
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: Fresh independent fulltext reading and original table/figure visual checks.
    XRD identifies anglesite in inoculated and control residues; approximate phase
    percentages refer to different mixed residues. SEM and solution chemistry do not
    demonstrate exclusively biological precipitation or a recovered product.
  snapshot_sha256: 9a0a9d6a4df1e2c42cc369aa8e17d7d35c47f2da29b5b0dc674901725eae4925
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original page11 Anglesite row, definitions pages1-2
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: 'Dated original visually checked: Pb(SO4),grandfatheredG,1832. Formula/year
    are not a minted ontology identifier.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/920
  locator: Retained current official JSON, scientific name/rank
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: 'Independently read curator-acquired live response: Acidithiobacillus ferrooxidans,species.
    This does not verify a separate F3-02 strain accession.'
  snapshot_sha256: f5107f8a4b1402959e12b452847ac3025f22d6005c88e6533f64d1fddef66b4f
- evidence_id: history
  kind: record_content
  reference: history/records/anglesite/2026-10-11T213956Z-codex-692a3f.yaml
  locator: Whole CREATE history and distinct inline event
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: Actual actor/model, target, time and narrow source scope match the recorded
    change.
  snapshot_sha256: f414af073b328ccad402913af7009e28612bcc28144b7dc8ffd9bad172f92c7e
- evidence_id: search
  kind: search
  reference: Independent web.run and local rg on2026-10-11
  locator: Exact-title notice query, organism/material context and Weijma2002 discovery
  accessed_at: '2026-10-11T21:53:50.874639Z'
  support: supports
  summary: No specific correction/retraction identified in the returned bounded results.
    Weijma2002 and other reducing-media studies remain full-evidence leads and do
    not invalidate this qualified sulfate-medium observation.
  search_scope: 'Web queries: "Bioleaching of galena flotation concentrate" correction
    erratum retraction; "Pacholewska" "anglesite" "2004" control; "Biological conversion
    of anglesite" Weijma2002. Returned result sets only. Root local command: rg --no-ignore
    --hidden --follow -l -i anglesite|bp025523k|Pacholewska data/records research
    reviews history /private/tmp/cmm-round34-galena-research /private/tmp/cmm-round35-anglesite-research;
    includes ignored/hidden and relevant symlinks within those boundaries, not a machine-wide
    or global absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral versus feed and constituent
  outcome: supported
  summary: Anglesite has a distinct mineral owner. Elemental lead, galena-rich concentrate,
    synthetic lead salt and battery paste are not conflated. No criticality inherited.
  target_ids:
  - cmmmech:anglesite
  evidence_ids:
  - record
  - ima
  - primary
- assessment_id: culture
  area: evidence
  topic: Organism, substrate and conditions
  outcome: supported
  summary: Natural concentrate, live F3-02, sulfate medium,25C/130rpm and288h residue
    endpoint match methods. Nominal versus tabulated starting chemistry, replicate
    and final-volume uncertainty remain explicit.
  target_ids:
  - cmmmech:anglesite
  evidence_ids:
  - record
  - primary
  - taxon
  dimensions:
  - name: organism
    value: Living source-labelled A.ferrooxidans F3-02
    definition: Taxon920 is species only; no authenticated strain accession.
    evidence_ids:
    - primary
    - taxon
  - name: scale
    value: Laboratory mixed-concentrate flask residue
    definition: Feed industrial origin does not establish deployed mineral recovery.
    evidence_ids:
    - record
    - primary
- assessment_id: phase
  area: evidence
  topic: Culture-associated formation and abiotic controls
  outcome: supported
  summary: Figure1 marks anglesite in both residues. Approximately40% versus25% phase
    proportions are retained as source estimates; different denominators and unspecified
    quantification prevent a conversion or recovery claim. Cell-like morphology does
    not prove taxon or crystal chemistry.
  target_ids:
  - cmmmech:anglesite
  evidence_ids:
  - record
  - primary
- assessment_id: accounting
  area: evidence
  topic: Contradictory quantities and causal limits
  outcome: supported
  summary: Original Tables2/3 checked:288h dissolvedPb0.0021 versus0.0022g/L; early
    control sulfate/residualsulfur printed ratios disagree. Sulfate-rich medium and
    other sulfides prevent attributing all product sulfate to galena. SyntheticPbS
    atpHnear5 is not a matched low-pH control.
  target_ids:
  - cmmmech:anglesite
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Study reuse, history and exact validation
  outcome: supported
  summary: Same experiment already appears under galena, explicitly identified as
    reuse rather than replication. History and exact-byte validation pass; narrow
    search and source limits remain disclosed.
  target_ids:
  - cmmmech:anglesite
  evidence_ids:
  - record
  - history
  - search
findings: []
actions: []
limitations:
- Original phase proportions have no reported quantitative fitting method or uncertainty.
- Biological replicate counts and detailed sterilization are unavailable; control
  chemistry diverges.
- Anglesite in the control prevents microbial-necessity or direct-enzymatic crystallization
  claims.
- No recovered lead/anglesite yield or industrial deployment; no raw diffraction reanalysis
  or independent experiment.
- Notice searches are bounded; deferred full-text leads remain unresolved.
notes:
- No maintained correction needed. Batch receipts refer to the same frozen record/history
  inputs.
tags:
- round35
- anglesite
- independent
- scientific
```
