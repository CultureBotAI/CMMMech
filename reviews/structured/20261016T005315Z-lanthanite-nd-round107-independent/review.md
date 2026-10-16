# Independent scientific review of Lanthanite-(Nd)

- Review: 20261016T005315Z-lanthanite-nd-round107-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T00:39:46.105753Z
- Finished UTC: 2026-10-16T00:53:15.767393Z
- Reviewer: codex /root/round104_borates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of the distinct natural mineral identity and characterization. No supported corrective owner finding was identified.

## Scope And Provenance

Complete exact owner, species identity, natural-specimen characterization and history. Broader deferred-source handoffs and future GitHub publication excluded.

Selection: Assigned named owner; initial native capture preceded scientific judgment. Later context capture adds the finalized paired dossier without changing any initial input hash.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 27d842b3e6239bf60565f93c958d3f2cad395037.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lanthanite-nd | data/records/lanthanite-nd.yaml | maintained | Lanthanite-(Nd) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict validation | passed | True | cmmmech:lanthanite-nd | Checked 2 record(s); 0 failed. Actual execution 2026-10-16T00:40:54.535452+00:00 through 2026-10-16T00:41:00.015947+00:00 |
| Actual final batch command 1 | passed | True | cmmmech:lanthanite-nd | Coordinator execution 2026-10-16T00:44:33.569603+00:00 through 2026-10-16T00:51:25.649736+00:00; terminal receipt and log hash verified. |
| Actual final batch command 2 | passed | True | cmmmech:lanthanite-nd | Coordinator execution 2026-10-16T00:51:25.651660+00:00 through 2026-10-16T00:51:42.046800+00:00; terminal receipt and log hash verified. |
| Actual final batch command 3 | passed | True | cmmmech:lanthanite-nd | Coordinator execution 2026-10-16T00:51:42.047805+00:00 through 2026-10-16T00:51:50.294344+00:00; terminal receipt and log hash verified. |
| Actual final batch command 4 | passed | True | cmmmech:lanthanite-nd | Coordinator execution 2026-10-16T00:51:50.295710+00:00 through 2026-10-16T00:51:57.934762+00:00; terminal receipt and log hash verified. |

## Scientific And Domain Assessments

### Species and material boundaries

identity: supported. Targets: cmmmech:lanthanite-nd.

Current authority lists Nd2(CO3)3(H2O)6·2H2O, approved A, IMA1979-074. This is the Nd-dominant mineral species, not elemental Nd, a group or bulk ore.

### Specimen-specific chemistry and measurement basis

evidence: supported. Targets: cmmmech:lanthanite-nd.

Experimental section gives 23 microprobe points on the natural Mitsukoshi sample; the record reproduces the source-reported mixed REE empirical formula and explicitly distinguishes water by difference from a direct water assay. Minor measured Tb/Dy omitted from the printed empirical formula are not silently renormalized.

### Diffraction, interpretation and unmeasured properties

evidence: supported. Targets: cmmmech:lanthanite-nd.

Crystal-data table supports Pccn at 296 K. Refinement treats all REE as Nd and excludes unreliable water H positions. Figures 1-2 and oxygen geometry support layered structure and proposed H-bond connections, not resolved hydrogen coordinates or separate REE site distributions.

### Mechanism and criticality restraint

evidence: supported. Targets: cmmmech:lanthanite-nd.

Natural mineral characterization does not establish microbial action, extraction yield or deployment. Optional mechanism and criticality fields are appropriately omitted.

### Exact input hashes, canonical history and actual checks

provenance: supported. Targets: cmmmech:lanthanite-nd.

