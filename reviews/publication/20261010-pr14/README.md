# PR 14 publication review and fixes

Audit UTC: 2026-10-10T01:23:29.236483Z. Trusted remote base: `193a5ab81cd66de55cd00df4405128c0a14471c9`.
Reviewed source revision: `c0adc2c0763e1515ed07dc712b024974d98fb342`. These publication artifacts and new reviews
are working additions against that source revision; no record bytes changed in
this publication round. Earlier research reports retain their historical state.

[PR #14](https://github.com/CultureBotAI/CMMMech/pull/14) publishes the ten-record
source-led corpus, nine mechanisms, thirteen dated criticality entries and eight
concentration observations. All records have new independent scientific reviews,
with scope exclusions and source limitations explicit. Two mineral identities
pass; eight other records pass with limitations. No new scientific correction
was required.

| Record | Verdict | Fresh structured review |
|---|---|---|
| cmmmech:cobalt | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011841Z-cobalt-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011841Z-cobalt-pr-science/review.md) |
| cmmmech:cobaltite | pass | [YAML](../../../reviews/structured/20261010T011911Z-cobaltite-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011911Z-cobaltite-pr-science/review.md) |
| cmmmech:fluorescent-lamp-phosphor | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011906Z-fluorescent-lamp-phosphor-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011906Z-fluorescent-lamp-phosphor-pr-science/review.md) |
| cmmmech:lithium | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011959Z-lithium-pr-adversarial/review.yaml) / [Markdown](../../../reviews/structured/20261010T011959Z-lithium-pr-adversarial/review.md) |
| cmmmech:manganese | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011858Z-manganese-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011858Z-manganese-pr-science/review.md) |
| cmmmech:monazite-nd | pass | [YAML](../../../reviews/structured/20261010T011916Z-monazite-nd-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011916Z-monazite-nd-pr-science/review.md) |
| cmmmech:neodymium | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011852Z-neodymium-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011852Z-neodymium-pr-science/review.md) |
| cmmmech:palladium | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011847Z-palladium-pr-science/review.yaml) / [Markdown](../../../reviews/structured/20261010T011847Z-palladium-pr-science/review.md) |
| cmmmech:uranium | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011959Z-uranium-pr-adversarial/review.yaml) / [Markdown](../../../reviews/structured/20261010T011959Z-uranium-pr-adversarial/review.md) |
| cmmmech:vanadium | pass_with_limitations | [YAML](../../../reviews/structured/20261010T011959Z-vanadium-pr-adversarial/review.yaml) / [Markdown](../../../reviews/structured/20261010T011959Z-vanadium-pr-adversarial/review.md) |

The [initial implementation review](../../../reviews/structured/20261010T011848Z-publication-code-review/review.md)
found two publication defects. [Issue #15](https://github.com/CultureBotAI/CMMMech/issues/15)
is addressed by the ten fresh bundles and current/historical README navigation.
[Issue #17](https://github.com/CultureBotAI/CMMMech/issues/17) is addressed by a
durable annotated provenance tag and the native publication instructions.
The [successor review](../../../reviews/structured/20261010T012303Z-publication-finding-resolution/review.md)
([YAML](../../../reviews/structured/20261010T012303Z-publication-finding-resolution/review.yaml)) explicitly resolves both finding
keys and cites their previous occurrences. The original needs-curation observation
is preserved rather than overwritten.

## Retained source provenance

The published tag `review-base/cmm-source-survey-20261009` has tag object
`fc4040c3abcd28f0a9cc52467e308100144ad1fd` and peels to `c0adc2c0763e1515ed07dc712b024974d98fb342`.
All twelve review bundles use this one inspected base. The tag is an evidence
reference, not a release. Keep it after deleting the topic branch; consumers
must fetch tags explicitly when using shallow or single-branch clones.

The independent [before probe](provenance-before.json) reproduced unavailable
provenance after a synthetic squash. The [retention probe](provenance-retained.json)
fetched the exact tag from GitHub and restored verification without a topic
branch. The [coverage/portability check](review-coverage-and-portability.json)
validated the then-present eleven bundles in that isolated repository. The final
successor and all twelve bundles are checked separately. No governed validator,
schema, workflow or pin was hand-edited to weaken the provenance requirement.

## Checks and publication follow-through

The [validation and hash manifest](validation.json) records ten exact scientific
record hashes, both issue dispositions, retained history/review/research paths,
and actual pre-merge gates. `just check`: 294 passed, 3 existing skips; ten valid
records and nineteen valid histories. Required-record validation, structured
review validation and canonical equality of all 22 governed artifacts pass.
The three numerical edge-case fixes were already in the reviewed implementation;
this publication round changes review/navigation/provenance artifacts only.

Queue admission, the final head/merge-group CI, actual squash merge, branch
deletion and fresh GitHub checkout validation occur after this committed report.
Their actual evidence will be posted on PR #14. This report does not claim those
future operations have already succeeded. Unrelated PR #16 and other sessions'
worktrees are outside this publication task and remain untouched.

Remote main advanced to `d3f608aaf75f621a27352e03ed90584588765bf1` during this
review when the separate governance PR merged. Its tree is byte-identical to
the tested `193a5ab` base; the refresh changed no reviewed input. Final queue
validation still uses GitHub's current base.
