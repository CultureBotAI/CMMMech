# Independent scientific review of spent NdFeB permanent magnets

- Review: 20261011T093449Z-spent-ndfeb-magnets-round14-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T09:28:59Z
- Finished UTC: 2026-10-11T09:34:49Z
- Reviewer: Codex /root/round14_resources (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supported distinct secondary-resource identity and narrowly scoped inactive-algal biosorption evidence. No actionable findings; source limitations and contradictory statements remain explicit.

## Scope And Provenance

Full scientific and provenance review of one new record and its final working-tree state.

Selection: Root-assigned new secondary-resource record; no sampling within its fields.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-ndfeb-magnets | data/records/spent-ndfeb-magnets.yaml | maintained | Spent NdFeB permanent magnets |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named scientific-record structural validation | passed | True | cmmmech:spent-ndfeb-magnets | Reviewer executed and read terminal-zero output: 1 record checked, 0 failed; /private/tmp/cmm-round14-magnet-review/named-validation.log. |
| Native full batch checks before FCC wording correction | passed | True | cmmmech:spent-ndfeb-magnets | Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending; this gate covers other unchanged targets. |
| Required corpus | passed | True | cmmmech:spent-ndfeb-magnets | Terminal0 session1358:119records,0failed. /private/tmp/cmm-round14-require.log |
| Trusted-base history | passed | True | cmmmech:spent-ndfeb-magnets | Terminal0 session1358:134histories,0errors. /private/tmp/cmm-round14-history.log |

## Scientific And Domain Assessments

### Resource identity, original feed and criticality boundaries

identity: supported. Targets: cmmmech:spent-ndfeb-magnets.

Spent NdFeB magnets are a secondary-resource class, distinct from the element, fixed-purity Nd2Fe14B and broader magnet-feed commodity groups. A separate primary paper grounds end-of-life identity; Kucuker's less precise feed provenance is openly limited. No criticality or external waste identifier is invented.

### Pretreatment, inactive biomass and laboratory outcome

evidence: supported. Targets: cmmmech:spent-ndfeb-magnets.

The narrow biosorption claim is supported. Thermal/acid preparation occurs before biomass contact, and the dried algae do not establish metabolic leaching. Primary text and exact supplement cells agree with the scoped endpoint; experimental and fitted uptake are separate. Pilot cultivation of biomass does not show pilot recovery.

### Adversarial controls, precipitation and model contradictions

evidence: supported. Targets: cmmmech:spent-ndfeb-magnets.

Missing matched blank and phase localization limit mechanistic attribution. The record retains sub-detection limits without numerical zeros, 50-degree-C precipitation/value tension and nonuniform kinetic fits. It does not claim untreated multimetal selectivity, a unique binding group, complete mass balance or commercial deployment. These are honest source limits, not actionable defects in the bounded record.

### Actual CREATE history and exact reviewed working bytes

provenance: supported. Targets: cmmmech:spent-ndfeb-magnets.

Actual GPT-6/codex sidecar targets the record and links issue 56; separate inline event describes current creation. Trusted base is merged main; exact source inputs remain unchanged after review. New resource representation reuses an experiment transparently.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/spent-ndfeb-magnets.yaml; Complete frozen target, linked CREATE sidecar and native schema | supports | Inspected before judgment at merged-main base 8f8abed with actual working-tree provenance. Reviewed scientific and history fields; target hash remains exact. Reviewer did not author or edit this record. |
| identity | https://doi.org/10.1039/C5GC00230C; Riano and Binnemans 2015, printed pp.2932-2933; end-of-life feed, University of Birmingham provenance, Table 1 and selective leaching methods | supports | Independently read retained originating-laboratory PDF, acquired by curator this round. Supports heterogeneous end-of-life NdFeB material identity; its chemical separation and product claims are not attributed to microbial treatment. Actual Kucuker feed history remains less precise. |
| paper | https://doi.org/10.1371/journal.pone.0175255; Kucuker et al. 2017, Methods pp.2-4, Eq.1, Figures 1-3, Table 1, Results pp.5-9 and Conclusion p.10 | supports | Independently reread retained full publisher PDF/HTML; visually inspected rendered pages 3, 6 and 8. Confirmed 950-degree-C roasting, nitric-acid preparation, 90-degree-C dried algae, 0.2-L laboratory assays, 90 minutes, 300 rpm, duplicates and scoped 35-degree-C endpoint. Uptake uses filtered-solution depletion, with no matched time-course blank or quantified isolated product reported in the inspected methods/results. |
| supplement | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0175255.s001&amp;type=supplementary; Original XLSX sheet1 XML; Tabelle1 merged A83:A86, B83:B86, C83:C86; D86, E86, J86, K100, K121 | supports | Independently parsed original ZIP/XML without editing or recalculating. Condition 35 degrees C, pH 5, 0.5 g/L and 250 mg Nd/L: E86 raw 157.39840000000004, J86 raw 161.29032258064515 mg/g. K100=0.72030000000000005 and K121=0.96350000000000002 challenge universal R-squared wording. Table 1 article capacity 188.68 mg/g is separately identified as fitted. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3077&amp;retmode=xml; Taxon 3077; ScientificName, Rank and type-culture context | supports | Independently read this round's retained NCBI export: Chlorella vulgaris at species rank. Species ID does not authenticate exact outdoor-grown assay biomass. |
| strain | https://sagdb.uni-goettingen.de/detailedList.php?str_number=211-12; SAG strain number, genus/species and Axenic field | supports | Independently read retained catalogue page: 211-12 identifies Chlorella vulgaris and catalogue states axenic. Record appropriately avoids translating catalogue status into independent confirmation of experimental outdoor-culture purity. |
| search | /private/tmp/cmm-round14-magnet-review/dedup.txt; Local scientific corpus, current raw evidence, existing neodymium record and saved reviews; first web-query results | context_only | Ignored-inclusive followed search confirms shared Kucuker experiment already under neodymium and distinct resource/commodity boundaries. Exact PLOS DOI correction/retraction, Riano DOI correction and biosorption precipitation/control searches returned original sources and related leads, without an applicable notice in this bounded window. No machine-wide absence or exhaustive literature conclusion. |
| gates | /private/tmp/cmm-round14-magnet-review/gate-checks.json; Named reviewer command plus root final native, require-records and trusted-base-history receipts | supports | Reviewer read actual completed command receipts and logs, separately supplied from parent execution. Offline gates support structural acceptance, not causal scientific truth. |

## Limits And Additional Notes

- The specific magnet source has incomplete device/collection history; separate used-magnet identity context does not repair that gap.
- Solution depletion with no matched blank or direct phase/localization evidence cannot establish a unique binding mechanism or original-feed product recovery.
- Full text and authorities were independently read from retained copies freshly acquired by the curator this round; reviewer did not describe these as independent downloads.
- Correction/counterevidence search is bounded to listed queries and returned results; no exhaustive clearance or corpus-wide scientific conclusion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T093449Z-spent-ndfeb-magnets-round14-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of spent NdFeB permanent magnets
started_at: '2026-10-11T09:28:59Z'
finished_at: '2026-10-11T09:34:49Z'
reviewer:
  identity: Codex /root/round14_resources
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this magnet record; this separate agent authored
    other resource records only and made no edits to the target. Reviewer independently
    inspected primary text, figures, original workbook cells, authorities and exact
    record/history bytes. Shared-team record-author independence, not organizational
    independence.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supported distinct secondary-resource identity and narrowly scoped inactive-algal
  biosorption evidence. No actionable findings; source limitations and contradictory
  statements remain explicit.
source:
  git_revision: 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  state: working_tree
  inputs:
  - path: data/records/spent-ndfeb-magnets.yaml
    sha256: 9a55438ef82ebcb1a7568878377e0ccb9c5762e2370f154b2c76902ad8c34697
    role: target
  - path: history/records/spent-ndfeb-magnets/2026-10-11T092622Z-codex-65cd7d.yaml
    sha256: 3fc49aa7b9b0f281470a9ff32466a055df4de76171faed7d018cdd0b55a777b7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: Full scientific and provenance review of one new record and its final
    working-tree state.
  selection: Root-assigned new secondary-resource record; no sampling within its fields.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-ndfeb-magnets
  exclusions:
  - target: Other records and uncurated mechanisms
    reason: Existing neodymium evidence checked for duplication only; no blanket re-review
      or literature census.
targets:
- target_id: cmmmech:spent-ndfeb-magnets
  path: data/records/spent-ndfeb-magnets.yaml
  label: Spent NdFeB permanent magnets
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-ndfeb-magnets.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Named scientific-record structural validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/spent-ndfeb-magnets.yaml
  status: passed
  required: true
  summary: 'Reviewer executed and read terminal-zero output: 1 record checked, 0 failed;
    /private/tmp/cmm-round14-magnet-review/named-validation.log.'
  target_ids:
  - cmmmech:spent-ndfeb-magnets
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full batch checks before FCC wording correction
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal0 session53639:307 passed,3 skipped in80.06s;119records,134histories
    valid. Log /private/tmp/cmm-round14-check.log. FCC wording correction pending;
    this gate covers other unchanged targets.
  target_ids:
  - cmmmech:spent-ndfeb-magnets
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal0 session1358:119records,0failed. /private/tmp/cmm-round14-require.log
  target_ids:
  - cmmmech:spent-ndfeb-magnets
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 8f8abedfce68f932e4f6f333a5470ee5f3897ff4
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal0 session1358:134histories,0errors. /private/tmp/cmm-round14-history.log
  target_ids:
  - cmmmech:spent-ndfeb-magnets
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/spent-ndfeb-magnets.yaml
  locator: Complete frozen target, linked CREATE sidecar and native schema
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: Inspected before judgment at merged-main base 8f8abed with actual working-tree
    provenance. Reviewed scientific and history fields; target hash remains exact.
    Reviewer did not author or edit this record.
  snapshot_sha256: 9a55438ef82ebcb1a7568878377e0ccb9c5762e2370f154b2c76902ad8c34697
- evidence_id: identity
  kind: primary_source
  reference: https://doi.org/10.1039/C5GC00230C
  locator: Riano and Binnemans 2015, printed pp.2932-2933; end-of-life feed, University
    of Birmingham provenance, Table 1 and selective leaching methods
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: Independently read retained originating-laboratory PDF, acquired by curator
    this round. Supports heterogeneous end-of-life NdFeB material identity; its chemical
    separation and product claims are not attributed to microbial treatment. Actual
    Kucuker feed history remains less precise.
  snapshot_sha256: 4a90583354b8bb69d315299347768e640f2f6c85de40b901261589dcae56bfe4
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0175255
  locator: Kucuker et al. 2017, Methods pp.2-4, Eq.1, Figures 1-3, Table 1, Results
    pp.5-9 and Conclusion p.10
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: Independently reread retained full publisher PDF/HTML; visually inspected
    rendered pages 3, 6 and 8. Confirmed 950-degree-C roasting, nitric-acid preparation,
    90-degree-C dried algae, 0.2-L laboratory assays, 90 minutes, 300 rpm, duplicates
    and scoped 35-degree-C endpoint. Uptake uses filtered-solution depletion, with
    no matched time-course blank or quantified isolated product reported in the inspected
    methods/results.
  snapshot_sha256: 91d132bd435d80db3114c1d8a784aa2d9faaf9f70cacdf9e62694ddcbb004f5d
- evidence_id: supplement
  kind: primary_source
  reference: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0175255.s001&type=supplementary
  locator: Original XLSX sheet1 XML; Tabelle1 merged A83:A86, B83:B86, C83:C86; D86,
    E86, J86, K100, K121
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: 'Independently parsed original ZIP/XML without editing or recalculating.
    Condition 35 degrees C, pH 5, 0.5 g/L and 250 mg Nd/L: E86 raw 157.39840000000004,
    J86 raw 161.29032258064515 mg/g. K100=0.72030000000000005 and K121=0.96350000000000002
    challenge universal R-squared wording. Table 1 article capacity 188.68 mg/g is
    separately identified as fitted.'
  snapshot_sha256: c39aa21b9bcebd6009658eb7e15cb4be4d7bc62d9f6cdfe6f506d146d2f8c074
- evidence_id: taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3077&retmode=xml
  locator: Taxon 3077; ScientificName, Rank and type-culture context
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: 'Independently read this round''s retained NCBI export: Chlorella vulgaris
    at species rank. Species ID does not authenticate exact outdoor-grown assay biomass.'
  snapshot_sha256: 62685f6909ce3b6d9b9ebf7eb2c78a316539c39bf524e96c51e736f20f94b0c9
- evidence_id: strain
  kind: authority
  reference: https://sagdb.uni-goettingen.de/detailedList.php?str_number=211-12
  locator: SAG strain number, genus/species and Axenic field
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: 'Independently read retained catalogue page: 211-12 identifies Chlorella
    vulgaris and catalogue states axenic. Record appropriately avoids translating
    catalogue status into independent confirmation of experimental outdoor-culture
    purity.'
  snapshot_sha256: 98f993b964d4b51788760af8c64822024f6b73ce03947b1517c5c8bc3256ae2b
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round14-magnet-review/dedup.txt
  locator: Local scientific corpus, current raw evidence, existing neodymium record
    and saved reviews; first web-query results
  accessed_at: '2026-10-11T09:34:49Z'
  support: context_only
  summary: Ignored-inclusive followed search confirms shared Kucuker experiment already
    under neodymium and distinct resource/commodity boundaries. Exact PLOS DOI correction/retraction,
    Riano DOI correction and biosorption precipitation/control searches returned original
    sources and related leads, without an applicable notice in this bounded window.
    No machine-wide absence or exhaustive literature conclusion.
  snapshot_sha256: 43a212e7748d5150549bacfeadf581206d53d08ecb0ed667d85bd5d7cc512207
  search_scope: 'rg --no-ignore --hidden --follow -n -i 0175255|C5GC00230C|spent-ndfeb|hard.disk.*magnet
    across data/records, research, reviews, history and /private/tmp/cmm-round14-magnet-raw.
    Web queries: "10.1371/journal.pone.0175255" correction retraction; "Biosorption
    of neodymium" "Chlorella" precipitation control; "10.1039/C5GC00230C" correction.
    No filters or pagination.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round14-magnet-review/gate-checks.json
  locator: Named reviewer command plus root final native, require-records and trusted-base-history
    receipts
  accessed_at: '2026-10-11T09:34:49Z'
  support: supports
  summary: Reviewer read actual completed command receipts and logs, separately supplied
    from parent execution. Offline gates support structural acceptance, not causal
    scientific truth.
  snapshot_sha256: ae991796336ef4a3c164df0b4a9f419a4dbff08de725e95c6ac5b7d4105a7694
assessments:
- assessment_id: identity
  area: identity
  topic: Resource identity, original feed and criticality boundaries
  outcome: supported
  summary: Spent NdFeB magnets are a secondary-resource class, distinct from the element,
    fixed-purity Nd2Fe14B and broader magnet-feed commodity groups. A separate primary
    paper grounds end-of-life identity; Kucuker's less precise feed provenance is
    openly limited. No criticality or external waste identifier is invented.
  target_ids:
  - cmmmech:spent-ndfeb-magnets
  evidence_ids:
  - identity
  - target
  - search
  dimensions:
  - name: material_form
    value: Used NdFeB permanent-magnet material
    definition: Variable alloy/coating/impurity feed, not an elemental or fixed-purity
      compound identity.
    evidence_ids:
    - identity
    - paper
  - name: criticality
    value: No designation recorded
    definition: Constituent-element listings are not transferred to the resource.
    evidence_ids:
    - target
- assessment_id: science
  area: evidence
  topic: Pretreatment, inactive biomass and laboratory outcome
  outcome: supported
  summary: The narrow biosorption claim is supported. Thermal/acid preparation occurs
    before biomass contact, and the dried algae do not establish metabolic leaching.
    Primary text and exact supplement cells agree with the scoped endpoint; experimental
    and fitted uptake are separate. Pilot cultivation of biomass does not show pilot
    recovery.
  target_ids:
  - cmmmech:spent-ndfeb-magnets
  evidence_ids:
  - paper
  - supplement
  - taxon
  - strain
  - target
  dimensions:
  - name: organism
    value: Chlorella vulgaris SAG 211-12
    definition: Species taxon and culture identifier are separate authorities; experimental
      purity unresolved.
    evidence_ids:
    - taxon
    - strain
    - paper
  - name: biomass_state
    value: Oven dried at 90 degrees C for 24 hours
    definition: Inactive microbial-origin sorbent, not growing-cell extraction.
    evidence_ids:
    - paper
  - name: conditions
    value: 0.2 L, 90 min, 300 rpm, pH 5, 35 degrees C, 250 mg Nd/L, 0.5 g dry biomass/L
    definition: Specific selected laboratory endpoint after roasting, nitric-acid
      leaching and solution preparation.
    evidence_ids:
    - paper
    - supplement
  - name: outcome
    value: 157.40 mg Nd/g dry biomass
    definition: Source-reported depletion-derived experimental uptake; not original-magnet
      percent recovery, fitted saturation capacity or isolated product yield.
    evidence_ids:
    - paper
    - supplement
- assessment_id: limits
  area: evidence
  topic: Adversarial controls, precipitation and model contradictions
  outcome: supported
  summary: Missing matched blank and phase localization limit mechanistic attribution.
    The record retains sub-detection limits without numerical zeros, 50-degree-C precipitation/value
    tension and nonuniform kinetic fits. It does not claim untreated multimetal selectivity,
    a unique binding group, complete mass balance or commercial deployment. These
    are honest source limits, not actionable defects in the bounded record.
  target_ids:
  - cmmmech:spent-ndfeb-magnets
  evidence_ids:
  - paper
  - supplement
  - target
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE history and exact reviewed working bytes
  outcome: supported
  summary: Actual GPT-6/codex sidecar targets the record and links issue 56; separate
    inline event describes current creation. Trusted base is merged main; exact source
    inputs remain unchanged after review. New resource representation reuses an experiment
    transparently.
  target_ids:
  - cmmmech:spent-ndfeb-magnets
  evidence_ids:
  - target
  - search
  - gates
findings: []
actions: []
limitations:
- The specific magnet source has incomplete device/collection history; separate used-magnet
  identity context does not repair that gap.
- Solution depletion with no matched blank or direct phase/localization evidence cannot
  establish a unique binding mechanism or original-feed product recovery.
- Full text and authorities were independently read from retained copies freshly acquired
  by the curator this round; reviewer did not describe these as independent downloads.
- Correction/counterevidence search is bounded to listed queries and returned results;
  no exhaustive clearance or corpus-wide scientific conclusion.
tags:
- round14
- independent
- scientific-review
```
