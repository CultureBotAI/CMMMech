# Round75: reviewed clay, copper-sulfide and CRT-glass additions

Recorded UTC: 2026-10-14T15:57:58.023029+00:00. Trusted base: `4cb10d22d5542370cf5fac27288907ec0d42308c`. Worktree `/private/tmp/CMMMech-expansion-round75-20261014`; branch `curate/cmm-expansion-round75-20261014`.

Four new material identities raise the catalogue from 354 to 358 records. Selection prioritized complete primary evidence and distinct material scope. Vermiculite is retained as a mineral group; montmorillonite and djurleite are mineral owners; waste CRT glass is a secondary resource. No constituent criticality or industrial performance is inherited.

| Record | Independent scientific review | Canonical histories |
|---|---|---|
| [Vermiculite](../../data/records/vermiculite.yaml) | [pass_with_limitations](../../reviews/structured/20261014T155141Z-vermiculite-round75-independent/review.md) · [YAML](../../reviews/structured/20261014T155141Z-vermiculite-round75-independent/review.yaml) | [history1](../../history/records/vermiculite/2026-10-14T154205Z-codex-c140d7.yaml) |
| [Montmorillonite](../../data/records/montmorillonite.yaml) | [pass_with_limitations](../../reviews/structured/20261014T155141Z-montmorillonite-round75-independent/review.md) · [YAML](../../reviews/structured/20261014T155141Z-montmorillonite-round75-independent/review.yaml) | [history1](../../history/records/montmorillonite/2026-10-14T154216Z-codex-d7937f.yaml) |
| [Djurleite](../../data/records/djurleite.yaml) | [pass_with_limitations](../../reviews/structured/20261014T155030Z-djurleite-round75-independent/review.md) · [YAML](../../reviews/structured/20261014T155030Z-djurleite-round75-independent/review.yaml) | [history1](../../history/records/djurleite/2026-10-14T154126Z-codex-2adec1.yaml) |
| [Waste lead-bearing cathode-ray-tube glass](../../data/records/cathode-ray-tube-glass.yaml) | [pass_with_limitations](../../reviews/structured/20261014T155153Z-cathode-ray-tube-glass-round75-independent/review.md) · [YAML](../../reviews/structured/20261014T155153Z-cathode-ray-tube-glass-round75-independent/review.yaml) | [history1](../../history/records/cathode-ray-tube-glass/2026-10-14T154456Z-codex-6992dd.yaml) |

All four final scientific owners have independent qualified passes with exact current hashes and no corrective scientific findings. Their limits remain explicit:

- Potassium-exchanged vermiculite has no matched aged fungus-free mineral control; the source aluminium claim conflicts with its statistical table.
- Montmorillonite SWy-2 comparisons do not inherit nontronite NAu-2 sterile controls, mechanistic assays or product assignments.
- Djurleite evidence concerns a mixed natural separate, substantial chemical baseline release, missing uninoculated controls and conflicting inoculum descriptions.
- CRT glass treatment is abiotic. Component provenance is unspecified; dissolution, electrodeposition and model flows have different denominators, with conflicting treatment durations.

The two clay reviews correctly enumerate four successful batch checks but contain a one-word receipt-locator error. Their immutable originals are preserved; [the paired metadata correction](../../reviews/publication/20261014-round75/20261014T155418Z-review-locator-correction.md) binds the exact original hashes and corrects “three” to “four”. [Issue245](https://github.com/CultureBotAI/CMMMech/issues/245) is addressed locally and awaits merge closure. No scientific owner, history event or canonical finding disposition changed.

Source investigations: [clays](../sources/round75-clays/20261014T154437Z.md), [copper sulfides](../sources/round75-sulfides/20261014T154309Z-source-investigation.md), [CRT glass](../sources/round75-crt/20261014T154702Z.md). Each paired JSON records queries, inspected originals/graphics, acquisition boundaries and hashes. Raw papers remain outside Git. [Issue244](https://github.com/CultureBotAI/CMMMech/issues/244) keeps the unavailable CRT microbial sources open; CRT phosphor is distinct from glass and lamp phosphor. Digenite and anilite remain research leads, not new owners.

Validation completed: `just check` — 317 passed, 3 skipped; strict `--require-records` — 358 records, zero failures; trusted-base history validation — 413 entries, zero errors; structured review check — 427 reviews; exact-hash positive scientific coverage — 358/358 records across 76 available review bases. Generated pages are current. [Retained receipts and logs](round75-checks-20261014/) distinguish scientific review, structural validation and coverage. All 22 governed artifacts match the pinned CLAW revision. No native schema, validator, test or governed-file change was needed.

Original main and the unrelated skill worktree match initialization, including hidden/ignored file snapshots. Git administrative files and external symlink-target contents are outside that preservation inventory. Publication helpers were statically checked and retain exact-head/base, queue, tag, cleanup and fresh-main verification requirements. The final publication audit and runtime publication steps are subsequent work; this precommit manifest does not assert they have run.

The [companion JSON](round75-frontier-20261014.json) binds records, reviews, histories and the pre-manifest artifact inventory. Discovery remains active: neither this bounded search nor four accepted additions establishes that no further CMMs exist.
