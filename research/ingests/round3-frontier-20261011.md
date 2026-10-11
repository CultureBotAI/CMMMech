# Round 3 frontier and disposition snapshot

Created 2026-10-11T04:42:52Z by Codex (GPT-6; `cmm3_chromium`). Local working-tree reconciliation above `5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da` on `curate/cmm-expansion-round3-20261011`. **No new web search or evidence acquisition was performed.**

The [historical authority inventory](../sources/expansion-authorities/20261011T040103Z.json) remains unchanged (SHA-256 `fb5cc04b2a937a82571511a712eeb646b577f2bae9ec3f0c2837852d00e69e69`). Its 94 provisional candidate keys arose from 268 designations across six jurisdictions and nine list roles; this snapshot updates only their disposition against current record identities.

## Coverage at this file state

| Measure | Count |
|---|---:|
| Current root records | 21 |
| Elements / mineral species / secondary resources | 18 / 2 / 1 |
| Records already present at current HEAD / new working additions | 17 / 4 |
| Historical candidates: elements / commodity proposals | 64 / 30 |
| Candidate identities represented at current HEAD / current working tree | 14 / 18 |
| Newly represented since historical snapshot (which had 7) | 11 |
| Still unrepresented proposals: elements / commodities | 46 / 30 |
| Total unrepresented provisional proposals | 76 |

The four new working-tree elements are cadmium, chromium, platinum and selenium. These counts do not claim their publication is complete. The three existing roots outside the 94-key authority inventory are cobaltite, monazite-(Nd) and spent fluorescent-lamp phosphor. They remain distinct mineral/resource records and are not counted as substitute element or commodity roots.

An element record does not represent a battery-grade commodity, material group, host mineral or secondary resource. For example, lithium/manganese/nickel do not close their battery-grade proposals; neodymium does not close REE groups or permanent-magnet materials; palladium and platinum do not close the PGM commodity group. An exact element match also does not imply every proposed jurisdiction, list edition or mechanism is already curated.

## Ranked next actions

Ranking is a practical evidence-readiness and coverage judgment, not a numerical scientific confidence score. Sources below are existing dossiers; their stated acquisition/evidence states are not fresh verification in this pass.

| Rank | Target | Evidence state and acceptance gate |
|---:|---|---|
| 1 | GaAs-production hydroxide sludge (potential new secondary resource) | Existing round2 dossier reports full primary experiment inspected; resource record not curated. This snapshot did not re-read remote evidence. Define specific manufacturing stream, feed preparation/composition and analytical fractions; preserve abiotic control and assay-date limits; no inherited Ga/As criticality or invented measured As valence. Sources: [round2-gallium-arsenic-20261011](round2-gallium-arsenic-20261011.md) |
| 2 | Chalcopyrite and sphalerite (potential new mineral species) | Selected Cu/Zn mechanism dossiers exist; exact current IMA rows remain deferred. Read dated IMA row and field dictionary, formula and approved status; distinguish species from impure concentrate and avoid claiming reused studies are independent replications or transferring element criticality. Sources: [expansion-copper-20261011](expansion-copper-20261011.md), [round2-zinc-20261011](round2-zinc-20261011.md) |
| 3 | Antimony from USGS BES release (potential new element) | Historical BES dossier explicitly defers As/Sb/Cr decisions; Sb-specific source cells/controls have not been accepted. Verify Sb identity, exact source keys, arms, censoring, fractions, dates and controls; do not inherit U/V conclusions, convert density, or call electrode association isolated recovery. Sources: [bes-evidence](bes-evidence.md), [20261009T054507Z-followup](20261009T054507Z-followup.md) |
| 4 | Phosphorus, iron, germanium and individual unrepresented REEs (new element primary evidence search) | Authority inventory priorities, not verified new microbial experiments. Existing Nd/lamp evidence cannot supply element-specific outcomes for all REEs. Verify each identifier, dated designation and exact primary organism/substrate/condition/outcome; keep phosphorus versus phosphate, iron versus high-purity ore, and individual REEs versus group commodities separate. Sources: [20261011T040103Z](../sources/expansion-authorities/20261011T040103Z.md), [ree-evidence](ree-evidence.md) |
| 5 | Alternative platinum mechanisms (existing record enrichment) | Source leads identified in the Pt dossier; full acquisition/assay interpretation remains incomplete. Acquire full methods, figures and supplements; separate donor-dependent abiotic reduction, viable-community role, analytical preparation and product phase; no cross-study performance pooling. Sources: [round3-platinum-20261011](round3-platinum-20261011.md) |
| 6 | Selenium, chromium and cadmium mechanism extensions (existing record enrichment) | Mixed abstract/indexed or partial-main-text leads only; no additional measurements accepted by this snapshot. Inspect complete primary evidence and controls; investigate anomalous units or unreplicated fits; distinguish immobilization/transformations from recovery and avoid extrapolating taxa. Sources: [round3-selenium-20261011](round3-selenium-20261011.md), [round3-chromium-20261011](round3-chromium-20261011.md), [round3-cadmium-20261011](round3-cadmium-20261011.md) |

