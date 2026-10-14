# Independent scientific review of Böhmite

- Review: 20261014T113920Z-boehmite-round70-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T11:28:21.923285Z
- Finished UTC: 2026-10-14T11:39:20.837528Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Distinct AlO(OH) mineral identity and an explicitly abiotic alkoxide-hydrolysis formation route are supported. Six processing recipes, five displayed diffraction fits, phase-purity limits and fitted domain sizes are correctly separated; microbial activity and recovery yield are not asserted.

## Scope And Provenance

Entire final mineral record, canonical history, authority identity and primary abiotic mechanism evidence.

Selection: Assigned new owner; native inspect before final assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:boehmite | data/records/boehmite.yaml | maintained | Böhmite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:boehmite | Reviewer executed named validation in round70 worktree; tool session98765 exited0, Checked1record;0failed. |
| Completed batch gate | passed | True | cmmmech:boehmite | Root execution 2026-10-14T11:33:43.296738+00:00 to 2026-10-14T11:37:15.611892+00:00; retained log hash verified. |
| Completed batch gate | passed | True | cmmmech:boehmite | Root execution 2026-10-14T11:37:15.611913+00:00 to 2026-10-14T11:37:23.980116+00:00; retained log hash verified. |
| Completed batch gate | passed | True | cmmmech:boehmite | Root execution 2026-10-14T11:37:23.980141+00:00 to 2026-10-14T11:37:29.732952+00:00; retained log hash verified. |

## Scientific And Domain Assessments

### Mineral identity and criticality

identity: supported. Targets: cmmmech:boehmite.

Böhmite is distinct from diaspore, Al(OH)3 polymorphs, bauxite, aluminium and alumina. No criticality designation or invented identifier.

### Abiotic synthesis, experimental conditions and fitted outcomes

evidence: supported. Targets: cmmmech:boehmite.

Record accurately represents chemical synthesis with no organism or biomass. Recipe differences and five-versus-six pattern availability remain explicit.

### Exact bytes and immutable history

provenance: supported. Targets: cmmmech:boehmite.

Native inspect precedes final judgment; record and sidecar hashes still match. Named and completed batch gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/boehmite.yaml; Entire inspected final record | supports | Distinct AlO(OH) mineral identity and an explicitly abiotic alkoxide-hydrolysis formation route are supported. Six processing recipes, five displayed diffraction fits, phase-purity limits and fitted domain sizes are correctly separated; microbial activity and recovery yield are not asserted. |
| history | history/records/boehmite/2026-10-14T112702Z-codex-e9dfd5.yaml; Entire canonical CREATE sidecar and distinct inline curation event | supports | Actual actor/model, target, dates and performed work match; no invented prior authorship. Trusted-base append-only validation passed. |
| batch | /private/tmp/cmm-round70-final-gates.json; Completed commands and retained log hash | supports | Root verified successful just check, nonempty corpus validation and trusted-base history before saving. |
| primary | https://doi.org/10.5562/cca1884; Complete pp481–485; Experimental, Tables1–2 and Figures1–4 | supports | Complete original text independently read; page482 tables/IR, page483 microscopy and page484 diffraction visually inspected. The six recipes differ in acid/base composition, temperature, duration and filtration. All-six phase assignment is author-reported; only five diffraction fits are displayed. |
| limits | https://doi.org/10.5562/cca1884; Table1, Table2, Figure1, Figure4 and Results/Discussion | partial | Acetate/water bands and unquantified amorphous material limit purity; B5 fit is absent. Size/strain values are fitted coherent domains, not particle/aggregate sizes or yields. Confounded processing recipes do not isolate a pH effect. Source supplies no independent synthesis replication or final washing/drying/recovery mass balance. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Pages1–2 status/number definitions; Böhmite row PDFp28 | supports | Previously acquired official list independently read, row image visually checked. Accepted Böhmite AlO(OH), G1927; year of original description does not become an approval accession. |
| handbook | https://www.handbookofmineralogy.org/pdfs/bohmite.pdf; Complete one-page entry, version1 2001–2005 | supports | Independent full text and image check supports orthorhombic identity and diaspore dimorphism; natural mixed-bauxite occurrence does not identify elemental Al or the alumina commodity. |
| search | https://hrcak.srce.hr/en/75056; Independent web search14Oct2026 | context_only | DOI/title correction queries returned the original journal, institutional repository and bibliographic/citing records. No affecting notice surfaced in these inspected first result sets; this is not exhaustive notice absence. |
| dedup | /private/tmp/cmm-round70-boehmite-dedup.txt; Scoped repository rg result and curator raw-boundary receipts | context_only | Contextual bauxite/aluminium mentions are distinct from this species owner. Hidden/ignored-inclusive source and history searches do not establish machine-wide absence. |

