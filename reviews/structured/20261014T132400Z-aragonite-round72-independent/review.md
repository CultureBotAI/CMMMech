# Independent scientific review of aragonite

- Review: 20261014T132400Z-aragonite-round72-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T13:16:56.854077Z
- Finished UTC: 2026-10-14T13:24:00.738181Z
- Reviewer: codex /root/round68_iron_sulfides (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The qualified mineral phase record is supported by original evidence. Source and control limitations are preserved; no corrective findings. Named and final batch checks passed.

## Scope And Provenance

Complete maintained owner and linked canonical CREATE, independently reassessed against full primary evidence and authority.

Selection: Assigned frozen owner; native inspection before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a2f08edab1307aba4281ce1e2a54d84bca88a889.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:aragonite | data/records/aragonite.yaml | maintained | Aragonite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named strict validation | passed | True | cmmmech:aragonite | Reviewer independently executed:2 checked, 0 failed. |
| Completed batch checks | passed | True | cmmmech:aragonite | Coordinator executed; reviewer verified terminal receipt/log SHA and all exit codes.317 passed, 3 skipped; 341 records, 0 failures; 394 histories, 0 errors. |

## Scientific And Domain Assessments

### Distinct carbonate species

identity: supported. Targets: cmmmech:aragonite.

Orthorhombic aragonite is correctly separated from calcite/vaterite/MHC and calcium. No criticality claim is inherited.

### Source-designated Y1

grounding: supported. Targets: cmmmech:aragonite.

MF808044.1 is a partial 16S submission named B. licheniformis strain Y1, consistent with the species mapping but not culture-collection authentication.

### Culture versus abiotic recipe

evidence: supported. Targets: cmmmech:aragonite.

Main2.1-2.5 confirms beefextract5g/L,tryptone10g/L,NaCl10g/L,Ca0.01M and stated Mg series;1%v/v,triplicate sterile-water controls,37C130rpm,day14/25 harvest. Drying temperature and pH-matched phase controls are not supplied. Section2.10 abiotic carbonate-addition experiment has different recipe and duration.

### Time- and Mg/Ca-dependent phase assignments

evidence: supported. Targets: cmmmech:aragonite.

Original Figure2 and SupplementaryFigure5 E-H support mixed14-day and aragonite-only25-day fits at ratios6/9; I-J support ratio12 both times. Fitted crystalline percentages are not recovered mass or proof of no amorphous/organic material.

### EPS, magnesium and dolomitization

scope: supported. Targets: cmmmech:aragonite.

Figures3-13 and sections3.6-4.3 distinguish observed associations,bulk acid-digest Mg,selected lattice spacings and calculations. Mg coordination and alternative replacement/dissolution-reprecipitation mechanisms remain explicitly uncertain. The record does not promote selected dolomite domains to a bulk conversion yield.

### Abiotic formation and scale

scope: supported. Targets: cmmmech:aragonite.

SupplementaryFigure13 includes precipitation without biomolecules; this does not substitute for a matched culture control. Laboratory mineral formation is not metal recovery or deployment.

### Exact owner, history and source binding

provenance: supported. Targets: cmmmech:aragonite.

Native inspection preceded judgment; exact owner/history/schema hashes remain unchanged. Canonical CREATE and distinct inline event are accurately attributed. Final batch gates actually passed and their log is bound.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/aragonite.yaml; Entire frozen maintained record | supports | Every scientific and provenance field independently checked against original evidence. |
| history | history/records/aragonite/2026-10-14T131516Z-codex-f69181.yaml; Entire CREATE sidecar and distinct inline history | supports | Actual actor, timestamp, target and stated curation scope agree. |
| primary | https://doi.org/10.3389/fmicb.2023.1078430; Complete main text, methods, results, discussion, tables and figure captions; original 19-page PDF | supports | Independent full-text assessment supports narrow phase observations and preserved causal/control limitations. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pp.1-2 and Aragonite p.12 | supports | Correct mineral identity and grandfathered status; original-description year is not an approval accession. |
| handbook | https://www.handbookofmineralogy.org/pdfs/aragonite.pdf; Full one-page original identity sheet | supports | Formula and mineral identity are distinct from other carbonate species and elemental calcium. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1402,2745; Current NCBI taxon XML: 1402 species and 2745 genus | supports | Identifier ranks and labels verified; taxonomy does not authenticate a laboratory stock. |
| sequence | https://www.ncbi.nlm.nih.gov/nuccore/MF808044.1; NCBI GenBank full XML, definition and source qualifiers | supports | Partial 16S source designation checked; strain Y1, taxon 1402. |
| binding | /private/tmp/cmm-round72-carbonates-independent/source-hashes.json; Actual nonempty artifacts, byte sizes and SHA256; failed HTML image routes explicitly excluded | context_only | Primary, SI and original graphics bound to actual successful artifacts, independently examined. |
| dedup | /private/tmp/cmm-round72-carbonates-independent/dedup.json; Main/worktree scientific trees plus four current/referenced raw roots | context_only | Ignored and hidden files included and symlinks followed. Related carbonate studies are not independent replication; no global absence claim. |
| notices | /private/tmp/cmm-round72-carbonates-independent/search.json; 2026-10-14 exact DOI correction/retraction queries and organism/phase contradiction searches | context_only | No applicable notice surfaced in returned windows. This is bounded search evidence, not proof that no notice or conflicting study exists. |
| named | /private/tmp/cmm-round72-carbonates-independent/named.log; Reviewer independently executed named strict validation | supports | Two reviewed records checked, zero failed. |
| batch | /private/tmp/cmm-round72-final-gates.json; Coordinator terminal receipt, exact base and commands | supports | All three actual commands exited 0; shared batch317passed/3skipped,341records/0fail,394histories/0errors. Reviewer verified receipt and log bytes. |
| batch_log | /private/tmp/cmm-round72-final-gates.log; Complete terminal log | supports | Exact log SHA matches receipt; structural tests do not establish scientific truth. |
| si_tables | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Data_Sheet_1_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.DOCX | context_only | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_10 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_10_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_11 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_11_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_12 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_12_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_13 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_13_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_14 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_14_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_1 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_1_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_2 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_2_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_3 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_3_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_4 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_4_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_5 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_5_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_6 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_6_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_7 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_7_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.PNG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_8 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_8_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |
| si_9 | https://doi.org/10.3389/fmicb.2023.1078430; Supplementary Image_9_The incorporation of Mg2+ ions into aragonite during biomineralization: Implications for the dolomitization of aragonite.JPEG | supports | Original supplementary artifact checked within disclosed visual scope. FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic experiment. |

## Limits And Additional Notes

- No raw diffraction refit or laboratory replication; phase claims remain author assignments among fitted crystalline phases.
- Original Han2023 TablesS1-S6 significance matrices are embedded EMF and were not visually rendered. Their titles were inspected, but no curated numerical claim relies on those matrices. S7 text and S8 original PNG were checked.
- Primary downloads were shared with the curator but independently read and visually assessed; no primary reacquisition performed.
- Mg coordination and causal necessity remain unresolved; no mass-balance recovery or industrial deployment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T132400Z-aragonite-round72-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of aragonite
started_at: '2026-10-14T13:16:56.854077Z'
finished_at: '2026-10-14T13:24:00.738181Z'
reviewer:
  identity: codex /root/round68_iron_sulfides
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Phosphates agent authored this owner/history. Reviewer authored
    only realgar/orpiment this round and did not edit the reviewed owners. Shared
    originals independently read, graphics checked, identifiers and current notices
    assessed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The qualified mineral phase record is supported by original evidence. Source
  and control limitations are preserved; no corrective findings. Named and final batch
  checks passed.
source:
  git_revision: a2f08edab1307aba4281ce1e2a54d84bca88a889
  state: working_tree
  inputs:
  - path: data/records/aragonite.yaml
    sha256: bf984de0c66475279d0fe5f75e450a59e4267955b8c399575cd000a4559f541a
    role: target
  - path: history/records/aragonite/2026-10-14T131516Z-codex-f69181.yaml
    sha256: a5e487edffb038f274634c3610a557c6a5b89d1f94bce07a49a68850d7ac31ed
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Complete maintained owner and linked canonical CREATE, independently
    reassessed against full primary evidence and authority.
  selection: Assigned frozen owner; native inspection before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:aragonite
targets:
- target_id: cmmmech:aragonite
  path: data/records/aragonite.yaml
  label: Aragonite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aragonite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named strict validation
  command: uv run --locked cmmmech validate data/records/aragonite.yaml data/records/monohydrocalcite.yaml
    --require-records
  status: passed
  required: true
  summary: Reviewer independently executed:2 checked, 0 failed.
  target_ids:
  - cmmmech:aragonite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Completed batch checks
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base a2f08edab1307aba4281ce1e2a54d84bca88a889
  status: passed
  required: true
  summary: Coordinator executed; reviewer verified terminal receipt/log SHA and all
    exit codes.317 passed, 3 skipped; 341 records, 0 failures; 394 histories, 0 errors.
  target_ids:
  - cmmmech:aragonite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
  - batch_log
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/aragonite.yaml
  locator: Entire frozen maintained record
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Every scientific and provenance field independently checked against original
    evidence.
  snapshot_sha256: bf984de0c66475279d0fe5f75e450a59e4267955b8c399575cd000a4559f541a
- evidence_id: history
  kind: record_content
  reference: history/records/aragonite/2026-10-14T131516Z-codex-f69181.yaml
  locator: Entire CREATE sidecar and distinct inline history
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Actual actor, timestamp, target and stated curation scope agree.
  snapshot_sha256: a5e487edffb038f274634c3610a557c6a5b89d1f94bce07a49a68850d7ac31ed
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: Complete main text, methods, results, discussion, tables and figure captions;
    original 19-page PDF
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Independent full-text assessment supports narrow phase observations and
    preserved causal/control limitations.
  snapshot_sha256: 526aacb8bef895c06f7560b5030ce41db554eb1f3138b08b7881625f03fecef7
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pp.1-2 and Aragonite p.12
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Correct mineral identity and grandfathered status; original-description
    year is not an approval accession.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/aragonite.pdf
  locator: Full one-page original identity sheet
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Formula and mineral identity are distinct from other carbonate species
    and elemental calcium.
  snapshot_sha256: ed2c4e9c023838281f838bbc483922f0d6626eceb267d936244abaf14ee99184
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1402,2745
  locator: 'Current NCBI taxon XML: 1402 species and 2745 genus'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Identifier ranks and labels verified; taxonomy does not authenticate a
    laboratory stock.
  snapshot_sha256: 299ffaa876b8e90b7deefd64f4342fbcc696155fc18a997a1fc195ecbd0f3793
- evidence_id: sequence
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/MF808044.1
  locator: NCBI GenBank full XML, definition and source qualifiers
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Partial 16S source designation checked; strain Y1, taxon 1402.
  snapshot_sha256: 2e671eadad79b12c62bf9ae4a7bd4fa4e087d0df553d84ced00b908409ed4dba
- evidence_id: binding
  kind: validation
  reference: /private/tmp/cmm-round72-carbonates-independent/source-hashes.json
  locator: Actual nonempty artifacts, byte sizes and SHA256; failed HTML image routes
    explicitly excluded
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: context_only
  summary: Primary, SI and original graphics bound to actual successful artifacts,
    independently examined.
  snapshot_sha256: 7fc7a7cd327f3657b1d2ad46950f8d0edc925b05f0a38fdb94926fc5b324b625
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round72-carbonates-independent/dedup.json
  locator: Main/worktree scientific trees plus four current/referenced raw roots
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: context_only
  summary: Ignored and hidden files included and symlinks followed. Related carbonate
    studies are not independent replication; no global absence claim.
  snapshot_sha256: bf04900b32e1274b00a8c4ba79a1bd68c5fc95fc04bc799b6347df7a88a60952
  search_scope: Exact command and every root retained in JSON; record/research/reviews/history
    in both checkouts and selected referenced raw roots.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round72-carbonates-independent/search.json
  locator: 2026-10-14 exact DOI correction/retraction queries and organism/phase contradiction
    searches
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: context_only
  summary: No applicable notice surfaced in returned windows. This is bounded search
    evidence, not proof that no notice or conflicting study exists.
  snapshot_sha256: 00c6d326d7565cdcc4bca97515b3726789a7cce1bf36a87d5e8b80ec4fcd0522
  search_scope: Four exact queries retained, no domain/date restriction; unrelated
    taxon/application hits excluded.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round72-carbonates-independent/named.log
  locator: Reviewer independently executed named strict validation
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Two reviewed records checked, zero failed.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round72-final-gates.json
  locator: Coordinator terminal receipt, exact base and commands
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: All three actual commands exited 0; shared batch317passed/3skipped,341records/0fail,394histories/0errors.
    Reviewer verified receipt and log bytes.
  snapshot_sha256: b5b2d551ac899632844d0d3a3f9dbc95897408e73a7ccec69513cdb22a1352e7
- evidence_id: batch_log
  kind: validation
  reference: /private/tmp/cmm-round72-final-gates.log
  locator: Complete terminal log
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Exact log SHA matches receipt; structural tests do not establish scientific
    truth.
  snapshot_sha256: 55435f8c2e7b77b442f38fee5e21be9920263c32956357e1e1482557ca332c3c
- evidence_id: si_tables
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Data_Sheet_1_The incorporation of Mg2+ ions into aragonite
    during biomineralization: Implications for the dolomitization of aragonite.DOCX'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: context_only
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: a0871cfd7edfacbdf3978b34f6432661470ce991cb8720807d05253afd200096
- evidence_id: si_10
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_10_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 44f270cdc4a560f404e304eba1fcbe73b1d2428e3c88059c5c35456cbebcb583
- evidence_id: si_11
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_11_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: cfec5a9f693a1be132d006a7b8eaba3408b25032054a5a68e9aac80915f2c850
- evidence_id: si_12
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_12_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 770d1640c9ce7297696628b1dfcdeedefde219a41900bd82034278eb85ac274e
- evidence_id: si_13
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_13_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 997ea86112ffa664eaf093313fb6505d9526b23aa460fa454ff34264e6949878
- evidence_id: si_14
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_14_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: e977f97e996e7ad996f00e4a1b82301844760c6c60e9b14dd05d87fde3084b72
- evidence_id: si_1
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_1_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 807bd7a0c560e094e0e5837c994df049fbb5560c14f220e9de76a5f8fac8c362
- evidence_id: si_2
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_2_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 48339bc8a8d90523e0c1a3c37d42b9f52dd5defb223514f259d7a65e30c73601
- evidence_id: si_3
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_3_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: fcb42ac233d6599a0d616c4a5e507fe557b05f4ba98706964758db017c3d2706
- evidence_id: si_4
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_4_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 7376acc328f1d04ef5e3c033d579298abfb4543d0348282fbd8d4204b4adda91
- evidence_id: si_5
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_5_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 3c681cd30594c9381341368c34f50ed4337b3045dcd83968fb74cc4562d9830b
- evidence_id: si_6
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_6_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: dc1ec9ee9c4cac437d85a124e47926cad9293a481a71df0f38395a784ee184e8
- evidence_id: si_7
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_7_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.PNG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 7dfa475db332dfcd6f2dfb3c79ee300733a6833b949cef18b9ea4b59e0293207
- evidence_id: si_8
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_8_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: 837887a1caea86b212b6236b600b73800a9ba66d1e310ea3093af51514bc3f01
- evidence_id: si_9
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1078430
  locator: 'Supplementary Image_9_The incorporation of Mg2+ ions into aragonite during
    biomineralization: Implications for the dolomitization of aragonite.JPEG'
  accessed_at: '2026-10-14T13:23:10.846935Z'
  support: supports
  summary: Original supplementary artifact checked within disclosed visual scope.
    FigureS5 independently supports phase assignments; FigureS13 is a separate abiotic
    experiment.
  snapshot_sha256: e1d1cc0e1f09d69fea73d611321d3b9cbbc8050148ac1094445bf15531f7a63b
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct carbonate species
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - record
  - ima
  - handbook
  summary: Orthorhombic aragonite is correctly separated from calcite/vaterite/MHC
    and calcium. No criticality claim is inherited.
- assessment_id: organism
  area: grounding
  topic: Source-designated Y1
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - primary
  - taxon
  - sequence
  summary: MF808044.1 is a partial 16S submission named B. licheniformis strain Y1,
    consistent with the species mapping but not culture-collection authentication.
- assessment_id: conditions
  area: evidence
  topic: Culture versus abiotic recipe
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - primary
  - record
  summary: Main2.1-2.5 confirms beefextract5g/L,tryptone10g/L,NaCl10g/L,Ca0.01M and
    stated Mg series;1%v/v,triplicate sterile-water controls,37C130rpm,day14/25 harvest.
    Drying temperature and pH-matched phase controls are not supplied. Section2.10
    abiotic carbonate-addition experiment has different recipe and duration.
- assessment_id: phases
  area: evidence
  topic: Time- and Mg/Ca-dependent phase assignments
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - primary
  - si_5
  summary: Original Figure2 and SupplementaryFigure5 E-H support mixed14-day and aragonite-only25-day
    fits at ratios6/9; I-J support ratio12 both times. Fitted crystalline percentages
    are not recovered mass or proof of no amorphous/organic material.
- assessment_id: causality
  area: scope
  topic: EPS, magnesium and dolomitization
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - primary
  - si_13
  - si_14
  summary: Figures3-13 and sections3.6-4.3 distinguish observed associations,bulk
    acid-digest Mg,selected lattice spacings and calculations. Mg coordination and
    alternative replacement/dissolution-reprecipitation mechanisms remain explicitly
    uncertain. The record does not promote selected dolomite domains to a bulk conversion
    yield.
- assessment_id: controls
  area: scope
  topic: Abiotic formation and scale
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - primary
  - si_13
  - record
  summary: SupplementaryFigure13 includes precipitation without biomolecules; this
    does not substitute for a matched culture control. Laboratory mineral formation
    is not metal recovery or deployment.
- assessment_id: provenance
  area: provenance
  topic: Exact owner, history and source binding
  outcome: supported
  target_ids:
  - cmmmech:aragonite
  evidence_ids:
  - record
  - history
  - binding
  - dedup
  - named
  - batch
  - batch_log
  summary: Native inspection preceded judgment; exact owner/history/schema hashes
    remain unchanged. Canonical CREATE and distinct inline event are accurately attributed.
    Final batch gates actually passed and their log is bound.
findings: []
actions: []
limitations:
- No raw diffraction refit or laboratory replication; phase claims remain author assignments
  among fitted crystalline phases.
- Original Han2023 TablesS1-S6 significance matrices are embedded EMF and were not
  visually rendered. Their titles were inspected, but no curated numerical claim relies
  on those matrices. S7 text and S8 original PNG were checked.
- Primary downloads were shared with the curator but independently read and visually
  assessed; no primary reacquisition performed.
- Mg coordination and causal necessity remain unresolved; no mass-balance recovery
  or industrial deployment.
```
