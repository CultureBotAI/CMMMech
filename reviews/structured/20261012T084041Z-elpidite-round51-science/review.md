# Independent scientific review of elpidite

- Review: 20261012T084041Z-elpidite-round51-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T08:34:02.129728Z
- Finished UTC: 2026-10-12T08:40:41Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen elpidite mineral identity and bounded natural occurrence are supported by the issuing-authority entry and complete main article. No corrective record finding; unavailable SI, uncertain phase assignment and inferred geology remain explicit.

## Scope And Provenance

All elpidite record fields, linked CREATE, both source-dossier formats and schema; complete main article/graphics and current cited IMA original.

Selection: Assigned independent exact-target scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 466cb14cbc271ba73ba05e89ed188cfd113d06ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:elpidite | data/records/elpidite.yaml | maintained | Elpidite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named structural validation | passed | True | cmmmech:elpidite | Reviewer executed in round51 worktree; one record checked, zero failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Parent completed batch | passed | True | cmmmech:elpidite | Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-batch.log SHA256 138fa7877c8c2d7365f17d35606c7ece6d6f2bdb0debaff0a9042ee308b5027c. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 197.77s (0:03:17)<br>Checked 249 record(s); 0 failed.<br>Checked 294 history record(s); 0 error(s).<br> |
| Parent completed nonempty | passed | True | cmmmech:elpidite | Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-nonempty.log SHA256 06b051452e7949992afa10ca6afb43fcde683c0e3fcbd9ec1827b3fc360a702b. Checked 249 record(s); 0 failed.<br> |
| Parent completed history | passed | True | cmmmech:elpidite | Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-history.log SHA256 534de7ca88921ec9466d980eda984e27b807ecc018a14caa60d77192e296e563. Checked 294 history record(s); 0 error(s).<br> |
| Parent completed render-check | passed | True | cmmmech:elpidite | Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-render-check.log SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Species identity and material boundaries

identity: supported. Targets: cmmmech:elpidite.

Current mineral identity and qualified natural occurrence are supported without confusing a geological block with a pure feed or elemental resource.

### Main-paper scope with missing supplementary evidence

evidence: supported. Targets: cmmmech:elpidite.

The record accurately confines conclusions to occurrence and inferred geological context. Missing Appendix/SI and the repeated IL-356 label prevent stronger assignment or quantitative claims; those limits are explicit.

### Frozen input integrity and actual required checks

provenance: supported. Targets: cmmmech:elpidite.

All explicit record/history/dossier/schema input hashes match, named validation and actual cohort checks passed, and original access limitations are retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.24425/agp.2022.140427; Complete original eleven-page article, printed235-245; all seven figures and six tables independently viewed/read. Methods236-237; Figure3B, Figures6-7, Table6 and240-243. | supports | A loose Dyrnaes River block is attributed to Green Granite from colour/mineralogy. Microscopy, microprobe chemistry and mapped textures support the authors' elpidite assignment. No specimen-specific diffraction or controlled reaction is reported. Formation sequence and hydrothermal sodium loss are geological interpretations. |
| table_conflict | /private/tmp/cmm-round51-hf-zr-research/raw/cegielka2022-pages/page-008.png; Original Table6 onprinted242 compared with Table4 onprinted238 and Figure3C onprinted239. | supports | Table6 contains elpidite and altered elpidite representative analyses. IL-356 also appears under secondary Zr-silicates in Table4; Figure3C phase wording differs between map/caption. The record preserves assignment uncertainty without numerical purity or alteration-yield inference. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Issuing-authority September2026 original reused, not newly downloaded: definitionspage1 and elpiditerow63 independently visually inspected. | supports | Elpidite Na2ZrSi6O15(H2O)3, grandfathered statusG and1894 are accurate. The year is not a numbered approval accession; identity is separate from elementalZr and same-formula polymorph assignments. |
| context | research/sources/round51-hf-zr/20261012T083417Z-source-investigation.json; Entire paired source investigation MD/JSON and explicitly captured input hashes. | supports | The source dossier documents complete main evidence, inaccessible analytical Appendix/SupplementaryTable1, and deferred hafnon investigations. Thirty-nine raw artifact hashes plus original IMA binding independently matched; unavailable material is not claimed inspected. |
| history | history/records/elpidite/2026-10-12T083032Z-codex-077784.yaml; Whole CREATE sidecar and separate inline event. | supports | Actual codex/GPT-6/codex actor, UTC events and exact target are consistent with new identity curation. The review does not append a curation event or change scientific bytes. |
| dedup | /private/tmp/cmm-round51-elpidite-review/evidence-proof.json; Independent bounded identity/DOI search plus raw-hash and named-validation receipt. | supports | The current elpidite record is the unique maintained owner in the searched scientific directories. Previously discussed elements, minerals and deferred feeds remain separate. |
| notices | /private/tmp/cmm-round51-elpidite-review/evidence-proof.json; Three actual independent web queries and inspected source metadata on2026-10-12. | supports | No applicable notice identified in returned primary/publisher/IMA results. This is bounded search coverage rather than proof that no future or unindexed correction exists. |
| gates | /private/tmp/cmm-round51-final-terminal.json; Completed first round51 cohort receipt and all four actual command logs, read and hash-verified. | supports | 317 tests passed with3skipped;249records and294histories passed before an unrelated monazite locator correction. Elpidite and all captured context bytes are unchanged. Later corrected cohort gates belong to publication; these actual gates cover this frozen target. |

