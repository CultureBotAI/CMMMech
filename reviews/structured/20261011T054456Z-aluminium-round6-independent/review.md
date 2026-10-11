# Aluminium independent primary-evidence review

- Review: 20261011T054456Z-aluminium-round6-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T05:41:18Z
- Finished UTC: 2026-10-11T05:44:56Z
- Reviewer: /root/cmm6_indium (Codex) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record supports a narrowly bounded laboratory G-10 red-mud leaching result. Element and commodity scope, analytical basis, no-fungus controls and non-equivalent synthetic-acid comparison are accurately retained. No corrective findings were identified within the declared scope.

## Scope And Provenance

Complete new aluminium record and linked history, assessed against the primary experiment and authority identifiers.

Selection: Assigned round6 elemental aluminium record, all asserted claims; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d09a5611767d94fd196393b31d44cb8cf6657f7f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:aluminium | data/records/aluminium.yaml | maintained | Aluminium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named aluminium validation | passed | True | cmmmech:aluminium | Checked 1 record; 0 failed. |
| Canonical sidecars and append-only history | passed | True | cmmmech:aluminium | Checked 45 history records; 0 errors. |
| Complete frozen four-record batch gate | passed | True | cmmmech:aluminium | Root ran final batch; reviewer inspected /private/tmp/cmm-round6-check.log. Terminal exit 0: 307 passed, 3 skipped in 46.67 s; lint passed; 36 records, 0 failed; 46 histories, 0 errors. |
| Required nonempty corpus validation | passed | True | cmmmech:aluminium | Parent terminal receipt: 36 records; 0 failed; exit 0 after all four records frozen. |
| Final complete trusted-base history validation | passed | True | cmmmech:aluminium | Parent terminal receipt: 46 history records; 0 errors; exit 0 after all four records frozen. Earlier reviewer-owned history check covered 45 sessions before the final batch addition. |

## Scientific And Domain Assessments

### Element and species/strain grounding

identity: supported. Targets: cmmmech:aluminium.

Elemental Al and species-level Aspergillus label are correctly grounded; the record does not equate element with waste feed or species identifier with strain authentication.

### Dated commodity designation

scope: supported. Targets: cmmmech:aluminium.

Named US 2025 Aluminum designation is represented with jurisdiction, edition and authority and not inherited by all Al-bearing materials.

### Assay and measured endpoint

evidence: supported. Targets: cmmmech:aluminium.

Primary experiment supports fungal-associated mobilization into filtrate under defined laboratory conditions and the stated approximately 141 mg/L endpoint.

### Null control and mechanistic limits

consistency: supported. Targets: cmmmech:aluminium.

Undetected/no-fungus Al and non-equivalent synthetic-acid comparison are retained without a numerical AlLOD or a proven proton-pump/enzyme mechanism.

### Acquisition and actual CREATE history

provenance: supported. Targets: cmmmech:aluminium.

Fresh local authority and primary payload hashes match receipt; primary reproduction and DOI identify one experiment. History target and real actor metadata agree with new record creation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/aluminium.yaml; Complete target and linked CREATE sidecar | supports | Inspection captured the exact working-tree record hash with real separate inline and canonical CREATE metadata. |
| primary | https://www.vut.cz/uredni-deska/habilitace?action=priloha&amp;priloha=226417; Attachment E, PDF 80-85 / journal 154-159; Sections 2.1-2.5, 3.1, 3.3-3.5; Table 1; Figures 3, 7-8 | supports | Complete reproduced primary paper independently read from retained valid PDF; Figures 3, 5-9 rendered and visually checked. Supports G-10 preparation, 0.2 g red mud/50 mL assay, ICP-OES filtrate result and chemical control, with no isolated-product demonstration. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:28984; Independently inspected freshly acquired authority HTML; title, formula and charge | supports | CHEBI:28984 is aluminium atom, formula Al and net charge 0; element distinct from salts, red mud, alumina and bauxite. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5061&amp;retmode=xml; Fresh retained XML ScientificName, Rank, TaxId | supports | NCBI 5061 resolves to Aspergillus niger at species rank. Primary paper assigns G-10 by morphology and 612-bp ITS/99% similarity, rather than independently authenticating this strain. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Page 50496 Aluminum row, final 2025 list; live page and retained HTML | supports | Named aluminum commodity is explicitly in the US 2025 list; record date and elemental mapping preserve scope. |
| search | 2026-10-11 independent bounded review searches; Exact DOI correction/retraction/erratum; title/control/G-10 search; local exact root/ID/DOI | context_only | No relevant correction notice found in returned first result sets; local target and current dossier are the only exact record/DOI matches. This is not an exhaustive literature or machine-wide claim. |
| batch-log | /private/tmp/cmm-round6-check.log; Full final log plus parent terminal exit-code and separate validator receipts | supports | Reviewer inspected final gate log; all required batch checks passed after record freeze. Scientific support was assessed independently of these structural checks. |

