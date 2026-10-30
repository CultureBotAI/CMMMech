# Cycle 5 Stage 4 record review: cmmmech:tetrahedrite-concentrate (Tetrahedrite concentrate)

- Review: 20261030T201008Z-tetrahedrite-concentrate-cycle5-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T20:07:30Z
- Finished UTC: 2026-10-30T20:10:08Z
- Reviewer: antigravity / cmmmech-cycle5-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/tetrahedrite-concentrate.yaml (cmmmech:tetrahedrite-concentrate) at commit 208134600496b954831b125033d33caa508dba8b following Cycle 5 Stage 3 expansion of Acidithiobacillus ferrooxidans ATCC 23270 (UP000001362) and Acidithiobacillus ferrivorans CF27 (UP000193925) UniProtKB protein_examples (6 entries: B7JBP8, B7J411, A0A060UVE9, A0A060UMZ1, B7J3C9, A0A060URH6) for the Kupka et al. (2025, DOI:10.1007/s40831-025-01089-0) bioleaching study. Verified all 6 UniProtKB accessions and synchronization between mechanisms[0] and causal_graphs[0]. Identified 1 minor graph/label finding (cmmmech-cycle5-stage4-finding-0002: causal_graphs[0].nodes[1] tth_hydrolase retains single-species A. ferrooxidans label/description and edges[0].evidence[0].explanation omits sqr2) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 5 Stage 4 audit of cmmmech:tetrahedrite-concentrate after Cycle 5 Stage 3 A. ferrooxidans and A. ferrivorans UniProtKB protein grounding expansion.

Selection: data/records/tetrahedrite-concentrate.yaml at 208134600496b954831b125033d33caa508dba8b
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 208134600496b954831b125033d33caa508dba8b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate tetrahedrite-concentrate.yaml | passed | True | cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml passes LinkML structural and semantic validation with 0 errors. |

## Scientific And Domain Assessments

### Dual-species A. ferrooxidans / A. ferrivorans UniProtKB protein_examples and causal graph labels

graph: supported. Targets: cmmmech:tetrahedrite-concentrate.

All 6 UniProtKB protein_examples (B7JBP8 [AFE_1792], B7J411 [sqr / AFE_0267], A0A060UVE9 [sqr / AFERRI_11118], A0A060UMZ1 [sqr2 / AFERRI_20483], B7J3C9 [tth / AFE_0029], and A0A060URH6 [tetH]) are accurately grounded to reference proteomes UP000001362 and UP000193925, qualified with partial support against kupka_2025, and synchronized between mechanisms[0] and causal_graphs[0]. However, causal_graphs[0].nodes[1] (tth_hydrolase) retains a single-species A. ferrooxidans label/description and edges[0].evidence[0].explanation omits sqr2.

## Findings

### cmmmech-cycle5-stage4-finding-0002: causal_graphs[0] in tetrahedrite-concentrate.yaml retains single-species tth_hydrolase label/description and omits sqr2 in edges[0].evidence[0].explanation

minor / open / confirmed; issue key: cmmmech.tetrahedrite-concentrate.tth-hydrolase-label-and-edge-explanation.

In data/records/tetrahedrite-concentrate.yaml (cmmmech:tetrahedrite-concentrate), causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) node tth_hydrolase (lines 304-307) retains single-species label 'Tth tetrathionate hydrolase (tth / AFE_0029)' and generic description without Acidithiobacillus ferrivorans tetH (UniProtKB:A0A060URH6, reference proteome UP000193925 strain CF27), whereas sibling node sqr_reductase (lines 209-212) and edges[0].evidence[0].explanation (line 380) explicitly name both experimental species arms (A. ferrooxidans and A. ferrivorans). In addition, edges[0].evidence[0].explanation (line 380) states 'individual sqr/tth/tetH genes were not mutated', omitting sqr2 (AFERRI_20483, UniProtKB:A0A060UMZ1).

## Recommended Actions And Acceptance Checks

### act-fix-tetrahedrite-concentrate-tth-label-and-edge-explanation

Update causal_graphs[0].nodes[1].label and description in data/records/tetrahedrite-concentrate.yaml to include both A. ferrooxidans Tth (tth / AFE_0029) and A. ferrivorans TetH (tetH / UniProtKB:A0A060URH6), and update causal_graphs[0].edges[0].evidence[0].explanation to list sqr/sqr2/tth/tetH during Stage 5 grouped remediation with a canonical history sidecar.

