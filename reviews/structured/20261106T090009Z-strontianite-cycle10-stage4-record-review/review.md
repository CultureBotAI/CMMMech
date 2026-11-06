# Cycle 10 Stage 4 record review: cmmmech:strontianite (Strontianite)

- Review: 20261106T090009Z-strontianite-cycle10-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-06T08:42:00Z
- Finished UTC: 2026-11-06T09:00:09Z
- Reviewer: antigravity / cmmmech-cycle10-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/strontianite.yaml (cmmmech:strontianite) at commit 0ca12c227e69903577eb76e0ee8d0dbb0314fb20. Verified IMA mineral identity (orthorhombic SrCO3, grandfathered 1791), Sporosarcina pasteurii DSM 33 strontianite coating mechanism on 3D-printed PLA coupons (Natalio &amp; Maria 2024, ACS Appl. Mater. Interfaces 16(5):6327-6336, DOI:10.1021/acsami.3c13665), all synchronized UniProtKB protein_examples (UreC UniProtKB:P41020, UreB UniProtKB:P41021, UreA UniProtKB:P41022), and causal_graphs[0] (pasteurii_strontianite_pla_coating_graph). Identified 1 minor graph finding (cmmmech-cycle10-stage4-finding-0003: nodes[2..3] retain generic template descriptions repeating their capitalized node labels in parentheses and mentioning '/phosphate', edges[0] uses a generic 70-character explanation, edges[2].relationship states 'cation precipitation with carbonate/phosphate', and edges[1..2] interpolate capitalized node labels mid-sentence with unqualified supports: support on edges[1]) for Stage 5 grouped remediation.

## Scope And Provenance

Single-record Cycle 10 Stage 4 audit of cmmmech:strontianite.

Selection: data/records/strontianite.yaml at 0ca12c227e69903577eb76e0ee8d0dbb0314fb20
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0ca12c227e69903577eb76e0ee8d0dbb0314fb20.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:strontianite | data/records/strontianite.yaml | maintained | Strontianite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate strontianite.yaml | passed | True | cmmmech:strontianite | data/records/strontianite.yaml passes LinkML structural, semantic, and canonical top-level key-order validation with 0 errors. |

## Scientific And Domain Assessments

### Sporosarcina pasteurii DSM 33 strontianite PLA coating causal graph and UreABC groundings

graph: supported. Targets: cmmmech:strontianite.

All Sporosarcina pasteurii UreABC UniProtKB protein_examples are accurately grounded and synchronized between mechanisms[0] and causal_graphs[0]. However, nodes[2..3] and edges[0..2] retain generic template descriptions, '/phosphate' wording in a SrCl2-urea system, mid-sentence capitalized label interpolations, and supports: support on edges[1].

## Findings

### cmmmech-cycle10-stage4-finding-0003: Sporosarcina pasteurii causal graphs in strontianite.yaml and smithsonite.yaml retain template node/edge descriptions, erroneous carbonate/phosphate wording, and uncharacterized FTIR/SEM-EDS claims in smithsonite.yaml

minor / open / confirmed; issue key: cmmmech.pasteurii-strontianite-smithsonite.template-descriptions-and-uncharacterized-modality-claims.

In data/records/strontianite.yaml (cmmmech:strontianite, mineral, Natalio &amp; Maria 2024 ACS Appl. Mater. Interfaces 16(5):6327-6336, DOI:10.1021/acsami.3c13665; causal_graphs[0] pasteurii_strontianite_pla_coating_graph, lines 190-338) and data/records/smithsonite.yaml (cmmmech:smithsonite, mineral, Huang et al. 2025 Biogeotechnics 3:100106, DOI:10.1016/j.bgtech.2024.100106; causal_graphs[0] pasteurii_smithsonite_precipitation_graph, lines 192-341), nodes[2].description (strontianite.yaml lines 299-300) and nodes[3].description (strontianite.yaml line 305; smithsonite.yaml lines 307-308) retain generic template descriptions repeating their capitalized node labels in parentheses ('Dissolved cations (Dissolved Sr2+ (SrCl2) in urea-containing medium) undergoing carbonate/phosphate precipitation.' and 'Solid mineral phase (&lt;Label&gt;) formed via ureolytic alkalinization...'), edges[2].relationship (strontianite.yaml line 331; smithsonite.yaml line 334) states 'cation precipitation with carbonate/phosphate' despite both studies using phosphate-free chloride-urea media (SrCl2 and ZnCl2), edges[0].evidence[0].explanation (strontianite.yaml line 316; smithsonite.yaml line 319) uses the generic 70-character template string, and edges[1..2] (strontianite.yaml lines 317-338; smithsonite.yaml lines 320-341) interpolate capitalized node labels mid-sentence with generic one-line explanations and supports: support on edges[1] despite mechanisms[0] noting the absence of urease knockout/inhibition or matched-pH abiotic controls (supports: partial). Additionally, in data/records/smithsonite.yaml, edges[2].evidence[0].explanation (lines 340-341) cites 'XRD, FTIR, SEM-EDS, and solution Zn depletion analysis in huang2025', whereas mechanisms[0].evidence[0..1] (lines 66-87) documents only powder XRD (PDF 08-0449 on 105 C-dried precipitate at 10 mmol/L Zn and 100 mmol/L urea, Figure 2U), AAS solution Zn removal (99.89% at 1 mmol/L Zn to 40.67% at 10 mmol/L Zn, Figure 2M), and Nessler ammonium / pH assays without FTIR or SEM-EDS. In this scope, 1 record(s) (strontianite) are affected.

