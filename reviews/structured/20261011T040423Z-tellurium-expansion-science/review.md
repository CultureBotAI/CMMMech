# Tellurium independent adversarial scientific review

- Review: 20261011T040423Z-tellurium-expansion-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T04:02:45Z
- Finished UTC: 2026-10-11T04:04:23Z
- Reviewer: /root (Codex) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded laboratory transformation claim, identities and dated criticality are supported. No actionable defect found. Concentration-label ambiguity, missing biomass normalization, controls at one dose and absent product mass yield remain explicit limitations.

## Scope And Provenance

All current tellurium record fields and linked creation history, with primary methods/results, relevant figures and supplement checks.

Selection: One assigned new record; exact final bytes after history attachment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 76cd81d310a6ccb4cf7bdebcc61be050d0863222.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tellurium | data/records/tellurium.yaml | maintained | Tellurium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record validation | passed | True | cmmmech:tellurium | 1 record checked; 0 failed. |
| History linkage and append-only check | passed | True | cmmmech:tellurium | 22 history records checked; 0 errors. |
| Independent source and identity verification | passed | True | cmmmech:tellurium | Authority pages, paper text, supplementary methods and selected figures inspected as recorded below. |

## Scientific And Domain Assessments

### Element, precursor and organism scope

identity: supported. Targets: cmmmech:tellurium.

Element identity and species grounding match authorities; experimental salt and exact BCP1/DSM strain are distinguished.

### Dated criticality

grounding: supported. Targets: cmmmech:tellurium.

Named final US 2025 edition supports the designation without extending it to all tellurium compounds.

### Organism, conditions, controls, analytical outcome and scale

evidence: supported. Targets: cmmmech:tellurium.

Narrow transformation claim is supported. Record distinguishes solution depletion from a recovered product yield and interpretation from established molecular causality.

### Measurement semantics

quantity: supported. Targets: cmmmech:tellurium.

Reported percentage endpoints are consistent with main text and Figure 1; uncertainty is SD in the source. No inappropriate mg/kg observation created.

### Distinct curation events and sidecar

provenance: supported. Targets: cmmmech:tellurium.

History attachment and creation event validated without changing target bytes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/tellurium.yaml; All fields and inline curation_history | supports | Read exact inspected bytes. No changes made by reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:30452; Name, formula, net charge and IUPAC synonym | supports | Tellurium atom, Te, charge zero; element identity does not denote potassium tellurite feed. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=191292&amp;mode=Info; Current name, includes and rank | supports | Species Rhodococcus aetherivorans includes Rhodococcus sp. BCP1. Species taxon does not resolve an experimental strain; DSM 44980 comes from primary Methods. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 notice, final table tellurium row on page 50497 and draft/final discussion | supports | Final United States 2025 list contains tellurium despite draft removal proposal. Edition and jurisdiction are explicit; no mineral or waste designation is inferred. |
| paper | https://link.springer.com/article/10.1038/s41598-018-22320-x; Results: tolerance and biotic conversion; electron microscopy; assembly; Methods; Figures 1-3,5,7 | supports | Read full relevant methods and results. Living resting BCP1 cells transform precursor under aerobic laboratory conditions. Endpoints 42 +/- 3% and 28 +/- 4% at higher doses, n=3 biological replicates, SD. SAED supports t-Te in analyzed rods. Proposed surfactant pathway is not a demonstrated necessary enzyme mechanism. |
| supplement | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-018-22320-x/MediaObjects/41598_2018_22320_MOESM1_ESM.doc; Supplementary methods, bioconversion assay and Figure S1 caption; retained supplement.txt extracted from linked DOC | supports | Read full retained text. Two PBS washes, pH 7.4, 50 mL, 30 C, 150 rpm, 0.5-16 h and K2TeO3 mass loadings supported. PBS-only/autoclaved controls at highest dose and 340 nm supernatant assay supported. No quantitative initial biomass or detection limit in exposure/assay protocol. |
| figures | https://link.springer.com/article/10.1038/s41598-018-22320-x; Full publisher Figures 1, 2 and 5 downloaded and visually inspected | supports | Figure 1c is consistent with partial high-dose removal; Figure 2 shows cell-associated rods with dose/time labels; Figure 5 shows one rod, lattice image and indexed SAED. No raw diffraction refitting, graph digitization or universal phase assignment performed. |
| search | Bounded web and repository searches on 2026-10-11; Exact DOI correction/retraction query; BCP1 tellurium contradictory/tellurite-reduction query; local identity/DOI search | context_only | No affecting notice identified in returned first-result sets. Earlier growing-cell and different-strain studies were surfaced, not conflated with this resting-cell assay. No exhaustive absence conclusion. |
| history | history/records/tellurium/2026-10-11T040057Z-codex-bc6ab1.yaml; Target, UTC session, actor/model and CREATE event; attached history_refs | supports | Sidecar and separate inline event describe actual present curation with no invented earlier authorship. Baseline history unchanged. |

## Limits And Additional Notes

