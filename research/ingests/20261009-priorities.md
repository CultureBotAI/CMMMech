# Ingest priorities from the CMM source-discovery run

Execution opened 2026-10-09 UTC by Codex (GPT-6), on base
`905388523b6e9184783989484896e4cc20297832`, branch
`research/cmm-source-survey-20261008`, worktree
`/private/tmp/CMMMech-source-survey-20261008`.

Input: [source assessment](../sources/cmm-landscape/20261008T073140Z.md),
[search log](../sources/cmm-landscape/20261008T073140Z-search-log.md), and
[acquisition manifest](../sources/cmm-landscape/20261008T073140Z-evidence.json).
The discovery output is a starting point; only independently reviewed records
count as completed ingests. Historical source reports remain unchanged.

## Ranked queue

Priority reflects evidence fitness, added mechanism/material coverage, and
reuse effort. It is not a numerical assessment of process efficiency or a
comparison of incompatible assay yields. An ingest unit here is a reviewed
claim in a native record, not a bulk copy of a dataset.

| Rank | Discovery keys | Concrete ingest | Decision and acceptance condition | Execution status |
|---|---|---|---|---|
| 1 | M1 | Separate Gluconobacter bioleaching mechanism in neodymium | Accessible direct-assay methods and sampled workbook; preserve mixed synthetic substrate and mutant limitations | Completed: scoped Nd mechanism accepted |
| 2 | E1 | Element-scoped USGS bioelectrochemical observations, initially U and V | Reconcile sample identities, detection limits, unmatched controls and solids before selecting claims; no unsupported microbial effect size | Completed: U/V separation observations accepted with partial microbial attribution |
| 3 | M4 | Manganese element with laboratory oxidation mechanism | Mutant and abiotic controls; resolve GB-1 identity and preserve oxide-equivalent assay boundary | Completed: Mn transformation record accepted |
| 4 | A1 | Explicit US 2025 criticality in Co/Nd and eligible new element records | Complete official notice, commodity-to-element mapping; retain earlier jurisdictions/editions | Completed: dated Co/Nd/Li/Mn/U/V entries; existing Pd entry retained |
| 5 | I1 | Separate cobaltite and monazite-(Nd) mineral identities | Dated IMA species rows and dictionary; no inherited element criticality or mechanisms | Completed: two identity records accepted |
| 6 | M2 | Retorted fluorescent-lamp phosphor secondary-resource record | Total-REE bioleaching may be curated without an Nd-specific yield; preserve pretreatment and clarified biolixiviant | Completed: scoped secondary-resource record accepted |
| 7 | M3, I3 | Lithium element and conditional mineral-feed bioleaching | Preserve null results, culture-identity uncertainty and 1%/2% loading conflict; defer normalized yield | Completed: qualitative Li record accepted; quantitative comparisons deferred |
| 8 | D1 | MCS commodity statistics as future structured observations | Resolve units, estimate/missing-value codes, intervals, nonunique keys and dictionary mismatch before observation ingest | Deferred: native schema has no statistical observation contract |
| 9 | A2 | Additional EU designations | Acquire authentic complete annexes and amendment/version context; preserve existing historical Co entry | Deferred: fresh annex evidence unavailable in discovery |
| 10 | D2 | Cobalt occurrence/resource context from USMIN | Acquire original files, dictionary, stable feature/reference joins and release history; mirror metadata is insufficient | Deferred: zero occurrence rows acquired in discovery |
| 11 | I2 | Relevant mineral specimens and Raman data | Acquire relevant specimens and verify axes, identity confidence and redistribution terms | Deferred: sampled archive was only a format demonstration |

These rows cover all twelve discovery keys; I3 is an identity prerequisite for
M3 rather than a second extraction experiment. E1's As/Sb/Cr coverage does not
justify automatically creating five equivalent microbial-recovery records.
No bulk importer or schema expansion is necessary for qualitative scoped claims.

## Review and verification

Each materially changed record has an independent timestamped review below,
including final SHA-256, source locators, uncertainties and verdict. New canonical
history sessions describe actual present work; the three committed sessions
remain byte-identical. Cobalt and neodymium retain every prior source,
designation, mechanism and history event/reference. Palladium is byte-unchanged.

The corpus grew from **3 to 10 records**: seven elements, two mineral species,
and one secondary resource. Seven records are new; two existing records changed.
There are nine scoped mechanisms and nine dated designation entries. Counts
describe corpus contents, not independent experimental replications.

