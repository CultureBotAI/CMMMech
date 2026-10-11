# Fifth expansion: scientific acceptance and publication preparation

Trusted base: `e305dcc67e526e585349c60f849567f4c2bfc835`.
Worktree: `/private/tmp/CMMMech-expansion-round5-20261011`.
Branch: `curate/cmm-expansion-round5-20261011`.

## Scope and evidence

The add-record workflow followed the round4 frontier, selecting five missing
element roots with accessible primary laboratory evidence. Element identities,
experimental ions/salts, mineral phases, commodity grades and secondary
resources remain distinct.

| Record | Research dossier | Accepted scientific boundary |
|---|---|---|
| [Iron](../../data/records/iron.yaml) | [Sklute2023](round5-iron-20261011.md) | Ax17 ferrihydrite reduction; mixed magnetite-rich product, extraction-based Fe(II) assay and abiotic mineral formation retained |
| [Germanium](../../data/records/germanium.yaml) | [Two companion 1986 studies](round5-germanium-20261011.md) | ATCC 33015 accumulation; separate kinetic/fractionation assays, low solution depletion and provisional transport explanation |
| [Lanthanum](../../data/records/lanthanum.yaml) | [REE dossier](round5-ree-20261011.md) | Fungal culture supernatant precipitation; chemical comparator and separate thermal oxide conversion |
| [Dysprosium](../../data/records/dysprosium.yaml) | [REE dossier](round5-ree-20261011.md) | Dried yeast biosorption; conflicting source conditions, fitted versus measured capacities, and incomplete aqueous assay reporting |
| [Magnesium](../../data/records/magnesium.yaml) | [Suyamud2020](round5-magnesium-20261011.md) | Fungal magnesium oxalate formation; natural struvite versus synthetic dittmarite, phase/control and recovery limits |

Iron cites the UK technical annex updated 23 January 2026, expressly sourced
to the 2024 CMIC assessment. It does not inherit Canada's high-purity iron ore
designation. The other four records cite individually named rows in the final
US 2025 list. No record asserts industrial deployment or turns solution removal
into purified-element recovery. Companion papers and reused fungal strains are
not presented as independent replications of one universal process.

Five CREATE sidecars and one corrective EDIT sidecar record actual Codex GPT-6
work, with separate inline events. The prior 27 records and all committed
histories/reviews are preserved. No schema, validator, test behavior, dependency
or governed artifact changed: the existing contract supports these claims.
Measurements outside exact mg/kg source cells remain qualified prose.

## Independent reviews and issue disposition

