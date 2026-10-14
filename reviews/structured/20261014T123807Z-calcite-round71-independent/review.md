# Independent scientific review of Calcite

- Review: 20261014T123807Z-calcite-round71-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T12:20:23.677017Z
- Finished UTC: 2026-10-14T12:38:07.327516Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Calcite is supported as a distinct mineral with narrowly scoped laboratory formation evidence. Mixed products, assay contradictions, unresolved controls and shared-study lineage are preserved; no phase-specific recovery or industrial inference.

## Scope And Provenance

Entire final mineral record, canonical history, authority identity and primary laboratory biomineralization evidence.

Selection: Assigned new owner; native inspect before final assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:calcite | data/records/calcite.yaml | maintained | Calcite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:calcite | Reviewer executed named validation: Checked 1 record; 0 failed; exit 0. |
| Completed batch gate | passed | True | cmmmech:calcite | Root execution 2026-10-14T12:34:24.446228+00:00 to 2026-10-14T12:37:22.682639+00:00; retained log hash verified. |
| Completed batch gate | passed | True | cmmmech:calcite | Root execution 2026-10-14T12:37:22.682665+00:00 to 2026-10-14T12:37:28.535953+00:00; retained log hash verified. |
| Completed batch gate | passed | True | cmmmech:calcite | Root execution 2026-10-14T12:37:28.535980+00:00 to 2026-10-14T12:37:31.693947+00:00; retained log hash verified. |

## Scientific And Domain Assessments

### Mineral polymorph and criticality boundaries

identity: supported. Targets: cmmmech:calcite.

Separate CaCO3 mineral owners with authority-backed names and no unsupported accession or inherited criticality. Existing resource owner retains shared experimental lineage.

### Laboratory ureolysis and processed mixed product

evidence: supported. Targets: cmmmech:calcite.

Narrow source-assigned phase presence is defensible. Conditions, biomass, pretreatment, controls and specimen processing are explicit; source timing, assay and model contradictions remain visible.

No claim of lithium product, phase-specific uptake, pure-phase yield, vaterite-to-calcite time course or industrial deployment. TableS7 model output does not validate FigureS7 phase assignment.

### Calcite formation versus terbium-removal causation

evidence: supported. Targets: cmmmech:calcite.

Record restricts outcome to calcite-assigned two-hour solids and preserves Ca-independent early solution depletion, missing matched-pH phase controls and uncertain Tb coordination.

### Exact bytes and immutable history

provenance: supported. Targets: cmmmech:calcite.

Native inspect precedes final judgment; record and sidecar hashes still match. Named and completed batch gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/calcite.yaml; Entire inspected final record | supports | Calcite is supported as a distinct mineral with narrowly scoped laboratory formation evidence. Mixed products, assay contradictions, unresolved controls and shared-study lineage are preserved; no phase-specific recovery or industrial inference. |
| history | history/records/calcite/2026-10-14T121905Z-codex-bcd6cf.yaml; Entire canonical CREATE sidecar and distinct inline curation event | supports | Actual actor/model, target, dates and performed work match; no invented prior authorship. Trusted-base append-only validation passed. |
| batch | /private/tmp/cmm-round71-final-gates.json; Completed commands and retained log hash | supports | Root verified successful just check, nonempty corpus validation and trusted-base history before saving. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions and calcite/vaterite rows, pp.35/227 | supports | CaCO3 polymorphs are separate mineral identities. Calcite G1836 and vaterite A1962 s.p. are status/date notation, not accession identifiers. |
| brine | https://doi.org/10.1039/d5ra06824j; Main Sections2.1–2.2 and4.1–4.7; Figures1–2; full12-page PDF | supports | Read relevant methods/results and original Figure1. Natural unsterilized brine, prepared DSM33 biomass and urea; dried mixed solids. Hour sampling conflicts with ten-minute text; no mineral-specific yield or lithium product. Source-designated comparator remains unverified. |
| si | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12590475/supplementaryFiles; 27-page SI, actual FigureS7 p24; original FigureS5 pp21–22; TablesS1/S2/S5/S7/S9 | supports | Original S7 explicitly labels vaterite1, calcite2, magnesite3. S6 is growth/pH, not diffraction. Separate no-cell comparison and main/SI Mn/Sr differences are preserved. Saturation calculations are not phase proof; no quantitative phase refinement. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1474&amp;mode=Info; Current complete taxonomy XML, TaxId/ScientificName/Rank | supports | NCBITaxon1474 identifies Sporosarcina pasteurii species, not DSM33 strain. |
| strain | https://www.dsmz.de/collection/catalogue/details/culture/DSM-33; Catalogue name, strain designation and type-strain fields | supports | DSM33 is S.pasteurii type strain22; culture identifier is kept distinct from the taxon. |
| search | Web search,2026-10-14; Queries: "10.3389/fmicb.2024.1416731" correction retraction; "10.1039/d5ra06824j" correction retraction; first returned result batches, no pagination | supports | Returned primary publisher/PubMed/PMC records and repository copies did not identify a correction or retraction notice. Bounded search cannot establish global absence. Directly relevant contradictory evidence within both originals was checked. |
| dedup | /private/tmp/cmm-round71-carbonates-root-dedup.txt; Hidden/ignored-inclusive, followed-symlink rg across data/records,research,reviews,history | supports | Existing geothermal-brine owner and prior source dossiers were compared; shared Rehmanji experiment is explicitly linked rather than counted as independent replication. |
| handbook | https://www.handbookofmineralogy.org/pdfs/calcite.pdf; Complete one-page mineral entry | supports | Authority supports distinct calcium carbonate mineral identity and polymorphism. |
| tb | https://doi.org/10.3389/fmicb.2024.1416731; Sections 2.1–2.9, 3.2–3.5, 4; original Figures 1–10 and Tables 1–2; complete 13-page original | supports | Two-hour Ca-supplemented product has calcite-assigned diffraction. Ten-minute removal and high removal without Ca cannot be attributed to calcite. SEM-EDS association does not establish lattice substitution, amorphous precursor identity or pure recovered product. Heat pretreatment and hot reaction are distinct arms. |
| genus | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=400634&amp;mode=Info; Complete current Taxonomy XML,TaxId/ScientificName/Rank | supports | NCBITaxon400634 is Lysinibacillus genus; source-designated DW018 has no authenticated strain accession in this record. |

