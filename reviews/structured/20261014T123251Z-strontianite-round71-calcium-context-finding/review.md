# Strontianite evidence context attribution finding

- Review: 20261014T123251Z-strontianite-round71-calcium-context-finding
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T12:24:02Z
- Finished UTC: 2026-10-14T12:32:51.340272Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor context attribution needs clarification: the source observation of no entrapped cells in coating fractures occurs in the calcium/polymer discussion. It does not directly establish cell exclusion in the Sr coating. Sr phase identification and no-cell control remain supported; completed final batch gates are pending.

## Scope And Provenance

Targeted context-attribution finding within independent full-record assessment; initial disposition before correction.

Selection: Frozen owner and canonical CREATE inspected before judgment; original calcium discussion compared against Sr evidence explanation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:strontianite | data/records/strontianite.yaml | maintained | Strontianite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named validation | passed | True | cmmmech:strontianite | Checked 2 records; 0 failed. |
| Pending completed batch gate | unavailable | True | cmmmech:strontianite | Coordinator final batch receipt not yet available; this is an initial corrective observation, not completed scientific acceptance. |
| Pending completed batch gate | unavailable | True | cmmmech:strontianite | Coordinator final batch receipt not yet available; this is an initial corrective observation, not completed scientific acceptance. |
| Pending completed batch gate | unavailable | True | cmmmech:strontianite | Coordinator final batch receipt not yet available; this is an initial corrective observation, not completed scientific acceptance. |

## Scientific And Domain Assessments

### Calcium-context observation versus Sr experiment

evidence: concern. Targets: cmmmech:strontianite.

The Sr mechanism explanation needs to limit the fracture observation to its original calcium/polymer context.

## Findings

### F1: Calcium coating fracture observation needs explicit source context

minor / open / confirmed; issue key: strontianite-round71-calcium-fracture-scope.

Qualify the no-entrapped-cell sentence as an observation in the calcium/polymer discussion, not direct evidence of absent cells in Sr coatings. Retain unresolved Sr nucleation explanations, Sr phase/control evidence and uncertainty. Correct the source dossier consistently and append actual EDIT history.

## Recommended Actions And Acceptance Checks

### A1

Curator clarify calcium-specific observation, retain Sr uncertainty, update dossier and canonical EDIT history; reviewer reassess corrected frozen bytes and save immutable successor.

- Confirm original paragraph context before Figure 2 and later distinct Sr series.
- Clarify owner and dossier without changing supported Sr measurements; save actual EDIT history.
- Repeat named and batch checks; successor must resolve this exact F1 occurrence and stable issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/strontianite.yaml; mechanisms[0].evidence[2].explanation; no-entrapped-cell sentence | refutes | Owner places an unqualified no-entrapped-cell observation under Sr-coating evidence, although the original paragraph concerns calcium/polymer coatings. |
| primary | https://doi.org/10.1021/acsami.3c13665; Results and Discussion, calcium/polymer paragraph immediately before Figure 2; /private/tmp/cmm-round71-strontium-research/natalio2024.txt lines 145–176 and matching original XML paragraph; Sr series starts later around Figure 3. | supports | The fracture observation appears amid calcium-carbonate polymorph and polymer-surface discussion, followed by further analysis of the vaterite coating. This is not explicitly a Sr-fracture observation. |
| named | /private/tmp/cmm-round71-strontium-independent/named-validation-initial.log; Reviewer-executed locked initial named validation | context_only | Two records pass structural validation; this does not validate experimental attribution. |

## Limits And Additional Notes

- Initial corrective observation, not final scientific acceptance; final batch checks remain pending.
- Original source does not resolve the molecular pathway or prove cell exclusion in Sr coatings.
- Reviewer has not modified peer owner or canonical history. Curator agreed the context concern before correction; immutable finding is saved first.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T123251Z-strontianite-round71-calcium-context-finding
kind: record
repository: CultureBotAI/CMMMech
title: Strontianite evidence context attribution finding
started_at: '2026-10-14T12:24:02Z'
finished_at: '2026-10-14T12:32:51.340272Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Peer authored reviewed owner and history. Reviewer independently
    read complete original source and supplement, all main figures and owner; no owner
    or history edits.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One minor context attribution needs clarification: the source observation
  of no entrapped cells in coating fractures occurs in the calcium/polymer discussion.
  It does not directly establish cell exclusion in the Sr coating. Sr phase identification
  and no-cell control remain supported; completed final batch gates are pending.'
source:
  git_revision: 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec
  state: working_tree
  inputs:
  - path: data/records/strontianite.yaml
    sha256: 24b79d701283399e97a38f358b031d0e7a8834e6baf54641f9c558b2fca40402
    role: target
  - path: history/records/strontianite/2026-10-14T122711Z-codex-8d2da3.yaml
    sha256: 84d7959c5dddc91041411ccab43c885cd184f2f24488c66f8bf1746fdfa617fd
    role: context
