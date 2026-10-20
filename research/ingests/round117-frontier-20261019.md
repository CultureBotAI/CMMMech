# Round117: fourteen critical material commodity and mineral records

Prepared 2026-10-19T05:35:00+00:00; trusted base `e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34`.

The batch adds fourteen primary-source-verified CMM records across two categories (`3` commodities and `11` minerals), expanding the corpus from `602` to `616` records (`744` canonical history sidecars, `714` structured review bundles):
- **DOE 2023 Critical Material & USGS 2026 Manufactured Commodities (`3`)**: [Electrical steel](../../data/records/electrical-steel.yaml), [Silicon carbide](../../data/records/silicon-carbide.yaml), and [Synthetic graphite](../../data/records/synthetic-graphite.yaml), completing explicit commodity coverage of every U.S. DOE 2023 Critical Material (88 FR 51792) and major USGS Mineral Commodity Summaries 2026 manufactured critical material commodity.
- **REE Carbonate Minerals (`5`)**: [Bainbridgeite-(NdCe)](../../data/records/bainbridgeite-ndce.yaml), [Piilonenite-(Nd)](../../data/records/piilonenite-nd.yaml), [Mckelveyite-(Y)](../../data/records/mckelveyite-y.yaml), [Adamsite-(Y)](../../data/records/adamsite-y.yaml), and [Thomasclarkite-(Y)](../../data/records/thomasclarkite-y.yaml).
- **Indium- & Tin-Bearing Sulfide Minerals (`3`)**: [Petrukite](../../data/records/petrukite.yaml), [Ferrokesterite](../../data/records/ferrokesterite.yaml), and [Sakuraiite](../../data/records/sakuraiite.yaml).
- **Borate & Uranyl Minerals (`3`)**: [Ammonioborite](../../data/records/ammonioborite.yaml), [Weeksite](../../data/records/weeksite.yaml), and [Richetite](../../data/records/richetite.yaml).

Complete primary studies support seven abiotic mechanisms across six owners: high-temperature Acheson carbothermic synthesis for silicon carbide, ~3,000 °C petroleum-coke graphitization for synthetic graphite, laboratory TGA/DTG dehydration and partial decarbonation for adamsite-(Y), laboratory TG/DTG dehydration and decarbonation for thomasclarkite-(Y), stepwise thermal dehydration holds and Larderello boric-acid liquor conversion for ammonioborite, and reversible thermal dehydration versus >500 °C decomposition for weeksite. No constituent criticality, microbial causation, or unmeasured industrial recovery yield is inferred.

| Record | Structured scientific review |
|---|---|
| [Electrical steel](../../data/records/electrical-steel.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-electrical-steel-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-electrical-steel-round117/review.yaml) |
| [Silicon carbide](../../data/records/silicon-carbide.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-silicon-carbide-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-silicon-carbide-round117/review.yaml) |
| [Synthetic graphite](../../data/records/synthetic-graphite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-synthetic-graphite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-synthetic-graphite-round117/review.yaml) |
| [Bainbridgeite-(NdCe)](../../data/records/bainbridgeite-ndce.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-bainbridgeite-ndce-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-bainbridgeite-ndce-round117/review.yaml) |
| [Piilonenite-(Nd)](../../data/records/piilonenite-nd.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-piilonenite-nd-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-piilonenite-nd-round117/review.yaml) |
| [Mckelveyite-(Y)](../../data/records/mckelveyite-y.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-mckelveyite-y-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-mckelveyite-y-round117/review.yaml) |
| [Adamsite-(Y)](../../data/records/adamsite-y.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-adamsite-y-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-adamsite-y-round117/review.yaml) |
| [Thomasclarkite-(Y)](../../data/records/thomasclarkite-y.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-thomasclarkite-y-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-thomasclarkite-y-round117/review.yaml) |
| [Petrukite](../../data/records/petrukite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-petrukite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-petrukite-round117/review.yaml) |
| [Ferrokesterite](../../data/records/ferrokesterite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-ferrokesterite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-ferrokesterite-round117/review.yaml) |
| [Sakuraiite](../../data/records/sakuraiite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-sakuraiite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-sakuraiite-round117/review.yaml) |
| [Ammonioborite](../../data/records/ammonioborite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-ammonioborite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-ammonioborite-round117/review.yaml) |
| [Weeksite](../../data/records/weeksite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-weeksite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-weeksite-round117/review.yaml) |
| [Richetite](../../data/records/richetite.yaml) | [Markdown](../../reviews/structured/20261019T053000Z-richetite-round117/review.md) · [YAML](../../reviews/structured/20261019T053000Z-richetite-round117/review.yaml) |

