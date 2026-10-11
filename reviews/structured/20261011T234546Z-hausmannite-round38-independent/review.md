# Independent scientific review of hausmannite fungal mobilization

- Review: 20261011T234546Z-hausmannite-round38-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T23:42:56.672625Z
- Finished UTC: 2026-10-11T23:45:46.453609Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Whole frozenhausmannite record is supported as a narrowly qualified selenium-conditioned fungal culture observation. Zero corrective findings. Syntheticphase attribution,untimematched controls,source unit/biomassconflicts,endpointanalyticalfractions and absence of recovery/deployment remain explicit.

## Scope And Provenance

Whole hausmannite identity,mechanism,conditions,controls,sourceboundaries and canonical/inlineprovenance.

Selection: Parent assigned record curated byanotheragent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f3d674806df8f5fd7925e46f1dcfec70cace706a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hausmannite | data/records/hausmannite.yaml | maintained | Hausmannite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:hausmannite | Reviewer executed: 1 record, 0 failed. Log /private/tmp/cmm-round38-hausmannite-review-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final cohort batch | passed | True | cmmmech:hausmannite | Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-batch.log SHA256 cd7dc72bc2a2f472d84f5e9c0ba200749f40d668cd6e39b05d8649de00308dd5. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 108.02s (0:01:48)<br>Checked 206 record(s); 0 failed.<br>Checked 237 history record(s); 0 error(s). |
| Final cohort nonempty | passed | True | cmmmech:hausmannite | Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-nonempty.log SHA256 0a70d3ea31b01abc1a047c1a68029b2e03f4a1284bce6f451cc2cf4da10a3181. Checked 206 record(s); 0 failed. |
| Final cohort history | passed | True | cmmmech:hausmannite | Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-history.log SHA256 4b62b8e5cb9dd0edb1deb96a0dcfd97e383ff2e308d024a39015dd7580f14a83. Checked 237 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Species and source-assigned synthetic feed

identity: supported. Targets: cmmmech:hausmannite.

IMA/Handbook identity and NCBIspecies mapping valid; target clearly distinguishes synthetic preparation and doesnot silently assume fresh batchpurity.

### Condition-dependent culture-associated Mn mobilization

evidence: supported. Targets: cmmmech:hausmannite.

Primary endpoints support comparison of two fungal selenium conditions, with all available controls and absent causal isolation made explicit.

### Endpoint/fraction, units and causal limits

evidence: supported. Targets: cmmmech:hausmannite.

Record accurately retains g/L–mg/L,biomass normalization/inhibition conflicts, undefinedstatistics and unmeasured molecular/speciationsteps.

### Independent exactstate and executedchecks

provenance: supported. Targets: cmmmech:hausmannite.