## Limits And Additional Notes

- ICP-OES of 0.45-micrometre filtrate reports filter-passing Al; no free-ion or isolated-product assay.
- No numerical aluminium detection limit supplied for no-fungus controls.
- Species assignment based on short ITS similarity is not independent strain authentication.
- Synthetic-acid experiments differ in medium and duration; proton and ligand mechanisms are not isolated.
- Al-host mineral phases unresolved; higher-loading figure40/50 g/L inconsistency excluded from imported low-loading assay.
- Authority payloads acquired by curator were independently read/rehashed; primary PDF is an official thesis reproduction of the same paper, not independent replication.
- Bounded first-page correction/counterevidence and hidden/ignored local searches are not exhaustive.
- Structured-review persistence and later publication/squash gates are separate from these completed scientific and batch checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T054456Z-aluminium-round6-independent
kind: record
repository: CultureBotAI/CMMMech
title: Aluminium independent primary-evidence review
started_at: '2026-10-11T05:41:18Z'
finished_at: '2026-10-11T05:44:56Z'
reviewer:
  identity: /root/cmm6_indium (Codex)
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from aluminium curator; did not write target
    or history. Independently read all six primary-paper pages and rendered figures,
    inspected authority payloads, ran named/history checks and searched corrections
    before assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record supports a narrowly bounded laboratory G-10 red-mud leaching result.
  Element and commodity scope, analytical basis, no-fungus controls and non-equivalent
  synthetic-acid comparison are accurately retained. No corrective findings were identified
  within the declared scope.
source:
  git_revision: d09a5611767d94fd196393b31d44cb8cf6657f7f
  state: working_tree
  inputs:
  - path: data/records/aluminium.yaml
    sha256: a749a1f2d5283f0839bd99ef7be43bde6d9e43d576efd488e6db1505369ed6f4
    role: target
  - path: history/records/aluminium/2026-10-11T053805Z-codex-7b51f9.yaml
    sha256: d58c4568f27e36e17adde9c0e5a8ee03a5ad52148bdf9a8568ee5eb4116c61dd
    role: context
  - path: research/ingests/round6-aluminium-20261011.json
    sha256: 491418b3391d8cd0a17e56f3d2962b80f7ffb9bb2278989157df2a55c6253bad
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:aluminium
  path: data/records/aluminium.yaml
  label: Aluminium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/aluminium.yaml
    role: maintained scientific record
scope:
  description: Complete new aluminium record and linked history, assessed against
    the primary experiment and authority identifiers.
  selection: Assigned round6 elemental aluminium record, all asserted claims; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:aluminium
  exclusions:
  - target: Other strains, higher red-mud loadings and industrial recovery
    reason: Not asserted in the target; higher-loading figures contain a 40 versus
      50 g/L inconsistency and were not imported.
checks:
- check_id: named-record
  name: Named aluminium validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/aluminium.yaml
  status: passed
  required: true
  summary: Checked 1 record; 0 failed.
  target_ids:
  - cmmmech:aluminium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Canonical sidecars and append-only history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base d09a5611767d94fd196393b31d44cb8cf6657f7f
  status: passed
  required: true
  summary: Checked 45 history records; 0 errors.
  target_ids:
  - cmmmech:aluminium
  exit_code: 0
  expected_exit_code: 0
- check_id: final-batch
  name: Complete frozen four-record batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root ran final batch; reviewer inspected /private/tmp/cmm-round6-check.log.
    Terminal exit 0: 307 passed, 3 skipped in 46.67 s; lint passed; 36 records, 0
    failed; 46 histories, 0 errors.'
  target_ids:
  - cmmmech:aluminium
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty-corpus
  name: Required nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Parent terminal receipt: 36 records; 0 failed; exit 0 after all four records
    frozen.'
  target_ids:
  - cmmmech:aluminium
  exit_code: 0
  expected_exit_code: 0
