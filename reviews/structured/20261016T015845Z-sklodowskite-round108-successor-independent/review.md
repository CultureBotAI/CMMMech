# Independent scientific review of sklodowskite (successor)

- Review: 20261016T015845Z-sklodowskite-round108-successor-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T01:36:36.500265Z
- Finished UTC: 2026-10-16T01:58:45.023673Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified mineral identity and laboratory claims are supported; source limitations remain explicit.

## Scope And Provenance

Entire owner/history and primary material/experimental claims; bounded independent scientific review, no raw-data reanalysis.

Selection: Native inspect before assessment of exact assigned owner and context inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26661b7f033d4bdb915e48e71080aa5774b4c3d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:sklodowskite | data/records/sklodowskite.yaml | maintained | Sklodowskite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual batch gate 1 | passed | True | cmmmech:sklodowskite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 2 | passed | True | cmmmech:sklodowskite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 3 | passed | True | cmmmech:sklodowskite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 4 | passed | True | cmmmech:sklodowskite | Terminal receipt and log checked; final input hashes unchanged. |

## Scientific And Domain Assessments

### Natural mineral and experimental material boundaries

identity: supported. Targets: cmmmech:sklodowskite.

Current mineral identity, formula and grandfathered status are supported. No elemental criticality, microbial mechanism or deployment claim is inherited.

### Primary laboratory evidence

evidence: supported. Targets: cmmmech:sklodowskite.

The Mg arm is separate from Na/Ca/Pb treatments, precursor preparation and boltwoodite solubility. Qualitative negative potassium testing does not prove solid potassium zero or a quantified conversion. The natural2018 refinement is separate from the1997 powder-derived cell. The printed synthetic c parameter requires exact transcription.

### Actual provenance and source limits

provenance: supported. Targets: cmmmech:sklodowskite.

Canonical history and inline events are distinct; source versions, natural/synthetic scope and unresolved reporting limits are preserved.

### Exact source transcription restored

quantity: supported. Targets: cmmmech:sklodowskite.

Current owner agrees with original Table4 for c and its parenthesized uncertainty; earlier finding explicitly resolved.

## Findings

### F108-SKL-1: Synthetic sklodowskite c parameter is mistranscribed

minor / resolved / confirmed; issue key: round108-sklodowskite-synthetic-c-transcription.

Vochten1997 Table4 Skl column gives c=6.6216(4) angstrom; the initial owner gives6.621(6). Preserve the exact value and uncertainty. This is a bounded transcription error, not a failure of the mineral identity or hydrothermal formation evidence.

