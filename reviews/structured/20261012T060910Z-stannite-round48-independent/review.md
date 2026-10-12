# Independent scientific review of stannite identity and historical bioleaching

- Review: 20261012T060910Z-stannite-round48-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T06:03:52Z
- Finished UTC: 2026-10-12T06:09:10Z
- Reviewer: Codex /root/round27_packaging (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The mineral owner, qualified natural evidence and historical laboratory assay are supported with explicit specimen, control, pH, phase-confidence and concentration-scale limitations. No corrective finding.

## Scope And Provenance

Whole new stannite record, canonical CREATE, paired source dossier and schema. Complete Teh1979 and Černý2001 originals and current authority; shared Haase2022 original and SI inventory checked as natural-context support for stannite, not assigned as new kesterite evidence.

Selection: Parent-assigned independent review of another curator’s frozen record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9b397b1f215381208c3381b175b3da8b6fe31399.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:stannite | data/records/stannite.yaml | maintained | Stannite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:stannite | Reviewer executed in explicit round48 cwd with offline cache and no bytecode:Checked2records;0failed. Raw log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042 |
| Completed cohort batch | passed | True | cmmmech:stannite | Parent-executed; independently read and raw-byte hash-verified 41150421ddd753d0cecf6d7a22bebd5a34d52f11b309beb820523a57d1624039. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 175.55s (0:02:55)<br>Checked 236 record(s); 0 failed.<br>Checked 279 history record(s); 0 error(s). |
| Completed cohort nonempty | passed | True | cmmmech:stannite | Parent-executed; independently read and raw-byte hash-verified ed2bc5cf4c32744127edd92734e33277402fc4a6990da56ff6c309c0c4e7673e. Checked 236 record(s); 0 failed. |
| Completed cohort history | passed | True | cmmmech:stannite | Parent-executed; independently read and raw-byte hash-verified 885e537286de29f10eb43fd520a420768782950c80808f190df3c2dd01832122. Checked 279 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Species, specimen and material boundaries

identity: supported. Targets: cmmmech:stannite.

Mineral species and natural Fe/Zn-bearing solid solutions remain distinct from elemental/commodity tin, synthetic endmembers, device films and polymorphic ferrokësterite. Composition-only names are not overrepresented as solved structures.

### Historical strain and biomass state

identity: supported. Targets: cmmmech:stannite.

Growing iron-oxidizing culture is identified at historical species level; current taxon ID is a species-name mapping and does not supply missing accession or inoculum.

### Conditions, controls and causality

evidence: supported. Targets: cmmmech:stannite.

The experiment supports source-attributed soluble-tin observations in inoculated assays. Direct versus indirect action, specific tin redox pathway and causal microbial advantage for unmatched materials remain unresolved. pH, loading and missing comparator limits are accurately retained.

### Percentages, denominator and product scope

evidence: supported. Targets: cmmmech:stannite.

Reported extraction percentages remain attributed to their exact natural/synthetic material. Incoherent graph concentration units are not converted; no closed balance, isolated product, purity or industrial deployment is inferred.

### Criticality and deployment

scope: supported. Targets: cmmmech:stannite.

No jurisdictional criticality claim is made. Element-list membership is not inherited by a mineral species. Laboratory dissolution and natural weathering are not industrial recovery.

### Exact state and completed checks

provenance: supported. Targets: cmmmech:stannite.

Native inspect captured record, CREATE history, both dossier files and schema before judgment; all hashes remain unchanged.94 source artifacts, named validation and actual parent gates independently verified.

### Natural specimen diffraction and weathering

evidence: supported. Targets: cmmmech:stannite.

Selected SAED identifications support the stated natural stannite context, with no blanket identification of all solid solutions or microbial attribution to mine-waste weathering.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/stannite.yaml; Whole frozen record | supports | All claims were checked against the precise material, culture, assay, source limitations and authority scope. No inherited criticality or product-recovery claim. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 definitions and distribution terms, original pages 1–2; species rows 71,112,204 | supports | Current IMA distinguishes stannite Cu2FeSnS4 from ferrokësterite with the same ideal formula, and kësterite Cu2ZnSnS4. Grandfathered years 1832/1956 are not approval identifiers. Current spelling and identity do not independently authenticate every historical specimen. |
| natural | https://www.jgeosci.org/content/JCGS2001_1-2__cerny2.pdf; Entire seven-page scanned original, printed 27–33, all Figures 1–4 and Tables 1–3 personally inspected; page 29 naming limitation | supports | Four natural Peerless nodules include Fe-dominant PPK-1/4 and Zn-dominant PPK-2/3. EMP chemistry and powder unit cells are supported. The authors explicitly assign names by composition without refined cation ordering or space-group determinations; the record retains that boundary. Publisher indexing 27–34 conflicts with the actual original ending 33. |
| leaching | https://gsm.org.my/wp-content/uploads/gsm_file_2/702001-101558-PDF.pdf; Complete Teh1979 article, issue PDF pages 3–9 / printed 85–91, all three original figures personally inspected | supports | Pure historical Thiobacillus ferrooxidans from Ranstad was maintained in 9K medium. Synthetic feeds were made in sealed evacuated silica tubes and reportedly XRD checked, without patterns or quantitative purity. Natural stannite is a separate Hock Leong Mine, Ampang specimen. Figure 1 follows 35 days,32 C,0.5% pulp and particles below0.16mm; initial pH1.5 in Results conflicts with pH2.5 in Figures1–2. Reported 0.1% optimum is a different claim. AAS tin and colorimetric confirmation support soluble tin observation, not isolated product. |
| controls | https://gsm.org.my/wp-content/uploads/gsm_file_2/702001-101558-PDF.pdf; Printed85–87 and Figure1 on89, bacterial and separate organic-acid assays | supports | Reported percentages are 54.45 synthetic stannite,31.30 natural stannite and72.66 synthetic kesterite. Only synthetic stannite has a plotted sterile comparator. No matched sterile kesterite or natural-stannite arm is shown. The printed x1000ppm graph axis is inconsistent with available loading information; neither record digitizes it. Inoculum, assay volume, aeration, replicate/error information and actual ferrous dose are missing. Different autoclaved organic-acid tests do not demonstrate biogenic leachant production or a matched bacterial advantage. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&amp;mode=Info; Official species page and historical homotypic synonym | supports | NCBITaxon920 maps Acidithiobacillus ferrooxidans and Thiobacillus ferrooxidans at species scope. No stock accession, sequenced isolate or molecular authentication of the historical Ranstad strain is inferred. |
| weathering | https://doi.org/10.5194/ejm-34-493-2022; Complete original14pages, all Figures1–8 and Tables1–4 personally inspected; Figures6b and8b | supports | Selected natural grains from Kaňk and Giftkies have SAED patterns identified as stannite. Other grains and compositional series are not all independently structure-refined. Weathering/diffusion versus dissolution-reprecipitation interpretations do not demonstrate microbial activity, controlled extraction or recovery. The historical ferrokësterite formula in Table1 is not adopted as current nomenclature. |
| supplement | https://ejm.copernicus.org/articles/34/493/2022/ejm-34-493-2022-supplement.zip; Original title page and Tables S1–S3 XLSX; six sheet XMLs independently parsed, headers plus first/last rows read | supports | The original supplement supplies element-mass and oxide-mass tables for the two localities, including Ag2O header in S3. Reviewer inventoried all six sheets and sampled their rows; no claim to analytically revalidate every cell. No supplemental numerical cell is imported into the record; other underlying data remain on request. |
| dossier | research/sources/round48-sn-minerals/20261012T060237Z-source-investigation.json; Complete paired dossier and all94 raw-artifact hashes | supports | All94 artifact hashes and the Markdown hash match. Full acquired1979,2001,2022 originals are separated from unavailable1981/Hall/Moore originals. Shared historical extraction percentages make1981 an overlap lead, not demonstrated independent replication. |
| history | history/records/stannite/2026-10-12T060009Z-codex-9ad869.yaml; Complete canonical CREATE sidecar plus distinct inline event | supports | Actual codex/GPT-6/codex provenance, new record target, timestamps and curation scope are coherent. Reviewer authored none of this record, its history or dossier. |
| dedup | /private/tmp/cmm-round48-sn-independent/dedup-receipt.json; Independent bounded current/original scientific text and referenced raw roots | supports | The two new owners are distinct from elemental tin, mixed resources, synthetic device materials and prior study mentions. Within this bounded search, no earlier accepted duplicate owner or duplicate curated1979 assay was identified; prior source leads are explicitly retained. |
| notices | /private/tmp/cmm-round48-sn-independent/web-notices.json; Three live exact-title/DOI notice queries | supports | No affecting correction or retraction was identified in the returned query sets. Publisher metadata corroborates the2001 indexing discrepancy. Secondary search hits are discovery context only, not authority or substitutes for original graphics. |
| gates | /private/tmp/cmm-round48-final-terminal.json; Actual completed cohort terminal receipt and each raw command log | supports | Parent-executed final gates independently read and byte-hash verified:308passed3skipped175.55s,236records,279histories; separate nonempty/history checks passed. Validation does not prove scientific truth. |

## Limits And Additional Notes

- Historical assay strain lacks an accession and modern molecular confirmation; no inoculum, assay volume, aeration, replication or error model is supplied.
- Initial pH1.5 prose conflicts with pH2.5 figure captions; graph x1000ppm scale cannot be reconciled confidently with pulp density. Reported extraction percentages are not validated closed balances.
- Synthetic-stannite sterile comparator is not a matched control for natural stannite or synthetic kesterite. Acid/iron chemistry and microbial effects are incompletely separated.
- Composition-based Peerless nomenclature does not determine cation ordering/space group; historical synthetic XRD patterns and phase-purity data are not published.
- No inherited criticality, isolated tin product, product purity or industrial recovery is demonstrated.
- Review uses independently read same-session official source bytes and verified acquisition receipts; every authority PDF was not separately redownloaded. Notice and dedup searches are bounded.
- Both tin records were assessed together from common originals and have separate native observations with their own exact target/history input hashes. The initial system-Python orchestration failed on missing yaml before native inspect; it was rerun using the existing project environment. No saved scientific review or curated record was altered.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T060910Z-stannite-round48-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of stannite identity and historical bioleaching
started_at: '2026-10-12T06:03:52Z'
finished_at: '2026-10-12T06:09:10Z'
reviewer:
  identity: Codex /root/round27_packaging
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record, CREATE history and shared source dossier authored by
    /root/round43_hardmetal. Reviewer authored a separate rutile record only; independently
    captured target inputs before judging, read all relevant original primary graphics
    and authority evidence, inventoried the shared supplement, and ran named validation.
    No self-certification of rutile.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The mineral owner, qualified natural evidence and historical laboratory assay
  are supported with explicit specimen, control, pH, phase-confidence and concentration-scale
  limitations. No corrective finding.
source:
  git_revision: 9b397b1f215381208c3381b175b3da8b6fe31399
  state: working_tree
  inputs:
  - path: data/records/stannite.yaml
    sha256: 8490730a9c745a6016f4f6fbeb5b27c6b62ba62c1c53b51e9919d21e6740eec0
    role: target
  - path: history/records/stannite/2026-10-12T060009Z-codex-9ad869.yaml
    sha256: 4d801149d5e841a454b5f156f401831e3698f3b824ca3fb9b9ce59424eb03951
    role: context
  - path: research/sources/round48-sn-minerals/20261012T060237Z-source-investigation.json
    sha256: 7190856a6e1afdbfc059dc14e1eb50a369a59946d83d3d0399b26a89d21972b0
    role: context
  - path: research/sources/round48-sn-minerals/20261012T060237Z-source-investigation.md
    sha256: 3f802754831c4f959101265f81f75469e68b4891fd7dcfce7a0f2ab0891583a2
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:stannite
  path: data/records/stannite.yaml
  label: Stannite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/stannite.yaml
    role: scientific_record
scope:
  description: Whole new stannite record, canonical CREATE, paired source dossier
    and schema. Complete Teh1979 and Černý2001 originals and current authority; shared
    Haase2022 original and SI inventory checked as natural-context support for stannite,
    not assigned as new kesterite evidence.
  selection: Parent-assigned independent review of another curator’s frozen record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:stannite
  exclusions:
  - target: Unavailable1981 followup, Hall and Moore originals; non-target pages of
      the1979 issue
    reason: Not accepted as additional primary experiments. No full inspection, notice
      completeness or independent replication claimed.
  - target: Every numerical supplemental cell and unpublished data on request
    reason: Six-sheet inventory and sampled-row check only; no supplemental measurement
      imported by these records.
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/stannite.yaml data/records/kesterite.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:stannite
  summary: Reviewer executed in explicit round48 cwd with offline cache and no bytecode:Checked2records;0failed.
    Raw log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
- check_id: batch
  name: Completed cohort batch
  command: just check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:stannite
  summary: 'Parent-executed; independently read and raw-byte hash-verified 41150421ddd753d0cecf6d7a22bebd5a34d52f11b309beb820523a57d1624039.
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 175.55s (0:02:55)

    Checked 236 record(s); 0 failed.

    Checked 279 history record(s); 0 error(s).'
- check_id: nonempty
  name: Completed cohort nonempty
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:stannite
  summary: Parent-executed; independently read and raw-byte hash-verified ed2bc5cf4c32744127edd92734e33277402fc4a6990da56ff6c309c0c4e7673e.
    Checked 236 record(s); 0 failed.
- check_id: history
  name: Completed cohort history
  command: uv run --locked cmmmech validate-history --base 9b397b1f215381208c3381b175b3da8b6fe31399
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - cmmmech:stannite
  summary: Parent-executed; independently read and raw-byte hash-verified 885e537286de29f10eb43fd520a420768782950c80808f190df3c2dd01832122.
    Checked 279 history record(s); 0 error(s).
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/stannite.yaml
  locator: Whole frozen record
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: All claims were checked against the precise material, culture, assay, source
    limitations and authority scope. No inherited criticality or product-recovery
    claim.
  snapshot_sha256: 8490730a9c745a6016f4f6fbeb5b27c6b62ba62c1c53b51e9919d21e6740eec0
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 definitions and distribution terms, original pages 1–2;
    species rows 71,112,204
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Current IMA distinguishes stannite Cu2FeSnS4 from ferrokësterite with the
    same ideal formula, and kësterite Cu2ZnSnS4. Grandfathered years 1832/1956 are
    not approval identifiers. Current spelling and identity do not independently authenticate
    every historical specimen.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: natural
  kind: primary_source
  reference: https://www.jgeosci.org/content/JCGS2001_1-2__cerny2.pdf
  locator: Entire seven-page scanned original, printed 27–33, all Figures 1–4 and
    Tables 1–3 personally inspected; page 29 naming limitation
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Four natural Peerless nodules include Fe-dominant PPK-1/4 and Zn-dominant
    PPK-2/3. EMP chemistry and powder unit cells are supported. The authors explicitly
    assign names by composition without refined cation ordering or space-group determinations;
    the record retains that boundary. Publisher indexing 27–34 conflicts with the
    actual original ending 33.
  snapshot_sha256: 725a03831bb5841af745634f5bdea72332b514135237c53244410b6bdf5c78e6
- evidence_id: leaching
  kind: primary_source
  reference: https://gsm.org.my/wp-content/uploads/gsm_file_2/702001-101558-PDF.pdf
  locator: Complete Teh1979 article, issue PDF pages 3–9 / printed 85–91, all three
    original figures personally inspected
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Pure historical Thiobacillus ferrooxidans from Ranstad was maintained in
    9K medium. Synthetic feeds were made in sealed evacuated silica tubes and reportedly
    XRD checked, without patterns or quantitative purity. Natural stannite is a separate
    Hock Leong Mine, Ampang specimen. Figure 1 follows 35 days,32 C,0.5% pulp and
    particles below0.16mm; initial pH1.5 in Results conflicts with pH2.5 in Figures1–2.
    Reported 0.1% optimum is a different claim. AAS tin and colorimetric confirmation
    support soluble tin observation, not isolated product.
  snapshot_sha256: 367cc2009beae95535ebab403eec317a554a05b2a3d21de55dbaef85c9e419d0
- evidence_id: controls
  kind: primary_source
  reference: https://gsm.org.my/wp-content/uploads/gsm_file_2/702001-101558-PDF.pdf
  locator: Printed85–87 and Figure1 on89, bacterial and separate organic-acid assays
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Reported percentages are 54.45 synthetic stannite,31.30 natural stannite
    and72.66 synthetic kesterite. Only synthetic stannite has a plotted sterile comparator.
    No matched sterile kesterite or natural-stannite arm is shown. The printed x1000ppm
    graph axis is inconsistent with available loading information; neither record
    digitizes it. Inoculum, assay volume, aeration, replicate/error information and
    actual ferrous dose are missing. Different autoclaved organic-acid tests do not
    demonstrate biogenic leachant production or a matched bacterial advantage.
  snapshot_sha256: 367cc2009beae95535ebab403eec317a554a05b2a3d21de55dbaef85c9e419d0
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920&mode=Info
  locator: Official species page and historical homotypic synonym
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: NCBITaxon920 maps Acidithiobacillus ferrooxidans and Thiobacillus ferrooxidans
    at species scope. No stock accession, sequenced isolate or molecular authentication
    of the historical Ranstad strain is inferred.
  snapshot_sha256: c6d264e2f6ed730350be86773d9564c7427f7f089b57ed566d6494e3bd21a4ac
- evidence_id: weathering
  kind: primary_source
  reference: https://doi.org/10.5194/ejm-34-493-2022
  locator: Complete original14pages, all Figures1–8 and Tables1–4 personally inspected;
    Figures6b and8b
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Selected natural grains from Kaňk and Giftkies have SAED patterns identified
    as stannite. Other grains and compositional series are not all independently structure-refined.
    Weathering/diffusion versus dissolution-reprecipitation interpretations do not
    demonstrate microbial activity, controlled extraction or recovery. The historical
    ferrokësterite formula in Table1 is not adopted as current nomenclature.
  snapshot_sha256: c4b5e5091a67f113997d6cf40a0969ae2cd7ef00a7b1e165b57336a397fb3323
- evidence_id: supplement
  kind: primary_source
  reference: https://ejm.copernicus.org/articles/34/493/2022/ejm-34-493-2022-supplement.zip
  locator: Original title page and Tables S1–S3 XLSX; six sheet XMLs independently
    parsed, headers plus first/last rows read
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: The original supplement supplies element-mass and oxide-mass tables for
    the two localities, including Ag2O header in S3. Reviewer inventoried all six
    sheets and sampled their rows; no claim to analytically revalidate every cell.
    No supplemental numerical cell is imported into the record; other underlying data
    remain on request.
  snapshot_sha256: 93600dfe967e758923c509c668fc4448bc27e25582e8e981f65a70dd7cb6e88a
- evidence_id: dossier
  kind: record_content
  reference: research/sources/round48-sn-minerals/20261012T060237Z-source-investigation.json
  locator: Complete paired dossier and all94 raw-artifact hashes
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: All94 artifact hashes and the Markdown hash match. Full acquired1979,2001,2022
    originals are separated from unavailable1981/Hall/Moore originals. Shared historical
    extraction percentages make1981 an overlap lead, not demonstrated independent
    replication.
  snapshot_sha256: 7190856a6e1afdbfc059dc14e1eb50a369a59946d83d3d0399b26a89d21972b0
- evidence_id: history
  kind: record_content
  reference: history/records/stannite/2026-10-12T060009Z-codex-9ad869.yaml
  locator: Complete canonical CREATE sidecar plus distinct inline event
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Actual codex/GPT-6/codex provenance, new record target, timestamps and
    curation scope are coherent. Reviewer authored none of this record, its history
    or dossier.
  snapshot_sha256: 4d801149d5e841a454b5f156f401831e3698f3b824ca3fb9b9ce59424eb03951
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round48-sn-independent/dedup-receipt.json
  locator: Independent bounded current/original scientific text and referenced raw
    roots
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: The two new owners are distinct from elemental tin, mixed resources, synthetic
    device materials and prior study mentions. Within this bounded search, no earlier
    accepted duplicate owner or duplicate curated1979 assay was identified; prior
    source leads are explicitly retained.
  snapshot_sha256: c32428520864b6983ed1bf1ad7036280198bef4bcd6b896cebfa7d02d714b526
  search_scope: rg --no-ignore --hidden --follow across current/original data/records,research,reviews,history;
    3720 metadata files and 177 existing referenced research/raw/evidence roots. Pattern
    stannite|k[eë]sterite|ejm-34-493-2022|geomicrobiological|Peerless. Text-bearing
    extensions only; missing historical roots listed in receipt, binary contents not
    generically decoded. Owner regex substring matches were manually distinguished;
    no unrelated machine search.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round48-sn-independent/web-notices.json
  locator: Three live exact-title/DOI notice queries
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: No affecting correction or retraction was identified in the returned query
    sets. Publisher metadata corroborates the2001 indexing discrepancy. Secondary
    search hits are discovery context only, not authority or substitutes for original
    graphics.
  snapshot_sha256: 05f4fca736252e1d7c7767091fe70f8d436236c7bfd01631bb9c0dc659da4c6a
  search_scope: 'web.run queries: "Recovery of tin by geomicrobiological techniques"
    correction erratum; "Stannite and kesterite from the Peerless pegmatite" correction
    nomenclature; "10.5194/ejm-34-493-2022" correction retraction. First returned
    sets only, no date/domain filters, no exhaustive pagination or universal absence
    claim.'
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round48-final-terminal.json
  locator: Actual completed cohort terminal receipt and each raw command log
  accessed_at: '2026-10-12T06:09:10Z'
  support: supports
  summary: Parent-executed final gates independently read and byte-hash verified:308passed3skipped175.55s,236records,279histories;
    separate nonempty/history checks passed. Validation does not prove scientific
    truth.
  snapshot_sha256: 720239d00b63ba44ee95474c1f3ad662a26a88edf01f1dfac2bd43ed0c223fbf
assessments:
- assessment_id: identity
  area: identity
  topic: Species, specimen and material boundaries
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - record
  - ima
  - natural
  - dedup
  summary: Mineral species and natural Fe/Zn-bearing solid solutions remain distinct
    from elemental/commodity tin, synthetic endmembers, device films and polymorphic
    ferrokësterite. Composition-only names are not overrepresented as solved structures.
- assessment_id: organism
  area: identity
  topic: Historical strain and biomass state
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - taxonomy
  - leaching
  - record
  summary: Growing iron-oxidizing culture is identified at historical species level;
    current taxon ID is a species-name mapping and does not supply missing accession
    or inoculum.
- assessment_id: mechanism
  area: evidence
  topic: Conditions, controls and causality
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - leaching
  - controls
  - record
  summary: The experiment supports source-attributed soluble-tin observations in inoculated
    assays. Direct versus indirect action, specific tin redox pathway and causal microbial
    advantage for unmatched materials remain unresolved. pH, loading and missing comparator
    limits are accurately retained.
- assessment_id: quantity
  area: evidence
  topic: Percentages, denominator and product scope
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - controls
  - record
  summary: Reported extraction percentages remain attributed to their exact natural/synthetic
    material. Incoherent graph concentration units are not converted; no closed balance,
    isolated product, purity or industrial deployment is inferred.
- assessment_id: criticality
  area: scope
  topic: Criticality and deployment
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - record
  - leaching
  summary: No jurisdictional criticality claim is made. Element-list membership is
    not inherited by a mineral species. Laboratory dissolution and natural weathering
    are not industrial recovery.
- assessment_id: provenance
  area: provenance
  topic: Exact state and completed checks
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - dossier
  - history
  - gates
  - notices
  summary: Native inspect captured record, CREATE history, both dossier files and
    schema before judgment; all hashes remain unchanged.94 source artifacts, named
    validation and actual parent gates independently verified.
- assessment_id: weathering
  area: evidence
  topic: Natural specimen diffraction and weathering
  outcome: supported
  target_ids:
  - cmmmech:stannite
  evidence_ids:
  - weathering
  - supplement
  - record
  summary: Selected SAED identifications support the stated natural stannite context,
    with no blanket identification of all solid solutions or microbial attribution
    to mine-waste weathering.
findings: []
actions: []
limitations:
- Historical assay strain lacks an accession and modern molecular confirmation; no
  inoculum, assay volume, aeration, replication or error model is supplied.
- Initial pH1.5 prose conflicts with pH2.5 figure captions; graph x1000ppm scale cannot
  be reconciled confidently with pulp density. Reported extraction percentages are
  not validated closed balances.
- Synthetic-stannite sterile comparator is not a matched control for natural stannite
  or synthetic kesterite. Acid/iron chemistry and microbial effects are incompletely
  separated.
- Composition-based Peerless nomenclature does not determine cation ordering/space
  group; historical synthetic XRD patterns and phase-purity data are not published.
- No inherited criticality, isolated tin product, product purity or industrial recovery
  is demonstrated.
- Review uses independently read same-session official source bytes and verified acquisition
  receipts; every authority PDF was not separately redownloaded. Notice and dedup
  searches are bounded.
notes:
- Both tin records were assessed together from common originals and have separate
  native observations with their own exact target/history input hashes. The initial
  system-Python orchestration failed on missing yaml before native inspect; it was
  rerun using the existing project environment. No saved scientific review or curated
  record was altered.
tags:
- round48
- independent
- stannite
- mineral-identity
- bioleaching
- control-limitations
```
