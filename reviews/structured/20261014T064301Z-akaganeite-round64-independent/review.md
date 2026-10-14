# Independent scientific review of conditional akaganeite reduction

- Review: 20261014T064301Z-akaganeite-round64-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T06:29:22.236446Z
- Finished UTC: 2026-10-14T06:43:01.885325Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record supports conditional laboratory Fe(III) reduction in XRD-assigned akaganeite by PCA and deletion mutants. It preserves inferred mineral potential, acid-extractable rather than dissolved-only Fe(II), variable pH/autoclave phenotypes and nonunique comparative product assignments. No supported curation defect was found.

## Scope And Provenance

Field-by-field review of the exact assigned mineral record and its linked history and claim-bearing sources.

Selection: Assigned frozen record and canonical inspect capture before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:akaganeite | data/records/akaganeite.yaml | maintained | Akaganeite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| named | passed | True | cmmmech:akaganeite | Reviewer execution:1 record,0 failed. |
| history | passed | True | cmmmech:akaganeite | Reviewer execution:342 histories,0 errors. |
| Batch gate | passed | True | cmmmech:akaganeite | Coordinator execution 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00; exit0. |
| Batch gate | passed | True | cmmmech:akaganeite | Coordinator execution 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00; exit0. |

## Scientific And Domain Assessments

### Mineral and organism grounding

identity: supported. Targets: cmmmech:akaganeite.

Species identity, material boundary and PCA grounding are accurate.

### Substrate, conditions and controls

evidence: supported. Targets: cmmmech:akaganeite.

Record separates experiment preparation, culture and analytical extraction and preserves conditional phenotypes.

### Reduction measurement and interpretation

quantity: supported. Targets: cmmmech:akaganeite.

Measured acid-extractable FeII and source-inferred pathway/potential interpretation are correctly distinguished.

### Contradictory and comparative boundaries

evidence: supported. Targets: cmmmech:akaganeite.

Different Ax17 assay and analytical signals are contextual; extraction null is not universal transformation null.

### Evidence and history integrity

provenance: supported. Targets: cmmmech:akaganeite.

Exact frozen record and linked CREATE history are covered by named checks; bounded source searches retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/akaganeite.yaml; Entire frozen record | supports | All fields, identifiers, evidence explanations and provenance read. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF pages 1-2 definitions and page 5 Akaganeite row | supports | Renamed species, IMA1962-004, formula (FeIII,NiII)8(OH,O)16Cl1.25·nH2O. Original page5 visually inspected; introductory definitions read. Synthetic beta-FeOOH naming does not establish exact ideal composition. |
| primary | https://doi.org/10.1038/ismej.2016.146; Methods pp742-744, Results pp745-749, Table1 and Figure2 | supports | Relevant methods/results read in complete 12-page original; original Table1 and Figure2 visually inspected. Fresh/autoclaved XRD-assigned feed, acetate cultures, pH6.8/6.3 and WT/delta-imcH/delta-cbcL show conditional acid-extractable FeII. Cell-free 14-day control null, triplicate culture summaries, duplicate incubation repetitions. Figure1 soluble-citrate voltage cannot be assigned to mineral. |
| limits | https://doi.org/10.1038/ismej.2016.146; Mineral preparation, ferrozine extraction and Discussion | partial | 0.5N HCl extraction at23-25C is not culture temperature. Nearby20mM loading follows goethite preparation. Mineral potential not directly measurable; XRD similarity does not exclude surface/aggregation changes. Complementation is cited from prior studies, not performed as Figure2 control. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=243231; TaxId, ScientificName and Rank in retained live XML | supports | 243231 is Geobacter sulfurreducens PCA, strain rank; does not individually identify deletion mutants. |
| collection | https://www.atcc.org/products/51573; Designation PCA, accession51573 | supports | Independently read retained authority HTML text; confirms PCA accession printed imperfectly in Table1. |
| comparative | https://doi.org/10.3389/fmicb.2023.1272245; Methods; akaganeite/lepidocrocite results; Discussion; Figures5-7 and SupplementS8-S11 | context_only | Read retained original XML sections and personally inspected figures5/6/7 acquired from publisher plus original supplement pages12-15. Ax17 at55C has extraction null relative to controls, amorphous iron-rich spheres and nonunique ferrous/ferric spectral components; heated abiotic controls also change. No direct PCA replication or unique product yield. |
| supplement | https://doi.org/10.3389/fmicb.2023.1272245; Data Sheet1, FiguresS8-S11, PDF pages12-15 | partial | Visually inspected original spectral panels and captions; multiple fitting assignments remain possible. |
| metadata | https://api.crossref.org/works/10.1038/ismej.2016.146; DOI/title, update-to and relation fields | supports | DOI/title agree. No update-to in inspected response; related preprint recorded. This does not prove absence of corrections. |
| notices | Web search and Nature article open; First returned sets of two exact queries | context_only | Search did not identify a correction/retraction in bounded returned results. Nature article open inaccessible. Later CbcBA2021, ImcH2023 and CbcL2022 papers were identified but not fully reassessed. No global absence assertion. |
| dedup | /private/tmp/cmm-round64-akaganeite-review/dedup.log; Complete scoped local output | context_only | Current target/history and prior contextual mentions were inspected; no second maintained akaganeite identity found in named roots. Curator dossier separately covers wider source inventory. |
| history | history/records/akaganeite/2026-10-14T062506Z-codex-282c73.yaml; Whole canonical sidecar and inline event | supports | Actual curator CREATE session and target agree; separate linked sidecar and inline event retained. |
| checks | /private/tmp/cmm-round64-akaganeite-review/checks.json; Actual named and trusted-base history receipts | supports | Reviewer ran named validation1/0 and trusted-base history342/0. |
| batch | /private/tmp/cmm-round64-final-gates.json; Coordinator receipt and final-gates.log | supports | Actual batch checks exited0 before saving this bundle. Log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99. These are structural gates, not scientific truth. |

