# Whole-record scientific review of Melanterite after CCTCC provenance update

- Review: 20261020T065759Z-melanterite-issue340-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-20T04:10:14.306901Z
- Finished UTC: 2026-10-20T06:57:59.757544Z
- Reviewer: codex /root/investigate_134 (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified whole-record acceptance with no corrective findings. Newly verified CCTCC accession provenance is accurately represented as context; HJ-2 species/aliquot lineage, mixed-solid phase assignment and biological causation remain unresolved. No recovery, purity or industrial claim is strengthened.

## Scope And Provenance

Whole exact melanterite owner and both history sidecars, all asserted source/identifier bindings, original main study and complete official supplement, all relevant figures and current mineral authorities.

Selection: Assigned single maintained target; native inspect captured owner/history before scientific judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2da10d95a72146ee0c69cb91fe303348fbadb638.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:melanterite | data/records/melanterite.yaml | maintained | Melanterite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:melanterite | Reviewer command:1record,0failures. |
| Canonical history validation | passed | True | cmmmech:melanterite | Reviewer command:745sessions,0errors. |
| Completed post-edit repository gate | passed | True | cmmmech:melanterite | Parent actually ran the completed gate; reviewer inspected retained log and success report rather than repeating suite.327passed,3skipped;616records and745histories valid. |
| Strict full record validation | passed | True | cmmmech:melanterite | Reviewer command:616records,0failures. |

## Scientific And Domain Assessments

### Mineral identity, external identifiers and criticality scope

identity: supported. Targets: cmmmech:melanterite.

IMA and Handbook support the distinct ferrous sulfate heptahydrate mineral; no criticality or species-level organism identifier is invented.

### New public culture-deposit provenance

provenance: supported. Targets: cmmmech:melanterite.

The new catalog source is correctly limited to context. It establishes public accession/name/history metadata while preserving the original article/sequence species conflict.

### Biomass, feed, pretreatment, conditions and controls

scope: supported. Targets: cmmmech:melanterite.

The full context is source-supported and retains unspecified liquid volume, inoculum basis, cell density, solid collection time and preparation.

Context values independently checked:100mL bottle capacity,10mMPIPES,nominal5%inoculum,30°C;8000g/4°C/8min cell centrifugation and two washes. These are source protocol descriptions, not a newly optimized procedure. The144h solution endpoint is not asserted as XRD collection time.

### Mixed diffraction assignment and causal interpretation

evidence: supported. Targets: cmmmech:melanterite.

Provisional minor melanterite is a faithful source-assigned observation. Unreported workup permits residual sulfate crystallization; separate ferrous sulfate does not prove incorporation of Fe(II) into ferric phases.

### Measured and reported values, denominators and outcome

quantity: supported. Targets: cmmmech:melanterite.

The record preserves reported concentrations and phase-label percentages without treating them as phase yield, purity or closed balance.

### Actual curation events and reviewed-byte provenance

provenance: supported. Targets: cmmmech:melanterite.

Separate inline EDIT and canonical EDIT describe the parent curator action accurately. Earlier CREATE provenance and historical review remain immutable.

Native inspect captured the exact owner before assessment. Later inspection normalized target-kind/repository metadata and added context inputs, with the initial owner/history hashes unchanged. This is a fresh whole-record scientific review, not a provenance-only waiver.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/melanterite.yaml; Complete frozen owner, including all sources, mechanism, inline history and sidecar references. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/data/records/melanterite.yaml | supports | Exact working-tree record reviewed as a whole. Catalog provenance is the only scientific change; no material or organism identifier, causal claim, protocol, phase fraction or yield was strengthened. |
| history-new | history/records/melanterite/2026-10-20T040736Z-codex-2b34d2.yaml; Complete EDIT session, target, actor, timestamp and description compared with working diff and inline event. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/history/records/melanterite/2026-10-20T040736Z-codex-2b34d2.yaml | supports | Parent curator created this session for the catalog provenance change. It accurately distinguishes blank lineage fields from resolved accession lookup and retains earlier immutable CREATE history. |
| history-old | history/records/melanterite/2026-10-15T124511Z-codex-f47746.yaml; Complete prior CREATE sidecar and corresponding inline event. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/history/records/melanterite/2026-10-15T124511Z-codex-f47746.yaml | supports | Historical actor and scope retained without rewriting authorship; the later reviewer did not curate owner or history. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 edition: PDF page139, Melanterite row visually inspected; definitions and terms on pages1–2 read. Newly downloaded bytes equal the PDF used to render page139. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-ima-202609.pdf | supports | Melanterite formula Fe(SO4)(H2O)6·H2O, G status and original-description year1850 support the distinct grandfathered mineral; G is not a numeric approval identifier. |
| handbook | https://handbookofmineralogy.org/pdfs/melanterite.pdf; Complete one-page entry, version1 (2001–2005), chemistry and cell data visually inspected. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-handbook.pdf | supports | Ferrous sulfate heptahydrate, monoclinic P21/c. Ideal mineral identity does not establish the culture-derived specimen purity. |
| primary | https://doi.org/10.1093/lambio/ovac022; Complete publisher HTML, especially Experimental setup, Analytical methods, Isolation and identification, nitrate and nitrite Results, Data availability; all main captions read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/peng2023-minimal.html | supports | Washed log-phase HJ-2 cells and no-cell/no-nitrate comparators support a culture-associated solution response. Solid preparation and comparator diffraction are unspecified. Main C.terrigena/NBRC14951 identification conflicts with original SI and current sequence labels. |
| si | https://doi.org/10.1093/lambio/ovac022; Complete official DOCX: native MethodologyS1, all TablesS1–S8, captions and all3 embedded original graphics read. Original embedded-image bytes verified against extracted images; no Word page-rendering claim. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/peng2023-si.docx | supports | The supplement is part of the same experiment. Functional annotations are predictions, not expression, enzyme or knockout demonstrations. FigureS2 provides a mixed pattern with an unresolved quantification basis, not a pure product or controlled mineral-formation test. |
| fig1 | https://doi.org/10.1093/lambio/ovac022; Original main Figure1 visually inspected with corresponding caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig1.jpeg | context_only | SEM/EDS and enrichment/cell images support Fe-bearing material but do not identify melanterite. |
| fig2 | https://doi.org/10.1093/lambio/ovac022; Original main Figure2 visually inspected with corresponding caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig2.jpeg | context_only | Nitrate arm: Fe(II) reported3.64→0.84mmol/L by144h, with little change in no-cell/no-nitrate comparators; no mineral-yield denominator. |
| fig3 | https://doi.org/10.1093/lambio/ovac022; Original main Figure3 visually inspected with corresponding caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig3.jpeg | context_only | Nitrite consumes Fe(II) with and without cells, with reported zero by480h; abiotic chemistry remains substantial. |
| fig4 | https://doi.org/10.1093/lambio/ovac022; Original main Figure4 visually inspected with corresponding caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig4.jpeg | context_only | Separate soluble Fe(III)-NTA reduction arm; not transferred to melanterite formation or recovery. |
| fig5 | https://doi.org/10.1093/lambio/ovac022; Original main Figure5 visually inspected with corresponding caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig5.jpeg | context_only | Separate nitrobenzene/aniline arm; not transferred to melanterite formation or recovery. |
| si1 | https://doi.org/10.1093/lambio/ovac022; Original embedded FigureS1, node labels and accessions visually inspected. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image1.jpeg | context_only | HJ-2 MZ701937.1 is adjacent to C.testosteroni NBRC14951 AB680720.1 and separate from plotted C.terrigena strains; a phylogenetic neighbor is not a reconciled species identity. |
| si2 | https://doi.org/10.1093/lambio/ovac022; Original embedded FigureS2: full diffraction trace, legend, assigned peaks, PR-1.raw label and caption visually inspected. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image2.jpeg | partial | Source reports melanterite13.35%, goethite55.52%, lepidocrocite15.35%, hematite15.76%. No underlying PR-1.raw file, refinement, uncertainty, internal standard or absolute phase-mass basis is supplied; percentages remain provisional source labels. |
| si3 | https://doi.org/10.1093/lambio/ovac022; Original embedded FigureS3 visually inspected with caption. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image3.png | context_only | Separate arsenate arm, excluded from mineral identity or yield claims. |
| mz701937 | https://www.ncbi.nlm.nih.gov/nuccore/MZ701937.1; Current NCBI XML accession-version, definition, organism and strain/taxon qualifiers read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/genbank-MZ701937.xml | context_only | MZ701937.1 is C.thiooxydans strainHJ-2, TaxId363952. Sequence label supports conflict documentation, not silent renaming of the article experiment. |
| ab680720 | https://www.ncbi.nlm.nih.gov/nuccore/AB680720.1; Current NCBI XML accession-version, definition, strain and type-material qualifiers read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/genbank-AB680720.xml | context_only | AB680720.1 identifies C.testosteroni NBRC14951 and agrees with FigureS1. Its type-strain status is not inherited by HJ-2. |
| cctcc | https://cctcc.whu.edu.cn/portal/no_center/wsw_detail_en?id=98389&amp;kind=bacteria; Public General information fields cctcc_no, name, strain_designation, type_culture, history, literature and genbank_accession_numbers read in original HTML. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/cctcc-hj2-detail.html | context_only | CCTCC AB2021274, C.thiooxydans HJ-2, non-type culture, historyChinaUniversityofGeosciences. Literature and sequence-accession fields are blank. Accession lookup is supported; experimental-aliquot/sequence lineage and article species conflict remain unresolved. |
| catalog-query | https://cctcc.whu.edu.cn/api/mic_en/search; Retained read-only public accession-search POST response (fie=f3; kind=bacteria; keyword=2021274; precision=2; p=1): exact accession row, id98389, HJ-2, non-type and name fields. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/cctcc-deposit-query.json | context_only | The public query binds the displayed detail entry to the article-reported accession. The date-like field hz_sc is not assigned deposition-date semantics. |
| crossref | https://api.crossref.org/works/10.1093/lambio/ovac022; Current relation/update fields inspected directly. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/crossref.json | context_only | No correction/retraction relation or update-to/updated-by field in this retrieved response; this is a metadata-bound observation only. |
| pubmed | https://pubmed.ncbi.nlm.nih.gov/36688790/; Retrieved PubMed XML CommentsCorrections nodes inspected directly. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/pubmed.xml | context_only | No CommentsCorrections nodes in this retrieved record; does not establish universal absence of a notice. |
| search | Bounded current source/notice and local overlap search; Two fresh exact queries plus same-day twenty-query dossier; retained raw response and argument scope. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-web-search.json | context_only | Inspected result window did not supply a study-specific correction or missing controlled phase dataset. Returned later work remains distinct, not a correction or same-aliquot experiment. |
| search-scope | Reviewer bounded ignored-inclusive search receipt; Complete current scope and exact local matching-file list. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-scope.json | context_only | Actual retained local matching-file list contains33files, including current owner, current handoff and historical related records. Match counts are not novelty evidence. |
| named | Reviewer named structural validation; Actual completed command and output. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-named.log | supports | Checked1record;0failed. Structural validity is separate from scientific truth. |
| history-check | Reviewer canonical history validation; Actual completed command against base2da10d95a72146ee0c69cb91fe303348fbadb638. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-history.log | supports | Checked745historyrecords;0errors. |
| batch | Parent completed post-edit just check; Original complete log, parent terminal success and frozen-input identity checked; reviewer did not rerun the full suite. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-postedit-check.log | supports | 327tests passed,3skipped;616records valid;745historysessions valid. Owner/history unchanged since these successful gates. |
| require-records | Reviewer full strict record gate; Actual completed command output. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-require-records.log | supports | Checked616records;0failed. |
| canon | Parent canonical CLAW artifact check; Original completed log and parent terminal success checked. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-canon.log | supports | 22governed artifacts match the pinned revision. |
| prior | reviews/structured/20261015T130653Z-melanterite-round95-independent/review.yaml; Complete historical observation read; no prior corrective findings were present. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/reviews/structured/20261015T130653Z-melanterite-round95-independent/review.yaml | context_only | Earlier scientific review accepted the qualified phase observation; this round reassesses the entire new owner and updates the deposit-access limit without claiming other gaps closed. |

## Limits And Additional Notes

- HJ-2 species assignment remains conflicting across main article, comparator tree, GenBank and CCTCC. Blank catalog literature/sequence fields prevent experimental-aliquot linkage; catalog agreement with MZ701937.1 does not reconcile the article.
- Melanterite remains a provisional minor phase in mixed solids. No raw diffraction re-refinement, preparation history, matched control-solid patterns, uncertainty or absolute phase-mass basis establishes biological necessity, purity or isolated yield.
- Whole main publisher HTML, all5original main graphics, native DOCX tables/captions and3embedded original graphics were inspected. No claim of Word page rendering or inspection of a publisher PDF.
- Bounded current searches and metadata checks do not establish universal absence of corrections or contradictory literature. Public later HJ-2/genome metadata is not accepted as same-sample experimental proof.
- Review independence is from owner/history curation; this reviewer authored the preceding source-discovery handoff.
- Actual native-inspection start is retained across the usage interruption; finish is the current UTC assessment completion, not a historical filename timestamp.
- Review file state is working_tree against main2da10d95; uncommitted source/history provenance is preserved honestly. No record, history, commit or outbound mutation by the reviewer.
- Initial uv inspection encountered global-cache sandbox access; a subsequent successful inspection completed. All later native commands used the existing environment with a scratch uv cache and offline/no-sync settings.
- The first IMA fetch was slow; a current earlier same-day official PDF was rendered and checked while waiting. The independent fetch completed successfully with exactly identical bytes.
- Prior review contains no corrective findings, so this clean follow-up does not silently close a prior issue. Source issue340 remains partially advanced, not resolved.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T065759Z-melanterite-issue340-independent
kind: record
repository: CultureBotAI/CMMMech
title: Whole-record scientific review of Melanterite after CCTCC provenance update
started_at: '2026-10-20T04:10:14.306901Z'
finished_at: '2026-10-20T06:57:59.757544Z'
reviewer:
  identity: codex /root/investigate_134
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from the parent curator of owner/history; no
    owner or history edits by this reviewer. Reviewer performed the preceding source-discovery
    handoff and therefore shares source-investigation context; independence is from
    record authorship, not from all earlier research. Exact frozen owner, original
    authorities, complete main/SI and original figures were reassessed for this whole-target
    round.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Qualified whole-record acceptance with no corrective findings. Newly verified
  CCTCC accession provenance is accurately represented as context; HJ-2 species/aliquot
  lineage, mixed-solid phase assignment and biological causation remain unresolved.
  No recovery, purity or industrial claim is strengthened.
source:
  git_revision: 2da10d95a72146ee0c69cb91fe303348fbadb638
  state: working_tree
  inputs:
  - path: data/records/melanterite.yaml
    sha256: a14d43beecbbed572835b146cdd1018e179bce9e585b5c9e348cb209be392637
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/melanterite/2026-10-15T124511Z-codex-f47746.yaml
    sha256: 2996fe82187d85af5309a5bdb312c46daa80377682dab5a1fcb3604f5b68065f
    role: context
  - path: history/records/melanterite/2026-10-20T040736Z-codex-2b34d2.yaml
    sha256: e7e077f99504297c1815dd051068a8e0dfcb833634ef49243eb32a898136eb49
    role: context
  - path: research/sources/issue-340-hj2-phase-evidence/20261020T040235Z.json
    sha256: 4c2726939e3b29c9dcf8d7410866b6f4389d3af23ba0025e02606c915996684c
    role: context
  - path: research/sources/issue-340-hj2-phase-evidence/20261020T040235Z.md
    sha256: fe6c59b60d885d028bebcb5abc45bf077a1e87bbf041f2d139067ea7f6e89b35
    role: context
  - path: reviews/structured/20261015T130653Z-melanterite-round95-independent/review.yaml
    sha256: fe3de53c19a042a91cfbd17416c80c48255489e613dac00bad4daeadd9d0924d
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: 105313f55214e4b81ce23a1338262c752c44017c8150fba8721d75826ec03932
    role: context
scope:
  description: Whole exact melanterite owner and both history sidecars, all asserted
    source/identifier bindings, original main study and complete official supplement,
    all relevant figures and current mineral authorities.
  selection: Assigned single maintained target; native inspect captured owner/history
    before scientific judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:melanterite
  exclusions:
  - target: new mechanisms from later HJ-2 papers or public genome projects
    reason: Separate experiments/metadata remain source-discovery leads; they do not
      establish the original specimen lineage or melanterite formation.
  - target: recovery performance and re-refined phase fractions
    reason: No adequate underlying data; these stronger claims are not present in
      the reviewed owner.
targets:
- target_id: cmmmech:melanterite
  path: data/records/melanterite.yaml
  label: Melanterite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/melanterite.yaml
    role: maintained material record
checks:
- check_id: named
  name: Named record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-backlog-20261019-fmj36s/uv-cache UV_OFFLINE=1
    uv run --no-sync cmmmech validate data/records/melanterite.yaml --require-records
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer command:1record,0failures.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - named
- check_id: history
  name: Canonical history validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-backlog-20261019-fmj36s/uv-cache UV_OFFLINE=1
    uv run --no-sync cmmmech validate-history --base 2da10d95a72146ee0c69cb91fe303348fbadb638
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer command:745sessions,0errors.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - history-check
- check_id: batch
  name: Completed post-edit repository gate
  command: just check
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Parent actually ran the completed gate; reviewer inspected retained log
    and success report rather than repeating suite.327passed,3skipped;616records and745histories
    valid.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - batch
- check_id: require-records
  name: Strict full record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-backlog-20261019-fmj36s/uv-cache UV_OFFLINE=1
    uv run --no-sync cmmmech validate --require-records
  required: true
  status: passed
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer command:616records,0failures.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - require-records
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/melanterite.yaml
  locator: 'Complete frozen owner, including all sources, mechanism, inline history
    and sidecar references. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/data/records/melanterite.yaml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: a14d43beecbbed572835b146cdd1018e179bce9e585b5c9e348cb209be392637
  summary: Exact working-tree record reviewed as a whole. Catalog provenance is the
    only scientific change; no material or organism identifier, causal claim, protocol,
    phase fraction or yield was strengthened.
- evidence_id: history-new
  kind: record_content
  reference: history/records/melanterite/2026-10-20T040736Z-codex-2b34d2.yaml
  locator: 'Complete EDIT session, target, actor, timestamp and description compared
    with working diff and inline event. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/history/records/melanterite/2026-10-20T040736Z-codex-2b34d2.yaml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: e7e077f99504297c1815dd051068a8e0dfcb833634ef49243eb32a898136eb49
  summary: Parent curator created this session for the catalog provenance change.
    It accurately distinguishes blank lineage fields from resolved accession lookup
    and retains earlier immutable CREATE history.
- evidence_id: history-old
  kind: record_content
  reference: history/records/melanterite/2026-10-15T124511Z-codex-f47746.yaml
  locator: 'Complete prior CREATE sidecar and corresponding inline event. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/history/records/melanterite/2026-10-15T124511Z-codex-f47746.yaml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 2996fe82187d85af5309a5bdb312c46daa80377682dab5a1fcb3604f5b68065f
  summary: Historical actor and scope retained without rewriting authorship; the later
    reviewer did not curate owner or history.
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: 'September 2026 edition: PDF page139, Melanterite row visually inspected;
    definitions and terms on pages1–2 read. Newly downloaded bytes equal the PDF used
    to render page139. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-ima-202609.pdf'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
  summary: Melanterite formula Fe(SO4)(H2O)6·H2O, G status and original-description
    year1850 support the distinct grandfathered mineral; G is not a numeric approval
    identifier.
- evidence_id: handbook
  kind: authority
  reference: https://handbookofmineralogy.org/pdfs/melanterite.pdf
  locator: 'Complete one-page entry, version1 (2001–2005), chemistry and cell data
    visually inspected. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-handbook.pdf'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: c3611abddef4f071176123516f854401304f0e30599110ab436d968c0d6bcf5f
  summary: Ferrous sulfate heptahydrate, monoclinic P21/c. Ideal mineral identity
    does not establish the culture-derived specimen purity.
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Complete publisher HTML, especially Experimental setup, Analytical methods,
    Isolation and identification, nitrate and nitrite Results, Data availability;
    all main captions read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/peng2023-minimal.html'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 7731d6e161c1203a3596c70bd8ecf6d6d1d778ada3799f64c61a7f228c54bdea
  summary: Washed log-phase HJ-2 cells and no-cell/no-nitrate comparators support
    a culture-associated solution response. Solid preparation and comparator diffraction
    are unspecified. Main C.terrigena/NBRC14951 identification conflicts with original
    SI and current sequence labels.
- evidence_id: si
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Complete official DOCX: native MethodologyS1, all TablesS1–S8, captions
    and all3 embedded original graphics read. Original embedded-image bytes verified
    against extracted images; no Word page-rendering claim. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/peng2023-si.docx'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: f3bc22caff4a5db9464229205fffbefe509a2b0cb095f0f969e26d6519ebad01
  summary: The supplement is part of the same experiment. Functional annotations are
    predictions, not expression, enzyme or knockout demonstrations. FigureS2 provides
    a mixed pattern with an unresolved quantification basis, not a pure product or
    controlled mineral-formation test.
- evidence_id: fig1
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original main Figure1 visually inspected with corresponding caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig1.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: ef06d461a6afa42dab53383f296c7ed11b76fe34b8fa3ff7d5f5184c00b84001
  summary: SEM/EDS and enrichment/cell images support Fe-bearing material but do not
    identify melanterite.
- evidence_id: fig2
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original main Figure2 visually inspected with corresponding caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig2.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: e4379919931cfdd460f51132a52cb78f915842af5236a10d330991e8a5b52f2e
  summary: 'Nitrate arm: Fe(II) reported3.64→0.84mmol/L by144h, with little change
    in no-cell/no-nitrate comparators; no mineral-yield denominator.'
- evidence_id: fig3
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original main Figure3 visually inspected with corresponding caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig3.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: b98e1aee3bf4ad6d920af8338d8077d6452a5f359a5b0b328dde0ced8730ed8f
  summary: Nitrite consumes Fe(II) with and without cells, with reported zero by480h;
    abiotic chemistry remains substantial.
- evidence_id: fig4
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original main Figure4 visually inspected with corresponding caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig4.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 985a93e08f7838d2cf659e42e6a06f901911a2babc453d601bed98ed98c5946f
  summary: Separate soluble Fe(III)-NTA reduction arm; not transferred to melanterite
    formation or recovery.
- evidence_id: fig5
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original main Figure5 visually inspected with corresponding caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/ovac022fig5.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: ca5cd16d826f75b4fa949929d0a0335805c0c157d431f04d035caba49756d0e7
  summary: Separate nitrobenzene/aniline arm; not transferred to melanterite formation
    or recovery.
- evidence_id: si1
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original embedded FigureS1, node labels and accessions visually inspected.
    Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image1.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 57d3f0c29928cfba260958a7ea0e6dd0cbff67cb5fd3046bfb26c4eebdf8b7c6
  summary: HJ-2 MZ701937.1 is adjacent to C.testosteroni NBRC14951 AB680720.1 and
    separate from plotted C.terrigena strains; a phylogenetic neighbor is not a reconciled
    species identity.
- evidence_id: si2
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original embedded FigureS2: full diffraction trace, legend, assigned peaks,
    PR-1.raw label and caption visually inspected. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image2.jpeg'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: partial
  snapshot_sha256: b58863584318567f36a316eb128e5e0a5b912a9ee1d12cba98aec701f5f413e6
  summary: Source reports melanterite13.35%, goethite55.52%, lepidocrocite15.35%,
    hematite15.76%. No underlying PR-1.raw file, refinement, uncertainty, internal
    standard or absolute phase-mass basis is supplied; percentages remain provisional
    source labels.
- evidence_id: si3
  kind: primary_source
  reference: https://doi.org/10.1093/lambio/ovac022
  locator: 'Original embedded FigureS3 visually inspected with caption. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/image3.png'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 43195c2551ebd83eb3221ae717871e0dd3b02337f794ce9f642b67f6292105d9
  summary: Separate arsenate arm, excluded from mineral identity or yield claims.
- evidence_id: mz701937
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/MZ701937.1
  locator: 'Current NCBI XML accession-version, definition, organism and strain/taxon
    qualifiers read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/genbank-MZ701937.xml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 851d0bda7ad853006e475f3d2025e1152c19c99f83f67789d8af50812b15858d
  summary: MZ701937.1 is C.thiooxydans strainHJ-2, TaxId363952. Sequence label supports
    conflict documentation, not silent renaming of the article experiment.
- evidence_id: ab680720
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/AB680720.1
  locator: 'Current NCBI XML accession-version, definition, strain and type-material
    qualifiers read. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/genbank-AB680720.xml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 32b4ca9a9c07cd9fddf733c6e7a86fb2fec308504342d3582f49b237d1a023e9
  summary: AB680720.1 identifies C.testosteroni NBRC14951 and agrees with FigureS1.
    Its type-strain status is not inherited by HJ-2.
- evidence_id: cctcc
  kind: database
  reference: https://cctcc.whu.edu.cn/portal/no_center/wsw_detail_en?id=98389&kind=bacteria
  locator: 'Public General information fields cctcc_no, name, strain_designation,
    type_culture, history, literature and genbank_accession_numbers read in original
    HTML. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/cctcc-hj2-detail.html'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 56d39cad1df3754a022bdcfce89bc78e37a88d7aa1577391bde6a51ae7940283
  summary: CCTCC AB2021274, C.thiooxydans HJ-2, non-type culture, historyChinaUniversityofGeosciences.
    Literature and sequence-accession fields are blank. Accession lookup is supported;
    experimental-aliquot/sequence lineage and article species conflict remain unresolved.
- evidence_id: catalog-query
  kind: database
  reference: https://cctcc.whu.edu.cn/api/mic_en/search
  locator: 'Retained read-only public accession-search POST response (fie=f3; kind=bacteria;
    keyword=2021274; precision=2; p=1): exact accession row, id98389, HJ-2, non-type
    and name fields. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/cctcc-deposit-query.json'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: b216ca106f82ab96fb91e8cc4a4d3d30eb3664dd347f4657439dd8e37f97046c
  summary: The public query binds the displayed detail entry to the article-reported
    accession. The date-like field hz_sc is not assigned deposition-date semantics.
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1093/lambio/ovac022
  locator: 'Current relation/update fields inspected directly. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/crossref.json'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 3f021419402b8b80a7dd7192476dd9a2b3560e6d6d4e206fa86926f73e203b7f
  summary: No correction/retraction relation or update-to/updated-by field in this
    retrieved response; this is a metadata-bound observation only.
