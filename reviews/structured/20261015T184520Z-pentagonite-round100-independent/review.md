# Independent scientific review of Pentagonite

- Review: 20261015T184520Z-pentagonite-round100-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T18:39:56.124306Z
- Finished UTC: 2026-10-15T18:45:20.430522Z
- Reviewer: codex /root/round100_vanadium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Distinct mineral identity and source-scoped abiotic thermal/pressure observations are supported, with explicit hydration, specimen and reversibility limits.

## Scope And Provenance

Entire frozen maintained record, canonical CREATE and inline provenance, dated identifiers, complete accessible claim-bearing original methods/results and relevant figures/tables/supplement, source dossier, and bounded counterevidence and duplicate searches.

Selection: Parent-assigned independent review after author freeze.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b6831c1da19b475ea048baea4ba5c10b96d678af.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pentagonite | data/records/pentagonite.yaml | maintained | Pentagonite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent primary-evidence assessment | passed | True | cmmmech:pentagonite | Exact owner and claim-bearing primary evidence independently assessed; preserved uncertainties are recorded below. |
| Independent named record validation | passed | True | cmmmech:pentagonite | Checked 1 record; 0 failed. |
| Completed coordinator batch check 1 | passed | True | cmmmech:pentagonite | Verified actual completed receipt, unchanged reviewed owner and complete log hash. This is coordinator execution, not an independently rerun suite. |
| Completed coordinator batch check 2 | passed | True | cmmmech:pentagonite | Verified actual completed receipt, unchanged reviewed owner and complete log hash. This is coordinator execution, not an independently rerun suite. |
| Completed coordinator batch check 3 | passed | True | cmmmech:pentagonite | Verified actual completed receipt, unchanged reviewed owner and complete log hash. This is coordinator execution, not an independently rerun suite. |
| Completed coordinator batch check 4 | passed | True | cmmmech:pentagonite | Verified actual completed receipt, unchanged reviewed owner and complete log hash. This is coordinator execution, not an independently rerun suite. |

## Scientific And Domain Assessments

### Distinct dated mineral identity

identity: supported. Targets: cmmmech:pentagonite.

Pentagonite mineral identity and topology are supported.

IMA 1971-039 is approved species status, not criticality. Ambient Ccm21 in original and later structures; distinct from cavansite despite shared nominal composition. Oregon and Wagholi specimens are not one material aliquot. Original semiquantitative composition and inferred water do not override current ideal formula.

### Protocol-specific thermal observation

evidence: supported. Targets: cmmmech:pentagonite.

The record preserves measured mass/diffraction outcomes without universalizing temperatures.

About 10 mg open-Pt powder TG-DTA in air at 10 C/min to 900 C; separate HT-XRPD at20/260/550/700 C and cooled quartz-mounted aliquot from 550 C.16.07 wt% water-assigned loss and95/220/280 C events agree with Figure 1/Table 1;1.73 wt% gain near 600 C supports authors oxidation interpretation. Figure 5 retained diffraction after550 C cooling versus amorphous at 700 C; not proof of complete water regain or cavansite conversion. ESR-silent V5+ cannot be excluded from room-temperature spectra alone.

### Separate powder media and single crystal

scope: supported. Targets: cmmmech:pentagonite.

Conditions and pressure transition brackets match tables.

Powder to 8.26(5) GPa m.e.w. 16:3:1 and 8.35(5) oil; orthorhombic/triclinic brackets2.45-2.96 and1.27-1.71 GPa agree with Tables 3A/B. Both powder rows return orthorhombic at ambient release. Oil poor/nonhydrostatic above~1 GPa qualifies comparison. Separate apparently untwinned crystal is 170 x 140 x 60 micrometres, despite Table 1B mm heading; irreversibly damaged/unindexable above~2.5 GPa.

### Modeled water and reversibility

quantity: supported. Targets: cmmmech:pentagonite.

Additional modeled oxygen is not an independent water balance.

