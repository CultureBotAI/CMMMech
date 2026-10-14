# Independent scientific review of Nontronite round 74

- Review: 20261014T145850Z-nontronite-round74-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T14:51:33.233972Z
- Finished UTC: 2026-10-14T14:58:50.488467Z
- Reviewer: codex /root/round68_phosphates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nontronite identity and humic-assisted microbial iron reduction are supported. Sterile SI controls, mixed illite-like products, operational iron fractions and missing donor/assay-pH details remain explicit; no pure product or industrial result is inferred.

## Scope And Provenance

Entire frozen owner and linked CREATE history, mineral/taxon authorities, complete relevant primary methods/results/figures and available supplement, bounded notice/conflict search and validation.

Selection: Assigned independent review of both frozen clay owners; one record observation per owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a524756f3f4f90d81f89035fa7f85f1e1897b99d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:nontronite | data/records/nontronite.yaml | maintained | Nontronite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:nontronite | Actual reviewer execution 2026-10-14T14:53:28.977177+00:00 to 2026-10-14T14:53:33.508329+00:00; two records checked, zero failures. |
| Coordinator terminal batch gate | passed | True | cmmmech:nontronite | Independently verified terminal receipt, trusted base, zero exit codes and full log hash. Structural checks do not prove scientific truth. |
| Coordinator terminal batch gate | passed | True | cmmmech:nontronite | Independently verified terminal receipt, trusted base, zero exit codes and full log hash. Structural checks do not prove scientific truth. |
| Coordinator terminal batch gate | passed | True | cmmmech:nontronite | Independently verified terminal receipt, trusted base, zero exit codes and full log hash. Structural checks do not prove scientific truth. |

## Scientific And Domain Assessments

### Material identity, external identifiers and criticality

identity: supported. Targets: cmmmech:nontronite.

Current IMA and Handbook identity are correctly separated from experimental specimen heterogeneity and resource identity. No criticality list, jurisdiction or edition is asserted.

### Organism, biomass, substrate, preparation, conditions and controls

evidence: supported. Targets: cmmmech:nontronite.

Washed source-reported ATCC700550 MR-1 was added to 30mL deoxygenated10mM PIPES with0.03g size-separated NAu-2,3mg KCl and10–200mg/L humic acids in50mL bottles at30 C in darkness. Separate loading and sorbed/unbound humic-fraction arms were kept distinct. Main live no-HA comparisons and supplementary sterile controls have different roles.

### Measured outcomes and mechanistic uncertainty

evidence: supported. Targets: cmmmech:nontronite.

Iron(II) increases support biological reduction and humic stimulation. Total, dissolved and solid-associated iron are operational fractions rather than recovery yield. Ethylene-glycolated XRD and TEM/HRTEM support partial illite-like domains alongside remaining nontronite; EDX alone does not prove pure mineral identity. Sparse siderite-like fringes and proposed molecular explanations are qualified.

### Exact owner, history, evidence and required checks

provenance: supported. Targets: cmmmech:nontronite.

