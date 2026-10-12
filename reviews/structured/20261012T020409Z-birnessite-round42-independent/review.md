# Independent scientific review of birnessite binary cobalt/nickel sorption extension

- Review: 20261012T020409Z-birnessite-round42-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T02:01:13.265346Z
- Finished UTC: 2026-10-12T02:04:09.038193Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record accurately adds a distinct laboratory binary Co/Ni sorption observation on a prepared fungal oxide, with defined selectivity ratios and explicit limitations. All 12 original figures, two tables and the complete source were independently checked. No corrective findings; prior accepted science and history remain unchanged.

## Scope And Provenance

Whole current target integration, fresh scientific review of the Sasaki2009 binary assay, and exact preservation with a prior review for unchanged earlier arms.

Selection: Assigned independent review of another agent's frozen record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a5528a4807ba14fd8088a557ad105ac10ca62965.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:birnessite | data/records/birnessite.yaml | maintained | Birnessite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:birnessite | Reviewer executed from round42 worktree; Checked1record,0failed. Log /private/tmp/cmm-round42-birnessite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final cohort batch | passed | True | cmmmech:birnessite | Coordinator executed; reviewer independently read and raw-byte hash-verified /private/tmp/cmm-round42-final-batch.log SHA256 4980aedbe1b677797b96f68809ecd197fb335257db08dd5e42f8677eca30b98f. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 174.24s (0:02:54)<br>Checked 216 record(s); 0 failed.<br>Checked 252 history record(s); 0 error(s). |
| Final cohort nonempty | passed | True | cmmmech:birnessite | Coordinator executed; reviewer independently read and raw-byte hash-verified /private/tmp/cmm-round42-final-nonempty.log SHA256 253a7b1f24733e2960a5844348786b1f7b8c035bb10af8e25c914e2d5234e023. Checked 216 record(s); 0 failed. |
| Final cohort history | passed | True | cmmmech:birnessite | Coordinator executed; reviewer independently read and raw-byte hash-verified /private/tmp/cmm-round42-final-history.log SHA256 c2a1a9ebbab06d77f85879fede0494f78da78b43ff3500e7c095428e8f54ba35. Checked 252 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral preparation and organism scope

identity: supported. Targets: cmmmech:birnessite.

The source-qualified poorly crystalline fungal oxide is accurately retained as a separate birnessite arm, without inflating mineral purity, strain authentication or criticality.

### Binary Co/Ni sorption and selectivity

evidence: supported. Targets: cmmmech:birnessite.

Original methods, curves, Equation3 and Table2 support preferential fractional cobalt sorption and correctly defined, source-reported coefficients.

### Controls,redox and source contradictions

evidence: supported. Targets: cmmmech:birnessite.

Material redox, normalization, concentration, phase/control and 2008/2009 handling limitations are accurately retained. The unresolved causal route is not overstated.

### Whole-record integration and prior scientific preservation

provenance: supported. Targets: cmmmech:birnessite.

All earlier field values and history bytes are unchanged, and the prior review covers the exact base hash. Earlier literature coverage relies explicitly on that independent review.

### Exact-state independentreview and required checks

provenance: supported. Targets: cmmmech:birnessite.

