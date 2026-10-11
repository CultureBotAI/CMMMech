# Independent scientific review of Boron

- Review: 20261011T073230Z-boron-round10-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:27:04Z
- Finished UTC: 2026-10-11T07:32:30Z
- Reviewer: codex /root/cmm10_ti_zr (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact boron record is defensible as a qualified culture-associated B-bearing solid observation. It does not promote SEM-EDS association into proven biological mineralization, a named mineral, quantitative recovery or industrial treatment. Existing source contradictions are retained; no actionable curation finding was established.

## Scope And Provenance

All maintained record fields and linked provenance checked against primary evidence and authorities; no sampling of record fields. Search and literature-access coverage is explicitly bounded.

Selection: Assigned named record; full field assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:boron | data/records/boron.yaml | maintained | Boron |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:boron | Reviewer executed directly; 2 records, 0 failed; terminal exit 0. Earlier same successful output retained in /private/tmp/cmm-round10-b-f-independent/named-validation.log. |
| Full batch gate | passed | True | cmmmech:boron | Parent executed session 84281; reviewer read /private/tmp/cmm-round10-batch-check.log: 307 passed, 3 skipped in 64.75 s; 61 records and 72 histories valid. Parent separately confirmed terminal exit 0. |
| Nonempty corpus | passed | True | cmmmech:boron | Parent executed session 20894; reviewer read /private/tmp/cmm-round10-batch-validation.log: 61 records, 0 failed. Parent separately confirmed terminal exit 0. |
| Trusted-base history | passed | True | cmmmech:boron | Parent executed session 33751; reviewer read /private/tmp/cmm-round10-batch-history.log: 72 histories, 0 errors. Parent separately confirmed terminal exit 0. |

## Scientific And Domain Assessments

### Element, substrate and organism identity

identity: supported. Targets: cmmmech:boron.

Atomic identity and taxonomic scope are supported; chemical feed and resulting forms are not conflated with the element.

### Dated jurisdiction and list designation

evidence: supported. Targets: cmmmech:boron.

The named authority, jurisdiction, list and edition support the record mapping with the stated qualifiers.

### Organism-specific conditions, controls and measured outcome

evidence: supported. Targets: cmmmech:boron.

The exact boron record is defensible as a qualified culture-associated B-bearing solid observation. It does not promote SEM-EDS association into proven biological mineralization, a named mineral, quantitative recovery or industrial treatment. Existing source contradictions are retained; no actionable curation finding was established.

### Actual CREATE provenance

provenance: supported. Targets: cmmmech:boron.

Distinct inline and sidecar events state actual actor/model/tool and target. Trusted-base history validation passed; no record edits or fabricated prior authorship by reviewer.

### Bounded duplicate and contrary-evidence coverage

completeness: supported. Targets: cmmmech:boron.

Scoped hidden/ignored inventory and primary internal counterevidence were checked. Searches provide bounded coverage, not proof of literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/boron.yaml; All fields, linked CREATE sidecar and both shared dossier files | supports | Reviewed exact pre-assessment working bytes and rechecked all hashes before saving. Inline CREATE event and earlier distinct actual CREATE sidecar identify the target, Codex actor, GPT-6 model and codex tool; no invented predecessor authorship. No record, history or dossier edits by this reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:27560; Released ChEBI entry name, chemical_data formula/charge and structure | supports | Boron atom identity is element B, neutral charge 0. Independently inspected and hashed the curator-acquired authoritative JSON. Live ChEBI page also resolved. |
| organism | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1883&amp;mode=Info; Taxonomy ID 1883, current name and rank | supports | Independent live and retained authority inspection confirms Streptomyces at genus rank. It does not resolve 053 or 128 to a species or strain identifier. |
| criticality | https://eur-lex.europa.eu/eli/reg/2024/1252/oj; Original OJ 3 May 2024; Annex II section 1(g), contrasted with Annex I section 1(c) | supports | Original EU 2024/1252 Annex II lists unqualified boron among critical raw materials; the separate strategic entry is metallurgy-grade boron. The record retains this named jurisdiction, list and edition rather than broadening the strategic designation. Live authority text and retained original HTML independently checked. |
| primary | https://doi.org/10.1016/j.jece.2017.06.044; Author manuscript §§2.1–2.9, 3.1–3.3 and conclusions | supports | Full primary author-manuscript methods/results support culture-associated boron-bearing prepared accretions, with nominal boric-acid doses, living cultures and detailed SEM preparation. Uninoculated boric-acid medium processed identically is not described; culture without boric acid and raw boric acid comparisons do not close that control gap. Manuscript is explicitly distinguished from final typeset version. |
| figures | https://doi.org/10.1016/j.jece.2017.06.044; PDF pp17–27: Figures 1 remainder and caption, 2–9; Tables 1–2 | supports | Independently inspected image pixels: Figure 3 extracellular accretions, Figure 4 selected EDS B/O signals and Table 2 atomic-percent title versus Weight-percent column. Calculated B2O3 composition is not a mineral-phase identification. Figure 1 caption/axis concentration mismatch is real; Table 1 removal percentages are not adopted. Figures 6–7 use raw solid reagent rather than processed sterile medium. Figures 8–9 show unidentified protein bands, not a proven pathway. |
| near-match | https://doi.org/10.1016/j.scitotenv.2026.182050; Publisher retraction notice title and referred DOI | context_only | Search returned a retracted review that cites Moraga, but publisher notice refers to DOI 10.1016/j.scitotenv.2023.164744, not the accepted 2017 primary. This disambiguation prevents a citation-list search match from being mistaken for a retraction of Moraga. No scientific claims from the retracted review were adopted. |
| search | Independent review-session searches and local hidden/ignored inventory; Exact DOI, title, contrary-evidence and identifier searches | context_only | Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23" correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation; "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract". Inspected first returned result sets only. Related reviews, primary citation matches and unrelated DOI/title collisions returned; no matched correction or retraction of the two accepted primary papers was identified. A retracted 2023 boron review is distinct and was not accepted as evidence. This is not an exhaustive registry or citation-network audit. rg --no-ignore --hidden searched data, research, reviews and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching files were inspected/scoped. find of those roots returned no symlinks. Hidden and ignored files were included; this is not a home-directory-wide absence claim. |

## Limits And Additional Notes

- The study lacks a matched processed sterile boric-acid medium control and diffraction-based phase identity; preparation-associated or abiotic deposition is not excluded.
- Nominal dose arithmetic, Figure 1 concentration labels, calibration/dilution description and Table 2 composition units remain contradictory; no quantitative recovery is inferred.
- Strains remain genus-qualified and protein bands unassigned; metabolic necessity, intracellular uptake, isolated product and deployment are unproven.
- Author manuscript was inspected; no separate supplement link was found in the inspected PDF/PMC content, a bounded access observation rather than universal absence.
- Correction/retraction and contrary-evidence searches cover first returned result sets and cited local sources, not exhaustive registries or all possible conflicting studies.
- Reviewed final working-tree bytes on trusted base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2; this is not a committed-source attestation.
- Findings by severity: no confirmed blocker, major, minor or informational curation defect. Corrections in this round: none. Unresolved scientific questions are retained under limitations; they do not invalidate the qualified observation.
- Raw source snapshots remain outside Git at /private/tmp/cmm-round10-b-f-raw. Reviewer inspections, local search receipt and named validation are under /private/tmp/cmm-round10-b-f-independent.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T073230Z-boron-round10-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Boron
started_at: '2026-10-11T07:27:04Z'
finished_at: '2026-10-11T07:32:30Z'
reviewer:
  identity: codex /root/cmm10_ti_zr
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from the B/F curator. Reviewer did not author
    or modify these records, histories or dossiers; independently read primary methods/results,
    figure/table pixels, valid supplement where present, authorities and exact frozen
    source bytes. Parent batch commands are attributed separately from reviewer-executed
    named validation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact boron record is defensible as a qualified culture-associated B-bearing
  solid observation. It does not promote SEM-EDS association into proven biological
  mineralization, a named mineral, quantitative recovery or industrial treatment.
  Existing source contradictions are retained; no actionable curation finding was
  established.
source:
  git_revision: 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  state: working_tree
  inputs:
  - path: data/records/boron.yaml
    sha256: b11782fc3d0f3783af0c4131448cdb38a68063c1fc66df9b956db01fcef8664a
    role: target
  - path: history/records/boron/2026-10-11T072436Z-codex-b9ef43.yaml
    sha256: 165e62dd3006488adf1bb2898c5c6a6edf8b7e28ec9670c69155923f8a492d3c
    role: context
  - path: research/ingests/round10-b-f-20261011.json
    sha256: b3ac680c2c33e9de07324e191a93d25fdee95127caea3b9826fb5ceda01fe87e
    role: context
  - path: research/ingests/round10-b-f-20261011.md
    sha256: cf537d0d736e0b2acded0677f744cf5f1c94b8af27837922938e72390797faa4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All maintained record fields and linked provenance checked against
    primary evidence and authorities; no sampling of record fields. Search and literature-access
    coverage is explicitly bounded.
  selection: Assigned named record; full field assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:boron
targets:
- target_id: cmmmech:boron
  path: data/records/boron.yaml
  label: Boron
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/boron.yaml
    role: maintained
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/boron.yaml data/records/fluorine.yaml
  status: passed
  required: true
  summary: Reviewer executed directly; 2 records, 0 failed; terminal exit 0. Earlier
    same successful output retained in /private/tmp/cmm-round10-b-f-independent/named-validation.log.
  target_ids:
  - cmmmech:boron
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Parent executed session 84281; reviewer read /private/tmp/cmm-round10-batch-check.log:
    307 passed, 3 skipped in 64.75 s; 61 records and 72 histories valid. Parent separately
    confirmed terminal exit 0.'
  target_ids:
  - cmmmech:boron
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Parent executed session 20894; reviewer read /private/tmp/cmm-round10-batch-validation.log:
    61 records, 0 failed. Parent separately confirmed terminal exit 0.'
  target_ids:
  - cmmmech:boron
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  status: passed
  required: true
  summary: 'Parent executed session 33751; reviewer read /private/tmp/cmm-round10-batch-history.log:
    72 histories, 0 errors. Parent separately confirmed terminal exit 0.'
  target_ids:
  - cmmmech:boron
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/boron.yaml
  locator: All fields, linked CREATE sidecar and both shared dossier files
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Reviewed exact pre-assessment working bytes and rechecked all hashes before
    saving. Inline CREATE event and earlier distinct actual CREATE sidecar identify
    the target, Codex actor, GPT-6 model and codex tool; no invented predecessor authorship.
    No record, history or dossier edits by this reviewer.
  snapshot_sha256: b11782fc3d0f3783af0c4131448cdb38a68063c1fc66df9b956db01fcef8664a
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27560
  locator: Released ChEBI entry name, chemical_data formula/charge and structure
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Boron atom identity is element B, neutral charge 0. Independently inspected
    and hashed the curator-acquired authoritative JSON. Live ChEBI page also resolved.
  snapshot_sha256: 8fbf80bf3b0626e5e3be64a90305436cae5fb3f4c6884a68a54d4e7a6cc9605f
- evidence_id: organism
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1883&mode=Info
  locator: Taxonomy ID 1883, current name and rank
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Independent live and retained authority inspection confirms Streptomyces
    at genus rank. It does not resolve 053 or 128 to a species or strain identifier.
  snapshot_sha256: b7e893978ed4042d7684e02b26653a52fc2550b5e4c2ad63ffa0cd0d5802e337
- evidence_id: criticality
  kind: authority
  reference: https://eur-lex.europa.eu/eli/reg/2024/1252/oj
  locator: Original OJ 3 May 2024; Annex II section 1(g), contrasted with Annex I
    section 1(c)
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Original EU 2024/1252 Annex II lists unqualified boron among critical raw
    materials; the separate strategic entry is metallurgy-grade boron. The record
    retains this named jurisdiction, list and edition rather than broadening the strategic
    designation. Live authority text and retained original HTML independently checked.
  snapshot_sha256: f3ed1698cb32ee124b21752b053af193d06afdabab6cbc3bf1b666a50f3dcdb9
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.jece.2017.06.044
  locator: Author manuscript §§2.1–2.9, 3.1–3.3 and conclusions
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Full primary author-manuscript methods/results support culture-associated
    boron-bearing prepared accretions, with nominal boric-acid doses, living cultures
    and detailed SEM preparation. Uninoculated boric-acid medium processed identically
    is not described; culture without boric acid and raw boric acid comparisons do
    not close that control gap. Manuscript is explicitly distinguished from final
    typeset version.
  snapshot_sha256: d1e2424263d89eb983bb588c023e36d537fd39c9771f95f44e44f83dc616ce16
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1016/j.jece.2017.06.044
  locator: 'PDF pp17–27: Figures 1 remainder and caption, 2–9; Tables 1–2'
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: 'Independently inspected image pixels: Figure 3 extracellular accretions,
    Figure 4 selected EDS B/O signals and Table 2 atomic-percent title versus Weight-percent
    column. Calculated B2O3 composition is not a mineral-phase identification. Figure
    1 caption/axis concentration mismatch is real; Table 1 removal percentages are
    not adopted. Figures 6–7 use raw solid reagent rather than processed sterile medium.
    Figures 8–9 show unidentified protein bands, not a proven pathway.'
  snapshot_sha256: d1e2424263d89eb983bb588c023e36d537fd39c9771f95f44e44f83dc616ce16
- evidence_id: near-match
  kind: primary_source
  reference: https://doi.org/10.1016/j.scitotenv.2026.182050
  locator: Publisher retraction notice title and referred DOI
  accessed_at: '2026-10-11T07:32:30Z'
  support: context_only
  summary: Search returned a retracted review that cites Moraga, but publisher notice
    refers to DOI 10.1016/j.scitotenv.2023.164744, not the accepted 2017 primary.
    This disambiguation prevents a citation-list search match from being mistaken
    for a retraction of Moraga. No scientific claims from the retracted review were
    adopted.
- evidence_id: search
  kind: search
  reference: Independent review-session searches and local hidden/ignored inventory
  locator: Exact DOI, title, contrary-evidence and identifier searches
  accessed_at: '2026-10-11T07:32:30Z'
  support: context_only
  summary: 'Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23"
    correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation;
    "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk
    management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract".
    Inspected first returned result sets only. Related reviews, primary citation matches
    and unrelated DOI/title collisions returned; no matched correction or retraction
    of the two accepted primary papers was identified. A retracted 2023 boron review
    is distinct and was not accepted as evidence. This is not an exhaustive registry
    or citation-network audit. rg --no-ignore --hidden searched data, research, reviews
    and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching
    files were inspected/scoped. find of those roots returned no symlinks. Hidden
    and ignored files were included; this is not a home-directory-wide absence claim.'
  search_scope: 'Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23"
    correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation;
    "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk
    management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract".
    Inspected first returned result sets only. Related reviews, primary citation matches
    and unrelated DOI/title collisions returned; no matched correction or retraction
    of the two accepted primary papers was identified. A retracted 2023 boron review
    is distinct and was not accepted as evidence. This is not an exhaustive registry
    or citation-network audit. rg --no-ignore --hidden searched data, research, reviews
    and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching
    files were inspected/scoped. find of those roots returned no symlinks. Hidden
    and ignored files were included; this is not a home-directory-wide absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element, substrate and organism identity
  outcome: supported
  summary: Atomic identity and taxonomic scope are supported; chemical feed and resulting
    forms are not conflated with the element.
  target_ids:
  - cmmmech:boron
  evidence_ids:
  - record
  - identity
  - organism
- assessment_id: criticality
  area: evidence
  topic: Dated jurisdiction and list designation
  outcome: supported
  summary: The named authority, jurisdiction, list and edition support the record
    mapping with the stated qualifiers.
  target_ids:
  - cmmmech:boron
  evidence_ids:
  - record
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Organism-specific conditions, controls and measured outcome
  outcome: supported
  summary: The exact boron record is defensible as a qualified culture-associated
    B-bearing solid observation. It does not promote SEM-EDS association into proven
    biological mineralization, a named mineral, quantitative recovery or industrial
    treatment. Existing source contradictions are retained; no actionable curation
    finding was established.
  target_ids:
  - cmmmech:boron
  evidence_ids:
  - record
  - primary
  - figures
  dimensions:
  - name: material_form
    value: Element B identity; boric acid feed and unspecified B/O-bearing prepared
      accretions.
    definition: Boron atom, boric acid, borate mineral and commercial borates are
      distinct.
    evidence_ids:
    - record
    - primary
    - figures
  - name: organism_and_biomass
    value: Streptomyces sp. 053 and 128, living cultures before fixation.
    definition: Genus taxonomy is not a strain-level identification; no metabolic-necessity
      experiment.
    evidence_ids:
    - record
    - primary
    - figures
  - name: conditions
    value: Nominal 20/40 mM boric acid, minimal medium, 72 h, 30 degrees C, 250 rpm;
      650 microliters inoculum into 20 mL in 100 mL flasks.
    definition: Post-addition pH 5.58/5.44; fixation, ethanol dehydration, critical-point
      drying and Au/Pd coating precede imaging.
    evidence_ids:
    - record
    - primary
    - figures
  - name: controls
    value: Growing-cell controls omit boric acid; raw solid reagent is separately
      imaged.
    definition: No matched sterile boric-acid medium carried through processing is
      described, leaving preparation and abiotic deposition alternatives.
    evidence_ids:
    - record
    - primary
    - figures
  - name: quantity
    value: No removal percentage, capacity or isolated solid yield adopted.
    definition: Nominal stock-dose arithmetic, Figure 1 mg/L scaling and undocumented
      colorimetric dilution prevent an assured mass balance.
    evidence_ids:
    - record
    - primary
    - figures
  - name: deployment
    value: Laboratory liquid culture only.
    definition: Soil origin of the strains does not demonstrate soil treatment or
      an industrial recovery process.
    evidence_ids:
    - record
    - primary
    - figures
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE provenance
  outcome: supported
  summary: Distinct inline and sidecar events state actual actor/model/tool and target.
    Trusted-base history validation passed; no record edits or fabricated prior authorship
    by reviewer.
  target_ids:
  - cmmmech:boron
  evidence_ids:
  - record
- assessment_id: search
  area: completeness
  topic: Bounded duplicate and contrary-evidence coverage
  outcome: supported
  summary: Scoped hidden/ignored inventory and primary internal counterevidence were
    checked. Searches provide bounded coverage, not proof of literature completeness.
  target_ids:
  - cmmmech:boron
  evidence_ids:
  - search
  - primary
findings: []
actions: []
limitations:
- The study lacks a matched processed sterile boric-acid medium control and diffraction-based
  phase identity; preparation-associated or abiotic deposition is not excluded.
- Nominal dose arithmetic, Figure 1 concentration labels, calibration/dilution description
  and Table 2 composition units remain contradictory; no quantitative recovery is
  inferred.
- Strains remain genus-qualified and protein bands unassigned; metabolic necessity,
  intracellular uptake, isolated product and deployment are unproven.
- Author manuscript was inspected; no separate supplement link was found in the inspected
  PDF/PMC content, a bounded access observation rather than universal absence.
- Correction/retraction and contrary-evidence searches cover first returned result
  sets and cited local sources, not exhaustive registries or all possible conflicting
  studies.
notes:
- Reviewed final working-tree bytes on trusted base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2;
  this is not a committed-source attestation.
- 'Findings by severity: no confirmed blocker, major, minor or informational curation
  defect. Corrections in this round: none. Unresolved scientific questions are retained
  under limitations; they do not invalidate the qualified observation.'
- Raw source snapshots remain outside Git at /private/tmp/cmm-round10-b-f-raw. Reviewer
  inspections, local search receipt and named validation are under /private/tmp/cmm-round10-b-f-independent.
links:
- https://github.com/CultureBotAI/CMMMech/issues/42
```
