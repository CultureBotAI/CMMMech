# Independent scientific review of Manganese ore

- Review: 20261011T114805Z-manganese-ore-round19-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:44:21Z
- Finished UTC: 2026-10-11T11:48:05Z
- Reviewer: Codex /root/round19_tailings (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major evidence-consistency finding: carbonate absence wording overlooks Figure 11 markers on both traces. Main bounded mobilization claims are supported; correction and a fresh successor are required.

## Scope And Provenance

Complete assigned new record and linked CREATE provenance, with primary identity, mechanism, outcome and scale verification.

Selection: One assigned maintained resource record from round19; source shared with companion iron/manganese record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:manganese-ore | data/records/manganese-ore.yaml | maintained | manganese-ore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:manganese-ore | Reviewer executed to terminal exit 0: two records, zero failed. Reviewed target still matches canonical inspect. |
| Native full checks | passed | True | cmmmech:manganese-ore | Parent executed; reviewer independently read completed terminal receipt and all three logs. /private/tmp/cmm-round19-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 122.38s (0:02:02)<br>Checked 145 record(s); 0 failed.<br>Checked 161 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:manganese-ore | Parent executed; reviewer independently read completed terminal receipt and all three logs. /private/tmp/cmm-round19-final-require.log: Checked 145 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:manganese-ore | Parent executed; reviewer independently read completed terminal receipt and all three logs. /private/tmp/cmm-round19-final-history.log: Checked 161 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Resource processing origin and concept boundary

identity: supported. Targets: cmmmech:manganese-ore.

Natural mixed manganese ore is not a pyrolusite species or processing residue; iron tailings are an explicitly processing-derived mixed feed.

### Microbial mobilization, controls, fractions and recovery boundaries

evidence: concern. Targets: cmmmech:manganese-ore.

Main mobilization observations and analytical/scale limitations are supported; manganese carbonate wording requires explicit text–figure ambiguity.

### Exact working state and actual append-only history

provenance: supported. Targets: cmmmech:manganese-ore.

Canonical inspect captured target/history/schema before assessment; CREATE actor and actual timestamp agree. Completed required checks pass.

## Findings

### manganese-figure11-carbonate-ambiguity: Retain Figure 11 text–figure contradiction in carbonate claim

major / open / confirmed; issue key: round19-manganese-figure11-carbonate.

The record states rhodochrosite peaks are not identified in the two-stage trace. The primary figure draws rhodochrosite legend dots on both traces, while Section 3.3 prose claims absence. Explicitly preserve this inconsistency; neither marker positions nor prose establish verified absence or confirmed new carbonate formation without further author clarification. Qualify the mechanism overview accordingly. Tracked in GitHub issue 71.

## Recommended Actions And Acceptance Checks

### qualify-carbonate-interpretation

State Section 3.3 prose claim and Figure 11 markers on both traces; leave carbonate absence/suppression unresolved. Append actual EDIT provenance and obtain final independent successor.

- Reinspect Figure 11 and Section 3.3; final wording makes both source observations explicit without asserting confirmed phase absence or presence.
- Named validation, just check, require-records and trusted-base history pass on corrected state.
- Fresh successor captures final bytes and exact previous occurrence/issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/manganese-ore.yaml; Complete maintained YAML and linked CREATE history | supports | All fields and actual CREATE event independently read; no asserted criticality designation or invented external material/strain identifiers. |
| primary | https://doi.org/10.1007/s42461-026-01506-2; Full Methods 2.1–2.6, Results 3.1–3.6, Tables 1–7; rendered PDF pages 4–10 Figures 4–13 | supports | Independently read retained 12-page primary PDF and visually inspected all material figures/tables. Processing-derived iron tailings and natural mixed manganese ore are distinct. Figure 5 labels 200 g iron feed and 350 g manganese ore; seven-day adaptation, weekly 300 mL in five increments, triplicates and mixed community match record. Figure 7 cumulative Fe masses differ from source concentration wording. Figure 12 loop concentrations and Table 7 oxide-equivalent analysis support the carefully bounded record. |
| carbonate | https://doi.org/10.1007/s42461-026-01506-2; Section 3.3 and Figure 11; printed page 2026, PDF page 8 | partial | Section 3.3 claims absent carbonate peaks in the two-stage residue, but Figure 11 black rhodochrosite legend markers appear at approximately 24.2 and 31.4 degrees on both upper two-stage and lower single-stage traces. This is an unresolved text–figure inconsistency; markers alone do not prove phase presence, and text alone does not establish reliable absence. |
| search | /private/tmp/cmm-round19-iron-manganese-independent/search.json; Exact query log and hidden/ignored-following dedup.txt | context_only | Two bounded live query first-result sets found no affecting notice. Live Springer DOI/title agrees with retained source. Scoped duplicate results contain newly authored records and prior leads/dossiers; source reuse is not independent replication. |
| gates | /private/tmp/cmm-round19-iron-manganese-independent/initial-gate-receipts.json; Completed receipts and /private/tmp/cmm-round19-final-{batch,require,history}.log | supports | Actual completed native tests: 308 passed/3 skipped, 145 records/161 histories; required-record and trusted-base history each terminal exit 0. Reviewer independently read receipt and logs. |

## Limits And Additional Notes

- Single-stage controls are historical, and no matched sterile two-stage or chemical-iron comparator isolates microbial necessity or mineral contributions.
- Unknown facility identity and unspecified operational analytical fraction limit transfer; independent instrument reprocessing was not performed.
- Section 3.3 carbonate prose conflicts with Figure 11 markers; the initial manganese record requires correction.
- Laboratory/bench outcomes do not demonstrate industrial deployment, closed mass balance, economics or battery qualification.
- Notice searches are bounded first-result sets, not proof that contradictory studies or corrections do not exist.
- Target orientation and source familiarization preceded canonical inspect. Target judgments followed inspect at the start of the recorded review interval. Raw source downloaded by curator was independently inspected, not claimed as an independent reviewer download.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T114805Z-manganese-ore-round19-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Manganese ore
started_at: '2026-10-11T11:44:21Z'
finished_at: '2026-10-11T11:48:05Z'
reviewer:
  identity: Codex /root/round19_tailings
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate parent /root authored these records and CREATE history.
    Reviewer independently read primary full text and visually checked figures/tables,
    performed live notice searches and validations, and made no record edits. Shared
    worktree and curator-acquired raw PDF are disclosed.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'One major evidence-consistency finding: carbonate absence wording overlooks
  Figure 11 markers on both traces. Main bounded mobilization claims are supported;
  correction and a fresh successor are required.'
source:
  git_revision: c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a
  state: working_tree
  inputs:
  - path: data/records/manganese-ore.yaml
    sha256: 1a50ff92f40534128825b5b51889107d69799df261bb04996ee44e4c56ce3e11
    role: target
  - path: history/records/manganese-ore/2026-10-11T114302Z-codex-4e6a73.yaml
    sha256: e37ff8b35c8eb9f909759b520dfdb3ebf4088543cce3acdb1d6bf98562f4e493
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Complete assigned new record and linked CREATE provenance, with primary
    identity, mechanism, outcome and scale verification.
  selection: One assigned maintained resource record from round19; source shared with
    companion iron/manganese record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:manganese-ore
  exclusions:
  - target: Other records, original raw instrument reprocessing and historical comparison
      study reanalysis
    reason: Companion and historical experiments provide context; this verdict is
      specific to the listed target and inspected primary claims.
targets:
- target_id: cmmmech:manganese-ore
  path: data/records/manganese-ore.yaml
  label: manganese-ore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganese-ore.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/iron-ore-tailings.yaml data/records/manganese-ore.yaml
  status: passed
  required: true
  summary: 'Reviewer executed to terminal exit 0: two records, zero failed. Reviewed
    target still matches canonical inspect.'
  target_ids:
  - cmmmech:manganese-ore
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed terminal receipt
    and all three logs. /private/tmp/cmm-round19-final-batch.log: uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 122.38s (0:02:02)

    Checked 145 record(s); 0 failed.

    Checked 161 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:manganese-ore
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed terminal receipt
    and all three logs. /private/tmp/cmm-round19-final-require.log: Checked 145 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:manganese-ore
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base c4b2a6c21a2ff54d1fdd3965ac98a6d90effba7a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read completed terminal receipt
    and all three logs. /private/tmp/cmm-round19-final-history.log: Checked 161 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:manganese-ore
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/manganese-ore.yaml
  locator: Complete maintained YAML and linked CREATE history
  accessed_at: '2026-10-11T11:48:05Z'
  support: supports
  summary: All fields and actual CREATE event independently read; no asserted criticality
    designation or invented external material/strain identifiers.
  snapshot_sha256: 1a50ff92f40534128825b5b51889107d69799df261bb04996ee44e4c56ce3e11
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1007/s42461-026-01506-2
  locator: Full Methods 2.1–2.6, Results 3.1–3.6, Tables 1–7; rendered PDF pages 4–10
    Figures 4–13
  accessed_at: '2026-10-11T11:48:05Z'
  support: supports
  summary: Independently read retained 12-page primary PDF and visually inspected
    all material figures/tables. Processing-derived iron tailings and natural mixed
    manganese ore are distinct. Figure 5 labels 200 g iron feed and 350 g manganese
    ore; seven-day adaptation, weekly 300 mL in five increments, triplicates and mixed
    community match record. Figure 7 cumulative Fe masses differ from source concentration
    wording. Figure 12 loop concentrations and Table 7 oxide-equivalent analysis support
    the carefully bounded record.
  snapshot_sha256: af3826b3ffc8c712ac8b7caa9185e61c45eb4d5bcac328a2a1c2ad530917f00d
- evidence_id: carbonate
  kind: primary_source
  reference: https://doi.org/10.1007/s42461-026-01506-2
  locator: Section 3.3 and Figure 11; printed page 2026, PDF page 8
  accessed_at: '2026-10-11T11:48:05Z'
  support: partial
  summary: Section 3.3 claims absent carbonate peaks in the two-stage residue, but
    Figure 11 black rhodochrosite legend markers appear at approximately 24.2 and
    31.4 degrees on both upper two-stage and lower single-stage traces. This is an
    unresolved text–figure inconsistency; markers alone do not prove phase presence,
    and text alone does not establish reliable absence.
  snapshot_sha256: af3826b3ffc8c712ac8b7caa9185e61c45eb4d5bcac328a2a1c2ad530917f00d
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round19-iron-manganese-independent/search.json
  locator: Exact query log and hidden/ignored-following dedup.txt
  accessed_at: '2026-10-11T11:48:05Z'
  support: context_only
  summary: Two bounded live query first-result sets found no affecting notice. Live
    Springer DOI/title agrees with retained source. Scoped duplicate results contain
    newly authored records and prior leads/dossiers; source reuse is not independent
    replication.
  snapshot_sha256: 01b1f859e1bc111b193c072c7b28171eb0e002039d1ea61cc14aa585b526acab
  search_scope: Hidden and ignored files included, relevant symlinks followed across
    data,research,reviews,history,.claude and named round19 iron/manganese raw directory.
    Binary source independently inspected. Web first-result sets only; no exhaustive
    absence claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round19-iron-manganese-independent/initial-gate-receipts.json
  locator: Completed receipts and /private/tmp/cmm-round19-final-{batch,require,history}.log
  accessed_at: '2026-10-11T11:48:05Z'
  support: supports
  summary: 'Actual completed native tests: 308 passed/3 skipped, 145 records/161 histories;
    required-record and trusted-base history each terminal exit 0. Reviewer independently
    read receipt and logs.'
  snapshot_sha256: 73640a84a624b3375df302586a36481457dbdc3e045f50101b67fe811860b6db
assessments:
- assessment_id: identity
  area: identity
  topic: Resource processing origin and concept boundary
  outcome: supported
  summary: Natural mixed manganese ore is not a pyrolusite species or processing residue;
    iron tailings are an explicitly processing-derived mixed feed.
  target_ids:
  - cmmmech:manganese-ore
  evidence_ids:
  - record
  - primary
  - search
  dimensions:
  - name: material_kind
    value: primary_resource
    definition: Primary Methods 2.1 establishes natural mine feed versus iron-production
      residual feed.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition designation is inherited from constituent
      manganese or iron.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Microbial mobilization, controls, fractions and recovery boundaries
  outcome: concern
  summary: Main mobilization observations and analytical/scale limitations are supported;
    manganese carbonate wording requires explicit text–figure ambiguity.
  target_ids:
  - cmmmech:manganese-ore
  evidence_ids:
  - record
  - primary
  - carbonate
  dimensions:
  - name: organism_and_biomass
    value: Living mixed fen-derived metal-reducing community; fermented Typha latifolia
      plus sucrose nutrients
    definition: Primary does not resolve a causal member, authenticated strain or
      sterile manganese stage; possible carryover remains explicit.
    evidence_ids:
    - record
    - primary
  - name: substrate_and_pretreatment
    value: Mixed Keweenaw mine ore below 3 mm
    definition: XRD phases describe mixed feed; elemental percentages calculated from
      XRD are not independent bulk assays.
    evidence_ids:
    - record
    - primary
  - name: conditions_controls_fraction
    value: Triplicate two-stage 250 mL flasks; historical single-stage comparators;
      colorimetric Mn/Fe(II) assays without operational dissolved fraction
    definition: No matched sterile two-stage or chemical-Fe comparator; pH and culture
      configuration prevent isolated causal interpretation.
    evidence_ids:
    - record
    - primary
  - name: scale_and_outcome
    value: 123-day laboratory mobilization and 19 L bench apparatus
    definition: Cumulative assayed metal, concentration, calculated loop balance and
      heat-treated oxide-equivalent composition are distinct; no industrial or battery-grade
      qualification.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Exact working state and actual append-only history
  outcome: supported
  summary: Canonical inspect captured target/history/schema before assessment; CREATE
    actor and actual timestamp agree. Completed required checks pass.
  target_ids:
  - cmmmech:manganese-ore
  evidence_ids:
  - record
  - gates
findings:
- finding_id: manganese-figure11-carbonate-ambiguity
  issue_key: round19-manganese-figure11-carbonate
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Retain Figure 11 text–figure contradiction in carbonate claim
  description: The record states rhodochrosite peaks are not identified in the two-stage
    trace. The primary figure draws rhodochrosite legend dots on both traces, while
    Section 3.3 prose claims absence. Explicitly preserve this inconsistency; neither
    marker positions nor prose establish verified absence or confirmed new carbonate
    formation without further author clarification. Qualify the mechanism overview
    accordingly. Tracked in GitHub issue 71.
  target_ids:
  - cmmmech:manganese-ore
  field_paths:
  - mechanisms[0].description
  - mechanisms[0].evidence[3].explanation
  evidence_ids:
  - record
  - carbonate
  ownership_note: Correct maintained manganese record and mirrored source dossier;
    append actual EDIT history. Preserve this initial review.
  rule_id: preserve-contradictory-evidence
actions:
- action_id: qualify-carbonate-interpretation
  description: State Section 3.3 prose claim and Figure 11 markers on both traces;
    leave carbonate absence/suppression unresolved. Append actual EDIT provenance
    and obtain final independent successor.
  finding_ids:
  - manganese-figure11-carbonate-ambiguity
  target_ids:
  - cmmmech:manganese-ore
  ownership_note: Maintained record and corresponding source dossier; issue https://github.com/CultureBotAI/CMMMech/issues/71.
  acceptance_checks:
  - Reinspect Figure 11 and Section 3.3; final wording makes both source observations
    explicit without asserting confirmed phase absence or presence.
  - Named validation, just check, require-records and trusted-base history pass on
    corrected state.
  - Fresh successor captures final bytes and exact previous occurrence/issue key.
limitations:
- Single-stage controls are historical, and no matched sterile two-stage or chemical-iron
  comparator isolates microbial necessity or mineral contributions.
- Unknown facility identity and unspecified operational analytical fraction limit
  transfer; independent instrument reprocessing was not performed.
- Section 3.3 carbonate prose conflicts with Figure 11 markers; the initial manganese
  record requires correction.
- Laboratory/bench outcomes do not demonstrate industrial deployment, closed mass
  balance, economics or battery qualification.
- Notice searches are bounded first-result sets, not proof that contradictory studies
  or corrections do not exist.
tags:
- round19
- independent
- scientific-review
- resource
notes:
- Target orientation and source familiarization preceded canonical inspect. Target
  judgments followed inspect at the start of the recorded review interval. Raw source
  downloaded by curator was independently inspected, not claimed as an independent
  reviewer download.
```
