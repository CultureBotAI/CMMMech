# Independent scientific review of allanite-derived leachate

- Review: 20261012T100758Z-allanite-leachate-round53-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T10:03:02Z
- Finished UTC: 2026-10-12T10:07:58Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record supports qualified laboratory REE solution depletion using yeast-produced oxalate in a separately prepared chemical liquor. No corrective finding was identified. Controls, replication, dose and impurity conventions, phase characterization and scale remain explicitly bounded.

## Scope And Provenance

All maintained fields, CREATE/inline history and paired dossiers; independent fresh scientific review of the Lu2026 real-liquor observation and all claim-relevant biological-production and synthetic-comparator context.

Selection: One assigned exact frozen record; reviewer did not author it.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b85c2c2c753fe83a2fc21f073ee1e49675ae647e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:allanite-leachate | data/records/allanite-leachate.yaml | maintained | Allanite-derived rare-earth leachate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:allanite-leachate | Reviewer executed in round53; terminal exit 0, Checked 1 record(s); 0 failed. Actual tool chunk 02b61b; /private/tmp/cmm-round53-allanite-review-evidence.json retains the receipt. |
| Parent-executed completed batch | passed | True | cmmmech:allanite-leachate | Reviewer independently read terminal log /private/tmp/cmm-round53-final-batch.log, SHA256 5dccf1da78b9111e8714e725ea5b540e319448ec511b2cd3cd161ed16ab3d5a5; actual receipt/log match. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 137.72s (0:02:17)<br>Checked 256 record(s); 0 failed.<br>Checked 303 history record(s); 0 error(s).<br> |
| Parent-executed completed nonempty | passed | True | cmmmech:allanite-leachate | Reviewer independently read terminal log /private/tmp/cmm-round53-final-nonempty.log, SHA256 f102e7162eedb9bf7d45e2a2fa9b011e7a3bf83fb2c341e1424889b9dd856f34; actual receipt/log match. Checked 256 record(s); 0 failed.<br> |
| Parent-executed completed history | passed | True | cmmmech:allanite-leachate | Reviewer independently read terminal log /private/tmp/cmm-round53-final-history.log, SHA256 60b1330e0225bff7414e09d933725aee3784ed120b5151b881814e9a98ae731c; actual receipt/log match. Checked 303 history record(s); 0 error(s).<br> |
| Parent-executed completed render-check | passed | True | cmmmech:allanite-leachate | Reviewer independently read terminal log /private/tmp/cmm-round53-final-render-check.log, SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6; actual receipt/log match. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Chemically generated liquor and species-level organism

identity: supported. Targets: cmmmech:allanite-leachate.

Secondary-resource ownership is justified by extensive chemical conversion and redissolution, distinct from ore, concentrate, species and isolated product. The source-specific scope does not import constituent criticality.

### Biogenic reagent and bounded precipitation observation

evidence: supported. Targets: cmmmech:allanite-leachate.

The record accurately separates culture-mediated reagent production from subsequent chemical precipitation. Real-liquor time/temperature are not borrowed from synthetic assays. Similar observed commercial and biogenic removal with n=1 does not imply statistical equivalence or general superiority.

### Contradictions and negative/zero measurements

evidence: supported. Targets: cmmmech:allanite-leachate.

Dose denominator, missing cells, negative apparent removals, Mn exception, Th/U zero conventions and unexplained reagent-batch mapping are explicit. No essential correction is needed to preserve the narrower observation.

### Exact inputs, true history, evidence gap disposition and completed checks

provenance: supported. Targets: cmmmech:allanite-leachate.