Disposition: Maintained owner now exactly transcribes6.6216(4) angstrom; actual EDIT sidecar and inline event added. Independent reinspection and successful final-byte gates confirm the correction without changing the mechanism scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/sklodowskite.yaml; Entire native-inspected owner Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/data/records/sklodowskite.yaml | supports | Identity and accepted experimental claims independently assessed against primary sources. |
| history0 | history/records/sklodowskite/2026-10-16T013411Z-codex-4dd638.yaml; Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/sklodowskite/2026-10-16T013411Z-codex-4dd638.yaml | supports | Actual GPT-6 actor, target, timestamp and described change checked. |
| history1 | history/records/sklodowskite/2026-10-16T014735Z-codex-e2bc99.yaml; Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/sklodowskite/2026-10-16T014735Z-codex-e2bc99.yaml | supports | Actual GPT-6 actor, target, timestamp and described change checked. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Current species rows on PDF pages201–202 visually inspected; definitions page1 Local artifact: /private/tmp/cmm-round108-uranium-research/ima202609.pdf | supports | Distinct grandfathered species, formulas and original-description years; no fabricated approval accessions. |
| plasil | https://doi.org/10.3390/min8120551; New original data in section2.1/Table2; sections3.1/3.3 and Figures2/4/7; pages2/4 visually inspected Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018.pdf | supports | Natural museum-crystal data are distinct from synthetic reaction products and illustrated locality specimens. Article is labelled Review but contains primary new diffraction data. |
| cif | Original Plášil2018 linked supplementary CIF; Formula, space group, cell values, R1 and reflection fields Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/sklodowskite_final.cif | supports | Deposited refinement corroborates identity and model statistics; article/CIF uncertainty differences remain explicit. |
| search | Independent exact-DOI/title notice and related-source search; First returned windows for Giammar2002 DOI, Plášil2018 DOI and Vochten1997 title with correction/erratum/retraction terms; fourth topic query Local artifact: /private/tmp/cmm-round108-uranium-independent-search.json | context_only | No affecting notice surfaced in bounded returned results; this does not establish universal absence. |
| dedup | Curator bounded hidden/ignored-inclusive inventory; Declared current/main/cited raw roots and issue title/body inventory Local artifact: /private/tmp/cmm-round108-uranium-research/dedup-final.json | context_only | Bounded results preserve two distinct owners and prior context; no machine-wide negative claim. |
| experiment | https://www.rruff.net/doclib/cm/vol35/CM35_735.pdf; Original pp736/740, synthesis paragraph and Table4 independently textually and visually checked; remaining source context read Local artifact: /private/tmp/cmm-round108-uranium-research/vochten1997.pdf | supports | MgSO4 hydrothermal treatment of boltwoodite gives powder-assigned sklodowskite, with repeated24h cycles and qualitative potassium endpoint. No yield, phase fraction or sklodowskite solubility measurement. |
| table | Vochten1997 Table4 original raster; High-resolution independent crop, Skl column c row Local artifact: /private/tmp/cmm-round108-uranium-research/root-table4-crop.png | supports | Printed synthetic c parameter is6.6216(4) angstrom. Initial owner transcribed6.621(6). |
| batch | Completed batch receipt; Commands, exact unchanged record inputs and retained log hash Local artifact: /private/tmp/cmm-round108-final-gates-corrected.json | supports | All required batch gates passed on final record state. |

## Limits And Additional Notes

- Independent review checked accepted-claim sections and listed original graphics; it did not visually reread every page, repeat experiments or re-refine diffraction data.
- Original numerical/CIF uncertainties and experiment omissions remain source gaps; no inferred product recovery, microbial action or industrial deployment.
- Correction searches and hidden/ignored-inclusive dedup are bounded, not universal absence proofs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T015845Z-sklodowskite-round108-successor-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of sklodowskite (successor)
started_at: '2026-10-16T01:36:36.500265Z'
finished_at: '2026-10-16T01:58:45.023673Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored the mineral owner/history; root authored
    the separate wastewater record and independently assessed these frozen mineral
    bytes and primary evidence without editing the owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified mineral identity and laboratory claims are supported; source limitations
  remain explicit.
source:
  git_revision: 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  state: working_tree
  inputs:
  - path: data/records/sklodowskite.yaml
    sha256: 4c65a7130837c668c697a43817c631a381191abf5f16fa9babeb5971f5865589
    role: target
  - path: history/records/sklodowskite/2026-10-16T013411Z-codex-4dd638.yaml
    sha256: 7947e852ffca5fe689816cc0dedc9b961f920b074df572a18ddf0e321188baf3
    role: context
  - path: history/records/sklodowskite/2026-10-16T014735Z-codex-e2bc99.yaml
    sha256: eac752b6e240fec05f6ecc6168821800fba6f3fb1d52d0d52aad2432ffb58738
    role: context
  - path: research/sources/round108-uranium/20261016T013528Z-source-investigation.json
    sha256: 22742db6336a576716ca2eb4931bdbab4551ccf56907e5351f12f1866b05f5c2
    role: context
  - path: research/sources/round108-uranium/20261016T013528Z-source-investigation.md
    sha256: b59590d74ec5874830df2fafbe79766bc9047c11d9c396ce74eb031c296786d6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:sklodowskite
  path: data/records/sklodowskite.yaml
  label: Sklodowskite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sklodowskite.yaml
    role: maintained_record
scope:
  description: Entire owner/history and primary material/experimental claims; bounded
    independent scientific review, no raw-data reanalysis.
  selection: Native inspect before assessment of exact assigned owner and context
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:sklodowskite
checks:
- check_id: batch1
  name: Actual batch gate 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal receipt and log checked; final input hashes unchanged.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - batch
- check_id: batch2
  name: Actual batch gate 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal receipt and log checked; final input hashes unchanged.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - batch