O10 occupancies 0.94(3)/0.96(3) at 1.51(5)/2.04(5) GPa qualify ideal five-water Table 1B formulas. Disordered O9/O10, grouped displacement parameters and restraints remain explicit. Triclinic atomic structure unrefined. Powder cell symmetry reversibility neither proves complete water reversibility nor negates single-crystal damage.

### Natural formation versus laboratory heating

consistency: supported. Targets: cmmmech:pentagonite.

Later geological interpretation is retained at the supported evidentiary scope.

Ishida intermediate-amorphous phrase is qualified without falsely contradicting terminal amorphization. Ottens challenges high-temperature natural formation using paragenesis; methods yielded usable fluid-inclusion data only for calcite. Internal pressure discrepancy remains unresolved. No measured pentagonite crystallization threshold imported from either source.

### Biological, recovery and authority scope

scope: supported. Targets: cmmmech:pentagonite.

No unsupported biological or industrial transfer.

Both mechanisms are explicitly abiotic, processother, microbialfalse with no organism. No constituent criticality designation, vanadium extraction/recovered-product yield or industrial deployment inferred.

### Exact frozen revision and history

provenance: supported. Targets: cmmmech:pentagonite.

Working-tree provenance and independent review are explicit.

Native inspect preceded judgment and exact source/owner/history hashes were rechecked. Canonical CREATE and inline history are distinct; actual GPT-6 metadata retained. Named validation independently executed; coordinator whole-corpus gates were added only after actual terminal receipt, base, log and unchanged target hashes were verified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/pentagonite.yaml; Entire exact owner captured with native inspect before judging; frozen hash verified again before review drafting. | supports | Identity, conditions, outcomes and caveats match the independently assessed scope. |
| history | history/records/pentagonite/2026-10-15T182725Z-codex-20b0ae.yaml; Complete canonical CREATE and distinct inline event/history_refs. | supports | Actual GPT-6 curator metadata, target and described changes agree. No earlier authorship invented. |
| dossier | research/sources/round100-pentagonite/20261015T182949Z.md; Paired JSON/Markdown discovery handoff and source/version inventory. | supports | Acquisition versus reuse and deferred leads are explicit; review does not treat the curator dossier as independent scientific replication. |
| named | uv run --locked cmmmech validate data/records/pentagonite.yaml; /private/tmp/cmm-round100-pentagonite-independent/named-validation.log | supports | Independently executed named validation: one record checked, zero failed. |
| search | Independent bounded correction/retraction and duplicate searches; /private/tmp/cmm-round100-pentagonite-independent/search-observations.json; /private/tmp/cmm-round100-pentagonite-independent/dedup.json | context_only | No affecting formal notice surfaced in the returned search sets. Related studies and neighboring identities are not duplicate owners; inspected source inconsistencies remain explicit. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 status definitions and exact pentagonite row, PDF p168 visually inspected. | supports | A/1971-039 and CaV4+OSi4O10(H2O)3·H2O verified independently; no criticality interpretation. |
| staples | https://msaweb.org/AmMin/AM58/AM58_405.pdf; Original pp405-411, especially p407 composition/water inference visually inspected. | supports | Oregon natural pentagonite small crystal XRF is semiquantitative; water content inferred with unit-cell/structural comparison. Not an independent quantitative water assay. |
| evans | https://msaweb.org/AmMin/AM58/AM58_412.pdf; Original structure paper pp415-416 and pp419-422; topology Fig3 p420 visually inspected. | supports | Six-membered silicate rings distinguish pentagonite from cavansite four/eight-membered topology. Same original Oregon investigation, not independent experimental replication. |
| ishida | https://doi.org/10.2465/jmps.070724b; Complete12p original; methods pp242-244, results245-248, Table1, Figures1-3/5/6; claim-bearing figures visually inspected. | supports | Natural Wagholi air-heating dehydration, terminal amorphization and ESR interpretation checked; hydrous species and oxidation completeness are inferences. |
| danisi | https://iris.unimore.it/retrieve/e31e124c-953d-987f-e053-3705fe0a095a/Revised_version.pdf; 45p accepted manuscript with cover and appended graphics/supplements; methods pp5-10, results14-17; Tables1B/3A/3B/S7, Fig4 visually inspected. | supports | Two powder media and separate single crystal retain distinct pressure, hydration and damage behavior. Accepted version is explicitly identified; final publisher version not verified. |
| ottens | https://doi.org/10.3390/min15020126; Complete27p original; abstract, methods p5, geological interpretation pp18-24 and conclusion. | context_only | Only calcite yielded usable fluid inclusions; pressure 0.01-0.03 GPa in the abstract differs from 0.1-0.3 conclusion. Neither is a direct pentagonite formation measurement. |
| batch | /private/tmp/cmm-round100-final-gates.json; Completed coordinator receipt; /private/tmp/cmm-round100-final-gates.log SHA256 1d26fc881828a6ce668c84c6458674b6be8a6af044068c144323a7200677e32d | supports | All four terminal exit codes are zero and recorded owners unchanged. just check, strict corpus validation, trusted-base history and rendered-page freshness passed. This review bundle is subsequently validated and saved through the native helper. |

