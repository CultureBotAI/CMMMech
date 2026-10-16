# Round114: eight independently reviewed mineral records

Prepared 2026-10-16T07:19:29.680373+00:00; trusted base `93f90797512dc8d1db3df9ce2e4994c475b1a4fe`.

The batch adds eight mineral species: two borates, two rare-earth carbonates, two uranium minerals and two titanium-bearing minerals. Primary evidence supports bounded abiotic observations for kaliborite, curite, vandenbrandeite and ilmenite; the other four records remain identity-only. No constituent-element criticality, microbial mechanism or industrial recovery is inferred.

| Record | Final scientific review |
|---|---|
| [Kaliborite](../../data/records/kaliborite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071745Z-kaliborite-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071745Z-kaliborite-round114-independent/review.yaml)) |
| [Preobrazhenskite](../../data/records/preobrazhenskite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071745Z-preobrazhenskite-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071745Z-preobrazhenskite-round114-independent/review.yaml)) |
| [Ancylite-(Ce)](../../data/records/ancylite-ce.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071741Z-ancylite-ce-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071741Z-ancylite-ce-round114-independent/review.yaml)) |
| [Calcioancylite-(La)](../../data/records/calcioancylite-la.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071741Z-calcioancylite-la-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071741Z-calcioancylite-la-round114-independent/review.yaml)) |
| [Curite](../../data/records/curite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071832Z-curite-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071832Z-curite-round114-independent/review.yaml)) |
| [Vandenbrandeite](../../data/records/vandenbrandeite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071840Z-vandenbrandeite-round114-independent/review.md) ([YAML](../../reviews/structured/20261016T071840Z-vandenbrandeite-round114-independent/review.yaml)) |
| [Ilmenite](../../data/records/ilmenite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071735Z-ilmenite-round114-final/review.md) ([YAML](../../reviews/structured/20261016T071735Z-ilmenite-round114-final/review.yaml)) |
| [Perovskite](../../data/records/perovskite.yaml) | [pass_with_limitations](../../reviews/structured/20261016T071736Z-perovskite-round114-final/review.md) ([YAML](../../reviews/structured/20261016T071736Z-perovskite-round114-final/review.yaml)) |

## Corrections and remaining evidence

Independent review found incorrect preobrazhenskite source locators. [#485](https://github.com/CultureBotAI/CMMMech/issues/485) is corrected with an actual EDIT session; the immutable initial finding and exact linked resolving successor are retained. The figure/table correction does not change the supported mineral identity. The first batch run began before this correction and is not the final-byte authorization; the corrected batch was checked separately. Separate operational finding [#486](https://github.com/CultureBotAI/CMMMech/issues/486), PUB114-1, is fixed by binding cleanup configuration to the commit receipt before issue reads and branch deletion; four inert checks independently verify it. Both immutable helper audits preserve the initial snapshot race and its explicit provenance correction.

Source priorities remain: [#482](https://github.com/CultureBotAI/CMMMech/issues/482) borate thermal/hydrogen discrepancies, [#483](https://github.com/CultureBotAI/CMMMech/issues/483) calcioancylite chemistry and deposit reconciliation, [#484](https://github.com/CultureBotAI/CMMMech/issues/484) uranium assay/thermal source gaps, and existing [#104](https://github.com/CultureBotAI/CMMMech/issues/104) ilmenite microbial full-text reconciliation. The accepted acid-dissolution study does not close the microbial question. Full-text fungal enrichment evidence remains insufficient for causal recovery and is described in the titanium dossier.

## Validation and provenance

Corrected `just check`, `validate --require-records`, trusted-base history validation and generated-page checks passed on unchanged records. The corpus has 586 records, 666 history sessions and 683 structured observations, including 115 distinct review bases. Every record has a positive scientific review matching its current exact bytes. Canonical review validation and fresh squash-shaped/post-deletion checks are separate publication gates. No schema or validator behavior changed.

Source dossiers:
- [20261016T065455Z-source-investigation.json](../../research/sources/round114-borates/20261016T065455Z-source-investigation.json)
- [20261016T065455Z-source-investigation.md](../../research/sources/round114-borates/20261016T065455Z-source-investigation.md)
- [20261016T065233Z-source-investigation.json](../../research/sources/round114-ree/20261016T065233Z-source-investigation.json)
- [20261016T065233Z-source-investigation.md](../../research/sources/round114-ree/20261016T065233Z-source-investigation.md)
- [20261016T065427Z-source-assessment.json](../../research/sources/round114-titanium/20261016T065427Z-source-assessment.json)
- [20261016T065427Z-source-assessment.md](../../research/sources/round114-titanium/20261016T065427Z-source-assessment.md)
- [20261016T065428Z-source-investigation.json](../../research/sources/round114-uranium/20261016T065428Z-source-investigation.json)
- [20261016T065428Z-source-investigation.md](../../research/sources/round114-uranium/20261016T065428Z-source-investigation.md)

The live integration check confirmed 22 governed files matching the CLAW pin and the native SQUASH/ALLGREEN queue. Admission/history/governance are installed. PR shepherd remains manual/comment-only, with no returned runs; a supported operational exercise remains follow-up. Future integration uses CLAW’s supported admission/synchronization process.

Publication receipts retained after execution will establish PR review, queue admission, exact merged tree, five hosted workflow outcomes, fresh remote-main validation and branch cleanup. The original checkout and hidden/ignored work are preserved.
