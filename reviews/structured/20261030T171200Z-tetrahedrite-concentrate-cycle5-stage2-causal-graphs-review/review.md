# Cycle 5 Stage 2 causal-graph review of Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate)

- Review: 20261030T171200Z-tetrahedrite-concentrate-cycle5-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-30T17:10:00Z
- Finished UTC: 2026-10-30T17:12:00Z
- Reviewer: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate) passes Cycle 5 Stage 2 causal-graph review (scientific_review: true) at SHA-256 c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8: Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph, mechanism_ref: acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate uses predicate 'solubilizes' (supports: partial) and edge solid_feed_substrate -&gt; solubilized_metal_species uses predicate 'produces' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate from acts_on to solubilizes (retaining supports: partial for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans DSM 14882 in sqr_reductase -&gt; tth_hydrolase, and replaced template node/edge descriptions with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details. Updated causal_graphs[0].description from 'Cu, Sb, Zn, and Fe mobilization from mixed tetrahedrite concentrate' to 'Cu, Zn, Ag, and sulfate mobilization (with transient Sb release) from mixed tetrahedrite concentrate' to match the product node and edge descriptions in Kupka et al. (2025) (kupka_2025).

## Scope And Provenance

Cycle 5 Stage 2 causal-graph review of data/records/tetrahedrite-concentrate.yaml (SHA-256 c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8) and its canonical EDIT history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml, history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml) verifying full synchronization between causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) and mechanisms[0] (acidophile_associated_metal_mobilization).

Selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:tetrahedrite-concentrate
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2f2de84859ee4156bb09f2a0110d35edc48b8020.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tetrahedrite-concentrate | data/records/tetrahedrite-concentrate.yaml | maintained | Tetrahedrite concentrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:tetrahedrite-concentrate | Checked 668 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:tetrahedrite-concentrate | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Synchronization of causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph) with mechanisms[0] (acidophile_associated_metal_mobilization) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0)

