# Independent pig-manure scientific review

- Review: 20261015T104328Z-pig-manure-round93-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-15T10:33:55.381017Z
- Finished UTC: 2026-10-15T10:43:28.784688Z
- Reviewer: codex /root/round68_phosphates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The secondary-resource identity and conditional enrichment-associated mobilization are supported. Nutrient losses, unresolved community, missing controls, assay conflicts and absence of recovered products are accurately bounded; no corrective finding.

## Scope And Provenance

Full current pig-manure record, canonical CREATE and paired dossier against complete accepted primary and authority evidence.

Selection: Explicit root-assigned new secondary-resource record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:pig-manure | data/records/pig-manure.yaml | maintained | Pig manure |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent original text, graphics and authority review | passed | True | cmmmech:pig-manure | Complete original JATS/HTML, all7 figures/all6 tables and exact authority/history checked. |
| Named structural validation | passed | True | cmmmech:pig-manure | Checked1record;0failed. |
| Completed batch command 1 | passed | True | cmmmech:pig-manure | Actual root execution verified through terminal receipt and log hash. |
| Completed batch command 2 | passed | True | cmmmech:pig-manure | Actual root execution verified through terminal receipt and log hash. |
| Completed batch command 3 | passed | True | cmmmech:pig-manure | Actual root execution verified through terminal receipt and log hash. |
| Completed batch command 4 | passed | True | cmmmech:pig-manure | Actual root execution verified through terminal receipt and log hash. |

## Scientific And Domain Assessments

### Real unincinerated agricultural feed

identity: supported. Targets: cmmmech:pig-manure.

The farm sample and diluted slurry are correctly one heterogeneous secondary resource, separate from ash, poultry and municipal sludge.

No mineral phase, criticality listing or isolated product identity is inferred.

### Culture-associated dose response with controls bounded

evidence: supported. Targets: cmmmech:pig-manure.

Methods and original figures support the reported dose response, with missing control and mass-balance limits explicit.

2%w/v slurry;200mL in500mL flasks;5%v/v active indigenous enrichment;2/5/8/10g/L elemental sulfur;28°C,180rpm,12days,triplicates. All reported arms inoculated; no matched sterile or zero-sulfur control. No species-specific mechanism assigned.

### Measured denominator and counterevidence

quantity: supported. Targets: cmmmech:pig-manure.

Source-reported metal solubilization is distinguished from isolated recovery, and residual nutrient decreases remain a tradeoff.

Cu48.5% at low dose is not replaced by high-dose endpoint. No sampling/inoculum/volume-corrected closed mass balance, fertilizer safety or industrial claim is accepted. Sequential fractions and empirical fits are operational proxies.

### Source contradictions and provenance

consistency: supported. Targets: cmmmech:pig-manure.

Time/unit/caption conflicts and incomplete species resolution are adequately retained.

Actual CREATE actor/time and inline event are distinct and valid. Original PDF route unavailable; official text plus original figures are the accepted route. Relevant review inputs were re-inspected using canonical repository labels before persistence; scientific hashes unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| main | https://doi.org/10.1016/j.heliyon.2018.e00778; Complete official JATS; sections2.1-2.4,3.1-3.5 and all6 original tables; local artifact /private/tmp/cmm-round93-resources-research/wei2018.xml | supports | Read full text and native table subtrees. Real farm manure, enrichment preparation, triplicate flask conditions and conditional solubilization/nutrient tradeoffs match the record. All dose arms inoculated; no sterile/no-sulfur series demonstrated. |
| html | https://pmc.ncbi.nlm.nih.gov/articles/PMC6129760/; Complete official PMC HTML and captions; local artifact /private/tmp/cmm-round93-resources-research/wei2018-pmc.html | supports | Independent official text corroboration; missing PDF is disclosed and no PDF page inspection claimed. |
| fig1 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure1; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr1.jpg | supports | Dose-dependent pH/ORP; original prose reverses crossing-time order, so exact crossing times are not accepted. |
| fig2 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure2; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr2.jpg | supports | Measured sulfate time courses; baseline and inoculum contribution not fully accounted. |
| fig3 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure3; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr3.jpg | supports | Empirical rate fit; it is not direct growth or causal enzyme evidence. |
| fig4 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure4; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr4.jpg | supports | Original Cu/Zn/Mn liquid solubilization curves; low-dose Cu endpoint48.5%, higher-dose near90%+ and diminishing8-to10g/L benefit. No isolated product. |
| fig5 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure5; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr5.jpg | supports | Empirical Cu rate fit, not an independently demonstrated molecular mechanism. |
| fig6 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure6; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr6.jpg | supports | Operational sequential extraction fractions; dose of after-treatment panel unspecified, not direct mineral or redox speciation. |
| fig7 | https://doi.org/10.1016/j.heliyon.2018.e00778; Original Figure7; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr7.jpg | supports | Residual TN/TP/K/TOC concentrations; caption nitrate/phosphate labels differ from axes/methods, and concentration change is not nutrient recovery yield. |
| taxonomy | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930; TaxId930, ScientificName, Rank; local artifact /private/tmp/cmm-round93-resources-research/ncbi930.xml | context_only | Current reference species Acidithiobacillus thiooxidans is species-rank;98% clone similarity from a separate enrichment does not establish the assay consortium identity. |
| named | Actual reviewer named validation; Completed named command; local artifact /private/tmp/cmm-round93-pig-independent/named-validation.log | supports | Checked1record;0failed. |
| batch | Actual root round93 terminal four-command gate; /private/tmp/cmm-round93-initial-gates.json; log /private/tmp/cmm-round93-initial-gates.log SHA256 93e8686db07b65d1fd2c5c636df051e0e00707251abae92a4ebc65c23b745d11; local artifact /private/tmp/cmm-round93-initial-gates.json | supports | All four actual commands exited0 with exact owner bytes unchanged. These are structural/provenance checks, not scientific proof. |
| search | Reviewer bounded live correction/counterevidence search; 2026-10-15 web queries and local scope dedup; local artifact /private/tmp/cmm-round93-pig-independent/scope-dedup.txt | context_only | Exact DOI correction/retraction/erratum and pig-manure sulfur-concentration queries returned the accepted article and related studies, without an attributable notice in those results. Related biochar/iron studies are not transferred. Hidden/ignored/followed current-owner scope search supports distinct resource boundary. |