Native inspection preceded assessment; the complete new primary and original graphics were checked. Actual named and cohort gates were verified. No corrective maintained-record edit is needed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/birnessite.yaml; Whole frozen target, native inspection before scientific judgment | supports | Reviewer authored neither this extension nor the previous birnessite science. Scope is fresh scientific assessment of Sasaki2009 and exact preservation of earlier independently reviewed fields. |
| primary | https://doi.org/10.2320/matertrans.M-M2009821; Complete six-page final publisher PDF, pages2643–2648, all12figures and2tables | supports | Read complete primary text and personally inspected all six rendered original pages. This is the source experiment, not a source-dossier verdict or an abstract. Advance publication7October2009 and November issue are correctly separated. |
| conditions | https://doi.org/10.2320/matertrans.M-M2009821; Section2 page2643, original methods column and Figures7–8/Table2 | supports | Section 2 specifies freeze-dried WL-2 biogenic preparation (0.020 g) or chemical oxide (0.015 g) in 0.150 L, nominally 1 mmol/L solid Mn, 100 mmol/L KNO3, PIPES-buffered initial pH 6.5, 25 degrees C, 100 rpm, 300 hours, in duplicate. Actual binary (Co,Ni) initial pairs are (0.31,0.10), (0.35,0.35), (0.34,1.00) mmol/L. Filtrates passed 0.2 micrometre membranes before ICP-MS. Residues were collected on 0.45 micrometre membranes and lyophilized overnight before XPS. No viability requirement was measured. |
| identity-controls | https://doi.org/10.2320/matertrans.M-M2009821; Section2 page2643 and Section3 page2644; complete graphical inventory | supports | The source calls its fungal material poorly crystalline birnessite but provides no new diffraction or purity measurement. The chemical comparator is explicitly ramsdellite, with specific area 11.5 versus 81.4 m2/g. Different phase, area, composition and retained biomass prevent a phase-matched test of biological origin. A preliminary tissue-only null is stated without a dataset; no no-sorbent or sterile formation time series is displayed. The characterization pointer to reference15 (Murray1984) does not create a new 2009 XRD result. |
| selectivity | https://doi.org/10.2320/matertrans.M-M2009821; Original Figures7–8,Equation3 page2646 and Table2 page2647 | supports | Figures support greater fractional Co than Ni depletion and inhibited Co uptake at higher Ni. Table 2 reports alpha_Co 7.92, 7.47 and 17.7 for biogenic material and 5.65, 2.23 and 2.65 for chemical material. Equation 3 defines the ratio of sorbed/aqueous mole-fraction quotients, which is dimensionless. These are not recovery percentages, purity or yields; no raw replicate dataset independently reproduces the exact coefficients. Co-only curves are separate comparators. |
| redox | https://doi.org/10.2320/matertrans.M-M2009821; Figures1–4,7–12; Table1 page2644 and Results discussion | supports | Mn release includes no-Co and no-Ni conditions and subsequently decreases; this does not establish a closed metal balance. Original XPS is interpreted as predominantly surface Co(III) and Ni(II), without proving complete bulk Co oxidation or measured CoOOH phase yield. Table 1 AOS values 3.09/3.68 differ from prose 3.17/3.70; a stated lack of synthetic Mn(III) conflicts with fraction0.296. Figure 12 is a proposed site diagram; vacancy/edge preference and coprecipitation are not directly imaged. |
| assay-limits | https://doi.org/10.2320/matertrans.M-M2009821; Section2,Figures1–6 and normalizedaxes on page2646 | supports | Methods maxima Co1.7/Ni2.11 mmol/L differ from Figure2 Co2.19/Figure3 Ni2.31. Single-solute arms remain distinct from binary assays. Figure5 normalizes quantity to Mn(III,IV) mass excluding Mn(II), not the whole composite. Figures5–6 are fitted models rather than independent measurements. Different 2008 post-assay handling prevents pooling the papers as identical replicates. |
| taxonomy | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/443224/dataset_report; Official current raw response independently read | supports | Taxon443224 retains exact Paraconiothyrium sp.WL-2 name atnominalspeciesrank. Unresolved named species and culture-stock authentication remain unasserted; noenzyme/functional gene assignment. |
| metadata | https://www.jstage.jst.go.jp/article/matertrans/50/11/50_M-M2009821/_article; Current publisher metadata and Supplementarymaterial(0), author-acquired rawHTML independentlyread | supports | Finalpaginated journal/article metadata and no declaredseparateSI confirmed. Crossref exact DOI/title/authors/pages has emptyrelation and no update-to/updated-by fields. Noextra originaldata inferred. |
| notices | /private/tmp/cmm-round42-birnessite-independent/notice-search.json; Reviewer fresh exact DOI correction/erratum/retraction query and exacttitle contradiction query | supports | Returnedsets identify no affecting formalnotice. Related structuralstudies are leads, notassessed refutations of thisspecificassay. Sourceinternalcontradictions remain explicit. |
| preservation | /private/tmp/cmm-round42-birnessite-independent/evidence-check.json; Independent Git-base semantic and byte comparisons | supports | Every earlier field, including the description, remains unchanged. Mechanisms, sources, inline events and history references are exact prefixes; both committed history files are byte-identical. The exact base-record SHA matches the named round41 independent review. This review does not claim a fresh full reassessment of unchanged Wei2012, Ferrier2022 or Sasaki2008 literature. |
| prior-review | reviews/structured/20261012T012836Z-birnessite-round41-independent/review.yaml; Prior scientific assessment and exact input hash | supports | Previously independentreviewed birnessite mechanisms retained. Root/packaging authored oldscience; presentreviewer also authored priorround41review independently. It chains to the unchangedWei2012 review with its declared sourcecoverage. |
| dedup | /private/tmp/cmm-round42-birnessite-independent/evidence-check.json; Hidden/ignored followed searches of current/original records,research,reviews,history and six relevant rawroots | supports | There are 1189 matching text lines, exit0 and no errors. The same WL-2 material lineage and related 2008/2009 papers are not independent culture-production replicates; the 2009 binary assay is a distinct reported observation. |
| history | history/records/birnessite/2026-10-12T015436Z-codex-a24dff.yaml; New canonicalEDIT and separateinline event | supports | The new canonical EDIT and separate inline event use actual codex/GPT-6/codex metadata and accurately describe the final scientific scope. Their timestamps differ honestly. Existing history remains immutable, and no automatic scientific approval is implied. |
| gates | /private/tmp/cmm-round42-final-terminal.json; Finalcohort receipt and independent raw-byte logverification | supports | All required commands finished with exit0; named-record validation was independently executed and checked one record with no failures. Frozen input hashes remain unchanged. Structural validation does not establish scientific truth. |

