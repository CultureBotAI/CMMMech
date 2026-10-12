# Independent scientific review of monazite ore: initial locator finding

- Review: 20261012T084101Z-monazite-ore-round51-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T08:35:13Z
- Finished UTC: 2026-10-12T08:41:01Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Mixed-feed biofilm and qualitative alteration claims are appropriately bounded. One minor S12 figure-to-claim locator mismatch needs correction; other source/control uncertainties are retained.

## Scope And Provenance

Entire new monazite-ore record and actual provenance; complete primary13pages and all mainfigures, fullAppendixS1 text/tables/availableembeddedgraphics plus sampledvideo.

Selection: Independent review of newly curated resource
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 466cb14cbc271ba73ba05e89ed188cfd113d06ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:monazite-ore | data/records/monazite-ore.yaml | maintained | Monazite ore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-file validation | passed | True | cmmmech:monazite-ore | Actually completed1record/0failed. Raw log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Coordinator initial cohort batch | passed | True | cmmmech:monazite-ore | Completed on original frozen bytes; independently read raw log and verified SHA256 138fa7877c8c2d7365f17d35606c7ece6d6f2bdb0debaff0a9042ee308b5027c. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 22%]<br>........................................................................ [ 45%]<br>........................................................................ [ 67%]<br>.............................................................sss........ [ 90%]<br>................................                                         [100%]<br>317 passed, 3 skipped in 197.77s (0:03:17)<br>Checked 249 record(s); 0 failed.<br>Checked 294 history record(s); 0 error(s).<br> |
| Coordinator initial cohort nonempty | passed | True | cmmmech:monazite-ore | Completed on original frozen bytes; independently read raw log and verified SHA256 06b051452e7949992afa10ca6afb43fcde683c0e3fcbd9ec1827b3fc360a702b. Checked 249 record(s); 0 failed.<br> |
| Coordinator initial cohort history | passed | True | cmmmech:monazite-ore | Completed on original frozen bytes; independently read raw log and verified SHA256 534de7ca88921ec9466d980eda984e27b807ecc018a14caa60d77192e296e563. Checked 294 history record(s); 0 error(s).<br> |
| Coordinator initial cohort render-check | passed | False | cmmmech:monazite-ore | Completed on original frozen bytes; independently read raw log and verified SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run python scripts/render_pages.py --check<br>pages/ is current<br> |

## Scientific And Domain Assessments

### Heterogeneous resource ownership

identity: supported. Targets: cmmmech:monazite-ore.

Primary-resource owner is justified and separated from mineral species and criticality.

Lynas supplied high-grade ore, mine unspecified. Monazite-group model65wt% is crystalline-only, totals101 versusprinted100, conflicting refinement/reference patterns and overlapping peaks retained. No wholefeedcommercialgrade or species-specific mechanism.

### Organism and experimental conditions

evidence: supported. Targets: cmmmech:monazite-ore.

Actual culture/pretreatments are described with meaningful limits.

Living ATCC13048 culture; enumeration aliquots fixed rather than entire inoculum. Gamma50kGy11h,50–200micrometre versus0.5–2mm unresolved; mounted specimens and1%slurry live-imaging separate. Growth dependence on mineralphosphate is unproven without documented washing/orefree control.

### Microscopy and causal limits

evidence: supported. Targets: cmmmech:monazite-ore.

Qualitative observation supported; quantitative extraction and causal pathways not asserted.

Sterilemedium/water controls exist but pH6/5/4 versus7/5/4 conflict, no matchedtrajectory/replicatecount/erosionstatistics. Figure5 representative differentgrains, not registered beforeafter. Hoechst/DiTO fluorescence not livecellcount, epoxy background acknowledged; SEM independently supports attachment. Phase-selectivity null limited to examinedfields.

### Exact-byte context and checks

provenance: supported. Targets: cmmmech:monazite-ore.

Explicit native capture and actual validation are bound.

Record, CREATE, both dossiers and schema explicitly inspected before judgment. Reviewer did not author target or edit it. One minor figure-to-claim locator needs correction; scientific outcome otherwise bounded.

## Findings

### F1: Appendix Figure S12 is attached to the wrong microscopy claim

minor / open / confirmed; issue key: CMMMech.monazite-ore.s12-evidence-locator.

The first evidence explanation attributes roughness localization to mainFigure3E/F and AppendixFigureS12. OriginalS12 caption identifies CLSM cross-sections of mature biofilm; mainResults1794 cites S12 withFigure2 for thin-layer structure. Roughness localization is supported by main3E/F. Move the S12 locator to the thin-layer sentence and leave main3E/F as the roughness locator. This changes evidential attribution, not the accepted observation.

