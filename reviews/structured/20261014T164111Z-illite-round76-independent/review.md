# Independent scientific review of illite round76

- Review: 20261014T164111Z-illite-round76-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T16:36:28.563507Z
- Finished UTC: 2026-10-14T16:41:11.429521Z
- Reviewer: codex /root/round68_phosphates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of a group-scoped IMt-1 illite record with culture-associated low-temperature redox and alteration. Source strain, medium, comparator, phase-provenance and potassium-ratio uncertainties are preserved; no isolated recovery or ocean-scale performance is inferred.

## Scope And Provenance

Entire exact owner, identity, mechanisms, conditions, controls, outcomes, source conflicts and canonical history; all claim-bearing original figures/tables and relevant SI.

Selection: Assigned frozen illite; all claims examined, not sampled.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 925a93db824261d146a14900b8367c88d25cbd71.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:illite | data/records/illite.yaml | maintained | Illite group |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent reviewer named validation | passed | True | cmmmech:illite | Actually executed 2026-10-14T16:36:36.127007+00:00 through 2026-10-14T16:36:39.950438+00:00;1record,0failures. |
| Coordinator terminal batch gate independently verified | passed | True | cmmmech:illite | Coordinator executed 2026-10-14T16:35:01.537264+00:00 through 2026-10-14T16:38:24.063506+00:00; terminal exit and entire log verified against unchanged input manifest. |
| Coordinator terminal batch gate independently verified | passed | True | cmmmech:illite | Coordinator executed 2026-10-14T16:38:24.063528+00:00 through 2026-10-14T16:38:33.692035+00:00; terminal exit and entire log verified against unchanged input manifest. |
| Coordinator terminal batch gate independently verified | passed | True | cmmmech:illite | Coordinator executed 2026-10-14T16:38:33.692058+00:00 through 2026-10-14T16:38:39.168718+00:00; terminal exit and entire log verified against unchanged input manifest. |
| Coordinator terminal batch gate independently verified | passed | True | cmmmech:illite | Coordinator executed 2026-10-14T16:38:39.168737+00:00 through 2026-10-14T16:38:42.769189+00:00; terminal exit and entire log verified against unchanged input manifest. |

## Scientific And Domain Assessments

### identity and claim scope

identity: supported. Targets: cmmmech:illite.

The compendium explicitly calls illite a GROUP. Record distinguishes group identity from the source IMt-1 preparation and from mixed illite-like transformation products elsewhere. It does not invent a universal endmember or transfer the species taxon to type strain M7.

### methods and claim scope

evidence: supported. Targets: cmmmech:illite.

&lt;2µm settled/freeze-dried IMt-1,4g/L,100mL nitrogen-purged M1, nominal20mM lactate,pH6,0/4°C and up to24weeks match original Methods. Unnamed Antarctic isolate washed three times and final~10^7CFU/mL is retained without an accession. Frozen/thawed sample treatment and acid/HF phenanthroline versus0.45µm-filtered ICP-AES are explicit. Triplicate analytical sets do not prove independent cultures.

### outcome and claim scope

evidence: supported. Targets: cmmmech:illite.

The narrow culture-control redox/operationally dissolved-iron contrast is supported. Both biotic trajectories end near3.1% source reduction at24weeks; earlier3.8%4°C is not a late endpoint. Dithionite2h is not time/medium matched to the multiweek culture. Limited vivianite XRD/Fe-P-OEDS does not prove pure phase or exclusive IMt-1 Fe provenance. Table1sodium selenate, undefinedM1stocks and2M lactate/formate conflict with sole-acceptor and20mM prose; exact full recipe and differentialK enrichment are correctly withheld.

### Exact reviewed inputs and actual gates

provenance: supported. Targets: cmmmech:illite.