## Limits And Additional Notes

- The original analytical Appendix/SupplementaryTable1 was not acquired; no full-dataset range or alteration efficiency is adopted.
- Sample assignment rests on source microscopy and microprobe chemistry, without specimen-specific diffraction; same-formula polymorph identity is not independently proven.
- Table4/Table6 share IL-356 under different headings; source graphical nomenclature is not treated as independent phase proof.
- Geological formation and later sodium loss are inferred, not controlled mechanisms or recovery experiments.
- Notice/dedup searches are bounded, include hidden/ignored files and followed relevant roots, and exclude unextracted binaries/unrelated machine paths.
- Cohort gates cited here precede a sibling monazite locator correction; this target and context remain unchanged, and final publication requires corrected-state gates.
- No Git/GitHub mutation, target edit, self-scientific approval or invented source acquisition.
- Native initial inspect preceded source judgment; final inspect also captures both final dossier formats before completed assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T084041Z-elpidite-round51-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of elpidite
started_at: '2026-10-12T08:34:02.129728Z'
finished_at: '2026-10-12T08:40:41Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer authored monazite-ore in this cohort, not elpidite.
    Elpidite record/history/dossier were authored by /root/round27_superalloy. Reviewer
    independently captured native inputs, inspected original eleven-page article/all
    graphics and IMA, and did not edit the target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen elpidite mineral identity and bounded natural occurrence are supported
  by the issuing-authority entry and complete main article. No corrective record finding;
  unavailable SI, uncertain phase assignment and inferred geology remain explicit.
source:
  git_revision: 466cb14cbc271ba73ba05e89ed188cfd113d06ea
  state: working_tree
  inputs:
  - path: data/records/elpidite.yaml
    sha256: d4380b722d62b9e66de5be913d7629dce70780fff4e55ec47147eb96ed9baf3e
    role: target
  - path: history/records/elpidite/2026-10-12T083032Z-codex-077784.yaml
    sha256: 01d42dcf6c7b20b55e37aff37ba526f86a5e2ade4f66149cf9e02f55e2cdd8ea
    role: context
  - path: research/sources/round51-hf-zr/20261012T083417Z-source-investigation.json
    sha256: d9af738401c786d6be136f2141a4c8f74248bc1a264ced9805d8a46620a8721d
    role: context
  - path: research/sources/round51-hf-zr/20261012T083417Z-source-investigation.md
    sha256: ac585894f77989140afae42702308f4edcbd38067da9693a14e7492cb7000757
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:elpidite
  path: data/records/elpidite.yaml
  label: Elpidite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/elpidite.yaml
    role: maintained
scope:
  description: All elpidite record fields, linked CREATE, both source-dossier formats
    and schema; complete main article/graphics and current cited IMA original.
  selection: Assigned independent exact-target scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:elpidite
  exclusions:
  - target: Unacquired analytical Appendix and SupplementaryTable1; deferred hafnon
      sources
    reason: No unsupported detailed analysis or independent phase/kinetic verification
      claimed; narrow main-paper occurrence only.
checks:
- check_id: named
  name: Independent named structural validation
  command: uv run --locked cmmmech validate data/records/elpidite.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:elpidite
  summary: Reviewer executed in round51 worktree; one record checked, zero failed.
    Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Parent completed batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:elpidite
  summary: 'Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-batch.log
    SHA256 138fa7877c8c2d7365f17d35606c7ece6d6f2bdb0debaff0a9042ee308b5027c. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 197.77s (0:03:17)

    Checked 249 record(s); 0 failed.

    Checked 294 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Parent completed nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:elpidite
  summary: 'Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-nonempty.log
    SHA256 06b051452e7949992afa10ca6afb43fcde683c0e3fcbd9ec1827b3fc360a702b. Checked
    249 record(s); 0 failed.

    '
