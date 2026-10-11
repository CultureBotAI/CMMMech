# Independent scientific review of the terbium expansion record

- Review: 20261011T060518Z-terbium-round7-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:05:18Z
- Finished UTC: 2026-10-11T06:05:18Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact terbium record is scientifically supportable as a qualified laboratory screen with lyophilized UTEX2973 biomass. It preserves absent matched blank, unidentified salt counter-ion and replicate structure, and excludes Ce-only mechanism extrapolation, fitted Tb capacity and product-recovery claims. No actionable defect remains in the frozen record.

## Scope And Provenance

All scientific, authority and provenance fields in the named final record.

Selection: Named single-record assignment; every field assessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58e7aef16a9643438cf621fa9fb402e9d325dc65.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:terbium | data/records/terbium.yaml | maintained | Terbium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:terbium | Reviewer executed; 1 record, zero failures; terminal exit0. |
| Completed-batch gate | passed | True | cmmmech:terbium | Root executed and inspected /private/tmp/cmm-round7-check.log; 307 passed,3 skipped; lint passed;42 records and52 histories valid; terminal exit0. |
| Nonempty corpus | passed | True | cmmmech:terbium | Root executed;42 records,zero failures; terminal exit0. |
| Trusted-base history | passed | True | cmmmech:terbium | Root executed;52 histories,zero errors; terminal exit0. |

## Scientific And Domain Assessments

### Element and strain scope

identity: supported. Targets: cmmmech:terbium.

Verified element and exact UTEX2973 identity remain separate from the reagent and other strains.

### Dated authority designation

evidence: supported. Targets: cmmmech:terbium.

Named United States final2025 row supports the scoped criticality claim.

### Analyte-specific experiment

evidence: supported. Targets: cmmmech:terbium.

The exact terbium record is scientifically supportable as a qualified laboratory screen with lyophilized UTEX2973 biomass. It preserves absent matched blank, unidentified salt counter-ion and replicate structure, and excludes Ce-only mechanism extrapolation, fitted Tb capacity and product-recovery claims. No actionable defect remains in the frozen record.

### Endpoint and causal limits

quantity: supported. Targets: cmmmech:terbium.

Screening mg/g is not a fitted Tb maximum or recovered-product yield; missing controls and Ce-only detailed experiments are explicit.

### Actual curation provenance

provenance: supported. Targets: cmmmech:terbium.

Distinct inline and sidecar CREATE events identify actual codex/GPT-6/codex work; trusted-base checks preserve previous histories.

### Bounded adversarial search

completeness: supported. Targets: cmmmech:terbium.

Primary limitations and external search coverage are retained honestly.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/terbium.yaml; Whole final record, schema and linked CREATE sidecar | supports | Root independently assessed the final inspected bytes and did not edit the record or its history. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33376; Live ChEBI atom entry, formula and net charge | supports | CHEBI:33376 is terbium atom, Tb with charge zero, distinct from experimental dissolved ion, salt, mineral or resource. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=1350461; Live current name, rank and equivalent name | supports | NCBITaxon:1350461 resolves Synechococcus elongatus UTEX 2973 at no rank, with equivalent Synechococcus sp. UTEX 2973; record uses this exact strain node. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final US2025 list; named terbium table row after page50497 break | supports | Authority, United States jurisdiction, final2025 edition and individual commodity row are verified. The corrected final record cites page50497 and explains mapping to the element without inheriting criticality to all host materials. |
| primary | https://doi.org/10.3389/fbioe.2023.1130939; Publisher full text and acquired article XML; Table1, Sections2.1-2.10,3.2-3.7,4.2 and5 | supports | Methods/results distinguish the Tb single-element dry-biomass screen from Ce-only pH, kinetic, isotherm, competition, ion-release and FTIR experiments. Published uptake is derived from initial/final supernatant concentration, not an isolated-product measurement. |
| figure | https://doi.org/10.3389/fbioe.2023.1130939; Original Figure2, supp/fbioe-11-1130939-g002.jpg | supports | Independent pixel inspection verifies legend order, positive UTEX2973 Tb bar and mg/g dry-biomass screening axis. No graph value, uncertainty or recovery percentage was reconstructed. |
| supplement | https://doi.org/10.3389/fbioe.2023.1130939; Table1.DOCX Supplementary Tables S1 and S2, complete extracted cell text | supports | Both supplementary tables explicitly concern Ce(III) Langmuir/Freundlich parameters; neither establishes a Tb fit, Tb blank or Tb-specific molecular cause. |
| search | Root review-session web searches and local source inventory; 2026-10-11 first returned search result sets; ignored-inclusive local search | context_only | No direct correction/retraction or contrary replication surfaced in the bounded results inspected. Primary XML has no related-article notice; other UTEX2973 uses concern different metals or processes. These checks do not prove universal absence. |

