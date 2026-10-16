# Independent scientific review of Uranopilite

- Review: 20261016T093814Z-uranopilite-round116-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T09:27:45.770219Z
- Finished UTC: 2026-10-16T09:38:14.726623Z
- Reviewer: codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Natural identity and bounded characterization are supported; no corrective owner defect found. Source contradictions and unavailable experimental evidence remain explicit.

## Scope And Provenance

Entire owner and linked history with independent claim-level review of relevant primary sections; no experimental replication or structure re-refinement.

Selection: Two uranium records assigned independently, each captured natively before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5d3c48e255705e269096c43cf1c5508a5178ecc1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:uranopilite | data/records/uranopilite.yaml | maintained | Uranopilite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Final batch check | passed | True | cmmmech:uranopilite | Verified terminal receipt, log hash and unchanged current bytes. |
| Final batch check | passed | True | cmmmech:uranopilite | Verified terminal receipt, log hash and unchanged current bytes. |
| Final batch check | passed | True | cmmmech:uranopilite | Verified terminal receipt, log hash and unchanged current bytes. |
| Final batch check | passed | True | cmmmech:uranopilite | Verified terminal receipt, log hash and unchanged current bytes. |

## Scientific And Domain Assessments

### Natural mineral species and authority

identity: supported. Targets: cmmmech:uranopilite.

Current mineral identity is supported; elemental, group, synthetic and commodity scopes remain distinct.

### Primary support and source contradictions

evidence: supported. Targets: cmmmech:uranopilite.

The natural species and structure are supported, with inferred H bonding, two-crystal/twinning limitations and model discrepancies disclosed. Fourteen-water Table15 values are calculated, not a separate water assay. Historical formula repartition is correctly distinguished from dehydration. Thermal claims remain deferred.

### History, bounded searches and checks

provenance: supported. Targets: cmmmech:uranopilite.

Actual CREATE provenance and final native-inspected hashes retained; structural validation does not establish scientific truth.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/uranopilite.yaml; Entire native-inspected record; retained /private/tmp/CMMMech-expansion-round116-20261016/data/records/uranopilite.yaml | supports | Final identity, sources, history, explicit exclusions and scientific qualifiers independently checked. |
| history0 | history/records/uranopilite/2026-10-16T092606Z-codex-2b5138.yaml; Entire canonical session; retained /private/tmp/CMMMech-expansion-round116-20261016/history/records/uranopilite/2026-10-16T092606Z-codex-2b5138.yaml | supports | Actual current CREATE event, target and actor/model/tool agree with the distinct inline event. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Page224 uranopilite and page242 zippeite rows visually inspected; definitions on page1; retained /private/tmp/cmm-round116-uranium-research/ima2026-09.pdf | supports | Uranopilite is G1882 with six coordinated/eight interstitial waters. Zippeite is Rd1971-029a with K2 and four waters. No elemental criticality is inherited. |
| natural | https://doi.org/10.3190/jgeosci.171; Locality/methods223-225, uranopilite234-235 and237-238, zippeite242-244 and247, interpretation249-250; original Tables15-17/29 and Figures13-14 visually checked; retained /private/tmp/cmm-round116-uranium-research/plasil2014.pdf | supports | Primary natural-specimen study supports bounded mineral identity and occurrence. Formation timing, pH and cation sources are geological interpretations; no controlled microbial conversion or recovery experiment is presented. |
| structure | https://doi.org/10.2113/gscanmin.39.4.1139; Complete original text; methods1140, Tables1-6 and Figures1-4 on1140-1145 visually checked; retained /private/tmp/cmm-round116-uranium-research/uranopilite2001.pdf | supports | Specimen89612 contains two microcrystals. Overlap-affected reflections were removed before reported R1=7.0%. Six coordinated/eight interstitial waters and sulfate chains follow structural/bond-valence arguments; H positions were not directly found. Earlier hydroxyl/water formula has identical elemental totals. |
| deposit | https://www.jgeosci.org/supplementary/jgeosci.171_plasil_uranopilite.cif; Formula, refinement-count/R-factor/density and beta metadata independently compared with Tables16-17; retained /private/tmp/cmm-round116-uranium-research/plasil2014-uranopilite.cif | supports | The CIF gives H-free O37.895 S1 U6,219parameters,11370reflections,R1gt0.0995 and density4.0194, while the printed table differs. The owner correctly avoids choosing disputed refinement metrics or measuring H from the CIF. |
| notices | Independent DOI/title correction and identity queries; Exact2014 and2001 DOI with correction/erratum/retraction plus natural/synthetic zippeite formula query; retained /private/tmp/cmm-round116-uranium-independent-web.json | context_only | Returned results did not establish an applicable correction or retraction; they are not an exhaustive notice search. Primary sources establish the claims. |
| dedup | Bounded current-record search; rg --hidden --no-ignore --follow with both names and primary DOIs over data/records; retained /private/tmp/cmm-round116-uranium-independent-dedup.txt | context_only | 29 matches belonged to these two dedicated owners. Curator broader research/reviews/raw searches are separately retained. |
| batch | Final batch gates; Actual terminal receipt and retained log; retained /private/tmp/cmm-round116-final-gates.json | supports | Four final checks passed on unchanged owner/history/schema inputs. |

