# Independent scientific review of tannery wastewater

- Review: 20261016T015926Z-tannery-wastewater-round108-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T01:36:35.490984Z
- Finished UTC: 2026-10-16T01:59:26.696820Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen wastewater record is scientifically defensible for laboratory removal by heat-inactivated C.elegans biomass. Separate feed batches, synthetic-solution nulls, uncertain molecular cause and absence of recovered-product/deployment evidence are preserved. No supported corrective record finding remains.

## Scope And Provenance

Complete maintained tannery-wastewater owner, linked CREATE history, schema and frozen source dossier; independent full primary and identifier assessment.

Selection: Exactly one maintained record selected by path and ID.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26661b7f033d4bdb915e48e71080aa5774b4c3d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tannery-wastewater | data/records/tannery-wastewater.yaml | maintained | Tannery wastewater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:tannery-wastewater | Checked 1 record(s); 0 failed. |
| Coordinator completed batch command1 | passed | True | cmmmech:tannery-wastewater | Terminal receipt and retained log independently verified; actual command exit0 and final owner hash match. |
| Coordinator completed batch command2 | passed | True | cmmmech:tannery-wastewater | Terminal receipt and retained log independently verified; actual command exit0 and final owner hash match. |
| Coordinator completed batch command3 | passed | True | cmmmech:tannery-wastewater | Terminal receipt and retained log independently verified; actual command exit0 and final owner hash match. |
| Coordinator completed batch command4 | passed | True | cmmmech:tannery-wastewater | Terminal receipt and retained log independently verified; actual command exit0 and final owner hash match. |

## Scientific And Domain Assessments

### Aqueous secondary resource and bounded criticality

identity: supported. Targets: cmmmech:tannery-wastewater.

Correct distinct wastewater owner.

The accepted material is conventionally treated real effluent from Acque del Chiampo, Arzignano, Italy. It is not the separate tannery-sludge solid, chromium-tanned leather, pure chromium, or synthetic nitrate solution. Source Cr(III) assignment is qualified; constituent criticality is not inherited, so no jurisdiction/list/edition assertion is being made. Table1 annual means are not assay-batch recipes.

### Species, stock and inactive state

identity: supported. Targets: cmmmech:tannery-wastewater.

Species identifier and source stock scope are kept distinct.

Primary paper identifies C.elegans MUT2861; official taxonomy verifies species4853, not stock authenticity. Seven-day30°C110rpm EQ/ST cultivation and 121°C30min autoclaving precede the biosorption assays. This is inactive biomass with microbial origin, not proof of living chromium metabolism or redox conversion. iModulonDB is not applicable: no gene, locus, regulator or transcriptomics claim is made.

### Real-feed conditions and controls

evidence: supported. Targets: cmmmech:tannery-wastewater.

Accepted methods match the full original.

Methods2.4–2.6 support ST versus EQ cultivation,18g/Lpotato starch in ST,15g fresh or1.5g lyophilized biomass per150mL in250mLflasks,30°C110rpm and24h, triplicates and no-biomass controls. Real effluent pH7.80–8.20 and0.31–0.56mg/L chromium vary across feeds; no buffer or explicit CrVI detection limit. NaOH pretreatment was boiling0.5M15min followed by washpH7–7.2; Discussion cold-alkali wording is retained as a source inconsistency.

### Tables3–4 retain separate denominators and feed batches

consistency: supported. Targets: cmmmech:tannery-wastewater.

The recorded percentages and uncertainties match the visually inspected tables.

Table3 articlep10/PDFp12 reports ST37.61±1.48% andEQ29.73±0.00% at24h, mean±SD. Table4 at0.39±0.00mg/L compares untreated37.61±1.48% versuslyophilized28.34±0.00%; its separate0.42±0.02mg/Lfeed compares untreated26.46±1.38% versusNaOH32.05±1.38%. No cross-batch causal comparison is made. Percentages refer to solution disappearance, not isolated-product yields.

### Removal, mechanistic inference and null evidence

evidence: supported. Targets: cmmmech:tannery-wastewater.

Aqueous removal is supported; molecular cause and product recovery remain limited.

Methods2.6 capacity is aqueous chromium disappearance divided by final dry biomass mass, not a directly measured complete biomass-bound inventory. Stable no-biomass controls support biomass-associated removal without excluding biomass-induced precipitation. APATCNRIRSA3010/3020Man29(2003) is cited without explicit instrument/LOD. Table5 articlep12/PDFp14 is separate pH5 chromium-nitrate chemistry; higher capacities cannot transfer to real pH8effluent. Synthetic lyophilized-biomass null is retained with data-not-shown qualification. Ligand/proton-exchange explanations remain interpretations.

