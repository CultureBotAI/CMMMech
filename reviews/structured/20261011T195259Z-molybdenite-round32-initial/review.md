# Independent molybdenite review: temporal wording ambiguity

- Review: 20261011T195259Z-molybdenite-round32-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T19:49:59Z
- Finished UTC: 2026-10-11T19:52:59.266455Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The controlled limited-leaching result and mineral/feed boundaries are supported. One minor wording finding overstates a temporally ambiguous source sentence as a definite contradiction. Named validation passed; final batch receipts pending. Correct wording and save an exact-hash successor.

## Scope And Provenance

Every field of one frozen molybdenite record and CREATE provenance, checked against original primary/SI, authority identities, controls, numerical bases and deployment limits.

Selection: Assigned round32 record curated by a different agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 09c15cbfb7699e40ae4648b6b414784a00b488db.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:molybdenite | data/records/molybdenite.yaml | maintained | Molybdenite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:molybdenite | Reviewer executed; 1 checked,0 failed. /private/tmp/cmm-round32-molybdenite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Required batch gate | unavailable | True | cmmmech:molybdenite | Final parent-coordinated cohort receipt pending at this initial finding; no success inferred. |
| Required nonempty gate | unavailable | True | cmmmech:molybdenite | Final parent-coordinated cohort receipt pending at this initial finding; no success inferred. |
| Required history gate | unavailable | True | cmmmech:molybdenite | Final parent-coordinated cohort receipt pending at this initial finding; no success inferred. |

## Scientific And Domain Assessments

### Mineral, mixed feed, organism and criticality boundaries

identity: supported. Targets: cmmmech:molybdenite.

Mineral root is supported while the experiment explicitly remains a low-Mo mixed specimen. No criticality transfer or strain accession is invented.

### Controls, conditions and original assay distinctions

evidence: supported. Targets: cmmmech:molybdenite.

Retained method quantities and controls match primary. Unknown flask replication, cell density, full medium, initial pH and dynamic pH matching remain explicit. Ferric sulfate versus FeIII addition basis is genuinely ambiguous.

### Null Mo, detection boundary and qualitative phases

quantity: supported. Targets: cmmmech:molybdenite.

Below2mg/L is censored supernatant concentration, not zero or recovered fraction. XRD companion-phase loss is qualitative.43-day SI is abiotic only; missing final biotic data and unmeasured galvanic mechanism remain limited.

### Temporal ambiguity versus definite contradiction

scope: concern. Targets: cmmmech:molybdenite.

One minor wording overstatement remains: the source sentence may describe no further changes after22days, whereas the record labels a definite contradiction with the22day residue interpretation.

### Exact working bytes, actual sources and pending cohort gates

provenance: supported. Targets: cmmmech:molybdenite.

Native inspect preceded judgment. A second capture corrected target metadata kind/repository only with identical scientific hashes. Source identity and append-only CREATE provenance are supported. Final batch checks are unavailable at this initial partial observation.

## Findings

### F1: Preserve temporal ambiguity instead of asserting a definite source contradiction

minor / open / confirmed; issue key: CMMMech.molybdenite.temporal-wording-contradiction.

The evidence explanation calls p1098 a conflict with Figure6. Portuguese "após esse período" can instead refer to no further mineralogical changes beyond day22, consistent with earlier iron-sulfide loss. Retain both temporal readings or the ambiguity and do not assert that the source definitely contradicts its22day result.

## Recommended Actions And Acceptance Checks

### A1

Replace definite-contradiction language with explicit temporal ambiguity; append actual EDIT sidecar and inline event. Preserve original dossier and initial review; add a short correction dossier.

