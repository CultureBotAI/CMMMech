# Independent review: CMMMech queue activation plan

- UTC snapshot: 2026-10-08T02:29:37Z.
- Reviewer: independent `queue_admission_audit` agent.
- Scope: read-only review before the authorized root agent applies settings.
- Plan: `/private/tmp/cmmmech-integration-evidence/queue-admission-plan.json`.
- Plan SHA-256: `c5f301d7bf2cd71bb110378bd1ad77f21575a5e7e73ae5fb0cdd07c398a25bd5`.
- Published authority: `849f336e025510316a5f235eb0af8547b8bd50cc`.
- Candidate deployed main: `842edc17fc603831c6ab56fd0ef1d813416d3ea5`.

## Evidence and checks

Independently read the immutable published CLAW queue policy: CMMMech maps only
`.github/workflows/validate-strict.yaml` to `validate-strict`. Re-read live CMMMech
main and workflow identity; they match the saved plan's main and workflow blob
`f0f9d794f1e4efe818ad4589b5e6354409251070`.

The successful workflow evidence is real:
[run 37717750857](https://github.com/CultureBotAI/CMMMech/actions/runs/37717750857)
is a completed successful main push at that exact SHA. Its single
[job 113118075562](https://github.com/CultureBotAI/CMMMech/actions/runs/37717750857/job/113118075562)
is named `validate-strict` and succeeded. The measured workflow runs for every
PR and requested merge group, checks out the combined event commit, runs the
local gate, then verifies canonical governed artifacts. No path filter or
conditional required job can skip that validation.

Live repository metadata confirms public organization ownership, main default,
administration permission, squash enabled and auto-merge disabled. Successful
repository/inherited ruleset and effective main-rule reads return empty lists;
the classic-protection API explicitly reports `Branch not protected` (HTTP 404).
The plan has no readiness errors and status `planned`.

## Desired changes reviewed

- One active named ruleset, `CLAW merge queue`, applying only to `refs/heads/main`.
- No bypass actors. Pull requests required; no new approval-count requirement.
- Required Actions context `validate-strict`, integration ID 15368; check
  enforcement on creation, with strict/up-to-date PR policy disabled because the
  queue validates the combined candidate.
- Native queue: SQUASH, ALLGREEN, up to three concurrent builds, one entry per
  merge, 120-minute check timeout, minimum one entry and five-minute minimum wait.
- Supported apply also enables `allow_auto_merge`. No unrelated rules or
  repository settings are scheduled for removal or replacement.

These values match CLAW's documented managed policy. The separate automatic
admission controller's approval and current-main integrity requirements are not
misrepresented as new native ruleset approval requirements.

## Findings, limits and verdict

No blocking or minor finding was confirmed. **Accept this exact plan for the
authorized supported apply**, subject to its built-in fingerprint/readiness
recheck immediately before writes. Changed settings or workflow bytes require a
fresh plan and review. Do not use `--admin` or remove unrelated protections.

No settings were changed by this reviewer. Successful application/read-back will
not prove native queue execution: retain a reviewed PR head, actual merge-group
SHA and successful Actions run, merged commit, post-merge validation/integrity,
and a fresh scoped configuration check. The next history PR changes workflow
bytes; it still needs successful PR and merge-group validation of those bytes.
