# Independent scientific review of greigite Thermococcales biomineralization

- Review: 20261011T211823Z-greigite-round34-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T21:13:08.020762Z
- Finished UTC: 2026-10-11T21:18:23.490280Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Both source-specific laboratory observations are defensible and preserve phase, control, quantitative and causal limits. No corrective findings. Required named and final cohort validation passed on unchanged reviewed inputs.

## Scope And Provenance

All fields, two mechanisms, sources, identity and distinct provenance events of one frozen mineral record.

Selection: Parent-assigned independent review of another curator's new greigite record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 38cef46aabbcb2b49536ed8c265c63646ff1da3d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:greigite | data/records/greigite.yaml | maintained | Greigite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:greigite | Reviewer executed; Checked 1 record(s); 0 failed.; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final frozen-cohort batch gate | passed | True | cmmmech:greigite | Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-batch.log (84e966930d55b1bbc3527e149d252fd1dfe7f3ec0454f71b71aaceb517ebf5c8). uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 195.87s (0:03:15)<br>Checked 194 record(s); 0 failed.<br>Checked 224 history record(s); 0 error(s). |
| Final frozen-cohort nonempty gate | passed | True | cmmmech:greigite | Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-nonempty.log (9a1c693b6ef6256da07b28e732785b92b62fc090e964b3303620f782db991cd9). Checked 194 record(s); 0 failed. |
| Final frozen-cohort history gate | passed | True | cmmmech:greigite | Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-history.log (70d4c90358c71eeb843da5b2f1b671d7ee9275ecd4d3c4dcb3330d4db4ed3d6f). Checked 224 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral and taxon identity

identity: supported. Targets: cmmmech:greigite.

Authoritative mineral and taxon assignments match the exact represented objects; FeS, pyrite, elemental Fe and greigite are not conflated. No constituent criticality imported.

### Culture state, sulfur feed and control contract

evidence: supported. Targets: cmmmech:greigite.

Both records accurately preserve 85 degrees C, nominal 5 mM FeSO4, early stationary 5 x 10^7 cells/mL, reducing/anoxic medium, pH adjusted before autoclaving and unknown incubation pH trajectory. Source-dependent sulfur versus L-cystine arms and phosphate carryover uncertainty remain explicit.

### Diffraction and bulk detection boundaries

evidence: supported. Targets: cmmmech:greigite.

Electron diffraction and lattice imaging support extracellular greigite; semiquantitative Fe/S alone would not. L-cystine microscopy presence and bulk non-detection are compatible with low abundance and different sampling times. Poorly ordered FeS is not silently renamed mackinawite.

### Relative fitted Fe speciation versus recovery

quantity: supported. Targets: cmmmech:greigite.

The sulfur-arm 160-hour 41% greigite, 49% pyrite, 11% FeS values are fitted Fe-species contributions, sum to 101%, and are not product masses or recovery percentages. The 98%/99.7% confidence-convention discrepancy is retained. Counts of crystals/patterns and triplicate growth do not establish mineralization biological replication.

### Phosphate association, model and survival claims

evidence: supported. Targets: cmmmech:greigite.

The association with iron-phosphate-rich debris supports a proposed precursor pathway, not a uniquely proven route. Oxidant and phosphate release are unresolved; CHESS phase suppression and chemical reference synthesis disallow universal biological-origin claims. ATP trends do not show greigite alone causes survival.

### Laboratory precipitation and deployment boundary

scope: supported. Targets: cmmmech:greigite.

The observed assemblages remain laboratory-scale products, without natural-ore extraction, isolated yield, magnetic recovery or industrial deployment. Scope is scientifically useful despite unresolved pathway details.

### Independent exact-byte review and checks

provenance: supported. Targets: cmmmech:greigite.

