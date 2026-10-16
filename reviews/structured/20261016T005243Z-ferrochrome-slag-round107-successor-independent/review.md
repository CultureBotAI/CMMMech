# Independent successor scientific review of ferrochrome slag

- Review: 20261016T005243Z-ferrochrome-slag-round107-successor-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T00:44:40.036200Z
- Finished UTC: 2026-10-16T00:52:43.757415Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The two citation-locator defects are corrected in maintained input with append-only EDIT history. The final scoped abiotic extraction record is supported with the original source contradictions retained.

## Scope And Provenance

Complete final maintained owner, original CREATE and new EDIT histories; independent reassessment of changed locators and unchanged scientific scope.

Selection: Assigned single owner; nativeinspect captured before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 27d842b3e6239bf60565f93c958d3f2cad395037.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:ferrochrome-slag | data/records/ferrochrome-slag.yaml | maintained | Ferrochrome slag |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent final named strict validation | passed | True | cmmmech:ferrochrome-slag | Checked 1 record(s); 0 failed.<br> |
| Coordinator completed batch command 1 | passed | True | cmmmech:ferrochrome-slag | Terminal receipt and log digest independently checked; actual command exit0. |
| Coordinator completed batch command 2 | passed | True | cmmmech:ferrochrome-slag | Terminal receipt and log digest independently checked; actual command exit0. |
| Coordinator completed batch command 3 | passed | True | cmmmech:ferrochrome-slag | Terminal receipt and log digest independently checked; actual command exit0. |
| Coordinator completed batch command 4 | passed | True | cmmmech:ferrochrome-slag | Terminal receipt and log digest independently checked; actual command exit0. |

## Scientific And Domain Assessments

### Processing-defined secondary resource is supported

identity: supported. Targets: cmmmech:ferrochrome-slag.

Processing-defined secondary resource is supported

The Zimasco smelting slag is distinct from ore, beneficiation tailings, chemical-processing residue, alloy and constituentmineral. Table1 is oxide composition despite mineralogy/XRD wording;26.4%MgO is not26.4%Mg. No incorrect material identifier or criticality mapping.

### Laboratory acid-extraction context is appropriately bounded

evidence: supported. Targets: cmmmech:ferrochrome-slag.

Laboratory acid-extraction context is appropriately bounded

Source§2 specifies pulverized80%-passing75µm feed,1L vessel,500mL5/6MHCl,nominalratio1:10,250rpm and5mLsampling, dilution/filtering/AAS, duplicateaverages. Record explicitly preserves conflicting optimizationarms, unspecifiedratio units and lack of fullmassbalance/control/productpurity.

### Source conflicts remain visible without causal inflation

consistency: supported. Targets: cmmmech:ferrochrome-slag.

Source conflicts remain visible without causal inflation

The88.2%claim is clearly author-reported and unreconciled withFigure4.350/250rpm,150-to180called15min and activation-energy disagreements retained. SCMfits are not independent proof of molecular control, and suggested silicaprecipitation/Mgadsorption is not direct phasecharacterization.

### Synthetic biology results are correctly excluded from slag mechanism

scope: supported. Targets: cmmmech:ferrochrome-slag.

Synthetic biology results are correctly excluded from slag mechanism

Bansal2017 describes K2CrO4 in BMM with glucose andaddedFe salts/culture. Actual solid slag or derivedleachate treatment is unestablished. No taxon or microbial mechanism is transferred; industrialfeed provenance does not elevate laboratory extraction to deployment.

### Previously incorrect source locators are corrected

provenance: supported. Targets: cmmmech:ferrochrome-slag.

Both minor provenance findings are resolved in maintained input.

Final first support now identifies the abstract as the full selected-condition source and Section3.3 as88.2%/150min support. Both Bansal references now point to actual inspected Sections 2.1–2.3 and 3.1–3.4 rather than nonexistent Section 2.4. The original source contradictions remain unchanged.

### Final histories and validation match reviewed bytes

provenance: supported. Targets: cmmmech:ferrochrome-slag.

Actual CREATE and EDIT histories, final owner and terminal gate agree.

New EDIT provenance supplements the original CREATE; no existing history or review was rewritten. Named and full batch checks passed on the final owner hash.