## Recommended Actions And Acceptance Checks

### act-refine-pasteurii-strontianite-and-smithsonite-graphs

Replace generic parenthetical template descriptions and erroneous '/phosphate' wording on nodes[2..3].description and edges[2].relationship, qualify edges[1].evidence[0].supports to partial to reflect the absence of urease-inhibition or matched-pH abiotic controls, replace mid-sentence capitalized node labels and generic edge explanations across data/records/strontianite.yaml and data/records/smithsonite.yaml, and remove the unsupported 'FTIR, SEM-EDS' claim from smithsonite.yaml edges[2].evidence[0].explanation during Stage 5 grouped remediation with canonical history provenance.

- nodes[2..3].description and edges[2].relationship in strontianite.yaml and smithsonite.yaml remove template label duplication and '/phosphate' wording.
- edges[0..2] in strontianite.yaml and smithsonite.yaml use lowercase mid-sentence prose, study-specific explanations, and supports: partial where control limitations apply.
- smithsonite.yaml edges[2].evidence[0].explanation cites only powder XRD (PDF 08-0449, Figure 2U) and AAS/Nessler/pH solution assays from huang2025 without claiming FTIR or SEM-EDS.
- Matching EDIT history sidecars exist in history/records/ and pass just check.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-strontianite-file | data/records/strontianite.yaml; mechanisms[0] (lines 44-102); causal_graphs[0] (lines 190-338) | supports | Inspected data/records/strontianite.yaml, verifying mechanisms[0] (lines 44-102) against causal_graphs[0].nodes[2..3] (lines 296-306) and causal_graphs[0].edges[0..2] (lines 308-338). |
| ev-strontianite-natalio2024 | DOI:10.1021/acsami.3c13665; Natalio &amp; Maria 2024 ACS Appl. Mater. Interfaces 16(5):6327-6336, Experimental Section, Figures 3-4, SI Figure S4 p. S7 | supports | Natalio &amp; Maria (2024) document Sporosarcina pasteurii DSM 33 culture-associated strontianite coating (36 +/- 3 mg coating mass, 45 +/- 6 um SEM thickness, 18 +/- 2 nm Scherrer crystallite estimate) on 1.5 x 1.5 x 0.1 cm 3D-printed PLA coupons in 333 mM urea + SrCl2·6H2O medium at 30 C for 1 week, with no coatings in uninoculated controls (Figure S4 p. S7) and no urease-knockout or matched-pH abiotic control series. |

## Limits And Additional Notes