## Limits And Additional Notes

- Mineral redox potential and molecular electron-transfer roles are interpretations of the 2017 experiments, not direct akaganeite voltage or purified-protein measurements. Later protein studies were not fully reassessed.
- Mineral incubation temperature and quantitative initial akaganeite Fe loading were not stated in the inspected methods; extraction temperature and goethite loading were not transferred.
- The Ax17 comparison differs in organism, medium, temperature and extraction. An oxalate-extraction null does not exclude transformation; ferrous/ferric spectral components do not uniquely identify a recovered crystalline product.
- Correction/retraction and duplicate searches cover explicitly documented queries and roots only; no literature-wide clearance is claimed.
- Corrections made by this reviewer: none. Record/history/dossier frozen bytes are unchanged. Earlier batch checks precede this immutable bundle and do not validate the bundle itself.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T064301Z-akaganeite-round64-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of conditional akaganeite reduction
started_at: '2026-10-14T06:29:22.236446Z'
finished_at: '2026-10-14T06:43:01.885325Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/round64_iron. Reviewer did
    not author the record, history or source dossier; independently inspected primary
    methods/results, relevant original figures and authority entries. Reviewer coordinated
    batch checks and authored README/pages.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record supports conditional laboratory Fe(III) reduction in XRD-assigned
  akaganeite by PCA and deletion mutants. It preserves inferred mineral potential,
  acid-extractable rather than dissolved-only Fe(II), variable pH/autoclave phenotypes
  and nonunique comparative product assignments. No supported curation defect was
  found.
source:
  git_revision: 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  state: working_tree
  inputs:
  - path: data/records/akaganeite.yaml
    sha256: a567761b180d080e7c2310b652338de4cf77d3e7b5db519c3a8d4959048d33e8
    role: target
  - path: history/records/akaganeite/2026-10-14T062506Z-codex-282c73.yaml
    sha256: 1a11b5e12b01578904968ae05dc6fdb15d3b28021e1b41bbed4c44f52fe87332
    role: context
  - path: research/sources/round64-iron/20261014T062830Z-source-investigation.json
    sha256: 1240f681667b6eb96a4d55b6d07d4f7664acb905987240579158d45b9e021f39
    role: context
  - path: research/sources/round64-iron/20261014T062830Z-source-investigation.md
    sha256: dbc148fd48d1c9f060b9ff03b5ce720f8ea5d3631f86fafcdb617551cc6833a4
    role: context