All five explicit native inputs match the frozen state. Source163 assessment requirements are addressed within review scope; scientific limitations remain visible, and only repository checks actually completed are included.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| main | https://doi.org/10.1038/s41467-026-68957-5; Complete original 11-page main article text; original Figures 1–4 on pp.3–6; detailed methods and Eq.1 on pp.7–9 personally checked. | supports | The real feed is chemically processed Halleck Creek ore leachate. Yeast reagent production and real-liquor precipitation are separate stages. The latter uses centrifuged supernatant, commercial comparator, pH1.5 and n=1 per condition; measured residual solution depletion does not establish isolated product yield. The synthetic salt assays and their XRD are distinct. |
| si | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-68957-5/MediaObjects/41467_2026_68957_MOESM1_ESM.pdf; Supplementary Methods1–2; Table1 p5 and Table3 p7; original Figures S1–S8 pp12–19 personally inspected. | supports | JL04 engineering and culture-production conditions are traceable. S8 is the separate 22g/L real-feed arm; S7 is synthetic single-salt precipitation. Table3 compares neodymium oxalate decahydrate and does not establish mixed real-feed phase purity. |
| workbooks | /private/tmp/cmm-round53-allanite-review-workbooks.json; Independent standard-library ZIP/XML reading of original MOESM4 and MOESM11; all four Data1 sheets and all sixteen SourceData sheets inventoried. Detailed checks of three Analysis sheets rows41–53 and66–77, SourceData Fig3a/3b rows17–28 and34–45, S1toS8 rows68–79 and Fig2 F11/F12. | supports | 780 cached-value arithmetic/plot relationships independently verified. Row74 TREE depletion is 99.674%,99.745%,99.576% at source-nominal2.7009,2.6901,2.772g/L. Biological arms start95mL but nominal dose divides by100mL. Mn6.8856% in A conflicts with the main blanket&lt;6% claim. Th/U zeros imply apparent100% disappearance without per-cell limits; negative values and missing cells are preserved. SourceData gives38.78 and40.27g/L production titers, separate from42.70g/L reagent. These checks do not validate instruments or mass closure. |
| peer_context | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-68957-5/MediaObjects/41467_2026_68957_MOESM2_ESM.pdf; Selective peer-review-file text: pp12–13 higher-titer repeat assays; pp46–48 supernatant preparation and single-Nd purity discussion. Supplement descriptions MOESM3, one complete page. | supports | Responses explain early versus later fermentation work but do not uniquely tie42.70g/L reagent to the displayed two10-day samples. Purity response concerns synthetic neodymium, not the mixed liquor. Historical draft ICP-MS wording does not supersede final main ICP-OES methods. Full TEA supplements and every peer-review response were not scientifically reanalyzed. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4909&amp;mode=Info; Fresh issuing-database browser read: Taxonomy ID4909, current name, species rank and heterotypic synonyms. | supports | Pichia kudriavzevii at species rank is correct; Issatchenkia orientalis is a listed synonym. This does not authenticate SD108 or engineered JL04 stock. |
| search | /private/tmp/cmm-round53-allanite-review-evidence.json; Fresh exact DOI correction/retraction and exact title critique queries, issuing NCBI page, current Crossmark result and independent hidden/ignored/followed owner/context search. | supports | Returned result sets contained no affecting notice; Crossmark states document current. The current record is distinct from prior Schmitz-backed concentrate and prior Lu source-only handoff. No assertion of exhaustive literature or filesystem coverage is made. |
| contexts | research/sources/round53-allanite-leachate/20261012T100150Z-source-investigation.json; All five explicit native inputs, paired author dossiers and canonical CREATE/inline event; provenance absolute artifact path/hash pairs independently rehashed. | supports | 51 absolute path/hash references representing33 unique retained artifacts match. Actual actor, date, target and sidecar agree; no earlier authorship is invented. Root authored the record and dossier; reviewer independently judged the underlying evidence. |
| issue163 | https://github.com/CultureBotAI/CMMMech/issues/163; Read-only live gh issue view163, title/body/OPEN state during review. | supports | The issue requests source assessment, controls/stages/denominator reconciliation, appropriate ownership, curation/history, independent review and gates; it does not require new experiments. The bounded accepted record addresses that assessment while retaining experimental questions. This review does not close or mutate the issue. |
| gates | /private/tmp/cmm-round53-final-terminal.json; Actual complete parent terminal receipt and all command logs read and SHA-256 verified; native frozen input hashes unchanged. | supports | Named validation and completed batch/nonempty/history/render checks supplement the scientific assessment. No unexecuted or prior-cohort result is claimed. |

## Limits And Additional Notes