Nativeinspect preceded whole-targetjudgment. Reviewer authored katsarosite, notthisrecord; pre-freeze original-source observations were communicated toauthor and independently reassessed against frozenrecord. Actualnamed/cohortchecks verified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/hausmannite.yaml; Whole frozen record/native inspect | supports | Target3f319c60 remains unchanged; reviewer did not curate target/history. |
| primary | https://doi.org/10.3390/jof7100810; Complete10-page original PDF and JATS; Methods2.1–2.4, Results3.1–3.4, Discussion | supports | Independently read full text and visually inspected all10originalpages including all5figures. Author-assigned synthetic hausmannite phase refers to priorXRD, no fresh batch pattern. A.niger CBS140837 from7daycolony, density/volume unspecified.45mL autoclavedSDB,0.11gsolid,5mLselenate stock to50mg/LSe,stated2.2g/Lsolid;24h130rpm precontact then21daystatic25Cdark,triplicate.0.45micrometre filtered totalMn byF-AAS is neither free-ion nor oxidationstate measurement. |
| controls | https://doi.org/10.3390/jof7100810; Originalpage3 Methods2.3 and Figures1a,2a,3 | supports | Lower finalpH3.2 vs4.4 and greaterMn in Se-containingfungal hausmannite cultures versusSe-free cultures are supported endpoints. No-solid fungal control and Se-free comparator are not abiotic controls.24h uninoculatedSe stage is not time-matched to21daylive cultures. No matchedpH,killedbiomass or directchemicalSe control isolates netfungaleffect. No specific acid,enzyme,transport orredoxstep quantified. |
| conflicts | https://doi.org/10.3390/jof7100810; OriginalFigures1b,2a,4–5 and Sections3.2,3.3,4 | supports | Figure2/resultsg/L conflicts with proposed threshold0.25–1.4mg/L. Source calls endpoint difference rate butrecord appropriately doesnot. ResultsFe/Mn86/65percent versus DiscussionMn86percent; Figure1bwhiteMn~128percent despite selenium-free normalizationlabel. Record declines numerical threshold/inhibition recalculation and preserves undefined significance/errorbars. These are source limits, not uncorrected target defects. |
| outcome | https://doi.org/10.3390/jof7100810; OriginalFigures3–5, Results3.3–3.4 and Discussion | supports | Small initialhausmanniteSe sorption, altered residualSe and washedbiomass concentrations support compartment observations. Concentration per drybiomass isnot intracellularlocalization or totaluptakemass; no speciesresolvedSe/Mn assay,isolated productyield or industrialdeployment. Ferricarm distinct;2020As/oxalate products not transferred. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Originalpage90 row; Handbook ofMineralogy originalonepage | supports | IMA Mn2+Mn3+2O4,G1828; Handbook tetragonal description corroborates species identity. Neither a naturalore nor manganeseelement owner. No criticalityinherited. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/5061/dataset_report; Fresh same-day officialJSON independently parsed | supports | 5061 is speciesAspergillus niger. CBS140837 remains source-reported strain; the record doesnot assert independent stockauthentication or strainTaxID. |
| notices | /private/tmp/cmm-round38-hausmannite-review-notice-search.json; Independent exactDOI/title notice and competing-studyqueries; fullJATS supplemental inventory | supports | No affecting notice verified among returned results or Crossref update metadata. CompleteJATS5figures,zero tables or supplementary-material nodes; PDF no separateSI section. Other antimony/arsenic studies are different experiments, not pooled. No exhaustive notice/supplement absence claimed. |
| dedup | /private/tmp/cmm-round38-hausmannite-review-dedup.txt; Hidden/ignored/followed current records,research,reviews,history; source-author cited-raw scan | supports | Distinct hausmannite owner despite samephase appearing as substrate in falottaite/lindbergite records. Normalized2021DOI not counted as newindependent experiment percopy. Referencedrawdedup scope read; all29actualmanifest rawhashes independently verified. |
| history | history/records/hausmannite/2026-10-11T234142Z-codex-45f4d6.yaml; WholeCREATEsidecar and distinctinlineevent | supports | Actualcodex/GPT-6/codex actor and new mineral scope correct; canonical23:41:42Z plus separate23:42:16inline. No prior scientific history rewritten. |
| gates | /private/tmp/cmm-round38-final-terminal.json; Finalterminal receipt/all3logs | supports | Parent executed completedcohortchecks; reviewer read/hashverified logs and frozeninputs. Structurevalidation isnot independent scienceproof. |

## Limits And Additional Notes

- Synthetic phase assignment refers toearlier XRD;2021doesnot supply freshbatch diffraction or quantifiedpurity.
- No time-matched sterile releasecontrol or matched-pH/killedbiomasscomparison isolates netfungalenhancement.
- InitialpH and sporeloadingunreported; active culturetemperature/duration reported.
- Sourceg/Lversusmg/L and inhibition/normalizationconflicts remain unresolved; preciseprotectivethreshold or inhibitionpercentnotadopted.
- FilteredtotalMn isnot freeion/redoxspeciation; biomassconcentration isnot intracellularlocalization or totalrecoveredmass.
- No specificacid/enzyme,closedrecoverypercentage,postculturemineralproduct,orindustrialdeployment demonstrated.
- Bounded notice/supplement search isnot exhaustive; no independent experimentreplication or rawanalyticalreanalysis.
- Full10originalpages andall5figures inspected; fullXMLshowsnomain tables orSupplementaryMaterialnode.
- No record/history editsbyreviewer;29rawmanifesthashesverified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T234546Z-hausmannite-round38-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of hausmannite fungal mobilization
started_at: '2026-10-11T23:42:56.672625Z'
finished_at: '2026-10-11T23:45:46.453609Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Hausmannite target,history and dossier authored by /root/round27_superalloy.
    Reviewer authored katsarosite and no hausmannite bytes. Shared original artifacts
    disclosed; source conditions/conflicts communicated pre-freeze as independent
    review observations. Nativeinspect preceded targetjudgment; whole frozenrecord
    reassessed against independently read fullprimary/alloriginalfigures.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Whole frozenhausmannite record is supported as a narrowly qualified selenium-conditioned
  fungal culture observation. Zero corrective findings. Syntheticphase attribution,untimematched
  controls,source unit/biomassconflicts,endpointanalyticalfractions and absence of
  recovery/deployment remain explicit.
