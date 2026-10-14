# Independent cuprite reference-sequence geography finding

- Review: 20261014T225820Z-cuprite-round83-reference-provenance-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T22:55:44.990043Z
- Finished UTC: 2026-10-14T22:58:20.672580Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed a minor unsupported geographic implication: the authority gives a Taiwan submission address, not a Taiwan specimen-origin qualifier. Preserve this observation before correction; complete batch acceptance is pending.

## Scope And Provenance

Whole current owner read; this initial observation adjudicates only the reference-sequence geographic provenance wording and its companion source report.

Selection: Native inspect preceded judgment. Initial scientific assessment found no mechanistic defect; root requested explicit handling of this bounded provenance ambiguity after reviewer identified the submission address.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6719e1fc18d122bde9ffa947ff70b6b7266622d3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cuprite | data/records/cuprite.yaml | maintained | Cuprite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:cuprite | Actual one-record validation, zero failures; 2026-10-14T22:55:45.239668+00:00 to 2026-10-14T22:55:48.939702+00:00 |
| Final affected batch checks pending | unavailable | True | cmmmech:cuprite | Root initial batch is running and the geographic correction has not yet been applied; no terminal acceptance is claimed. |

## Scientific And Domain Assessments

### Submission address versus specimen geographic provenance

provenance: concern. Targets: cmmmech:cuprite.

The authority supports a Taiwanese submitting institution, not a specimen-origin assignment. In contrast with the experimental UK isolate, the unqualified Taiwan-provenance/source wording invites that unsupported interpretation. Narrow it to the actual submission address.

## Findings

### F1: Distinguish the reference sequence submission address from specimen origin

minor / open / confirmed; issue key: CMMMech.cuprite.reference-sequence-taiwan-provenance.

U19043.1 REFERENCE2 lists a National Taiwan University submission address. No inspected source qualifier establishes Taiwan specimen origin. Replace the record wording reference with Taiwan provenance and dossier Taiwan source with explicit submission-address provenance; preserve that this accession is not the experimental UK isolate.

## Recommended Actions And Acceptance Checks

### A1

Narrow geographic wording to the submitting institution/address, append canonical EDIT and inline history, preserve this initial observation, correct the source dossier with explicit amendment and save a linked successor after affected checks.

- Record and report identify Taiwan solely as the U19043.1 submission address, leaving specimen origin unresolved.
- Experimental isolate remains unnamed UK lawn-soil strain; no mechanism or numerical result changes.
- Original CREATE and initial review remain immutable; canonical EDIT and actual inline event describe the narrow correction.
- Named and affected batch checks pass; successor resolves exact F1 occurrence and issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cuprite.yaml; mechanisms[0].evidence[4].explanation. Actual local artifact: /private/tmp/CMMMech-expansion-round83-20261014/data/records/cuprite.yaml | supports | The record calls U19043.1 a reference with Taiwan provenance while distinguishing the UK experimental isolate. |
| dossier | research/sources/round83-copper-oxides/20261014T225443Z.md; Source inventory item4, line15. Actual local artifact: /private/tmp/CMMMech-expansion-round83-20261014/research/sources/round83-copper-oxides/20261014T225443Z.md | supports | The companion report calls U19043.1 a Taiwan source without identifying that the geographic information is a submission address. |
| genbank | https://www.ncbi.nlm.nih.gov/nuccore/U19043.1; Complete2395-byte GenBank record, REFERENCE2 Direct Submission and FEATURES source qualifiers. Actual local artifact: /private/tmp/cmm-round83-copper-oxides-research/raw/U19043.gb | supports | REFERENCE2 gives National Taiwan University, Taipei as the submitting address. The source features identify species, genomic DNA and mycelium, but do not provide a country, collection location or specimen isolation source establishing Taiwan origin. |
| named | /private/tmp/cmm-round83-cuprite-independent/named.json; Actual independent command receipt, log hash 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e. Actual local artifact: /private/tmp/cmm-round83-cuprite-independent/named.json | supports | One target passed strict validation; structural validity does not establish source geography. |