- check_id: final-history
  name: Final complete trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base d09a5611767d94fd196393b31d44cb8cf6657f7f
  status: passed
  required: true
  summary: 'Parent terminal receipt: 46 history records; 0 errors; exit 0 after all
    four records frozen. Earlier reviewer-owned history check covered 45 sessions
    before the final batch addition.'
  target_ids:
  - cmmmech:aluminium
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/aluminium.yaml
  locator: Complete target and linked CREATE sidecar
  accessed_at: '2026-10-11T05:42:39Z'
  support: supports
  summary: Inspection captured the exact working-tree record hash with real separate
    inline and canonical CREATE metadata.
  snapshot_sha256: a749a1f2d5283f0839bd99ef7be43bde6d9e43d576efd488e6db1505369ed6f4
- evidence_id: primary
  kind: primary_source
  reference: https://www.vut.cz/uredni-deska/habilitace?action=priloha&priloha=226417
  locator: Attachment E, PDF 80-85 / journal 154-159; Sections 2.1-2.5, 3.1, 3.3-3.5;
    Table 1; Figures 3, 7-8
  accessed_at: '2026-10-11T05:42:39Z'
  support: supports
  summary: Complete reproduced primary paper independently read from retained valid
    PDF; Figures 3, 5-9 rendered and visually checked. Supports G-10 preparation,
    0.2 g red mud/50 mL assay, ICP-OES filtrate result and chemical control, with
    no isolated-product demonstration.
  snapshot_sha256: 1ad163bac045935f00a43d67208749ea3b2091d6fb4d0d3efedabf831f637d84
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28984
  locator: Independently inspected freshly acquired authority HTML; title, formula
    and charge
  accessed_at: '2026-10-11T05:42:39Z'
  support: supports
  summary: CHEBI:28984 is aluminium atom, formula Al and net charge 0; element distinct
    from salts, red mud, alumina and bauxite.
  snapshot_sha256: 226574ac9bfb03e16c8cb83ae8aba71a219ae634627f2753eda3e106ebf1991b
- evidence_id: taxon
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5061&retmode=xml
  locator: Fresh retained XML ScientificName, Rank, TaxId
  accessed_at: '2026-10-11T05:42:39Z'
  support: supports
  summary: NCBI 5061 resolves to Aspergillus niger at species rank. Primary paper
    assigns G-10 by morphology and 612-bp ITS/99% similarity, rather than independently
    authenticating this strain.
  snapshot_sha256: d668c305ba04f31ca50a1582a5a9c85d6547109cbc132a097d5d2185a8c34ff8
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Page 50496 Aluminum row, final 2025 list; live page and retained HTML
  accessed_at: '2026-10-11T05:42:39Z'
  support: supports
  summary: Named aluminum commodity is explicitly in the US 2025 list; record date
    and elemental mapping preserve scope.
  snapshot_sha256: 0f56f0c2a87ab8ba92b46bcf407adc6f8d9a2d32f9383189c9c5e4092c2a99d1
- evidence_id: search
  kind: search
  reference: 2026-10-11 independent bounded review searches
  locator: Exact DOI correction/retraction/erratum; title/control/G-10 search; local
    exact root/ID/DOI
  accessed_at: '2026-10-11T05:42:39Z'
  support: context_only
  summary: No relevant correction notice found in returned first result sets; local
    target and current dossier are the only exact record/DOI matches. This is not
    an exhaustive literature or machine-wide claim.
  search_scope: web.search_query exact DOI correction OR retraction OR erratum and
    exact title control G-10, first results, no date filter / no pagination. rg --no-ignore
    --hidden exact root/CHEBI/DOI over data/records, research, reviews, history; cited
    primary/authority raw paths rehashed;unrelated home/temp not searched.
- evidence_id: batch-log
  kind: validation
  reference: /private/tmp/cmm-round6-check.log
  locator: Full final log plus parent terminal exit-code and separate validator receipts
  accessed_at: '2026-10-11T05:44:56Z'
  support: supports
  summary: Reviewer inspected final gate log; all required batch checks passed after
    record freeze. Scientific support was assessed independently of these structural
    checks.
