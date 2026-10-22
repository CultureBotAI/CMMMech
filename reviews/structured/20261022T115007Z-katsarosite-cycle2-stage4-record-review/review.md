# Cycle 2 Stage 4 record review: cmmmech:katsarosite (Katsarosite)

- Review: 20261022T115007Z-katsarosite-cycle2-stage4-record-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-22T11:47:00Z
- Finished UTC: 2026-10-22T11:50:07Z
- Reviewer: antigravity / cmmmech-cycle2-stage4-record-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reviewed data/records/katsarosite.yaml (cmmmech:katsarosite) at commit 547283a882c1d657f934434f2eb5ea9a1418771a. Katsarosite (Zn(C2O4)·2H2O, IMA:2020-014) carries accurate mineral identity and crystallography from Giester et al. (2023, DOI:10.1007/s00710-023-00810-9), Aspergillus niger co-culture zinc oxalate biomineralization evidence from Sazanova et al. (2025, DOI:10.3390/cryst15020118), structured IMA:2020-014 identifier added in Cycle 1 Stage 5, and live-verified UniProtKB grounding (UniProtKB:A0A254TZW7 CexA in Aspergillus niger ATCC 13496 NCBITaxon:1459638). However, while sibling Aspergillus niger oxalate biomineralization causal graphs (falottaite, lindbergite, moolooite, hopeite, humboldtine, whewellite) were updated in Cycle 2 Stage 2 to use the new solubilizes predicate introduced in Cycle 1 Stage 6 (cmmmech-infra-0003), niger_associated_zinc_oxalate_formation_graph in katsarosite.yaml still uses the legacy chelates predicate on its secreted_organic_acids -&gt; znso4_hopeite_culture_substrate dissolution edge. Recorded open minor finding cmmmech-cycle2-stage4-finding-0003 for Stage 5 remediation.

## Scope And Provenance

Single-record Cycle 2 Stage 4 audit of cmmmech:katsarosite.

Selection: data/records/katsarosite.yaml at 547283a882c1d657f934434f2eb5ea9a1418771a
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 547283a882c1d657f934434f2eb5ea9a1418771a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:katsarosite | data/records/katsarosite.yaml | maintained | Katsarosite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| cmmmech validate katsarosite.yaml | passed | True | cmmmech:katsarosite | data/records/katsarosite.yaml passes LinkML structural and semantic validation. |

## Scientific And Domain Assessments

### Katsarosite formula (Zn(C2O4)·2H2O, IMA:2020-014) and Aspergillus niger CexA grounding

identity: supported. Targets: cmmmech:katsarosite.

Katsarosite species identity (IMA:2020-014, Zn(C2O4)·2H2O), Aspergillus niger Ch4/07 + Beauveria bassiana co-culture biomineralization mechanism, and UniProtKB:A0A254TZW7 (CexA) protein grounding are accurately supported by primary sources.

### CausalPredicateEnum selection on secreted_organic_acids -&gt; znso4_hopeite_culture_substrate

graph: concern. Targets: cmmmech:katsarosite.

In niger_associated_zinc_oxalate_formation_graph, the edge secreted_organic_acids -&gt; znso4_hopeite_culture_substrate ('fungal acidification, hopeite dissolution, and Zn(II) oxalate complexation') still uses predicate: chelates instead of predicate: solubilizes used across the rest of the Aspergillus niger oxalate biomineralization cohort (falottaite, lindbergite, moolooite).

## Findings

### cmmmech-cycle2-stage4-finding-0003: cmmmech:katsarosite causal graph still uses legacy chelates predicate instead of solubilizes on organic-acid hopeite dissolution edge

minor / open / confirmed; issue key: cmmmech.katsarosite.legacy-chelates-predicate-on-hopeite-solubilization.

