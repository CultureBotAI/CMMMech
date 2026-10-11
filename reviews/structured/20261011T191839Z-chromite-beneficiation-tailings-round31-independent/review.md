# Independent scientific review of chromite-beneficiation-tailings culture assays

- Review: 20261011T191839Z-chromite-beneficiation-tailings-round31-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T19:11:41.953770Z
- Finished UTC: 2026-10-11T19:18:39.920468Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The record accurately represents mixed physical-beneficiation tailings and two conditional culture-associated laboratory observations. Measured filtered-element trajectories, separate chemical extraction and predicted MINTEQ species are distinguished. Acid-control counterevidence, source unit/time conflicts and unmeasured Cr reduction remain explicit. No actionable record defect was identified within this full target review. Full suite308passed3skipped; affected postcorrection gates passed184records/210histories. Structured bundle check follows saving all reviews.

## Scope And Provenance

All maintained record fields and CREATE history; resource identity, experimental arms, exact adopted measurements, taxon mapping, controls, missing mass accounting and deployment limits.

Selection: One new round31 record authored by another agent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 075c1ca032b68162eb8350b7e8d9bfe9530ca143.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chromite-beneficiation-tailings | data/records/chromite-beneficiation-tailings.yaml | maintained | Chromite beneficiation tailings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:chromite-beneficiation-tailings | Reviewer executed directly; terminal exit0, Checked1record;0failed. Target bytes remain unchanged. |
| final batch gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-final-batch.log; SHA256 c42464b59af6a3aac67f79d03121e06de34f98a4ed6048683c370ac90c3cf639. .................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 108.69s (0:01:48)<br>Checked 184 record(s); 0 failed.<br>Checked 209 history record(s); 0 error(s). |
| final nonempty gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-final-nonempty.log; SHA256 28173453e8d0bf2d4fc8bf1a392f98d24e15c5c4998de9cb6b4813c91f243899. Checked 184 record(s); 0 failed. |
| final history gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-final-history.log; SHA256 e5d1e7a4f33f2e4e4cacc7cf1250be42d30c91e582bb145f3fe2218069e9ff5c. Checked 209 history record(s); 0 error(s). |
| corrected named gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-corrected-named.log; SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e. Checked 1 record(s); 0 failed. |
| corrected nonempty gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-corrected-nonempty.log; SHA256 28173453e8d0bf2d4fc8bf1a392f98d24e15c5c4998de9cb6b4813c91f243899. Checked 184 record(s); 0 failed. |
| corrected history gate | passed | True | cmmmech:chromite-beneficiation-tailings | Actual root terminal receipt; /private/tmp/cmm-round31-corrected-history.log; SHA256 230525627011be86c95ae540fadb75444fc0ff0a4e135c46f2fbaf2c448fcb36. Checked 210 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Resource and organism boundaries

identity: supported. Targets: cmmmech:chromite-beneficiation-tailings.

Mixed beneficiation tailings are correctly separated from chromite, concentrate, overburden and chromate-manufacturing waste. Current organism mapping retains historical names and qualifications.

### Experimental controls and conditions

evidence: supported. Targets: cmmmech:chromite-beneficiation-tailings.

Record distinguishes initial media pH from cultured trajectories, printed11%sulfur from a corrected recipe, reagent acid from final concentration, and independent chemical arms from medium controls.

### Measured versus inferred release and speciation

quantity: supported. Targets: cmmmech:chromite-beneficiation-tailings.

Adopted Fe and operational Cr extraction quantities match exact original prose/tables; source units/time conflicts are explicitly retained. No numeric observations requiring unavailable analysis dates were invented.

### Exact history, sources and structural validity

provenance: supported. Targets: cmmmech:chromite-beneficiation-tailings.

