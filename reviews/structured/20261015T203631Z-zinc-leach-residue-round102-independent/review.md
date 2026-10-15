# Independent scientific review of Zinc leach residue

- Review: 20261015T203631Z-zinc-leach-residue-round102-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T20:25:33.686315Z
- Finished UTC: 2026-10-15T20:36:31.338551Z
- Reviewer: codex /root/round100_vanadium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two separately bounded abiotic laboratory treatments of distinct zinc leach residues are supported, with copper-corrected residual rates, slag-loss denominators and source contradictions preserved.

## Scope And Provenance

Entire frozen owner, canonical CREATE and inline history, full accessible claim-bearing primary evidence, original figures/tables/supplements, identity authorities, source dossier and bounded correction/counterevidence/duplicate searches.

Selection: Parent-assigned independent scientific review after author freeze.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2a3bb043c4bd267a3d911d0e77b029c742689e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:zinc-leach-residue | data/records/zinc-leach-residue.yaml | maintained | Zinc leach residue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent primary-evidence assessment | passed | True | cmmmech:zinc-leach-residue | Exact frozen owner and accessible claim-bearing primary methods, results, figures, tables and supplements assessed with source limitations preserved. |
| Independent named record validation | passed | True | cmmmech:zinc-leach-residue | Three frozen resource owners checked; zero failed. This owner is one of those targets. |
| Completed coordinator batch check 1 | passed | True | cmmmech:zinc-leach-residue | Verified actual terminal receipt, trusted base, matching log hash and unchanged owner; not independently rerun by this reviewer. |
| Completed coordinator batch check 2 | passed | True | cmmmech:zinc-leach-residue | Verified actual terminal receipt, trusted base, matching log hash and unchanged owner; not independently rerun by this reviewer. |
| Completed coordinator batch check 3 | passed | True | cmmmech:zinc-leach-residue | Verified actual terminal receipt, trusted base, matching log hash and unchanged owner; not independently rerun by this reviewer. |
| Completed coordinator batch check 4 | passed | True | cmmmech:zinc-leach-residue | Verified actual terminal receipt, trusted base, matching log hash and unchanged owner; not independently rerun by this reviewer. |

## Scientific And Domain Assessments

### Feed identity and study separation

identity: supported. Targets: cmmmech:zinc-leach-residue.

The secondary-resource identity is appropriate.

Hunan and Yunnan residues are industrially generated mixed solids with separate chemistry, rather than pure zinc ferrite or zinc metal. The owner retains the Hunan residue at 17.30 wt.% Zn and 25.20 wt.% Fe, excluding the calcine arm at 61.70 wt.% Zn and 11.10 wt.% Fe. Wang feed values of 14.51 wt.% Zn, 21.34 wt.% Fe and 8.70 wt.% S are separately anchored.

### Copper-assisted leaching and residual-solid denominator

quantity: supported. Targets: cmmmech:zinc-leach-residue.

The matched comparison is supported without becoming a purified-product yield.

Zhang reports 92.82% versus 32.82% at 60 C, 100 g/L H2SO4, 20 mL/g and 60 min, with 21.60% copper or no copper. The 4 mL solution in 50 mL tubes, 240 rpm protocol and centrifugation, washing and freeze-drying are explicit. Equation 2 deducts estimated unreacted copper from weighed solids; 25.20% and 62.34% residual rates do not close a waste balance. Figure 4/Table 1 retain the reagent tradeoff between 90.47% and 96.30%. Negative pH values are censored at zero. Replication, uncertainty and the molecular explanation borrowed from pure-ferrite work remain qualified.

### Smelting conditions, metric and phase observations

quantity: supported. Targets: cmmmech:zinc-leach-residue.

The supported laboratory arm is correctly limited to slag depletion and observed phase changes.

