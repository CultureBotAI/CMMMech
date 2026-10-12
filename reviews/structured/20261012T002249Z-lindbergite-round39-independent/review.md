# Independent adversarial review of the Wei2012 lindbergite extension

- Review: 20261012T002249Z-lindbergite-round39-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T00:18:18.740603Z
- Finished UTC: 2026-10-12T00:22:49.289495Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The additional source-assigned phase-formation arm is defensible with preparation, control, strain and yield limits explicit; no corrective defect identified.

## Scope And Provenance

Entire current lindbergite record; fresh primary review of Wei2012 addition plus exact preserved-field assessment against earlier scientific review.

Selection: Independent assessment of another agent’s material record extension.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bf1f7000014287805ea7c44341a3ce9e112e6689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:lindbergite | data/records/lindbergite.yaml | maintained | Lindbergite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:lindbergite | Checked 1 record(s); 0 failed.; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Completed cohort batch | passed | True | cmmmech:lindbergite | uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 186.10s (0:03:06)<br>Checked 210 record(s); 0 failed.<br>Checked 242 history record(s); 0 error(s).; log SHA256 97728f73d7f6f23423c32ceb6fe3e9688ef9fc83a4fbbdb185675bcafef84793 |
| Completed cohort nonempty | passed | True | cmmmech:lindbergite | Checked 210 record(s); 0 failed.; log SHA256 8088527a34a0b38dfa3a5e7dc9ba7acbb2db5645f2022a0277c19fbc93b5c23f |
| Completed cohort history | passed | True | cmmmech:lindbergite | Checked 242 history record(s); 0 error(s).; log SHA256 248ff272d20e51f3c8767e9de06bb1481564fc01d11b353d8e0570f1628918e3 |

## Scientific And Domain Assessments

### Mineral and material boundaries

identity: supported. Targets: cmmmech:lindbergite.

Approved monoclinic lindbergite remains distinct from element Mn, synthetic sodium-birnessite feed, mixed natural nodules, orthorhombic dihydrate and unnamed trihydrate. No inherited criticality is asserted.

### Organism, feed, pretreatment and incubation

evidence: supported. Targets: cmmmech:lindbergite.

The living unaccessioned S.himantioides isolate, synthetic Na-birnessite,0.5%w/v,20cm3MEA,90mm plate,84mm membrane,5mm leading-edge disk from≥14-dayculture,25C dark triplicates agree with original methods. TaxID is species-only. Table3 pH2.93 versus initial7.26 is25-day surface sampling, not5/23-day diffraction-harvest pH.

### Recovered diffraction assignment

evidence: supported. Targets: cmmmech:lindbergite.

Figure4 explicitly names lindbergite and compares mixed5-day and dihydrate-only23-day recovered crystals. Figure2K/L morphology does not prove polymorph/hydration.80C extraction and vacuum drying, absent refined cells/water assay/phase fractions, and ambiguous analytical-versus-biological determinations are correctly retained.

### Mechanistic attribution and measured outcomes

evidence: supported. Targets: cmmmech:lindbergite.

Growth controls and abiotic morphology do not form a sterile time-matched diffraction series.50µL0.5M acid wells are separate unmatched chemical assays; halo formation is not lindbergite confirmation. No measured fungal oxalate, killed-biomass series, mass balance or isolated product yield establishes an exclusive pathway. Figure6 is conceptual.

### Existing evidence and independent review scope

provenance: supported. Targets: cmmmech:lindbergite.

Fresh scientific assessment covers Wei2012. All earlier scientific claims and old provenance reconstruct exactly from trusted base and remain within the previous independent review; they are not represented as freshly reread literature. New sidecar and inlineEDIT describe only the added arm.

### Contradictions and search limits

evidence: supported. Targets: cmmmech:lindbergite.

