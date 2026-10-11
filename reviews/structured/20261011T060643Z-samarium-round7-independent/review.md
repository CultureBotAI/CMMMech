# Independent scientific review of the round 7 samarium record

- Review: 20261011T060643Z-samarium-round7-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:03:43Z
- Finished UTC: 2026-10-11T06:06:43Z
- Reviewer: Codex /root/cmm7_ho_er_gd (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Samarium identity, dated US2025 criticality and carefully bounded culture-associated sorption are supported. Exact supplementary measurements take precedence over inconsistent narrative summaries. No actionable curation findings in the frozen record; source/control/visual-access limits remain explicit.

## Scope And Provenance

All scientific fields, source references, inline and canonical CREATE provenance of one maintained element record.

Selection: Assigned named record; full target assessment, with stated primary-image and follow-up access limitations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58e7aef16a9643438cf621fa9fb402e9d325dc65.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:samarium | data/records/samarium.yaml | maintained | Samarium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Affected record validation | passed | True | cmmmech:samarium | Reviewer executed: 2 records checked, zero failures; terminal exit 0. |
| Append-only history gate | passed | True | cmmmech:samarium | Reviewer executed: 52 history sessions checked, zero errors; terminal exit 0. |
| Nonempty full corpus gate | passed | True | cmmmech:samarium | Reviewer executed: 42 records checked, zero failures; terminal exit 0. |
| Complete batch check | passed | True | cmmmech:samarium | Parent executed and reported terminal exit 0; reviewer read /private/tmp/cmm-round7-check.log: lint passed, 307 tests passed, 3 skipped in 51.17s, 42 records and 52 histories valid. Frozen reviewed target bytes were unchanged. |

## Scientific And Domain Assessments

### Element and experimental strain identity

identity: supported. Targets: cmmmech:samarium.

The neutral element, experimental nitrate/ion context, catalogue strain and taxonomy mapping are accurately separated.

### Jurisdiction, list, edition and commodity scope

grounding: supported. Targets: cmmmech:samarium.

The individual 2025 US row supports the stated dated designation without extending it to every host mineral or compound.

### Qualified culture-associated biosorption

evidence: supported. Targets: cmmmech:samarium.

The source supports reduced supernatant element and qualitative biomass enrichment. The record does not convert this association into isolated product recovery or an exclusively metabolic mechanism.

### Exact supplementary cells versus conflicting summaries

quantity: supported. Targets: cmmmech:samarium.

Cell values, units, dose/medium arms and timing were checked directly. Derived percentages are labeled as calculations; RSD statistics remain unresolved; mmol/L data are not coerced into the mg/kg observation contract.

### Source contradictions and later evidence

consistency: supported. Targets: cmmmech:samarium.

The record preserves source disagreements and limits the later literature to what the inspected methods establish. It does not turn lack of proof in one series into a universal impossibility claim.

### Actual CREATE events and immutable base

provenance: supported. Targets: cmmmech:samarium.

Inline curation and canonical history are distinct actual UTC events. Actor codex/GPT-6/codex, target and issue 34 agree; no reviewed record/history edits were made by reviewer.

### Bounded scientific review

completeness: supported. Targets: cmmmech:samarium.

All record fields assessed; source access and image limitations retained explicitly. Current hashes match the inspected state and offline gates are green.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/samarium.yaml; All scientific fields, source links, inline event and linked canonical CREATE session | supports | Exact frozen bytes inspected after initial inspect; recapture added completed dossier context without changing target hashes. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:33374; Preferred ID and name, formula and net charge | supports | 33374 resolves to samarium atom, formula Sm, charge 0. Web open failed; independent direct HTML retrieval succeeded and the exact fields were read. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final US2025 list, Federal Register 90:50494-50497; page 50497 samarium row | supports | Live official notice explicitly names this mineral commodity. Jurisdiction, USGS list name and 2025 edition match. The element mapping is stated without broadening criticality to salts, minerals or wastes. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=272123; Exact current name, rank and synonyms/co-identical strain entries | supports | Live NCBI no-rank node 272123 uses Anabaena cylindrica PCC 7122 and explicitly lists SAG 1403-2 as co-identical; the record does not claim a different PCC culture was assayed. |
| culture | https://sagdb.uni-goettingen.de/detailedList.php?str_number=1403-2; Current strain identity and axenic/strain-relative fields | supports | Live SAG entry lists A. cylindrica 1403-2 as axenic and gives PCC 7122 among strain relatives. Record distinguishes current catalogue state from a contemporaneous purity test. |
| primary | https://doi.org/10.1039/C9RA06570A; Full JATS main.xml; Experimental culture/ICP-MS/LIBS/TEM/XRD; Results, Discussion and Conclusions; live PMC full text | supports | Full primary methods and results independently read. Separate element/strain assays, starting doses, modified BBM culture conditions, untreated references, stock-reference baseline, centrifugation/filtering, qualitative LIBS and sampling uncertainty match the record. No matched incubated abiotic control, biological replication count or biomass denominator is established. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9073238/supplementaryFiles; Complete recovered five-page RA-009-C9RA06570A-s001.pdf: Table/Figure S3, page S4 | supports | Reviewer visually inspected page S4, confirmed exact source cells and recomputed first decrease: 1.52E-3/0.139 leaves approximately 1.09%, so the main less-than-1% wording is inconsistent. Record retains exact values, nonzero later concentrations and unresolved error-column meaning. |
| integrity | /private/tmp/cmm-round7-eu-sm-independent/verify_raw.py; Independent parsing of supplement ZIP local header, raw DEFLATE stream and following data descriptor | supports | Complete 470633-byte PDF independently reproduced from incomplete archive; DEFLATE EOF, compressed length 366116, uncompressed length 470633 and CRC32 873cb15c all matched, as did recovered bytes and SHA256. This validates the individual member, not the enclosing ZIP. |
| search | Review-session web queries and hidden/ignored local source search; Correction, retraction, conflicting evidence and duplicate coverage | context_only | Bounded searches found no matching correction or retraction notice. Later Eu image analysis and later Sm particle claims were considered without upgrading unsupported chemistry. No additional duplicate root was found within the searched corpus; no global literature-exhaustion claim is made. |
| localization | https://doi.org/10.1039/C9RA06570A; Results LIBS/Figure 4 caption and Discussion Sm particle paragraph | partial | Source attributes Sm emission peaks to washed biomass after 200 h versus nitrate and untreated controls; LIBS is explicitly qualitative. Figure 4 pixels were unavailable, so no independent spectral remeasurement is claimed. Discussion did not demonstrate Sm particles in this 2019 series; record keeps that narrow scope. |
| later | https://doi.org/10.1016/j.impact.2022.100398; Publisher indexed abstract/highlights and source metadata only | context_only | Later paper reports A. cylindrica Sm particles, but full methods and speciation evidence were not acquired in this review. This is a deferred follow-up, not grounds for claiming Sm(0), overturning the narrower 2019 observation, or declaring particles impossible. |

## Limits And Additional Notes

- No independent biological replication, original instrument data or complete elemental mass balance was available. Lack of an incubated abiotic control, biomass denominator and killed-cell comparison limits causal attribution.
- The 2019 primary main PDF and selected .jpg requests returned challenge HTML. Reviewer did not treat them as PDFs/images. The complete XML and valid recovered supplement were inspected; additional EuropePMC direct-image routes returned403. Figure 4 LIBS remains an attributed primary result rather than independently remeasured image; relevant supplementary Sm plot/table was visually checked.
- Recovered supplementary PDF is individually CRC/size/DEFLATE verified, but the parent ZIP is incomplete. Unrecovered members were not silently assumed available.
- Later 2022 Sm particle source remained abstract/metadata-level; full experimental and phase evidence must be acquired before adding a new mechanism.
- Bounded correction and counterevidence searches do not establish comprehensive literature clearance.
- Passing verdict concerns faithful, appropriately qualified representation of the inspected evidence, not experimental reproducibility or industrial feasibility.
- Source state is working_tree at trusted main revision 58e7aef16a9643438cf621fa9fb402e9d325dc65, with exact current target hashes. No curator fix was requested and no review issue was manufactured.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T060643Z-samarium-round7-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the round 7 samarium record
started_at: '2026-10-11T06:03:43Z'
finished_at: '2026-10-11T06:06:43Z'
reviewer:
  identity: Codex /root/cmm7_ho_er_gd
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/cmm7_europium_samarium. Prepared
    source research before freeze, captured exact targets/schema/history before formal
    target assessment, independently read original full text and supplement, checked
    authority IDs and calculations, and made no reviewed record edits. Completed dossier
    context captured after finalization.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Samarium identity, dated US2025 criticality and carefully bounded culture-associated
  sorption are supported. Exact supplementary measurements take precedence over inconsistent
  narrative summaries. No actionable curation findings in the frozen record; source/control/visual-access
  limits remain explicit.
source:
  git_revision: 58e7aef16a9643438cf621fa9fb402e9d325dc65
  state: working_tree
  inputs:
  - path: data/records/samarium.yaml
    sha256: 580b317ea1c31ef21c185f2e0c2b935a36de609adbba0a721ed2b756bba40a60
    role: target
  - path: history/records/samarium/2026-10-11T060235Z-codex-f02c8c.yaml
    sha256: 70f9f5b85772a248309b309536a74b4f21f96972f3c9b3a1d62babab1934af27
    role: context
  - path: research/ingests/round7-eu-sm-20261011.json
    sha256: d4b4221a5dd85859b48fd3187fb6b03a538ea189c1ba1541c756a8c0dc28b0eb
    role: context
  - path: research/ingests/round7-eu-sm-20261011.md
    sha256: 4d63a52607ecc2abdad02333c82e5d7b7096473ebb6de029895417b0c389d398
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific fields, source references, inline and canonical CREATE
    provenance of one maintained element record.
  selection: Assigned named record; full target assessment, with stated primary-image
    and follow-up access limitations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:samarium
targets:
- target_id: cmmmech:samarium
  path: data/records/samarium.yaml
  label: Samarium
  kind: maintained
  record_class: CriticalMineralRecord
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/samarium.yaml
    role: maintained_record
checks:
- check_id: records
  name: Affected record validation
  status: passed
  required: true
  summary: 'Reviewer executed: 2 records checked, zero failures; terminal exit 0.'
  target_ids:
  - cmmmech:samarium
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/europium.yaml data/records/samarium.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Append-only history gate
  status: passed
  required: true
  summary: 'Reviewer executed: 52 history sessions checked, zero errors; terminal
    exit 0.'
  target_ids:
  - cmmmech:samarium
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 58e7aef16a9643438cf621fa9fb402e9d325dc65
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty full corpus gate
  status: passed
  required: true
  summary: 'Reviewer executed: 42 records checked, zero failures; terminal exit 0.'
  target_ids:
  - cmmmech:samarium
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Complete batch check
  status: passed
  required: true
  summary: 'Parent executed and reported terminal exit 0; reviewer read /private/tmp/cmm-round7-check.log:
    lint passed, 307 tests passed, 3 skipped in 51.17s, 42 records and 52 histories
    valid. Frozen reviewed target bytes were unchanged.'
  target_ids:
  - cmmmech:samarium
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/samarium.yaml
  locator: All scientific fields, source links, inline event and linked canonical
    CREATE session
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Exact frozen bytes inspected after initial inspect; recapture added completed
    dossier context without changing target hashes.
  snapshot_sha256: 580b317ea1c31ef21c185f2e0c2b935a36de609adbba0a721ed2b756bba40a60
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33374
  locator: Preferred ID and name, formula and net charge
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: 33374 resolves to samarium atom, formula Sm, charge 0. Web open failed;
    independent direct HTML retrieval succeeded and the exact fields were read.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final US2025 list, Federal Register 90:50494-50497; page 50497 samarium
    row
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Live official notice explicitly names this mineral commodity. Jurisdiction,
    USGS list name and 2025 edition match. The element mapping is stated without broadening
    criticality to salts, minerals or wastes.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=272123
  locator: Exact current name, rank and synonyms/co-identical strain entries
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Live NCBI no-rank node 272123 uses Anabaena cylindrica PCC 7122 and explicitly
    lists SAG 1403-2 as co-identical; the record does not claim a different PCC culture
    was assayed.
- evidence_id: culture
  kind: database
  reference: https://sagdb.uni-goettingen.de/detailedList.php?str_number=1403-2
  locator: Current strain identity and axenic/strain-relative fields
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Live SAG entry lists A. cylindrica 1403-2 as axenic and gives PCC 7122
    among strain relatives. Record distinguishes current catalogue state from a contemporaneous
    purity test.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA06570A
  locator: Full JATS main.xml; Experimental culture/ICP-MS/LIBS/TEM/XRD; Results,
    Discussion and Conclusions; live PMC full text
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Full primary methods and results independently read. Separate element/strain
    assays, starting doses, modified BBM culture conditions, untreated references,
    stock-reference baseline, centrifugation/filtering, qualitative LIBS and sampling
    uncertainty match the record. No matched incubated abiotic control, biological
    replication count or biomass denominator is established.
  snapshot_sha256: 6ad2ff7a2c931279c8cdb42a184088b6279f43e495e3d27d9b12cc7995078a25
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9073238/supplementaryFiles
  locator: 'Complete recovered five-page RA-009-C9RA06570A-s001.pdf: Table/Figure
    S3, page S4'
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: 'Reviewer visually inspected page S4, confirmed exact source cells and
    recomputed first decrease: 1.52E-3/0.139 leaves approximately 1.09%, so the main
    less-than-1% wording is inconsistent. Record retains exact values, nonzero later
    concentrations and unresolved error-column meaning.'
  snapshot_sha256: b8c15455505ac49222ae60eb5297d3ac4564833d29d22ccceb7b0918491e459b
- evidence_id: integrity
  kind: validation
  reference: /private/tmp/cmm-round7-eu-sm-independent/verify_raw.py
  locator: Independent parsing of supplement ZIP local header, raw DEFLATE stream
    and following data descriptor
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Complete 470633-byte PDF independently reproduced from incomplete archive;
    DEFLATE EOF, compressed length 366116, uncompressed length 470633 and CRC32 873cb15c
    all matched, as did recovered bytes and SHA256. This validates the individual
    member, not the enclosing ZIP.
- evidence_id: search
  kind: search
  reference: Review-session web queries and hidden/ignored local source search
  locator: Correction, retraction, conflicting evidence and duplicate coverage
  accessed_at: '2026-10-11T06:06:43Z'
  support: context_only
  summary: Bounded searches found no matching correction or retraction notice. Later
    Eu image analysis and later Sm particle claims were considered without upgrading
    unsupported chemistry. No additional duplicate root was found within the searched
    corpus; no global literature-exhaustion claim is made.
  search_scope: '2026-10-11 web first returned result sets, no filters/pagination:
    "10.1039/C9RA06570A" correction retraction; "Cyanobacterial promoted enrichment"
    europium samarium contradiction heterocysts vegetative; "10.3390/nano13010130"
    correction retraction; "High-resolution particle size" "Samarium" nanoparticles
    2022; "Anabaena" "samarium" abiotic precipitation control. rg --no-ignore --hidden
    -L searched data/records, research, history, reviews and the cited /private/tmp/cmm-round7-eu-sm
    directory by names/DOI/PMCID; unrelated home/temp trees excluded.'
- evidence_id: localization
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA06570A
  locator: Results LIBS/Figure 4 caption and Discussion Sm particle paragraph
  accessed_at: '2026-10-11T06:06:43Z'
  support: partial
  summary: Source attributes Sm emission peaks to washed biomass after 200 h versus
    nitrate and untreated controls; LIBS is explicitly qualitative. Figure 4 pixels
    were unavailable, so no independent spectral remeasurement is claimed. Discussion
    did not demonstrate Sm particles in this 2019 series; record keeps that narrow
    scope.
- evidence_id: later
  kind: primary_source
  reference: https://doi.org/10.1016/j.impact.2022.100398
  locator: Publisher indexed abstract/highlights and source metadata only
  accessed_at: '2026-10-11T06:06:43Z'
  support: context_only
  summary: Later paper reports A. cylindrica Sm particles, but full methods and speciation
    evidence were not acquired in this review. This is a deferred follow-up, not grounds
    for claiming Sm(0), overturning the narrower 2019 observation, or declaring particles
    impossible.
assessments:
- assessment_id: identity
  area: identity
  topic: Element and experimental strain identity
  outcome: supported
  summary: The neutral element, experimental nitrate/ion context, catalogue strain
    and taxonomy mapping are accurately separated.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - identity
  - taxon
  - culture
- assessment_id: criticality
  area: grounding
  topic: Jurisdiction, list, edition and commodity scope
  outcome: supported
  summary: The individual 2025 US row supports the stated dated designation without
    extending it to every host mineral or compound.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Qualified culture-associated biosorption
  outcome: supported
  summary: The source supports reduced supernatant element and qualitative biomass
    enrichment. The record does not convert this association into isolated product
    recovery or an exclusively metabolic mechanism.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - primary
  - supplement
  - localization
  dimensions:
  - name: organism
    value: Anabaena cylindrica SAG 1403-2; co-identical NCBI PCC 7122 node 272123
    definition: Assayed culture identity and purity limitations.
    evidence_ids:
    - primary
    - taxon
    - culture
  - name: biomass_state
    value: Living culture exposed; harvested washed biomass dried for qualitative
      LIBS
    definition: Culture viability is judged visually, not quantitative viable counts
      or a killed-cell comparison.
    evidence_ids:
    - primary
  - name: substrate
    value: 0.139 mM Sm in modified nutrient medium, supplied as nitrate hexahydrate
    definition: Separate synthetic-element arms; no mixed-REE selectivity assay.
    evidence_ids:
    - primary
    - supplement
  - name: conditions
    value: 22 degrees C, modified BBM with half nitrate, initial medium pH 6.8 / culture
      pH 7.3, 150 mL growth medium in 250 mL flasks, shaking and 12 h day/night
    definition: Growth conditions are not converted into an unreported biomass-normalized
      capacity.
    evidence_ids:
    - primary
  - name: controls
    value: Untreated culture and diluted initial stock; no matched incubated biomass-free
      time course
    definition: Initial stock reference does not exclude precipitation, filter loss
      or associated organisms.
    evidence_ids:
    - primary
    - record
  - name: measurement
    value: Supernatant ICP-MS concentration and qualitative LIBS; ±10 min sampling
      uncertainty
    definition: Total element and biomass presence do not establish oxidation state,
      intracellular fraction or mass balance.
    evidence_ids:
    - primary
    - supplement
  - name: deployment
    value: Laboratory synthetic solution; no product isolation, real-waste validation
      or industrial deployment
    definition: Boundary of accepted practical recovery claim.
    evidence_ids:
    - primary
    - record
- assessment_id: quantities
  area: quantity
  topic: Exact supplementary cells versus conflicting summaries
  outcome: supported
  summary: Cell values, units, dose/medium arms and timing were checked directly.
    Derived percentages are labeled as calculations; RSD statistics remain unresolved;
    mmol/L data are not coerced into the mg/kg observation contract.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - supplement
  - integrity
- assessment_id: uncertainty
  area: consistency
  topic: Source contradictions and later evidence
  outcome: supported
  summary: The record preserves source disagreements and limits the later literature
    to what the inspected methods establish. It does not turn lack of proof in one
    series into a universal impossibility claim.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - primary
  - localization
  - later
  - search
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE events and immutable base
  outcome: supported
  summary: Inline curation and canonical history are distinct actual UTC events. Actor
    codex/GPT-6/codex, target and issue 34 agree; no reviewed record/history edits
    were made by reviewer.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded scientific review
  outcome: supported
  summary: All record fields assessed; source access and image limitations retained
    explicitly. Current hashes match the inspected state and offline gates are green.
  target_ids:
  - cmmmech:samarium
  evidence_ids:
  - record
  - search
  - integrity
findings: []
actions: []
limitations:
- No independent biological replication, original instrument data or complete elemental
  mass balance was available. Lack of an incubated abiotic control, biomass denominator
  and killed-cell comparison limits causal attribution.
- The 2019 primary main PDF and selected .jpg requests returned challenge HTML. Reviewer
  did not treat them as PDFs/images. The complete XML and valid recovered supplement
  were inspected; additional EuropePMC direct-image routes returned403. Figure 4 LIBS
  remains an attributed primary result rather than independently remeasured image;
  relevant supplementary Sm plot/table was visually checked.
- Recovered supplementary PDF is individually CRC/size/DEFLATE verified, but the parent
  ZIP is incomplete. Unrecovered members were not silently assumed available.
- Later 2022 Sm particle source remained abstract/metadata-level; full experimental
  and phase evidence must be acquired before adding a new mechanism.
- Bounded correction and counterevidence searches do not establish comprehensive literature
  clearance.
notes:
- Passing verdict concerns faithful, appropriately qualified representation of the
  inspected evidence, not experimental reproducibility or industrial feasibility.
- Source state is working_tree at trusted main revision 58e7aef16a9643438cf621fa9fb402e9d325dc65,
  with exact current target hashes. No curator fix was requested and no review issue
  was manufactured.
links:
- research/ingests/round7-eu-sm-20261011.md
- research/ingests/round7-eu-sm-20261011.json
tags:
- round7
- independent-review
- samarium
- primary-literature
- bounded-evidence
```