scope:
  description: Field-by-field review of the exact assigned mineral record and its
    linked history and claim-bearing sources.
  selection: Assigned frozen record and canonical inspect capture before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:akaganeite
  exclusions:
  - target: New mechanisms from subsequent ImcH/CbcL/CbcBA papers
    reason: Search metadata identified later mechanistic studies, but full originals
      were not reassessed and their measurements are not imported.
targets:
- target_id: cmmmech:akaganeite
  path: data/records/akaganeite.yaml
  label: Akaganeite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/akaganeite.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: named
  command: uv run --locked cmmmech validate data/records/akaganeite.yaml
  status: passed
  required: true
  summary: Reviewer execution:1 record,0 failed.
  target_ids:
  - cmmmech:akaganeite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
- check_id: history
  name: history
  command: uv run --locked cmmmech validate-history --base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  status: passed
  required: true
  summary: Reviewer execution:342 histories,0 errors.
  target_ids:
  - cmmmech:akaganeite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
- check_id: batch0
  name: Batch gate
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00;
    exit0.
  target_ids:
  - cmmmech:akaganeite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch1
  name: Batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00;
    exit0.
  target_ids:
  - cmmmech:akaganeite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/akaganeite.yaml
  locator: Entire frozen record
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: All fields, identifiers, evidence explanations and provenance read.
  snapshot_sha256: a567761b180d080e7c2310b652338de4cf77d3e7b5db519c3a8d4959048d33e8
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF pages 1-2 definitions and page 5 Akaganeite row
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Renamed species, IMA1962-004, formula (FeIII,NiII)8(OH,O)16Cl1.25·nH2O.
    Original page5 visually inspected; introductory definitions read. Synthetic beta-FeOOH
    naming does not establish exact ideal composition.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1038/ismej.2016.146
  locator: Methods pp742-744, Results pp745-749, Table1 and Figure2
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Relevant methods/results read in complete 12-page original; original Table1
    and Figure2 visually inspected. Fresh/autoclaved XRD-assigned feed, acetate cultures,
    pH6.8/6.3 and WT/delta-imcH/delta-cbcL show conditional acid-extractable FeII.
    Cell-free 14-day control null, triplicate culture summaries, duplicate incubation
    repetitions. Figure1 soluble-citrate voltage cannot be assigned to mineral.
  snapshot_sha256: 137245330b6e38917a00d087510e670a870acf605a66b5ff38b59380b9c77ebe
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1038/ismej.2016.146
  locator: Mineral preparation, ferrozine extraction and Discussion
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: partial
  summary: 0.5N HCl extraction at23-25C is not culture temperature. Nearby20mM loading
    follows goethite preparation. Mineral potential not directly measurable; XRD similarity
    does not exclude surface/aggregation changes. Complementation is cited from prior
    studies, not performed as Figure2 control.
  snapshot_sha256: 137245330b6e38917a00d087510e670a870acf605a66b5ff38b59380b9c77ebe
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=243231
  locator: TaxId, ScientificName and Rank in retained live XML
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: 243231 is Geobacter sulfurreducens PCA, strain rank; does not individually
    identify deletion mutants.
  snapshot_sha256: f1291f188fae1b43a82d2f75e98d90aa41434ef36115f217a9485629eebb2736
- evidence_id: collection
  kind: authority
  reference: https://www.atcc.org/products/51573
  locator: Designation PCA, accession51573
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Independently read retained authority HTML text; confirms PCA accession
    printed imperfectly in Table1.
  snapshot_sha256: 6f4455a170b95466dd2aac6e48c89a40909ef9e13332b789639e04c0593e7372
