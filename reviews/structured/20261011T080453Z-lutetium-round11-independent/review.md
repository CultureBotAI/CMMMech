# Independent scientific review of lutetium round11 record

- Review: 20261011T080453Z-lutetium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:57:28Z
- Finished UTC: 2026-10-11T08:04:53Z
- Reviewer: Codex /root/cmm11_be_rb_re (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Element identity, dated US designation and the Lu-specific control-relative biosorption observation are supported, with appropriate preparation, control, percentage denominator and deployment limits. No actionable defect found.

## Scope And Provenance

All scientific and provenance fields of this named record; source-specific identity, criticality and accepted experimental evidence. Deferred literature is context only.

Selection: Assigned named record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lutetium | data/records/lutetium.yaml | maintained | Lutetium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:lutetium | Reviewer session 21846 terminal exit 0; final named validation checked 3 records, 0 failed. |
| Parent full native batch gate | passed | True | cmmmech:lutetium | Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records and 83 histories valid. Root session 92015 terminal exit 0. Reviewer independently read the complete log and received the terminal exit receipt. |
| Parent nonempty corpus validation | passed | True | cmmmech:lutetium | Final required-record validation passed 71 records, zero failed. Root session 93511 terminal exit 0. Reviewer independently read the complete log and received the terminal exit receipt. |
| Parent trusted-base history validation | passed | True | cmmmech:lutetium | Final trusted-base history validation passed 83 histories, zero errors. Root session 88115 terminal exit 0. Reviewer independently read the complete log and received the terminal exit receipt. |

## Scientific And Domain Assessments

### Element versus experimental form and list scope

identity: supported. Targets: cmmmech:lutetium.

Verified element identity and explicit dated criticality remain distinct from ions, host minerals, isotope tracers and commodity mixtures.

### Control-relative Lu depletion

evidence: supported. Targets: cmmmech:lutetium.

The narrow biosorption observation is supported with cell localization and chemistry unresolved.

### CREATE provenance and frozen bytes

provenance: supported. Targets: cmmmech:lutetium.

Actual sidecar and separate inline CREATE event are consistent; no review-derived curation is backdated.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lutetium.yaml; Entire frozen native record, linked CREATE history, shared MD/JSON dossier and schema | supports | Final inspect captured target, histories and corrected shared dossier bytes. The only shared scientific correction narrows Tm LTA causality; Lu and Pm target bytes remain unchanged. Actual actor codex/GPT-6/codex and issue links match the separate inline events. |
| identity | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33382/; Fresh public API chebi_accession, name and chemical_data fields | supports | Independent fresh HTTP 200 API resolution identifies lutetium atom, formula Lu, charge zero. The identifier denotes an elemental root, not the experimental ion, isotope or salt. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; US DOI/USGS final notice, 7 November 2025, 90 FR 50494–50497; Lutetium commodity row | supports | Independent live notice and retained authority HTML confirm the named commodity in Final 2025 list. Adjacent Yes describes byproduct status. The experimental chloride feed does not itself become a designated mineral. |
| validation | /private/tmp/cmm-round11-final-check.log; Complete batch, nonempty, history logs plus reviewer named validation | supports | Actual logs were read independently; precise commands and terminal results are reported under checks. Canonical history and inline events are distinct provenance. |
| search | Bounded independent web queries and scoped local trees; First returned web result sets, 11 October 2026; exact identity/DOI local search | context_only | The inspected DOI correction/erratum/retraction result sets returned papers and citing literature, no matching notice. This is a bounded observation, not exhaustive absence. Accepted full texts and source figures were checked separately from regex. |
| primary | https://doi.org/10.3390/met10070954; Complete main methods/results/discussion/conclusion text; rendered pp3,5,6,8,11; supplementary Table S1/Figure S1 p1 and immobilization Figure S4 p4 | supports | Independent reading confirms the eight-element Lu arm and concurrent no-biomass denominator. Table S1 has 74% at 2h and4h; four-element arm and Figure S1 omit Lu. Separate loading, Fe/Zr and autoclaved arms do not establish universal selectivity, metabolic causation or deployment. |
| supplement | https://mdpi-res.com/d_attachment/metals/metals-10-00954/article_deploy/metals-10-00954-s001.pdf; All five pages text; Table S1/Figure S1 p1 and Figure S4 p4 visually | supports | Table S1 experiment2 contains Lu; experiment1 does not. The immobilized-biomass experiment remains separate from the accepted suspended-biomass outcome. |
| taxonomy | https://www.atcc.org/products/7003; ATCC 7003 retained official HTML; fresh NCBI taxonomy1423 XML | supports | ATCC identifies NRS 730 as B.subtilis; NCBI 1423 is species rank. Strain ATCC 7003 is not strain 168. |

## Limits And Additional Notes

- No raw ICP-MS recalculation or independent culture replication is available; duplicate assays do not establish biological replication.
- Control-relative loss cannot distinguish extracellular binding, intracellular retention and cell-associated precipitation.
- No Lu-specific ligand causality, product purity, desorption yield or industrial deployment follows from the accepted arm.
- Bounded search result sets and cited-source inspection do not exhaust all later corrections, supplements or alternative mechanisms. Verdict applies to the exact target hash.
- No record, history or dossier edits by this reviewer. Initial failed inspect invocations used a wrong schema path and then an unwritable default UV cache; corrected invocations succeeded and bound unchanged target bytes. Named validation passed independently.
- Twenty acquired source hashes matched the curator receipts. Raw papers remain outside Git. The dated list assertions do not assert latest status in every jurisdiction.
- Shared Tm dossier correction was independently compared before final inspection; it changes no lutetium science, source acquisitions or record bytes. This review binds the corrected shared dossier context.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080453Z-lutetium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of lutetium round11 record
started_at: '2026-10-11T07:57:28Z'
finished_at: '2026-10-11T08:04:53Z'
reviewer:
  identity: Codex /root/cmm11_be_rb_re
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer curated only the separate Be/Rb/Re trio. I did not
    author or edit these Lu/Tm/Pm records, histories or dossier. After helper path/cache
    invocation errors were corrected, inspect captured the unchanged frozen bytes
    before conclusions; primary sources, figures, identity authorities and dated criticality
    were assessed independently.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: data/records/lutetium.yaml
    sha256: a7962fcca9cdea5dd0c538f7d0f4707439a5241cd49819e93750245bf9a69789
    role: target
  - path: history/records/lutetium/2026-10-11T075300Z-codex-aa9d5e.yaml
    sha256: 64ea6d42d4ca519103a55b4a68f033bcd80376bb8ecefe4b9095d3ff2a9f3aea
    role: context
  - path: research/ingests/round11-lu-tm-pm-20261011.json
    sha256: aa6f8e56272c8b2396c532eddd36bbb96eb4bc8d16bb5ecfb6e71d97fc2bae77
    role: context
  - path: research/ingests/round11-lu-tm-pm-20261011.md
    sha256: 6859b6dbb806348045fae5c2234217c226c494dc7bacbc5ef38296b749630398
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:lutetium
  path: data/records/lutetium.yaml
  label: Lutetium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lutetium.yaml
    role: maintained native record
scope:
  description: All scientific and provenance fields of this named record; source-specific
    identity, criticality and accepted experimental evidence. Deferred literature
    is context only.
  selection: Assigned named record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lutetium
checks:
- check_id: named
  name: Reviewer named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/lutetium.yaml data/records/thulium.yaml data/records/promethium.yaml
  status: passed
  required: true
  summary: Reviewer session 21846 terminal exit 0; final named validation checked
    3 records, 0 failed.
  scope_note: /private/tmp/cmm-round11-final-independent-lu-tm-pm-validation.log;
    independently executed after the correction.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:lutetium
- check_id: batch
  name: Parent full native batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records
    and 83 histories valid. Root session 92015 terminal exit 0. Reviewer independently
    read the complete log and received the terminal exit receipt.
  scope_note: /private/tmp/cmm-round11-final-check.log
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:lutetium
- check_id: nonempty
  name: Parent nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Final required-record validation passed 71 records, zero failed. Root session
    93511 terminal exit 0. Reviewer independently read the complete log and received
    the terminal exit receipt.
  scope_note: /private/tmp/cmm-round11-final-validation.log
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:lutetium
- check_id: history
  name: Parent trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  status: passed
  required: true
  summary: Final trusted-base history validation passed 83 histories, zero errors.
    Root session 88115 terminal exit 0. Reviewer independently read the complete log
    and received the terminal exit receipt.
  scope_note: /private/tmp/cmm-round11-final-history.log
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:lutetium
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lutetium.yaml
  locator: Entire frozen native record, linked CREATE history, shared MD/JSON dossier
    and schema
  accessed_at: '2026-10-11T08:03:56Z'
  support: supports
  summary: Final inspect captured target, histories and corrected shared dossier bytes.
    The only shared scientific correction narrows Tm LTA causality; Lu and Pm target
    bytes remain unchanged. Actual actor codex/GPT-6/codex and issue links match the
    separate inline events.
  snapshot_sha256: a7962fcca9cdea5dd0c538f7d0f4707439a5241cd49819e93750245bf9a69789
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33382/
  locator: Fresh public API chebi_accession, name and chemical_data fields
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Independent fresh HTTP 200 API resolution identifies lutetium atom, formula
    Lu, charge zero. The identifier denotes an elemental root, not the experimental
    ion, isotope or salt.
  snapshot_sha256: 57ef1e72de79ec409889e0aa97fa403d9f4dd957a0e0ec977c688daf1823674f
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: US DOI/USGS final notice, 7 November 2025, 90 FR 50494–50497; Lutetium
    commodity row
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Independent live notice and retained authority HTML confirm the named commodity
    in Final 2025 list. Adjacent Yes describes byproduct status. The experimental
    chloride feed does not itself become a designated mineral.
  snapshot_sha256: f9d7bdc090fcdfa861c220efbcbddd889efda4fe005800a11906532427ffade0
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round11-final-check.log
  locator: Complete batch, nonempty, history logs plus reviewer named validation
  accessed_at: '2026-10-11T08:04:53Z'
  support: supports
  summary: Actual logs were read independently; precise commands and terminal results
    are reported under checks. Canonical history and inline events are distinct provenance.
  snapshot_sha256: c77a6c80e36a0fc706ea157d0a79dc84cabdd120f3952e93f950832cb3b881be
- evidence_id: search
  kind: search
  reference: Bounded independent web queries and scoped local trees
  locator: First returned web result sets, 11 October 2026; exact identity/DOI local
    search
  accessed_at: '2026-10-11T08:01:04Z'
  support: context_only
  summary: The inspected DOI correction/erratum/retraction result sets returned papers
    and citing literature, no matching notice. This is a bounded observation, not
    exhaustive absence. Accepted full texts and source figures were checked separately
    from regex.
  search_scope: 'web.run without filters or pagination: "10.3390/met10070954" correction
    retraction erratum; "10.1007/s00253-012-4200-3" correction retraction erratum;
    "lutetium" "Bacillus" "biosorption" Breuker contrary; "promethium" bacteria sorption
    Pedersen 1990 1991; exact Tm DOI with erratum; exact Lu DOI with retraction; "lipoteichoic"
    "Tm" "adsorption" mutant residual. rg --no-ignore --hidden --follow searched ChEBI33382/33380/33373,
    exact CMM IDs and accepted DOIs in data/research/reviews/history/.claude, including
    ignored files; matches were this trio and shared dossier. Prior cited raw roots
    and acquisition manifest were read as scoped provenance, not a machine-wide absence
    search.'
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/met10070954
  locator: Complete main methods/results/discussion/conclusion text; rendered pp3,5,6,8,11;
    supplementary Table S1/Figure S1 p1 and immobilization Figure S4 p4
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Independent reading confirms the eight-element Lu arm and concurrent no-biomass
    denominator. Table S1 has 74% at 2h and4h; four-element arm and Figure S1 omit
    Lu. Separate loading, Fe/Zr and autoclaved arms do not establish universal selectivity,
    metabolic causation or deployment.
  snapshot_sha256: b2ce390d51e652b3a5cdbbb03ebad7e08997126e3c26d4d1836a0d924abb66d8
- evidence_id: supplement
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/metals/metals-10-00954/article_deploy/metals-10-00954-s001.pdf
  locator: All five pages text; Table S1/Figure S1 p1 and Figure S4 p4 visually
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Table S1 experiment2 contains Lu; experiment1 does not. The immobilized-biomass
    experiment remains separate from the accepted suspended-biomass outcome.
  snapshot_sha256: c4f7b98a87ee5ae06ef17676deaf9f35f233b3d1f6a32467d99255b2e675cc9f
- evidence_id: taxonomy
  kind: database
  reference: https://www.atcc.org/products/7003
  locator: ATCC 7003 retained official HTML; fresh NCBI taxonomy1423 XML
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: ATCC identifies NRS 730 as B.subtilis; NCBI 1423 is species rank. Strain
    ATCC 7003 is not strain 168.
  snapshot_sha256: 3acf923cb755e3184466b4dba362a904c6ecc91f785e3c8b6a41cf2f9c4e4c4b
assessments:
- assessment_id: identity-grounding
  area: identity
  topic: Element versus experimental form and list scope
  outcome: supported
  summary: Verified element identity and explicit dated criticality remain distinct
    from ions, host minerals, isotope tracers and commodity mixtures.
  target_ids:
  - cmmmech:lutetium
  evidence_ids:
  - record
  - identity
  - criticality
  dimensions:
  - name: material-form
    value: Lutetium elemental root; CHEBI:33382
    definition: Neutral atomic identity grounds the element record.
    evidence_ids:
    - identity
  - name: criticality
    value: United States DOI/USGS; Final 2025 List of Critical Minerals; 7 November
      2025
    definition: Dated source-specific designation.
    evidence_ids:
    - criticality
- assessment_id: assay
  area: evidence
  topic: Control-relative Lu depletion
  outcome: supported
  summary: The narrow biosorption observation is supported with cell localization
    and chemistry unresolved.
  target_ids:
  - cmmmech:lutetium
  evidence_ids:
  - record
  - primary
  - supplement
  - taxonomy
  dimensions:
  - name: organism
    value: Bacillus subtilis ATCC 7003; NCBITaxon1423 species
    definition: Species ID is not a strain ID.
    evidence_ids:
    - taxonomy
    - primary
  - name: biomass-state
    value: Washed non-autoclaved biomass; authors call it living
    definition: Viability during acidic assay not demonstrated; autoclaving also changes
      integrity.
    evidence_ids:
    - primary
  - name: pretreatment
    value: FP medium; 30C/120rpm/2–4days; twice acid-water washed
    definition: Growth temperature differs from assay room temperature.
    evidence_ids:
    - primary
  - name: feed-conditions
    value: Eight REE chlorides, each15micromol/L; biomass5g dry/L; pH2.5 HCl; room
      temperature
    definition: The accepted Table S1 arm; separate autoclaved assay used4g/L.
    evidence_ids:
    - primary
    - supplement
  - name: controls
    value: Concurrent duplicated no-biomass controls; centrifugation/0.2micrometre
      nylon filtration and ICP-MS
    definition: Independent culture replication unspecified; excludes some abiotic
      loss but not cell-associated precipitation.
    evidence_ids:
    - primary
  - name: outcome
    value: 74% Lu at2h and4h
    definition: (concurrent control concentration minus sample)/control ×100; not
      product yield.
    evidence_ids:
    - supplement
  - name: deployment
    value: Laboratory synthetic feed
    definition: Gd wastewater arm and fungi are not Lu deployment evidence.
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: CREATE provenance and frozen bytes
  outcome: supported
  summary: Actual sidecar and separate inline CREATE event are consistent; no review-derived
    curation is backdated.
  target_ids:
  - cmmmech:lutetium
  evidence_ids:
  - record
  - validation
findings: []
actions: []
limitations:
- No raw ICP-MS recalculation or independent culture replication is available; duplicate
  assays do not establish biological replication.
- Control-relative loss cannot distinguish extracellular binding, intracellular retention
  and cell-associated precipitation.
- No Lu-specific ligand causality, product purity, desorption yield or industrial
  deployment follows from the accepted arm.
- Bounded search result sets and cited-source inspection do not exhaust all later
  corrections, supplements or alternative mechanisms. Verdict applies to the exact
  target hash.
notes:
- No record, history or dossier edits by this reviewer. Initial failed inspect invocations
  used a wrong schema path and then an unwritable default UV cache; corrected invocations
  succeeded and bound unchanged target bytes. Named validation passed independently.
- Twenty acquired source hashes matched the curator receipts. Raw papers remain outside
  Git. The dated list assertions do not assert latest status in every jurisdiction.
- Shared Tm dossier correction was independently compared before final inspection;
  it changes no lutetium science, source acquisitions or record bytes. This review
  binds the corrected shared dossier context.
summary: Element identity, dated US designation and the Lu-specific control-relative
  biosorption observation are supported, with appropriate preparation, control, percentage
  denominator and deployment limits. No actionable defect found.
```
