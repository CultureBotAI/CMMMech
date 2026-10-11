# Independent scientific review of electric-arc-furnace dust

- Review: 20261011T154251Z-electric-arc-furnace-dust-round26-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T15:40:13Z
- Finished UTC: 2026-10-11T15:42:51.267497Z
- Reviewer: Codex /root/round24_identity_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen EAF-dust record supports a distinct secondary-resource identity, filtered culture-derived acid leaching and a separate laboratory bioelectrochemical stage. Its evidence retains source contradictions, staged denominators and absent-control limits. No actionable curation defect was found in the reviewed scope.

## Scope And Provenance

All fields, primary evidence, source identifiers and linked history for one frozen EAF-dust record.

Selection: One assigned new round26 record, independently reviewed from its curator.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:electric-arc-furnace-dust | data/records/electric-arc-furnace-dust.yaml | maintained | Electric-arc-furnace dust |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:electric-arc-furnace-dust | Reviewer executed named validation after inspection; terminal exit 0, one record and zero failures. Actual log /private/tmp/cmm-round26-eaf-review-validate.log. |
| Completed batch checks | passed | True | cmmmech:electric-arc-furnace-dust | Coordinating root executed final batch, terminal 0: 308 passed, 3 skipped in 145.97 seconds; 169 records and 190 histories valid. Reviewer read actual final-gates.json and final-batch.log. This check was not rerun by reviewer. |
| Required-record validation | passed | True | cmmmech:electric-arc-furnace-dust | Root terminal 0; actual /private/tmp/cmm-round26-final-require.log reports 169 records and zero failures. Target hash matches gated bytes. |
| Append-only history validation | passed | True | cmmmech:electric-arc-furnace-dust | Root terminal 0; actual /private/tmp/cmm-round26-final-history.log reports 190 histories and zero errors at trusted base. Current sidecar matches captured bytes. |

## Scientific And Domain Assessments

### Process-defined resource and criticality

identity: supported. Targets: cmmmech:electric-arc-furnace-dust.

The resource identity is defensible and distinct from slag, cast-house dust, ore, minerals and elemental zinc. Two sample compositions are not a universal specification.

### Organism resolution and biomass state

evidence: supported. Targets: cmmmech:electric-arc-furnace-dust.

The record assigns source-supported microbial production of a filtered lixiviant and separately an unresolved mixed bioanode. It does not infer cell contact during leaching or taxonomic causality for the MEC.

### Substrate, preparation, conditions and controls

evidence: supported. Targets: cmmmech:electric-arc-furnace-dust.

Detailed conditions match the source without transferring reactor stirring speed to the separate leaching assays. Absent matched acid and electrochemical controls appropriately limit causal/comparative conclusions.

### Conditional outcomes and contradictions

evidence: supported. Targets: cmmmech:electric-arc-furnace-dust.

The record correctly distinguishes leaching fraction, catholyte depletion and selected-metal deposit composition. It preserves unresolved table/figure conflicts and the missing linkage between processing stages.

### Product and scale

evidence: supported. Targets: cmmmech:electric-arc-furnace-dust.

Laboratory process association is supported. Proposed residue reuse, galvanizing use and energy benefits are not presented as measured industrial performance.

### Independent frozen-state review

provenance: supported. Targets: cmmmech:electric-arc-furnace-dust.