- Real-liquor conditions have n=1 and no documented matched broth comparator; independent performance replication and matrix attribution remain unknown.
- Real-liquor precipitation temperature/time are not specified separately; synthetic overnight conditions cannot fill this gap.
- Nominal doses divide by100mL despite95mL biological starting volumes; sequential samples and dilution correction do not establish closed mass balance.
- Zero/censoring conventions, Th/U co-retention, negative apparent removals and the Mn&lt;6% prose conflict remain source limitations.
- The42.70g/L reagent is not identified with the two displayed38.78/40.27g/L production observations.
- Synthetic-Nd diffraction and FTIR do not identify mixed real-liquor phases or establish product purity.
- No isolated ore-to-product yield, industrial deployment, measured full-process LCA or inherited criticality is claimed.
- Source and duplicate searches are bounded; not all economic supplements, historical raw roots or unextracted binary contents were semantically reviewed.
- The issue163 live state was OPEN at assessment. This review supports completion of its evidence-assessment objective subject to publication procedure; no GitHub mutation occurred.
- Original raw files and independent workbook extraction/arithmetic receipts remain outside Git. No curation-history event is added by this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T100758Z-allanite-leachate-round53-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of allanite-derived leachate
started_at: '2026-10-12T10:03:02Z'
finished_at: '2026-10-12T10:07:58Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: The reviewer authored hafnon in this cohort, not the parent-authored
    allanite-leachate record, history or dossier. Explicit native inputs were captured
    before judgment; original methods, graphics and workbooks were independently inspected.
    No target edits were made.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record supports qualified laboratory REE solution depletion using
  yeast-produced oxalate in a separately prepared chemical liquor. No corrective finding
  was identified. Controls, replication, dose and impurity conventions, phase characterization
  and scale remain explicitly bounded.
source:
  git_revision: b85c2c2c753fe83a2fc21f073ee1e49675ae647e
  state: working_tree
  inputs:
  - path: data/records/allanite-leachate.yaml
    sha256: 08a2b7ef4f280ae14006cb66d380c5d080807725d0be8f484ca92d30ee7e4af9
    role: target
  - path: history/records/allanite-leachate/2026-10-12T100026Z-codex-3c88ef.yaml
    sha256: f16a029d3835423b42fd0296cc40e968af90f2ca16a0377df15233d2d77bc48d
    role: context
  - path: research/sources/round53-allanite-leachate/20261012T100150Z-source-investigation.json
    sha256: 992432acc723c23fabc6578657b6fec467c3ce1f968ef3d3580dae8fee9925e7
    role: context
  - path: research/sources/round53-allanite-leachate/20261012T100150Z-source-investigation.md
    sha256: b0fc2cf4861aa93cd36b62bc8a8d557675c21e84f3405ea7e689dc844dadca8d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:allanite-leachate
  path: data/records/allanite-leachate.yaml
  label: Allanite-derived rare-earth leachate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/allanite-leachate.yaml
    role: maintained scientific record
scope:
  description: All maintained fields, CREATE/inline history and paired dossiers; independent
    fresh scientific review of the Lu2026 real-liquor observation and all claim-relevant
    biological-production and synthetic-comparator context.
  selection: One assigned exact frozen record; reviewer did not author it.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:allanite-leachate
  exclusions:
  - target: Full TEA/LCA simulation rerun and economic supplement cell-by-cell validation
    reason: Only the model-versus-experiment boundary is asserted; no economic measurement
      is curated.
  - target: Every historical peer-review reply and all primer sequences
    reason: Selective relevant context was read; no exhaustive replication of engineering
      or review history is claimed.
checks:
- check_id: named
  name: Independent named record validation
  command: uv run --locked cmmmech validate data/records/allanite-leachate.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:allanite-leachate
  summary: Reviewer executed in round53; terminal exit 0, Checked 1 record(s); 0 failed.
    Actual tool chunk 02b61b; /private/tmp/cmm-round53-allanite-review-evidence.json
    retains the receipt.
- check_id: batch
  name: Parent-executed completed batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:allanite-leachate
  summary: 'Reviewer independently read terminal log /private/tmp/cmm-round53-final-batch.log,
    SHA256 5dccf1da78b9111e8714e725ea5b540e319448ec511b2cd3cd161ed16ab3d5a5; actual
    receipt/log match. uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 137.72s (0:02:17)

    Checked 256 record(s); 0 failed.

    Checked 303 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Parent-executed completed nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:allanite-leachate
  summary: 'Reviewer independently read terminal log /private/tmp/cmm-round53-final-nonempty.log,
    SHA256 f102e7162eedb9bf7d45e2a2fa9b011e7a3bf83fb2c341e1424889b9dd856f34; actual
    receipt/log match. Checked 256 record(s); 0 failed.

    '
