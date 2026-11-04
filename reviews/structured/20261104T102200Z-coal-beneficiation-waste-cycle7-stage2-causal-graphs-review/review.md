# Cycle 7 Stage 2 causal-graphs review of Coal beneficiation waste (cmmmech:coal-beneficiation-waste)

- Review: 20261104T102200Z-coal-beneficiation-waste-cycle7-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T10:15:00Z
- Finished UTC: 2026-11-04T10:22:00Z
- Reviewer: antigravity / cmmmech-cycle7-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Coal beneficiation waste (cmmmech:coal-beneficiation-waste) passes Cycle 7 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe: Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) with causal_graph 'three_stage_experimental_dump_leaching_graph' (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) blayda2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 7 Stage 2 causal-graphs review of data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) and its canonical EDIT history sidecar(s) (history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'three_stage_experimental_dump_leaching_graph' (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]).

Selection: Cycle 7 Stage 2 causal_graphs curation for cmmmech:coal-beneficiation-waste
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fa7431aece56c8a1d2344a7812db30b2a78f8022.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:coal-beneficiation-waste | data/records/coal-beneficiation-waste.yaml | maintained | Coal beneficiation waste |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:coal-beneficiation-waste | Checked 678 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:coal-beneficiation-waste | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'three_stage_experimental_dump_leaching_graph' (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:coal-beneficiation-waste.

Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) with causal_graph 'three_stage_experimental_dump_leaching_graph' (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) blayda2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:coal-beneficiation-waste.