### Laboratory evidence and deployment boundary

scope: supported. Targets: cmmmech:tannery-wastewater.

No scale or regulatory claim is inflated.

Figure1 articlep11/PDFp13 compares another0.44mg/Lreal feed: approximately16%clariflocculation,40%biosorption,44%combined, which are separate source-reported outcomes rather than additive effects or demonstrated synergy. Industrial wastewater origin/plant flow does not prove deployed fungal treatment, legal compliance, detoxification, desorption, recovered product or useful product quality.

### Source version, current bytes and actual provenance

provenance: supported. Targets: cmmmech:tannery-wastewater.

The review and checks are bound to exact inspected inputs.

The full23page institutional author manuscript is explicit; version-of-record PDF was not independently compared. PMID/DOI/title/authors/year are verified. Actual inline CREATE and canonical sidecar are distinct. All pre-assessment input hashes remained unchanged. Named validation and coordinator terminal batch/history checks are accurately represented and do not substitute for scientific assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/tannery-wastewater.yaml; Complete frozen maintained owner, all claims and evidence; inspected before assessment. | supports | Exact record hash matches pre-assessment inspection and current bytes. |
| history | history/records/tannery-wastewater/2026-10-16T013224Z-codex-3ea6cc.yaml; Canonical CREATE session plus separate inline event and attached reference. | supports | Correct actual codex/GPT-6 actor, target and current creation scope; no older provenance invented. |
| primary | https://doi.org/10.1016/j.biortech.2009.01.002; Complete University of Turin author manuscript, 23 PDF pages (two covers plus article pp.1–21), Methods2.1–2.6, Results3.2–3.3, Tables1–5, Figure1 and Discussion. | supports | Reviewer independently read complete text and visually inspected all23pages including all tables and figure. Exact primary PDF was acquired by coordinator, not freshly downloaded by reviewer. |
| visual | /private/tmp/cmm-round108-uranium-research/tannery-review-source-manifest.json; SHA256 manifest of original PDF, full text and all23 rendered pages inspected independently. | supports | Visual table checks distinguish both Table4 feed batches and Table5 synthetic comparison. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4853&amp;mode=Info; Fresh official NCBI taxonomy search returned full entry; direct browser opening failed. Retained web evidence includes both outcomes. | supports | NCBITaxon4853 is Cunninghamella elegans at species rank. This does not authenticate experimental MUT2861. |
| bibliography | https://pubmed.ncbi.nlm.nih.gov/19211244/; Fresh PubMed/official publisher metadata and retained Crossref response. | supports | DOI, PMID, title, authors, year2009 and Bioresource Technology100(11):2770–2776 agree. Retrieval cover date2026 is not publication date. |
| notices | /private/tmp/cmm-round108-uranium-research/tannery-review-web.json; Exact DOI/title correction/retraction/erratum queries, publisher/PubMed checks and Crossref relation/update metadata. | context_only | No notice surfaced in this bounded search. This does not establish global absence or exhaustive review of citing papers. |
| dedup | /private/tmp/cmm-round108-uranium-research/tannery-review-dedup.json; Recorded rg --no-ignore --hidden --follow search across W owners/research/reviews/history, main records/ignored reports and current source root. | context_only | Existing tannery-sludge owner was read: different solid feed and different2019 acidophile study. No identity conflation with this aqueous2009 feed is needed; scope is bounded. |
| validation | /private/tmp/cmm-round108-uranium-research/tannery-review-validation.json; Independent named strict validation actual terminal receipt. | supports | Checked1record;0failed. Exact owner digest and command retained. |
| batch | /private/tmp/cmm-round108-final-gates-corrected.json; Coordinator terminal four-command receipt, actual worktree/base, all exits0, unchanged owner input and retained log digest. | supports | Full check, nonempty validation, canonical history and rendered pages passed on the completed batch. Reviewer verified receipt rather than claiming a duplicated corpus execution. |

## Limits And Additional Notes