graph: supported. Targets: cmmmech:tetrahedrite-concentrate.

Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph, mechanism_ref: acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate uses predicate 'solubilizes' (supports: partial) and edge solid_feed_substrate -&gt; solubilized_metal_species uses predicate 'produces' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate from acts_on to solubilizes (retaining supports: partial for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans DSM 14882 in sqr_reductase -&gt; tth_hydrolase, and replaced template node/edge descriptions with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details. Updated causal_graphs[0].description from 'Cu, Sb, Zn, and Fe mobilization from mixed tetrahedrite concentrate' to 'Cu, Zn, Ag, and sulfate mobilization (with transient Sb release) from mixed tetrahedrite concentrate' to match the product node and edge descriptions in Kupka et al. (2025) (kupka_2025).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:tetrahedrite-concentrate.

data/records/tetrahedrite-concentrate.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml, history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml, latest SHA-256 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/tetrahedrite-concentrate.yaml; Working-tree record data/records/tetrahedrite-concentrate.yaml (causal_graphs[0]: ferrooxidans_tetrahedrite_bioleaching_graph) | supports | Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph, mechanism_ref: acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate uses predicate 'solubilizes' (supports: partial) and edge solid_feed_substrate -&gt; solubilized_metal_species uses predicate 'produces' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate from acts_on to solubilizes (retaining supports: partial for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans DSM 14882 in sqr_reductase -&gt; tth_hydrolase, and replaced template node/edge descriptions with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details. Updated causal_graphs[0].description from 'Cu, Sb, Zn, and Fe mobilization from mixed tetrahedrite concentrate' to 'Cu, Zn, Ag, and sulfate mobilization (with transient Sb release) from mixed tetrahedrite concentrate' to match the product node and edge descriptions in Kupka et al. (2025) (kupka_2025). |
| primary_source | DOI:10.1007/s40831-025-01089-0; kupka_2025: Kupka D et al. (2025). Bioleaching of Tetrahedrite by Iron- and Sulfur-Oxidizing Bacteria. Journal of Sustainable Metallurgy 11:3685-3699. DOI 10.1007/s40831-025-01089-0. Complete 15-page original article, Figures 1-8, Tables 1-2 and seven-page supplement with Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0) | supports | Separate inoculated laboratory cultures showed greater copper mobilization and sulfate accumulation than the uninoculated acidic control. The two organisms denote separate culture arms, not a consortium. Dissolved copper and sulfate trajectories, oxygen consumption and altered grain surfaces support culture-associated oxidative leaching, while iron cycling is the authors' mechanistic interpretation. No enzyme-specific or genetic cause was established. The response was element dependent: dissolved antimony rose early and subsequently declined, and the abiotic treatment released more iron and manganese than the inoculated treatments in the reported day-35 comparison. Copper and sulfur depletion with antimony and iron enrichment in selected alteration rims does not demonstrate a pure secondary mineral product or complete dissolution of every grain. Substrate-edge evidence (kupka_2025, supports: partial): Kupka et al. (2025) demonstrate higher Cu mobilization, sulfate accumulation, and O2 consumption in inoculated flasks than in the autoclaved control over 120 days, though unbuffered pH and ferric-iron trajectories were not matched independently of living cells. Product-edge evidence (kupka_2025, supports: support): Kupka et al. (2025) Figures 2–5 and S12 document increased dissolved Cu, sulfate, Zn, and Ag trajectories and transient Sb release in 0.2-um-filtered leachates relative to abiotic controls. |
| edit_history | history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml; Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml | supports | Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml (SHA-256 5c3f15468c3f48432f41a905a701aadcaa1d4eae26c6f74eb343545823bdbb35): Upgrade tetrahedrite-concentrate causal_graphs[0] lixiviant predicate to solubilizes and ground node/edge text in kupka_2025 — Upgraded acidic_ferric_sulfate_lixiviant -&gt; solid_feed_substrate from acts_on to solubilizes (retaining supports: partial for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans DSM 14882 in sqr_reductase -&gt; tth_hydrolase, and replaced template node/edge descriptions with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details. |
| edit_history_2 | history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml; Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml | supports | Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml (SHA-256 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a): Align tetrahedrite-concentrate causal_graphs[0].description with measured Cu, Zn, Ag, and sulfate mobilization in kupka_2025 — Updated causal_graphs[0].description from 'Cu, Sb, Zn, and Fe mobilization from mixed tetrahedrite concentrate' to 'Cu, Zn, Ag, and sulfate mobilization (with transient Sb release) from mixed tetrahedrite concentrate' to match the product node and edge descriptions in Kupka et al. (2025) (kupka_2025). |
| validation | data/records/tetrahedrite-concentrate.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/tetrahedrite-concentrate.yaml and history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml, history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml pass strict LinkML schema and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T171200Z-tetrahedrite-concentrate-cycle5-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 5 Stage 2 causal-graph review of Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate)
started_at: '2026-10-30T17:10:00Z'
finished_at: '2026-10-30T17:12:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle5-stage2-causal-graphs-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 5 Stage 2 causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph)
    update in data/records/tetrahedrite-concentrate.yaml (SHA-256 c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8)
    against mechanisms[0] (acidophile_associated_metal_mobilization) and its cited
    primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0).
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 2f2de84859ee4156bb09f2a0110d35edc48b8020
  state: working_tree
  inputs:
  - path: data/records/tetrahedrite-concentrate.yaml
    sha256: c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8
    role: target
  - path: history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml
    sha256: 5c3f15468c3f48432f41a905a701aadcaa1d4eae26c6f74eb343545823bdbb35
    role: context
  - path: history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
    sha256: 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:tetrahedrite-concentrate
  path: data/records/tetrahedrite-concentrate.yaml
  label: Tetrahedrite concentrate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tetrahedrite-concentrate.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
    role: canonical_history
