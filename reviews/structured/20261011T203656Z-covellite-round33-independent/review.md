# Independent adversarial review of covellite phase-formation evidence

- Review: 20261011T203656Z-covellite-round33-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T20:32:25.437724Z
- Finished UTC: 2026-10-11T20:36:56.698517Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record admits supported phase formation and explicitly retains its control, accounting and purity limitations. No corrective record defect was found; source uncertainties are not fabricated curation findings.

## Scope And Provenance

All fields of one new record, its exact identity, accepted experiment and CREATE history.

Selection: Round33 new mineral record curated by another agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bee4f42bb622ae0a0999f8f3e3dac31f14282278.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:covellite | data/records/covellite.yaml | maintained | Covellite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:covellite | Root executed; one record, zero failures. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final cohort batch | passed | True | cmmmech:covellite | /private/tmp/cmm-round33-final-batch.log SHA256 4ca5dc5133c70847781db60f3ac8024963b461a718c7fc9083c43e10ec5d4d32; uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 129.87s (0:02:09)<br>Checked 190 record(s); 0 failed.<br>Checked 219 history record(s); 0 error(s).<br> |
| Final cohort nonempty | passed | True | cmmmech:covellite | /private/tmp/cmm-round33-final-nonempty.log SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299; Checked 190 record(s); 0 failed.<br> |
| Final cohort history | passed | True | cmmmech:covellite | /private/tmp/cmm-round33-final-history.log SHA256 5fdfb5898956d9c86e8d8c3976c1c07f567b349cb0cbeae4a4385905857b70a1; Checked 219 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Material identity and process owner

identity: supported. Targets: cmmmech:covellite.

Covellite mineral species is distinguished from copper element, dissolved ions, mixed feeds and unspecified manufactured CuS; crystallographic phase identification supports the product claim.

### Organism, substrate, conditions and controls

evidence: supported. Targets: cmmmech:covellite.

Unresolved living consortium produces H2S upstream; no taxa are guessed. Synthetic Cu-free feed and real drainage occupy different vessels. Missing control, replicate, H2S and off-line temperature information stays explicit.

### Phases, measurements and source contradictions

evidence: supported. Targets: cmmmech:covellite.

XRD and lattice parameters support a covellite phase, not quantified bulk purity. Impossible wt-percent totals and mass-versus-molar ratios are rejected as valid composition. Dv90 values are volume quantiles, not crystallite size or recovery fractions.

### Causality and deployment

evidence: supported. Targets: cmmmech:covellite.

Biogenic sulfide provision is distinguished from chemical precipitation. Color, pH and settling cannot quantify removal. No isolation of microbial superiority, copper balance, product mass or industrial deployment is claimed.

### Sources, curation history and scientific-review limits

provenance: supported. Targets: cmmmech:covellite.

Fresh independent evidence assessment matches frozen record and actual history. Acquired originals were shared with curator and are retained outside Git; independent interpretation and version checks are disclosed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/covellite.yaml; All frozen fields | supports | Mineral identity and a separate upstream microbial/downstream chemical process; no invented community identifiers. |
| primary | https://doi.org/10.3390/met9020206; Complete nine-page unversioned publisher PDF and XML; Figures 1-5, Tables 1-4, Sections 2-4 | supports | Root independently read full scientific text and visually examined all five figures and four tables. Source supports recovered covellite-phase solids after gas exposure, not a quantified yield or pure bulk product. Reactor and off-line conditions, unknown controls/replication and composition problems match the record. |
| authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Page 50 Covellite row; pages 1-2 field definitions | supports | CuS, grandfathered G, original description 1832. No approval number or criticality inherited. Curator PDF is byte-identical to the independent root acquisition for pyrite. |
| version | https://mdpi-res.com/d_attachment/metals/metals-09-00206/article_deploy/metals-09-00206-v2.pdf?version=1550831691; Independently opened updated publisher PDF, pages 3-6, especially Table 3 on page 5 | supports | The web-accessed v2 retains Cu/S 87.67/73.99 and 70.97/106.08 wt-percent entries and 1.18/0.67 ratio prose. This verifies the inconsistency is not only in the retained unversioned PDF. No local v2 download or visual screenshot inspection is claimed. |
| search | Independent web search 2026-10-11; Returned result pages and original XML supplement inventory | supports | No specific correction or retraction identified in bounded DOI/title results. Publisher notes indexed an updated version on 22 February 2019; current notes open returned an internal error, but the v2 original opened. XML and whole PDF contain no supplementary-material section. |
| history | history/records/covellite/2026-10-11T203120Z-codex-db7cc3.yaml; CREATE sidecar and distinct inline event | supports | Actual actor, timestamp, maintained path and completed curation scope match. History correctly says independent review and batch gates were pending when created. |

