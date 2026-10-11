# Independent scientific review of the cesium expansion record

- Review: 20261011T065833Z-cesium-round9-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T06:54:47Z
- Finished UTC: 2026-10-11T06:58:33Z
- Reviewer: Codex /root/cmm9_si_sn (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The inspected cesium record accurately represents retention by washed JCM 1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer step. Quantities, separate mapping conditions and laboratory scope match the primary paper. It does not claim a proven intracellular transport/polyphosphate mechanism, unique Sr displacement, radioisotope treatment, clinical benefit or recovered-product yield. No actionable curation defect was found in this scope.

## Scope And Provenance

All scientific, criticality, identity and provenance fields of the named final record.

Selection: Named single-record assignment; all fields assessed, no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9fa187ff5a455f495cfa2635e60c413b6763370d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cesium | data/records/cesium.yaml | maintained | Cesium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:cesium | Reviewer executed; terminal exit 0, 2 records, zero failures. |
| Trusted-base history | passed | True | cmmmech:cesium | Reviewer executed; terminal exit 0, 64 history records, zero errors. |
| Completed-batch gate | passed | True | cmmmech:cesium | Root executed; reviewer read /private/tmp/cmm-round9-batch-check.log. Terminal exit 0: lint passed; 307 tests passed, 3 skipped; 54 records and 64 histories valid. |
| Nonempty corpus | passed | True | cmmmech:cesium | Root executed; reviewer read /private/tmp/cmm-round9-validation.log. Terminal exit 0: 54 records, zero failures. |

## Scientific And Domain Assessments

### Material and organism boundaries

identity: supported. Targets: cmmmech:cesium.

ChEBI:30514 denotes caesium atom, formula Cs and charge zero; neutral elemental identity does not denote the experimental Cs(I) chloride, pollucite or a radioisotope. NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275 catalogue independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence; the record does not present the species identifier as strain-specific.

### Authority and dated commodity designation

evidence: supported. Targets: cmmmech:cesium.

United States Department of the Interior / USGS final 2025 mineral-commodity designation names Cesium. Its No table cell concerns byproduct/co-product occurrence, not whether cesium is critical. The elemental mapping and list edition are explicit.

### Experimental support and causal boundaries

evidence: supported. Targets: cmmmech:cesium.

The inspected cesium record accurately represents retention by washed JCM 1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer step. Quantities, separate mapping conditions and laboratory scope match the primary paper. It does not claim a proven intracellular transport/polyphosphate mechanism, unique Sr displacement, radioisotope treatment, clinical benefit or recovered-product yield. No actionable curation defect was found in this scope.

### Units, denominators and endpoint interpretation

quantity: supported. Targets: cmmmech:cesium.

Text and Figure 4 report 70.5 mg Cs/g dry cells before the sequential Sr step, 55.7 mg Cs/g dry cells afterward and 8.1 mg Sr/g dry cells afterward; 21% is the reported decline in retained Cs, not a feed-removal fraction. Figure 4 uses standard errors with n=3 without resolving replicate type. Figures 1 and 2 do not establish polyphosphate chemistry or a quantitative mass balance.

### Actual curation events

provenance: supported. Targets: cmmmech:cesium.

Separate actual inline and CREATE sidecar timestamps, actor/model/tool and issue39 linkage are present. Trusted-base history validation passed. The reviewer did not append a curation event for review alone.

### Bounded adversarial checks

completeness: supported. Targets: cmmmech:cesium.

Scoped correction, contrary-evidence and ignored-inclusive duplicate searches are explicit; source access limitations remain visible.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cesium.yaml; All frozen fields, schema and linked CREATE sidecar | supports | Inspected exact working-tree bytes before formal assessment; no edits to this record or history. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:30514; Authority compound entry, formula and charge; acquired official API payload | supports | ChEBI:30514 denotes caesium atom, formula Cs and charge zero; neutral elemental identity does not denote the experimental Cs(I) chloride, pollucite or a radioisotope. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1680/dataset_report; Official NCBI taxonomy payload and strain authority | supports | NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275 catalogue independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence; the record does not present the species identifier as strain-specific. |
| criticality | https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm; Final 2025 List of Critical Minerals, November 7 2025, Cesium row on page 50496 | supports | United States Department of the Interior / USGS final 2025 mineral-commodity designation names Cesium. Its No table cell concerns byproduct/co-product occurrence, not whether cesium is critical. The elemental mapping and list edition are explicit. |
| primary | https://doi.org/10.1038/s41598-024-57678-8; Culture conditions; Determination of Cs contained in bacterial cells; mapping method; simultaneous removal method; Results and Discussion; Figures 1-4 | supports | The inspected cesium record accurately represents retention by washed JCM 1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer step. Quantities, separate mapping conditions and laboratory scope match the primary paper. It does not claim a proven intracellular transport/polyphosphate mechanism, unique Sr displacement, radioisotope treatment, clinical benefit or recovered-product yield. No actionable curation defect was found in this scope. Text and Figure 4 report 70.5 mg Cs/g dry cells before the sequential Sr step, 55.7 mg Cs/g dry cells afterward and 8.1 mg Sr/g dry cells afterward; 21% is the reported decline in retained Cs, not a feed-removal fraction. Figure 4 uses standard errors with n=3 without resolving replicate type. Figures 1 and 2 do not establish polyphosphate chemistry or a quantitative mass balance. |
| strain | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1275; Catalogue equivalence and species ID | supports | NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275 catalogue independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence; the record does not present the species identifier as strain-specific. |
| figure1 | https://doi.org/10.1038/s41598-024-57678-8; Main Figure 1, original acquired JPEG inspected visually | supports | Independent pixel inspection of the original figure alongside its caption, legend and methods. No unreported numerical value was digitized or reconstructed. |
| figure2 | https://doi.org/10.1038/s41598-024-57678-8; Main Figure 2, original acquired JPEG inspected visually | supports | Independent pixel inspection of the original figure alongside its caption, legend and methods. No unreported numerical value was digitized or reconstructed. |
| figure3 | https://doi.org/10.1038/s41598-024-57678-8; Main Figure 3, original acquired JPEG inspected visually | supports | Independent pixel inspection of the original figure alongside its caption, legend and methods. No unreported numerical value was digitized or reconstructed. |
| figure4 | https://doi.org/10.1038/s41598-024-57678-8; Main Figure 4, original acquired JPEG inspected visually | supports | Independent pixel inspection of the original figure alongside its caption, legend and methods. No unreported numerical value was digitized or reconstructed. |
| search | Reviewer web searches and bounded local inventory; 2026-10-11 first returned web result sets; hidden/ignored-inclusive local search | context_only | No direct correction, retraction or contrary replication surfaced in the bounded result sets inspected. Related patents and secondary summaries do not establish a direct contradiction to the qualified recorded endpoints. This is not an exhaustive absence claim. |

## Limits And Additional Notes

- The primary study does not resolve all Cs as intracellular, identify polyphosphate chemically or distinguish all sorption/uptake pathways with perturbation controls.
- A matched Sr-free post-loading incubation is absent from the described design; the observed Cs loss cannot uniquely be attributed to Sr displacement.
- The dry-cell denominator lacks a stated drying protocol, the n=3 biological/technical distinction is unspecified, and growth-medium pH and controlled atmosphere are not reported.
- 50 mM capacity assays and 100 mM mapping are distinct; the high-concentration inhibition and practical gastrointestinal mismatch are preserved.
- No whole-feed mass balance, isolated product, radionuclide trial, clinical outcome or industrial deployment is established.
- Correction/counterevidence and duplicate searches are bounded, not literature-wide or machine-wide absence proofs.
- Working-tree input hashes attest these uncommitted bytes against the durable trusted main ancestor, not their presence in that ancestor.
- Source limitations already stated in the record are not manufactured as corrective findings.
- Fresh web resolution succeeded for Cs ChEBI, JCM and both designation authorities. Browser retrieval of Sr ChEBI and the NCBI JSON API failed; independently inspected the curator-acquired official API payloads with recorded URLs, actual acquisition times and hashes instead.
- Reviewer verified root batch gate logs; no claim is made to have personally rerun the full suite.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T065833Z-cesium-round9-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of the cesium expansion record
started_at: '2026-10-11T06:54:47Z'
finished_at: '2026-10-11T06:58:33Z'
reviewer:
  identity: Codex /root/cmm9_si_sn
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different from the Cs/Sr curator; authored only the Si/Sn records
    in this batch. Independently inspected Cs/Sr primary methods/results, original
    figure pixels, authority entries and exact frozen inputs; made no Cs/Sr record
    or history edits.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The inspected cesium record accurately represents retention by washed JCM
  1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer step.
  Quantities, separate mapping conditions and laboratory scope match the primary paper.
  It does not claim a proven intracellular transport/polyphosphate mechanism, unique
  Sr displacement, radioisotope treatment, clinical benefit or recovered-product yield.
  No actionable curation defect was found in this scope.
source:
  git_revision: 9fa187ff5a455f495cfa2635e60c413b6763370d
  state: working_tree
  inputs:
  - path: data/records/cesium.yaml
    sha256: d4e1a06183ea4b843f0083eb93c4fca315a1f1a3b2bca5048e06403d6922f345
    role: target
  - path: history/records/cesium/2026-10-11T065053Z-codex-6510dc.yaml
    sha256: 6faeb484820419058c193a71e2ba063a61f2832d6d0f3385f7c3622849ae8b03
    role: context
  - path: research/ingests/round9-cs-sr-20261011.json
    sha256: 2197455050fb7f15189bc8f75f6e5b6054d94b0af843c6c719ea6e023898be5e
    role: context
  - path: research/ingests/round9-cs-sr-20261011.md
    sha256: e3b306a61ac17a071ec5a5a4e1e1736741e3a81470206d33632f0a152fdcb757
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
scope:
  description: All scientific, criticality, identity and provenance fields of the
    named final record.
  selection: Named single-record assignment; all fields assessed, no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cesium
targets:
- target_id: cmmmech:cesium
  path: data/records/cesium.yaml
  label: Cesium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cesium.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/cesium.yaml data/records/strontium.yaml
  status: passed
  required: true
  summary: Reviewer executed; terminal exit 0, 2 records, zero failures.
  target_ids:
  - cmmmech:cesium
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 9fa187ff5a455f495cfa2635e60c413b6763370d
  status: passed
  required: true
  summary: Reviewer executed; terminal exit 0, 64 history records, zero errors.
  target_ids:
  - cmmmech:cesium
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed-batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root executed; reviewer read /private/tmp/cmm-round9-batch-check.log.
    Terminal exit 0: lint passed; 307 tests passed, 3 skipped; 54 records and 64 histories
    valid.'
  target_ids:
  - cmmmech:cesium
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Root executed; reviewer read /private/tmp/cmm-round9-validation.log. Terminal
    exit 0: 54 records, zero failures.'
  target_ids:
  - cmmmech:cesium
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cesium.yaml
  locator: All frozen fields, schema and linked CREATE sidecar
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: Inspected exact working-tree bytes before formal assessment; no edits to
    this record or history.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30514
  locator: Authority compound entry, formula and charge; acquired official API payload
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: ChEBI:30514 denotes caesium atom, formula Cs and charge zero; neutral elemental
    identity does not denote the experimental Cs(I) chloride, pollucite or a radioisotope.
  snapshot_sha256: 995f28529290f890cd9e231ff78a2e79a73721cd9f8cadc92e7a5cdf7863b1a6
- evidence_id: taxon
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1680/dataset_report
  locator: Official NCBI taxonomy payload and strain authority
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275
    catalogue independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence;
    the record does not present the species identifier as strain-specific.
  snapshot_sha256: 4d821af4a662dfb21de8309f3ab600c998f63a68358fb372cb875b832fbbe4d6
- evidence_id: criticality
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm
  locator: Final 2025 List of Critical Minerals, November 7 2025, Cesium row on page
    50496
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: United States Department of the Interior / USGS final 2025 mineral-commodity
    designation names Cesium. Its No table cell concerns byproduct/co-product occurrence,
    not whether cesium is critical. The elemental mapping and list edition are explicit.
  snapshot_sha256: e13ee3cb37efbea401f4a7e9e3c761a9653d6aab258ff6c4cd6ba4a0076dd615
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-024-57678-8
  locator: Culture conditions; Determination of Cs contained in bacterial cells; mapping
    method; simultaneous removal method; Results and Discussion; Figures 1-4
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: The inspected cesium record accurately represents retention by washed JCM
    1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer
    step. Quantities, separate mapping conditions and laboratory scope match the primary
    paper. It does not claim a proven intracellular transport/polyphosphate mechanism,
    unique Sr displacement, radioisotope treatment, clinical benefit or recovered-product
    yield. No actionable curation defect was found in this scope. Text and Figure
    4 report 70.5 mg Cs/g dry cells before the sequential Sr step, 55.7 mg Cs/g dry
    cells afterward and 8.1 mg Sr/g dry cells afterward; 21% is the reported decline
    in retained Cs, not a feed-removal fraction. Figure 4 uses standard errors with
    n=3 without resolving replicate type. Figures 1 and 2 do not establish polyphosphate
    chemistry or a quantitative mass balance.
  snapshot_sha256: 6fdbce5bf05ff9a1483966a8bf72b2d2570d070c0a016edeb817607e8417c4cb
- evidence_id: strain
  kind: database
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1275
  locator: Catalogue equivalence and species ID
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275
    catalogue independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence;
    the record does not present the species identifier as strain-specific.
  snapshot_sha256: 87fc870a0df9e431e47e4da9a3052e354fc5e5e74cd02a9b5a8d9e61425282b2
- evidence_id: figure1
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-024-57678-8
  locator: Main Figure 1, original acquired JPEG inspected visually
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: Independent pixel inspection of the original figure alongside its caption,
    legend and methods. No unreported numerical value was digitized or reconstructed.
  snapshot_sha256: 140f0ec09779382fa8370ff4eba8c71168c4cb86b1d68b03cc59b08e111b9433
- evidence_id: figure2
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-024-57678-8
  locator: Main Figure 2, original acquired JPEG inspected visually
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: Independent pixel inspection of the original figure alongside its caption,
    legend and methods. No unreported numerical value was digitized or reconstructed.
  snapshot_sha256: 91d02f6a1d9c90b7f69e1bb61395d13d68f97dd538c6a315c6480abca9380efd
- evidence_id: figure3
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-024-57678-8
  locator: Main Figure 3, original acquired JPEG inspected visually
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: Independent pixel inspection of the original figure alongside its caption,
    legend and methods. No unreported numerical value was digitized or reconstructed.
  snapshot_sha256: 56f15e964b34e7867ba3f0c0bf0ed4756abf9efa5fa674db2d15e724c6b17d14
- evidence_id: figure4
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-024-57678-8
  locator: Main Figure 4, original acquired JPEG inspected visually
  accessed_at: '2026-10-11T06:58:33Z'
  support: supports
  summary: Independent pixel inspection of the original figure alongside its caption,
    legend and methods. No unreported numerical value was digitized or reconstructed.
  snapshot_sha256: 2fefafd4319267e0871e7fdcc18f79230a1b0f4f07dbb0a730f5c51ac2d7e332
- evidence_id: search
  kind: search
  reference: Reviewer web searches and bounded local inventory
  locator: 2026-10-11 first returned web result sets; hidden/ignored-inclusive local
    search
  accessed_at: '2026-10-11T06:58:33Z'
  support: context_only
  summary: No direct correction, retraction or contrary replication surfaced in the
    bounded result sets inspected. Related patents and secondary summaries do not
    establish a direct contradiction to the qualified recorded endpoints. This is
    not an exhaustive absence claim.
  search_scope: 'Web queries: "10.1038/s41598-024-57678-8" correction retraction;
    "10.1128/AEM.00855-17" correction retraction; "Bifidobacterium adolescentis" "cesium"
    "polyphosphate"; "Bacillus" "TK2d" strontium abiotic control. First returned sets
    only, no exhaustive pagination. rg --hidden --no-ignore -L searched data/records,
    history, research, reviews and /private/tmp/cmm-round9-cs-sr-raw for both exact
    record IDs and both DOIs, including ignored files and following relevant symlinks.
    Matches include each intended record, shared dossier/frontier and cited primary/raw
    files; no second maintained record was identified within this bounded inventory.'
assessments:
- assessment_id: identity
  area: identity
  topic: Material and organism boundaries
  outcome: supported
  summary: ChEBI:30514 denotes caesium atom, formula Cs and charge zero; neutral elemental
    identity does not denote the experimental Cs(I) chloride, pollucite or a radioisotope.
    NCBI 1680 is Bifidobacterium adolescentis at species rank. The JCM 1275 catalogue
    independently supplies strain identity and ATCC 15703 / DSM 20083 equivalence;
    the record does not present the species identifier as strain-specific.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - record
  - identity
  - taxon
  - strain
- assessment_id: criticality
  area: evidence
  topic: Authority and dated commodity designation
  outcome: supported
  summary: United States Department of the Interior / USGS final 2025 mineral-commodity
    designation names Cesium. Its No table cell concerns byproduct/co-product occurrence,
    not whether cesium is critical. The elemental mapping and list edition are explicit.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - record
  - criticality
  dimensions:
  - name: designation
    value: United States Department of the Interior / USGS final 2025 mineral-commodity
      designation names Cesium. Its No table cell concerns byproduct/co-product occurrence,
      not whether cesium is critical. The elemental mapping and list edition are explicit.
    definition: Authority, jurisdiction, named list and exact edition define the criticality
      claim; no undated universal status.
    evidence_ids:
    - criticality
- assessment_id: mechanism
  area: evidence
  topic: Experimental support and causal boundaries
  outcome: supported
  summary: The inspected cesium record accurately represents retention by washed JCM
    1275 biomass and the subsequent loss of some retained Cs during the Sr-buffer
    step. Quantities, separate mapping conditions and laboratory scope match the primary
    paper. It does not claim a proven intracellular transport/polyphosphate mechanism,
    unique Sr displacement, radioisotope treatment, clinical benefit or recovered-product
    yield. No actionable curation defect was found in this scope.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - record
  - primary
  - figure1
  - figure2
  - figure3
  - figure4
  dimensions:
  - name: organism
    value: Bifidobacterium adolescentis JCM 1275; NCBITaxon:1680 is species-level.
    definition: Experimental strain and identifier scope are not conflated.
    evidence_ids:
    - record
    - primary
  - name: biomass
    value: Growth-derived, twice-water-washed cells; nitric-acid/peroxide digest analyzed
      by ICP-MS.
    definition: Pellet-associated content after washing is the operational endpoint.
    evidence_ids:
    - record
    - primary
  - name: substrate
    value: Non-radioactive CsCl at 50 mM for capacity; 100 mM for separate EPMA mapping.
    definition: Dissolved Cs(I) salt is not elemental Cs metal, ore, waste or radionuclide
      feed.
    evidence_ids:
    - record
    - primary
  - name: conditions
    value: Static 24 h at 37 C following two 1% v/v precultures; complex bifidobacterial
      medium with glucose, peptone, extracts and reducing additives.
    definition: Capacity applies to the reported laboratory growth medium, whose pH
      and gas control are unspecified.
    evidence_ids:
    - record
    - primary
  - name: sequential_step
    value: Cells from 2 mL culture transferred to 2 mL 1 mM Bis-Tris pH 6.8 plus 1
      mM SrCl2, 3 h at 37 C, 200 strokes/min and 25 mm stroke.
    definition: The study sequences Cs loading and Sr exposure rather than simultaneous
      mixed-feed extraction.
    evidence_ids:
    - record
    - primary
  - name: controls
    value: Zero-Cs growth comparator; no killed-cell or metabolic perturbation mechanism
      control and no matched post-loading Sr-free incubation.
    definition: Observed retention/release is supported while a unique molecular cause
      is not.
    evidence_ids:
    - record
    - primary
  - name: outcome
    value: Biomass-associated elemental Cs measured as mg/g dry cells; subsequent
      partial release; Cs/P mapping at a distinct concentration.
    definition: Biomass normalization is neither feed-removal fraction nor isolated-product
      yield.
    evidence_ids:
    - record
    - primary
  - name: deployment
    value: Laboratory non-radioactive reagent experiments; future in vivo work proposed.
    definition: No clinical, radionuclide or industrial efficacy claim is justified.
    evidence_ids:
    - record
    - primary
- assessment_id: quantity
  area: quantity
  topic: Units, denominators and endpoint interpretation
  outcome: supported
  summary: Text and Figure 4 report 70.5 mg Cs/g dry cells before the sequential Sr
    step, 55.7 mg Cs/g dry cells afterward and 8.1 mg Sr/g dry cells afterward; 21%
    is the reported decline in retained Cs, not a feed-removal fraction. Figure 4
    uses standard errors with n=3 without resolving replicate type. Figures 1 and
    2 do not establish polyphosphate chemistry or a quantitative mass balance.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Actual curation events
  outcome: supported
  summary: Separate actual inline and CREATE sidecar timestamps, actor/model/tool
    and issue39 linkage are present. Trusted-base history validation passed. The reviewer
    did not append a curation event for review alone.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - record
- assessment_id: search
  area: completeness
  topic: Bounded adversarial checks
  outcome: supported
  summary: Scoped correction, contrary-evidence and ignored-inclusive duplicate searches
    are explicit; source access limitations remain visible.
  target_ids:
  - cmmmech:cesium
  evidence_ids:
  - search
findings: []
actions: []
limitations:
- The primary study does not resolve all Cs as intracellular, identify polyphosphate
  chemically or distinguish all sorption/uptake pathways with perturbation controls.
- A matched Sr-free post-loading incubation is absent from the described design; the
  observed Cs loss cannot uniquely be attributed to Sr displacement.
- The dry-cell denominator lacks a stated drying protocol, the n=3 biological/technical
  distinction is unspecified, and growth-medium pH and controlled atmosphere are not
  reported.
- 50 mM capacity assays and 100 mM mapping are distinct; the high-concentration inhibition
  and practical gastrointestinal mismatch are preserved.
- No whole-feed mass balance, isolated product, radionuclide trial, clinical outcome
  or industrial deployment is established.
- Correction/counterevidence and duplicate searches are bounded, not literature-wide
  or machine-wide absence proofs.
notes:
- Working-tree input hashes attest these uncommitted bytes against the durable trusted
  main ancestor, not their presence in that ancestor.
- Source limitations already stated in the record are not manufactured as corrective
  findings.
- Fresh web resolution succeeded for Cs ChEBI, JCM and both designation authorities.
  Browser retrieval of Sr ChEBI and the NCBI JSON API failed; independently inspected
  the curator-acquired official API payloads with recorded URLs, actual acquisition
  times and hashes instead.
- Reviewer verified root batch gate logs; no claim is made to have personally rerun
  the full suite.
links:
- research/ingests/round9-cs-sr-20261011.md
- research/ingests/round9-cs-sr-20261011.json
- https://github.com/CultureBotAI/CMMMech/issues/39
tags:
- round9
- cesium
- independent-review
- primary-literature
```