Wang uses dry air at 300 mL/min, a 10 K/min ramp, 17.5 wt.% anthracite and 1623 K for 90 min; zero-minute holds include heating. Equation 2 divides the initial-mixture zinc absent from slag by initial-mixture zinc. The 99.13% and 0.22 wt.% values agree with the source, but no collected gas/dust mass, purity or complete balance is given. EPMA retains upper/lower heterogeneity and residual ZnS–FeS. The proposed oxygen and volatilization pathway remains interpretation.

### Contradictions and less favorable results

evidence: supported. Targets: cmmmech:zinc-leach-residue.

The record preserves source conflicts rather than choosing favorable labels.

Methods list 1473–1623 K, whereas Figure 6/introduction use 1523–1673 K. Figure 7a plots 10.41% at 1323 K and 25.22% at 1473 K; Section 3.2 instead assigns 10.41% to 1473 K. Equation 1 liquid-assay units and error-bar/replicate definitions remain unclear. TCLP values of 960.6 versus 29.9 mg/L, and the 15 wt.% anthracite arm at 338.4 mg/L, retain the reported assay scope without compliance or zero-toxicity inference. The 1373 K desulfurization sequence and iron product lack a separately traceable complete protocol/product characterization.

### Microbial, criticality and deployment boundaries

scope: supported. Targets: cmmmech:zinc-leach-residue.

No unsupported biological or industrial claim is introduced.

Both mechanisms are explicitly abiotic. Neither industrial feed origin nor laboratory furnace treatment establishes deployment. No jurisdiction/list/edition or constituent-element criticality is inherited. The deferred 2017 microbial paper is not treated as evidence.

### Revision, provenance and review independence

provenance: supported. Targets: cmmmech:zinc-leach-residue.

Frozen working changes, independent scope and actual executions are explicit.

Native inspect preceded judgment. Owner, history, paired dossier and schema hashes were rechecked at final drafting. No scientific owner edit was made by this reviewer. Named validation was independently run; four whole-repository checks were included only after verifying the coordinator terminal receipt and log hash. No acceptance was assigned to the reviewer own pascoite/navajoite records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/zinc-leach-residue.yaml; Entire frozen owner captured by native inspect before judgment; exact SHA rechecked before final drafting. | supports | Identity, measurements, study boundaries and limitations agree with the primary evidence assessed. |
| history | history/records/zinc-leach-residue/2026-10-15T202455Z-codex-bbd011.yaml; Canonical CREATE event, inline history and linked history_refs independently read. | supports | Actual GPT-6 curator, target, timestamp and described additions agree. Canonical and inline events remain distinct. |
| dossier | research/sources/round102-zinc/20261015T202456Z-source-investigation.md; Paired source-investigation JSON/Markdown, acquisition receipts, checksums, prior reuse and access limits. | supports | Curator provenance is explicit and does not constitute independent replication or acceptance. |
| named | uv run --locked cmmmech validate data/records/zinc-leach-residue.yaml data/records/uranium-mine-tailings.yaml data/records/carbonatite-associated-rare-earth-ore.yaml; /private/tmp/cmm-round102-vanadium-research/independent-reviews/named-validation.log | supports | Independently executed named validation checked all three assigned resources with zero failures. |
| search | Independent bounded DOI/title correction, retraction and duplicate searches; /private/tmp/cmm-round102-vanadium-research/independent-reviews/search-observations.json; /private/tmp/cmm-round102-vanadium-research/independent-reviews/dedup.json | context_only | No affecting formal notice surfaced in the bounded returned sets. Source conflicts are preserved. Exact queries, primary URLs and raw-output hashes are retained externally. |
| zhang | https://doi.org/10.12034/j.issn.1009-606X.223327; Complete eight-page Chinese original with English abstract; Sections 2-4, Figures 1-8, Table 1. All pages visually inspected in rendered contact sheets; methods and numbers independently text checked. | supports | The residue arm, reagent copper, matched no-copper control and copper-corrected residual mass definition agree with the owner. Calcine is a distinct feed and its numerical results are excluded. |
| wang | https://doi.org/10.1016/S1003-6326(26)67069-0; Complete thirteen-page official PDF; Sections 2-4, Tables 1-2 and Figures 1-12. All pages independently viewed; Figure 7a labels and main prose directly compared. | supports | The common1623 K/90 min/17.5 wt.% arm is traceable. Equation 2 counts Zn absent from slag, not collected product. Temperature conflicts, residual heterogeneity, TCLP scope and untraceable lower-temperature proposal remain explicit. |
| batch | /private/tmp/cmm-round102-final-gates.json; Completed coordinator receipt; /private/tmp/cmm-round102-final-gates.log SHA256 5ee1c9e4474da08bc2b3ea0ff0316ffb5f9f5861ce2efcca816f9f3238a95b85 | supports | Four actual terminal zero exits, exact base, unchanged reviewed owners and log hash verified. The coordinator executed these suites; review persistence follows them. |

