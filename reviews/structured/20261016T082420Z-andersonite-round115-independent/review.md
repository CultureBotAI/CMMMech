# Independent scientific review of Andersonite

- Review: 20261016T082420Z-andersonite-round115-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T08:09:44.425548Z
- Finished UTC: 2026-10-16T08:24:20.934678Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded identity and abiotic laboratory observations are supported. No corrective curator defect was identified; unresolved source and reproducibility limits remain explicit.

## Scope And Provenance

Entire maintained owner and linked history; claim-level primary-source review, without experiment replication or structure re-refinement.

Selection: Two uranium-agent records independently assigned; separate native capture preceded assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97c978dcfb98269ea46fa6a9d02a6fb0253e111.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:andersonite | data/records/andersonite.yaml | maintained | Andersonite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Required final batch gate | passed | True | cmmmech:andersonite | Terminal receipt and log hash verified against current owner bytes. |
| Required final batch gate | passed | True | cmmmech:andersonite | Terminal receipt and log hash verified against current owner bytes. |
| Required final batch gate | passed | True | cmmmech:andersonite | Terminal receipt and log hash verified against current owner bytes. |
| Required final batch gate | passed | True | cmmmech:andersonite | Terminal receipt and log hash verified against current owner bytes. |

## Scientific And Domain Assessments

### Species, material form and authority

identity: supported. Targets: cmmmech:andersonite.

Current ideal formula and natural specimen identity are supported. The refined water occupancy and proposed (5+x) formulation are explicitly separate from the IMA formula and synthetic material.

### Primary experimental support and transfer limits

evidence: supported. Targets: cmmmech:andersonite.

The record accurately limits support to stepped laboratory loss of crystallinity and author-assigned later phases. Last relicts105C versus onset changes95C are not universal thresholds. Heating rate, collection dwell, minor quartz, irreversible cooling observation and missing replicates are preserved. No water-loss mass balance, uranium-valence measurement, microbial process or recovered-product yield is inferred.

### Actual history, bounded searches and final validation

provenance: supported. Targets: cmmmech:andersonite.

Actual CREATE history and exact inspected bytes are retained; structural checks do not establish experimental truth.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/andersonite.yaml; Entire native-inspected owner; retained /private/tmp/CMMMech-expansion-round115-20261016/data/records/andersonite.yaml | supports | Final maintained bytes, source locators, material form, outcome and limitations checked independently. |
| history0 | history/records/andersonite/2026-10-16T080655Z-codex-5ed076.yaml; Entire canonical CREATE session and separate inline event; retained /private/tmp/CMMMech-expansion-round115-20261016/history/records/andersonite/2026-10-16T080655Z-codex-5ed076.yaml | supports | Actual target, actor/model/tool and current timestamps agree; review itself is not a new curation event. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Species rows PDF10 and189 visually inspected, plus status definitions; retained /private/tmp/cmm-round115-uranium-research/ima202609.pdf | supports | Andersonite ideal6H2O is G1951; rutherfordine is A1962s.p., not grandfathered. These are mineral identities, not inherited uranium criticality. |
| primary | https://doi.org/10.3390/min8120586; Full main text, sections2.1-2.4 and3.1-4; original Figure4 PDF8 visually checked; retained /private/tmp/cmm-round115-uranium-research/andersonite2018-v2.pdf | supports | Natural Cane Springs specimen1272, 100K single-crystal refinement and stepped25-800C in-air powder experiment independently checked. Refined5.3 waters are distinct from ideal6, and dehydration is an interpretation rather than simultaneous TG measurement. Figure4 CuKalpha label conflicts with methods CoKalpha as the owner states. |
| notices | Independent exact DOI/title notice queries; Three live DOI/title correction/retraction queries on2026-10-16; retained /private/tmp/cmm-round115-uranium-independent-web.json | context_only | Returned results did not identify a verified applicable notice. Relevant primary originals, rather than secondary snippets or the inconsistent bibliographic page range in one index, establish source identity. |
| dedup | Current owner duplicate search; rg --no-ignore --hidden --follow over data/records; retained /private/tmp/cmm-round115-uranium-independent-dedup.txt | context_only | Only the two dedicated new owners match these names/DOIs in this bounded current-record search. Broader source/raw dedup is separately retained by the curator. |
| batch | Final exact-byte batch receipt; Terminal command rows and retained log hash; retained /private/tmp/cmm-round115-final-gates.json | supports | All four required commands passed against unchanged inputs; current reviewed owner hash matches the completed receipt. |