Record and canonical history hashes are attested against durable merged base; independent primary/authority checks support qualified scientific acceptance.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/chromite-beneficiation-tailings.yaml; Every frozen field | supports | Distinct mixed secondary resource; no inherited criticality or recovered-product claim. |
| primary | https://doi.org/10.3390/min8060261; 23-page original; complete Sections2–4 and all main Figures1–8/Tables1–2; visual pages3,4,7–14 and full relevant extracted prose | supports | Primary methods establish May2017 Sukinda fresh physical-beneficiation tailings, duplicate500mL reactors at30°C190rpm,5/10/30g/L,1% inoculum, medium/water controls with azide and20mL replacement. Figures support acidic Fe/Ni/Mn/Al release and transient alkaline-culture Fe with Cr decline. Separate chemical extraction has1h/1g:25mL and CrVI assay; batch elemental concentration does not itself prove Cr reduction. Authors explicitly compare lower cultured Fe to acidified water at30g/L. Source discrepancies are accurately preserved. |
| si | https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf; All seven original pages, FiguresS1–S5 and TablesS1–S3; final page blank | context_only | SI independently confirms evolving dissolved oxygen, abiotic iron speciation, acid/alkaline water contrasts, transient protein/CAS, unlike concentrate curves and calculated species. S2 Fe usesmg/L while S3 usesmg/kg; S3 acid iron approaches479mg/kg and S5 concentrate Cr is much lower but not at a matched curve point. Tables are MINTEQ inputs/predictions, not measured precipitates or Cr-valence time courses. |
| taxa | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1495066; Live NCBI1495066 and930; DSMZ9463 catalogue current name, strain, origin fields | supports | NCBI1495066 lists Pseudomonas capeferrum, rank species, WCS358 type strain and Pseudomonas sp.WCS358 inclusion, with effective/not validly published caveat. NCBI930 is A.thiooxidans; DSM9463 is B-S2 from Australian bioleaching reactor. No authority authenticates the source stocks. |
| provenance | history/records/chromite-beneficiation-tailings/2026-10-11T190716Z-codex-68d22b.yaml; Complete canonical sidecar and distinct inline CREATE | supports | Actual Codex/GPT-6 authorship, current UTC, exact target and qualified change. Inline event does not claim this independent review. |
| dedup | /private/tmp/cmm-round31-chromite-independent-dedup.txt; Full matching-path output, independently assessed | supports | Only current new record plus prior round30 handoff/current research/history hit the exact resource/DOI search. Existing chromite denotes mineral species and has a different source. Curator broad binary search separately records10 parse/time failures; no missing-binary negative claim. |
| notices | Independent web search2026-10-11; First returned result sets for exact DOI/title notices and contradiction searches | supports | No affecting notice identified. Main paper itself contains chemical controls and weak-effect counterevidence retained by record; later uninspected snippets are not new experimental evidence. |

## Limits And Additional Notes

- Culture effects are confounded with unlike pH and medium composition; lower release in a chemical acid comparison prevents universal microbial enhancement.
- Main Table2/prose total-Cr units conflict; SI iron normalization and 30/34-day schedules are not reconciled. Working volume, tested particle distribution and cumulative sample-replacement accounting remain unresolved.
- Direct Cr(III)/Cr(VI) trajectories, specific molecular reductants, isolated products and industrial microbial deployment were not demonstrated. MINTEQ and CAS signals are not direct molecular or solid-phase proof.
- Species/collection mappings resolve source names, not genomic authentication of experimental stocks. WCS358 current effective-name status remains qualified.
- Notice and dedup searches are bounded. Local text search includes hidden/ignored files and relevant symlinks but is not an exhaustive search of inaccessible binaries or the literature.
- No maintained corrections were necessary. Source limitations already explicitly retained are not manufactured as review issues.
- Original PDFs and image renders remain outside Git; only this review pair is saved.
- Full tests passed before the unrelated kaolin-mine-waste wording/history correction. The affected named/nonempty/history gates were rerun afterward; this reviewed target/history/schema/dossier never changed. No identical pytest repetition is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191839Z-chromite-beneficiation-tailings-round31-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of chromite-beneficiation-tailings culture assays
started_at: '2026-10-11T19:11:41.953770Z'
finished_at: '2026-10-11T19:18:39.920468Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent, /root/round27_eaf_slag, authored this record/history/dossier.
    Root independently inspected the frozen inputs before assessment, original main
    methods/results/discussion, all eight main figures and both tables, and all seven
    SI pages. Current organism authorities were independently opened. Shared worktree
    and curator-acquired raw files are disclosed; root made no maintained target edits.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The record accurately represents mixed physical-beneficiation tailings and
  two conditional culture-associated laboratory observations. Measured filtered-element
  trajectories, separate chemical extraction and predicted MINTEQ species are distinguished.
  Acid-control counterevidence, source unit/time conflicts and unmeasured Cr reduction
  remain explicit. No actionable record defect was identified within this full target
  review. Full suite308passed3skipped; affected postcorrection gates passed184records/210histories.
  Structured bundle check follows saving all reviews.
