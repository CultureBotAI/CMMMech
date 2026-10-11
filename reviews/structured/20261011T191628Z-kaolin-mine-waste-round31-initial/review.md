# Independent scientific review of kaolin mine waste: bounded repeat-experiment wording

- Review: 20261011T191628Z-kaolin-mine-waste-round31-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T19:13:36.119437Z
- Finished UTC: 2026-10-11T19:16:28.786008Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The narrow mine-discard identity, poor biological performance, EDTA-control limits and chemical comparator are supported. One minor wording claim calls an unquantified repeated218-day experiment successful when the primary only asserts linear increase. Named validation passed; final cohort gates remain pending. Correct this sentence, append history and save an exact-hash successor disposition.

## Scope And Provenance

Every field of one frozen mine-waste record, its two mechanisms and CREATE provenance, grounded against complete original primary and supplement.

Selection: Assigned record curated by a different agent in round31.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 075c1ca032b68162eb8350b7e8d9bfe9530ca143.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:kaolin-mine-waste | data/records/kaolin-mine-waste.yaml | maintained | Kaolin mine waste |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:kaolin-mine-waste | Reviewer executed; terminal session12333 exited0 with Checked1record(s);0failed. Log /private/tmp/cmm-round31-kaolin-waste-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Required batch gate | unavailable | True | cmmmech:kaolin-mine-waste | Parent-coordinated final cohort gate receipt is not yet available at this initial finding observation; no result inferred. |
| Required nonempty gate | unavailable | True | cmmmech:kaolin-mine-waste | Parent-coordinated final cohort gate receipt is not yet available at this initial finding observation; no result inferred. |
| Required history gate | unavailable | True | cmmmech:kaolin-mine-waste | Parent-coordinated final cohort gate receipt is not yet available at this initial finding observation; no result inferred. |

## Scientific And Domain Assessments

### Mine-discard resource, species and criticality boundaries

identity: supported. Targets: cmmmech:kaolin-mine-waste.

Explicit mine-dump provenance supports secondary-resource scope; conflicting geological primary/secondary descriptions do not change mine-discard status. Species-level taxonomy is conservative.

### Biomass, conditions, arms and assay provenance

evidence: supported. Targets: cmmmech:kaolin-mine-waste.

All retained loadings, medium ingredients, culture preparation, filtration and assay distinctions match the primary. Missing leaching temperature, low-iron abiotic arm, pH matching and EDTA-free control remain explicit.

### Assay fractions, oxides, reported percentages and model limits

quantity: supported. Targets: cmmmech:kaolin-mine-waste.

The record retains gross0.83% as unreconciled source-reported result, not net biological yield; chemical32.21% is a distinct nominal assay. Fe2O3 versus Fe, filtrate versus residue, fitted equilibrium/model versus observation, and chromatographic area versus acid concentration are separated accurately.

### Poor performance, unquantified repeat and industrial limits

scope: concern. Targets: cmmmech:kaolin-mine-waste.

The record correctly rejects an industrial deployment/product claim and preserves failed long validation, but the word successful overstates the unquantified repeated218-day assertion.

### Exact sources and authorship; incomplete batch gates

provenance: supported. Targets: cmmmech:kaolin-mine-waste.

Native inspect captured exact working-tree bytes before judgment. Citation/source versions and separate CREATE provenance are accurate; named validation passes. Required final batch/nonempty/history results are not yet available, so this observation is partial.

## Findings

### F1: Do not call the unquantified 218-day repeat successful

minor / open / confirmed; issue key: CMMMech.kaolin-mine-waste.unquantified-repeat-success.

The second chemical-comparator evidence explanation calls a repeated218-day experiment successful. Original printedp393 only asserts that iron leaching increased linearly with time, without numerical repeat data or a final endpoint establishing successful beneficiation/complete removal. Preserve that narrower source claim without the adjective successful.

## Recommended Actions And Acceptance Checks

### A1

Replace successful-repeat wording with the exact bounded assertion that leaching increased linearly with time in a repeated218-day experiment without the corresponding numerical dataset. Append canonical EDIT history and a distinct inline event; preserve original source dossier and initial review.

