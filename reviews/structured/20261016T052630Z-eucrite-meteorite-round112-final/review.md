# Independent scientific review of eucrite meteorite

- Review: 20261016T052630Z-eucrite-meteorite-round112-final
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T05:19:13.141650Z
- Finished UTC: 2026-10-16T05:26:30.317775Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The eucrite record is defensible for a narrow terrestrial Sphingomonas-associated trace-metal mobilization observation. EU-specific Pt values and methods match original text/Figure4B; the single abiotic control, arbitrary fold-change threshold, unavailable supplementary cells and unresolved specimen provenance are preserved. No corrective curator finding was established.

## Scope And Provenance

Full assessment of the one assigned maintained meteorite record, source and control boundaries, primary figures/tables and relevant available supplements, exact CREATE provenance and completed structural checks.

Selection: One of two root-authored meteorite owners explicitly assigned to this independent reviewer; each receives a separate native bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e3a638e04d9e64cbda7c26d277bdf4f5e7d1e3ae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:eucrite-meteorite | data/records/eucrite-meteorite.yaml | maintained | eucrite-meteorite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation of assigned two meteorite owners | passed | True | cmmmech:eucrite-meteorite | Checked 2 record(s); 0 failed. |
| Coordinator final batch command1 | passed | True | cmmmech:eucrite-meteorite | Terminal receipt independently bound to exact command, worktree/base, log hash and current owner hash; exit0. |
| Coordinator final batch command2 | passed | True | cmmmech:eucrite-meteorite | Terminal receipt independently bound to exact command, worktree/base, log hash and current owner hash; exit0. |
| Coordinator final batch command3 | passed | True | cmmmech:eucrite-meteorite | Terminal receipt independently bound to exact command, worktree/base, log hash and current owner hash; exit0. |
| Coordinator final batch command4 | passed | True | cmmmech:eucrite-meteorite | Terminal receipt independently bound to exact command, worktree/base, log hash and current owner hash; exit0. |

## Scientific And Domain Assessments

### Natural meteorite feed and unresolved specimen provenance

identity: supported. Targets: cmmmech:eucrite-meteorite.

The owner correctly denotes an EU eucrite primary resource, separate from L-chondrite and terrestrial basalt.

Table2 supports plagioclase/pyroxene dominance with minor olivine/quartz, while its percentm/V label is retained as a source unit conflict. Vesta attribution comes from the paper, without exact specimen name/accession. Table1Skylab versus acknowledgmentSkyFall remains unresolved. No commodity/mineral identity or jurisdiction/list/edition criticality designation is inherited.

### Species and strain boundaries

identity: supported. Targets: cmmmech:eucrite-meteorite.

NCBITaxon429134 supports the species label; CP1D remains the study designation.

M9-grown living S.desiccabilis is the experimental organism. The species authority does not independently authenticate the actual DSMZ culture. No inactive-biomass mechanism or genetic causal pathway is inferred; iModulonDB is not applicable to the evidence/claim type.

### Correct treatment and comparison scope

consistency: supported. Targets: cmmmech:eucrite-meteorite.

The substrate, culture medium, time, temperature and replication match the primary methods.

Fragments≤1mm,.15g in25mLglass tubes,250C4h,15mLM9with2%m/Vglucose,1%w/vpulp,OD600.039±.006 and static25C30d are correctly reported. Three biological replicates but only one uninoculated replicate per rock and separate rock-free cultures are distinguished. No microgravity treatment is transferred from the L-chondrite study.

### EU-specific Pt values and uncertainty

evidence: supported. Targets: cmmmech:eucrite-meteorite.

Reported Pt endpoint fractions/ratios are correctly assigned to EU and explicitly not recomputed from inaccessible cells.

(8.98±3.20)×10^-2%bulkPt and ratio2.47±.48 are text/figure summaries with SE. Figure4B and methods2.9 identify arbitrary ratio≥2, not inferential significance. One control cannot characterize control variance. EU Pd ratio&lt;2 limits enhancement claims. High Ce/Th values from unrelated Sudbury specimens are not transferred to EU.

### Clarified liquid and omitted pellet accounting

evidence: supported. Targets: cmmmech:eucrite-meteorite.

The operational liquid measurement is distinguished from total extraction and recovered product.

