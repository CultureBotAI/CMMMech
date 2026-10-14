# Independent scientific review of Bobierrite culture-associated phosphate evidence

- Review: 20261014T083149Z-bobierrite-round66-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T08:25:54.170515Z
- Finished UTC: 2026-10-14T08:31:49.125817Z
- Reviewer: codex /root/round66_magnesium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Both primary sources support the bounded historical culture-associated phase assignments. The record preserves impurities, processing uncertainty, control limits and contradictory later source labels. No supported curation defect was found.

## Scope And Provenance

Field-by-field review of the single frozen mineral record, canonical CREATE history and its primary-source claims.

Selection: Assigned record from the round66 phosphate cohort; inspect captured the current Git base and target/context hashes before scientific assessment. Each sibling has a separate review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d57f45621cbe465eb13dfb6cc26cc4197d98f90e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bobierrite | data/records/bobierrite.yaml | maintained | Bobierrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:bobierrite | Reviewer executed the command; exit zero and original log retained. |
| Coordinator batch gate 1 | passed | True | cmmmech:bobierrite | Coordinator execution 2026-10-14T08:26:37.417759+00:00 to 2026-10-14T08:30:04.266682+00:00; reviewer checked actual outcomes and log digest. |
| Coordinator batch gate 2 | passed | True | cmmmech:bobierrite | Coordinator execution 2026-10-14T08:30:04.266767+00:00 to 2026-10-14T08:30:11.880507+00:00; reviewer checked actual outcomes and log digest. |
| Coordinator batch gate 3 | passed | True | cmmmech:bobierrite | Coordinator execution 2026-10-14T08:30:11.880596+00:00 to 2026-10-14T08:30:17.021271+00:00; reviewer checked actual outcomes and log digest. |

## Scientific And Domain Assessments

### Distinct hydrated phosphate mineral

identity: supported. Targets: cmmmech:bobierrite.

The record uses the dated IMA identity, distinguishes the separate barićite species and does not inherit element or commodity criticality.

### 1987 isolate, medium and control boundary

evidence: supported. Targets: cmmmech:bobierrite.

Historical culture-associated phase assignment is supported while purification, impurity, control-outcome and taxonomy limitations remain explicit.

### 2014 recovered agar phase and contradictory evidence

evidence: supported. Targets: cmmmech:bobierrite.

The second mechanism is a qualified recovered-phase observation. It preserves phase-label and sequence inconsistencies, source-dependent outcomes and the lack of isolate-specific phase attribution.

### Identifiers, history and executed checks

provenance: supported. Targets: cmmmech:bobierrite.

