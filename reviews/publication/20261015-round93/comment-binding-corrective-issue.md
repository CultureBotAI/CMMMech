Independent publication review found a minor operational assurance gap in the round93 external `post-review.py` helper. Stable key: `CMMMech.round93.post-review-comment-binding`; observation OP1.

The helper verifies the accepted peer receipt and live PR, but its initial version reads a fixed COMMENT file without requiring that file's path and SHA-256 to equal the peer receipt's `comment_draft` binding. Changed comment bytes could therefore be posted without acceptance by that peer review. This is a posting-consumer gap, separate from #323's closeout/receipt-copy contract. No unreviewed comment was posted.

Acceptance: bind the exact COMMENT path and bytes to the accepted peer producer before request creation or POST; recheck before mutation; preserve that binding in the posted receipt. Independently exercise the valid case and mismatched path/hash/content cases without network mutations. Save the initial observation, corrected helper and verification disposition with the publication evidence. Do not change any scientific owner or governed artifact for this fix.

The initial helper and independent observation are preserved externally as `cmm-round93-comment-binding-initial-20261015T103919Z.{py,json,md}` and will be retained in the publication package. Initial helper SHA-256: `956284c23cfa64095d9466f88d42b396411227bb8a0dd31d2fa3e85a68fdb213`.
