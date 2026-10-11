# Independent scientific review of chalcocite community-associated leaching indices

- Review: 20261011T203735Z-chalcocite-round33-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T20:34:18.130769Z
- Finished UTC: 2026-10-11T20:37:35.986017Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen chalcocite record accurately preserves a community-associated source-reported leaching observation and its numerical, material and causal limits. No corrective finding identified. Full original primary, allfigures/tables/equations and mineral identity were assessed independently. Named and finalcohort checks pass with unchanged exact inputs.

## Scope And Provenance

Everyfield ofone newmineralrecord, its mechanism/evidence/sources and separateCREATE/inline provenance.

Selection: Parent assigned frozenrecord authored byotheragent inround33.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bee4f42bb622ae0a0999f8f3e3dac31f14282278.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chalcocite | data/records/chalcocite.yaml | maintained | Chalcocite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:chalcocite | Reviewer executed successfully: Checked1record;0failed. Log /private/tmp/cmm-round33-chalcocite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final frozen-cohort batch gate | passed | True | cmmmech:chalcocite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round33-final-batch.log SHA256 4ca5dc5133c70847781db60f3ac8024963b461a718c7fc9083c43e10ec5d4d32. uv run --locked --extra dev python scripts/check.py All checks passed! ........................................................................ [ 23%] ........................................................................ [ 46%] ........................................................................ [ 69%] ....................................................sss................. [ 92%] .......................                                                  [100%] 308 passed, 3 skipped in 129.87s (0:02:09) Checked 190 record(s); 0 failed. Checked 219 history record(s); 0 error(s). |
| Final frozen-cohort nonempty gate | passed | True | cmmmech:chalcocite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round33-final-nonempty.log SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299. Checked 190 record(s); 0 failed. |
| Final frozen-cohort history gate | passed | True | cmmmech:chalcocite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round33-final-history.log SHA256 5fdfb5898956d9c86e8d8c3976c1c07f567b349cb0cbeae4a4385905857b70a1. Checked 219 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral identity, experimental mixture and criticality boundary

identity: supported. Targets: cmmmech:chalcocite.

Cu2S is verified at IMA. Table2 values and source-labelled92.40%purity are faithfully reported as composition, not a independently quantified endmember phase fraction. Natural separate is distinct from element, mixedore and synthetic reagent.

### Community, assay conditions and controls

evidence: supported. Targets: cmmmech:chalcocite.

Mineheap-sump community,4–5day laboratory adaptation,9Kmedium,30°C,14days,initialpH1.8 and1:10inoculum:pulp align with Sections2.2/4.1–4.2 and Figure4. Exact medium recipe,solidmass,workingvolume,flaskagitation,washing and subsequentpHcontrols remain unavailable. The rawore reactor5%loading/120rpm are correctly separated.

### Direction of equation and source-reported indices

quantity: supported. Targets: cmmmech:chalcocite.

Original Equation2 on18286 is E=1−(CVM/alpha m)×100% without resolving concentrations/units. SinceCis defined as solution concentration, its direction conflicts with extraction interpretation. Record preserves only plotted indices, not reconstructed yields. Figure4 indeed shows copper comparators similaratday2, followed by higher inoculated indices; ironindices also rise. Table2exactnumbers are correct.

### Community association versus mineral-selective or molecular cause

evidence: supported. Targets: cmmmech:chalcocite.

Taxa inFigure6are relative sequence abundances fromseparatemineral assays; paper alternates attachedsample wording withsolutionDNA harvesting. These do not determine taxa contributions to the mixed assay. Ferric attack,sulfur oxidation,galvanic effects,electronic vacancies and two-stageprocess remain interpretations. Correctly no verified exclusive Cu-onlyselectivity,enzyme mechanism or phase-conversion measurement is claimed.

### Laboratory scope and unadopted wider claims

scope: supported. Targets: cmmmech:chalcocite.

