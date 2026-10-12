# Independent scientific review of eudialyte concentrate

- Review: 20261012T100755Z-eudialyte-concentrate-round53-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T10:05:00Z
- Finished UTC: 2026-10-12T10:07:55Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The distinct beneficiated feed and scoped chemical laboratory/pilot recovery are primary-supported. No corrective finding; retained temperature, impurity losses, product-total discrepancy, incomplete finalmassbalance and deployment limits prevent stronger claims.

## Scope And Provenance

All target fields, CREATEhistory, paired source context and schema; complete Ma2019 original including all18figures/4tables and source/processing-state authority.

Selection: Assigned independent exact-target scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b85c2c2c753fe83a2fc21f073ee1e49675ae647e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:eudialyte-concentrate | data/records/eudialyte-concentrate.yaml | maintained | Eudialyte concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named structural validation | passed | True | cmmmech:eudialyte-concentrate | Reviewer executed in round53, one checked/zero failed; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Parent completed batch | passed | True | cmmmech:eudialyte-concentrate | Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-batch.log SHA256 5dccf1da78b9111e8714e725ea5b540e319448ec511b2cd3cd161ed16ab3d5a5. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 137.72s (0:02:17)<br>Checked 256 record(s); 0 failed.<br>Checked 303 history record(s); 0 error(s).<br> |
| Parent completed nonempty | passed | True | cmmmech:eudialyte-concentrate | Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-nonempty.log SHA256 f102e7162eedb9bf7d45e2a2fa9b011e7a3bf83fb2c341e1424889b9dd856f34. Checked 256 record(s); 0 failed.<br> |
| Parent completed history | passed | True | cmmmech:eudialyte-concentrate | Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-history.log SHA256 60b1330e0225bff7414e09d933725aee3784ed120b5151b881814e9a98ae731c. Checked 303 history record(s); 0 error(s).<br> |
| Parent completed render-check | passed | True | cmmmech:eudialyte-concentrate | Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-render-check.log SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Beneficiated mixed geological feed owner

identity: supported. Targets: cmmmech:eudialyte-concentrate.

Concentrate processing and characterized composition distinguish the owner from uncharacterized crushed ore, mineral species, elements and secondarywaste. No inherited criticality.

### Chemical process, denominators and scale

evidence: supported. Targets: cmmmech:eudialyte-concentrate.

Source reports actualchemicalrecovery and a collectedmixedproduct; massbalance and productpurity limits, source arithmetic and laboratory/pilot distinction are accurately retained.

### Frozen sourcecontext and executedchecks

provenance: supported. Targets: cmmmech:eudialyte-concentrate.

