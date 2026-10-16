# Initial independent scientific review of ferrochrome slag

- Review: 20261016T004158Z-ferrochrome-slag-round107-initial-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T00:39:40.781676Z
- Finished UTC: 2026-10-16T00:41:58.833796Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The scoped abiotic slag-extraction mechanism is supported, with two minor citation-locator defects requiring correction and final batch checks pending.

## Scope And Provenance

Complete current maintained owner, canonicalCREATE and exact primary material/experimental scope.

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
| Independent named validation | passed | True | cmmmech:ferrochrome-slag | Checked 1 record(s); 0 failed. |
| Independent history validation | passed | True | cmmmech:ferrochrome-slag | Checked 606 history record(s); 0 error(s). |
| Completed batch just check and strict corpus validation | unavailable | True | cmmmech:ferrochrome-slag | Coordinator final batch has not completed for these new owners at this initial finding observation; no passing batch claim. |

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

### Two source-locator defects require correction

provenance: concern. Targets: cmmmech:ferrochrome-slag.

Two source-locator defects require correction

The2022conclusion is incorrectly listed as the88.2%/condition locator, and the2017source refers to nonexistent§2.4 instead of the actual§2.3/3.4 experimental sections. Scientific interpretation can remain unchanged.

## Findings

### F107-SLAG-1: The 2022 conclusion is not the claimed numerical-result locator

minor / open / confirmed; issue key: round107-ferrochrome-moyo-result-locator.

The first support explanation attributes88.2% and the full selected condition set to the abstract,§3.3 and conclusion. In the exact originalXML/HTML, the abstract supplies the full tuple and§3.3 reports88.2% at150min, while§4 has neither88.2% nor that tuple. Correct the locator without changing the qualified experimental interpretation.

### F107-SLAG-2: The simulated-slag source has no Section2.4

minor / open / confirmed; issue key: round107-ferrochrome-bansal-methods-locator.

Both the Bansal2017 source title and context-only explanation cite§2.1–2.4. The original has§2.1–2.3 followed by§3; stockK2CrO4 is§2.3, cultureisolation§3.1 and glucose/Fe/batchprotocol§3.4. Cite these inspected locations rather than a nonexistentsection. The exclusion of actual slag treatment is supported and remains appropriate.

## Recommended Actions And Acceptance Checks

### correct_source_locators

Correct only supported evidence locators in the maintained owner and append actual EDIT history.

- Cite abstract for the complete88.2% conditiontuple and§3.3 for88.2%/150min, removing the false§4 attribution.
- Replace both§2.1–2.4 references with exact inspected§2.3/§3.1–3.4 locations.
- Keep all qualified results, source conflicts, nonmicrobial scope and deployment limits.
- Run affected named/history checks and complete batch gates, then save an independent successor with exact previous finding occurrences and finalownerhash.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/ferrochrome-slag.yaml; Complete native-inspected maintained YAML. | supports | Resource scope and experiment claims inspected; two bounded source-locator defects confirmed. |
| history | history/records/ferrochrome-slag/2026-10-16T003844Z-codex-41610f.yaml; Canonical CREATE sidecar and separate inline event. | supports | Actual GPT-6/codex actor, current time, exact owner and performed scope agree. |
| moyo | https://pmc.ncbi.nlm.nih.gov/articles/PMC9791875/; Retained complete original XML and HTML, abstract, Sections1–4, Tables1–2, equations and declarations; acquired by curator, independently read by reviewer. | supports | Actual slag source, abiotic HCl extraction, duplicates and source contradictions support the narrowed mechanism; Section4 does not contain88.2% or the stated condition tuple. |
| figures | /private/tmp/cmm-round107-uranium-research/slag-review-figure-manifest.json; All8originalJPEGs, especially Figures3–4 and8 independently viewed. | supports | Figure4 temperature-series response is lower than claimed88.2%; Figure8 line labels support the retained activation-energy conflict. No numbers digitized. |
| bansal | https://www.aidic.it/cet/17/61/007.pdf; All six original pages55–60 independently read and visually inspected; §2.3 stockchromate and §3.4 batches. | supports | Synthetic K2CrO4/BMM/glucose/Fe-salt culture experiment does not establish actual slag treatment. Sections2.1–2.3 are followed by3.1; there is no2.4. |
| metadata | https://pubmed.ncbi.nlm.nih.gov/36578389/; Live PubMed metadata and retained PubMedXML/Crossref; live CET article landing and official programme. | supports | DOI/PMID/PMCID for2022 agree with original; CET DOI/title/authors/year61:55–60 agree. No constituent identity or criticality inherited. |
| search | /private/tmp/cmm-round107-uranium-research/slag-review-web.txt; Exact DOI correction/erratum/retraction returned result sets and live authority check. | context_only | No relevant notice verified in the bounded primary authorities. A generic translated aggregator label is not treated as authoritative retraction evidence. Live PMC opening returned a browser challenge; retained originalXML/HTML inspected. |
| dedup | /private/tmp/cmm-round107-uranium-research/slag-review-dedup.json; Hidden/ignored/followed current records,research,reviews,histories, original records/ignoredreports and current rawsource root. | context_only | Only current ferrochrome owner identified within the declared roots; generic chromite, tailings and processing residue remain conceptually distinct. |
| validation | /private/tmp/cmm-round107-uranium-research/slag-review-initial-validation.json; Actual named/history executions independently completed. | supports | One owner passed strict validation;606histories passed at the stated base. Final batch gates remain pending. |

## Limits And Additional Notes

