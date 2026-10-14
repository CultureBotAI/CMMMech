# Independent scientific review of riebeckite

- Review: 20261014T093328Z-riebeckite-round67-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-14T09:28:03.978660Z
- Finished UTC: 2026-10-14T09:33:28.290242Z
- Reviewer: codex /root/round67_phosphates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact record supports riebeckite identity via UICC crocidolite and a narrow laboratory culture-associated iron-redox observation. Extracted and dissolved fractions, unresolved redox location and persistent fibres are correctly distinguished. No supported curation defect found.

## Scope And Provenance

Full exact record and CREATE sidecar against claim-bearing primary evidence and authority identifiers.

Selection: Assigned two separate mineral records, one per native record observation. Preliminary source/record reading before inspect is disclosed; final field-by-field judgment and figures followed inspect.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4df8fe16fc1625d789d28bb7ec727d48785c1a26.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:riebeckite | data/records/riebeckite.yaml | maintained | Riebeckite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Named record validation | passed | True | cmmmech:riebeckite | Reviewer execution in locked offline environment; one record, zero failures. |
| Coordinator completed batch gate 1 | passed | True | cmmmech:riebeckite | Actual coordinator execution 2026-10-14T09:26:52.988700+00:00 to 2026-10-14T09:30:06.414696+00:00; receipt and original log hash checked independently. |
| Coordinator completed batch gate 2 | passed | True | cmmmech:riebeckite | Actual coordinator execution 2026-10-14T09:30:06.414787+00:00 to 2026-10-14T09:30:12.029136+00:00; receipt and original log hash checked independently. |
| Coordinator completed batch gate 3 | passed | True | cmmmech:riebeckite | Actual coordinator execution 2026-10-14T09:30:12.029235+00:00 to 2026-10-14T09:30:15.099901+00:00; receipt and original log hash checked independently. |

## Scientific And Domain Assessments

### Riebeckite species versus asbestiform experimental feed

identity: supported. Targets: cmmmech:riebeckite.

Current IMA species and Handbook crocidolite mapping justify mineral owner; UICC crocidolite does not imply all riebeckite specimens are asbestos waste.

### Living iron-reducing culture and analytical fraction boundaries

evidence: supported. Targets: cmmmech:riebeckite.

Methods support species-level living cultures, anaerobic conditions, hydrogen electron donor/CO2 carbon source, Fe(OH)3 comparator and uninoculated mineral controls. Analytical HCl extraction is separate from culture medium and aqueous filtered analysis.

### Culture-associated redox, dissolved release and unresolved location

quantity: supported. Targets: cmmmech:riebeckite.

Figure1A/C supports growth and greater extractableFe(II) fraction; Figure2A supports a transient dissolved-Fe increase over controls. Figure3A–C preserves crystallinity/grain boundaries, and Figure4C does not establish biomass Fe uptake. Structural/coating location and electron-transfer pathways remain hypotheses.

### Exact bytes, source identity, history and completed gates

provenance: supported. Targets: cmmmech:riebeckite.