## Limits And Additional Notes

- No matched biomass-free Tb solution-control result is reported; concentration depletion does not exclude all nonspecific losses or prove an exclusive binding mechanism.
- Biomass viability, precise Tb counter-ion, numerical room temperature, strain-specific mass and independent versus technical replication are unspecified.
- Detailed kinetic, pH, ion-exchange, competition and fitted-isotherm evidence concerns cerium; it cannot be transferred to terbium.
- No independent raw-data reanalysis, digitized endpoint, terbium-selective separation, purified yield or industrial deployment was established.
- Correction/counterevidence and duplicate searches are bounded; no literature-wide absence claim is made.
- Source reading began as preparation before the inspect snapshot; the saved assessment covers the subsequently frozen c47181aa12c1c060c9e04e95c96c37552c4ec183032033dbf9f4500c71e40ffb record.
- Root noticed a draft page locator error, but the curator had already independently corrected it before final freeze and before receiving the message. No known defect was reintroduced or manufactured as an issue.
- Working-tree source state is an input-byte attestation at a durable main ancestor, not a claim that new records existed at that commit.
- Source limitations preserved in the record are not corrective curation findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T060518Z-terbium-round7-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the terbium expansion record
started_at: '2026-10-11T06:05:18Z'
finished_at: '2026-10-11T06:05:18Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root is different from curator /root/cmm7_terbium, independently
    read authority/primary evidence and Figure2 pixels, inspected exact target/schema/history
    before formal assessment, and made no record/history edits.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact terbium record is scientifically supportable as a qualified laboratory
  screen with lyophilized UTEX2973 biomass. It preserves absent matched blank, unidentified
  salt counter-ion and replicate structure, and excludes Ce-only mechanism extrapolation,
  fitted Tb capacity and product-recovery claims. No actionable defect remains in
  the frozen record.
source:
  git_revision: 58e7aef16a9643438cf621fa9fb402e9d325dc65
  state: working_tree
  inputs:
  - path: data/records/terbium.yaml
    sha256: c47181aa12c1c060c9e04e95c96c37552c4ec183032033dbf9f4500c71e40ffb
    role: target
  - path: history/records/terbium/2026-10-11T055851Z-codex-8457ec.yaml
    sha256: 9384fa59dc42eaf731209410edeb68fb3e7322e81a9ff362fb7548765d591ed9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific, authority and provenance fields in the named final
    record.
  selection: Named single-record assignment; every field assessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:terbium
