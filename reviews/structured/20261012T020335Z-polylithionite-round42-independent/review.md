# Independent scientific identity review of Polylithionite

- Review: 20261012T020335Z-polylithionite-round42-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T02:00:21.656853Z
- Finished UTC: 2026-10-12T02:03:35.861638Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Dated mineral identity and bounded geological context are supported. No microbial, criticality, universal-grade or recovery claim is imported from mixed-feed research. No corrective findings.

## Scope And Provenance

Whole new identity record and canonical provenance.

Selection: Distinct supported mineral owner from the source handoff.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a5528a4807ba14fd8088a557ad105ac10ca62965.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:polylithionite | data/records/polylithionite.yaml | maintained | Polylithionite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Completed named validation | passed | True | cmmmech:polylithionite | Root executed to terminal0; retained log /private/tmp/cmm-round42-mineral-independent-named.log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042. Checked 2 record(s); 0 failed. |
| Completed batch validation | passed | True | cmmmech:polylithionite | Root executed to terminal0; retained log /private/tmp/cmm-round42-final-batch.log SHA256 4980aedbe1b677797b96f68809ecd197fb335257db08dd5e42f8677eca30b98f. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 174.24s (0:02:54)<br>Checked 216 record(s); 0 failed.<br>Checked 252 history record(s); 0 error(s). |
| Completed nonempty validation | passed | True | cmmmech:polylithionite | Root executed to terminal0; retained log /private/tmp/cmm-round42-final-nonempty.log SHA256 253a7b1f24733e2960a5844348786b1f7b8c035bb10af8e25c914e2d5234e023. Checked 216 record(s); 0 failed. |
| Completed history validation | passed | True | cmmmech:polylithionite | Root executed to terminal0; retained log /private/tmp/cmm-round42-final-history.log SHA256 c2a1a9ebbab06d77f85879fede0494f78da78b43ff3500e7c095428e8f54ba35. Checked 252 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Dated nomenclature, formula and material scope

identity: supported. Targets: cmmmech:polylithionite.

September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p. Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2 and natural analyses remain separate from the dated ideal formula.

### Geological and series-name limits

evidence: supported. Targets: cmmmech:polylithionite.

Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic replacement. Original Rieder1998 page586 records IMA approval; page589/Table4 defines lepidolite as a series covering micas near the trilithionite-polylithionite join. An incompletely characterized mixed feed is not an endmember assay.

### Actual CREATE history and exact inspected state

provenance: supported. Targets: cmmmech:polylithionite.

Native captured hashes match frozen inputs; named and cohort gates passed. No previous provenance rewritten.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/polylithionite.yaml; Whole frozen record | supports | September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p. Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2 and natural analyses remain separate from the dated ideal formula. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 PDF page1 and page175 | supports | September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p. Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2 and natural analyses remain separate from the dated ideal formula. |
| handbook | https://www.handbookofmineralogy.org/pdfs/polylithionite.pdf; Complete one-page2001 version1.2 entry | supports | Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic replacement. Original Rieder1998 page586 records IMA approval; page589/Table4 defines lepidolite as a series covering micas near the trilithionite-polylithionite join. An incompletely characterized mixed feed is not an endmember assay. |
| history | history/records/polylithionite/2026-10-12T015837Z-codex-b6575d.yaml; Whole canonical CREATE sidecar and distinct inline event | supports | Actual actor/model/tool, target and scope match current curation; committed history unchanged. |
| checks | /private/tmp/cmm-round42-final-terminal.json; Completed batch/nonempty/trusted-base history | supports | All required checks completed successfully; validation is not scientific proof. |
| inspection | /private/tmp/cmm-round42-mineral-independent-evidence.json; Actual visual inspection and raw artifact hashes | supports | Root visually inspected seven original page images: IMA definitions and both rows, complete Handbook entries, and mica nomenclature pages586/589. Read relevant source text and fresh author acquisition receipts; independently opened both canonical Handbook URLs and ran bounded notice/nomenclature searches. IMA bytes were reused from a dated retained source, not freshly downloaded by root. Named validation passed; initial page-render command lacked pdftoppm and was replaced with isolated uv --no-project pymupdf, outside checkouts. |
| search | /private/tmp/cmm-round42-mineral-independent-web.json; Live primary URL opens and first returned notice/nomenclature results | context_only | No specific affecting nomenclature correction was verified in these returned sets. Bound to explicit dated authorities; no universal absence claim. |
| dedup | /private/tmp/cmm-round42-mineral-independent-dedup.txt; Current/original data, research, reviews and history | context_only | Root independently searched current/original scientific trees with hidden/ignored included and followed links; author ten referenced raw-root search read, not independently rerun. Missing referenced paths and unextracted binary text are explicit. No machine-wide or exhaustive notice-absence claim. |
| micas | https://doi.org/10.1346/CCMN.1998.0460513; Rieder et al1998, original pages586 and589/Table4 | supports | Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic replacement. Original Rieder1998 page586 records IMA approval; page589/Table4 defines lepidolite as a series covering micas near the trilithionite-polylithionite join. An incompletely characterized mixed feed is not an endmember assay. |

