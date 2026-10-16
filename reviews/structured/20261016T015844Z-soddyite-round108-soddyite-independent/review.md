# Independent scientific review of soddyite (soddyite)

- Review: 20261016T015844Z-soddyite-round108-soddyite-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T01:36:31.465670Z
- Finished UTC: 2026-10-16T01:58:44.996493Z
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
| cmmmech:soddyite | data/records/soddyite.yaml | maintained | Soddyite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual batch gate 1 | passed | True | cmmmech:soddyite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 2 | passed | True | cmmmech:soddyite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 3 | passed | True | cmmmech:soddyite | Terminal receipt and log checked; final input hashes unchanged. |
| Actual batch gate 4 | passed | True | cmmmech:soddyite | Terminal receipt and log checked; final input hashes unchanged. |

## Scientific And Domain Assessments

### Natural mineral and experimental material boundaries

identity: supported. Targets: cmmmech:soddyite.

Current mineral identity, formula and grandfathered status are supported. No elemental criticality, microbial mechanism or deployment claim is inherited.

### Primary laboratory evidence

evidence: supported. Targets: cmmmech:soddyite.

The no-added-Si and100 micromol/L Si flow arms have different saturation and changing concentrations; no unique surface inhibition or independent flow replication is asserted. Batch fit windows differ for U and Si. XRD cannot uniquely distinguish the secondary sodium uranates; Raman reference is itself clarkeite-like. Natural2018 crystal identity is not experimental powder provenance.

### Actual provenance and source limits

provenance: supported. Targets: cmmmech:soddyite.

Canonical history and inline events are distinct; source versions, natural/synthetic scope and unresolved reporting limits are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/soddyite.yaml; Entire native-inspected owner Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/data/records/soddyite.yaml | supports | Identity and accepted experimental claims independently assessed against primary sources. |
| history0 | history/records/soddyite/2026-10-16T013344Z-codex-965e52.yaml; Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/soddyite/2026-10-16T013344Z-codex-965e52.yaml | supports | Actual GPT-6 actor, target, timestamp and described change checked. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Current species rows on PDF pages201–202 visually inspected; definitions page1 Local artifact: /private/tmp/cmm-round108-uranium-research/ima202609.pdf | supports | Distinct grandfathered species, formulas and original-description years; no fabricated approval accessions. |
| plasil | https://doi.org/10.3390/min8120551; New original data in section2.1/Table2; sections3.1/3.3 and Figures2/4/7; pages2/4 visually inspected Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018.pdf | supports | Natural museum-crystal data are distinct from synthetic reaction products and illustrated locality specimens. Article is labelled Review but contains primary new diffraction data. |
| cif | Original Plášil2018 linked supplementary CIF; Formula, space group, cell values, R1 and reflection fields Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/soddyite_final.cif | supports | Deposited refinement corroborates identity and model statistics; article/CIF uncertainty differences remain explicit. |
| search | Independent exact-DOI/title notice and related-source search; First returned windows for Giammar2002 DOI, Plášil2018 DOI and Vochten1997 title with correction/erratum/retraction terms; fourth topic query Local artifact: /private/tmp/cmm-round108-uranium-independent-search.json | context_only | No affecting notice surfaced in bounded returned results; this does not establish universal absence. |
| dedup | Curator bounded hidden/ignored-inclusive inventory; Declared current/main/cited raw roots and issue title/body inventory Local artifact: /private/tmp/cmm-round108-uranium-research/dedup-final.json | context_only | Bounded results preserve two distinct owners and prior context; no machine-wide negative claim. |
| experiment | https://doi.org/10.1016/S0016-7037(02)00927-4; Methods2.1–2.4, Results3.1–3.3, Discussion4.1–4.4; original PDFpages2–9 text and pages4–6 graphics independently checked Local artifact: /private/tmp/cmm-round108-uranium-research/giammar2002.pdf | supports | Synthetic batch and flow experiments support qualified dissolution and secondary precipitation. Differing fit windows, numerical summaries, lost Si data, wall adherence and uncertain clarkeite-like phase are preserved. |
| batch | Completed batch receipt; Commands, exact unchanged record inputs and retained log hash Local artifact: /private/tmp/cmm-round108-final-gates-corrected.json | supports | All required batch gates passed on final record state. |

## Limits And Additional Notes

- Independent review checked accepted-claim sections and listed original graphics; it did not visually reread every page, repeat experiments or re-refine diffraction data.
- Original numerical/CIF uncertainties and experiment omissions remain source gaps; no inferred product recovery, microbial action or industrial deployment.
- Correction searches and hidden/ignored-inclusive dedup are bounded, not universal absence proofs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T015844Z-soddyite-round108-soddyite-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of soddyite (soddyite)
started_at: '2026-10-16T01:36:31.465670Z'
finished_at: '2026-10-16T01:58:44.996493Z'
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
  - path: data/records/soddyite.yaml
    sha256: 346601a9ef95444ac9cf161bbcd8c41132a22d6e73c3d1517c97bdd6c0d68adf
    role: target
  - path: history/records/soddyite/2026-10-16T013344Z-codex-965e52.yaml
    sha256: 2bfe3de2fa41b21910feb880a2a347bdd951c3863730d8683b7a1aff2f705aef
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
- target_id: cmmmech:soddyite
  path: data/records/soddyite.yaml
  label: Soddyite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/soddyite.yaml
    role: maintained_record