All initially captured owner/history/schema bytes remain unchanged; final dossier was captured as additional context. Independent named validation and actual coordinator batch gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lanthanite-nd.yaml; Complete exact owner after native inspect; no edits by reviewer. | supports | All identity, quantitative and scope statements assessed. |
| history | history/records/lanthanite-nd/2026-10-16T003811Z-codex-aa4d69.yaml; Complete linked canonical CREATE and inline event. | supports | Actual actor/model/tool and target match; review completion not backdated. |
| primary | https://doi.org/10.1107/S1600536813003164; Complete PMC3588547 article HTML and rendered supplementary Comment, Experimental, Refinement, crystal-data/geometry tables; original Figures 1-3 independently viewed. Not a visual review of a downloaded PDF. Nominal PDF/CIF/HKL responses were independently checked and are HTML challenges, not valid original data files. Shared acquisition: /private/tmp/cmm-round107-ree-research/lanthanite-nd-pmc.html | supports | Independently inspected original primary evidence supports the bounded record. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Freshly acquired by curator; independently viewed definitions page1 and species row page121. Artifact /private/tmp/cmm-round107-ree-research/ima2026-09.pdf. | supports | Current authority lists Nd2(CO3)3(H2O)6·2H2O, approved A, IMA1979-074. This is the Nd-dominant mineral species, not elemental Nd, a group or bulk ore. |
| dossier | research/sources/round107-ree/20261016T004047Z-source-investigation.json; Paired dossier and source receipts; species-specific accepted claims assessed. | context_only | Shared acquisition and deferred leads disclosed; dossier is not substituted for primary evidence. |
| search | /private/tmp/cmm-round107-borates-research/review-ree-web.json; Independent exact DOI/title/author notice queries, first returned result sets. | context_only | No affecting notice identified within the bounded returned results; no exhaustive absence claim. |
| dedup | /private/tmp/cmm-round107-borates-research/review-ree-dedup.json; Actual command, path list and errors retained. | context_only | No duplicate maintained owner found in independent bounded current-WT search; broader curator precreation search separately inspected. |
| named | /private/tmp/cmm-round107-borates-research/review-ree-named-validation.json; Actual independent command/terminal exit and exact owner hashes. | supports | Two named records checked; zero failed. |
| baseline | /private/tmp/cmm-round107-baseline.json; Coordinator terminal baseline receipt and independently verified log digest 9e5774ef26487d5f888822621d15caea9fe5b73e82efdd5fe4c0192f77468740 | context_only | Baseline context only, not final-state proof. |
| batch | /private/tmp/cmm-round107-final-gates.json; Coordinator terminal receipt; exact base, unchanged owner inputs and log digest 4185f25a993d68b080a9c2a474ce5862e8284f6665a760daa83540e913968f84 independently verified. | supports | All four required batch commands passed; native persistence and publication remain separate. |

## Limits And Additional Notes

- The natural specimen is chemically mixed; the ideal formula is not a purity measurement or ore grade.
- Original CIF and reflection bytes were not acquired. Complete rendered crystallographic information supports the bounded record; no independent refinement was performed.
- The separate Vallina2015 transformation lead was not independently reviewed here and remains excluded from the owner. Its acquisition/experimental disputes are source-discovery follow-up, not accepted mechanism evidence.
- No microbial mechanism, recovered-metal yield, industrial deployment or jurisdiction/list/edition criticality designation is established or asserted.
- Correction and dedup searches are bounded. Raw source acquisition is shared; this is an independent scientific reading, not independent experimental replication.
- Structural validation is not scientific proof. Native saved-review checking and exact-head publication/hosted checks are separate later gates.
- Initial native inspection outputs are retained externally; start time uses their actual filesystem completion time. Later inspect-context outputs preserve the same original hashes and add finalized dossier context.
- No target edit was required. Already qualified source limitations are not invented corrective findings.
- Only species-related dossier sections were assessed; the deferred 2015 experiment was not independently re-reviewed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/CMMMech
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
review_id: 20261016T005315Z-lanthanite-nd-round107-independent
title: Independent scientific review of Lanthanite-(Nd)
started_at: '2026-10-16T00:39:46.105753Z'
finished_at: '2026-10-16T00:53:15.767393Z'
reviewer:
  identity: codex /root/round104_borates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/round104_ree; reviewer made
    no edits to this owner/history/dossier. Reviewer authored unrelated calcioveatchite
    and ludwigite-ore. Shared acquisition is disclosed; original source content and
    figures/tables were independently inspected after initial native capture.
source:
  git_revision: 27d842b3e6239bf60565f93c958d3f2cad395037
  state: working_tree
  inputs:
  - path: data/records/lanthanite-nd.yaml
    sha256: 1dee86d641a588d11539e26991434d33000a3cb1779ddf9911c35cb0db47c9db
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/lanthanite-nd/2026-10-16T003811Z-codex-aa4d69.yaml
    sha256: af5fd701d71b80b13c469a20846d140e64b4e18ed840ec536066ad22969d6bcf
    role: context
  - path: research/sources/round107-ree/20261016T004047Z-source-investigation.json
    sha256: 9db5743da03fd625d454d56641b6294cee7cf934cbded3b4d09d36a618d8cfed
    role: context
  - path: research/sources/round107-ree/20261016T004047Z-source-investigation.md
    sha256: 8f132cd80488868551d1988aa335d233e389864780b0dbd72181d17480b70808
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:lanthanite-nd
  path: data/records/lanthanite-nd.yaml
  label: Lanthanite-(Nd)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lanthanite-nd.yaml
    role: maintained record
scope:
  description: Complete exact owner, species identity, natural-specimen characterization
    and history. Broader deferred-source handoffs and future GitHub publication excluded.
  selection: Assigned named owner; initial native capture preceded scientific judgment.
    Later context capture adds the finalized paired dossier without changing any initial
    input hash.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lanthanite-nd
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lanthanite-nd.yaml
  locator: Complete exact owner after native inspect; no edits by reviewer.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: All identity, quantitative and scope statements assessed.
  snapshot_sha256: 1dee86d641a588d11539e26991434d33000a3cb1779ddf9911c35cb0db47c9db
