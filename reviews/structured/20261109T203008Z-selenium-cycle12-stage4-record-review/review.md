# Cycle 12 Stage 4 record review: cmmmech:selenium (Selenium)

- Review: 20261109T203008Z-selenium-cycle12-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T20:28:00Z
- Finished UTC: 2026-11-09T20:30:08Z
- Reviewer: antigravity / cmmmech-cycle12-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/selenium.yaml (cmmmech:selenium) at commit f145e25990270f79cb760bb68e900595df4d308c. Verified CHEBI identity (CHEBI:27568 selenium atom), dated Australian 2024 criticality, the non-growing Shewanella oneidensis MR-1 selenite reduction mechanism from Li et al. (2014, Scientific Reports 4:3735, DOI:10.1038/srep03735) and Klonowska et al. (2005, Appl. Environ. Microbiol. 71:5607-5609), all three synchronized UniProtKB protein_examples (FccA P83223, CymA Q8E8S0, MtrC Q8EG34), and causal_graphs[0] (mr1_fcca_cyma_selenite_reduction_graph). Identified 1 minor graph finding (cmmmech-cycle12-stage4-finding-0002: causal_graphs[0] and protein_examples[0..1] use abbreviated 75-90 char explanations and supports: support stating direct periplasmic FccA catalysis and periplasmic/cell-envelope Se(0) accumulation, omitting conditional deletion kinetics, absence of complementation/purified-FccA assays, residual delta-cymA reduction, and predominantly intracellular plus surface particle localization) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record/pair Cycle 12 Stage 4 audit of cmmmech:selenium.

Selection: data/records/selenium.yaml at f145e25990270f79cb760bb68e900595df4d308c
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base f145e25990270f79cb760bb68e900595df4d308c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:selenium | data/records/selenium.yaml | maintained | Selenium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate data/records/selenium.yaml | passed | True | cmmmech:selenium | data/records/selenium.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### Shewanella oneidensis MR-1 selenite reduction causal graph and FccA/CymA/MtrC groundings

graph: supported. Targets: cmmmech:selenium.

All three S. oneidensis MR-1 UniProtKB protein_examples (P83223 FccA, Q8E8S0 CymA, Q8EG34 MtrC) are synchronized between mechanisms[0] and causal_graphs[0]. However, FccA/CymA protein_examples and causal_graphs[0] nodes and edges use abbreviated one-line explanations and supports: support polarity that omit key deletion-kinetic, control, and intracellular-localization caveats from mechanisms[0].

## Findings

### cmmmech-cycle12-stage4-finding-0002: Selenium Shewanella oneidensis MR-1 FccA/CymA causal graph and protein examples use abbreviated one-line explanations and unqualified direct-catalysis / periplasmic-localization claims

minor / open / confirmed; issue key: cmmmech.li2014-selenium-mr1.abbreviated-graph-evidence-and-localization-catalysis-qualifications.

In data/records/selenium.yaml (cmmmech:selenium, element, Li et al. 2014 Scientific Reports 4:3735, DOI:10.1038/srep03735, li_2014 / li_2014_supplement, and Klonowska et al. 2005 Appl. Environ. Microbiol. 71:5607-5609, klonowska_2005; mechanisms[0] mr1_selenite_reduction, lines 40-135; causal_graphs[0] mr1_fcca_cyma_selenite_reduction_graph, lines 137-283), mechanisms[0].description (line 43) and mechanisms[0].evidence[0..1,3] (lines 124-135) explicitly establish that gene-deletion phenotypes in washed non-growing Shewanella oneidensis MR-1 suspensions (OD600 1.0 in 40 mL anaerobic mineral medium under N2 with 0.5 mM selenite and 20 mM lactate at 30 C; declining Micro BCA protein biomass in Figure S2/S4) support conditional FccA and CymA involvement rather than an exclusive pathway or direct catalysis by purified FccA (no complementation or purified-FccA enzyme assay is reported; initial 12 h selenite-depletion rate drops from 1.35 +/- 0.05 umol/h in WT to 0.54 +/- 0.13 umol/h in delta-fccA [Figure 2, triplicate SE], while Figure 4 preserves substantial later residual reduction in delta-cymA and klonowska_2005 reports selenite reduction by a cymA mutant in LB), and that 48 h TEM/EDX and Se 3d XPS (Figure 5) show predominantly intracellular plus smaller surface Se(0)-assigned particles rather than exclusive periplasmic localization or an isolated phase-pure product (Table 1 provides an acid-digestion/ICP-AES selenium balance). By contrast, in causal_graphs[0] and protein_examples: nodes[0].description (line 147, 81 chars), nodes[1].description (line 178, 90 chars), and edges[1].description (line 261) assert unqualified electron transfer and direct periplasmic catalysis ('FccA directly reduces soluble selenite in the periplasm.'); nodes[4].description (elemental_se0_nanoparticles, line 245, 85 chars) states 'Red elemental selenium nanoparticles accumulated in the periplasm and cell envelope.', omitting the predominantly intracellular plus surface particle distribution in Figure 5 TEM/EDX (and extracellular/cell-attached deposits at 2 mM selenite in LB in klonowska_2005 Figure 1); and edges[0..3] (lines 248-283) carry abbreviated 75-to-87-character one-sentence evidence[0].explanation strings with supports: support on edges[0], edges[1], and edges[3] (as well as protein_examples[0..1].evidence[0] on UniProtKB:P83223 and UniProtKB:Q8E8S0, lines 75, 99, 172, 206) despite the absence of complementation or purified-FccA assays, substantial residual reduction in delta-cymA, and mixed intracellular/surface localization. In this scope, 1 record(s) (selenium) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-li2014-selenium-mr1-graph-and-protein-evidence

