# BES concentration-cell ingest

Curated 2026-10-09 UTC by `/root/ingest_bes`, Codex (GPT-6). Base commit:
`610d27a40d89861961052f0e0bebfaa7882e35cf`, branch
`research/cmm-source-survey-20261008`. This dossier documents curation and
source interpretation; independent record and implementation reviews follow.

## Scope and reason for the contract

The previously accepted [uranium](../../data/records/uranium.yaml) and
[vanadium](../../data/records/vanadium.yaml) narratives contain eight exact
concentration cells from [USGS release 10.5066/P9ERLSM6](https://doi.org/10.5066/P9ERLSM6).
They are now represented as observations nested under their existing separation
mechanisms. The new native class preserves a reported numeric value separately
from a below-detection boundary and binds each result to the source cell,
sample, analysis date, study arm and fraction. No bulk importer, generic
statistics framework, T6 amount, recovery percentage or microbial-effect
estimate is added.

An observation can belong to an abiotic control within a microbial mechanism.
Its existence does not establish microbial causation. Biotic baselines were
sampled before inoculation; `study_arm: biotic` identifies the assigned run.
ICP-OES measures total elemental U/V; the ChEBI atom identifiers identify the
elements, not dissolved neutral atoms or measured oxidation states. The unit
is mass-based `mg/kg`; no density conversion to `mg/L` is assumed.

## Source-cell manifest

All rows come from `T3_AqueousICPOES.csv`; `RunDate` is the analysis date.
Raw tokens below are copied exactly. Collection dates are joined from the
`Date` column of `T2_pH.csv` using an **exact** `SampleID`, with US date
strings parsed explicitly as month/day/year. No suffix normalization, fuzzy
join or timestamp timezone was invented.

| Record | Source SampleID | Column | Raw token | Result | Analysis date | Exact T2 sample date |
|---|---|---|---|---|---|---|
| U | BESU.8Vb_W.EQ | U_ppm | `975` | measured 975 mg/kg | 2024-09-24 | 2024-09-06 |
| U | BESU.8Vb_W.END | U_ppm | `-0.1` | below detection; limit 0.1 mg/kg; no value | 2024-10-29 | 2024-09-27 |
| U | BESU.8Va_W.t0 | U_ppm | `914` | measured 914 mg/kg | 2024-09-24 | 2024-08-08 |
| U | BESU.8Va_W.END | U_ppm | `0.819` | measured 0.819 mg/kg | 2024-09-24 | unrecorded: no exact T2 match |
| V | Vbrr_0 | V_ppm | `44.1` | measured 44.1 mg/kg | 2025-08-06 | 2025-05-21 |
| V | BESV.brr_END | V_ppm | `34` | measured 34 mg/kg | 2025-06-12 | 2025-05-30 |
| V | BESVarr_0 | V_ppm | `19.1` | measured 19.1 mg/kg | 2025-07-03 | 2025-05-15 |
| V | BESVarr_END | V_ppm | `12.2` | measured 12.2 mg/kg | 2025-07-03 | 2025-05-21 |

These eight observations preserve previously accepted numerical claims; they
do not silently enlarge their experimental scope. The V biotic baseline was
analyzed later than the endpoint. Ordering the experiment by `RunDate` would
reverse the apparent time course, so both dates are retained. The missing U
abiotic-endpoint sampling date is not borrowed from another sample or from
its analysis date.

## Dictionary, keys and excluded cells

Re-inspected T1, T2, T3, T6 and FGDC metadata process steps 1-8. T1 defines
ICP-OES ppm as mg/kg and negative assay values as below the absolute-value
detection limit; metadata step 8 separately defines `-9999` as no data. No
blank, missing sentinel or unrelated negative cell is ingested. A raw negative
number in another dataset must not automatically receive this interpretation.
The source-dictionary check is a curation duty; the native validator checks
consistency of the declared measured/below-detection interpretation.

- T3 has 87 rows, unique by normalized `(RunDate, SampleID)` in this snapshot.
  A concentration cell additionally requires its analyte column.
- T2 has 43 rows with unique `SampleID`; exactly seven of the eight selected
  concentration cells have a matching sampling-date row.
- T6 has 22 rows with unique normalized `(RunDate, SampleID)`; all 22 map to
  T3 by that pair. The tempting `(ExpName, ExpCondition, DigestMedia)` key is
  not unique and conflates distinct samples/fractions.
- The biotic U carbonate row `BESU.8Vb_CarbExtract` has T6 amount `2.00E-05`
  mmol but corresponding T3 `U_ppm=-0.1`. Treating that T6 figure as an exact
  quantified measurement would disregard its censored concentration input.
  No T6 quantities are imported in this batch.
- T3 contains both solution samples and digests. Only the eight explicitly
  selected working-solution cells are ingested; the filename does not establish
  a common sample fraction. Metadata step 2 supplies the 0.22 micrometre
  filtration and nitric-acid preservation used for these solution samples.
- Metadata steps 1 and 3 place inoculation after the second solution sample.
  The biotic U EQ and V sample-0 observations are therefore pre-inoculation
  baselines, not already populated with live cells because of their arm label.

## Acquisition and source version

This is re-inspection of retained sources, not a new download or a new USGS
edition. Original public acquisition receipts are in the prior
[landscape evidence JSON](../sources/cmm-landscape/20261008T073140Z-evidence.json)
and [BES dossier](bes-evidence.md). The release is CC0, published 2026-09-15,
with the portal dated 2026-09-17. It supplies no semantic version. Source
bytes used in this pass were rehashed on 2026-10-09:

| File | SHA-256 |
|---|---|
| `T1_TableDefinitions.csv` | `35faec5b3a4b1f7fb2d2eff61b8ae0a5d41f1ebce361202faa6f411f8eaca1d3` |
| `T2_pH.csv` | `37b437d1194bc4d0b1906d6a5e63e0f347158ceef6e7621ec339fa3ece1911cf` |
| `T3_AqueousICPOES.csv` | `f58cea91f3710752ea44d05fde1f489d8c66b42aa351a2b2e8c08f946751ac32` |
| `T6_DigestRecovery.csv` | `b2e0680798f379adfa34d12acab667d8658d0ee35579526adcda9b89dcaf8024` |
| FGDC `bes-metadata.xml` | `473351beae50f2bc4d86078ddeeb34b71978bd88eb145cecc10d767b376d6bd6` |

The earlier BES investigation by this same curator on 2026-10-09 performed
these live web searches, one returned result set each and no pagination:

- `"10.5066/P9ERLSM6" correction retraction`
- `"P9ERLSM6" uranium vanadium bioelectrochemical`
- `"Data acquired in experiments on bioelectrochemical" correction`
- `Kane Selvage Ciechanowicz Campbell Shewanella uranium vanadium 2026`

Those bounded results resolved the release and related work but did not verify
a correction, retraction or companion interpretation paper. They are not an
exhaustive absence claim. This subsequent structured-cell pass reused that
same-day search coverage and retained sources; it did not rerun the searches
or claim fresh remote acquisition. The prior [BES dossier](bes-evidence.md)
records the findings and acquisition limits in more detail.

T2 resides at `/private/tmp/cmm-bes-ingest/T2_pH.csv`; the other four files
are under `/private/tmp/cmm-source-discovery-downloads/`. No raw bulk table
or third-party full text is committed by this batch. The earlier independent
record reviews establish unchanged identity/criticality and bounded narrative
claims; the new reviews must cover these added observations and final hashes.

## Implemented native behavior

`ConcentrationObservation` is a closed optional class nested under a mechanism.
Measured results require only finite nonnegative `value`; below-detection
results require only finite positive `detection_limit`. Exact source-token
consistency is checked with decimal arithmetic without rounding the source
mantissa. `NaN`, infinities, contradictory status/numeric fields, and numeric
conversion failures fail cleanly. A true source zero is permitted.

Observation IDs and source-cell keys are unique within the material record.
`source_ref` must resolve both to a record source and the parent mechanism's
evidence. Sampling date and its locator are paired; sampling after analysis
is rejected rather than silently repaired. Unknown sampling dates remain
absent. Existing records without observations remain valid. The schema's
governed imports were not edited.

Synthetic regression tests cover censored-as-measured and zero substitutions,
raw-token mismatches, required/exclusive result fields, nonfinite YAML values,
very large numeric representations, exact censored mantissa comparison,
source/evidence linkage, duplicate IDs/cells, malformed dates, sampling-date
provenance, incompatible units and closed fields. These tests exercise the
contract, not scientific truth or source access.

## Provenance and checks

Final parsed comparison against `610d27a40d89861961052f0e0bebfaa7882e35cf`
proved that removing the new observations and the one appended history event
and reference in each record leaves **every prior U/V field unchanged**.
All eight raw values and analysis dates exactly matched their T3 source keys;
all seven recorded sample dates matched exact T2 keys. New actual-time sidecars
were created through the native `new-history` command and separately linked;
all committed sessions are preserved.

Final curator checks used `UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache`:

- `just check` passed lint and **280 tests, 3 existing optional-command skips**.
  Its corpus-validation stage encountered a concurrently edited neodymium YAML
  indentation error outside this U/V assignment; it did not report a U/V
  failure. The completed batch gate is owned by the parent session after the
  concurrent record edits settle.
- `uv run --locked cmmmech validate data/records/uranium.yaml data/records/vanadium.yaml`:
  **2 records, 0 failed** after all U/V additions and history links.
- `uv run --locked cmmmech validate-history --base 610d27a40d89861961052f0e0bebfaa7882e35cf`:
  **19 history sessions, 0 errors** at the concurrent batch snapshot.
- `git diff --check` passed.

Final record SHA-256 values for independent review:

- Uranium: `ab487f64f4ea571ddb2560a7cd2d51ce8131c8a24ef9570ed0eb21c62d51b60f`.
- Vanadium: `c923fc61cee7c487e376a6b42d023bd7241a635aa8a837c6cd21db1f8fa919ce`.

Independent review is still required; these checks do not establish scientific
truth or resolve the retained experimental limitations.
