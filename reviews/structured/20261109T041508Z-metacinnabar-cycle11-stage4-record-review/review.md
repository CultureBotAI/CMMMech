# Cycle 11 Stage 4 record review: cmmmech:metacinnabar (Metacinnabar)

- Review: 20261109T041508Z-metacinnabar-cycle11-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T04:08:00Z
- Finished UTC: 2026-11-09T04:15:08Z
- Reviewer: antigravity / cmmmech-cycle11-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/metacinnabar.yaml (cmmmech:metacinnabar) at commit 794684703f77385b6e9bca32167f6c8d1e5e29bf. Verified mineral identity (cubic beta-HgS, grandfathered 1870), the Thiobacillus thioparus ATCC 8158 oxidative dissolution and Hg volatilization mechanism from Vazquez-Rodriguez et al. (2015, Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596), both synchronized UniProtKB protein_examples (Thiobacillus thioparus SoxB UniProtKB:U5TVQ7 and Thiobacillus denitrificans ATCC 25259 MerA UniProtKB:Q3SJ73), and causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph). Identified 1 minor graph finding (cmmmech-cycle11-stage4-finding-0002: SoxB protein_examples[0] evidence states 'synthetic metacinnabar (beta-HgS)' whereas primary pure-culture incubations used 2 g/L ground natural museum metacinnabar &lt;250 um, nodes[1].description omits feed specifics, edges[1] asserts supports: support for soluble Hg(II) accumulation, and edges[0..3] retain generic one-line explanations) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 11 Stage 4 audit of cmmmech:metacinnabar.

Selection: data/records/metacinnabar.yaml at 794684703f77385b6e9bca32167f6c8d1e5e29bf
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 794684703f77385b6e9bca32167f6c8d1e5e29bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:metacinnabar | data/records/metacinnabar.yaml | maintained | Metacinnabar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate metacinnabar.yaml | passed | True | cmmmech:metacinnabar | data/records/metacinnabar.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### Thiobacillus thioparus ATCC 8158 metacinnabar dissolution causal graph and SoxB/MerA groundings

graph: supported. Targets: cmmmech:metacinnabar.

Both UniProtKB protein_examples (U5TVQ7 SoxB in Thiobacillus thioparus and Q3SJ73 MerA in Thiobacillus denitrificans ATCC 25259) are synchronized between mechanisms[0] and causal_graphs[0]. However, SoxB protein_examples[0] misstates the primary natural museum metacinnabar feed as synthetic beta-HgS, and causal_graphs[0] nodes[1] and edges[0..3] retain generic one-line explanations and unqualified soluble-Hg(II) accumulation support on edges[1].

## Findings

### cmmmech-cycle11-stage4-finding-0002: Thiobacillus thioparus metacinnabar record and causal graph misstate primary natural museum metacinnabar feed as synthetic beta-HgS in SoxB protein evidence and assert unqualified soluble-Hg(II) accumulation edge support

minor / open / confirmed; issue key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support.

In data/records/metacinnabar.yaml (cmmmech:metacinnabar, mineral, Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596, vazquez_rodriguez2015), mechanisms[0].protein_examples[0].evidence[0].explanation (lines 118-120) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation (lines 192-194) for UniProtKB:U5TVQ7 (soxB, Thiobacillus thioparus) state that Vazquez-Rodriguez et al. (2015) studied 'axenic Thiobacillus thioparus ATCC 8158 pure-culture dissolution of synthetic metacinnabar (beta-HgS)', whereas mechanisms[0].context (lines 45-51) and mechanisms[0].evidence[0..4] (lines 58-97) establish that the primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural museum metacinnabar (&lt;250 um, containing pyritic inclusions, autoclaved under N2), with commercial synthetic black HgS tested only in the separate daily-thiosulfate-spike comparison (Figures 6-7). Furthermore, in causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph, lines 157-291), nodes[1].description (metacinnabar_substrate, line 198) omits the 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions) versus synthetic black HgS feed distinction; edges[1] (metacinnabar_substrate -&gt; dissolved_hg2_species, lines 265-273) asserts supports: support with description: 'Oxidation of beta-HgS releases soluble Hg(II) into the medium.' and explanation: 'Dissolved Hg(II) accumulates as an intermediate during beta-HgS bio-oxidation.', even though mechanisms[0].evidence[0..2] (lines 58-81) document that aqueous Hg remained relatively low in viable T. thioparus incubations (because mobilized Hg was reduced to volatile Hg(0)) while killed-cell and thiosulfate controls showed substantial chemical Hg release and inoculum elemental-sulfur carryover (supports: partial); and edges[0].evidence[0].explanation (line 264), edges[2].evidence[0].explanation (line 282), and edges[3].evidence[0].explanation (line 291) retain generic one-line strings omitting the Table 1 sulfate-proxy dissolution estimate (48-68% after carryover correction, Figure S3), the 285-bp merA PCR amplicon in Supplementary Data S1 (genetic potential only, without expression or mutagenesis), and gold-trap cold-vapor atomic fluorescence spectroscopy (CVAFS) volatile-Hg measurements. In this scope, 1 record(s) (metacinnabar) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-vazquez-rodriguez2015-metacinnabar-graph-and-soxb-evidence

