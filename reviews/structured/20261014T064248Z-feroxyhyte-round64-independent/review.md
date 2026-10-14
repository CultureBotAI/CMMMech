# Independent scientific review of conditional CN32 feroxyhyte transformation

- Review: 20261014T064248Z-feroxyhyte-round64-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T06:34:25.996316Z
- Finished UTC: 2026-10-14T06:42:48.068190Z
- Reviewer: codex /root/round64_manganese (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record correctly identifies feroxyhyte and retains a condition-specific laboratory CN32 culture-associated reduction and secondary-mineral observation. It accurately preserves the sterile diffraction control, missing matched sterile kinetics, partial total iron reduction, unequal endpoints, source caption conflict and culture-accession discrepancy. No supported curation defect was found in the retained claims.

## Scope And Provenance

Field-by-field scientific review of the assigned mineral record, linked CREATE history, frozen source dossier and claimed primary/authority evidence.

Selection: Assigned exact path and frozen SHA256 6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61. Native inspect captured all four working-tree inputs before assessment; started_at is the actual inspect receipt filesystem UTC timestamp.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:feroxyhyte | data/records/feroxyhyte.yaml | maintained | Feroxyhyte |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:feroxyhyte | Reviewer execution 2026-10-14T06:36:47.623803+00:00 to 2026-10-14T06:36:59.108694+00:00; Checked 1 record(s); 0 failed. |
| Trusted-base canonical history validation | passed | True | cmmmech:feroxyhyte | Reviewer execution 2026-10-14T06:36:59.108769+00:00 to 2026-10-14T06:37:12.022198+00:00; Checked 342 history record(s); 0 error(s). |
| Full batch checks | passed | True | cmmmech:feroxyhyte | Coordinator execution 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00; exit 0. Actual final receipt and log inspected. |
| Explicit nonempty corpus validation | passed | True | cmmmech:feroxyhyte | Coordinator execution 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00; exit 0. Actual final receipt and log inspected. |

## Scientific And Domain Assessments

### Mineral species and material boundary

identity: supported. Targets: cmmmech:feroxyhyte.

IMA approval and formula are correct. The laboratory synthetic mineral is not a natural ore, elemental iron or a mixed secondary product. No criticality is inherited from iron.

### Organism, biomass, substrate and conditions

evidence: supported. Targets: cmmmech:feroxyhyte.

The record preserves the named CN32 culture, synthetic substrate and explicit 2021 treatment conditions without reconstructing absent inherited recipes or authenticating the stock.

### Causal scope and experimental controls

evidence: supported. Targets: cmmmech:feroxyhyte.

Actual sterile-control diffraction is recognized, while unreported matched sterile kinetics and amendment metadata limit microbial-increment quantification. Molecular and biological-necessity claims are not overextended.

### Measurements, phase assignment and deployment

quantity: supported. Targets: cmmmech:feroxyhyte.

The retained outcome is acid-extractable Fe(II) plus condition-dependent mixed secondary solids. The record correctly avoids complete reduction, dissolved-only Fe(II), recovered mass fractions and industrial deployment.

### Internal contradictions and transfer limits

evidence: supported. Targets: cmmmech:feroxyhyte.

The record preserves the Figure 23 timing conflict, unlike endpoint durations and plateau versus total-reduction distinction. Independent abstract-level comparison supports keeping mineral morphology and organism context explicit.

### Source, history and actual validation

provenance: supported. Targets: cmmmech:feroxyhyte.

DOI, IMA approval, taxon mapping and claim locators are supported; the collection-number conflict is explicit. Named and trusted-base history validation passed. All 37 raw artifacts in the frozen dossier were rehashed with zero mismatches.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/feroxyhyte.yaml; Entire frozen file and all four claim-level evidence entries | supports | Read every field; no scientific or provenance input was edited by this reviewer. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF pages 1 and 68; column definitions and Feroxyhyte row | supports | Personally inspected rendered authority pages. Feroxyhyte is Fe3+O(OH), status A, approval number 1975-032. This is a distinct mineral species; the IMA approval number is not a commodity identifier. Reused same-round authority acquisition and verified its hash. |
| primary | https://doi.org/10.3390/min11020149; Complete 43-page original available; Sections 2.1–2.3, 3.7, 4.1–4.4; Figures 22–24; Tables 4–5 | supports | Independently read the relevant original methods, results and discussion, and personally inspected Figures 22–24 and Tables 4–5. Peroxide-synthesized, washed, dried and sieved feroxyhyte was supplied to duplicate anoxic CN32 cultures with formate. pXRD, microscopy and selected Mossbauer fits support conditional transformation to Fe(II)-bearing mixed solids. Original retained outside Git at /private/tmp/cmm-round64-iron-research/oloughlin2021.pdf. |
| measurement | https://doi.org/10.3390/min11020149; Sections 2.3 and 3.7; Figure 22; Table 4, PDF pages 4–5, 18 and 24–25 | supports | Fe(II) is the one-week HCl-extractable suspension pool measured by ferrozine, with added acid for magnetite, not dissolved Fe(II). Day-78 phosphate-free endpoints are 24.28 +/- 2.10 and 24.51 +/- 6.02 mM, about 30% of 80 mM initial Fe(III). Phosphate arms end at day 156 with 55.07 +/- 2.92 and 59.93 +/- 1.65 mM. Maximum sustained production rates use regression; none is an instantaneous enzymatic rate. |
| controls | https://doi.org/10.3390/min11020149; Sections 2.2–2.3 and 3.7; Figure 23; Table 4 | partial | Figure 23 actually contains a sterile-control diffraction trace with starting feroxyhyte peaks. Neither that trace nor the methods supplies a matched sterile Fe(II) kinetic series and fully specified control amendments/age. All phosphate arms contain AQDS; no phosphate-amended AQDS-free arm, killed-cell, cell-free-metabolite or mutant comparison is reported for this retained experiment. The record limits microbial-increment and molecular-causality claims accordingly. |
| contradictions | https://doi.org/10.3390/min11020149; Section 3.7; Figure 23 labels/caption; Tables 4–5; Section 4.2 | partial | The plotted XRD labels give 78 or 156 days while the caption says 46 days. The phrase essentially complete bioreduction refers to a plateau, not reduction of all supplied Fe(III), as the measured phosphate-free fraction is about 30%. Table 4 marks the high-phosphate SEM green-rust assignment GR? and supplies no Mossbauer result for that arm. Table 5 relative spectral areas are not recovered mass fractions. These conflicts and limits are accurately preserved. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=319224; Same-round NCBI XML plus fresh independent browser access | supports | The authority label is Shewanella putrefaciens CN-32, with equivalent strain names. Retained XML rank is strain; browser rendering uses no rank. Neither authenticates the actual experimental stock. The record relies on the named-strain label and explicitly preserves the collection-number conflict. |
| atcc_cn32 | https://www.atcc.org/products/baa-453; Retained original authority HTML title and strain designation | supports | BAA-453 is Shewanella putrefaciens, strain CN-32 [OCM 576, SMCC 576W]. Independently read the same-round downloaded authority content; fresh web-tool access returned an internal error, not contradictory authority data. |
| atcc_other | https://www.atcc.org/products/baa-543; Retained original authority HTML title and strain designation | supports | BAA-543 is Cellulomonas sp., strain ES5, unlike CN32. The source prints BAA-543 beside CN32; preserving this unresolved provenance conflict is correct. Independent fresh web-tool access failed, so the retained same-round original HTML was used. |
| metadata | https://api.crossref.org/works/10.3390/min11020149; Same-round Crossref response, title/DOI/date/relation/update-to/license fields versus original page 1 | supports | Title, DOI and 31 January 2021 publication agree. Retained response has empty relation and no update-to field, with CC BY 4.0 license. The actual retained PDF has 43 pages; a current publisher search representation says 44 pages, so this review identifies the exact original PDF rather than inferring a substantive update from page-count metadata. |
| notices | /private/tmp/cmm-round64-feroxyhyte-independent/web-search.json; Initial independent live queries and authority opens, followed by web-search-followup.json | context_only | Returned exact DOI/title correction searches did not identify a correction or retraction. Primary-source leads include Cutting 2009 (10.1016/j.gca.2009.04.009) and a later Sb-bearing ferrihydrite study; these were screened at abstract level only, not accepted as new mechanisms or full replication evidence. |
| counterevidence | https://research.manchester.ac.uk/en/publications/mineralogical-and-morphological-constraints-on-the-reduction-of-f/; Author-institution record and abstract for Cutting et al. 2009; retained in web-search-followup.json | context_only | The original-study abstract reports substantially different initial reduction rates for two synthetic feroxyhytes with similar surface areas but different crystallinities, and warns about aggregation/spectrophotometric normalization. This supports the curated condition-specific scope. Its reported AQDS effect in Geobacter is not a contradiction of the narrowly stated CN32 result; no rates or additional organism mechanism were imported without the full original. |
| history | history/records/feroxyhyte/2026-10-14T062756Z-codex-bd8d5e.yaml; Entire canonical CREATE session and inline created event | supports | Canonical CREATE records codex/GPT-6/codex at 06:27:56Z with the correct target and bounded scientific changes. Inline creation at 06:28:06Z is a distinct actual event. No historical authorship or reviewer authorship was invented. |
| local_search | /private/tmp/cmm-round64-feroxyhyte-independent/local-search.txt; Exact mineral name, IMA number and DOI search in maintained records, structured reviews and history | context_only | Only the new feroxyhyte record/history matched these terms within the independently searched roots at review time. Broader discovery dossier dedup is separate. Hidden and ignored files and symlinks were included; no machinewide or unsearched-root absence is claimed. |
| named_validation | /private/tmp/cmm-round64-feroxyhyte-independent/named.log; Entire actual output and checks.json command timestamps | supports | Executed by this reviewer: Checked 1 record(s); 0 failed; exit 0. |
| history_validation | /private/tmp/cmm-round64-feroxyhyte-independent/history.log; Entire actual output and checks.json command timestamps | supports | Executed by this reviewer against base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb: Checked 342 history record(s); 0 error(s); exit 0. |
| batch_validation | /private/tmp/cmm-round64-final-gates.json; Coordinator round64 command receipt and entire final-gates.log | supports | Coordinator just check and explicit --require-records passed against this unchanged feroxyhyte record. Actual command receipts and complete log were inspected. Log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99. An unrelated lepidocrocite correction landed during the batch run, so the coordinator will rerun whole-batch gates after that correction. This review does not attest that correction or the later saved review bundle. |

## Limits And Additional Notes

- Experimental stock authentication is unresolved because the paper prints ATCC BAA-543 beside CN32, while collection authority assigns CN32 to BAA-453.
- Sterile-control diffraction exists, but matched sterile Fe(II) kinetics and complete control amendment/time metadata are not supplied. Unique biological necessity and electron-transfer pathways remain unresolved.
- All phosphate-amended cultures also contain AQDS; conclusions cannot be generalized to shuttle-free phosphate treatments.
- Figure 23 caption says 46 days while traces say 78/156 days. The record preserves this and does not invent a common harvest time.
- Acid-extractable Fe(II), nondetection of starting mineral and selected Mossbauer spectral areas do not establish complete iron reduction, pure-phase yield or isolated product recovery.
- The high-phosphate SEM green-rust assignment is tentative and lacks a Mossbauer result for that arm. pXRD-based mixed-phase assignments remain the source-supported scope.
- Earlier complete medium/inoculum recipes were not reconstructed. Other studies were screened only at primary abstract level; no literature-wide completeness or full replication check is claimed.
- Fresh ATCC web-tool opens failed. Same-round original authority HTML was independently read and checksum-verified; the exact access limitation is retained.
- Corrections made by this reviewer: none. All four inspected record/history/dossier inputs remain byte-identical. No external issue or comment was posted by this reviewer.
- The actual review start is anchored to inspect.json mtime 2026-10-14T06:34:25.996316Z. Evidence-access timestamps here denote completion of this review pass, not fresh acquisition of every reused source.
- Empty findings is scoped to the accepted record claims; it does not remove the reported source limitations or endorse unrelated experiments.
- The coordinator reported an unrelated lepidocrocite correction during the recorded batch gate. All four feroxyhyte inputs remained frozen and were rehashed before save. A later whole-batch rerun is a coordinator publication gate, not an unexecuted check claimed by this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T064248Z-feroxyhyte-round64-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of conditional CN32 feroxyhyte transformation
started_at: '2026-10-14T06:34:25.996316Z'
finished_at: '2026-10-14T06:42:48.068190Z'
reviewer:
  identity: codex /root/round64_manganese
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from feroxyhyte curator /root/round64_lithium.
    Reviewer did not author or edit this record, its history or dossier. Reviewer
    independently read the original experimental sections and authority content and
    inspected the relevant figures/tables; reviewer authored only unrelated manganese
    records in this batch.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record correctly identifies feroxyhyte and retains a condition-specific
  laboratory CN32 culture-associated reduction and secondary-mineral observation.
  It accurately preserves the sterile diffraction control, missing matched sterile
  kinetics, partial total iron reduction, unequal endpoints, source caption conflict
  and culture-accession discrepancy. No supported curation defect was found in the
  retained claims.
source:
  git_revision: 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  state: working_tree
  inputs:
  - path: data/records/feroxyhyte.yaml
    sha256: 6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61
    role: target
  - path: history/records/feroxyhyte/2026-10-14T062756Z-codex-bd8d5e.yaml
    sha256: b762f1dac09b715e8c8c31f8d717011af630da47dc076353bc50809e6f974908
    role: context
  - path: research/sources/round64-feroxyhyte/20261014T063035Z-source-investigation.json
    sha256: 4283c790a750e63c5a6fa9abe7096d8951093708f9ff021ab167ef39a3811f8a
    role: context
  - path: research/sources/round64-feroxyhyte/20261014T063035Z-source-investigation.md
    sha256: e0d8a56517c7618a8a8333aa5ed8bddc2be34e6da0fc098ab296a7cdf6a632d6
    role: context
scope:
  description: Field-by-field scientific review of the assigned mineral record, linked
    CREATE history, frozen source dossier and claimed primary/authority evidence.
  selection: Assigned exact path and frozen SHA256 6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61.
    Native inspect captured all four working-tree inputs before assessment; started_at
    is the actual inspect receipt filesystem UTC timestamp.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:feroxyhyte
  exclusions:
  - target: Other mineral systems in the 43-page source
    reason: Shared methods/discussion were checked, but no independent scientific
      acceptance of other records or every unrelated figure is claimed.
  - target: Earlier inoculum and basal-medium preparation references
    reason: Full inherited recipes were not acquired/reconstructed. The curated record
      explicitly delegates them and does not invent their composition.
  - target: Cutting 2009 and later Sb-bearing ferrihydrite study
    reason: Only primary abstract-level leads were checked for scope and conflicting
      trends. Full originals, figures and controls were not assessed and no new mechanism
      was imported.
targets:
- target_id: cmmmech:feroxyhyte
  path: data/records/feroxyhyte.yaml
  label: Feroxyhyte
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/feroxyhyte.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Named record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/feroxyhyte.yaml
  status: passed
  required: true
  summary: Reviewer execution 2026-10-14T06:36:47.623803+00:00 to 2026-10-14T06:36:59.108694+00:00;
    Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:feroxyhyte
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named_validation
- check_id: history
  name: Trusted-base canonical history validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate-history --base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  status: passed
  required: true
  summary: Reviewer execution 2026-10-14T06:36:59.108769+00:00 to 2026-10-14T06:37:12.022198+00:00;
    Checked 342 history record(s); 0 error(s).
  target_ids:
  - cmmmech:feroxyhyte
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history_validation
- check_id: batch
  name: Full batch checks
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00;
    exit 0. Actual final receipt and log inspected.
  target_ids:
  - cmmmech:feroxyhyte
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_validation
- check_id: nonempty
  name: Explicit nonempty corpus validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00;
    exit 0. Actual final receipt and log inspected.
  target_ids:
  - cmmmech:feroxyhyte
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/feroxyhyte.yaml
  locator: Entire frozen file and all four claim-level evidence entries
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Read every field; no scientific or provenance input was edited by this
    reviewer.
  snapshot_sha256: 6d33c03a73ed8b43201efd8608536cf213bf5625af78b85d0326fb0342fc4c61
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF pages 1 and 68; column definitions and Feroxyhyte row
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Personally inspected rendered authority pages. Feroxyhyte is Fe3+O(OH),
    status A, approval number 1975-032. This is a distinct mineral species; the IMA
    approval number is not a commodity identifier. Reused same-round authority acquisition
    and verified its hash.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min11020149
  locator: Complete 43-page original available; Sections 2.1–2.3, 3.7, 4.1–4.4; Figures
    22–24; Tables 4–5
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Independently read the relevant original methods, results and discussion,
    and personally inspected Figures 22–24 and Tables 4–5. Peroxide-synthesized, washed,
    dried and sieved feroxyhyte was supplied to duplicate anoxic CN32 cultures with
    formate. pXRD, microscopy and selected Mossbauer fits support conditional transformation
    to Fe(II)-bearing mixed solids. Original retained outside Git at /private/tmp/cmm-round64-iron-research/oloughlin2021.pdf.
  snapshot_sha256: 9da3ec0eebfa8b05a9aec4398fa45a80748c9f212b153f6010a695a2d6cdb062
- evidence_id: measurement
  kind: primary_source
  reference: https://doi.org/10.3390/min11020149
  locator: Sections 2.3 and 3.7; Figure 22; Table 4, PDF pages 4–5, 18 and 24–25
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Fe(II) is the one-week HCl-extractable suspension pool measured by ferrozine,
    with added acid for magnetite, not dissolved Fe(II). Day-78 phosphate-free endpoints
    are 24.28 +/- 2.10 and 24.51 +/- 6.02 mM, about 30% of 80 mM initial Fe(III).
    Phosphate arms end at day 156 with 55.07 +/- 2.92 and 59.93 +/- 1.65 mM. Maximum
    sustained production rates use regression; none is an instantaneous enzymatic
    rate.
  snapshot_sha256: 9da3ec0eebfa8b05a9aec4398fa45a80748c9f212b153f6010a695a2d6cdb062
- evidence_id: controls
  kind: primary_source
  reference: https://doi.org/10.3390/min11020149
  locator: Sections 2.2–2.3 and 3.7; Figure 23; Table 4
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: partial
  summary: Figure 23 actually contains a sterile-control diffraction trace with starting
    feroxyhyte peaks. Neither that trace nor the methods supplies a matched sterile
    Fe(II) kinetic series and fully specified control amendments/age. All phosphate
    arms contain AQDS; no phosphate-amended AQDS-free arm, killed-cell, cell-free-metabolite
    or mutant comparison is reported for this retained experiment. The record limits
    microbial-increment and molecular-causality claims accordingly.
  snapshot_sha256: 9da3ec0eebfa8b05a9aec4398fa45a80748c9f212b153f6010a695a2d6cdb062
- evidence_id: contradictions
  kind: primary_source
  reference: https://doi.org/10.3390/min11020149
  locator: Section 3.7; Figure 23 labels/caption; Tables 4–5; Section 4.2
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: partial
  summary: The plotted XRD labels give 78 or 156 days while the caption says 46 days.
    The phrase essentially complete bioreduction refers to a plateau, not reduction
    of all supplied Fe(III), as the measured phosphate-free fraction is about 30%.
    Table 4 marks the high-phosphate SEM green-rust assignment GR? and supplies no
    Mossbauer result for that arm. Table 5 relative spectral areas are not recovered
    mass fractions. These conflicts and limits are accurately preserved.
  snapshot_sha256: 9da3ec0eebfa8b05a9aec4398fa45a80748c9f212b153f6010a695a2d6cdb062
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=319224
  locator: Same-round NCBI XML plus fresh independent browser access
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: The authority label is Shewanella putrefaciens CN-32, with equivalent strain
    names. Retained XML rank is strain; browser rendering uses no rank. Neither authenticates
    the actual experimental stock. The record relies on the named-strain label and
    explicitly preserves the collection-number conflict.
  snapshot_sha256: 8de6ac66eb65af66efa3115fce5deaf9132ff4ad27428e909ea9cd13a626707d
- evidence_id: atcc_cn32
  kind: authority
  reference: https://www.atcc.org/products/baa-453
  locator: Retained original authority HTML title and strain designation
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: BAA-453 is Shewanella putrefaciens, strain CN-32 [OCM 576, SMCC 576W].
    Independently read the same-round downloaded authority content; fresh web-tool
    access returned an internal error, not contradictory authority data.
  snapshot_sha256: 77741f65aa58d00f6406d9033f7f42d90e3211a4d0f4ca3969d9a0fd6c7ef5fe
- evidence_id: atcc_other
  kind: authority
  reference: https://www.atcc.org/products/baa-543
  locator: Retained original authority HTML title and strain designation
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: BAA-543 is Cellulomonas sp., strain ES5, unlike CN32. The source prints
    BAA-543 beside CN32; preserving this unresolved provenance conflict is correct.
    Independent fresh web-tool access failed, so the retained same-round original
    HTML was used.
  snapshot_sha256: db8046e6456b3fa97383e00498b6a58a7245036b5cb18fe523c54575611a51bd
- evidence_id: metadata
  kind: database
  reference: https://api.crossref.org/works/10.3390/min11020149
  locator: Same-round Crossref response, title/DOI/date/relation/update-to/license
    fields versus original page 1
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Title, DOI and 31 January 2021 publication agree. Retained response has
    empty relation and no update-to field, with CC BY 4.0 license. The actual retained
    PDF has 43 pages; a current publisher search representation says 44 pages, so
    this review identifies the exact original PDF rather than inferring a substantive
    update from page-count metadata.
  snapshot_sha256: dfe7bb0cd975fd2eff7e9326a1cf7c1a66d5c143e06edcea027b5e75b9667430
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round64-feroxyhyte-independent/web-search.json
  locator: Initial independent live queries and authority opens, followed by web-search-followup.json
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: context_only
  summary: Returned exact DOI/title correction searches did not identify a correction
    or retraction. Primary-source leads include Cutting 2009 (10.1016/j.gca.2009.04.009)
    and a later Sb-bearing ferrihydrite study; these were screened at abstract level
    only, not accepted as new mechanisms or full replication evidence.
  snapshot_sha256: ac4172d7c1b3d276b2e6c345167bd19cfe0a36618f3e8c6d0c572c4ff4816e88
  search_scope: 'Five total queries retained across two JSON files: DOI correction/erratum/retraction;
    feroxyhyte bioreduction Geobacter Cutting 2009; feroxyhyte Shewanella phosphate
    sterile; exact Cutting title on the University of Manchester site; exact 2021
    title correction/erratum. First returned sets only, no date filters or pagination.
    Negative result is bounded and does not certify notice absence.'
- evidence_id: counterevidence
  kind: primary_source
  reference: https://research.manchester.ac.uk/en/publications/mineralogical-and-morphological-constraints-on-the-reduction-of-f/
  locator: Author-institution record and abstract for Cutting et al. 2009; retained
    in web-search-followup.json
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: context_only
  summary: The original-study abstract reports substantially different initial reduction
    rates for two synthetic feroxyhytes with similar surface areas but different crystallinities,
    and warns about aggregation/spectrophotometric normalization. This supports the
    curated condition-specific scope. Its reported AQDS effect in Geobacter is not
    a contradiction of the narrowly stated CN32 result; no rates or additional organism
    mechanism were imported without the full original.
  snapshot_sha256: 9d8512b7c35f94c09eeaa77c197a320b4b6a2bec93a82876dadf70677eda771a
- evidence_id: history
  kind: record_content
  reference: history/records/feroxyhyte/2026-10-14T062756Z-codex-bd8d5e.yaml
  locator: Entire canonical CREATE session and inline created event
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Canonical CREATE records codex/GPT-6/codex at 06:27:56Z with the correct
    target and bounded scientific changes. Inline creation at 06:28:06Z is a distinct
    actual event. No historical authorship or reviewer authorship was invented.
  snapshot_sha256: b762f1dac09b715e8c8c31f8d717011af630da47dc076353bc50809e6f974908
- evidence_id: local_search
  kind: search
  reference: /private/tmp/cmm-round64-feroxyhyte-independent/local-search.txt
  locator: Exact mineral name, IMA number and DOI search in maintained records, structured
    reviews and history
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: context_only
  summary: Only the new feroxyhyte record/history matched these terms within the independently
    searched roots at review time. Broader discovery dossier dedup is separate. Hidden
    and ignored files and symlinks were included; no machinewide or unsearched-root
    absence is claimed.
  snapshot_sha256: dbfd0cfe0068cadd9e2ce9f9b5b32a3455ca5e73597a35d480db7476ca47c27d
  search_scope: rg --no-ignore --hidden --follow -n -i 'feroxyhyte|1975-032|min11020149'
    data/records reviews/structured history/records
- evidence_id: named_validation
  kind: validation
  reference: /private/tmp/cmm-round64-feroxyhyte-independent/named.log
  locator: Entire actual output and checks.json command timestamps
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: 'Executed by this reviewer: Checked 1 record(s); 0 failed; exit 0.'
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: history_validation
  kind: validation
  reference: /private/tmp/cmm-round64-feroxyhyte-independent/history.log
  locator: Entire actual output and checks.json command timestamps
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: 'Executed by this reviewer against base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb:
    Checked 342 history record(s); 0 error(s); exit 0.'
  snapshot_sha256: c848103fbbc2eba28d3ebd20cfb8ed459ca3780c20c22e2634514ae5c10bae12
- evidence_id: batch_validation
  kind: validation
  reference: /private/tmp/cmm-round64-final-gates.json
  locator: Coordinator round64 command receipt and entire final-gates.log
  accessed_at: '2026-10-14T06:42:48.068190Z'
  support: supports
  summary: Coordinator just check and explicit --require-records passed against this
    unchanged feroxyhyte record. Actual command receipts and complete log were inspected.
    Log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99. An
    unrelated lepidocrocite correction landed during the batch run, so the coordinator
    will rerun whole-batch gates after that correction. This review does not attest
    that correction or the later saved review bundle.
  snapshot_sha256: f2af92147f4a25ed646c60e50766925356e9f605d68c9526b0ee195301b4ee5f
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species and material boundary
  outcome: supported
  summary: IMA approval and formula are correct. The laboratory synthetic mineral
    is not a natural ore, elemental iron or a mixed secondary product. No criticality
    is inherited from iron.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - ima
  - primary
  dimensions:
  - name: material_form
    value: Feroxyhyte Fe3+O(OH), synthetic delta-prime FeOOH in the experiment
    definition: Species identity and experimental material form are separate from
      secondary mixtures
    evidence_ids:
    - ima
    - primary
  - name: criticality
    value: No jurisdiction/list/edition claim
    definition: Omission does not assert the mineral is noncritical in every jurisdiction
    evidence_ids:
    - record
- assessment_id: system
  area: evidence
  topic: Organism, biomass, substrate and conditions
  outcome: supported
  summary: The record preserves the named CN32 culture, synthetic substrate and explicit
    2021 treatment conditions without reconstructing absent inherited recipes or authenticating
    the stock.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - primary
  - taxon
  - atcc_cn32
  - atcc_other
  dimensions:
  - name: organism_resolution
    value: Named Shewanella putrefaciens CN32; NCBITaxon:319224
    definition: ATCC printed BAA-543 conflicts with authority BAA-453; exact stock
      remains unresolved
    evidence_ids:
    - taxon
    - atcc_cn32
    - atcc_other
    - primary
  - name: biomass_state
    value: Late-log live culture, approximately 5 x 10^9 cells/mL as printed
    definition: Not dead biomass, purified reductase or authenticated genome of the
      experimental stock
    evidence_ids:
    - primary
  - name: substrate
    value: 80 mM Fe(III) as chemically synthesized feroxyhyte
    definition: pXRD-checked mineral, not a natural mixed ore
    evidence_ids:
    - primary
  - name: pretreatment
    value: Peroxide oxidation of Fe(OH)2, repeated washing, 60 C drying and 200-mesh
      sieving
    definition: Experimental synthetic mineral preparation
    evidence_ids:
    - primary
  - name: conditions
    value: Duplicate 100 mL cultures in 160 mL bottles; 75 mM formate; argon; roller
      drum; 30 C darkness; medium set to pH 7.5 before sterilization
    definition: Not a constant-pH trajectory; phosphate arms all also have 100 micromolar
      AQDS
    evidence_ids:
    - primary
    - controls
- assessment_id: controls
  area: evidence
  topic: Causal scope and experimental controls
  outcome: supported
  summary: Actual sterile-control diffraction is recognized, while unreported matched
    sterile kinetics and amendment metadata limit microbial-increment quantification.
    Molecular and biological-necessity claims are not overextended.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - primary
  - controls
  dimensions:
  - name: controls
    value: Sterile-control XRD trace; AQDS-free/no-phosphate versus AQDS treatments;
      two phosphate loads with AQDS
    definition: No matched sterile Fe(II) trajectories, complete control metadata
      or phosphate-amended AQDS-free arm
    evidence_ids:
    - controls
  - name: causal_scope
    value: Culture-associated reductive transformation; morphology-based dissolution-reprecipitation
      inference
    definition: No mutant, killed-cell, purified-enzyme or tracer demonstration of
      a unique pathway
    evidence_ids:
    - primary
    - controls
- assessment_id: outcome
  area: quantity
  topic: Measurements, phase assignment and deployment
  outcome: supported
  summary: The retained outcome is acid-extractable Fe(II) plus condition-dependent
    mixed secondary solids. The record correctly avoids complete reduction, dissolved-only
    Fe(II), recovered mass fractions and industrial deployment.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - primary
  - measurement
  - contradictions
  dimensions:
  - name: measurement_basis
    value: One-week acid-extractable total suspension Fe(II) measured by ferrozine
    definition: Initial denominator 80 mM Fe(III); phosphate-free day-78 endpoints
      are about 30%, with longer day-156 phosphate endpoints
    evidence_ids:
    - measurement
  - name: outcome
    value: Source-assigned magnetite/chukanovite at low/no phosphate and carbonate
      green rust/vivianite at 5 mM phosphate
    definition: pXRD plus microscopy and selected spectral fits; high-P SEM green
      rust tentative and no high-P Mossbauer result
    evidence_ids:
    - primary
    - contradictions
  - name: deployment
    value: Laboratory serum-bottle transformation
    definition: No isolated iron product, ore recovery, pilot process or industrial
      deployment demonstrated
    evidence_ids:
    - record
    - primary
- assessment_id: limits
  area: evidence
  topic: Internal contradictions and transfer limits
  outcome: supported
  summary: The record preserves the Figure 23 timing conflict, unlike endpoint durations
    and plateau versus total-reduction distinction. Independent abstract-level comparison
    supports keeping mineral morphology and organism context explicit.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - measurement
  - contradictions
  - counterevidence
  - notices
- assessment_id: provenance
  area: provenance
  topic: Source, history and actual validation
  outcome: supported
  summary: DOI, IMA approval, taxon mapping and claim locators are supported; the
    collection-number conflict is explicit. Named and trusted-base history validation
    passed. All 37 raw artifacts in the frozen dossier were rehashed with zero mismatches.
  target_ids:
  - cmmmech:feroxyhyte
  evidence_ids:
  - record
  - ima
  - metadata
  - history
  - named_validation
  - history_validation
  - batch_validation
findings: []
actions: []
limitations:
- Experimental stock authentication is unresolved because the paper prints ATCC BAA-543
  beside CN32, while collection authority assigns CN32 to BAA-453.
- Sterile-control diffraction exists, but matched sterile Fe(II) kinetics and complete
  control amendment/time metadata are not supplied. Unique biological necessity and
  electron-transfer pathways remain unresolved.
- All phosphate-amended cultures also contain AQDS; conclusions cannot be generalized
  to shuttle-free phosphate treatments.
- Figure 23 caption says 46 days while traces say 78/156 days. The record preserves
  this and does not invent a common harvest time.
- Acid-extractable Fe(II), nondetection of starting mineral and selected Mossbauer
  spectral areas do not establish complete iron reduction, pure-phase yield or isolated
  product recovery.
- The high-phosphate SEM green-rust assignment is tentative and lacks a Mossbauer
  result for that arm. pXRD-based mixed-phase assignments remain the source-supported
  scope.
- Earlier complete medium/inoculum recipes were not reconstructed. Other studies were
  screened only at primary abstract level; no literature-wide completeness or full
  replication check is claimed.
- Fresh ATCC web-tool opens failed. Same-round original authority HTML was independently
  read and checksum-verified; the exact access limitation is retained.
notes:
- 'Corrections made by this reviewer: none. All four inspected record/history/dossier
  inputs remain byte-identical. No external issue or comment was posted by this reviewer.'
- The actual review start is anchored to inspect.json mtime 2026-10-14T06:34:25.996316Z.
  Evidence-access timestamps here denote completion of this review pass, not fresh
  acquisition of every reused source.
- Empty findings is scoped to the accepted record claims; it does not remove the reported
  source limitations or endorse unrelated experiments.
- The coordinator reported an unrelated lepidocrocite correction during the recorded
  batch gate. All four feroxyhyte inputs remained frozen and were rehashed before
  save. A later whole-batch rerun is a coordinator publication gate, not an unexecuted
  check claimed by this review.
tags:
- round64
- independent
- feroxyhyte
- primary-figures
```