Native inspection preceded assessment; owner and canonical CREATE remain unchanged. Actual source hashes, reviewer named validation and terminal coordinator gates are retained. No review acceptance was inferred from curation alone.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/nontronite.yaml; Entire frozen owner captured by native inspect | supports | Whole owner assessed against original evidence without reviewer edits. |
| history | history/records/nontronite/2026-10-14T145017Z-codex-ebec97.yaml; Entire canonical CREATE, inline event and history_refs | supports | Actual actor, timestamps, target and change description agree; no fabricated earlier authorship. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Retained official original; definitions pp.1–2 and Nontronite row PDF p.157; row pixels inspected | supports | Na0.3Fe3+2(Si,Al)4O10(OH)2·nH2O, A,1962 s.p.; variable interlayer composition and NAu-2 specimen distinguished from ideal mineral. |
| handbook | https://www.handbookofmineralogy.org/pdfs/nontronite.pdf; Complete one-page original /private/tmp/cmm-round74-clays-research/nontronite-handbook.pdf; all pages visually inspected | supports | Monoclinic nontronite smectite identity and natural compositional variability corroborated. |
| primary | https://doi.org/10.1038/srep45354; Complete nine-page original /private/tmp/cmm-round74-clays-research/liu2017.pdf, whole text plus all Figures1–6; Methodspp7–8 | supports | NAu-2 and SWy-2 arms are distinct. Washed MR-1 in deoxygenated PIPES, supplied KCl, different humic acids/concentrations, no-HA live comparisons, iron assay fractions, electrochemical/sorption experiments and partial transformation were independently checked. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5371790/supplementaryFiles; Complete nineteen-page original /private/tmp/cmm-round74-clays-research/liu2017-si-acquired.pdf; TextS1, FiguresS1–S10, TablesS1–S5; all pages visually inspected | supports | Actual archive-extracted SI hash checked. FigureS5b explicitly contains sterile arms with and without HA, low Fe(II) relative to live systems, and dissolved/solid-associated partitions. FiguresS7–S10 support mixed illite-like domains; TableS4 undetectable Al is not zero and supplied KCl prevents an invented potassium mass balance. |
| limits | https://doi.org/10.1038/srep45354; Methodspp7–8; mainFigure6; SITextS1, FiguresS5/S7–S10, TableS4/S5 | partial | The inspected main and SI omit explicit reduction-assay donor and PIPES pH. Stock/model pH7 is not a replacement. No complete sterile phase-transformation series, refined phase fractions, pure illite/siderite product or isolated iron recovery follows. Molecular shuttling/complexation claims remain interpretations. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586; Official XML /private/tmp/cmm-round74-clays-research/ncbi-mr1.xml and live browser metadata | supports | Taxon211586 is Shewanella oneidensis MR-1 at strain rank; ATCC700550 synonym matches the primary report. Identity does not fill missing assay details. |
| search | /private/tmp/cmm-round74-clays-peer/independent-search.json; Four actual bounded DOI notice/conflict queries, with two additional exact Liu notice queries retained separately | context_only | Inspected returned results and publisher/PMC metadata did not identify an affecting formal notice; related primary studies were treated as leads, not imported mechanism evidence. |
| search_extra | /private/tmp/cmm-round74-clays-peer/independent-search-additional.json; Additional exact Liu notice queries and live NCBI browser routes | context_only | Original Nature/PMC/PubMed article metadata returned; no correction was identified in these returned sets. Taxon300 browser text was sparse, so the acquired authoritative XML is the identity evidence. |
| dedup | /private/tmp/cmm-round74-clays-peer/dedup.json; rg --no-ignore --hidden --follow across explicit current/main records/research/reviews/history and current source raw root | context_only | 533 matching lines include existing mixed resource records, prior leads and new owners. Mineral species are distinguished from kaolin resources and other clay species; no all-filesystem novelty assertion. |
| named | /private/tmp/cmm-round74-clays-peer/named-validation.json; Actual reviewer command/timestamps, exit0 and independently checked log hash | supports | Two exact frozen owners passed structural validation. |
| batch | /private/tmp/cmm-round74-final-gates.json; Terminal coordinator receipt independently read; trusted base, three command outcomes and complete log hash verified | supports | All required batch commands passed; log SHA256 51cd4800a68a40be1899a30a91be79c4d9e747bbedbbb4a56c3d63f54fbfda24. |

## Limits And Additional Notes

- The reduction-assay electron donor and PIPES pH are missing from the inspected original/SI and are not reconstructed from other studies.
- Sterile controls support the iron-reduction signal but do not provide a complete matched phase-transformation series.
- Transformation products are mixed; source-assigned illite domains and sparse siderite-like fringes do not establish pure products, complete conversion or phase-specific recovery.
- TableS4 lacks an explicit Al detection limit and suitable elemental potassium accounting; TextS1 is a model and TableS5 combines different experiments.
- Bounded correction/conflict searches do not establish exhaustive literature coverage; no raw-data reanalysis was performed.
- No supported corrective finding in this bounded scope. Reviewer did not edit either clay owner or history.
- Review start is the actual filesystem creation time of the first native inspect output. A second inspection added canonical history and schema hashes before final disposition; original owner hashes were verified unchanged.
- Source inventory: /private/tmp/cmm-round74-clays-peer/source-hashes.json. Main and supplement graphics were visually checked, not accepted from text extraction alone.
- Before persistence, review-only target metadata was normalized to maintained/CultureBotAI-CMMMech routing and the extra search evidence gained its required bounded scope. Scientific owner bytes were unchanged and re-inspected; earlier saver attempts produced no review bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T145850Z-nontronite-round74-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Nontronite round 74
started_at: '2026-10-14T14:51:33.233972Z'
finished_at: '2026-10-14T14:58:50.488467Z'
reviewer:
  identity: codex /root/round68_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The new_frontier peer authored the clay records, histories and
    dossier. Reviewer authored separate variscite/strengite records in this batch
    but did not author or edit the reviewed clay owners or histories. Native inspect
    preceded scientific assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Nontronite identity and humic-assisted microbial iron reduction are supported.
  Sterile SI controls, mixed illite-like products, operational iron fractions and
  missing donor/assay-pH details remain explicit; no pure product or industrial result
  is inferred.