Industrial mine origin is not industrial deployment. The record curates the separate-mixture flask result, not the rawore reactor nor modeledtwo-stage separation. Relatedsource leads with differentfeed/potentialcontrol do not refute this deliberately bounded observation.

### Exact scientific state, primary ownership and completed gates

provenance: supported. Targets: cmmmech:chalcocite.

Frozenrecord/history/schema hashes are identicalininitialandfinal nativecaptures. PDF/JATS and independently openedPMC verify sourceidentity despite unavailableCrossrefresponse. CanonicalCREATE and inlineevent are coherent. Named and allfinalcohort gates passed; no maintainedfile was changed bythisreviewer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/chalcocite.yaml; Complete frozen maintained record, all fields | supports | Record retains natural-separate identity, reported leaching-index comparison and explicit numerical/causal limits. |
| primary | https://doi.org/10.1021/acsomega.9b02294; Complete original10-page PDF, Sections1–4, Figures1–13, Tables1–5 and Equations1–2; every original page visually inspected and full text read. | supports | Natural Zijinshan separates and mine-sump community are supported. Figure4 shows similar early copper indices and higher later inoculated values; iron indices also increase. Equation2 has a subtractive direction incompatible with increasing solution concentration. Methods and figure captions support the limited assay scope and do not supply the missing mass/volume/sterility details. |
| xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC6844112/; Complete original JATS inspected; independently live-opened PMC article corroborates identity. | supports | JATS contains13figures,5table-wraps and no supplementary-material nodes. The retained ZIP contains32image renditions, representing article figures, equations and graphical abstract, not a separate experimental supplement. Original PDF/JATS/PMC are related artifacts of one experiment, not independent replications. |
| archive | /private/tmp/cmm-round33-chalcocite-research/raw/wu2019-supplementary.zip; Complete ZIP member inventory inspected | supports | All32members are article JPG/GIF images. Main-page originals were visually checked; no separate raw assay table or additional methods was found inside this archive. Filename supplementary.zip does not establish an experimental supplement. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Retained September2026 original PDFpage40 chalcocite row; column definitions onpage1 | supports | Independently inspected chalcocite row:Cu2S,statusG,1751. Grandfathered mineral identity and original-description year match. Same-day retained authority reused, not claimed as fresh download. Record assigns no synthetic-reagent identity or elemental criticality. |
| history | history/records/chalcocite/2026-10-11T202953Z-codex-610893.yaml; Complete canonical CREATE sidecar and separate inline event | supports | Actual20:29:53Z Codex/GPT-6/codex CREATE targets this file and reports accurate scope; inline event20:29:59Z is separate. It does not claim already-completed independent review or backdated curation. |
| dedup | /private/tmp/cmm-round33-chalcocite-independent/dedup.json; Reviewer executed hidden/ignored-inclusive symlink-following search and inspected current/original record hits | supports | Accepted chalcocite root is distinct from contextual mentions of transient chalcocite in chalcopyrite and comparison naming in bornite. Current source research and historical raw references are not duplicate accepted roots. Search completed0 with empty stderr,592matching lines. |
| notices | Independent web searches11October2026; First returned result sets and original PMC article reopened | supports | No affecting correction/retraction surfaced in these bounded results. Related redox-control studies use distinct chalcopyrite/pyrite feeds and do not establish a contradictory result for the exact chalcocite assay. Secondary/wiki results were not used as evidence. Crossref local file is empty and independent live Crossref web-open failed, so no clean-Crossref assertion is made. |
| gates | /private/tmp/cmm-round33-final-terminal.json; All3terminal command entries, corresponding complete logs and final native recapture | supports | All gates completed0;308passed3skipped129.87s,190records219histories. Reviewer independently read and SHA-256 verified logs. Final target/history/schema inputs exactly match initial native capture. |

## Limits And Additional Notes