## Limits And Additional Notes

- No isolated zinc-product purity, gas/dust balance or industrial deployment is demonstrated by these studies.
- Wang temperature labels, chemical-phase assay units, replicate/error-bar definitions and the proposed 1373 K sequence need attributable original data or correction. Qualified current claims do not require invented reconciliation.
- Zhang residual-solid rates use an estimated copper subtraction; total-element ICP-OES and a prior pure-ferrite interpretation do not establish molecular causation throughout this mixed feed.
- Source-evidence follow-up: https://github.com/CultureBotAI/CMMMech/issues/377. The issue draft was independently checked; no corrective owner finding was supported. The separate microbial-source access gap remains issue 186.
- All claim-bearing original pages/figures/tables were inspected; experiments, chemical assays and off-gas analyses were not independently repeated.
- Native inspect began at the recorded start; final drafting timestamps and source hashes are actual. No supported corrective owner finding was identified or suppressed.
- Original PDFs, XML, assets and official identifier responses were acquired by the authors and independently inspected by this reviewer. Current bounded web correction and metadata searches and named validation were independently executed. Acquisition is not experimental replication.
- The coordinator source-gap issue drafts were independently assessed as evidence priorities rather than defects in deliberately qualified records. Carbonatite calculation-unit clarification was additionally recommended. No author contact or Git/GitHub mutation was performed by this reviewer.
- This review does not claim native-review checks before persistence, exhaustive literature absence, raw experimental replication or universal industrial performance. Coordinator full-suite executions are attributed explicitly.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T203631Z-zinc-leach-residue-round102-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Zinc leach residue
started_at: '2026-10-15T20:25:33.686315Z'
finished_at: '2026-10-15T20:36:31.338551Z'
reviewer:
  identity: codex /root/round100_vanadium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The root coordinator authored this resource. I authored only
    pascoite/navajoite in this batch and independently assessed the frozen zinc owner
    and primary originals without editing them.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Two separately bounded abiotic laboratory treatments of distinct zinc leach
  residues are supported, with copper-corrected residual rates, slag-loss denominators
  and source contradictions preserved.
source:
  git_revision: 1c2a3bb043c4bd267a3d911d0e77b029c742689e
  state: working_tree
  inputs:
  - path: data/records/zinc-leach-residue.yaml
    sha256: ea520360db699961992304f933eb8dd4225eab72ceb02148941394aab846511d
    role: target
  - path: history/records/zinc-leach-residue/2026-10-15T202455Z-codex-bbd011.yaml
    sha256: ab5e01c9abb8d6986cb62fbb9cfeea321b073e1c6fe452f45dc222f923b07598
    role: context
  - path: research/sources/round102-zinc/20261015T202456Z-source-investigation.json
    sha256: 23123ea2013c8beb3b2d6950be74aa13085395f9971bcaaa1947f1589f28bb5c
    role: context
  - path: research/sources/round102-zinc/20261015T202456Z-source-investigation.md
    sha256: 971b782ed8b163bca04fbbd4ba48b9e7331399e5ef8985db156dfce646da9a7b
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen owner, canonical CREATE and inline history, full accessible
    claim-bearing primary evidence, original figures/tables/supplements, identity
    authorities, source dossier and bounded correction/counterevidence/duplicate searches.
  selection: Parent-assigned independent scientific review after author freeze.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:zinc-leach-residue