- causal_graphs[0].nodes[1].label and description in data/records/tetrahedrite-concentrate.yaml name both A. ferrooxidans Tth (tth / AFE_0029) and A. ferrivorans TetH (tetH / UniProtKB:A0A060URH6).
- causal_graphs[0].edges[0].evidence[0].explanation lists individual sqr/sqr2/tth/tetH genes.
- A matching EDIT history sidecar exists in history/records/tetrahedrite-concentrate/ and passes just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-tetrahedrite-file | data/records/tetrahedrite-concentrate.yaml; lines 1-444 | supports | Inspected all 444 lines of data/records/tetrahedrite-concentrate.yaml, including mechanisms[0] (6 protein_examples) and causal_graphs[0] (5 nodes, 4 edges). |
| ev-tetrahedrite-kupka2025 | DOI:10.1007/s40831-025-01089-0; Kupka et al. 2025 Journal of Sustainable Metallurgy 11:3685-3699, Tables 1-2, Figures 1-8, Supplement Figures S1-S12 | supports | Kupka et al. (2025) assayed separate aerobic shake-flask bioleaching arms of Acidithiobacillus ferrooxidans DSM 14882 and Acidithiobacillus ferrivorans SS3 (DSM 17398) on Strieborna vein flotation tetrahedrite concentrate over 120 days at 25 °C. |

## Limits And Additional Notes

- data/records/tetrahedrite-concentrate.yaml retains a single-species A. ferrooxidans label/description on causal_graphs[0].nodes[1] (tth_hydrolase) and omits sqr2 in causal_graphs[0].edges[0].evidence[0].explanation (tracked as open finding cmmmech-cycle5-stage4-finding-0002 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T201008Z-tetrahedrite-concentrate-cycle5-stage4-record-review
title: 'Cycle 5 Stage 4 record review: cmmmech:tetrahedrite-concentrate (Tetrahedrite
  concentrate)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-30T20:07:30Z'
finished_at: '2026-10-30T20:10:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/tetrahedrite-concentrate.yaml (cmmmech:tetrahedrite-concentrate)
  at commit 208134600496b954831b125033d33caa508dba8b following Cycle 5 Stage 3 expansion
  of Acidithiobacillus ferrooxidans ATCC 23270 (UP000001362) and Acidithiobacillus
  ferrivorans CF27 (UP000193925) UniProtKB protein_examples (6 entries: B7JBP8, B7J411,
  A0A060UVE9, A0A060UMZ1, B7J3C9, A0A060URH6) for the Kupka et al. (2025, DOI:10.1007/s40831-025-01089-0)
  bioleaching study. Verified all 6 UniProtKB accessions and synchronization between
  mechanisms[0] and causal_graphs[0]. Identified 1 minor graph/label finding (cmmmech-cycle5-stage4-finding-0002:
  causal_graphs[0].nodes[1] tth_hydrolase retains single-species A. ferrooxidans label/description
  and edges[0].evidence[0].explanation omits sqr2) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 5 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit 208134600496b954831b125033d33caa508dba8b.
source:
  git_revision: 208134600496b954831b125033d33caa508dba8b
  state: git_commit
  inputs:
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: 3fdb94f907c15d06181c587c3b808643b58df94c6ab31d0febd2f33fe026a00f
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: d2a31e40b52cee60a86a2897db9b8274b1089c92dd043d83313b7d87e05c6635
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tetrahedrite-concentrate
  selection: data/records/tetrahedrite-concentrate.yaml at 208134600496b954831b125033d33caa508dba8b
  description: Single-record Cycle 5 Stage 4 audit of cmmmech:tetrahedrite-concentrate
    after Cycle 5 Stage 3 A. ferrooxidans and A. ferrivorans UniProtKB protein grounding
    expansion.
targets:
- target_id: cmmmech:tetrahedrite-concentrate
  path: data/records/tetrahedrite-concentrate.yaml
  kind: maintained
  label: Tetrahedrite concentrate
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-tetrahedrite-concentrate
  name: cmmmech validate tetrahedrite-concentrate.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/tetrahedrite-concentrate.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - ev-tetrahedrite-file
  summary: data/records/tetrahedrite-concentrate.yaml passes LinkML structural and
    semantic validation with 0 errors.
