# Round 45 scientific review and publication report

Add argyrodite, briartite and Theisen sludge; extend coal-beneficiation-waste with qualified 2018 primary evidence. The corpus grows from 221 to 224 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round45-20261012`; branch: `curate/cmm-expansion-round45-20261012`; trusted base: `2b975ae5327b94ac3c1e6583378408add2b8d1f2`. Generated at 2026-10-12T04:18:12.392690+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [argyrodite](../../data/records/argyrodite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T041446Z-argyrodite-round45-evidence-resolution/review.md) / [YAML](../../reviews/structured/20261012T041446Z-argyrodite-round45-evidence-resolution/review.yaml) |
| [briartite](../../data/records/briartite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T040624Z-briartite-round45-independent/review.md) / [YAML](../../reviews/structured/20261012T040624Z-briartite-round45-independent/review.yaml) |
| [coal-beneficiation-waste](../../data/records/coal-beneficiation-waste.yaml) | EDIT | pass_with_limitations | [Markdown](../../reviews/structured/20261012T040413Z-coal-beneficiation-waste-round45-independent/review.md) / [YAML](../../reviews/structured/20261012T040413Z-coal-beneficiation-waste-round45-independent/review.yaml) |
| [theisen-sludge](../../data/records/theisen-sludge.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T040404Z-theisen-sludge-round45-independent/review.md) / [YAML](../../reviews/structured/20261012T040404Z-theisen-sludge-round45-independent/review.yaml) |

All 4 independent final scientific reviews match the current record bytes. The [manifest](round45-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Argyrodite and briartite are mineral identity records grounded in dated IMA authority and original natural-specimen evidence. Historical alburnite and zincobriartite boundaries remain explicit. Theisen sludge is a processing-derived resource with sampled-feed context; its synthetic membrane experiments and reused bioleaching information do not establish a new microbial mechanism. The coal extension preserves overlapping studies, recipe conflicts, control limits and unresolved volume accounting.

## Findings and corrections

Four independent final scientific reviews cover the current records. A minor argyrodite source-locator error and a subsequent review checksum-reference mismatch were corrected with preserved observations and explicit successor dispositions; issues #146 and #147 track those fixes. Review issues: [#146](https://github.com/CultureBotAI/CMMMech/issues/146), [#147](https://github.com/CultureBotAI/CMMMech/issues/147).

The review-metadata finding retains its [initial publication observation](../../reviews/publication/20261012-round45/20261012T041301Z-independent-initial.md) and [independent resolved disposition](../../reviews/publication/20261012-round45/20261012T041600Z-independent-resolution.md). The earlier saved review remains immutable; the manifest explicitly selects its corrected successor.

- `CMMMech.argyrodite.handbook-synthetic-reference`: resolved in the final review, retaining [the preceding observation](../../reviews/structured/20261012T041053Z-argyrodite-round45-resolution/review.md) and exact predecessor `F1`.

Scientific source limitations remain documented. Existing acquisition issues remain open; see the [frontier](round45-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round44-postmerge-20261012-published-terminal.json`, SHA-256 `ef5d65fabe991cfed703282af91e5865a91ec99403cf3ddfde54cb9134f1a036`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `5e6d87f0e99f5ff1f24fe8e6cfbe98a38442b4787add02cbf0c5d0f0b5aa1c1d`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `422762d06cd992924323952fee0ca1e7d56c09a13fca4fc98a425f8f8f911adc`.
- `uv run --locked cmmmech validate-history --base 2b975ae5327b94ac3c1e6583378408add2b8d1f2`: exit 0; log SHA-256 `2b2ddc7d5293ef78a29c990b065cb8b4d1cae9a128977c0c3aaf7fa0053d1e32`.
- `just review-check --base 2b975ae5327b94ac3c1e6583378408add2b8d1f2 --require-reviews`: exit 0; log SHA-256 `5a69e96e57a829974ce056d73b92ae33c61936458a0ad8cdce8fda6212b3f644`.

Final `just check`: 308 passed, 3 skipped in 208.23 seconds. The gates accept 224 records, 267 histories and 272 review bundles. Exact-hash coverage verifies 224/224 current scientific reviews and 46 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round45/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round45/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and four active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
