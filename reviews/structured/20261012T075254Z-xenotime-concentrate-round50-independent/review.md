# Independent scientific review of xenotime concentrate

- Review: 20261012T075254Z-xenotime-concentrate-round50-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T07:44:13Z
- Finished UTC: 2026-10-12T07:52:54Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Mixed-feed bacterial mobilization is supported within laboratory/control/analytical limits. Source contradictions, unverified isolate identity, unisolated products and conditional phase-specific dissolution models are preserved. No corrective record finding.

## Scope And Provenance

Whole frozen xenotime-concentrate record and CREATE provenance, all maintained biological/material/outcome claims against main/SI and current taxon mapping.

Selection: Independent peer review of the newly curated mixed primary resource.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 98e787e8d61593797aef1ed29840b2315a0cc6e5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:xenotime-concentrate | data/records/xenotime-concentrate.yaml | maintained | Xenotime concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-file validation | passed | True | cmmmech:xenotime-concentrate | Actually completed 1 record / 0 failed; retained log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Coordinator corrected cohort batch | passed | True | cmmmech:xenotime-concentrate | Actually completed by coordinator; independently read and SHA256-verified raw log dcc7d1261abfca630c5a13f9ed142b85bb1462960ff410d2072f7b14d4c3908a. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 166.09s (0:02:46)<br>Checked 246 record(s); 0 failed.<br>Checked 291 history record(s); 0 error(s).<br> |
| Coordinator corrected cohort nonempty | passed | True | cmmmech:xenotime-concentrate | Actually completed by coordinator; independently read and SHA256-verified raw log 5599312a3ee08a5df1b1f5d52f06e26aec1513ffe4bc0a5e4ef60dd00ea6e0aa. Checked 246 record(s); 0 failed.<br> |
| Coordinator corrected cohort history | passed | True | cmmmech:xenotime-concentrate | Actually completed by coordinator; independently read and SHA256-verified raw log bf614125e66d58201aeb2a712034842703a4c3090392cb57e00cd260c9c6e79a. Checked 291 history record(s); 0 error(s).<br> |
| Coordinator corrected cohort render-check | passed | False | cmmmech:xenotime-concentrate | Actually completed by coordinator; independently read and SHA256-verified raw log be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Mixed natural feed versus species or waste

identity: supported. Targets: cmmmech:xenotime-concentrate.

The primary-resource owner is scientifically distinct and appropriately bounded.

Source-assigned82.0 wt% xenotime and 2.7 wt% monazite are particle-count/density estimates. Concentrate origin/supplier is unspecified; Renju is the isolate source. The article mixes other phases and does not establish a pure mineral product, commodity or secondary waste. Constituent criticality is not inherited.

### Living culture, species mapping and isolate uncertainty

evidence: supported. Targets: cmmmech:xenotime-concentrate.

Organism and experimental scope are supported without a fabricated isolate accession.

Exponentially harvested, washed living cells identified by authors as B. thuringiensis; initial ~1e6 CFU/mL. NCBI 1428 maps the species only. Methods 2.2 states BLAST comparison but supplies no verifiable accession in reviewed main/SI. CFU excludes attached cells.

### Controlled laboratory mobilization and causal limits

evidence: supported. Targets: cmmmech:xenotime-concentrate.

Reported bacterial enhancement is supported against corresponding abiotic controls.

0.5 g/100 mL, 48–74 micrometre feed, 25–28 C, 180 rpm, 30 days, initial pH 6 with or without 20 mM MES; feed biotic / feed abiotic / cells-only arms. Replicate numbers accurately preserved. Acidification and buffered release plus96 h, 1 mM acid tests support proton/ligand contributions but not each metabolite causal share.96 h chemical tests do not reproduce30-day pH trajectories.

### Aqueous concentration versus mineral-specific modeled losses

evidence: supported. Targets: cmmmech:xenotime-concentrate.

Units, endpoints and conditional models are accurately distinguished.

Figure 2 / ~716 micrograms/L day 15 unbuffered and ~343 micrograms/L day 30 buffered are filtered aqueous concentrations, not recovered mass or cumulative extraction. Precipitation changes solution values. Main Table 3 percentages are two-source inferred dissolutions;Table S7 / Text S1 reuse whole-concentrate area. No isolated REE product or species-general kinetic ratio asserted.

### Source contradictions and unidentified precipitates

evidence: supported. Targets: cmmmech:xenotime-concentrate.

