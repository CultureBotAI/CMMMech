# Independent commit-helper amendment review

2026-10-15T17:52:03.312093+00:00 — codex /root/round99_sulfates (GPT-6).

Verdict: **pass_with_limitations**. Finding OPH1 is resolved; no unresolved findings. [Issue363](https://github.com/CultureBotAI/CMMMech/issues/363).

Independent of vanadium agent implementation. Read complete original/current helper and exact diff, independently executed the inspected regression suite, made no helper or Git/GitHub edits.

The original runtime review remains unchanged. Only `/private/tmp/cmm-round99-commit.py` changes from `74d13a0ea171dac8ebc158e05e64ebddb7b02ee02458f984adb64aa1df477c59` to `8aba55b56d686d2ae52c927503005e99cc0666fe055fcd961ea9d50374da8a55`; the other twelve core helper hashes match.

Only one inserted checker/constants block and two call-site replacements differ from the accepted original; reversing those exact changes reproduces original source bytes. All other twelve core helper hashes match the original runtime audit.

The exception requires Git status2, exact complete stdout diagnostic for dossier lines3/4, and empty stderr. Status0 requires empty stdout/stderr. Missing/reordered/extra output, different statuses or any stderr are rejected. No global whitespace configuration or broad path exclusion was introduced.

On the exception path the entire dossier SHA256 and exact double-space lines are required. Working mode requires a regular nonsymlink file; staged mode reads the indexed blob with git show and verifies that blob instead of trusting disk. Read failures propagate. Existing prepared manifest and staged-content guards remain unchanged.

Independently executed thirteen inspected mock-only cases: clean and exact allowed paths; extra/missing/reordered/changed diagnostic; changed complete file and index-only bytes; wrong status; stderr; wrong spaces despite adjusted hash; missing/symlinked file; index read failure; both real helper call sites. All passed; no Git subprocess or mutation occurred in the suite.

Implementer captured the original actual staged status2 diagnostic at17:48:25; those retained bytes match the exception constants and independently verified dossier. My17:48:37 read occurred after root recovery unstaging, when actual cached check was clean. The review does not misattribute the original failing-index observation as my independent execution.

Independent tests: **13 passed, 0 failures, 0 errors**. The paired JSON binds the exact test, receipt, log, original/current helpers and prior review.

Limitations:

- This is acceptance of the narrow commit helper amendment, not proof of successful live commit or hosted publication. Root must rebuild exact publication bindings and rerun its precommit checks before invoking.
- The initial runtime review remains immutable; hosted consumers must explicitly verify this single commit.py amendment chain while retaining the original other-twelve hashes. Separate readonly-helper adaptation review is required.
- The thirteen new tests are mock-only and scoped to this behavior. Existing core guard/receipt regression evidence remains distinct; provider failure and race behavior is not newly tested.
- Any later helper byte change invalidates this exact-hash acceptance. The preserved original and recovery receipts remain separately auditable.
