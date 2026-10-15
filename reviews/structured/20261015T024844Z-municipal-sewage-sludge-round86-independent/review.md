# Independent scientific review of municipal sewage sludge

- Review: 20261015T024844Z-municipal-sewage-sludge-round86-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T02:34:43.116932Z
- Finished UTC: 2026-10-15T02:48:44.778878Z
- Reviewer: codex /root/round68_phosphates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of unincinerated municipal sewage sludge as a distinct resource, with culture-associated phosphorus solubilization and indigenous iron-oxidizer metal leaching in two laboratory studies. Source-input accounting, nonsterile controls, uneven metal outcomes and the separate chemical peroxide extension are explicitly bounded.

## Scope And Provenance

Whole exact maintained owner and canonical CREATE, with accepted primary and identity evidence specified per locator.

Selection: Assigned canonical target; native inspect completed before record-level judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a579d90978267cf5d145bca05b4c97e5ba4d629.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:municipal-sewage-sludge | data/records/municipal-sewage-sludge.yaml | maintained | Municipal sewage sludge |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:municipal-sewage-sludge | Actual two records checked, zero failures; retained receipt and log independently verified. |
| Completed coordinator batch gate 1 | passed | True | cmmmech:municipal-sewage-sludge | Actual terminal coordinator receipt and log verified; not a claim that this reviewer reran the batch. |
| Completed coordinator batch gate 2 | passed | True | cmmmech:municipal-sewage-sludge | Actual terminal coordinator receipt and log verified; not a claim that this reviewer reran the batch. |
| Completed coordinator batch gate 3 | passed | True | cmmmech:municipal-sewage-sludge | Actual terminal coordinator receipt and log verified; not a claim that this reviewer reran the batch. |
| Completed coordinator batch gate 4 | passed | True | cmmmech:municipal-sewage-sludge | Actual terminal coordinator receipt and log verified; not a claim that this reviewer reran the batch. |

## Scientific And Domain Assessments

### Resource and organism boundaries

identity: supported. Targets: cmmmech:municipal-sewage-sludge.

Unincinerated municipal sludge is distinct from incineration ash, untreated wastewater and industrial-specific sludge. Kuopio and Tianjin feeds are distinct examples, not a standardized universal feed. DSM catalogue identities and species-only NCBI identifiers agree; indigenous controls and the unresolved second enrichment are not assigned to those strains.

### Sequential sulfur-assisted sludge treatment

evidence: supported. Targets: cmmmech:municipal-sewage-sludge.

Pradhan10mLsludge/90mLmedium-or-culture in250mLbottles at30°C150rpm ran three21-day phases, replacing10mL at21/42days and adding nominal10g/L80%-pure sulfur at42days. Control sludge was not sterile and indigenous acidithiobacilli grew. Figure/table evidence supports the culture-associated observation without proving individual-strain causality.

### Reported phosphorus percentage and source accounting

quantity: supported. Targets: cmmmech:municipal-sewage-sludge.

Table5 reports92% atpH0.9 for T+S versus27%TC+S and10%F+S, after precedingT10/5% phases. Media introduce phosphate/metals and no complete input/replacement/sampling correction is supplied. The record correctly does not adopt92% as a verified sludge-origin or isolated-product yield. Figure1/Table5 pH conflicts and Table6 values above100% remain explicit.

### Indigenous enrichment and separate chemical stage

evidence: supported. Targets: cmmmech:municipal-sewage-sludge.

Qiu4%solids,300mLsludge,5%v/vlivinginoculum,4g/LFe2+,28°C150rpm and10days are reported. Zn67.28/Ni49.83% versusCr6.32% and weakAs/Pb prevent uniform-extraction claims. H2O2 arms are a separate chemical extension; they can reduceAs/Pb removal. No matched sterile Fe-fed or acidity control, recovered product or demonstrated industrial process is supplied.

### Operational fractions and conflicting optimum labels

evidence: supported. Targets: cmmmech:municipal-sewage-sludge.

BCR fractions are operational extractions; FeAsO4/PbSO4 and radical pathways are hypotheses. Ni65.81/65.19 and Cu peroxide-dose inconsistencies are retained without selecting an exact combined optimum. Prior-work-dependent enrichment/sample preparation, incompletely reported chemical-contact details, uncertain upstream feed histories and unclosed solution balance limit transfer.