## Limits And Additional Notes

- No matched uninoculated reactor, gas-only blank or reagent-H2S comparator; biological superiority is unestablished.
- Unknown independent replication, H2S dose, hydraulic residence and off-line temperature/mixing constrain reproducibility.
- EDXRF normalization and ratio basis remain unresolved; XRD detection limits and amorphous fractions are unknown.
- No final dissolved Cu, solid mass or whole-feed balance; no validated copper recovery yield or industrial deployment.
- Updated v2 was inspected through web text; locally retained unversioned PDF and original XML were read and figures visually reviewed. No raw diffraction reanalysis or ICDD database access is claimed.
- Notice search was bounded; the absence of a returned notice is not an exhaustive clearance.
- No maintained correction was needed and no issue was invented from limits already explicit in the record.
- Final batch receipts describe actual completed commands and the same frozen record bytes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T203656Z-covellite-round33-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial review of covellite phase-formation evidence
started_at: '2026-10-11T20:32:25.437724Z'
finished_at: '2026-10-11T20:36:56.698517Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The record, history and source dossier were authored by /root/round27_packaging.
    Root captured the frozen target and input hashes before final assessment, independently
    read the primary text, figures, tables and authority, and checked the updated
    original version. Shared curator-acquired originals and preliminary routing are
    disclosed; root did not author or edit the record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record admits supported phase formation and explicitly retains its control,
  accounting and purity limitations. No corrective record defect was found; source
  uncertainties are not fabricated curation findings.
source:
  git_revision: bee4f42bb622ae0a0999f8f3e3dac31f14282278
  state: working_tree
  inputs:
  - path: data/records/covellite.yaml
    sha256: 090a48e7e40c145d9daef4b9ca4c4be5e74e5e454c6f0862c3c0548c5b9c222a
    role: target
  - path: history/records/covellite/2026-10-11T203120Z-codex-db7cc3.yaml
    sha256: c4f7c34ac441bd3d8d80f8dcb7fa30e180c2b89728049214de5a06e459a21b81
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields of one new record, its exact identity, accepted experiment
    and CREATE history.
  selection: Round33 new mineral record curated by another agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:covellite
  exclusions:
  - target: Deferred natural-mineral bioleaching studies and 2020 chemical comparator
    reason: Not adopted as record mechanisms; acquisition/research leads remain separate.
targets:
- target_id: cmmmech:covellite
  path: data/records/covellite.yaml
  label: Covellite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/covellite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/covellite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; one record, zero failures. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:covellite
- check_id: batch
  name: Final cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round33-final-batch.log SHA256 4ca5dc5133c70847781db60f3ac8024963b461a718c7fc9083c43e10ec5d4d32;
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 129.87s (0:02:09)

    Checked 190 record(s); 0 failed.

    Checked 219 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:covellite
- check_id: nonempty
  name: Final cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round33-final-nonempty.log SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299;
    Checked 190 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:covellite
- check_id: history
  name: Final cohort history
  command: uv run --locked cmmmech validate-history --base bee4f42bb622ae0a0999f8f3e3dac31f14282278
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: '/private/tmp/cmm-round33-final-history.log SHA256 5fdfb5898956d9c86e8d8c3976c1c07f567b349cb0cbeae4a4385905857b70a1;
    Checked 219 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:covellite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/covellite.yaml
  locator: All frozen fields
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: Mineral identity and a separate upstream microbial/downstream chemical
    process; no invented community identifiers.
  snapshot_sha256: 090a48e7e40c145d9daef4b9ca4c4be5e74e5e454c6f0862c3c0548c5b9c222a
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/met9020206
  locator: Complete nine-page unversioned publisher PDF and XML; Figures 1-5, Tables
    1-4, Sections 2-4
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: Root independently read full scientific text and visually examined all
    five figures and four tables. Source supports recovered covellite-phase solids
    after gas exposure, not a quantified yield or pure bulk product. Reactor and off-line
    conditions, unknown controls/replication and composition problems match the record.
  snapshot_sha256: 0217821d7f1fc4cbf92b98ab5598eb9738232b12df8d92799c702c3563967bcd
- evidence_id: authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Page 50 Covellite row; pages 1-2 field definitions
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: CuS, grandfathered G, original description 1832. No approval number or
    criticality inherited. Curator PDF is byte-identical to the independent root acquisition
    for pyrite.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: version
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/metals/metals-09-00206/article_deploy/metals-09-00206-v2.pdf?version=1550831691
  locator: Independently opened updated publisher PDF, pages 3-6, especially Table
    3 on page 5
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: The web-accessed v2 retains Cu/S 87.67/73.99 and 70.97/106.08 wt-percent
    entries and 1.18/0.67 ratio prose. This verifies the inconsistency is not only
    in the retained unversioned PDF. No local v2 download or visual screenshot inspection
    is claimed.