Day30liquid centrifugation5000rpm5min precedes4%v/vHNO3 and ICPMS/OES. The pellet was not assayed because biomass and rock could not be separated. Prior-study biomass&lt;5% is not a measurement from this assay. Fractions of bulk inventory and ratios are endpoints; no isolated platinum, mineral-specific dissolution or full mass balance is demonstrated.

### Molecular mechanism and terrestrial laboratory setting

scope: supported. Targets: cmmmech:eucrite-meteorite.

Selective culture-associated mobilization is supported with bounded causal confidence.

Biofilm/local-complexation/ligand explanations in discussion are hypotheses without direct causal ligand measurements or verified mineral-phase dissolution for EU. The single-control design and unacquired supplementary data limit robustness. This remains terrestrial laboratory work, not an ISS experiment, industrial recovery or demonstrated space mining.

### Actual history, exact inputs and completed structural checks

provenance: supported. Targets: cmmmech:eucrite-meteorite.

The immutable review binds actual owner/history/dossier bytes and verified completed gates.

Canonical CREATE and distinct inline CREATE record root authorship with actual GPT-6/codex metadata; no earlier work is invented. Reviewer authored unrelated studtite/metastudtite, not these meteorite owners. Named validation passed; four coordinator batch commands and log digest were independently checked against exactbase/worktree/currenthash. Structural passes do not certify the whole corpus scientifically.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/eucrite-meteorite.yaml; Complete exact target captured before assessment, together with canonical CREATE history, frozen source dossier and schema. | supports | The current owner, rather than an earlier draft or generated page, is the scientific target. |
| authorities | /private/tmp/cmm-round112-uranium-research/meteorite-review-web.json; Independently opened official NCBI species pages429134 and69488 on16October2026. | supports | Sphingomonas desiccabilis and Penicillium simplicissimum are species-level labels. Experimental CP1D and DSM1078 designations come from primary Methods, not authenticated by a species CURIE. |
| notices | /private/tmp/cmm-round112-uranium-research/meteorite-review-web.json; Four bounded exact DOI/title correction, erratum and retraction queries; publisher/PubMed results and both retained Crossref relation/update fields. | context_only | No relevant notice surfaced in these returned results. Earlier BioAsteroid preprint and article-in-press are prior versions, not independent replications or substitutes for the inspected final PDF. No exhaustive notice-absence claim. |
| dedup | /private/tmp/cmm-round112-uranium-research/meteorite-review-dedup.json; Hidden/ignored-inclusive rg --no-ignore --hidden --follow in maintained record/research/review/history roots, existing ignored main reports, and current/previous cited resource raw roots. | context_only | Thirty matching paths include the assigned owners, source and acquisition references and one old discovery lead. No second dedicated owner in these bounded searched roots was found. Binary PDFs were separately inspected. Raw matches remain external and hashed. |
| provenance | research/sources/round112-resources/20261016-source-investigation.json; Frozen paired source dossier and exact linked canonical CREATE session, both included in native source.inputs. | supports | Real working-tree creation and separate inline event are retained; this reviewer did not author or mutate either meteorite owner/history. Acquisition status, specimen limits and source access gaps are explicit. |
| named | /private/tmp/cmm-round112-uranium-research/meteorite-review-named-validation.json; Actual independent named validation of exactly the two assigned owners, terminal session76575/chunk837aed; command, cwd, base and current hashes checked. | supports | Checked2records;0failed. The receipt honestly records that a separate command start timestamp was not captured; structural validity is not scientific proof. |
| batch | /private/tmp/cmm-round112-final-gates.json; Completed coordinator batch; exact worktree, base, four command arrays, zero exits, unchanged inputs, both owner hashes and retained log digest independently verified. | supports | 317passed/3skipped;570records0failed;647history records0errors;generated pages current. These are structural and provenance gates, not a fresh scientific review of the whole corpus. |
| primary | https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1741305/full; Complete fourteen-page publisher PDF plus live full HTML; Methods2.1–2.10, Table1p3, Table2p6, EU-specific Results3.4pp8–9, Figure4B p9 and Discussion/Acknowledgmentspp10–12 checked. Original pages2–6,8–9,12 independently visually inspected. | supports | The EU-specific30-day terrestrial assay supports qualified trace-metal mobilization; missing raw supplementary cells are not represented as inspected. Table1Skylab(US) differs from acknowledgmentSkyFallMeteorites and no named meteorite/accession is supplied. |
| figure | https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1741305/full; Original Figure4B p9 and EU resultspp8–9; original source plot and caption inspected alongside methods2.9. | supports | Pt extraction(8.98±3.20)×10^-2% and biotic/abiotic2.47±.48 match the text/plot. Caption defines SE and arbitrary2threshold; it is not a significance test. EU Pd ratio is below2 and the endpoint fraction is not a kinetic rate. |
| access | /private/tmp/cmm-round112-resources-research/acquisition-5.json; Publisher/API/public-files routes retained in acquisition3–5, including404 HTML/JSON responses at files named.xlsx/.pdf. | context_only | The tested responses are not usable supplementary files. Main article claims remain author-reported, without recomputation from supplementary TablesS5–S7 or independent supplier/accession authentication. This bounds access, not global unavailability. |

