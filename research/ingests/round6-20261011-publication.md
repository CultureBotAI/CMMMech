# Sixth expansion: scientific acceptance and publication preparation

Trusted base: `d09a5611767d94fd196393b31d44cb8cf6657f7f`.
Worktree: `/private/tmp/CMMMech-expansion-round6-20261011`.
Branch: `curate/cmm-expansion-round6-20261011`.
[Acceptance issue 32](https://github.com/CultureBotAI/CMMMech/issues/32).

## Scope and evidence

The add-record workflow followed the preceding frontier and selected four
missing element roots with accessible primary laboratory evidence. Element,
experimental ion/salt, mineral species, concentrate and resource identities
remain distinct. No schema, validator, test, dependency or governed artifact
needed modification; the existing field contract supports the scoped claims.

| Record | Evidence dossier | Accepted boundary |
|---|---|---|
| [Aluminium](../../data/records/aluminium.yaml) | [Urík2015](round6-aluminium-20261011.md) | Fungal mobilization from red mud; comparable acid-only result under a different protocol, undetected control with unspecified numerical detection limit, unresolved host phases |
| [Indium](../../data/records/indium.yaml) | [Nicomel2020](round6-indium-20261011.md) | Inactive mixed microalgal biosorption from synthetic solutions; Fe competition, declining reuse and uninspected supplementary controls retained |
| [Molybdenum](../../data/records/molybdenum.yaml) | [Ahmad2013](round6-mo-w-20261011.md) | DRY1 culture-associated blue signal; provisional product chemistry, inconsistent source protocols and no total-Mo recovery measurement |
| [Tungsten](../../data/records/tungsten.yaml) | [Blazevic2019](round6-mo-w-20261011.md) | Culture-enhanced filtered W release from impure scheelite concentrate; abiotic release, unknown energy donor and qualified carbide-like interpretation |

Molybdenum uses Canada's named 2024 critical-minerals list, confirmed against
the official 10 June 2024 release. The other three use individually named rows
in the final US2025 list. List membership does not make every compound or feed
containing the element critical. GenBank/NCBI labels are retained at their actual
scope: DRY1's tentative published Pseudomonas assignment is not promoted to a
resolved species, and the mixed indium biomass receives no invented taxon ID.

Four canonical CREATE sessions and separate inline events describe actual
Codex GPT-6 curation. Earlier records and committed histories/reviews remain
unchanged. Measurements outside the exact mg/kg source-cell contract remain
qualified prose. None of these studies establishes industrial deployment or
isolated pure-metal recovery.

## Independent review

The indium curator independently reviewed aluminium; the aluminium curator
reviewed indium. Root independently reviewed Mo/W, curated by a third agent.
Each reviewer captured the exact target/schema/history state before formal
assessment and independently checked the primary evidence and authorities.

All four final observations are `pass_with_limitations` with no actionable
findings. Source shortcomings already preserved in a record are not fabricated
curation defects. Issue32 tracks concrete acceptance and publication work;
there are no corrective scientific issues to conceal or silently close.

| Record | Immutable review pair |
|---|---|
| Aluminium | [YAML](../../reviews/structured/20261011T054456Z-aluminium-round6-independent/review.yaml), [Markdown](../../reviews/structured/20261011T054456Z-aluminium-round6-independent/review.md) |
| Indium | [YAML](../../reviews/structured/20261011T054446Z-indium-round6-independent/review.yaml), [Markdown](../../reviews/structured/20261011T054446Z-indium-round6-independent/review.md) |
| Molybdenum | [YAML](../../reviews/structured/20261011T054452Z-molybdenum-round6-independent/review.yaml), [Markdown](../../reviews/structured/20261011T054452Z-molybdenum-round6-independent/review.md) |
| Tungsten | [YAML](../../reviews/structured/20261011T054452Z-tungsten-round6-independent/review.yaml), [Markdown](../../reviews/structured/20261011T054452Z-tungsten-round6-independent/review.md) |

Raw full text stays outside Git. Dossiers retain original URLs, actual acquisition
times, checksums, formats, terms and failed access attempts. Indium's accepted
manuscript was inspected, but the final publisher version and supplementary
precipitation-control figure were not acquired. The W supplementary download
timed out; its main methods/results and original figures support the accepted
release observation. Review artifacts explicitly retain these access limits.
No review claims an independent raw-data replication or crystallographic
reanalysis.

## Local gates

- Baseline `just check`: 307 passed, 3 skipped in 82.95s; 32 records and
  42 histories valid, terminal exit 0.
- Complete four-record batch `just check`: 307 passed, 3 skipped in 46.67s;
  36 records and 46 histories valid, terminal exit 0.
- Separate `cmmmech validate --require-records`: 36 checked, 0 failed.
- Separate `cmmmech validate-history --base d09a5611767d94fd196393b31d44cb8cf6657f7f`:
  46 checked, 0 errors. Named-record validations also passed.
- `bash scripts/check_vendored_sync.sh`: 22 governed artifacts match immutable
  pin `a5d562962c75a2ad9efd8160b548df5944315422`, terminal exit 0.
- Trusted-base `just review-check --require-reviews`: 41 valid review pairs,
  terminal exit 0. All 36 current record hashes match independent passing
  scientific observations; 215 prior tracked corpus/history/review files are
  byte-identical to the trusted base.

Independent PR-level review and isolated squash-shaped checks remain publication
gates. Their exact outcomes,
topic/merge trees, CI runs, guarded branch deletion and fresh remote-main
validation will be recorded in the PR publication receipts; these actions are
not preclaimed here.

## Integration and provenance

Live checks on 2026-10-11 confirm [CLAW admission PR 581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
merged at `849f336e025510316a5f235eb0af8547b8bd50cc` on 8 October 2026.
History support and 22 governed artifacts are installed. Main ruleset 24692449
is active with the SQUASH/ALLGREEN native queue, required `validate-strict`
and no bypass. The manual comment-only PR shepherd is active; its runs API
returned zero executions. No broader autonomous capability or model invocation
is inferred. This batch changes no fleet configuration.

Concrete follow-up remains a deliberately scoped PR-shepherd dry run with
inspection of its output, and writer/reviewer App separation in CLAW before
expansion beyond comments. Future integration must use CLAW's supported
admission/synchronization process and immutable pins.

All new review bases are the trusted main ancestor above. The existing annotated
tag `review-base/cmm-source-survey-20261009` is retained unchanged: remote tag
object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Every distinct historical and new
review base must resolve through main ancestry or that retained reference,
including in a fresh checkout after topic-branch deletion.

## Remaining work

The [frontier](round6-frontier-20261011.md) records 36 roots and 64 unrepresented
historical proposals: 34 elements and 30 overlapping commodities. Individual REE
assays, other elements, mineral/commodity identity decisions and existing-record
evidence gaps remain actionable. This batch does not claim literature exhaustion.