In Cycle 1 Stage 6 (cmmmech-infra-0003, PR #809), solubilizes was added to CausalPredicateEnum specifically so organic-acid mineral dissolution edges in Aspergillus niger oxalate biomineralization graphs (falottaite, katsarosite, lindbergite, moolooite) would not overload chelates. While falottaite, lindbergite, and moolooite were updated to predicate: solubilizes in Cycle 2 Stage 2 (PR #811), data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph) still uses predicate: chelates on the edge secreted_organic_acids -&gt; znso4_hopeite_culture_substrate (relationship: 'fungal acidification, hopeite dissolution, and Zn(II) oxalate complexation').

## Recommended Actions And Acceptance Checks

### action-update-katsarosite-edge-predicate-to-solubilizes

Update predicate from chelates to solubilizes on the secreted_organic_acids -&gt; znso4_hopeite_culture_substrate edge in data/records/katsarosite.yaml and record an EDIT history sidecar during Stage 5.

- In data/records/katsarosite.yaml, niger_associated_zinc_oxalate_formation_graph edge secreted_organic_acids -&gt; znso4_hopeite_culture_substrate uses predicate: solubilizes.
- A matching EDIT history sidecar exists in history/records/katsarosite/ and passes cmmmech validate-history --base main.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-katsarosite-file | data/records/katsarosite.yaml; lines 1-264 | supports | Inspected data/records/katsarosite.yaml: IMA:2020-014 identifier and UniProtKB:A0A254TZW7 grounding are present, while niger_associated_zinc_oxalate_formation_graph edge secreted_organic_acids -&gt; znso4_hopeite_culture_substrate at lines 229-236 retains predicate: chelates. |
| ev-katsarosite-giester2023 | DOI:10.1007/s00710-023-00810-9; Giester et al. 2023 Mineralogy and Petrology 117:259-267 | supports | Supports IMA 2020-014 approval and monoclinic P21/n structure of katsarosite, Zn(C2O4)·2H2O. |
| ev-katsarosite-sazanova2025 | DOI:10.3390/cryst15020118; Sazanova et al. 2025 Crystals 15(2):118 | supports | Supports organic-acid dissolution of hopeite/ZnSO4 substrate and monoclinic katsarosite crystallization in Aspergillus niger Ch4/07 + Beauveria bassiana co-culture. |

## Limits And Additional Notes

- Edge secreted_organic_acids -&gt; znso4_hopeite_culture_substrate in niger_associated_zinc_oxalate_formation_graph retains legacy predicate: chelates instead of predicate: solubilizes (tracked as open finding cmmmech-cycle2-stage4-finding-0003 for Stage 5 remediation).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T115007Z-katsarosite-cycle2-stage4-record-review
title: 'Cycle 2 Stage 4 record review: cmmmech:katsarosite (Katsarosite)'
repository: CultureBotAI/CMMMech
kind: record
started_at: '2026-10-22T11:47:00Z'
finished_at: '2026-10-22T11:50:07Z'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reviewed data/records/katsarosite.yaml (cmmmech:katsarosite) at commit 547283a882c1d657f934434f2eb5ea9a1418771a.
  Katsarosite (Zn(C2O4)·2H2O, IMA:2020-014) carries accurate mineral identity and
  crystallography from Giester et al. (2023, DOI:10.1007/s00710-023-00810-9), Aspergillus
  niger co-culture zinc oxalate biomineralization evidence from Sazanova et al. (2025,
  DOI:10.3390/cryst15020118), structured IMA:2020-014 identifier added in Cycle 1
  Stage 5, and live-verified UniProtKB grounding (UniProtKB:A0A254TZW7 CexA in Aspergillus
  niger ATCC 13496 NCBITaxon:1459638). However, while sibling Aspergillus niger oxalate
  biomineralization causal graphs (falottaite, lindbergite, moolooite, hopeite, humboldtine,
  whewellite) were updated in Cycle 2 Stage 2 to use the new solubilizes predicate
  introduced in Cycle 1 Stage 6 (cmmmech-infra-0003), niger_associated_zinc_oxalate_formation_graph
  in katsarosite.yaml still uses the legacy chelates predicate on its secreted_organic_acids
  -> znso4_hopeite_culture_substrate dissolution edge. Recorded open minor finding
  cmmmech-cycle2-stage4-finding-0003 for Stage 5 remediation.
reviewer:
  identity: antigravity / cmmmech-cycle2-stage4-record-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of Cycle 2 Stage 4 record_review
    (.claude/skills/review-yaml-record/SKILL.md) against frozen commit 547283a882c1d657f934434f2eb5ea9a1418771a.
source:
  git_revision: 547283a882c1d657f934434f2eb5ea9a1418771a
  state: git_commit
  inputs:
  - path: data/records/katsarosite.yaml
    sha256: 2b5712225072094be6d4d42379dbd9a796c6f94b5b063349fbea290b655e31c9
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
scope:
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:katsarosite
  selection: data/records/katsarosite.yaml at 547283a882c1d657f934434f2eb5ea9a1418771a
  description: Single-record Cycle 2 Stage 4 audit of cmmmech:katsarosite.
targets:
- target_id: cmmmech:katsarosite
  path: data/records/katsarosite.yaml
  kind: maintained
  label: Katsarosite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: schema
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: validator
checks:
- check_id: cmmmech-validate-katsarosite
  name: cmmmech validate katsarosite.yaml
  status: passed
  required: true
  command: .venv/bin/cmmmech validate data/records/katsarosite.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:katsarosite
  evidence_ids:
  - ev-katsarosite-file
  summary: data/records/katsarosite.yaml passes LinkML structural and semantic validation.
assessments:
- assessment_id: assess-katsarosite-identity-and-protein
  topic: Katsarosite formula (Zn(C2O4)·2H2O, IMA:2020-014) and Aspergillus niger CexA
    grounding
  area: identity
  outcome: supported
  target_ids:
  - cmmmech:katsarosite
  evidence_ids:
  - ev-katsarosite-file
  - ev-katsarosite-giester2023
  - ev-katsarosite-sazanova2025
  summary: Katsarosite species identity (IMA:2020-014, Zn(C2O4)·2H2O), Aspergillus
    niger Ch4/07 + Beauveria bassiana co-culture biomineralization mechanism, and
    UniProtKB:A0A254TZW7 (CexA) protein grounding are accurately supported by primary
    sources.
- assessment_id: assess-katsarosite-causal-edge-predicate
  topic: CausalPredicateEnum selection on secreted_organic_acids -> znso4_hopeite_culture_substrate
  area: graph
  outcome: concern
  target_ids:
  - cmmmech:katsarosite
  evidence_ids:
  - ev-katsarosite-file
  summary: 'In niger_associated_zinc_oxalate_formation_graph, the edge secreted_organic_acids
    -> znso4_hopeite_culture_substrate (''fungal acidification, hopeite dissolution,
    and Zn(II) oxalate complexation'') still uses predicate: chelates instead of predicate:
    solubilizes used across the rest of the Aspergillus niger oxalate biomineralization
    cohort (falottaite, lindbergite, moolooite).'
findings:
- finding_id: cmmmech-cycle2-stage4-finding-0003
  issue_key: cmmmech.katsarosite.legacy-chelates-predicate-on-hopeite-solubilization
  title: cmmmech:katsarosite causal graph still uses legacy chelates predicate instead
    of solubilizes on organic-acid hopeite dissolution edge
  category: consistency
  severity: minor
  certainty: confirmed
  status: open
  target_ids:
  - cmmmech:katsarosite
  evidence_ids:
  - ev-katsarosite-file
  description: 'In Cycle 1 Stage 6 (cmmmech-infra-0003, PR #809), solubilizes was
    added to CausalPredicateEnum specifically so organic-acid mineral dissolution
    edges in Aspergillus niger oxalate biomineralization graphs (falottaite, katsarosite,
    lindbergite, moolooite) would not overload chelates. While falottaite, lindbergite,
    and moolooite were updated to predicate: solubilizes in Cycle 2 Stage 2 (PR #811),
    data/records/katsarosite.yaml (niger_associated_zinc_oxalate_formation_graph)
    still uses predicate: chelates on the edge secreted_organic_acids -> znso4_hopeite_culture_substrate
    (relationship: ''fungal acidification, hopeite dissolution, and Zn(II) oxalate
    complexation'').'
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
actions:
- action_id: action-update-katsarosite-edge-predicate-to-solubilizes
  finding_ids:
  - cmmmech-cycle2-stage4-finding-0003
  target_ids:
  - cmmmech:katsarosite
  description: Update predicate from chelates to solubilizes on the secreted_organic_acids
    -> znso4_hopeite_culture_substrate edge in data/records/katsarosite.yaml and record
    an EDIT history sidecar during Stage 5.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/katsarosite.yaml
    role: maintained_record
  acceptance_checks:
  - 'In data/records/katsarosite.yaml, niger_associated_zinc_oxalate_formation_graph
    edge secreted_organic_acids -> znso4_hopeite_culture_substrate uses predicate:
    solubilizes.'
  - A matching EDIT history sidecar exists in history/records/katsarosite/ and passes
    cmmmech validate-history --base main.
evidence:
- evidence_id: ev-katsarosite-file
  kind: record_content
  reference: data/records/katsarosite.yaml
  locator: lines 1-264
  accessed_at: '2026-10-22T11:50:07Z'
  support: supports
  summary: 'Inspected data/records/katsarosite.yaml: IMA:2020-014 identifier and UniProtKB:A0A254TZW7
    grounding are present, while niger_associated_zinc_oxalate_formation_graph edge
    secreted_organic_acids -> znso4_hopeite_culture_substrate at lines 229-236 retains
    predicate: chelates.'
- evidence_id: ev-katsarosite-giester2023
  kind: primary_source
  reference: DOI:10.1007/s00710-023-00810-9
  locator: Giester et al. 2023 Mineralogy and Petrology 117:259-267
  accessed_at: '2026-10-22T11:50:07Z'
  support: supports
  summary: Supports IMA 2020-014 approval and monoclinic P21/n structure of katsarosite,
    Zn(C2O4)·2H2O.
- evidence_id: ev-katsarosite-sazanova2025
  kind: primary_source
  reference: DOI:10.3390/cryst15020118
  locator: Sazanova et al. 2025 Crystals 15(2):118
  accessed_at: '2026-10-22T11:50:07Z'
  support: supports
  summary: Supports organic-acid dissolution of hopeite/ZnSO4 substrate and monoclinic
    katsarosite crystallization in Aspergillus niger Ch4/07 + Beauveria bassiana co-culture.
limitations:
- 'Edge secreted_organic_acids -> znso4_hopeite_culture_substrate in niger_associated_zinc_oxalate_formation_graph
  retains legacy predicate: chelates instead of predicate: solubilizes (tracked as
  open finding cmmmech-cycle2-stage4-finding-0003 for Stage 5 remediation).'
notes: []
```