targets:
- target_id: cmmmech:zinc-leach-residue
  path: data/records/zinc-leach-residue.yaml
  label: Zinc leach residue
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/zinc-leach-residue.yaml
    role: maintained_record
checks:
- check_id: science
  name: Independent primary-evidence assessment
  required: true
  status: passed
  summary: Exact frozen owner and accessible claim-bearing primary methods, results,
    figures, tables and supplements assessed with source limitations preserved.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - history
  - search
- check_id: named
  name: Independent named record validation
  required: true
  status: passed
  command: uv run --locked cmmmech validate data/records/zinc-leach-residue.yaml data/records/uranium-mine-tailings.yaml
    data/records/carbonatite-associated-rare-earth-ore.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Three frozen resource owners checked; zero failed. This owner is one of
    those targets.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - named
- check_id: batch1
  name: Completed coordinator batch check 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual terminal receipt, trusted base, matching log hash and unchanged
    owner; not independently rerun by this reviewer.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed coordinator batch check 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual terminal receipt, trusted base, matching log hash and unchanged
    owner; not independently rerun by this reviewer.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed coordinator batch check 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 1c2a3bb043c4bd267a3d911d0e77b029c742689e
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual terminal receipt, trusted base, matching log hash and unchanged
    owner; not independently rerun by this reviewer.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed coordinator batch check 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual terminal receipt, trusted base, matching log hash and unchanged
    owner; not independently rerun by this reviewer.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/zinc-leach-residue.yaml
  locator: Entire frozen owner captured by native inspect before judgment; exact SHA
    rechecked before final drafting.
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: Identity, measurements, study boundaries and limitations agree with the
    primary evidence assessed.
  snapshot_sha256: ea520360db699961992304f933eb8dd4225eab72ceb02148941394aab846511d
- evidence_id: history
  kind: record_content
  reference: history/records/zinc-leach-residue/2026-10-15T202455Z-codex-bbd011.yaml
  locator: Canonical CREATE event, inline history and linked history_refs independently
    read.
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: Actual GPT-6 curator, target, timestamp and described additions agree.
    Canonical and inline events remain distinct.
  snapshot_sha256: ab5e01c9abb8d6986cb62fbb9cfeea321b073e1c6fe452f45dc222f923b07598
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round102-zinc/20261015T202456Z-source-investigation.md
  locator: Paired source-investigation JSON/Markdown, acquisition receipts, checksums,
    prior reuse and access limits.
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: Curator provenance is explicit and does not constitute independent replication
    or acceptance.
  snapshot_sha256: 971b782ed8b163bca04fbbd4ba48b9e7331399e5ef8985db156dfce646da9a7b
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/zinc-leach-residue.yaml
    data/records/uranium-mine-tailings.yaml data/records/carbonatite-associated-rare-earth-ore.yaml
  locator: /private/tmp/cmm-round102-vanadium-research/independent-reviews/named-validation.log
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: Independently executed named validation checked all three assigned resources
    with zero failures.
  snapshot_sha256: 10c82c02ccbb2c9d0b1dd25497ab97be593452ac7d5d9b18fe4b18777cbf7058
- evidence_id: search
  kind: search
  reference: Independent bounded DOI/title correction, retraction and duplicate searches
  locator: /private/tmp/cmm-round102-vanadium-research/independent-reviews/search-observations.json;
    /private/tmp/cmm-round102-vanadium-research/independent-reviews/dedup.json
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: context_only
  summary: No affecting formal notice surfaced in the bounded returned sets. Source
    conflicts are preserved. Exact queries, primary URLs and raw-output hashes are
    retained externally.
  snapshot_sha256: 3cb23f8546bf17a70126eb73d274c115053c0b85b5187a58612a8acd5a940eda
  search_scope: First returned web result sets, no exhaustive pagination. rg --no-ignore
    --hidden --follow covered data/research/reviews/history/docs plus the two exact
    raw-source roots and all261 issue title/body entries in the supplied snapshot.
    Author transitive historical raw-search receipts were separately inspected, not
    independently rerun. Issue comments and machine-wide files were outside this absence
    boundary.