source:
  git_revision: a524756f3f4f90d81f89035fa7f85f1e1897b99d
  state: working_tree
  inputs:
  - path: data/records/nontronite.yaml
    sha256: a946556b1dfd735b5c23e8aa7b4d320b82faa839b55c58dabb1c34523f344cde
    role: target
  - path: history/records/nontronite/2026-10-14T145017Z-codex-ebec97.yaml
    sha256: a85d5ba7918625f7cf6d5196000284c20af769921037b2abcbcff34dfbc71dd4
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen owner and linked CREATE history, mineral/taxon authorities,
    complete relevant primary methods/results/figures and available supplement, bounded
    notice/conflict search and validation.
  selection: Assigned independent review of both frozen clay owners; one record observation
    per owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:nontronite
targets:
- target_id: cmmmech:nontronite
  path: data/records/nontronite.yaml
  label: Nontronite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nontronite.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Reviewer named validation
  command: uv run --locked cmmmech validate data/records/kaolinite.yaml data/records/nontronite.yaml
    --require-records
  status: passed
  required: true
  summary: Actual reviewer execution 2026-10-14T14:53:28.977177+00:00 to 2026-10-14T14:53:33.508329+00:00;
    two records checked, zero failures.
  target_ids:
  - cmmmech:nontronite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Coordinator terminal batch gate
  command: just check
  status: passed
  required: true
  summary: Independently verified terminal receipt, trusted base, zero exit codes
    and full log hash. Structural checks do not prove scientific truth.
  target_ids:
  - cmmmech:nontronite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Coordinator terminal batch gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Independently verified terminal receipt, trusted base, zero exit codes
    and full log hash. Structural checks do not prove scientific truth.
  target_ids:
  - cmmmech:nontronite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Coordinator terminal batch gate
  command: uv run --locked cmmmech validate-history --base a524756f3f4f90d81f89035fa7f85f1e1897b99d
  status: passed
  required: true
  summary: Independently verified terminal receipt, trusted base, zero exit codes
    and full log hash. Structural checks do not prove scientific truth.
  target_ids:
  - cmmmech:nontronite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/nontronite.yaml
  locator: Entire frozen owner captured by native inspect
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Whole owner assessed against original evidence without reviewer edits.
  snapshot_sha256: a946556b1dfd735b5c23e8aa7b4d320b82faa839b55c58dabb1c34523f344cde
