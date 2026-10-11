# Independent scientific review of K-jarosite culture-associated reductive dissolution

- Review: 20261011T215421Z-jarosite-round35-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T21:48:29.638922Z
- Finished UTC: 2026-10-11T21:54:21.425506Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Whole frozen jarosite record is defensible with its explicit quantitative, control, phase and causal limits. No corrective findings. Required named and corrected cohort checks passed on unchanged target hashes.

## Scope And Provenance

All fields of one frozen jarosite record, one mechanism, all source-specific evidence and distinct provenance events.

Selection: Parent-assigned independent review of another curator target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f83cf867a38c470b4347f721d9ea9370c3019eaf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:jarosite | data/records/jarosite.yaml | maintained | Jarosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:jarosite | Reviewer executed; Checked 1 record(s); 0 failed. Log /private/tmp/cmm-round35-jarosite-review-named.log, SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e. |
| Corrected final cohort batch | passed | True | cmmmech:jarosite | Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-batch.log SHA256 9801e41c5e7f39c58f9711c4b6a36747750740f6e2ccc7ea055ebc0db408af91. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 119.23s (0:01:59)<br>Checked 198 record(s); 0 failed.<br>Checked 229 history record(s); 0 error(s). |
| Corrected final cohort nonempty | passed | True | cmmmech:jarosite | Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-nonempty.log SHA256 1a7af2b5ea572ea7e356525122eadd4bbd64b3ce247bc0c1a7b3eb3b71865ae1. Checked 198 record(s); 0 failed. |
| Corrected final cohort history | passed | True | cmmmech:jarosite | Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-history.log SHA256 6a35723bdc6888001561b265c4859a17d59b55bb8c460f13518e2b9d72d87b64. Checked 229 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral species, strain and source boundary

identity: supported. Targets: cmmmech:jarosite.

IMA-grounded K-jarosite identity is separate from family, substitutions, waste feeds and elemental iron; NCBI species and sourceDSM 504scope match authorities. No criticality assertion.

### Controlled culture-associated dissolution and reduction

evidence: supported. Targets: cmmmech:jarosite.

Donor-matched controls and Fe/solid analyses support culture-associated enhancement; exclusive enzymatic respiration and living-growth cause are carefully not asserted. Missing oxygen/viability/filtrate/killed controls are retained.

### Numerical conflicts and product bounds

evidence: supported. Targets: cmmmech:jarosite.

The96.4/98.4source conflict, abiotic endpoint versus maxima, nonzero Fe(II) andK deficit are retained. Neither solution release nor absent Raman peaks is promoted to purified recovery orcomplete phase extinction.

### Independent input capture and terminal checks

provenance: supported. Targets: cmmmech:jarosite.

