# Independent review of staged PCB ferric regeneration and paired dataset

- Review: 20261011T132452Z-waste-printed-circuit-boards-round22-independent
- Repository: CultureBotAI/CMMMech
- Started UTC: 2026-10-11T13:18:07.559222Z
- Finished UTC: 2026-10-11T13:24:52.755478Z
- Reviewer: Codex /root/round22_seafloor_sulfides (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The added 2024 mechanism correctly separates chemical ferric leaching, living-community liquor regeneration, actual-liquor solvent extraction and synthetic-feed electrowinning. Primary manuscript and paired workbook support its conditional laboratory claims, including retained acid-wash, feed, timing, units and current-efficiency discrepancies. Earlier mechanisms are unchanged and their prior independent review is transparently carried forward. A minor dossier readability issue raised before saving was corrected and rechecked; no actionable record defect remains in this review scope.

## Scope And Provenance

Full current record and provenance integration inspected. Fresh primary-literature assessment concerns the new 2024 staged-mobile-phone mechanism and paired 2024 dataset; previous 2021/2022 mechanisms are covered by exact field-preservation checks and their identified prior independent scientific review, not falsely presented as newly reread primary literature.

Selection: One assigned maintained PCB target, including all fields, its added mechanism, paired dossier and both actual history sidecars.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b19103bb393096e405bbecd2808a1aa0e01bb200.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cmmmech:waste-printed-circuit-boards | data/records/waste-printed-circuit-boards.yaml | maintained | Waste printed circuit boards |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent named-record validation | passed | True | cmmmech:waste-printed-circuit-boards | Reviewer executed; Checked 1 record(s); 0 failed. Terminal exit 0 observed (session 6018). Target remained unchanged through final inspect. |
| Native full checks | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read the completed receipt and terminal logs. /private/tmp/cmm-round22-final-batch.log: uv run --locked --extra dev python scripts/check.py<br>All checks passed!<br>........................................................................ [ 23%]<br>........................................................................ [ 46%]<br>........................................................................ [ 69%]<br>....................................................sss................. [ 92%]<br>.......................                                                  [100%]<br>308 passed, 3 skipped in 124.01s (0:02:04)<br>Checked 154 record(s); 0 failed.<br>Checked 173 history record(s); 0 error(s).<br> |
| Required corpus | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read the completed receipt and terminal logs. /private/tmp/cmm-round22-final-require.log: Checked 154 record(s); 0 failed.<br> |
| Trusted-base history | passed | True | cmmmech:waste-printed-circuit-boards | Parent executed; reviewer independently read the completed receipt and terminal logs. /private/tmp/cmm-round22-final-history.log: Checked 173 history record(s); 0 error(s).<br> |

## Scientific And Domain Assessments

### Maintained heterogeneous secondary resource

identity: supported. Targets: cmmmech:waste-printed-circuit-boards.

The new study belongs under the existing waste-board resource. It does not define a new element, mineral, commodity or universal board composition, and its dataset/mirror are not separate experiments. No unsupported identifier or inherited criticality claim is introduced.

### Conditional living-community ferric regeneration

evidence: supported. Targets: cmmmech:waste-printed-circuit-boards.

The measured column inlet/outlet results support operational regeneration under the reported conditions. Loading-dependent residual Fe(II), altered flow and missing sterile/replicated controls prevent exclusive microbial effect sizes, member-specific attribution or universal inhibition-tolerance claims.

### Measured chemistry, fitted trajectories and residue accounting

evidence: supported. Targets: cmmmech:waste-printed-circuit-boards.

The paper-attributed approximate 99% extraction estimate is appropriately qualified rather than imported as an independently reproduced reactor-only balance. Acid washing, copper-spiked inlet, sampled fractions, heterogeneous feed and workbook normalization prevent direct whole-board recovery accounting.

### Actual-liquor solvent extraction and synthetic electrowinning

evidence: supported. Targets: cmmmech:waste-printed-circuit-boards.

Actual biooxidized liquor supports a solvent-extraction stage. Explicitly synthetic electrowinning and simulated stripping solutions prevent attributing the metal deposit to actual board-derived copper or claiming a tested closed loop. Current efficiency and local Cu-rich EDS do not prove bulk purity.

### Transparent carryforward of unchanged older mechanisms

provenance: supported. Targets: cmmmech:waste-printed-circuit-boards.

The current full record preserves both prior mechanisms and their evidential qualifications, with actual field-equality proof and a specifically identified corrected independent review. This review freshly evaluates only the added 2024 evidence; no false claim of rereading 2021/2022 literature or repeated independence is made.

### Actual EDIT, frozen inputs and completed native gates

provenance: supported. Targets: cmmmech:waste-printed-circuit-boards.

Initial canonical inspection preceded judging the PCB evidence. After root corrected the source-dossier spacing, that changed context was read again and re-inspected with actual CREATE/EDIT sidecars. Final target bytes match both initial and gated target hashes. Native checks pass; their structural success is not used as scientific proof.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/records/waste-printed-circuit-boards.yaml; Complete current record; new EDIT and unchanged CREATE sidecars | supports | The heterogeneous secondary-resource identity, three distinct mechanisms, source entries, actual codex/GPT-6 EDIT at 13:15:57Z and separately recorded inline event at 13:16:41Z are coherent. No material/community CURIE or criticality designation is asserted. |
| primary | https://doi.org/10.1016/j.mineng.2023.108459; Accepted manuscript: full Methods 2.1–2.2, Results 3.1–3.5, relevant introduction/conclusions; Tables 2–6. Figures 2–8 visually inspected via rendered PDF pages 16,17,19,22,23,24; Tables 5–6 visually inspected on pages 20–21. Table 4 and Figure 1 caption read on page 12; Figure 1 graphic was not visually inspected. | supports | Actual ground end-of-life mobile-phone feed, chemically leached with biogenic ferric, supplied a separately tested living Riotinto community column. Table 6 reports loading-dependent Fe(II) outlet behavior. Actual biooxidized liquor underwent solvent extraction; manuscript Methods and Results explicitly identify synthetic electrowinning solution. |
| primary_limits | https://doi.org/10.1016/j.mineng.2023.108459; Methods 2.1–2.2; Table 4; Results 3.2–3.5; Figures 4–8 and Tables 5–6 | partial | No matched sterile biooxidation comparator or replicated whole process is described in inspected Methods/Results. At 95 h, inlet Fe(II) 9.29 g/L with Cu 10.45 g/L leaves 2.37 g/L Fe(II); later zero outlet follows reduced liquid flow. Table 4 AP SX/150 g/L acid conflicts with Methods/Results synthetic/155 g/L acid. SEM-EDS is local composition, and 99.2% is current efficiency, not certified product purity or actual-board recovery yield. Fitted batch/depletion curves and proposed closed-loop performance are not independent observations. |
| dataset | https://doi.org/10.12795/11441/161670; Original Data.xlsx, freshly parsed ZIP/XML; composition B21,D23:D24,T8; Batch C2,B9,B11:B13; every nonempty CSTR, biooxidation and EW cell; selected SX G2:H3 cells | partial | Six sheets contain 1,435 nonempty cells (170 composition, 895 Batch, 20 CSTR, 83 biooxidation, 213 SX, 54 EW). Independent parsing reproduces the documented retained-solid HCl wash and 62.03 to 53 g mass change; batch 1.2 L label; biooxidation g/h heading and mixed 2023/2024 dates; EW C16=1.02 and additional 50-degree series; differing Au mean and SX Fe increase. Only selected SX cells were scientifically inspected; all parsed formulas were not recalculated. These are same-experiment data and limitations, not independent replication. |
| dataset_readme | https://doi.org/10.12795/11441/161670; Original repository README, complete text | partial | README supplies feed preparation, methods and six-sheet identities, but its 2–7 mm range conflicts with manuscript target 800–2000 micrometres, and stated 10-01-2022 collection date conflicts with workbook biooxidation dates. No chronological or density conversion is invented. |
| paper_identity | https://api.crossref.org/works/10.1016/j.mineng.2023.108459; Retained Crossref response and primary title/author metadata | supports | Crossref and source metadata support Iglesias-González, Dorado, Ramírez and Mazuelos, January 2024 Minerals Engineering 205:108459. The Seville cover year 2003 is not adopted. No update-to relation appears in the inspected response; that is not an exhaustive notice audit. |
| dataset_identity | https://doi.org/10.12795/11441/161670; Official repository dataset metadata and acquired README/workbook bundle | supports | Dataset DOI and authors agree with the paired experiment; deposit/issue is 25 July 2024, distinct from declared data creation date. Metadata identifies CC BY 4.0 for the dataset; no rights are inferred for other publisher artifacts. |
| carryforward | reviews/structured/20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction/review.yaml; Corrected round21 independent review plus comparison to b19103bb393096e405bbecd2808a1aa0e01bb200 | supports | The first two full mechanisms, first two sources, existing inline curation-history and history-ref prefixes are semantically identical to the trusted base. Their independent scientific assessment is retained with its explicit Figure 1 inspection-provenance correction. Those 2021/2022 primary studies were not freshly reread by this reviewer. |
| preservation | /private/tmp/cmm-round22-pcb-independent/checks.json; Successful .venv Python field comparison and bounded hidden/ignored-following dedup receipt | supports | Verified the exact preserved old scientific/provenance prefixes against the trusted base; searched DOI/title patterns across data/records, research, reviews, history and cited round21/round22 PCB raw directories. Matching scientific owners were this target and its frontier/dossiers, without a duplicate new experiment in other maintained records in this bounded scope. |
| search | /private/tmp/cmm-round22-pcb-independent/search.json; Three exact DOI/title correction/synthetic/dataset queries, 11 October 2026 | context_only | Independent queries: DOI 10.1016/j.mineng.2023.108459 correction erratum retraction; exact article-title prefix with synthetic; DOI 10.12795/11441/161670. First returned sets identified no directly affecting notice; official UPC source results support synthetic electrowinning and source identity. Irrelevant results were not used. |
| gates | /private/tmp/cmm-round22-gate-receipts.json; Completed parent batch/require/history terminal receipt and logs; frozen target hash file | supports | Root executed all three gates to exit 0: 308 tests passed, 3 skipped; 154 records and 173 histories. Reviewer independently read each completed terminal log and verified the target equals the gated SHA-256. Named file validation was independently executed by this reviewer. |
| dossier_fix | research/ingests/round22-pcb-sources-20261011.md; Re-read final source Markdown after pre-save publication issue CultureBotAI/CMMMech#81 | supports | Joined quantities identified during this review were corrected by root with spaces; final dossier is readable and preserves scientific content/URLs. Final context SHA-256 is da3ccffa12df5af65e8515d6532ba73c1608a7b1955a054974867cc7c6fbf6f2. The unchanged target was reinspected with this corrected context before save. |

## Limits And Additional Notes

- Fresh primary-literature work covers the added 2024 study and paired dataset. Earlier 2021/2022 scientific assessments are carried forward only for field-identical content from the named prior independent review.
- No matched sterile biooxidation column, replicated full process, species-resolved causal assay or independent laboratory reproduction is available in the reviewed evidence.
- The original XLSX was parsed afresh and focused cells inspected, but every formula was not recalculated and raw instrument traces were not independently audited.
- Particle-size, batch-volume, dataset-date/flow-unit, acid concentration/origin, Au assay and current-efficiency discrepancies remain unresolved and explicitly limit interpretation.
- Feed heterogeneity, commercial inlet copper and acid-washed/sampled solids prevent treating paper-reported extraction as an independently closed reactor-only Cu balance.
- Synthetic electrowinning, local SEM-EDS and current efficiency do not demonstrate certified bulk purity, actual-board metal recovery, an operating closed loop or industrial deployment.
- Live searches covered first returned result sets without pagination; no exhaustive literature or notice-registry absence is asserted. Figure 1 graphic was not visually inspected, although its caption/conceptual description was read.
- Evidence access times denote completion of this review interval, which began at the recorded actual UTC start; they do not imply new downloads of curator-acquired sources. Primary reading, direct figure inspection, fresh workbook parsing and searches occurred within that interval.
- Temporary gate helper adaptations were authored by this reviewer but root executed the batch commands. Receipt/log inspection and target-hash comparison were independent; checks are not represented as reviewer executions except named validation.
- Minor dossier readability finding was raised before the first canonical save, tracked by root as CultureBotAI/CMMMech#81 (https://github.com/CultureBotAI/CMMMech/issues/81), corrected and independently verified. No previous structured finding existed, so no fabricated resolved finding or previous_occurrences lineage is added. Issue closure remains the parent publication workflow responsibility.
- The original round21 review had an inspection-provenance correction retained in its successor. This review cites that corrected assessment transparently and does not alter, silently replace or claim to resolve an earlier structured finding.
- An initial independent prefix-check invocation with system Python lacked PyYAML; rerunning with the project .venv Python succeeded. This transient environment mismatch did not affect any scientific file or the successful checks recorded here.
- No PCB record, history or source dossier was edited by this reviewer. Raw PDFs, original workbook, images and extracted text remain outside Git.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T132452Z-waste-printed-circuit-boards-round22-independent
kind: record
repository: CultureBotAI/CMMMech
title: Independent review of staged PCB ferric regeneration and paired dataset
started_at: '2026-10-11T13:18:07.559222Z'
finished_at: '2026-10-11T13:24:52.755478Z'
reviewer:
  identity: Codex /root/round22_seafloor_sulfides
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Root authored the PCB extension and its source dossiers. This
    reviewer authored the separate sulfide record, independently read the PCB primary
    manuscript and selected rendered figures/tables, parsed the original XLSX afresh,
    searched notice/identity evidence and compared prior record fields. No PCB record/history/source-dossier
    edits were made by this reviewer. Shared worktree and curator-acquired source
    files are disclosed; the temporary batch-gate helpers were prepared by this reviewer
    and executed by root.
skill: .claude/skills/review-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The added 2024 mechanism correctly separates chemical ferric leaching, living-community
  liquor regeneration, actual-liquor solvent extraction and synthetic-feed electrowinning.
  Primary manuscript and paired workbook support its conditional laboratory claims,
  including retained acid-wash, feed, timing, units and current-efficiency discrepancies.
  Earlier mechanisms are unchanged and their prior independent review is transparently
  carried forward. A minor dossier readability issue raised before saving was corrected
  and rechecked; no actionable record defect remains in this review scope.
source:
  git_revision: b19103bb393096e405bbecd2808a1aa0e01bb200
  state: working_tree
  inputs:
  - path: data/records/waste-printed-circuit-boards.yaml
    sha256: 08994df8c73e773c677d9a0397c86c4a23b698380d870923b255fccffb7888dd
    role: target
  - path: docs/records.md
    sha256: 381bbb73b78607fe4729512f0c30e1f0f3cf010344c88104e84d495639f69c9b
    role: context
  - path: history/records/waste-printed-circuit-boards/2026-10-11T124047Z-codex-fd23ae.yaml
    sha256: b5ee90ea4961aba93941dbde5f68872e19609831c2cb366f55b9d4455d5f94bb
    role: context
  - path: history/records/waste-printed-circuit-boards/2026-10-11T131557Z-codex-cd46c3.yaml
    sha256: 2990a3d5082ea2cbf5c7fb2aa264f2e9c8abdd119ce93e700b4d245b7c4a5803
    role: context
  - path: research/ingests/round22-pcb-sources-20261011.json
    sha256: 081fd307fd198dbe63d1d0ff2244f961178863feb3cbeb20236aab5c3bfc020b
    role: context
  - path: research/ingests/round22-pcb-sources-20261011.md
    sha256: da3ccffa12df5af65e8515d6532ba73c1608a7b1955a054974867cc7c6fbf6f2
    role: context
  - path: reviews/structured/20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction/review.yaml
    sha256: 34cb3db9d4050912e3be7540c7b5e1c2219cff20a98ec8ee2004c21adaba0406
    role: context
  - path: src/cmmmech/schema/cmmmech.yaml
    sha256: f13df7392fb27e6ff2c1fa658446cdac9bc1e1c544ef9cb903578107f1d66f1c
    role: context
scope:
  description: Full current record and provenance integration inspected. Fresh primary-literature
    assessment concerns the new 2024 staged-mobile-phone mechanism and paired 2024
    dataset; previous 2021/2022 mechanisms are covered by exact field-preservation
    checks and their identified prior independent scientific review, not falsely presented
    as newly reread primary literature.
  selection: One assigned maintained PCB target, including all fields, its added mechanism,
    paired dossier and both actual history sidecars.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cmmmech:waste-printed-circuit-boards
  exclusions:
  - target: Fresh reassessment of unchanged 2021/2022 primary studies
    reason: Their mechanisms, sources and history prefixes equal the trusted base.
      The corrected round21 independent scientific review is explicitly carried forward;
      no new reading of those earlier primary papers is claimed.
  - target: Every workbook formula, raw instrument traces, author clarification and
      other corpus records
    reason: The workbook was freshly parsed in full, with focused scientific inspection
      of relevant cells. This is not numerical reproduction of every model, laboratory
      replication or corpus-wide scientific review.
targets:
- target_id: cmmmech:waste-printed-circuit-boards
  path: data/records/waste-printed-circuit-boards.yaml
  label: Waste printed circuit boards
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CMMMech
    path: data/records/waste-printed-circuit-boards.yaml
    role: maintained_record
checks:
- check_id: named
  name: Independent named-record validation
  command: UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache uv run --locked
    cmmmech validate data/records/waste-printed-circuit-boards.yaml
  status: passed
  required: true
  summary: Reviewer executed; Checked 1 record(s); 0 failed. Terminal exit 0 observed
    (session 6018). Target remained unchanged through final inspect.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  exit_code: 0
  expected_exit_code: 0
- check_id: batch
  name: Native full checks
  command: just check
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the completed receipt and
    terminal logs. /private/tmp/cmm-round22-final-batch.log: uv run --locked --extra
    dev python scripts/check.py

    All checks passed!

    ........................................................................ [ 23%]

    ........................................................................ [ 46%]

    ........................................................................ [ 69%]

    ....................................................sss................. [ 92%]

    .......................                                                  [100%]

    308 passed, 3 skipped in 124.01s (0:02:04)

    Checked 154 record(s); 0 failed.

    Checked 173 history record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
- check_id: require
  name: Required corpus
  command: uv run --locked cmmmech validate --require-records
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the completed receipt and
    terminal logs. /private/tmp/cmm-round22-final-require.log: Checked 154 record(s);
    0 failed.

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
- check_id: history
  name: Trusted-base history
  command: uv run --locked cmmmech validate-history --base b19103bb393096e405bbecd2808a1aa0e01bb200
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parent executed; reviewer independently read the completed receipt and
    terminal logs. /private/tmp/cmm-round22-final-history.log: Checked 173 history
    record(s); 0 error(s).

    '
  target_ids:
  - cmmmech:waste-printed-circuit-boards
evidence:
- evidence_id: record
  kind: record_content
  reference: data/records/waste-printed-circuit-boards.yaml
  locator: Complete current record; new EDIT and unchanged CREATE sidecars
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: The heterogeneous secondary-resource identity, three distinct mechanisms,
    source entries, actual codex/GPT-6 EDIT at 13:15:57Z and separately recorded inline
    event at 13:16:41Z are coherent. No material/community CURIE or criticality designation
    is asserted.
  snapshot_sha256: 08994df8c73e773c677d9a0397c86c4a23b698380d870923b255fccffb7888dd
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1016/j.mineng.2023.108459
  locator: 'Accepted manuscript: full Methods 2.1–2.2, Results 3.1–3.5, relevant introduction/conclusions;
    Tables 2–6. Figures 2–8 visually inspected via rendered PDF pages 16,17,19,22,23,24;
    Tables 5–6 visually inspected on pages 20–21. Table 4 and Figure 1 caption read
    on page 12; Figure 1 graphic was not visually inspected.'
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: Actual ground end-of-life mobile-phone feed, chemically leached with biogenic
    ferric, supplied a separately tested living Riotinto community column. Table 6
    reports loading-dependent Fe(II) outlet behavior. Actual biooxidized liquor underwent
    solvent extraction; manuscript Methods and Results explicitly identify synthetic
    electrowinning solution.
  snapshot_sha256: dfad516802ab79b1058e2d6659479bf18e851838cd731e79a16a0821ad82bff6
- evidence_id: primary_limits
  kind: primary_source
  reference: https://doi.org/10.1016/j.mineng.2023.108459
  locator: Methods 2.1–2.2; Table 4; Results 3.2–3.5; Figures 4–8 and Tables 5–6
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: partial
  summary: No matched sterile biooxidation comparator or replicated whole process
    is described in inspected Methods/Results. At 95 h, inlet Fe(II) 9.29 g/L with
    Cu 10.45 g/L leaves 2.37 g/L Fe(II); later zero outlet follows reduced liquid
    flow. Table 4 AP SX/150 g/L acid conflicts with Methods/Results synthetic/155
    g/L acid. SEM-EDS is local composition, and 99.2% is current efficiency, not certified
    product purity or actual-board recovery yield. Fitted batch/depletion curves and
    proposed closed-loop performance are not independent observations.
  snapshot_sha256: dfad516802ab79b1058e2d6659479bf18e851838cd731e79a16a0821ad82bff6
- evidence_id: dataset
  kind: primary_source
  reference: https://doi.org/10.12795/11441/161670
  locator: Original Data.xlsx, freshly parsed ZIP/XML; composition B21,D23:D24,T8;
    Batch C2,B9,B11:B13; every nonempty CSTR, biooxidation and EW cell; selected SX
    G2:H3 cells
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: partial
  summary: Six sheets contain 1,435 nonempty cells (170 composition, 895 Batch, 20
    CSTR, 83 biooxidation, 213 SX, 54 EW). Independent parsing reproduces the documented
    retained-solid HCl wash and 62.03 to 53 g mass change; batch 1.2 L label; biooxidation
    g/h heading and mixed 2023/2024 dates; EW C16=1.02 and additional 50-degree series;
    differing Au mean and SX Fe increase. Only selected SX cells were scientifically
    inspected; all parsed formulas were not recalculated. These are same-experiment
    data and limitations, not independent replication.
  snapshot_sha256: e058132bb509f6197ef30e192be561af0d92a2ca93eda84e381620acd1a5c4d3
- evidence_id: dataset_readme
  kind: primary_source
  reference: https://doi.org/10.12795/11441/161670
  locator: Original repository README, complete text
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: partial
  summary: README supplies feed preparation, methods and six-sheet identities, but
    its 2–7 mm range conflicts with manuscript target 800–2000 micrometres, and stated
    10-01-2022 collection date conflicts with workbook biooxidation dates. No chronological
    or density conversion is invented.
  snapshot_sha256: 05f2fd04d68797894de73dde255127d9dea24a4cfef9ee6db4684b0e14bf65e9
- evidence_id: paper_identity
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.mineng.2023.108459
  locator: Retained Crossref response and primary title/author metadata
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: Crossref and source metadata support Iglesias-González, Dorado, Ramírez
    and Mazuelos, January 2024 Minerals Engineering 205:108459. The Seville cover
    year 2003 is not adopted. No update-to relation appears in the inspected response;
    that is not an exhaustive notice audit.
  snapshot_sha256: 5f5f7c6a1c814c5ba7d329c5dc48b7593528f20a4c4b93ca68240f32fa6dcfa8
- evidence_id: dataset_identity
  kind: database
  reference: https://doi.org/10.12795/11441/161670
  locator: Official repository dataset metadata and acquired README/workbook bundle
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: Dataset DOI and authors agree with the paired experiment; deposit/issue
    is 25 July 2024, distinct from declared data creation date. Metadata identifies
    CC BY 4.0 for the dataset; no rights are inferred for other publisher artifacts.
  snapshot_sha256: ab1be3ba406822f37e033622dc33f67edcd0214a83de04f73773ee7cb828104e
- evidence_id: carryforward
  kind: prior_review
  reference: reviews/structured/20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction/review.yaml
  locator: Corrected round21 independent review plus comparison to b19103bb393096e405bbecd2808a1aa0e01bb200
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: The first two full mechanisms, first two sources, existing inline curation-history
    and history-ref prefixes are semantically identical to the trusted base. Their
    independent scientific assessment is retained with its explicit Figure 1 inspection-provenance
    correction. Those 2021/2022 primary studies were not freshly reread by this reviewer.
  snapshot_sha256: 34cb3db9d4050912e3be7540c7b5e1c2219cff20a98ec8ee2004c21adaba0406
- evidence_id: preservation
  kind: record_content
  reference: /private/tmp/cmm-round22-pcb-independent/checks.json
  locator: Successful .venv Python field comparison and bounded hidden/ignored-following
    dedup receipt
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: Verified the exact preserved old scientific/provenance prefixes against
    the trusted base; searched DOI/title patterns across data/records, research, reviews,
    history and cited round21/round22 PCB raw directories. Matching scientific owners
    were this target and its frontier/dossiers, without a duplicate new experiment
    in other maintained records in this bounded scope.
  snapshot_sha256: 51c5b190e54ab08b7c0596a05bdf23e4ca340d296af2e9d902cde42700e00dbb
  search_scope: rg --no-ignore --hidden --follow -n -i over named scientific trees
    and cited current/prior raw directories. Ignored and hidden files included; relevant
    symlinks followed. PDFs separately inspected. Unrelated directories excluded;
    no global absence claim.
- evidence_id: search
  kind: search
  reference: /private/tmp/cmm-round22-pcb-independent/search.json
  locator: Three exact DOI/title correction/synthetic/dataset queries, 11 October
    2026
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: context_only
  summary: 'Independent queries: DOI 10.1016/j.mineng.2023.108459 correction erratum
    retraction; exact article-title prefix with synthetic; DOI 10.12795/11441/161670.
    First returned sets identified no directly affecting notice; official UPC source
    results support synthetic electrowinning and source identity. Irrelevant results
    were not used.'
  snapshot_sha256: 3cb76a828cce6ba7ead877368387ff4b64af758c4b1534a65a2bee7dd177d94c
  search_scope: Web search, no date/domain filters, first returned result sets only,
    no pagination. Not an exhaustive correction registry or literature census.
- evidence_id: gates
  kind: validation
  reference: /private/tmp/cmm-round22-gate-receipts.json
  locator: Completed parent batch/require/history terminal receipt and logs; frozen
    target hash file
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: 'Root executed all three gates to exit 0: 308 tests passed, 3 skipped;
    154 records and 173 histories. Reviewer independently read each completed terminal
    log and verified the target equals the gated SHA-256. Named file validation was
    independently executed by this reviewer.'
  snapshot_sha256: ee1b6156ba8df516f968a764970052ed3ec86221a56f7a182b4d2a374766fbfb
- evidence_id: dossier_fix
  kind: record_content
  reference: research/ingests/round22-pcb-sources-20261011.md
  locator: Re-read final source Markdown after pre-save publication issue CultureBotAI/CMMMech#81
  accessed_at: '2026-10-11T13:24:52.755478Z'
  support: supports
  summary: Joined quantities identified during this review were corrected by root
    with spaces; final dossier is readable and preserves scientific content/URLs.
    Final context SHA-256 is da3ccffa12df5af65e8515d6532ba73c1608a7b1955a054974867cc7c6fbf6f2.
    The unchanged target was reinspected with this corrected context before save.
  snapshot_sha256: da3ccffa12df5af65e8515d6532ba73c1608a7b1955a054974867cc7c6fbf6f2
assessments:
- assessment_id: identity
  area: identity
  topic: Maintained heterogeneous secondary resource
  outcome: supported
  summary: The new study belongs under the existing waste-board resource. It does
    not define a new element, mineral, commodity or universal board composition, and
    its dataset/mirror are not separate experiments. No unsupported identifier or
    inherited criticality claim is introduced.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - primary
  - paper_identity
  - dataset_identity
  - preservation
  dimensions:
  - name: material_kind
    value: secondary_resource
    definition: End-of-life electronic board feed, with study-specific source and
      pretreatment retained.
    evidence_ids:
    - record
    - primary
  - name: criticality
    value: Not asserted
    definition: No designation is inferred from constituent copper or other metals;
      no jurisdiction/list/edition claim requires expansion.
    evidence_ids:
    - record
- assessment_id: biological_stage
  area: evidence
  topic: Conditional living-community ferric regeneration
  outcome: supported
  summary: The measured column inlet/outlet results support operational regeneration
    under the reported conditions. Loading-dependent residual Fe(II), altered flow
    and missing sterile/replicated controls prevent exclusive microbial effect sizes,
    member-specific attribution or universal inhibition-tolerance claims.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - primary
  - primary_limits
  - dataset
  dimensions:
  - name: organism_biomass
    value: Living immobilized Riotinto community, reported mainly A. ferrooxidans
      and L. ferrooxidans
    definition: Individual strains and member-specific roles unresolved; no community
      or strain CURIE asserted.
    evidence_ids:
    - record
    - primary
  - name: substrate_pretreatment
    value: Ground end-of-life mobile-phone material after casing/battery removal;
      subsequently produced and filtered leach liquor
    definition: Manuscript 800–2000 micrometre target conflicts with README 2–7 mm;
      board heterogeneity remains explicit.
    evidence_ids:
    - record
    - primary
    - dataset_readme
  - name: conditions
    value: Separate 31-degree C, 0.55 L column; nominal 100 mL/h liquid and 750 mL/min
      air; later 37 mL/h liquid
    definition: Chemical ferric leaching occurs separately at 60 degrees C; measured
      column feed chemistry and reduced-flow endpoint stay distinct.
    evidence_ids:
    - record
    - primary
  - name: controls
    value: No matched sterile column or replicated full train reported
    definition: Paper describes sequential stages and heterogeneous/spiked feed; these
      are not matched organism-necessity comparisons.
    evidence_ids:
    - record
    - primary_limits
  - name: outcome
    value: Fe(II) inlet/outlet assays at 24, 45, 67, 95, 168 h
    definition: Near-zero early outlets differ from 2.37 g/L at 95 h and later zero
      after flow reduction; zero report does not establish a quantified detection
      limit.
    evidence_ids:
    - record
    - primary
    - dataset
- assessment_id: accounting
  area: evidence
  topic: Measured chemistry, fitted trajectories and residue accounting
  outcome: supported
  summary: The paper-attributed approximate 99% extraction estimate is appropriately
    qualified rather than imported as an independently reproduced reactor-only balance.
    Acid washing, copper-spiked inlet, sampled fractions, heterogeneous feed and workbook
    normalization prevent direct whole-board recovery accounting.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - primary
  - primary_limits
  - dataset
  - dataset_readme
  dimensions:
  - name: feed_denominator
    value: Nine Cu assays mean 35.71 wt%, SD 4.16 percentage points
    definition: A heterogeneous starting-feed assay, not an invariant material composition
      or proof of every-run Cu input.
    evidence_ids:
    - record
    - primary
  - name: residue_fraction
    value: 135.01 g feed; 21.93 g filtered solid; 53 g retained washed solid
    definition: Workbook retained-solid mass decreases 62.03 to 53 g after 1.5% HCl
      wash; wash Cu loss is not resolved by final-solid assay alone.
    evidence_ids:
    - record
    - primary
    - dataset
  - name: model_measurement
    value: Fitted curves, batch normalization and model settings remain separate
    definition: No normalized batch conversion or synthetic EW model is transformed
      into a measured total-board yield.
    evidence_ids:
    - record
    - primary_limits
    - dataset
- assessment_id: recovery_scope
  area: evidence
  topic: Actual-liquor solvent extraction and synthetic electrowinning
  outcome: supported
  summary: Actual biooxidized liquor supports a solvent-extraction stage. Explicitly
    synthetic electrowinning and simulated stripping solutions prevent attributing
    the metal deposit to actual board-derived copper or claiming a tested closed loop.
    Current efficiency and local Cu-rich EDS do not prove bulk purity.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - primary
  - primary_limits
  - dataset
  dimensions:
  - name: solvent_extraction
    value: 15 vol% LIX 973 NS-LV in kerosene at 20 degrees C; reported 91.4% at equal
      phase volumes
    definition: Aqueous analyses support transfer; organic concentrations were calculated,
      and this percentage is not whole-board metal recovery.
    evidence_ids:
    - record
    - primary
  - name: electrowinning
    value: Synthetic 15 g/L Cu plus 155 g/L sulfuric acid in Methods/Results
    definition: Table 4 AP SX origin and 150 g/L acid conflict is retained;99.2% denotes
      current efficiency, not purity, and EW C16=1.02 remains unresolved.
    evidence_ids:
    - record
    - primary_limits
    - dataset
  - name: deployment
    value: Laboratory stage tests
    definition: No simultaneous continuously closed process, zero-reagent operation,
      certified bulk product or industrial deployment demonstrated.
    evidence_ids:
    - record
    - primary_limits
- assessment_id: prior_integration
  area: provenance
  topic: Transparent carryforward of unchanged older mechanisms
  outcome: supported
  summary: The current full record preserves both prior mechanisms and their evidential
    qualifications, with actual field-equality proof and a specifically identified
    corrected independent review. This review freshly evaluates only the added 2024
    evidence; no false claim of rereading 2021/2022 literature or repeated independence
    is made.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - carryforward
  - preservation
  dimensions: []
- assessment_id: provenance
  area: provenance
  topic: Actual EDIT, frozen inputs and completed native gates
  outcome: supported
  summary: Initial canonical inspection preceded judging the PCB evidence. After root
    corrected the source-dossier spacing, that changed context was read again and
    re-inspected with actual CREATE/EDIT sidecars. Final target bytes match both initial
    and gated target hashes. Native checks pass; their structural success is not used
    as scientific proof.
  target_ids:
  - cmmmech:waste-printed-circuit-boards
  evidence_ids:
  - record
  - gates
  - dossier_fix
  - paper_identity
  - dataset_identity
  dimensions: []
findings: []
actions: []
limitations:
- Fresh primary-literature work covers the added 2024 study and paired dataset. Earlier
  2021/2022 scientific assessments are carried forward only for field-identical content
  from the named prior independent review.
- No matched sterile biooxidation column, replicated full process, species-resolved
  causal assay or independent laboratory reproduction is available in the reviewed
  evidence.
- The original XLSX was parsed afresh and focused cells inspected, but every formula
  was not recalculated and raw instrument traces were not independently audited.
- Particle-size, batch-volume, dataset-date/flow-unit, acid concentration/origin,
  Au assay and current-efficiency discrepancies remain unresolved and explicitly limit
  interpretation.
- Feed heterogeneity, commercial inlet copper and acid-washed/sampled solids prevent
  treating paper-reported extraction as an independently closed reactor-only Cu balance.
- Synthetic electrowinning, local SEM-EDS and current efficiency do not demonstrate
  certified bulk purity, actual-board metal recovery, an operating closed loop or
  industrial deployment.
- Live searches covered first returned result sets without pagination; no exhaustive
  literature or notice-registry absence is asserted. Figure 1 graphic was not visually
  inspected, although its caption/conceptual description was read.
notes:
- Evidence access times denote completion of this review interval, which began at
  the recorded actual UTC start; they do not imply new downloads of curator-acquired
  sources. Primary reading, direct figure inspection, fresh workbook parsing and searches
  occurred within that interval.
- Temporary gate helper adaptations were authored by this reviewer but root executed
  the batch commands. Receipt/log inspection and target-hash comparison were independent;
  checks are not represented as reviewer executions except named validation.
- Minor dossier readability finding was raised before the first canonical save, tracked
  by root as CultureBotAI/CMMMech#81 (https://github.com/CultureBotAI/CMMMech/issues/81),
  corrected and independently verified. No previous structured finding existed, so
  no fabricated resolved finding or previous_occurrences lineage is added. Issue closure
  remains the parent publication workflow responsibility.
- The original round21 review had an inspection-provenance correction retained in
  its successor. This review cites that corrected assessment transparently and does
  not alter, silently replace or claim to resolve an earlier structured finding.
- An initial independent prefix-check invocation with system Python lacked PyYAML;
  rerunning with the project .venv Python succeeded. This transient environment mismatch
  did not affect any scientific file or the successful checks recorded here.
- No PCB record, history or source dossier was edited by this reviewer. Raw PDFs,
  original workbook, images and extracted text remain outside Git.
tags:
- round22
- independent
- scientific-review
- secondary-resource
- dataset-reconciliation
related_reviews:
- repository: CultureBotAI/CMMMech
  review_id: 20261011T125008Z-waste-printed-circuit-boards-round21-review-scope-correction
  relationship: Carries forward the corrected independent scientific assessment of
    the field-identical earlier 2021/2022 mechanisms; freshly assesses the new 2024
    addition and full-record integration. No earlier finding disposition is changed.
```
