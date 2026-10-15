# Independent scientific review of titanogypsum

- Review: 20261015T013338Z-titanogypsum-round85-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T01:33:38.379546Z
- Finished UTC: 2026-10-15T01:33:38.748378Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance: source-defined industrial waste and yeast-associated fluoride redistribution are supported; source conflicts and limited causality remain explicit. No supported corrective record defect found.

## Scope And Provenance

Complete titanogypsum owner and linked CREATE session; all accepted claims assessed at their source-specific scope.

Selection: Named frozen record after author handoff and native inspect.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 51adf4be6c544642f6bf54a4e7f514adb84aa34e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:titanogypsum | data/records/titanogypsum.yaml | maintained | Titanogypsum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:titanogypsum | Actual independent command passed for the frozen record. |
| Actual batch gate 1 | passed | True | cmmmech:titanogypsum | Terminal outcome/log checked; actual interval 2026-10-15T01:22:50.828855+00:00 to 2026-10-15T01:31:26.415505+00:00 |
| Actual batch gate 2 | passed | True | cmmmech:titanogypsum | Terminal outcome/log checked; actual interval 2026-10-15T01:31:26.415715+00:00 to 2026-10-15T01:31:45.874908+00:00 |
| Actual batch gate 3 | passed | True | cmmmech:titanogypsum | Terminal outcome/log checked; actual interval 2026-10-15T01:31:45.874937+00:00 to 2026-10-15T01:31:56.553967+00:00 |
| Actual batch gate 4 | passed | True | cmmmech:titanogypsum | Terminal outcome/log checked; actual interval 2026-10-15T01:31:56.553994+00:00 to 2026-10-15T01:32:08.065969+00:00 |

## Scientific And Domain Assessments

### Secondary resource and organism identity

identity: supported. Targets: cmmmech:titanogypsum.

Titanium-dioxide production waste is not natural gypsum, pureCaSO4, phosphogypsum or elementalTi. The species identifier has correct rank; deposit16597 remains a source label. No jurisdictional criticality claim is inherited.

### Culture-associated partitioning with limited causal resolution

evidence: supported. Targets: cmmmech:titanogypsum.

Recipe, liveculture,150mL medium,5/10g feed,2mL inoculum,5days36C and controls match the original. Filtered fluoride falls inTG whilePdoesnotchange. Sorption remains proposed alongside changed dissolution/precipitation; source-specific analytical fractions are kept distinct.

### Source conflicts, product identity and null outcomes

evidence: supported. Targets: cmmmech:titanogypsum.

TG/PG figure labels, abstractloading discrepancy, unusualCa/S, mixed diffraction, nullP and supplementaryscope are explicit. XRFproportion,thermalmassloss andEPSsolutionF are not accepted as pureproductyield, adsorptioncapacity or a mass balance. Safety is not demonstrated.

### Exact state and validation

provenance: supported. Targets: cmmmech:titanogypsum.

