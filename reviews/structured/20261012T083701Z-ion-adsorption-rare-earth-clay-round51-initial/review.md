# Independent initial scientific review of ion-adsorption rare-earth clay

- Review: 20261012T083701Z-ion-adsorption-rare-earth-clay-round51-initial
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T08:33:36Z
- Finished UTC: 2026-10-12T08:37:01Z
- Reviewer: Codex /root/round43_hardmetal (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The frozen clay record preserves the primary study scope and is scientifically supported with stated limitations. One minor source-dossier finding needs correction: Table4 visibly prints Original medium Eh4.38, whereas the dossier incorrectly calls the cell blank and attributes the value to extraction. Record and history need no change. Final cohort gates remain pending for this initial observation.

## Scope And Provenance

Whole frozen record and its retained evidence, complete original article and supplements, all three figures and five tables, original workbook cells, source provenance and source contradictions. Initial review saved before dossier correction and before completed cohort gates.

Selection: Parent-assigned independent adversarial review of one new resource owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 466cb14cbc271ba73ba05e89ed188cfd113d06ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ion-adsorption-rare-earth-clay | data/records/ion-adsorption-rare-earth-clay.yaml | maintained | Ion-adsorption rare-earth clay |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named record validation | passed | True | cmmmech:ion-adsorption-rare-earth-clay | Actually executed by reviewer; Checked1record(s);0failed; tool session43600, terminal0. |
| Original sources and frozen input verification | passed | True | cmmmech:ion-adsorption-rare-earth-clay | Verified all50 source-dossier raw hashes and all five native captured inputs; independently decoded complete workbook and matched extracted PDF/XLSX bytes to publisher ZIP. |
| Final cohort check, nonempty validation and base history | unavailable | True | cmmmech:ion-adsorption-rare-earth-clay | Parent is coordinating cohort gates; no completed gate receipt was available to this initial review. Successor must bind actual terminal results. |

## Scientific And Domain Assessments

### Natural resource, feed provenance and species boundaries

identity: supported. Targets: cmmmech:ion-adsorption-rare-earth-clay.

Source-specific ferruginous poorly sorted clay above volcanic breccia is a primary resource; isolate country-rock profile differs. Individual clay minerals, constituent rare earths and processing residues are not conflated.

### Culture-associated release with nonsterile controls

evidence: supported. Targets: cmmmech:ion-adsorption-rare-earth-clay.

Living separate genus-level isolates, nonaseptic provenance,25°C/150rpm/60days,3g per150mL,&lt;0.5mm feed,48h preculture and140g/L glucose match originals. Uninoculated feed was not sterile and developed acidification; all release is not assigned exclusively to inoculated taxa. Proton versus ligand effects remain unresolved.

### Release denominator, chemical advantage and uncertainties

quantity: supported. Targets: cmmmech:ion-adsorption-rare-earth-clay.

Lu percentages use total feedLu; mass-based workbook values are not solution concentrations or purified yields. Salt is generally faster/better withCe exception; sourceCe R² disagreement, possible redox explanation, slow kinetics andSi/Fe co-leaching remain qualified. Dy discrepancy is retained in dossier without selecting a measurement.

### Dossier Table4 misdescription

provenance: concern. Targets: cmmmech:ion-adsorption-rare-earth-clay.

The original source visibly prints Eh4.38; the frozen dossier falsely labels its cell blank and blames extraction. Minor evidence-description defect; the record does not contain or rely on this Eh value. A dated correction note can supersede this sentence while preserving original dossier and review.

### Frozen provenance and structural checks

schema: supported. Targets: cmmmech:ion-adsorption-rare-earth-clay.

Named strict validation and all50 raw hashes passed; inline/canonical CREATE are distinct actual events. Full batch verification is pending and not substituted by source checks.

## Findings

### F1: Source dossier misstates printed Table4 Eh as an extraction artifact

minor / open / confirmed; issue key: CMMMech.ion-adsorption-rare-earth-clay.dossier-table4-eh.

Under Contradictions and extraction hazards, the dossier says the Original medium Eh cell is visually blank and the extractor duplicated pH4.38. Both independently rendered original PDF page6 and publisher XML print4.38 in the Eh cell as well as pH. Correct the documentary claim without declaring the source value scientifically valid or a confirmed typo. The record imports no Eh value and needs no scientific change.

## Recommended Actions And Acceptance Checks

### A1

Append a timestamped paired source correction explicitly superseding only the original Table4 bullet: both PDF and XML print4.38 in pH and Eh; its physical correctness is unresolved and it is not curated. Preserve the original dossier, initial review and unchanged record/history; save a full successor with correction input and exact F1 lineage.

- Reinspect original PDF page6 and publisher XML Table4 final row.
- Pin original dossier and new correction hashes; prove record/history unchanged.
- Save full scientific successor after actual cohort gates, resolving this exact F1 issue key without rewriting predecessor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/ion-adsorption-rare-earth-clay.yaml; Complete frozen input | supports | Read complete file and verified exact native pre-assessment hash. |
| history | history/records/ion-adsorption-rare-earth-clay/2026-10-12T082825Z-codex-0d6399.yaml; Complete frozen input | supports | Read complete file and verified exact native pre-assessment hash. |
| dossier_json | research/sources/round51-ree-clay/20261012T083313Z-source-investigation.json; Complete frozen input | supports | Read complete file and verified exact native pre-assessment hash. |
| dossier_md | research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md; Complete frozen input | supports | Read complete file and verified exact native pre-assessment hash. |
| schema | src/cmmmech/schema/cmmmech.yaml; Complete frozen input | supports | Read complete file and verified exact native pre-assessment hash. |
| primary | https://doi.org/10.3390/min8060236; Complete original11-page article, Sections2–5, Figures1–3 and Tables1–5 | supports | All11 pages personally visually inspected and retained scientific text read. Nonsterile source-specific mixed clay, separate isolate profile, chemical comparison, sampling correction, organic-acid data, control failure and industrial limitations are accurately qualified in the record. |
| supplement | https://mdpi-res.com/d_attachment/minerals/minerals-08-00236/article_deploy/minerals-08-00236-s001.zip; Complete DocumentS1 four pages, including blankpage2; original TableS1 Sheet1 A1:U20 | supports | All four PDF pages viewed. Independently opened original XLSX and read all cells, headers, four treatment/time groups and total feed row. Values include mean±SD and blankD12Fe; no new zero or concentration conversion. Both original file bytes match ZIP. |
| table4_pixels | /private/tmp/cmm-round51-ree-clay-research/raw/barnett2018-primary.pdf; Page6 Table4, Original medium row, pH and Eh columns | refutes | Both pH and Eh visibly print4.38. Independently rerendered page6 directly from the original PDF and personally viewed it; no inference that the publisher value is correct, erroneous or an extraction artifact. |
| independent_render | /private/tmp/cmm-round51-clay-independent/independent-page06.png; Fresh independent full-page render of original page6 | supports | Visible original-cell evidence corroborates the separately acquired curator page6 image. This is a rendering of the same paper, not independent experimental data. |
| publisher_xml | /private/tmp/cmm-round51-ree-clay-research/raw/barnett2018-primary.xml; table-wrap id minerals-08-00236-t004, final tbody row | supports | Official publisher JATS likewise contains six cells: Original medium,&lt;0.05,&lt;0.05,&lt;0.05,4.38,4.38. The duplication is in both source representations, not introduced solely by the plain-text extractor. |
| workbook_read | /private/tmp/cmm-round51-clay-independent/workbook-independent.json; Original XLSX independently decoded; all cells and types retained | supports | T7=3.76±0.04,T19=3.89±0.1,T20=5.32mg/kg support rounded70.7% and73.1% Lu released per total feedLu. O20Dy53.13 differs from mainTable2Dy53.3; record imports neither Dy value. |
| taxonomy | /private/tmp/cmm-round51-clay-independent/round51clayTaxaNotes.json; Live official NCBI5052 and1386 Info pages, current name/rank | supports | Both identifiers resolve to the stated genera. They do not authenticate TD25 orTD29. Closest-match accessions in mainTable3 remain comparison sequences, not accessioned experimental isolates. |
| notices | /private/tmp/cmm-round51-clay-independent/round51clayIndependentWeb.json; Exact DOI notice query and Barnett ion-adsorption control/counterevidence search | supports | No applicable notice appeared in these returned sets. Official MDPI notes search result shows version-of-record2018-05-30; direct notes fetch later429 and DOI fetch failed. Primary NORA copy read locally. Later papers remain leads, not contradictory measurements imported from abstracts. |
| verification | /private/tmp/cmm-round51-clay-independent/verification.json; All50 raw hashes, exact captured inputs, named validation and Lu denominator check | supports | Actual independent checks; no batch or hosted CI execution claimed. |

## Limits And Additional Notes

- Required cohort checks are pending for this initial observation; completion is partial, not a final passing acceptance.
- The study does not resolve each community member contribution, strain identity, proton versus complexation or isolated product recovery; no industrial deployment or taxonomic reclassification inferred.
- Original main11pages, all3figures/5tables, all4supplementpages and allworkbookcells were independently inspected. No independent culture, sequence reanalysis, chemical measurement or raw statistical rerun performed.
- Table4 prints a duplicated number; this review establishes its presence only, not that it is valid or a proven publisher error.
- Notice search and curator dedup are bounded; missing raw roots and unextracted binary contents do not support global absence claims.
- Initial native finding saved before any correction. No record, Git, GitHub or governance mutation by this reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T083701Z-ion-adsorption-rare-earth-clay-round51-initial
kind: record
repository: CultureBotAI/CMMMech
title: Independent initial scientific review of ion-adsorption rare-earth clay
started_at: '2026-10-12T08:33:36Z'
finished_at: '2026-10-12T08:37:01Z'
reviewer:
  identity: Codex /root/round43_hardmetal
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root curator authored the record, CREATE history and clay dossier.
    Reviewer authored only the separate zircon-feed source update in this cohort.
    Native inspect captured exact record, history, paired dossier and schema before
    judgment; reviewer did not edit any target/context.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The frozen clay record preserves the primary study scope and is scientifically
  supported with stated limitations. One minor source-dossier finding needs correction:
  Table4 visibly prints Original medium Eh4.38, whereas the dossier incorrectly calls
  the cell blank and attributes the value to extraction. Record and history need no
  change. Final cohort gates remain pending for this initial observation.'
source:
  git_revision: 466cb14cbc271ba73ba05e89ed188cfd113d06ea
  state: working_tree
  inputs:
  - path: data/records/ion-adsorption-rare-earth-clay.yaml
    sha256: 33422e33022dffdd44c22c4d18fd08ab6c2ff5b293300648182c127e6696cb06
    role: target
  - path: history/records/ion-adsorption-rare-earth-clay/2026-10-12T082825Z-codex-0d6399.yaml
    sha256: 7ca3a5b0237f741effdec76f4e8394852ecce95a20175ebdbfdf5c9893eb7566
    role: context
  - path: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.json
    sha256: 446709aa78126ef05c4776e7494083d40df1754596a25d06d85b26dc6ec59d93
    role: context
  - path: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md
    sha256: 5b2011fa49b42b9087d4dd426817ae0f9823bd0c287357a076525fda306d625f
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:ion-adsorption-rare-earth-clay
  path: data/records/ion-adsorption-rare-earth-clay.yaml
  label: Ion-adsorption rare-earth clay
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ion-adsorption-rare-earth-clay.yaml
    role: maintained scientific record
scope:
  description: Whole frozen record and its retained evidence, complete original article
    and supplements, all three figures and five tables, original workbook cells, source
    provenance and source contradictions. Initial review saved before dossier correction
    and before completed cohort gates.
  selection: Parent-assigned independent adversarial review of one new resource owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
checks:
- check_id: named
  name: Independent named record validation
  command: uv run --locked cmmmech validate data/records/ion-adsorption-rare-earth-clay.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  summary: Actually executed by reviewer; Checked1record(s);0failed; tool session43600,
    terminal0.
- check_id: source_hashes
  name: Original sources and frozen input verification
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  summary: Verified all50 source-dossier raw hashes and all five native captured inputs;
    independently decoded complete workbook and matched extracted PDF/XLSX bytes to
    publisher ZIP.
- check_id: batch
  name: Final cohort check, nonempty validation and base history
  status: unavailable
  required: true
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  summary: Parent is coordinating cohort gates; no completed gate receipt was available
    to this initial review. Successor must bind actual terminal results.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/ion-adsorption-rare-earth-clay.yaml
  locator: Complete frozen input
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Read complete file and verified exact native pre-assessment hash.
  snapshot_sha256: 33422e33022dffdd44c22c4d18fd08ab6c2ff5b293300648182c127e6696cb06
- evidence_id: history
  kind: record_content
  reference: history/records/ion-adsorption-rare-earth-clay/2026-10-12T082825Z-codex-0d6399.yaml
  locator: Complete frozen input
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Read complete file and verified exact native pre-assessment hash.
  snapshot_sha256: 7ca3a5b0237f741effdec76f4e8394852ecce95a20175ebdbfdf5c9893eb7566
- evidence_id: dossier_json
  kind: record_content
  reference: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.json
  locator: Complete frozen input
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Read complete file and verified exact native pre-assessment hash.
  snapshot_sha256: 446709aa78126ef05c4776e7494083d40df1754596a25d06d85b26dc6ec59d93
- evidence_id: dossier_md
  kind: record_content
  reference: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md
  locator: Complete frozen input
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Read complete file and verified exact native pre-assessment hash.
  snapshot_sha256: 5b2011fa49b42b9087d4dd426817ae0f9823bd0c287357a076525fda306d625f
- evidence_id: schema
  kind: record_content
  reference: src/cmmmech/schema/cmmmech.yaml
  locator: Complete frozen input
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Read complete file and verified exact native pre-assessment hash.
  snapshot_sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/min8060236
  locator: Complete original11-page article, Sections2–5, Figures1–3 and Tables1–5
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: All11 pages personally visually inspected and retained scientific text
    read. Nonsterile source-specific mixed clay, separate isolate profile, chemical
    comparison, sampling correction, organic-acid data, control failure and industrial
    limitations are accurately qualified in the record.
  snapshot_sha256: e001aa957514955ae26257df21d7e9f0f680497abfeca9f0048241cd9a664f04
- evidence_id: supplement
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/minerals/minerals-08-00236/article_deploy/minerals-08-00236-s001.zip
  locator: Complete DocumentS1 four pages, including blankpage2; original TableS1
    Sheet1 A1:U20
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: All four PDF pages viewed. Independently opened original XLSX and read
    all cells, headers, four treatment/time groups and total feed row. Values include
    mean±SD and blankD12Fe; no new zero or concentration conversion. Both original
    file bytes match ZIP.
  snapshot_sha256: 2bbcb68b9adcaaeb84f38e275b15bd32412ee0060cc2dcc80338cf786801bea6
- evidence_id: table4_pixels
  kind: primary_source
  reference: /private/tmp/cmm-round51-ree-clay-research/raw/barnett2018-primary.pdf
  locator: Page6 Table4, Original medium row, pH and Eh columns
  accessed_at: '2026-10-12T08:37:01Z'
  support: refutes
  summary: Both pH and Eh visibly print4.38. Independently rerendered page6 directly
    from the original PDF and personally viewed it; no inference that the publisher
    value is correct, erroneous or an extraction artifact.
  snapshot_sha256: e001aa957514955ae26257df21d7e9f0f680497abfeca9f0048241cd9a664f04
- evidence_id: independent_render
  kind: primary_source
  reference: /private/tmp/cmm-round51-clay-independent/independent-page06.png
  locator: Fresh independent full-page render of original page6
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Visible original-cell evidence corroborates the separately acquired curator
    page6 image. This is a rendering of the same paper, not independent experimental
    data.
  snapshot_sha256: 02a6e6a2430c5fa5531cc925cee5a7459d112337891a882b5106b32a9e2f250b
- evidence_id: publisher_xml
  kind: primary_source
  reference: /private/tmp/cmm-round51-ree-clay-research/raw/barnett2018-primary.xml
  locator: table-wrap id minerals-08-00236-t004, final tbody row
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: 'Official publisher JATS likewise contains six cells: Original medium,<0.05,<0.05,<0.05,4.38,4.38.
    The duplication is in both source representations, not introduced solely by the
    plain-text extractor.'
  snapshot_sha256: 141d580bb1f9d7537f0703aeeb05d63d8829ebec9370edd145454e552e79cce3
- evidence_id: workbook_read
  kind: primary_source
  reference: /private/tmp/cmm-round51-clay-independent/workbook-independent.json
  locator: Original XLSX independently decoded; all cells and types retained
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: T7=3.76±0.04,T19=3.89±0.1,T20=5.32mg/kg support rounded70.7% and73.1% Lu
    released per total feedLu. O20Dy53.13 differs from mainTable2Dy53.3; record imports
    neither Dy value.
  snapshot_sha256: 389a022b75ffd890459a417b906cde11246e715d7491f593ae1fc41a00f3b5b2
- evidence_id: taxonomy
  kind: authority
  reference: /private/tmp/cmm-round51-clay-independent/round51clayTaxaNotes.json
  locator: Live official NCBI5052 and1386 Info pages, current name/rank
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Both identifiers resolve to the stated genera. They do not authenticate
    TD25 orTD29. Closest-match accessions in mainTable3 remain comparison sequences,
    not accessioned experimental isolates.
  snapshot_sha256: 6e4c62f1c29c9e522acae7f43a3e656c6db41620206c3f79f0e8beab248a0cb2
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round51-clay-independent/round51clayIndependentWeb.json
  locator: Exact DOI notice query and Barnett ion-adsorption control/counterevidence
    search
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: No applicable notice appeared in these returned sets. Official MDPI notes
    search result shows version-of-record2018-05-30; direct notes fetch later429 and
    DOI fetch failed. Primary NORA copy read locally. Later papers remain leads, not
    contradictory measurements imported from abstracts.
  snapshot_sha256: 51e34f0ff350504e45d9f130aaaf42eb938c0c0519901d8fba0ce6cc149762ff
  search_scope: '2026-10-12 first returned web sets, no pagination/recency filter:
    "10.3390/min8060236" correction erratum retraction; "Barnett" "ion-adsorption"
    bioleaching control contradiction. No exhaustive notice/field absence claim. Local
    dossier dedup explicitly included hidden/ignored files and symlinks, bounded referenced
    raw roots with nine missing roots; no new machine-wide absence claim.'
- evidence_id: verification
  kind: validation
  reference: /private/tmp/cmm-round51-clay-independent/verification.json
  locator: All50 raw hashes, exact captured inputs, named validation and Lu denominator
    check
  accessed_at: '2026-10-12T08:37:01Z'
  support: supports
  summary: Actual independent checks; no batch or hosted CI execution claimed.
  snapshot_sha256: 3fa3e7f64b14d4c25df1c06d302d6667846d93328102757e3519421c38ebb314
assessments:
- assessment_id: identity
  area: identity
  topic: Natural resource, feed provenance and species boundaries
  outcome: supported
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  evidence_ids:
  - primary
  - record
  summary: Source-specific ferruginous poorly sorted clay above volcanic breccia is
    a primary resource; isolate country-rock profile differs. Individual clay minerals,
    constituent rare earths and processing residues are not conflated.
  dimensions:
  - name: material_form
    value: Natural ion-adsorption rare-earth clay; one Madagascan feed
    definition: Scope of experimental material, not every ion-adsorption deposit.
    evidence_ids:
    - primary
    - record
  - name: criticality
    value: No criticality designation asserted
    definition: No jurisdiction/list/edition claim inherited from constituent rare
      earths.
    evidence_ids:
    - record
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated release with nonsterile controls
  outcome: supported
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  evidence_ids:
  - primary
  - supplement
  - record
  - taxonomy
  summary: Living separate genus-level isolates, nonaseptic provenance,25°C/150rpm/60days,3g
    per150mL,<0.5mm feed,48h preculture and140g/L glucose match originals. Uninoculated
    feed was not sterile and developed acidification; all release is not assigned
    exclusively to inoculated taxa. Proton versus ligand effects remain unresolved.
  dimensions:
  - name: control_scope
    value: Uninoculated CAB contains nonsterile feed; chemical salt comparator0.5M
      ammonium sulfate
    definition: Neither culture control establishes a fully sterile matched abiotic
      experiment.
    evidence_ids:
    - primary
    - record
- assessment_id: outcomes
  area: quantity
  topic: Release denominator, chemical advantage and uncertainties
  outcome: supported
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  evidence_ids:
  - primary
  - workbook_read
  - supplement
  - record
  summary: Lu percentages use total feedLu; mass-based workbook values are not solution
    concentrations or purified yields. Salt is generally faster/better withCe exception;
    sourceCe R² disagreement, possible redox explanation, slow kinetics andSi/Fe co-leaching
    remain qualified. Dy discrepancy is retained in dossier without selecting a measurement.
- assessment_id: provenance
  area: provenance
  topic: Dossier Table4 misdescription
  outcome: concern
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  evidence_ids:
  - table4_pixels
  - independent_render
  - publisher_xml
  - dossier_md
  summary: The original source visibly prints Eh4.38; the frozen dossier falsely labels
    its cell blank and blames extraction. Minor evidence-description defect; the record
    does not contain or rely on this Eh value. A dated correction note can supersede
    this sentence while preserving original dossier and review.
- assessment_id: structure
  area: schema
  topic: Frozen provenance and structural checks
  outcome: supported
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  evidence_ids:
  - verification
  - history
  - schema
  summary: Named strict validation and all50 raw hashes passed; inline/canonical CREATE
    are distinct actual events. Full batch verification is pending and not substituted
    by source checks.
findings:
- finding_id: F1
  issue_key: CMMMech.ion-adsorption-rare-earth-clay.dossier-table4-eh
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source dossier misstates printed Table4 Eh as an extraction artifact
  description: Under Contradictions and extraction hazards, the dossier says the Original
    medium Eh cell is visually blank and the extractor duplicated pH4.38. Both independently
    rendered original PDF page6 and publisher XML print4.38 in the Eh cell as well
    as pH. Correct the documentary claim without declaring the source value scientifically
    valid or a confirmed typo. The record imports no Eh value and needs no scientific
    change.
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  field_paths:
  - research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md#Contradictions-and-extraction-hazards:Table4-bullet
  evidence_ids:
  - dossier_md
  - table4_pixels
  - independent_render
  - publisher_xml
  - record
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md
    role: Source dossier; append a dated correction preserving original
  rule_id: primary-source-exact-observation
  native_severity: minor
  normalization_reason: Bounded source-dossier observation error; no wrong record
    identity, measurement or mechanism depends on the disputed Eh cell.
actions:
- action_id: A1
  description: 'Append a timestamped paired source correction explicitly superseding
    only the original Table4 bullet: both PDF and XML print4.38 in pH and Eh; its
    physical correctness is unresolved and it is not curated. Preserve the original
    dossier, initial review and unchanged record/history; save a full successor with
    correction input and exact F1 lineage.'
  finding_ids:
  - F1
  target_ids:
  - cmmmech:ion-adsorption-rare-earth-clay
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: research/sources/round51-ree-clay/20261012T083313Z-source-investigation.md
    role: Source dossier; append a dated correction preserving original
  acceptance_checks:
  - Reinspect original PDF page6 and publisher XML Table4 final row.
  - Pin original dossier and new correction hashes; prove record/history unchanged.
  - Save full scientific successor after actual cohort gates, resolving this exact
    F1 issue key without rewriting predecessor.
limitations:
- Required cohort checks are pending for this initial observation; completion is partial,
  not a final passing acceptance.
- The study does not resolve each community member contribution, strain identity,
  proton versus complexation or isolated product recovery; no industrial deployment
  or taxonomic reclassification inferred.
- Original main11pages, all3figures/5tables, all4supplementpages and allworkbookcells
  were independently inspected. No independent culture, sequence reanalysis, chemical
  measurement or raw statistical rerun performed.
- Table4 prints a duplicated number; this review establishes its presence only, not
  that it is valid or a proven publisher error.
- Notice search and curator dedup are bounded; missing raw roots and unextracted binary
  contents do not support global absence claims.
notes:
- Initial native finding saved before any correction. No record, Git, GitHub or governance
  mutation by this reviewer.
tags:
- round51
- clay
- independent
- initial
```
