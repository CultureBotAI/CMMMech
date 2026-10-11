# Round25 reviewed secondary-resource additions

Worktree: `/private/tmp/CMMMech-expansion-round25-20261011`.
Branch: `curate/cmm-expansion-round25-20261011`.
Trusted base: `baedff25eafad1516270916a651af6754ffa5996`.
Acceptance: [issue 90](https://github.com/CultureBotAI/CMMMech/issues/90).

Five new records bring the corpus to **165 records**. Each describes a distinct secondary resource with source-qualified laboratory evidence. None inherits elemental criticality. Dissolution, acid production and filtered-liquid measurements are distinguished from isolated-product recovery and industrial deployment. No existing scientific record, schema, validator, skill or governed artifact was changed.

## Independent scientific reviews

| New record | Final exact-state review |
|---|---|
| [Blast-furnace cast-house dust](../../data/records/blast-furnace-cast-house-dust.yaml) | [YAML](../../reviews/structured/20261011T150320Z-blast-furnace-cast-house-dust-round25-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T150320Z-blast-furnace-cast-house-dust-round25-independent/review.md) |
| [Heavy-fuel-oil combustion ash](../../data/records/heavy-fuel-oil-combustion-ash.yaml) | [YAML](../../reviews/structured/20261011T150126Z-heavy-fuel-oil-combustion-ash-round25-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T150126Z-heavy-fuel-oil-combustion-ash-round25-independent/review.md) |
| [Discarded light-emitting-diode lamps](../../data/records/discarded-led-lamps.yaml) | [YAML](../../reviews/structured/20261011T150328Z-discarded-led-lamps-round25-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T150328Z-discarded-led-lamps-round25-independent/review.md) |
| [Biogas-desulfurization sulfur residue](../../data/records/biogas-desulfurization-sulfur-residue.yaml) | [YAML](../../reviews/structured/20261011T150333Z-biogas-desulfurization-sulfur-residue-round25-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T150333Z-biogas-desulfurization-sulfur-residue-round25-independent/review.md) |
| [Spent zinc-manganese button-cell batteries](../../data/records/spent-zinc-manganese-button-cell-batteries.yaml) | [YAML](../../reviews/structured/20261011T150309Z-spent-zinc-manganese-button-cell-batteries-round25-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T150309Z-spent-zinc-manganese-button-cell-batteries-round25-independent/review.md) |

All five records have actual CREATE sidecars, distinct inline events and independent scientific reviews matching their final hashes. The [manifest](round25-frontier-20261011.json) lists exact record/history/review paths. All five reviews use `pass_with_limitations`; no actionable defect in these frozen scientific records was identified. Source limitations remain visible and are not erased by passing validation. Independent publication review identified [issue 91](https://github.com/CultureBotAI/CMMMech/issues/91), a minor spacing defect in the frontier source dossier. Only whitespace in 19 descriptive prose values changed; exact queries, URLs, paths, identifiers, numerical content, records, histories and original reviews remained unchanged. The [LED successor](../../reviews/structured/20261011T150757Z-discarded-led-lamps-round25-context-readability/review.md) and [sulfur successor](../../reviews/structured/20261011T150800Z-biogas-desulfurization-sulfur-residue-round25-context-readability/review.md) capture the corrected context with `scientific_review: false`; literature was not reassessed.

## Evidence boundaries and next work

Cast-house dust is distinct from flue-gas dust and EAF dust. Its serial reactor cycles retain liquid and solids, limiting apparent fresh-charge extraction. The statistical supplement contains a duplicated day-7 Zn value inconsistent with a pooled table and figure. Unmatched abiotic controls and missing inventories prevent a complete process-yield interpretation.

Oil-combustion ash is deliberately broader than fly ash because the collection fraction is unknown. Its full primary experiment reports different V/Ni outcomes for spent media from different cultivation conditions. Missing liquid-metal assay details and matched leach controls remain explicit. The 1-L reactor concerns culture production, not a validated leach-scale or industrial operation.

Discarded LED lamps remain distinct from fluorescent phosphors, LCD panels and isolated semiconductor compounds. Reagent acid outperforms biogenic acid for Nd in the selected comparison. Source table/conclusion disagreements and unclear normalization remain unresolved; no unique enzyme/EPS pathway or isolated product is claimed.

Biogas-desulfurization residue is a sulfur-rich oxidation substrate. A paper-assigned DSM 1927 species conflicts with the collection catalogue, so the mixed culture is not silently repaired or assigned a false organism identifier. Sulfur accounting is incomplete, and subsequent battery leaching is a separate context.

Zn-Mn button cells retain inhibited treatments, unresolved PTCC stock identity, unlike solution histories, analytical labels and endpoint/improvement contradictions. The four-hour thermal step and biological treatment are distinct. No complete thermal/whole-battery mass balance, detoxification certificate or purified product is established.

The [next-ingest frontier](round25-frontier-20261011.md) includes EAF dust, pharmaceutical blister packaging, superalloy residues, pickling sludge, beverage cans, brake pads and silver-oxide cells, plus earlier unresolved extensions. These are leads with explicit acquisition limits. New identities and unassessed sources remain; global exhaustion is not established.

## Validation, provenance and preservation

Baseline `just check`: **308 passed, 3 skipped in 118.77 seconds**, with 160 records and 181 histories. Final `just check`: **308 passed, 3 skipped in 98.72 seconds**, with 165 records and 186 histories. Separate `validate --require-records` and trusted-base history validation passed with zero errors. Final `just review-check --base baedff25eafad1516270916a651af6754ffa5996 --require-reviews` completed with exit 0 and **190 valid review bundles**; its `declared_scopes_only` result is recorded separately from scientific coverage. Independent coverage inspection confirmed that all 165 current record hashes have completed positive scientific reviews; context-only successors do not substitute for that coverage.

All **1084 prior scientific files** under data/history/reviews/research are byte-identical to the trusted base. Current README membership is 165 unique record rows. The original checkout and unrelated dirty add-record-skill worktree are preserved; original ignored/untracked inventory contains 7,187 entries. The final publication receipt must recheck this preservation after any main advancement.

All new review bases are the already-merged trusted base. Existing annotated provenance tag `review-base/cmm-source-survey-20261009` still points to `c0adc2c0763e1515ed07dc712b024974d98fb342`, tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`. Published evidence tags remain intact.

The 22 governed artifacts match CLAW pin `a5d562962c75a2ad9efd8160b548df5944315422`. Live ruleset 24692449 remains active, SQUASH/ALLGREEN, required `validate-strict` from App 15368 and no bypass actors. Admission, shared history and governance are installed. The PR shepherd remains manual/comment-only; this batch did not invoke it. Future integration must use CLAW's supported admission and synchronization process.

Independent publication audit, exact-tree squash-shaped preflight, queue merge, branch deletion and fresh remote-main validation are pending at report preparation. Their terminal receipts belong on the PR. Main advancement requires a clean checkout and explicit path/symlink collision and ignored/untracked preservation checks.