The record retains the material source conflicts and avoids their silent correction.

Personally confirmed Figure 5 Exp-Control caption versus Exp-Bt legend;0.22 mm versus micrometre filters;P2O3/U2O3 labels;Figure S1 duplicated card;S3/S4Yb/Lu mismatch;TiO2 nonclosure;above-range Y;SI contents/caption order;granite wording. Figure 7 REE/P signals lack mineralogical identification, so rhabdophane/churchite remain proposals. The dossier also notesTable 3 rounding and Y-O/Ce-O bond-energy contradiction, neither promoted as causal proof.

### Current exact-byte review and history

provenance: supported. Targets: cmmmech:xenotime-concentrate.

Current target/history/dossiers and validation receipts are bound and consistent.

Native inspect preceded target judgment and explicitly captured record, CREATE, both dossiers, schema. Curator and reviewer are different agents. Raw-data statistical reproduction was not performed. No record edit or history event was added by reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/xenotime-concentrate.yaml; Whole native-inspected target | supports | Distinct primary-resource owner, five source evidence statements, conditions and explicit uncertainties checked field by field. |
| main | https://doi.org/10.1016/j.chemgeo.2024.122186; Complete GFZ 56-page postprint; Methods2.1-2.5, Results3.1-3.6, Discussion4.1-4.4, conclusion; all Figures 1–7 and Tables 1–3 personally viewed on PDF pages 17, 19, 22, 24, 25, 26, 36, 55, 56. | supports | Read complete main scientific text and original graphics. Mixed feed, laboratory bacterial/abiotic/cells-only arms, observed filtered concentrations, acid profiles and separate96 h chemical assays support the scoped mechanism. Whole 56-page visual inspection is not claimed. |
| supplement | https://ars.els-cdn.com/content/image/1-s2.0-S0009254124002663-mmc1.pdf; All 16 original pages; Figures S1–S7, Tables S1–S8, Text S1, actual captions compared with contents list. | supports | Source identity matches main title/authors. Independently verified mixed phases, particle/density-derived fractions, model equations and discrepancies in card numbers, Yb/Lu tables, numbering and bond-energy explanation. Source-assigned phases and rates remain qualified. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1428&amp;mode=Info; Live current-name/rank/lineage returned 2026-10-12; 1428 species in Bacillus cereus group. | supports | Species label/identifier resolves. It cannot identify the particular Renju isolate without deposited sequence/strain accession; record retains this limit. |
| artifacts | /private/tmp/cmm-round50-xenotime-independent/evidence-check.json; All 99 declared curator artifact hashes independently recomputed; original graphics inspected within recorded scope. | supports | Artifacts match the handoff. This is independent examination of retained originals, not an independent download of every artifact or reanalysis of unacquired Mendeley raw data. |
| dedup | /private/tmp/cmm-round50-xenotime-independent/dedup.log; Exact DOI 122186 / PII and xenotime-concentrate text search over current scientific directories. | supports | Hits identify this resource and current source handoffs; concurrently curated xenotime-(Y)/monazite-(Ce) are distinct mineral owners. Broader author raw-root receipt reviewed with its declared missing/binary limits, not rerun as machine-wide search. |
| notices | /private/tmp/cmm-round50-xenotime-independent/web-evidence.json; Exact DOI plus correction/erratum/retraction and exact-title correction searches; live DOI/NCBI opens. | supports | Returned bounded sets reveal no affecting formal notice. DOI reader itself errored while GFZ original metadata is available; no universal no-notice claim or raw-data replication is made. |
| history | history/records/xenotime-concentrate/2026-10-12T074155Z-codex-66bb20.yaml; Actual CREATE session plus distinct inline curation event. | supports | Target, timestamp, actor GPT-6 / codex and event details match the new owner and completed work; no prior history rewritten. |
| gates | /private/tmp/cmm-round50-corrected-terminal.json; Four completed corrected cohort commands; all log hashes independently checked. | supports | Named-file and final cohort structural checks passed. Offline validity is separate from this scientific evidence assessment. |

## Limits And Additional Notes