Reviewer authored mackinawite, not greigite, and did not edit this target. Native initial hashes remain exact; separate history events and all required validation receipts are coherent.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/greigite.yaml; Complete frozen record and all source-specific fields | supports | Input hashes captured natively before judgment remain unchanged; no maintained record or history edits by reviewer. |
| primary2018 | https://doi.org/10.1371/journal.pone.0201549; Complete 10-page PDF and JATS; methods, results, discussion, all five original publisher figure images | supports | T. prieurii mineralization methods and diffraction support extracellular greigite in a mixed mineral assemblage. Original Figure 2D/E supports phase assignment, Figure 4 distinguishes crystals, organic material and pyrite. Counts of diffraction patterns are not independent biological replicates. |
| si2018 | /private/tmp/cmm-round34-greigite-research/raw/gorlas2018-s1.docx; Original CHESS reports S1 and S2, complete extracted document text | supports | S1 predicts pyrite; S2 disables pyrite and several competing sulfides and predicts greigite. These are equilibrium-model outputs, not experimental abiotic controls or evidence that abiotic greigite is impossible. |
| si2018b | /private/tmp/cmm-round34-greigite-research/raw/gorlas2018-s2.docx; S2 full model report | supports | Phase suppression includes pyrite, marcasite and several other iron sulfides. Record correctly states pyrite suppression without asserting it is the only suppressed phase. |
| primary2022 | https://doi.org/10.1111/1462-2920.15915; Complete archived JATS/text; Experimental procedures; Table 1; all six original figure images | supports | KOD1/JCM12380 and sulfur-source arms verified. Microscopy detects sparse L-cystine greigite at 144 hours while the 160-hour bulk XANES fit does not; sulfur-arm fitted Fe-species contributions 41/49/11 sum to 101 as printed. Table 1 98% confidence and methods 99.7% conventions differ. No conversion to mass or recovery yield. |
| si2022 | /private/tmp/cmm-round34-greigite-research/raw/gorlas2022-media.zip; All original supplemental figures S1-S8, with captions in JATS and Appendix S1; extracted TIFF renderings independently viewed | supports | S6 is a 70-hour sulfur-arm abiotic SEM/EDX control, not a full matched phase-abundance time series. S2/S3 distinguish pyrite-bearing spherules; S4 shows early Fe/P cell debris; S5/S7 and S8 show cell/ATP observations without proving greigite causes survival. Image filenames are not numerical figure order; caption mapping was checked. |
| appendix2022 | /private/tmp/cmm-round34-greigite-research/raw/gorlas2022-media/EMI-24-626-s006.docx; Complete Appendix S1 methods and figure captions | supports | Greigite reference material was chemically synthesized from mixed Fe(II)/Fe(III) and sulfide, then aged three months. It is an analytical reference, distinct from culture-derived products. Phosphate release in the main study was explicitly unmeasured. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 official list, page 86 original rendered row | supports | Greigite is Fe2+Fe3+2S4, status A, IMA 1963-007. Retained same-day official PDF and original row visually inspected, not a new download. |
| prieurii | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1128108; Live official NCBI page, independently reopened; retained HTML | supports | Taxon 1128108 is species Thermococcus prieurii. Source methods do not supply a strain accession, correctly not invented. |
| kod1 | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=69014; Live official NCBI page, independently reopened; retained HTML | supports | Taxon 69014 is Thermococcus kodakarensis KOD1, matching the primary named strain JCM12380. |
| history | history/records/greigite/2026-10-11T210905Z-codex-c1e0b6.yaml; Entire canonical CREATE sidecar and separate inline event | supports | Actual Codex/GPT-6/codex actor and scope agree; sidecar 21:09:05Z and distinct inline 21:09:26.932628+00:00 are retained without fabricated prior authorship. |
| notices | /private/tmp/cmm-round34-greigite-independent/notices.json; Independent live exact-DOI correction/retraction searches and official taxonomy opens | supports | No affecting correction or retraction surfaced in the returned bounded result sets. Earlier related-abiotic search returned different chemical systems; these are discovery context only, not newly established mechanisms or a universal biogenicity claim. |
| dedup | /private/tmp/cmm-round34-greigite-independent/dedup.txt; rg --hidden --no-ignore --follow current data/records research reviews history | supports | Relevant greigite mentions in pyrite/mackinawite contexts do not denote the same mineral record. This review makes no machine-wide absence claim. |
| gates | /private/tmp/cmm-round34-final-terminal.json; All three terminal commands and their complete logs | supports | Required batch, nonempty and trusted-base history gates passed on unchanged exact target inputs: 308 passed, 3 skipped, 194 records, 224 histories. Reviewer separately executed named validation. |

