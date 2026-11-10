# Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Chromium-tanned leather shavings (cmmmech:chromium-tanned-leather-shavings)

- Review: 20261110T054200Z-chromium-tanned-leather-shavings-cycle13-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-10T05:40:00Z
- Finished UTC: 2026-11-10T05:42:00Z
- Reviewer: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chromium-tanned leather shavings (cmmmech:chromium-tanned-leather-shavings) passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2: Updated data/records/chromium-tanned-leather-shavings.yaml with 'ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph' (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes / 4 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML, Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23). Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI, pH-response transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300).

## Scope And Provenance

Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/chromium-tanned-leather-shavings.yaml (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2) and its canonical EDIT history sidecar (history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:P78978 (PACC_YARLI, pH-response transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300)), and primary-source evidence fidelity across 'ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph' (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes / 4 edges).

Selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:chromium-tanned-leather-shavings
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chromium-tanned-leather-shavings | data/records/chromium-tanned-leather-shavings.yaml | maintained | Chromium-tanned leather shavings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:chromium-tanned-leather-shavings | Checked 708 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:chromium-tanned-leather-shavings | Checked 1529 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across 'ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph' (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes / 4 edges)

graph: supported. Targets: cmmmech:chromium-tanned-leather-shavings.

Updated data/records/chromium-tanned-leather-shavings.yaml (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2) with causal_graphs ('ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph' (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML, Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23). Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI, pH-response transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300).

### Verification of canonical EDIT history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:chromium-tanned-leather-shavings.

data/records/chromium-tanned-leather-shavings.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml (SHA-256 d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899: Add ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph causal graph and ground ips21_matrix_bioconversion_and_chromium_partitioning to reviewed Yarrowia lipolytica Swiss-Prot entries (UniProtKB:P09230, UniProtKB:Q92389, UniProtKB:P78978)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/chromium-tanned-leather-shavings.yaml; Working-tree record data/records/chromium-tanned-leather-shavings.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Updated data/records/chromium-tanned-leather-shavings.yaml (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2) with causal_graphs ('ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph' (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1128/spectrum.02749-23; wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML, Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23) | supports | Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI, pH-response transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300). Primary mechanism source (wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML, Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23)) parameters and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml; Canonical EDIT history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml | supports | Canonical EDIT history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml (SHA-256 d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899): Add ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph causal graph and ground ips21_matrix_bioconversion_and_chromium_partitioning to reviewed Yarrowia lipolytica Swiss-Prot entries (UniProtKB:P09230, UniProtKB:Q92389, UniProtKB:P78978) |
| validation | data/records/chromium-tanned-leather-shavings.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/chromium-tanned-leather-shavings.yaml and history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:chromium-tanned-leather-shavings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T054200Z-chromium-tanned-leather-shavings-cycle13-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 13 Stage 2 causal_graphs and UniProtKB grounding review of Chromium-tanned
  leather shavings (cmmmech:chromium-tanned-leather-shavings)
