# Cycle 12 Stage 2 causal-graphs review of Strontium (cmmmech:strontium)

- Review: 20261109T163600Z-strontium-cycle12-stage2-causal-graphs-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-11-09T16:15:00Z
- Finished UTC: 2026-11-09T16:36:00Z
- Reviewer: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Strontium (cmmmech:strontium) passes Cycle 12 Stage 2 causal-graphs review (scientific_review: true) at SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe: Curated data/records/strontium.yaml with causal_graph 'tk2d_sr_biomineralization_graph' (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats from horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17). Live-verified UniProtKB grounding across UniProtKB:P77837 (URE1_BACSU, Urease subunit alpha, gene_symbol: ureC, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P71035 (URE2_BACSU, Urease subunit beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU, Urease subunit gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570).

## Scope And Provenance

Cycle 12 Stage 2 causal-graphs review of data/records/strontium.yaml (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe) and its canonical EDIT history sidecar(s) (history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml) verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source evidence fidelity across causal_graph 'tk2d_sr_biomineralization_graph' (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]).

Selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:strontium
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7449fa912e2d92f8aff400481ee75b49edbb685e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:strontium | data/records/strontium.yaml | maintained | Strontium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:strontium | Checked 703 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:strontium | Checked 1484 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Verification of causal_graphs structure, UniProtKB grounding, and parity across causal_graph 'tk2d_sr_biomineralization_graph' (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)])

graph: supported. Targets: cmmmech:strontium.