- evidence_id: pubmed
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/36688790/
  locator: 'Retrieved PubMed XML CommentsCorrections nodes inspected directly. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/pubmed.xml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 71ac0f0f5c5724a859f389861802f4bb10fbcafaff0da2affc625c3b9d9eb6ad
  summary: No CommentsCorrections nodes in this retrieved record; does not establish
    universal absence of a notice.
- evidence_id: search
  kind: search
  reference: Bounded current source/notice and local overlap search
  locator: 'Two fresh exact queries plus same-day twenty-query dossier; retained raw
    response and argument scope. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/sources-340/review-web-search.json'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 9fc634b4376b680df03de6171a04c23ba7ff6e426860b65001e4f5434cbf5bdf
  summary: Inspected result window did not supply a study-specific correction or missing
    controlled phase dataset. Returned later work remains distinct, not a correction
    or same-aliquot experiment.
  search_scope: 'Fresh exact queries: "10.1093/lambio/ovac022" (correction OR corrigendum
    OR erratum OR retraction); "HJ-2" "melanterite" (diffraction OR control OR correction).
    Earlier20queries in sources-340/web-search-1.json through web-search-5.json. Publisher
    HTML, Crossref and PubMed metadata checked. Local rg --no-ignore --hidden --follow
    over this worktree data/records, research/sources, reviews/structured, history/records
    returned33files; raw scratch and other checkouts excluded. No exhaustive absence
    claim.'