## Limits And Additional Notes

- Cell-free controls and temporal comparisons do not isolate active metabolism, cell debris, templating and sulfur chemistry.
- No unique phosphate-to-greigite pathway, oxidant, measured phosphate release or causal survival benefit is established.
- Microscopy samples individual particles; bulk XANES detection and fitted species fractions have different denominators and limits.
- The original 2022 full PDF was unavailable; complete archived JATS, all six original main images, all eight original SI images and original Appendix S1 were independently assessed. No local PDF access is claimed.
- 2018 CHESS supplements are text model reports rather than new empirical controls.
- Bounded notice and conflict searches are not exhaustive; no newly returned later study is imported as fully reviewed evidence.
- Native inspect preceded judgment; final input hashes and parent log hashes independently verified.
- 2018 all five main images and two CHESS reports; 2022 all six main images, Table 1, eight supplementary figures and methods appendix assessed.
- Source limitations already qualified in the record are not manufactured corrective findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T211823Z-greigite-round34-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of greigite Thermococcales biomineralization
started_at: '2026-10-11T21:13:08.020762Z'
finished_at: '2026-10-11T21:18:23.490280Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Greigite was curated by /root/round27_superalloy. Reviewer authored
    mackinawite only in this cohort and did not edit greigite record/history/dossier.
    Shared worktree and curator-acquired artifacts are disclosed; complete original
    evidence was independently assessed after native input capture.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Both source-specific laboratory observations are defensible and preserve
  phase, control, quantitative and causal limits. No corrective findings. Required
  named and final cohort validation passed on unchanged reviewed inputs.
source:
  git_revision: 38cef46aabbcb2b49536ed8c265c63646ff1da3d
  state: working_tree
  inputs:
  - path: data/records/greigite.yaml
    sha256: ff4d81433f6a854621fa16213167ed62120b7aa73bc0e2dd684e76200c35a8e4
    role: target
  - path: history/records/greigite/2026-10-11T210905Z-codex-c1e0b6.yaml
    sha256: a4aeb2146ae2f930aaf2b02cd9c8928589db36d89b550c89d198b5106eff3e9c
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: All fields, two mechanisms, sources, identity and distinct provenance
    events of one frozen mineral record.
  selection: Parent-assigned independent review of another curator's new greigite
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:greigite
  exclusions:
  - target: Raw diffraction or XANES reprocessing and later studies
    reason: Original published evidence assessed; no raw-instrument refitting or new
      mechanism import.
targets:
- target_id: cmmmech:greigite
  path: data/records/greigite.yaml
  label: Greigite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/greigite.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked
    cmmmech validate data/records/greigite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed; Checked 1 record(s); 0 failed.; log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:greigite
- check_id: batch
  name: Final frozen-cohort batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-batch.log
    (84e966930d55b1bbc3527e149d252fd1dfe7f3ec0454f71b71aaceb517ebf5c8). uv run --locked
    --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 195.87s (0:03:15)

    Checked 194 record(s); 0 failed.

    Checked 224 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:greigite
- check_id: nonempty
  name: Final frozen-cohort nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-nonempty.log
    (9a1c693b6ef6256da07b28e732785b92b62fc090e964b3303620f782db991cd9). Checked 194
    record(s); 0 failed.
  target_ids:
  - cmmmech:greigite
- check_id: history
  name: Final frozen-cohort history gate
  command: uv run --locked cmmmech validate-history --base 38cef46aabbcb2b49536ed8c265c63646ff1da3d
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read and SHA256-verified /private/tmp/cmm-round34-final-history.log
    (70d4c90358c71eeb843da5b2f1b671d7ee9275ecd4d3c4dcb3330d4db4ed3d6f). Checked 224
    history record(s); 0 error(s).
  target_ids:
  - cmmmech:greigite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/greigite.yaml
  locator: Complete frozen record and all source-specific fields
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Input hashes captured natively before judgment remain unchanged; no maintained
    record or history edits by reviewer.
  snapshot_sha256: ff4d81433f6a854621fa16213167ed62120b7aa73bc0e2dd684e76200c35a8e4