## Limits And Additional Notes

- Supplementary deposited coordinates were not acquired or re-refined.
- The Co/Cu radiation-label discrepancy remains unresolved; original diffraction data and thermal gas/gravimetric measurements were not reproduced.
- Independent agent assessment is not external human peer review. Full text and selected original page images were checked, not every page visually reread.
- Bounded searches cannot prove absence of later corrections or contradictory studies.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T082420Z-andersonite-round115-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Andersonite
started_at: '2026-10-16T08:09:44.425548Z'
finished_at: '2026-10-16T08:24:20.934678Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored this record/history. Root independently
    inspected exact final owner and primary full text, claim-bearing figure/method
    images, authority rows and notice results; root did not edit these owners.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded identity and abiotic laboratory observations are supported. No
  corrective curator defect was identified; unresolved source and reproducibility
  limits remain explicit.
source:
  git_revision: f97c978dcfb98269ea46fa6a9d02a6fb0253e111
  state: working_tree
  inputs:
  - path: data/records/andersonite.yaml
    sha256: 0e416b7232fac6ca28da0758415dbcec38e0914d739a7a3bf4ef1160e39fbc8f
    role: target
  - path: history/records/andersonite/2026-10-16T080655Z-codex-5ed076.yaml
    sha256: 673ff6f8dd7118ff23813479b0084bc4775366a563f0d4512c5cf26a560b9fb6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- kind: maintained
  label: Andersonite
  owner_paths:
  - path: data/records/andersonite.yaml
    repository: CultureBotAI/CMMMech
    role: scientific_record
  path: data/records/andersonite.yaml
  target_id: cmmmech:andersonite
scope:
  description: Entire maintained owner and linked history; claim-level primary-source
    review, without experiment replication or structure re-refinement.
  selection: Two uranium-agent records independently assigned; separate native capture
    preceded assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:andersonite
checks:
- check_id: gate0
  name: Required final batch gate
  required: true
  status: passed
  command: just check
  exit_code: 0
  summary: Terminal receipt and log hash verified against current owner bytes.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - batch
- check_id: gate1
  name: Required final batch gate
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  summary: Terminal receipt and log hash verified against current owner bytes.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - batch
- check_id: gate2
  name: Required final batch gate
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base f97c978dcfb98269ea46fa6a9d02a6fb0253e111
  exit_code: 0
  summary: Terminal receipt and log hash verified against current owner bytes.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - batch
- check_id: gate3
  name: Required final batch gate
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  summary: Terminal receipt and log hash verified against current owner bytes.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/andersonite.yaml
  locator: Entire native-inspected owner; retained /private/tmp/CMMMech-expansion-round115-20261016/data/records/andersonite.yaml
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: 0e416b7232fac6ca28da0758415dbcec38e0914d739a7a3bf4ef1160e39fbc8f
  support: supports
  summary: Final maintained bytes, source locators, material form, outcome and limitations
    checked independently.
- evidence_id: history0
  kind: record_content
  reference: history/records/andersonite/2026-10-16T080655Z-codex-5ed076.yaml
  locator: Entire canonical CREATE session and separate inline event; retained /private/tmp/CMMMech-expansion-round115-20261016/history/records/andersonite/2026-10-16T080655Z-codex-5ed076.yaml
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: 673ff6f8dd7118ff23813479b0084bc4775366a563f0d4512c5cf26a560b9fb6
  support: supports
  summary: Actual target, actor/model/tool and current timestamps agree; review itself
    is not a new curation event.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Species rows PDF10 and189 visually inspected, plus status definitions;
    retained /private/tmp/cmm-round115-uranium-research/ima202609.pdf
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Andersonite ideal6H2O is G1951; rutherfordine is A1962s.p., not grandfathered.
    These are mineral identities, not inherited uranium criticality.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min8120586
  locator: Full main text, sections2.1-2.4 and3.1-4; original Figure4 PDF8 visually
    checked; retained /private/tmp/cmm-round115-uranium-research/andersonite2018-v2.pdf
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: e4835bfb8ed332d38c792e236f1468ecd5df7ddf7270d6819b57c4b087997680
  support: supports
  summary: Natural Cane Springs specimen1272, 100K single-crystal refinement and stepped25-800C
    in-air powder experiment independently checked. Refined5.3 waters are distinct
    from ideal6, and dehydration is an interpretation rather than simultaneous TG
    measurement. Figure4 CuKalpha label conflicts with methods CoKalpha as the owner
    states.