## Limits And Additional Notes

- The source-assigned fungal birnessite lacks a new 2009 diffraction or purity measurement; the ramsdellite comparator cannot isolate biological origin.
- The prepared material has fungal origins, but active cells or metabolism during sorption were not measured.
- No displayed no-sorbent or sterile formation time series; preliminary tissue controls lack displayed data.
- Reported selectivity ratios lack a raw replicate dataset for independent exact reconstruction; they are not percentages or purified recovery.
- Surface ex situ XPS does not establish complete bulk cobalt oxidation, unique site occupancy or a quantified CoOOH phase.
- Table/prose manganese oxidation-state conflicts and single-solute loading discrepancies are preserved.
- Different normalization and post-assay handling prevent unqualified isotherm transfer or pooling of 2008 and 2009 assays.
- Real leachate scale-up, desorption/regeneration and industrial deployment were not established.
- Earlier scientific evidence is retained through the exact-hash prior review, not a fresh full reassessment here.
- Notice and deduplication searches are bounded; no exhaustive absence claim.
- The reviewer made no changes to maintained records, histories or source dossiers.
- Named validation was personally executed; coordinator batch logs were independently read and their raw-byte hashes verified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T020409Z-birnessite-round42-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of birnessite binary cobalt/nickel sorption extension
started_at: '2026-10-12T02:01:13.265346Z'
finished_at: '2026-10-12T02:04:09.038193Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The packaging agent authored the 2009 extension, history and
    dossier; this reviewer authored none of the birnessite scientific record. The
    reviewer authored separate round42 petalite/polylithionite records and the lithium
    source dossier. The prior round41 birnessite review was also authored independently
    by this reviewer; unchanged earlier science is carried through that assessment
    and an exact preservation proof. Shared source originals and worktree are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record accurately adds a distinct laboratory binary Co/Ni sorption
  observation on a prepared fungal oxide, with defined selectivity ratios and explicit
  limitations. All 12 original figures, two tables and the complete source were independently
  checked. No corrective findings; prior accepted science and history remain unchanged.
source:
  git_revision: a5528a4807ba14fd8088a557ad105ac10ca62965
  state: working_tree
  inputs:
  - path: data/records/birnessite.yaml
    sha256: 68f1ff968be471ba2095191414df2e51608002b5d34285dadde2814825ac65f4
    role: target
  - path: docs/record-review-profile.md
    sha256: 93f65e8f516a9b7756afd89e4823c1b64e493a46ecbcb3ca5e54a5aa599b10f2
    role: context
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/birnessite/2026-10-12T015436Z-codex-a24dff.yaml
    sha256: 76bac25843cd385f3fac82ac6bbd486c95561de7e1b615c6b5eef99550accaa4
    role: context
  - path: reviews/structured/20261012T012836Z-birnessite-round41-independent/review.yaml
    sha256: 8ff028f8cdbde5226774df40f408721622567b39a87916537a8f610c6f73d9e8
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Whole current target integration, fresh scientific review of the Sasaki2009
    binary assay, and exact preservation with a prior review for unchanged earlier
    arms.
  selection: Assigned independent review of another agent's frozen record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:birnessite
  exclusions:
  - target: Fresh full primary reassessment of unchanged Wei2012, Ferrier2022 and
      Sasaki2008
    reason: Every prior field and history file is preserved and the prior review target
      matches the base. Coverage relies explicitly on that named independent review.
  - target: Other records and unacquired source leads
    reason: Separate owners; no acceptance claim or review of the reviewer's lithium
      records.
