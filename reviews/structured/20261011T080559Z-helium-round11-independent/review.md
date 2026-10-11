# Independent scientific review of round 11 helium

- Review: 20261011T080559Z-helium-round11-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T07:59:31Z
- Finished UTC: 2026-10-11T08:05:59Z
- Reviewer: Codex /root/cmm11_ir_os_hf (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Helium identity and the original EU 2024 designation are supported. The record correctly separates neutral element, isotopes, grades and gas resources, and withholds an unsupported microbial mechanism. Independently inspected DOE tracer recovery is a gas-communication test, not microbial helium extraction.

## Scope And Provenance

All scientific and provenance fields of the named frozen record; declared primary evidence and dated authorities.

Selection: Assigned named record; no sampling. Other candidate studies are context or future leads.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:helium | data/records/helium.yaml | maintained | Helium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named validation | passed | True | cmmmech:helium | Reviewer session 43433 terminal exit 0; Checked 3 records, 0 failed. Read /private/tmp/cmm11-independent-named-validation.log. |
| Full batch gate | passed | True | cmmmech:helium | Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records and 83 histories valid. Root session 92015 terminal exit 0. |
| Required-record validation | passed | True | cmmmech:helium | Final required-record validation passed 71 records, zero failed. Root session 93511 terminal exit 0. |
| Trusted-base history validation | passed | True | cmmmech:helium | Final trusted-base history validation passed 83 histories, zero errors. Root session 88115 terminal exit 0. |

## Scientific And Domain Assessments

### Neutral element and dated criticality

identity: supported. Targets: cmmmech:helium.

Correct element identity, jurisdiction, list and edition; ion/mineral/resource/grade distinctions preserved.

### Identity-only record and mechanism exclusion

evidence: supported. Targets: cmmmech:helium.

Helium identity and the original EU 2024 designation are supported. The record correctly separates neutral element, isotopes, grades and gas resources, and withholds an unsupported microbial mechanism. Independently inspected DOE tracer recovery is a gas-communication test, not microbial helium extraction.

### Actual curation and immutable observation

provenance: supported. Targets: cmmmech:helium.

Canonical CREATE sidecar and separate inline event match the target and actual actor/times; reviewed working changes remain uncommitted and are attested by byte hash. Scientific review does not append curation history.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/helium.yaml; Entire record, linked CREATE history, inline event, dossier and schema inspected; exact working-tree input hashes captured before judgment. | supports | Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records, dossiers or histories. Shared inspect captured final inputs before scientific assessment. Existing raw evidence was independently read, key primary images checked, authority content independently resolved or read from retained verified captures. No scientific target edits made by reviewer. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:30217; Neutral element name/formula/charge, hierarchy and alternate identifiers | supports | Verified 30217 denotes helium atom, formula He, charge 0. Helium live page succeeded; Rb/Re live web route failed, so independently read same-day curator-acquired official HTML rather than claiming a fresh successful reviewer download. Element root does not identify an assay ion or commodity stream. |
| criticality | https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng; Official title/date and exact annex or commodity row | supports | European Union; Regulation (EU) 2024/1252 original act 11 April 2024 published 3 May 2024; Annex II Section 1(p). Live authority content and retained source text agree. No timeless or universal material designation inferred. |
| primary | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf; Retained USGS Mineral Commodity Summaries 2026 PDF pages 100–101/printed 96–97, independently visually read both pages; DOE OSTI 7093 PDF p. 11/printed p. 7 visual scope check. | supports | USGS distinguishes grade-A/gaseous/crude helium, isotope-specific production and geological gas resources. DOE separates microbial contaminant activity from the helium pulse tracer communication test. These support conceptual boundaries, not biological helium recovery. Numerical industrial/tracer metrics are not imported into the record. |
| search | Bounded independent web and local search; Returned result sets and /private/tmp/cmm11-independent-{local,raw}-search.txt | context_only | Selected primary and authority leads examined within the stated bounded search; no comprehensive absence claim. |
| validation | /private/tmp/cmm-round11-final-batch-receipts.json; Final parent terminal receipts and full logs; reviewer named-validation log | supports | Reviewer independently read parent final checks/logs and own named validation terminal 0; structural checks do not prove scientific truth. |
| tracer | https://www.osti.gov/servlets/purl/7093; DOE 1995 performance, PDF p. 11/printed p. 7; independently visually read | context_only | Microbial activity describes contaminants; helium tracer injection/recovery describes injection-extraction well communication. The graph does not measure microbial helium extraction. |

## Limits And Additional Notes

- Original EU act designation only; no all-jurisdiction or latest-consolidated-edition claim.
- The literature scan is bounded and cannot establish universal absence of biological helium interactions.
- A fresh search found the Qaidam microbial-gas/helium-enrichment lead, PII S0264817224002095. Publisher open returned 403; only discovery metadata inspected, so geological association is deferred, not accepted as mechanism.
- No accepted journal mechanism claim requires a specific correction/retraction conclusion; tracer/context sources were checked within the stated locators.
- No unresolved blocker, major or minor record defect identified. No corrective action required for the inspected scope; listed limitations remain.
- No target content, history, dossier or schema changed by this reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T080559Z-helium-round11-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of round 11 helium
started_at: '2026-10-11T07:59:31Z'
finished_at: '2026-10-11T08:05:59Z'
reviewer:
  identity: Codex /root/cmm11_ir_os_hf
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records,
    dossiers or histories. Shared inspect captured final inputs before scientific
    assessment. Existing raw evidence was independently read, key primary images checked,
    authority content independently resolved or read from retained verified captures.
    No scientific target edits made by reviewer.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Helium identity and the original EU 2024 designation are supported. The record
  correctly separates neutral element, isotopes, grades and gas resources, and withholds
  an unsupported microbial mechanism. Independently inspected DOE tracer recovery
  is a gas-communication test, not microbial helium extraction.
source:
  git_revision: a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  state: working_tree
  inputs:
  - path: data/records/helium.yaml
    sha256: a2ff0d6c70298786262cd5ceb276ba5c873fe77cf60790a8ceb7be2504371f4c
    role: target
  - path: history/records/helium/2026-10-11T075135Z-codex-c80080.yaml
    sha256: f7dde6fac58f95661f56a3a1796de5037ca5abd645250ff98ffad0a6e080e000
    role: context
  - path: research/ingests/round11-helium-20261011.json
    sha256: 9e1a3e83b71c346c3b8b9217e3cd8a6664c9100c9d8ee64c89d57772696f4c01
    role: context
  - path: research/ingests/round11-helium-20261011.md
    sha256: 0dc18402b3abf6f5c87b57dc8f55234149f4c4e86a2a1253d0c4a24a0cad1295
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 861e6299240364ebddc53f7fb238b11014a5c2d48d2a211a80fcb18a5cc2170c
    role: context
targets:
- target_id: cmmmech:helium
  path: data/records/helium.yaml
  label: Helium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/helium.yaml
    role: maintained_record
scope:
  description: All scientific and provenance fields of the named frozen record; declared
    primary evidence and dated authorities.
  selection: Assigned named record; no sampling. Other candidate studies are context
    or future leads.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:helium
checks:
- check_id: named
  name: Reviewer named validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/rubidium.yaml data/records/rhenium.yaml data/records/helium.yaml
    --require-records
  status: passed
  required: true
  summary: Reviewer session 43433 terminal exit 0; Checked 3 records, 0 failed. Read
    /private/tmp/cmm11-independent-named-validation.log.
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - validation
- check_id: batch
  name: Full batch gate
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache just check
  status: passed
  required: true
  summary: Final just check passed 307 tests, three skipped in 61.95 seconds; 71 records
    and 83 histories valid. Root session 92015 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-check.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - validation
- check_id: nonempty
  name: Required-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate --require-records
  status: passed
  required: true
  summary: Final required-record validation passed 71 records, zero failed. Root session
    93511 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-validation.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - validation
- check_id: history
  name: Trusted-base history validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base a1d46ce5ca9958ff4cbd8a3b6aaf83bc8710ae0c
  status: passed
  required: true
  summary: Final trusted-base history validation passed 83 histories, zero errors.
    Root session 88115 terminal exit 0.
  scope_note: Parent executed; reviewer independently read full terminal receipt and
    /private/tmp/cmm-round11-final-history.log
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - validation
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/helium.yaml
  locator: Entire record, linked CREATE history, inline event, dossier and schema
    inspected; exact working-tree input hashes captured before judgment.
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Reviewer authored only Ir/Os/Hf, not these Rb/Re/He records, dossiers or
    histories. Shared inspect captured final inputs before scientific assessment.
    Existing raw evidence was independently read, key primary images checked, authority
    content independently resolved or read from retained verified captures. No scientific
    target edits made by reviewer.
  snapshot_sha256: a2ff0d6c70298786262cd5ceb276ba5c873fe77cf60790a8ceb7be2504371f4c
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30217
  locator: Neutral element name/formula/charge, hierarchy and alternate identifiers
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Verified 30217 denotes helium atom, formula He, charge 0. Helium live page
    succeeded; Rb/Re live web route failed, so independently read same-day curator-acquired
    official HTML rather than claiming a fresh successful reviewer download. Element
    root does not identify an assay ion or commodity stream.
- evidence_id: criticality
  kind: authority
  reference: https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng
  locator: Official title/date and exact annex or commodity row
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: European Union; Regulation (EU) 2024/1252 original act 11 April 2024 published
    3 May 2024; Annex II Section 1(p). Live authority content and retained source
    text agree. No timeless or universal material designation inferred.
- evidence_id: primary
  kind: primary_source
  reference: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf
  locator: Retained USGS Mineral Commodity Summaries 2026 PDF pages 100–101/printed
    96–97, independently visually read both pages; DOE OSTI 7093 PDF p. 11/printed
    p. 7 visual scope check.
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: USGS distinguishes grade-A/gaseous/crude helium, isotope-specific production
    and geological gas resources. DOE separates microbial contaminant activity from
    the helium pulse tracer communication test. These support conceptual boundaries,
    not biological helium recovery. Numerical industrial/tracer metrics are not imported
    into the record.
  snapshot_sha256: 595e6e66674236dea40125a03eb1ea6b347f331c0bcf3411a1e77eba53c0d391
- evidence_id: search
  kind: search
  reference: Bounded independent web and local search
  locator: Returned result sets and /private/tmp/cmm11-independent-{local,raw}-search.txt
  accessed_at: '2026-10-11T08:05:59Z'
  support: context_only
  summary: Selected primary and authority leads examined within the stated bounded
    search; no comprehensive absence claim.
  search_scope: 'Live web.run on 2026-10-11: exact DOI 10.1128/jb.150.3.1183-1191.1982
    and 10.3390/ma14164763 with correction retraction erratum; rubidium sphaeroides
    valinomycin uptake; rhenium Saccharomyces 4763 control; helium microbial extraction
    recovery tracer; exact ChEBI and taxonomy terms. Selected first returned results,
    no pagination/date filters. No matching correction notice identified in inspected
    returned titles; not an exhaustive registry audit. Hidden/ignored-inclusive rg
    --no-ignore --hidden --follow covered data/research/reviews/history/.claude and
    bounded cited roots /private/tmp/cmm-next-eu, /private/tmp/cmm-expansion-authorities-20261011,
    /private/tmp/cmm-round11-be-rb-re-raw and /private/tmp/cmm-round11-he-raw; all
    46 repository lines read and selected raw hits inspected. No symlinks in the inspected
    repository science/provenance trees or two new raw roots. No machine-wide absence
    claim.'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round11-final-batch-receipts.json
  locator: Final parent terminal receipts and full logs; reviewer named-validation
    log
  accessed_at: '2026-10-11T08:05:59Z'
  support: supports
  summary: Reviewer independently read parent final checks/logs and own named validation
    terminal 0; structural checks do not prove scientific truth.
- evidence_id: tracer
  kind: primary_source
  reference: https://www.osti.gov/servlets/purl/7093
  locator: DOE 1995 performance, PDF p. 11/printed p. 7; independently visually read
  accessed_at: '2026-10-11T08:05:59Z'
  support: context_only
  summary: Microbial activity describes contaminants; helium tracer injection/recovery
    describes injection-extraction well communication. The graph does not measure
    microbial helium extraction.
  snapshot_sha256: 1b27f242eaf12854c297a9d75e92f253644ebb374ed8f0630a1061b96aca09f9
assessments:
- assessment_id: identity-authority
  area: identity
  topic: Neutral element and dated criticality
  outcome: supported
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - record
  - identity
  - criticality
  summary: Correct element identity, jurisdiction, list and edition; ion/mineral/resource/grade
    distinctions preserved.
  dimensions:
  - name: criticality-edition
    value: European Union; Regulation (EU) 2024/1252 original act 11 April 2024 published
      3 May 2024; Annex II Section 1(p)
    definition: Edition-specific designation at original authority, not a perpetual
      property of every derived material.
    evidence_ids:
    - criticality
- assessment_id: scientific-scope
  area: evidence
  topic: Identity-only record and mechanism exclusion
  outcome: supported
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - record
  - primary
  - tracer
  summary: Helium identity and the original EU 2024 designation are supported. The
    record correctly separates neutral element, isotopes, grades and gas resources,
    and withholds an unsupported microbial mechanism. Independently inspected DOE
    tracer recovery is a gas-communication test, not microbial helium extraction.
  dimensions:
  - name: material-form
    value: Element helium, CHEBI:30217, He neutral atom
    definition: Isotopic children, commercial grades and helium-bearing gases are
      distinct entities.
    evidence_ids:
    - record
    - primary
  - name: mechanism-scope
    value: No accepted microbial mechanism; no organism/strain/biomass/substrate/assay
      outcome asserted
    definition: Identity-only scope is deliberate, not proof that all biological helium
      interactions are absent.
    evidence_ids:
    - record
    - primary
  - name: context-scale
    value: USGS commercial-resource context; DOE injected gas tracer test
    definition: Industrial gas statistics and co-located microbial contaminant removal
      do not establish industrial microbial helium recovery.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Actual curation and immutable observation
  outcome: supported
  target_ids:
  - cmmmech:helium
  evidence_ids:
  - record
  - validation
  summary: Canonical CREATE sidecar and separate inline event match the target and
    actual actor/times; reviewed working changes remain uncommitted and are attested
    by byte hash. Scientific review does not append curation history.
findings: []
actions: []
limitations:
- Original EU act designation only; no all-jurisdiction or latest-consolidated-edition
  claim.
- The literature scan is bounded and cannot establish universal absence of biological
  helium interactions.
- A fresh search found the Qaidam microbial-gas/helium-enrichment lead, PII S0264817224002095.
  Publisher open returned 403; only discovery metadata inspected, so geological association
  is deferred, not accepted as mechanism.
- No accepted journal mechanism claim requires a specific correction/retraction conclusion;
  tracer/context sources were checked within the stated locators.
notes:
- No unresolved blocker, major or minor record defect identified. No corrective action
  required for the inspected scope; listed limitations remain.
- No target content, history, dossier or schema changed by this reviewer.
tags:
- round11
- independent
- scientific-review
```
