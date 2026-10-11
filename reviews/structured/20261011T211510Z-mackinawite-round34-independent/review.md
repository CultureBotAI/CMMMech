# Independent scientific review of mackinawite AM13 mineralization

- Review: 20261011T211510Z-mackinawite-round34-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T21:12:03.123974Z
- Finished UTC: 2026-10-11T21:15:10.235598Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record supports a bounded mineralization observation, preserving inactivebiomass versus metabolism, imperfectcontrols, phaseidentification limits and measured/fitted/geometric distinctions. No correctivefinding identified. Named andfinalcohort checks pass onunchangedinputs.

## Scope And Provenance

Every field of one new mineral record, its source-specificmechanism and separateCREATE/inline provenance.

Selection: Parent-assigned independent review of another agent frozen mackinawite record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 38cef46aabbcb2b49536ed8c265c63646ff1da3d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:mackinawite | data/records/mackinawite.yaml | maintained | Mackinawite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:mackinawite | Reviewer executed; Checked 1 record(s); 0 failed. Log /private/tmp/cmm-round34-mackinawite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final frozen-cohort batch gate | passed | True | cmmmech:mackinawite | Root executed; reviewer independently read complete terminal log and SHA256 verified. /private/tmp/cmm-round34-final-batch.log SHA256 84e966930d55b1bbc3527e149d252fd1dfe7f3ec0454f71b71aaceb517ebf5c8. uv run --locked --extra dev python scripts/check.py All checks passed! ........................................................................ [ 23%] ........................................................................ [ 46%] ........................................................................ [ 69%] ....................................................sss................. [ 92%] ....................... [100%] 308 passed, 3 skipped in 195.87s (0:03:15) Checked 194 record(s); 0 failed. Checked 224 history record(s); 0 error(s). |
| Final frozen-cohort nonempty gate | passed | True | cmmmech:mackinawite | Root executed; reviewer independently read complete terminal log and SHA256 verified. /private/tmp/cmm-round34-final-nonempty.log SHA256 9a1c693b6ef6256da07b28e732785b92b62fc090e964b3303620f782db991cd9. Checked 194 record(s); 0 failed. |
| Final frozen-cohort history gate | passed | True | cmmmech:mackinawite | Root executed; reviewer independently read complete terminal log and SHA256 verified. /private/tmp/cmm-round34-final-history.log SHA256 70d4c90358c71eeb843da5b2f1b671d7ee9275ecd4d3c4dcb3330d4db4ed3d6f. Checked 224 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral, strain and criticality boundaries

identity: supported. Targets: cmmmech:mackinawite.

FeS mackinawite has direct IMA identity and actual crystalline diffraction support. An amorphous FeS precipitate or elementaliron is not substituted; no criticality imported. NCBI source-name synonym resolves the exact experimental strain.

### Live and inactive biomass, reagents and experimental controls

evidence: supported. Targets: cmmmech:mackinawite.

Methods andS1 substantiate washed stationary AM13,50mL/110mLvials,35C,nominal4mMFe,initialpH7.03,live10^6/10^8cells/mL,cell-free slow/fastNa2S and post-growthFe arms. Irradiatedcells48–72h at2Gy/min lack sulfide production and spend two weeks inFe medium beforeNa2S. These distinctions remain explicit.

### Phase and microscopy-scale attribution

evidence: supported. Targets: cmmmech:mackinawite.

OriginalFigure2 and referencepanelD substantiate early crystalline mackinawite acrossarms, plus vivianite in some controls. Figure6Fe/S maps cannot individually identify each cellcrust; record retains bulk-to-local inference. Greigiteappears5months inFigure2C with residualmackinawite11months, not completeconversion; &gt;5monthsdiscussion conflict retained.

### Domain sizes, aggregation and geometric estimates

quantity: supported. Targets: cmmmech:mackinawite.

Table3 pools unequal-time n10/5/11/5 measurements.18.5±7.7nm inactivec-axis inTable versus18.7±7.7prose is disclosed. Scherrerdomain size,DLSaggregate size and geometric~60%FeS allocation have distinct meanings, neither extraction nor isolated recovery. FinalpH7.06/7.30/7.37 values supportcontrol limitation.