Native-inspected working-tree hashes match final bytes; CREATE sidecar and inline event accurately describe curator work. Named and actual final batch gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/riebeckite.yaml; Entire inspected record | supports | Final field-by-field judgment used exact native-inspected bytes. Preliminary reading preceded inspect; no target changed during review. |
| history | history/records/riebeckite/2026-10-14T092131Z-codex-a6a5ce.yaml; Whole CREATE sidecar and inline curation_history | supports | Actual Codex GPT-6/codex actor, target and creation description agree. Reviewer made no record/history edit. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; Definitions pages 1–2; chrysotile page45 and riebeckite page185 | supports | Original retained IMA pages visually inspected: chrysotile Mg3Si2O5(OH)4 Rd2007 s.p.; riebeckite vacancy-Na2(Fe(II)3Fe(III)2)Si8O22(OH)2 Rd2012 s.p. Special-procedure dates are not invented approval accessions. |
| choi | https://doi.org/10.1128/aem.02048-22; Main Results, Discussion, Conclusions and Materials and Methods; figure captions1–4 | supports | Independently read scientific main body and claim-bearing methods/results/discussion in retained complete PMC HTML/text. Crocidolite culture-associated redox and transient dissolved-Fe increase, and chrysotile null bulk-release enhancement, are reported. Control-subtraction and Mg text/plot discrepancy remain unresolved; no SI tables adopted. |
| metadata | https://pubmed.ncbi.nlm.nih.gov/37184266/; PubMed XML journal, title, DOI/PMCID and article dates | supports | Original PubMed record confirms author/title, 2023, AEM89(6), e02048-22, DOI10.1128/aem.02048-22 and PMCID10304897. No affecting notice was identified in this retained metadata or bounded live query, not an exhaustive notice guarantee. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1573172; Official retained species XML TaxId, ScientificName and Rank | supports | Species identity agrees. Type-material synonym lists do not authenticate the experimental stock at strain rank. |
| dedup | /private/tmp/cmm-round67-phosphate-peer-reviews/dedup.txt; Repository records, research, history and reviews searched with hidden/ignored files included | context_only | Existing chrysotile-asbestos-tailings is a secondary resource and does not duplicate the mineral species. No machinewide or study-novelty absence claim. |
| search | https://journals.asm.org/doi/10.1128/aem.02048-22; Live independent search first returned result sets on 2026-10-14 UTC | context_only | No affecting correction/retraction or direct independent contradiction surfaced in these result sets. Press-release toxicity/electron-transfer claims were not adopted. Main-study negative controls and persistent crystallinity remain strongest directly reviewed counterevidence. |
| si_limit | https://github.com/CultureBotAI/CMMMech/issues/210; Prepared issue body, acquisition-alternatives.json and source dossier | context_only | Publisher403 and non-PDF PMC responses are documented access limits. Reviewer did not acquire/read original SI. Issue210 tracks recipes, tables, extraction/beam controls and numerical correction reconciliation; its body agrees with narrow accepted record claims. |
| named | /private/tmp/cmm-round67-phosphate-peer-reviews/riebeckite-validation.log; Reviewer-executed complete named validation log | supports | Locked offline named validation exit0; one record checked, zero failures. |
| batch | /private/tmp/cmm-round67-final-gates.json; Actual completed coordinator receipt and SHA-verified original log | supports | just check passed317 tests with3 skips; nonempty validation312 records0 failures; trusted-base history validation362 histories0 errors. Structural success does not establish scientific truth. |
| figure1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/; Original Figure 1; all panels visually inspected | supports | Original figure independently visually checked against its caption, axes and main text. Specific accepted/limited interpretations are assessed below. |
| figure2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/; Original Figure 2; all panels visually inspected | supports | Original figure independently visually checked against its caption, axes and main text. Specific accepted/limited interpretations are assessed below. |
| figure3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/; Original Figure 3; all panels visually inspected | supports | Original figure independently visually checked against its caption, axes and main text. Specific accepted/limited interpretations are assessed below. |
| figure4 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/; Original Figure 4; all panels visually inspected | supports | Original figure independently visually checked against its caption, axes and main text. Specific accepted/limited interpretations are assessed below. |
| handbook | https://www.handbookofmineralogy.org/pdfs/riebeckite.pdf; Page1 Occurrence and full two-page entry | supports | Original page1 visually checked: asbestiform crocidolite maps to riebeckite. Older formula is not substituted for current IMA identity. |

## Limits And Additional Notes

