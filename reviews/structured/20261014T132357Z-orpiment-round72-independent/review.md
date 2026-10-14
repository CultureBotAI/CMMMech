# Independent scientific review of orpiment

- Review: 20261014T132357Z-orpiment-round72-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T13:17:15.488133Z
- Finished UTC: 2026-10-14T13:23:57.743377Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified independent acceptance of orpiment as an XRD-assigned secondary phase in the already-curated Liu2019 arsenopyrite experiment. Phase identity, controls and shared-study limits are correctly scoped; Newman1997 amorphous As2S3 is explicitly excluded from crystalline orpiment evidence. No corrective defect identified.

## Scope And Provenance

Entire maintained record and linked canonical history; independent original-source assessment of all accepted scientific claims.

Selection: Assigned frozen owner; native inspect before record-level judgment and exact input hashes rechecked at save.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a2f08edab1307aba4281ce1e2a54d84bca88a889.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:orpiment | data/records/orpiment.yaml | maintained | Orpiment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named strict validation | passed | True | cmmmech:orpiment | Reviewer executed;2 records,0 failures. |
| Completed batch check 1 | passed | True | cmmmech:orpiment | Coordinator execution 2026-10-14T13:17:12.131110+00:00 through 2026-10-14T13:20:48.706062+00:00; receipt and log hash independently checked. |
| Completed batch check 2 | passed | True | cmmmech:orpiment | Coordinator execution 2026-10-14T13:20:48.706092+00:00 through 2026-10-14T13:20:56.556799+00:00; receipt and log hash independently checked. |
| Completed batch check 3 | passed | True | cmmmech:orpiment | Coordinator execution 2026-10-14T13:20:56.556822+00:00 through 2026-10-14T13:21:01.412318+00:00; receipt and log hash independently checked. |

## Scientific And Domain Assessments

### Species, material and organism boundaries

identity: supported. Targets: cmmmech:orpiment.

Dated IMA and Handbook identities support separate monoclinic mineral owners; no elemental criticality is inherited. NCBI920 identifies A. ferrooxidans at species rank, not a deposited assay strain.

### History and source lineage

provenance: supported. Targets: cmmmech:orpiment.

Actual CREATE sidecar and inline entry identify this new owner, curator and current source assessment; named checks and shared batch gates bind exact reviewed bytes.

### Secondary phase and shared experiment

evidence: supported. Targets: cmmmech:orpiment.

Original XRD/QPA supports source-assigned orpiment during a live A. ferrooxidans arsenopyrite culture experiment; the record discloses missing causal controls and shared lineage with arsenopyrite.

Verified10g/L feed,100mL9K plus15mL inoculum,30°C,160rpm,pH1.8 and3monthacclimation. Cubes are separate microscopy samples, not identical particleXRD material.

### Amorphous versus crystalline As2S3

identity: supported. Targets: cmmmech:orpiment.

Newman1997 states amorphous electron diffraction; composition and cellular co-occurrence do not identify the orpiment crystal structure.

### Passivation model and extraction boundary

scope: supported. Targets: cmmmech:orpiment.