## Findings

### F107-SLAG-1: The 2022 conclusion is not the claimed numerical-result locator

minor / resolved / confirmed; issue key: round107-ferrochrome-moyo-result-locator.

The first support explanation attributes88.2% and the full selected condition set to the abstract,§3.3 and conclusion. In the exact originalXML/HTML, the abstract supplies the full tuple and§3.3 reports88.2% at150min, while§4 has neither88.2% nor that tuple. Correct the locator without changing the qualified experimental interpretation.

Disposition: Root corrected the cited section locations in the maintained owner, appended actual EDIT history, and the reviewer independently matched final bytes to the primary originals. Exact original finding occurrence is retained.

### F107-SLAG-2: The simulated-slag source has no Section2.4

minor / resolved / confirmed; issue key: round107-ferrochrome-bansal-methods-locator.

Both the Bansal2017 source title and context-only explanation cite§2.1–2.4. The original has§2.1–2.3 followed by§3; stockK2CrO4 is§2.3, cultureisolation§3.1 and glucose/Fe/batchprotocol§3.4. Cite these inspected locations rather than a nonexistentsection. The exclusion of actual slag treatment is supported and remains appropriate.

Disposition: Root corrected the cited section locations in the maintained owner, appended actual EDIT history, and the reviewer independently matched final bytes to the primary originals. Exact original finding occurrence is retained.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ferrochrome-slag.yaml; Complete native-inspected maintained YAML. | supports | Final exact owner independently inspected; both previously confirmed citation-locator defects are corrected and all qualified scientific boundaries retained. |
| history | history/records/ferrochrome-slag/2026-10-16T003844Z-codex-41610f.yaml; Canonical CREATE sidecar and separate inline event. | supports | Actual GPT-6/codex actor, current time, exact owner and performed scope agree. |
| moyo | https://pmc.ncbi.nlm.nih.gov/articles/PMC9791875/; Retained complete original XML and HTML, abstract, Sections1–4, Tables1–2, equations and declarations; acquired by curator, independently read by reviewer. | supports | Actual slag source, abiotic HCl extraction, duplicates and source contradictions support the narrowed mechanism; Section4 does not contain88.2% or the stated condition tuple. |
| figures | /private/tmp/cmm-round107-uranium-research/slag-review-figure-manifest.json; All8originalJPEGs, especially Figures3–4 and8 independently viewed. | supports | Figure4 temperature-series response is lower than claimed88.2%; Figure8 line labels support the retained activation-energy conflict. No numbers digitized. |
| bansal | https://www.aidic.it/cet/17/61/007.pdf; All six original pages55–60 independently read and visually inspected; §2.3 stockchromate and §3.4 batches. | supports | Synthetic K2CrO4/BMM/glucose/Fe-salt culture experiment does not establish actual slag treatment. Sections2.1–2.3 are followed by3.1; there is no2.4. |
| metadata | https://pubmed.ncbi.nlm.nih.gov/36578389/; Live PubMed metadata and retained PubMedXML/Crossref; live CET article landing and official programme. | supports | DOI/PMID/PMCID for2022 agree with original; CET DOI/title/authors/year61:55–60 agree. No constituent identity or criticality inherited. |
| search | /private/tmp/cmm-round107-uranium-research/slag-review-web.txt; Exact DOI correction/erratum/retraction returned result sets and live authority check. | context_only | No relevant notice verified in the bounded primary authorities. A generic translated aggregator label is not treated as authoritative retraction evidence. Live PMC opening returned a browser challenge; retained originalXML/HTML inspected. |
| dedup | /private/tmp/cmm-round107-uranium-research/slag-review-dedup.json; Hidden/ignored/followed current records,research,reviews,histories, original records/ignoredreports and current rawsource root. | context_only | Only current ferrochrome owner identified within the declared roots; generic chromite, tailings and processing residue remain conceptually distinct. |
| validation | /private/tmp/cmm-round107-uranium-research/slag-review-successor-validation.json; Actual successor named validation receipt. | supports | Affected final owner independently passed named strict validation; full terminal batch evidence is recorded separately. |
| edit_history | history/records/ferrochrome-slag/2026-10-16T004334Z-codex-0dd330.yaml; New immutable EDIT sidecar and its attached history reference. | supports | Actual locator corrections and linked corrective issue are described with correct actor and target. |
| prior | reviews/structured/20261016T004158Z-ferrochrome-slag-round107-initial-independent/review.yaml; Exact initial native observation and its two finding identities. | supports | Original findings remain immutable and are explicitly resolved here after maintained corrections. |
| batch | /private/tmp/cmm-round107-final-gates.json; Coordinator terminal four-command receipt, exact owner input hash and retained log checksum independently verified. | supports | All required batch commands exited0; no redundant reviewer corpus execution claimed. |