- data/records/strontianite.yaml retains generic template node/edge descriptions, '/phosphate' wording, mid-sentence capitalized label interpolations, and unqualified edge[1] support in causal_graphs[0] (tracked as open finding cmmmech-cycle10-stage4-finding-0003 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T090009Z-strontianite-cycle10-stage4-record-review
title: 'Cycle 10 Stage 4 record review: cmmmech:strontianite (Strontianite)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-11-06T08:42:00Z'
finished_at: '2026-11-06T09:00:09Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Reviewed data/records/strontianite.yaml (cmmmech:strontianite) at commit
  0ca12c227e69903577eb76e0ee8d0dbb0314fb20. Verified IMA mineral identity (orthorhombic
  SrCO3, grandfathered 1791), Sporosarcina pasteurii DSM 33 strontianite coating mechanism
  on 3D-printed PLA coupons (Natalio & Maria 2024, ACS Appl. Mater. Interfaces 16(5):6327-6336,
  DOI:10.1021/acsami.3c13665), all synchronized UniProtKB protein_examples (UreC UniProtKB:P41020,
  UreB UniProtKB:P41021, UreA UniProtKB:P41022), and causal_graphs[0] (pasteurii_strontianite_pla_coating_graph).
  Identified 1 minor graph finding (cmmmech-cycle10-stage4-finding-0003: nodes[2..3]
  retain generic template descriptions repeating their capitalized node labels in
  parentheses and mentioning ''/phosphate'', edges[0] uses a generic 70-character
  explanation, edges[2].relationship states ''cation precipitation with carbonate/phosphate'',
  and edges[1..2] interpolate capitalized node labels mid-sentence with unqualified
  supports: support on edges[1]) for Stage 5 grouped remediation.'
reviewer:
  identity: antigravity / cmmmech-cycle10-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 10 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit 0ca12c227e69903577eb76e0ee8d0dbb0314fb20.
source:
  git_revision: 0ca12c227e69903577eb76e0ee8d0dbb0314fb20
  state: git_commit
  inputs:
  - path: data/records/strontianite.yaml
    sha256: fd0ba6d8bd4e69e250e0e0109e01dcccb86771cbcfb8e9b0f6ef6fd890275d66
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
  - cmmmech:strontianite
  selection: data/records/strontianite.yaml at 0ca12c227e69903577eb76e0ee8d0dbb0314fb20
  description: Single-record Cycle 10 Stage 4 audit of cmmmech:strontianite.
targets:
- target_id: cmmmech:strontianite
  path: data/records/strontianite.yaml
  kind: maintained
  label: Strontianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-strontianite
  name: cmmmech validate strontianite.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/strontianite.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:strontianite
  evidence_ids:
  - ev-strontianite-file
  summary: data/records/strontianite.yaml passes LinkML structural, semantic, and
    canonical top-level key-order validation with 0 errors.
assessments:
- assessment_id: assess-strontianite-pasteurii-graph-and-proteins
  topic: Sporosarcina pasteurii DSM 33 strontianite PLA coating causal graph and UreABC
    groundings
  area: graph
  outcome: supported
  target_ids:
  - cmmmech:strontianite
  evidence_ids:
  - ev-strontianite-file
  - ev-strontianite-natalio2024
  summary: 'All Sporosarcina pasteurii UreABC UniProtKB protein_examples are accurately
    grounded and synchronized between mechanisms[0] and causal_graphs[0]. However,
    nodes[2..3] and edges[0..2] retain generic template descriptions, ''/phosphate''
    wording in a SrCl2-urea system, mid-sentence capitalized label interpolations,
    and supports: support on edges[1].'
findings:
- finding_id: cmmmech-cycle10-stage4-finding-0003
  issue_key: cmmmech.pasteurii-strontianite-smithsonite.template-descriptions-and-uncharacterized-modality-claims
  title: Sporosarcina pasteurii causal graphs in strontianite.yaml and smithsonite.yaml
    retain template node/edge descriptions, erroneous carbonate/phosphate wording,
    and uncharacterized FTIR/SEM-EDS claims in smithsonite.yaml
  severity: minor
  category: graph
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:strontianite
  field_paths:
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].edges[0].evidence[0].explanation
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].supports
  - causal_graphs[0].edges[1].evidence[0].explanation
  - causal_graphs[0].edges[2].relationship
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].explanation
  evidence_ids:
  - ev-strontianite-file
  - ev-strontianite-natalio2024
  description: 'In data/records/strontianite.yaml (cmmmech:strontianite, mineral,
    Natalio & Maria 2024 ACS Appl. Mater. Interfaces 16(5):6327-6336, DOI:10.1021/acsami.3c13665;
    causal_graphs[0] pasteurii_strontianite_pla_coating_graph, lines 190-338) and
    data/records/smithsonite.yaml (cmmmech:smithsonite, mineral, Huang et al. 2025
    Biogeotechnics 3:100106, DOI:10.1016/j.bgtech.2024.100106; causal_graphs[0] pasteurii_smithsonite_precipitation_graph,
    lines 192-341), nodes[2].description (strontianite.yaml lines 299-300) and nodes[3].description
    (strontianite.yaml line 305; smithsonite.yaml lines 307-308) retain generic template
    descriptions repeating their capitalized node labels in parentheses (''Dissolved
    cations (Dissolved Sr2+ (SrCl2) in urea-containing medium) undergoing carbonate/phosphate
    precipitation.'' and ''Solid mineral phase (<Label>) formed via ureolytic alkalinization...''),
    edges[2].relationship (strontianite.yaml line 331; smithsonite.yaml line 334)
    states ''cation precipitation with carbonate/phosphate'' despite both studies
    using phosphate-free chloride-urea media (SrCl2 and ZnCl2), edges[0].evidence[0].explanation
    (strontianite.yaml line 316; smithsonite.yaml line 319) uses the generic 70-character
    template string, and edges[1..2] (strontianite.yaml lines 317-338; smithsonite.yaml
    lines 320-341) interpolate capitalized node labels mid-sentence with generic one-line
    explanations and supports: support on edges[1] despite mechanisms[0] noting the
    absence of urease knockout/inhibition or matched-pH abiotic controls (supports:
    partial). Additionally, in data/records/smithsonite.yaml, edges[2].evidence[0].explanation
    (lines 340-341) cites ''XRD, FTIR, SEM-EDS, and solution Zn depletion analysis
    in huang2025'', whereas mechanisms[0].evidence[0..1] (lines 66-87) documents only
    powder XRD (PDF 08-0449 on 105 C-dried precipitate at 10 mmol/L Zn and 100 mmol/L
    urea, Figure 2U), AAS solution Zn removal (99.89% at 1 mmol/L Zn to 40.67% at
    10 mmol/L Zn, Figure 2M), and Nessler ammonium / pH assays without FTIR or SEM-EDS.
    In this scope, 1 record(s) (strontianite) are affected.'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