## Limits And Additional Notes

- This scoped partial observation does not claim completed final batch or publication gates.
- Complete main-text/graphics assessment is prepared separately; this finding concerns context-only geography, not an invented species or mechanistic defect.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T225820Z-cuprite-round83-reference-provenance-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent cuprite reference-sequence geography finding
started_at: '2026-10-14T22:55:44.990043Z'
finished_at: '2026-10-14T22:58:20.672580Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored cuprite and the dossier. Reviewer authored only
    spent-potlining and made no target/history/dossier edits. Reviewer independently
    read U19043, reported its Taiwan submission institution, and confirmed the bounded
    ambiguity after root requested explicit adjudication.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Confirmed a minor unsupported geographic implication: the authority gives
  a Taiwan submission address, not a Taiwan specimen-origin qualifier. Preserve this
  observation before correction; complete batch acceptance is pending.'
source:
  git_revision: 6719e1fc18d122bde9ffa947ff70b6b7266622d3
  state: working_tree
  inputs:
  - path: data/records/cuprite.yaml
    sha256: 3abd262fe8366280c0430c430af38ff21020489cb0bb2c3637de17bb4fd85dc2
    role: target
  - path: history/records/cuprite/2026-10-14T225433Z-codex-9c0462.yaml
    sha256: 980032ca0f478e88ba43701aeb09faf856cbc9033d917dd4dffb6ee390f70c8f
    role: context
  - path: research/sources/round83-copper-oxides/20261014T225443Z.json
    sha256: e71f88ac77eb6cd3a07d7aaf947353ab695b4898329e3518ed372c3fe54b8b78
    role: context
  - path: research/sources/round83-copper-oxides/20261014T225443Z.md
    sha256: f568749e0fdf3d1ede9f238bc425a7cbaae2c0e2911b82a3a842e3f78cdff189
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:cuprite
  path: data/records/cuprite.yaml
  label: Cuprite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/cuprite/2026-10-14T225433Z-codex-9c0462.yaml
    role: canonical_history
scope:
  description: Whole current owner read; this initial observation adjudicates only
    the reference-sequence geographic provenance wording and its companion source
    report.
  selection: Native inspect preceded judgment. Initial scientific assessment found
    no mechanistic defect; root requested explicit handling of this bounded provenance
    ambiguity after reviewer identified the submission address.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cuprite
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate data/records/cuprite.yaml --require-records
  status: passed
  required: true
  summary: Actual one-record validation, zero failures; 2026-10-14T22:55:45.239668+00:00
    to 2026-10-14T22:55:48.939702+00:00
  target_ids:
  - cmmmech:cuprite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Final affected batch checks pending
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base 6719e1fc18d122bde9ffa947ff70b6b7266622d3
  status: unavailable
  required: true
  summary: Root initial batch is running and the geographic correction has not yet
    been applied; no terminal acceptance is claimed.
  target_ids:
  - cmmmech:cuprite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cuprite.yaml
  locator: 'mechanisms[0].evidence[4].explanation. Actual local artifact: /private/tmp/CMMMech-expansion-round83-20261014/data/records/cuprite.yaml'
  accessed_at: '2026-10-14T22:58:20.672580Z'
  support: supports
  summary: The record calls U19043.1 a reference with Taiwan provenance while distinguishing
    the UK experimental isolate.
  snapshot_sha256: 3abd262fe8366280c0430c430af38ff21020489cb0bb2c3637de17bb4fd85dc2
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round83-copper-oxides/20261014T225443Z.md
  locator: 'Source inventory item4, line15. Actual local artifact: /private/tmp/CMMMech-expansion-round83-20261014/research/sources/round83-copper-oxides/20261014T225443Z.md'
  accessed_at: '2026-10-14T22:58:20.672580Z'
  support: supports
  summary: The companion report calls U19043.1 a Taiwan source without identifying
    that the geographic information is a submission address.
  snapshot_sha256: f568749e0fdf3d1ede9f238bc425a7cbaae2c0e2911b82a3a842e3f78cdff189