assessments:
- assessment_id: assess-tetrahedrite-proteins-and-graph
  topic: Dual-species A. ferrooxidans / A. ferrivorans UniProtKB protein_examples
    and causal graph labels
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - ev-tetrahedrite-file
  - ev-tetrahedrite-kupka2025
  summary: All 6 UniProtKB protein_examples (B7JBP8 [AFE_1792], B7J411 [sqr / AFE_0267],
    A0A060UVE9 [sqr / AFERRI_11118], A0A060UMZ1 [sqr2 / AFERRI_20483], B7J3C9 [tth
    / AFE_0029], and A0A060URH6 [tetH]) are accurately grounded to reference proteomes
    UP000001362 and UP000193925, qualified with partial support against kupka_2025,
    and synchronized between mechanisms[0] and causal_graphs[0]. However, causal_graphs[0].nodes[1]
    (tth_hydrolase) retains a single-species A. ferrooxidans label/description and
    edges[0].evidence[0].explanation omits sqr2.
findings:
- finding_id: cmmmech-cycle5-stage4-finding-0002
  issue_key: cmmmech.tetrahedrite-concentrate.tth-hydrolase-label-and-edge-explanation
  title: causal_graphs[0] in tetrahedrite-concentrate.yaml retains single-species
    tth_hydrolase label/description and omits sqr2 in edges[0].evidence[0].explanation
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  evidence_ids:
  - ev-tetrahedrite-file
  - ev-tetrahedrite-kupka2025
  description: In data/records/tetrahedrite-concentrate.yaml (cmmmech:tetrahedrite-concentrate),
    causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) node tth_hydrolase
    (lines 304-307) retains single-species label 'Tth tetrathionate hydrolase (tth
    / AFE_0029)' and generic description without Acidithiobacillus ferrivorans tetH
    (UniProtKB:A0A060URH6, reference proteome UP000193925 strain CF27), whereas sibling
    node sqr_reductase (lines 209-212) and edges[0].evidence[0].explanation (line
    380) explicitly name both experimental species arms (A. ferrooxidans and A. ferrivorans).
    In addition, edges[0].evidence[0].explanation (line 380) states 'individual sqr/tth/tetH
    genes were not mutated', omitting sqr2 (AFERRI_20483, UniProtKB:A0A060UMZ1).
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
actions:
- action_id: act-fix-tetrahedrite-concentrate-tth-label-and-edge-explanation
  finding_ids:
  - cmmmech-cycle5-stage4-finding-0002
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  description: Update causal_graphs[0].nodes[1].label and description in data/records/tetrahedrite-concentrate.yaml
    to include both A. ferrooxidans Tth (tth / AFE_0029) and A. ferrivorans TetH (tetH
    / UniProtKB:A0A060URH6), and update causal_graphs[0].edges[0].evidence[0].explanation
    to list sqr/sqr2/tth/tetH during Stage 5 grouped remediation with a canonical
    history sidecar.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  acceptance_checks:
  - causal_graphs[0].nodes[1].label and description in data/records/tetrahedrite-concentrate.yaml
    name both A. ferrooxidans Tth (tth / AFE_0029) and A. ferrivorans TetH (tetH /
    UniProtKB:A0A060URH6).
  - causal_graphs[0].edges[0].evidence[0].explanation lists individual sqr/sqr2/tth/tetH
    genes.
  - A matching EDIT history sidecar exists in history/records/tetrahedrite-concentrate/
    and passes just check.
evidence:
- evidence_id: ev-tetrahedrite-file
  kind: record_content
  reference: data/records/tetrahedrite-concentrate.yaml
  locator: lines 1-444
  accessed_at: '2026-10-30T20:10:08Z'
  support: supports
  summary: Inspected all 444 lines of data/records/tetrahedrite-concentrate.yaml,
    including mechanisms[0] (6 protein_examples) and causal_graphs[0] (5 nodes, 4
    edges).
- evidence_id: ev-tetrahedrite-kupka2025
  kind: primary_source
  reference: DOI:10.1007/s40831-025-01089-0
  locator: Kupka et al. 2025 Journal of Sustainable Metallurgy 11:3685-3699, Tables
    1-2, Figures 1-8, Supplement Figures S1-S12
  accessed_at: '2026-10-30T20:10:08Z'
  support: supports
  summary: Kupka et al. (2025) assayed separate aerobic shake-flask bioleaching arms
    of Acidithiobacillus ferrooxidans DSM 14882 and Acidithiobacillus ferrivorans
    SS3 (DSM 17398) on Strieborna vein flotation tetrahedrite concentrate over 120
    days at 25 °C.
limitations:
- data/records/tetrahedrite-concentrate.yaml retains a single-species A. ferrooxidans
  label/description on causal_graphs[0].nodes[1] (tth_hydrolase) and omits sqr2 in
  causal_graphs[0].edges[0].evidence[0].explanation (tracked as open finding cmmmech-cycle5-stage4-finding-0002
  for Stage 5 remediation).
notes: []
```