## Limits And Additional Notes

- IMA scope is explicitly September2026; older Handbook context does not assert current production.
- No microbial mechanism, criticality designation or industrial deployment is claimed.
- Original nineteenth-century descriptions and crystallographic measurements were not reprocessed; authority identity scope does not require that.
- Mixed-feed microbial leads remain separate research tasks.
- Search bounds and unavailable referenced paths are explicit; source exhaustion is not established.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T020335Z-polylithionite-round42-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific identity review of Polylithionite
started_at: '2026-10-12T02:00:21.656853Z'
finished_at: '2026-10-12T02:03:35.861638Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record, CREATE history and source dossier authored by /root/round27_superalloy.
    Root assigned scope but authored none of these bytes; independently captured native
    state, inspected original authority pages and conducted named and batch validation.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Dated mineral identity and bounded geological context are supported. No microbial,
  criticality, universal-grade or recovery claim is imported from mixed-feed research.
  No corrective findings.
source:
  git_revision: a5528a4807ba14fd8088a557ad105ac10ca62965
  state: working_tree
  inputs:
  - path: data/records/polylithionite.yaml
    sha256: e40dfba62223862df7097462628ab53542b29a8302ed945e67d866c331d0e3d8
    role: target
  - path: history/records/polylithionite/2026-10-12T015837Z-codex-b6575d.yaml
    sha256: 4812aa033ffcc53391626bd09eeeb27e9e3bd558538f8ca6a280912903a0182f
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:polylithionite
  path: data/records/polylithionite.yaml
  label: Polylithionite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/polylithionite.yaml
    role: scientific_record
scope:
  description: Whole new identity record and canonical provenance.
  selection: Distinct supported mineral owner from the source handoff.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:polylithionite
  exclusions:
  - target: Mixed-feed microbial assays and quantitative ore/resource claims
    reason: Not asserted in this identity record; require separate complete experimental/phase
      assessment.
checks:
- check_id: named
  name: Completed named validation
  command: uv run --locked cmmmech validate data/records/petalite.yaml data/records/polylithionite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed to terminal0; retained log /private/tmp/cmm-round42-mineral-independent-named.log
    SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042. Checked
    2 record(s); 0 failed.
  target_ids:
  - cmmmech:polylithionite
- check_id: batch
  name: Completed batch validation
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Root executed to terminal0; retained log /private/tmp/cmm-round42-final-batch.log
    SHA256 4980aedbe1b677797b96f68809ecd197fb335257db08dd5e42f8677eca30b98f. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 174.24s (0:02:54)

    Checked 216 record(s); 0 failed.

    Checked 252 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:polylithionite