### Study lineage and outcome boundary

scope: supported. Targets: cmmmech:municipal-sewage-sludge.

The two different2021 studies support separate laboratory mechanisms for heterogeneous feeds. Culture-associated solubilization is not isolated phosphorus recovery; peroxide chemistry is not microbial oxidation. No universal detoxification, safe fertilizer product, industrial operation or criticality designation is asserted.

### Exact records, canonical history and actual gates

provenance: supported. Targets: cmmmech:municipal-sewage-sludge.

Inspect-first capture binds unchanged owner and canonical CREATE. Separate inline history and sidecar attribution agree with the actual curation. Each accepted primary/authority/database row binds exact nonempty local bytes and SHA256. Named and four completed batch gates passed; no owner/history edit by this reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/municipal-sewage-sludge.yaml; Whole exact maintained owner after native inspection. Artifact: /private/tmp/CMMMech-expansion-round86-20261015/data/records/municipal-sewage-sludge.yaml | supports | All curated identity, conditions, outcomes, limitations and references reviewed. |
| history | history/records/municipal-sewage-sludge/2026-10-15T022845Z-codex-ebd103.yaml; Canonical CREATE sidecar, history_refs and separate inline CREATE event. Artifact: /private/tmp/CMMMech-expansion-round86-20261015/history/records/municipal-sewage-sludge/2026-10-15T022845Z-codex-ebd103.yaml | supports | Actual codex/GPT-6 attribution, target, timestamps and change description agree. These are distinct recorded events; no claim their timestamps must be identical. |
| pradhan | https://doi.org/10.3390/ijerph18137135; Complete13-page original acquired; Methods2.1–2.7, Results3.1–3.3 and conclusion independently read. All Figures1–2 and Tables1–6, including Table6 continuation onPDF11, visually checked. Table5 reported92% denominator and Figure1/Table5 pH inconsistency scrutinized. Artifact: /private/tmp/cmm-round86-resources-research/pradhan2021.pdf | supports | Supports the qualified sequential culture-associated solubilization observation, with source-accounting and nonsterile-control limits. |
| qiu | https://doi.org/10.1038/s41598-021-94216-2; Complete12-page original acquired and claim-bearing methods/results/discussion read; MethodsPDF2–3, all Figures1–6 and Table1 independently visually checked. Figure1 time series, Figure3 unequal removal and Figures4–6 chemical extension/BCR fractions inspected. Artifact: /private/tmp/cmm-round86-resources-research/qiu2021.pdf | supports | Supports unequal elemental mobilization, a separate peroxide stage and operational fractionation; not direct mineral or oxidation-state identification. |
| dsm29444 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-29444; Complete retained catalogue identity fields read and current catalogue independently opened. Artifact: /private/tmp/cmm-round86-resources-research/dsm29444.html | context_only | DSM29444 is A.ferrooxidans strainR1. Catalogue cultivation temperature does not replace the study assay. |
| dsm14887 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-14887; Complete retained catalogue identity fields read and current catalogue independently opened. Artifact: /private/tmp/cmm-round86-resources-research/dsm14887.html | context_only | DSM14887 is A.thiooxidans strain3/TA, equivalent ATCC19377/NCIMB8343/JCM3867; this does not resolve its contribution in nonsterile sludge. |
| ncbi | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=920,930&amp;retmode=xml; Exact TaxId920 and930 Taxon elements and ranks independently parsed/read. Artifact: /private/tmp/cmm-round86-resources-research/ncbi920-930.xml | context_only | A.ferrooxidans and A.thiooxidans species identifiers match; neither is a strain or an identifier for the unresolved Tianjin enrichment. |
| dedup | /private/tmp/cmm-round86-minerals-research/peer-dedup.json; Actual hidden/ignored-inclusive, followed-symlink rg command, roots and61 matching paths retained. Artifact: /private/tmp/cmm-round86-minerals-research/peer-dedup.json | context_only | Distinct current canonical owners; contextual reuse is not an independent study or duplicate resource owner. |
| notices | /private/tmp/cmm-round86-minerals-research/peer-search-assessment.json; Actual seven query strings, retained responses, metadata hashes, catalogue checks and publisher access limitations. Artifact: /private/tmp/cmm-round86-minerals-research/peer-search-assessment.json | context_only | No matching formal corrective notice surfaced in bounded returned sets; absence is not proved. Different-treatment primary leads were not imported as equivalent replications. |
| named | /private/tmp/cmm-round86-minerals-research/peer-named-validation.json; Actual independent check 2026-10-15T02:39:16.264224+00:00 to 2026-10-15T02:39:21.130520+00:00; log /private/tmp/cmm-round86-minerals-research/peer-named-validation.log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042. Artifact: /private/tmp/cmm-round86-minerals-research/peer-named-validation.json | supports | Two named records checked, zero failures. |
| batch | /private/tmp/cmm-round86-final-gates.json; All FOUR coordinator commands 2026-10-15T02:38:30.480480+00:00 to 2026-10-15T02:47:49.096395+00:00; log /private/tmp/cmm-round86-final-gates.log SHA256 b2ced490afd5c19f314cc545a9c33d806424d96397e41f6cdf10e95eb099429c. Artifact: /private/tmp/cmm-round86-final-gates.json | supports | Actual terminal exits, trusted base/worktree and unchanged owner inputs independently verified. |