## Limits And Additional Notes

- Final publisher 2015 version and separate 2013 dehydration full text were not verified; the complete accepted 2015 manuscript is explicitly version-scoped.
- 2025 separate supplement not inspected; no supplemental morphology/twinning claim is imported.
- No independent structural re-refinement, evolved-gas analysis or complete hydration mass balance. V4+ ESR does not exclude ESR-silent V5+.
- Natural formation estimates remain inferential and internally inconsistent in pressure; abiotic laboratory observations do not establish microbial activity, extraction or deployment.
- Final assessment drafting timestamps are actual; preliminary independent source inspection and native capture preceded this drafting interval.
- Primary artifacts were acquired by the curator or reused from prior acquisition and independently inspected here; current accession requests for seawater and the IMA download used for mineral authority were independently checked. No independent experimental replication is claimed.
- Whole-corpus gates are coordinator executions, verified from actual completed receipt/log. The native review corpus check follows persistence; no future check is represented as already run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T184520Z-pentagonite-round100-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Pentagonite
started_at: '2026-10-15T18:39:56.124306Z'
finished_at: '2026-10-15T18:45:20.430522Z'
reviewer:
  identity: codex /root/round100_vanadium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The pentagonite-lane agent authored this owner. I curated separate
    goldmanite/haradaite records and independently inspected this exact frozen owner
    and primary evidence without editing its record, history or source dossier.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Distinct mineral identity and source-scoped abiotic thermal/pressure observations
  are supported, with explicit hydration, specimen and reversibility limits.
source:
  git_revision: b6831c1da19b475ea048baea4ba5c10b96d678af
  state: working_tree
  inputs:
  - path: data/records/pentagonite.yaml
    sha256: b9df9885b6850d0e03cf5d30220e806e060b618fe07166804574a375598235ed
    role: target
  - path: history/records/pentagonite/2026-10-15T182725Z-codex-20b0ae.yaml
    sha256: ff5a23622c5220c496cdedd8832fd73cdea4698a8d3075376ac53f3837b6c845
    role: context
  - path: research/sources/round100-pentagonite/20261015T182949Z.json
    sha256: 354884418c32ce647f0324862d591df8159b4abe6fff3b76046e4b15e19a422f
    role: context
  - path: research/sources/round100-pentagonite/20261015T182949Z.md
    sha256: e981c5779d0e92a476b13ece20108bb23e7e2ffe9c1aee36f5404de1126fdd6d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire frozen maintained record, canonical CREATE and inline provenance,
    dated identifiers, complete accessible claim-bearing original methods/results
    and relevant figures/tables/supplement, source dossier, and bounded counterevidence
    and duplicate searches.
  selection: Parent-assigned independent review after author freeze.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pentagonite
targets:
- target_id: cmmmech:pentagonite
  path: data/records/pentagonite.yaml
  label: Pentagonite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pentagonite.yaml
    role: maintained_record
