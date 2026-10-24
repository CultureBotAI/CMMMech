# Cycle 3 Stage 5 Post-Remediation Verification Review: 3 Remediated CMMMech Records

- Review: 20261024T034200Z-cycle3-stage5-remediation-verification
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-24T03:40:00Z
- Finished UTC: 2026-10-24T03:42:00Z
- Reviewer: antigravity / cmmmech-cycle3-stage5-remediation-reviewer (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation scientific and structural verification of all 3 CMMMech records remediated in Cycle 3 Stage 5 (run mech-goal-sequence-20261019, cycle 3, stage 5) across GitHub issues #830 (GRP-C3S5-001: cmmmech-cycle3-stage4-finding-0001, bixbyite-mn.yaml protein_examples[0] for UniProtKB:A0A0K2YWP2 updated with gene_symbol: Mesau_02205 on both mechanisms[0] and causal_graphs[0].nodes[0]), #831 (GRP-C3S5-002: cmmmech-cycle3-stage4-finding-0002, olivine-group.yaml 2019 IMA-CNMNC Nomenclature Compendium source ID normalized from ima_compendium to canonical ima_compendium_2019), and #832 (GRP-C3S5-003: cmmmech-cycle3-stage4-finding-0003, humboldtine.yaml Aspergillus niger strain Ch 4/07 GenBank ITS KF768341.1 source ID and source_ref normalized from genbank_niger to canonical genbank_ch407). All 3 carried-forward Cycle 3 Stage 4 findings are verified as resolved with append-only EDIT history sidecars.

## Scope And Provenance

All 3 CMMMech records affected by the 3 Cycle 3 Stage 4 findings carried into Stage 5 (bixbyite-mn in GRP-C3S5-001 / #830, olivine-group in GRP-C3S5-002 / #831, and humboldtine in GRP-C3S5-003 / #832).

Selection: cycle3_stage4_open_finding_targets
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 3d36a06c76337922d651bdacbffbe05368e28abc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:bixbyite-mn | data/records/bixbyite-mn.yaml | maintained | Bixbyite-(Mn) |
| cmmmech:humboldtine | data/records/humboldtine.yaml | maintained | Humboldtine |
| cmmmech:olivine-group | data/records/olivine-group.yaml | maintained | Olivine group |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema and semantic record validation | passed | True | cmmmech:bixbyite-mn, cmmmech:humboldtine, cmmmech:olivine-group | All 646 records (including all 3 remediated records) pass .venv/bin/python -m cmmmech.cli validate --strict with 0 errors and 0 warnings. |
| Append-only history sidecar validation | passed | True | cmmmech:bixbyite-mn, cmmmech:humboldtine, cmmmech:olivine-group | All 3 new EDIT history sidecars and existing history sidecars pass .venv/bin/python -m cmmmech.cli validate-history --base main. |
| Mesau_02205 gene_symbol parity on UniProtKB:A0A0K2YWP2 in bixbyite-mn.yaml (#830) | passed | True | cmmmech:bixbyite-mn | Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml now explicitly carry gene_symbol: Mesau_02205, matching parent node tg1_acidic_mn_oxidase_factor and paired reference-proteome homolog UniProtKB:L0KKS2. |
| Canonical ima_compendium_2019 source key in olivine-group.yaml (#831) | passed | True | cmmmech:olivine-group | data/records/olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature Compendium under canonical sources[0].id: ima_compendium_2019, achieving 5/5 uniformity across all mineral_group records citing that compilation. |
| Canonical genbank_ch407 source key and source_ref in humboldtine.yaml (#832) | passed | True | cmmmech:humboldtine | data/records/humboldtine.yaml now keys GenBank ITS accession KF768341.1 for Aspergillus niger strain Ch 4/07 under canonical sources[4].id: genbank_ch407 and mechanisms[0].evidence[3].source_ref: genbank_ch407, achieving 6/6 uniformity across the Aspergillus niger Ch 4/07 oxalate/phosphate mineral cohort. |

## Scientific And Domain Assessments

### Mesau_02205 gene_symbol parity on UniProtKB:A0A0K2YWP2 in bixbyite-mn.yaml (#830)

consistency: supported. Targets: cmmmech:bixbyite-mn.

Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml now include gene_symbol: Mesau_02205, achieving 100% parity with parent node tg1_acidic_mn_oxidase_factor and paired homolog UniProtKB:L0KKS2.

### Canonical ima_compendium_2019 source key in olivine-group.yaml (#831)

consistency: supported. Targets: cmmmech:olivine-group.

data/records/olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature Compendium under canonical id: ima_compendium_2019, matching all 4 sibling mineral_group records citing that compilation (biotite, chlorite, illite, potassium-feldspar).

### Canonical genbank_ch407 source key in humboldtine.yaml (#832)

consistency: supported. Targets: cmmmech:humboldtine.

data/records/humboldtine.yaml now keys GenBank ITS accession KF768341.1 for Aspergillus niger strain Ch 4/07 under canonical sources[4].id: genbank_ch407 and mechanisms[0].evidence[3].source_ref: genbank_ch407, matching all 5 sibling Ch 4/07 mineral records (hopeite, katsarosite, moolooite, wheatleyite, whewellite).

## Findings

### cmmmech-cycle3-stage4-finding-0001: bixbyite-mn.yaml protein_examples[0] (UniProtKB:A0A0K2YWP2) now carries gene_symbol: Mesau_02205

minor / resolved / confirmed; issue key: cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol.

Added gene_symbol: Mesau_02205 to mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH) in data/records/bixbyite-mn.yaml with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #830 (group GRP-C3S5-001) by adding gene_symbol: Mesau_02205 to both mechanism and causal-graph node protein_examples[0] in data/records/bixbyite-mn.yaml with an append-only EDIT history sidecar.

### cmmmech-cycle3-stage4-finding-0002: olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature Compendium under canonical ima_compendium_2019

minor / resolved / confirmed; issue key: cmmmech.mineral_group.noncanonical-ima-compendium-source-id.

Normalized sources[0].id from ima_compendium to canonical ima_compendium_2019 in data/records/olivine-group.yaml with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #831 (group GRP-C3S5-002) by normalizing sources[0].id to ima_compendium_2019 in data/records/olivine-group.yaml with an append-only EDIT history sidecar.

### cmmmech-cycle3-stage4-finding-0003: humboldtine.yaml now keys GenBank ITS accession KF768341.1 under canonical genbank_ch407

minor / resolved / confirmed; issue key: cmmmech.mineral.noncanonical-ch407-its-source-id.

Normalized sources[4].id and mechanisms[0].evidence[3].source_ref from genbank_niger to canonical genbank_ch407 in data/records/humboldtine.yaml with an append-only EDIT history sidecar.

Disposition: Resolved under GitHub issue #832 (group GRP-C3S5-003) by normalizing sources[4].id and mechanisms[0].evidence[3].source_ref to genbank_ch407 in data/records/humboldtine.yaml with an append-only EDIT history sidecar.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:bixbyite-mn, cmmmech:humboldtine, cmmmech:olivine-group. All 3 remediated records represent distinct mineral species (2 records: bixbyite-mn, humboldtine) or mineral groups (1 record: olivine-group) with disjoint identifiers and provenance; cohort boundaries from Cycle 3 Stage 4 are retained unchanged.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-uniprot-a0a0k2ywp2 | https://rest.uniprot.org/uniprotkb/A0A0K2YWP2.json; UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH) and reference-proteome homolog UniProtKB:L0KKS2 (Mesau_02205) | supports | UniProtKB entry A0A0K2YWP2 (Multicopper oxidase, Mesorhizobium sp. TG-1, GenBank AIM41301.1) and its Mesorhizobium australicum WSM2073 reference-proteome homolog UniProtKB:L0KKS2 (locus tag Mesau_02205). |
| ev-ima-compendium-2019 | https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf; IMA-CNMNC Compendium of Mineral Nomenclature (2019) | supports | 2019 IMA-CNMNC Nomenclature Compendium cited across all 5 mineral_group records (biotite, chlorite, illite, olivine-group, potassium-feldspar) under canonical source key ima_compendium_2019. |
| ev-genbank-kf768341 | https://www.ncbi.nlm.nih.gov/nuccore/KF768341.1; GenBank KF768341.1 (Aspergillus niger strain Ch 4/07 ITS) | supports | GenBank ITS accession KF768341.1 for Aspergillus niger strain Ch 4/07 cited across all 6 sibling Ch 4/07 mineral records (hopeite, humboldtine, katsarosite, moolooite, wheatleyite, whewellite) under canonical source key genbank_ch407. |
| ev-cycle3-stage4-findings | reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/review_findings.yaml; findings[0..2] | supports | Frozen Cycle 3 Stage 4 review findings ledger defining cmmmech-cycle3-stage4-finding-0001, cmmmech-cycle3-stage4-finding-0002, and cmmmech-cycle3-stage4-finding-0003 across the 3 target records. |
| ev-schema | src/cmmmech/schema/cmmmech.yaml; classes.MaterialRecord, classes.ProteinExample, classes.Source | supports | Canonical LinkML schema defining MaterialRecord, ProteinExample, and Source. |

## Limits And Additional Notes

- This verification review is scoped to the 3 records remediated in Cycle 3 Stage 5; the remaining 643 records were verified with 0 open findings in the immutable Cycle 3 Stage 4 review bundles.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T034200Z-cycle3-stage5-remediation-verification
title: 'Cycle 3 Stage 5 Post-Remediation Verification Review: 3 Remediated CMMMech
  Records'
repository: CultureBotAI/CMMMech
kind: category
started_at: '2026-10-24T03:40:00Z'
finished_at: '2026-10-24T03:42:00Z'
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Post-remediation scientific and structural verification of all 3 CMMMech
  records remediated in Cycle 3 Stage 5 (run mech-goal-sequence-20261019, cycle 3,
  stage 5) across GitHub issues #830 (GRP-C3S5-001: cmmmech-cycle3-stage4-finding-0001,
  bixbyite-mn.yaml protein_examples[0] for UniProtKB:A0A0K2YWP2 updated with gene_symbol:
  Mesau_02205 on both mechanisms[0] and causal_graphs[0].nodes[0]), #831 (GRP-C3S5-002:
  cmmmech-cycle3-stage4-finding-0002, olivine-group.yaml 2019 IMA-CNMNC Nomenclature
  Compendium source ID normalized from ima_compendium to canonical ima_compendium_2019),
  and #832 (GRP-C3S5-003: cmmmech-cycle3-stage4-finding-0003, humboldtine.yaml Aspergillus
  niger strain Ch 4/07 GenBank ITS KF768341.1 source ID and source_ref normalized
  from genbank_niger to canonical genbank_ch407). All 3 carried-forward Cycle 3 Stage
  4 findings are verified as resolved with append-only EDIT history sidecars.'
reviewer:
  identity: antigravity / cmmmech-cycle3-stage5-remediation-reviewer
  kind: agent
  independence: self_review
  independence_basis: Cycle 3 Stage 5 post-remediation verification review (.claude/skills/review-yaml-category/SKILL.md)
    of the 3 remediated records against the immutable Cycle 3 Stage 4 review bundles.
  model: claude-opus-4-6
source:
  git_revision: 3d36a06c76337922d651bdacbffbe05368e28abc
  state: working_tree
  inputs:
  - path: data/records/bixbyite-mn.yaml
    sha256: bd546f878977f8954f3c3fafb9ed52ea912984b23c53236452eb843f98ae3b81
    role: target
  - path: data/records/humboldtine.yaml
    sha256: 89ce3f10493aae4051b520f74ed762fedc9a779eac49c4b94e644c7c9edd9241
    role: target
  - path: data/records/olivine-group.yaml
    sha256: 5d4bc2931ae936c7b536919030546e3c32131b55d6c0d1eaf854bcb047dd2418
    role: target
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml
    sha256: 0f2abb0b16f292df06e8e4388f14528c328feb975ce8b5240855f8c092bd0a60
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/review_findings.yaml
    sha256: 7ca7ad9bbdef88ee30cb7bd67e4a4245e8b15f5bbd1433af6c7555f2a9b2d9f8
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
    role: context
  - path: src/cmmmech/validation.py
    sha256: 63ff33d51b753dd715e6bd1c3e5f60a99e4fcb41b3aee68d536306a862d922e2
    role: context
targets:
- target_id: cmmmech:bixbyite-mn
  path: data/records/bixbyite-mn.yaml
  label: Bixbyite-(Mn)
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 3a31879608b17c29b75e7556ebd65f26e85ffb8d6c6edcf1630b27937c598fbb
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
    role: maintained_record
- target_id: cmmmech:humboldtine
  path: data/records/humboldtine.yaml
  label: Humboldtine
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: 9a15ee33f2316aea92a4c7b49bfc1608016c52e568e0c07311102bb8e536f662
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/humboldtine.yaml
    role: maintained_record
- target_id: cmmmech:olivine-group
  path: data/records/olivine-group.yaml
  label: Olivine group
  record_class: MaterialRecord
  kind: maintained
  semantic_digest:
    algorithm: yaml_canonical_sha256
    sha256: b806a0f8a7d93d7e384ed60c9d50f45b99065a77291ae049a74e1dcf84ad257f
    description: SHA-256 of canonical sorted-key YAML parse of record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
scope:
  description: 'All 3 CMMMech records affected by the 3 Cycle 3 Stage 4 findings carried
    into Stage 5 (bixbyite-mn in GRP-C3S5-001 / #830, olivine-group in GRP-C3S5-002
    / #831, and humboldtine in GRP-C3S5-003 / #832).'
  selection: cycle3_stage4_open_finding_targets
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - cmmmech:bixbyite-mn
  - cmmmech:humboldtine
  - cmmmech:olivine-group
checks:
- check_id: chk-validate-records
  name: Schema and semantic record validation
  status: passed
  required: true
  summary: All 646 records (including all 3 remediated records) pass .venv/bin/python
    -m cmmmech.cli validate --strict with 0 errors and 0 warnings.
  target_ids:
  - cmmmech:bixbyite-mn
  - cmmmech:humboldtine
  - cmmmech:olivine-group
  command: .venv/bin/python -m cmmmech.cli validate --strict
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle3-stage4-findings
  - ev-schema
- check_id: chk-validate-history
  name: Append-only history sidecar validation
  status: passed
  required: true
  summary: All 3 new EDIT history sidecars and existing history sidecars pass .venv/bin/python
    -m cmmmech.cli validate-history --base main.
  target_ids:
  - cmmmech:bixbyite-mn
  - cmmmech:humboldtine
  - cmmmech:olivine-group
  command: .venv/bin/python -m cmmmech.cli validate-history --base main
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-cycle3-stage4-findings
- check_id: chk-bixbyite-mn-gene-symbol
  name: Mesau_02205 gene_symbol parity on UniProtKB:A0A0K2YWP2 in bixbyite-mn.yaml
    (#830)
  status: passed
  required: true
  summary: 'Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml now explicitly carry
    gene_symbol: Mesau_02205, matching parent node tg1_acidic_mn_oxidase_factor and
    paired reference-proteome homolog UniProtKB:L0KKS2.'
  target_ids:
  - cmmmech:bixbyite-mn
  evidence_ids:
  - ev-uniprot-a0a0k2ywp2
  - ev-cycle3-stage4-findings
  - ev-schema
- check_id: chk-olivine-group-ima-compendium-source-id
  name: Canonical ima_compendium_2019 source key in olivine-group.yaml (#831)
  status: passed
  required: true
  summary: 'data/records/olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature
    Compendium under canonical sources[0].id: ima_compendium_2019, achieving 5/5 uniformity
    across all mineral_group records citing that compilation.'
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - ev-ima-compendium-2019
  - ev-cycle3-stage4-findings
- check_id: chk-humboldtine-ch407-source-id
  name: Canonical genbank_ch407 source key and source_ref in humboldtine.yaml (#832)
  status: passed
  required: true
  summary: 'data/records/humboldtine.yaml now keys GenBank ITS accession KF768341.1
    for Aspergillus niger strain Ch 4/07 under canonical sources[4].id: genbank_ch407
    and mechanisms[0].evidence[3].source_ref: genbank_ch407, achieving 6/6 uniformity
    across the Aspergillus niger Ch 4/07 oxalate/phosphate mineral cohort.'
  target_ids:
  - cmmmech:humboldtine
  evidence_ids:
  - ev-genbank-kf768341
  - ev-cycle3-stage4-findings
evidence:
- evidence_id: ev-uniprot-a0a0k2ywp2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A0K2YWP2.json
  locator: UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH) and reference-proteome homolog
    UniProtKB:L0KKS2 (Mesau_02205)
  accessed_at: '2026-10-24T03:40:00Z'
  support: supports
  summary: UniProtKB entry A0A0K2YWP2 (Multicopper oxidase, Mesorhizobium sp. TG-1,
    GenBank AIM41301.1) and its Mesorhizobium australicum WSM2073 reference-proteome
    homolog UniProtKB:L0KKS2 (locus tag Mesau_02205).
- evidence_id: ev-ima-compendium-2019
  kind: authority
  reference: https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf
  locator: IMA-CNMNC Compendium of Mineral Nomenclature (2019)
  accessed_at: '2026-10-24T03:40:00Z'
  support: supports
  summary: 2019 IMA-CNMNC Nomenclature Compendium cited across all 5 mineral_group
    records (biotite, chlorite, illite, olivine-group, potassium-feldspar) under canonical
    source key ima_compendium_2019.
- evidence_id: ev-genbank-kf768341
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/KF768341.1
  locator: GenBank KF768341.1 (Aspergillus niger strain Ch 4/07 ITS)
  accessed_at: '2026-10-24T03:40:00Z'
  support: supports
  summary: GenBank ITS accession KF768341.1 for Aspergillus niger strain Ch 4/07 cited
    across all 6 sibling Ch 4/07 mineral records (hopeite, humboldtine, katsarosite,
    moolooite, wheatleyite, whewellite) under canonical source key genbank_ch407.
- evidence_id: ev-cycle3-stage4-findings
  kind: record_content
  reference: reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/review_findings.yaml
  locator: findings[0..2]
  accessed_at: '2026-10-24T03:40:00Z'
  support: supports
  summary: Frozen Cycle 3 Stage 4 review findings ledger defining cmmmech-cycle3-stage4-finding-0001,
    cmmmech-cycle3-stage4-finding-0002, and cmmmech-cycle3-stage4-finding-0003 across
    the 3 target records.
  snapshot_sha256: 7ca7ad9bbdef88ee30cb7bd67e4a4245e8b15f5bbd1433af6c7555f2a9b2d9f8
- evidence_id: ev-schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: classes.MaterialRecord, classes.ProteinExample, classes.Source
  accessed_at: '2026-10-24T03:40:00Z'
  support: supports
  summary: Canonical LinkML schema defining MaterialRecord, ProteinExample, and Source.
  snapshot_sha256: 8141cecb3e1abf908515fd86c21da808c6b2d611a83eaaea20da80e2018ed781
assessments:
- assessment_id: assess-grp1-bixbyite-gene-symbol
  area: consistency
  topic: Mesau_02205 gene_symbol parity on UniProtKB:A0A0K2YWP2 in bixbyite-mn.yaml
    (#830)
  outcome: supported
  summary: 'Both mechanisms[0].protein_examples[0] and causal_graphs[0].nodes[0].protein_examples[0]
    for UniProtKB:A0A0K2YWP2 in data/records/bixbyite-mn.yaml now include gene_symbol:
    Mesau_02205, achieving 100% parity with parent node tg1_acidic_mn_oxidase_factor
    and paired homolog UniProtKB:L0KKS2.'
  target_ids:
  - cmmmech:bixbyite-mn
  evidence_ids:
  - ev-uniprot-a0a0k2ywp2
  - ev-cycle3-stage4-findings
  - ev-schema
  metrics:
  - name: bixbyite_protein_example_gene_symbol_parity
    value: 1.0
    unit: fraction
    definition: 'Fraction of protein_examples in bixbyite-mn.yaml carrying gene_symbol:
      Mesau_02205'
    denominator: 2
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp2-olivine-group-source-id
  area: consistency
  topic: Canonical ima_compendium_2019 source key in olivine-group.yaml (#831)
  outcome: supported
  summary: 'data/records/olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature
    Compendium under canonical id: ima_compendium_2019, matching all 4 sibling mineral_group
    records citing that compilation (biotite, chlorite, illite, potassium-feldspar).'
  target_ids:
  - cmmmech:olivine-group
  evidence_ids:
  - ev-ima-compendium-2019
  - ev-cycle3-stage4-findings
  metrics:
  - name: mineral_group_ima_compendium_key_uniformity
    value: 1.0
    unit: fraction
    definition: Fraction of mineral_group records citing the 2019 IMA Compendium under
      canonical source id ima_compendium_2019
    denominator: 5
    minimum: 0.0
    maximum: 1.0
- assessment_id: assess-grp3-humboldtine-source-id
  area: consistency
  topic: Canonical genbank_ch407 source key in humboldtine.yaml (#832)
  outcome: supported
  summary: 'data/records/humboldtine.yaml now keys GenBank ITS accession KF768341.1
    for Aspergillus niger strain Ch 4/07 under canonical sources[4].id: genbank_ch407
    and mechanisms[0].evidence[3].source_ref: genbank_ch407, matching all 5 sibling
    Ch 4/07 mineral records (hopeite, katsarosite, moolooite, wheatleyite, whewellite).'
  target_ids:
  - cmmmech:humboldtine
  evidence_ids:
  - ev-genbank-kf768341
  - ev-cycle3-stage4-findings
  metrics:
  - name: ch407_cohort_genbank_source_key_uniformity
    value: 1.0
    unit: fraction
    definition: Fraction of Aspergillus niger Ch 4/07 mineral records citing GenBank
      KF768341.1 under canonical source id genbank_ch407
    denominator: 6
    minimum: 0.0
    maximum: 1.0
findings:
- finding_id: cmmmech-cycle3-stage4-finding-0001
  issue_key: cmmmech.bixbyite-mn.amplicon-protein-example-missing-gene-symbol
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: 'bixbyite-mn.yaml protein_examples[0] (UniProtKB:A0A0K2YWP2) now carries
    gene_symbol: Mesau_02205'
  description: 'Added gene_symbol: Mesau_02205 to mechanisms[0].protein_examples[0]
    and causal_graphs[0].nodes[0].protein_examples[0] for UniProtKB:A0A0K2YWP2 (A0A0K2YWP2_9HYPH)
    in data/records/bixbyite-mn.yaml with an append-only EDIT history sidecar.'
  target_ids:
  - cmmmech:bixbyite-mn
  field_paths:
  - mechanisms[0].protein_examples[0].gene_symbol
  - causal_graphs[0].nodes[0].protein_examples[0].gene_symbol
  - curation_history
  - history_refs
  evidence_ids:
  - ev-uniprot-a0a0k2ywp2
  - ev-cycle3-stage4-findings
  - ev-schema
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/bixbyite-mn.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #830 (group GRP-C3S5-001) by adding
    gene_symbol: Mesau_02205 to both mechanism and causal-graph node protein_examples[0]
    in data/records/bixbyite-mn.yaml with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261024T024506Z-cycle3-stage4-causal-graphs-cohort-review
    finding_id: cmmmech-cycle3-stage4-finding-0001
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/830
- finding_id: cmmmech-cycle3-stage4-finding-0002
  issue_key: cmmmech.mineral_group.noncanonical-ima-compendium-source-id
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: olivine-group.yaml now keys the 2019 IMA-CNMNC Nomenclature Compendium under
    canonical ima_compendium_2019
  description: Normalized sources[0].id from ima_compendium to canonical ima_compendium_2019
    in data/records/olivine-group.yaml with an append-only EDIT history sidecar.
  target_ids:
  - cmmmech:olivine-group
  field_paths:
  - sources[0].id
  - curation_history
  - history_refs
  evidence_ids:
  - ev-ima-compendium-2019
  - ev-cycle3-stage4-findings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/olivine-group.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #831 (group GRP-C3S5-002) by normalizing
    sources[0].id to ima_compendium_2019 in data/records/olivine-group.yaml with an
    append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261024T024502Z-cycle3-stage4-mineral-group-cohort-review
    finding_id: cmmmech-cycle3-stage4-finding-0002
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/831
- finding_id: cmmmech-cycle3-stage4-finding-0003
  issue_key: cmmmech.mineral.noncanonical-ch407-its-source-id
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: humboldtine.yaml now keys GenBank ITS accession KF768341.1 under canonical
    genbank_ch407
  description: Normalized sources[4].id and mechanisms[0].evidence[3].source_ref from
    genbank_niger to canonical genbank_ch407 in data/records/humboldtine.yaml with
    an append-only EDIT history sidecar.
  target_ids:
  - cmmmech:humboldtine
  field_paths:
  - sources[4].id
  - mechanisms[0].evidence[3].source_ref
  - curation_history
  - history_refs
  evidence_ids:
  - ev-genbank-kf768341
  - ev-cycle3-stage4-findings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/humboldtine.yaml
    role: maintained_record
  disposition_reason: 'Resolved under GitHub issue #832 (group GRP-C3S5-003) by normalizing
    sources[4].id and mechanisms[0].evidence[3].source_ref to genbank_ch407 in data/records/humboldtine.yaml
    with an append-only EDIT history sidecar.'
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261024T024507Z-humboldtine-cycle3-stage4-record-review
    finding_id: cmmmech-cycle3-stage4-finding-0003
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/832
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:bixbyite-mn
  - cmmmech:humboldtine
  - cmmmech:olivine-group
  evidence_ids:
  - ev-uniprot-a0a0k2ywp2
  - ev-ima-compendium-2019
  - ev-genbank-kf768341
  - ev-cycle3-stage4-findings
  - ev-schema
  rationale: 'All 3 remediated records represent distinct mineral species (2 records:
    bixbyite-mn, humboldtine) or mineral groups (1 record: olivine-group) with disjoint
    identifiers and provenance; cohort boundaries from Cycle 3 Stage 4 are retained
    unchanged.'
limitations:
- This verification review is scoped to the 3 records remediated in Cycle 3 Stage
  5; the remaining 643 records were verified with 0 open findings in the immutable
  Cycle 3 Stage 4 review bundles.
```
