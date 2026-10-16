# Round107 finalization and archive helper review

- UTC timestamp: 2026-10-16T00:48:27.875151+00:00
- Reviewer: Codex (GPT-6; codex), independent of root's helper adaptations.
- Reviewed revision: `27d842b3e6239bf60565f93c958d3f2cad395037` plus the exact temporary helper bytes listed below.
- Scope: final-preservation and additive ignored local archive adapters compared with round106. The separately assigned round107 queue/cleanup audit and actual publication execution are excluded.
- Verdict: **pass with limitations**. No supported retained defect was found.

## Evidence checked

- `/private/tmp/cmm-round107-finalize.py` — SHA256 `848015e32a4d2740fcfaa7f01c167843c976f5e735b4a08d96fac856b968edc7`.
- `/private/tmp/cmm-round107-archive.py` — SHA256 `da7a1448e73a054780d362ed277791d37145e1f8240ce6838dd3ca04054b4f31`.
- `/private/tmp/cmm-round106-finalize.py` — SHA256 `8f941db82c79aae0a1bb4d287e3a323686035d715af9aae2f47b7abffe2c47de`.
- `/private/tmp/cmm-round106-archive.py` — SHA256 `5b4c933fdcc3108c2f58cab09026f151fff97e9829bc890e2e56b019efa3f126`.
- `/private/tmp/cmm-round107-publication-guards.py` — SHA256 `5a0e5474250ec0e8b70df1aca99d00f57fa8b8d5d688f85f354d46cd54818cf4`.
- `/private/tmp/cmm-round107-helper-config.json` — SHA256 `3cda11670608d704a9975908e6cad59528f973f27b310e4aa9f7cc129c8174d0`.
- `/private/tmp/cmm-round107-preservation-before.json` — SHA256 `480557f5665cc8dcd2dee5bf582b3d70febb3c5298977e3059b95e313a2bc90f`.
- `/private/tmp/cmm-round106-cleanup.py` — SHA256 `ba7ccf7c7779ca96c531809d5e930a19a3597971ec860e68665ca61d8affb840`.

Finalizer derives topic HEAD/TREE from this round commit receipt and validates its helper/config hashes and strict postmerge receipt through the unchanged guard contract before mutation.

Pinned baseline is 27d842b3e6239bf60565f93c958d3f2cad395037; original-main inventory hash 480557f5665cc8dcd2dee5bf582b3d70febb3c5298977e3059b95e313a2bc90f matches inspected inventory with 10971 nontracked entries, including hidden/ignored files and three symlinks.

Before main fast-forward, clean main/base, expected origin and remote main, exact merge parent/tree, preserved bytes/modes/symlink targets and new-tracked-path collisions are checked. git merge --ff-only --no-overwrite-ignore is retained; inventory and clean state are checked again afterward.

Annotated review-base tag object and peeled target are checked locally and remotely; no tag deletion is performed.

Archive requires absent nonsymlink destination within original-main root and ignored manifest location. mkdir and exclusive x/xb files reject existing paths; source and destination digests match, symlinks are excluded, and original inventory is rechecked after writing.

Updated archive prose names the seven agreed owners, issue424 and source follow-ups418–423. It is a future output template, not evidence that gates, merge, closure or archive have already occurred.

Branch deletion is delegated to separately reviewed round107 cleanup. Prior106 CAS semantics were read as context only; no claim is made about uninspected107 cleanup.

## Checks

Twelve inert extracted-function and static ordering checks passed. Exact bytes/modes/symlink fixtures were accepted; changed bytes, mode, symlink target and regular-file replacement were rejected. Archive copy accepted a fresh path and refused an existing destination and source symlink. The retained destination bytes were unchanged. Full mutation modules were never executed; no Git/GitHub operation was invoked. Probe receipts and implementation are linked in the JSON artifact.

## Findings by severity

Critical: 0; major: 0; minor: 0; advisory: 0. No correction was required.

## Unresolved questions and limits

Final measured config, commit receipt, HEAD/TREE/PR bindings and actual postmerge/hosted receipts remain future prerequisites.

Separate queue/cleanup107 review must establish its exact CAS and issue-state bindings.

Static/inert helper review does not certify publication execution or hosted checks.

No review of new concurrent code changes after the captured input hashes.

No complete mutation helper was imported or executed.
