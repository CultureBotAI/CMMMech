# Independent round98 scientific review of Ludlamite

- Review: 20261015T162645Z-ludlamite-round98-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T16:18:59Z
- Finished UTC: 2026-10-15T16:26:45.779576Z
- Reviewer: codex /root/round98_sulfates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact owner passes independent evidence, identity, source-boundary and provenance review. No supported curation defect was found; scientific limitations remain explicit.

## Scope And Provenance

Full asserted owner claims, source and history boundaries for this single new record.

Selection: Assigned independent review of frozen round98 owner against primary originals.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 56be9949049d47fc9e065b8c016e25bc247752e6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ludlamite | data/records/ludlamite.yaml | maintained | Ludlamite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:ludlamite | Both assigned owners validated; 2 records, 0 failed. |
| Completed batch gate 1 | passed | True | cmmmech:ludlamite | Root-run command inspected in actual final receipt; exact reviewed owner hash included and unchanged. |
| Completed batch gate 2 | passed | True | cmmmech:ludlamite | Root-run command inspected in actual final receipt; exact reviewed owner hash included and unchanged. |
| Completed batch gate 3 | passed | True | cmmmech:ludlamite | Root-run command inspected in actual final receipt; exact reviewed owner hash included and unchanged. |
| Completed batch gate 4 | passed | True | cmmmech:ludlamite | Root-run command inspected in actual final receipt; exact reviewed owner hash included and unchanged. |
| Independent primary-source scientific review | passed | True | cmmmech:ludlamite | Inspected complete acquired original, relevant methods/results, figures/tables, authority and available supplement; scope and limitations retained. |

## Scientific And Domain Assessments

### Species and material boundary

identity: supported. Targets: cmmmech:ludlamite.

The species is distinct from elemental constituents and nearby hydrate species; current official formula/status is exact.

### Experimental scope, controls and measured versus inferred results

evidence: supported. Targets: cmmmech:ludlamite.

The broad source auto-oxidation/reduction interpretation is kept separate from the measured ferric assay and altered diffraction. The owner does not claim an identified crystalline ferric mineral.

Natural mineral crystals; abiotic, no organism/strain/biomass. Open capillaries in air at 120, 180 and 240 C for five days, touching thermocouple, quench, HCl/dichromate assay. At 120/180 C superficial oxidation and original powder pattern; at 240 C ferric assay and diffuse unrelated lines. No masses, replicate count, conversion error or balance. Initial diffraction comparison is not a displayed matched control; other minerals are comparisons, and no oxygen-free ludlamite arm tests oxygen causality. The phosphoferrite hydrogen proposal and hypothetical oxidized ludlamite formula are not observed products. No recovery, product purity or industrial deployment.

### Primary provenance, source lineage and immutable CREATE history

provenance: supported. Targets: cmmmech:ludlamite.

Both inline and linked canonical CREATE histories describe this round accurately. Full originals are acquired outside Git and the owner and dossier have matching source boundaries.

### Counterevidence and limits

consistency: supported. Targets: cmmmech:ludlamite.

The owner preserves relevant negative results or source/model contradictions and does not transfer evidence from another mineral arm.

The broad source auto-oxidation/reduction interpretation is kept separate from the measured ferric assay and altered diffraction. The owner does not claim an identified crystalline ferric mineral.

### Exact-owner structural and batch gates

schema: supported. Targets: cmmmech:ludlamite.

