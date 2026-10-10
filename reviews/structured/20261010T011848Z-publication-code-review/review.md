# Adversarial implementation and publication-review integration review

- Review: 20261010T011848Z-publication-code-review
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-10T01:15:30Z
- Finished UTC: 2026-10-10T01:18:48Z
- Reviewer: codex /root/publish_code_20261009 (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

No material code defect found in the new concentration contract or discovery workflow; 104 targeted tests pass. Two publication findings remain: a minor current structured-review coverage/navigation gap, and a major portability failure if the squash merge drops the reviewed topic-branch base. A main-only synthetic squash clone reproduces unverified provenance. Neither finding invalidates historical Markdown or requires governed helper edits.

## Scope And Provenance

Bounded review of all eight code, tests, contract, skill and README targets changed relative to origin/main in the source-survey branch at c0adc2c. This is not a fresh primary-literature review or a full-repository security audit.

Selection: All implementation/skill/documentation targets in origin/main...HEAD; research reports, scientific records and history sidecars excluded because independently reviewed by other agents.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base c0adc2c0763e1515ed07dc712b024974d98fb342.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| observation-schema | src/cmmmech/schema/cmmmech.yaml | maintained | observation schema |
| observation-validator | src/cmmmech/validation.py | maintained | observation validator |
| observation-tests | tests/test_observations.py | maintained | observation tests |
| record-contract | docs/records.md | maintained | record contract |
| discovery-skill | .claude/skills/cmmmech-discover-sources/SKILL.md | maintained | discovery skill |
| discovery-template | .claude/skills/cmmmech-discover-sources/references/report-template.md | maintained | discovery template |
| discovery-routes | .claude/skills/cmmmech-discover-sources/references/source-guide.md | maintained | discovery routes |
| readme | README.md | maintained | readme |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Concentration and native validation tests | passed | True | observation-schema, observation-validator, observation-tests | 104 tests passed; no skips or failures. |
| Structured review coverage before this round | failed | True | readme, record-contract | Exit 1: no structured reviews exist; absence is not reviewed coverage. This is an initial review-round observation, not a assertion that legacy reports are invalid. |
| Diff whitespace validation | passed | True | observation-schema, observation-validator, observation-tests, record-contract, discovery-skill, discovery-template, discovery-routes, readme | No whitespace errors. |
| Documentation and skill relative-link targets | passed | True | readme, record-contract, discovery-skill | Python extraction of Markdown relative links from README, docs/records.md and source-discovery SKILL.md resolved each target path. This checked file paths, not remote availability or anchors. |
| Full batch CI and scientific validation | not_applicable | False | observation-schema, observation-validator, observation-tests, record-contract, discovery-skill, discovery-template, discovery-routes, readme | Assigned to publishing agent; no claim that full gates or external scientific evidence were reassessed by this reviewer. |
| Reviewed Git base survives squash-only checkout | failed | True | readme, record-contract | Main-only clone advanced to origin/main 193a5ab, then given the topic tree in a synthetic squash commit, still cannot resolve c0adc2c. Canonical source_provenance reports unverified. |

## Scientific And Domain Assessments

### Source concentration representation

schema: supported. Targets: observation-schema.

Optional source observations remain a bounded, closed schema; mg/kg concentrations and detection limits do not introduce yield or effect-size claims.

### Numerical and source-cell integrity

quantity: supported. Targets: observation-validator.

No confirmed behavioral defect found. Numeric comparison is decimal-exact relative to the YAML-parsed number, large integers avoid float overflow, and invalid exponents fail cleanly. Source tables still require scientific interpretation.

### Meaningful behavioral regressions

completeness: supported. Targets: observation-tests.

104 affected tests pass, including required/forbidden field behavior, numeric and provenance edge cases. Tests are synthetic and do not manufacture corpus measurements.

### Documented source-cell semantics

representation: supported. Targets: record-contract.

The observation documentation matches implementation and preserves mass-based units, censored values, source locators and temporal meaning.

### Discovery handoff boundaries

scope: supported. Targets: discovery-skill, discovery-template, discovery-routes.

The skill and template produce bounded evidence assessment and explicit prerequisites, with source acquisition distinct from scientific acceptance and automatic import.

### Corpus and review navigation

scope: supported. Targets: readme.

README material inventory and observation scope links resolve and preserve laboratory/measurement limits; publication-review navigation needs the separate minor correction below.

### Current review-round coverage and navigation

provenance: concern. Targets: readme, record-contract.

No structured reviews existed before this invoked publication round, and README only points to legacy reviews. Save fresh per-record structured bundles and direct readers to them, while preserving earlier Markdown.

### Portability of immutable review bases after squash

provenance: concern. Targets: readme, record-contract.

Current reviews use topic commit c0adc2c as their base. A squash tree does not retain that ancestry; canonical checks need the base object even for working-tree attestations. The publication workflow must retain these reviewed commits durably and ensure consumers fetch them, or create valid reviews anchored to a permanent main base.

## Findings

### F1: Complete and expose current structured publication reviews

minor / open / confirmed; issue key: publication-structured-review-coverage.

After merging the new review contract, the requested adversarial publication round starts with no structured bundles: check --require-reviews exits 1. README links only reviews/records. This is a bounded current-round process/navigation gap, not a scientific-data defect and not a demand to retro-convert valid historical reports. The current publication should finish fresh per-record structured reviews and link their location before merge.

### F2: Preserve reviewed Git bases across squash and branch deletion

major / open / confirmed; issue key: squash-review-base-retention.

Structured working_tree reviews still require source.git_revision to exist as a commit. The inspected base c0adc2c lies on the topic branch, while the configured queue uses squash. An isolated clone containing current main plus the prospective tree as a new single-parent commit cannot resolve c0adc2c; canonical source_provenance reports unverified and read_review rejects it. Before squash/deleting the topic branch, ensure durable reviewed-base retention and supported consumer fetch behavior, or author valid reviews from a permanent-main-base worktree. The scientific review bytes alone do not preserve their required Git base.

## Recommended Actions And Acceptance Checks

### A1

Save fresh schema-valid reviews for the ten records in this publication round, link structured reviews and the contract from README, retain old reports unchanged, and save a successor observation explicitly resolving F1 after validation.

- scripts/record_review.py check --require-reviews exits 0.
- Each of ten material record paths has a fresh kind: record bundle identifying reviewed bytes in this publication round.
- README links current structured reviews and clearly identifies historical Markdown reviews.
- Previous committed review artifacts remain byte-identical and the successor finding retains issue_key publication-structured-review-coverage.

### A2

Choose and implement a durable review-base strategy compatible with squash and branch deletion, retain every referenced base required by these reviews, document consumer fetch behavior, and save a successor disposition with isolated fresh-clone evidence.

- Fresh normal clone after a simulated or actual squash can resolve every source.git_revision and scripts/record_review.py check --require-reviews passes.
- Required CI/review consumers fetch retained reviewed bases; shallow/tag-fetch limitations are explicitly tested or excluded with documented requirements.
- No governed helper is hand-edited and original reviews remain immutable.
- Successor finding retains issue_key squash-review-base-retention and cites this exact predecessor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| implementation | src/cmmmech/validation.py and src/cmmmech/schema/cmmmech.yaml; ConcentrationObservation, _observation_errors and validate_record observation loop | supports | Reviewed full changed code and generated-schema control flow. Structural errors return before semantic access; finite values, exclusive result fields, exact Decimal source comparisons, positive limits, source linkage, unique IDs/cells and sampling chronology are enforced. Integer overflow and long-mantissa censoring fixes remain covered. |
| tests | tests/test_observations.py; tests/test_validation.py; Actual targeted pytest execution; 104 passed in 2.41 s | supports | Synthetic regressions cover censored versus measured values, raw-value fidelity, nonfinite numbers, huge exponent error handling, large integers, closed fields, source references, IDs/cells and date provenance. |
| contract | docs/records.md; Quantitative source observations | supports | The narrow mg/kg total-element source-cell contract documents assigned study arms versus actual inoculation, no inferred microbial causality, no density conversion, separate sample/analysis dates, negative-limit encoding and omitted unresolved dates. |
| skill | .claude/skills/cmmmech-discover-sources/SKILL.md and references/; All three changed skill files | supports | Read the complete skill, report template and source routes. They require claim-level source roles, exact identity/version, bounded hidden/ignored searches, sample inspection, license checks, contradictions, access failures and separate curation/review acceptance; historical route checks do not claim current remote availability. |
| coverage | docs/record-reviews.md; docs/record-review-profile.md; README.md; initial review inventory; Initial check --require-reviews and README links to reviews/records | refutes | New review contract requires current rounds as structured pairs. At review start the required coverage command exited 1 because no structured reviews existed. README linked the historical directory only. Existing Markdown reports remain legitimate immutable historical evidence. |
| diff | git diff origin/main...HEAD; Eight changed implementation/docs/skill targets | supports | Read all eight targets and relevant complete files; git diff --check exited 0. |
| links | README.md; docs/records.md; .claude/skills/cmmmech-discover-sources/SKILL.md; All relative Markdown link paths in these three files | supports | Path existence assertions passed for every extracted relative link; remote URLs were deliberately excluded. |
| squash-provenance | scripts/record_review.py; /private/tmp/cmm-publish-code-review/main-only-provenance.json; source_provenance lines 670-687 and read_review lines 660-668; synthetic main parent 193a5ab81cd66de55cd00df4405128c0a14471c9, squash f27d49f08be4e1ec070db780e75cd76bf89083c6 | refutes | The working_tree provenance path requires git_revision to resolve as a commit. Original worktree accepts c0adc2c; a clone with current main plus identical topic tree as a synthetic squash commit returns unverified because c0adc2c is absent (git cat-file exit 128). Deleting the only branch reference after a squash without durable base retention breaks fresh-clone review checks. No GitHub branch deletion or governed helper modification was performed. |

## Limits And Additional Notes

- No new primary scientific source or identifier verification was performed in this repository implementation review; separate reviewers own those checks.
- The eight curated USGS cells motivated this schema. Tests establish declared interpretation, not whether arbitrary negative source values represent detection limits.
- Remote entry-point URLs were reviewed as workflow examples, not checked for present service availability.
- Full just check, history immutability, governed sync and GitHub CI are assigned to the publishing agent; this review records only targeted checks actually executed.
- Squash portability was reproduced locally with current origin/main and a synthetic squash commit, not by deleting the live remote branch. Durable tag availability and CI fetching still require resolution by the publisher.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T011848Z-publication-code-review
kind: repository
repository: CultureBotAI/CMMMech
title: Adversarial implementation and publication-review integration review
started_at: '2026-10-10T01:15:30Z'
finished_at: '2026-10-10T01:18:48Z'
reviewer:
  identity: codex /root/publish_code_20261009
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Fresh delegated agent; did not implement the concentration schema,
    validator, tests, source-discovery skill, records or prior reviews. Maintainer
    flagged the newly merged review-contract integration question; this reviewer independently
    reproduced it.
skill: docs/record-reviews.md; .claude/skills/review-record/SKILL.md output and evidence
  rubric, bounded repository review
completion: completed
verdict: needs_curation
scientific_review: false
summary: 'No material code defect found in the new concentration contract or discovery
  workflow; 104 targeted tests pass. Two publication findings remain: a minor current
  structured-review coverage/navigation gap, and a major portability failure if the
  squash merge drops the reviewed topic-branch base. A main-only synthetic squash
  clone reproduces unverified provenance. Neither finding invalidates historical Markdown
  or requires governed helper edits.'
source:
  git_revision: c0adc2c0763e1515ed07dc712b024974d98fb342
  state: working_tree
  inputs:
  - path: .claude/skills/cmmmech-discover-sources/SKILL.md
    sha256: 52bfb4803adbf394c82c3b47b1eb8c1928ddf7cb35aa81ed8ff50de9cd569e21
    role: target
  - path: .claude/skills/cmmmech-discover-sources/references/report-template.md
    sha256: 79e2494b02e49fda12724b47221ff3c282893e70a5bf96d772dcfd04b0633e41
    role: target
  - path: .claude/skills/cmmmech-discover-sources/references/source-guide.md
    sha256: 893e38956eaaca8430a0957b8ecbe5539d23d01a363c9f7fbbc029de2b057090
    role: target
  - path: .claude/skills/review-record/SKILL.md
    sha256: abe8f0aebf9540aaaf5d2e2c2b43a4b17b7d5963d04e084b65e1ada19f4eb6be
    role: context
  - path: CLAUDE.md
    sha256: 6304e7e757a03a66f059155ba421ba3e7e2b2a562f36100bbf177efed6b57460
    role: context
  - path: README.md
    sha256: 471ebb931ddf3b0fcea68be8c4ee77558767f1b39e010155d52cf95d2b2b2fee
    role: target
  - path: docs/record-review-profile.md
    sha256: fa6a328afe91261d415d20ba6ba53d223202f71af2ce82a73876b65571acf2f8
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: target
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: target
  - path: src/cmmmech/validation.py
    sha256: 510e7ed92887ea6e8c8e5828af378ffe0aa737772f8188ade6b42bde14bb5dfa
    role: target
  - path: tests/test_observations.py
    sha256: e1d48c5b449d54689207e0e0ad160b8e2e9531e890f7d024982d2b9f607130b8
    role: target
scope:
  description: Bounded review of all eight code, tests, contract, skill and README
    targets changed relative to origin/main in the source-survey branch at c0adc2c.
    This is not a fresh primary-literature review or a full-repository security audit.
  selection: All implementation/skill/documentation targets in origin/main...HEAD;
    research reports, scientific records and history sidecars excluded because independently
    reviewed by other agents.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - observation-schema
  - observation-validator
  - observation-tests
  - record-contract
  - discovery-skill
  - discovery-template
  - discovery-routes
  - readme
  exclusions:
  - target: data/records/*.yaml and primary literature
    reason: Fresh scientific review delegated separately; this implementation review
      cannot certify source claims.
  - target: history/records and reviews/records historical artifacts
    reason: Append-only batch gates owned by publishing agent; past artifacts are
      not rewritten or retro-converted.
  - target: CLAW governed helpers and CI outside this delta
    reason: Merged upstream governance is context, not modified implementation under
      review.
targets:
- target_id: observation-schema
  path: src/cmmmech/schema/cmmmech.yaml
  label: observation schema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/schema/cmmmech.yaml
    role: maintained implementation or documentation
- target_id: observation-validator
  path: src/cmmmech/validation.py
  label: observation validator
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: src/cmmmech/validation.py
    role: maintained implementation or documentation
- target_id: observation-tests
  path: tests/test_observations.py
  label: observation tests
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: tests/test_observations.py
    role: maintained implementation or documentation
- target_id: record-contract
  path: docs/records.md
  label: record contract
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: docs/records.md
    role: maintained implementation or documentation
- target_id: discovery-skill
  path: .claude/skills/cmmmech-discover-sources/SKILL.md
  label: discovery skill
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: .claude/skills/cmmmech-discover-sources/SKILL.md
    role: maintained implementation or documentation
- target_id: discovery-template
  path: .claude/skills/cmmmech-discover-sources/references/report-template.md
  label: discovery template
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: .claude/skills/cmmmech-discover-sources/references/report-template.md
    role: maintained implementation or documentation
- target_id: discovery-routes
  path: .claude/skills/cmmmech-discover-sources/references/source-guide.md
  label: discovery routes
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: .claude/skills/cmmmech-discover-sources/references/source-guide.md
    role: maintained implementation or documentation
- target_id: readme
  path: README.md
  label: readme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: README.md
    role: maintained implementation or documentation
checks:
- check_id: targeted-tests
  name: Concentration and native validation tests
  status: passed
  required: true
  summary: 104 tests passed; no skips or failures.
  target_ids:
  - observation-schema
  - observation-validator
  - observation-tests
  command: .venv/bin/python -m pytest -q tests/test_observations.py tests/test_validation.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - tests
- check_id: structured-coverage
  name: Structured review coverage before this round
  status: failed
  required: true
  summary: 'Exit 1: no structured reviews exist; absence is not reviewed coverage.
    This is an initial review-round observation, not a assertion that legacy reports
    are invalid.'
  target_ids:
  - readme
  - record-contract
  command: .venv/bin/python scripts/record_review.py check --require-reviews
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - coverage
- check_id: diff-whitespace
  name: Diff whitespace validation
  status: passed
  required: true
  summary: No whitespace errors.
  target_ids:
  - observation-schema
  - observation-validator
  - observation-tests
  - record-contract
  - discovery-skill
  - discovery-template
  - discovery-routes
  - readme
  command: git diff --check origin/main...HEAD
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - diff
- check_id: local-links
  name: Documentation and skill relative-link targets
  status: passed
  required: true
  summary: Python extraction of Markdown relative links from README, docs/records.md
    and source-discovery SKILL.md resolved each target path. This checked file paths,
    not remote availability or anchors.
  target_ids:
  - readme
  - record-contract
  - discovery-skill
  command: 'Python pathlib + re: extract relative Markdown links from README.md, docs/records.md
    and .claude/skills/cmmmech-discover-sources/SKILL.md; assert resolved paths exist'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - links
- check_id: full-batch
  name: Full batch CI and scientific validation
  status: not_applicable
  required: false
  summary: Assigned to publishing agent; no claim that full gates or external scientific
    evidence were reassessed by this reviewer.
  target_ids:
  - observation-schema
  - observation-validator
  - observation-tests
  - record-contract
  - discovery-skill
  - discovery-template
  - discovery-routes
  - readme
- check_id: squash-provenance
  name: Reviewed Git base survives squash-only checkout
  status: failed
  required: true
  summary: Main-only clone advanced to origin/main 193a5ab, then given the topic tree
    in a synthetic squash commit, still cannot resolve c0adc2c. Canonical source_provenance
    reports unverified.
  target_ids:
  - readme
  - record-contract
  command: Local isolated clone --no-local --single-branch main; fetch only refs/remotes/origin/main;
    archive topic HEAD into a new single-parent commit; git cat-file -e c0adc2c^{commit};
    invoke scripts/record_review.py source_provenance
  exit_code: 128
  expected_exit_code: 0
  evidence_ids:
  - squash-provenance
evidence:
- evidence_id: implementation
  kind: record_content
  reference: src/cmmmech/validation.py and src/cmmmech/schema/cmmmech.yaml
  locator: ConcentrationObservation, _observation_errors and validate_record observation
    loop
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: Reviewed full changed code and generated-schema control flow. Structural
    errors return before semantic access; finite values, exclusive result fields,
    exact Decimal source comparisons, positive limits, source linkage, unique IDs/cells
    and sampling chronology are enforced. Integer overflow and long-mantissa censoring
    fixes remain covered.
- evidence_id: tests
  kind: validation
  reference: tests/test_observations.py; tests/test_validation.py
  locator: Actual targeted pytest execution; 104 passed in 2.41 s
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: Synthetic regressions cover censored versus measured values, raw-value
    fidelity, nonfinite numbers, huge exponent error handling, large integers, closed
    fields, source references, IDs/cells and date provenance.
- evidence_id: contract
  kind: record_content
  reference: docs/records.md
  locator: Quantitative source observations
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: The narrow mg/kg total-element source-cell contract documents assigned
    study arms versus actual inoculation, no inferred microbial causality, no density
    conversion, separate sample/analysis dates, negative-limit encoding and omitted
    unresolved dates.
- evidence_id: skill
  kind: record_content
  reference: .claude/skills/cmmmech-discover-sources/SKILL.md and references/
  locator: All three changed skill files
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: Read the complete skill, report template and source routes. They require
    claim-level source roles, exact identity/version, bounded hidden/ignored searches,
    sample inspection, license checks, contradictions, access failures and separate
    curation/review acceptance; historical route checks do not claim current remote
    availability.
- evidence_id: coverage
  kind: validation
  reference: docs/record-reviews.md; docs/record-review-profile.md; README.md; initial
    review inventory
  locator: Initial check --require-reviews and README links to reviews/records
  accessed_at: '2026-10-10T01:16:43Z'
  support: refutes
  summary: New review contract requires current rounds as structured pairs. At review
    start the required coverage command exited 1 because no structured reviews existed.
    README linked the historical directory only. Existing Markdown reports remain
    legitimate immutable historical evidence.
  search_scope: Inspected reviews with rg --no-ignore --hidden including ignored files,
    and the shared checker recursively checks hidden/ignored bundles. reviews/structured
    did not exist at that time. Excluded .git and .venv; no machine-wide absence claim.
- evidence_id: diff
  kind: validation
  reference: git diff origin/main...HEAD
  locator: Eight changed implementation/docs/skill targets
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: Read all eight targets and relevant complete files; git diff --check exited
    0.
- evidence_id: links
  kind: validation
  reference: README.md; docs/records.md; .claude/skills/cmmmech-discover-sources/SKILL.md
  locator: All relative Markdown link paths in these three files
  accessed_at: '2026-10-10T01:16:43Z'
  support: supports
  summary: Path existence assertions passed for every extracted relative link; remote
    URLs were deliberately excluded.
- evidence_id: squash-provenance
  kind: validation
  reference: scripts/record_review.py; /private/tmp/cmm-publish-code-review/main-only-provenance.json
  locator: source_provenance lines 670-687 and read_review lines 660-668; synthetic
    main parent 193a5ab81cd66de55cd00df4405128c0a14471c9, squash f27d49f08be4e1ec070db780e75cd76bf89083c6
  accessed_at: '2026-10-10T01:18:27Z'
  support: refutes
  summary: The working_tree provenance path requires git_revision to resolve as a
    commit. Original worktree accepts c0adc2c; a clone with current main plus identical
    topic tree as a synthetic squash commit returns unverified because c0adc2c is
    absent (git cat-file exit 128). Deleting the only branch reference after a squash
    without durable base retention breaks fresh-clone review checks. No GitHub branch
    deletion or governed helper modification was performed.
assessments:
- assessment_id: schema
  area: schema
  topic: Source concentration representation
  outcome: supported
  summary: Optional source observations remain a bounded, closed schema; mg/kg concentrations
    and detection limits do not introduce yield or effect-size claims.
  target_ids:
  - observation-schema
  evidence_ids:
  - implementation
  - contract
  - tests
- assessment_id: validator
  area: quantity
  topic: Numerical and source-cell integrity
  outcome: supported
  summary: No confirmed behavioral defect found. Numeric comparison is decimal-exact
    relative to the YAML-parsed number, large integers avoid float overflow, and invalid
    exponents fail cleanly. Source tables still require scientific interpretation.
  target_ids:
  - observation-validator
  evidence_ids:
  - implementation
  - tests
- assessment_id: tests
  area: completeness
  topic: Meaningful behavioral regressions
  outcome: supported
  summary: 104 affected tests pass, including required/forbidden field behavior, numeric
    and provenance edge cases. Tests are synthetic and do not manufacture corpus measurements.
  target_ids:
  - observation-tests
  evidence_ids:
  - tests
- assessment_id: record-docs
  area: representation
  topic: Documented source-cell semantics
  outcome: supported
  summary: The observation documentation matches implementation and preserves mass-based
    units, censored values, source locators and temporal meaning.
  target_ids:
  - record-contract
  evidence_ids:
  - contract
- assessment_id: discovery
  area: scope
  topic: Discovery handoff boundaries
  outcome: supported
  summary: The skill and template produce bounded evidence assessment and explicit
    prerequisites, with source acquisition distinct from scientific acceptance and
    automatic import.
  target_ids:
  - discovery-skill
  - discovery-template
  - discovery-routes
  evidence_ids:
  - skill
  - links
- assessment_id: readme
  area: scope
  topic: Corpus and review navigation
  outcome: supported
  summary: README material inventory and observation scope links resolve and preserve
    laboratory/measurement limits; publication-review navigation needs the separate
    minor correction below.
  target_ids:
  - readme
  evidence_ids:
  - links
  - contract
- assessment_id: publication-gap
  area: provenance
  topic: Current review-round coverage and navigation
  outcome: concern
  summary: No structured reviews existed before this invoked publication round, and
    README only points to legacy reviews. Save fresh per-record structured bundles
    and direct readers to them, while preserving earlier Markdown.
  target_ids:
  - readme
  - record-contract
  evidence_ids:
  - coverage
- assessment_id: squash-provenance
  area: provenance
  topic: Portability of immutable review bases after squash
  outcome: concern
  summary: Current reviews use topic commit c0adc2c as their base. A squash tree does
    not retain that ancestry; canonical checks need the base object even for working-tree
    attestations. The publication workflow must retain these reviewed commits durably
    and ensure consumers fetch them, or create valid reviews anchored to a permanent
    main base.
  target_ids:
  - readme
  - record-contract
  evidence_ids:
  - squash-provenance
findings:
- finding_id: F1
  issue_key: publication-structured-review-coverage
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Complete and expose current structured publication reviews
  description: 'After merging the new review contract, the requested adversarial publication
    round starts with no structured bundles: check --require-reviews exits 1. README
    links only reviews/records. This is a bounded current-round process/navigation
    gap, not a scientific-data defect and not a demand to retro-convert valid historical
    reports. The current publication should finish fresh per-record structured reviews
    and link their location before merge.'
  target_ids:
  - readme
  - record-contract
  field_paths:
  - 'README.md: corpus record reviews link'
  - 'docs/records.md: Curation and review requirements'
  evidence_ids:
  - coverage
  rule_id: current-round-structured-review-output
  native_severity: minor
  normalization_reason: Bounded process/documentation issue; no record identity or
    scientific claim has been shown wrong. Required review round is incomplete at
    the captured initial state.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: README.md
    role: Review navigation
  - repository: CultureBotAI/CMMMech
    path: reviews/structured
    role: Fresh review bundles saved through canonical helper
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/15
- finding_id: F2
  issue_key: squash-review-base-retention
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Preserve reviewed Git bases across squash and branch deletion
  description: Structured working_tree reviews still require source.git_revision to
    exist as a commit. The inspected base c0adc2c lies on the topic branch, while
    the configured queue uses squash. An isolated clone containing current main plus
    the prospective tree as a new single-parent commit cannot resolve c0adc2c; canonical
    source_provenance reports unverified and read_review rejects it. Before squash/deleting
    the topic branch, ensure durable reviewed-base retention and supported consumer
    fetch behavior, or author valid reviews from a permanent-main-base worktree. The
    scientific review bytes alone do not preserve their required Git base.
  target_ids:
  - readme
  - record-contract
  field_paths:
  - 'publication workflow: structured source.git_revision'
  - 'docs/record-reviews.md: retained base commit requirement'
  evidence_ids:
  - squash-provenance
  rule_id: available-reviewed-git-base
  native_severity: major
  normalization_reason: Systemic publication portability failure makes saved reviews
    unverifiable in a fresh clone after the requested squash/delete workflow; independent
    local reproduction confirms the failure.
  ownership_note: Publication owner retains reviewed Git bases and documents/fetches
    their durable references. Governed scripts/record_review.py is behaving according
    to its contract and must not be hand-edited.
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/17
actions:
- action_id: A1
  description: Save fresh schema-valid reviews for the ten records in this publication
    round, link structured reviews and the contract from README, retain old reports
    unchanged, and save a successor observation explicitly resolving F1 after validation.
  finding_ids:
  - F1
  target_ids:
  - readme
  - record-contract
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: README.md
    role: Review navigation
  - repository: CultureBotAI/CMMMech
    path: reviews/structured
    role: Fresh review output
  acceptance_checks:
  - scripts/record_review.py check --require-reviews exits 0.
  - 'Each of ten material record paths has a fresh kind: record bundle identifying
    reviewed bytes in this publication round.'
  - README links current structured reviews and clearly identifies historical Markdown
    reviews.
  - Previous committed review artifacts remain byte-identical and the successor finding
    retains issue_key publication-structured-review-coverage.
- action_id: A2
  description: Choose and implement a durable review-base strategy compatible with
    squash and branch deletion, retain every referenced base required by these reviews,
    document consumer fetch behavior, and save a successor disposition with isolated
    fresh-clone evidence.
  finding_ids:
  - F2
  target_ids:
  - readme
  - record-contract
  ownership_note: Publishing agent owns Git retention/fetch configuration and local
    workflow documentation, using supported governance update paths for any governed
    changes.
  acceptance_checks:
  - Fresh normal clone after a simulated or actual squash can resolve every source.git_revision
    and scripts/record_review.py check --require-reviews passes.
  - Required CI/review consumers fetch retained reviewed bases; shallow/tag-fetch
    limitations are explicitly tested or excluded with documented requirements.
  - No governed helper is hand-edited and original reviews remain immutable.
  - Successor finding retains issue_key squash-review-base-retention and cites this
    exact predecessor.
limitations:
- No new primary scientific source or identifier verification was performed in this
  repository implementation review; separate reviewers own those checks.
- The eight curated USGS cells motivated this schema. Tests establish declared interpretation,
  not whether arbitrary negative source values represent detection limits.
- Remote entry-point URLs were reviewed as workflow examples, not checked for present
  service availability.
- Full just check, history immutability, governed sync and GitHub CI are assigned
  to the publishing agent; this review records only targeted checks actually executed.
- Squash portability was reproduced locally with current origin/main and a synthetic
  squash commit, not by deleting the live remote branch. Durable tag availability
  and CI fetching still require resolution by the publisher.
tags:
- adversarial
- publication
- concentration-contract
```