### Microbial association and proposed molecular explanations

evidence: supported. Targets: cmmmech:mackinawite.

Abiotic formation and inactive-cell growth effects support a nonexclusive biomass influence. Cellbinding/EPS,Feoxidation and enzyme claims remain proposed or unmeasured. The primary nullpyrite/marcasite is condition-specific.

### Laboratory versus deployment and natural relevance

scope: supported. Targets: cmmmech:mackinawite.

Record explicitly confines evidence to reagent-based laboratory precipitation. Section4.5 states elevatedconcentrations unlike typicalsediments; no fieldperformance,naturalfeed extraction or industrial recovery inferred.

### Exact independent assessment and valid records

provenance: supported. Targets: cmmmech:mackinawite.

Scientific record and history were authored bypackaging; thisreviewer did not edit them. Exact nativeinputs unchanged, separatehistory/inline coherent, requirednamed/cohort gates passed. Rawsource acquisition limits preserved honestly.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/mackinawite.yaml; Complete frozen record, all maintained fields | supports | Exact inputs match initial and final native captures; mechanism, identity and provenance checked. |
| primary | https://doi.org/10.1016/j.gca.2017.10.006; Complete 18-page author-hosted PDF text, independently reopened through web reader; Sections 2-5, Tables 1-3, all seven original publisher figure images | supports | Methods support AM13/DSM14728, medium, live/dead/cell-free/post-growth arms,4mMFe,35C and explicit pretreatment. Original figures show early mackinawite with vivianite in some arms, larger cell-associated domain sizes and conditional greigite. Main PDF bytes were not downloaded; text and original figures are separate legitimate representations of the original publication. |
| figures | /private/tmp/cmm-round34-mackinawite-research/raw; picard2018-figure1.jpg through figure7.jpg, all original images independently viewed | supports | Figure2 actual panelD gives reference patterns, despite caption slip. Figure4 upperrowA-D biotic and lowerrowE-H abiotic contradict one prose crossreference; record does not repeat that slip. Figures5-7 distinguish preparation-dependent appearances, encrustation and damaged inactive cells. |
| supplement | /private/tmp/cmm-round34-mackinawite-research/raw/picard2018-supplement.pdf; All four original PDF pages and FiguresS1-S3 independently viewed | supports | S1 clearly distinguishes order of Fe/sulfide/cell exposure. S2 shows imperfectly matched sulfide levels/rates,Fe/S andpH; S3 shows aggregate appearance. None supplies an isolated mineral recovery yield. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original retained PDFpage130 row visually inspected | supports | Mackinawite FeS,statusA,1967s.p. agrees with record. Same-day retained authority artifact, not a new remote download. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1121451&amp;mode=Info; Independently live-opened current NCBI strain node and retained original HTML | supports | Current name Maridesulfovibrio hydrothermalis AM13=DSM14728, source-name Desulfovibrio homotypic synonym, no-rank strain node. Exact strain is named in primarymethods. |
| history | history/records/mackinawite/2026-10-11T210936Z-codex-4cb40f.yaml; Complete CREATE sidecar and separate inline event | supports | Canonical21:09:36Z and inline21:09:39Z events identify actual Codex/GPT-6/codex curation and correct target/scope; no backdated authorship or self-approved scientific review. |
| dedup | /private/tmp/cmm-round34-mackinawite-independent/dedup.json; Independent hidden/ignored-inclusive, symlink-following bounded search | supports | Current/original records mention mackinawite as reagent/intermediate under antimony and pyrite; these are distinct owners from the new mineral species. Newgreigite source context does not duplicate mineralidentity. Search return0,empty stderr; retained command/output define boundary. |
| notices | Independent web searches 2026-10-11; First returned result sets; no date/domain filters or pagination | supports | No affecting correction/retraction surfaced in bounded exactDOI notice search. Related2026vesicle work,2022carbonpreservation and broader abiotic studies surfaced as leads, not newly verified mechanisms or refutations. Original2018 own chemical controls already disprove biological necessity, accurately retained. |
| gates | /private/tmp/cmm-round34-final-terminal.json; All three terminal commands and complete hashed logs, plus final native input recapture | supports | All required frozen-cohort gates pass; reviewer verified logSHA256 and target/history/schema remain unchanged. |