Authoritative identities, exact record/history bytes and executed named/batch checks support the saved review. Literature completeness is not claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/bobierrite.yaml; Entire inspected, frozen record | supports | Reviewer independently read every field and compared claims to primary originals. Record and linked CREATE history remain byte-identical to the pre-assessment inspect capture. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 edition, pages 1–2 definitions, page 20 barićite and page 27 bobierrite | supports | Both mineral rows were visually inspected and field definitions reread. Both approved formulas are Mg3(PO4)2(H2O)8, but they remain separate named mineral species. Barićite has approval number 1975-027; bobierrite is grandfathered with original-description year 1868. |
| primary2014 | https://doi.org/10.3390/ijerph110403689; Complete scientific text, Sections 2–4; all five main figures and Tables 1–3 | partial | Independent read of the retained complete publisher PDF and visual check of all figures/tables. The reactor supplies isolated bacteria; phase formation occurs in artificial agar. Six of twelve selected isolates produce spherulites, without an individual bobierrite/barićite phase map. Boiling-water agar recovery and drying precede XRD; no-crystal controls and wastewater-medium negative outcomes are reported. |
| limits2014 | https://doi.org/10.3390/ijerph110403689; Sections 2.4–2.7; Table 2; Table 3; Figures 3–5 | partial | Figure 5 labels a magnesium-phosphate dihydrate instead of the octahydrate companion assigned in Figure 4/text. XRD is an intensity map and EDX does not establish hydration. The 650-nt/200-nt sequence lengths, strain-12 identity discrepancy and biofilm-suspension versus strain-row liquid experiments are visible source limitations. No confirmed molecular mechanism or industrial phosphate recovery follows. |
| metadata2014 | https://api.crossref.org/works/10.3390/ijerph110403689; Retained DOI metadata and original publisher PDF page 1 | supports | Title, DOI, 2014 publication and source identity agree. Retained metadata contains no update-to entry and an empty relation mapping; this does not prove universal notice absence. |
| dedup | /private/tmp/cmm-round66-bobierrite-review-dedup.txt; Independent scoped repository search, including hidden and ignored files and followed links | context_only | Search finds the round65 source handoff, both sibling mineral records and current dossier/history. The studies were already prioritized; they are not presented as newly discovered. Within maintained records the target is a distinct species owner, not a duplicate mineral or elemental record. |
| notices | https://doi.org/10.2465/minerj.13.443; Reviewer live web searches on 2026-10-14 UTC and retained Crossref metadata | context_only | No affecting correction or retraction was identified in the bounded returned sets. Results include the primary publisher/PMC pages and a 1989 clinical bobierrite study, retained as an unassessed lead. New evidence does not remove the explicitly retained source inconsistencies. Direct J-STAGE and NCBI browser opens returned tool errors; the retained official original scan and same-day NCBI XML were used instead. |
| history | history/records/bobierrite/2026-10-14T081659Z-codex-fc5ba1.yaml; Complete canonical CREATE session and linked inline event | supports | Actual codex / GPT-6 CREATE history has the correct target, UTC timestamp, actor and evidence-bounded summary. Independent reviewer authored neither the scientific record nor its CREATE history. |
| named | /private/tmp/cmm-round66-bobierrite-review-validation.log; Entire reviewer-run named validation log | supports | Locked offline named record validation exited zero: Checked 1 record(s); 0 failed. |
| batch | /private/tmp/cmm-round66-final-gates.json; Coordinator command receipts and retained log SHA256 | supports | Actual just check, explicit nonempty corpus validation and trusted-base history validation passed. Reviewer verified receipt outcomes and log hash before saving the positive verdict. |
| primary1987 | https://doi.org/10.2465/minerj.13.443; Complete official five-page scan, pages 443–447, Figures 1–3 | supports | Reviewer visually read every original page because the scan has no extractable text. B-17 recipe, pH 8, aerobic 27 C incubation, up to 35 days, nine experiments per medium and phenotypic Acinetobacter sp. assignment agree with the record. One of 96 screened carbonate-forming isolates produces the target aggregates; 20 others produce struvite. |
| limits1987 | https://doi.org/10.2465/minerj.13.443; Page 444 control paragraph, separation-method referral and unmatched XRD peaks; pages 445–446 spectra/SEM | partial | The original names uninoculated and autoclaved-cell controls but gives no explicit outcome. It refers purification to the uninspected 1983 paper. Figure 1 and text acknowledge unmatched reflections/intensity differences and impurities. Infrared/chemical analysis support a hydrated phosphate assignment without quantitative purity, authentic strain deposit or a controlled biochemical cause. |
| metadata1987 | https://api.crossref.org/works/10.2465/minerj.13.443; Retained Crossref metadata and original title/author/journal page | supports | Title, authors, DOI, year, volume 13(7) and pages 443–447 are consistent. No update-to entry or populated relation mapping appears in retained metadata. |

## Limits And Additional Notes

