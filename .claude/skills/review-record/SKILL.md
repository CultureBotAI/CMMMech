---
name: review-record
description: Adversarially review CMMMech material records against primary evidence and identifiers, and save timestamped per-record Markdown review artifacts. Use for new or changed data/records YAML, not fleet admission or publication.
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

Save a separate UTF-8 file for **each** record and review round:
`reviews/records/<record-slug>/<YYYYMMDDTHHMMSSZ>.md`.
Read the UTC clock; never fabricate a timestamp. Do not overwrite a prior round.
Use this consistent structure (additional scientific sections are welcome):

1. **Record ID/path** — stable ID and repository-relative YAML path; reviewer
   role and independence from its curator.
2. **UTC timestamp** — ISO 8601 UTC time.
3. **Reviewed revision and working changes** — `git rev-parse HEAD`, branch,
   tracked/untracked changes relevant to the review, and SHA-256 of reviewed
   record bytes. If correcting in this round, give pre/post hashes. A review
   of uncommitted content must not claim it is contained in the HEAD commit.
4. **Scope** — included claims, exclusions and acquisition limits.
5. **Evidence checked** — primary URLs/DOIs, section/table locators, authority
   and identifier lookups, contradiction/correction searches and access date.
6. **Findings by severity** — critical, major, minor, informational; explicitly
   say when a severity has no findings. Link each finding to a field and source.
7. **Corrections** — concrete edits and whether independently rechecked.
8. **Unresolved questions** — scientific uncertainty and any blocking work.
9. **Verdict** — `accept`, `accept with limitations`, or `revise`; no acceptance
   with unresolved critical/major errors. Limitations retained accurately in the
   record may remain. Include actual validation commands and results.

Run the affected file validation, then `just check` and
`uv run --locked cmmmech validate --require-records` for the completed batch.
Validation does not prove scientific truth. After subsequent substantive edits,
repeat affected evidence checks and save a new timestamped round with the final
record hash. Report all artifact paths and unresolved limitations.