- Finalbatchchecks are pending, so this is a partial observation rather than a passing completed review.
- No new laboratory replication, rawdata request, graph digitization or primary2023struvite reassessment. Source-level inconsistencies remain unresolved and explicitly narrow the owner.
- LivePMC route returned a challenge; original fullXML/HTML and officialfigures acquired bycurator were independently inspected, with freshPubMed/CET authority checks.
- Initial owner/hash remains unchanged until native finding bundle is saved. No Git or GitHub mutation by reviewer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T004158Z-ferrochrome-slag-round107-initial-independent
kind: record
repository: CultureBotAI/CMMMech
title: Initial independent scientific review of ferrochrome slag
started_at: '2026-10-16T00:39:40.781676Z'
finished_at: '2026-10-16T00:41:58.833796Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this owner/history; reviewer authored the unrelated
    uranophane/parauranophane pair, independently read original evidence and graphics,
    and made no target/history edits.
skill: .claude/skills/review-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The scoped abiotic slag-extraction mechanism is supported, with two minor
  citation-locator defects requiring correction and final batch checks pending.
source:
  git_revision: 27d842b3e6239bf60565f93c958d3f2cad395037
  state: working_tree
  inputs:
  - path: data/records/ferrochrome-slag.yaml
    sha256: a5c480b3e78f6c27ea790f4aaf365935b87faa1d0419f1aadb3f1d71ec38ee11
    role: target
  - path: history/records/ferrochrome-slag/2026-10-16T003844Z-codex-41610f.yaml
    sha256: e27207fd82cfcb95e796a504160e13267b4659837d0bde12d00b1f7df4d7d964
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
  description: Complete current maintained owner, canonicalCREATE and exact primary
    material/experimental scope.
  selection: Assigned single owner; nativeinspect captured before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:ferrochrome-slag
checks:
- check_id: named
  name: Independent named validation
  status: passed
  required: true
  summary: Checked 1 record(s); 0 failed.
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked cmmmech validate data/records/ferrochrome-slag.yaml --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: history
  name: Independent history validation
  status: passed
  required: true
  summary: Checked 606 history record(s); 0 error(s).
  target_ids:
  - cmmmech:ferrochrome-slag
  command: uv run --locked cmmmech validate-history --base 27d842b3e6239bf60565f93c958d3f2cad395037
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: final_batch
  name: Completed batch just check and strict corpus validation
  status: unavailable
  required: true
  summary: Coordinator final batch has not completed for these new owners at this
    initial finding observation; no passing batch claim.
  target_ids:
  - cmmmech:ferrochrome-slag
  scope_note: Retain initial findings now; independent successor will verify terminal
    batch evidence.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/ferrochrome-slag.yaml
  locator: Complete native-inspected maintained YAML.
  summary: Resource scope and experiment claims inspected; two bounded source-locator
    defects confirmed.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: a5c480b3e78f6c27ea790f4aaf365935b87faa1d0419f1aadb3f1d71ec38ee11
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
  reference: /private/tmp/cmm-round107-uranium-research/slag-review-initial-validation.json
  locator: Actual named/history executions independently completed.
  summary: One owner passed strict validation;606histories passed at the stated base.
    Final batch gates remain pending.
  accessed_at: '2026-10-16T00:41:58.833796Z'
  support: supports
  snapshot_sha256: 6677e7fdaf75ea5bcf7e4a1e9d07ba667867601cff5cceeaa5cd71818d3bcd62
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
  topic: Two source-locator defects require correction
  outcome: concern
  summary: Two source-locator defects require correction
  details: The2022conclusion is incorrectly listed as the88.2%/condition locator,
    and the2017source refers to nonexistent§2.4 instead of the actual§2.3/3.4 experimental
    sections. Scientific interpretation can remain unchanged.
  target_ids:
  - cmmmech:ferrochrome-slag
  evidence_ids:
  - owner
  - moyo
  - bansal
findings:
- finding_id: F107-SLAG-1
  issue_key: round107-ferrochrome-moyo-result-locator
  category: provenance
  severity: minor
  status: open
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
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
- finding_id: F107-SLAG-2
  issue_key: round107-ferrochrome-bansal-methods-locator
  category: provenance
  severity: minor
  status: open
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
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
actions:
- action_id: correct_source_locators
  description: Correct only supported evidence locators in the maintained owner and
    append actual EDIT history.
  finding_ids:
  - F107-SLAG-1
  - F107-SLAG-2
  target_ids:
  - cmmmech:ferrochrome-slag
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/ferrochrome-slag.yaml
    role: maintained_record
  acceptance_checks:
  - Cite abstract for the complete88.2% conditiontuple and§3.3 for88.2%/150min, removing
    the false§4 attribution.
  - Replace both§2.1–2.4 references with exact inspected§2.3/§3.1–3.4 locations.
  - Keep all qualified results, source conflicts, nonmicrobial scope and deployment
    limits.
  - Run affected named/history checks and complete batch gates, then save an independent
    successor with exact previous finding occurrences and finalownerhash.
limitations:
- Finalbatchchecks are pending, so this is a partial observation rather than a passing
  completed review.
- No new laboratory replication, rawdata request, graph digitization or primary2023struvite
  reassessment. Source-level inconsistencies remain unresolved and explicitly narrow
  the owner.
- LivePMC route returned a challenge; original fullXML/HTML and officialfigures acquired
  bycurator were independently inspected, with freshPubMed/CET authority checks.
notes:
- Initial owner/hash remains unchanged until native finding bundle is saved. No Git
  or GitHub mutation by reviewer.
```
