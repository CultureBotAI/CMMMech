# Independent scientific review of the tungsten expansion record

- Review: 20261011T054452Z-tungsten-round6-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T05:43:17Z
- Finished UTC: 2026-10-11T05:44:52Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact record supports culture-enhanced operationally filtered tungsten release from the tested impure scheelite concentrate. It retains abiotic dissolution, source graph/composition ambiguities and unresolved energy/phase mechanisms; no actionable curation defect was found.

## Scope And Provenance

All scientific fields, criticality, identifiers and CREATE provenance in the exact maintained target.

Selection: Named single-record assignment; all target fields assessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d09a5611767d94fd196393b31d44cb8cf6657f7f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tungsten | data/records/tungsten.yaml | maintained | Tungsten |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Affected records | passed | True | cmmmech:tungsten | Reviewer executed; two records, zero failures, terminal exit 0. |
| Trusted-base append-only history | passed | True | cmmmech:tungsten | Reviewer executed; 46 histories, zero errors, terminal exit 0. |
| Nonempty corpus | passed | True | cmmmech:tungsten | Reviewer executed; 36 records, zero failures, terminal exit 0. |
| Complete batch gate | passed | True | cmmmech:tungsten | Root executed and read /private/tmp/cmm-round6-check.log; 307 passed, 3 skipped, lint passed, 36 records and 46 histories valid; terminal exit 0. |

## Scientific And Domain Assessments

### Material and taxonomic grounding

identity: supported. Targets: cmmmech:tungsten.

Element identity stays distinct from dissolved reagent, product phases and resource feed; organism scope matches the authority and primary evidence.

### Named jurisdiction/list/edition

evidence: supported. Targets: cmmmech:tungsten.

Designation is tied to the named authority and edition; it is not inherited by every element-bearing compound or resource.

### Experimental assay and its causal boundary

evidence: supported. Targets: cmmmech:tungsten.

The exact record supports culture-enhanced operationally filtered tungsten release from the tested impure scheelite concentrate. It retains abiotic dissolution, source graph/composition ambiguities and unresolved energy/phase mechanisms; no actionable curation defect was found.

### Contradictions, analytical denominator and deployment limits

quantity: supported. Targets: cmmmech:tungsten.

Published inconsistencies and weak causal controls remain explicit; assay response is not converted into pure-metal yield or industrial performance.

### Inline event and canonical CREATE session

provenance: supported. Targets: cmmmech:tungsten.

Record and actual codex/GPT-6/codex sidecar name the same target and work; append-only validation used the trusted pre-curation base.

### Bounded adversarial searches

completeness: supported. Targets: cmmmech:tungsten.

Hidden and ignored records, research, reviews, history and task downloads were searched; returned correction/counterevidence results do not establish exhaustive literature clearance.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/tungsten.yaml; Whole record and attached canonical CREATE session | supports | Exact target/schema/history hashes inspected; no reviewer edits. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:27998; Live ChEBI atom page | supports | CHEBI:27998 resolves to tungsten atom, W with zero charge; not scheelite, tungstate or tungsten carbide. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final US2025 list, named tungsten row, FederalRegister90:50494-50497 | supports | Live official edition identifies named tungsten commodity; material-specific scope is retained. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=43687; Live name/rank/type-strain designations; retained original NCBI XML | supports | NCBITaxon43687 identifies Metallosphaera sedula species and lists DSM5348 among type-strain designations; record keeps the experimental culture separate from species-level ID. |
| primary | https://doi.org/10.3389/fmicb.2019.01492; PMC6614383 complete XML and original publisher PDF; Materials and Methods, Results and Discussion, Conclusion | supports | Independent full methods/results assessment supports filtered-phase tungsten enhancement in inoculated culture versus uninoculated concentrate controls. It also discloses actual-energy-source uncertainty, possible indirect/abiotic chemistry, sample processing and need for additional W-environment spectroscopy. |
| figures | https://doi.org/10.3389/fmicb.2019.01492; Original PDF pages3-9, Figures1-7 and Table1; independent local rendered-pixel inspection | supports | Visual inspection confirms qualitative culture/control separation in Figure3A, impure feed composition, growth/attachment images and surface W association. The x-axis/caption days/hours and log10/mg/L wording are inconsistent. No concentration was digitized or exponentiated. EELS carbon-edge similarity and FFT spots were inspected as published comparisons, not independently reindexed phase proof. |
| supplement | https://doi.org/10.3389/fmicb.2019.01492; Main XML supplementary links SM1/SM2; acquisition receipt in dossier | context_only | The main source links supplemental microscopy material/video. Curator download timed out without usable files. Reviewer did not inspect supplemental content or video and does not rely on them for the accepted Figure3 release comparison. |
| search | Review-session web searches and local ignored-inclusive search; 2026-10-11 first returned sets, no filters or pagination | context_only | No direct correction/retraction or contrary replication surfaced in inspected returned results. A later desiccation paper is a distinct investigation, not a replication of release efficiency. No exhaustive absence is asserted. |

