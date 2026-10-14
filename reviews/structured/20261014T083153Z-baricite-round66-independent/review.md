# Independent scientific review of Barićite culture-associated phosphate evidence

- Review: 20261014T083153Z-baricite-round66-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T08:25:57.711655Z
- Finished UTC: 2026-10-14T08:31:53.689366Z
- Reviewer: codex /root/round66_magnesium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The G20 acetate/hydrogen experiment supports a narrowly stated barićite-assigned mixed-precipitate observation. The record preserves no net magnesium-removal advantage, phase and recipe conflicts, and missing causal measurements. No supported curation defect was found.

## Scope And Provenance

Field-by-field review of the single frozen mineral record, canonical CREATE history and its primary-source claims.

Selection: Assigned record from the round66 phosphate cohort; inspect captured the current Git base and target/context hashes before scientific assessment. Each sibling has a separate review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d57f45621cbe465eb13dfb6cc26cc4197d98f90e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:baricite | data/records/baricite.yaml | maintained | Barićite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:baricite | Reviewer executed the command; exit zero and original log retained. |
| Coordinator batch gate 1 | passed | True | cmmmech:baricite | Coordinator execution 2026-10-14T08:26:37.417759+00:00 to 2026-10-14T08:30:04.266682+00:00; reviewer checked actual outcomes and log digest. |
| Coordinator batch gate 2 | passed | True | cmmmech:baricite | Coordinator execution 2026-10-14T08:30:04.266767+00:00 to 2026-10-14T08:30:11.880507+00:00; reviewer checked actual outcomes and log digest. |
| Coordinator batch gate 3 | passed | True | cmmmech:baricite | Coordinator execution 2026-10-14T08:30:11.880596+00:00 to 2026-10-14T08:30:17.021271+00:00; reviewer checked actual outcomes and log digest. |

## Scientific And Domain Assessments

### Barićite identity and historical formula

identity: supported. Targets: cmmmech:baricite.

The current IMA species and approval number are distinct from the historical mixed Mg/Fe formula used for the experimental phase assignment. Neither a current ideal composition nor inherited criticality is asserted as measured.

### Strain, biomass, substrate and controls

evidence: supported. Targets: cmmmech:baricite.

The exact G20 strain mapping and source culture conditions are supported, with reactive iron, phosphate enrichment, unknown cell dose and source model discrepancies retained.

### Phase proportions, magnesium removal and model limits

quantity: supported. Targets: cmmmech:baricite.

Rietveld phase proportions are represented as fitted assemblage composition. The source does not establish enhanced magnesium removal, phase-pure recovery, biochemical necessity or natural/industrial deployment.

### 2014 study is context, not replication

evidence: supported. Targets: cmmmech:baricite.

The agar-culture report uses another inoculum and processing method and contains a conflicting phase label. The record correctly declines to treat it as replication of the G20 system.

### Identifiers, history and executed checks

provenance: supported. Targets: cmmmech:baricite.