targets:
- target_id: cmmmech:birnessite
  path: data/records/birnessite.yaml
  label: Birnessite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/birnessite.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/birnessite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed from round42 worktree; Checked1record,0failed. Log /private/tmp/cmm-round42-birnessite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:birnessite
- check_id: batch
  name: Final cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinator executed; reviewer independently read and raw-byte hash-verified
    /private/tmp/cmm-round42-final-batch.log SHA256 4980aedbe1b677797b96f68809ecd197fb335257db08dd5e42f8677eca30b98f.
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 174.24s (0:02:54)

    Checked 216 record(s); 0 failed.

    Checked 252 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:birnessite
- check_id: nonempty
  name: Final cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Coordinator executed; reviewer independently read and raw-byte hash-verified
    /private/tmp/cmm-round42-final-nonempty.log SHA256 253a7b1f24733e2960a5844348786b1f7b8c035bb10af8e25c914e2d5234e023.
    Checked 216 record(s); 0 failed.
  target_ids:
  - cmmmech:birnessite
- check_id: history
  name: Final cohort history
  command: uv run --locked cmmmech validate-history --base a5528a4807ba14fd8088a557ad105ac10ca62965
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Coordinator executed; reviewer independently read and raw-byte hash-verified
    /private/tmp/cmm-round42-final-history.log SHA256 c2a1a9ebbab06d77f85879fede0494f78da78b43ff3500e7c095428e8f54ba35.
    Checked 252 history record(s); 0 error(s).
  target_ids:
  - cmmmech:birnessite
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/birnessite.yaml
  locator: Whole frozen target, native inspection before scientific judgment
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Reviewer authored neither this extension nor the previous birnessite science.
    Scope is fresh scientific assessment of Sasaki2009 and exact preservation of earlier
    independently reviewed fields.
  snapshot_sha256: 68f1ff968be471ba2095191414df2e51608002b5d34285dadde2814825ac65f4
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Complete six-page final publisher PDF, pages2643–2648, all12figures and2tables
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Read complete primary text and personally inspected all six rendered original
    pages. This is the source experiment, not a source-dossier verdict or an abstract.
    Advance publication7October2009 and November issue are correctly separated.
  snapshot_sha256: eb7ecae442f557dc472c2fe06c2ac7699f7ff1e7f7b1029a319605ea35ef6cb2
- evidence_id: conditions
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Section2 page2643, original methods column and Figures7–8/Table2
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Section 2 specifies freeze-dried WL-2 biogenic preparation (0.020 g) or
    chemical oxide (0.015 g) in 0.150 L, nominally 1 mmol/L solid Mn, 100 mmol/L KNO3,
    PIPES-buffered initial pH 6.5, 25 degrees C, 100 rpm, 300 hours, in duplicate.
    Actual binary (Co,Ni) initial pairs are (0.31,0.10), (0.35,0.35), (0.34,1.00)
    mmol/L. Filtrates passed 0.2 micrometre membranes before ICP-MS. Residues were
    collected on 0.45 micrometre membranes and lyophilized overnight before XPS. No
    viability requirement was measured.
- evidence_id: identity-controls
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Section2 page2643 and Section3 page2644; complete graphical inventory
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: The source calls its fungal material poorly crystalline birnessite but
    provides no new diffraction or purity measurement. The chemical comparator is
    explicitly ramsdellite, with specific area 11.5 versus 81.4 m2/g. Different phase,
    area, composition and retained biomass prevent a phase-matched test of biological
    origin. A preliminary tissue-only null is stated without a dataset; no no-sorbent
    or sterile formation time series is displayed. The characterization pointer to
    reference15 (Murray1984) does not create a new 2009 XRD result.
- evidence_id: selectivity
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Original Figures7–8,Equation3 page2646 and Table2 page2647
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Figures support greater fractional Co than Ni depletion and inhibited Co
    uptake at higher Ni. Table 2 reports alpha_Co 7.92, 7.47 and 17.7 for biogenic
    material and 5.65, 2.23 and 2.65 for chemical material. Equation 3 defines the
    ratio of sorbed/aqueous mole-fraction quotients, which is dimensionless. These
    are not recovery percentages, purity or yields; no raw replicate dataset independently
    reproduces the exact coefficients. Co-only curves are separate comparators.