## Limits And Additional Notes

- Primary Figure3 has inconsistent time/ordinate descriptions; exact numerical extraction or recovery calculation was intentionally not accepted.
- The concentrate is impure and its Fe composition descriptions conflict. Actual oxidizable energy source and direct versus indirect dissolution contribution are unresolved.
- Processed-cell microscopy is not in-vivo phase stoichiometry or isolated pure-WC evidence. No total-W mass balance or isolated recovery yield is supplied.
- Supplementary microscopy/video were not acquired or inspected; accepted release comparison is supported by complete main methods/results and original Figure3.
- No raw replicate data reanalysis or independent crystallographic reindexing was performed. Bounded searches cannot certify that all contradictory literature is absent.
- Primary-source reading began as preparation before the inspect snapshot; formal target assessment started after inspect. All target bytes remained unchanged through save.
- Source state is working_tree at a retained main ancestor; this is not a claim that target bytes were committed at that base.
- Scientific limits already preserved in the record are not manufactured curation defects.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T054452Z-tungsten-round6-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the tungsten expansion record
started_at: '2026-10-11T05:43:17Z'
finished_at: '2026-10-11T05:44:52Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/cmm6_molybdenum_tungsten.
    Root independently read primary methods/results, original figure pixels and authority
    evidence; captured target/history/schema hashes before formal assessment. Root
    made no scientific or history edits to this record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact record supports culture-enhanced operationally filtered tungsten
  release from the tested impure scheelite concentrate. It retains abiotic dissolution,
  source graph/composition ambiguities and unresolved energy/phase mechanisms; no
  actionable curation defect was found.
source:
  git_revision: d09a5611767d94fd196393b31d44cb8cf6657f7f
  state: working_tree
  inputs:
  - path: data/records/tungsten.yaml
    sha256: d87ad7f8783feba23aace69512babacfd006e26190e49196d446b9b9c7bc40fa
    role: target
  - path: history/records/tungsten/2026-10-11T054211Z-codex-657b0a.yaml
    sha256: 7018faa0e51868cab1e74f938a78985f8d9ec0f78989042a30490d674fc98ff6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific fields, criticality, identifiers and CREATE provenance
    in the exact maintained target.
  selection: Named single-record assignment; all target fields assessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tungsten
targets:
- target_id: cmmmech:tungsten
  path: data/records/tungsten.yaml
  label: Tungsten
  kind: maintained
  record_class: CriticalMineralRecord
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tungsten.yaml
    role: maintained_record
