# Independent scientific review of eudialyte ore

- Review: 20261012T092440Z-eudialyte-ore-round52-science
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T09:18:55.861107Z
- Finished UTC: 2026-10-12T09:24:40.352428Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The source-qualified ore and narrow culture-associated laboratory leaching claim are supported. No corrective finding in the reviewed state; organism, analytical, denominator and control limitations are retained.

## Scope And Provenance

All eudialyte-ore fields, CREATE history, paired dossier and schema; Chapter4 experiment and relevant general methods, taxon, original graphics and archive scope.

Selection: Independent assigned exact-target review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 79ed7d69ea654d1b67bbf74bb931ff70c4c6913e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:eudialyte-ore | data/records/eudialyte-ore.yaml | maintained | Eudialyte ore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:eudialyte-ore | Root reviewer executed; one record checked, zero failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Completed batch batch | passed | True | cmmmech:eudialyte-ore | Root executed; actual log /private/tmp/cmm-round52-final-batch.log SHA256 98c9a3c5b08e68cefe8dc71e984bff78ca3b8320a49f048a43ca0402489f5685. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 179.41s (0:02:59)<br>Checked 253 record(s); 0 failed.<br>Checked 299 history record(s); 0 error(s).<br> |
| Completed batch nonempty | passed | True | cmmmech:eudialyte-ore | Root executed; actual log /private/tmp/cmm-round52-final-nonempty.log SHA256 4a50f2f93e44bfb9e2561b166775c22abe8b3fb410bdcd90d2c75a2ff66d406a. Checked 253 record(s); 0 failed.<br> |
| Completed batch history | passed | True | cmmmech:eudialyte-ore | Root executed; actual log /private/tmp/cmm-round52-final-history.log SHA256 6fab9a1f2f422f605fd0b242200596b27558aa866fa8b2dffabac4718cbce617. Checked 299 history record(s); 0 error(s).<br> |
| Completed batch render-check | passed | True | cmmmech:eudialyte-ore | Root executed; actual log /private/tmp/cmm-round52-final-render-check.log SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Ore feed versus pure mineral and commodity

identity: supported. Targets: cmmmech:eudialyte-ore.

A source-qualified geological feed is defensible without a pure-species identifier, inferred grade or inherited criticality.

### Culture-associated leaching under qualified conditions

evidence: supported. Targets: cmmmech:eudialyte-ore.

Reported inoculated acidification and greater solution concentrations support the narrow observation; chemistry-mismatched controls and analytical issues prevent stronger causal, quantitative recovery or scale claims.

### Actual sources, review state and required gates

provenance: supported. Targets: cmmmech:eudialyte-ore.

Primary thesis evidence is accurately identified as such, original relevant graphics were independently inspected, and final bytes/history pass completed required checks.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://doi.org/10.7488/era/834; Original217-page Edinburgh thesis; experimental Chapter4 text, Figures4.5.2.1 and4.5.3.1-6 and4.5.4.1-2 and4.5.5.1-2; relevant Chapter7 methods/Section7.2 equations. Original figure pages independently viewed. | supports | Natural Ilimaussaq ore is jaw-crushed and ground. Culture-associated acidification and solution mobilization exceed the mild uninoculated arm;2M nitric/sulfuric acids extract substantially more. Dissolved concentrations and downstream partitioning are not ore-to-product yields. |
| conflicts | /private/tmp/cmm-round52-eudialyte-research/raw/hunter2020-thesis.pdf; Abstract versus Section7.4.1; Sections4.5.1,4.5.3,4.5.5 and7.4.9; original pages149,154,177,182. | supports | The record retains abstract thiooxidans versus body ferrooxidans, stated stock-molarity inconsistency,562/568nm disagreement, malformed iron calibration/equations, mass-ratio versus atomic-stoichiometry inference, and actual acid/nitrate adjustment despite no-adjustment rhetoric. These limitations justify narrow qualitative claims. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Current NCBI species entry independently opened during review. | supports | NCBITaxon920 maps Acidithiobacillus ferrooxidans at species level. It cannot authenticate NCIMB10435 or resolve which organism was actually used. |
| archive | https://era.ed.ac.uk/bitstreams/f4ed3ae2-174e-40a0-b60d-7f9ab0de1e3e/download; Actual original ZIP inventory;69members including59files. Curator complete decodable-text/seven-workbook relevance screening separately inspected. | supports | Member names and documented screening concern computational ionic-liquid work. Reviewer independently verified ZIP and all74 retained raw-artifact hashes. No independent reproduction of unrelated simulations or fresh all-cell workbook screening claimed. |
| provenance | research/sources/round52-eudialyte/20261012T091948Z-source-investigation.json; Paired source dossier, frozen record, canonical CREATE and inline event; native inspection before assessment and final dossier capture. | supports | Record and history reflect actual new curation with codex/GPT-6 metadata; the reviewer authored allanite, not this record. All captured input hashes match. Source access and binary-search limits are explicit. |
| search | /private/tmp/cmm-round52-eudialyte-review/evidence-proof.json; Independent bounded hidden/ignored-inclusive search and raw-hash proof, plus live exact DOI correction/erratum and Hunter/eudialyte/bioleaching/ferrooxidans queries. | supports | No duplicate maintained ore owner or applicable correction surfaced within this scope. DOI web-open itself errored; the official migrated landing was returned by search and the complete curator-acquired original is independently inspected. Unrelated search hits are not scientific evidence. |
| gates | /private/tmp/cmm-round52-final-terminal.json; Actual completed just check, nonempty, history and render-check logs. | supports | All required batch commands returned zero and logs match recorded SHA256; this is structural validation, not proof of experimental truth. |