Update mechanisms[0].protein_examples[0..1].evidence[0] and causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0] (UniProtKB:P83223 FccA and UniProtKB:Q8E8S0 CymA) in data/records/selenium.yaml to supports: partial with synchronized deletion-mutant kinetic prose (0.54 +/- 0.13 vs 1.35 +/- 0.05 umol/h in Figure 2; 20 mM fumarate competition; residual delta-cymA reduction in Figure 4 and klonowska_2005; no complementation or purified-FccA assay), expand nodes[0..4].description to reflect non-growing washed-cell conditions and predominantly intracellular plus surface Se(0)-assigned particles (Figure 5 TEM/EDX, 48 h Se 3d XPS, Table 1 ICP-AES balance), and expand edges[0..3] (setting edges[0], edges[1], and edges[3] to supports: partial) during Stage 5 grouped remediation with canonical history provenance.

- mechanisms[0].protein_examples[0..1] and causal_graphs[0].nodes[0..1].protein_examples[0] in selenium.yaml are byte-identical with supports: partial and study-specific kinetic/control prose.
- causal_graphs[0].nodes[0..4].description and edges[0..3] in selenium.yaml align with mechanisms[0].evidence[0..3] and use supports: partial on edges[0..3].
- Matching EDIT history sidecar exists in history/records/selenium/ and passes just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-selenium-file | data/records/selenium.yaml; mechanisms[0] (lines 40-135); causal_graphs[0] (lines 137-283) | supports | Inspected data/records/selenium.yaml, comparing mechanisms[0].description, context, and evidence[0..3] (lines 43-135) against protein_examples[0..1] (lines 50-100) and causal_graphs[0] (lines 137-283). |
| ev-selenium-li2014 | DOI:10.1038/srep03735; Li et al. 2014 Scientific Reports 4:3735, Figures 2, 4, 5, Table 1, and Supplement Figures S1-S2, S4 | supports | Li et al. (2014) reported initial 12 h selenite-depletion rates of 0.54 +/- 0.13 umol/h in delta-fccA vs 1.35 +/- 0.05 umol/h in WT (Figure 2), substantial later residual reduction in delta-cymA (Figure 4), and predominantly intracellular plus smaller surface Se(0) particles by TEM/EDX and 48 h Se 3d XPS (Figure 5) without purified-FccA or complementation assays. |

## Limits And Additional Notes