- Source p1098 read in context; no-change-from-start is not asserted as the only reading.
- Mo censoring, phase interpretation and43-day missing-biotic-data boundaries remain unchanged.
- Corrected record and append-only history validate; final cohort receipts and exact-hash successor explicitly resolve this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/molybdenite.yaml; Every field, one mechanism and inline CREATE event | supports | The record correctly separates mineral identity, mixed natural specimen and controlled low-Mo result; one sentence calls a temporally ambiguous source statement a definite contradiction. |
| primary | https://doi.org/10.1590/S0100-40422007000500008; Complete main article pp1095-1099, all six original figures; independently read Portuguese methods/results and rendered original pages | supports | Source confirms Ward natural ore-grade specimen, 0.8 wt% Mo/34.0 wt% Fe/23.0 wt% S, &lt;0.2 mm, LR provenance, 150 mL medium/250 mL flasks, 2.5% w/v ore, 120 C 30 min, 5% inoculum, 30 +/-2 C, 150 rpm, biotic plus/minus FeII and uninoculated controls. All liquid Mo below 2 mg/L; Fe and XRD support conditional companion-phase removal. Resting-cell triplicate respiration is a separate assay, not flask replication or molybdenite-specific metabolism. Later biotic XRD is explicitly not shown. No mass balance or product yield is established. |
| temporal | https://doi.org/10.1590/S0100-40422007000500008; Printed p1098, Análise da fase sólida, first paragraph and Figure6; original page4 independently viewed | refutes | After referring to patterns at 22 days, the Portuguese sentence says that after that period no mineralogical changes occurred in inoculated samples. It can refer to no further changes beyond day22, consistent with earlier companion-phase loss, rather than claiming no change from initial feed. The record should preserve the temporal ambiguity instead of asserting a definite contradiction. |
| supplement | https://repositorio.unesp.br/server/api/core/bitstreams/4a0fec08-6d23-49aa-b365-0eff66bd691f/content; Original appended S1 page, both Figures1S and2S; rendered page6 independently inspected | supports | Figure2S is explicitly 43-day uninoculated controls without iron, with FeII and with FeIII. It supports retained molybdenite in those controls and does not supply missing final inoculated patterns. Figure1S is heterogeneous-specimen respiration; no molybdenite-specific kinetic constants are adopted. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 master-list original page146 and field definitions pages1-2 | supports | Molybdenite row has MoS2, G and1796; G and year denote grandfathered mineral/original description. Same-day retained authority acquisition is disclosed, not a fresh retrieval. Species does not identify elemental Mo, dissolved molybdate or manufactured MoS2. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Official NCBI species page independently opened in this round and identical retained HTML read | supports | NCBITaxon920 resolves Acidithiobacillus ferrooxidans at species rank; it does not authenticate LR or equate it to the type strain. |
| metadata | /private/tmp/cmm-round32-molybdenite-research/raw/quimicanova2007-crossref.json; Retained Crossref works metadata and publisher primary front page | supports | DOI, title, authors, journal and pages match. Year2007 is supported; publisher online July2 versus Crossref October is not converted into a falsely reconciled day. Empty relation/no update-to is bounded metadata, not a global notice guarantee. |
| search | /private/tmp/cmm-round32-molybdenite-independent/notices-search.json; Independent exact-DOI notices query and molybdenite/Nasernejad counterevidence query | supports | No affecting notice was identified in returned results. The primary itself cites contrasting extraction under different procedures; later publisher abstracts confirm condition-specific performance. No unacquired full study or abstract-only numerical comparison is promoted into the record. |
| dedup | /private/tmp/cmm-round32-molybdenite-independent/dedup-current.json; Current scientific-tree hidden/ignored/symlink-inclusive search and curator wider raw inventory boundaries | supports | Current molybdenum element record excludes molybdenite; black-shale record excludes its separate concentrate arm. The new mineral is not a duplicate of those materials; source mirrors/SI represent one experiment. Curator wider prior raw search retained rather than claimed as independently rerun. |
| history | history/records/molybdenite/2026-10-11T194752Z-codex-f27d24.yaml; Complete CREATE sidecar and separate inline timestamp | supports | Actual codex/GPT-6/codex authorship and exact target are recorded. Canonical and inline events are distinct; independent review and parent gates were pending, not retrospectively invented. |

## Limits And Additional Notes

- Required final batch/nonempty/history gates pending, so this is partial rather than acceptance.
- Original source omits flask replication, inoculum density/washing, full medium recipe and matched dynamic-pH controls.
- 43-day inoculated XRD is reported as data not shown; qualitative phase absence is not complete mineral mass balance.
- Notice/counterevidence queries are bounded; unacquired later primary methods remain deferred.
- Working-tree attestation does not imply committed bytes.
- The wording correction concerns maintained source interpretation, not a request to repair or invent primary measurements.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T195259Z-molybdenite-round32-initial
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent molybdenite review: temporal wording ambiguity'
started_at: '2026-10-11T19:49:59Z'
finished_at: '2026-10-11T19:52:59.266455Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record/history/dossier authored by round27_superalloy. Reviewer
    authored separate arsenopyrite, excluded from this verdict. Shared acquisition
    artifacts are disclosed; reviewer independently read full primary Portuguese text,
    original graphics/SI and identity sources after native inspect. No molybdenite
    maintained edit made.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The controlled limited-leaching result and mineral/feed boundaries are supported.
  One minor wording finding overstates a temporally ambiguous source sentence as a
  definite contradiction. Named validation passed; final batch receipts pending. Correct
  wording and save an exact-hash successor.