- evidence_id: comparative
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1272245
  locator: Methods; akaganeite/lepidocrocite results; Discussion; Figures5-7 and SupplementS8-S11
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: context_only
  summary: Read retained original XML sections and personally inspected figures5/6/7
    acquired from publisher plus original supplement pages12-15. Ax17 at55C has extraction
    null relative to controls, amorphous iron-rich spheres and nonunique ferrous/ferric
    spectral components; heated abiotic controls also change. No direct PCA replication
    or unique product yield.
  snapshot_sha256: 17dd49089580015c98d705a1f6ceb239da3377ce85c2e5369a52cd0a4dd7f4c9
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1272245
  locator: Data Sheet1, FiguresS8-S11, PDF pages12-15
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: partial
  summary: Visually inspected original spectral panels and captions; multiple fitting
    assignments remain possible.
  snapshot_sha256: f4d4514592189e6c68ecf0466c858919e946208c2ec71a6fb4c2834793b43455
- evidence_id: metadata
  kind: database
  reference: https://api.crossref.org/works/10.1038/ismej.2016.146
  locator: DOI/title, update-to and relation fields
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: DOI/title agree. No update-to in inspected response; related preprint recorded.
    This does not prove absence of corrections.
  snapshot_sha256: 9083e50d39476e79d6aac4378b67ec367afb12537b4e10daf884fee4949d89ca
- evidence_id: notices
  kind: search
  reference: Web search and Nature article open
  locator: First returned sets of two exact queries
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: context_only
  summary: Search did not identify a correction/retraction in bounded returned results.
    Nature article open inaccessible. Later CbcBA2021, ImcH2023 and CbcL2022 papers
    were identified but not fully reassessed. No global absence assertion.
  search_scope: 'Queries: "10.1038/ismej.2016.146" correction retraction akaganeite;
    "Geobacter sulfurreducens" akaganeite imcH cbcL reduction contradiction control.
    First result sets, no pagination/date/domain restrictions.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round64-akaganeite-review/dedup.log
  locator: Complete scoped local output
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: context_only
  summary: Current target/history and prior contextual mentions were inspected; no
    second maintained akaganeite identity found in named roots. Curator dossier separately
    covers wider source inventory.
  snapshot_sha256: 4eac3749e60ebe8be0eb0b6d4d3fffb26a4c11f7dfa4d5e806d6de33a50d7fa1
  search_scope: rg --no-ignore --hidden --follow -n -i akaganeite|1962-004|ismej.2016.146
    data/records history/records reviews/structured; hidden/ignored included, symlinks
    followed; no other roots exhaustively searched.
- evidence_id: history
  kind: record_content
  reference: history/records/akaganeite/2026-10-14T062506Z-codex-282c73.yaml
  locator: Whole canonical sidecar and inline event
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Actual curator CREATE session and target agree; separate linked sidecar
    and inline event retained.
  snapshot_sha256: 1a11b5e12b01578904968ae05dc6fdb15d3b28021e1b41bbed4c44f52fe87332
- evidence_id: checks
  kind: validation
  reference: /private/tmp/cmm-round64-akaganeite-review/checks.json
  locator: Actual named and trusted-base history receipts
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Reviewer ran named validation1/0 and trusted-base history342/0.
  snapshot_sha256: 28693873d26abdd412ae338a19422b66bf463b66440efcfe3307a5a157b5c179
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round64-final-gates.json
  locator: Coordinator receipt and final-gates.log
  accessed_at: '2026-10-14T06:43:01.885325Z'
  support: supports
  summary: Actual batch checks exited0 before saving this bundle. Log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99.
    These are structural gates, not scientific truth.
  snapshot_sha256: f2af92147f4a25ed646c60e50766925356e9f605d68c9526b0ee195301b4ee5f
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral and organism grounding
  outcome: supported
  summary: Species identity, material boundary and PCA grounding are accurate.
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - record
  - ima
  - taxonomy
  - collection
  dimensions:
  - name: material_form
    value: Akaganeite mineral; synthetic XRD-assigned beta-FeOOH
    definition: Not iron element, ore commodity or inferred ideal-composition feed
    evidence_ids:
    - record
    - ima
    - taxonomy
    - collection
  - name: criticality
    value: No jurisdiction/list/edition assertion
    definition: No inherited constituent criticality; omission is not noncritical
      status
    evidence_ids:
    - record
    - ima
    - taxonomy
    - collection
  - name: organism
    value: Living PCA WT and engineered deletion mutants
    definition: Taxon243231 grounds parental strain, not each mutant
    evidence_ids:
    - record
    - ima
    - taxonomy
    - collection