Reviewer authored schwertmannite, not jarosite. Native inspect preceded judgment, full target assessed andfrozen hashes match; independent named andparent corrected cohort checksverified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/jarosite.yaml; All fields in frozen record | supports | The full record remains identical to native pre-judgment capture. Reviewer did not author or edit it. |
| primary | https://doi.org/10.1016/j.hydromet.2022.105908; Complete Coventry accepted manuscript, PDF pages1-23; Methods2.1-2.4, Table 1, original Figures1-8 | supports | Original methods support potassium-jarosite feed preparation and donor-matched inoculated/uninoculated assays. 0.5g feed per50mL, sulfur-equivalent 10 g/L,4 x 10^8 cells/mL, initial pH 1.94,30 degrees C, 180 rpm,N2/CO2sealedbatches,34 days,duplicate assays. Record appropriately limits direct respiration, complete dissolution and isolated recovery. Accepted-manuscript version is explicit. |
| quantitative | https://doi.org/10.1016/j.hydromet.2022.105908; Table 1; Figure2a-c; abstract, manuscript line 246 and conclusion; original PDFpages3,9-11,19 | supports | Table 1 has lowerK than idealjarosite. 96.4% line 246 differs from98.4% abstract/conclusion; Figure 2c near-complete signal does not reconcile exact values. Dissolved Fe(II) is calculated total minus ferric underMethods 2.4. Fe(II) decreases at some late times; solution concentrations and source-defined extents are not product yield or full Fe balance. |
| solid | https://doi.org/10.1016/j.hydromet.2022.105908; Original Figures4-8; PDFpages14-19 | supports | SEM/Raman/Fe L-edge/sulfur K-edge independently viewed. Sulfite culture residue loses recognizable jarosite Raman features and has a spectrum resembling ferrous sulfate standard; chemical controls retain jarosite features. This supports substantial transformation without quantified detection limits, phase purity or an isolated crystalline product. Thiosulfate yields elemental S signatures in both biotic and abiotic residues. |
| supplement | https://pure.coventry.ac.uk/ws/files/65409385/Post_Print.pdf; Appended SI cover and all four original figures S1-S4, PDFpages24-28 | supports | S1 shows initial powder; S2 endpoints 1.3/6.3/8.5% differs from maxima 1.5/6.3/8.7%; S3 abiotic dissolvedFe is low but nonzero. S4 abiotic thiosulfate pH rises toward 2.8 and includes extra Na2SO4 arm not described among Methods donors. Record retains these conflicts and avoids zero-control and matched pH claims. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 master list, original row onpage 104, visuallyinspected | supports | Jarosite is KFe(III)3(SO4)2(OH)6, redefined1987 s.p.; retained same-day officiallist reused and its PDF/row inspected. Species distinct from family members and jarosite-bearing wastes. |
| ncbi | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&amp;mode=Info; Live official species page independently opened plus retainedHTML | supports | NCBITaxon 930 resolves Acidithiobacillus thiooxidans at species rank. It is not the strain identifier. |
| dsm | https://www.dsmz.de/collection/catalogue/details/culture/DSM-504; Live official DSM 504 catalogue independently opened and collectionequivalents checked | supports | DSM 504 is A. thiooxidans; ATCC 8085 andNCIMB 9112 equivalents agree. The primary strain was obtained from Changsha laboratory, not necessarily directly from DSMZ. |
| history | history/records/jarosite/2026-10-11T214126Z-codex-bd6b8a.yaml; Entire CREATE sidecar and distinct inline CREATE | supports | Sidecar21:41:26Z and inline21:41:36.525409+00:00 have actual codex/GPT-6/codex attribution and matching target/change. No fabricated prior authorship. |
| notices | /private/tmp/cmm-round35-jarosite-independent/search-assessment.json; Exact DOI correction/retraction and title/thiooxidans contradiction queries; fresh retainedCrossref and independently openedpublisher/repository metadata | supports | No affecting notice surfaced in bounded returned results; Crossref update fields absent/relation empty. Related laterite or sulfur reduction studies are different assays and not newly imported evidence. This does not prove global absence. |
| dedup | /private/tmp/cmm-round35-jarosite-independent/dedup.txt; Hidden/ignored-inclusive current worktree relevant paths | supports | Existing contextual jarosite mineral mentions in other records do not duplicate this K-species record or its selected 2022 assay. No broad machine-wide absence claim. |
| gates | /private/tmp/cmm-round35-corrected-final-terminal.json; All corrected final commands and logs | supports | Named and corrected final cohort checks pass on unchanged exact reviewed target bytes. Root executed cohort gates; reviewer independently verified hashes and read logs. |

## Limits And Additional Notes

- Complete publicly retained author-accepted manuscript including SI was inspected, not a separately acquired publisher-version PDF; source version is explicit.
- Source 96.4/98.4 percent discrepancy remains unresolved; percentage formula andclosed Fe inventory are absent.
- Nominal anaerobic setup has no measured O2 time course, pH-clamped controls, independent viability assessment orcell-free/killed-cell assay to isolate causality.
- XRD/Raman/XANES phase assignments do not establish absolute purity orcomplete absence without detection limits; ferrous-like residues are not recovered pure FeSO4 product.
- Bounded notice and contradiction searches are not exhaustive and do not establish absence across all literature.
- All original Figures1-8, Table 1 and appended S1-S4 independently inspected; sourceconstraints already qualified in record are not manufactured corrective findings.
- Reviewer did not change maintained jarosite input bytes. Schwertmannite correction elsewhere in cohort is outside this scientific target.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T215421Z-jarosite-round35-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of K-jarosite culture-associated reductive dissolution
started_at: '2026-10-11T21:48:29.638922Z'
finished_at: '2026-10-11T21:54:21.425506Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Jarosite was curated by /root. Reviewer authored schwertmannite
    only in this cohort and did not edit jarosite/history/source dossier. Shared worktree
    and curator-acquired original artifacts disclosed; original evidence independently
    read after native inspect.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Whole frozen jarosite record is defensible with its explicit quantitative,
  control, phase and causal limits. No corrective findings. Required named and corrected
  cohort checks passed on unchanged target hashes.
