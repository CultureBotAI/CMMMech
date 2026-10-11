# Round27 publication-readiness audit

- UTC: 2026-10-11T16:23:49.586732+00:00.
- Reviewer: Codex `/root/round27_eaf_slag` (GPT-6).
- Worktree: `/private/tmp/CMMMech-expansion-round27-20261011`; branch `curate/cmm-expansion-round27-20261011`; reviewed base `3f1350b24b4f6248ed2e17caade936c15af9be93` with the current working changes listed below.
- Scope: publication documentation, source-dossier provenance, changed-record/history coverage and review-status claims. This is a documentation/provenance audit, **not a fresh scientific review of the records**.
- Independence: this reviewer authored the BOF slag extension and its EAF/slag source dossiers. No self-approval of that record is made. Its independent scientific assessment belongs to `/root/round27_packaging`; BOF dust and Cu/Ag scientific reviews belong to their separately assigned reviewers. The reviewer did not author or edit the README/frontier wording assessed here; `/root` applied both documentation fixes.
- Artifact timing: this first saved audit was written **after** both fixes were inspected. Initial wording below was captured in the earlier read-only audit; no pre-fix file hash was captured, and none is invented. Both local dispositions therefore appear in this single initial artifact rather than rewriting an earlier saved verdict.

## Reviewed working changes and evidence

The changed scientific scope is exactly two new records—BOF steelmaking dust and electroformed Cu/Ag manufacturing scrap—and one extension to BOF steel slag. At inspection there are 171 corpus records and 195 canonical sidecars. All 5 history references from these three records resolve. Existing committed history/review files are not modified in the working diff; no schema, validator, test or governed configuration edits appear. This is a bounded Git diff check, not a claim about every filesystem location.

The five round27 investigation JSON files parse; 93 manifest path/hash entries were rechecked against their local raw files, including stored sizes where supplied, with no mismatch. These are references to local evidence retained outside Git, not a promise that ephemeral raw paths will remain accessible to future clones. Paired dossier Markdown local links were separately checked and resolved during the audit. Source access limitations, nonacceptance of deferred candidates, no inherited criticality, and non-exhaustion are stated explicitly.

Inputs read directly for the two findings and their correction:

| Input | SHA-256 after correction |
|---|---|
| `README.md` | `0efdcdc560c67b229a4599dff0fc9e376c027743bca07f5da65fe1432e496605` |
| `research/ingests/round27-frontier-20261011.md` | `7f170720ffc6cefc61e8b8770394611be599a4f3fe263021f8f00524f84cbf7d` |
| `research/ingests/round27-goethite-sources-20261011.md` | `fcc3221fd08bc3c668cc098d99ed8994510f44e93398f1853fa698968587a73c` |
| `data/records/electroformed-copper-silver-manufacturing-scrap.yaml` | `cd4c7e284b4ad47079d0c609db007795f1aeeb28dcdf7cf359d2a32b52b1ea62` |
| `reviews/structured/20261011T161956Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-initial/review.yaml` | `e27807adfe3246cbb13fde9d7f554dced27b698c696d590c3c7fa9155197d05b` |

## Findings by severity and corrections

### P1 — Minor, resolved: ambiguous attribution of the Cu/Ag plot error

- Stable issue key: `CMMMech.round27.frontier-review-finding-attribution`.
- Owner: `research/ingests/round27-frontier-20261011.md`, Cu/Ag item under “Scientific questions retained”.
- Initial exact wording: “The initial review's incorrect plot-direction finding is corrected while preserving the source's 59% versus 50.0% conflict.”
- Evidence: the initial independent review `20261011T161956Z-electroformed-copper-silver-manufacturing-scrap-round27-independent-initial`, finding `F1`, correctly identifies an error in the record's interpretation of Figure 5. The draft frontier could instead be read as calling that finding incorrect.
- Expected correction: attribute the error to the record and retain the original abstract/Results discrepancy; do not undermine the review's finding or imply a new scientific result.
- Inspected final wording: “The record’s plot-direction error identified by the initial review is corrected while preserving the source's 59% versus 50.0% conflict.”
- Disposition: resolved in the inspected frontier bytes. The corrected Cu/Ag record hash is `cd4c7e284b4ad47079d0c609db007795f1aeeb28dcdf7cf359d2a32b52b1ea62`. This documentation disposition does not substitute for the scientific reviewer's final successor or final required gates.

### P2 — Minor, resolved: insufficiently precise goethite supplement inspection scope

- Stable issue key: `CMMMech.round27.frontier-supplement-inspection-scope`.
- Owner: `research/ingests/round27-frontier-20261011.md`, first ingest priority.
- Initial exact wording: “Round27 acquired and inspected the official supplement, adding useful tables and figures.”
- Evidence: the goethite source dossier explicitly limits inspection to supplement text/tables, captions and the two original XRD panels; remaining embedded chart figures were not fully rendered or scientifically adjudicated.
- Expected correction: name the inspected portions and preserve the uninspected-chart limitation so the frontier cannot be mistaken for full supplementary-figure review.
- Inspected final wording: “Round27 acquired the official supplement and inspected its tables, captions and original XRD panels; the remaining charts retain the dossier’s inspection limitations.”
- Disposition: resolved in the inspected frontier bytes. The candidate remains deferred until complete primary methods and process provenance are obtained.

## Unresolved questions and checks outside this snapshot

The batch checks and final independent scientific review artifacts were still being finalized when this audit was written. The frontier manifest and publication receipt linked by README/frontier were not yet present; those expected files and their final hashes, review coverage, gates, GitHub issue lineage and publication claims require a final bounded check. This audit does not authorize publication and does not claim PR creation, external issue posting, CI success, merge or branch deletion.

The root agent reported an automatic approval rejection for an earlier external issue attempt. This reviewer did not perform that attempt. Local findings and fixes are complete; any later shared mutation must follow the applicable authorization and recorded outcome rather than assuming this artifact created a GitHub issue.

## Verdict

**Two minor documentation findings resolved; final publication readiness remains pending final package checks.** No additional actionable inconsistency was found in the examined README summaries, dossier provenance and changed-record/history boundary. This bounded conclusion excludes fresh scientific self-review of the authored BOF slag material, final not-yet-saved review bundles, CI and remote state.