Update mechanisms[0].protein_examples[0].evidence[0].explanation, causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation, and causal_graphs[0].nodes[1].description in data/records/metacinnabar.yaml to distinguish the primary 2 g/L ground natural museum metacinnabar (&lt;250 um, containing pyritic inclusions, Figures 3-5, Table 1) from the synthetic black HgS daily-thiosulfate-spike comparison (Figures 6-7), qualify causal_graphs[0].edges[1].evidence[0].supports to partial with accurate aqueous-Hg vs volatile-Hg(0) partitioning prose, and replace generic one-line explanations on edges[0..3] during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] in metacinnabar.yaml remain byte-identical and accurately distinguish natural museum metacinnabar (&lt;250 um) from synthetic black HgS.
- causal_graphs[0].nodes[1].description and edges[0..3] in metacinnabar.yaml use vazquez_rodriguez2015-specific prose with supports: partial on edges[1].
- Matching EDIT history sidecar exists in history/records/metacinnabar/ and passes just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-metacinnabar-file | data/records/metacinnabar.yaml; mechanisms[0] (lines 43-120); causal_graphs[0] (lines 157-291) | supports | Inspected data/records/metacinnabar.yaml, comparing mechanisms[0].context and evidence[0..4] (lines 45-97) against protein_examples[0] (lines 118-120, 192-194) and causal_graphs[0] (lines 157-291). |
| ev-metacinnabar-vazquez2015 | DOI:10.3389/fmicb.2015.00596; Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, Figures 3-7, Table 1, Supplementary Data S1 and Figure S3 | supports | Vazquez-Rodriguez et al. (2015) incubated T. thioparus ATCC 8158 primarily with 2 g/L ground natural museum metacinnabar (&lt;250 um, with pyritic inclusions; Figures 3-5, Table 1) and observed low aqueous Hg alongside major volatile Hg(0) trapping. |

## Limits And Additional Notes

- data/records/metacinnabar.yaml misstates the primary natural museum metacinnabar feed as synthetic beta-HgS in SoxB protein evidence and retains generic one-line edge explanations and unqualified soluble-Hg(II) accumulation support on edges[1] (tracked as open finding cmmmech-cycle11-stage4-finding-0002 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T041508Z-metacinnabar-cycle11-stage4-record-review
title: 'Cycle 11 Stage 4 record review: cmmmech:metacinnabar (Metacinnabar)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-11-09T04:08:00Z'
finished_at: '2026-11-09T04:15:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/metacinnabar.yaml (cmmmech:metacinnabar) at commit
  794684703f77385b6e9bca32167f6c8d1e5e29bf. Verified mineral identity (cubic beta-HgS,
  grandfathered 1870), the Thiobacillus thioparus ATCC 8158 oxidative dissolution
  and Hg volatilization mechanism from Vazquez-Rodriguez et al. (2015, Frontiers in
  Microbiology 6:596, DOI:10.3389/fmicb.2015.00596), both synchronized UniProtKB protein_examples
  (Thiobacillus thioparus SoxB UniProtKB:U5TVQ7 and Thiobacillus denitrificans ATCC
  25259 MerA UniProtKB:Q3SJ73), and causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph).
  Identified 1 minor graph finding (cmmmech-cycle11-stage4-finding-0002: SoxB protein_examples[0]
  evidence states ''synthetic metacinnabar (beta-HgS)'' whereas primary pure-culture
  incubations used 2 g/L ground natural museum metacinnabar <250 um, nodes[1].description
  omits feed specifics, edges[1] asserts supports: support for soluble Hg(II) accumulation,
  and edges[0..3] retain generic one-line explanations) for Stage 5 grouped remediation.'
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
  - path: data/records/metacinnabar.yaml
    sha256: 0bb941fbfa16112b5dddff9d25e414e4a5ce00ce79bf9ab80ee39f4285ca4c31
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
  - cmmmech:metacinnabar
  selection: data/records/metacinnabar.yaml at 794684703f77385b6e9bca32167f6c8d1e5e29bf
  description: Single-record Cycle 11 Stage 4 audit of cmmmech:metacinnabar.
