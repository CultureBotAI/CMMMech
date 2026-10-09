---
name: review-record
description: Adversarially review CMMMech material records against primary evidence and identifiers, and save schema-validated timestamped per-record YAML/Markdown review bundles. Use for new or changed data/records YAML, not fleet admission or publication.
---

# Review a CMMMech record

Read `CLAUDE.md`, `docs/records.md`, the record, schema, and relevant working
diff. Review the exact file state; an earlier review does not cover later edits.
Use an independent reviewer when available, including a different agent from
the curator. A single-agent pass must say so, not claim independent review.

Before duplicate or absence claims, search hidden and ignored files with
`rg --no-ignore --hidden`. Keep the main checkout and unrelated work intact.
An assigned review authorizes a local review artifact. Correct record content
only when the task authorizes curation; otherwise report proposed corrections.
This skill does not authorize shared messages, issues, PRs, merging, or admission.

## Scientific checks

- Check primary full text, methods, results, figures/tables and relevant
  supplements. Record exact section/table locators and access limitations.
  Search for corrections, retractions and directly relevant conflicting results;
  state search coverage, not an unsupported claim that none exist.
- Resolve every asserted external identifier and verify its label and scope.
  An element, ion, mineral species, commodity, alloy and secondary resource
  are different concepts. A species identifier does not identify a strain or
  establish a consortium member's causal role.
- Check criticality against the named authority, jurisdiction, list and edition.
  Preserve grouped-list scope and distinguish historical from current status.
  A source's generic use of "critical" is insufficient.
- Test every mechanism against its organism/strain or community, substrate,
  pretreatment, biomass state, conditions, controls and outcome. Keep measured
  results separate from fitted/modelled values and inferred molecular causes.
  Separate solubilization or aqueous removal from isolated product recovery.
  Do not turn laboratory assays, pilot biomass cultivation or a waste supplier's
  industrial origin into industrial deployment of the mechanism.
- Preserve contradictory results, weak controls, unknowns and transfer limits.
  Use `partial`, `refute` or `context_only` for the particular claim explained;
  disagreement with an overbroad claim need not refute the narrower observation.
- Check inline `curation_history` events and linked `history_refs` sidecars as
  distinct provenance. Verify the actual actor, timestamp, target and change
  described; adoption of history must not invent earlier authorship. Validate
  sidecars against the reviewed Git base with `cmmmech validate-history --base
  <revision>`. Committed sessions are immutable; corrections need new sessions.
- For a provenance-only change, prove scientific bytes or field values are
  unchanged from the reviewed baseline and identify the earlier scientific
  review. State that literature was not reassessed; do not present a metadata
  check as fresh scientific verification.

## Required artifact

Use the CLAW contract in `docs/record-reviews.md` and the local routing profile
in `docs/record-review-profile.md`. Every record and review round requires its
own schema-valid `kind: record` observation. Save through
`uv run python scripts/record_review.py save --content <completed-review.yaml>`
to `reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` and its generated
`review.md`. Do not hand-author a separate verdict or overwrite an older round.

Capture actual UTC start/finish, independence and its basis, exact target path,
Git base and reviewed byte hashes with the shared `inspect` command before the
assessment. Preserve uncommitted provenance honestly. Retain material form,
criticality authority/jurisdiction/list/edition, biomass state, organism/strain,
substrate, pretreatment, controls, outcome and deployment scope in evidence-linked
assessment dimensions/details. Keep measurements and local metrics with their
definitions, units and denominators. Link each finding to its evidence, affected
field, maintained input and proposed acceptance checks.

Map native `critical` to shared `blocker` with an explicit normalization reason;
retain major/minor/informational and native rule labels as applicable. Shared
verdicts are `pass`, `pass_with_limitations`, `needs_curation`, `blocked`,
`seed_only`, or `not_assessed`; optional `native_verdict` retains accept/revise
wording without becoming a second decision. No passing verdict with unresolved
blocker/major errors. For provenance-only work use `scientific_review: false`
and state literature was not reassessed.

Once a target is resolved, unavailable required checks need an honest partial
or blocked saved observation. If the saver itself is unavailable, report that
persistence is blocked rather than claiming a session-only review was saved.
Earlier `reviews/records/` Markdown stays historical; do not convert it by
guessing findings or rewriting timestamps. A follow-up retains the issue key
and exact previous occurrence links instead of silently closing old findings.

Run the affected file validation, then `just check` and
`uv run --locked cmmmech validate --require-records` for the completed batch.
Validation does not prove scientific truth. After subsequent substantive edits,
repeat affected evidence checks and save a new timestamped round with the final
record hash. Report all artifact paths and unresolved limitations.