checks:
- check_id: science
  name: Independent primary-evidence assessment
  required: true
  status: passed
  summary: Exact owner and claim-bearing primary evidence independently assessed;
    preserved uncertainties are recorded below.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - history
  - search
- check_id: named
  name: Independent named record validation
  required: true
  status: passed
  command: uv run --locked cmmmech validate data/records/pentagonite.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record; 0 failed.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - named
- check_id: batch1
  name: Completed coordinator batch check 1
  required: true
  status: passed
  command: just check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual completed receipt, unchanged reviewed owner and complete
    log hash. This is coordinator execution, not an independently rerun suite.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed coordinator batch check 2
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual completed receipt, unchanged reviewed owner and complete
    log hash. This is coordinator execution, not an independently rerun suite.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed coordinator batch check 3
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base b6831c1da19b475ea048baea4ba5c10b96d678af
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual completed receipt, unchanged reviewed owner and complete
    log hash. This is coordinator execution, not an independently rerun suite.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - batch
- check_id: batch4
  name: Completed coordinator batch check 4
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Verified actual completed receipt, unchanged reviewed owner and complete
    log hash. This is coordinator execution, not an independently rerun suite.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/pentagonite.yaml
  locator: Entire exact owner captured with native inspect before judging; frozen
    hash verified again before review drafting.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Identity, conditions, outcomes and caveats match the independently assessed
    scope.
  snapshot_sha256: b9df9885b6850d0e03cf5d30220e806e060b618fe07166804574a375598235ed
- evidence_id: history
  kind: record_content
  reference: history/records/pentagonite/2026-10-15T182725Z-codex-20b0ae.yaml
  locator: Complete canonical CREATE and distinct inline event/history_refs.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Actual GPT-6 curator metadata, target and described changes agree. No earlier
    authorship invented.
  snapshot_sha256: ff5a23622c5220c496cdedd8832fd73cdea4698a8d3075376ac53f3837b6c845
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round100-pentagonite/20261015T182949Z.md
  locator: Paired JSON/Markdown discovery handoff and source/version inventory.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Acquisition versus reuse and deferred leads are explicit; review does not
    treat the curator dossier as independent scientific replication.
  snapshot_sha256: e981c5779d0e92a476b13ece20108bb23e7e2ffe9c1aee36f5404de1126fdd6d
- evidence_id: named
  kind: validation
  reference: uv run --locked cmmmech validate data/records/pentagonite.yaml
  locator: /private/tmp/cmm-round100-pentagonite-independent/named-validation.log
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: 'Independently executed named validation: one record checked, zero failed.'
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: search
  kind: search
  reference: Independent bounded correction/retraction and duplicate searches
  locator: /private/tmp/cmm-round100-pentagonite-independent/search-observations.json;
    /private/tmp/cmm-round100-pentagonite-independent/dedup.json
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: context_only
  summary: No affecting formal notice surfaced in the returned search sets. Related
    studies and neighboring identities are not duplicate owners; inspected source
    inconsistencies remain explicit.
  snapshot_sha256: f76e828460274e8f343a3732348e538a14280220a4554b0690afd574fa2b7e67
  search_scope: Exact queries in receipt; rg --no-ignore --hidden --follow across
    explicitly listed maintained roots, referenced raw directories and 253 all-state
    issues. Hidden and ignored files included, symlinks followed. No machine-wide
    or exhaustive literature absence claim.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September2026 status definitions and exact pentagonite row, PDF p168 visually
    inspected.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: A/1971-039 and CaV4+OSi4O10(H2O)3·H2O verified independently; no criticality
    interpretation.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: staples
  kind: primary_source
  reference: https://msaweb.org/AmMin/AM58/AM58_405.pdf
  locator: Original pp405-411, especially p407 composition/water inference visually
    inspected.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Oregon natural pentagonite small crystal XRF is semiquantitative; water
    content inferred with unit-cell/structural comparison. Not an independent quantitative
    water assay.
  snapshot_sha256: b4c97e61c89f721d1264e2286e19dedc67aa888054e0392b245a064b59d50790
