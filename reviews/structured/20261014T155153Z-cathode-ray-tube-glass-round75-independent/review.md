# Independent scientific review of waste lead-bearing CRT glass

- Review: 20261014T155153Z-cathode-ray-tube-glass-round75-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T15:45:22.137436Z
- Finished UTC: 2026-10-14T15:51:53.521679Z
- Reviewer: codex /root/round68_iron_sulfides (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Waste-glass identity and qualified abiotic laboratory lead dissolution/electrodeposition are supported. Unknown component provenance, distinct measurement denominators, source timing/model contradictions and absence of verified complete recovery are retained. No corrective finding in this scope.

## Scope And Provenance

Entire frozen maintained CRT-glass owner, linked CREATE and full primary independent assessment.

Selection: Assigned independent single-record review; exact inputs captured with native helper before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4cb10d22d5542370cf5fac27288907ec0d42308c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cathode-ray-tube-glass | data/records/cathode-ray-tube-glass.yaml | maintained | Cathode ray tube glass |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named nonempty validation | passed | True | cmmmech:cathode-ray-tube-glass | Reviewer executed: 1 record / 0 failed; terminal exit 0. |
| Actual current batch and history gates | passed | True | cmmmech:cathode-ray-tube-glass | Coordinator executed; reviewer verified terminal receipt, all command exit codes and log SHA. |

## Scientific And Domain Assessments

### Waste composite glass distinct from lead and phosphors

identity: supported. Targets: cmmmech:cathode-ray-tube-glass.

The paper explicitly calls the experimental material waste CRT glass and reports 22.08 wt.% PbO, not 22.08 wt.% elemental Pb. No component origin, supplier or device provenance is reported. The owner deliberately avoids proving a separately collected funnel fraction from general introduction context; secondary-resource scope is supported and no inherited criticality or material CURIE added.

### Actual thermal, acid and electrodeposition conditions

evidence: supported. Targets: cmmmech:cathode-ray-tube-glass.

Sections2.1–2.3 support 10 g feed / 24 g Na2CO3,1000 degrees C for 30 min,100 mL wash,150 mL 0.2–1 M acetic acid at 80 degrees C for 1 h and divided galvanostatic 150 mL, 22 degrees C electrochemical comparison. Stainless-steel cathode, graphite anode, flow 15/30/45 mL/min and current 4/8/12 mA/cm2 match. Electrolyte composition matches reported leachate but actual unmodified leachate use is not demonstrated for every arm. No organisms or biological mechanism.

### Dissolution, deposition and electrical efficiency have different denominators

quantity: supported. Targets: cmmmech:cathode-ray-tube-glass.

Section2.4 distinguishes dissolved Pb/initial Pb in processed solid, deposited Pb/initial Pb in electrolyte, and current efficiency as charge use. Figures 1–4 make 0.6 M an acid-use/dissolution compromise; its 9.25 g/L Pb or 80% maximum series concentration is not 80% feed recovery. Figure 5 maximum deposited fraction occurs at 12 mA/cm2; lowest energy at 4 mA/cm2 / 45 mL/min is a different criterion. Record preserves these distinctions.

### Observed deposit with qualified purity and integrated-balance limits

evidence: supported. Targets: cmmmech:cathode-ray-tube-glass.

Deposit dissolved in concentrated HNO3 for quantification; conclusion reports 99.98 wt.% Pb without detailed impurity assay/replicate uncertainty. One-hour approximately 10% feed-Pb statement conflicts with Section 2.3 two-hour protocol and cannot close an integrated balance. Figure 1 partial dissolution does not support all remaining feed Pb being dissolved. Abstract complete-recovery assertion is explicitly rejected.

### Environmental mass-flow model is not demonstrated throughput

scope: supported. Targets: cmmmech:cathode-ray-tube-glass.

Tables 3–4 supply 10 kg/h model flows and different carbonate-to-feed ratio from lab; 2.02 kg/h Pb output is not reconciled with one-hour approximately 10% metal recovery. Table 3 water classifications also conflict with all-C prose and zero EF, reinforcing the decision not to accept environmental superiority. Table 2 trends are not uniformly monotone despite source prose; no such universal claim is curated. Section 4 leaves scale-up to future work.

### Comparator and replication limitations retained

evidence: supported. Targets: cmmmech:cathode-ray-tube-glass.

Compared acid/current/flow conditions establish conditional observations. No specified untreated-glass/no-carbonate control, replicate count, raw-data uncertainty or continuous closed-loop trial. No causal necessity of thermal pretreatment or general industrial efficiency inferred.

### Exact independently reviewed bytes and current checks

provenance: supported. Targets: cmmmech:cathode-ray-tube-glass.

Native inspect preceded record-level scientific assessment and full original reading. Reviewer authored djurleite, not CRT glass; no CRT owner/history edits. Sixteen primary/render artifacts are nonempty and hashed. All required checks passed at save; no unsupported corrective issue manufactured from limitations already represented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cathode-ray-tube-glass.yaml; Entire frozen owner | supports | Exact maintained scientific fields independently assessed without reviewer edits. |
| history | history/records/cathode-ray-tube-glass/2026-10-14T154456Z-codex-6992dd.yaml; Entire linked CREATE and distinct inline event | supports | Target, actor, actual UTC times and scope match this curation. |
| primary | https://doi.org/10.3390/ma14061546; Complete 12-page original imre2021.pdf, all original page renders; Sections1–4, Figures1–8, Tables1–4 and end matter | supports | Shared acquired original independently read in full and all twelve page images visually inspected after native target capture. Laboratory abiotic observations support qualified dissolution and electrodeposition; environmental-model and whole-feed completeness claims remain restricted. |
| xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8004233/fullTextXML; Official original JATS corroborating Methods, metrics and Data Availability Statement | context_only | Identical article identity and methods; no supplementary-material node. Original PDF likewise has no supplementary-material section. This is not a universal absence claim. |
| metadata | https://api.crossref.org/works/10.3390/ma14061546; Retained original Crossref plus independent current PubMed/PMC search | context_only | DOI, authors, publication title and 22 March 2021 agree. Crossref update-to absent and relation empty; bounded notice search found no affecting correction. |
| bindings | /private/tmp/cmm-round75-crt-independent/source-hashes.json; Sixteen nonempty original/source/render artifacts, including actual 2188188-byte main PDF | context_only | Binds actual inspected artifacts by size and SHA256; no failed PDF placeholder substituted. |
| dedup | /private/tmp/cmm-round75-crt-independent/dedup.json; Current hidden/ignored-inclusive searches in isolated worktree and original main | context_only | Only new CRT owner/history matched within this explicit corpus boundary. Glass is distinguished from elemental lead and phosphor powders; no machine-wide novelty claim. |
| notices | /private/tmp/cmm-round75-crt-independent/search.json; Bounded current DOI/title correction, limitation and supplement search | context_only | First returned search windows found no affecting notice; source-internal contradictions were independently checked, not repaired. |
| named | /private/tmp/cmm-round75-crt-independent/named.log; Reviewer-executed named --require-records validation, actual terminal exit0 | supports | One record checked, zero failed. Structural validation does not establish scientific truth. |
| batch | /private/tmp/cmm-round75-final-gates.json; Coordinator-executed current batch after all owner freezes | supports | Reviewer checked trusted base, actual terminal exit0 for every command and matching retained log digest. |
| batch_log | /private/tmp/cmm-round75-final-gates.log; Actual current batch log bound to terminal receipt | supports | Newly executed final batch and append-only history checks, not baseline substitution. |

## Limits And Additional Notes

- Experimental component/supplier/device origin and independent feed-batch replication remain unknown.
- No raw-data supplement is identified in inspected original representations; Data Availability states sharing not applicable. Bounded correction search is not exhaustive.
- Source purity, durations and environmental model contain unresolved limitations; no independent plant operation, complete feed recovery or environmental-superiority claim accepted.
- This review does not assess inaccessible Pant 2014 or Beolchini 2012 microbial originals as experimental evidence; phosphor powder and CRT glass are distinct resources.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T155153Z-cathode-ray-tube-glass-round75-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of waste lead-bearing CRT glass
started_at: '2026-10-14T15:45:22.137436Z'
finished_at: '2026-10-14T15:51:53.521679Z'
reviewer:
  identity: codex /root/round68_iron_sulfides
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Phosphates agent authored this owner/history. Reviewer authored
    only djurleite this round and made no CRT scientific or history edits. Native
    target/history/schema capture preceded full original reading and record-level
    judgment. Shared acquired original independently read and all twelve pages/graphics
    inspected. Preliminary DOI notice searching is separately logged.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Waste-glass identity and qualified abiotic laboratory lead dissolution/electrodeposition
  are supported. Unknown component provenance, distinct measurement denominators,
  source timing/model contradictions and absence of verified complete recovery are
  retained. No corrective finding in this scope.
source:
  git_revision: 4cb10d22d5542370cf5fac27288907ec0d42308c
  state: working_tree
  inputs:
  - path: data/records/cathode-ray-tube-glass.yaml
    sha256: f56443bdc8ab1501589248bbb76dde08193743236983dd2ab7c9b7757e89e670
    role: target
  - path: history/records/cathode-ray-tube-glass/2026-10-14T154456Z-codex-6992dd.yaml
    sha256: 531e1a3b4ecccf3794125a1e2ab1e8f7d419d5cb05865e7a5b5fad89184dbdb3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen maintained CRT-glass owner, linked CREATE and full primary
    independent assessment.
  selection: Assigned independent single-record review; exact inputs captured with
    native helper before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cathode-ray-tube-glass
targets:
- target_id: cmmmech:cathode-ray-tube-glass
  path: data/records/cathode-ray-tube-glass.yaml
  label: Cathode ray tube glass
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cathode-ray-tube-glass.yaml
    role: maintained record
checks:
- check_id: named
  name: Named nonempty validation
  command: uv run --locked cmmmech validate data/records/cathode-ray-tube-glass.yaml
    --require-records
  status: passed
  required: true
  summary: 'Reviewer executed: 1 record / 0 failed; terminal exit 0.'
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Actual current batch and history gates
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base 4cb10d22d5542370cf5fac27288907ec0d42308c
  status: passed
  required: true
  summary: Coordinator executed; reviewer verified terminal receipt, all command exit
    codes and log SHA.
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
  - batch_log
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cathode-ray-tube-glass.yaml
  locator: Entire frozen owner
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: Exact maintained scientific fields independently assessed without reviewer
    edits.
  snapshot_sha256: f56443bdc8ab1501589248bbb76dde08193743236983dd2ab7c9b7757e89e670
- evidence_id: history
  kind: record_content
  reference: history/records/cathode-ray-tube-glass/2026-10-14T154456Z-codex-6992dd.yaml
  locator: Entire linked CREATE and distinct inline event
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: Target, actor, actual UTC times and scope match this curation.
  snapshot_sha256: 531e1a3b4ecccf3794125a1e2ab1e8f7d419d5cb05865e7a5b5fad89184dbdb3
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/ma14061546
  locator: Complete 12-page original imre2021.pdf, all original page renders; Sections1–4,
    Figures1–8, Tables1–4 and end matter
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: Shared acquired original independently read in full and all twelve page
    images visually inspected after native target capture. Laboratory abiotic observations
    support qualified dissolution and electrodeposition; environmental-model and whole-feed
    completeness claims remain restricted.
  snapshot_sha256: 366cb28dce44df644bbae7f0f7a20a8cc2a3bdd547ba4d28ac75ca91f71519fa
- evidence_id: xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8004233/fullTextXML
  locator: Official original JATS corroborating Methods, metrics and Data Availability
    Statement
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: context_only
  summary: Identical article identity and methods; no supplementary-material node.
    Original PDF likewise has no supplementary-material section. This is not a universal
    absence claim.
  snapshot_sha256: b74d87eb1d195f0bc275a0ac35dbedb910ec3f9b2a767dda82efe075d2a2665c
- evidence_id: metadata
  kind: authority
  reference: https://api.crossref.org/works/10.3390/ma14061546
  locator: Retained original Crossref plus independent current PubMed/PMC search
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: context_only
  summary: DOI, authors, publication title and 22 March 2021 agree. Crossref update-to
    absent and relation empty; bounded notice search found no affecting correction.
  snapshot_sha256: a8f4fcc706f5340c4248c8e9a098d22680dd4b56ff1ce02950c05a66cdb0a890
- evidence_id: bindings
  kind: validation
  reference: /private/tmp/cmm-round75-crt-independent/source-hashes.json
  locator: Sixteen nonempty original/source/render artifacts, including actual 2188188-byte
    main PDF
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: context_only
  summary: Binds actual inspected artifacts by size and SHA256; no failed PDF placeholder
    substituted.
  snapshot_sha256: 26e146ba3839c0ca1f009300b4c833b1c3cb6b685dfd3a3777390df87fe89c23
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round75-crt-independent/dedup.json
  locator: Current hidden/ignored-inclusive searches in isolated worktree and original
    main
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: context_only
  summary: Only new CRT owner/history matched within this explicit corpus boundary.
    Glass is distinguished from elemental lead and phosphor powders; no machine-wide
    novelty claim.
  snapshot_sha256: 621163d2f2fcfe8781bfedfed8f0dba62aa1d5073fca352e0dcb4545da6c968c
  search_scope: rg --hidden --no-ignore --follow --text -l -i cathode.ray|ma14061546
    across data/records,research,reviews,history in both checkouts; actual exit 0
    worktree / exit 1 main with no errors. Curator prior-raw boundary examined separately.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round75-crt-independent/search.json
  locator: Bounded current DOI/title correction, limitation and supplement search
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: context_only
  summary: First returned search windows found no affecting notice; source-internal
    contradictions were independently checked, not repaired.
  snapshot_sha256: d91797c091681d21f628cbb9aaa30448fce522f984b9d123e63fce3fbeba1052
  search_scope: 2026-10-14 exact DOI correction/erratum/retraction; CRT glass+Imre
    2021 lead limitations; exact DOI supplementary; no date/domain filter or exhaustive
    pagination.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round75-crt-independent/named.log
  locator: Reviewer-executed named --require-records validation, actual terminal exit0
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: One record checked, zero failed. Structural validation does not establish
    scientific truth.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round75-final-gates.json
  locator: Coordinator-executed current batch after all owner freezes
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: Reviewer checked trusted base, actual terminal exit0 for every command
    and matching retained log digest.
  snapshot_sha256: 181ca72cfa526f2d6e43b7472b32024d250ce34583cadf1d400e2a2a1e394879
- evidence_id: batch_log
  kind: validation
  reference: /private/tmp/cmm-round75-final-gates.log
  locator: Actual current batch log bound to terminal receipt
  accessed_at: '2026-10-14T15:51:53.521679Z'
  support: supports
  summary: Newly executed final batch and append-only history checks, not baseline
    substitution.
  snapshot_sha256: c6b5357c7bcc3003495533f942055076b5c6e8320007a4af9741592c69d98270
assessments:
- assessment_id: identity
  area: identity
  topic: Waste composite glass distinct from lead and phosphors
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  - dedup
  summary: The paper explicitly calls the experimental material waste CRT glass and
    reports 22.08 wt.% PbO, not 22.08 wt.% elemental Pb. No component origin, supplier
    or device provenance is reported. The owner deliberately avoids proving a separately
    collected funnel fraction from general introduction context; secondary-resource
    scope is supported and no inherited criticality or material CURIE added.
- assessment_id: protocol
  area: evidence
  topic: Actual thermal, acid and electrodeposition conditions
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  summary: Sections2.1–2.3 support 10 g feed / 24 g Na2CO3,1000 degrees C for 30 min,100
    mL wash,150 mL 0.2–1 M acetic acid at 80 degrees C for 1 h and divided galvanostatic
    150 mL, 22 degrees C electrochemical comparison. Stainless-steel cathode, graphite
    anode, flow 15/30/45 mL/min and current 4/8/12 mA/cm2 match. Electrolyte composition
    matches reported leachate but actual unmodified leachate use is not demonstrated
    for every arm. No organisms or biological mechanism.
- assessment_id: denominators
  area: quantity
  topic: Dissolution, deposition and electrical efficiency have different denominators
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  summary: Section2.4 distinguishes dissolved Pb/initial Pb in processed solid, deposited
    Pb/initial Pb in electrolyte, and current efficiency as charge use. Figures 1–4
    make 0.6 M an acid-use/dissolution compromise; its 9.25 g/L Pb or 80% maximum
    series concentration is not 80% feed recovery. Figure 5 maximum deposited fraction
    occurs at 12 mA/cm2; lowest energy at 4 mA/cm2 / 45 mL/min is a different criterion.
    Record preserves these distinctions.
- assessment_id: product
  area: evidence
  topic: Observed deposit with qualified purity and integrated-balance limits
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  summary: Deposit dissolved in concentrated HNO3 for quantification; conclusion reports
    99.98 wt.% Pb without detailed impurity assay/replicate uncertainty. One-hour
    approximately 10% feed-Pb statement conflicts with Section 2.3 two-hour protocol
    and cannot close an integrated balance. Figure 1 partial dissolution does not
    support all remaining feed Pb being dissolved. Abstract complete-recovery assertion
    is explicitly rejected.
- assessment_id: scale
  area: scope
  topic: Environmental mass-flow model is not demonstrated throughput
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  summary: Tables 3–4 supply 10 kg/h model flows and different carbonate-to-feed ratio
    from lab; 2.02 kg/h Pb output is not reconciled with one-hour approximately 10%
    metal recovery. Table 3 water classifications also conflict with all-C prose and
    zero EF, reinforcing the decision not to accept environmental superiority. Table
    2 trends are not uniformly monotone despite source prose; no such universal claim
    is curated. Section 4 leaves scale-up to future work.
- assessment_id: controls
  area: evidence
  topic: Comparator and replication limitations retained
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - primary
  summary: Compared acid/current/flow conditions establish conditional observations.
    No specified untreated-glass/no-carbonate control, replicate count, raw-data uncertainty
    or continuous closed-loop trial. No causal necessity of thermal pretreatment or
    general industrial efficiency inferred.
- assessment_id: provenance
  area: provenance
  topic: Exact independently reviewed bytes and current checks
  outcome: supported
  target_ids:
  - cmmmech:cathode-ray-tube-glass
  evidence_ids:
  - record
  - history
  - bindings
  - named
  - batch
  - batch_log
  summary: Native inspect preceded record-level scientific assessment and full original
    reading. Reviewer authored djurleite, not CRT glass; no CRT owner/history edits.
    Sixteen primary/render artifacts are nonempty and hashed. All required checks
    passed at save; no unsupported corrective issue manufactured from limitations
    already represented.
findings: []
actions: []
limitations:
- Experimental component/supplier/device origin and independent feed-batch replication
  remain unknown.
- No raw-data supplement is identified in inspected original representations; Data
  Availability states sharing not applicable. Bounded correction search is not exhaustive.
- Source purity, durations and environmental model contain unresolved limitations;
  no independent plant operation, complete feed recovery or environmental-superiority
  claim accepted.
- This review does not assess inaccessible Pant 2014 or Beolchini 2012 microbial originals
  as experimental evidence; phosphor powder and CRT glass are distinct resources.
```
