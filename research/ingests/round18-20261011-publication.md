# Round 18 reviewed rock, mineral, catalyst and manganese-product records

Worktree: `/private/tmp/CMMMech-expansion-round18-20261011`.
Branch: `curate/cmm-expansion-round18-20261011`.
Trusted base: `26cb0688effb2f71e4a570c416f6f43ff858c5ab`.
Acceptance: [issue #68](https://github.com/CultureBotAI/CMMMech/issues/68).

Six additions bring the corpus to **138 records**. Dunite is a geological primary
resource; hematite a mineral species; potassium feldspar an explicitly informal
mineral family; spent diesel-hydrodesulfurization catalyst a secondary resource;
and electrolytic manganese metal/dioxide manufactured commodities. No constituent
criticality or industrial microbial deployment is inferred. Every addition has
a genuine CREATE sidecar and a distinct inline event.

## Independent scientific reviews

| Record | Kind | Final exact-state review |
|---|---|---|
| [Dunite](../../data/records/dunite.yaml) | primary_resource | [YAML](../../reviews/structured/20261011T112143Z-dunite-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112143Z-dunite-round18-independent/review.md) |
| [Electrolytic manganese dioxide commodity](../../data/records/electrolytic-manganese-dioxide.yaml) | commodity | [YAML](../../reviews/structured/20261011T112033Z-electrolytic-manganese-dioxide-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112033Z-electrolytic-manganese-dioxide-round18-independent/review.md) |
| [Electrolytic manganese metal commodity](../../data/records/electrolytic-manganese-metal.yaml) | commodity | [YAML](../../reviews/structured/20261011T112033Z-electrolytic-manganese-metal-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112033Z-electrolytic-manganese-metal-round18-independent/review.md) |
| [Hematite](../../data/records/hematite.yaml) | mineral | [YAML](../../reviews/structured/20261011T112045Z-hematite-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112045Z-hematite-round18-independent/review.md) |
| [Potassium feldspar family](../../data/records/potassium-feldspar.yaml) | mineral_group | [YAML](../../reviews/structured/20261011T112045Z-potassium-feldspar-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112045Z-potassium-feldspar-round18-independent/review.md) |
| [Spent hydrodesulfurization catalyst](../../data/records/spent-hydrodesulfurization-catalyst.yaml) | secondary_resource | [YAML](../../reviews/structured/20261011T112143Z-spent-hydrodesulfurization-catalyst-round18-independent/review.yaml) · [Markdown](../../reviews/structured/20261011T112143Z-spent-hydrodesulfurization-catalyst-round18-independent/review.md) |


Each reviewer is a different agent from the respective record author. The linked
immutable observations preserve assessed evidence, source limitations and verdicts.
The [manifest](round18-frontier-20261011.json) records exact final hashes and history
references. No actionable scientific finding was identified by these reviews;
source discrepancies are not silently corrected or turned into artificial issues.
Any later actionable publication finding must be resolved before queue admission.

Dunite experiments include strongly altered powders and measured solution release;
initially acid-matched and cell-free comparisons constrain microbial explanations.
Carbon-demand calculations are not measured net sequestration. Hematite and
potassium-feldspar assays share the Dong experiment; the latter measures aluminium,
not potassium release. Bulk oxides do not quantify phase purity, and biotite-specific
molecular results do not establish causality for these other feeds.

The raw diesel-HDS catalyst record uses full Ferreira2017 evidence and preserves
chemical-control nulls, inconsistent source values and unknown comparison details.
Solution release is not isolated-metal recovery. EMM/EMD records establish product
identity only: producer specifications, their conflicts and assay denominators do
not supply universal battery-grade qualification. JRC's historical capacity grouping
does not settle the deferred legal/technical manganese grade boundary.

## Sources and remaining work

- [Dunite dossier](round18-dunite-sources-20261011.md) and [JSON](round18-dunite-sources-20261011.json).
- [Mineral-feed dossier](round18-mineral-feeds-sources-20261011.md) and [JSON](round18-mineral-feeds-sources-20261011.json).
- [Catalyst dossier](round18-catalyst-sources-20261011.md) and [JSON](round18-catalyst-sources-20261011.json).
- [Manganese-product dossier](round18-products-sources-20261011.md) and [JSON](round18-products-sources-20261011.json).
- [Prioritized further ingests](round18-frontier-20261011.md).

Timestamped discovery reports retain bounded hidden/ignored searches, source
versions, actual acquisition records and access limitations. Raw full texts remain
outside Git. Open cross-species dunite, NK851 and manganese-reductant studies, plus
distinct catalyst/residue leads and older full-main gaps, remain concrete work.
This batch does not establish global source or material exhaustion.

## Validation and preservation

Baseline: 308 tests passed, three skipped; 132 records and 148 histories.
Final `just check`: **308 passed, 3 skipped in 86.49s (0:01:26)**; 138 records and 154 histories valid.
Separate `validate --require-records` and trusted-base history checks passed.
No schema or validator behavior changed, so no behavioral regression was added.

Structured review validation passed for 153 pairs. All **138** current records have
independent scientific coverage matching their exact bytes. All **839** earlier
tracked files under `data`, `history`, `reviews` and `research` remain unchanged.
All **19** distinct review bases resolve; the annotated source-survey provenance
tag remains unchanged. New reviews use the already merged trusted base.

All 22 governed artifacts match CLAW pin
`a5d562962c75a2ad9efd8160b548df5944315422`. The live main ruleset remains active
SQUASH/ALLGREEN, requires `validate-strict` from App15368, and has no bypass actors.
Fleet admission and shared history are installed. PR shepherd remains manual and
comment-only; any future expansion requires CLAW's supported process and the
appropriate distinct writer/reviewer identities. No governance or skill changes
are part of this batch.

Independent publication audit, exact-tree squash-shaped verification, required
queue CI and fresh remote-main validation after deletion complete publication.
Terminal receipts will be posted on the PR. Original main advances only after
ignored/untracked and symlink collision checks plus matching before/after snapshots;
unrelated branches and worktrees remain intact.