Native inspection preceded final judgment; owner and canonical CREATE hashes remain frozen. Named validation plus all four current batch commands actually passed. No curation/history event was appended by reviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/illite.yaml; Entire native-inspected frozen owner | supports | All fields read; scientific assessment followed native inspection after preliminary read. No reviewer owner edits. |
| history | history/records/illite/2026-10-14T163249Z-codex-b0a6a1.yaml; Canonical CREATE sidecar plus distinct inline event | supports | Verified actor, actual timestamps, exact target and described creation scope; no invented historic authorship. |
| primary | https://doi.org/10.3389/fmicb.2022.980078; Complete ten-page original; Methodspp2–3, Figures1–6/Tables1–2 and Discussionpp4–7; full XML checked | supports | Read complete original and viewed all ten pages. Figure1 shows4°C early peak/decrease/recovery and0°C trajectory; Figure2 shows dissolved-total-Fe rise then decline, not monotonic accumulation. Figure3/Table2 and Figures4/5 support altered illite and source-assigned secondary phase. Figure4 K/(K+Ca) differs from prose K/(K+2Ca); chemical/biotic final ratios agree despite Discussion differential enrichment claim. Figure6 is a schematic, not direct molecular evidence. |
| group | https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf; PDFp34, reproduced Whitney/Evans Table1: chlorite and illite rows | supports | Original row pixels explicitly GROUP. Historical nomenclature table, not a claimed2026 mineral approval. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=518738; Current acquired authoritative XML; exact TaxId, ScientificName, Rank | supports | Shewanella vesiculosa, species rank verified independently. Taxonomy does not establish the experimental phenotype. |
| named | /private/tmp/cmm-round76-clays-independent/named-validation.json; Actual reviewer commands and log | supports | Each target checked separately,1record/0failures; exact start/finish and matching log checksum retained. |
| batch | /private/tmp/cmm-round76-final-gates.json; Terminal receipt: all FOUR actual commands, unchanged364-record input manifest and matching log | supports | Independently verified worktree/base, four expected command vectors, all exits0, unchanged owners and log SHA256 8bbfc2d4a2a7e38d93f94c3a9f0f7758fb6af775b4217cddf39ece223afe075a. Structural gates are not scientific proof. |
| dedup | /private/tmp/cmm-round76-clays-independent/dedup.txt; Hidden/ignored-inclusive, symlink-following local search | context_only | Bounded records/research/reviews/history and cited current raw; existing group/species/context mentions checked. No machine-wide absence claim. |
| notices | /private/tmp/cmm-round76-clays-independent/notice-search.json; Four bounded live query results plus Crossref relation/update fields | context_only | No matching notice surfaced. Follow-up2016sorption and2024freeze-thaw leads were not imported as direct replication. |
| xml | https://doi.org/10.3389/fmicb.2022.980078; Full Jung2022XML, methods/table/media and supplement-element inspection | context_only | Corroborates main text and metadata. No separate supplementary element is present; generic article/supplementary-material data statement is not evidence of an acquired SI file. |

## Limits And Additional Notes

- Experimental isolate lacks a strain accession or deposited sequence; species identity is a source assignment with correctly bounded taxonomy.
- Exact complete M1 composition and source of all dissolved/product Fe remain unresolved; Table1 includes metal/phosphate stocks andselenate.
- Chemical comparator duration/medium differs; no unique biological mechanism, time-matched superiority or phase-resolved Fe mass balance demonstrated.
- Jung fullXML/main did not identify an attached supplemental object; generic data-availability wording is not a downloaded SI dataset. Underlying raw data were not reanalyzed.
- Review uses curator-acquired originals independently inspected; it is not a fresh independent experimental replication or a comprehensive literature synthesis.
- Bounded live notice/conflicting-evidence queries and Crossref metadata did not surface a matching notice; absence is not proved.
- Criticality jurisdiction/list/edition is not asserted; no designation is inherited from constituents.
- Analytical validation establishes structure/provenance, not scientific truth. No reviewed owner or canonical history was edited by the reviewer.
- Start is actual native-inspect invocation; finish is actual completed-review construction after terminal batch receipt verification. Preliminary record read preceded inspect; scientific judgment followed it.
- Shared source PDFs, XML, taxonomy and nomenclature acquisitions were reused transparently, with exact hashes. All main original pages were visually inspected; no external source bytes were committed.
- iModulonDB is not applicable: no gene, locus, regulator or transcriptomics claim is asserted.
- No supported corrective finding was established in this scope. Source limitations remain explicit rather than being converted into invented review defects.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T164111Z-illite-round76-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of illite round76
started_at: '2026-10-14T16:36:28.563507Z'
finished_at: '2026-10-14T16:41:11.429521Z'
reviewer:
  identity: codex /root/round68_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: new_frontier peer authored these clay owners/history. Reviewer
    authored separate hopeite/whitlockite owners and made no changes to reviewed clay
    owners or histories. Shared original acquisitions were independently read and
    visually inspected; this is not independent experimental replication.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified acceptance of a group-scoped IMt-1 illite record with culture-associated
  low-temperature redox and alteration. Source strain, medium, comparator, phase-provenance
  and potassium-ratio uncertainties are preserved; no isolated recovery or ocean-scale
  performance is inferred.
