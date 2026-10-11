# Seventh expansion: scientific acceptance and publication preparation

Trusted base: `58e7aef16a9643438cf621fa9fb402e9d325dc65`.
Worktree: `/private/tmp/CMMMech-expansion-round7-20261011`.
Branch: `curate/cmm-expansion-round7-20261011`.
[Acceptance issue 34](https://github.com/CultureBotAI/CMMMech/issues/34).

## Scope and evidence

The add-record skill selected six previously unrepresented rare-earth elements
from the preceding frontier and accessible individual-analyte primary studies.
The element roots remain distinct from their dissolved ions, salts, minerals,
commodities and secondary resources. Six roots do not represent six independent
studies. All six use individually named rows in the USGS Final 2025 List,
with United States jurisdiction, edition and commodity-to-element scope explicit.
No timeless criticality or industrial deployment is asserted.

| Record | Evidence dossier | Accepted boundary |
|---|---|---|
| [Europium](../../data/records/europium.yaml) | [Fischer 2019 and later evidence](round7-eu-sm-20261011.md) | Culture-associated depletion; non-axenic strain, different assay arms, source numerical/localization conflicts and unproven particle chemistry |
| [Samarium](../../data/records/samarium.yaml) | [Fischer 2019](round7-eu-sm-20261011.md) | Separate strain and solution-depletion assay; exact supplemental concentrations, missing abiotic controls and qualitative biomass signal |
| [Terbium](../../data/records/terbium.yaml) | [Paper 2023](round7-terbium-20261011.md) | Lyophilized UTEX2973 screening endpoint; detailed Ce assays do not establish Tb kinetics, binding chemistry or fitted capacity |
| [Holmium](../../data/records/holmium.yaml) | [Zinicovscaia 2024](round7-ho-er-gd-20261011.md) | NAA of dried harvested fraction; alkaline chemistry, missing wash/control descriptions and nonuniversal rank |
| [Erbium](../../data/records/erbium.yaml) | [2024 and contrasting 2022 assays](round7-ho-er-gd-20261011.md) | Harvested-fraction association; contrasting growth outcomes under different protocols |
| [Gadolinium](../../data/records/gadolinium.yaml) | [Zinicovscaia 2024](round7-ho-er-gd-20261011.md) | Harvested-fraction association; graph/text endpoint and biochemical-summary discrepancies preserved |

Ho/Er/Gd use `process: other` because their assay cannot resolve intracellular
uptake, surface binding and retained abiotic material. No chemical phase is
invented. Eu/Sm preserve exact supplement values rather than adopting stronger
main-text summaries. ICP-MS and NAA measure elemental content, not oxidation
state. No isolated product yield, mixed-REE selectivity or field performance
is inferred from these assays.

Six canonical CREATE sessions and separate inline events record actual
codex/GPT-6/codex curation. No schema, validator, test, dependency or governed
artifact needed modification. Measurements outside the exact native mg/kg
source-cell contract remain qualified prose; missing analysis dates or source
cells are not manufactured to force graph results into structured observations.

## Independent scientific reviews

The Ho/Er/Gd curator reviewed Eu/Sm; the Tb curator reviewed Ho/Er/Gd; root
reviewed Tb. Each reviewer is different from the corresponding curator and
captured final target/schema/history hashes before formal assessment.

All six observations are `pass_with_limitations`, with no actionable findings.
The source shortcomings already encoded in the records are not fabricated
curation defects. A draft Tb page locator was independently corrected by its
curator before freeze; it was not reintroduced to manufacture a review issue.
Issue 34 tracks genuine acceptance and publication work.

| Record | Immutable review pair |
|---|---|
| Europium | [YAML](../../reviews/structured/20261011T060643Z-europium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060643Z-europium-round7-independent/review.md) |
| Samarium | [YAML](../../reviews/structured/20261011T060643Z-samarium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060643Z-samarium-round7-independent/review.md) |
| Terbium | [YAML](../../reviews/structured/20261011T060518Z-terbium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060518Z-terbium-round7-independent/review.md) |
| Holmium | [YAML](../../reviews/structured/20261011T060517Z-holmium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060517Z-holmium-round7-independent/review.md) |
| Erbium | [YAML](../../reviews/structured/20261011T060517Z-erbium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060517Z-erbium-round7-independent/review.md) |
| Gadolinium | [YAML](../../reviews/structured/20261011T060517Z-gadolinium-round7-independent/review.yaml), [Markdown](../../reviews/structured/20261011T060517Z-gadolinium-round7-independent/review.md) |

Raw primary material remains outside Git. Dossiers retain URLs, actual UTC
receipts, terms, content checks, hashes and failed routes. Eu/Sm supplement
archives timed out, but complete members were recovered with matching CRC32,
DEFLATE completion and compressed/uncompressed lengths; the independent reviewer
recomputed the five-page supplement's integrity. No incomplete archive is
represented as complete. Main Figure 4/8 pixels remained unavailable; relevant
claims are explicitly attributed to Results/captions, not independently
remeasured microscopy. Later Sm full text remains a deferred evidence gap.

## Local gates

- Baseline `just check`: 307 passed, 3 skipped in 68.10s; 36 records and
  46 histories valid; terminal exit 0.
- Complete batch `just check`: 307 passed, 3 skipped in 51.17s; lint passed,
  42 records and 52 histories valid; terminal exit 0.
- Separate `cmmmech validate --require-records`: 42 checked, zero failures.
- Separate `cmmmech validate-history --base 58e7aef16a9643438cf621fa9fb402e9d325dc65`:
  52 checked, zero errors. Named-record validations also passed.
- `bash scripts/check_vendored_sync.sh`: 22 governed artifacts match unchanged
  immutable pin `a5d562962c75a2ad9efd8160b548df5944315422`; terminal exit 0.

Trusted-base `just review-check --require-reviews` passed with 47 valid review
pairs. All 42 current record hashes match independent passing scientific
observations. All 231 prior corpus/history/review files remain byte-identical.
The packaging audit matched 179 recorded path/hash pairs and 119 relative links.
All eight distinct review bases resolve through main ancestry or the retained
tag below.

Independent PR review, isolated squash preflight, CI/queue execution, branch
deletion and fresh-main results will be recorded in PR publication receipts.
This report does not preclaim those subsequent publication steps.

## Integration and durable provenance

Live checks on 2026-10-11 confirm [CLAW admission PR 581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
merged at `849f336e025510316a5f235eb0af8547b8bd50cc` on 8 October 2026.
History and 22 governed artifacts are installed. Main ruleset 24692449 is active,
using the SQUASH/ALLGREEN native queue, required `validate-strict`, and no bypass.
The manual comment-only PR shepherd is active; its runs API returned zero
executions. No model invocation or broader fleet capability is inferred here.

Concrete follow-up remains a scoped PR-shepherd dry run with inspected output,
and writer/reviewer App separation in CLAW before expanding beyond comments.
Future integration must use CLAW's supported admission/synchronization process
and immutable pins; this curation batch changes no fleet configuration.

All new scientific reviews use the trusted main ancestor above. Existing
annotated tag `review-base/cmm-source-survey-20261009` remains unchanged:
remote tag object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Every distinct historical/new review
base must resolve through main ancestry or this retained reference, including
in the isolated and post-deletion remote-main checkouts.

## Remaining priorities

The [frontier](round7-frontier-20261011.md) records 42 roots and 58 unrepresented
historical proposals: 28 elements and 30 overlapping commodities. Priorities are
individual Y/Yb/other REE assays, separate commodity-identity decisions, primary
source-data reconciliation and better controlled extensions of existing records.
This batch does not claim exhaustion of CMMs or their primary literature.
