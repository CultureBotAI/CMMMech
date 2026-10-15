# Independent wood-ash statistical wording finding

- Review: 20261015T140555Z-wood-ash-round96-statistical-wording-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T13:59:15Z
- Finished UTC: 2026-10-15T14:05:55.210218Z
- Reviewer: codex /root (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor wording correction: state that no statistically significant increase was demonstrated, rather than implying numerically identical plant phosphorus. The narrower solution-phosphate observation and qualified total-P interpretation are supported; final batch gates remain pending.

## Scope And Provenance

Complete record scientific assessment, with final batch checks pending.

Selection: Independent cross-review of the newly curated wood-ash owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4ef2e0dd88837ef729839ffde8ed828bcbb59cda.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:wood-ash | data/records/wood-ash.yaml | maintained | Wood ash |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary-source and identity check | passed | True | cmmmech:wood-ash | Read complete original publisher HTML, all five native tables, Figures1–4, and NCBI80663 species authority. |
| Named strict validation | passed | True | cmmmech:wood-ash | Checked one record; zero failed. |
| Final batch gates | unavailable | True | cmmmech:wood-ash | Final corrected batch validation and history receipt not yet available. |

## Scientific And Domain Assessments

### Secondary resource and experimental organisms

identity: supported. Targets: cmmmech:wood-ash.

Distinct hardened wood-combustion resource; sample-specific ground ash and live seedling-associated fungi. No constituent criticality is inherited; no strain mapping invented.

### Solution phosphate versus total and plant phosphorus

evidence: concern. Targets: cmmmech:wood-ash.

The narrow solution observation and qualified causal limitations are supported, but description should specify statistical rather than literal equality.

Living mycorrhizal seedlings in nonaxenic, unmatched-pH pots; high-N elemental endpoints; 120days, six g/L ash, five replicates. Extracted soil solution concentration is not a recovery rate. Oxalate and selective Ca transport are proposals; plant uptake and total source budgets do not establish isolated product or industrial deployment.

## Findings

### F1: Qualify the null phosphorus comparison statistically

minor / open / confirmed; issue key: wood-ash-round96-statistical-null-wording.

Mechanism description says plant phosphorus content was not greater. Figure2d and Table4 support no statistically significant increase; plant-fraction means4.4 versus4.3 percent differ numerically. Existing later evidence correctly says an increase is not demonstrated. Align the lead description with this precise interpretation.

## Recommended Actions And Acceptance Checks

### A1

Replace the null comparison with did not show a statistically significant increase; append actual EDIT provenance and retain prior review.

- Description preserves statistical null without claiming numerical equality.
- Named and batch checks pass.
- Independent successor resolves this exact finding against final bytes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.1111/j.1574-6941.2003.tb01051.x; Complete original HTML, sections2–4 and Tables1–5; artifact /private/tmp/cmm-round96-resources-research/mahmood2003.html | supports | Table4 has plant-P fractions4.3±0.2 versus4.4±0.1 in the same statistical group. Solution-phosphate elevation is supported; total mobilisation has no significant increase. |
| figure2 | https://academic.oup.com/femsec/article/43/1/121/510286; Original Figure2 paneld; artifact /private/tmp/cmm-round96-resources-research/mahmood2003-fig2.jpeg | supports | All +Ash plant-P arms share the letterx; bars need not be numerically identical to support a nonsignificant comparison. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=80663; Official NCBI XML TaxId, ScientificName and Rank; artifact /private/tmp/cmm-round96-resources-research/ncbi-80663.xml | supports | 80663 is Piloderma croceum at species rank, not an isolate identifier. |
| named | uv run --locked cmmmech validate data/records/wood-ash.yaml; Actual independent command log; artifact /private/tmp/cmm-round96-wood-named-initial.log | supports | Named validation passed one record, zero failures. |

## Limits And Additional Notes

- No industrial process, isolated recovery product or fungus-exclusive dissolution is demonstrated.
- Ash fraction and wood blend remain unresolved; species authority does not identify Piloderma sp.1 or experimental isolates.
- Correction/retraction searches were bounded to exact DOI/title queries and returned results; no exhaustive global absence claim. The full2001 predecessor graphics remain inaccessible and are not accepted as new mechanism evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T140555Z-wood-ash-round96-statistical-wording-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent wood-ash statistical wording finding
started_at: '2026-10-15T13:59:15Z'
finished_at: '2026-10-15T14:05:55.210218Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The frontier agent authored wood ash; root inspected frozen
    bytes and independently checked the complete primary HTML, all five tables and
    four original figures, without editing this owner.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One minor wording correction: state that no statistically significant increase
  was demonstrated, rather than implying numerically identical plant phosphorus. The
  narrower solution-phosphate observation and qualified total-P interpretation are
  supported; final batch gates remain pending.'
source:
  git_revision: 4ef2e0dd88837ef729839ffde8ed828bcbb59cda
  state: working_tree
  inputs:
  - path: data/records/wood-ash.yaml
    sha256: 9d85481ac0f6fb723374379cd5e99f7fa797cb03fe06343779518922eb804132
    role: target
  - path: history/records/wood-ash/2026-10-15T135430Z-codex-e412cf.yaml
    sha256: 33f6e78bc4f496b1c1dadaf338442535848c5a9cdfa2dc5068654eeb6d32564a
    role: context
scope:
  description: Complete record scientific assessment, with final batch checks pending.
  selection: Independent cross-review of the newly curated wood-ash owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:wood-ash
targets:
- target_id: cmmmech:wood-ash
  path: data/records/wood-ash.yaml
  label: Wood ash
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wood-ash.yaml
    role: maintained record
checks:
- check_id: science
  name: Primary-source and identity check
  required: true
  status: passed
  summary: Read complete original publisher HTML, all five native tables, Figures1–4,
    and NCBI80663 species authority.
  target_ids:
  - cmmmech:wood-ash
  evidence_ids:
  - primary
  - figure2
  - taxonomy
- check_id: named
  name: Named strict validation
  command: uv run --locked cmmmech validate data/records/wood-ash.yaml
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Checked one record; zero failed.
  target_ids:
  - cmmmech:wood-ash
  evidence_ids:
  - named
- check_id: final-batch
  name: Final batch gates
  required: true
  status: unavailable
  summary: Final corrected batch validation and history receipt not yet available.
  target_ids:
  - cmmmech:wood-ash
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1111/j.1574-6941.2003.tb01051.x
  locator: Complete original HTML, sections2–4 and Tables1–5; artifact /private/tmp/cmm-round96-resources-research/mahmood2003.html
  accessed_at: '2026-10-15T14:05:55.210218Z'
  support: supports
  snapshot_sha256: 574120109b9006dddcf7a36942dc304c0d66995f783c8df5dfc19f53390af99b
  summary: Table4 has plant-P fractions4.3±0.2 versus4.4±0.1 in the same statistical
    group. Solution-phosphate elevation is supported; total mobilisation has no significant
    increase.
- evidence_id: figure2
  kind: primary_source
  reference: https://academic.oup.com/femsec/article/43/1/121/510286
  locator: Original Figure2 paneld; artifact /private/tmp/cmm-round96-resources-research/mahmood2003-fig2.jpeg
  accessed_at: '2026-10-15T14:05:55.210218Z'
  support: supports
  snapshot_sha256: dc8052950f3c9152046c5f6ac1c10c0d0201aedc85f43be461aa4444e4682219
  summary: All +Ash plant-P arms share the letterx; bars need not be numerically identical
    to support a nonsignificant comparison.
- evidence_id: taxonomy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=80663
  locator: Official NCBI XML TaxId, ScientificName and Rank; artifact /private/tmp/cmm-round96-resources-research/ncbi-80663.xml
  accessed_at: '2026-10-15T14:05:55.210218Z'
  support: supports
  snapshot_sha256: deba69f4320f5968025cfe520edac4cdbe2cd6dcdde46ded67e0f17d1fb32a34
  summary: 80663 is Piloderma croceum at species rank, not an isolate identifier.
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/wood-ash.yaml
  locator: Actual independent command log; artifact /private/tmp/cmm-round96-wood-named-initial.log
  accessed_at: '2026-10-15T14:05:55.210218Z'
  support: supports
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  summary: Named validation passed one record, zero failures.
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary resource and experimental organisms
  outcome: supported
  target_ids:
  - cmmmech:wood-ash
  evidence_ids:
  - primary
  - taxonomy
  summary: Distinct hardened wood-combustion resource; sample-specific ground ash
    and live seedling-associated fungi. No constituent criticality is inherited; no
    strain mapping invented.
- assessment_id: mechanism
  area: evidence
  topic: Solution phosphate versus total and plant phosphorus
  outcome: concern
  target_ids:
  - cmmmech:wood-ash
  evidence_ids:
  - primary
  - figure2
  summary: The narrow solution observation and qualified causal limitations are supported,
    but description should specify statistical rather than literal equality.
  details: Living mycorrhizal seedlings in nonaxenic, unmatched-pH pots; high-N elemental
    endpoints; 120days, six g/L ash, five replicates. Extracted soil solution concentration
    is not a recovery rate. Oxalate and selective Ca transport are proposals; plant
    uptake and total source budgets do not establish isolated product or industrial
    deployment.
findings:
- finding_id: F1
  issue_key: wood-ash-round96-statistical-null-wording
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the null phosphorus comparison statistically
  description: Mechanism description says plant phosphorus content was not greater.
    Figure2d and Table4 support no statistically significant increase; plant-fraction
    means4.4 versus4.3 percent differ numerically. Existing later evidence correctly
    says an increase is not demonstrated. Align the lead description with this precise
    interpretation.
  target_ids:
  - cmmmech:wood-ash
  field_paths:
  - mechanisms[0].description
  evidence_ids:
  - primary
  - figure2
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wood-ash.yaml
    role: maintained record
  rule_id: preserve-null-outcome-scope
  native_severity: minor
  normalization_reason: Bounded wording precision; the record already retains correct
    numbers and statistical context.
actions:
- action_id: A1
  description: Replace the null comparison with did not show a statistically significant
    increase; append actual EDIT provenance and retain prior review.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:wood-ash
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/wood-ash.yaml
    role: maintained record
  acceptance_checks:
  - Description preserves statistical null without claiming numerical equality.
  - Named and batch checks pass.
  - Independent successor resolves this exact finding against final bytes.
limitations:
- No industrial process, isolated recovery product or fungus-exclusive dissolution
  is demonstrated.
- Ash fraction and wood blend remain unresolved; species authority does not identify
  Piloderma sp.1 or experimental isolates.
- Correction/retraction searches were bounded to exact DOI/title queries and returned
  results; no exhaustive global absence claim. The full2001 predecessor graphics remain
  inaccessible and are not accepted as new mechanism evidence.
```
