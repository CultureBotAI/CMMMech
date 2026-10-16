# Independent scientific review of tin-copper-solder

- Review: 20261016T082356Z-tin-copper-solder-round115-final
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-16T08:12:32.530172Z
- Finished UTC: 2026-10-16T08:23:56.366813Z
- Reviewer: codex /root/round104_uranium (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The tin-copper solder commodity record is scientifically defensible for the reported commercial pieces and narrowly scoped Acetobacter-culture-associated dissolution. Full original methods and Figures7–8 support retained conditions, while culture identity, biomass state, acid background, feed composition and recovery limits are explicit. No supported curator defect identified.

## Scope And Provenance

Complete independent assessment of one assigned maintained recovery-material owner, primary methods/outcomes, identity, uncertainty, provenance and actual checks.

Selection: One of two root-authored recovery records assigned for independent review; separate record artifact.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97c978dcfb98269ea46fa6a9d02a6fb0253e111.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:tin-copper-solder | data/records/tin-copper-solder.yaml | maintained | Tin-copper solder |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation 1 | passed | True | cmmmech:tin-copper-solder | Checked 2 record(s); 0 failed.<br> |
| Independent named validation 2 | passed | True | cmmmech:tin-copper-solder | Checked 2 history record(s); 0 error(s).<br> |
| Coordinator completed batch command 1 | passed | True | cmmmech:tin-copper-solder | Exact worktree/base/commands/input hashes/log hash and completed terminal receipt independently checked; exit 0. |
| Coordinator completed batch command 2 | passed | True | cmmmech:tin-copper-solder | Exact worktree/base/commands/input hashes/log hash and completed terminal receipt independently checked; exit 0. |
| Coordinator completed batch command 3 | passed | True | cmmmech:tin-copper-solder | Exact worktree/base/commands/input hashes/log hash and completed terminal receipt independently checked; exit 0. |
| Coordinator completed batch command 4 | passed | True | cmmmech:tin-copper-solder | Exact worktree/base/commands/input hashes/log hash and completed terminal receipt independently checked; exit 0. |

## Scientific And Domain Assessments

### Commercial solder identity and provenance

identity: supported. Targets: cmmmech:tin-copper-solder.

The commodity and specimen scope are supported without assuming a waste origin.

Methods identify Taiwan-Solid Enterprises material nominally Sn-Cu 63–37%; no service history. SEM/EDS discussion suggests tin-rich coating and copper-containing core but does not establish homogeneous bulk alloy or a quantitative assay. The record faithfully reports the unusual nominal ratio without silently changing it. No mineral or elemental ID or inherited criticality designation is assigned.

### Culture preparation, substrate and conditions

consistency: supported. Targets: cmmmech:tin-copper-solder.

The accepted microbial-arm conditions match the full original.

Methods give 3 mm pieces, 100 mg, 4 mL Acetobacter culture, 24 h culture growth then 30 h leaching at 30 C/150 rpm; washing uses water and 75% ethanol. Results instead call the liquid supernatant. Cell removal/viability cannot be resolved, and the owner preserves this ambiguity rather than assigning live-cell contact. Three sets are reported without defined statistics or biological independence.

### Collection identity versus experiment authentication

identity: supported. Targets: cmmmech:tin-copper-solder.

The authority claim is accurate and the experimental mismatch is preserved.

The paper names TISTR 102 but says BCRC Taiwan; fresh authority says pasteurianus with historical aceti. Catalogue identity is correctly not converted into authenticated culture identity. The mechanism remains Acetobacter preparation rather than an invented species/strain accession.

### Culture-associated dissolution and causal limits

evidence: supported. Targets: cmmmech:tin-copper-solder.

Figure 7 supports time-dependent dissolved Cu/Sn, not net microbial benefit or isolated recovery.

Figure 7 contains 10/20/30 h bars and the reported dissolved endpoint. YGEA includes acetic acid; titration estimates total acidity and its underlying data are not shown. No matched uninoculated-medium/acid-only arm is provided. Low-strength chemical-acid series uses 10 mL rather than 4 mL, so it cannot quantify benefit. Figure 8 belongs to 80% chemical-acid treatment and supplies no direct microbial contact/mineralization evidence.

### Scale, numerical claims and deferred source

scope: supported. Targets: cmmmech:tin-copper-solder.

Laboratory material testing is not industrial treatment of end-of-life solder.

Generic recycling/economic prose and the 2014 secondary comparison do not establish the 2017 feed as waste, industrial deployment, or reusable quantitative yield. Exact percentages remain unadopted given composition/denominator uncertainty. Complete 2014 original was not obtained, so its fungal mechanisms and values are not accepted.

### Exact current inputs and completed checks

provenance: supported. Targets: cmmmech:tin-copper-solder.

Frozen record/history/schema/dossier and completed checks are verified for this owner.

Actual inline CREATE and linked canonical CREATE metadata, timestamps and target are coherent. Reviewer did not mutate target/history. Named records/history and root four-command batch all pass with current hash/log binding. The final scientific review is limited to this assigned owner, not the entire corpus.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/records/tin-copper-solder.yaml; Complete maintained owner and exact current canonical CREATE history, schema, record instructions and frozen author dossier captured before scientific judgment. | supports | Reviewer independently read original primary sources; no owner or history mutation by reviewer. |
| provenance | research/sources/round115-recovery/20261016-source-investigation.md; Frozen root source dossier and both inspection captures. | supports | Root authored assigned recovery records. Reviewer authored unrelated andersonite/rutherfordine; independent review does not rely on author conclusions. Initial target labels were normalized to canonical repository/maintained-owner metadata in a second capture; identical source hashes were proved and both captures retained. |
| dedup | /private/tmp/cmm-round115-uranium-research/recovery-review-dedup.json; rg --no-ignore --hidden --follow over current records/research/reviews/history, original-main ignored reports and assigned cited raw source root. | context_only | 19 matching paths; only two assigned owners matched in records. Current solder product and solid spent target remain distinct from elements, LCD glass and etching wastewater. Unrelated home/temp and unextracted binary content excluded; no machine-wide absence claim. |
| notices | /private/tmp/cmm-round115-uranium-research/recovery-review-web.json; Exact DOI correction/retraction/corrigendum queries and TISTR 102 authority lookup; first returned sets, no exhaustive pagination. | context_only | No applicable notice identified in bounded returned results. Live DOI/publisher web opens failed; complete acquired PDFs and freshly acquired Crossref metadata independently checked. Metadata relation/update fields were empty/absent. These limits do not establish that no notice can exist. |
| named | /private/tmp/cmm-round115-uranium-research/recovery-review-checks.json; Actual independent validation of two owners and their exact two canonical CREATE sidecars against trusted base. | supports | Both commands exited0: records2/0failed and histories2/0errors. Current owner and inspection bindings verified. |
| batch | /private/tmp/cmm-round115-final-gates.json; Actual terminal four-command receipt, exact base/worktree/commands/current owner hashes/log and timestamp ordering independently verified. | supports | All four commands exited0 and scientific inputs were unchanged. Retained logSHA256 46f8098674f6197b2eabd022019feaa1c8609989a5395c364a1d26e2ae76dba0. These are structural/provenance checks, not fresh whole-corpus scientific review. |
| primary | https://doi.org/10.1186/s40643-017-0173-5; Complete 10-page published original from German National Library mirror; methods pp. 2–3; results pp. 3–8, original Figures 7–8 and Table 2 visually inspected; limitations/data availability p. 8. | supports | The culture preparation, chemical-acid comparisons, product feed, surface interpretation and dissolved-metal endpoint were independently checked. Numerical extraction yields and inferred net biological enhancement are not promoted. |
| culture | https://www.tistr.or.th/tistr_culture/cdetail.php?tno=102&amp;type=b; Fresh direct HTTP200 authority HTML; TISTR Number, Organism Name, Original No. and History fields. | supports | TISTR 102 currently resolves to Acetobacter pasteurianus, No. 24 DMKU B-45, deposited as A. aceti. It does not prove BCRC supply or authenticate the experimental culture; no organism CURIE is assigned. |
| metadata | https://api.crossref.org/works/10.1186%2Fs40643-017-0173-5; Fresh exact DOI authority response, compared with original first page. | supports | Four authors, title, DOI and 2017 publication agree. A newer publisher-platform page date is not interpreted as a new study or correction. |

## Limits And Additional Notes

- The assay does not isolate newly biosynthesized acetic acid, establish live-cell necessity or demonstrate net microbial enhancement over a matched control.
- The experimental culture was not authenticated; the fresh catalogue resolution cannot repair the BCRC/TISTR supply mismatch.
- Nominal 63–37% composition, bulk homogeneity, extraction denominator and error-bar meaning are not independently resolved; no yield digitization or pooled measurement performed.
- The 2014 original and underlying culture-acidity data were not acquired; no industrial deployment or spent-feed history is established.
- Notice and hidden/ignored-inclusive duplicate searches are bounded; absence is not claimed outside recorded roots/results.
- Raw copyrighted literature and renders remain outside Git; source access does not authorize redistribution.
- Source-evidence follow-ups are not fabricated current curator defects. No fresh scientific review of other corpus owners.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T082356Z-tin-copper-solder-round115-final
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of tin-copper-solder
started_at: '2026-10-16T08:12:32.530172Z'
finished_at: '2026-10-16T08:23:56.366813Z'
reviewer:
  identity: codex /root/round104_uranium
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored assigned recovery owner/history/dossier. Reviewer
    authored unrelated andersonite/rutherfordine and independently inspected original
    evidence, live authority and captured current bytes without editing these recovery
    owners.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The tin-copper solder commodity record is scientifically defensible for the
  reported commercial pieces and narrowly scoped Acetobacter-culture-associated dissolution.
  Full original methods and Figures7–8 support retained conditions, while culture
  identity, biomass state, acid background, feed composition and recovery limits are
  explicit. No supported curator defect identified.
source:
  git_revision: f97c978dcfb98269ea46fa6a9d02a6fb0253e111
  state: working_tree
  inputs:
  - path: data/records/tin-copper-solder.yaml
    sha256: 017b16672161b117c2ab07300342e3f1ba861036f10c2dfad8d994a7419f8c8b
    role: target
  - path: docs/record-review-profile.md
    sha256: 01c6f39d0d097876a0446131270df58bb32fa15804c66487419c171719d3ddc0
    role: context
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/tin-copper-solder/2026-10-16T080654Z-codex-4b3f51.yaml
    sha256: bb3ae0d89b55941a4bd342c59fb41cb8854ab96bff9dc73750ff58c8bf9d103f
    role: context
  - path: research/sources/round115-recovery/20261016-source-investigation.md
    sha256: 9a4bc6eb31a99b3993489c91c563c805243672441808bd58378df2f421a30e19
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
targets:
- target_id: cmmmech:tin-copper-solder
  path: data/records/tin-copper-solder.yaml
  label: Tin-copper solder
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/tin-copper-solder.yaml
    role: maintained_owner
scope:
  description: Complete independent assessment of one assigned maintained recovery-material
    owner, primary methods/outcomes, identity, uncertainty, provenance and actual
    checks.
  selection: One of two root-authored recovery records assigned for independent review;
    separate record artifact.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:tin-copper-solder
checks:
- check_id: named1
  name: Independent named validation 1
  status: passed
  required: true
  summary: 'Checked 2 record(s); 0 failed.

    '
  target_ids:
  - cmmmech:tin-copper-solder
  command: uv run --locked cmmmech validate data/records/tin-copper-solder.yaml data/records/spent-ito-targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: named2
  name: Independent named validation 2
  status: passed
  required: true
  summary: 'Checked 2 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:tin-copper-solder
  command: uv run --locked cmmmech validate-history history/records/tin-copper-solder/2026-10-16T080654Z-codex-4b3f51.yaml
    history/records/spent-ito-targets/2026-10-16T080705Z-codex-be0274.yaml --base
    f97c978dcfb98269ea46fa6a9d02a6fb0253e111
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - named
- check_id: batch1
  name: Coordinator completed batch command 1
  status: passed
  required: true
  summary: Exact worktree/base/commands/input hashes/log hash and completed terminal
    receipt independently checked; exit 0.
  target_ids:
  - cmmmech:tin-copper-solder
  command: just check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch2
  name: Coordinator completed batch command 2
  status: passed
  required: true
  summary: Exact worktree/base/commands/input hashes/log hash and completed terminal
    receipt independently checked; exit 0.
  target_ids:
  - cmmmech:tin-copper-solder
  command: uv run --locked cmmmech validate --require-records
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch3
  name: Coordinator completed batch command 3
  status: passed
  required: true
  summary: Exact worktree/base/commands/input hashes/log hash and completed terminal
    receipt independently checked; exit 0.
  target_ids:
  - cmmmech:tin-copper-solder
  command: uv run --locked cmmmech validate-history --base f97c978dcfb98269ea46fa6a9d02a6fb0253e111
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
- check_id: batch4
  name: Coordinator completed batch command 4
  status: passed
  required: true
  summary: Exact worktree/base/commands/input hashes/log hash and completed terminal
    receipt independently checked; exit 0.
  target_ids:
  - cmmmech:tin-copper-solder
  command: uv run --locked python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - batch
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/records/tin-copper-solder.yaml
  locator: Complete maintained owner and exact current canonical CREATE history, schema,
    record instructions and frozen author dossier captured before scientific judgment.
  summary: Reviewer independently read original primary sources; no owner or history
    mutation by reviewer.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 017b16672161b117c2ab07300342e3f1ba861036f10c2dfad8d994a7419f8c8b
- evidence_id: provenance
  kind: record_content
  reference: research/sources/round115-recovery/20261016-source-investigation.md
  locator: Frozen root source dossier and both inspection captures.
  summary: Root authored assigned recovery records. Reviewer authored unrelated andersonite/rutherfordine;
    independent review does not rely on author conclusions. Initial target labels
    were normalized to canonical repository/maintained-owner metadata in a second
    capture; identical source hashes were proved and both captures retained.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 9a4bc6eb31a99b3993489c91c563c805243672441808bd58378df2f421a30e19
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round115-uranium-research/recovery-review-dedup.json
  locator: rg --no-ignore --hidden --follow over current records/research/reviews/history,
    original-main ignored reports and assigned cited raw source root.
  summary: 19 matching paths; only two assigned owners matched in records. Current
    solder product and solid spent target remain distinct from elements, LCD glass
    and etching wastewater. Unrelated home/temp and unextracted binary content excluded;
    no machine-wide absence claim.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: context_only
  snapshot_sha256: 06df527c98b2d2318804819fa14fb83c9f48ba1317d8573b61db524f55f174d1
  search_scope: rg --no-ignore --hidden --follow over current records/research/reviews/history,
    original-main ignored reports and assigned cited raw source root. 19 matching
    paths; only two assigned owners matched in records. Current solder product and
    solid spent target remain distinct from elements, LCD glass and etching wastewater.
    Unrelated home/temp and unextracted binary content excluded; no machine-wide absence
    claim.
- evidence_id: notices
  kind: search
  reference: /private/tmp/cmm-round115-uranium-research/recovery-review-web.json
  locator: Exact DOI correction/retraction/corrigendum queries and TISTR 102 authority
    lookup; first returned sets, no exhaustive pagination.
  summary: No applicable notice identified in bounded returned results. Live DOI/publisher
    web opens failed; complete acquired PDFs and freshly acquired Crossref metadata
    independently checked. Metadata relation/update fields were empty/absent. These
    limits do not establish that no notice can exist.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: context_only
  snapshot_sha256: 6677745b81f4df080bf88e61b1b2d6de65bdd412198f707d79ef2190456e957d
  search_scope: Exact DOI correction/retraction/corrigendum queries and TISTR 102
    authority lookup; first returned sets, no exhaustive pagination. No applicable
    notice identified in bounded returned results. Live DOI/publisher web opens failed;
    complete acquired PDFs and freshly acquired Crossref metadata independently checked.
    Metadata relation/update fields were empty/absent. These limits do not establish
    that no notice can exist.
- evidence_id: named
  kind: validation
  reference: /private/tmp/cmm-round115-uranium-research/recovery-review-checks.json
  locator: Actual independent validation of two owners and their exact two canonical
    CREATE sidecars against trusted base.
  summary: 'Both commands exited0: records2/0failed and histories2/0errors. Current
    owner and inspection bindings verified.'
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 2d25c64878dba72d9e8e0a31ae1b05843a8cd938e36543904860d892dda1d6bc
- evidence_id: batch
  kind: validation
  reference: /private/tmp/cmm-round115-final-gates.json
  locator: Actual terminal four-command receipt, exact base/worktree/commands/current
    owner hashes/log and timestamp ordering independently verified.
  summary: All four commands exited0 and scientific inputs were unchanged. Retained
    logSHA256 46f8098674f6197b2eabd022019feaa1c8609989a5395c364a1d26e2ae76dba0. These
    are structural/provenance checks, not fresh whole-corpus scientific review.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: a4961d4886685d1dee2e32cefac92f59918148398b3cd4d909e7e214efb1d31f
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1186/s40643-017-0173-5
  locator: Complete 10-page published original from German National Library mirror;
    methods pp. 2–3; results pp. 3–8, original Figures 7–8 and Table 2 visually inspected;
    limitations/data availability p. 8.
  summary: The culture preparation, chemical-acid comparisons, product feed, surface
    interpretation and dissolved-metal endpoint were independently checked. Numerical
    extraction yields and inferred net biological enhancement are not promoted.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 81158339d72c15802cfcaa01990ddae25bd70c06bc62419006d08d3fd8dfd788
- evidence_id: culture
  kind: primary_source
  reference: https://www.tistr.or.th/tistr_culture/cdetail.php?tno=102&type=b
  locator: Fresh direct HTTP200 authority HTML; TISTR Number, Organism Name, Original
    No. and History fields.
  summary: TISTR 102 currently resolves to Acetobacter pasteurianus, No. 24 DMKU B-45,
    deposited as A. aceti. It does not prove BCRC supply or authenticate the experimental
    culture; no organism CURIE is assigned.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 9ab8ab850ccfc0eac7a2ce3e3d15f645520c1d369edf742be861142375b7abe5
- evidence_id: metadata
  kind: primary_source
  reference: https://api.crossref.org/works/10.1186%2Fs40643-017-0173-5
  locator: Fresh exact DOI authority response, compared with original first page.
  summary: Four authors, title, DOI and 2017 publication agree. A newer publisher-platform
    page date is not interpreted as a new study or correction.
  accessed_at: '2026-10-16T08:23:56.366813Z'
  support: supports
  snapshot_sha256: 664e4cdca99a22b2670393b42886cdb6fd1928f802faca035412f1dde9832c58
assessments:
- assessment_id: identity
  area: identity
  topic: Commercial solder identity and provenance
  outcome: supported
  summary: The commodity and specimen scope are supported without assuming a waste
    origin.
  details: Methods identify Taiwan-Solid Enterprises material nominally Sn-Cu 63–37%;
    no service history. SEM/EDS discussion suggests tin-rich coating and copper-containing
    core but does not establish homogeneous bulk alloy or a quantitative assay. The
    record faithfully reports the unusual nominal ratio without silently changing
    it. No mineral or elemental ID or inherited criticality designation is assigned.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - primary
  - dedup
- assessment_id: conditions
  area: consistency
  topic: Culture preparation, substrate and conditions
  outcome: supported
  summary: The accepted microbial-arm conditions match the full original.
  details: Methods give 3 mm pieces, 100 mg, 4 mL Acetobacter culture, 24 h culture
    growth then 30 h leaching at 30 C/150 rpm; washing uses water and 75% ethanol.
    Results instead call the liquid supernatant. Cell removal/viability cannot be
    resolved, and the owner preserves this ambiguity rather than assigning live-cell
    contact. Three sets are reported without defined statistics or biological independence.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - primary
- assessment_id: organism
  area: identity
  topic: Collection identity versus experiment authentication
  outcome: supported
  summary: The authority claim is accurate and the experimental mismatch is preserved.
  details: The paper names TISTR 102 but says BCRC Taiwan; fresh authority says pasteurianus
    with historical aceti. Catalogue identity is correctly not converted into authenticated
    culture identity. The mechanism remains Acetobacter preparation rather than an
    invented species/strain accession.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - primary
  - culture
- assessment_id: mechanism
  area: evidence
  topic: Culture-associated dissolution and causal limits
  outcome: supported
  summary: Figure 7 supports time-dependent dissolved Cu/Sn, not net microbial benefit
    or isolated recovery.
  details: Figure 7 contains 10/20/30 h bars and the reported dissolved endpoint.
    YGEA includes acetic acid; titration estimates total acidity and its underlying
    data are not shown. No matched uninoculated-medium/acid-only arm is provided.
    Low-strength chemical-acid series uses 10 mL rather than 4 mL, so it cannot quantify
    benefit. Figure 8 belongs to 80% chemical-acid treatment and supplies no direct
    microbial contact/mineralization evidence.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - primary
- assessment_id: deployment
  area: scope
  topic: Scale, numerical claims and deferred source
  outcome: supported
  summary: Laboratory material testing is not industrial treatment of end-of-life
    solder.
  details: Generic recycling/economic prose and the 2014 secondary comparison do not
    establish the 2017 feed as waste, industrial deployment, or reusable quantitative
    yield. Exact percentages remain unadopted given composition/denominator uncertainty.
    Complete 2014 original was not obtained, so its fungal mechanisms and values are
    not accepted.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - primary
  - notices
- assessment_id: provenance
  area: provenance
  topic: Exact current inputs and completed checks
  outcome: supported
  summary: Frozen record/history/schema/dossier and completed checks are verified
    for this owner.
  details: Actual inline CREATE and linked canonical CREATE metadata, timestamps and
    target are coherent. Reviewer did not mutate target/history. Named records/history
    and root four-command batch all pass with current hash/log binding. The final
    scientific review is limited to this assigned owner, not the entire corpus.
  target_ids:
  - cmmmech:tin-copper-solder
  evidence_ids:
  - owner
  - provenance
  - named
  - batch
  - metadata
findings: []
actions: []
limitations:
- The assay does not isolate newly biosynthesized acetic acid, establish live-cell
  necessity or demonstrate net microbial enhancement over a matched control.
- The experimental culture was not authenticated; the fresh catalogue resolution cannot
  repair the BCRC/TISTR supply mismatch.
- Nominal 63–37% composition, bulk homogeneity, extraction denominator and error-bar
  meaning are not independently resolved; no yield digitization or pooled measurement
  performed.
- The 2014 original and underlying culture-acidity data were not acquired; no industrial
  deployment or spent-feed history is established.
- Notice and hidden/ignored-inclusive duplicate searches are bounded; absence is not
  claimed outside recorded roots/results.
notes:
- Raw copyrighted literature and renders remain outside Git; source access does not
  authorize redistribution.
- Source-evidence follow-ups are not fabricated current curator defects. No fresh
  scientific review of other corpus owners.
```