- evidence_id: primary2018
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0201549
  locator: Complete 10-page PDF and JATS; methods, results, discussion, all five original
    publisher figure images
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: T. prieurii mineralization methods and diffraction support extracellular
    greigite in a mixed mineral assemblage. Original Figure 2D/E supports phase assignment,
    Figure 4 distinguishes crystals, organic material and pyrite. Counts of diffraction
    patterns are not independent biological replicates.
  snapshot_sha256: 03d0b58ac2fdc6b1f497bd47aeec4aaef0ab8a4de8fefb8b6e70b65c817f9223
- evidence_id: si2018
  kind: primary_source
  reference: /private/tmp/cmm-round34-greigite-research/raw/gorlas2018-s1.docx
  locator: Original CHESS reports S1 and S2, complete extracted document text
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: S1 predicts pyrite; S2 disables pyrite and several competing sulfides and
    predicts greigite. These are equilibrium-model outputs, not experimental abiotic
    controls or evidence that abiotic greigite is impossible.
  snapshot_sha256: 9a627910fff8762738b32a1043c5299ecd6b36e5a3b7107d5d346c6e12dd4631
- evidence_id: si2018b
  kind: primary_source
  reference: /private/tmp/cmm-round34-greigite-research/raw/gorlas2018-s2.docx
  locator: S2 full model report
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Phase suppression includes pyrite, marcasite and several other iron sulfides.
    Record correctly states pyrite suppression without asserting it is the only suppressed
    phase.
  snapshot_sha256: ebebbd959894d57f2317522ba8a909fce6faf5ff2df3c52f083be8825a268d32
- evidence_id: primary2022
  kind: primary_source
  reference: https://doi.org/10.1111/1462-2920.15915
  locator: Complete archived JATS/text; Experimental procedures; Table 1; all six
    original figure images
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: KOD1/JCM12380 and sulfur-source arms verified. Microscopy detects sparse
    L-cystine greigite at 144 hours while the 160-hour bulk XANES fit does not; sulfur-arm
    fitted Fe-species contributions 41/49/11 sum to 101 as printed. Table 1 98% confidence
    and methods 99.7% conventions differ. No conversion to mass or recovery yield.
  snapshot_sha256: 155ba224ada3e9b8ade6a400fec9df73424a95c98bbae8df9d4bed81894faeef
- evidence_id: si2022
  kind: primary_source
  reference: /private/tmp/cmm-round34-greigite-research/raw/gorlas2022-media.zip
  locator: All original supplemental figures S1-S8, with captions in JATS and Appendix
    S1; extracted TIFF renderings independently viewed
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: S6 is a 70-hour sulfur-arm abiotic SEM/EDX control, not a full matched
    phase-abundance time series. S2/S3 distinguish pyrite-bearing spherules; S4 shows
    early Fe/P cell debris; S5/S7 and S8 show cell/ATP observations without proving
    greigite causes survival. Image filenames are not numerical figure order; caption
    mapping was checked.
  snapshot_sha256: d4e3d59cf9280b2b6bc2281b3e561be08a185119f15b978e28ee83ad036c476d
- evidence_id: appendix2022
  kind: primary_source
  reference: /private/tmp/cmm-round34-greigite-research/raw/gorlas2022-media/EMI-24-626-s006.docx
  locator: Complete Appendix S1 methods and figure captions
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Greigite reference material was chemically synthesized from mixed Fe(II)/Fe(III)
    and sulfide, then aged three months. It is an analytical reference, distinct from
    culture-derived products. Phosphate release in the main study was explicitly unmeasured.
  snapshot_sha256: fecc13137b4b8f013613315e73d0caad4ee74257451acd712ea217e4c68f803b
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 official list, page 86 original rendered row
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Greigite is Fe2+Fe3+2S4, status A, IMA 1963-007. Retained same-day official
    PDF and original row visually inspected, not a new download.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: prieurii
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1128108
  locator: Live official NCBI page, independently reopened; retained HTML
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Taxon 1128108 is species Thermococcus prieurii. Source methods do not supply
    a strain accession, correctly not invented.
  snapshot_sha256: 3f793323f4ac9f8f683a05dfdf1bf53dfd51b01a56f70db89b8b78ec7d15c166