## Limits And Additional Notes

- Controls differ in sulfide/pH and inactivecell two-weekFe pretreatment; exclusive molecularcausality is not established.
- BulkXRD does not prove the phase of each imaged cellcrust; relevant assignment is an explicit inference.
- Unequal monthranges and pooledreplicates, source18.5/18.7 discrepancy and5/&gt;5month wording limit precision.
- Domain sizes, DLSaggregates and geometric60%estimate are not productrecovery metrics.
- MainPDF was available through webreader and originalpublisher figures; localPDF acquisition was unavailable. Web screenshot requests returned references without imagepayload, so no original full-page table visualinspection is claimed. Original tablecontents read from complete primary text and all originalfigures independently viewed.
- Bounded noticesearch is not exhaustive; later2026/2022 sources not fully reassessed or imported.
- No maintainedrecord/history/dossier edits by reviewer.
- All seven original mainfigureimages, four SIpages/threeSIfigures, complete originalprimarytext/three tables and IMArow were independently assessed.
- No corrective issue invented from disclosed primary-source limitations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T211510Z-mackinawite-round34-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of mackinawite AM13 mineralization
started_at: '2026-10-11T21:12:03.123974Z'
finished_at: '2026-10-11T21:15:10.235598Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Mackinawite was authored by /root/round27_packaging. Reviewer
    authored only greigite in this cohort and did not edit mackinawite record/history/dossier.
    Shared worktree and curator-acquired artifacts disclosed. Native exact inputs
    captured before judgment; primary text, originalfigures/supplement andauthority
    IDs independently assessed. Root ran batchgates; reviewer read andhashed terminal
    logs.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record supports a bounded mineralization observation, preserving
  inactivebiomass versus metabolism, imperfectcontrols, phaseidentification limits
  and measured/fitted/geometric distinctions. No correctivefinding identified. Named
  andfinalcohort checks pass onunchangedinputs.
source:
  git_revision: 38cef46aabbcb2b49536ed8c265c63646ff1da3d
  state: working_tree
  inputs:
  - path: data/records/mackinawite.yaml
    sha256: 8710787a7c9658a26b83d6fe7306f7e338f31ee823747ac3b259b26d9367e507
    role: target
  - path: history/records/mackinawite/2026-10-11T210936Z-codex-4cb40f.yaml
    sha256: 099842aa60a4d74cab11be1caab19c5c6fab46bb31f78cd406abedc31b60c538
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every field of one new mineral record, its source-specificmechanism
    and separateCREATE/inline provenance.
  selection: Parent-assigned independent review of another agent frozen mackinawite
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:mackinawite
  exclusions:
  - target: Rawinstrument reanalysis and newstudies
    reason: No rawXRD refinement or broadliterature expansion; later sources remain
      discovery-level context.
targets:
- target_id: cmmmech:mackinawite
  path: data/records/mackinawite.yaml
  label: Mackinawite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/mackinawite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/mackinawite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed; Checked 1 record(s); 0 failed. Log /private/tmp/cmm-round34-mackinawite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:mackinawite
- check_id: batch
  name: Final frozen-cohort batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA256
    verified. /private/tmp/cmm-round34-final-batch.log SHA256 84e966930d55b1bbc3527e149d252fd1dfe7f3ec0454f71b71aaceb517ebf5c8.
    uv run --locked --extra dev python scripts/check.py All checks passed! ........................................................................
    [ 23%] ........................................................................
    [ 46%] ........................................................................
    [ 69%] ....................................................sss.................
    [ 92%] ....................... [100%] 308 passed, 3 skipped in 195.87s (0:03:15)
    Checked 194 record(s); 0 failed. Checked 224 history record(s); 0 error(s).
  target_ids:
  - cmmmech:mackinawite