source:
  git_revision: 075c1ca032b68162eb8350b7e8d9bfe9530ca143
  state: working_tree
  inputs:
  - path: data/records/chromite-beneficiation-tailings.yaml
    sha256: fb1b610706d32f32e8984ad07d1e776e2ec804438e7d292b0e80d14874a15cb2
    role: target
  - path: history/records/chromite-beneficiation-tailings/2026-10-11T190716Z-codex-68d22b.yaml
    sha256: 7584f4e68f8bb94acb855bd2324c87996f8f1d1bcaf70a7387605771ddf8ebe1
    role: context
  - path: research/sources/round31-chromite-tailings/20261011T190925Z-source-investigation.md
    sha256: f812775c1f3a3c7a099918d49cb6ee8355196cf180324ca8a37d82f127023508
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All maintained record fields and CREATE history; resource identity,
    experimental arms, exact adopted measurements, taxon mapping, controls, missing
    mass accounting and deployment limits.
  selection: One new round31 record authored by another agent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chromite-beneficiation-tailings
  exclusions:
  - target: New primary experiments, raw instrumental reanalysis and uncurated follow-up
      papers
    reason: Not needed to validate the bounded 2018 record; no completeness claim
      for all chromite-tailings literature.
targets:
- target_id: cmmmech:chromite-beneficiation-tailings
  path: data/records/chromite-beneficiation-tailings.yaml
  label: Chromite beneficiation tailings
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite-beneficiation-tailings.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named record validation
  command: uv run --locked cmmmech validate data/records/chromite-beneficiation-tailings.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed directly; terminal exit0, Checked1record;0failed. Target
    bytes remain unchanged.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: final_batch
  name: final batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual root terminal receipt; /private/tmp/cmm-round31-final-batch.log;
    SHA256 c42464b59af6a3aac67f79d03121e06de34f98a4ed6048683c370ac90c3cf639. .................................sss.................
    [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 108.69s (0:01:48)

    Checked 184 record(s); 0 failed.

    Checked 209 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: final_nonempty
  name: final nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual root terminal receipt; /private/tmp/cmm-round31-final-nonempty.log;
    SHA256 28173453e8d0bf2d4fc8bf1a392f98d24e15c5c4998de9cb6b4813c91f243899. Checked
    184 record(s); 0 failed.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: final_history
  name: final history gate
  command: uv run --locked cmmmech validate-history --base 075c1ca032b68162eb8350b7e8d9bfe9530ca143
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual root terminal receipt; /private/tmp/cmm-round31-final-history.log;
    SHA256 e5d1e7a4f33f2e4e4cacc7cf1250be42d30c91e582bb145f3fe2218069e9ff5c. Checked
    209 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: corrected_named
  name: corrected named gate
  command: uv run --locked cmmmech validate data/records/kaolin-mine-waste.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual root terminal receipt; /private/tmp/cmm-round31-corrected-named.log;
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e. Checked
    1 record(s); 0 failed.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: corrected_nonempty
  name: corrected nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual root terminal receipt; /private/tmp/cmm-round31-corrected-nonempty.log;
    SHA256 28173453e8d0bf2d4fc8bf1a392f98d24e15c5c4998de9cb6b4813c91f243899. Checked
    184 record(s); 0 failed.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
- check_id: corrected_history
  name: corrected history gate
  command: uv run --locked cmmmech validate-history --base 075c1ca032b68162eb8350b7e8d9bfe9530ca143
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual root terminal receipt; /private/tmp/cmm-round31-corrected-history.log;
    SHA256 230525627011be86c95ae540fadb75444fc0ff0a4e135c46f2fbaf2c448fcb36. Checked
    210 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/chromite-beneficiation-tailings.yaml
  locator: Every frozen field
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: Distinct mixed secondary resource; no inherited criticality or recovered-product
    claim.
  snapshot_sha256: fb1b610706d32f32e8984ad07d1e776e2ec804438e7d292b0e80d14874a15cb2
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min8060261
  locator: 23-page original; complete Sections2–4 and all main Figures1–8/Tables1–2;
    visual pages3,4,7–14 and full relevant extracted prose
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: Primary methods establish May2017 Sukinda fresh physical-beneficiation
    tailings, duplicate500mL reactors at30°C190rpm,5/10/30g/L,1% inoculum, medium/water
    controls with azide and20mL replacement. Figures support acidic Fe/Ni/Mn/Al release
    and transient alkaline-culture Fe with Cr decline. Separate chemical extraction
    has1h/1g:25mL and CrVI assay; batch elemental concentration does not itself prove
    Cr reduction. Authors explicitly compare lower cultured Fe to acidified water
    at30g/L. Source discrepancies are accurately preserved.
  snapshot_sha256: ad6db3e6510e8ea87060053a3faf2cd0f50320ea596583328bcfccff0f71d140
- evidence_id: si
  kind: primary_source
  reference: https://mdpi-res.com/minerals/minerals-08-00261/article_deploy/minerals-08-00261-s001.pdf
  locator: All seven original pages, FiguresS1–S5 and TablesS1–S3; final page blank
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: context_only
  summary: SI independently confirms evolving dissolved oxygen, abiotic iron speciation,
    acid/alkaline water contrasts, transient protein/CAS, unlike concentrate curves
    and calculated species. S2 Fe usesmg/L while S3 usesmg/kg; S3 acid iron approaches479mg/kg
    and S5 concentrate Cr is much lower but not at a matched curve point. Tables are
    MINTEQ inputs/predictions, not measured precipitates or Cr-valence time courses.
  snapshot_sha256: b3786e7a2eab0d5216758405f2c54e52503875dc3017dc5f47c8849fa4db4265
- evidence_id: taxa
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1495066
  locator: Live NCBI1495066 and930; DSMZ9463 catalogue current name, strain, origin
    fields
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: NCBI1495066 lists Pseudomonas capeferrum, rank species, WCS358 type strain
    and Pseudomonas sp.WCS358 inclusion, with effective/not validly published caveat.
    NCBI930 is A.thiooxidans; DSM9463 is B-S2 from Australian bioleaching reactor.
    No authority authenticates the source stocks.
- evidence_id: provenance
  kind: record_content
  reference: history/records/chromite-beneficiation-tailings/2026-10-11T190716Z-codex-68d22b.yaml
  locator: Complete canonical sidecar and distinct inline CREATE
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: Actual Codex/GPT-6 authorship, current UTC, exact target and qualified
    change. Inline event does not claim this independent review.
  snapshot_sha256: 7584f4e68f8bb94acb855bd2324c87996f8f1d1bcaf70a7387605771ddf8ebe1
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round31-chromite-independent-dedup.txt
  locator: Full matching-path output, independently assessed
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: Only current new record plus prior round30 handoff/current research/history
    hit the exact resource/DOI search. Existing chromite denotes mineral species and
    has a different source. Curator broad binary search separately records10 parse/time
    failures; no missing-binary negative claim.
  search_scope: rg --no-ignore --hidden --follow -l -i chromite.beneficiation.tailings|10\.3390/min8060261
    in current data,research,reviews,history; ignored files included. Curator referenced-root
    receipts read as supporting context, not claimed as reviewer-executed searches.
  snapshot_sha256: 0039ca56fea4a36f11bdb6005b3f6aab20265caadcabaae325705c4a47b65f60
- evidence_id: notices
  kind: search
  reference: Independent web search2026-10-11
  locator: First returned result sets for exact DOI/title notices and contradiction
    searches
  accessed_at: '2026-10-11T19:13:36.711951Z'
  support: supports
  summary: No affecting notice identified. Main paper itself contains chemical controls
    and weak-effect counterevidence retained by record; later uninspected snippets
    are not new experimental evidence.
  search_scope: '"10.3390/min8060261" correction retraction erratum; "(Bio)leaching
    Behavior of Chromite Tailings" contradictory. No pagination or exhaustive clearance
    claimed.'
assessments:
- assessment_id: identity
  area: identity
  topic: Resource and organism boundaries
  outcome: supported
  summary: Mixed beneficiation tailings are correctly separated from chromite, concentrate,
    overburden and chromate-manufacturing waste. Current organism mapping retains
    historical names and qualifications.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - record
  - primary
  - taxa
  - dedup
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: Processing origin, not constituent metal value, establishes category.
    evidence_ids:
    - primary
  - name: criticality
    value: Not asserted
    definition: Omission is not a not-listed claim; no list/edition is inherited.
    evidence_ids:
    - record
  - name: organisms
    value: A.thiooxidans DSM9463 and WCS358/current P.capeferrum
    definition: Living source-labelled cultures; species mapping does not authenticate
      experimental stocks.
    evidence_ids:
    - primary
    - taxa
- assessment_id: conditions
  area: evidence
  topic: Experimental controls and conditions
  outcome: supported
  summary: Record distinguishes initial media pH from cultured trajectories, printed11%sulfur
    from a corrected recipe, reagent acid from final concentration, and independent
    chemical arms from medium controls.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - record
  - primary
  - si
  dimensions:
  - name: scale
    value: Laboratory duplicate batches
    definition: 500mL vessels,unknown working liquid volume,5/10/30g/L,30°C190rpm;
      no industrial deployment.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Azide-treated medium/water controls and separate acid/alkaline water comparisons
    definition: Unmatched pH and chemistry prevent acidity-independent microbial effect
      estimates.
    evidence_ids:
    - primary
    - si
- assessment_id: outcome
  area: quantity
  topic: Measured versus inferred release and speciation
  outcome: supported
  summary: Adopted Fe and operational Cr extraction quantities match exact original
    prose/tables; source units/time conflicts are explicitly retained. No numeric
    observations requiring unavailable analysis dates were invented.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - record
  - primary
  - si
  dimensions:
  - name: denominator
    value: mg extracted element per kg tailings
    definition: Not leachate mg/L, phase abundance or recovered product percentage.
    evidence_ids:
    - primary
  - name: causality
    value: Culture-associated trajectories
    definition: No unique iron-oxidation, siderophore or Cr-reductase mechanism asserted;
      CAS/protein and MINTEQ are appropriately limited.
    evidence_ids:
    - primary
    - si
    - record
- assessment_id: provenance
  area: provenance
  topic: Exact history, sources and structural validity
  outcome: supported
  summary: Record and canonical history hashes are attested against durable merged
    base; independent primary/authority checks support qualified scientific acceptance.
  target_ids:
  - cmmmech:chromite-beneficiation-tailings
  evidence_ids:
  - record
  - provenance
  - notices
findings: []
actions: []
limitations:
- Culture effects are confounded with unlike pH and medium composition; lower release
  in a chemical acid comparison prevents universal microbial enhancement.
- Main Table2/prose total-Cr units conflict; SI iron normalization and 30/34-day schedules
  are not reconciled. Working volume, tested particle distribution and cumulative
  sample-replacement accounting remain unresolved.
- Direct Cr(III)/Cr(VI) trajectories, specific molecular reductants, isolated products
  and industrial microbial deployment were not demonstrated. MINTEQ and CAS signals
  are not direct molecular or solid-phase proof.
- Species/collection mappings resolve source names, not genomic authentication of
  experimental stocks. WCS358 current effective-name status remains qualified.
- Notice and dedup searches are bounded. Local text search includes hidden/ignored
  files and relevant symlinks but is not an exhaustive search of inaccessible binaries
  or the literature.
notes:
- No maintained corrections were necessary. Source limitations already explicitly
  retained are not manufactured as review issues.
- Original PDFs and image renders remain outside Git; only this review pair is saved.
- Full tests passed before the unrelated kaolin-mine-waste wording/history correction.
  The affected named/nonempty/history gates were rerun afterward; this reviewed target/history/schema/dossier
  never changed. No identical pytest repetition is claimed.
links:
- research/sources/round31-chromite-tailings/20261011T190925Z-source-investigation.md
- https://doi.org/10.3390/min8060261
tags:
- round31
- independent
- scientific
- chromite-beneficiation-tailings
```