- check_id: history
  name: Parent completed history
  command: uv run --locked cmmmech validate-history --base 466cb14cbc271ba73ba05e89ed188cfd113d06ea
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:elpidite
  summary: 'Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-history.log
    SHA256 534de7ca88921ec9466d980eda984e27b807ecc018a14caa60d77192e296e563. Checked
    294 history record(s); 0 error(s).

    '
- check_id: render-check
  name: Parent completed render-check
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:elpidite
  summary: 'Parent executed; reviewer read and hash-verified actual log /private/tmp/cmm-round51-final-render-check.log
    SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run
    python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.24425/agp.2022.140427
  locator: Complete original eleven-page article, printed235-245; all seven figures
    and six tables independently viewed/read. Methods236-237; Figure3B, Figures6-7,
    Table6 and240-243.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: A loose Dyrnaes River block is attributed to Green Granite from colour/mineralogy.
    Microscopy, microprobe chemistry and mapped textures support the authors' elpidite
    assignment. No specimen-specific diffraction or controlled reaction is reported.
    Formation sequence and hydrothermal sodium loss are geological interpretations.
  snapshot_sha256: 5dada77414c55b55b616b53c73e3f74ded64f33a04db6517a23ff8d98d9e1fc1
- evidence_id: table_conflict
  kind: primary_source
  reference: /private/tmp/cmm-round51-hf-zr-research/raw/cegielka2022-pages/page-008.png
  locator: Original Table6 onprinted242 compared with Table4 onprinted238 and Figure3C
    onprinted239.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: Table6 contains elpidite and altered elpidite representative analyses.
    IL-356 also appears under secondary Zr-silicates in Table4; Figure3C phase wording
    differs between map/caption. The record preserves assignment uncertainty without
    numerical purity or alteration-yield inference.
  snapshot_sha256: 2beb76f8020011785ba463ac916430cf07b1e27f06f3dadb8937a8e44d43af81
- evidence_id: ima
  kind: database
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'Issuing-authority September2026 original reused, not newly downloaded:
    definitionspage1 and elpiditerow63 independently visually inspected.'
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: Elpidite Na2ZrSi6O15(H2O)3, grandfathered statusG and1894 are accurate.
    The year is not a numbered approval accession; identity is separate from elementalZr
    and same-formula polymorph assignments.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: context
  kind: record_content
  reference: research/sources/round51-hf-zr/20261012T083417Z-source-investigation.json
  locator: Entire paired source investigation MD/JSON and explicitly captured input
    hashes.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: The source dossier documents complete main evidence, inaccessible analytical
    Appendix/SupplementaryTable1, and deferred hafnon investigations. Thirty-nine
    raw artifact hashes plus original IMA binding independently matched; unavailable
    material is not claimed inspected.
  snapshot_sha256: d9af738401c786d6be136f2141a4c8f74248bc1a264ced9805d8a46620a8721d