source:
  git_revision: f83cf867a38c470b4347f721d9ea9370c3019eaf
  state: working_tree
  inputs:
  - path: data/records/jarosite.yaml
    sha256: 5642b5560b9d351f581fab9725486c440b4a3a0e6e4978c78478898e172b011b
    role: target
  - path: history/records/jarosite/2026-10-11T214126Z-codex-bd6b8a.yaml
    sha256: a9c21ce2f60f66f3e5f25d2be7be21062b31ec7bdacc2fcc48a90c8890e5ef95
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields of one frozen jarosite record, one mechanism, all source-specific
    evidence and distinct provenance events.
  selection: Parent-assigned independent review of another curator target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:jarosite
  exclusions:
  - target: Raw instrument refitting and unrelated jarosite studies
    reason: Published primary and SI independently checked; no new analysis orsource
      import.
targets:
- target_id: cmmmech:jarosite
  path: data/records/jarosite.yaml
  label: Jarosite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/jarosite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked
    cmmmech validate data/records/jarosite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed; Checked 1 record(s); 0 failed. Log /private/tmp/cmm-round35-jarosite-review-named.log,
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e.
  target_ids:
  - cmmmech:jarosite
- check_id: batch
  name: Corrected final cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-batch.log
    SHA256 9801e41c5e7f39c58f9711c4b6a36747750740f6e2ccc7ea055ebc0db408af91. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 119.23s (0:01:59)

    Checked 198 record(s); 0 failed.

    Checked 229 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:jarosite
- check_id: nonempty
  name: Corrected final cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-nonempty.log
    SHA256 1a7af2b5ea572ea7e356525122eadd4bbd64b3ce247bc0c1a7b3eb3b71865ae1. Checked
    198 record(s); 0 failed.
  target_ids:
  - cmmmech:jarosite
- check_id: history
  name: Corrected final cohort history
  command: uv run --locked cmmmech validate-history --base f83cf867a38c470b4347f721d9ea9370c3019eaf
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read and hash-verified /private/tmp/cmm-round35-corrected-final-history.log
    SHA256 6a35723bdc6888001561b265c4859a17d59b55bb8c460f13518e2b9d72d87b64. Checked
    229 history record(s); 0 error(s).
  target_ids:
  - cmmmech:jarosite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/jarosite.yaml
  locator: All fields in frozen record
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: The full record remains identical to native pre-judgment capture. Reviewer
    did not author or edit it.
  snapshot_sha256: 5642b5560b9d351f581fab9725486c440b4a3a0e6e4978c78478898e172b011b
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.hydromet.2022.105908
  locator: Complete Coventry accepted manuscript, PDF pages1-23; Methods2.1-2.4, Table
    1, original Figures1-8
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Original methods support potassium-jarosite feed preparation and donor-matched
    inoculated/uninoculated assays. 0.5g feed per50mL, sulfur-equivalent 10 g/L,4
    x 10^8 cells/mL, initial pH 1.94,30 degrees C, 180 rpm,N2/CO2sealedbatches,34
    days,duplicate assays. Record appropriately limits direct respiration, complete
    dissolution and isolated recovery. Accepted-manuscript version is explicit.
  snapshot_sha256: f458a0d2e86fd8a19c41575aa78029006783e844ec52a0c662c9b510598a2ce2
- evidence_id: quantitative
  kind: primary_source
  reference: https://doi.org/10.1016/j.hydromet.2022.105908
  locator: Table 1; Figure2a-c; abstract, manuscript line 246 and conclusion; original
    PDFpages3,9-11,19
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Table 1 has lowerK than idealjarosite. 96.4% line 246 differs from98.4%
    abstract/conclusion; Figure 2c near-complete signal does not reconcile exact values.
    Dissolved Fe(II) is calculated total minus ferric underMethods 2.4. Fe(II) decreases
    at some late times; solution concentrations and source-defined extents are not
    product yield or full Fe balance.
  snapshot_sha256: f458a0d2e86fd8a19c41575aa78029006783e844ec52a0c662c9b510598a2ce2
