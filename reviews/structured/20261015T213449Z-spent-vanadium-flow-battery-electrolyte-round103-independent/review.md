# Independent scientific review of Spent vanadium-flow-battery electrolyte

- Review: 20261015T213449Z-spent-vanadium-flow-battery-electrolyte-round103-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T21:20:38.891746Z
- Finished UTC: 2026-10-15T21:34:49.440248Z
- Reviewer: codex /root/round100_vanadium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two distinct used-electrolyte feeds and abiotic treatments are supported: reported pilot ammonium-metavanadate product and laboratory electrochemical function regeneration. The record preserves assay denominators, hardware/compartment differences, source contradictions and scale limits.

## Scope And Provenance

Entire frozen resource, inline/canonical CREATE history, paired dossier and complete primary originals with every original page, figure and table independently inspected. Includes bounded source notice/identity and hidden/ignored duplicate checks.

Selection: Parent-assigned independent scientific review after author freeze.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 44d5b468519eb862b32ef54bf7c066bc0f79ba62.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:spent-vanadium-flow-battery-electrolyte | data/records/spent-vanadium-flow-battery-electrolyte.yaml | maintained | Spent vanadium flow-battery electrolyte |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent primary-evidence assessment | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | Both full primary originals, exact frozen owner and all claim-bearing methods/figures/tables checked; supported limitations retained. |
| Independent named record validation | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | One frozen owner checked, zero failed; independently executed by this reviewer. |
| Completed coordinator batch gate 1 | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | Verified terminal coordinator receipt/log and unchanged frozen review inputs; execution attributed to coordinator. |
| Completed coordinator batch gate 2 | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | Verified terminal coordinator receipt/log and unchanged frozen review inputs; execution attributed to coordinator. |
| Completed coordinator batch gate 3 | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | Verified terminal coordinator receipt/log and unchanged frozen review inputs; execution attributed to coordinator. |
| Completed coordinator batch gate 4 | passed | True | cmmmech:spent-vanadium-flow-battery-electrolyte | Verified terminal coordinator receipt/log and unchanged frozen review inputs; execution attributed to coordinator. |

## Scientific And Domain Assessments

### Used-resource identity and feed boundaries

identity: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

The secondary-resource identity is appropriate.

Company-supplied failed positive and negative sulfuric-acid electrolytes are separate from the purchased electrolyte subsequently cycled below 50% rated capacity in a laboratory cell. Neither is elemental vanadium, fresh electrolyte, spent catalyst or solid battery scrap. The 2024 citation to 2016 is contextual, not a second measurement of its pilot batch.

### Abiotic oxidation and precipitation conditions

evidence: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

Laboratory oxidation and precipitation are supported with explicit analytical limits.

Yang Table 1 distinguishes positive 1.28 M total V (0.76 M V(V), 0.52 M V(IV)), 1.75 M H2SO4 from negative 1.53 M V(III)/total V and 1.82 M acid. Separate 500-mL room-temperature trials selected 1:0.20 and 1:0.40 V:chlorate molar ratios. Printed zero low-valent-V cells lack detection limits. Methods support pH 8.0-8.5, 50-60 C, 100-120 min, filtration and 65 C vacuum drying for 4 h, without supplied replication, oxidation duration or complete balance.

### V2O5-equivalent concentration and product yield

quantity: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

The record does not turn liquid removal into a measured isolated-product yield.

Figure 2 labels V2O5 g/L and nearby prose gives residual V on that basis. K is the added ammonium-sulfate mass divided by solution V expressed as V2O5. Table 4 at nominal 26.35 g/L, pH 8, 50 C, K=1.2 gives 0.26 g/L and 99.01% at 120/140 min; 80 min gives 0.65 g/L and 97.53%. Percentages match concentration differences. Section 3 separately reports a 1-m3 positive-feed pilot batch, 148.30 kg white NH4VO3-labelled powder and 99.58% dry-basis content. No supplied product diffraction or explicit NH4VO3 assay establishes crystallographic purity or independent specification compliance.