Authoritative identity, taxonomy, DOI metadata, exact record/history bytes and executed checks support the saved review. Search completeness is not claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/baricite.yaml; Entire inspected, frozen record | supports | Reviewer independently read every field and compared claims to primary originals. Record and linked CREATE history remain byte-identical to the pre-assessment inspect capture. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 edition, pages 1–2 definitions, page 20 barićite and page 27 bobierrite | supports | Both mineral rows were visually inspected and field definitions reread. Both approved formulas are Mg3(PO4)2(H2O)8, but they remain separate named mineral species. Barićite has approval number 1975-027; bobierrite is grandfathered with original-description year 1868. |
| primary2014 | https://doi.org/10.3390/ijerph110403689; Complete scientific text, Sections 2–4; all five main figures and Tables 1–3 | partial | Independent read of the retained complete publisher PDF and visual check of all figures/tables. The reactor supplies isolated bacteria; phase formation occurs in artificial agar. Six of twelve selected isolates produce spherulites, without an individual bobierrite/barićite phase map. Boiling-water agar recovery and drying precede XRD; no-crystal controls and wastewater-medium negative outcomes are reported. |
| limits2014 | https://doi.org/10.3390/ijerph110403689; Sections 2.4–2.7; Table 2; Table 3; Figures 3–5 | partial | Figure 5 labels a magnesium-phosphate dihydrate instead of the octahydrate companion assigned in Figure 4/text. XRD is an intensity map and EDX does not establish hydration. The 650-nt/200-nt sequence lengths, strain-12 identity discrepancy and biofilm-suspension versus strain-row liquid experiments are visible source limitations. No confirmed molecular mechanism or industrial phosphate recovery follows. |
| metadata2014 | https://api.crossref.org/works/10.3390/ijerph110403689; Retained DOI metadata and original publisher PDF page 1 | supports | Title, DOI, 2014 publication and source identity agree. Retained metadata contains no update-to entry and an empty relation mapping; this does not prove universal notice absence. |
| dedup | /private/tmp/cmm-round66-baricite-review-dedup.txt; Independent scoped repository search, including hidden and ignored files and followed links | context_only | Search finds the round65 source handoff, both sibling mineral records and current dossier/history. The studies were already prioritized; they are not presented as newly discovered. Within maintained records the target is a distinct species owner, not a duplicate mineral or elemental record. |
| notices | https://doi.org/10.1016/j.chemgeo.2016.04.022; Reviewer live web searches on 2026-10-14 UTC and retained Crossref metadata | context_only | No affecting correction or retraction was identified in the bounded returned sets. Results include the primary publisher/PMC pages and a 1989 clinical bobierrite study, retained as an unassessed lead. New evidence does not remove the explicitly retained source inconsistencies. Direct J-STAGE and NCBI browser opens returned tool errors; the retained official original scan and same-day NCBI XML were used instead. |
| history | history/records/baricite/2026-10-14T081704Z-codex-5fa318.yaml; Complete canonical CREATE session and linked inline event | supports | Actual codex / GPT-6 CREATE history has the correct target, UTC timestamp, actor and evidence-bounded summary. Independent reviewer authored neither the scientific record nor its CREATE history. |
| named | /private/tmp/cmm-round66-baricite-review-validation.log; Entire reviewer-run named validation log | supports | Locked offline named record validation exited zero: Checked 1 record(s); 0 failed. |
| batch | /private/tmp/cmm-round66-final-gates.json; Coordinator command receipts and retained log SHA256 | supports | Actual just check, explicit nonempty corpus validation and trusted-base history validation passed. Reviewer verified receipt outcomes and log hash before saving the positive verdict. |
| primary2016 | https://doi.org/10.1016/j.chemgeo.2016.04.022; Complete retained 12-page author manuscript, scientific Sections 2–4, Tables 1–3 and all three main figures | supports | Methods/results/discussion were independently read and all main figures visually inspected. Hydrogen-purged, acetate-containing G20 cultures at 25 C for 10 months produce the XRD-assigned mixed phosphate assemblage; sterile counterparts predominantly retain amorphous material and calcite. Table 2 assigns barićite 30.6 and 27.8 wt% of fitted mineral assemblages, not recovery yield. |
| limits2016 | https://doi.org/10.1016/j.chemgeo.2016.04.022; Main Table 2 and Sections 2.4, 3.1–3.2, 4.2–4.3; Figure 1c-d | partial | Similar magnesium depletion in sterile and inoculated acetate medium precludes a net microbial-removal advantage. Sulfate/sulfide, growth, DIC and phosphate depletion were not measured; endpoint alkalinity has one bottle per condition. The iron nail and pre-existing white solids are explicit. Phosphate crystal SEM is data not shown and not further characterized, preventing an independent phase-specific Mg/Fe composition claim. |
| si_table1 | https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc1.docx; Entire official SI Table 1 OOXML table, including row/column structure | partial | Reviewer parsed the original table, confirming phosphate 0.089 mM versus 0.89 mM in main Table 1, iron 4.00E-04 versus 0.0009 mM and formate sodium 757.7 versus 575.7 mM. Model inputs cannot silently substitute for the experimental recipe. |
| si_other_tables | https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc2.docx; Entire SI Tables 2 and 3, retained DOCX files mmc2 and mmc3 | context_only | Table 2 microscopy/EDS concerns the formate arm, not acetate barićite crystals. Table 3 reports modeled complexation ratios. Neither establishes barićite crystal purity or measured recovery. |
| si_fig1 | https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc4.docx; SI Figure 1, both concentration panels and caption | partial | Original embedded chart visually inspected. Acetate magnesium depletion is comparable under sterile and inoculated conditions; graph agrees with main Table 2 and the conservative record. |
| si_models | https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc5.docx; SI Figure 2 formate/acetate panels; SI Figure 3 all panels and captions in mmc6 | context_only | Embedded relevant model plots visually inspected. Saturation ratios and predicted pH are model results, not direct phase occurrence or measured sulfate reduction. The lactate-only Figure 2 EMF panel was not rendered; it is outside the accepted acetate-arm claim. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=207559&amp;mode=Info; Same-day retained official taxonomy XML Taxon 207559 | supports | Reviewer inspected TaxId, ScientificName, Rank, ParentTaxId and EquivalentName: Oleidesulfovibrio alaskensis G20, strain rank, parent species 58180, historical equivalent Desulfovibrio alaskensis G20. This supports the exact recorded strain CURIE. |
| metadata2016 | https://api.crossref.org/works/10.1016/j.chemgeo.2016.04.022; Retained Crossref metadata, author manuscript cover and live publisher landing | supports | DOI, title, authors and Chemical Geology 435:49–59 agree. Publisher issue is October 2016; the repository cover mentions April acceptance/publication context, but the record correctly uses year 2016 without adopting an inconsistent month. |