- Official Choi supplement was not acquired or assessed; detailed recipes/extraction and beam-control claims remain bounded to main text.
- ICP-OES negative-control subtraction is ambiguous alongside displayed control series.
- Structural versus surface-coating reactive iron, electron-transfer mechanism and exact stock identity remain unresolved.
- Dissolved iron declines after its early peak and acid-extractable fractions are not recovered-product yield.
- Corrections required from this review: none. No target or history bytes changed.
- The absent local SI artifact is an acquisition limitation, not a claim that the published supplement does not exist; follow-up issue210 remains open.
- Raw originals stay outside Git; this review does not authorize future publication or direct author contact.
- Initial inspect attempt used a wrong schema path and failed; successful inspect with src/cmmmech/schema/cmmmech.yaml captured the source hashes before final assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T093328Z-riebeckite-round67-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of riebeckite
started_at: '2026-10-14T09:28:03.978660Z'
finished_at: '2026-10-14T09:33:28.290242Z'
reviewer:
  identity: codex /root/round67_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Record, history and source dossier authored by /root/round67_new_frontier.
    Reviewer independently read originals/figures and judged exact inspected bytes;
    no target/history/dossier edits. Original acquisitions were shared; assessment
    was independent. Reviewer authored separate phosphate records, not these targets.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact record supports riebeckite identity via UICC crocidolite and a
  narrow laboratory culture-associated iron-redox observation. Extracted and dissolved
  fractions, unresolved redox location and persistent fibres are correctly distinguished.
  No supported curation defect found.
source:
  git_revision: 4df8fe16fc1625d789d28bb7ec727d48785c1a26
  state: working_tree
  inputs:
  - path: data/records/riebeckite.yaml
    sha256: 5c0febb77a492454be39c398cd2d364aa3fdb927e2f9aab46e59efd35dd20e11
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/riebeckite/2026-10-14T092131Z-codex-a6a5ce.yaml
    sha256: 31b3d7a0e52ad875c84dd3dbfaa0d651f2b8c66955babb2a64e9ee4732f42df2
    role: context
  - path: research/sources/round67-new-frontier/20261014T092355Z-source-investigation.json
    sha256: cf7ca63baf04b82b523e11115c6bcdaf0b87f15a9883b46d22d5ca04d64705ca
    role: context
  - path: research/sources/round67-new-frontier/20261014T092355Z-source-investigation.md
    sha256: a27e269302c1bef8ca2e34ed504fbf59375d03ab8e6eaefb89b17f8efba9fb22
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full exact record and CREATE sidecar against claim-bearing primary
    evidence and authority identifiers.
  selection: Assigned two separate mineral records, one per native record observation.
    Preliminary source/record reading before inspect is disclosed; final field-by-field
    judgment and figures followed inspect.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:riebeckite
targets:
- kind: maintained
  label: Riebeckite
  owner_paths:
  - path: data/records/riebeckite.yaml
    repository: CultureBotAI/CMMMech
    role: maintained record
  path: data/records/riebeckite.yaml
  target_id: cmmmech:riebeckite
checks:
- check_id: named
  name: Named record validation
  command: uv run --locked cmmmech validate data/records/riebeckite.yaml
  status: passed
  required: true
  summary: Reviewer execution in locked offline environment; one record, zero failures.
  target_ids:
  - cmmmech:riebeckite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch0
  name: Coordinator completed batch gate 1
  command: just check
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T09:26:52.988700+00:00 to 2026-10-14T09:30:06.414696+00:00;
    receipt and original log hash checked independently.
  target_ids:
  - cmmmech:riebeckite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch1
  name: Coordinator completed batch gate 2
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T09:30:06.414787+00:00 to 2026-10-14T09:30:12.029136+00:00;
    receipt and original log hash checked independently.
  target_ids:
  - cmmmech:riebeckite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Coordinator completed batch gate 3
  command: uv run --locked cmmmech validate-history --base 4df8fe16fc1625d789d28bb7ec727d48785c1a26
  status: passed
  required: true
  summary: Actual coordinator execution 2026-10-14T09:30:12.029235+00:00 to 2026-10-14T09:30:15.099901+00:00;
    receipt and original log hash checked independently.
  target_ids:
  - cmmmech:riebeckite
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/riebeckite.yaml
  locator: Entire inspected record
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Final field-by-field judgment used exact native-inspected bytes. Preliminary
    reading preceded inspect; no target changed during review.
  snapshot_sha256: 5c0febb77a492454be39c398cd2d364aa3fdb927e2f9aab46e59efd35dd20e11
