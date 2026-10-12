# Independent initial scientific review of anatase

- Review: 20261012T065628Z-anatase-round49-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T06:50:38Z
- Finished UTC: 2026-10-12T06:56:28Z
- Reviewer: Codex /root/round43_hardmetal (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The microbial-template and abiotic thermal-crystallization boundaries are supported, but one minor incorrect original-figure locator requires correction. Full original main/SI inspected; actual original-state cohort gates passed.

## Scope And Provenance

All frozen anatase fields/history/paired source dossier; complete main andSI graphics, currentIMA/NCBIidentity andbounded searches.

Selection: Assigned independent review of new anatase owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b701555aa8b06a51f94a4d97bed7f3ebf96ab439.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:anatase | data/records/anatase.yaml | maintained | Anatase |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:anatase | Actually executed by reviewer in explicit round49worktree; Checked2records,0failed. |
| Final cohort gates | passed | True | cmmmech:anatase | Original-state gate actually completed; all four terminal logs verified. Any later correction requires affected checks again. |

## Scientific And Domain Assessments

### Distinct anatase mineral and manufactured counterpart

identity: supported. Targets: cmmmech:anatase.

Distinct TiO2species and syntheticreagent/cell-template context are explicit; no inheritedcriticality, naturalbiogenesis or recovery.

### Biomass template and abiotic crystalline stage

evidence: supported. Targets: cmmmech:anatase.

37C largelyamorphous deposition and600C crystalline product are separated. R5/INPcontrol supports morphology, not microbialnecessity. Missing biomassdose, precursorstockconcentration, viability and massbalance remain explicit.

### Powder-reference label attribution

evidence: concern. Targets: cmmmech:anatase.

F1: Original Figure2e agrees with S6on21-1272; onlyprose says21-1271.

## Findings

### F1: Anatase powder-card discrepancy misattributes the main figure label

minor / open / confirmed; issue key: CMMMech.anatase.powder-card-figure-locator.

The record says Main Figure2e and its prose cite21-1271, whereas FigureS6 labels21-1272. Full-resolution Figure2e itself labels21-1272, agreeing with S6; only surrounding prose says21-1271. The dossier Markdown repeats this bounded locator error. Preserve the genuine prose/graphic discrepancy and qualified phase assignment while correcting the attribution. The dossier JSON does not repeat this exact wording.

## Recommended Actions And Acceptance Checks

### A1

Correct the record attribution to prose21-1271 versus Figure2e/S6labels21-1272; append actual EDIT history and source-dossier correction with predecessor preserved.

- Inspect original Figure2e andS6 independently; corrected wording states exact discrepancy.
- Preserve originalCREATE and thisinitialbundle; save successor with exact F1 lineage and reviewissue.
- Repeat named and affectedcohort checks; review finalbytehashes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/anatase.yaml; All fields; mechanisms[0].evidence[1] powder-reference sentence | supports | Exact frozen pre-correction record inspected; one bounded incorrect figure attribution identified. |
| history | history/records/anatase/2026-10-12T064814Z-codex-810f65.yaml; Actual CREATE and separate inline event | supports | History describes the creation scope and does not claim independent acceptance. |
| dossier | research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.md; Anatase section: MainFigure2/prose uses powder card21-1271 sentence | supports | This Markdown repeats the incorrect attribution. The paired JSON is captured context and source integrity metadata, not a second occurrence of that exact sentence. |
| original | https://doi.org/10.1039/C6SC02311H; Complete seven-page original, Figures1–7; page6332 prose versus Figure2e | supports | All main pages visually inspected. Prose says21-1271; original Figure2e says21-1272. The source itself retains a prose/graphic inconsistency. |
| figure2e | /private/tmp/cmm-round49-ti-research/raw/anatase2016-c6sc02311h-f2.jpg; Original full-resolution Figure2e graph lower-right label | supports | Label unambiguously reads Anatase PDF21-1272. It does not read21-1271. |
| supplement | /private/tmp/cmm-round49-ti-research/raw/anatase2016-cloud-SC-007-C6SC02311H-s001.pdf; Complete14pages, FiguresS1–S13 andTablesS1–S2; S6onpage7 | supports | All SI pages visually inspected. FigureS6 also says21-1272. Cell-pellet synthesis, 37/80Cincubation and600Ccalcination support separate biological-template and thermal stages; controls do not establish microbial necessity. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Current edition page10Anatase; definitions/terms independently inspected thisround | supports | TiO2,A,1962s.p.,France; the specialprocedure is not a unique approval accession. |
| validation | /private/tmp/cmm-round49-ti-independent/source-check.json; Independent named validation and all119 raw artifact hash bindings | supports | Named validation checked2records,0failed; all captured target/context hashes and all119rawbindings matched. |
| dedup | /private/tmp/cmm-round49-ti-independent/dedup-receipt.json; Independent ignored-inclusive identity/experiment search | supports | Only the assigned new owner matches its exactID. Source/material distinctions retained. |
| notices | /private/tmp/cmm-round49-ti-independent/web-notices.txt; Returned DOI/title/correction and NCBI562 queries on2026-10-12 | supports | No applicable correction/retraction appeared in the returned search sets; NCBI562 resolves toEscherichia coli species, not stock authentication. |
| cohort_receipt | /private/tmp/cmm-round49-final-terminal.json; Four actual original-state terminal commands and verified log hashes | supports | just check317passed3skipped;241records284histories;nonempty/history/render-check0. These precede the authorized F1 correction. |

## Limits And Additional Notes

- Original-state gates passed; a later correction must be reviewed and its affected checks repeated before final acceptance.
- No independent raw diffraction re-refinement, stock authentication or viability assay; studycontrols do not establish metabolism.
- Record is synthetic-reagent materials synthesis, not natural mineral extraction or deployment.
- Notice/dedupsearches bounded asdeclared; everyunextractedbinary or unavailablehistoricalroot was not searched.
- No record, Git/GitHub or governance mutation by reviewer. Initial review saved before anycorrection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T065628Z-anatase-round49-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial scientific review of anatase
started_at: '2026-10-12T06:50:38Z'
finished_at: '2026-10-12T06:56:28Z'
reviewer:
  identity: Codex /root/round43_hardmetal
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Peer /root/round27_packaging authored anatase/history/dossier.
    Reviewer authored separate baddeleyite only. Native inspect captured exact target/context
    before judgment; unsupported preliminary target-kind label was corrected and identical
    bytes recaptured before first save. Reviewer inspected originals independently
    and made no target edit.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The microbial-template and abiotic thermal-crystallization boundaries are
  supported, but one minor incorrect original-figure locator requires correction.
  Full original main/SI inspected; actual original-state cohort gates passed.
source:
  git_revision: b701555aa8b06a51f94a4d97bed7f3ebf96ab439
  state: working_tree
  inputs:
  - path: data/records/anatase.yaml
    sha256: 1b75b2c9a7bc922bd7503a2a3415478e77498df6db23c6385e8a612a547db60e
    role: target
  - path: history/records/anatase/2026-10-12T064814Z-codex-810f65.yaml
    sha256: 0235c06c755d2e23ed39210e179588216fc0585127be6af493cb6cacfaad6800
    role: context
  - path: research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.json
    sha256: cb591bbfda47b62ffa39fa1629c28e2a4ad88ca1c7a1bfc34e62e1668234f0ff
    role: context
  - path: research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.md
    sha256: 0777f05cacdeb9fd0ff916a8152e3b43511ee6929f3364eed5dd2ca83d0146e8
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:anatase
  path: data/records/anatase.yaml
  label: Anatase
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anatase.yaml
    role: maintained scientific record
scope:
  description: All frozen anatase fields/history/paired source dossier; complete main
    andSI graphics, currentIMA/NCBIidentity andbounded searches.
  selection: Assigned independent review of new anatase owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:anatase
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/anatase.yaml data/records/brookite.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:anatase
  summary: Actually executed by reviewer in explicit round49worktree; Checked2records,0failed.
- check_id: cohort
  name: Final cohort gates
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base b701555aa8b06a51f94a4d97bed7f3ebf96ab439
  status: passed
  required: true
  target_ids:
  - cmmmech:anatase
  summary: Original-state gate actually completed; all four terminal logs verified.
    Any later correction requires affected checks again.
  exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/anatase.yaml
  locator: All fields; mechanisms[0].evidence[1] powder-reference sentence
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: Exact frozen pre-correction record inspected; one bounded incorrect figure
    attribution identified.
  snapshot_sha256: 1b75b2c9a7bc922bd7503a2a3415478e77498df6db23c6385e8a612a547db60e
- evidence_id: history
  kind: record_content
  reference: history/records/anatase/2026-10-12T064814Z-codex-810f65.yaml
  locator: Actual CREATE and separate inline event
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: History describes the creation scope and does not claim independent acceptance.
  snapshot_sha256: 0235c06c755d2e23ed39210e179588216fc0585127be6af493cb6cacfaad6800
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.md
  locator: 'Anatase section: MainFigure2/prose uses powder card21-1271 sentence'
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: This Markdown repeats the incorrect attribution. The paired JSON is captured
    context and source integrity metadata, not a second occurrence of that exact sentence.
  snapshot_sha256: 0777f05cacdeb9fd0ff916a8152e3b43511ee6929f3364eed5dd2ca83d0146e8
- evidence_id: original
  kind: primary_source
  reference: https://doi.org/10.1039/C6SC02311H
  locator: Complete seven-page original, Figures1–7; page6332 prose versus Figure2e
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: All main pages visually inspected. Prose says21-1271; original Figure2e
    says21-1272. The source itself retains a prose/graphic inconsistency.
  snapshot_sha256: e022ad627cb847c673dae3c31a86b2cd82a812c01ed8b57c444453e779c4c3e0
- evidence_id: figure2e
  kind: primary_source
  reference: /private/tmp/cmm-round49-ti-research/raw/anatase2016-c6sc02311h-f2.jpg
  locator: Original full-resolution Figure2e graph lower-right label
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: Label unambiguously reads Anatase PDF21-1272. It does not read21-1271.
  snapshot_sha256: 2001b6710b493f92705bdcd2522deabfaa305a8a79c7d6bf522d0760e57b0899
- evidence_id: supplement
  kind: primary_source
  reference: /private/tmp/cmm-round49-ti-research/raw/anatase2016-cloud-SC-007-C6SC02311H-s001.pdf
  locator: Complete14pages, FiguresS1–S13 andTablesS1–S2; S6onpage7
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: All SI pages visually inspected. FigureS6 also says21-1272. Cell-pellet
    synthesis, 37/80Cincubation and600Ccalcination support separate biological-template
    and thermal stages; controls do not establish microbial necessity.
  snapshot_sha256: 133e3d5066b86ccf51c9aac6cb9ff076dee0f3b851e1f5bf080d6d0722e8da20
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Current edition page10Anatase; definitions/terms independently inspected
    thisround
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: TiO2,A,1962s.p.,France; the specialprocedure is not a unique approval accession.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round49-ti-independent/source-check.json
  locator: Independent named validation and all119 raw artifact hash bindings
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: Named validation checked2records,0failed; all captured target/context hashes
    and all119rawbindings matched.
  snapshot_sha256: e4bf9bdb2c266b645a2077037fa0e14c9cee9fcf17b886576172694514b056ae
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round49-ti-independent/dedup-receipt.json
  locator: Independent ignored-inclusive identity/experiment search
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: Only the assigned new owner matches its exactID. Source/material distinctions
    retained.
  snapshot_sha256: 8f854c3c97fe0499fa9a9675d95f2501d44d09397529ba7b82c4d5d35becb65e
  search_scope: rg --no-ignore --hidden --follow across current/original records,research,reviews,history
    plus180 existing cited rawroots;3802textfiles. Nine missing historicalroots and
    unextractedbinaries excluded explicitly. Terms anatase,brookite,C6SC02311H,8b00213,INP.5R5,8115.*brookite.
    No machine-wideabsence claim.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round49-ti-independent/web-notices.txt
  locator: Returned DOI/title/correction and NCBI562 queries on2026-10-12
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: No applicable correction/retraction appeared in the returned search sets;
    NCBI562 resolves toEscherichia coli species, not stock authentication.
  snapshot_sha256: d6f1f4b1f2c6a91d31674d0aaf09998df73eca4151cccb900d78605a05ca9a22
  search_scope: 'First returned web result sets, no pagination: exact10.1039/C6SC02311H
    and10.1021/acsearthspacechem.8b00213 with correction erratum retraction; exact
    anatase title with control criticism; officialNCBI562 species lookup. Bounded
    search, not proof of notice absence.'
- evidence_id: cohort_receipt
  kind: validation
  reference: /private/tmp/cmm-round49-final-terminal.json
  locator: Four actual original-state terminal commands and verified log hashes
  accessed_at: '2026-10-12T06:56:28Z'
  support: supports
  summary: just check317passed3skipped;241records284histories;nonempty/history/render-check0.
    These precede the authorized F1 correction.
  snapshot_sha256: f4b7ce550db56904c8c1720dc9692d93cbb7dc471890f22f2be8b4f6c639f2d1
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct anatase mineral and manufactured counterpart
  outcome: supported
  target_ids:
  - cmmmech:anatase
  evidence_ids:
  - ima
  - original
  - supplement
  summary: Distinct TiO2species and syntheticreagent/cell-template context are explicit;
    no inheritedcriticality, naturalbiogenesis or recovery.
- assessment_id: mechanism
  area: evidence
  topic: Biomass template and abiotic crystalline stage
  outcome: supported
  target_ids:
  - cmmmech:anatase
  evidence_ids:
  - original
  - supplement
  summary: 37C largelyamorphous deposition and600C crystalline product are separated.
    R5/INPcontrol supports morphology, not microbialnecessity. Missing biomassdose,
    precursorstockconcentration, viability and massbalance remain explicit.
- assessment_id: locator
  area: evidence
  topic: Powder-reference label attribution
  outcome: concern
  target_ids:
  - cmmmech:anatase
  evidence_ids:
  - record
  - figure2e
  - original
  - supplement
  - dossier
  summary: 'F1: Original Figure2e agrees with S6on21-1272; onlyprose says21-1271.'
findings:
- finding_id: F1
  issue_key: CMMMech.anatase.powder-card-figure-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Anatase powder-card discrepancy misattributes the main figure label
  description: The record says Main Figure2e and its prose cite21-1271, whereas FigureS6
    labels21-1272. Full-resolution Figure2e itself labels21-1272, agreeing with S6;
    only surrounding prose says21-1271. The dossier Markdown repeats this bounded
    locator error. Preserve the genuine prose/graphic discrepancy and qualified phase
    assignment while correcting the attribution. The dossier JSON does not repeat
    this exact wording.
  target_ids:
  - cmmmech:anatase
  field_paths:
  - mechanisms[0].evidence[1].explanation
  evidence_ids:
  - record
  - figure2e
  - original
  - supplement
  - dossier
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anatase.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.md
    role: source dossier occurrence; preserve predecessor and append correction note
  rule_id: primary-source-exact-locator
  native_severity: minor
  normalization_reason: Bounded attribution error; does not overturn the qualified
    anatase identity or thermal-stage mechanism.
actions:
- action_id: A1
  description: Correct the record attribution to prose21-1271 versus Figure2e/S6labels21-1272;
    append actual EDIT history and source-dossier correction with predecessor preserved.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:anatase
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/anatase.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round49-ti-minerals/20261012T065018Z-source-investigation.md
    role: source dossier occurrence; preserve predecessor and append correction note
  acceptance_checks:
  - Inspect original Figure2e andS6 independently; corrected wording states exact
    discrepancy.
  - Preserve originalCREATE and thisinitialbundle; save successor with exact F1 lineage
    and reviewissue.
  - Repeat named and affectedcohort checks; review finalbytehashes.
limitations:
- Original-state gates passed; a later correction must be reviewed and its affected
  checks repeated before final acceptance.
- No independent raw diffraction re-refinement, stock authentication or viability
  assay; studycontrols do not establish metabolism.
- Record is synthetic-reagent materials synthesis, not natural mineral extraction
  or deployment.
- Notice/dedupsearches bounded asdeclared; everyunextractedbinary or unavailablehistoricalroot
  was not searched.
notes:
- No record, Git/GitHub or governance mutation by reviewer. Initial review saved before
  anycorrection.
tags:
- round49
- anatase
- independent
- initial
```
