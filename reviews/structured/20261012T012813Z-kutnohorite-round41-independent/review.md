# Independent scientific identity review of Kutnohorite

- Review: 20261012T012813Z-kutnohorite-round41-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T01:21:11.305644Z
- Finished UTC: 2026-10-12T01:28:13.642731Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The mineral identity and bounded geological context are supported by the dated IMA authority and complete original Handbook entry. Variable specimen composition is retained; no microbial, criticality or recovery claim imported from deferred evidence. No corrective findings.

## Scope And Provenance

Whole newly created mineral identity record and canonical provenance.

Selection: New distinct mineral owner selected from the source handoff; no microbial requirement inferred.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 762508748eaa4f857179fa6f3450765bc62ebd6a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:kutnohorite | data/records/kutnohorite.yaml | maintained | Kutnohorite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:kutnohorite | Root executed both new minerals:2 checked,0 failed; raw log /private/tmp/cmm-round41-mineral-independent-named.log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042 |
| Cohort batch | passed | True | cmmmech:kutnohorite | Root executed to terminal0 and verified raw log hash. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 164.97s (0:02:44)<br>Checked 213 record(s); 0 failed.<br>Checked 248 history record(s); 0 error(s). |
| Cohort nonempty | passed | True | cmmmech:kutnohorite | Root executed to terminal0 and verified raw log hash. Checked 213 record(s); 0 failed. |
| Cohort history | passed | True | cmmmech:kutnohorite | Root executed to terminal0 and verified raw log hash. Checked 248 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Dated nomenclature, formula and species scope

identity: supported. Targets: cmmmech:kutnohorite.

Current IMA row specifies CaMn2+(CO3)2, G status and1903original-description field. Handbook identifies dolomite-group ordered Ca:Mn approximately1:1 with Mg/Fe2+ substitution and separate KutnaHora/Franklin analyses. Historical kutnahorite reference spelling is not a second accepted species.

### Geological occurrence and compositional boundaries

evidence: supported. Targets: cmmmech:kutnohorite.

Handbook lists manganiferous sediment associations and specimen localities. Variable natural analyses are not treated as invariant manganese content or bulk-ore identity.

### Exact state, actual history and completed gates

provenance: supported. Targets: cmmmech:kutnohorite.

Native inspection/current hashes, actual CREATE history and completed validation agree. No earlier immutable artifact changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/kutnohorite.yaml; Entire frozen record and linked CREATE history | supports | Independent exact-state assessment after native inspect; no target/history/dossier authorship by reviewer. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original September2026 PDF page1 definitions and page119 row | supports | Current IMA row specifies CaMn2+(CO3)2, G status and1903original-description field. Handbook identifies dolomite-group ordered Ca:Mn approximately1:1 with Mg/Fe2+ substitution and separate KutnaHora/Franklin analyses. Historical kutnahorite reference spelling is not a second accepted species. |
| handbook | https://www.handbookofmineralogy.org/pdfs/kutnohorite.pdf; Complete original one-page Handbook entry; Chemistry, CrystalData, Occurrence/Distribution and References | supports | Handbook lists manganiferous sediment associations and specimen localities. Variable natural analyses are not treated as invariant manganese content or bulk-ore identity. |
| history | history/records/kutnohorite/2026-10-12T012017Z-codex-31a32c.yaml; Complete canonical CREATE and distinct actual inline event | supports | Current actor/model/tool and target/path match actual curation; no earlier provenance invented. |
| checks | /private/tmp/cmm-round41-final-terminal.json; Completed final batch, explicit nonempty gate and trusted-base append-only history | supports | All required cohort checks passed and current record bytes still match inspection. |
| inspection | /private/tmp/cmm-round41-mineral-independent-evidence.json; Five original authority page images and recomputed PDF/image hashes | supports | Root personally inspected IMA definitions/rows and both complete Handbook originals. IMA PDF was reused, not freshly downloaded. Handbook author acquisition logs verified and live canonical URLs independently opened. |
| search | /private/tmp/cmm-round41-mineral-independent-web.json; First-result current nomenclature/notice queries and live authority URL opens | context_only | No affecting formal nomenclature update verified in returned primary authority results. Secondary historic-year discrepancies are not substituted for the explicitly dated IMA field. This is bounded, not exhaustive. |
| dedup | /private/tmp/cmm-round41-mineral-independent-dedup.txt; Current and original data/research/reviews/history, hidden/ignored/followed links | context_only | Root independently searched both corpora and read author125raw-root receipt with no missing/error paths. New owner is distinct from prior mineral mentions, ores, nodules, elements and oxalate products; raw-root sweep itself was not rerun by root. |

## Limits And Additional Notes