GaAs sludge, chalcopyrite and sphalerite are additional concepts outside the historical 94-key candidate list. Antimony is a potential new element ingest; As/Cr from that same BES release would be existing-root enrichment. Later Pt/Se/Cr/Cd studies likewise enrich existing roots rather than increase material counts. No uninspected source lead is promoted to an accepted mechanism.

## Complete candidate reconciliation

| Candidate key | Proposed kind | Disposition | Exact root / related element only |
|---|---|---|---|
| `alumina` | commodity | Unrepresented | Identity/evidence assessment needed |
| `aluminium` | element | Unrepresented | Identity/evidence assessment needed |
| `antimony` | element | Unrepresented | Identity/evidence assessment needed |
| `arsenic` | element | Represented | [cmmmech:arsenic](../../data/records/arsenic.yaml) |
| `baryte` | commodity | Unrepresented | Identity/evidence assessment needed |
| `bauxite` | commodity | Unrepresented | Identity/evidence assessment needed |
| `beryllium` | element | Unrepresented | Identity/evidence assessment needed |
| `bismuth` | element | Unrepresented | Identity/evidence assessment needed |
| `borates` | commodity | Unrepresented | Identity/evidence assessment needed |
| `boron` | element | Unrepresented | Identity/evidence assessment needed |
| `boron-metallurgy-grade` | commodity | Unrepresented | Identity/evidence assessment needed |
| `cadmium` | element | Represented | [cmmmech:cadmium](../../data/records/cadmium.yaml) |
| `cerium` | element | Unrepresented | Identity/evidence assessment needed |
| `cesium` | element | Unrepresented | Identity/evidence assessment needed |
| `chromium` | element | Represented | [cmmmech:chromium](../../data/records/chromium.yaml) |
| `cobalt` | element | Represented | [cmmmech:cobalt](../../data/records/cobalt.yaml) |
| `coking-coal` | commodity | Unrepresented | Identity/evidence assessment needed |
| `copper` | element | Represented | [cmmmech:copper](../../data/records/copper.yaml) |
| `dysprosium` | element | Unrepresented | Identity/evidence assessment needed |
| `erbium` | element | Unrepresented | Identity/evidence assessment needed |
| `europium` | element | Unrepresented | Identity/evidence assessment needed |
| `feldspar` | commodity | Unrepresented | Identity/evidence assessment needed |
| `fluorine` | element | Unrepresented | Identity/evidence assessment needed |
| `fluorspar` | commodity | Unrepresented | Identity/evidence assessment needed |
| `gadolinium` | element | Unrepresented | Identity/evidence assessment needed |
| `gallium` | element | Represented | [cmmmech:gallium](../../data/records/gallium.yaml) |
| `germanium` | element | Unrepresented | Identity/evidence assessment needed |
| `graphite` | commodity | Unrepresented | Identity/evidence assessment needed |
| `graphite-battery-grade` | commodity | Unrepresented | Identity/evidence assessment needed |
| `hafnium` | element | Unrepresented | Identity/evidence assessment needed |
| `heavy-rare-earth-elements` | commodity | Unrepresented | Identity/evidence assessment needed |
| `helium` | element | Unrepresented | Identity/evidence assessment needed |
| `high-purity-alumina` | commodity | Unrepresented | Identity/evidence assessment needed |
| `high-purity-iron-ore` | commodity | Unrepresented | Identity/evidence assessment needed |
| `holmium` | element | Unrepresented | Identity/evidence assessment needed |
| `indium` | element | Unrepresented | Identity/evidence assessment needed |
| `iridium` | element | Unrepresented | Identity/evidence assessment needed |
| `iron` | element | Unrepresented | Identity/evidence assessment needed |
| `lanthanum` | element | Unrepresented | Identity/evidence assessment needed |
| `lead` | element | Unrepresented | Identity/evidence assessment needed |
| `light-rare-earth-elements` | commodity | Unrepresented | Related only: cmmmech:neodymium |
| `lithium` | element | Represented | [cmmmech:lithium](../../data/records/lithium.yaml) |
| `lithium-battery-grade` | commodity | Unrepresented | Related only: cmmmech:lithium |
| `lutetium` | element | Unrepresented | Identity/evidence assessment needed |
| `magnesite` | commodity | Unrepresented | Identity/evidence assessment needed |
| `magnesium` | element | Unrepresented | Identity/evidence assessment needed |
| `magnesium-metal` | commodity | Unrepresented | Identity/evidence assessment needed |
| `manganese` | element | Represented | [cmmmech:manganese](../../data/records/manganese.yaml) |
| `manganese-battery-grade` | commodity | Unrepresented | Related only: cmmmech:manganese |
| `metallurgical-coal` | commodity | Unrepresented | Identity/evidence assessment needed |
| `molybdenum` | element | Unrepresented | Identity/evidence assessment needed |
| `natural-graphite` | commodity | Unrepresented | Identity/evidence assessment needed |
| `neodymium` | element | Represented | [cmmmech:neodymium](../../data/records/neodymium.yaml) |
| `nickel` | element | Represented | [cmmmech:nickel](../../data/records/nickel.yaml) |
| `nickel-battery-grade` | commodity | Unrepresented | Related only: cmmmech:nickel |
| `niobium` | element | Unrepresented | Identity/evidence assessment needed |
| `osmium` | element | Unrepresented | Identity/evidence assessment needed |
| `palladium` | element | Represented | [cmmmech:palladium](../../data/records/palladium.yaml) |
| `phosphate` | commodity | Unrepresented | Identity/evidence assessment needed |
| `phosphate-rock` | commodity | Unrepresented | Identity/evidence assessment needed |
| `phosphorus` | element | Unrepresented | Identity/evidence assessment needed |
| `platinum` | element | Represented | [cmmmech:platinum](../../data/records/platinum.yaml) |
| `platinum-group-commodities` | commodity | Unrepresented | Related only: cmmmech:palladium, cmmmech:platinum |
| `potash` | commodity | Unrepresented | Identity/evidence assessment needed |
| `praseodymium` | element | Unrepresented | Identity/evidence assessment needed |
| `promethium` | element | Unrepresented | Identity/evidence assessment needed |
| `rare-earth-element-commodities` | commodity | Unrepresented | Related only: cmmmech:neodymium |
| `rare-earth-permanent-magnet-materials` | commodity | Unrepresented | Related only: cmmmech:neodymium |
| `rhenium` | element | Unrepresented | Identity/evidence assessment needed |
| `rhodium` | element | Unrepresented | Identity/evidence assessment needed |
| `rubidium` | element | Unrepresented | Identity/evidence assessment needed |
| `ruthenium` | element | Unrepresented | Identity/evidence assessment needed |
| `samarium` | element | Unrepresented | Identity/evidence assessment needed |
| `scandium` | element | Unrepresented | Identity/evidence assessment needed |
| `selenium` | element | Represented | [cmmmech:selenium](../../data/records/selenium.yaml) |
| `silicon` | element | Unrepresented | Identity/evidence assessment needed |
| `silicon-metal` | commodity | Unrepresented | Identity/evidence assessment needed |
| `silver` | element | Represented | [cmmmech:silver](../../data/records/silver.yaml) |
| `sodium-compounds` | commodity | Unrepresented | Identity/evidence assessment needed |
| `strontium` | element | Unrepresented | Identity/evidence assessment needed |
| `tantalum` | element | Unrepresented | Identity/evidence assessment needed |
| `tellurium` | element | Represented | [cmmmech:tellurium](../../data/records/tellurium.yaml) |
| `terbium` | element | Unrepresented | Identity/evidence assessment needed |
| `thulium` | element | Unrepresented | Identity/evidence assessment needed |
| `tin` | element | Unrepresented | Identity/evidence assessment needed |
| `titanium` | element | Unrepresented | Identity/evidence assessment needed |
| `titanium-metal` | commodity | Unrepresented | Identity/evidence assessment needed |
| `tungsten` | element | Unrepresented | Identity/evidence assessment needed |
| `uranium` | element | Represented | [cmmmech:uranium](../../data/records/uranium.yaml) |
| `vanadium` | element | Represented | [cmmmech:vanadium](../../data/records/vanadium.yaml) |
| `ytterbium` | element | Unrepresented | Identity/evidence assessment needed |
| `yttrium` | element | Unrepresented | Identity/evidence assessment needed |
| `zinc` | element | Represented | [cmmmech:zinc](../../data/records/zinc.yaml) |
| `zirconium` | element | Unrepresented | Identity/evidence assessment needed |

## Search and interpretation limits

Local inventories and searches used `rg --no-ignore --hidden` across records, research, reviews and history, including ignored and hidden files. All current record YAML files were parsed; `find data research reviews history -type l` returned no symlinks. Searches/readbacks of current dossiers covered identity, DOI and next-action references. No unrelated home or temporary trees were searched for this reconciliation, and no raw scientific source was rechecked here. The JSON records every current root hash, historical designation links, original candidate mapping notes and dossier input hashes.

The 76 unrepresented proposals are **not 76 automatic additions**: grades, overlapping names and group concepts require identity adjudication, and source membership alone does not establish microbial evidence. Remaining jurisdictions, citation chains, mineral hosts and secondary resources keep discovery open. This snapshot does not establish that no new CMMs remain.

Local checks: JSON parsed; 94 candidate keys unique; all 21 YAML roots parsed; 18 exact element matches; 76 residual proposals partition into 46 elements and 30 commodities; historical inventory bytes unchanged. No schema, record, historical review or governance file was modified by this snapshot.