- evidence_id: genbank
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/U19043.1
  locator: 'Complete2395-byte GenBank record, REFERENCE2 Direct Submission and FEATURES
    source qualifiers. Actual local artifact: /private/tmp/cmm-round83-copper-oxides-research/raw/U19043.gb'
  accessed_at: '2026-10-14T22:58:20.672580Z'
  support: supports
  summary: REFERENCE2 gives National Taiwan University, Taipei as the submitting address.
    The source features identify species, genomic DNA and mycelium, but do not provide
    a country, collection location or specimen isolation source establishing Taiwan
    origin.
  snapshot_sha256: 3059f690f854d19c86ee71c0cff12a65db37dc0db5a91d0196a773c275eaa6c0
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round83-cuprite-independent/named.json
  locator: 'Actual independent command receipt, log hash 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e.
    Actual local artifact: /private/tmp/cmm-round83-cuprite-independent/named.json'
  accessed_at: '2026-10-14T22:58:20.672580Z'
  support: supports
  summary: One target passed strict validation; structural validity does not establish
    source geography.
  snapshot_sha256: 7a34f927ccc1cfd7cb83ddb15656e0437c51de6ec8683b38f7568f20e3fe0b1b
assessments:
- assessment_id: reference-geography
  area: provenance
  topic: Submission address versus specimen geographic provenance
  outcome: concern
  summary: The authority supports a Taiwanese submitting institution, not a specimen-origin
    assignment. In contrast with the experimental UK isolate, the unqualified Taiwan-provenance/source
    wording invites that unsupported interpretation. Narrow it to the actual submission
    address.
  target_ids:
  - cmmmech:cuprite
  evidence_ids:
  - record
  - dossier
  - genbank
findings:
- finding_id: F1
  issue_key: CMMMech.cuprite.reference-sequence-taiwan-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the reference sequence submission address from specimen origin
  description: U19043.1 REFERENCE2 lists a National Taiwan University submission address.
    No inspected source qualifier establishes Taiwan specimen origin. Replace the
    record wording reference with Taiwan provenance and dossier Taiwan source with
    explicit submission-address provenance; preserve that this accession is not the
    experimental UK isolate.
  target_ids:
  - cmmmech:cuprite
  field_paths:
  - mechanisms[0].evidence[4].explanation
  - research/sources/round83-copper-oxides/20261014T225443Z.md:source-inventory-item4
  evidence_ids:
  - record
  - dossier
  - genbank
  rule_id: source-identifier-provenance-scope
  native_severity: minor
  normalization_reason: Bounded geographic overinterpretation/ambiguity in context-only
    reference evidence; species identity and the accepted Cu2O experimental mechanism
    are not invalidated.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round83-copper-oxides/20261014T225443Z.md
    role: source_dossier
actions:
- action_id: A1
  description: Narrow geographic wording to the submitting institution/address, append
    canonical EDIT and inline history, preserve this initial observation, correct
    the source dossier with explicit amendment and save a linked successor after affected
    checks.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:cuprite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cuprite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round83-copper-oxides/20261014T225443Z.md
    role: source_dossier
  acceptance_checks:
  - Record and report identify Taiwan solely as the U19043.1 submission address, leaving
    specimen origin unresolved.
  - Experimental isolate remains unnamed UK lawn-soil strain; no mechanism or numerical
    result changes.
  - Original CREATE and initial review remain immutable; canonical EDIT and actual
    inline event describe the narrow correction.
  - Named and affected batch checks pass; successor resolves exact F1 occurrence and
    issue key.
limitations:
- This scoped partial observation does not claim completed final batch or publication
  gates.
- Complete main-text/graphics assessment is prepared separately; this finding concerns
  context-only geography, not an invented species or mechanistic defect.
```
