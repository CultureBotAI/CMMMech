# Independent initial scientific review of phosphate-ore tailings

- Review: 20261016T043352Z-phosphate-ore-tailings-round111-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T04:28:40.901382Z
- Finished UTC: 2026-10-16T04:33:52.243238Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor context defects require correction: Figures1–2 do not show an explicit feed/no-feed comparison, and Figures3–4 specify75micrometres for the accepted time-series arms. The reported tailings45%/22.5% values and bounded culture-associated interpretation are supported. Final batch checks remain pending.

## Scope And Provenance

Complete one-record scientific assessment and original seven-page source, with a bounded initial corrective observation before the final batch completes.

Selection: Exactly one independently assigned maintained owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a43774bf15a206b04e59c7525e93fdb334325d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:phosphate-ore-tailings | data/records/phosphate-ore-tailings.yaml | maintained | Phosphate ore tailings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:phosphate-ore-tailings | Checked1record;0failed. |
| Final batch structural and history checks | unavailable | True | cmmmech:phosphate-ore-tailings | Coordinator final batch is running. No terminal success is claimed by this partial initial observation. |

## Scientific And Domain Assessments

### Resource and organism scope

identity: supported. Targets: cmmmech:phosphate-ore-tailings.

Process-defined phosphate tailings are distinct from concentrate, commodity and phosphogypsum; species identifiers match author labels without strain authentication.

### Reported aggregate leaching fractions and uncertainty

evidence: supported. Targets: cmmmech:phosphate-ore-tailings.

Original time-series plots support45%tailings bacterial and22.5%fungal. Source totals, assay limits, missing controls, timing/inoculum/unit contradictions and unmeasured molecular pathways remain explicit.

### Displayed comparison and sample preparation

consistency: concern. Targets: cmmmech:phosphate-ore-tailings.

Two figure-level context corrections are required; the limited accepted leaching observation remains defensible.

## Findings

### growth-comparison: Growth figures do not display the claimed feed comparison

minor / open / confirmed; issue key: cmmmech.phosphate-ore-tailings.growth-comparison.

Mechanism context says Figures1–2 compare growth with and without feed. The original figures show pure-culture growth curves, with no explicit paired feed/no-feed series. Retain the absence of uninoculated leaching controls and avoid asserting a comparison supported only by a section heading.

### time-series-particle-size: Accepted time-series particle size is omitted and misleadingly assigned to optimization

minor / open / confirmed; issue key: cmmmech.phosphate-ore-tailings.time-series-particle-size.

Mechanism context gives received tailings size about147micrometres and says separately ground classes belong to later optimization. Figures3–4, which support the accepted45%/22.5% outcomes, explicitly use75micrometres. State the figure-specific size for both time-series arms and retain received-feed and later optimization scope separately.

## Recommended Actions And Acceptance Checks

### correct-context

Correct the two context sentences in the maintained owner; retain accepted outcomes and uncertainty. Append actual EDIT history and save a successor of exact final bytes.

- Compare corrected growth wording with original Figures1–2.
- Explicitly map75micrometres to both Figures3–4 time-series arms.
- Repeat named validation and canonical history validation; verify final batch terminal receipt for corrected bytes.
- Retain both exact prior finding occurrences in the successor review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/phosphate-ore-tailings.yaml; Complete target, linked canonical CREATE, schema and frozen source dossier captured by native inspect before judgment. | supports | The owner remains identical to captured bytes; no reviewer target edits. |
| primary | https://scholars.direct/Articles/microbiology/amr-2-009.pdf; Complete original seven-page published PDF pp.54–60; independently read all text and visually inspected all seven page renders, including Table1/Figures1–8. | supports | DOI10.36959/958/570, Somasundaran et al.2018. Tailings and concentrate are distinct feeds; controls, assay, timing, inoculum and source arithmetic limits are explicit. |
| growth | https://scholars.direct/Articles/microbiology/amr-2-009.pdf; Printed p.56, Figures1–2; original phosphate-page-3.png. | refutes | Each caption describes a pure culture. Figure1 plots bacterial OD and pH; Figure2 a single fungal dry-weight series. No explicit paired with-feed/without-feed series is displayed, despite the broader preceding section heading. |
| particles | https://scholars.direct/Articles/microbiology/amr-2-009.pdf; Printed p.57, Figures3–4 captions; initial-feed description p.54. | refutes | Both accepted time-series captions explicitly specify particle size75micrometres. About147micrometres is the received tailings description; the figure-specific size must not be assigned only to later optimization. |
| identifiers | /private/tmp/cmm-round111-uranium-research/tailings-review-web.json; Live official NCBI Taxonomy species920 and5061 and publisher title/authors/DOI/date, independently opened16October2026. | supports | Taxon920 identifies Acidithiobacillus ferrooxidans;5061 identifies Aspergillus niger. Neither determines the unspecified study strain or authenticates the source isolate. |
| named | /private/tmp/cmm-round111-uranium-research/tailings-review-validation-initial.json; Actual completed independent strict named validation, terminal session64935. | supports | Checked1record;0failed. Structural success does not establish scientific accuracy. |

