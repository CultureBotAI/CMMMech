# Independent scientific review of MR-4-associated synthetic manganite dissolution

- Review: 20261014T064301Z-manganite-round64-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T06:29:08.536487Z
- Finished UTC: 2026-10-14T06:43:01.681477Z
- Reviewer: codex /root/round64_iron (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The frozen record correctly distinguishes manganite mineral identity from source-assigned synthetic feed, current MR-4 taxonomy and historical nomenclature. The controlled laboratory release observation is supported, with acidic abiotic dissolution, analytical replication, contradictory experimental labels and lack of a product mass balance retained. No supported curation defect was identified.

## Scope And Provenance

Full field-by-field scientific review of the exact maintained record and linked CREATE history, with independent original-source and authority inspection.

Selection: Assigned path and frozen SHA256 a53c5947dbb29076591a28ad0953344af5d5f91c6e7aec3b9640ebfd1ca1f276. Native inspect captured record/history/dossier bytes before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:manganite | data/records/manganite.yaml | maintained | Manganite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:manganite | Checked 1 record(s); 0 failed. Executed by this reviewer; exit 0; 2026-10-14T06:33:02.654323+00:00 to 2026-10-14T06:33:11.371939+00:00. |
| Trusted-base canonical history validation | passed | True | cmmmech:manganite | Checked 342 history record(s); 0 error(s). Executed by this reviewer; exit 0; 2026-10-14T06:33:11.372763+00:00 to 2026-10-14T06:33:22.578754+00:00. |
| Full batch checks | passed | True | cmmmech:manganite | Coordinator command executed 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00; exit 0. Complete receipt and log personally inspected. Assigned record and its reviewed inputs remained frozen; an unrelated lepidocrocite correction landed during this initial batch run, so coordinator is separately repeating the final batch after that correction. |
| Explicit nonempty corpus validation | passed | True | cmmmech:manganite | Coordinator command executed 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00; exit 0. Complete receipt and log personally inspected. Assigned record and its reviewed inputs remained frozen; an unrelated lepidocrocite correction landed during this initial batch run, so coordinator is separately repeating the final batch after that correction. |

## Scientific And Domain Assessments

### Mineral, resource and organism boundaries

identity: supported. Targets: cmmmech:manganite.

Current mineral identity and MR-4 taxon are correctly grounded without inherited element criticality, invented mineral accession or authenticated-stock claim. A manganite constituent in the existing manganese-ore record is a different material owner.

### Biomass, preparation and assay conditions

evidence: supported. Targets: cmmmech:manganite.

The exact living acclimated culture, synthetic preparation and controlled laboratory conditions are retained; separate bottle arms and donor limitations are not conflated.

### Measured release and source contradictions

quantity: supported. Targets: cmmmech:manganite.

Filtered manganese increase supports laboratory culture-associated dissolution. Mn(II) is the authors interpretation; no recovery percentage, product yield, universal mineral ranking or deployment is claimed.

### Traceable sources and actual checks

provenance: supported. Targets: cmmmech:manganite.

Frozen record/history/dossier bytes, original source DOI and named/history validation are consistent. Scientific limitations were retained rather than harmonized.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| named_validation | /private/tmp/cmm-round64-manganite-independent/named.log; Entire log; checks.json preserves actual command and UTC start/finish | supports | Checked 1 record(s); 0 failed. Executed by this independent reviewer. |
| history_validation | /private/tmp/cmm-round64-manganite-independent/history.log; Entire log; checks.json preserves actual command and UTC start/finish | supports | Checked 342 history record(s); 0 error(s). Executed by this independent reviewer. |
| record | data/records/manganite.yaml; Entire file at the exact source.inputs SHA256 | supports | Every field and all retained evidence entries were compared with the original source and identity authorities. |
| history | history/records/manganite/2026-10-14T062347Z-codex-9f9289.yaml; Complete canonical CREATE session and record inline CREATE entry | supports | Correct owner, codex/GPT-6 actor and actual distinct CREATE times. Scope accurately describes the new qualified record; no earlier authorship is invented. |
| local_search | /private/tmp/cmm-round64-manganite-independent/local-search.txt; Exact rg command, full returned path set and exit status | context_only | Hidden and ignored files and relevant symlinks were included. Related raw sources or mixed-resource mentions are not an existing owner for this exact mineral record; no duplicate maintained owner was found within this declared text-search scope. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Original PDF pages 1-2 and 134; status/date definitions, terms and Manganite row | supports | Personally inspected rendered authority pages. Mn3+O(OH), grandfathered G and historical year 1826 are accurately retained; 1826 is not an approval CURIE. |
| handbook | https://handbookofmineralogy.org/pdfs/manganite.pdf; Entire one-page mineral entry | supports | Personally inspected mineral entry and independently opened authority URL. The Mn(III) oxyhydroxide, monoclinic identity and distinct feitknechtite/groutite polymorphs agree; natural-mineral identity does not certify experimental batch purity. |
| taxon | https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/60480/dataset_report; Complete retained Datasets response; taxonomy tax_id, rank, name and parent fields | supports | Personally read curator-acquired authority response: 60480 is species-rank Shewanella sp. MR-4 under unclassified Shewanella. Historical S. putrefaciens is not upgraded to a modern authenticated species or whole-genome match. Independent browser API retry returned Internal Error; no new successful download is claimed. |
| primary | https://doi.org/10.2138/am-1998-11-1244; Complete original nine pages 1564-1572; methods and Figures 1-9/Table 1 | supports | Personally read the complete original and visually inspected all nine pages including every figure and Table 1. M1/lactate, serial acclimation, no experimental casamino acids, anaerobic 10%H2/90%N2, source-reported 27 C/pH 7.4, nominal 200 micromol/L MnOOH and 5e6 cells/mL are correctly scoped. RRUFF original was independently opened in the browser; retained PDF was re-inspected. |
| controls | https://doi.org/10.2138/am-1998-11-1244; Pages 1565-1568; Figure 3 and Table 1 | partial | Active cultures release much more filtered manganese than no-cell/killed/oxygen/CCCP/no-contact arms under the stated protocol. No-carbon cultures still encounter chamber H2. Table 1 acidic inoculated/no-cell means are 101.3/103.1 at pH 4 and 39.4/44.0 at pH 5 versus 12.2/1.2 micromol/L at pH 7.4; acidic release is not a positive microbial increment. HQNO and cyanide do not show the strong inhibition of CCCP/HgCl2. These data do not uniquely identify an enzyme or rule out every diffusible mediator. |
| assay | https://doi.org/10.2138/am-1998-11-1244; Pages 1565-1568; Analytical chemistry, standardization and Table 1 | partial | 0.2 micrometre filtration and acidified flame-AAS samples measure dissolved elemental manganese, not direct oxidation-state speciation. Three samples and repeated instrument reads are subsampling/analytical replication; pH/temperature arms have only two sampling times. Blank subtraction and standards/handling limits are described. Complete eventual reduction is data not shown, and no isolated yield or mass balance is imported. |
| discrepancies | https://doi.org/10.2138/am-1998-11-1244; Abstract; methods; Figures 1-2/8; Table 1; discussion pages 1569-1571 | partial | Record preserves 26/27/around 35 C and pH7.0/7.4 statements; 100 versus 200 micromol/L duplicate labels; Figure 2 100-fold versus text 300-fold cell ranges and timing; and Figure 8 caption approximately 75% versus prose greater than 90%. Microscopy area estimates are not BET. Fixed wet ESEM versus dehydrated gold-coated SEM do not establish native polymer chemistry or a causal reduction function. |
| metadata | https://api.crossref.org/works/10.2138/am-1998-11-1244; Retained Crossref title/DOI/alias/relation fields versus original page 1 | supports | Canonical Crossref DOI and original 1998 volume/pages agree. The 1997 DOI is explicitly an alias. Alternate publisher metadata uses DOI 10.2138/am-1998-1117 for the same title/pages; this is not evidence that the canonical retained DOI is wrong. No update-to entry and empty relation field in the retained response. Browser API retry failed; retained response was personally read. |
| notices | /private/tmp/cmm-round64-manganite-independent/web-search.json; Independent exact DOI notice query and title/contact/mediator query, first returned sets | context_only | No matching correction/retraction notice was identified in the returned sets. Broader Shewanella mediator results concern other experimental systems and were not treated as a verified contradiction or imported mechanism. |
| batch_validation | /private/tmp/cmm-round64-final-gates.json; Complete JSON receipt and referenced full final-gates.log | supports | 317 tests passed, 3 skipped; 293 records and 343 histories valid. Explicit --require-records and trusted-base history also passed. Checked log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99. The assigned record/source inputs did not change. These initial gates preceded saving this review and overlapped another record correction; no claim that they validated this bundle or the subsequently rerendered final batch. |
| dossier_audit | research/sources/round64-manganese/20261014T062554Z-manganite-source-investigation.json; Full curator source dossier and independently recomputed raw-file hashes | supports | Reviewed source boundaries and claim limitations; independently checked all 28 listed raw-file hashes. Complete check receipt /private/tmp/cmm-round64-manganite-independent/dossier-checks.json has SHA256 f8c0f992e8a7ca94f58a2da4d920c2f661be0f411105fc04b7403ed183ad46de. Hash equality establishes preserved evidence bytes, not scientific agreement by itself. |

## Limits And Additional Notes

- Source-assigned synthetic feed lacks reported batch diffraction refinement, composition or quantitative phase purity.
- Dissolved Mn measured by AAS is interpreted as Mn(II); no full product mass balance or isolated recovery was measured.
- Technical sampling/analytical replicates do not establish three independent cultures; no-carbon arms retain H2 availability.
- Acidic no-cell release equals or exceeds inoculated release. Contact and inhibitor effects identify assay dependencies, not a unique universal electron-transfer pathway.
- Temperature, cell-range, duplicate-treatment and microscopy endpoint discrepancies remain unresolved in the original and explicit in the record.
- Native hydrated polymer chemistry and causal biofilm function are not established by fixed/wet versus dehydrated microscopy.
- Notice and duplicate searches were bounded; browser authority retries failed but the curator-acquired exact authority responses were independently inspected.
- Corrections made by this reviewer: none. Record, history and source dossier remain unchanged. No GitHub issue or comment was posted by this reviewer.
- An empty findings list applies only to this exact record and declared evidence scope. It is not a claim of exhaustive literature coverage.
- The review start is the native-inspection input file creation time converted to UTC; the review includes subsequent evidence inspection and checks.
- The initial coordinator batch gates overlapped a correction to lepidocrocite, an unrelated record. This record and all source.inputs hashes remained unchanged; coordinator will repeat final whole-batch gates after that correction and generated-page refresh. This review does not claim that later run already happened.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T064301Z-manganite-round64-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of MR-4-associated synthetic manganite dissolution
started_at: '2026-10-14T06:29:08.536487Z'
finished_at: '2026-10-14T06:43:01.681477Z'
reviewer:
  identity: codex /root/round64_iron
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Different agent from curator /root/round64_manganese. Reviewer
    authored the unrelated akaganeite and lepidocrocite records in this batch, but
    did not author or edit this record, its canonical history or source dossier. Personally
    inspected the cited original evidence and authority entries; native inspection
    preceded the scientific assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The frozen record correctly distinguishes manganite mineral identity from
  source-assigned synthetic feed, current MR-4 taxonomy and historical nomenclature.
  The controlled laboratory release observation is supported, with acidic abiotic
  dissolution, analytical replication, contradictory experimental labels and lack
  of a product mass balance retained. No supported curation defect was identified.
source:
  git_revision: 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  state: working_tree
  inputs:
  - path: data/records/manganite.yaml
    sha256: a53c5947dbb29076591a28ad0953344af5d5f91c6e7aec3b9640ebfd1ca1f276
    role: target
  - path: history/records/manganite/2026-10-14T062347Z-codex-9f9289.yaml
    sha256: c6c2eead6bee5ca0cc19ed1656dbc0f0451a2eeda662e97ee7498c478a58d897
    role: context
  - path: research/sources/round64-manganese/20261014T062554Z-manganite-source-investigation.json
    sha256: 2fa4e3821e9299c56259d8759c9d4cefbdd8540ad9affbc82e2fa2d987e4c2f0
    role: context
  - path: research/sources/round64-manganese/20261014T062554Z-manganite-source-investigation.md
    sha256: 87acbede18e1d633f9ca955706ad024bb8135d86957d16673c93c3f0986a399e
    role: context
scope:
  description: Full field-by-field scientific review of the exact maintained record
    and linked CREATE history, with independent original-source and authority inspection.
  selection: Assigned path and frozen SHA256 a53c5947dbb29076591a28ad0953344af5d5f91c6e7aec3b9640ebfd1ca1f276.
    Native inspect captured record/history/dossier bytes before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:manganite
  exclusions:
  - target: Other organisms, manganese-oxide experiments and new mechanistic extensions
    reason: Other returned references are leads only. No later complete original was
      reviewed as a replication or new measurement for this record.
targets:
- target_id: cmmmech:manganite
  path: data/records/manganite.yaml
  label: Manganite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/manganite.yaml
    role: maintained scientific record
checks:
- check_id: named
  name: Named record validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate data/records/manganite.yaml
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed. Executed by this reviewer; exit 0; 2026-10-14T06:33:02.654323+00:00
    to 2026-10-14T06:33:11.371939+00:00.
  target_ids:
  - cmmmech:manganite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named_validation
- check_id: history
  name: Trusted-base canonical history validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate-history --base 0f4d8ff9e4919714e3dd902dc3573e95922a65fb
  status: passed
  required: true
  summary: Checked 342 history record(s); 0 error(s). Executed by this reviewer; exit
    0; 2026-10-14T06:33:11.372763+00:00 to 2026-10-14T06:33:22.578754+00:00.
  target_ids:
  - cmmmech:manganite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history_validation
- check_id: batch
  name: Full batch checks
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    just check
  status: passed
  required: true
  summary: Coordinator command executed 2026-10-14T06:34:30.350112+00:00 to 2026-10-14T06:41:38.259359+00:00;
    exit 0. Complete receipt and log personally inspected. Assigned record and its
    reviewed inputs remained frozen; an unrelated lepidocrocite correction landed
    during this initial batch run, so coordinator is separately repeating the final
    batch after that correction.
  target_ids:
  - cmmmech:manganite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_validation
- check_id: nonempty
  name: Explicit nonempty corpus validation
  command: UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1
    uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Coordinator command executed 2026-10-14T06:41:38.259472+00:00 to 2026-10-14T06:42:04.731172+00:00;
    exit 0. Complete receipt and log personally inspected. Assigned record and its
    reviewed inputs remained frozen; an unrelated lepidocrocite correction landed
    during this initial batch run, so coordinator is separately repeating the final
    batch after that correction.
  target_ids:
  - cmmmech:manganite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch_validation
evidence:
- evidence_id: named_validation
  kind: validation
  reference: /private/tmp/cmm-round64-manganite-independent/named.log
  locator: Entire log; checks.json preserves actual command and UTC start/finish
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Checked 1 record(s); 0 failed. Executed by this independent reviewer.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: history_validation
  kind: validation
  reference: /private/tmp/cmm-round64-manganite-independent/history.log
  locator: Entire log; checks.json preserves actual command and UTC start/finish
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Checked 342 history record(s); 0 error(s). Executed by this independent
    reviewer.
  snapshot_sha256: c848103fbbc2eba28d3ebd20cfb8ed459ca3780c20c22e2634514ae5c10bae12
- evidence_id: record
  kind: record_content
  reference: data/records/manganite.yaml
  locator: Entire file at the exact source.inputs SHA256
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Every field and all retained evidence entries were compared with the original
    source and identity authorities.
  snapshot_sha256: a53c5947dbb29076591a28ad0953344af5d5f91c6e7aec3b9640ebfd1ca1f276
- evidence_id: history
  kind: record_content
  reference: history/records/manganite/2026-10-14T062347Z-codex-9f9289.yaml
  locator: Complete canonical CREATE session and record inline CREATE entry
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Correct owner, codex/GPT-6 actor and actual distinct CREATE times. Scope
    accurately describes the new qualified record; no earlier authorship is invented.
  snapshot_sha256: c6c2eead6bee5ca0cc19ed1656dbc0f0451a2eeda662e97ee7498c478a58d897
- evidence_id: local_search
  kind: search
  reference: /private/tmp/cmm-round64-manganite-independent/local-search.txt
  locator: Exact rg command, full returned path set and exit status
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: context_only
  summary: Hidden and ignored files and relevant symlinks were included. Related raw
    sources or mixed-resource mentions are not an existing owner for this exact mineral
    record; no duplicate maintained owner was found within this declared text-search
    scope.
  snapshot_sha256: 69ef4dbabc7b1402e67e9d539533dc323b0fe8bf2b98e03ecbc11223c91e26d7
  search_scope: 'Command: [''rg'', ''--no-ignore'', ''--hidden'', ''--follow'', ''-l'',
    ''-i'', ''manganite|10\\.2138/am-199[78]-11-1244'', ''data/records'', ''research'',
    ''reviews'', ''history'', ''/private/tmp/cmm-round38-hausmannite-research'', ''/private/tmp/cmm-round40-cobalt-manganese-oxide-research'',
    ''/private/tmp/cmm-round41-biogenic-birnessite-research'', ''/private/tmp/cmm-round42-biogenic-selectivity-research'',
    ''/private/tmp/cmm-round64-manganese-research''] Scoped text search over records,
    research, reviews, history and the five named raw roots. Binary/unextracted PDFs
    and unrelated machine caches were not exhaustively searched.'
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Original PDF pages 1-2 and 134; status/date definitions, terms and Manganite
    row
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Personally inspected rendered authority pages. Mn3+O(OH), grandfathered
    G and historical year 1826 are accurately retained; 1826 is not an approval CURIE.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://handbookofmineralogy.org/pdfs/manganite.pdf
  locator: Entire one-page mineral entry
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Personally inspected mineral entry and independently opened authority URL.
    The Mn(III) oxyhydroxide, monoclinic identity and distinct feitknechtite/groutite
    polymorphs agree; natural-mineral identity does not certify experimental batch
    purity.
  snapshot_sha256: 664264b589f3ff0481b0b26b6923835f2759eaa0d83467a6adda53a53cb2a6e1