## Limits And Additional Notes

- Only one abiotic control was used per rock, so control variability and a statistically replicated microbial enhancement are not established.
- Supplementary tables/figures were not obtained through the documented public routes; author-reported Pt summaries were not recomputed or given stronger precision.
- Exact EU meteorite identity/accession and Skylab versus SkyFall supplier wording remain unresolved; the source Table2%m/V label is not independently corrected.
- No separate pellet/biomass metal accounting, direct causal ligand assay, authenticated experimental stock, laboratory replication or isolated product was verified.
- The assessment is limited to EU; high Ce/Th values or mechanisms from other substrates and prior studies are not accepted by transfer. Bounded notice/duplicate searches are not exhaustive.
- No target or canonical history edits were made during this review. No fresh scientific review of other corpus owners is claimed.
- Source follow-up issue473 addresses EU supplementary/specimen provenance gaps; future evidence work is distinct from a current curator defect.
- Unsaved draft validation caught target metadata using record/CMMMech instead of maintained/CultureBotAI/CMMMech. Target descriptors were corrected and re-inspected; source input hashes were exactly unchanged. Original external drafts are retained; no native review was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T052630Z-eucrite-meteorite-round112-final
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of eucrite meteorite
started_at: '2026-10-16T05:19:13.141650Z'
finished_at: '2026-10-16T05:26:30.317775Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored this meteorite owner/history/dossier. Reviewer
    authored unrelated studtite/metastudtite; independently captured target bytes
    before assessment and inspected original primary evidence, official species identities
    and source limitations without editing either meteorite owner.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The eucrite record is defensible for a narrow terrestrial Sphingomonas-associated
  trace-metal mobilization observation. EU-specific Pt values and methods match original
  text/Figure4B; the single abiotic control, arbitrary fold-change threshold, unavailable
  supplementary cells and unresolved specimen provenance are preserved. No corrective
  curator finding was established.
source:
  git_revision: e3a638e04d9e64cbda7c26d277bdf4f5e7d1e3ae
  state: working_tree
  inputs:
  - path: data/records/eucrite-meteorite.yaml
    sha256: 92a87d16eb94ca6965bc030fc3ea541135f7e7b56c7559c50dd73c5733f6d0c8
    role: target
  - path: history/records/eucrite-meteorite/2026-10-16T051458Z-codex-678910.yaml
    sha256: 40a2c5bda8979dbe6bb717e6e8e7681a31c0dc847748deb673b2374c4efdacdf
    role: context
  - path: research/sources/round112-resources/20261016-source-investigation.json
    sha256: 2d881acb60c146da0ca017cb6815c7c503ae6faabd8d4c4bcacd1ba2796cef96
    role: context
  - path: research/sources/round112-resources/20261016-source-investigation.md
    sha256: 04e1e5125de063574b0c03825dbb27e5ff3fb9ca216f29cc79f4917ac4342832
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:eucrite-meteorite
  path: data/records/eucrite-meteorite.yaml
  label: eucrite-meteorite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/eucrite-meteorite.yaml
    role: maintained_record
scope:
  description: Full assessment of the one assigned maintained meteorite record, source
    and control boundaries, primary figures/tables and relevant available supplements,
    exact CREATE provenance and completed structural checks.
  selection: One of two root-authored meteorite owners explicitly assigned to this
    independent reviewer; each receives a separate native bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:eucrite-meteorite
