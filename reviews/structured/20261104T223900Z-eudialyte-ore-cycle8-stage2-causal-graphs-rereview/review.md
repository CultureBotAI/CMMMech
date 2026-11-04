# Cycle 8 Stage 2 causal-graphs re-review of Eudialyte ore (cmmmech:eudialyte-ore) after Issue #925 fixes

- Review: 20261104T223900Z-eudialyte-ore-cycle8-stage2-causal-graphs-rereview
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-04T22:38:00Z
- Finished UTC: 2026-11-04T22:39:00Z
- Reviewer: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Eudialyte ore (cmmmech:eudialyte-ore) passes Cycle 8 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569: Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) with causal_graph 'culture_assisted_acid_leaching_graph' (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hunter2020. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

## Scope And Provenance

Cycle 8 Stage 2 causal-graphs review of data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) and its canonical EDIT history sidecar(s) (history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml, history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml) verifying causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source evidence fidelity across causal_graph 'culture_assisted_acid_leaching_graph' (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]).

Selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:eudialyte-ore
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e299e1aca151b2192b36a718acf832b137818789.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:eudialyte-ore | data/records/eudialyte-ore.yaml | maintained | Eudialyte ore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:eudialyte-ore | Checked 683 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:eudialyte-ore | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB paralog grounding, and parity across causal_graph 'culture_assisted_acid_leaching_graph' (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)])

