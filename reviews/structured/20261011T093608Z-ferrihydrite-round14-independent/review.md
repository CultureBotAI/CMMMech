# Independent scientific review of Ferrihydrite

- Review: 20261011T093608Z-ferrihydrite-round14-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:30:05Z
- Finished UTC: 2026-10-11T09:36:08Z
- Reviewer: Codex /root/round14_products (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Scientifically supported species identity and bounded assay interpretation; no actionable record defects. Known source inconsistencies and laboratory transfer limits remain explicit.

## Scope And Provenance

All fields, cited evidence and linked CREATE provenance of one exact new uncommitted mineral record.

Selection: Assigned six-mineral cohort; this per-record observation covers only cmmmech:ferrihydrite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ferrihydrite | data/records/ferrihydrite.yaml | maintained | Ferrihydrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named mineral validation | passed | True | cmmmech:ferrihydrite | Reviewer session60838 terminal0;6 records,0failed; /private/tmp/cmm-round14-mineral-review/named-validation.log |
| Reviewer trusted-base history validation | passed | True | cmmmech:ferrihydrite | Reviewer session63319 terminal0;134 histories,0errors; /private/tmp/cmm-round14-mineral-review/history-validation.log |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:ferrihydrite | Root executed; reviewer read actual logs. Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |
| Required corpus | passed | True | cmmmech:ferrihydrite | Root executed; reviewer read actual logs. Terminal0 session1358:119records,0failed. /private/tmp/cmm-round14-require.log |
| Trusted-base history | passed | True | cmmmech:ferrihydrite | Root executed; reviewer read actual logs. Terminal0 session1358:134histories,0errors. /private/tmp/cmm-round14-history.log |

## Scientific And Domain Assessments

### Species identity, taxonomy, criticality and experimental material distinction

identity: supported. Targets: cmmmech:ferrihydrite.

IMA September 2026 ferrihydrite formula Fe(III)5O7(OH), approved1971-015. The synthetic two-line assay substrate does not establish ideal formula or natural provenance. No inherited iron criticality.

### Primary methods, controls, quantities and inference boundaries

evidence: supported. Targets: cmmmech:ferrihydrite.

Living Ax17 DSM111878 transforms synthetic ferrihydrite to a black magnetic mixed product. Oxalate dissolution followed by ferrozine yields reported24 mM FeII vs2–3 mM controls; not dissolved Fe or percent recovery. The84% pre-oxalate filter retention is particulate fraction, not magnetite phase yield. Heated/unheated uninoculated arms share cysteine and addedFeII. Main and supplement spectra support primarily cation-deficient magnetite with residual/other phases.

Reported100 mmol/L mineral is retained without assuming ideal ferrihydrite formula for an Fe mass balance. Low-temperature Mossbauer spectra exclude pure magnetite; XRD alone cannot resolve magnetite versus maghemite/cation-deficient magnetite. Heated abiotic controls show lepidocrocite and possible minor magnetite; the product is not uniquely diagnostic of biology.

### Actual working changes, author attribution and gate scope

provenance: supported. Targets: cmmmech:ferrihydrite.

New record and actual CREATE sidecar target match; reviewed bytes match initial inspect and the batch gate. No older history/review was rewritten. Saving this review neither alters the record nor adds a curation event.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/ferrihydrite.yaml; All target fields and linked CREATE sidecar; target inspected before assessment at09:30:05Z; final context inspection confirms same scientific bytes | supports | New uncommitted record and matching CREATE event under trusted merged base. Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar are distinct. Reviewer authored no mineral records or histories. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF page69, Ferrihydrite row; pages1–2 definitions and reuse terms | supports | IMA September 2026 ferrihydrite formula Fe(III)5O7(OH), approved1971-015. The synthetic two-line assay substrate does not establish ideal formula or natural provenance. No inherited iron criticality. Independently read retained official PDF text and date/status definitions. |
| paper | https://doi.org/10.3389/fmicb.2023.1272245; Methods; Cell growth on ferrihydrite; Figures1–3 and accompanying TEM/XRD interpretation; retained supplement FiguresS2–S5 visually inspected | supports | Living Ax17 DSM111878 transforms synthetic ferrihydrite to a black magnetic mixed product. Oxalate dissolution followed by ferrozine yields reported24 mM FeII vs2–3 mM controls; not dissolved Fe or percent recovery. The84% pre-oxalate filter retention is particulate fraction, not magnetite phase yield. Heated/unheated uninoculated arms share cysteine and addedFeII. Main and supplement spectra support primarily cation-deficient magnetite with residual/other phases. Independently inspected retained original evidence at /private/tmp/cmm-round14-mineral-raw/sklute.pdf. |
| search | /private/tmp/cmm-round14-mineral-review/web-search-transcript.json; Exact queries, observed first result windows and hidden/ignored-inclusive dedup.txt | context_only | No applicable correction/retraction notice surfaced in the returned windows; that bounded result is not a global absence claim. Existing elemental experiments and dossiers are recognized as shared evidence. Nearby additional studies are extension leads rather than evidence for broader claims in this record. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Root actual terminal-zero receipt plus check, require and history logs; named reviewer6/0 and history134/0 | supports | Reviewer read root logs:307 passed,3 skipped in80.06s;119 records;134 histories. This batch gate precedes an unrelated pending FCC wording correction; all six mineral hashes remain unchanged. Reviewer independently executed named validation and history. Offline validation is not scientific proof. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2831190; Retained NCBI XML or browser HTML: TaxId, ScientificName, Rank, relevant type material | supports | 2831190 resolves to Desulfovulcanus ferrireducens, rankspecies; paper-specific strain assignment is not strengthened beyond authority support. |
| supplement | https://doi.org/10.3389/fmicb.2023.1272245; Retained original Data Sheet1, FiguresS2–S5 pp6–9; actual spectral-fit/XRD pixels | supports | Independent inspection confirms mixed Mossbauer fits at295K/4K, heated/unheated controls and overlapping magnetite/maghemite XRD. Reused supplement from an earlier legitimate acquisition, not a claimed fresh successful download. |

## Limits And Additional Notes

- Reported100 mmol/L mineral is retained without assuming ideal ferrihydrite formula for an Fe mass balance.
- Low-temperature Mossbauer spectra exclude pure magnetite; XRD alone cannot resolve magnetite versus maghemite/cation-deficient magnetite.
- Heated abiotic controls show lepidocrocite and possible minor magnetite; the product is not uniquely diagnostic of biology.
- Fresh DOI reader routes for Blazevic, Topolska, Kang and Sklute failed or returned access errors in this review. Independently read legitimate retained original PDFs/XML and rendered relevant original figures/tables instead; raw hashes and source acquisition provenance are retained. This is not a claim of fresh successful download of every source.
- Laboratory observations do not establish industrial deployment; bounded correction/conflict search is not exhaustive.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093608Z-ferrihydrite-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Ferrihydrite
started_at: '2026-10-11T09:30:05Z'
finished_at: '2026-10-11T09:36:08Z'
reviewer:
  identity: Codex /root/round14_products
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different subagent /root/round14_minerals authored the mineral
    records and histories. This reviewer independently inspected exact bytes, primary
    source methods, relevant figures/tables and identifiers, and did not edit those
    records. Reviewer authored separate product commodity records in the same batch;
    independence is record-author separation, not organizational separation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Scientifically supported species identity and bounded assay interpretation;
  no actionable record defects. Known source inconsistencies and laboratory transfer
  limits remain explicit.
source:
  git_revision: 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  state: working_tree
  inputs:
  - path: data/records/ferrihydrite.yaml
    sha256: 2de9e5fdbd96b7d9ec8b74c7b09ffd04951e1351288c88a37872fd4a0c22791c
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/ferrihydrite/2026-10-11T092701Z-codex-96a5b2.yaml
    sha256: 98461c0c42d917e17a16b65a875be3facf0f7c36d0fd6bf063b5150d63faafbb
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, cited evidence and linked CREATE provenance of one exact
    new uncommitted mineral record.
  selection: Assigned six-mineral cohort; this per-record observation covers only
    cmmmech:ferrihydrite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ferrihydrite
  exclusions:
  - target: Uncurated literature and unrelated records
    reason: Context and contradiction searches are bounded; no corpus-wide scientific
      recertification.
targets:
- target_id: cmmmech:ferrihydrite
  path: data/records/ferrihydrite.yaml
  label: Ferrihydrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrihydrite.yaml
    role: maintained_record
  record_class: mineral
checks:
- check_id: named
  name: Reviewer named mineral validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/scheelite.yaml data/records/pyromorphite.yaml data/records/struvite.yaml
    data/records/ferrihydrite.yaml data/records/magnetite.yaml data/records/pyrolusite.yaml
  status: passed
  required: true
  summary: Reviewer session60838 terminal0;6 records,0failed; /private/tmp/cmm-round14-mineral-review/named-validation.log
  target_ids:
  - cmmmech:ferrihydrite
  exit_code: 0
  expected_exit_code: 0
- check_id: reviewer-history
  name: Reviewer trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  summary: Reviewer session63319 terminal0;134 histories,0errors; /private/tmp/cmm-round14-mineral-review/history-validation.log
  target_ids:
  - cmmmech:ferrihydrite
  exit_code: 0
  expected_exit_code: 0
- check_id: root-batch
  name: Native full batch checks before FCC wording correction
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer read actual logs. Terminal0 session53639:307 passed,3
    skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log.
    FCC wording correction pending; this gate covers other unchanged targets.
  target_ids:
  - cmmmech:ferrihydrite
- check_id: root-require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer read actual logs. Terminal0 session1358:119records,0failed.
    /private/tmp/cmm-round14-require.log
  target_ids:
  - cmmmech:ferrihydrite
- check_id: root-history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer read actual logs. Terminal0 session1358:134histories,0errors.
    /private/tmp/cmm-round14-history.log
  target_ids:
  - cmmmech:ferrihydrite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/ferrihydrite.yaml
  locator: All target fields and linked CREATE sidecar; target inspected before assessment
    at09:30:05Z; final context inspection confirms same scientific bytes
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: New uncommitted record and matching CREATE event under trusted merged base.
    Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar
    are distinct. Reviewer authored no mineral records or histories.
  snapshot_sha256: 2de9e5fdbd96b7d9ec8b74c7b09ffd04951e1351288c88a37872fd4a0c22791c
- evidence_id: ima
  kind: primary_source
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF page69, Ferrihydrite row; pages1–2 definitions and reuse terms
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: IMA September 2026 ferrihydrite formula Fe(III)5O7(OH), approved1971-015.
    The synthetic two-line assay substrate does not establish ideal formula or natural
    provenance. No inherited iron criticality. Independently read retained official
    PDF text and date/status definitions.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1272245
  locator: Methods; Cell growth on ferrihydrite; Figures1–3 and accompanying TEM/XRD
    interpretation; retained supplement FiguresS2–S5 visually inspected
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: Living Ax17 DSM111878 transforms synthetic ferrihydrite to a black magnetic
    mixed product. Oxalate dissolution followed by ferrozine yields reported24 mM
    FeII vs2–3 mM controls; not dissolved Fe or percent recovery. The84% pre-oxalate
    filter retention is particulate fraction, not magnetite phase yield. Heated/unheated
    uninoculated arms share cysteine and addedFeII. Main and supplement spectra support
    primarily cation-deficient magnetite with residual/other phases. Independently
    inspected retained original evidence at /private/tmp/cmm-round14-mineral-raw/sklute.pdf.
  snapshot_sha256: d36613a038eccc0f05dc944e09ced3920940e32360b765d318484154d54f26c6
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round14-mineral-review/web-search-transcript.json
  locator: Exact queries, observed first result windows and hidden/ignored-inclusive
    dedup.txt
  accessed_at: '2026-10-11T09:36:08Z'
  support: context_only
  summary: No applicable correction/retraction notice surfaced in the returned windows;
    that bounded result is not a global absence claim. Existing elemental experiments
    and dossiers are recognized as shared evidence. Nearby additional studies are
    extension leads rather than evidence for broader claims in this record.
  search_scope: rg --no-ignore --hidden --follow -n -i over data/records, research,
    reviews, history, /private/tmp/cmm-round14-mineral-raw, /private/tmp/cmm-round14-product-raw,
    /private/tmp/cmm-round8-pb-bi-evidence and /private/tmp/cmm-round5-iron-evidence-20261011
    for six mineral names, seven cited DOIs, gluconic acid secretion and 1462-2920.14949;
    2889 matched lines. Twelve exact web queries retained in web-search-transcript.json;
    first returned windows only, no exhaustive Crossmark/retraction census.
  snapshot_sha256: 0710ec94c31426f6c33b695179422c039e15660e3f2c110edc5d0731272c1190
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round14-gate-receipts-initial.json
  locator: Root actual terminal-zero receipt plus check, require and history logs;
    named reviewer6/0 and history134/0
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: Reviewer read root logs:307 passed,3 skipped in80.06s;119 records;134 histories.
    This batch gate precedes an unrelated pending FCC wording correction; all six
    mineral hashes remain unchanged. Reviewer independently executed named validation
    and history. Offline validation is not scientific proof.
  snapshot_sha256: cd1d462bdeea6cc6174ffa7ccff29bf6f49a9037541c6b3327fb923fc64106bb
- evidence_id: taxonomy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2831190
  locator: 'Retained NCBI XML or browser HTML: TaxId, ScientificName, Rank, relevant
    type material'
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: 2831190 resolves to Desulfovulcanus ferrireducens, rankspecies; paper-specific
    strain assignment is not strengthened beyond authority support.
  snapshot_sha256: b81790b3e68bd34b2f9eff752ec8edd0fc048a9b1cc53da413e88c76cffbffba
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1272245
  locator: Retained original Data Sheet1, FiguresS2–S5 pp6–9; actual spectral-fit/XRD
    pixels
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: Independent inspection confirms mixed Mossbauer fits at295K/4K, heated/unheated
    controls and overlapping magnetite/maghemite XRD. Reused supplement from an earlier
    legitimate acquisition, not a claimed fresh successful download.
  snapshot_sha256: f4d4514592189e6c68ecf0466c858919e946208c2ec71a6fb4c2834793b43455
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, taxonomy, criticality and experimental material distinction
  outcome: supported
  summary: IMA September 2026 ferrihydrite formula Fe(III)5O7(OH), approved1971-015.
    The synthetic two-line assay substrate does not establish ideal formula or natural
    provenance. No inherited iron criticality.
  target_ids:
  - cmmmech:ferrihydrite
  evidence_ids:
  - ima
  - taxonomy
  - record
  - search
  dimensions:
  - name: material_form
    value: IMA September 2026 ferrihydrite formula Fe(III)5O7(OH), approved1971-015.
      The synthetic two-line assay substrate does not establish ideal formula or natural
      provenance. No inherited iron criticality.
    definition: Exact species versus measured substrate/product boundary.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: biomass
    value: Living Desulfovulcanus ferrireducens Ax17 DSM111878; species-level NCBITaxon2831190
    definition: Biomass state and taxonomic scope of accepted mechanism.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: conditions
    value: 50 mL modifiedDSM981/160 mL;reported100 mmol/L synthetic two-line ferrihydrite;pH6.80±.05;0.5
      mM cysteine,1.3 mM FeCl2;H2CO2 80:20 200 kPa;55 C~5 d
    definition: Reported assay conditions, not universal process conditions.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: controls_outcome
    value: Triplicate culture, heated/unheated uninoculated controls; oxalate/ferrozine
      and separate filtration; mixed product spectra
    definition: Control contrast, measurement definition and inference limits.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: criticality
    value: No criticality claims asserted
    definition: No constituent-element status transferred to species; no absent jurisdiction/list/edition
      invented.
    evidence_ids:
    - record
    - paper
    - taxonomy
- assessment_id: science
  area: evidence
  topic: Primary methods, controls, quantities and inference boundaries
  outcome: supported
  summary: Living Ax17 DSM111878 transforms synthetic ferrihydrite to a black magnetic
    mixed product. Oxalate dissolution followed by ferrozine yields reported24 mM
    FeII vs2–3 mM controls; not dissolved Fe or percent recovery. The84% pre-oxalate
    filter retention is particulate fraction, not magnetite phase yield. Heated/unheated
    uninoculated arms share cysteine and addedFeII. Main and supplement spectra support
    primarily cation-deficient magnetite with residual/other phases.
  details: Reported100 mmol/L mineral is retained without assuming ideal ferrihydrite
    formula for an Fe mass balance. Low-temperature Mossbauer spectra exclude pure
    magnetite; XRD alone cannot resolve magnetite versus maghemite/cation-deficient
    magnetite. Heated abiotic controls show lepidocrocite and possible minor magnetite;
    the product is not uniquely diagnostic of biology.
  target_ids:
  - cmmmech:ferrihydrite
  evidence_ids:
  - paper
  - supplement
  - record
  - search
- assessment_id: provenance
  area: provenance
  topic: Actual working changes, author attribution and gate scope
  outcome: supported
  summary: New record and actual CREATE sidecar target match; reviewed bytes match
    initial inspect and the batch gate. No older history/review was rewritten. Saving
    this review neither alters the record nor adds a curation event.
  target_ids:
  - cmmmech:ferrihydrite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Reported100 mmol/L mineral is retained without assuming ideal ferrihydrite formula
  for an Fe mass balance.
- Low-temperature Mossbauer spectra exclude pure magnetite; XRD alone cannot resolve
  magnetite versus maghemite/cation-deficient magnetite.
- Heated abiotic controls show lepidocrocite and possible minor magnetite; the product
  is not uniquely diagnostic of biology.
- Fresh DOI reader routes for Blazevic, Topolska, Kang and Sklute failed or returned
  access errors in this review. Independently read legitimate retained original PDFs/XML
  and rendered relevant original figures/tables instead; raw hashes and source acquisition
  provenance are retained. This is not a claim of fresh successful download of every
  source.
- Laboratory observations do not establish industrial deployment; bounded correction/conflict
  search is not exhaustive.
tags:
- round14
- independent
- scientific-review
```