## Recommended Actions And Acceptance Checks

### A1

Move S12 locator to thin-layer observation, append actual EDIT/inline provenance and correction dossier, preserve initial CREATE/dossier/review.

- Corrected statement matches mainResults1794 and originalS12 caption; roughness locator remains main3E/F.
- Named and affected cohort/history/render checks pass on corrected bytes.
- Save fresh native successor linking exact initial F1 and GitHub issue, after independent correction assessment.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/records/monazite-ore.yaml; Whole native-inspected frozen record | supports | Every maintained material, culture, conditions, controls, outcome and limitation statement assessed against source. |
| primary | https://doi.org/10.1111/1751-7915.14260; Complete13-page original PDF,1790–1802; all5original figures and Methods/Results/Discussion personally inspected. | supports | Natural mixed feed from Lynas with unspecified mine; K.aerogenes laboratory surface colonization and qualitative erosion. Results1794 assigns S12 to thin-layer structure and main3E/F to roughness localization. |
| appendix | https://pmc-oa-opendata.s3.amazonaws.com/PMC10443343.1/MBT2-16-1790-s001.docx; All AppendixS1 text/four tables; all59 embedded PNG/JPEG/TIFF images viewed through10contact sheets, relevantS2/S7/S10/S12 individually enlarged; FiguresS1–S16. | supports | S12 caption describes CLSM cross-section of mature ore biofilm, not the specific roughness-localization experiment. Phase tables/control images support preserved uncertainty. Nine WDP alternate encodings were not decoded; paired fallback graphics were inspected. DOCX print layout not rendered. |
| video | https://pmc-oa-opendata.s3.amazonaws.com/PMC10443343.1/MBT2-16-1790-s002.zip; All three original video files inventory; six time-distributed decoded frames per clip personally viewed via three contact sheets; sampling receipt inspected. | supports | Approx16/48/32second depth-coded rotations are viewing displays, not a continuous culture experiment. No fullframe movie playback, viability or dissolution-rate inference claimed. |
| identity | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548&amp;mode=Info; Live NCBI548 and officialATCC13048 search results, retained same-day XML/HTML receipts. | supports | 548 correctly maps K.aerogenes species and ATCC13048 catalog maps NCDC819-56/former Enterobacter name; neither authenticates experimental stock. |
| notices | /private/tmp/cmm-round51-monazite-independent/web-evidence.json; Exact DOI and title with correction/erratum/retraction/conflicting terms; officialPMC record and current authority results. | supports | Bounded returned results identified primary and later review context, no affecting notice. No global absence conclusion. |
| dedup | /private/tmp/cmm-round51-monazite-independent/dedup.log; Current scientific dirs exact14260/PMC10443343/material term search with rg --no-ignore --hidden --follow. | supports | Current record and handoffs match this experiment; prior crystal/concentrate/mineral owners remain distinct. Author broader raw-root dedup receipt read with declared boundaries, not a machine-wide independent search. |
| artifacts | /private/tmp/cmm-round51-monazite-independent/evidence-check.json; 211 declared source/artifact hashes recomputed independently. | supports | All bytes match handoff; original observed coverage is stated separately and does not equate hash verification with visual inspection. |
| history | history/records/monazite-ore/2026-10-12T082924Z-codex-7eb1e5.yaml; Canonical CREATE and distinct inlineevent | supports | Actor/model, timestamp and target agree with new primary-resource owner. |
| gates | /private/tmp/cmm-round51-final-terminal.json; Four actual initial cohort commands and independent named check. | supports | All passed; scientific finding persists despite structural validity. |

## Limits And Additional Notes

- S12 locator finding unresolved; no record mutation by reviewer.
- Qualitative microscopy does not establish molecular mechanism, REE recovery, livecell viability, orephosphate growth dependence or industrial deployment.
- Natural mixedfeed heterogeneity, source size/controlpH/QXRD conflicts, missing matchedtrajectories and quantitativeerosion remain explicit.
- Embedded raster graphics inspected, nine WDP alternates notdecoded; video sampled rather than every frame.
- Searches bounded; no claimed complete literature absence or experimental replication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T084101Z-monazite-ore-round51-initial
kind: record
repository: CultureBotAI/CMMMech
title: 'Independent scientific review of monazite ore: initial locator finding'
started_at: '2026-10-12T08:35:13Z'
finished_at: '2026-10-12T08:41:01Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Peer /root/round27_packaging authored monazite ore/history/dossier.
    Reviewer authored only separate elpidite, inspected exact target/context before
    judgment, independently read primary/SI and original graphics/video samples, and
    did not edit target.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Mixed-feed biofilm and qualitative alteration claims are appropriately bounded.
  One minor S12 figure-to-claim locator mismatch needs correction; other source/control
  uncertainties are retained.