- evidence_id: history
  kind: record_content
  reference: history/records/elpidite/2026-10-12T083032Z-codex-077784.yaml
  locator: Whole CREATE sidecar and separate inline event.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: Actual codex/GPT-6/codex actor, UTC events and exact target are consistent
    with new identity curation. The review does not append a curation event or change
    scientific bytes.
  snapshot_sha256: 01d42dcf6c7b20b55e37aff37ba526f86a5e2ade4f66149cf9e02f55e2cdd8ea
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round51-elpidite-review/evidence-proof.json
  locator: Independent bounded identity/DOI search plus raw-hash and named-validation
    receipt.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: The current elpidite record is the unique maintained owner in the searched
    scientific directories. Previously discussed elements, minerals and deferred feeds
    remain separate.
  snapshot_sha256: 475208772485e83378dcbbf0ab217cd31f01be75bb9606c76c2650fb4889fb2e
  search_scope: Independent cycle-safe os.walkfollowlinks includeshidden/ignoredcurrent+original
    data/records,history,reviews,research and two specificallycitedrawroots; textualextensions<=30MB
    only. No binarysemantic or entiremachineabsenceclaim. Widercurator170-rootreceiptwasinspectedseparately,notmisrepresentedasanindependentrerun.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round51-elpidite-review/evidence-proof.json
  locator: Three actual independent web queries and inspected source metadata on2026-10-12.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: No applicable notice identified in returned primary/publisher/IMA results.
    This is bounded search coverage rather than proof that no future or unindexed
    correction exists.
  snapshot_sha256: 475208772485e83378dcbbf0ab217cd31f01be75bb9606c76c2650fb4889fb2e
  search_scope: 'Freshweb firstreturnedrelevancesets, no pagination. Primarypublisher/bibliographicresults
    andIMAmetadata returned; noapplicablecorrectionlocated inthisboundedset. Notexhaustiveabsence.
    SearchMayIMAresultisnottherecordauthority; retainedSeptemberoriginalindependentlyviewed.
    Queries: "10.24425/agp.2022.140427" correction erratum retraction; elpidite "IL-356"
    Cegielka; site:cnmnc.units.it "Elpidite" 2026'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round51-final-terminal.json
  locator: Completed first round51 cohort receipt and all four actual command logs,
    read and hash-verified.
  accessed_at: '2026-10-12T08:40:41Z'
  support: supports
  summary: 317 tests passed with3skipped;249records and294histories passed before
    an unrelated monazite locator correction. Elpidite and all captured context bytes
    are unchanged. Later corrected cohort gates belong to publication; these actual
    gates cover this frozen target.
  snapshot_sha256: 4fd864559f58298f65698cb37b12dba04f230471fa4501ad962e42eab302a740
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity and material boundaries
  outcome: supported
  target_ids:
  - cmmmech:elpidite
  evidence_ids:
  - ima
  - primary
  - dedup
  summary: Current mineral identity and qualified natural occurrence are supported
    without confusing a geological block with a pure feed or elemental resource.
  dimensions:
  - name: material_form
    value: Mineral identity; source-assigned elpidite in heterogeneous natural granite
      block
    definition: Not purified mineral, synthetic product or measured recovery feed
    evidence_ids:
    - primary
    - ima
  - name: criticality
    value: No criticality designation
    definition: No jurisdiction/list/edition inherited from zirconium
    evidence_ids:
    - ima
- assessment_id: science
  area: evidence
  topic: Main-paper scope with missing supplementary evidence
  outcome: supported
  target_ids:
  - cmmmech:elpidite
  evidence_ids:
  - primary
  - table_conflict
  - context
  summary: The record accurately confines conclusions to occurrence and inferred geological
    context. Missing Appendix/SI and the repeated IL-356 label prevent stronger assignment
    or quantitative claims; those limits are explicit.
  dimensions:
  - name: mechanism_and_biomass
    value: No microbial mechanism, organism or biomass state asserted
    definition: Natural geological observations are not microbial reaction experiments
    evidence_ids:
    - primary
  - name: outcome_scale
    value: Textures/compositions and interpreted magmatic/hydrothermal sequence
    definition: No controlled transformation yield, extraction, isolated product or
      industrial deployment
    evidence_ids:
    - primary
    - table_conflict
- assessment_id: provenance
  area: provenance
  topic: Frozen input integrity and actual required checks
  outcome: supported
  target_ids:
  - cmmmech:elpidite
  evidence_ids:
  - history
  - context
  - gates
  - notices
  summary: All explicit record/history/dossier/schema input hashes match, named validation
    and actual cohort checks passed, and original access limitations are retained.
findings: []
actions: []
limitations:
- The original analytical Appendix/SupplementaryTable1 was not acquired; no full-dataset
  range or alteration efficiency is adopted.
- Sample assignment rests on source microscopy and microprobe chemistry, without specimen-specific
  diffraction; same-formula polymorph identity is not independently proven.
- Table4/Table6 share IL-356 under different headings; source graphical nomenclature
  is not treated as independent phase proof.
- Geological formation and later sodium loss are inferred, not controlled mechanisms
  or recovery experiments.
- Notice/dedup searches are bounded, include hidden/ignored files and followed relevant
  roots, and exclude unextracted binaries/unrelated machine paths.
- Cohort gates cited here precede a sibling monazite locator correction; this target
  and context remain unchanged, and final publication requires corrected-state gates.
notes:
- No Git/GitHub mutation, target edit, self-scientific approval or invented source
  acquisition.
- Native initial inspect preceded source judgment; final inspect also captures both
  final dossier formats before completed assessment.
tags:
- round51
- elpidite
- independent
- scientific
```