- check_id: batch3
  name: Actual batch gate 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal receipt and log checked; final input hashes unchanged.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - batch
- check_id: batch4
  name: Actual batch gate 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal receipt and log checked; final input hashes unchanged.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/sklodowskite.yaml
  locator: 'Entire native-inspected owner Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/data/records/sklodowskite.yaml'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 4c65a7130837c668c697a43817c631a381191abf5f16fa9babeb5971f5865589
  support: supports
  summary: Identity and accepted experimental claims independently assessed against
    primary sources.
- evidence_id: history0
  kind: record_content
  reference: history/records/sklodowskite/2026-10-16T013411Z-codex-4dd638.yaml
  locator: 'Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/sklodowskite/2026-10-16T013411Z-codex-4dd638.yaml'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 7947e852ffca5fe689816cc0dedc9b961f920b074df572a18ddf0e321188baf3
  support: supports
  summary: Actual GPT-6 actor, target, timestamp and described change checked.
- evidence_id: history1
  kind: record_content
  reference: history/records/sklodowskite/2026-10-16T014735Z-codex-e2bc99.yaml
  locator: 'Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/sklodowskite/2026-10-16T014735Z-codex-e2bc99.yaml'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: eac752b6e240fec05f6ecc6168821800fba6f3fb1d52d0d52aad2432ffb58738
  support: supports
  summary: Actual GPT-6 actor, target, timestamp and described change checked.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'Current species rows on PDF pages201–202 visually inspected; definitions
    page1 Local artifact: /private/tmp/cmm-round108-uranium-research/ima202609.pdf'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Distinct grandfathered species, formulas and original-description years;
    no fabricated approval accessions.
- evidence_id: plasil
  kind: primary_source
  reference: https://doi.org/10.3390/min8120551
  locator: 'New original data in section2.1/Table2; sections3.1/3.3 and Figures2/4/7;
    pages2/4 visually inspected Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018.pdf'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: f96034e17b57086c19566d0f63f9b28bc94bc8c47de52e368c391204ba87e3d4
  support: supports
  summary: Natural museum-crystal data are distinct from synthetic reaction products
    and illustrated locality specimens. Article is labelled Review but contains primary
    new diffraction data.
- evidence_id: cif
  kind: primary_source
  reference: Original Plášil2018 linked supplementary CIF
  locator: 'Formula, space group, cell values, R1 and reflection fields Local artifact:
    /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/sklodowskite_final.cif'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 23cf68160de6e6b15a467838ab6be7d9bb7d34d10c7174041f595db1187d4e56
  support: supports
  summary: Deposited refinement corroborates identity and model statistics; article/CIF
    uncertainty differences remain explicit.
- evidence_id: search
  kind: search
  reference: Independent exact-DOI/title notice and related-source search
  locator: 'First returned windows for Giammar2002 DOI, Plášil2018 DOI and Vochten1997
    title with correction/erratum/retraction terms; fourth topic query Local artifact:
    /private/tmp/cmm-round108-uranium-independent-search.json'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 0e000236c5221cc29cbe794091a33fdab1c69e2b5a2e5fabcb1dd5a6c99f330b
  support: context_only
  summary: No affecting notice surfaced in bounded returned results; this does not
    establish universal absence.
  search_scope: Four web queries, primary source links retained; no exhaustive citing-paper
    search or author outreach.
- evidence_id: dedup
  kind: search
  reference: Curator bounded hidden/ignored-inclusive inventory
  locator: 'Declared current/main/cited raw roots and issue title/body inventory Local
    artifact: /private/tmp/cmm-round108-uranium-research/dedup-final.json'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 624079198a2711dc621ab053e64e584c8b03ace885843e411e0290d9869a4833
  support: context_only
  summary: Bounded results preserve two distinct owners and prior context; no machine-wide
    negative claim.
  search_scope: Curator inventory independently examined; hidden/ignored files and
    relevant symlinks included. Issue comments and arbitrary external paths excluded.