Pagination discrepancy and preparation/timing ambiguities are explicit. The prior orthorhombic Farkas assignment remains context-only. Bounded notice search found no affecting notice within returned results, without claiming exhaustive absence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/lindbergite.yaml; All current fields after native inspect | supports | Frozen final bytes independently read; existing claims compared to trusted base and earlier review. |
| wei | https://doi.org/10.1111/j.1462-2920.2012.02776.x; Complete nine-page primary PDF, all six figures and three tables, printed1744–1752; especially Figures2/4/5 and Experimental procedures | supports | Root independently read full text and visually inspected all nine original pages. Figure4 expressly assigns dihydrate lindbergite at5/23days, with a mixed trihydrate at5days. Hot-water extraction and vacuum drying prevent asserting a demonstrated live-culture hydration conversion. Publicly indexed mirror copy was acquired by the curator; ownership/licence not authenticated and raw PDF remains outside Git. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Retained original page126 Lindbergite row | supports | Independent visual recheck confirms approved Mn(C2O4)(H2O)2, IMA2003-029. Reused authority snapshot, not a new download. |
| handbook | https://www.handbookofmineralogy.org/pdfs/Lindbergite.pdf; Entire original one-page entry, revision2/8/2021 | supports | Independently viewed retained original: monoclinic C2/c, distinct from orthorhombic dihydrate and falottaite. Authority does not authenticate experimental crystals. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/Serpula%20himantioides/dataset_report; Fresh curator-acquired JSON current scientific name/rank/TaxID | supports | Independently parsed: Serpula himantioides species80602. Root web-reader request failed; shared current authority JSON inspected. Does not authenticate the unaccessioned N.White isolate. |
| prior | reviews/structured/20261011T230525Z-lindbergite-round37-independent/review.yaml; Prior complete independent scientific review and exact base scientific fields | supports | Root authored the earlier independent review of Ferrier2019 and Farkas2020. An independent semantic reconstruction in this round removed only the two added sources, new mechanism, inline EDIT and new history reference and exactly recovered the trusted-base YAML values. Prior canonical sidecar bytes are unchanged. Earlier primary papers were not freshly reassessed in this round. |
| history | history/records/lindbergite/2026-10-12T001526Z-codex-997e03.yaml; New canonical EDIT and separate inline event | supports | Actual actor/model/tool, target, timestamps and completed evidence work agree with the added mechanism; old history preserved. |
| search | Root web.run and rg on2026-10-12; DOI notices, phase conflicts, current duplicates and metadata | supports | Exact-DOI notice query and phase-context query returned no affecting correction/retraction in inspected sets. PubMed/publisher metadata end1753, while Hutton/Dundee and complete original end1752; record preserves discrepancy. Existing prior Farkas crystallographic conflict remains unchanged. Hidden/ignored local search identifies existing owner and source handoffs, not a duplicate material. |
| proof | /private/tmp/cmm-round39-lindbergite-review/independent-checks.json; Independent preserved-field reconstruction and bounded duplicate search receipt | supports | Root verified exact semantic preservation of all prior fields and byte preservation of old history; new study belongs in the existing record. |

## Limits And Additional Notes

- No wet in-culture diffraction, matched preparation series, phase-specific mass balance or industrial demonstration. Culture accession and oxalate measurements remain unavailable.
- Primary PDF is a publicly indexed copy with unknown mirror ownership and no established redistribution licence. All nine original pages complete the printed article; bibliographic end-page discrepancy retained.
- Prior papers were not freshly re-reviewed; their unchanged fields and earlier independent scientific observation are explicit. Notice and local searches are bounded. Root direct NCBI web-reader request failed; current shared JSON was parsed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T002249Z-lindbergite-round39-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent adversarial review of the Wei2012 lindbergite extension
started_at: '2026-10-12T00:18:18.740603Z'
finished_at: '2026-10-12T00:22:49.289495Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The new extension and dossier were authored by /root/round27_superalloy.
    Root did not author/edit this record; it specified the existing record owner and
    review scope. Shared acquired primary artifacts were independently inspected.
    Root authored the prior round37 independent review and sibling falottaite, disclosed
    here; earlier claims are assessed by exact preservation and that earlier review.
    Root authored other brown-rot feed records in this cohort, which separate agents
    review. Native inspect preceded judgment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The additional source-assigned phase-formation arm is defensible with preparation,
  control, strain and yield limits explicit; no corrective defect identified.
source:
  git_revision: bf1f7000014287805ea7c44341a3ce9e112e6689
  state: working_tree
  inputs:
  - path: data/records/lindbergite.yaml
    sha256: f345183f653b44e65279806043716ff679356d55c52595c05a28d26f1a56311b
    role: target
  - path: history/records/lindbergite/2026-10-11T225957Z-codex-f222f6.yaml
    sha256: c76f5fc967279b20ae35314f2c2f535a1f29ec459f93df64a55252f1bfd5cb0b
    role: context
  - path: history/records/lindbergite/2026-10-12T001526Z-codex-997e03.yaml
    sha256: d084176fe0237605cc6861564ad4cb8670ea3f53bfbe30069d257a497ef61a7b
    role: context
  - path: reviews/structured/20261011T230525Z-lindbergite-round37-independent/review.yaml
    sha256: c95b7d86daed1c331427331962d40349d2780023bb344f9799903cd97089152a
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Entire current lindbergite record; fresh primary review of Wei2012
    addition plus exact preserved-field assessment against earlier scientific review.
  selection: Independent assessment of another agent’s material record extension.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:lindbergite
  exclusions:
  - target: Fresh re-review of unchanged Ferrier2019 and Farkas2020 literature
    reason: Verified prior claims unchanged and linked exact earlier independent review;
      no claim of fresh primary reassessment.
  - target: New crystallographic or biological experiments
    reason: Original raw diffraction/strain material unavailable; retained source-assigned
      mineral and preparation limitations.
