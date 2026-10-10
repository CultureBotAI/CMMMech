# Neodymium source-led PR adversarial review

- Review: 20261010T011852Z-neodymium-pr-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-10T01:15:15.003680Z
- Finished UTC: 2026-10-10T01:18:52Z
- Reviewer: Codex /root/publish_other_records_20261009 (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

New Nd bioleaching claims match the primary methods and inspected workbook. Mixed phases, relative improvement, control-data limits and transposon/deletion disagreement remain explicit.

## Scope And Provenance

New Gluconobacter synthetic-phosphate mechanism, workbook comparison, US-2025 and EU-2024 designations, conceptual identity and provenance. Existing Chlorella biosorption and US-2022 claims are preservation-only.

Selection: This named record is one of seven assigned PR targets; one record per review bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c0adc2c0763e1515ed07dc712b024974d98fb342.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:neodymium | data/records/neodymium.yaml | maintained | Neodymium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Affected seven-record strict validation | passed | True | cmmmech:neodymium | Seven records checked; zero failures. |
| History linkage and append-only base check | passed | True | cmmmech:neodymium | 19 history sessions checked; zero errors. Base was origin/main at the available admitted main revision. |

## Scientific And Domain Assessments

### Mixed-phase Nd solubilization versus causality and yield

evidence: supported. Targets: cmmmech:neodymium.

New Nd bioleaching claims match the primary methods and inspected workbook. Mixed phases, relative improvement, control-data limits and transposon/deletion disagreement remain explicit.

Biolixiviant generation uses living B58 derivatives; NCBITaxon:442 denotes species. ICP-MS leachate is a dissolved-element endpoint, not product recovery. The workbook header is micrograms Nd per gram NdPO4; no absolute percentage yield is created. Wild-type and intergenic-transposon proxy controls are distinct. Parsed comparison proves the prior Chlorella mechanism is unchanged.

### Maintained record and append-only history

provenance: supported. Targets: cmmmech:neodymium.

Exact file hash captured by shared inspect before assessment; extra history inputs captured before their assessment. New events describe actual scoped additions; prior immutable sessions preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| us2025 | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final table, printed pp. 50496–50497; notice publication 7 November 2025 | supports | Read official title, edition and named commodity rows. Cobalt, neodymium, manganese and palladium are explicitly listed. A commodity listing does not name every bearing compound or waste. |
| eu2024 | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401252; Original OJ PDF pp. 57–58, Annex II Section 1(h),(r),(u),(aa) | supports | Retained official PDF and extracted Annex II checked. Critical entries include cobalt, light rare earth elements, manganese and platinum group metals. Original 2024 act is the asserted edition, not an undated latest-law claim. Fresh web route redirected to OJ landing; retained original PDF was used. |
| ecgroups | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52017DC0490; COM(2017) 490 final, Annex 1 p.4, footnotes 12–13 | supports | Read neodymium among light rare earths and palladium among platinum group metals. Used solely for explicit group membership; 2024 designation derives separately from Annex II. |
| tax442 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=442&amp;retmode=xml; Taxon 442, ScientificName and Rank | supports | Retained issuing-authority XML resolves Gluconobacter oxydans at species rank. Live web renderer was unavailable. This does not independently identify B58 or engineered derivatives. |
| marecos | https://doi.org/10.1038/s42003-025-08061-4; Results Mon1/Mon2 and Figures 3–5; Methods Direct REE-bioleaching measurements | supports | Retained full text independently reread. Mon2 is mixed monazite-Nd/rhabdophane-Nd. Methods support 20% glucose biolixiviant, 1% pulp, 24 h, 30 C, 200 rpm, three replicates and filtration after contact. No precontact cell-removal step is specified. GO_1096 clean deletion differs from transposon disruption. |
| data4 | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42003-025-08061-4/MediaObjects/42003_2025_8061_MOESM6_ESM.xlsx; Sheet 4A A3:D44, especially B6:B8 and B27:B29; Sheet 4B A3:D11 | supports | Independently parsed both worksheet XMLs: 42 bacterial observations in 4A, 14 strain labels with triplicates, pH 2.17–2.84; no no-bacteria label in those populated rows. GO_1598 versus pWT B means give approximately 111% relative increase. Sheet 4B is a distinct 9-observation experiment. |
| ndidentity | https://www.ebi.ac.uk/chebi/CHEBI:33372; Canonical entry CHEBI:33372 | supports | Live authority identifies neodymium atom; it does not denote its ionic form, mineral or magnet. |
| record | data/records/neodymium.yaml; Entire current file, working diff against origin/main, inline history and linked sidecars | supports | Read exact maintained YAML and provenance. History targets/actors/timestamps agree with inline events; committed prior history is preserved. |
| prior | reviews/records/neodymium/20261006T042218Z.md; Scope, evidence and limitations | context_only | Read prior independent primary-evidence review. Retained scientific fields were compared programmatically with origin/main; prior literature is not claimed as newly inspected. |
| search | Web search and local scoped review; First returned result set, no pagination | context_only | No directly affecting correction notice identified in this bounded search; this is not an exhaustive claim. Retained known within-study contrary evidence remains explicit. |

## Limits And Additional Notes

- No raw ICP-MS reconstruction, mineral batch recharacterization or comprehensive literature integrity audit. Workbook-only reconstruction lacks no-bacteria observations. Molecular lixiviants remain unidentified.
- Chlorella 2017 mechanism, its strain catalogue and US-2022 listing were retained by field comparison and the historical independent review, not freshly reassessed.
- Bounded correction searches are not an exhaustive retraction audit. Validation checks the contract, not scientific truth. Root coordinator owns final just check and nonempty-corpus PR gates.
- No record corrections were required or performed in this independent pass. Empty findings is scoped to this target and the declared review, not a fleet-wide pass.
- Reviewed Git revision includes the origin/main governance merge; source state is working_tree as reported by inspect. Historical Markdown reviews remain unmodified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T011852Z-neodymium-pr-science
kind: record
repository: CultureBotAI/CMMMech
title: Neodymium source-led PR adversarial review
started_at: '2026-10-10T01:15:15.003680Z'
finished_at: '2026-10-10T01:18:52Z'
reviewer:
  identity: Codex /root/publish_other_records_20261009
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Fresh review agent distinct from the record curators and prior
    reviewers; no record or curation-history edits performed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: New Nd bioleaching claims match the primary methods and inspected workbook.
  Mixed phases, relative improvement, control-data limits and transposon/deletion
  disagreement remain explicit.
source:
  git_revision: c0adc2c0763e1515ed07dc712b024974d98fb342
  state: working_tree
  inputs:
  - path: data/records/neodymium.yaml
    sha256: 3740247c0a93c9af1e068719aa552b43ead2c62b015f3ae98071972b84d88268
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/neodymium/2026-10-08T023605Z-codex-131e84.yaml
    sha256: 8f7956e9b75412067b985f4ecb8020e0945b385af6cadd9d90a00f035174c51b
    role: context
  - path: history/records/neodymium/2026-10-09T044752Z-codex-7f72ec.yaml
    sha256: dd928b87ed45a0b58ac0038af621f544c2e4ce82ddad961ddca9dd86e1307b4e
    role: context
  - path: history/records/neodymium/2026-10-09T055127Z-codex-172ef4.yaml
    sha256: 04f0b43d3f9a510f16da3be44de005a961d2d642a2243ad969fe16b41aea0884
    role: context
  - path: reviews/records/neodymium/20261006T042218Z.md
    sha256: 1767a91ebd1d7dde4a4985262c37a9deb1715b3b4509cc76434b0da3c2603c46
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: New Gluconobacter synthetic-phosphate mechanism, workbook comparison,
    US-2025 and EU-2024 designations, conceptual identity and provenance. Existing
    Chlorella biosorption and US-2022 claims are preservation-only.
  selection: This named record is one of seven assigned PR targets; one record per
    review bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:neodymium
targets:
- target_id: cmmmech:neodymium
  path: data/records/neodymium.yaml
  label: Neodymium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/neodymium.yaml
    role: maintained scientific record
checks:
- check_id: record-validation
  name: Affected seven-record strict validation
  status: passed
  required: true
  summary: Seven records checked; zero failures.
  target_ids:
  - cmmmech:neodymium
  command: .venv/bin/cmmmech validate data/records/cobalt.yaml data/records/neodymium.yaml
    data/records/palladium.yaml data/records/manganese.yaml data/records/cobaltite.yaml
    data/records/monazite-nd.yaml data/records/fluorescent-lamp-phosphor.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: history-validation
  name: History linkage and append-only base check
  status: passed
  required: true
  summary: 19 history sessions checked; zero errors. Base was origin/main at the available
    admitted main revision.
  target_ids:
  - cmmmech:neodymium
  command: .venv/bin/cmmmech validate-history --base origin/main
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: us2025
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final table, printed pp. 50496–50497; notice publication 7 November 2025
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Read official title, edition and named commodity rows. Cobalt, neodymium,
    manganese and palladium are explicitly listed. A commodity listing does not name
    every bearing compound or waste.
- evidence_id: eu2024
  kind: authority
  reference: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401252
  locator: Original OJ PDF pp. 57–58, Annex II Section 1(h),(r),(u),(aa)
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Retained official PDF and extracted Annex II checked. Critical entries
    include cobalt, light rare earth elements, manganese and platinum group metals.
    Original 2024 act is the asserted edition, not an undated latest-law claim. Fresh
    web route redirected to OJ landing; retained original PDF was used.
  snapshot_sha256: eb89f374a725ebde267c90f237898cd1d0bdfa65a1d4a118511e225bde60283e
- evidence_id: ecgroups
  kind: authority
  reference: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52017DC0490
  locator: COM(2017) 490 final, Annex 1 p.4, footnotes 12–13
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Read neodymium among light rare earths and palladium among platinum group
    metals. Used solely for explicit group membership; 2024 designation derives separately
    from Annex II.
  snapshot_sha256: 9a3407b786c9cefb486a84e456b0411537593d5da14b35e18f0f1585ad04718d
- evidence_id: tax442
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=442&retmode=xml
  locator: Taxon 442, ScientificName and Rank
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Retained issuing-authority XML resolves Gluconobacter oxydans at species
    rank. Live web renderer was unavailable. This does not independently identify
    B58 or engineered derivatives.
  snapshot_sha256: 89f99310d5d7c407ef81f67b1446286364362a850c9e49e3e1d4518822fb9c5f
- evidence_id: marecos
  kind: primary_source
  reference: https://doi.org/10.1038/s42003-025-08061-4
  locator: Results Mon1/Mon2 and Figures 3–5; Methods Direct REE-bioleaching measurements
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Retained full text independently reread. Mon2 is mixed monazite-Nd/rhabdophane-Nd.
    Methods support 20% glucose biolixiviant, 1% pulp, 24 h, 30 C, 200 rpm, three
    replicates and filtration after contact. No precontact cell-removal step is specified.
    GO_1096 clean deletion differs from transposon disruption.
  snapshot_sha256: 3010ce6ce2448298d1a649ab227e80639feb3c43faf6f59742b5781f48c56f9e
- evidence_id: data4
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42003-025-08061-4/MediaObjects/42003_2025_8061_MOESM6_ESM.xlsx
  locator: Sheet 4A A3:D44, especially B6:B8 and B27:B29; Sheet 4B A3:D11
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: 'Independently parsed both worksheet XMLs: 42 bacterial observations in
    4A, 14 strain labels with triplicates, pH 2.17–2.84; no no-bacteria label in those
    populated rows. GO_1598 versus pWT B means give approximately 111% relative increase.
    Sheet 4B is a distinct 9-observation experiment.'
  snapshot_sha256: 3e9725efe640ee5a510a5f0f733145172b7473c586a54e4fb1b1f2bcd685d07c
- evidence_id: ndidentity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33372
  locator: Canonical entry CHEBI:33372
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Live authority identifies neodymium atom; it does not denote its ionic
    form, mineral or magnet.
- evidence_id: record
  kind: record_content
  reference: data/records/neodymium.yaml
  locator: Entire current file, working diff against origin/main, inline history and
    linked sidecars
  accessed_at: '2026-10-10T01:18:41Z'
  support: supports
  summary: Read exact maintained YAML and provenance. History targets/actors/timestamps
    agree with inline events; committed prior history is preserved.
  snapshot_sha256: 3740247c0a93c9af1e068719aa552b43ead2c62b015f3ae98071972b84d88268
- evidence_id: prior
  kind: prior_review
  reference: reviews/records/neodymium/20261006T042218Z.md
  locator: Scope, evidence and limitations
  accessed_at: '2026-10-10T01:18:41Z'
  support: context_only
  summary: Read prior independent primary-evidence review. Retained scientific fields
    were compared programmatically with origin/main; prior literature is not claimed
    as newly inspected.
  snapshot_sha256: 1767a91ebd1d7dde4a4985262c37a9deb1715b3b4509cc76434b0da3c2603c46
- evidence_id: search
  kind: search
  reference: Web search and local scoped review
  locator: First returned result set, no pagination
  accessed_at: '2026-10-10T01:18:41Z'
  support: context_only
  summary: No directly affecting correction notice identified in this bounded search;
    this is not an exhaustive claim. Retained known within-study contrary evidence
    remains explicit.
  search_scope: '"10.1038/s42003-025-08061-4" correction retraction. Local file discovery
    included hidden/ignored files with rg --no-ignore --hidden; no machine-wide absence
    claim. Source bodies and relevant supplements were separately inspected as listed.'
assessments:
- assessment_id: scientific-scope
  area: evidence
  topic: Mixed-phase Nd solubilization versus causality and yield
  outcome: supported
  summary: New Nd bioleaching claims match the primary methods and inspected workbook.
    Mixed phases, relative improvement, control-data limits and transposon/deletion
    disagreement remain explicit.
  target_ids:
  - cmmmech:neodymium
  evidence_ids:
  - us2025
  - eu2024
  - ecgroups
  - tax442
  - marecos
  - data4
  - ndidentity
  - record
  details: Biolixiviant generation uses living B58 derivatives; NCBITaxon:442 denotes
    species. ICP-MS leachate is a dissolved-element endpoint, not product recovery.
    The workbook header is micrograms Nd per gram NdPO4; no absolute percentage yield
    is created. Wild-type and intergenic-transposon proxy controls are distinct. Parsed
    comparison proves the prior Chlorella mechanism is unchanged.
  dimensions:
  - name: material_form
    value: Element Nd; new substrate Mon2 is synthetic monazite-Nd plus rhabdophane-Nd,
      not a pure mineral species or natural ore.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
  - name: criticality
    value: US final 2025 and EU 2024 Annex II(r) light rare earth elements; COM(2017)490
      footnote 12 supplies Nd group membership.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
  - name: organism
    value: Gluconobacter oxydans species 442; B58 and derivatives described by the
      study.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
  - name: conditions_controls
    value: 20% glucose production; 1% pulp, 24 h, 30 C, 200 rpm; triplicates, WT/pWT,
      described no-bacteria control.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
  - name: outcome
    value: Reported 56–111% relative improvement in 8 of 12 selected disruptions;
      not fraction of feed Nd recovered.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
  - name: deployment_scope
    value: Laboratory solubilization only.
    definition: Reviewed domain scope; preserves representation and evidentiary limits.
    evidence_ids:
    - us2025
    - eu2024
    - ecgroups
    - tax442
    - marecos
    - data4
    - ndidentity
    - record
- assessment_id: provenance
  area: provenance
  topic: Maintained record and append-only history
  outcome: supported
  summary: Exact file hash captured by shared inspect before assessment; extra history
    inputs captured before their assessment. New events describe actual scoped additions;
    prior immutable sessions preserved.
  target_ids:
  - cmmmech:neodymium
  evidence_ids:
  - record
findings: []
actions: []
limitations:
- No raw ICP-MS reconstruction, mineral batch recharacterization or comprehensive
  literature integrity audit. Workbook-only reconstruction lacks no-bacteria observations.
  Molecular lixiviants remain unidentified.
- Chlorella 2017 mechanism, its strain catalogue and US-2022 listing were retained
  by field comparison and the historical independent review, not freshly reassessed.
- Bounded correction searches are not an exhaustive retraction audit. Validation checks
  the contract, not scientific truth. Root coordinator owns final just check and nonempty-corpus
  PR gates.
notes:
- No record corrections were required or performed in this independent pass. Empty
  findings is scoped to this target and the declared review, not a fleet-wide pass.
- Reviewed Git revision includes the origin/main governance merge; source state is
  working_tree as reported by inspect. Historical Markdown reviews remain unmodified.
```
