# Cycle 11 Stage 4 record review: cmmmech:scandium (scandium atom)

- Review: 20261109T041509Z-scandium-cycle11-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T04:09:00Z
- Finished UTC: 2026-11-09T04:15:09Z
- Reviewer: antigravity / cmmmech-cycle11-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/scandium.yaml (cmmmech:scandium) at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf. Verified CHEBI identity (CHEBI:33330 scandium atom), its dated jurisdiction-scoped criticality entry (United States of America, USGS Final List of Critical Minerals 2025, usgs2025), the immobilized Methylorubrum extorquens AM1 lanmodulin (Mex-LanM, UniProtKB:C5B164) chromatographic separation mechanism from Dong et al. (2024, Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919), and causal_graphs[0] (immobilized_mex_lanm_scandium_separation_graph). Identified 1 minor graph finding (cmmmech-cycle11-stage4-finding-0003: Mex-LanM protein_examples[0] evidence asserts supports: support with 'mild acid stripping' over 'transition/base metals' instead of stepwise 30 mM and 50 mM malonate elution at pH 5.0 from a synthetic 16-REE chloride feed, and causal_graphs[0] describes the synthetic 16-REE feed as a 'mixed leachate feed' / 'multi-metal leachate' with unqualified supports: support on edges[0]) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 11 Stage 4 audit of cmmmech:scandium.

Selection: data/records/scandium.yaml at 794684703f77385b6e9bca32167f6c8d1e5e29bf
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 794684703f77385b6e9bca32167f6c8d1e5e29bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:scandium | data/records/scandium.yaml | maintained | Scandium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate scandium.yaml | passed | True | cmmmech:scandium | data/records/scandium.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### Immobilized Mex-LanM scandium chromatography causal graph and UniProtKB:C5B164 grounding

graph: supported. Targets: cmmmech:scandium.

UniProtKB:C5B164 (Mex-LanM) is accurately grounded to Methylorubrum extorquens AM1 and synchronized between mechanisms[0] and causal_graphs[0]. However, protein_examples[0] misdescribes stepwise pH 5.0 malonate elution from a synthetic 16-REE chloride mixture as mild acid stripping over transition/base metals with supports: support, and causal_graphs[0] describes the synthetic feed as a mixed leachate with unqualified support on edges[0].

## Findings

### cmmmech-cycle11-stage4-finding-0003: Mex-LanM scandium chromatography record and causal graph misdescribe pH 5.0 malonate elution from a synthetic 16-REE chloride feed as mild acid stripping of transition/base metals from a multi-metal leachate

minor / open / confirmed; issue key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording.

In data/records/scandium.yaml (cmmmech:scandium, element, Dong et al. 2024 Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919, dong2024), mechanisms[0].protein_examples[0].evidence[0] (lines 64-66) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0] (lines 109-111) for UniProtKB:C5B164 (lanM / Mex-LanM) assert supports: support with explanation: 'Immobilized Mex-LanM selectively binds Sc(III) over competing transition/base metals and elutes high-purity scandium upon mild acid stripping.', whereas mechanisms[0].description (line 39), mechanisms[0].context (line 40), and mechanisms[0].evidence[0..1] (lines 68-73) establish that Dong et al. (2024) Section 3.4 and Figures 3C and 5E-F tested a synthetic 16-REE chloride-salt mixture at pH 3.0 (nominal 0.4 mM total REE in Figure 5, summing to 0.2430 mM across 16 REEs with 23.8 +/- 1.1 uM Sc in supplement Table S10, labeled Table S9 in the caption) and eluted Sc(III) selectively using stepwise 30 mM and 50 mM malonate at pH 5.0 (not mild acid stripping of transition/base metals), without a matched Sc-only resin-without-LanM control (supports: partial). Furthermore, in causal_graphs[0] (immobilized_mex_lanm_scandium_separation_graph, lines 78-140), causal_graphs[0].description (line 80), nodes[1].label and nodes[1].description (mixed_scandium_feed, lines 113-115), nodes[2].description (purified_scandium_eluate, line 120), and edges[1] (lines 135-140) describe the Figure 5 column input as a 'mixed leachate feed' / 'multi-metal leachate' rather than a synthetic pH 3.0 chloride-salt REE solution resembling selected leachate compositions (mechanisms[0].context, line 40), and edges[0] (mex_lanm_protein -&gt; mixed_scandium_feed, lines 123-131) uses a generic 78-character explanation ('Immobilized LanM columns selectively retain Sc(III) from multi-metal mixtures.') with supports: support that omits the Table S9/S10 feed-concentration discrepancy (0.4 mM nominal vs 0.2430 mM sum) and the absence of a matched Sc-only resin-without-LanM control (mechanisms[0].evidence[1], supports: partial). In this scope, 1 record(s) (scandium) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-dong2024-scandium-mex-lanm-graph-and-protein-evidence