checks:
- check_id: named
  name: Independent named validation of assigned two meteorite owners
  status: passed
  required: true
  summary: Checked 2 record(s); 0 failed.
  target_ids:
  - cmmmech:eucrite-meteorite
  command: uv run --locked cmmmech validate data/records/l-chondrite-meteorite.yaml
    data/records/eucrite-meteorite.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch1
  name: Coordinator final batch command1
  status: passed
  required: true
  summary: Terminal receipt independently bound to exact command, worktree/base, log
    hash and current owner hash; exit0.
  target_ids:
  - cmmmech:eucrite-meteorite
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Coordinator final batch command2
  status: passed
  required: true
  summary: Terminal receipt independently bound to exact command, worktree/base, log
    hash and current owner hash; exit0.
  target_ids:
  - cmmmech:eucrite-meteorite
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Coordinator final batch command3
  status: passed
  required: true
  summary: Terminal receipt independently bound to exact command, worktree/base, log
    hash and current owner hash; exit0.
  target_ids:
  - cmmmech:eucrite-meteorite
  command: uv run --locked cmmmech validate-history --base e3a638e04d9e64cbda7c26d277bdf4f5e7d1e3ae
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch4
  name: Coordinator final batch command4
  status: passed
  required: true
  summary: Terminal receipt independently bound to exact command, worktree/base, log
    hash and current owner hash; exit0.
  target_ids:
  - cmmmech:eucrite-meteorite
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/eucrite-meteorite.yaml
  locator: Complete exact target captured before assessment, together with canonical
    CREATE history, frozen source dossier and schema.
  summary: The current owner, rather than an earlier draft or generated page, is the
    scientific target.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 92a87d16eb94ca6965bc030fc3ea541135f7e7b56c7559c50dd73c5733f6d0c8
- evidence_id: authorities
  kind: authority
  reference: /private/tmp/cmm-round112-uranium-research/meteorite-review-web.json
  locator: Independently opened official NCBI species pages429134 and69488 on16October2026.
  summary: Sphingomonas desiccabilis and Penicillium simplicissimum are species-level
    labels. Experimental CP1D and DSM1078 designations come from primary Methods,
    not authenticated by a species CURIE.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 05eaceeb7fc7a7e5652ad1107596fe13dbf23e67ef54d5cc3dcf9234b45bbbe1
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round112-uranium-research/meteorite-review-web.json
  locator: Four bounded exact DOI/title correction, erratum and retraction queries;
    publisher/PubMed results and both retained Crossref relation/update fields.
  summary: No relevant notice surfaced in these returned results. Earlier BioAsteroid
    preprint and article-in-press are prior versions, not independent replications
    or substitutes for the inspected final PDF. No exhaustive notice-absence claim.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: context_only
  snapshot_sha256: 05eaceeb7fc7a7e5652ad1107596fe13dbf23e67ef54d5cc3dcf9234b45bbbe1
  search_scope: Four bounded exact DOI/title correction, erratum and retraction queries;
    publisher/PubMed results and both retained Crossref relation/update fields. No
    relevant notice surfaced in these returned results. Earlier BioAsteroid preprint
    and article-in-press are prior versions, not independent replications or substitutes
    for the inspected final PDF. No exhaustive notice-absence claim.
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round112-uranium-research/meteorite-review-dedup.json
  locator: Hidden/ignored-inclusive rg --no-ignore --hidden --follow in maintained
    record/research/review/history roots, existing ignored main reports, and current/previous
    cited resource raw roots.
  summary: Thirty matching paths include the assigned owners, source and acquisition
    references and one old discovery lead. No second dedicated owner in these bounded
    searched roots was found. Binary PDFs were separately inspected. Raw matches remain
    external and hashed.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: context_only
  snapshot_sha256: 0d5a6c191bce1130ceebf5fce397d4da18917e132187b4bb0915d0acf7d7d7e5
  search_scope: Hidden/ignored-inclusive rg --no-ignore --hidden --follow in maintained
    record/research/review/history roots, existing ignored main reports, and current/previous
    cited resource raw roots. Thirty matching paths include the assigned owners, source
    and acquisition references and one old discovery lead. No second dedicated owner
    in these bounded searched roots was found. Binary PDFs were separately inspected.
    Raw matches remain external and hashed.