- evidence_id: taxon
  kind: authority
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/60480/dataset_report
  locator: Complete retained Datasets response; taxonomy tax_id, rank, name and parent
    fields
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: 'Personally read curator-acquired authority response: 60480 is species-rank
    Shewanella sp. MR-4 under unclassified Shewanella. Historical S. putrefaciens
    is not upgraded to a modern authenticated species or whole-genome match. Independent
    browser API retry returned Internal Error; no new successful download is claimed.'
  snapshot_sha256: 315dcabedff9c15a032d3f001fc0337cd4a55a80f8a9685698f6d25655e7aaf8
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.2138/am-1998-11-1244
  locator: Complete original nine pages 1564-1572; methods and Figures 1-9/Table 1
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Personally read the complete original and visually inspected all nine pages
    including every figure and Table 1. M1/lactate, serial acclimation, no experimental
    casamino acids, anaerobic 10%H2/90%N2, source-reported 27 C/pH 7.4, nominal 200
    micromol/L MnOOH and 5e6 cells/mL are correctly scoped. RRUFF original was independently
    opened in the browser; retained PDF was re-inspected.
  snapshot_sha256: 4b735a42e3aa0e9a5bf1b5b681c01891c1e958bd7a776abd1241e2582357e99f
- evidence_id: controls
  kind: primary_source
  reference: https://doi.org/10.2138/am-1998-11-1244
  locator: Pages 1565-1568; Figure 3 and Table 1
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: partial
  summary: Active cultures release much more filtered manganese than no-cell/killed/oxygen/CCCP/no-contact
    arms under the stated protocol. No-carbon cultures still encounter chamber H2.
    Table 1 acidic inoculated/no-cell means are 101.3/103.1 at pH 4 and 39.4/44.0
    at pH 5 versus 12.2/1.2 micromol/L at pH 7.4; acidic release is not a positive
    microbial increment. HQNO and cyanide do not show the strong inhibition of CCCP/HgCl2.
    These data do not uniquely identify an enzyme or rule out every diffusible mediator.
  snapshot_sha256: 4b735a42e3aa0e9a5bf1b5b681c01891c1e958bd7a776abd1241e2582357e99f