## Limits And Additional Notes

- No matched sterile, uninoculated, no-sulfur or acidity-matched control.
- No complete metal/nutrient mass balance or isolated recovered product; final volume and sampling corrections unresolved.
- Only98% sequence similarity from a separate salt-medium enrichment; no confirmed experimental species/strain.
- Original PDF unavailable; complete official JATS/HTML and all original main graphics inspected instead. No separate SI announced in that original.
- Bounded correction/counterevidence searches do not prove global absence of notices or studies.
- Early unsaved inspect preparation used URL-form owner repository labels; canonical labels were recaptured with unchanged hashes before persistence.
- Unsaved schema-format drafts used UTC +00:00 and, for corkite, a colon in the proposed issue key; normalized to native Z timestamps and permitted key characters before persistence, without changing the observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T104328Z-pig-manure-round93-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent pig-manure scientific review
started_at: '2026-10-15T10:33:55.381017Z'
finished_at: '2026-10-15T10:43:28.784688Z'
reviewer:
  identity: codex /root/round68_phosphates
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Frontier agent authored pig-manure. Reviewer authored separate
    lithium-phosphate records, did not edit this owner/history, and captured native
    inspection before independent source assessment.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The secondary-resource identity and conditional enrichment-associated mobilization
  are supported. Nutrient losses, unresolved community, missing controls, assay conflicts
  and absence of recovered products are accurately bounded; no corrective finding.
source:
  git_revision: e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d
  state: working_tree
  inputs:
  - path: data/records/pig-manure.yaml
    sha256: 20caf6979236a7b9464da8e1f43fe1f95547f7d8cc0dc2576ff6b676f418a124
    role: target
  - path: history/records/pig-manure/2026-10-15T103022Z-codex-0ab705.yaml
    sha256: afb4ad70190451f8c3dcfd9b5e0f0e801713c9c8dadbadc545c2aa0c29921681
    role: context
  - path: research/sources/round93-resources/20261015T103216Z-source-investigation.json
    sha256: be589a2caf5b0ed7245ac5da92a5894efe33c71f45c06a1138f23fab0244775d
    role: context
  - path: research/sources/round93-resources/20261015T103216Z-source-investigation.md
    sha256: eb88638cd11d87fe04b6e1a74a9e93dd6aa88e8a649bc0013cb9555ffc5ee985
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:pig-manure
  path: data/records/pig-manure.yaml
  label: Pig manure
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/pig-manure.yaml
    role: maintained_record
scope:
  description: Full current pig-manure record, canonical CREATE and paired dossier
    against complete accepted primary and authority evidence.
  selection: Explicit root-assigned new secondary-resource record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:pig-manure
checks:
- check_id: source
  name: Independent original text, graphics and authority review
  required: true
  status: passed
  summary: Complete original JATS/HTML, all7 figures/all6 tables and exact authority/history
    checked.
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - main
  - html
  - taxonomy
