# Independent scientific review of heavy-fuel-oil combustion ash

- Review: 20261011T150126Z-heavy-fuel-oil-combustion-ash-round25-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T14:57:27.627988Z
- Finished UTC: 2026-10-11T15:01:26.658372Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact record is defensible as a source-reported laboratory spent-medium observation. It preserves unverified culture accession, absent matched controls and metal-assay detail, declining reactor-derived Ni extraction, ambiguous residue phases and scale boundaries. No corrective record finding was identified.

## Scope And Provenance

Whole new scientific record, material identity, species mapping, experimental conditions and comparisons, source limits, and actual history.

Selection: Assigned independent assessment of oil-ash record authored by another agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baedff25eafad1516270916a651af6754ffa5996.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:heavy-fuel-oil-combustion-ash | data/records/heavy-fuel-oil-combustion-ash.yaml | maintained | Heavy-fuel-oil combustion ash |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-file validation | passed | True | cmmmech:heavy-fuel-oil-combustion-ash | Checked 1 record(s); 0 failed. Executed by this reviewer before saving. |
| Native full checks | passed | True | cmmmech:heavy-fuel-oil-combustion-ash | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 98.72s (0:01:38)<br>Checked 165 record(s); 0 failed.<br>Checked 186 history record(s); 0 error(s). |
| Nonempty corpus | passed | True | cmmmech:heavy-fuel-oil-combustion-ash | Checked 165 record(s); 0 failed. |
| Trusted-base history | passed | True | cmmmech:heavy-fuel-oil-combustion-ash | Checked 186 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Process-defined waste identity

identity: supported. Targets: cmmmech:heavy-fuel-oil-combustion-ash.

The broader combustion-ash resource is supported; a specific fly-ash collection fraction and inherited criticality are correctly not asserted.

### Culture-liquid leaching observation

evidence: supported. Targets: cmmmech:heavy-fuel-oil-combustion-ash.

Primary evidence supports the recorded assay and asymmetric V/Ni outcomes, while inadequate controls and assay detail prevent causal or independently reconstructed recovery claims.

### Exact final-state curation and checks

provenance: supported. Targets: cmmmech:heavy-fuel-oil-combustion-ash.

Actual CREATE history and inline event are distinct; unchanged target hash matches final gates. All prior artifacts remain historical observations.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/heavy-fuel-oil-combustion-ash.yaml; Entire frozen target and attached history | supports | Resource identity, reported experimental scope and uncertainty are explicit. |
| primary | https://www.ijcea.org/vol7/606-G0007.pdf; All four pages read; Sections II-IV and Figures 1-4 independently viewed in local rendered pages 2-4. Primary text does not contain a data table. | supports | The full paper supports actual oil-power-plant residue, A. niger PTCC 5210 as reported, different culture durations, biomass separation without method, 3 percent w/v leaching at 60 degrees C for seven days, V/Ni outcomes and substantial analytical/control limits. |
| authority | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5061&amp;mode=Info; Live NCBI Taxonomy species page | supports | NCBITaxon:5061 resolves Aspergillus niger. Species resolution does not authenticate PTCC 5210; the record states this boundary. |
| search | https://www.ijcea.org/index.php?a=show&amp;c=index&amp;catid=81&amp;id=981&amp;m=content; Live exact DOI/title correction/retraction searches, first returned result sets, and publisher metadata; local rg --no-ignore --hidden --follow data research reviews history and round25 oil-ash raw directory, excluding binary PDF/image and HTML grep with primary PDF independently inspected. | supports | No applicable correction notice surfaced in the bounded results; related publications and conference abstract cannot be assumed independent experiments. No exhaustive absence claim. Existing coal ash/catalyst roots do not denote this oil-combustion feed. |
| gates | /private/tmp/cmm-round25-final-batch-terminal.json; Terminal command receipt and final record hash | supports | This reviewer independently ran named validation and inspected root-run final batch, nonempty and history checks. Their hashes match this target. Offline checks do not prove scientific validity. |

## Limits And Additional Notes