- The 1983 crystal separation/purification procedure remains uninspected; handling effects cannot be excluded.
- The 1987 paper reports impurities and provides no explicit control outcomes, quantitative phase refinement or authentic strain accession.
- The 2014 phase-label, sequence-length and liquid-inoculum inconsistencies remain unresolved and are preserved in the record.
- Neither source establishes phase-specific recovery yield, unique biochemical cause or industrial deployment.
- The 1989 clinical bobierrite report and additional literature remain unassessed; notice searches are bounded.
- Findings by severity: zero blocker, major, minor or informational curation defects; scientific uncertainties are recorded as limitations rather than invented findings.
- Corrections by reviewer: none. Scientific record and CREATE history remain identical to the inspect snapshot.
- Raw copyrighted source originals and renderings remain outside Git. Review records the curator-acquired sources independently checked by this reviewer.
- Final structured review validation and exact current-record coverage remain coordinator publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T083149Z-bobierrite-round66-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Bobierrite culture-associated phosphate evidence
started_at: '2026-10-14T08:25:54.170515Z'
finished_at: '2026-10-14T08:31:49.125817Z'
reviewer:
  identity: codex /root/round66_magnesium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The record, phosphate dossier and CREATE history were authored
    by /root/round66_phosphates. Reviewer independently inspected source originals
    and frozen inputs and made no phosphate record/history changes; reviewer curated
    unrelated magnesium carbonate/hydroxide records.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Both primary sources support the bounded historical culture-associated phase
  assignments. The record preserves impurities, processing uncertainty, control limits
  and contradictory later source labels. No supported curation defect was found.
source:
  git_revision: d57f45621cbe465eb13dfb6cc26cc4197d98f90e
  state: working_tree
  inputs:
  - path: data/records/bobierrite.yaml
    sha256: 593352892fe231fe888b0282b2068cd673a545be0a63ca02bd80f5a9ea84e53d
    role: target
  - path: history/records/bobierrite/2026-10-14T081659Z-codex-fc5ba1.yaml
    sha256: 9549f86d8feb01ca2c78b46171b3bb2f122685cbda317fff2cb693d241d85165
    role: context
  - path: research/sources/round66-phosphates/20261014T081917Z-source-investigation.json
    sha256: 11bcde593824e281f0296d738ba484abbf2ac5730c1f4ea530c8c9c955505fc3
    role: context
  - path: research/sources/round66-phosphates/20261014T081917Z-source-investigation.md
    sha256: adce885ab19af730c80ce5f9ca441bbd3b769eef1b3c5ede71ae382459869675
    role: context
scope:
  description: Field-by-field review of the single frozen mineral record, canonical
    CREATE history and its primary-source claims.
  selection: Assigned record from the round66 phosphate cohort; inspect captured the
    current Git base and target/context hashes before scientific assessment. Each
    sibling has a separate review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:bobierrite
  exclusions:
  - target: Additional uncurated phosphate literature and unrelated experimental arms
    reason: Not part of the accepted record claims; bounded handoffs and evidence
      access limits remain explicit.
targets:
- target_id: cmmmech:bobierrite
  path: data/records/bobierrite.yaml
  label: Bobierrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bobierrite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/bobierrite.yaml
  status: passed
  required: true
  summary: Reviewer executed the command; exit zero and original log retained.
  target_ids:
  - cmmmech:bobierrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Coordinator batch gate 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:26:37.417759+00:00 to 2026-10-14T08:30:04.266682+00:00;
    reviewer checked actual outcomes and log digest.
  target_ids:
  - cmmmech:bobierrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Coordinator batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:30:04.266767+00:00 to 2026-10-14T08:30:11.880507+00:00;
    reviewer checked actual outcomes and log digest.
  target_ids:
  - cmmmech:bobierrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Coordinator batch gate 3
  command: uv run --locked cmmmech validate-history --base d57f45621cbe465eb13dfb6cc26cc4197d98f90e
  status: passed
  required: true
  summary: Coordinator execution 2026-10-14T08:30:11.880596+00:00 to 2026-10-14T08:30:17.021271+00:00;
    reviewer checked actual outcomes and log digest.
  target_ids:
  - cmmmech:bobierrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/bobierrite.yaml
  locator: Entire inspected, frozen record
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Reviewer independently read every field and compared claims to primary
    originals. Record and linked CREATE history remain byte-identical to the pre-assessment
    inspect capture.
  snapshot_sha256: 593352892fe231fe888b0282b2068cd673a545be0a63ca02bd80f5a9ea84e53d
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 edition, pages 1–2 definitions, page 20 barićite and page
    27 bobierrite
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Both mineral rows were visually inspected and field definitions reread.
    Both approved formulas are Mg3(PO4)2(H2O)8, but they remain separate named mineral
    species. Barićite has approval number 1975-027; bobierrite is grandfathered with
    original-description year 1868.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary2014
  kind: primary_source
  reference: https://doi.org/10.3390/ijerph110403689
  locator: Complete scientific text, Sections 2–4; all five main figures and Tables
    1–3
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: partial
  summary: Independent read of the retained complete publisher PDF and visual check
    of all figures/tables. The reactor supplies isolated bacteria; phase formation
    occurs in artificial agar. Six of twelve selected isolates produce spherulites,
    without an individual bobierrite/barićite phase map. Boiling-water agar recovery
    and drying precede XRD; no-crystal controls and wastewater-medium negative outcomes
    are reported.
  snapshot_sha256: e2713ce7f5d8d37f35c9263eca4990addcf3de0d7112250b25b73256db7cc130