## Limits And Additional Notes

- The source-level numerical and arm inconsistencies remain unresolved;88.2% is author-reported, not independently reconciled with Figure4.
- No unique molecular rate-control mechanism, isolated Mg product, validated selectivity, industrial deployment or actual microbial slag treatment is established.
- No new laboratory replication, raw-data request, graph digitization or review of the separate2023struvite experiment.
- Live PMC opening returned a challenge during original review; retained complete XML/HTML and official figures were independently inspected, with fresh PubMed/CET authority checks. Bounded correction searches do not establish global absence.
- Two minor prior findings resolved; zero unresolved record findings. Initial review remains immutable.
- The final batch receipt is a completed coordinator execution independently verified by this reviewer, not a duplicated local gate run.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T005243Z-ferrochrome-slag-round107-successor-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent successor scientific review of ferrochrome slag
started_at: '2026-10-16T00:44:40.036200Z'
finished_at: '2026-10-16T00:52:43.757415Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored and corrected this owner/history. Reviewer authored
    unrelated uranophane/parauranophane records, independently inspected the original
    articles and graphics, saved the initial two findings and reassessed exact corrections
    without editing this owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The two citation-locator defects are corrected in maintained input with append-only
  EDIT history. The final scoped abiotic extraction record is supported with the original
  source contradictions retained.
source:
  git_revision: 27d842b3e6239bf60565f93c958d3f2cad395037
  state: working_tree
  inputs:
  - path: data/records/ferrochrome-slag.yaml
    sha256: e0fb45e628bffe1b413f06a098f54ad34c4fe47e094d2b35880cef9a7a28e9c9
    role: target
  - path: history/records/ferrochrome-slag/2026-10-16T003844Z-codex-41610f.yaml
    sha256: e27207fd82cfcb95e796a504160e13267b4659837d0bde12d00b1f7df4d7d964
    role: context
  - path: history/records/ferrochrome-slag/2026-10-16T004334Z-codex-0dd330.yaml
    sha256: 8cec3268c4203182722f02ab3dc7f5c467768fbfa94090ac9e38177c3a1b49f0
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:ferrochrome-slag
  path: data/records/ferrochrome-slag.yaml
  label: Ferrochrome slag
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
scope:
  description: Complete final maintained owner, original CREATE and new EDIT histories;
    independent reassessment of changed locators and unchanged scientific scope.
  selection: Assigned single owner; nativeinspect captured before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ferrochrome-slag
checks:
- check_id: named
  name: Independent final named strict validation
  status: passed
  required: true
  summary: 'Checked 1 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked cmmmech validate data/records/ferrochrome-slag.yaml --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: batch1
  name: Coordinator completed batch command 1
  status: passed
  required: true
  summary: Terminal receipt and log digest independently checked; actual command exit0.
  target_ids:
  - cmmmech:ferrochrome-slag
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Coordinator completed batch command 2
  status: passed
  required: true
  summary: Terminal receipt and log digest independently checked; actual command exit0.
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Coordinator completed batch command 3
  status: passed
  required: true
  summary: Terminal receipt and log digest independently checked; actual command exit0.
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked cmmmech validate-history --base 27d842b3e6239bf60565f93c958d3f2cad395037
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch4
  name: Coordinator completed batch command 4
  status: passed
  required: true
  summary: Terminal receipt and log digest independently checked; actual command exit0.
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ferrochrome-slag.yaml
  locator: Complete native-inspected maintained YAML.
  summary: Final exact owner independently inspected; both previously confirmed citation-locator
    defects are corrected and all qualified scientific boundaries retained.
  accessed_at: '2026-10-16T00:52:43.757415Z'
  support: supports
  snapshot_sha256: e0fb45e628bffe1b413f06a098f54ad34c4fe47e094d2b35880cef9a7a28e9c9
