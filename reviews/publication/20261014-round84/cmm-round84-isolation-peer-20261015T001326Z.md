# Round84 isolation-tool static review

Independent static read only: two root-authored round84 isolation helpers and current local publication requirements. No helper top-level execution, network call or Git mutation. Authored cinnabar and independently reviewing silica-sand; this is an operational assessment, not self scientific acceptance.

UTC: 2026-10-15T00:13:26.687736Z

Verdict: **pass with limitations**; no supported corrective findings.

- Full helper source and AST inspected; exact derivation is only round83-to-round84 labels/paths and trusted-base substitution. No stale round83 cohort claim remains.
- Fresh uniquely named /private/tmp clone and exclusive output paths; source checkout operations are read-only. Temporary deletion/add/commit are confined to the new clone. Archive path filtering and safe extraction reject traversal and external links. No push or source branch deletion occurs.
- Preflight requires clean exact source head/tree and remote main at trusted base; synthetic tree matches topic exactly and parent is trusted base. Topic commit absence is checked three times.
- Postmerge requires local and remote topic refs absent, fresh remote main equal actual merge, identical reviewed tree and exactly one trusted-base parent.
- Explicit tag fetch, retained annotated tag object/peeled remote target verification, canonical review checker, and every distinct native review base commit availability checked.
- Named strict nonempty corpus/history/review gates bind retained logs; postmerge additionally runs just check. Coverage follows hidden/ignored directories and symlinks with cycle prevention, requires canonical target/path/exact record SHA and completed positive scientific review.
- Configured expected counts are read at execution. Current provisional record-only configuration is not final all-count evidence and must be reconciled before runtime publication. Existing helpers supplement, not replace, native finding-lineage validation.

Current configuration contains only the provisional 403-record count. This audit does not treat that as a complete runtime census. Final config and actual isolated gate receipts remain publication prerequisites.

- `/private/tmp/cmm-round84-isolated-verification.py` SHA256 `df16aea762aaa88f2be39143595e3c9d9fe5a1cb9f9185ecad61d959ffcab2a4`
- `/private/tmp/cmm-round84-isolated-coverage.py` SHA256 `cb22e6f5f1c3956a2972e443fefd3f4ad6d775e0a58515567318ec9f9991d9f3`