- evidence_id: provenance
  kind: record_content
  reference: research/sources/round112-resources/20261016-source-investigation.json
  locator: Frozen paired source dossier and exact linked canonical CREATE session,
    both included in native source.inputs.
  summary: Real working-tree creation and separate inline event are retained; this
    reviewer did not author or mutate either meteorite owner/history. Acquisition
    status, specimen limits and source access gaps are explicit.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 2d881acb60c146da0ca017cb6815c7c503ae6faabd8d4c4bcacd1ba2796cef96
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round112-uranium-research/meteorite-review-named-validation.json
  locator: Actual independent named validation of exactly the two assigned owners,
    terminal session76575/chunk837aed; command, cwd, base and current hashes checked.
  summary: Checked2records;0failed. The receipt honestly records that a separate command
    start timestamp was not captured; structural validity is not scientific proof.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 32705064146ea400d169caa31f6d63fd249831e7528f9b643a852416683c2768
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round112-final-gates.json
  locator: Completed coordinator batch; exact worktree, base, four command arrays,
    zero exits, unchanged inputs, both owner hashes and retained log digest independently
    verified.
  summary: 317passed/3skipped;570records0failed;647history records0errors;generated
    pages current. These are structural and provenance gates, not a fresh scientific
    review of the whole corpus.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 5211cc2ab6a7cc4d7143f4e604ef6abbbd51ce3e9cd8727d5ef9083acd14c2b5
- evidence_id: primary
  kind: primary_source
  reference: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1741305/full
  locator: Complete fourteen-page publisher PDF plus live full HTML; Methods2.1–2.10,
    Table1p3, Table2p6, EU-specific Results3.4pp8–9, Figure4B p9 and Discussion/Acknowledgmentspp10–12
    checked. Original pages2–6,8–9,12 independently visually inspected.
  summary: The EU-specific30-day terrestrial assay supports qualified trace-metal
    mobilization; missing raw supplementary cells are not represented as inspected.
    Table1Skylab(US) differs from acknowledgmentSkyFallMeteorites and no named meteorite/accession
    is supplied.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: cf994f738b6af0da509e3484648b74fd2d1d4736c58b233ef9fa4f1b9e604d51
- evidence_id: figure
  kind: primary_source
  reference: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1741305/full
  locator: Original Figure4B p9 and EU resultspp8–9; original source plot and caption
    inspected alongside methods2.9.
  summary: Pt extraction(8.98±3.20)×10^-2% and biotic/abiotic2.47±.48 match the text/plot.
    Caption defines SE and arbitrary2threshold; it is not a significance test. EU
    Pd ratio is below2 and the endpoint fraction is not a kinetic rate.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: supports
  snapshot_sha256: 6c61e9bc084c9dd482e79b7c8971e36a93e4e551e515c14c308de41657e03915
- evidence_id: access
  kind: record_content
  reference: /private/tmp/cmm-round112-resources-research/acquisition-5.json
  locator: Publisher/API/public-files routes retained in acquisition3–5, including404
    HTML/JSON responses at files named.xlsx/.pdf.
  summary: The tested responses are not usable supplementary files. Main article claims
    remain author-reported, without recomputation from supplementary TablesS5–S7 or
    independent supplier/accession authentication. This bounds access, not global
    unavailability.
  accessed_at: '2026-10-16T05:25:40.613577Z'
  support: context_only
  snapshot_sha256: ab7fc50a2758e76a24410df3b6eec2260daa88b03813dfa2c8ce1dbaf0702bb5
assessments:
- assessment_id: identity
  area: identity
  topic: Natural meteorite feed and unresolved specimen provenance
  outcome: supported
  summary: The owner correctly denotes an EU eucrite primary resource, separate from
    L-chondrite and terrestrial basalt.
  details: Table2 supports plagioclase/pyroxene dominance with minor olivine/quartz,
    while its percentm/V label is retained as a source unit conflict. Vesta attribution
    comes from the paper, without exact specimen name/accession. Table1Skylab versus
    acknowledgmentSkyFall remains unresolved. No commodity/mineral identity or jurisdiction/list/edition
    criticality designation is inherited.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
  - dedup
- assessment_id: culture
  area: identity
  topic: Species and strain boundaries
  outcome: supported
  summary: NCBITaxon429134 supports the species label; CP1D remains the study designation.
  details: M9-grown living S.desiccabilis is the experimental organism. The species
    authority does not independently authenticate the actual DSMZ culture. No inactive-biomass
    mechanism or genetic causal pathway is inferred; iModulonDB is not applicable
    to the evidence/claim type.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
  - authorities