- evidence_id: assay
  kind: primary_source
  reference: https://doi.org/10.2138/am-1998-11-1244
  locator: Pages 1565-1568; Analytical chemistry, standardization and Table 1
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: partial
  summary: 0.2 micrometre filtration and acidified flame-AAS samples measure dissolved
    elemental manganese, not direct oxidation-state speciation. Three samples and
    repeated instrument reads are subsampling/analytical replication; pH/temperature
    arms have only two sampling times. Blank subtraction and standards/handling limits
    are described. Complete eventual reduction is data not shown, and no isolated
    yield or mass balance is imported.
  snapshot_sha256: 4b735a42e3aa0e9a5bf1b5b681c01891c1e958bd7a776abd1241e2582357e99f
- evidence_id: discrepancies
  kind: primary_source
  reference: https://doi.org/10.2138/am-1998-11-1244
  locator: Abstract; methods; Figures 1-2/8; Table 1; discussion pages 1569-1571
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: partial
  summary: Record preserves 26/27/around 35 C and pH7.0/7.4 statements; 100 versus
    200 micromol/L duplicate labels; Figure 2 100-fold versus text 300-fold cell ranges
    and timing; and Figure 8 caption approximately 75% versus prose greater than 90%.
    Microscopy area estimates are not BET. Fixed wet ESEM versus dehydrated gold-coated
    SEM do not establish native polymer chemistry or a causal reduction function.
  snapshot_sha256: 4b735a42e3aa0e9a5bf1b5b681c01891c1e958bd7a776abd1241e2582357e99f