Different author and reviewer agents; exact record, sidecar and source dossiers match canonical inspect and gated bytes. Reviewer made no edits to the target or its sources.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/electric-arc-furnace-dust.yaml; All fields, source links, two mechanisms, inline history and history_refs | supports | Exact frozen bytes assessed after successful canonical inspect. Two industrial EAF dusts exemplify a distinct secondary resource; no inherited criticality, universal composition, mineral identification or industrial biological deployment is asserted. |
| primary | https://doi.org/10.1016/j.rcradv.2025.200278; Complete nine-page primary PDF: Methods 2.1–2.7, Results 3.1–3.3, Conclusion; all Figures 1–9 and Tables 1–5 visually inspected on local page renderings | supports | Full main text and actual pixels independently checked. Duplicate 50-mL leaching assays use filtered acid produced upstream by DSM 504; mixed-culture MEC is a separate later stage. Dust 2 Table 5 Zn 29900 mg/L and Fe 3 mg/L at 100 g/L and 10 minutes are correctly scoped; selected-metal electrode analysis supports a Zn-rich deposit without full mass, phase or marketable-purity certification. |
| contradictions | https://doi.org/10.1016/j.rcradv.2025.200278; Abstract versus Results 3.2/Figure 7B; Tables 3–5 versus Figure 6; Methods 2.7 and Results 3.1; Figures 8–9 | supports | Record preserves 48% versus 42% Fe precipitation, Dust 1 table-derived approximately 60.5% versus plotted approximately 30% Zn at 100 g/L/10 minutes, and unclosed linkage from best 29900 mg/L leachate to 1785 mg/L catholyte after reported 1:1 dilution. Reported average calculated acidity and unclear peroxide specification are qualified; no correction or complete sequential mass balance is invented. |
| metric | https://doi.org/10.3389/fmicb.2023.1238853; Analytics and calculations, page 3 Equations 1–2; actual method-page image and surrounding calculation text | context_only | Equation 1 defines recovery as initial minus final catholyte concentration divided by initial concentration. Therefore the 2025 near-total percentage is solution depletion, not independently weighed electrode mass or total dust recovery. Only cited method context was assessed; separate 2023 biological outcomes were not accepted as observations on the 2025 EAF feed. |
| dsm | https://www.dsmz.de/collection/catalogue/details/culture/DSM-504; Live official culture entry: name and DSM number fields; independently opened 2026-10-11 | supports | DSM 504 maps to Acidithiobacillus thiooxidans. This validates the reported accession mapping, not the purity or authentication of the experimental stock. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&amp;mode=Info; Live official Taxonomy ID, current name and rank fields, independently opened 2026-10-11 | supports | NCBITaxon:930 is the species Acidithiobacillus thiooxidans. The unresolved MEC community has no invented species/strain assignment and is not assigned to the upstream acid producer. |
| search | /private/tmp/cmm-round26-eaf-review-web.txt; Independent first-result-set searches and live authority captures; local hidden/ignored/follow receipt /private/tmp/cmm-round26-eaf-review-dedup.txt | context_only | Queries were "10.1016/j.rcradv.2025.200278" correction erratum retraction, and "electric arc furnace dust" "Acidithiobacillus thiooxidans" zinc control sulfuric acid. No affecting notice appeared in those returned sets. A 2026 publisher abstract on EAF bioleaching residues describes chemical-acid advantage for REE extraction; it is a lead requiring full methods, not a quantitative cross-study comparison. Local matches include this target, adjacent cast-house/BOF distinctions and prior frontier/context mentions; no second EAF-dust root was found in that bounded scope. |
| history | history/records/electric-arc-furnace-dust/2026-10-11T153000Z-codex-86367d.yaml; Complete CREATE sidecar and distinct inline event | supports | Actor codex/GPT-6/codex, actual UTC event, target path and issue 93 match the authored scope. Inline timestamp precedes the separate sidecar; neither invents earlier curation. |
| gates | /private/tmp/cmm-round26-final-gates.json; Actual terminal receipt and all three linked logs; reviewer named validation; current input hash recheck | supports | Required batch and history checks are terminal successes, not inferred from running jobs. Target matches the gated hash and every captured input remains unchanged immediately before saving. |

## Limits And Additional Notes