source:
  git_revision: 925a93db824261d146a14900b8367c88d25cbd71
  state: working_tree
  inputs:
  - path: data/records/illite.yaml
    sha256: 26ec1710dfe94d7dc6adf5b776eb1448612b9b698c0836b3a3b97eed98808899
    role: target
  - path: history/records/illite/2026-10-14T163249Z-codex-b0a6a1.yaml
    sha256: 47ee269309295cc523997346b4b65313665ac9d5d9800ecb7746f901b70f8a0a
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire exact owner, identity, mechanisms, conditions, controls, outcomes,
    source conflicts and canonical history; all claim-bearing original figures/tables
    and relevant SI.
  selection: Assigned frozen illite; all claims examined, not sampled.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:illite
targets:
- target_id: cmmmech:illite
  path: data/records/illite.yaml
  label: Illite group
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/illite.yaml
    role: maintained_scientific_record
checks:
- check_id: named
  name: Independent reviewer named validation
  command: uv run --locked cmmmech validate data/records/illite.yaml --require-records
  status: passed
  required: true
  summary: Actually executed 2026-10-14T16:36:36.127007+00:00 through 2026-10-14T16:36:39.950438+00:00;1record,0failures.
  target_ids:
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch_0
  name: Coordinator terminal batch gate independently verified
  command: just check
  status: passed
  required: true
  summary: Coordinator executed 2026-10-14T16:35:01.537264+00:00 through 2026-10-14T16:38:24.063506+00:00;
    terminal exit and entire log verified against unchanged input manifest.
  target_ids:
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_1
  name: Coordinator terminal batch gate independently verified
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator executed 2026-10-14T16:38:24.063528+00:00 through 2026-10-14T16:38:33.692035+00:00;
    terminal exit and entire log verified against unchanged input manifest.
  target_ids:
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_2
  name: Coordinator terminal batch gate independently verified
  command: uv run --locked cmmmech validate-history --base 925a93db824261d146a14900b8367c88d25cbd71
  status: passed
  required: true
  summary: Coordinator executed 2026-10-14T16:38:33.692058+00:00 through 2026-10-14T16:38:39.168718+00:00;
    terminal exit and entire log verified against unchanged input manifest.
  target_ids:
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch_3
  name: Coordinator terminal batch gate independently verified
  command: uv run --locked python scripts/render_pages.py --check
  status: passed
  required: true
  summary: Coordinator executed 2026-10-14T16:38:39.168737+00:00 through 2026-10-14T16:38:42.769189+00:00;
    terminal exit and entire log verified against unchanged input manifest.
  target_ids:
  - cmmmech:illite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/illite.yaml
  locator: Entire native-inspected frozen owner
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: All fields read; scientific assessment followed native inspection after
    preliminary read. No reviewer owner edits.
  snapshot_sha256: 26ec1710dfe94d7dc6adf5b776eb1448612b9b698c0836b3a3b97eed98808899
- evidence_id: history
  kind: record_content
  reference: history/records/illite/2026-10-14T163249Z-codex-b0a6a1.yaml
  locator: Canonical CREATE sidecar plus distinct inline event
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Verified actor, actual timestamps, exact target and described creation
    scope; no invented historic authorship.
  snapshot_sha256: 47ee269309295cc523997346b4b65313665ac9d5d9800ecb7746f901b70f8a0a
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2022.980078
  locator: Complete ten-page original; Methodspp2–3, Figures1–6/Tables1–2 and Discussionpp4–7;
    full XML checked
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Read complete original and viewed all ten pages. Figure1 shows4°C early
    peak/decrease/recovery and0°C trajectory; Figure2 shows dissolved-total-Fe rise
    then decline, not monotonic accumulation. Figure3/Table2 and Figures4/5 support
    altered illite and source-assigned secondary phase. Figure4 K/(K+Ca) differs from
    prose K/(K+2Ca); chemical/biotic final ratios agree despite Discussion differential
    enrichment claim. Figure6 is a schematic, not direct molecular evidence.
  snapshot_sha256: 3e3c3b008d74f71044bdf3a1c75e476e013d5fb080f38c6e2891fcb5607a593c