- evidence_id: metadata
  kind: database
  reference: https://api.crossref.org/works/10.2138/am-1998-11-1244
  locator: Retained Crossref title/DOI/alias/relation fields versus original page
    1
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: supports
  summary: Canonical Crossref DOI and original 1998 volume/pages agree. The 1997 DOI
    is explicitly an alias. Alternate publisher metadata uses DOI 10.2138/am-1998-1117
    for the same title/pages; this is not evidence that the canonical retained DOI
    is wrong. No update-to entry and empty relation field in the retained response.
    Browser API retry failed; retained response was personally read.
  snapshot_sha256: 249a5000c38b28624cb56dee0937c70d760207fe99739a54d2cafb163018070b
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round64-manganite-independent/web-search.json
  locator: Independent exact DOI notice query and title/contact/mediator query, first
    returned sets
  accessed_at: '2026-10-14T06:37:48.741317Z'
  support: context_only
  summary: No matching correction/retraction notice was identified in the returned
    sets. Broader Shewanella mediator results concern other experimental systems and
    were not treated as a verified contradiction or imported mechanism.
  snapshot_sha256: 927b656c2ca090ea65af70fb504622ebc5435fb80eca04d531c6846b5dcabd04
  search_scope: Two exact queries preserved in web-search.json; no date/domain filters
    or pagination. Search results are bounded and do not establish global notice absence.
    Earlier identical searches were also run; only this repeat has a retained full
    response.
