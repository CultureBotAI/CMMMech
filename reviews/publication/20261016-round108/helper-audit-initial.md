# Round108 publication helper review — initial

Reviewed at 2026-10-16T01:41:45.366645+00:00; base `26661b7f033d4bdb915e48e71080aa5774b4c3d6`. Reviewer: Codex /root/round104_uranium, GPT-6. Exact twelve-helper/config snapshots and SHA256 values are retained in the companion JSON. These are session helpers; no Git/GitHub mutations or original-main environment commands were run.

## Scope and evidence

Read all twelve helpers. Verified current round/base/branch, receipt and tree gates, branch-deletion guards, original-main preservation and additive archive behavior. Twenty-eight inert acceptance/rejection probes passed against the actual queue/cleanup binding definitions. An inert call to the actual acquisition issue function reproduced the missing events route. No main function was executed. Probe and evidence hashes are in the JSON.

## Findings by severity

- **Minor PUB108-1:** `release-acquire.py` has `if n in []`, so no source or corrective issue events are collected for premerge assessment. Request paginated events unconditionally for each selected issue and verify the actual function issues all three requests. Final hosted collector already captures issue events; this does not cure the premerge omission.
- **Minor PUB108-2:** `archive.py` generates the heading “Round107 publication receipt” inside the round108 archive. Correct the label and preserve operational guards.

## Corrections and verdict

No helpers changed by reviewer. **Needs changes** for the two concrete adaptation defects. Initial evidence remains immutable; successor review should inspect corrected bytes and rerun affected inert probes.

## Boundaries and unresolved questions

Config counts remain provisional and fail closed in operational queue/cleanup binding checks. Actual commit/tree/PR, complete report issue lists, final gates and hosted results remain future inputs; this audit does not assert them. The release GraphQL literal417 is replaced by the actual receipt PR before use and is not a wrong-PR request. Final hosted assessment must inspect check conclusions and annotations independently of the collector aggregate. Original-main commands in the inspected adapters are Git operations only; isolated clones own project/environment execution. Remote deletion uses an exact-head lease, local deletion a compare-and-swap, and original-main fast-forward preserves pre-existing bytes with `--no-overwrite-ignore` and the current preservation-manifest hash.
