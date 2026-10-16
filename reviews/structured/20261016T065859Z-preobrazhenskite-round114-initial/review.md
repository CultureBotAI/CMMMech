# Independent initial scientific review of preobrazhenskite

- Review: 20261016T065859Z-preobrazhenskite-round114-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T06:56:13.288806Z
- Finished UTC: 2026-10-16T06:58:59.115575Z
- Reviewer: codex /root/round104_ree (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed minor source-locator finding requires correction. Natural-mineral identity and bounded structural interpretation are supported; current final batch checks remain pending, so this is not a passing acceptance.

## Scope And Provenance

Exact preobrazhenskite owner and source context; identity, structural evidence, scientific limits and citation locators inspected. Final batch gates pending.

Selection: Assigned frozen record captured through native inspect before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 93f90797512dc8d1db3df9ce2e4994c475b1a4fe.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:preobrazhenskite | data/records/preobrazhenskite.yaml | maintained | Preobrazhenskite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:preobrazhenskite | Actual named command completed with2 records/0 failures; base/cwd/hash/log bindings verified. |
| Completed final batch gates | unavailable | True | cmmmech:preobrazhenskite | Coordinator final gate is not accepted as terminal current-state evidence in this initial observation; no batch success is claimed. |

## Scientific And Domain Assessments

### Current species and natural crystal

identity: supported. Targets: cmmmech:preobrazhenskite.

Current Mg-borate identity, Inder crystal and Pbcn structure are supported; no elemental/commodity or microbial claim.

### Hydrogen and fitted spectroscopy

evidence: supported. Targets: cmmmech:preobrazhenskite.

Original pp.388–395 support located H positions, uncertain local symmetry, proposed rather than measured transition, opposite printed observation inequality and switched H labels. Fitted IR components remain distinct from resolved peaks.

### Primary-source navigation

provenance: concern. Targets: cmmmech:preobrazhenskite.

The owner and paired JSON misidentify figure/page locators; correct the bounded references before final acceptance.

## Findings

### F1: Primary figure/page locators are incorrect

minor / open / confirmed; issue key: round114-preobrazhenskite-primary-locators.

The owner sources[1].title calls the IR fit Figure5 pp.395–396, but Figure5 is a structural projection on p.393; the IR spectrum/fit is Figure7 p.394 and its Table6 is p.395. The same title places hydrogen Table5/Figures3–4 at pp.393–395, but Table5 is p.390 and Figures3–4 p.392. Context primary_sources[2].checked truncates the figure inventory to1–5 although the paper has1–9. Scientific identity/H-model interpretation remains supported; these are bounded provenance errors, not altered measurements.

## Recommended Actions And Acceptance Checks

### A1

Correct only the maintained source locators and context figure inventory, preserving the exact initial observation and predecessor context.

- Read original printed figure/table/page labels and use Figure7 p.394, Table6 p.395; Table5 p.390 and Figures3–4 p.392.
- Correct the context figure count to1–9, retain old bytes and exact change receipt, and append actual canonical and inline EDIT provenance for the owner.
- Revalidate the changed owner, capture fresh exact inputs, and save an independent successor with this issue_key and exact predecessor finding; use actual terminal final batch gates before positive acceptance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/preobrazhenskite.yaml; sources[1].title and full owner | supports | Exact captured owner contains incorrect source locators; scientific description retains the source uncertainties. |
| source | https://www.frankhawthorne.com/_files/ugd/70a3a9_52f962a50804426ca437455347705cfe.pdf; Full original pp.387–396, all nine figures/six tables read and visually inspected; Table5 p.390, Figures3–4 p.392, structural Figures5–6 p.393, IR Figure7 p.394, Table6/Figures8–9 p.395. | refutes | The correct IR spectrum/fit is Figure7, not Figure5; published figure and page labels directly refute the owner locator. |
| dossier | research/sources/round114-borates/20261016T065455Z-source-investigation.json; primary_sources[2].checked | refutes | The paired context states Figures1–5 although the complete primary has Figures1–9; exact predecessor bytes captured. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions p.1 and Preobrazhenskite row p.177 visually checked; bytes match independently acquired current REE authority. | supports | Grandfathered Mg3B11O15(OH)9 with description year1956, not an approval accession. |
| cif | https://www.crystallography.net/cod/9004294.cif; Complete derivative CIF, revision293658, identity/cell/atomic and displacement loops and original-source relationship. | supports | COD9004294 identifies this Burns-Hawthorne1994 experiment; not independent replication or original reflections. |
| named | /private/tmp/cmm-round114-ree-research/borate-review-named-validation-initial.json; Exact command/cwd/base/owner hashes and log checked; completed 2026-10-16T06:57:41.322154+00:00 | supports | Two records checked, zero failed; does not validate the incorrect literature locator. |

## Limits And Additional Notes

- No original measured reflections acquired or independent structure refinement performed.
- Source-local inequality/H-label ambiguity remains an acknowledged scientific limit; this review does not silently repair the source model.
- Final batch checks and successor acceptance remain outstanding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T065859Z-preobrazhenskite-round114-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial scientific review of preobrazhenskite
started_at: '2026-10-16T06:56:13.288806Z'
finished_at: '2026-10-16T06:58:59.115575Z'
reviewer:
  identity: codex /root/round104_ree
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/round104_borates; no edits
    to this owner/history/dossier. Shared original acquisition independently read;
    reviewer authored separate ancylite-Ce/calcioancylite-La owners.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: 93f90797512dc8d1db3df9ce2e4994c475b1a4fe
  state: working_tree
  inputs:
  - path: data/records/preobrazhenskite.yaml
    sha256: 4cecffdb8b7c2fe2c0676fc88bfe97004369ca1dc641ff5e2a72cd4042acd642
    role: target
  - path: history/records/preobrazhenskite/2026-10-16T065154Z-codex-17a4a3.yaml
    sha256: 909378f8f28f17f17ad0b0085cf71c238ee421a0d7cc0941b8fb3fd2871468be
    role: context
  - path: research/sources/round114-borates/20261016T065455Z-source-investigation.json
    sha256: 0749d9fa1fda339d7fdc8418129cfe9b40ad9e404378bf6f01e9261cd643ff1f
    role: context
  - path: research/sources/round114-borates/20261016T065455Z-source-investigation.md
    sha256: 451f4217b20ec77851e8f9e29712cc761891cebfa8b34a3acd05466cc12bfc48
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:preobrazhenskite
  path: data/records/preobrazhenskite.yaml
  label: Preobrazhenskite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/preobrazhenskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: history/records/preobrazhenskite/2026-10-16T065154Z-codex-17a4a3.yaml
    role: canonical_history
scope:
  description: Exact preobrazhenskite owner and source context; identity, structural
    evidence, scientific limits and citation locators inspected. Final batch gates
    pending.
  selection: Assigned frozen record captured through native inspect before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:preobrazhenskite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/preobrazhenskite.yaml
  locator: sources[1].title and full owner
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: supports
  summary: Exact captured owner contains incorrect source locators; scientific description
    retains the source uncertainties.
  snapshot_sha256: 4cecffdb8b7c2fe2c0676fc88bfe97004369ca1dc641ff5e2a72cd4042acd642
- evidence_id: source
  kind: primary_source
  reference: https://www.frankhawthorne.com/_files/ugd/70a3a9_52f962a50804426ca437455347705cfe.pdf
  locator: Full original pp.387–396, all nine figures/six tables read and visually
    inspected; Table5 p.390, Figures3–4 p.392, structural Figures5–6 p.393, IR Figure7
    p.394, Table6/Figures8–9 p.395.
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: refutes
  summary: The correct IR spectrum/fit is Figure7, not Figure5; published figure and
    page labels directly refute the owner locator.
  snapshot_sha256: 41426548bb763451ef85c7ac8229955dc636b85a02324a2191cd5a212e1a2890
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round114-borates/20261016T065455Z-source-investigation.json
  locator: primary_sources[2].checked
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: refutes
  summary: The paired context states Figures1–5 although the complete primary has
    Figures1–9; exact predecessor bytes captured.
  snapshot_sha256: 0749d9fa1fda339d7fdc8418129cfe9b40ad9e404378bf6f01e9261cd643ff1f
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions p.1 and Preobrazhenskite row p.177 visually checked; bytes
    match independently acquired current REE authority.
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: supports
  summary: Grandfathered Mg3B11O15(OH)9 with description year1956, not an approval
    accession.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: cif
  kind: database
  reference: https://www.crystallography.net/cod/9004294.cif
  locator: Complete derivative CIF, revision293658, identity/cell/atomic and displacement
    loops and original-source relationship.
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: supports
  summary: COD9004294 identifies this Burns-Hawthorne1994 experiment; not independent
    replication or original reflections.
  snapshot_sha256: 90232f434c760317194da14ae02d89b05eba4721f09fa253af250aa0f6812061
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round114-ree-research/borate-review-named-validation-initial.json
  locator: Exact command/cwd/base/owner hashes and log checked; completed 2026-10-16T06:57:41.322154+00:00
  accessed_at: '2026-10-16T06:58:59.115575Z'
  support: supports
  summary: Two records checked, zero failed; does not validate the incorrect literature
    locator.
  snapshot_sha256: 04e1283befdb7e76956e557e6bb43273750066f0d13f1a7e9557ce5e6a5124cc
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate --require-records data/records/kaliborite.yaml
    data/records/preobrazhenskite.yaml
  status: passed
  required: true
  summary: Actual named command completed with2 records/0 failures; base/cwd/hash/log
    bindings verified.
  target_ids:
  - cmmmech:preobrazhenskite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch
  name: Completed final batch gates
  command: just check; uv run --locked cmmmech validate --require-records; uv run
    --locked cmmmech validate-history --base 93f90797512dc8d1db3df9ce2e4994c475b1a4fe
  status: unavailable
  required: true
  summary: Coordinator final gate is not accepted as terminal current-state evidence
    in this initial observation; no batch success is claimed.
  target_ids:
  - cmmmech:preobrazhenskite
assessments:
- assessment_id: identity
  area: identity
  topic: Current species and natural crystal
  outcome: supported
  summary: Current Mg-borate identity, Inder crystal and Pbcn structure are supported;
    no elemental/commodity or microbial claim.
  target_ids:
  - cmmmech:preobrazhenskite
  evidence_ids:
  - record
  - ima
  - cif
- assessment_id: limits
  area: evidence
  topic: Hydrogen and fitted spectroscopy
  outcome: supported
  summary: Original pp.388–395 support located H positions, uncertain local symmetry,
    proposed rather than measured transition, opposite printed observation inequality
    and switched H labels. Fitted IR components remain distinct from resolved peaks.
  target_ids:
  - cmmmech:preobrazhenskite
  evidence_ids:
  - record
  - source
  - cif
- assessment_id: locators
  area: provenance
  topic: Primary-source navigation
  outcome: concern
  summary: The owner and paired JSON misidentify figure/page locators; correct the
    bounded references before final acceptance.
  target_ids:
  - cmmmech:preobrazhenskite
  evidence_ids:
  - record
  - source
  - dossier
findings:
- finding_id: F1
  issue_key: round114-preobrazhenskite-primary-locators
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Primary figure/page locators are incorrect
  description: The owner sources[1].title calls the IR fit Figure5 pp.395–396, but
    Figure5 is a structural projection on p.393; the IR spectrum/fit is Figure7 p.394
    and its Table6 is p.395. The same title places hydrogen Table5/Figures3–4 at pp.393–395,
    but Table5 is p.390 and Figures3–4 p.392. Context primary_sources[2].checked truncates
    the figure inventory to1–5 although the paper has1–9. Scientific identity/H-model
    interpretation remains supported; these are bounded provenance errors, not altered
    measurements.
  target_ids:
  - cmmmech:preobrazhenskite
  field_paths:
  - sources[1].title
  - research/sources/round114-borates/20261016T065455Z-source-investigation.json#/primary_sources/2/checked
  evidence_ids:
  - record
  - source
  - dossier
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/preobrazhenskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round114-borates/20261016T065455Z-source-investigation.json
    role: context
actions:
- action_id: A1
  description: Correct only the maintained source locators and context figure inventory,
    preserving the exact initial observation and predecessor context.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:preobrazhenskite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/preobrazhenskite.yaml
    role: maintained_record
  - repository: CultureBotAI/CMMMech
    path: research/sources/round114-borates/20261016T065455Z-source-investigation.json
    role: context
  acceptance_checks:
  - Read original printed figure/table/page labels and use Figure7 p.394, Table6 p.395;
    Table5 p.390 and Figures3–4 p.392.
  - Correct the context figure count to1–9, retain old bytes and exact change receipt,
    and append actual canonical and inline EDIT provenance for the owner.
  - Revalidate the changed owner, capture fresh exact inputs, and save an independent
    successor with this issue_key and exact predecessor finding; use actual terminal
    final batch gates before positive acceptance.
summary: One confirmed minor source-locator finding requires correction. Natural-mineral
  identity and bounded structural interpretation are supported; current final batch
  checks remain pending, so this is not a passing acceptance.
limitations:
- No original measured reflections acquired or independent structure refinement performed.
- Source-local inequality/H-label ambiguity remains an acknowledged scientific limit;
  this review does not silently repair the source model.
- Final batch checks and successor acceptance remain outstanding.
```