source:
  git_revision: f3d674806df8f5fd7925e46f1dcfec70cace706a
  state: working_tree
  inputs:
  - path: data/records/hausmannite.yaml
    sha256: 3f319c603aa92069f7c1e04c4c34e4bd11820b8697f1e3396eac26a3a01e5d3e
    role: target
  - path: history/records/hausmannite/2026-10-11T234142Z-codex-45f4d6.yaml
    sha256: 124d3cb3152ec9db4ece2ba644d32701a87b601df6cbd59dcfaaaa43f7572133
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Whole hausmannite identity,mechanism,conditions,controls,sourceboundaries
    and canonical/inlineprovenance.
  selection: Parent assigned record curated byanotheragent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hausmannite
  exclusions:
  - target: 2020arsenic/oxalate experiment; ferricoxyhydroxide owner
    reason: Different experiments/materials. Their observedproducts or desorption
      cannot be transferred to this2021hausmannite arm.
targets:
- target_id: cmmmech:hausmannite
  path: data/records/hausmannite.yaml
  label: Hausmannite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hausmannite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: PYTHONDONTWRITEBYTECODE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1
    uv run --locked cmmmech validate data/records/hausmannite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer executed: 1 record, 0 failed. Log /private/tmp/cmm-round38-hausmannite-review-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e'
  target_ids:
  - cmmmech:hausmannite
- check_id: batch
  name: Final cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-batch.log
    SHA256 cd7dc72bc2a2f472d84f5e9c0ba200749f40d668cd6e39b05d8649de00308dd5. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 108.02s (0:01:48)

    Checked 206 record(s); 0 failed.

    Checked 237 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:hausmannite
- check_id: nonempty
  name: Final cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-nonempty.log
    SHA256 0a70d3ea31b01abc1a047c1a68029b2e03f4a1284bce6f451cc2cf4da10a3181. Checked
    206 record(s); 0 failed.
  target_ids:
  - cmmmech:hausmannite
- check_id: history
  name: Final cohort history
  command: uv run --locked cmmmech validate-history --base f3d674806df8f5fd7925e46f1dcfec70cace706a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Parent executed; reviewer independently read and hash-verified /private/tmp/cmm-round38-final-history.log
    SHA256 4b62b8e5cb9dd0edb1deb96a0dcfd97e383ff2e308d024a39015dd7580f14a83. Checked
    237 history record(s); 0 error(s).
  target_ids:
  - cmmmech:hausmannite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/hausmannite.yaml
  locator: Whole frozen record/native inspect
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Target3f319c60 remains unchanged; reviewer did not curate target/history.
  snapshot_sha256: 3f319c603aa92069f7c1e04c4c34e4bd11820b8697f1e3396eac26a3a01e5d3e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/jof7100810
  locator: Complete10-page original PDF and JATS; Methods2.1–2.4, Results3.1–3.4,
    Discussion
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Independently read full text and visually inspected all10originalpages
    including all5figures. Author-assigned synthetic hausmannite phase refers to priorXRD,
    no fresh batch pattern. A.niger CBS140837 from7daycolony, density/volume unspecified.45mL
    autoclavedSDB,0.11gsolid,5mLselenate stock to50mg/LSe,stated2.2g/Lsolid;24h130rpm
    precontact then21daystatic25Cdark,triplicate.0.45micrometre filtered totalMn byF-AAS
    is neither free-ion nor oxidationstate measurement.
  snapshot_sha256: 4f3b5501bc0c8a1ccdf98665f24db7a4cb72b965a0abb47d19fe59a0134f6fff
- evidence_id: controls
  kind: primary_source
  reference: https://doi.org/10.3390/jof7100810
  locator: Originalpage3 Methods2.3 and Figures1a,2a,3
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Lower finalpH3.2 vs4.4 and greaterMn in Se-containingfungal hausmannite
    cultures versusSe-free cultures are supported endpoints. No-solid fungal control
    and Se-free comparator are not abiotic controls.24h uninoculatedSe stage is not
    time-matched to21daylive cultures. No matchedpH,killedbiomass or directchemicalSe
    control isolates netfungaleffect. No specific acid,enzyme,transport orredoxstep
    quantified.
  snapshot_sha256: 7b2c582e06011ba4740791fc6dc5819daea3062d1cdefcc7c0a629bb9cc5184d