- evidence_id: history
  kind: record_content
  reference: history/records/riebeckite/2026-10-14T092131Z-codex-a6a5ce.yaml
  locator: Whole CREATE sidecar and inline curation_history
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Actual Codex GPT-6/codex actor, target and creation description agree.
    Reviewer made no record/history edit.
  snapshot_sha256: 31b3d7a0e52ad875c84dd3dbfaa0d651f2b8c66955babb2a64e9ee4732f42df2
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: Definitions pages 1–2; chrysotile page45 and riebeckite page185
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: 'Original retained IMA pages visually inspected: chrysotile Mg3Si2O5(OH)4
    Rd2007 s.p.; riebeckite vacancy-Na2(Fe(II)3Fe(III)2)Si8O22(OH)2 Rd2012 s.p. Special-procedure
    dates are not invented approval accessions.'
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: choi
  kind: primary_source
  reference: https://doi.org/10.1128/aem.02048-22
  locator: Main Results, Discussion, Conclusions and Materials and Methods; figure
    captions1–4
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Independently read scientific main body and claim-bearing methods/results/discussion
    in retained complete PMC HTML/text. Crocidolite culture-associated redox and transient
    dissolved-Fe increase, and chrysotile null bulk-release enhancement, are reported.
    Control-subtraction and Mg text/plot discrepancy remain unresolved; no SI tables
    adopted.
  snapshot_sha256: ef77b46faacbab1d69208675a4913bb84e5fe9f42fb17e9d0230c886a3010105
- evidence_id: metadata
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/37184266/
  locator: PubMed XML journal, title, DOI/PMCID and article dates
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Original PubMed record confirms author/title, 2023, AEM89(6), e02048-22,
    DOI10.1128/aem.02048-22 and PMCID10304897. No affecting notice was identified
    in this retained metadata or bounded live query, not an exhaustive notice guarantee.
  snapshot_sha256: 81ae8f14fd1924234214a554caa62ce56037c1f8f7688ca41f40849ebe8412ab
- evidence_id: taxonomy
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1573172
  locator: Official retained species XML TaxId, ScientificName and Rank
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Species identity agrees. Type-material synonym lists do not authenticate
    the experimental stock at strain rank.
  snapshot_sha256: 430122a5ae634e84230b743070254cc99c02a6058e33167867969492a99c565d
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round67-phosphate-peer-reviews/dedup.txt
  locator: Repository records, research, history and reviews searched with hidden/ignored
    files included
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: context_only
  summary: Existing chrysotile-asbestos-tailings is a secondary resource and does
    not duplicate the mineral species. No machinewide or study-novelty absence claim.
  search_scope: rg --no-ignore --hidden --follow -n -i 'chrysotile|riebeckite|crocidolite|10.1128/aem.02048-22'
    data/records research history reviews; relevant owner references inspected.
  snapshot_sha256: 1e4f2fde32ba5aa2880da6994cb396597b34ee2ec973291c9bd8c885681ee931
- evidence_id: search
  kind: search
  reference: https://journals.asm.org/doi/10.1128/aem.02048-22
  locator: Live independent search first returned result sets on 2026-10-14 UTC
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: context_only
  summary: No affecting correction/retraction or direct independent contradiction
    surfaced in these result sets. Press-release toxicity/electron-transfer claims
    were not adopted. Main-study negative controls and persistent crystallinity remain
    strongest directly reviewed counterevidence.
  search_scope: 'Queries: "10.1128/aem.02048-22" correction retraction erratum; "Thermovibrio
    ammonificans" chrysotile magnesium silicon biosilicification; "Deferrisoma palaeochoriense"
    crocidolite reduction contradiction. First batches only; no pagination, domain
    or date restriction.'