- check_id: history
  name: Parent-executed completed history
  command: uv run --locked cmmmech validate-history --base b85c2c2c753fe83a2fc21f073ee1e49675ae647e
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:allanite-leachate
  summary: 'Reviewer independently read terminal log /private/tmp/cmm-round53-final-history.log,
    SHA256 60b1330e0225bff7414e09d933725aee3784ed120b5151b881814e9a98ae731c; actual
    receipt/log match. Checked 303 history record(s); 0 error(s).

    '
- check_id: render-check
  name: Parent-executed completed render-check
  command: just render-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:allanite-leachate
  summary: 'Reviewer independently read terminal log /private/tmp/cmm-round53-final-render-check.log,
    SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6; actual
    receipt/log match. uv run python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: main
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-026-68957-5
  locator: Complete original 11-page main article text; original Figures 1–4 on pp.3–6;
    detailed methods and Eq.1 on pp.7–9 personally checked.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: The real feed is chemically processed Halleck Creek ore leachate. Yeast
    reagent production and real-liquor precipitation are separate stages. The latter
    uses centrifuged supernatant, commercial comparator, pH1.5 and n=1 per condition;
    measured residual solution depletion does not establish isolated product yield.
    The synthetic salt assays and their XRD are distinct.
  snapshot_sha256: 6e452116325eb24021399bad565be7058c79cd866a744fcae5c374155274f3b1
- evidence_id: si
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-68957-5/MediaObjects/41467_2026_68957_MOESM1_ESM.pdf
  locator: Supplementary Methods1–2; Table1 p5 and Table3 p7; original Figures S1–S8
    pp12–19 personally inspected.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: JL04 engineering and culture-production conditions are traceable. S8 is
    the separate 22g/L real-feed arm; S7 is synthetic single-salt precipitation. Table3
    compares neodymium oxalate decahydrate and does not establish mixed real-feed
    phase purity.
  snapshot_sha256: 9cf3b67a97adea7c98846f0ac06fc118a789821d709fc9ffad02614c06cfac2a
- evidence_id: workbooks
  kind: primary_source
  reference: /private/tmp/cmm-round53-allanite-review-workbooks.json
  locator: Independent standard-library ZIP/XML reading of original MOESM4 and MOESM11;
    all four Data1 sheets and all sixteen SourceData sheets inventoried. Detailed
    checks of three Analysis sheets rows41–53 and66–77, SourceData Fig3a/3b rows17–28
    and34–45, S1toS8 rows68–79 and Fig2 F11/F12.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: 780 cached-value arithmetic/plot relationships independently verified.
    Row74 TREE depletion is 99.674%,99.745%,99.576% at source-nominal2.7009,2.6901,2.772g/L.
    Biological arms start95mL but nominal dose divides by100mL. Mn6.8856% in A conflicts
    with the main blanket<6% claim. Th/U zeros imply apparent100% disappearance without
    per-cell limits; negative values and missing cells are preserved. SourceData gives38.78
    and40.27g/L production titers, separate from42.70g/L reagent. These checks do
    not validate instruments or mass closure.
  snapshot_sha256: d01aefbd3dcb9c715661805a907f8a2d5356ab74eecae9b915e713eef92d5323
- evidence_id: peer_context
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-68957-5/MediaObjects/41467_2026_68957_MOESM2_ESM.pdf
  locator: 'Selective peer-review-file text: pp12–13 higher-titer repeat assays; pp46–48
    supernatant preparation and single-Nd purity discussion. Supplement descriptions
    MOESM3, one complete page.'
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: Responses explain early versus later fermentation work but do not uniquely
    tie42.70g/L reagent to the displayed two10-day samples. Purity response concerns
    synthetic neodymium, not the mixed liquor. Historical draft ICP-MS wording does
    not supersede final main ICP-OES methods. Full TEA supplements and every peer-review
    response were not scientifically reanalyzed.
  snapshot_sha256: 5be92008a0b76bb6e266af927debfcaea332629c71ad3e8a73786be9774c8d10
