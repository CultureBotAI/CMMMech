# Round105 publication-helper audit successor

Recorded 2026-10-15T23:12:32.460072+00:00 by `codex /root/round104_uranium` (GPT-6, Codex), independently of coordinator/fixer `/root`. Reviewed base `ee4ea8c2efa351a688946660c9ddc70560c3e86e` with exact corrected helper bytes identified in the paired JSON.

**Verdict: pass with limitations.** Both findings from the immutable [initial audit](helper-audit.md), tracked in [issue 407](https://github.com/CultureBotAI/CMMMech/issues/407), are resolved.

## Corrections and evidence

- **PUB105-1, minor, resolved:** finalization now binds current config/helper hashes to the commit receipt and requires complete, successful postmerge validation plus successful matching coverage. It rejects missing or duplicated gates, failed gates even if listed as allowed, wrong command directories, wrong counts/clone, malformed receipt identity, and changed current helpers/config before any main mutation.
- **PUB105-2, minor, resolved:** cleanup verifies the expected CMMMech origin before any API or deletion. Valid exact-ref flow succeeds; a different origin or moved local/remote ref fails before deletion. Finalization also verifies origin before main operations.

The coordinator's 33 pure/order regression cases were inspected. Independently, 33 exact-caller AST cases passed using inert Git/API functions and actual corrected guards. These repeat the original invalid-evidence and wrong-origin demonstrations and add malformed receipts/current-hash tests. All eight helpers parse as Python. The initial audit remains byte-for-byte unchanged.

## Reviewed working changes

The correction changes `publication-guards.py`, `finalize.py` and `cleanup.py`. Exact hashes for all eight helpers plus config, the retained patch, regression receipts and independent probe outcomes are in the paired JSON. Reviewer made no helper, owner, Git or GitHub changes.

## Unresolved questions and limits

- Final topic/tree/PR/preflight bindings and measured counts are pending. Issue lists are bound to [133,397,403,404,405,406,407,408,409], with 407 expected closed after merge and the others expected open. That future disposition is not asserted to have occurred; remaining explicit placeholders are not publication-ready.
- Recheck final bindings against actual commit and PR receipts before queue admission.
- These inert tests do not claim that preflight, merge queue, hosted checks, deletion or fresh postmerge clone validation already ran. Those event receipts remain separate required evidence.
- No unresolved corrective finding remains in this bounded helper audit. Scientific record validation was not repeated for helper-only changes.