- evidence_id: zhang
  kind: primary_source
  reference: https://doi.org/10.12034/j.issn.1009-606X.223327
  locator: Complete eight-page Chinese original with English abstract; Sections 2-4,
    Figures 1-8, Table 1. All pages visually inspected in rendered contact sheets;
    methods and numbers independently text checked.
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: The residue arm, reagent copper, matched no-copper control and copper-corrected
    residual mass definition agree with the owner. Calcine is a distinct feed and
    its numerical results are excluded.
  snapshot_sha256: e3604fa7ab2fe741b078e2c5e93b239484a7d0576539c0777ba809afe12e1c69
- evidence_id: wang
  kind: primary_source
  reference: https://doi.org/10.1016/S1003-6326(26)67069-0
  locator: Complete thirteen-page official PDF; Sections 2-4, Tables 1-2 and Figures
    1-12. All pages independently viewed; Figure 7a labels and main prose directly
    compared.
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: The common1623 K/90 min/17.5 wt.% arm is traceable. Equation 2 counts Zn
    absent from slag, not collected product. Temperature conflicts, residual heterogeneity,
    TCLP scope and untraceable lower-temperature proposal remain explicit.
  snapshot_sha256: f2d43a40e21f734dca8d5d72698c44a56400d9b9a887f9b279991071d725b622
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round102-final-gates.json
  locator: Completed coordinator receipt; /private/tmp/cmm-round102-final-gates.log
    SHA256 5ee1c9e4474da08bc2b3ea0ff0316ffb5f9f5861ce2efcca816f9f3238a95b85
  accessed_at: '2026-10-15T20:36:31.338551Z'
  support: supports
  summary: Four actual terminal zero exits, exact base, unchanged reviewed owners
    and log hash verified. The coordinator executed these suites; review persistence
    follows them.
  snapshot_sha256: 27bacebde96bb1b572897eb3ca5ed83263195f774c2871a4d734f18a2d5d46fe
assessments:
- assessment_id: identity
  area: identity
  topic: Feed identity and study separation
  outcome: supported
  summary: The secondary-resource identity is appropriate.
  details: Hunan and Yunnan residues are industrially generated mixed solids with
    separate chemistry, rather than pure zinc ferrite or zinc metal. The owner retains
    the Hunan residue at 17.30 wt.% Zn and 25.20 wt.% Fe, excluding the calcine arm
    at 61.70 wt.% Zn and 11.10 wt.% Fe. Wang feed values of 14.51 wt.% Zn, 21.34 wt.%
    Fe and 8.70 wt.% S are separately anchored.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - zhang
  - wang
- assessment_id: copper
  area: quantity
  topic: Copper-assisted leaching and residual-solid denominator
  outcome: supported
  summary: The matched comparison is supported without becoming a purified-product
    yield.
  details: Zhang reports 92.82% versus 32.82% at 60 C, 100 g/L H2SO4, 20 mL/g and
    60 min, with 21.60% copper or no copper. The 4 mL solution in 50 mL tubes, 240
    rpm protocol and centrifugation, washing and freeze-drying are explicit. Equation
    2 deducts estimated unreacted copper from weighed solids; 25.20% and 62.34% residual
    rates do not close a waste balance. Figure 4/Table 1 retain the reagent tradeoff
    between 90.47% and 96.30%. Negative pH values are censored at zero. Replication,
    uncertainty and the molecular explanation borrowed from pure-ferrite work remain
    qualified.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - zhang