- No matched reagent-acid or acid-generation control establishes biological superiority; filtered acid chemically contacts the dust.
- No matched abiotic/open-circuit MEC or independent reactor replication establishes exclusive microbial causality. Seven cycles share one operating system.
- Dust 1 table/figure disagreement, 48 versus 42% Fe precipitation, calculated-acidity convention and peroxide amount remain unresolved source limitations.
- MEC feed lineage and losses are insufficient to compute total dust-to-product recovery. Solution depletion and selected-metal ICP composition are not complete deposited-mass or phase/purity measurements.
- No supplemental appendix was identified in the inspected nine-page article; author acquisition receipt contains failed conventional probes, not observed supplement links. Original data are stated to be available on request and were not acquired.
- Experimental stock authentication, dust mineral phases, supplier location and anode community taxonomy remain unresolved.
- Notice/conflict and duplicate searches were bounded. Source bytes were acquired by the author, independently read by this reviewer; batch gates were executed by coordinating root and actual terminal receipts read.
- Successful canonical inspect preceded scientific assessment. Two earlier setup attempts failed before capture because system Python lacked PyYAML and an input schema path was wrong; neither is presented as a passing check.
- All nine main pages, Figures 1–9 and Tables 1–5 were visually inspected. The 2023 methods page and Equations 1–2 were visually inspected; no unrelated 2023 experimental result was imported.
- No issue is invented for scientific limitations already preserved by the record. Coordinating root will run the complete structured-bundle gate after saved reviews are assembled.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T154251Z-electric-arc-furnace-dust-round26-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of electric-arc-furnace dust
started_at: '2026-10-11T15:40:13Z'
finished_at: '2026-10-11T15:42:51.267497Z'
reviewer:
  identity: Codex /root/round24_identity_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round24_copper_slag authored this record. Reviewer
    /root/round24_identity_frontier independently captured exact inputs, inspected
    the primary text/figures and cited method context, checked live identifiers and
    controls, and made no target edits. Shared worktree, curator-acquired raw files
    and root-run terminal batch checks are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen EAF-dust record supports a distinct secondary-resource identity,
  filtered culture-derived acid leaching and a separate laboratory bioelectrochemical
  stage. Its evidence retains source contradictions, staged denominators and absent-control
  limits. No actionable curation defect was found in the reviewed scope.
source:
  git_revision: d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9
  state: working_tree
  inputs:
  - path: data/records/electric-arc-furnace-dust.yaml
    sha256: 528841c1923db4f091500d3de5d57d5a13274f8886f9f0a610eafd05e89217b7
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/electric-arc-furnace-dust/2026-10-11T153000Z-codex-86367d.yaml
    sha256: f23e97d1512683cc39f82f54911dccfc8eed6cf3521bb104c02386902d813521
    role: context
  - path: research/ingests/round26-eaf-dust-sources-20261011.json
    sha256: 22edc1f4e914c78b1a2a969636d7ba8703e9c373d58f2ca68159ecadaa8394d1
    role: context
  - path: research/ingests/round26-eaf-dust-sources-20261011.md
    sha256: cc2cdda491f7ecf94341ead96f4e19002726e6acac9eb03042c9ebf9b2ba725d
    role: context
  - path: research/sources/round26-eaf-dust/20261011T153204Z-source-investigation.md
    sha256: cc2cdda491f7ecf94341ead96f4e19002726e6acac9eb03042c9ebf9b2ba725d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields, primary evidence, source identifiers and linked history
    for one frozen EAF-dust record.
  selection: One assigned new round26 record, independently reviewed from its curator.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:electric-arc-furnace-dust
  exclusions:
  - target: Uncurated mechanisms and unpublished original data
    reason: 2023 biological outcome and 2026 REE lead are not imported; underlying
      laboratory data, industrial feasibility and complete mass balances are unavailable.
targets:
- target_id: cmmmech:electric-arc-furnace-dust
  path: data/records/electric-arc-furnace-dust.yaml
  label: Electric-arc-furnace dust
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/electric-arc-furnace-dust.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/electric-arc-furnace-dust.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed named validation after inspection; terminal exit 0, one
    record and zero failures. Actual log /private/tmp/cmm-round26-eaf-review-validate.log.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
- check_id: batch
  name: Completed batch checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Coordinating root executed final batch, terminal 0: 308 passed, 3 skipped
    in 145.97 seconds; 169 records and 190 histories valid. Reviewer read actual final-gates.json
    and final-batch.log. This check was not rerun by reviewer.'
  target_ids:
  - cmmmech:electric-arc-furnace-dust
- check_id: nonempty
  name: Required-record validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root terminal 0; actual /private/tmp/cmm-round26-final-require.log reports
    169 records and zero failures. Target hash matches gated bytes.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