### Electrochemical regeneration and comparison arms

evidence: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

Functional reuse is supported at laboratory scale.

Peng purchased nominal 1.7 M V of average valence +3.5 in 3 M acid, then cycled it below 50% rated capacity in a 28-cm2 cell with 4.2-mm graphite felt and Nafion 212. Figures 3-7 compare new, aged and regenerated fluid. At 100 mA/cm2, approximately 1200/500/900 mAh support the 75% proportion-arm result. Sequential cycles are not independent replicates. Direct regeneration sacrifices the positive-compartment state; acid electrolysis uses 100 mL 3 M H2SO4 in that compartment and replaces corroded hardware/felt; 5-A asymmetric treatment to less than 0.01-V difference took about 5 h for 100 mL. All are abiotic.

### Conflicting values and limits on inference

evidence: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

Source disagreements are retained accurately.

Yang conclusion pH 2.0-2.5 conflicts with methods/results/Figure 3/abstract at 8.0-8.5; 80-120 versus 100-120 min should not produce a universal 99% endpoint. Peng Results assign direct/acid restoration 93%/92%, while abstract/conclusion reverse them; the asymmetric paragraph also misnames acid electrolysis. Stated 1190 mAh differs from 2238 mA times 0.5 h = 1119 mAh. Fifty-fold UV-visible dilution is explicit, so reported assay concentrations are not undiluted inventory. No guessed correction is introduced.

### Criticality, biology and deployment

scope: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

Unsupported inherited claims are absent.

No jurisdiction/list/edition claim is made; no element criticality is assigned to the used liquid. No organism or microbial necessity was tested. Yang supports a reported pilot batch, not continuous commercial deployment. Peng supports short changing-current laboratory tests, not durable whole-feed recycling or recovered metal yield. High coulombic efficiency is not equivalent to retained capacity or energy efficiency.

### Exact reviewed state and reviewer independence

provenance: supported. Targets: cmmmech:spent-vanadium-flow-battery-electrolyte.

Frozen bytes and independent work are explicit.

Successful native inspect preceded owner judgment, and final input hashes were verified. The author downloaded the originals; this reviewer independently inspected their bytes/pages and executed bounded source searches and named validation. No owner/history correction was made. Batch gate results are included only after actual coordinator receipt/log verification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/spent-vanadium-flow-battery-electrolyte.yaml; Whole frozen owner captured with successful native inspect before judging; source hashes rechecked at final drafting. | supports | Exact resource identity, mechanism claims, study-specific measurements and limitations agree with the inspected originals. |
| history | history/records/spent-vanadium-flow-battery-electrolyte/2026-10-15T211729Z-codex-4ea0f7.yaml; Canonical CREATE session, target, actor, summary/details and distinct inline event/history_refs. | supports | Actual GPT-6 attribution, timestamps and described curation agree. The sidecar is creation provenance, not scientific review. |
| dossier | research/sources/round103-electrolyte/20261015T211843Z-source-investigation.md; Paired JSON/Markdown, acquisition receipts and all 27 listed raw artifact hashes independently rechecked. | supports | Author acquisition was reused honestly. DOI publisher identities, source licenses and unavailable raw assay/deposit limits remain explicit. |
| yang | https://doi.org/10.16085/j.issn.1000-6613.2016.09.047; Full five-page Chinese publisher original with English abstract; Sections 1.1-2.3, Figures 1-5, Tables 1-5, Section 3 pilot product and conclusion item 2. All five rendered original pages viewed. | supports | Defined company-supplied positive/negative feeds, chemical oxidation/precipitation and reported pilot solid are supported with pH, analytical-basis and balance limits. |
| peng | https://doi.org/10.7513/j.issn.1004-7638.2024.03.002; Full seven-page Chinese publisher original with English abstract; Sections 1.1-1.3 and 2.1-2.2, Figures 1-7, Tables 1-2 and conclusion. All seven rendered original pages viewed. | supports | Laboratory-aged feed and four distinct protocols are supported; conflicting arm percentages, charge arithmetic and different hardware/compartment treatment are correctly preserved. |
| search | Independent exact-source correction/retraction and duplicate checks; /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/search-observations.json; /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/dedup.json | context_only | No affecting formal notice surfaced in bounded returned results. Original source conflicts remain rather than an invented correction. |
| named | uv run --locked cmmmech validate data/records/spent-vanadium-flow-battery-electrolyte.yaml; /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/named-validation.log | supports | Independent validation passed: one checked and zero failed. |
| batch | /private/tmp/cmm-round103-final-gates.json; Actual terminal coordinator receipt and log /private/tmp/cmm-round103-final-gates.log SHA256 f4f7cd3987bee8509a9d87fce2c0ac9fcdb731dc67a221a8b06b6c0052d1ed1a | supports | Final batch commands each returned zero; exact base, input state and log hash verified. These suites were executed by the coordinator, not independently rerun. |