## Limits And Additional Notes

- The accepted evidence is the retained author manuscript and official supplements; an independently compared final publisher PDF and raw Rietveld data were not inspected.
- Experimental barićite composition is source-assigned from mixed-powder XRD, not independent Mg/Fe analysis of isolated crystals.
- Main/SI recipe inputs and the decahydrate formula conflict remain unresolved and explicit in the record.
- No sulfate, sulfide, growth, DIC or phosphate-depletion measurement isolates a biochemical cause; matched-pH controls are absent.
- Similar sterile magnesium depletion precludes a net-removal advantage; no phase-specific mass balance, purified product or industrial deployment is shown.
- The lactate-only SI Figure 2 EMF panel was not rendered because that arm is outside the accepted claim; all relevant acetate evidence was inspected.
- Correction/retraction and conflicting-evidence searches are bounded, not a claim of literature completeness.
- Findings by severity: zero blocker, major, minor or informational curation defects; scientific uncertainties are recorded as limitations rather than invented findings.
- Corrections by reviewer: none. Scientific record and CREATE history remain identical to the inspect snapshot.
- Raw copyrighted source originals and renderings remain outside Git. Review records the curator-acquired sources independently checked by this reviewer.
- Final structured review validation and exact current-record coverage remain coordinator publication gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T083153Z-baricite-round66-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Barićite culture-associated phosphate evidence
started_at: '2026-10-14T08:25:57.711655Z'
finished_at: '2026-10-14T08:31:53.689366Z'
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
summary: The G20 acetate/hydrogen experiment supports a narrowly stated barićite-assigned
  mixed-precipitate observation. The record preserves no net magnesium-removal advantage,
  phase and recipe conflicts, and missing causal measurements. No supported curation
  defect was found.
source:
  git_revision: d57f45621cbe465eb13dfb6cc26cc4197d98f90e
  state: working_tree
  inputs:
  - path: data/records/baricite.yaml
    sha256: 8d0b77267485c73ab254b440c3f32c4322bd1d8dd46c48d212c316ef2eebe7ed
    role: target
  - path: history/records/baricite/2026-10-14T081704Z-codex-5fa318.yaml
    sha256: 107353cae53692e3ccc2d9ab83a548451c71ae3425f9c58ee0e46a182b10c54c
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
  - cmmmech:baricite
  exclusions:
  - target: Additional uncurated phosphate literature and unrelated experimental arms
    reason: Not part of the accepted record claims; bounded handoffs and evidence
      access limits remain explicit.