All five captured inputs and50rawartifact hashes matched. Named and actual completed shared gates passed; access and search bounds remain explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.1595/205651318X15270000571362; Complete twelve original pages, printed2–13; Figures1–18,TablesI–IV and equations personally inspected. | supports | Beneficiated TANBREEZ feed has measured bulk grade and QEMSCAN phase classes. Chemical acid digestion, impurity separation and product precipitation are demonstrated at laboratory and pilot scales; no microbial arm or commercial deployment. |
| feed | /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-02.png; Printedp3 Methods; TableI and Figures1–4 onpp4–5. | supports | Crushing and partly magnetic selection establish a processing-state boundary from existing uncharacterized eudialyte-ore. QEMSCAN67.05% classification and1.60wt%TREE/6.46wt%Zr are specimen-specific, not pure mineral identity or commercial specification. |
| process | /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-08.png; Original Sections3.1–4.2,TablesII–III,Figures5–17. | supports | 500g laboratory aliquots,10MHCl1.25L/kg,40min dry digestion; no externalheat but70–80°C exotherm. Laboratory1h versuspilot30min and36kg total are correctly separated. Impurity removal costs2.1%REE; higherpH increasesloss. PlannedNb/Zr/Hf residue route is not a demonstratedproduct. |
| product | /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-10.png; Printedp11 TableIV,Figure18 and product prose; compared withFigure16 flow sheet. | supports | &gt;98.8% precipitationfromliquor differs from85.5% overallreportedrecovery. TableIV individualREEsum30.40wt% versusTREE29.95wt%, impurities and absent finalmass prevent closedyield reconstruction. Carbonate is process-assigned, not productdiffractionverified; missing finalreprecipitationdetails retained. |
| context | research/sources/round53-zircon-feed/20261012T095915Z-source-investigation.json; Paired source dossier, all explicit native inputs and50 externalartifact hashes. | supports | Acquisition truthfully separates validoriginalmirror from failed institutional/publisher downloads. Bansal/Hedrich sourcegap remains deferred. Completeprimary supplies narrow chemicalclaim; no availableSI or dataset is invented. |
| history | history/records/eudialyte-concentrate/2026-10-12T095619Z-codex-9b0f45.yaml; Entire canonical CREATE and distinct inline event. | supports | Actorcodex/GPT-6/codex, UTC, target and actual newowner action are consistent. |
| dedup | /private/tmp/cmm-round53-eudialyte-peer/hash-dedup-proof.json; Independent bounded source/owner search and rawhash checks. | supports | Existing eudialyte-ore explicitly excludes concentrate; source Methods verifies beneficiation. Prior same-group cited modeling/fuming is not accepted as independent replication. |
| notices | /private/tmp/cmm-round53-eudialyte-peer/notice-search.txt; Fresh exactDOI notice query,title/author query and RWTH758718 official metadata on2026-10-12. | supports | Authority verifies DOI/authors/63(1)2–13 and2018online/2019issue relation. No applicable correction/retraction surfaced in bounded firstreturnedsets; no universal absence assertion. Related priorfuming/modeling source leads not pooled. |
| gates | /private/tmp/cmm-round53-final-terminal.json; Actual completed cohort receipt and all four logs independently read/hashed. | supports | Required batch,nonempty,history andrender checks passed; all five captured inputs unchanged. |

## Limits And Additional Notes

- No matched microbial experiment; currentmechanism is chemical and explicitly microbial:false.
- TableIV TREE29.95 differs from individualREEsum30.40wt%; finalproductmass, fullreprecipitationdetails and productdiffraction absent.
- Replicatecounts and statisticaluncertainty not supplied for parameterplots; no strong claim from small bar differences.
- Original institutional directPDF response was invalid; correct fulloriginal mirror corroborated by publisher/RWTH metadata.
- No declared supplement in inspectedpaper; publisher interface gave nofileentry, not proof no underlying data exist.
- Deferred zircon microbial sourcegaps and prior same-group experiment overlap remain outside accepted evidence.
- Bounded hidden/ignored/followed textual search cannot establish machine-wide or unextractedbinary absence.
- Reviewer did not change scientific target, history or dossier and did not mutate Git/GitHub.
- Nativeinspect captured record/history/pairedMDJSON/schema before scientific judgment; record hash remains afa309420e2e20f08868b5708c24e08ba612088643b9c484d9c53d755846b647.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T100755Z-eudialyte-concentrate-round53-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of eudialyte concentrate
started_at: '2026-10-12T10:05:00Z'
finished_at: '2026-10-12T10:07:55Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer authored the round53 clay extension, not eudialyte-concentrate.
    Curator /root/round43_hardmetal authored this target/history/dossier. Native inspection
    preceded assessment; reviewer personally checked all original twelve pages and
    every graphic, independently verified authority/dedup/raw hashes and did not edit
    the target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The distinct beneficiated feed and scoped chemical laboratory/pilot recovery
  are primary-supported. No corrective finding; retained temperature, impurity losses,
  product-total discrepancy, incomplete finalmassbalance and deployment limits prevent
  stronger claims.