- evidence_id: search-scope
  kind: search
  reference: Reviewer bounded ignored-inclusive search receipt
  locator: 'Complete current scope and exact local matching-file list. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-scope.json'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: 003478fa5d249b2226185129cab1d91744b3e25110b09688933052b4f99d2e98
  summary: Actual retained local matching-file list contains33files, including current
    owner, current handoff and historical related records. Match counts are not novelty
    evidence.
  search_scope: rg --no-ignore --hidden --follow -n -l 'melanterite|MZ701937|ovac022|2021274'
    over data/records, research/sources, reviews/structured, history/records in issue-340.
    Hidden/ignored and followed symlinks included; raw scratch, unrelated checkouts
    and machine-wide roots excluded. Retained list has33files.
- evidence_id: named
  kind: validation
  reference: Reviewer named structural validation
  locator: 'Actual completed command and output. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-named.log'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
  summary: Checked1record;0failed. Structural validity is separate from scientific
    truth.
- evidence_id: history-check
  kind: validation
  reference: Reviewer canonical history validation
  locator: 'Actual completed command against base2da10d95a72146ee0c69cb91fe303348fbadb638.
    Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-history.log'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: b82876e657df90a30cb77317251616e6ae290765a60c68afdc3fb41a82eaa193
  summary: Checked745historyrecords;0errors.