- evidence_id: batch_validation
  kind: validation
  reference: /private/tmp/cmm-round64-final-gates.json
  locator: Complete JSON receipt and referenced full final-gates.log
  accessed_at: '2026-10-14T06:43:01.681477Z'
  support: supports
  summary: 317 tests passed, 3 skipped; 293 records and 343 histories valid. Explicit
    --require-records and trusted-base history also passed. Checked log SHA256 25e07902430edb5bfa8e05065fa05624a5821c292ddc1cb3955dec856a280b99.
    The assigned record/source inputs did not change. These initial gates preceded
    saving this review and overlapped another record correction; no claim that they
    validated this bundle or the subsequently rerendered final batch.
  snapshot_sha256: f2af92147f4a25ed646c60e50766925356e9f605d68c9526b0ee195301b4ee5f
- evidence_id: dossier_audit
  kind: record_content
  reference: research/sources/round64-manganese/20261014T062554Z-manganite-source-investigation.json
  locator: Full curator source dossier and independently recomputed raw-file hashes
  accessed_at: '2026-10-14T06:43:01.681477Z'
  support: supports
  summary: Reviewed source boundaries and claim limitations; independently checked
    all 28 listed raw-file hashes. Complete check receipt /private/tmp/cmm-round64-manganite-independent/dossier-checks.json
    has SHA256 f8c0f992e8a7ca94f58a2da4d920c2f661be0f411105fc04b7403ed183ad46de. Hash
    equality establishes preserved evidence bytes, not scientific agreement by itself.
  snapshot_sha256: 2fa4e3821e9299c56259d8759c9d4cefbdd8540ad9affbc82e2fa2d987e4c2f0