## Limits And Additional Notes

- No structure re-refinement was performed. The2001 deposited structure-factor file was not acquired;2014 paper/CIF differences remain unresolved.
- The2020 thermal SI was unavailable to the curator; no experimental thermal transition is accepted.
- Independent agent review is not external human peer review. Not every page of the31-page2014 multispecies study was visually reread.
- Bounded searches cannot prove absence of later corrections or conflicting studies.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T093814Z-uranopilite-round116-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Uranopilite
started_at: '2026-10-16T09:27:45.770219Z'
finished_at: '2026-10-16T09:38:14.726623Z'
reviewer:
  identity: codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Uranium agent authored the record/history. Root independently
    inspected final bytes, primary methods/results, relevant original figures/tables,
    authority rows and deposited metadata, without editing these owners.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Natural identity and bounded characterization are supported; no corrective
  owner defect found. Source contradictions and unavailable experimental evidence
  remain explicit.
source:
  git_revision: 5d3c48e255705e269096c43cf1c5508a5178ecc1
  state: working_tree
  inputs:
  - path: data/records/uranopilite.yaml
    sha256: 4f149c8fc021ebde419c0c308b632b0800885539fd9dc2ca44957d63cf4095c8
    role: target
targets:
- target_id: cmmmech:uranopilite
  path: data/records/uranopilite.yaml
  label: Uranopilite
  kind: maintained
  ownership_note: Maintained scientific YAML owned by CultureBotAI/CMMMech.
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/uranopilite.yaml
    role: maintained_owner
scope:
  description: Entire owner and linked history with independent claim-level review
    of relevant primary sections; no experimental replication or structure re-refinement.
  selection: Two uranium records assigned independently, each captured natively before
    judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:uranopilite
checks:
- check_id: gate0
  name: Final batch check
  required: true
  status: passed
  command: just check
  exit_code: 0
  summary: Verified terminal receipt, log hash and unchanged current bytes.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - batch
- check_id: gate1
  name: Final batch check
  required: true
  status: passed
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  summary: Verified terminal receipt, log hash and unchanged current bytes.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - batch
- check_id: gate2
  name: Final batch check
  required: true
  status: passed
  command: uv run --locked cmmmech validate-history --base 5d3c48e255705e269096c43cf1c5508a5178ecc1
  exit_code: 0
  summary: Verified terminal receipt, log hash and unchanged current bytes.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - batch
- check_id: gate3
  name: Final batch check
  required: true
  status: passed
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  summary: Verified terminal receipt, log hash and unchanged current bytes.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/uranopilite.yaml
  locator: Entire native-inspected record; retained /private/tmp/CMMMech-expansion-round116-20261016/data/records/uranopilite.yaml
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 4f149c8fc021ebde419c0c308b632b0800885539fd9dc2ca44957d63cf4095c8
  support: supports
  summary: Final identity, sources, history, explicit exclusions and scientific qualifiers
    independently checked.
- evidence_id: history0
  kind: record_content
  reference: history/records/uranopilite/2026-10-16T092606Z-codex-2b5138.yaml
  locator: Entire canonical session; retained /private/tmp/CMMMech-expansion-round116-20261016/history/records/uranopilite/2026-10-16T092606Z-codex-2b5138.yaml
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 0abe03b77f20eed92e9bbfdd290e3ab0be8538e316a46df76178e2e1f4a3b1c9
  support: supports
  summary: Actual current CREATE event, target and actor/model/tool agree with the
    distinct inline event.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Page224 uranopilite and page242 zippeite rows visually inspected; definitions
    on page1; retained /private/tmp/cmm-round116-uranium-research/ima2026-09.pdf
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  support: supports
  summary: Uranopilite is G1882 with six coordinated/eight interstitial waters. Zippeite
    is Rd1971-029a with K2 and four waters. No elemental criticality is inherited.
- evidence_id: natural
  kind: primary_source
  reference: https://doi.org/10.3190/jgeosci.171
  locator: Locality/methods223-225, uranopilite234-235 and237-238, zippeite242-244
    and247, interpretation249-250; original Tables15-17/29 and Figures13-14 visually
    checked; retained /private/tmp/cmm-round116-uranium-research/plasil2014.pdf
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 084679ecb2056457e21692d8b4f4f3fe6943cf49b215c3bb59204b4e1ba810c7
  support: supports
  summary: Primary natural-specimen study supports bounded mineral identity and occurrence.
    Formation timing, pH and cation sources are geological interpretations; no controlled
    microbial conversion or recovery experiment is presented.