## Limits And Additional Notes

- The 2016 product is author-reported pilot powder with incomplete assay, diffraction, detection-limit, replicate and total-element balance evidence; no independently measured overall yield or compliance is asserted.
- The 2016 pH/time/concentration-basis discrepancies need attributable clarification before wider process transfer.
- The 2024 percentage-to-arm assignments and 1190/1119-mAh mismatch remain unresolved; raw replicate data and independent uncertainty estimates were not supplied.
- Hardware replacement, compartment sacrifice and absent durable whole-feed accounting limit comparison and scale inference; no recovery percentage is inferred from coulombic efficiency.
- Both full originals and all printed figures/tables were inspected, but experiments and chemical assays were not independently repeated. Publisher zero attachments is a bounded site observation, not proof no unpublished supplement exists.
- No supported corrective owner finding was identified. Qualified source gaps remain research follow-ups rather than defects to manufacture.
- An initial inspector command contained a mistyped sidecar path and failed before owner judgment. The path was corrected to the author-confirmed sidecar, successful inspect captured the exact inputs, and only that successful capture is used here.
- No scientific self-acceptance of this reviewer autunite/torbernite owners, Git/GitHub mutation, author contact, or automatic criticality/deployment claim occurred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T213449Z-spent-vanadium-flow-battery-electrolyte-round103-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Spent vanadium-flow-battery electrolyte
started_at: '2026-10-15T21:20:38.891746Z'
finished_at: '2026-10-15T21:34:49.440248Z'
reviewer:
  identity: codex /root/round100_vanadium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this resource. I authored only autunite/torbernite
    in this round and independently assessed the frozen resource and original studies
    without editing this owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Two distinct used-electrolyte feeds and abiotic treatments are supported:
  reported pilot ammonium-metavanadate product and laboratory electrochemical function
  regeneration. The record preserves assay denominators, hardware/compartment differences,
  source contradictions and scale limits.'
source:
  git_revision: 44d5b468519eb862b32ef54bf7c066bc0f79ba62
  state: working_tree
  inputs:
  - path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    sha256: e66884747bdbd2f2a51a9e04b4aa33e747b26948fedba9eda9be421c5d84a739
    role: target
  - path: history/records/spent-vanadium-flow-battery-electrolyte/2026-10-15T211729Z-codex-4ea0f7.yaml
    sha256: ce2980528f07a6f213b81bc6ddfa5e0a5f6a6230d83464246989748ed5da47c3
    role: context
  - path: research/sources/round103-electrolyte/20261015T211843Z-source-investigation.json
    sha256: a1860b3707e692050d6d30cae49495510db0770a3a90b8b2257f0547f76a3b80
    role: context
  - path: research/sources/round103-electrolyte/20261015T211843Z-source-investigation.md
    sha256: b9db07aa202dc873568d2d34d90f01017d898719ae5ea791e7b9ce3ef14702c5
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen resource, inline/canonical CREATE history, paired dossier
    and complete primary originals with every original page, figure and table independently
    inspected. Includes bounded source notice/identity and hidden/ignored duplicate
    checks.
  selection: Parent-assigned independent scientific review after author freeze.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
