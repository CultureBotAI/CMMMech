# Cycle 7 Stage 2 causal-graphs review of Chalcopyrite (cmmmech:chalcopyrite)

- Review: 20261104T102200Z-chalcopyrite-cycle7-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T10:15:00Z
- Finished UTC: 2026-11-04T10:22:00Z
- Reviewer: antigravity / cmmmech-cycle7-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chalcopyrite (cmmmech:chalcopyrite) passes Cycle 7 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043: Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) with causal_graph 'acidophile_concentrate_bioleaching_graph' (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) christel_2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone reductase, gene_symbol: Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum YSK, UP000027059); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).

## Scope And Provenance

Cycle 7 Stage 2 causal-graphs review of data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) and its canonical EDIT history sidecar(s) (history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'acidophile_concentrate_bioleaching_graph' (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]).

Selection: Cycle 7 Stage 2 causal_graphs curation for cmmmech:chalcopyrite
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fa7431aece56c8a1d2344a7812db30b2a78f8022.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chalcopyrite | data/records/chalcopyrite.yaml | maintained | Chalcopyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:chalcopyrite | Checked 678 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:chalcopyrite | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'acidophile_concentrate_bioleaching_graph' (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)])

graph: supported. Targets: cmmmech:chalcopyrite.

Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) with causal_graph 'acidophile_concentrate_bioleaching_graph' (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) christel_2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone reductase, gene_symbol: Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum YSK, UP000027059); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:chalcopyrite.

