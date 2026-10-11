# Independent scientific review of Pyrolusite

- Review: 20261011T093608Z-pyrolusite-round14-independent
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

Selection: Assigned six-mineral cohort; this per-record observation covers only cmmmech:pyrolusite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pyrolusite | data/records/pyrolusite.yaml | maintained | Pyrolusite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named mineral validation | passed | True | cmmmech:pyrolusite | Reviewer session60838 terminal0;6 records,0failed; /private/tmp/cmm-round14-mineral-review/named-validation.log |
| Reviewer trusted-base history validation | passed | True | cmmmech:pyrolusite | Reviewer session63319 terminal0;134 histories,0errors; /private/tmp/cmm-round14-mineral-review/history-validation.log |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:pyrolusite | Root executed; reviewer read actual logs. Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |
| Required corpus | passed | True | cmmmech:pyrolusite | Root executed; reviewer read actual logs. Terminal0 session1358:119records,0failed. /private/tmp/cmm-round14-require.log |
| Trusted-base history | passed | True | cmmmech:pyrolusite | Root executed; reviewer read actual logs. Terminal0 session1358:134histories,0errors. /private/tmp/cmm-round14-history.log |

## Scientific And Domain Assessments

### Species identity, taxonomy, criticality and experimental material distinction

identity: supported. Targets: cmmmech:pyrolusite.

IMA September 2026 MnO2,statusA,1982s.p.; the special-procedure date is not a sequential approval identifier. Characterized beta-MnO2 differs from uncharacterized ore and manganese element; no inherited criticality.

### Primary methods, controls, quantities and inference boundaries

evidence: supported. Targets: cmmmech:pyrolusite.

The accepted mechanism is explicitly microbial:false. Commercial beta-MnO2 reacts with aqueousFeII in anoxic pH7.5 buffer, producing filter-passing Mn and Fe-rich surface solids. Figure2 confirms2.4 mM initialFeII and about0.6 mM Mn at75 min, while Fe-free controls stay near zero. The total-Mn colorimetric assay does not directly identify aqueous oxidation state. Later magnetite/maghemite grouping is correctly retained.

No temperature or replicate count was found in the inspected experiment methods; none is invented. Co/Cu radiation label conflict prevents precise angle transcription. SolutionMn below simple twoFe:oneMn prediction leaves sorption/incorporation/reoxidation unresolved; no isolatedMn product yield. KL3 study uses sulfur/iron-rich unverified Kliripan ore, a no-mineral C arm, conflicting pH and nonclosing Table1; it remains context_only and cannot establish phase-specific microbial causality.

### Actual working changes, author attribution and gate scope

provenance: supported. Targets: cmmmech:pyrolusite.

New record and actual CREATE sidecar target match; reviewed bytes match initial inspect and the batch gate. No older history/review was rewritten. Saving this review neither alters the record nor adds a curation event.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/pyrolusite.yaml; All target fields and linked CREATE sidecar; target inspected before assessment at09:30:05Z; final context inspection confirms same scientific bytes | supports | New uncommitted record and matching CREATE event under trusted merged base. Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar are distinct. Reviewer authored no mineral records or histories. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF page179, Pyrolusite row; pages1–2 definitions and reuse terms | supports | IMA September 2026 MnO2,statusA,1982s.p.; the special-procedure date is not a sequential approval identifier. Characterized beta-MnO2 differs from uncharacterized ore and manganese element; no inherited criticality. Independently read retained official PDF text and date/status definitions. |
| paper | https://doi.org/10.1186/s12932-017-0045-0; Experimental; Figures1–3; first Results and secondary Fe-oxide discussion; Figure2 kinetic plot visually inspected | supports | The accepted mechanism is explicitly microbial:false. Commercial beta-MnO2 reacts with aqueousFeII in anoxic pH7.5 buffer, producing filter-passing Mn and Fe-rich surface solids. Figure2 confirms2.4 mM initialFeII and about0.6 mM Mn at75 min, while Fe-free controls stay near zero. The total-Mn colorimetric assay does not directly identify aqueous oxidation state. Later magnetite/maghemite grouping is correctly retained. Independently inspected retained original evidence at /private/tmp/cmm-round14-mineral-raw/pyrolusite-abiotic.pdf. |
| search | /private/tmp/cmm-round14-mineral-review/web-search-transcript.json; Exact queries, observed first result windows and hidden/ignored-inclusive dedup.txt | context_only | No applicable correction/retraction notice surfaced in the returned windows; that bounded result is not a global absence claim. Existing elemental experiments and dossiers are recognized as shared evidence. Nearby additional studies are extension leads rather than evidence for broader claims in this record. |
| gates | /private/tmp/cmm-round14-gate-receipts-initial.json; Root actual terminal-zero receipt plus check, require and history logs; named reviewer6/0 and history134/0 | supports | Reviewer read root logs:307 passed,3 skipped in80.06s;119 records;134 histories. This batch gate precedes an unrelated pending FCC wording correction; all six mineral hashes remain unchanged. Reviewer independently executed named validation and history. Offline validation is not scientific proof. |
| context-study | https://doi.org/10.22146/ijc.38898; Original PDF Experimental pp2–3, Figure2 p4 and Table1 p6; figure/table pixels independently inspected | context_only | Mixed feed, no phase diffraction, no-mineral C, pH6 methods vs2 caption, duplicate0.03 loading, atomic/mass label conflict and day16 sum193.03 all make microbial phase-specific causal claims unsafe. Record correctly declines those claims and does not make KL3 a control for Schaefer. |

