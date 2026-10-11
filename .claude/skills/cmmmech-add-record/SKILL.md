---
name: cmmmech-add-record
description: Add evidence-backed critical mineral or material records to CMMMech, with identity checks, primary-source curation, history, validation, and saved scientific reviews. Use when creating data/records YAML or curating a source-discovery handoff; use cmmmech-discover-sources for research without record creation.
---

# Add a CMMMech record

Create a scientifically defensible record and its review artifacts, carrying the
requested local curation through corrections and final validation. Evidence may
justify an identity-only record; criticality and microbial mechanisms are not
mandatory. Do not fill unsupported fields merely to resemble another record.

## Orient and select the record

Work in a verified CMMMech checkout. All paths below are relative to that
checkout, not the installed skill directory. Read applicable `AGENTS.md`,
`CLAUDE.md`, `README.md`, `docs/records.md`, the authoritative
`src/cmmmech/schema/cmmmech.yaml`, relevant validator/tests, and nearby records.
Inspect git status and worktrees; use an isolated branch/worktree for curation
without switching, stashing, or resetting another session's checkout. Retain an
available trusted base revision for append-only history and review checks. Run
`just check` before changes and distinguish pre-existing failures from new ones.

Use the user's material and evidence scope. When selecting from a discovery
handoff, inspect the assessment and rank candidates by primary evidence quality,
identity clarity and useful coverage; briefly explain the selection. Read the
relevant research reports and existing review findings before claiming novelty.
Search records, research, reviews, and referenced local downloads with
`rg --no-ignore --hidden`; follow relevant symlinks and state search boundaries.
Deduplicate by material identity and verified IDs, and studies by DOI/accession
and experiment, not just filename or title. If the same material already has a
record, update that record within the requested curation scope instead of adding
a duplicate. Keep a deferred candidate in research when evidence cannot support
an accepted record; do not place speculative drafts or fixtures in the corpus.

Ground the concept before choosing a slug or identifier. Elements, ions, mineral
species/groups, commodities, alloys and secondary resources differ. Use only
current schema kinds (`element`, `mineral`, `mineral_group`, `commodity`,
`secondary_resource`); describe experimental salts, ions or alloys in context
without pretending their identifiers identify an element or mineral. Resolve
every asserted external ID and label at its authority. Leave unsupported IDs
absent. Do not inherit criticality or mechanisms from a constituent element into
its host mineral or waste feed.

## Establish evidence for each claim

Use `.claude/skills/cmmmech-discover-sources/SKILL.md` when additional source
investigation is needed. A discovery report is a handoff, not verification of
every proposed claim. Inspect the official list, primary full text, methods,
results, tables/figures and supplements relevant to the record. Verify source
identity, edition/version and access dates; retain precise locators in source
titles, evidence explanations or a research dossier. For local-only work,
distinguish inspected artifacts from live checks not performed.

- Criticality requires authority, jurisdiction, exact list, edition and source.
  Explain grouped-list or commodity mappings in the record. Historical editions
  are valid evidence for that edition; claims about the latest list need a
  current authority check. `not_listed` requires the complete relevant list.
- Mechanism evidence must support the stated organism/strain or community,
  biomass state, substrate, pretreatment, conditions, controls, outcome and
  scale. Keep unavailable details explicit. Species identity does not prove
  strain identity or a member's causal role. Unresolved communities need no
  invented taxon ID. Inactive microbial biomass still uses `microbial: true`,
  with its inactive state explicit; this does not imply metabolism.
- Preserve null results, contradictory evidence and weak controls. Use
  `support`, `partial`, `refute` or `context_only` for the particular claim the
  evidence explanation identifies. Search relevant corrections, retractions and
  conflicting results, recording coverage and access limits. Do not invent a
  refutation to populate a field or erase a supported narrower observation.
- Keep measured and fitted values distinct, units and denominators attached,
  and proposed molecular causes separate from demonstrated activity. Dissolution
  or solution depletion does not alone establish isolated-product recovery.
  Laboratory assays, pilot biomass cultivation and industrial feedstock origin
  do not establish industrial deployment of the mechanism.

