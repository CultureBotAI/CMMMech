# Independent scientific review of biogas-desulfurization sulfur residue

- Review: 20261011T150333Z-biogas-desulfurization-sulfur-residue-round25-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T15:01:07.288134Z
- Finished UTC: 2026-10-11T15:03:33.514180Z
- Reviewer: Codex /root/round24_copper_slag (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No actionable finding in the frozen record. Biogas-desulfurization powder and bounded mixed-culture acid production are supported, with unresolved DSM 1927 species identity and serial-cycle sulfur accounting explicitly retained.

## Scope And Provenance

Entire maintained resource record, all mechanism/identity/evidence claims and attached actual curation provenance.

Selection: One assigned newly curated record, independently assessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baedff25eafad1516270916a651af6754ffa5996.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:biogas-desulfurization-sulfur-residue | data/records/biogas-desulfurization-sulfur-residue.yaml | maintained | Biogas-desulfurization sulfur residue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:biogas-desulfurization-sulfur-residue | Executed independently by reviewer. /private/tmp/cmm-round25-sulfur-review-validation.log:<br>Checked 1 record(s); 0 failed.<br> |
| Native full checks | passed | True | cmmmech:biogas-desulfurization-sulfur-residue | Executed by root for this batch; actual terminal receipt and log independently inspected. /private/tmp/cmm-round25-final-batch.log:<br>uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 98.72s (0:01:38)<br>Checked 165 record(s); 0 failed.<br>Checked 186 history record(s); 0 error(s).<br> |
| Nonempty corpus validation | passed | True | cmmmech:biogas-desulfurization-sulfur-residue | Executed by root for this batch; actual terminal receipt and log independently inspected. /private/tmp/cmm-round25-final-require.log:<br>Checked 165 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:biogas-desulfurization-sulfur-residue | Executed by root for this batch; actual terminal receipt and log independently inspected. /private/tmp/cmm-round25-final-history.log:<br>Checked 186 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Actual feed identity and criticality boundaries

identity: supported. Targets: cmmmech:biogas-desulfurization-sulfur-residue.

The Danish desulfurization-derived sulfur powder is a process-defined secondary resource, distinct from the element sulfur, commercial acid and downstream battery black mass. Other records using a related sulfur nutrient do not create duplicate resource roots.

### Qualified microbial process, source controls and measured outcome

evidence: supported. Targets: cmmmech:biogas-desulfurization-sulfur-residue.

Methods and observed acidic liquor support a conditional mixed-culture transformation observation. Exact first-member identity, live-cell necessity and source superiority remain unproven. Carryover and repeated sulfur additions prevent deriving a single-charge conversion fraction.

### Independent exact-state scientific assessment and actual curation history

provenance: supported. Targets: cmmmech:biogas-desulfurization-sulfur-residue.

After preliminary orientation, canonical inspect captured the exact target and maintained context before detailed assessment. Author and reviewer are different agents; no reviewed record or history was edited. Final input hashes match the captured state and current successful gate receipt.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/biogas-desulfurization-sulfur-residue.yaml; Entire frozen record and attached CREATE history | supports | No actionable finding in the frozen record. Biogas-desulfurization powder and bounded mixed-culture acid production are supported, with unresolved DSM 1927 species identity and serial-cycle sulfur accounting explicitly retained. |
| primary | https://doi.org/10.3389/fmicb.2026.1921494; Sections 2.1-2.4 and 3.1-3.3, conclusion/data statement; Table 1 and Figures 1-4 visually inspected on PDF pages 3 and 5-8. | supports | Section 2.2 explicitly supplies Danish desulfurization powder, a 2-L vessel with 1.8-L working volume, 1% w/v sulfur, pH 3.5, 30 degrees C, 250 rpm and 50 L/h air. Ten serial cycles withdraw 1.2 L and retain 0.6 L. The 0.63-M, pH-0.44 endpoints are measured liquor descriptors, not a conversion fraction or sulfur purity. No complete powder composition, per-cycle sulfur mass inventory, independent acid-production replication or uninoculated residue control is supplied. Those gaps are correctly retained. |
| counter | https://doi.org/10.3389/fmicb.2026.1921494; Source conflicts, controls and causal/deployment limits; primary PDF figures and narrative | partial | All four figures and Table 1 concern downstream NMC battery assays, not sulfur-resource conversion yield. Figure 2 shows no biosurfactant advantage, and Figure 3 includes high Li/Mn endpoints without peroxide. SEM-EDS non-detection in Figure 4 cannot certify complete removal or isolated products. The medium is source-labelled basalt salt medium and its referenced paper concerns sulfate reducers; the record does not invent a repaired recipe. Prior-study commercial-sulfur comparisons are not experiments performed here. |
| authority | https://www.dsmz.de/collection/catalogue/details/culture/DSM-1927; Live authority pages independently checked 2026-10-11 | supports | Independently opened live DSMZ catalogues. DSM 1927 is Acidithiobacillus ferrooxidans F221, conflicting with the paper A. thiooxidans label; DSM 9466 is A. caldus C-SH12. Neither catalogue establishes which stock was actually inoculated or which member caused conversion. Omitting a mechanism organism CURIE and preserving the conflict avoids an invented correction. |
| search | https://doi.org/10.3389/fmicb.2026.1921494; Exact DOI/title, correction/retraction, source-link and repository searches | context_only | Reviewer queried exact DOI and exact DOI plus correction OR retraction OR erratum in first returned web sets without filters or pagination. No matching notice appeared in those bounded sets. LED publisher open returned an internal error, while indexed primary/PubMed metadata matched the complete acquired PDF; Frontiers live primary HTML was available. Primary PDF and acquired HTML link inventory yielded no study-specific supplement in this scope; raw data were not requested from authors. No universal absence claim. |
| gates | /private/tmp/cmm-round25-final-batch-terminal.json; Actual current batch receipt/logs, canonical inspect and matching final SHA-256 | supports | Root batch gates passed 308 tests with 3 skips, 165 records and 186 histories. Named validation was independently run by reviewer. All inspected local input hashes and gate target hashes were rechecked immediately before saving. |

## Limits And Additional Notes

- DSM 1927 species conflict remains unresolved; author or stock evidence is needed before assigning exact culture membership.
- Complete residue composition, purity and drying history are unspecified; medium recipe is referenced rather than fully supplied.
- Retained material, repeated inputs and missing cycle inventories preclude a closed sulfur balance. The acid-production arm lacks independent replication and matched uninoculated controls.
- Downstream battery assays and a nominal 1-L vessel are laboratory context. Prior-paper sulfur advantages, economic viability and life-cycle benefits are not demonstrated by this experiment.
- Correction/supplement and dedup searches are bounded. Full source files were reused from this batch author acquisition, not independently redownloaded; no unpublished raw data were obtained.
- No corrections to the reviewed scientific record were required. A qualified pass preserves the stated scientific questions; it does not resolve source errors or authorize deployment.
- Batch gates were run by root and read independently; named validations were executed by this reviewer. All commands used the prepared project environment and offline UV cache.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T150333Z-biogas-desulfurization-sulfur-residue-round25-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of biogas-desulfurization sulfur residue
started_at: '2026-10-11T15:01:07.288134Z'
finished_at: '2026-10-11T15:03:33.514180Z'
reviewer:
  identity: Codex /root/round24_copper_slag
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round24_identity_frontier authored this record.
    This reviewer independently read the primary methods/results and all relevant
    figure/table pixels, checked live authorities and judged the frozen bytes without
    editing them. Shared workspace, curator dossier and source downloads are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: No actionable finding in the frozen record. Biogas-desulfurization powder
  and bounded mixed-culture acid production are supported, with unresolved DSM 1927
  species identity and serial-cycle sulfur accounting explicitly retained.
source:
  git_revision: baedff25eafad1516270916a651af6754ffa5996
  state: working_tree
  inputs:
  - path: data/records/biogas-desulfurization-sulfur-residue.yaml
    sha256: 494b43f384f2a9a2463c774ba33fd028c447ae9b6550eda78d0aaf9de1ccfebf
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/biogas-desulfurization-sulfur-residue/2026-10-11T145542Z-codex-606521.yaml
    sha256: 748a71915513e47ad49620ebafef90968edf75c6123095752d69bd6c706379ef
    role: context
  - path: research/ingests/round25-frontier-sources-20261011.json
    sha256: 2b2ce46ac8521b499c602cfb51df809ab29abebdc8399bc626b8360eccd5f6b4
    role: context
  - path: research/ingests/round25-frontier-sources-20261011.md
    sha256: 3e8cf73dce0ec7eac6065a42a90bcc78060ae161bde2f33a092165377107d09e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire maintained resource record, all mechanism/identity/evidence
    claims and attached actual curation provenance.
  selection: One assigned newly curated record, independently assessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
  exclusions:
  - target: Unreported raw data, author correspondence and experimental stock authentication
    reason: These were not available in the inspected publications/routes and were
      not invented or requested.
targets:
- target_id: cmmmech:biogas-desulfurization-sulfur-residue
  path: data/records/biogas-desulfurization-sulfur-residue.yaml
  label: Biogas-desulfurization sulfur residue
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/biogas-desulfurization-sulfur-residue.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/biogas-desulfurization-sulfur-residue.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Executed independently by reviewer. /private/tmp/cmm-round25-sulfur-review-validation.log:

    Checked 1 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Executed by root for this batch; actual terminal receipt and log independently
    inspected. /private/tmp/cmm-round25-final-batch.log:

    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 98.72s (0:01:38)

    Checked 165 record(s); 0 failed.

    Checked 186 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
- check_id: require
  name: Nonempty corpus validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Executed by root for this batch; actual terminal receipt and log independently
    inspected. /private/tmp/cmm-round25-final-require.log:

    Checked 165 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base baedff25eafad1516270916a651af6754ffa5996
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Executed by root for this batch; actual terminal receipt and log independently
    inspected. /private/tmp/cmm-round25-final-history.log:

    Checked 186 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/biogas-desulfurization-sulfur-residue.yaml
  locator: Entire frozen record and attached CREATE history
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: supports
  summary: No actionable finding in the frozen record. Biogas-desulfurization powder
    and bounded mixed-culture acid production are supported, with unresolved DSM 1927
    species identity and serial-cycle sulfur accounting explicitly retained.
  snapshot_sha256: 494b43f384f2a9a2463c774ba33fd028c447ae9b6550eda78d0aaf9de1ccfebf
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2026.1921494
  locator: Sections 2.1-2.4 and 3.1-3.3, conclusion/data statement; Table 1 and Figures
    1-4 visually inspected on PDF pages 3 and 5-8.
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: supports
  summary: Section 2.2 explicitly supplies Danish desulfurization powder, a 2-L vessel
    with 1.8-L working volume, 1% w/v sulfur, pH 3.5, 30 degrees C, 250 rpm and 50
    L/h air. Ten serial cycles withdraw 1.2 L and retain 0.6 L. The 0.63-M, pH-0.44
    endpoints are measured liquor descriptors, not a conversion fraction or sulfur
    purity. No complete powder composition, per-cycle sulfur mass inventory, independent
    acid-production replication or uninoculated residue control is supplied. Those
    gaps are correctly retained.
  snapshot_sha256: e9af35f1ad449ff6591356148d172a8a2bb3feaced654bd8a779650ed6647c97
- evidence_id: counter
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2026.1921494
  locator: Source conflicts, controls and causal/deployment limits; primary PDF figures
    and narrative
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: partial
  summary: All four figures and Table 1 concern downstream NMC battery assays, not
    sulfur-resource conversion yield. Figure 2 shows no biosurfactant advantage, and
    Figure 3 includes high Li/Mn endpoints without peroxide. SEM-EDS non-detection
    in Figure 4 cannot certify complete removal or isolated products. The medium is
    source-labelled basalt salt medium and its referenced paper concerns sulfate reducers;
    the record does not invent a repaired recipe. Prior-study commercial-sulfur comparisons
    are not experiments performed here.
  snapshot_sha256: e9af35f1ad449ff6591356148d172a8a2bb3feaced654bd8a779650ed6647c97
- evidence_id: authority
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-1927
  locator: Live authority pages independently checked 2026-10-11
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: supports
  summary: Independently opened live DSMZ catalogues. DSM 1927 is Acidithiobacillus
    ferrooxidans F221, conflicting with the paper A. thiooxidans label; DSM 9466 is
    A. caldus C-SH12. Neither catalogue establishes which stock was actually inoculated
    or which member caused conversion. Omitting a mechanism organism CURIE and preserving
    the conflict avoids an invented correction.
- evidence_id: search
  kind: search
  reference: https://doi.org/10.3389/fmicb.2026.1921494
  locator: Exact DOI/title, correction/retraction, source-link and repository searches
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: context_only
  summary: Reviewer queried exact DOI and exact DOI plus correction OR retraction
    OR erratum in first returned web sets without filters or pagination. No matching
    notice appeared in those bounded sets. LED publisher open returned an internal
    error, while indexed primary/PubMed metadata matched the complete acquired PDF;
    Frontiers live primary HTML was available. Primary PDF and acquired HTML link
    inventory yielded no study-specific supplement in this scope; raw data were not
    requested from authors. No universal absence claim.
  search_scope: rg --no-ignore --hidden --follow for 04937-x, 1921494, discarded.?LED
    and biogas.desulfur under data/records, research, reviews and history; result
    /private/tmp/cmm-round25-led-sulfur-review-dedup.txt. Read named curator raw acquisition/link
    inventories and full primary files. Related historical discovery and sulfur-nutrient
    usage were distinguished from resource roots; unrelated home/temp trees excluded.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round25-final-batch-terminal.json
  locator: Actual current batch receipt/logs, canonical inspect and matching final
    SHA-256
  accessed_at: '2026-10-11T15:03:33.514180Z'
  support: supports
  summary: Root batch gates passed 308 tests with 3 skips, 165 records and 186 histories.
    Named validation was independently run by reviewer. All inspected local input
    hashes and gate target hashes were rechecked immediately before saving.
  snapshot_sha256: 1a824b26e98d09ece2c6ff116385fdc5651f4d2de7245d3f3a20c15ac3cc32ce
assessments:
- assessment_id: identity
  area: identity
  topic: Actual feed identity and criticality boundaries
  outcome: supported
  summary: The Danish desulfurization-derived sulfur powder is a process-defined secondary
    resource, distinct from the element sulfur, commercial acid and downstream battery
    black mass. Other records using a related sulfur nutrient do not create duplicate
    resource roots.
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
  evidence_ids:
  - record
  - primary
  - search
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Defined by supported process/manufactured-waste origin, not a constituent
      element or mineral.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No inherited authority, jurisdiction, list or edition claim.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Qualified microbial process, source controls and measured outcome
  outcome: supported
  summary: Methods and observed acidic liquor support a conditional mixed-culture
    transformation observation. Exact first-member identity, live-cell necessity and
    source superiority remain unproven. Carryover and repeated sulfur additions prevent
    deriving a single-charge conversion fraction.
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
  evidence_ids:
  - record
  - primary
  - counter
  - authority
  dimensions:
  - name: organism_strain
    value: Paper labels A. thiooxidans DSM 1927 plus A. caldus DSM 9466; first assignment
      conflicts with DSMZ
    definition: Collection/species labels and experimental authentication are distinct.
    evidence_ids:
    - primary
    - authority
  - name: biomass_state
    value: Living mixed culture during acid production; centrifuged acidic liquor
      used downstream
    definition: A centrifugation step is not independently verified sterility.
    evidence_ids:
    - primary
  - name: pretreatment_conditions
    value: Dried powdered residue, 1% w/v sulfur in 1.8 L, 30 degrees C, 250 rpm,
      50 L/h air, 14-21-day serial cycles
    definition: Parameters are scoped to the selected primary experiment.
    evidence_ids:
    - primary
  - name: controls
    value: No matched uninoculated residue or commercial-sulfur control in this study;
      downstream peroxide/surfactant controls answer a different question
    definition: Comparators limit causal and source-superiority claims.
    evidence_ids:
    - primary
    - counter
  - name: outcome
    value: Reported 0.63-M acidic liquor at pH 0.44; no independently reconstructed
      conversion yield, isolated pure acid or recovered metal product
    definition: Measured solution endpoints are distinct from recovered pure products
      and closed mass balances.
    evidence_ids:
    - primary
    - counter
  - name: deployment
    value: Laboratory
    definition: Industrial feed origin or a nominal 1-L vessel does not establish
      industrial biological operation.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Independent exact-state scientific assessment and actual curation history
  outcome: supported
  summary: After preliminary orientation, canonical inspect captured the exact target
    and maintained context before detailed assessment. Author and reviewer are different
    agents; no reviewed record or history was edited. Final input hashes match the
    captured state and current successful gate receipt.
  target_ids:
  - cmmmech:biogas-desulfurization-sulfur-residue
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- DSM 1927 species conflict remains unresolved; author or stock evidence is needed
  before assigning exact culture membership.
- Complete residue composition, purity and drying history are unspecified; medium
  recipe is referenced rather than fully supplied.
- Retained material, repeated inputs and missing cycle inventories preclude a closed
  sulfur balance. The acid-production arm lacks independent replication and matched
  uninoculated controls.
- Downstream battery assays and a nominal 1-L vessel are laboratory context. Prior-paper
  sulfur advantages, economic viability and life-cycle benefits are not demonstrated
  by this experiment.
- Correction/supplement and dedup searches are bounded. Full source files were reused
  from this batch author acquisition, not independently redownloaded; no unpublished
  raw data were obtained.
notes:
- No corrections to the reviewed scientific record were required. A qualified pass
  preserves the stated scientific questions; it does not resolve source errors or
  authorize deployment.
- Batch gates were run by root and read independently; named validations were executed
  by this reviewer. All commands used the prepared project environment and offline
  UV cache.
tags:
- round25
- independent
- scientific-review
- secondary-resource
```