| Record | Accepted change | Independent review |
|---|---|---|
| [Neodymium](../../data/records/neodymium.yaml) | New bioleaching mechanism and US2025 entry | [20261009T045304Z](../../reviews/records/neodymium/20261009T045304Z.md) |
| [Uranium](../../data/records/uranium.yaml) | New element and scoped BES observations | [20261009T045152Z](../../reviews/records/uranium/20261009T045152Z.md) |
| [Vanadium](../../data/records/vanadium.yaml) | New element and scoped BES observations | [20261009T045152Z](../../reviews/records/vanadium/20261009T045152Z.md) |
| [Manganese](../../data/records/manganese.yaml) | New element and oxidation mechanism | [20261009T044911Z](../../reviews/records/manganese/20261009T044911Z.md) |
| [Cobalt](../../data/records/cobalt.yaml) | Added dated US2025 designation | [20261009T044937Z](../../reviews/records/cobalt/20261009T044937Z.md) |
| [Cobaltite](../../data/records/cobaltite.yaml) | New mineral identity | [20261009T044937Z](../../reviews/records/cobaltite/20261009T044937Z.md) |
| [Monazite-(Nd)](../../data/records/monazite-nd.yaml) | New mineral identity | [20261009T044937Z](../../reviews/records/monazite-nd/20261009T044937Z.md) |
| [Lamp phosphor](../../data/records/fluorescent-lamp-phosphor.yaml) | New secondary resource and bioleaching mechanism | [20261009T045304Z](../../reviews/records/fluorescent-lamp-phosphor/20261009T045304Z.md) |
| [Lithium](../../data/records/lithium.yaml) | New element and qualified bioleaching mechanism | [20261009T044911Z](../../reviews/records/lithium/20261009T044911Z.md) |

All nine reviews accept their final state, with scientific limitations where
applicable and no unresolved critical/major findings. Review corrections
restored Mn uncertainty terms, clarified the Mn light experiment's preparation,
qualified Li pH/acid attribution during curation, and removed the inappropriate
"biological" label from lamp no-bacteria replicates. The package audit also
corrected queue wording from cell-free to clarified biolixiviant. None of these
corrections silently repairs an unresolved source contradiction.

Baseline `just check`: lint passed, **215 passed, 3 skipped**, three records
and three histories valid. Final checks on 2026-10-09 (using the writable
`UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache`):

```sh
just check
uv run --locked cmmmech validate --require-records
uv run --locked cmmmech validate-history --base 905388523b6e9184783989484896e4cc20297832
git diff --check
```

Final results: lint passed; **215 tests passed, 3 optional-command cases
skipped**; **10 records, 0 failed; 12 histories, 0 errors**; whitespace check
passed. The lamp correction was revalidated individually and the independent
reviewer also reran the complete final gate. The
[validation and hash receipt](20261009-validation.json) maps every changed
record to its accepted review. Validation does not prove scientific truth.

Changes remain local and uncommitted in the dedicated worktree. The original
checkout remains clean. No issues, PRs, merges, fleet configuration, governed
artifacts or other worktrees were changed in this ingest session. The read-only
GitHub check returned no open CMMMech issues or PRs at session start; a separate
local structured-review governance branch was preserved.

## Next ingests and dependencies

1. **E1 quantitative observations:** define an observation contract retaining
   sample IDs, experimental versus analysis dates, detection-limit censoring,
   units and electrode fractions. Resolve inoculum details and matched controls
   before estimating a microbial effect; acquire an expert/reference-pattern
   interpretation before assigning a solid phase. As/Sb/Cr remain separately
   assessed candidates, not automatically accepted from U/V coverage. See
   [the BES dossier](bes-evidence.md).
2. **M3 reproducible Li comparisons:** obtain the raw Mendeley V1 data, reconcile
   the 1%/2% loading conflict and acid-dose differences, and establish culture
   provenance. Evaluate the newer lithium-study lead in
   [the Mn/Li dossier](mn-li-evidence.md) from actual methods before importing it.
   Preserve the accepted null/control-convergence results when extending coverage.
3. **M1/M2 expanded REE assays:** resolve absolute workbook units and control
   coverage for Mon2; obtain batch-specific phosphor composition before assigning
   element-specific recoveries or comparing feeds. The [REE dossier](ree-evidence.md)
   distinguishes newly inspected supplements from earlier acquisitions.
4. **A2 EU coverage:** retrieve an authentic complete original/consolidated text
   with amendment context, check the relevant annex and grouping/grade scope,
   then add separate dated designations. Existing EU2024 cobalt evidence remains
   historical; this batch makes no latest-policy assertion.
5. **D1/D2 resource context:** design a statistical observation layer only when
   a concrete use requires it; resolve the MCS dictionary/key issues first.
   For USMIN, acquire the original release and its feature/reference joins
   before any occurrence or tonnage ingest. The failure log identifies the
   original and mirror routes already attempted.
6. **I2 mineral spectra:** acquire relevant, identified specimens, verify axis
   units and reuse terms, and retain specimen-to-species distinctions. The
   discovery sample archive alone cannot populate this material/mechanism corpus.

The current narrative schema represents this batch without a behavioral change;
no schema/validator migration or implementation-mirroring tests were introduced.
Future structured data work must earn its own contract and regression tests
from actual observation requirements, rather than flattening these caveats into
free-standing numbers.
