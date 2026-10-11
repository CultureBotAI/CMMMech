# Independent scientific review of Scheelite

- Review: 20261011T093608Z-scheelite-round14-independent
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

Selection: Assigned six-mineral cohort; this per-record observation covers only cmmmech:scheelite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:scheelite | data/records/scheelite.yaml | maintained | Scheelite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named mineral validation | passed | True | cmmmech:scheelite | Reviewer session60838 terminal0;6 records,0failed; /private/tmp/cmm-round14-mineral-review/named-validation.log |
| Reviewer trusted-base history validation | passed | True | cmmmech:scheelite | Reviewer session63319 terminal0;134 histories,0errors; /private/tmp/cmm-round14-mineral-review/history-validation.log |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:scheelite | Root executed; reviewer read actual logs. Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |
| Required corpus | passed | True | cmmmech:scheelite | Root executed; reviewer read actual logs. Terminal0 session1358:119records,0failed. /private/tmp/cmm-round14-require.log |
| Trusted-base history | passed | True | cmmmech:scheelite | Root executed; reviewer read actual logs. Terminal0 session1358:134histories,0errors. /private/tmp/cmm-round14-history.log |

## Scientific And Domain Assessments

### Species identity, taxonomy, criticality and experimental material distinction

identity: supported. Targets: cmmmech:scheelite.

IMA September 2026 Ca(WO4), grandfathered G, original-description year 1821. Species distinct from W element, wolframite and impure concentrate; no inherited criticality.

### Primary methods, controls, quantities and inference boundaries

evidence: supported. Targets: cmmmech:scheelite.

Living DSM5348 cultures at 73 C, initial pH2 with CO2 and 10 g/L sterilized, impure 1-mm scheelite concentrate show greater filter-passing W than uninoculated same-feed controls. ICP-OES of centrifuged 0.44-micrometre filtrate over21 days is not an isolated-product yield. Figure3 n=3/SD and abiotic release are visible. No exact W value is transferred from the log10/mg/L and day/hour ambiguity.

The energy source and Fe/Mn oxidation contribution are unresolved; no tungsten-oxidation or enzyme mechanism demonstrated. Methods19.0% Fe oxides and Table1 22.6 wt%Fe disagree; no pure-scheelite yield accepted. The carbide-like cell deposits were examined after30 days oxic dehydration; pure WC, in-vivo stoichiometry and useful product recovery remain unestablished.

### Actual working changes, author attribution and gate scope

provenance: supported. Targets: cmmmech:scheelite.

New record and actual CREATE sidecar target match; reviewed bytes match initial inspect and the batch gate. No older history/review was rewritten. Saving this review neither alters the record nor adds a curation event.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/scheelite.yaml; All target fields and linked CREATE sidecar; target inspected before assessment at09:30:05Z; final context inspection confirms same scientific bytes | supports | New uncommitted record and matching CREATE event under trusted merged base. Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar are distinct. Reviewer authored no mineral records or histories. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF page194, Scheelite row; pages1–2 definitions and reuse terms | supports | IMA September 2026 Ca(WO4), grandfathered G, original-description year 1821. Species distinct from W element, wolframite and impure concentrate; no inherited criticality. Independently read retained official PDF text and date/status definitions. |
| paper | https://doi.org/10.3389/fmicb.2019.01492; Materials and Methods; Results and Discussion; Table 1, Figures 1 and 3; Fig3 pixels on PDF page6 and Table1 pixels on page5 | supports | Living DSM5348 cultures at 73 C, initial pH2 with CO2 and 10 g/L sterilized, impure 1-mm scheelite concentrate show greater filter-passing W than uninoculated same-feed controls. ICP-OES of centrifuged 0.44-micrometre filtrate over21 days is not an isolated-product yield. Figure3 n=3/SD and abiotic release are visible. No exact W value is transferred from the log10/mg/L and day/hour ambiguity. Independently inspected retained original evidence at /private/tmp/cmm-round14-mineral-raw/scheelite.pdf. |
| search | /private/tmp/cmm-round14-mineral-review/web-search-transcript.json; Exact queries, observed first result windows and hidden/ignored-inclusive dedup.txt | context_only | No applicable correction/retraction notice surfaced in the returned windows; that bounded result is not a global absence claim. Existing elemental experiments and dossiers are recognized as shared evidence. Nearby additional studies are extension leads rather than evidence for broader claims in this record. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Root actual terminal-zero receipt plus check, require and history logs; named reviewer6/0 and history134/0 | supports | Reviewer read root logs:307 passed,3 skipped in80.06s;119 records;134 histories. This batch gate precedes an unrelated pending FCC wording correction; all six mineral hashes remain unchanged. Reviewer independently executed named validation and history. Offline validation is not scientific proof. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=43687; Retained NCBI XML or browser HTML: TaxId, ScientificName, Rank, relevant type material | supports | 43687 resolves to Metallosphaera sedula, rankspecies; paper-specific strain assignment is not strengthened beyond authority support. |

## Limits And Additional Notes

- The energy source and Fe/Mn oxidation contribution are unresolved; no tungsten-oxidation or enzyme mechanism demonstrated.
- Methods19.0% Fe oxides and Table1 22.6 wt%Fe disagree; no pure-scheelite yield accepted.
- The carbide-like cell deposits were examined after30 days oxic dehydration; pure WC, in-vivo stoichiometry and useful product recovery remain unestablished.
- Fresh DOI reader routes for Blazevic, Topolska, Kang and Sklute failed or returned access errors in this review. Independently read legitimate retained original PDFs/XML and rendered relevant original figures/tables instead; raw hashes and source acquisition provenance are retained. This is not a claim of fresh successful download of every source.
- Laboratory observations do not establish industrial deployment; bounded correction/conflict search is not exhaustive.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093608Z-scheelite-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Scheelite
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
  - path: data/records/scheelite.yaml
    sha256: a8fd85cedb9100cb6a3b1ec8e5bafe5be2d5a4fe1ea740abf33acee44a1c7425
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/scheelite/2026-10-11T092653Z-codex-43e8e4.yaml
    sha256: 7716d4bc457c2917b69845f17dc32c06ab4318560d1e67cb14011fc9ac68524d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, cited evidence and linked CREATE provenance of one exact
    new uncommitted mineral record.
  selection: Assigned six-mineral cohort; this per-record observation covers only
    cmmmech:scheelite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:scheelite
  exclusions:
  - target: Uncurated literature and unrelated records
    reason: Context and contradiction searches are bounded; no corpus-wide scientific
      recertification.
