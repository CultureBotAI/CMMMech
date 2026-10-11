# Round20 reviewed mineral and resource records

Worktree: `/private/tmp/CMMMech-expansion-round20-20261011`.
Branch: `curate/cmm-expansion-round20-20261011`.
Trusted base: `e98bdfaba62869faf5112ef281a9371d2a04d78e`.
Acceptance: [issue 74](https://github.com/CultureBotAI/CMMMech/issues/74).
Publication readability correction: [issue 75](https://github.com/CultureBotAI/CMMMech/issues/75).

Four additions bring the corpus to **149 records**: goethite as a mineral, nickel laterite ore and polymetallic nodules as primary resources, and boron-ore concentration tailings as a secondary resource. Each has narrowly supported microbial evidence, an actual CREATE sidecar and a distinct inline event. No constituent criticality, universal feed composition or industrial microbial deployment is inferred.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Boron-ore concentration tailings](../../data/records/boron-ore-concentration-tailings.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T122052Z-boron-ore-concentration-tailings-round20-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T122052Z-boron-ore-concentration-tailings-round20-independent/review.md) |
| [Goethite](../../data/records/goethite.yaml) | mineral | [YAML](../../reviews/structured/20261011T121929Z-goethite-round20-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T121929Z-goethite-round20-independent/review.md) |
| [Nickel laterite ore](../../data/records/nickel-laterite-ore.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T122141Z-nickel-laterite-ore-round20-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T122141Z-nickel-laterite-ore-round20-independent/review.md) |
| [Polymetallic nodules](../../data/records/polymetallic-nodules.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T121937Z-polymetallic-nodules-round20-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T121937Z-polymetallic-nodules-round20-independent/review.md) |

The publication audit identified compressed numeric prose in the report and PR draft. Issue 75 tracks spacing corrections, with scientific records and immutable reviews unchanged; independent verification precedes publication.

Every reviewer is independent of that record's author. The [manifest](round20-frontier-20261011.json) lists final hashes, history and review paths. No actionable blocker, major or minor scientific defect was identified; all four verdicts are pass_with_limitations. The limitations describe the accepted evidence boundary and are not erased by structural validation.

Goethite evidence distinguishes natural mineral feed from synthetic material with possible ferrihydrite, acid-confounded release and organism-dependent nulls. Laterite evidence retains matched-pH ore-dependent outcomes, inhibitory loading and unlike chemical comparators; whole-ore recovery is not goethite-specific flux. Nodules retain added citrate, absent matched sterile controls, divergent extraction accounting and five measured collections versus an unverified 25-cycle endpoint. Boron residue evidence preserves unresolved strain and study overlap, missing abiotic series, and quantitative/kinetic source discrepancies. All remain laboratory observations, not isolated industrial products.

## Sources and remaining work

The [prioritized frontier](round20-frontier-20261011.md) links paired source dossiers and timestamped discovery reports. It identifies concrete existing-record extensions and potential new resource identities. The mafic-tailings study remains deferred because deposit identity does not establish processing origin. Source text, tables, figures and access failures were checked independently of validator success. Raw full texts remain outside Git. No schema or validator change was necessary; no global exhaustion is claimed.

## Validation and preservation

Baseline: 308 tests passed, 3 skipped in 142.63 seconds; 145 records and 162 histories.
Final `just check`: **308 passed, 3 skipped in 80.63s (0:01:20)**.
All **149 records and 166 history sessions** validate. Separate `validate --require-records` and trusted-base `validate-history` passed. Structured review validation passed for **165 pairs**, and all 149 current records have independent scientific reviews matching their exact bytes.

All **926 prior tracked files** under data, history, reviews and research remain unchanged. All 21 distinct review bases resolve; the annotated source-survey provenance tag is unchanged, and the new reviews use the already merged trusted base. All 22 governed files match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`.

Live ruleset 24692449 remains active with SQUASH/ALLGREEN queue, required validate-strict from App 15368 and no bypass actors. Fleet admission and shared history are installed; PR shepherd remains manual/comment-only as documented. Future fleet changes must use CLAW's supported admission/synchronization process. This batch changes no governance or skills.

An independent publication audit and exact-tree squash-shaped checkout check precede queue admission. Required CI and actual merge state must be verified before deleting only the merged topic branch. A fresh remote-main checkout then revalidates the complete corpus/review history. Original main advances only after collision/symlink checks and unchanged ignored/untracked snapshots. Terminal publication evidence will be posted on the PR; unrelated worktrees and branches remain intact.