- check_id: history
  name: Append-only history validation
  command: uv run --locked cmmmech validate-history --base d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root terminal 0; actual /private/tmp/cmm-round26-final-history.log reports
    190 histories and zero errors at trusted base. Current sidecar matches captured
    bytes.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/electric-arc-furnace-dust.yaml
  locator: All fields, source links, two mechanisms, inline history and history_refs
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: Exact frozen bytes assessed after successful canonical inspect. Two industrial
    EAF dusts exemplify a distinct secondary resource; no inherited criticality, universal
    composition, mineral identification or industrial biological deployment is asserted.
  snapshot_sha256: 528841c1923db4f091500d3de5d57d5a13274f8886f9f0a610eafd05e89217b7
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.rcradv.2025.200278
  locator: 'Complete nine-page primary PDF: Methods 2.1–2.7, Results 3.1–3.3, Conclusion;
    all Figures 1–9 and Tables 1–5 visually inspected on local page renderings'
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: Full main text and actual pixels independently checked. Duplicate 50-mL
    leaching assays use filtered acid produced upstream by DSM 504; mixed-culture
    MEC is a separate later stage. Dust 2 Table 5 Zn 29900 mg/L and Fe 3 mg/L at 100
    g/L and 10 minutes are correctly scoped; selected-metal electrode analysis supports
    a Zn-rich deposit without full mass, phase or marketable-purity certification.
  snapshot_sha256: 546dd93365556668101e219980f2b6d02301757385331caabd50bddc4a012139
- evidence_id: contradictions
  kind: primary_source
  reference: https://doi.org/10.1016/j.rcradv.2025.200278
  locator: Abstract versus Results 3.2/Figure 7B; Tables 3–5 versus Figure 6; Methods
    2.7 and Results 3.1; Figures 8–9
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: Record preserves 48% versus 42% Fe precipitation, Dust 1 table-derived
    approximately 60.5% versus plotted approximately 30% Zn at 100 g/L/10 minutes,
    and unclosed linkage from best 29900 mg/L leachate to 1785 mg/L catholyte after
    reported 1:1 dilution. Reported average calculated acidity and unclear peroxide
    specification are qualified; no correction or complete sequential mass balance
    is invented.
  snapshot_sha256: 546dd93365556668101e219980f2b6d02301757385331caabd50bddc4a012139
- evidence_id: metric
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1238853
  locator: Analytics and calculations, page 3 Equations 1–2; actual method-page image
    and surrounding calculation text
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: context_only
  summary: Equation 1 defines recovery as initial minus final catholyte concentration
    divided by initial concentration. Therefore the 2025 near-total percentage is
    solution depletion, not independently weighed electrode mass or total dust recovery.
    Only cited method context was assessed; separate 2023 biological outcomes were
    not accepted as observations on the 2025 EAF feed.
  snapshot_sha256: c140d5040a5f0e1525fe91094d66f592a51adfdffac419b0495dbfff8f403c0f
- evidence_id: dsm
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-504
  locator: 'Live official culture entry: name and DSM number fields; independently
    opened 2026-10-11'
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: DSM 504 maps to Acidithiobacillus thiooxidans. This validates the reported
    accession mapping, not the purity or authentication of the experimental stock.
- evidence_id: taxon
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info
  locator: Live official Taxonomy ID, current name and rank fields, independently
    opened 2026-10-11
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: NCBITaxon:930 is the species Acidithiobacillus thiooxidans. The unresolved
    MEC community has no invented species/strain assignment and is not assigned to
    the upstream acid producer.
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round26-eaf-review-web.txt
  locator: Independent first-result-set searches and live authority captures; local
    hidden/ignored/follow receipt /private/tmp/cmm-round26-eaf-review-dedup.txt
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: context_only
  summary: Queries were "10.1016/j.rcradv.2025.200278" correction erratum retraction,
    and "electric arc furnace dust" "Acidithiobacillus thiooxidans" zinc control sulfuric
    acid. No affecting notice appeared in those returned sets. A 2026 publisher abstract
    on EAF bioleaching residues describes chemical-acid advantage for REE extraction;
    it is a lead requiring full methods, not a quantitative cross-study comparison.
    Local matches include this target, adjacent cast-house/BOF distinctions and prior
    frontier/context mentions; no second EAF-dust root was found in that bounded scope.
  search_scope: Two independent web queries, first returned sets only, no pagination.
    rg --no-ignore --hidden --follow across data/records, research, reviews and history.
    Raw primary files and acquisition receipt were inspected; no machine-wide or exhaustive
    literature absence claim.
