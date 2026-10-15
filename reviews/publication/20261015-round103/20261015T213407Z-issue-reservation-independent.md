# Independent issue-receipt guard review

- UTC timestamp: 2026-10-15T21:34:07.426547+00:00
- Reviewer: Codex, GPT-6, `/root/round100_vanadium`, independent of the helper author.
- Reviewed base: `44d5b468519eb862b32ef54bf7c066bc0f79ba62`; temporary helper working changes only.
- Issue: #391; predecessor: `reviews/publication/20261015-round103/20261015T212926Z-preparation-initial.json`.
- Helper: `/private/tmp/cmm-round103-create-issues.py`; SHA-256 `55a838aead9338efd18e5bc8ad933aaecf4d5503d91579e92a6e1c3748320a99`.

## Scope and evidence

I inspected the complete corrected helper and independently executed its exact bytes only through the temporary-path, subprocess-mocked regression. Eight cases passed: normal success, occupied regular receipt, existing and dangling symlinks, racing creator, successful-run replay, partial creation failure and post-creation verification failure. The original real #385–390 receipt remains byte-identical (`ffc84e4e262426139f495b574581e9432ae865ded02f47645e5e2ac169b97564`).

Exclusive aggregate reservation precedes remote mutations. Persisted progress retains known created issues and failed verification responses. The successful receipt retains the established list shape.

Test: `/private/tmp/cmm-round103-ree-review/test-issue-reservation.py` (`da2e490b7bf9aa2b55992364cd062d80e88c98eed2e5987f4de32ab468460179`). Independent terminal receipt: `/private/tmp/cmm-round103-helper-audit/independent-issue-reservation-regression.json` (`28ff8d000002d2ddb6fd685ac355fefa7a531aad2b52025fb7313c4b3f8ea7cf`). An initial system-Python 3.9 attempt failed inside the test's pathlib mock (`_flavour`) before subprocess calls; rerunning with the supported standalone interpreter passed all eight cases.

## Findings by severity and corrections

No new supported finding. The predecessor's major replay defect is resolved for the reviewed bytes. Separate push/archive guards are assessed by another reviewer; they are outside this verdict.

## Unresolved questions and limits

Remote creation and receipt writing are not one atomic transaction. A transport interruption after creation can require read-only reconciliation against retained progress. These mocked cases do not certify live GitHub availability or every filesystem failure. Final concrete bindings and lifecycle gates remain technical checks; existing user authorization is unchanged. No real Git/GitHub mutation or scientific self-acceptance occurred.

## Verdict

**Pass with limitations** for the exact corrected create-issues helper and the receipt-reservation finding in #391.