## Limits And Additional Notes

- No microbial mechanism is supported by this chemical synthesis study.
- B5 has no displayed diffraction fit, and amorphous fraction and chemical purity are not quantified.
- Independent synthesis replication, final solid handling and gravimetric recovery are unspecified; confounded recipes do not isolate one processing variable.
- Correction/contradiction searches are bounded; no independent synthesis or raw diffraction refit was performed.
- No supported corrective defect found in this frozen state. Source limitations remain explicit.
- Initial saver rejected target kind record; corrected review metadata to maintained and re-inspected identical record/history hashes. No scientific owner or history changed.
- Raw originals remain outside Git. Whole-batch structured checking and exact coverage follow saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T113920Z-boehmite-round70-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Böhmite
started_at: '2026-10-14T11:28:21.923285Z'
finished_at: '2026-10-14T11:39:20.837528Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record and CREATE sidecar authored by /root/round68_iron_sulfides.
    Root independently inspected source text, claim-bearing original graphics and
    authorities; root did not edit the scientific record or history. Source downloads
    are shared. Root authors publication documents and helpers.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Distinct AlO(OH) mineral identity and an explicitly abiotic alkoxide-hydrolysis
  formation route are supported. Six processing recipes, five displayed diffraction
  fits, phase-purity limits and fitted domain sizes are correctly separated; microbial
  activity and recovery yield are not asserted.
source:
  git_revision: 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7
  state: working_tree
  inputs:
  - path: data/records/boehmite.yaml
    sha256: e31bc47bd90bd013882ab16837dd2850321b2549b89dafd0549a8e09d030d876
    role: target
  - path: history/records/boehmite/2026-10-14T112702Z-codex-e9dfd5.yaml
    sha256: 91fe7ffac1dd20a0c20e220bdcf51002d78032dd018d565c73a206deb37aee81
    role: context
scope:
  description: Entire final mineral record, canonical history, authority identity
    and primary abiotic mechanism evidence.
  selection: Assigned new owner; native inspect before final assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:boehmite
targets:
- target_id: cmmmech:boehmite
  path: data/records/boehmite.yaml
  label: Böhmite
  kind: maintained
  ownership_note: Maintained record YAML and its canonical history sidecar own this
    scientific state.
checks:
- check_id: named
  name: Reviewer named validation
  command: uv run --locked cmmmech validate data/records/boehmite.yaml
  status: passed
  required: true
  summary: Reviewer executed named validation in round70 worktree; tool session98765
    exited0, Checked1record;0failed.
  target_ids:
  - cmmmech:boehmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - record
