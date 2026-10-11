# Independent scientific review of Dunite

- Review: 20261011T112143Z-dunite-round18-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:16:41Z
- Finished UTC: 2026-10-11T11:21:43Z
- Reviewer: Codex /root/round18_mineral_feeds (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded resource identity and laboratory mechanism claims are supported. No actionable defect was identified in the inspected bytes. Source contradictions and experimental limits remain explicit.

## Scope And Provenance

All fields and linked CREATE history of the assigned final record, including resource boundary, assay conditions, controls, quantitative claims and limitations.

Selection: One assigned new maintained record in the round18 batch, reviewed against its frozen inspected hash.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26cb0688effb2f71e4a570c416f6f43ff858c5ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:dunite | data/records/dunite.yaml | maintained | Dunite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:dunite | Reviewer observed terminal exit 0: Checked 2 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:dunite | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 86.49s (0:01:26)<br>Checked 138 record(s); 0 failed.<br>Checked 154 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:dunite | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-require.log: Checked 138 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:dunite | Parent executed and confirmed terminal completion; reviewer independently read completed receipt and all three logs. /private/tmp/cmm-round18-final-history.log: Checked 154 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Resource, organism and criticality boundaries

identity: supported. Targets: cmmmech:dunite.

Dunite is a geological primary resource. Its normative rock definition is retained alongside the lower residual olivine fractions of the studied altered powders.

### Assay-specific mechanism, controls and quantitative limits

evidence: supported. Targets: cmmmech:dunite.

The evidence supports biologically produced leaching chemistry under the reported laboratory conditions; contact necessity, additional active metabolites and mineral-specific release remain unproved.

### Exact reviewed bytes and CREATE history

provenance: supported. Targets: cmmmech:dunite.

Canonical inspect hashes, final byte comparison and actual CREATE session agree. Named validation and completed batch/history gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/dunite.yaml; Complete final YAML and linked CREATE sidecar | supports | All content and provenance inspected. Criticality is not asserted for this resource; no constituent-element designation is inherited. |
| search | /private/tmp/cmm-round18-cross-review/search.json; Exact DOI correction/retraction/erratum queries, related-source query and dedup-receipt.json | context_only | No affecting notice surfaced in the checked first-result sets. Related and reused publications are not assumed independent replication. |
| gates | /private/tmp/cmm-round18-gate-receipts.json; Completed receipt and final-batch.log, final-require.log, final-history.log | supports | All required gates finished with exit 0: 308 tests passed, 3 skipped; 138 records and 154 histories validated. Final target hashes match the initial canonical inspection. |
| identity | https://webapps.bgs.ac.uk/bgsrcs/rcs_details.cfm?code=DUN; BGS name and definition, code DUN | supports | Live BGS entry and retained HTML distinguish dunite rock from mineral species: more than 90% olivine in the olivine/pyroxene/hornblende assemblage. The record explicitly distinguishes this definition from strongly altered experimental deposit powders. |
| primary | https://doi.org/10.1038/s41598-025-99655-9; Full primary paper; Results, Methods, Limitations; Figures 2-8, particularly original rendered Figures 4, 6, 7 and 8 | supports | Independent full-text and figure checks support conditional liquid metal release, matched-initial-pH comparisons, the filtered/unfiltered null and the mutant comparison. Figure 8 estimates potential carbonation; it measures neither carbonate production nor net carbon removal. Post-leach pH and incomplete mass balance are explicit limitations. |
| supplement | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-025-99655-9/MediaObjects/41598_2025_99655_MOESM2_ESM.pdf; Figures S1-S5, Tables S1-S4, Note S1; original Figure S1 and Table S1 images | supports | Checked protocol, oxide/trace-element composition, cellulosic-hydrolysate metal blanks, stoppering null and poor/variable chromium release. Main/SI timing, feed/figure labels and attempt numbers conflict as recorded. Table S2 n.d. means not determined. Note S1 is proposed downstream chemistry. |
| workbook | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-025-99655-9/MediaObjects/41598_2025_99655_MOESM1_ESM.xlsx; Original ZIP/XML, all nine worksheet names; Figure 4 60%-pulp 72-h WT/GA rows; Figure 5 filtered rows; Figures 3&amp;7 censored cells | supports | Independently parsed original cells and dilution metadata. Three-row mean Mg concentrations at 60% pulp and 72 h are 4324.1225 and 1331.1208 mg/L after dilution, ratio 3.24848. This confirms about 3.25, not 2.25 as a ratio. Stale worksheet names, technical/biological replicate ambiguity and less-than-zero tokens are preserved. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=442&amp;mode=Info; Retained NCBI Taxonomy XML name and rank | supports | Taxon 442 is Gluconobacter oxydans at species rank; it does not identify the engineered derivative. |
| strain | https://www.ncbi.nlm.nih.gov/bioproject/761721; Retained BioProject XML ProjectID, organism and strain | supports | PRJNA761721 describes G. oxydans NRRL B-58 genome sequencing. This is contextual strain identity, not a genome assertion for the delta-pstS, P112:mgdh leaching derivative. |

## Limits And Additional Notes

- Reported phase fractions are author-assigned XRD proportions; no independent phase reanalysis or phase-specific release accounting was performed.
- Main/SI workbook labeling, initial growth duration, attempt numbering and replicate wording remain inconsistent. No precise long-duration attempt-to-feed yield is imported.
- Initially pH-matched controls do not match acid inventory or subsequent chemistry; the double mutant does not isolate either gene causally.
- Raw instrument recalibration and all statistical calculations were not reproduced. The selected ratio was independently recalculated; modeled carbonation is not demonstrated sequestration.
- Correction/conflict searches were bounded to stated query results, not an exhaustive proof of absence.
- Canonical inspect captured exact working-tree target, history and schema hashes before target assessment. All hashes were rechecked after completed batch gates. No source contradiction was silently repaired, and no new curation history event was invented for this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112143Z-dunite-round18-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Dunite
started_at: '2026-10-11T11:16:41Z'
finished_at: '2026-10-11T11:21:43Z'
reviewer:
  identity: Codex /root/round18_mineral_feeds
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A separate /root/round18_dunite agent authored the target and
    its CREATE history. Reviewer independently read primary methods, results, original
    figures/tables and identity authorities after canonical target inspection; no
    target changes were made. Shared worktree and source dossier access are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded resource identity and laboratory mechanism claims are supported.
  No actionable defect was identified in the inspected bytes. Source contradictions
  and experimental limits remain explicit.
source:
  git_revision: 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  state: working_tree
  inputs:
  - path: data/records/dunite.yaml
    sha256: 4ee783b7ec26bf8ce662fe6cdd6c73a5e6f18bd8742b135660676dac8fa1d166
    role: target
  - path: history/records/dunite/2026-10-11T111317Z-codex-75893c.yaml
    sha256: 40c81ceb2f365b9df7e8cabbd1a1be0908408b8e3832ab4c50decf02eecfae78
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields and linked CREATE history of the assigned final record,
    including resource boundary, assay conditions, controls, quantitative claims and
    limitations.
  selection: One assigned new maintained record in the round18 batch, reviewed against
    its frozen inspected hash.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:dunite
  exclusions:
  - target: Other corpus records, original instrument recalibration and industrial
      deployment
    reason: Related records and companion assay arms are contextual; no verdict beyond
      the assigned target or independent replication is asserted.
targets:
- target_id: cmmmech:dunite
  path: data/records/dunite.yaml
  label: Dunite
  kind: maintained
  ownership_note: Scientific changes belong in this maintained record; reviewed independently
    of its curator.
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/dunite.yaml data/records/spent-hydrodesulfurization-catalyst.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer observed terminal exit 0: Checked 2 record(s); 0 failed.'
  target_ids:
  - cmmmech:dunite
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-batch.log:
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 86.49s (0:01:26)

    Checked 138 record(s); 0 failed.

    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:dunite
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-require.log:
    Checked 138 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:dunite
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed and confirmed terminal completion; reviewer independently
    read completed receipt and all three logs. /private/tmp/cmm-round18-final-history.log:
    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:dunite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/dunite.yaml
  locator: Complete final YAML and linked CREATE sidecar
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: All content and provenance inspected. Criticality is not asserted for this
    resource; no constituent-element designation is inherited.
  snapshot_sha256: 4ee783b7ec26bf8ce662fe6cdd6c73a5e6f18bd8742b135660676dac8fa1d166
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round18-cross-review/search.json
  locator: Exact DOI correction/retraction/erratum queries, related-source query and
    dedup-receipt.json
  accessed_at: '2026-10-11T11:21:43Z'
  support: context_only
  summary: No affecting notice surfaced in the checked first-result sets. Related
    and reused publications are not assumed independent replication.
  snapshot_sha256: e9c9daf65089a5855c8afeabf303c80c2d9491cead1f4cfce314d7ba366898fe
  search_scope: Hidden and ignored files included with relevant symlinks followed
    across data, history, research, reviews, .claude and named round18 dunite/catalyst
    raw directories. Relevant binaries inspected separately. Search exit 0 and empty
    stderr; no machine-wide or exhaustive literature absence claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round18-gate-receipts.json
  locator: Completed receipt and final-batch.log, final-require.log, final-history.log
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: 'All required gates finished with exit 0: 308 tests passed, 3 skipped;
    138 records and 154 histories validated. Final target hashes match the initial
    canonical inspection.'
  snapshot_sha256: f77f5decb184fd5e6544b9d89c9699a95621e2a83749524526f6283fb5be2f66
- evidence_id: identity
  kind: authority
  reference: https://webapps.bgs.ac.uk/bgsrcs/rcs_details.cfm?code=DUN
  locator: BGS name and definition, code DUN
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: 'Live BGS entry and retained HTML distinguish dunite rock from mineral
    species: more than 90% olivine in the olivine/pyroxene/hornblende assemblage.
    The record explicitly distinguishes this definition from strongly altered experimental
    deposit powders.'
  snapshot_sha256: f1ab8cd376c9c60717f5b6e6363be0ed48f684363a48cae33d94e7bff69b8207
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-025-99655-9
  locator: Full primary paper; Results, Methods, Limitations; Figures 2-8, particularly
    original rendered Figures 4, 6, 7 and 8
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: Independent full-text and figure checks support conditional liquid metal
    release, matched-initial-pH comparisons, the filtered/unfiltered null and the
    mutant comparison. Figure 8 estimates potential carbonation; it measures neither
    carbonate production nor net carbon removal. Post-leach pH and incomplete mass
    balance are explicit limitations.
  snapshot_sha256: f2df07204a7ae1099e962fcd8c3b644ea1b1a43020114009012682b1edc48acc
- evidence_id: supplement
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-025-99655-9/MediaObjects/41598_2025_99655_MOESM2_ESM.pdf
  locator: Figures S1-S5, Tables S1-S4, Note S1; original Figure S1 and Table S1 images
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: Checked protocol, oxide/trace-element composition, cellulosic-hydrolysate
    metal blanks, stoppering null and poor/variable chromium release. Main/SI timing,
    feed/figure labels and attempt numbers conflict as recorded. Table S2 n.d. means
    not determined. Note S1 is proposed downstream chemistry.
  snapshot_sha256: 7a29b046f02a5b9336d722eb44f764fcd46a4cf3735de8e1318c1614d0155bef
- evidence_id: workbook
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-025-99655-9/MediaObjects/41598_2025_99655_MOESM1_ESM.xlsx
  locator: Original ZIP/XML, all nine worksheet names; Figure 4 60%-pulp 72-h WT/GA
    rows; Figure 5 filtered rows; Figures 3&7 censored cells
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: Independently parsed original cells and dilution metadata. Three-row mean
    Mg concentrations at 60% pulp and 72 h are 4324.1225 and 1331.1208 mg/L after
    dilution, ratio 3.24848. This confirms about 3.25, not 2.25 as a ratio. Stale
    worksheet names, technical/biological replicate ambiguity and less-than-zero tokens
    are preserved.
  snapshot_sha256: 64bf48b7543ef39721548c7b3f2fe48abb16d92fd3a6670c3a830428a84b30d2
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=442&mode=Info
  locator: Retained NCBI Taxonomy XML name and rank
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: Taxon 442 is Gluconobacter oxydans at species rank; it does not identify
    the engineered derivative.
  snapshot_sha256: 89f99310d5d7c407ef81f67b1446286364362a850c9e49e3e1d4518822fb9c5f
- evidence_id: strain
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/bioproject/761721
  locator: Retained BioProject XML ProjectID, organism and strain
  accessed_at: '2026-10-11T11:21:43Z'
  support: supports
  summary: PRJNA761721 describes G. oxydans NRRL B-58 genome sequencing. This is contextual
    strain identity, not a genome assertion for the delta-pstS, P112:mgdh leaching
    derivative.
  snapshot_sha256: 627bf2ab12a9a1622894dcb9bad6430fc2e42e0af2b49700ea7e58c1ca011bf5
assessments:
- assessment_id: identity
  area: identity
  topic: Resource, organism and criticality boundaries
  outcome: supported
  summary: Dunite is a geological primary resource. Its normative rock definition
    is retained alongside the lower residual olivine fractions of the studied altered
    powders.
  target_ids:
  - cmmmech:dunite
  evidence_ids:
  - record
  - primary
  - search
  - identity
  dimensions:
  - name: material_kind
    value: primary_resource
    definition: Material identity remains separate from constituent elements, mineral
      phases, commercial products and other resource types.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority/jurisdiction/list/edition designation is inherited from
      constituent elements or generic source terminology.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Assay-specific mechanism, controls and quantitative limits
  outcome: supported
  summary: The evidence supports biologically produced leaching chemistry under the
    reported laboratory conditions; contact necessity, additional active metabolites
    and mineral-specific release remain unproved.
  target_ids:
  - cmmmech:dunite
  evidence_ids:
  - record
  - primary
  - taxon
  - workbook
  - supplement
  - strain
  dimensions:
  - name: organism_and_biomass
    value: Gluconobacter oxydans NRRL B-58 and separately its delta-pstS, P112:mgdh
      derivative; cell-containing and 0.22-micrometre-filtered biolixiviant
    definition: Biolixiviant production is biological; cell presence during leaching
      is not shown necessary. Species and BioProject identifiers have explicit scopes.
    evidence_ids:
    - primary
    - taxon
    - strain
  - name: substrate_and_conditions
    value: Milled DUN-1/2/3 deposit powders with distinct olivine/serpentine phase
      proportions; principal assay 1% wt/vol, 22 degrees C, 24 h
    definition: Altered deposit feed is not phase-pure dunite or pure forsterite.
      High-pulp DUN-2 comparisons do not isolate pulp density across feeds.
    evidence_ids:
    - primary
    - supplement
  - name: controls_and_fraction
    value: Water, sugar-water or initially pH-matched gluconic acid according to arm;
      0.45-micrometre-filtered ICP-MS aliquot
    definition: Equal initial pH does not equal acid inventory or trajectory. Extraction
      uses bulk-feed element content times pulp density, not mineral-specific flux
      or isolated recovery.
    evidence_ids:
    - primary
    - workbook
  - name: outcome_and_scale
    value: Laboratory liquid metal mobilization; modeled future carbonation potential
    definition: No industrial deployment, isolated product, verified anoxia, gene-specific
      causal allocation or measured net atmospheric removal.
    evidence_ids:
    - primary
    - supplement
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed bytes and CREATE history
  outcome: supported
  summary: Canonical inspect hashes, final byte comparison and actual CREATE session
    agree. Named validation and completed batch/history gates passed.
  target_ids:
  - cmmmech:dunite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Reported phase fractions are author-assigned XRD proportions; no independent phase
  reanalysis or phase-specific release accounting was performed.
- Main/SI workbook labeling, initial growth duration, attempt numbering and replicate
  wording remain inconsistent. No precise long-duration attempt-to-feed yield is imported.
- Initially pH-matched controls do not match acid inventory or subsequent chemistry;
  the double mutant does not isolate either gene causally.
- Raw instrument recalibration and all statistical calculations were not reproduced.
  The selected ratio was independently recalculated; modeled carbonation is not demonstrated
  sequestration.
- Correction/conflict searches were bounded to stated query results, not an exhaustive
  proof of absence.
tags:
- round18
- independent
- scientific-review
- resource
notes:
- Canonical inspect captured exact working-tree target, history and schema hashes
  before target assessment. All hashes were rechecked after completed batch gates.
  No source contradiction was silently repaired, and no new curation history event
  was invented for this review.
```