- evidence_id: batch
  kind: validation
  reference: Parent completed post-edit just check
  locator: 'Original complete log, parent terminal success and frozen-input identity
    checked; reviewer did not rerun the full suite. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-postedit-check.log'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 41cd2e233839c62f864cb0c2fce0ce54269bed7a531350e2cc55bc545c2c1837
  summary: 327tests passed,3skipped;616records valid;745historysessions valid. Owner/history
    unchanged since these successful gates.
- evidence_id: require-records
  kind: validation
  reference: Reviewer full strict record gate
  locator: 'Actual completed command output. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-review-require-records.log'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: d47e19b123c18f1d48610ace095471a408192c504a56fb4fb473f668afceda40
  summary: Checked616records;0failed.
- evidence_id: canon
  kind: validation
  reference: Parent canonical CLAW artifact check
  locator: 'Original completed log and parent terminal success checked. Artifact:
    /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340-canon.log'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: supports
  snapshot_sha256: 3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e
  summary: 22governed artifacts match the pinned revision.
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261015T130653Z-melanterite-round95-independent/review.yaml
  locator: 'Complete historical observation read; no prior corrective findings were
    present. Artifact: /private/tmp/cmmmech-backlog-20261019-fmj36s/issue-340/reviews/structured/20261015T130653Z-melanterite-round95-independent/review.yaml'
  accessed_at: '2026-10-20T06:57:59.757544Z'
  support: context_only
  snapshot_sha256: fe3de53c19a042a91cfbd17416c80c48255489e613dac00bad4daeadd9d0924d
  summary: Earlier scientific review accepted the qualified phase observation; this
    round reassesses the entire new owner and updates the deposit-access limit without
    claiming other gaps closed.
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral identity, external identifiers and criticality scope
  outcome: supported
  summary: IMA and Handbook support the distinct ferrous sulfate heptahydrate mineral;
    no criticality or species-level organism identifier is invented.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - ima
  - handbook
  - mz701937
  - ab680720
  dimensions:
  - name: material-form
    value: mineral; FeSO4·7H2O; monoclinic P21/c
    definition: Mineral species identity; not dissolved ferrous sulfate, ferric oxide,
      commodity or other hydrate.
    evidence_ids:
    - ima
    - handbook
  - name: criticality
    value: unrecorded
    definition: No jurisdiction/list/edition designation asserted. Omission is not
      a not_listed claim and does not inherit iron commodity status.
    evidence_ids:
    - owner