- check_id: nonempty
  name: Final frozen-cohort nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA256
    verified. /private/tmp/cmm-round34-final-nonempty.log SHA256 9a1c693b6ef6256da07b28e732785b92b62fc090e964b3303620f782db991cd9.
    Checked 194 record(s); 0 failed.
  target_ids:
  - cmmmech:mackinawite
- check_id: history
  name: Final frozen-cohort history gate
  command: uv run --locked cmmmech validate-history --base 38cef46aabbcb2b49536ed8c265c63646ff1da3d
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA256
    verified. /private/tmp/cmm-round34-final-history.log SHA256 70d4c90358c71eeb843da5b2f1b671d7ee9275ecd4d3c4dcb3330d4db4ed3d6f.
    Checked 224 history record(s); 0 error(s).
  target_ids:
  - cmmmech:mackinawite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/mackinawite.yaml
  locator: Complete frozen record, all maintained fields
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Exact inputs match initial and final native captures; mechanism, identity
    and provenance checked.
  snapshot_sha256: 8710787a7c9658a26b83d6fe7306f7e338f31ee823747ac3b259b26d9367e507
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.gca.2017.10.006
  locator: Complete 18-page author-hosted PDF text, independently reopened through
    web reader; Sections 2-5, Tables 1-3, all seven original publisher figure images
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Methods support AM13/DSM14728, medium, live/dead/cell-free/post-growth
    arms,4mMFe,35C and explicit pretreatment. Original figures show early mackinawite
    with vivianite in some arms, larger cell-associated domain sizes and conditional
    greigite. Main PDF bytes were not downloaded; text and original figures are separate
    legitimate representations of the original publication.
  snapshot_sha256: fbbbc81e82c67a1ec643ea04af6b38eb621b143398a0c10380fee6c4242a3519
- evidence_id: figures
  kind: primary_source
  reference: /private/tmp/cmm-round34-mackinawite-research/raw
  locator: picard2018-figure1.jpg through figure7.jpg, all original images independently
    viewed
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Figure2 actual panelD gives reference patterns, despite caption slip. Figure4
    upperrowA-D biotic and lowerrowE-H abiotic contradict one prose crossreference;
    record does not repeat that slip. Figures5-7 distinguish preparation-dependent
    appearances, encrustation and damaged inactive cells.
  snapshot_sha256: 2b629666bae890ea62383ab3570bd4c16a0e92c065f60a1a1f7ea2231b765ccb
- evidence_id: supplement
  kind: primary_source
  reference: /private/tmp/cmm-round34-mackinawite-research/raw/picard2018-supplement.pdf
  locator: All four original PDF pages and FiguresS1-S3 independently viewed
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: S1 clearly distinguishes order of Fe/sulfide/cell exposure. S2 shows imperfectly
    matched sulfide levels/rates,Fe/S andpH; S3 shows aggregate appearance. None supplies
    an isolated mineral recovery yield.
  snapshot_sha256: ce0829fb42a4d7457463f6ab45d5df2b1681526e597a144fb7556327ea36d8b2
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original retained PDFpage130 row visually inspected
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Mackinawite FeS,statusA,1967s.p. agrees with record. Same-day retained
    authority artifact, not a new remote download.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1121451&mode=Info
  locator: Independently live-opened current NCBI strain node and retained original
    HTML
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Current name Maridesulfovibrio hydrothermalis AM13=DSM14728, source-name
    Desulfovibrio homotypic synonym, no-rank strain node. Exact strain is named in
    primarymethods.
  snapshot_sha256: f35bc26cd1f40bc80dff4ecf8cd10edf02c3b58831deacf462fc355d35ac29b1