- data/records/selenium.yaml uses abbreviated 75-90 char explanations and supports: support polarity on FccA/CymA protein_examples and causal_graphs[0] edges[0,1,3], omitting conditional deletion kinetics, absence of purified-FccA/complementation assays, and predominantly intracellular plus surface Se(0) localization (tracked as open finding cmmmech-cycle12-stage4-finding-0002 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T203008Z-selenium-cycle12-stage4-record-review
title: 'Cycle 12 Stage 4 record review: cmmmech:selenium (Selenium)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-11-09T20:28:00Z'
finished_at: '2026-11-09T20:30:08Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/selenium.yaml (cmmmech:selenium) at commit f145e25990270f79cb760bb68e900595df4d308c.
  Verified CHEBI identity (CHEBI:27568 selenium atom), dated Australian 2024 criticality,
  the non-growing Shewanella oneidensis MR-1 selenite reduction mechanism from Li
  et al. (2014, Scientific Reports 4:3735, DOI:10.1038/srep03735) and Klonowska et
  al. (2005, Appl. Environ. Microbiol. 71:5607-5609), all three synchronized UniProtKB
  protein_examples (FccA P83223, CymA Q8E8S0, MtrC Q8EG34), and causal_graphs[0] (mr1_fcca_cyma_selenite_reduction_graph).
  Identified 1 minor graph finding (cmmmech-cycle12-stage4-finding-0002: causal_graphs[0]
  and protein_examples[0..1] use abbreviated 75-90 char explanations and supports:
  support stating direct periplasmic FccA catalysis and periplasmic/cell-envelope
  Se(0) accumulation, omitting conditional deletion kinetics, absence of complementation/purified-FccA
  assays, residual delta-cymA reduction, and predominantly intracellular plus surface
  particle localization) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 12 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit f145e25990270f79cb760bb68e900595df4d308c.
source:
  git_revision: f145e25990270f79cb760bb68e900595df4d308c
  state: git_commit
  inputs:
  - path: data/records/selenium.yaml
    sha256: 3c88fca92fd61d7c2c88981eb4497eb71b0d4af4bfa8f2d1acd062735d59fca9
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
  - cmmmech:selenium
  selection: data/records/selenium.yaml at f145e25990270f79cb760bb68e900595df4d308c
  description: Single-record/pair Cycle 12 Stage 4 audit of cmmmech:selenium.
targets:
- target_id: cmmmech:selenium
  path: data/records/selenium.yaml
  kind: maintained
  label: Selenium
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-selenium
  name: cmmmech validate data/records/selenium.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/selenium.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - ev-selenium-file
  summary: data/records/selenium.yaml passes LinkML structural, semantic, and canonical
    top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-selenium-mr1-fcca-cyma-graph-and-proteins
  topic: Shewanella oneidensis MR-1 selenite reduction causal graph and FccA/CymA/MtrC
    groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:selenium
  evidence_ids:
  - ev-selenium-file
  - ev-selenium-li2014
  summary: 'All three S. oneidensis MR-1 UniProtKB protein_examples (P83223 FccA,
    Q8E8S0 CymA, Q8EG34 MtrC) are synchronized between mechanisms[0] and causal_graphs[0].
    However, FccA/CymA protein_examples and causal_graphs[0] nodes and edges use abbreviated
    one-line explanations and supports: support polarity that omit key deletion-kinetic,
    control, and intracellular-localization caveats from mechanisms[0].'
findings:
- finding_id: cmmmech-cycle12-stage4-finding-0002
  issue_key: cmmmech.li2014-selenium-mr1.abbreviated-graph-evidence-and-localization-catalysis-qualifications
  title: Selenium Shewanella oneidensis MR-1 FccA/CymA causal graph and protein examples
    use abbreviated one-line explanations and unqualified direct-catalysis / periplasmic-localization
    claims
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:selenium
  field_paths:
  - mechanisms[0].protein_examples[0].evidence[0].supports
  - mechanisms[0].protein_examples[0].evidence[0].explanation
  - mechanisms[0].protein_examples[1].evidence[0].supports
  - mechanisms[0].protein_examples[1].evidence[0].explanation
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[0].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].supports
  - causal_graphs[0].nodes[1].protein_examples[0].evidence[0].explanation
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].nodes[4].description
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].supports
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].explanation
  - causal_graphs[0].edges[3].description
  - causal_graphs[0].edges[3].evidence[0].supports
  - causal_graphs[0].edges[3].evidence[0].explanation
  evidence_ids:
  - ev-selenium-file
  - ev-selenium-li2014
  description: 'In data/records/selenium.yaml (cmmmech:selenium, element, Li et al.
    2014 Scientific Reports 4:3735, DOI:10.1038/srep03735, li_2014 / li_2014_supplement,
    and Klonowska et al. 2005 Appl. Environ. Microbiol. 71:5607-5609, klonowska_2005;
    mechanisms[0] mr1_selenite_reduction, lines 40-135; causal_graphs[0] mr1_fcca_cyma_selenite_reduction_graph,
    lines 137-283), mechanisms[0].description (line 43) and mechanisms[0].evidence[0..1,3]
    (lines 124-135) explicitly establish that gene-deletion phenotypes in washed non-growing
    Shewanella oneidensis MR-1 suspensions (OD600 1.0 in 40 mL anaerobic mineral medium
    under N2 with 0.5 mM selenite and 20 mM lactate at 30 C; declining Micro BCA protein
    biomass in Figure S2/S4) support conditional FccA and CymA involvement rather
    than an exclusive pathway or direct catalysis by purified FccA (no complementation
    or purified-FccA enzyme assay is reported; initial 12 h selenite-depletion rate
    drops from 1.35 +/- 0.05 umol/h in WT to 0.54 +/- 0.13 umol/h in delta-fccA [Figure
    2, triplicate SE], while Figure 4 preserves substantial later residual reduction
    in delta-cymA and klonowska_2005 reports selenite reduction by a cymA mutant in
    LB), and that 48 h TEM/EDX and Se 3d XPS (Figure 5) show predominantly intracellular
    plus smaller surface Se(0)-assigned particles rather than exclusive periplasmic
    localization or an isolated phase-pure product (Table 1 provides an acid-digestion/ICP-AES
    selenium balance). By contrast, in causal_graphs[0] and protein_examples: nodes[0].description
    (line 147, 81 chars), nodes[1].description (line 178, 90 chars), and edges[1].description
    (line 261) assert unqualified electron transfer and direct periplasmic catalysis
    (''FccA directly reduces soluble selenite in the periplasm.''); nodes[4].description
    (elemental_se0_nanoparticles, line 245, 85 chars) states ''Red elemental selenium
    nanoparticles accumulated in the periplasm and cell envelope.'', omitting the
    predominantly intracellular plus surface particle distribution in Figure 5 TEM/EDX
    (and extracellular/cell-attached deposits at 2 mM selenite in LB in klonowska_2005
    Figure 1); and edges[0..3] (lines 248-283) carry abbreviated 75-to-87-character
    one-sentence evidence[0].explanation strings with supports: support on edges[0],
    edges[1], and edges[3] (as well as protein_examples[0..1].evidence[0] on UniProtKB:P83223
    and UniProtKB:Q8E8S0, lines 75, 99, 172, 206) despite the absence of complementation
    or purified-FccA assays, substantial residual reduction in delta-cymA, and mixed
    intracellular/surface localization. In this scope, 1 record(s) (selenium) are
    affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
