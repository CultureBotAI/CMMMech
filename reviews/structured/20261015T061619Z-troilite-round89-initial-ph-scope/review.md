# Independent troilite initial review: distinguish medium pH from reactor pH

- Review: 20261015T061619Z-troilite-round89-initial-ph-scope
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T06:13:54.632426Z
- Finished UTC: 2026-10-15T06:16:19.990229Z
- Reviewer: codex /root (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The record should distinguish reported pre-addition medium pH from the figure reactor time course before calling their difference a source discrepancy. The narrower dissolution observation is not challenged; final whole-record and batch acceptance remains pending.

## Scope And Provenance

Initial scoped assessment of the third mechanism-evidence explanation and its pH interpretation.

Selection: Explicit newly curated troilite owner.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b797f1be3d9d7b45444e0e3f54f3845d8aeeb1ae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:troilite | data/records/troilite.yaml | maintained | Troilite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary methods and graphic cross-check | passed | True | cmmmech:troilite | Read complete eight-page original; independently inspected Methods2.2/2.5 and rendered Figure4A alongside printed p23 prose. |
| Final whole-record batch gates | unavailable | True | cmmmech:troilite | Final batch results and final corrected owner do not yet exist. |

## Scientific And Domain Assessments

### pH measurement basis and timing

consistency: concern. Targets: cmmmech:troilite.

The numerical difference is real, but the record should treat comparability as unresolved instead of implying a demonstrated same-state contradiction.

## Findings

### F1: Separate medium pH from reactor time-course pH

minor / open / confirmed; issue key: troilite-round89-medium-versus-reactor-ph.

The pH passage currently groups a medium preparation value and early reactor measurements as source discrepancies without distinguishing the intervening mineral addition. Retain both observations and state that their timing/material basis is not resolved. Do not assert that mineral addition did cause the rise, but include it as an untested explanation. The separate redox prose/graphic difference can remain qualified.

## Recommended Actions And Acceptance Checks

### A1

Narrow the pH statement in the maintained record and companion dossier, append EDIT history, and independently review final bytes with an explicit successor disposition.

- Distinguish medium preparation from reactor time-course measurements.
- Preserve nominal pH2, Figure4A early/control range, chemical dissolution possibility and remaining redox discrepancy without asserting unmeasured timing.
- Validate corrected owner/history; final batch gates pass and successor explicitly resolves this occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/troilite.yaml; mechanisms[0].evidence[2].explanation | supports | Owner groups nominal medium pH2 and early/control reactor readings near4.5–5 as unresolved source discrepancies. |
| primary | https://doi.org/10.1016/j.hydromet.2010.11.015; Complete CONICET original PDF3–4 and6 / printed20–21 and23; Methods2.2/2.5, Figure4A and adjacent text. Local artifact /private/tmp/cmm-round89-sulfides-research/troilite2011.pdf | partial | Methods specify M88 medium adjusted to pH2. Mineral is then added, and Figure4A reports the experimental mixture. The source discusses acid-consuming dissolution. It does not establish identical sampling times/material states for the medium and plotted early measurements. A post-addition rise is possible, not verified. Prose that the control retains its initial pH can refer to the experimental mixture; it does not explicitly state that the control stayed at2. |

## Limits And Additional Notes

- Scoped initial observation; final whole-record acceptance is pending.
- The paper supplies no resolved paired pre/post-addition pH observations; no causal explanation is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T061619Z-troilite-round89-initial-ph-scope
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent troilite initial review: distinguish medium pH from reactor pH'
started_at: '2026-10-15T06:13:54.632426Z'
finished_at: '2026-10-15T06:16:19.990229Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The round68_iron_sulfides agent authored this record. Root has
    not edited it and captured owner/history through native inspect before assessment.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The record should distinguish reported pre-addition medium pH from the figure
  reactor time course before calling their difference a source discrepancy. The narrower
  dissolution observation is not challenged; final whole-record and batch acceptance
  remains pending.
source:
  git_revision: b797f1be3d9d7b45444e0e3f54f3845d8aeeb1ae
  state: working_tree
  inputs:
  - path: data/records/troilite.yaml
    sha256: c19e1e51c77145cdc8f6bdf56aad20237a9a3cd3b75fe0d634505b5604252ed7
    role: target
  - path: history/records/troilite/2026-10-15T061210Z-codex-7d933f.yaml
    sha256: faa988375fd80f5a98f3ef48d7f6b4a0a572723e0245c327474bc70c58435140
    role: context
targets:
- target_id: cmmmech:troilite
  path: data/records/troilite.yaml
  label: Troilite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/troilite.yaml
    role: scientific record
scope:
  description: Initial scoped assessment of the third mechanism-evidence explanation
    and its pH interpretation.
  selection: Explicit newly curated troilite owner.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - cmmmech:troilite
checks:
- check_id: primary
  name: Primary methods and graphic cross-check
  required: true
  status: passed
  summary: Read complete eight-page original; independently inspected Methods2.2/2.5
    and rendered Figure4A alongside printed p23 prose.
  target_ids:
  - cmmmech:troilite
  evidence_ids:
  - primary
- check_id: final_pending
  name: Final whole-record batch gates
  required: true
  status: unavailable
  summary: Final batch results and final corrected owner do not yet exist.
  target_ids:
  - cmmmech:troilite
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/troilite.yaml
  locator: mechanisms[0].evidence[2].explanation
  accessed_at: '2026-10-15T06:16:19.990229Z'
  support: supports
  summary: Owner groups nominal medium pH2 and early/control reactor readings near4.5–5
    as unresolved source discrepancies.
  snapshot_sha256: c19e1e51c77145cdc8f6bdf56aad20237a9a3cd3b75fe0d634505b5604252ed7
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.hydromet.2010.11.015
  locator: Complete CONICET original PDF3–4 and6 / printed20–21 and23; Methods2.2/2.5,
    Figure4A and adjacent text. Local artifact /private/tmp/cmm-round89-sulfides-research/troilite2011.pdf
  accessed_at: '2026-10-15T06:16:19.990229Z'
  support: partial
  summary: Methods specify M88 medium adjusted to pH2. Mineral is then added, and
    Figure4A reports the experimental mixture. The source discusses acid-consuming
    dissolution. It does not establish identical sampling times/material states for
    the medium and plotted early measurements. A post-addition rise is possible, not
    verified. Prose that the control retains its initial pH can refer to the experimental
    mixture; it does not explicitly state that the control stayed at2.
  snapshot_sha256: 44466a4514b75365b4984a80af7dee6d23ecee78e344c5489f00daebb7610648
assessments:
- assessment_id: ph
  area: consistency
  topic: pH measurement basis and timing
  outcome: concern
  summary: The numerical difference is real, but the record should treat comparability
    as unresolved instead of implying a demonstrated same-state contradiction.
  target_ids:
  - cmmmech:troilite
  evidence_ids:
  - owner
  - primary
findings:
- finding_id: F1
  issue_key: troilite-round89-medium-versus-reactor-ph
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate medium pH from reactor time-course pH
  description: The pH passage currently groups a medium preparation value and early
    reactor measurements as source discrepancies without distinguishing the intervening
    mineral addition. Retain both observations and state that their timing/material
    basis is not resolved. Do not assert that mineral addition did cause the rise,
    but include it as an untested explanation. The separate redox prose/graphic difference
    can remain qualified.
  target_ids:
  - cmmmech:troilite
  field_paths:
  - mechanisms[0].evidence[2].explanation
  evidence_ids:
  - owner
  - primary
  rule_id: compare-like-experimental-states
  native_severity: minor
  normalization_reason: Bounded overstatement of a limitation; identity and conditional
    dissolution comparison remain supported.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/troilite.yaml
    role: scientific record
actions:
- action_id: A1
  description: Narrow the pH statement in the maintained record and companion dossier,
    append EDIT history, and independently review final bytes with an explicit successor
    disposition.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:troilite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/troilite.yaml
    role: scientific record
  acceptance_checks:
  - Distinguish medium preparation from reactor time-course measurements.
  - Preserve nominal pH2, Figure4A early/control range, chemical dissolution possibility
    and remaining redox discrepancy without asserting unmeasured timing.
  - Validate corrected owner/history; final batch gates pass and successor explicitly
    resolves this occurrence.
limitations:
- Scoped initial observation; final whole-record acceptance is pending.
- The paper supplies no resolved paired pre/post-addition pH observations; no causal
  explanation is claimed.
```