source:
  git_revision: 466cb14cbc271ba73ba05e89ed188cfd113d06ea
  state: working_tree
  inputs:
  - path: data/records/monazite-ore.yaml
    sha256: 37c301ad96d2992289489748490ca48567b3f0e0f0f9d8f9b6d893dcbecdd3c6
    role: target
  - path: history/records/monazite-ore/2026-10-12T082924Z-codex-7eb1e5.yaml
    sha256: 0545df8726c7600df1ec37b900991ef4b9c38d82139fc43ee79e9796b8396758
    role: context
  - path: research/sources/round51-monazite-feed/20261012T083200Z-source-investigation.json
    sha256: 74555edff5a510fa535d6cad0424ef9e9e5a2f9e7a5461d9187aeac902ab6364
    role: context
  - path: research/sources/round51-monazite-feed/20261012T083200Z-source-investigation.md
    sha256: 495fdd139eb4d3e7acf0f15661218dd264cf7ac5572b569b38e9fc9cee4a56d7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:monazite-ore
  path: data/records/monazite-ore.yaml
  label: Monazite ore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-ore.yaml
    role: maintained scientific record
scope:
  description: Entire new monazite-ore record and actual provenance; complete primary13pages
    and all mainfigures, fullAppendixS1 text/tables/availableembeddedgraphics plus
    sampledvideo.
  selection: Independent review of newly curated resource
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:monazite-ore
  exclusions:
  - target: Nine WDP alternate encodings and continuous full-video playback
    reason: Paired raster fallbacks and six evenly distributed frames per video inspected;
      no stronger visual coverage claimed.
  - target: Prior2017–2018 experiments and global literature completeness
    reason: Context citations not imported as this study measurements; boundednotice/dedupchecks
      only.
checks:
- check_id: named
  name: Independent named-file validation
  command: uv run --locked cmmmech validate data/records/monazite-ore.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:monazite-ore
  summary: Actually completed1record/0failed. Raw log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- check_id: batch
  name: Coordinator initial cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:monazite-ore
  summary: 'Completed on original frozen bytes; independently read raw log and verified
    SHA256 138fa7877c8c2d7365f17d35606c7ece6d6f2bdb0debaff0a9042ee308b5027c. uv run
    --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 22%]

    ........................................................................ [ 45%]

    ........................................................................ [ 67%]

    .............................................................sss........ [ 90%]

    ................................                                         [100%]

    317 passed, 3 skipped in 197.77s (0:03:17)

    Checked 249 record(s); 0 failed.

    Checked 294 history record(s); 0 error(s).

    '
- check_id: nonempty
  name: Coordinator initial cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:monazite-ore
  summary: 'Completed on original frozen bytes; independently read raw log and verified
    SHA256 06b051452e7949992afa10ca6afb43fcde683c0e3fcbd9ec1827b3fc360a702b. Checked
    249 record(s); 0 failed.

    '
- check_id: history
  name: Coordinator initial cohort history
  command: uv run --locked cmmmech validate-history --base 466cb14cbc271ba73ba05e89ed188cfd113d06ea
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:monazite-ore
  summary: 'Completed on original frozen bytes; independently read raw log and verified
    SHA256 534de7ca88921ec9466d980eda984e27b807ecc018a14caa60d77192e296e563. Checked
    294 history record(s); 0 error(s).

    '
- check_id: render-check
  name: Coordinator initial cohort render-check
  command: just render-check
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - cmmmech:monazite-ore
  summary: 'Completed on original frozen bytes; independently read raw log and verified
    SHA256 be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6. uv run
    python scripts/render_pages.py --check

    pages/ is current

    '
evidence:
- evidence_id: target
  kind: record_content
  reference: data/records/monazite-ore.yaml
  locator: Whole native-inspected frozen record
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Every maintained material, culture, conditions, controls, outcome and limitation
    statement assessed against source.
  snapshot_sha256: 37c301ad96d2992289489748490ca48567b3f0e0f0f9d8f9b6d893dcbecdd3c6
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1111/1751-7915.14260
  locator: Complete13-page original PDF,1790–1802; all5original figures and Methods/Results/Discussion
    personally inspected.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Natural mixed feed from Lynas with unspecified mine; K.aerogenes laboratory
    surface colonization and qualitative erosion. Results1794 assigns S12 to thin-layer
    structure and main3E/F to roughness localization.
  snapshot_sha256: 8dffc5c0d31032fb45105d2dc824048f846bcb55d3f39cc2e4985ca3629660bd
