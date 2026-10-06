# First three records: curation and review handoff

Session: 2026-10-05 America/Los_Angeles; sources and review timestamps use
2026-10-06 UTC. At the initial handoff, the implementation was uncommitted on
`curate/first-three-records-20261005` in
`/private/tmp/CMMMech-first-three-20261005`, based on
`c791655d607d8df73a61f2c66ff3f28103aaadd7`.
The original CMMMech checkout remained clean on `main` at that revision.
No issues, PRs, comments, settings or other shared content were written during
this local implementation. Review artifacts record their exact pre-commit
working states; later commits do not retroactively change those snapshots.

## Selection and scientific boundaries

The pilots use primary experiments with accessible methods, organism or
community provenance, experimental conditions and observed outcomes. Three
different processes exercise the contract without treating an element,
mineral species, commodity and secondary resource as interchangeable.

| Record | Why selected | Criticality scope |
|---|---|---|
| [Cobalt](../data/records/cobalt.yaml) | [Lalropuia et al. 2024](https://doi.org/10.3389/fmicb.2024.1347072): mixed-community bioleaching of actual battery black mass tests secondary-feed and community attribution. | EU Regulation 2024/1252, original Annex II Section 1(h) |
| [Neodymium](../data/records/neodymium.yaml) | [Kucuker et al. 2017](https://doi.org/10.1371/journal.pone.0175255): inactive algal biomass and magnet-derived leachate test biosorption, pretreatment and measured-versus-fitted distinctions. | USGS 2022 final list; deliberately historical |
| [Palladium](../data/records/palladium.yaml) | [Lloyd et al. 1998](https://doi.org/10.1128/AEM.64.11.4607-4609.1998): resting-cell reduction with negative controls and solid-phase characterization tests redox evidence. | USGS 2025 final list |

All three record roots are **elements**. The experiment-specific forms are
defined within mechanism context. Criticality entries are particular editions,
not a synchronized current-policy catalogue. All curated performance claims
are laboratory observations. None establishes industrial deployment.

Reviews preserved the cobalt paper's adaptation-dose inconsistency, clarified
that its original enrichment profile does not characterize the adapted
community, and made its pretreatment explicit. Neodymium's uptake is calculated
from solution depletion; its fitted capacity, high-temperature precipitation
discussion and chemically simplified feed remain distinct. Palladium's current
ChEBI label was corrected, and a second primary paper supplies a caveat about
copper-inhibition specificity without transferring genetic evidence between
species. Full source and acquisition limits are in the per-record reviews.

## Schema assessment and implementation

No schema or validator-library expansion was justified by these pilots.
`material_kind` distinguishes root identity; `context` can retain substrate,
strain/community resolution, biomass state, conditions and scale; `evidence`
can distinguish direct support, partial inference and contextual caution.
The optional organism list correctly accommodates an unresolved consortium.
The schema remains intentionally unable to verify scientific truth offline.

The real behavioral need is preventing accidental loss of the newly populated
corpus. `scripts/check.py` now passes `--require-records` to validation, so
`just check` and the existing CI fail if the corpus becomes empty. The new
`tests/test_check.py` executes the actual gate in an isolated empty repository
layout: lint and a small nested suite pass, then real validation must fail.
Direct exploratory CLI validation without the flag retains its prior behavior.

The reusable [record-review skill](../.claude/skills/review-record/SKILL.md)
requires separate timestamped artifacts, source/identifier checks, review of
contradictions, severity-ranked findings and final byte hashes. `CLAUDE.md` and
the [record guide](records.md) route new and changed records through it.
Scientific-review coverage is a workflow requirement, not a machine-enforced
claim made by `just check`. These artifacts do not implement CLAW history.
An independent agent reviewed the skill and gate/test change with no material
findings; a further independent check accepted the corrected palladium file.

## Review artifacts

Every record was reviewed by an agent other than its original curator.
The following final hashes were checked against the files after all corrections.

| Record | Timestamped artifact | Verdict |
|---|---|---|
| Cobalt | [20261006T021831Z](../reviews/records/cobalt/20261006T021831Z.md) | Accept with limitations |
| Neodymium | [20261006T021711Z](../reviews/records/neodymium/20261006T021711Z.md) | Accept with limitations |
| Palladium | [20261006T021817Z](../reviews/records/palladium/20261006T021817Z.md) | Accept with limitations |

No unresolved critical or major record error remains. Source limitations,
unresolved scientific questions and acquisition gaps are explicitly retained.

### Continuation: source access and commit preparation

The continuation preserved all three YAML byte hashes. The new
[cobalt follow-up](../reviews/records/cobalt/20261006T022704Z.md) inspected the
actual primary Figures 4-6, confirming the qualitative comparison and control
limitations. The [neodymium follow-up](../reviews/records/neodymium/20261006T022704Z.md)
retrieved S1 and confirmed the scoped experimental uptake against its workbook
entry. It also recorded exceptions to the article's broad kinetic-fit statement;
the record makes no universal kinetic-fit claim. Earlier reviews are retained.
Complete EU Annex II access and the cobalt ASV supplement remain acquisition
gaps; the original indexed official cobalt entry remains the criticality evidence.

An [independent package review](../reviews/process/20261006T022521Z.md) accepted
the local changes for commit after correcting a stale current-status sentence.
The coordinating agent then checked the two new review artifacts and their
unchanged record hashes. The repeated full gate passed **50 tests** (10.95 s)
and **3 records, 0 failures**; separate strict validation passed again. Remote
main remained at the bootstrap revision and the refreshed open issue queue
was empty. The prepared publication proposal is a draft PR from this branch
to `CultureBotAI/CMMMech:main`; publication requires the repository's exact-action
approval and is not claimed by this handoff.

## Validation

- Baseline on original main: `just check` passed lint and **49 tests** and
  reported **0 records**. Separate strict validation returned exit 1 for the
  empty corpus, as intended.
- Final worktree: `just check` passed lint and **50 tests** (11.63 s), then
  reported **3 records, 0 failures**.
- Separate `uv run --locked cmmmech validate --require-records`: **3 records,
  0 failures**, exit 0.
- Skill-creator `quick_validate.py`: **Skill is valid**.
- `git diff --check`: passed. All three final record SHA-256 values occur in
  their corresponding review artifacts.

The final commands used `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache` because
the default user uv cache is sandbox-protected. Dependencies were installed
from the locked project environment. No check depends on source/network access
after installation. Live Linux CI was not run or claimed; this is local macOS
verification. Documentation edits after these checks do not change the
reviewed YAML hashes or executable behavior.

## Integration and next priorities

The [integration audit](integration-status.md) records the remote APIs,
immutable CLAW authority revision, hidden/ignored-inclusive searches and
supported admission sequence. It found **zero open GitHub issues**, pending
fleet registration/shared history/vendored governance/PR shepherd, and no
native merge-queue configuration. External App/credential readiness is unknown.

1. Resolve the documented scientific limits before adding stronger recovery,
   molecular-causality or deployment claims. Obtain inaccessible supplements
   where future claims depend on them, and inspect source corrections over time.
2. Expand with a mineral-species record and a separately identified secondary
   resource supported by primary evidence; retain material/host/product scope.
   The pilots demonstrate mechanism variety, not coverage of every material kind.
3. Add structured measurements or scale fields only when real curation and
   querying needs justify them; keep measured, fitted and inferred values distinct.
4. Use CLAW's supported `onboard-mech` process in a separate authorized
   integration change, implement the canonical history adapter, and coordinate
   immutable governance release and consumer re-pinning. Follow with verified
   PR shepherd configuration and native queue plan/apply/check plus an actual
   reviewed merge-group execution. Do not hand-copy governed files or invent a pin.

## Publication and adversarial PR review

The user subsequently authorized committing, pushing, opening a PR, adversarial
review, issue filing and resolution, merging, and branch deletion. Commit
`2961df4540675b2d07aa7aa658776d779233d6c3` was pushed and
[PR #1](https://github.com/CultureBotAI/CMMMech/pull/1) opened. The earlier
handoff and integration audit remain historical snapshots of their stated times.

A fresh independent [code/process review](../reviews/process/20261006T042058Z.md)
accepted that commit with no actionable defects. It rechecked the actual empty
corpus regression, strict record validation, review hashes and local links.

Fresh independent scientific reviews accepted the unchanged
[cobalt](../reviews/records/cobalt/20261006T042218Z.md),
[neodymium](../reviews/records/neodymium/20261006T042218Z.md), and
[palladium](../reviews/records/palladium/20261006T042218Z.md) records with their
stated limitations and no blocking findings. The complete original EU
regulation PDF became accessible; Annex II Section 1(h), printed page 57,
independently confirms cobalt and closes that earlier acquisition gap.
The cobalt ASV workbook remains unchecked after bounded retrieval attempts;
post-adaptation community composition remains uncertain.

[Issue #2](https://github.com/CultureBotAI/CMMMech/issues/2) tracks the baseline
empty-corpus defect already fixed by this PR and is linked for closure on merge.
[Issue #3](https://github.com/CultureBotAI/CMMMech/issues/3) tracks the separate
CLAW-supported integration sequence; that future rollout is not claimed by this
corpus change.

The coordinating agent repeated `just check`: lint passed, **50 tests passed**
(7.15 s), and **3 records, 0 failures**. Separate strict validation again passed.
GitHub's Linux validation is tracked on the PR; merge must follow a successful
check on the final pushed revision. Live PR status, merge evidence and final
branch cleanup are recorded on GitHub rather than predicted by this document.
