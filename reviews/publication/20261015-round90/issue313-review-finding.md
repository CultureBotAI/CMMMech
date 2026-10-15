Independent static review found a missing direct-target guard in the temporary round90 publication audit. Matching an owner file as a review input does not alone establish that the owner was actually selected and scientifically reviewed. The existing coverage helper checks target scope, but the final selected review should be checked directly too.

Require the selected review to contain the exact record ID/path in `targets` and the ID in `scope.reviewed_target_ids`, alongside the existing positive scientific verdict and matching final file hash. Exercise rejection of input-only context, wrong-ID, wrong-path and unreviewed-target cases. Retain the initial observation, corrected helper and independent disposition in round90 publication evidence.

The reviewer also recommended retaining the exact required check-run and underlying GitHub Actions run/job identity in the hosted audit receipt. Verify the expected head, pull-request event, workflow path and successful required job before queue admission.

These are publication assurance changes; no current record's scientific assessment is alleged defective. Original helper SHA-256: `ea40dd67811f3275e3b11f0b533227f8d3bbfddc77b3ceaec635e1bc4723e5ba`. Independent observation: `cmm-round90-publication-static-20261015T073007Z`, S1 (target scope), with S2 (CI provenance) as an informational improvement.

Combined initial finding: `CMMMech.round90.publication-review-target-ci-binding`, OP1, saved in `cmm-round90-publication-static-expanded-20261015T073056Z` before correction.
