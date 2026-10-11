# Corrected independent scientific review of Dittmarite

- Review: 20261011T100535Z-dittmarite-round15-successor
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T10:05:04Z
- Finished UTC: 2026-10-11T10:05:35Z
- Reviewer: Codex /root/round15_brine (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Mineral identity and scoped solid-medium fungal transformation remain supported. This successor corrects the predecessor review's material-source lineage context: magnesium reuses Suyamud 2020; the existing struvite record uses separate Kang 2022 evidence. No maintained-record error or edit was involved.

## Scope And Provenance

Reinspection of the same exact new mineral record and CREATE provenance, with focused reassessment of experimental-source lineage against current magnesium and struvite records. The unchanged primary-source assessments from the immediately preceding scientific review are retained with their actual earlier access times.

Selection: Same single mineral target and same target hash as predecessor; related magnesium/struvite files are contextual lineage inputs, not additional scientifically reviewed targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:dittmarite | data/records/dittmarite.yaml | maintained | Dittmarite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named-record validation | passed | True | cmmmech:dittmarite | Reviewer subprocess terminal exit0 at2026-10-11T10:00:41Z;2records0failed. Exact receipt read and retained at /private/tmp/cmm-round15-mineral-review/named-receipt.json. This successor retains that actual completed check; it was not rerun merely for a review-prose correction. Fresh inspection confirms unchanged target/history/schema bytes. |
| Completed root batch check | passed | True | cmmmech:dittmarite | Root terminal gate:308tests passed,3skipped;122records and138histories valid. Reviewer read root gate receipt and actual logs; record hash remained unchanged. This successor retains that actual completed check; it was not rerun merely for a review-prose correction. Fresh inspection confirms unchanged target/history/schema bytes. |
| Nonempty corpus validation | passed | True | cmmmech:dittmarite | Root terminal gate:122records,0failed. Reviewer read root gate receipt and actual logs; record hash remained unchanged. This successor retains that actual completed check; it was not rerun merely for a review-prose correction. Fresh inspection confirms unchanged target/history/schema bytes. |
| Append-only history validation | passed | True | cmmmech:dittmarite | Root terminal gate:138history records,0errors at trusted base. Reviewer read root gate receipt and actual logs; record hash remained unchanged. This successor retains that actual completed check; it was not rerun merely for a review-prose correction. Fresh inspection confirms unchanged target/history/schema bytes. |

## Scientific And Domain Assessments

### Mineral species and hydration-state boundary

identity: supported. Targets: cmmmech:dittmarite.

Dittmarite is an IMA-listed mineral species (magnesium ammonium phosphate monohydrate, (NH4)Mg(PO4)(H2O)), distinct from elemental constituents, struvite and the other magnesium mineral root. Study reuse is explicit and no criticality is inherited.

### Living fungal solid-medium transformation

evidence: supported. Targets: cmmmech:dittmarite.

Synthetic monohydrate identity is established by source methods and Figure5D despite the paper's broad synthetic-struvite wording. Clearing at3days, acidification and7day secondary oxalate formation are correctly distinguished; no dissolution fraction is inferred. Record retains the source's controls, amorphous debris and unmeasured product-yield limitations.

### Exact current bytes and actual CREATE history

provenance: supported. Targets: cmmmech:dittmarite.

Record and sidecar inspected at trusted main base with explicit uncommitted state; actor/model/timestamp and exact record target agree. Independent reviewer did not curate the mineral. Batch and named validation passed.

### Correction of predecessor review experimental-source lineage

provenance: supported. Targets: cmmmech:dittmarite.

The new glushinskite and dittmarite records reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate experiment; it is not part of that Suyamud reuse group. This corrects both erroneous predecessor passages without altering target content or prior review artifacts.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/dittmarite.yaml; Entire maintained YAML plus exact linked CREATE sidecar | supports | Independent reviewer read all maintained fields and actual sidecar. Exact inspected working bytes, actor/model and timestamps match the new creation; history and scientific review remain separate. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA September2026 PDF p.58, mineral row; pp.1-2 column definitions and reuse terms | supports | Independently reread retained official PDF acquired09:55UTC this round, verified SHA, rendered row and definitions. Supports magnesium ammonium phosphate monohydrate, (NH4)Mg(PO4)(H2O); grandfathered original-description year or special-procedure redefinition year is not an invented approval CURIE. No fresh reviewer PDF download claimed. |
| primary | https://doi.org/10.1111/1462-2920.14949; Full published PDF: Experimental procedures (Organisms and media; Struvite preparation; Struvite solubilization; Purification of biogenic crystals), Table2, Figures1,3-5; PDFpp.4,6-7,12 | supports | Independently reread retained complete institutional PDF and verified original acquisition hash. Visually checked Table2/Figure1 and Figures3-5. Methods explicitly identify synthetic feed as dittmarite, living ATCC1015,1%solid-medium arm,25Cdark,7dayphase collection; Figure1C is a3day clearing zone. Figure5A/B matches published glushinskite reference and C/D are feed controls. No liquid-arm yield transferred. |
| limits | https://doi.org/10.1111/1462-2920.14949; Results transformation subsection, Table2; Figure5; Experimental procedures, crystal purification and liquid culture | context_only | Amorphous debris accompanies crystals; selected solids collected with80Cwater and washing. Mineral-free fungal controls and feed diffraction do not isolate oxalate-specific action from acidification in chemistry-matched assays. Liquid105rpm/125rpm discrepancy and equimolar-reagent wording are not imported into the selected solid experiment; no complete conversion, phase fraction or recovered-metal yield asserted. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&amp;mode=Info; Fresh live NCBI browser entry and independently read retained taxonomy XML | supports | NCBITaxon380704 resolves Aspergillus niger ATCC1015. Retained XML explicitly reports rank strain, matching the exact reported experimental strain; does not imply new culture authentication. |
| search | /private/tmp/cmm-round15-mineral-review/search.json; Two exact live searches and ignored/hidden-inclusive local dedup log | context_only | Original bounded correction search remains valid but its original source-lineage summary was erroneous. The new glushinskite and dittmarite records reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate experiment; it is not part of that Suyamud reuse group. New forsterite/talc literature remains a full-methods acquisition lead; no new live literature search is claimed in this correction round. |
| gates | /private/tmp/cmm-round15-gate-receipts.json; Actual root gate receipts and check/require/history logs; independent named receipt | supports | Offline structure, nonempty corpus and append-only provenance gates passed; reviewed current record hashes and inputs remain unchanged. Checks do not independently validate mineralogy. |
| lineage-correction | data/records/magnesium.yaml; data/records/struvite.yaml; Current full source lists, mechanism evidence source_refs and descriptions; predecessor evidence[search].search_scope and limitations | supports | The new glushinskite and dittmarite records reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate experiment; it is not part of that Suyamud reuse group. Independently reread all four record source lists after fresh inspect. Both new mineral records already described the reuse group correctly; the mistake existed only in the predecessor review prose. |
| predecessor | reviews/structured/20261011T100137Z-dittmarite-round15-independent/review.yaml; Complete immutable predecessor YAML and generated Markdown | context_only | Preserved exact predecessor review bytes. No record finding existed (findings=[]), so this successor does not invent a resolved finding or previous_occurrences identity; the correction is review provenance, tracked in issue61. |

## Limits And Additional Notes

- Published XRD phase assignment was checked against the presented comparison but raw diffraction data were not refitted; purity and complete-conversion fraction remain unmeasured.
- The selected solid-medium comparisons lack chemistry-matched abiotic controls that would isolate contributions of acidification, oxalate and living fungal metabolism.
- The new glushinskite and dittmarite records reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate experiment; it is not part of that Suyamud reuse group.
- Bounded literature searches are not exhaustive; the newly identified forsterite/talc study remains a full-methods acquisition lead.
- Correction tracked by https://github.com/CultureBotAI/CMMMech/issues/61. The previous review incorrectly stated that existing magnesium and struvite both reused Suyamud2020. Corrected lineage is explicitly assessed here.
- No maintained record, history sidecar, predecessor YAML or generated Markdown was edited. Findings remain empty because the correction concerns review context, not a newly discovered target defect.
- Primary methods, rendered figures, authority rows and taxonomy were checked during the immediately preceding independent review. This successor rechecks unchanged exact target fields and contextual source lineage; it does not claim a new complete literature acquisition or new experimental validation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T100535Z-dittmarite-round15-successor
kind: record
repository: CultureBotAI/CMMMech
title: Corrected independent scientific review of Dittmarite
started_at: '2026-10-11T10:05:04Z'
finished_at: '2026-10-11T10:05:35Z'
reviewer:
  identity: Codex /root/round15_brine
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate /root/round15_minerals agent authored these mineral
    records and history. Reviewer independently reread primary literature, figure/table
    images and authority rows, resolved taxonomy live and made no mineral-record edits.
    Shared task/worktree does not imply organizational independence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Mineral identity and scoped solid-medium fungal transformation remain supported.
  This successor corrects the predecessor review''s material-source lineage context:
  magnesium reuses Suyamud 2020; the existing struvite record uses separate Kang 2022
  evidence. No maintained-record error or edit was involved.'
source:
  git_revision: a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0
  state: working_tree
  inputs:
  - path: data/records/dittmarite.yaml
    sha256: cdd67254dea22a44812ebfcf71ebb5aef3db97b77e77f2eb29099ddbb8e9a797
    role: target
  - path: data/records/magnesium.yaml
    sha256: 15a759a837c5cf046685087a20bbeec9cca5370037be5304e14267f94bff100c
    role: context
  - path: data/records/struvite.yaml
    sha256: 02d68b2c3524462ac21f614c70ded7263156f713481c732264b9849567f6e945
    role: context
  - path: history/records/dittmarite/2026-10-11T095732Z-codex-93ecbd.yaml
    sha256: 0ed736a0684a72bf3461688ad2ade9f16ba6de77ff1bb2e8db31473e8f66b253
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Reinspection of the same exact new mineral record and CREATE provenance,
    with focused reassessment of experimental-source lineage against current magnesium
    and struvite records. The unchanged primary-source assessments from the immediately
    preceding scientific review are retained with their actual earlier access times.
  selection: Same single mineral target and same target hash as predecessor; related
    magnesium/struvite files are contextual lineage inputs, not additional scientifically
    reviewed targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:dittmarite
  exclusions:
  - target: Liquid-culture assays, other records and raw crystallographic reanalysis
    reason: Liquid assays are intentionally outside curated mechanism; related records
      checked for boundaries only, raw diffraction intensities not acquired or refitted.
targets:
- target_id: cmmmech:dittmarite
  path: data/records/dittmarite.yaml
  label: Dittmarite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/dittmarite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent reviewer named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/glushinskite.yaml data/records/dittmarite.yaml
  status: passed
  required: true
  summary: Reviewer subprocess terminal exit0 at2026-10-11T10:00:41Z;2records0failed.
    Exact receipt read and retained at /private/tmp/cmm-round15-mineral-review/named-receipt.json.
    This successor retains that actual completed check; it was not rerun merely for
    a review-prose correction. Fresh inspection confirms unchanged target/history/schema
    bytes.
  target_ids:
  - cmmmech:dittmarite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed root batch check
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Root terminal gate:308tests passed,3skipped;122records and138histories
    valid. Reviewer read root gate receipt and actual logs; record hash remained unchanged.
    This successor retains that actual completed check; it was not rerun merely for
    a review-prose correction. Fresh inspection confirms unchanged target/history/schema
    bytes.
  target_ids:
  - cmmmech:dittmarite
  exit_code: 0
  expected_exit_code: 0
- check_id: require
  name: Nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Root terminal gate:122records,0failed. Reviewer read root gate receipt
    and actual logs; record hash remained unchanged. This successor retains that actual
    completed check; it was not rerun merely for a review-prose correction. Fresh
    inspection confirms unchanged target/history/schema bytes.
  target_ids:
  - cmmmech:dittmarite
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0
  status: passed
  required: true
  summary: Root terminal gate:138history records,0errors at trusted base. Reviewer
    read root gate receipt and actual logs; record hash remained unchanged. This successor
    retains that actual completed check; it was not rerun merely for a review-prose
    correction. Fresh inspection confirms unchanged target/history/schema bytes.
  target_ids:
  - cmmmech:dittmarite
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/dittmarite.yaml
  locator: Entire maintained YAML plus exact linked CREATE sidecar
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Independent reviewer read all maintained fields and actual sidecar. Exact
    inspected working bytes, actor/model and timestamps match the new creation; history
    and scientific review remain separate.
  snapshot_sha256: cdd67254dea22a44812ebfcf71ebb5aef3db97b77e77f2eb29099ddbb8e9a797
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA September2026 PDF p.58, mineral row; pp.1-2 column definitions and
    reuse terms
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Independently reread retained official PDF acquired09:55UTC this round,
    verified SHA, rendered row and definitions. Supports magnesium ammonium phosphate
    monohydrate, (NH4)Mg(PO4)(H2O); grandfathered original-description year or special-procedure
    redefinition year is not an invented approval CURIE. No fresh reviewer PDF download
    claimed.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1111/1462-2920.14949
  locator: 'Full published PDF: Experimental procedures (Organisms and media; Struvite
    preparation; Struvite solubilization; Purification of biogenic crystals), Table2,
    Figures1,3-5; PDFpp.4,6-7,12'
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Independently reread retained complete institutional PDF and verified original
    acquisition hash. Visually checked Table2/Figure1 and Figures3-5. Methods explicitly
    identify synthetic feed as dittmarite, living ATCC1015,1%solid-medium arm,25Cdark,7dayphase
    collection; Figure1C is a3day clearing zone. Figure5A/B matches published glushinskite
    reference and C/D are feed controls. No liquid-arm yield transferred.
  snapshot_sha256: 13f7d2deb8340715bec8748d53a77d61885ebe05b903c55f6273fb82a61298b7
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1111/1462-2920.14949
  locator: Results transformation subsection, Table2; Figure5; Experimental procedures,
    crystal purification and liquid culture
  accessed_at: '2026-10-11T10:01:37Z'
  support: context_only
  summary: Amorphous debris accompanies crystals; selected solids collected with80Cwater
    and washing. Mineral-free fungal controls and feed diffraction do not isolate
    oxalate-specific action from acidification in chemistry-matched assays. Liquid105rpm/125rpm
    discrepancy and equimolar-reagent wording are not imported into the selected solid
    experiment; no complete conversion, phase fraction or recovered-metal yield asserted.
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&mode=Info
  locator: Fresh live NCBI browser entry and independently read retained taxonomy
    XML
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: NCBITaxon380704 resolves Aspergillus niger ATCC1015. Retained XML explicitly
    reports rank strain, matching the exact reported experimental strain; does not
    imply new culture authentication.
  snapshot_sha256: 93bd7f58b9967dd080c971d4980128b3bdb35f9e4aa9c86ef3d1065fc404a500
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round15-mineral-review/search.json
  locator: Two exact live searches and ignored/hidden-inclusive local dedup log
  accessed_at: '2026-10-11T10:01:37Z'
  support: context_only
  summary: Original bounded correction search remains valid but its original source-lineage
    summary was erroneous. The new glushinskite and dittmarite records reuse Suyamud
    et al. (2020), DOI 10.1111/1462-2920.14949, already curated under magnesium. The
    existing struvite record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0,
    a separate experiment; it is not part of that Suyamud reuse group. New forsterite/talc
    literature remains a full-methods acquisition lead; no new live literature search
    is claimed in this correction round.
  search_scope: Original review used rg --no-ignore --hidden --follow across data,
    research, reviews, history and /private/tmp/cmm-round15-mineral-raw and two first-window
    web searches without filters. This successor rereads the exact source lists and
    evidence links of magnesium.yaml, struvite.yaml, glushinskite.yaml and dittmarite.yaml
    with ignored/hidden-inclusive matching. The new glushinskite and dittmarite records
    reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949, already curated under
    magnesium. The existing struvite record instead curates Kang et al. (2022), DOI
    10.1007/s00253-021-11721-0, a separate experiment; it is not part of that Suyamud
    reuse group.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round15-gate-receipts.json
  locator: Actual root gate receipts and check/require/history logs; independent named
    receipt
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Offline structure, nonempty corpus and append-only provenance gates passed;
    reviewed current record hashes and inputs remain unchanged. Checks do not independently
    validate mineralogy.
  snapshot_sha256: 6305164a252d489178c974d78093f646c5e73ccc6862e7b8d6d4afd267cdbd71
