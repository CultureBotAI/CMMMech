# Independent scientific review of ground waste tire rubber and its qualified transformation evidence

- Review: 20261011T171324Z-ground-waste-tire-rubber-round28-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T17:06:45Z
- Finished UTC: 2026-10-11T17:13:24.965406Z
- Reviewer: Codex /root/round27_eaf_slag (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record preserves conditional laboratory rubber transformation and the chemical pretreatment stage, without claiming demonstrated microbial zinc extraction, specific enzyme causality, complete mineralization or industrial recovery. All retained numerical bases and source contradictions were checked. No corrective record finding was identified.

## Scope And Provenance

Entire new record, both microbial and chemical mechanism blocks, and its linked CREATE history.

Selection: Assigned independent review of the newly curated ground waste tire rubber record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ground-waste-tire-rubber | data/records/ground-waste-tire-rubber.yaml | maintained | Ground waste tire rubber |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:ground-waste-tire-rubber | Executed by this reviewer; terminal exit 0 and log reports 1 record checked, 0 failed. |
| Coordinator final batch checks | passed | True | cmmmech:ground-waste-tire-rubber | Actual coordinator receipt and log independently read and SHA-256 verified: 308 passed, 3 skipped; 174 records and 198 histories valid. |
| Coordinator final nonempty record validation | passed | True | cmmmech:ground-waste-tire-rubber | Actual coordinator receipt and log independently read and SHA-256 verified: 174 records checked, 0 failed. |
| Coordinator trusted-base history validation | passed | True | cmmmech:ground-waste-tire-rubber | Actual coordinator receipt and log independently read and SHA-256 verified: 198 history records checked, 0 errors, against the retained merged-main base. |

## Scientific And Domain Assessments

### Resource and taxon identities remain distinct

identity: supported. Targets: cmmmech:ground-waste-tire-rubber.

Ground used-tire rubber is correctly represented as a heterogeneous secondary resource, without inheriting criticality or another material identity.

### Biological incubation and chemical preparation have separate scopes

evidence: supported. Targets: cmmmech:ground-waste-tire-rubber.

The record correctly preserves each stage and the controls that constrain its causal interpretation.

### Partial phenotype without pathway or complete mineralization claims

evidence: supported. Targets: cmmmech:ground-waste-tire-rubber.

Swelling, morphology, staining and compositional changes support the qualified culture-associated transformation account. Model-derived network properties and tentative LC-MS/ABTS results are not promoted to specific enzyme causality.

### No demonstrated microbial zinc extraction; concentration bases preserved

evidence: supported. Targets: cmmmech:ground-waste-tire-rubber.

The record accurately retains increased digest-residue Zn fractions after bacterial treatment and the chemically attributed DES decrease, without inferring exact absolute Zn conservation or metal recovery.

### Primary inconsistencies retained without silent repair

evidence: supported. Targets: cmmmech:ground-waste-tire-rubber.

The record accurately preserves Figure 1 count/OD conflicts, Figure 8 char ranking, Figure 10 protein discrepancies, TGA hold-time inconsistency and tentative LC-MS formula/adduct problem. These are limitations of the source, not new precise mechanism measurements.

The SI C20H32O2 sodium-adduct entry at m/z 307 conflicts with a nominal mass near 327. Rounded SI gross-loss subtraction gives 12.54 percentage points while prose reports 12.53. No correction of the primary numbers or unsupported general solvent-nontoxicity claim is imported.

### Exact frozen inputs and truthful CREATE accounting

provenance: supported. Targets: cmmmech:ground-waste-tire-rubber.

Canonical inspect, inline event and linked CREATE session describe actual new curation at the retained merged-main base. The review does not create an additional history event or promote source certainty.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/ground-waste-tire-rubber.yaml; Entire frozen YAML and linked CREATE history | supports | The target retains the process-defined resource, separate chemical preparation and conditional biological phenotype. Canonical inspect captures the merged-main base and exact uncommitted input bytes. |
| primary | https://doi.org/10.1039/d6ra01664b; Complete Europe PMC original XML: all Methods 2.1–2.8, Results 3.1–3.13, Tables 1–4, conclusions, references and front/back matter | supports | Identity, preparation, culture conditions and assay scope were independently checked against the full primary. Its DOI/PMCID and media references agree with the retained package. |
| graphics | https://doi.org/10.1039/d6ra01664b; All eleven original main JPEG figures independently viewed, including every multi-panel image and Figure 8 embedded table | supports | The original pixels substantiate the qualitative and quantitative observations and the retained graphic/prose conflicts. Files are d6ra01664b-f1.jpg through -f11.jpg in /private/tmp/cmm-round28-tire-research/raw/des2026-supplementary/. |
| supplement | https://doi.org/10.1039/d6ra01664b; Original four-page RA-016-D6RA01664B-s001.pdf: Tables S1–S3 and Figures S1–S2; all rendered pages and both extracted embedded JPEGs inspected | supports | The original supplement establishes gross gravimetric values and tentative LC-MS reporting. Page 3 has overlapping figure layout, so both original embedded images were inspected separately; page 4 is blank. Table S2 correctly says rhodochrous; no organism-name conflict is present there. |
| limits | https://doi.org/10.1039/d6ra01664b; Methods 2.6–2.8; Results 3.4–3.13; Tables 1–4 and S1–S3; Figures 1, 7–11 and S1–S2 | context_only | Gross/control-adjusted mass loss, residue fractions and model-derived network properties have distinct denominators. No treatment-matched DES-pretreated abiotic 28-day gravimetric/Schiff arm, aqueous Zn balance, isolated product or direct pathway experiment resolves the stated attribution limits. |
| dsm | https://www.dsmz.de/collection/catalogue/details/culture/DSM-103064; Live collection page independently opened; retained full HTML also read | supports | DSM 103064 maps to Rhodococcus rhodochrous, strain designation RPK 1. This verifies accession-name provenance without authenticating the experimental stock. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1829&amp;mode=Info; Live current-name and rank fields independently opened | supports | NCBI taxon 1829 identifies Rhodococcus rhodochrous at species rank; the record correctly separates this from DSM strain identity. |
| metadata | https://api.crossref.org/works/10.1039%2Fd6ra01664b; Retained full Crossref JSON compared with original XML and live PMC/PubMed metadata | supports | Title and DOI agree. Crossref year-only publication metadata is not substituted for the original 18 May 2026 article date. Inspected relation is empty and no update-to/updated-by is present; this does not establish universal correction absence. |
| search | https://doi.org/10.1039/d6ra01664b; Fresh web first-result sets; independent local dedup-paths.txt and dedup-broad-paths.txt under /private/tmp/cmm-round28-tire-independent-review/ | context_only | No applicable correction was identified in the returned sets. A new adjacent Gordonia tire-degradation lead, DOI 10.1039/d6ra04972a, was surfaced but not primary-assessed or accepted. Local maintained matches are the new target and an unrelated rubber-stopper mention in the nodule record. |
| gates | /private/tmp/cmm-round28-final-terminal.json; Actual coordinator terminal receipt and all three named logs; independent named-record validation log | supports | All required checks reached terminal exit 0. Log checksums and every canonical target/context input were independently verified before saving. |

## Limits And Additional Notes

- One laboratory study supports a narrowly qualified transformation phenotype; no industrial deployment or recovered metal product is established.
- Broth carryover, incompletely documented gravimetric preparation and the missing DES-pretreated abiotic incubation comparator limit microbial attribution and synergy claims.
- Weight-fraction changes, model-derived crosslink values and control-subtracted mass losses have different denominators; no closed Zn/carbon/sulfur inventory is available.
- Primary numerical/graphic conflicts and tentative LC-MS assignments remain unresolved. No specific enzyme pathway or complete mineralization is established.
- Full original XML/tables and figure assets were inspected; the publisher main PDF was unavailable. Shared curator acquisition/rendering was independently read, not independently repeated.
- Correction and counterevidence searches cover only documented returned sets; adjacent source leads were not accepted as corroboration or refutation.
- Source preparation preceded canonical inspect; frozen maintained claims were assessed only after their exact hashes were captured.
- A mistaken source-spelling-conflict claim in an outside-Git handoff was identified and corrected by the curator before target freeze. The frozen record correctly says the main and SI organism names agree; no saved predecessor record finding existed to resolve.
- No corrective finding was identified within the frozen-record scope. Structural validation does not establish scientific truth.
- Final batch receipts were inspected after all three round28 records froze. This target and its canonical context inputs remained byte-identical through the save preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T171324Z-ground-waste-tire-rubber-round28-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of ground waste tire rubber and its qualified
  transformation evidence
started_at: '2026-10-11T17:06:45Z'
finished_at: '2026-10-11T17:13:24.965406Z'
reviewer:
  identity: Codex /root/round27_eaf_slag
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The record and CREATE history were authored by /root/round27_packaging.
    This reviewer authored neither and made no maintained-record or history edits.
    Assessment independently read the full primary XML/body/tables, all eleven original
    figures, complete supplementary PDF and embedded images, live identifier pages
    and fresh bounded searches. Acquisition/rendering artifacts were shared; curator
    prose was not the sole evidence. The reviewer identified a mistaken source-typo
    statement during preparation, which the curator removed before freezing and before
    canonical inspect.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record preserves conditional laboratory rubber transformation
  and the chemical pretreatment stage, without claiming demonstrated microbial zinc
  extraction, specific enzyme causality, complete mineralization or industrial recovery.
  All retained numerical bases and source contradictions were checked. No corrective
  record finding was identified.
source:
  git_revision: 9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3
  state: working_tree
  inputs:
  - path: data/records/ground-waste-tire-rubber.yaml
    sha256: 10ca9ca7bd494f12919f5a1d1a4220fee2685560b7dbc1222881c973564e1dd2
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/ground-waste-tire-rubber/2026-10-11T170536Z-codex-b238c9.yaml
    sha256: 091cbd953d648948997165804163e6630608c9a902880269b7bd78efbad7c926
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire new record, both microbial and chemical mechanism blocks, and
    its linked CREATE history.
  selection: Assigned independent review of the newly curated ground waste tire rubber
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ground-waste-tire-rubber
  exclusions:
  - target: Publisher main PDF
    reason: Not acquired; complete original XML/tables plus original figure files
      were used.
  - target: Other tire-soil, tire-ash, pyrolysis and rubber-degradation studies
    reason: Not accepted as mechanism evidence or independent replication for this
      record.
targets:
- target_id: cmmmech:ground-waste-tire-rubber
  path: data/records/ground-waste-tire-rubber.yaml
  label: Ground waste tire rubber
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ground-waste-tire-rubber.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: uv run --locked cmmmech validate data/records/ground-waste-tire-rubber.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Executed by this reviewer; terminal exit 0 and log reports 1 record checked,
    0 failed.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
- check_id: batch
  name: Coordinator final batch checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual coordinator receipt and log independently read and SHA-256 verified:
    308 passed, 3 skipped; 174 records and 198 histories valid.'
  target_ids:
  - cmmmech:ground-waste-tire-rubber
- check_id: nonempty
  name: Coordinator final nonempty record validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual coordinator receipt and log independently read and SHA-256 verified:
    174 records checked, 0 failed.'
  target_ids:
  - cmmmech:ground-waste-tire-rubber
- check_id: history
  name: Coordinator trusted-base history validation
  command: uv run --locked cmmmech validate-history --base 9f37042ef36b8f20ebf44f8228f6a4b5d27e00c3
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual coordinator receipt and log independently read and SHA-256 verified:
    198 history records checked, 0 errors, against the retained merged-main base.'
  target_ids:
  - cmmmech:ground-waste-tire-rubber
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/ground-waste-tire-rubber.yaml
  locator: Entire frozen YAML and linked CREATE history
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: The target retains the process-defined resource, separate chemical preparation
    and conditional biological phenotype. Canonical inspect captures the merged-main
    base and exact uncommitted input bytes.
  snapshot_sha256: 10ca9ca7bd494f12919f5a1d1a4220fee2685560b7dbc1222881c973564e1dd2
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1039/d6ra01664b
  locator: 'Complete Europe PMC original XML: all Methods 2.1–2.8, Results 3.1–3.13,
    Tables 1–4, conclusions, references and front/back matter'
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: Identity, preparation, culture conditions and assay scope were independently
    checked against the full primary. Its DOI/PMCID and media references agree with
    the retained package.
  snapshot_sha256: 4773650b133d943158045ccf396cda5caa540834eeec031057f90b25f7c469e2
- evidence_id: graphics
  kind: primary_source
  reference: https://doi.org/10.1039/d6ra01664b
  locator: All eleven original main JPEG figures independently viewed, including every
    multi-panel image and Figure 8 embedded table
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: The original pixels substantiate the qualitative and quantitative observations
    and the retained graphic/prose conflicts. Files are d6ra01664b-f1.jpg through
    -f11.jpg in /private/tmp/cmm-round28-tire-research/raw/des2026-supplementary/.
- evidence_id: supplement
  kind: primary_source
  reference: https://doi.org/10.1039/d6ra01664b
  locator: 'Original four-page RA-016-D6RA01664B-s001.pdf: Tables S1–S3 and Figures
    S1–S2; all rendered pages and both extracted embedded JPEGs inspected'
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: The original supplement establishes gross gravimetric values and tentative
    LC-MS reporting. Page 3 has overlapping figure layout, so both original embedded
    images were inspected separately; page 4 is blank. Table S2 correctly says rhodochrous;
    no organism-name conflict is present there.
  snapshot_sha256: 4fa49a807edcadd3d5d891962cd5ddffb90e8d0afe580b331171e40e7726de20
- evidence_id: limits
  kind: primary_source
  reference: https://doi.org/10.1039/d6ra01664b
  locator: Methods 2.6–2.8; Results 3.4–3.13; Tables 1–4 and S1–S3; Figures 1, 7–11
    and S1–S2
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: context_only
  summary: Gross/control-adjusted mass loss, residue fractions and model-derived network
    properties have distinct denominators. No treatment-matched DES-pretreated abiotic
    28-day gravimetric/Schiff arm, aqueous Zn balance, isolated product or direct
    pathway experiment resolves the stated attribution limits.
  snapshot_sha256: 4773650b133d943158045ccf396cda5caa540834eeec031057f90b25f7c469e2
- evidence_id: dsm
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-103064
  locator: Live collection page independently opened; retained full HTML also read
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: DSM 103064 maps to Rhodococcus rhodochrous, strain designation RPK 1. This
    verifies accession-name provenance without authenticating the experimental stock.
  snapshot_sha256: ba5941dde7ba39af82d881a059c58046adcdc065c209c936fefc46e4854a85d5
- evidence_id: taxon
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1829&mode=Info
  locator: Live current-name and rank fields independently opened
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: NCBI taxon 1829 identifies Rhodococcus rhodochrous at species rank; the
    record correctly separates this from DSM strain identity.
- evidence_id: metadata
  kind: primary_source
  reference: https://api.crossref.org/works/10.1039%2Fd6ra01664b
  locator: Retained full Crossref JSON compared with original XML and live PMC/PubMed
    metadata
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: supports
  summary: Title and DOI agree. Crossref year-only publication metadata is not substituted
    for the original 18 May 2026 article date. Inspected relation is empty and no
    update-to/updated-by is present; this does not establish universal correction
    absence.
  snapshot_sha256: 70649db1e90c158d231496b8fd91c5605cf82e0f75b3107f6354e48c07cdd2b2
- evidence_id: search
  kind: search
  reference: https://doi.org/10.1039/d6ra01664b
  locator: Fresh web first-result sets; independent local dedup-paths.txt and dedup-broad-paths.txt
    under /private/tmp/cmm-round28-tire-independent-review/
  accessed_at: '2026-10-11T17:08:31.651335Z'
  support: context_only
  summary: No applicable correction was identified in the returned sets. A new adjacent
    Gordonia tire-degradation lead, DOI 10.1039/d6ra04972a, was surfaced but not primary-assessed
    or accepted. Local maintained matches are the new target and an unrelated rubber-stopper
    mention in the nodule record.
  search_scope: 'Queries: exact DOI plus correction OR retraction OR corrigendum;
    "RPK1" "tyre rubber" "zinc" degradation; "Deep eutectic solvent-assisted bacterial
    devulcanization" criticism correction. First returned sets, no pagination or filters.
    rg --no-ignore --hidden --follow searched tire/tyre/rubber and selected DOI terms
    in current and original checkouts data/history/research/reviews plus round28 tire,
    round27 packaging/EAF and round26 root raw directories. Ignored and hidden files
    were included; unrelated directories and all literature were not exhaustively
    searched.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round28-final-terminal.json
  locator: Actual coordinator terminal receipt and all three named logs; independent
    named-record validation log
  accessed_at: '2026-10-11T17:13:24.965406Z'
  support: supports
  summary: All required checks reached terminal exit 0. Log checksums and every canonical
    target/context input were independently verified before saving.
  snapshot_sha256: 59c24f18641d0787b153c9dccb7174419193fe718d81c903d07e735904edafa0
assessments:
- assessment_id: identity
  area: identity
  topic: Resource and taxon identities remain distinct
  outcome: supported
  summary: Ground used-tire rubber is correctly represented as a heterogeneous secondary
    resource, without inheriting criticality or another material identity.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - record
  - primary
  - dsm
  - taxon
  - search
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: 400–600 micrometre particles from an unnamed waste-tire recycling
      facility; ash, char, manufacturing waste and glove rubber excluded.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: No authority, jurisdiction, list or edition is assigned from constituent
      zinc or rubber.
    evidence_ids:
    - record
  - name: organism_and_biomass
    value: Growing R. rhodochrous RPK1; reported DSM 103064; species NCBITaxon:1829
    definition: Collection mapping verifies label/accession scope, not experimental
      stock authentication.
    evidence_ids:
    - primary
    - dsm
    - taxon
- assessment_id: conditions
  area: evidence
  topic: Biological incubation and chemical preparation have separate scopes
  outcome: supported
  summary: The record correctly preserves each stage and the controls that constrain
    its causal interpretation.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - primary
  - graphics
  - supplement
  - limits
  dimensions:
  - name: chemical_pretreatment
    value: Choline chloride/urea 1:2; rubber:DES 1:40; 24 h swelling, 2 h 37 kHz sonication,
      180 degrees C for 45 min
    definition: Ethanol washing/drying precede and follow this nonmicrobial preparation;
      separate TGA hold-time conflict retained.
    evidence_ids:
    - primary
    - graphics
  - name: culture_conditions
    value: 1% w/v GTR in 100 mL MSM, 250 mL flasks, 10% v/v nutrient-broth-grown inoculum,
      pH 7.0 +/- 0.05, 30 degrees C, 120 rpm, 28 days
    definition: No inoculum washing is reported; broth carryover limits sole-carbon
      attribution.
    evidence_ids:
    - primary
  - name: controls
    value: Untreated GTR without bacteria; bacteria without GTR; DES-only compositional/swelling
      data
    definition: No DES-pretreated abiotic 28-day gravimetry/Schiff arm; cleanup and
      independent flask replication remain incompletely specified.
    evidence_ids:
    - primary
    - supplement
- assessment_id: transformation
  area: evidence
  topic: Partial phenotype without pathway or complete mineralization claims
  outcome: supported
  summary: Swelling, morphology, staining and compositional changes support the qualified
    culture-associated transformation account. Model-derived network properties and
    tentative LC-MS/ABTS results are not promoted to specific enzyme causality.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - primary
  - graphics
  - supplement
  - limits
  dimensions:
  - name: crosslink_metric
    value: 9.61, 8.09, 7.03 and 5.44 × 10^-5 mol/cm3; reported mean +/- SD, n=3
    definition: Untreated, bacterial, DES and combined groups respectively; swelling-model
      estimates, not direct counts of cleaved bonds.
    evidence_ids:
    - primary
  - name: gravimetric_metric
    value: Gross losses 3.30 +/- 2.36%, 4.93 +/- 1.15% and 15.84 +/- 8.78%
    definition: Untreated abiotic, bacteria/GTR and bacteria/DES-GTR from initial
      1.00 g; source n and plus/minus statistic undefined. Prose control subtraction
      is not a DES-matched biological increment or product yield.
    evidence_ids:
    - graphics
    - supplement
  - name: deployment
    value: Laboratory flask study
    definition: No isolated zinc product, validated industrial rubber recovery, lifecycle
      benefit or closed material balance.
    evidence_ids:
    - primary
    - limits
- assessment_id: zinc
  area: evidence
  topic: No demonstrated microbial zinc extraction; concentration bases preserved
  outcome: supported
  summary: The record accurately retains increased digest-residue Zn fractions after
    bacterial treatment and the chemically attributed DES decrease, without inferring
    exact absolute Zn conservation or metal recovery.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - primary
  - limits
  dimensions:
  - name: digest_zinc
    value: 1.94 +/- 0.06, 2.25 +/- 0.10, 1.30 +/- 0.17 and 1.73 +/- 0.11 wt%
    definition: Untreated, bacterial, DES and combined solid residues; ICP digestion
      method retained; replicate count/statistic unspecified.
    evidence_ids:
    - primary
  - name: surface_zinc
    value: 3.36, 2.06, 0.80 and 1.06 wt%
    definition: Area-based EDS means of two measurements, not interchangeable with
      digest ICP or whole-feed extraction yields.
    evidence_ids:
    - primary
- assessment_id: contradictions
  area: evidence
  topic: Primary inconsistencies retained without silent repair
  outcome: supported
  summary: The record accurately preserves Figure 1 count/OD conflicts, Figure 8 char
    ranking, Figure 10 protein discrepancies, TGA hold-time inconsistency and tentative
    LC-MS formula/adduct problem. These are limitations of the source, not new precise
    mechanism measurements.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - record
  - graphics
  - supplement
  - limits
  dimensions: []
  details: The SI C20H32O2 sodium-adduct entry at m/z 307 conflicts with a nominal
    mass near 327. Rounded SI gross-loss subtraction gives 12.54 percentage points
    while prose reports 12.53. No correction of the primary numbers or unsupported
    general solvent-nontoxicity claim is imported.
- assessment_id: provenance
  area: provenance
  topic: Exact frozen inputs and truthful CREATE accounting
  outcome: supported
  summary: Canonical inspect, inline event and linked CREATE session describe actual
    new curation at the retained merged-main base. The review does not create an additional
    history event or promote source certainty.
  target_ids:
  - cmmmech:ground-waste-tire-rubber
  evidence_ids:
  - record
  - metadata
  dimensions: []
findings: []
actions: []
limitations:
- One laboratory study supports a narrowly qualified transformation phenotype; no
  industrial deployment or recovered metal product is established.
- Broth carryover, incompletely documented gravimetric preparation and the missing
  DES-pretreated abiotic incubation comparator limit microbial attribution and synergy
  claims.
- Weight-fraction changes, model-derived crosslink values and control-subtracted mass
  losses have different denominators; no closed Zn/carbon/sulfur inventory is available.
- Primary numerical/graphic conflicts and tentative LC-MS assignments remain unresolved.
  No specific enzyme pathway or complete mineralization is established.
- Full original XML/tables and figure assets were inspected; the publisher main PDF
  was unavailable. Shared curator acquisition/rendering was independently read, not
  independently repeated.
- Correction and counterevidence searches cover only documented returned sets; adjacent
  source leads were not accepted as corroboration or refutation.
notes:
- Source preparation preceded canonical inspect; frozen maintained claims were assessed
  only after their exact hashes were captured.
- A mistaken source-spelling-conflict claim in an outside-Git handoff was identified
  and corrected by the curator before target freeze. The frozen record correctly says
  the main and SI organism names agree; no saved predecessor record finding existed
  to resolve.
- No corrective finding was identified within the frozen-record scope. Structural
  validation does not establish scientific truth.
- Final batch receipts were inspected after all three round28 records froze. This
  target and its canonical context inputs remained byte-identical through the save
  preparation.
tags:
- round28
- independent
- scientific-review
- secondary-resource
```