- evidence_id: redox
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Figures1–4,7–12; Table1 page2644 and Results discussion
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Mn release includes no-Co and no-Ni conditions and subsequently decreases;
    this does not establish a closed metal balance. Original XPS is interpreted as
    predominantly surface Co(III) and Ni(II), without proving complete bulk Co oxidation
    or measured CoOOH phase yield. Table 1 AOS values 3.09/3.68 differ from prose
    3.17/3.70; a stated lack of synthetic Mn(III) conflicts with fraction0.296. Figure
    12 is a proposed site diagram; vacancy/edge preference and coprecipitation are
    not directly imaged.
- evidence_id: assay-limits
  kind: primary_source
  reference: https://doi.org/10.2320/matertrans.M-M2009821
  locator: Section2,Figures1–6 and normalizedaxes on page2646
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Methods maxima Co1.7/Ni2.11 mmol/L differ from Figure2 Co2.19/Figure3 Ni2.31.
    Single-solute arms remain distinct from binary assays. Figure5 normalizes quantity
    to Mn(III,IV) mass excluding Mn(II), not the whole composite. Figures5–6 are fitted
    models rather than independent measurements. Different 2008 post-assay handling
    prevents pooling the papers as identical replicates.
- evidence_id: taxonomy
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/443224/dataset_report
  locator: Official current raw response independently read
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Taxon443224 retains exact Paraconiothyrium sp.WL-2 name atnominalspeciesrank.
    Unresolved named species and culture-stock authentication remain unasserted; noenzyme/functional
    gene assignment.
  snapshot_sha256: 2d97e5866e43400dfe134e084b344c55db139bf2f201a75ef37c04f940fd2004
- evidence_id: metadata
  kind: authority
  reference: https://www.jstage.jst.go.jp/article/matertrans/50/11/50_M-M2009821/_article
  locator: Current publisher metadata and Supplementarymaterial(0), author-acquired
    rawHTML independentlyread
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Finalpaginated journal/article metadata and no declaredseparateSI confirmed.
    Crossref exact DOI/title/authors/pages has emptyrelation and no update-to/updated-by
    fields. Noextra originaldata inferred.
  snapshot_sha256: 4a517ea8245c7f2186f6e25c84af399f2a9345146e023ab9af05e00b4304e8c3
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round42-birnessite-independent/notice-search.json
  locator: Reviewer fresh exact DOI correction/erratum/retraction query and exacttitle
    contradiction query
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Returnedsets identify no affecting formalnotice. Related structuralstudies
    are leads, notassessed refutations of thisspecificassay. Sourceinternalcontradictions
    remain explicit.
  search_scope: Two livewebqueries, firstreturned results only; currentpublisher/Crossref
    and wholeoriginal checked. Not exhaustiveabsence of notices/unpublished data.
  snapshot_sha256: 73505df1221cc6c5b09005c40872e2022105ab38acfe9456e09721b3bf3c3bb0
- evidence_id: preservation
  kind: record_content
  reference: /private/tmp/cmm-round42-birnessite-independent/evidence-check.json
  locator: Independent Git-base semantic and byte comparisons
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Every earlier field, including the description, remains unchanged. Mechanisms,
    sources, inline events and history references are exact prefixes; both committed
    history files are byte-identical. The exact base-record SHA matches the named
    round41 independent review. This review does not claim a fresh full reassessment
    of unchanged Wei2012, Ferrier2022 or Sasaki2008 literature.
  snapshot_sha256: c5d22d5e6de427e4c173256c580448cf93b48faa0ef147dfedad384d4138cea5
- evidence_id: prior-review
  kind: record_content
  reference: reviews/structured/20261012T012836Z-birnessite-round41-independent/review.yaml
  locator: Prior scientific assessment and exact input hash
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: Previously independentreviewed birnessite mechanisms retained. Root/packaging
    authored oldscience; presentreviewer also authored priorround41review independently.
    It chains to the unchangedWei2012 review with its declared sourcecoverage.
  snapshot_sha256: 8ff028f8cdbde5226774df40f408721622567b39a87916537a8f610c6f73d9e8
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round42-birnessite-independent/evidence-check.json
  locator: Hidden/ignored followed searches of current/original records,research,reviews,history
    and six relevant rawroots
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: There are 1189 matching text lines, exit0 and no errors. The same WL-2
    material lineage and related 2008/2009 papers are not independent culture-production
    replicates; the 2009 binary assay is a distinct reported observation.
  search_scope: rg --no-ignore --hidden --follow over explicit corpora and six retained
    source roots. Text derivatives only; no claim about unparsed binary content or
    machine-wide absence.
  snapshot_sha256: c5d22d5e6de427e4c173256c580448cf93b48faa0ef147dfedad384d4138cea5