targets:
- target_id: cmmmech:baricite
  path: data/records/baricite.yaml
  label: Barićite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/baricite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/baricite.yaml
  status: passed
  required: true
  summary: Reviewer executed the command; exit zero and original log retained.
  target_ids:
  - cmmmech:baricite
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
  - cmmmech:baricite
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
  - cmmmech:baricite
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
  - cmmmech:baricite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/baricite.yaml
  locator: Entire inspected, frozen record
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: Reviewer independently read every field and compared claims to primary
    originals. Record and linked CREATE history remain byte-identical to the pre-assessment
    inspect capture.
  snapshot_sha256: 8d0b77267485c73ab254b440c3f32c4322bd1d8dd46c48d212c316ef2eebe7ed
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 edition, pages 1–2 definitions, page 20 barićite and page
    27 bobierrite
  accessed_at: '2026-10-14T08:31:53.689366Z'
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
  accessed_at: '2026-10-14T08:31:53.689366Z'
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
  accessed_at: '2026-10-14T08:31:53.689366Z'
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
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: Title, DOI, 2014 publication and source identity agree. Retained metadata
    contains no update-to entry and an empty relation mapping; this does not prove
    universal notice absence.
  snapshot_sha256: c884b761b39692d8cde2dff5fb7b7e687eacfd50068620c29f7f03ab0c169d2c
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round66-baricite-review-dedup.txt
  locator: Independent scoped repository search, including hidden and ignored files
    and followed links
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: context_only
  summary: Search finds the round65 source handoff, both sibling mineral records and
    current dossier/history. The studies were already prioritized; they are not presented
    as newly discovered. Within maintained records the target is a distinct species
    owner, not a duplicate mineral or elemental record.
  search_scope: rg --no-ignore --hidden --follow -n -i across data/records, research,
    history and reviews; queries include the species spelling, barićite accent variant
    where relevant, and the primary DOI. No machinewide absence claim.
  snapshot_sha256: 8ac77915cc0195ba8fc0061edc97021c33bc70fad4d76cce6752d5b1d144bb11
- evidence_id: notices
  kind: search
  reference: https://doi.org/10.1016/j.chemgeo.2016.04.022
  locator: Reviewer live web searches on 2026-10-14 UTC and retained Crossref metadata
  accessed_at: '2026-10-14T08:31:53.689366Z'
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
  reference: history/records/baricite/2026-10-14T081704Z-codex-5fa318.yaml
  locator: Complete canonical CREATE session and linked inline event
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: Actual codex / GPT-6 CREATE history has the correct target, UTC timestamp,
    actor and evidence-bounded summary. Independent reviewer authored neither the
    scientific record nor its CREATE history.
  snapshot_sha256: 107353cae53692e3ccc2d9ab83a548451c71ae3425f9c58ee0e46a182b10c54c
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round66-baricite-review-validation.log
  locator: Entire reviewer-run named validation log
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: 'Locked offline named record validation exited zero: Checked 1 record(s);
    0 failed.'
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round66-final-gates.json
  locator: Coordinator command receipts and retained log SHA256
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: Actual just check, explicit nonempty corpus validation and trusted-base
    history validation passed. Reviewer verified receipt outcomes and log hash before
    saving the positive verdict.
  snapshot_sha256: f770d6a65bb5b55e55ec2ef08ddfa02330dab31a1f87a26af94b2b92150a28dc
- evidence_id: primary2016
  kind: primary_source
  reference: https://doi.org/10.1016/j.chemgeo.2016.04.022
  locator: Complete retained 12-page author manuscript, scientific Sections 2–4, Tables
    1–3 and all three main figures
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: Methods/results/discussion were independently read and all main figures
    visually inspected. Hydrogen-purged, acetate-containing G20 cultures at 25 C for
    10 months produce the XRD-assigned mixed phosphate assemblage; sterile counterparts
    predominantly retain amorphous material and calcite. Table 2 assigns barićite
    30.6 and 27.8 wt% of fitted mineral assemblages, not recovery yield.
  snapshot_sha256: e64eb5018f28d503a0f065a8cf98f1bf09e2ae165558654b546e7a002eb9f602
- evidence_id: limits2016
  kind: primary_source
  reference: https://doi.org/10.1016/j.chemgeo.2016.04.022
  locator: Main Table 2 and Sections 2.4, 3.1–3.2, 4.2–4.3; Figure 1c-d
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: partial
  summary: Similar magnesium depletion in sterile and inoculated acetate medium precludes
    a net microbial-removal advantage. Sulfate/sulfide, growth, DIC and phosphate
    depletion were not measured; endpoint alkalinity has one bottle per condition.
    The iron nail and pre-existing white solids are explicit. Phosphate crystal SEM
    is data not shown and not further characterized, preventing an independent phase-specific
    Mg/Fe composition claim.
  snapshot_sha256: e64eb5018f28d503a0f065a8cf98f1bf09e2ae165558654b546e7a002eb9f602