## Limits And Additional Notes

- Added cultures are not distinguished from native sludge organisms by strain tracking, and comparators are not sterile sludge; unique microbial causal attribution is limited.
- Medium phosphate/metals, sequential replacement and sampling are not fully reconciled; reported extraction percentages are not verified sludge-origin or isolated-product recoveries.
- The Tianjin enrichment lacks an identified species/strain; peroxide treatment is chemical and its full contact protocol/earlier-method dependencies are not completely reproduced in the accepted article.
- BCR fractions and proposed precipitates do not demonstrate mineral phases or valence changes. Inconsistent pH, dose and metal endpoints remain unresolved.
- No separate supplement is announced in inspected original PDFs or the inspected Pradhan JATS. MDPI landing429 and Nature identity-provider redirect500 limit live supplement/notice inventory; full accepted originals remain available.
- Bounded correction/counterevidence screening is not a global completeness claim. Structural checks do not establish scientific truth or replace laboratory replication.
- No owner or history changes by this reviewer; no finding disposition is silently changed.
- All accepted source and authority/database evidence has an exact nonempty local artifact and SHA256. Source uncertainties remain limitations, not fabricated corrective findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T024844Z-municipal-sewage-sludge-round86-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of municipal sewage sludge
started_at: '2026-10-15T02:34:43.116932Z'
finished_at: '2026-10-15T02:48:44.778878Z'
reviewer:
  identity: codex /root/round68_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer authored willemite and hemimorphite, not this target
    or its history. Heterogenite curator is round68_iron_sulfides; municipal sludge
    curator is round68_new_frontier. Shared acquisition is disclosed; original claim-bearing
    text/graphics and authority/database identities were independently checked. Native
    inspect completed before record-level judgment; preliminary source/owner reading
    also occurred during capture preparation. No laboratory replication.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified acceptance of unincinerated municipal sewage sludge as a distinct
  resource, with culture-associated phosphorus solubilization and indigenous iron-oxidizer
  metal leaching in two laboratory studies. Source-input accounting, nonsterile controls,
  uneven metal outcomes and the separate chemical peroxide extension are explicitly
  bounded.
source:
  git_revision: 6a579d90978267cf5d145bca05b4c97e5ba4d629
  state: working_tree
  inputs:
  - path: data/records/municipal-sewage-sludge.yaml
    sha256: 7ba8cdbe6caff95bc497768d59d0da0004241b11759deb171cfaffa19748be44
    role: target
  - path: history/records/municipal-sewage-sludge/2026-10-15T022845Z-codex-ebd103.yaml
    sha256: 13bf4f09c24d5448dcd7d0bbbfe95492d95fcbcde7e6531cce7ffb8b43f5c5bc
    role: context
scope:
  description: Whole exact maintained owner and canonical CREATE, with accepted primary
    and identity evidence specified per locator.
  selection: Assigned canonical target; native inspect completed before record-level
    judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:municipal-sewage-sludge
