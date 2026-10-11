# Independent scientific review of bornite culture and biofilm observations

- Review: 20261011T195817Z-bornite-round32-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T19:50:45Z
- Finished UTC: 2026-10-11T19:58:17.332560Z
- Reviewer: Codex /root/round27_eaf_slag (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record accurately represents bornite identity and two bounded culture/biofilm-associated laboratory observations. Original endpoint, biomass-unit, specimen-purity and iron-label conflicts remain explicit; controls and apparatus/community confounding constrain causal and recovery claims. No actionable record defect was identified. Named validation and all final cohort batch/nonempty/history gates passed; canonical review checking follows saving all cohort reviews.

## Scope And Provenance

Every maintained bornite field, both mechanisms and canonical CREATE; identity, primary methods, all original figures and relevant SI, controls, measurements, contrary evidence, notices and laboratory scope.

Selection: One new root-authored round32 mineral record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 09c15cbfb7699e40ae4648b6b414784a00b488db.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bornite | data/records/bornite.yaml | maintained | Bornite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:bornite | Reviewer executed: Checked 1 record; 0 failed. Retained log /private/tmp/cmm-round32-bornite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final cohort batch gate | passed | True | cmmmech:bornite | Parent executed; reviewer independently read the actual terminal receipt and hash-verified this log: /private/tmp/cmm-round32-final-batch.log SHA256 91fc92a09a1ef9acd34601d396f1956413ad4d0908a98399d6bdff93c817b541. Final log lines: ....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 172.64s (0:02:52)<br>Checked 187 record(s); 0 failed.<br>Checked 215 history record(s); 0 error(s). |
| Final cohort nonempty gate | passed | True | cmmmech:bornite | Parent executed; reviewer independently read the actual terminal receipt and hash-verified this log: /private/tmp/cmm-round32-final-nonempty.log SHA256 3870a3df4688495609ebd3dce4c53379dc4bd7f1a56290d344ad3305e9e0b6e8. Final log lines: Checked 187 record(s); 0 failed. |
| Final cohort history gate | passed | True | cmmmech:bornite | Parent executed; reviewer independently read the actual terminal receipt and hash-verified this log: /private/tmp/cmm-round32-final-history.log SHA256 76cc5044dce12bef4c094bf7e498e5830da0fdb431ee001241a0e78159d21bab. Final log lines: Checked 215 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral, specimen and organism boundaries

identity: supported. Targets: cmmmech:bornite.

Bornite is correctly represented as the IMA mineral Cu5FeS4. Natural multiphase specimens, copper element and other copper minerals remain distinct. Species-level organism mapping is appropriately limited.

### 2019 conditions, controls and outcomes

evidence: supported. Targets: cmmmech:bornite.

The record accurately limits the observation to culture-associated aqueous copper release under externally maintained acid conditions and retains stronger marmatite-addition effects in abiotic assays. It does not infer biological acid production, a unique molecular pathway or industrial operation.

### 2021 biofilm association and causal limits

evidence: supported. Targets: cmmmech:bornite.

The record preserves feed-level solution-copper observations while limiting causal attribution to an association. Nonsterility, unidentified organisms, genus-level FISH and simultaneous apparatus changes preclude a species-specific or biofilm-only causal claim.

### Denominators and source conflicts

quantity: supported. Targets: cmmmech:bornite.

No unsupported harmonization of final copper percentage, cell-count units, specimen purity or phase disappearance was found. Reported Frontiers percentages remain source-labelled feed-copper values, not isolated recovery or pure-bornite conversion.

### Exact record, source and history consistency

provenance: supported. Targets: cmmmech:bornite.

The record and canonical history match the inspected durable-base input hashes. Original main texts, all relevant original figures/SI and the actual author correction support the scoped qualified acceptance. No maintained correction was required.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/bornite.yaml; All maintained fields and both mechanisms | supports | The mineral identity, specimen-specific observations, uncertainty, source mapping and laboratory scope were independently assessed. No criticality entry or isolated-product yield is asserted. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original PDF pages 1, 2 and 29, all visually inspected | supports | The official row identifies Bornite, Cu5FeS4, approved status A and 1962 s.p.; column definitions establish special-procedure notation. It does not identify the purity of either experimental specimen. |
| rsc | https://doi.org/10.1039/C9RA03658J; Complete original JATS body; Sections 2–4; all original Figures 1–5 visually inspected | supports | Methods support the source-labelled unaccessioned A. ferrooxidans culture, UV-treated museum specimen, externally maintained acidity and culture-associated copper mobilization. Figure 1d endpoints contradict the prose greater-than-90% final result; Figure 4c biomass units conflict with discussion units. No single final yield or biomass value is imported. Independent flask replication and sampling mass correction are not established. Graphite/paraffin electrode assays and the heap schematic remain separate from the culture experiment. |
| rsc_si | https://doi.org/10.1039/C9RA03658J; Original two-page supplementary PDF, Table S1 and all Figure S1 panels; both pages visually inspected | supports | Elemental XRF values 62.301 wt% Cu, 9.982 wt% Fe and 24.222 wt% S match the record. Elemental analysis is not quantitative phase purity; residual Raman signals do not supply an absolute mineral balance. |
| correction | https://doi.org/10.1039/C9RA90072A; Complete original publisher correction JATS | context_only | The notice corrects Hussnain Ahmed Janjua’s author-name spelling only. It does not revise the experimental results or reconcile the endpoint/unit discrepancies. |
| frontiers | https://doi.org/10.3389/fmicb.2021.761997; Complete ten-page primary PDF and JATS body; all ten original page renders and Figures 1–6 visually inspected | supports | The source supports mixed-specimen copper release, attached material and microbial signals in nonsterile screening/flow experiments. Optical 74.91% and QEMSCAN approximately 32% bornite estimates are not reconciled. The record preserves the 0.7 versus 0.5 g/L iron-label conflict, day 46/48 discrepancy, missing displayed bornite control curves, genus-level FISH and apparatus confounding. Reported feed-level copper percentages do not establish selective bornite conversion. The separate chalcopyrite arm and proposed pathway are not transferred as demonstrated bornite causation. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Live issuing-authority search plus retained browser and Datasets API response | supports | NCBI 920 resolves to Acidithiobacillus ferrooxidans at species rank, with historical Thiobacillus ferrooxidans synonym. This mapping does not authenticate the unaccessioned 2019 stock or assign a collection type strain to it. |
| history | history/records/bornite/2026-10-11T194734Z-codex-824206.yaml; Complete canonical CREATE and the distinct inline event in the record | supports | The sidecar identifies the actual Codex/GPT-6 actor, target and current creation session. Its source-scoped event is consistent with the changed record and does not claim this independent review. |
| local_overlap | /private/tmp/cmm-round32-bornite-independent/local-overlap.txt; Independent matching-line output across current records, research, reviews and history | supports | The search locates the new bornite record and its current supporting artifacts; existing copper/chalcopyrite contexts do not denote this mineral record. This is a bounded text-overlap assessment, not a claim of machine-wide or binary-complete novelty. |
| notices | /private/tmp/cmm-round32-bornite-independent/search-receipt.json; Independent exact-DOI correction/retraction queries and issuing-taxonomy search; returned result sets | supports | The search confirms the actual RSC author correction. No additional Frontiers notice surfaced in the bounded returned results. Source-internal counterevidence was independently assessed; full methods of the uncurated 2010/2019 external leads were not reviewed. |

## Limits And Additional Notes

- 2019 final extraction prose and original plot disagree; biomass units, flask replication, solid-loading comparability and sampling-volume mass accounting remain unresolved.
- 2021 mixed-specimen mineral estimates disagree and unclassified surface material affects QEMSCAN. Source iron additions and final-day labels conflict; no independent pure-bornite copper balance is possible.
- Nonsterile community signals and unlike screening/flow apparatus cannot establish biofilm-only or species-specific causation. The proposed ferric/idaite pathways are interpretations, not isolated molecular mechanisms.
- Source-labelled organisms are not authenticated strains. No inherited criticality or industrial deployment is established.
- Notice and local overlap searches are bounded, with hidden/ignored local text included. Deferred external studies were not promoted from abstracts to mechanisms.
- 2019 main was assessed through complete original JATS and original figures plus SI; the blocked local main-PDF response was not treated as a readable PDF. All ten original 2021 PDF pages were inspected.
- The separate molybdenite wording correction does not change this reviewed record. Final cohort gates were executed by the parent and independently verified from complete terminal receipts and matching log hashes; no redundant full suite was run by this reviewer.
- No record or history edit was necessary. Original sources and review working inputs remain outside Git; only the schema-validated native review pair is saved. Source limitations retained in the record are not manufactured into corrective findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T195817Z-bornite-round32-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of bornite culture and biofilm observations
started_at: '2026-10-11T19:50:45Z'
finished_at: '2026-10-11T19:58:17.332560Z'
reviewer:
  identity: Codex /root/round27_eaf_slag
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored bornite; this reviewer authored the separate chromite-tailings
    extension and round32 publication/frontier drafts, not bornite or its history.
    Shared worktree and curator-acquired original artifacts are disclosed. Canonical
    inspection preceded independent full-primary assessment; no target bytes were
    edited.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record accurately represents bornite identity and two bounded culture/biofilm-associated
  laboratory observations. Original endpoint, biomass-unit, specimen-purity and iron-label
  conflicts remain explicit; controls and apparatus/community confounding constrain
  causal and recovery claims. No actionable record defect was identified. Named validation
  and all final cohort batch/nonempty/history gates passed; canonical review checking
  follows saving all cohort reviews.
source:
  git_revision: 09c15cbfb7699e40ae4648b6b414784a00b488db
  state: working_tree
  inputs:
  - path: data/records/bornite.yaml
    sha256: 85a23954d070772bf059c74b7cabf10fe20c6131220abd99cef8b900fbebd261
    role: target
  - path: history/records/bornite/2026-10-11T194734Z-codex-824206.yaml
    sha256: 452167e33eb4a93dcd59c61a2eaadef94c2aeceee01d90cf8bfa3a1ae1955daa
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every maintained bornite field, both mechanisms and canonical CREATE;
    identity, primary methods, all original figures and relevant SI, controls, measurements,
    contrary evidence, notices and laboratory scope.
  selection: One new root-authored round32 mineral record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bornite
  exclusions:
  - target: Raw instrumental reanalysis and full methods of deferred 2010/2019 external
      leads
    reason: Not available or needed to assert the narrower accepted observations;
      no exhaustive literature or independent numerical reconstruction is claimed.
targets:
- target_id: cmmmech:bornite
  path: data/records/bornite.yaml
  label: Bornite
  kind: maintained
  ownership_note: Maintained CMMMech YAML; root authored this record, reviewer did
    not.
checks:
- check_id: named
  name: Independent named record validation
  command: uv run --locked cmmmech validate data/records/bornite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer executed: Checked 1 record; 0 failed. Retained log /private/tmp/cmm-round32-bornite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e'
  target_ids:
  - cmmmech:bornite
- check_id: cohort_batch
  name: Final cohort batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the actual terminal receipt
    and hash-verified this log: /private/tmp/cmm-round32-final-batch.log SHA256 91fc92a09a1ef9acd34601d396f1956413ad4d0908a98399d6bdff93c817b541.
    Final log lines: ....................................................sss.................
    [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 172.64s (0:02:52)

    Checked 187 record(s); 0 failed.

    Checked 215 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:bornite
- check_id: cohort_nonempty
  name: Final cohort nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the actual terminal receipt
    and hash-verified this log: /private/tmp/cmm-round32-final-nonempty.log SHA256
    3870a3df4688495609ebd3dce4c53379dc4bd7f1a56290d344ad3305e9e0b6e8. Final log lines:
    Checked 187 record(s); 0 failed.'
  target_ids:
  - cmmmech:bornite
- check_id: cohort_history
  name: Final cohort history gate
  command: uv run --locked cmmmech validate-history --base 09c15cbfb7699e40ae4648b6b414784a00b488db
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the actual terminal receipt
    and hash-verified this log: /private/tmp/cmm-round32-final-history.log SHA256
    76cc5044dce12bef4c094bf7e498e5830da0fdb431ee001241a0e78159d21bab. Final log lines:
    Checked 215 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:bornite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/bornite.yaml
  locator: All maintained fields and both mechanisms
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The mineral identity, specimen-specific observations, uncertainty, source
    mapping and laboratory scope were independently assessed. No criticality entry
    or isolated-product yield is asserted.
  snapshot_sha256: 85a23954d070772bf059c74b7cabf10fe20c6131220abd99cef8b900fbebd261
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original PDF pages 1, 2 and 29, all visually inspected
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The official row identifies Bornite, Cu5FeS4, approved status A and 1962
    s.p.; column definitions establish special-procedure notation. It does not identify
    the purity of either experimental specimen.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: rsc
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA03658J
  locator: Complete original JATS body; Sections 2–4; all original Figures 1–5 visually
    inspected
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: Methods support the source-labelled unaccessioned A. ferrooxidans culture,
    UV-treated museum specimen, externally maintained acidity and culture-associated
    copper mobilization. Figure 1d endpoints contradict the prose greater-than-90%
    final result; Figure 4c biomass units conflict with discussion units. No single
    final yield or biomass value is imported. Independent flask replication and sampling
    mass correction are not established. Graphite/paraffin electrode assays and the
    heap schematic remain separate from the culture experiment.
  snapshot_sha256: c3bc31018b6d287b3ebb233ade5c14bd17a7d6871451c62b7132f615040b6254
- evidence_id: rsc_si
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA03658J
  locator: Original two-page supplementary PDF, Table S1 and all Figure S1 panels;
    both pages visually inspected
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: Elemental XRF values 62.301 wt% Cu, 9.982 wt% Fe and 24.222 wt% S match
    the record. Elemental analysis is not quantitative phase purity; residual Raman
    signals do not supply an absolute mineral balance.
  snapshot_sha256: f1937ae26ea9e7fd94839a98a9e3c3265dc56515dfbc54287408a917ab01fd71
- evidence_id: correction
  kind: primary_source
  reference: https://doi.org/10.1039/C9RA90072A
  locator: Complete original publisher correction JATS
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: context_only
  summary: The notice corrects Hussnain Ahmed Janjua’s author-name spelling only.
    It does not revise the experimental results or reconcile the endpoint/unit discrepancies.
  snapshot_sha256: 07b49f0a633bbe51467b4966c6a709803ef8672ffa38023a9f3cc1a530ce0114
- evidence_id: frontiers
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2021.761997
  locator: Complete ten-page primary PDF and JATS body; all ten original page renders
    and Figures 1–6 visually inspected
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The source supports mixed-specimen copper release, attached material and
    microbial signals in nonsterile screening/flow experiments. Optical 74.91% and
    QEMSCAN approximately 32% bornite estimates are not reconciled. The record preserves
    the 0.7 versus 0.5 g/L iron-label conflict, day 46/48 discrepancy, missing displayed
    bornite control curves, genus-level FISH and apparatus confounding. Reported feed-level
    copper percentages do not establish selective bornite conversion. The separate
    chalcopyrite arm and proposed pathway are not transferred as demonstrated bornite
    causation.
  snapshot_sha256: 02d34d6104607f52393541b7edf207c5148fc29792df285e8a0dc3abb39ec436
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Live issuing-authority search plus retained browser and Datasets API response
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: NCBI 920 resolves to Acidithiobacillus ferrooxidans at species rank, with
    historical Thiobacillus ferrooxidans synonym. This mapping does not authenticate
    the unaccessioned 2019 stock or assign a collection type strain to it.
  snapshot_sha256: a9018b21b07448df4983bdc7fbada96c6331825223cb00220b4f51109279d4bf
- evidence_id: history
  kind: record_content
  reference: history/records/bornite/2026-10-11T194734Z-codex-824206.yaml
  locator: Complete canonical CREATE and the distinct inline event in the record
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The sidecar identifies the actual Codex/GPT-6 actor, target and current
    creation session. Its source-scoped event is consistent with the changed record
    and does not claim this independent review.
  snapshot_sha256: 452167e33eb4a93dcd59c61a2eaadef94c2aeceee01d90cf8bfa3a1ae1955daa
- evidence_id: local_overlap
  kind: search
  reference: /private/tmp/cmm-round32-bornite-independent/local-overlap.txt
  locator: Independent matching-line output across current records, research, reviews
    and history
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The search locates the new bornite record and its current supporting artifacts;
    existing copper/chalcopyrite contexts do not denote this mineral record. This
    is a bounded text-overlap assessment, not a claim of machine-wide or binary-complete
    novelty.
  search_scope: rg --no-ignore --hidden --follow -n C9RA03658J|c9ra03658j|761997|cmmmech:bornite
    in data/records research reviews history; hidden and ignored files and relevant
    symlinks included. Curator’s broader referenced-raw dedup is contextual evidence,
    not claimed as reviewer-executed.
  snapshot_sha256: 3e741606cc009bc41862787e866c11a3ac941338c5bd88e3cd85738ef2a3d92e
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round32-bornite-independent/search-receipt.json
  locator: Independent exact-DOI correction/retraction queries and issuing-taxonomy
    search; returned result sets
  accessed_at: '2026-10-11T19:55:43.212358Z'
  support: supports
  summary: The search confirms the actual RSC author correction. No additional Frontiers
    notice surfaced in the bounded returned results. Source-internal counterevidence
    was independently assessed; full methods of the uncurated 2010/2019 external leads
    were not reviewed.
  search_scope: Exact queries and returned provider results retained. No pagination,
    citation census or universal no-notice clearance claimed.
  snapshot_sha256: 3db66df231af17bb8af9492d6178b10159354beba24bf9b6b2fb2f42d98e4190
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral, specimen and organism boundaries
  outcome: supported
  summary: Bornite is correctly represented as the IMA mineral Cu5FeS4. Natural multiphase
    specimens, copper element and other copper minerals remain distinct. Species-level
    organism mapping is appropriately limited.
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - record
  - ima
  - taxon
  - rsc
  - frontiers
  dimensions:
  - name: material_kind
    value: mineral
    definition: Species identity is independent of the composition and phase proportions
      of the experimental feeds.
    evidence_ids:
    - ima
    - record
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim is inherited from constituent copper
      or iron. This omission is not a not-listed assertion.
    evidence_ids:
    - record
  - name: biomass
    value: Living unaccessioned culture and separate ore-derived mixed enrichment
    definition: 2019 A. ferrooxidans stock and 2021 Leptospirillum/Acidithiobacillus
      enrichment are distinct; neither is authenticated by a species ID.
    evidence_ids:
    - rsc
    - frontiers
    - taxon
- assessment_id: rsc_scope
  area: evidence
  topic: 2019 conditions, controls and outcomes
  outcome: supported
  summary: The record accurately limits the observation to culture-associated aqueous
    copper release under externally maintained acid conditions and retains stronger
    marmatite-addition effects in abiotic assays. It does not infer biological acid
    production, a unique molecular pathway or industrial operation.
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - record
  - rsc
  - rsc_si
  - correction
  dimensions:
  - name: conditions
    value: 250 mL flasks, 99 mL basal medium plus 1 mL inoculum; 30 °C, 170 rpm, 14
      days
    definition: Sulfuric acid maintains pH 1.70–1.80. Pre-growth ferrous medium is
      not a verified final assay iron concentration.
    evidence_ids:
    - rsc
    - record
  - name: control_boundary
    value: Uninoculated assays and separate mineral-mixing/electrode experiments
    definition: Unknown flask replication, variable mass-label interpretation and
      sample replacement prevent an independently reconstructed yield or precision
      estimate.
    evidence_ids:
    - rsc
    - record
- assessment_id: frontiers_scope
  area: evidence
  topic: 2021 biofilm association and causal limits
  outcome: supported
  summary: The record preserves feed-level solution-copper observations while limiting
    causal attribution to an association. Nonsterility, unidentified organisms, genus-level
    FISH and simultaneous apparatus changes preclude a species-specific or biofilm-only
    causal claim.
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - record
  - frontiers
  dimensions:
  - name: conditions
    value: 30 °C, modified 9K; screening wells versus recirculating laminar flow
    definition: 8 mL screening and 100–200 mL flow conditions differ in volume, geometry,
      orientation and hydrodynamics. Source iron labels conflict.
    evidence_ids:
    - frontiers
    - record
  - name: replication
    value: Three flow replicates; three to five screening replicates per condition/time
    definition: Methods mention uninoculated screening but separate bornite control
      trajectories are not displayed.
    evidence_ids:
    - frontiers
  - name: deployment
    value: Laboratory
    definition: Flow-cell analogy and a proposed heap pathway are not pilot or industrial
      deployment.
    evidence_ids:
    - frontiers
    - record
- assessment_id: quantities
  area: quantity
  topic: Denominators and source conflicts
  outcome: supported
  summary: No unsupported harmonization of final copper percentage, cell-count units,
    specimen purity or phase disappearance was found. Reported Frontiers percentages
    remain source-labelled feed-copper values, not isolated recovery or pure-bornite
    conversion.
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - record
  - rsc
  - rsc_si
  - frontiers
  dimensions:
  - name: measurement
    value: Solution copper by ICP-AES in 2019 and atomic absorption in 2021
    definition: Dissolved copper is distinct from recovered metal. Sample accounting
      and solid-phase attribution remain incomplete.
    evidence_ids:
    - rsc
    - frontiers
  - name: counterevidence
    value: Endpoint decline, optical/QEMSCAN disagreement and unmatched apparatus
    definition: These observations constrain interpretation rather than being silently
      averaged or dropped.
    evidence_ids:
    - rsc
    - frontiers
    - record
- assessment_id: provenance
  area: provenance
  topic: Exact record, source and history consistency
  outcome: supported
  summary: The record and canonical history match the inspected durable-base input
    hashes. Original main texts, all relevant original figures/SI and the actual author
    correction support the scoped qualified acceptance. No maintained correction was
    required.
  target_ids:
  - cmmmech:bornite
  evidence_ids:
  - record
  - history
  - notices
  - local_overlap
  - correction
findings: []
actions: []
limitations:
- 2019 final extraction prose and original plot disagree; biomass units, flask replication,
  solid-loading comparability and sampling-volume mass accounting remain unresolved.
- 2021 mixed-specimen mineral estimates disagree and unclassified surface material
  affects QEMSCAN. Source iron additions and final-day labels conflict; no independent
  pure-bornite copper balance is possible.
- Nonsterile community signals and unlike screening/flow apparatus cannot establish
  biofilm-only or species-specific causation. The proposed ferric/idaite pathways
  are interpretations, not isolated molecular mechanisms.
- Source-labelled organisms are not authenticated strains. No inherited criticality
  or industrial deployment is established.
- Notice and local overlap searches are bounded, with hidden/ignored local text included.
  Deferred external studies were not promoted from abstracts to mechanisms.
- 2019 main was assessed through complete original JATS and original figures plus
  SI; the blocked local main-PDF response was not treated as a readable PDF. All ten
  original 2021 PDF pages were inspected.
notes:
- The separate molybdenite wording correction does not change this reviewed record.
  Final cohort gates were executed by the parent and independently verified from complete
  terminal receipts and matching log hashes; no redundant full suite was run by this
  reviewer.
- No record or history edit was necessary. Original sources and review working inputs
  remain outside Git; only the schema-validated native review pair is saved. Source
  limitations retained in the record are not manufactured into corrective findings.
links:
- research/sources/round32-bornite/20261011T194942Z-source-investigation.md
- https://doi.org/10.1039/C9RA03658J
- https://doi.org/10.3389/fmicb.2021.761997
tags:
- round32
- independent
- scientific
- bornite
```