- evidence_id: kod1
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=69014
  locator: Live official NCBI page, independently reopened; retained HTML
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Taxon 69014 is Thermococcus kodakarensis KOD1, matching the primary named
    strain JCM12380.
  snapshot_sha256: 8757648aaa22640bbebd24612982dfc252641118aa34749286fb405d76f1d661
- evidence_id: history
  kind: record_content
  reference: history/records/greigite/2026-10-11T210905Z-codex-c1e0b6.yaml
  locator: Entire canonical CREATE sidecar and separate inline event
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Actual Codex/GPT-6/codex actor and scope agree; sidecar 21:09:05Z and distinct
    inline 21:09:26.932628+00:00 are retained without fabricated prior authorship.
  snapshot_sha256: a4aeb2146ae2f930aaf2b02cd9c8928589db36d89b550c89d198b5106eff3e9c
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round34-greigite-independent/notices.json
  locator: Independent live exact-DOI correction/retraction searches and official
    taxonomy opens
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: No affecting correction or retraction surfaced in the returned bounded
    result sets. Earlier related-abiotic search returned different chemical systems;
    these are discovery context only, not newly established mechanisms or a universal
    biogenicity claim.
  search_scope: Two exact DOI strings with correction retraction; first returned result
    sets, no pagination or time/domain filters. Earlier greigite Thermococcales abiotic
    query considered as counterevidence discovery. This does not prove global absence.
  snapshot_sha256: dde82ff108bcf387a1ad49881364b39ebbd5f04e0b91b1db65489c84246b7808
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round34-greigite-independent/dedup.txt
  locator: rg --hidden --no-ignore --follow current data/records research reviews
    history
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: Relevant greigite mentions in pyrite/mackinawite contexts do not denote
    the same mineral record. This review makes no machine-wide absence claim.
  search_scope: Current round34 worktree data/records, research, reviews and history;
    YAML/Markdown/JSON/text; ignored and hidden files included, symlinks followed.
    Query greigite|0201549|1462-2920.15915. Raw binary files assessed separately,
    not claimed greppable.
  snapshot_sha256: 531671101101ba1aaf14f39e151b99569450a133b7cbe108b0cc159aba8a496f
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round34-final-terminal.json
  locator: All three terminal commands and their complete logs
  accessed_at: '2026-10-11T21:18:23.490280Z'
  support: supports
  summary: 'Required batch, nonempty and trusted-base history gates passed on unchanged
    exact target inputs: 308 passed, 3 skipped, 194 records, 224 histories. Reviewer
    separately executed named validation.'
  snapshot_sha256: 5a57d3f8d6cb1555e588da6687ab9d2266293025c6301d9e950bff153ad2b14d
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral and taxon identity
  outcome: supported
  summary: Authoritative mineral and taxon assignments match the exact represented
    objects; FeS, pyrite, elemental Fe and greigite are not conflated. No constituent
    criticality imported.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - ima
  - prieurii
  - kod1
  - dedup
  dimensions:
  - name: material_form
    value: Mineral species; mixed laboratory precipitate
    definition: Greigite phase identified locally and, for one arm, by bulk spectroscopy;
      no ore or purified commodity identity.
    evidence_ids:
    - record
    - primary2018
    - primary2022
  - name: criticality
    value: Not asserted
    definition: No jurisdiction, list or edition claim is made.
    evidence_ids:
    - record
  - name: organisms
    value: T. prieurii species; T. kodakarensis KOD1 strain
    definition: Taxon ranks and primary strain availability are kept distinct.
    evidence_ids:
    - prieurii
    - kod1
    - primary2018
    - primary2022
- assessment_id: methods
  area: evidence
  topic: Culture state, sulfur feed and control contract
  outcome: supported
  summary: Both records accurately preserve 85 degrees C, nominal 5 mM FeSO4, early
    stationary 5 x 10^7 cells/mL, reducing/anoxic medium, pH adjusted before autoclaving
    and unknown incubation pH trajectory. Source-dependent sulfur versus L-cystine
    arms and phosphate carryover uncertainty remain explicit.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - primary2018
  - primary2022
  - si2022
  dimensions:
  - name: biomass_state
    value: Initially live early-stationary cultures; subsequent cell damage/debris
    definition: Later mineral nucleation does not establish an obligatory living-cell
      or enzymatic pathway.
    evidence_ids:
    - primary2018
    - primary2022
    - record
  - name: controls
    value: Cell-free controls; imperfect temporal and chemical matching
    definition: No matched full 144-160-hour quantified control series or separation
      of metabolism from cell-derived chemistry.
    evidence_ids:
    - record
    - si2022
    - primary2018