targets:
- target_id: cmmmech:spent-vanadium-flow-battery-electrolyte
  path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
  label: Spent vanadium flow-battery electrolyte
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/spent-vanadium-flow-battery-electrolyte.yaml
    role: maintained_record
checks:
- check_id: science
  name: Independent primary-evidence assessment
  required: true
  status: passed
  summary: Both full primary originals, exact frozen owner and all claim-bearing methods/figures/tables
    checked; supported limitations retained.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
  - peng
  - search
- check_id: named
  name: Independent named record validation
  required: true
  status: passed
  command: uv run --locked cmmmech validate data/records/spent-vanadium-flow-battery-electrolyte.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One frozen owner checked, zero failed; independently executed by this reviewer.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - named
- check_id: batch1
  name: Completed coordinator batch gate 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified terminal coordinator receipt/log and unchanged frozen review inputs;
    execution attributed to coordinator.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed coordinator batch gate 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Verified terminal coordinator receipt/log and unchanged frozen review inputs;
    execution attributed to coordinator.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed coordinator batch gate 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 44d5b468519eb862b32ef54bf7c066bc0f79ba62
  exit_code: 0
  expected_exit_code: 0
  summary: Verified terminal coordinator receipt/log and unchanged frozen review inputs;
    execution attributed to coordinator.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed coordinator batch gate 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified terminal coordinator receipt/log and unchanged frozen review inputs;
    execution attributed to coordinator.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/spent-vanadium-flow-battery-electrolyte.yaml
  locator: Whole frozen owner captured with successful native inspect before judging;
    source hashes rechecked at final drafting.
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Exact resource identity, mechanism claims, study-specific measurements
    and limitations agree with the inspected originals.
  snapshot_sha256: e66884747bdbd2f2a51a9e04b4aa33e747b26948fedba9eda9be421c5d84a739
- evidence_id: history
  kind: record_content
  reference: history/records/spent-vanadium-flow-battery-electrolyte/2026-10-15T211729Z-codex-4ea0f7.yaml
  locator: Canonical CREATE session, target, actor, summary/details and distinct inline
    event/history_refs.
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Actual GPT-6 attribution, timestamps and described curation agree. The
    sidecar is creation provenance, not scientific review.
  snapshot_sha256: ce2980528f07a6f213b81bc6ddfa5e0a5f6a6230d83464246989748ed5da47c3
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round103-electrolyte/20261015T211843Z-source-investigation.md
  locator: Paired JSON/Markdown, acquisition receipts and all 27 listed raw artifact
    hashes independently rechecked.
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Author acquisition was reused honestly. DOI publisher identities, source
    licenses and unavailable raw assay/deposit limits remain explicit.
  snapshot_sha256: b9db07aa202dc873568d2d34d90f01017d898719ae5ea791e7b9ce3ef14702c5
- evidence_id: yang
  kind: primary_source
  reference: https://doi.org/10.16085/j.issn.1000-6613.2016.09.047
  locator: Full five-page Chinese publisher original with English abstract; Sections
    1.1-2.3, Figures 1-5, Tables 1-5, Section 3 pilot product and conclusion item
    2. All five rendered original pages viewed.
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Defined company-supplied positive/negative feeds, chemical oxidation/precipitation
    and reported pilot solid are supported with pH, analytical-basis and balance limits.
  snapshot_sha256: 3418860ee1e3c7366c540ed392f1f444e340be765fcebcb6cc02b5bf00326399
- evidence_id: peng
  kind: primary_source
  reference: https://doi.org/10.7513/j.issn.1004-7638.2024.03.002
  locator: Full seven-page Chinese publisher original with English abstract; Sections
    1.1-1.3 and 2.1-2.2, Figures 1-7, Tables 1-2 and conclusion. All seven rendered
    original pages viewed.
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Laboratory-aged feed and four distinct protocols are supported; conflicting
    arm percentages, charge arithmetic and different hardware/compartment treatment
    are correctly preserved.
  snapshot_sha256: 1e542492ac1f08d17e615f7fd3cdb50e90828c201d9b8b83d5095543b2573c25
