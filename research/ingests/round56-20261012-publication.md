# Round 56 scientific review and publication report

Add three material owners: chalcopyrite-enargite concentrate, nickeline-bearing ore and zirconolite. The corpus grows from 261 to 264 records. These changes preserve material identity, source inconsistencies and laboratory limits; no criticality designation or industrial deployment is inferred from a constituent or source rhetoric.

Worktree: `/private/tmp/CMMMech-expansion-round56-20261012`; branch: `curate/cmm-expansion-round56-20261012`; trusted base: `934bb36319e857321840c0ae145664ca6910c382`. Generated at 2026-10-12T11:57:48.523500+00:00.

## Scientific review

| Record | Action | Verdict | Artifacts |
|---|---|---|---|
| [chalcopyrite-enargite-concentrate](../../data/records/chalcopyrite-enargite-concentrate.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T115435Z-chalcopyrite-enargite-concentrate-round56-science/review.md) / [YAML](../../reviews/structured/20261012T115435Z-chalcopyrite-enargite-concentrate-round56-science/review.yaml) |
| [nickeline-bearing-ore](../../data/records/nickeline-bearing-ore.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T115400Z-nickeline-bearing-ore-round56-independent/review.md) / [YAML](../../reviews/structured/20261012T115400Z-nickeline-bearing-ore-round56-independent/review.yaml) |
| [zirconolite](../../data/records/zirconolite.yaml) | CREATE | pass_with_limitations | [Markdown](../../reviews/structured/20261012T115449Z-zirconolite-round56-science/review.md) / [YAML](../../reviews/structured/20261012T115449Z-zirconolite-round56-science/review.yaml) |

All 3 independent final scientific reviews match the current record bytes. The [manifest](round56-frontier-20261012.json) retains exact record, history, review and dossier hashes. Canonical history sessions and inline curation events describe actual changes; prior histories and reviews remain immutable.

The mixed copper concentrate retains distinct feed arms, nonsterilized no-added-cell controls and theoretical versus measured copper contributions. Nickeline-bearing ore separates natural feed grades and mixed-culture assays from ferric-only experiments, retaining control and source inconsistencies. Zirconolite is an identity-only mineral record grounded in the current issuing list, nomenclature and an unheated natural metamict specimen; no polytype, criticality or microbial mechanism is inferred.

## Findings and corrections

Independent scientific reviews of the three final record states found no corrective record defect. Review issue #172 tracks a corrected zirconolite dossier validation-command typo: the original is retained, a fresh actual CLI receipt supersedes the mistaken command, and the final independent review includes both. Scientific source inconsistencies and limitations remain explicit. Publication review issue #173 corrects README navigation to the round56 report and current frontier, retaining the prior report link and the saved initial finding. Review issues: [#172](https://github.com/CultureBotAI/CMMMech/issues/172), [#173](https://github.com/CultureBotAI/CMMMech/issues/173).

No unresolved corrective finding remains in the final scientific reviews.

Scientific source limitations remain documented. The complete official Oyama2025 supplement was acquired and inspected, but its main is unavailable and its kinetic-fit caption conflicts with displayed statistics. Source issue #171 tracks the gap and reconciliation. A complete 2026 enargite primary original and XML were newly acquired for subsequent full assessment, not imported into records. No existing source issue is closed by this batch. Acquisition issues remain open; see the [frontier](round56-frontier-20261012.md). No source exhaustion is claimed.

## Validation and preservation

The baseline reuses the freshly completed published-base checks at the exact unchanged commit/tree: `/private/tmp/cmm-round55-postmerge-20261012-published-terminal.json`, SHA-256 `4032b80290185e92fb36b0d1379b359911297dccabb5c67da545811b4efff351`. It was not redundantly rerun before curation.

- `just check`: exit 0; log SHA-256 `6b01c5d11d5c079d67ed60e5ceb352b4cf707467ca43be19d2e6f55e336aec4e`.
- `uv run --locked cmmmech validate --require-records`: exit 0; log SHA-256 `b71f33e5942dcb1e7200178792ad93d0e537a0132030be50e91a20a7420f50d9`.
- `uv run --locked cmmmech validate-history --base 934bb36319e857321840c0ae145664ca6910c382`: exit 0; log SHA-256 `4430a4d8296252884291d0f0bc2783aee79f4fc5616262d646e4b1357926aba1`.
- `just render-check`: exit 0; log SHA-256 `be156b3acc20d39b6bad41632b10eb7ccfc2c8a7fdeaec3f6236fbc67831aea6`.
- `just review-check --base 934bb36319e857321840c0ae145664ca6910c382 --require-reviews`: exit 0; log SHA-256 `c3ab74123fa63ade2e9459e91932fe18b46e8329fc78e6b81113034655f02293`.

Final `just check`: 317 passed, 3 skipped in 170.05 seconds. The gates accept 264 records, 312 histories and 322 review bundles. Exact-hash coverage verifies 264/264 current scientific reviews and 57 available review bases. Offline validity does not itself establish scientific truth.

The [preservation receipt](../../reviews/publication/20261012-round56/preservation-prepublication.json) verifies 7,187 hidden/ignored nontracked main-checkout entries and eight bounded unrelated skill-worktree entries plus Git state. Raw originals remain outside Git. No schema, validator, tests, skills or governed artifacts changed in this batch.

## Integration and publication

The [live status](../../reviews/publication/20261012-round56/current-status.json) confirms merged CLAW admission, the immutable governance pin, shared history/review support and active workflows. Main uses the native SQUASH/ALLGREEN queue with required validation and no bypass actors. Workflow presence does not verify credentials or fleet-wide convergence. Future integration uses CLAW's supported admission and synchronization process.

Commit, isolated squash-shaped validation, hosted review and CI, queue merge, owned-branch deletion and fresh-main validation follow this report. This artifact does not claim those later operations have occurred; the PR closeout records actual publication results. All review bases must remain available after branch deletion.
