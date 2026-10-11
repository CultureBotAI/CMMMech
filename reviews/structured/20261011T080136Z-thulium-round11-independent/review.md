# Independent scientific review of thulium round11 record

- Review: 20261011T080136Z-thulium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:57:28Z
- Finished UTC: 2026-10-11T08:01:36Z
- Reviewer: Codex /root/cmm11_be_rb_re (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Element identity, dated US designation and prepared-powder depletion/elution observations are supported. One minor mechanistic overstatement needs correction: residual binding in an LTA-defective preparation does not establish that LTA is unnecessary when residual LTA is unquantified.

## Scope And Provenance

All scientific and provenance fields of this named record; source-specific identity, criticality and accepted experimental evidence. Deferred literature is context only.

Selection: Assigned named record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:thulium | Reviewer session5351 terminal0; 3 records checked, 0 failed. |
| Parent full native batch gate | passed | True | cmmmech:thulium | Parent session54253 terminal0 confirmed; reviewer read complete log:307 passed,3 skipped in50.77s;71 records and82 histories valid. |
| Parent nonempty corpus validation | passed | True | cmmmech:thulium | Parent session22172 terminal0 confirmed; reviewer read complete log:71 records checked,0 failed. |
| Parent trusted-base history validation | passed | True | cmmmech:thulium | Parent session72936 terminal0 confirmed; reviewer read complete log:82 histories checked,0 errors. |

## Scientific And Domain Assessments

### Element versus experimental form and list scope

identity: supported. Targets: cmmmech:thulium.

Verified element identity and explicit dated criticality remain distinct from ions, host minerals, isotope tracers and commodity mixtures.

### Prepared bacterial powder adsorption and acidic elution

evidence: supported. Targets: cmmmech:thulium.

Experimental form and measured endpoint are accurately scoped; necessity wording is handled separately.

### Necessity is not established by a defective preparation

consistency: concern. Targets: cmmmech:thulium.

One sentence asserts LTA is not necessary despite unquantified residual LTA.

RY1604 retains inducible ltaS; preparation removes IPTG for a limited cultivation period. The manuscript does not directly measure LTA absence in the tested powder and says ligand abundance ratios were unquantified. The observed residual depletion alone cannot decide necessity.

### CREATE provenance and frozen bytes

provenance: supported. Targets: cmmmech:thulium.

Actual sidecar and separate inline CREATE event are consistent; no review-derived curation is backdated.

## Findings

### F1: Residual adsorption does not establish that LTA is unnecessary

minor / open / confirmed; issue key: thulium-lta-necessity-overstatement.

The mechanism description says LTA is not an exclusive or necessary binding route. Conditional ltaS expression after IPTG removal and unmeasured residual LTA do not prove complete ligand absence. Preserve the residual adsorption observation and state that the comparison cannot establish exclusive LTA causality or quantify its contribution. The same overstatement occurs in the shared dossier.

## Recommended Actions And Acceptance Checks

### A1

Narrow the record and matching dossier language to the observed defective-biomass comparison; append actual EDIT provenance and independently reassess the final bytes.

- No claim that LTA is unnecessary without direct absence/complementation evidence.
- Retain observed WT/mutant values, conditional genotype, source yvgJ/yvyJ discrepancy and uncertainty.
- Run affected named validation and full required gates; save successor review resolving this exact occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/thulium.yaml; Entire frozen native record, linked CREATE history, shared MD/JSON dossier and schema | supports | Exact inspected target hash agrees with the curator freeze. Sidecar actor codex/GPT-6/codex, actual CREATE time and issue44 linkage agree with the later, separate inline event. |
| identity | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33380/; Fresh public API chebi_accession, name and chemical_data fields | supports | Independent fresh HTTP200 API resolution identifies thulium atom, formula Tm, charge zero. The identifier denotes an elemental root, not the experimental ion, isotope or salt. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; US DOI/USGS final notice, 7 November2025, 90FR50494–50497; Thulium commodity row | supports | Independent live notice and retained authority HTML confirm the named commodity in Final2025 list. Adjacent Yes describes byproduct status. The experimental chloride feed does not itself become a designated mineral. |
| validation | /private/tmp/cmm-round11-batch-check.log; Complete batch, nonempty, history logs plus reviewer named validation | supports | Actual logs were read independently; precise commands and terminal results are reported under checks. Canonical history and inline events are distinct provenance. |
| search | Bounded independent web queries and scoped local trees; First returned web result sets, 11October2026; exact identity/DOI local search | context_only | The inspected DOI correction/erratum/retraction result sets returned papers and citing literature, no matching notice. This is a bounded observation, not exhaustive absence. Accepted full texts and source figures were checked separately from regex. |
| primary | https://soar-ir.repo.nii.ac.jp/records/13337; Deposited24-page accepted manuscript; methods pp5–9, results/discussion pp10–14; Tables1/3 pp19/21 and all figures pp22–24 visually | supports | Boiled and freeze-dried parent/mutant powders show Tm depletion with loading dependence. Conditional ltaS construction and unquantified ligand abundances limit necessity claims. Table3 values and microgram/mL units were visually checked. Referenced Table4 is absent from this manuscript. |
| publication | https://link.springer.com/article/10.1007/s00253-012-4200-3; Publisher metadata, abstract and access boundary | context_only | Online12June2012, volume97:3721–3728 in2013. Subscription full text was not accessed; accepted manuscript is distinguished from published version. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=224308; Fresh XML TaxId, ScientificName and Rank | supports | 224308 resolves Bacillus subtilis subsp.subtilis str.168 at strain rank; no separate ID for engineered RY1604 is inferred. |

## Limits And Additional Notes

- Accepted manuscript only; final publisher capacity table and raw assay data were unavailable.
- Table3 replication, filter blank correction and direct Tm coordination/ligand-abundance measurements are unreported.
- Empirical isotherm fits and morphology do not establish a unique mechanism; elution is not purified Tm recovery.
- Bounded search result sets and cited-source inspection do not exhaust all later corrections, supplements or alternative mechanisms. Verdict applies to the exact target hash.
- No record, history or dossier edits by this reviewer. Initial failed inspect invocations used a wrong schema path and then an unwritable default UV cache; corrected invocations succeeded and bound unchanged target bytes. Named validation passed independently.
- Twenty acquired source hashes matched the curator receipts. Raw papers remain outside Git. The dated list assertions do not assert latest status in every jurisdiction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080136Z-thulium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of thulium round11 record
started_at: '2026-10-11T07:57:28Z'
finished_at: '2026-10-11T08:01:36Z'
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
verdict: needs_curation
scientific_review: true
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: data/records/thulium.yaml
    sha256: d498820bc424bbdcf22ede740759d950328f8cad47ef14aa762be06c6a9c1837
    role: target
  - path: history/records/thulium/2026-10-11T075320Z-codex-34a805.yaml
    sha256: 16ede09afc0dfa37afe3846b54b626fcb3ccc95c39eb0dc759c4fc52dbccb082
    role: context
  - path: research/ingests/round11-lu-tm-pm-20261011.json
    sha256: f051782badf744dcb00ec98fec77177cc09990945b9f8db3e227f6cac917522a
    role: context
  - path: research/ingests/round11-lu-tm-pm-20261011.md
    sha256: 090a4fda9a7fc5d47110fc7f200ffd4088cbf091564b8d07ea5a8d475e1ce7a2
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:thulium
  path: data/records/thulium.yaml
  label: Thulium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained native record
scope:
  description: All scientific and provenance fields of this named record; source-specific
    identity, criticality and accepted experimental evidence. Deferred literature
    is context only.
  selection: Assigned named record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:thulium
checks:
- check_id: named
  name: Reviewer named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/lutetium.yaml data/records/thulium.yaml data/records/promethium.yaml
  status: passed
  required: true
  summary: Reviewer session5351 terminal0; 3 records checked, 0 failed.
  scope_note: /private/tmp/cmm-round11-independent-lu-tm-pm-validate.log; scientific
    truth is not established by structural validation.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:thulium
- check_id: batch
  name: Parent full native batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Parent session54253 terminal0 confirmed; reviewer read complete log:307
    passed,3 skipped in50.77s;71 records and82 histories valid.
  scope_note: /private/tmp/cmm-round11-batch-check.log; scientific truth is not established
    by structural validation.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:thulium
- check_id: nonempty
  name: Parent nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Parent session22172 terminal0 confirmed; reviewer read complete log:71
    records checked,0 failed.
  scope_note: /private/tmp/cmm-round11-batch-validation.log; scientific truth is not
    established by structural validation.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:thulium
- check_id: history
  name: Parent trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  status: passed
  required: true
  summary: Parent session72936 terminal0 confirmed; reviewer read complete log:82
    histories checked,0 errors.
  scope_note: /private/tmp/cmm-round11-batch-history.log; scientific truth is not
    established by structural validation.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  target_ids:
  - cmmmech:thulium
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/thulium.yaml
  locator: Entire frozen native record, linked CREATE history, shared MD/JSON dossier
    and schema
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Exact inspected target hash agrees with the curator freeze. Sidecar actor
    codex/GPT-6/codex, actual CREATE time and issue44 linkage agree with the later,
    separate inline event.
  snapshot_sha256: d498820bc424bbdcf22ede740759d950328f8cad47ef14aa762be06c6a9c1837
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33380/
  locator: Fresh public API chebi_accession, name and chemical_data fields
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Independent fresh HTTP200 API resolution identifies thulium atom, formula
    Tm, charge zero. The identifier denotes an elemental root, not the experimental
    ion, isotope or salt.
  snapshot_sha256: 866fda43a90315d2ba1942a1a1591a155baa37999017a17220b78c887ad5369e
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: US DOI/USGS final notice, 7 November2025, 90FR50494–50497; Thulium commodity
    row
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Independent live notice and retained authority HTML confirm the named commodity
    in Final2025 list. Adjacent Yes describes byproduct status. The experimental chloride
    feed does not itself become a designated mineral.
  snapshot_sha256: f9d7bdc090fcdfa861c220efbcbddd889efda4fe005800a11906532427ffade0
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round11-batch-check.log
  locator: Complete batch, nonempty, history logs plus reviewer named validation
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Actual logs were read independently; precise commands and terminal results
    are reported under checks. Canonical history and inline events are distinct provenance.
  snapshot_sha256: e46b17911b81a267dd243f56590c3279ab414beda1327dc9f10f084ed732196e
- evidence_id: search
  kind: search
  reference: Bounded independent web queries and scoped local trees
  locator: First returned web result sets, 11October2026; exact identity/DOI local
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
  reference: https://soar-ir.repo.nii.ac.jp/records/13337
  locator: Deposited24-page accepted manuscript; methods pp5–9, results/discussion
    pp10–14; Tables1/3 pp19/21 and all figures pp22–24 visually
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: Boiled and freeze-dried parent/mutant powders show Tm depletion with loading
    dependence. Conditional ltaS construction and unquantified ligand abundances limit
    necessity claims. Table3 values and microgram/mL units were visually checked.
    Referenced Table4 is absent from this manuscript.
  snapshot_sha256: 7117a19b1a67bc808aa58e61ad3fbc4030dd4c0d6d6a80b4d71b6ae073a34cb2
- evidence_id: publication
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s00253-012-4200-3
  locator: Publisher metadata, abstract and access boundary
  accessed_at: '2026-10-11T08:01:04Z'
  support: context_only
  summary: Online12June2012, volume97:3721–3728 in2013. Subscription full text was
    not accessed; accepted manuscript is distinguished from published version.
- evidence_id: taxonomy
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=224308
  locator: Fresh XML TaxId, ScientificName and Rank
  accessed_at: '2026-10-11T08:01:04Z'
  support: supports
  summary: 224308 resolves Bacillus subtilis subsp.subtilis str.168 at strain rank;
    no separate ID for engineered RY1604 is inferred.
  snapshot_sha256: a7274328febb0c8ea55df921fc5d3ded73d98cf0e5f10a780a882abb48cd2e8b
assessments:
- assessment_id: identity-grounding
  area: identity
  topic: Element versus experimental form and list scope
  outcome: supported
  summary: Verified element identity and explicit dated criticality remain distinct
    from ions, host minerals, isotope tracers and commodity mixtures.
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - record
  - identity
  - criticality
  dimensions:
  - name: material-form
    value: Thulium elemental root; CHEBI:33380
    definition: Neutral atomic identity grounds the element record.
    evidence_ids:
    - identity
  - name: criticality
    value: United States DOI/USGS; Final2025 List of Critical Minerals; 7November2025
    definition: Dated source-specific designation.
    evidence_ids:
    - criticality
- assessment_id: assay
  area: evidence
  topic: Prepared bacterial powder adsorption and acidic elution
  outcome: supported
  summary: Experimental form and measured endpoint are accurately scoped; necessity
    wording is handled separately.
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - record
  - primary
  - taxonomy
  dimensions:
  - name: organism
    value: Parent B.subtilis168 and engineered RY1604
    definition: NCBITaxon224308 denotes parent; conditional ltaS plus three deletions.
    evidence_ids:
    - primary
    - taxonomy
  - name: biomass-state
    value: Boiled20min, washed, freeze-dried, crushed/sieved53–100micrometres
    definition: Inactive material; no living metabolism claim.
    evidence_ids:
    - primary
  - name: conditions
    value: 20mg/20mL; Tm20micrograms/mL; pH3,25C,10rpm,30min
    definition: Synthetic chloride feed;7micrometre filter then centrifugation, ICP-AES.
    evidence_ids:
    - primary
  - name: controls
    value: WT comparator; filter adsorption below10%
    definition: Blank correction and replicated Table3 uncertainty unspecified; no
      complemented adsorption test.
    evidence_ids:
    - primary
  - name: outcome
    value: 90%WT/74%defective at20micrograms/mL;35%/29% at100micrograms/mL
    definition: Source Table3 feed-depletion percentages, not isolated-metal yield.
    evidence_ids:
    - primary
  - name: elution
    value: Two20mL portions2.7M nitric acid; greater94% stated across adsorbed REEs
    definition: Adsorbed-ion denominator, not Tm feed recovery; no per-element elution
      table.
    evidence_ids:
    - primary
  - name: deployment
    value: Laboratory synthetic feed and prepared powder
    definition: No ore or industrial operation demonstrated.
    evidence_ids:
    - primary
- assessment_id: causality
  area: consistency
  topic: Necessity is not established by a defective preparation
  outcome: concern
  summary: One sentence asserts LTA is not necessary despite unquantified residual
    LTA.
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - record
  - primary
  details: RY1604 retains inducible ltaS; preparation removes IPTG for a limited cultivation
    period. The manuscript does not directly measure LTA absence in the tested powder
    and says ligand abundance ratios were unquantified. The observed residual depletion
    alone cannot decide necessity.
- assessment_id: provenance
  area: provenance
  topic: CREATE provenance and frozen bytes
  outcome: supported
  summary: Actual sidecar and separate inline CREATE event are consistent; no review-derived
    curation is backdated.
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - record
  - validation
findings:
- finding_id: F1
  issue_key: thulium-lta-necessity-overstatement
  category: evidence
  severity: minor
  native_severity: minor
  normalization_reason: Bounded causal wording overstatement in one sentence; organism,
    prepared material, numerical outcomes and multiple surrounding limits are otherwise
    supported. It does not invalidate the narrow biosorption observation.
  status: open
  certainty: confirmed
  title: Residual adsorption does not establish that LTA is unnecessary
  description: The mechanism description says LTA is not an exclusive or necessary
    binding route. Conditional ltaS expression after IPTG removal and unmeasured residual
    LTA do not prove complete ligand absence. Preserve the residual adsorption observation
    and state that the comparison cannot establish exclusive LTA causality or quantify
    its contribution. The same overstatement occurs in the shared dossier.
  target_ids:
  - cmmmech:thulium
  field_paths:
  - mechanisms[0].description
  evidence_ids:
  - record
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained native record
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round11-lu-tm-pm-20261011.md
    role: maintained research dossier
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/45
actions:
- action_id: A1
  description: Narrow the record and matching dossier language to the observed defective-biomass
    comparison; append actual EDIT provenance and independently reassess the final
    bytes.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:thulium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained native record
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round11-lu-tm-pm-20261011.md
    role: maintained research dossier
  acceptance_checks:
  - No claim that LTA is unnecessary without direct absence/complementation evidence.
  - Retain observed WT/mutant values, conditional genotype, source yvgJ/yvyJ discrepancy
    and uncertainty.
  - Run affected named validation and full required gates; save successor review resolving
    this exact occurrence.
limitations:
- Accepted manuscript only; final publisher capacity table and raw assay data were
  unavailable.
- Table3 replication, filter blank correction and direct Tm coordination/ligand-abundance
  measurements are unreported.
- Empirical isotherm fits and morphology do not establish a unique mechanism; elution
  is not purified Tm recovery.
- Bounded search result sets and cited-source inspection do not exhaust all later
  corrections, supplements or alternative mechanisms. Verdict applies to the exact
  target hash.
notes:
- No record, history or dossier edits by this reviewer. Initial failed inspect invocations
  used a wrong schema path and then an unwritable default UV cache; corrected invocations
  succeeded and bound unchanged target bytes. Named validation passed independently.
- Twenty acquired source hashes matched the curator receipts. Raw papers remain outside
  Git. The dated list assertions do not assert latest status in every jurisdiction.
summary: 'Element identity, dated US designation and prepared-powder depletion/elution
  observations are supported. One minor mechanistic overstatement needs correction:
  residual binding in an LTA-defective preparation does not establish that LTA is
  unnecessary when residual LTA is unquantified.'
```
