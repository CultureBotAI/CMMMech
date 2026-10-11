# Independent review of Graphite commodity family

- Review: 20261011T084343Z-graphite-round12-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:33:40Z
- Finished UTC: 2026-10-11T08:43:43Z
- Reviewer: Codex /root/cmm12_industrial_minerals (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The natural-and-synthetic commodity family and original EU critical designation are supported. Explicit overlap with natural-graphite is preserved and battery-product suitability is not inferred from origin.

## Scope And Provenance

All identity, criticality, mechanism/evidence and provenance fields in the selected frozen record.

Selection: Parent-assigned carbon/metal cohort; this observation covers exactly data/records/graphite.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:graphite | data/records/graphite.yaml | maintained | Graphite commodity family |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:graphite | Reviewer executed after inspecting the frozen files: terminal exit 0, Checked 5 record(s); 0 failed. This target is one of those five. |
| Trusted-base canonical history validation | passed | True | cmmmech:graphite | Reviewer executed: terminal exit 0, Checked 100 history record(s); 0 error(s). The linked target CREATE sidecar was separately read; corpus history validation does not imply scientific review of all other records. |
| Completed batch gate | passed | True | cmmmech:graphite | Root executed final batch session99845, terminal exit0. Reviewer read /private/tmp/cmm-round12-gate-receipts.json and /private/tmp/cmm-round12-check.log: all lint checks passed; 307 tests passed, 3 skipped in 70.99s; 93 records/0 failed and 108 histories/0 errors. Root receipt timestamps 08:41:42-08:43:00 UTC; this is the final changed-state gate, not the baseline. |
| Nonempty final corpus gate | passed | True | cmmmech:graphite | Root executed final nonempty validation, terminal exit0. Reviewer read /private/tmp/cmm-round12-require.log and receipt: 93 records, 0 failed, 08:43:00-08:43:03 UTC. |

## Scientific And Domain Assessments

### Commercial material boundary and exact dated criticality

identity: supported. Targets: cmmmech:graphite.

The USGS yearbook jointly treats and separately accounts for natural and synthetic graphite. The broad record explicitly overlaps the maintained natural-graphite subset; it is not a duplicate synonym or a claimed disjoint partition. The original EU critical entry is unqualified; its strategic battery-grade entry is not generalized.

### Actual curation actor, separate inline event and canonical history

provenance: supported. Targets: cmmmech:graphite.

Actual codex / GPT-6 / codex CREATE attribution and issue 48 linkage are consistent with the inspected sidecar and inline event. The prior sidecar timestamp and later inline timestamp are separate honest events. Trusted-base history validation passes.

### Identity-only record and absent unsupported mechanism/identifier transfer

scope: supported. Targets: cmmmech:graphite.

No microbial mechanism, recovery yield, industrial deployment or external commodity identifier is asserted. Material distinctions and qualified evidence scope are maintained; no claim is made that microbial processing cannot exist.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/graphite.yaml; Entire record; inline CREATE event and linked history/records/graphite/2026-10-11T083013Z-codex-0dda78.yaml | supports | Read all record bytes and linked CREATE history, with source hashes captured before assessment. The inline event and sidecar have actual codex / GPT-6 / codex actor attribution, distinct timestamps and the expected target and issue 48. No curator assertion is treated as independent scientific proof. |
| eu | https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng; Article 3(3); Annex I, Section 1(k), graphite battery grade; Annex II, Section 1(v), unqualified graphite | supports | Independently read retained original-act text and freshly opened official EUR-Lex text. Exact 11 April 2024 act / 3 May 2024 OJ wording matches the recorded classification and material scope. This is a dated designation, not an assertion of every subsequent revision. |
| handoff | research/ingests/round12-carbon-metals-20261011.json; Cohort dossier, access receipts and raw_artifacts/retained_inputs | supports | Read the cohort dossier and receipt metadata. Independently rehashed all 100 raw/retained entries; every expected SHA-256 matched. Receipt /private/tmp/cmm-round12-carbonmetal-review-hashes.json. Hash verification proves retained bytes, not scientific truth or independent download. Relevant source content was independently read below. |
| search | Reviewer local and live-web boundary/correction searches; Named corpus and cited raw roots; returned web result windows | supports | Ignored-inclusive local search surfaces the maintained element/natural-origin boundaries, proposal history and new commodity roots. Explicit related-record distinctions were inspected. The bounded correction searches and publisher page did not surface a matching correction or retraction notice; this is not a literature-wide absence claim. |
| definition | https://pubs.usgs.gov/myb/vol1/2021/myb1-2021-graphite.pdf; 2021 Minerals Yearbook, advance release December 2024; printed pp. 32.1-32.2 / PDF pp. 2-3 | supports | Read both pages and directly viewed printed 32.1 pixels. The yearbook gives separate production/consumption streams and synthetic graphitization context. The USGS yearbook jointly treats and separately accounts for natural and synthetic graphite. The broad record explicitly overlaps the maintained natural-graphite subset; it is not a duplicate synonym or a claimed disjoint partition. The original EU critical entry is unqualified; its strategic battery-grade entry is not generalized. Raw PDF /private/tmp/cmm-round12-carbon-metals-raw/usgs-graphite2021.pdf. |
| boundary | data/records/natural-graphite.yaml; Entire existing natural-origin commodity description and evidence scope | supports | Read the existing natural-graphite record. Its natural-origin scope fits within the new broader natural-and-synthetic family; the new record expressly acknowledges overlap and does not collapse mineral species, natural material and battery qualification. Existing natural-graphite scientific review is not superseded. |
| batch-receipts | /private/tmp/cmm-round12-gate-receipts.json; All three commands and logs; /private/tmp/cmm-round12-gated-record-hashes.json | supports | Reviewer read final root gate receipts/logs. just check, nonempty validation and trusted-base 108-history check all exited0. Independently compared this target hash with the gated manifest and all inspected source inputs with their current bytes; unchanged. Root performed the batch; reviewer performed the earlier named/history checks. |

## Limits And Additional Notes

- Review covers only the five assigned records through separate per-record artifacts; other round12 curation is not independently reviewed here.
- Criticality is the named original 2024 EU act, not a claim about all later revisions or a broader element/mineral/product designation.
- Retained primary artifacts were independently inspected and rehashed; acquisition itself was performed by the curator. The raw files are outside Git and their availability is not guaranteed by the review bundle.
- Searches include ignored files in the declared local corpus but are bounded; web search returned provider windows, not an exhaustive literature or correction inventory.
- This is an evidence-backed identity/designation record without an accepted microbial mechanism or external commodity identifier. Review does not establish impossibility of microbial processing.
- The graphite family overlaps its natural-origin subset; the record explicitly acknowledges that relation. No disjoint partition or universal battery qualification is inferred.
- Review began with inspect capture at 08:33:40 UTC; later contextual inspection expanded the input ledger without changing the target hash.
- Working-tree hashes attest inspected uncommitted bytes against durable trusted base 1e52585c9019a32d37f959e0dafa00ae431f28c4. They do not claim these bytes existed in that commit.
- No corrective findings were identified in the declared scope; no record/history edit or shared publication was performed by this reviewer.
- Named-record and initial trusted-base history checks were executed by this reviewer. Final batch and nonempty gates were executed by root and their terminal receipts/logs were independently read. The five target hashes match the root gated manifest; inspected inputs were rechecked unchanged before saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T084343Z-graphite-round12-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent review of Graphite commodity family
started_at: '2026-10-11T08:33:40Z'
finished_at: '2026-10-11T08:43:43Z'
reviewer:
  identity: Codex /root/cmm12_industrial_minerals
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Curated the separate round12 industrial-mineral records. Did
    not author or edit these carbon/metal records, histories or source dossier. Independently
    inspected frozen bytes, official authorities, retained primary methods/results
    and figure/table pixels; performed own boundary/correction searches and named/history
    checks.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The natural-and-synthetic commodity family and original EU critical designation
  are supported. Explicit overlap with natural-graphite is preserved and battery-product
  suitability is not inferred from origin.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: data/records/graphite.yaml
    sha256: a31f18565b3b15c366d1587b88f1f70f047f865bf73591a3bd618a05d37f9a80
    role: target
  - path: data/records/natural-graphite.yaml
    sha256: e6d403add676fb3ae70b64fffcd698328165f4a98a0500442daa851f8c6828b8
    role: context
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/graphite/2026-10-11T083013Z-codex-0dda78.yaml
    sha256: 9aadb6e7f924231cc93a64eb79a2cad560e81a3c649692a59f23857c997f1bdc
    role: context
  - path: research/ingests/round12-carbon-metals-20261011.json
    sha256: 0f8feb02fb79de40cef04b1eafb0aa57adea51bdcc1df73340772172d36fdd2a
    role: context
  - path: research/ingests/round12-carbon-metals-20261011.md
    sha256: 3ea7d7d4e07d6bc4b52f24898733974fbba7881a2e0c4985bc75809b0bfa25e9
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:graphite
  path: data/records/graphite.yaml
  label: Graphite commodity family
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/graphite.yaml
    role: maintained_record
scope:
  description: All identity, criticality, mechanism/evidence and provenance fields
    in the selected frozen record.
  selection: Parent-assigned carbon/metal cohort; this observation covers exactly
    data/records/graphite.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:graphite
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/magnesium-metal.yaml data/records/silicon-metal.yaml
    data/records/titanium-metal.yaml data/records/coking-coal.yaml data/records/graphite.yaml
  status: passed
  required: true
  summary: 'Reviewer executed after inspecting the frozen files: terminal exit 0,
    Checked 5 record(s); 0 failed. This target is one of those five.'
  target_ids:
  - cmmmech:graphite
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base canonical history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 1e52585c9019a32d37f959e0dafa00ae431f28c4
  status: passed
  required: true
  summary: 'Reviewer executed: terminal exit 0, Checked 100 history record(s); 0 error(s).
    The linked target CREATE sidecar was separately read; corpus history validation
    does not imply scientific review of all other records.'
  target_ids:
  - cmmmech:graphite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed batch gate
  status: passed
  required: true
  summary: 'Root executed final batch session99845, terminal exit0. Reviewer read
    /private/tmp/cmm-round12-gate-receipts.json and /private/tmp/cmm-round12-check.log:
    all lint checks passed; 307 tests passed, 3 skipped in 70.99s; 93 records/0 failed
    and 108 histories/0 errors. Root receipt timestamps 08:41:42-08:43:00 UTC; this
    is the final changed-state gate, not the baseline.'
  target_ids:
  - cmmmech:graphite
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty final corpus gate
  status: passed
  required: true
  summary: 'Root executed final nonempty validation, terminal exit0. Reviewer read
    /private/tmp/cmm-round12-require.log and receipt: 93 records, 0 failed, 08:43:00-08:43:03
    UTC.'
  target_ids:
  - cmmmech:graphite
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/graphite.yaml
  locator: Entire record; inline CREATE event and linked history/records/graphite/2026-10-11T083013Z-codex-0dda78.yaml
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read all record bytes and linked CREATE history, with source hashes captured
    before assessment. The inline event and sidecar have actual codex / GPT-6 / codex
    actor attribution, distinct timestamps and the expected target and issue 48. No
    curator assertion is treated as independent scientific proof.
  snapshot_sha256: a31f18565b3b15c366d1587b88f1f70f047f865bf73591a3bd618a05d37f9a80
- evidence_id: eu
  kind: authority
  reference: https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng
  locator: Article 3(3); Annex I, Section 1(k), graphite battery grade; Annex II,
    Section 1(v), unqualified graphite
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Independently read retained original-act text and freshly opened official
    EUR-Lex text. Exact 11 April 2024 act / 3 May 2024 OJ wording matches the recorded
    classification and material scope. This is a dated designation, not an assertion
    of every subsequent revision.
  snapshot_sha256: e596f0ade92a8d267236304d072866f74fdb2c38955abb8da563c13c9f6d9213
- evidence_id: handoff
  kind: record_content
  reference: research/ingests/round12-carbon-metals-20261011.json
  locator: Cohort dossier, access receipts and raw_artifacts/retained_inputs
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read the cohort dossier and receipt metadata. Independently rehashed all
    100 raw/retained entries; every expected SHA-256 matched. Receipt /private/tmp/cmm-round12-carbonmetal-review-hashes.json.
    Hash verification proves retained bytes, not scientific truth or independent download.
    Relevant source content was independently read below.
- evidence_id: search
  kind: search
  reference: Reviewer local and live-web boundary/correction searches
  locator: Named corpus and cited raw roots; returned web result windows
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Ignored-inclusive local search surfaces the maintained element/natural-origin
    boundaries, proposal history and new commodity roots. Explicit related-record
    distinctions were inspected. The bounded correction searches and publisher page
    did not surface a matching correction or retraction notice; this is not a literature-wide
    absence claim.
  search_scope: 'Reviewer ran rg -l --no-ignore --hidden --follow -i with pattern
    magnesium[- ]metal|silicon[- ]metal|titanium[- ]metal|coking[- ]coal|cmmmech:graphite|name:
    Graphite commodity over data research reviews history and /private/tmp/cmm-round12-carbon-metals-raw
    and /private/tmp/cmm-round9-graphite-evidence. 59 matching paths retained in /private/tmp/cmm-round12-carbonmetal-review-dedup.txt;
    ignored files included. Independent bounded web queries: "10.22044/jme.2023.13127.2387"
    correction retraction; "Shahbazi" "Tabas" "Bioleaching" correction retraction;
    "Bioflotation and Bioleaching" "Tabas" controls sulfur; "2024/1252" "silicon metal"
    "titanium metal" graphite; "Tabas" "coal" "bacteria" sulfur "control". Returned
    provider windows only, without exhaustive pagination. Fresh official EUR-Lex,
    EIA metallurgical glossary and publisher landing page inspected; find Correction
    on the publisher landing page returned no match. The direct EIA coking-page web
    open initially returned Internal Error; retained official HTML was inspected.
    Adjacent coal studies surfaced but their abstracts/snippets were not promoted
    to primary contradictory or supportive evidence.'
- evidence_id: definition
  kind: authority
  reference: https://pubs.usgs.gov/myb/vol1/2021/myb1-2021-graphite.pdf
  locator: 2021 Minerals Yearbook, advance release December 2024; printed pp. 32.1-32.2
    / PDF pp. 2-3
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read both pages and directly viewed printed 32.1 pixels. The yearbook gives
    separate production/consumption streams and synthetic graphitization context.
    The USGS yearbook jointly treats and separately accounts for natural and synthetic
    graphite. The broad record explicitly overlaps the maintained natural-graphite
    subset; it is not a duplicate synonym or a claimed disjoint partition. The original
    EU critical entry is unqualified; its strategic battery-grade entry is not generalized.
    Raw PDF /private/tmp/cmm-round12-carbon-metals-raw/usgs-graphite2021.pdf.
  snapshot_sha256: 4f9f98fca68e8f58c4a297f6734d3ecead402fc3f4ea8337b89637bdeab098bc
- evidence_id: boundary
  kind: record_content
  reference: data/records/natural-graphite.yaml
  locator: Entire existing natural-origin commodity description and evidence scope
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read the existing natural-graphite record. Its natural-origin scope fits
    within the new broader natural-and-synthetic family; the new record expressly
    acknowledges overlap and does not collapse mineral species, natural material and
    battery qualification. Existing natural-graphite scientific review is not superseded.
- evidence_id: batch-receipts
  kind: validation
  reference: /private/tmp/cmm-round12-gate-receipts.json
  locator: All three commands and logs; /private/tmp/cmm-round12-gated-record-hashes.json
  accessed_at: '2026-10-11T08:43:43Z'
  support: supports
  summary: Reviewer read final root gate receipts/logs. just check, nonempty validation
    and trusted-base 108-history check all exited0. Independently compared this target
    hash with the gated manifest and all inspected source inputs with their current
    bytes; unchanged. Root performed the batch; reviewer performed the earlier named/history
    checks.
  snapshot_sha256: b9708428cb9e7e46ca5320cfdbcba8a12de6b2688d7eb1dc9fc3af9820f068a3
assessments:
- assessment_id: identity
  area: identity
  topic: Commercial material boundary and exact dated criticality
  outcome: supported
  summary: The USGS yearbook jointly treats and separately accounts for natural and
    synthetic graphite. The broad record explicitly overlaps the maintained natural-graphite
    subset; it is not a duplicate synonym or a claimed disjoint partition. The original
    EU critical entry is unqualified; its strategic battery-grade entry is not generalized.
  target_ids:
  - cmmmech:graphite
  evidence_ids:
  - record
  - eu
  - definition
  - search
  - boundary
  dimensions:
  - name: material_form
    value: Industrial commodity; Graphite commodity family
    definition: The maintained commercial material concept, distinct from elemental/species/product-qualified
      identities
    evidence_ids:
    - record
    - definition
  - name: criticality
    value: European Union; Regulation 2024/1252 original act 11 April 2024, OJ 3 May
      2024; Article 3(3); Annex I, Section 1(k), graphite battery grade; Annex II,
      Section 1(v), unqualified graphite
    definition: Exact authority, edition and list-entry scope; no later-currentness
      or adjacent-list transfer
    evidence_ids:
    - eu
- assessment_id: provenance
  area: provenance
  topic: Actual curation actor, separate inline event and canonical history
  outcome: supported
  summary: Actual codex / GPT-6 / codex CREATE attribution and issue 48 linkage are
    consistent with the inspected sidecar and inline event. The prior sidecar timestamp
    and later inline timestamp are separate honest events. Trusted-base history validation
    passes.
  target_ids:
  - cmmmech:graphite
  evidence_ids:
  - record
  - handoff
- assessment_id: scope
  area: scope
  topic: Identity-only record and absent unsupported mechanism/identifier transfer
  outcome: supported
  summary: No microbial mechanism, recovery yield, industrial deployment or external
    commodity identifier is asserted. Material distinctions and qualified evidence
    scope are maintained; no claim is made that microbial processing cannot exist.
  target_ids:
  - cmmmech:graphite
  evidence_ids:
  - record
  - definition
  - search
findings: []
actions: []
limitations:
- Review covers only the five assigned records through separate per-record artifacts;
  other round12 curation is not independently reviewed here.
- Criticality is the named original 2024 EU act, not a claim about all later revisions
  or a broader element/mineral/product designation.
- Retained primary artifacts were independently inspected and rehashed; acquisition
  itself was performed by the curator. The raw files are outside Git and their availability
  is not guaranteed by the review bundle.
- Searches include ignored files in the declared local corpus but are bounded; web
  search returned provider windows, not an exhaustive literature or correction inventory.
- This is an evidence-backed identity/designation record without an accepted microbial
  mechanism or external commodity identifier. Review does not establish impossibility
  of microbial processing.
- The graphite family overlaps its natural-origin subset; the record explicitly acknowledges
  that relation. No disjoint partition or universal battery qualification is inferred.
notes:
- Review began with inspect capture at 08:33:40 UTC; later contextual inspection expanded
  the input ledger without changing the target hash.
- Working-tree hashes attest inspected uncommitted bytes against durable trusted base
  1e52585c9019a32d37f959e0dafa00ae431f28c4. They do not claim these bytes existed
  in that commit.
- No corrective findings were identified in the declared scope; no record/history
  edit or shared publication was performed by this reviewer.
- Named-record and initial trusted-base history checks were executed by this reviewer.
  Final batch and nonempty gates were executed by root and their terminal receipts/logs
  were independently read. The five target hashes match the root gated manifest; inspected
  inputs were rechecked unchanged before saving.
links:
- research/ingests/round12-carbon-metals-20261011.md
- research/ingests/round12-carbon-metals-20261011.json
- https://github.com/CultureBotAI/CMMMech/issues/48
tags:
- round12
- independent-review
- carbon-metals
```