- Mass basis differs between supplementary salt labels and main-text oxyanion labels; record preserves ambiguity.
- No initial dry biomass/OD quantification or analytical detection limit in inspected exposure/assay protocol; not a normalized capacity or literal zero claim.
- Supplementary figures were text/caption inspected, not visually inspected; main Figures 1, 2 and 5 were visually examined. No raw diffraction or microscopy reanalysis.
- One primary assay; search was bounded. Methods for additional discovery leads are not accepted evidence for this record.
- Batch tests, current-hash coverage, queue checks and fresh post-merge validation are separate parent-owned publication gates.
- This scientific review does not amend the record or create a curation-history event. The reviewed revision is reachable from current main; working-tree attestation retains exact target hash.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040423Z-tellurium-expansion-science
kind: record
repository: CultureBotAI/CMMMech
title: Tellurium independent adversarial scientific review
started_at: '2026-10-11T04:02:45Z'
finished_at: '2026-10-11T04:04:23Z'
reviewer:
  identity: /root (Codex)
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Parent reviewer did not author or edit tellurium record, history
    or dossier. Independently opened identity/list authorities and primary full text,
    read retained supplementary methods and visually examined primary Figures 1, 2
    and 5.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded laboratory transformation claim, identities and dated criticality
  are supported. No actionable defect found. Concentration-label ambiguity, missing
  biomass normalization, controls at one dose and absent product mass yield remain
  explicit limitations.
source:
  git_revision: 76cd81d310a6ccb4cf7bdebcc61be050d0863222
  state: working_tree
  inputs:
  - path: data/records/tellurium.yaml
    sha256: 8de03e4ddd334be7f6adf1813384529600bdbab2b9b0dec6f0f394fdbab81f38
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/tellurium/2026-10-11T040057Z-codex-bc6ab1.yaml
    sha256: 565ba88f23db358c418968066f3ae52de7250318493e44ddf3537a49525768cb
    role: context
  - path: research/ingests/expansion-tellurium-20261011.md
    sha256: 72727c1fd8d47f38134d3f88eecbd63106b9f77ebe137f6c21ac45de98dfb8a3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All current tellurium record fields and linked creation history, with
    primary methods/results, relevant figures and supplement checks.
  selection: One assigned new record; exact final bytes after history attachment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tellurium
  exclusions:
  - target: Other tellurium mechanisms and PR publication
    reason: Additional experiments are discovery leads; root manages publication separately.
targets:
- target_id: cmmmech:tellurium
  path: data/records/tellurium.yaml
  label: Tellurium
  kind: maintained
  record_class: CriticalMineralRecord
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tellurium.yaml
    role: maintained scientific record
checks:
- check_id: record
  name: Single-record validation
  status: passed
  required: true
  summary: 1 record checked; 0 failed.
  target_ids:
  - cmmmech:tellurium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/tellurium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: History linkage and append-only check
  status: passed
  required: true
  summary: 22 history records checked; 0 errors.
  target_ids:
  - cmmmech:tellurium
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate-history
    --base 76cd81d310a6ccb4cf7bdebcc61be050d0863222
  exit_code: 0
  expected_exit_code: 0
- check_id: science
  name: Independent source and identity verification
  status: passed
  required: true
  summary: Authority pages, paper text, supplementary methods and selected figures
    inspected as recorded below.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - identity
  - taxon
  - criticality
  - paper
  - supplement
  - figures
  - search
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/tellurium.yaml
  locator: All fields and inline curation_history
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Read exact inspected bytes. No changes made by reviewer.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30452
  locator: Name, formula, net charge and IUPAC synonym
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Tellurium atom, Te, charge zero; element identity does not denote potassium
    tellurite feed.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=191292&mode=Info
  locator: Current name, includes and rank
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Species Rhodococcus aetherivorans includes Rhodococcus sp. BCP1. Species
    taxon does not resolve an experimental strain; DSM 44980 comes from primary Methods.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 notice, final table tellurium row on page 50497 and draft/final
    discussion
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Final United States 2025 list contains tellurium despite draft removal
    proposal. Edition and jurisdiction are explicit; no mineral or waste designation
    is inferred.
- evidence_id: paper
  kind: primary_source
  reference: https://link.springer.com/article/10.1038/s41598-018-22320-x
  locator: 'Results: tolerance and biotic conversion; electron microscopy; assembly;
    Methods; Figures 1-3,5,7'
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Read full relevant methods and results. Living resting BCP1 cells transform
    precursor under aerobic laboratory conditions. Endpoints 42 +/- 3% and 28 +/-
    4% at higher doses, n=3 biological replicates, SD. SAED supports t-Te in analyzed
    rods. Proposed surfactant pathway is not a demonstrated necessary enzyme mechanism.
- evidence_id: supplement
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-018-22320-x/MediaObjects/41598_2018_22320_MOESM1_ESM.doc
  locator: Supplementary methods, bioconversion assay and Figure S1 caption; retained
    supplement.txt extracted from linked DOC
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Read full retained text. Two PBS washes, pH 7.4, 50 mL, 30 C, 150 rpm,
    0.5-16 h and K2TeO3 mass loadings supported. PBS-only/autoclaved controls at highest
    dose and 340 nm supernatant assay supported. No quantitative initial biomass or
    detection limit in exposure/assay protocol.
  snapshot_sha256: 6fb9ea09cca1c9f3ce46e1647b5f8d2de2fbe799d7a610ba08aab2924f675727