- evidence_id: si_table1
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc1.docx
  locator: Entire official SI Table 1 OOXML table, including row/column structure
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: partial
  summary: Reviewer parsed the original table, confirming phosphate 0.089 mM versus
    0.89 mM in main Table 1, iron 4.00E-04 versus 0.0009 mM and formate sodium 757.7
    versus 575.7 mM. Model inputs cannot silently substitute for the experimental
    recipe.
  snapshot_sha256: dc4edc14be0a33217a5fc53dde4e1af56f6550ab8beae612e5074bce791518cb
- evidence_id: si_other_tables
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc2.docx
  locator: Entire SI Tables 2 and 3, retained DOCX files mmc2 and mmc3
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: context_only
  summary: Table 2 microscopy/EDS concerns the formate arm, not acetate barićite crystals.
    Table 3 reports modeled complexation ratios. Neither establishes barićite crystal
    purity or measured recovery.
  snapshot_sha256: 744387318917e8b952430a10fdb9b6539518b3eb68b526c51619a357e2246aa3
- evidence_id: si_fig1
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc4.docx
  locator: SI Figure 1, both concentration panels and caption
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: partial
  summary: Original embedded chart visually inspected. Acetate magnesium depletion
    is comparable under sterile and inoculated conditions; graph agrees with main
    Table 2 and the conservative record.
  snapshot_sha256: c55bb7fdc4851d7acae85b5a4522ee7a9d70efb5be50221552509c41d860b6e0
- evidence_id: si_models
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0009254116302042-mmc5.docx
  locator: SI Figure 2 formate/acetate panels; SI Figure 3 all panels and captions
    in mmc6
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: context_only
  summary: Embedded relevant model plots visually inspected. Saturation ratios and
    predicted pH are model results, not direct phase occurrence or measured sulfate
    reduction. The lactate-only Figure 2 EMF panel was not rendered; it is outside
    the accepted acetate-arm claim.
  snapshot_sha256: e7a37c9d06182b37d29fcf9b46118401f71afba5aa9d537c1dc6c0d4f7434432
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=207559&mode=Info
  locator: Same-day retained official taxonomy XML Taxon 207559
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: 'Reviewer inspected TaxId, ScientificName, Rank, ParentTaxId and EquivalentName:
    Oleidesulfovibrio alaskensis G20, strain rank, parent species 58180, historical
    equivalent Desulfovibrio alaskensis G20. This supports the exact recorded strain
    CURIE.'
  snapshot_sha256: 8eda5ac3d43623188cc04d5ff058388ef97ecea1d5d1fcb1d9a644d1303a8486
- evidence_id: metadata2016
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.chemgeo.2016.04.022
  locator: Retained Crossref metadata, author manuscript cover and live publisher
    landing
  accessed_at: '2026-10-14T08:31:53.689366Z'
  support: supports
  summary: DOI, title, authors and Chemical Geology 435:49–59 agree. Publisher issue
    is October 2016; the repository cover mentions April acceptance/publication context,
    but the record correctly uses year 2016 without adopting an inconsistent month.
  snapshot_sha256: 96bed78b1ee69cf9701f5a29bf4b04f02e8a88766448fca7a88ebb4f90c39a74
assessments:
- assessment_id: identity
  area: identity
  topic: Barićite identity and historical formula
  outcome: supported
  summary: The current IMA species and approval number are distinct from the historical
    mixed Mg/Fe formula used for the experimental phase assignment. Neither a current
    ideal composition nor inherited criticality is asserted as measured.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - record
  - ima
  - primary2016
  dimensions:
  - name: material_form
    value: Mixed recovered phosphate solids assigned by XRD to barićite
    definition: A mineral owner distinct from bobierrite and constituent elements;
      not a pure recovery commodity.
    evidence_ids:
    - ima
    - primary2016
  - name: criticality
    value: No criticality claim
    definition: No jurisdiction/list/edition designation is asserted.
    evidence_ids:
    - record
