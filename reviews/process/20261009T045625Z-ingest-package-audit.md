# Source-led ingest package audit

## Reviewed state and role

UTC: **2026-10-09T04:56:25Z**, read from the UTC clock. Reviewer:
`/root/ingest_mn_li` (Codex, GPT-6), distinct from coordinator `/root`.
This agent curated manganese/lithium and independently reviewed cobalt's
addition and the two mineral identities. It is therefore not independent of
every scientific change in the batch. This audit checks package consistency;
the separate independent scientific reviewers and exact final record hashes
remain the authority for per-record acceptance.

Worktree `/private/tmp/CMMMech-source-survey-20261008`, branch
`research/cmm-source-survey-20261008`, HEAD
`905388523b6e9184783989484896e4cc20297832`. Changes remain uncommitted.
Scope: README inventory, ranked ingest queue, discovery-key coverage, evidence
boundaries across records, review/hash coverage, preservation of earlier
evidence/history, links and the validation receipt. This is not a repeated
full scientific review, deployment audit or experimental replication.

## Evidence and checks performed

- Read the final [queue](../../research/ingests/20261009-priorities.md),
  [validation receipt](../../research/ingests/20261009-validation.json),
  [README](../../README.md), all new/changed records, the evidence dossiers,
  and applicable record reviews. The queue covers all **12 discovery keys**
  exactly once across 11 ranked rows: A1, A2, D1, D2, E1, I1, I2, I3 and M1-M4.
  I3 appropriately serves the M3 ingest as an identity prerequisite.
- Independently counted **10 records**: seven elements, two mineral species,
  one secondary resource; nine mechanisms, nine dated designations and
  12 canonical history sessions. The change comprises seven new records and
  two changed records. These counts agree with the README, queue and receipt.
- Recomputed all ten receipt record hashes and all nine new review hashes.
  Every changed record's exact final hash appears in its corresponding accepted
  review: **9/9 match**. Unchanged palladium's hash also appears in its prior
  provenance review. The reviews disclose their scientific scope, source access
  limits and independent reviewer roles; retained claims are not represented
  as freshly re-researched where only an addition was reviewed.
- Compared all committed history and prior record-review files against HEAD:
  **all 14 artifacts are byte-identical** (three history sessions and eleven
  reviews). Palladium is byte-identical. Parsed comparisons prove that every
  old cobalt/neodymium mechanism, source, criticality entry and history
  reference remains present unchanged.
- Recomputed the seven hashes recorded in the earlier accepted
  [source-survey review](20261008T074426Z-source-survey-review.md): discovery
  skill and both references, source assessment, search log, acquisition manifest
  and forward test all match. The ingest did not rewrite historical discovery
  limitations to imply that later evidence had been available earlier.
- Checked **59 relative Markdown links** in the final README, ingest dossiers,
  queue and nine new per-record reviews: all resolve. Research JSON parses,
  including the final receipt. `git diff --check` passed during this audit.
- Hidden/ignored-independent filesystem inventories of `data`, `history`,
  `research` and `reviews` included dotfiles and found no symlinks there. The
  research tree contains only Markdown/JSON artifacts, not imported primary
  PDFs, workbooks, spectra or CSV dumps. Original downloaded evidence remains
  outside this worktree. These are bounded repository checks, not a claim that
  such files are absent from the machine or from ignored dependency caches.

## Findings by severity

- **Critical:** none identified within package scope.
- **Major:** none identified within package scope.
- **Minor, corrected:** the queue's M2 row initially said “cell-free lixiviant,”
  whereas the final lamp record and dossier deliberately say clarified culture
  liquid and do not establish sterile filtration before leaching. The coordinator
  changed the queue to “clarified biolixiviant.” This reviewer reread the final
  queue and confirmed consistency without changing any accepted record bytes.
- **Informational:** mineral identity records inherit neither element criticality
  nor mixed-feed mechanisms. Nd's synthetic Mon2 assay remains distinct from
  natural monazite-(Nd), and total-REE lamp results are not assigned to Nd.
- **Informational:** U/V records describe combined electrochemical observations
  with partial microbial attribution; no unmatched comparison becomes a microbial
  effect size. Mn's assay equivalents remain separate from crystalline identity.
  Li retains transient improvement, control convergence, null outcomes and
  unreconciled source contradictions. These boundaries survive README/queue
  summarization.
- **Informational:** completed queue rows refer to scoped accepted claims.
  D1, A2, D2 and I2 remain explicitly deferred; E1 quantitative observations,
  missing controls/phase assignment and Li reproducibility work remain concrete
  follow-ups. No schema or validator behavior changed for narrative curation.

## Validation attribution

This reviewer did not rerun the full test suite in the package audit. The
coordinator's final receipt and the independent Nd/lamp reviewer report
`just check`: lint passed, **215 tests passed, 3 existing optional-command
cases skipped**, ten valid records and 12 valid histories. They report
`uv run --locked cmmmech validate --require-records`: **10 checked, 0 failed**,
and history validation against the stated base: **12 checked, 0 errors**.
The independent reviewer reran the complete gate after the lamp replicate
wording correction. This audit independently performed the file/hash,
preservation, count, JSON and link checks enumerated above. Validation establishes
contracts and provenance consistency, not experimental truth.

## Unresolved limits and verdict

**Accept the local ingest package with the scientific limitations recorded in
its per-record reviews and follow-up queue.** No unresolved critical/major
package finding remains. Primary raw-data gaps, source inconsistencies and
unproven industrial deployment were preserved rather than silently resolved.
The original checkout's clean state and lack of remote mutations are reported
by the coordinator; this audit did not operate other checkouts or GitHub.
Publication and integration of a separate governance branch are outside scope.

## Reviewed package hashes

| Path | SHA-256 |
|---|---|
| `README.md` | `a0e4a94ab9675c8ea041a2111230c9706460f85f7e7c7a247fd9da20327fcb63` |
| `research/ingests/20261009-priorities.md` | `7ce72d5bcf6d160363f11ff7eb86796aca0d3ab799863cca2f62ab7a078a7f43` |
| `research/ingests/20261009-validation.json` | `252e126393d41179f77538d124a5941b0f4ad523181a5b1dbb37296c81f001ae` |

The receipt contains the individual record and review hashes independently
matched above. The coordinator has frozen these package files for this audit.