targets:
- target_id: cmmmech:lindbergite
  path: data/records/lindbergite.yaml
  label: Lindbergite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/lindbergite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/lindbergite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 1 record(s); 0 failed.; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:lindbergite
- check_id: batch
  name: Completed cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 186.10s (0:03:06)

    Checked 210 record(s); 0 failed.

    Checked 242 history record(s); 0 error(s).; log SHA256 97728f73d7f6f23423c32ceb6fe3e9688ef9fc83a4fbbdb185675bcafef84793'
  target_ids:
  - cmmmech:lindbergite
- check_id: nonempty
  name: Completed cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 210 record(s); 0 failed.; log SHA256 8088527a34a0b38dfa3a5e7dc9ba7acbb2db5645f2022a0277c19fbc93b5c23f
  target_ids:
  - cmmmech:lindbergite
- check_id: history
  name: Completed cohort history
  command: uv run --locked cmmmech validate-history --base bf1f7000014287805ea7c44341a3ce9e112e6689
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 242 history record(s); 0 error(s).; log SHA256 248ff272d20e51f3c8767e9de06bb1481564fc01d11b353d8e0570f1628918e3
  target_ids:
  - cmmmech:lindbergite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/lindbergite.yaml
  locator: All current fields after native inspect
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Frozen final bytes independently read; existing claims compared to trusted
    base and earlier review.
  snapshot_sha256: f345183f653b44e65279806043716ff679356d55c52595c05a28d26f1a56311b
- evidence_id: wei
  kind: primary_source
  reference: https://doi.org/10.1111/j.1462-2920.2012.02776.x
  locator: Complete nine-page primary PDF, all six figures and three tables, printed1744–1752;
    especially Figures2/4/5 and Experimental procedures
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Root independently read full text and visually inspected all nine original
    pages. Figure4 expressly assigns dihydrate lindbergite at5/23days, with a mixed
    trihydrate at5days. Hot-water extraction and vacuum drying prevent asserting a
    demonstrated live-culture hydration conversion. Publicly indexed mirror copy was
    acquired by the curator; ownership/licence not authenticated and raw PDF remains
    outside Git.
  snapshot_sha256: aa93ca545b5b192196a36112b79276fb47e12f9cd31a2cf520a06b79ec4b08ec
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Retained original page126 Lindbergite row
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Independent visual recheck confirms approved Mn(C2O4)(H2O)2, IMA2003-029.
    Reused authority snapshot, not a new download.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/Lindbergite.pdf
  locator: Entire original one-page entry, revision2/8/2021
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: 'Independently viewed retained original: monoclinic C2/c, distinct from
    orthorhombic dihydrate and falottaite. Authority does not authenticate experimental
    crystals.'
  snapshot_sha256: 27f1d14550498638367b512616910c87039f06aaf7a5b2f41490678feea623f0
- evidence_id: taxon
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/Serpula%20himantioides/dataset_report
  locator: Fresh curator-acquired JSON current scientific name/rank/TaxID
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: 'Independently parsed: Serpula himantioides species80602. Root web-reader
    request failed; shared current authority JSON inspected. Does not authenticate
    the unaccessioned N.White isolate.'
  snapshot_sha256: 3af26251e7d64026b156097d61aee326452f5552de5c542ecdfae2a0b6b1fbb4
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261011T230525Z-lindbergite-round37-independent/review.yaml
  locator: Prior complete independent scientific review and exact base scientific
    fields
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Root authored the earlier independent review of Ferrier2019 and Farkas2020.
    An independent semantic reconstruction in this round removed only the two added
    sources, new mechanism, inline EDIT and new history reference and exactly recovered
    the trusted-base YAML values. Prior canonical sidecar bytes are unchanged. Earlier
    primary papers were not freshly reassessed in this round.
  snapshot_sha256: c95b7d86daed1c331427331962d40349d2780023bb344f9799903cd97089152a
- evidence_id: history
  kind: record_content
  reference: history/records/lindbergite/2026-10-12T001526Z-codex-997e03.yaml
  locator: New canonical EDIT and separate inline event
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Actual actor/model/tool, target, timestamps and completed evidence work
    agree with the added mechanism; old history preserved.
  snapshot_sha256: d084176fe0237605cc6861564ad4cb8670ea3f53bfbe30069d257a497ef61a7b
