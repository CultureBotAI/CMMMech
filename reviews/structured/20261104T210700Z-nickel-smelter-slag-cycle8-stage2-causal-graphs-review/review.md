# Cycle 8 Stage 2 causal-graphs review of Nickel smelter slag (cmmmech:nickel-smelter-slag)

- Review: 20261104T210700Z-nickel-smelter-slag-cycle8-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T21:05:00Z
- Finished UTC: 2026-11-04T21:07:00Z
- Reviewer: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Nickel smelter slag (cmmmech:nickel-smelter-slag) passes Cycle 8 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591: Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) with causal_graph 'lr_associated_leaching_with_nickel_null_graph' (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) munoz_blandon2010. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 8 Stage 2 causal-graphs review of data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) and its canonical EDIT history sidecar(s) (history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'lr_associated_leaching_with_nickel_null_graph' (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:nickel-smelter-slag
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4d0c73a2a05c271df0b845f389dfa216535a05b5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:nickel-smelter-slag | data/records/nickel-smelter-slag.yaml | maintained | Nickel smelter slag |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:nickel-smelter-slag | Checked 683 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:nickel-smelter-slag | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'lr_associated_leaching_with_nickel_null_graph' (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:nickel-smelter-slag.

Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) with causal_graph 'lr_associated_leaching_with_nickel_null_graph' (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) munoz_blandon2010. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:nickel-smelter-slag.

data/records/nickel-smelter-slag.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml (SHA-256 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929): Add lr_associated_leaching_with_nickel_null_graph causal graph and ground lr_associated_leaching_with_nickel_null to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and lr_associated_leaching_with_nickel_null_graph causal graph to nickel-smelter-slag.yaml.) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/nickel-smelter-slag.yaml; Working-tree record data/records/nickel-smelter-slag.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) with causal_graph 'lr_associated_leaching_with_nickel_null_graph' (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) munoz_blandon2010. |
| primary_source | https://hdl.handle.net/11449/100745; munoz_blandon2010: Nury Alexandra Munoz Blandon (2010). Recuperacao de niquel e outros metais a partir de diferentes fontes (rejeitos minerais de processo industrial e pentlandita (Ni,Fe)9S8) por lixiviacao bacteriana e acida. Doctoral thesis, UNESP, Instituto de Quimica, Araraquara. Official repository handle 11449/100745, issued 15 July 2010; repository accession in 2014 is not the experiment's publication year. Original 125-page PDF; source pp. 33, 36-39 and 50-58, Tables 1-2 and 7-9, Figures 4-9. Repository title wording differs slightly from the thesis front matter. (https://hdl.handle.net/11449/100745) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (munoz_blandon2010: Nury Alexandra Munoz Blandon (2010). Recuperacao de niquel e outros metais a partir de diferentes fontes (rejeitos minerais de processo industrial e pentlandita (Ni,Fe)9S8) por lixiviacao bacteriana e acida. Doctoral thesis, UNESP, Instituto de Quimica, Araraquara. Official repository handle 11449/100745, issued 15 July 2010; repository accession in 2014 is not the experiment's publication year. Original 125-page PDF; source pp. 33, 36-39 and 50-58, Tables 1-2 and 7-9, Figures 4-9. Repository title wording differs slightly from the thesis front matter. (https://hdl.handle.net/11449/100745)) report culture-level iron/sulfur oxidation and mineral transformation/leaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml; Canonical EDIT history sidecar history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml | supports | Canonical EDIT history sidecar history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml (SHA-256 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929): Add lr_associated_leaching_with_nickel_null_graph causal graph and ground lr_associated_leaching_with_nickel_null to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and lr_associated_leaching_with_nickel_null_graph causal graph to nickel-smelter-slag.yaml. |
| validation | data/records/nickel-smelter-slag.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/nickel-smelter-slag.yaml and history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 8 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T210700Z-nickel-smelter-slag-cycle8-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 8 Stage 2 causal-graphs review of Nickel smelter slag (cmmmech:nickel-smelter-slag)
started_at: '2026-11-04T21:05:00Z'
finished_at: '2026-11-04T21:07:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 8 Stage 2 causal_graphs and ProteinExample curation in data/records/nickel-smelter-slag.yaml
    (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) against
    UniProtKB reference proteomes and cited primary source(s) munoz_blandon2010.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 4d0c73a2a05c271df0b845f389dfa216535a05b5
  state: working_tree
  inputs:
  - path: data/records/nickel-smelter-slag.yaml
    sha256: be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591
    role: target
  - path: history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
    sha256: 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:nickel-smelter-slag
  path: data/records/nickel-smelter-slag.yaml
  label: Nickel smelter slag
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-smelter-slag.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
    role: canonical_history