Update mechanisms[0].protein_examples[0].evidence[0] and causal_graphs[0].nodes[0].protein_examples[0].evidence[0] in data/records/scandium.yaml to supports: partial with synchronized prose describing selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride mixture and stepwise 30 mM / 50 mM malonate elution at pH 5.0 (above 99 mol% purity among REEs and above 99% two-step yield; ~94.5% Sc yield at 30 mM malonate, Figures 3C and 5E-F, Table S9/S10), and update causal_graphs[0].description, nodes[1..2], and edges[0..1] (with supports: partial on edges[0]) during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] in scandium.yaml are synchronized with supports: partial and specify stepwise pH 5.0 malonate elution (30 mM and 50 mM) from a synthetic 16-REE chloride feed rather than mild acid stripping.
- causal_graphs[0].description, nodes[1..2], and edges[0..1] in scandium.yaml accurately describe the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM sum in Table S9/S10) and qualify edges[0].evidence[0].supports to partial.
- Matching EDIT history sidecar exists in history/records/scandium/ and passes just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-scandium-file | data/records/scandium.yaml; mechanisms[0] (lines 36-74); causal_graphs[0] (lines 78-140) | supports | Inspected data/records/scandium.yaml, comparing mechanisms[0].description, context, and evidence[0..1] (lines 39-73) against protein_examples[0] (lines 64-66, 109-111) and causal_graphs[0] (lines 78-140). |
| ev-scandium-dong2024 | DOI:10.1016/j.seppur.2023.125919; Dong et al. 2024 Separation and Purification Technology 333:125919, Section 3.4, Figures 3C and 5E-F, Supplement Table S9/S10 | supports | Dong et al. (2024) loaded a synthetic pH 3.0 16-REE chloride mixture (nominal 0.4 mM total REE in Figure 5; 0.2430 mM sum with 23.8 +/- 1.1 uM Sc in Table S9/S10) onto an agarose resin column with immobilized Mex-LanM and eluted Sc(III) at above 99 mol% purity among REEs and above 99% yield for the two-step malonate process (~94.5% Sc yield at 30 mM malonate and ~98.9% La yield at 50 mM malonate at pH 5.0). |

## Limits And Additional Notes