- Version-of-record PDF was not compared with the complete institutional author manuscript; primary raw source acquisition was by coordinator, independently inspected by reviewer.
- No independent MUT2861 stock authentication, new experiment, raw-data reconstruction or author outreach. Species taxonomy does not establish stock identity.
- No complete chromium/speciation balance, explicit analytical instrument/LOD, direct molecular binding proof, desorption/product recovery or industrial fungal deployment is established.
- Additional wastewater-study leads in source dossier remain unaccepted pending full methods; bounded notice searches and hidden/ignored-inclusive dedup do not establish universal absence or source exhaustion.
- No corrective record issue manufactured; remaining source limitations are explicit and do not contradict the accepted narrow observation.
- Final batch receipt is coordinator execution independently checked, not an additional reviewer corpus run.
- Reviewer authored other records in the same batch, disclosed above; this is an independent assessment of the root-authored wastewater owner.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T015926Z-tannery-wastewater-round108-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of tannery wastewater
started_at: '2026-10-16T01:36:35.490984Z'
finished_at: '2026-10-16T01:59:26.696820Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored the reviewed wastewater owner/history. Reviewer
    authored unrelated soddyite/sklodowskite owners and independently inspected all
    primary pages, figures/tables and current identifier sources; reviewer did not
    edit this target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen wastewater record is scientifically defensible for laboratory
  removal by heat-inactivated C.elegans biomass. Separate feed batches, synthetic-solution
  nulls, uncertain molecular cause and absence of recovered-product/deployment evidence
  are preserved. No supported corrective record finding remains.
source:
  git_revision: 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  state: working_tree
  inputs:
  - path: data/records/tannery-wastewater.yaml
    sha256: 8597e28a89aa444285118e1ccf08f83b8c68f124ec73c1fdc32020f10748d5b1
    role: target
  - path: history/records/tannery-wastewater/2026-10-16T013224Z-codex-3ea6cc.yaml
    sha256: 39b35cf05f52580c6bb9ae294d5ba92ac6183663c28e33fd7b3e974f89141bd9
    role: context
  - path: research/sources/round108-resources/20261016T013311Z-source-investigation.json
    sha256: 3a6124422e4ff9ebc39b0bf5b2a6efdf5a041cbf91e5c14ff1595b3925162f40
    role: context
  - path: research/sources/round108-resources/20261016T013311Z-source-investigation.md
    sha256: 4c503f0eda961e5bebc974679dbde00670f14f8174173c5d9c5a12581e208581
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:tannery-wastewater
  path: data/records/tannery-wastewater.yaml
  label: Tannery wastewater
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tannery-wastewater.yaml
    role: maintained_record
scope:
  description: Complete maintained tannery-wastewater owner, linked CREATE history,
    schema and frozen source dossier; independent full primary and identifier assessment.
  selection: Exactly one maintained record selected by path and ID.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tannery-wastewater
checks:
- check_id: named
  name: Independent named strict validation
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:tannery-wastewater
  command: uv run --locked cmmmech validate data/records/tannery-wastewater.yaml --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: batch1
  name: Coordinator completed batch command1
  status: passed
  required: true
  summary: Terminal receipt and retained log independently verified; actual command
    exit0 and final owner hash match.
  target_ids:
  - cmmmech:tannery-wastewater
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Coordinator completed batch command2
  status: passed
  required: true
  summary: Terminal receipt and retained log independently verified; actual command
    exit0 and final owner hash match.
  target_ids:
  - cmmmech:tannery-wastewater
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Coordinator completed batch command3
  status: passed
  required: true
  summary: Terminal receipt and retained log independently verified; actual command
    exit0 and final owner hash match.
  target_ids:
  - cmmmech:tannery-wastewater
  command: uv run --locked cmmmech validate-history --base 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch4
  name: Coordinator completed batch command4
  status: passed
  required: true
  summary: Terminal receipt and retained log independently verified; actual command
    exit0 and final owner hash match.
  target_ids:
  - cmmmech:tannery-wastewater
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/tannery-wastewater.yaml
  locator: Complete frozen maintained owner, all claims and evidence; inspected before
    assessment.
  summary: Exact record hash matches pre-assessment inspection and current bytes.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: 8597e28a89aa444285118e1ccf08f83b8c68f124ec73c1fdc32020f10748d5b1
- evidence_id: history
  kind: record_content
  reference: history/records/tannery-wastewater/2026-10-16T013224Z-codex-3ea6cc.yaml
  locator: Canonical CREATE session plus separate inline event and attached reference.
  summary: Correct actual codex/GPT-6 actor, target and current creation scope; no
    older provenance invented.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: 39b35cf05f52580c6bb9ae294d5ba92ac6183663c28e33fd7b3e974f89141bd9
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.biortech.2009.01.002
  locator: Complete University of Turin author manuscript, 23 PDF pages (two covers
    plus article pp.1–21), Methods2.1–2.6, Results3.2–3.3, Tables1–5, Figure1 and
    Discussion.
  summary: Reviewer independently read complete text and visually inspected all23pages
    including all tables and figure. Exact primary PDF was acquired by coordinator,
    not freshly downloaded by reviewer.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: 432557380a8162dd74193cbede55583106be1c9d5e04ccea79698e7bf49b4cf2
