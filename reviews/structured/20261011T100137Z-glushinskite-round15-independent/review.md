# Independent scientific review of Glushinskite

- Review: 20261011T100137Z-glushinskite-round15-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:59:55Z
- Finished UTC: 2026-10-11T10:01:37Z
- Reviewer: Codex /root/round15_brine (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Mineral identity and scoped solid-medium fungal transformation are supported. Source reuse, control limitations, phase purity and deployment bounds are explicit; no actionable findings.

## Scope And Provenance

All fields and linked CREATE provenance of one exact new mineral record; primary identity and selected mechanism claims.

Selection: One assigned mineral from round15; full record assessment, not all experiments in the source paper.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:glushinskite | data/records/glushinskite.yaml | maintained | Glushinskite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named-record validation | passed | True | cmmmech:glushinskite | Reviewer subprocess terminal exit0 at2026-10-11T10:00:41Z;2records0failed. Exact receipt read and retained at /private/tmp/cmm-round15-mineral-review/named-receipt.json. |
| Completed root batch check | passed | True | cmmmech:glushinskite | Root terminal gate:308tests passed,3skipped;122records and138histories valid. Reviewer read root gate receipt and actual logs; record hash remained unchanged. |
| Nonempty corpus validation | passed | True | cmmmech:glushinskite | Root terminal gate:122records,0failed. Reviewer read root gate receipt and actual logs; record hash remained unchanged. |
| Append-only history validation | passed | True | cmmmech:glushinskite | Root terminal gate:138history records,0errors at trusted base. Reviewer read root gate receipt and actual logs; record hash remained unchanged. |

## Scientific And Domain Assessments

### Mineral species and hydration-state boundary

identity: supported. Targets: cmmmech:glushinskite.

Glushinskite is an IMA-listed mineral species (magnesium oxalate dihydrate, Mg(C2O4)(H2O)2), distinct from elemental constituents, struvite and the other magnesium mineral root. Study reuse is explicit and no criticality is inherited.

### Living fungal solid-medium transformation

evidence: supported. Targets: cmmmech:glushinskite.

Product phase identified after fungal growth on natural struvite and XRD-identified synthetic dittmarite; chemical necessity and isolated purity/yield are not claimed. Record retains the source's controls, amorphous debris and unmeasured product-yield limitations.

### Exact current bytes and actual CREATE history

provenance: supported. Targets: cmmmech:glushinskite.

Record and sidecar inspected at trusted main base with explicit uncommitted state; actor/model/timestamp and exact record target agree. Independent reviewer did not curate the mineral. Batch and named validation passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/glushinskite.yaml; Entire maintained YAML plus exact linked CREATE sidecar | supports | Independent reviewer read all maintained fields and actual sidecar. Exact inspected working bytes, actor/model and timestamps match the new creation; history and scientific review remain separate. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; IMA September2026 PDF p.84, mineral row; pp.1-2 column definitions and reuse terms | supports | Independently reread retained official PDF acquired09:55UTC this round, verified SHA, rendered row and definitions. Supports magnesium oxalate dihydrate, Mg(C2O4)(H2O)2; grandfathered original-description year or special-procedure redefinition year is not an invented approval CURIE. No fresh reviewer PDF download claimed. |
| primary | https://doi.org/10.1111/1462-2920.14949; Full published PDF: Experimental procedures (Organisms and media; Struvite preparation; Struvite solubilization; Purification of biogenic crystals), Table2, Figures1,3-5; PDFpp.4,6-7,12 | supports | Independently reread retained complete institutional PDF and verified original acquisition hash. Visually checked Table2/Figure1 and Figures3-5. Methods explicitly identify synthetic feed as dittmarite, living ATCC1015,1%solid-medium arm,25Cdark,7dayphase collection; Figure1C is a3day clearing zone. Figure5A/B matches published glushinskite reference and C/D are feed controls. No liquid-arm yield transferred. |
| limits | https://doi.org/10.1111/1462-2920.14949; Results transformation subsection, Table2; Figure5; Experimental procedures, crystal purification and liquid culture | context_only | Amorphous debris accompanies crystals; selected solids collected with80Cwater and washing. Mineral-free fungal controls and feed diffraction do not isolate oxalate-specific action from acidification in chemistry-matched assays. Liquid105rpm/125rpm discrepancy and equimolar-reagent wording are not imported into the selected solid experiment; no complete conversion, phase fraction or recovered-metal yield asserted. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704&amp;mode=Info; Fresh live NCBI browser entry and independently read retained taxonomy XML | supports | NCBITaxon380704 resolves Aspergillus niger ATCC1015. Retained XML explicitly reports rank strain, matching the exact reported experimental strain; does not imply new culture authentication. |
| search | /private/tmp/cmm-round15-mineral-review/search.json; Two exact live searches and ignored/hidden-inclusive local dedup log | context_only | Bounded correction and contrary-mechanism search; no affecting notice returned, not absence certification. Cai2013forsterite/talc abstract shows substrate dependence and is a full-methods acquisition lead. Existing magnesium/struvite experiments and new mineral roots are distinguished. |
| gates | /private/tmp/cmm-round15-gate-receipts.json; Actual root gate receipts and check/require/history logs; independent named receipt | supports | Offline structure, nonempty corpus and append-only provenance gates passed; reviewed current record hashes and inputs remain unchanged. Checks do not independently validate mineralogy. |

## Limits And Additional Notes

- Published XRD phase assignment was checked against the presented comparison but raw diffraction data were not refitted; purity and complete-conversion fraction remain unmeasured.
- Chemistry-matched abiotic controls do not isolate the contribution of acidification, oxalate and living fungal metabolism in the selected solid-medium assay.
- Existing magnesium and struvite records reuse the same experiment; distinct mineral roots are not independent replications.
- Bounded literature searches are not exhaustive; the newly identified forsterite/talc study remains a full-methods acquisition lead.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T100137Z-glushinskite-round15-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Glushinskite
started_at: '2026-10-11T09:59:55Z'
finished_at: '2026-10-11T10:01:37Z'
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
summary: Mineral identity and scoped solid-medium fungal transformation are supported.
  Source reuse, control limitations, phase purity and deployment bounds are explicit;
  no actionable findings.
source:
  git_revision: a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0
  state: working_tree
  inputs:
  - path: data/records/glushinskite.yaml
    sha256: 5ccb9078ddb4c0c2910d827f1afd426d489c78656aa8c5fa8ebc40b303e11a67
    role: target
  - path: history/records/glushinskite/2026-10-11T095727Z-codex-e44619.yaml
    sha256: 69c3713758910d21b7f8ffe106bea39d3cd51c450ea59be4b2907d2b1b7f0bf6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields and linked CREATE provenance of one exact new mineral record;
    primary identity and selected mechanism claims.
  selection: One assigned mineral from round15; full record assessment, not all experiments
    in the source paper.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:glushinskite
  exclusions:
  - target: Liquid-culture assays, other records and raw crystallographic reanalysis
    reason: Liquid assays are intentionally outside curated mechanism; related records
      checked for boundaries only, raw diffraction intensities not acquired or refitted.
targets:
- target_id: cmmmech:glushinskite
  path: data/records/glushinskite.yaml
  label: Glushinskite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/glushinskite.yaml
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
  target_ids:
  - cmmmech:glushinskite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed root batch check
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Root terminal gate:308tests passed,3skipped;122records and138histories
    valid. Reviewer read root gate receipt and actual logs; record hash remained unchanged.
  target_ids:
  - cmmmech:glushinskite
  exit_code: 0
  expected_exit_code: 0
- check_id: require
  name: Nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Root terminal gate:122records,0failed. Reviewer read root gate receipt
    and actual logs; record hash remained unchanged.
  target_ids:
  - cmmmech:glushinskite
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0
  status: passed
  required: true
  summary: Root terminal gate:138history records,0errors at trusted base. Reviewer
    read root gate receipt and actual logs; record hash remained unchanged.
  target_ids:
  - cmmmech:glushinskite
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/glushinskite.yaml
  locator: Entire maintained YAML plus exact linked CREATE sidecar
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Independent reviewer read all maintained fields and actual sidecar. Exact
    inspected working bytes, actor/model and timestamps match the new creation; history
    and scientific review remain separate.
  snapshot_sha256: 5ccb9078ddb4c0c2910d827f1afd426d489c78656aa8c5fa8ebc40b303e11a67
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: IMA September2026 PDF p.84, mineral row; pp.1-2 column definitions and
    reuse terms
  accessed_at: '2026-10-11T10:01:37Z'
  support: supports
  summary: Independently reread retained official PDF acquired09:55UTC this round,
    verified SHA, rendered row and definitions. Supports magnesium oxalate dihydrate,
    Mg(C2O4)(H2O)2; grandfathered original-description year or special-procedure redefinition
    year is not an invented approval CURIE. No fresh reviewer PDF download claimed.
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
  summary: Bounded correction and contrary-mechanism search; no affecting notice returned,
    not absence certification. Cai2013forsterite/talc abstract shows substrate dependence
    and is a full-methods acquisition lead. Existing magnesium/struvite experiments
    and new mineral roots are distinguished.
  search_scope: rg --no-ignore --hidden --follow across data, research, reviews, history
    and /private/tmp/cmm-round15-mineral-raw; existing magnesium and struvite records
    explicitly reuse Suyamud2020. Two first-window web searches with no filters; no
    exhaustive pagination.
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
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral species and hydration-state boundary
  outcome: supported
  summary: Glushinskite is an IMA-listed mineral species (magnesium oxalate dihydrate,
    Mg(C2O4)(H2O)2), distinct from elemental constituents, struvite and the other
    magnesium mineral root. Study reuse is explicit and no criticality is inherited.
  target_ids:
  - cmmmech:glushinskite
  evidence_ids:
  - ima
  - record
  - primary
  - search
  dimensions:
  - name: material_form
    value: magnesium oxalate dihydrate, Mg(C2O4)(H2O)2
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
  summary: Product phase identified after fungal growth on natural struvite and XRD-identified
    synthetic dittmarite; chemical necessity and isolated purity/yield are not claimed.
    Record retains the source's controls, amorphous debris and unmeasured product-yield
    limitations.
  target_ids:
  - cmmmech:glushinskite
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
  - cmmmech:glushinskite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Published XRD phase assignment was checked against the presented comparison but
  raw diffraction data were not refitted; purity and complete-conversion fraction
  remain unmeasured.
- Chemistry-matched abiotic controls do not isolate the contribution of acidification,
  oxalate and living fungal metabolism in the selected solid-medium assay.
- Existing magnesium and struvite records reuse the same experiment; distinct mineral
  roots are not independent replications.
- Bounded literature searches are not exhaustive; the newly identified forsterite/talc
  study remains a full-methods acquisition lead.
tags:
- round15
- independent
- scientific-review
- mineral
```