## Limits And Additional Notes

- Thesis evidence is not a peer-reviewed journal article; organism identity is internally inconsistent and stock authentication remains unavailable.
- Feed mineralogy, grade, particle distribution and whole-process mass balance are unresolved.
- Biological and abiotic pH histories differ; strong-acid comparisons outperform the microbial arm.
- Printed analytical equations and wavelengths limit exact iron oxidation and quantitative extraction claims.
- No full scientific audit of unrelated computational chapters or independent all-cell workbook rerun; the curator relevance screen was inspected as such.
- Hidden/ignored-inclusive dedup and notice searches are bounded; unavailable historical roots and unextracted binaries preclude universal absence claims.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T092440Z-eudialyte-ore-round52-science
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of eudialyte ore
started_at: '2026-10-12T09:18:55.861107Z'
finished_at: '2026-10-12T09:24:40.352428Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record/history/dossier authored by /root/round43_hardmetal.
    Root curated the separate allanite record, captured native inputs and independently
    inspected original thesis graphics/text, taxon and source provenance without editing
    eudialyte.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The source-qualified ore and narrow culture-associated laboratory leaching
  claim are supported. No corrective finding in the reviewed state; organism, analytical,
  denominator and control limitations are retained.
source:
  git_revision: 79ed7d69ea654d1b67bbf74bb931ff70c4c6913e
  state: working_tree
  inputs:
  - path: data/records/eudialyte-ore.yaml
    sha256: ddecf732576b7bd3d791b9bb2d90529a202cae0bcfeb0caefbf8d0e6a6e39f5e
    role: target
  - path: history/records/eudialyte-ore/2026-10-12T091728Z-codex-d2511a.yaml
    sha256: 55610e308856722c110b9b3445ea423cd082f2a1d54b0566ef89d60aec4411c6
    role: context
  - path: research/sources/round52-eudialyte/20261012T091948Z-source-investigation.json
    sha256: 105483c8d2807bde3dac6c4bb1e78f87132f6b1310c3501cff6188ca390a2c0f
    role: context
  - path: research/sources/round52-eudialyte/20261012T091948Z-source-investigation.md
    sha256: 11f61530cceb3a3b24b1fe10548d102b842019b343c4caa49e430d949543fc10
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:eudialyte-ore
  path: data/records/eudialyte-ore.yaml
  label: Eudialyte ore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eudialyte-ore.yaml
    role: maintained