targets:
- target_id: cmmmech:metacinnabar
  path: data/records/metacinnabar.yaml
  kind: maintained
  label: Metacinnabar
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-metacinnabar
  name: cmmmech validate metacinnabar.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/metacinnabar.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:metacinnabar
  evidence_ids:
  - ev-metacinnabar-file
  summary: data/records/metacinnabar.yaml passes LinkML structural, semantic, and
    canonical top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-metacinnabar-thioparus-graph-and-proteins
  topic: Thiobacillus thioparus ATCC 8158 metacinnabar dissolution causal graph and
    SoxB/MerA groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:metacinnabar
  evidence_ids:
  - ev-metacinnabar-file
  - ev-metacinnabar-vazquez2015
  summary: Both UniProtKB protein_examples (U5TVQ7 SoxB in Thiobacillus thioparus
    and Q3SJ73 MerA in Thiobacillus denitrificans ATCC 25259) are synchronized between
    mechanisms[0] and causal_graphs[0]. However, SoxB protein_examples[0] misstates
    the primary natural museum metacinnabar feed as synthetic beta-HgS, and causal_graphs[0]
    nodes[1] and edges[0..3] retain generic one-line explanations and unqualified
    soluble-Hg(II) accumulation support on edges[1].
findings:
- finding_id: cmmmech-cycle11-stage4-finding-0002
  issue_key: cmmmech.vazquez-rodriguez2015-metacinnabar.natural-vs-synthetic-feed-and-aqueous-hg-edge-support
  title: Thiobacillus thioparus metacinnabar record and causal graph misstate primary
    natural museum metacinnabar feed as synthetic beta-HgS in SoxB protein evidence
    and assert unqualified soluble-Hg(II) accumulation edge support
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:metacinnabar
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].evidence[0].explanation
  evidence_ids:
  - ev-metacinnabar-file
  - ev-metacinnabar-vazquez2015
  description: 'In data/records/metacinnabar.yaml (cmmmech:metacinnabar, mineral,
    Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, DOI:10.3389/fmicb.2015.00596,
    vazquez_rodriguez2015), mechanisms[0].protein_examples[0].evidence[0].explanation
    (lines 118-120) and causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
    (lines 192-194) for UniProtKB:U5TVQ7 (soxB, Thiobacillus thioparus) state that
    Vazquez-Rodriguez et al. (2015) studied ''axenic Thiobacillus thioparus ATCC 8158
    pure-culture dissolution of synthetic metacinnabar (beta-HgS)'', whereas mechanisms[0].context
    (lines 45-51) and mechanisms[0].evidence[0..4] (lines 58-97) establish that the
    primary pure-culture incubations (Figures 3-5, Table 1) used 2 g/L ground natural
    museum metacinnabar (<250 um, containing pyritic inclusions, autoclaved under
    N2), with commercial synthetic black HgS tested only in the separate daily-thiosulfate-spike
    comparison (Figures 6-7). Furthermore, in causal_graphs[0] (thioparus_soxb_mera_metacinnabar_graph,
    lines 157-291), nodes[1].description (metacinnabar_substrate, line 198) omits
    the 2 g/L ground natural museum metacinnabar (<250 um, with pyritic inclusions)
    versus synthetic black HgS feed distinction; edges[1] (metacinnabar_substrate
    -> dissolved_hg2_species, lines 265-273) asserts supports: support with description:
    ''Oxidation of beta-HgS releases soluble Hg(II) into the medium.'' and explanation:
    ''Dissolved Hg(II) accumulates as an intermediate during beta-HgS bio-oxidation.'',
    even though mechanisms[0].evidence[0..2] (lines 58-81) document that aqueous Hg
    remained relatively low in viable T. thioparus incubations (because mobilized
    Hg was reduced to volatile Hg(0)) while killed-cell and thiosulfate controls showed
    substantial chemical Hg release and inoculum elemental-sulfur carryover (supports:
    partial); and edges[0].evidence[0].explanation (line 264), edges[2].evidence[0].explanation
    (line 282), and edges[3].evidence[0].explanation (line 291) retain generic one-line
    strings omitting the Table 1 sulfate-proxy dissolution estimate (48-68% after
    carryover correction, Figure S3), the 285-bp merA PCR amplicon in Supplementary
    Data S1 (genetic potential only, without expression or mutagenesis), and gold-trap
    cold-vapor atomic fluorescence spectroscopy (CVAFS) volatile-Hg measurements.
    In this scope, 1 record(s) (metacinnabar) are affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