## Limits And Additional Notes

- Partial initial corrective observation: final batch gates are pending and no final acceptance is claimed.
- Original source has unresolved assay/control/protocol/arithmetic limitations; narrow culture-associated observations do not establish microbial necessity, a defined metabolite pathway or recovered product.
- No independent laboratory replication or strain-stock authentication; this is an independent agent scientific review, not external human peer review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T043352Z-phosphate-ore-tailings-round111-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial scientific review of phosphate-ore tailings
started_at: '2026-10-16T04:28:40.901382Z'
finished_at: '2026-10-16T04:33:52.243238Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this target/history/dossier. Reviewer authored
    unrelated schoepite/becquerelite owners; independently read the original full
    article and figures and verified species identifiers without editing this target.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Two minor context defects require correction: Figures1–2 do not show an
  explicit feed/no-feed comparison, and Figures3–4 specify75micrometres for the accepted
  time-series arms. The reported tailings45%/22.5% values and bounded culture-associated
  interpretation are supported. Final batch checks remain pending.'
source:
  git_revision: 6a43774bf15a206b04e59c7525e93fdb334325d6
  state: working_tree
  inputs:
  - path: data/records/phosphate-ore-tailings.yaml
    sha256: e2cacdf9358c014fd03beff8fbcb5a44e24ccb1f0fd0e65e0063e4698afbf8a1
    role: target
  - path: history/records/phosphate-ore-tailings/2026-10-16T042651Z-codex-0ce69c.yaml
    sha256: da6d32773eb749a630a857aeeabd590ad6ab10020c9afd15e5a8abad307cb159
    role: context
  - path: research/sources/round111-resources/20261016-source-investigation.json
    sha256: ae1c55020a269f68377fd9a6f714f404784407b2479cd49eb8bfd3eb3f115d12
    role: context
  - path: research/sources/round111-resources/20261016-source-investigation.md
    sha256: 067cae89035255c561c3378a131dc980587f104c9f50e4c67e7a0d6e30ff05ae
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:phosphate-ore-tailings
  path: data/records/phosphate-ore-tailings.yaml
  label: Phosphate ore tailings
  kind: maintained
  ownership_note: Maintained native YAML; root curator owns scientific corrections.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-ore-tailings.yaml
    role: maintained_record
scope:
  description: Complete one-record scientific assessment and original seven-page source,
    with a bounded initial corrective observation before the final batch completes.
  selection: Exactly one independently assigned maintained owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:phosphate-ore-tailings
checks:
- check_id: named
  name: Independent named strict validation
  status: passed
  required: true
  summary: Checked1record;0failed.
  target_ids:
  - cmmmech:phosphate-ore-tailings
  command: uv run --locked cmmmech validate data/records/phosphate-ore-tailings.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch-pending
  name: Final batch structural and history checks
  status: unavailable
  required: true
  summary: Coordinator final batch is running. No terminal success is claimed by this
    partial initial observation.
  target_ids:
  - cmmmech:phosphate-ore-tailings
  command: just check
  evidence_ids:
  - owner
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/phosphate-ore-tailings.yaml
  locator: Complete target, linked canonical CREATE, schema and frozen source dossier
    captured by native inspect before judgment.
  summary: The owner remains identical to captured bytes; no reviewer target edits.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: supports
  snapshot_sha256: e2cacdf9358c014fd03beff8fbcb5a44e24ccb1f0fd0e65e0063e4698afbf8a1
- evidence_id: primary
  kind: primary_source
  reference: https://scholars.direct/Articles/microbiology/amr-2-009.pdf
  locator: Complete original seven-page published PDF pp.54–60; independently read
    all text and visually inspected all seven page renders, including Table1/Figures1–8.
  summary: DOI10.36959/958/570, Somasundaran et al.2018. Tailings and concentrate
    are distinct feeds; controls, assay, timing, inoculum and source arithmetic limits
    are explicit.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: supports
  snapshot_sha256: aa1016557644efc02904878a6784fe8f070676060a456cc8c1e7dba21537646f
- evidence_id: growth
  kind: primary_source
  reference: https://scholars.direct/Articles/microbiology/amr-2-009.pdf
  locator: Printed p.56, Figures1–2; original phosphate-page-3.png.
  summary: Each caption describes a pure culture. Figure1 plots bacterial OD and pH;
    Figure2 a single fungal dry-weight series. No explicit paired with-feed/without-feed
    series is displayed, despite the broader preceding section heading.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: refutes
  snapshot_sha256: 9f6a48c8654246cfc97449834ac15e52551e09c79b158615a6ca1851a12ee35c