Named validation and actual final batch receipt pass for these reviewed owner bytes. Structural tests do not establish scientific truth.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:ludlamite. Retain the distinct species identity and its qualified evidence boundary; do not merge with constituent elements or neighboring mineral species.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ludlamite.yaml; Entire owner, inline CREATE and canonical history; inspected exact working-tree bytes | supports | Record and history target, actor, timestamps, scope and source references match the new owner. No prior event is overwritten. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; PDF page 1 status definitions; page 129 Ludlamite row | supports | Current mineral identity and ideal formula are supported by the September 2026 list; no criticality or external CURIE is inferred. |
| dossier | research/sources/round98-phosphates/20261015T161805Z-source-investigation.json; Acquisition metadata, bounded deduplication, source access and contradiction accounting | supports | Original URLs, access times, hashes, exact model limitations and prior-study lineage are retained. |
| search | /private/tmp/cmm-round98-phosphates-independent-review/search-observation.json; Independent live correction queries and ignored-inclusive maintained corpus search | supports | No formal correction or retraction surfaced within the recorded first-result queries. Existing references and mineral arms are not mislabeled as independent replication. |
| named-validation | /private/tmp/cmm-round98-phosphates-independent-review/validation.log; Both assigned files; actual command exit 0 | supports | Checked 2 records; 0 failed. |
| batch-gates | /private/tmp/cmm-round98-final-gates.json; Actual root-run final batch receipt and hash-bound log | supports | Inspected completed receipt: all recorded commands exit 0, input hashes unchanged, and the reviewed owner hash equals the gate record input. |
| primary | https://www.rruff.net/doclib/am/vol56/AM56_1.pdf; Complete 17-page original; Table 1 p2, methods/results p14, Figure 7 p15, structural interpretation p16 | supports | Natural Palermo number 1 crystals, separate 120/180/240 C five-day air arms, cold-HCl/dichromate assay and reported diffraction outcomes support a qualified oxidation observation. The product identity and hydrogen pathway are not established. |

## Limits And Additional Notes

- Moore reports no ludlamite-specific sample masses, replicate counts, quantitative conversion uncertainty or mass balance. Product mineral identity remains unknown.
- The heating observations are one mineral arm of the same original study used for phosphoferrite, not an independent replication.
- This review examines primary full text and relevant figures/tables but does not reproduce the heating or assay. Earlier structural references were not reacquired and are not used as independent experimental support.
- Searches were bounded to recorded queries and local roots including ignored/hidden files; no source-exhaustion claim. Hosted PR, queue and postmerge gates are outside this scientific review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T162645Z-ludlamite-round98-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent round98 scientific review of Ludlamite
started_at: '2026-10-15T16:18:59Z'
finished_at: '2026-10-15T16:26:45.779576Z'
reviewer:
  identity: codex /root/round98_sulfates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent from /root/round98_phosphates, who authored
    these owners. I authored sulfate owners, not this target; I inspected primary
    sources and exact frozen bytes without changing this record.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact owner passes independent evidence, identity, source-boundary and provenance
  review. No supported curation defect was found; scientific limitations remain explicit.
source:
  git_revision: 56be9949049d47fc9e065b8c016e25bc247752e6
  state: working_tree
  inputs:
  - path: data/records/ludlamite.yaml
    sha256: 42c64afbc1a9abdfbe0292079391033175f61692a075e429932c08a9b684973c
    role: target
  - path: history/records/ludlamite/2026-10-15T161555Z-codex-42f1d7.yaml
    sha256: 24627a4d97e9195c66c339bb0306c89f6f96f57766de262c69ce39d5ee73024d
    role: context
  - path: research/sources/round98-phosphates/20261015T161805Z-source-investigation.json
    sha256: 0ba9097cfab5972044c72267b213bfdadec4646659feb8948b969ce5ffdf6df0
    role: context
  - path: research/sources/round98-phosphates/20261015T161805Z-source-investigation.md
    sha256: 17fe37ee545a1646b0f9f35d0108f025a2b1455bcbdb3270f7e3152b84f2cae6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full asserted owner claims, source and history boundaries for this
    single new record.
  selection: Assigned independent review of frozen round98 owner against primary originals.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ludlamite
targets:
- target_id: cmmmech:ludlamite
  path: data/records/ludlamite.yaml
  label: Ludlamite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ludlamite.yaml
    role: maintained scientific record
checks:
- check_id: named-validation
  name: Named record validation
  status: passed
  required: true
  summary: Both assigned owners validated; 2 records, 0 failed.
  target_ids:
  - cmmmech:ludlamite
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/ludlamite.yaml data/records/regerite.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named-validation
- check_id: batch-1
  name: Completed batch gate 1
  status: passed
  required: true
  summary: Root-run command inspected in actual final receipt; exact reviewed owner
    hash included and unchanged.
  target_ids:
  - cmmmech:ludlamite
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch-gates
  scope_note: Executed by root for the completed batch; independently inspected receipt
    and retained log hash.