- evidence_id: visual
  kind: primary_source
  reference: /private/tmp/cmm-round108-uranium-research/tannery-review-source-manifest.json
  locator: SHA256 manifest of original PDF, full text and all23 rendered pages inspected
    independently.
  summary: Visual table checks distinguish both Table4 feed batches and Table5 synthetic
    comparison.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: c9f009506334028bc8e5ed8e6b433a16cdd7dcfe3b1ce7d366c87b1b69df0706
- evidence_id: taxonomy
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4853&mode=Info
  locator: Fresh official NCBI taxonomy search returned full entry; direct browser
    opening failed. Retained web evidence includes both outcomes.
  summary: NCBITaxon4853 is Cunninghamella elegans at species rank. This does not
    authenticate experimental MUT2861.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: a3868b3b7898238a96388ebe25c23cf067a9a916d7ab8049a70d7c7717267b0d
- evidence_id: bibliography
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/19211244/
  locator: Fresh PubMed/official publisher metadata and retained Crossref response.
  summary: DOI, PMID, title, authors, year2009 and Bioresource Technology100(11):2770–2776
    agree. Retrieval cover date2026 is not publication date.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: a3868b3b7898238a96388ebe25c23cf067a9a916d7ab8049a70d7c7717267b0d
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round108-uranium-research/tannery-review-web.json
  locator: Exact DOI/title correction/retraction/erratum queries, publisher/PubMed
    checks and Crossref relation/update metadata.
  summary: No notice surfaced in this bounded search. This does not establish global
    absence or exhaustive review of citing papers.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: context_only
  snapshot_sha256: a3868b3b7898238a96388ebe25c23cf067a9a916d7ab8049a70d7c7717267b0d
  search_scope: Exact DOI/title correction/retraction/erratum queries, publisher/PubMed
    checks and Crossref relation/update metadata. No notice surfaced in this bounded
    search. This does not establish global absence or exhaustive review of citing
    papers.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round108-uranium-research/tannery-review-dedup.json
  locator: Recorded rg --no-ignore --hidden --follow search across W owners/research/reviews/history,
    main records/ignored reports and current source root.
  summary: 'Existing tannery-sludge owner was read: different solid feed and different2019
    acidophile study. No identity conflation with this aqueous2009 feed is needed;
    scope is bounded.'
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: context_only
  snapshot_sha256: 1acbf1115b26fc83ed218f507393b9aba4f6896b6e4f63a6fe883fb25fb6ef4c
  search_scope: 'Recorded rg --no-ignore --hidden --follow search across W owners/research/reviews/history,
    main records/ignored reports and current source root. Existing tannery-sludge
    owner was read: different solid feed and different2019 acidophile study. No identity
    conflation with this aqueous2009 feed is needed; scope is bounded.'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round108-uranium-research/tannery-review-validation.json
  locator: Independent named strict validation actual terminal receipt.
  summary: Checked1record;0failed. Exact owner digest and command retained.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: bb2af784528530063498777ced847c130b11e958e9a5954f4dc171c4a26de253
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round108-final-gates-corrected.json
  locator: Coordinator terminal four-command receipt, actual worktree/base, all exits0,
    unchanged owner input and retained log digest.
  summary: Full check, nonempty validation, canonical history and rendered pages passed
    on the completed batch. Reviewer verified receipt rather than claiming a duplicated
    corpus execution.
  accessed_at: '2026-10-16T01:59:26.696820Z'
  support: supports
  snapshot_sha256: b537f2550a758f2e973b21f657129e0922fe41ea0cde632899d354d5bf11daf3