- The printedpercent equation and missingoriginalconcentrations/masses/volumes prevent verifiedextraction or chalcociteconversion yields.
- Natural mineral separates lack quantitatively establishedendmember phase fractions; othercopper phases are notexcluded.
- Uninoculated comparison hasno verifiedsterility or matched dynamicpH/potential; chemicalconditions confound isolatedmicrobial causality.
- Communityrelativeabundances and ambiguoussolution-versus-attachedDNA fraction do not establish organism-specific mechanisms.
- Exactflaskloading/workingvolume/agitation/mediumrecipe and inoculumcell-densitybasis remain incomplete.
- Crossref localfilewas empty and independentlivewebopen failed; originalPDF/JATS/livePMC establishbibliography, but no cleanCrossrefnotice result isclaimed. Correction/counterevidencesearch wasbounded.
- All10originalpages,13figures,5tables and2equations independentlyinspected. No maintainedtarget/history/dossieredited.
- No correctiveissueisinvented from honestlydeclared primary-source limitations.
- Initialinspect attempt included an unsupportedcontext_paths key andwasrejected; correctednativeinspect with --input succeeded beforejudgment and finalcapturewasidentical.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T203735Z-chalcocite-round33-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of chalcocite community-associated leaching indices
started_at: '2026-10-11T20:34:18.130769Z'
finished_at: '2026-10-11T20:37:35.986017Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Another agent authored chalcocite. Reviewer authored only molybdenite
    extension and its research in this round, did not edit chalcocite record/history/dossier,
    and captured exact native inputs before scientific judgment. Shared worktree and
    curator-acquired raw files are disclosed. Reviewer independently read complete10-page
    primary, all13figures/5tables/2equations, IMA row, JATS/archive and live PMC/notices.
    Root executed cohort gates; reviewer read and hashed their terminal logs.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen chalcocite record accurately preserves a community-associated
  source-reported leaching observation and its numerical, material and causal limits.
  No corrective finding identified. Full original primary, allfigures/tables/equations
  and mineral identity were assessed independently. Named and finalcohort checks pass
  with unchanged exact inputs.
source:
  git_revision: bee4f42bb622ae0a0999f8f3e3dac31f14282278
  state: working_tree
  inputs:
  - path: data/records/chalcocite.yaml
    sha256: 1b6d4f56c629f2c029f8856734aee1317744f90b468891c27103d40c2496fc0e
    role: target
  - path: history/records/chalcocite/2026-10-11T202953Z-codex-610893.yaml
    sha256: cb24167fbb02c475ca4bb777a69139f708bcf0852fbd103a295dcbdbefcc2139
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Everyfield ofone newmineralrecord, its mechanism/evidence/sources and
    separateCREATE/inline provenance.
  selection: Parent assigned frozenrecord authored byotheragent inround33.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chalcocite
  exclusions:
  - target: Raw sequencing reanalysis,rawinstrument data andunrelated studies
    reason: No rawsequence/material-balance reconstruction isperformed; otherfeeds
      andexperiments are scope checks only, notnewcuration.
targets:
- target_id: cmmmech:chalcocite
  path: data/records/chalcocite.yaml
  label: Chalcocite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chalcocite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/chalcocite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Reviewer executed successfully: Checked1record;0failed. Log /private/tmp/cmm-round33-chalcocite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e'
  target_ids:
  - cmmmech:chalcocite
- check_id: batch
  name: Final frozen-cohort batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round33-final-batch.log SHA256 4ca5dc5133c70847781db60f3ac8024963b461a718c7fc9083c43e10ec5d4d32.
    uv run --locked --extra dev python scripts/check.py All checks passed! ........................................................................
    [ 23%] ........................................................................
    [ 46%] ........................................................................
    [ 69%] ....................................................sss.................
    [ 92%] .......................                                                  [100%]
    308 passed, 3 skipped in 129.87s (0:02:09) Checked 190 record(s); 0 failed. Checked
    219 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chalcocite
- check_id: nonempty
  name: Final frozen-cohort nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round33-final-nonempty.log SHA256 dc2cb7cea2d56632e877b4a0aa4fd88a366a2948425add2449d30c92d14ec299.
    Checked 190 record(s); 0 failed.
  target_ids:
  - cmmmech:chalcocite