- evidence_id: history
  kind: record_content
  reference: history/records/ferrochrome-slag/2026-10-16T003844Z-codex-41610f.yaml
  locator: Canonical CREATE sidecar and separate inline event.
  summary: Actual GPT-6/codex actor, current time, exact owner and performed scope
    agree.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: e27207fd82cfcb95e796a504160e13267b4659837d0bde12d00b1f7df4d7d964
- evidence_id: moyo
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9791875/
  locator: Retained complete original XML and HTML, abstract, Sections1–4, Tables1–2,
    equations and declarations; acquired by curator, independently read by reviewer.
  summary: Actual slag source, abiotic HCl extraction, duplicates and source contradictions
    support the narrowed mechanism; Section4 does not contain88.2% or the stated condition
    tuple.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: 22d1c3a7679829e7558f663581e7f3f6b9f89646486b00b5aabace7f4185057b
- evidence_id: figures
  kind: primary_source
  reference: /private/tmp/cmm-round107-uranium-research/slag-review-figure-manifest.json
  locator: All8originalJPEGs, especially Figures3–4 and8 independently viewed.
  summary: Figure4 temperature-series response is lower than claimed88.2%; Figure8
    line labels support the retained activation-energy conflict. No numbers digitized.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: 29218daf1cd76d407e4a26f732f1fe55ee74f6939d60ef62056c515190b7d943
- evidence_id: bansal
  kind: primary_source
  reference: https://www.aidic.it/cet/17/61/007.pdf
  locator: All six original pages55–60 independently read and visually inspected;
    §2.3 stockchromate and §3.4 batches.
  summary: Synthetic K2CrO4/BMM/glucose/Fe-salt culture experiment does not establish
    actual slag treatment. Sections2.1–2.3 are followed by3.1; there is no2.4.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: 9e721dd7acec3ff13aea6b3466d908a33d0e243f0d1c593a400ef32a4789d32a
- evidence_id: metadata
  kind: authority
  reference: https://pubmed.ncbi.nlm.nih.gov/36578389/
  locator: Live PubMed metadata and retained PubMedXML/Crossref; live CET article
    landing and official programme.
  summary: DOI/PMID/PMCID for2022 agree with original; CET DOI/title/authors/year61:55–60
    agree. No constituent identity or criticality inherited.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: 2e1dbce83850a4631de9a8dc80f798aae036fd91fd27822e80a010717bb95d63
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round107-uranium-research/slag-review-web.txt
  locator: Exact DOI correction/erratum/retraction returned result sets and live authority
    check.
  summary: No relevant notice verified in the bounded primary authorities. A generic
    translated aggregator label is not treated as authoritative retraction evidence.
    Live PMC opening returned a browser challenge; retained originalXML/HTML inspected.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: context_only
  snapshot_sha256: 8ac1119de14082d75dd6ce3e94a53456bfd83c428ecbaec7f8c79bf9f94fa81f
  search_scope: Live exactDOI queries with correction/erratum/retraction terms; first
    returned result sets. PubMedXML has no CommentsCorrections and Crossref has no
    update/relation notice. This does not prove universal absence.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round107-uranium-research/slag-review-dedup.json
  locator: Hidden/ignored/followed current records,research,reviews,histories, original
    records/ignoredreports and current rawsource root.
  summary: Only current ferrochrome owner identified within the declared roots; generic
    chromite, tailings and processing residue remain conceptually distinct.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: context_only
  snapshot_sha256: a9cb41240f0e5e01bfacfdcac976faaedb1960d8199914ad8fe659db0b106d5a
  search_scope: rg --no-ignore --hidden --follow across the exact roots retained in
    the receipt, exit0 and no stderr; binary documents not exhaustively indexed, no
    machine-wide absence claim.
- evidence_id: validation
  kind: validation
  reference: /private/tmp/cmm-round107-uranium-research/slag-review-successor-validation.json
  locator: Actual successor named validation receipt.
  summary: Affected final owner independently passed named strict validation; full
    terminal batch evidence is recorded separately.
  accessed_at: '2026-10-16T00:52:43.757415Z'
  support: supports
  snapshot_sha256: d07ae58a40cff7a02f6961eb12d7b742ddeb8f67049af10063856296f0a9f8d3
