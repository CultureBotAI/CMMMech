# Independent scientific review of chromite ore processing residue

- Review: 20261014T045145Z-chromite-ore-processing-residue-round62-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T04:43:35.718857Z
- Finished UTC: 2026-10-14T04:51:45.342136Z
- Reviewer: codex /root/round61_zinc_sources (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The mixed chemical-processing residue and laboratory reductive stabilization by separately produced biogenic magnetite are supported. The record correctly separates microbial reagent synthesis from treatment of hyperalkaline waste, uses field-wet doses and fitted total-Cr speciation denominators, and preserves incomplete reduction and air-challenge rebound. No supported curation defect was found; conclusions remain limited to this sample and laboratory design.

## Scope And Provenance

Full field assessment of one newly maintained resource record, with fresh primary-source review of the exact claims and its actual CREATE provenance. No target-field sampling. Source sections about downstream product performance or separate groundwater arms are inspected only to police transfer of claims.

Selection: Assigned exact ID cmmmech:chromite-ore-processing-residue at maintained path data/records/chromite-ore-processing-residue.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 11a0b0f8e2714f1863304faf408da4ce0e7c5b53.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:chromite-ore-processing-residue | data/records/chromite-ore-processing-residue.yaml | maintained | Chromite ore processing residue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reviewer named-record validation | passed | True | cmmmech:chromite-ore-processing-residue | Executed by this reviewer: Checked 1 record(s); 0 failed. Actual command finished 2026-10-14T04:45:59.777640+00:00; exit 0. |
| Reviewer trusted-base append-only history validation | passed | True | cmmmech:chromite-ore-processing-residue | Executed by this reviewer: Checked 333 history record(s); 0 error(s). Actual command finished 2026-10-14T04:46:16.478231+00:00; exit 0. |
| Parent full batch checks | passed | True | cmmmech:chromite-ore-processing-residue | Parent executed this command, not the reviewer. Reviewer read actual receipt and retained log and verified its SHA-256. 317 tests passed, 3 skipped; 284 records and 333 histories valid; generated-page freshness passed. Actual interval 2026-10-14T04:44:05.207435+00:00 to 2026-10-14T04:50:52.392759+00:00; exit 0. |
| Parent nonempty corpus validation | passed | True | cmmmech:chromite-ore-processing-residue | Parent executed this command, not the reviewer. Reviewer read actual receipt and retained log and verified its SHA-256. 284 records checked; 0 failed. Actual interval 2026-10-14T04:50:52.393005+00:00 to 2026-10-14T04:51:09.920273+00:00; exit 0. |

## Scientific And Domain Assessments

### Secondary resource distinct from chromite mineral or beneficiation tailings

identity: supported. Targets: cmmmech:chromite-ore-processing-residue.

The borehole sample is a mixed high-lime chemical-processing waste, initially tentatively recognized and then characterized by XRF/XRD. Table4 Cr content is not a pure-mineral fraction or field-wet concentration. The broad owner is appropriately illustrated by this one waste source.

### Biogenic reagent synthesis versus treatment of waste

scope: supported. Targets: cmmmech:chromite-ore-processing-residue.

Microbial true is supported for the explicitly described production of reactive magnetite by G. sulfurreducens. It does not assert direct enzymatic reduction, viability or growth in pH12.5-12.9 COPR. Three washes aimed to remove cells; complete sterility was not demonstrated and is not claimed.

### Treatment design, controls and sample provenance

evidence: supported. Targets: cmmmech:chromite-ore-processing-residue.

The record preserves 25g field-moist COPR/50mL water,120mL bottles,N2,20C,100days,duplicate microcosms and wet-feed dose percentages. No-addition control and commercial nZVI comparator are distinct. Day50 XANES/XRD and later air challenge are correctly timed; separate groundwater comes from another site.

### Measured concentrations, fitted speciation and stabilization

quantity: supported. Targets: cmmmech:chromite-ore-processing-residue.

The BnM 5/10% arms yield aqueous Cr(VI) below1micromolar within1day and fitted day50 total-Cr Cr(VI) fractions of7%, against26% in control. The4-7% range belongs to nZVI, not wholly BnM. XANES proportions are fitted oxidation states, not recovered mass; Cr(III)-hydroxide-like spectra do not resolve a unique crystalline product.

### Contrary results, analytical disagreement and deployment limits

evidence: supported. Targets: cmmmech:chromite-ore-processing-residue.

The record retains7% extraction versus26% XANES initial Cr(VI), residual poorly accessible Cr(VI), dose dependence, all-BnM-arm rebound during air challenge, unresolved oxidation versus solubility causes, passivation and oxygen interference. Field injection and barriers remain proposals.

### No inherited criticality or unsupported identifiers

evidence: supported. Targets: cmmmech:chromite-ore-processing-residue.

No constituent-element criticality designation is assigned to this mixed waste. List/jurisdiction/edition claims are absent; no claim of not-listed status is made. External identifiers are limited to verified source identity and, where present, the correctly scoped organism species.

### New maintained owner and actual CREATE history

provenance: supported. Targets: cmmmech:chromite-ore-processing-residue.

Native input hashes match the frozen record, sidecar, schema and source pair. The record is new at the trusted base. Inline event and canonical sidecar identify actual curation rather than prior authorship; trusted-base history validation passed.

### Structural and final batch requirements

schema: supported. Targets: cmmmech:chromite-ore-processing-residue.

Reviewer named validation and trusted-base history checks passed, as did the parent final full-batch and separate nonempty corpus commands. Every target field was assessed within the source scope. These checks complement, but do not replace, the original-evidence assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/chromite-ore-processing-residue.yaml; All fields at the source.inputs target hash | supports | Read the complete maintained record and compared every claim to the primary methods/results and the schema. It is a new record at the trusted base. |
| history | history/records/chromite-ore-processing-residue/2026-10-14T043756Z-codex-1ad4c3.yaml; Actual CREATE session, target, actors, event and linked inline provenance | supports | Read the sidecar and inline event. The actor/model/tool and current creation timestamps identify this curation; they do not imply older authorship, completed external review or industrial implementation. |
| dossier | research/sources/round62-secondary/20261014T044043Z-source-investigation.md; Source assessment plus full paired JSON acquisition/curation manifest | supports | Read the dossier and parsed the manifest, including query/acquisition scope and deferred leads. Independently checked every listed artifact hash and the report hash. The source dossier guided retrieval; it did not substitute for original-figure assessment. |
| metadata | https://doi.org/10.1016/j.apgeochem.2014.12.001; Primary title/author page and same-day retained Crossref metadata | supports | DOI, authors, title and publication year match the original. Crossref contains no update-to entry and an empty relation object. The issuing metadata are retained in the raw source inventory; publication dates are distinguished from file/download dates. |
| search | /private/tmp/cmm-round62-resource-reviews/notice-search.json; Independent exact-DOI correction/retraction/erratum search | context_only | No affecting notice was identified in the returned sets. Source-internal negative/limiting results were separately examined. Other-source search hits were not used as uninspected experimental proof. |
| dedup | /private/tmp/cmm-round62-resource-reviews/bounded-record-dedup.txt; Bounded current-corpus material/DOI search | context_only | Hidden/ignored-inclusive, symlink-following current record search returned the two new owners and incidental lexical matches. The dossier separately records wider prior-research/raw-root coverage and missing or timed-out extractions; this review makes no machine-wide absence claim. |
| local_checks | /private/tmp/cmm-round62-resource-reviews/checks.json; Reviewer-executed named validations and trusted-base history command | supports | Both named records validated with 1 checked/0 failed each; trusted-base history validated 333 records with 0 errors. These are structural checks, not a substitute for scientific assessment. |
| batch_checks | /private/tmp/cmm-round62-final-gates.json; Parent-executed final command receipt and log | supports | Read the actual full-batch receipt and short log, verified every command exit 0 and rehashed the log. The completed review does not rely on the earlier prechange baseline. Full run: just render; just check; separate require-records; trusted-base history. Log SHA-256 a94cb9fef74e0ca15a967cea93f42b5809488135e8e614a46d2f9826506895a4. |
| watts_primary | https://strathprints.strath.ac.uk/56145/1/Watts_etal_AG_2015_Biogenic_nano_magnetite_and_nano_zero_valent_iron_treatment.pdf; Original PDF pages 2-13; methods 2.1-2.9, results 3.1-3.7, discussion 4-5; all Figures 1-9 and Tables 1-4 | supports | Personally viewed original page renders and read relevant body text. Methods separate G. sulfurreducens ferrihydrite reduction and three washes from field-moist COPR treatment. Figure 7 supports aqueous Cr(VI) suppression, Figure 8 labels 26:74 control versus 7:93 at both 5/10% BnM, Figure 6 lacks a unique new Cr(III) phase, and Figure 9 shows rebound on air exposure. The 7% alkaline-extraction estimate and 26% XANES fit are different assays. Separate groundwater figures demonstrate passivation and oxygen inhibition, not direct COPR recovery. |
| watts_si | https://ars.els-cdn.com/content/image/1-s2.0-S088329271400300X-mmc1.docx; Original DOCX document XML and both embedded TIFF images, viewed through faithful PNG renders | supports | Personally inspected SI1 reagent diffraction (BnM magnetite; nZVI Fe metal plus magnetite) and SI2 pseudo-first-order fits for separate model chromate/groundwater arms. DOCX title/authors and embedded-media hashes match the retained publisher file. Neither figure supplies a new COPR recovery yield. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=35554&amp;mode=Info; Fresh issuing browser: taxon ID, current name and rank | supports | Live authority resolves NCBITaxon:35554 to Geobacter sulfurreducens, rank species. Type-strain information does not prove the unspecified experimental strain. The record correctly avoids inventing a strain accession. |
| article_ids | https://pmc.ncbi.nlm.nih.gov/articles/PMC4461148/; Retained same-day primary PMC HTML metadata and header | supports | The inspected same-day PMC HTML links PMID26109747, PMCIDPMC4461148 and the exact DOI/title. Reviewer live PubMed returned no body and PMC returned a challenge; no successful fresh live full-text acquisition is claimed. |

## Limits And Additional Notes

- Evidence describes a single characterized COPR source and duplicate laboratory microcosms; extrapolation across waste origins, field dosing or long-term performance is unsupported.
- The supplied primary does not identify a strain accession or demonstrate complete cell removal; biological scope is upstream reagent production.
- Residual Cr(VI), extraction/XANES disagreement and air-challenge rebound remain scientific limitations; they are already represented and not hidden curation defects.
- All relevant primary figures/tables and the original SI were inspected, but raw beamline data, a full reference-chain investigation and independent experimental replication were not available.
- Live PubMed/PMC retrieval was empty/challenged. Same-day retained primary metadata were independently read; the NCBI taxon browser resolved live.
- This new record does not exist at the trusted base; the reviewed state is an uncommitted working-tree attestation, not a claim that these bytes were already committed. Native inspect captured input hashes before scientific assessment.
- No criticality designation is asserted, so omission is not interpreted as a not-listed determination.
- Raw source integrity was checked against the dossier: all 52 listed artifacts matched their recorded SHA-256. Raw full text and renders remain outside Git.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T045145Z-chromite-ore-processing-residue-round62-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of chromite ore processing residue
started_at: '2026-10-14T04:43:35.718857Z'
finished_at: '2026-10-14T04:51:45.342136Z'
reviewer:
  identity: codex /root/round61_zinc_sources
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from /root/round61_fluorite_sources, who acquired
    the source dossier and authored this record. This reviewer did not edit this record,
    its history or dossier. Original retained PDFs, relevant figures/tables and metadata
    were independently inspected; unrelated uranium-vanadate curation by this reviewer
    is outside this target. Parent-executed final batch gates are attributed separately.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The mixed chemical-processing residue and laboratory reductive stabilization
  by separately produced biogenic magnetite are supported. The record correctly separates
  microbial reagent synthesis from treatment of hyperalkaline waste, uses field-wet
  doses and fitted total-Cr speciation denominators, and preserves incomplete reduction
  and air-challenge rebound. No supported curation defect was found; conclusions remain
  limited to this sample and laboratory design.
source:
  git_revision: 11a0b0f8e2714f1863304faf408da4ce0e7c5b53
  state: working_tree
  inputs:
  - path: data/records/chromite-ore-processing-residue.yaml
    sha256: 914ccebc64d0bf486808683d35531b9279b109ebe9eb4b1998b90cc6873571ad
    role: target
  - path: history/records/chromite-ore-processing-residue/2026-10-14T043756Z-codex-1ad4c3.yaml
    sha256: a33209932c1f6cfa391abcdf7e5edf480c42d716f7d5b235834c6df12be9a1b2
    role: context
  - path: research/sources/round62-secondary/20261014T044043Z-source-investigation.json
    sha256: bbb1ed8c39ed442901b73d91e36bed806e150984e7863eb490d876ca19550f34
    role: context
  - path: research/sources/round62-secondary/20261014T044043Z-source-investigation.md
    sha256: 4d0ef2e47e4897c0972f6ca58b64f7770859e19afd3958c7d0191f4c846944b7
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full field assessment of one newly maintained resource record, with
    fresh primary-source review of the exact claims and its actual CREATE provenance.
    No target-field sampling. Source sections about downstream product performance
    or separate groundwater arms are inspected only to police transfer of claims.
  selection: Assigned exact ID cmmmech:chromite-ore-processing-residue at maintained
    path data/records/chromite-ore-processing-residue.yaml.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:chromite-ore-processing-residue
  exclusions:
  - target: New curation, external issue posting and publication
    reason: Assigned scope is independent local review; maintained record and history
      remain unchanged by reviewer.
  - target: Uncurated downstream product performance or new experiments beyond the
      named study
    reason: Not required to assess the current waste-transformation/recovery claims
      and not silently promoted into this record.
targets:
- target_id: cmmmech:chromite-ore-processing-residue
  path: data/records/chromite-ore-processing-residue.yaml
  label: Chromite ore processing residue
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/chromite-ore-processing-residue.yaml
    role: maintained
checks:
- check_id: named
  name: Reviewer named-record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/chromite-ore-processing-residue.yaml
  status: passed
  required: true
  summary: 'Executed by this reviewer: Checked 1 record(s); 0 failed. Actual command
    finished 2026-10-14T04:45:59.777640+00:00; exit 0.'
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - local_checks
- check_id: history
  name: Reviewer trusted-base append-only history validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate-history --base 11a0b0f8e2714f1863304faf408da4ce0e7c5b53
  status: passed
  required: true
  summary: 'Executed by this reviewer: Checked 333 history record(s); 0 error(s).
    Actual command finished 2026-10-14T04:46:16.478231+00:00; exit 0.'
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - local_checks
- check_id: batch
  name: Parent full batch checks
  command: just check
  status: passed
  required: true
  summary: Parent executed this command, not the reviewer. Reviewer read actual receipt
    and retained log and verified its SHA-256. 317 tests passed, 3 skipped; 284 records
    and 333 histories valid; generated-page freshness passed. Actual interval 2026-10-14T04:44:05.207435+00:00
    to 2026-10-14T04:50:52.392759+00:00; exit 0.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_checks
- check_id: nonempty
  name: Parent nonempty corpus validation
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Parent executed this command, not the reviewer. Reviewer read actual receipt
    and retained log and verified its SHA-256. 284 records checked; 0 failed. Actual
    interval 2026-10-14T04:50:52.393005+00:00 to 2026-10-14T04:51:09.920273+00:00;
    exit 0.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_checks
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/chromite-ore-processing-residue.yaml
  locator: All fields at the source.inputs target hash
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Read the complete maintained record and compared every claim to the primary
    methods/results and the schema. It is a new record at the trusted base.
  snapshot_sha256: 914ccebc64d0bf486808683d35531b9279b109ebe9eb4b1998b90cc6873571ad
- evidence_id: history
  kind: record_content
  reference: history/records/chromite-ore-processing-residue/2026-10-14T043756Z-codex-1ad4c3.yaml
  locator: Actual CREATE session, target, actors, event and linked inline provenance
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Read the sidecar and inline event. The actor/model/tool and current creation
    timestamps identify this curation; they do not imply older authorship, completed
    external review or industrial implementation.
  snapshot_sha256: a33209932c1f6cfa391abcdf7e5edf480c42d716f7d5b235834c6df12be9a1b2
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round62-secondary/20261014T044043Z-source-investigation.md
  locator: Source assessment plus full paired JSON acquisition/curation manifest
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Read the dossier and parsed the manifest, including query/acquisition scope
    and deferred leads. Independently checked every listed artifact hash and the report
    hash. The source dossier guided retrieval; it did not substitute for original-figure
    assessment.
  snapshot_sha256: 4d0ef2e47e4897c0972f6ca58b64f7770859e19afd3958c7d0191f4c846944b7
- evidence_id: metadata
  kind: database
  reference: https://doi.org/10.1016/j.apgeochem.2014.12.001
  locator: Primary title/author page and same-day retained Crossref metadata
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: DOI, authors, title and publication year match the original. Crossref contains
    no update-to entry and an empty relation object. The issuing metadata are retained
    in the raw source inventory; publication dates are distinguished from file/download
    dates.
  snapshot_sha256: e94b3bd5d65ffaa280186c690b405836fb7ff1448e16ec67b9fb09d753a71278
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round62-resource-reviews/notice-search.json
  locator: Independent exact-DOI correction/retraction/erratum search
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: context_only
  summary: No affecting notice was identified in the returned sets. Source-internal
    negative/limiting results were separately examined. Other-source search hits were
    not used as uninspected experimental proof.
  snapshot_sha256: 52ed56b3a6b7ee3995203cc45dc226e7f3ec53e94eee0e63a4013be784bbcfee
  search_scope: 'web.run exact queries: "10.1016/j.apgeochem.2014.12.001" correction
    retraction erratum; "10.1155/2015/241421" correction retraction erratum. Initial
    contrary-context queries: "chromite ore processing residue" "magnetite" "reoxidation";
    "Recovery of Cerium Dioxide from Spent Glass-Polishing" yield control. First returned
    sets, no pagination or domain/date filters; not an exhaustive registry or citation-chain
    clearance.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round62-resource-reviews/bounded-record-dedup.txt
  locator: Bounded current-corpus material/DOI search
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: context_only
  summary: Hidden/ignored-inclusive, symlink-following current record search returned
    the two new owners and incidental lexical matches. The dossier separately records
    wider prior-research/raw-root coverage and missing or timed-out extractions; this
    review makes no machine-wide absence claim.
  snapshot_sha256: bbacf69c2d967b188078f2886733d7cd8687e0577b2e55fa1a27a7d696994f7f
  search_scope: rg --no-ignore --hidden --follow -n -i over data/records/*.yaml for
    chromite ore processing residue, COPR, spent/polishing slurry variants and the
    two exact DOIs; no ignore-dependent absence claim.
- evidence_id: local_checks
  kind: validation
  reference: /private/tmp/cmm-round62-resource-reviews/checks.json
  locator: Reviewer-executed named validations and trusted-base history command
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Both named records validated with 1 checked/0 failed each; trusted-base
    history validated 333 records with 0 errors. These are structural checks, not
    a substitute for scientific assessment.
  snapshot_sha256: 55fde7c203fde0dcad83e1a381124636acc3aeaf44f5f3221a2639fb048d88ee
- evidence_id: batch_checks
  kind: validation
  reference: /private/tmp/cmm-round62-final-gates.json
  locator: Parent-executed final command receipt and log
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: 'Read the actual full-batch receipt and short log, verified every command
    exit 0 and rehashed the log. The completed review does not rely on the earlier
    prechange baseline. Full run: just render; just check; separate require-records;
    trusted-base history. Log SHA-256 a94cb9fef74e0ca15a967cea93f42b5809488135e8e614a46d2f9826506895a4.'
  snapshot_sha256: b26f9636cadb474165ded2df1ca1ccd65dfbf1876a9cf46f08df4a228b8e50fa
- evidence_id: watts_primary
  kind: primary_source
  reference: https://strathprints.strath.ac.uk/56145/1/Watts_etal_AG_2015_Biogenic_nano_magnetite_and_nano_zero_valent_iron_treatment.pdf
  locator: Original PDF pages 2-13; methods 2.1-2.9, results 3.1-3.7, discussion 4-5;
    all Figures 1-9 and Tables 1-4
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Personally viewed original page renders and read relevant body text. Methods
    separate G. sulfurreducens ferrihydrite reduction and three washes from field-moist
    COPR treatment. Figure 7 supports aqueous Cr(VI) suppression, Figure 8 labels
    26:74 control versus 7:93 at both 5/10% BnM, Figure 6 lacks a unique new Cr(III)
    phase, and Figure 9 shows rebound on air exposure. The 7% alkaline-extraction
    estimate and 26% XANES fit are different assays. Separate groundwater figures
    demonstrate passivation and oxygen inhibition, not direct COPR recovery.
  snapshot_sha256: 3911ef2ef9013ac4af29895e62113d314e4f5ceace6caa3c3b1d61dcff9ac977
- evidence_id: watts_si
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S088329271400300X-mmc1.docx
  locator: Original DOCX document XML and both embedded TIFF images, viewed through
    faithful PNG renders
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Personally inspected SI1 reagent diffraction (BnM magnetite; nZVI Fe metal
    plus magnetite) and SI2 pseudo-first-order fits for separate model chromate/groundwater
    arms. DOCX title/authors and embedded-media hashes match the retained publisher
    file. Neither figure supplies a new COPR recovery yield.
  snapshot_sha256: d04f569069ca4af5ae879e30833893dc3ca3bea8596c4bbf8ea9b247c422ac9b
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=35554&mode=Info
  locator: 'Fresh issuing browser: taxon ID, current name and rank'
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: Live authority resolves NCBITaxon:35554 to Geobacter sulfurreducens, rank
    species. Type-strain information does not prove the unspecified experimental strain.
    The record correctly avoids inventing a strain accession.
  snapshot_sha256: b1d0f8d3cc8e9a1f559799f6769567001ea8a525e3be4e788f038b3c07bbc40b
- evidence_id: article_ids
  kind: database
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4461148/
  locator: Retained same-day primary PMC HTML metadata and header
  accessed_at: '2026-10-14T04:51:45.302916Z'
  support: supports
  summary: The inspected same-day PMC HTML links PMID26109747, PMCIDPMC4461148 and
    the exact DOI/title. Reviewer live PubMed returned no body and PMC returned a
    challenge; no successful fresh live full-text acquisition is claimed.
  snapshot_sha256: 6c654c46be5414a73849f8c56f020a335b0e3eb4e1e6b044d024d9e84fab6b6d
assessments:
- assessment_id: identity
  area: identity
  topic: Secondary resource distinct from chromite mineral or beneficiation tailings
  outcome: supported
  summary: The borehole sample is a mixed high-lime chemical-processing waste, initially
    tentatively recognized and then characterized by XRF/XRD. Table4 Cr content is
    not a pure-mineral fraction or field-wet concentration. The broad owner is appropriately
    illustrated by this one waste source.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - record
  - watts_primary
  dimensions:
  - name: material_form
    value: secondary_resource; field-moist mixed chemical-processing residue
    definition: The maintained owner is the waste, not its constituent chromium or
      a pure mineral.
    evidence_ids:
    - record
    - watts_primary
- assessment_id: microbial_scope
  area: scope
  topic: Biogenic reagent synthesis versus treatment of waste
  outcome: supported
  summary: Microbial true is supported for the explicitly described production of
    reactive magnetite by G. sulfurreducens. It does not assert direct enzymatic reduction,
    viability or growth in pH12.5-12.9 COPR. Three washes aimed to remove cells; complete
    sterility was not demonstrated and is not claimed.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - watts_primary
  - watts_si
  - taxonomy
  dimensions:
  - name: organism
    value: Geobacter sulfurreducens; NCBITaxon:35554; species rank
    definition: The publication supplies the species, not a strain accession.
    evidence_ids:
    - watts_primary
    - watts_si
    - taxonomy
  - name: biomass_state
    value: Living culture used to produce magnetite separately; washed reagent applied
      to waste
    definition: Microbial contribution concerns upstream reagent production; reagent
      application has no proven living-cell contribution.
    evidence_ids:
    - watts_primary
    - watts_si
    - taxonomy
- assessment_id: conditions
  area: evidence
  topic: Treatment design, controls and sample provenance
  outcome: supported
  summary: The record preserves 25g field-moist COPR/50mL water,120mL bottles,N2,20C,100days,duplicate
    microcosms and wet-feed dose percentages. No-addition control and commercial nZVI
    comparator are distinct. Day50 XANES/XRD and later air challenge are correctly
    timed; separate groundwater comes from another site.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - watts_primary
  dimensions:
  - name: dose_basis
    value: 0-10% BnM by mass of field-wet COPR
    definition: These are wet-feed reagent doses, not dry-solid mass percentages.
    evidence_ids:
    - watts_primary
  - name: controls
    value: Unamended COPR and separate synthetic NANOFER25S comparator
    definition: No matched viable/killed-cell control establishes a direct microbial
      action in the waste.
    evidence_ids:
    - watts_primary
- assessment_id: outcome
  area: quantity
  topic: Measured concentrations, fitted speciation and stabilization
  outcome: supported
  summary: The BnM 5/10% arms yield aqueous Cr(VI) below1micromolar within1day and
    fitted day50 total-Cr Cr(VI) fractions of7%, against26% in control. The4-7% range
    belongs to nZVI, not wholly BnM. XANES proportions are fitted oxidation states,
    not recovered mass; Cr(III)-hydroxide-like spectra do not resolve a unique crystalline
    product.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - watts_primary
  dimensions:
  - name: outcome
    value: Reduction and solid-system stabilization; no isolated chromium product
    definition: Aqueous suppression plus fitted solid speciation support transformation,
      not commercial recovery.
    evidence_ids:
    - watts_primary
  - name: measurement_basis
    value: XANES percent of total Cr; DPC aqueous Cr(VI) detection limit1micromolar
    definition: Distinct denominators and analytical methods are preserved.
    evidence_ids:
    - watts_primary
- assessment_id: limits
  area: evidence
  topic: Contrary results, analytical disagreement and deployment limits
  outcome: supported
  summary: The record retains7% extraction versus26% XANES initial Cr(VI), residual
    poorly accessible Cr(VI), dose dependence, all-BnM-arm rebound during air challenge,
    unresolved oxidation versus solubility causes, passivation and oxygen interference.
    Field injection and barriers remain proposals.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - watts_primary
  - watts_si
  dimensions:
  - name: deployment
    value: Laboratory; industrial waste origin only
    definition: No field deployment or indefinite detoxification is demonstrated.
    evidence_ids:
    - watts_primary
    - watts_si
- assessment_id: criticality
  area: evidence
  topic: No inherited criticality or unsupported identifiers
  outcome: supported
  summary: No constituent-element criticality designation is assigned to this mixed
    waste. List/jurisdiction/edition claims are absent; no claim of not-listed status
    is made. External identifiers are limited to verified source identity and, where
    present, the correctly scoped organism species.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - record
  - metadata
  dimensions:
  - name: criticality
    value: unrecorded
    definition: No jurisdiction/list/edition assertion; this is not a negative membership
      determination.
    evidence_ids:
    - record
- assessment_id: provenance
  area: provenance
  topic: New maintained owner and actual CREATE history
  outcome: supported
  summary: Native input hashes match the frozen record, sidecar, schema and source
    pair. The record is new at the trusted base. Inline event and canonical sidecar
    identify actual curation rather than prior authorship; trusted-base history validation
    passed.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - record
  - history
  - local_checks
  - dossier
- assessment_id: validation
  area: schema
  topic: Structural and final batch requirements
  outcome: supported
  summary: Reviewer named validation and trusted-base history checks passed, as did
    the parent final full-batch and separate nonempty corpus commands. Every target
    field was assessed within the source scope. These checks complement, but do not
    replace, the original-evidence assessment.
  target_ids:
  - cmmmech:chromite-ore-processing-residue
  evidence_ids:
  - local_checks
  - batch_checks
findings: []
actions: []
limitations:
- Evidence describes a single characterized COPR source and duplicate laboratory microcosms;
  extrapolation across waste origins, field dosing or long-term performance is unsupported.
- The supplied primary does not identify a strain accession or demonstrate complete
  cell removal; biological scope is upstream reagent production.
- Residual Cr(VI), extraction/XANES disagreement and air-challenge rebound remain
  scientific limitations; they are already represented and not hidden curation defects.
- All relevant primary figures/tables and the original SI were inspected, but raw
  beamline data, a full reference-chain investigation and independent experimental
  replication were not available.
- Live PubMed/PMC retrieval was empty/challenged. Same-day retained primary metadata
  were independently read; the NCBI taxon browser resolved live.
notes:
- This new record does not exist at the trusted base; the reviewed state is an uncommitted
  working-tree attestation, not a claim that these bytes were already committed. Native
  inspect captured input hashes before scientific assessment.
- No criticality designation is asserted, so omission is not interpreted as a not-listed
  determination.
- 'Raw source integrity was checked against the dossier: all 52 listed artifacts matched
  their recorded SHA-256. Raw full text and renders remain outside Git.'
```