targets:
- target_id: cmmmech:terbium
  path: data/records/terbium.yaml
  label: Terbium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/terbium.yaml
    role: maintained
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/terbium.yaml
  status: passed
  required: true
  summary: Reviewer executed; 1 record, zero failures; terminal exit0.
  target_ids:
  - cmmmech:terbium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed-batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Root executed and inspected /private/tmp/cmm-round7-check.log; 307 passed,3
    skipped; lint passed;42 records and52 histories valid; terminal exit0.
  target_ids:
  - cmmmech:terbium
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Root executed;42 records,zero failures; terminal exit0.
  target_ids:
  - cmmmech:terbium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 58e7aef16a9643438cf621fa9fb402e9d325dc65
  status: passed
  required: true
  summary: Root executed;52 histories,zero errors; terminal exit0.
  target_ids:
  - cmmmech:terbium
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/terbium.yaml
  locator: Whole final record, schema and linked CREATE sidecar
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: Root independently assessed the final inspected bytes and did not edit
    the record or its history.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33376
  locator: Live ChEBI atom entry, formula and net charge
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: CHEBI:33376 is terbium atom, Tb with charge zero, distinct from experimental
    dissolved ion, salt, mineral or resource.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=1350461
  locator: Live current name, rank and equivalent name
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: NCBITaxon:1350461 resolves Synechococcus elongatus UTEX 2973 at no rank,
    with equivalent Synechococcus sp. UTEX 2973; record uses this exact strain node.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final US2025 list; named terbium table row after page50497 break
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: Authority, United States jurisdiction, final2025 edition and individual
    commodity row are verified. The corrected final record cites page50497 and explains
    mapping to the element without inheriting criticality to all host materials.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fbioe.2023.1130939
  locator: Publisher full text and acquired article XML; Table1, Sections2.1-2.10,3.2-3.7,4.2
    and5
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: Methods/results distinguish the Tb single-element dry-biomass screen from
    Ce-only pH, kinetic, isotherm, competition, ion-release and FTIR experiments.
    Published uptake is derived from initial/final supernatant concentration, not
    an isolated-product measurement.
  snapshot_sha256: cd9e18823fbb8e79e6c73026132ac2cf9eea4874fd83e3d141f7f2c42bf6bdf0
- evidence_id: figure
  kind: primary_source
  reference: https://doi.org/10.3389/fbioe.2023.1130939
  locator: Original Figure2, supp/fbioe-11-1130939-g002.jpg
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: Independent pixel inspection verifies legend order, positive UTEX2973 Tb
    bar and mg/g dry-biomass screening axis. No graph value, uncertainty or recovery
    percentage was reconstructed.
  snapshot_sha256: e067c81963f4cb8d1aa8cecf35cab21c8ec7fcabf540726170c557e4ed55550f
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.3389/fbioe.2023.1130939
  locator: Table1.DOCX Supplementary Tables S1 and S2, complete extracted cell text
  accessed_at: '2026-10-11T06:05:18Z'
  support: supports
  summary: Both supplementary tables explicitly concern Ce(III) Langmuir/Freundlich
    parameters; neither establishes a Tb fit, Tb blank or Tb-specific molecular cause.
  snapshot_sha256: 26a2eba350e8dc3fc0ba267687accc50510f2df556b9f94cbadc956dc328bc50
- evidence_id: search
  kind: search
  reference: Root review-session web searches and local source inventory
  locator: 2026-10-11 first returned search result sets; ignored-inclusive local search
  accessed_at: '2026-10-11T06:05:18Z'
  support: context_only
  summary: No direct correction/retraction or contrary replication surfaced in the
    bounded results inspected. Primary XML has no related-article notice; other UTEX2973
    uses concern different metals or processes. These checks do not prove universal
    absence.
  search_scope: 'Web queries: "10.3389/fbioe.2023.1130939" correction OR corrigendum
    OR retraction; "Synechococcus elongatus UTEX 2973" terbium biosorption. No exhaustive
    pagination. rg --no-ignore --hidden -L searched data/records,research,reviews,history
    and the task raw directory for cmmmech:terbium, CHEBI:33376 and exact DOI; binary
    files and large XML/HTML/JSON/text were excluded from this root text pass, with
    primary XML and supplementary cell text separately inspected and the curator exhaustive
    bounded dossier checked. Scope includes ignored records and cited research, not
    unrelated machine paths or all literature.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element and strain scope
  outcome: supported
  summary: Verified element and exact UTEX2973 identity remain separate from the reagent
    and other strains.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - record
  - identity
  - taxon