assessments:
- assessment_id: identity
  area: identity
  topic: Mineral, resource and organism boundaries
  outcome: supported
  summary: Current mineral identity and MR-4 taxon are correctly grounded without
    inherited element criticality, invented mineral accession or authenticated-stock
    claim. A manganite constituent in the existing manganese-ore record is a different
    material owner.
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - record
  - ima
  - handbook
  - taxon
  - local_search
  dimensions:
  - name: material_form
    value: Manganite mineral; laboratory synthetic source-assigned feed
    definition: Not natural ore, elemental manganese, or certified phase-pure standard
    evidence_ids:
    - ima
    - primary
  - name: criticality
    value: No jurisdiction/list/edition claim
    definition: Omission does not assert noncriticality; it avoids inheritance from
      manganese
    evidence_ids:
    - record
  - name: organism_resolution
    value: NCBITaxon:60480; strain-labelled species node Shewanella sp. MR-4
    definition: Historical S. putrefaciens is retained as publication nomenclature
    evidence_ids:
    - taxon
    - primary
- assessment_id: system
  area: evidence
  topic: Biomass, preparation and assay conditions
  outcome: supported
  summary: The exact living acclimated culture, synthetic preparation and controlled
    laboratory conditions are retained; separate bottle arms and donor limitations
    are not conflated.
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - record
  - primary
  - controls
  dimensions:
  - name: biomass_state
    value: Living serially acclimated MR-4; no-cell and killed comparisons
    definition: Not inert sorbent or isolated enzyme
    evidence_ids:
    - primary
    - controls
  - name: substrate
    value: Source-assigned needle-shaped synthetic manganite
    definition: Synthesis and morphology do not quantify batch phase purity
    evidence_ids:
    - primary
  - name: conditions
    value: M1 with 30 mM lactate, pH 7.4, reported 27 C, anaerobic 10% H2/90% N2
    definition: No-carbon arm is not donor-free; 50 mL bottle arms separate
    evidence_ids:
    - primary
    - controls