- evidence_id: edit_history
  kind: record_content
  reference: history/records/ferrochrome-slag/2026-10-16T004334Z-codex-0dd330.yaml
  locator: New immutable EDIT sidecar and its attached history reference.
  summary: Actual locator corrections and linked corrective issue are described with
    correct actor and target.
  accessed_at: '2026-10-16T00:52:43.757415Z'
  support: supports
  snapshot_sha256: 8cec3268c4203182722f02ab3dc7f5c467768fbfa94090ac9e38177c3a1b49f0
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261016T004158Z-ferrochrome-slag-round107-initial-independent/review.yaml
  locator: Exact initial native observation and its two finding identities.
  summary: Original findings remain immutable and are explicitly resolved here after
    maintained corrections.
  accessed_at: '2026-10-16T00:52:43.757415Z'
  support: supports
  snapshot_sha256: ddd8925d4ec2837432950d3b9d2e742b2a54f211a7c442542dd0f8d90b7bf7ce
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round107-final-gates.json
  locator: Coordinator terminal four-command receipt, exact owner input hash and retained
    log checksum independently verified.
  summary: All required batch commands exited0; no redundant reviewer corpus execution
    claimed.
  accessed_at: '2026-10-16T00:52:43.757415Z'
  support: supports
  snapshot_sha256: 9ecba8d70f57d4bf2df433becdf3581dca4a634de4fd5294f1c66f4aaf6b1d4c
assessments:
- assessment_id: identity
  area: identity
  topic: Processing-defined secondary resource is supported
  outcome: supported
  summary: Processing-defined secondary resource is supported
  details: The Zimasco smelting slag is distinct from ore, beneficiation tailings,
    chemical-processing residue, alloy and constituentmineral. Table1 is oxide composition
    despite mineralogy/XRD wording;26.4%MgO is not26.4%Mg. No incorrect material identifier
    or criticality mapping.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - metadata
- assessment_id: methods
  area: evidence
  topic: Laboratory acid-extraction context is appropriately bounded
  outcome: supported
  summary: Laboratory acid-extraction context is appropriately bounded
  details: Source§2 specifies pulverized80%-passing75µm feed,1L vessel,500mL5/6MHCl,nominalratio1:10,250rpm
    and5mLsampling, dilution/filtering/AAS, duplicateaverages. Record explicitly preserves
    conflicting optimizationarms, unspecifiedratio units and lack of fullmassbalance/control/productpurity.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - figures
  dimensions:
  - name: material_form
    value: Pulverized ferrochrome smelting slag
    definition: Processing-derived sample from Zimasco, not chromite ore or pure Mg
      phase.
    evidence_ids:
    - owner
    - moyo
  - name: organism_biomass
    value: None in accepted mechanism
    definition: HCl extraction is abiotic; synthetic-solution culture study is context
      only.
    evidence_ids:
    - owner
    - bansal
  - name: scale
    value: Laboratory stirred vessel
    definition: Industrial waste origin does not establish industrial extraction deployment.
    evidence_ids:
    - owner
    - moyo
- assessment_id: causality
  area: consistency
  topic: Source conflicts remain visible without causal inflation
  outcome: supported
  summary: Source conflicts remain visible without causal inflation
  details: The88.2%claim is clearly author-reported and unreconciled withFigure4.350/250rpm,150-to180called15min
    and activation-energy disagreements retained. SCMfits are not independent proof
    of molecular control, and suggested silicaprecipitation/Mgadsorption is not direct
    phasecharacterization.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - figures
- assessment_id: biology
  area: scope
  topic: Synthetic biology results are correctly excluded from slag mechanism
  outcome: supported
  summary: Synthetic biology results are correctly excluded from slag mechanism
  details: Bansal2017 describes K2CrO4 in BMM with glucose andaddedFe salts/culture.
    Actual solid slag or derivedleachate treatment is unestablished. No taxon or microbial
    mechanism is transferred; industrialfeed provenance does not elevate laboratory
    extraction to deployment.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - bansal