- Changed sentence does not imply successful beneficiation, complete removal, isolated recovery or a quantified endpoint.
- Re-read printedp393, capture corrected record/history hashes, and validate the exact record and append-only history against trusted base.
- Final required batch/nonempty/history results are available and a successor review retains this stable issue_key and exact previous_occurrences.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/kaolin-mine-waste.yaml; Every field, two mechanisms and distinct inline CREATE event | supports | Frozen record accurately distinguishes mine discard from natural kaolin and mineral species, preserves source contradictions and poor performance; one adjective overstates an unquantified repeat experiment. |
| primary | https://doi.org/10.1007/s42860-022-00192-7; Complete original 19-page PDF pp386-404; all12 original figures and Tables1-4 visually inspected; all methods/results and references read | supports | Main methods explicitly identify Caobar mine waste, independently cultured wastewater isolate91, EDTA-containing medium and paired high-iron control. Figures7-12 show gross microbial versus chemical-medium leaching, clipped D2 day7 totalFe bar, nonmonotonic acid/Fe patterns and plotted pH near6.8 rather than method7.5. Table3 uses Fe2O3 mass percentages. Tables1/4 support ten chemical runs and32.21% source-reported removal; 218-day validation gives traces of solutionFe and3.42%Fe2O3 residue. The record properly separates proposed causal explanations from measured quantities. |
| repeat | https://doi.org/10.1007/s42860-022-00192-7; Printed p393, Chemical Leaching Results, final paragraph before Bacterial Leaching Results; original PDFpage8 visually read | refutes | The prose asserts iron leaching increased linearly with time in a repeated218-day experiment. It supplies no corresponding numerical trajectory, final extraction amount or commercial-quality endpoint. The maintained adjective successful can imply a demonstrated success beyond this unquantified assertion. |
| supplement | https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs42860-022-00192-7/MediaObjects/42860_2022_192_MOESM1_ESM.docx; Complete original DOCX text and all four embedded images, including duplicate S1 geological-map asset; S1-S3 | supports | Supplement describes sedimentary Utrillas Formation and secondary geological origin, conflicting with main introduction primary in-place granite wording. This geological discrepancy is distinct from explicit mine-discard identity. S3 is a midway photograph of yellow suspension, not a final recovery or phase measurement. Full OOXML text and original images inspected; printed DOCX pagination not rendered. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1428&amp;mode=Info; Live official current name, species rank and Bacillus cereus group lineage opened by reviewer11October2026 | supports | NCBITaxon1428 is Bacillus thuringiensis at species level. It does not authenticate source isolate91 as EB63 or supply missing sequence accession; the record explicitly retains that boundary. |
| metadata | https://api.crossref.org/works/10.1007/s42860-022-00192-7; Retained Crossref payload, original publisher landing and original PDF title/header | supports | DOI/title/ten authors, volume70 and pp386-404 match. Original Springer landing says7July2022; Crossref/Cambridge online2024 is rehosting, not a new experiment. Crossref update-to absent and relation empty in retained payload. |
| dedup | /private/tmp/cmm-round31-kaolin-waste-independent/dedup.json; Exact independent command,188 matching lines and retained boundaries | supports | Current new mine-waste record and separately curated natural kaolin record are distinct maintained material forms. No earlier accepted Caobar waste experiment was identified in searched text. The original binary PDFs/images/Office files were not used as text-search negatives; adopted originals were independently inspected. |
| notices | Independent web search11October2026; First returned results from two exact DOI/title queries; original publisher and NCBI pages opened | supports | No affecting correction/retraction identified in checked results or Crossref fields. Results identify the same2022 experiment under laterCambridge hosting; snippets of other Bacillus/kaolin studies do not establish directly contradictory results for the same Caobar feed. |
| history | history/records/kaolin-mine-waste/2026-10-11T191240Z-codex-59f11b.yaml; Complete CREATE sidecar and separate inline event | supports | Codex/GPT-6/codex creation at19:12:40Z targets exact new file and records source/poor-performance limits, with independent review and full gates still pending. No earlier authorship is invented. |

## Limits And Additional Notes