Film/thermodynamic interpretations remain partial; no orpiment-specific causality, microbial necessity, isolated yield or deployment is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/orpiment.yaml; Complete final owner | supports | Read every field, source reference and frozen byte hash. |
| history | history/records/orpiment/2026-10-14T130937Z-codex-0f01bd.yaml; Entire linked canonical sidecar | supports | Target, actor, actual timestamp and finished curation/correction details checked against inline history. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pages1-2 and species row 160 | supports | Original retained IMA row visually checked for exact species, formula, status and historical date. No constituent criticality inherited. |
| handbook | https://www.handbookofmineralogy.org/pdfs/orpiment.pdf; Complete one-page mineral entry | supports | Formula and crystallographic identity checked; authority entry is not experimental phase-purity certification. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Species-level920,current name and rank | supports | Retained source and independent current NCBI browser agree on A.ferrooxidans species; no strain-resolution claim. |
| primary | https://doi.org/10.3390/met9121320; Complete original11pages; Methods3.1–3.3,Results4,Figures1–6,Tables1–2,AppendixA | supports | Independently checked methods and all figures/tables. Figure2 assigns crystalline orpiment in mixed residues; bars are normalized relative phase proportions, not absolute production. Separate particleXRD and cubeEDS do not isolate orpiment passivation or microbial necessity;25°C equilibrium differs from30°C culture. |
| amorphous | https://doi.org/10.1128/aem.63.5.2022-2028.1997; Complete7pageoriginal,identificationp2023,Figures1–5,especiallyFigure2 | context_only | Read original and inspected all main figures. Electron diffraction explicitly describes amorphous precipitate; EDS supports composition only. The record correctly excludes this separate microbial experiment as proof of crystalline orpiment. |
| dedup | /private/tmp/cmm-round72-arsenic-independent/dedup.txt; Records/research/reviews/history and referenced current raw source directory | context_only | Hidden/ignored-inclusive search with relevant symlinks followed; related elemental owner and source lineages distinguished. |
| notices | /private/tmp/cmm-round72-arsenic-independent/notice-search.json; Independent exact DOI queries and direct NCBI/MDPI checks | context_only | No relevant notice surfaced in bounded returned results; ASM erratum relates to another study and MDPI landing returned429. Retained original sources remain assessed. |
| named | /private/tmp/cmm-round72-arsenic-independent/named-validation.log; Reviewer execution log | supports | Named validation passed on both frozen owners. |
| batch | /private/tmp/cmm-round72-final-gates.json; Completed root batch receipt and matching log | supports | Required commands completed successfully; exact worktree/base, exit codes and nonempty log checksum independently verified. |
| artifact_audit | /private/tmp/cmm-round72-arsenic-independent/source-artifact-audit.json; Actual nonempty original PDF/source sizes, hashes and PDF signatures/page counts | context_only | Checked actual inspected original PDFs and taxonomy capture rather than failed download filenames. |

## Limits And Additional Notes

- No matched sterile or pH-controlled kinetic arm, quantitative replicate count, error-bar definition or selective film-removal intervention is reported in Liu2019.
- ParticleXRD/Rietveld identifies a mixed residual phase; cubeEDS alone cannot identify an orpiment-specific passivating film. Washing/drying and different preparations limit cross-assay transfer.
- Relative phase proportions cannot supply absolute orpiment production/destruction or isolated recovered yield. Thermodynamic pathways remain proposed and differ from early observed phases.
- Newman1997 precipitates amorphous arsenic trisulfide; its biological necessity/removal measurements do not establish crystalline orpiment.
- Independent bounded notice search does not prove absence of every correction or inaccessible supplement; current MDPI page returned429, but original retained fulltext/graphics were assessed.
- No claim of pure-phase recovery, industrial deployment or universal microbial necessity is inferred. Full source files remain outside Git.
- All evidence hashes bind nonempty actual inspected artifacts. The realgar2012.pdf HTML viewer is not used as PDF evidence; the actual realgar2012-original.pdf is bound.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T132357Z-orpiment-round72-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of orpiment
started_at: '2026-10-14T13:17:15.488133Z'
finished_at: '2026-10-14T13:23:57.743377Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The reviewed arsenic-sulfide owners and their histories were
    curated by /root/round68_iron_sulfides. This reviewer curated only albite and
    orthoclase in round72 and made no edits to the reviewed owners or histories. Acquired
    raw sources are shared, but original text, all claim-bearing figures/tables, authorities
    and exact record bytes were independently examined; this is independent assessment,
    not independent experimental replication.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified independent acceptance of orpiment as an XRD-assigned secondary
  phase in the already-curated Liu2019 arsenopyrite experiment. Phase identity, controls
  and shared-study limits are correctly scoped; Newman1997 amorphous As2S3 is explicitly
  excluded from crystalline orpiment evidence. No corrective defect identified.
source:
  git_revision: a2f08edab1307aba4281ce1e2a54d84bca88a889
  state: working_tree
  inputs:
  - path: data/records/orpiment.yaml
    sha256: 6c4b4f1a6d0004ddd7df308fd339651adb8e1db18d8d570829fcb2bec20b754b
    role: target
  - path: history/records/orpiment/2026-10-14T130937Z-codex-0f01bd.yaml
    sha256: 07f413e538f70ed15dc130835b8ca9ff8015a3d42a0924eace74b5ce1fb7e3f9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire maintained record and linked canonical history; independent
    original-source assessment of all accepted scientific claims.
  selection: Assigned frozen owner; native inspect before record-level judgment and
    exact input hashes rechecked at save.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:orpiment