source:
  git_revision: 09c15cbfb7699e40ae4648b6b414784a00b488db
  state: working_tree
  inputs:
  - path: data/records/molybdenite.yaml
    sha256: 1fcf52ffb9a97856e1cb92358755f86801d9741dd2493a9c3a8e499a94884a3a
    role: target
  - path: history/records/molybdenite/2026-10-11T194752Z-codex-f27d24.yaml
    sha256: 83c28c85d96658de53ea2b1bffffe8f98a92199716b68e12bc844cdcdac9b180
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every field of one frozen molybdenite record and CREATE provenance,
    checked against original primary/SI, authority identities, controls, numerical
    bases and deployment limits.
  selection: Assigned round32 record curated by a different agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:molybdenite
  exclusions:
  - target: Other cohort records and unacquired later molybdenite experiments
    reason: Reviewer-authored arsenopyrite excluded; no raw instrumental reprocessing
      or abstract-only later numerical curation.
targets:
- target_id: cmmmech:molybdenite
  path: data/records/molybdenite.yaml
  label: Molybdenite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked
    cmmmech validate data/records/molybdenite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed; 1 checked,0 failed. /private/tmp/cmm-round32-molybdenite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:molybdenite
- check_id: batch
  name: Required batch gate
  command: just check
  status: unavailable
  required: true
  summary: Final parent-coordinated cohort receipt pending at this initial finding;
    no success inferred.
  target_ids:
  - cmmmech:molybdenite
- check_id: nonempty
  name: Required nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: unavailable
  required: true
  summary: Final parent-coordinated cohort receipt pending at this initial finding;
    no success inferred.
  target_ids:
  - cmmmech:molybdenite
- check_id: history
  name: Required history gate
  command: uv run --locked cmmmech validate-history --base 09c15cbfb7699e40ae4648b6b414784a00b488db
  status: unavailable
  required: true
  summary: Final parent-coordinated cohort receipt pending at this initial finding;
    no success inferred.
  target_ids:
  - cmmmech:molybdenite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/molybdenite.yaml
  locator: Every field, one mechanism and inline CREATE event
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: The record correctly separates mineral identity, mixed natural specimen
    and controlled low-Mo result; one sentence calls a temporally ambiguous source
    statement a definite contradiction.
  snapshot_sha256: 1fcf52ffb9a97856e1cb92358755f86801d9741dd2493a9c3a8e499a94884a3a
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1590/S0100-40422007000500008
  locator: Complete main article pp1095-1099, all six original figures; independently
    read Portuguese methods/results and rendered original pages
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: Source confirms Ward natural ore-grade specimen, 0.8 wt% Mo/34.0 wt% Fe/23.0
    wt% S, <0.2 mm, LR provenance, 150 mL medium/250 mL flasks, 2.5% w/v ore, 120
    C 30 min, 5% inoculum, 30 +/-2 C, 150 rpm, biotic plus/minus FeII and uninoculated
    controls. All liquid Mo below 2 mg/L; Fe and XRD support conditional companion-phase
    removal. Resting-cell triplicate respiration is a separate assay, not flask replication
    or molybdenite-specific metabolism. Later biotic XRD is explicitly not shown.
    No mass balance or product yield is established.
  snapshot_sha256: dbab73ee9ceaaf8648c94e79fe5b8007d79d1b5acf394c5917113cb16a6655db
- evidence_id: temporal
  kind: primary_source
  reference: https://doi.org/10.1590/S0100-40422007000500008
  locator: Printed p1098, Análise da fase sólida, first paragraph and Figure6; original
    page4 independently viewed
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: refutes
  summary: After referring to patterns at 22 days, the Portuguese sentence says that
    after that period no mineralogical changes occurred in inoculated samples. It
    can refer to no further changes beyond day22, consistent with earlier companion-phase
    loss, rather than claiming no change from initial feed. The record should preserve
    the temporal ambiguity instead of asserting a definite contradiction.
  snapshot_sha256: a9704a1e875a757af07692f045cbdc7f33c9f8c753b703dc125358c5a2eeee69