- evidence_id: history
  kind: record_content
  reference: history/records/mackinawite/2026-10-11T210936Z-codex-4cb40f.yaml
  locator: Complete CREATE sidecar and separate inline event
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Canonical21:09:36Z and inline21:09:39Z events identify actual Codex/GPT-6/codex
    curation and correct target/scope; no backdated authorship or self-approved scientific
    review.
  snapshot_sha256: 099842aa60a4d74cab11be1caab19c5c6fab46bb31f78cd406abedc31b60c538
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round34-mackinawite-independent/dedup.json
  locator: Independent hidden/ignored-inclusive, symlink-following bounded search
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: Current/original records mention mackinawite as reagent/intermediate under
    antimony and pyrite; these are distinct owners from the new mineral species. Newgreigite
    source context does not duplicate mineralidentity. Search return0,empty stderr;
    retained command/output define boundary.
  search_scope: Current and original checkout records/research/reviews/history plus
    previously cited raw locations and current mackinawite raw; 485 declared roots.
    rg --no-ignore --hidden --follow; query mackinawite|gca[.]2017[.]10[.]006|hydrothermalis.*AM13|1121451.
    BinaryPDF/images/Office/ZIP excluded from grep; extractedtext/metadata searched
    and relevant originals assessed separately. Not machine-wide.
  snapshot_sha256: 19c57bcbd8ffda8499ef9f147832a3b29850b96e4e9779bf13940fb26dbb5530
- evidence_id: notices
  kind: search
  reference: Independent web searches 2026-10-11
  locator: First returned result sets; no date/domain filters or pagination
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: No affecting correction/retraction surfaced in bounded exactDOI notice
    search. Related2026vesicle work,2022carbonpreservation and broader abiotic studies
    surfaced as leads, not newly verified mechanisms or refutations. Original2018
    own chemical controls already disprove biological necessity, accurately retained.
  search_scope: 'Exact queries: "10.1016/j.gca.2017.10.006" correction OR retraction
    OR corrigendum; "Picard" "mackinawite" "2018" contradictory abiotic. Live original
    author-hosted PDF and NCBI reopened independently. Search coverage is bounded.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round34-final-terminal.json
  locator: All three terminal commands and complete hashed logs, plus final native
    input recapture
  accessed_at: '2026-10-11T21:15:10.235598Z'
  support: supports
  summary: All required frozen-cohort gates pass; reviewer verified logSHA256 and
    target/history/schema remain unchanged.
  snapshot_sha256: 5a57d3f8d6cb1555e588da6687ab9d2266293025c6301d9e950bff153ad2b14d
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral, strain and criticality boundaries
  outcome: supported
  summary: FeS mackinawite has direct IMA identity and actual crystalline diffraction
    support. An amorphous FeS precipitate or elementaliron is not substituted; no
    criticality imported. NCBI source-name synonym resolves the exact experimental
    strain.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
  - ima
  - taxon
  - dedup
  dimensions:
  - name: material_form
    value: Laboratory biomineral with crystallographic assignment
    definition: Record is mineral species; assay starts from dissolved FeCl2 and sulfide
      rather than natural ore.
    evidence_ids:
    - record
    - primary
    - ima
  - name: criticality
    value: Not asserted
    definition: No authority/jurisdiction/list/edition transferred from a constituent.
    evidence_ids:
    - record
- assessment_id: methods
  area: evidence
  topic: Live and inactive biomass, reagents and experimental controls
  outcome: supported
  summary: Methods andS1 substantiate washed stationary AM13,50mL/110mLvials,35C,nominal4mMFe,initialpH7.03,live10^6/10^8cells/mL,cell-free
    slow/fastNa2S and post-growthFe arms. Irradiatedcells48–72h at2Gy/min lack sulfide
    production and spend two weeks inFe medium beforeNa2S. These distinctions remain
    explicit.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
  - supplement
  - taxon
  dimensions:
  - name: organism
    value: Maridesulfovibrio hydrothermalis AM13=DSM14728
    definition: Primary uses Desulfovibrio source-name; current strain label verified.
    evidence_ids:
    - taxon
    - primary
  - name: biomass_state
    value: Live cells and separately gamma-inactivated cells
    definition: Inactive biomass can influence nucleation but is not described as
      metabolically active.
    evidence_ids:
    - primary
    - record
  - name: controls
    value: Cell-free chemical; dead-cell; post-growth Fe addition
    definition: Sulfide dose/rate,pH andinactivecellpretreatment not perfectly matched.
    evidence_ids:
    - primary
    - supplement
    - record
