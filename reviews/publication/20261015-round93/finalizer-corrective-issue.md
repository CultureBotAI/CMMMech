Independent static review of the new round93 external finalizer found an operational receipt-binding gap (OP1; stable key `round93-finalize-hosted-receipt-binding`). Its initial assertions accepted a peer receipt for the wrong PR number and five arbitrary successful workflow-role entries. The hosted-five producer already verifies the actual API observations; this finding concerns the final report consumer, not an observed hosted failure or a scientific-record defect.

Before runtime, bind the peer to the actual PR and the hosted producer's input hashes to the current commit/config/queue/preflight/peer/comment receipts. Require the five specific workflow roles and reconcile their run/event/head/attempt/job identities with the retained raw producer responses. Keep the copy-plan prevalidation and original-main preservation guards.

Acceptance: independent negative cases must reject mismatched PR, input hashes and role/run/job identities while accepting a coherent fixture; preserve the initial observation, fixed helper and successor evidence. Actual postmerge finalization remains a later runtime gate. This is distinct from #326, which concerns posting the COMMENT before finalization.

Initial evidence: `cmm-round93-finalize-static-initial-20261015T105005Z.{json,md}` and the independently retained original helper snapshot. No finalization was executed before review.
