# Independent scientific review of copper-smelter slag

- Review: 20261011T142755Z-copper-smelter-slag-round24-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T14:22:37.776952Z
- Finished UTC: 2026-10-11T14:27:55.458809Z
- Reviewer: Codex /root/round24_sulfuric_catalyst (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact record supports a narrowly scoped culture-associated metal-mobilization observation in two historical copper slags. Source inconsistencies, unlike pH and incomplete phase/product accounting remain explicit; no corrective finding in this scope.

## Scope And Provenance

Entire exact maintained record, resource identity, organism/strain, mechanism conditions and controls, outcome limits, source locators and actual CREATE history.

Selection: One assigned new copper-smelter-slag record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d7183efeb2e528d6d88f0b69da41323642b8fa85.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:copper-smelter-slag | data/records/copper-smelter-slag.yaml | maintained | Copper-smelter slag |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:copper-smelter-slag | Checked 1 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:copper-smelter-slag | /private/tmp/cmm-round24-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 89.10s (0:01:29)<br>Checked 160 record(s); 0 failed.<br>Checked 181 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:copper-smelter-slag | /private/tmp/cmm-round24-final-require.log: Checked 160 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:copper-smelter-slag | /private/tmp/cmm-round24-final-history.log: Checked 181 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Process-defined secondary resource

identity: supported. Targets: cmmmech:copper-smelter-slag.

Historical crystalline and predominantly glassy copper slags are two characterized feeds in one process-defined resource. Their constituent phases and bulk copper do not replace the root identity.

### Conditional culture-associated solubilization

evidence: supported. Targets: cmmmech:copper-smelter-slag.

The narrow 1 percent-loading observation is scientifically defensible and retains pH confounding, source contradictions and process-scale limits.

### Actual CREATE and independent exact-state review

provenance: supported. Targets: cmmmech:copper-smelter-slag.

Canonical sidecar and separate inline event describe actual new curation. This reviewer did not author or modify the target; inspected hashes remain equal to the frozen gated state.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/copper-smelter-slag.yaml; Entire exact record, its CREATE sidecar and input hashes captured before scientific judgment | supports | The reviewed material denotes actual historical copper-smelting slag, distinct from copper ore, flotation tailings, mineral species and a recovered product. No inherited criticality or invented resource CURIE is asserted. |
| primary | https://doi.org/10.3390/min9090542; Publisher v2 PDF, 24 pages; Methods 2.1-2.3, Results 3.1-3.6 and conclusions; Figures 1-9 and Tables 1-4 visually checked on pages 4,6,8,9,13-15,17,19-20 | supports | Independent full-text and visual inspection supports the low-loading culture association and confirms the record retains source conflicts: 52.1 versus 52.7 percent CS Cu, 1981 versus 2257 mg/kg, highest loading 3 versus 5 percent, and the inconsistent 31-fold AS improvement. Figure 6 shows substantial AS sterile-medium Cu release; Table 2 shows much lower culture pH. These limit exact effect sizes and direct cellular causality. Figures 7-9 do not quantify all phase fluxes or a pure recovered product. |
| authority | https://www.dsmz.de/collection/catalogue/details/culture/DSM-9463; Live DSMZ culture catalogue and NCBI Taxonomy 930, read independently in this curation/review session | supports | DSM 9463 is A. thiooxidans B-S2 from an Australian bioleaching reactor. NCBI 930 is the species; neither page independently authenticates the study stock or demonstrates necessity of an identified strain gene. |
| search | https://www.mdpi.com/2075-163X/9/9/542/xml; Live primary indexed text and bounded correction/control queries on 2026-10-11 | context_only | Independent queries "10.3390/min9090542" correction OR retraction and "Prospective (Bio)leaching of Historical Copper Slags" "control" did not return an affecting correction in the inspected first sets. Primary indexed XML independently confirms the paper identity and relevant culture result. Direct publisher main/notes opens failed, so the curator version-note chronology is not represented as independently reacquired. A fresh complete publisher v2 PDF had been acquired by the author and was independently read here. |
| provenance | research/ingests/round24-copper-slag-sources-20261011.json; Acquisition manifest, PDF SHA-256 and source/version boundaries | supports | Version-specific publisher PDF hash matches the inspected artifact. Source assessment identifies the earlier incorrect discovery DOI and uses the verified DOI in this record without editing immutable historical artifacts. Raw articles stay outside Git and author versus reviewer roles are distinct. |
| gates | /private/tmp/cmm-round24-gate-receipts.json; Completed batch command receipts and exact frozen target hash | supports | The coordinating agent ran the batch checks; this reviewer independently read the terminal receipt/logs and checked the current target hash against the gated set. Named-file validation was run independently. These are structural checks, not proof of scientific causality. |

## Limits And Additional Notes

- The changing biotic-versus-sterile acidity prevents separation of direct cellular action from solution chemistry.
- Source highest-loading labels, CS Cu endpoint and enhancement ratio conflict; the record preserves them without inventing repaired values.
- Temperature, working volume, initial cell density and arm-specific replication remain unresolved in the inspected primary methods.
- Microscopy and elemental ratios do not quantify all phase-specific dissolution or isolated product purity; theoretical economic estimates do not establish deployment or safe reuse.
- Direct publisher main/notes routes failed during reviewer browsing; the acquired 24-page v2 PDF and indexed primary XML were inspected. No complete scientific comparison of every publisher version was performed.
- The correction and local duplicate searches were bounded; no universal absence or exhausted-literature claim is made.
- Canonical inspection preceded scientific assessment. All named target/context hashes were checked again before saving.
- No record correction or GitHub issue was warranted by this scoped review; broader batch publication remains the coordinating agent responsibility.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T142755Z-copper-smelter-slag-round24-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of copper-smelter slag
started_at: '2026-10-11T14:22:37.776952Z'
finished_at: '2026-10-11T14:27:55.458809Z'
reviewer:
  identity: Codex /root/round24_sulfuric_catalyst
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round24_copper_slag authored this record. Reviewer
    independently read the primary v2 PDF, relevant figures/tables and authority identifiers,
    and made no target edits. Shared worktree, curator dossier and curator-acquired
    primary files are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact record supports a narrowly scoped culture-associated metal-mobilization
  observation in two historical copper slags. Source inconsistencies, unlike pH and
  incomplete phase/product accounting remain explicit; no corrective finding in this
  scope.
source:
  git_revision: d7183efeb2e528d6d88f0b69da41323642b8fa85
  state: working_tree
  inputs:
  - path: data/records/copper-smelter-slag.yaml
    sha256: 7bb7f5b9f30798aea8d3dc8d5bb4eeef849612bbd4aafc640a12a386149d7a2d
    role: target
  - path: history/records/copper-smelter-slag/2026-10-11T142004Z-codex-b5d18a.yaml
    sha256: 1abf6bf915f99a8545c70c80dbe64feba1e2e00258e1d812e68e599699195f97
    role: context
  - path: research/ingests/round24-copper-slag-sources-20261011.json
    sha256: c3a4eb36d708af79451cd76c8b64adbd278d38ae325582fc4a9ad046d43838a7
    role: context
  - path: research/ingests/round24-copper-slag-sources-20261011.md
    sha256: de57da01008480bc6792a7ff127d9e8f0c73479f8806990c2b2191577ce48115
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire exact maintained record, resource identity, organism/strain,
    mechanism conditions and controls, outcome limits, source locators and actual
    CREATE history.
  selection: One assigned new copper-smelter-slag record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:copper-smelter-slag
  exclusions:
  - target: Other copper-slag experiments and unavailable underlying raw measurements
    reason: No claims from the deferred Brar/Kaksonen studies were imported. This
      review assesses the current 2019-study record rather than uncurated extensions.
targets:
- target_id: cmmmech:copper-smelter-slag
  path: data/records/copper-smelter-slag.yaml
  label: Copper-smelter slag
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/copper-smelter-slag.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named validation
  command: .venv/bin/python -m cmmmech validate data/records/copper-smelter-slag.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:copper-smelter-slag
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round24-final-batch.log: uv run --locked --extra dev
    python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 89.10s (0:01:29)

    Checked 160 record(s); 0 failed.

    Checked 181 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:copper-smelter-slag
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round24-final-require.log: Checked 160 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:copper-smelter-slag
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base d7183efeb2e528d6d88f0b69da41323642b8fa85
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round24-final-history.log: Checked 181 history record(s);
    0 error(s).

    '
  target_ids:
  - cmmmech:copper-smelter-slag
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/copper-smelter-slag.yaml
  locator: Entire exact record, its CREATE sidecar and input hashes captured before
    scientific judgment
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: supports
  summary: The reviewed material denotes actual historical copper-smelting slag, distinct
    from copper ore, flotation tailings, mineral species and a recovered product.
    No inherited criticality or invented resource CURIE is asserted.
  snapshot_sha256: 7bb7f5b9f30798aea8d3dc8d5bb4eeef849612bbd4aafc640a12a386149d7a2d
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min9090542
  locator: Publisher v2 PDF, 24 pages; Methods 2.1-2.3, Results 3.1-3.6 and conclusions;
    Figures 1-9 and Tables 1-4 visually checked on pages 4,6,8,9,13-15,17,19-20
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: supports
  summary: 'Independent full-text and visual inspection supports the low-loading culture
    association and confirms the record retains source conflicts: 52.1 versus 52.7
    percent CS Cu, 1981 versus 2257 mg/kg, highest loading 3 versus 5 percent, and
    the inconsistent 31-fold AS improvement. Figure 6 shows substantial AS sterile-medium
    Cu release; Table 2 shows much lower culture pH. These limit exact effect sizes
    and direct cellular causality. Figures 7-9 do not quantify all phase fluxes or
    a pure recovered product.'
  snapshot_sha256: 01a049220ef20c8bc9722087714a571f61309a384d10a332eec315162d663717
- evidence_id: authority
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-9463
  locator: Live DSMZ culture catalogue and NCBI Taxonomy 930, read independently in
    this curation/review session
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: supports
  summary: DSM 9463 is A. thiooxidans B-S2 from an Australian bioleaching reactor.
    NCBI 930 is the species; neither page independently authenticates the study stock
    or demonstrates necessity of an identified strain gene.
- evidence_id: search
  kind: search
  reference: https://www.mdpi.com/2075-163X/9/9/542/xml
  locator: Live primary indexed text and bounded correction/control queries on 2026-10-11
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: context_only
  summary: Independent queries "10.3390/min9090542" correction OR retraction and "Prospective
    (Bio)leaching of Historical Copper Slags" "control" did not return an affecting
    correction in the inspected first sets. Primary indexed XML independently confirms
    the paper identity and relevant culture result. Direct publisher main/notes opens
    failed, so the curator version-note chronology is not represented as independently
    reacquired. A fresh complete publisher v2 PDF had been acquired by the author
    and was independently read here.
  search_scope: First result sets only; no filters or pagination. Fresh rg --no-ignore
    --hidden --follow covered data/records, research, reviews and history for DOI,
    copper-smelter-slag and historical-copper-slag variants. The author named raw
    directory and round23 dedup report were inspected; no machine-wide or literature-exhaustion
    assertion.
- evidence_id: provenance
  kind: record_content
  reference: research/ingests/round24-copper-slag-sources-20261011.json
  locator: Acquisition manifest, PDF SHA-256 and source/version boundaries
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: supports
  summary: Version-specific publisher PDF hash matches the inspected artifact. Source
    assessment identifies the earlier incorrect discovery DOI and uses the verified
    DOI in this record without editing immutable historical artifacts. Raw articles
    stay outside Git and author versus reviewer roles are distinct.
  snapshot_sha256: c3a4eb36d708af79451cd76c8b64adbd278d38ae325582fc4a9ad046d43838a7
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round24-gate-receipts.json
  locator: Completed batch command receipts and exact frozen target hash
  accessed_at: '2026-10-11T14:27:55.458809Z'
  support: supports
  summary: The coordinating agent ran the batch checks; this reviewer independently
    read the terminal receipt/logs and checked the current target hash against the
    gated set. Named-file validation was run independently. These are structural checks,
    not proof of scientific causality.
  snapshot_sha256: 78d51f2509b4419f72d1833d47d0d3b26bb21a56e3cad6bd806665d10ca026bb
assessments:
- assessment_id: identity
  area: identity
  topic: Process-defined secondary resource
  outcome: supported
  summary: Historical crystalline and predominantly glassy copper slags are two characterized
    feeds in one process-defined resource. Their constituent phases and bulk copper
    do not replace the root identity.
  target_ids:
  - cmmmech:copper-smelter-slag
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Residue generated by copper smelting; actual historical Polish feeds
      CS and AS.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction, authority, list or edition is inherited from copper
      or other constituents.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Conditional culture-associated solubilization
  outcome: supported
  summary: The narrow 1 percent-loading observation is scientifically defensible and
    retains pH confounding, source contradictions and process-scale limits.
  target_ids:
  - cmmmech:copper-smelter-slag
  evidence_ids:
  - record
  - primary
  - authority
  dimensions:
  - name: organism_strain
    value: Acidithiobacillus thiooxidans DSM 9463 (B-S2)
    definition: Species identifier NCBITaxon:930 and separately source-reported culture
      accession.
    evidence_ids:
    - authority
    - primary
  - name: biomass_state
    value: Living pregrown culture
    definition: Two-week preculture and 2 percent v/v inoculum; sulfur-settling assay
      is qualitative activity evidence.
    evidence_ids:
    - primary
  - name: substrate_pretreatment
    value: 0.25-0.5 mm historical copper-smelter slags CS and AS
    definition: Mixed fayalite/glass-rich versus predominantly glassy feeds with different
      Cu-bearing phases; not pure mineral assays.
    evidence_ids:
    - primary
  - name: conditions_controls
    value: 21 days, 150 rpm, initial pH 3.5 with free drift, 1 percent w/v S
    definition: 1 percent pulp-density focus; sterile-medium controls end at higher
      pH. Working volume, incubation temperature and starting cell density remain
      unspecified rather than inferred.
    evidence_ids:
    - primary
  - name: outcome
    value: Reported liquid metal extraction relative to starting slag inventory
    definition: AS day-21 values are source-reported 98.7 percent Cu and 73.0 percent
      Zn; record does not adopt contradictory exact CS effect sizes or prove product
      recovery.
    evidence_ids:
    - primary
  - name: deployment
    value: Laboratory flask experiment
    definition: Historical industrial feed origin and theoretical metal-price tables
      do not demonstrate industrial operation, measured profit or safe residue reuse.
    evidence_ids:
    - record
    - primary
- assessment_id: history
  area: provenance
  topic: Actual CREATE and independent exact-state review
  outcome: supported
  summary: Canonical sidecar and separate inline event describe actual new curation.
    This reviewer did not author or modify the target; inspected hashes remain equal
    to the frozen gated state.
  target_ids:
  - cmmmech:copper-smelter-slag
  evidence_ids:
  - record
  - provenance
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- The changing biotic-versus-sterile acidity prevents separation of direct cellular
  action from solution chemistry.
- Source highest-loading labels, CS Cu endpoint and enhancement ratio conflict; the
  record preserves them without inventing repaired values.
- Temperature, working volume, initial cell density and arm-specific replication remain
  unresolved in the inspected primary methods.
- Microscopy and elemental ratios do not quantify all phase-specific dissolution or
  isolated product purity; theoretical economic estimates do not establish deployment
  or safe reuse.
- Direct publisher main/notes routes failed during reviewer browsing; the acquired
  24-page v2 PDF and indexed primary XML were inspected. No complete scientific comparison
  of every publisher version was performed.
- The correction and local duplicate searches were bounded; no universal absence or
  exhausted-literature claim is made.
notes:
- Canonical inspection preceded scientific assessment. All named target/context hashes
  were checked again before saving.
- No record correction or GitHub issue was warranted by this scoped review; broader
  batch publication remains the coordinating agent responsibility.
tags:
- round24
- independent
- scientific-review
- secondary-resource
```
