# Eighth expansion: evidence and publication preparation

Trusted base: `5b4a463f700bceb441f7b669f58a5e60823d2841`.
Worktree: `/private/tmp/CMMMech-expansion-round8-20261011`.
Branch: `curate/cmm-expansion-round8-20261011`.
[Acceptance issue 36](https://github.com/CultureBotAI/CMMMech/issues/36).

## Scope and evidence

The add-record skill selected six element roots from the preceding frontier,
prioritizing accessible individual-analyte evidence and different experimental
approaches. Research changed the initial source choices where complete methods
were unavailable or reported quantities were inconsistent. Each root remains
distinct from ions, salts, minerals, commodity mixtures and secondary resources.
All six criticality entries name the United States, the final 2025 list and its
publication edition; each exact commodity row was checked at GovInfo. No
timeless criticality or industrial deployment is asserted.

| Record | Evidence dossier | Scientific boundary |
|---|---|---|
| [Yttrium](../../data/records/yttrium.yaml) | [Y/Yb](round8-y-yb-20261011.md) | Washed living ACUF 427 biomass association; revised taxonomy, weaker mixture results and unresolved localization |
| [Ytterbium](../../data/records/ytterbium.yaml) | [Y/Yb](round8-y-yb-20261011.md) | Partial aqueous depletion with T9; Dy-specific microscopy, capacities and replication cannot be transferred to Yb |
| [Scandium](../../data/records/scandium.yaml) | [Sc/Pr](round8-sc-pr-20261011.md) | Cell-free lanmodulin capture and malonate elution; inconsistent source feed accounting, limited replication and missing direct resin control |
| [Praseodymium](../../data/records/praseodymium.yaml) | [Sc/Pr](round8-sc-pr-20261011.md) | Binary Pr/La protein separation; collected-fraction yield and lower repeat performance remain explicit |
| [Lead](../../data/records/lead.yaml) | [Pb/Bi](round8-pb-bi-20261011.md) | Controlled remobilization from synthetic pyromorphite; nutrient dependence, unequal pH and reversible binding limit generalization |
| [Bismuth](../../data/records/bismuth.yaml) | [Pb/Bi](round8-pb-bi-20261011.md) | Fusarium BI accumulation in phosphorus-rich granules; soluble-pool denominator, uncertain replication and unresolved chemical phase/valence |

Y/Yb and Bi use `process: other` where the evidence cannot establish a unique
transport, binding or precipitation pathway. Sc/Pr explicitly distinguish the
protein-origin organism, recombinant expression host and cell-free separation.
Their aqueous fractions are not isolated elemental products. Lead adds an
adverse environmental direction: microorganisms can mobilize material previously
immobilized as a mineral. Separate deposition studies under different conditions
do not negate that controlled result.

Six canonical CREATE sessions and distinct inline events record actual
codex/GPT-6/codex curation. No schema, validator, test, dependency or governed
artifact changes were needed. Numerical results outside the native exact mg/kg
source-cell contract remain qualified prose; missing dates and measurements
were not invented to populate structured observations.

## Independent review and corrections

The Pb/Bi curator reviewed Y/Yb, the Y/Yb curator reviewed Sc/Pr, and the
Sc/Pr curator reviewed Pb/Bi. Each reviewer differed from the corresponding
curator, captured exact target/schema/history/dossier hashes before assessment
and checked the primary evidence independently. All six final observations are
`pass_with_limitations`.

One minor dossier finding was saved before correction and tracked in
[issue 37](https://github.com/CultureBotAI/CMMMech/issues/37): the Y narrative
called unspecified triplicate experiments biological replication. The corrected
wording leaves independent culture derivation unknown. The record already used
appropriately narrow wording, so record and history bytes did not change and
no artificial EDIT event was added. The initial
[YAML](../../reviews/structured/20261011T063036Z-yttrium-round8-independent/review.yaml)
and [Markdown](../../reviews/structured/20261011T063036Z-yttrium-round8-independent/review.md)
remain unchanged. The successor below explicitly resolves the same issue key
and exact predecessor occurrence. No other actionable scientific findings were
identified in this bounded review; source limitations remain visible.

| Record | Immutable final review pair | Verdict |
|---|---|---|
| Yttrium | [YAML](../../reviews/structured/20261011T063602Z-yttrium-round8-resolution/review.yaml), [Markdown](../../reviews/structured/20261011T063602Z-yttrium-round8-resolution/review.md) | pass_with_limitations |
| Ytterbium | [YAML](../../reviews/structured/20261011T063602Z-ytterbium-round8-independent/review.yaml), [Markdown](../../reviews/structured/20261011T063602Z-ytterbium-round8-independent/review.md) | pass_with_limitations |
| Scandium | [YAML](../../reviews/structured/20261011T063207Z-scandium-round8-independent/review.yaml), [Markdown](../../reviews/structured/20261011T063207Z-scandium-round8-independent/review.md) | pass_with_limitations |
| Praseodymium | [YAML](../../reviews/structured/20261011T063207Z-praseodymium-round8-independent/review.yaml), [Markdown](../../reviews/structured/20261011T063207Z-praseodymium-round8-independent/review.md) | pass_with_limitations |
| Lead | [YAML](../../reviews/structured/20261011T063400Z-lead-round8-independent/review.yaml), [Markdown](../../reviews/structured/20261011T063400Z-lead-round8-independent/review.md) | pass_with_limitations |
| Bismuth | [YAML](../../reviews/structured/20261011T063400Z-bismuth-round8-independent/review.yaml), [Markdown](../../reviews/structured/20261011T063400Z-bismuth-round8-independent/review.md) | pass_with_limitations |

Raw primary material stays outside Git. Dossiers preserve URLs, actual UTC
acquisitions, hashes, content checks, terms and failed routes. Y supplements
remain an access gap; the relevant main-text claims are qualified accordingly.
The initial freeze-dried Y study's capacity exceeds its stated input mass
balance and is deferred, as are abstract-only Yb studies. Bi nanocrystal claims
from an inaccessible source are not borrowed into the accepted accumulation
record. No missing evidence is replaced by inferred measurements.

## Local gates

- Baseline `just check`: 307 passed, 3 skipped in 81.07s; lint passed,
  42 records and 52 histories valid; terminal exit 0.
- Complete-batch `just check`: 307 passed, 3 skipped in 46.87s; lint passed,
  48 records and 58 histories valid; terminal exit 0.
- Separate `cmmmech validate --require-records`: 48 checked, zero failures.
- Separate `cmmmech validate-history --base 5b4a463f700bceb441f7b669f58a5e60823d2841`:
  58 checked, zero errors. Named-record checks also passed.
- `bash scripts/check_vendored_sync.sh`: 22 artifacts match unchanged pin
  `a5d562962c75a2ad9efd8160b548df5944315422`; terminal exit 0 after retrying
  an initial sandbox DNS failure with authorized network access.

Trusted-base `just review-check --require-reviews` passed with 54 valid review
pairs, including seven new observations. All 48 current record hashes match
independent passing scientific reviews. All 255 prior corpus/history/review
files remain byte-identical, as does the initial Y finding pair. The packaging
audit matched 182 recorded path/hash pairs and 121 relative links. All nine
review bases resolve through main ancestry or the retained tag below.

The dossier-only correction did not alter code, record or history bytes.
Post-correction named validation passed, and the affected review, lineage,
hash and documentation checks were repeated. Subsequent independent PR review,
isolated squash verification, queue execution, branch deletion and fresh-main
results belong in the PR publication receipts; this preparation report does
not preclaim those steps.

## Integration and durable provenance

Live checks on 2026-10-11 confirm [CLAW admission PR 581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
merged at `849f336e025510316a5f235eb0af8547b8bd50cc` on 8 October 2026.
History support and the 22 governed artifacts are installed. Main ruleset
24692449 is active, using the SQUASH/ALLGREEN native queue, required
`validate-strict`, zero approving-review requirement and no bypass actors.
The manual, comment-only PR shepherd is active; its runs API returned zero
executions. No model invocation or broader fleet capability is inferred.

Concrete follow-up remains a scoped PR-shepherd dry run with inspected output,
and writer/reviewer App separation in CLAW before expanding beyond comments.
Future integration must use CLAW's supported admission/synchronization process
and immutable pins. This batch changes no fleet configuration.

New reviews use the trusted main ancestor above. The historical annotated tag
`review-base/cmm-source-survey-20261009` remains unchanged: remote tag object
`fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Every distinct review base must
resolve through main ancestry or this retained reference after squash and
topic-branch deletion; no new review depends on a disposable topic commit.

## Remaining priorities

The [frontier](round8-frontier-20261011.md) contains 48 roots and 52 unrepresented
historical proposals: 22 elements and 30 overlapping commodities. Next work
includes independent concept decisions for commodity grades/groups, remaining
element assays, source-data reconciliation and better controlled extensions
of existing records. This batch does not claim CMM or literature exhaustion.