- evidence_id: taxonomy
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4909&mode=Info
  locator: 'Fresh issuing-database browser read: Taxonomy ID4909, current name, species
    rank and heterotypic synonyms.'
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: Pichia kudriavzevii at species rank is correct; Issatchenkia orientalis
    is a listed synonym. This does not authenticate SD108 or engineered JL04 stock.
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round53-allanite-review-evidence.json
  locator: Fresh exact DOI correction/retraction and exact title critique queries,
    issuing NCBI page, current Crossmark result and independent hidden/ignored/followed
    owner/context search.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: Returned result sets contained no affecting notice; Crossmark states document
    current. The current record is distinct from prior Schmitz-backed concentrate
    and prior Lu source-only handoff. No assertion of exhaustive literature or filesystem
    coverage is made.
  snapshot_sha256: 1ed6c11d9e96441d7407d38671cdcb22cfda88abffe370338c0b9bea48a6f65e
  search_scope: 'Web queries: "10.1038/s41467-026-68957-5" correction retraction;
    "Bio-based oxalic acid production" "Issatchenkia" critique; NCBI4909 synonym lookup.
    Independent rg --hidden --no-ignore --follow across current and original checkout
    data/history/research/reviews plus round52-allanite and round53-allanite-leachate
    raw roots.33 matching paths. Wider author dedup receipt inspected, not wholly
    rerun; its nine missing roots and unextracted binary contents remain outside semantic
    coverage.'
- evidence_id: contexts
  kind: record_content
  reference: research/sources/round53-allanite-leachate/20261012T100150Z-source-investigation.json
  locator: All five explicit native inputs, paired author dossiers and canonical CREATE/inline
    event; provenance absolute artifact path/hash pairs independently rehashed.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: 51 absolute path/hash references representing33 unique retained artifacts
    match. Actual actor, date, target and sidecar agree; no earlier authorship is
    invented. Root authored the record and dossier; reviewer independently judged
    the underlying evidence.
  snapshot_sha256: 992432acc723c23fabc6578657b6fec467c3ce1f968ef3d3580dae8fee9925e7
- evidence_id: issue163
  kind: record_content
  reference: https://github.com/CultureBotAI/CMMMech/issues/163
  locator: Read-only live gh issue view163, title/body/OPEN state during review.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: The issue requests source assessment, controls/stages/denominator reconciliation,
    appropriate ownership, curation/history, independent review and gates; it does
    not require new experiments. The bounded accepted record addresses that assessment
    while retaining experimental questions. This review does not close or mutate the
    issue.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round53-final-terminal.json
  locator: Actual complete parent terminal receipt and all command logs read and SHA-256
    verified; native frozen input hashes unchanged.
  accessed_at: '2026-10-12T10:07:58Z'
  support: supports
  summary: Named validation and completed batch/nonempty/history/render checks supplement
    the scientific assessment. No unexecuted or prior-cohort result is claimed.
  snapshot_sha256: 87d8701e2f43cdccb46f2fd4e788c31593c8be134573a12a2b8d7cb419b3ab36
assessments:
- assessment_id: identity
  area: identity
  topic: Chemically generated liquor and species-level organism
  outcome: supported
  target_ids:
  - cmmmech:allanite-leachate
  evidence_ids:
  - main
  - taxonomy
  - search
  summary: Secondary-resource ownership is justified by extensive chemical conversion
    and redissolution, distinct from ore, concentrate, species and isolated product.
    The source-specific scope does not import constituent criticality.
  dimensions:
  - name: material_form
    value: Processed Halleck Creek REE liquor after HCl leaching, impurity removal,
      NaOH precipitation and HCl redissolution
    definition: Chemical processing defines this intermediate; no mineral phase identifier
      assigned
    evidence_ids:
    - main
  - name: organism
    value: Source-named I.orientalis SD108-derived JL04; species P.kudriavzevii NCBITaxon:4909
    definition: Engineered stock is described, not authenticated by the species taxon
    evidence_ids:
    - main
    - si
    - taxonomy
  - name: criticality
    value: No designation asserted
    definition: No inherited jurisdiction/list/edition from constituent REEs
    evidence_ids:
    - main
