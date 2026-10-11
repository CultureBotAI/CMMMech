# Independent scientific review of coal-mine-drainage treatment solids

- Review: 20261011T142727Z-coal-mine-drainage-treatment-solids-round24-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T14:24:05.493107Z
- Finished UTC: 2026-10-11T14:27:27.005646Z
- Reviewer: Codex /root/round24_copper_slag (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No actionable finding in the reviewed state. Treatment-origin identity and bounded culture-associated REE mobilization are supported; control counterexamples, missing assay metadata and unresolved source accounting remain explicit.

## Scope And Provenance

Entire maintained record, its identity and scientific claims, all cited sources and attached curation provenance.

Selection: One assigned newly curated treatment-solids record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d7183efeb2e528d6d88f0b69da41323642b8fa85.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:coal-mine-drainage-treatment-solids | data/records/coal-mine-drainage-treatment-solids.yaml | maintained | Coal mine drainage treatment solids |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:coal-mine-drainage-treatment-solids | Checked 1 record(s); 0 failed. |
| Native full checks | passed | True | cmmmech:coal-mine-drainage-treatment-solids | Parent executed current batch gate; reviewer inspected terminal receipt and actual log. /private/tmp/cmm-round24-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 89.10s (0:01:29)<br>Checked 160 record(s); 0 failed.<br>Checked 181 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:coal-mine-drainage-treatment-solids | Parent executed current batch gate; reviewer inspected terminal receipt and actual log. /private/tmp/cmm-round24-final-require.log: Checked 160 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:coal-mine-drainage-treatment-solids | Parent executed current batch gate; reviewer inspected terminal receipt and actual log. /private/tmp/cmm-round24-final-history.log: Checked 181 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Treatment-origin secondary resource and feed boundaries

identity: supported. Targets: cmmmech:coal-mine-drainage-treatment-solids.

The five passive coal-mine-drainage treatment feeds form one process-defined resource distinct from untreated water, ash, ore and individual minerals; composition and criticality are not generalized.

### Qualified acidogenic culture association with REE mobilization

evidence: supported. Targets: cmmmech:coal-mine-drainage-treatment-solids.

The selected culture-associated concentration comparisons are supported by the complete supplement. Negative comparisons, unreported conditions and source mass-balance inconsistencies prevent causal or recovery overstatement.

### Actual CREATE provenance and independent exact-state assessment

provenance: supported. Targets: cmmmech:coal-mine-drainage-treatment-solids.

The author differs from the reviewer. Canonical inspection preceded assessment, final input hashes remain current, and distinct inline/sidecar histories describe actual curation. No record changes were made by the reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/coal-mine-drainage-treatment-solids.yaml; Entire frozen scientific record and attached actual CREATE sidecar | supports | Independently read after canonical inspection. The resource has treatment origin and explicitly scoped laboratory culture-associated mobilization; no material CURIE, criticality or isolated-product claim is invented. |
| primary | https://doi.org/10.3390/min16090930; Methods 2.1-2.5, Results 3.1-3.6, Discussion and data statement; Figures 1-7 visually checked on main PDF pages 3, 5, 7-10 and 12 | supports | Read complete relevant primary text independently from the same acquired source used by the curator. Preparation and 1% w/v, three-day, 30 degrees C assay are supported. Decanted supernatant processing, final pH, REE replication, inoculum dose and working volume are unspecified; separate Mn and SEM methods do not fill these gaps. Lactate production, annotations, staining and SEM are associations rather than causal interventions. Figure 3 is normalized by element column, and Figure 7 is a proposed schematic. The less-than-1% extraction claim lacks reconciled mass accounting and is appropriately not adopted. |
| supplement | https://mdpi-res.com/d_attachment/minerals/minerals-16-00930/article_deploy/minerals-16-00930-s001.zip; Complete four-page minerals-4280163-supplementary.pdf; Figures S1-S2 and Tables S1-S2, all visually inspected | supports | Checked all 15 curated JR07/KB7/sterile TREE values against Table S1 and verified row-to-feed/isolate key. Kentucky Hollow sterile 228.08 ppb remains visible; Wingfield Pines JR07 0.82 ppb is below sterile 1.59 ppb. Missing AV22/AV24 rows are not zero outcomes. BDL analytes and absent Pm column are explicit; TREE is source-reported with an unstated summation convention. Mn n=3 and HPLC n=3 are separate assays, while Table S2 genome metrics do not establish strain accessions or gene necessity. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1405&amp;mode=info; Live NCBI species pages 1405 and 64104 on 2026-10-11 | supports | Bacillus mycoides and Bacillus pseudomycoides names correspond to the record species identifiers. These species pages do not independently identify isolates JR07/KB7, prove study-stock identity or supply unreported genome accessions. |
| search | https://www.mdpi.com/2075-163X/16/9/930; Exact DOI/title publication and correction searches plus bounded repository dedup | context_only | Queries "10.3390/min16090930" correction OR retraction OR erratum and "Bioleaching Rare Earth Elements from Abandoned Coal Mine Drainage" returned matching bibliographic metadata without a matching correction notice in the inspected first sets. Direct publisher open was unavailable, but full publisher-CDN PDF and supplement provenance were independently inspected. No exhaustive absence assertion. |
| gates | /private/tmp/cmm-round24-gate-receipts.json; Current batch terminal receipts, actual logs, frozen target hashes and named validation | supports | Root executed the current full batch, nonempty corpus and trusted-base history gates. Reviewer independently ran named validation and read root receipts/logs, confirming the reviewed target and input bytes remain unchanged. These checks establish structural/provenance validity, not scientific truth. |

## Limits And Additional Notes

- REE-assay final pH, oxygen conditions, inoculum amount, working volume and replicate/uncertainty metadata remain unspecified.
- Unreported filtration and digestion leave the analytical fraction broader than proven dissolved ions; no phase-specific flux or product mass balance is established.
- No matched-acid or pathway intervention establishes lactate, genes or biofilms as necessary causes.
- TREE totals, absent Pm column, censored individual analytes and less-than-1% extraction accounting retain the source limitations; no repaired measurements are asserted.
- Bounded correction and dedup searches do not prove global absence of notices, sources or duplicate concepts outside the stated boundary.
- All required gate commands were executed for the current batch; shared batch gates were run by the parent and independently inspected by this reviewer.
- Primary and supplement PDFs were reused from this batch curator acquisition, not falsely represented as an independent redownload.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T142727Z-coal-mine-drainage-treatment-solids-round24-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of coal-mine-drainage treatment solids
started_at: '2026-10-11T14:24:05.493107Z'
finished_at: '2026-10-11T14:27:27.005646Z'
reviewer:
  identity: Codex /root/round24_copper_slag
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Agent /root/round24_identity_frontier authored the record. This
    reviewer independently inspected primary text, every relevant figure/table, taxonomy
    and exact frozen bytes without editing the record. Shared worktree, curator dossier
    and same acquired source PDFs are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: No actionable finding in the reviewed state. Treatment-origin identity and
  bounded culture-associated REE mobilization are supported; control counterexamples,
  missing assay metadata and unresolved source accounting remain explicit.
source:
  git_revision: d7183efeb2e528d6d88f0b69da41323642b8fa85
  state: working_tree
  inputs:
  - path: data/records/coal-mine-drainage-treatment-solids.yaml
    sha256: 9fce0c00b764999d6dd324311b30ec492d3b8cd9e3ff869f618e587d06e0baa9
    role: target
  - path: history/records/coal-mine-drainage-treatment-solids/2026-10-11T142246Z-codex-f53e30.yaml
    sha256: 5a2f6080b948adc92b202869dfb22ef83b2faefc2e8d2031ace44226f1a0f01a
    role: context
  - path: research/ingests/round24-amd-solids-sources-20261011.json
    sha256: 807a1e90cce377bdb73602386b2aad63cddcfe66570c32b6dbce86f4d9d50809
    role: context
  - path: research/ingests/round24-amd-solids-sources-20261011.md
    sha256: d67ce3f9167318726721126997a9708eb20641d0c8b2cebba1206919f849094b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire maintained record, its identity and scientific claims, all cited
    sources and attached curation provenance.
  selection: One assigned newly curated treatment-solids record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
  exclusions:
  - target: Unreported raw analytical replicates and inaccessible or undisclosed genome
      accessions
    reason: Article and supplement were complete; no underlying data were requested
      from authors or invented.
targets:
- target_id: cmmmech:coal-mine-drainage-treatment-solids
  path: data/records/coal-mine-drainage-treatment-solids.yaml
  label: Coal mine drainage treatment solids
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-mine-drainage-treatment-solids.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/coal-mine-drainage-treatment-solids.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed current batch gate; reviewer inspected terminal receipt
    and actual log. /private/tmp/cmm-round24-final-batch.log: uv run --locked --extra
    dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 89.10s (0:01:29)

    Checked 160 record(s); 0 failed.

    Checked 181 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed current batch gate; reviewer inspected terminal receipt
    and actual log. /private/tmp/cmm-round24-final-require.log: Checked 160 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base d7183efeb2e528d6d88f0b69da41323642b8fa85
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed current batch gate; reviewer inspected terminal receipt
    and actual log. /private/tmp/cmm-round24-final-history.log: Checked 181 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/coal-mine-drainage-treatment-solids.yaml
  locator: Entire frozen scientific record and attached actual CREATE sidecar
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: supports
  summary: Independently read after canonical inspection. The resource has treatment
    origin and explicitly scoped laboratory culture-associated mobilization; no material
    CURIE, criticality or isolated-product claim is invented.
  snapshot_sha256: 9fce0c00b764999d6dd324311b30ec492d3b8cd9e3ff869f618e587d06e0baa9
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min16090930
  locator: Methods 2.1-2.5, Results 3.1-3.6, Discussion and data statement; Figures
    1-7 visually checked on main PDF pages 3, 5, 7-10 and 12
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: supports
  summary: Read complete relevant primary text independently from the same acquired
    source used by the curator. Preparation and 1% w/v, three-day, 30 degrees C assay
    are supported. Decanted supernatant processing, final pH, REE replication, inoculum
    dose and working volume are unspecified; separate Mn and SEM methods do not fill
    these gaps. Lactate production, annotations, staining and SEM are associations
    rather than causal interventions. Figure 3 is normalized by element column, and
    Figure 7 is a proposed schematic. The less-than-1% extraction claim lacks reconciled
    mass accounting and is appropriately not adopted.
  snapshot_sha256: ae54aec052180a4c8f83c9db883537c5526dd75ad581a07f3b0a2a8dfcbed564
- evidence_id: supplement
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/minerals/minerals-16-00930/article_deploy/minerals-16-00930-s001.zip
  locator: Complete four-page minerals-4280163-supplementary.pdf; Figures S1-S2 and
    Tables S1-S2, all visually inspected
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: supports
  summary: Checked all 15 curated JR07/KB7/sterile TREE values against Table S1 and
    verified row-to-feed/isolate key. Kentucky Hollow sterile 228.08 ppb remains visible;
    Wingfield Pines JR07 0.82 ppb is below sterile 1.59 ppb. Missing AV22/AV24 rows
    are not zero outcomes. BDL analytes and absent Pm column are explicit; TREE is
    source-reported with an unstated summation convention. Mn n=3 and HPLC n=3 are
    separate assays, while Table S2 genome metrics do not establish strain accessions
    or gene necessity.
  snapshot_sha256: 934f7daf82352301093b8236788d522d1bb9011a0b1999854efa7de190070f9c
- evidence_id: taxonomy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1405&mode=info
  locator: Live NCBI species pages 1405 and 64104 on 2026-10-11
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: supports
  summary: Bacillus mycoides and Bacillus pseudomycoides names correspond to the record
    species identifiers. These species pages do not independently identify isolates
    JR07/KB7, prove study-stock identity or supply unreported genome accessions.
- evidence_id: search
  kind: search
  reference: https://www.mdpi.com/2075-163X/16/9/930
  locator: Exact DOI/title publication and correction searches plus bounded repository
    dedup
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: context_only
  summary: Queries "10.3390/min16090930" correction OR retraction OR erratum and "Bioleaching
    Rare Earth Elements from Abandoned Coal Mine Drainage" returned matching bibliographic
    metadata without a matching correction notice in the inspected first sets. Direct
    publisher open was unavailable, but full publisher-CDN PDF and supplement provenance
    were independently inspected. No exhaustive absence assertion.
  search_scope: Web first returned result sets, no filters or pagination. Reviewer
    ran rg --no-ignore --hidden --follow for min16090930, coal.mine.drainage, CMD
    solids, JR07 and KB7 under data/records, research, reviews and history; only this
    new lane matched. Cited raw acquisition manifests were read; unrelated home/temp
    trees were excluded.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round24-gate-receipts.json
  locator: Current batch terminal receipts, actual logs, frozen target hashes and
    named validation
  accessed_at: '2026-10-11T14:27:27.005646Z'
  support: supports
  summary: Root executed the current full batch, nonempty corpus and trusted-base
    history gates. Reviewer independently ran named validation and read root receipts/logs,
    confirming the reviewed target and input bytes remain unchanged. These checks
    establish structural/provenance validity, not scientific truth.
  snapshot_sha256: 78d51f2509b4419f72d1833d47d0d3b26bb21a56e3cad6bd806665d10ca026bb
assessments:
- assessment_id: identity
  area: identity
  topic: Treatment-origin secondary resource and feed boundaries
  outcome: supported
  summary: The five passive coal-mine-drainage treatment feeds form one process-defined
    resource distinct from untreated water, ash, ore and individual minerals; composition
    and criticality are not generalized.
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Solids accumulated during passive treatment of coal-mine drainage.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority, jurisdiction, list or edition is inherited from REE
      or other constituents.
    evidence_ids:
    - record
  - name: feed_scope
    value: Five Pennsylvania passive treatment systems
    definition: Prepared coatings from Glasgow, Scootac, Kentucky Hollow, Sterrett
      and Wingfield Pines; heterogeneity remains explicit.
    evidence_ids:
    - primary
- assessment_id: mechanism
  area: evidence
  topic: Qualified acidogenic culture association with REE mobilization
  outcome: supported
  summary: The selected culture-associated concentration comparisons are supported
    by the complete supplement. Negative comparisons, unreported conditions and source
    mass-balance inconsistencies prevent causal or recovery overstatement.
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
  evidence_ids:
  - record
  - primary
  - supplement
  - taxonomy
  dimensions:
  - name: organism_strain
    value: Author-assigned B. mycoides JR07 and B. pseudomycoides KB7
    definition: Two separately inoculated isolates; CURIEs identify species, not independently
      verified strain accessions.
    evidence_ids:
    - record
    - primary
    - taxonomy
  - name: biomass_state
    value: Living bacterial cultures
    definition: The mechanism is microbial; separate preparation/autoclaving of feed
      does not imply inactive inoculum.
    evidence_ids:
    - primary
  - name: pretreatment
    value: Washed coatings, dried, ground and autoclaved
    definition: 60 degrees C for about 24-48 h, then 121 degrees C for 30 min; transfer
      limits retained.
    evidence_ids:
    - primary
  - name: conditions_controls
    value: 1% w/v, three days, 30 degrees C and sterile-medium/solid controls
    definition: Medium recipe pH 7.6 does not provide final experimental pH. There
      is no matched-acid series; Mn and SEM assay parameters are distinct.
    evidence_ids:
    - primary
    - supplement
  - name: outcome
    value: Source-reported decanted-supernatant TREE in ppb
    definition: Concentrations are not isolated product, extraction yield or statistically
      estimated effect. Kentucky Hollow sterile and Wingfield JR07 counterexamples
      are explicit.
    evidence_ids:
    - record
    - supplement
  - name: deployment
    value: Laboratory assay using material from field treatment systems
    definition: Operational feed origin does not establish an operating microbial
      extraction process.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE provenance and independent exact-state assessment
  outcome: supported
  summary: The author differs from the reviewer. Canonical inspection preceded assessment,
    final input hashes remain current, and distinct inline/sidecar histories describe
    actual curation. No record changes were made by the reviewer.
  target_ids:
  - cmmmech:coal-mine-drainage-treatment-solids
  evidence_ids:
  - record
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- REE-assay final pH, oxygen conditions, inoculum amount, working volume and replicate/uncertainty
  metadata remain unspecified.
- Unreported filtration and digestion leave the analytical fraction broader than proven
  dissolved ions; no phase-specific flux or product mass balance is established.
- No matched-acid or pathway intervention establishes lactate, genes or biofilms as
  necessary causes.
- TREE totals, absent Pm column, censored individual analytes and less-than-1% extraction
  accounting retain the source limitations; no repaired measurements are asserted.
- Bounded correction and dedup searches do not prove global absence of notices, sources
  or duplicate concepts outside the stated boundary.
notes:
- All required gate commands were executed for the current batch; shared batch gates
  were run by the parent and independently inspected by this reviewer.
- Primary and supplement PDFs were reused from this batch curator acquisition, not
  falsely represented as an independent redownload.
tags:
- round24
- independent
- scientific-review
- secondary-resource
```