targets:
- target_id: cmmmech:municipal-sewage-sludge
  path: data/records/municipal-sewage-sludge.yaml
  label: Municipal sewage sludge
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/municipal-sewage-sludge.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate data/records/heterogenite.yaml data/records/municipal-sewage-sludge.yaml
    --require-records
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual two records checked, zero failures; retained receipt and log independently
    verified.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - named
- check_id: batch1
  name: Completed coordinator batch gate 1
  command: just check
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal coordinator receipt and log verified; not a claim that
    this reviewer reran the batch.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed coordinator batch gate 2
  command: uv run --locked cmmmech validate --require-records
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal coordinator receipt and log verified; not a claim that
    this reviewer reran the batch.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed coordinator batch gate 3
  command: uv run --locked cmmmech validate-history --base 6a579d90978267cf5d145bca05b4c97e5ba4d629
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal coordinator receipt and log verified; not a claim that
    this reviewer reran the batch.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed coordinator batch gate 4
  command: uv run --locked python scripts/render_pages.py --check
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Actual terminal coordinator receipt and log verified; not a claim that
    this reviewer reran the batch.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/municipal-sewage-sludge.yaml
  locator: 'Whole exact maintained owner after native inspection. Artifact: /private/tmp/CMMMech-expansion-round86-20261015/data/records/municipal-sewage-sludge.yaml'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: All curated identity, conditions, outcomes, limitations and references
    reviewed.
  snapshot_sha256: 7ba8cdbe6caff95bc497768d59d0da0004241b11759deb171cfaffa19748be44
- evidence_id: history
  kind: record_content
  reference: history/records/municipal-sewage-sludge/2026-10-15T022845Z-codex-ebd103.yaml
  locator: 'Canonical CREATE sidecar, history_refs and separate inline CREATE event.
    Artifact: /private/tmp/CMMMech-expansion-round86-20261015/history/records/municipal-sewage-sludge/2026-10-15T022845Z-codex-ebd103.yaml'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: Actual codex/GPT-6 attribution, target, timestamps and change description
    agree. These are distinct recorded events; no claim their timestamps must be identical.
  snapshot_sha256: 13bf4f09c24d5448dcd7d0bbbfe95492d95fcbcde7e6531cce7ffb8b43f5c5bc
- evidence_id: pradhan
  kind: primary_source
  reference: https://doi.org/10.3390/ijerph18137135
  locator: 'Complete13-page original acquired; Methods2.1–2.7, Results3.1–3.3 and
    conclusion independently read. All Figures1–2 and Tables1–6, including Table6
    continuation onPDF11, visually checked. Table5 reported92% denominator and Figure1/Table5
    pH inconsistency scrutinized. Artifact: /private/tmp/cmm-round86-resources-research/pradhan2021.pdf'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: Supports the qualified sequential culture-associated solubilization observation,
    with source-accounting and nonsterile-control limits.
  snapshot_sha256: 814f0989066848ac230444a798bf5180cf3788a950e449228013e9e84a7e2a11
- evidence_id: qiu
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-021-94216-2
  locator: 'Complete12-page original acquired and claim-bearing methods/results/discussion
    read; MethodsPDF2–3, all Figures1–6 and Table1 independently visually checked.
    Figure1 time series, Figure3 unequal removal and Figures4–6 chemical extension/BCR
    fractions inspected. Artifact: /private/tmp/cmm-round86-resources-research/qiu2021.pdf'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: Supports unequal elemental mobilization, a separate peroxide stage and
    operational fractionation; not direct mineral or oxidation-state identification.
  snapshot_sha256: 9dff58964c80e18866a70e06e1fa5719986de4724e0a536014fe54a72f8629d0
- evidence_id: dsm29444
  kind: database
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-29444
  locator: 'Complete retained catalogue identity fields read and current catalogue
    independently opened. Artifact: /private/tmp/cmm-round86-resources-research/dsm29444.html'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: context_only
  summary: DSM29444 is A.ferrooxidans strainR1. Catalogue cultivation temperature
    does not replace the study assay.
  snapshot_sha256: af08148e66bef402e17ef23f0e282db9246541f2a95270e7ab4aa79e542d070f
