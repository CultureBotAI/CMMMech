# Independent scientific review of Germanite

- Review: 20261012T025122Z-germanite-round43-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-12T02:37:03.998473Z
- Finished UTC: 2026-10-12T02:51:22.601063Z
- Reviewer: Codex /root/round43_hardmetal (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Dated mineral identity and bounded primary mineralogical context are supported, with specimen, nomenclature and evidence limits preserved. No corrective findings in the whole-record scope.

## Scope And Provenance

Whole new mineral identity record, source-backed description and canonical CREATE provenance.

Selection: All claims in this assigned new material owner.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 59e24ec38d9c7b377dcfeade1637b298aab9623e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:germanite | data/records/germanite.yaml | maintained | Germanite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named validation | passed | True | cmmmech:germanite | Reviewer executed to terminal 0 (session 4668), Checked 2 record(s); 0 failed. Log /private/tmp/cmm-round43-ge-independent-named.log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042 |
| Completed parent batch gate | passed | True | cmmmech:germanite | Parent executed to terminal 0; reviewer independently read and hash-verified receipt/log. /private/tmp/cmm-round43-final-v2-batch.log SHA256 3b461ec716372779d864a3273f66a8f5e36a3275912d2edc011da55513defab4. uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 214.77s (0:03:34)<br>Checked 220 record(s); 0 failed.<br>Checked 259 history record(s); 0 error(s). |
| Completed parent nonempty gate | passed | True | cmmmech:germanite | Parent executed to terminal 0; reviewer independently read and hash-verified receipt/log. /private/tmp/cmm-round43-final-v2-nonempty.log SHA256 5f5111acf2e1d4f13998e3baccfe8b9a433c95528bd47cfbc3572bbbef706f99. Checked 220 record(s); 0 failed. |
| Completed parent history gate | passed | True | cmmmech:germanite | Parent executed to terminal 0; reviewer independently read and hash-verified receipt/log. /private/tmp/cmm-round43-final-v2-history.log SHA256 a7e1e37a7ef921c16b129f63f7319e52d3effcf1660ec0e77c1d93369e0f3063. Checked 259 history record(s); 0 error(s). |

## Scientific And Domain Assessments

### Species identity, formula and dated nomenclature

identity: supported. Targets: cmmmech:germanite.

September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent. Neither date nor specimen number is represented as a mineral identifier.

### Primary specimen context, intergrowths and limits

evidence: supported. Targets: cmmmech:germanite.

The complete Handbook page supports Tsumeb dolostone-hosted hydrothermal Cu-Pb-Zn occurrence and renierite association. The primary bulk specimen contains tennantite, sphalerite and galena impurities; cation-site assignment is explicitly nonunique. The record retains these qualifications and the Handbook F-43n versus primary P-43n discrepancy, without adopting suspect crystal-size text.

### Exact reviewed state and completed required checks

provenance: supported. Targets: cmmmech:germanite.

Native inputs were captured before assessment and remain byte-identical. Canonical CREATE history is distinct from inline event and review. Named and parent batch gates passed; no previous history or review rewritten.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/germanite.yaml; Whole exact current record | supports | September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent. Neither date nor specimen number is represented as a mineral identifier. |
| ima | https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf; September 2026 PDF definitions page 1 and species row page 82 | supports | September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent. Neither date nor specimen number is represented as a mineral identifier. |
| handbook | https://handbookofmineralogy.org/pdfs/germanite.pdf; Complete version 1 copyright 2001-2005 one-page entry | supports | The complete Handbook page supports Tsumeb dolostone-hosted hydrothermal Cu-Pb-Zn occurrence and renierite association. The primary bulk specimen contains tennantite, sphalerite and galena impurities; cation-site assignment is explicitly nonunique. The record retains these qualifications and the Handbook F-43n versus primary P-43n discrepancy, without adopting suspect crystal-size text. |
| primary | https://msaweb.org/AmMin/AM69/AM69_943.pdf; Tettenhorst and Corbato 1984, pp. 943-947: experimental/refinement and discussion; directly viewed original pp. 943, 945, 946 with Tables 2-4. Five-page extracted text consulted for accepted claims; Table 1 original page not visually rechecked. | supports | The primary supports a cubic specimen interpretation and doubled ideal formula while admitting microscopic impurities and inability to distinguish cation sites. No numerical table values are imported. Directly viewed p. 943 confirms P-43n, and pp. 945-946 confirm nonunique cation assignment and impure bulk specimen. |
| history | history/records/germanite/2026-10-12T023451Z-codex-bac8ae.yaml; Whole CREATE sidecar and separate inline event | supports | Actual actor, model, tool, target and timestamps agree with this uncommitted curation; no claim of past authorship or review-as-curation. Parent trusted-base history gate passed. |
| inspection | /private/tmp/cmm-round43-ge-independent-research/evidence-check.json; Original page inspection,42 artifact hash checks and actual acquisition/search details | supports | Reviewer independently inspected 14 original page images across both mineral reviews, verified 42 declared artifacts and freshly downloaded both primary PDFs which match curator bytes. IMA and Handbook artifacts reused with verified provenance, not claimed fresh reviewer downloads. Native inspect preceded assessment; after inspection-only target-kind metadata correction, recaptured source input hashes are identical. |
| search | /private/tmp/cmm-round43-ge-independent-research/evidence-check.json; Three exact title/author/notice and mineral-microbial queries | context_only | No affecting formal notice or verified mineral-specific microbial experiment was identified in these bounded returned sets. MSA web opens failed internally; direct authorized downloads returned 200 and matched. No absence of all notices or all mechanisms is claimed. |
| dedup | /private/tmp/cmm-round43-ge-independent-research/corpus-dedup-receipt.json; Independent current data/records hidden/ignored-inclusive symlink-following search | context_only | Current accepted record search has exactly these two owners and their explicit crossreferences. Author broader scientific/raw-root search read and hash-checked, not independently rerun; unextracted binaries and missing raw references remain explicit. |
| checks | /private/tmp/cmm-round43-final-terminal.json; Actual completed parent batch/nonempty/trusted-base history receipt | supports | All required checks completed successfully and logs independently hash-verified. Structural gates do not prove scientific claims. |

## Limits And Additional Notes

- IMA authority explicitly dated September 2026; Handbook historical context is not present-day production evidence.
- Primary numerical diffraction table 1 was not visually rechecked and no refinement was recomputed; the accepted claims are bounded identity, cubic context and explicitly retained primary limitations.
- No criticality designation, microbial mechanism, quantitative recovery or industrial deployment is asserted.
- Bounded notice/dedup searches do not establish universal absence or source-frontier exhaustion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T025122Z-germanite-round43-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent scientific review of Germanite
started_at: '2026-10-12T02:37:03.998473Z'
finished_at: '2026-10-12T02:51:22.601063Z'
reviewer:
  identity: Codex /root/round43_hardmetal
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored the mineral records, histories and source dossier.
    This reviewer authored none of those bytes and independently inspected source
    images/text, refreshed primary downloads, checked nomenclature/scope and validated
    records. Reviewer curated a separate titanium record in this batch.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Dated mineral identity and bounded primary mineralogical context are supported,
  with specimen, nomenclature and evidence limits preserved. No corrective findings
  in the whole-record scope.
source:
  git_revision: 59e24ec38d9c7b377dcfeade1637b298aab9623e
  state: working_tree
  inputs:
  - path: data/records/germanite.yaml
    sha256: 7a15d724ccb45945471b744657f8e43e00aec76a37d4a49d8ddb08a35a0fad14
    role: target
  - path: history/records/germanite/2026-10-12T023451Z-codex-bac8ae.yaml
    sha256: 4064d4559fd27ed2f508925eebff9efbbe79a66f07215fcbf53372e15720db8d
    role: context
  - path: research/sources/round43-ge-minerals/20261012T023445Z-source-investigation.json
    sha256: 2ea7a4c287e9b9fb1048ec29eb97c6563b961b4c15d2f0422875117ef8f72210
    role: context
targets:
- target_id: cmmmech:germanite
  path: data/records/germanite.yaml
  label: Germanite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/germanite.yaml
    role: scientific_record
scope:
  description: Whole new mineral identity record, source-backed description and canonical
    CREATE provenance.
  selection: All claims in this assigned new material owner.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:germanite
  exclusions:
  - target: Unasserted extraction experiments, detailed physical-property values and
      later crystallographic refinements
    reason: Not claimed by the record; require a separately scoped primary assessment
      before curation.
checks:
- check_id: named
  name: Independent named validation
  command: uv run --locked cmmmech validate data/records/germanite.yaml data/records/renierite.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Reviewer executed to terminal 0 (session 4668), Checked 2 record(s); 0
    failed. Log /private/tmp/cmm-round43-ge-independent-named.log SHA256 4022ad8ba440a72bf4f1c8b321e447df36133d812f52f21611becf103551b042
  target_ids:
  - cmmmech:germanite
- check_id: batch
  name: Completed parent batch gate
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed to terminal 0; reviewer independently read and hash-verified
    receipt/log. /private/tmp/cmm-round43-final-v2-batch.log SHA256 3b461ec716372779d864a3273f66a8f5e36a3275912d2edc011da55513defab4.
    uv run --locked --extra dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 214.77s (0:03:34)

    Checked 220 record(s); 0 failed.

    Checked 259 history record(s); 0 error(s).'
  target_ids:
  - cmmmech:germanite
- check_id: nonempty
  name: Completed parent nonempty gate
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Parent executed to terminal 0; reviewer independently read and hash-verified
    receipt/log. /private/tmp/cmm-round43-final-v2-nonempty.log SHA256 5f5111acf2e1d4f13998e3baccfe8b9a433c95528bd47cfbc3572bbbef706f99.
    Checked 220 record(s); 0 failed.
  target_ids:
  - cmmmech:germanite
- check_id: history
  name: Completed parent history gate
  command: uv run --locked cmmmech validate-history --base 59e24ec38d9c7b377dcfeade1637b298aab9623e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Parent executed to terminal 0; reviewer independently read and hash-verified
    receipt/log. /private/tmp/cmm-round43-final-v2-history.log SHA256 a7e1e37a7ef921c16b129f63f7319e52d3effcf1660ec0e77c1d93369e0f3063.
    Checked 259 history record(s); 0 error(s).
  target_ids:
  - cmmmech:germanite
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/germanite.yaml
  locator: Whole exact current record
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description
    year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent.
    Neither date nor specimen number is represented as a mineral identifier.
  snapshot_sha256: 7a15d724ccb45945471b744657f8e43e00aec76a37d4a49d8ddb08a35a0fad14
- evidence_id: ima
  kind: authority
  reference: https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf
  locator: September 2026 PDF definitions page 1 and species row page 82
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description
    year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent.
    Neither date nor specimen number is represented as a mineral identifier.
  snapshot_sha256: 2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973
- evidence_id: handbook
  kind: authority
  reference: https://handbookofmineralogy.org/pdfs/germanite.pdf
  locator: Complete version 1 copyright 2001-2005 one-page entry
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: The complete Handbook page supports Tsumeb dolostone-hosted hydrothermal
    Cu-Pb-Zn occurrence and renierite association. The primary bulk specimen contains
    tennantite, sphalerite and galena impurities; cation-site assignment is explicitly
    nonunique. The record retains these qualifications and the Handbook F-43n versus
    primary P-43n discrepancy, without adopting suspect crystal-size text.
  snapshot_sha256: ce2f16ea20ce7b9c82f2c29c8c69a43d882fb7612ddf65cdbc5ba1d7d15cd8cf
- evidence_id: primary
  kind: primary_source
  reference: https://msaweb.org/AmMin/AM69/AM69_943.pdf
  locator: 'Tettenhorst and Corbato 1984, pp. 943-947: experimental/refinement and
    discussion; directly viewed original pp. 943, 945, 946 with Tables 2-4. Five-page
    extracted text consulted for accepted claims; Table 1 original page not visually
    rechecked.'
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: The primary supports a cubic specimen interpretation and doubled ideal
    formula while admitting microscopic impurities and inability to distinguish cation
    sites. No numerical table values are imported. Directly viewed p. 943 confirms
    P-43n, and pp. 945-946 confirm nonunique cation assignment and impure bulk specimen.
  snapshot_sha256: 4c9fa9ad7d8aed4ecf3e6b0cc9f260612a22739cd203080001d97d29d9306a70
- evidence_id: history
  kind: record_content
  reference: history/records/germanite/2026-10-12T023451Z-codex-bac8ae.yaml
  locator: Whole CREATE sidecar and separate inline event
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: Actual actor, model, tool, target and timestamps agree with this uncommitted
    curation; no claim of past authorship or review-as-curation. Parent trusted-base
    history gate passed.
  snapshot_sha256: 4064d4559fd27ed2f508925eebff9efbbe79a66f07215fcbf53372e15720db8d
- evidence_id: inspection
  kind: record_content
  reference: /private/tmp/cmm-round43-ge-independent-research/evidence-check.json
  locator: Original page inspection,42 artifact hash checks and actual acquisition/search
    details
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: Reviewer independently inspected 14 original page images across both mineral
    reviews, verified 42 declared artifacts and freshly downloaded both primary PDFs
    which match curator bytes. IMA and Handbook artifacts reused with verified provenance,
    not claimed fresh reviewer downloads. Native inspect preceded assessment; after
    inspection-only target-kind metadata correction, recaptured source input hashes
    are identical.
  snapshot_sha256: 1e71e2e3c54268faabdb1f18c35ca906838fd2d5f21ac01c216cb8d78b4f08ce
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round43-ge-independent-research/evidence-check.json
  locator: Three exact title/author/notice and mineral-microbial queries
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: context_only
  summary: No affecting formal notice or verified mineral-specific microbial experiment
    was identified in these bounded returned sets. MSA web opens failed internally;
    direct authorized downloads returned 200 and matched. No absence of all notices
    or all mechanisms is claimed.
  snapshot_sha256: 1e71e2e3c54268faabdb1f18c35ca906838fd2d5f21ac01c216cb8d78b4f08ce
  search_scope: 'web.run 2026-10-12: "Tettenhorst" "Corbato" "germanite" correction
    erratum; "Bernstein" "Renierite" "1986" erratum correction; "germanite" "renierite"
    bioleaching microorganisms. First returned sets only; no filters/pagination.'
- evidence_id: dedup
  kind: search
  reference: /private/tmp/cmm-round43-ge-independent-research/corpus-dedup-receipt.json
  locator: Independent current data/records hidden/ignored-inclusive symlink-following
    search
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: context_only
  summary: Current accepted record search has exactly these two owners and their explicit
    crossreferences. Author broader scientific/raw-root search read and hash-checked,
    not independently rerun; unextracted binaries and missing raw references remain
    explicit.
  snapshot_sha256: 629f227a05ef89494c083dd4c91c70810823f4b1de13b0a26fd083d0a0ea2e27
  search_scope: rg --no-ignore --hidden --follow over complete current data/records.
    Broader author current/scientific and 135 raw-root boundary and missing paths
    inspected in curator dossier, not independently rerun. Not a machine-wide absence
    assertion.
- evidence_id: checks
  kind: validation
  reference: /private/tmp/cmm-round43-final-terminal.json
  locator: Actual completed parent batch/nonempty/trusted-base history receipt
  accessed_at: '2026-10-12T02:51:22.601063Z'
  support: supports
  summary: All required checks completed successfully and logs independently hash-verified.
    Structural gates do not prove scientific claims.
  snapshot_sha256: f3793509763515344bdb4e1474284705fc01318d2ebd6d8ab827e5885f714cb6
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity, formula and dated nomenclature
  outcome: supported
  target_ids:
  - cmmmech:germanite
  summary: September 2026 IMA gives Germanite, Cu13Fe2Ge2S16, G status and 1922 original-description
    year. The primary doubled formula Cu26Ge4Fe4S32 is stoichiometrically equivalent.
    Neither date nor specimen number is represented as a mineral identifier.
  evidence_ids:
  - record
  - ima
  - handbook
  - primary
  dimensions:
  - name: material
    value: Mineral species
    definition: Distinct from germanium element, a bulk ore/feed and the other mineral
      owner.
    evidence_ids:
    - record
    - ima
  - name: criticality
    value: Not asserted
    definition: No constituent-element designation is inherited into the mineral.
    evidence_ids:
    - record
  - name: mechanism
    value: Not asserted
    definition: Mineralogical measurements do not establish microbial extraction,
      product recovery or deployment.
    evidence_ids:
    - record
    - primary
- assessment_id: context
  area: evidence
  topic: Primary specimen context, intergrowths and limits
  outcome: supported
  target_ids:
  - cmmmech:germanite
  summary: The complete Handbook page supports Tsumeb dolostone-hosted hydrothermal
    Cu-Pb-Zn occurrence and renierite association. The primary bulk specimen contains
    tennantite, sphalerite and galena impurities; cation-site assignment is explicitly
    nonunique. The record retains these qualifications and the Handbook F-43n versus
    primary P-43n discrepancy, without adopting suspect crystal-size text.
  evidence_ids:
  - primary
  - handbook
  - inspection
- assessment_id: provenance
  area: provenance
  topic: Exact reviewed state and completed required checks
  outcome: supported
  target_ids:
  - cmmmech:germanite
  summary: Native inputs were captured before assessment and remain byte-identical.
    Canonical CREATE history is distinct from inline event and review. Named and parent
    batch gates passed; no previous history or review rewritten.
  evidence_ids:
  - record
  - history
  - checks
  - inspection
findings: []
actions: []
limitations:
- IMA authority explicitly dated September 2026; Handbook historical context is not
  present-day production evidence.
- Primary numerical diffraction table 1 was not visually rechecked and no refinement
  was recomputed; the accepted claims are bounded identity, cubic context and explicitly
  retained primary limitations.
- No criticality designation, microbial mechanism, quantitative recovery or industrial
  deployment is asserted.
- Bounded notice/dedup searches do not establish universal absence or source-frontier
  exhaustion.
tags:
- round43
- independent
- mineral
- identity
```
