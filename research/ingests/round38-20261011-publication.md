# Round 38 scientific review and publication report

This batch adds three distinct mineral records: hausmannite, katsarosite and mimetite. The corpus grows from 203 to 206 records. The evidence concerns laboratory dissolution, transformation and precipitation under specified culture conditions. No criticality is inherited from constituent elements; mineral formation and solution changes do not establish isolated-metal recovery or industrial deployment.

Worktree: `/private/tmp/CMMMech-expansion-round38-20261011`; branch: `curate/cmm-expansion-round38-20261011`; trusted base: `f3d674806df8f5fd7925e46f1dcfec70cace706a`.

## Independent scientific reviews

| Record | Reviewer | Verdict | Review artifacts |
|---|---|---|---|
| [hausmannite](../../data/records/hausmannite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T234546Z-hausmannite-round38-independent/review.md) / [YAML](../../reviews/structured/20261011T234546Z-hausmannite-round38-independent/review.yaml) |
| [katsarosite](../../data/records/katsarosite.yaml) | Codex /root/round27_eaf_slag | pass_with_limitations | [Markdown](../../reviews/structured/20261011T234621Z-katsarosite-round38-independent/review.md) / [YAML](../../reviews/structured/20261011T234621Z-katsarosite-round38-independent/review.yaml) |
| [mimetite](../../data/records/mimetite.yaml) | Codex /root/round27_packaging | pass_with_limitations | [Markdown](../../reviews/structured/20261011T234546Z-mimetite-round38-independent/review.md) / [YAML](../../reviews/structured/20261011T234546Z-mimetite-round38-independent/review.yaml) |

The [manifest](round38-frontier-20261011.json) pins exact record, history, source-dossier and review hashes. Each final review matches its record bytes. The source dossiers record identity checks, primary-source inspection, contradictions, acquisition failures and bounded hidden/ignored-inclusive deduplication. Raw articles and figures remain outside Git.

## Findings and corrections

Scientific records retain source-specific phase, identity, control and causal limits. Publication review corrected ambient-environment mutation risk, stale helper reviewer attribution and a README culture-authentication overstatement. Original preserved bytes were restored exactly.

[Issue #124](https://github.com/CultureBotAI/CMMMech/issues/124): a standalone PDF renderer accidentally rebuilt the original checkout’s editable environment. Six generated files changed. Every replacement was verified against the pre-incident SHA-256 snapshot before restoration; the full 7,187-entry hidden/ignored inventory and eight bounded unrelated skill-worktree files then matched, as did the preserved Git state. The [incident receipt](../../reviews/publication/20261011-round38/environment-preservation.json) records the event and recovery. The add-record skill now requires explicit isolated working directories and separates standalone source-tool environments. The original baseline was not replaced.

[Issue #125](https://github.com/CultureBotAI/CMMMech/issues/125): independent review found prior-batch authorship text in a temporary hosted-audit helper before execution. Reviewer and authorship are now required explicit arguments; stale batch labels were corrected. Publication review checks the actual agent role and eventual hosted receipt.

[Issue #126](https://github.com/CultureBotAI/CMMMech/issues/126): the README called the A. niger culture verified, overstating what the record supports. The summary now says source-identified culture; the record already distinguished sequence/label verification from independent experimental-culture authentication.

No schema, validator, test or governed artifact changed. The skill correction is instructional; existing skill-frontmatter tests run as part of the full gate.

## Validation

Fresh baseline `just check` passed before record edits: 308 tests passed, 3 skipped; 203 records and 234 histories validated. Final commands were separately executed on the frozen cohort:

- `just check`: exit 0. 308 passed, 3 skipped in 108.02s (0:01:48); Checked 206 record(s); 0 failed.; Checked 237 history record(s); 0 error(s). Log SHA-256 `cd7dc72bc2a2f472d84f5e9c0ba200749f40d668cd6e39b05d8649de00308dd5`.
- `uv run --locked cmmmech validate --require-records`: exit 0. Checked 206 record(s); 0 failed. Log SHA-256 `0a70d3ea31b01abc1a047c1a68029b2e03f4a1284bce6f451cc2cf4da10a3181`.
- `uv run --locked cmmmech validate-history --base f3d674806df8f5fd7925e46f1dcfec70cace706a`: exit 0. Checked 237 history record(s); 0 error(s). Log SHA-256 `4b62b8e5cb9dd0edb1deb96a0dcfd97e383ff2e308d024a39015dd7580f14a83`.
- `just review-check --base f3d674806df8f5fd7925e46f1dcfec70cace706a --require-reviews`: exit 0.  Log SHA-256 `9fb9824f7d69da1c111ea82e87422874c816a351db3f2b927cbc6b32e42b6b7d`.

Exact-hash coverage separately verified 206/206 current scientific records, 237 canonical histories, 241 structured reviews and 39 available review bases. Structural checks are distinct from scientific verification.

## Publication and remaining work

Live read-only checks confirmed merged CLAW admission PR 581, four active workflows and the effective native SQUASH/ALLGREEN queue without ruleset bypass actors. Canonical history and pinned governance artifacts are installed; the manual/comment-only shepherd configuration does not prove credential readiness. Future changes use CLAW’s supported admission/synchronization process.

New reviews use the trusted main revision. The existing annotated `review-base/cmm-source-survey-20261009` tag preserves its earlier otherwise-lost base. An isolated squash-shaped checkout must pass before publication; after actual queue merge and owned-branch deletion, fresh remote main must pass all checks again. Those results belong in the PR closeout receipt.

Vanadinite remains source-only because original figures were not inspectable through the legitimate routes checked. It receives no record or CREATE history. Existing acquisition issues #103, #104 and #120 remain open. [Remaining priorities](round38-frontier-20261011.md) preserve these and other unreviewed evidence tasks; no exhausted-frontier claim is made.