- assessment_id: phase
  area: evidence
  topic: Diffraction and bulk detection boundaries
  outcome: supported
  summary: Electron diffraction and lattice imaging support extracellular greigite;
    semiquantitative Fe/S alone would not. L-cystine microscopy presence and bulk
    non-detection are compatible with low abundance and different sampling times.
    Poorly ordered FeS is not silently renamed mackinawite.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - primary2018
  - primary2022
  - si2022
- assessment_id: quantity
  area: quantity
  topic: Relative fitted Fe speciation versus recovery
  outcome: supported
  summary: The sulfur-arm 160-hour 41% greigite, 49% pyrite, 11% FeS values are fitted
    Fe-species contributions, sum to 101%, and are not product masses or recovery
    percentages. The 98%/99.7% confidence-convention discrepancy is retained. Counts
    of crystals/patterns and triplicate growth do not establish mineralization biological
    replication.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - primary2018
  - primary2022
- assessment_id: causality
  area: evidence
  topic: Phosphate association, model and survival claims
  outcome: supported
  summary: The association with iron-phosphate-rich debris supports a proposed precursor
    pathway, not a uniquely proven route. Oxidant and phosphate release are unresolved;
    CHESS phase suppression and chemical reference synthesis disallow universal biological-origin
    claims. ATP trends do not show greigite alone causes survival.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - primary2018
  - si2018
  - si2018b
  - primary2022
  - si2022
  - appendix2022
- assessment_id: scope
  area: scope
  topic: Laboratory precipitation and deployment boundary
  outcome: supported
  summary: The observed assemblages remain laboratory-scale products, without natural-ore
    extraction, isolated yield, magnetic recovery or industrial deployment. Scope
    is scientifically useful despite unresolved pathway details.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - primary2018
  - primary2022
  dimensions:
  - name: outcome
    value: Observed culture-associated extracellular mineral formation
    definition: A mineral identity and conditional transformation observation rather
      than recovered product performance.
    evidence_ids:
    - record
    - primary2018
    - primary2022
  - name: deployment
    value: Laboratory batch
    definition: No field hydrothermal demonstration or industrial process established.
    evidence_ids:
    - record
- assessment_id: provenance
  area: provenance
  topic: Independent exact-byte review and checks
  outcome: supported
  summary: Reviewer authored mackinawite, not greigite, and did not edit this target.
    Native initial hashes remain exact; separate history events and all required validation
    receipts are coherent.
  target_ids:
  - cmmmech:greigite
  evidence_ids:
  - record
  - history
  - gates
  - notices
findings: []
actions: []
limitations:
- Cell-free controls and temporal comparisons do not isolate active metabolism, cell
  debris, templating and sulfur chemistry.
- No unique phosphate-to-greigite pathway, oxidant, measured phosphate release or
  causal survival benefit is established.
- Microscopy samples individual particles; bulk XANES detection and fitted species
  fractions have different denominators and limits.
- The original 2022 full PDF was unavailable; complete archived JATS, all six original
  main images, all eight original SI images and original Appendix S1 were independently
  assessed. No local PDF access is claimed.
- 2018 CHESS supplements are text model reports rather than new empirical controls.
- Bounded notice and conflict searches are not exhaustive; no newly returned later
  study is imported as fully reviewed evidence.
notes:
- Native inspect preceded judgment; final input hashes and parent log hashes independently
  verified.
- 2018 all five main images and two CHESS reports; 2022 all six main images, Table
  1, eight supplementary figures and methods appendix assessed.
- Source limitations already qualified in the record are not manufactured corrective
  findings.
links:
- https://doi.org/10.1371/journal.pone.0201549
- https://doi.org/10.1111/1462-2920.15915
```
