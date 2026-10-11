# Independent pyrite successor: original workbook discrepancy retained

- Review: 20261011T204047Z-pyrite-round33-resolution
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T20:38:19Z
- Finished UTC: 2026-10-11T20:40:47.267719Z
- Reviewer: Codex /root/round27_eaf_slag (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The corrected record accurately retains the original workbook versus Figure 1c unamended-methane conflict. Exact F1 is resolved locally without repairing source values or altering separately supported specimen and dialysis observations. Named validation, corrected full suite and separate cohort checks passed; all accepted scientific scope remains qualified.

## Scope And Provenance

All corrected pyrite fields, both canonical histories and exact predecessor F1; retained independent full primary/figures/SI/workbook/authority assessment plus rechecked correction.

Selection: Parent-assigned independently authored round33 record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bee4f42bb622ae0a0999f8f3e3dac31f14282278.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pyrite | data/records/pyrite.yaml | maintained | Pyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent corrected named validation | passed | True | cmmmech:pyrite | Reviewer executed: 1 checked, 0 failed. Log /private/tmp/cmm-round33-pyrite-independent-review/corrected-named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Corrected state batch gate | passed | True | cmmmech:pyrite | Parent executed, independently read terminal receipt and verified log SHA256. Corrected state. Final log: ....................................................sss................. [ 92%] / .......................                                                  [100%] / 308 passed, 3 skipped in 116.48s (0:01:56) / Checked 190 record(s); 0 failed. / Checked 220 history record(s); 0 error(s). Log /private/tmp/cmm-round33-corrected-batch.log SHA256 d116c3fbe06436f79c375b8941e05c0f551569d7576dd93a0f2521139237f9b0 |
| Corrected state nonempty gate | passed | True | cmmmech:pyrite | Parent executed, independently read terminal receipt and verified log SHA256. Corrected state. Final log: Checked 190 record(s); 0 failed. Log /private/tmp/cmm-round33-corrected-nonempty.log SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299 |
| Corrected state history gate | passed | True | cmmmech:pyrite | Parent executed, independently read terminal receipt and verified log SHA256. Corrected state. Final log: Checked 220 history record(s); 0 error(s). Log /private/tmp/cmm-round33-corrected-history.log SHA256 62b341a0909b6a1a766ed08cd09fdc07d06ecf3cfd384f47da4f5717c886613a |

## Scientific And Domain Assessments

### Mineral and strain scope

identity: supported. Targets: cmmmech:pyrite.

Mineral identity and A3 strain mapping are sound. Natural specimen, synthesized FeS2, companion culture and proposed secondary products remain separate.

### Conditions, control boundaries and microscopy

evidence: supported. Targets: cmmmech:pyrite.

The record preserves natural day-5 growth separately from synthetic seven-day and day-5 dialysis assays. Surface-area equivalence is estimated geometry. Specimen association images are not a mineral-specific dissolution balance.

### Censored values and inferential quantities

quantity: supported. Targets: cmmmech:pyrite.

Table S3 sulfide amount/SD and n=3 are exact; B.D. is not zero and acid-labile FeII is below about 11 micromolar. Cell reduction estimates and secondary phases remain inferred.

### Original workbook versus methane control figure

evidence: supported. Targets: cmmmech:pyrite.

The current context-only explanation accurately retains original H26:H32 formulas, pyrite SD references and H29=225.334939 mmol versus near-zero Figure1c. It explicitly rejects use as control measurements and keeps S3/Table S3 separate. No invented repair.

### Exact working state and history

provenance: supported. Targets: cmmmech:pyrite.

Exact corrected record, original CREATE, new EDIT and schema hashes are pinned at the durable base. Required named/pre-correction full/corrected affected checks pass; original assessment remains valid for byte-identical remaining scientific content.

## Findings

### F1: Retain the original A3 workbook versus control-figure discrepancy

minor / resolved / confirmed; issue key: CMMMech.pyrite.workbook-unamended-methane-conflict.

First-sheet H26:H32 are labelled unamended total methane but formulas reference G26:G32 pyrite SD values multiplied by 1000. These cached values contradict the near-zero Figure 1c control. The record cites Data Set 1 and Figure 1 without retaining this specific uncertainty. Add a bounded limitation; no source values should be repaired, and Table S3/natural S3 remain independent observations.

Disposition: Independently verified added context-only evidence against original first-sheet headers, cached values and shared formulas; exact initial scientific bytes reconstructed after removal of only correction/provenance additions. Corrected named and affected cohort gates pass. No data repair or unchanged-observation overclaim.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/pyrite.yaml; Every field, one mechanism and inline CREATE | supports | All corrected fields assessed. Exact workbook/control-figure discrepancy is now explicit; no synthetic numeric result is transferred to natural specimen. Original remaining scientific bytes reconstruct the initial hash after removing only the correction and appended provenance. |
| main | https://doi.org/10.1038/s41396-021-01028-3; Complete original JATS main text; Materials and methods, Results and discussion, all four original main figures independently visually inspected | supports | A3 specimen growth and synthetic FeS2 sulfide production are separate experiments. Methods support washing, natural 63–125 micrometre fraction and 1.5 g/75 mL, synthetic 2 mM Fe, washed 10% inoculum, pH 7, 38 C static incubation, 80:20 N2/CO2 at 3.14 atm. Mean/SD biological triplicates versus single abiotic reactors are explicit. Dialysis does not isolate electron transfer from access to products or extracellular assemblies; secondary phases and cell-based reduction quantities are inferred. Main-source year, DOI and authors verified against publisher and retained metadata. |
| si | https://doi.org/10.1038/s41396-021-01028-3; Original 12-page supplement, all pages visually inspected: Figures S1–S8, Tables S1–S3 and references | supports | S3a shows specimen-associated day-5 growth and methane relative to no-added-Fe/S controls. S1 explicitly characterizes synthesized phases, not a separate natural-specimen XRD. Table S3 gives accessible synthetic-phase 10.55 +/- 0.13 micromol total sulfide (mean +/- SD, n=3) at day 5, other sulfide arms B.D.; this is not a mineral recovery denominator. S6 shows growth with sulfide alone. Table S2 conflicts with main M. barkeri medium. S7–S8 support cell association, not directly quantified mineral dissolution. |
| workbook | https://doi.org/10.1038/s41396-021-01028-3; Data Set 1 original XLSX, both worksheets decoded independently; sheet Figure 1 CH4 and Sulfide Values cells E23,H24,H26:H32,G26:G32 and raw OOXML formulas | supports | The first sheet labels H24 as Unamended within the CH4(total mmol) block. H26 has formula G26*1000 and H27:H32 share G27*1000, referencing neighboring pyrite SD values. Cached H29=225.33493937882702 contrasts with near-zero unamended Figure 1c. Source workbook therefore cannot independently validate that methane control. Companion M. barkeri cells also include DIV/0 errors; concentration/total blocks and blank values are not interchangeable. Both sheets were decoded; no experimental reanalysis or source-data repair is claimed. The successor record now explicitly retains this discrepancy; original workbook rechecked, not corrected. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original pages 1,2 and179, visually inspected | supports | Pyrite row is FeS2, G, year ?, with no approval number. The record does not inherit elemental criticality or equate natural material to synthetic phases, marcasite, pyrrhotite or a nickel-substituted product. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=456320; Official current taxonomy and independently opened issuing ATCC BAA-1334/BAA-2329 pages; retained API/browser bytes | supports | 456320 is Methanococcus voltae A3, a no-rank strain node; ATCC BAA-1334 identifies A3. BAA-2329 is Fusaro, contradicting the companion MS label. The record correctly refrains from resolving actual culture identity by guessing. |
| history | history/records/pyrite/2026-10-11T202913Z-codex-7036c0.yaml; Complete canonical CREATE and distinct inline event | supports | Actual Codex/GPT-6/codex actor, target and current creation event are consistent. It does not invent independent review or previous authorship. |
| notices | /private/tmp/cmm-round33-pyrite-independent-review/search-receipt.json; Independent bounded notice, identifier and counterevidence searches | supports | No specific correction/retraction surfaced in returned results. Jorgensen correspondence DOI 10.1038/s41396-021-01055-0 was identified; full access failed, so its search excerpt is not adopted as experimental refutation. Spietz2022 text and abiotic2024 abstract provide follow-up routing, not fully assessed mechanism additions. |
| overlap | /private/tmp/cmm-round33-pyrite-independent-review/local-overlap.txt; Current data/records, research, reviews and history text search | supports | Current pyrite identity is distinct from contextual pyrite in other records. Curator broader original/raw dedup is routing rather than reviewer-executed. No machine-wide novelty claim. |
| edit | history/records/pyrite/2026-10-11T203753Z-codex-171a3f.yaml; Complete EDIT and separate inline event; correction dossier and reverse-byte proof | supports | Actual actor/session, exact correction and issue115 are consistent. Removing only workbook context paragraph plus appended inline EDIT/history reference reconstructs initial SHA24a514260f2361439ec3e9c75e0bedf01866fad6beb65fa8e147f519e1fa1849. Initial review/dossier remain untouched. |

## Limits And Additional Notes

- Natural specimen purity and dissolution balance remain unquantified; source XRD displays synthesized phases only.
- Culture-associated transformation does not establish a unique electron-transfer or uptake pathway, secondary mineral products or field-scale flux.
- Companion strain and medium conflicts are preserved; no companion strain CURIE is assigned.
- Supplementary videos were not inspected. Full original follow-up methods and inaccessible correspondence were not adopted as evidence of a new mechanism or refutation.
- Search coverage is bounded and hidden/ignored local text included.
- Original workbook methane-control inconsistency remains unresolved in the primary data; local curation resolves its omission by preserving it explicitly. GitHub issue closure is a later publication operation, not claimed here.
- The original review remains immutable; F1 resolution is this new observation. Reviewer did not edit any maintained pyrite record or history.
- Native initial inspect had metadata-only target repository normalization with identical scientific input hashes.
- Full just check and separate nonempty/history checks were rerun on the corrected state by the parent; reviewer verified completed receipts and hashes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T204047Z-pyrite-round33-resolution
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent pyrite successor: original workbook discrepancy retained'
started_at: '2026-10-11T20:38:19Z'
finished_at: '2026-10-11T20:40:47.267719Z'
reviewer:
  identity: Codex /root/round27_eaf_slag
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored pyrite; reviewer authored separate chalcocite,
    excluded from this review. Shared worktree and curator-acquired originals disclosed.
    Canonical inspect preceded assessment; reviewer independently read full main text,
    all original main figures and supplement pages, decoded original workbook and
    checked authorities. No maintained target edits. The same independent reviewer
    re-inspected corrected bytes and new history; prior full-primary assessment is
    retained with an exact reverse-byte proof of unchanged remaining content.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The corrected record accurately retains the original workbook versus Figure
  1c unamended-methane conflict. Exact F1 is resolved locally without repairing source
  values or altering separately supported specimen and dialysis observations. Named
  validation, corrected full suite and separate cohort checks passed; all accepted
  scientific scope remains qualified.
source:
  git_revision: bee4f42bb622ae0a0999f8f3e3dac31f14282278
  state: working_tree
  inputs:
  - path: data/records/pyrite.yaml
    sha256: 44ae5da852faad88e3056fb6e00a8e4be0d43c241a58e31c3661cd4bee812f9b
    role: target
  - path: history/records/pyrite/2026-10-11T202913Z-codex-7036c0.yaml
    sha256: d75b0177a63d378da627027f1a6208ad23bdf22fea3a91c1f584d1439b392a25
    role: context
  - path: history/records/pyrite/2026-10-11T203753Z-codex-171a3f.yaml
    sha256: af1cef6fed8bdb1b428e33c0008cca878aa6d5a796a43841c240fd7827918a67
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All corrected pyrite fields, both canonical histories and exact predecessor
    F1; retained independent full primary/figures/SI/workbook/authority assessment
    plus rechecked correction.
  selection: Parent-assigned independently authored round33 record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pyrite
  exclusions:
  - target: Other cohort records, source videos and raw instrumental reconstruction
    reason: No claim rests on uninspected videos; follow-up studies are screened as
      leads rather than fully curated mechanisms.
targets:
- target_id: cmmmech:pyrite
  path: data/records/pyrite.yaml
  label: Pyrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrite.yaml
    role: maintained record
checks:
- check_id: named
  name: Independent corrected named validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked
    cmmmech validate data/records/pyrite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer executed: 1 checked, 0 failed. Log /private/tmp/cmm-round33-pyrite-independent-review/corrected-named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e'
  target_ids:
  - cmmmech:pyrite
- check_id: batch
  name: Corrected state batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed, independently read terminal receipt and verified log
    SHA256. Corrected state. Final log: ....................................................sss.................
    [ 92%] / .......................                                                  [100%]
    / 308 passed, 3 skipped in 116.48s (0:01:56) / Checked 190 record(s); 0 failed.
    / Checked 220 history record(s); 0 error(s). Log /private/tmp/cmm-round33-corrected-batch.log
    SHA256 d116c3fbe06436f79c375b8941e05c0f551569d7576dd93a0f2521139237f9b0'
  target_ids:
  - cmmmech:pyrite
- check_id: nonempty
  name: Corrected state nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed, independently read terminal receipt and verified log
    SHA256. Corrected state. Final log: Checked 190 record(s); 0 failed. Log /private/tmp/cmm-round33-corrected-nonempty.log
    SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299'
  target_ids:
  - cmmmech:pyrite
- check_id: history
  name: Corrected state history gate
  command: uv run --locked cmmmech validate-history --base bee4f42bb622ae0a0999f8f3e3dac31f14282278
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed, independently read terminal receipt and verified log
    SHA256. Corrected state. Final log: Checked 220 history record(s); 0 error(s).
    Log /private/tmp/cmm-round33-corrected-history.log SHA256 62b341a0909b6a1a766ed08cd09fdc07d06ecf3cfd384f47da4f5717c886613a'
  target_ids:
  - cmmmech:pyrite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/pyrite.yaml
  locator: Every field, one mechanism and inline CREATE
  accessed_at: '2026-10-11T20:40:47.267719Z'
  support: supports
  summary: All corrected fields assessed. Exact workbook/control-figure discrepancy
    is now explicit; no synthetic numeric result is transferred to natural specimen.
    Original remaining scientific bytes reconstruct the initial hash after removing
    only the correction and appended provenance.
  snapshot_sha256: 44ae5da852faad88e3056fb6e00a8e4be0d43c241a58e31c3661cd4bee812f9b
- evidence_id: main
  kind: primary_source
  reference: https://doi.org/10.1038/s41396-021-01028-3
  locator: Complete original JATS main text; Materials and methods, Results and discussion,
    all four original main figures independently visually inspected
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: A3 specimen growth and synthetic FeS2 sulfide production are separate experiments.
    Methods support washing, natural 63–125 micrometre fraction and 1.5 g/75 mL, synthetic
    2 mM Fe, washed 10% inoculum, pH 7, 38 C static incubation, 80:20 N2/CO2 at 3.14
    atm. Mean/SD biological triplicates versus single abiotic reactors are explicit.
    Dialysis does not isolate electron transfer from access to products or extracellular
    assemblies; secondary phases and cell-based reduction quantities are inferred.
    Main-source year, DOI and authors verified against publisher and retained metadata.
  snapshot_sha256: ff3c0e23006152134855c929e075f792cffc20024444e468f2414b8877bf181f
- evidence_id: si
  kind: primary_source
  reference: https://doi.org/10.1038/s41396-021-01028-3
  locator: 'Original 12-page supplement, all pages visually inspected: Figures S1–S8,
    Tables S1–S3 and references'
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: S3a shows specimen-associated day-5 growth and methane relative to no-added-Fe/S
    controls. S1 explicitly characterizes synthesized phases, not a separate natural-specimen
    XRD. Table S3 gives accessible synthetic-phase 10.55 +/- 0.13 micromol total sulfide
    (mean +/- SD, n=3) at day 5, other sulfide arms B.D.; this is not a mineral recovery
    denominator. S6 shows growth with sulfide alone. Table S2 conflicts with main
    M. barkeri medium. S7–S8 support cell association, not directly quantified mineral
    dissolution.
  snapshot_sha256: ddae8a4706037d8392b2c16855375d1537a553f15323f677ce0a571386a6da3f
- evidence_id: workbook
  kind: primary_source
  reference: https://doi.org/10.1038/s41396-021-01028-3
  locator: Data Set 1 original XLSX, both worksheets decoded independently; sheet
    Figure 1 CH4 and Sulfide Values cells E23,H24,H26:H32,G26:G32 and raw OOXML formulas
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: The first sheet labels H24 as Unamended within the CH4(total mmol) block.
    H26 has formula G26*1000 and H27:H32 share G27*1000, referencing neighboring pyrite
    SD values. Cached H29=225.33493937882702 contrasts with near-zero unamended Figure
    1c. Source workbook therefore cannot independently validate that methane control.
    Companion M. barkeri cells also include DIV/0 errors; concentration/total blocks
    and blank values are not interchangeable. Both sheets were decoded; no experimental
    reanalysis or source-data repair is claimed. The successor record now explicitly
    retains this discrepancy; original workbook rechecked, not corrected.
  snapshot_sha256: 13fffe1fbd15c28d57e911377df4117acd60c5df20fc31d9411e40a3f73ab3e0
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original pages 1,2 and179, visually inspected
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: Pyrite row is FeS2, G, year ?, with no approval number. The record does
    not inherit elemental criticality or equate natural material to synthetic phases,
    marcasite, pyrrhotite or a nickel-substituted product.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=456320
  locator: Official current taxonomy and independently opened issuing ATCC BAA-1334/BAA-2329
    pages; retained API/browser bytes
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: 456320 is Methanococcus voltae A3, a no-rank strain node; ATCC BAA-1334
    identifies A3. BAA-2329 is Fusaro, contradicting the companion MS label. The record
    correctly refrains from resolving actual culture identity by guessing.
  snapshot_sha256: a7fa82ccf69d5967861484cf731075e4e889d2a7fce415f1196ac709f569aeb2
- evidence_id: history
  kind: record_content
  reference: history/records/pyrite/2026-10-11T202913Z-codex-7036c0.yaml
  locator: Complete canonical CREATE and distinct inline event
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: Actual Codex/GPT-6/codex actor, target and current creation event are consistent.
    It does not invent independent review or previous authorship.
  snapshot_sha256: d75b0177a63d378da627027f1a6208ad23bdf22fea3a91c1f584d1439b392a25
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round33-pyrite-independent-review/search-receipt.json
  locator: Independent bounded notice, identifier and counterevidence searches
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: No specific correction/retraction surfaced in returned results. Jorgensen
    correspondence DOI 10.1038/s41396-021-01055-0 was identified; full access failed,
    so its search excerpt is not adopted as experimental refutation. Spietz2022 text
    and abiotic2024 abstract provide follow-up routing, not fully assessed mechanism
    additions.
  snapshot_sha256: c98b3a620da95b76d5192c37a749593347777c9baf310528cf2d6f5c202c9ee6
  search_scope: Exact queries retained; first result sets on 11 October 2026, no pagination.
    Original publisher main and issuing taxon/collection pages inspected. No universal
    absence claim.
- evidence_id: overlap
  kind: search
  reference: /private/tmp/cmm-round33-pyrite-independent-review/local-overlap.txt
  locator: Current data/records, research, reviews and history text search
  accessed_at: '2026-10-11T20:37:00.653378Z'
  support: supports
  summary: Current pyrite identity is distinct from contextual pyrite in other records.
    Curator broader original/raw dedup is routing rather than reviewer-executed. No
    machine-wide novelty claim.
  snapshot_sha256: e3d0d0290913dfbcad1ca86034b2593292e7da6ba514e20b20d57b21c6a4043d
  search_scope: rg --no-ignore --hidden --follow -n cmmmech:pyrite|s41396-021-01028-3|8630215|456320;
    includes hidden and ignored text and relevant symlinks.
- evidence_id: edit
  kind: record_content
  reference: history/records/pyrite/2026-10-11T203753Z-codex-171a3f.yaml
  locator: Complete EDIT and separate inline event; correction dossier and reverse-byte
    proof
  accessed_at: '2026-10-11T20:40:47.267719Z'
  support: supports
  summary: Actual actor/session, exact correction and issue115 are consistent. Removing
    only workbook context paragraph plus appended inline EDIT/history reference reconstructs
    initial SHA24a514260f2361439ec3e9c75e0bedf01866fad6beb65fa8e147f519e1fa1849. Initial
    review/dossier remain untouched.
  snapshot_sha256: af1cef6fed8bdb1b428e33c0008cca878aa6d5a796a43841c240fd7827918a67
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral and strain scope
  summary: Mineral identity and A3 strain mapping are sound. Natural specimen, synthesized
    FeS2, companion culture and proposed secondary products remain separate.
  evidence_ids:
  - record
  - ima
  - taxon
  - main
  target_ids:
  - cmmmech:pyrite
  outcome: supported
  dimensions:
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim is inherited; not a claim of absence
      from all lists.
    evidence_ids:
    - record
  - name: biomass
    value: Living washed Methanococcus voltae A3
    definition: 10% inoculum; authenticated strain identifier does not establish a
      molecular pathway.
    evidence_ids:
    - main
    - taxon
- assessment_id: methods
  area: evidence
  topic: Conditions, control boundaries and microscopy
  summary: The record preserves natural day-5 growth separately from synthetic seven-day
    and day-5 dialysis assays. Surface-area equivalence is estimated geometry. Specimen
    association images are not a mineral-specific dissolution balance.
  evidence_ids:
  - record
  - main
  - si
  target_ids:
  - cmmmech:pyrite
  outcome: supported
  dimensions:
  - name: deployment
    value: Laboratory culture assays
    definition: No isolated metal recovery, industrial deployment or environmental
      flux is asserted.
    evidence_ids:
    - record
    - main
- assessment_id: accounting
  area: quantity
  topic: Censored values and inferential quantities
  summary: Table S3 sulfide amount/SD and n=3 are exact; B.D. is not zero and acid-labile
    FeII is below about 11 micromolar. Cell reduction estimates and secondary phases
    remain inferred.
  evidence_ids:
  - record
  - main
  - si
  target_ids:
  - cmmmech:pyrite
  outcome: supported
- assessment_id: workbook_conflict
  area: evidence
  topic: Original workbook versus methane control figure
  summary: The current context-only explanation accurately retains original H26:H32
    formulas, pyrite SD references and H29=225.334939 mmol versus near-zero Figure1c.
    It explicitly rejects use as control measurements and keeps S3/Table S3 separate.
    No invented repair.
  evidence_ids:
  - record
  - main
  - workbook
  - edit
  target_ids:
  - cmmmech:pyrite
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Exact working state and history
  summary: Exact corrected record, original CREATE, new EDIT and schema hashes are
    pinned at the durable base. Required named/pre-correction full/corrected affected
    checks pass; original assessment remains valid for byte-identical remaining scientific
    content.
  evidence_ids:
  - record
  - history
  - overlap
  - notices
  - edit
  target_ids:
  - cmmmech:pyrite
  outcome: supported
findings:
- finding_id: F1
  issue_key: CMMMech.pyrite.workbook-unamended-methane-conflict
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Retain the original A3 workbook versus control-figure discrepancy
  description: First-sheet H26:H32 are labelled unamended total methane but formulas
    reference G26:G32 pyrite SD values multiplied by 1000. These cached values contradict
    the near-zero Figure 1c control. The record cites Data Set 1 and Figure 1 without
    retaining this specific uncertainty. Add a bounded limitation; no source values
    should be repaired, and Table S3/natural S3 remain independent observations.
  target_ids:
  - cmmmech:pyrite
  field_paths:
  - mechanisms[id=voltae-pyrite-associated-growth-and-reduction].evidence
  evidence_ids:
  - record
  - main
  - workbook
  - edit
  rule_id: preserve-contradictory-source-data
  native_severity: minor
  normalization_reason: Limited source-data provenance qualification; mineral identity,
    specimen growth and synthetic Table S3 observation remain supported.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrite.yaml
    role: maintained_record
  disposition_reason: Independently verified added context-only evidence against original
    first-sheet headers, cached values and shared formulas; exact initial scientific
    bytes reconstructed after removal of only correction/provenance additions. Corrected
    named and affected cohort gates pass. No data repair or unchanged-observation
    overclaim.
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261011T203700Z-pyrite-round33-initial
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/115
actions: []
limitations:
- Natural specimen purity and dissolution balance remain unquantified; source XRD
  displays synthesized phases only.
- Culture-associated transformation does not establish a unique electron-transfer
  or uptake pathway, secondary mineral products or field-scale flux.
- Companion strain and medium conflicts are preserved; no companion strain CURIE is
  assigned.
- Supplementary videos were not inspected. Full original follow-up methods and inaccessible
  correspondence were not adopted as evidence of a new mechanism or refutation.
- Search coverage is bounded and hidden/ignored local text included.
- Original workbook methane-control inconsistency remains unresolved in the primary
  data; local curation resolves its omission by preserving it explicitly. GitHub issue
  closure is a later publication operation, not claimed here.
notes:
- The original review remains immutable; F1 resolution is this new observation. Reviewer
  did not edit any maintained pyrite record or history.
- Native initial inspect had metadata-only target repository normalization with identical
  scientific input hashes.
- Full just check and separate nonempty/history checks were rerun on the corrected
  state by the parent; reviewer verified completed receipts and hashes.
links:
- research/sources/round33-pyrite/20261011T203016Z-source-investigation.md
- research/sources/round33-pyrite/20261011T203807Z-workbook-correction.md
- reviews/structured/20261011T203700Z-pyrite-round33-initial/review.md
- https://github.com/CultureBotAI/CMMMech/issues/115
tags:
- round33
- pyrite
- independent
- resolution
```