- evidence_id: search
  kind: search
  reference: Independent web search 2026-10-11
  locator: Returned result pages and original XML supplement inventory
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: No specific correction or retraction identified in bounded DOI/title results.
    Publisher notes indexed an updated version on 22 February 2019; current notes
    open returned an internal error, but the v2 original opened. XML and whole PDF
    contain no supplementary-material section.
  search_scope: 'Exact queries: "10.3390/met9020206" correction retraction erratum;
    "Covellite" "Production from a Real" "correction". Returned pages only, no exhaustive
    notice clearance.'
- evidence_id: history
  kind: record_content
  reference: history/records/covellite/2026-10-11T203120Z-codex-db7cc3.yaml
  locator: CREATE sidecar and distinct inline event
  accessed_at: '2026-10-11T20:36:56.698517Z'
  support: supports
  summary: Actual actor, timestamp, maintained path and completed curation scope match.
    History correctly says independent review and batch gates were pending when created.
  snapshot_sha256: c4f7c34ac441bd3d8d80f8dcb7fa30e180c2b89728049214de5a06e459a21b81
assessments:
- assessment_id: identity
  area: identity
  topic: Material identity and process owner
  outcome: supported
  summary: Covellite mineral species is distinguished from copper element, dissolved
    ions, mixed feeds and unspecified manufactured CuS; crystallographic phase identification
    supports the product claim.
  target_ids:
  - cmmmech:covellite
  evidence_ids:
  - record
  - authority
  - primary
  dimensions:
  - name: material_kind
    value: mineral
    definition: IMA covellite species; no copper criticality inherited.
    evidence_ids:
    - authority
    - record
- assessment_id: conditions
  area: evidence
  topic: Organism, substrate, conditions and controls
  outcome: supported
  summary: Unresolved living consortium produces H2S upstream; no taxa are guessed.
    Synthetic Cu-free feed and real drainage occupy different vessels. Missing control,
    replicate, H2S and off-line temperature information stays explicit.
  target_ids:
  - cmmmech:covellite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biomass
    value: Living, unresolved acidophilic sulfate-reducing consortium
    definition: Immobilized upstream on glass beads; no demonstrated direct cellular
      precipitation in the off-line bottle.
    evidence_ids:
    - primary
  - name: scale
    value: Laboratory
    definition: 2.3 L sulfide bioreactor and separate 1 L mine-drainage precipitation
      bottle.
    evidence_ids:
    - primary
- assessment_id: outcome
  area: evidence
  topic: Phases, measurements and source contradictions
  outcome: supported
  summary: XRD and lattice parameters support a covellite phase, not quantified bulk
    purity. Impossible wt-percent totals and mass-versus-molar ratios are rejected
    as valid composition. Dv90 values are volume quantiles, not crystallite size or
    recovery fractions.
  target_ids:
  - cmmmech:covellite
  evidence_ids:
  - record
  - primary
  - version
- assessment_id: scope
  area: evidence
  topic: Causality and deployment
  outcome: supported
  summary: Biogenic sulfide provision is distinguished from chemical precipitation.
    Color, pH and settling cannot quantify removal. No isolation of microbial superiority,
    copper balance, product mass or industrial deployment is claimed.
  target_ids:
  - cmmmech:covellite
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Sources, curation history and scientific-review limits
  outcome: supported
  summary: Fresh independent evidence assessment matches frozen record and actual
    history. Acquired originals were shared with curator and are retained outside
    Git; independent interpretation and version checks are disclosed.
  target_ids:
  - cmmmech:covellite
  evidence_ids:
  - record
  - history
  - search
findings: []
actions: []
limitations:
- No matched uninoculated reactor, gas-only blank or reagent-H2S comparator; biological
  superiority is unestablished.
- Unknown independent replication, H2S dose, hydraulic residence and off-line temperature/mixing
  constrain reproducibility.
- EDXRF normalization and ratio basis remain unresolved; XRD detection limits and
  amorphous fractions are unknown.
- No final dissolved Cu, solid mass or whole-feed balance; no validated copper recovery
  yield or industrial deployment.
- Updated v2 was inspected through web text; locally retained unversioned PDF and
  original XML were read and figures visually reviewed. No raw diffraction reanalysis
  or ICDD database access is claimed.
- Notice search was bounded; the absence of a returned notice is not an exhaustive
  clearance.
notes:
- No maintained correction was needed and no issue was invented from limits already
  explicit in the record.
- Final batch receipts describe actual completed commands and the same frozen record
  bytes.
links:
- https://doi.org/10.3390/met9020206
tags:
- round33
- independent
- scientific
- covellite
```