assessments:
- assessment_id: identity
  area: identity
  topic: Element and species/strain grounding
  outcome: supported
  summary: Elemental Al and species-level Aspergillus label are correctly grounded;
    the record does not equate element with waste feed or species identifier with
    strain authentication.
  target_ids:
  - cmmmech:aluminium
  evidence_ids:
  - record
  - identity
  - taxon
  - primary
  dimensions:
  - name: material
    value: Element Al; red mud remains mixed feed
    definition: Record-root boundary
    evidence_ids:
    - identity
    - record
  - name: organism
    value: Authors assign G-10 to Aspergillus niger
    definition: 612-bp ITS with 99 percent similarity plus morphology; not a validated
      strain accession
    evidence_ids:
    - taxon
    - primary
- assessment_id: criticality
  area: scope
  topic: Dated commodity designation
  outcome: supported
  summary: Named US 2025 Aluminum designation is represented with jurisdiction, edition
    and authority and not inherited by all Al-bearing materials.
  target_ids:
  - cmmmech:aluminium
  evidence_ids:
  - record
  - criticality
  dimensions:
  - name: designation
    value: United States; USGS Final2025 List; 7 November2025
    definition: Dated authority designation, not universal criticality
    evidence_ids:
    - criticality
- assessment_id: mechanism
  area: evidence
  topic: Assay and measured endpoint
  outcome: supported
  summary: Primary experiment supports fungal-associated mobilization into filtrate
    under defined laboratory conditions and the stated approximately 141 mg/L endpoint.
  target_ids:
  - cmmmech:aluminium
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biomass
    value: Growing G-10 fungal cultures
    definition: Living culture, not dead sorbent or purified enzyme
    evidence_ids:
    - primary
  - name: substrate
    value: 0.2 g Ajka red mud; 45 mL broth + 5 mL spores
    definition: Air-dried, sieved below 0.2 mm; mixed feed with 6.97 percent total
      Al; Al-host mineral unresolved
    evidence_ids:
    - primary
  - name: conditions
    value: 25 degrees C, dark, static, 7 days, triplicate 250-mL flasks
    definition: Selected low-loading assay; higher loadings not silently pooled
    evidence_ids:
    - primary
  - name: measurement
    value: 0.45-micrometre filtrate; ICP-OES total Al
    definition: Approximately141 mg/L concentration, not free Al3+ speciation or isolated
      product yield
    evidence_ids:
    - primary
- assessment_id: controls
  area: consistency
  topic: Null control and mechanistic limits
  outcome: supported
  summary: Undetected/no-fungus Al and non-equivalent synthetic-acid comparison are
    retained without a numerical AlLOD or a proven proton-pump/enzyme mechanism.
  target_ids:
  - cmmmech:aluminium
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: controls
    value: No fungus; synthetic acid mixtures
    definition: Mixture B about 142 mg/L after 2 days; fungal 7-day results are not
      a matched kinetic comparison
    evidence_ids:
    - primary
  - name: scale
    value: Laboratory flasks only
    definition: No isolated aluminium metal or industrial deployment established
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Acquisition and actual CREATE history
  outcome: supported
  summary: Fresh local authority and primary payload hashes match receipt; primary
    reproduction and DOI identify one experiment. History target and real actor metadata
    agree with new record creation.
  target_ids:
  - cmmmech:aluminium
  evidence_ids:
  - record
  - primary
  - identity
  - taxon
  - criticality
findings: []
actions: []
limitations:
- ICP-OES of 0.45-micrometre filtrate reports filter-passing Al; no free-ion or isolated-product
  assay.
- No numerical aluminium detection limit supplied for no-fungus controls.
- Species assignment based on short ITS similarity is not independent strain authentication.
- Synthetic-acid experiments differ in medium and duration; proton and ligand mechanisms
  are not isolated.
- Al-host mineral phases unresolved; higher-loading figure40/50 g/L inconsistency
  excluded from imported low-loading assay.
- Authority payloads acquired by curator were independently read/rehashed; primary
  PDF is an official thesis reproduction of the same paper, not independent replication.
- Bounded first-page correction/counterevidence and hidden/ignored local searches
  are not exhaustive.
- Structured-review persistence and later publication/squash gates are separate from
  these completed scientific and batch checks.
```