started_at: '2026-11-10T05:40:00Z'
finished_at: '2026-11-10T05:42:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle13-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 13 Stage 2 curation of data/records/chromium-tanned-leather-shavings.yaml
    (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2) against
    live UniProtKB grounding and cited primary source (wieczorek2023: Dorota Wieczorek,
    Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska
    (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica IPS21 to
    high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23.
    DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML,
    Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal
    local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 3bc89f7aeaf6db9fc42676e61efb86ca906fbdc5
  state: working_tree
  inputs:
  - path: data/records/chromium-tanned-leather-shavings.yaml
    sha256: 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2
    role: target
  - path: history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
    sha256: d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:chromium-tanned-leather-shavings
  path: data/records/chromium-tanned-leather-shavings.yaml
  label: Chromium-tanned leather shavings
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromium-tanned-leather-shavings.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
    role: canonical_history
scope:
  description: 'Cycle 13 Stage 2 causal_graphs and protein_examples review of data/records/chromium-tanned-leather-shavings.yaml
    (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2) and
    its canonical EDIT history sidecar (history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding (UniProtKB:P78978
    (PACC_YARLI, pH-response transcription factor pacC/RIM101, gene_symbol: RIM101,
    SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300);
    UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2,
    SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300);
    UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1,
    SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300)),
    and primary-source evidence fidelity across ''ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph''
    (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes
    / 4 edges).'
  selection: Cycle 13 Stage 2 causal_graphs cohort review for cmmmech:chromium-tanned-leather-shavings
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chromium-tanned-leather-shavings
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/chromium-tanned-leather-shavings.yaml
  locator: Working-tree record data/records/chromium-tanned-leather-shavings.yaml
    (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Updated data/records/chromium-tanned-leather-shavings.yaml (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2)
    with causal_graphs (''ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph''
    (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes
    / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and experimental caveats.'
  snapshot_sha256: 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/spectrum.02749-23
  locator: 'wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz,
    Anna Słubik and Katarzyna Ławińska (2023). Biotransformation of protein-rich waste
    by Yarrowia lipolytica IPS21 to high-value products—amino acid supernatants. Microbiology
    Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069.
    Complete original JATS/HTML, Tables 1–2, Figures 1–5 and all five supplemental
    PDFs inspected; the nominal local main-PDF download was HTML and is not evidence.
    (https://doi.org/10.1128/spectrum.02749-23)'
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI,
    pH-response transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT,
    NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300);
    UniProtKB:P09230 (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2,
    SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300);
    UniProtKB:Q92389 (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1,
    SWISS_PROT, NCBITaxon:284591 Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300).
    Primary mechanism source (wieczorek2023: Dorota Wieczorek, Dorota Gendaszewska,
    Katarzyna Miśkiewicz, Anna Słubik and Katarzyna Ławińska (2023). Biotransformation
    of protein-rich waste by Yarrowia lipolytica IPS21 to high-value products—amino
    acid supernatants. Microbiology Spectrum 11(5):e02749-23. DOI 10.1128/spectrum.02749-23;
    PMID 37707427; PMC10581069. Complete original JATS/HTML, Tables 1–2, Figures 1–5
    and all five supplemental PDFs inspected; the nominal local main-PDF download
    was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23)) parameters
    and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
  locator: Canonical EDIT history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
    (SHA-256 d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899): Add
    ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph causal
    graph and ground ips21_matrix_bioconversion_and_chromium_partitioning to reviewed
    Yarrowia lipolytica Swiss-Prot entries (UniProtKB:P09230, UniProtKB:Q92389, UniProtKB:P78978)'
  snapshot_sha256: d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899
- evidence_id: validation
  kind: validation
  reference: data/records/chromium-tanned-leather-shavings.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-10T05:42:00Z'
  support: supports
  summary: data/records/chromium-tanned-leather-shavings.yaml and history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 708 record(s); 0 failed.
  target_ids:
  - cmmmech:chromium-tanned-leather-shavings
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1529 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chromium-tanned-leather-shavings
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across ''ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph''
    (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes
    / 4 edges)'
  outcome: supported
  summary: 'Updated data/records/chromium-tanned-leather-shavings.yaml (SHA-256 45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2)
    with causal_graphs (''ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph''
    (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes
    / 4 edges)), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
    and preserving source-faithful support levels and caveats from wieczorek2023:
    Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna
    Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica
    IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23.
    DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML,
    Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal
    local main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23).
    Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI, pH-response
    transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591
    Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230
    (AEP_YARLI, Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591
    Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389
    (AXP1_YARLI, Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591
    Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300).'
  target_ids:
  - cmmmech:chromium-tanned-leather-shavings
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar and strict schema validation
  outcome: supported
  summary: 'data/records/chromium-tanned-leather-shavings.yaml was updated exclusively
    through scripts/curate_causal_graphs.py (curate_record_file), producing append-only
    history sidecar history/records/chromium-tanned-leather-shavings/2026-11-10T054033Z-marcin-dd04cd.yaml
    (SHA-256 d77b4e7ff9ae9303bb8eb572f0bf342faf89829493866c48a00a871cd5341899: Add
    ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph causal
    graph and ground ips21_matrix_bioconversion_and_chromium_partitioning to reviewed
    Yarrowia lipolytica Swiss-Prot entries (UniProtKB:P09230, UniProtKB:Q92389, UniProtKB:P78978))
    and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:chromium-tanned-leather-shavings
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Chromium-tanned leather shavings (cmmmech:chromium-tanned-leather-shavings)
  passes Cycle 13 Stage 2 causal_graphs review (scientific_review: true) at SHA-256
  45175ecd151b02d096b4f3a6b8a1fa96fe3edec69cc549a5209ff3dbdb28c4a2: Updated data/records/chromium-tanned-leather-shavings.yaml
  with ''ips21_proteolytic_leather_matrix_bioconversion_and_cr_partitioning_graph''
  (mechanism_ref: ips21_matrix_bioconversion_and_chromium_partitioning, 5 nodes /
  4 edges), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from wieczorek2023:
  Dorota Wieczorek, Dorota Gendaszewska, Katarzyna Miśkiewicz, Anna Słubik and Katarzyna
  Ławińska (2023). Biotransformation of protein-rich waste by Yarrowia lipolytica
  IPS21 to high-value products—amino acid supernatants. Microbiology Spectrum 11(5):e02749-23.
  DOI 10.1128/spectrum.02749-23; PMID 37707427; PMC10581069. Complete original JATS/HTML,
  Tables 1–2, Figures 1–5 and all five supplemental PDFs inspected; the nominal local
  main-PDF download was HTML and is not evidence. (https://doi.org/10.1128/spectrum.02749-23).
  Live-verified UniProtKB grounding across UniProtKB:P78978 (PACC_YARLI, pH-response
  transcription factor pacC/RIM101, gene_symbol: RIM101, SWISS_PROT, NCBITaxon:284591
  Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:P09230 (AEP_YARLI,
  Alkaline extracellular protease, gene_symbol: XPR2, SWISS_PROT, NCBITaxon:284591
  Yarrowia lipolytica (strain CLIB 122 / E 150), UP000001300); UniProtKB:Q92389 (AXP1_YARLI,
  Acid extracellular protease, gene_symbol: AXP1, SWISS_PROT, NCBITaxon:284591 Yarrowia
  lipolytica (strain CLIB 122 / E 150), UP000001300).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 13 Stage 2 (causal_graphs) for cmmmech:chromium-tanned-leather-shavings.
related_reviews: []
```