- PTCC 5210 is source-reported and not independently resolved at the collection; species mapping cannot authenticate the stock.
- Liquid-metal analysis, sampling fraction, yield equation, replication and uncertainty are unspecified; no matched abiotic leach control is available.
- Different culture histories confound scale and metabolite effects. Reactor-derived medium has lower Ni extraction than flask-derived medium.
- Figure 3 labels additional treated-solid phases beyond the simplified prose. Ni-oxalate precipitation is proposed without independent phase confirmation; loss of an XRD peak is not proof of zero residual V.
- Raw paper was read locally; a fresh web PDF request failed, while indexed publisher identity and live NCBI resolved. Correction/supplement search coverage is bounded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T150126Z-heavy-fuel-oil-combustion-ash-round25-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of heavy-fuel-oil combustion ash
started_at: '2026-10-11T14:57:27.627988Z'
finished_at: '2026-10-11T15:01:26.658372Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round24_sulfuric_catalyst authored the scientific
    record and history. Root independently inspected complete primary text, all figures
    and authority/search evidence without editing the target. Shared worktree and
    author-acquired primary PDF are disclosed; root coordinates publication.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact record is defensible as a source-reported laboratory spent-medium
  observation. It preserves unverified culture accession, absent matched controls
  and metal-assay detail, declining reactor-derived Ni extraction, ambiguous residue
  phases and scale boundaries. No corrective record finding was identified.
source:
  git_revision: baedff25eafad1516270916a651af6754ffa5996
  state: working_tree
  inputs:
  - path: data/records/heavy-fuel-oil-combustion-ash.yaml
    sha256: bba70873e33a58d1834885cb4f9a42651a50d6c37c3386a5795becee07bb4b96
    role: target
  - path: history/records/heavy-fuel-oil-combustion-ash/2026-10-11T145457Z-codex-1000af.yaml
    sha256: 1760bd5c7fc8ee1d86793ad79b30fbd52259f3c06a91852c211650016470f582
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Whole new scientific record, material identity, species mapping, experimental
    conditions and comparisons, source limits, and actual history.
  selection: Assigned independent assessment of oil-ash record authored by another
    agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
  exclusions:
  - target: RSC and Waste Management extensions
    reason: Incomplete full-source access in the curation dossier; no unverified mechanism
      claim from those papers enters this record.
targets:
- target_id: cmmmech:heavy-fuel-oil-combustion-ash
  path: data/records/heavy-fuel-oil-combustion-ash.yaml
  label: Heavy-fuel-oil combustion ash
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/heavy-fuel-oil-combustion-ash.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named-file validation
  command: .venv/bin/python -m cmmmech validate data/records/heavy-fuel-oil-combustion-ash.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed. Executed by this reviewer before saving.
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
- check_id: batch
  name: Native full checks
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

    308 passed, 3 skipped in 98.72s (0:01:38)

    Checked 165 record(s); 0 failed.

    Checked 186 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
- check_id: require
  name: Nonempty corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 165 record(s); 0 failed.
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base baedff25eafad1516270916a651af6754ffa5996
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 186 history record(s); 0 error(s).
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/heavy-fuel-oil-combustion-ash.yaml
  locator: Entire frozen target and attached history
  accessed_at: '2026-10-11T15:01:26.658372Z'
  support: supports
  summary: Resource identity, reported experimental scope and uncertainty are explicit.
  snapshot_sha256: bba70873e33a58d1834885cb4f9a42651a50d6c37c3386a5795becee07bb4b96
- evidence_id: primary
  kind: primary_source
  reference: https://www.ijcea.org/vol7/606-G0007.pdf
  locator: All four pages read; Sections II-IV and Figures 1-4 independently viewed
    in local rendered pages 2-4. Primary text does not contain a data table.
  accessed_at: '2026-10-11T15:01:26.658372Z'
  support: supports
  summary: The full paper supports actual oil-power-plant residue, A. niger PTCC 5210
    as reported, different culture durations, biomass separation without method, 3
    percent w/v leaching at 60 degrees C for seven days, V/Ni outcomes and substantial
    analytical/control limits.
  snapshot_sha256: 2d93472f2b7fdc1f056c4be031ee3b9bb187ed1f9e29193ad7b67d44cb15f269
- evidence_id: authority
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5061&mode=Info
  locator: Live NCBI Taxonomy species page
  accessed_at: '2026-10-11T15:01:26.658372Z'
  support: supports
  summary: NCBITaxon:5061 resolves Aspergillus niger. Species resolution does not
    authenticate PTCC 5210; the record states this boundary.