- Final full-cohort required checks are not yet available; completion is partial, not acceptance.
- The source does not supply raw biological assay data, exact0.83% calculation, low-iron abiotic control, EDTA-free or matched-pH control, exact mineral-incubation temperature or authenticated isolate accession.
- Modelled pH/Eh speciation and lauric-acid area cannot establish a specific respiratory or organic-acid cause; failed long-duration validation lacks independent precipitate identity/temperature causality.
- Searches have declared text/binary and first-result notice boundaries; no exhaustive absence claim.
- Original fullPDF and supplement were accessed through curator-retained legitimate publisher downloads; reviewer independently assessed all adopted claims.
- The minor issue concerns maintained wording, not a demand to repair the source paper or invent missing measurements.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191628Z-kaolin-mine-waste-round31-initial
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent scientific review of kaolin mine waste: bounded repeat-experiment
  wording'
started_at: '2026-10-11T19:13:36.119437Z'
finished_at: '2026-10-11T19:16:28.786008Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Another agent authored this record/history/dossier. Reviewer
    authored only separate stibnite and tungsten research this round. Native inspect
    preceded judgment; reviewer independently read complete primary methods/results,
    original figures/tables, supplement, taxonomy, source metadata and bounded dedup/notices.
    Shared worktree and curator-acquired artifacts are disclosed. No maintained record/history/dossier
    edits by reviewer.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The narrow mine-discard identity, poor biological performance, EDTA-control
  limits and chemical comparator are supported. One minor wording claim calls an unquantified
  repeated218-day experiment successful when the primary only asserts linear increase.
  Named validation passed; final cohort gates remain pending. Correct this sentence,
  append history and save an exact-hash successor disposition.
source:
  git_revision: 075c1ca032b68162eb8350b7e8d9bfe9530ca143
  state: working_tree
  inputs:
  - path: data/records/kaolin-mine-waste.yaml
    sha256: 9b827fa7da79c540e5d997a1f1d54fe6d68b14bd99fe3cad3117202e29ba04a1
    role: target
  - path: history/records/kaolin-mine-waste/2026-10-11T191240Z-codex-59f11b.yaml
    sha256: 3973b7c9c417bae7f9b20e800b783c0326243d62b15068aa8421309760592ddb
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every field of one frozen mine-waste record, its two mechanisms and
    CREATE provenance, grounded against complete original primary and supplement.
  selection: Assigned record curated by a different agent in round31.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:kaolin-mine-waste
  exclusions:
  - target: Raw instrument data and new kaolin studies
    reason: No instrument reprocessing or new mechanism curation; unprovided datasets
      cannot be inferred from source prose.
targets:
- target_id: cmmmech:kaolin-mine-waste
  path: data/records/kaolin-mine-waste.yaml
  label: Kaolin mine waste
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin-mine-waste.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/kaolin-mine-waste.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed; terminal session12333 exited0 with Checked1record(s);0failed.
    Log /private/tmp/cmm-round31-kaolin-waste-independent/named-validation.log SHA256
    6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:kaolin-mine-waste
- check_id: batch
  name: Required batch gate
  command: just check
  status: unavailable
  required: true
  summary: Parent-coordinated final cohort gate receipt is not yet available at this
    initial finding observation; no result inferred.
  target_ids:
  - cmmmech:kaolin-mine-waste
- check_id: nonempty
  name: Required nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: unavailable
  required: true
  summary: Parent-coordinated final cohort gate receipt is not yet available at this
    initial finding observation; no result inferred.
  target_ids:
  - cmmmech:kaolin-mine-waste