scope:
  description: Cycle 5 Stage 2 causal-graph review of data/records/tetrahedrite-concentrate.yaml
    (SHA-256 c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8) and
    its canonical EDIT history sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml,
    history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml)
    verifying full synchronization between causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph)
    and mechanisms[0] (acidophile_associated_metal_mobilization).
  selection: Cycle 5 Stage 2 causal_graphs update for cmmmech:tetrahedrite-concentrate
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tetrahedrite-concentrate
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/tetrahedrite-concentrate.yaml
  locator: 'Working-tree record data/records/tetrahedrite-concentrate.yaml (causal_graphs[0]:
    ferrooxidans_tetrahedrite_bioleaching_graph)'
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph,
    mechanism_ref: acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml
    with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite
    concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge
    acidic_ferric_sulfate_lixiviant -> solid_feed_substrate uses predicate ''solubilizes''
    (supports: partial) and edge solid_feed_substrate -> solubilized_metal_species
    uses predicate ''produces'' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant
    -> solid_feed_substrate from acts_on to solubilizes (retaining supports: partial
    for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans
    DSM 14882 in sqr_reductase -> tth_hydrolase, and replaced template node/edge descriptions
    with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details.
    Updated causal_graphs[0].description from ''Cu, Sb, Zn, and Fe mobilization from
    mixed tetrahedrite concentrate'' to ''Cu, Zn, Ag, and sulfate mobilization (with
    transient Sb release) from mixed tetrahedrite concentrate'' to match the product
    node and edge descriptions in Kupka et al. (2025) (kupka_2025).'
  snapshot_sha256: c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.1007/s40831-025-01089-0
  locator: 'kupka_2025: Kupka D et al. (2025). Bioleaching of Tetrahedrite by Iron-
    and Sulfur-Oxidizing Bacteria. Journal of Sustainable Metallurgy 11:3685-3699.
    DOI 10.1007/s40831-025-01089-0. Complete 15-page original article, Figures 1-8,
    Tables 1-2 and seven-page supplement with Figures S1-S12. (https://doi.org/10.1007/s40831-025-01089-0)'
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Separate inoculated laboratory cultures showed greater copper mobilization
    and sulfate accumulation than the uninoculated acidic control. The two organisms
    denote separate culture arms, not a consortium. Dissolved copper and sulfate trajectories,
    oxygen consumption and altered grain surfaces support culture-associated oxidative
    leaching, while iron cycling is the authors'' mechanistic interpretation. No enzyme-specific
    or genetic cause was established. The response was element dependent: dissolved
    antimony rose early and subsequently declined, and the abiotic treatment released
    more iron and manganese than the inoculated treatments in the reported day-35
    comparison. Copper and sulfur depletion with antimony and iron enrichment in selected
    alteration rims does not demonstrate a pure secondary mineral product or complete
    dissolution of every grain. Substrate-edge evidence (kupka_2025, supports: partial):
    Kupka et al. (2025) demonstrate higher Cu mobilization, sulfate accumulation,
    and O2 consumption in inoculated flasks than in the autoclaved control over 120
    days, though unbuffered pH and ferric-iron trajectories were not matched independently
    of living cells. Product-edge evidence (kupka_2025, supports: support): Kupka
    et al. (2025) Figures 2–5 and S12 document increased dissolved Cu, sulfate, Zn,
    and Ag trajectories and transient Sb release in 0.2-um-filtered leachates relative
    to abiotic controls.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml
  locator: Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml
    (SHA-256 5c3f15468c3f48432f41a905a701aadcaa1d4eae26c6f74eb343545823bdbb35): Upgrade
    tetrahedrite-concentrate causal_graphs[0] lixiviant predicate to solubilizes and
    ground node/edge text in kupka_2025 — Upgraded acidic_ferric_sulfate_lixiviant
    -> solid_feed_substrate from acts_on to solubilizes (retaining supports: partial
    for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans
    DSM 14882 in sqr_reductase -> tth_hydrolase, and replaced template node/edge descriptions
    with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details.'
  snapshot_sha256: 5c3f15468c3f48432f41a905a701aadcaa1d4eae26c6f74eb343545823bdbb35
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
  locator: Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
    (SHA-256 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a): Align
    tetrahedrite-concentrate causal_graphs[0].description with measured Cu, Zn, Ag,
    and sulfate mobilization in kupka_2025 — Updated causal_graphs[0].description
    from ''Cu, Sb, Zn, and Fe mobilization from mixed tetrahedrite concentrate'' to
    ''Cu, Zn, Ag, and sulfate mobilization (with transient Sb release) from mixed
    tetrahedrite concentrate'' to match the product node and edge descriptions in
    Kupka et al. (2025) (kupka_2025).'
  snapshot_sha256: 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a
- evidence_id: validation
  kind: validation
  reference: data/records/tetrahedrite-concentrate.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-30T17:11:30Z'
  support: supports
  summary: data/records/tetrahedrite-concentrate.yaml and history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml,
    history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml
    pass strict LinkML schema and history validation with 0 errors.
  snapshot_sha256: c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 668 record(s); 0 failed.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: All history sidecars pass validation with 0 errors.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_mechanism_synchronization
  area: graph
  topic: Synchronization of causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph)
    with mechanisms[0] (acidophile_associated_metal_mobilization) and primary source
    kupka_2025 (DOI:10.1007/s40831-025-01089-0)
  outcome: supported
  summary: 'Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph,
    mechanism_ref: acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml
    with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite
    concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge
    acidic_ferric_sulfate_lixiviant -> solid_feed_substrate uses predicate ''solubilizes''
    (supports: partial) and edge solid_feed_substrate -> solubilized_metal_species
    uses predicate ''produces'' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant
    -> solid_feed_substrate from acts_on to solubilizes (retaining supports: partial
    for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans
    DSM 14882 in sqr_reductase -> tth_hydrolase, and replaced template node/edge descriptions
    with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details.
    Updated causal_graphs[0].description from ''Cu, Sb, Zn, and Fe mobilization from
    mixed tetrahedrite concentrate'' to ''Cu, Zn, Ag, and sulfate mobilization (with
    transient Sb release) from mixed tetrahedrite concentrate'' to match the product
    node and edge descriptions in Kupka et al. (2025) (kupka_2025).'
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: data/records/tetrahedrite-concentrate.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar(s) (history/records/tetrahedrite-concentrate/2026-10-30T171004Z-marcin-f2dc1e.yaml,
    history/records/tetrahedrite-concentrate/2026-10-30T175759Z-marcin-428fe7.yaml,
    latest SHA-256 0325fe8871cf827627bb4adfef0578c7316373cda8ccbb28e673ea634ede1c7a)
    and passing all LinkML and history validation gates.
  target_ids:
  - cmmmech:tetrahedrite-concentrate
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Tetrahedrite concentrate (cmmmech:tetrahedrite-concentrate) passes Cycle
  5 Stage 2 causal-graph review (scientific_review: true) at SHA-256 c4c0397cd9cac4045b53800457d3a45a2a18a94c41f978619fbe809e829bf8d8:
  Synchronized causal_graphs[0] (ferrooxidans_tetrahedrite_bioleaching_graph, mechanism_ref:
  acidophile_associated_metal_mobilization) in data/records/tetrahedrite-concentrate.yaml
  with mechanisms[0] (Acidophile-associated metal mobilization from mixed tetrahedrite
  concentrate) and primary source kupka_2025 (DOI:10.1007/s40831-025-01089-0): edge
  acidic_ferric_sulfate_lixiviant -> solid_feed_substrate uses predicate ''solubilizes''
  (supports: partial) and edge solid_feed_substrate -> solubilized_metal_species uses
  predicate ''produces'' (supports: support). Upgraded acidic_ferric_sulfate_lixiviant
  -> solid_feed_substrate from acts_on to solubilizes (retaining supports: partial
  for unmatched pH/iron controls), included A. ferrivorans SS3 alongside A. ferrooxidans
  DSM 14882 in sqr_reductase -> tth_hydrolase, and replaced template node/edge descriptions
  with exact kupka_2025 120-day Strieborna tetrahedrite concentrate leaching details.
  Updated causal_graphs[0].description from ''Cu, Sb, Zn, and Fe mobilization from
  mixed tetrahedrite concentrate'' to ''Cu, Zn, Ag, and sulfate mobilization (with
  transient Sb release) from mixed tetrahedrite concentrate'' to match the product
  node and edge descriptions in Kupka et al. (2025) (kupka_2025).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 5 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