- evidence_id: history
  kind: record_content
  reference: history/records/electric-arc-furnace-dust/2026-10-11T153000Z-codex-86367d.yaml
  locator: Complete CREATE sidecar and distinct inline event
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: Actor codex/GPT-6/codex, actual UTC event, target path and issue 93 match
    the authored scope. Inline timestamp precedes the separate sidecar; neither invents
    earlier curation.
  snapshot_sha256: f23e97d1512683cc39f82f54911dccfc8eed6cf3521bb104c02386902d813521
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round26-final-gates.json
  locator: Actual terminal receipt and all three linked logs; reviewer named validation;
    current input hash recheck
  accessed_at: '2026-10-11T15:42:51.267497Z'
  support: supports
  summary: Required batch and history checks are terminal successes, not inferred
    from running jobs. Target matches the gated hash and every captured input remains
    unchanged immediately before saving.
  snapshot_sha256: cc38dc4ba880acadda0ace39440d83a1939fa131abad0177eeef959da39e2f7e
assessments:
- assessment_id: identity
  area: identity
  topic: Process-defined resource and criticality
  outcome: supported
  summary: The resource identity is defensible and distinct from slag, cast-house
    dust, ore, minerals and elemental zinc. Two sample compositions are not a universal
    specification.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: EAF steelmaking process defines the actual industrial dust feed; supplier
      location is not supplied.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction, list or edition is assigned to the mixed resource;
      omission is not a not-listed decision.
    evidence_ids:
    - record
- assessment_id: biology
  area: evidence
  topic: Organism resolution and biomass state
  outcome: supported
  summary: The record assigns source-supported microbial production of a filtered
    lixiviant and separately an unresolved mixed bioanode. It does not infer cell
    contact during leaching or taxonomic causality for the MEC.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - primary
  - dsm
  - taxon
  dimensions:
  - name: organism
    value: Acidithiobacillus thiooxidans DSM 504; NCBITaxon:930
    definition: Collection accession and species CURIE identify different levels;
      stock authentication is unverified.
    evidence_ids:
    - primary
    - dsm
    - taxon
  - name: biomass_state
    value: Upstream living sulfur culture; 0.22-micrometre-filtered acid; separate
      living mixed bioanode
    definition: Filtration precedes dust contact. The MEC community is transferred
      from another MEC and not taxonomically resolved here.
    evidence_ids:
    - primary
- assessment_id: design
  area: evidence
  topic: Substrate, preparation, conditions and controls
  outcome: supported
  summary: Detailed conditions match the source without transferring reactor stirring
    speed to the separate leaching assays. Absent matched acid and electrochemical
    controls appropriately limit causal/comparative conclusions.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: feed_and_pretreatment
    value: Two EAF dusts, 99.8% reported dry mass
    definition: 105-degree characterization is not claimed as whole-feed sterilization;
      exact mineral phases and country remain unknown.
    evidence_ids:
    - primary
  - name: acid_and_leaching
    value: 3-L generator, 30 degrees C, 160 rpm, 75 L/h air; duplicate 50-mL assays
    definition: Source-called fed-batch exchanges/reinoculation every two weeks; separate
      assays vary 50–100 g/L, 30–50 degrees C and 2 minutes–24 hours.
    evidence_ids:
    - primary
  - name: MEC_conditions
    value: 220 mL per chamber; mixed anode; seven-day serial cycles; anode held at
      -100 mV versus Ag/AgCl
    definition: Electrode area 12.5 square centimetres, room temperature and 70 rpm.
      Applied anode potential is not a cell voltage.
    evidence_ids:
    - primary
  - name: controls
    value: No matched reagent-acid, uninoculated acid-generation, abiotic-anode or
      open-circuit comparator reported
    definition: Chemical dissolution remains sufficient explanation for the leaching
      stage; microbial advantage and exclusive zinc sink are not demonstrated.
    evidence_ids:
    - primary
