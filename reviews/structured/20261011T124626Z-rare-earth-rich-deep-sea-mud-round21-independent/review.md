# Independent scientific review of rare-earth-rich deep-sea mud

- Review: 20261011T124626Z-rare-earth-rich-deep-sea-mud-round21-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T12:44:20Z
- Finished UTC: 2026-10-11T12:46:26Z
- Reviewer: Codex /root/round21_circuit_boards (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Natural heterogeneous sediment identity and primary-resource boundary are supported. Observational microbial context is correctly separated from causal extraction, and no inherited criticality or yield is asserted. No actionable defect found in the complete assigned record.

## Scope And Provenance

Complete frozen identity-only mud record, attached CREATE provenance and all accepted identity/context claims.

Selection: One assigned new maintained record in round21; independent review after canonical inspect.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 55fd1947e80f67ec91dfe63e7bf15f72d822cefb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:rare-earth-rich-deep-sea-mud | data/records/rare-earth-rich-deep-sea-mud.yaml | maintained | Rare-earth-rich deep-sea mud |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:rare-earth-rich-deep-sea-mud | Reviewer executed to terminal exit 0; Checked 1 record(s); 0 failed. Log /private/tmp/cmm-round21-mud-review/named-validation.log. |
| Native full checks | passed | True | cmmmech:rare-earth-rich-deep-sea-mud | Parent executed; reviewer independently inspected the actual completed receipt and logs. /private/tmp/cmm-round21-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 132.48s (0:02:12)<br>Checked 152 record(s); 0 failed.<br>Checked 169 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:rare-earth-rich-deep-sea-mud | Parent executed; reviewer independently inspected the actual completed receipt and logs. /private/tmp/cmm-round21-final-require.log: Checked 152 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:rare-earth-rich-deep-sea-mud | Parent executed; reviewer independently inspected the actual completed receipt and logs. /private/tmp/cmm-round21-final-history.log: Checked 169 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Natural mixed sediment versus host minerals, commodities and marine concretion feeds

identity: supported. Targets: cmmmech:rare-earth-rich-deep-sea-mud.

Official resource classification and primary natural-sediment study support primary_resource and a distinct mud identity; BCP host grains are contextual, not a universal formula.

### Primary host evidence and observational community context

evidence: supported. Targets: cmmmech:rare-earth-rich-deep-sea-mud.

Takaya analytical/physical methods support REY-bearing BCP grains in selected samples. Wang sequencing/correlations supply context while causal extraction and industrial outcomes remain unasserted.

### Exact working bytes, actor history and required checks

provenance: supported. Targets: cmmmech:rare-earth-rich-deep-sea-mud.

Canonical inspect captured trusted base, target and context before judging. Actual CREATE history and separate inline event are coherent; named/corpus/native/history checks pass for unchanged target bytes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/rare-earth-rich-deep-sea-mud.yaml; Complete maintained YAML, linked CREATE history, source dossier and schema | supports | Exact frozen record and actual CREATE event read after canonical inspect. Primary-resource identity; no criticality, mechanism, organism CURIE or quantitative yield assertions. History actor/model/tool and actual timestamp are consistent. |
| usgs | https://pubs.usgs.gov/fs/2025/3017/fs20253017.pdf; Page 1 version and page 2 Table 1; retained four-page official PDF | supports | Independently read official fact-sheet text and visually inspected Table 1. Version 1.1, April 2025 is explicit. REY-rich muds are distinct from nodules, cobalt-rich crusts and phosphorite minerals; the table asterisk cites the 2022 constituent list, not this resource identity. Retained curator acquisition independently read, not a new reviewer download. |
| takaya | https://doi.org/10.1038/s41598-018-23948-5; Results: Determination of the host mineral of REY; Figure 3 on PDF page 4; grain-size separation; Methods for bulk sediment, EPMA/LA-ICP-MS and hydrocyclone processing; Supplementary Table S5(A), supplement page 31 | supports | Independently read the relevant complete sections, source XML metadata and corresponding PDF text, visually inspected Figure 3 and the S5(A) table. Natural western North Pacific sediment contains REY-bearing biogenic calcium phosphate grains; elemental grain analysis and physical separation do not establish microbial processing. The record does not adopt resource estimates, extraction percentages, all-ocean host dominance or a pure apatite formula. Main source and 36-page SI acquired by curator; review examines claim-relevant portions, not all table cells. |
| takaya_si | https://doi.org/10.1038/s41598-018-23948-5; Associated Supplementary Information, 36 pages; Table S5(A), page 31 | supports | Supplementary grain-analysis table separates sample/core depths and major/trace analytes, supporting sample-specific host context. No numeric cell is imported or independently reprocessed for this identity-only record. |
| wang | https://doi.org/10.1371/journal.pone.0208230; Methods 2.1–2.3, Results 3.5, Discussion 4; live PLOS article metadata; retained full XML | supports | Natural Indian Ocean gravity-core sediments were chemically characterized and assayed with 16S community sequencing and environmental correlations. These are observational data, not controlled extraction assays. Discussion expressly retains functional uncertainty. Record correctly limits source to sediment and community context. Live PLOS page confirms title, authors and 17 December 2018 date. Sequence reads and supplements were not reanalysed and no organism-specific claim is imported. |
| search | /private/tmp/cmm-round21-mud-review/dedup.json; Reviewer executed ignored/hidden/follow search, exact DOI notice queries and retained Crossref metadata | context_only | Bounded duplicate search returned 221 matches with no stderr, exit 0, and only the assigned mud identity among maintained records. Neighbouring nodules, crusts and phosphate-rock descriptions were read to check distinct forms. Searches on 2026-10-11: "10.1038/s41598-018-23948-5" correction retraction; "10.1371/journal.pone.0208230" correction retraction; site.pubs.usgs.gov "2025–3017" "1.1". First returned web sets, no pagination or date filters. No specific correction notice found in these sets or retrieved Crossref update/relation fields; this is not exhaustive certification. Direct Nature open failed authentication redirection; retained primary PDF/XML/SI were read. |
| gates | /private/tmp/cmm-round21-gate-receipts.json; Completed receipt plus final-batch, final-require and final-history logs; gated record hash | supports | Actual just check reports 308 passed/3 skipped in 132.48s, 152 records and 169 histories valid. --require-records and trusted-base history exit 0. Reviewer separately validated the target and confirmed the exact gated SHA equals canonical inspect. |

## Limits And Additional Notes

- Review validates identity-only scope, not microbial recovery feasibility, economic resources/reserves or industrial deployment.
- Source host phases vary and BCP sample evidence does not identify a universal host formula or all-ocean enrichment mechanism.
- Only relevant Takaya supplementary material was checked; full raw data, all supplemental cells, Wang supplements and sequence reads were not reprocessed.
- Notice searches cover first result sets and retrieved metadata; publisher Nature live access redirected to authentication. Prior verified primary artifacts were independently inspected.
- Shared worktree, curator-acquired raw files and parent-executed batch checks are disclosed; reviewer independently assessed the scientific target.
- Orientation reading of target and instructions preceded canonical inspect; scientific target judgment followed inspect and the recorded assessment start.
- No scientific record, history or source dossier edits were made by this reviewer. No corrective issue is invented in the absence of an actionable finding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T124626Z-rare-earth-rich-deep-sea-mud-round21-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of rare-earth-rich deep-sea mud
started_at: '2026-10-11T12:44:20Z'
finished_at: '2026-10-11T12:46:26Z'
reviewer:
  identity: Codex /root/round21_circuit_boards
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate agent /root/round21_rare_earth_muds authored this record/history/dossier.
    Reviewer authored a different PCB record in the shared worktree, made no mud edits,
    independently inspected source text and figures, performed notice/duplicate searches
    and named validation. Curator-acquired sources and parent-run batch gates are
    disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Natural heterogeneous sediment identity and primary-resource boundary are
  supported. Observational microbial context is correctly separated from causal extraction,
  and no inherited criticality or yield is asserted. No actionable defect found in
  the complete assigned record.
source:
  git_revision: 55fd1947e80f67ec91dfe63e7bf15f72d822cefb
  state: working_tree
  inputs:
  - path: data/records/rare-earth-rich-deep-sea-mud.yaml
    sha256: 15b30b8b449302f740b33058d42b45bd2524f0b925c69b34cae835ceb9c58499
    role: target
  - path: history/records/rare-earth-rich-deep-sea-mud/2026-10-11T124020Z-codex-a75004.yaml
    sha256: 8c11b72ce4ffdb0e1c29f43b40968b5fd3a61a3cd3bd226a570716670cca748d
    role: context
  - path: research/ingests/round21-ree-mud-sources-20261011.json
    sha256: 450f53a60d803c0764d87be798c13e9942a9d6559e448565db7d0be00291194c
    role: context
  - path: research/ingests/round21-ree-mud-sources-20261011.md
    sha256: 7b85b309e80c357e1fe55e3e497f7b0793bebe53dc8a4b4e127e01924c99fa73
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Complete frozen identity-only mud record, attached CREATE provenance
    and all accepted identity/context claims.
  selection: One assigned new maintained record in round21; independent review after
    canonical inspect.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
  exclusions:
  - target: Other records, quantitative source-table reprocessing, uncurated formation
      mechanisms, raw sequencing and Wang supplements
    reason: No accepted record claim depends on quantitative estimates, taxon-specific
      activity or modelled formation; neighbouring record descriptions checked only
      for identity boundaries.
targets:
- target_id: cmmmech:rare-earth-rich-deep-sea-mud
  path: data/records/rare-earth-rich-deep-sea-mud.yaml
  label: Rare-earth-rich deep-sea mud
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/rare-earth-rich-deep-sea-mud.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/rare-earth-rich-deep-sea-mud.yaml
  status: passed
  required: true
  summary: Reviewer executed to terminal exit 0; Checked 1 record(s); 0 failed. Log
    /private/tmp/cmm-round21-mud-review/named-validation.log.
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently inspected the actual completed
    receipt and logs. /private/tmp/cmm-round21-final-batch.log: uv run --locked --extra
    dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 132.48s (0:02:12)

    Checked 152 record(s); 0 failed.

    Checked 169 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently inspected the actual completed
    receipt and logs. /private/tmp/cmm-round21-final-require.log: Checked 152 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 55fd1947e80f67ec91dfe63e7bf15f72d822cefb
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently inspected the actual completed
    receipt and logs. /private/tmp/cmm-round21-final-history.log: Checked 169 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/rare-earth-rich-deep-sea-mud.yaml
  locator: Complete maintained YAML, linked CREATE history, source dossier and schema
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Exact frozen record and actual CREATE event read after canonical inspect.
    Primary-resource identity; no criticality, mechanism, organism CURIE or quantitative
    yield assertions. History actor/model/tool and actual timestamp are consistent.
  snapshot_sha256: 15b30b8b449302f740b33058d42b45bd2524f0b925c69b34cae835ceb9c58499
- evidence_id: usgs
  kind: primary_source
  reference: https://pubs.usgs.gov/fs/2025/3017/fs20253017.pdf
  locator: Page 1 version and page 2 Table 1; retained four-page official PDF
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Independently read official fact-sheet text and visually inspected Table
    1. Version 1.1, April 2025 is explicit. REY-rich muds are distinct from nodules,
    cobalt-rich crusts and phosphorite minerals; the table asterisk cites the 2022
    constituent list, not this resource identity. Retained curator acquisition independently
    read, not a new reviewer download.
  snapshot_sha256: 881d2703e3e0d5425789859a9403175e8cceed44093167480bcb3c820c46439f
- evidence_id: takaya
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-018-23948-5
  locator: 'Results: Determination of the host mineral of REY; Figure 3 on PDF page
    4; grain-size separation; Methods for bulk sediment, EPMA/LA-ICP-MS and hydrocyclone
    processing; Supplementary Table S5(A), supplement page 31'
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Independently read the relevant complete sections, source XML metadata
    and corresponding PDF text, visually inspected Figure 3 and the S5(A) table. Natural
    western North Pacific sediment contains REY-bearing biogenic calcium phosphate
    grains; elemental grain analysis and physical separation do not establish microbial
    processing. The record does not adopt resource estimates, extraction percentages,
    all-ocean host dominance or a pure apatite formula. Main source and 36-page SI
    acquired by curator; review examines claim-relevant portions, not all table cells.
  snapshot_sha256: b7990eb2e26149d7b457ec264738e73582e2813d0490f51c5542b5c368172f46
- evidence_id: takaya_si
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-018-23948-5
  locator: Associated Supplementary Information, 36 pages; Table S5(A), page 31
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Supplementary grain-analysis table separates sample/core depths and major/trace
    analytes, supporting sample-specific host context. No numeric cell is imported
    or independently reprocessed for this identity-only record.
  snapshot_sha256: 5a20876d2d23682626fe1ce4bac36194be86f92825c4849ab4dd4b9f1364788e
- evidence_id: wang
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0208230
  locator: Methods 2.1–2.3, Results 3.5, Discussion 4; live PLOS article metadata;
    retained full XML
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Natural Indian Ocean gravity-core sediments were chemically characterized
    and assayed with 16S community sequencing and environmental correlations. These
    are observational data, not controlled extraction assays. Discussion expressly
    retains functional uncertainty. Record correctly limits source to sediment and
    community context. Live PLOS page confirms title, authors and 17 December 2018
    date. Sequence reads and supplements were not reanalysed and no organism-specific
    claim is imported.
  snapshot_sha256: 33d1ad620da7489271649c387a512f528b520661739feba8f1041bf771d6698c
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round21-mud-review/dedup.json
  locator: Reviewer executed ignored/hidden/follow search, exact DOI notice queries
    and retained Crossref metadata
  accessed_at: '2026-10-11T12:46:26Z'
  support: context_only
  summary: 'Bounded duplicate search returned 221 matches with no stderr, exit 0,
    and only the assigned mud identity among maintained records. Neighbouring nodules,
    crusts and phosphate-rock descriptions were read to check distinct forms. Searches
    on 2026-10-11: "10.1038/s41598-018-23948-5" correction retraction; "10.1371/journal.pone.0208230"
    correction retraction; site.pubs.usgs.gov "2025–3017" "1.1". First returned web
    sets, no pagination or date filters. No specific correction notice found in these
    sets or retrieved Crossref update/relation fields; this is not exhaustive certification.
    Direct Nature open failed authentication redirection; retained primary PDF/XML/SI
    were read.'
  snapshot_sha256: 9fda0bf932104a698ed9a0ad1b837f83693b049f4b2ffbc4639397a74e914811
  search_scope: All data/records, research, reviews, history, /private/tmp/cmm-round21-ree-mud-raw
    and /private/tmp/cmm-round20-nodule-raw; rg --no-ignore --hidden --follow. Unrelated
    machine paths excluded.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round21-gate-receipts.json
  locator: Completed receipt plus final-batch, final-require and final-history logs;
    gated record hash
  accessed_at: '2026-10-11T12:46:26Z'
  support: supports
  summary: Actual just check reports 308 passed/3 skipped in 132.48s, 152 records
    and 169 histories valid. --require-records and trusted-base history exit 0. Reviewer
    separately validated the target and confirmed the exact gated SHA equals canonical
    inspect.
  snapshot_sha256: 80d63b110e213b06b5ff48a2ffb95f6234a571e23ca42ca53b6c7613c3745901
assessments:
- assessment_id: identity
  area: identity
  topic: Natural mixed sediment versus host minerals, commodities and marine concretion
    feeds
  outcome: supported
  summary: Official resource classification and primary natural-sediment study support
    primary_resource and a distinct mud identity; BCP host grains are contextual,
    not a universal formula.
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
  evidence_ids:
  - record
  - usgs
  - takaya
  - takaya_si
  - search
  dimensions:
  - name: material_kind
    value: primary_resource
    definition: Natural REY-enriched deep-ocean sediment; collection and physical
      separation do not establish use/processing waste origin.
    evidence_ids:
    - record
    - usgs
    - takaya
  - name: criticality
    value: Not asserted
    definition: USGS 2025 fact-sheet asterisks refer to 2022 constituent list; no
      resource designation or latest-list inference.
    evidence_ids:
    - record
    - usgs
  - name: identifiers
    value: No external material or organism CURIE asserted
    definition: Verified DOI/title/version sources ground heterogeneous resource,
      not an elemental or taxonomic accession.
    evidence_ids:
    - record
    - takaya
    - wang
- assessment_id: scope
  area: evidence
  topic: Primary host evidence and observational community context
  outcome: supported
  summary: Takaya analytical/physical methods support REY-bearing BCP grains in selected
    samples. Wang sequencing/correlations supply context while causal extraction and
    industrial outcomes remain unasserted.
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
  evidence_ids:
  - record
  - takaya
  - takaya_si
  - wang
  dimensions:
  - name: microbial_scope
    value: No accepted microbial mechanism
    definition: Community composition is observational; strain, biomass state, causal
      activity, treatment conditions/controls and recovery outcomes are not inferred.
    evidence_ids:
    - record
    - wang
  - name: outcome_and_scale
    value: Identity-only; no recovery yield, reserve estimate or industrial claim
    definition: Measured host chemistry and physical separation do not establish microbial
      leaching or deployability; broader paper claims are excluded.
    evidence_ids:
    - record
    - takaya
    - wang
- assessment_id: provenance
  area: provenance
  topic: Exact working bytes, actor history and required checks
  outcome: supported
  summary: Canonical inspect captured trusted base, target and context before judging.
    Actual CREATE history and separate inline event are coherent; named/corpus/native/history
    checks pass for unchanged target bytes.
  target_ids:
  - cmmmech:rare-earth-rich-deep-sea-mud
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- Review validates identity-only scope, not microbial recovery feasibility, economic
  resources/reserves or industrial deployment.
- Source host phases vary and BCP sample evidence does not identify a universal host
  formula or all-ocean enrichment mechanism.
- Only relevant Takaya supplementary material was checked; full raw data, all supplemental
  cells, Wang supplements and sequence reads were not reprocessed.
- Notice searches cover first result sets and retrieved metadata; publisher Nature
  live access redirected to authentication. Prior verified primary artifacts were
  independently inspected.
- Shared worktree, curator-acquired raw files and parent-executed batch checks are
  disclosed; reviewer independently assessed the scientific target.
tags:
- round21
- independent
- scientific-review
- primary-resource
notes:
- Orientation reading of target and instructions preceded canonical inspect; scientific
  target judgment followed inspect and the recorded assessment start.
- No scientific record, history or source dossier edits were made by this reviewer.
  No corrective issue is invented in the absence of an actionable finding.
```