- assessment_id: smelting
  area: quantity
  topic: Smelting conditions, metric and phase observations
  outcome: supported
  summary: The supported laboratory arm is correctly limited to slag depletion and
    observed phase changes.
  details: Wang uses dry air at 300 mL/min, a 10 K/min ramp, 17.5 wt.% anthracite
    and 1623 K for 90 min; zero-minute holds include heating. Equation 2 divides the
    initial-mixture zinc absent from slag by initial-mixture zinc. The 99.13% and
    0.22 wt.% values agree with the source, but no collected gas/dust mass, purity
    or complete balance is given. EPMA retains upper/lower heterogeneity and residual
    ZnS–FeS. The proposed oxygen and volatilization pathway remains interpretation.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - wang
- assessment_id: conflicts
  area: evidence
  topic: Contradictions and less favorable results
  outcome: supported
  summary: The record preserves source conflicts rather than choosing favorable labels.
  details: Methods list 1473–1623 K, whereas Figure 6/introduction use 1523–1673 K.
    Figure 7a plots 10.41% at 1323 K and 25.22% at 1473 K; Section 3.2 instead assigns
    10.41% to 1473 K. Equation 1 liquid-assay units and error-bar/replicate definitions
    remain unclear. TCLP values of 960.6 versus 29.9 mg/L, and the 15 wt.% anthracite
    arm at 338.4 mg/L, retain the reported assay scope without compliance or zero-toxicity
    inference. The 1373 K desulfurization sequence and iron product lack a separately
    traceable complete protocol/product characterization.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - wang
- assessment_id: scope
  area: scope
  topic: Microbial, criticality and deployment boundaries
  outcome: supported
  summary: No unsupported biological or industrial claim is introduced.
  details: Both mechanisms are explicitly abiotic. Neither industrial feed origin
    nor laboratory furnace treatment establishes deployment. No jurisdiction/list/edition
    or constituent-element criticality is inherited. The deferred 2017 microbial paper
    is not treated as evidence.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - zhang
  - wang
- assessment_id: provenance
  area: provenance
  topic: Revision, provenance and review independence
  outcome: supported
  summary: Frozen working changes, independent scope and actual executions are explicit.
  details: Native inspect preceded judgment. Owner, history, paired dossier and schema
    hashes were rechecked at final drafting. No scientific owner edit was made by
    this reviewer. Named validation was independently run; four whole-repository checks
    were included only after verifying the coordinator terminal receipt and log hash.
    No acceptance was assigned to the reviewer own pascoite/navajoite records.
  target_ids:
  - cmmmech:zinc-leach-residue
  evidence_ids:
  - owner
  - history
  - dossier
  - named
  - batch
findings: []
actions: []
limitations:
- No isolated zinc-product purity, gas/dust balance or industrial deployment is demonstrated
  by these studies.
- Wang temperature labels, chemical-phase assay units, replicate/error-bar definitions
  and the proposed 1373 K sequence need attributable original data or correction.
  Qualified current claims do not require invented reconciliation.
- Zhang residual-solid rates use an estimated copper subtraction; total-element ICP-OES
  and a prior pure-ferrite interpretation do not establish molecular causation throughout
  this mixed feed.
- 'Source-evidence follow-up: https://github.com/CultureBotAI/CMMMech/issues/377.
  The issue draft was independently checked; no corrective owner finding was supported.
  The separate microbial-source access gap remains issue 186.'
- All claim-bearing original pages/figures/tables were inspected; experiments, chemical
  assays and off-gas analyses were not independently repeated.
notes:
- Native inspect began at the recorded start; final drafting timestamps and source
  hashes are actual. No supported corrective owner finding was identified or suppressed.
- Original PDFs, XML, assets and official identifier responses were acquired by the
  authors and independently inspected by this reviewer. Current bounded web correction
  and metadata searches and named validation were independently executed. Acquisition
  is not experimental replication.
- The coordinator source-gap issue drafts were independently assessed as evidence
  priorities rather than defects in deliberately qualified records. Carbonatite calculation-unit
  clarification was additionally recommended. No author contact or Git/GitHub mutation
  was performed by this reviewer.
- This review does not claim native-review checks before persistence, exhaustive literature
  absence, raw experimental replication or universal industrial performance. Coordinator
  full-suite executions are attributed explicitly.
```