- IMA identity is explicitly tied to September2026; Handbook specimen chemistry is not universal grade or phase purity.
- No microbial mechanism, criticality designation or industrial deployment is asserted.
- No original mineral description or crystallographic signal reprocessed; authority synthesis is adequate for the stated identity scope.
- Missing original experimental graphics remain outside accepted claims and source issue134 stays open.
- Bounded searches do not prove absence of all further nomenclature or experimental evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T012813Z-kutnohorite-round41-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific identity review of Kutnohorite
started_at: '2026-10-12T01:21:11.305644Z'
finished_at: '2026-10-12T01:28:13.642731Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record, CREATE history and identity dossier authored by /root/round27_superalloy.
    Root assigned scope but authored none of these bytes; independently inspected
    original authority pages after native capture, rechecked evidence hashes and executed
    named/batch gates. Root authored separate birnessite extension reviewed by another
    agent.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The mineral identity and bounded geological context are supported by the
  dated IMA authority and complete original Handbook entry. Variable specimen composition
  is retained; no microbial, criticality or recovery claim imported from deferred
  evidence. No corrective findings.
source:
  git_revision: 762508748eaa4f857179fa6f3450765bc62ebd6a
  state: working_tree
  inputs:
  - path: data/records/kutnohorite.yaml
    sha256: 20562fc3fdb5fc1b2be7f521ae0701920de6a61f994b38dc596c9cc75372ddcd
    role: target
  - path: history/records/kutnohorite/2026-10-12T012017Z-codex-31a32c.yaml
    sha256: 750f0181fa2cc36208d76d5f976a696e643da18dc121bb7b187bf3cb58784ef6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:kutnohorite
  path: data/records/kutnohorite.yaml
  label: Kutnohorite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/kutnohorite.yaml
    role: scientific_record
scope:
  description: Whole newly created mineral identity record and canonical provenance.
  selection: New distinct mineral owner selected from the source handoff; no microbial
    requirement inferred.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:kutnohorite
  exclusions:
  - target: Unaccepted microbial experiments and quantitative resource estimates
    reason: Record asserts neither; missing experimental original graphics remain
      a research issue rather than accepted mechanism evidence.
checks:
- check_id: named
  name: Independent named-record validation
  command: uv run --locked cmmmech validate data/records/todorokite.yaml data/records/kutnohorite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed both new minerals:2 checked,0 failed; raw log /private/tmp/cmm-round41-mineral-independent-named.log
    SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
  target_ids:
  - cmmmech:kutnohorite
- check_id: batch
  name: Cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Root executed to terminal0 and verified raw log hash. uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 164.97s (0:02:44)

    Checked 213 record(s); 0 failed.

    Checked 248 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:kutnohorite
- check_id: nonempty
  name: Cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed to terminal0 and verified raw log hash. Checked 213 record(s);
    0 failed.
  target_ids:
  - cmmmech:kutnohorite
- check_id: history
  name: Cohort history
  command: uv run --locked cmmmech validate-history --base 762508748eaa4f857179fa6f3450765bc62ebd6a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed to terminal0 and verified raw log hash. Checked 248 history
    record(s); 0 error(s).
  target_ids:
  - cmmmech:kutnohorite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/kutnohorite.yaml
  locator: Entire frozen record and linked CREATE history
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: Independent exact-state assessment after native inspect; no target/history/dossier
    authorship by reviewer.
  snapshot_sha256: 20562fc3fdb5fc1b2be7f521ae0701920de6a61f994b38dc596c9cc75372ddcd
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original September2026 PDF page1 definitions and page119 row
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: Current IMA row specifies CaMn2+(CO3)2, G status and1903original-description
    field. Handbook identifies dolomite-group ordered Ca:Mn approximately1:1 with
    Mg/Fe2+ substitution and separate KutnaHora/Franklin analyses. Historical kutnahorite
    reference spelling is not a second accepted species.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/kutnohorite.pdf
  locator: Complete original one-page Handbook entry; Chemistry, CrystalData, Occurrence/Distribution
    and References
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: Handbook lists manganiferous sediment associations and specimen localities.
    Variable natural analyses are not treated as invariant manganese content or bulk-ore
    identity.
  snapshot_sha256: 9dafc338a7393b2ef315ffe09274bb4de2d1f61fb6501324cb83567805ae477f
- evidence_id: history
  kind: record_content
  reference: history/records/kutnohorite/2026-10-12T012017Z-codex-31a32c.yaml
  locator: Complete canonical CREATE and distinct actual inline event
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: Current actor/model/tool and target/path match actual curation; no earlier
    provenance invented.
  snapshot_sha256: 750f0181fa2cc36208d76d5f976a696e643da18dc121bb7b187bf3cb58784ef6
- evidence_id: checks
  kind: validation
  reference: /private/tmp/cmm-round41-final-terminal.json
  locator: Completed final batch, explicit nonempty gate and trusted-base append-only
    history
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: All required cohort checks passed and current record bytes still match
    inspection.
  snapshot_sha256: fac7a8a8b654e5ea256c2a1a4d9718b00e926b0fccb75268ec8d7312a5f036c2