- evidence_id: history
  kind: record_content
  reference: history/records/birnessite/2026-10-12T015436Z-codex-a24dff.yaml
  locator: New canonicalEDIT and separateinline event
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: The new canonical EDIT and separate inline event use actual codex/GPT-6/codex
    metadata and accurately describe the final scientific scope. Their timestamps
    differ honestly. Existing history remains immutable, and no automatic scientific
    approval is implied.
  snapshot_sha256: 76bac25843cd385f3fac82ac6bbd486c95561de7e1b615c6b5eef99550accaa4
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round42-final-terminal.json
  locator: Finalcohort receipt and independent raw-byte logverification
  accessed_at: '2026-10-12T02:04:09.038193Z'
  support: supports
  summary: All required commands finished with exit0; named-record validation was
    independently executed and checked one record with no failures. Frozen input hashes
    remain unchanged. Structural validation does not establish scientific truth.
  snapshot_sha256: a25cbb01ec2e6d41c20607099611dd95f796cfe264c28c29a012e8f5b64f235f
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral preparation and organism scope
  outcome: supported
  summary: The source-qualified poorly crystalline fungal oxide is accurately retained
    as a separate birnessite arm, without inflating mineral purity, strain authentication
    or criticality.
  target_ids:
  - cmmmech:birnessite
  evidence_ids:
  - target
  - identity-controls
  - taxonomy
  - prior-review
- assessment_id: experiment
  area: evidence
  topic: Binary Co/Ni sorption and selectivity
  outcome: supported
  summary: Original methods, curves, Equation3 and Table2 support preferential fractional
    cobalt sorption and correctly defined, source-reported coefficients.
  target_ids:
  - cmmmech:birnessite
  evidence_ids:
  - conditions
  - selectivity
  - primary
- assessment_id: limits
  area: evidence
  topic: Controls,redox and source contradictions
  outcome: supported
  summary: Material redox, normalization, concentration, phase/control and 2008/2009
    handling limitations are accurately retained. The unresolved causal route is not
    overstated.
  target_ids:
  - cmmmech:birnessite
  evidence_ids:
  - identity-controls
  - redox
  - assay-limits
- assessment_id: preserved
  area: provenance
  topic: Whole-record integration and prior scientific preservation
  outcome: supported
  summary: All earlier field values and history bytes are unchanged, and the prior
    review covers the exact base hash. Earlier literature coverage relies explicitly
    on that independent review.
  target_ids:
  - cmmmech:birnessite
  evidence_ids:
  - preservation
  - prior-review
  - history
- assessment_id: checks
  area: provenance
  topic: Exact-state independentreview and required checks
  outcome: supported
  summary: Native inspection preceded assessment; the complete new primary and original
    graphics were checked. Actual named and cohort gates were verified. No corrective
    maintained-record edit is needed.
  target_ids:
  - cmmmech:birnessite
  evidence_ids:
  - target
  - gates
  - dedup
  - metadata
  - notices
findings: []
actions: []
limitations:
- The source-assigned fungal birnessite lacks a new 2009 diffraction or purity measurement;
  the ramsdellite comparator cannot isolate biological origin.
- The prepared material has fungal origins, but active cells or metabolism during
  sorption were not measured.
- No displayed no-sorbent or sterile formation time series; preliminary tissue controls
  lack displayed data.
- Reported selectivity ratios lack a raw replicate dataset for independent exact reconstruction;
  they are not percentages or purified recovery.
- Surface ex situ XPS does not establish complete bulk cobalt oxidation, unique site
  occupancy or a quantified CoOOH phase.
- Table/prose manganese oxidation-state conflicts and single-solute loading discrepancies
  are preserved.
- Different normalization and post-assay handling prevent unqualified isotherm transfer
  or pooling of 2008 and 2009 assays.
- Real leachate scale-up, desorption/regeneration and industrial deployment were not
  established.
- Earlier scientific evidence is retained through the exact-hash prior review, not
  a fresh full reassessment here.
- Notice and deduplication searches are bounded; no exhaustive absence claim.
notes:
- The reviewer made no changes to maintained records, histories or source dossiers.
- Named validation was personally executed; coordinator batch logs were independently
  read and their raw-byte hashes verified.
links:
- https://doi.org/10.2320/matertrans.M-M2009821
- reviews/structured/20261012T012836Z-birnessite-round41-independent/review.md
```
