Title: Correct round95 hosted-review authored-owner guard and stale role provenance

The independent static review found OP1 (`CMMMech.round95.hosted-review-authorship-cohort`, minor operational): round95's hosted-peer special independent-review guard still tested `petroleum-coke`, absent from the current cohort, while its JSON provenance and hosted-five role description retained round94 authorship.

The current authored owner is `spent-steel-pickling-liquors`, whose science is independently reviewed by the root agent. The operational reviewer independently reviewed `hauerite` and `melanterite`. Generic scientific independence/target/hash checks were present, but the intended current-owner reviewer check was bypassed by the stale slug. No scientific record defect or completed hosted-runtime success is asserted.

Initial evidence and exact source snapshots will be retained in this PR under `reviews/publication/20261015-round95/`, including `cmm-round95-helper-static-initial-20261015T125808Z.json` and its Markdown pair/source directory. Exact occurrence lines and initial hashes are recorded there.

Acceptance:
- Apply the current owned-slug guard with actual independent root reviewer identity, retaining generic target/hash/history checks.
- Make JSON/Markdown authorship and limitations reflect the actual round95 assignment; keep the already-correct COMMENT and its exact-byte posting guard unchanged.
- Verify the actual AST guard accepts the root reviewer and rejects this owner author or the wrong reviewer for the current owner, without API mutation.
- Preserve before/after helper sources and checks, obtain independent static resolution, and require the separate actual hosted runtime before publication acceptance.

Final count changes (525 histories/542 reviews) are a separate expected reconciliation after the heterosite review correction, not this defect.