- evidence_id: structure
  kind: primary_source
  reference: https://doi.org/10.2113/gscanmin.39.4.1139
  locator: Complete original text; methods1140, Tables1-6 and Figures1-4 on1140-1145
    visually checked; retained /private/tmp/cmm-round116-uranium-research/uranopilite2001.pdf
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 6ef267253f80fe5aa23137bf4a4ae510a0c5d5821bbb26ab997e30bb6ab10e65
  support: supports
  summary: Specimen89612 contains two microcrystals. Overlap-affected reflections
    were removed before reported R1=7.0%. Six coordinated/eight interstitial waters
    and sulfate chains follow structural/bond-valence arguments; H positions were
    not directly found. Earlier hydroxyl/water formula has identical elemental totals.
- evidence_id: deposit
  kind: primary_source
  reference: https://www.jgeosci.org/supplementary/jgeosci.171_plasil_uranopilite.cif
  locator: Formula, refinement-count/R-factor/density and beta metadata independently
    compared with Tables16-17; retained /private/tmp/cmm-round116-uranium-research/plasil2014-uranopilite.cif
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 8a609df8ce4f49be92af0fee524820549356d87e1f9bda5ca53cedb342eebf35
  support: supports
  summary: The CIF gives H-free O37.895 S1 U6,219parameters,11370reflections,R1gt0.0995
    and density4.0194, while the printed table differs. The owner correctly avoids
    choosing disputed refinement metrics or measuring H from the CIF.
- evidence_id: notices
  kind: search
  reference: Independent DOI/title correction and identity queries
  locator: Exact2014 and2001 DOI with correction/erratum/retraction plus natural/synthetic
    zippeite formula query; retained /private/tmp/cmm-round116-uranium-independent-web.json
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: 22de877cead705d208eb0da1238d37ba48fd326ea0f23f4b7235b9005c1394e4
  support: context_only
  summary: Returned results did not establish an applicable correction or retraction;
    they are not an exhaustive notice search. Primary sources establish the claims.
  search_scope: Initial live returned results for three queries on2026-10-16; no global
    absence assertion.
- evidence_id: dedup
  kind: search
  reference: Bounded current-record search
  locator: rg --hidden --no-ignore --follow with both names and primary DOIs over
    data/records; retained /private/tmp/cmm-round116-uranium-independent-dedup.txt
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: eb91bccefb482fea80dfff7d50031618662c77a2bf64b76fdfd07bacae827a34
  support: context_only
  summary: 29 matches belonged to these two dedicated owners. Curator broader research/reviews/raw
    searches are separately retained.
  search_scope: Current data/records including hidden/ignored and followed symlinks;
    not a machine-wide inventory.
- evidence_id: batch
  kind: validation
  reference: Final batch gates
  locator: Actual terminal receipt and retained log; retained /private/tmp/cmm-round116-final-gates.json
  accessed_at: '2026-10-16T09:38:14.726623Z'
  snapshot_sha256: e38ebb987e57047c4f30e4e0b7583c4bdfafbc987656a9bfbe765fefcfeadc3d
  support: supports
  summary: Four final checks passed on unchanged owner/history/schema inputs.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural mineral species and authority
  outcome: supported
  summary: Current mineral identity is supported; elemental, group, synthetic and
    commodity scopes remain distinct.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - owner
  - ima
  - natural
  - structure
- assessment_id: science
  area: evidence
  topic: Primary support and source contradictions
  outcome: supported
  summary: The natural species and structure are supported, with inferred H bonding,
    two-crystal/twinning limitations and model discrepancies disclosed. Fourteen-water
    Table15 values are calculated, not a separate water assay. Historical formula
    repartition is correctly distinguished from dehydration. Thermal claims remain
    deferred.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - owner
  - natural
  - structure
  - deposit
- assessment_id: provenance
  area: provenance
  topic: History, bounded searches and checks
  outcome: supported
  summary: Actual CREATE provenance and final native-inspected hashes retained; structural
    validation does not establish scientific truth.
  target_ids:
  - cmmmech:uranopilite
  evidence_ids:
  - history0
  - dedup
  - notices
  - batch
findings: []
actions: []
limitations:
- No structure re-refinement was performed. The2001 deposited structure-factor file
  was not acquired;2014 paper/CIF differences remain unresolved.
- The2020 thermal SI was unavailable to the curator; no experimental thermal transition
  is accepted.
- Independent agent review is not external human peer review. Not every page of the31-page2014
  multispecies study was visually reread.
- Bounded searches cannot prove absence of later corrections or conflicting studies.
```