- evidence_id: lineage-correction
  kind: record_content
  reference: data/records/magnesium.yaml; data/records/struvite.yaml
  locator: Current full source lists, mechanism evidence source_refs and descriptions;
    predecessor evidence[search].search_scope and limitations
  accessed_at: '2026-10-11T10:05:35Z'
  support: supports
  summary: The new glushinskite and dittmarite records reuse Suyamud et al. (2020),
    DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite
    record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate
    experiment; it is not part of that Suyamud reuse group. Independently reread all
    four record source lists after fresh inspect. Both new mineral records already
    described the reuse group correctly; the mistake existed only in the predecessor
    review prose.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261011T100137Z-dittmarite-round15-independent/review.yaml
  locator: Complete immutable predecessor YAML and generated Markdown
  accessed_at: '2026-10-11T10:05:35Z'
  support: context_only
  summary: Preserved exact predecessor review bytes. No record finding existed (findings=[]),
    so this successor does not invent a resolved finding or previous_occurrences identity;
    the correction is review provenance, tracked in issue61.
  snapshot_sha256: f0572d369bebe1bef5f00d074a3048092d67fa46d96af0c2bd7f4094244791d0
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species and hydration-state boundary
  outcome: supported
  summary: Dittmarite is an IMA-listed mineral species (magnesium ammonium phosphate
    monohydrate, (NH4)Mg(PO4)(H2O)), distinct from elemental constituents, struvite
    and the other magnesium mineral root. Study reuse is explicit and no criticality
    is inherited.
  target_ids:
  - cmmmech:dittmarite
  evidence_ids:
  - ima
  - record
  - primary
  - search
  dimensions:
  - name: material_form
    value: magnesium ammonium phosphate monohydrate, (NH4)Mg(PO4)(H2O)
    definition: Mineral identity, not elemental constituent, commodity or all unspecified
      magnesium salts.
    evidence_ids:
    - ima
    - primary
  - name: criticality
    value: Not asserted
    definition: No inherited jurisdiction/list/edition claim from magnesium or phosphorus.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Living fungal solid-medium transformation
  outcome: supported
  summary: Synthetic monohydrate identity is established by source methods and Figure5D
    despite the paper's broad synthetic-struvite wording. Clearing at3days, acidification
    and7day secondary oxalate formation are correctly distinguished; no dissolution
    fraction is inferred. Record retains the source's controls, amorphous debris and
    unmeasured product-yield limitations.
  target_ids:
  - cmmmech:dittmarite
  evidence_ids:
  - primary
  - limits
  - taxon
  - record
  dimensions:
  - name: organism_biomass
    value: Growing Aspergillus niger ATCC1015,NCBITaxon380704
    definition: Exact reported strain and living colony during the assay, rather than
      inactive biomass or unconstrained species generalization.
    evidence_ids:
    - primary
    - taxon
  - name: conditions_controls
    value: 1%w/v mineral on MEA;25Cdark;3dayhalo versus7dayphasecollection; feed diffraction/mineral-free
      fungal comparisons
    definition: Selected solid-medium experiment; chemistry-matched abiotic causality
      is not established.
    evidence_ids:
    - primary
    - limits
  - name: scale_outcome
    value: Laboratory phase transformation; no isolated elemental recovery or industrial
      deployment
    definition: Observed crystal assignment and clearing do not measure pure phase
      mass fraction or whole-feed recovery.
    evidence_ids:
    - primary
    - limits