- evidence_id: evans
  kind: primary_source
  reference: https://msaweb.org/AmMin/AM58/AM58_412.pdf
  locator: Original structure paper pp415-416 and pp419-422; topology Fig3 p420 visually
    inspected.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Six-membered silicate rings distinguish pentagonite from cavansite four/eight-membered
    topology. Same original Oregon investigation, not independent experimental replication.
  snapshot_sha256: c85a0ed742c8bfeac5ddb32bbc3cf29cd6d91d7354aa1cd76c9805ecc5905920
- evidence_id: ishida
  kind: primary_source
  reference: https://doi.org/10.2465/jmps.070724b
  locator: Complete12p original; methods pp242-244, results245-248, Table1, Figures1-3/5/6;
    claim-bearing figures visually inspected.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Natural Wagholi air-heating dehydration, terminal amorphization and ESR
    interpretation checked; hydrous species and oxidation completeness are inferences.
  snapshot_sha256: c1a23a8fc6ec158b42eedc49c329aa5e336f04d131c4c017d55b1bcf8df96b02
- evidence_id: danisi
  kind: primary_source
  reference: https://iris.unimore.it/retrieve/e31e124c-953d-987f-e053-3705fe0a095a/Revised_version.pdf
  locator: 45p accepted manuscript with cover and appended graphics/supplements; methods
    pp5-10, results14-17; Tables1B/3A/3B/S7, Fig4 visually inspected.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: supports
  summary: Two powder media and separate single crystal retain distinct pressure,
    hydration and damage behavior. Accepted version is explicitly identified; final
    publisher version not verified.
  snapshot_sha256: 2c38213aab2c93e48c617f48e80e20b4d8bca78f93ad302110d808cf502f099a
- evidence_id: ottens
  kind: primary_source
  reference: https://doi.org/10.3390/min15020126
  locator: Complete27p original; abstract, methods p5, geological interpretation pp18-24
    and conclusion.
  accessed_at: '2026-10-15T18:42:27.289046Z'
  support: context_only
  summary: Only calcite yielded usable fluid inclusions; pressure 0.01-0.03 GPa in
    the abstract differs from 0.1-0.3 conclusion. Neither is a direct pentagonite
    formation measurement.
  snapshot_sha256: 2a698373f43c30a0b0a376bf50ac92407601e63ffa0a686ab8296db10895c3a5
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round100-final-gates.json
  locator: Completed coordinator receipt; /private/tmp/cmm-round100-final-gates.log
    SHA256 1d26fc881828a6ce668c84c6458674b6be8a6af044068c144323a7200677e32d
  accessed_at: '2026-10-15T18:45:20.430522Z'
  support: supports
  summary: All four terminal exit codes are zero and recorded owners unchanged. just
    check, strict corpus validation, trusted-base history and rendered-page freshness
    passed. This review bundle is subsequently validated and saved through the native
    helper.
  snapshot_sha256: 3a6f970f9a5bb1e442804dd5529b6eb0acfdcb76a9311cda62204cf368c6b939
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct dated mineral identity
  outcome: supported
  summary: Pentagonite mineral identity and topology are supported.
  details: IMA 1971-039 is approved species status, not criticality. Ambient Ccm21
    in original and later structures; distinct from cavansite despite shared nominal
    composition. Oregon and Wagholi specimens are not one material aliquot. Original
    semiquantitative composition and inferred water do not override current ideal
    formula.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - ima
  - staples
  - evans
  - ishida
- assessment_id: heating
  area: evidence
  topic: Protocol-specific thermal observation
  outcome: supported
  summary: The record preserves measured mass/diffraction outcomes without universalizing
    temperatures.
  details: About 10 mg open-Pt powder TG-DTA in air at 10 C/min to 900 C; separate
    HT-XRPD at20/260/550/700 C and cooled quartz-mounted aliquot from 550 C.16.07
    wt% water-assigned loss and95/220/280 C events agree with Figure 1/Table 1;1.73
    wt% gain near 600 C supports authors oxidation interpretation. Figure 5 retained
    diffraction after550 C cooling versus amorphous at 700 C; not proof of complete
    water regain or cavansite conversion. ESR-silent V5+ cannot be excluded from room-temperature
    spectra alone.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - ishida
