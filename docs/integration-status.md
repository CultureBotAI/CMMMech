# CMMMech integration and issue audit

- Snapshot: 2026-10-06T02:14:32Z (2026-10-05 in America/Los_Angeles).
- Scope: read-only CMMMech issue/governance audit and identification of CLAW's supported future admission process. No GitHub writes, admission, synchronization, configuration changes, or publication were performed.
- Candidate: `CultureBotAI/CMMMech`, default branch `main`, committed remote and local main `c791655d607d8df73a61f2c66ff3f28103aaadd7`. Both origin fetch and push URLs are `https://github.com/CultureBotAI/CMMMech.git`. Original checkout was clean at final inspection.
- CLAW authority: remote main `20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838` (`Add MechCheck fleet feature audit skill (#566)`). Canonical content was read at that immutable revision.
- Local CLAW checkout: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw`, local HEAD `d26793fc1bacd00b44912681956baaf5e3cff2a7`; dirty, and eight commits behind its cached origin/main at inspection. Preserved unchanged. Its modified fleet/configuration/governance files were not treated as deployed authority.

## Evidence and completeness

Read CMMMech `CLAUDE.md`, `README.md`, its repository-local `.claude/skills/review-open-issues/SKILL.md`, `justfile`, and `.github/workflows/validate-strict.yaml`. Used the local issue-review skill's read-only full-queue process.

Local absence checks used `rg --no-ignore --hidden` in the original CMMMech checkout. A final full filename inventory included **7,277 paths, including ignored and hidden paths and the dependency environment**, and found no `mech_shared.yaml`, `history.yaml`, `.vendored_canon_ref`, `pr-shepherd`, or `merge-queue` paths. Targeted content searches included ignored/hidden files in `src`, `scripts`, `justfile`, and `.github`. Git object bytes are not an implementation search; the committed remote tree was checked separately through the recursive tree API, whose response reported `truncated: false`.

Read-only GitHub API evidence:

| API request | Observed response |
|---|---|
| `GET repos/CultureBotAI/CMMMech` | Identity and default branch above; `open_issues_count: 0`, `allow_auto_merge: false`. |
| Paginated `GET repos/CultureBotAI/CMMMech/issues?state=open&sort=created&direction=asc&per_page=100` | `[]` initially and on final refresh. The issue endpoint includes PRs; there were no entries of either type. Zero issue bodies/discussions required reading. |
| `GET repos/CultureBotAI/CMMMech/commits/main` | SHA above; unchanged at final refresh. |
| `GET repos/CultureBotAI/CMMMech/branches/main` | `protected: false`, protection `enabled: false`, no required check contexts. |
| `GET repos/CultureBotAI/CMMMech/branches/main/protection` | HTTP 404 with explicit `Branch not protected`, consistent with the branch response. This is not a generic failed-access inference. |
| `GET repos/CultureBotAI/CMMMech/rulesets?includes_parents=true&per_page=100` | `[]`. |
| `GET repos/CultureBotAI/CMMMech/rules/branches/main` | `[]`. |
| `GET repos/CultureBotAI/CMMMech/actions/workflows` | Exactly one active registered workflow: `Validate strictly`, `.github/workflows/validate-strict.yaml`. |
| `GET repos/CultureBotAI/CMMMech/git/trees/c791655d607d8df73a61f2c66ff3f28103aaadd7?recursive=1` | Complete committed bootstrap tree; `truncated: false`. |

There are no open issues to prioritize or close in this time-bounded snapshot. An empty issue queue is not completion of integration work. Suggested work below has **not** been published as issues.

## Current status

| Area | Verified status | Consequence |
|---|---|---|
| Fleet admission | **Pending.** No `cmmmech`/`CMMMech` entry in the complete canonical `src/kg_microbe_fleet/fleet.yaml` at the CLAW revision above. | The candidate is not a registered fleet member; no claim of fleet-wide coverage is warranted. |
| Shared schemas and curation history | **Pending.** No canonical `mech_shared.yaml` or `history.yaml`, history adapter/recipe, or canonical history import in CMMMech's inspected implementation. | Timestamped scientific review Markdown is useful review evidence, but does not implement CLAW's canonical curation-history contract. |
| Vendored governance | **Pending.** CMMMech is absent from canonical `vendored_artifacts.json` consumers; no local vendored pin or sync checker. | Do not invent a pin or copy another Mech's governed artifacts. Registration changes the canonical manifest and requires a coordinated release. |
| PR shepherd | **Pending as repository deployment.** No committed/local shepherd workflow; GitHub lists only strict validation. The current canonical manifest identifies `pr_shepherd_workflow` at `.github/workflows/pr-shepherd.yml` for all consumers. | Adoption should follow governed synchronization and configuration verification. App installation/credential readiness was **not inspected** and remains unknown. |
| Native merge queue | **Not configured at snapshot.** No repository or inherited rulesets, no effective main rules, no classic protection, `allow_auto_merge: false`; CLAW's queue policy has no CMMMech entry. | The existing unconditional PR trigger and `merge_group: {types: [checks_requested]}` are CI preparation, not evidence of an active queue. |
| Local CI | One active validation workflow invokes `scripts/check.py`, exercising the same gate used by `just check`. Job key/context candidate is `validate-strict`. | Future admission must verify the successful live Actions job context and combined merge-group commit before adding a queue policy mapping. |

## Concrete follow-up sequence

1. **Prepare a separate CLAW admission change using its supported `onboard-mech` skill**, from an isolated clean worktree. Reverify candidate identity/revision. Add `cmmmech`, `CultureBotAI/CMMMech`, a verified `CMMMECH_ROOT`, `src/cmmmech`, `src/cmmmech/schema/cmmmech.yaml`, and actual `data/records` globs. Declare every current capability catalogue key with measured implementation evidence; use disabled/not-applicable reasons and required path assertions when appropriate. Establish serialization compatibility by measured round trips before declaring verified options. Preserve this session's domain review skill and evidence records.
2. **Register the same identity in the governance consumer manifest and reconcile all admission contracts.** Update packaged configuration and `.env.example`, research `MechEnum`, queue policy mapping, contract tests, and maintained setup guidance. Measure applicable artifact gaps against the committed CMMMech main tree. If admitting before completion, record only exact outstanding paths in CLAW's supported `INCOMPLETE_CONSUMERS` ledger; its bidirectional checks must pass, and the entry must disappear when completed. An exception is not deployment.
3. **Adopt canonical shared/history schemas through the supported governed release, then implement CMMMech-owned adapters and history gates.** The canonical Tier 1 standard requires `schema/mech_shared.yaml`, `schema/history.yaml`, record `curation_history`, and `just new-history`. Design imports and validation against CMMMech's closed schema, append history without rewriting scientific meaning, and test adapter behavior and preservation of timestamps/provenance. Record review artifacts remain complementary.
4. **Complete a coordinated immutable governing release.** Publish the admitted CLAW revision only through an authorized release; derive the consumer set from the new manifest, inspect pin-coupling, use `kg-microbe-governance sync` dry-run and reviewed apply from the matching installed authority package in clean consumer worktrees, and re-pin **every** consumer. Run `check` for each and `fleet-audit` over clean committed default-branch tips at the same full CLAW revision. Do not hand-edit governed copies or use the legacy `transition` state to bypass equality. The inspected canonical manifest currently lists 11 consumers; re-derive at execution time rather than freezing this count.
5. **Finish PR shepherd and queue rollout with separate operational evidence.** Verify required App/configuration readiness without exposing credentials. Land any remaining CI readiness first. Use CLAW's `kg-microbe-merge-queue plan` scoped to CMMMech, retain a reviewed plan, and apply only when authorized with a new receipt. Verify settings using `check`, then prove one authorized reviewed PR actually merges through a native merge group, retaining reviewed head, merge-group SHA, Actions run and final merge commit. Do not equate a rules read-back or workflow presence with queue execution. Deterministic queue-admission and post-merge-integrity artifacts may also become applicable under the authority version chosen for the release; use its manifest rather than an older hand-maintained list.

Admission acceptance should include `openclaw-cli config validate`, manifest/profile and research/fleet contract tests, authoritative governance-layout checks, consumer-completeness checks, and fleet report visibility. Capability-specific target validation must use the verified root. This audit intentionally did not run the dirty local CLAW package to claim coverage against remote canonical state.

## Authoritative process references

- [CLAW supported admission skill](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/.claude/skills/onboard-mech/SKILL.md).
- [Canonical fleet registry](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/src/kg_microbe_fleet/fleet.yaml).
- [Canonical artifact/consumer manifest](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/src/kg_microbe_governance/vendored_artifacts.json).
- [Mech standard and history requirements](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/docs/guides/MECH_STANDARD.md).
- [Governed release and synchronization](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/docs/guides/VENDORED_GOVERNANCE.md).
- [Merge-queue plan/apply and operational proof](https://github.com/CultureBotAI/culturebotai-claw/blob/20aae24502ad6a76a1a2c6cdb1eb0d5c8ce42838/docs/guides/MERGE_QUEUES.md).

No failures were interpreted as empty results. Remote App installation, available secrets, or automation outside the registered repository workflows were not audited. Baseline and final CMMMech implementation checks belong to the parent session's verification record, not to this read-only integration audit.