An abstract or snippet cannot verify unavailable methods or measurements. After
bounded legitimate acquisition attempts, narrow or defer unsupported claims
and record the missing evidence. Never invent citations, measurements or access.
Keep bulk raw data and copyrighted full text outside committed artifacts unless
redistribution is justified; record provenance and source terms for retained data.

## Curate YAML and history

Create one `data/records/<slug>.yaml` with `id: cmmmech:<slug>`. Follow
`docs/records.md` and the live schema rather than copying another material's
claims. Supply required fields and record-local source IDs; quote YAML dates
and timestamps. Link every criticality/evidence/observation source reference to
that record's sources. Keep optional unknown claims absent or explicitly scoped.

If curating quantitative observations, read the quantitative-source section of
`docs/records.md`. The current contract is exact source concentration cells in
`mg/kg`, not yields, rates or pooled effects. Preserve raw tokens, cell keys,
units, assay fractions, arms, dates and source-defined censoring; never turn a
detection limit into zero or infer a density conversion. Other measurements may
remain qualified prose with locators. Change native schema/validator behavior
only for a demonstrated need and add meaningful regression coverage. Do not
hand-edit governed CLAW copies or introduce an importer just to add a few records.

As this skill's curation workflow, create a canonical sidecar with
`just new-history`, using `--event CREATE` for a new record (`EDIT` for an
existing one), actual actor/model/tool metadata, and finished summary/details.
Read `docs/records.md` for the command arguments. Append its printed path under
`history_refs`; the helper does not modify the record. Add a distinct inline
`curation_history` event describing the actual change. Do this before capturing
review hashes. History presence is advisory in the schema, but this workflow
records its work. Do not backdate, invent earlier authorship, rewrite committed
sidecars, or use symlinks beneath `history/`.

## Review, correct and validate

Validate each edited file with `uv run --locked cmmmech validate <record-path>`.
Apply `.claude/skills/review-record/SKILL.md` to every new or materially changed
record, using an independent reviewer/agent when available and disclosing any
single-agent review. Read `docs/record-reviews.md` and
`docs/record-review-profile.md` for the actual shared output contract.

Capture exact targets, Git base, working state and input hashes with
`uv run --locked python scripts/record_review.py inspect --targets <targets.yaml>`
before judging. Assess primary evidence and identifiers independently of offline
validation. Save one `kind: record` observation per record/reviewed state through
`scripts/record_review.py save --content <completed-review.yaml>` in the project
environment. Required outputs are immutable
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` and generated
`review.md`, with actual UTC times, scope, evidence, findings, verdict and limits.
Do not write new legacy `reviews/records/` reports or hand-edit generated verdicts.

Address supported findings in maintained records. After substantive changes,
repeat affected checks and save a new review of the final bytes, including any
new history references. Resolve findings explicitly with stable issue keys and
exact predecessor occurrence links; a newer clean review alone cannot close an
older finding. Preserve prior observations. Do not claim a passing record with
unresolved major/blocker findings. Save an honest partial/blocked observation
when required checks are unavailable, as the review contract permits.

For the completed batch, run:

```sh
just check
uv run --locked cmmmech validate --require-records
uv run --locked cmmmech validate-history --base <trusted-base>
just review-check --base <trusted-base> --require-reviews
```

Replace `<trusted-base>` with the actual available revision established for this
change, not a base selected to hide a history rewrite. Record command results.
The full-corpus gate detects duplicate IDs that single-file checks cannot;
`just check` does not replace the separate structured-review check. Manually
verify every changed record has a current scientific review matching its final
hash; a nonempty review gate alone does not establish coverage. Repeat checks
affected by corrections. Report unresolved evidence and validation limits.

## Deliver and publish within scope

Report added/updated/deferred records, history paths, both review artifact paths,
validation results, worktree/branch and remaining scientific questions. Record
creation authorizes local curation and reviews, not automatic external posting.
Follow the user's existing authorization for commits, PRs, issues, comments,
merge and branch cleanup; do not ask again for actions already authorized.
Do not configure fleet admission or governance as a side effect of curation.

When publication is requested, follow
`docs/record-review-profile.md#publishing-through-the-squash-queue`, including
preservation of every otherwise-lost review base and fresh-checkout validation
after squash/branch deletion. Keep saved reviews immutable and use the current
repository publication process without bypassing required checks.