targets:
- target_id: cmmmech:orpiment
  path: data/records/orpiment.yaml
  label: Orpiment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/orpiment.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named strict validation
  command: uv run --locked cmmmech validate data/records/realgar.yaml data/records/orpiment.yaml
    --require-records
  status: passed
  required: true
  summary: Reviewer executed;2 records,0 failures.
  target_ids:
  - cmmmech:orpiment
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Completed batch check 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T13:17:12.131110+00:00 through 2026-10-14T13:20:48.706062+00:00;
    receipt and log hash independently checked.
  target_ids:
  - cmmmech:orpiment
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Completed batch check 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T13:20:48.706092+00:00 through 2026-10-14T13:20:56.556799+00:00;
    receipt and log hash independently checked.
  target_ids:
  - cmmmech:orpiment
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Completed batch check 3
  command: uv run --locked cmmmech validate-history --base a2f08edab1307aba4281ce1e2a54d84bca88a889
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T13:20:56.556822+00:00 through 2026-10-14T13:21:01.412318+00:00;
    receipt and log hash independently checked.
  target_ids:
  - cmmmech:orpiment
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/orpiment.yaml
  locator: Complete final owner
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Read every field, source reference and frozen byte hash.
  snapshot_sha256: 6c4b4f1a6d0004ddd7df308fd339651adb8e1db18d8d570829fcb2bec20b754b
- evidence_id: history
  kind: record_content
  reference: history/records/orpiment/2026-10-14T130937Z-codex-0f01bd.yaml
  locator: Entire linked canonical sidecar
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Target, actor, actual timestamp and finished curation/correction details
    checked against inline history.
  snapshot_sha256: 07f413e538f70ed15dc130835b8ca9ff8015a3d42a0924eace74b5ce1fb7e3f9
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pages1-2 and species row 160
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Original retained IMA row visually checked for exact species, formula,
    status and historical date. No constituent criticality inherited.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/orpiment.pdf
  locator: Complete one-page mineral entry
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Formula and crystallographic identity checked; authority entry is not experimental
    phase-purity certification.
  snapshot_sha256: 115e7eaa2eb9df6e4d21b3e54846c1a04bab55118b77bec0bb2afafa8ff4978f
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Species-level920,current name and rank
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Retained source and independent current NCBI browser agree on A.ferrooxidans
    species; no strain-resolution claim.
  snapshot_sha256: c6d264e2f6ed730350be86773d9564c7427f7f089b57ed566d6494e3bd21a4ac
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/met9121320
  locator: Complete original11pages; Methods3.1–3.3,Results4,Figures1–6,Tables1–2,AppendixA
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Independently checked methods and all figures/tables. Figure2 assigns crystalline
    orpiment in mixed residues; bars are normalized relative phase proportions, not
    absolute production. Separate particleXRD and cubeEDS do not isolate orpiment
    passivation or microbial necessity;25°C equilibrium differs from30°C culture.
  snapshot_sha256: 062168a7c2e6bf9cfc8524f4e30e4511d86c5dea931b6c787b960810ed3afb19
- evidence_id: amorphous
  kind: primary_source
  reference: https://doi.org/10.1128/aem.63.5.2022-2028.1997
  locator: Complete7pageoriginal,identificationp2023,Figures1–5,especiallyFigure2
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: context_only
  summary: Read original and inspected all main figures. Electron diffraction explicitly
    describes amorphous precipitate; EDS supports composition only. The record correctly
    excludes this separate microbial experiment as proof of crystalline orpiment.
  snapshot_sha256: f3e9a7ea542602a933cb55c7f6540ed56bd649ed7e7e227fc63c1bc4833e085d
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round72-arsenic-independent/dedup.txt
  locator: Records/research/reviews/history and referenced current raw source directory
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: context_only
  summary: Hidden/ignored-inclusive search with relevant symlinks followed; related
    elemental owner and source lineages distinguished.
  search_scope: rg --no-ignore --hidden --follow -n -i realgar|orpiment|met9121320|1501.01.154|2022-2028.1997
    data/records research reviews history and /private/tmp/cmm-round72-arsenic-sulfides-research
  snapshot_sha256: 47b002948e60732ae235d788fe31c20fa9df831d84d45d25d53301368f045990
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round72-arsenic-independent/notice-search.json
  locator: Independent exact DOI queries and direct NCBI/MDPI checks
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: context_only
  summary: No relevant notice surfaced in bounded returned results; ASM erratum relates
    to another study and MDPI landing returned429. Retained original sources remain
    assessed.
  search_scope: Three exact-DOI queries plus correction/retraction/supplement, first
    batches, no filters; no universal absence claim.
  snapshot_sha256: 88b7fd4dde4a9d71df8d3cdd5a574a971965a576c46f0fd539f9959d403e6389
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round72-arsenic-independent/named-validation.log
  locator: Reviewer execution log
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Named validation passed on both frozen owners.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round72-final-gates.json
  locator: Completed root batch receipt and matching log
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: supports
  summary: Required commands completed successfully; exact worktree/base, exit codes
    and nonempty log checksum independently verified.
  snapshot_sha256: b5b2d551ac899632844d0d3a3f9dbc95897408e73a7ccec69513cdb22a1352e7