actions:
- action_id: act-refine-vazquez-rodriguez2015-metacinnabar-graph-and-soxb-evidence
  finding_ids:
  - cmmmech-cycle11-stage4-finding-0002
  target_ids:
  - cmmmech:metacinnabar
  description: Update mechanisms[0].protein_examples[0].evidence[0].explanation, causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation,
    and causal_graphs[0].nodes[1].description in data/records/metacinnabar.yaml to
    distinguish the primary 2 g/L ground natural museum metacinnabar (<250 um, containing
    pyritic inclusions, Figures 3-5, Table 1) from the synthetic black HgS daily-thiosulfate-spike
    comparison (Figures 6-7), qualify causal_graphs[0].edges[1].evidence[0].supports
    to partial with accurate aqueous-Hg vs volatile-Hg(0) partitioning prose, and
    replace generic one-line explanations on edges[0..3] during Stage 5 grouped remediation
    with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/metacinnabar.yaml
    role: maintained_record
  acceptance_checks:
  - mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    in metacinnabar.yaml remain byte-identical and accurately distinguish natural
    museum metacinnabar (<250 um) from synthetic black HgS.
  - 'causal_graphs[0].nodes[1].description and edges[0..3] in metacinnabar.yaml use
    vazquez_rodriguez2015-specific prose with supports: partial on edges[1].'
  - Matching EDIT history sidecar exists in history/records/metacinnabar/ and passes
    just check.
evidence:
- evidence_id: ev-metacinnabar-file
  kind: record_content
  reference: data/records/metacinnabar.yaml
  locator: mechanisms[0] (lines 43-120); causal_graphs[0] (lines 157-291)
  accessed_at: '2026-11-09T04:15:08Z'
  support: supports
  summary: Inspected data/records/metacinnabar.yaml, comparing mechanisms[0].context
    and evidence[0..4] (lines 45-97) against protein_examples[0] (lines 118-120, 192-194)
    and causal_graphs[0] (lines 157-291).
- evidence_id: ev-metacinnabar-vazquez2015
  kind: primary_source
  reference: DOI:10.3389/fmicb.2015.00596
  locator: Vazquez-Rodriguez et al. 2015 Frontiers in Microbiology 6:596, Figures
    3-7, Table 1, Supplementary Data S1 and Figure S3
  accessed_at: '2026-11-09T04:15:08Z'
  support: supports
  summary: Vazquez-Rodriguez et al. (2015) incubated T. thioparus ATCC 8158 primarily
    with 2 g/L ground natural museum metacinnabar (<250 um, with pyritic inclusions;
    Figures 3-5, Table 1) and observed low aqueous Hg alongside major volatile Hg(0)
    trapping.
limitations:
- data/records/metacinnabar.yaml misstates the primary natural museum metacinnabar
  feed as synthetic beta-HgS in SoxB protein evidence and retains generic one-line
  edge explanations and unqualified soluble-Hg(II) accumulation support on edges[1]
  (tracked as open finding cmmmech-cycle11-stage4-finding-0002 for Stage 5 remediation).
notes: []
```
