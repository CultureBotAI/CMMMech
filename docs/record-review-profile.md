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

## Publishing through the squash queue

The native merge queue squashes topic commits. A saved review's
`source.git_revision` must remain available after its topic branch is deleted,
including when `source.state` is `working_tree`. The shared checker intentionally
rejects an unavailable base. A working-tree attestation preserves inspected
hashes; retaining its base does not change it into a committed-byte attestation.

Before queue admission:

1. Enumerate the distinct `source.git_revision` values in the bundles being
   published. Check each exact revision and retain any base that will not remain
   in `main` history under an annotated `review-base/<descriptive-unique-name>`
   tag. Confirm the name is unused, target the inspected commit exactly, and
   push the explicit tag ref. Do not move or delete a published provenance tag.
   These tags are evidence references, not software releases.
2. Verify the tag's peeled commit remotely. Record its name and revision in the
   publication receipt. A tag for one revision does not preserve unrelated
   review bases; enumerate every distinct revision, including follow-up rounds.
3. Run the structured review checker against the trusted PR base and inspect
   record coverage/hashes. Its nonempty gate does not itself prove that every
   changed record has a current scientific review.
4. Verify an isolated squash-shaped checkout without the topic branch. Fetch
   tags explicitly and require saved review validation to pass. After the actual
   merge and branch deletion, repeat in a fresh checkout of remote `main`.

Consumers must fetch the retained references before checking provenance:

```sh
git fetch origin --tags
uv run --locked python scripts/record_review.py check --require-reviews --base HEAD
```

The CI checkout uses `fetch-depth: 0`, which fetches complete branch/tag history.
A shallow or single-branch clone must not assume that an unrelated provenance
tag was fetched automatically. If a base is unavailable, fetch its documented
reference and verify its target; do not rewrite the review or relax the governed
validator. No review base should depend solely on a soon-to-be-deleted branch.
