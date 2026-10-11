# Independent scientific review of lanthanum expansion record

- Review: 20261011T052640Z-lanthanum-round5-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T05:21:45Z
- Finished UTC: 2026-10-11T05:26:40Z
- Reviewer: Codex /root/cmm5_iron (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The lanthanum element identity, dated US designation and deliberately bounded laboratory mechanism are supported by the inspected sources. Source limitations are retained in the record; no actionable findings in the exact reviewed state.

## Scope And Provenance

All scientific fields and current CREATE provenance of this maintained record.

Selection: Assigned named record; complete single-record assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e305dcc67e526e585349c60f849567f4c2bfc835.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lanthanum | data/records/lanthanum.yaml | maintained | Lanthanum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Affected record validation | passed | True | cmmmech:lanthanum | Reviewer executed; 2 records checked, zero failures, terminal exit 0. |
| Append-only history against trusted base | passed | True | cmmmech:lanthanum | Reviewer executed; 42 history records checked, zero errors, terminal exit 0. |
| Nonempty corpus validation | passed | True | cmmmech:lanthanum | Reviewer executed; 32 records checked, zero failures, terminal exit 0. |
| Complete batch gate | passed | True | cmmmech:lanthanum | Parent executed and reported terminal exit 0; reviewer inspected /private/tmp/cmm-round5-check.log: 307 passed, 3 skipped, lint passed, 32 records and 41 histories valid. This gate preceded a subsequent germanium-only wording/history edit; La/Dy bytes stayed unchanged. The reviewer reran affected, corpus and 42-session history gates afterward. |

## Scientific And Domain Assessments

### Material, strain and criticality grounding

identity: supported. Targets: cmmmech:lanthanum.

The element, strain node and dated named-commodity designation are accurately scoped.

### Fungal-supernatant precipitation with chemical comparator

evidence: supported. Targets: cmmmech:lanthanum.

The record follows the strong direct precipitation experiment without making live-cell necessity or unique biological chemistry claims.

### Limits of phase and removal measurements

quantity: supported. Targets: cmmmech:lanthanum.

Inconsistent phosphate formula is left unassigned; 25 mM model/comparator oxalate is not a measured fungal concentration. Authors reported percentages are retained in qualified prose, outside the mg/kg observation contract.

### Distinct inline and canonical CREATE events

provenance: supported. Targets: cmmmech:lanthanum.

Actual actor, times, target paths and changes are consistent; canonical sidecars validate against the trusted base. Reviewer did not alter scientific or provenance bytes.

### Bounded adversarial coverage

completeness: supported. Targets: cmmmech:lanthanum.

Full record scope was tested against direct primary methods/results, relevant figures, authorities and bounded correction/counterevidence search; absence claims remain scoped.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lanthanum.yaml; Entire inspected record; distinct inline CREATE and linked canonical CREATE sidecar | supports | Exact scientific and provenance bytes inspected; actor codex/GPT-6/codex and target agree. Inline event and canonical session are separate actual events. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 list; Federal Register 90:50494-50497, individual row on page 50496 | supports | Live official edition explicitly names lanthanum; this is a named commodity mapping to the elemental record, not a designation for every compound or resource containing it. |
| search | Review-session web search and local corpus inspection; Exact DOI searches with correction/retraction; relevant controls queries; hidden and ignored local search | context_only | The bounded returned sets did not identify a direct correction, retraction or contradictory replication of the curated assay. Original studies supply material counterevidence and unresolved reporting gaps. This is not exhaustive literature clearance. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33336; Live entry ID, preferred label, formula and charge | supports | CHEBI:33336 resolves to lanthanum atom, La, net charge 0. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704; Live current name, taxonomy ID and rank | supports | NCBITaxon:380704 is the no-rank strain node Aspergillus niger ATCC 1015, matching the primary strain. |
| primary | https://doi.org/10.1007/s00253-018-9489-0; PMC6373195 full XML: Methods paragraphs 4-14; Results paragraphs 16-23; Discussion; Figure captions 3-9 | supports | Full methods and relevant results independently read. Culture, supernatant reaction, solution assay, dry precipitate and chemical oxalate comparator support the narrow mechanism. Geochemical calculations are distinguished from measured oxalate or phase evidence. |
| figures | https://doi.org/10.1007/s00253-018-9489-0; Independent visual inspection of original Figure 4,5,7,8,9 JPGs retained under /private/tmp/cmmmech-round5-ree-raw/PMC6373195 | partial | Figure 7 distinguishes precipitate dry mass, removed La amount, removal percentage and pH. Figures 4/8/9 support a concentration-dependent phosphorus-containing mixture; Figure 9 shows La7P3O18 whereas Results says La7P3O8. Figure 5 shows agar oxalate versus separately heated oxide. |

## Limits And Additional Notes

- No raw replicate dataset was reanalysed; reported solution-removal percentages were checked against results and Figure 7 rather than independently reconstructed from the malformed printed removal equation.
- Filtration is coarse and no sterility test is established. Chemical comparator pH and oxalate dose are not matched to fungal supernatant.
- High-La solid composition is mixed and the phosphorus-phase formula is inconsistent; it remains deliberately unspecified. Laboratory synthetic feed does not establish selectivity, real-waste treatment or deployment.
- Independent review used curator-acquired original XML and figure assets with acquisition receipts; live publisher, PubMed, ChEBI, NCBI and Federal Register checks corroborated authority and source identity.
- Assessment started after the inspect snapshot. Source state remains working_tree at the preserved e305 base; this does not attest committed target bytes.
- No record edits were made by reviewer. Source-identified shortcomings are scientific limits already retained, not unresolved curation findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T052640Z-lanthanum-round5-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of lanthanum expansion record
started_at: '2026-10-11T05:21:45Z'
finished_at: '2026-10-11T05:26:40Z'
reviewer:
  identity: Codex /root/cmm5_iron
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/cmm5_ree; captured exact
    target and context hashes before primary scientific assessment, independently
    read source methods/results and images, and made no edits to either reviewed record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The lanthanum element identity, dated US designation and deliberately bounded
  laboratory mechanism are supported by the inspected sources. Source limitations
  are retained in the record; no actionable findings in the exact reviewed state.
source:
  git_revision: e305dcc67e526e585349c60f849567f4c2bfc835
  state: working_tree
  inputs:
  - path: data/records/lanthanum.yaml
    sha256: 29704195a47edf4fdd6dde6b6285bc1a45959675decad1b60b3e5f8368f5d7b6
    role: target
  - path: history/records/lanthanum/2026-10-11T051857Z-codex-3e4940.yaml
    sha256: a5d23d97b462aff1919dd39043f12353bcb65bdf5f51e163806a4ec6d7d76093
    role: context
  - path: research/ingests/round5-ree-20261011.json
    sha256: a2d1b930e718198cfa16e414a6456f0cb3df3a9629105ed7cb23fe474df70bfd
    role: context
  - path: research/ingests/round5-ree-20261011.md
    sha256: 9d797b46d7dadda24447aed1871361ada77c7dda559186bfa22a851045580445
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific fields and current CREATE provenance of this maintained
    record.
  selection: Assigned named record; complete single-record assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lanthanum
targets:
- target_id: cmmmech:lanthanum
  path: data/records/lanthanum.yaml
  label: Lanthanum
  kind: maintained
  record_class: CriticalMineralRecord
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanum.yaml
    role: maintained_record
checks:
- check_id: records
  name: Affected record validation
  status: passed
  required: true
  summary: Reviewer executed; 2 records checked, zero failures, terminal exit 0.
  target_ids:
  - cmmmech:lanthanum
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/lanthanum.yaml data/records/dysprosium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history against trusted base
  status: passed
  required: true
  summary: Reviewer executed; 42 history records checked, zero errors, terminal exit
    0.
  target_ids:
  - cmmmech:lanthanum
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base e305dcc67e526e585349c60f849567f4c2bfc835
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus validation
  status: passed
  required: true
  summary: Reviewer executed; 32 records checked, zero failures, terminal exit 0.
  target_ids:
  - cmmmech:lanthanum
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Complete batch gate
  status: passed
  required: true
  summary: 'Parent executed and reported terminal exit 0; reviewer inspected /private/tmp/cmm-round5-check.log:
    307 passed, 3 skipped, lint passed, 32 records and 41 histories valid. This gate
    preceded a subsequent germanium-only wording/history edit; La/Dy bytes stayed
    unchanged. The reviewer reran affected, corpus and 42-session history gates afterward.'
  target_ids:
  - cmmmech:lanthanum
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lanthanum.yaml
  locator: Entire inspected record; distinct inline CREATE and linked canonical CREATE
    sidecar
  accessed_at: '2026-10-11T05:26:40Z'
  support: supports
  summary: Exact scientific and provenance bytes inspected; actor codex/GPT-6/codex
    and target agree. Inline event and canonical session are separate actual events.
  snapshot_sha256: 29704195a47edf4fdd6dde6b6285bc1a45959675decad1b60b3e5f8368f5d7b6
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 list; Federal Register 90:50494-50497, individual row on page
    50496
  accessed_at: '2026-10-11T05:26:40Z'
  support: supports
  summary: Live official edition explicitly names lanthanum; this is a named commodity
    mapping to the elemental record, not a designation for every compound or resource
    containing it.
- evidence_id: search
  kind: search
  reference: Review-session web search and local corpus inspection
  locator: Exact DOI searches with correction/retraction; relevant controls queries;
    hidden and ignored local search
  accessed_at: '2026-10-11T05:26:40Z'
  support: context_only
  summary: The bounded returned sets did not identify a direct correction, retraction
    or contradictory replication of the curated assay. Original studies supply material
    counterevidence and unresolved reporting gaps. This is not exhaustive literature
    clearance.
  search_scope: '2026-10-11 first returned sets for both exact DOIs plus correction/retraction,
    followed by publisher/PubMed domain-limited queries; controls queries: Biotransformation
    of lanthanum oxalic acid control supernatant; dysprosium Saccharomyces abiotic
    biosorption 2023. Search inspected original publisher/PubMed identities; unrelated
    aggregated correction results were not used as scientific evidence. rg --no-ignore
    --hidden covered data, history, research, reviews and /private/tmp/cmmmech-round5-ree-raw
    for root IDs and exact DOIs. No separate pre-existing maintained root duplicate
    found in that scope.'
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33336
  locator: Live entry ID, preferred label, formula and charge
  accessed_at: '2026-10-11T05:26:40Z'
  support: supports
  summary: CHEBI:33336 resolves to lanthanum atom, La, net charge 0.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=380704
  locator: Live current name, taxonomy ID and rank
  accessed_at: '2026-10-11T05:26:40Z'
  support: supports
  summary: NCBITaxon:380704 is the no-rank strain node Aspergillus niger ATCC 1015,
    matching the primary strain.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-018-9489-0
  locator: 'PMC6373195 full XML: Methods paragraphs 4-14; Results paragraphs 16-23;
    Discussion; Figure captions 3-9'
  accessed_at: '2026-10-11T05:26:40Z'
  support: supports
  summary: Full methods and relevant results independently read. Culture, supernatant
    reaction, solution assay, dry precipitate and chemical oxalate comparator support
    the narrow mechanism. Geochemical calculations are distinguished from measured
    oxalate or phase evidence.
  snapshot_sha256: cc34de8084e11c33383e611691909af9b0f1f69773c5c9541ee73be415eb9d85
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-018-9489-0
  locator: Independent visual inspection of original Figure 4,5,7,8,9 JPGs retained
    under /private/tmp/cmmmech-round5-ree-raw/PMC6373195
  accessed_at: '2026-10-11T05:26:40Z'
  support: partial
  summary: Figure 7 distinguishes precipitate dry mass, removed La amount, removal
    percentage and pH. Figures 4/8/9 support a concentration-dependent phosphorus-containing
    mixture; Figure 9 shows La7P3O18 whereas Results says La7P3O8. Figure 5 shows
    agar oxalate versus separately heated oxide.
assessments:
- assessment_id: identity
  area: identity
  topic: Material, strain and criticality grounding
  outcome: supported
  summary: The element, strain node and dated named-commodity designation are accurately
    scoped.
  target_ids:
  - cmmmech:lanthanum
  evidence_ids:
  - record
  - identity
  - taxon
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Fungal-supernatant precipitation with chemical comparator
  outcome: supported
  summary: The record follows the strong direct precipitation experiment without making
    live-cell necessity or unique biological chemistry claims.
  target_ids:
  - cmmmech:lanthanum
  evidence_ids:
  - primary
  - figures
  - record
  dimensions:
  - name: material
    value: Soluble LaCl3 to lanthanum-containing precipitates; root is elemental La.
    definition: Experimental feed and product are distinct from record identity.
    evidence_ids:
    - record
    - identity
    - primary
  - name: organism
    value: A. niger ATCC 1015; NCBITaxon:380704 strain-level no-rank node.
    definition: Exact organism used to generate supernatant.
    evidence_ids:
    - taxon
    - primary
  - name: biomass_state
    value: 7-day culture followed by 63 micrometre mesh filtration; described as biomass-free,
      not proven sterile.
    definition: Biological contribution is prior production of the precipitation medium.
    evidence_ids:
    - primary
  - name: conditions
    value: '100 mL culture in 250 mL flask, modified nitrate AP1 with 20 g/L glucose,
      initially pH 5.5, 25 C, 125 rpm, dark; harvest pH 3.41 +/- 0.10. Reaction: 9
      mL supernatant + 1 mL La solution, 1-50 mM final, 24 h room-temperature rolling,
      at least triplicate.'
    definition: Separate culture and reaction scale and conditions.
    evidence_ids:
    - primary
  - name: controls
    value: 9 mL 25 mM chemical oxalic acid + 1 mL LaCl3; different pH and unknown
      equivalence to fungal oxalate dose.
    definition: Positive chemical comparator limits claims of unique biological necessity
      or normalized efficiency.
    evidence_ids:
    - primary
    - figures
  - name: outcome
    value: Source reports 100% aqueous removal at 1/3/5 mM and 49.8% at 15 mM; maximal
      23.3 mg dry precipitate per 10 mL reaction at 15 mM.
    definition: Arsenazo III post-centrifugation solution assay and weighed solids
      are different endpoints; neither establishes purified-element yield or zero
      residual independently.
    evidence_ids:
    - primary
    - figures
  - name: deployment
    value: Laboratory synthetic-solute precipitation; separate agar crystals become
      La2O3 after abiotic 1000 C heating.
    definition: No ore extraction, mixed-REE selectivity, actual-waste performance
      or industrial operation demonstrated.
    evidence_ids:
    - primary
    - figures
- assessment_id: uncertainty
  area: quantity
  topic: Limits of phase and removal measurements
  outcome: supported
  summary: Inconsistent phosphate formula is left unassigned; 25 mM model/comparator
    oxalate is not a measured fungal concentration. Authors reported percentages are
    retained in qualified prose, outside the mg/kg observation contract.
  target_ids:
  - cmmmech:lanthanum
  evidence_ids:
  - primary
  - figures
  - record
- assessment_id: provenance
  area: provenance
  topic: Distinct inline and canonical CREATE events
  outcome: supported
  summary: Actual actor, times, target paths and changes are consistent; canonical
    sidecars validate against the trusted base. Reviewer did not alter scientific
    or provenance bytes.
  target_ids:
  - cmmmech:lanthanum
  evidence_ids:
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded adversarial coverage
  outcome: supported
  summary: Full record scope was tested against direct primary methods/results, relevant
    figures, authorities and bounded correction/counterevidence search; absence claims
    remain scoped.
  target_ids:
  - cmmmech:lanthanum
  evidence_ids:
  - search
  - record
findings: []
actions: []
limitations:
- No raw replicate dataset was reanalysed; reported solution-removal percentages were
  checked against results and Figure 7 rather than independently reconstructed from
  the malformed printed removal equation.
- Filtration is coarse and no sterility test is established. Chemical comparator pH
  and oxalate dose are not matched to fungal supernatant.
- High-La solid composition is mixed and the phosphorus-phase formula is inconsistent;
  it remains deliberately unspecified. Laboratory synthetic feed does not establish
  selectivity, real-waste treatment or deployment.
- Independent review used curator-acquired original XML and figure assets with acquisition
  receipts; live publisher, PubMed, ChEBI, NCBI and Federal Register checks corroborated
  authority and source identity.
notes:
- Assessment started after the inspect snapshot. Source state remains working_tree
  at the preserved e305 base; this does not attest committed target bytes.
- No record edits were made by reviewer. Source-identified shortcomings are scientific
  limits already retained, not unresolved curation findings.
links:
- research/ingests/round5-ree-20261011.md
- research/ingests/round5-ree-20261011.json
tags:
- round5
- independent-review
- lanthanum
- primary-literature
- bounded-evidence
```