scope:
  description: Entire owner/history and primary material/experimental claims; bounded
    independent scientific review, no raw-data reanalysis.
  selection: Native inspect before assessment of exact assigned owner and context
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:soddyite
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
  - cmmmech:soddyite
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
  - cmmmech:soddyite
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
  - cmmmech:soddyite
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
  - cmmmech:soddyite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/soddyite.yaml
  locator: 'Entire native-inspected owner Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/data/records/soddyite.yaml'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: 346601a9ef95444ac9cf161bbcd8c41132a22d6e73c3d1517c97bdd6c0d68adf
  support: supports
  summary: Identity and accepted experimental claims independently assessed against
    primary sources.
- evidence_id: history0
  kind: record_content
  reference: history/records/soddyite/2026-10-16T013344Z-codex-965e52.yaml
  locator: 'Canonical sidecar and separate inline event Local artifact: /private/tmp/CMMMech-expansion-round108-20261016/history/records/soddyite/2026-10-16T013344Z-codex-965e52.yaml'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: 2bfe3de2fa41b21910feb880a2a347bdd951c3863730d8683b7a1aff2f705aef
  support: supports
  summary: Actual GPT-6 actor, target, timestamp and described change checked.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'Current species rows on PDF pages201–202 visually inspected; definitions
    page1 Local artifact: /private/tmp/cmm-round108-uranium-research/ima202609.pdf'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Distinct grandfathered species, formulas and original-description years;
    no fabricated approval accessions.
- evidence_id: plasil
  kind: primary_source
  reference: https://doi.org/10.3390/min8120551
  locator: 'New original data in section2.1/Table2; sections3.1/3.3 and Figures2/4/7;
    pages2/4 visually inspected Local artifact: /private/tmp/cmm-round108-uranium-research/plasil2018.pdf'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: f96034e17b57086c19566d0f63f9b28bc94bc8c47de52e368c391204ba87e3d4
  support: supports
  summary: Natural museum-crystal data are distinct from synthetic reaction products
    and illustrated locality specimens. Article is labelled Review but contains primary
    new diffraction data.
- evidence_id: cif
  kind: primary_source
  reference: Original Plášil2018 linked supplementary CIF
  locator: 'Formula, space group, cell values, R1 and reflection fields Local artifact:
    /private/tmp/cmm-round108-uranium-research/plasil2018-supplement/soddyite_final.cif'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: 0f2eb00c4e668e0cc29ab226725a45e7e965c088a690e4157cc8b5d19e463f84
  support: supports
  summary: Deposited refinement corroborates identity and model statistics; article/CIF
    uncertainty differences remain explicit.
- evidence_id: search
  kind: search
  reference: Independent exact-DOI/title notice and related-source search
  locator: 'First returned windows for Giammar2002 DOI, Plášil2018 DOI and Vochten1997
    title with correction/erratum/retraction terms; fourth topic query Local artifact:
    /private/tmp/cmm-round108-uranium-independent-search.json'
  accessed_at: '2026-10-16T01:58:44.996493Z'
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
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: 624079198a2711dc621ab053e64e584c8b03ace885843e411e0290d9869a4833
  support: context_only
  summary: Bounded results preserve two distinct owners and prior context; no machine-wide
    negative claim.
  search_scope: Curator inventory independently examined; hidden/ignored files and
    relevant symlinks included. Issue comments and arbitrary external paths excluded.
- evidence_id: experiment
  kind: primary_source
  reference: https://doi.org/10.1016/S0016-7037(02)00927-4
  locator: 'Methods2.1–2.4, Results3.1–3.3, Discussion4.1–4.4; original PDFpages2–9
    text and pages4–6 graphics independently checked Local artifact: /private/tmp/cmm-round108-uranium-research/giammar2002.pdf'
  accessed_at: '2026-10-16T01:58:44.996493Z'
  snapshot_sha256: deaf899af9116124cbbab3dc98b0c4630cbb50234d9eb95333278400303cb813
  support: supports
  summary: Synthetic batch and flow experiments support qualified dissolution and
    secondary precipitation. Differing fit windows, numerical summaries, lost Si data,
    wall adherence and uncertain clarkeite-like phase are preserved.
- evidence_id: batch
  kind: validation
  reference: Completed batch receipt
  locator: 'Commands, exact unchanged record inputs and retained log hash Local artifact:
    /private/tmp/cmm-round108-final-gates-corrected.json'
  accessed_at: '2026-10-16T01:58:44.996493Z'
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
  - cmmmech:soddyite
  evidence_ids:
  - owner
  - ima
  - plasil
  - cif
- assessment_id: science
  area: evidence
  topic: Primary laboratory evidence
  outcome: supported
  summary: The no-added-Si and100 micromol/L Si flow arms have different saturation
    and changing concentrations; no unique surface inhibition or independent flow
    replication is asserted. Batch fit windows differ for U and Si. XRD cannot uniquely
    distinguish the secondary sodium uranates; Raman reference is itself clarkeite-like.
    Natural2018 crystal identity is not experimental powder provenance.
  target_ids:
  - cmmmech:soddyite
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
  - cmmmech:soddyite
  evidence_ids:
  - owner
  - search
  - dedup
  - history0
findings: []
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