- assessment_id: outcome
  area: quantity
  topic: Measured release and source contradictions
  outcome: supported
  summary: Filtered manganese increase supports laboratory culture-associated dissolution.
    Mn(II) is the authors interpretation; no recovery percentage, product yield, universal
    mineral ranking or deployment is claimed.
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - record
  - assay
  - controls
  - discrepancies
  dimensions:
  - name: outcome
    value: Filtered dissolved elemental Mn by AAS
    definition: Does not directly speciate Mn oxidation state or establish isolated
      product
    evidence_ids:
    - assay
  - name: controls
    value: No-cell/killed/oxygen/contact/inhibitor arms; separate pH controls
    definition: Acidic abiotic release and inhibitor-specific nulls remain explicit
    evidence_ids:
    - controls
  - name: scale
    value: Laboratory flask and serum-bottle assays
    definition: Not pilot or commercial extraction
    evidence_ids:
    - primary
- assessment_id: provenance
  area: provenance
  topic: Traceable sources and actual checks
  outcome: supported
  summary: Frozen record/history/dossier bytes, original source DOI and named/history
    validation are consistent. Scientific limitations were retained rather than harmonized.
  target_ids:
  - cmmmech:manganite
  evidence_ids:
  - record
  - history
  - metadata
  - named_validation
  - history_validation
  dimensions: []
findings: []
actions: []
limitations:
- Source-assigned synthetic feed lacks reported batch diffraction refinement, composition
  or quantitative phase purity.
- Dissolved Mn measured by AAS is interpreted as Mn(II); no full product mass balance
  or isolated recovery was measured.
- Technical sampling/analytical replicates do not establish three independent cultures;
  no-carbon arms retain H2 availability.
- Acidic no-cell release equals or exceeds inoculated release. Contact and inhibitor
  effects identify assay dependencies, not a unique universal electron-transfer pathway.
- Temperature, cell-range, duplicate-treatment and microscopy endpoint discrepancies
  remain unresolved in the original and explicit in the record.
- Native hydrated polymer chemistry and causal biofilm function are not established
  by fixed/wet versus dehydrated microscopy.
- Notice and duplicate searches were bounded; browser authority retries failed but
  the curator-acquired exact authority responses were independently inspected.
notes:
- 'Corrections made by this reviewer: none. Record, history and source dossier remain
  unchanged. No GitHub issue or comment was posted by this reviewer.'
- An empty findings list applies only to this exact record and declared evidence scope.
  It is not a claim of exhaustive literature coverage.
- The review start is the native-inspection input file creation time converted to
  UTC; the review includes subsequent evidence inspection and checks.
- The initial coordinator batch gates overlapped a correction to lepidocrocite, an
  unrelated record. This record and all source.inputs hashes remained unchanged; coordinator
  will repeat final whole-batch gates after that correction and generated-page refresh.
  This review does not claim that later run already happened.
tags:
- round64
- independent
- manganite
- primary-figures
```