- evidence_id: search
  kind: search
  reference: https://www.ijcea.org/index.php?a=show&c=index&catid=81&id=981&m=content
  locator: Live exact DOI/title correction/retraction searches, first returned result
    sets, and publisher metadata; local rg --no-ignore --hidden --follow data research
    reviews history and round25 oil-ash raw directory, excluding binary PDF/image
    and HTML grep with primary PDF independently inspected.
  accessed_at: '2026-10-11T15:01:26.658372Z'
  support: supports
  summary: No applicable correction notice surfaced in the bounded results; related
    publications and conference abstract cannot be assumed independent experiments.
    No exhaustive absence claim. Existing coal ash/catalyst roots do not denote this
    oil-combustion feed.
  search_scope: Live exact DOI/title correction/retraction searches, first returned
    result sets, and publisher metadata; local rg --no-ignore --hidden --follow data
    research reviews history and round25 oil-ash raw directory, excluding binary PDF/image
    and HTML grep with primary PDF independently inspected.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round25-final-batch-terminal.json
  locator: Terminal command receipt and final record hash
  accessed_at: '2026-10-11T15:01:26.658372Z'
  support: supports
  summary: This reviewer independently ran named validation and inspected root-run
    final batch, nonempty and history checks. Their hashes match this target. Offline
    checks do not prove scientific validity.
  snapshot_sha256: 1a824b26e98d09ece2c6ff116385fdc5651f4d2de7245d3f3a20c15ac3cc32ce
assessments:
- assessment_id: identity
  area: identity
  topic: Process-defined waste identity
  outcome: supported
  summary: The broader combustion-ash resource is supported; a specific fly-ash collection
    fraction and inherited criticality are correctly not asserted.
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Oil-fired thermal-power-plant ash; distinct from coal ash, petroleum
      coke, refinery catalysts and constituent elements.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition designation is claimed for this resource.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Culture-liquid leaching observation
  outcome: supported
  summary: Primary evidence supports the recorded assay and asymmetric V/Ni outcomes,
    while inadequate controls and assay detail prevent causal or independently reconstructed
    recovery claims.
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
  evidence_ids:
  - record
  - primary
  - authority
  dimensions:
  - name: organism
    value: Source-reported Aspergillus niger PTCC 5210
    definition: Species NCBITaxon:5061 is verified; collection stock is not independently
      authenticated.
    evidence_ids:
    - primary
    - authority
  - name: biomass_state
    value: Spent medium after stated biomass removal
    definition: Removal procedure and residual viable cells are unspecified.
    evidence_ids:
    - primary
  - name: conditions_controls
    value: 3 percent w/v ash, 60 degrees C, seven days
    definition: 'Culture production differed: fourteen-day flasks versus seven-day
      1-L reactor. No matched abiotic ash-leaching arm was reported; Figure 1 agar
      control is a different experiment.'
    evidence_ids:
    - primary
  - name: outcomes
    value: Reported 97 percent V/50 percent Ni versus 100 percent V/33 percent Ni
    definition: Missing liquid-metal assay, fraction, yield equation, replicates and
      errors prevent treating source percentages as closed product yields.
    evidence_ids:
    - primary
  - name: deployment
    value: Laboratory culture comparison and subsequent leaching
    definition: 1-L scale concerns culture production; no demonstrated industrial
      process, isolated product or validated safe residue reuse.
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Exact final-state curation and checks
  outcome: supported
  summary: Actual CREATE history and inline event are distinct; unchanged target hash
    matches final gates. All prior artifacts remain historical observations.
  target_ids:
  - cmmmech:heavy-fuel-oil-combustion-ash
  evidence_ids:
  - record
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- PTCC 5210 is source-reported and not independently resolved at the collection; species
  mapping cannot authenticate the stock.
- Liquid-metal analysis, sampling fraction, yield equation, replication and uncertainty
  are unspecified; no matched abiotic leach control is available.
- Different culture histories confound scale and metabolite effects. Reactor-derived
  medium has lower Ni extraction than flask-derived medium.
- Figure 3 labels additional treated-solid phases beyond the simplified prose. Ni-oxalate
  precipitation is proposed without independent phase confirmation; loss of an XRD
  peak is not proof of zero residual V.
- Raw paper was read locally; a fresh web PDF request failed, while indexed publisher
  identity and live NCBI resolved. Correction/supplement search coverage is bounded.
tags:
- round25
- independent
- secondary-resource
links:
- https://github.com/CultureBotAI/CMMMech/issues/90
```