- check_id: batch-2
  name: Completed batch gate 2
  status: passed
  required: true
  summary: Root-run command inspected in actual final receipt; exact reviewed owner
    hash included and unchanged.
  target_ids:
  - cmmmech:ludlamite
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch-gates
  scope_note: Executed by root for the completed batch; independently inspected receipt
    and retained log hash.
- check_id: batch-3
  name: Completed batch gate 3
  status: passed
  required: true
  summary: Root-run command inspected in actual final receipt; exact reviewed owner
    hash included and unchanged.
  target_ids:
  - cmmmech:ludlamite
  command: uv run --locked cmmmech validate-history --base 56be9949049d47fc9e065b8c016e25bc247752e6
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch-gates
  scope_note: Executed by root for the completed batch; independently inspected receipt
    and retained log hash.
- check_id: batch-4
  name: Completed batch gate 4
  status: passed
  required: true
  summary: Root-run command inspected in actual final receipt; exact reviewed owner
    hash included and unchanged.
  target_ids:
  - cmmmech:ludlamite
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch-gates
  scope_note: Executed by root for the completed batch; independently inspected receipt
    and retained log hash.
- check_id: primary-review
  name: Independent primary-source scientific review
  status: passed
  required: true
  summary: Inspected complete acquired original, relevant methods/results, figures/tables,
    authority and available supplement; scope and limitations retained.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - primary
  - ima
  - owner
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ludlamite.yaml
  locator: Entire owner, inline CREATE and canonical history; inspected exact working-tree
    bytes
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: Record and history target, actor, timestamps, scope and source references
    match the new owner. No prior event is overwritten.
  snapshot_sha256: 42c64afbc1a9abdfbe0292079391033175f61692a075e429932c08a9b684973c
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: PDF page 1 status definitions; page 129 Ludlamite row
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: Current mineral identity and ideal formula are supported by the September
    2026 list; no criticality or external CURIE is inferred.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round98-phosphates/20261015T161805Z-source-investigation.json
  locator: Acquisition metadata, bounded deduplication, source access and contradiction
    accounting
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: Original URLs, access times, hashes, exact model limitations and prior-study
    lineage are retained.
  snapshot_sha256: 0ba9097cfab5972044c72267b213bfdadec4646659feb8948b969ce5ffdf6df0
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round98-phosphates-independent-review/search-observation.json
  locator: Independent live correction queries and ignored-inclusive maintained corpus
    search
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: No formal correction or retraction surfaced within the recorded first-result
    queries. Existing references and mineral arms are not mislabeled as independent
    replication.
  snapshot_sha256: a05025bc92f6e74f23c56505ccfe0d67b491a4e372885b25b237c9aff525b1c6
  search_scope: web.run exact DOI correction/erratum/retraction and Moore 1971 ludlamite
    oxidation correction; official EJM primary landing page. rg --no-ignore --hidden
    --follow across data/records, research, reviews and history. Curator raw scan
    is bounded to named paths in dossier; no universal absence claim.
- evidence_id: named-validation
  kind: validation
  reference: /private/tmp/cmm-round98-phosphates-independent-review/validation.log
  locator: Both assigned files; actual command exit 0
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: Checked 2 records; 0 failed.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch-gates
  kind: validation
  reference: /private/tmp/cmm-round98-final-gates.json
  locator: Actual root-run final batch receipt and hash-bound log
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: 'Inspected completed receipt: all recorded commands exit 0, input hashes
    unchanged, and the reviewed owner hash equals the gate record input.'
  snapshot_sha256: d75dfd3bf78265dd50a250045bc62898f2680e05a2b44c19235c1674b7b2909d
