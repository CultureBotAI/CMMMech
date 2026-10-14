# Round 64: conditional iron reduction and manganese transformation

UTC: 2026-10-14T06:54:09.889711+00:00. Worktree `/private/tmp/CMMMech-expansion-round64-20261014`, branch `curate/cmm-expansion-round64-20261014`, trusted base `0f4d8ff9e4919714e3dd902dc3573e95922a65fb`.

## Accepted records

Five mineral records bring the corpus from 288 to **293**. These candidates had inspectable originals and distinct mineral identities. Element, mineral species, commodity and process-defined waste remain separate. No criticality designation is inherited from a constituent, and no laboratory assay is presented as industrial deployment. The pilots required no schema or validator changes.

- **Akaganeite:** PCA and deletion-mutant reduction in synthetic XRD-assigned feed. pH and autoclaving alter phenotypes; mineral potential is inferred and acid-extractable Fe(II) is not a dissolved-only fraction.
- **Lepidocrocite:** CN32 formate-fed reduction and source-assigned green-rust formation. The printed collection accession conflicts with the authority entry; fractions, controls and unresolved donor/salt matching remain explicit.
- **Feroxyhyte:** conditional CN32 reduction and product phases with AQDS/phosphate arms. Partial Fe reduction, unlike 78/156-day endpoints and the source's conflicting figure caption remain unresolved.
- **Manganite:** synthetic MnOOH reduction by MR-4. Acidic sterile controls can exceed biotic dissolved Mn; source temperature/replication discrepancies and inferred dissolved oxidation state are preserved.
- **Bixbyite-(Mn):** tentative bixbyite-like phase formation by T-G1. Long culture incubation differs from short oxidation assays; neutral-pH oxidation without particles, missing matched long-term controls and recipe conflicts prevent stronger attribution.

| Record | Final independent scientific review | History sessions |
|---|---|---|
| [akaganeite](../../data/records/akaganeite.yaml) | [review](../../reviews/structured/20261014T064301Z-akaganeite-round64-independent/review.md) | 1 |
| [lepidocrocite](../../data/records/lepidocrocite.yaml) | [review](../../reviews/structured/20261014T064938Z-lepidocrocite-round64-successor/review.md) | 2 |
| [feroxyhyte](../../data/records/feroxyhyte.yaml) | [review](../../reviews/structured/20261014T064248Z-feroxyhyte-round64-independent/review.md) | 1 |
| [manganite](../../data/records/manganite.yaml) | [review](../../reviews/structured/20261014T064301Z-manganite-round64-independent/review.md) | 1 |
| [bixbyite-mn](../../data/records/bixbyite-mn.yaml) | [review](../../reviews/structured/20261014T064301Z-bixbyite-mn-round64-independent/review.md) | 1 |

All final scientific reviews were authored by an agent other than the record curator and cover exact current record hashes. The machine manifest pins records, histories, reviews and dossiers. Quantitative denominators and analytical fractions remain study-specific; solution release or phase assignment is not an isolated-product recovery yield.

## Adversarial correction

Review [#203](https://github.com/CultureBotAI/CMMMech/issues/203) identified a missing control detail in lepidocrocite: original Figure 1 visibly includes a near-baseline sterile-control curve. The record now retains that comparator while explicitly preserving the unknown donor/salt match to the focused formate treatments. No endpoint was invented. The initial `needs_curation` observation remains immutable at `reviews/structured/20261014T063915Z-lepidocrocite-round64-independent/`; the final review links its resolved finding and issue. An appended EDIT session preserves correction history. This local report does not preclaim issue closure; the fixing PR will close it on merge.

## Source investigation and next work

Source dossiers: [round64-iron](../sources/round64-iron/20261014T062830Z-source-investigation.md), [round64-manganese](../sources/round64-manganese/20261014T062554Z-manganite-source-investigation.md), [round64-manganese](../sources/round64-manganese/20261014T063052Z-bixbyite-mn-source-investigation.md), [round64-feroxyhyte](../sources/round64-feroxyhyte/20261014T063035Z-source-investigation.md), [round64-lithium](../sources/round64-lithium/20261014T062345Z-source-investigation.md). They retain exact searches, raw-source hashes, authoritative identity checks, original figures/tables and limitations. Copyrighted originals remain outside Git. Searches used to establish local absence included hidden and ignored files and relevant symlinks within explicitly named roots.

The lithium investigation remains a source handoff, with no accepted new lithium record. [#202](https://github.com/CultureBotAI/CMMMech/issues/202) tracks acquisition of the full Kordloo 2025 waste-aluminum-electrolyte article and supplements. Publisher metadata/abstract access cannot establish feed provenance, controls or recovery denominators. Iqbal's 2015 thesis still needs a complete accessible original before any distinct lepidolite-waste claim; a title or specimen caption cannot establish assay feed identity.

Next priorities include full assessment of the acquired Fredrickson 2002 manganese original, acquisition of the ACS 2022 ligand-assisted manganese study, complete lithium source acquisition, and the existing magnesium-carbonate/nickel-waste follow-ups from [round63](round63-frontier-20261014.md). The complete 126-issue inventory was inspected before this batch created its two issues. These bounded searches do not establish source exhaustion.

## Checks and integration

Baseline and both batch runs passed **317 tests, 3 skipped**. Lepidocrocite was corrected during the first batch run, so the complete gate was repeated after freezing corrected bytes and regenerating pages. Final explicit nonempty validation passed **293 records**, trusted-base history passed **343 sessions**, structured review checking passed **354 bundles**, and exact current scientific coverage is **293/293** across **65 available review bases**. Structural checks do not establish scientific truth.

Preservation receipts compare hidden/ignored-inclusive bytes, modes, symlink targets and Git states: 7,187 original-main nontracked entries and 7,389 unrelated-skill tracked/nontracked entries. Git administrative bytes and external symlink contents are excluded. All 22 governed artifacts match the immutable CLAW pin. Admission PR581 is merged, convergence issue580 and CMMMech issue3 are closed, and the native SQUASH/ALLGREEN merge queue is active without bypass actors. PR shepherd remains dispatch-only/comment-only; future integration must use CLAW's supported process.

This report records local completion. Independent operational review, exact-commit hosted checks, squash-shaped provenance verification, native queue admission, branch deletion and fresh remote-main verification remain separate publication gates.