- assessment_id: provenance
  area: provenance
  topic: Exact current bytes and actual CREATE history
  outcome: supported
  summary: Record and sidecar inspected at trusted main base with explicit uncommitted
    state; actor/model/timestamp and exact record target agree. Independent reviewer
    did not curate the mineral. Batch and named validation passed.
  target_ids:
  - cmmmech:dittmarite
  evidence_ids:
  - record
  - gates
- assessment_id: source-lineage
  area: provenance
  topic: Correction of predecessor review experimental-source lineage
  outcome: supported
  summary: The new glushinskite and dittmarite records reuse Suyamud et al. (2020),
    DOI 10.1111/1462-2920.14949, already curated under magnesium. The existing struvite
    record instead curates Kang et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate
    experiment; it is not part of that Suyamud reuse group. This corrects both erroneous
    predecessor passages without altering target content or prior review artifacts.
  target_ids:
  - cmmmech:dittmarite
  evidence_ids:
  - lineage-correction
  - predecessor
  - record
  dimensions:
  - name: source_reuse
    value: 'Suyamud2020: magnesium, glushinskite, dittmarite; Kang2022: existing struvite
      context'
    definition: Record-to-primary-study lineage; sharing a mineral or fungal strain
      does not make two different papers one experimental replication.
    evidence_ids:
    - lineage-correction