- assessment_id: pressure
  area: scope
  topic: Separate powder media and single crystal
  outcome: supported
  summary: Conditions and pressure transition brackets match tables.
  details: Powder to 8.26(5) GPa m.e.w. 16:3:1 and 8.35(5) oil; orthorhombic/triclinic
    brackets2.45-2.96 and1.27-1.71 GPa agree with Tables 3A/B. Both powder rows return
    orthorhombic at ambient release. Oil poor/nonhydrostatic above~1 GPa qualifies
    comparison. Separate apparently untwinned crystal is 170 x 140 x 60 micrometres,
    despite Table 1B mm heading; irreversibly damaged/unindexable above~2.5 GPa.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - danisi
- assessment_id: hydration
  area: quantity
  topic: Modeled water and reversibility
  outcome: supported
  summary: Additional modeled oxygen is not an independent water balance.
  details: O10 occupancies 0.94(3)/0.96(3) at 1.51(5)/2.04(5) GPa qualify ideal five-water
    Table 1B formulas. Disordered O9/O10, grouped displacement parameters and restraints
    remain explicit. Triclinic atomic structure unrefined. Powder cell symmetry reversibility
    neither proves complete water reversibility nor negates single-crystal damage.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - danisi
- assessment_id: counterevidence
  area: consistency
  topic: Natural formation versus laboratory heating
  outcome: supported
  summary: Later geological interpretation is retained at the supported evidentiary
    scope.
  details: Ishida intermediate-amorphous phrase is qualified without falsely contradicting
    terminal amorphization. Ottens challenges high-temperature natural formation using
    paragenesis; methods yielded usable fluid-inclusion data only for calcite. Internal
    pressure discrepancy remains unresolved. No measured pentagonite crystallization
    threshold imported from either source.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - ishida
  - ottens
- assessment_id: criticality
  area: scope
  topic: Biological, recovery and authority scope
  outcome: supported
  summary: No unsupported biological or industrial transfer.
  details: Both mechanisms are explicitly abiotic, processother, microbialfalse with
    no organism. No constituent criticality designation, vanadium extraction/recovered-product
    yield or industrial deployment inferred.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - ima
  - ishida
  - danisi
- assessment_id: provenance
  area: provenance
  topic: Exact frozen revision and history
  outcome: supported
  summary: Working-tree provenance and independent review are explicit.
  details: Native inspect preceded judgment and exact source/owner/history hashes
    were rechecked. Canonical CREATE and inline history are distinct; actual GPT-6
    metadata retained. Named validation independently executed; coordinator whole-corpus
    gates were added only after actual terminal receipt, base, log and unchanged target
    hashes were verified.
  target_ids:
  - cmmmech:pentagonite
  evidence_ids:
  - owner
  - history
  - dossier
  - named
  - batch
findings: []
actions: []
limitations:
- Final publisher 2015 version and separate 2013 dehydration full text were not verified;
  the complete accepted 2015 manuscript is explicitly version-scoped.
- 2025 separate supplement not inspected; no supplemental morphology/twinning claim
  is imported.
- No independent structural re-refinement, evolved-gas analysis or complete hydration
  mass balance. V4+ ESR does not exclude ESR-silent V5+.
- Natural formation estimates remain inferential and internally inconsistent in pressure;
  abiotic laboratory observations do not establish microbial activity, extraction
  or deployment.
notes:
- Final assessment drafting timestamps are actual; preliminary independent source
  inspection and native capture preceded this drafting interval.
- Primary artifacts were acquired by the curator or reused from prior acquisition
  and independently inspected here; current accession requests for seawater and the
  IMA download used for mineral authority were independently checked. No independent
  experimental replication is claimed.
- Whole-corpus gates are coordinator executions, verified from actual completed receipt/log.
  The native review corpus check follows persistence; no future check is represented
  as already run.
```