scope:
  description: Targeted context-attribution finding within independent full-record
    assessment; initial disposition before correction.
  selection: Frozen owner and canonical CREATE inspected before judgment; original
    calcium discussion compared against Sr evidence explanation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:strontianite
targets:
- target_id: cmmmech:strontianite
  path: data/records/strontianite.yaml
  label: Strontianite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Named validation
  command: uv run --locked cmmmech validate data/records/celestine.yaml data/records/strontianite.yaml
    --require-records
  status: passed
  required: true
  summary: Checked 2 records; 0 failed.
  target_ids:
  - cmmmech:strontianite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Pending completed batch gate
  command: just check
  status: unavailable
  required: true
  summary: Coordinator final batch receipt not yet available; this is an initial corrective
    observation, not completed scientific acceptance.
  target_ids:
  - cmmmech:strontianite
  evidence_ids: []
- check_id: nonempty
  name: Pending completed batch gate
  command: uv run --locked cmmmech validate --require-records
  status: unavailable
  required: true
  summary: Coordinator final batch receipt not yet available; this is an initial corrective
    observation, not completed scientific acceptance.
  target_ids:
  - cmmmech:strontianite
  evidence_ids: []
- check_id: history
  name: Pending completed batch gate
  command: uv run --locked cmmmech validate-history --base 188ce7cb6f6dd1b7966b527546d80f9b4fb7fcec
  status: unavailable
  required: true
  summary: Coordinator final batch receipt not yet available; this is an initial corrective
    observation, not completed scientific acceptance.
  target_ids:
  - cmmmech:strontianite
  evidence_ids: []
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/strontianite.yaml
  locator: mechanisms[0].evidence[2].explanation; no-entrapped-cell sentence
  accessed_at: '2026-10-14T12:32:51.340272Z'
  support: refutes
  summary: Owner places an unqualified no-entrapped-cell observation under Sr-coating
    evidence, although the original paragraph concerns calcium/polymer coatings.
  snapshot_sha256: 24b79d701283399e97a38f358b031d0e7a8834e6baf54641f9c558b2fca40402
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/acsami.3c13665
  locator: Results and Discussion, calcium/polymer paragraph immediately before Figure
    2; /private/tmp/cmm-round71-strontium-research/natalio2024.txt lines 145–176 and
    matching original XML paragraph; Sr series starts later around Figure 3.
  accessed_at: '2026-10-14T12:32:51.340272Z'
  support: supports
  summary: The fracture observation appears amid calcium-carbonate polymorph and polymer-surface
    discussion, followed by further analysis of the vaterite coating. This is not
    explicitly a Sr-fracture observation.
  snapshot_sha256: ff9b9f4ce957981595f83a3bb46645f899195089d43ddbd937aaaf6438d47ace
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round71-strontium-independent/named-validation-initial.log
  locator: Reviewer-executed locked initial named validation
  accessed_at: '2026-10-14T12:32:51.340272Z'
  support: context_only
  summary: Two records pass structural validation; this does not validate experimental
    attribution.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
assessments:
- assessment_id: context
  area: evidence
  topic: Calcium-context observation versus Sr experiment
  outcome: concern
  summary: The Sr mechanism explanation needs to limit the fracture observation to
    its original calcium/polymer context.
  target_ids:
  - cmmmech:strontianite
  evidence_ids:
  - record
  - primary
findings:
- finding_id: F1
  issue_key: strontianite-round71-calcium-fracture-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Calcium coating fracture observation needs explicit source context
  description: Qualify the no-entrapped-cell sentence as an observation in the calcium/polymer
    discussion, not direct evidence of absent cells in Sr coatings. Retain unresolved
    Sr nucleation explanations, Sr phase/control evidence and uncertainty. Correct
    the source dossier consistently and append actual EDIT history.
  target_ids:
  - cmmmech:strontianite
  field_paths:
  - mechanisms[0].evidence[2].explanation
  evidence_ids:
  - record
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/229
  rule_id: native-review-experimental-scope
  native_severity: minor
  normalization_reason: 'Minor retained: contextual evidence transfer needs correction,
    while phase identity, measured Sr-coating outcomes and independent no-cell controls
    remain supported.'
actions:
- action_id: A1
  description: Curator clarify calcium-specific observation, retain Sr uncertainty,
    update dossier and canonical EDIT history; reviewer reassess corrected frozen
    bytes and save immutable successor.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:strontianite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/strontianite.yaml
    role: maintained scientific record
  acceptance_checks:
  - Confirm original paragraph context before Figure 2 and later distinct Sr series.
  - Clarify owner and dossier without changing supported Sr measurements; save actual
    EDIT history.
  - Repeat named and batch checks; successor must resolve this exact F1 occurrence
    and stable issue key.
limitations:
- Initial corrective observation, not final scientific acceptance; final batch checks
  remain pending.
- Original source does not resolve the molecular pathway or prove cell exclusion in
  Sr coatings.
notes:
- Reviewer has not modified peer owner or canonical history. Curator agreed the context
  concern before correction; immutable finding is saved first.
tags:
- round71
- strontianite
- independent
- experimental-context
```