[Issue 29](https://github.com/CultureBotAI/CMMMech/issues/29) tracks concrete
batch acceptance. Each record is reviewed by a different agent from its curator:
the germanium curator reviews iron; the iron curator reviews La/Dy; the REE
curator reviews magnesium; the root reviews germanium.

The initial germanium review found one minor consistency defect: unqualified
unreported-replication wording overlooked the paper's duplicate analytical
aliquots. [Issue 30](https://github.com/CultureBotAI/CMMMech/issues/30) records
that finding. The curator distinguished analytical duplicates from missing
biological replicate counts/statistical uncertainty, appended an EDIT history,
and obtained an independent successor disposition retaining the exact issue key
and predecessor. The original review and CREATE sidecar remain intact.

All five final records have independent `pass_with_limitations` observations.
The only actionable scientific finding is explicitly resolved; no open
major/blocker finding is hidden by a later clean review. Final record hashes
match the corresponding acceptance observations.

| Record / round | Immutable review pair |
|---|---|
| Iron | [YAML](../../reviews/structured/20261011T052250Z-iron-round5-independent/review.yaml), [Markdown](../../reviews/structured/20261011T052250Z-iron-round5-independent/review.md) |
| Germanium initial | [YAML](../../reviews/structured/20261011T052122Z-germanium-round5-independent/review.yaml), [Markdown](../../reviews/structured/20261011T052122Z-germanium-round5-independent/review.md) |
| Germanium resolution | [YAML](../../reviews/structured/20261011T052423Z-germanium-round5-resolution/review.yaml), [Markdown](../../reviews/structured/20261011T052423Z-germanium-round5-resolution/review.md) |
| Lanthanum | [YAML](../../reviews/structured/20261011T052640Z-lanthanum-round5-independent/review.yaml), [Markdown](../../reviews/structured/20261011T052640Z-lanthanum-round5-independent/review.md) |
| Dysprosium | [YAML](../../reviews/structured/20261011T052640Z-dysprosium-round5-independent/review.yaml), [Markdown](../../reviews/structured/20261011T052640Z-dysprosium-round5-independent/review.md) |
| Magnesium | [YAML](../../reviews/structured/20261011T052311Z-magnesium-round5-independent/review.yaml), [Markdown](../../reviews/structured/20261011T052311Z-magnesium-round5-independent/review.md) |

## Validation

- Baseline `just check`: 307 passed, 3 skipped in 57.23s; 27 records and
  36 histories valid, terminal exit 0.
- Complete five-record batch `just check`: 307 passed, 3 skipped in 57.39s;
  32 records and 41 histories valid, terminal exit 0. This precedes the
  germanium prose clarification and added correction history.
- After that correction, named germanium validation passed (1/0),
  `cmmmech validate --require-records` passed (32/0), and
  `cmmmech validate-history --base e305dcc67e526e585349c60f849567f4c2bfc835`
  passed (42 histories, 0 errors). No code/schema changed.
- `bash scripts/check_vendored_sync.sh`: 22 governed artifacts match
  `a5d562962c75a2ad9efd8160b548df5944315422`, terminal exit 0.

- Final trusted-base `just review-check --require-reviews`: 37 valid review
  pairs, terminal exit 0. All 32 current record hashes match independent
  passing scientific observations.
- Preservation/packaging audits: 192 base-tracked corpus/history/review files
  unchanged; 78 retained raw/derived hashes and 32 frontier record hashes
  match; 96 relative links across 14 Markdown documents resolve.
- A fresh independent PR-level agent found no remaining actionable semantic
  or packaging defect. Its small trailing-whitespace finding in the iron
  dossier was fixed; it did not repeat the primary-literature audit.

Raw evidence remains outside Git, with acquisition failures, source terms and
checksums in the dossiers. Magnesium's full primary text/captions were inspected
through the web PDF reader, but figure pixels were not available in that route;
no diffraction-image reanalysis is claimed. Other reviewers independently
inspected the acquired primary scans/figures and relevant supplements as stated
in their own artifacts. Reviews distinguish actual access from missing evidence.

## Integration and publication gates

Live checks on 2026-10-11 confirm [CLAW admission PR 581](https://github.com/CultureBotAI/culturebotai-claw/pull/581)
merged at `849f336e025510316a5f235eb0af8547b8bd50cc` on 8 October 2026.
History and governed artifacts are installed. Main ruleset 24692449 is active
with SQUASH/ALLGREEN native queue and required `validate-strict`; it permits
no bypass. The PR shepherd is active as a manual, comment-only workflow;
the runs API returned zero executions. No model execution or broader autonomous
fleet capability is inferred. Future integration must use CLAW's supported
admission and synchronization process; this batch changes no configuration.

Concrete integration follow-up is to run and inspect a deliberately scoped
PR-shepherd dry run, then address its documented writer/reviewer App separation
in CLAW before expanding it beyond comments. Any governed update should be
published there and synchronized at an immutable pin. Existing admission,
shared history and native queue installation are complete, not pending setup.

All new review bases are the trusted main ancestor above. The existing annotated
tag `review-base/cmm-source-survey-20261009` is retained unchanged: remote tag
object `fc4040c3abcd28f0a9cc52467e308100144ad1fd`, peeled commit
`c0adc2c0763e1515ed07dc712b024974d98fb342`. Every distinct review base must
resolve through main ancestry or that retained tag. The PR publication receipt
will record exact topic/merge trees, independent PR review, squash-shaped
validation without the topic branch, queue CI, guarded branch deletion and a
fresh remote-main checkout with explicit tag fetch. These are gates, not
preclaimed merge results.

## Remaining priorities

The [frontier](round5-frontier-20261011.md) now records 32 roots and 68
unrepresented historical proposals: 38 elements and 30 overlapping commodities.
Next work includes individual-analyte REE/other-element experiments, Ge feed and
strain extensions, commodity/mineral identity decisions and existing-record
evidence gaps. This batch does not establish exhaustion of CMM literature.
