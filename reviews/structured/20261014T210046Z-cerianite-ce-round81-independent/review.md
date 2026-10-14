# Independent scientific review of cerianite-(Ce)

- Review: 20261014T210046Z-cerianite-ce-round81-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T20:50:39.599657Z
- Finished UTC: 2026-10-14T21:00:46.315133Z
- Reviewer: codex /root/round68_new_frontier (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified acceptance of cerianite-(Ce) identity and source-assigned minor CeO2 after abiotic thermal conversion of a fungal-conditioned precursor. The record correctly excludes direct living-cell precipitation, pure product yield and industrial recovery. No supported corrective defect found.

## Scope And Provenance

Whole frozen mineral owner, canonical CREATE and inline provenance, full primary thermal-conversion claim, authority identity, controls and contradictory phase accounting.

Selection: Assigned exact frozen record; native inspect captured source before scientific judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 623b19fe2ac59b8328d0af3002a6c0da4ee064a7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:cerianite-ce | data/records/cerianite-ce.yaml | maintained | Cerianite-(Ce) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named strict record validation | passed | True | cmmmech:cerianite-ce | Actual independent reviewer execution 2026-10-14T20:50:39.599657+00:00 through 2026-10-14T20:50:47.337000+00:00; one record, zero failures. |
| Actual batch gate 1 | passed | True | cmmmech:cerianite-ce | Actual coordinator execution 2026-10-14T20:50:36.969271+00:00 through 2026-10-14T20:58:51.320453+00:00; terminal exit and log hash independently verified. |
| Actual batch gate 2 | passed | True | cmmmech:cerianite-ce | Actual coordinator execution 2026-10-14T20:58:51.320489+00:00 through 2026-10-14T20:59:22.394167+00:00; terminal exit and log hash independently verified. |
| Actual batch gate 3 | passed | True | cmmmech:cerianite-ce | Actual coordinator execution 2026-10-14T20:59:22.394197+00:00 through 2026-10-14T20:59:34.664069+00:00; terminal exit and log hash independently verified. |
| Actual batch gate 4 | passed | True | cmmmech:cerianite-ce | Actual coordinator execution 2026-10-14T20:59:34.664098+00:00 through 2026-10-14T20:59:42.948169+00:00; terminal exit and log hash independently verified. |

## Scientific And Domain Assessments

### Mineral versus element, natural composition and experimental analogue

identity: supported. Targets: cmmmech:cerianite-ce.

Current authority supports cerianite-(Ce), ideal CeO2, as distinct from elemental cerium and precursor phosphate/oxalate phases. Rn/1987 s.p. identity is accurately represented; natural thorium is not transferred to the laboratory sample. No jurisdiction/list/edition criticality claim is asserted.

### Full upstream preparation and thermal stage

evidence: supported. Targets: cmmmech:cerianite-ce.

Aspergillus niger ATCC1015 conditions a natural struvite/dittmarite feed in MCD containing Na2HPO4. Biomass removal, H-form resin, pH7.5 adjustment and filtration precede synthetic CeCl3 precipitation. The selected20/50mM products are washed/dried then heated below100mg at10K/min to1000°C under dryN2 at100cm3/min. Thermal mechanism microbial:false is scientifically appropriate despite upstream fungal culture. No waste-Ce feed or commercial deployment is established.

### Contrasting loadings and fitted fraction denominator

evidence: supported. Targets: cmmmech:cerianite-ce.

Before heating the50mM precursor is assigned78.3%CePO4.H2O and21.7%Ce2(C2O4)3.10H2O; after heating90.4%CePO4 and9.6%CeO2. At20mM oxalate is undetected before heating and CeO2 is undetected after heating, with100%fittedCePO4. Those are source-modelled phase fractions, not quantitative isolated recovery. Figure7a/b are sample traces andc/d reference patterns.

### Control and reaction-pathway limits

evidence: supported. Targets: cmmmech:cerianite-ce.

All nine main figures and both tables were independently checked. Figure8 thermal differences support association with the contrasting precursors; no time-resolved diffraction or direct Ce-valence measurement proves every reaction step. Greater-than99%aqueousCe removal and precursor masses do not establish cerianite yield. Missing matched Ce-stage comparators are accurately retained without erasing the upstream uninoculated culture control.

### Additional phase and figure-reference conflict

evidence: supported. Targets: cmmmech:cerianite-ce.

Discussion mentions unquantified Na3Ce(PO4)2 while Table2 and Figure7 legend provide CePO4/CeO2 accounting. The record neither suppresses nor quantifies that additional phase. Source specimen/reference lettering and broad amorphous-precursor language are cautiously separated from tabulated XRD fits.

### Shared experiment, history and actual checks

provenance: supported. Targets: cmmmech:cerianite-ce.

Native inspect preceded judgment; exact final owner/schema/history inputs remain unchanged. Canonical CREATE and inline event accurately identify their actual actor/time. Same Kang2022 evidence in cerium/phosphorus/struvite remains shared lineage. Independent named validation and all four actual root batch gates passed; no hosted CI or merge result is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/cerianite-ce.yaml; Whole frozen owner. Actual local artifact: /private/tmp/CMMMech-expansion-round81-20261014/data/records/cerianite-ce.yaml | supports | Identity, process, evidence and provenance checked against exact inspected bytes. |
| history | history/records/cerianite-ce/2026-10-14T204842Z-codex-430886.yaml; Whole canonical CREATE sidecar and separately assessed inline CREATE. Actual local artifact: /private/tmp/CMMMech-expansion-round81-20261014/history/records/cerianite-ce/2026-10-14T204842Z-codex-430886.yaml | supports | Actor codex/GPT-6, actual distinct timestamps, target and bounded description verified; no reviewer edits. |
| primary | https://doi.org/10.1007/s00253-021-11721-0; Complete original thirteen pages, Methods pp.822–824, Figures1–9, Tables1–2, Results/Discussion pp.825–831; all claim-bearing figures/tables visually inspected using original PDF page renders4–9. Actual local artifact: /private/tmp/cmm-round81-ceria-research/kang2022.pdf | supports | Full upstream culture, resin/pH pretreatment, precipitation and thermal methods independently checked; Table2 and Figure7 support a mixed minor CeO2 product at higher loading, with a lower-loading contrasting result. |
| xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8763747/fullTextXML; Complete original XML, methods, figure captions and tables. Actual local artifact: /private/tmp/cmm-round81-ceria-research/kang2022.xml | supports | Same article and experiment; text corroboration and enumeration of article assets, not a second replication. |
| assets | https://doi.org/10.1007/s00253-021-11721-0; ZIP independently enumerated: eighteen main-figure assets, nine JPG and nine GIF, no separate experimental SI document. Actual local artifact: /private/tmp/cmm-round81-ceria-research/kang2022-supplementary.zip | context_only | Despite the local filename, this ZIP is main-figure media, not a supplemental experiment. No supplementary-material node occurs in the acquired complete XML. Main PDF graphics independently inspected. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 master list definitions pp.1–2 and Cerianite-(Ce) row p.39, row visually inspected. Actual local artifact: /private/tmp/cmm-round80-carbonates-research/ima2026-09.pdf | supports | Current CeO2 identity and renamed Rn/1987 special-procedure status confirmed; special-procedure notation is not invented as a sequential approval identifier. |
| handbook | https://www.handbookofmineralogy.org/pdfs/cerianite-Ce.pdf; Complete one-page original, printed p.105; visually inspected composition, cubic crystallography and powder pattern. Actual local artifact: /private/tmp/cmm-round81-ceria-research/handbook-cerianite.pdf | supports | Natural thorium-bearing composition and synthetic CeO2 analogue are distinguished; authority does not establish thorium in this experimental solid. |
| notices | /private/tmp/cmm-round81-cerianite-independent/notice-search.json; Actual retained web result sets. Actual local artifact: /private/tmp/cmm-round81-cerianite-independent/notice-search.json | context_only | No affecting correction, erratum or retraction was identified in these bounded results; not a global absence claim. |
| dedup | /private/tmp/cmm-round81-cerianite-independent/dedup.txt; Current worktree records/research/reviews/history; name and normalized DOI search. Actual local artifact: /private/tmp/cmm-round81-cerianite-independent/dedup.txt | context_only | Existing cerium/phosphorus/struvite owners share Kang2022; this thermal phase is not presented as independent replication. Hidden/ignored-inclusive search has bounded repository-text scope. |
| named | /private/tmp/cmm-round81-cerianite-independent/named-validation.json; Actual independent reviewer command and terminal log binding. Actual local artifact: /private/tmp/cmm-round81-cerianite-independent/named-validation.json | supports | Named strict validation passed one record, zero failures; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e. |
| batch | /private/tmp/cmm-round81-final-gates.json; Actual coordinator terminal receipt, all four commands; actual log /private/tmp/cmm-round81-final-gates.log SHA256 be6da2760c4de77f9fa334aa3b47406982628dd290b9b49ecdbb272839e0b6f4. Actual local artifact: /private/tmp/cmm-round81-final-gates.json | supports | All four exits, exact command sequence, trusted base, unchanged owner hash and log digest independently verified. This is local validation, not hosted publication. |

## Limits And Additional Notes

- Rietveld-fitted percentages describe a mixed product, not isolated cerianite yield, recovery efficiency or validated absolute purity; fit uncertainties and phase detection limit are not supplied.
- The source mentions an additional Na3Ce(PO4)2 phase without reconciling it with Table2 two-phase fits; the record keeps that discrepancy explicit.
- The proposed oxalate-to-ceria pathway lacks direct time-resolved phase/valence proof; nitrogen thermal atmosphere is retained and air oxidation is not assumed.
- No matched synthetic phosphate/oxalate or untreated-filtrate comparator resolves microbial necessity for the Ce precipitation/thermal sequence. This does not deny the separately stated uninoculated upstream struvite control.
- Bounded notice searches are not an exhaustive global correction audit; the acquired media ZIP contains main figures, not independent SI.
- The reported start is the actual timestamp captured for the independent named-validation phase; native inspection and preliminary source reading had already begun and their first instant was not separately clocked. The finish is captured during final evidence binding.
- Accepted article PDF and XML are complete nonempty originals; actual paths and SHA256 bind the inspected files. All main graphics were visually checked. The artifact named supplementary.zip is explicitly context-only main-figure media, not invented SI.
- No target/history edits were made by this reviewer. No gene, pathway accession or taxon CURIE is asserted for the abiotic thermal mechanism; the original organism strain text is retained only for its upstream context.

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
review_id: 20261014T210046Z-cerianite-ce-round81-independent
title: Independent scientific review of cerianite-(Ce)
started_at: '2026-10-14T20:50:39.599657Z'
finished_at: '2026-10-14T21:00:46.315133Z'
reviewer:
  identity: codex /root/round68_new_frontier
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored the cerianite owner/history. This reviewer authored
    the unrelated used-photographic-fixer-solutions record, independently inspected
    the cerianite primary methods/results, all nine figures and both tables, and authorities,
    and did not edit this owner or history. Shared acquisition artifacts are not independent
    experimental replication.
source:
  git_revision: 623b19fe2ac59b8328d0af3002a6c0da4ee064a7
  state: working_tree
  inputs:
  - path: data/records/cerianite-ce.yaml
    sha256: 94b904083cfa29367512be8795474bc670c817032a059a9eca472935b2ebe052
    role: target
  - path: history/records/cerianite-ce/2026-10-14T204842Z-codex-430886.yaml
    sha256: 00c0a256f962cb16fe4d70d59ce6f324ecef25276af6b7925bed8d52722b4df3
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:cerianite-ce
  path: data/records/cerianite-ce.yaml
  label: Cerianite-(Ce)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/cerianite-ce.yaml
    role: maintained_record
scope:
  description: Whole frozen mineral owner, canonical CREATE and inline provenance,
    full primary thermal-conversion claim, authority identity, controls and contradictory
    phase accounting.
  selection: Assigned exact frozen record; native inspect captured source before scientific
    judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:cerianite-ce
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/cerianite-ce.yaml
  locator: 'Whole frozen owner. Actual local artifact: /private/tmp/CMMMech-expansion-round81-20261014/data/records/cerianite-ce.yaml'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Identity, process, evidence and provenance checked against exact inspected
    bytes.
  snapshot_sha256: 94b904083cfa29367512be8795474bc670c817032a059a9eca472935b2ebe052
- evidence_id: history
  kind: record_content
  reference: history/records/cerianite-ce/2026-10-14T204842Z-codex-430886.yaml
  locator: 'Whole canonical CREATE sidecar and separately assessed inline CREATE.
    Actual local artifact: /private/tmp/CMMMech-expansion-round81-20261014/history/records/cerianite-ce/2026-10-14T204842Z-codex-430886.yaml'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Actor codex/GPT-6, actual distinct timestamps, target and bounded description
    verified; no reviewer edits.
  snapshot_sha256: 00c0a256f962cb16fe4d70d59ce6f324ecef25276af6b7925bed8d52722b4df3
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-021-11721-0
  locator: 'Complete original thirteen pages, Methods pp.822–824, Figures1–9, Tables1–2,
    Results/Discussion pp.825–831; all claim-bearing figures/tables visually inspected
    using original PDF page renders4–9. Actual local artifact: /private/tmp/cmm-round81-ceria-research/kang2022.pdf'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Full upstream culture, resin/pH pretreatment, precipitation and thermal
    methods independently checked; Table2 and Figure7 support a mixed minor CeO2 product
    at higher loading, with a lower-loading contrasting result.
  snapshot_sha256: 954eba1e205d7b1f7eea5120ffbfed47bd1fbb800a7b70ce696e36a8ae99cbdd
- evidence_id: xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8763747/fullTextXML
  locator: 'Complete original XML, methods, figure captions and tables. Actual local
    artifact: /private/tmp/cmm-round81-ceria-research/kang2022.xml'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Same article and experiment; text corroboration and enumeration of article
    assets, not a second replication.
  snapshot_sha256: de81edbc2854a8b9b5fae071ca74af0a2bd163c799b3d6786baba9b755ed6c83
- evidence_id: assets
  kind: primary_source
  reference: https://doi.org/10.1007/s00253-021-11721-0
  locator: 'ZIP independently enumerated: eighteen main-figure assets, nine JPG and
    nine GIF, no separate experimental SI document. Actual local artifact: /private/tmp/cmm-round81-ceria-research/kang2022-supplementary.zip'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: context_only
  summary: Despite the local filename, this ZIP is main-figure media, not a supplemental
    experiment. No supplementary-material node occurs in the acquired complete XML.
    Main PDF graphics independently inspected.
  snapshot_sha256: bf061d11b4ff17b326480f93770aee40cb81fcd76d5a220e454bba6be66f687b
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'September2026 master list definitions pp.1–2 and Cerianite-(Ce) row p.39,
    row visually inspected. Actual local artifact: /private/tmp/cmm-round80-carbonates-research/ima2026-09.pdf'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Current CeO2 identity and renamed Rn/1987 special-procedure status confirmed;
    special-procedure notation is not invented as a sequential approval identifier.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/cerianite-Ce.pdf
  locator: 'Complete one-page original, printed p.105; visually inspected composition,
    cubic crystallography and powder pattern. Actual local artifact: /private/tmp/cmm-round81-ceria-research/handbook-cerianite.pdf'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Natural thorium-bearing composition and synthetic CeO2 analogue are distinguished;
    authority does not establish thorium in this experimental solid.
  snapshot_sha256: ef13dafae0ce3fd276d439f81b8d10456ce3b7ead0cf83dda2b5d5e105427397
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round81-cerianite-independent/notice-search.json
  locator: 'Actual retained web result sets. Actual local artifact: /private/tmp/cmm-round81-cerianite-independent/notice-search.json'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: context_only
  summary: No affecting correction, erratum or retraction was identified in these
    bounded results; not a global absence claim.
  snapshot_sha256: 5dec7e96c388f2fba8f68dee0c3e246e10ea04731d90d23cd410d96a1f57ffba
  search_scope: Exact DOI plus correction/retraction/erratum and exact study-title
    correction queries on 2026-10-14; returned result sets retained.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round81-cerianite-independent/dedup.txt
  locator: 'Current worktree records/research/reviews/history; name and normalized
    DOI search. Actual local artifact: /private/tmp/cmm-round81-cerianite-independent/dedup.txt'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: context_only
  summary: Existing cerium/phosphorus/struvite owners share Kang2022; this thermal
    phase is not presented as independent replication. Hidden/ignored-inclusive search
    has bounded repository-text scope.
  snapshot_sha256: adc2ffc4b275aa90bf9ad580d37f2894d308db34c149c8d4d2128cc22340a440
  search_scope: rg --no-ignore --hidden --follow -n -i cerianite|s00253-021-11721-0
    data/records research reviews history, excluding only binary PDF/PNG/JPG patterns;
    current textual files including ignored ones searched.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round81-cerianite-independent/named-validation.json
  locator: 'Actual independent reviewer command and terminal log binding. Actual local
    artifact: /private/tmp/cmm-round81-cerianite-independent/named-validation.json'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: Named strict validation passed one record, zero failures; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e.
  snapshot_sha256: 0d12bbd9d5103d62920bf364d20317b17788a16326f6a441fe7a75463c97b83e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round81-final-gates.json
  locator: 'Actual coordinator terminal receipt, all four commands; actual log /private/tmp/cmm-round81-final-gates.log
    SHA256 be6da2760c4de77f9fa334aa3b47406982628dd290b9b49ecdbb272839e0b6f4. Actual
    local artifact: /private/tmp/cmm-round81-final-gates.json'
  accessed_at: '2026-10-14T21:00:46.315133Z'
  support: supports
  summary: All four exits, exact command sequence, trusted base, unchanged owner hash
    and log digest independently verified. This is local validation, not hosted publication.
  snapshot_sha256: 2c442921cebcdcc981d4e9b0c2300dd3b7665494493391f6c8a8bd62b6fb9de3
checks:
- check_id: named
  name: Independent named strict record validation
  command: uv run --locked cmmmech validate data/records/cerianite-ce.yaml --require-records
  status: passed
  required: true
  summary: Actual independent reviewer execution 2026-10-14T20:50:39.599657+00:00
    through 2026-10-14T20:50:47.337000+00:00; one record, zero failures.
  target_ids:
  - cmmmech:cerianite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch0
  name: Actual batch gate 1
  command: just check
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T20:50:36.969271+00:00 through 2026-10-14T20:58:51.320453+00:00;
    terminal exit and log hash independently verified.
  target_ids:
  - cmmmech:cerianite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch1
  name: Actual batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T20:58:51.320489+00:00 through 2026-10-14T20:59:22.394167+00:00;
    terminal exit and log hash independently verified.
  target_ids:
  - cmmmech:cerianite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Actual batch gate 3
  command: uv run --locked cmmmech validate-history --base 623b19fe2ac59b8328d0af3002a6c0da4ee064a7
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T20:59:22.394197+00:00 through 2026-10-14T20:59:34.664069+00:00;
    terminal exit and log hash independently verified.
  target_ids:
  - cmmmech:cerianite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Actual batch gate 4
  command: uv run --locked python scripts/render_pages.py --check
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T20:59:34.664098+00:00 through 2026-10-14T20:59:42.948169+00:00;
    terminal exit and log hash independently verified.
  target_ids:
  - cmmmech:cerianite-ce
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
summary: Qualified acceptance of cerianite-(Ce) identity and source-assigned minor
  CeO2 after abiotic thermal conversion of a fungal-conditioned precursor. The record
  correctly excludes direct living-cell precipitation, pure product yield and industrial
  recovery. No supported corrective defect found.
limitations:
- Rietveld-fitted percentages describe a mixed product, not isolated cerianite yield,
  recovery efficiency or validated absolute purity; fit uncertainties and phase detection
  limit are not supplied.
- The source mentions an additional Na3Ce(PO4)2 phase without reconciling it with
  Table2 two-phase fits; the record keeps that discrepancy explicit.
- The proposed oxalate-to-ceria pathway lacks direct time-resolved phase/valence proof;
  nitrogen thermal atmosphere is retained and air oxidation is not assumed.
- No matched synthetic phosphate/oxalate or untreated-filtrate comparator resolves
  microbial necessity for the Ce precipitation/thermal sequence. This does not deny
  the separately stated uninoculated upstream struvite control.
- Bounded notice searches are not an exhaustive global correction audit; the acquired
  media ZIP contains main figures, not independent SI.
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral versus element, natural composition and experimental analogue
  outcome: supported
  summary: Current authority supports cerianite-(Ce), ideal CeO2, as distinct from
    elemental cerium and precursor phosphate/oxalate phases. Rn/1987 s.p. identity
    is accurately represented; natural thorium is not transferred to the laboratory
    sample. No jurisdiction/list/edition criticality claim is asserted.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - ima
  - handbook
- assessment_id: preparation
  area: evidence
  topic: Full upstream preparation and thermal stage
  outcome: supported
  summary: Aspergillus niger ATCC1015 conditions a natural struvite/dittmarite feed
    in MCD containing Na2HPO4. Biomass removal, H-form resin, pH7.5 adjustment and
    filtration precede synthetic CeCl3 precipitation. The selected20/50mM products
    are washed/dried then heated below100mg at10K/min to1000°C under dryN2 at100cm3/min.
    Thermal mechanism microbial:false is scientifically appropriate despite upstream
    fungal culture. No waste-Ce feed or commercial deployment is established.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - primary
  - xml
- assessment_id: phase
  area: evidence
  topic: Contrasting loadings and fitted fraction denominator
  outcome: supported
  summary: Before heating the50mM precursor is assigned78.3%CePO4.H2O and21.7%Ce2(C2O4)3.10H2O;
    after heating90.4%CePO4 and9.6%CeO2. At20mM oxalate is undetected before heating
    and CeO2 is undetected after heating, with100%fittedCePO4. Those are source-modelled
    phase fractions, not quantitative isolated recovery. Figure7a/b are sample traces
    andc/d reference patterns.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - primary
  - xml
- assessment_id: causality
  area: evidence
  topic: Control and reaction-pathway limits
  outcome: supported
  summary: All nine main figures and both tables were independently checked. Figure8
    thermal differences support association with the contrasting precursors; no time-resolved
    diffraction or direct Ce-valence measurement proves every reaction step. Greater-than99%aqueousCe
    removal and precursor masses do not establish cerianite yield. Missing matched
    Ce-stage comparators are accurately retained without erasing the upstream uninoculated
    culture control.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - primary
- assessment_id: conflicts
  area: evidence
  topic: Additional phase and figure-reference conflict
  outcome: supported
  summary: Discussion mentions unquantified Na3Ce(PO4)2 while Table2 and Figure7 legend
    provide CePO4/CeO2 accounting. The record neither suppresses nor quantifies that
    additional phase. Source specimen/reference lettering and broad amorphous-precursor
    language are cautiously separated from tabulated XRD fits.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - primary
  - xml
- assessment_id: provenance
  area: provenance
  topic: Shared experiment, history and actual checks
  outcome: supported
  summary: Native inspect preceded judgment; exact final owner/schema/history inputs
    remain unchanged. Canonical CREATE and inline event accurately identify their
    actual actor/time. Same Kang2022 evidence in cerium/phosphorus/struvite remains
    shared lineage. Independent named validation and all four actual root batch gates
    passed; no hosted CI or merge result is claimed.
  target_ids:
  - cmmmech:cerianite-ce
  evidence_ids:
  - record
  - history
  - named
  - batch
  - dedup
  - notices
findings: []
actions: []
notes:
- The reported start is the actual timestamp captured for the independent named-validation
  phase; native inspection and preliminary source reading had already begun and their
  first instant was not separately clocked. The finish is captured during final evidence
  binding.
- Accepted article PDF and XML are complete nonempty originals; actual paths and SHA256
  bind the inspected files. All main graphics were visually checked. The artifact
  named supplementary.zip is explicitly context-only main-figure media, not invented
  SI.
- No target/history edits were made by this reviewer. No gene, pathway accession or
  taxon CURIE is asserted for the abiotic thermal mechanism; the original organism
  strain text is retained only for its upstream context.
```