- evidence_id: inspection
  kind: record_content
  reference: /private/tmp/cmm-round41-mineral-independent-evidence.json
  locator: Five original authority page images and recomputed PDF/image hashes
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: supports
  summary: Root personally inspected IMA definitions/rows and both complete Handbook
    originals. IMA PDF was reused, not freshly downloaded. Handbook author acquisition
    logs verified and live canonical URLs independently opened.
  snapshot_sha256: 93071a2209a989ad4651cd7df7f3a453e88728cb448cea162698f9cff4682e7a
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round41-mineral-independent-web.json
  locator: First-result current nomenclature/notice queries and live authority URL
    opens
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: context_only
  summary: No affecting formal nomenclature update verified in returned primary authority
    results. Secondary historic-year discrepancies are not substituted for the explicitly
    dated IMA field. This is bounded, not exhaustive.
  snapshot_sha256: 511ec51b8709e24df3143aaee922cee13f6b84e03d40dad4b0786f4a693e3809
  search_scope: 'Exact queries: site:cnmnc.units.it todorokite kutnohorite September2026;
    todorokite mineral redefinition correction IMA; kutnohorite mineral nomenclature
    correction kutnahorite IMA. First returned sets only; accepted claims use original
    dated IMA/Handbook authorities.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round41-mineral-independent-dedup.txt
  locator: Current and original data/research/reviews/history, hidden/ignored/followed
    links
  accessed_at: '2026-10-12T01:28:13.642731Z'
  support: context_only
  summary: Root independently searched both corpora and read author125raw-root receipt
    with no missing/error paths. New owner is distinct from prior mineral mentions,
    ores, nodules, elements and oxalate products; raw-root sweep itself was not rerun
    by root.
  snapshot_sha256: 39314ac763e9c5d169ffdc4e771a620adcdf7c818a38b8be04c068045ee5116a
  search_scope: Root independently searched current and original corpora with hidden/ignored
    and followed links; author125raw-root receipt read and scoped, not fully rerun
    by root. Root visually inspected all five authority pages and read both complete
    original Handbook entries. Live authority URLs opened successfully; first-set
    notice/nomenclature searches not exhaustive.
assessments:
- assessment_id: identity
  area: identity
  topic: Dated nomenclature, formula and species scope
  outcome: supported
  target_ids:
  - cmmmech:kutnohorite
  summary: Current IMA row specifies CaMn2+(CO3)2, G status and1903original-description
    field. Handbook identifies dolomite-group ordered Ca:Mn approximately1:1 with
    Mg/Fe2+ substitution and separate KutnaHora/Franklin analyses. Historical kutnahorite
    reference spelling is not a second accepted species.
  evidence_ids:
  - record
  - ima
  - handbook
  - dedup
  dimensions:
  - name: material
    value: Mineral species
    definition: Species identity distinct from element, commodity, mixed ore/resource
      or product.
    evidence_ids:
    - record
    - ima
  - name: criticality
    value: Not asserted
    definition: No constituent or generic critical-mineral designation inherited.
    evidence_ids:
    - record
  - name: organism_biomass
    value: Not asserted
    definition: No experimental mechanism or strain claim accepted from incomplete
      primary graphics.
    evidence_ids:
    - record
  - name: conditions_outcome
    value: Not applicable to identity record
    definition: Natural specimen and occurrence context do not establish a microbial
      transformation or recovery yield.
    evidence_ids:
    - record
    - handbook
  - name: scale
    value: Geological occurrence
    definition: Occurrence is not industrial deployment or resource grade.
    evidence_ids:
    - record
    - handbook
- assessment_id: context
  area: evidence
  topic: Geological occurrence and compositional boundaries
  outcome: supported
  target_ids:
  - cmmmech:kutnohorite
  summary: Handbook lists manganiferous sediment associations and specimen localities.
    Variable natural analyses are not treated as invariant manganese content or bulk-ore
    identity.
  evidence_ids:
  - record
  - handbook
- assessment_id: provenance
  area: provenance
  topic: Exact state, actual history and completed gates
  outcome: supported
  target_ids:
  - cmmmech:kutnohorite
  summary: Native inspection/current hashes, actual CREATE history and completed validation
    agree. No earlier immutable artifact changed.
  evidence_ids:
  - record
  - history
  - checks
  - inspection
findings: []
actions: []
limitations:
- IMA identity is explicitly tied to September2026; Handbook specimen chemistry is
  not universal grade or phase purity.
- No microbial mechanism, criticality designation or industrial deployment is asserted.
- No original mineral description or crystallographic signal reprocessed; authority
  synthesis is adequate for the stated identity scope.
- Missing original experimental graphics remain outside accepted claims and source
  issue134 stays open.
- Bounded searches do not prove absence of all further nomenclature or experimental
  evidence.
tags:
- round41
- independent
- mineral
- identity
```