- evidence_id: primary
  kind: primary_source
  reference: https://www.rruff.net/doclib/am/vol56/AM56_1.pdf
  locator: Complete 17-page original; Table 1 p2, methods/results p14, Figure 7 p15,
    structural interpretation p16
  accessed_at: '2026-10-15T16:26:45.753969Z'
  support: supports
  summary: Natural Palermo number 1 crystals, separate 120/180/240 C five-day air
    arms, cold-HCl/dichromate assay and reported diffraction outcomes support a qualified
    oxidation observation. The product identity and hydrogen pathway are not established.
  snapshot_sha256: aa2689ec16ad209dfeeea2209cf795b1a7af7713e000a34cd131412d313617db
assessments:
- assessment_id: identity
  area: identity
  topic: Species and material boundary
  outcome: supported
  summary: The species is distinct from elemental constituents and nearby hydrate
    species; current official formula/status is exact.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - ima
  - owner
  - primary
  dimensions:
  - name: material_form
    value: Natural mineral species, with ideal formula distinguished from measured
      specimen chemistry
    definition: Identity granularity; not an element, commodity or secondary resource
    evidence_ids:
    - ima
    - primary
  - name: criticality_scope
    value: No criticality status asserted
    definition: No authority, jurisdiction or list edition is inherited from constituents
    evidence_ids:
    - owner
- assessment_id: evidence-scope
  area: evidence
  topic: Experimental scope, controls and measured versus inferred results
  outcome: supported
  summary: The broad source auto-oxidation/reduction interpretation is kept separate
    from the measured ferric assay and altered diffraction. The owner does not claim
    an identified crystalline ferric mineral.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - primary
  - owner
  details: Natural mineral crystals; abiotic, no organism/strain/biomass. Open capillaries
    in air at 120, 180 and 240 C for five days, touching thermocouple, quench, HCl/dichromate
    assay. At 120/180 C superficial oxidation and original powder pattern; at 240
    C ferric assay and diffuse unrelated lines. No masses, replicate count, conversion
    error or balance. Initial diffraction comparison is not a displayed matched control;
    other minerals are comparisons, and no oxygen-free ludlamite arm tests oxygen
    causality. The phosphoferrite hydrogen proposal and hypothetical oxidized ludlamite
    formula are not observed products. No recovery, product purity or industrial deployment.
- assessment_id: provenance
  area: provenance
  topic: Primary provenance, source lineage and immutable CREATE history
  outcome: supported
  summary: Both inline and linked canonical CREATE histories describe this round accurately.
    Full originals are acquired outside Git and the owner and dossier have matching
    source boundaries.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - owner
  - dossier
  - primary
- assessment_id: contradictions
  area: consistency
  topic: Counterevidence and limits
  outcome: supported
  summary: The owner preserves relevant negative results or source/model contradictions
    and does not transfer evidence from another mineral arm.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - primary
  - owner
  details: The broad source auto-oxidation/reduction interpretation is kept separate
    from the measured ferric assay and altered diffraction. The owner does not claim
    an identified crystalline ferric mineral.
- assessment_id: validation
  area: schema
  topic: Exact-owner structural and batch gates
  outcome: supported
  summary: Named validation and actual final batch receipt pass for these reviewed
    owner bytes. Structural tests do not establish scientific truth.
  target_ids:
  - cmmmech:ludlamite
  evidence_ids:
  - named-validation
  - batch-gates
  - owner
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:ludlamite
  rationale: Retain the distinct species identity and its qualified evidence boundary;
    do not merge with constituent elements or neighboring mineral species.
  evidence_ids:
  - ima
  - primary
  - owner
limitations:
- Moore reports no ludlamite-specific sample masses, replicate counts, quantitative
  conversion uncertainty or mass balance. Product mineral identity remains unknown.
- The heating observations are one mineral arm of the same original study used for
  phosphoferrite, not an independent replication.
- This review examines primary full text and relevant figures/tables but does not
  reproduce the heating or assay. Earlier structural references were not reacquired
  and are not used as independent experimental support.
- Searches were bounded to recorded queries and local roots including ignored/hidden
  files; no source-exhaustion claim. Hosted PR, queue and postmerge gates are outside
  this scientific review.
```