Curated data/records/strontium.yaml (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe) with causal_graph 'tk2d_sr_biomineralization_graph' (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17). Live-verified UniProtKB grounding across UniProtKB:P77837 (URE1_BACSU, Urease subunit alpha, gene_symbol: ureC, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P71035 (URE2_BACSU, Urease subunit beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU, Urease subunit gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570).

### Verification of canonical EDIT history sidecar(s) and strict schema validation

provenance: supported. Targets: cmmmech:strontium.

data/records/strontium.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only history sidecar(s) (history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml (SHA-256 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de: Add tk2d_sr_biomineralization_graph causal graph and ground tk2d_sr_biomineralization to congeneric Bacillus subtilis Swiss-Prot UreABC subunits (UniProtKB:P77837, UniProtKB:P71035, UniProtKB:P75030))) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/strontium.yaml; Working-tree record data/records/strontium.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/strontium.yaml (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe) with causal_graph 'tk2d_sr_biomineralization_graph' (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and experimental caveats. |
| primary_source | https://doi.org/10.1128/AEM.00855-17; horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17) | supports | Live-verified UniProtKB grounding across UniProtKB:P77837 (URE1_BACSU, Urease subunit alpha, gene_symbol: ureC, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P71035 (URE2_BACSU, Urease subunit beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU, Urease subunit gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570). Primary mechanism source (horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17)) parameters, analytical denominators, and source-level caveats are strictly preserved on all nodes, edges, and ProteinExample evidence items. |
| edit_history | history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml; Canonical EDIT history sidecar history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml | supports | Canonical EDIT history sidecar history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml (SHA-256 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de): Add tk2d_sr_biomineralization_graph causal graph and ground tk2d_sr_biomineralization to congeneric Bacillus subtilis Swiss-Prot UreABC subunits (UniProtKB:P77837, UniProtKB:P71035, UniProtKB:P75030) |
| validation | data/records/strontium.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/strontium.yaml and history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py for cmmmech:strontium.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T163600Z-strontium-cycle12-stage2-causal-graphs-review
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 12 Stage 2 causal-graphs review of Strontium (cmmmech:strontium)
started_at: '2026-11-09T16:15:00Z'
finished_at: '2026-11-09T16:36:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle12-stage2-causal-graphs-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: 'Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying the Cycle 12 Stage 2 causal_graphs and ProteinExample curation in data/records/strontium.yaml
    (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe) against
    live UniProtKB grounding and cited primary source (horiike_2017: Horiike, Dotsuta,
    Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal of Soluble Strontium
    via Incorporation into Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus
    sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental Microbiology
    83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17)).'
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 7449fa912e2d92f8aff400481ee75b49edbb685e
  state: working_tree
  inputs:
  - path: data/records/strontium.yaml
    sha256: f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe
    role: target
  - path: history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
    sha256: 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:strontium
  path: data/records/strontium.yaml
  label: Strontium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
    role: canonical_history
scope:
  description: 'Cycle 12 Stage 2 causal-graphs review of data/records/strontium.yaml
    (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe) and
    its canonical EDIT history sidecar(s) (history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml)
    verifying causal-graph node/edge topology, live UniProtKB grounding, and primary-source
    evidence fidelity across causal_graph ''tk2d_sr_biomineralization_graph'' (mechanism_ref:
    tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837
    (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570),
    UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]).'
  selection: Cycle 12 Stage 2 causal_graphs curation for cmmmech:strontium
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:strontium
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/strontium.yaml
  locator: Working-tree record data/records/strontium.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Curated data/records/strontium.yaml (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe)
    with causal_graph ''tk2d_sr_biomineralization_graph'' (mechanism_ref: tk2d_sr_biomineralization,
    4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU,
    UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030
    (ureA, URE3_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and experimental caveats.'
  snapshot_sha256: f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe
- evidence_id: primary_source
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.00855-17
  locator: 'horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and
    Yamashita (2017). Removal of Soluble Strontium via Incorporation into Biogenic
    Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in a Highly
    Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17. DOI
    10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17)'
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Live-verified UniProtKB grounding across UniProtKB:P77837 (URE1_BACSU,
    Urease subunit alpha, gene_symbol: ureC, SWISS_PROT, NCBITaxon:224308 Bacillus
    subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P71035 (URE2_BACSU,
    Urease subunit beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308 Bacillus
    subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU,
    Urease subunit gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus
    subtilis subsp. subtilis str. 168, UP000001570). Primary mechanism source (horiike_2017:
    Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal
    of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic
    Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental
    Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000.
    (https://doi.org/10.1128/AEM.00855-17)) parameters, analytical denominators, and
    source-level caveats are strictly preserved on all nodes, edges, and ProteinExample
    evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
  locator: Canonical EDIT history sidecar history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: 'Canonical EDIT history sidecar history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
    (SHA-256 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de): Add
    tk2d_sr_biomineralization_graph causal graph and ground tk2d_sr_biomineralization
    to congeneric Bacillus subtilis Swiss-Prot UreABC subunits (UniProtKB:P77837,
    UniProtKB:P71035, UniProtKB:P75030)'
  snapshot_sha256: 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de
- evidence_id: validation
  kind: validation
  reference: data/records/strontium.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-11-09T16:36:00Z'
  support: supports
  summary: data/records/strontium.yaml and history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 703 record(s); 0 failed.
  target_ids:
  - cmmmech:strontium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: validate_history
  name: Canonical history validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base main
  status: passed
  required: true
  summary: Checked 1484 history record(s); 0 error(s).
  target_ids:
  - cmmmech:strontium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: causal_graph_and_protein_grounding
  area: graph
  topic: 'Verification of causal_graphs structure, UniProtKB grounding, and parity
    across causal_graph ''tk2d_sr_biomineralization_graph'' (mechanism_ref: tk2d_sr_biomineralization,
    4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU,
    UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030
    (ureA, URE3_BACSU, UP000001570)])'
  outcome: supported
  summary: 'Curated data/records/strontium.yaml (SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe)
    with causal_graph ''tk2d_sr_biomineralization_graph'' (mechanism_ref: tk2d_sr_biomineralization,
    4 nodes / 3 edges; bacillus_ureabc_complex: [UniProtKB:P77837 (ureC, URE1_BACSU,
    UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU, UP000001570), UniProtKB:P75030
    (ureA, URE3_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples
    and causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from horiike_2017: Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya,
    Ohnuki and Yamashita (2017). Removal of Soluble Strontium via Incorporation into
    Biogenic Carbonate Minerals by Halophilic Bacterium Bacillus sp. Strain TK2d in
    a Highly Saline Solution. Applied and Environmental Microbiology 83(20), e00855-17.
    DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000. (https://doi.org/10.1128/AEM.00855-17).
    Live-verified UniProtKB grounding across UniProtKB:P77837 (URE1_BACSU, Urease
    subunit alpha, gene_symbol: ureC, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
    subsp. subtilis str. 168, UP000001570); UniProtKB:P71035 (URE2_BACSU, Urease subunit
    beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp.
    subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU, Urease subunit
    gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp.
    subtilis str. 168, UP000001570).'
  target_ids:
  - cmmmech:strontium
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT history sidecar(s) and strict schema validation
  outcome: supported
  summary: 'data/records/strontium.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only history sidecar(s) (history/records/strontium/2026-11-09T161813Z-marcin-f7c945.yaml
    (SHA-256 7ddb3e8869167ba24e991a8c132a57690ff4f43c362f4554a8b3592a26a313de: Add
    tk2d_sr_biomineralization_graph causal graph and ground tk2d_sr_biomineralization
    to congeneric Bacillus subtilis Swiss-Prot UreABC subunits (UniProtKB:P77837,
    UniProtKB:P71035, UniProtKB:P75030))) and passing all LinkML and history validation
    gates.'
  target_ids:
  - cmmmech:strontium
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Strontium (cmmmech:strontium) passes Cycle 12 Stage 2 causal-graphs review
  (scientific_review: true) at SHA-256 f066b1a1749226d70aede2fe7a871e40b11734ae3a348cd4c3326f6edd77fdbe:
  Curated data/records/strontium.yaml with causal_graph ''tk2d_sr_biomineralization_graph''
  (mechanism_ref: tk2d_sr_biomineralization, 4 nodes / 3 edges; bacillus_ureabc_complex:
  [UniProtKB:P77837 (ureC, URE1_BACSU, UP000001570), UniProtKB:P71035 (ureB, URE2_BACSU,
  UP000001570), UniProtKB:P75030 (ureA, URE3_BACSU, UP000001570)]), achieving 100%
  parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples
  and preserving source-faithful support levels and experimental caveats from horiike_2017:
  Horiike, Dotsuta, Nakano, Ochiai, Utsunomiya, Ohnuki and Yamashita (2017). Removal
  of Soluble Strontium via Incorporation into Biogenic Carbonate Minerals by Halophilic
  Bacterium Bacillus sp. Strain TK2d in a Highly Saline Solution. Applied and Environmental
  Microbiology 83(20), e00855-17. DOI 10.1128/AEM.00855-17; PMID 28802269; PMC5627000.
  (https://doi.org/10.1128/AEM.00855-17). Live-verified UniProtKB grounding across
  UniProtKB:P77837 (URE1_BACSU, Urease subunit alpha, gene_symbol: ureC, SWISS_PROT,
  NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P71035
  (URE2_BACSU, Urease subunit beta, gene_symbol: ureB, SWISS_PROT, NCBITaxon:224308
  Bacillus subtilis subsp. subtilis str. 168, UP000001570); UniProtKB:P75030 (URE3_BACSU,
  Urease subunit gamma, gene_symbol: ureA, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
  subsp. subtilis str. 168, UP000001570).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Executed during Cycle 12 Stage 2 (causal_graphs) using scripts/curate_causal_graphs.py
  for cmmmech:strontium.
related_reviews: []
```