- assessment_id: provenance
  area: provenance
  topic: New public culture-deposit provenance
  outcome: supported
  summary: The new catalog source is correctly limited to context. It establishes
    public accession/name/history metadata while preserving the original article/sequence
    species conflict.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - primary
  - si1
  - mz701937
  - ab680720
  - cctcc
  - catalog-query
  dimensions:
  - name: organism-strain
    value: Comamonas strain HJ-2; experimental species unresolved
    definition: Main C.terrigena, SI comparator C.testosteroni, HJ-2 sequence/catalog
      C.thiooxydans are kept separate. No comparison type-strain identity transfers.
    evidence_ids:
    - primary
    - si1
    - mz701937
    - ab680720
    - cctcc
- assessment_id: experiment
  area: scope
  topic: Biomass, feed, pretreatment, conditions and controls
  outcome: supported
  summary: The full context is source-supported and retains unspecified liquid volume,
    inoculum basis, cell density, solid collection time and preparation.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - primary
  - si
  - fig1
  - fig2
  - fig3
  dimensions:
  - name: biomass-state
    value: washed log-phase LB-grown cells
    definition: Cultured cells present; microbial:true denotes experimental inclusion
      and does not prove metabolically necessary melanterite crystallization.
    evidence_ids:
    - primary
    - owner
  - name: substrate
    value: FeSO4 and nitrate in buffered laboratory microcosm
    definition: Not mineral-feed leaching or industrial recovered iron.
    evidence_ids:
    - primary
    - fig2
  - name: pretreatment
    value: centrifuged and twice washed in PIPES
    definition: The owner accurately records washed biomass and unreported solid workup.
    evidence_ids:
    - primary
  - name: controls
    value: no-cell and no-nitrate solution comparators; no matching control-solid
      XRD
    definition: Two parallels per group are reported, without a phase-specific causal
      contrast.
    evidence_ids:
    - primary
    - fig2
    - fig3
    - si2
  details: Context values independently checked:100mL bottle capacity,10mMPIPES,nominal5%inoculum,30°C;8000g/4°C/8min
    cell centrifugation and two washes. These are source protocol descriptions, not
    a newly optimized procedure. The144h solution endpoint is not asserted as XRD
    collection time.