data/records/chalcopyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml (SHA-256 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc): Add acidophile_concentrate_bioleaching_graph causal graph and ground acidophile_concentrate_bioleaching to Acidithiobacillus caldus and Leptospirillum ferriphilum reference-proteome UniProtKB Sqr/TetH homologs (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:A0A059XTE6, UniProtKB:F9ZNI0) — Added representative Acidithiobacillus caldus SM-1 (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:F9ZNI0) and Leptospirillum ferriphilum YSK (UniProtKB:A0A059XTE6) protein_examples and acidophile_concentrate_bioleaching_graph causal graph to chalcopyrite.yaml.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/chalcopyrite.yaml; Working-tree record data/records/chalcopyrite.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) with causal_graph 'acidophile_concentrate_bioleaching_graph' (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) christel_2018. |
| primary_source | DOI:10.3389/fmicb.2018.03059; christel_2018: Christel et al. (2018). Weak Iron Oxidation by Sulfobacillus thermosulfidooxidans Maintains a Favorable Redox Potential for Chalcopyrite Bioleaching. Frontiers in Microbiology 9:3059. DOI 10.3389/fmicb.2018.03059. Mineral and Bioleaching Experiments Methods; Bioleaching of Chalcopyrite Concentrate results; Figures 1-2. (https://doi.org/10.3389/fmicb.2018.03059) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone reductase, gene_symbol: Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum YSK, UP000027059); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135). Primary mechanism source(s) (christel_2018: Christel et al. (2018). Weak Iron Oxidation by Sulfobacillus thermosulfidooxidans Maintains a Favorable Redox Potential for Chalcopyrite Bioleaching. Frontiers in Microbiology 9:3059. DOI 10.3389/fmicb.2018.03059. Mineral and Bioleaching Experiments Methods; Bioleaching of Chalcopyrite Concentrate results; Figures 1-2. (https://doi.org/10.3389/fmicb.2018.03059)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml; Canonical EDIT history sidecar history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml | supports | Canonical EDIT history sidecar history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml (SHA-256 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc): Add acidophile_concentrate_bioleaching_graph causal graph and ground acidophile_concentrate_bioleaching to Acidithiobacillus caldus and Leptospirillum ferriphilum reference-proteome UniProtKB Sqr/TetH homologs (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:A0A059XTE6, UniProtKB:F9ZNI0) — Added representative Acidithiobacillus caldus SM-1 (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:F9ZNI0) and Leptospirillum ferriphilum YSK (UniProtKB:A0A059XTE6) protein_examples and acidophile_concentrate_bioleaching_graph causal graph to chalcopyrite.yaml. |
| validation | data/records/chalcopyrite.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/chalcopyrite.yaml and history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 7 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T102200Z-chalcopyrite-cycle7-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 7 Stage 2 causal-graphs review of Chalcopyrite (cmmmech:chalcopyrite)
started_at: '2026-11-04T10:15:00Z'
finished_at: '2026-11-04T10:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle7-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 7 Stage 2 causal_graphs and ProteinExample curation in data/records/chalcopyrite.yaml
    (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) against
    UniProtKB reference proteomes and cited primary source(s) christel_2018.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: fa7431aece56c8a1d2344a7812db30b2a78f8022
  state: working_tree
  inputs:
  - path: data/records/chalcopyrite.yaml
    sha256: c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043
    role: target
  - path: history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
    sha256: 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:chalcopyrite
  path: data/records/chalcopyrite.yaml
  label: Chalcopyrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcopyrite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
    role: canonical_history
scope:
  description: 'Cycle 7 Stage 2 causal-graphs review of data/records/chalcopyrite.yaml
    (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043) and
    its canonical EDIT history sidecar(s) (history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''acidophile_concentrate_bioleaching_graph''
    (mechanism_ref: acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437,
    F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT,
    UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]).'
  selection: Cycle 7 Stage 2 causal_graphs curation for cmmmech:chalcopyrite
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chalcopyrite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/chalcopyrite.yaml
  locator: Working-tree record data/records/chalcopyrite.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043)
    with causal_graph ''acidophile_concentrate_bioleaching_graph'' (mechanism_ref:
    acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6
    (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS,
    UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)];
    tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    christel_2018.'
  snapshot_sha256: c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.3389/fmicb.2018.03059
  locator: 'christel_2018: Christel et al. (2018). Weak Iron Oxidation by Sulfobacillus
    thermosulfidooxidans Maintains a Favorable Redox Potential for Chalcopyrite Bioleaching.
    Frontiers in Microbiology 9:3059. DOI 10.3389/fmicb.2018.03059. Mineral and Bioleaching
    Experiments Methods; Bioleaching of Chalcopyrite Concentrate results; Figures
    1-2. (https://doi.org/10.3389/fmicb.2018.03059)'
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:F9ZQD6
    (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288
    Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone
    reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus
    caldus SM-1, UP000006135); UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone
    reductase, gene_symbol: Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum
    YSK, UP000027059); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH,
    gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135). Primary mechanism source(s) (christel_2018: Christel et al. (2018).
    Weak Iron Oxidation by Sulfobacillus thermosulfidooxidans Maintains a Favorable
    Redox Potential for Chalcopyrite Bioleaching. Frontiers in Microbiology 9:3059.
    DOI 10.3389/fmicb.2018.03059. Mineral and Bioleaching Experiments Methods; Bioleaching
    of Chalcopyrite Concentrate results; Figures 1-2. (https://doi.org/10.3389/fmicb.2018.03059))
    report culture-level sulfur oxidation and leaching without single-gene sqr/tth
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
  locator: Canonical EDIT history sidecar history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
    (SHA-256 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc): Add
    acidophile_concentrate_bioleaching_graph causal graph and ground acidophile_concentrate_bioleaching
    to Acidithiobacillus caldus and Leptospirillum ferriphilum reference-proteome
    UniProtKB Sqr/TetH homologs (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:A0A059XTE6,
    UniProtKB:F9ZNI0) — Added representative Acidithiobacillus caldus SM-1 (UniProtKB:F9ZQD6,
    UniProtKB:F9ZN43, UniProtKB:F9ZNI0) and Leptospirillum ferriphilum YSK (UniProtKB:A0A059XTE6)
    protein_examples and acidophile_concentrate_bioleaching_graph causal graph to
    chalcopyrite.yaml.'
  snapshot_sha256: 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc
- evidence_id: validation
  kind: validation
  reference: data/records/chalcopyrite.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: data/records/chalcopyrite.yaml and history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 678 record(s); 0 failed.
  target_ids:
  - cmmmech:chalcopyrite
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
  - cmmmech:chalcopyrite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''acidophile_concentrate_bioleaching_graph'' (mechanism_ref:
    acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6
    (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS,
    UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)];
    tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)])'
  outcome: supported
  summary: 'Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043)
    with causal_graph ''acidophile_concentrate_bioleaching_graph'' (mechanism_ref:
    acidophile_concentrate_bioleaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6
    (Atc_1705, F9ZQD6_ACICS, UP000006135), UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS,
    UP000006135), UniProtKB:A0A059XTE6 (Y981_02650, A0A059XTE6_9BACT, UP000027059)];
    tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS, UP000006135)]), achieving
    100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    christel_2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:F9ZQD6
    (F9ZQD6_ACICS, Sulfide-quinone reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288
    Acidithiobacillus caldus SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone
    reductase, putative, gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus
    caldus SM-1, UP000006135); UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone
    reductase, gene_symbol: Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum
    YSK, UP000027059); UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH,
    gene_symbol: Atc_1595, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1,
    UP000006135).'
  target_ids:
  - cmmmech:chalcopyrite
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/chalcopyrite.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/chalcopyrite/2026-11-04T101915Z-marcin-d99b4b.yaml
    (SHA-256 10dfaac974b932f5f83377f908c569647c2cfbb842cabf2c43edd73b7bc27ddc): Add
    acidophile_concentrate_bioleaching_graph causal graph and ground acidophile_concentrate_bioleaching
    to Acidithiobacillus caldus and Leptospirillum ferriphilum reference-proteome
    UniProtKB Sqr/TetH homologs (UniProtKB:F9ZQD6, UniProtKB:F9ZN43, UniProtKB:A0A059XTE6,
    UniProtKB:F9ZNI0) — Added representative Acidithiobacillus caldus SM-1 (UniProtKB:F9ZQD6,
    UniProtKB:F9ZN43, UniProtKB:F9ZNI0) and Leptospirillum ferriphilum YSK (UniProtKB:A0A059XTE6)
    protein_examples and acidophile_concentrate_bioleaching_graph causal graph to
    chalcopyrite.yaml.) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:chalcopyrite
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Chalcopyrite (cmmmech:chalcopyrite) passes Cycle 7 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043:
  Curated data/records/chalcopyrite.yaml (SHA-256 c02f09ceec8439d628f7105d7ebd1ca46393c609b3e88eff8bb770164943b043)
  with causal_graph ''acidophile_concentrate_bioleaching_graph'' (mechanism_ref: acidophile_concentrate_bioleaching,
  5 nodes / 4 edges; sqr_reductase: [UniProtKB:F9ZQD6 (Atc_1705, F9ZQD6_ACICS, UP000006135),
  UniProtKB:F9ZN43 (Atc_1437, F9ZN43_ACICS, UP000006135), UniProtKB:A0A059XTE6 (Y981_02650,
  A0A059XTE6_9BACT, UP000027059)]; tth_hydrolase: [UniProtKB:F9ZNI0 (Atc_1595, F9ZNI0_ACICS,
  UP000006135)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and caveats from primary source(s) christel_2018. Live-verified UniProtKB
  reference-proteome grounding across UniProtKB:F9ZQD6 (F9ZQD6_ACICS, Sulfide-quinone
  reductase, gene_symbol: Atc_1705, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus
  SM-1, UP000006135); UniProtKB:F9ZN43 (F9ZN43_ACICS, Sulfide-quinone reductase, putative,
  gene_symbol: Atc_1437, TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135);
  UniProtKB:A0A059XTE6 (A0A059XTE6_9BACT, Sulfide-quinone reductase, gene_symbol:
  Y981_02650, TREMBL, NCBITaxon:1441628 Leptospirillum ferriphilum YSK, UP000027059);
  UniProtKB:F9ZNI0 (F9ZNI0_ACICS, Tetrathionate hydrolase TetH, gene_symbol: Atc_1595,
  TREMBL, NCBITaxon:990288 Acidithiobacillus caldus SM-1, UP000006135).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 7 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