- Author-assigned isolate species maps toNCBI 1428, but sequence/strain identity is not independently established.
- Measured aqueous mobilization includes possible re-sorption/precipitation; separate phase losses and apparent rates are conditional models, not isolated-product recovery.
- Source composition/unit/caption inconsistencies remain explicit; no new closed balance or silent repaired source data.
- Complete primary scientific text and relevant original main graphics/all SI were inspected; not all 56 main pages were visually inspected.
- Mendeley raw files and statistical reproduction are outside this completed record review; notices/dedup searches are bounded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T075254Z-xenotime-concentrate-round50-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of xenotime concentrate
started_at: '2026-10-12T07:44:13Z'
finished_at: '2026-10-12T07:52:54Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Peer /root/round43_hardmetal authored xenotime concentrate,
    history and source dossier. Reviewer authored separate indite only, captured explicit
    native target/context hashes before judgment, independently inspected the actual
    main/SI evidence and identifiers, and did not edit this record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Mixed-feed bacterial mobilization is supported within laboratory/control/analytical
  limits. Source contradictions, unverified isolate identity, unisolated products
  and conditional phase-specific dissolution models are preserved. No corrective record
  finding.
source:
  git_revision: 98e787e8d61593797aef1ed29840b2315a0cc6e5
  state: working_tree
  inputs:
  - path: data/records/xenotime-concentrate.yaml
    sha256: 8e1d30e8c05053055fc352625e894a6575f3ed288c5c702d0aff702cdb9290ea
    role: target
  - path: history/records/xenotime-concentrate/2026-10-12T074155Z-codex-66bb20.yaml
    sha256: 87c774cecb3f231387c6f8dfd604b7c39cd0b5c2bfeb1add3d85b3355cb2b5a1
    role: context
  - path: research/sources/round50-xenotime-feed/20261012T074339Z-source-investigation.json
    sha256: ca6c84eadcf08e1d6bdeb339d56a4ef1186b1ec5c5085ae9ad0e6ba67d412ad6
    role: context
  - path: research/sources/round50-xenotime-feed/20261012T074339Z-source-investigation.md
    sha256: 374b2a53f2a113ba2a675510d4a61fab62d10a391f047395ee4f7f0f669dd120
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:xenotime-concentrate
  path: data/records/xenotime-concentrate.yaml
  label: Xenotime concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/xenotime-concentrate.yaml
    role: scientific_record
scope:
  description: Whole frozen xenotime-concentrate record and CREATE provenance, all
    maintained biological/material/outcome claims against main/SI and current taxon
    mapping.
  selection: Independent peer review of the newly curated mixed primary resource.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:xenotime-concentrate
  exclusions:
  - target: Unacquired Mendeley raw-data files and reproduction of statistics
    reason: Full primary/SI support the bounded claims; raw-data reanalysis and independent
      replication are not claimed.
  - target: Global literature completeness and other mineral owners
    reason: Bounded searches and this one record only; species records require their
      own independent reviews.
checks:
- check_id: named
  name: Independent named-file validation
  command: uv run --locked cmmmech validate data/records/xenotime-concentrate.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xenotime-concentrate
  summary: Actually completed 1 record / 0 failed; retained log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Coordinator corrected cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xenotime-concentrate
  summary: 'Actually completed by coordinator; independently read and SHA256-verified
    raw log dcc7d1261abfca630c5a13f9ed142b85bb1462960ff410d2072f7b14d4c3908a. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 166.09s (0:02:46)

    Checked 246 record(s); 0 failed.

    Checked 291 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Coordinator corrected cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xenotime-concentrate
  summary: 'Actually completed by coordinator; independently read and SHA256-verified
    raw log 5599312a3ee08a5df1b1f5d52f06e26aec1513ffe4bc0a5e4ef60dd00ea6e0aa. Checked
    246 record(s); 0 failed.

    '
- check_id: history
  name: Coordinator corrected cohort history
  command: uv run --locked cmmmech validate-history --base 98e787e8d61593797aef1ed29840b2315a0cc6e5
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xenotime-concentrate
  summary: 'Actually completed by coordinator; independently read and SHA256-verified
    raw log bf614125e66d58201aeb2a712034842703a4c3090392cb57e00cd260c9c6e79a. Checked
    291 history record(s); 0 error(s).

    '
- check_id: render-check
  name: Coordinator corrected cohort render-check
  command: just render-check
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:xenotime-concentrate
  summary: 'Actually completed by coordinator; independently read and SHA256-verified
    raw log be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run
    python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/xenotime-concentrate.yaml
  locator: Whole native-inspected target
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Distinct primary-resource owner, five source evidence statements, conditions
    and explicit uncertainties checked field by field.
  snapshot_sha256: 8e1d30e8c05053055fc352625e894a6575f3ed288c5c702d0aff702cdb9290ea
