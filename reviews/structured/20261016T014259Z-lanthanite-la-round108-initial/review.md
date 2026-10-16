# Initial independent review of lanthanite-(La) thermal-arm provenance

- Review: 20261016T014259Z-lanthanite-la-round108-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T01:36:06.720569Z
- Finished UTC: 2026-10-16T01:42:59.651764Z
- Reviewer: codex /root/round104_borates (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor protocol-attribution correction is supported. Mineral identity and bounded phase outcomes are supported; required final batch checks remain pending.

## Scope And Provenance

Complete exact La owner, species identity, separate synthetic thermal/rehydration arm and history; initial observation before remediation.

Selection: Assigned named owner; native inspect preceded judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26661b7f033d4bdb915e48e71080aa5774b4c3d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lanthanite-la | data/records/lanthanite-la.yaml | maintained | Lanthanite-(La) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:lanthanite-la | Checked 2 record(s); 0 failed. |
| Required final batch gate pending | unavailable | True | cmmmech:lanthanite-la | Coordinator batch is still running on frozen original inputs. No final terminal outcome claimed; this initial observation records the supported finding before correction. |
| Required final corpus gate pending | unavailable | True | cmmmech:lanthanite-la | Coordinator batch is still running on frozen original inputs. No final terminal outcome claimed; this initial observation records the supported finding before correction. |
| Required final history gate pending | unavailable | True | cmmmech:lanthanite-la | Coordinator batch is still running on frozen original inputs. No final terminal outcome claimed; this initial observation records the supported finding before correction. |

## Scientific And Domain Assessments

### Distinct mineral identity and natural/synthetic boundary

identity: supported. Targets: cmmmech:lanthanite-la.

Current IMA identity, historical locality caution and synthetic-analogue boundary are supported.

### Observed phase outcomes and uncertainty

evidence: supported. Targets: cmmmech:lanthanite-la.

The7h dry-heating product and89/11wt% partial return at120.5h are supported; total equilibrium and recovery yields are not asserted.

### Separate experiment synthesis scale

provenance: concern. Targets: cmmmech:lanthanite-la.

The general solution recipe is transferred to the separate2g thermal aliquot without an explicit source linkage or scale qualification.

### Canonical CREATE history

provenance: supported. Targets: cmmmech:lanthanite-la.

Current actor/model/tool, target and actual history are correct.

## Findings

### F1: Separate thermal sample inherits an unreported synthesis scale

minor / open / confirmed; issue key: round108-lanthanite-la-thermal-synthesis-scale.

The owner states the general40mL50mMLa plus40mL50mMcarbonate recipe and immediately calls the dry-heating aliquot a2g portion of the resulting solid. The separate Methods p948 arm specifies ambient homogeneous-mixing synthesis but does not report scale or batch count. The general recipe contains2mmolLa, corresponding to about0.60g idealLa2(CO3)3·8H2O if allLa entered that phase; this is a consistency calculation, not an observed yield. It reinforces why a direct single-batch relationship must not be asserted. Remove the transferred recipe from this separate arm or explicitly leave its scale unspecified. The2g heating mass and phase outcomes remain supported.

## Recommended Actions And Acceptance Checks

### A1

Describe the separate dry-heating sample as synthesized by homogeneous mixing at21C and state that its synthesis scale or batch count is unspecified; preserve2g/0.2g/0.3g experimental masses and phase outcomes.

- Re-read Methods p946 and separate p948 arm; do not infer the2g sample came from one stated40+40mLbatch.
- Append canonical EDIT history and distinct inline event, repeat named and affected final gates, then capture final bytes in a successor review resolving this exact occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lanthanite-la.yaml; Exact original owner after initial native inspect. | supports | The context links the general40mL recipe directly to a2g portion of its resulting solid. |
| history | history/records/lanthanite-la/2026-10-16T013309Z-codex-a2893c.yaml; Complete canonical CREATE and inline event. | supports | Correct current actor, target and session; no changes by reviewer. |
| primary | https://doi.org/10.1021/acs.cgd.4c01168; Published article Methods p946 general homogeneous-mixing protocol and separate p948 Lanthanite Dehydration and Rehydration Experiments; Figures10-13 and SI TableSI-1 also inspected. | partial | Page948 states ambient21C homogeneous-mixing synthesis followed by a2g solid aliquot, but does not specify the synthesis scale or number of batches used for that aliquot. |
| si | https://doi.org/10.1021/acs.cgd.4c01168.s001; Complete8page supplement; TableSI-1 and Figure12 in the main article. | supports | Both phases remain at120.5h; the owner correctly limits return to89wt%lanthanite/11wt%tengerite. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitionsp1 and La speciesrowp121 independently viewed. | supports | Renamed1987s.p. La species identity is correctly separated from unique approval IDs. |
| natural | https://doi.org/10.1180/minmag.1989.053.373.17; Complete original4pages, Table1 and Figure1. | supports | Locality and composition caution is supported. |
| named | /private/tmp/cmm-round108-borates-research/review-ree-named-validation.json; Independent actual terminal named-validation receipt. | supports | Checked2records;0failed. Structural validation does not resolve protocol attribution. |
| baseline | /private/tmp/cmm-round108-baseline.json; Actual coordinator baseline receipt; independently checked completed exit0 and log digest. | context_only | Baseline context, not final-state proof. |

## Limits And Additional Notes

- Final just check, strict corpus validation and history validation are pending at this observation; passing baseline and named validation are not substitutes.
- Mass calculation is a consistency bound for ideal hydratedLa carbonate, not a reported synthesis yield or new chemical assay.
- No author contact, independent experimental replication or complete phase mass balance performed.
- Original bytes and initial native capture are preserved. Curator must wait for coordinator signal before editing frozen inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T014259Z-lanthanite-la-round108-initial
kind: record
repository: CultureBotAI/CMMMech
title: Initial independent review of lanthanite-(La) thermal-arm provenance
started_at: '2026-10-16T01:36:06.720569Z'
finished_at: '2026-10-16T01:42:59.651764Z'
reviewer:
  identity: codex /root/round104_borates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator; no edits to this owner/history/dossier.
    Shared primary artifacts independently read after native inspect. Reviewer authored
    unrelated boracite/larderellite.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor protocol-attribution correction is supported. Mineral identity
  and bounded phase outcomes are supported; required final batch checks remain pending.
source:
  git_revision: 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  state: working_tree
  inputs:
  - path: data/records/lanthanite-la.yaml
    sha256: ffba6de0e9dd8b228659c7b623c463711f3970b373865c9d049dbc0b80889aeb
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/lanthanite-la/2026-10-16T013309Z-codex-a2893c.yaml
    sha256: 17e12b77b042a50daff947a5758a1e3746b76c61f9adbd055937143588a46a9d
    role: context
  - path: research/sources/round108-ree/20261016T013538Z-source-investigation.json
    sha256: db6845df76499b8d4a58188ac075fbb8c063a8653a1f731c9aa45efedff808bb
    role: context
  - path: research/sources/round108-ree/20261016T013538Z-source-investigation.md
    sha256: 43eb36e0535a23031a094cf130393d32f9f04f5ad543cfd619fcc3100fb211f9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:lanthanite-la
  path: data/records/lanthanite-la.yaml
  label: Lanthanite-(La)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-la.yaml
    role: maintained record
scope:
  description: Complete exact La owner, species identity, separate synthetic thermal/rehydration
    arm and history; initial observation before remediation.
  selection: Assigned named owner; native inspect preceded judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lanthanite-la
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate data/records/lanthanite-la.yaml data/records/lanthanite-ce.yaml
    --require-records
  status: passed
  required: true
  summary: Checked 2 record(s); 0 failed.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:lanthanite-la
  evidence_ids:
  - named
- check_id: batch
  name: Required final batch gate pending
  command: just check
  status: unavailable
  required: true
  summary: Coordinator batch is still running on frozen original inputs. No final
    terminal outcome claimed; this initial observation records the supported finding
    before correction.
  target_ids:
  - cmmmech:lanthanite-la
- check_id: corpus
  name: Required final corpus gate pending
  command: uv run --locked cmmmech validate --require-records
  status: unavailable
  required: true
  summary: Coordinator batch is still running on frozen original inputs. No final
    terminal outcome claimed; this initial observation records the supported finding
    before correction.
  target_ids:
  - cmmmech:lanthanite-la
- check_id: history
  name: Required final history gate pending
  command: uv run --locked cmmmech validate-history --base 26661b7f033d4bdb915e48e71080aa5774b4c3d6
  status: unavailable
  required: true
  summary: Coordinator batch is still running on frozen original inputs. No final
    terminal outcome claimed; this initial observation records the supported finding
    before correction.
  target_ids:
  - cmmmech:lanthanite-la
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lanthanite-la.yaml
  locator: Exact original owner after initial native inspect.
  summary: The context links the general40mL recipe directly to a2g portion of its
    resulting solid.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: ffba6de0e9dd8b228659c7b623c463711f3970b373865c9d049dbc0b80889aeb
- evidence_id: history
  kind: record_content
  reference: history/records/lanthanite-la/2026-10-16T013309Z-codex-a2893c.yaml
  locator: Complete canonical CREATE and inline event.
  summary: Correct current actor, target and session; no changes by reviewer.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: 17e12b77b042a50daff947a5758a1e3746b76c61f9adbd055937143588a46a9d
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/acs.cgd.4c01168
  locator: Published article Methods p946 general homogeneous-mixing protocol and
    separate p948 Lanthanite Dehydration and Rehydration Experiments; Figures10-13
    and SI TableSI-1 also inspected.
  summary: Page948 states ambient21C homogeneous-mixing synthesis followed by a2g
    solid aliquot, but does not specify the synthesis scale or number of batches used
    for that aliquot.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: partial
  snapshot_sha256: 0313cca68f53a4b2d6bfb965940c035dfff20e87f7c29dd5dd9c1afaf58c3d83
- evidence_id: si
  kind: primary_source
  reference: https://doi.org/10.1021/acs.cgd.4c01168.s001
  locator: Complete8page supplement; TableSI-1 and Figure12 in the main article.
  summary: Both phases remain at120.5h; the owner correctly limits return to89wt%lanthanite/11wt%tengerite.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: 10144ad4fc658a5863fac6c6aa4e889bf5cad5ebad17b09bc375ee193deed0c1
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitionsp1 and La speciesrowp121 independently viewed.
  summary: Renamed1987s.p. La species identity is correctly separated from unique
    approval IDs.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: natural
  kind: primary_source
  reference: https://doi.org/10.1180/minmag.1989.053.373.17
  locator: Complete original4pages, Table1 and Figure1.
  summary: Locality and composition caution is supported.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: 2df34dae07defdba86fc9d1f5f57a39beacd05d13aa3e126d9d127cfbab5101d
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round108-borates-research/review-ree-named-validation.json
  locator: Independent actual terminal named-validation receipt.
  summary: Checked2records;0failed. Structural validation does not resolve protocol
    attribution.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: supports
  snapshot_sha256: 34ebb5eeb4a7b9ac2a59e2b6e57bd2d24a43e29ef7a8b97616dc50b5ca2d665e
- evidence_id: baseline
  kind: validation
  reference: /private/tmp/cmm-round108-baseline.json
  locator: Actual coordinator baseline receipt; independently checked completed exit0
    and log digest.
  summary: Baseline context, not final-state proof.
  accessed_at: '2026-10-16T01:42:59.651764Z'
  support: context_only
  snapshot_sha256: 79bd16a41889a65c6686b6161e03287b92a832762760c2f9533121be9b39f0ae
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct mineral identity and natural/synthetic boundary
  outcome: supported
  summary: Current IMA identity, historical locality caution and synthetic-analogue
    boundary are supported.
  target_ids:
  - cmmmech:lanthanite-la
  evidence_ids:
  - record
  - ima
  - natural
- assessment_id: phase
  area: evidence
  topic: Observed phase outcomes and uncertainty
  outcome: supported
  summary: The7h dry-heating product and89/11wt% partial return at120.5h are supported;
    total equilibrium and recovery yields are not asserted.
  target_ids:
  - cmmmech:lanthanite-la
  evidence_ids:
  - record
  - primary
  - si
- assessment_id: protocol
  area: provenance
  topic: Separate experiment synthesis scale
  outcome: concern
  summary: The general solution recipe is transferred to the separate2g thermal aliquot
    without an explicit source linkage or scale qualification.
  target_ids:
  - cmmmech:lanthanite-la
  evidence_ids:
  - record
  - primary
- assessment_id: history
  area: provenance
  topic: Canonical CREATE history
  outcome: supported
  summary: Current actor/model/tool, target and actual history are correct.
  target_ids:
  - cmmmech:lanthanite-la
  evidence_ids:
  - history
findings:
- finding_id: F1
  issue_key: round108-lanthanite-la-thermal-synthesis-scale
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate thermal sample inherits an unreported synthesis scale
  description: The owner states the general40mL50mMLa plus40mL50mMcarbonate recipe
    and immediately calls the dry-heating aliquot a2g portion of the resulting solid.
    The separate Methods p948 arm specifies ambient homogeneous-mixing synthesis but
    does not report scale or batch count. The general recipe contains2mmolLa, corresponding
    to about0.60g idealLa2(CO3)3·8H2O if allLa entered that phase; this is a consistency
    calculation, not an observed yield. It reinforces why a direct single-batch relationship
    must not be asserted. Remove the transferred recipe from this separate arm or
    explicitly leave its scale unspecified. The2g heating mass and phase outcomes
    remain supported.
  target_ids:
  - cmmmech:lanthanite-la
  field_paths:
  - mechanisms[0].context
  evidence_ids:
  - record
  - primary
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-la.yaml
    role: maintained record
actions:
- action_id: A1
  description: Describe the separate dry-heating sample as synthesized by homogeneous
    mixing at21C and state that its synthesis scale or batch count is unspecified;
    preserve2g/0.2g/0.3g experimental masses and phase outcomes.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:lanthanite-la
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-la.yaml
    role: maintained record
  acceptance_checks:
  - Re-read Methods p946 and separate p948 arm; do not infer the2g sample came from
    one stated40+40mLbatch.
  - Append canonical EDIT history and distinct inline event, repeat named and affected
    final gates, then capture final bytes in a successor review resolving this exact
    occurrence.
limitations:
- Final just check, strict corpus validation and history validation are pending at
  this observation; passing baseline and named validation are not substitutes.
- Mass calculation is a consistency bound for ideal hydratedLa carbonate, not a reported
  synthesis yield or new chemical assay.
- No author contact, independent experimental replication or complete phase mass balance
  performed.
notes:
- Original bytes and initial native capture are preserved. Curator must wait for coordinator
  signal before editing frozen inputs.
```
