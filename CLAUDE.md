# CMMMech Working Guide

Scope covers critical minerals/materials and microbial extraction,
transformation, and recovery. Read README.md and docs/records.md first.

- Use `just check` before proposing a commit; CI runs the same offline checks
  plus `bash scripts/check_vendored_sync.sh` against the pinned public CLAW revision.
- Keep one record per YAML file under data/records. Do not place fixtures there.
- Criticality needs jurisdiction, list edition, and source, not a global flag.
- Mechanism evidence must support the stated organism, substrate, and conditions.
  Do not extrapolate a laboratory result to industrial performance.
- Never fabricate citations, ontology labels, measurements, or deployment claims.
- Use `.claude/skills/cmmmech-discover-sources/SKILL.md` for source investigations;
  keep discovery reports separate from accepted scientific records.
- Review new or materially changed records with the local
  `.claude/skills/review-record/SKILL.md`; retain a timestamped artifact for
  each record and reviewed file state through `docs/record-reviews.md` under
  `reviews/structured/<timestamp>-<slug>/` (YAML plus generated Markdown).
- Use `rg --no-ignore --hidden` before making absence claims.
- Preserve unrelated changes; never stash/reset or switch an active checkout.
- Do not send issues, PRs, reviews, comments, or other shared-content mutations
  without approval of the exact destination and final content/action.
- Fleet admission and governed artifacts are installed. Use CLAW's supported
  synchronizer and the immutable pin; never hand-edit governed copies.
- Use `just new-history` for canonical sidecars and attach their printed paths
  under `history_refs`; keep inline `curation_history` change events distinct.
  Committed sidecars are immutable: add a new correction session. History paths
  must not contain symlinks. `just check` compares against `HEAD` locally; CI
  supplies the trusted event base through `CMMMECH_HISTORY_BASE`.
- Installed history support does not enable other unverified fleet capabilities.
- The repository's review-open-issues skill is read-only and does not authorize
  implementation, closure, or publication.