actions:
- action_id: act-refine-li2014-selenium-mr1-graph-and-protein-evidence
  finding_ids:
  - cmmmech-cycle12-stage4-finding-0002
  target_ids:
  - cmmmech:selenium
  description: 'Update mechanisms[0].protein_examples[0..1].evidence[0] and causal_graphs[0].nodes[0..1].protein_examples[0].evidence[0]
    (UniProtKB:P83223 FccA and UniProtKB:Q8E8S0 CymA) in data/records/selenium.yaml
    to supports: partial with synchronized deletion-mutant kinetic prose (0.54 +/-
    0.13 vs 1.35 +/- 0.05 umol/h in Figure 2; 20 mM fumarate competition; residual
    delta-cymA reduction in Figure 4 and klonowska_2005; no complementation or purified-FccA
    assay), expand nodes[0..4].description to reflect non-growing washed-cell conditions
    and predominantly intracellular plus surface Se(0)-assigned particles (Figure
    5 TEM/EDX, 48 h Se 3d XPS, Table 1 ICP-AES balance), and expand edges[0..3] (setting
    edges[0], edges[1], and edges[3] to supports: partial) during Stage 5 grouped
    remediation with canonical history provenance.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/selenium.yaml
    role: maintained_record
  acceptance_checks:
  - 'mechanisms[0].protein_examples[0..1] and causal_graphs[0].nodes[0..1].protein_examples[0]
    in selenium.yaml are byte-identical with supports: partial and study-specific
    kinetic/control prose.'
  - 'causal_graphs[0].nodes[0..4].description and edges[0..3] in selenium.yaml align
    with mechanisms[0].evidence[0..3] and use supports: partial on edges[0..3].'
  - Matching EDIT history sidecar exists in history/records/selenium/ and passes just
    check.
evidence:
- evidence_id: ev-selenium-file
  kind: record_content
  reference: data/records/selenium.yaml
  locator: mechanisms[0] (lines 40-135); causal_graphs[0] (lines 137-283)
  accessed_at: '2026-11-09T20:30:08Z'
  support: supports
  summary: Inspected data/records/selenium.yaml, comparing mechanisms[0].description,
    context, and evidence[0..3] (lines 43-135) against protein_examples[0..1] (lines
    50-100) and causal_graphs[0] (lines 137-283).
- evidence_id: ev-selenium-li2014
  kind: primary_source
  reference: DOI:10.1038/srep03735
  locator: Li et al. 2014 Scientific Reports 4:3735, Figures 2, 4, 5, Table 1, and
    Supplement Figures S1-S2, S4
  accessed_at: '2026-11-09T20:30:08Z'
  support: supports
  summary: Li et al. (2014) reported initial 12 h selenite-depletion rates of 0.54
    +/- 0.13 umol/h in delta-fccA vs 1.35 +/- 0.05 umol/h in WT (Figure 2), substantial
    later residual reduction in delta-cymA (Figure 4), and predominantly intracellular
    plus smaller surface Se(0) particles by TEM/EDX and 48 h Se 3d XPS (Figure 5)
    without purified-FccA or complementation assays.
limitations:
- 'data/records/selenium.yaml uses abbreviated 75-90 char explanations and supports:
  support polarity on FccA/CymA protein_examples and causal_graphs[0] edges[0,1,3],
  omitting conditional deletion kinetics, absence of purified-FccA/complementation
  assays, and predominantly intracellular plus surface Se(0) localization (tracked
  as open finding cmmmech-cycle12-stage4-finding-0002 for Stage 5 remediation).'
notes: []
```
