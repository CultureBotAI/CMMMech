# Independent scientific review of arsenopyrite leaching and proposed passivation

- Review: 20261011T195823Z-arsenopyrite-round32-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T19:50:46.627225Z
- Finished UTC: 2026-10-11T19:58:23.013184Z
- Reviewer: Codex /root/round27_superalloy (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen arsenopyrite record is scientifically supported within its explicit laboratory and causal limits. All original methods, figures, tables, authority identities and provenance were independently assessed. No corrective finding was identified. Independent named validation and the actual final corrected-cohort tests, nonempty-record and trusted-base-history gates passed; all terminal logs were read and SHA-256 verified.

## Scope And Provenance

Every field of one new mineral record, one mechanism, all evidence entries, source references and distinct CREATE/inline provenance.

Selection: Assigned frozen record authored by another agent in round32.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 09c15cbfb7699e40ae4648b6b414784a00b488db.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:arsenopyrite | data/records/arsenopyrite.yaml | maintained | Arsenopyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:arsenopyrite | Reviewer executed at 2026-10-11T19:51:41.188651+00:00; one checked,zero failed. Log /private/tmp/cmm-round32-arsenopyrite-independent/named-validation.log SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e |
| Final corrected-cohort batch gate | passed | True | cmmmech:arsenopyrite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round32-final-batch.log SHA256 91fc92a09a1ef9acd34601d396f1956413ad4d0908a98399d6bdff93c817b541. All checks passed!; 308 passed, 3 skipped in 172.64s (0:02:52); Checked 187 record(s); 0 failed.; Checked 215 history record(s); 0 error(s). |
| Final corrected-cohort nonempty gate | passed | True | cmmmech:arsenopyrite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round32-final-nonempty.log SHA256 3870a3df4688495609ebd3dce4c53379dc4bd7f1a56290d344ad3305e9e0b6e8. Checked 187 record(s); 0 failed. |
| Final corrected-cohort history gate | passed | True | cmmmech:arsenopyrite | Root executed; reviewer independently read complete terminal log and SHA-256 verified it. /private/tmp/cmm-round32-final-history.log SHA256 76cc5044dce12bef4c094bf7e498e5830da0fdb431ee001241a0e78159d21bab. Checked 215 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Mineral identity, species scope and criticality omission

identity: supported. Targets: cmmmech:arsenopyrite.

FeAsS identity is verified at IMA. Natural high-purity specimen is explicit and is not treated as gold-bearing ore; species920 does not identify a strain. No inherited criticality is asserted.

### Living culture, preparation, conditions and controls

evidence: supported. Targets: cmmmech:arsenopyrite.

Record values match original sections3.1-3.3, including all listed9K salts, three-month adaptation, initialpH1.8,30°C/160rpm and particle versus cube handling. The100mLmedium+15mLinoculum is accurately preserved rather than asserted as100mL final volume. Sterile,pH-matched controls, replication and error-bar definitions are not supplied and are explicit.

### Dissolved arsenic, reported leaching ratio and relative residue phases

quantity: supported. Targets: cmmmech:arsenopyrite.

The30.4% and1.3g/L after19days are accurately source-reported, not reconstructed recovery. Figure1a has a plateau but visibly varying earlier slope. Figures1c-d and9Kcomposition prevent attributing iron solely to mineral. Figure2b is relative residue weight fraction;Table1 is local atomic percentage. Neither is a whole-mineral massbalance.

### Observed surface films versus proposed passivation model

evidence: supported. Targets: cmmmech:arsenopyrite.

Dense early36/120hfilm and porous8daydeposits are visible in Figures4-5;Table1 confirms As/S enrichment relative toFe rather than molecular identification. ParticleXRD is a separate supporting line. The source admits kinetic and equilibrium tensions; the record consistently retains the earlyfilm explanation as proposed, with no removal perturbation or universaljarosite claim.

### Laboratory result and conditional evidence boundaries

scope: supported. Targets: cmmmech:arsenopyrite.

No isolated arsenic product, measured gold recovery or industrial deployment is claimed. Additive/strain-specific related studies and mixed gold ores are not pooled into the single natural-mineral assay.

### Exact reviewed bytes and actual curation provenance

provenance: supported. Targets: cmmmech:arsenopyrite.

Source identity and actual CREATE/inline metadata are coherent. Final native capture exactly matches initial reviewed bytes at trustedbase09c15cb. Independent named validation and all final required cohort gates pass; terminal logs independently read and hashed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/arsenopyrite.yaml; Complete frozen record, all maintained fields | supports | Exact reviewed bytes retain material, assay, numerical and causal scope without asserting a microbial increment over a sterile control. |
| primary | https://doi.org/10.3390/met9121320; Complete publisher PDF11pages; sections2-5, Figures1-6, Tables1-2 and AppendixA. All original pages visually inspected and full text read. | supports | Natural Yaogangxian FeAsS specimens and cultured A.ferrooxidans are explicitly specified. Methods support both particle and prepared cube assays. Figure1a gives a plateau near30.4% while early changes are not exactly constant. Particle XRD/QPA and cube SEM/EDS are different geometries; modeled Eh-pH and proposed reactions do not establish selective causal proof. |
| xml | https://mdpi-res.com/d_attachment/metals/metals-09-01320/article_deploy/metals-09-01320.xml; Complete publisher XML, article identity and supplement-element scan | supports | XML corroborates complete article identity. No separate supplementary-material node/link was found in this inspected original XML; AppendixA is in the main article. This is not a global absence assertion or substitute for reading the actual figures. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September2026 original PDFpage15 Arsenopyrite row; page1 column definitions | supports | Row reads FeAsS,statusA,1962s.p. The record accurately preserves special-procedure notation without fabricating an approval accession, and distinguishes mineral from elemental arsenic and mixed ores. Same-day retained authority edition reused, not claimed as a new independent download. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=info; Live official current name and species rank opened independently11October2026; retained same-day original HTML | supports | NCBITaxon920 identifies Acidithiobacillus ferrooxidans at species level. The study provides no strain accession; the record does not borrow a type-strain identity. |
| metadata | https://api.crossref.org/works/10.3390/met9121320; Retained Crossref record, original PDF title and publication header | supports | Authors,title,DOI,Metals9(12)1320 and2019 agree. Relation is empty and update-to/updates absent in this retained response; no affecting notice is identified by that metadata alone. |
| history | history/records/arsenopyrite/2026-10-11T194714Z-codex-d48d52.yaml; Complete canonical CREATE and separate inline event | supports | Actual19:47:14Z Codex/GPT-6/codex CREATE targets the new file and accurately describes supported scope and pending independent review. Inline event is separately timestamped19:47:29Z. Neither fabricates prior curation or already-completed checks. |
| dedup | /private/tmp/cmm-round32-arsenopyrite-independent/dedup.json; Reviewer-executed hidden/ignored and symlink-aware query, exact command and output retained | supports | The new mineral record and experimental primary are not conflated with dissolved-arsenic or gold-bearing resources. Matching research/raw references are source leads, not additional accepted copies of the same maintained mineral record. |
| notices | Independent web search11October2026; First result sets for exact-DOI notice search and targeted arsenopyrite/passivation contrast search | supports | No affecting correction/retraction was identified in these bounded results. Primary related sources describe different additives/strains and surface products; they do not refute this specific unamended9K observation. Official publisher web-open had an internal parser error, but complete publisher PDF/XML were available and independently read. |
| counter | https://www.mdpi.com/2075-4701/10/3/403; Related2020 original publisher sections4.3-4.4 returned by search; targeted text only, not full independent study assessment | context_only | Ag-amended arsenopyrite study describes altered early phases and a comparison with its no-Ag condition. This confirms that additive-specific results should not be transferred into this record. Quantities, strains and new extraction mechanisms from this related work are not adopted. |
| gates | /private/tmp/cmm-round32-final-terminal.json; All three completed command entries and corresponding complete logs; final canonical input recapture | supports | All three required cohort commands finished with exit0 after molybdenite correction. Reviewer independently read and SHA-256 checked each log. Final native capture matches all original arsenopyrite target/history/schema input hashes exactly, preserving the original scientific assessment. |

## Limits And Additional Notes

- No matched sterile, matched-pH or cell-contact perturbation is reported; this cannot quantify a biological increment or prove phase-specific passivation.
- Experimental strain accession, exactreplicatecount,errorbardefinition and initial inoculumdensity remain unspecified.
- 100mLmedium+15mLinoculum and10g/Lpulp do not establish a transparently recalculable final-volume recovery denominator; solution leaching is not isolated product.
- ParticleXRD and preparedcubeSEM/EDS use different geometries and post-treatment; no rawinstrument reprocessing or absolute solidmassbalance is available.
- Thermodynamics at25°C and1atm are modeled context for30°Cculture; the original source notes earlyphase disagreement.
- Related-source and correction/retraction searches were bounded. The2020Agpaper was assessed only as targeted primary context; no complete review or imported measurements are claimed.
- All11original pages, sixfigures, twoTables andAppendixA independently inspected. No maintained target/history/dossier edited by reviewer.
- No corrective finding is invented from a primary-source limitation that the maintained record already states accurately.
- Rawprimary and authorities remain outsideGit with hashes in this review and curator acquisition logs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T195823Z-arsenopyrite-round32-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of arsenopyrite leaching and proposed passivation
started_at: '2026-10-11T19:50:46.627225Z'
finished_at: '2026-10-11T19:58:23.013184Z'
reviewer:
  identity: Codex /root/round27_superalloy
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: A different agent authored arsenopyrite. Reviewer curated only
    molybdenite this round and did not edit this record/history/dossier. Native inspect
    captured the frozen target before scientific judgment. Reviewer independently
    read the complete original11-page article, all6figures, both tables, AppendixA,
    IMA row, live NCBI taxonomy, source metadata and bounded counterevidence/notices.
    Shared worktree and curator-acquired raw files are disclosed. Root executed cohort
    gates; reviewer read and hash-verified their actual terminal receipts and recaptured
    unchanged inputs before final saving.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen arsenopyrite record is scientifically supported within its explicit
  laboratory and causal limits. All original methods, figures, tables, authority identities
  and provenance were independently assessed. No corrective finding was identified.
  Independent named validation and the actual final corrected-cohort tests, nonempty-record
  and trusted-base-history gates passed; all terminal logs were read and SHA-256 verified.
source:
  git_revision: 09c15cbfb7699e40ae4648b6b414784a00b488db
  state: working_tree
  inputs:
  - path: data/records/arsenopyrite.yaml
    sha256: c5964569b34c3bb772113634b0dde144d6f79849a36f076c7d3effb8083ccc4d
    role: target
  - path: history/records/arsenopyrite/2026-10-11T194714Z-codex-d48d52.yaml
    sha256: 1f3458e71098d3b12d0375968fcdea2cc896428f410451b6e881186255f78dfd
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Every field of one new mineral record, one mechanism, all evidence
    entries, source references and distinct CREATE/inline provenance.
  selection: Assigned frozen record authored by another agent in round32.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:arsenopyrite
  exclusions:
  - target: Additional arsenopyrite studies and raw instrument data
    reason: Other strains, additives, feedstocks and unavailable raw instruments are
      not newly curated or reprocessed. Bounded related-source inspection tests universal-scope
      claims without treating abstracts as methods evidence.
targets:
- target_id: cmmmech:arsenopyrite
  path: data/records/arsenopyrite.yaml
  label: Arsenopyrite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/arsenopyrite.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked cmmmech validate
    data/records/arsenopyrite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed at 2026-10-11T19:51:41.188651+00:00; one checked,zero
    failed. Log /private/tmp/cmm-round32-arsenopyrite-independent/named-validation.log
    SHA256 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  target_ids:
  - cmmmech:arsenopyrite
- check_id: batch
  name: Final corrected-cohort batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round32-final-batch.log SHA256 91fc92a09a1ef9acd34601d396f1956413ad4d0908a98399d6bdff93c817b541.
    All checks passed!; 308 passed, 3 skipped in 172.64s (0:02:52); Checked 187 record(s);
    0 failed.; Checked 215 history record(s); 0 error(s).
  target_ids:
  - cmmmech:arsenopyrite
- check_id: nonempty
  name: Final corrected-cohort nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round32-final-nonempty.log SHA256 3870a3df4688495609ebd3dce4c53379dc4bd7f1a56290d344ad3305e9e0b6e8.
    Checked 187 record(s); 0 failed.
  target_ids:
  - cmmmech:arsenopyrite
- check_id: history
  name: Final corrected-cohort history gate
  command: uv run --locked cmmmech validate-history --base 09c15cbfb7699e40ae4648b6b414784a00b488db
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root executed; reviewer independently read complete terminal log and SHA-256
    verified it. /private/tmp/cmm-round32-final-history.log SHA256 76cc5044dce12bef4c094bf7e498e5830da0fdb431ee001241a0e78159d21bab.
    Checked 215 history record(s); 0 error(s).
  target_ids:
  - cmmmech:arsenopyrite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/arsenopyrite.yaml
  locator: Complete frozen record, all maintained fields
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: Exact reviewed bytes retain material, assay, numerical and causal scope
    without asserting a microbial increment over a sterile control.
  snapshot_sha256: c5964569b34c3bb772113634b0dde144d6f79849a36f076c7d3effb8083ccc4d
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.3390/met9121320
  locator: Complete publisher PDF11pages; sections2-5, Figures1-6, Tables1-2 and AppendixA.
    All original pages visually inspected and full text read.
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: Natural Yaogangxian FeAsS specimens and cultured A.ferrooxidans are explicitly
    specified. Methods support both particle and prepared cube assays. Figure1a gives
    a plateau near30.4% while early changes are not exactly constant. Particle XRD/QPA
    and cube SEM/EDS are different geometries; modeled Eh-pH and proposed reactions
    do not establish selective causal proof.
  snapshot_sha256: 062168a7c2e6bf9cfc8524f4e30e4511d86c5dea931b6c787b960810ed3afb19
- evidence_id: xml
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/metals/metals-09-01320/article_deploy/metals-09-01320.xml
  locator: Complete publisher XML, article identity and supplement-element scan
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: XML corroborates complete article identity. No separate supplementary-material
    node/link was found in this inspected original XML; AppendixA is in the main article.
    This is not a global absence assertion or substitute for reading the actual figures.
  snapshot_sha256: 502e544c00e3af0ada01144d1a2ebe60a0c999ae4b13ce0f1f40982ed9e7967f
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September2026 original PDFpage15 Arsenopyrite row; page1 column definitions
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: Row reads FeAsS,statusA,1962s.p. The record accurately preserves special-procedure
    notation without fabricating an approval accession, and distinguishes mineral
    from elemental arsenic and mixed ores. Same-day retained authority edition reused,
    not claimed as a new independent download.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=info
  locator: Live official current name and species rank opened independently11October2026;
    retained same-day original HTML
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: NCBITaxon920 identifies Acidithiobacillus ferrooxidans at species level.
    The study provides no strain accession; the record does not borrow a type-strain
    identity.
  snapshot_sha256: c6d264e2f6ed730350be86773d9564c7427f7f089b57ed566d6494e3bd21a4ac
- evidence_id: metadata
  kind: database
  reference: https://api.crossref.org/works/10.3390/met9121320
  locator: Retained Crossref record, original PDF title and publication header
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: Authors,title,DOI,Metals9(12)1320 and2019 agree. Relation is empty and
    update-to/updates absent in this retained response; no affecting notice is identified
    by that metadata alone.
  snapshot_sha256: fa6ce85b8a69cb9a5feae8655cc7f2d0edd826a56be4aa2e68a65b8c5a1ae85d
- evidence_id: history
  kind: record_content
  reference: history/records/arsenopyrite/2026-10-11T194714Z-codex-d48d52.yaml
  locator: Complete canonical CREATE and separate inline event
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: Actual19:47:14Z Codex/GPT-6/codex CREATE targets the new file and accurately
    describes supported scope and pending independent review. Inline event is separately
    timestamped19:47:29Z. Neither fabricates prior curation or already-completed checks.
  snapshot_sha256: 1f3458e71098d3b12d0375968fcdea2cc896428f410451b6e881186255f78dfd
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round32-arsenopyrite-independent/dedup.json
  locator: Reviewer-executed hidden/ignored and symlink-aware query, exact command
    and output retained
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: The new mineral record and experimental primary are not conflated with
    dissolved-arsenic or gold-bearing resources. Matching research/raw references
    are source leads, not additional accepted copies of the same maintained mineral
    record.
  snapshot_sha256: a769f1496a21010ea046f96c54ff9ab2f1eb9c9b690f3920da1497811e58ecc0
  search_scope: Current and original records/research/reviews/history; available non-cache
    roots inherited from round31 referenced-raw inventory plus all round31 research
    roots and current raw. Hidden and ignored included, relevant symlinks followed.
    PDF/image/Office/archive bytes excluded; available extracted text and metadata
    searched. Accepted original PDF pages independently inspected; no OCR or global-binary
    absence assertion. Independent review adds current arsenopyrite raw. Query arsenopyrite|met9121320|passivating
    products. Successful exit0 without stderr. No global binary/OCR or machine-wide
    absence claim.
- evidence_id: notices
  kind: search
  reference: Independent web search11October2026
  locator: First result sets for exact-DOI notice search and targeted arsenopyrite/passivation
    contrast search
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: supports
  summary: No affecting correction/retraction was identified in these bounded results.
    Primary related sources describe different additives/strains and surface products;
    they do not refute this specific unamended9K observation. Official publisher web-open
    had an internal parser error, but complete publisher PDF/XML were available and
    independently read.
  search_scope: 'Exact queries: "10.3390/met9121320" correction retraction; arsenopyrite
    bioleaching Acidithiobacillus ferrooxidans jarosite passivation realgar orpiment
    contradiction. First returned result sets, no filters or pagination. Secondary/wiki
    results ignored. No exhaustive literature or notice absence asserted.'
- evidence_id: counter
  kind: primary_source
  reference: https://www.mdpi.com/2075-4701/10/3/403
  locator: Related2020 original publisher sections4.3-4.4 returned by search; targeted
    text only, not full independent study assessment
  accessed_at: '2026-10-11T19:55:31.008958Z'
  support: context_only
  summary: Ag-amended arsenopyrite study describes altered early phases and a comparison
    with its no-Ag condition. This confirms that additive-specific results should
    not be transferred into this record. Quantities, strains and new extraction mechanisms
    from this related work are not adopted.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round32-final-terminal.json
  locator: All three completed command entries and corresponding complete logs; final
    canonical input recapture
  accessed_at: '2026-10-11T19:58:23.013184Z'
  support: supports
  summary: All three required cohort commands finished with exit0 after molybdenite
    correction. Reviewer independently read and SHA-256 checked each log. Final native
    capture matches all original arsenopyrite target/history/schema input hashes exactly,
    preserving the original scientific assessment.
  snapshot_sha256: 2ca31d24e6ea16510ce3f9cb503df04eef634a84a45f3bb6074e132f2a9af8fa
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity, species scope and criticality omission
  outcome: supported
  summary: FeAsS identity is verified at IMA. Natural high-purity specimen is explicit
    and is not treated as gold-bearing ore; species920 does not identify a strain.
    No inherited criticality is asserted.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - primary
  - ima
  - taxon
  - dedup
  dimensions:
  - name: material_form
    value: Natural arsenopyrite mineral specimen
    definition: FeAsS species versus element, mixed concentrate and commodity scopes.
    evidence_ids:
    - primary
    - ima
  - name: criticality
    value: Not asserted
    definition: No jurisdiction,list or edition is borrowed from arsenic or gold.
    evidence_ids:
    - record
  - name: organism
    value: Acidithiobacillus ferrooxidans; speciesNCBITaxon920
    definition: Experimental strain accession and cell-density origin are absent and
      remain unassigned.
    evidence_ids:
    - primary
    - taxon
- assessment_id: methods
  area: evidence
  topic: Living culture, preparation, conditions and controls
  outcome: supported
  summary: Record values match original sections3.1-3.3, including all listed9K salts,
    three-month adaptation, initialpH1.8,30°C/160rpm and particle versus cube handling.
    The100mLmedium+15mLinoculum is accurately preserved rather than asserted as100mL
    final volume. Sterile,pH-matched controls, replication and error-bar definitions
    are not supplied and are explicit.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: biomass
    value: Living adapted culture
    definition: No washed inoculum, validated strain identity or initialcellcount
      is inferred.
    evidence_ids:
    - primary
    - record
  - name: conditions
    value: 250mLflask;100mLmedium+15mLinoculum;10g/LFeAsS;30°C;160rpm
    definition: Same cultivation conditions are expressly adopted for bioleaching;
      finalworkingvolume basis is not silently normalized.
    evidence_ids:
    - primary
  - name: controls
    value: No matched sterile or evolving-pH kinetic series
    definition: Therefore microbial enhancement above abiotic ferric chemistry is
      not quantified.
    evidence_ids:
    - primary
    - record
- assessment_id: measurements
  area: quantity
  topic: Dissolved arsenic, reported leaching ratio and relative residue phases
  outcome: supported
  summary: The30.4% and1.3g/L after19days are accurately source-reported, not reconstructed
    recovery. Figure1a has a plateau but visibly varying earlier slope. Figures1c-d
    and9Kcomposition prevent attributing iron solely to mineral. Figure2b is relative
    residue weight fraction;Table1 is local atomic percentage. Neither is a whole-mineral
    massbalance.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - primary
  dimensions:
  - name: solution_outcome
    value: Reported30.4%As leaching and1.3g/L after19days
    definition: Source formula/sampling correction unavailable; no exact independently
      computed extraction or isolated product asserted.
    evidence_ids:
    - primary
    - record
  - name: solid_outcome
    value: Relative phases and localEDS
    definition: ParticleQPAwt% and cubeEDSat% have different denominators, not totalrecovery.
    evidence_ids:
    - primary
- assessment_id: causality
  area: evidence
  topic: Observed surface films versus proposed passivation model
  outcome: supported
  summary: Dense early36/120hfilm and porous8daydeposits are visible in Figures4-5;Table1
    confirms As/S enrichment relative toFe rather than molecular identification. ParticleXRD
    is a separate supporting line. The source admits kinetic and equilibrium tensions;
    the record consistently retains the earlyfilm explanation as proposed, with no
    removal perturbation or universaljarosite claim.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - primary
  - counter
  dimensions:
  - name: causal_tier
    value: Culture-associated result and proposed ferric/passivation mechanism
    definition: No unique direct-cell attack or phase-specific causal contribution
      demonstrated.
    evidence_ids:
    - primary
    - record
  - name: modeled_result
    value: 25°C/1atmEh-pH and hypotheticalreaction energetics
    definition: Distinct from30°Ccultures and directspeciation.
    evidence_ids:
    - primary
- assessment_id: scope
  area: scope
  topic: Laboratory result and conditional evidence boundaries
  outcome: supported
  summary: No isolated arsenic product, measured gold recovery or industrial deployment
    is claimed. Additive/strain-specific related studies and mixed gold ores are not
    pooled into the single natural-mineral assay.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - primary
  - counter
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed bytes and actual curation provenance
  outcome: supported
  summary: Source identity and actual CREATE/inline metadata are coherent. Final native
    capture exactly matches initial reviewed bytes at trustedbase09c15cb. Independent
    named validation and all final required cohort gates pass; terminal logs independently
    read and hashed.
  target_ids:
  - cmmmech:arsenopyrite
  evidence_ids:
  - record
  - history
  - metadata
  - xml
  - gates
findings: []
actions: []
limitations:
- No matched sterile, matched-pH or cell-contact perturbation is reported; this cannot
  quantify a biological increment or prove phase-specific passivation.
- Experimental strain accession, exactreplicatecount,errorbardefinition and initial
  inoculumdensity remain unspecified.
- 100mLmedium+15mLinoculum and10g/Lpulp do not establish a transparently recalculable
  final-volume recovery denominator; solution leaching is not isolated product.
- ParticleXRD and preparedcubeSEM/EDS use different geometries and post-treatment;
  no rawinstrument reprocessing or absolute solidmassbalance is available.
- Thermodynamics at25°C and1atm are modeled context for30°Cculture; the original source
  notes earlyphase disagreement.
- Related-source and correction/retraction searches were bounded. The2020Agpaper was
  assessed only as targeted primary context; no complete review or imported measurements
  are claimed.
notes:
- All11original pages, sixfigures, twoTables andAppendixA independently inspected.
  No maintained target/history/dossier edited by reviewer.
- No corrective finding is invented from a primary-source limitation that the maintained
  record already states accurately.
- Rawprimary and authorities remain outsideGit with hashes in this review and curator
  acquisition logs.
links:
- https://doi.org/10.3390/met9121320
- https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
- https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=info
```