- assessment_id: phase
  area: evidence
  topic: Phase and microscopy-scale attribution
  outcome: supported
  summary: OriginalFigure2 and referencepanelD substantiate early crystalline mackinawite
    acrossarms, plus vivianite in some controls. Figure6Fe/S maps cannot individually
    identify each cellcrust; record retains bulk-to-local inference. Greigiteappears5months
    inFigure2C with residualmackinawite11months, not completeconversion; >5monthsdiscussion
    conflict retained.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
  - figures
  - supplement
- assessment_id: quantity
  area: quantity
  topic: Domain sizes, aggregation and geometric estimates
  outcome: supported
  summary: Table3 pools unequal-time n10/5/11/5 measurements.18.5±7.7nm inactivec-axis
    inTable versus18.7±7.7prose is disclosed. Scherrerdomain size,DLSaggregate size
    and geometric~60%FeS allocation have distinct meanings, neither extraction nor
    isolated recovery. FinalpH7.06/7.30/7.37 values supportcontrol limitation.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
  - figures
  - supplement
  dimensions:
  - name: outcome
    value: Culture/biomass-associated crystalline-domain and aggregation differences
    definition: Qualitativecomparative observation with fitted size estimates; no
      mineral productyield.
    evidence_ids:
    - primary
    - record
- assessment_id: causality
  area: evidence
  topic: Microbial association and proposed molecular explanations
  outcome: supported
  summary: Abiotic formation and inactive-cell growth effects support a nonexclusive
    biomass influence. Cellbinding/EPS,Feoxidation and enzyme claims remain proposed
    or unmeasured. The primary nullpyrite/marcasite is condition-specific.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
  - figures
  - supplement
  - notices
- assessment_id: scope
  area: scope
  topic: Laboratory versus deployment and natural relevance
  outcome: supported
  summary: Record explicitly confines evidence to reagent-based laboratory precipitation.
    Section4.5 states elevatedconcentrations unlike typicalsediments; no fieldperformance,naturalfeed
    extraction or industrial recovery inferred.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: provenance
  topic: Exact independent assessment and valid records
  outcome: supported
  summary: Scientific record and history were authored bypackaging; thisreviewer did
    not edit them. Exact nativeinputs unchanged, separatehistory/inline coherent,
    requirednamed/cohort gates passed. Rawsource acquisition limits preserved honestly.
  target_ids:
  - cmmmech:mackinawite
  evidence_ids:
  - record
  - history
  - gates
findings: []
actions: []
limitations:
- Controls differ in sulfide/pH and inactivecell two-weekFe pretreatment; exclusive
  molecularcausality is not established.
- BulkXRD does not prove the phase of each imaged cellcrust; relevant assignment is
  an explicit inference.
- Unequal monthranges and pooledreplicates, source18.5/18.7 discrepancy and5/>5month
  wording limit precision.
- Domain sizes, DLSaggregates and geometric60%estimate are not productrecovery metrics.
- MainPDF was available through webreader and originalpublisher figures; localPDF
  acquisition was unavailable. Web screenshot requests returned references without
  imagepayload, so no original full-page table visualinspection is claimed. Original
  tablecontents read from complete primary text and all originalfigures independently
  viewed.
- Bounded noticesearch is not exhaustive; later2026/2022 sources not fully reassessed
  or imported.
notes:
- No maintainedrecord/history/dossier edits by reviewer.
- All seven original mainfigureimages, four SIpages/threeSIfigures, complete originalprimarytext/three
  tables and IMArow were independently assessed.
- No corrective issue invented from disclosed primary-source limitations.
links:
- https://doi.org/10.1016/j.gca.2017.10.006
- https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1121451&mode=Info
- https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
```
