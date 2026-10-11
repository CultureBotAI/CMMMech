# Round 17 independent publication audit

- UTC audit timestamp: 2026-10-11T10:59:06.751755Z.
- Reviewer: Codex `/root/round17_publication_adversary`, GPT-6 / codex.
- Independence: this agent authored none of the four records, their histories,
  scientific reviews or source dossiers. This is agent separation within the
  shared workflow, not external organizational independence.
- Worktree: `/private/tmp/CMMMech-expansion-round17-20261011`.
- Branch: `curate/cmm-expansion-round17-20261011`.
- Reviewed base and current HEAD: `4504ab1c5a005ea31e65318c3b3f206d6fbf44ed`.
- Reviewed state: uncommitted working changes. The 29 input paths consist of
  README, four records, four CREATE sidecars, eight scientific review files,
  six source-dossier files, three timestamped source artifacts, a frontier pair
  and the publication report. This audit is the thirtieth publication path.
- Exact input receipt: `/private/tmp/cmm-round17-independent-package-snapshot.json`,
  SHA256 `2cfdf3024ba202f5a26c346e14ff2ac106d2ad9b0f4fac1a9ff21f8532311d56`. The later freeze receipt includes this audit.

## Scope and evidence checked

Read CLAUDE.md, the add-record and record-review skills, record contract, shared
review contract and local publication profile; inspected the README working diff,
all four new records, their scientific review declarations, three paired source
dossiers, timestamped discovery artifacts, the frontier and publication manifest.
Verified record/history/schema input hashes and reviewer identities, exact source
hash receipts, earlier-file preservation, review-base retention and publication
helper guards. The field-level scientific assessments remain in the independently
authored record reviews; this audit does not replace them or claim a fresh
reanalysis of every primary figure.

A successful `rg --files --no-ignore --hidden --follow` inventory covered this
worktree, excluding only Git metadata and the runtime virtual environment.
Source-receipt checks additionally covered their named round 16 and round 17 raw
paths. Those boundaries include ignored and hidden curation files; this is not a
machine-wide absence search. An earlier broad `/private/tmp` inventory encountered
unrelated broken symlinks and was not used to establish absence.

## Exact scientific review coverage

All four records have completed independent `scientific_review: true` observations
with verdict `pass_with_limitations`, no findings, and exact current input hashes.
Their reviewers differ from the respective record authors. All 132 current corpus
records have at least one independent scientific review matching their current
bytes; the structured checker alone was not treated as a coverage proof.

| Record | SHA256 | Independent review |
|---|---|---|
| [biotite](../../../data/records/biotite.yaml) | `52c2162343ba439ef35da695d6aed7cdf03c6e91fb43bfa9c9d706de24a5cbe8` | [YAML](../../../reviews/structured/20261011T105429Z-biotite-round17-independent/review.yaml) · [Markdown](../../../reviews/structured/20261011T105429Z-biotite-round17-independent/review.md) |
| [enstatite](../../../data/records/enstatite.yaml) | `94b7451a26318dfb63100b86b88ac692ec4a577db8ca77edd797b1cba9a8c36e` | [YAML](../../../reviews/structured/20261011T105423Z-enstatite-round17-independent/review.yaml) · [Markdown](../../../reviews/structured/20261011T105423Z-enstatite-round17-independent/review.md) |
| [olivine-group](../../../data/records/olivine-group.yaml) | `2db3527893e6449e4c99491853a28132952a313a6c7f20462560f22dccbcf3e3` | [YAML](../../../reviews/structured/20261011T105423Z-olivine-group-round17-independent/review.yaml) · [Markdown](../../../reviews/structured/20261011T105423Z-olivine-group-round17-independent/review.md) |
| [reverse-osmosis-concentrate](../../../data/records/reverse-osmosis-concentrate.yaml) | `19cad077f7e6536be6cb051af5fdfb3f0d6fe6c72d40cccbe3c3e18b51b1fe73` | [YAML](../../../reviews/structured/20261011T105455Z-reverse-osmosis-concentrate-round17-independent/review.yaml) · [Markdown](../../../reviews/structured/20261011T105455Z-reverse-osmosis-concentrate-round17-independent/review.md) |

The mineral records retain species/group and mixed-feed boundaries; no constituent
criticality is inherited. Enstatite and olivine share one Klug experiment, rather
than representing independent replication. Biotite remains a mica-series group.
The RO record is a process-generated resource, with confounded controls, tentative
phases, source discrepancies and modeled downstream outcomes explicit. Laboratory
assays do not become industrial deployment in the summaries.