## Limits And Additional Notes

- Shared downloaded originals were independently inspected; no new experiment or reprocessing of raw diffraction data.
- Formation evidence is laboratory-only, with ex situ preparation and incomplete phase controls.
- Correction/retraction search was bounded to the stated first result batches; no global absence claim.
- Whole-corpus structured review and exact coverage gates will run after immutable reviews are saved.
- No supported corrective defect found in this frozen state. Source limitations remain explicit.
- Start time is the filesystem completion time of the native inspection retained before scientific assessment; preliminary record orientation preceded inspection.
- Raw originals remain outside Git. Whole-batch structured checking and exact coverage follow saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T123807Z-calcite-round71-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Calcite
started_at: '2026-10-14T12:20:23.677017Z'
finished_at: '2026-10-14T12:38:07.327516Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record and CREATE sidecar authored by /root/round68_phosphates.
    Root independently inspected source text, claim-bearing original graphics and
    authorities; root did not edit the scientific record or history. Source downloads
    are shared. Root authors publication documents and helpers.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Calcite is supported as a distinct mineral with narrowly scoped laboratory
  formation evidence. Mixed products, assay contradictions, unresolved controls and
  shared-study lineage are preserved; no phase-specific recovery or industrial inference.
source:
  git_revision: 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec
  state: working_tree
  inputs:
  - path: data/records/calcite.yaml
    sha256: 1438ef08aee436d6f360d78cfaf5667bbf6ec2dcd866ac5e9b8a347c5d145e49
    role: target
  - path: history/records/calcite/2026-10-14T121905Z-codex-bcd6cf.yaml
    sha256: eb45f8b144340e3bbf3e3d0529494b10e751f34f7203c946c986a83942b5b3d6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire final mineral record, canonical history, authority identity
    and primary laboratory biomineralization evidence.
  selection: Assigned new owner; native inspect before final assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:calcite
targets:
- target_id: cmmmech:calcite
  path: data/records/calcite.yaml
  label: Calcite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/calcite.yaml
    role: maintained
checks:
- check_id: named
  name: Reviewer named validation
  command: uv run --locked cmmmech validate data/records/calcite.yaml
  status: passed
  required: true
  summary: 'Reviewer executed named validation: Checked 1 record; 0 failed; exit 0.'
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - record
- check_id: batch_0
  name: Completed batch gate
  command: just check
  status: passed
  required: true
  summary: Root execution 2026-10-14T12:34:24.446228+00:00 to 2026-10-14T12:37:22.682639+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Completed batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Root execution 2026-10-14T12:37:22.682665+00:00 to 2026-10-14T12:37:28.535953+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Completed batch gate
  command: uv run --locked cmmmech validate-history --base 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec
  status: passed
  required: true
  summary: Root execution 2026-10-14T12:37:28.535980+00:00 to 2026-10-14T12:37:31.693947+00:00;
    retained log hash verified.
  target_ids:
  - cmmmech:calcite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/calcite.yaml
  locator: Entire inspected final record
  accessed_at: '2026-10-14T12:38:07.327516Z'
  support: supports
  summary: Calcite is supported as a distinct mineral with narrowly scoped laboratory
    formation evidence. Mixed products, assay contradictions, unresolved controls
    and shared-study lineage are preserved; no phase-specific recovery or industrial
    inference.
  snapshot_sha256: 1438ef08aee436d6f360d78cfaf5667bbf6ec2dcd866ac5e9b8a347c5d145e49