- assessment_id: phase
  area: evidence
  topic: Mixed diffraction assignment and causal interpretation
  outcome: supported
  summary: Provisional minor melanterite is a faithful source-assigned observation.
    Unreported workup permits residual sulfate crystallization; separate ferrous sulfate
    does not prove incorporation of Fe(II) into ferric phases.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - primary
  - si
  - si2
  - fig1
  - fig3
  dimensions:
  - name: evidence-tier
    value: partial phase assignment; causal limits explicit
    definition: No raw diffraction re-refinement, comparator solid pattern, processing
      control or isolated product was inspected or supplied.
    evidence_ids:
    - si2
    - primary
  - name: molecular-mechanism
    value: not established
    definition: Gene annotation tables support functional predictions only; no formation-specific
      expression, knockout or enzyme assay.
    evidence_ids:
    - si
    - primary
- assessment_id: quantity
  area: quantity
  topic: Measured and reported values, denominators and outcome
  outcome: supported
  summary: The record preserves reported concentrations and phase-label percentages
    without treating them as phase yield, purity or closed balance.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - primary
  - si2
  - fig2
  - fig3
  dimensions:
  - name: source-phase-values
    value: 13.35% melanterite;55.52% goethite;15.35% lepidocrocite;15.76% hematite
    definition: Source-reported pattern labels; phase-mass denominator, uncertainty,
      standard and refinement method unresolved.
    evidence_ids:
    - si2
  - name: concentration-endpoint
    value: Fe(II)3.64→0.84mmol/L within144h
    definition: Reported solution-system concentration change; no conversion into
      melanterite quantified.
    evidence_ids:
    - primary
    - fig2
  - name: deployment
    value: laboratory microcosm only
    definition: No isolated melanterite recovery, closed iron balance or industrial
      deployment. Separate Fe-NTA, nitrobenzene and arsenic arms are not imported.
    evidence_ids:
    - primary
    - fig4
    - fig5
    - si3