- check_id: history
  name: Final frozen-cohort history gate
  command: uv run --locked cmmmech validate-history --base bee4f42bb622ae0a0999f8f3e3dac31f14282278
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round33-final-history.log SHA256 5fdfb5898956d9c86e8d8c3976c1c07f567b349cb0cbeae4a4385905857b70a1.
    Checked 219 history record(s); 0 error(s).
  target_ids:
  - cmmmech:chalcocite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/chalcocite.yaml
  locator: Complete frozen maintained record, all fields
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: Record retains natural-separate identity, reported leaching-index comparison
    and explicit numerical/causal limits.
  snapshot_sha256: 1b6d4f56c629f2c029f8856734aee1317744f90b468891c27103d40c2496fc0e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/acsomega.9b02294
  locator: Complete original10-page PDF, Sections1–4, Figures1–13, Tables1–5 and Equations1–2;
    every original page visually inspected and full text read.
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: Natural Zijinshan separates and mine-sump community are supported. Figure4
    shows similar early copper indices and higher later inoculated values; iron indices
    also increase. Equation2 has a subtractive direction incompatible with increasing
    solution concentration. Methods and figure captions support the limited assay
    scope and do not supply the missing mass/volume/sterility details.
  snapshot_sha256: 52003e64693bce72bcc0999c21434c8a9718f779e84868022e729d6e647b0cc6
- evidence_id: xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6844112/
  locator: Complete original JATS inspected; independently live-opened PMC article
    corroborates identity.
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: JATS contains13figures,5table-wraps and no supplementary-material nodes.
    The retained ZIP contains32image renditions, representing article figures, equations
    and graphical abstract, not a separate experimental supplement. Original PDF/JATS/PMC
    are related artifacts of one experiment, not independent replications.
  snapshot_sha256: c6ed400e8ae576250d5c2b31ceea4092b585a896e191b692bc47aee368276bb7
- evidence_id: archive
  kind: primary_source
  reference: /private/tmp/cmm-round33-chalcocite-research/raw/wu2019-supplementary.zip
  locator: Complete ZIP member inventory inspected
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: All32members are article JPG/GIF images. Main-page originals were visually
    checked; no separate raw assay table or additional methods was found inside this
    archive. Filename supplementary.zip does not establish an experimental supplement.
  snapshot_sha256: d9b9b8147de5724ac98a94bf795a2b260761de119f993571e474fb5b14e8f9d4
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Retained September2026 original PDFpage40 chalcocite row; column definitions
    onpage1
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: Independently inspected chalcocite row:Cu2S,statusG,1751. Grandfathered
    mineral identity and original-description year match. Same-day retained authority
    reused, not claimed as fresh download. Record assigns no synthetic-reagent identity
    or elemental criticality.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: history
  kind: record_content
  reference: history/records/chalcocite/2026-10-11T202953Z-codex-610893.yaml
  locator: Complete canonical CREATE sidecar and separate inline event
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: Actual20:29:53Z Codex/GPT-6/codex CREATE targets this file and reports
    accurate scope; inline event20:29:59Z is separate. It does not claim already-completed
    independent review or backdated curation.
  snapshot_sha256: cb24167fbb02c475ca4bb777a69139f708bcf0852fbd103a295dcbdbefcc2139
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round33-chalcocite-independent/dedup.json
  locator: Reviewer executed hidden/ignored-inclusive symlink-following search and
    inspected current/original record hits
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: Accepted chalcocite root is distinct from contextual mentions of transient
    chalcocite in chalcopyrite and comparison naming in bornite. Current source research
    and historical raw references are not duplicate accepted roots. Search completed0
    with empty stderr,592matching lines.
  search_scope: Current worktree and original checkout records/research/reviews/history,
    previously declared referenced raw roots, new round32 research and current raw.
    Hidden/ignored included and symlinks followed. Binary PDFs/images/Office/zip excluded;
    available extracted text/metadata searched, relevant originals inspected separately.
    Not machine-wide. Query:chalcocite|acsomega[.]9b02294|PRJNA555796|Semiconductor.Microbial
    Mechanism. Current chalcocite raw added to inherited referenced-raw inventory.
    Exact command and outputs retained; no machine-wide claim.
  snapshot_sha256: 1cbe6b61d47c08b9a206811f78490d1dad53b4e35eb00d48f8c7e45460b01c6e