data/records/coal-beneficiation-waste.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml (SHA-256 ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d): Add three_stage_experimental_dump_leaching_graph causal graph and ground three_stage_experimental_dump_leaching to Acidithiobacillus ferrooxidans reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 Sqr/Tth protein_examples (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) and three_stage_experimental_dump_leaching_graph causal graph to coal-beneficiation-waste.yaml.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/coal-beneficiation-waste.yaml; Working-tree record data/records/coal-beneficiation-waste.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) with causal_graph 'three_stage_experimental_dump_leaching_graph' (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) blayda2018. |
| primary_source | DOI:10.31643/2018/6445.27; blayda2018: Blayda, Vasyleva, Slyusarenko, Barba and Vodzinskii (2018). Technological Parameters of Coal Mine Dumps Bioleaching for the Rare Metals Extraction. Kompleksnoe Ispolzovanie Mineralnogo Syra 307(4):28-37. DOI 10.31643/2018/6445.27; complete official ten-page original, Methods p29, Figures 1-5 and Tables 1-2; accepted 1 October 2018. (https://doi.org/10.31643/2018/6445.27) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8 (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2, Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2, Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (blayda2018: Blayda, Vasyleva, Slyusarenko, Barba and Vodzinskii (2018). Technological Parameters of Coal Mine Dumps Bioleaching for the Rare Metals Extraction. Kompleksnoe Ispolzovanie Mineralnogo Syra 307(4):28-37. DOI 10.31643/2018/6445.27; complete official ten-page original, Methods p29, Figures 1-5 and Tables 1-2; accepted 1 October 2018. (https://doi.org/10.31643/2018/6445.27)) report culture-level sulfur oxidation and leaching without single-gene sqr/tth knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml; Canonical EDIT history sidecar history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml | supports | Canonical EDIT history sidecar history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml (SHA-256 ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d): Add three_stage_experimental_dump_leaching_graph causal graph and ground three_stage_experimental_dump_leaching to Acidithiobacillus ferrooxidans reference-proteome UniProtKB Sqr/Tth paralogs (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 Sqr/Tth protein_examples (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) and three_stage_experimental_dump_leaching_graph causal graph to coal-beneficiation-waste.yaml. |
| validation | data/records/coal-beneficiation-waste.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/coal-beneficiation-waste.yaml and history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 7 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T102200Z-coal-beneficiation-waste-cycle7-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 7 Stage 2 causal-graphs review of Coal beneficiation waste (cmmmech:coal-beneficiation-waste)
started_at: '2026-11-04T10:15:00Z'
finished_at: '2026-11-04T10:22:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle7-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 7 Stage 2 causal_graphs and ProteinExample curation in data/records/coal-beneficiation-waste.yaml
    (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) against
    UniProtKB reference proteomes and cited primary source(s) blayda2018.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: fa7431aece56c8a1d2344a7812db30b2a78f8022
  state: working_tree
  inputs:
  - path: data/records/coal-beneficiation-waste.yaml
    sha256: 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe
    role: target
  - path: history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
    sha256: ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:coal-beneficiation-waste
  path: data/records/coal-beneficiation-waste.yaml
  label: Coal beneficiation waste
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coal-beneficiation-waste.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
    role: canonical_history
scope:
  description: 'Cycle 7 Stage 2 causal-graphs review of data/records/coal-beneficiation-waste.yaml
    (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe) and
    its canonical EDIT history sidecar(s) (history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''three_stage_experimental_dump_leaching_graph''
    (mechanism_ref: three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase:
    [UniProtKB:B7JBP8 (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr,
    B7J411_ACIF2, UP000001362)]; tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2,
    UP000001362)]).'
  selection: Cycle 7 Stage 2 causal_graphs curation for cmmmech:coal-beneficiation-waste
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:coal-beneficiation-waste
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/coal-beneficiation-waste.yaml
  locator: Working-tree record data/records/coal-beneficiation-waste.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe)
    with causal_graph ''three_stage_experimental_dump_leaching_graph'' (mechanism_ref:
    three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
    (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
    tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    blayda2018.'
  snapshot_sha256: 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.31643/2018/6445.27
  locator: 'blayda2018: Blayda, Vasyleva, Slyusarenko, Barba and Vodzinskii (2018).
    Technological Parameters of Coal Mine Dumps Bioleaching for the Rare Metals Extraction.
    Kompleksnoe Ispolzovanie Mineralnogo Syra 307(4):28-37. DOI 10.31643/2018/6445.27;
    complete official ten-page original, Methods p29, Figures 1-5 and Tables 1-2;
    accepted 1 October 2018. (https://doi.org/10.31643/2018/6445.27)'
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
    (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
    Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2,
    Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (blayda2018:
    Blayda, Vasyleva, Slyusarenko, Barba and Vodzinskii (2018). Technological Parameters
    of Coal Mine Dumps Bioleaching for the Rare Metals Extraction. Kompleksnoe Ispolzovanie
    Mineralnogo Syra 307(4):28-37. DOI 10.31643/2018/6445.27; complete official ten-page
    original, Methods p29, Figures 1-5 and Tables 1-2; accepted 1 October 2018. (https://doi.org/10.31643/2018/6445.27))
    report culture-level sulfur oxidation and leaching without single-gene sqr/tth
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
  locator: Canonical EDIT history sidecar history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
    (SHA-256 ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d): Add
    three_stage_experimental_dump_leaching_graph causal graph and ground three_stage_experimental_dump_leaching
    to Acidithiobacillus ferrooxidans reference-proteome UniProtKB Sqr/Tth paralogs
    (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) — Added representative
    Acidithiobacillus ferrooxidans ATCC 23270 Sqr/Tth protein_examples (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9) and three_stage_experimental_dump_leaching_graph
    causal graph to coal-beneficiation-waste.yaml.'
  snapshot_sha256: ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d
- evidence_id: validation
  kind: validation
  reference: data/records/coal-beneficiation-waste.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T10:21:00Z'
  support: supports
  summary: data/records/coal-beneficiation-waste.yaml and history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 678 record(s); 0 failed.
  target_ids:
  - cmmmech:coal-beneficiation-waste
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
  - cmmmech:coal-beneficiation-waste
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''three_stage_experimental_dump_leaching_graph'' (mechanism_ref:
    three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
    (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
    tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe)
    with causal_graph ''three_stage_experimental_dump_leaching_graph'' (mechanism_ref:
    three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
    (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
    tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
    parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    blayda2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
    (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
    Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2,
    Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/coal-beneficiation-waste.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar(s) (history/records/coal-beneficiation-waste/2026-11-04T102016Z-marcin-44b213.yaml
    (SHA-256 ff4877730b32517189921a3174a95b9879ef93a5b00959131edbff5d703b0c2d): Add
    three_stage_experimental_dump_leaching_graph causal graph and ground three_stage_experimental_dump_leaching
    to Acidithiobacillus ferrooxidans reference-proteome UniProtKB Sqr/Tth paralogs
    (UniProtKB:B7JBP8, UniProtKB:B7J411, UniProtKB:B7J3C9) — Added representative
    Acidithiobacillus ferrooxidans ATCC 23270 Sqr/Tth protein_examples (UniProtKB:B7JBP8,
    UniProtKB:B7J411, UniProtKB:B7J3C9) and three_stage_experimental_dump_leaching_graph
    causal graph to coal-beneficiation-waste.yaml.) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:coal-beneficiation-waste
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Coal beneficiation waste (cmmmech:coal-beneficiation-waste) passes Cycle
  7 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe:
  Curated data/records/coal-beneficiation-waste.yaml (SHA-256 626e0b40d86710eed177a374b98a3ce384e57358e93075c7462d6fb6f54d59fe)
  with causal_graph ''three_stage_experimental_dump_leaching_graph'' (mechanism_ref:
  three_stage_experimental_dump_leaching, 5 nodes / 4 edges; sqr_reductase: [UniProtKB:B7JBP8
  (AFE_1792, SQRD_ACIF2, UP000001362), UniProtKB:B7J411 (sqr, B7J411_ACIF2, UP000001362)];
  tth_hydrolase: [UniProtKB:B7J3C9 (tth, TTH_ACIF2, UP000001362)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  blayda2018. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JBP8
  (SQRD_ACIF2, Sulfide-quinone reductase, gene_symbol: AFE_1792, SWISS_PROT, NCBITaxon:243159
  Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J411 (B7J411_ACIF2,
  Sulfide quinone reductase, putative, gene_symbol: sqr, TREMBL, NCBITaxon:243159
  Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7J3C9 (TTH_ACIF2,
  Tetrathionate hydrolase, gene_symbol: tth, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 7 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