- assessment_id: history
  area: provenance
  topic: Actual curation events and reviewed-byte provenance
  outcome: supported
  summary: Separate inline EDIT and canonical EDIT describe the parent curator action
    accurately. Earlier CREATE provenance and historical review remain immutable.
  target_ids:
  - cmmmech:melanterite
  evidence_ids:
  - owner
  - history-new
  - history-old
  - prior
  - history-check
  - named
  - batch
  - require-records
  details: Native inspect captured the exact owner before assessment. Later inspection
    normalized target-kind/repository metadata and added context inputs, with the
    initial owner/history hashes unchanged. This is a fresh whole-record scientific
    review, not a provenance-only waiver.
findings: []
actions: []
limitations:
- HJ-2 species assignment remains conflicting across main article, comparator tree,
  GenBank and CCTCC. Blank catalog literature/sequence fields prevent experimental-aliquot
  linkage; catalog agreement with MZ701937.1 does not reconcile the article.
- Melanterite remains a provisional minor phase in mixed solids. No raw diffraction
  re-refinement, preparation history, matched control-solid patterns, uncertainty
  or absolute phase-mass basis establishes biological necessity, purity or isolated
  yield.
- Whole main publisher HTML, all5original main graphics, native DOCX tables/captions
  and3embedded original graphics were inspected. No claim of Word page rendering or
  inspection of a publisher PDF.
