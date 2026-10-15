# Independent scientific review of Pascoite

- Review: 20261015T203548Z-pascoite-round102-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T20:25:44.831832Z
- Finished UTC: 2026-10-15T20:35:48.544753Z
- Reviewer: codex /root/round100_pentagonite (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of the exact identity-only mineral record; source conflicts, shared chemistry and model limits are preserved. No supported corrective owner finding.

## Scope And Provenance

Entire frozen owner and CREATE, current IMA identity, claim-bearing primary original methods/results/figures/tables and relevant deposits; bounded correction/conflict search.

Selection: Coordinator-assigned independent review after separate-curator freeze.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2a3bb043c4bd267a3d911d0e77b029c742689e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pascoite | data/records/pascoite.yaml | maintained | Pascoite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent original-evidence assessment | passed | True | cmmmech:pascoite | Primary claims, source boundaries and relevant figures/tables checked. |
| Independent named validation | passed | True | cmmmech:pascoite | Actual independent execution, 2 records checked and 0 failed. |
| Verified coordinator batch check 1 | passed | True | cmmmech:pascoite | Verified actual receipt and retained log hash; not a second reviewer execution. |
| Verified coordinator batch check 2 | passed | True | cmmmech:pascoite | Verified actual receipt and retained log hash; not a second reviewer execution. |
| Verified coordinator batch check 3 | passed | True | cmmmech:pascoite | Verified actual receipt and retained log hash; not a second reviewer execution. |
| Verified coordinator batch check 4 | passed | True | cmmmech:pascoite | Verified actual receipt and retained log hash; not a second reviewer execution. |

## Scientific And Domain Assessments

### Species and hydration identity

identity: supported. Targets: cmmmech:pascoite.

Species and hydration identity is represented within the inspected evidence.

Current IMA [Ca3(H2O)17]V5+10O28, G, 1914 is accurately represented. Mineral species is distinct from free decavanadate ion, broader group and elemental vanadium. Bibliographic 16/17-water disagreement is retained, not silently normalized.

### Natural crystal and model limitations

evidence: supported. Targets: cmmmech:pascoite.

Natural crystal and model limitations is represented within the inspected evidence.

The experiment used Harvard 91449 from Minasragra, Peru, with MoKalpha diffraction and anisotropic non-H refinement. Ca1 possible local 6/7/8 oxygen coordination averages7 in the disordered model. C2/m versus C2 comparison and constrained H positions are qualified; local configurations and universal model uniqueness are not asserted.

### Dependent deposits and table mismatches

provenance: supported. Targets: cmmmech:pascoite.

Dependent deposits and table mismatches is represented within the inspected evidence.

Official artifacts contain23 non-H rows and 2844 unique indexed reflections. This matches Table 1 all-data count, not 2743 significance-filtered reflections. Article/deposit numbering mismatch, slight O13A Ueq difference and unused F000 header remain bounded; no structural re-refinement or independent replication is claimed.

### Criticality, biology, quantities and deployment

scope: supported. Targets: cmmmech:pascoite.

Identity-only scope is defensible.

No organism, strain, biomass, microbial causal role, controlled recovery yield, isolated product or industrial deployment is invented. Criticality and external identifiers are unrecorded, not inferred from vanadium and not an assertion of noncriticality. Historical structural/chemistry values do not become mechanism outcomes.

### Exact source capture and actual CREATE

provenance: supported. Targets: cmmmech:pascoite.

Reviewed bytes and current curation provenance align.

Native inspect preceded judgment and captured trusted 1c2a3bb base with honest working-tree state. Different agent authored this owner/history; reviewer authored borates and made no vanadium owner changes. All captured owner/history/dossier/schema hashes rechecked before save. Primary reuse is disclosed, final coordinator checks distinguished from independent named execution.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/pascoite.yaml; Entire exact frozen owner. | supports | Material identity, source boundaries and absence of unsupported mechanisms assessed. |
| history | history/records/pascoite/2026-10-15T202352Z-codex-4a0ffe.yaml; Canonical CREATE and separate inline CREATE. | supports | Actual actor/model, target, timestamps and described changes align. |
| dossier | research/sources/round102-vanadium/20261015T202416Z-source-investigation.json; Paired source dossier, acquisition/reuse receipts and source limits. | context_only | Author handoff is context; primary originals and deposited artifacts were independently inspected. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions page 1 and exact rendered row on PDF page 167. | supports | September 2026 species formula and grandfathered status verified; year is original description, not a numbered approval or criticality designation. |
| hughes2005 | https://www.rruff.net/doclib/cm/vol43/CM43_1379.pdf; Complete eight-page original; specimen/methods and Table 1 p. 1380, Tables 2–3 p. 1381, Figures1–2 pp. 1382–1383, space-group/H limits pp. 1383–1384, reference p. 1386. | supports | Natural Harvard 91449 crystal supports a disordered C2/m refinement and average Ca1O7, with local 6/7/8 coordination possibilities. Difference-map H sites were restrained and partly disordered; the model is not unconstrained determination of all local configurations. |
| deposit | https://www.mineralogicalassociation.ca/wordpress/depository/; Official download 1821 thermal-parameter DOCX and download 1822 FCF; independent artifact inspection in /private/tmp/cmm-round102-vanadium-review/independent-artifact-inspection.json. | supports | Independently extracted 23 non-H rows and 2844 unique HKL entries. FCF cell matches original; total is not significance-filtered count. Deposit Tables 5/6 differ from paper Tables 4/5; O131 Ueq 0.07442 versus printed O13A 0.0743(3) is not claimed exact equivalence. These are dependent files from the same experiment. |
| iucr1966 | https://journals.iucr.org/q/issues/1966/09/00/index.html; Live publisher issue index, article 397–405, DOI 10.1107/S0365110X66002974; full text not acquired. | context_only | Publisher title contains 16H2O; the 2005 bibliography prints 17H2O. The owner retains the discrepancy without inventing an independently inspected 1966 result. |
| search | Independent bounded local and web review; /private/tmp/cmm-round102-vanadium-review/search.json and dedup.json. | context_only | No attributable formal correction affecting these bounded claims surfaced in returned sets. Bibliographic/model disagreements already in the owners remain explicit. Newly surfaced source leads are not full-text evidence. |
| named | uv run --locked cmmmech validate data/records/pascoite.yaml data/records/navajoite.yaml; /private/tmp/cmm-round102-vanadium-review/validation.log | supports | Independent execution exited 0: two checked, zero failed. |
| batch | /private/tmp/cmm-round102-final-gates.json; /private/tmp/cmm-round102-final-gates.log; SHA256 5ee1c9e4474da08bc2b3ea0ff0316ffb5f9f5861ce2efcca816f9f3238a95b85 | supports | Coordinator terminal four-command receipt and log hash verified. All commands exit 0 and all recorded owner hashes unchanged; no duplicate independent full-suite execution claimed. |

## Limits And Additional Notes

- The 1914 original and 1966 full text remain unacquired; 1966 evidence is bibliographic only.
- No independent structural re-refinement, H-position experiment or full reproduction of model choice was performed.
- Deposit label mismatch and minor printed/deposited parameter differences are not reconciled by an invented corrected table.
- Search/acquisition scope is bounded; no universal absence of corrections, alternative models or microbial mechanisms is asserted.
- Shared prior-round primary downloads were reused with exact hashes and independently inspected; official pascoite deposits were acquired this round.
- Separate publication wording/helper audits do not alter the scientific owner or this verdict.
- Structured whole-corpus validation follows bundle creation; no previous review or history is overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T203548Z-pascoite-round102-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Pascoite
started_at: '2026-10-15T20:25:44.831832Z'
finished_at: '2026-10-15T20:35:48.544753Z'
reviewer:
  identity: codex /root/round100_pentagonite
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from vanadium curator /root/round100_vanadium.
    This reviewer authored borax/tincalconite, independently inspected vanadium evidence
    after exact capture, and made no vanadium owner/history edits.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified acceptance of the exact identity-only mineral record; source conflicts,
  shared chemistry and model limits are preserved. No supported corrective owner finding.
source:
  git_revision: 1c2a3bb043c4bd267a3d911d0e77b029c742689e
  state: working_tree
  inputs:
  - path: data/records/pascoite.yaml
    sha256: 37b434c93cb30ed04dfc43e6108ddc33a69c6da8f131dc271e3c5e03b2b28e75
    role: target
  - path: history/records/pascoite/2026-10-15T202352Z-codex-4a0ffe.yaml
    sha256: 26a29e92c0959e808df8b38771450a9a55ae8c5bc3c281f5898ebc22730ebfde
    role: context
  - path: research/sources/round102-vanadium/20261015T202416Z-source-investigation.json
    sha256: 6335c64b657b7b4563e7bd565807b62c2e09a3b0879eab675215fa7f79c307db
    role: context
  - path: research/sources/round102-vanadium/20261015T202416Z-source-investigation.md
    sha256: 5f0cdcd3c27966f94a3a09e876e0b934e69a6d318a55aca3a314e8121d478f06
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen owner and CREATE, current IMA identity, claim-bearing
    primary original methods/results/figures/tables and relevant deposits; bounded
    correction/conflict search.
  selection: Coordinator-assigned independent review after separate-curator freeze.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pascoite
targets:
- target_id: cmmmech:pascoite
  path: data/records/pascoite.yaml
  label: Pascoite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pascoite.yaml
    role: maintained_record
checks:
- check_id: science
  name: Independent original-evidence assessment
  required: true
  status: passed
  summary: Primary claims, source boundaries and relevant figures/tables checked.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - ima
  - hughes2005
  - deposit
  - iucr1966
  - search
- check_id: named
  name: Independent named validation
  required: true
  status: passed
  command: uv run --locked cmmmech validate data/records/pascoite.yaml data/records/navajoite.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual independent execution, 2 records checked and 0 failed.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - named
- check_id: batch1
  name: Verified coordinator batch check 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual receipt and retained log hash; not a second reviewer execution.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - batch
- check_id: batch2
  name: Verified coordinator batch check 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual receipt and retained log hash; not a second reviewer execution.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - batch
- check_id: batch3
  name: Verified coordinator batch check 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 1c2a3bb043c4bd267a3d911d0e77b029c742689e
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual receipt and retained log hash; not a second reviewer execution.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - batch
- check_id: batch4
  name: Verified coordinator batch check 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual receipt and retained log hash; not a second reviewer execution.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/pascoite.yaml
  locator: Entire exact frozen owner.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: Material identity, source boundaries and absence of unsupported mechanisms
    assessed.
  snapshot_sha256: 37b434c93cb30ed04dfc43e6108ddc33a69c6da8f131dc271e3c5e03b2b28e75
- evidence_id: history
  kind: record_content
  reference: history/records/pascoite/2026-10-15T202352Z-codex-4a0ffe.yaml
  locator: Canonical CREATE and separate inline CREATE.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: Actual actor/model, target, timestamps and described changes align.
  snapshot_sha256: 26a29e92c0959e808df8b38771450a9a55ae8c5bc3c281f5898ebc22730ebfde
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round102-vanadium/20261015T202416Z-source-investigation.json
  locator: Paired source dossier, acquisition/reuse receipts and source limits.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: context_only
  summary: Author handoff is context; primary originals and deposited artifacts were
    independently inspected.
  snapshot_sha256: 6335c64b657b7b4563e7bd565807b62c2e09a3b0879eab675215fa7f79c307db
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions page 1 and exact rendered row on PDF page 167.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: September 2026 species formula and grandfathered status verified; year
    is original description, not a numbered approval or criticality designation.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: hughes2005
  kind: primary_source
  reference: https://www.rruff.net/doclib/cm/vol43/CM43_1379.pdf
  locator: Complete eight-page original; specimen/methods and Table 1 p. 1380, Tables
    2–3 p. 1381, Figures1–2 pp. 1382–1383, space-group/H limits pp. 1383–1384, reference
    p. 1386.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: Natural Harvard 91449 crystal supports a disordered C2/m refinement and
    average Ca1O7, with local 6/7/8 coordination possibilities. Difference-map H sites
    were restrained and partly disordered; the model is not unconstrained determination
    of all local configurations.
  snapshot_sha256: 37810bbe390b3c792008357523dc42882842ac6f6514361a2b05438752f64bf5
- evidence_id: deposit
  kind: primary_source
  reference: https://www.mineralogicalassociation.ca/wordpress/depository/
  locator: Official download 1821 thermal-parameter DOCX and download 1822 FCF; independent
    artifact inspection in /private/tmp/cmm-round102-vanadium-review/independent-artifact-inspection.json.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: Independently extracted 23 non-H rows and 2844 unique HKL entries. FCF
    cell matches original; total is not significance-filtered count. Deposit Tables
    5/6 differ from paper Tables 4/5; O131 Ueq 0.07442 versus printed O13A 0.0743(3)
    is not claimed exact equivalence. These are dependent files from the same experiment.
  snapshot_sha256: 00c3d0606f46b331a2a6b90ecda06887b0381c6c10c050ef4a041eaee716ccbc
- evidence_id: iucr1966
  kind: authority
  reference: https://journals.iucr.org/q/issues/1966/09/00/index.html
  locator: Live publisher issue index, article 397–405, DOI 10.1107/S0365110X66002974;
    full text not acquired.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: context_only
  summary: Publisher title contains 16H2O; the 2005 bibliography prints 17H2O. The
    owner retains the discrepancy without inventing an independently inspected 1966
    result.
- evidence_id: search
  kind: search
  reference: Independent bounded local and web review
  locator: /private/tmp/cmm-round102-vanadium-review/search.json and dedup.json.
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: context_only
  summary: No attributable formal correction affecting these bounded claims surfaced
    in returned sets. Bibliographic/model disagreements already in the owners remain
    explicit. Newly surfaced source leads are not full-text evidence.
  search_scope: 'Four current queries: pascoite exact 2005 DOI plus correction/erratum/retraction;
    navajoite Weeks/Evans correction/structure; 1966 pascoite title 16H2O; navajoite
    microbial/extraction/structure 2024–2026. Live IUCr index and DTU 2020 author-institution
    abstract inspected; MAC live open failed, acquired official artifacts inspected.
    Hidden/ignored/followed rg covered data/research/reviews/history/local skills,
    cited round 101/102 vanadium raw and 261-issue title/body snapshot. 43 files matched.
    No machine-wide, issue-comment or literature-completeness assertion.'
  snapshot_sha256: 617139e7157005e218ab2e8310f5bfc9d372871d3df1aae40488514b8302b265
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/pascoite.yaml data/records/navajoite.yaml
  locator: /private/tmp/cmm-round102-vanadium-review/validation.log
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: 'Independent execution exited 0: two checked, zero failed.'
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round102-final-gates.json
  locator: /private/tmp/cmm-round102-final-gates.log; SHA256 5ee1c9e4474da08bc2b3ea0ff0316ffb5f9f5861ce2efcca816f9f3238a95b85
  accessed_at: '2026-10-15T20:35:48.544753Z'
  support: supports
  summary: Coordinator terminal four-command receipt and log hash verified. All commands
    exit 0 and all recorded owner hashes unchanged; no duplicate independent full-suite
    execution claimed.
  snapshot_sha256: 27bacebde96bb1b572897eb3ca5ed83263195f774c2871a4d734f18a2d5d46fe
assessments:
- assessment_id: identity
  area: identity
  topic: Species and hydration identity
  outcome: supported
  summary: Species and hydration identity is represented within the inspected evidence.
  details: Current IMA [Ca3(H2O)17]V5+10O28, G, 1914 is accurately represented. Mineral
    species is distinct from free decavanadate ion, broader group and elemental vanadium.
    Bibliographic 16/17-water disagreement is retained, not silently normalized.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - ima
  - hughes2005
  - iucr1966
- assessment_id: structure
  area: evidence
  topic: Natural crystal and model limitations
  outcome: supported
  summary: Natural crystal and model limitations is represented within the inspected
    evidence.
  details: The experiment used Harvard 91449 from Minasragra, Peru, with MoKalpha
    diffraction and anisotropic non-H refinement. Ca1 possible local 6/7/8 oxygen
    coordination averages7 in the disordered model. C2/m versus C2 comparison and
    constrained H positions are qualified; local configurations and universal model
    uniqueness are not asserted.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - hughes2005
  - owner
- assessment_id: deposits
  area: provenance
  topic: Dependent deposits and table mismatches
  outcome: supported
  summary: Dependent deposits and table mismatches is represented within the inspected
    evidence.
  details: Official artifacts contain23 non-H rows and 2844 unique indexed reflections.
    This matches Table 1 all-data count, not 2743 significance-filtered reflections.
    Article/deposit numbering mismatch, slight O13A Ueq difference and unused F000
    header remain bounded; no structural re-refinement or independent replication
    is claimed.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - deposit
  - hughes2005
  - dossier
- assessment_id: scope
  area: scope
  topic: Criticality, biology, quantities and deployment
  outcome: supported
  summary: Identity-only scope is defensible.
  details: No organism, strain, biomass, microbial causal role, controlled recovery
    yield, isolated product or industrial deployment is invented. Criticality and
    external identifiers are unrecorded, not inferred from vanadium and not an assertion
    of noncriticality. Historical structural/chemistry values do not become mechanism
    outcomes.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - owner
  - ima
- assessment_id: provenance
  area: provenance
  topic: Exact source capture and actual CREATE
  outcome: supported
  summary: Reviewed bytes and current curation provenance align.
  details: Native inspect preceded judgment and captured trusted 1c2a3bb base with
    honest working-tree state. Different agent authored this owner/history; reviewer
    authored borates and made no vanadium owner changes. All captured owner/history/dossier/schema
    hashes rechecked before save. Primary reuse is disclosed, final coordinator checks
    distinguished from independent named execution.
  target_ids:
  - cmmmech:pascoite
  evidence_ids:
  - owner
  - history
  - dossier
  - named
  - batch
findings: []
actions: []
limitations:
- The 1914 original and 1966 full text remain unacquired; 1966 evidence is bibliographic
  only.
- No independent structural re-refinement, H-position experiment or full reproduction
  of model choice was performed.
- Deposit label mismatch and minor printed/deposited parameter differences are not
  reconciled by an invented corrected table.
- Search/acquisition scope is bounded; no universal absence of corrections, alternative
  models or microbial mechanisms is asserted.
notes:
- Shared prior-round primary downloads were reused with exact hashes and independently
  inspected; official pascoite deposits were acquired this round.
- Separate publication wording/helper audits do not alter the scientific owner or
  this verdict.
- Structured whole-corpus validation follows bundle creation; no previous review or
  history is overwritten.
```