scope:
  description: All eudialyte-ore fields, CREATE history, paired dossier and schema;
    Chapter4 experiment and relevant general methods, taxon, original graphics and
    archive scope.
  selection: Independent assigned exact-target review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:eudialyte-ore
  exclusions:
  - target: Unrelated thesis modeling chapters, unavailable raw Chapter4 assay table
      and Hedrich2023
    reason: Not claimed as independent replication, recovered source gap or reproduced
      experimental data.
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/eudialyte-ore.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-ore
  summary: Root reviewer executed; one record checked, zero failed. Log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Completed batch batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-ore
  summary: 'Root executed; actual log /private/tmp/cmm-round52-final-batch.log SHA256
    98c9a3c5b08e68cefe8dc71e984bff78ca3b8320a49f048a43ca0402489f5685. uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 179.41s (0:02:59)

    Checked 253 record(s); 0 failed.

    Checked 299 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Completed batch nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-ore
  summary: 'Root executed; actual log /private/tmp/cmm-round52-final-nonempty.log
    SHA256 4a50f2f93e44bfb9e2561b166775c22abe8b3fb410bdcd90d2c75a2ff66d406a. Checked
    253 record(s); 0 failed.

    '
- check_id: history
  name: Completed batch history
  command: uv run --locked cmmmech validate-history --base 79ed7d69ea654d1b67bbf74bb931ff70c4c6913e
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-ore
  summary: 'Root executed; actual log /private/tmp/cmm-round52-final-history.log SHA256
    6fab9a1f2f422f605fd0b242200596b27558aa866fa8b2dffabac4718cbce617. Checked 299
    history record(s); 0 error(s).

    '
- check_id: render-check
  name: Completed batch render-check
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:eudialyte-ore
  summary: 'Root executed; actual log /private/tmp/cmm-round52-final-render-check.log
    SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run
    python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.7488/era/834
  locator: Original217-page Edinburgh thesis; experimental Chapter4 text, Figures4.5.2.1
    and4.5.3.1-6 and4.5.4.1-2 and4.5.5.1-2; relevant Chapter7 methods/Section7.2 equations.
    Original figure pages independently viewed.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: Natural Ilimaussaq ore is jaw-crushed and ground. Culture-associated acidification
    and solution mobilization exceed the mild uninoculated arm;2M nitric/sulfuric
    acids extract substantially more. Dissolved concentrations and downstream partitioning
    are not ore-to-product yields.
  snapshot_sha256: a09ea4909d1c2a261a8d1f85839309e773cec675362afebdcd47c3333643640d
- evidence_id: conflicts
  kind: primary_source
  reference: /private/tmp/cmm-round52-eudialyte-research/raw/hunter2020-thesis.pdf
  locator: Abstract versus Section7.4.1; Sections4.5.1,4.5.3,4.5.5 and7.4.9; original
    pages149,154,177,182.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: The record retains abstract thiooxidans versus body ferrooxidans, stated
    stock-molarity inconsistency,562/568nm disagreement, malformed iron calibration/equations,
    mass-ratio versus atomic-stoichiometry inference, and actual acid/nitrate adjustment
    despite no-adjustment rhetoric. These limitations justify narrow qualitative claims.
  snapshot_sha256: a09ea4909d1c2a261a8d1f85839309e773cec675362afebdcd47c3333643640d
- evidence_id: taxon
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Current NCBI species entry independently opened during review.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: NCBITaxon920 maps Acidithiobacillus ferrooxidans at species level. It cannot
    authenticate NCIMB10435 or resolve which organism was actually used.
- evidence_id: archive
  kind: primary_source
  reference: https://era.ed.ac.uk/bitstreams/f4ed3ae2-174e-40a0-b60d-7f9ab0de1e3e/download
  locator: Actual original ZIP inventory;69members including59files. Curator complete
    decodable-text/seven-workbook relevance screening separately inspected.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: Member names and documented screening concern computational ionic-liquid
    work. Reviewer independently verified ZIP and all74 retained raw-artifact hashes.
    No independent reproduction of unrelated simulations or fresh all-cell workbook
    screening claimed.
  snapshot_sha256: ff7592e32c2f5c51720d7d2d4c0584129cb6f1c959a436c499f4640e098d9c12