checks:
- check_id: named
  name: Affected records
  status: passed
  required: true
  summary: Reviewer executed; two records, zero failures, terminal exit 0.
  target_ids:
  - cmmmech:tungsten
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/molybdenum.yaml data/records/tungsten.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base append-only history
  status: passed
  required: true
  summary: Reviewer executed; 46 histories, zero errors, terminal exit 0.
  target_ids:
  - cmmmech:tungsten
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base d09a5611767d94fd196393b31d44cb8cf6657f7f
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus
  status: passed
  required: true
  summary: Reviewer executed; 36 records, zero failures, terminal exit 0.
  target_ids:
  - cmmmech:tungsten
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Complete batch gate
  status: passed
  required: true
  summary: Root executed and read /private/tmp/cmm-round6-check.log; 307 passed, 3
    skipped, lint passed, 36 records and 46 histories valid; terminal exit 0.
  target_ids:
  - cmmmech:tungsten
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/tungsten.yaml
  locator: Whole record and attached canonical CREATE session
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: Exact target/schema/history hashes inspected; no reviewer edits.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27998
  locator: Live ChEBI atom page
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: CHEBI:27998 resolves to tungsten atom, W with zero charge; not scheelite,
    tungstate or tungsten carbide.
  snapshot_sha256: d0783c0eeed3abe90226b674c436c646bbbee926c3ed82a32b2cb13b6227f79b
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final US2025 list, named tungsten row, FederalRegister90:50494-50497
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: Live official edition identifies named tungsten commodity; material-specific
    scope is retained.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=43687
  locator: Live name/rank/type-strain designations; retained original NCBI XML
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: NCBITaxon43687 identifies Metallosphaera sedula species and lists DSM5348
    among type-strain designations; record keeps the experimental culture separate
    from species-level ID.
  snapshot_sha256: 134cef049bb3640b8c986f089500c3a2d47c0146d133b1f190c8bc9bde19dc53
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2019.01492
  locator: PMC6614383 complete XML and original publisher PDF; Materials and Methods,
    Results and Discussion, Conclusion
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: Independent full methods/results assessment supports filtered-phase tungsten
    enhancement in inoculated culture versus uninoculated concentrate controls. It
    also discloses actual-energy-source uncertainty, possible indirect/abiotic chemistry,
    sample processing and need for additional W-environment spectroscopy.
  snapshot_sha256: 6e00c962bc622a0a902172474167f2a26dec2022eaba078fb1dd0f7ad82f5724
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2019.01492
  locator: Original PDF pages3-9, Figures1-7 and Table1; independent local rendered-pixel
    inspection
  accessed_at: '2026-10-11T05:44:52Z'
  support: supports
  summary: Visual inspection confirms qualitative culture/control separation in Figure3A,
    impure feed composition, growth/attachment images and surface W association. The
    x-axis/caption days/hours and log10/mg/L wording are inconsistent. No concentration
    was digitized or exponentiated. EELS carbon-edge similarity and FFT spots were
    inspected as published comparisons, not independently reindexed phase proof.
  snapshot_sha256: e493f15bf233713838fc9728c59587cc79abd59442b211001330c67ccfe4d8a4
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2019.01492
  locator: Main XML supplementary links SM1/SM2; acquisition receipt in dossier
  accessed_at: '2026-10-11T05:44:52Z'
  support: context_only
  summary: The main source links supplemental microscopy material/video. Curator download
    timed out without usable files. Reviewer did not inspect supplemental content
    or video and does not rely on them for the accepted Figure3 release comparison.
- evidence_id: search
  kind: search
  reference: Review-session web searches and local ignored-inclusive search
  locator: 2026-10-11 first returned sets, no filters or pagination
  accessed_at: '2026-10-11T05:44:52Z'
  support: context_only
  summary: No direct correction/retraction or contrary replication surfaced in inspected
    returned results. A later desiccation paper is a distinct investigation, not a
    replication of release efficiency. No exhaustive absence is asserted.
  search_scope: 'Queries: "10.3389/fmicb.2019.01492" correction retraction; "Metallosphaera"
    "scheelite" tungsten carbide artifacts control. Primary publisher/PMC versions
    inspected. rg --no-ignore --hidden covered data/records,research,reviews,history
    and /private/tmp/cmmmech-round6-mo-w-raw for exact DOI/rootIDs. No pre-existing
    separate maintained W root found in that scope; all home/temp trees and all literature
    are excluded from absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Material and taxonomic grounding
  outcome: supported
  summary: Element identity stays distinct from dissolved reagent, product phases
    and resource feed; organism scope matches the authority and primary evidence.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - record
  - identity
  - taxon