- check_id: history
  name: Required history gate
  command: uv run --locked cmmmech validate-history --base 075c1ca032b68162eb8350b7e8d9bfe9530ca143
  status: unavailable
  required: true
  summary: Parent-coordinated final cohort gate receipt is not yet available at this
    initial finding observation; no result inferred.
  target_ids:
  - cmmmech:kaolin-mine-waste
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/kaolin-mine-waste.yaml
  locator: Every field, two mechanisms and distinct inline CREATE event
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: Frozen record accurately distinguishes mine discard from natural kaolin
    and mineral species, preserves source contradictions and poor performance; one
    adjective overstates an unquantified repeat experiment.
  snapshot_sha256: 9b827fa7da79c540e5d997a1f1d54fe6d68b14bd99fe3cad3117202e29ba04a1
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1007/s42860-022-00192-7
  locator: Complete original 19-page PDF pp386-404; all12 original figures and Tables1-4
    visually inspected; all methods/results and references read
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: Main methods explicitly identify Caobar mine waste, independently cultured
    wastewater isolate91, EDTA-containing medium and paired high-iron control. Figures7-12
    show gross microbial versus chemical-medium leaching, clipped D2 day7 totalFe
    bar, nonmonotonic acid/Fe patterns and plotted pH near6.8 rather than method7.5.
    Table3 uses Fe2O3 mass percentages. Tables1/4 support ten chemical runs and32.21%
    source-reported removal; 218-day validation gives traces of solutionFe and3.42%Fe2O3
    residue. The record properly separates proposed causal explanations from measured
    quantities.
  snapshot_sha256: b9ad212cb085303beecb2f564963666e47d37715cbd67e211a49bc1e69bbcbaf
- evidence_id: repeat
  kind: primary_source
  reference: https://doi.org/10.1007/s42860-022-00192-7
  locator: Printed p393, Chemical Leaching Results, final paragraph before Bacterial
    Leaching Results; original PDFpage8 visually read
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: refutes
  summary: The prose asserts iron leaching increased linearly with time in a repeated218-day
    experiment. It supplies no corresponding numerical trajectory, final extraction
    amount or commercial-quality endpoint. The maintained adjective successful can
    imply a demonstrated success beyond this unquantified assertion.
  snapshot_sha256: c31e66b863c70b2ca4b293ebc79d51b7b249454425383643d8d165738a85243f
- evidence_id: supplement
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs42860-022-00192-7/MediaObjects/42860_2022_192_MOESM1_ESM.docx
  locator: Complete original DOCX text and all four embedded images, including duplicate
    S1 geological-map asset; S1-S3
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: Supplement describes sedimentary Utrillas Formation and secondary geological
    origin, conflicting with main introduction primary in-place granite wording. This
    geological discrepancy is distinct from explicit mine-discard identity. S3 is
    a midway photograph of yellow suspension, not a final recovery or phase measurement.
    Full OOXML text and original images inspected; printed DOCX pagination not rendered.
  snapshot_sha256: 89d61428bcca71f324637b0f4681b816c66d960a03e5bf8d7064b2c57e12e579
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1428&mode=Info
  locator: Live official current name, species rank and Bacillus cereus group lineage
    opened by reviewer11October2026
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: NCBITaxon1428 is Bacillus thuringiensis at species level. It does not authenticate
    source isolate91 as EB63 or supply missing sequence accession; the record explicitly
    retains that boundary.
- evidence_id: metadata
  kind: database
  reference: https://api.crossref.org/works/10.1007/s42860-022-00192-7
  locator: Retained Crossref payload, original publisher landing and original PDF
    title/header
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: DOI/title/ten authors, volume70 and pp386-404 match. Original Springer
    landing says7July2022; Crossref/Cambridge online2024 is rehosting, not a new experiment.
    Crossref update-to absent and relation empty in retained payload.
  snapshot_sha256: 2b2bc859ffa69bf5cf3dfc567011bac5fecb05ae7443dc0ff0d1160e866dc636
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round31-kaolin-waste-independent/dedup.json
  locator: Exact independent command,188 matching lines and retained boundaries
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: Current new mine-waste record and separately curated natural kaolin record
    are distinct maintained material forms. No earlier accepted Caobar waste experiment
    was identified in searched text. The original binary PDFs/images/Office files
    were not used as text-search negatives; adopted originals were independently inspected.
  snapshot_sha256: 60e5e4e5e50f32d4dc83cb1df2fddbcf6452210f3c0005c4c053b52826255e55
  search_scope: Hidden/ignored included; relevant symlinks followed across current
    and original maintained/research/review/history and explicitly inventoried available
    non-cache prior raw roots, plus exact new kaolin raw. PDF/image/Office/zip bytes
    excluded from text matching; source originals inspected separately. No global
    binary/OCR completeness claim.
