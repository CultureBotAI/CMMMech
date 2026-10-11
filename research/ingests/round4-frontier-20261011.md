# Fourth expansion frontier

This local reconciliation is based on `c081a749cd63feafcc25414f5ad006d1f78f1e36`
plus the six round4 working-tree records. Exact creation time, prior-snapshot
hash, all current record hashes and remaining candidate keys/designation
references are in [the JSON snapshot](round4-frontier-20261011.json).
The historical authority inventory and earlier frontier snapshots are unchanged.

There are **27 records: 21 elements, 4 mineral species and 2 secondary
resources**. The historical inventory proposed 94 keys (64 elements and 30
commodities). Exact element-root matching now represents 21; **73 proposals
remain unrepresented: 43 elements and 30 commodities**. The six mineral/resource
roots are outside that inventory. These are scope counts, not counts of independent
studies, accepted commodity classes, or fully curated jurisdiction designations.

Record enumeration used `rg --files --hidden --no-ignore data/records` and parsed
every YAML returned. Related source/review/history searches also included hidden
and ignored files. Boundaries are this worktree and cited task downloads, not all
home/temp paths or all possible literature. Exact IDs and kinds were matched;
an element never substitutes for an ore grade, mineral species or waste stream.

## Prioritized next work

1. **Iron, germanium and individual REEs still absent from the corpus.** Start
   from the [authority inventory](../sources/expansion-authorities/20261011T040103Z.md)
   and inspect primary microbial experiments. Resolve elemental iron separately
   from high-purity iron ore, and individual REEs separately from group commodities.
   Existing cerium or neodymium experiments cannot supply outcomes for every REE.
2. **Phosphorus enrichment and possible magnesium outcome.** Inspect
   [Suyamud2020](https://doi.org/10.1111/1462-2920.14949) full methods, figures,
   controls and supplement. The [P/Ce dossier](round4-phosphorus-cerium-20261011.md)
   retains this as an indexed primary lead, not accepted extra measurements.
   Different media and magnesium oxalate precipitation require separate claims.
3. **Resource and commodity concept decisions.** Adjudicate the 30 overlapping
   commodity proposals before adding roots. New waste streams need exact origin,
   characterization and mechanisms; new mineral species need authority grounding.
   Existing GaAs sludge and mineral-host studies are shared with elemental records.
4. **Antimony follow-up.** The [dossier](round4-antimony-20261011.md) explains why
   the original USGS BES lead cannot inherit U/V microbial conclusions. Resolve
   its arm/date/speciation gaps before accepting cells. For the accepted sediment
   experiment, resolve lactate recipe inconsistency and obtain evidence that
   distinguishes candidate Sb(III) phases before broadening mechanism claims.
5. **Existing records with unresolved primary evidence.** The newly accessible
   GaAs-sludge supplement can inform future Ga/As enrichment; its higher-loading
   arsenic counterevidence does not rewrite historical review access states.
   Selenium, cadmium, chromium and platinum extension leads in the
   [round3 frontier](round3-frontier-20261011.md) still require their stated checks.

This is a bounded, reproducible queue. It does not establish that no new CMMs
remain or authorize automatic bulk imports of the outstanding proposals.