- evidence_id: search
  kind: search
  reference: Independent exact-source correction/retraction and duplicate checks
  locator: /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/search-observations.json;
    /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/dedup.json
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: context_only
  summary: No affecting formal notice surfaced in bounded returned results. Original
    source conflicts remain rather than an invented correction.
  snapshot_sha256: 16c54ec31818cac5949c4857b19a1df427a25e6764658cee9c85adef81998915
  search_scope: English DOI and Chinese exact-title correction queries, first returned
    web result sets, no exhaustive pagination. rg --no-ignore --hidden --follow covered
    current WT data/research/reviews/history/local skills, the exact raw source root
    and provided open-issue title/body snapshot. Root fourteen historical raw-root
    search was inspected as author provenance, not independently rerun. No machine-wide
    or issue-comment/closed-issue absence claimed.
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/spent-vanadium-flow-battery-electrolyte.yaml
  locator: /private/tmp/cmm-round103-uranium-research/independent-electrolyte-review/named-validation.log
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: 'Independent validation passed: one checked and zero failed.'
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round103-final-gates.json
  locator: Actual terminal coordinator receipt and log /private/tmp/cmm-round103-final-gates.log
    SHA256 f4f7cd3987bee8509a9d87fce2c0ac9fcdb731dc67a221a8b06b6c0052d1ed1a
  accessed_at: '2026-10-15T21:34:49.440248Z'
  support: supports
  summary: Final batch commands each returned zero; exact base, input state and log
    hash verified. These suites were executed by the coordinator, not independently
    rerun.
  snapshot_sha256: ef3d0446342aee65fbc39d26d23478afef6891e4ef86fc083805c990b0f9f1c3
assessments:
- assessment_id: identity
  area: identity
  topic: Used-resource identity and feed boundaries
  outcome: supported
  summary: The secondary-resource identity is appropriate.
  details: Company-supplied failed positive and negative sulfuric-acid electrolytes
    are separate from the purchased electrolyte subsequently cycled below 50% rated
    capacity in a laboratory cell. Neither is elemental vanadium, fresh electrolyte,
    spent catalyst or solid battery scrap. The 2024 citation to 2016 is contextual,
    not a second measurement of its pilot batch.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
  - peng
- assessment_id: oxidation
  area: evidence
  topic: Abiotic oxidation and precipitation conditions
  outcome: supported
  summary: Laboratory oxidation and precipitation are supported with explicit analytical
    limits.
  details: Yang Table 1 distinguishes positive 1.28 M total V (0.76 M V(V), 0.52 M
    V(IV)), 1.75 M H2SO4 from negative 1.53 M V(III)/total V and 1.82 M acid. Separate
    500-mL room-temperature trials selected 1:0.20 and 1:0.40 V:chlorate molar ratios.
    Printed zero low-valent-V cells lack detection limits. Methods support pH 8.0-8.5,
    50-60 C, 100-120 min, filtration and 65 C vacuum drying for 4 h, without supplied
    replication, oxidation duration or complete balance.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
- assessment_id: precipitation_metric
  area: quantity
  topic: V2O5-equivalent concentration and product yield
  outcome: supported
  summary: The record does not turn liquid removal into a measured isolated-product
    yield.
  details: Figure 2 labels V2O5 g/L and nearby prose gives residual V on that basis.
    K is the added ammonium-sulfate mass divided by solution V expressed as V2O5.
    Table 4 at nominal 26.35 g/L, pH 8, 50 C, K=1.2 gives 0.26 g/L and 99.01% at 120/140
    min; 80 min gives 0.65 g/L and 97.53%. Percentages match concentration differences.
    Section 3 separately reports a 1-m3 positive-feed pilot batch, 148.30 kg white
    NH4VO3-labelled powder and 99.58% dry-basis content. No supplied product diffraction
    or explicit NH4VO3 assay establishes crystallographic purity or independent specification
    compliance.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