- assessment_id: protocol
  area: consistency
  topic: Correct treatment and comparison scope
  outcome: supported
  summary: The substrate, culture medium, time, temperature and replication match
    the primary methods.
  details: Fragments≤1mm,.15g in25mLglass tubes,250C4h,15mLM9with2%m/Vglucose,1%w/vpulp,OD600.039±.006
    and static25C30d are correctly reported. Three biological replicates but only
    one uninoculated replicate per rock and separate rock-free cultures are distinguished.
    No microgravity treatment is transferred from the L-chondrite study.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
- assessment_id: outcomes
  area: evidence
  topic: EU-specific Pt values and uncertainty
  outcome: supported
  summary: Reported Pt endpoint fractions/ratios are correctly assigned to EU and
    explicitly not recomputed from inaccessible cells.
  details: (8.98±3.20)×10^-2%bulkPt and ratio2.47±.48 are text/figure summaries with
    SE. Figure4B and methods2.9 identify arbitrary ratio≥2, not inferential significance.
    One control cannot characterize control variance. EU Pd ratio<2 limits enhancement
    claims. High Ce/Th values from unrelated Sudbury specimens are not transferred
    to EU.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
  - figure
  - access
- assessment_id: analytical
  area: evidence
  topic: Clarified liquid and omitted pellet accounting
  outcome: supported
  summary: The operational liquid measurement is distinguished from total extraction
    and recovered product.
  details: Day30liquid centrifugation5000rpm5min precedes4%v/vHNO3 and ICPMS/OES.
    The pellet was not assayed because biomass and rock could not be separated. Prior-study
    biomass<5% is not a measurement from this assay. Fractions of bulk inventory and
    ratios are endpoints; no isolated platinum, mineral-specific dissolution or full
    mass balance is demonstrated.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
- assessment_id: causality
  area: scope
  topic: Molecular mechanism and terrestrial laboratory setting
  outcome: supported
  summary: Selective culture-associated mobilization is supported with bounded causal
    confidence.
  details: Biofilm/local-complexation/ligand explanations in discussion are hypotheses
    without direct causal ligand measurements or verified mineral-phase dissolution
    for EU. The single-control design and unacquired supplementary data limit robustness.
    This remains terrestrial laboratory work, not an ISS experiment, industrial recovery
    or demonstrated space mining.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - primary
  - figure
  - access
- assessment_id: checks
  area: provenance
  topic: Actual history, exact inputs and completed structural checks
  outcome: supported
  summary: The immutable review binds actual owner/history/dossier bytes and verified
    completed gates.
  details: Canonical CREATE and distinct inline CREATE record root authorship with
    actual GPT-6/codex metadata; no earlier work is invented. Reviewer authored unrelated
    studtite/metastudtite, not these meteorite owners. Named validation passed; four
    coordinator batch commands and log digest were independently checked against exactbase/worktree/currenthash.
    Structural passes do not certify the whole corpus scientifically.
  target_ids:
  - cmmmech:eucrite-meteorite
  evidence_ids:
  - owner
  - provenance
  - named
  - batch
  - notices
findings: []
actions: []
limitations:
- Only one abiotic control was used per rock, so control variability and a statistically
  replicated microbial enhancement are not established.
- Supplementary tables/figures were not obtained through the documented public routes;
  author-reported Pt summaries were not recomputed or given stronger precision.
- Exact EU meteorite identity/accession and Skylab versus SkyFall supplier wording
  remain unresolved; the source Table2%m/V label is not independently corrected.
- No separate pellet/biomass metal accounting, direct causal ligand assay, authenticated
  experimental stock, laboratory replication or isolated product was verified.
- The assessment is limited to EU; high Ce/Th values or mechanisms from other substrates
  and prior studies are not accepted by transfer. Bounded notice/duplicate searches
  are not exhaustive.
notes:
- No target or canonical history edits were made during this review. No fresh scientific
  review of other corpus owners is claimed.
- Source follow-up issue473 addresses EU supplementary/specimen provenance gaps; future
  evidence work is distinct from a current curator defect.
- Unsaved draft validation caught target metadata using record/CMMMech instead of
  maintained/CultureBotAI/CMMMech. Target descriptors were corrected and re-inspected;
  source input hashes were exactly unchanged. Original external drafts are retained;
  no native review was overwritten.
```