- check_id: named
  name: Named structural validation
  required: true
  status: passed
  summary: Checked1record;0failed.
  command: uv run --locked cmmmech validate --require-records data/records/pig-manure.yaml
  exit_code: 0
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - named
- check_id: batch0
  name: Completed batch command 1
  required: true
  status: passed
  summary: Actual root execution verified through terminal receipt and log hash.
  command: just check
  exit_code: 0
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - batch
- check_id: batch1
  name: Completed batch command 2
  required: true
  status: passed
  summary: Actual root execution verified through terminal receipt and log hash.
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - batch
- check_id: batch2
  name: Completed batch command 3
  required: true
  status: passed
  summary: Actual root execution verified through terminal receipt and log hash.
  command: uv run --locked cmmmech validate-history --base e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d
  exit_code: 0
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - batch
- check_id: batch3
  name: Completed batch command 4
  required: true
  status: passed
  summary: Actual root execution verified through terminal receipt and log hash.
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - batch
evidence:
- evidence_id: main
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Complete official JATS; sections2.1-2.4,3.1-3.5 and all6 original tables;
    local artifact /private/tmp/cmm-round93-resources-research/wei2018.xml
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Read full text and native table subtrees. Real farm manure, enrichment
    preparation, triplicate flask conditions and conditional solubilization/nutrient
    tradeoffs match the record. All dose arms inoculated; no sterile/no-sulfur series
    demonstrated.
  snapshot_sha256: d59cfd9fd2864a5ce09355907fba718240829d05616040046580f22078fbea20
- evidence_id: html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6129760/
  locator: Complete official PMC HTML and captions; local artifact /private/tmp/cmm-round93-resources-research/wei2018-pmc.html
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Independent official text corroboration; missing PDF is disclosed and no
    PDF page inspection claimed.
  snapshot_sha256: f75149f8e0ae6920f6a7931e809c66ef0741fb9fe23b25c2b34ee06cbcb7e5f1
- evidence_id: fig1
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure1; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr1.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Dose-dependent pH/ORP; original prose reverses crossing-time order, so
    exact crossing times are not accepted.
  snapshot_sha256: a2b3b21aa5e4d767caa8a5b4b9127b992995749d4b771298af2f5bc8a053148d
- evidence_id: fig2
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure2; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr2.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Measured sulfate time courses; baseline and inoculum contribution not fully
    accounted.
  snapshot_sha256: be2f6a33e0b1b34defe03e6f9f249cba269710f415118bf9120fa2968ce426f4
- evidence_id: fig3
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure3; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr3.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Empirical rate fit; it is not direct growth or causal enzyme evidence.
  snapshot_sha256: f8231bbf1ce0eb9f5c7b1ae0925ade6db4332c6490edd366484d04ed7afa6817
- evidence_id: fig4
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure4; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr4.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Original Cu/Zn/Mn liquid solubilization curves; low-dose Cu endpoint48.5%,
    higher-dose near90%+ and diminishing8-to10g/L benefit. No isolated product.
  snapshot_sha256: 2b75046dc7eb53d18de7ccc49e61b123608f7deb04f2e0db556df65c69c13ef7
- evidence_id: fig5
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure5; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr5.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Empirical Cu rate fit, not an independently demonstrated molecular mechanism.
  snapshot_sha256: 094bb6da8b083ee17f60f060e4b92e2b590e17afee01de7293dd418f75726599
- evidence_id: fig6
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure6; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr6.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Operational sequential extraction fractions; dose of after-treatment panel
    unspecified, not direct mineral or redox speciation.
  snapshot_sha256: 01106403196341a217eae8e8b682b033befffbdbf55cde1741fa3e9f3a58a2b1
- evidence_id: fig7
  kind: primary_source
  reference: https://doi.org/10.1016/j.heliyon.2018.e00778
  locator: Original Figure7; local artifact /private/tmp/cmm-round93-resources-research/wei2018-assets/gr7.jpg
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Residual TN/TP/K/TOC concentrations; caption nitrate/phosphate labels differ
    from axes/methods, and concentration change is not nutrient recovery yield.
  snapshot_sha256: 6a225c2947a3b862e57673b070a7ffcdc73f5837441efb4b28bd6d35a6cbc101
- evidence_id: taxonomy
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930
  locator: TaxId930, ScientificName, Rank; local artifact /private/tmp/cmm-round93-resources-research/ncbi930.xml
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: context_only
  summary: Current reference species Acidithiobacillus thiooxidans is species-rank;98%
    clone similarity from a separate enrichment does not establish the assay consortium
    identity.
  snapshot_sha256: 1ac710626a004467c8fbe0248715cc6d01360e721fbdb8f681edd536c8fc1cbc
