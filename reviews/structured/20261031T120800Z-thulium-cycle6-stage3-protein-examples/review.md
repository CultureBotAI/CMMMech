# Cycle 6 Stage 3 successor protein_examples review of Thulium (cmmmech:thulium)

- Review: 20261031T120800Z-thulium-cycle6-stage3-protein-examples
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-31T12:06:00Z
- Finished UTC: 2026-10-31T12:08:00Z
- Reviewer: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Thulium (cmmmech:thulium) passes Cycle 6 Stage 3 successor protein_examples review (scientific_review: true, superseding 20261031T110700Z-thulium-cycle6-stage3-protein-examples) at SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62: Align Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly EC 2.7.8.40) (#896). Live-verified UniProtKB metadata across UniProtKB:O34952 (LTAS2_BACSU, Lipoteichoic acid synthase 2, gene_symbol: ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic acid synthase 1, gene_symbol: ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic acid synthase YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]).

## Scope And Provenance

Cycle 6 Stage 3 successor protein_examples review of data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62) and its canonical EDIT correction history sidecar (history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml), superseding 20261031T110700Z-thulium-cycle6-stage3-protein-examples and verifying UniProtKB accession identity, reference-proteome grounding, EC/InterPro/Pfam cross-reference correspondence, node/mechanism parity, and primary-source evidence fidelity across causal_graph 'bsubtilis_ltas_thulium_biosorption_graph' (mechanism_ref: bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952 (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570), UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU, UP000001570)]).

Selection: Cycle 6 Stage 3 successor protein_examples review for cmmmech:thulium
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f9aa5d290081014a5d337f8ab33c2fcc464646f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:thulium | data/records/thulium.yaml | maintained | Thulium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation | passed | True | cmmmech:thulium | Checked 673 record(s); 0 failed. |
| Canonical history validation | passed | True | cmmmech:thulium | All history sidecars pass validation with 0 errors. |

## Scientific And Domain Assessments

### Verification of protein_examples UniProtKB accession identity, EC/InterPro/Pfam cross-references, and node/mechanism parity across causal_graph 'bsubtilis_ltas_thulium_biosorption_graph' (mechanism_ref: bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952 (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570), UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU, UP000001570)])

graph: supported. Targets: cmmmech:thulium.

Curated data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62) with causal_graph 'bsubtilis_ltas_thulium_biosorption_graph' (mechanism_ref: bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952 (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570), UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and live-verifying UniProtKB metadata across UniProtKB:O34952 (LTAS2_BACSU, Lipoteichoic acid synthase 2, gene_symbol: ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic acid synthase 1, gene_symbol: ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic acid synthase YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]).

### Verification of canonical EDIT correction history sidecar and strict schema validation

provenance: supported. Targets: cmmmech:thulium.