- evidence_id: particles
  kind: primary_source
  reference: https://scholars.direct/Articles/microbiology/amr-2-009.pdf
  locator: Printed p.57, Figures3–4 captions; initial-feed description p.54.
  summary: Both accepted time-series captions explicitly specify particle size75micrometres.
    About147micrometres is the received tailings description; the figure-specific
    size must not be assigned only to later optimization.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: refutes
  snapshot_sha256: 6d0a1a560fd54d11c2e4951a5e1adb51b01af946523f2641e80c562a3c974577
- evidence_id: identifiers
  kind: authority
  reference: /private/tmp/cmm-round111-uranium-research/tailings-review-web.json
  locator: Live official NCBI Taxonomy species920 and5061 and publisher title/authors/DOI/date,
    independently opened16October2026.
  summary: Taxon920 identifies Acidithiobacillus ferrooxidans;5061 identifies Aspergillus
    niger. Neither determines the unspecified study strain or authenticates the source
    isolate.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: supports
  snapshot_sha256: 71df3ca2433becbedb5c8f86e3f5d968b62cd38d0f10ffb71b5ff5db8e62a723
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round111-uranium-research/tailings-review-validation-initial.json
  locator: Actual completed independent strict named validation, terminal session64935.
  summary: Checked1record;0failed. Structural success does not establish scientific
    accuracy.
  accessed_at: '2026-10-16T04:33:52.243238Z'
  support: supports
  snapshot_sha256: cbaa80d2c6f9f48b034a0dd770a7f5f54be4aa8cd977f92c379503d53da0a46f
assessments:
- assessment_id: identity
  area: identity
  topic: Resource and organism scope
  outcome: supported
  summary: Process-defined phosphate tailings are distinct from concentrate, commodity
    and phosphogypsum; species identifiers match author labels without strain authentication.
  target_ids:
  - cmmmech:phosphate-ore-tailings
  evidence_ids:
  - owner
  - primary
  - identifiers
- assessment_id: quantitative
  area: evidence
  topic: Reported aggregate leaching fractions and uncertainty
  outcome: supported
  summary: Original time-series plots support45%tailings bacterial and22.5%fungal.
    Source totals, assay limits, missing controls, timing/inoculum/unit contradictions
    and unmeasured molecular pathways remain explicit.
  target_ids:
  - cmmmech:phosphate-ore-tailings
  evidence_ids:
  - owner
  - primary
- assessment_id: protocol
  area: consistency
  topic: Displayed comparison and sample preparation
  outcome: concern
  summary: Two figure-level context corrections are required; the limited accepted
    leaching observation remains defensible.
  target_ids:
  - cmmmech:phosphate-ore-tailings
  evidence_ids:
  - growth
  - particles
  - owner
findings:
- finding_id: growth-comparison
  issue_key: cmmmech.phosphate-ore-tailings.growth-comparison
  title: Growth figures do not display the claimed feed comparison
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - cmmmech:phosphate-ore-tailings
  field_paths:
  - mechanisms[0].context
  evidence_ids:
  - growth
  - owner
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-ore-tailings.yaml
    role: maintained_record
  description: Mechanism context says Figures1–2 compare growth with and without feed.
    The original figures show pure-culture growth curves, with no explicit paired
    feed/no-feed series. Retain the absence of uninoculated leaching controls and
    avoid asserting a comparison supported only by a section heading.
- finding_id: time-series-particle-size
  issue_key: cmmmech.phosphate-ore-tailings.time-series-particle-size
  title: Accepted time-series particle size is omitted and misleadingly assigned to
    optimization
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - cmmmech:phosphate-ore-tailings
  field_paths:
  - mechanisms[0].context
  evidence_ids:
  - particles
  - owner
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-ore-tailings.yaml
    role: maintained_record
  description: Mechanism context gives received tailings size about147micrometres
    and says separately ground classes belong to later optimization. Figures3–4, which
    support the accepted45%/22.5% outcomes, explicitly use75micrometres. State the
    figure-specific size for both time-series arms and retain received-feed and later
    optimization scope separately.
actions:
- action_id: correct-context
  description: Correct the two context sentences in the maintained owner; retain accepted
    outcomes and uncertainty. Append actual EDIT history and save a successor of exact
    final bytes.
  finding_ids:
  - growth-comparison
  - time-series-particle-size
  target_ids:
  - cmmmech:phosphate-ore-tailings
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/phosphate-ore-tailings.yaml
    role: maintained_record
  acceptance_checks:
  - Compare corrected growth wording with original Figures1–2.
  - Explicitly map75micrometres to both Figures3–4 time-series arms.
  - Repeat named validation and canonical history validation; verify final batch terminal
    receipt for corrected bytes.
  - Retain both exact prior finding occurrences in the successor review.
limitations:
- 'Partial initial corrective observation: final batch gates are pending and no final
  acceptance is claimed.'
- Original source has unresolved assay/control/protocol/arithmetic limitations; narrow
  culture-associated observations do not establish microbial necessity, a defined
  metabolite pathway or recovered product.
- No independent laboratory replication or strain-stock authentication; this is an
  independent agent scientific review, not external human peer review.
```