- evidence_id: artifact_audit
  kind: validation
  reference: /private/tmp/cmm-round72-arsenic-independent/source-artifact-audit.json
  locator: Actual nonempty original PDF/source sizes, hashes and PDF signatures/page
    counts
  accessed_at: '2026-10-14T13:23:57.743377Z'
  support: context_only
  summary: Checked actual inspected original PDFs and taxonomy capture rather than
    failed download filenames.
  snapshot_sha256: 161cf7df1372354f2c833fd3c20a5f7b5a3f113b578aa80ea5761aa21d8823f9
assessments:
- assessment_id: identity
  area: identity
  topic: Species, material and organism boundaries
  outcome: supported
  summary: Dated IMA and Handbook identities support separate monoclinic mineral owners;
    no elemental criticality is inherited. NCBI920 identifies A. ferrooxidans at species
    rank, not a deposited assay strain.
  evidence_ids:
  - ima
  - handbook
  - taxonomy
  - record
  target_ids:
  - cmmmech:orpiment
- assessment_id: provenance
  area: provenance
  topic: History and source lineage
  outcome: supported
  summary: Actual CREATE sidecar and inline entry identify this new owner, curator
    and current source assessment; named checks and shared batch gates bind exact
    reviewed bytes.
  evidence_ids:
  - history
  - record
  - named
  - batch
  target_ids:
  - cmmmech:orpiment
- assessment_id: mechanism
  area: evidence
  topic: Secondary phase and shared experiment
  outcome: supported
  summary: Original XRD/QPA supports source-assigned orpiment during a live A. ferrooxidans
    arsenopyrite culture experiment; the record discloses missing causal controls
    and shared lineage with arsenopyrite.
  evidence_ids:
  - primary
  - record
  details: Verified10g/L feed,100mL9K plus15mL inoculum,30°C,160rpm,pH1.8 and3monthacclimation.
    Cubes are separate microscopy samples, not identical particleXRD material.
  target_ids:
  - cmmmech:orpiment
- assessment_id: phase_boundary
  area: identity
  topic: Amorphous versus crystalline As2S3
  outcome: supported
  summary: Newman1997 states amorphous electron diffraction; composition and cellular
    co-occurrence do not identify the orpiment crystal structure.
  evidence_ids:
  - amorphous
  - handbook
  - record
  target_ids:
  - cmmmech:orpiment
- assessment_id: scope
  area: scope
  topic: Passivation model and extraction boundary
  outcome: supported
  summary: Film/thermodynamic interpretations remain partial; no orpiment-specific
    causality, microbial necessity, isolated yield or deployment is asserted.
  evidence_ids:
  - primary
  - record
  target_ids:
  - cmmmech:orpiment
findings: []
actions: []
limitations:
- No matched sterile or pH-controlled kinetic arm, quantitative replicate count, error-bar
  definition or selective film-removal intervention is reported in Liu2019.
- ParticleXRD/Rietveld identifies a mixed residual phase; cubeEDS alone cannot identify
  an orpiment-specific passivating film. Washing/drying and different preparations
  limit cross-assay transfer.
- Relative phase proportions cannot supply absolute orpiment production/destruction
  or isolated recovered yield. Thermodynamic pathways remain proposed and differ from
  early observed phases.
- Newman1997 precipitates amorphous arsenic trisulfide; its biological necessity/removal
  measurements do not establish crystalline orpiment.
- Independent bounded notice search does not prove absence of every correction or
  inaccessible supplement; current MDPI page returned429, but original retained fulltext/graphics
  were assessed.
notes:
- No claim of pure-phase recovery, industrial deployment or universal microbial necessity
  is inferred. Full source files remain outside Git.
- All evidence hashes bind nonempty actual inspected artifacts. The realgar2012.pdf
  HTML viewer is not used as PDF evidence; the actual realgar2012-original.pdf is
  bound.
```