Native inspect captured owner/history before final assessment. Separate creator/reviewer; no reviewer target edits. Independent named and actual batch checks passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/titanogypsum.yaml; Complete native-inspected maintained record; exact artifact /private/tmp/CMMMech-expansion-round85-20261015/data/records/titanogypsum.yaml | supports | Scope, qualifiers and source-specific conditions independently assessed. |
| history | history/records/titanogypsum/2026-10-15T012037Z-codex-1bad0c.yaml; Complete CREATE sidecar; exact artifact /private/tmp/CMMMech-expansion-round85-20261015/history/records/titanogypsum/2026-10-15T012037Z-codex-1bad0c.yaml | supports | Actual target, actor and change agree with distinct inline event. |
| chen | https://doi.org/10.3389/fbioe.2021.777957; Complete13-page original acquired; claim-bearing Materials and Methods, Results and Discussion independently read; Table1 and allFigures1-7 visually inspected; exact artifact /private/tmp/cmm-round85-resources-research/chen2021.pdf | supports | TG has lower filtered fluoride, unchanged phosphorus and distinct pH; separated polymer fraction contains fluoride. Mixed phases, incompatible abstract loading, repeated labels and compositional XRF endpoint do not establish recovery, phase purity or safety. |
| si | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8758580/supplementaryFiles; Original DataSheet1.docx complete text and both embedded figures inspected; S2 rendered to losslessPNG for viewing; exact artifact /private/tmp/cmm-round85-resources-research/chen2021-DataSheet1.docx | context_only | S1 labels deionized-water phosphorus; S2 is phosphogypsum only. Neither supplies a titanogypsum recovery mass balance. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5537&amp;retmode=xml; Current direct NCBITaxonomy XML TaxId,ScientificName,Rank; exact artifact /private/tmp/cmm-round85-resources-research/ncbi5537.xml | supports | 5537 identifies species Rhodotorula mucilaginosa; not experimental culture16597 authentication. |
| dedup | local maintained roots; Exact matched-path receipt; exact artifact /private/tmp/cmm-round85-titanogypsum-review-dedup.txt | context_only | Bounded hidden/ignored/followed search has current owner/dossier/history and prior context, not a duplicate material owner. |
| batch | /private/tmp/cmm-round85-final-gates.json; Actual terminal four-command batch receipt and bound log; exact artifact /private/tmp/cmm-round85-final-gates.json | supports | Required batch commands exited0 with stable owner input hashes. |
| named | uv run --locked cmmmech validate data/records/titanogypsum.yaml; Independent named validation run; exact artifact /private/tmp/cmm-round85-titanogypsum-named.log | supports | One record,zero failures. |

## Limits And Additional Notes

- No new experiment, diffraction refinement or independent culture authentication performed.
- No matched pH/killedcell/polymer-free control resolves microbial necessity or exclusive sorption; no whole-process mass balance or isolated fluorine product.
- Abstractloading, figure-label, repeated-comparison and unusual feed-composition issues remain source gaps.
- The source uses industrial waste in laboratory flasks; no soil/toxicity/field evidence establishes reuse safety or industrial operation.
- Independent2026-10-15 exactDOI correction/corrigendum/retraction and titanogypsum Rhodotorula fluoride webqueries returned originals and related literature without a resolving notice; first returnedsets, no datefilter/exhaustivepagination. Negative search is bounded.
- No target correction required. Source follow-up remains open; future supported claim changes require actualEDIT history and an independent successor scientific review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T013338Z-titanogypsum-round85-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of titanogypsum
started_at: '2026-10-15T01:33:38.379546Z'
finished_at: '2026-10-15T01:33:38.748378Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Frontier agent authored this record/history. Root independently
    inspected primary claim-bearing methods/results, Table1 and Figures1-7, supplementtext/graphics
    and taxonomy, then assessed the exact inspected maintained bytes without editing
    the owner. Downloads shared, assessment independent.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
source:
  git_revision: 51adf4be6c544642f6bf54a4e7f514adb84aa34e
  state: working_tree
  inputs:
  - path: data/records/titanogypsum.yaml
    sha256: da978617d7f84a63f2904ee3e78a682c3ff8d0644e85b64d86ff1da5ab409f72
    role: target
  - path: history/records/titanogypsum/2026-10-15T012037Z-codex-1bad0c.yaml
    sha256: 9fbfc9ce9651546c6b7fd58680ca1b4a66813235ef9b81cf13b99ca4412c4bec
    role: context
targets:
- target_id: cmmmech:titanogypsum
  path: data/records/titanogypsum.yaml
  label: Titanogypsum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/titanogypsum.yaml
    role: maintained_record
scope:
  description: Complete titanogypsum owner and linked CREATE session; all accepted
    claims assessed at their source-specific scope.
  selection: Named frozen record after author handoff and native inspect.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:titanogypsum