- evidence_id: limits2014
  kind: primary_source
  reference: https://doi.org/10.3390/ijerph110403689
  locator: Sections 2.4–2.7; Table 2; Table 3; Figures 3–5
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: partial
  summary: Figure 5 labels a magnesium-phosphate dihydrate instead of the octahydrate
    companion assigned in Figure 4/text. XRD is an intensity map and EDX does not
    establish hydration. The 650-nt/200-nt sequence lengths, strain-12 identity discrepancy
    and biofilm-suspension versus strain-row liquid experiments are visible source
    limitations. No confirmed molecular mechanism or industrial phosphate recovery
    follows.
  snapshot_sha256: e2713ce7f5d8d37f35c9263eca4990addcf3de0d7112250b25b73256db7cc130
- evidence_id: metadata2014
  kind: database
  reference: https://api.crossref.org/works/10.3390/ijerph110403689
  locator: Retained DOI metadata and original publisher PDF page 1
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Title, DOI, 2014 publication and source identity agree. Retained metadata
    contains no update-to entry and an empty relation mapping; this does not prove
    universal notice absence.
  snapshot_sha256: c884b761b39692d8cde2dff5fb7b7e687eacfd50068620c29f7f03ab0c169d2c
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round66-bobierrite-review-dedup.txt
  locator: Independent scoped repository search, including hidden and ignored files
    and followed links
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: context_only
  summary: Search finds the round65 source handoff, both sibling mineral records and
    current dossier/history. The studies were already prioritized; they are not presented
    as newly discovered. Within maintained records the target is a distinct species
    owner, not a duplicate mineral or elemental record.
  search_scope: rg --no-ignore --hidden --follow -n -i across data/records, research,
    history and reviews; queries include the species spelling, barićite accent variant
    where relevant, and the primary DOI. No machinewide absence claim.
  snapshot_sha256: 6c1a5051957b61ef177e0c8da202d3d3bbd0a357e83491f959f2bfd1462e39b7
- evidence_id: notices
  kind: search
  reference: https://doi.org/10.2465/minerj.13.443
  locator: Reviewer live web searches on 2026-10-14 UTC and retained Crossref metadata
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: context_only
  summary: No affecting correction or retraction was identified in the bounded returned
    sets. Results include the primary publisher/PMC pages and a 1989 clinical bobierrite
    study, retained as an unassessed lead. New evidence does not remove the explicitly
    retained source inconsistencies. Direct J-STAGE and NCBI browser opens returned
    tool errors; the retained official original scan and same-day NCBI XML were used
    instead.
  search_scope: 'Six queries: each of the three exact primary DOIs with correction
    OR erratum OR retraction; bobierrite baricite bacterial precipitation phase assignment;
    bobierrite Acinetobacter 1987 correction; exact Han title with corrigendum. First
    returned sets only; no date/domain filters or pagination.'