- evidence_id: appendix
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10443343.1/MBT2-16-1790-s001.docx
  locator: All AppendixS1 text/four tables; all59 embedded PNG/JPEG/TIFF images viewed
    through10contact sheets, relevantS2/S7/S10/S12 individually enlarged; FiguresS1–S16.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: S12 caption describes CLSM cross-section of mature ore biofilm, not the
    specific roughness-localization experiment. Phase tables/control images support
    preserved uncertainty. Nine WDP alternate encodings were not decoded; paired fallback
    graphics were inspected. DOCX print layout not rendered.
  snapshot_sha256: 72a855635fc6d7736daf87f8201be14115d3937bd0f31fcd3f6985ac67b36e0c
- evidence_id: video
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10443343.1/MBT2-16-1790-s002.zip
  locator: All three original video files inventory; six time-distributed decoded
    frames per clip personally viewed via three contact sheets; sampling receipt inspected.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Approx16/48/32second depth-coded rotations are viewing displays, not a
    continuous culture experiment. No fullframe movie playback, viability or dissolution-rate
    inference claimed.
  snapshot_sha256: d5842ce6fc16c28d70f60fbdf79fd25814bc092fc47b319957da9d4e037c562f
- evidence_id: identity
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=548&mode=Info
  locator: Live NCBI548 and officialATCC13048 search results, retained same-day XML/HTML
    receipts.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: 548 correctly maps K.aerogenes species and ATCC13048 catalog maps NCDC819-56/former
    Enterobacter name; neither authenticates experimental stock.
  snapshot_sha256: f914aa1c38a4d91b2261a70838294382f5d982bf109095660630f02517121449
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round51-monazite-independent/web-evidence.json
  locator: Exact DOI and title with correction/erratum/retraction/conflicting terms;
    officialPMC record and current authority results.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Bounded returned results identified primary and later review context, no
    affecting notice. No global absence conclusion.
  snapshot_sha256: f914aa1c38a4d91b2261a70838294382f5d982bf109095660630f02517121449
  search_scope: Four live exact DOI/title/taxon/catalog queries; returned results
    only, no exhaustive literature or biological replication.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round51-monazite-independent/dedup.log
  locator: Current scientific dirs exact14260/PMC10443343/material term search with
    rg --no-ignore --hidden --follow.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Current record and handoffs match this experiment; prior crystal/concentrate/mineral
    owners remain distinct. Author broader raw-root dedup receipt read with declared
    boundaries, not a machine-wide independent search.
  snapshot_sha256: 84ca17281ca8a1ee42fec3b3d6a2d5fccc70e97826469d224170fa7397751eb7
  search_scope: Hidden/ignored/followed current data/records,research,reviews,history
    text; unextracted binaries and unrelated paths excluded; broader author raw-root
    receipt separately inspected.
- evidence_id: artifacts
  kind: record_content
  reference: /private/tmp/cmm-round51-monazite-independent/evidence-check.json
  locator: 211 declared source/artifact hashes recomputed independently.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: All bytes match handoff; original observed coverage is stated separately
    and does not equate hash verification with visual inspection.
  snapshot_sha256: 2c35a45b9682ca41328c287b20113b124656b4678cc33973be78a676595e6639
- evidence_id: history
  kind: record_content
  reference: history/records/monazite-ore/2026-10-12T082924Z-codex-7eb1e5.yaml
  locator: Canonical CREATE and distinct inlineevent
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: Actor/model, timestamp and target agree with new primary-resource owner.
  snapshot_sha256: 0545df8726c7600df1ec37b900991ef4b9c38d82139fc43ee79e9796b8396758
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round51-final-terminal.json
  locator: Four actual initial cohort commands and independent named check.
  accessed_at: '2026-10-12T08:41:01Z'
  support: supports
  summary: All passed; scientific finding persists despite structural validity.
  snapshot_sha256: 4fd864559f58298f65698cb37b12dba04f230471fa4501ad962e42eab302a740