graph: supported. Targets: cmmmech:eudialyte-ore.

Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) with causal_graph 'culture_assisted_acid_leaching_graph' (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hunter2020. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:eudialyte-ore.

data/records/eudialyte-ore.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml (SHA-256 b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9): Add culture_assisted_acid_leaching_graph causal graph and ground culture_assisted_acid_leaching to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and culture_assisted_acid_leaching_graph causal graph to eudialyte-ore.yaml.; history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml (SHA-256 df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805): Align culture_assisted_acid_leaching_graph and protein_examples annotations with Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1-4.5.4.1 in Hunter (2020) (Issue #925) — Updated culture_assisted_acid_leaching_graph and protein_examples in eudialyte-ore.yaml to cite Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1, 4.5.3.1, and 4.5.3.4-4.5.4.1 of Hunter (2020) and match the ~3-week room-temperature (~25 C) triplicate 125 mL flask conditions and absence of silica gelation at 0.50-1.00 g ore loading (Issue #925).) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/eudialyte-ore.yaml; Working-tree record data/records/eudialyte-ore.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) with causal_graph 'culture_assisted_acid_leaching_graph' (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) hunter2020. |
| primary_source | DOI:10.7488/era/834; hunter2020: Hunter, Jamie Patrick (2020). Investigating the recovery of rare earth elements by ionic liquids and bacteria. PhD thesis, University of Edinburgh. DOI 10.7488/era/834. Chapter 4, printed pp.119-138; relevant general methods pp.158-167. Complete 217-page repository PDF acquired; this is primary thesis evidence, not a journal article. (https://doi.org/10.7488/era/834) | supports | Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7 (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin, gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol: cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362). Primary mechanism source(s) (hunter2020: Hunter, Jamie Patrick (2020). Investigating the recovery of rare earth elements by ionic liquids and bacteria. PhD thesis, University of Edinburgh. DOI 10.7488/era/834. Chapter 4, printed pp.119-138; relevant general methods pp.158-167. Complete 217-page repository PDF acquired; this is primary thesis evidence, not a journal article. (https://doi.org/10.7488/era/834)) report culture-level iron/sulfur oxidation and mineral transformation/leaching without single-gene knockouts; supports: partial is strictly preserved on all enzyme-level edges and ProteinExample evidence items. |
| edit_history | history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml; Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml | supports | Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml (SHA-256 b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9): Add culture_assisted_acid_leaching_graph causal graph and ground culture_assisted_acid_leaching to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7, UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0 rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and culture_assisted_acid_leaching_graph causal graph to eudialyte-ore.yaml. |
| edit_history_2 | history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml; Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml | supports | Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml (SHA-256 df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805): Align culture_assisted_acid_leaching_graph and protein_examples annotations with Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1-4.5.4.1 in Hunter (2020) (Issue #925) — Updated culture_assisted_acid_leaching_graph and protein_examples in eudialyte-ore.yaml to cite Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1, 4.5.3.1, and 4.5.3.4-4.5.4.1 of Hunter (2020) and match the ~3-week room-temperature (~25 C) triplicate 125 mL flask conditions and absence of silica gelation at 0.50-1.00 g ore loading (Issue #925). |
| validation | data/records/eudialyte-ore.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/eudialyte-ore.yaml and history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml, history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 8 Stage 2 (causal_graphs) after addressing Issue #925 internal-consistency findings using scripts/curate_causal_graphs.py; supersedes initial review 20261104T210700Z-eudialyte-ore-cycle8-stage2-causal-graphs-review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T223900Z-eudialyte-ore-cycle8-stage2-causal-graphs-rereview
kind: record
repository: CultureBotAI/CMMMech
title: 'Cycle 8 Stage 2 causal-graphs re-review of Eudialyte ore (cmmmech:eudialyte-ore)
  after Issue #925 fixes'
started_at: '2026-11-04T22:38:00Z'
finished_at: '2026-11-04T22:39:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle8-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 8 Stage 2 causal_graphs and ProteinExample curation in data/records/eudialyte-ore.yaml
    (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) against
    UniProtKB reference proteomes and cited primary source(s) hunter2020.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: e299e1aca151b2192b36a718acf832b137818789
  state: working_tree
  inputs:
  - path: data/records/eudialyte-ore.yaml
    sha256: bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569
    role: target
  - path: history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
    sha256: b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9
    role: context
  - path: history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
    sha256: df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:eudialyte-ore
  path: data/records/eudialyte-ore.yaml
  label: Eudialyte ore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eudialyte-ore.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
    role: canonical_history
  - repository: CultureBotAI/CMMMech
    path: history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
    role: canonical_history
scope:
  description: 'Cycle 8 Stage 2 causal-graphs review of data/records/eudialyte-ore.yaml
    (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569) and
    its canonical EDIT history sidecar(s) (history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml,
    history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml) verifying
    causal-graph node/edge topology, UniProtKB reference-proteome grounding, and primary-source
    evidence fidelity across causal_graph ''culture_assisted_acid_leaching_graph''
    (mechanism_ref: culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)]).'
  selection: Cycle 8 Stage 2 causal_graphs curation for cmmmech:eudialyte-ore
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:eudialyte-ore
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/eudialyte-ore.yaml
  locator: Working-tree record data/records/eudialyte-ore.yaml (causal_graphs and
    mechanisms[].protein_examples)
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569)
    with causal_graph ''culture_assisted_acid_leaching_graph'' (mechanism_ref: culture_assisted_acid_leaching,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    hunter2020.'
  snapshot_sha256: bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569
- evidence_id: primary_source
  kind: primary_source
  reference: DOI:10.7488/era/834
  locator: 'hunter2020: Hunter, Jamie Patrick (2020). Investigating the recovery of
    rare earth elements by ionic liquids and bacteria. PhD thesis, University of Edinburgh.
    DOI 10.7488/era/834. Chapter 4, printed pp.119-138; relevant general methods pp.158-167.
    Complete 217-page repository PDF acquired; this is primary thesis evidence, not
    a journal article. (https://doi.org/10.7488/era/834)'
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
    gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
    cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).
    Primary mechanism source(s) (hunter2020: Hunter, Jamie Patrick (2020). Investigating
    the recovery of rare earth elements by ionic liquids and bacteria. PhD thesis,
    University of Edinburgh. DOI 10.7488/era/834. Chapter 4, printed pp.119-138; relevant
    general methods pp.158-167. Complete 217-page repository PDF acquired; this is
    primary thesis evidence, not a journal article. (https://doi.org/10.7488/era/834))
    report culture-level iron/sulfur oxidation and mineral transformation/leaching
    without single-gene knockouts; supports: partial is strictly preserved on all
    enzyme-level edges and ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
  locator: Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
    (SHA-256 b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9): Add
    culture_assisted_acid_leaching_graph causal graph and ground culture_assisted_acid_leaching
    to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans
    ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0
    rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and culture_assisted_acid_leaching_graph
    causal graph to eudialyte-ore.yaml.'
  snapshot_sha256: b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9
- evidence_id: edit_history_2
  kind: record_content
  reference: history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
  locator: Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
    (SHA-256 df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805): Align
    culture_assisted_acid_leaching_graph and protein_examples annotations with Sections
    4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1-4.5.4.1 in Hunter (2020) (Issue #925)
    — Updated culture_assisted_acid_leaching_graph and protein_examples in eudialyte-ore.yaml
    to cite Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1, 4.5.3.1, and 4.5.3.4-4.5.4.1
    of Hunter (2020) and match the ~3-week room-temperature (~25 C) triplicate 125
    mL flask conditions and absence of silica gelation at 0.50-1.00 g ore loading
    (Issue #925).'
  snapshot_sha256: df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805
- evidence_id: validation
  kind: validation
  reference: data/records/eudialyte-ore.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-04T22:38:30Z'
  support: supports
  summary: data/records/eudialyte-ore.yaml and history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml,
    history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml pass strict
    LinkML schema, protein_examples parity, and history validation with 0 errors.
  snapshot_sha256: bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 683 record(s); 0 failed.
  target_ids:
  - cmmmech:eudialyte-ore
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
  - cmmmech:eudialyte-ore
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB paralog grounding, and
    parity across causal_graph ''culture_assisted_acid_leaching_graph'' (mechanism_ref:
    culture_assisted_acid_leaching, 5 nodes / 4 edges; cyc2_outer_membrane_cytochrome:
    [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2, UP000001362)]; rus_cyc1_periplasmic_electron_transfer:
    [UniProtKB:B7JAQ0 (rus, RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2,
    UP000001362)])'
  outcome: supported
  summary: 'Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569)
    with causal_graph ''culture_assisted_acid_leaching_graph'' (mechanism_ref: culture_assisted_acid_leaching,
    5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
    UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus,
    RUS_ACIF2, UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]),
    achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from primary source(s)
    hunter2020. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
    (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
    ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
    gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans
    ATCC 23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
    cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
  target_ids:
  - cmmmech:eudialyte-ore
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/eudialyte-ore.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/eudialyte-ore/2026-11-04T210559Z-marcin-e72eff.yaml
    (SHA-256 b13253ca7fbe9928524ae0231855947153d4e9d1197de8a59571cea4a60ab6f9): Add
    culture_assisted_acid_leaching_graph causal graph and ground culture_assisted_acid_leaching
    to Acidithiobacillus ferrooxidans ATCC 23270 rus-operon UniProtKB entries (UniProtKB:B7JAQ7,
    UniProtKB:B7JAQ0, UniProtKB:B7JAQ6) — Added representative Acidithiobacillus ferrooxidans
    ATCC 23270 rus-operon protein_examples (UniProtKB:B7JAQ7 cyc2/AFE_3153, UniProtKB:B7JAQ0
    rus/AFE_3146, UniProtKB:B7JAQ6 cyc1/AFE_3152) and culture_assisted_acid_leaching_graph
    causal graph to eudialyte-ore.yaml.; history/records/eudialyte-ore/2026-11-04T223800Z-marcin-43b914.yaml
    (SHA-256 df1578758e510c461ce2399c19935adfb23976f3efc0113669d007e15831b805): Align
    culture_assisted_acid_leaching_graph and protein_examples annotations with Sections
    4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1-4.5.4.1 in Hunter (2020) (Issue #925)
    — Updated culture_assisted_acid_leaching_graph and protein_examples in eudialyte-ore.yaml
    to cite Sections 4.5.2-4.5.4 and 7.4.1 and Figures 4.5.2.1, 4.5.3.1, and 4.5.3.4-4.5.4.1
    of Hunter (2020) and match the ~3-week room-temperature (~25 C) triplicate 125
    mL flask conditions and absence of silica gelation at 0.50-1.00 g ore loading
    (Issue #925).) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:eudialyte-ore
  evidence_ids:
  - owner
  - edit_history
  - edit_history_2
  - validation
findings: []
actions: []
summary: 'Eudialyte ore (cmmmech:eudialyte-ore) passes Cycle 8 Stage 2 causal-graphs
  review (scientific_review: true) at SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569:
  Curated data/records/eudialyte-ore.yaml (SHA-256 bea193acd8a6bd7bcc48af7773671dc24a21cf6c4cd0fc33915793ebf463e569)
  with causal_graph ''culture_assisted_acid_leaching_graph'' (mechanism_ref: culture_assisted_acid_leaching,
  5 nodes / 4 edges; cyc2_outer_membrane_cytochrome: [UniProtKB:B7JAQ7 (cyc2, B7JAQ7_ACIF2,
  UP000001362)]; rus_cyc1_periplasmic_electron_transfer: [UniProtKB:B7JAQ0 (rus, RUS_ACIF2,
  UP000001362), UniProtKB:B7JAQ6 (cyc1, B7JAQ6_ACIF2, UP000001362)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and caveats from primary source(s)
  hunter2020. Live-verified UniProtKB reference-proteome grounding across UniProtKB:B7JAQ7
  (B7JAQ7_ACIF2, Cytochrome c, gene_symbol: cyc2, TREMBL, NCBITaxon:243159 Acidithiobacillus
  ferrooxidans ATCC 23270, UP000001362); UniProtKB:B7JAQ0 (RUS_ACIF2, Rusticyanin,
  gene_symbol: rus, SWISS_PROT, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC
  23270, UP000001362); UniProtKB:B7JAQ6 (B7JAQ6_ACIF2, Cytochrome c552, gene_symbol:
  cyc1, TREMBL, NCBITaxon:243159 Acidithiobacillus ferrooxidans ATCC 23270, UP000001362).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- 'Executed during Cycle 8 Stage 2 (causal_graphs) after addressing Issue #925 internal-consistency
  findings using scripts/curate_causal_graphs.py; supersedes initial review 20261104T210700Z-eudialyte-ore-cycle8-stage2-causal-graphs-review.'
related_reviews: []
```