scope:
  description: 'Cycle 8 Stage 2 causal-graphs review of data/records/nickel-smelter-slag.yaml
    (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591) and
    its canonical EDIT history sidecar(s) (history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml)
    verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding,
    and primary-source evidence fidelity across causal_graph ''lr_associated_leaching_with_nickel_null_graph''
    (mechanism_ref: lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)]).'
  selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:nickel-smelter-slag
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:nickel-smelter-slag
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/nickel-smelter-slag.yaml
  locator: Working-tree record data/records/nickel-smelter-slag.yaml (causal_graphs
    and mechanisms[].protein_examples)
  accessed_at: '2026-11-04T21:06:30Z'
  support: supports
  summary: 'Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591)
    with causal_graph ''lr_associated_leaching_with_nickel_null_graph'' (mechanism_ref:
    lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) munoz_blandon2010.'
  snapshot_sha256: be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591
- evidence_id: primary_source
  kind: primary_source
  reference: https://hdl.handle.net/11449/100745
  locator: 'munoz_blandon2010: Nury Alexandra Munoz Blandon (2010). Recuperacao de
    niquel e outros metais a partir de diferentes fontes (rejeitos minerais de processo
    industrial e pentlandita (Ni,Fe)9S8) por lixiviacao bacteriana e acida. Doctoral
    thesis, UNESP, Instituto de Quimica, Araraquara. Official repository handle 11449/100745,
    issued 15 July 2010; repository accession in 2014 is not the experiment''s publication
    year. Original 125-page PDF; source pp. 33, 36-39 and 50-58, Tables 1-2 and 7-9,
    Figures 4-9. Repository title wording differs slightly from the thesis front matter.
    (https://hdl.handle.net/11449/100745)'
  accessed_at: '2026-11-04T21:06:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
    gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
    cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).
    Primary mechanism source(s) (munoz_blandon2010: Nury Alexandra Munoz Blandon (2010).
    Recuperacao de niquel e outros metais a partir de diferentes fontes (rejeitos
    minerais de processo industrial e pentlandita (Ni,Fe)9S8) por lixiviacao bacteriana
    e acida. Doctoral thesis, UNESP, Instituto de Quimica, Araraquara. Official repository
    handle 11449/100745, issued 15 July 2010; repository accession in 2014 is not
    the experiment''s publication year. Original 125-page PDF; source pp. 33, 36-39
    and 50-58, Tables 1-2 and 7-9, Figures 4-9. Repository title wording differs slightly
    from the thesis front matter. (https://hdl.handle.net/11449/100745)) report culture-level
    iron/sulfur oxidation and mineral transformation/leaching without single-gene
    knockouts; supports: partial is strictly preserved on all enzyme-level edges and
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
  locator: Canonical EDIT history sidecar history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
  accessed_at: '2026-11-04T21:06:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
    (SHA-256 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929): Add
    lr_associated_leaching_with_nickel_null_graph causal graph and ground lr_associated_leaching_with_nickel_null
    to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans
    ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0
    rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and lr_associated_leaching_with_nickel_null_graph
    causal graph to nickel-smelter-slag.yaml.'
  snapshot_sha256: 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929
- evidence_id: validation
  kind: validation
  reference: data/records/nickel-smelter-slag.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T21:06:30Z'
  support: supports
  summary: data/records/nickel-smelter-slag.yaml and history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 683 record(s); 0 failed.
  target_ids:
  - cmmmech:nickel-smelter-slag
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
  - cmmmech:nickel-smelter-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''lr_associated_leaching_with_nickel_null_graph'' (mechanism_ref:
    lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591)
    with causal_graph ''lr_associated_leaching_with_nickel_null_graph'' (mechanism_ref:
    lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) munoz_blandon2010. Live-verified UniProtKB
    reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome
    c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol:
    rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
    UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
    Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/nickel-smelter-slag.yaml was updated exclusively through
    scripts/curate_causal_graphs.py (curate_record_file), producing append-only history
    sidecar(s) (history/records/nickel-smelter-slag/2026-11-04T210559Z-marcin-bd6580.yaml
    (SHA-256 369144514c8967e74cd7406759a42c7162c1b22b49e2f340a1991bcf07a52929): Add
    lr_associated_leaching_with_nickel_null_graph causal graph and ground lr_associated_leaching_with_nickel_null
    to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans
    ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0
    rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and lr_associated_leaching_with_nickel_null_graph
    causal graph to nickel-smelter-slag.yaml.) and passing all LinkML and history
    validation gates.'
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Nickel smelter slag (cmmmech:nickel-smelter-slag) passes Cycle 8 Stage 2
  causal-graphs review (scientific_review: true) at SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591:
  Curated data/records/nickel-smelter-slag.yaml (SHA-256 be88b5c74e61ae005c48fbac8f2417fb274c605c7b256d6645505e537713a591)
  with causal_graph ''lr_associated_leaching_with_nickel_null_graph'' (mechanism_ref:
  lr_associated_leaching_with_nickel_null, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
  [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
  [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
  UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and
  causal_graphs[].nodes[].protein_examples and preserving source-faithful support
  levels and caveats from primary source(s) munoz_blandon2010. Live-verified UniProtKB
  reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c,
  gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
  23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus,
  SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362);
  UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159
  Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 8 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py.
related_reviews: []
```