- evidence_id: history
  kind: record_content
  reference: history/records/nontronite/2026-10-14T145017Z-codex-ebec97.yaml
  locator: Entire canonical CREATE, inline event and history_refs
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Actual actor, timestamps, target and change description agree; no fabricated
    earlier authorship.
  snapshot_sha256: a85d5ba7918625f7cf6d5196000284c20af769921037b2abcbcff34dfbc71dd4
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Retained official original; definitions pp.1–2 and Nontronite row PDF p.157;
    row pixels inspected
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Na0.3Fe3+2(Si,Al)4O10(OH)2·nH2O, A,1962 s.p.; variable interlayer composition
    and NAu-2 specimen distinguished from ideal mineral.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/nontronite.pdf
  locator: Complete one-page original /private/tmp/cmm-round74-clays-research/nontronite-handbook.pdf;
    all pages visually inspected
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Monoclinic nontronite smectite identity and natural compositional variability
    corroborated.
  snapshot_sha256: 9256aaecb466989b78675ca127cc19f1b5343b067f16e6d7e53d70ec323db9b1
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1038/srep45354
  locator: Complete nine-page original /private/tmp/cmm-round74-clays-research/liu2017.pdf,
    whole text plus all Figures1–6; Methodspp7–8
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: NAu-2 and SWy-2 arms are distinct. Washed MR-1 in deoxygenated PIPES, supplied
    KCl, different humic acids/concentrations, no-HA live comparisons, iron assay
    fractions, electrochemical/sorption experiments and partial transformation were
    independently checked.
  snapshot_sha256: e400e983c37063a6f85d9ee6e3ae3861c5d0731e3299564e3c7933a691225286
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5371790/supplementaryFiles
  locator: Complete nineteen-page original /private/tmp/cmm-round74-clays-research/liu2017-si-acquired.pdf;
    TextS1, FiguresS1–S10, TablesS1–S5; all pages visually inspected
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Actual archive-extracted SI hash checked. FigureS5b explicitly contains
    sterile arms with and without HA, low Fe(II) relative to live systems, and dissolved/solid-associated
    partitions. FiguresS7–S10 support mixed illite-like domains; TableS4 undetectable
    Al is not zero and supplied KCl prevents an invented potassium mass balance.
  snapshot_sha256: c1fed5c32020eabd7ce7305229c76e05a29505fbbcfb13c0245d0c03ab19f74a
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1038/srep45354
  locator: Methodspp7–8; mainFigure6; SITextS1, FiguresS5/S7–S10, TableS4/S5
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: partial
  summary: The inspected main and SI omit explicit reduction-assay donor and PIPES
    pH. Stock/model pH7 is not a replacement. No complete sterile phase-transformation
    series, refined phase fractions, pure illite/siderite product or isolated iron
    recovery follows. Molecular shuttling/complexation claims remain interpretations.
  snapshot_sha256: e400e983c37063a6f85d9ee6e3ae3861c5d0731e3299564e3c7933a691225286
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586
  locator: Official XML /private/tmp/cmm-round74-clays-research/ncbi-mr1.xml and live
    browser metadata
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Taxon211586 is Shewanella oneidensis MR-1 at strain rank; ATCC700550 synonym
    matches the primary report. Identity does not fill missing assay details.
  snapshot_sha256: 242ace15df22ed93abda0ea977cee8da12577ddd18f60c98051af3c58f6c4de4
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round74-clays-peer/independent-search.json
  locator: Four actual bounded DOI notice/conflict queries, with two additional exact
    Liu notice queries retained separately
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: context_only
  summary: Inspected returned results and publisher/PMC metadata did not identify
    an affecting formal notice; related primary studies were treated as leads, not
    imported mechanism evidence.
  snapshot_sha256: ddaf515d56bb8fb210475082ee2ac6ee01aab8c4f05070dfb1f5b72a4f24b8de
  search_scope: Exact queries and outputs retained in independent-search.json and
    independent-search-additional.json; no exhaustive search or all-notices absence
    claim.
- evidence_id: search_extra
  kind: search
  reference: /private/tmp/cmm-round74-clays-peer/independent-search-additional.json
  locator: Additional exact Liu notice queries and live NCBI browser routes
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: context_only
  summary: Original Nature/PMC/PubMed article metadata returned; no correction was
    identified in these returned sets. Taxon300 browser text was sparse, so the acquired
    authoritative XML is the identity evidence.
  snapshot_sha256: 7ec2b058057dfcc0fc4a0be3d6bc470605f1c7fc5a73ed1f747280df26659a68
  search_scope: Two exact Liu DOI/title correction/retraction queries and two NCBI
    browser opens, first returned result sets only; no exhaustive notice search.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round74-clays-peer/dedup.json
  locator: rg --no-ignore --hidden --follow across explicit current/main records/research/reviews/history
    and current source raw root
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: context_only
  summary: 533 matching lines include existing mixed resource records, prior leads
    and new owners. Mineral species are distinguished from kaolin resources and other
    clay species; no all-filesystem novelty assertion.
  snapshot_sha256: fe2d67665fea20c8585a75ec9b5861276fd049086b48c9f3a1f5960bfae6f8f1
  search_scope: Explicit roots, text globs, command, exit0 and empty stderr retained;
    hidden/ignored files and relevant symlinks included.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round74-clays-peer/named-validation.json
  locator: Actual reviewer command/timestamps, exit0 and independently checked log
    hash
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: Two exact frozen owners passed structural validation.
  snapshot_sha256: e18dda5c136c3b3ea7485efa5756c6e5851cc594d92ecae1cefaf677cfaffcc3
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round74-final-gates.json
  locator: Terminal coordinator receipt independently read; trusted base, three command
    outcomes and complete log hash verified
  accessed_at: '2026-10-14T14:56:59.005577Z'
  support: supports
  summary: All required batch commands passed; log SHA256 51cd4800a68a40be1899a30a91be79c4d9e747bbedbbb4a56c3d63f54fbfda24.
  snapshot_sha256: 54fa72f75c13ce01a699c7b09f54e794c10d9cc6165d8bc93d4d08d37ccb7c35