- evidence_id: notices
  kind: search
  reference: Independent web search11October2026
  locator: First returned results from two exact DOI/title queries; original publisher
    and NCBI pages opened
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: No affecting correction/retraction identified in checked results or Crossref
    fields. Results identify the same2022 experiment under laterCambridge hosting;
    snippets of other Bacillus/kaolin studies do not establish directly contradictory
    results for the same Caobar feed.
  search_scope: 'Queries: "10.1007/s42860-022-00192-7" correction erratum retraction;
    "Iron Removal from Kaolin Waste Dumps" "Bacillus". First result sets, no date
    filter or pagination; no exhaustive notice or literature absence claim.'
- evidence_id: history
  kind: record_content
  reference: history/records/kaolin-mine-waste/2026-10-11T191240Z-codex-59f11b.yaml
  locator: Complete CREATE sidecar and separate inline event
  accessed_at: '2026-10-11T19:16:28.786008Z'
  support: supports
  summary: Codex/GPT-6/codex creation at19:12:40Z targets exact new file and records
    source/poor-performance limits, with independent review and full gates still pending.
    No earlier authorship is invented.
  snapshot_sha256: 3973b7c9c417bae7f9b20e800b783c0326243d62b15068aa8421309760592ddb
assessments:
- assessment_id: identity
  area: identity
  topic: Mine-discard resource, species and criticality boundaries
  outcome: supported
  summary: Explicit mine-dump provenance supports secondary-resource scope; conflicting
    geological primary/secondary descriptions do not change mine-discard status. Species-level
    taxonomy is conservative.
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - record
  - primary
  - supplement
  - taxon
  - dedup
  dimensions:
  - name: material_form
    value: 'Secondary resource: discarded mixed kaolin mine feed'
    definition: This is not processing tailings, a pure kaolinite species or ordinary
      extracted natural feed.
    evidence_ids:
    - primary
    - supplement
  - name: criticality
    value: Not asserted
    definition: No constituent criticality or source use of commercial value is inherited.
    evidence_ids:
    - record
  - name: organism
    value: Source isolate91; species mapping NCBITaxon1428 only
    definition: EB63 is a published identification label without sequence accession
      or verified culture-stock mapping.
    evidence_ids:
    - primary
    - taxon
- assessment_id: methods
  area: evidence
  topic: Biomass, conditions, arms and assay provenance
  outcome: supported
  summary: All retained loadings, medium ingredients, culture preparation, filtration
    and assay distinctions match the primary. Missing leaching temperature, low-iron
    abiotic arm, pH matching and EDTA-free control remain explicit.
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biomass
    value: Living wastewater-derived Bacillus isolate
    definition: Culture reactivation30C24h is not an unambiguous mineral-incubation
      temperature. Inoculum clumps mean comparable, not identical aliquots.
    evidence_ids:
    - primary
    - record
  - name: conditions
    value: 12.5g feed,250mL medium,1mL inoculum,14days
    definition: Approximately5x10^4 CFU/mL describes pre-dilution inoculum; EDTA0.75g/L
      and20g/L glucose are retained.
    evidence_ids:
    - primary
  - name: controls
    value: Matched high-iron uninoculated medium; low-iron control absent
    definition: Abiotic leaching and differing pH prevent uniquely attributing all
      dissolvedFe to bacterial activity.
    evidence_ids:
    - primary
    - record
- assessment_id: quantity
  area: quantity
  topic: Assay fractions, oxides, reported percentages and model limits
  outcome: supported
  summary: The record retains gross0.83% as unreconciled source-reported result, not
    net biological yield; chemical32.21% is a distinct nominal assay. Fe2O3 versus
    Fe, filtrate versus residue, fitted equilibrium/model versus observation, and
    chromatographic area versus acid concentration are separated accurately.
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: microbial_result
    value: Source-reported maximum0.83% with uncertain calculation/arm/time
    definition: 14.9mg/L D2day7 caption and clippedFigure10 bar cannot transparently
      reconstruct the reported maximum; no closed mass balance asserted.
    evidence_ids:
    - primary
    - record
  - name: chemical_result
    value: Table4 experiment4:32.21% Fe removal
    definition: Nominal100mM each acid,1g/100mL,60days,pH0.74. Stock versus final
      mixed acid concentration is not clarified.
    evidence_ids:
    - primary
  - name: measurement_basis
    value: AAS totalFe; colorimetricFeII; differenceFeIII; GC-MS percent area
    definition: No isotope/specific respiratory activity, isolated product or direct
      mineral phase identification is established by these measurements.
    evidence_ids:
    - primary
    - record