- evidence_id: conflicts
  kind: primary_source
  reference: https://doi.org/10.3390/jof7100810
  locator: OriginalFigures1b,2a,4–5 and Sections3.2,3.3,4
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Figure2/resultsg/L conflicts with proposed threshold0.25–1.4mg/L. Source
    calls endpoint difference rate butrecord appropriately doesnot. ResultsFe/Mn86/65percent
    versus DiscussionMn86percent; Figure1bwhiteMn~128percent despite selenium-free
    normalizationlabel. Record declines numerical threshold/inhibition recalculation
    and preserves undefined significance/errorbars. These are source limits, not uncorrected
    target defects.
  snapshot_sha256: 8468fbe71eff7e17daa8dd78c2df825b5a5274fe928e99c187b6fb5b16f48a8c
- evidence_id: outcome
  kind: primary_source
  reference: https://doi.org/10.3390/jof7100810
  locator: OriginalFigures3–5, Results3.3–3.4 and Discussion
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Small initialhausmanniteSe sorption, altered residualSe and washedbiomass
    concentrations support compartment observations. Concentration per drybiomass
    isnot intracellularlocalization or totaluptakemass; no speciesresolvedSe/Mn assay,isolated
    productyield or industrialdeployment. Ferricarm distinct;2020As/oxalate products
    not transferred.
  snapshot_sha256: 549d6ac9691ab1242943ad0e39ee973b1cbbaa6ea12f1b0d901c8b3660a3c141
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Originalpage90 row; Handbook ofMineralogy originalonepage
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: IMA Mn2+Mn3+2O4,G1828; Handbook tetragonal description corroborates species
    identity. Neither a naturalore nor manganeseelement owner. No criticalityinherited.
  snapshot_sha256: 96677c0aa815c893db84f73a32edb97a1bb1c61a99e1a67773f86522b641f5ab
- evidence_id: taxon
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/5061/dataset_report
  locator: Fresh same-day officialJSON independently parsed
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: 5061 is speciesAspergillus niger. CBS140837 remains source-reported strain;
    the record doesnot assert independent stockauthentication or strainTaxID.
  snapshot_sha256: 6d2d9b2a4b031de6fd14225ddc52dec2a240dadb51d83f12a549e035575e9126
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round38-hausmannite-review-notice-search.json
  locator: Independent exactDOI/title notice and competing-studyqueries; fullJATS
    supplemental inventory
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: No affecting notice verified among returned results or Crossref update
    metadata. CompleteJATS5figures,zero tables or supplementary-material nodes; PDF
    no separateSI section. Other antimony/arsenic studies are different experiments,
    not pooled. No exhaustive notice/supplement absence claimed.
  snapshot_sha256: dac5ac260aac29f6278a347918e78d863dfef4d71f8e9ff396eb1e1efdf6a368
  search_scope: '2026-10-11 queries: "10.3390/jof7100810" correction retraction erratum;
    "Fungal Mobilization of Selenium" "Hausmannite" correction; "hausmannite" "Aspergillus
    niger" selenium bioleaching. First resultsets,no pagination; JATS/PDF link inventory.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round38-hausmannite-review-dedup.txt
  locator: Hidden/ignored/followed current records,research,reviews,history; source-author
    cited-raw scan
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Distinct hausmannite owner despite samephase appearing as substrate in
    falottaite/lindbergite records. Normalized2021DOI not counted as newindependent
    experiment percopy. Referencedrawdedup scope read; all29actualmanifest rawhashes
    independently verified.
  snapshot_sha256: d1429d8693adb2664363ed119af375c937092e3f411d3c52809f3d741e7ef253
  search_scope: rg --hidden --no-ignore --follow for hausmannite,jof7100810,PMC8539610
    across maintained relevanttrees. Author scan127boundedroots includes citedrawdownloads;
    unextractedbinarycontent not universallydecoded. No machinewide noveltyclaim.
- evidence_id: history
  kind: record_content
  reference: history/records/hausmannite/2026-10-11T234142Z-codex-45f4d6.yaml
  locator: WholeCREATEsidecar and distinctinlineevent
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Actualcodex/GPT-6/codex actor and new mineral scope correct; canonical23:41:42Z
    plus separate23:42:16inline. No prior scientific history rewritten.
  snapshot_sha256: 124d3cb3152ec9db4ece2ba644d32701a87b601df6cbd59dcfaaaa43f7572133
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round38-final-terminal.json
  locator: Finalterminal receipt/all3logs
  accessed_at: '2026-10-11T23:45:46.453609Z'
  support: supports
  summary: Parent executed completedcohortchecks; reviewer read/hashverified logs
    and frozeninputs. Structurevalidation isnot independent scienceproof.
  snapshot_sha256: 850e1fa0a84d2d56f1e7de5069d74be8fdd3dba5f5ed09ccd56ad78a33ea159c