- data/records/scandium.yaml misdescribes stepwise pH 5.0 malonate elution from a synthetic 16-REE chloride feed as mild acid stripping over transition/base metals in protein_examples[0] and labels the synthetic feed as a mixed leachate in causal_graphs[0] with unqualified supports: support (tracked as open finding cmmmech-cycle11-stage4-finding-0003 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T041509Z-scandium-cycle11-stage4-record-review
title: 'Cycle 11 Stage 4 record review: cmmmech:scandium (scandium atom)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-11-09T04:09:00Z'
finished_at: '2026-11-09T04:15:09Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/scandium.yaml (cmmmech:scandium) at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
  Verified CHEBI identity (CHEBI:33330 scandium atom), its dated jurisdiction-scoped
  criticality entry (United States of America, USGS Final List of Critical Minerals
  2025, usgs2025), the immobilized Methylorubrum extorquens AM1 lanmodulin (Mex-LanM,
  UniProtKB:C5B164) chromatographic separation mechanism from Dong et al. (2024, Separation
  and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919), and causal_graphs[0]
  (immobilized_mex_lanm_scandium_separation_graph). Identified 1 minor graph finding
  (cmmmech-cycle11-stage4-finding-0003: Mex-LanM protein_examples[0] evidence asserts
  supports: support with ''mild acid stripping'' over ''transition/base metals'' instead
  of stepwise 30 mM and 50 mM malonate elution at pH 5.0 from a synthetic 16-REE chloride
  feed, and causal_graphs[0] describes the synthetic 16-REE feed as a ''mixed leachate
  feed'' / ''multi-metal leachate'' with unqualified supports: support on edges[0])
  for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle11-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 11 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit 794684703f77385b6e9bca32167f6c8d1e5e29bf.
source:
  git_revision: 794684703f77385b6e9bca32167f6c8d1e5e29bf
  state: git_commit
  inputs:
  - path: data/records/scandium.yaml
    sha256: a5790221b2863ad14ecb1ef28425f2b95659f818a18b658dcd2f2a70e4e5fe16
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: edf999adb3da7dceadcc340b5561663a7fb56dfd1178992633a1a7ad1abcb937
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:scandium
  selection: data/records/scandium.yaml at 794684703f77385b6e9bca32167f6c8d1e5e29bf
  description: Single-record Cycle 11 Stage 4 audit of cmmmech:scandium.
targets:
- target_id: cmmmech:scandium
  path: data/records/scandium.yaml
  kind: maintained
  label: Scandium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-scandium
  name: cmmmech validate scandium.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/scandium.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:scandium
  evidence_ids:
  - ev-scandium-file
  summary: data/records/scandium.yaml passes LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-scandium-mex-lanm-graph-and-protein
  topic: Immobilized Mex-LanM scandium chromatography causal graph and UniProtKB:C5B164
    grounding
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:scandium
  evidence_ids:
  - ev-scandium-file
  - ev-scandium-dong2024
  summary: 'UniProtKB:C5B164 (Mex-LanM) is accurately grounded to Methylorubrum extorquens
    AM1 and synchronized between mechanisms[0] and causal_graphs[0]. However, protein_examples[0]
    misdescribes stepwise pH 5.0 malonate elution from a synthetic 16-REE chloride
    mixture as mild acid stripping over transition/base metals with supports: support,
    and causal_graphs[0] describes the synthetic feed as a mixed leachate with unqualified
    support on edges[0].'
findings:
- finding_id: cmmmech-cycle11-stage4-finding-0003
  issue_key: cmmmech.dong2024-scandium.synthetic-feed-vs-leachate-and-malonate-elution-wording
  title: Mex-LanM scandium chromatography record and causal graph misdescribe pH 5.0
    malonate elution from a synthetic 16-REE chloride feed as mild acid stripping
    of transition/base metals from a multi-metal leachate
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:scandium
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].explanation
  evidence_ids:
  - ev-scandium-file
  - ev-scandium-dong2024
  description: 'In data/records/scandium.yaml (cmmmech:scandium, element, Dong et
    al. 2024 Separation and Purification Technology 333:125919, DOI:10.1016/j.seppur.2023.125919,
    dong2024), mechanisms[0].protein_examples[0].evidence[0] (lines 64-66) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0]
    (lines 109-111) for UniProtKB:C5B164 (lanM / Mex-LanM) assert supports: support
    with explanation: ''Immobilized Mex-LanM selectively binds Sc(III) over competing
    transition/base metals and elutes high-purity scandium upon mild acid stripping.'',
    whereas mechanisms[0].description (line 39), mechanisms[0].context (line 40),
    and mechanisms[0].evidence[0..1] (lines 68-73) establish that Dong et al. (2024)
    Section 3.4 and Figures 3C and 5E-F tested a synthetic 16-REE chloride-salt mixture
    at pH 3.0 (nominal 0.4 mM total REE in Figure 5, summing to 0.2430 mM across 16
    REEs with 23.8 +/- 1.1 uM Sc in supplement Table S10, labeled Table S9 in the
    caption) and eluted Sc(III) selectively using stepwise 30 mM and 50 mM malonate
    at pH 5.0 (not mild acid stripping of transition/base metals), without a matched
    Sc-only resin-without-LanM control (supports: partial). Furthermore, in causal_graphs[0]
    (immobilized_mex_lanm_scandium_separation_graph, lines 78-140), causal_graphs[0].description
    (line 80), nodes[1].label and nodes[1].description (mixed_scandium_feed, lines
    113-115), nodes[2].description (purified_scandium_eluate, line 120), and edges[1]
    (lines 135-140) describe the Figure 5 column input as a ''mixed leachate feed''
    / ''multi-metal leachate'' rather than a synthetic pH 3.0 chloride-salt REE solution
    resembling selected leachate compositions (mechanisms[0].context, line 40), and
    edges[0] (mex_lanm_protein -> mixed_scandium_feed, lines 123-131) uses a generic
    78-character explanation (''Immobilized LanM columns selectively retain Sc(III)
    from multi-metal mixtures.'') with supports: support that omits the Table S9/S10
    feed-concentration discrepancy (0.4 mM nominal vs 0.2430 mM sum) and the absence
    of a matched Sc-only resin-without-LanM control (mechanisms[0].evidence[1], supports:
    partial). In this scope, 1 record(s) (scandium) are affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
