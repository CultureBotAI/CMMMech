# Independent scientific review of the round 7 europium record

- Review: 20261011T060643Z-europium-round7-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:03:43Z
- Finished UTC: 2026-10-11T06:06:43Z
- Reviewer: Codex /root/cmm7_ho_er_gd (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Europium identity, dated US2025 criticality and carefully bounded culture-associated sorption are supported. Exact supplementary measurements take precedence over inconsistent narrative summaries. No actionable curation findings in the frozen record; source/control/visual-access limits remain explicit.

## Scope And Provenance

All scientific fields, source references, inline and canonical CREATE provenance of one maintained element record.

Selection: Assigned named record; full target assessment, with stated primary-image and follow-up access limitations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58e7aef16a9643438cf621fa9fb402e9d325dc65.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:europium | data/records/europium.yaml | maintained | Europium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Affected record validation | passed | True | cmmmech:europium | Reviewer executed: 2 records checked, zero failures; terminal exit 0. |
| Append-only history gate | passed | True | cmmmech:europium | Reviewer executed: 52 history sessions checked, zero errors; terminal exit 0. |
| Nonempty full corpus gate | passed | True | cmmmech:europium | Reviewer executed: 42 records checked, zero failures; terminal exit 0. |
| Complete batch check | passed | True | cmmmech:europium | Parent executed and reported terminal exit 0; reviewer read /private/tmp/cmm-round7-check.log: lint passed, 307 tests passed, 3 skipped in 51.17s, 42 records and 52 histories valid. Frozen reviewed target bytes were unchanged. |

## Scientific And Domain Assessments

### Element and experimental strain identity

identity: supported. Targets: cmmmech:europium.

The neutral element, experimental nitrate/ion context, catalogue strain and taxonomy mapping are accurately separated.

### Jurisdiction, list, edition and commodity scope

grounding: supported. Targets: cmmmech:europium.

The individual 2025 US row supports the stated dated designation without extending it to every host mineral or compound.

### Qualified culture-associated biosorption

evidence: supported. Targets: cmmmech:europium.

The source supports reduced supernatant element and qualitative biomass enrichment. The record does not convert this association into isolated product recovery or an exclusively metabolic mechanism.

### Exact supplementary cells versus conflicting summaries

quantity: supported. Targets: cmmmech:europium.

Cell values, units, dose/medium arms and timing were checked directly. Derived percentages are labeled as calculations; RSD statistics remain unresolved; mmol/L data are not coerced into the mg/kg observation contract.

### Source contradictions and later evidence

consistency: supported. Targets: cmmmech:europium.

The record preserves source disagreements and limits the later literature to what the inspected methods establish. It does not turn lack of proof in one series into a universal impossibility claim.

### Actual CREATE events and immutable base

provenance: supported. Targets: cmmmech:europium.

Inline curation and canonical history are distinct actual UTC events. Actor codex/GPT-6/codex, target and issue 34 agree; no reviewed record/history edits were made by reviewer.

### Bounded scientific review

completeness: supported. Targets: cmmmech:europium.

All record fields assessed; source access and image limitations retained explicitly. Current hashes match the inspected state and offline gates are green.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/europium.yaml; All scientific fields, source links, inline event and linked canonical CREATE session | supports | Exact frozen bytes inspected after initial inspect; recapture added completed dossier context without changing target hashes. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:32999; Preferred ID and name, formula and net charge | supports | 32999 resolves to europium atom, formula Eu, charge 0. Live web entry inspected. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final US2025 list, Federal Register 90:50494-50497; page 50496 europium row | supports | Live official notice explicitly names this mineral commodity. Jurisdiction, USGS list name and 2025 edition match. The element mapping is stated without broadening criticality to salts, minerals or wastes. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1840102; Exact current name, rank and synonyms/co-identical strain entries | supports | Independent NCBI XML retrieval confirms taxon 1840102, Anabaena sp. SAG 12.82, species rank despite its strain-like name. No new species inference is made. |
| culture | https://sagdb.uni-goettingen.de/detailedList.php?str_number=12.82; Current strain identity and axenic/strain-relative fields | supports | Live SAG entry lists Anabaena spec. 12.82 as non-axenic, with bacterial and other contamination. Record correctly limits this to current catalogue context, not proven 2019 community composition. |
| primary | https://doi.org/10.1039/C9RA06570A; Full JATS main.xml; Experimental culture/ICP-MS/LIBS/TEM/XRD; Results, Discussion and Conclusions; live PMC full text | supports | Full primary methods and results independently read. Separate element/strain assays, starting doses, modified BBM culture conditions, untreated references, stock-reference baseline, centrifugation/filtering, qualitative LIBS and sampling uncertainty match the record. No matched incubated abiotic control, biological replication count or biomass denominator is established. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9073238/supplementaryFiles; Complete recovered five-page RA-009-C9RA06570A-s001.pdf: Tables/Figures S1 and S4, pages S2 and S5 | supports | Reviewer visually inspected rendered pages S2/S5 and independently checked exact tabulated concentrations, minute values, error-column labeling and percentage arithmetic. Main narrative overstates one-hour and three-hour removal; record correctly preserves the conflicting table results and later increases. |
| integrity | /private/tmp/cmm-round7-eu-sm-independent/verify_raw.py; Independent parsing of supplement ZIP local header, raw DEFLATE stream and following data descriptor | supports | Complete 470633-byte PDF independently reproduced from incomplete archive; DEFLATE EOF, compressed length 366116, uncompressed length 470633 and CRC32 873cb15c all matched, as did recovered bytes and SHA256. This validates the individual member, not the enclosing ZIP. |
| search | Review-session web queries and hidden/ignored local source search; Correction, retraction, conflicting evidence and duplicate coverage | context_only | Bounded searches found no matching correction or retraction notice. Later Eu image analysis and later Sm particle claims were considered without upgrading unsupported chemistry. No additional duplicate root was found within the searched corpus; no global literature-exhaustion claim is made. |
| localization | https://doi.org/10.1039/C9RA06570A; Abstract versus TEM Results/Figure 8 caption and Conclusion; XRD Results | partial | Body/caption consistently attribute deposits to heterocysts at 10/28 h, unlike abstract vegetative-cell wording. Original Figure 8 pixels were unavailable; assessment verifies the explicitly attributed report, not cell-level reanalysis or particle composition. Original Figure 3 LIBS spectrum was visually inspected and confirms the starved-arm qualitative comparison. Missing oxidation-state measurement and negative bulk XRD cannot establish Eu(0). |
| later | https://doi.org/10.3390/nano13010130; PMC9824745 complete main XML, Sections 2-4 and Abstract; inspected independently | partial | Later article describes microscopy and image processing of Eu-exposed SAG 12.82 heterocysts, calls Eu particles amorphous and uses bioreduction language in the abstract. No new Eu oxidation-state assay is described in its main methods. Detailed particle-size results and unacquired full supplements are outside the accepted claim. |

## Limits And Additional Notes

- No independent biological replication, original instrument data or complete elemental mass balance was available. Lack of an incubated abiotic control, biomass denominator and killed-cell comparison limits causal attribution.
- The 2019 primary main PDF and selected .jpg requests returned challenge HTML. Reviewer did not treat them as PDFs/images. The complete XML and valid recovered supplement were inspected; additional EuropePMC direct-image routes returned403. Figure 8 localization remains an attributed Results/caption observation, not independent microscopy remeasurement. Figure 3 and relevant supplement pages were visually checked.
- Recovered supplementary PDF is individually CRC/size/DEFLATE verified, but the parent ZIP is incomplete. Unrecovered members were not silently assumed available.
- Later Eu main text was assessed only for assay/speciation scope; full later supplements and raw micrographs were not acquired.
- Bounded correction and counterevidence searches do not establish comprehensive literature clearance.
- Passing verdict concerns faithful, appropriately qualified representation of the inspected evidence, not experimental reproducibility or industrial feasibility.
- Source state is working_tree at trusted main revision 58e7aef16a9643438cf621fa9fb402e9d325dc65, with exact current target hashes. No curator fix was requested and no review issue was manufactured.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T060643Z-europium-round7-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the round 7 europium record
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
summary: Europium identity, dated US2025 criticality and carefully bounded culture-associated
  sorption are supported. Exact supplementary measurements take precedence over inconsistent
  narrative summaries. No actionable curation findings in the frozen record; source/control/visual-access
  limits remain explicit.
source:
  git_revision: 58e7aef16a9643438cf621fa9fb402e9d325dc65
  state: working_tree
  inputs:
  - path: data/records/europium.yaml
    sha256: 2a0e8347906dd98a6fb00147db7f24976cb4ed86df21b65f9e3f2b2dc855d869
    role: target
  - path: history/records/europium/2026-10-11T060214Z-codex-7e06cb.yaml
    sha256: 178e316cbf292670c844cfd1f41b88ca205467d661fca45ad134ef65739f01da
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
  - cmmmech:europium
targets:
- target_id: cmmmech:europium
  path: data/records/europium.yaml
  label: Europium
  kind: maintained
  record_class: CriticalMineralRecord
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/europium.yaml
    role: maintained_record
checks:
- check_id: records
  name: Affected record validation
  status: passed
  required: true
  summary: 'Reviewer executed: 2 records checked, zero failures; terminal exit 0.'
  target_ids:
  - cmmmech:europium
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
  - cmmmech:europium
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
  - cmmmech:europium
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
  - cmmmech:europium
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/europium.yaml
  locator: All scientific fields, source links, inline event and linked canonical
    CREATE session
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Exact frozen bytes inspected after initial inspect; recapture added completed
    dossier context without changing target hashes.
  snapshot_sha256: 2a0e8347906dd98a6fb00147db7f24976cb4ed86df21b65f9e3f2b2dc855d869
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32999
  locator: Preferred ID and name, formula and net charge
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: 32999 resolves to europium atom, formula Eu, charge 0. Live web entry inspected.
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final US2025 list, Federal Register 90:50494-50497; page 50496 europium
    row
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Live official notice explicitly names this mineral commodity. Jurisdiction,
    USGS list name and 2025 edition match. The element mapping is stated without broadening
    criticality to salts, minerals or wastes.
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1840102
  locator: Exact current name, rank and synonyms/co-identical strain entries
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Independent NCBI XML retrieval confirms taxon 1840102, Anabaena sp. SAG
    12.82, species rank despite its strain-like name. No new species inference is
    made.
- evidence_id: culture
  kind: database
  reference: https://sagdb.uni-goettingen.de/detailedList.php?str_number=12.82
  locator: Current strain identity and axenic/strain-relative fields
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Live SAG entry lists Anabaena spec. 12.82 as non-axenic, with bacterial
    and other contamination. Record correctly limits this to current catalogue context,
    not proven 2019 community composition.
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
  locator: 'Complete recovered five-page RA-009-C9RA06570A-s001.pdf: Tables/Figures
    S1 and S4, pages S2 and S5'
  accessed_at: '2026-10-11T06:06:43Z'
  support: supports
  summary: Reviewer visually inspected rendered pages S2/S5 and independently checked
    exact tabulated concentrations, minute values, error-column labeling and percentage
    arithmetic. Main narrative overstates one-hour and three-hour removal; record
    correctly preserves the conflicting table results and later increases.
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
  locator: Abstract versus TEM Results/Figure 8 caption and Conclusion; XRD Results
  accessed_at: '2026-10-11T06:06:43Z'
  support: partial
  summary: Body/caption consistently attribute deposits to heterocysts at 10/28 h,
    unlike abstract vegetative-cell wording. Original Figure 8 pixels were unavailable;
    assessment verifies the explicitly attributed report, not cell-level reanalysis
    or particle composition. Original Figure 3 LIBS spectrum was visually inspected
    and confirms the starved-arm qualitative comparison. Missing oxidation-state measurement
    and negative bulk XRD cannot establish Eu(0).
- evidence_id: later
  kind: primary_source
  reference: https://doi.org/10.3390/nano13010130
  locator: PMC9824745 complete main XML, Sections 2-4 and Abstract; inspected independently
  accessed_at: '2026-10-11T06:06:43Z'
  support: partial
  summary: Later article describes microscopy and image processing of Eu-exposed SAG
    12.82 heterocysts, calls Eu particles amorphous and uses bioreduction language
    in the abstract. No new Eu oxidation-state assay is described in its main methods.
    Detailed particle-size results and unacquired full supplements are outside the
    accepted claim.
  snapshot_sha256: d2456e576f50df0b25f55418c3be9d38d46dd3c0b0ddbcb668dfefdae3854b0a
assessments:
- assessment_id: identity
  area: identity
  topic: Element and experimental strain identity
  outcome: supported
  summary: The neutral element, experimental nitrate/ion context, catalogue strain
    and taxonomy mapping are accurately separated.
  target_ids:
  - cmmmech:europium
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
  - cmmmech:europium
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
  - cmmmech:europium
  evidence_ids:
  - record
  - primary
  - supplement
  - localization
  dimensions:
  - name: organism
    value: Anabaena sp. SAG 12.82, strain-named species node 1840102; current catalogue
      non-axenic
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
    value: 0.111 mM Eu fed and 0.191 mM Eu starved, supplied as nitrate hexahydrate
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
  - cmmmech:europium
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
  - cmmmech:europium
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
  - cmmmech:europium
  evidence_ids:
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded scientific review
  outcome: supported
  summary: All record fields assessed; source access and image limitations retained
    explicitly. Current hashes match the inspected state and offline gates are green.
  target_ids:
  - cmmmech:europium
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
  were inspected; additional EuropePMC direct-image routes returned403. Figure 8 localization
  remains an attributed Results/caption observation, not independent microscopy remeasurement.
  Figure 3 and relevant supplement pages were visually checked.
- Recovered supplementary PDF is individually CRC/size/DEFLATE verified, but the parent
  ZIP is incomplete. Unrecovered members were not silently assumed available.
- Later Eu main text was assessed only for assay/speciation scope; full later supplements
  and raw micrographs were not acquired.
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
- europium
- primary-literature
- bounded-evidence
```