- evidence_id: experiment
  kind: primary_source
  reference: https://www.rruff.net/doclib/cm/vol35/CM35_735.pdf
  locator: 'Original pp736/740, synthesis paragraph and Table4 independently textually
    and visually checked; remaining source context read Local artifact: /private/tmp/cmm-round108-uranium-research/vochten1997.pdf'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: e1318999e81c0e2da373a60798c71675b279b42c6ac4c29fa4a2af188cd5658d
  support: supports
  summary: MgSO4 hydrothermal treatment of boltwoodite gives powder-assigned sklodowskite,
    with repeated24h cycles and qualitative potassium endpoint. No yield, phase fraction
    or sklodowskite solubility measurement.
- evidence_id: table
  kind: primary_source
  reference: Vochten1997 Table4 original raster
  locator: 'High-resolution independent crop, Skl column c row Local artifact: /private/tmp/cmm-round108-uranium-research/root-table4-crop.png'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: 48951974007431f48792e64cd6d210baa5d866f4072bd5f6e4b78f82e8402fe8
  support: supports
  summary: Printed synthetic c parameter is6.6216(4) angstrom. Initial owner transcribed6.621(6).
- evidence_id: batch
  kind: validation
  reference: Completed batch receipt
  locator: 'Commands, exact unchanged record inputs and retained log hash Local artifact:
    /private/tmp/cmm-round108-final-gates-corrected.json'
  accessed_at: '2026-10-16T01:58:45.023673Z'
  snapshot_sha256: b537f2550a758f2e973b21f657129e0922fe41ea0cde632899d354d5bf11daf3
  support: supports
  summary: All required batch gates passed on final record state.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural mineral and experimental material boundaries
  outcome: supported
  summary: Current mineral identity, formula and grandfathered status are supported.
    No elemental criticality, microbial mechanism or deployment claim is inherited.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - owner
  - ima
  - plasil
  - cif
- assessment_id: science
  area: evidence
  topic: Primary laboratory evidence
  outcome: supported
  summary: The Mg arm is separate from Na/Ca/Pb treatments, precursor preparation
    and boltwoodite solubility. Qualitative negative potassium testing does not prove
    solid potassium zero or a quantified conversion. The natural2018 refinement is
    separate from the1997 powder-derived cell. The printed synthetic c parameter requires
    exact transcription.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - owner
  - experiment
  - plasil
- assessment_id: provenance
  area: provenance
  topic: Actual provenance and source limits
  outcome: supported
  summary: Canonical history and inline events are distinct; source versions, natural/synthetic
    scope and unresolved reporting limits are preserved.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - owner
  - search
  - dedup
  - history0
- assessment_id: correction
  area: quantity
  topic: Exact source transcription restored
  outcome: supported
  summary: Current owner agrees with original Table4 for c and its parenthesized uncertainty;
    earlier finding explicitly resolved.
  target_ids:
  - cmmmech:sklodowskite
  evidence_ids:
  - owner
  - experiment
  - table
findings:
- finding_id: F108-SKL-1
  issue_key: round108-sklodowskite-synthetic-c-transcription
  category: quantity
  severity: minor
  status: resolved
  certainty: confirmed
  title: Synthetic sklodowskite c parameter is mistranscribed
  description: Vochten1997 Table4 Skl column gives c=6.6216(4) angstrom; the initial
    owner gives6.621(6). Preserve the exact value and uncertainty. This is a bounded
    transcription error, not a failure of the mineral identity or hydrothermal formation
    evidence.
  target_ids:
  - cmmmech:sklodowskite
  field_paths:
  - mechanisms[0].evidence[0].explanation
  evidence_ids:
  - owner
  - experiment
  - table
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/sklodowskite.yaml
    role: maintained_record
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261016T014047Z-sklodowskite-round108-initial-independent
    finding_id: F108-SKL-1
  disposition_reason: Maintained owner now exactly transcribes6.6216(4) angstrom;
    actual EDIT sidecar and inline event added. Independent reinspection and successful
    final-byte gates confirm the correction without changing the mechanism scope.
actions: []
limitations:
- Independent review checked accepted-claim sections and listed original graphics;
  it did not visually reread every page, repeat experiments or re-refine diffraction
  data.
- Original numerical/CIF uncertainties and experiment omissions remain source gaps;
  no inferred product recovery, microbial action or industrial deployment.
- Correction searches and hidden/ignored-inclusive dedup are bounded, not universal
  absence proofs.
```