summary: 'Qualified acceptance: source-defined industrial waste and yeast-associated
  fluoride redistribution are supported; source conflicts and limited causality remain
  explicit. No supported corrective record defect found.'
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/titanogypsum.yaml
  locator: Complete native-inspected maintained record; exact artifact /private/tmp/CMMMech-expansion-round85-20261015/data/records/titanogypsum.yaml
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: Scope, qualifiers and source-specific conditions independently assessed.
  snapshot_sha256: da978617d7f84a63f2904ee3e78a682c3ff8d0644e85b64d86ff1da5ab409f72
- evidence_id: history
  kind: record_content
  reference: history/records/titanogypsum/2026-10-15T012037Z-codex-1bad0c.yaml
  locator: Complete CREATE sidecar; exact artifact /private/tmp/CMMMech-expansion-round85-20261015/history/records/titanogypsum/2026-10-15T012037Z-codex-1bad0c.yaml
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: Actual target, actor and change agree with distinct inline event.
  snapshot_sha256: 9fbfc9ce9651546c6b7fd58680ca1b4a66813235ef9b81cf13b99ca4412c4bec
- evidence_id: chen
  kind: primary_source
  reference: https://doi.org/10.3389/fbioe.2021.777957
  locator: Complete13-page original acquired; claim-bearing Materials and Methods,
    Results and Discussion independently read; Table1 and allFigures1-7 visually inspected;
    exact artifact /private/tmp/cmm-round85-resources-research/chen2021.pdf
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: TG has lower filtered fluoride, unchanged phosphorus and distinct pH; separated
    polymer fraction contains fluoride. Mixed phases, incompatible abstract loading,
    repeated labels and compositional XRF endpoint do not establish recovery, phase
    purity or safety.
  snapshot_sha256: 6d1dab33b635d2cf38ea6cf0565c93ea862cee355424c4fa22725f1f804f557f
- evidence_id: si
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8758580/supplementaryFiles
  locator: Original DataSheet1.docx complete text and both embedded figures inspected;
    S2 rendered to losslessPNG for viewing; exact artifact /private/tmp/cmm-round85-resources-research/chen2021-DataSheet1.docx
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: context_only
  summary: S1 labels deionized-water phosphorus; S2 is phosphogypsum only. Neither
    supplies a titanogypsum recovery mass balance.
  snapshot_sha256: 5a7e99a2cbad3f443b0b890a3712ba5574b3e63839bba4489240319d790d0ed7
- evidence_id: taxonomy
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5537&retmode=xml
  locator: Current direct NCBITaxonomy XML TaxId,ScientificName,Rank; exact artifact
    /private/tmp/cmm-round85-resources-research/ncbi5537.xml
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: 5537 identifies species Rhodotorula mucilaginosa; not experimental culture16597
    authentication.
  snapshot_sha256: b404b5c2420eab018827b5a49a261dfab1f71135525dc685bd9f3e97c40b67b9