assessments:
- assessment_id: identity
  area: identity
  topic: Material identity, external identifiers and criticality
  outcome: supported
  summary: Current IMA and Handbook identity are correctly separated from experimental
    specimen heterogeneity and resource identity. No criticality list, jurisdiction
    or edition is asserted.
  target_ids:
  - cmmmech:nontronite
  evidence_ids:
  - record
  - ima
  - handbook
  - taxon
  dimensions:
  - name: material_form
    value: Mineral species; source-characterized natural reference specimens
    definition: Ideal formula does not establish experimental purity.
    evidence_ids:
    - record
    - ima
    - handbook
    - primary
  - name: criticality
    value: No designation asserted
    definition: No inheritance from constituent element or related commodity.
    evidence_ids:
    - record
- assessment_id: methods
  area: evidence
  topic: Organism, biomass, substrate, preparation, conditions and controls
  outcome: supported
  summary: Washed source-reported ATCC700550 MR-1 was added to 30mL deoxygenated10mM
    PIPES with0.03g size-separated NAu-2,3mg KCl and10–200mg/L humic acids in50mL
    bottles at30 C in darkness. Separate loading and sorbed/unbound humic-fraction
    arms were kept distinct. Main live no-HA comparisons and supplementary sterile
    controls have different roles.
  target_ids:
  - cmmmech:nontronite
  evidence_ids:
  - record
  - primary
  - supplement
  - limits
  - taxon
  dimensions:
  - name: organism_and_biomass
    value: Living Shewanella oneidensis MR-1, NCBITaxon211586, source ATCC700550;
      no genome-level mechanism inferred.
    definition: Biological identity scope is limited to the experimentally reported
      culture.
    evidence_ids:
    - record
    - primary
    - supplement
    - limits
    - taxon
  - name: controls
    value: Main live cultures without HA; SI FigureS5b sterile ±HA comparisons for
      Fe(II). No complete sterile XRD/TEM series; missing donor and assay pH limit
      reproducibility.
    definition: Comparator scope constrains causal claims.
    evidence_ids:
    - record
    - primary
    - supplement
    - limits
    - taxon
  - name: deployment
    value: Laboratory assays only
    definition: No isolated product recovery or industrial deployment is established.
    evidence_ids:
    - record
    - primary
- assessment_id: outcomes
  area: evidence
  topic: Measured outcomes and mechanistic uncertainty
  outcome: supported
  summary: Iron(II) increases support biological reduction and humic stimulation.
    Total, dissolved and solid-associated iron are operational fractions rather than
    recovery yield. Ethylene-glycolated XRD and TEM/HRTEM support partial illite-like
    domains alongside remaining nontronite; EDX alone does not prove pure mineral
    identity. Sparse siderite-like fringes and proposed molecular explanations are
    qualified.
  target_ids:
  - cmmmech:nontronite
  evidence_ids:
  - record
  - primary
  - supplement
  - limits
  - taxon
- assessment_id: provenance
  area: provenance
  topic: Exact owner, history, evidence and required checks
  outcome: supported
  summary: Native inspection preceded assessment; owner and canonical CREATE remain
    unchanged. Actual source hashes, reviewer named validation and terminal coordinator
    gates are retained. No review acceptance was inferred from curation alone.
  target_ids:
  - cmmmech:nontronite
  evidence_ids:
  - record
  - history
  - named
  - batch
  - search
  - search_extra
  - dedup
findings: []
actions: []
limitations:
- The reduction-assay electron donor and PIPES pH are missing from the inspected original/SI
  and are not reconstructed from other studies.
- Sterile controls support the iron-reduction signal but do not provide a complete
  matched phase-transformation series.
- Transformation products are mixed; source-assigned illite domains and sparse siderite-like
  fringes do not establish pure products, complete conversion or phase-specific recovery.
- TableS4 lacks an explicit Al detection limit and suitable elemental potassium accounting;
  TextS1 is a model and TableS5 combines different experiments.
- Bounded correction/conflict searches do not establish exhaustive literature coverage;
  no raw-data reanalysis was performed.
notes:
- No supported corrective finding in this bounded scope. Reviewer did not edit either
  clay owner or history.
- Review start is the actual filesystem creation time of the first native inspect
  output. A second inspection added canonical history and schema hashes before final
  disposition; original owner hashes were verified unchanged.
- 'Source inventory: /private/tmp/cmm-round74-clays-peer/source-hashes.json. Main
  and supplement graphics were visually checked, not accepted from text extraction
  alone.'
- Before persistence, review-only target metadata was normalized to maintained/CultureBotAI-CMMMech
  routing and the extra search evidence gained its required bounded scope. Scientific
  owner bytes were unchanged and re-inspected; earlier saver attempts produced no
  review bundle.
tags:
- round74
- nontronite
- independent
- primary-figures
- qualified-microbial
```