- evidence_id: supplement
  kind: primary_source
  reference: https://repositorio.unesp.br/server/api/core/bitstreams/4a0fec08-6d23-49aa-b365-0eff66bd691f/content
  locator: Original appended S1 page, both Figures1S and2S; rendered page6 independently
    inspected
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: Figure2S is explicitly 43-day uninoculated controls without iron, with
    FeII and with FeIII. It supports retained molybdenite in those controls and does
    not supply missing final inoculated patterns. Figure1S is heterogeneous-specimen
    respiration; no molybdenite-specific kinetic constants are adopted.
  snapshot_sha256: dbab73ee9ceaaf8648c94e79fe5b8007d79d1b5acf394c5917113cb16a6655db
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September2026 master-list original page146 and field definitions pages1-2
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: Molybdenite row has MoS2, G and1796; G and year denote grandfathered mineral/original
    description. Same-day retained authority acquisition is disclosed, not a fresh
    retrieval. Species does not identify elemental Mo, dissolved molybdate or manufactured
    MoS2.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Official NCBI species page independently opened in this round and identical
    retained HTML read
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: NCBITaxon920 resolves Acidithiobacillus ferrooxidans at species rank; it
    does not authenticate LR or equate it to the type strain.
  snapshot_sha256: c6d264e2f6ed730350be86773d9564c7427f7f089b57ed566d6494e3bd21a4ac
- evidence_id: metadata
  kind: database
  reference: /private/tmp/cmm-round32-molybdenite-research/raw/quimicanova2007-crossref.json
  locator: Retained Crossref works metadata and publisher primary front page
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: DOI, title, authors, journal and pages match. Year2007 is supported; publisher
    online July2 versus Crossref October is not converted into a falsely reconciled
    day. Empty relation/no update-to is bounded metadata, not a global notice guarantee.
  snapshot_sha256: f9256fff2959570fe7ec4b1930f508ec5db775484ff483a75ac0e568e36e5323
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round32-molybdenite-independent/notices-search.json
  locator: Independent exact-DOI notices query and molybdenite/Nasernejad counterevidence
    query
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: No affecting notice was identified in returned results. The primary itself
    cites contrasting extraction under different procedures; later publisher abstracts
    confirm condition-specific performance. No unacquired full study or abstract-only
    numerical comparison is promoted into the record.
  snapshot_sha256: 533bf2e33ba68d9752a0396f91d050cbd97962a7f97bed981b7a2690d764d285
  search_scope: 11October2026 first returned web results for "10.1590/S0100-40422007000500008"
    correction OR erratum OR retraction; "molybdenite" "Nasernejad" "93" bioleaching.
    No filters or exhaustive pagination; full later primary methods not inspected.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round32-molybdenite-independent/dedup-current.json
  locator: Current scientific-tree hidden/ignored/symlink-inclusive search and curator
    wider raw inventory boundaries
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: Current molybdenum element record excludes molybdenite; black-shale record
    excludes its separate concentrate arm. The new mineral is not a duplicate of those
    materials; source mirrors/SI represent one experiment. Curator wider prior raw
    search retained rather than claimed as independently rerun.
  snapshot_sha256: 81d19e89a1834986f78739af82eb8b1318a3756b265b365695895b974f7e42c3
  search_scope: Current data/records,research,reviews,history searched with rg --hidden
    --no-ignore --follow;208matching lines. Curator declared prior original/raw coverage
    inspected separately. No machine-wide absence assertion.
- evidence_id: history
  kind: record_content
  reference: history/records/molybdenite/2026-10-11T194752Z-codex-f27d24.yaml
  locator: Complete CREATE sidecar and separate inline timestamp
  accessed_at: '2026-10-11T19:52:59.266455Z'
  support: supports
  summary: Actual codex/GPT-6/codex authorship and exact target are recorded. Canonical
    and inline events are distinct; independent review and parent gates were pending,
    not retrospectively invented.
  snapshot_sha256: 83c28c85d96658de53ea2b1bffffe8f98a92199716b68e12bc844cdcdac9b180
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral, mixed feed, organism and criticality boundaries
  outcome: supported
  summary: Mineral root is supported while the experiment explicitly remains a low-Mo
    mixed specimen. No criticality transfer or strain accession is invented.
  target_ids:
  - cmmmech:molybdenite
  evidence_ids:
  - record
  - primary
  - ima
  - taxon
  - dedup
  dimensions:
  - name: material_form
    value: Natural MoS2 mineral within heterogeneous commercial ore-grade feed
    definition: 0.8wt%Mo does not imply pure molybdenite; supplier location is not
      mine origin.
    evidence_ids:
    - primary
    - ima
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim needs reconciliation because none
      is made.
    evidence_ids:
    - record
  - name: organism
    value: Source-assigned A. ferrooxidans LR; NCBITaxon920 species mapping
    definition: Living adapted flask culture; separate washed non-growing respiration
      assay does not fill flask metadata.
    evidence_ids:
    - primary
    - taxon