assessments:
- assessment_id: identity
  area: identity
  topic: Aqueous secondary resource and bounded criticality
  outcome: supported
  summary: Correct distinct wastewater owner.
  details: The accepted material is conventionally treated real effluent from Acque
    del Chiampo, Arzignano, Italy. It is not the separate tannery-sludge solid, chromium-tanned
    leather, pure chromium, or synthetic nitrate solution. Source Cr(III) assignment
    is qualified; constituent criticality is not inherited, so no jurisdiction/list/edition
    assertion is being made. Table1 annual means are not assay-batch recipes.
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - dedup
- assessment_id: biomass
  area: identity
  topic: Species, stock and inactive state
  outcome: supported
  summary: Species identifier and source stock scope are kept distinct.
  details: 'Primary paper identifies C.elegans MUT2861; official taxonomy verifies
    species4853, not stock authenticity. Seven-day30°C110rpm EQ/ST cultivation and
    121°C30min autoclaving precede the biosorption assays. This is inactive biomass
    with microbial origin, not proof of living chromium metabolism or redox conversion.
    iModulonDB is not applicable: no gene, locus, regulator or transcriptomics claim
    is made.'
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - taxonomy
- assessment_id: methods
  area: evidence
  topic: Real-feed conditions and controls
  outcome: supported
  summary: Accepted methods match the full original.
  details: Methods2.4–2.6 support ST versus EQ cultivation,18g/Lpotato starch in ST,15g
    fresh or1.5g lyophilized biomass per150mL in250mLflasks,30°C110rpm and24h, triplicates
    and no-biomass controls. Real effluent pH7.80–8.20 and0.31–0.56mg/L chromium vary
    across feeds; no buffer or explicit CrVI detection limit. NaOH pretreatment was
    boiling0.5M15min followed by washpH7–7.2; Discussion cold-alkali wording is retained
    as a source inconsistency.
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - visual
- assessment_id: numbers
  area: consistency
  topic: Tables3–4 retain separate denominators and feed batches
  outcome: supported
  summary: The recorded percentages and uncertainties match the visually inspected
    tables.
  details: Table3 articlep10/PDFp12 reports ST37.61±1.48% andEQ29.73±0.00% at24h,
    mean±SD. Table4 at0.39±0.00mg/L compares untreated37.61±1.48% versuslyophilized28.34±0.00%;
    its separate0.42±0.02mg/Lfeed compares untreated26.46±1.38% versusNaOH32.05±1.38%.
    No cross-batch causal comparison is made. Percentages refer to solution disappearance,
    not isolated-product yields.
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - visual
- assessment_id: outcome
  area: evidence
  topic: Removal, mechanistic inference and null evidence
  outcome: supported
  summary: Aqueous removal is supported; molecular cause and product recovery remain
    limited.
  details: Methods2.6 capacity is aqueous chromium disappearance divided by final
    dry biomass mass, not a directly measured complete biomass-bound inventory. Stable
    no-biomass controls support biomass-associated removal without excluding biomass-induced
    precipitation. APATCNRIRSA3010/3020Man29(2003) is cited without explicit instrument/LOD.
    Table5 articlep12/PDFp14 is separate pH5 chromium-nitrate chemistry; higher capacities
    cannot transfer to real pH8effluent. Synthetic lyophilized-biomass null is retained
    with data-not-shown qualification. Ligand/proton-exchange explanations remain
    interpretations.
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - visual
- assessment_id: scale
  area: scope
  topic: Laboratory evidence and deployment boundary
  outcome: supported
  summary: No scale or regulatory claim is inflated.
  details: 'Figure1 articlep11/PDFp13 compares another0.44mg/Lreal feed: approximately16%clariflocculation,40%biosorption,44%combined,
    which are separate source-reported outcomes rather than additive effects or demonstrated
    synergy. Industrial wastewater origin/plant flow does not prove deployed fungal
    treatment, legal compliance, detoxification, desorption, recovered product or
    useful product quality.'
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - primary
  - visual
- assessment_id: provenance
  area: provenance
  topic: Source version, current bytes and actual provenance
  outcome: supported
  summary: The review and checks are bound to exact inspected inputs.
  details: The full23page institutional author manuscript is explicit; version-of-record
    PDF was not independently compared. PMID/DOI/title/authors/year are verified.
    Actual inline CREATE and canonical sidecar are distinct. All pre-assessment input
    hashes remained unchanged. Named validation and coordinator terminal batch/history
    checks are accurately represented and do not substitute for scientific assessment.
  target_ids:
  - cmmmech:tannery-wastewater
  evidence_ids:
  - owner
  - history
  - bibliography
  - notices
  - validation
  - batch
findings: []
actions: []
limitations:
- Version-of-record PDF was not compared with the complete institutional author manuscript;
  primary raw source acquisition was by coordinator, independently inspected by reviewer.
- No independent MUT2861 stock authentication, new experiment, raw-data reconstruction
  or author outreach. Species taxonomy does not establish stock identity.
- No complete chromium/speciation balance, explicit analytical instrument/LOD, direct
  molecular binding proof, desorption/product recovery or industrial fungal deployment
  is established.
- Additional wastewater-study leads in source dossier remain unaccepted pending full
  methods; bounded notice searches and hidden/ignored-inclusive dedup do not establish
  universal absence or source exhaustion.
notes:
- No corrective record issue manufactured; remaining source limitations are explicit
  and do not contradict the accepted narrow observation.
- Final batch receipt is coordinator execution independently checked, not an additional
  reviewer corpus run.
- Reviewer authored other records in the same batch, disclosed above; this is an independent
  assessment of the root-authored wastewater owner.
```
