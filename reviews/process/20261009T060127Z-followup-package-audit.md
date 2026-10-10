# Follow-up ingest packaging audit

## Target and reviewer

Target: the [follow-up report](../../research/ingests/20261009T054507Z-followup.md),
its [validation receipt](../../research/ingests/20261009T054507Z-validation.json),
and the consistency and preservation of the package they describe.
Reviewer: `/root/ingest_bes`, Codex (GPT-6).

This reviewer curated uranium/vanadium and implemented the observation contract.
This is a packaging audit, **not independent scientific acceptance of those
records or independent implementation acceptance**. The coordinator separately
reviewed U/V; `/root/ingest_ree` independently reviewed the implementation. This
audit checks their review artifacts against the final bytes. It also does not
replace the independent scientific reviews of the other four changed records.

## UTC timestamp

2026-10-09T06:01:27Z, read from the UTC clock. Local checks immediately preceded
this timestamp; this artifact was written afterward.

## Reviewed revision and working changes

Worktree `/private/tmp/CMMMech-source-survey-20261008`, branch
`research/cmm-source-survey-20261008`, base/HEAD
`610d27a40d89861961052f0e0bebfaa7882e35cf`, plus the uncommitted follow-up changes.
The report and receipt are new files, not artifacts already contained in HEAD.

| Artifact | SHA-256 at audit |
| --- | --- |
| `research/ingests/20261009T054507Z-followup.md` | `99e2182757f385c3a639d7dc2ae8f3d8d52879a6466b3825886850e42f447ee2` |
| `research/ingests/20261009T054507Z-validation.json` | `95be71ebac173460d3936d060b8c32ebf3cdf35a6ae6d9fbb6cfa6e15f7edc62` |

No record, implementation, history, prior review, report or governed file was
edited by this audit. The only addition is this artifact.

## Scope

Check reported corpus counts, exact record/review/implementation hashes, local
links, baseline preservation, original checkout state, worktree inventory,
governed artifact integrity and diff whitespace. Scientific limitations remain
within the record reviews and evidence dossiers. No new literature search or
full test rerun was needed for this packaging-only pass.

## Evidence checked

- Parsed all ten YAML records and the JSON receipt. Recomputed every record
  hash, all six latest review hashes, the four implementation hashes and the
  implementation review hash; every value matches the receipt. Each latest
  record review contains the exact current record hash, and the implementation
  review contains all four current implementation hashes.
- Recomputed corpus totals: **10 records** (7 elements, 2 minerals, 1 secondary
  resource), **9 mechanisms, 13 criticality entries, 8 observations** (7 measured,
  1 below detection; 7 explicit sampling dates), and **19 history sessions**.
  Six records changed, zero records were added, and seven history sessions and
  six per-record reviews were added relative to the checkpoint. These match
  the report and receipt; counts are not biological replication counts.
- Compared every baseline record recursively against current YAML. All prior
  scalar fields, dictionary entries and list prefixes are preserved. The four
  unchanged records are byte-identical. Every current record's history
  references match the receipt.
- Compared all **76** receipt-listed preserved files against their Git blobs
  at the base: zero differences. This includes all committed history sessions,
  research reports, reviews, local skills, workflows, governed schema imports
  and the canonical pin. Broader committed-prefix checks also found no change
  in `history/`, `reviews/`, `research/`, `.claude/`, `scripts/` or `.github/`.
- Independently compared all **18** CMMMech-governed artifacts' bytes and file
  modes with the canonical manifest at pinned revision
  `849f336e025510316a5f235eb0af8547b8bd50cc` in the available authority checkout.
  All match. This is an offline check against the pinned authority, not a
  fresh check of a remote branch.
- Checked **33** relative links in the follow-up report, six latest record
  reviews and implementation review: every target exists. The README/report
  observation link resolves to the actual `Quantitative source observations`
  section in `docs/records.md`. Evidence dossier links were also checked.
- Inspected tracked and untracked changes; additions are Markdown, JSON, YAML
  and the synthetic Python test file, without bulk publisher workbooks/PDFs.
  Hidden/ignored-inclusive inventories and searches were used where completeness
  mattered. The original checkout has no tracked or untracked changes at
  `905388523b6e9184783989484896e4cc20297832`; ignored caches, `.venv`, build output
  and Python metadata remain present and are not claimed absent.
- Read the worktree inventory. The concurrent governance worktree remains at
  `380a80f71b631bead5686fd7fecc9644b2e02ef1`, the prior integration worktree at
  `c32d78e26a15bb67a737700668badaed7da10597`, and the detached admission worktree
  at `905388523b6e9184783989484896e4cc20297832`. This audit made no Git mutation.
- `git diff --check` passed. The coordinator's completed final gates are
  separately recorded in the receipt: `just check` **280 passed, 3 skipped**, ten
  records valid, 19 histories valid; `validate --require-records` and
  `validate-history --base 610d27a40d89861961052f0e0bebfaa7882e35cf` passed.
  Those full-suite results are attributed to the coordinator, not rerun here.

## Findings by severity

- **Critical:** none within packaging scope.
- **Major:** none within packaging scope.
- **Minor:** none requiring correction in the audited final package.
- **Informational:** historical reports/reviews correctly retain their earlier
  revision and count snapshots; the new report identifies its separate base.
- **Informational:** accepted scientific limitations and future ingest priorities
  remain explicit. A package consistency check does not establish causal
  microbial effects, industrial deployment or source truth.

## Corrections

No package correction was needed in this audit. The coordinator had corrected
the observation-section anchor before this final pass; it was verified here.
No prior artifact was rewritten to incorporate this review.

## Unresolved questions

No blocking packaging question remains. U/V source scope and causality, lithium
quantitative discrepancies, historical EU-list coverage and other next-ingest
questions remain documented in the linked dossiers and independent reviews.
Remote publication and any later integration are outside this local audit.

## Verdict

**Accept the local follow-up package for its stated scope and exact audited
bytes.** Counts, provenance references, review coverage, preservation claims
and validation reporting are consistent. Independent U/V scientific acceptance
and implementation acceptance remain delegated to their separate reviewers.
