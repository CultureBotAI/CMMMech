# Independent scientific review of Hematite

- Review: 20261011T112045Z-hematite-round18-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T11:16:02Z
- Finished UTC: 2026-10-11T11:20:45Z
- Reviewer: Codex /root/round18_catalyst (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The material identity and narrow assay observation are supported. Source uncertainties are explicitly preserved; no actionable defect was identified in the reviewed record.

## Scope And Provenance

Full scientific and provenance review of this frozen new record, associated CREATE sidecar and relevant primary/authority evidence.

Selection: One assigned new record; all fields read and evaluated.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 26cb0688effb2f71e4a570c416f6f43ff858c5ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:hematite | data/records/hematite.yaml | maintained | Hematite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:hematite | Reviewer executed to terminal exit 0 at 2026-10-11T11:17:06.634566Z: 2 records, 0 failed. Final captured record hashes rechecked unchanged. |
| Native full checks | passed | True | cmmmech:hematite | Parent executed; reviewer independently read finished receipt and actual terminal log. /private/tmp/cmm-round18-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 86.49s (0:01:26)<br>Checked 138 record(s); 0 failed.<br>Checked 154 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:hematite | Parent executed; reviewer independently read finished receipt and actual terminal log. /private/tmp/cmm-round18-final-require.log: Checked 138 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:hematite | Parent executed; reviewer independently read finished receipt and actual terminal log. /private/tmp/cmm-round18-final-history.log: Checked 154 history record(s); 0 error(s).<br> |
| Independent interim trusted-base history check | passed | False | cmmmech:hematite | Reviewer executed to terminal exit 0 at 2026-10-11T11:17:13.626426Z: 152 histories, 0 errors. This interim count preceded completion of the six-record batch; final parent receipt above is 154 histories. |

## Scientific And Domain Assessments

### Material identity, feed and criticality boundaries

identity: supported. Targets: cmmmech:hematite.

Hematite is an approved mineral species, Fe2O3; bulk oxide composition of the tested feed does not establish phase purity.

### Assay-specific microbial mobilization and limits

evidence: supported. Targets: cmmmech:hematite.

Matched uninoculated controls support a culture-associated filtered-element increase. Acidification, expression correlations and cross-feed observations are bounded, with no isolated recovery yield or deployment claim.

### Actual CREATE session and exact reviewed bytes

provenance: supported. Targets: cmmmech:hematite.

Separate curator authored genuine codex/GPT-6 CREATE history. Canonical inspect preceded scientific assessment; final target/schema/history hashes and actual terminal checks agree.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/hematite.yaml; Complete final YAML and linked CREATE history sidecar | supports | Final file and complete sidecar independently inspected. Canonical inspect captured bytes before scientific assessment. Actor, target, actual CREATE event and sidecar agree; no material CURIE or criticality claim is inferred. |
| identity_authority | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 master list, PDF p. 92 Hematite row; pp. 1-2 definitions | supports | Retained official authority PDF text and rendered row independently inspected: Hematite, Fe2O3, approved, 1971 special procedure. The historical status notation is not an external material identifier. Iron element, hematite species and the impure commercial assay feed remain distinct. |
| primary | https://doi.org/10.1128/aem.01201-26; Retained complete Europe PMC XML: mineral weathering Methods, Results and Discussion; Figure 5; supplement methods pp. 1-2 and Tables S6/S7, rendered PDF pp. 11-12 | supports | Independent review checked organism and inoculum, 0.60 g 75-150 micrometre feed in 60 mL GMM, 0.2 mL nominal 10^8 cells/mL inoculum, triplicate sacrificial assays at 37 C/160 rpm and 12/24 h; centrifuged, 0.45 micrometre filtered ICP-OES fraction. Visually inspected Table S6 exact cells, Table S7 oxide composition and Figure 5. These data support culture-associated mobilization, without pH-matched or killed-cell controls in the selected feed assay, phase purity, oxidation-state resolution or causal gene validation. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13599522/supplementaryFiles; aem.01201-26-s0001.pdf, Tables S6/S7 and supplement Methods | supports | Table S6 Fe means ± SD, n=3, in micromolar: 25.95 ± 0.90 at 12 h and 71.43 ± 1.56 at 24 h versus 0.04 ± 0.00 controls at both times. Biological pH 4.69/4.66 versus 7.16/7.12 controls; Table S7 86.58% Fe2O3 and 9.82% SiO2 are bulk oxide analyses, not phase percentages. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1404&amp;mode=Info; Live taxonomy label/rank and retained official taxonomy XML | supports | NCBITaxon:1404 is Priestia megaterium at species rank. No strain-specific taxonomic ID is inferred. |
| strain | https://www.ncbi.nlm.nih.gov/nuccore/CM125967.1; Retained official GenBank source features retrieved with seq_start=1, seq_stop=1; comparator CM125968.1 also checked | supports | CM125967.1 source metadata identify strain PMA2-2, taxonomy 1404 and BioSample SAMN50659134. Comparator PMD1-1 is CM125968.1. This resolves the duplicated accession typo in one primary Methods paragraph consistently with Data Availability, without claiming full-genome sequence reanalysis. Browser nuccore open failed; retained official efetch feature metadata were inspected. |
| search | /private/tmp/cmm-round18-catalyst-independent/dedup.log; Independent hidden/ignored-inclusive dedup and first returned web query sets | context_only | Queries included exact DOI 10.1128/aem.01201-26 with correction/retraction/erratum and potassium feldspar NK851 controls acid protein. No applicable Dong notice surfaced in these returned sets. NK851 DOI 10.3390/ijms241814226 is a distinct potassium-release strain/assay with acid and protein-fraction comparisons, not a refutation of this narrower PMA2-2 observation; full curation remains deferred. Retained Crossref author notice check is contextual, not an independently exhaustive notice audit. |
| gates | /private/tmp/cmm-round18-gate-receipts.json; Finished receipt and /private/tmp/cmm-round18-final-{batch,require,history}.log | supports | Reviewer independently read actual terminal receipt/logs: 308 passed, 3 skipped in 86.49 s; 138 records and 154 history sessions valid. Separate nonempty and trusted-base history checks passed. The two reviewed files remain byte-identical to inspection. |

## Limits And Additional Notes

- The commercial hematite-labelled material has substantial SiO2 by bulk analysis; supplier origin, cleaning and quantitative phase purity are unspecified. No pure-hematite-normalized yield follows.
- No pH-matched or killed-cell control isolates a causal contribution beyond the culture-associated observation. Figure 5 expression responses are associational, not gene-function validation.
- Primary text contains a duplicated comparator accession and olivine magnesium-unit conflict; the relevant official strain metadata and selected Fe/Al assays avoid importing those errors. Biotite-specific mechanistic experiments are not transferred.
- Publisher and PMC live routes were unavailable or challenged in some requests; full retained Europe PMC XML, relevant downloaded supplement, rendered tables and Figure 5 were inspected. No complete genomics/metabolomics reanalysis was performed.
- Bounded notice and contrary-evidence searches cannot establish global absence. Dissolved elemental concentration is not phase-specific extraction yield, isolated product recovery or industrial deployment.
- Review interval starts at the recorded creation time of its canonical inspection target file, before scientific judgment; finished time marks final hash and terminal-receipt capture. Two independent per-record decisions share a primary paper and are not independent biological replications.
- All 34 mineral-feed dossier inventory/record hashes were independently recomputed with no discrepancy. No corrections were required; unresolved limitations remain in the record and frontier.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112045Z-hematite-round18-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Hematite
started_at: '2026-10-11T11:16:02Z'
finished_at: '2026-10-11T11:20:45Z'
reviewer:
  identity: Codex /root/round18_catalyst
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Separate /root/round18_mineral_feeds agent authored this record
    and CREATE sidecar. Reviewer independently read retained primary sources, figures
    and authority entries, checked identifiers and performed additional searches;
    made no target edits. Shared worktree disclosed. Reviewer authored the separate
    HDS record, outside this review target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The material identity and narrow assay observation are supported. Source
  uncertainties are explicitly preserved; no actionable defect was identified in the
  reviewed record.
source:
  git_revision: 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  state: working_tree
  inputs:
  - path: data/records/hematite.yaml
    sha256: c677b20cd2ead19cf7bf8b1882cfd567f55ca38ffe0bfa7c7514cfc9143c4c49
    role: target
  - path: history/records/hematite/2026-10-11T111406Z-codex-f219a6.yaml
    sha256: 90af4075d82ece6b6b8329f60f354d5ce8b6a3c160afc637ef6f8d916be74b07
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full scientific and provenance review of this frozen new record, associated
    CREATE sidecar and relevant primary/authority evidence.
  selection: One assigned new record; all fields read and evaluated.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:hematite
  exclusions:
  - target: Other maintained records, independent raw-data reanalysis and industrial
      deployment
    reason: Contextual reads do not constitute scientific review of those targets;
      no new independent experiment or genome analysis was performed.
targets:
- target_id: cmmmech:hematite
  path: data/records/hematite.yaml
  label: Hematite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/hematite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/hematite.yaml data/records/potassium-feldspar.yaml
  status: passed
  required: true
  summary: 'Reviewer executed to terminal exit 0 at 2026-10-11T11:17:06.634566Z: 2
    records, 0 failed. Final captured record hashes rechecked unchanged.'
  target_ids:
  - cmmmech:hematite
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read finished receipt and actual
    terminal log. /private/tmp/cmm-round18-final-batch.log: uv run --locked --extra
    dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 86.49s (0:01:26)

    Checked 138 record(s); 0 failed.

    Checked 154 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:hematite
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read finished receipt and actual
    terminal log. /private/tmp/cmm-round18-final-require.log: Checked 138 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:hematite
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read finished receipt and actual
    terminal log. /private/tmp/cmm-round18-final-history.log: Checked 154 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:hematite
- check_id: interim_history
  name: Independent interim trusted-base history check
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate-history --base 26cb0688effb2f71e4a570c416f6f43ff858c5ab
  status: passed
  required: false
  summary: 'Reviewer executed to terminal exit 0 at 2026-10-11T11:17:13.626426Z: 152
    histories, 0 errors. This interim count preceded completion of the six-record
    batch; final parent receipt above is 154 histories.'
  target_ids:
  - cmmmech:hematite
  exit_code: 0
  expected_exit_code: 0
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/hematite.yaml
  locator: Complete final YAML and linked CREATE history sidecar
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: Final file and complete sidecar independently inspected. Canonical inspect
    captured bytes before scientific assessment. Actor, target, actual CREATE event
    and sidecar agree; no material CURIE or criticality claim is inferred.
  snapshot_sha256: c677b20cd2ead19cf7bf8b1882cfd567f55ca38ffe0bfa7c7514cfc9143c4c49
- evidence_id: identity_authority
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 master list, PDF p. 92 Hematite row; pp. 1-2 definitions
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: 'Retained official authority PDF text and rendered row independently inspected:
    Hematite, Fe2O3, approved, 1971 special procedure. The historical status notation
    is not an external material identifier. Iron element, hematite species and the
    impure commercial assay feed remain distinct.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/aem.01201-26
  locator: 'Retained complete Europe PMC XML: mineral weathering Methods, Results
    and Discussion; Figure 5; supplement methods pp. 1-2 and Tables S6/S7, rendered
    PDF pp. 11-12'
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: Independent review checked organism and inoculum, 0.60 g 75-150 micrometre
    feed in 60 mL GMM, 0.2 mL nominal 10^8 cells/mL inoculum, triplicate sacrificial
    assays at 37 C/160 rpm and 12/24 h; centrifuged, 0.45 micrometre filtered ICP-OES
    fraction. Visually inspected Table S6 exact cells, Table S7 oxide composition
    and Figure 5. These data support culture-associated mobilization, without pH-matched
    or killed-cell controls in the selected feed assay, phase purity, oxidation-state
    resolution or causal gene validation.
  snapshot_sha256: 6c7e4c45cb387bf0806c0e517e153ccc094fbd6b103eaa00de4c62f8999a7c6c
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13599522/supplementaryFiles
  locator: aem.01201-26-s0001.pdf, Tables S6/S7 and supplement Methods
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: 'Table S6 Fe means ± SD, n=3, in micromolar: 25.95 ± 0.90 at 12 h and 71.43
    ± 1.56 at 24 h versus 0.04 ± 0.00 controls at both times. Biological pH 4.69/4.66
    versus 7.16/7.12 controls; Table S7 86.58% Fe2O3 and 9.82% SiO2 are bulk oxide
    analyses, not phase percentages.'
  snapshot_sha256: bc170447b630c216e22448d6a5ae544d2c8efd5331e6a846564dc337da6e3616
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1404&mode=Info
  locator: Live taxonomy label/rank and retained official taxonomy XML
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: NCBITaxon:1404 is Priestia megaterium at species rank. No strain-specific
    taxonomic ID is inferred.
  snapshot_sha256: 0700c8fc37a88c59d57e25c8d1be945b20eb15a895544a22a39a6cd9942edcc2
- evidence_id: strain
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/CM125967.1
  locator: Retained official GenBank source features retrieved with seq_start=1, seq_stop=1;
    comparator CM125968.1 also checked
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: CM125967.1 source metadata identify strain PMA2-2, taxonomy 1404 and BioSample
    SAMN50659134. Comparator PMD1-1 is CM125968.1. This resolves the duplicated accession
    typo in one primary Methods paragraph consistently with Data Availability, without
    claiming full-genome sequence reanalysis. Browser nuccore open failed; retained
    official efetch feature metadata were inspected.
  snapshot_sha256: 312bb58411c8bc4aa9a5d74858d71c5ffbf2453dccbc0f742e951ab01eebbb63
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round18-catalyst-independent/dedup.log
  locator: Independent hidden/ignored-inclusive dedup and first returned web query
    sets
  accessed_at: '2026-10-11T11:20:45Z'
  support: context_only
  summary: Queries included exact DOI 10.1128/aem.01201-26 with correction/retraction/erratum
    and potassium feldspar NK851 controls acid protein. No applicable Dong notice
    surfaced in these returned sets. NK851 DOI 10.3390/ijms241814226 is a distinct
    potassium-release strain/assay with acid and protein-fraction comparisons, not
    a refutation of this narrower PMA2-2 observation; full curation remains deferred.
    Retained Crossref author notice check is contextual, not an independently exhaustive
    notice audit.
  search_scope: Ignored and hidden files included and symlinks followed in data, research,
    reviews, history, .claude and the named mineral-feeds raw directory. First returned
    web results only, no pagination; no machine-wide or exhaustive literature absence
    claim.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round18-gate-receipts.json
  locator: Finished receipt and /private/tmp/cmm-round18-final-{batch,require,history}.log
  accessed_at: '2026-10-11T11:20:45Z'
  support: supports
  summary: 'Reviewer independently read actual terminal receipt/logs: 308 passed,
    3 skipped in 86.49 s; 138 records and 154 history sessions valid. Separate nonempty
    and trusted-base history checks passed. The two reviewed files remain byte-identical
    to inspection.'
  snapshot_sha256: f77f5decb184fd5e6544b9d89c9699a95621e2a83749524526f6283fb5be2f66
assessments:
- assessment_id: identity
  area: identity
  topic: Material identity, feed and criticality boundaries
  outcome: supported
  summary: Hematite is an approved mineral species, Fe2O3; bulk oxide composition
    of the tested feed does not establish phase purity.
  target_ids:
  - cmmmech:hematite
  evidence_ids:
  - record
  - identity_authority
  - supplement
  - search
  dimensions:
  - name: material_kind
    value: mineral
    definition: Identity authority does not imply experimental feed purity or phase-specific
      release.
    evidence_ids:
    - record
    - identity_authority
    - supplement
  - name: criticality
    value: Not asserted
    definition: No jurisdiction/list/edition claim inherited from constituent elements
      or a broad critical-material label.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Assay-specific microbial mobilization and limits
  outcome: supported
  summary: Matched uninoculated controls support a culture-associated filtered-element
    increase. Acidification, expression correlations and cross-feed observations are
    bounded, with no isolated recovery yield or deployment claim.
  target_ids:
  - cmmmech:hematite
  evidence_ids:
  - record
  - primary
  - supplement
  - taxon
  - strain
  dimensions:
  - name: organism_and_biomass
    value: Living Priestia megaterium PMA2-2 culture, species ID 1404; CM125967.1
      strain source metadata
    definition: Species authority and accession metadata support reported identity;
      no full-genome experimental strain authentication was performed.
    evidence_ids:
    - taxon
    - strain
    - primary
  - name: substrate_and_pretreatment
    value: Commercial labelled 75-150 micrometre powder; 0.60 g per 60 mL GMM; original
      phase purity and cleaning unresolved
    definition: Nominal feed name and bulk oxides bound substrate identity; no unreported
      purification step is added.
    evidence_ids:
    - primary
    - supplement
    - record
  - name: conditions_controls_outcome
    value: 37 C, 160 rpm; 12/24 h, n=3; uninoculated GMM controls; filtered ICP-OES
      concentration and medium pH
    definition: Operational solution fraction and assay time distinguish observed
      mobilization from extraction percentage, oxidation-state reduction or pure-product
      recovery. No pH-matched or killed-cell comparison was available for these feeds.
    evidence_ids:
    - primary
    - supplement
  - name: mechanism_and_scale
    value: Laboratory culture-associated mobilization; molecular mechanism remains
      proposed
    definition: Separate 12-hour RT-qPCR associations do not establish gene necessity;
      biotite EPS, buffer or transcriptome experiments cannot establish the same cause
      in these feeds. No industrial deployment is asserted.
    evidence_ids:
    - record
    - primary
- assessment_id: provenance
  area: provenance
  topic: Actual CREATE session and exact reviewed bytes
  outcome: supported
  summary: Separate curator authored genuine codex/GPT-6 CREATE history. Canonical
    inspect preceded scientific assessment; final target/schema/history hashes and
    actual terminal checks agree.
  target_ids:
  - cmmmech:hematite
  evidence_ids:
  - record
  - gates
findings: []
actions: []
limitations:
- The commercial hematite-labelled material has substantial SiO2 by bulk analysis;
  supplier origin, cleaning and quantitative phase purity are unspecified. No pure-hematite-normalized
  yield follows.
- No pH-matched or killed-cell control isolates a causal contribution beyond the culture-associated
  observation. Figure 5 expression responses are associational, not gene-function
  validation.
- Primary text contains a duplicated comparator accession and olivine magnesium-unit
  conflict; the relevant official strain metadata and selected Fe/Al assays avoid
  importing those errors. Biotite-specific mechanistic experiments are not transferred.
- Publisher and PMC live routes were unavailable or challenged in some requests; full
  retained Europe PMC XML, relevant downloaded supplement, rendered tables and Figure
  5 were inspected. No complete genomics/metabolomics reanalysis was performed.
- Bounded notice and contrary-evidence searches cannot establish global absence. Dissolved
  elemental concentration is not phase-specific extraction yield, isolated product
  recovery or industrial deployment.
tags:
- round18
- independent
- scientific-review
- mineral
notes:
- Review interval starts at the recorded creation time of its canonical inspection
  target file, before scientific judgment; finished time marks final hash and terminal-receipt
  capture. Two independent per-record decisions share a primary paper and are not
  independent biological replications.
- All 34 mineral-feed dossier inventory/record hashes were independently recomputed
  with no discrepancy. No corrections were required; unresolved limitations remain
  in the record and frontier.
```