findings: []
actions: []
limitations:
- Published XRD phase assignment was checked against the presented comparison but
  raw diffraction data were not refitted; purity and complete-conversion fraction
  remain unmeasured.
- The selected solid-medium comparisons lack chemistry-matched abiotic controls that
  would isolate contributions of acidification, oxalate and living fungal metabolism.
- The new glushinskite and dittmarite records reuse Suyamud et al. (2020), DOI 10.1111/1462-2920.14949,
  already curated under magnesium. The existing struvite record instead curates Kang
  et al. (2022), DOI 10.1007/s00253-021-11721-0, a separate experiment; it is not
  part of that Suyamud reuse group.
- Bounded literature searches are not exhaustive; the newly identified forsterite/talc
  study remains a full-methods acquisition lead.
tags:
- round15
- independent
- scientific-review
- mineral
- successor
- review-provenance-correction
notes:
- Correction tracked by https://github.com/CultureBotAI/CMMMech/issues/61. The previous
  review incorrectly stated that existing magnesium and struvite both reused Suyamud2020.
  Corrected lineage is explicitly assessed here.
- No maintained record, history sidecar, predecessor YAML or generated Markdown was
  edited. Findings remain empty because the correction concerns review context, not
  a newly discovered target defect.
- Primary methods, rendered figures, authority rows and taxonomy were checked during
  the immediately preceding independent review. This successor rechecks unchanged
  exact target fields and contextual source lineage; it does not claim a new complete
  literature acquisition or new experimental validation.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261011T100137Z-dittmarite-round15-independent
  relationship: Corrects experimental-source lineage context in evidence[search].search_scope
    and limitations; retains identical target hash and scientific verdict, preserving
    predecessor immutably.
links:
- https://github.com/CultureBotAI/CMMMech/issues/61
```
