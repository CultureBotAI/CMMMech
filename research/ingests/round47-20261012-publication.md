# Round 47 scientific review and publication report

Add dzhalindite as a distinct mineral owner and cassiterite-polymetallic-sulfide ore as a primary resource with qualified microbial pretreatment evidence. The corpus grows from 229 to 231 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round47-20261012`; branch: `curate/cmm-expansion-round47-20261012`; trusted base: `18c9f3dd5005e14142b8a0b7e13bb84870e1731a`. Generated at 2026-10-12T05:34:52.075405+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [dzhalindite](../../data/records/dzhalindite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T053054Z-dzhalindite-round47-independent/review.md) / [YAML](../../reviews/structured/20261012T053054Z-dzhalindite-round47-independent/review.yaml) |
| [cassiterite-polymetallic-sulfide-ore](../../data/records/cassiterite-polymetallic-sulfide-ore.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T053057Z-cassiterite-polymetallic-sulfide-ore-round47-independent/review.md) / [YAML](../../reviews/structured/20261012T053057Z-cassiterite-polymetallic-sulfide-ore-round47-independent/review.yaml) |

All 2 independent final scientific reviews match the current record bytes. The [manifest](round47-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Dzhalindite identity is grounded in dated IMA authority and a complete natural-occurrence study. The reported identification lacked successful X-ray diffraction; iron zoning, hypogene formation and inferred temperatures remain qualified. The mixed cassiterite ore is a geological primary resource, distinct from its mineral constituents and tin element. Its laboratory pretreatment record retains culture-specific comparisons, inconsistent phase/element composition tables and the limits of dissolved iron as a desulfurization proxy. No recovered-tin yield or industrial deployment is inferred. The deferred stannite and kësterite leads are research handoffs rather than accepted records.

## Findings and corrections

Two independent final scientific reviews cover the exact current record bytes. No unresolved corrective finding remains in their assessed scope.

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Existing acquisition issues remain open; see the [frontier](round47-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round46-postmerge-20261012-published-terminal.json`, SHA-256 `719766b970909effe526a68eb72cb459846f9d0a75becca721f643a7f63a178a`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `85ba85c6ae6c37eaf08de9cff32bf752bfd53530f8ee6653b90180e4098a30b5`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `6127dc337a4794cd0f1fb158f348c4a20223bc3098da0a4adb0b2d278ce742b4`.
- `uv run --locked cmmmech validate-history --base 18c9f3dd5005e14142b8a0b7e13bb84870e1731a`: exit 0; log SHA-256 `469f96953d0dcc57034205a455d1f0374b1537438c67118a89cdd87e14ff88de`.
- `just review-check --base 18c9f3dd5005e14142b8a0b7e13bb84870e1731a --require-reviews`: exit 0; log SHA-256 `389d59a8fedb03b5b5c3b6ba8882e6f442c450509e4beb61abbf9a06c16c400f`.

Final `just check`: 308 passed, 3 skipped in 243.86 seconds. The gates accept 231 records, 274 histories and 283 review bundles. Exact-hash coverage verifies 231/231 current scientific reviews and 48 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round47/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round47/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