- evidence_id: history
  kind: record_content
  reference: history/records/bobierrite/2026-10-14T081659Z-codex-fc5ba1.yaml
  locator: Complete canonical CREATE session and linked inline event
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Actual codex / GPT-6 CREATE history has the correct target, UTC timestamp,
    actor and evidence-bounded summary. Independent reviewer authored neither the
    scientific record nor its CREATE history.
  snapshot_sha256: 9549f86d8feb01ca2c78b46171b3bb2f122685cbda317fff2cb693d241d85165
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round66-bobierrite-review-validation.log
  locator: Entire reviewer-run named validation log
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: 'Locked offline named record validation exited zero: Checked 1 record(s);
    0 failed.'
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round66-final-gates.json
  locator: Coordinator command receipts and retained log SHA256
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Actual just check, explicit nonempty corpus validation and trusted-base
    history validation passed. Reviewer verified receipt outcomes and log hash before
    saving the positive verdict.
  snapshot_sha256: f770d6a65bb5b55e55ec2ef08ddfa02330dab31a1f87a26af94b2b92150a28dc
- evidence_id: primary1987
  kind: primary_source
  reference: https://doi.org/10.2465/minerj.13.443
  locator: Complete official five-page scan, pages 443–447, Figures 1–3
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Reviewer visually read every original page because the scan has no extractable
    text. B-17 recipe, pH 8, aerobic 27 C incubation, up to 35 days, nine experiments
    per medium and phenotypic Acinetobacter sp. assignment agree with the record.
    One of 96 screened carbonate-forming isolates produces the target aggregates;
    20 others produce struvite.
  snapshot_sha256: 943b6fa5c973a987e2bf2d357375ce05d87f0e3fa40a88d2bb5295f259889446
- evidence_id: limits1987
  kind: primary_source
  reference: https://doi.org/10.2465/minerj.13.443
  locator: Page 444 control paragraph, separation-method referral and unmatched XRD
    peaks; pages 445–446 spectra/SEM
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: partial
  summary: The original names uninoculated and autoclaved-cell controls but gives
    no explicit outcome. It refers purification to the uninspected 1983 paper. Figure
    1 and text acknowledge unmatched reflections/intensity differences and impurities.
    Infrared/chemical analysis support a hydrated phosphate assignment without quantitative
    purity, authentic strain deposit or a controlled biochemical cause.
  snapshot_sha256: 943b6fa5c973a987e2bf2d357375ce05d87f0e3fa40a88d2bb5295f259889446
- evidence_id: metadata1987
  kind: database
  reference: https://api.crossref.org/works/10.2465/minerj.13.443
  locator: Retained Crossref metadata and original title/author/journal page
  accessed_at: '2026-10-14T08:31:49.125817Z'
  support: supports
  summary: Title, authors, DOI, year, volume 13(7) and pages 443–447 are consistent.
    No update-to entry or populated relation mapping appears in retained metadata.
  snapshot_sha256: 9ff2e16147559b5fba9df0842916c5329565983ca3905cf6fa546687b66cd3ce
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct hydrated phosphate mineral
  outcome: supported
  summary: The record uses the dated IMA identity, distinguishes the separate barićite
    species and does not inherit element or commodity criticality.
  target_ids:
  - cmmmech:bobierrite
  evidence_ids:
  - record
  - ima
  dimensions:
  - name: material_form
    value: Recovered culture precipitates assigned to bobierrite
    definition: The species owner is not an element, phosphate ion or mixed recovery
      commodity.
    evidence_ids:
    - ima
    - primary1987
    - primary2014
  - name: criticality
    value: No criticality claim
    definition: No jurisdiction/list/edition designation is asserted; omission is
      not universal noncritical status.
    evidence_ids:
    - record