- evidence_id: notices
  kind: search
  reference: Independent exact DOI/title notice queries
  locator: Three live DOI/title correction/retraction queries on2026-10-16; retained
    /private/tmp/cmm-round115-uranium-independent-web.json
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: 71d0259f89f9d5b2e1dd71efaf33286106929097282cc6cc07898e5c8bef8edd
  support: context_only
  summary: Returned results did not identify a verified applicable notice. Relevant
    primary originals, rather than secondary snippets or the inconsistent bibliographic
    page range in one index, establish source identity.
  search_scope: Initial returned results for exact DOI/title plus correction, erratum
    or retraction; no exhaustive pagination or global absence assertion.
- evidence_id: dedup
  kind: search
  reference: Current owner duplicate search
  locator: rg --no-ignore --hidden --follow over data/records; retained /private/tmp/cmm-round115-uranium-independent-dedup.txt
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: 4777d6f204f48bb680275261fad837e8aa2e65ed262f0459e0831e2178c92430
  support: context_only
  summary: Only the two dedicated new owners match these names/DOIs in this bounded
    current-record search. Broader source/raw dedup is separately retained by the
    curator.
  search_scope: Names and primary DOIs across current data/records including hidden/ignored
    files and followed symlinks; not a machine-wide search.
- evidence_id: batch
  kind: validation
  reference: Final exact-byte batch receipt
  locator: Terminal command rows and retained log hash; retained /private/tmp/cmm-round115-final-gates.json
  accessed_at: '2026-10-16T08:24:20.934678Z'
  snapshot_sha256: a4961d4886685d1dee2e32cefac92f59918148398b3cd4d909e7e214efb1d31f
  support: supports
  summary: All four required commands passed against unchanged inputs; current reviewed
    owner hash matches the completed receipt.
assessments:
- assessment_id: identity
  area: identity
  topic: Species, material form and authority
  outcome: supported
  summary: Current ideal formula and natural specimen identity are supported. The
    refined water occupancy and proposed (5+x) formulation are explicitly separate
    from the IMA formula and synthetic material.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - owner
  - ima
  - primary
- assessment_id: science
  area: evidence
  topic: Primary experimental support and transfer limits
  outcome: supported
  summary: The record accurately limits support to stepped laboratory loss of crystallinity
    and author-assigned later phases. Last relicts105C versus onset changes95C are
    not universal thresholds. Heating rate, collection dwell, minor quartz, irreversible
    cooling observation and missing replicates are preserved. No water-loss mass balance,
    uranium-valence measurement, microbial process or recovered-product yield is inferred.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - owner
  - primary
- assessment_id: provenance
  area: provenance
  topic: Actual history, bounded searches and final validation
  outcome: supported
  summary: Actual CREATE history and exact inspected bytes are retained; structural
    checks do not establish experimental truth.
  target_ids:
  - cmmmech:andersonite
  evidence_ids:
  - history0
  - notices
  - dedup
  - batch
findings: []
actions: []
limitations:
- Supplementary deposited coordinates were not acquired or re-refined.
- The Co/Cu radiation-label discrepancy remains unresolved; original diffraction data
  and thermal gas/gravimetric measurements were not reproduced.
- Independent agent assessment is not external human peer review. Full text and selected
  original page images were checked, not every page visually reread.
- Bounded searches cannot prove absence of later corrections or contradictory studies.
```