- evidence_id: dsm14887
  kind: database
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-14887
  locator: 'Complete retained catalogue identity fields read and current catalogue
    independently opened. Artifact: /private/tmp/cmm-round86-resources-research/dsm14887.html'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: context_only
  summary: DSM14887 is A.thiooxidans strain3/TA, equivalent ATCC19377/NCIMB8343/JCM3867;
    this does not resolve its contribution in nonsterile sludge.
  snapshot_sha256: 313f679a6ceeb3ca36be9bf576a9be39029674461dddc0bee8afe73be8284732
- evidence_id: ncbi
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=920,930&retmode=xml
  locator: 'Exact TaxId920 and930 Taxon elements and ranks independently parsed/read.
    Artifact: /private/tmp/cmm-round86-resources-research/ncbi920-930.xml'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: context_only
  summary: A.ferrooxidans and A.thiooxidans species identifiers match; neither is
    a strain or an identifier for the unresolved Tianjin enrichment.
  snapshot_sha256: 937e9fadaef05e41fcf82b0a01e4f89cc8ccf9f2053dce482115b22be4894389
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round86-minerals-research/peer-dedup.json
  locator: 'Actual hidden/ignored-inclusive, followed-symlink rg command, roots and61
    matching paths retained. Artifact: /private/tmp/cmm-round86-minerals-research/peer-dedup.json'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: context_only
  summary: Distinct current canonical owners; contextual reuse is not an independent
    study or duplicate resource owner.
  snapshot_sha256: 17dc4de739efd0cb85c7b7722660c441f87e7266640db23bb78bff44821b231f
  search_scope: Current worktree and original main records/research/reviews/history
    plus both assigned peer raw roots and this reviewer raw root. Bounded retained-text
    search; original PDFs separately inspected.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round86-minerals-research/peer-search-assessment.json
  locator: 'Actual seven query strings, retained responses, metadata hashes, catalogue
    checks and publisher access limitations. Artifact: /private/tmp/cmm-round86-minerals-research/peer-search-assessment.json'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: context_only
  summary: No matching formal corrective notice surfaced in bounded returned sets;
    absence is not proved. Different-treatment primary leads were not imported as
    equivalent replications.
  snapshot_sha256: b29e771fe149f54b6359587363549caf072cf801b3b28d15f126632299276a6a
  search_scope: 2026-10-15 exact title/DOI correction queries and related mechanism
    queries; first returned result sets, no exhaustive pagination; retained Crossref
    update/relation fields.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round86-minerals-research/peer-named-validation.json
  locator: 'Actual independent check 2026-10-15T02:39:16.264224+00:00 to 2026-10-15T02:39:21.130520+00:00;
    log /private/tmp/cmm-round86-minerals-research/peer-named-validation.log SHA256
    4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042. Artifact: /private/tmp/cmm-round86-minerals-research/peer-named-validation.json'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: Two named records checked, zero failures.
  snapshot_sha256: 57a4da2cc30bfb97d348ca651ccccb97a3dec9a6e25e59f891839ad5fad15578
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round86-final-gates.json
  locator: 'All FOUR coordinator commands 2026-10-15T02:38:30.480480+00:00 to 2026-10-15T02:47:49.096395+00:00;
    log /private/tmp/cmm-round86-final-gates.log SHA256 b2ced490afd5c19f314cc545a9c33d806424d96397e41f6cdf10e95eb099429c.
    Artifact: /private/tmp/cmm-round86-final-gates.json'
  accessed_at: '2026-10-15T02:48:44.778878Z'
  support: supports
  summary: Actual terminal exits, trusted base/worktree and unchanged owner inputs
    independently verified.
  snapshot_sha256: 3ec871c723db50601e97218a1ae032d225aabe4336f6eabc626b85aa0e87bd00
assessments:
- assessment_id: identity
  area: identity
  topic: Resource and organism boundaries
  outcome: supported
  summary: Unincinerated municipal sludge is distinct from incineration ash, untreated
    wastewater and industrial-specific sludge. Kuopio and Tianjin feeds are distinct
    examples, not a standardized universal feed. DSM catalogue identities and species-only
    NCBI identifiers agree; indigenous controls and the unresolved second enrichment
    are not assigned to those strains.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - pradhan
  - qiu
  - dsm29444
  - dsm14887
  - ncbi