source:
  git_revision: b85c2c2c753fe83a2fc21f073ee1e49675ae647e
  state: working_tree
  inputs:
  - path: data/records/eudialyte-concentrate.yaml
    sha256: afa309420e2e20f08868b5708c24e08ba612088643b9c484d9c53d755846b647
    role: target
  - path: history/records/eudialyte-concentrate/2026-10-12T095619Z-codex-9b0f45.yaml
    sha256: a86172b746388969cdd20a1c3610746e1e9b5a667d0e2cb891ba3eca08b90a49
    role: context
  - path: research/sources/round53-zircon-feed/20261012T095915Z-source-investigation.json
    sha256: b4ee1cf4538cda10a4bb013dba3bbf60562dc066826204e5386d72308cbc31dd
    role: context
  - path: research/sources/round53-zircon-feed/20261012T095915Z-source-investigation.md
    sha256: 97cde65dd3ee1d3df61f358dc34856f3eb8f01bce444ea50add23723bba13913
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:eudialyte-concentrate
  path: data/records/eudialyte-concentrate.yaml
  label: Eudialyte concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eudialyte-concentrate.yaml
    role: maintained
scope:
  description: All target fields, CREATEhistory, paired source context and schema;
    complete Ma2019 original including all18figures/4tables and source/processing-state
    authority.
  selection: Assigned independent exact-target scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:eudialyte-concentrate
  exclusions:
  - target: Deferred microbial zircon studies Bansal2007 and Hedrich2023
    reason: No new fullsource scientific acceptance; current target is the distinct
      characterized chemical concentrate and does not close issue153.
checks:
- check_id: named
  name: Independent named structural validation
  command: uv run --locked cmmmech validate data/records/eudialyte-concentrate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-concentrate
  summary: Reviewer executed in round53, one checked/zero failed; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Parent completed batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-concentrate
  summary: 'Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-batch.log
    SHA256 5dccf1da78b9111e8714e725ea5b540e319448ec511b2cd3cd161ed16ab3d5a5. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 137.72s (0:02:17)

    Checked 256 record(s); 0 failed.

    Checked 303 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Parent completed nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-concentrate
  summary: 'Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-nonempty.log
    SHA256 f102e7162eedb9bf7d45e2a2fa9b011e7a3bf83fb2c341e1424889b9dd856f34. Checked
    256 record(s); 0 failed.

    '
- check_id: history
  name: Parent completed history
  command: uv run --locked cmmmech validate-history --base b85c2c2c753fe83a2fc21f073ee1e49675ae647e
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-concentrate
  summary: 'Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-history.log
    SHA256 60b1330e0225bff7414e09d933725aee3784ed120b5151b881814e9a98ae731c. Checked
    303 history record(s); 0 error(s).

    '
- check_id: render-check
  name: Parent completed render-check
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-concentrate
  summary: 'Parent executed; reviewer read and hash-verified /private/tmp/cmm-round53-final-render-check.log
    SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run
    python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1595/205651318X15270000571362
  locator: Complete twelve original pages, printed2–13; Figures1–18,TablesI–IV and
    equations personally inspected.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Beneficiated TANBREEZ feed has measured bulk grade and QEMSCAN phase classes.
    Chemical acid digestion, impurity separation and product precipitation are demonstrated
    at laboratory and pilot scales; no microbial arm or commercial deployment.
  snapshot_sha256: 8c8f68490eef55fc657afa3d4762bd6a1e397c1a803c6a95ebec3125ad4924a7
- evidence_id: feed
  kind: primary_source
  reference: /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-02.png
  locator: Printedp3 Methods; TableI and Figures1–4 onpp4–5.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Crushing and partly magnetic selection establish a processing-state boundary
    from existing uncharacterized eudialyte-ore. QEMSCAN67.05% classification and1.60wt%TREE/6.46wt%Zr
    are specimen-specific, not pure mineral identity or commercial specification.
  snapshot_sha256: 4bd71c818ff57b26d8dc4603a2fd346b6a99a7a9aa9e204ad878a4d54ffdd34a