- assessment_id: accounting
  area: evidence
  topic: Conditional outcomes and contradictions
  outcome: supported
  summary: The record correctly distinguishes leaching fraction, catholyte depletion
    and selected-metal deposit composition. It preserves unresolved table/figure conflicts
    and the missing linkage between processing stages.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - primary
  - contradictions
  - metric
  dimensions:
  - name: leaching_outcome
    value: Dust 2 approximately 76.67% Zn and 0.02% Fe
    definition: Table 5 concentrations normalized by Table 4 inventory at 100 g/L
      and 10 minutes; 2-minute uncertainty is not assigned to the 10-minute point.
    evidence_ids:
    - primary
  - name: MEC_outcome
    value: 99.9 ± 0.1% average catholyte Zn depletion over seven serial cycles
    definition: Source concentration metric; neither seven independent reactors nor
      an overall dust-to-product yield.
    evidence_ids:
    - primary
    - metric
  - name: deposit
    value: 99.15% Zn among analyzed deposit metals
    definition: Acid-dissolved selected-metal ICP proportions do not establish complete
      dry deposit mass, phase, oxygen content or market specification.
    evidence_ids:
    - primary
  - name: source_conflicts
    value: Fe 48 versus 42%; Dust 1 approximately 60.5 versus 30%; unknown MEC-feed
      linkage
    definition: Conflicts and uncertainties are explicit; no invented corrected values
      or combined process recovery.
    evidence_ids:
    - contradictions
- assessment_id: deployment
  area: evidence
  topic: Product and scale
  outcome: supported
  summary: Laboratory process association is supported. Proposed residue reuse, galvanizing
    use and energy benefits are not presented as measured industrial performance.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: deployment
    value: Laboratory only
    definition: Industrial dust origin does not establish industrial biological operation,
      energy advantage or validated residue safety.
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Independent frozen-state review
  outcome: supported
  summary: Different author and reviewer agents; exact record, sidecar and source
    dossiers match canonical inspect and gated bytes. Reviewer made no edits to the
    target or its sources.
  target_ids:
  - cmmmech:electric-arc-furnace-dust
  evidence_ids:
  - record
  - history
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- No matched reagent-acid or acid-generation control establishes biological superiority;
  filtered acid chemically contacts the dust.
- No matched abiotic/open-circuit MEC or independent reactor replication establishes
  exclusive microbial causality. Seven cycles share one operating system.
- Dust 1 table/figure disagreement, 48 versus 42% Fe precipitation, calculated-acidity
  convention and peroxide amount remain unresolved source limitations.
- MEC feed lineage and losses are insufficient to compute total dust-to-product recovery.
  Solution depletion and selected-metal ICP composition are not complete deposited-mass
  or phase/purity measurements.
- No supplemental appendix was identified in the inspected nine-page article; author
  acquisition receipt contains failed conventional probes, not observed supplement
  links. Original data are stated to be available on request and were not acquired.
- Experimental stock authentication, dust mineral phases, supplier location and anode
  community taxonomy remain unresolved.
- Notice/conflict and duplicate searches were bounded. Source bytes were acquired
  by the author, independently read by this reviewer; batch gates were executed by
  coordinating root and actual terminal receipts read.
notes:
- Successful canonical inspect preceded scientific assessment. Two earlier setup attempts
  failed before capture because system Python lacked PyYAML and an input schema path
  was wrong; neither is presented as a passing check.
- All nine main pages, Figures 1–9 and Tables 1–5 were visually inspected. The 2023
  methods page and Equations 1–2 were visually inspected; no unrelated 2023 experimental
  result was imported.
- No issue is invented for scientific limitations already preserved by the record.
  Coordinating root will run the complete structured-bundle gate after saved reviews
  are assembled.
tags:
- round26
- independent
- scientific-review
- secondary-resource
```
