# Independent scientific review of Voltaite

- Review: 20261015T184530Z-voltaite-round100-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T18:32:13.970535Z
- Finished UTC: 2026-10-15T18:45:30.203853Z
- Reviewer: codex /root/round100_pentagonite (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of the exact mineral identity record. Original evidence, methods and limitations support its scoped claims; no corrective owner finding.

## Scope And Provenance

Entire frozen maintained owner and linked CREATE history, current identity authority, complete claim-bearing primary article and bounded conflicting-evidence/notice searches. No independent diffraction refinement or full literature census.

Selection: Parent-assigned independent assessment after curator freeze.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b6831c1da19b475ea048baea4ba5c10b96d678af.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:voltaite | data/records/voltaite.yaml | maintained | Voltaite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent primary-evidence and identity assessment | passed | True | cmmmech:voltaite | Original methods, results, figures/tables and current authority checked against exact frozen inputs. |
| Independent strict named-record validation | passed | True | cmmmech:voltaite | Independently executed: two records checked, zero failed. |
| Completed coordinator batch check 1 | passed | True | cmmmech:voltaite | Verified the completed coordinator receipt, log hash and unchanged assigned inputs. This is not a claimed duplicate independent execution. |
| Completed coordinator batch check 2 | passed | True | cmmmech:voltaite | Verified the completed coordinator receipt, log hash and unchanged assigned inputs. This is not a claimed duplicate independent execution. |
| Completed coordinator batch check 3 | passed | True | cmmmech:voltaite | Verified the completed coordinator receipt, log hash and unchanged assigned inputs. This is not a claimed duplicate independent execution. |
| Completed coordinator batch check 4 | passed | True | cmmmech:voltaite | Verified the completed coordinator receipt, log hash and unchanged assigned inputs. This is not a claimed duplicate independent execution. |

## Scientific And Domain Assessments

### Species versus mineral group

identity: supported. Targets: cmmmech:voltaite.

Current cubic species identity is supported.

IMA grandfathered G, original-description year 1841, K2Fe(II)5Fe(III)3Al(SO4)12(H2O)18. Distinct from the voltaite group, tetragonal pertlikite, Mg-, Zn- and ammonium-dominant members; 1841 is not an approval accession.

### Selected crystals and mixed assemblages

scope: supported. Targets: cmmmech:voltaite.

Two specimens are correctly scoped.

Ni4225 from the 1988 Nikitovka coal-fire collection and SCCIII-14-20s from Bolshoi Semiachik are the only 2023 samples labelled voltaite. Tables 1–2 support cubic Fd-3c at 293 K; no clear lowered symmetry in these samples does not refute all synthetic-sector observations. Figures 2–3 show mixed associated sulfates, not pure bulk feed or controlled formation.

### EDS, oxidation state, water and A-site discrepancy

quantity: supported. Targets: cmmmech:voltaite.

The record correctly preserves calculated quantities and conflicting source accounting.

Section 3.2 calculates Fe(II)/Fe(III) by charge balance and water using 18 H2O per formula unit; Table 4 normalizes unpolished specimens. NH4+Na+K sums to 1.00 for Ni4225 and 1.02 for SCCIII, whereas its footnote says normalization to 2.00 and the full A site/ideal formula imply two. Table 2 Ni N/K 0.365/0.635 differs from the Table 4 chemical ratio. The record does not invent vacancies or double values. SCCIII Fe(II)/Mg 2.54/2.51 lies near the species boundary; no reclassification is inferred.

### Disorder and incomplete raw-data access

evidence: supported. Targets: cmmmech:voltaite.

Refinement limitations remain explicit.

Table 2 and section 3.1 use restrained H positions for one water type; Al-bound-water H was not refined because of disorder. Deposit identifiers 2303617/2303618 are reported, but their original files were not acquired or re-refined. Geological temperature estimates are not experimental synthesis conditions.

### Criticality, mechanism and deployment

scope: supported. Targets: cmmmech:voltaite.

No unsupported criticality or biological/application claim is present.

Material kind is mineral. Criticality is unrecorded, not declared absent or inherited from constituent elements. Neither record asserts an organism, strain, biomass mechanism, extraction yield, recovered product or industrial deployment. Geological occurrence alone would not establish those claims.

### Actual review and change provenance

provenance: supported. Targets: cmmmech:voltaite.

Exact inputs and the separate CREATE events are auditable.

Native inspect captured the trusted base and exact owner/history/dossier/schema bytes before assessment. Canonical and inline CREATE events are distinct actual provenance. This reviewer authored pentagonite rather than either sulfate. Completed coordinator batch results were verified without claiming duplicate execution.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/voltaite.yaml; Entire exact maintained owner captured by native inspect. | supports | Identity, source scope, measured/modelled distinction, uncertainty and provenance inspected. |
| history | history/records/voltaite/2026-10-15T182803Z-codex-b82d46.yaml; Canonical CREATE and separate inline CREATE. | supports | Actual actor, model, timestamp, target and described work agree; no immutable-history rewrite. |
| dossier | research/sources/round100-sulfates/20261015T183043Z-source-investigation.json; Paired JSON/Markdown dossier and linked raw acquisition receipts. | context_only | Curator handoff is context; accepted science was independently checked in originals. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Official September 2026 PDF: field definitions pages 1–2; species page 230; text and rendered row independently inspected. | supports | Accepted species formula and status checked. Mineral authority does not establish criticality. |
| search | Independent bounded notice, conflict and local duplicate checks; /private/tmp/cmm-round100-sulfates-independent-review/search.json; /private/tmp/cmm-round100-sulfates-independent-review/dedup.txt | context_only | No attributable affecting correction surfaced in these result sets. Local matches are the new owners and historical context/handoffs; ignored/hidden files were included. |
| named | uv run --locked cmmmech validate data/records/voltaite.yaml data/records/pertlikite.yaml; /private/tmp/cmm-round100-sulfates-independent-review/validation.log | supports | Independent affected-file validation exited zero; structural validation is not proof of scientific truth. |
| batch | /private/tmp/cmm-round100-final-gates.json; Completed receipt and /private/tmp/cmm-round100-final-gates.log; log SHA256 1d26fc881828a6ce668c84c6458674b6be8a6af044068c144323a7200677e32d | supports | Required batch commands exited zero; exact target/context hashes were rechecked before save. |
| primary | https://doi.org/10.3390/sym15122126; Complete official 14-page 2023 PDF: sections 2.1–3.2, Tables 1–4, Figures 1–5 and discussion/data-availability pages 10–12. | supports | Two natural/coal-fire specimens support the limited identity claim; calculated chemistry and inconsistent A-site accounting are preserved. |
| handbook | https://handbookofmineralogy.org/pdfs/voltaite.pdf; Complete one-page version 1, 2001–2005; formula and chemistry columns. | context_only | Historical variable Fe(III)/Al formula and Fe(III)-only calculated composition do not replace the current IMA ideal. |

## Limits And Additional Notes

- The unresolved 2023 A-site accounting prevents acceptance of its reported chemical values as an exact ideal formula or a verified vacancy model; source clarification remains useful.
- CCDC/FIZ original deposits were not acquired or independently re-refined. Unavailable 2013 synthetic-study methods were not accepted from its accessible supplement alone.
- Two labelled specimens do not establish universal voltaite composition, environmental transformation kinetics, a pure bulk feed, or microbial/industrial recovery.
- The historical 1841 original description was not acquired; current species status rests on the official IMA list and inspected later primary study.
- Shared primary acquisitions are disclosed; this reviewer independently read originals and visually checked claim-bearing figures/tables after native capture.
- DOI landing-page access via the web tool failed during peer review; original article headers, official/archive PDF provenance and Crossref records verify the citations. Current IMA web access succeeded.
- Search coverage is bounded. No global absence of contrary publications, corrections or microbes is asserted.
- Whole-corpus structured-review checking follows saving these native bundles; no review or history is overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T184530Z-voltaite-round100-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Voltaite
started_at: '2026-10-15T18:32:13.970535Z'
finished_at: '2026-10-15T18:45:30.203853Z'
reviewer:
  identity: codex /root/round100_pentagonite
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The separate sulfate curator authored the owner and history.
    I curated pentagonite, independently inspected the exact sulfate inputs and original
    evidence, and made no sulfate owner/history edits.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified acceptance of the exact mineral identity record. Original evidence,
  methods and limitations support its scoped claims; no corrective owner finding.
source:
  git_revision: b6831c1da19b475ea048baea4ba5c10b96d678af
  state: working_tree
  inputs:
  - path: data/records/voltaite.yaml
    sha256: 04192b1dedc33a17cd294639ca2d53a63afd2665804207d330ce68f2bb236605
    role: target
  - path: history/records/voltaite/2026-10-15T182803Z-codex-b82d46.yaml
    sha256: 03559455b62be9bab3c63d373d8670cc43772e93683d654e7517ec764c62b83e
    role: context
  - path: research/sources/round100-sulfates/20261015T183043Z-source-investigation.json
    sha256: f0bbc92549128d225a8ef30b5875bb098db49030155d8b82cc45282a20a608fe
    role: context
  - path: research/sources/round100-sulfates/20261015T183043Z-source-investigation.md
    sha256: 931982d05dac995041ac2c01be300c77473415b3f76e8628486b6d00f821472e
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen maintained owner and linked CREATE history, current identity
    authority, complete claim-bearing primary article and bounded conflicting-evidence/notice
    searches. No independent diffraction refinement or full literature census.
  selection: Parent-assigned independent assessment after curator freeze.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:voltaite
targets:
- target_id: cmmmech:voltaite
  path: data/records/voltaite.yaml
  label: Voltaite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/voltaite.yaml
    role: maintained_record
checks:
- check_id: science
  name: Independent primary-evidence and identity assessment
  required: true
  status: passed
  summary: Original methods, results, figures/tables and current authority checked
    against exact frozen inputs.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - primary
  - ima
  - search
- check_id: named
  name: Independent strict named-record validation
  required: true
  status: passed
  command: uv run --locked cmmmech validate data/records/voltaite.yaml data/records/pertlikite.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'Independently executed: two records checked, zero failed.'
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - named
- check_id: batch1
  name: Completed coordinator batch check 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified the completed coordinator receipt, log hash and unchanged assigned
    inputs. This is not a claimed duplicate independent execution.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed coordinator batch check 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Verified the completed coordinator receipt, log hash and unchanged assigned
    inputs. This is not a claimed duplicate independent execution.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed coordinator batch check 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base b6831c1da19b475ea048baea4ba5c10b96d678af
  exit_code: 0
  expected_exit_code: 0
  summary: Verified the completed coordinator receipt, log hash and unchanged assigned
    inputs. This is not a claimed duplicate independent execution.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed coordinator batch check 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified the completed coordinator receipt, log hash and unchanged assigned
    inputs. This is not a claimed duplicate independent execution.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/voltaite.yaml
  locator: Entire exact maintained owner captured by native inspect.
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Identity, source scope, measured/modelled distinction, uncertainty and
    provenance inspected.
  snapshot_sha256: 04192b1dedc33a17cd294639ca2d53a63afd2665804207d330ce68f2bb236605
- evidence_id: history
  kind: record_content
  reference: history/records/voltaite/2026-10-15T182803Z-codex-b82d46.yaml
  locator: Canonical CREATE and separate inline CREATE.
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Actual actor, model, timestamp, target and described work agree; no immutable-history
    rewrite.
  snapshot_sha256: 03559455b62be9bab3c63d373d8670cc43772e93683d654e7517ec764c62b83e
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round100-sulfates/20261015T183043Z-source-investigation.json
  locator: Paired JSON/Markdown dossier and linked raw acquisition receipts.
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: context_only
  summary: Curator handoff is context; accepted science was independently checked
    in originals.
  snapshot_sha256: f0bbc92549128d225a8ef30b5875bb098db49030155d8b82cc45282a20a608fe
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'Official September 2026 PDF: field definitions pages 1–2; species page
    230; text and rendered row independently inspected.'
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Accepted species formula and status checked. Mineral authority does not
    establish criticality.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: search
  kind: search
  reference: Independent bounded notice, conflict and local duplicate checks
  locator: /private/tmp/cmm-round100-sulfates-independent-review/search.json; /private/tmp/cmm-round100-sulfates-independent-review/dedup.txt
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: context_only
  summary: No attributable affecting correction surfaced in these result sets. Local
    matches are the new owners and historical context/handoffs; ignored/hidden files
    were included.
  search_scope: 'Queries: exact 2008 DOI with erratum/correction/retraction; exact
    2023 DOI with correction/retraction; pertlikite with Mossbauer and water; voltaite
    with Ni4225. First returned sets on 2026-10-15, no exhaustive pagination. rg --no-ignore
    --hidden --follow covered records/research/reviews/history/local skills, current
    sulfate raw directory and all 253 issues in the coordinator snapshot. Secondary
    search pages were discovery only.'
  snapshot_sha256: 1d2be483cd68e3505ff62e2ae3c864da5802ff435741b2006b3528aec83e8fac
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/voltaite.yaml data/records/pertlikite.yaml
  locator: /private/tmp/cmm-round100-sulfates-independent-review/validation.log
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Independent affected-file validation exited zero; structural validation
    is not proof of scientific truth.
  snapshot_sha256: 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round100-final-gates.json
  locator: Completed receipt and /private/tmp/cmm-round100-final-gates.log; log SHA256
    1d26fc881828a6ce668c84c6458674b6be8a6af044068c144323a7200677e32d
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Required batch commands exited zero; exact target/context hashes were rechecked
    before save.
  snapshot_sha256: 3a6f970f9a5bb1e442804dd5529b6eb0acfdcb76a9311cda62204cf368c6b939
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/sym15122126
  locator: 'Complete official 14-page 2023 PDF: sections 2.1–3.2, Tables 1–4, Figures
    1–5 and discussion/data-availability pages 10–12.'
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: supports
  summary: Two natural/coal-fire specimens support the limited identity claim; calculated
    chemistry and inconsistent A-site accounting are preserved.
  snapshot_sha256: dc4ebd473cb4bdfef5d5d66cc4b96bab9e644e199afa9f8fccb2e19e7a2428bf
- evidence_id: handbook
  kind: authority
  reference: https://handbookofmineralogy.org/pdfs/voltaite.pdf
  locator: Complete one-page version 1, 2001–2005; formula and chemistry columns.
  accessed_at: '2026-10-15T18:45:30.203853Z'
  support: context_only
  summary: Historical variable Fe(III)/Al formula and Fe(III)-only calculated composition
    do not replace the current IMA ideal.
  snapshot_sha256: 9e9a57eea7884478028ced3f756251c78b0c125159114e797708adf55585eaab
assessments:
- assessment_id: identity
  area: identity
  topic: Species versus mineral group
  outcome: supported
  summary: Current cubic species identity is supported.
  details: IMA grandfathered G, original-description year 1841, K2Fe(II)5Fe(III)3Al(SO4)12(H2O)18.
    Distinct from the voltaite group, tetragonal pertlikite, Mg-, Zn- and ammonium-dominant
    members; 1841 is not an approval accession.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - ima
  - primary
  - handbook
- assessment_id: specimens
  area: scope
  topic: Selected crystals and mixed assemblages
  outcome: supported
  summary: Two specimens are correctly scoped.
  details: Ni4225 from the 1988 Nikitovka coal-fire collection and SCCIII-14-20s from
    Bolshoi Semiachik are the only 2023 samples labelled voltaite. Tables 1–2 support
    cubic Fd-3c at 293 K; no clear lowered symmetry in these samples does not refute
    all synthetic-sector observations. Figures 2–3 show mixed associated sulfates,
    not pure bulk feed or controlled formation.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - primary
- assessment_id: composition
  area: quantity
  topic: EDS, oxidation state, water and A-site discrepancy
  outcome: supported
  summary: The record correctly preserves calculated quantities and conflicting source
    accounting.
  details: Section 3.2 calculates Fe(II)/Fe(III) by charge balance and water using
    18 H2O per formula unit; Table 4 normalizes unpolished specimens. NH4+Na+K sums
    to 1.00 for Ni4225 and 1.02 for SCCIII, whereas its footnote says normalization
    to 2.00 and the full A site/ideal formula imply two. Table 2 Ni N/K 0.365/0.635
    differs from the Table 4 chemical ratio. The record does not invent vacancies
    or double values. SCCIII Fe(II)/Mg 2.54/2.51 lies near the species boundary; no
    reclassification is inferred.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - primary
- assessment_id: structure_limits
  area: evidence
  topic: Disorder and incomplete raw-data access
  outcome: supported
  summary: Refinement limitations remain explicit.
  details: Table 2 and section 3.1 use restrained H positions for one water type;
    Al-bound-water H was not refined because of disorder. Deposit identifiers 2303617/2303618
    are reported, but their original files were not acquired or re-refined. Geological
    temperature estimates are not experimental synthesis conditions.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - primary
- assessment_id: application_boundaries
  area: scope
  topic: Criticality, mechanism and deployment
  outcome: supported
  summary: No unsupported criticality or biological/application claim is present.
  details: Material kind is mineral. Criticality is unrecorded, not declared absent
    or inherited from constituent elements. Neither record asserts an organism, strain,
    biomass mechanism, extraction yield, recovered product or industrial deployment.
    Geological occurrence alone would not establish those claims.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - primary
  - ima
- assessment_id: provenance
  area: provenance
  topic: Actual review and change provenance
  outcome: supported
  summary: Exact inputs and the separate CREATE events are auditable.
  details: Native inspect captured the trusted base and exact owner/history/dossier/schema
    bytes before assessment. Canonical and inline CREATE events are distinct actual
    provenance. This reviewer authored pentagonite rather than either sulfate. Completed
    coordinator batch results were verified without claiming duplicate execution.
  target_ids:
  - cmmmech:voltaite
  evidence_ids:
  - owner
  - history
  - dossier
  - named
  - batch
findings: []
actions: []
limitations:
- The unresolved 2023 A-site accounting prevents acceptance of its reported chemical
  values as an exact ideal formula or a verified vacancy model; source clarification
  remains useful.
- CCDC/FIZ original deposits were not acquired or independently re-refined. Unavailable
  2013 synthetic-study methods were not accepted from its accessible supplement alone.
- Two labelled specimens do not establish universal voltaite composition, environmental
  transformation kinetics, a pure bulk feed, or microbial/industrial recovery.
- The historical 1841 original description was not acquired; current species status
  rests on the official IMA list and inspected later primary study.
notes:
- Shared primary acquisitions are disclosed; this reviewer independently read originals
  and visually checked claim-bearing figures/tables after native capture.
- DOI landing-page access via the web tool failed during peer review; original article
  headers, official/archive PDF provenance and Crossref records verify the citations.
  Current IMA web access succeeded.
- Search coverage is bounded. No global absence of contrary publications, corrections
  or microbes is asserted.
- Whole-corpus structured-review checking follows saving these native bundles; no
  review or history is overwritten.
```