- assessment_id: scope
  area: scope
  topic: Poor performance, unquantified repeat and industrial limits
  outcome: concern
  summary: The record correctly rejects an industrial deployment/product claim and
    preserves failed long validation, but the word successful overstates the unquantified
    repeated218-day assertion.
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - record
  - primary
  - repeat
  - supplement
- assessment_id: provenance
  area: provenance
  topic: Exact sources and authorship; incomplete batch gates
  outcome: supported
  summary: Native inspect captured exact working-tree bytes before judgment. Citation/source
    versions and separate CREATE provenance are accurate; named validation passes.
    Required final batch/nonempty/history results are not yet available, so this observation
    is partial.
  target_ids:
  - cmmmech:kaolin-mine-waste
  evidence_ids:
  - record
  - history
  - metadata
  - notices
findings:
- finding_id: F1
  issue_key: CMMMech.kaolin-mine-waste.unquantified-repeat-success
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Do not call the unquantified 218-day repeat successful
  description: The second chemical-comparator evidence explanation calls a repeated218-day
    experiment successful. Original printedp393 only asserts that iron leaching increased
    linearly with time, without numerical repeat data or a final endpoint establishing
    successful beneficiation/complete removal. Preserve that narrower source claim
    without the adjective successful.
  target_ids:
  - cmmmech:kaolin-mine-waste
  field_paths:
  - mechanisms[id=chemical_oxalate_comparator].evidence[1].explanation
  evidence_ids:
  - record
  - repeat
  - primary
  rule_id: preserve-measured-versus-asserted-outcome
  native_severity: minor
  normalization_reason: Bounded wording overreach within an otherwise explicitly limited
    record; it does not change material identity or the stated failed validation and
    nonindustrial conclusion.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin-mine-waste.yaml
    role: maintained_record
actions:
- action_id: A1
  description: Replace successful-repeat wording with the exact bounded assertion
    that leaching increased linearly with time in a repeated218-day experiment without
    the corresponding numerical dataset. Append canonical EDIT history and a distinct
    inline event; preserve original source dossier and initial review.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:kaolin-mine-waste
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kaolin-mine-waste.yaml
    role: maintained_record
  acceptance_checks:
  - Changed sentence does not imply successful beneficiation, complete removal, isolated
    recovery or a quantified endpoint.
  - Re-read printedp393, capture corrected record/history hashes, and validate the
    exact record and append-only history against trusted base.
  - Final required batch/nonempty/history results are available and a successor review
    retains this stable issue_key and exact previous_occurrences.
limitations:
- Final full-cohort required checks are not yet available; completion is partial,
  not acceptance.
- The source does not supply raw biological assay data, exact0.83% calculation, low-iron
  abiotic control, EDTA-free or matched-pH control, exact mineral-incubation temperature
  or authenticated isolate accession.
- Modelled pH/Eh speciation and lauric-acid area cannot establish a specific respiratory
  or organic-acid cause; failed long-duration validation lacks independent precipitate
  identity/temperature causality.
- Searches have declared text/binary and first-result notice boundaries; no exhaustive
  absence claim.
notes:
- Original fullPDF and supplement were accessed through curator-retained legitimate
  publisher downloads; reviewer independently assessed all adopted claims.
- The minor issue concerns maintained wording, not a demand to repair the source paper
  or invent missing measurements.
links:
- https://doi.org/10.1007/s42860-022-00192-7
- research/sources/round31-kaolin-waste/20261011T191406Z-source-investigation.md
tags:
- round31
- independent
- scientific
- kaolin-mine-waste
```