- evidence_id: history
  kind: record_content
  reference: history/records/lanthanite-nd/2026-10-16T003811Z-codex-aa4d69.yaml
  locator: Complete linked canonical CREATE and inline event.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: Actual actor/model/tool and target match; review completion not backdated.
  snapshot_sha256: af5fd701d71b80b13c469a20846d140e64b4e18ed840ec536066ad22969d6bcf
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1107/S1600536813003164
  locator: 'Complete PMC3588547 article HTML and rendered supplementary Comment, Experimental,
    Refinement, crystal-data/geometry tables; original Figures 1-3 independently viewed.
    Not a visual review of a downloaded PDF. Nominal PDF/CIF/HKL responses were independently
    checked and are HTML challenges, not valid original data files. Shared acquisition:
    /private/tmp/cmm-round107-ree-research/lanthanite-nd-pmc.html'
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: Independently inspected original primary evidence supports the bounded
    record.
  snapshot_sha256: 0d195a199d946f86aa40818d4ee87ef108da5497db77b9a7e75eb721438fba26
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Freshly acquired by curator; independently viewed definitions page1 and
    species row page121. Artifact /private/tmp/cmm-round107-ree-research/ima2026-09.pdf.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: Current authority lists Nd2(CO3)3(H2O)6·2H2O, approved A, IMA1979-074.
    This is the Nd-dominant mineral species, not elemental Nd, a group or bulk ore.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round107-ree/20261016T004047Z-source-investigation.json
  locator: Paired dossier and source receipts; species-specific accepted claims assessed.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: context_only
  summary: Shared acquisition and deferred leads disclosed; dossier is not substituted
    for primary evidence.
  snapshot_sha256: 9db5743da03fd625d454d56641b6294cee7cf934cbded3b4d09d36a618d8cfed
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round107-borates-research/review-ree-web.json
  locator: Independent exact DOI/title/author notice queries, first returned result
    sets.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: context_only
  summary: No affecting notice identified within the bounded returned results; no
    exhaustive absence claim.
  snapshot_sha256: 14c09ae2250359bc8d84a74e671e9ef7dfc17c4fc1b125cdfde7ee71ab15f4b9
  search_scope: '2026-10-16 queries: "10.1107/S1600536813003164" correction erratum
    retraction; "Xenotime-(Yb)" "Buck" 1999 correction erratum; "Lanthanite-(Nd)"
    "Morrison" "Pccn". Primary full text, not snippets, supports science.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round107-borates-research/review-ree-dedup.json
  locator: Actual command, path list and errors retained.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: context_only
  summary: No duplicate maintained owner found in independent bounded current-WT search;
    broader curator precreation search separately inspected.
  snapshot_sha256: 512a892fe318fbd8650df7e8458cc0cc247e81bd1a55884919485f87321c6e26
  search_scope: rg --no-ignore --hidden --follow across current worktree records/research/reviews/history;
    exact names, IMA numbers and DOI. Ignored files included; no machine-wide absence
    assertion.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round107-borates-research/review-ree-named-validation.json
  locator: Actual independent command/terminal exit and exact owner hashes.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: Two named records checked; zero failed.
  snapshot_sha256: fc9ae1597e75945b886986eaa05565e93226f9c5c1396fc3767c61310db789d6
- evidence_id: baseline
  kind: validation
  reference: /private/tmp/cmm-round107-baseline.json
  locator: Coordinator terminal baseline receipt and independently verified log digest
    9e5774ef26487d5f888822621d15caea9fe5b73e82efdd5fe4c0192f77468740
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: context_only
  summary: Baseline context only, not final-state proof.
  snapshot_sha256: 3db8c60184af9ddd1dec47700f4a57ba703f9d4cfec97bf5a66f32d502a17c0c
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round107-final-gates.json
  locator: Coordinator terminal receipt; exact base, unchanged owner inputs and log
    digest 4185f25a993d68b080a9c2a474ce5862e8284f6665a760daa83540e913968f84 independently
    verified.
  accessed_at: '2026-10-16T00:53:15.767393Z'
  support: supports
  summary: All four required batch commands passed; native persistence and publication
    remain separate.
  snapshot_sha256: 9ecba8d70f57d4bf2df433becdf3581dca4a634de4fd5294f1c66f4aaf6b1d4c
