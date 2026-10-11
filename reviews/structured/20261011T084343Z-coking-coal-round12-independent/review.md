# Independent review of Coking coal

- Review: 20261011T084343Z-coking-coal-round12-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T08:33:40Z
- Finished UTC: 2026-10-11T08:43:43Z
- Reviewer: Codex /root/cmm12_industrial_minerals (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The coke-making commodity identity and original EU critical designation are supported. The qualified PE culture-associated sulfur-content reduction is reproduced from primary tables, while acid chemistry, unmatched thymol controls, contradictory ash results and untested coke properties remain explicit.

## Scope And Provenance

All identity, criticality, mechanism/evidence and provenance fields in the selected frozen record.

Selection: Parent-assigned carbon/metal cohort; this observation covers exactly data/records/coking-coal.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e52585c9019a32d37f959e0dafa00ae431f28c4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:coking-coal | data/records/coking-coal.yaml | maintained | Coking coal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:coking-coal | Reviewer executed after inspecting the frozen files: terminal exit 0, Checked 5 record(s); 0 failed. This target is one of those five. |
| Trusted-base canonical history validation | passed | True | cmmmech:coking-coal | Reviewer executed: terminal exit 0, Checked 100 history record(s); 0 error(s). The linked target CREATE sidecar was separately read; corpus history validation does not imply scientific review of all other records. |
| Completed batch gate | passed | True | cmmmech:coking-coal | Root executed final batch session99845, terminal exit0. Reviewer read /private/tmp/cmm-round12-gate-receipts.json and /private/tmp/cmm-round12-check.log: all lint checks passed; 307 tests passed, 3 skipped in 70.99s; 93 records/0 failed and 108 histories/0 errors. Root receipt timestamps 08:41:42-08:43:00 UTC; this is the final changed-state gate, not the baseline. |
| Nonempty final corpus gate | passed | True | cmmmech:coking-coal | Root executed final nonempty validation, terminal exit0. Reviewer read /private/tmp/cmm-round12-require.log and receipt: 93 records, 0 failed, 08:43:00-08:43:03 UTC. |

## Scientific And Domain Assessments

### Commercial material boundary and exact dated criticality

identity: supported. Targets: cmmmech:coking-coal.

The EIA defines coking coal by coke-making suitability and gives metallurgical coal a broader definition including pulverized steelmaking coal. USGS Fact Sheet 2026-3061 v1.1 uses the terms interchangeably within its coke-making scope. The record faithfully retains the narrower identity and the terminology difference without transferring another designation.

### Actual curation actor, separate inline event and canonical history

provenance: supported. Targets: cmmmech:coking-coal.

Actual codex / GPT-6 / codex CREATE attribution and issue 48 linkage are consistent with the inspected sidecar and inline event. The prior sidecar timestamp and later inline timestamp are separate honest events. Trusted-base history validation passes.

### Qualified culture-associated PE sulfur-content reduction

evidence: supported. Targets: cmmmech:coking-coal.

The two PE residue sulfur concentrations and concentration-reduction percentages are reproducible from primary tables. The record accepts a culture-associated laboratory observation while explicitly preserving chemical contributions and inconsistent other results.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/coking-coal.yaml; Entire record; inline CREATE event and linked history/records/coking-coal/2026-10-11T083015Z-codex-d535fa.yaml | supports | Read all record bytes and linked CREATE history, with source hashes captured before assessment. The inline event and sidecar have actual codex / GPT-6 / codex actor attribution, distinct timestamps and the expected target and issue 48. No curator assertion is treated as independent scientific proof. |
| eu | https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng; Annex II, Section 1(i): coking coal | supports | Independently read retained original-act text and freshly opened official EUR-Lex text. Exact 11 April 2024 act / 3 May 2024 OJ wording matches the recorded classification and material scope. This is a dated designation, not an assertion of every subsequent revision. |
| handoff | research/ingests/round12-carbon-metals-20261011.json; Cohort dossier, access receipts and raw_artifacts/retained_inputs | supports | Read the cohort dossier and receipt metadata. Independently rehashed all 100 raw/retained entries; every expected SHA-256 matched. Receipt /private/tmp/cmm-round12-carbonmetal-review-hashes.json. Hash verification proves retained bytes, not scientific truth or independent download. Relevant source content was independently read below. |
| search | Reviewer local and live-web boundary/correction searches; Named corpus and cited raw roots; returned web result windows | supports | Ignored-inclusive local search surfaces the maintained element/natural-origin boundaries, proposal history and new commodity roots. Explicit related-record distinctions were inspected. The bounded correction searches and publisher page did not surface a matching correction or retraction notice; this is not a literature-wide absence claim. |
| definition | https://www.eia.gov/tools/glossary/index.php?id=Coking+coal; Coking coal and Metallurgical coal glossary entries | supports | The EIA defines coking coal by coke-making suitability and gives metallurgical coal a broader definition including pulverized steelmaking coal. USGS Fact Sheet 2026-3061 v1.1 uses the terms interchangeably within its coke-making scope. The record faithfully retains the narrower identity and the terminology difference without transferring another designation. Independently read both retained official definitions, and freshly opened the metallurgical definition at https://www.eia.gov/tools/glossary/index.php?id=Metallurgical+coal. The coking web open failed; retained coking HTML SHA-256 is attached. |
| coal-usgs | https://pubs.usgs.gov/fs/2026/3061/fs20263061.pdf; Fact Sheet 2026-3061 version 1.1 August 2026, pp. 1-2 introduction and specifications | supports | Read both pages and directly viewed page 1 pixels. This source uses metallurgical/coking coal in a coke-making scope and describes physical properties as well as impurities. Reduced sulfur alone cannot certify preserved coking performance. |
| coal-methods | https://doi.org/10.22044/jme.2023.13127.2387; Shahbazi et al. 2024 pp. 583-584, Sections 2.1-2.4 and Table 1; primary PDF pp. 3-4 | supports | Independently read source methods and viewed original page pixels. Selected PE and concentrated B4 feeds, reported acidophile mixture, culture preparation, flask conditions, thymol-containing uninoculated comparisons, acidified makeup, final HCl washing, and cited sulfur/ash assays match the record. The source has 9K/K9 and iron-amendment ambiguity; strain/member causality and exact speciation implementation are not established. Raw /private/tmp/cmm-round12-carbon-metals-raw/coal-shahbazi2024.pdf. |
| coal-results | https://doi.org/10.22044/jme.2023.13127.2387; Table 1 p.583; Tables 3-5 pp.589-590; Figure 4 p.590; Figure 5 p.592 and Sections 3.3-4 | supports | Independently read results/conclusions and viewed Table 1, Tables 3-5 and Figures 4-5 pixels. PE starts at 1.85% total sulfur; the 20-day, 20% inoculum, 5% pulp endpoint is 0.51%, versus 1.25% in the uninoculated comparison. (1.85-0.51)/1.85*100=72.4324 and (1.85-1.25)/1.85*100=32.4324 reproduce the cited percentages. These are residue concentration changes, not coal or sulfur mass balances. Figure 4 pH/ORP is compatible with acidophile activity, not causal pathway proof. |
| coal-limits | https://doi.org/10.22044/jme.2023.13127.2387; Sections 2.4, 3.3-3.4, Table 3 vs Figure 5, conclusion p.593 | partial | The abiotic comparator contains 3% thymol and has appreciable sulfur reduction. The final HCl wash is not separately isolated. Non-PE concentration/percentage discrepancies and reversed/conflicting ash assignments occur in tables/text/Figure 5, as the record states. Replicate n and error-bar definition are not specified in inspected text. Section 4 raises scale and product-quality questions without post-treatment coke-strength/plasticity tests. These limitations constrain inference but do not refute the narrower PE culture-associated comparison. |
| publisher | https://jme.shahroodut.ac.ir/article_2938.html; Current publisher landing page, title/DOI, issue 15(2), pp.581-595 and linked full PDF | supports | Freshly opened the primary publisher page, confirmed DOI, authors and issue metadata, and searched for a correction label with no match. The page lists PDF/XML but no separate experimental supplement link. No absolute claim about undiscovered notices or supplements is made. |
| batch-receipts | /private/tmp/cmm-round12-gate-receipts.json; All three commands and logs; /private/tmp/cmm-round12-gated-record-hashes.json | supports | Reviewer read final root gate receipts/logs. just check, nonempty validation and trusted-base 108-history check all exited0. Independently compared this target hash with the gated manifest and all inspected source inputs with their current bytes; unchanged. Root performed the batch; reviewer performed the earlier named/history checks. |

## Limits And Additional Notes

- Review covers only the five assigned records through separate per-record artifacts; other round12 curation is not independently reviewed here.
- Criticality is the named original 2024 EU act, not a claim about all later revisions or a broader element/mineral/product designation.
- Retained primary artifacts were independently inspected and rehashed; acquisition itself was performed by the curator. The raw files are outside Git and their availability is not guaranteed by the review bundle.
- Searches include ignored files in the declared local corpus but are bounded; web search returned provider windows, not an exhaustive literature or correction inventory.
- Acid chemistry, thymol and final HCl washing prevent isolated assignment of the sulfur change to microbes or a specific consortium member; no matched cell-free spent-culture or wash-only control was established.
- Residue concentration reduction is not whole-feed sulfur removal mass balance, coal yield or recovered sulfur product.
- Unspecified replication/error bars, ambiguous medium/iron description, inconsistent ash/non-PE tables and Figure 5 limit quantitative generalization; these are already explicit in the record.
- Coking suitability was described for the feed; post-treatment coke-making performance was not tested.
- Review began with inspect capture at 08:33:40 UTC; later contextual inspection expanded the input ledger without changing the target hash.
- Working-tree hashes attest inspected uncommitted bytes against durable trusted base 1e52585c9019a32d37f959e0dafa00ae431f28c4. They do not claim these bytes existed in that commit.
- No corrective findings were identified in the declared scope; no record/history edit or shared publication was performed by this reviewer.
- Named-record and initial trusted-base history checks were executed by this reviewer. Final batch and nonempty gates were executed by root and their terminal receipts/logs were independently read. The five target hashes match the root gated manifest; inspected inputs were rechecked unchanged before saving.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T084343Z-coking-coal-round12-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent review of Coking coal
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
summary: The coke-making commodity identity and original EU critical designation are
  supported. The qualified PE culture-associated sulfur-content reduction is reproduced
  from primary tables, while acid chemistry, unmatched thymol controls, contradictory
  ash results and untested coke properties remain explicit.
source:
  git_revision: 1e52585c9019a32d37f959e0dafa00ae431f28c4
  state: working_tree
  inputs:
  - path: data/records/coking-coal.yaml
    sha256: c6a10946b8617678052512de77c670f6648caa34b11186e056d92312ddccb2a2
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/coking-coal/2026-10-11T083015Z-codex-d535fa.yaml
    sha256: 6e916066c14e2c79cacdd533c55c255dc754be5e678641d39d5c92850df7f14d
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
- target_id: cmmmech:coking-coal
  path: data/records/coking-coal.yaml
  label: Coking coal
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/coking-coal.yaml
    role: maintained_record
scope:
  description: All identity, criticality, mechanism/evidence and provenance fields
    in the selected frozen record.
  selection: Parent-assigned carbon/metal cohort; this observation covers exactly
    data/records/coking-coal.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:coking-coal
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
  - cmmmech:coking-coal
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
  - cmmmech:coking-coal
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
  - cmmmech:coking-coal
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
  - cmmmech:coking-coal
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/coking-coal.yaml
  locator: Entire record; inline CREATE event and linked history/records/coking-coal/2026-10-11T083015Z-codex-d535fa.yaml
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read all record bytes and linked CREATE history, with source hashes captured
    before assessment. The inline event and sidecar have actual codex / GPT-6 / codex
    actor attribution, distinct timestamps and the expected target and issue 48. No
    curator assertion is treated as independent scientific proof.
  snapshot_sha256: c6a10946b8617678052512de77c670f6648caa34b11186e056d92312ddccb2a2
- evidence_id: eu
  kind: authority
  reference: https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng
  locator: 'Annex II, Section 1(i): coking coal'
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
  reference: https://www.eia.gov/tools/glossary/index.php?id=Coking+coal
  locator: Coking coal and Metallurgical coal glossary entries
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: The EIA defines coking coal by coke-making suitability and gives metallurgical
    coal a broader definition including pulverized steelmaking coal. USGS Fact Sheet
    2026-3061 v1.1 uses the terms interchangeably within its coke-making scope. The
    record faithfully retains the narrower identity and the terminology difference
    without transferring another designation. Independently read both retained official
    definitions, and freshly opened the metallurgical definition at https://www.eia.gov/tools/glossary/index.php?id=Metallurgical+coal.
    The coking web open failed; retained coking HTML SHA-256 is attached.
  snapshot_sha256: 4cb52b42c611daa177e84acaec2d9b55012d446d1d55a402304030493107292e
- evidence_id: coal-usgs
  kind: authority
  reference: https://pubs.usgs.gov/fs/2026/3061/fs20263061.pdf
  locator: Fact Sheet 2026-3061 version 1.1 August 2026, pp. 1-2 introduction and
    specifications
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Read both pages and directly viewed page 1 pixels. This source uses metallurgical/coking
    coal in a coke-making scope and describes physical properties as well as impurities.
    Reduced sulfur alone cannot certify preserved coking performance.
  snapshot_sha256: 033f9d3ff40d243893a762050584f80d03edf7565010549d1e5ec5b3d9e22f8b
- evidence_id: coal-methods
  kind: primary_source
  reference: https://doi.org/10.22044/jme.2023.13127.2387
  locator: Shahbazi et al. 2024 pp. 583-584, Sections 2.1-2.4 and Table 1; primary
    PDF pp. 3-4
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Independently read source methods and viewed original page pixels. Selected
    PE and concentrated B4 feeds, reported acidophile mixture, culture preparation,
    flask conditions, thymol-containing uninoculated comparisons, acidified makeup,
    final HCl washing, and cited sulfur/ash assays match the record. The source has
    9K/K9 and iron-amendment ambiguity; strain/member causality and exact speciation
    implementation are not established. Raw /private/tmp/cmm-round12-carbon-metals-raw/coal-shahbazi2024.pdf.
  snapshot_sha256: 1a7557e0cd453854b062c87651614b7ad20b0484ae3e65a9a59e57a48eed1af9
- evidence_id: coal-results
  kind: primary_source
  reference: https://doi.org/10.22044/jme.2023.13127.2387
  locator: Table 1 p.583; Tables 3-5 pp.589-590; Figure 4 p.590; Figure 5 p.592 and
    Sections 3.3-4
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Independently read results/conclusions and viewed Table 1, Tables 3-5 and
    Figures 4-5 pixels. PE starts at 1.85% total sulfur; the 20-day, 20% inoculum,
    5% pulp endpoint is 0.51%, versus 1.25% in the uninoculated comparison. (1.85-0.51)/1.85*100=72.4324
    and (1.85-1.25)/1.85*100=32.4324 reproduce the cited percentages. These are residue
    concentration changes, not coal or sulfur mass balances. Figure 4 pH/ORP is compatible
    with acidophile activity, not causal pathway proof.
  snapshot_sha256: 1a7557e0cd453854b062c87651614b7ad20b0484ae3e65a9a59e57a48eed1af9
- evidence_id: coal-limits
  kind: primary_source
  reference: https://doi.org/10.22044/jme.2023.13127.2387
  locator: Sections 2.4, 3.3-3.4, Table 3 vs Figure 5, conclusion p.593
  accessed_at: '2026-10-11T08:38:35Z'
  support: partial
  summary: The abiotic comparator contains 3% thymol and has appreciable sulfur reduction.
    The final HCl wash is not separately isolated. Non-PE concentration/percentage
    discrepancies and reversed/conflicting ash assignments occur in tables/text/Figure
    5, as the record states. Replicate n and error-bar definition are not specified
    in inspected text. Section 4 raises scale and product-quality questions without
    post-treatment coke-strength/plasticity tests. These limitations constrain inference
    but do not refute the narrower PE culture-associated comparison.
  snapshot_sha256: 1a7557e0cd453854b062c87651614b7ad20b0484ae3e65a9a59e57a48eed1af9
- evidence_id: publisher
  kind: primary_source
  reference: https://jme.shahroodut.ac.ir/article_2938.html
  locator: Current publisher landing page, title/DOI, issue 15(2), pp.581-595 and
    linked full PDF
  accessed_at: '2026-10-11T08:38:35Z'
  support: supports
  summary: Freshly opened the primary publisher page, confirmed DOI, authors and issue
    metadata, and searched for a correction label with no match. The page lists PDF/XML
    but no separate experimental supplement link. No absolute claim about undiscovered
    notices or supplements is made.
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
  summary: The EIA defines coking coal by coke-making suitability and gives metallurgical
    coal a broader definition including pulverized steelmaking coal. USGS Fact Sheet
    2026-3061 v1.1 uses the terms interchangeably within its coke-making scope. The
    record faithfully retains the narrower identity and the terminology difference
    without transferring another designation.
  target_ids:
  - cmmmech:coking-coal
  evidence_ids:
  - record
  - eu
  - definition
  - search
  - coal-usgs
  dimensions:
  - name: material_form
    value: Industrial commodity; Coking coal
    definition: The maintained commercial material concept, distinct from elemental/species/product-qualified
      identities
    evidence_ids:
    - record
    - definition
  - name: criticality
    value: 'European Union; Regulation 2024/1252 original act 11 April 2024, OJ 3
      May 2024; Annex II, Section 1(i): coking coal'
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
  - cmmmech:coking-coal
  evidence_ids:
  - record
  - handoff
- assessment_id: mechanism
  area: evidence
  topic: Qualified culture-associated PE sulfur-content reduction
  outcome: supported
  summary: The two PE residue sulfur concentrations and concentration-reduction percentages
    are reproducible from primary tables. The record accepts a culture-associated
    laboratory observation while explicitly preserving chemical contributions and
    inconsistent other results.
  target_ids:
  - cmmmech:coking-coal
  evidence_ids:
  - coal-methods
  - coal-results
  - coal-limits
  - publisher
  dimensions:
  - name: organism
    value: Source-reported Acidithiobacillus ferrooxidans, A. thiooxidans and Leptospirillum
      ferrooxidans mixed culture; reported 1:1:1
    definition: No strain identifier or individual-member causal attribution established
    evidence_ids:
    - coal-methods
  - name: biomass_state
    value: Prepared living acidophilic culture; grown 14 days without coal adaptation
    definition: Experimental culture state, not purified enzyme or immobilized/dried
      biomass
    evidence_ids:
    - coal-methods
  - name: substrate_pretreatment
    value: Eastern Parvadeh PE feed at reported +180/-350 micrometres; other B4 preparations
      include flotation/heavy-liquid concentration
    definition: The numerical claim is PE-specific and is not commodity-wide
    evidence_ids:
    - coal-methods
  - name: conditions
    value: 100 mL in 250 mL flasks, 34 C, 150 rpm, initial pH 1.7; selected endpoint
      20 days, 20% v/v inoculum, 5% w/v coal
    definition: Experimental conditions; evolving chemistry and medium-description
      ambiguity retained
    evidence_ids:
    - coal-methods
    - coal-results
  - name: controls
    value: Uninoculated acidic medium/coal with 3% w/w thymol; acidified makeup and
      final 10% v/v HCl residue wash
    definition: Unmatched comparator chemistry and unisolated wash contribution limit
      microbial causality
    evidence_ids:
    - coal-methods
    - coal-limits
  - name: outcome
    value: PE residual total sulfur 0.51% vs 1.25% uninoculated from 1.85% initial;
      72.43% vs 32.43% concentration reduction
    definition: Percentage denominator is initial sulfur concentration, not feed mass
      or isolated-product yield
    evidence_ids:
    - coal-results
  - name: deployment
    value: Laboratory impurity removal; post-treatment coke strength/plasticity and
      industrial implementation not demonstrated
    definition: Scale and product-performance limits
    evidence_ids:
    - coal-limits
    - coal-usgs
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
- Acid chemistry, thymol and final HCl washing prevent isolated assignment of the
  sulfur change to microbes or a specific consortium member; no matched cell-free
  spent-culture or wash-only control was established.
- Residue concentration reduction is not whole-feed sulfur removal mass balance, coal
  yield or recovered sulfur product.
- Unspecified replication/error bars, ambiguous medium/iron description, inconsistent
  ash/non-PE tables and Figure 5 limit quantitative generalization; these are already
  explicit in the record.
- Coking suitability was described for the feed; post-treatment coke-making performance
  was not tested.
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
