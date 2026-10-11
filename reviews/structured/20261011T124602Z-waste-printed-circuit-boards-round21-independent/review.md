# Independent scientific review of waste printed circuit boards

- Review: 20261011T124602Z-waste-printed-circuit-boards-round21-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T12:42:56.425721Z
- Finished UTC: 2026-10-11T12:46:02.358596Z
- Reviewer: Codex /root/round21_marine_crusts (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The process-defined secondary resource and two scoped laboratory observations are supported. The record preserves culture carryover, unlike comparison chemistry, Fe/pH text–figure discrepancies, reconstructed copper inventories and lack of isolated-product or industrial evidence. No corrective finding identified in this assigned scope.

## Scope And Provenance

Complete assigned new PCB record and actual CREATE provenance; primary material, mechanism, controls, measurement and scale assessment.

Selection: One assigned maintained record from round21; all target fields inspected.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 55fd1947e80f67ec91dfe63e7bf15f72d822cefb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:waste-printed-circuit-boards | data/records/waste-printed-circuit-boards.yaml | maintained | Waste printed circuit boards |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:waste-printed-circuit-boards | Reviewer executed; Checked 1 record(s); 0 failed. Terminal exit 0 observed. |
| Native full checks | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round21-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 132.48s (0:02:12)<br>Checked 152 record(s); 0 failed.<br>Checked 169 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round21-final-require.log: Checked 152 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read completed receipt and all three terminal logs. /private/tmp/cmm-round21-final-history.log: Checked 169 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Process-defined secondary resource without inherited criticality

identity: supported. Targets: cmmmech:waste-printed-circuit-boards.

Waste boards represent a use/disposal-derived heterogeneous feed, distinct from whole electronic waste, removed tantalum capacitors, minerals and constituent elements. Primary material descriptions support the boundary. No external ontology mapping or criticality is asserted.

### Conditional culture-associated filtered copper mobilization

evidence: supported. Targets: cmmmech:waste-printed-circuit-boards.

Source-reported inoculated 1047 mg/L versus 413 mg/L at day seven is correctly kept as filtered solution concentration. Pre-culture growth/iron oxidation does not isolate PCB iron cycling; residue and filtration observations cannot establish extraction percentage, purified product or microbial necessity.

### Biogenic ferric regeneration connected to a PCB column

evidence: supported. Targets: cmmmech:waste-printed-circuit-boards.

Connected operational observations support the claimed system, while unlike column comparators do not establish an isolated microbial effect size. The record correctly preserves startup redox change, pH excursion, liquor replacement, reconstructed inventory and laboratory scale.

### Frozen target, actual CREATE and completed validation

provenance: supported. Targets: cmmmech:waste-printed-circuit-boards.

Canonical inspect captured target/schema/docs/history before scientific judgment. Record hash matches completed native gates. Actual history is valid against the trusted base; source primary metadata match cited publications.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/waste-printed-circuit-boards.yaml; Complete target and linked CREATE history | supports | All target fields and actual CREATE actor/timestamp/target linkage read; no material or organism CURIE or criticality designation asserted. |
| an | https://doi.org/10.3390/min11020224; Primary eight-page PDF; Methods 2.1–2.2, Results 3.1–3.3, rendered Figures 1–4 | supports | The author is Jinsung An (2021), despite the curator raw filename karwowska2021.pdf. Actual waste-computer fragments, seven-day triplicate inoculated versus 0K/DI assays, reported 1047 versus 413 mg/L filtered Cu endpoints, ICP-OES and retained-residue XRD/SEM-EDS support the qualified observation. |
| an_limits | https://doi.org/10.3390/min11020224; Methods 2.1–2.2; Results 3.2; rendered Figures 2–4 on pp.5–7 | partial | Preculture is distinct from PCB assay. Washing/carryover and board headspace are unresolved; 0K is not matched spent culture. Figure 2b generally places inoculated Fe below 0K despite conflicting prose. Figure 3 labels libethenite in 0K residue only. Figure 4 includes Cu and Pb-associated signals in inoculated residue and mismatches source prose panel references; absent phase assignment does not mean no Cu-bearing solid. |
| iglesias | https://doi.org/10.1016/j.mineng.2022.107471; Eight-page primary PDF; Methods 2.1–2.4, Results 3.1–3.2, discussion and Figures 1–6 | supports | RECILEC boards cut to mean 4.4 cm2, immobilized Rio Tinto community and separate regeneration/column configuration are described. Connected 100 g, 736 mL, initial 20 g/L Fe(III), 0.8 L/h circulation and 750 mL/h air are reported; 90% dissolution at day 25 uses reconstructed copper inventory. No isolated metal product is demonstrated. |
| iglesias_limits | https://doi.org/10.1016/j.mineng.2022.107471; Methods 2.2–2.4; rendered Figures 5–6 p.6 and discussion/conclusions p.7 | partial | Unconnected run differs in board mass, initial iron, feed grade and liquid inventory and also uses biogenic ferric. Figure 5 has initial redox lag and a pH excursion above 2; Figure 6 shows purges. Acid and fresh liquor are supplied; high ORP alone does not authenticate member-specific metabolism, universal toxicity tolerance or industrial deployment. |
| an_identity | https://api.crossref.org/works/10.3390/min11020224; Curator-retained Crossref record re-inspected and primary PDF front page | supports | DOI, title, author and 22 February 2021 publication agree; metadata contains no update-to entry, which is not an exhaustive notice audit. |
| iglesias_identity | https://api.crossref.org/works/10.1016/j.mineng.2022.107471; Curator-retained Crossref record re-inspected and primary PDF front page | supports | Title/authors/DOI and April 2022 volume agree. Primary front page distinguishes available-online 4 March 2022. Metadata contains no update-to entry, which does not establish universal absence of corrections. |
| search | /private/tmp/cmm-round21-pcb-independent/search.json; Six exact notice/identity/contrary-result queries and independent dedup receipt | context_only | First result sets identified no affecting corrective notice; additional experimental leads are not imported. Hidden/ignored-following text dedup found the maintained new root, history, source dossiers and cited raw materials, without a duplicate existing root in this bounded scope. |
| gates | /private/tmp/cmm-round21-gate-receipts.json; Completed batch/require/history receipt, terminal logs and frozen record hash | supports | 308 tests passed, 3 skipped; 152 records, 169 histories; all three parent gates exit 0. Reviewer independently read terminal logs and verified this target matches the gated hash. |

## Limits And Additional Notes

- No raw instrument data or independent reproduction of either experiment.
- KCTC4516 remains explicitly the primary paper-reported designation; no collection authority equivalence or taxon CURIE is asserted.
- The inoculated flask comparison retains residual-culture chemistry, unreported headspace/pH trajectory and source Fe/panel contradictions.
- Connected column comparisons differ in chemistry and inventory; source lacks replicated-column uncertainty and an independent initial Cu assay.
- Operational ORP, filtered concentration and reconstructed dissolution do not establish universal microbial necessity, an isolated product or industrial deployment.
- Correction/supplement searches cover first result sets only, not an exhaustive literature or notice index. Additional PCB recovery papers are deferred leads.
- Started-at is the recorded completion time of the second canonical inspect including history, before substantive assessment. The earlier target-only inspect also preceded assessment.
- Primary PDFs were acquired by the curator and independently read here; they are not described as fresh reviewer downloads. A differently named raw file was authenticated by its actual title/DOI.
- Batch/required-record/history commands were performed by the parent; this reviewer read their actual terminal receipts and did not silently re-run or invent them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T124602Z-waste-printed-circuit-boards-round21-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of waste printed circuit boards
started_at: '2026-10-11T12:42:56.425721Z'
finished_at: '2026-10-11T12:46:02.358596Z'
reviewer:
  identity: Codex /root/round21_marine_crusts
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different round21 PCB author created the target and history.
    This reviewer authored the separate crust record, independently inspected this
    PCB target, primary PDFs and rendered figures, ran named validation and live searches,
    and made no PCB target edits. Shared worktree and curator-acquired source files
    are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The process-defined secondary resource and two scoped laboratory observations
  are supported. The record preserves culture carryover, unlike comparison chemistry,
  Fe/pH text–figure discrepancies, reconstructed copper inventories and lack of isolated-product
  or industrial evidence. No corrective finding identified in this assigned scope.
source:
  git_revision: 55fd1947e80f67ec91dfe63e7bf15f72d822cefb
  state: working_tree
  inputs:
  - path: data/records/waste-printed-circuit-boards.yaml
    sha256: 1c4084c10b590efcbef858e3a37a74bbfc7bb1687c7635a0337ec3a09f870e93
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/waste-printed-circuit-boards/2026-10-11T124047Z-codex-fd23ae.yaml
    sha256: b5ee90ea4961aba93941dbde5f68872e19609831c2cb366f55b9d4455d5f94bb
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Complete assigned new PCB record and actual CREATE provenance; primary
    material, mechanism, controls, measurement and scale assessment.
  selection: One assigned maintained record from round21; all target fields inspected.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:waste-printed-circuit-boards
  exclusions:
  - target: Other corpus records, new follow-up assays and raw instrument data
    reason: Review covers the named record and its two accepted primary studies; new
      leads are not accepted without full review. Raw instrument datasets unavailable.
targets:
- target_id: cmmmech:waste-printed-circuit-boards
  path: data/records/waste-printed-circuit-boards.yaml
  label: Waste printed circuit boards
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-printed-circuit-boards.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/waste-printed-circuit-boards.yaml
  status: passed
  required: true
  summary: Reviewer executed; Checked 1 record(s); 0 failed. Terminal exit 0 observed.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round21-final-batch.log: uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 132.48s (0:02:12)

    Checked 152 record(s); 0 failed.

    Checked 169 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round21-final-require.log: Checked 152 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 55fd1947e80f67ec91dfe63e7bf15f72d822cefb
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed receipt and all
    three terminal logs. /private/tmp/cmm-round21-final-history.log: Checked 169 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/waste-printed-circuit-boards.yaml
  locator: Complete target and linked CREATE history
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: All target fields and actual CREATE actor/timestamp/target linkage read;
    no material or organism CURIE or criticality designation asserted.
  snapshot_sha256: 1c4084c10b590efcbef858e3a37a74bbfc7bb1687c7635a0337ec3a09f870e93
- evidence_id: an
  kind: primary_source
  reference: https://doi.org/10.3390/min11020224
  locator: Primary eight-page PDF; Methods 2.1–2.2, Results 3.1–3.3, rendered Figures
    1–4
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: The author is Jinsung An (2021), despite the curator raw filename karwowska2021.pdf.
    Actual waste-computer fragments, seven-day triplicate inoculated versus 0K/DI
    assays, reported 1047 versus 413 mg/L filtered Cu endpoints, ICP-OES and retained-residue
    XRD/SEM-EDS support the qualified observation.
  snapshot_sha256: b025c8a93a083257d5e2fe2621e12e1caccc8fcaf8bd5a7d6e1eadf29569ea1c
- evidence_id: an_limits
  kind: primary_source
  reference: https://doi.org/10.3390/min11020224
  locator: Methods 2.1–2.2; Results 3.2; rendered Figures 2–4 on pp.5–7
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: partial
  summary: Preculture is distinct from PCB assay. Washing/carryover and board headspace
    are unresolved; 0K is not matched spent culture. Figure 2b generally places inoculated
    Fe below 0K despite conflicting prose. Figure 3 labels libethenite in 0K residue
    only. Figure 4 includes Cu and Pb-associated signals in inoculated residue and
    mismatches source prose panel references; absent phase assignment does not mean
    no Cu-bearing solid.
  snapshot_sha256: b025c8a93a083257d5e2fe2621e12e1caccc8fcaf8bd5a7d6e1eadf29569ea1c
- evidence_id: iglesias
  kind: primary_source
  reference: https://doi.org/10.1016/j.mineng.2022.107471
  locator: Eight-page primary PDF; Methods 2.1–2.4, Results 3.1–3.2, discussion and
    Figures 1–6
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: RECILEC boards cut to mean 4.4 cm2, immobilized Rio Tinto community and
    separate regeneration/column configuration are described. Connected 100 g, 736
    mL, initial 20 g/L Fe(III), 0.8 L/h circulation and 750 mL/h air are reported;
    90% dissolution at day 25 uses reconstructed copper inventory. No isolated metal
    product is demonstrated.
  snapshot_sha256: 3309ff6eabdeaec90b66052598a8268a69e4db121a74b57ce36556265a8f69ef
- evidence_id: iglesias_limits
  kind: primary_source
  reference: https://doi.org/10.1016/j.mineng.2022.107471
  locator: Methods 2.2–2.4; rendered Figures 5–6 p.6 and discussion/conclusions p.7
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: partial
  summary: Unconnected run differs in board mass, initial iron, feed grade and liquid
    inventory and also uses biogenic ferric. Figure 5 has initial redox lag and a
    pH excursion above 2; Figure 6 shows purges. Acid and fresh liquor are supplied;
    high ORP alone does not authenticate member-specific metabolism, universal toxicity
    tolerance or industrial deployment.
  snapshot_sha256: 3309ff6eabdeaec90b66052598a8268a69e4db121a74b57ce36556265a8f69ef
- evidence_id: an_identity
  kind: database
  reference: https://api.crossref.org/works/10.3390/min11020224
  locator: Curator-retained Crossref record re-inspected and primary PDF front page
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: DOI, title, author and 22 February 2021 publication agree; metadata contains
    no update-to entry, which is not an exhaustive notice audit.
  snapshot_sha256: b32da69b67380d38b937fdc3b54e541b744b793a43efa51956f113532c278ef0
- evidence_id: iglesias_identity
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.mineng.2022.107471
  locator: Curator-retained Crossref record re-inspected and primary PDF front page
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: Title/authors/DOI and April 2022 volume agree. Primary front page distinguishes
    available-online 4 March 2022. Metadata contains no update-to entry, which does
    not establish universal absence of corrections.
  snapshot_sha256: 7a3d12a42819df806772452cc03a227cd97b312e7a6798a12520ee02b0001c66
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round21-pcb-independent/search.json
  locator: Six exact notice/identity/contrary-result queries and independent dedup
    receipt
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: context_only
  summary: First result sets identified no affecting corrective notice; additional
    experimental leads are not imported. Hidden/ignored-following text dedup found
    the maintained new root, history, source dossiers and cited raw materials, without
    a duplicate existing root in this bounded scope.
  snapshot_sha256: d8a40fe9d5ccd704c04e939e66510ddf046fc31bdc5619068652cbd04cc5b837
  search_scope: Specified scientific trees and curator-cited current raw directory
    only; hidden/ignored files included and symlinks followed. PDFs inspected separately.
    Unrelated directories excluded; no global absence claim. Live web queries inspect
    first returned result sets only.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round21-gate-receipts.json
  locator: Completed batch/require/history receipt, terminal logs and frozen record
    hash
  accessed_at: '2026-10-11T12:46:02.358596Z'
  support: supports
  summary: 308 tests passed, 3 skipped; 152 records, 169 histories; all three parent
    gates exit 0. Reviewer independently read terminal logs and verified this target
    matches the gated hash.
  snapshot_sha256: 80d63b110e213b06b5ff48a2ffb95f6234a571e23ca42ca53b6c7613c3745901
assessments:
- assessment_id: identity
  area: identity
  topic: Process-defined secondary resource without inherited criticality
  outcome: supported
  summary: Waste boards represent a use/disposal-derived heterogeneous feed, distinct
    from whole electronic waste, removed tantalum capacitors, minerals and constituent
    elements. Primary material descriptions support the boundary. No external ontology
    mapping or criticality is asserted.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - an
  - iglesias
  - search
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Waste electronic circuit-board feed, preserving board/source composition
      heterogeneity.
    evidence_ids:
    - record
    - an
    - iglesias
  - name: criticality
    value: Not asserted
    definition: Constituent metals do not confer a jurisdiction/list/edition designation
      on boards.
    evidence_ids:
    - record
- assessment_id: an_mechanism
  area: evidence
  topic: Conditional culture-associated filtered copper mobilization
  outcome: supported
  summary: Source-reported inoculated 1047 mg/L versus 413 mg/L at day seven is correctly
    kept as filtered solution concentration. Pre-culture growth/iron oxidation does
    not isolate PCB iron cycling; residue and filtration observations cannot establish
    extraction percentage, purified product or microbial necessity.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - an
  - an_limits
  dimensions:
  - name: organism_biomass
    value: Living A. ferrooxidans reported as KCTC4516 by the primary paper
    definition: Paper-reported collection designation is not promoted to a verified
      taxon/strain CURIE.
    evidence_ids:
    - record
    - an
  - name: substrate_conditions
    value: Washed, oven-dried waste-computer fragments below 1 cm2; 5 g; reported
      50 mL; 30 degrees C; seven days
    definition: Preculture shaking rate is not silently assigned to the final board
      assay; headspace and pH trajectory remain unresolved.
    evidence_ids:
    - record
    - an
    - an_limits
  - name: controls
    value: DI water and acidic 0K medium
    definition: No matched sterile spent-culture carryover control; acidic dissolution
      and residue precipitation contribute.
    evidence_ids:
    - record
    - an_limits
  - name: outcome
    value: Filtered ICP-OES copper; XRD/SEM-EDS of filter residue
    definition: Liquid concentration and phase-assigned residues are distinct from
      recovery yield and isolated metal.
    evidence_ids:
    - record
    - an
    - an_limits
- assessment_id: column_mechanism
  area: evidence
  topic: Biogenic ferric regeneration connected to a PCB column
  outcome: supported
  summary: Connected operational observations support the claimed system, while unlike
    column comparators do not establish an isolated microbial effect size. The record
    correctly preserves startup redox change, pH excursion, liquor replacement, reconstructed
    inventory and laboratory scale.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - iglesias
  - iglesias_limits
  dimensions:
  - name: organism_biomass
    value: Immobilized living Rio Tinto acidophilic consortium
    definition: Primarily named iron oxidizers and Acidiphilium-related heterotrophs;
      no member-specific causal attribution.
    evidence_ids:
    - record
    - iglesias
  - name: substrate_conditions
    value: Recycler boards; connected 100 g and 736 mL, initial 20 g/L Fe(III)
    definition: Separate bioreactor and column, mean board area 4.4 cm2, acid and
      liquor adjustments; no numerical connected-run temperature inferred.
    evidence_ids:
    - record
    - iglesias
  - name: controls
    value: Unconnected stored-biogenic-ferric column is chemically and materially
      unmatched
    definition: Different mass, liquid, ferric concentrations and reconstructed grade;
      not a matched sterile test.
    evidence_ids:
    - record
    - iglesias_limits
  - name: outcome_scale
    value: Source-reported 90% copper dissolution at 25 days; laboratory system
    definition: Inventory reconstructed from output/wash/residue fractions; proposed
      solvent extraction/electrowinning is not performed isolated-product recovery.
    evidence_ids:
    - record
    - iglesias
    - iglesias_limits
- assessment_id: provenance
  area: provenance
  topic: Frozen target, actual CREATE and completed validation
  outcome: supported
  summary: Canonical inspect captured target/schema/docs/history before scientific
    judgment. Record hash matches completed native gates. Actual history is valid
    against the trusted base; source primary metadata match cited publications.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - an_identity
  - iglesias_identity
  - gates
  dimensions: []
findings: []
actions: []
limitations:
- No raw instrument data or independent reproduction of either experiment.
- KCTC4516 remains explicitly the primary paper-reported designation; no collection
  authority equivalence or taxon CURIE is asserted.
- The inoculated flask comparison retains residual-culture chemistry, unreported headspace/pH
  trajectory and source Fe/panel contradictions.
- Connected column comparisons differ in chemistry and inventory; source lacks replicated-column
  uncertainty and an independent initial Cu assay.
- Operational ORP, filtered concentration and reconstructed dissolution do not establish
  universal microbial necessity, an isolated product or industrial deployment.
- Correction/supplement searches cover first result sets only, not an exhaustive literature
  or notice index. Additional PCB recovery papers are deferred leads.
notes:
- Started-at is the recorded completion time of the second canonical inspect including
  history, before substantive assessment. The earlier target-only inspect also preceded
  assessment.
- Primary PDFs were acquired by the curator and independently read here; they are
  not described as fresh reviewer downloads. A differently named raw file was authenticated
  by its actual title/DOI.
- Batch/required-record/history commands were performed by the parent; this reviewer
  read their actual terminal receipts and did not silently re-run or invent them.
tags:
- round21
- independent
- scientific-review
- secondary-resource
```