- evidence_id: process
  kind: primary_source
  reference: /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-08.png
  locator: Original Sections3.1–4.2,TablesII–III,Figures5–17.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: 500g laboratory aliquots,10MHCl1.25L/kg,40min dry digestion; no externalheat
    but70–80°C exotherm. Laboratory1h versuspilot30min and36kg total are correctly
    separated. Impurity removal costs2.1%REE; higherpH increasesloss. PlannedNb/Zr/Hf
    residue route is not a demonstratedproduct.
  snapshot_sha256: 7791d6a34b37bfdd03e778b93818788eeff52d05e74c99b9abc960a1e043f486
- evidence_id: product
  kind: primary_source
  reference: /private/tmp/cmm-round53-zircon-feed-research/raw/ma2019-mirror-pages/page-10.png
  locator: Printedp11 TableIV,Figure18 and product prose; compared withFigure16 flow
    sheet.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: '>98.8% precipitationfromliquor differs from85.5% overallreportedrecovery.
    TableIV individualREEsum30.40wt% versusTREE29.95wt%, impurities and absent finalmass
    prevent closedyield reconstruction. Carbonate is process-assigned, not productdiffractionverified;
    missing finalreprecipitationdetails retained.'
  snapshot_sha256: a8af12b54d15241eb79fbd473a4d032094c85787609f36e2fbcab4c23753273b
- evidence_id: context
  kind: record_content
  reference: research/sources/round53-zircon-feed/20261012T095915Z-source-investigation.json
  locator: Paired source dossier, all explicit native inputs and50 externalartifact
    hashes.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Acquisition truthfully separates validoriginalmirror from failed institutional/publisher
    downloads. Bansal/Hedrich sourcegap remains deferred. Completeprimary supplies
    narrow chemicalclaim; no availableSI or dataset is invented.
  snapshot_sha256: b4ee1cf4538cda10a4bb013dba3bbf60562dc066826204e5386d72308cbc31dd
- evidence_id: history
  kind: record_content
  reference: history/records/eudialyte-concentrate/2026-10-12T095619Z-codex-9b0f45.yaml
  locator: Entire canonical CREATE and distinct inline event.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Actorcodex/GPT-6/codex, UTC, target and actual newowner action are consistent.
  snapshot_sha256: a86172b746388969cdd20a1c3610746e1e9b5a667d0e2cb891ba3eca08b90a49
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round53-eudialyte-peer/hash-dedup-proof.json
  locator: Independent bounded source/owner search and rawhash checks.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Existing eudialyte-ore explicitly excludes concentrate; source Methods
    verifies beneficiation. Prior same-group cited modeling/fuming is not accepted
    as independent replication.
  snapshot_sha256: 06e75cb1d39954f08f7a6985671965ba029beef064c04380ce59b12c6d8ceeec
  search_scope: Fresh rg --no-ignore --hidden --follow over current/original records,research,reviews,history
    and305 explicitly referenced existing directories;9missingrawcandidates disclosed
    in receipt. Searchable text, no OCR of every prior binary or machine-wide absence
    claim.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round53-eudialyte-peer/notice-search.txt
  locator: Fresh exactDOI notice query,title/author query and RWTH758718 official
    metadata on2026-10-12.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Authority verifies DOI/authors/63(1)2–13 and2018online/2019issue relation.
    No applicable correction/retraction surfaced in bounded firstreturnedsets; no
    universal absence assertion. Related priorfuming/modeling source leads not pooled.
  snapshot_sha256: 12f8494e1671f4b5aeef0a8e5f9bae2422320187f0ebf158fdb120764979cc24
  search_scope: 'Queries: "10.1595/205651318X15270000571362" correction erratum retraction;
    "Hydrometallurgical Treatment of an Eudialyte Concentrate" Ma Stopic Friedrich2019;
    official RWTH758718 opened. Firstreturnedrelevance sets only; no pagination.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round53-final-terminal.json
  locator: Actual completed cohort receipt and all four logs independently read/hashed.
  accessed_at: '2026-10-12T10:07:55Z'
  support: supports
  summary: Required batch,nonempty,history andrender checks passed; all five captured
    inputs unchanged.
  snapshot_sha256: 87d8701e2f43cdccb46f2fd4e788c31593c8be134573a12a2b8d7cb419b3ab36