- evidence_id: si_limit
  kind: search
  reference: https://github.com/CultureBotAI/CMMMech/issues/210
  locator: Prepared issue body, acquisition-alternatives.json and source dossier
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: context_only
  summary: Publisher403 and non-PDF PMC responses are documented access limits. Reviewer
    did not acquire/read original SI. Issue210 tracks recipes, tables, extraction/beam
    controls and numerical correction reconciliation; its body agrees with narrow
    accepted record claims.
  search_scope: Reviewed curator acquisition-alternatives.json publisher and PMC URLs
    plus prepared issue210 and dossier describing EuropePMC failure; no fresh supplement
    download attempt by this reviewer and no existence-absence inference.
  snapshot_sha256: 0f50b1c47c7cda2c429e7d0997362ea0502d7cea1f897692ee332574fd1db32e
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round67-phosphate-peer-reviews/riebeckite-validation.log
  locator: Reviewer-executed complete named validation log
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Locked offline named validation exit0; one record checked, zero failures.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round67-final-gates.json
  locator: Actual completed coordinator receipt and SHA-verified original log
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: just check passed317 tests with3 skips; nonempty validation312 records0
    failures; trusted-base history validation362 histories0 errors. Structural success
    does not establish scientific truth.
  snapshot_sha256: 082a605db5c68ab999281d596f4971f8cfef0db72f37635dbe375c1470852de2
- evidence_id: figure1
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/
  locator: Original Figure 1; all panels visually inspected
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Original figure independently visually checked against its caption, axes
    and main text. Specific accepted/limited interpretations are assessed below.
  snapshot_sha256: 2ef74904ffae8eb6b55a23eddb20aeefb5216d71a820044f6299dbbf974ecf5d
- evidence_id: figure2
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/
  locator: Original Figure 2; all panels visually inspected
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Original figure independently visually checked against its caption, axes
    and main text. Specific accepted/limited interpretations are assessed below.
  snapshot_sha256: ab24a1e23ab6595b0a5b83af4e22ea0fbe776ac68c48461f483ac416bb57a026
- evidence_id: figure3
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/
  locator: Original Figure 3; all panels visually inspected
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Original figure independently visually checked against its caption, axes
    and main text. Specific accepted/limited interpretations are assessed below.
  snapshot_sha256: 58d3275dabe9f119fc1205024c052f176e703a0515e79e4c329b5cdcb019fcd3
- evidence_id: figure4
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304897/
  locator: Original Figure 4; all panels visually inspected
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: Original figure independently visually checked against its caption, axes
    and main text. Specific accepted/limited interpretations are assessed below.
  snapshot_sha256: 47ea66313625d6fe997a8b8dfc0ac1652d1d6c981b65dec3a3dc7f40fb4fab08
- evidence_id: handbook
  kind: authority
  reference: https://www.handbookofmineralogy.org/pdfs/riebeckite.pdf
  locator: Page1 Occurrence and full two-page entry
  accessed_at: '2026-10-14T09:33:28.290242Z'
  support: supports
  summary: 'Original page1 visually checked: asbestiform crocidolite maps to riebeckite.
    Older formula is not substituted for current IMA identity.'
  snapshot_sha256: acfb2c8cafe534260785ecedf1a9f01e3f76cdfe06737a21e53a93af96b9c6ad
assessments:
- assessment_id: identity
  area: identity
  topic: Riebeckite species versus asbestiform experimental feed
  outcome: supported
  summary: Current IMA species and Handbook crocidolite mapping justify mineral owner;
    UICC crocidolite does not imply all riebeckite specimens are asbestos waste.
  target_ids:
  - cmmmech:riebeckite
  evidence_ids:
  - record
  - ima
  - handbook
  - dedup
  dimensions:
  - name: material_form
    value: UICC crocidolite reference material as supplied
    definition: Asbestiform variety in one laboratory assay, not universal riebeckite
      behavior.
    evidence_ids:
    - choi
    - handbook
  - name: criticality
    value: No jurisdiction/list/edition asserted
    definition: No constituent criticality inherited.
    evidence_ids:
    - record