- evidence_id: notices
  kind: search
  reference: Independent web searches11October2026
  locator: First returned result sets and original PMC article reopened
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: No affecting correction/retraction surfaced in these bounded results. Related
    redox-control studies use distinct chalcopyrite/pyrite feeds and do not establish
    a contradictory result for the exact chalcocite assay. Secondary/wiki results
    were not used as evidence. Crossref local file is empty and independent live Crossref
    web-open failed, so no clean-Crossref assertion is made.
  search_scope: Exact queries:"10.1021/acsomega.9b02294" correction retraction; "chalcocite"
    "pyrite" bioleaching bacteria abiotic redox potential comparison. No date/domain
    filters or pagination. Related publisher abstract for electrochemical simulation
    S0304386X1400022X surfaced; direct opening failed. This was a lead-level scope
    check, not full assessment or new imported measurements.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round33-final-terminal.json
  locator: All3terminal command entries, corresponding complete logs and final native
    recapture
  accessed_at: '2026-10-11T20:37:35.986017Z'
  support: supports
  summary: All gates completed0;308passed3skipped129.87s,190records219histories. Reviewer
    independently read and SHA-256 verified logs. Final target/history/schema inputs
    exactly match initial native capture.
  snapshot_sha256: 29cf633edeea5fa42c30a4093bc01d37b53fa6daab522e076ac605c5c531fc40
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity, experimental mixture and criticality boundary
  outcome: supported
  summary: Cu2S is verified at IMA. Table2 values and source-labelled92.40%purity
    are faithfully reported as composition, not a independently quantified endmember
    phase fraction. Natural separate is distinct from element, mixedore and synthetic
    reagent.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
  - ima
  - dedup
  dimensions:
  - name: material_form
    value: Natural chalcocite separate within1:2mass mixture with pyrite
    definition: Prepared by hand sorting,gravityseparation,flotation and grindingbelow0.074mm;
      no complete phase-purity guarantee.
    evidence_ids:
    - primary
    - record
  - name: criticality
    value: Not asserted
    definition: No jurisdiction,list or edition borrowed from elemental copper.
    evidence_ids:
    - record
- assessment_id: methods
  area: evidence
  topic: Community, assay conditions and controls
  outcome: supported
  summary: Mineheap-sump community,4–5day laboratory adaptation,9Kmedium,30°C,14days,initialpH1.8
    and1:10inoculum:pulp align with Sections2.2/4.1–4.2 and Figure4. Exact medium
    recipe,solidmass,workingvolume,flaskagitation,washing and subsequentpHcontrols
    remain unavailable. The rawore reactor5%loading/120rpm are correctly separated.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: organism
    value: Unresolved living mine-derived community
    definition: Genus profiles do not establish authenticated strain IDs or species-specific
      causal contributions.
    evidence_ids:
    - primary
    - record
  - name: biomass
    value: Living cultivated/adapted community
    definition: No inactive biomass or purestrain mechanism inferred.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Uninoculated comparison; sterility not verified
    definition: No matched evolvingpH/potential or directcontact perturbation isolates
      an effect beyond changed solution chemistry.
    evidence_ids:
    - primary
    - record
  - name: replication
    value: At least3repetitions;mean±SD
    definition: SourceSection4.5states this generally; actual flask workingmass/volume
      and cell-density basis acrossinoculumratios remain missing.
    evidence_ids:
    - primary
    - record