assessments:
- assessment_id: identity
  area: identity
  topic: Species and source-assigned synthetic feed
  outcome: supported
  summary: IMA/Handbook identity and NCBIspecies mapping valid; target clearly distinguishes
    synthetic preparation and doesnot silently assume fresh batchpurity.
  target_ids:
  - cmmmech:hausmannite
  evidence_ids:
  - record
  - ima
  - taxon
  - dedup
  dimensions:
  - name: material_form
    value: Hausmannite mineral species; source-assigned synthesized Mn3O4 assayfeed
    definition: No elemental manganese,otherMnoxide or naturalore substitution.
    evidence_ids:
    - ima
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition borrowed from manganese.
    evidence_ids:
    - record
  - name: organism
    value: SourceA.nigerCBS140837; NCBITaxon5061species
    definition: Strain phenotype/identity not independently authenticated byspeciesnode.
    evidence_ids:
    - primary
    - taxon
- assessment_id: mechanism
  area: evidence
  topic: Condition-dependent culture-associated Mn mobilization
  outcome: supported
  summary: Primary endpoints support comparison of two fungal selenium conditions,
    with all available controls and absent causal isolation made explicit.
  target_ids:
  - cmmmech:hausmannite
  evidence_ids:
  - record
  - primary
  - controls
  dimensions:
  - name: biomass
    value: Spores from7day colony; concentration and volume unreported
    definition: Activeculture source description only.
    evidence_ids:
    - primary
  - name: conditions
    value: 45mLSDB+5mLSeaddition;0.11goxide;50mg/LSe;21daystatic25Cdark;triplicate
    definition: 24h130rpm precontact precedes inoculation; initialpHunknown.
    evidence_ids:
    - primary
  - name: controls
    value: No-solid fungal andSe-free comparators;24hpreinoculationbaseline
    definition: No21daysterile,killedor pH-matchedcontrol.
    evidence_ids:
    - controls
- assessment_id: boundaries
  area: evidence
  topic: Endpoint/fraction, units and causal limits
  outcome: supported
  summary: Record accurately retains g/L–mg/L,biomass normalization/inhibition conflicts,
    undefinedstatistics and unmeasured molecular/speciationsteps.
  target_ids:
  - cmmmech:hausmannite
  evidence_ids:
  - record
  - conflicts
  - outcome
  dimensions:
  - name: outcome
    value: GreaterfilteredtotalMn inSe-treatedfungalculture
    definition: Endpointnotkineticrate; no purifiedproduct or closed recoverypercentage.
    evidence_ids:
    - primary
    - controls
  - name: deployment
    value: Laboratoryonly
    definition: No fieldremediation orindustrialoperatingevidence.
    evidence_ids:
    - primary
    - outcome
- assessment_id: provenance
  area: provenance
  topic: Independent exactstate and executedchecks
  outcome: supported
  summary: Nativeinspect preceded whole-targetjudgment. Reviewer authored katsarosite,
    notthisrecord; pre-freeze original-source observations were communicated toauthor
    and independently reassessed against frozenrecord. Actualnamed/cohortchecks verified.
  target_ids:
  - cmmmech:hausmannite
  evidence_ids:
  - record
  - history
  - gates
  - notices
findings: []
actions: []
limitations:
- Synthetic phase assignment refers toearlier XRD;2021doesnot supply freshbatch diffraction
  or quantifiedpurity.
- No time-matched sterile releasecontrol or matched-pH/killedbiomasscomparison isolates
  netfungalenhancement.
- InitialpH and sporeloadingunreported; active culturetemperature/duration reported.
- Sourceg/Lversusmg/L and inhibition/normalizationconflicts remain unresolved; preciseprotectivethreshold
  or inhibitionpercentnotadopted.
- FilteredtotalMn isnot freeion/redoxspeciation; biomassconcentration isnot intracellularlocalization
  or totalrecoveredmass.
- No specificacid/enzyme,closedrecoverypercentage,postculturemineralproduct,orindustrialdeployment
  demonstrated.
- Bounded notice/supplement search isnot exhaustive; no independent experimentreplication
  or rawanalyticalreanalysis.
notes:
- Full10originalpages andall5figures inspected; fullXMLshowsnomain tables orSupplementaryMaterialnode.
- No record/history editsbyreviewer;29rawmanifesthashesverified.
links:
- https://doi.org/10.3390/jof7100810
- https://handbookofmineralogy.org/pdfs/hausmannite.pdf
```