- evidence_id: figures
  kind: primary_source
  reference: https://link.springer.com/article/10.1038/s41598-018-22320-x
  locator: Full publisher Figures 1, 2 and 5 downloaded and visually inspected
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Figure 1c is consistent with partial high-dose removal; Figure 2 shows
    cell-associated rods with dose/time labels; Figure 5 shows one rod, lattice image
    and indexed SAED. No raw diffraction refitting, graph digitization or universal
    phase assignment performed.
- evidence_id: search
  kind: search
  reference: Bounded web and repository searches on 2026-10-11
  locator: Exact DOI correction/retraction query; BCP1 tellurium contradictory/tellurite-reduction
    query; local identity/DOI search
  accessed_at: '2026-10-11T04:04:23Z'
  support: context_only
  summary: No affecting notice identified in returned first-result sets. Earlier growing-cell
    and different-strain studies were surfaced, not conflated with this resting-cell
    assay. No exhaustive absence conclusion.
  search_scope: 'Web queries: "10.1038/s41598-018-22320-x" correction retraction;
    "Rhodococcus aetherivorans BCP1" tellurium contradictory tellurite reduction.
    First returned sets only. rg --no-ignore --hidden across data, history, reviews
    and research for CHEBI:30452, cmmmech:tellurium and DOI; current record and dossier
    were only identity/DOI matches at check time.'
- evidence_id: history
  kind: record_content
  reference: history/records/tellurium/2026-10-11T040057Z-codex-bc6ab1.yaml
  locator: Target, UTC session, actor/model and CREATE event; attached history_refs
  accessed_at: '2026-10-11T04:04:23Z'
  support: supports
  summary: Sidecar and separate inline event describe actual present curation with
    no invented earlier authorship. Baseline history unchanged.
assessments:
- assessment_id: identity
  area: identity
  topic: Element, precursor and organism scope
  outcome: supported
  summary: Element identity and species grounding match authorities; experimental
    salt and exact BCP1/DSM strain are distinguished.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - identity
  - taxon
  - record
- assessment_id: authority
  area: grounding
  topic: Dated criticality
  outcome: supported
  summary: Named final US 2025 edition supports the designation without extending
    it to all tellurium compounds.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - criticality
  - record
- assessment_id: mechanism
  area: evidence
  topic: Organism, conditions, controls, analytical outcome and scale
  outcome: supported
  summary: Narrow transformation claim is supported. Record distinguishes solution
    depletion from a recovered product yield and interpretation from established molecular
    causality.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - paper
  - supplement
  - figures
  - record
  dimensions:
  - name: biomass
    value: Living resting, non-growing R. aetherivorans BCP1 (DSM 44980)
    definition: Species ID plus experimental strain from Methods; not inactive biomass
      or industrial culture.
    evidence_ids:
    - paper
    - taxon
  - name: substrate_conditions
    value: K2TeO3 in PBS pH 7.4; 50 mL; 30 C; 150 rpm; 0.5-16 h
    definition: Supplement reports salt-mass loadings while main text labels tellurite;
      no elemental-Te conversion.
    evidence_ids:
    - supplement
  - name: controls
    value: PBS only and autoclaved biomass at highest nominal dose
    definition: Controls do not establish the same analytical precision at every dose.
    evidence_ids:
    - supplement
  - name: outcome_scale
    value: Partial high-dose depletion and intracellular Te rods; laboratory only
    definition: No mass-balanced isolated-product yield or industrial deployment.
    evidence_ids:
    - paper
    - figures
- assessment_id: quantity
  area: quantity
  topic: Measurement semantics
  outcome: supported
  summary: Reported percentage endpoints are consistent with main text and Figure
    1; uncertainty is SD in the source. No inappropriate mg/kg observation created.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - paper
  - figures
  - supplement
- assessment_id: provenance
  area: provenance
  topic: Distinct curation events and sidecar
  outcome: supported
  summary: History attachment and creation event validated without changing target
    bytes.
  target_ids:
  - cmmmech:tellurium
  evidence_ids:
  - history
  - record
findings: []
actions: []
limitations:
- Mass basis differs between supplementary salt labels and main-text oxyanion labels;
  record preserves ambiguity.
- No initial dry biomass/OD quantification or analytical detection limit in inspected
  exposure/assay protocol; not a normalized capacity or literal zero claim.
- Supplementary figures were text/caption inspected, not visually inspected; main
  Figures 1, 2 and 5 were visually examined. No raw diffraction or microscopy reanalysis.
- One primary assay; search was bounded. Methods for additional discovery leads are
  not accepted evidence for this record.
- Batch tests, current-hash coverage, queue checks and fresh post-merge validation
  are separate parent-owned publication gates.
notes:
- This scientific review does not amend the record or create a curation-history event.
  The reviewed revision is reachable from current main; working-tree attestation retains
  exact target hash.
```