- assessment_id: experiment
  area: evidence
  topic: Living iron-reducing culture and analytical fraction boundaries
  outcome: supported
  summary: Methods support species-level living cultures, anaerobic conditions, hydrogen
    electron donor/CO2 carbon source, Fe(OH)3 comparator and uninoculated mineral
    controls. Analytical HCl extraction is separate from culture medium and aqueous
    filtered analysis.
  target_ids:
  - cmmmech:riebeckite
  evidence_ids:
  - record
  - choi
  - taxonomy
  - figure1
  dimensions:
  - name: organism_and_biomass
    value: Living Deferrisoma palaeochoriense cultures; speciesNCBITaxon1573172
    definition: Type strain synonyms do not establish assay stock provenance.
    evidence_ids:
    - taxonomy
    - choi
  - name: conditions
    value: 10g/L UICCfeed,25mL modifiedDSM1210,60°C,pH6.1–6.4,1.5wt%NaCl,H2/CO2(80:20,0.2MPa),oneweek,n=3
    definition: Fe(OH)3 is positive growth comparator; mineral-medium bottles are
      negative comparators.
    evidence_ids:
    - choi
  - name: analytical_fraction
    value: 0.2-micrometre filtrates versus8hHCl extraction of unfiltered samples
    definition: 12NHCl reagent added1:1 is not a recovery operation or incubation
      condition.
    evidence_ids:
    - choi
- assessment_id: outcome
  area: quantity
  topic: Culture-associated redox, dissolved release and unresolved location
  outcome: supported
  summary: Figure1A/C supports growth and greater extractableFe(II) fraction; Figure2A
    supports a transient dissolved-Fe increase over controls. Figure3A–C preserves
    crystallinity/grain boundaries, and Figure4C does not establish biomass Fe uptake.
    Structural/coating location and electron-transfer pathways remain hypotheses.
  target_ids:
  - cmmmech:riebeckite
  evidence_ids:
  - record
  - choi
  - figure1
  - figure2
  - figure3
  - figure4
  dimensions:
  - name: denominator
    value: ExtractableFe(II)/total extractedFe is a redox fraction
    definition: Not the percentage of feed iron recovered as product.
    evidence_ids:
    - choi
    - figure1
  - name: causal_limits
    value: Coating versus lattice reduction unresolved; exact ICP-OES subtraction
      basis unresolved
    definition: No unique long-range mechanism or quantitative recovery yield inferred.
    evidence_ids:
    - record
    - choi
    - si_limit
  - name: deployment
    value: Laboratory feed-associated iron transformation
    definition: No fibre destruction, detoxification, isolated metal product or industrial
      treatment demonstrated.
    evidence_ids:
    - choi
    - figure3
- assessment_id: provenance
  area: provenance
  topic: Exact bytes, source identity, history and completed gates
  outcome: supported
  summary: Native-inspected working-tree hashes match final bytes; CREATE sidecar
    and inline event accurately describe curator work. Named and actual final batch
    gates passed.
  target_ids:
  - cmmmech:riebeckite
  evidence_ids:
  - record
  - history
  - metadata
  - search
  - named
  - batch
findings: []
actions: []
limitations:
- Official Choi supplement was not acquired or assessed; detailed recipes/extraction
  and beam-control claims remain bounded to main text.
- ICP-OES negative-control subtraction is ambiguous alongside displayed control series.
- Structural versus surface-coating reactive iron, electron-transfer mechanism and
  exact stock identity remain unresolved.
- Dissolved iron declines after its early peak and acid-extractable fractions are
  not recovered-product yield.
notes:
- 'Corrections required from this review: none. No target or history bytes changed.'
- The absent local SI artifact is an acquisition limitation, not a claim that the
  published supplement does not exist; follow-up issue210 remains open.
- Raw originals stay outside Git; this review does not authorize future publication
  or direct author contact.
- Initial inspect attempt used a wrong schema path and failed; successful inspect
  with src/cmmmech/schema/cmmmech.yaml captured the source hashes before final assessment.
tags:
- round67
- independent
- riebeckite
- original-figures
```