- assessment_id: conditions
  area: evidence
  topic: Strain, biomass, substrate and controls
  outcome: supported
  summary: The exact G20 strain mapping and source culture conditions are supported,
    with reactive iron, phosphate enrichment, unknown cell dose and source model discrepancies
    retained.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - record
  - taxonomy
  - primary2016
  - limits2016
  - si_table1
  dimensions:
  - name: organism
    value: Oleidesulfovibrio alaskensis G20, NCBITaxon:207559
    definition: Current exact strain name corresponding to historical Desulfovibrio
      alaskensis G20.
    evidence_ids:
    - taxonomy
    - primary2016
  - name: biomass_state
    value: Live inoculum, two drops per bottle
    definition: Drop volume and cell density are unspecified.
    evidence_ids:
    - primary2016
  - name: substrate_conditions
    value: 100 mL nutrient-enriched medium in 120 mL serum bottles; H2 purge; 47 mM
      acetate; 25 C; 10 months
    definition: Recipe contains an iron nail, elevated phosphate and magnesium; this
      is a synthetic laboratory system.
    evidence_ids:
    - primary2016
  - name: controls
    value: Duplicate sterile and duplicate inoculated acetate bottles
    definition: No matched-pH or cell-free-metabolite controls; alkalinity has one
      endpoint bottle per condition.
    evidence_ids:
    - primary2016
    - limits2016
  - name: pretreatment
    value: Filtration and overnight 30 C drying in nitrogen
    definition: Recovered solids were analyzed within one week; in-culture hydrate
      state was not directly measured.
    evidence_ids:
    - primary2016
- assessment_id: outcome
  area: quantity
  topic: Phase proportions, magnesium removal and model limits
  outcome: supported
  summary: Rietveld phase proportions are represented as fitted assemblage composition.
    The source does not establish enhanced magnesium removal, phase-pure recovery,
    biochemical necessity or natural/industrial deployment.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - record
  - primary2016
  - limits2016
  - si_table1
  - si_fig1
  - si_models
  dimensions:
  - name: phase_proportions
    value: 30.6 and 27.8 wt% barićite in the reported fitted mineral assemblages
    definition: Samples 1_103 and 2_35; fitted composition with rounding and no confidence
      intervals, not element recovery percentages.
    evidence_ids:
    - primary2016
  - name: outcome
    value: Culture-associated phase selection without net magnesium-removal advantage
    definition: Sterile and inoculated magnesium depletion is similar.
    evidence_ids:
    - limits2016
    - si_fig1
  - name: deployment
    value: Laboratory synthetic marine pore-water medium
    definition: No cold-seep field formation, fertilizer performance or industrial
      process is established.
    evidence_ids:
    - primary2016
    - record
- assessment_id: context
  area: evidence
  topic: 2014 study is context, not replication
  outcome: supported
  summary: The agar-culture report uses another inoculum and processing method and
    contains a conflicting phase label. The record correctly declines to treat it
    as replication of the G20 system.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - primary2014
  - limits2014
  - record
- assessment_id: provenance
  area: provenance
  topic: Identifiers, history and executed checks
  outcome: supported
  summary: Authoritative identity, taxonomy, DOI metadata, exact record/history bytes
    and executed checks support the saved review. Search completeness is not claimed.
  target_ids:
  - cmmmech:baricite
  evidence_ids:
  - metadata2016
  - metadata2014
  - taxonomy
  - history
  - named
  - batch
  - dedup
  - notices
findings: []
actions: []
limitations:
- The accepted evidence is the retained author manuscript and official supplements;
  an independently compared final publisher PDF and raw Rietveld data were not inspected.
- Experimental barićite composition is source-assigned from mixed-powder XRD, not
  independent Mg/Fe analysis of isolated crystals.
- Main/SI recipe inputs and the decahydrate formula conflict remain unresolved and
  explicit in the record.
- No sulfate, sulfide, growth, DIC or phosphate-depletion measurement isolates a biochemical
  cause; matched-pH controls are absent.
- Similar sterile magnesium depletion precludes a net-removal advantage; no phase-specific
  mass balance, purified product or industrial deployment is shown.
- The lactate-only SI Figure 2 EMF panel was not rendered because that arm is outside
  the accepted claim; all relevant acetate evidence was inspected.
- Correction/retraction and conflicting-evidence searches are bounded, not a claim
  of literature completeness.
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
- baricite
- primary-evidence
```