- evidence_id: main
  kind: primary_source
  reference: https://doi.org/10.1016/j.chemgeo.2024.122186
  locator: Complete GFZ 56-page postprint; Methods2.1-2.5, Results3.1-3.6, Discussion4.1-4.4,
    conclusion; all Figures 1–7 and Tables 1–3 personally viewed on PDF pages 17,
    19, 22, 24, 25, 26, 36, 55, 56.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Read complete main scientific text and original graphics. Mixed feed, laboratory
    bacterial/abiotic/cells-only arms, observed filtered concentrations, acid profiles
    and separate96 h chemical assays support the scoped mechanism. Whole 56-page visual
    inspection is not claimed.
  snapshot_sha256: 8b269c3ef6c76060ea8b73c5e5129978f2272de74e34611b8ebb1fb5f4256ab7
- evidence_id: supplement
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0009254124002663-mmc1.pdf
  locator: All 16 original pages; Figures S1–S7, Tables S1–S8, Text S1, actual captions
    compared with contents list.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Source identity matches main title/authors. Independently verified mixed
    phases, particle/density-derived fractions, model equations and discrepancies
    in card numbers, Yb/Lu tables, numbering and bond-energy explanation. Source-assigned
    phases and rates remain qualified.
  snapshot_sha256: 9c9e72c594a0f136fc7bc299eecaf91054de43d2f17cee12db696536a84863d0
- evidence_id: taxonomy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1428&mode=Info
  locator: Live current-name/rank/lineage returned 2026-10-12; 1428 species in Bacillus
    cereus group.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Species label/identifier resolves. It cannot identify the particular Renju
    isolate without deposited sequence/strain accession; record retains this limit.
  snapshot_sha256: b355f629fe6fb4128fe04ec5f95cf9eee2c1b48010d80320548dac916ce443ec
- evidence_id: artifacts
  kind: record_content
  reference: /private/tmp/cmm-round50-xenotime-independent/evidence-check.json
  locator: All 99 declared curator artifact hashes independently recomputed; original
    graphics inspected within recorded scope.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Artifacts match the handoff. This is independent examination of retained
    originals, not an independent download of every artifact or reanalysis of unacquired
    Mendeley raw data.
  snapshot_sha256: 4ce7a4a84407d4e5f757ef3f7ce0287e8e46a4a0bde007105a411a6fecf36b08
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round50-xenotime-independent/dedup.log
  locator: Exact DOI 122186 / PII and xenotime-concentrate text search over current
    scientific directories.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Hits identify this resource and current source handoffs; concurrently curated
    xenotime-(Y)/monazite-(Ce) are distinct mineral owners. Broader author raw-root
    receipt reviewed with its declared missing/binary limits, not rerun as machine-wide
    search.
  snapshot_sha256: f98e50dd8176c04f50db23fe3f1bf9e73d7a940fac20ad916c191746faddc486
  search_scope: rg --no-ignore --hidden --follow on current data/records,research,reviews,history;
    exactDOI/PII/material terms; currenttextboundary only, unrelated directories/unextracted
    binaries excluded.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round50-xenotime-independent/web-evidence.json
  locator: Exact DOI plus correction/erratum/retraction and exact-title correction
    searches; live DOI/NCBI opens.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Returned bounded sets reveal no affecting formal notice. DOI reader itself
    errored while GFZ original metadata is available; no universal no-notice claim
    or raw-data replication is made.
  snapshot_sha256: b355f629fe6fb4128fe04ec5f95cf9eee2c1b48010d80320548dac916ce443ec
  search_scope: Two current exactDOI/title queries, first returned result sets, primary
    GFZ metadata and officialNCBI; secondary citations are leads only.
- evidence_id: history
  kind: record_content
  reference: history/records/xenotime-concentrate/2026-10-12T074155Z-codex-66bb20.yaml
  locator: Actual CREATE session plus distinct inline curation event.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Target, timestamp, actor GPT-6 / codex and event details match the new
    owner and completed work; no prior history rewritten.
  snapshot_sha256: 87c774cecb3f231387c6f8dfd604b7c39cd0b5c2bfeb1add3d85b3355cb2b5a1
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round50-corrected-terminal.json
  locator: Four completed corrected cohort commands; all log hashes independently
    checked.
  accessed_at: '2026-10-12T07:52:54Z'
  support: supports
  summary: Named-file and final cohort structural checks passed. Offline validity
    is separate from this scientific evidence assessment.
  snapshot_sha256: e100469f511872754cd380524eb7f2b4077877db7445e203b9fa465925a28568