- check_id: batch_0
  name: Completed batch gate
  command: just check
  status: passed
  required: true
  summary: Root execution 2026-10-14T11:33:43.296738+00:00 to 2026-10-14T11:37:15.611892+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:boehmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Completed batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Root execution 2026-10-14T11:37:15.611913+00:00 to 2026-10-14T11:37:23.980116+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:boehmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Completed batch gate
  command: uv run --locked cmmmech validate-history --base 1d40bb5d7496a02b937acc1f6ef3aec5af5d32e7
  status: passed
  required: true
  summary: Root execution 2026-10-14T11:37:23.980141+00:00 to 2026-10-14T11:37:29.732952+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:boehmite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/boehmite.yaml
  locator: Entire inspected final record
  accessed_at: '2026-10-14T11:39:20.837528Z'
  support: supports
  summary: Distinct AlO(OH) mineral identity and an explicitly abiotic alkoxide-hydrolysis
    formation route are supported. Six processing recipes, five displayed diffraction
    fits, phase-purity limits and fitted domain sizes are correctly separated; microbial
    activity and recovery yield are not asserted.
  snapshot_sha256: e31bc47bd90bd013882ab16837dd2850321b2549b89dafd0549a8e09d030d876
- evidence_id: history
  kind: record_content
  reference: history/records/boehmite/2026-10-14T112702Z-codex-e9dfd5.yaml
  locator: Entire canonical CREATE sidecar and distinct inline curation event
  accessed_at: '2026-10-14T11:39:20.837528Z'
  support: supports
  summary: Actual actor/model, target, dates and performed work match; no invented
    prior authorship. Trusted-base append-only validation passed.
  snapshot_sha256: 91fe7ffac1dd20a0c20e220bdcf51002d78032dd018d565c73a206deb37aee81
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round70-final-gates.json
  locator: Completed commands and retained log hash
  accessed_at: '2026-10-14T11:39:20.837528Z'
  support: supports
  summary: Root verified successful just check, nonempty corpus validation and trusted-base
    history before saving.
  snapshot_sha256: 901e0e7e3ecaf5f364fa05b6c1f5dfcfb231dca506ef61e77988b19f9ee39cfb
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.5562/cca1884
  locator: Complete pp481–485; Experimental, Tables1–2 and Figures1–4
  support: supports
  summary: Complete original text independently read; page482 tables/IR, page483 microscopy
    and page484 diffraction visually inspected. The six recipes differ in acid/base
    composition, temperature, duration and filtration. All-six phase assignment is
    author-reported; only five diffraction fits are displayed.
  accessed_at: '2026-10-14T11:39:20.837528Z'
  snapshot_sha256: bf4e559a916713cc1c1c38bbf6ba4e0799caa68c1fbbe32e2178a813341348fe
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.5562/cca1884
  locator: Table1, Table2, Figure1, Figure4 and Results/Discussion
  support: partial
  summary: Acetate/water bands and unquantified amorphous material limit purity; B5
    fit is absent. Size/strain values are fitted coherent domains, not particle/aggregate
    sizes or yields. Confounded processing recipes do not isolate a pH effect. Source
    supplies no independent synthesis replication or final washing/drying/recovery
    mass balance.
  accessed_at: '2026-10-14T11:39:20.837528Z'
  snapshot_sha256: bf4e559a916713cc1c1c38bbf6ba4e0799caa68c1fbbe32e2178a813341348fe
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Pages1–2 status/number definitions; Böhmite row PDFp28
  support: supports
  summary: Previously acquired official list independently read, row image visually
    checked. Accepted Böhmite AlO(OH), G1927; year of original description does not
    become an approval accession.
  accessed_at: '2026-10-14T11:39:20.837528Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/bohmite.pdf
  locator: Complete one-page entry, version1 2001–2005
  support: supports
  summary: Independent full text and image check supports orthorhombic identity and
    diaspore dimorphism; natural mixed-bauxite occurrence does not identify elemental
    Al or the alumina commodity.
  accessed_at: '2026-10-14T11:39:20.837528Z'
  snapshot_sha256: a9cf9bcba5c6085e929f4faaae62a350052d27c52f2753a7286d6c235e06ad45