- evidence_id: search
  kind: search
  reference: Root web.run and rg on2026-10-12
  locator: DOI notices, phase conflicts, current duplicates and metadata
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Exact-DOI notice query and phase-context query returned no affecting correction/retraction
    in inspected sets. PubMed/publisher metadata end1753, while Hutton/Dundee and
    complete original end1752; record preserves discrepancy. Existing prior Farkas
    crystallographic conflict remains unchanged. Hidden/ignored local search identifies
    existing owner and source handoffs, not a duplicate material.
  search_scope: 'Queries: exact DOI10.1111/j.1462-2920.2012.02776.x with correction/retraction/erratum;
    lindbergite Wei2012 polymorph. Returned result sets only. Independent rg --no-ignore
    --hidden --follow for lindbergite|2003-029|02776|22591055 in current data/records,research,reviews,history
    and existing round39 Wei and round37 humboldtine/lindbergite raw roots; 2229 matching
    lines, exit0, no stderr. Binary originals inspected separately. Not an exhaustive
    literature or filesystem absence claim.'
- evidence_id: proof
  kind: validation
  reference: /private/tmp/cmm-round39-lindbergite-review/independent-checks.json
  locator: Independent preserved-field reconstruction and bounded duplicate search
    receipt
  accessed_at: '2026-10-12T00:22:49.289495Z'
  support: supports
  summary: Root verified exact semantic preservation of all prior fields and byte
    preservation of old history; new study belongs in the existing record.
  snapshot_sha256: 02fffd1b9c174061148cdbf8cdcad290de637d100ef6897a8fa0616462d9c7fd
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral and material boundaries
  outcome: supported
  summary: Approved monoclinic lindbergite remains distinct from element Mn, synthetic
    sodium-birnessite feed, mixed natural nodules, orthorhombic dihydrate and unnamed
    trihydrate. No inherited criticality is asserted.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - ima
  - handbook
  - prior
- assessment_id: conditions
  area: evidence
  topic: Organism, feed, pretreatment and incubation
  outcome: supported
  summary: The living unaccessioned S.himantioides isolate, synthetic Na-birnessite,0.5%w/v,20cm3MEA,90mm
    plate,84mm membrane,5mm leading-edge disk from≥14-dayculture,25C dark triplicates
    agree with original methods. TaxID is species-only. Table3 pH2.93 versus initial7.26
    is25-day surface sampling, not5/23-day diffraction-harvest pH.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - wei
  - taxon
  dimensions:
  - name: biomass
    value: Living fungal culture; isolate supplied by N.White, no accession
    definition: Species grounding does not authenticate strain or prove phenotype
      across the species.
    evidence_ids:
    - wei
    - taxon
  - name: scale
    value: Laboratory plate culture
    definition: No industrial deployment or recovered-metal product demonstrated.
    evidence_ids:
    - record
    - wei
- assessment_id: phase
  area: evidence
  topic: Recovered diffraction assignment
  outcome: supported
  summary: Figure4 explicitly names lindbergite and compares mixed5-day and dihydrate-only23-day
    recovered crystals. Figure2K/L morphology does not prove polymorph/hydration.80C
    extraction and vacuum drying, absent refined cells/water assay/phase fractions,
    and ambiguous analytical-versus-biological determinations are correctly retained.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - wei
  - handbook
- assessment_id: controls
  area: evidence
  topic: Mechanistic attribution and measured outcomes
  outcome: supported
  summary: Growth controls and abiotic morphology do not form a sterile time-matched
    diffraction series.50µL0.5M acid wells are separate unmatched chemical assays;
    halo formation is not lindbergite confirmation. No measured fungal oxalate, killed-biomass
    series, mass balance or isolated product yield establishes an exclusive pathway.
    Figure6 is conceptual.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - wei
- assessment_id: preservation
  area: provenance
  topic: Existing evidence and independent review scope
  outcome: supported
  summary: Fresh scientific assessment covers Wei2012. All earlier scientific claims
    and old provenance reconstruct exactly from trusted base and remain within the
    previous independent review; they are not represented as freshly reread literature.
    New sidecar and inlineEDIT describe only the added arm.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - prior
  - proof
  - history
- assessment_id: conflicts
  area: evidence
  topic: Contradictions and search limits
  outcome: supported
  summary: Pagination discrepancy and preparation/timing ambiguities are explicit.
    The prior orthorhombic Farkas assignment remains context-only. Bounded notice
    search found no affecting notice within returned results, without claiming exhaustive
    absence.
  target_ids:
  - cmmmech:lindbergite
  evidence_ids:
  - record
  - wei
  - search
  - prior
findings: []
actions: []
limitations:
- No wet in-culture diffraction, matched preparation series, phase-specific mass balance
  or industrial demonstration. Culture accession and oxalate measurements remain unavailable.
- Primary PDF is a publicly indexed copy with unknown mirror ownership and no established
  redistribution licence. All nine original pages complete the printed article; bibliographic
  end-page discrepancy retained.
- Prior papers were not freshly re-reviewed; their unchanged fields and earlier independent
  scientific observation are explicit. Notice and local searches are bounded. Root
  direct NCBI web-reader request failed; current shared JSON was parsed.
```