assessments:
- assessment_id: identity
  area: identity
  topic: Mixed natural feed versus species or waste
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - target
  - main
  - supplement
  - dedup
  summary: The primary-resource owner is scientifically distinct and appropriately
    bounded.
  details: Source-assigned82.0 wt% xenotime and 2.7 wt% monazite are particle-count/density
    estimates. Concentrate origin/supplier is unspecified; Renju is the isolate source.
    The article mixes other phases and does not establish a pure mineral product,
    commodity or secondary waste. Constituent criticality is not inherited.
- assessment_id: organism
  area: evidence
  topic: Living culture, species mapping and isolate uncertainty
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - main
  - taxonomy
  summary: Organism and experimental scope are supported without a fabricated isolate
    accession.
  details: Exponentially harvested, washed living cells identified by authors as B.
    thuringiensis; initial ~1e6 CFU/mL. NCBI 1428 maps the species only. Methods 2.2
    states BLAST comparison but supplies no verifiable accession in reviewed main/SI.
    CFU excludes attached cells.
- assessment_id: controls
  area: evidence
  topic: Controlled laboratory mobilization and causal limits
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - main
  - supplement
  summary: Reported bacterial enhancement is supported against corresponding abiotic
    controls.
  details: 0.5 g/100 mL, 48–74 micrometre feed, 25–28 C, 180 rpm, 30 days, initial
    pH 6 with or without 20 mM MES; feed biotic / feed abiotic / cells-only arms.
    Replicate numbers accurately preserved. Acidification and buffered release plus96
    h, 1 mM acid tests support proton/ligand contributions but not each metabolite
    causal share.96 h chemical tests do not reproduce30-day pH trajectories.
- assessment_id: measurement
  area: evidence
  topic: Aqueous concentration versus mineral-specific modeled losses
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - main
  - supplement
  summary: Units, endpoints and conditional models are accurately distinguished.
  details: Figure 2 / ~716 micrograms/L day 15 unbuffered and ~343 micrograms/L day
    30 buffered are filtered aqueous concentrations, not recovered mass or cumulative
    extraction. Precipitation changes solution values. Main Table 3 percentages are
    two-source inferred dissolutions;Table S7 / Text S1 reuse whole-concentrate area.
    No isolated REE product or species-general kinetic ratio asserted.
- assessment_id: uncertainty
  area: evidence
  topic: Source contradictions and unidentified precipitates
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - main
  - supplement
  summary: The record retains the material source conflicts and avoids their silent
    correction.
  details: Personally confirmed Figure 5 Exp-Control caption versus Exp-Bt legend;0.22
    mm versus micrometre filters;P2O3/U2O3 labels;Figure S1 duplicated card;S3/S4Yb/Lu
    mismatch;TiO2 nonclosure;above-range Y;SI contents/caption order;granite wording.
    Figure 7 REE/P signals lack mineralogical identification, so rhabdophane/churchite
    remain proposals. The dossier also notesTable 3 rounding and Y-O/Ce-O bond-energy
    contradiction, neither promoted as causal proof.
- assessment_id: provenance
  area: provenance
  topic: Current exact-byte review and history
  outcome: supported
  target_ids:
  - cmmmech:xenotime-concentrate
  evidence_ids:
  - target
  - history
  - artifacts
  - gates
  summary: Current target/history/dossiers and validation receipts are bound and consistent.
  details: Native inspect preceded target judgment and explicitly captured record,
    CREATE, both dossiers, schema. Curator and reviewer are different agents. Raw-data
    statistical reproduction was not performed. No record edit or history event was
    added by reviewer.
findings: []
actions: []
limitations:
- Author-assigned isolate species maps toNCBI 1428, but sequence/strain identity is
  not independently established.
- Measured aqueous mobilization includes possible re-sorption/precipitation; separate
  phase losses and apparent rates are conditional models, not isolated-product recovery.
- Source composition/unit/caption inconsistencies remain explicit; no new closed balance
  or silent repaired source data.
- Complete primary scientific text and relevant original main graphics/all SI were
  inspected; not all 56 main pages were visually inspected.
- Mendeley raw files and statistical reproduction are outside this completed record
  review; notices/dedup searches are bounded.
tags:
- round50
- independent-scientific-review
- mixed-feed
- laboratory-bioleaching
```