- evidence_id: solid
  kind: primary_source
  reference: https://doi.org/10.1016/j.hydromet.2022.105908
  locator: Original Figures4-8; PDFpages14-19
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: SEM/Raman/Fe L-edge/sulfur K-edge independently viewed. Sulfite culture
    residue loses recognizable jarosite Raman features and has a spectrum resembling
    ferrous sulfate standard; chemical controls retain jarosite features. This supports
    substantial transformation without quantified detection limits, phase purity or
    an isolated crystalline product. Thiosulfate yields elemental S signatures in
    both biotic and abiotic residues.
  snapshot_sha256: f458a0d2e86fd8a19c41575aa78029006783e844ec52a0c662c9b510598a2ce2
- evidence_id: supplement
  kind: primary_source
  reference: https://pure.coventry.ac.uk/ws/files/65409385/Post_Print.pdf
  locator: Appended SI cover and all four original figures S1-S4, PDFpages24-28
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: S1 shows initial powder; S2 endpoints 1.3/6.3/8.5% differs from maxima
    1.5/6.3/8.7%; S3 abiotic dissolvedFe is low but nonzero. S4 abiotic thiosulfate
    pH rises toward 2.8 and includes extra Na2SO4 arm not described among Methods
    donors. Record retains these conflicts and avoids zero-control and matched pH
    claims.
  snapshot_sha256: f458a0d2e86fd8a19c41575aa78029006783e844ec52a0c662c9b510598a2ce2
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September2026 master list, original row onpage 104, visuallyinspected
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Jarosite is KFe(III)3(SO4)2(OH)6, redefined1987 s.p.; retained same-day
    officiallist reused and its PDF/row inspected. Species distinct from family members
    and jarosite-bearing wastes.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: ncbi
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info
  locator: Live official species page independently opened plus retainedHTML
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: NCBITaxon 930 resolves Acidithiobacillus thiooxidans at species rank. It
    is not the strain identifier.
  snapshot_sha256: ccb7193588d181feb9d728dd1949805f36d04fc448e89a2a798552b2572c79c9
- evidence_id: dsm
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-504
  locator: Live official DSM 504 catalogue independently opened and collectionequivalents
    checked
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: DSM 504 is A. thiooxidans; ATCC 8085 andNCIMB 9112 equivalents agree. The
    primary strain was obtained from Changsha laboratory, not necessarily directly
    from DSMZ.
  snapshot_sha256: 5ec0de034b3c0b34a660dc47904a866be2e11d566a979f2bf3f2609455ce1099
- evidence_id: history
  kind: record_content
  reference: history/records/jarosite/2026-10-11T214126Z-codex-bd6b8a.yaml
  locator: Entire CREATE sidecar and distinct inline CREATE
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Sidecar21:41:26Z and inline21:41:36.525409+00:00 have actual codex/GPT-6/codex
    attribution and matching target/change. No fabricated prior authorship.
  snapshot_sha256: a9c21ce2f60f66f3e5f25d2be7be21062b31ec7bdacc2fcc48a90c8890e5ef95
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round35-jarosite-independent/search-assessment.json
  locator: Exact DOI correction/retraction and title/thiooxidans contradiction queries;
    fresh retainedCrossref and independently openedpublisher/repository metadata
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: No affecting notice surfaced in bounded returned results; Crossref update
    fields absent/relation empty. Related laterite or sulfur reduction studies are
    different assays and not newly imported evidence. This does not prove global absence.
  snapshot_sha256: 380c79515170423e119bcb1d064af2b3ba67578e5c8aea4f9d87c53de773e3ad
  search_scope: Two exact queries as recorded; first web result sets, no exhaustive
    citation crawl. Publisher metadata and institutionalfull accepted manuscript distinguish
    version bounds.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round35-jarosite-independent/dedup.txt
  locator: Hidden/ignored-inclusive current worktree relevant paths
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Existing contextual jarosite mineral mentions in other records do not duplicate
    this K-species record or its selected 2022 assay. No broad machine-wide absence
    claim.
  snapshot_sha256: 0f6e410f6214234e71e0b835af45338285425bf674375e72b8645a9862eb2b44
  search_scope: rg --hidden --no-ignore --follow jarosite|105908 over data/records,
    research, reviews, history in round35 worktree; actual output retained.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round35-corrected-final-terminal.json
  locator: All corrected final commands and logs
  accessed_at: '2026-10-11T21:54:21.425506Z'
  support: supports
  summary: Named and corrected final cohort checks pass on unchanged exact reviewed
    target bytes. Root executed cohort gates; reviewer independently verified hashes
    and read logs.
  snapshot_sha256: 3cebf17ce0815a56ce35c4e7c9485ce4ec9f574b670b40f37e458b69616bf3e4
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species, strain and source boundary
  outcome: supported
  summary: IMA-grounded K-jarosite identity is separate from family, substitutions,
    waste feeds and elemental iron; NCBI species and sourceDSM 504scope match authorities.
    No criticality assertion.
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - record
  - ima
  - ncbi
  - dsm
  - dedup
  dimensions:
  - name: material_form
    value: Mineral species; biosynthesized nonideal laboratory feed
    definition: Potassium jarosite phase assigned by XRD; elemental composition does
      not provepure endmember.
    evidence_ids:
    - primary
    - ima
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim is made.
    evidence_ids:
    - record
  - name: organism
    value: A. thiooxidans DSM 504; speciesnode930
    definition: Collection label and species rank are distinct;Acidianus manzaensis
      feed production is separate.
    evidence_ids:
    - primary
    - ncbi
    - dsm