- evidence_id: search
  kind: search
  reference: https://hrcak.srce.hr/en/75056
  locator: Independent web search14Oct2026
  support: context_only
  summary: DOI/title correction queries returned the original journal, institutional
    repository and bibliographic/citing records. No affecting notice surfaced in these
    inspected first result sets; this is not exhaustive notice absence.
  search_scope: 'Queries: "10.5562/cca1884" correction erratum retraction; "Microstructural
    Analysis of Boehmite Nanoparticles Prepared by Rapid" correction. No domain/date
    filters or pagination. Web PDF open failed, but complete independently inspected
    local original was available.'
  accessed_at: '2026-10-14T11:39:20.837528Z'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round70-boehmite-dedup.txt
  locator: Scoped repository rg result and curator raw-boundary receipts
  support: context_only
  summary: Contextual bauxite/aluminium mentions are distinct from this species owner.
    Hidden/ignored-inclusive source and history searches do not establish machine-wide
    absence.
  search_scope: rg --hidden --no-ignore --follow -l -i boehmite|böhmite|cca1884 data/records
    research reviews history; curator referenced-raw boundary retained under round70-aluminium-research.
  accessed_at: '2026-10-14T11:39:20.837528Z'
  snapshot_sha256: 621ae81e05de508de21b14d3e5625230d7c271bb6348aa9b1ab39e0c6b13c240
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity and criticality
  outcome: supported
  summary: Böhmite is distinct from diaspore, Al(OH)3 polymorphs, bauxite, aluminium
    and alumina. No criticality designation or invented identifier.
  evidence_ids:
  - record
  - ima
  - handbook
  - dedup
  dimensions:
  - name: criticality
    value: No authority/jurisdiction/list/edition claim asserted
    definition: Omission does not establish global noncriticality.
    evidence_ids:
    - record
  target_ids:
  - cmmmech:boehmite
- assessment_id: mechanism
  area: evidence
  topic: Abiotic synthesis, experimental conditions and fitted outcomes
  outcome: supported
  summary: Record accurately represents chemical synthesis with no organism or biomass.
    Recipe differences and five-versus-six pattern availability remain explicit.
  evidence_ids:
  - record
  - primary
  - limits
  dimensions:
  - name: biomass_state
    value: None; microbial false
    definition: No microorganism, biomass or biogenic reagent in accepted mechanism.
    evidence_ids:
    - primary
  - name: substrate
    value: Analytical-grade aluminium sec-butoxide in six distinct recipes
    definition: Laboratory chemical precursor, not a natural bauxite feed.
    evidence_ids:
    - primary
  - name: outcome
    value: Source-assigned nanocrystalline boehmite, fitted coherent-domain dimensions
    definition: No phase-pure mass yield, complete precursor conversion or industrial
      deployment inferred.
    evidence_ids:
    - primary
    - limits
  target_ids:
  - cmmmech:boehmite
- assessment_id: provenance
  area: provenance
  topic: Exact bytes and immutable history
  outcome: supported
  summary: Native inspect precedes final judgment; record and sidecar hashes still
    match. Named and completed batch gates passed.
  target_ids:
  - cmmmech:boehmite
  evidence_ids:
  - record
  - history
  - batch
findings: []
actions: []
limitations:
- No microbial mechanism is supported by this chemical synthesis study.
- B5 has no displayed diffraction fit, and amorphous fraction and chemical purity
  are not quantified.
- Independent synthesis replication, final solid handling and gravimetric recovery
  are unspecified; confounded recipes do not isolate one processing variable.
- Correction/contradiction searches are bounded; no independent synthesis or raw diffraction
  refit was performed.
notes:
- No supported corrective defect found in this frozen state. Source limitations remain
  explicit.
- Initial saver rejected target kind record; corrected review metadata to maintained
  and re-inspected identical record/history hashes. No scientific owner or history
  changed.
- Raw originals remain outside Git. Whole-batch structured checking and exact coverage
  follow saving.
tags:
- round70
- independent
- boehmite
- primary-figures
```