- assessment_id: mechanism
  area: evidence
  topic: Biogenic reagent and bounded precipitation observation
  outcome: supported
  target_ids:
  - cmmmech:allanite-leachate
  evidence_ids:
  - main
  - si
  - workbooks
  - peer_context
  summary: The record accurately separates culture-mediated reagent production from
    subsequent chemical precipitation. Real-liquor time/temperature are not borrowed
    from synthetic assays. Similar observed commercial and biogenic removal with n=1
    does not imply statistical equivalence or general superiority.
  dimensions:
  - name: biomass_state
    value: Supernatant after8000g30min centrifugation
    definition: REE stage does not expose ore or liquor to intact growing yeast
    evidence_ids:
    - main
  - name: conditions
    value: JL04 at30C,pH4,10%DO in100mL glucose-fed SC-URA bioreactors; precipitation
      atpH1.5 with source22.00/42.70g/L reagents
    definition: Production and precipitation conditions are separate; real-liquor
      duration/temperature unresolved
    evidence_ids:
    - main
    - si
  - name: controls
    value: 1M commercial oxalic acid; no documented matched parental-supernatant or
      uninoculated-medium real-liquor arm
    definition: Broth contribution and independent real-feed performance replication
      remain unresolved
    evidence_ids:
    - main
    - workbooks
  - name: outcome_denominator
    value: Over99% residual-solution TREE depletion near source-nominal2.7g/L dose
    definition: Source16-element grouping includesSc; corrected concentrations, volume
      convention and sequential samples are retained; no closed mass balance
    evidence_ids:
    - main
    - workbooks
  - name: phase_and_scale
    value: Synthetic single-Nd phase identification; real-liquor laboratory assay;
      TEA/LCA modeled
    definition: No mixed-product purity, plant operation or measured systemwide environmental
      performance
    evidence_ids:
    - main
    - si
- assessment_id: limitations
  area: evidence
  topic: Contradictions and negative/zero measurements
  outcome: supported
  target_ids:
  - cmmmech:allanite-leachate
  evidence_ids:
  - main
  - si
  - workbooks
  summary: Dose denominator, missing cells, negative apparent removals, Mn exception,
    Th/U zero conventions and unexplained reagent-batch mapping are explicit. No essential
    correction is needed to preserve the narrower observation.
- assessment_id: provenance
  area: provenance
  topic: Exact inputs, true history, evidence gap disposition and completed checks
  outcome: supported
  target_ids:
  - cmmmech:allanite-leachate
  evidence_ids:
  - contexts
  - issue163
  - gates
  summary: All five explicit native inputs match the frozen state. Source163 assessment
    requirements are addressed within review scope; scientific limitations remain
    visible, and only repository checks actually completed are included.
findings: []
actions: []
limitations:
- Real-liquor conditions have n=1 and no documented matched broth comparator; independent
  performance replication and matrix attribution remain unknown.
- Real-liquor precipitation temperature/time are not specified separately; synthetic
  overnight conditions cannot fill this gap.
- Nominal doses divide by100mL despite95mL biological starting volumes; sequential
  samples and dilution correction do not establish closed mass balance.
- Zero/censoring conventions, Th/U co-retention, negative apparent removals and the
  Mn<6% prose conflict remain source limitations.
- The42.70g/L reagent is not identified with the two displayed38.78/40.27g/L production
  observations.
- Synthetic-Nd diffraction and FTIR do not identify mixed real-liquor phases or establish
  product purity.
- No isolated ore-to-product yield, industrial deployment, measured full-process LCA
  or inherited criticality is claimed.
- Source and duplicate searches are bounded; not all economic supplements, historical
  raw roots or unextracted binary contents were semantically reviewed.
notes:
- The issue163 live state was OPEN at assessment. This review supports completion
  of its evidence-assessment objective subject to publication procedure; no GitHub
  mutation occurred.
- Original raw files and independent workbook extraction/arithmetic receipts remain
  outside Git. No curation-history event is added by this review.
tags:
- round53
- allanite-leachate
- independent
- scientific
```