- assessment_id: mechanism
  area: evidence
  topic: Controlled culture-associated dissolution and reduction
  outcome: supported
  summary: Donor-matched controls and Fe/solid analyses support culture-associated
    enhancement; exclusive enzymatic respiration and living-growth cause are carefully
    not asserted. Missing oxygen/viability/filtrate/killed controls are retained.
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - primary
  - solid
  - supplement
  - record
  dimensions:
  - name: biomass
    value: Inoculated cultures; initial4 x 10^8 cells/mL
    definition: Counts of planktonic cells do not measure viability oriron-respiratory
      yield.
    evidence_ids:
    - primary
  - name: conditions
    value: Nominal anaerobic 34-day laboratory batches, 30 degrees C, initial pH 1.94
    definition: 50 mL in 150 mL bottles,0.5 g feed,N2/CO2 purge,10 g/L sulfur-equivalent,duplicate
      assays.
    evidence_ids:
    - primary
  - name: controls
    value: Each sulfur donor has uninoculated sterile control
    definition: No matched pH-clamped, killed-cell orcell-free filtrate panel.
    evidence_ids:
    - primary
    - supplement
- assessment_id: quantities
  area: evidence
  topic: Numerical conflicts and product bounds
  outcome: supported
  summary: The96.4/98.4source conflict, abiotic endpoint versus maxima, nonzero Fe(II)
    andK deficit are retained. Neither solution release nor absent Raman peaks is
    promoted to purified recovery orcomplete phase extinction.
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - quantitative
  - solid
  - supplement
  - record
  dimensions:
  - name: measurements
    value: Dissolved Fe g/L; source-defined extent percent; bulk elemental percent
    definition: Fe(II)calculatedbydifference; explicit extent formula/full mass balance
      unavailable.
    evidence_ids:
    - quantitative
  - name: deployment
    value: Laboratory reagent-derived feed dissolution
    definition: No mixed ore, industrial waste orcommercial benefit demonstrated.
    evidence_ids:
    - primary
    - record
- assessment_id: provenance
  area: provenance
  topic: Independent input capture and terminal checks
  outcome: supported
  summary: Reviewer authored schwertmannite, not jarosite. Native inspect preceded
    judgment, full target assessed andfrozen hashes match; independent named andparent
    corrected cohort checksverified.
  target_ids:
  - cmmmech:jarosite
  evidence_ids:
  - record
  - history
  - gates
  - notices
findings: []
actions: []
limitations:
- Complete publicly retained author-accepted manuscript including SI was inspected,
  not a separately acquired publisher-version PDF; source version is explicit.
- Source 96.4/98.4 percent discrepancy remains unresolved; percentage formula andclosed
  Fe inventory are absent.
- Nominal anaerobic setup has no measured O2 time course, pH-clamped controls, independent
  viability assessment orcell-free/killed-cell assay to isolate causality.
- XRD/Raman/XANES phase assignments do not establish absolute purity orcomplete absence
  without detection limits; ferrous-like residues are not recovered pure FeSO4 product.
- Bounded notice and contradiction searches are not exhaustive and do not establish
  absence across all literature.
notes:
- All original Figures1-8, Table 1 and appended S1-S4 independently inspected; sourceconstraints
  already qualified in record are not manufactured corrective findings.
- Reviewer did not change maintained jarosite input bytes. Schwertmannite correction
  elsewhere in cohort is outside this scientific target.
links:
- https://doi.org/10.1016/j.hydromet.2022.105908
- https://pure.coventry.ac.uk/ws/files/65409385/Post_Print.pdf
```