- assessment_id: criticality
  area: evidence
  topic: Named jurisdiction/list/edition
  outcome: supported
  summary: Designation is tied to the named authority and edition; it is not inherited
    by every element-bearing compound or resource.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - record
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Experimental assay and its causal boundary
  outcome: supported
  summary: The exact record supports culture-enhanced operationally filtered tungsten
    release from the tested impure scheelite concentrate. It retains abiotic dissolution,
    source graph/composition ambiguities and unresolved energy/phase mechanisms; no
    actionable curation defect was found.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - record
  - primary
  - figures
  dimensions:
  - name: material
    value: Impure scheelite concentrate from Serido Province,Brazil;10g/L,average1mm;
      Fe/Mn and other constituents.
    definition: Element W is distinct from a pure mineral root and the experimental
      concentrate.
    evidence_ids:
    - primary
    - record
  - name: organism
    value: M. sedula DSM5348; NCBITaxon43687 species-level ID.
    definition: Culture identifier is source-reported; species ID is not a universal
      strain claim.
    evidence_ids:
    - primary
    - record
  - name: conditions
    value: Aerobic73C withCO2,DSMZ88,initialpH2H2SO4,no further pH adjustment;21-day
      assay;feed180C at least24h plus121C20min.
    definition: Exact pretreatment and culture conditions constrain transfer.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Uninoculated medium with identically sterilized concentrate; appreciable
      abiotic release.
    definition: Comparator supports culture-associated enhancement, not exclusive
      direct microbial dissolution.
    evidence_ids:
    - primary
    - record
  - name: analytical_basis
    value: Centrifuged supernatant,0.44micrometre filtration,ICP-OES;Figure3 n=3biological
      replicates,SD.
    definition: Operational filtered-phase signal is not W speciation or whole-system
      mass balance.
    evidence_ids:
    - primary
    - record
  - name: outcome
    value: Qualitatively higher W in inoculated samples; published figure-label ambiguity
      prevents exact numerical concentration/recovery extraction.
    definition: No inferred logarithmic conversion or pseudo-precise digitized endpoint.
    evidence_ids:
    - primary
    - record
  - name: mechanism_limits
    value: Actual growth energy source unconfirmed; Fe/Mn-mediated disruption,indirect
      chemistry and acid dissolution remain possibilities.
    definition: Growth on impure concentrate does not prove energy conservation from
      W/pure scheelite.
    evidence_ids:
    - primary
    - record
  - name: phase_and_scale
    value: Surface W in processed cells;30-day oxic drying andFIB preparation;carbide-like
      authors interpretation. Laboratory only.
    definition: No pure WC phase, in-vivo product stoichiometry, isolated yield or
      industrial deployment is established.
    evidence_ids:
    - primary
    - record
- assessment_id: uncertainty
  area: quantity
  topic: Contradictions, analytical denominator and deployment limits
  outcome: supported
  summary: Published inconsistencies and weak causal controls remain explicit; assay
    response is not converted into pure-metal yield or industrial performance.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - record
  - primary
  - figures
- assessment_id: provenance
  area: provenance
  topic: Inline event and canonical CREATE session
  outcome: supported
  summary: Record and actual codex/GPT-6/codex sidecar name the same target and work;
    append-only validation used the trusted pre-curation base.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded adversarial searches
  outcome: supported
  summary: Hidden and ignored records, research, reviews, history and task downloads
    were searched; returned correction/counterevidence results do not establish exhaustive
    literature clearance.
  target_ids:
  - cmmmech:tungsten
  evidence_ids:
  - search
findings: []
actions: []
limitations:
- Primary Figure3 has inconsistent time/ordinate descriptions; exact numerical extraction
  or recovery calculation was intentionally not accepted.
- The concentrate is impure and its Fe composition descriptions conflict. Actual oxidizable
  energy source and direct versus indirect dissolution contribution are unresolved.
- Processed-cell microscopy is not in-vivo phase stoichiometry or isolated pure-WC
  evidence. No total-W mass balance or isolated recovery yield is supplied.
- Supplementary microscopy/video were not acquired or inspected; accepted release
  comparison is supported by complete main methods/results and original Figure3.
- No raw replicate data reanalysis or independent crystallographic reindexing was
  performed. Bounded searches cannot certify that all contradictory literature is
  absent.
notes:
- Primary-source reading began as preparation before the inspect snapshot; formal
  target assessment started after inspect. All target bytes remained unchanged through
  save.
- Source state is working_tree at a retained main ancestor; this is not a claim that
  target bytes were committed at that base.
- Scientific limits already preserved in the record are not manufactured curation
  defects.
links:
- research/ingests/round6-mo-w-20261011.md
- research/ingests/round6-mo-w-20261011.json
- https://github.com/CultureBotAI/CMMMech/issues/32
tags:
- round6
- independent-review
- tungsten
- primary-literature
```