## Review and source boundaries

Every record was curated after full-text visual inspection of the primary mineralogical, metallurgical, and statutory authority PDFs:
- `electrical-steel`, `silicon-carbide`, and `synthetic-graphite` separate DOE 2023 Critical Material for Energy status (`criticality_sources`) from non-critical elemental iron/silicon (`cmmmech:iron`, `cmmmech:silicon`), natural moissanite (`cmmmech:moissanite`), and natural graphite (`cmmmech:graphite`).
- `bainbridgeite-ndce` preserves the triclinic `P1` weloganite-type structure (`Na2Ba2NdCe(CO3)6·3H2O`, holotype `CMNMC 90534` and hornfels `CMNMC 52468`) with `Ce, La, Pr` partitioned at 10-coordinated `Ce3` and `Nd, Sm, Gd, Y` at 9-coordinated `Nd6`.
- `piilonenite-nd` preserves the orthorhombic `P212121` synchrotron refinement on holotype `CMNMC 93393` (`IMA:2025-031` vs master list `2025-031b`) and stoichiometric `CO2/H2O` calculation.
- `mckelveyite-y` preserves the 1965 original Wyoming pseudo-trigonal description (`P31m`) alongside the Demartin et al. (2008) single-crystal `P1` triclinic structural solution of the `-1M` polytype (`CMNMC 85686`) and `-2M` polytype (`MCSNM 37812`).
- `adamsite-y` and `thomasclarkite-y` preserve the Mont Saint-Hilaire cotype structures (`P-1` and `P2`) and bounded `N2` TGA/DTG thermal dehydration and decarbonation steps.
- `petrukite`, `ferrokesterite`, and `sakuraiite` preserve the Kissin & Owens (1989) and Shimizu et al. (1986) structural and compositional boundaries between orthorhombic `Pmn21` petrukite, low-temperature `I-4` ferrokësterite, high-temperature `I-42m` stannite, and `(Cu,Zn,Fe)3(In,Sn)S4` sakuraiite.
- `ammonioborite` preserves both the Schaller (1933) `3B2O3` oxide-ratio formula (with stepwise dehydration holds and Larderello crystallizer conversion) and the Merlino & Sartori (1971) / IMA 1999 `[B15O20(OH)8]3-` pentadecaborate polyanion revision.
- `weeksite` and `richetite` preserve natural/modern IMA stoichiometry and single-crystal refinement limits (`K2(UO2)2(Si5O13)·4H2O` vs 1960 `6SiO2`; triclinic `P1` richetite with disordered interlayer `Pb2+` and `M(1)/M(2)` sites).

## Validation and provenance

`PYTHONPATH=src .venv/bin/python -m cmmmech validate --require-records` (`Checked 616 record(s); 0 failed`), `PYTHONPATH=src .venv/bin/python -m cmmmech validate-history --base e4e32f5e7dd8bca8e1cd86557db5bbb8c53dea34` (`Checked 744 history record(s); 0 error(s)`), `.venv/bin/python scripts/record_review.py validate` (`{"valid_reviews": 14}`), `PYTHONPATH=src .venv/bin/python scripts/render_pages.py --check`, `.venv/bin/ruff check .`, and `PYTHONPATH=src .venv/bin/pytest` pass with 0 errors.

## Source dossiers

- [20261019T052500Z-source-investigation.json](../../research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.json)
- [20261019T052500Z-source-investigation.md](../../research/sources/round117-commodities-and-minerals/20261019T052500Z-source-investigation.md)