- evidence_id: group
  kind: authority
  reference: https://cnmnc.units.it/ima_reports/2%20IMA-Nomenclature-e-Booklet-2019-1.pdf
  locator: 'PDFp34, reproduced Whitney/Evans Table1: chlorite and illite rows'
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Original row pixels explicitly GROUP. Historical nomenclature table, not
    a claimed2026 mineral approval.
  snapshot_sha256: aa78fca8983aa876dd2657e1874aa8f012a3e0236ad6717b675b76d86f8868c5
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=518738
  locator: Current acquired authoritative XML; exact TaxId, ScientificName, Rank
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Shewanella vesiculosa, species rank verified independently. Taxonomy does
    not establish the experimental phenotype.
  snapshot_sha256: 3191fa4402dd7539f337f4ee2b960653f3d08876eb783765b2e2cf0829bd7198
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round76-clays-independent/named-validation.json
  locator: Actual reviewer commands and log
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Each target checked separately,1record/0failures; exact start/finish and
    matching log checksum retained.
  snapshot_sha256: b9c0490d0470eb316521afb11d6f037cc7b0d9ba0929cf5e70947362db303ce1
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round76-final-gates.json
  locator: 'Terminal receipt: all FOUR actual commands, unchanged364-record input
    manifest and matching log'
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: supports
  summary: Independently verified worktree/base, four expected command vectors, all
    exits0, unchanged owners and log SHA256 8bbfc2d4a2a7e38d93f94c3a9f0f7758fb6af775b4217cddf39ece223afe075a.
    Structural gates are not scientific proof.
  snapshot_sha256: f18e5f6a252ea29194da47a54fe630e7a58a68c3b3591987f8befe1dd12b95ae
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round76-clays-independent/dedup.txt
  locator: Hidden/ignored-inclusive, symlink-following local search
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: context_only
  summary: Bounded records/research/reviews/history and cited current raw; existing
    group/species/context mentions checked. No machine-wide absence claim.
  snapshot_sha256: 34ba669e65977668657b23d221c3e40c17572f345903be99dda2e7205d0fc2cc
  search_scope: Current corpus/research/reviews/history, main records and current
    raw source directory; hidden/ignored included, symlinks followed. No machine-wide
    absence asserted.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round76-clays-independent/notice-search.json
  locator: Four bounded live query results plus Crossref relation/update fields
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: context_only
  summary: No matching notice surfaced. Follow-up2016sorption and2024freeze-thaw leads
    were not imported as direct replication.
  snapshot_sha256: d0517e52a95496a80a1f0f81c676049bd2273cf936608ff11b3d6e348df1ee4c
  search_scope: web.run 2026-10-14; exact two DOI correction/retraction queries plus
    chlorite/Brookshaw/Shewanella/impurity and illite/Shewanella vesiculosa/reduction2022;
    no filters, bounded returned results.
- evidence_id: xml
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2022.980078
  locator: Full Jung2022XML, methods/table/media and supplement-element inspection
  accessed_at: '2026-10-14T16:41:11.429521Z'
  support: context_only
  summary: Corroborates main text and metadata. No separate supplementary element
    is present; generic article/supplementary-material data statement is not evidence
    of an acquired SI file.
  snapshot_sha256: ee42a014c61538feead4b2a8a122ccc8727f3e957c6dcac1cd15501029d43df2
assessments:
- assessment_id: identity
  area: identity
  topic: identity and claim scope
  outcome: supported
  summary: The compendium explicitly calls illite a GROUP. Record distinguishes group
    identity from the source IMt-1 preparation and from mixed illite-like transformation
    products elsewhere. It does not invent a universal endmember or transfer the species
    taxon to type strain M7.
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - record
  - group
  - taxonomy
  dimensions:
  - name: criticality
    value: No jurisdiction/list/edition asserted
    definition: Constituent status is not inherited by mineral-group owner.
    evidence_ids:
    - record
