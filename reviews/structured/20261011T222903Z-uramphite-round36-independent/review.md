# Independent adversarial review of precipitated uramphite reduction evidence

- Review: 20261011T222903Z-uramphite-round36-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T22:20:31.874565Z
- Finished UTC: 2026-10-11T22:29:03.496777Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The narrow laboratory transformation claim is supported with phase, concentration, source discrepancy and pathway limits preserved. No corrective record defect identified.

## Scope And Provenance

One new uramphite record, all fields, canonical CREATE history and claim-specific primary evidence.

Selection: Independent review of another agent’s round36 record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ef6fdde620a4053fbfff99c51065082dce32d39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:uramphite | data/records/uramphite.yaml | maintained | Uramphite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:uramphite | Checked 1 record(s); 0 failed. |
| Final batch batch | passed | True | cmmmech:uramphite | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 134.59s (0:02:14)<br>Checked 200 record(s); 0 failed.<br>Checked 231 history record(s); 0 error(s).; log SHA256 cac731be567d421580f78dafc063be4b2ca406ca450d98bb15c72eab76e37b57 |
| Final batch nonempty | passed | True | cmmmech:uramphite | Checked 200 record(s); 0 failed.; log SHA256 0ed97773d44e6b06c1b7964ea58e27e8370bf048dd0a7c0384cf9f7681603b10 |
| Final batch history | passed | True | cmmmech:uramphite | Checked 231 history record(s); 0 error(s).; log SHA256 75168340cd2362ddc1a2cc07d98f1a645893ffaa1d3d3f678ad3141c78cf40c4 |

## Scientific And Domain Assessments

### Mineral versus synthetic feed and constituent

identity: supported. Targets: cmmmech:uramphite.

Distinct IMA mineral owner. Assay concerns an abiotic laboratory precipitate assigned by characteristic XRD lines, not a natural uramphite specimen or ore. Uranium/ningyoite identities and inherited criticality are excluded.

### Organism, biomass and assay conditions

evidence: supported. Targets: cmmmech:uramphite.

Fumarate-grown5%inoculum, initialpH7,65C dark static10mL/27mLtubes, uranyl acetate and2.4mMphosphate match primary methods. Species-only grounding is explicit. The3mL/L versus30mmol/L glycerol discrepancy and unclear independent biological replication remain unresolved.

### Phase, controls and pathway

evidence: supported. Targets: cmmmech:uramphite.

Initial yellow phase is XRD-assigned uramphite, reduced gray product ningyoite with U(IV)/phosphate spectroscopy. Uninoculated control preserves U(VI); dissolved uranium pools and no pathway-specific tests prevent exclusive direct-contact or enzyme claims.

### Outcome denominator and null results

evidence: supported. Targets: cmmmech:uramphite.

Reported80–90%concerns assayed U(VI) reduction at1/2.5mM by68h, not mineral-specific dissolution, phase purity or recovery yield. No reduction/growth at5/10mM and Figure3’s separate kinetics are preserved. Figure1D/text describes a crystal mixture.

### History, source reuse and review independence

provenance: supported. Targets: cmmmech:uramphite.

CREATE provenance matches new material owner; the existing ningyoite record represents the same experiment from product perspective, with no claim of independent replication. Root did not author or edit uramphite.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/uramphite.yaml; All frozen fields | supports | Reviewed exact working bytes after native capture. |
| primary | https://doi.org/10.1128/AEM.71.10.6423-6426.2005; Complete pp6423–6426; original Figures1–3 | supports | Independently reread retained complete original and visually inspected all three figures. XRD assigns the yellow starting precipitate to uramphite; XAS and XRD support reduced phosphate product. Controls, concentration-dependent nulls, small dissolved pools and differing Figure2/Figure3 kinetics limit generalization. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original page224 Uramphite row; page1 definitions | supports | Retained official original row/definitions visually checked: ammonium uranyl phosphate trihydrate, grandfathered G, original-description year1957. No fabricated approval CURIE. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/Thermoterrabacterium%20ferrireducens; Current curator-acquired JSON, tax_id/organism_name/rank/query | supports | Independent read verifies historical name resolves to species Carboxydothermus ferrireducens54265. It does not prove an experimental strain accession. |
| history | history/records/uramphite/2026-10-11T221946Z-codex-45fbfb.yaml; Whole CREATE sidecar and distinct inline event | supports | Actor, model, actual timestamp, target and scoped experimental reuse match this addition. |
| search | Independent web.run and local rg on2026-10-11; Notice/context queries and bounded local deduplication | supports | Returned search results did not identify a specific correction/retraction. Related meta-autunite and field U-phosphate observations do not establish contradiction of this narrow synthetic-feed assay. Earlier ningyoite uses the same experiment, explicitly disclosed in the record. |

