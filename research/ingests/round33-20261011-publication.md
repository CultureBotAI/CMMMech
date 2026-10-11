# Round33 curation and publication review

Worktree `/private/tmp/CMMMech-expansion-round33-20261011`; branch `curate/cmm-expansion-round33-20261011`; trusted base `bee4f42bb622ae0a0999f8f3e3dac31f14282278`.

Three new mineral records and one evidence extension bring the corpus to 190 records. Pyrite contributes methanogen-associated growth and separate reduction assays, chalcocite contributes qualified culture-associated leaching observations, and covellite contributes phase formation using biogenic sulfide. Molybdenite gains a separate concentrate comparison whose accounting cannot establish extraction. Distinct identities, assay substrates and laboratory limits are retained. No constituent's criticality, unsupported product yield or industrial deployment is inherited.

| Changed record | Accepted scope and retained limitations | Source assessment |
| --- | --- | --- |
| [Pyrite](../../data/records/pyrite.yaml) | Natural-specimen growth and separate synthesized-phase assays; accessibility does not identify electron-transfer mechanism, and source strain, medium and workbook discrepancies remain explicit. | [Dossier](../sources/round33-pyrite/20261011T203016Z-source-investigation.md) |
| [Chalcocite](../../data/records/chalcocite.yaml) | Mineral-separate and mixed-mineral observations; inconsistent extraction equation, feed composition and imperfect controls preclude a verified normalized yield. | [Dossier](../sources/round33-chalcocite/20261011T203153Z-source-investigation.md) |
| [Covellite](../../data/records/covellite.yaml) | Sulfide produced by an unresolved community drives separate chemical precipitation; impossible composition values cannot establish purity, and no complete copper balance is reported. | [Dossier](../sources/round33-covellite/20261011T203337Z-source-investigation.md) |
| [Molybdenite](../../data/records/molybdenite.yaml) | New concentrate context preserves residue-versus-solution ambiguity and missing controls; black-shale extraction values are not transferred. Earlier 2007 evidence is unchanged. | [Dossier](../sources/round33-molybdenite/20261011T203346Z-source-investigation.md) |

Independent reviewers assessed the original methods, figures, tables and relevant supplements. The [initial pyrite review](../../reviews/structured/20261011T203700Z-pyrite-round33-initial/review.md) identified minor F1, tracked in [issue #115](https://github.com/CultureBotAI/CMMMech/issues/115): Data Set 1 cells labelled unamended methane reference the adjacent pyrite standard-deviation column, conflicting with the near-zero plotted control. The [correction](../sources/round33-pyrite/20261011T203807Z-workbook-correction.md) retains this source discrepancy explicitly without silently repairing data or weakening separate observations. The original review and CREATE history remain immutable; a new EDIT documents the correction.

All four final scientific reviews are `pass_with_limitations` and match the final record hashes. The pyrite successor resolves the exact initial F1 occurrence; no unresolved corrective finding remains for these targets.

| Record | Final scientific review |
| --- | --- |
| [pyrite](../../data/records/pyrite.yaml) | [YAML](../../reviews/structured/20261011T204047Z-pyrite-round33-resolution/review.yaml) · [Markdown](../../reviews/structured/20261011T204047Z-pyrite-round33-resolution/review.md) |
| [chalcocite](../../data/records/chalcocite.yaml) | [YAML](../../reviews/structured/20261011T203735Z-chalcocite-round33-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T203735Z-chalcocite-round33-independent/review.md) |
| [covellite](../../data/records/covellite.yaml) | [YAML](../../reviews/structured/20261011T203656Z-covellite-round33-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T203656Z-covellite-round33-independent/review.md) |
| [molybdenite](../../data/records/molybdenite.yaml) | [YAML](../../reviews/structured/20261011T204052Z-molybdenite-round33-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T204052Z-molybdenite-round33-independent/review.md) |

Corrected-state `just check` completed: 308 passed, 3 skipped in 116.48s. Nonempty validation passed 190 records; trusted-base history passed 220 histories. The canonical review checker passed 224 bundles. Exact current scientific review coverage is 190/190, and all 34 review bases are available. The prior pre-correction receipts remain immutable. The unchanged chalcocite and covellite reviews accurately cite that earlier successful batch; the final corrected-state gates cover all current record bytes.

The starting baseline reused successful fresh-main checks at the identical trusted base and tree, recorded in `/private/tmp/cmm-round33-baseline-reuse.json`; this was not a new baseline execution. Offline validation cannot establish scientific truth. No schema, validator or test behavior changed: the existing evidence model accommodates the qualified observations.

The [frontier](round33-frontier-20261011.md) separates accessible originals from acquisition gaps and unresolved source accounting. The [manifest](round33-frontier-20261011.json) pins final records, histories, reviews, dossiers and completed gate receipts.

## Publication and preservation

This report records prepublication evidence. Commit, isolated squash-shaped verification, hosted CI, native queue merge, owned-branch deletion and fresh-main validation are later steps until actual runtime receipts exist. The independent [publication audit](../../reviews/publication/20261011-round33/) assesses readiness. Existing scientific content outside the molybdenite extension and unrelated original-checkout work must remain intact. Preservation inventory includes hidden and ignored main files and the unrelated skill worktree. Only the owned topic branch may be deleted after verified merge; the owned worktree is retained detached.

All 1,357 previously tracked record/history/research/review files outside the intentionally extended molybdenite target remain byte-identical. Every original molybdenite field value and list prefix is preserved; additions are limited to its new source, three context-only explanations and history. Hidden/ignored-inclusive catalogue enumeration verifies exactly 190 README record links for 190 records without duplicates. The preservation baseline includes 7,187 nontracked hidden/ignored main entries and eight bounded unrelated skill-work entries; their final comparison follows publication.

Live checks on 2026-10-11 verified [CLAW admission PR581](https://github.com/CultureBotAI/culturebotai-claw/pull/581) merged and [convergence issue580](https://github.com/CultureBotAI/culturebotai-claw/issues/580) closed. All 22 governed artifacts match immutable CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Shared history is installed. The PR shepherd remains manual and comment-only. Native ruleset24692449 is active, has no bypass actors, requires `validate-strict` from App15368, and uses SQUASH/ALLGREEN queue policy. Future integration changes must use CLAW's supported admission and synchronization process; no governance capability changes are included here.

New review base `bee4f42` is durable main history. The existing annotated `review-base/cmm-source-survey-20261009` tag preserves an older otherwise-unreachable review base. Verify every base and the exact tag object/target in fresh main-only clones before and after publication. Runtime PR/queue/merge/cleanup receipts will record actual outcomes separately.

Source-access follow-ups [#103](https://github.com/CultureBotAI/CMMMech/issues/103) and [#104](https://github.com/CultureBotAI/CMMMech/issues/104) remain open scientific work. The broader discovery objective is not exhausted.