- evidence_id: history
  kind: record_content
  reference: history/records/calcite/2026-10-14T121905Z-codex-bcd6cf.yaml
  locator: Entire canonical CREATE sidecar and distinct inline curation event
  accessed_at: '2026-10-14T12:38:07.327516Z'
  support: supports
  summary: Actual actor/model, target, dates and performed work match; no invented
    prior authorship. Trusted-base append-only validation passed.
  snapshot_sha256: eb45f8b144340e3bbf3e3d0529494b10e751f34f7203c946c986a83942b5b3d6
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round71-final-gates.json
  locator: Completed commands and retained log hash
  accessed_at: '2026-10-14T12:38:07.327516Z'
  support: supports
  summary: Root verified successful just check, nonempty corpus validation and trusted-base
    history before saving.
  snapshot_sha256: 0373e95dc7899e0d2e3cb655ed0be6b3aba46920988dde89cccfb9276e71c5c8
- evidence_id: ima
  kind: primary_source
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions and calcite/vaterite rows, pp.35/227
  support: supports
  summary: CaCO3 polymorphs are separate mineral identities. Calcite G1836 and vaterite
    A1962 s.p. are status/date notation, not accession identifiers.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: brine
  kind: primary_source
  reference: https://doi.org/10.1039/d5ra06824j
  locator: Main Sections2.1–2.2 and4.1–4.7; Figures1–2; full12-page PDF
  support: supports
  summary: Read relevant methods/results and original Figure1. Natural unsterilized
    brine, prepared DSM33 biomass and urea; dried mixed solids. Hour sampling conflicts
    with ten-minute text; no mineral-specific yield or lithium product. Source-designated
    comparator remains unverified.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 3b1dd238e4fb9652d82846dcdb3d304edc667ff918977566d7da05522c6e6af8
- evidence_id: si
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12590475/supplementaryFiles
  locator: 27-page SI, actual FigureS7 p24; original FigureS5 pp21–22; TablesS1/S2/S5/S7/S9
  support: supports
  summary: Original S7 explicitly labels vaterite1, calcite2, magnesite3. S6 is growth/pH,
    not diffraction. Separate no-cell comparison and main/SI Mn/Sr differences are
    preserved. Saturation calculations are not phase proof; no quantitative phase
    refinement.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: d484e7bdfde39ed1e262a0095308a562c7ae971c724de2bc8a0c8564a2beff19
- evidence_id: taxon
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1474&mode=Info
  locator: Current complete taxonomy XML, TaxId/ScientificName/Rank
  support: supports
  summary: NCBITaxon1474 identifies Sporosarcina pasteurii species, not DSM33 strain.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 7b44a61e29e773bb0b1e73801f2a780b94158f2002fd6090081dd4c9c05ef32a
- evidence_id: strain
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-33
  locator: Catalogue name, strain designation and type-strain fields
  support: supports
  summary: DSM33 is S.pasteurii type strain22; culture identifier is kept distinct
    from the taxon.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 7d9adb9513707dbf5b6f222007168cc8d1b565b52a4b3f6e16111912ac5751bb
- evidence_id: search
  kind: search
  reference: Web search,2026-10-14
  locator: 'Queries: "10.3389/fmicb.2024.1416731" correction retraction; "10.1039/d5ra06824j"
    correction retraction; first returned result batches, no pagination'
  support: supports
  summary: Returned primary publisher/PubMed/PMC records and repository copies did
    not identify a correction or retraction notice. Bounded search cannot establish
    global absence. Directly relevant contradictory evidence within both originals
    was checked.
  search_scope: 'Queries: "10.3389/fmicb.2024.1416731" correction retraction; "10.1039/d5ra06824j"
    correction retraction; first returned result batches, no pagination; primary publisher/PubMed/PMC
    result records inspected, no domain/date filter.'
  accessed_at: '2026-10-14T12:38:07.327516Z'
- evidence_id: dedup
  kind: record_content
  reference: /private/tmp/cmm-round71-carbonates-root-dedup.txt
  locator: Hidden/ignored-inclusive, followed-symlink rg across data/records,research,reviews,history
  support: supports
  summary: Existing geothermal-brine owner and prior source dossiers were compared;
    shared Rehmanji experiment is explicitly linked rather than counted as independent
    replication.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 92661a30f363cc4d16e85f8d4882894ed7fc7fd5f7f66247c6c6537a45c0e58f
