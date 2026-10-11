# Second expansion batch: review and publication preparation

This batch continues the [authority inventory](../sources/expansion-authorities/20261011T040103Z.md)
above trusted main revision `268498d0a9748f3a18955e35f175f67115f88b97`.
Worktree: `/private/tmp/CMMMech-expansion-round2-20261011`.
Branch: `curate/cmm-expansion-round2-20261011`.

## Selection and scope

The four additions were selected for accessible primary methods and useful
control evidence: zinc adds a matched-chemistry mechanistic challenge; silver
adds an XRD-supported transformation with abiotic precipitation and toxicity
limits; gallium and arsenic reuse one sludge experiment for two distinct
analytes. They are not four independent experimental replications.
All roots are elements; mineral concentrates, salts and sludge remain explicit
experimental forms. Each criticality assertion names the US final 2025 list.

| Record | Dossier | Preserved limits |
|---|---|---|
| [Zinc](../../data/records/zinc.yaml) | [Evidence](round2-zinc-20261011.md) | 1998 null; 1999 figure/prose tension; sulfur-layer interpretation, not a demonstrated enzyme |
| [Silver](../../data/records/silver.yaml) | [Evidence](round2-silver-20261011.md) | Salt-feed ambiguity; abiotic precipitation; toxicity; no isolated yield |
| [Gallium](../../data/records/gallium.yaml) | [Evidence](round2-gallium-arsenic-20261011.md) | Acid dissolution dominates; microbial increment provisional |
| [Arsenic](../../data/records/arsenic.yaml) | [Evidence](round2-gallium-arsenic-20261011.md) | Similar acid-control endpoint; no measured redox/speciation or demonstrated microbial advantage |

The model and schema already represent these bounded claims; no schema,
validator, tests, dependencies or governed artifacts changed. Four actual CREATE
sidecars and separate inline events were attached before independent review.
The existing thirteen records and their immutable histories/reviews were preserved.

## Adversarial review and issue disposition

Three curation agents authored disjoint records. The root reviewer independently
reviewed Ga/As; the zinc and silver curators reviewed each other's records.
A separate publication-process audit checked README scope, provenance receipts,
local links, source terms, bounded absence claims and live merge rules without
claiming independent scientific review of its own Ga/As curation.

The reviewers found no actionable record defects. Source uncertainty was already
preserved during curation; it was not fabricated into a validator failure or a
scientific correction. [Issue #23](https://github.com/CultureBotAI/CMMMech/issues/23)
is an explicit curation acceptance/tracking issue for these source ambiguities,
final review coverage and publication checks. It does not claim the drafts had
omitted the caveats. Its acceptance is addressed by these reviewed records and
publication receipts; experimental uncertainties remain limitations.

## Checks before publication

- Baseline: `just check` — 307 passed, 3 skipped; 13 records, 22 histories valid.
- Four-record batch: `just check` — 307 passed, 3 skipped in 42.24 seconds;
  17 records, 26 histories valid.
- `uv run --locked cmmmech validate --require-records` — 17 valid, zero failed.
- `uv run --locked cmmmech validate-history --base 268498d0a9748f3a18955e35f175f67115f88b97`
  — 26 valid, zero errors.
- `bash scripts/check_vendored_sync.sh` — 22 governed artifacts match the
  immutable public CLAW pin.
- Scientific reviews and final record hashes are checked separately; the PR
  publication receipt records final structured-review and squash/fresh-main gates.

Raw articles/images stay outside Git. The independent process audit verified all
24 successful retained-file entries across the new acquisition receipts against
local byte sizes and SHA-256 values. The selenium receipt transparently records
its reconstruction after a failed second acquisition and distinct source license.

## Integration and provenance

Live GitHub ruleset 24692449 was read on 2026-10-11: main has the active native
SQUASH/ALLGREEN queue and required `validate-strict`; no bypass is used. Fleet
admission, curation history and the 22 governed artifacts are installed. The
shepherd remains manual/comment-only. No integration configuration was changed;
future governance changes must use CLAW's supported admission/synchronization
process rather than edits to vendored copies.

New reviews use the existing main revision above. The earlier retained annotated
`review-base/cmm-source-survey-20261009` tag remains unchanged, remotely verified
at tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. All distinct review bases must be
available in both squash-shaped and post-deletion fresh checkouts.

## Remaining frontier

[Selenium](../sources/round2-selenium-handoff/20261011T042117Z.md) is a documented
handoff, not an accepted record: full claim-level interpretation, supporting
file/figure review and differing localization reports still need resolution.
The GaAs-production sludge is a potential separate secondary resource, with
no inherited element criticality. Additional gallium experiments, chromium,
platinum, cadmium, phosphorus and mineral-host identities remain in the earlier
inventory/dossiers. Many jurisdictions and citation chains remain unsearched.
This batch advances coverage; it does not establish that no new CMMs remain.