## Limits And Additional Notes

- No temperature or replicate count was found in the inspected experiment methods; none is invented. Co/Cu radiation label conflict prevents precise angle transcription.
- SolutionMn below simple twoFe:oneMn prediction leaves sorption/incorporation/reoxidation unresolved; no isolatedMn product yield.
- KL3 study uses sulfur/iron-rich unverified Kliripan ore, a no-mineral C arm, conflicting pH and nonclosing Table1; it remains context_only and cannot establish phase-specific microbial causality.
- Fresh DOI reader routes for Blazevic, Topolska, Kang and Sklute failed or returned access errors in this review. Independently read legitimate retained original PDFs/XML and rendered relevant original figures/tables instead; raw hashes and source acquisition provenance are retained. This is not a claim of fresh successful download of every source.
- Laboratory observations do not establish industrial deployment; bounded correction/conflict search is not exhaustive.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093608Z-pyrolusite-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Pyrolusite
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
  - path: data/records/pyrolusite.yaml
    sha256: 47ce73b2f3c987208bee82bbd91109870d1866a90fbc580172f1907269f44831
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/pyrolusite/2026-10-11T092706Z-codex-4fdff9.yaml
    sha256: d5fd4f0f47a95c3aa4b22aebc6e3d8cee63df2be27bae962d99e42f8878cb175
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All fields, cited evidence and linked CREATE provenance of one exact
    new uncommitted mineral record.
  selection: Assigned six-mineral cohort; this per-record observation covers only
    cmmmech:pyrolusite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pyrolusite
  exclusions:
  - target: Uncurated literature and unrelated records
    reason: Context and contradiction searches are bounded; no corpus-wide scientific
      recertification.
targets:
- target_id: cmmmech:pyrolusite
  path: data/records/pyrolusite.yaml
  label: Pyrolusite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pyrolusite.yaml
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
  - cmmmech:pyrolusite
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
  - cmmmech:pyrolusite
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
  - cmmmech:pyrolusite
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
  - cmmmech:pyrolusite
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
  - cmmmech:pyrolusite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/pyrolusite.yaml
  locator: All target fields and linked CREATE sidecar; target inspected before assessment
    at09:30:05Z; final context inspection confirms same scientific bytes
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: New uncommitted record and matching CREATE event under trusted merged base.
    Actual GPT-6/codex attribution and issue56 linkage; inline and canonical sidecar
    are distinct. Reviewer authored no mineral records or histories.
  snapshot_sha256: 47ce73b2f3c987208bee82bbd91109870d1866a90fbc580172f1907269f44831