checks:
- check_id: named
  name: Independent named strict validation
  command: uv run --locked cmmmech validate data/records/lanthanite-nd.yaml data/records/xenotime-yb.yaml
    --require-records
  status: passed
  required: true
  summary: Checked 2 record(s); 0 failed. Actual execution 2026-10-16T00:40:54.535452+00:00
    through 2026-10-16T00:41:00.015947+00:00
  target_ids:
  - cmmmech:lanthanite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch0
  name: Actual final batch command 1
  command: just check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-16T00:44:33.569603+00:00 through 2026-10-16T00:51:25.649736+00:00;
    terminal receipt and log hash verified.
  target_ids:
  - cmmmech:lanthanite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch1
  name: Actual final batch command 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator execution 2026-10-16T00:51:25.651660+00:00 through 2026-10-16T00:51:42.046800+00:00;
    terminal receipt and log hash verified.
  target_ids:
  - cmmmech:lanthanite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Actual final batch command 3
  command: uv run --locked cmmmech validate-history --base 27d842b3e6239bf60565f93c958d3f2cad395037
  status: passed
  required: true
  summary: Coordinator execution 2026-10-16T00:51:42.047805+00:00 through 2026-10-16T00:51:50.294344+00:00;
    terminal receipt and log hash verified.
  target_ids:
  - cmmmech:lanthanite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Actual final batch command 4
  command: uv run --locked python scripts/render_pages.py --check
  status: passed
  required: true
  summary: Coordinator execution 2026-10-16T00:51:50.295710+00:00 through 2026-10-16T00:51:57.934762+00:00;
    terminal receipt and log hash verified.
  target_ids:
  - cmmmech:lanthanite-nd
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
summary: Qualified acceptance of the distinct natural mineral identity and characterization.
  No supported corrective owner finding was identified.
limitations:
- The natural specimen is chemically mixed; the ideal formula is not a purity measurement
  or ore grade.
- Original CIF and reflection bytes were not acquired. Complete rendered crystallographic
  information supports the bounded record; no independent refinement was performed.
- The separate Vallina2015 transformation lead was not independently reviewed here
  and remains excluded from the owner. Its acquisition/experimental disputes are source-discovery
  follow-up, not accepted mechanism evidence.
- No microbial mechanism, recovered-metal yield, industrial deployment or jurisdiction/list/edition
  criticality designation is established or asserted.
- Correction and dedup searches are bounded. Raw source acquisition is shared; this
  is an independent scientific reading, not independent experimental replication.
- Structural validation is not scientific proof. Native saved-review checking and
  exact-head publication/hosted checks are separate later gates.
assessments:
- assessment_id: identity
  area: identity
  topic: Species and material boundaries
  outcome: supported
  summary: Current authority lists Nd2(CO3)3(H2O)6·2H2O, approved A, IMA1979-074.
    This is the Nd-dominant mineral species, not elemental Nd, a group or bulk ore.
  target_ids:
  - cmmmech:lanthanite-nd
  evidence_ids:
  - record
  - primary
  - ima
- assessment_id: chemistry
  area: evidence
  topic: Specimen-specific chemistry and measurement basis
  outcome: supported
  summary: Experimental section gives 23 microprobe points on the natural Mitsukoshi
    sample; the record reproduces the source-reported mixed REE empirical formula
    and explicitly distinguishes water by difference from a direct water assay. Minor
    measured Tb/Dy omitted from the printed empirical formula are not silently renormalized.
  target_ids:
  - cmmmech:lanthanite-nd
  evidence_ids:
  - record
  - primary
- assessment_id: structure
  area: evidence
  topic: Diffraction, interpretation and unmeasured properties
  outcome: supported
  summary: Crystal-data table supports Pccn at 296 K. Refinement treats all REE as
    Nd and excludes unreliable water H positions. Figures 1-2 and oxygen geometry
    support layered structure and proposed H-bond connections, not resolved hydrogen
    coordinates or separate REE site distributions.
  target_ids:
  - cmmmech:lanthanite-nd
  evidence_ids:
  - record
  - primary
- assessment_id: scope
  area: evidence
  topic: Mechanism and criticality restraint
  outcome: supported
  summary: Natural mineral characterization does not establish microbial action, extraction
    yield or deployment. Optional mechanism and criticality fields are appropriately
    omitted.
  target_ids:
  - cmmmech:lanthanite-nd
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Exact input hashes, canonical history and actual checks
  outcome: supported
  summary: All initially captured owner/history/schema bytes remain unchanged; final
    dossier was captured as additional context. Independent named validation and actual
    coordinator batch gates passed.
  target_ids:
  - cmmmech:lanthanite-nd
  evidence_ids:
  - record
  - history
  - dossier
  - named
  - batch
  - dedup
findings: []
actions: []
notes:
- Initial native inspection outputs are retained externally; start time uses their
  actual filesystem completion time. Later inspect-context outputs preserve the same
  original hashes and add finalized dossier context.
- No target edit was required. Already qualified source limitations are not invented
  corrective findings.
- Only species-related dossier sections were assessed; the deferred 2015 experiment
  was not independently re-reviewed.
```