## Limits And Additional Notes

- Source-derived phase purity, glycerol concentration, independent replication and direct-contact versus dissolved-pathway uncertainties remain. No mineral-specific recovery or long-term stability measured.
- Bounded notice and context searches are not exhaustive. Authority JSON and primary originals were shared acquisition artifacts, independently inspected rather than newly downloaded by root.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T222903Z-uramphite-round36-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial review of precipitated uramphite reduction evidence
started_at: '2026-10-11T22:20:31.874565Z'
finished_at: '2026-10-11T22:29:03.496777Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Authored by /root/round27_eaf_slag; root did not author/edit
    uramphite. Native input capture preceded judgment. Shared acquired originals and
    prior work with the same Khijniak2005 study for ningyoite are disclosed; full
    primary and original figures independently reread for this distinct starting-phase
    target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The narrow laboratory transformation claim is supported with phase, concentration,
  source discrepancy and pathway limits preserved. No corrective record defect identified.
source:
  git_revision: 1ef6fdde620a4053fbfff99c51065082dce32d39
  state: working_tree
  inputs:
  - path: data/records/uramphite.yaml
    sha256: 9a75ded70935425b4d938cb62081a28b767a9df66b7c22a8734df54912a014eb
    role: target
  - path: history/records/uramphite/2026-10-11T221946Z-codex-45fbfb.yaml
    sha256: 7cd7271813793147abfbf3a59b8737ba7e3975302392e028ae652528e842edbd
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: One new uramphite record, all fields, canonical CREATE history and
    claim-specific primary evidence.
  selection: Independent review of another agent’s round36 record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:uramphite
  exclusions:
  - target: Additional Caulobacter or field phosphate transformations
    reason: Not mechanisms asserted in this record; distinct phase and causal evidence
      requires separate assessment.
targets:
- target_id: cmmmech:uramphite
  path: data/records/uramphite.yaml
  label: Uramphite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uramphite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/uramphite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:uramphite
- check_id: batch
  name: Final batch batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 134.59s (0:02:14)

    Checked 200 record(s); 0 failed.

    Checked 231 history record(s); 0 error(s).; log SHA256 cac731be567d421580f78dafc063be4b2ca406ca450d98bb15c72eab76e37b57'
  target_ids:
  - cmmmech:uramphite
- check_id: nonempty
  name: Final batch nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 200 record(s); 0 failed.; log SHA256 0ed97773d44e6b06c1b7964ea58e27e8370bf048dd0a7c0384cf9f7681603b10
  target_ids:
  - cmmmech:uramphite
- check_id: history
  name: Final batch history
  command: uv run --locked cmmmech validate-history --base 1ef6fdde620a4053fbfff99c51065082dce32d39
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 231 history record(s); 0 error(s).; log SHA256 75168340cd2362ddc1a2cc07d98f1a645893ffaa1d3d3f678ad3141c78cf40c4
  target_ids:
  - cmmmech:uramphite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/uramphite.yaml
  locator: All frozen fields
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: Reviewed exact working bytes after native capture.
  snapshot_sha256: 9a75ded70935425b4d938cb62081a28b767a9df66b7c22a8734df54912a014eb
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.71.10.6423-6426.2005
  locator: Complete pp6423–6426; original Figures1–3
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: Independently reread retained complete original and visually inspected
    all three figures. XRD assigns the yellow starting precipitate to uramphite; XAS
    and XRD support reduced phosphate product. Controls, concentration-dependent nulls,
    small dissolved pools and differing Figure2/Figure3 kinetics limit generalization.
  snapshot_sha256: 80854f7a09bcf03e75bcdbfb9a0f45ce406f6adc4bc18f9e630c7a85862e7087
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original page224 Uramphite row; page1 definitions
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: 'Retained official original row/definitions visually checked: ammonium
    uranyl phosphate trihydrate, grandfathered G, original-description year1957. No
    fabricated approval CURIE.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/Thermoterrabacterium%20ferrireducens
  locator: Current curator-acquired JSON, tax_id/organism_name/rank/query
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: Independent read verifies historical name resolves to species Carboxydothermus
    ferrireducens54265. It does not prove an experimental strain accession.
  snapshot_sha256: 6c790ca5f7ad9e4b34c724b8f09d6f9a1980217d2b78b003ff71a07ee705b96a