- assessment_id: regeneration
  area: evidence
  topic: Electrochemical regeneration and comparison arms
  outcome: supported
  summary: Functional reuse is supported at laboratory scale.
  details: Peng purchased nominal 1.7 M V of average valence +3.5 in 3 M acid, then
    cycled it below 50% rated capacity in a 28-cm2 cell with 4.2-mm graphite felt
    and Nafion 212. Figures 3-7 compare new, aged and regenerated fluid. At 100 mA/cm2,
    approximately 1200/500/900 mAh support the 75% proportion-arm result. Sequential
    cycles are not independent replicates. Direct regeneration sacrifices the positive-compartment
    state; acid electrolysis uses 100 mL 3 M H2SO4 in that compartment and replaces
    corroded hardware/felt; 5-A asymmetric treatment to less than 0.01-V difference
    took about 5 h for 100 mL. All are abiotic.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - peng
- assessment_id: conflicts
  area: evidence
  topic: Conflicting values and limits on inference
  outcome: supported
  summary: Source disagreements are retained accurately.
  details: Yang conclusion pH 2.0-2.5 conflicts with methods/results/Figure 3/abstract
    at 8.0-8.5; 80-120 versus 100-120 min should not produce a universal 99% endpoint.
    Peng Results assign direct/acid restoration 93%/92%, while abstract/conclusion
    reverse them; the asymmetric paragraph also misnames acid electrolysis. Stated
    1190 mAh differs from 2238 mA times 0.5 h = 1119 mAh. Fifty-fold UV-visible dilution
    is explicit, so reported assay concentrations are not undiluted inventory. No
    guessed correction is introduced.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
  - peng
- assessment_id: scope
  area: scope
  topic: Criticality, biology and deployment
  outcome: supported
  summary: Unsupported inherited claims are absent.
  details: No jurisdiction/list/edition claim is made; no element criticality is assigned
    to the used liquid. No organism or microbial necessity was tested. Yang supports
    a reported pilot batch, not continuous commercial deployment. Peng supports short
    changing-current laboratory tests, not durable whole-feed recycling or recovered
    metal yield. High coulombic efficiency is not equivalent to retained capacity
    or energy efficiency.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - yang
  - peng
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed state and reviewer independence
  outcome: supported
  summary: Frozen bytes and independent work are explicit.
  details: Successful native inspect preceded owner judgment, and final input hashes
    were verified. The author downloaded the originals; this reviewer independently
    inspected their bytes/pages and executed bounded source searches and named validation.
    No owner/history correction was made. Batch gate results are included only after
    actual coordinator receipt/log verification.
  target_ids:
  - cmmmech:spent-vanadium-flow-battery-electrolyte
  evidence_ids:
  - owner
  - history
  - dossier
  - named
  - batch
findings: []
actions: []
limitations:
- The 2016 product is author-reported pilot powder with incomplete assay, diffraction,
  detection-limit, replicate and total-element balance evidence; no independently
  measured overall yield or compliance is asserted.
- The 2016 pH/time/concentration-basis discrepancies need attributable clarification
  before wider process transfer.
- The 2024 percentage-to-arm assignments and 1190/1119-mAh mismatch remain unresolved;
  raw replicate data and independent uncertainty estimates were not supplied.
- Hardware replacement, compartment sacrifice and absent durable whole-feed accounting
  limit comparison and scale inference; no recovery percentage is inferred from coulombic
  efficiency.
- Both full originals and all printed figures/tables were inspected, but experiments
  and chemical assays were not independently repeated. Publisher zero attachments
  is a bounded site observation, not proof no unpublished supplement exists.
notes:
- No supported corrective owner finding was identified. Qualified source gaps remain
  research follow-ups rather than defects to manufacture.
- An initial inspector command contained a mistyped sidecar path and failed before
  owner judgment. The path was corrected to the author-confirmed sidecar, successful
  inspect captured the exact inputs, and only that successful capture is used here.
- No scientific self-acceptance of this reviewer autunite/torbernite owners, Git/GitHub
  mutation, author contact, or automatic criticality/deployment claim occurred.
```