- evidence_id: named
  kind: validation
  reference: Actual reviewer named validation
  locator: Completed named command; local artifact /private/tmp/cmm-round93-pig-independent/named-validation.log
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: Checked1record;0failed.
  snapshot_sha256: 6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e
- evidence_id: batch
  kind: validation
  reference: Actual root round93 terminal four-command gate
  locator: /private/tmp/cmm-round93-initial-gates.json; log /private/tmp/cmm-round93-initial-gates.log
    SHA256 93e8686db07b65d1fd2c5c636df051e0e00707251abae92a4ebc65c23b745d11; local
    artifact /private/tmp/cmm-round93-initial-gates.json
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: supports
  summary: All four actual commands exited0 with exact owner bytes unchanged. These
    are structural/provenance checks, not scientific proof.
  snapshot_sha256: 62efc465f83b93012e3be8c6a1c2e57104ad45e459a7696ced9b53cef26464ea
- evidence_id: search
  kind: search
  reference: Reviewer bounded live correction/counterevidence search
  locator: 2026-10-15 web queries and local scope dedup; local artifact /private/tmp/cmm-round93-pig-independent/scope-dedup.txt
  accessed_at: '2026-10-15T10:43:28.784688Z'
  support: context_only
  summary: Exact DOI correction/retraction/erratum and pig-manure sulfur-concentration
    queries returned the accepted article and related studies, without an attributable
    notice in those results. Related biochar/iron studies are not transferred. Hidden/ignored/followed
    current-owner scope search supports distinct resource boundary.
  snapshot_sha256: 85f4465968a4e547c674e79aea8f86ffc56f21df7164cf98a5e91701bf3c1fa4
  search_scope: 'Queries: "10.1016/j.heliyon.2018.e00778" correction retraction erratum;
    "pig manure" "sulfur concentration" Wei bioleaching nutrient loss. Bounded search,
    not exhaustive absence. rg --hidden --no-ignore --follow across current records
    and own source report.'
assessments:
- assessment_id: identity
  area: identity
  topic: Real unincinerated agricultural feed
  outcome: supported
  summary: The farm sample and diluted slurry are correctly one heterogeneous secondary
    resource, separate from ash, poultry and municipal sludge.
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - main
  details: No mineral phase, criticality listing or isolated product identity is inferred.
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated dose response with controls bounded
  outcome: supported
  summary: Methods and original figures support the reported dose response, with missing
    control and mass-balance limits explicit.
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - main
  - fig1
  - fig2
  - fig4
  - taxonomy
  details: 2%w/v slurry;200mL in500mL flasks;5%v/v active indigenous enrichment;2/5/8/10g/L
    elemental sulfur;28°C,180rpm,12days,triplicates. All reported arms inoculated;
    no matched sterile or zero-sulfur control. No species-specific mechanism assigned.
- assessment_id: outcomes
  area: quantity
  topic: Measured denominator and counterevidence
  outcome: supported
  summary: Source-reported metal solubilization is distinguished from isolated recovery,
    and residual nutrient decreases remain a tradeoff.
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - fig4
  - fig6
  - fig7
  - main
  details: Cu48.5% at low dose is not replaced by high-dose endpoint. No sampling/inoculum/volume-corrected
    closed mass balance, fertilizer safety or industrial claim is accepted. Sequential
    fractions and empirical fits are operational proxies.
- assessment_id: limits
  area: consistency
  topic: Source contradictions and provenance
  outcome: supported
  summary: Time/unit/caption conflicts and incomplete species resolution are adequately
    retained.
  target_ids:
  - cmmmech:pig-manure
  evidence_ids:
  - main
  - fig1
  - fig3
  - fig5
  - fig7
  - taxonomy
  - batch
  details: Actual CREATE actor/time and inline event are distinct and valid. Original
    PDF route unavailable; official text plus original figures are the accepted route.
    Relevant review inputs were re-inspected using canonical repository labels before
    persistence; scientific hashes unchanged.
findings: []
actions: []
limitations:
- No matched sterile, uninoculated, no-sulfur or acidity-matched control.
- No complete metal/nutrient mass balance or isolated recovered product; final volume
  and sampling corrections unresolved.
- Only98% sequence similarity from a separate salt-medium enrichment; no confirmed
  experimental species/strain.
- Original PDF unavailable; complete official JATS/HTML and all original main graphics
  inspected instead. No separate SI announced in that original.
- Bounded correction/counterevidence searches do not prove global absence of notices
  or studies.
- Early unsaved inspect preparation used URL-form owner repository labels; canonical
  labels were recaptured with unchanged hashes before persistence.
- Unsaved schema-format drafts used UTC +00:00 and, for corkite, a colon in the proposed
  issue key; normalized to native Z timestamps and permitted key characters before
  persistence, without changing the observation.
```