- Bounded current searches and metadata checks do not establish universal absence
  of corrections or contradictory literature. Public later HJ-2/genome metadata is
  not accepted as same-sample experimental proof.
- Review independence is from owner/history curation; this reviewer authored the preceding
  source-discovery handoff.
notes:
- Actual native-inspection start is retained across the usage interruption; finish
  is the current UTC assessment completion, not a historical filename timestamp.
- Review file state is working_tree against main2da10d95; uncommitted source/history
  provenance is preserved honestly. No record, history, commit or outbound mutation
  by the reviewer.
- Initial uv inspection encountered global-cache sandbox access; a subsequent successful
  inspection completed. All later native commands used the existing environment with
  a scratch uv cache and offline/no-sync settings.
- The first IMA fetch was slow; a current earlier same-day official PDF was rendered
  and checked while waiting. The independent fetch completed successfully with exactly
  identical bytes.
- Prior review contains no corrective findings, so this clean follow-up does not silently
  close a prior issue. Source issue340 remains partially advanced, not resolved.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261015T130653Z-melanterite-round95-independent
  relationship: New whole-target observation after narrowly scoped catalog-provenance
    curation; earlier phase/species limitations retained, deposit-access subgap advanced.
links:
- https://github.com/CultureBotAI/CMMMech/issues/340
```