actions:
- action_id: act-refine-pasteurii-strontianite-and-smithsonite-graphs
  finding_ids:
  - cmmmech-cycle10-stage4-finding-0003
  target_ids:
  - cmmmech:strontianite
  description: Replace generic parenthetical template descriptions and erroneous '/phosphate'
    wording on nodes[2..3].description and edges[2].relationship, qualify edges[1].evidence[0].supports
    to partial to reflect the absence of urease-inhibition or matched-pH abiotic controls,
    replace mid-sentence capitalized node labels and generic edge explanations across
    data/records/strontianite.yaml and data/records/smithsonite.yaml, and remove the
    unsupported 'FTIR, SEM-EDS' claim from smithsonite.yaml edges[2].evidence[0].explanation
    during Stage 5 grouped remediation with canonical history provenance.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
  acceptance_checks:
  - nodes[2..3].description and edges[2].relationship in strontianite.yaml and smithsonite.yaml
    remove template label duplication and '/phosphate' wording.
  - 'edges[0..2] in strontianite.yaml and smithsonite.yaml use lowercase mid-sentence
    prose, study-specific explanations, and supports: partial where control limitations
    apply.'
  - smithsonite.yaml edges[2].evidence[0].explanation cites only powder XRD (PDF 08-0449,
    Figure 2U) and AAS/Nessler/pH solution assays from huang2025 without claiming
    FTIR or SEM-EDS.
  - Matching EDIT history sidecars exist in history/records/ and pass just check.
evidence:
- evidence_id: ev-strontianite-file
  kind: record_content
  reference: data/records/strontianite.yaml
  locator: mechanisms[0] (lines 44-102); causal_graphs[0] (lines 190-338)
  accessed_at: '2026-11-06T09:00:09Z'
  support: supports
  summary: Inspected data/records/strontianite.yaml, verifying mechanisms[0] (lines
    44-102) against causal_graphs[0].nodes[2..3] (lines 296-306) and causal_graphs[0].edges[0..2]
    (lines 308-338).
- evidence_id: ev-strontianite-natalio2024
  kind: primary_source
  reference: DOI:10.1021/acsami.3c13665
  locator: Natalio & Maria 2024 ACS Appl. Mater. Interfaces 16(5):6327-6336, Experimental
    Section, Figures 3-4, SI Figure S4 p. S7
  accessed_at: '2026-11-06T09:00:09Z'
  support: supports
  summary: Natalio & Maria (2024) document Sporosarcina pasteurii DSM 33 culture-associated
    strontianite coating (36 +/- 3 mg coating mass, 45 +/- 6 um SEM thickness, 18
    +/- 2 nm Scherrer crystallite estimate) on 1.5 x 1.5 x 0.1 cm 3D-printed PLA coupons
    in 333 mM urea + SrCl2·6H2O medium at 30 C for 1 week, with no coatings in uninoculated
    controls (Figure S4 p. S7) and no urease-knockout or matched-pH abiotic control
    series.
limitations:
- data/records/strontianite.yaml retains generic template node/edge descriptions,
  '/phosphate' wording, mid-sentence capitalized label interpolations, and unqualified
  edge[1] support in causal_graphs[0] (tracked as open finding cmmmech-cycle10-stage4-finding-0003
  for Stage 5 remediation).
notes: []
```