- evidence_id: dedup
  kind: search
  reference: local maintained roots
  locator: Exact matched-path receipt; exact artifact /private/tmp/cmm-round85-titanogypsum-review-dedup.txt
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: context_only
  summary: Bounded hidden/ignored/followed search has current owner/dossier/history
    and prior context, not a duplicate material owner.
  snapshot_sha256: b53bad0043176621b99e077b01830e243b036ae68d5d82079eff37ff6fdff376
  search_scope: rg --no-ignore --hidden --follow -l -i titanogypsum|titanium.gypsum|10.3389/fbioe.2021.777957
    data research reviews history .claude
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round85-final-gates.json
  locator: Actual terminal four-command batch receipt and bound log; exact artifact
    /private/tmp/cmm-round85-final-gates.json
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: Required batch commands exited0 with stable owner input hashes.
  snapshot_sha256: 265694b8cec9b7c39325508f7811fea2ad2b656d6553c62449c545255123e748
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/titanogypsum.yaml
  locator: Independent named validation run; exact artifact /private/tmp/cmm-round85-titanogypsum-named.log
  accessed_at: '2026-10-15T01:33:38.748378Z'
  support: supports
  summary: One record,zero failures.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/titanogypsum.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual independent command passed for the frozen record.
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - named
- check_id: batch0
  name: Actual batch gate 1
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal outcome/log checked; actual interval 2026-10-15T01:22:50.828855+00:00
    to 2026-10-15T01:31:26.415505+00:00
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - batch
- check_id: batch1
  name: Actual batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal outcome/log checked; actual interval 2026-10-15T01:31:26.415715+00:00
    to 2026-10-15T01:31:45.874908+00:00
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - batch
- check_id: batch2
  name: Actual batch gate 3
  command: uv run --locked cmmmech validate-history --base 51adf4be6c544642f6bf54a4e7f514adb84aa34e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal outcome/log checked; actual interval 2026-10-15T01:31:45.874937+00:00
    to 2026-10-15T01:31:56.553967+00:00
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - batch
- check_id: batch3
  name: Actual batch gate 4
  command: uv run --locked python scripts/render_pages.py --check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Terminal outcome/log checked; actual interval 2026-10-15T01:31:56.553994+00:00
    to 2026-10-15T01:32:08.065969+00:00
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - batch
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary resource and organism identity
  outcome: supported
  summary: Titanium-dioxide production waste is not natural gypsum, pureCaSO4, phosphogypsum
    or elementalTi. The species identifier has correct rank; deposit16597 remains
    a source label. No jurisdictional criticality claim is inherited.
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - owner
  - chen
  - taxonomy
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated partitioning with limited causal resolution
  outcome: supported
  summary: Recipe, liveculture,150mL medium,5/10g feed,2mL inoculum,5days36C and controls
    match the original. Filtered fluoride falls inTG whilePdoesnotchange. Sorption
    remains proposed alongside changed dissolution/precipitation; source-specific
    analytical fractions are kept distinct.
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - owner
  - chen
  dimensions:
  - name: biomass_state
    value: Living culture upstream; ethanol-precipitated dialyzed extracellular fraction
      separately assayed
    definition: Assay context, not proof of an exclusive molecular binding pathway.
    evidence_ids:
    - chen
  - name: deployment_scope
    value: Laboratory flasks with industrial-origin waste
    definition: Feed provenance does not establish field or industrial deployment.
    evidence_ids:
    - chen
- assessment_id: limits
  area: evidence
  topic: Source conflicts, product identity and null outcomes
  outcome: supported
  summary: TG/PG figure labels, abstractloading discrepancy, unusualCa/S, mixed diffraction,
    nullP and supplementaryscope are explicit. XRFproportion,thermalmassloss andEPSsolutionF
    are not accepted as pureproductyield, adsorptioncapacity or a mass balance. Safety
    is not demonstrated.
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - owner
  - chen
  - si
- assessment_id: provenance
  area: provenance
  topic: Exact state and validation
  outcome: supported
  summary: Native inspect captured owner/history before final assessment. Separate
    creator/reviewer; no reviewer target edits. Independent named and actual batch
    checks passed.
  target_ids:
  - cmmmech:titanogypsum
  evidence_ids:
  - owner
  - history
  - dedup
  - named
  - batch
findings: []
actions: []
limitations:
- No new experiment, diffraction refinement or independent culture authentication
  performed.
- No matched pH/killedcell/polymer-free control resolves microbial necessity or exclusive
  sorption; no whole-process mass balance or isolated fluorine product.
- Abstractloading, figure-label, repeated-comparison and unusual feed-composition
  issues remain source gaps.
- The source uses industrial waste in laboratory flasks; no soil/toxicity/field evidence
  establishes reuse safety or industrial operation.
- Independent2026-10-15 exactDOI correction/corrigendum/retraction and titanogypsum
  Rhodotorula fluoride webqueries returned originals and related literature without
  a resolving notice; first returnedsets, no datefilter/exhaustivepagination. Negative
  search is bounded.
notes:
- No target correction required. Source follow-up remains open; future supported claim
  changes require actualEDIT history and an independent successor scientific review.
```