## Validation and provenance

- Root terminal receipt `/private/tmp/cmm-round17-gate-receipts.json`, SHA256
  `a97866f32dbfe066d7f81fdc33be528505b734a195c8db28c8df0c7880e027d0`, records actual exit 0 for
  `just check` (308 passed, 3 skipped in 98.20 seconds; 132 records and 148 histories),
  `cmmmech validate --require-records`, and trusted-base history validation.
  The runner, terminal logs and gated record-hash manifest were independently read;
  all current record bytes still match those validated bytes. Native tests were not
  unnecessarily repeated by this auditor.
- Auditor separately ran `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache
  just review-check --base 4504ab1c5a005ea31e65318c3b3f206d6fbf44ed --require-reviews`;
  tool session 93413 completed exit 0 and reported 147 valid review pairs.
- Independent byte comparison against `git archive` of the trusted base found
  all 810 previously tracked scientific files under data/history/reviews/research
  unchanged. No existing scientific record or prior review was rewritten.
- All 18 distinct review bases resolve to commits and are retained in trusted-main
  ancestry or the annotated provenance tag. All new reviews use the merged base.
  Live `git ls-remote` verified tag `review-base/cmm-source-survey-20261009` object
  `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
  `c0adc2c0763e1515ed07dc712b024974d98fb342`, matching local references.
- All 71 distinct current raw-file hash claims in the inspected JSON receipts
  matched retained files. Five explicitly historical failed-DNS empty responses
  were distinguished from later successful acquisitions at the same paths; they
  do not claim that current artifacts are empty. Failed-access HTML and deferred
  main papers are not misrepresented as inspected full text.
- All 202 relative Markdown links in the 29 input paths resolved; the four
  frontier-manifest record hashes and history references match maintained files.
  External URLs were not exhaustively refreshed by this publication audit.
- The terminal package receipt reports canonical-sync exit 0. Its log confirms
  22 artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`.
  The root-acquired ruleset receipt is active SQUASH/ALLGREEN, requires
  `validate-strict` from App15368 and has no bypass actors. Governed files, native
  schema/validator, workflows and installed skills are outside the changed paths.

Independent detailed receipts: `/private/tmp/cmm-round17-independent-publication-check.json`
and `/private/tmp/cmm-round17-independent-links-sources-final.json`. These are local
verification receipts, not committed redistributable scientific source files.

## Findings by severity and corrections

- Blocker: none identified in this publication scope.
- Major: none identified.
- Minor, corrected: [issue #66](https://github.com/CultureBotAI/CMMMech/issues/66)
  recorded the root's finding that the new enstatite and olivine README summaries
  incorrectly said fungal. Both final rows now say **Bacterial**, link the correct
  maintained records, and agree with Gluconobacter oxydans NCBITaxon:442. The retained
  authoritative XML identifies species rank and Bacteria lineage. The underlying
  records already had the correct organism; no artificial scientific EDIT history
  was created for this README correction. Both issue acceptance conditions are
  independently satisfied in the reviewed working state; issue closure awaits
  the authorized publication workflow.
- New actionable findings from this audit: zero. Existing bounded scientific or
  source-access limitations were not manufactured as additional review issues.

## Unresolved questions and publication limits

Primary evidence gaps and concrete next investigations remain in the
[frontier](../../../research/ingests/round17-frontier-20261011.md); this package
makes no global material or source exhaustion claim. Scientific controls and
measurements retain the limitations recorded in each scientific review.

The guarded publication helper restricts staging to the expected frozen file set,
checks the remote trusted base and unused branch, and rejects extra changes. The
squash preflight checks exact tree equality with the topic commit unavailable and
fetches provenance tags. Those scripts were inspected, but their future success
is not claimed here. Exact-tree squash validation, PR and merge-group CI, actual
queue merge, branch deletion, fresh remote-main gates and ignored/untracked
preservation checks remain required operational steps. Standing user authorization
covers those actions; this audit does not grant a governance bypass.

## Verdict

**Pass with limitations for the local publication package.** Zero unresolved
blocker, major or minor findings. The README correction in #66 is independently
verified. Proceed through the documented, guarded publication and queue checks;
report their actual terminal outcomes separately.
