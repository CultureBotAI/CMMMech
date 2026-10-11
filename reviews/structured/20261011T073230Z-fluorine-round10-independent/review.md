# Independent scientific review of Fluorine

- Review: 20261011T073230Z-fluorine-round10-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:27:04Z
- Finished UTC: 2026-10-11T07:32:30Z
- Reviewer: codex /root/cmm10_ti_zr (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact fluorine record is defensible as enantioselective hydrolytic defluorination in an engineered laboratory culture. It preserves the racemic denominator, fluoride stress, species/strain separation and control limits, without claiming fluorine reduction, universal PFAS removal, intracellular concentrations or isolated recovery. No actionable curation finding was established.

## Scope And Provenance

All maintained record fields and linked provenance checked against primary evidence and authorities; no sampling of record fields. Search and literature-access coverage is explicitly bounded.

Selection: Assigned named record; full field assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:fluorine | data/records/fluorine.yaml | maintained | Fluorine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:fluorine | Reviewer executed directly; 2 records, 0 failed; terminal exit 0. Earlier same successful output retained in /private/tmp/cmm-round10-b-f-independent/named-validation.log. |
| Full batch gate | passed | True | cmmmech:fluorine | Parent executed session 84281; reviewer read /private/tmp/cmm-round10-batch-check.log: 307 passed, 3 skipped in 64.75 s; 61 records and 72 histories valid. Parent separately confirmed terminal exit 0. |
| Nonempty corpus | passed | True | cmmmech:fluorine | Parent executed session 20894; reviewer read /private/tmp/cmm-round10-batch-validation.log: 61 records, 0 failed. Parent separately confirmed terminal exit 0. |
| Trusted-base history | passed | True | cmmmech:fluorine | Parent executed session 33751; reviewer read /private/tmp/cmm-round10-batch-history.log: 72 histories, 0 errors. Parent separately confirmed terminal exit 0. |

## Scientific And Domain Assessments

### Element, substrate and organism identity

identity: supported. Targets: cmmmech:fluorine.

Atomic identity and taxonomic scope are supported; chemical feed and resulting forms are not conflated with the element.

### Dated jurisdiction and list designation

evidence: supported. Targets: cmmmech:fluorine.

The named authority, jurisdiction, list and edition support the record mapping with the stated qualifiers.

### Organism-specific conditions, controls and measured outcome

evidence: supported. Targets: cmmmech:fluorine.

The exact fluorine record is defensible as enantioselective hydrolytic defluorination in an engineered laboratory culture. It preserves the racemic denominator, fluoride stress, species/strain separation and control limits, without claiming fluorine reduction, universal PFAS removal, intracellular concentrations or isolated recovery. No actionable curation finding was established.

### Actual CREATE provenance

provenance: supported. Targets: cmmmech:fluorine.

Distinct inline and sidecar events state actual actor/model/tool and target. Trusted-base history validation passed; no record edits or fabricated prior authorship by reviewer.

### Bounded duplicate and contrary-evidence coverage

completeness: supported. Targets: cmmmech:fluorine.

Scoped hidden/ignored inventory and primary internal counterevidence were checked. Searches provide bounded coverage, not proof of literature completeness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/fluorine.yaml; All fields, linked CREATE sidecar and both shared dossier files | supports | Reviewed exact pre-assessment working bytes and rechecked all hashes before saving. Inline CREATE event and earlier distinct actual CREATE sidecar identify the target, Codex actor, GPT-6 model and codex tool; no invented predecessor authorship. No record, history or dossier edits by this reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:24061; Released ChEBI entry name, chemical_data formula/charge and structure | supports | Fluorine atom identity is element F, neutral charge 0. Independently inspected and hashed the curator-acquired authoritative JSON. Two live ChEBI page requests returned internal errors; retained official API JSON supplied the independent inspection. |
| organism | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=303&amp;mode=Info; Taxonomy ID 303, current name and rank | supports | Independent live and retained authority inspection confirms Pseudomonas putida at species rank, separate from ATCC 12633 and its engineered expression construct. |
| strain | https://www.atcc.org/products/12633; Culture product identity | supports | Independent live ATCC page and retained catalog establish P. putida 12633. The primary introduction isolated 12663 spelling is inconsistent with Methods/Results and is explicitly qualified. |
| criticality | https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list; 20 February 2024 update; Table 1 Fluorine row, footnote 13 | supports | Live government page independently read: Australia explicitly lists Fluorine in Table 1 and dates the update to 20 February 2024. Footnote 13 says US/EU identify fluorspar; the record does not transfer those commodity designations to elemental fluorine. Direct downloaded authority bytes were unavailable to the curator; this successful provider-web reading has no fabricated raw-file hash. |
| primary | https://doi.org/10.1128/mbio.02785-23; Full main XML: Results, Table 1, Table 2 and Materials and Methods | supports | Main study reports engineered P. putida 12633 expressing Delftia strain B defluorinase, growth and fluoride release from the two specified racemic mono-fluorinated acids. Table 2 gives 9.9±0.1 and 9.9±0.2 mM released fluoride from 20 mM racemates at maximum OD times 29/78 h, n=3 biological replicates plus reported independent repetition. Purified enzyme no-enzyme controls are distinct from wild-type culture nongrowth. Unassigned 28/30-degree flask temperature remains explicit. |
| figures | https://doi.org/10.1128/mbio.02785-23; Main Figures 2 and 3 original JPEG pixels; Table 2 XML cells | supports | Figure 2 supports growth-associated fluoride release near half the total racemate fluorine, and Figure 2F includes initial CFU decline. Figure 3 separates residual culture-substrate polarimetry from purified-enzyme D-lactate identification; active-site geometry is modeled. No fluoride intracellular concentration or isolated product yield follows from these panels. |
| supplement | https://doi.org/10.1128/mbio.02785-23; Valid mbio.02785-23-s0001.docx: Figures S1–S7 text; S1–S5 embedded image pixels; Tables S1/S2 context | supports | Independently inspected the valid DOCX and images, not the misleading .docx-named challenge HTML. Purification and control context support the enzyme experiments. S4 shows lower net fluoride-release trajectory with 5 mM NaF despite main-text minimal-inhibition wording; the record makes no no-inhibition claim. S3 conditions differ in wording from the main morphology discussion and are not imported quantitatively. S5 compares CrcB sequences and locus organization, not a knockout in the curated recombinant strain. Main reference to S9 instead of actual S7 is a source cross-reference inconsistency, not invented evidence. |
| search | Independent review-session searches and local hidden/ignored inventory; Exact DOI, title, contrary-evidence and identifier searches | context_only | Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23" correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation; "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract". Inspected first returned result sets only. Related reviews, primary citation matches and unrelated DOI/title collisions returned; no matched correction or retraction of the two accepted primary papers was identified. A retracted 2023 boron review is distinct and was not accepted as evidence. This is not an exhaustive registry or citation-network audit. rg --no-ignore --hidden searched data, research, reviews and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching files were inspected/scoped. find of those roots returned no symlinks. Hidden and ignored files were included; this is not a home-directory-wide absence claim. |

## Limits And Additional Notes

- The flask temperature is ambiguous between the two general values; intracellular fluoride was inferred from cytoplasmic enzyme location, not measured.
- Wild-type nongrowth is not a quantitative abiotic culture-release blank, and CrcB causal necessity was not tested by knockout in this strain.
- Supplement S4 limits the main text minimal-inhibition wording; S3 morphology dose wording and S7/S9 reference numbering are source inconsistencies not used as new quantitative record claims.
- The accepted evidence covers selected monofluorinated model substrates and laboratory engineering, not all PFAS, mineral feeds, mixed wastes or recovered fluoride products.
- Australia authority was successfully read live through the web provider without a raw-file byte hash; fluorine ChEBI live web opens failed and retained official API bytes were independently verified instead.
- Correction/retraction and contrary-evidence searches cover first returned result sets and cited local sources, not exhaustive registries or all possible conflicting studies.
- Reviewed final working-tree bytes on trusted base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2; this is not a committed-source attestation.
- Findings by severity: no confirmed blocker, major, minor or informational curation defect. Corrections in this round: none. Unresolved scientific questions are retained under limitations; they do not invalidate the qualified observation.
- Raw source snapshots remain outside Git at /private/tmp/cmm-round10-b-f-raw. Reviewer inspections, local search receipt and named validation are under /private/tmp/cmm-round10-b-f-independent.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T073230Z-fluorine-round10-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Fluorine
started_at: '2026-10-11T07:27:04Z'
finished_at: '2026-10-11T07:32:30Z'
reviewer:
  identity: codex /root/cmm10_ti_zr
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from the B/F curator. Reviewer did not author
    or modify these records, histories or dossiers; independently read primary methods/results,
    figure/table pixels, valid supplement where present, authorities and exact frozen
    source bytes. Parent batch commands are attributed separately from reviewer-executed
    named validation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact fluorine record is defensible as enantioselective hydrolytic defluorination
  in an engineered laboratory culture. It preserves the racemic denominator, fluoride
  stress, species/strain separation and control limits, without claiming fluorine
  reduction, universal PFAS removal, intracellular concentrations or isolated recovery.
  No actionable curation finding was established.
source:
  git_revision: 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  state: working_tree
  inputs:
  - path: data/records/fluorine.yaml
    sha256: f9f0566c95807e1017edb90b9ae8d51de700b6129788b1fc8d3052e08cfe10c2
    role: target
  - path: history/records/fluorine/2026-10-11T072439Z-codex-95b027.yaml
    sha256: 9a381201a617b1942946b6dd1808aa9cef354121c37c457e6f4004cf7a38c519
    role: context
  - path: research/ingests/round10-b-f-20261011.json
    sha256: b3ac680c2c33e9de07324e191a93d25fdee95127caea3b9826fb5ceda01fe87e
    role: context
  - path: research/ingests/round10-b-f-20261011.md
    sha256: cf537d0d736e0b2acded0677f744cf5f1c94b8af27837922938e72390797faa4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All maintained record fields and linked provenance checked against
    primary evidence and authorities; no sampling of record fields. Search and literature-access
    coverage is explicitly bounded.
  selection: Assigned named record; full field assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:fluorine
targets:
- target_id: cmmmech:fluorine
  path: data/records/fluorine.yaml
  label: Fluorine
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/fluorine.yaml
    role: maintained
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/boron.yaml data/records/fluorine.yaml
  status: passed
  required: true
  summary: Reviewer executed directly; 2 records, 0 failed; terminal exit 0. Earlier
    same successful output retained in /private/tmp/cmm-round10-b-f-independent/named-validation.log.
  target_ids:
  - cmmmech:fluorine
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Parent executed session 84281; reviewer read /private/tmp/cmm-round10-batch-check.log:
    307 passed, 3 skipped in 64.75 s; 61 records and 72 histories valid. Parent separately
    confirmed terminal exit 0.'
  target_ids:
  - cmmmech:fluorine
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Parent executed session 20894; reviewer read /private/tmp/cmm-round10-batch-validation.log:
    61 records, 0 failed. Parent separately confirmed terminal exit 0.'
  target_ids:
  - cmmmech:fluorine
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  status: passed
  required: true
  summary: 'Parent executed session 33751; reviewer read /private/tmp/cmm-round10-batch-history.log:
    72 histories, 0 errors. Parent separately confirmed terminal exit 0.'
  target_ids:
  - cmmmech:fluorine
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/fluorine.yaml
  locator: All fields, linked CREATE sidecar and both shared dossier files
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Reviewed exact pre-assessment working bytes and rechecked all hashes before
    saving. Inline CREATE event and earlier distinct actual CREATE sidecar identify
    the target, Codex actor, GPT-6 model and codex tool; no invented predecessor authorship.
    No record, history or dossier edits by this reviewer.
  snapshot_sha256: f9f0566c95807e1017edb90b9ae8d51de700b6129788b1fc8d3052e08cfe10c2
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:24061
  locator: Released ChEBI entry name, chemical_data formula/charge and structure
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Fluorine atom identity is element F, neutral charge 0. Independently inspected
    and hashed the curator-acquired authoritative JSON. Two live ChEBI page requests
    returned internal errors; retained official API JSON supplied the independent
    inspection.
  snapshot_sha256: 240ca4b13e7cd05936c6917d31d89366b6c15b48a937360c942834005a0cc89b
- evidence_id: organism
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=303&mode=Info
  locator: Taxonomy ID 303, current name and rank
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Independent live and retained authority inspection confirms Pseudomonas
    putida at species rank, separate from ATCC 12633 and its engineered expression
    construct.
  snapshot_sha256: 29b5acb68a34fb99e2f61f21e6f1ac13d266f666256f6450287a9a0fbe4f5b3f
- evidence_id: strain
  kind: database
  reference: https://www.atcc.org/products/12633
  locator: Culture product identity
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Independent live ATCC page and retained catalog establish P. putida 12633.
    The primary introduction isolated 12663 spelling is inconsistent with Methods/Results
    and is explicitly qualified.
  snapshot_sha256: 9af3e04c603531fa6b2b6ecef0cbb106619a1670d812248d938d5bfb03daebba
- evidence_id: criticality
  kind: authority
  reference: https://www.industry.gov.au/publications/australias-critical-minerals-list-and-strategic-materials-list
  locator: 20 February 2024 update; Table 1 Fluorine row, footnote 13
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: 'Live government page independently read: Australia explicitly lists Fluorine
    in Table 1 and dates the update to 20 February 2024. Footnote 13 says US/EU identify
    fluorspar; the record does not transfer those commodity designations to elemental
    fluorine. Direct downloaded authority bytes were unavailable to the curator; this
    successful provider-web reading has no fabricated raw-file hash.'
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/mbio.02785-23
  locator: 'Full main XML: Results, Table 1, Table 2 and Materials and Methods'
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Main study reports engineered P. putida 12633 expressing Delftia strain
    B defluorinase, growth and fluoride release from the two specified racemic mono-fluorinated
    acids. Table 2 gives 9.9±0.1 and 9.9±0.2 mM released fluoride from 20 mM racemates
    at maximum OD times 29/78 h, n=3 biological replicates plus reported independent
    repetition. Purified enzyme no-enzyme controls are distinct from wild-type culture
    nongrowth. Unassigned 28/30-degree flask temperature remains explicit.
  snapshot_sha256: 57fa50ee9f4a234a9cf6e928f60405eb18ef8d5c9da2e1505de8b5ffdee4531e
- evidence_id: figures
  kind: primary_source
  reference: https://doi.org/10.1128/mbio.02785-23
  locator: Main Figures 2 and 3 original JPEG pixels; Table 2 XML cells
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Figure 2 supports growth-associated fluoride release near half the total
    racemate fluorine, and Figure 2F includes initial CFU decline. Figure 3 separates
    residual culture-substrate polarimetry from purified-enzyme D-lactate identification;
    active-site geometry is modeled. No fluoride intracellular concentration or isolated
    product yield follows from these panels.
  snapshot_sha256: 57fa50ee9f4a234a9cf6e928f60405eb18ef8d5c9da2e1505de8b5ffdee4531e
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.1128/mbio.02785-23
  locator: 'Valid mbio.02785-23-s0001.docx: Figures S1–S7 text; S1–S5 embedded image
    pixels; Tables S1/S2 context'
  accessed_at: '2026-10-11T07:32:30Z'
  support: supports
  summary: Independently inspected the valid DOCX and images, not the misleading .docx-named
    challenge HTML. Purification and control context support the enzyme experiments.
    S4 shows lower net fluoride-release trajectory with 5 mM NaF despite main-text
    minimal-inhibition wording; the record makes no no-inhibition claim. S3 conditions
    differ in wording from the main morphology discussion and are not imported quantitatively.
    S5 compares CrcB sequences and locus organization, not a knockout in the curated
    recombinant strain. Main reference to S9 instead of actual S7 is a source cross-reference
    inconsistency, not invented evidence.
  snapshot_sha256: 1f2c1e59d169c3e2df06b551d5bf92dcf2248f8a0d90c71682b6df3704290bd7
- evidence_id: search
  kind: search
  reference: Independent review-session searches and local hidden/ignored inventory
  locator: Exact DOI, title, contrary-evidence and identifier searches
  accessed_at: '2026-10-11T07:32:30Z'
  support: context_only
  summary: 'Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23"
    correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation;
    "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk
    management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract".
    Inspected first returned result sets only. Related reviews, primary citation matches
    and unrelated DOI/title collisions returned; no matched correction or retraction
    of the two accepted primary papers was identified. A retracted 2023 boron review
    is distinct and was not accepted as evidence. This is not an exhaustive registry
    or citation-network audit. rg --no-ignore --hidden searched data, research, reviews
    and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching
    files were inspected/scoped. find of those roots returned no symlinks. Hidden
    and ignored files were included; this is not a home-directory-wide absence claim.'
  search_scope: 'Queries: "10.1016/j.jece.2017.06.044" correction retraction; "10.1128/mbio.02785-23"
    correction retraction; "Streptomyces" "boron" "Moraga" contradiction precipitation;
    "Dodge" "02785-23" defluorinase replication; "Boron contamination and its risk
    management" retraction DOI; "Bio-precipitates produced by two autochthonous" "retract".
    Inspected first returned result sets only. Related reviews, primary citation matches
    and unrelated DOI/title collisions returned; no matched correction or retraction
    of the two accepted primary papers was identified. A retracted 2023 boron review
    is distinct and was not accepted as evidence. This is not an exhaustive registry
    or citation-network audit. rg --no-ignore --hidden searched data, research, reviews
    and the cited raw root for exact target IDs, ChEBI IDs and primary DOIs; 15 matching
    files were inspected/scoped. find of those roots returned no symlinks. Hidden
    and ignored files were included; this is not a home-directory-wide absence claim.'
assessments:
- assessment_id: identity
  area: identity
  topic: Element, substrate and organism identity
  outcome: supported
  summary: Atomic identity and taxonomic scope are supported; chemical feed and resulting
    forms are not conflated with the element.
  target_ids:
  - cmmmech:fluorine
  evidence_ids:
  - record
  - identity
  - organism
- assessment_id: criticality
  area: evidence
  topic: Dated jurisdiction and list designation
  outcome: supported
  summary: The named authority, jurisdiction, list and edition support the record
    mapping with the stated qualifiers.
  target_ids:
  - cmmmech:fluorine
  evidence_ids:
  - record
  - criticality
- assessment_id: mechanism
  area: evidence
  topic: Organism-specific conditions, controls and measured outcome
  outcome: supported
  summary: The exact fluorine record is defensible as enantioselective hydrolytic
    defluorination in an engineered laboratory culture. It preserves the racemic denominator,
    fluoride stress, species/strain separation and control limits, without claiming
    fluorine reduction, universal PFAS removal, intracellular concentrations or isolated
    recovery. No actionable curation finding was established.
  target_ids:
  - cmmmech:fluorine
  evidence_ids:
  - record
  - primary
  - figures
  - supplement
  dimensions:
  - name: material_form
    value: Element F identity; specified racemic alpha-fluorophenylacetic acid or
      2-fluoropropionic acid feeds; inorganic fluoride in medium.
    definition: Fluoride, F2, fluorite mineral and fluorspar commodity remain distinct.
    evidence_ids:
    - record
    - primary
    - figures
  - name: organism_and_biomass
    value: Living recombinant P. putida ATCC 12633 expressing Delftia acidovorans
      strain B defluorinase.
    definition: Species taxonomy does not identify the construct; the tested culture
      differs from purified enzyme assays.
    evidence_ids:
    - record
    - primary
    - figures
  - name: conditions
    value: 20 mM racemic substrate; MSB pH 6.8, 40 mM sodium/potassium phosphate,
      NH4Cl 1 g/L, vitamins/metals and kanamycin 50 micrograms/mL.
    definition: 20 mL in 125 mL baffled flasks at 200 rpm; initial OD600 0.05–0.1;
      washed pregrown inoculum. General flask temperatures 28 or 30 degrees C cannot
      be assigned uniquely; separate plate assay is 30 degrees C.
    evidence_ids:
    - record
    - primary
    - figures
  - name: controls
    value: Wild-type no growth on tested acids; purified enzyme no-enzyme spontaneous-release
      controls; corresponding nonfluorinated products with/without NaF.
    definition: These controls support selective hydrolysis and stress comparisons
      but are not a complete abiotic fluoride-release blank for every culture result.
    evidence_ids:
    - record
    - primary
    - figures
  - name: quantity
    value: Table 2 fluoride 9.9±0.1 / 9.9±0.2 mM, means and SD of three biological
      replicates; 29/78 h to maximum OD600.
    definition: Denominator is 20 mM total racemic substrate; about half the fluorine,
      not complete racemate conversion or recovered-product yield.
    evidence_ids:
    - record
    - primary
    - figures
  - name: deployment
    value: Engineered laboratory model-substrate culture.
    definition: No mineral extraction, environmental waste remediation, industrial
      deployment or universal PFAS degradation was tested in the curated assays.
    evidence_ids:
    - record
    - primary
    - figures
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE provenance
  outcome: supported
  summary: Distinct inline and sidecar events state actual actor/model/tool and target.
    Trusted-base history validation passed; no record edits or fabricated prior authorship
    by reviewer.
  target_ids:
  - cmmmech:fluorine
  evidence_ids:
  - record
- assessment_id: search
  area: completeness
  topic: Bounded duplicate and contrary-evidence coverage
  outcome: supported
  summary: Scoped hidden/ignored inventory and primary internal counterevidence were
    checked. Searches provide bounded coverage, not proof of literature completeness.
  target_ids:
  - cmmmech:fluorine
  evidence_ids:
  - search
  - primary
findings: []
actions: []
limitations:
- The flask temperature is ambiguous between the two general values; intracellular
  fluoride was inferred from cytoplasmic enzyme location, not measured.
- Wild-type nongrowth is not a quantitative abiotic culture-release blank, and CrcB
  causal necessity was not tested by knockout in this strain.
- Supplement S4 limits the main text minimal-inhibition wording; S3 morphology dose
  wording and S7/S9 reference numbering are source inconsistencies not used as new
  quantitative record claims.
- The accepted evidence covers selected monofluorinated model substrates and laboratory
  engineering, not all PFAS, mineral feeds, mixed wastes or recovered fluoride products.
- Australia authority was successfully read live through the web provider without
  a raw-file byte hash; fluorine ChEBI live web opens failed and retained official
  API bytes were independently verified instead.
- Correction/retraction and contrary-evidence searches cover first returned result
  sets and cited local sources, not exhaustive registries or all possible conflicting
  studies.
notes:
- Reviewed final working-tree bytes on trusted base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2;
  this is not a committed-source attestation.
- 'Findings by severity: no confirmed blocker, major, minor or informational curation
  defect. Corrections in this round: none. Unresolved scientific questions are retained
  under limitations; they do not invalidate the qualified observation.'
- Raw source snapshots remain outside Git at /private/tmp/cmm-round10-b-f-raw. Reviewer
  inspections, local search receipt and named validation are under /private/tmp/cmm-round10-b-f-independent.
links:
- https://github.com/CultureBotAI/CMMMech/issues/42
```