- assessment_id: quantity
  area: quantity
  topic: Direction of equation and source-reported indices
  outcome: supported
  summary: Original Equation2 on18286 is E=1−(CVM/alpha m)×100% without resolving
    concentrations/units. SinceCis defined as solution concentration, its direction
    conflicts with extraction interpretation. Record preserves only plotted indices,
    not reconstructed yields. Figure4 indeed shows copper comparators similaratday2,
    followed by higher inoculated indices; ironindices also rise. Table2exactnumbers
    are correct.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: outcome
    value: Reported comparativeleaching indices
    definition: Original measuredconcentrations,residue mass and solutionvolumes cannot
      reconstruct feed-mass extraction or isolatedproduct recovery.
    evidence_ids:
    - primary
    - record
  - name: potential
    value: Ag/AgCl measurement normalizedtohydrogen scale
    definition: Section4.4expresslystates the scale; finalhigherinoculatedpotential
      is visibleinFigure5.
    evidence_ids:
    - primary
- assessment_id: causality
  area: evidence
  topic: Community association versus mineral-selective or molecular cause
  outcome: supported
  summary: Taxa inFigure6are relative sequence abundances fromseparatemineral assays;
    paper alternates attachedsample wording withsolutionDNA harvesting. These do not
    determine taxa contributions to the mixed assay. Ferric attack,sulfur oxidation,galvanic
    effects,electronic vacancies and two-stageprocess remain interpretations. Correctly
    no verified exclusive Cu-onlyselectivity,enzyme mechanism or phase-conversion
    measurement is claimed.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
- assessment_id: scope
  area: scope
  topic: Laboratory scope and unadopted wider claims
  outcome: supported
  summary: Industrial mine origin is not industrial deployment. The record curates
    the separate-mixture flask result, not the rawore reactor nor modeledtwo-stage
    separation. Relatedsource leads with differentfeed/potentialcontrol do not refute
    this deliberately bounded observation.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
  - notices
- assessment_id: provenance
  area: provenance
  topic: Exact scientific state, primary ownership and completed gates
  outcome: supported
  summary: Frozenrecord/history/schema hashes are identicalininitialandfinal nativecaptures.
    PDF/JATS and independently openedPMC verify sourceidentity despite unavailableCrossrefresponse.
    CanonicalCREATE and inlineevent are coherent. Named and allfinalcohort gates passed;
    no maintainedfile was changed bythisreviewer.
  target_ids:
  - cmmmech:chalcocite
  evidence_ids:
  - record
  - primary
  - xml
  - archive
  - history
  - gates
findings: []
actions: []
limitations:
- The printedpercent equation and missingoriginalconcentrations/masses/volumes prevent
  verifiedextraction or chalcociteconversion yields.
- Natural mineral separates lack quantitatively establishedendmember phase fractions;
  othercopper phases are notexcluded.
- Uninoculated comparison hasno verifiedsterility or matched dynamicpH/potential;
  chemicalconditions confound isolatedmicrobial causality.
- Communityrelativeabundances and ambiguoussolution-versus-attachedDNA fraction do
  not establish organism-specific mechanisms.
- Exactflaskloading/workingvolume/agitation/mediumrecipe and inoculumcell-densitybasis
  remain incomplete.
- Crossref localfilewas empty and independentlivewebopen failed; originalPDF/JATS/livePMC
  establishbibliography, but no cleanCrossrefnotice result isclaimed. Correction/counterevidencesearch
  wasbounded.
notes:
- All10originalpages,13figures,5tables and2equations independentlyinspected. No maintainedtarget/history/dossieredited.
- No correctiveissueisinvented from honestlydeclared primary-source limitations.
- Initialinspect attempt included an unsupportedcontext_paths key andwasrejected;
  correctednativeinspect with --input succeeded beforejudgment and finalcapturewasidentical.
links:
- https://doi.org/10.1021/acsomega.9b02294
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6844112/
- https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
```