- assessment_id: conditions
  area: evidence
  topic: Sequential sulfur-assisted sludge treatment
  outcome: supported
  summary: Pradhan10mLsludge/90mLmedium-or-culture in250mLbottles at30°C150rpm ran
    three21-day phases, replacing10mL at21/42days and adding nominal10g/L80%-pure
    sulfur at42days. Control sludge was not sterile and indigenous acidithiobacilli
    grew. Figure/table evidence supports the culture-associated observation without
    proving individual-strain causality.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - pradhan
- assessment_id: phosphorus
  area: quantity
  topic: Reported phosphorus percentage and source accounting
  outcome: supported
  summary: Table5 reports92% atpH0.9 for T+S versus27%TC+S and10%F+S, after precedingT10/5%
    phases. Media introduce phosphate/metals and no complete input/replacement/sampling
    correction is supplied. The record correctly does not adopt92% as a verified sludge-origin
    or isolated-product yield. Figure1/Table5 pH conflicts and Table6 values above100%
    remain explicit.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - pradhan
- assessment_id: metal
  area: evidence
  topic: Indigenous enrichment and separate chemical stage
  outcome: supported
  summary: Qiu4%solids,300mLsludge,5%v/vlivinginoculum,4g/LFe2+,28°C150rpm and10days
    are reported. Zn67.28/Ni49.83% versusCr6.32% and weakAs/Pb prevent uniform-extraction
    claims. H2O2 arms are a separate chemical extension; they can reduceAs/Pb removal.
    No matched sterile Fe-fed or acidity control, recovered product or demonstrated
    industrial process is supplied.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - qiu
- assessment_id: uncertainty
  area: evidence
  topic: Operational fractions and conflicting optimum labels
  outcome: supported
  summary: BCR fractions are operational extractions; FeAsO4/PbSO4 and radical pathways
    are hypotheses. Ni65.81/65.19 and Cu peroxide-dose inconsistencies are retained
    without selecting an exact combined optimum. Prior-work-dependent enrichment/sample
    preparation, incompletely reported chemical-contact details, uncertain upstream
    feed histories and unclosed solution balance limit transfer.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - pradhan
  - qiu
- assessment_id: scope
  area: scope
  topic: Study lineage and outcome boundary
  outcome: supported
  summary: The two different2021 studies support separate laboratory mechanisms for
    heterogeneous feeds. Culture-associated solubilization is not isolated phosphorus
    recovery; peroxide chemistry is not microbial oxidation. No universal detoxification,
    safe fertilizer product, industrial operation or criticality designation is asserted.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - pradhan
  - qiu
- assessment_id: provenance
  area: provenance
  topic: Exact records, canonical history and actual gates
  outcome: supported
  summary: Inspect-first capture binds unchanged owner and canonical CREATE. Separate
    inline history and sidecar attribution agree with the actual curation. Each accepted
    primary/authority/database row binds exact nonempty local bytes and SHA256. Named
    and four completed batch gates passed; no owner/history edit by this reviewer.
  target_ids:
  - cmmmech:municipal-sewage-sludge
  evidence_ids:
  - owner
  - history
  - named
  - batch
  - dedup
  - notices
findings: []
actions: []
limitations:
- Added cultures are not distinguished from native sludge organisms by strain tracking,
  and comparators are not sterile sludge; unique microbial causal attribution is limited.
- Medium phosphate/metals, sequential replacement and sampling are not fully reconciled;
  reported extraction percentages are not verified sludge-origin or isolated-product
  recoveries.
- The Tianjin enrichment lacks an identified species/strain; peroxide treatment is
  chemical and its full contact protocol/earlier-method dependencies are not completely
  reproduced in the accepted article.
- BCR fractions and proposed precipitates do not demonstrate mineral phases or valence
  changes. Inconsistent pH, dose and metal endpoints remain unresolved.
- No separate supplement is announced in inspected original PDFs or the inspected
  Pradhan JATS. MDPI landing429 and Nature identity-provider redirect500 limit live
  supplement/notice inventory; full accepted originals remain available.
- Bounded correction/counterevidence screening is not a global completeness claim.
  Structural checks do not establish scientific truth or replace laboratory replication.
notes:
- No owner or history changes by this reviewer; no finding disposition is silently
  changed.
- All accepted source and authority/database evidence has an exact nonempty local
  artifact and SHA256. Source uncertainties remain limitations, not fabricated corrective
  findings.
```