- assessment_id: system
  area: evidence
  topic: Substrate, conditions and controls
  outcome: supported
  summary: Record separates experiment preparation, culture and analytical extraction
    and preserves conditional phenotypes.
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - primary
  - limits
  dimensions:
  - name: substrate
    value: Fresh FeCl3/NaOH synthetic phase, washed and used within24h
    definition: XRD assignment does not quantify Ni/Cl stoichiometry
    evidence_ids:
    - primary
    - limits
  - name: pretreatment
    value: Fresh versus20min autoclave121C
    definition: Surface changes unresolved despite similar XRD
    evidence_ids:
    - primary
    - limits
  - name: conditions
    value: Acetate/NB basal medium; pH6.8 or6.3;14–15day figures
    definition: Culture temperature not imported from extraction
    evidence_ids:
    - primary
    - limits
  - name: controls
    value: Cell-free14day null; WT/deletions; Table1 growth context
    definition: Not universal knockout inability or same-figure complementation
    evidence_ids:
    - primary
    - limits
- assessment_id: outcome
  area: quantity
  topic: Reduction measurement and interpretation
  outcome: supported
  summary: Measured acid-extractable FeII and source-inferred pathway/potential interpretation
    are correctly distinguished.
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - primary
  - limits
  - comparative
  - supplement
  dimensions:
  - name: outcome
    value: Acid-extractable FeII; timing and extent differ across arms
    definition: Not dissolved-only fraction or total feed conversion
    evidence_ids:
    - primary
    - limits
    - comparative
    - supplement
  - name: mechanism
    value: Condition-dependent electron-transfer pathway association
    definition: Direct mineral voltage/protein electron flow not measured in these2017
      experiments
    evidence_ids:
    - primary
    - limits
    - comparative
    - supplement
  - name: deployment
    value: Laboratory cultures
    definition: No isolated mineral recovery, elemental iron production or industrial
      deployment
    evidence_ids:
    - primary
    - limits
    - comparative
    - supplement
- assessment_id: context
  area: evidence
  topic: Contradictory and comparative boundaries
  outcome: supported
  summary: Different Ax17 assay and analytical signals are contextual; extraction
    null is not universal transformation null.
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - comparative
  - supplement
  - notices
  dimensions:
  - name: uncertainty
    value: Amorphous spheres, ferrous/ferric components, nonunique fits
    definition: Does not establish one pure crystalline product or refute PCA experiment
    evidence_ids:
    - comparative
    - supplement
    - notices
- assessment_id: provenance
  area: provenance
  topic: Evidence and history integrity
  outcome: supported
  summary: Exact frozen record and linked CREATE history are covered by named checks;
    bounded source searches retained.
  target_ids:
  - cmmmech:akaganeite
  evidence_ids:
  - record
  - history
  - checks
  - batch
  - dedup
  dimensions: []
findings: []
actions: []
limitations:
- Mineral redox potential and molecular electron-transfer roles are interpretations
  of the 2017 experiments, not direct akaganeite voltage or purified-protein measurements.
  Later protein studies were not fully reassessed.
- Mineral incubation temperature and quantitative initial akaganeite Fe loading were
  not stated in the inspected methods; extraction temperature and goethite loading
  were not transferred.
- The Ax17 comparison differs in organism, medium, temperature and extraction. An
  oxalate-extraction null does not exclude transformation; ferrous/ferric spectral
  components do not uniquely identify a recovered crystalline product.
- Correction/retraction and duplicate searches cover explicitly documented queries
  and roots only; no literature-wide clearance is claimed.
notes:
- 'Corrections made by this reviewer: none. Record/history/dossier frozen bytes are
  unchanged. Earlier batch checks precede this immutable bundle and do not validate
  the bundle itself.'
tags:
- round64
- independent
- akaganeite
```