- evidence_id: handbook
  kind: primary_source
  reference: https://www.handbookofmineralogy.org/pdfs/calcite.pdf
  locator: Complete one-page mineral entry
  support: supports
  summary: Authority supports distinct calcium carbonate mineral identity and polymorphism.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 84e244ab0fc205558685a97b27e962eca5cddc44e9619e5208a91099cc093a67
- evidence_id: tb
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2024.1416731
  locator: Sections 2.1–2.9, 3.2–3.5, 4; original Figures 1–10 and Tables 1–2; complete
    13-page original
  support: supports
  summary: Two-hour Ca-supplemented product has calcite-assigned diffraction. Ten-minute
    removal and high removal without Ca cannot be attributed to calcite. SEM-EDS association
    does not establish lattice substitution, amorphous precursor identity or pure
    recovered product. Heat pretreatment and hot reaction are distinct arms.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 3de1dd0158812ed91ba0ca13e599a9daab9215996388b4df17c03a17f6c8fe9e
- evidence_id: genus
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=400634&mode=Info
  locator: Complete current Taxonomy XML,TaxId/ScientificName/Rank
  support: supports
  summary: NCBITaxon400634 is Lysinibacillus genus; source-designated DW018 has no
    authenticated strain accession in this record.
  accessed_at: '2026-10-14T12:38:07.327516Z'
  snapshot_sha256: 4688b84286c6e723b222abc516052c5ec4c59a6b0bc4f7e75fdb627cac546aed
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral polymorph and criticality boundaries
  outcome: supported
  summary: Separate CaCO3 mineral owners with authority-backed names and no unsupported
    accession or inherited criticality. Existing resource owner retains shared experimental
    lineage.
  evidence_ids:
  - ima
  - dedup
  dimensions:
  - name: criticality
    value: No designation asserted
    definition: A constituent or target metal list does not automatically designate
      this mineral.
    evidence_ids:
    - record
  target_ids:
  - cmmmech:calcite
- assessment_id: brine
  area: evidence
  topic: Laboratory ureolysis and processed mixed product
  outcome: supported
  summary: Narrow source-assigned phase presence is defensible. Conditions, biomass,
    pretreatment, controls and specimen processing are explicit; source timing, assay
    and model contradictions remain visible.
  evidence_ids:
  - brine
  - si
  - taxon
  - strain
  details: No claim of lithium product, phase-specific uptake, pure-phase yield, vaterite-to-calcite
    time course or industrial deployment. TableS7 model output does not validate FigureS7
    phase assignment.
  dimensions:
  - name: scale
    value: Laboratory flask assay
    definition: 100mL brine in250mL flasks,28C,24h static,500mM urea; initialOD6000.05–0.4.
    evidence_ids:
    - brine
  - name: biomass
    value: Prepared mid-log DSM33 cells
    definition: PBS-washed cells, source-described non-growth brine conditions; activity
      not inferred from strain identity alone.
    evidence_ids:
    - brine
    - strain
  target_ids:
  - cmmmech:calcite
- assessment_id: tb
  area: evidence
  topic: Calcite formation versus terbium-removal causation
  outcome: supported
  summary: Record restricts outcome to calcite-assigned two-hour solids and preserves
    Ca-independent early solution depletion, missing matched-pH phase controls and
    uncertain Tb coordination.
  evidence_ids:
  - tb
  - genus
  dimensions:
  - name: conditions
    value: 30mL synthetic Tb assay;OD6001.0;400micromolarTb;25mMCaCl2;2%urea;37C
    definition: Source standard Ca-supplemented assay, distinct from recommended zero-added-Ca/0.5%urea
      condition; percentage basis and Tb counterion unresolved.
    evidence_ids:
    - tb
  target_ids:
  - cmmmech:calcite
- assessment_id: provenance
  area: provenance
  topic: Exact bytes and immutable history
  outcome: supported
  summary: Native inspect precedes final judgment; record and sidecar hashes still
    match. Named and completed batch gates passed.
  target_ids:
  - cmmmech:calcite
  evidence_ids:
  - record
  - history
  - batch
findings: []
actions: []
limitations:
- Shared downloaded originals were independently inspected; no new experiment or reprocessing
  of raw diffraction data.
- Formation evidence is laboratory-only, with ex situ preparation and incomplete phase
  controls.
- Correction/retraction search was bounded to the stated first result batches; no
  global absence claim.
- Whole-corpus structured review and exact coverage gates will run after immutable
  reviews are saved.
notes:
- No supported corrective defect found in this frozen state. Source limitations remain
  explicit.
- Start time is the filesystem completion time of the native inspection retained before
  scientific assessment; preliminary record orientation preceded inspection.
- Raw originals remain outside Git. Whole-batch structured checking and exact coverage
  follow saving.
tags:
- round71
- independent
- calcite
- primary-figures
```