assessments:
- assessment_id: material
  area: identity
  topic: Heterogeneous resource ownership
  outcome: supported
  target_ids:
  - cmmmech:monazite-ore
  evidence_ids:
  - target
  - primary
  - appendix
  - dedup
  summary: Primary-resource owner is justified and separated from mineral species
    and criticality.
  details: Lynas supplied high-grade ore, mine unspecified. Monazite-group model65wt%
    is crystalline-only, totals101 versusprinted100, conflicting refinement/reference
    patterns and overlapping peaks retained. No wholefeedcommercialgrade or species-specific
    mechanism.
- assessment_id: culture
  area: evidence
  topic: Organism and experimental conditions
  outcome: supported
  target_ids:
  - cmmmech:monazite-ore
  evidence_ids:
  - primary
  - identity
  summary: Actual culture/pretreatments are described with meaningful limits.
  details: Living ATCC13048 culture; enumeration aliquots fixed rather than entire
    inoculum. Gamma50kGy11h,50–200micrometre versus0.5–2mm unresolved; mounted specimens
    and1%slurry live-imaging separate. Growth dependence on mineralphosphate is unproven
    without documented washing/orefree control.
- assessment_id: controls
  area: evidence
  topic: Microscopy and causal limits
  outcome: supported
  target_ids:
  - cmmmech:monazite-ore
  evidence_ids:
  - primary
  - appendix
  - video
  summary: Qualitative observation supported; quantitative extraction and causal pathways
    not asserted.
  details: Sterilemedium/water controls exist but pH6/5/4 versus7/5/4 conflict, no
    matchedtrajectory/replicatecount/erosionstatistics. Figure5 representative differentgrains,
    not registered beforeafter. Hoechst/DiTO fluorescence not livecellcount, epoxy
    background acknowledged; SEM independently supports attachment. Phase-selectivity
    null limited to examinedfields.
- assessment_id: provenance
  area: provenance
  topic: Exact-byte context and checks
  outcome: supported
  target_ids:
  - cmmmech:monazite-ore
  evidence_ids:
  - target
  - history
  - artifacts
  - gates
  summary: Explicit native capture and actual validation are bound.
  details: Record, CREATE, both dossiers and schema explicitly inspected before judgment.
    Reviewer did not author target or edit it. One minor figure-to-claim locator needs
    correction; scientific outcome otherwise bounded.
findings:
- finding_id: F1
  issue_key: CMMMech.monazite-ore.s12-evidence-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Appendix Figure S12 is attached to the wrong microscopy claim
  description: The first evidence explanation attributes roughness localization to
    mainFigure3E/F and AppendixFigureS12. OriginalS12 caption identifies CLSM cross-sections
    of mature biofilm; mainResults1794 cites S12 withFigure2 for thin-layer structure.
    Roughness localization is supported by main3E/F. Move the S12 locator to the thin-layer
    sentence and leave main3E/F as the roughness locator. This changes evidential
    attribution, not the accepted observation.
  target_ids:
  - cmmmech:monazite-ore
  field_paths:
  - mechanisms[0].evidence[0].explanation
  evidence_ids:
  - target
  - primary
  - appendix
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-ore.yaml
    role: maintained scientific record
  rule_id: primary-figure-to-claim-fidelity
  native_severity: minor
  normalization_reason: Narrow locator mismatch; material identity, biofilm observation
    and qualitative erosion remain supported.
actions:
- action_id: A1
  description: Move S12 locator to thin-layer observation, append actual EDIT/inline
    provenance and correction dossier, preserve initial CREATE/dossier/review.
  finding_ids:
  - F1
  target_ids:
  - cmmmech:monazite-ore
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/monazite-ore.yaml
    role: maintained scientific record
  acceptance_checks:
  - Corrected statement matches mainResults1794 and originalS12 caption; roughness
    locator remains main3E/F.
  - Named and affected cohort/history/render checks pass on corrected bytes.
  - Save fresh native successor linking exact initial F1 and GitHub issue, after independent
    correction assessment.
limitations:
- S12 locator finding unresolved; no record mutation by reviewer.
- Qualitative microscopy does not establish molecular mechanism, REE recovery, livecell
  viability, orephosphate growth dependence or industrial deployment.
- Natural mixedfeed heterogeneity, source size/controlpH/QXRD conflicts, missing matchedtrajectories
  and quantitativeerosion remain explicit.
- Embedded raster graphics inspected, nine WDP alternates notdecoded; video sampled
  rather than every frame.
- Searches bounded; no claimed complete literature absence or experimental replication.
tags:
- round51
- independent-scientific-review
- monazite-ore
- initial
```