- assessment_id: methods
  area: evidence
  topic: Controls, conditions and original assay distinctions
  outcome: supported
  summary: Retained method quantities and controls match primary. Unknown flask replication,
    cell density, full medium, initial pH and dynamic pH matching remain explicit.
    Ferric sulfate versus FeIII addition basis is genuinely ambiguous.
  target_ids:
  - cmmmech:molybdenite
  evidence_ids:
  - record
  - primary
  - supplement
- assessment_id: quantity
  area: quantity
  topic: Null Mo, detection boundary and qualitative phases
  outcome: supported
  summary: Below2mg/L is censored supernatant concentration, not zero or recovered
    fraction. XRD companion-phase loss is qualitative.43-day SI is abiotic only; missing
    final biotic data and unmeasured galvanic mechanism remain limited.
  target_ids:
  - cmmmech:molybdenite
  evidence_ids:
  - record
  - primary
  - supplement
- assessment_id: wording
  area: scope
  topic: Temporal ambiguity versus definite contradiction
  outcome: concern
  summary: 'One minor wording overstatement remains: the source sentence may describe
    no further changes after22days, whereas the record labels a definite contradiction
    with the22day residue interpretation.'
  target_ids:
  - cmmmech:molybdenite
  evidence_ids:
  - record
  - temporal
  - primary
- assessment_id: provenance
  area: provenance
  topic: Exact working bytes, actual sources and pending cohort gates
  outcome: supported
  summary: Native inspect preceded judgment. A second capture corrected target metadata
    kind/repository only with identical scientific hashes. Source identity and append-only
    CREATE provenance are supported. Final batch checks are unavailable at this initial
    partial observation.
  target_ids:
  - cmmmech:molybdenite
  evidence_ids:
  - record
  - history
  - metadata
  - search
findings:
- finding_id: F1
  issue_key: CMMMech.molybdenite.temporal-wording-contradiction
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve temporal ambiguity instead of asserting a definite source contradiction
  description: The evidence explanation calls p1098 a conflict with Figure6. Portuguese
    "após esse período" can instead refer to no further mineralogical changes beyond
    day22, consistent with earlier iron-sulfide loss. Retain both temporal readings
    or the ambiguity and do not assert that the source definitely contradicts its22day
    result.
  target_ids:
  - cmmmech:molybdenite
  field_paths:
  - mechanisms[id=lr_mixed_specimen_leaching_limit].evidence[2].explanation
  evidence_ids:
  - record
  - temporal
  - primary
  rule_id: preserve-source-ambiguity
  native_severity: minor
  normalization_reason: Bounded interpretation wording; mineral identity, censored
    Mo observation and quantitative limits remain supported.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenite.yaml
    role: maintained_record
actions:
- action_id: A1
  description: Replace definite-contradiction language with explicit temporal ambiguity;
    append actual EDIT sidecar and inline event. Preserve original dossier and initial
    review; add a short correction dossier.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:molybdenite
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/molybdenite.yaml
    role: maintained_record
  acceptance_checks:
  - Source p1098 read in context; no-change-from-start is not asserted as the only
    reading.
  - Mo censoring, phase interpretation and43-day missing-biotic-data boundaries remain
    unchanged.
  - Corrected record and append-only history validate; final cohort receipts and exact-hash
    successor explicitly resolve this finding.
limitations:
- Required final batch/nonempty/history gates pending, so this is partial rather than
  acceptance.
- Original source omits flask replication, inoculum density/washing, full medium recipe
  and matched dynamic-pH controls.
- 43-day inoculated XRD is reported as data not shown; qualitative phase absence is
  not complete mineral mass balance.
- Notice/counterevidence queries are bounded; unacquired later primary methods remain
  deferred.
- Working-tree attestation does not imply committed bytes.
notes:
- The wording correction concerns maintained source interpretation, not a request
  to repair or invent primary measurements.
tags:
- round32
- independent
- molybdenite
- initial-finding
```