assessments:
- assessment_id: identity
  area: identity
  topic: Beneficiated mixed geological feed owner
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-concentrate
  evidence_ids:
  - primary
  - feed
  - dedup
  summary: Concentrate processing and characterized composition distinguish the owner
    from uncharacterized crushed ore, mineral species, elements and secondarywaste.
    No inherited criticality.
  dimensions:
  - name: material_form
    value: Partly magnetically beneficiated TANBREEZ mixed geological concentrate
    definition: Source-specific primary_resource; not pure eudialyte or a universal
      traded specification
    evidence_ids:
    - feed
  - name: criticality
    value: No designation asserted
    definition: No jurisdiction/list/edition inherited from constituentREE/Zr
    evidence_ids:
    - primary
- assessment_id: science
  area: evidence
  topic: Chemical process, denominators and scale
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-concentrate
  evidence_ids:
  - primary
  - process
  - product
  - context
  summary: Source reports actualchemicalrecovery and a collectedmixedproduct; massbalance
    and productpurity limits, source arithmetic and laboratory/pilot distinction are
    accurately retained.
  dimensions:
  - name: organism_biomass
    value: No organism or microbialbiomass; microbial:false
    definition: Acid digestion and chemicalprecipitation are the tested process
    evidence_ids:
    - process
  - name: controls
    value: Chemical parametercomparisons; no microbialcomparator
    definition: No inference of microbial enhancement or statistical significance
      from bars without replicateuncertainty
    evidence_ids:
    - process
  - name: outcome_denominators
    value: Solutionextraction, precipitationfromliquor, overallreportedrecovery and
      elementgrade remain distinct
    definition: No finalmass or productdiffraction to independently reconstruct yield/purity
    evidence_ids:
    - product
  - name: scale
    value: 500g laboratory and36kg pilot; not commercial operation
    definition: Apparatuscapacity and possible downstreamroutes are not sustainedindustrialperformance
    evidence_ids:
    - process
- assessment_id: provenance
  area: provenance
  topic: Frozen sourcecontext and executedchecks
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-concentrate
  evidence_ids:
  - context
  - history
  - notices
  - gates
  summary: All five captured inputs and50rawartifact hashes matched. Named and actual
    completed shared gates passed; access and search bounds remain explicit.
findings: []
actions: []
limitations:
- No matched microbial experiment; currentmechanism is chemical and explicitly microbial:false.
- TableIV TREE29.95 differs from individualREEsum30.40wt%; finalproductmass, fullreprecipitationdetails
  and productdiffraction absent.
- Replicatecounts and statisticaluncertainty not supplied for parameterplots; no strong
  claim from small bar differences.
- Original institutional directPDF response was invalid; correct fulloriginal mirror
  corroborated by publisher/RWTH metadata.
- No declared supplement in inspectedpaper; publisher interface gave nofileentry,
  not proof no underlying data exist.
- Deferred zircon microbial sourcegaps and prior same-group experiment overlap remain
  outside accepted evidence.
- Bounded hidden/ignored/followed textual search cannot establish machine-wide or
  unextractedbinary absence.
notes:
- Reviewer did not change scientific target, history or dossier and did not mutate
  Git/GitHub.
- Nativeinspect captured record/history/pairedMDJSON/schema before scientific judgment;
  record hash remains afa309420e2e20f08868b5708c24e08ba612088643b9c484d9c53d755846b647.
tags:
- round53
- eudialyte-concentrate
- independent
- scientific
```