- check_id: nonempty
  name: Completed nonempty validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed to terminal0; retained log /private/tmp/cmm-round42-final-nonempty.log
    SHA256 253a7b1f24733e2960a5844348786b1f7b8c035bb10af8e25c914e2d5234e023. Checked
    216 record(s); 0 failed.
  target_ids:
  - cmmmech:polylithionite
- check_id: history
  name: Completed history validation
  command: uv run --locked cmmmech validate-history --base a5528a4807ba14fd8088a557ad105ac10ca62965
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed to terminal0; retained log /private/tmp/cmm-round42-final-history.log
    SHA256 c2a1a9ebbab06d77f85879fede0494f78da78b43ff3500e7c095428e8f54ba35. Checked
    252 history record(s); 0 error(s).
  target_ids:
  - cmmmech:polylithionite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/polylithionite.yaml
  locator: Whole frozen record
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p.
    Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2
    and natural analyses remain separate from the dated ideal formula.
  snapshot_sha256: e40dfba62223862df7097462628ab53542b29a8302ed945e67d866c331d0e3d8
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September2026 PDF page1 and page175
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p.
    Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2
    and natural analyses remain separate from the dated ideal formula.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/polylithionite.pdf
  locator: Complete one-page2001 version1.2 entry
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic
    replacement. Original Rieder1998 page586 records IMA approval; page589/Table4
    defines lepidolite as a series covering micas near the trilithionite-polylithionite
    join. An incompletely characterized mixed feed is not an endmember assay.
  snapshot_sha256: 1855e03367a1f8c1e29c3444113ebe6c6c3e7f5bb55b8cab3586c00d9034e66f
- evidence_id: history
  kind: record_content
  reference: history/records/polylithionite/2026-10-12T015837Z-codex-b6575d.yaml
  locator: Whole canonical CREATE sidecar and distinct inline event
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: Actual actor/model/tool, target and scope match current curation; committed
    history unchanged.
  snapshot_sha256: 4812aa033ffcc53391626bd09eeeb27e9e3bd558538f8ca6a280912903a0182f
- evidence_id: checks
  kind: validation
  reference: /private/tmp/cmm-round42-final-terminal.json
  locator: Completed batch/nonempty/trusted-base history
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: All required checks completed successfully; validation is not scientific
    proof.
  snapshot_sha256: a25cbb01ec2e6d41c20607099611dd95f796cfe264c28c29a012e8f5b64f235f
- evidence_id: inspection
  kind: record_content
  reference: /private/tmp/cmm-round42-mineral-independent-evidence.json
  locator: Actual visual inspection and raw artifact hashes
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: 'Root visually inspected seven original page images: IMA definitions and
    both rows, complete Handbook entries, and mica nomenclature pages586/589. Read
    relevant source text and fresh author acquisition receipts; independently opened
    both canonical Handbook URLs and ran bounded notice/nomenclature searches. IMA
    bytes were reused from a dated retained source, not freshly downloaded by root.
    Named validation passed; initial page-render command lacked pdftoppm and was replaced
    with isolated uv --no-project pymupdf, outside checkouts.'
  snapshot_sha256: 1dfed8f64f608d004ab9379f89aa91c74c0e72a86fe961ad3e7d68270a26dc44
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round42-mineral-independent-web.json
  locator: Live primary URL opens and first returned notice/nomenclature results
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: context_only
  summary: No specific affecting nomenclature correction was verified in these returned
    sets. Bound to explicit dated authorities; no universal absence claim.
  snapshot_sha256: 518053e362ce0b693b34db3d488fe5987a37bde9e46feca5b97b2e0496c90fb1
  search_scope: 'Queries: site:cnmnc.units.it petalite polylithionite redefinition;
    "10.1346/CCMN.1998.0460513" correction erratum; petalite polylithionite mineral
    nomenclature correction IMA lepidolite. No date filters; first returned sets only.
    Secondary hits used for discovery, not accepted claims.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round42-mineral-independent-dedup.txt
  locator: Current/original data, research, reviews and history
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: context_only
  summary: Root independently searched current/original scientific trees with hidden/ignored
    included and followed links; author ten referenced raw-root search read, not independently
    rerun. Missing referenced paths and unextracted binary text are explicit. No machine-wide
    or exhaustive notice-absence claim.
  snapshot_sha256: a97a374493bb970abac67569d7817c3fd37c8a8c7ee9eec353293d1d86d9a137
  search_scope: Root independently searched current/original scientific trees with
    hidden/ignored included and followed links; author ten referenced raw-root search
    read, not independently rerun. Missing referenced paths and unextracted binary
    text are explicit. No machine-wide or exhaustive notice-absence claim.