actions:
- action_id: act-refine-dong2024-scandium-mex-lanm-graph-and-protein-evidence
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0003
  target_ids:
  - cmmmech:scandium
  description: 'Update mechanisms[0].protein_examples[0].evidence[0] and causal_graphs[0].nodes[0].protein_examples[0].evidence[0]
    in data/records/scandium.yaml to supports: partial with synchronized prose describing
    selective Sc(III) retention from a synthetic pH 3.0 16-REE chloride mixture and
    stepwise 30 mM / 50 mM malonate elution at pH 5.0 (above 99 mol% purity among
    REEs and above 99% two-step yield; ~94.5% Sc yield at 30 mM malonate, Figures
    3C and 5E-F, Table S9/S10), and update causal_graphs[0].description, nodes[1..2],
    and edges[0..1] (with supports: partial on edges[0]) during Stage 5 grouped remediation
    with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/scandium.yaml
    role: maintained_record
  acceptance_checks:
  - 'mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    in scandium.yaml are synchronized with supports: partial and specify stepwise
    pH 5.0 malonate elution (30 mM and 50 mM) from a synthetic 16-REE chloride feed
    rather than mild acid stripping.'
  - causal_graphs[0].description, nodes[1..2], and edges[0..1] in scandium.yaml accurately
    describe the synthetic pH 3.0 16-REE chloride feed (0.4 mM nominal / 0.2430 mM
    sum in Table S9/S10) and qualify edges[0].evidence[0].supports to partial.
  - Matching EDIT history sidecar exists in history/records/scandium/ and passes just
    check.
evidence:
- evidence_id: ev-scandium-file
  kind: record_content
  reference: data/records/scandium.yaml
  locator: mechanisms[0] (lines 36-74); causal_graphs[0] (lines 78-140)
  accessed_at: '2026-11-09T04:15:09Z'
  support: supports
  summary: Inspected data/records/scandium.yaml, comparing mechanisms[0].description,
    context, and evidence[0..1] (lines 39-73) against protein_examples[0] (lines 64-66,
    109-111) and causal_graphs[0] (lines 78-140).
- evidence_id: ev-scandium-dong2024
  kind: primary_source
  reference: DOI:10.1016/j.seppur.2023.125919
  locator: Dong et al. 2024 Separation and Purification Technology 333:125919, Section
    3.4, Figures 3C and 5E-F, Supplement Table S9/S10
  accessed_at: '2026-11-09T04:15:09Z'
  support: supports
  summary: Dong et al. (2024) loaded a synthetic pH 3.0 16-REE chloride mixture (nominal
    0.4 mM total REE in Figure 5; 0.2430 mM sum with 23.8 +/- 1.1 uM Sc in Table S9/S10)
    onto an agarose resin column with immobilized Mex-LanM and eluted Sc(III) at above
    99 mol% purity among REEs and above 99% yield for the two-step malonate process
    (~94.5% Sc yield at 30 mM malonate and ~98.9% La yield at 50 mM malonate at pH
    5.0).
limitations:
- 'data/records/scandium.yaml misdescribes stepwise pH 5.0 malonate elution from a
  synthetic 16-REE chloride feed as mild acid stripping over transition/base metals
  in protein_examples[0] and labels the synthetic feed as a mixed leachate in causal_graphs[0]
  with unqualified supports: support (tracked as open finding cmmmech-cycle11-stage4-finding-0003
  for Stage 5 remediation).'
notes: []
```
