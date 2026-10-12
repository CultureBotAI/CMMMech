# Round 59 scientific review and publication report

Add four distinct material owners: rhodochrosite, spent nickel-cadmium batteries, pyrite-roasting cinder and tannery sludge. The corpus grows from 270 to 274 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round59-20261012`; branch: `curate/cmm-expansion-round59-20261012`; trusted base: `d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5`. Generated at 2026-10-12T14:14:57.639086+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [rhodochrosite](../../data/records/rhodochrosite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T141259Z-rhodochrosite-round59-science/review.md) / [YAML](../../reviews/structured/20261012T141259Z-rhodochrosite-round59-science/review.yaml) |
| [spent-nickel-cadmium-batteries](../../data/records/spent-nickel-cadmium-batteries.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T141140Z-spent-nickel-cadmium-batteries-round59-science/review.md) / [YAML](../../reviews/structured/20261012T141140Z-spent-nickel-cadmium-batteries-round59-science/review.yaml) |
| [pyrite-roasting-cinder](../../data/records/pyrite-roasting-cinder.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T141109Z-pyrite-roasting-cinder-round59-independent/review.md) / [YAML](../../reviews/structured/20261012T141109Z-pyrite-roasting-cinder-round59-independent/review.yaml) |
| [tannery-sludge](../../data/records/tannery-sludge.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T141105Z-tannery-sludge-round59-science/review.md) / [YAML](../../reviews/structured/20261012T141105Z-tannery-sludge-round59-science/review.yaml) |

All 4 independent final scientific reviews match the current record bytes. The [manifest](round59-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

Rhodochrosite formation is confined to defined synthetic-manganese-oxide experiments. The NiCd study retains comparable bacterial and abiotic extraction and conflicting culture/figure descriptions. Cinder evidence separates weakly controlled sulfur-solubilization observations from a thesis assay with no established leaching advantage. Tannery sludge evidence retains inoculum, reagent, sulfate and mass-balance inconsistencies; dissolved chromium is not an isolated recovery product.

## Findings and corrections

Four independent scientific reviews assess final record states with no corrective record findings. The separate publication review found a stale three-record count in the unposted closeout draft; it was changed to derive the count from the actual four-record configuration and independently rechecked. The initial finding and successor disposition are retained in the publication audit. A second publication finding corrected README navigation to link the round59 report and current frontier while retaining historical links; its initial finding and successor verification are also preserved. Review issues: [#183](https://github.com/CultureBotAI/CMMMech/issues/183), [#184](https://github.com/CultureBotAI/CMMMech/issues/184).

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. Source issue #181 tracks the complete Yao2022 tannery main; its official supplement was acquired but is not evidence without the main assessment. Issue #182 tracks complete Panda2017/2018 pyrite-ash originals and experiment-overlap checks. Both remain open. No existing source issue is closed by this batch. Acquisition issues remain open; see the [frontier](round59-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round58-postmerge-20261012-published-terminal.json`, SHA-256 `a09013a9be0470070bcccf806251353dda2e432326cf72e2e7cb73a95c078c6d`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `40fe42671fea94d48592eafa974ddb7f128b780c660493a3f9ab65af15d7f102`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `974da8ce5acdb657064309f2a5392e871dc7c31a17aba44605144b950cff04ed`.
- `uv run --locked cmmmech validate-history --base d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5`: exit 0; log SHA-256 `e34b8f84f2447bb164b1ddab2a65975c0671eee4d0549db8fac18bcc14c1b9dc`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5 --require-reviews`: exit 0; log SHA-256 `492a91817dc79d4e30a5cffe2ece49c98aa3ed6abc16f07c394c8584ea1d1469`.

Final `just check`: 317 passed, 3 skipped in 119.33 seconds. The gates accept 274 records, 322 histories and 332 review bundles. Exact-hash coverage verifies 274/274 current scientific reviews and 60 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round59/preservation-prepublication.json) verifies the original Documents checkout's 7,187 nontracked/ignored entries and the unrelated skill worktree's 7,389 tracked and nontracked/ignored entries, including file modes and symlink targets. Their Git states are unchanged from initialization. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round59/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