- assessment_id: locators
  area: provenance
  topic: Previously incorrect source locators are corrected
  outcome: supported
  summary: Both minor provenance findings are resolved in maintained input.
  details: Final first support now identifies the abstract as the full selected-condition
    source and Section3.3 as88.2%/150min support. Both Bansal references now point
    to actual inspected Sections 2.1–2.3 and 3.1–3.4 rather than nonexistent Section
    2.4. The original source contradictions remain unchanged.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - bansal
  - edit_history
  - prior
- assessment_id: final_checks
  area: provenance
  topic: Final histories and validation match reviewed bytes
  outcome: supported
  summary: Actual CREATE and EDIT histories, final owner and terminal gate agree.
  details: New EDIT provenance supplements the original CREATE; no existing history
    or review was rewritten. Named and full batch checks passed on the final owner
    hash.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - history
  - edit_history
  - validation
  - batch
findings:
- finding_id: F107-SLAG-1
  issue_key: round107-ferrochrome-moyo-result-locator
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: The 2022 conclusion is not the claimed numerical-result locator
  description: The first support explanation attributes88.2% and the full selected
    condition set to the abstract,§3.3 and conclusion. In the exact originalXML/HTML,
    the abstract supplies the full tuple and§3.3 reports88.2% at150min, while§4 has
    neither88.2% nor that tuple. Correct the locator without changing the qualified
    experimental interpretation.
  target_ids:
  - cmmmech:ferrochrome-slag
  field_paths:
  - mechanisms[0].evidence[0].explanation
  evidence_ids:
  - owner
  - moyo
  - edit_history
  - prior
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261016T004158Z-ferrochrome-slag-round107-initial-independent
    finding_id: F107-SLAG-1
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/424
  disposition_reason: Root corrected the cited section locations in the maintained
    owner, appended actual EDIT history, and the reviewer independently matched final
    bytes to the primary originals. Exact original finding occurrence is retained.
- finding_id: F107-SLAG-2
  issue_key: round107-ferrochrome-bansal-methods-locator
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: The simulated-slag source has no Section2.4
  description: Both the Bansal2017 source title and context-only explanation cite§2.1–2.4.
    The original has§2.1–2.3 followed by§3; stockK2CrO4 is§2.3, cultureisolation§3.1
    and glucose/Fe/batchprotocol§3.4. Cite these inspected locations rather than a
    nonexistentsection. The exclusion of actual slag treatment is supported and remains
    appropriate.
  target_ids:
  - cmmmech:ferrochrome-slag
  field_paths:
  - sources[1].title
  - mechanisms[0].evidence[4].explanation
  evidence_ids:
  - owner
  - bansal
  - edit_history
  - prior
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
  previous_occurrences:
  - repository: CultureBotAI/CMMMech
    review_id: 20261016T004158Z-ferrochrome-slag-round107-initial-independent
    finding_id: F107-SLAG-2
  external_issues:
  - https://github.com/CultureBotAI/CMMMech/issues/424
  disposition_reason: Root corrected the cited section locations in the maintained
    owner, appended actual EDIT history, and the reviewer independently matched final
    bytes to the primary originals. Exact original finding occurrence is retained.
actions: []
limitations:
- The source-level numerical and arm inconsistencies remain unresolved;88.2% is author-reported,
  not independently reconciled with Figure4.
- No unique molecular rate-control mechanism, isolated Mg product, validated selectivity,
  industrial deployment or actual microbial slag treatment is established.
- No new laboratory replication, raw-data request, graph digitization or review of
  the separate2023struvite experiment.
- Live PMC opening returned a challenge during original review; retained complete
  XML/HTML and official figures were independently inspected, with fresh PubMed/CET
  authority checks. Bounded correction searches do not establish global absence.
notes:
- Two minor prior findings resolved; zero unresolved record findings. Initial review
  remains immutable.
- The final batch receipt is a completed coordinator execution independently verified
  by this reviewer, not a duplicated local gate run.
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261016T004158Z-ferrochrome-slag-round107-initial-independent
  relationship: Successor resolves both exact minor locator findings after maintained
    corrections.
links:
- https://github.com/CultureBotAI/CMMMech/issues/424
```