- evidence_id: provenance
  kind: record_content
  reference: research/sources/round52-eudialyte/20261012T091948Z-source-investigation.json
  locator: Paired source dossier, frozen record, canonical CREATE and inline event;
    native inspection before assessment and final dossier capture.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: Record and history reflect actual new curation with codex/GPT-6 metadata;
    the reviewer authored allanite, not this record. All captured input hashes match.
    Source access and binary-search limits are explicit.
  snapshot_sha256: 105483c8d2807bde3dac6c4bb1e78f87132f6b1310c3501cff6188ca390a2c0f
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round52-eudialyte-review/evidence-proof.json
  locator: Independent bounded hidden/ignored-inclusive search and raw-hash proof,
    plus live exact DOI correction/erratum and Hunter/eudialyte/bioleaching/ferrooxidans
    queries.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: No duplicate maintained ore owner or applicable correction surfaced within
    this scope. DOI web-open itself errored; the official migrated landing was returned
    by search and the complete curator-acquired original is independently inspected.
    Unrelated search hits are not scientific evidence.
  search_scope: Current/original records,research,reviews,history plus explicit round52
    source root; rg --no-ignore --hidden --follow. Broader curator190-root receipt
    inspected separately, nine unavailable roots and unextracted binary contents remain
    limitations. Web first returned relevance sets, no exhaustive notice claim.
  snapshot_sha256: 8372c54c47021e16d1a9e6d30c6c9eeeb5517d324e6864a12c1d62a05e7910bd
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round52-final-terminal.json
  locator: Actual completed just check, nonempty, history and render-check logs.
  accessed_at: '2026-10-12T09:24:40.352428Z'
  support: supports
  summary: All required batch commands returned zero and logs match recorded SHA256;
    this is structural validation, not proof of experimental truth.
  snapshot_sha256: 5b99f9d171be5aa6cf30e680ccb15098c90864664c7a773aa6e57fa27ce0ab40
assessments:
- assessment_id: identity
  area: identity
  topic: Ore feed versus pure mineral and commodity
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-ore
  evidence_ids:
  - primary
  - provenance
  - search
  summary: A source-qualified geological feed is defensible without a pure-species
    identifier, inferred grade or inherited criticality.
  dimensions:
  - name: material_form
    value: Ilimaussaq eudialyte ore; primary_resource
    definition: Crushed/ground heterogeneous natural feed, not authenticated pure
      mineral or upgraded concentrate
    evidence_ids:
    - primary
  - name: criticality
    value: No jurisdiction/list/edition claim
    definition: No designation inherited from elemental constituents
    evidence_ids:
    - provenance
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated leaching under qualified conditions
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-ore
  evidence_ids:
  - primary
  - conflicts
  - taxon
  summary: Reported inoculated acidification and greater solution concentrations support
    the narrow observation; chemistry-mismatched controls and analytical issues prevent
    stronger causal, quantitative recovery or scale claims.
  dimensions:
  - name: organism_and_biomass
    value: Live inoculated culture, methods-labelled A.ferrooxidans NCIMB10435; abstract
      says A.thiooxidans
    definition: Species mapping only; experimental stock and contradictory name unresolved
    evidence_ids:
    - primary
    - conflicts
    - taxon
  - name: substrate_conditions_controls
    value: Ground autoclaved ore in125mL iron/acid medium;0.50g time course and1.00g
      chemical comparison
    definition: Distinct loading arms; no matched-pH trajectory or resolved culture
      density/agitation set point
    evidence_ids:
    - primary
  - name: outcome_and_scale
    value: Laboratory filtered aqueous mobilization; stronger2M acid comparators;
      separate chemical partitioning
    definition: No isolated product, feed-to-product mass balance, pH-independent
      microbial advantage or industrial deployment
    evidence_ids:
    - primary
    - conflicts
- assessment_id: provenance
  area: provenance
  topic: Actual sources, review state and required gates
  outcome: supported
  target_ids:
  - cmmmech:eudialyte-ore
  evidence_ids:
  - provenance
  - archive
  - search
  - gates
  summary: Primary thesis evidence is accurately identified as such, original relevant
    graphics were independently inspected, and final bytes/history pass completed
    required checks.
findings: []
actions: []
limitations:
- Thesis evidence is not a peer-reviewed journal article; organism identity is internally
  inconsistent and stock authentication remains unavailable.
- Feed mineralogy, grade, particle distribution and whole-process mass balance are
  unresolved.
- Biological and abiotic pH histories differ; strong-acid comparisons outperform the
  microbial arm.
- Printed analytical equations and wavelengths limit exact iron oxidation and quantitative
  extraction claims.
- No full scientific audit of unrelated computational chapters or independent all-cell
  workbook rerun; the curator relevance screen was inspected as such.
- Hidden/ignored-inclusive dedup and notice searches are bounded; unavailable historical
  roots and unextracted binaries preclude universal absence claims.
tags:
- round52
- eudialyte
- independent
- scientific
```