- evidence_id: history
  kind: record_content
  reference: history/records/uramphite/2026-10-11T221946Z-codex-45fbfb.yaml
  locator: Whole CREATE sidecar and distinct inline event
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: Actor, model, actual timestamp, target and scoped experimental reuse match
    this addition.
  snapshot_sha256: 7cd7271813793147abfbf3a59b8737ba7e3975302392e028ae652528e842edbd
- evidence_id: search
  kind: search
  reference: Independent web.run and local rg on2026-10-11
  locator: Notice/context queries and bounded local deduplication
  accessed_at: '2026-10-11T22:29:03.496777Z'
  support: supports
  summary: Returned search results did not identify a specific correction/retraction.
    Related meta-autunite and field U-phosphate observations do not establish contradiction
    of this narrow synthetic-feed assay. Earlier ningyoite uses the same experiment,
    explicitly disclosed in the record.
  search_scope: 'Web queries: "10.1128/AEM.71.10.6423-6426.2005" correction retraction;
    "uramphite" "Thermoterrabacterium" reduction dissolution; "Uramphite" "IMA" "2026".
    Returned sets only. Local rg --no-ignore --hidden --follow -n -i uramphite|6423-6426.2005
    across data/records,research,reviews,history and the explicitly referenced round35-ningyoite/round36-uramphite
    raw directories; not a global literature or machine-wide absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral versus synthetic feed and constituent
  outcome: supported
  summary: Distinct IMA mineral owner. Assay concerns an abiotic laboratory precipitate
    assigned by characteristic XRD lines, not a natural uramphite specimen or ore.
    Uranium/ningyoite identities and inherited criticality are excluded.
  target_ids:
  - cmmmech:uramphite
  evidence_ids:
  - record
  - ima
  - primary
- assessment_id: conditions
  area: evidence
  topic: Organism, biomass and assay conditions
  outcome: supported
  summary: Fumarate-grown5%inoculum, initialpH7,65C dark static10mL/27mLtubes, uranyl
    acetate and2.4mMphosphate match primary methods. Species-only grounding is explicit.
    The3mL/L versus30mmol/L glycerol discrepancy and unclear independent biological
    replication remain unresolved.
  target_ids:
  - cmmmech:uramphite
  evidence_ids:
  - record
  - primary
  - taxon
  dimensions:
  - name: biomass
    value: Growing thermophilic culture
    definition: Source historical species name; current taxon54265 does not authenticate
      a strain.
    evidence_ids:
    - primary
    - taxon
  - name: scale
    value: Laboratory synthetic growth-medium precipitate
    definition: No ore-processing or industrial deployment experiment.
    evidence_ids:
    - record
    - primary
- assessment_id: transformation
  area: evidence
  topic: Phase, controls and pathway
  outcome: supported
  summary: Initial yellow phase is XRD-assigned uramphite, reduced gray product ningyoite
    with U(IV)/phosphate spectroscopy. Uninoculated control preserves U(VI); dissolved
    uranium pools and no pathway-specific tests prevent exclusive direct-contact or
    enzyme claims.
  target_ids:
  - cmmmech:uramphite
  evidence_ids:
  - record
  - primary
- assessment_id: quantity
  area: evidence
  topic: Outcome denominator and null results
  outcome: supported
  summary: Reported80–90%concerns assayed U(VI) reduction at1/2.5mM by68h, not mineral-specific
    dissolution, phase purity or recovery yield. No reduction/growth at5/10mM and
    Figure3’s separate kinetics are preserved. Figure1D/text describes a crystal mixture.
  target_ids:
  - cmmmech:uramphite
  evidence_ids:
  - record
  - primary
- assessment_id: reuse
  area: provenance
  topic: History, source reuse and review independence
  outcome: supported
  summary: CREATE provenance matches new material owner; the existing ningyoite record
    represents the same experiment from product perspective, with no claim of independent
    replication. Root did not author or edit uramphite.
  target_ids:
  - cmmmech:uramphite
  evidence_ids:
  - record
  - history
  - primary
  - search
findings: []
limitations:
- Source-derived phase purity, glycerol concentration, independent replication and
  direct-contact versus dissolved-pathway uncertainties remain. No mineral-specific
  recovery or long-term stability measured.
- Bounded notice and context searches are not exhaustive. Authority JSON and primary
  originals were shared acquisition artifacts, independently inspected rather than
  newly downloaded by root.
actions: []
```
