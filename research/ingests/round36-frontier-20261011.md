# Remaining evidence priorities after round 36

The source frontier remains open. The [meta-autunite deferral dossier](../sources/round36-meta-autunite/20261011T222742Z-source-deferral.md) records the source-access checks and unresolved visual review. The publication batch contains uramphite and
moolooite. Calcium uranyl-phosphate evidence remains source-only because the
checked routes did not provide inspectable original figures. Acceptance and
review outcomes belong in the accompanying publication report and per-record
dossiers; the leads below are research handoffs, not accepted mechanisms.

| Priority | Candidate or existing owner | Evidence task before curation |
|---|---|---|
| 1 | Meta-autunite | Track [#120](https://github.com/CultureBotAI/CMMMech/issues/120): obtain inspectable original figures for [Smeaton2008](https://doi.org/10.2138/am.2008.2836). Complete text was accessible, but screenshot interfaces omitted image payloads and direct PDF/figure routes returned access errors. Verify the plotted dissolution/oxidation-state and microscopy evidence before admission; no record or CREATE history was made from text alone. |
| 2 | Lindbergite | Inspect complete primary methods, original diffraction figures and supplements for [manganese-nodule transformation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6849720/) and [manganese-oxide/arsenic experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC7711977/). Verify the IMA species, strain, medium, substrate and controls; distinguish product-phase evidence from recovery or environmental stability. |
| 3 | Humboldtine | Acquire and review [Aspergillus niger crystallization](https://www.mdpi.com/2073-4352/11/12/1591) and [brown-rot fungal experiments](https://www.mdpi.com/2073-4352/13/3/432). Keep siderite and pyrrhotite feeds, organism-specific arms, iron oxidation state and oxalate hydrate assignment separate. |
| 4 | Falottaite or other manganese phases | The manganese-oxide/arsenic search lead also names falottaite. Verify current species identity and actual phase measurements before creating another material owner; multiple phases in one experiment do not provide independent replications. |
| 5 | Rhabdophane species | Assess [weathered-granite/methylotroph evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC10875860/), then resolve hydration, dominant rare-earth element, mineral-group versus species identity, and biotic causality. The existing neodymium record already describes a mixed monazite-Nd/rhabdophane-Nd feed from a different study; deduplicate experiment claims as well as names. |
| Carry forward | Existing ningyoite, anglesite, galena, jarosite and schwertmannite | The [round35 frontier](round35-frontier-20261011.md) retains additional full-primary and supplement-acquisition tasks. A new record for a related phase does not close those evidence gaps. |
| Access queue | Tungsten mining waste and ilmenite | [#103](https://github.com/CultureBotAI/CMMMech/issues/103) and [#104](https://github.com/CultureBotAI/CMMMech/issues/104) remain acquisition and reconciliation tasks; no abstract-only mechanism is admitted. |

## Search coverage and limits

The coordinator's 2026-10-11 discovery queries were:

- `lindbergite manganese oxalate microbial fungi biomineralization primary study`
- `humboldtine fungal formation iron oxalate biomineralization Aspergillus primary study`
- `microbial biomineralization rhabdophane lanthanite rare earth phosphate mineral primary study`
- `critical minerals microbial bioleaching new mineral resources data full text 2025 2026`

These returned titles, metadata and snippets for the leads above. They do not
constitute full scientific assessment. The broad fourth query also returned
secondary and irrelevant material, which is not evidence for an accepted record.

A bounded search at 2026-10-11T22:18:55Z used `rg --no-ignore --hidden --follow`
across this worktree's `data`, `research`, `reviews` and `history` for the four
candidate names, falottaite, and the cited PMC/article identifiers. It found the
existing mixed rhabdophane-Nd context in neodymium and its earlier research and
reviews. No lindbergite, humboldtine or falottaite match occurred within those
boundaries, including hidden and ignored files. This does not assert absence
from unsearched external downloads or the literature. The local search receipt
is `/private/tmp/cmm-round36-frontier-dedup.json`; output SHA256 is
`f8c475c7bea384bcabd247a81dca1038a25c9f83fb731636b50582d945055a00`.

Before an addition, repeat identity and experiment deduplication, including
referenced downloads and relevant symlinks; verify authoritative identifiers;
read full primary evidence and relevant supplements; and use the add-record and
independent record-review skills. Preserve abiotic outcomes, uncertain phase
assignments and differences between solution change, mineral formation and
isolated product recovery. No exhaustive material or source coverage is claimed.