- assessment_id: criticality
  area: evidence
  topic: Dated authority designation
  outcome: supported
  summary: Named United States final2025 row supports the scoped criticality claim.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - record
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Analyte-specific experiment
  outcome: supported
  summary: The exact terbium record is scientifically supportable as a qualified laboratory
    screen with lyophilized UTEX2973 biomass. It preserves absent matched blank, unidentified
    salt counter-ion and replicate structure, and excludes Ce-only mechanism extrapolation,
    fitted Tb capacity and product-recovery claims. No actionable defect remains in
    the frozen record.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - record
  - primary
  - figure
  - supplement
  dimensions:
  - name: biomass
    value: Washed three times, frozen at -80C and lyophilized UTEX2973 biomass.
    definition: Microbial origin does not imply growth-dependent uptake or verified
      loss of viability.
    evidence_ids:
    - record
    - primary
  - name: substrate
    value: Synthetic single-metal Tb solution,10mM; exact counter-ion unspecified.
    definition: The reagent is distinct from elemental root, mineral and actual waste
      feed.
    evidence_ids:
    - record
    - primary
  - name: conditions
    value: 10-20mg dry biomass,2mL solution,pH5+/-0.2,3h shaking at room temperature;triplicate.
    definition: Screening parameters constrain transfer; source does not resolve replicate
      structure or exact strain-specific mass.
    evidence_ids:
    - record
    - primary
  - name: analysis
    value: 10,000rcf5min centrifugation then supernatant ICP-OES;initial/final difference
      normalized to dry biomass.
    definition: Operational solution loss is the measured basis, not recovered product
      or confirmed intracellular metal.
    evidence_ids:
    - record
    - primary
  - name: mechanism_boundary
    value: Ce-only detailed kinetics, pH, fitted isotherms, competition, ion release
      and FTIR.
    definition: Those assays cannot establish corresponding Tb behavior.
    evidence_ids:
    - record
    - primary
  - name: scale
    value: Laboratory synthetic-solution screen; no purified yield or industrial treatment.
    definition: Biomass cultivation volume is not a deployment claim.
    evidence_ids:
    - record
    - primary
- assessment_id: limits
  area: quantity
  topic: Endpoint and causal limits
  outcome: supported
  summary: Screening mg/g is not a fitted Tb maximum or recovered-product yield; missing
    controls and Ce-only detailed experiments are explicit.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - record
  - primary
  - figure
  - supplement
- assessment_id: provenance
  area: provenance
  topic: Actual curation provenance
  outcome: supported
  summary: Distinct inline and sidecar CREATE events identify actual codex/GPT-6/codex
    work; trusted-base checks preserve previous histories.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - record
- assessment_id: search
  area: completeness
  topic: Bounded adversarial search
  outcome: supported
  summary: Primary limitations and external search coverage are retained honestly.
  target_ids:
  - cmmmech:terbium
  evidence_ids:
  - search
findings: []
actions: []
limitations:
- No matched biomass-free Tb solution-control result is reported; concentration depletion
  does not exclude all nonspecific losses or prove an exclusive binding mechanism.
- Biomass viability, precise Tb counter-ion, numerical room temperature, strain-specific
  mass and independent versus technical replication are unspecified.
- Detailed kinetic, pH, ion-exchange, competition and fitted-isotherm evidence concerns
  cerium; it cannot be transferred to terbium.
- No independent raw-data reanalysis, digitized endpoint, terbium-selective separation,
  purified yield or industrial deployment was established.
- Correction/counterevidence and duplicate searches are bounded; no literature-wide
  absence claim is made.
notes:
- Source reading began as preparation before the inspect snapshot; the saved assessment
  covers the subsequently frozen c47181aa12c1c060c9e04e95c96c37552c4ec183032033dbf9f4500c71e40ffb
  record.
- Root noticed a draft page locator error, but the curator had already independently
  corrected it before final freeze and before receiving the message. No known defect
  was reintroduced or manufactured as an issue.
- Working-tree source state is an input-byte attestation at a durable main ancestor,
  not a claim that new records existed at that commit.
- Source limitations preserved in the record are not corrective curation findings.
links:
- research/ingests/round7-terbium-20261011.md
- research/ingests/round7-terbium-20261011.json
- https://github.com/CultureBotAI/CMMMech/issues/34
tags:
- round7
- terbium
- independent-review
- primary-literature
```
