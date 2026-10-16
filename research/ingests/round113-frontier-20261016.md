# Round113: eight reviewed mineral and secondary-resource records

Prepared 2026-10-16T06:14:05.044362+00:00, working base `9ebff7bf980911e7be86bf19d865aeeca8450781`.

The batch adds six mineral species and two process-defined secondary resources. Identity-only records are retained where processing evidence is unavailable. No microbial mechanism, criticality designation or industrial deployment is inherited from a constituent element.

| Record | Final scientific review |
|---|---|
| [Mcallisterite](../../data/records/mcallisterite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061128Z-mcallisterite-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061128Z-mcallisterite-round113-independent/review.yaml)) |
| [Tunellite](../../data/records/tunellite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061128Z-tunellite-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061128Z-tunellite-round113-independent/review.yaml)) |
| [Kukharenkoite-(Ce)](../../data/records/kukharenkoite-ce.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061142Z-kukharenkoite-ce-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061142Z-kukharenkoite-ce-round113-independent/review.yaml)) |
| [Cordylite-(Ce)](../../data/records/cordylite-ce.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061142Z-cordylite-ce-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061142Z-cordylite-ce-round113-independent/review.yaml)) |
| [Billietite](../../data/records/billietite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061124Z-billietite-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061124Z-billietite-round113-independent/review.yaml)) |
| [Compreignacite](../../data/records/compreignacite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061128Z-compreignacite-round113-independent/review.md) ([YAML](../../reviews/structured/20261016T061128Z-compreignacite-round113-independent/review.yaml)) |
| [Zinc purification hot filter cake](../../data/records/zinc-purification-hot-filter-cake.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061101Z-zinc-purification-hot-filter-cake-round113-final/review.md) ([YAML](../../reviews/structured/20261016T061101Z-zinc-purification-hot-filter-cake-round113-final/review.yaml)) |
| [Aluminium salt slag](../../data/records/aluminium-salt-slag.yaml) | [pass_with_limitations](../../reviews/structured/20261016T061101Z-aluminium-salt-slag-round113-final/review.md) ([YAML](../../reviews/structured/20261016T061101Z-aluminium-salt-slag-round113-final/review.yaml)) |

Mcallisterite and tunellite retain distinct natural/synthetic and heating arms, including historical product uncertainty. Kukharenkoite-(Ce) and cordylite-(Ce) retain natural-specimen chemistry and structural-model limits. Billietite surface relief is not bulk recovery; compreignacite separates K/Na specimens, natural/synthetic hydration and modeled rates. Zinc hot filter cake and aluminium salt slag retain their distinct process origins and source-specific laboratory results.

## Corrections and evidence gaps

- [#476](https://github.com/CultureBotAI/CMMMech/issues/476): corrected billietite solution volume versus vessel capacity.
- [#480](https://github.com/CultureBotAI/CMMMech/issues/480): acknowledged the salt-slag paper’s scaled mass balance and separated it from demonstrated throughput.
- The two initial observations remain immutable; exact linked successors resolve both findings. GitHub closure remains pending merge.
- A source-inventory-only borate dossier correction changed the deferred 2019 figure count from 1–5 to 1–4; owner/history bytes were unaffected and final review captures corrected context.

Remaining priorities: [#477 borate evidence](https://github.com/CultureBotAI/CMMMech/issues/477), [#478 uranium source reconciliation](https://github.com/CultureBotAI/CMMMech/issues/478), and [#479 salt-slag/HFC expansion](https://github.com/CultureBotAI/CMMMech/issues/479). The acquired 2026 salt-slag original is ready for detailed assessment; unavailable fungal HFC methods remain deferred.

## Checks and provenance

Final `just check`, `validate --require-records`, trusted-base history validation and page freshness checks passed on unchanged record bytes. The batch contains 578 records and 657 history sessions; 674 structured observations include 114 distinct bases. Canonical review validation and whole-corpus exact-byte coverage are separate publication gates. No schema or validator behavior changed.

Source dossiers:
- [round113-resources-20261016.json](../../research/ingests/round113-resources-20261016.json)
- [round113-resources-20261016.md](../../research/ingests/round113-resources-20261016.md)
- [20261016T060107Z-source-investigation.json](../../research/sources/round113-borates/20261016T060107Z-source-investigation.json)
- [20261016T060107Z-source-investigation.md](../../research/sources/round113-borates/20261016T060107Z-source-investigation.md)
- [20261016T060000Z-source-investigation.json](../../research/sources/round113-ree/20261016T060000Z-source-investigation.json)
- [20261016T060000Z-source-investigation.md](../../research/sources/round113-ree/20261016T060000Z-source-investigation.md)
- [20261016T060054Z-source-investigation.json](../../research/sources/round113-uranium/20261016T060054Z-source-investigation.json)
- [20261016T060054Z-source-investigation.md](../../research/sources/round113-uranium/20261016T060054Z-source-investigation.md)
- [20261016T060441Z-curation-correction.json](../../research/sources/round113-uranium/20261016T060441Z-curation-correction.json)
- [20261016T060441Z-curation-correction.md](../../research/sources/round113-uranium/20261016T060441Z-curation-correction.md)

CLAW admission/history/governed artifacts are installed. The live integration check found 22 matching governed files and the native SQUASH/ALLGREEN queue. PR shepherd remains manual/comment-only with no returned runs. Future integration must use CLAW’s supported admission/synchronization process.

This is a bounded batch, not source exhaustion. Commit/push, live PR review, queue execution, merge, post-deletion fresh-clone checks and branch cleanup are documented in publication receipts after they occur.