targets:
- target_id: cmmmech:scheelite
  path: data/records/scheelite.yaml
  label: Scheelite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scheelite.yaml
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
  - cmmmech:scheelite
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
  - cmmmech:scheelite
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
  - cmmmech:scheelite
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
  - cmmmech:scheelite
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
  - cmmmech:scheelite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/scheelite.yaml
  locator: All target fields and linked CREATE sidecar; target inspected before assessment
    at09:30:05Z; final context inspection confirms same scientific bytes
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: New uncommitted record and matching CREATE event under trusted merged base.
    Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar
    are distinct. Reviewer authored no mineral records or histories.
  snapshot_sha256: a8fd85cedb9100cb6a3b1ec8e5bafe5be2d5a4fe1ea740abf33acee44a1c7425
- evidence_id: ima
  kind: primary_source
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF page194, Scheelite row; pages1–2 definitions and reuse terms
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: IMA September 2026 Ca(WO4), grandfathered G, original-description year
    1821. Species distinct from W element, wolframite and impure concentrate; no inherited
    criticality. Independently read retained official PDF text and date/status definitions.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2019.01492
  locator: Materials and Methods; Results and Discussion; Table 1, Figures 1 and 3;
    Fig3 pixels on PDF page6 and Table1 pixels on page5
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: Living DSM5348 cultures at 73 C, initial pH2 with CO2 and 10 g/L sterilized,
    impure 1-mm scheelite concentrate show greater filter-passing W than uninoculated
    same-feed controls. ICP-OES of centrifuged 0.44-micrometre filtrate over21 days
    is not an isolated-product yield. Figure3 n=3/SD and abiotic release are visible.
    No exact W value is transferred from the log10/mg/L and day/hour ambiguity. Independently
    inspected retained original evidence at /private/tmp/cmm-round14-mineral-raw/scheelite.pdf.
  snapshot_sha256: e493f15bf233713838fc9728c59587cc79abd59442b211001330c67ccfe4d8a4
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
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=43687
  locator: 'Retained NCBI XML or browser HTML: TaxId, ScientificName, Rank, relevant
    type material'
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: 43687 resolves to Metallosphaera sedula, rankspecies; paper-specific strain
    assignment is not strengthened beyond authority support.
  snapshot_sha256: 134cef049bb3640b8c986f089500c3a2d47c0146d133b1f190c8bc9bde19dc53
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, taxonomy, criticality and experimental material distinction
  outcome: supported
  summary: IMA September 2026 Ca(WO4), grandfathered G, original-description year
    1821. Species distinct from W element, wolframite and impure concentrate; no inherited
    criticality.
  target_ids:
  - cmmmech:scheelite
  evidence_ids:
  - ima
  - taxonomy
  - record
  - search
  dimensions:
  - name: material_form
    value: IMA September 2026 Ca(WO4), grandfathered G, original-description year
      1821. Species distinct from W element, wolframite and impure concentrate; no
      inherited criticality.
    definition: Exact species versus measured substrate/product boundary.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: biomass
    value: Living Metallosphaera sedula DSM5348; NCBITaxon43687 is species-level
    definition: Biomass state and taxonomic scope of accepted mechanism.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: conditions
    value: DSMZ88 initial pH2;73 C;CO2;10 g/L impure concentrate;180 C at least24
      h then121 C20 min;21-day culture
    definition: Reported assay conditions, not universal process conditions.
    evidence_ids:
    - record
    - paper
    - taxonomy
  - name: controls_outcome
    value: Uninoculated sterilized same-feed medium; n=3 biological replicates/SD;
      operational filtrate W, not extraction fraction
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
  summary: Living DSM5348 cultures at 73 C, initial pH2 with CO2 and 10 g/L sterilized,
    impure 1-mm scheelite concentrate show greater filter-passing W than uninoculated
    same-feed controls. ICP-OES of centrifuged 0.44-micrometre filtrate over21 days
    is not an isolated-product yield. Figure3 n=3/SD and abiotic release are visible.
    No exact W value is transferred from the log10/mg/L and day/hour ambiguity.
  details: The energy source and Fe/Mn oxidation contribution are unresolved; no tungsten-oxidation
    or enzyme mechanism demonstrated. Methods19.0% Fe oxides and Table1 22.6 wt%Fe
    disagree; no pure-scheelite yield accepted. The carbide-like cell deposits were
    examined after30 days oxic dehydration; pure WC, in-vivo stoichiometry and useful
    product recovery remain unestablished.
  target_ids:
  - cmmmech:scheelite
  evidence_ids:
  - paper
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
  - cmmmech:scheelite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- The energy source and Fe/Mn oxidation contribution are unresolved; no tungsten-oxidation
  or enzyme mechanism demonstrated.
- Methods19.0% Fe oxides and Table1 22.6 wt%Fe disagree; no pure-scheelite yield accepted.
- The carbide-like cell deposits were examined after30 days oxic dehydration; pure
  WC, in-vivo stoichiometry and useful product recovery remain unestablished.
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
