# CMMMech Review Profile

The common output contract is [record-reviews.md](record-reviews.md), using
`schema/record_review.yaml`. `conf/record_review.yaml` declares the entrypoints
and rubrics checked in CI.

- Named records: `.claude/skills/review-record/SKILL.md` is the native adversarial
  rubric; `review-yaml-record` routes the common single-record workflow to it.
- Categories: `review-yaml-category` adds exact membership and evidence-backed
  lump/split/retain/defer decisions. Elements, ions, mineral species, commodities,
  alloys and resources must not be lumped merely because they share an element.
- Maintained targets are `data/records/*.yaml`. Future scientific fixes belong
  there, not in a review artifact. This infrastructure does not authorize edits.
- The local field contract is `docs/records.md`. Preserve criticality authority,
  jurisdiction/list/edition, experimental material form, organism and strain,
  biomass state, conditions, controls, measured/modelled outcome, and deployment
  limits. Solubilization/removal is not automatically recovered product.
- Keep critical/major/minor/informational priorities and normalize explicitly.
  Retain provenance-only scope separately from fresh primary-literature review.

Run `uv run --locked cmmmech validate <record>` for a named file, `just check`
and `uv run --locked cmmmech validate --require-records` for the batch, and
`uv run --locked cmmmech validate-history --base <revision>` where sidecars
are in scope. These are offline structural checks, not scientific verification.
Record each actual command/result and any unavailable check in the review.

`just review-check` validates all new-format bundles and their append-only
history. CI supplies `RECORD_REVIEW_BASE` from the trusted event base. Old
`reviews/records/` artifacts remain unchanged historical reviews; new output is
the standard YAML/Markdown pair in `reviews/structured/`.

Saving a review does not append an inline event or canonical history sidecar,
change `history_refs`, claim an earlier actor's work, or authorize GitHub
publication. Follow CMMMech's exact-content approval rule for shared mutations.