- assessment_id: methods
  area: evidence
  topic: methods and claim scope
  outcome: supported
  summary: <2µm settled/freeze-dried IMt-1,4g/L,100mL nitrogen-purged M1, nominal20mM
    lactate,pH6,0/4°C and up to24weeks match original Methods. Unnamed Antarctic isolate
    washed three times and final~10^7CFU/mL is retained without an accession. Frozen/thawed
    sample treatment and acid/HF phenanthroline versus0.45µm-filtered ICP-AES are
    explicit. Triplicate analytical sets do not prove independent cultures.
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - record
  - primary
  - taxonomy
  - xml
  dimensions:
  - name: material_form
    value: Source-designated IMt-1 illite group preparation, <2µm
    definition: No phase-pure ideal endmember or universal formula asserted.
    evidence_ids:
    - record
    - primary
    - taxonomy
    - xml
  - name: organism_and_biomass
    value: Source-assigned unnamed Shewanella vesiculosa isolate, species TaxID518738;
      washed cells~10^7CFU/mL
    definition: Species mapping does not identify M7 or independently authenticate
      the inoculum.
    evidence_ids:
    - record
    - primary
    - taxonomy
    - xml
  - name: conditions_and_controls
    value: 0/4°C,pH6,up to24weeks; uninoculated controls and separate2h dithionite
    definition: Source table/prose medium contradictions and unmatched comparator
      persist.
    evidence_ids:
    - record
    - primary
    - taxonomy
    - xml
  - name: outcome_denominators
    value: Source operational Fe reduction and filtered total dissolved iron; morphology/XRD
    definition: No biological uptake, phase-pure product or closed recovery balance
      measured.
    evidence_ids:
    - record
    - primary
    - taxonomy
    - xml
  - name: deployment
    value: Laboratory bottles only
    definition: Proposed ocean implications are not quantified deployment.
    evidence_ids:
    - record
    - primary
    - taxonomy
    - xml
- assessment_id: outcome
  area: evidence
  topic: outcome and claim scope
  outcome: supported
  summary: The narrow culture-control redox/operationally dissolved-iron contrast
    is supported. Both biotic trajectories end near3.1% source reduction at24weeks;
    earlier3.8%4°C is not a late endpoint. Dithionite2h is not time/medium matched
    to the multiweek culture. Limited vivianite XRD/Fe-P-OEDS does not prove pure
    phase or exclusive IMt-1 Fe provenance. Table1sodium selenate, undefinedM1stocks
    and2M lactate/formate conflict with sole-acceptor and20mM prose; exact full recipe
    and differentialK enrichment are correctly withheld.
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - record
  - primary
  - taxonomy
  - xml
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed inputs and actual gates
  outcome: supported
  summary: Native inspection preceded final judgment; owner and canonical CREATE hashes
    remain frozen. Named validation plus all four current batch commands actually
    passed. No curation/history event was appended by reviewer.
  target_ids:
  - cmmmech:illite
  evidence_ids:
  - record
  - history
  - named
  - batch
  - dedup
  - notices
findings: []
actions: []
limitations:
- Experimental isolate lacks a strain accession or deposited sequence; species identity
  is a source assignment with correctly bounded taxonomy.
- Exact complete M1 composition and source of all dissolved/product Fe remain unresolved;
  Table1 includes metal/phosphate stocks andselenate.
- Chemical comparator duration/medium differs; no unique biological mechanism, time-matched
  superiority or phase-resolved Fe mass balance demonstrated.
- Jung fullXML/main did not identify an attached supplemental object; generic data-availability
  wording is not a downloaded SI dataset. Underlying raw data were not reanalyzed.
- Review uses curator-acquired originals independently inspected; it is not a fresh
  independent experimental replication or a comprehensive literature synthesis.
- Bounded live notice/conflicting-evidence queries and Crossref metadata did not surface
  a matching notice; absence is not proved.
- Criticality jurisdiction/list/edition is not asserted; no designation is inherited
  from constituents.
- Analytical validation establishes structure/provenance, not scientific truth. No
  reviewed owner or canonical history was edited by the reviewer.
notes:
- Start is actual native-inspect invocation; finish is actual completed-review construction
  after terminal batch receipt verification. Preliminary record read preceded inspect;
  scientific judgment followed it.
- Shared source PDFs, XML, taxonomy and nomenclature acquisitions were reused transparently,
  with exact hashes. All main original pages were visually inspected; no external
  source bytes were committed.
- 'iModulonDB is not applicable: no gene, locus, regulator or transcriptomics claim
  is asserted.'
- No supported corrective finding was established in this scope. Source limitations
  remain explicit rather than being converted into invented review defects.
tags:
- round76
- illite
- independent
- primary-figures
- qualified-microbial
```
