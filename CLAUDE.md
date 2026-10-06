# CMMMech Working Guide

Scope covers critical minerals/materials and microbial extraction,
transformation, and recovery. Read README.md and docs/records.md first.

- Use `just check` before proposing a commit; CI runs the same checks.
- Keep one record per YAML file under data/records. Do not place fixtures there.
- Criticality needs jurisdiction, list edition, and source, not a global flag.
- Mechanism evidence must support the stated organism, substrate, and conditions.
  Do not extrapolate a laboratory result to industrial performance.
- Never fabricate citations, ontology labels, measurements, or deployment claims.
- Review new or materially changed records with the local
  `.claude/skills/review-record/SKILL.md`; retain a timestamped artifact for
  each record and reviewed file state under `reviews/records/<slug>/`.
- Use `rg --no-ignore --hidden` before making absence claims.
- Preserve unrelated changes; never stash/reset or switch an active checkout.
- Do not send issues, PRs, reviews, comments, or other shared-content mutations
  without approval of the exact destination and final content/action.
- Fleet admission and governed history/vendored artifacts are pending. Do not
  invent a CLAW pin or hand-edit governed copies to claim parity.
- The repository's review-open-issues skill is read-only and does not authorize
  implementation, closure, or publication.