- evidence_id: ima
  kind: primary_source
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF page179, Pyrolusite row; pages1–2 definitions and reuse terms
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: IMA September 2026 MnO2,statusA,1982s.p.; the special-procedure date is
    not a sequential approval identifier. Characterized beta-MnO2 differs from uncharacterized
    ore and manganese element; no inherited criticality. Independently read retained
    official PDF text and date/status definitions.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.1186/s12932-017-0045-0
  locator: Experimental; Figures1–3; first Results and secondary Fe-oxide discussion;
    Figure2 kinetic plot visually inspected
  accessed_at: '2026-10-11T09:36:08Z'
  support: supports
  summary: The accepted mechanism is explicitly microbial:false. Commercial beta-MnO2
    reacts with aqueousFeII in anoxic pH7.5 buffer, producing filter-passing Mn and
    Fe-rich surface solids. Figure2 confirms2.4 mM initialFeII and about0.6 mM Mn
    at75 min, while Fe-free controls stay near zero. The total-Mn colorimetric assay
    does not directly identify aqueous oxidation state. Later magnetite/maghemite
    grouping is correctly retained. Independently inspected retained original evidence
    at /private/tmp/cmm-round14-mineral-raw/pyrolusite-abiotic.pdf.
  snapshot_sha256: d89993b072ec7eef6060bcb1fa7ecbf62b6ca4928ad3446804c0d80176e569ec
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
- evidence_id: context-study
  kind: primary_source
  reference: https://doi.org/10.22146/ijc.38898
  locator: Original PDF Experimental pp2–3, Figure2 p4 and Table1 p6; figure/table
    pixels independently inspected
  accessed_at: '2026-10-11T09:36:08Z'
  support: context_only
  summary: Mixed feed, no phase diffraction, no-mineral C, pH6 methods vs2 caption,
    duplicate0.03 loading, atomic/mass label conflict and day16 sum193.03 all make
    microbial phase-specific causal claims unsafe. Record correctly declines those
    claims and does not make KL3 a control for Schaefer.
  snapshot_sha256: 6fe563e92ece898d92d06e477c36bc9fbe68ef2a0a4edc018bf9cdd0b1f7743d
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, taxonomy, criticality and experimental material distinction
  outcome: supported
  summary: IMA September 2026 MnO2,statusA,1982s.p.; the special-procedure date is
    not a sequential approval identifier. Characterized beta-MnO2 differs from uncharacterized
    ore and manganese element; no inherited criticality.
  target_ids:
  - cmmmech:pyrolusite
  evidence_ids:
  - ima
  - record
  - search
  dimensions:
  - name: material_form
    value: IMA September 2026 MnO2,statusA,1982s.p.; the special-procedure date is
      not a sequential approval identifier. Characterized beta-MnO2 differs from uncharacterized
      ore and manganese element; no inherited criticality.
    definition: Exact species versus measured substrate/product boundary.
    evidence_ids:
    - record
    - paper
  - name: biomass
    value: None in accepted Schaefer assay; no organism identifiers assigned to abiotic
      mechanism
    definition: Biomass state and taxonomic scope of accepted mechanism.
    evidence_ids:
    - record
    - paper
  - name: conditions
    value: 18 mg/18 mL;25 mM HEPES+25 mM KBr;pH7.5;95%N2/5%H2,<1 ppmv O2;dark rotating
      assays;about90 min typical and75 min plotted
    definition: Reported assay conditions, not universal process conditions.
    evidence_ids:
    - record
    - paper
  - name: controls_outcome
    value: Fe-free resuspension comparisons;0.2-micrometre nylon filtration; Fe photometry
      and totalMn formaldoxime; no product yield
    definition: Control contrast, measurement definition and inference limits.
    evidence_ids:
    - record
    - paper
  - name: criticality
    value: No criticality claims asserted
    definition: No constituent-element status transferred to species; no absent jurisdiction/list/edition
      invented.
    evidence_ids:
    - record
    - paper
- assessment_id: science
  area: evidence
  topic: Primary methods, controls, quantities and inference boundaries
  outcome: supported
  summary: The accepted mechanism is explicitly microbial:false. Commercial beta-MnO2
    reacts with aqueousFeII in anoxic pH7.5 buffer, producing filter-passing Mn and
    Fe-rich surface solids. Figure2 confirms2.4 mM initialFeII and about0.6 mM Mn
    at75 min, while Fe-free controls stay near zero. The total-Mn colorimetric assay
    does not directly identify aqueous oxidation state. Later magnetite/maghemite
    grouping is correctly retained.
  details: No temperature or replicate count was found in the inspected experiment
    methods; none is invented. Co/Cu radiation label conflict prevents precise angle
    transcription. SolutionMn below simple twoFe:oneMn prediction leaves sorption/incorporation/reoxidation
    unresolved; no isolatedMn product yield. KL3 study uses sulfur/iron-rich unverified
    Kliripan ore, a no-mineral C arm, conflicting pH and nonclosing Table1; it remains
    context_only and cannot establish phase-specific microbial causality.
  target_ids:
  - cmmmech:pyrolusite
  evidence_ids:
  - paper
  - context-study
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
  - cmmmech:pyrolusite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- No temperature or replicate count was found in the inspected experiment methods;
  none is invented. Co/Cu radiation label conflict prevents precise angle transcription.
- SolutionMn below simple twoFe:oneMn prediction leaves sorption/incorporation/reoxidation
  unresolved; no isolatedMn product yield.
- KL3 study uses sulfur/iron-rich unverified Kliripan ore, a no-mineral C arm, conflicting
  pH and nonclosing Table1; it remains context_only and cannot establish phase-specific
  microbial causality.
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
