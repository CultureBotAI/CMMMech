# Round 63 preliminary publication finding

UTC: 2026-10-14T05:48:36.639903+00:00. Reviewer: codex /root/round63_publication_audit, GPT-6, with independent helper inspection by /root/round63_publication_audit/helper_safety. Neither authored the operational helper or scientific content.

Reviewed working revision: 1e3d834112099855c0398459415d0022336055f5. Scope: local queue-admission helper `/private/tmp/cmm-round63-enqueue.py`, SHA256 `2371cec932c85cf48a51d72ddd3b0530efc5edb1d9e8d88b95b087ead34c1dbf`. This preliminary report is not final publication acceptance or a scientific record review.

## Findings by severity

**Major / P2 — Require a fresh trusted-base check before queue admission.** The queue helper checks the topic head and stored preflight head/tree but does not verify preflight mode/trusted_base or fresh remote main against the reviewed base immediately before admission. A main advance after preflight can be admitted; later cleanup and hosted audit detect parent/tree mismatch only after merge.

The invariant is already required by isolated preflight, cleanup, hosted audit and original-main synchronization. Moving the same check to immediately before admission reduces the window in which a known stale base could enter the queue. It does not guarantee immunity to later concurrent updates.

## Correction and acceptance

Require mode=preflight, trusted_base equal commit receipt base, matching successful commands/log and a fresh read-only remote main/base equality observation immediately before enqueue; retain that observation in the queue receipt. A subsequent concurrent update remains a native queue race.

Inspect revised guard, compile helper, exercise the guard in an isolated mocked command harness with matching and changed base and mismatched preflight identity; no live enqueue required for this regression.

## Verdict and unresolved questions

Needs correction before this audit's passing verdict. No helper or scientific file was changed by this reviewer. All other inspected guards were supported. The final audit must reference this observation and explicitly record its disposition; it must not erase this finding.