- assessment_id: historical
  area: evidence
  topic: 1987 isolate, medium and control boundary
  outcome: supported
  summary: Historical culture-associated phase assignment is supported while purification,
    impurity, control-outcome and taxonomy limitations remain explicit.
  target_ids:
  - cmmmech:bobierrite
  evidence_ids:
  - record
  - primary1987
  - limits1987
  dimensions:
  - name: organism
    value: Phenotypic Acinetobacter sp. soil isolate
    definition: No exact species or deposited strain identity is established.
    evidence_ids:
    - primary1987
  - name: biomass_state
    value: Live inoculated cultures; dead-cell and uninoculated controls named
    definition: Control results are not reported, so a biological enhancement is not
      measured.
    evidence_ids:
    - limits1987
  - name: substrate_conditions
    value: Magnesium-acetate B-17; pH 8; aerobic 27 C; up to 35 days
    definition: Recipe and incubation are source-reported, with magnesium acetate
      hydration unspecified.
    evidence_ids:
    - primary1987
  - name: pretreatment
    value: Separation and purification referred to a 1983 method
    definition: Missing procedural original prevents exclusion of recovery-induced
      phase changes.
    evidence_ids:
    - limits1987
- assessment_id: later
  area: evidence
  topic: 2014 recovered agar phase and contradictory evidence
  outcome: supported
  summary: The second mechanism is a qualified recovered-phase observation. It preserves
    phase-label and sequence inconsistencies, source-dependent outcomes and the lack
    of isolate-specific phase attribution.
  target_ids:
  - cmmmech:bobierrite
  evidence_ids:
  - record
  - primary2014
  - limits2014
  dimensions:
  - name: controls
    value: Uninoculated and dead-cell cultures have no crystals; wastewater medium
      also negative
    definition: The negative wastewater result prevents extrapolation to actual wastewater
      mineral recovery.
    evidence_ids:
    - primary2014
  - name: processing
    value: Boiling-water agar recovery and drying at 37 C
    definition: Unchanged optical morphology does not prove unchanged hydrate structure.
    evidence_ids:
    - primary2014
    - limits2014
  - name: outcome
    value: Mixed spherulitic phosphate products assigned by source XRD
    definition: No phase-specific mass balance, purified yield or universal isolate
      capacity.
    evidence_ids:
    - limits2014
  - name: deployment
    value: Laboratory solid-media cultures from a bench reactor inoculum
    definition: Reactor organic-load removal is not deployment of phosphate recovery.
    evidence_ids:
    - primary2014
- assessment_id: provenance
  area: provenance
  topic: Identifiers, history and executed checks
  outcome: supported
  summary: Authoritative identities, exact record/history bytes and executed named/batch
    checks support the saved review. Literature completeness is not claimed.
  target_ids:
  - cmmmech:bobierrite
  evidence_ids:
  - ima
  - metadata1987
  - metadata2014
  - dedup
  - notices
  - history
  - named
  - batch
findings: []
actions: []
limitations:
- The 1983 crystal separation/purification procedure remains uninspected; handling
  effects cannot be excluded.
- The 1987 paper reports impurities and provides no explicit control outcomes, quantitative
  phase refinement or authentic strain accession.
- The 2014 phase-label, sequence-length and liquid-inoculum inconsistencies remain
  unresolved and are preserved in the record.
- Neither source establishes phase-specific recovery yield, unique biochemical cause
  or industrial deployment.
- The 1989 clinical bobierrite report and additional literature remain unassessed;
  notice searches are bounded.
notes:
- 'Findings by severity: zero blocker, major, minor or informational curation defects;
  scientific uncertainties are recorded as limitations rather than invented findings.'
- 'Corrections by reviewer: none. Scientific record and CREATE history remain identical
  to the inspect snapshot.'
- Raw copyrighted source originals and renderings remain outside Git. Review records
  the curator-acquired sources independently checked by this reviewer.
- Final structured review validation and exact current-record coverage remain coordinator
  publication gates.
tags:
- round66
- independent
- bobierrite
- primary-evidence
```