data/records/thulium.yaml was updated exclusively through scripts/curate_causal_graphs.py (curate_record_file), producing append-only correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml (SHA-256 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b: Align Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly EC 2.7.8.40) (#896)) and passing all LinkML and history validation gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/thulium.yaml; Working-tree record data/records/thulium.yaml (causal_graphs and mechanisms[].protein_examples) | supports | Curated data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62) with causal_graph 'bsubtilis_ltas_thulium_biosorption_graph' (mechanism_ref: bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952 (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570), UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU, UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and causal_graphs[].nodes[].protein_examples and preserving source-faithful support levels and caveats from primary source(s) moriwaki_accepted_manuscript. |
| primary_source | https://soar-ir.repo.nii.ac.jp/records/13337; moriwaki_accepted_manuscript: Moriwaki et al., Shinshu University deposited accepted manuscript; 24 PDF pages, methods pp. 5–9, results/discussion pp. 10–14, Tables 1–3 and Figures 1–3 (https://soar-ir.repo.nii.ac.jp/records/13337) | supports | Live-verified UniProtKB reference-proteome and domain cross-reference grounding across UniProtKB:O34952 (LTAS2_BACSU, Lipoteichoic acid synthase 2, gene_symbol: ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic acid synthase 1, gene_symbol: ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic acid synthase YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884, Pfam:PF27449]). Primary mechanism source(s) (moriwaki_accepted_manuscript) support the stated organism, substrate, and partial/direct support levels on all ProteinExample evidence items. |
| edit_history | history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml; Canonical EDIT correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml | supports | Canonical EDIT correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml (SHA-256 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b): Align Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly EC 2.7.8.40) (#896) — Updates ltas_synthase_paralogs.description and the functional_role descriptions on UniProtKB:O34952 (LtaS2, EC:2.7.8.-), UniProtKB:Q797B3 (LtaS1, EC:2.7.8.46), UniProtKB:P54496 (YqgS, EC:2.7.8.46), and UniProtKB:O32206 (YvgJ, EC:2.7.8.-) across both causal_graphs[0].nodes[0].protein_examples and mechanisms[0].protein_examples in data/records/thulium.yaml so prose EC numbers explicitly match structured UniProtKB ec_numbers while noting the transferred EC 2.7.8.40 designation (#896). |
| validation | data/records/thulium.yaml; Real CLI validation via python -m cmmmech validate --require-records and validate-history --base main | supports | data/records/thulium.yaml and history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml pass strict LinkML schema, protein_examples parity, and history validation with 0 errors. |

## Limits And Additional Notes

- Review is conducted in single-agent Goal Mode (independence: self_review) against working-tree bytes; an independent subagent PR review is executed prior to merge.
- Successor scientific review superseding immutable bundle 20261031T110700Z-thulium-cycle6-stage3-protein-examples after remediating independent review findings (#894/#895/#896).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T120800Z-thulium-cycle6-stage3-protein-examples
kind: record
repository: CultureBotAI/CMMMech
title: Cycle 6 Stage 3 successor protein_examples review of Thulium (cmmmech:thulium)
started_at: '2026-10-31T12:06:00Z'
finished_at: '2026-10-31T12:08:00Z'
reviewer:
  identity: antigravity / cmmmech-cycle6-stage3-protein-examples-reviewer
  kind: agent
  model: antigravity
  independence: self_review
  independence_basis: Single-agent Goal Mode execution of .claude/skills/review-record/SKILL.md
    verifying Cycle 6 Stage 3 successor protein_examples curation and provenance remediation
    (#894/#895/#896) in data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62)
    against live UniProtKB REST API metadata and cited primary source(s) moriwaki_accepted_manuscript.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 0f9aa5d290081014a5d337f8ab33c2fcc464646f
  state: working_tree
  inputs:
  - path: data/records/thulium.yaml
    sha256: d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62
    role: target
  - path: history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
    sha256: 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
targets:
- target_id: cmmmech:thulium
  path: data/records/thulium.yaml
  label: Thulium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/thulium.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
    role: canonical_history
scope:
  description: 'Cycle 6 Stage 3 successor protein_examples review of data/records/thulium.yaml
    (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62) and
    its canonical EDIT correction history sidecar (history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml),
    superseding 20261031T110700Z-thulium-cycle6-stage3-protein-examples and verifying
    UniProtKB accession identity, reference-proteome grounding, EC/InterPro/Pfam cross-reference
    correspondence, node/mechanism parity, and primary-source evidence fidelity across
    causal_graph ''bsubtilis_ltas_thulium_biosorption_graph'' (mechanism_ref: bsubtilis_powder_tm_biosorption,
    4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952 (ltaS2, LTAS2_BACSU,
    UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570), UniProtKB:P54496
    (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU, UP000001570)]).'
  selection: Cycle 6 Stage 3 successor protein_examples review for cmmmech:thulium
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:thulium
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/thulium.yaml
  locator: Working-tree record data/records/thulium.yaml (causal_graphs and mechanisms[].protein_examples)
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Curated data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62)
    with causal_graph ''bsubtilis_ltas_thulium_biosorption_graph'' (mechanism_ref:
    bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952
    (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570),
    UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU,
    UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and preserving source-faithful support
    levels and caveats from primary source(s) moriwaki_accepted_manuscript.'
  snapshot_sha256: d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62
- evidence_id: primary_source
  kind: primary_source
  reference: https://soar-ir.repo.nii.ac.jp/records/13337
  locator: 'moriwaki_accepted_manuscript: Moriwaki et al., Shinshu University deposited
    accepted manuscript; 24 PDF pages, methods pp. 5–9, results/discussion pp. 10–14,
    Tables 1–3 and Figures 1–3 (https://soar-ir.repo.nii.ac.jp/records/13337)'
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Live-verified UniProtKB reference-proteome and domain cross-reference
    grounding across UniProtKB:O34952 (LTAS2_BACSU, Lipoteichoic acid synthase 2,
    gene_symbol: ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis
    str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160,
    InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884,
    Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic acid synthase 1, gene_symbol:
    ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168,
    UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160,
    InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884,
    Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic acid synthase
    YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp.
    subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917,
    InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
    pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic
    acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
    subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917,
    InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
    pfam: [Pfam:PF00884, Pfam:PF27449]). Primary mechanism source(s) (moriwaki_accepted_manuscript)
    support the stated organism, substrate, and partial/direct support levels on all
    ProteinExample evidence items.'
- evidence_id: edit_history
  kind: record_content
  reference: history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
  locator: Canonical EDIT correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: 'Canonical EDIT correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
    (SHA-256 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b): Align
    Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description
    EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly
    EC 2.7.8.40) (#896) — Updates ltas_synthase_paralogs.description and the functional_role
    descriptions on UniProtKB:O34952 (LtaS2, EC:2.7.8.-), UniProtKB:Q797B3 (LtaS1,
    EC:2.7.8.46), UniProtKB:P54496 (YqgS, EC:2.7.8.46), and UniProtKB:O32206 (YvgJ,
    EC:2.7.8.-) across both causal_graphs[0].nodes[0].protein_examples and mechanisms[0].protein_examples
    in data/records/thulium.yaml so prose EC numbers explicitly match structured UniProtKB
    ec_numbers while noting the transferred EC 2.7.8.40 designation (#896).'
  snapshot_sha256: 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b
- evidence_id: validation
  kind: validation
  reference: data/records/thulium.yaml
  locator: Real CLI validation via python -m cmmmech validate --require-records and
    validate-history --base main
  accessed_at: '2026-10-31T12:07:30Z'
  support: supports
  summary: data/records/thulium.yaml and history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
    pass strict LinkML schema, protein_examples parity, and history validation with
    0 errors.
  snapshot_sha256: d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62
checks:
- check_id: validate_records
  name: Strict corpus validation
  command: PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records
  status: passed
  required: true
  summary: Checked 673 record(s); 0 failed.
  target_ids:
  - cmmmech:thulium
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
  - cmmmech:thulium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
assessments:
- assessment_id: protein_examples_and_uniprot_grounding
  area: graph
  topic: 'Verification of protein_examples UniProtKB accession identity, EC/InterPro/Pfam
    cross-references, and node/mechanism parity across causal_graph ''bsubtilis_ltas_thulium_biosorption_graph''
    (mechanism_ref: bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs:
    [UniProtKB:O34952 (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1,
    LTAS1_BACSU, UP000001570), UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206
    (yvgJ, YVGJ_BACSU, UP000001570)])'
  outcome: supported
  summary: 'Curated data/records/thulium.yaml (SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62)
    with causal_graph ''bsubtilis_ltas_thulium_biosorption_graph'' (mechanism_ref:
    bsubtilis_powder_tm_biosorption, 4 nodes / 3 edges; ltas_synthase_paralogs: [UniProtKB:O34952
    (ltaS2, LTAS2_BACSU, UP000001570), UniProtKB:Q797B3 (ltaS1, LTAS1_BACSU, UP000001570),
    UniProtKB:P54496 (yqgS, YQGS_BACSU, UP000001570), UniProtKB:O32206 (yvgJ, YVGJ_BACSU,
    UP000001570)]), achieving 100% parity between mechanisms[].protein_examples and
    causal_graphs[].nodes[].protein_examples and live-verifying UniProtKB metadata
    across UniProtKB:O34952 (LTAS2_BACSU, Lipoteichoic acid synthase 2, gene_symbol:
    ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168,
    UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917, InterPro:IPR012160,
    InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884,
    Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic acid synthase 1, gene_symbol:
    ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp. subtilis str. 168,
    UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917, InterPro:IPR012160,
    InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270], pfam: [Pfam:PF00884,
    Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic acid synthase
    YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis subsp.
    subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917,
    InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
    pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic
    acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
    subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917,
    InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
    pfam: [Pfam:PF00884, Pfam:PF27449]).'
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - owner
  - primary_source
- assessment_id: provenance_and_validation_verification
  area: provenance
  topic: Verification of canonical EDIT correction history sidecar and strict schema
    validation
  outcome: supported
  summary: 'data/records/thulium.yaml was updated exclusively through scripts/curate_causal_graphs.py
    (curate_record_file), producing append-only correction history sidecar history/records/thulium/2026-10-31T120502Z-marcin-dd7951.yaml
    (SHA-256 359ba17a2b4aabe91d230b7cf29f59aa20cc44364370f241ff3f95ba4f0e326b: Align
    Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description
    EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly
    EC 2.7.8.40) (#896)) and passing all LinkML and history validation gates.'
  target_ids:
  - cmmmech:thulium
  evidence_ids:
  - owner
  - edit_history
  - validation
findings: []
actions: []
summary: 'Thulium (cmmmech:thulium) passes Cycle 6 Stage 3 successor protein_examples
  review (scientific_review: true, superseding 20261031T110700Z-thulium-cycle6-stage3-protein-examples)
  at SHA-256 d7d49d1af77bbbc3654054a6b65877d1d04b57fa47c4e83c75cfa7491371ec62: Align
  Bacillus subtilis 168 LtaS2/LtaS1/YqgS/YvgJ functional_role and node description
  EC numbers with structured UniProtKB ec_numbers (EC 2.7.8.46 / EC 2.7.8.-, formerly
  EC 2.7.8.40) (#896). Live-verified UniProtKB metadata across UniProtKB:O34952 (LTAS2_BACSU,
  Lipoteichoic acid synthase 2, gene_symbol: ltaS2, SWISS_PROT, NCBITaxon:224308 Bacillus
  subtilis subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917,
  InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
  pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:Q797B3 (LTAS1_BACSU, Lipoteichoic
  acid synthase 1, gene_symbol: ltaS1, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
  subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917,
  InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
  pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:P54496 (YQGS_BACSU, Minor lipoteichoic
  acid synthase YqgS, gene_symbol: yqgS, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
  subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.46], interpro: [InterPro:IPR000917,
  InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
  pfam: [Pfam:PF00884, Pfam:PF27449]); UniProtKB:O32206 (YVGJ_BACSU, putative lipoteichoic
  acid primase YvgJ, gene_symbol: yvgJ, SWISS_PROT, NCBITaxon:224308 Bacillus subtilis
  subsp. subtilis str. 168, UP000001570, ec: [EC:2.7.8.-], interpro: [InterPro:IPR000917,
  InterPro:IPR012160, InterPro:IPR017850, InterPro:IPR050448, InterPro:IPR060270],
  pfam: [Pfam:PF00884, Pfam:PF27449]).'
limitations:
- 'Review is conducted in single-agent Goal Mode (independence: self_review) against
  working-tree bytes; an independent subagent PR review is executed prior to merge.'
notes:
- Successor scientific review superseding immutable bundle 20261031T110700Z-thulium-cycle6-stage3-protein-examples
  after remediating independent review findings (#894/#895/#896).
related_reviews: []
```
