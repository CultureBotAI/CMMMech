# Round27 final local publication-readiness audit

- UTC: 2026-10-11T16:29:52.280247+00:00.
- Reviewer: Codex `/root/round27_eaf_slag` (GPT-6).
- Worktree: `/private/tmp/CMMMech-expansion-round27-20261011`; branch `curate/cmm-expansion-round27-20261011`; trusted base `3f1350b24b4f6248ed2e17caade936c15af9be93`, with the final working changes inspected.
- Predecessor: [20261011T162349Z-readiness-audit.md](20261011T162349Z-readiness-audit.md), retained unchanged. This successor closes its pending **local package** checks; it does not claim remote publication.
- Scope and independence: documentation/provenance/coverage audit, not fresh primary-literature assessment. This reviewer authored the BOF slag extension and its source dossiers and does not scientifically self-approve them. Independent scientific review of that record is supplied by `/root/round27_packaging`; the other two records have separate assigned scientific reviewers. README/frontier fixes and final manifest/publication report were authored by `/root`.

## Inputs and reviewed revision

| Final maintained input | SHA-256 |
|---|---|
| `README.md` | `0efdcdc560c67b229a4599dff0fc9e376c027743bca07f5da65fe1432e496605` |
| `research/ingests/round27-frontier-20261011.md` | `7f170720ffc6cefc61e8b8770394611be599a4f3fe263021f8f00524f84cbf7d` |
| `research/ingests/round27-frontier-20261011.json` | `042b75fea1663dcc2ce1c8c7c7e790c6ce487bcb671bd7adc45a2edfdc65f9ed` |
| `research/ingests/round27-20261011-publication.md` | `d1df0b4ccfe233695885770807c40b7f36b2eefd70cfcf782cb18172ceb1e791` |
| `reviews/publication/20261011-round27/20261011T162349Z-readiness-audit.md` | `e2ced3b85b44253f26df2d63d328f9e79b249fd164e30c0110690a4af54ce5b6` |

| Changed record | Exact final SHA-256 | Completed independent review |
|---|---|---|
| `cmmmech:basic-oxygen-furnace-steelmaking-dust` | `79c2f6499166f317766618a25684e1f639499e919fbcfc291c1c0f27b92b702f` | `20261011T162622Z-basic-oxygen-furnace-steelmaking-dust-round27-independent` |
| `cmmmech:basic-oxygen-furnace-steel-slag` | `88e0d8b3c9ce06a1d70cf1ab5a34059259c28eac1904cf9589a9dd9364575ea4` | `20261011T162604Z-basic-oxygen-furnace-steel-slag-round27-independent` |
| `cmmmech:electroformed-copper-silver-manufacturing-scrap` | `cd4c7e284b4ad47079d0c609db007795f1aeeb28dcdf7cf359d2a32b52b1ea62` | `20261011T162619Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-resolution` |

Every input recorded by these three final scientific reviews matches current file bytes. Each is completed, `scientific_review: true`, and `pass_with_limitations`, with successful required checks. The older Cu/Ag initial finding retains its historical pre-correction record hash; its successor explicitly resolves the exact `F1` occurrence through `previous_occurrences`. That expected historical hash difference is not silently rewritten or represented as current coverage.

## Evidence and checks

- The frozen frontier JSON parses. All three record hashes, record IDs, history references, final review identities/hashes/Markdown paths and exact target-input relationships match maintained files. No speculative deferred feed is listed as an accepted record.
- Independent hidden/ignored-inclusive filesystem enumeration and matching of target ID, target path, actually reviewed scope, target-role SHA-256, completed positive scientific verdict and an evidence-linked supported assessment confirms **171/171 current records** have qualifying reviews. This is a provenance/coverage result, not a fresh scientific assessment of 171 records. There are **195 histories and 199 structured review bundles**.
- The README has **171 distinct valid record rows**. All **245 local links** extracted from README, the round27 frontier and publication report resolve. The two new roots and one existing-root extension agree across record files, README, frontier, manifest and publication report.
- Recomputed Git blob hashes for all **1,159 previously tracked scientific/research paths** show only the intended BOF slag record changed; **1,158 are byte-identical** and none is missing. No previous committed sidecar or review bundle was rewritten. No schema, validator, tests, skill or governed configuration change is included.
- The root-executed terminal receipts and their log SHA-256 values were independently checked. `just check` returned zero with **308 passed, 3 skipped in 140.18 seconds**, **171 records** and **195 histories** valid. Separate `cmmmech validate --require-records` and trusted-base history validation returned zero. The three final record hashes still match those captured before the gates. No redundant full test run is claimed by this reviewer.
- The subsequent trusted-base `just review-check --require-reviews` receipt records exit zero for all **199** bundles; its log checksum matches the manifest. This covers the final newly saved scientific bundles, which postdate the earlier batch test.
- The coverage-receipt checksum matches the manifest. Independent local Git checks establish **28 available review bases**: **27 are ancestors of the trusted merged main base**; the remaining `c0adc2c0763e1515ed07dc712b024974d98fb342` is pointed to by the existing `review-base/cmm-source-survey-20261009` tag. No new review requires preservation of an ephemeral topic-only commit. Remote peeled-tag verification, isolated squash-shaped verification and later main-only checks remain the publishing agent's responsibilities.
- The earlier dossier audit rechecked **93 raw manifest path/hash entries** with no mismatch. This final pass did not reacquire primary literature or broaden those inspection claims. All candidate-access limitations, source conflicts and absence of an exhaustion claim remain explicit.

Independent verification receipt: `/private/tmp/cmm-round27-independent-publication-audit-20261011T162952Z.json`, SHA-256 `2e576ddcdf32b9ead528cca8c96bb2d341d0397985f2a850153eb66ee57af962`. The receipt includes the local coverage enumeration and Git-base retention results. Parent terminal receipts are `/private/tmp/cmm-round27-final-terminal.json`, `/private/tmp/cmm-round27-review-check-terminal.json` and `/private/tmp/cmm-round27-local-coverage.json`; their relevant checksums are preserved in the repository frontier manifest.

## Findings, corrections and disposition

| Finding | Severity | Current disposition | Evidence |
|---|---|---|---|
| `CMMMech.round27.frontier-review-finding-attribution` / P1 | Minor | Resolved; predecessor disposition retained | Final frontier assigns the plot error to the record and preserves source 59% versus 50.0% conflict |
| `CMMMech.round27.frontier-supplement-inspection-scope` / P2 | Minor | Resolved; predecessor disposition retained | Final frontier specifies inspected tables, captions and XRD panels, retaining remaining chart limitations |

**No new actionable finding and no unresolved blocker or major issue were identified in this bounded local publication audit.** Record-level scientific limitations remain in the independent reviews; a qualified scientific pass is not a claim that source contradictions were eliminated.

## Remaining boundaries and verdict

**Local package: pass with stated scope limitations.** The publication report correctly distinguishes checked local results from future PR, CI, queue, merge and branch-deletion outcomes. This audit does not verify or authorize those future mutations. It also does not freshly verify the publishing agent's live GitHub governance checks or the original-checkout preservation inventories; those are separately reported session evidence and must be rechecked at closeout as promised. An earlier automatic approval rejection for external issue creation remains disclosed, and no external issue creation is inferred from local resolved findings.

The final publishing agent must use actual receipts for PR and review-issue publication, issue disposition, isolated squash verification, queue outcome, remote branch deletion and fresh-main validation. No conclusion here depends on assuming those actions already occurred.