- evidence_id: micas
  kind: authority
  reference: https://doi.org/10.1346/CCMN.1998.0460513
  locator: Rieder et al1998, original pages586 and589/Table4
  accessed_at: '2026-10-12T02:03:35.861638Z'
  support: supports
  summary: Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic
    replacement. Original Rieder1998 page586 records IMA approval; page589/Table4
    defines lepidolite as a series covering micas near the trilithionite-polylithionite
    join. An incompletely characterized mixed feed is not an endmember assay.
  snapshot_sha256: 8661dd8e830f3cab69ee6659ce05b3295df72afd8db6d8b21974da4f454058a3
assessments:
- assessment_id: identity
  area: identity
  topic: Dated nomenclature, formula and material scope
  outcome: supported
  target_ids:
  - cmmmech:polylithionite
  summary: September2026 IMA row lists polylithionite KLi2AlSi4O10F2, A status and1998s.p.
    Page1 defines special-procedure years. The older Handbook generalized KLi2AlSi4O10(F,OH)2
    and natural analyses remain separate from the dated ideal formula.
  evidence_ids:
  - record
  - ima
  - handbook
  - micas
  dimensions:
  - name: material
    value: Mineral species
    definition: Distinct from lithium element, bulk concentrate and manufactured product.
    evidence_ids:
    - record
    - ima
  - name: criticality
    value: Not asserted
    definition: No constituent-element criticality inherited.
    evidence_ids:
    - record
  - name: mechanism
    value: Not asserted
    definition: Mixed-feed microbial evidence remains outside this identity record.
    evidence_ids:
    - record
  - name: scale
    value: Geological context
    definition: Occurrence does not establish deployment, ore grade or recovery.
    evidence_ids:
    - record
    - handbook
- assessment_id: context
  area: evidence
  topic: Geological and series-name limits
  outcome: supported
  target_ids:
  - cmmmech:polylithionite
  summary: Handbook supports Lovozero syenite-pegmatite occurrence and metasomatic
    replacement. Original Rieder1998 page586 records IMA approval; page589/Table4
    defines lepidolite as a series covering micas near the trilithionite-polylithionite
    join. An incompletely characterized mixed feed is not an endmember assay.
  evidence_ids:
  - record
  - ima
  - handbook
  - micas
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE history and exact inspected state
  outcome: supported
  target_ids:
  - cmmmech:polylithionite
  summary: Native captured hashes match frozen inputs; named and cohort gates passed.
    No previous provenance rewritten.
  evidence_ids:
  - record
  - history
  - checks
  - inspection
findings: []
actions: []
limitations:
- IMA scope is explicitly September2026; older Handbook context does not assert current
  production.
- No microbial mechanism, criticality designation or industrial deployment is claimed.
- Original nineteenth-century descriptions and crystallographic measurements were
  not reprocessed; authority identity scope does not require that.
- Mixed-feed microbial leads remain separate research tasks.
- Search bounds and unavailable referenced paths are explicit; source exhaustion is
  not established.
tags:
- round42
- independent
- mineral
- identity
```
