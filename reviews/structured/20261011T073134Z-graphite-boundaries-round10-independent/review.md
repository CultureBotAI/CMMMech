# Independent graphite commodity boundary review

- Review: 20261011T073134Z-graphite-boundaries-round10-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:26:36Z
- Finished UTC: 2026-10-11T07:31:34Z
- Reviewer: Codex /root/cmm10_nb_ta (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the supported natural-graphite commodity and defer distinct broad-graphite and battery-grade proposals pending their own identity/evidence decisions. Origin and product suitability overlap and do not define a disjoint partition. Historical source rows remain historical rather than being rewritten as current coverage. All four selected targets were assessed; no actionable boundary defect was found.

## Scope And Provenance

One maintained natural-graphite record and three exact historical authority-inventory candidate rows defining the graphite commodity boundary decision.

Selection: Full bounded cohort: natural record plus candidates[27] graphite, candidates[28] graphite-battery-grade and candidates[51] natural-graphite in research/sources/expansion-authorities/20261011T040103Z.json. Related handoffs checked for context; no sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:natural-graphite | data/records/natural-graphite.yaml | maintained | Natural graphite |
| proposal:graphite | research/sources/expansion-authorities/20261011T040103Z.json # candidates[27] (candidate_key == graphite) | snapshot_row | graphite inventory proposal |
| proposal:graphite-battery-grade | research/sources/expansion-authorities/20261011T040103Z.json # candidates[28] (candidate_key == graphite-battery-grade) | snapshot_row | graphite-battery-grade inventory proposal |
| proposal:natural-graphite | research/sources/expansion-authorities/20261011T040103Z.json # candidates[51] (candidate_key == natural-graphite) | snapshot_row | natural-graphite inventory proposal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named-record validation | passed | True | cmmmech:natural-graphite | Reviewer executed: terminal 0; 1 record; 0 failed. Log /private/tmp/cmm-round10-graphite-review-validate.log. |
| Trusted-base history validation | passed | True | cmmmech:natural-graphite | Reviewer executed: terminal 0; 72 history records; 0 errors. Log /private/tmp/cmm-round10-graphite-review-history.log. |
| Completed batch gate | passed | True | cmmmech:natural-graphite | Root executed session84281, terminal exit0, reviewer read /private/tmp/cmm-round10-batch-check.log: all lint checks passed; 307 tests passed,3 skipped in64.75s;61records and72histories validated. |
| Nonempty corpus validation | passed | True | cmmmech:natural-graphite | Root executed session20894, terminal exit0; reviewer read /private/tmp/cmm-round10-batch-validation.log:61records,0failed. |

## Scientific And Domain Assessments

### Retain the natural commodity boundary

identity: supported. Targets: cmmmech:natural-graphite, proposal:natural-graphite.

USGS commercial scope and BGS designation support a natural-origin commodity record. The historical natural-graphite proposal is consistent with this accepted scope but its old representation field remains a historical snapshot.

### Defer broad graphite rather than mark represented

scope: supported. Targets: proposal:graphite.

The broader graphite proposal cannot be exhausted by one natural-origin root: the EU act and USGS synthetic-substitution context explicitly distinguish synthetic material. A future broad record needs its own identity and relation decision.

### Defer product-qualified graphite

scope: supported. Targets: proposal:graphite-battery-grade.

EU strategic battery-grade graphite has a suitability axis distinct from natural origin and explicitly retains synthetic scope. Neither universal purity thresholds nor natural/synthetic equivalence can be inferred.

### Avoid process transfer across commodity and resource boundaries

evidence: supported. Targets: cmmmech:natural-graphite, proposal:graphite, proposal:graphite-battery-grade, proposal:natural-graphite.

The inspected 2007 experiment is sulfide beneficiation with a graphite-containing unwanted fraction. Partial-access spent-battery leads do not yet establish natural feed origin or an accepted microbial process.

### Preserve historical rows and maintained correction owners

ownership: supported. Targets: cmmmech:natural-graphite, proposal:graphite, proposal:graphite-battery-grade, proposal:natural-graphite.

The proposal selectors identify exact immutable source-snapshot rows, not current records. Current acceptance and follow-up belong to the round10 dossier and future maintained records, leaving the historical authority snapshot intact.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: cmmmech:natural-graphite, proposal:natural-graphite. Natural-origin commercial material has a directly supported commodity identity and dated assessment; retain the accepted record and historical proposal as separate representations of their own roles, not duplicate curated records.
- defer: proposal:graphite. A broad graphite root could include synthetic material and therefore is not fully represented by the natural-origin commodity. Define its own scope and relationships before acceptance.
- defer: proposal:graphite-battery-grade. Product suitability and origin are overlapping axes. Require a source-defined product scope and its own evidence; do not invent a universal threshold or treat these proposals as a complete disjoint split.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/natural-graphite.yaml; All 44 lines; linked CREATE history; frozen dossier and native material contract | supports | Read the entire commodity record and actual CREATE sidecar. It has no external identity CURIE, mechanism, measurements or industrial deployment claim. Exact scientific inputs were captured with inspect before assessment. |
| usgs | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf; Graphite (Natural), printed pp.92–93/PDF pp.96–97; commercial forms, developments and substitutes | supports | Independently read text and rendered page pixels. The commodity chapter distinguishes natural commercial forms and synthetic substitutes; natural origin alone does not certify an anode product specification. Raw PDF /private/tmp/cmm-round9-graphite-evidence/usgs-mcs2026.pdf; rendered pages usgs-mcs2026-p96.png and -p97.png. |
| uk | https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf; Cover disclaimer; Table 1 printed vii/PDF11; Table 11 printed44/PDF48 | supports | Independently read disclaimer and inspected both table images. Natural graphite is in the 2024 critical assessment list. The designation is a BGS/CMIC assessment explicitly not government policy, exactly as the record says. Raw PDF /private/tmp/cmm-round10-graphite-raw/uk2024-or24059.pdf and table renders uk-or24059-p11.png, uk-or24059-p48.png. |
| uk-version | https://nora.nerc.ac.uk/id/eprint/539735/; Current and superseded NORA item metadata; current PDF cover | supports | Freshly opened the current and old https://nora.nerc.ac.uk/id/eprint/538471/ pages and inspected retained HTML. OR/24/047 is marked superseded. The old note says OR/24/057 while its link resolves to the current OR/24/059 item; the record follows the actual current item and PDF. The 2024 edition remains explicit despite the current item being made live in July 2025. Internally reviewed, not externally peer-reviewed, is a report limitation. |
| eu | https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng; Original Regulation 2024/1252 Article3(3), AnnexI(k), AnnexII(v) | supports | Fresh official text confirms the strategic battery-grade entry, broader critical graphite entry and explicit synthetic-graphite strategic context. Origin and product suitability therefore cannot be collapsed into one identity. Retained original act /private/tmp/cmm-round9-graphite-evidence/eu2024-1252.html. |
| primary2007 | https://www.journalssystem.com/ppmp/pdf-79310-15375?filename=Bio-beneficiation-of-mult.pdf; Langwaldt and Kalapudas 2007, methods pp.292–294, Table 2, Figure 2/Table 6 p.297, conclusions p.298 | context_only | Read retained primary text and independently viewed methods/Table 2, Figure 2/Table 6 and conclusion pixels. Freeze-dried bacterial preparations were tested to concentrate sulfides from Talvivaara black shale; graphite was an unwanted co-floating component. Table 6 combines graphite and minerals, not isolated graphite. Figure 2 is nickel recovery. The conclusion reports no substantial grade/recovery improvement. These data do not prove natural-graphite purification. Raw /private/tmp/cmm-round9-graphite-evidence/landwaldt2007.pdf; filename spelling differs from PDF author spelling. |
| handoff | research/ingests/round10-graphite-20261011.json; Full JSON/Markdown source dossier, query/access receipts and all 30 raw-artifact hashes | supports | Independently recomputed all 30 retained/new raw artifact hashes with no mismatches. The dossier preserves 2023/2026 spent-battery graphite leads as unaccepted partial-access sources and distinguishes graphite additives from graphite recovery. Independent ACS opening returned 403; full methods were not reviewed by this reviewer. The 2026 issue date is future relative to this assessment and online-publication timing is unresolved. |
| search | Local graphite duplicate/boundary and official correction searches; Current working-tree data, history, research, reviews and .claude; cited round9/round10 graphite raw roots | supports | Ignored-inclusive searches found the new natural commodity record, its history, historical proposal rows and previous handoffs; no second maintained graphite record surfaced in the declared corpus. This is a bounded corpus finding, not a machine-wide or literature-wide absence claim. Correction searches did not surface an applicable notice; the UK replacement is explicitly retained. |
| inventory | research/sources/expansion-authorities/20261011T040103Z.json; candidates[27] graphite; candidates[28] graphite-battery-grade; candidates[51] natural-graphite | supports | Read the three exact historical candidate objects and their labels, commodity kinds, authority mappings, review-needed status and historical unrepresented state. They are discovery proposals rather than verified commodity identities; the current boundary decision is in the round10 dossier. |

## Limits And Additional Notes

- This is an identity-and-designation commodity record without an accepted microbial mechanism; it is not evidence that microbial graphite processing is impossible.
- The BGS/CMIC source is the named 2024 assessment, not government policy or a claim about every later list. The old landing-page OR/24/057 wording conflicts with the current item/PDF OR/24/059 identifier and is documented.
- No external commodity identifier is asserted; a carbon-atom or graphite-mineral identifier would not by itself establish commercial commodity equivalence.
- The 2007 sulfide-flotation study is contextual and cannot establish a natural-graphite product yield, purity or deployment. Its combined graphite/minerals measurement must not be interpreted as pure graphite.
- The 2023/2026 spent-battery graphite leads need full-text/supplement acquisition, product/feed-origin assessment and, for the 2026 item, online-publication timing. This reviewer did not verify their complete experimental methods.
- Ignored-inclusive local searches and correction queries are bounded to the named corpus/roots and returned provider windows; no comprehensive literature-exhaustion or machine-wide absence claim is made.
- This category review assesses current retain/defer decisions and exact source-row identities. It does not revalidate every designation in the historical multicountry inventory or assert that the source corpus is exhausted.
- Working-tree input hashes attest the inspected uncommitted bytes against the durable trusted main base, not their presence in that base.
- No blocker, major, minor or informational corrective findings were identified in the assessed scope; no curation correction or new history event was made by this reviewer.
- Reviewer independently ran the named-record and trusted-base history checks; the batch gates were executed by root and their terminal receipts were inspected.
- An initial inspect --help attempt without the task UV_CACHE_DIR failed to open the sandbox-restricted default cache; rerunning with the configured task cache succeeded. This was a tool setup failure, not a record validation failure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
repository: CultureBotAI/CMMMech
started_at: '2026-10-11T07:26:36Z'
finished_at: '2026-10-11T07:31:34Z'
reviewer:
  identity: Codex /root/cmm10_nb_ta
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Authored only niobium/tantalum in this batch. Did not author
    or edit natural-graphite, its source dossier, its history or the historical graphite
    inventory. Independently inspected frozen bytes, official authority text, raw
    evidence and original figure/table pixels.
completion: completed
verdict: pass_with_limitations
scientific_review: true
checks:
- check_id: named
  name: Named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/natural-graphite.yaml
  status: passed
  required: true
  summary: 'Reviewer executed: terminal 0; 1 record; 0 failed. Log /private/tmp/cmm-round10-graphite-review-validate.log.'
  target_ids:
  - cmmmech:natural-graphite
  exit_code: 0
  expected_exit_code: 0
- check_id: history
  name: Trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  status: passed
  required: true
  summary: 'Reviewer executed: terminal 0; 72 history records; 0 errors. Log /private/tmp/cmm-round10-graphite-review-history.log.'
  target_ids:
  - cmmmech:natural-graphite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Completed batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: 'Root executed session84281, terminal exit0, reviewer read /private/tmp/cmm-round10-batch-check.log:
    all lint checks passed; 307 tests passed,3 skipped in64.75s;61records and72histories
    validated.'
  target_ids:
  - cmmmech:natural-graphite
  exit_code: 0
  expected_exit_code: 0
- check_id: nonempty
  name: Nonempty corpus validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Root executed session20894, terminal exit0; reviewer read /private/tmp/cmm-round10-batch-validation.log:61records,0failed.
  target_ids:
  - cmmmech:natural-graphite
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/natural-graphite.yaml
  locator: All 44 lines; linked CREATE history; frozen dossier and native material
    contract
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Read the entire commodity record and actual CREATE sidecar. It has no external
    identity CURIE, mechanism, measurements or industrial deployment claim. Exact
    scientific inputs were captured with inspect before assessment.
  snapshot_sha256: e6d403add676fb3ae70b64fffcd698328165f4a98a0500442daa851f8c6828b8
- evidence_id: usgs
  kind: authority
  reference: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf
  locator: Graphite (Natural), printed pp.92–93/PDF pp.96–97; commercial forms, developments
    and substitutes
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Independently read text and rendered page pixels. The commodity chapter
    distinguishes natural commercial forms and synthetic substitutes; natural origin
    alone does not certify an anode product specification. Raw PDF /private/tmp/cmm-round9-graphite-evidence/usgs-mcs2026.pdf;
    rendered pages usgs-mcs2026-p96.png and -p97.png.
  snapshot_sha256: 595e6e66674236dea40125a03eb1ea6b347f331c0bcf3411a1e77eba53c0d391
- evidence_id: uk
  kind: authority
  reference: https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf
  locator: Cover disclaimer; Table 1 printed vii/PDF11; Table 11 printed44/PDF48
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Independently read disclaimer and inspected both table images. Natural
    graphite is in the 2024 critical assessment list. The designation is a BGS/CMIC
    assessment explicitly not government policy, exactly as the record says. Raw PDF
    /private/tmp/cmm-round10-graphite-raw/uk2024-or24059.pdf and table renders uk-or24059-p11.png,
    uk-or24059-p48.png.
  snapshot_sha256: e5708ffb1080c874cc57f0e20aad8f99aea746977971280434a1cfbb37f28c9e
- evidence_id: uk-version
  kind: authority
  reference: https://nora.nerc.ac.uk/id/eprint/539735/
  locator: Current and superseded NORA item metadata; current PDF cover
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Freshly opened the current and old https://nora.nerc.ac.uk/id/eprint/538471/
    pages and inspected retained HTML. OR/24/047 is marked superseded. The old note
    says OR/24/057 while its link resolves to the current OR/24/059 item; the record
    follows the actual current item and PDF. The 2024 edition remains explicit despite
    the current item being made live in July 2025. Internally reviewed, not externally
    peer-reviewed, is a report limitation.
- evidence_id: eu
  kind: authority
  reference: https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng
  locator: Original Regulation 2024/1252 Article3(3), AnnexI(k), AnnexII(v)
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Fresh official text confirms the strategic battery-grade entry, broader
    critical graphite entry and explicit synthetic-graphite strategic context. Origin
    and product suitability therefore cannot be collapsed into one identity. Retained
    original act /private/tmp/cmm-round9-graphite-evidence/eu2024-1252.html.
  snapshot_sha256: 4b09770aa8d3abb936cdd360993149c644d2f91cf890e24ceb1998beef4650c6
- evidence_id: primary2007
  kind: primary_source
  reference: https://www.journalssystem.com/ppmp/pdf-79310-15375?filename=Bio-beneficiation-of-mult.pdf
  locator: Langwaldt and Kalapudas 2007, methods pp.292–294, Table 2, Figure 2/Table
    6 p.297, conclusions p.298
  accessed_at: '2026-10-11T07:31:34Z'
  support: context_only
  summary: Read retained primary text and independently viewed methods/Table 2, Figure
    2/Table 6 and conclusion pixels. Freeze-dried bacterial preparations were tested
    to concentrate sulfides from Talvivaara black shale; graphite was an unwanted
    co-floating component. Table 6 combines graphite and minerals, not isolated graphite.
    Figure 2 is nickel recovery. The conclusion reports no substantial grade/recovery
    improvement. These data do not prove natural-graphite purification. Raw /private/tmp/cmm-round9-graphite-evidence/landwaldt2007.pdf;
    filename spelling differs from PDF author spelling.
  snapshot_sha256: 55a8c03cb5999c2d7e4c42bac13f8d9d8c7d007b829a86cd3989949e756d9769
- evidence_id: handoff
  kind: record_content
  reference: research/ingests/round10-graphite-20261011.json
  locator: Full JSON/Markdown source dossier, query/access receipts and all 30 raw-artifact
    hashes
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Independently recomputed all 30 retained/new raw artifact hashes with no
    mismatches. The dossier preserves 2023/2026 spent-battery graphite leads as unaccepted
    partial-access sources and distinguishes graphite additives from graphite recovery.
    Independent ACS opening returned 403; full methods were not reviewed by this reviewer.
    The 2026 issue date is future relative to this assessment and online-publication
    timing is unresolved.
- evidence_id: search
  kind: search
  reference: Local graphite duplicate/boundary and official correction searches
  locator: Current working-tree data, history, research, reviews and .claude; cited
    round9/round10 graphite raw roots
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Ignored-inclusive searches found the new natural commodity record, its
    history, historical proposal rows and previous handoffs; no second maintained
    graphite record surfaced in the declared corpus. This is a bounded corpus finding,
    not a machine-wide or literature-wide absence claim. Correction searches did not
    surface an applicable notice; the UK replacement is explicitly retained.
  search_scope: 'rg --no-ignore --hidden --follow, both graphite and natural.graphite|graphite.battery.grade|cmmmech:graphite,
    across data history research reviews .claude; find for relevant symlinks returned
    none. Bounded raw inventory: /private/tmp/cmm-round9-graphite-evidence and /private/tmp/cmm-round10-graphite-raw.
    Fresh web queries: "Graphite (Natural)" "2026" USGS; "UK 2024 Criticality Assessment"
    "OR/24/059" correction; "Bio-beneficiation of multimetal black shale ore" correction
    retraction. Returned result windows only, no exhaustive pagination. No structured
    gene/expression adapter applies to this commodity/category scope.'
- evidence_id: inventory
  kind: record_content
  reference: research/sources/expansion-authorities/20261011T040103Z.json
  locator: candidates[27] graphite; candidates[28] graphite-battery-grade; candidates[51]
    natural-graphite
  accessed_at: '2026-10-11T07:31:34Z'
  support: supports
  summary: Read the three exact historical candidate objects and their labels, commodity
    kinds, authority mappings, review-needed status and historical unrepresented state.
    They are discovery proposals rather than verified commodity identities; the current
    boundary decision is in the round10 dossier.
  snapshot_sha256: fb5cc04b2a937a82571511a712eeb646b577f2bae9ec3f0c2837852d00e69e69
findings: []
actions: []
limitations:
- This is an identity-and-designation commodity record without an accepted microbial
  mechanism; it is not evidence that microbial graphite processing is impossible.
- The BGS/CMIC source is the named 2024 assessment, not government policy or a claim
  about every later list. The old landing-page OR/24/057 wording conflicts with the
  current item/PDF OR/24/059 identifier and is documented.
- No external commodity identifier is asserted; a carbon-atom or graphite-mineral
  identifier would not by itself establish commercial commodity equivalence.
- The 2007 sulfide-flotation study is contextual and cannot establish a natural-graphite
  product yield, purity or deployment. Its combined graphite/minerals measurement
  must not be interpreted as pure graphite.
- The 2023/2026 spent-battery graphite leads need full-text/supplement acquisition,
  product/feed-origin assessment and, for the 2026 item, online-publication timing.
  This reviewer did not verify their complete experimental methods.
- Ignored-inclusive local searches and correction queries are bounded to the named
  corpus/roots and returned provider windows; no comprehensive literature-exhaustion
  or machine-wide absence claim is made.
- This category review assesses current retain/defer decisions and exact source-row
  identities. It does not revalidate every designation in the historical multicountry
  inventory or assert that the source corpus is exhausted.
notes:
- Working-tree input hashes attest the inspected uncommitted bytes against the durable
  trusted main base, not their presence in that base.
- No blocker, major, minor or informational corrective findings were identified in
  the assessed scope; no curation correction or new history event was made by this
  reviewer.
- Reviewer independently ran the named-record and trusted-base history checks; the
  batch gates were executed by root and their terminal receipts were inspected.
- An initial inspect --help attempt without the task UV_CACHE_DIR failed to open the
  sandbox-restricted default cache; rerunning with the configured task cache succeeded.
  This was a tool setup failure, not a record validation failure.
links:
- research/ingests/round10-graphite-20261011.md
- research/ingests/round10-graphite-20261011.json
- https://github.com/CultureBotAI/CMMMech/issues/42
tags:
- round10
- graphite
- independent-review
review_id: 20261011T073134Z-graphite-boundaries-round10-independent
kind: category
title: Independent graphite commodity boundary review
skill: .claude/skills/review-yaml-category/SKILL.md
summary: Retain the supported natural-graphite commodity and defer distinct broad-graphite
  and battery-grade proposals pending their own identity/evidence decisions. Origin
  and product suitability overlap and do not define a disjoint partition. Historical
  source rows remain historical rather than being rewritten as current coverage. All
  four selected targets were assessed; no actionable boundary defect was found.
source:
  git_revision: 6ea63a8c98e22fd3c6794b17c77f7909c3b851a2
  state: working_tree
  inputs:
  - path: data/records/natural-graphite.yaml
    sha256: e6d403add676fb3ae70b64fffcd698328165f4a98a0500442daa851f8c6828b8
    role: target
  - path: docs/records.md
    sha256: 212cdbb723eb1ad9eb76ea1b7dad066914659b1f85eb2cdb51ee67466cfcc8ee
    role: context
  - path: history/records/natural-graphite/2026-10-11T072058Z-codex-03825a.yaml
    sha256: 0d6f2eaabb39b645b20b30fa0c0c5d8c859b193caaa955d9895cc2e0471dbf3e
    role: context
  - path: research/ingests/round10-graphite-20261011.json
    sha256: 835e3a5e02486422fdd1e998ffa23ba66b3839b93fc263fc93e82b7f0c299289
    role: context
  - path: research/ingests/round10-graphite-20261011.md
    sha256: 7e79ef707802b781a384303f0180839f3add17645bdb2aa61d7d7ef29e874537
    role: context
  - path: research/sources/expansion-authorities/20261011T040103Z.json
    sha256: fb5cc04b2a937a82571511a712eeb646b577f2bae9ec3f0c2837852d00e69e69
    role: target
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:natural-graphite
  path: data/records/natural-graphite.yaml
  label: Natural graphite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/natural-graphite.yaml
    role: scientific record
- target_id: proposal:graphite
  path: research/sources/expansion-authorities/20261011T040103Z.json
  selector: candidates[27] (candidate_key == graphite)
  label: graphite inventory proposal
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round10-graphite-20261011.md
    role: current boundary decision; preserve historical snapshot
- target_id: proposal:graphite-battery-grade
  path: research/sources/expansion-authorities/20261011T040103Z.json
  selector: candidates[28] (candidate_key == graphite-battery-grade)
  label: graphite-battery-grade inventory proposal
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round10-graphite-20261011.md
    role: current boundary decision; preserve historical snapshot
- target_id: proposal:natural-graphite
  path: research/sources/expansion-authorities/20261011T040103Z.json
  selector: candidates[51] (candidate_key == natural-graphite)
  label: natural-graphite inventory proposal
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/ingests/round10-graphite-20261011.md
    role: current boundary decision; preserve historical snapshot
scope:
  description: One maintained natural-graphite record and three exact historical authority-inventory
    candidate rows defining the graphite commodity boundary decision.
  selection: 'Full bounded cohort: natural record plus candidates[27] graphite, candidates[28]
    graphite-battery-grade and candidates[51] natural-graphite in research/sources/expansion-authorities/20261011T040103Z.json.
    Related handoffs checked for context; no sampling.'
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - cmmmech:natural-graphite
  - proposal:graphite
  - proposal:graphite-battery-grade
  - proposal:natural-graphite
  exclusions:
  - target: Carbon element, graphite mineral species, individual spent-battery resource
      and particular anode product
    reason: Distinct possible identities; none is an accepted member of this commodity-origin/category
      decision.
assessments:
- assessment_id: natural
  area: identity
  topic: Retain the natural commodity boundary
  outcome: supported
  summary: USGS commercial scope and BGS designation support a natural-origin commodity
    record. The historical natural-graphite proposal is consistent with this accepted
    scope but its old representation field remains a historical snapshot.
  target_ids:
  - cmmmech:natural-graphite
  - proposal:natural-graphite
  evidence_ids:
  - record
  - usgs
  - uk
  - inventory
- assessment_id: broad
  area: scope
  topic: Defer broad graphite rather than mark represented
  outcome: supported
  summary: 'The broader graphite proposal cannot be exhausted by one natural-origin
    root: the EU act and USGS synthetic-substitution context explicitly distinguish
    synthetic material. A future broad record needs its own identity and relation
    decision.'
  target_ids:
  - proposal:graphite
  evidence_ids:
  - eu
  - usgs
  - handoff
  - inventory
- assessment_id: battery
  area: scope
  topic: Defer product-qualified graphite
  outcome: supported
  summary: EU strategic battery-grade graphite has a suitability axis distinct from
    natural origin and explicitly retains synthetic scope. Neither universal purity
    thresholds nor natural/synthetic equivalence can be inferred.
  target_ids:
  - proposal:graphite-battery-grade
  evidence_ids:
  - eu
  - usgs
  - handoff
  - inventory
- assessment_id: evidence
  area: evidence
  topic: Avoid process transfer across commodity and resource boundaries
  outcome: supported
  summary: The inspected 2007 experiment is sulfide beneficiation with a graphite-containing
    unwanted fraction. Partial-access spent-battery leads do not yet establish natural
    feed origin or an accepted microbial process.
  target_ids:
  - cmmmech:natural-graphite
  - proposal:graphite
  - proposal:graphite-battery-grade
  - proposal:natural-graphite
  evidence_ids:
  - primary2007
  - handoff
- assessment_id: ownership
  area: ownership
  topic: Preserve historical rows and maintained correction owners
  outcome: supported
  summary: The proposal selectors identify exact immutable source-snapshot rows, not
    current records. Current acceptance and follow-up belong to the round10 dossier
    and future maintained records, leaving the historical authority snapshot intact.
  target_ids:
  - cmmmech:natural-graphite
  - proposal:graphite
  - proposal:graphite-battery-grade
  - proposal:natural-graphite
  evidence_ids:
  - record
  - handoff
  - search
  - inventory
boundary_decisions:
- action: retain
  target_ids:
  - cmmmech:natural-graphite
  - proposal:natural-graphite
  rationale: Natural-origin commercial material has a directly supported commodity
    identity and dated assessment; retain the accepted record and historical proposal
    as separate representations of their own roles, not duplicate curated records.
  evidence_ids:
  - record
  - usgs
  - uk
- action: defer
  target_ids:
  - proposal:graphite
  rationale: A broad graphite root could include synthetic material and therefore
    is not fully represented by the natural-origin commodity. Define its own scope
    and relationships before acceptance.
  evidence_ids:
  - usgs
  - eu
  - handoff
- action: defer
  target_ids:
  - proposal:graphite-battery-grade
  rationale: Product suitability and origin are overlapping axes. Require a source-defined
    product scope and its own evidence; do not invent a universal threshold or treat
    these proposals as a complete disjoint split.
  evidence_ids:
  - eu
  - usgs
  - handoff
```
