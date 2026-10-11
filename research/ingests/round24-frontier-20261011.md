# Round24 source frontier and next ingests

This batch adds four distinct secondary resources: spent sulfuric-acid-production catalyst, copper-smelter slag, coal-mine-drainage treatment solids, and spent nickel-metal-hydride batteries. The [manifest](round24-frontier-20261011.json) records final hashes, actual CREATE history and independent reviews. Source leads below require their own full assessment before acceptance.

**Citation correction ([issue 87](https://github.com/CultureBotAI/CMMMech/issues/87)):** the round23 handoff's 2019 copper-slag DOI `10.3390/min9110542` was incorrect. The verified Potysz/Kierczak primary source is [10.3390/min9090542](https://doi.org/10.3390/min9090542), Minerals 9(9):542. The new record and source dossier use the corrected DOI. The historical report is retained unchanged.

| Priority | Candidate or existing record | Required next evidence | Placement decision |
|---|---|---|---|
| 1 | Blast-furnace cast-house dust | [10.1016/j.bej.2025.109859](https://doi.org/10.1016/j.bej.2025.109859): full primary PDF acquired, initial methods read; inspect all figures, supplementary/feed characterization, cycles and inventories | Candidate new dust resource, distinct from slag and tailings |
| 2 | Heavy-fuel-oil fly ash | [10.1039/C5RA00128E](https://doi.org/10.1039/C5RA00128E), plus traced leads 10.1016/j.wasman.2016.04.004 and 10.1039/C5RA24870A; acquire primary methods and figures | Candidate combustion resource distinct from coal ash and refinery catalysts |
| 3 | Electric-arc-furnace steel slag | [10.1016/j.chemosphere.2014.09.089](https://doi.org/10.1016/j.chemosphere.2014.09.089): acquire complete methods, controls and serial-cycle evidence beyond abstract/preview | Candidate new resource; use as neutralizer does not establish extraction from it |
| 4 | Spent NiMH batteries | [10.1016/j.mineng.2021.107361](https://doi.org/10.1016/j.mineng.2021.107361) and [10.1039/d6ra03345h](https://doi.org/10.1039/d6ra03345h): inspect original figures and supplements; resolve 2026 metal-percentage assignments | Extend the new NiMH root; no abstract-only yields or imported 2021 conditions |
| 5 | Copper-smelter slag | [10.3390/min11030262](https://doi.org/10.3390/min11030262), [10.3390/min14111094](https://doi.org/10.3390/min14111094) and 10.1016/j.hydromet.2015.10.032: finish primary assay/control/figure and mass accounting | Existing-resource extensions; citric-acid fungal mimic is not a fungal experiment |
| 6 | Biogas-plant sulfur residue | [10.3389/fmicb.2026.1921494](https://doi.org/10.3389/fmicb.2026.1921494): metadata-only lead; verify feed identity, acid-generation arm and complete primary experiment | Potential distinct sulfur resource; do not conflate its acid-production role with the battery substrate |
| 7 | Alkaline button-cell batteries and discarded LED lamps | [Battery primary lead](https://www.sciencedirect.com/science/article/abs/pii/S0304386X18309113), [LED primary lead](https://pmc.ncbi.nlm.nih.gov/articles/PMC12216006/): full primary evidence and identity comparison | Candidate resources; distinguish NiMH/LIB, fluorescent phosphors and LCD panels |
| 8 | Earlier retained priorities | LCD pretreatment evidence, automotive catalyst supplements/PGM accounting, manganese B4 taxonomy, marine resource supplements and older deferred assays | See [round23](round23-frontier-20261011.md) and linked earlier frontiers; retain those leads without creating locality-only duplicates |

Source assessments:

- [Sulfuric-acid catalyst](round24-sulfuric-sources-20261011.md), [JSON](round24-sulfuric-sources-20261011.json).
- [Copper-smelter slag](round24-copper-slag-sources-20261011.md), [JSON](round24-copper-slag-sources-20261011.json).
- [Drainage treatment solids and broader identity search](round24-amd-solids-sources-20261011.md), [JSON](round24-amd-solids-sources-20261011.json).
- [NiMH batteries](round24-nimh-sources-20261011.md), [JSON](round24-nimh-sources-20261011.json).

Bounded duplicate searches included hidden/ignored relevant files and followed relevant symlinks. Source availability, contradictory measurements, null controls and unreviewed supplements remain explicit. Raw primary artifacts stay outside Git. Accessible new-resource evidence remains, so this batch is concrete progress, not exhaustion of CMM identities or literature. Continue with the add-record skill and independent exact-state review. Future fleet integration must use CLAW's supported admission and synchronization process.
