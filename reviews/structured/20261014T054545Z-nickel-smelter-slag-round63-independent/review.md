# Independent scientific review of Nickel smelter slag

- Review: 20261014T054545Z-nickel-smelter-slag-round63-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T05:36:59.186961Z
- Finished UTC: 2026-10-14T05:45:45.592050Z
- Reviewer: codex /root/publication_completion_check (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The process-defined nickel slag owner is distinct from flotation tailings and a pure silicate mineral. The source supports culture-associated redox and limited nickel release, with 13/13, 12/12 and 11/10 percent inoculated/control total-Ni comparisons. The record does not convert inoculation into a proven recovery advantage. Required checks passed; no corrective finding.

## Scope And Provenance

Full field assessment of one new maintained nickel process-resource record against relevant original thesis chapters, exact source dossier and CREATE provenance.

Selection: Assigned exact maintained ID and path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1e3d834112099855c0398459415d0022336055f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:nickel-smelter-slag | data/records/nickel-smelter-slag.yaml | maintained | Nickel smelter slag |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named records | passed | True | cmmmech:nickel-smelter-slag | Executed by this reviewer; Checked 2 record(s); 0 failed. |
| Trusted-base history | passed | True | cmmmech:nickel-smelter-slag | Executed by this reviewer; Checked 337 history record(s); 0 error(s). |
| Full batch gate | passed | True | cmmmech:nickel-smelter-slag | Coordinator execution completed 2026-10-14T05:41:32Z: 317 tests passed, 3 skipped; 288 records and 337 histories valid. Reviewer read actual receipt/log and verified log SHA256. |
| Nonempty corpus | passed | True | cmmmech:nickel-smelter-slag | Coordinator execution completed 2026-10-14T05:41:51Z: 288 records, 0 failed. Reviewer read actual receipt/log and verified log SHA256. |

## Scientific And Domain Assessments

### Process-defined owner and citation identity

identity: supported. Targets: cmmmech:nickel-smelter-slag.

Feed provenance and production process support a separate secondary-resource owner. Source mineral assignments do not turn the mixed waste into a pure mineral. The existing copper-process owners and mineral records remain distinct.

### Conditional culture-associated leaching and null comparisons

evidence: supported. Targets: cmmmech:nickel-smelter-slag.

The process-defined nickel slag owner is distinct from flotation tailings and a pure silicate mineral. The source supports culture-associated redox and limited nickel release, with 13/13, 12/12 and 11/10 percent inoculated/control total-Ni comparisons. The record does not convert inoculation into a proven recovery advantage.

### Controls, denominator limits and source contradictions retained

consistency: supported. Targets: cmmmech:nickel-smelter-slag.

The record preserves unmatched pH and inoculum chemistry, uncertain LR authentication, no displayed replicate dispersion or statistical equivalence/significance, and inferred rather than measured passivation or oxygen effects. It avoids transferring respirometry, strong-acid/static or mineral-specific experiments into the 14-day flask mechanism. Numerical static inconsistencies are not pooled or silently repaired.

### Exact bytes, native history and access provenance

provenance: supported. Targets: cmmmech:nickel-smelter-slag.

Initial native inspect preceded assessment; final dossier reinspection did not change target/history bytes. The actual CREATE actor and timing are accurate. Primary original images, metadata and source-artifact hashes were independently checked. No gene/transcriptomic adapter is applicable to these source-defined material/assay claims.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/nickel-smelter-slag.yaml; Entire exact frozen maintained YAML, all fields | supports | Read the entire target. Material form, feed composition, source organism, methods, controls, total-metal denominators, null comparisons, source contradictions and provenance are explicitly represented. |
| primary | https://repositorio.unesp.br/server/api/core/bitstreams/bba9395f-d86b-4d4f-b763-0f632387492b/content; Munoz Blandon 2010 original 125-page thesis: title/front matter; pp. 33, 36-40, 50-72; relevant conclusions pp. 110-115; Figures 4-22, Tables 1-3 and 7-14 | supports | Independently read the complete relevant waste methods/results chapter, not the entire later mineral/isolate study. Visually inspected original pages containing Figures 4-22 and Tables 1-3, 7-11 and 13-14; Table 12 was read in extracted text as a summary of the preceding tables. Table 7 distinguishes HF/microwave total assays from partial aqua-regia digestion. Table 9 preserves negligible slag Ni benefit; Table 11 supplies total-Ni tailings comparisons. Table 2 shows strong-acid control lacks matched ferric culture; Figures 19/20 disagree on 120 versus 30 mmol/L iron. Static denominator inconsistencies and unmeasured oxygen/mass-transfer explanations are not silently promoted. Original file was acquired by curator; this reviewer re-inspected retained original pixels and verified its hash. |
| metadata | https://hdl.handle.net/11449/100745; Live official repository page and retained UNESP item metadata e0725f7c-7f63-47fe-9926-3c749e34cc7f | supports | Author, handle and issued date 2010-07-15 verified. Accession in 2014 is separate. Repository title differs slightly from original front matter. Catalog extent is 127 folios, while the supplied original PDF has 125 pages; relevant experimental pages are present. Open access is not treated as a redistribution license. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=info; Fresh NCBI species page and curator-retained HTML | supports | NCBITaxon:920 resolves Acidithiobacillus ferrooxidans at species rank. Type strain entries do not identify LR. The record retains source-labelled LR and its Lagoa Real origin without accession or independent stock authentication. |
| dossier | research/sources/round63-nickel-resources/20261014T053805Z-source-investigation.md; Final source report and companion JSON acquisition manifest | supports | Read final report and checked all 69 retained artifact hashes and byte sizes. Confirmed actual original acquisition versus HTML/PDF failures, metadata-only related 2009/2021 publications, 2017 methods gap and bounded first-result searches. Deferred source-gap issue 197 does not undermine the separately supported 2010 thesis record. |
| science_receipt | /private/tmp/cmm-round63-nickel-independent/scientific-receipt.json; Reviewer source/image coverage, hash verification and provenance receipt | supports | Pins exact inspected original page renders, complete primary PDF, metadata, source-manifest artifact checks and commands. No supported corrective record finding identified. Final batch checks are recorded separately after coordinator completion. |
| dedup | /private/tmp/cmm-round63-nickel-independent/dedup.json; Reviewer repository search plus inspected curator cited-raw scope | context_only | Hidden-, ignored- and symlink-inclusive rg search covers data/research/reviews/history/docs/.claude in selected text formats up to 8 MB. Current new owners and prior lead mentions are present; no earlier owner for this thesis experiment was found in that bounded scope. Copper-process owners, nickel laterite and mineral species have distinct identities. Curator 379-root cited-raw search was inspected, not rerun or represented as reviewer execution. No machine-wide absence claim. |
| search | /private/tmp/cmm-round63-nickel-independent/web-review.json; Fresh exact handle/author notice searches and NCBI authority lookup; first returned sets only | context_only | Queries included handle 11449/100745 with errata/corrigenda/correcao, author/year/slag/bacteria and exact NCBI taxon name. Returned evidence did not identify an affecting correction notice. This is bounded notice/source checking, not exhaustive citation-chain clearance. Original internal nulls and inconsistencies were assessed directly. |
| history | history/records/nickel-smelter-slag/2026-10-14T053537Z-codex-23c8e8.yaml; Actual inline CREATE and separately timestamped helper-generated CREATE sidecar | supports | Actor codex, model GPT-6, tool codex, exact target and scientific scope agree with this creation. No earlier authorship or completed review is invented. Reviewer did not edit records or histories. |
| validation | /private/tmp/cmm-round63-nickel-independent/checks.json; Actual reviewer named validation, trusted-base history gate and native inspections | supports | Reviewer execution: both named records valid, 0 failures; 337 histories, 0 errors against trusted base. Native inspect before assessment and reinspection after final dossier capture preserve unchanged target hashes. Commands, timestamps and exit codes retained. |
| batch | /private/tmp/cmm-round63-final-gates.json; Coordinator final batch command receipt and independently hash-checked log | supports | Coordinator executed final batch gates, each exit 0. Reviewer read receipt/log and verified log SHA256 90bf3a83eebaa7ca2d2378b9c1fd4862c324ca57cf55aaefd60a1ec5de53285c. This is coordinator execution, not duplicated reviewer testing. |

## Limits And Additional Notes

- Source-labelled LR is not independently authenticated; a species ID is not a strain accession.
- Inoculum chemistry, pH trajectories and some ferric/acid controls are unmatched; no unique molecular mechanism or statistically established effect is inferred.
- Mixed phase diffraction and solution assays do not establish mineral-specific mass balance or isolated recovery.
- Static unit/denominator inconsistencies remain unresolved; null comparisons are retained and precise inconsistent yields excluded.
- No inherited criticality or industrial microbial deployment. Relevant chapter and graphics were reviewed, not every later thesis experiment.
- Web notice searches and local hidden/ignored/symlink-inclusive dedup are bounded; no exhaustive absence claim.
- Findings by severity: no supported blocker, major, minor or informational corrective finding. Reviewer corrections: none.
- Complete primary PDF was curator-acquired and reviewer-reinspected. Live NCBI/UNESP source pages and notice searches supplement retained raw evidence.
- Scientific receipt records the earlier pending batch state; completed review separately binds the actual final batch receipt.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T054545Z-nickel-smelter-slag-round63-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Nickel smelter slag
started_at: '2026-10-14T05:36:59.186961Z'
finished_at: '2026-10-14T05:45:45.592050Z'
reviewer:
  identity: codex /root/publication_completion_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from the nickel-record and source-dossier curator.
    Reviewer independently inspected original thesis figures/tables and authority
    pages and did not edit nickel records or histories. Reviewer authored separate
    scorodite, which another agent reviews.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The process-defined nickel slag owner is distinct from flotation tailings
  and a pure silicate mineral. The source supports culture-associated redox and limited
  nickel release, with 13/13, 12/12 and 11/10 percent inoculated/control total-Ni
  comparisons. The record does not convert inoculation into a proven recovery advantage.
  Required checks passed; no corrective finding.
source:
  git_revision: 1e3d834112099855c0398459415d0022336055f5
  state: working_tree
  inputs:
  - path: data/records/nickel-smelter-slag.yaml
    sha256: 7dd113070944069fc2c4c8ab1096407587759570dc0a16c99f4bd53dc7947f71
    role: target
  - path: history/records/nickel-smelter-slag/2026-10-14T053537Z-codex-23c8e8.yaml
    sha256: f6196815c66ec71213557cfa673c1f1b30fbaa3efac3d6a43f1760897bc743b2
    role: context
  - path: research/sources/round63-nickel-resources/20261014T053805Z-source-investigation.json
    sha256: 15e6d80afaa639459d5fa8eafd779cbfc9091e45cf16626ae98048215c26418c
    role: context
  - path: research/sources/round63-nickel-resources/20261014T053805Z-source-investigation.md
    sha256: cef6624fa6a5c07e790eced6ada23f296677caab340e441f4298a4f9ac5b6aa6
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full field assessment of one new maintained nickel process-resource
    record against relevant original thesis chapters, exact source dossier and CREATE
    provenance.
  selection: Assigned exact maintained ID and path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:nickel-smelter-slag
  exclusions:
  - target: Other round63 records and deferred source candidates
    reason: Different reviewers/curators own other records. Deferred 2009/2021 methods
      and later thesis isolate/mineral experiments are not accepted mechanism claims
      here.
targets:
- target_id: cmmmech:nickel-smelter-slag
  path: data/records/nickel-smelter-slag.yaml
  label: Nickel smelter slag
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/nickel-smelter-slag.yaml
    role: maintained_input
checks:
- check_id: named
  name: Named records
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/nickel-smelter-slag.yaml data/records/nickel-flotation-tailings.yaml
    --require-records
  status: passed
  required: true
  summary: Executed by this reviewer; Checked 2 record(s); 0 failed.
  target_ids:
  - cmmmech:nickel-smelter-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: history
  name: Trusted-base history
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate-history --base 1e3d834112099855c0398459415d0022336055f5
  status: passed
  required: true
  summary: Executed by this reviewer; Checked 337 history record(s); 0 error(s).
  target_ids:
  - cmmmech:nickel-smelter-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: batch
  name: Full batch gate
  command: just check
  status: passed
  required: true
  summary: 'Coordinator execution completed 2026-10-14T05:41:32Z: 317 tests passed,
    3 skipped; 288 records and 337 histories valid. Reviewer read actual receipt/log
    and verified log SHA256.'
  target_ids:
  - cmmmech:nickel-smelter-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: nonempty
  name: Nonempty corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: 'Coordinator execution completed 2026-10-14T05:41:51Z: 288 records, 0 failed.
    Reviewer read actual receipt/log and verified log SHA256.'
  target_ids:
  - cmmmech:nickel-smelter-slag
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/nickel-smelter-slag.yaml
  locator: Entire exact frozen maintained YAML, all fields
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Read the entire target. Material form, feed composition, source organism,
    methods, controls, total-metal denominators, null comparisons, source contradictions
    and provenance are explicitly represented.
  snapshot_sha256: 7dd113070944069fc2c4c8ab1096407587759570dc0a16c99f4bd53dc7947f71
- evidence_id: primary
  kind: primary_source
  reference: https://repositorio.unesp.br/server/api/core/bitstreams/bba9395f-d86b-4d4f-b763-0f632387492b/content
  locator: 'Munoz Blandon 2010 original 125-page thesis: title/front matter; pp. 33,
    36-40, 50-72; relevant conclusions pp. 110-115; Figures 4-22, Tables 1-3 and 7-14'
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Independently read the complete relevant waste methods/results chapter,
    not the entire later mineral/isolate study. Visually inspected original pages
    containing Figures 4-22 and Tables 1-3, 7-11 and 13-14; Table 12 was read in extracted
    text as a summary of the preceding tables. Table 7 distinguishes HF/microwave
    total assays from partial aqua-regia digestion. Table 9 preserves negligible slag
    Ni benefit; Table 11 supplies total-Ni tailings comparisons. Table 2 shows strong-acid
    control lacks matched ferric culture; Figures 19/20 disagree on 120 versus 30
    mmol/L iron. Static denominator inconsistencies and unmeasured oxygen/mass-transfer
    explanations are not silently promoted. Original file was acquired by curator;
    this reviewer re-inspected retained original pixels and verified its hash.
  snapshot_sha256: be9382b6681d42d7b951e23ad2bff012a4bac2a2c1d929a548461feffdeb1c79
- evidence_id: metadata
  kind: database
  reference: https://hdl.handle.net/11449/100745
  locator: Live official repository page and retained UNESP item metadata e0725f7c-7f63-47fe-9926-3c749e34cc7f
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Author, handle and issued date 2010-07-15 verified. Accession in 2014 is
    separate. Repository title differs slightly from original front matter. Catalog
    extent is 127 folios, while the supplied original PDF has 125 pages; relevant
    experimental pages are present. Open access is not treated as a redistribution
    license.
  snapshot_sha256: 1de129b5843690a58814fcb8cadaaaa210c9b6ab0966304a005da2b79694f7d6
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=info
  locator: Fresh NCBI species page and curator-retained HTML
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: NCBITaxon:920 resolves Acidithiobacillus ferrooxidans at species rank.
    Type strain entries do not identify LR. The record retains source-labelled LR
    and its Lagoa Real origin without accession or independent stock authentication.
  snapshot_sha256: c6d264e2f6ed730350be86773d9564c7427f7f089b57ed566d6494e3bd21a4ac
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round63-nickel-resources/20261014T053805Z-source-investigation.md
  locator: Final source report and companion JSON acquisition manifest
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Read final report and checked all 69 retained artifact hashes and byte
    sizes. Confirmed actual original acquisition versus HTML/PDF failures, metadata-only
    related 2009/2021 publications, 2017 methods gap and bounded first-result searches.
    Deferred source-gap issue 197 does not undermine the separately supported 2010
    thesis record.
  snapshot_sha256: cef6624fa6a5c07e790eced6ada23f296677caab340e441f4298a4f9ac5b6aa6
- evidence_id: science_receipt
  kind: record_content
  reference: /private/tmp/cmm-round63-nickel-independent/scientific-receipt.json
  locator: Reviewer source/image coverage, hash verification and provenance receipt
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Pins exact inspected original page renders, complete primary PDF, metadata,
    source-manifest artifact checks and commands. No supported corrective record finding
    identified. Final batch checks are recorded separately after coordinator completion.
  snapshot_sha256: 91273c86dcfd0d2fbf9eb5d1364bf2b91beacb4fdc960588ecd1a904245da703
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round63-nickel-independent/dedup.json
  locator: Reviewer repository search plus inspected curator cited-raw scope
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: context_only
  summary: Hidden-, ignored- and symlink-inclusive rg search covers data/research/reviews/history/docs/.claude
    in selected text formats up to 8 MB. Current new owners and prior lead mentions
    are present; no earlier owner for this thesis experiment was found in that bounded
    scope. Copper-process owners, nickel laterite and mineral species have distinct
    identities. Curator 379-root cited-raw search was inspected, not rerun or represented
    as reviewer execution. No machine-wide absence claim.
  snapshot_sha256: 3cf1f7d13aa4f7bd16ce1b48a0275559b59aec0426bc2a4138e0b2e4b1c2ac99
  search_scope: Reviewer rg --no-ignore --hidden --follow within data, research, reviews,
    history, docs and .claude; nickel slag/tailings names, exact thesis handle, Blandon
    and Serra de Fortaleza; md/json/yaml/yml/txt up to 8 MB. Curator cited-raw 379-root
    search separately inspected. No unrelated home/temp sweep or binary-only PDF absence
    claim.
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round63-nickel-independent/web-review.json
  locator: Fresh exact handle/author notice searches and NCBI authority lookup; first
    returned sets only
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: context_only
  summary: Queries included handle 11449/100745 with errata/corrigenda/correcao, author/year/slag/bacteria
    and exact NCBI taxon name. Returned evidence did not identify an affecting correction
    notice. This is bounded notice/source checking, not exhaustive citation-chain
    clearance. Original internal nulls and inconsistencies were assessed directly.
  snapshot_sha256: 427345dff1201e65c39723e3805572b4bde4d5e9769cfb1ac3ecdbe904173c4d
  search_scope: Exact handle 11449/100745 with errata/corrigenda/correcao; author
    Munoz Blandon, 2010, escoria and bacterias; exact Acidithiobacillus ferrooxidans
    Taxonomy ID 920. First returned web sets only, no date filters or pagination;
    NCBI and UNESP pages opened. No exhaustive notice clearance.
- evidence_id: history
  kind: record_content
  reference: history/records/nickel-smelter-slag/2026-10-14T053537Z-codex-23c8e8.yaml
  locator: Actual inline CREATE and separately timestamped helper-generated CREATE
    sidecar
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Actor codex, model GPT-6, tool codex, exact target and scientific scope
    agree with this creation. No earlier authorship or completed review is invented.
    Reviewer did not edit records or histories.
  snapshot_sha256: f6196815c66ec71213557cfa673c1f1b30fbaa3efac3d6a43f1760897bc743b2
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round63-nickel-independent/checks.json
  locator: Actual reviewer named validation, trusted-base history gate and native
    inspections
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: 'Reviewer execution: both named records valid, 0 failures; 337 histories,
    0 errors against trusted base. Native inspect before assessment and reinspection
    after final dossier capture preserve unchanged target hashes. Commands, timestamps
    and exit codes retained.'
  snapshot_sha256: c939cab90fcf9b5bd7f5e4bc39ee729b43bdcdd3a9fe8957e6f9d6be49065848
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round63-final-gates.json
  locator: Coordinator final batch command receipt and independently hash-checked
    log
  accessed_at: '2026-10-14T05:43:30.474745Z'
  support: supports
  summary: Coordinator executed final batch gates, each exit 0. Reviewer read receipt/log
    and verified log SHA256 90bf3a83eebaa7ca2d2378b9c1fd4862c324ca57cf55aaefd60a1ec5de53285c.
    This is coordinator execution, not duplicated reviewer testing.
  snapshot_sha256: f609ce00abe12705c5c76645c1f43d3fdb1461e9e4dc0ca0d963f591a215801d
assessments:
- assessment_id: identity
  area: identity
  topic: Process-defined owner and citation identity
  outcome: supported
  summary: Feed provenance and production process support a separate secondary-resource
    owner. Source mineral assignments do not turn the mixed waste into a pure mineral.
    The existing copper-process owners and mineral records remain distinct.
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - record
  - primary
  - metadata
  - dedup
- assessment_id: mechanism
  area: evidence
  topic: Conditional culture-associated leaching and null comparisons
  outcome: supported
  summary: The process-defined nickel slag owner is distinct from flotation tailings
    and a pure silicate mineral. The source supports culture-associated redox and
    limited nickel release, with 13/13, 12/12 and 11/10 percent inoculated/control
    total-Ni comparisons. The record does not convert inoculation into a proven recovery
    advantage.
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - record
  - primary
  - taxon
  dimensions:
  - name: material_form
    value: Nickel flash-smelting slag
    definition: A mixed process residue from the specified Votorantim feed, not a
      mineral species or universal waste composition.
    evidence_ids:
    - record
    - primary
  - name: organism_and_biomass
    value: Living source-labelled Acidithiobacillus ferrooxidans LR culture; NCBITaxon:920
      is species only
    definition: Unverified isolate accession. Washed cells belong to separate Warburg
      respirometry, not established for leaching inocula.
    evidence_ids:
    - primary
    - taxon
  - name: assay_and_controls
    value: Duplicate 150 mL cultures in 250 mL flasks; 5% w/v feed, 5% v/v inoculum,
      30 degrees C, 150 rpm, 14 days
    definition: No-added-iron, 120 mmol/L ferrous and grown-ferric-culture treatments
      with controls; pH correction and inoculum carryover limit causal isolation.
    evidence_ids:
    - primary
    - record
  - name: outcome_denominator
    value: Source-reported dissolved-metal extraction as percent of total feed Ni/Cu
    definition: Total feed determined by HF/microwave digestion; aqua-regia-soluble
      fraction is separate and not water solubility. No isolated-product yield.
    evidence_ids:
    - primary
    - record
  - name: criticality_and_deployment
    value: No inherited criticality; laboratory experiments with industrial-origin
      feed
    definition: No jurisdiction/list/edition assertion or pilot/commercial biological
      deployment is claimed.
    evidence_ids:
    - record
    - primary
- assessment_id: uncertainty
  area: consistency
  topic: Controls, denominator limits and source contradictions retained
  outcome: supported
  summary: The record preserves unmatched pH and inoculum chemistry, uncertain LR
    authentication, no displayed replicate dispersion or statistical equivalence/significance,
    and inferred rather than measured passivation or oxygen effects. It avoids transferring
    respirometry, strong-acid/static or mineral-specific experiments into the 14-day
    flask mechanism. Numerical static inconsistencies are not pooled or silently repaired.
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Exact bytes, native history and access provenance
  outcome: supported
  summary: Initial native inspect preceded assessment; final dossier reinspection
    did not change target/history bytes. The actual CREATE actor and timing are accurate.
    Primary original images, metadata and source-artifact hashes were independently
    checked. No gene/transcriptomic adapter is applicable to these source-defined
    material/assay claims.
  target_ids:
  - cmmmech:nickel-smelter-slag
  evidence_ids:
  - history
  - validation
  - dossier
  - science_receipt
findings: []
actions: []
limitations:
- Source-labelled LR is not independently authenticated; a species ID is not a strain
  accession.
- Inoculum chemistry, pH trajectories and some ferric/acid controls are unmatched;
  no unique molecular mechanism or statistically established effect is inferred.
- Mixed phase diffraction and solution assays do not establish mineral-specific mass
  balance or isolated recovery.
- Static unit/denominator inconsistencies remain unresolved; null comparisons are
  retained and precise inconsistent yields excluded.
- No inherited criticality or industrial microbial deployment. Relevant chapter and
  graphics were reviewed, not every later thesis experiment.
- Web notice searches and local hidden/ignored/symlink-inclusive dedup are bounded;
  no exhaustive absence claim.
notes:
- 'Findings by severity: no supported blocker, major, minor or informational corrective
  finding. Reviewer corrections: none.'
- Complete primary PDF was curator-acquired and reviewer-reinspected. Live NCBI/UNESP
  source pages and notice searches supplement retained raw evidence.
- Scientific receipt records the earlier pending batch state; completed review separately
  binds the actual final batch receipt.
links:
- https://hdl.handle.net/11449/100745
- https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=info
```
